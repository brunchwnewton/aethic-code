#!/usr/bin/env python3
"""Bradley-Terry refit of the Carnivora.net Interspecific Conflict Directory duels (Dinosaur Recalibration, Sections 2-6).

Usage:  python3 bt_refit.py duels.csv            -> writes bt_scores_african_lion_100.csv and bt_refit_summary.json

duels.csv has no header: animal_a, animal_b, P(a beats b), votes.
Pipeline: name cleaning (ASCII allowlist + a corrections dictionary for the 24 corrupted names); exclusion of matchups
outside [5%, 95%]; the largest connected component of the filtered graph; gender pseudo-matchups (male beats base,
base beats female, p = 0.60, weight 10); group-to-solo pseudo-matchups (group beats solo with N^0.7/(N^0.7+1), weight 3);
weighted BT likelihood with L2 penalty 0.01 on log-strengths, maximized by L-BFGS; standard errors from the inverse of
the penalized observed information; normalization African Lion = 100; genus-based scaling classes; the elicited
lognormal anatomy model and its median rescaling. The original pipeline's manual island bridges, generic/regional
duplicate links and subspecies links are not reproduced (their lists were not preserved)."""
import sys, re, json, itertools
import numpy as np, pandas as pd, networkx as nx
from collections import Counter
from scipy import stats, optimize

LAMBDA, P_GENDER, W_GENDER, W_GROUP, GROUP_EXP = 0.01, 0.60, 10, 3, 0.7
FIX = {'Alano Espa\ufffdol': 'Alano Espanol', 'Alano Espa\ufffdols (2)': 'Alano Espanols (2)', 'Arctotherium\ufffdangustidens': 'Arctotherium angustidens',
 'Baird\ufffds Beaked Whale': "Baird's Beaked Whale", 'Cimarr\ufffdn Uruguayo': 'Cimarron Uruguayo', 'Cimarr\ufffdn Uruguayo (2)': 'Cimarron Uruguayo (2)',
 'Dhole\ufffd(female)': 'Dhole (female)', 'Galap\ufffdgos Islands Feral Dog': 'Galapagos Islands Feral Dog', 'Giganotosaurus\ufffdcarolinii': 'Giganotosaurus carolinii',
 'Haida Gwaii\ufffdBlack Bear': 'Haida Gwaii Black Bear', 'Lappet-faced Vultures\ufffd(venue of 4)': 'Lappet-faced Vultures (venue of 4)',
 'Lappet-faced Vulture\ufffd(venue of 2)': 'Lappet-faced Vulture (venue of 2)', 'Lappet-faced Vulture\ufffd(venue of 3)': 'Lappet-faced Vulture (venue of 3)',
 'Lettered Ara\ufffdari': 'Lettered Aracari', 'Megalictis\ufffdferox': 'Megalictis ferox', 'Molina\ufffds Hog-nosed Skunk': "Molina's Hog-nosed Skunk",
 'Morelet\ufffds Crocodile': "Morelet's Crocodile", 'Orca\ufffdPod (of 5)': 'Orca Pod (of 5)', "R\ufffdppell's Griffon Vulture": "Ruppell's Griffon Vulture",
 'Sarcosuchus\ufffdimperator': 'Sarcosuchus imperator', 'Sperm\ufffdWhale\ufffd(Bull)': 'Sperm Whale (Bull)', 'Ussuri\ufffdWild Boar': 'Ussuri Wild Boar',
 'Zalmoxes\ufffdshqiperorum': 'Zalmoxes shqiperorum', '\ufffdarplaninac': 'Sarplaninac'}

def clean(x):
    x = FIX.get(x, x)
    if '\ufffd' in x: x = re.sub(r'(?<=\w)\ufffd(?=\w)', '', x).replace('\ufffd', ' ')
    x = ''.join(c for c in x if 32 <= ord(c) < 127)
    return re.sub(r'\s+', ' ', x).strip()

