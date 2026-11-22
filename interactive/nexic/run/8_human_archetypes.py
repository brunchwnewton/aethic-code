#!/usr/bin/env python3
"""Step 8 — human archetypes on the scale, and n fighters against a raptor (new; exploratory, not part of the paper).

Usage:  python3 8_human_archetypes.py      reads ../final_scores.csv (and outputs/graph/summary.json for the mass exponent)
        -> outputs/human_archetypes.csv, outputs/human_duel_matrix.csv, outputs/humans_vs_raptors.csv, outputs/human_model.json
           and, when ../arena.html exists, the data block of that page

Each archetype gets two numbers, because one cannot do both jobs.
  score      where the fighter stands among the animals, on the scale of final_scores.csv (African Lion = 100):
                 log S = log S_Human + sex + mass + weapon + armour + GAMMA * transfer * skill
  duel_elo   how the fighter does against other humans, in real odds: P(A beats B) = 1 / (1 + 10^((elo_B - elo_A) / 400)),
             the untrained 70 kg man at 1000:
                 log-odds = sex / GAMMA + mass + weapon + armour + skill
             When one fighter is armed and the other is not, the unarmed fighter's skill counts for CROSS of its value
             (subtract (1 - CROSS) * unarmed_skill_elo from his rating); human_duel_matrix.csv applies this.
Scores are shares of a crowd's votes, far less lopsided than real outcomes (the crowd puts a lion at 15 times a man). GAMMA,
crowd log-odds per real log-odds, converts between the two; two rough readings agree on about a third (see GAMMA below).
Skill is known in real odds between humans; against an animal only a fraction of it carries over (TRANSFER).

Evidence grades, written to the csv for every archetype (its weakest term):
  A  measured on this scale, from the votes: "Human"; the spear and club premiums (hominin entries with and without the
     weapon); the female offset; the exponent with which groups grow (every group entry against its solo entry).
  B  measured, then converted: body mass (the scale's own mammal exponent; combat-sport weight studies for duels).
  C  judgment anchored on a measured term: the other weapons, stated relative to the spear.
  D  judgment: skill, its carry-over against animals, armour, GAMMA. No data set gives win rates for these.
Every term is a normal distribution on the log scale; N_DRAWS joint draws give each archetype's median and 90% band.

Against one animal, n fighters count as n^k one fighter, and the crowd's vote share is S_n / (S_n + S_animal). Three exponents
are reported: the one the crowd's own groups show, the linear case, and step 3's N^0.7 rule. The raptors take their crowd
score and their anatomy-corrected score with the full band of final_scores.csv."""
import json, os, re
import numpy as np, pandas as pd

N_DRAWS, SEED = 20000, 8
GAMMA = (0.35, 0.08)        # D. log 15 (lion over man, crowd) / log 1000 (the same in real odds, a guess) = 0.39; and the scale's
                            # mass exponent 1.29 over the real one below = 0.29
MASS_REAL = (4.5, 2.0)      # B. real odds grow as mass^4.5 at equal skill: +4.6% odds per +1% of weight regained after the weigh-in
                            # (Faro et al., 1,474 MMA weigh-ins); Baribeau et al. find 7%, a Bellator study nothing, hence the spread
MASS_SCALE_SD = 0.15        # B. the exponent itself is read from the coupled fit's mammals (summary.json), between species
ARMED_MASS = 0.5            # D. a weapon halves what body mass is worth
REF_MASS = {'m': 70, 'f': 58}   # the female offset is measured against "Human" and already holds the usual difference in mass
TRANSFER = {'unarmed': (0.15, 0.10), 'duellist': (0.50, 0.20), 'beast': (1.0, 0.0)}   # D. share of skill that carries over against animals
NOVICE = (0.65, 0.15)       # D. share of a weapon's log premium that an untrained user gets
SKILL = {                   # D. real log-odds over the reference fighter
    'untrained': (0.0, 0.0), 'trained amateur': (3.0, 1.0), 'professional': (5.7, 1.2), 'elite': (7.6, 1.5),    # unarmed, over an untrained man
    'novice': (0.0, 0.0), 'competent': (0.0, 0.0), 'professional (armed)': (2.3, 0.9), 'elite (armed)': (3.4, 1.1)}   # armed, over a habitual user
