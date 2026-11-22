#!/usr/bin/env python3
"""Step 8 — human archetypes on the scale, and n fighters against a raptor (new; exploratory, not part of the paper).

Usage:  python3 8_human_archetypes.py      reads ../final_scores.csv (and outputs/graph/summary.json for the mass exponent)
        -> outputs/human_archetypes.csv, outputs/human_duel_matrix.csv, outputs/humans_vs_raptors.csv, outputs/human_model.json
           and, when ../arena.html exists, the data block of that page (fighters, animals, group exponent)

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

Bows and firearms. No vote covers them, so they are placed with one outside measurement and one outside index.
  The measurement: in 269 bear incidents in Alaska, a firearm stopped the bear in 76% (long guns) to 84% (handguns) of cases
  (Smith, Herrero et al., J. Wildl. Manage. 2012). Read as real odds of about 3.5 to 1 against the bears of that sample and
  shrunk by GAMMA, this puts an ordinary user with a hunting rifle somewhat above a brown bear (grade B).
  The index: Dupuy's Theoretical Lethality Index (sword or pike 23, longbow 36, flintlock 43, Springfield M1903 rifle 495,
  WWII machine gun 4,973, French 75 mm 386,530, ...). A weapon's premium is the spear's plus BETA * log(index / 23), and BETA
  is whatever makes the M1903's 495 land on the bear measurement (it comes out near one half). Weapons Dupuy does not list
  (pistols, assault rifles, rocket launchers) carry an index of mine (grade D).
  One number cannot say that a rifle loses less to a larger animal than a spear does. The firearm scores are fitted on
  bear-sized animals; the field guns and the tank lie three orders of magnitude of index away and are the roughest here.

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
TRANSFER = {'unarmed': (0.15, 0.10), 'duellist': (0.50, 0.20), 'beast': (1.0, 0.0), 'ranged': (0.8, 0.2)}   # D. share of skill that carries over against animals
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
    'mail or plates with helmet': ((0.45, 0.25), (1.5, 0.6)), 'full plate': ((0.8, 0.35), (3.0, 1.0)),
    'body armour and helmet': ((0.1, 0.1), (1.0, 0.5)), 'tank armour': ((1.2, 0.5), (0, 0))}
OLD_ARMOUR = {'arm and shoulder guard', 'helmet and guards', 'mail or plates with helmet', 'full plate'}
ARMOUR_VS_GUNS = 0.1        # D. share of pre-modern armour, and (with CROSS) of blade skill, that counts against a side with firearms
RANGED_MASS = 0.25          # D. what body mass is worth behind a bow or a gun
NOVICE_GUN = (0.80, 0.10)   # D. share of a firearm's log premium that an untrained user gets (a gun asks less of its user than a spear)
BEAR = dict(success=0.78, logit_sd=0.35, context_sd=0.5,   # B. Alaska 1883-2009: a firearm stopped the bear in 76% (long guns) to 84% (handguns)
            incidents={'Brown Bear': 218, 'American Black Bear': 30, 'Polar Bear': 6})   # of cases; context_sd for an arena not being a trail
TLI_HAND, TLI_RIFLE, TLI_SD = 23, 495, {True: 0.2, False: 0.5}   # Dupuy: sword or pike, Springfield M1903; log spread of an index (listed, mine)
RANGED = {                  # weapon: (lethality index, listed by Dupuy, duel log-odds over the spear (D), shot drawn on the page, range m there, crew, size m)
    'longbow': (36, True, (1.0, 0.7), 'arrow', 20, 1, 0), 'flintlock musket': (43, True, (1.5, 0.7), 'bullet', 16, 1, 0),
    '9 mm pistol': (150, False, (3.7, 0.8), 'bullet', 14, 1, 0), '.44 Magnum revolver': (400, False, (3.7, 0.8), 'bullet', 14, 1, 0),
    '12-gauge shotgun': (450, False, (4.5, 0.8), 'bullet', 14, 1, 0), 'bolt-action rifle': (495, True, (4.2, 0.8), 'bullet', 24, 1, 0),
    'double rifle': (600, False, (4.0, 0.8), 'bullet', 20, 1, 0), 'assault rifle': (1000, False, (5.0, 0.9), 'burst', 24, 1, 0),
    '.50 rifle': (1200, False, (4.5, 0.9), 'bullet', 28, 1, 0), 'rocket launcher': (3000, False, (5.0, 1.0), 'rocket', 22, 1, 0),
    'machine gun': (4973, True, (6.5, 1.0), 'burst', 26, 1, 0), 'heavy machine gun': (9000, False, (7.0, 1.0), 'burst', 28, 3, 1.8),
    'field gun': (386530, True, (7.0, 1.2), 'shell', 30, 6, 3.6), 'howitzer': (657215, True, (7.2, 1.2), 'shell', 30, 7, 4.2),
    'tank gun': (575000, True, (12.0, 1.5), 'shell', 30, 5, 6.0)}   # WWII medium tank as one reprint of Dupuy's table has it; another gives 935,458
GUNS = set(RANGED) - {'longbow'}
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
    'English longbowman': ('m', 72, 'longbow', 'professional (armed)', 'ranged', 'helmet and guards', ''),
    'Musketeer, flintlock and bayonet': ('m', 68, 'flintlock musket', 'professional (armed)', 'ranged', 'none', ''),
    'Civilian with a 9 mm pistol': ('m', 80, '9 mm pistol', 'novice', 'ranged', 'none', ''),
    'Police officer, 9 mm pistol': ('m', 85, '9 mm pistol', 'competent', 'ranged', 'body armour and helmet', ''),
    'Alaskan guide, .44 Magnum revolver': ('m', 85, '.44 Magnum revolver', 'competent', 'ranged', 'none', 'the bear-country sidearm'),
    'Hunter, bolt-action .30-06 rifle': ('m', 80, 'bolt-action rifle', 'competent', 'ranged', 'none', 'the anchor: bear incidents in Alaska'),
    'Hunter, 12-gauge shotgun with slugs': ('m', 80, '12-gauge shotgun', 'competent', 'ranged', 'none', ''),
    'Professional hunter, .470 double rifle': ('m', 85, 'double rifle', 'professional (armed)', 'ranged', 'none', 'a dangerous-game rifle'),
    'Soldier, assault rifle': ('m', 80, 'assault rifle', 'professional (armed)', 'ranged', 'body armour and helmet', ''),
    'Special forces operator, assault rifle': ('m', 85, 'assault rifle', 'elite (armed)', 'ranged', 'body armour and helmet', ''),
    'Sniper, .50 anti-materiel rifle': ('m', 80, '.50 rifle', 'professional (armed)', 'ranged', 'body armour and helmet', ''),
    'Soldier with a rocket launcher (RPG-7)': ('m', 80, 'rocket launcher', 'professional (armed)', 'ranged', 'body armour and helmet', ''),
    'Machine gunner, belt-fed 7.62 mm': ('m', 85, 'machine gun', 'professional (armed)', 'ranged', 'body armour and helmet', ''),
    'Heavy machine gun crew, .50 (3 men)': ('m', 80, 'heavy machine gun', 'professional (armed)', 'ranged', 'body armour and helmet', ''),
    'Field gun crew, 75 mm (6 men)': ('m', 75, 'field gun', 'professional (armed)', 'ranged', 'none', 'the French 75'),
    'Howitzer crew, 105 mm (7 men)': ('m', 75, 'howitzer', 'professional (armed)', 'ranged', 'none', ''),
    'Medium tank, 75 mm gun (crew of 5)': ('m', 75, 'tank gun', 'professional (armed)', 'ranged', 'tank armour', 'a Second World War medium'),
}
VERSUS = ['Venator (arena hunter), hunting spear', 'Gladiator, murmillo', 'Gladiator, hoplomachus', 'Gladiator, retiarius', 'Hunter with a spear', 'Untrained man',
          'Hunter, bolt-action .30-06 rifle', 'Soldier, assault rifle', 'Machine gunner, belt-fed 7.62 mm']
RAPTORS = ['Dakotaraptor steini', 'Utahraptor ostrommaysorum']
ARENA = os.path.join('..', 'arena.html')
ANIMALS = {     # for the arena page: (label, plural, kg, body length m, shape, coat, body colour, dark colour, accent); masses as in step 6 where it has them
    'African Lion': ('Lion', 'Lions', 185, 2.6, 'cat', 'mane', '#b98a4b', '#6b4a22', '#c2954f'),
    'Tiger': ('Tiger', 'Tigers', 220, 2.9, 'cat', 'stripes', '#d9822b', '#2b1a0c', '#f1e3c8'),
    'Leopard': ('Leopard', 'Leopards', 60, 2.0, 'cat', 'spots', '#c9a35a', '#3a2a14', '#e2c98a'),
    'Grey Wolf': ('Grey Wolf', 'Grey Wolves', 40, 1.6, 'dog', '', '#8d8b84', '#4c4a45', '#c9c6bb'),
    'Spotted Hyena': ('Spotted Hyena', 'Spotted Hyenas', 55, 1.5, 'dog', 'spots', '#a8946a', '#3d3222', '#cdbb93'),
    'Brown Bear': ('Brown Bear', 'Brown Bears', 300, 2.3, 'bear', '', '#4a3626', '#3a2a1e', '#5a4230'),
    'Polar Bear': ('Polar Bear', 'Polar Bears', 450, 2.6, 'bear', '', '#e6e3d8', '#bdb8a8', '#f4f2ea'),
    'African Bush Elephant': ('Elephant', 'Elephants', 6000, 6.5, 'elephant', '', '#77736c', '#55514b', '#efe6cf'),
    'Velociraptor mongoliensis': ('Velociraptor', 'Velociraptors', 15, 2.0, 'raptor', '', '#8a6f4d', '#5c4830', '#d9c8a0'),
    'Deinonychus antirrhopus': ('Deinonychus', 'Deinonychus', 73, 3.3, 'raptor', '', '#5d5346', '#3b352d', '#7fa0b8'),
    'Dakotaraptor steini': ('Dakotaraptor', 'Dakotaraptors', 250, 5.5, 'raptor', '', '#4d4038', '#2f2722', '#c9772e'),
    'Utahraptor ostrommaysorum': ('Utahraptor', 'Utahraptors', 500, 6.0, 'raptor', '', '#5a4433', '#3d2e22', '#a3492c'),
    'Dilophosaurus wetherilli': ('Dilophosaurus', 'Dilophosaurus', 400, 6.5, 'rex', 'crest', '#6a6a3c', '#48482a', '#c05a2e'),
    'Ceratosaurus nasicornis': ('Ceratosaurus', 'Ceratosaurus', 700, 6.0, 'rex', 'horn', '#7a4a34', '#4f2f22', '#d8c9a8'),
    'Carnotaurus sastrei': ('Carnotaurus', 'Carnotaurus', 1500, 8.0, 'rex', 'horns', '#7d4b3a', '#52302a', '#d8c9a8'),
    'Allosaurus fragilis': ('Allosaurus', 'Allosaurus', 1700, 8.5, 'rex', 'crest', '#5e5a44', '#3e3b2c', '#a8452c'),
    'Tyrannosaurus rex': ('T. rex', 'T. rexes', 8000, 12.3, 'rex', '', '#55603f', '#3c452c', '#e8c14a')}
COMPANIONS = {  # animals that fight beside people; same fields
    'German Shepherd': ('German Shepherd', 'German Shepherds', 35, 1.1, 'dog', '', '#9a7440', '#2e2620', '#c9a56a'),
    'Belgian Malinois': ('Belgian Malinois', 'Belgian Malinois', 28, 1.0, 'dog', '', '#b78a4a', '#2a211a', '#d4ad72'),
    'American Pit Bull Terrier': ('Pit Bull', 'Pit Bulls', 27, 0.9, 'dog', '', '#a7836a', '#5b4334', '#d2b59e'),
    'Rottweiler': ('Rottweiler', 'Rottweilers', 50, 1.2, 'dog', '', '#2a2522', '#15110f', '#9a5a2a'),
    'Dogo Argentino': ('Dogo Argentino', 'Dogos Argentinos', 43, 1.2, 'dog', '', '#ece8df', '#bdb6a8', '#f6f3ec'),
    'Kangal': ('Kangal', 'Kangals', 60, 1.4, 'dog', '', '#cdb287', '#3b2f22', '#e3cfa9'),
    'Alpine Mastiff': ('Alpine Mastiff', 'Alpine Mastiffs', 90, 1.5, 'dog', '', '#b88a55', '#4a3524', '#d9b78c'),
    'Cheetah': ('Cheetah', 'Cheetahs', 50, 2.0, 'cat', 'spots', '#d8b56a', '#2e2416', '#ead29a'),
    'Golden Eagle': ('Golden Eagle', 'Golden Eagles', 5, 0.9, 'bird', '', '#5a4630', '#3a2c1d', '#c9a45a'),
    'Wild Horse': ('Horse', 'Horses', 400, 2.2, 'hoof', 'horse', '#7a5536', '#2b1d12', '#a0764f'),
    'Shire Horse': ('Shire Horse', 'Shire Horses', 900, 2.6, 'hoof', 'horse', '#3d2e24', '#17110d', '#e9e4da'),
    'Dromedary (Arabian) Camel': ('Dromedary Camel', 'Dromedary Camels', 500, 3.0, 'hoof', 'camel', '#c9a878', '#8d744f', '#dcc39a'),
    'Iberian (Spanish) Fighting Bull': ('Fighting Bull', 'Fighting Bulls', 550, 2.5, 'hoof', 'bull', '#1f1b19', '#0e0c0b', '#e6dcc4')}


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
    if weapon in RANGED:
        plain = SKILL[skill][1] == 0 and skill != 'novice' and armour == 'none'
        return 'B' if plain and weapon == 'bolt-action rifle' else 'C' if plain and RANGED[weapon][1] else 'D'
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
    rng2 = np.random.default_rng(SEED + 1); later = {'ranged', 'body armour and helmet', 'tank armour'}   # everything added with the firearms draws from its own
    draw2 = lambda ms: rng2.normal(ms[0], ms[1], n) if ms[1] > 0 else np.full(n, float(ms[0]))            # stream, so that the earlier fighters keep their numbers
    pick = lambda key: draw2 if key in later else draw
    gamma = np.clip(draw(GAMMA), 0.15, 0.8); m_real = np.clip(draw(MASS_REAL), 0.5, 9); m_scale = draw((b_scale, MASS_SCALE_SD)); novice = np.clip(draw(NOVICE), 0.2, 1)
    human = draw((np.log(B.score['Human']), B.se_log['Human'])); fem = draw(female); sp = draw(spear[:2]); cl = draw((club[0], max(club[1], 0.4)))
    skill = {s: draw(v) for s, v in SKILL.items()}; transfer = {t: np.clip(pick(t)(v), 0, 1) for t, v in TRANSFER.items()}
    weapon = {w: draw(v[0]) for w, v in WEAPON.items()}; wpn_d = {w: draw(v[1]) for w, v in WEAPON.items()}; cross = np.clip(draw(CROSS), 0, 1); arm_b = {a: pick(a)(v[0]) for a, v in ARMOUR.items()}; arm_d = {a: pick(a)(v[1]) for a, v in ARMOUR.items()}
    # bows and firearms: the bear incidents fix how fast a weapon's premium grows with Dupuy's index
    tot = sum(BEAR['incidents'].values()); bear = sum(w / tot * rng2.normal(np.log(B.score[b]), B.se_log[b], n) for b, w in BEAR['incidents'].items())
    real = rng2.normal(np.log(BEAR['success'] / (1 - BEAR['success'])), np.hypot(BEAR['logit_sd'], BEAR['context_sd']), n)
    rifle = bear + gamma * real - human; beta = np.clip((rifle - sp) / np.log(TLI_RIFLE / TLI_HAND), 0.1, 1.2)   # rifle: log premium of the hunting rifle over the unarmed man
    rwl = {w: sp + beta * (np.log(v[0] / TLI_HAND) + (0.0 if w == 'bolt-action rifle' else rng2.normal(0, TLI_SD[v[1]], n))) for w, v in RANGED.items()}
    rwd = {w: draw2(v[2]) for w, v in RANGED.items()}; novice_gun = np.clip(draw2(NOVICE_GUN), 0.2, 1)
    rows, logs, duel, usk, ask, arm, body, dbody = [], {}, {}, {}, {}, {}, {}, {}
    for name, (sex, mass, wpn, sk, tr, armour, note) in ARCHETYPES.items():
        rg = wpn in RANGED; nov = (novice_gun if wpn in GUNS else novice) if sk == 'novice' else 1.0; sx = fem if sex == 'f' else 0.0; crew = RANGED[wpn][5] if rg else 1
        lm = np.log(mass / REF_MASS[sex]) * (RANGED_MASS if rg else ARMED_MASS if wpn else 1.0)
        wl = 0.0 if wpn is None else (cl if wpn == 'club' else rwl[wpn] if rg else sp + weapon[wpn]) * nov
        bd = human + sx + m_scale * lm + arm_b[armour] + gamma * transfer[tr] * skill[sk]; ls = bd + wl          # bd: the fighter without the weapon
        wd = 0.0 if wpn is None else (cl / gamma if wpn == 'club' else sp / gamma + (rwd[wpn] if rg else wpn_d[wpn])) * nov
        db = sx / gamma + m_real * lm + arm_d[armour] + skill[sk]; dl = db + wd
        logs[name], duel[name], usk[name] = ls, dl, (skill[sk] if wpn is None else None); p = np.exp(np.percentile(ls, [5, 50, 95])); e = 1000 + 400 / np.log(10) * np.percentile(dl, [5, 50, 95])
        ask[name] = skill[sk] if wpn is not None and wpn not in GUNS else None; arm[name] = arm_d[armour] if armour in OLD_ARMOUR else None
        body[name], dbody[name] = (ls, dl) if armour == 'tank armour' else (bd + np.log(crew), db + np.log(crew))   # what a hit has to get through (the page's staging)
        rows.append(dict(archetype=name, sex=sex, mass_kg=mass, weapon=wpn or 'none', skill=sk, armour=armour, score=p[1], score_p05=p[0], score_p95=p[2], lions=p[1] / 100,
                         duel_elo=e[1], duel_elo_p05=e[0], duel_elo_p95=e[2], lethality_index=RANGED[wpn][0] if rg else '', crew=crew,
                         unarmed_skill_elo=400 / np.log(10) * SKILL[sk][0] if wpn is None else 0.0, evidence=grade(wpn, sk, armour, mass, sex), note=note))
    T = pd.DataFrame(rows).sort_values('score', ascending=False); os.makedirs('outputs', exist_ok=True)
    T.to_csv('outputs/human_archetypes.csv', index=False, float_format='%.4g')
    names = list(T.archetype)   # P(row beats column), real odds, median over the draws
    def beats(a, b):
        da, db = duel[a], duel[b]
        if (usk[a] is None) != (usk[b] is None): da, db = (da - (1 - cross) * usk[a], db) if usk[b] is None else (da, db - (1 - cross) * usk[b])
        cut = lambda x, y: ((1 - cross) * (ask[x] if ask[x] is not None else 0) + (1 - ARMOUR_VS_GUNS) * (arm[x] if arm[x] is not None else 0)
                            if ARCHETYPES[y][2] in GUNS and ARCHETYPES[x][2] not in GUNS else 0)   # against firearms, blade skill and old armour count for little
        da, db = da - cut(a, b), db - cut(b, a)
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
                 transfer=TRANSFER, novice=NOVICE, skill_real_log_odds=SKILL, weapon_vs_spear=WEAPON, armour=ARMOUR, cross=CROSS, armour_vs_guns=ARMOUR_VS_GUNS,
                 firearms=dict(bear=BEAR, bear_scale=float(np.exp(np.median(bear))), rifle_score=float(np.exp(np.median(rifle + human))), rifle_premium_log=float(np.median(rifle)),
                               beta=float(np.median(beta)), beta_p05=float(np.percentile(beta, 5)), beta_p95=float(np.percentile(beta, 95)), index_hand=TLI_HAND, index_rifle=TLI_RIFLE,
                               weapons={w: dict(lethality_index=v[0], dupuy=v[1], premium_factor=float(np.exp(np.median(rwl[w]))), duel_log_odds_over_spear=v[2]) for w, v in RANGED.items()}),
                 raptors={r: dict(crowd=float(B.score[r]), corrected=float(B.full_p50[r]), corrected_p05=float(B.full_p05[r]), corrected_p95=float(B.full_p95[r])) for r in RAPTORS})
    json.dump(model, open('outputs/human_model.json', 'w'), indent=1)
    if os.path.exists(ARENA):   # refresh the data block of the arena page
        # a dinosaur's corrected log-score is its crowd log-score plus dmu, with the factor's own spread dsd (one draw shared by all dinosaurs)
        def fighter(a):
            sex, mass, wpn, sk, tr, armour, note = ARCHETYPES[a]; rg = wpn in RANGED
            d = dict(name=a, group='Bows and firearms' if rg else 'Fighters', mu=float(np.median(logs[a])), sd=sd(logs[a]), duel=float(np.median(duel[a])), duel_sd=sd(duel[a]),
                     usk=float(SKILL[sk][0]) if wpn is None else 0.0, ask=float(SKILL[sk][0]) if wpn is not None and wpn not in GUNS else 0.0,
                     arm=float(ARMOUR[armour][1][0]) if armour in OLD_ARMOUR else 0.0, gun=wpn in GUNS, weapon=wpn or 'none', armour=armour, mass=mass)
            if rg: d.update(rng=RANGED[wpn][4], shot=RANGED[wpn][3], crew=RANGED[wpn][5], size=RANGED[wpn][6], dur=float(np.median(body[a])), ddur=float(np.median(dbody[a])))
            return d
        beasts = {**ANIMALS, **COMPANIONS}
        data = dict(k=k_hat, k_sd=K_SD, gamma=GAMMA[0], gamma_sd=GAMMA[1], cross=CROSS[0], arm_vs_guns=ARMOUR_VS_GUNS,
                    fighters=[fighter(a) for a in sorted(names, key=lambda a: ARCHETYPES[a][2] in RANGED)],
                    animals=[dict(name=o, label=lab, plural=pl, kg=kg, length=L, shape=shp, coat=coat, body=bc, dark=dark, accent=acc, comp=o in COMPANIONS, mu=float(np.log(B.score[o])), sd=float(B.se_log[o]),
                                  dino=bool(B['class'][o] == 'dinosaur'), dmu=float(np.log(B.full_p50[o] / B.score[o])),
                                  dsd=float(np.sqrt(max((np.log(B.full_p95[o] / B.full_p05[o]) / 3.29)**2 - B.se_log[o]**2, 0.0))))
                             for o, (lab, pl, kg, L, shp, coat, bc, dark, acc) in beasts.items()])
        page = open(ARENA, encoding='utf-8').read(); a, b = page.find('/*DATA*/'), page.find('/*END DATA*/')
        if 0 <= a < b: open(ARENA, 'w', encoding='utf-8').write(page[:a] + '/*DATA*/const DATA = ' + json.dumps(data, separators=(',', ':')) + ';' + page[b:]); print('refreshed ../arena.html')
    print(f"measured on the scale: spear x{np.exp(spear[0]):.2f} (log {spear[0]:.2f} ± {spear[1]:.2f}), club x{np.exp(club[0]):.2f}, female x{np.exp(female[0]):.2f}, "
          f"group exponent {k_hat:.2f} ± {k_se:.2f} over {len(G)} group entries, mass exponent {b_scale:.2f}")
    print(f"firearms: bears of the Alaska sample {np.exp(np.median(bear)):.0f}, hunting rifle {np.exp(np.median(rifle + human)):.0f} "
          f"[{np.exp(np.percentile(rifle + human, 5)):.0f}-{np.exp(np.percentile(rifle + human, 95)):.0f}], beta {np.median(beta):.2f} [{np.percentile(beta, 5):.2f}-{np.percentile(beta, 95):.2f}]")
    print(T[['archetype', 'score', 'score_p05', 'score_p95', 'duel_elo', 'evidence']].to_string(index=False, float_format=lambda v: f'{v:,.1f}'))
    q = Vs[Vs.fighters.isin(VERSUS[1:2] + VERSUS[-2:]) & (Vs.group_exponent != '0.7 (step 3 rule)')]
    print(q[['raptor', 'fighters', 'raptor_score', 'group_exponent', 'n_even', 'n_even_p05', 'n_even_p95', 'share_n5', 'share_n10']].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    print('wrote outputs/human_archetypes.csv, outputs/human_duel_matrix.csv, outputs/humans_vs_raptors.csv, outputs/human_model.json')


if __name__ == '__main__':
    main()