DINOSAUR = set("""Achillobator Acrocanthosaurus Afrovenator Albertosaurus Alectrosaurus Aletopelta Alioramus Allosaurus Amargasaurus Ankylosaurus Anzu Apatosaurus
Archaeopteryx Astrodon Aucasaurus Australovenator Baryonyx Blikanasaurus Brontosaurus Carcharodontosaurus Carnotaurus Ceratosaurus Citipati Coelophysis
Compsognathus Cryolophosaurus Dacentrurus Dakotaraptor Daspletosaurus Deinocheirus Deinonychus Dilophosaurus Diplodocus Dromaeosauroides Dromaeosaurus
Edmontosaurus Ekrixinatosaurus Eocarcharia Eotriceratops Euoplocephalus Europasaurus Futalognkosaurus Gallimimus Gargoyleosaurus Gastonia Giganotosaurus
Gigantoraptor Gojirasaurus Gorgosaurus Herrerasaurus Hesperosaurus Iguanodon Irritator Kentrosaurus Liliensternus Linheraptor Maip Majungasaurus Mapusaurus
Marshosaurus Megalosaurus Megaraptor Metriacanthosaurus Minmi Monolophosaurus Moros Nanshiungosaurus Nanuqsaurus Nasutoceratops Neovenator Ohmdenosaurus
Orkoraptor Ornitholestes Ornithomimus Oxalaia Pachycephalosaurus Parasaurolophus Pentaceratops Phuwiangosaurus Protoceratops Psittacosaurus Pycnonemosaurus Rajasaurus
Rhoetosaurus Rugops Saltriovenator Saurophaganax Shantungosaurus Shaochilong Shunosaurus Siamotyrannus Siats Sigilmassasaurus Sinraptor Skorpiovenator
Spinosaurus Stegosaurus Stenonychosaurus Styracosaurus Suchomimus Suskityrannus Tarbosaurus Tenontosaurus Teratophoneus Thanos Therizinosaurus Timurlengia
Titanoceratops Torosaurus Torvosaurus Triceratops Tyrannosaurus Tyrannotitan Utahceratops Utahraptor Velociraptor Yamaceratops Yangchuanosaurus Yi
Yutyrannus Zhuchengtyrannus Zuniceratops""".split())
MESOZOIC_OTHER = set("""Archelon Arizonasaurus Armadillosuchus Batrachotomus Clidastes Cymbospondylus Dakosaurus Deinosuchus Elasmosaurus Erythrosuchus Fasolasuchus Globidens
Hatzegopteryx Himalayasaurus Ichthyosaurus Kaprosuchus Kronosaurus Liopleurodon Megacephalosaurus Mosasaurus Ophthalmosaurus Pliosaurus Postosuchus
Prestosuchus Prognathodon Proterosuchus Pteranodon Quetzalcoatlus Rauisuchus Sachicasaurus Sarcosuchus Saurosuchus Shastasaurus Shonisaurus Sillosuchus
Smilosuchus Smok Temnodontosaurus Thalattoarchon Tylosaurus""".split())
PERMIAN = set("""Dimetrodon Sphenacodon Secodontosaurus Anteosaurus Inostrancevia Lycaenops Rubidgea Estemmenosuchus Tapinocephalus Trochosuchus Lystrosaurus Helicoprion""".split())

def scaling_class(name):
    """dinosaur | mesozoic-other | baseline, by genus; plus a Permian flag (Permian animals are baseline)."""
    base = name.split(' (')[0].strip(); words = base.split(); first = words[0] if words else ''
    genus_like = bool(re.match(r'^[A-Z][a-z]+$', first)) and (len(words) == 1 or words[1][:1].islower())
    cls = 'baseline'
    if genus_like and first in DINOSAUR: cls = 'dinosaur'
    elif genus_like and first in MESOZOIC_OTHER: cls = 'mesozoic-other'
    return cls, genus_like and first in PERMIAN

