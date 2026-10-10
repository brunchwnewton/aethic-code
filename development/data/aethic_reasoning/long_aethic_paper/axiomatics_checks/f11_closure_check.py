# F11: is closure (narrowing + propagation, with propagation narrowing the blank) a closure operator?
# Three readings of propagation, tested by brute force on random small rulebooks.
#   C = current text: remove the peg from the narrowest filling present, or from the whole attribute if none (F7 (i) as written)
#   A = repair A: remove from every filling present; narrow the blank too, but only for declared sets whose other members lie on other attributes
#   E = repair E: record the removal as an exclusion; narrow present fillings; the filling is read as states intersected with non-excluded pegs
import random, itertools
ATTR = {'X': ['x1','x2','x3'], 'Y': ['y1','y2','y3'], 'W': ['w1','w2'], 'H': ['h1','h2']}
OF = {p: a for a, ps in ATTR.items() for p in ps}
PEGS = list(OF); fs = frozenset
EXPLODE = False
ALL_STATES = frozenset((a, frozenset(c)) for a, ps in ATTR.items() for k in range(len(ps) + 1) for c in itertools.combinations(ps, k))

def rulebook(rng):
    D = [fs(pair) for ps in ATTR.values() for pair in itertools.combinations(ps, 2)]      # disjointness
    for _ in range(rng.randint(2, 6)):                                                 # cross-attribute declarations
        k = rng.choice([2, 2, 3]); attrs = rng.sample(list(ATTR), k)
        D.append(fs(rng.choice(ATTR[a]) for a in attrs))
    return D

def rep(rng, n=None, avoid=()):
    R = set()
    for _ in range(n if n is not None else rng.randint(1, 3)):
        a = rng.choice([x for x in ATTR if x not in avoid]); ps = ATTR[a]
        R.add((a, fs(rng.sample(ps, rng.randint(1, len(ps))))))
    return R

def close(R, D, v, Ex0=()):
    C, Ex = set(R), set(Ex0)
    while True:
        new, newEx = set(), set()
        by = {}
        for a, F in C: by.setdefault(a, []).append(F)
        for a, Fs in by.items():
            for F in Fs:
                for G in Fs: new.add((a, F & G))
        held = {next(iter(F)) for a, F in C if len(F) == 1}
        for Dset in D:
          for p in Dset:                       # 'every member but one' read monotonically: all OTHER members held
            if not all(q in held for q in Dset if q != p): continue
            a = OF[p]
            if v == 'C':
                cur = fs.intersection(*by[a]) if a in by else fs(ATTR[a]); new.add((a, cur - {p}))
            elif v == 'A':
                for F in by.get(a, []): new.add((a, F - {p}))
                if all(OF[q] != a for q in Dset if q != p): new.add((a, fs(ATTR[a]) - {p}))
            else:
                newEx.add(p)
        if v == 'E':
            for p in Ex | newEx:
                for F in by.get(OF[p], []): new.add((OF[p], F - {p}))
            for a, ps in ATTR.items():
                for p in ps:
                    if all(q in (Ex | newEx) for q in ps if q != p): new.add((a, fs({p})))
        if new <= C and newEx <= Ex: break
        C |= new; Ex |= newEx
    if EXPLODE and any(len(F) == 0 for a, F in C):                     # the paper's unique bottom: every invalid content is the invalid Aethus 0
        return (ALL_STATES, fs(PEGS) if v == 'E' else fs())
    return (fs(C), fs(Ex)) if v == 'E' else (fs(C), fs())

valid = lambda c: c[0] != ALL_STATES and not any(len(F) == 0 for a, F in c[0])
leq = lambda c, d: c[0] <= d[0] and c[1] <= d[1]
def meet_reps(RA, RB, D, v): return close(RA | RB, D, v)
def meet_contents(cA, cB, D, v): return close(cA[0] | cB[0], D, v, cA[1] | cB[1])

