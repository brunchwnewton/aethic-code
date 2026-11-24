#!/usr/bin/env python3
"""Step 11: many against one. What the scores say about groups, and what a fight model adds.

Usage:  python3 11_group_mechanics.py [--fights 300000] [--arena]

The scale gives one-on-one odds (Bradley-Terry: a beats b with a / (a + b)) and, from the crowd's votes on its 259
group entries, a rule for numbers: n animals count as n^k one animal, k = 1.44 (step 8). Neither says how a fight
goes. The arena (arena.html) therefore plays every fight with an exchange model, and this step runs that same model
on its own, with nothing pinned to the group rule, to see what it implies for one theropod against several mammals.

The exchange model. A fight is a row of exchanges. In each, one fighter of either side, taken at random, meets one of
the other; one of the two lands a blow, the theropod's side with chance q; a blow takes a fixed share of the
victim's staying power; a side is out when its last fighter is down. For every pairing q is solved so that one
against one the model gives exactly the pair's Bradley-Terry odds. What it then gives for one against n is not fitted
to anything: it follows from how the one-on-one odds are divided between who lands and what a landed blow takes.
Five ways of dividing them ("stagings") are run:

  scores   a blow's size goes by the score ratio to the power 0.4 (the arena's rule until November 2026)
  weights  it goes by the cube root of the weight ratio; what a fighter has beyond its size shows as blows landed
  lunge    weights, and a mammal's landed blow on the theropod counts double (it has had to get inside the reach)
  bite     lunge, and the theropod's bite takes a third of the blow at once and leaves a wound that takes as much
           again with every exchange that follows (the arena's rule now)
  hold     bite, and the mammal's one landed blow decides: a single hold, however long it takes to get

Bleeding runs on the fight's clock: as many exchanges are fought at once as the smaller side has fighters, so one
exchange is that part of a turn. The one-on-one solution is exact (a small tree, by recursion); the group shares are
counted over --fights simulated fights each (standard error about 0.1 points at the default).

Scores are the paper's: the pooled crowd score and its median anatomy-corrected value from final_scores.csv. With
--arena the theropods take the arena's own accurate scores instead (the medians of the full percentiles, a few per
cent lower), to check this step against the page.

Outputs: outputs/group_mechanics.json (every number), outputs/group_mechanics.csv (the table), and LaTeX rows on
standard output for the paper's table."""
import argparse, csv, json, math, os, sys
from functools import lru_cache

import numpy as np

F0, RHO, ETA, LUNGE, BITE_NOW, BITE_RATE = 1 / 3, 0.4, 1 / 3, 2.0, 1 / 3, 1 / 3      # as in arena.html
SEED = 20261124
MASS = {'Dakotaraptor steini': 250, 'Utahraptor ostrommaysorum': 500, 'Tyrannosaurus rex': 8000, 'Allosaurus fragilis': 1700,
        'Deinonychus antirrhopus': 73, 'African Lion': 185, 'Tiger': 220, 'African Bush Elephant': 6000, 'Grey Wolf': 40,
        'Polar Bear': 450}                                                            # kg, as on the paper's charts and in the arena
SHORT = {'Dakotaraptor steini': 'Dakotaraptor', 'Utahraptor ostrommaysorum': 'Utahraptor', 'Tyrannosaurus rex': 'Tyrannosaurus',
         'Allosaurus fragilis': 'Allosaurus', 'Deinonychus antirrhopus': 'Deinonychus', 'African Lion': 'lion', 'Tiger': 'tiger',
         'African Bush Elephant': 'elephant', 'Grey Wolf': 'wolf', 'Polar Bear': 'polar bear'}