CROSS = (0.30, 0.15)        # D. share of unarmed skill that counts when the opponent is armed and the fighter is not
WEAPON = {                  # C. relative to the spear, whose own premium is measured (as is the club's): (against animals, crowd log units),
                            # (against humans, real log-odds). Reach is worth more against an animal than against a man. The four
                            # gladiator kits are set even in duels with their armour, the pairings having been chosen to be even.
    'spear': ((0.0, 0.0), (0.0, 0.0)), 'spear + shield': ((0.3, 0.3), (0.8, 0.5)), 'spear + small shield': ((0.2, 0.3), (0.5, 0.5)),
    'trident + net': ((-0.1, 0.4), (0.9, 0.6)), 'pike or polearm': ((0.2, 0.4), (0.5, 0.6)), 'sword + large shield': ((-0.2, 0.3), (0.5, 0.5)),
    'sword + small shield': ((-0.35, 0.3), (0.5, 0.5)), 'two-handed sword': ((-0.4, 0.4), (0.0, 0.6)), 'axe + shield': ((-0.25, 0.35), (0.3, 0.5)),
    'short stabbing spear + shield': ((0.1, 0.35), (0.5, 0.5)), 'staff': ((-0.9, 0.4), (-1.2, 0.6)), 'knife': ((-1.2, 0.4), (-2.5, 0.7))}
ARMOUR = {                  # D. (against animals, crowd log units), (against humans, real log-odds)
    'none': ((0, 0), (0, 0)), 'arm and shoulder guard': ((0.05, 0.1), (0.2, 0.3)), 'helmet and guards': ((0.2, 0.15), (0.6, 0.4)),
    'mail or plates with helmet': ((0.45, 0.25), (1.5, 0.6)), 'full plate': ((0.8, 0.35), (3.0, 1.0))}
SPEAR_PAIRS = [('Neanderthal (armed with a spear)', 'Neanderthal'), ('Neanderthal (with spear)', 'Neanderthal'), ('Homo erectus (armed with spear)', 'Homo erectus'),
               ('Archaic Human (armed with spear)', 'Archaic Human'), ('Homo floresiensis (armed with a spear)', 'Homo floresiensis')]
CLUB_PAIRS = [('Homo floresiensis (Armed with club)', 'Homo floresiensis')]
GROUP_FIX = {'Neanderthal (armed with spears, troop of 10)': 'Neanderthal (armed with a spear)', 'Archaic Humans (group of 3 - 5) armed with spear': 'Archaic Human (armed with spear)',
             'Homo floresiensis (group of 4) (armed with clubs)': 'Homo floresiensis (Armed with club)', 'Neanderthals (3) (armed with spears)': 'Neanderthal (armed with a spear)'}
