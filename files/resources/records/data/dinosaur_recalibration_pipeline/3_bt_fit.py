#!/usr/bin/env python3
"""Step 3 — Bradley-Terry fit (replaces the earlier 3_power_assembler.py).

Usage:  python3 3_bt_fit.py [duels.csv]          -> outputs/bt_scores.csv, outputs/bt_fit_summary.json

Input: the scraped duels (no header; animal_a, animal_b, P(a beats b), votes). Comma- or tab-separated files are both
accepted, so the raw output of 2_scrape_duels.py (tab-separated duel.csv) can be used directly.

Pipeline (paper, Sections 2-4):
  1. Name cleaning: ASCII allowlist, with a corrections dictionary for the 24 names carrying U+FFFD, and an alias list
     merging spelling, case and alternate-name variants of the same animal (ALIASES).
  2. Filtering: matchups with win probability outside [5%, 95%] are excluded from the fitted graph.
  3. Connectivity: the largest connected component of the filtered graph is kept (a Bradley-Terry scale is only
     defined within a connected graph).
  4. Pseudo-matchups: gender (male beats base and base beats female, p = 0.60, weight 10), and group-to-solo
     (group beats solo with probability N^0.7/(N^0.7+1), weight 3).
  5. Weighted Bradley-Terry likelihood with L2 penalty 0.01 on log-strengths, maximized by L-BFGS and polished by exact
     Newton steps until the Bradley-Terry score equations hold to machine precision; standard errors
     from the inverse of the penalized observed information; scores normalized so that African Lion = 100.

What changed from 3_power_assembler.py: the same model and penalty, plus steps 3-4, ASCII cleaning with explicit
corrections, the African Lion = 100 normalization (instead of median = 1), and standard errors. The original
pipeline's manual island bridges, generic/regional duplicate links and subspecies links are not reproduced (their
lists were not preserved); the paper's cultural-inflation analysis relies on generic entries being fitted from their
own votes."""
import sys, os, re, csv, json
import numpy as np, pandas as pd, networkx as nx
from collections import Counter
from scipy import optimize

LAMBDA, P_LO, P_HI = 0.01, 0.05, 0.95
P_GENDER, W_GENDER, W_GROUP, GROUP_EXP = 0.60, 10, 3, 0.7
FIX = {'Alano Espa\ufffdol': 'Alano Espanol', 'Alano Espa\ufffdols (2)': 'Alano Espanols (2)', 'Arctotherium\ufffdangustidens': 'Arctotherium angustidens',
 'Baird\ufffds Beaked Whale': "Baird's Beaked Whale", 'Cimarr\ufffdn Uruguayo': 'Cimarron Uruguayo', 'Cimarr\ufffdn Uruguayo (2)': 'Cimarron Uruguayo (2)',
 'Dhole\ufffd(female)': 'Dhole (female)', 'Galap\ufffdgos Islands Feral Dog': 'Galapagos Islands Feral Dog', 'Giganotosaurus\ufffdcarolinii': 'Giganotosaurus carolinii',
 'Haida Gwaii\ufffdBlack Bear': 'Haida Gwaii Black Bear', 'Lappet-faced Vultures\ufffd(venue of 4)': 'Lappet-faced Vultures (venue of 4)',
 'Lappet-faced Vulture\ufffd(venue of 2)': 'Lappet-faced Vulture (venue of 2)', 'Lappet-faced Vulture\ufffd(venue of 3)': 'Lappet-faced Vulture (venue of 3)',
 'Lettered Ara\ufffdari': 'Lettered Aracari', 'Megalictis\ufffdferox': 'Megalictis ferox', 'Molina\ufffds Hog-nosed Skunk': "Molina's Hog-nosed Skunk",
 'Morelet\ufffds Crocodile': "Morelet's Crocodile", 'Orca\ufffdPod (of 5)': 'Orca Pod (of 5)', "R\ufffdppell's Griffon Vulture": "Ruppell's Griffon Vulture",
 'Sarcosuchus\ufffdimperator': 'Sarcosuchus imperator', 'Sperm\ufffdWhale\ufffd(Bull)': 'Sperm Whale (Bull)', 'Ussuri\ufffdWild Boar': 'Ussuri Wild Boar',
 'Zalmoxes\ufffdshqiperorum': 'Zalmoxes shqiperorum', '\ufffdarplaninac': 'Sarplaninac'}