PLURAL = {'wolf': 'wolves'}
# (theropods, mammals, the numbers of each): one against n, and two packs
CASES = [('Dakotaraptor steini', 'African Lion', [(1, n) for n in (1, 2, 3, 4, 6, 8)]),
         ('Utahraptor ostrommaysorum', 'African Lion', [(1, n) for n in (1, 2, 3, 4, 6, 8)]),
         ('Tyrannosaurus rex', 'African Bush Elephant', [(1, n) for n in (1, 2, 3, 4, 6, 8)]),
         ('Tyrannosaurus rex', 'African Lion', [(1, n) for n in (1, 4, 8, 12, 16, 24)]),
         ('Deinonychus antirrhopus', 'Grey Wolf', [(1, n) for n in (1, 2, 4, 8, 12)]),
         ('Allosaurus fragilis', 'Polar Bear', [(1, n) for n in (1, 2, 4, 8)]),
         ('Dakotaraptor steini', 'African Lion', [(3, 6), (3, 9), (5, 12), (5, 20)])]
STAGINGS = ['scores', 'weights', 'lunge', 'bite', 'hold']


def blows(staging, sT, sM, mT, mM):
    """What a landed blow does: (theropod's, mammal's), each (now, rate) in shares of the victim's staying power."""
    if staging == 'scores':
        return (min(1.0, F0 * (sT / sM) ** RHO), 0.0), (min(1.0, F0 * (sM / sT) ** RHO), 0.0)
    rawT, rawM = F0 * (mT / mM) ** ETA, F0 * (mM / mT) ** ETA
    if staging == 'weights':
        return (min(1.0, rawT), 0.0), (min(1.0, rawM), 0.0)
    mam = (min(1.0, rawM * LUNGE), 0.0)
    if staging == 'lunge':
        return (min(1.0, rawT), 0.0), mam
    bite = (min(1.0, rawT * BITE_NOW), min(1.0, rawT * BITE_RATE))
    return (bite, mam) if staging == 'bite' else (bite, (1.0, 0.0))


def pair_chance(q, A, B):
    """Chance that A beats B one on one, exchange by exchange, wounds bleeding before each exchange (as biteChance in arena.html)."""
    @lru_cache(maxsize=None)
    def go(hA, hB, rA, rB):                     # in units of 1e-9, so that the states are exact
        tA = hA / rA if rA > 0 else math.inf; tB = hB / rB if rB > 0 else math.inf
        if min(tA, tB) <= 1 + 1e-12:
            return 0.0 if tA < tB - 1e-12 else 1.0 if tB < tA - 1e-12 else 0.5
        a, b = hA - rA, hB - rB
        pa = 1.0 if b - A[0] <= 1 else go(a, b - A[0], rA, rB + A[1])
        pb = 0.0 if a - B[0] <= 1 else go(a - B[0], b, rA + B[1], rB)
        return q * pa + (1 - q) * pb
    return go(10 ** 9, 10 ** 9, 0, 0)


def solve_q(P, A, B):
    A, B = tuple(round(x * 1e9) for x in A), tuple(round(x * 1e9) for x in B); lo, hi = 1e-9, 1 - 1e-9
    for _ in range(44):
        m = (lo + hi) / 2
        if pair_chance(m, A, B) < P: lo = m
        else: hi = m
    return (lo + hi) / 2