GROUP_RE = re.compile(r'\(?\b(?:pack|pride|herd|troop|group|pod|flock|mob|clan|coalition|swarm)\s+of\s+(\d+)(?:\s*[-/]\s*(\d+))?[^)]*\)?|\((\d+)\)', re.I)
K_SD = 0.15                 # spread given to the group exponent in the draws, wider than its standard error (classes differ)
# name: (sex, mass kg, weapon, skill, carry-over, armour, note)
ARCHETYPES = {
    'Untrained man': ('m', 70, None, 'untrained', 'unarmed', 'none', 'the scale\'s own "Human"'),
    'Untrained woman': ('f', 58, None, 'untrained', 'unarmed', 'none', 'the scale\'s own "Human (female)"'),
    'Amateur boxer, 75 kg': ('m', 75, None, 'trained amateur', 'unarmed', 'none', ''),
    'Professional MMA fighter, 77 kg': ('m', 77, None, 'professional', 'unarmed', 'none', ''),
    'Professional MMA fighter, 120 kg': ('m', 120, None, 'professional', 'unarmed', 'none', ''),
    'Elite heavyweight champion, 110 kg': ('m', 110, None, 'elite', 'unarmed', 'none', ''),
    'Professional woman fighter, 61 kg': ('f', 61, None, 'professional', 'unarmed', 'none', ''),
    'Untrained man with a knife': ('m', 70, 'knife', 'novice', 'beast', 'none', ''),
    'Untrained man with a club': ('m', 70, 'club', 'novice', 'beast', 'none', ''),
    'Untrained man with a spear': ('m', 70, 'spear', 'novice', 'beast', 'none', ''),
    'Martial artist with a staff': ('m', 72, 'staff', 'professional (armed)', 'duellist', 'none', ''),
    'Martial artist with a knife': ('m', 72, 'knife', 'professional (armed)', 'duellist', 'none', ''),
    'Hunter with a spear': ('m', 68, 'spear', 'competent', 'beast', 'none', 'what the crowd\'s armed hominins stand for'),
    'Maasai warrior, spear and shield': ('m', 68, 'spear + shield', 'competent', 'beast', 'none', 'lion hunting is the tradition'),
    'Zulu warrior, iklwa and shield': ('m', 70, 'short stabbing spear + shield', 'professional (armed)', 'duellist', 'none', ''),
    'Roman legionary, gladius and scutum': ('m', 68, 'sword + large shield', 'professional (armed)', 'duellist', 'mail or plates with helmet', ''),
    'Greek hoplite, dory and aspis': ('m', 68, 'spear + shield', 'professional (armed)', 'duellist', 'mail or plates with helmet', ''),
    'Gladiator, novice murmillo': ('m', 76, 'sword + large shield', 'competent', 'duellist', 'helmet and guards', 'first-year tiro'),
    'Gladiator, murmillo': ('m', 78, 'sword + large shield', 'professional (armed)', 'duellist', 'helmet and guards', 'Ephesus stature (168 cm), fed to carry bulk'),
    'Gladiator, thraex': ('m', 76, 'sword + small shield', 'professional (armed)', 'duellist', 'helmet and guards', ''),
    'Gladiator, hoplomachus': ('m', 76, 'spear + small shield', 'professional (armed)', 'duellist', 'helmet and guards', ''),
    'Gladiator, retiarius': ('m', 72, 'trident + net', 'professional (armed)', 'duellist', 'arm and shoulder guard', ''),
    'Gladiator, champion murmillo, 90 kg': ('m', 90, 'sword + large shield', 'elite (armed)', 'duellist', 'helmet and guards', ''),
    'Venator (arena hunter), hunting spear': ('m', 74, 'spear', 'professional (armed)', 'beast', 'none', 'trained for animals and given spears'),
    'Venator, champion, hunting spear': ('m', 80, 'spear', 'elite (armed)', 'beast', 'none', ''),
    'Viking, axe and shield': ('m', 78, 'axe + shield', 'professional (armed)', 'duellist', 'mail or plates with helmet', ''),
    'Samurai, katana': ('m', 62, 'two-handed sword', 'professional (armed)', 'duellist', 'mail or plates with helmet', ''),
    'Swiss pikeman': ('m', 70, 'pike or polearm', 'professional (armed)', 'duellist', 'helmet and guards', ''),
    'Knight on foot, longsword, full plate': ('m', 78, 'two-handed sword', 'professional (armed)', 'duellist', 'full plate', ''),
    'Knight on foot, poleaxe, full plate': ('m', 78, 'pike or polearm', 'professional (armed)', 'duellist', 'full plate', ''),
}
VERSUS = ['Venator (arena hunter), hunting spear', 'Gladiator, murmillo', 'Gladiator, hoplomachus', 'Gladiator, retiarius', 'Hunter with a spear', 'Untrained man']
RAPTORS = ['Dakotaraptor steini', 'Utahraptor ostrommaysorum']
ARENA = os.path.join('..', 'arena.html')
OPPONENTS = {   # for the arena page: (kg, body length m, shape); masses as in step 6
    'African Lion': (185, 2.6, 'cat'), 'Brown Bear': (300, 2.3, 'bear'), 'Deinonychus antirrhopus': (73, 3.3, 'raptor'), 'Dakotaraptor steini': (250, 5.5, 'raptor'),
    'Utahraptor ostrommaysorum': (500, 6.0, 'raptor'), 'Tyrannosaurus rex': (8000, 12.3, 'rex')}