# Spelling, case and alternate-name variants of the same animal, merged onto one name (variant -> canonical), and plain
# typos corrected. Applied after cleaning, so every vote for an animal lands on one entry.
ALIASES = {
    'American Pitbull Terrier': 'American Pit Bull Terrier', 'Brown hyena': 'Brown Hyena', 'Dhole (Pack of 2)': 'Dhole (pack of 2)',
    'Edmontosaurus Annectens': 'Edmontosaurus annectens', 'Ethiopian Wolf (Simian Jackal)': 'Ethiopian Wolf (Simian jackal)',
    'Eurasian Eagle Owl': 'Eurasian Eagle-owl', 'Grey Wolf (Pack of 10)': 'Grey Wolf (pack of 10)', 'Kodiak bear': 'Kodiak Bear',
    'Lion (coalition of 5)': 'Lion (Coalition of 5)', 'Scottish Wild Cat': 'Scottish Wildcat', 'Tibetan Mastiffs(2)': 'Tibetan Mastiffs (2)',
    'Bearded Vulture (Lammergeier)': 'Bearded Vulture', 'Bonobo': 'Bonobo (Pygmy Chimpanzee)', 'Eastern Coyote (Coywolf)': 'Eastern Coyote',
    'Indonesian Wild Boar (Banded Pig)': 'Indonesian Wild Boar', 'Nile Monitor (Leguan)': 'Nile Monitor', 'Orca': 'Orca (Killer Whale)',
    'Shortfin Mako': 'Shortfin Mako Shark', 'Spinosaurus aegypticus': 'Spinosaurus aegyptiacus', 'Boryaena tuberata': 'Borhyaena tuberata',
    'Sectretary Bird': 'Secretary Bird', 'Woods Bison': 'Wood Bison', 'Boerbel': 'Boerboel', 'Proterogyrinus scheeleri': 'Proterogyrinus scheelei',
    # typos with no twin
    'Alaskan Penisula Brown Bear': 'Alaskan Peninsula Brown Bear', 'Livestock Gaurdian Donkey': 'Livestock Guardian Donkey',
    'Mexican Beaded LIzard': 'Mexican Beaded Lizard', 'Sago pedo': 'Saga pedo', 'Wonambi naracoortensi': 'Wonambi naracoortensis',
    'Jagdterriers (pack of3/4)': 'Jagdterriers (pack of 3/4)',
}


def clean(x):
    x = FIX.get(x, x)
    if '\ufffd' in x: x = re.sub(r'(?<=\w)\ufffd(?=\w)', '', x).replace('\ufffd', ' ')
    x = ''.join(c for c in x if 32 <= ord(c) < 127)
    x = re.sub(r'\s+', ' ', x).strip()
    return ALIASES.get(x, x)


def load(path):
    with open(path, encoding='utf-8', errors='replace') as f: first = f.readline()
    sep = '\t' if first.count('\t') >= 3 else ','
    df = pd.read_csv(path, header=None, names=['a', 'b', 'p', 'n'], sep=sep, quoting=csv.QUOTE_MINIMAL)
    raw = len(set(df.a) | set(df.b)); df['a'] = df.a.map(clean); df['b'] = df.b.map(clean)
    return df, raw


def fit(path='duels.csv'):
    """Return (names, theta relative to African Lion, covariance of theta, per-animal counts, summary)."""
    df, raw_names = load(path)
    real = df[(df.p >= P_LO) & (df.p <= P_HI)]
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
            c = ALIASES.get(c, c)
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
    def hessian(th):
        d = th[I] - th[J]; pp = 1 / (1 + np.exp(-d)); w = Nt * pp * (1 - pp)
        H = np.zeros((K, K)); np.add.at(H, (I, I), w); np.add.at(H, (J, J), w); np.add.at(H, (I, J), -w); np.add.at(H, (J, I), -w)
        return H + 2 * LAMBDA * np.eye(K)
    # Newton polishing: L-BFGS stops early in weakly connected corners of the graph; exact Newton steps on the
    # (positive definite) penalized Hessian solve the Bradley-Terry score equations to machine precision.
    newton_steps = 0
    for newton_steps in range(1, 31):
        step = np.linalg.solve(hessian(th), nll(th)[1]); th = th - step
        if np.abs(step).max() < 1e-12: break
    H = hessian(th); max_score_residual = float(np.abs(nll(th)[1]).max())
    Sig = np.linalg.inv(H); al = idx['African Lion']; th = th - th[al]
    deg, votes = Counter(), Counter()
    for a, b, n in zip(real.a, real.b, real.n): deg[a] += 1; deg[b] += 1; votes[a] += n; votes[b] += n
    summary = dict(matchups=int(len(df)), animals_raw=int(raw_names), animals_clean=int(len(set(df.a) | set(df.b))), excluded_outside_5_95=int(((df.p < P_LO) | (df.p > P_HI)).sum()),
                   components=len(comps), two_animal_islands=sum(1 for c in comps if len(c) == 2), larger_islands=sum(1 for c in comps[1:] if len(c) >= 3),
                   main_component_animals=K, real_matchups=int(len(real)), real_votes=int(real.n.sum()), gender_pseudo=sum(1 for p in pseudo if p[4] == 'gender'),
                   group_pseudo=sum(1 for p in pseudo if p[4] == 'group'), group_unmatched=unmatched, converged=bool(res.success),
                   newton_steps=newton_steps, max_score_equation_residual=max_score_residual)
    return names, idx, th, Sig, deg, votes, summary


def main(path):
    names, idx, th, Sig, deg, votes, summary = fit(path)
    al = idx['African Lion']; se = np.sqrt(np.maximum(np.diag(Sig) + Sig[al, al] - 2 * Sig[:, al], 0))
    out = pd.DataFrame({'animal': names, 'score': 100 * np.exp(th), 'log_score': th, 'se_log': se, 'real_matchups': [deg[x] for x in names], 'real_votes': [votes[x] for x in names]})
    out = out.sort_values('score', ascending=False); out.insert(0, 'rank', range(1, len(out) + 1))
    os.makedirs('outputs', exist_ok=True); out.to_csv('outputs/bt_scores.csv', index=False, float_format='%.6g')
    json.dump(summary, open('outputs/bt_fit_summary.json', 'w'), indent=1); print(json.dumps(summary, indent=1)); print("wrote outputs/bt_scores.csv")


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'duels.csv')