def simulate(q, A, B, m, n, fights, rng):
    """m theropods against n mammals, `fights` times. Returns the theropods' share of wins, the share of fallen mammals that
    fell to blood loss, and the mean number of exchanges."""
    hT, rT, hM, rM = np.ones((fights, m)), np.zeros((fights, m)), np.ones((fights, n)), np.zeros((fights, n))
    act = np.arange(fights); wins = 0; blood = 0; blow = 0; exch = 0
    while act.size:
        t, tr, mm, mr = hT[act], rT[act], hM[act], rM[act]; aT, aM = t > 0, mm > 0
        dt = 1.0 / np.minimum(aT.sum(1), aM.sum(1)); over = np.zeros(act.size, bool); won = np.zeros(act.size, bool)
        if tr.any() or mr.any():                  # the clock: those whose wounds finish them before the next exchange fall, nearest first
            with np.errstate(divide='ignore', invalid='ignore'):
                dT = np.where(aT & (tr > 0), t / tr, np.inf); dM = np.where(aM & (mr > 0), mm / mr, np.inf)
            fT, fM = dT <= dt[:, None] + 1e-12, dM <= dt[:, None] + 1e-12
            outT, outM = ~(aT & ~fT).any(1), ~(aM & ~fM).any(1)           # a side all of whose standing fighters fall in this turn
            endT = np.where(outT, np.where(fT, dT, -np.inf).max(1), np.inf); endM = np.where(outM, np.where(fM, dM, -np.inf).max(1), np.inf)
            tie = outT & outM & (endT == endM); coin = rng.random(act.size) < 0.5
            won = outM & (~outT | (endM < endT) | (tie & coin)); over = outT | outM; end = np.minimum(endT, endM)
            fM &= dM <= end[:, None]; fT &= dT <= end[:, None]            # (nobody falls after the fight is over)
            blood += int(fM.sum()); mm[fM] = 0; mr[fM] = 0; t[fT] = 0; tr[fT] = 0
            live = ~over; t[live] -= (tr * dt[:, None])[live]; mm[live] -= (mr * dt[:, None])[live]
            aT, aM = t > 0, mm > 0
        go = ~over; k = int(go.sum())
        if k:                                     # the exchange: one of each side at random, and one of them lands
            iT = np.argmax(rng.random((act.size, m)) * aT, 1); iM = np.argmax(rng.random((act.size, n)) * aM, 1); rows = np.arange(act.size)
            lands = (rng.random(act.size) < q) & go; taken = go & ~lands; exch += k
            v = mm[rows, iM] - A[0]; dead = lands & (v <= 1e-9); blow += int(dead.sum())
            mm[rows[lands], iM[lands]] = np.where(dead[lands], 0.0, v[lands]); mr[rows[lands], iM[lands]] = np.where(dead[lands], 0.0, mr[rows[lands], iM[lands]] + A[1])
            v = t[rows, iT] - B[0]; dead = taken & (v <= 1e-9)
            t[rows[taken], iT[taken]] = np.where(dead[taken], 0.0, v[taken]); tr[rows[taken], iT[taken]] = np.where(dead[taken], 0.0, tr[rows[taken], iT[taken]] + B[1])
            noT, noM = go & ~(t > 0).any(1), go & ~(mm > 0).any(1); won |= noM; over |= noT | noM
        hT[act], rT[act], hM[act], rM[act] = t, tr, mm, mr
        wins += int(won.sum()); act = act[~over]
    return wins / fights, blood / max(1, blood + blow), exch / fights