def pooled(pairs, B):
    """Random-effects mean of the log-ratios of paired entries (DerSimonian-Laird), and its standard deviation for a new case."""
    eta = np.array([np.log(B.score[a] / B.score[b]) for a, b in pairs]); se = np.array([np.hypot(B.se_log[a], B.se_log[b]) for a, b in pairs])
    w = 1 / se**2; m = (w * eta).sum() / w.sum(); Q = (w * (eta - m)**2).sum(); C = w.sum() - (w**2).sum() / w.sum()
    tau2 = max(0.0, (Q - len(eta) + 1) / C) if len(eta) > 1 else 0.0; wr = 1 / (se**2 + tau2)
    return float((wr * eta).sum() / wr.sum()), float(np.sqrt(1 / wr.sum() + tau2)), [float(e) for e in eta]


def group_exponent(B):
    """k in score(N animals) = N^k score(one): weighted least squares through the origin over every group entry with a solo entry."""
    rows = []
    for a in B.index:
        m = GROUP_RE.search(a)
        if not m: continue
        N = (float(m.group(1)) + float(m.group(2) or m.group(1))) / 2 if m.group(1) else float(m.group(3))
        base = re.sub(r'\(\s*\)', '', re.sub(r'\s+', ' ', a[:m.start()] + a[m.end():])).strip()
        cands = [GROUP_FIX.get(a), base, re.sub(r's\b', '', base, count=1), base.replace('Wolves', 'Wolf').replace('Buffaloes', 'Buffalo').replace('Humans', 'Human').replace(' Cows', '')]
        solo = next((c for c in cands if c in B.index), None)
        if solo and N >= 2: rows.append((a, solo, N, np.log(B.score[a] / B.score[solo]), np.hypot(B.se_log[a], B.se_log[solo])))
    G = pd.DataFrame(rows, columns=['group', 'solo', 'N', 'y', 'se']); x = np.log(G.N); w = 1 / G.se**2
    k = float((w * x * G.y).sum() / (w * x * x).sum()); phi = max(1.0, float((w * (G.y - k * x)**2).sum() / (len(G) - 1)))
    return k, float(np.sqrt(phi / (w * x * x).sum())), G


def grade(weapon, skill, armour, mass, sex):
    if SKILL[skill][1] > 0 or armour != 'none' or skill == 'novice': return 'D'
    if weapon not in (None, 'spear', 'club'): return 'C'
    return 'B' if mass != REF_MASS[sex] else 'A'


