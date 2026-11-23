#!/usr/bin/env python3
"""Step 8 — human archetypes on the scale, and n fighters against a raptor (new; exploratory, not part of the paper).

Usage:  python3 8_human_archetypes.py      reads ../final_scores.csv (and outputs/graph/summary.json for the mass exponent)
        -> outputs/human_archetypes.csv, outputs/human_duel_matrix.csv, outputs/humans_vs_raptors.csv, outputs/human_model.json,
           outputs/titan_classes.csv (a fantasy race, placed by the same rules; see TITANS)
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
# For the arena page only, which simulates fights with bows and guns outright instead of scoring them. Stated assumptions:
# weapon: (rounds a second, muzzle energy J (None: explosive), chance to hit a man-sized target inside the next range for a practised
#          user under stress, that range m, reach m, how fast a crewed piece can be swung round rad/s, rounds before reloading, seconds to reload)
SIM = {'longbow': (0.17, 400, 0.35, 30, 150, None, 0, 0), 'flintlock musket': (0.05, 3000, 0.30, 40, 100, None, 0, 0), '9 mm pistol': (2.0, 500, 0.30, 12, 50, None, 15, 2.5),
       '.44 Magnum revolver': (1.0, 1400, 0.35, 15, 60, None, 6, 5), '12-gauge shotgun': (0.8, 3500, 0.55, 30, 100, None, 6, 7), 'bolt-action rifle': (0.4, 3800, 0.60, 80, 400, None, 5, 5),
       'double rifle': (1.5, 6900, 0.60, 50, 150, None, 2, 4), 'assault rifle': (3.0, 1750, 0.40, 60, 400, None, 30, 3), '.50 rifle': (0.3, 18000, 0.60, 150, 1000, None, 10, 6),
       'rocket launcher': (0.1, None, 0.50, 60, 300, None, 0, 0), 'machine gun': (10.0, 3400, 0.12, 80, 800, None, 200, 8), 'heavy machine gun': (8.0, 18000, 0.12, 100, 1500, 0.8, 100, 8),
       'field gun': (0.25, None, 0.75, 150, 2000, 0.12, 0, 0), 'howitzer': (0.12, None, 0.70, 150, 2000, 0.10, 0, 0), 'tank gun': (0.2, None, 0.75, 150, 2000, 0.42, 0, 0)}
SIM_SKILL = {'novice': 0.5, 'competent': 1.0, 'professional (armed)': 1.3, 'elite (armed)': 1.6}   # multiplies the chance to hit
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
    'Gun crewman with a pistol': ('m', 75, '9 mm pistol', 'competent', 'ranged', 'none', 'what a gun crew becomes on the arena page when it leaves its gun'),
}
# ---- a fantasy race, for the author's story ROTG: Titans, about twice a human's mass and built for it. Placed by the rules above. ----
BUILD = {'Titan': (1.54, 0.25), 'Alaarn': (1.54 * 1.25, 0.25)}   # D. strength over a human of the same mass: between a Neanderthal's on this scale (1.25) and a gorilla's (1.9).
#   Alaarn are "the Neanderthals of the Titans": the Titan's build times the premium the Neanderthal has over a human of its mass on this scale.
#   It is a body made for its size, so it counts in full with a weapon in hand (unlike mass, which a weapon halves).
REACH = {'unarmed': (3.0, 1.5), 'armed': (4.0, 2.0)}       # real log-odds per log of height. Unarmed: UFC fighters giving away 7 inches of reach or more win 37% (about
#   3 per log of reach; another study of 2,229 bouts finds almost nothing). Armed: D, set above the unarmed value. Among fighters of like size it is small; a Titan has a third more.
REF_HEIGHT = {'m': 1.70, 'f': 1.60}                        # the height that goes with the reference masses
LADDER = {'New Adamantine Guard': 1.605, 'Mid Adamantine Guard': 6.956, 'Veteran Adamantine Guard': 16.05, 'New Wolfpacks': 17.58, 'Veteran Wolfpacks': 30.86, 'Ascendent': 37.99}
#   the author's ladder of training schools, as ratios to a Titan Warrior; read here as odds in a duel between two Titans (skill belongs there; little of it carries to animals)
SCHOOL = {s: (2.3 + np.log(r), 1.0) for s, r in LADDER.items()}        # real log-odds over a habitual user; the plain warrior is 'professional (armed)', 2.3
KIT = ("warrior's arms", "warrior's armour")                           # a generic warrior: midway between spear and sword with a shield; between helmet and mail
T_M, T_F, H_M, H_F = 132.1, 117.7, 65.6, 56.2                          # kg: the author's Titans and humans
THICK, SHORT = 1.21, 0.96                                              # an Alaarn against a Titan, as a Neanderthal against a human. Heavier at equal height: Neanderthal men, 78-83 kg
A_M, A_F = T_M * THICK * SHORT**2.5, T_F * THICK * SHORT**2.5          #   at 164-168 cm, against this story's humans (65.6 kg at 1.651 m), mass going as height^2.5. And a little shorter.
#   (The one Alaarn with a known weight, Bear of the Woods, 335 kg at 2.855 m, is their greatest warrior and far out on the tail; his build index is 1.30 times the average Titan's.)
TALL = {('Titan', 'm'): 2.184, ('Titan', 'f'): 2.081, ('Alaarn', 'm'): 2.184 * SHORT, ('Alaarn', 'f'): 2.081 * SHORT, (None, 'm'): 1.651, (None, 'f'): 1.55}   # m
ALAARN_ARMS, ALAARN_ARMOUR = 'axe + shield', 'mail or plates with helmet'   # the author's: an Alaarn warrior is a Viking in kit, mail included
TITANS = {  # name: (sex, mass, weapon, skill, carry-over, armour, note, race or None, the author's own figure or None: it has no scale, only its ratios mean anything)
    'Unarmed Male Human': ('m', H_M, None, 'untrained', 'unarmed', 'none', '', None, 0.003608),
    'Unarmed Female Human': ('f', H_F, None, 'untrained', 'unarmed', 'none', '', None, 0.00056),
    'Male Human': ('m', H_M, 'spear', 'novice', 'beast', 'none', 'armed, untrained', None, 0.0472),
    'Female Human': ('f', H_F, 'spear', 'novice', 'beast', 'none', 'armed, untrained', None, 0.001985014338),
    'Human Warrior': ('m', H_M, KIT[0], 'professional (armed)', 'duellist', KIT[1], '', None, 0.1816651865),
    'Female Human Warrior': ('f', H_F, KIT[0], 'professional (armed)', 'duellist', KIT[1], '', None, 0.02940512765),
    'Human Warrior, elite (1.75 m, 75 kg)': ('m', 75, KIT[0], 'elite (armed)', 'duellist', KIT[1], 'for comparison: a veteran soldier', None, None),
    'Human Warrior, a giant (2.18 m, 132 kg)': ('m', T_M, KIT[0], 'professional (armed)', 'duellist', KIT[1], 'for comparison: a human at a Titan\'s size, without the Titan\'s build', None, None),
    'Unarmed Male Titan': ('m', T_M, None, 'untrained', 'unarmed', 'none', '', 'Titan', 0.011448),
    'Unarmed Female Titan': ('f', T_F, None, 'untrained', 'unarmed', 'none', '', 'Titan', 0.001888),
    'Male Titan': ('m', T_M, 'spear', 'novice', 'beast', 'none', 'armed, untrained', 'Titan', 0.3032),
    'Female Titan': ('f', T_F, 'spear', 'novice', 'beast', 'none', 'armed, untrained', 'Titan', 0.056184),
    'Titan Warrior': ('m', T_M, KIT[0], 'professional (armed)', 'duellist', KIT[1], '', 'Titan', 0.3884808165),
    'Female Titan Warrior': ('f', T_F, KIT[0], 'professional (armed)', 'duellist', KIT[1], '', 'Titan', 0.07198682782),
    'New Adamantine Guard': ('m', T_M, KIT[0], 'New Adamantine Guard', 'duellist', KIT[1], 'a training school', 'Titan', 0.6235647135),
    'Mid Adamantine Guard': ('m', T_M, KIT[0], 'Mid Adamantine Guard', 'duellist', KIT[1], 'a training school', 'Titan', 2.702113759),
    'Veteran Adamantine Guard': ('m', T_M, KIT[0], 'Veteran Adamantine Guard', 'duellist', KIT[1], 'a training school', 'Titan', 6.235647135),
    'New Wolfpacks': ('m', T_M, KIT[0], 'New Wolfpacks', 'duellist', KIT[1], 'a training school', 'Titan', 6.830112162),
    'Veteran Wolfpacks': ('m', T_M, KIT[0], 'Veteran Wolfpacks', 'duellist', KIT[1], 'a training school', 'Titan', 11.98907089),
    'Ascendent': ('m', T_M, KIT[0], 'Ascendent', 'duellist', KIT[1], 'a training school', 'Titan', 14.75769822),
    'Unarmed Male Alaarn': ('m', A_M, None, 'untrained', 'unarmed', 'none', 'not in the author\'s table', 'Alaarn', None),
    'Male Alaarn': ('m', A_M, 'spear', 'novice', 'beast', 'none', 'armed, untrained', 'Alaarn', 1.344128382),
    'Female Alaarn': ('f', A_F, 'spear', 'novice', 'beast', 'none', 'armed, untrained', 'Alaarn', 0.2490715997),
    'Alaarn Warrior': ('m', A_M, ALAARN_ARMS, 'professional (armed)', 'duellist', ALAARN_ARMOUR, 'modelled on a Viking: axe, shield and mail', 'Alaarn', 4.032385147),
    'Female Alaarn Warrior': ('f', A_F, ALAARN_ARMS, 'professional (armed)', 'duellist', ALAARN_ARMOUR, '', 'Alaarn', 0.7472147992)}
MEANS = {'Unarmed Human': ('Unarmed Male Human', 'Unarmed Female Human', 0.001392), 'Unarmed Titan': ('Unarmed Male Titan', 'Unarmed Female Titan', 0.0038),
         'Alaarn': ('Male Alaarn', 'Female Alaarn', 0.5786053979)}     # the rows without a sex: the geometric mean of the two
HEIGHT = {k: TALL[(v[7], v[0])] for k, v in TITANS.items()}; HEIGHT['Human Warrior, elite (1.75 m, 75 kg)'] = 1.75; HEIGHT['Human Warrior, a giant (2.18 m, 132 kg)'] = TALL[('Titan', 'm')]
# On the arena page a fighter is a training, arms and armour, and the body under them is a human's, a Titan's or an Alaarn's. Step 8 gives every
# archetype its numbers on each body (race_delta in main), so "Titan Warrior" there is the plain warrior below on a Titan's body, and a Titan
# legionary or a Titan gun crew come the same way. CLASSES exist only on that page, at the human reference body:
ROTG_GROUP = 'ROTG titles and schools (fantasy)'
CLASSES = {
    'Untrained woman with a spear': ('f', 58, 'spear', 'novice', 'beast', 'none', ''),
    'Roman veles, light spear and parma': ('m', 66, 'spear + small shield', 'competent', 'duellist', 'none', 'the skirmishers of the manipular legion; their javelins are not modelled'),
    'Roman hastatus, gladius and scutum': ('m', 68, 'sword + large shield', 'competent', 'duellist', 'mail or plates with helmet', 'the first line: the younger men'),
    'Roman triarius, hasta and scutum': ('m', 68, 'spear + shield', 'elite (armed)', 'duellist', 'mail or plates with helmet', 'the third line: the veterans. (The second line, the principes, is the legionary above.)'),
    'Warrior, spear or sword with shield': ('m', 70, KIT[0], 'professional (armed)', 'duellist', KIT[1], "the story's plain warrior"),
    'Woman warrior, spear or sword with shield': ('f', 58, KIT[0], 'professional (armed)', 'duellist', KIT[1], ''),
    'class: Alaarn Warrior': ('m', 70, ALAARN_ARMS, 'professional (armed)', 'duellist', ALAARN_ARMOUR, 'a title: the plain warrior, at home on an Alaarn'),
    **{'class: ' + s: ('m', 70, KIT[0], s, 'duellist', KIT[1], 'a Titan training school') for s in LADDER}}     # (the Titans of each school are in TITANS under the plain name)
# how they are listed and drawn there: group, native race (the page's letter), the weapon as drawn, a look. The looks are for the eye only:
# the Wolfpacks in black like assassins (the author's), the Adamantine Guard in bright steel behind large shields and the rest are guesses.
LOOK = lambda s: (dict(show='twin swords', look='wolf') if 'Wolfpacks' in s else dict(show='spear + large shield', look='adamant') if 'Adamantine' in s else dict(show='spear + shield', look='gold'))
PAGE = {'Warrior, spear or sword with shield': dict(show='spear + shield'), 'Woman warrior, spear or sword with shield': dict(show='spear + shield'),
        'class: Alaarn Warrior': dict(group=ROTG_GROUP, native='l'), **{'class: ' + s: dict(group=ROTG_GROUP, native='t', **LOOK(s)) for s in LADDER}}
RACES = {'t': 'Titan', 'l': 'Alaarn'}                                  # the page's letter for each race (a human is 'f')
SKIN = {'Titan': '#ab81e4', 'Alaarn': '#3e3748'}                       # the author's
STOP = {'Titan': 0.7, 'Alaarn': 0.8}                                   # D. page's gun fights: the energy that stops one, as a share of an animal's of its weight (a human: 0.4)
RACE_BODY = {'Titan': {'m': (T_M, TALL[('Titan', 'm')]), 'f': (T_F, TALL[('Titan', 'f')])}, 'Alaarn': {'m': (A_M, TALL[('Alaarn', 'm')]), 'f': (A_F, TALL[('Alaarn', 'f')])}}
#   A class keeps its own build on the new body: a 78 kg murmillo is 78/70 of the average man, and so of the average Titan (147 kg).
DRAWN = {'Titan': (1.33, 1.0), 'Alaarn': (1.33 * SHORT, 1.25)}                 # height over a human's, and breadth over a Titan's, for the page
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
    SKILL.update(SCHOOL); WEAPON[KIT[0]] = ((0.05, 0.3), (0.65, 0.5)); ARMOUR[KIT[1]] = ((0.3, 0.2), (1.0, 0.5)); OLD_ARMOUR.add(KIT[1])
    rng2 = np.random.default_rng(SEED + 1); later = {'ranged', 'body armour and helmet', 'tank armour'}; rng3 = np.random.default_rng(SEED + 2); titan = {*SCHOOL, *KIT}   # everything added with the firearms draws from its own
    draw2 = lambda ms: rng2.normal(ms[0], ms[1], n) if ms[1] > 0 else np.full(n, float(ms[0]))            # stream, so that the earlier fighters keep their numbers
    draw3 = lambda ms: rng3.normal(ms[0], ms[1], n) if ms[1] > 0 else np.full(n, float(ms[0]))            # (and the Titans a third)
    pick = lambda key: draw3 if key in titan else draw2 if key in later else draw
    gamma = np.clip(draw(GAMMA), 0.15, 0.8); m_real = np.clip(draw(MASS_REAL), 0.5, 9); m_scale = draw((b_scale, MASS_SCALE_SD)); novice = np.clip(draw(NOVICE), 0.2, 1)
    human = draw((np.log(B.score['Human']), B.se_log['Human'])); fem = draw(female); sp = draw(spear[:2]); cl = draw((club[0], max(club[1], 0.4)))
    skill = {s: pick(s)(v) for s, v in SKILL.items()}; transfer = {t: np.clip(pick(t)(v), 0, 1) for t, v in TRANSFER.items()}
    weapon = {w: pick(w)(v[0]) for w, v in WEAPON.items()}; wpn_d = {w: pick(w)(v[1]) for w, v in WEAPON.items()}; cross = np.clip(draw(CROSS), 0, 1); arm_b = {a: pick(a)(v[0]) for a, v in ARMOUR.items()}; arm_d = {a: pick(a)(v[1]) for a, v in ARMOUR.items()}
    # bows and firearms: the bear incidents fix how fast a weapon's premium grows with Dupuy's index
    tot = sum(BEAR['incidents'].values()); bear = sum(w / tot * rng2.normal(np.log(B.score[b]), B.se_log[b], n) for b, w in BEAR['incidents'].items())
    real = rng2.normal(np.log(BEAR['success'] / (1 - BEAR['success'])), np.hypot(BEAR['logit_sd'], BEAR['context_sd']), n)
    rifle = bear + gamma * real - human; beta = np.clip((rifle - sp) / np.log(TLI_RIFLE / TLI_HAND), 0.1, 1.2)   # rifle: log premium of the hunting rifle over the unarmed man
    rwl = {w: sp + beta * (np.log(v[0] / TLI_HAND) + (0.0 if w == 'bolt-action rifle' else rng2.normal(0, TLI_SD[v[1]], n))) for w, v in RANGED.items()}
    rwd = {w: draw2(v[2]) for w, v in RANGED.items()}; novice_gun = np.clip(draw2(NOVICE_GUN), 0.2, 1)
    rows, trows, logs, duel, usk, ask, arm, body, dbody = [], [], {}, {}, {}, {}, {}, {}, {}
    bld = {r: rng3.normal(np.log(v[0]), v[1], n) for r, v in BUILD.items()}; reach = {r: np.clip(rng3.normal(v[0], v[1], n), 0, None) for r, v in REACH.items()}; ALL = {**{k: v + (None, None) for k, v in {**ARCHETYPES, **CLASSES}.items()}, **TITANS}
    for name, (sex, mass, wpn, sk, tr, armour, note, race, authors) in ALL.items():
        bl = bld[race] if race else 0.0                                                                # a Titan's build
        rc = reach['armed' if wpn else 'unarmed'] * np.log(HEIGHT[name] / REF_HEIGHT[sex]) if name in HEIGHT and wpn not in RANGED else 0.0   # and reach, in real log-odds
        rg = wpn in RANGED; nov = (novice_gun if wpn in GUNS else novice) if sk == 'novice' else 1.0; sx = fem if sex == 'f' else 0.0; crew = RANGED[wpn][5] if rg else 1
        lm = np.log(mass / REF_MASS[sex]) * (RANGED_MASS if rg else ARMED_MASS if wpn else 1.0)
        wl = 0.0 if wpn is None else (cl if wpn == 'club' else rwl[wpn] if rg else sp + weapon[wpn]) * nov
        bd = human + sx + m_scale * lm + bl + gamma * rc + arm_b[armour] + gamma * transfer[tr] * skill[sk]; ls = bd + wl     # bd: the fighter without the weapon
        wd = 0.0 if wpn is None else (cl / gamma if wpn == 'club' else sp / gamma + (rwd[wpn] if rg else wpn_d[wpn])) * nov
        db = sx / gamma + m_real * lm + bl * m_real / m_scale + rc + arm_d[armour] + skill[sk]; dl = db + wd
        logs[name], duel[name], usk[name] = ls, dl, (skill[sk] if wpn is None else None); p = np.exp(np.percentile(ls, [5, 50, 95])); e = 1000 + 400 / np.log(10) * np.percentile(dl, [5, 50, 95])
        ask[name] = skill[sk] if wpn is not None and wpn not in GUNS else None; arm[name] = arm_d[armour] if armour in OLD_ARMOUR else None
        body[name], dbody[name] = (ls, dl) if armour == 'tank armour' else (bd + np.log(crew), db + np.log(crew))   # what a hit has to get through (the page's staging)
        if name in TITANS:
            trows.append(dict(cls=name, race=race or 'Human', sex=sex, mass_kg=mass, weapon=wpn or 'none', skill=sk, armour=armour, authors_figure=authors if authors else np.nan,
                              score=p[1], score_p05=p[0], score_p95=p[2], lions=p[1] / 100, duel_elo=e[1], note=note)); continue
        if name in CLASSES: continue
        rows.append(dict(archetype=name, sex=sex, mass_kg=mass, weapon=wpn or 'none', skill=sk, armour=armour, score=p[1], score_p05=p[0], score_p95=p[2], lions=p[1] / 100,
                         duel_elo=e[1], duel_elo_p05=e[0], duel_elo_p95=e[2], lethality_index=RANGED[wpn][0] if rg else '', crew=crew,
                         unarmed_skill_elo=400 / np.log(10) * SKILL[sk][0] if wpn is None else 0.0, evidence=grade(wpn, sk, armour, mass, sex), note=note))
    def race_delta(a, race, bare=False):   # what a Titan's or an Alaarn's body adds to a class: to its log score, to its real log-odds; and the mass it then has
        sex, mass, wpn = ALL[a][:3]; wpn = None if bare else wpn; rg = wpn in RANGED; w = RANGED_MASS if rg else ARMED_MASS if wpn else 1.0; M, H = RACE_BODY[race][sex]   # bare: the body itself, weapon aside
        lm = np.log(M / REF_MASS[sex]) * w; bl = bld[race] * (RANGED_MASS if rg else 1.0)        # behind a bow or a gun the build counts as little as the mass does
        rc = 0.0 if rg else reach['armed' if wpn else 'unarmed'] * np.log(H / REF_HEIGHT[sex])
        return m_scale * lm + bl + gamma * rc, m_real * lm + bl * m_real / m_scale + rc, mass * M / REF_MASS[sex]
    for letter, race in RACES.items():   # the page's bodies agree with the story's table
        for a, b in (('Untrained man', f'Unarmed Male {race}'), ('Warrior, spear or sword with shield' if race == 'Titan' else 'class: Alaarn Warrior', f'{race} Warrior'), ('Untrained woman with a spear', f'Female {race}')) + ((('class: Ascendent', 'Ascendent'),) if race == 'Titan' else ()):
            d = race_delta(a, race); assert abs(np.median(logs[a] + d[0]) - np.median(logs[b])) < 1e-9 and abs(np.median(duel[a] + d[1]) - np.median(duel[b])) < 1e-9, (a, b)
    T = pd.DataFrame(rows).sort_values('score', ascending=False); os.makedirs('outputs', exist_ok=True)
    T.to_csv('outputs/human_archetypes.csv', index=False, float_format='%.4g')
    for g, (a, b, authors) in MEANS.items():   # the rows without a sex
        ls = (logs[a] + logs[b]) / 2; p = np.exp(np.percentile(ls, [5, 50, 95])); r = next(t for t in trows if t['cls'] == a)
        trows.append(dict(cls=g, race=r['race'], sex='both', mass_kg=np.nan, weapon=r['weapon'], skill=r['skill'], armour=r['armour'], authors_figure=authors, score=p[1], score_p05=p[0],
                          score_p95=p[2], lions=p[1] / 100, duel_elo=1000 + 400 / np.log(10) * float(np.median((duel[a] + duel[b]) / 2)), note='geometric mean of man and woman'))
    TT = pd.DataFrame(trows); anchor = TT.set_index('cls').loc['Male Human']   # the author's figures have no scale: set it where the armed, untrained man agrees
    TT.insert(TT.columns.get_loc('authors_figure') + 1, 'authors_rescaled', TT.authors_figure * anchor.score / anchor.authors_figure)
    TT.to_csv('outputs/titan_classes.csv', index=False, float_format='%.4g')
    odds = lambda a, b: float(np.median(1 / (1 + np.exp(duel[b] - duel[a]))))   # a duel between two of the story's classes
    for a, b in (('Titan Warrior', 'Human Warrior'), ('Titan Warrior', 'Human Warrior, elite (1.75 m, 75 kg)'), ('Titan Warrior', 'Human Warrior, a giant (2.18 m, 132 kg)'),
                 ('Human Warrior, a giant (2.18 m, 132 kg)', 'Human Warrior, elite (1.75 m, 75 kg)'), ('Human Warrior, a giant (2.18 m, 132 kg)', 'Human Warrior'),
                 ('Unarmed Male Titan', 'Unarmed Male Human'), ('Alaarn Warrior', 'Titan Warrior'), ('Ascendent', 'Titan Warrior')):
        print(f'duel: {a} beats {b} {odds(a, b):.1%}')
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
    kinds = {'unarmed': 'Untrained man', 'armed': 'Untrained man with a spear', 'behind a bow or a gun': 'Hunter, bolt-action .30-06 rifle', 'unarmed woman': 'Untrained woman'}
    model['race_body'] = {race: {kd: dict(score_factor=float(np.exp(np.median(race_delta(a, race)[0]))), rating_points=float(400 / np.log(10) * np.median(race_delta(a, race)[1]))) for kd, a in kinds.items()}
                          for race in RACES.values()}
    json.dump(model, open('outputs/human_model.json', 'w'), indent=1)
    if os.path.exists(ARENA):   # refresh the data block of the arena page
        # a dinosaur's corrected log-score is its crowd log-score plus dmu, with the factor's own spread dsd (one draw shared by all dinosaurs)
        def fighter(a):
            sex, mass, wpn, sk, tr, armour, note, race, _ = ALL[a]; rg = wpn in RANGED; med = lambda v: float(np.median(v))
            d = dict(name=a.replace('class: ', ''), group='Bows and firearms' if rg else 'Fighters', mu=float(np.median(logs[a])), sd=sd(logs[a]), duel=float(np.median(duel[a])), duel_sd=sd(duel[a]),
                     usk=float(SKILL[sk][0]) if wpn is None else 0.0, ask=float(SKILL[sk][0]) if wpn is not None and wpn not in GUNS else 0.0,
                     arm=float(ARMOUR[armour][1][0]) if armour in OLD_ARMOUR else 0.0, gun=wpn in GUNS, weapon=wpn or 'none', armour=armour, mass=mass)
            if rg: d.update(rng=RANGED[wpn][4], shot=RANGED[wpn][3], crew=RANGED[wpn][5], size=RANGED[wpn][6], dur=float(np.median(body[a])), ddur=float(np.median(dbody[a])),
                            sim=dict(rof=SIM[wpn][0], E=SIM[wpn][1], acc=min(0.95, SIM[wpn][2] * SIM_SKILL[sk]), r0=SIM[wpn][3], reach=SIM[wpn][4], trav=SIM[wpn][5], mag=SIM[wpn][6], reload=SIM[wpn][7]))
            if armour != 'tank armour':   # the same class on a Titan's and on an Alaarn's body: score, its spread, duel log-odds, its spread, mass; and for a gun what a hit is set against
                d['r'] = {}
                for letter, rc_ in RACES.items():
                    dl_, dd_, m2 = race_delta(a, rc_); d['r'][letter] = [med(logs[a] + dl_), sd(logs[a] + dl_), med(duel[a] + dd_), sd(duel[a] + dd_), round(float(m2), 1)] + ([med(body[a] + race_delta(a, rc_, True)[0]), med(dbody[a] + race_delta(a, rc_, True)[1])] if rg else [])   # a hit lands on the body, not on the gun
            d.update(PAGE.get(a, {})); return d
        force = lambda r: (RACE_BODY[r]['m'][0] / RACE_BODY[r]['m'][1]) / (REF_MASS['m'] / REF_HEIGHT['m']) * BUILD[r][0] ** ((2 / 3) / b_scale)   # muscular force over the reference man's
        races = {letter: dict(name=r, skin=SKIN[r], scale=DRAWN[r][0], bulk=DRAWN[r][1], stop=STOP[r], haul=round(float(force(r)), 2),   # haul: how much faster a crew swings its gun round
                              bow=round(float(force(r) * RACE_BODY[r]['m'][1] / REF_HEIGHT['m']), 2)) for letter, r in RACES.items()}             # bow: an arrow's energy, draw weight x draw length
        on_page = sorted(names + list(CLASSES), key=lambda a: (2, list(CLASSES).index(a)) if PAGE.get(a, {}).get('group') else (int(ALL[a][2] in RANGED), -float(np.median(logs[a]))))
        beasts = {**ANIMALS, **COMPANIONS}
        data = dict(k=k_hat, k_sd=K_SD, gamma=GAMMA[0], gamma_sd=GAMMA[1], cross=CROSS[0], arm_vs_guns=ARMOUR_VS_GUNS, races=races,
                    fighters=[fighter(a) for a in on_page],
                    animals=[dict(name=o, label=lab, plural=pl, kg=kg, length=L, shape=shp, coat=coat, body=bc, dark=dark, accent=acc, comp=o in COMPANIONS, mu=float(np.log(B.score[o])), sd=float(B.se_log[o]),
                                  dino=bool(B['class'][o] == 'dinosaur'), dmu=float(np.log(B.full_p50[o] / B.score[o])),
                                  dsd=float(np.sqrt(max((np.log(B.full_p95[o] / B.full_p05[o]) / 3.29)**2 - B.se_log[o]**2, 0.0))))
                             for o, (lab, pl, kg, L, shp, coat, bc, dark, acc) in beasts.items()])
        page = open(ARENA, encoding='utf-8').read(); a, b = page.find('/*DATA*/'), page.find('/*END DATA*/')
        if 0 <= a < b: open(ARENA, 'w', encoding='utf-8').write(page[:a] + '/*DATA*/const DATA = ' + json.dumps(data, separators=(',', ':')) + ';' + page[b:]); print('refreshed ../arena.html')
    print(TT[['cls', 'authors_rescaled', 'score', 'score_p05', 'score_p95', 'duel_elo']].to_string(index=False, float_format=lambda v: f'{v:,.1f}'))
    print(f"measured on the scale: spear x{np.exp(spear[0]):.2f} (log {spear[0]:.2f} ± {spear[1]:.2f}), club x{np.exp(club[0]):.2f}, female x{np.exp(female[0]):.2f}, "
          f"group exponent {k_hat:.2f} ± {k_se:.2f} over {len(G)} group entries, mass exponent {b_scale:.2f}")
    print(f"firearms: bears of the Alaska sample {np.exp(np.median(bear)):.0f}, hunting rifle {np.exp(np.median(rifle + human)):.0f} "
          f"[{np.exp(np.percentile(rifle + human, 5)):.0f}-{np.exp(np.percentile(rifle + human, 95)):.0f}], beta {np.median(beta):.2f} [{np.percentile(beta, 5):.2f}-{np.percentile(beta, 95):.2f}]")
    print(T[['archetype', 'score', 'score_p05', 'score_p95', 'duel_elo', 'evidence']].to_string(index=False, float_format=lambda v: f'{v:,.1f}'))
    q = Vs[Vs.fighters.isin(VERSUS[1:2] + VERSUS[-2:]) & (Vs.group_exponent != '0.7 (step 3 rule)')]
    print(q[['raptor', 'fighters', 'raptor_score', 'group_exponent', 'n_even', 'n_even_p05', 'n_even_p95', 'share_n5', 'share_n10']].to_string(index=False, float_format=lambda v: f'{v:.2f}'))
    print('wrote outputs/human_archetypes.csv, outputs/human_duel_matrix.csv, outputs/humans_vs_raptors.csv, outputs/human_model.json, outputs/titan_classes.csv')


if __name__ == '__main__':
    main()