def main(path):
    df = pd.read_csv(path, header=None, names=['a', 'b', 'p', 'n'])
    raw_names = len(set(df.a) | set(df.b)); df['a'] = df.a.map(clean); df['b'] = df.b.map(clean)
    real = df[(df.p >= .05) & (df.p <= .95)]
    G = nx.Graph(); G.add_edges_from(zip(real.a, real.b))
    comps = sorted(nx.connected_components(G), key=len, reverse=True); main_c = comps[0]
    real = real[real.a.isin(main_c) & real.b.isin(main_c)]
    pseudo = []
    for x in sorted(main_c):
        m, f = x + ' (male)', x + ' (female)'
        if m in main_c and f in main_c: pseudo += [(m, x, P_GENDER, W_GENDER, 'gender'), (x, f, P_GENDER, W_GENDER, 'gender')]
    GROUP = re.compile(r'^(.*?)\s*\((?:[A-Za-z ]*?\bof\s+)?(\d+(?:\s*[-/]\s*\d+)?)\)\s*$')
    def solo_of(base):
        base = re.sub(r'\s*\((?:females?|males?|cows?|bulls?)\)\s*$', '', base, flags=re.I).strip()
        words = base.split(); last = words[-1] if words else ''
        sing = [re.sub(r'ves$', 'f', last), re.sub(r'ies$', 'y', last), re.sub(r'es$', '', last), re.sub(r's$', '', last)]
        for c in [base] + [' '.join(words[:-1] + [w]) for w in sing] + [re.sub(r'\s+(Pod|Pack|Herd|Troop|Pride|Clan|Group|Cows|Bulls)$', '', base)]:
            if c in main_c: return c
        return None
    unmatched = 0
    for x in sorted(main_c):
        g = GROUP.match(x)
        if not g: continue
        nums = [float(v) for v in re.findall(r'\d+', g.group(2))]; N = sum(nums) / len(nums)
        if N < 2: continue
        s = solo_of(g.group(1).strip())
        if s and s != x: pseudo.append((x, s, N**GROUP_EXP / (N**GROUP_EXP + 1), W_GROUP, 'group'))
        else: unmatched += 1
    names = sorted(main_c); idx = {a: i for i, a in enumerate(names)}; K = len(names)
    rows = [(idx[a], idx[b], p * n, (1 - p) * n) for a, b, p, n in zip(real.a, real.b, real.p, real.n)] + [(idx[a], idx[b], p * w, (1 - p) * w) for a, b, p, w, _ in pseudo]
    I = np.array([r[0] for r in rows]); J = np.array([r[1] for r in rows]); Wi = np.array([r[2] for r in rows]); Wj = np.array([r[3] for r in rows]); Nt = Wi + Wj
    def nll(th):
        d = th[I] - th[J]; f = (Wi * np.logaddexp(0, -d) + Wj * np.logaddexp(0, d)).sum() + LAMBDA * (th**2).sum()
        ge = -(Wi - Nt / (1 + np.exp(-d))); g = np.zeros(K); np.add.at(g, I, ge); np.add.at(g, J, -ge); return f, g + 2 * LAMBDA * th
    res = optimize.minimize(nll, np.zeros(K), jac=True, method='L-BFGS-B', options={'maxiter': 20000, 'gtol': 1e-9}); th = res.x
    d = th[I] - th[J]; pp = 1 / (1 + np.exp(-d)); w = Nt * pp * (1 - pp)
    H = np.zeros((K, K)); np.add.at(H, (I, I), w); np.add.at(H, (J, J), w); np.add.at(H, (I, J), -w); np.add.at(H, (J, I), -w); H += 2 * LAMBDA * np.eye(K)
    Sig = np.linalg.inv(H); al = idx['African Lion']; se = np.sqrt(np.maximum(np.diag(Sig) + Sig[al, al] - 2 * Sig[:, al], 0))
    deg, votes = Counter(), Counter()
    for a, b, n in zip(real.a, real.b, real.n): deg[a] += 1; deg[b] += 1; votes[a] += n; votes[b] += n
    out = pd.DataFrame({'animal': names, 'log_score': th - th[al], 'se_log': se, 'real_matchups': [deg[x] for x in names], 'real_votes': [votes[x] for x in names]})
    out['score'] = 100 * np.exp(out.log_score)
    cl = out.animal.map(scaling_class); out['class'] = [c[0] for c in cl]; out['permian'] = [c[1] for c in cl]
    # the elicited anatomy model (Section 6): ladder on the African Lion, 2:1 log centring, 15% outside the anchors
    S = dict(zip(out.animal, out.score)); human = S['Human']; Dt = 100**2 / human; L = np.sqrt(Dt / S['Dakotaraptor steini']); U = Dt / S['Utahraptor ostrommaysorum']
    mu = (2 / 3) * np.log(L) + (1 / 3) * np.log(U)
    sigma = optimize.brentq(lambda s: stats.norm.cdf((np.log(L) - mu) / s) + 1 - stats.norm.cdf((np.log(U) - mu) / s) - .15, 1e-4, 5)
    sd = {'dinosaur': sigma, 'mesozoic-other': sigma / 2, 'baseline': 0.0}; fac = {'dinosaur': np.exp(mu), 'mesozoic-other': np.exp(mu / 2), 'baseline': 1.0}
    out['median_factor'] = out['class'].map(fac); out['median_score'] = out.score * out.median_factor
    out['band1_low'] = out.median_score * np.exp(-out['class'].map(sd)); out['band1_high'] = out.median_score * np.exp(out['class'].map(sd))
    out = out.sort_values('score', ascending=False); out.insert(0, 'rank', range(1, K + 1))
    cols = ['rank', 'animal', 'score', 'log_score', 'se_log', 'real_matchups', 'real_votes', 'class', 'permian', 'median_factor', 'median_score', 'band1_low', 'band1_high']
    out[cols].to_csv('bt_scores_african_lion_100.csv', index=False, float_format='%.6g')
    summary = dict(matchups=len(df), animals_raw=raw_names, animals_clean=len(set(df.a) | set(df.b)), excluded_outside_5_95=int(((df.p < .05) | (df.p > .95)).sum()),
                   main_component_animals=K, real_matchups=len(real), real_votes=int(real.n.sum()), gender_pseudo=sum(1 for p in pseudo if p[4] == 'gender'),
                   group_pseudo=sum(1 for p in pseudo if p[4] == 'group'), group_unmatched=unmatched, converged=bool(res.success),
                   anatomy_model=dict(human=human, D_target=Dt, strong=Dt / S['Dakotaraptor steini'], L=L, U=U, mu=mu, sigma=sigma, median=float(np.exp(mu))))
    json.dump(summary, open('bt_refit_summary.json', 'w'), indent=1, default=float); print(json.dumps(summary, indent=1, default=float))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'duels.csv')