def main():
    ap = argparse.ArgumentParser(description='What the arena\'s fight model implies for one theropod against several mammals.')
    ap.add_argument('--fights', type=int, default=300000, help='simulated fights for each number (default: %(default)s)')
    ap.add_argument('--arena', action='store_true', help='use the arena\'s accurate scores (full-percentile medians) instead of the paper\'s medians')
    args = ap.parse_args(); sys.setrecursionlimit(20000)
    here = os.path.dirname(os.path.abspath(__file__)); os.chdir(here)
    S = {r['animal']: r for r in csv.DictReader(open(os.path.join('..', 'final_scores.csv'), encoding='utf-8'))}
    k = json.load(open(os.path.join('outputs', 'human_model.json')))['group_exponent']['k']
    crowd = lambda a: float(S[a]['score']); acc = lambda a: float(S[a]['full_p50' if args.arena else 'median_score'])
    rng = np.random.default_rng(SEED); out = []; rows = []
    for T, M, sizes in CASES:
        sT, sM, mT, mM = acc(T), crowd(M), MASS[T], MASS[M]; P1 = sT / (sT + sM); stag = {}
        for st in STAGINGS:
            A, B = blows(st, sT, sM, mT, mM); q = solve_q(P1, A, B); check = pair_chance(q, tuple(round(x * 1e9) for x in A), tuple(round(x * 1e9) for x in B))
            assert abs(check - P1) < 1e-7, (T, M, st, check, P1)
            stag[st] = dict(lands=q, theropod_now=A[0], theropod_bleeds=A[1], mammal_now=B[0], mammal_blows_needed=math.ceil(1 / B[0] - 1e-9), by_n=[])
        for m, n in sizes:
            rule = 1 / (1 + (n ** k * sM) / (m ** k * sT)); linear = 1 / (1 + n * sM / (m * sT)); row = dict(theropods=m, mammals=n, score_rule=rule, linear=linear)
            for st in STAGINGS:
                A, B = blows(st, sT, sM, mT, mM); share, blood, ex = simulate(stag[st]['lands'], A, B, m, n, args.fights, rng)
                keff = math.log((P1 / (1 - P1)) / (share / (1 - share))) / math.log(n) if m == 1 and n > 1 and 0 < share < 1 else None
                stag[st]['by_n'].append(dict(theropods=m, mammals=n, share=share, to_blood=blood, exchanges=ex, k_eff=keff)); row[st] = share
            rows.append(dict(theropod=SHORT[T], mammal=SHORT[M], **row))
        out.append(dict(theropod=T, mammal=M, theropod_score=sT, mammal_score=sM, theropod_kg=mT, mammal_kg=mM, one_on_one=P1,
                        even_by_score_rule=(sT / sM) ** (1 / k), even_linear=sT / sM, stagings=stag))
    os.makedirs('outputs', exist_ok=True); tag = '_arena' if args.arena else ''
    json.dump(dict(k=k, fights=args.fights, seed=SEED, scores='arena (full-percentile medians)' if args.arena else 'paper (median anatomy factor)',
                   constants=dict(F0=F0, RHO=RHO, ETA=ETA, LUNGE=LUNGE, BITE_NOW=BITE_NOW, BITE_RATE=BITE_RATE), cases=out), open(f'outputs/group_mechanics{tag}.json', 'w'), indent=1)
    with open(f'outputs/group_mechanics{tag}.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['theropod', 'mammal', 'theropods', 'mammals', 'score_rule', 'linear'] + STAGINGS)
        for r in rows: w.writerow([r['theropod'], r['mammal'], r['theropods'], r['mammals']] + [f"{r[c]:.4f}" for c in ['score_rule', 'linear'] + STAGINGS])
    pc = lambda v: f"{100 * v:.0f}" if 0.005 <= v < 0.995 else ('$<$1' if v < 0.005 else '$>$99')
    for c in out:
        t, mname = SHORT[c['theropod']], SHORT[c['mammal']]; s = c['stagings']
        print(f"\n{t} ({c['theropod_score']:,.0f}, {c['theropod_kg']} kg) against {PLURAL.get(mname, mname + 's')} ({c['mammal_score']:,.0f}, {c['mammal_kg']} kg): one on one {100 * c['one_on_one']:.1f}%;"
              f" even by the score rule at {c['even_by_score_rule']:.1f}, by adding scores at {c['even_linear']:.1f}")
        for st in STAGINGS:
            x = s[st]; bite = f"{100 * x['theropod_now']:.0f}%" + (f" then {100 * x['theropod_bleeds']:.0f}% an exchange" if x['theropod_bleeds'] else '')
            print(f"  {st:8s} theropod lands {100 * x['lands']:.0f}%, its blow {bite}; the mammal's {100 * x['mammal_now']:.0f}% ({x['mammal_blows_needed']} needed) | " +
                  '  '.join(f"{d['theropods']}v{d['mammals']} {100 * d['share']:.1f}%" + (f" (k {d['k_eff']:.2f})" if d['k_eff'] is not None else '') for d in x['by_n']) +
                  f" | mammals falling to blood loss {100 * x['by_n'][0]['to_blood']:.0f}% one on one")
    print('\nLaTeX rows (theropods v mammals & score rule & adding scores & ' + ' & '.join(STAGINGS) + '):')
    for r in rows:
        print(f"{r['theropod']} & {r['theropods']} v {r['mammals']} {PLURAL.get(r['mammal'], r['mammal'] + 's') if r['mammals'] > 1 else r['mammal']} & " + ' & '.join(pc(r[c]) for c in ['score_rule', 'linear'] + STAGINGS) + ' \\\\')
    print(f"\nwrote outputs/group_mechanics{tag}.json, outputs/group_mechanics{tag}.csv (group exponent {k:.3f}, {args.fights:,} fights each)")


if __name__ == '__main__':
    main()