def main():
    B = pd.read_csv(os.path.join('..', 'final_scores.csv')).set_index('animal'); rng = np.random.default_rng(SEED); n = N_DRAWS
    spear, club = pooled(SPEAR_PAIRS, B), pooled(CLUB_PAIRS, B); k_hat, k_se, G = group_exponent(B)
    female = (float(np.log(B.score['Human (female)'] / B.score['Human'])), float(np.hypot(B.se_log['Human (female)'], B.se_log['Human'])))
    try: b_scale = json.load(open('outputs/graph/summary.json'))['variants']['coupled']['weight_score']['fits']['mammals'][1]
    except (OSError, KeyError): b_scale = json.load(open('outputs/weight_score.json'))['fits']['mammals'][1]
    draw = lambda ms: rng.normal(ms[0], ms[1], n) if ms[1] > 0 else np.full(n, float(ms[0]))
    gamma = np.clip(draw(GAMMA), 0.15, 0.8); m_real = np.clip(draw(MASS_REAL), 0.5, 9); m_scale = draw((b_scale, MASS_SCALE_SD)); novice = np.clip(draw(NOVICE), 0.2, 1)
    human = draw((np.log(B.score['Human']), B.se_log['Human'])); fem = draw(female); sp = draw(spear[:2]); cl = draw((club[0], max(club[1], 0.4)))
    skill = {s: draw(v) for s, v in SKILL.items()}; transfer = {t: np.clip(draw(v), 0, 1) for t, v in TRANSFER.items()}
    weapon = {w: draw(v[0]) for w, v in WEAPON.items()}; wpn_d = {w: draw(v[1]) for w, v in WEAPON.items()}; cross = np.clip(draw(CROSS), 0, 1); arm_b = {a: draw(v[0]) for a, v in ARMOUR.items()}; arm_d = {a: draw(v[1]) for a, v in ARMOUR.items()}
    rows, logs, duel, usk = [], {}, {}, {}
    for name, (sex, mass, wpn, sk, tr, armour, note) in ARCHETYPES.items():
        lm = np.log(mass / REF_MASS[sex]) * (ARMED_MASS if wpn else 1.0); sx = fem if sex == 'f' else 0.0
        wl = 0.0 if wpn is None else (cl if wpn == 'club' else sp + weapon[wpn]) * (novice if sk == 'novice' else 1.0)
        ls = human + sx + m_scale * lm + wl + arm_b[armour] + gamma * transfer[tr] * skill[sk]
        wd = 0.0 if wpn is None else (cl / gamma if wpn == 'club' else sp / gamma + wpn_d[wpn]) * (novice if sk == 'novice' else 1.0)
        dl = sx / gamma + m_real * lm + wd + arm_d[armour] + skill[sk]
        logs[name], duel[name], usk[name] = ls, dl, (skill[sk] if wpn is None else None); p = np.exp(np.percentile(ls, [5, 50, 95])); e = 1000 + 400 / np.log(10) * np.percentile(dl, [5, 50, 95])
        rows.append(dict(archetype=name, sex=sex, mass_kg=mass, weapon=wpn or 'none', skill=sk, armour=armour, score=p[1], score_p05=p[0], score_p95=p[2], lions=p[1] / 100,
                         duel_elo=e[1], duel_elo_p05=e[0], duel_elo_p95=e[2],
                         unarmed_skill_elo=400 / np.log(10) * SKILL[sk][0] if wpn is None else 0.0, evidence=grade(wpn, sk, armour, mass, sex), note=note))
    T = pd.DataFrame(rows).sort_values('score', ascending=False); os.makedirs('outputs', exist_ok=True)
    T.to_csv('outputs/human_archetypes.csv', index=False, float_format='%.4g')
    names = list(T.archetype)   # P(row beats column), real odds, median over the draws
    def beats(a, b):
        da, db = duel[a], duel[b]
        if (usk[a] is None) != (usk[b] is None): da, db = (da - (1 - cross) * usk[a], db) if usk[b] is None else (da, db - (1 - cross) * usk[b])
        return float(np.median(1 / (1 + np.exp(db - da))))
    M = pd.DataFrame([[beats(a, b) if a != b else 0.5 for b in names] for a in names], index=names, columns=names)
    M.to_csv('outputs/human_duel_matrix.csv', float_format='%.3f')
    k_draw = np.clip(rng.normal(k_hat, K_SD, n), 0.5, 2.5); vs = []
    full = lambda b: rng.normal(np.log(b.full_p50), np.log(b.full_p95 / b.full_p05) / 3.29, n)
    for r in RAPTORS:
        b = B.loc[r]; crowd = rng.normal(np.log(b.score), b.se_log, n); corr = full(b)
        for who in VERSUS:
            for scale, lr in (('crowd', crowd), ('anatomy-corrected', corr)):
                for kname, k in ((f'{k_hat:.2f} (crowd, measured)', k_draw), ('1 (linear)', 1.0), ('0.7 (step 3 rule)', 0.7)):
                    need = np.exp((lr - logs[who]) / k)   # fighters for an even vote
                    rec = dict(raptor=r, fighters=who, raptor_score=scale, group_exponent=kname, n_even=float(np.median(need)), n_even_p05=float(np.percentile(need, 5)),
                               n_even_p95=float(np.percentile(need, 95)))
                    for m in (1, 2, 3, 5, 10, 20, 50):
                        ratio = np.exp(k * np.log(m) + logs[who] - lr); rec[f'share_n{m}'] = float(np.median(ratio / (1 + ratio)))
                    vs.append(rec)
    Vs = pd.DataFrame(vs); Vs.to_csv('outputs/humans_vs_raptors.csv', index=False, float_format='%.4g')
    sd = lambda v: float(np.std(v))
    model = dict(human=float(B.score['Human']), spear_premium=dict(log=spear[0], sd=spear[1], factor=float(np.exp(spear[0])), pairs=dict(zip([a for a, _ in SPEAR_PAIRS], spear[2]))),
                 club_premium=dict(log=club[0], factor=float(np.exp(club[0]))), female=dict(log=female[0], se=female[1], factor=float(np.exp(female[0]))),
                 group_exponent=dict(k=k_hat, se=k_se, pairs=len(G), sd_used=K_SD), gamma=GAMMA, mass_exponent_real=MASS_REAL, mass_exponent_scale=float(b_scale), armed_mass=ARMED_MASS,
                 transfer=TRANSFER, novice=NOVICE, skill_real_log_odds=SKILL, weapon_vs_spear=WEAPON, armour=ARMOUR, cross=CROSS,
                 raptors={r: dict(crowd=float(B.score[r]), corrected=float(B.full_p50[r]), corrected_p05=float(B.full_p05[r]), corrected_p95=float(B.full_p95[r])) for r in RAPTORS})
    json.dump(model, open('outputs/human_model.json', 'w'), indent=1)
    if os.path.exists(ARENA):   # refresh the data block of the arena page
        data = dict(k=k_hat, k_sd=K_SD,
                    fighters=[dict(name=a, mu=float(np.median(logs[a])), sd=sd(logs[a]), weapon=ARCHETYPES[a][2] or 'none', armour=ARCHETYPES[a][5], mass=ARCHETYPES[a][1]) for a in names],
                    opponents=[dict(name=o, kg=kg, length=L, shape=shp, crowd_mu=float(np.log(B.score[o])), crowd_sd=float(B.se_log[o]), corr_mu=float(np.log(B.full_p50[o])),
                                    corr_sd=float(np.log(B.full_p95[o] / B.full_p05[o]) / 3.29), dino=shp in ('raptor', 'rex')) for o, (kg, L, shp) in OPPONENTS.items()])
        page = open(ARENA, encoding='utf-8').read(); a, b = page.find('/*DATA*/'), page.find('/*END DATA*/')
        if 0 <= a < b: open(ARENA, 'w', encoding='utf-8').write(page[:a] + '/*DATA*/const DATA = ' + json.dumps(data, separators=(',', ':')) + ';' + page[b:]); print('refreshed ../arena.html')
    print(f"measured on the scale: spear x{np.exp(spear[0]):.2f} (log {spear[0]:.2f} ± {spear[1]:.2f}), club x{np.exp(club[0]):.2f}, female x{np.exp(female[0]):.2f}, "
          f"group exponent {k_hat:.2f} ± {k_se:.2f} over {len(G)} group entries, mass exponent {b_scale:.2f}")
    print(T[['archetype', 'score', 'score_p05', 'score_p95', 'duel_elo', 'evidence']].to_string(index=False, float_format=lambda v: f'{v:,.1f}'))
    q = Vs[Vs.fighters.isin(VERSUS[:2]) & (Vs.group_exponent != '0.7 (step 3 rule)')]
    print(q[['raptor', 'fighters', 'raptor_score', 'group_exponent', 'n_even', 'n_even_p05', 'n_even_p95', 'share_n5', 'share_n10']].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    print('wrote outputs/human_archetypes.csv, outputs/human_duel_matrix.csv, outputs/humans_vs_raptors.csv, outputs/human_model.json')


if __name__ == '__main__':
    main()