for EXPLODE in (False, True):
    print('\n=== invalid contents ' + ('collapsed to the one invalid Aethus 0' if EXPLODE else 'kept distinct (tagged, as in the tree paper)') + ' ===')
    rng = random.Random(20260924)
    N = 4000
    fails = {v: dict(monotone=0, idempotent=0, meet_rep_indep=0, shadow_no_state=0, branch_within=0) for v in 'CAE'}
    tested_shadow = 0
    for _ in range(N):
        D = rulebook(rng)
        R1 = rep(rng); R2 = R1 | rep(rng, 1); RA = rep(rng); RB = rep(rng)
        base = rep(rng, rng.randint(0, 2), avoid=('X',))
        other = rep(rng, rng.randint(0, 2), avoid=('X',))
        for v in 'CAE':
            c1, c2 = close(R1, D, v), close(R2, D, v)
            if not leq(c1, c2): fails[v]['monotone'] += 1
            cc = close(c1[0], D, v, c1[1])
            if cc != c1: fails[v]['idempotent'] += 1
            cA, cB = close(RA, D, v), close(RB, D, v)
            if meet_reps(RA, RB, D, v) != meet_contents(cA, cB, D, v): fails[v]['meet_rep_indep'] += 1
            # F1 second half: a representation whose only state on X is [X:{x1}] keeps every X-filling within {x1}
            cw = close(other | {('X', fs({'x1'}))}, D, v)
            if valid(cw) and any(a == 'X' and not F <= {'x1'} for a, F in cw[0]): fails[v]['branch_within'] += 1   # valid branches only, as in the F1 proof
            # 3.3: branches on a base with no state (and, for E, no exclusion) on X carry no common state on X
            cb = close(base, D, v)
            if any(a == 'X' for a, F in cb[0]) or any(OF[p] == 'X' for p in cb[1]): continue
            if v == 'C': tested_shadow += 1
            b1 = close(cb[0] | {('X', fs({'x1'}))}, D, v, cb[1]); b2 = close(cb[0] | {('X', fs({'x2'}))}, D, v, cb[1])
            if valid(b1) and valid(b2) and any(a == 'X' for a, F in (b1[0] & b2[0])): fails[v]['shadow_no_state'] += 1

    print(f"{N} random rulebooks; shadow test ran on {tested_shadow} bases with no state on X\n")
    print(f"{'property (violations)':<44}{'current':>9}{'repair A':>10}{'repair E':>10}")
    labels = {'monotone': 'Cl monotone (Prop 4)', 'idempotent': 'Cl idempotent (Prop 4)',
              'meet_rep_indep': 'meet independent of representations (Prop 8)',
              'branch_within': 'F1 proof: X-fillings stay within {x1}', 'shadow_no_state': '3.3: shadow carries no state on X'}
    for k, lab in labels.items():
        print(f"{lab:<44}{fails['C'][k]:>9}{fails['A'][k]:>10}{fails['E'][k]:>10}")


EXPLODE = False
# the minimal hand counterexample for the paper as it stands
D0 = [fs(p) for ps in ATTR.values() for p in itertools.combinations(ps, 2)] + [fs({'h1', 'y2'})]
RA0, RB0 = {('H', fs({'h1'}))}, {('Y', fs({'y1', 'y2'}))}
cA0, cB0 = close(RA0, D0, 'C'), close(RB0, D0, 'C')
show = lambda c: sorted((a, ''.join(sorted(F))) for a, F in c[0] if a == 'Y')
print("\nminimal witness, current text: A = [H:{h1}] with {h1, y2} declared; B = [Y:{y1,y2}]")
print("  C(A) on Y:", show(cA0))
print("  meet from representations, on Y:", show(meet_reps(RA0, RB0, D0, 'C')))
print("  meet from contents, on Y:       ", show(meet_contents(cA0, cB0, D0, 'C')))
