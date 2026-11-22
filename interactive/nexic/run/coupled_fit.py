#!/usr/bin/env python3
"""Category-graph models with error bars (new): the merge (variant A) and the coupled model (variant B).

Usage:  python3 coupled_fit.py [duels.csv]          reads category_graph.csv  ->  ../final_scores.csv, outputs/graph/

The end result is ../final_scores.csv, in the nexic folder beside the paper: variant B's scores. outputs/graph/ holds the
paper's fit and variant A in the same layout, for comparison, with categories.csv and summary.json.

Step 3 places every entry by its own votes, so a broad name such as "Tiger" and its sub-categories such as
"Bengal Tiger" are fitted apart. Two variants use the category graph of category_graph.py:
  A  merge    each taxon tree collapses into its top name; duels inside a tree become self-matchups and are dropped.
              Sex forms stay separate fighters, so step 3's gender pseudo-matchups are kept.
  B  coupled  every entry keeps its own score, and each taxon category gets a stand-in, a latent score tied to its
              members (the broad entry and its sub-categories, nested as the trees are) by a normal coupling of SD
              tau_taxon. Each sex form is tied to its base around a common offset (one for female forms, one for male)
              with SD tau_sex, replacing the gender pseudo-matchups. tau_taxon, tau_sex and the offsets are estimated
              from the votes by empirical Bayes (Laplace-approximate marginal likelihood). A broad name's row reports
              its stand-in, so it reads as cleanly as in A, while the sub-categories keep their own scores.
Error bars, for the paper's fit and both variants:
  - the votes are overdispersed against the binomial (Pearson chi^2/df, phi, about 1.85), so the fit's covariance is
    widened by phi (quasi-likelihood); in B the likelihood is tempered by 1/phi, which does the same;
  - scores are on each fit's lion scale: the row holding the African Lion's votes reads 100 (the African Lion in the
    paper's fit and in B, where its row is the African Lion stand-in; the merged Lion in A). Uncertainty is measured
    against the field, the animals outside the category graph, so the lion row has an error bar too;
  - crowd_p*: percentiles of the crowd score, exact (log-normal);
    joint_p*: percentiles of the anatomy-corrected score with the elicited factor of step 5 (log F ~ N(mu, sigma^2),
              F for dinosaurs, sqrt(F) for Mesozoic-other) at the ladder's point estimates, exact;
    full_p*, rank_p*: the same with the ladder itself redrawn: each of N_DRAWS joint draws of all scores re-elicits
              mu and sigma from the drawn anchor, Human, Dakotaraptor and Utahraptor and draws one factor shared by
              every dinosaur; rank_p* are percentiles of each row's rank among all rows on the corrected scale.
Downstream, each variant re-elicits the anatomy factor on its own scores (anchor: the row holding the African Lion's
votes) and reruns the weight-score analysis of step 6 (in A on the merged rows, one point per tree, masses averaged; in B
on each listed animal's own coupled entry)."""
import sys, os, re, csv, json, importlib.util
from collections import Counter, defaultdict
import numpy as np, pandas as pd, networkx as nx
from scipy import optimize, stats, linalg


def _load(name, file):
    spec = importlib.util.spec_from_file_location(name, file); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


bt, c4, c5, c6 = _load('bt', '3_bt_fit.py'), _load('c4', '4_categorize.py'), _load('c5', '5_rescale_dinos.py'), _load('c6', '6_curve_fit.py')
c7 = _load('c7', '7_cultural_inflation.py')
LEVELS = (5, 16, 50, 84, 95); Z = stats.norm.ppf(np.array(LEVELS) / 100)
N_DRAWS, SEED, S0 = 5000, 2026, 1.0            # joint draws; prior SD of the two sex offsets (log scale)
OUT, FINAL = 'outputs/graph', os.path.join('..', 'final_scores.csv')    # FINAL: the end result, in the nexic folder
HEADLINE = ['Tyrannosaurus rex', 'Utahraptor ostrommaysorum', 'Dakotaraptor steini', 'Deinonychus antirrhopus', 'Velociraptor mongoliensis',
            'Mosasaurus hoffmannii', 'Lion', 'African Lion', 'Tiger', 'Bengal Tiger', 'Siberian Tiger', 'Leopard', 'Jaguar', 'Brown Bear',
            'Grizzly Bear', 'Grey Wolf', 'Human']
FELT = ['Velociraptor mongoliensis', 'Deinonychus antirrhopus', 'Dakotaraptor steini', 'Utahraptor ostrommaysorum', 'Tyrannosaurus rex']


# ---------------------------------------------------------------- category graph
def read_graph(path='category_graph.csv'):
    rows = [r for r in csv.DictReader(open(path)) if r['status'] == 'kept']
    parent = {r['child']: r['parent'] for r in rows if r['link'] == 'taxon'}
    sex = [(r['child'], r['parent'], r['link']) for r in rows if r['link'] in ('female', 'male')]
    root = {}
    for c in parent:
        x = c
        while x in parent: x = parent[x]
        root[c] = x
    return parent, sex, root


def categories(parent, present):
    """Stand-ins: categories with two or more present members. A member is ('entry', name) or ('cat', name); child
    categories come before their parents."""
    kids = defaultdict(list)
    for c, p in parent.items(): kids[p].append(c)
    cats = {}
    def build(node):
        members = [('entry', node)] if node in present else []
        for c in sorted(kids[node]):
            tok = build(c)
            if tok: members.append(tok)
        if kids[node] and len(members) >= 2: cats[node] = members; return ('cat', node)
        return members[0] if members else None
    for r in sorted(p for p in kids if p not in parent): build(r)
    return cats


# ---------------------------------------------------------------- step 3's preprocessing
def prepare(path, rename=None, gender=True, extra_edges=()):
    """Step 3's preprocessing (fit() of 3_bt_fit.py up to the likelihood), with an optional renaming of the cleaned names
    (the merge), optional extra edges counted for connectivity (the couplings) and optional gender pseudo-matchups."""
    df, raw_names = bt.load(path); within = 0
    if rename:
        df = df.assign(a=df.a.map(lambda x: rename.get(x, x)), b=df.b.map(lambda x: rename.get(x, x)))
        within = int((df.a == df.b).sum()); df = df[df.a != df.b]
    real = df[(df.p >= bt.P_LO) & (df.p <= bt.P_HI)]
    G = nx.Graph(); G.add_edges_from(zip(real.a, real.b)); present = set(G.nodes)
    G.add_edges_from((u, v) for u, v in extra_edges if (u in present or u.startswith('§')) and (v in present or v.startswith('§')))
    comps = sorted(nx.connected_components(G), key=len, reverse=True); main_c = comps[0]
    real = real[real.a.isin(main_c) & real.b.isin(main_c)]; entries = {x for x in main_c if not x.startswith('§')}
    pseudo = []
    if gender:
        for x in sorted(entries):
            m, f = x + ' (male)', x + ' (female)'
            if m in entries and f in entries: pseudo += [(m, x, bt.P_GENDER, bt.W_GENDER, 'gender'), (x, f, bt.P_GENDER, bt.W_GENDER, 'gender')]
    GROUP = re.compile(r'^(.*?)\s*\((?:[A-Za-z ]*?\bof\s+)?(\d+(?:\s*[-/]\s*\d+)?)\)\s*$')
    def solo_of(base):
        base = re.sub(r'\s*\((?:females?|males?|cows?|bulls?)\)\s*$', '', base, flags=re.I).strip()
        words = base.split(); last = words[-1] if words else ''
        sing = [re.sub(r'ves$', 'f', last), re.sub(r'ies$', 'y', last), re.sub(r'es$', '', last), re.sub(r's$', '', last)]
        for c in [base] + [' '.join(words[:-1] + [w]) for w in sing] + [re.sub(r'\s+(Pod|Pack|Herd|Troop|Pride|Clan|Group|Cows|Bulls)$', '', base)]:
            c = bt.ALIASES.get(c, c)
            if rename: c = rename.get(c, c)
            if c in entries: return c
        return None
    unmatched = 0
    for x in sorted(entries):
        g = GROUP.match(x)
        if not g: continue
        nums = [float(v) for v in re.findall(r'\d+', g.group(2))]; N = sum(nums) / len(nums)
        if N < 2: continue
        s = solo_of(g.group(1).strip())
        if s and s != x: pseudo.append((x, s, N**bt.GROUP_EXP / (N**bt.GROUP_EXP + 1), bt.W_GROUP, 'group'))
        else: unmatched += 1
    names = sorted(entries); idx = {a: i for i, a in enumerate(names)}
    rows = [(idx[a], idx[b], p * n, (1 - p) * n) for a, b, p, n in zip(real.a, real.b, real.p, real.n)] + [(idx[a], idx[b], p * w, (1 - p) * w) for a, b, p, w, _ in pseudo]
    I = np.array([r[0] for r in rows]); J = np.array([r[1] for r in rows]); Wi = np.array([r[2] for r in rows]); Wj = np.array([r[3] for r in rows])
    deg, votes = Counter(), Counter()
    for a, b, n in zip(real.a, real.b, real.n): deg[a] += 1; deg[b] += 1; votes[a] += n; votes[b] += n
    summary = dict(matchups=int(len(df)), within_category_dropped=within, animals=len(names), real_matchups=int(len(real)), real_votes=int(real.n.sum()),
                   gender_pseudo=sum(1 for p in pseudo if p[4] == 'gender'), group_pseudo=sum(1 for p in pseudo if p[4] == 'group'), group_unmatched=unmatched)
    return dict(names=names, idx=idx, I=I, J=J, Wi=Wi, Wj=Wj, real=real, deg=deg, votes=votes, summary=summary, main_c=main_c)


def solve_plain(P):
    """Step 3's penalized Bradley-Terry fit, the same arithmetic: L-BFGS, Newton polishing; returns theta, Hessian."""
    I, J, Wi, Wj = P['I'], P['J'], P['Wi'], P['Wj']; K = len(P['names']); Nt = Wi + Wj; LAMBDA = bt.LAMBDA
    def nll(th):
        d = th[I] - th[J]; f = (Wi * np.logaddexp(0, -d) + Wj * np.logaddexp(0, d)).sum() + LAMBDA * (th**2).sum()
        ge = -(Wi - Nt / (1 + np.exp(-d))); g = np.zeros(K); np.add.at(g, I, ge); np.add.at(g, J, -ge); return f, g + 2 * LAMBDA * th
    def hessian(th):
        d = th[I] - th[J]; pp = 1 / (1 + np.exp(-d)); w = Nt * pp * (1 - pp)
        H = np.zeros((K, K)); np.add.at(H, (I, I), w); np.add.at(H, (J, J), w); np.add.at(H, (I, J), -w); np.add.at(H, (J, I), -w)
        return H + 2 * LAMBDA * np.eye(K)
    th = optimize.minimize(nll, np.zeros(K), jac=True, method='L-BFGS-B', options={'maxiter': 20000, 'gtol': 1e-9}).x
    for _ in range(30):
        step = np.linalg.solve(hessian(th), nll(th)[1]); th = th - step
        if np.abs(step).max() < 1e-12: break
    return th, hessian(th)


# ---------------------------------------------------------------- the coupled model
class Coupled:
    """Negative log posterior of variant B: step 3's penalized likelihood (BT plus ridge), tempered by 1/phi, on the
    entries (the ridge also on the stand-ins), taxon couplings (member - stand-in)^2 / (2 tau_t^2), sex couplings (form - base - offset)^2 / (2 tau_s^2),
    and N(0, S0^2) priors on the two offsets. x = [entries (K), stand-ins (C), offset_female, offset_male]. With broad_pairs
    (broad entry, its stand-in), those couplings get a shared offset of their own, offset_broad, appended to x: the check of
    whether broad names sit systematically above their categories."""
    def __init__(self, P, tax_pairs, sex_pairs, C, temper, broad_pairs=None):
        self.n_off = 2 if broad_pairs is None else 3
        self.P, self.K, self.C, self.n = P, len(P['names']), C, len(P['names']) + C + self.n_off
        self.tm, self.ts = tax_pairs[:, 0], tax_pairs[:, 1]; self.sf, self.sb, self.so = sex_pairs.T; self.temper = temper
        self.bb, self.bs = (None, None) if broad_pairs is None else (broad_pairs[:, 0], broad_pairs[:, 1])
        self.Nt = P['Wi'] + P['Wj']

    def prior(self, tau_t, tau_s):
        n, KC, wt, ws = self.n, self.K + self.C, tau_t**-2, tau_s**-2; Q = np.zeros((n, n))
        Q[np.arange(KC), np.arange(KC)] += 2 * bt.LAMBDA * self.temper      # step 3's ridge, tempered with the votes
        for a, b, s in [(self.tm, self.tm, 1), (self.ts, self.ts, 1), (self.tm, self.ts, -1), (self.ts, self.tm, -1)]: np.add.at(Q, (a, b), s * wt)
        f, b_, o = self.sf, self.sb, self.so
        for a, b, s in [(f, f, 1), (b_, b_, 1), (o, o, 1), (f, b_, -1), (b_, f, -1), (f, o, -1), (o, f, -1), (b_, o, 1), (o, b_, 1)]: np.add.at(Q, (a, b), s * ws)
        if self.bb is not None:                                              # (broad - stand-in - offset_broad)^2 / (2 tau_t^2)
            b_, s_, o = self.bb, self.bs, np.full(len(self.bb), KC + 2)
            for a, b, s in [(b_, b_, 1), (s_, s_, 1), (o, o, 1), (b_, s_, -1), (s_, b_, -1), (b_, o, -1), (o, b_, -1), (s_, o, 1), (o, s_, 1)]: np.add.at(Q, (a, b), s * wt)
        Q[KC:, KC:] += np.eye(self.n_off) / S0**2
        return Q

    def bt_terms(self, x):
        P, K = self.P, self.K; d = x[P['I']] - x[P['J']]
        val = self.temper * (P['Wi'] * np.logaddexp(0, -d) + P['Wj'] * np.logaddexp(0, d)).sum()
        ge = -self.temper * (P['Wi'] - self.Nt / (1 + np.exp(-d))); g = np.zeros(self.n); np.add.at(g, P['I'], ge); np.add.at(g, P['J'], -ge)
        pp = 1 / (1 + np.exp(-d)); w = self.temper * self.Nt * pp * (1 - pp)
        return val, g, w

    def mode(self, tau_t, tau_s, x0):
        Q = self.prior(tau_t, tau_s); P = self.P; x = x0.copy()
        def f(x): return self.bt_terms(x)[0] + 0.5 * x @ Q @ x
        for _ in range(100):
            val, g, w = self.bt_terms(x); g = g + Q @ x
            H = Q.copy(); np.add.at(H, (P['I'], P['I']), w); np.add.at(H, (P['J'], P['J']), w); np.add.at(H, (P['I'], P['J']), -w); np.add.at(H, (P['J'], P['I']), -w)
            step = linalg.cho_solve(linalg.cho_factor(H), g); t, f0 = 1.0, val + 0.5 * x @ Q @ x
            while f(x - t * step) > f0 - 1e-4 * t * (g @ step) and t > 1e-8: t /= 2
            x = x - t * step
            if np.abs(t * step).max() < 1e-10: break
        val, g, w = self.bt_terms(x); H = Q.copy()
        np.add.at(H, (P['I'], P['I']), w); np.add.at(H, (P['J'], P['J']), w); np.add.at(H, (P['I'], P['J']), -w); np.add.at(H, (P['J'], P['I']), -w)
        logml = -(val + 0.5 * x @ Q @ x) + np.log(np.diag(linalg.cholesky(Q))).sum() - np.log(np.diag(linalg.cholesky(H))).sum()
        return x, H, logml


# ---------------------------------------------------------------- the three fits
def fit_original(path, phi):
    names, idx, th, Sig, deg, votes, summary = bt.fit(path)
    return dict(label='original', rows=names, theta=th, cov=phi * Sig, kind=['entry'] * len(names), members={n: [n] for n in names},
                matchups=[deg[n] for n in names], votes=[votes[n] for n in names], entry_theta=th.copy(), summary=summary, anchor='African Lion', alt_anchor='Lion')


def fit_merge(path, root, phi):
    P = prepare(path, rename=root); th, H = solve_plain(P); names = P['names']
    members = defaultdict(list)
    for c, r in root.items(): members[r].append(c)
    return dict(label='merge', rows=names, theta=th, cov=phi * np.linalg.inv(H), kind=['merged' if n in members else 'entry' for n in names],
                members={n: sorted([n] + members[n]) for n in names}, matchups=[P['deg'][n] for n in names], votes=[P['votes'][n] for n in names],
                entry_theta=np.full(len(names), np.nan), summary=P['summary'], anchor=root.get('African Lion', 'African Lion'), alt_anchor=None)


def fit_coupled(path, parent, sex, phi, start):
    df, _ = bt.load(path); real = df[(df.p >= bt.P_LO) & (df.p <= bt.P_HI)]; present = set(real.a) | set(real.b)
    cats = categories(parent, present)
    edges = [('§' + c, (m if k == 'entry' else '§' + m)) for c, mem in cats.items() for k, m in mem] + [(f, b) for f, b, _ in sex]
    P = prepare(path, gender=False, extra_edges=edges); idx, K = P['idx'], len(P['names'])
    cats = {c: m for c, m in cats.items() if '§' + c in P['main_c']}; cidx = {c: K + i for i, c in enumerate(cats)}; C = len(cats)
    tok = lambda k, m: idx[m] if k == 'entry' else cidx[m]
    tax_pairs = np.array([(tok(k, m), cidx[c]) for c, mem in cats.items() for k, m in mem])
    sex_in = [(f, b, kind) for f, b, kind in sex if f in idx and b in idx]
    sex_pairs = np.array([(idx[f], idx[b], K + C + (0 if kind == 'female' else 1)) for f, b, kind in sex_in])
    model = Coupled(P, tax_pairs, sex_pairs, C, 1 / phi)
    x0 = np.zeros(model.n); x0[:K] = [start.get(n, 0.0) for n in P['names']]
    for c, mem in cats.items(): x0[cidx[c]] = np.mean([x0[tok(k, m)] for k, m in mem])
    cache = {'x': x0, 'evals': []}
    def neg_logml(v):
        lt, ls = np.clip(v, np.log(0.02), np.log(5.0)); x, H, lm = model.mode(np.exp(lt), np.exp(ls), cache['x'])
        cache['x'] = x; cache['evals'].append((float(np.exp(lt)), float(np.exp(ls)), float(lm))); return -lm
    res = optimize.minimize(neg_logml, np.log([0.5, 0.5]), method='Nelder-Mead', options=dict(xatol=0.01, fatol=0.005, maxiter=80))
    tau_t, tau_s = np.exp(np.clip(res.x, np.log(0.02), np.log(5.0))); x, H, logml = model.mode(tau_t, tau_s, cache['x']); cov = np.linalg.inv(H)
    # checks: the marginal likelihood near a full merge and near no pooling, and a shared offset for broad names
    checks = {f'log_marginal_likelihood_tau_taxon_{t}': float(model.mode(t, tau_s, x)[2]) for t in (0.05, 2.0)}
    broad = np.array([(idx[c], cidx[c]) for c, mem in cats.items() if ('entry', c) in mem])
    rest = np.array([(tok(k, m), cidx[c]) for c, mem in cats.items() for k, m in mem if not (k == 'entry' and m == c)])
    mb = Coupled(P, rest, sex_pairs, C, 1 / phi, broad_pairs=broad); xb, Hb, lmb = mb.mode(tau_t, tau_s, np.append(x, 0.0))
    checks.update(broad_offset=float(xb[-1]), broad_offset_se=float(np.sqrt(np.linalg.inv(Hb)[-1, -1])), broad_offset_categories=len(broad),
                  broad_offset_log_marginal_likelihood_change=float(lmb - logml))
    # rows: leaf entries keep their own score; a broad name's row is its stand-in
    rows, pos, kind, ent = [], [], [], []
    for n in P['names']:
        if n in cats: continue
        rows.append(n); pos.append(idx[n]); kind.append('entry'); ent.append(x[idx[n]])
    for c in cats:
        rows.append(c); pos.append(cidx[c]); kind.append('category'); ent.append(x[idx[c]] if c in idx else np.nan)
    def subtree(c):
        out = []
        for k, m in cats[c]: out += [m] if k == 'entry' else subtree(m)
        return out
    members = {r: (sorted(subtree(r)) if k == 'category' else [r]) for r, k in zip(rows, kind)}
    pos = np.array(pos)
    matchups = [sum(P['deg'][m] for m in members[r]) for r in rows]; votes = [sum(P['votes'][m] for m in members[r]) for r in rows]
    summary = dict(P['summary'], stand_ins=C, taxon_couplings=len(tax_pairs), sex_couplings=len(sex_in), tau_taxon=float(tau_t), tau_sex=float(tau_s),
                   offset_female=float(x[K + C]), offset_male=float(x[K + C + 1]), offset_female_se=float(np.sqrt(cov[K + C, K + C])),
                   offset_male_se=float(np.sqrt(cov[K + C + 1, K + C + 1])), log_marginal_likelihood=float(logml), eb_evaluations=len(cache['evals']), checks=checks)
    return dict(label='coupled', rows=rows, theta=x[pos], cov=cov[np.ix_(pos, pos)], kind=kind, members=members, matchups=matchups, votes=votes,
                entry_theta=np.array(ent), summary=summary, anchor='African Lion', alt_anchor='Lion', eb_path=cache['evals'])


# ---------------------------------------------------------------- scale, error bars, simulation
def dispersion(path):
    names, idx, th, Sig, deg, votes, summary = bt.fit(path)
    df, _ = bt.load(path); real = df[(df.p >= bt.P_LO) & (df.p <= bt.P_HI)]; real = real[real.a.isin(idx) & real.b.isin(idx)]
    d = th[[idx[a] for a in real.a]] - th[[idx[b] for b in real.b]]; pi = 1 / (1 + np.exp(-d))
    chi2 = float(((real.p.values - pi)**2 * real.n.values / (pi * (1 - pi))).sum()); dfree = len(real) - len(names) + 1
    return chi2 / dfree, dict(pearson_chi2=chi2, df=dfree, phi=chi2 / dfree, start=dict(zip(names, th)))


def elicit_vec(A, H, D, U):
    """Step 5's elicitation, vectorized over draws (log scale in, mu and sigma out). Where a draw puts L above U, the
    15% rule is applied to the interval between them."""
    Dt = 2 * A - H; lL = (Dt - D) / 2; lU = Dt - U; mu = (2 / 3) * lL + (1 / 3) * lU; lo, hi = np.minimum(lL, lU), np.maximum(lL, lU)
    s_lo, s_hi = np.full_like(mu, 1e-4), np.full_like(mu, 5.0)
    for _ in range(60):
        s = (s_lo + s_hi) / 2; out = stats.norm.cdf((lo - mu) / s) + 1 - stats.norm.cdf((hi - mu) / s)
        s_hi = np.where(out > 0.15, s, s_hi); s_lo = np.where(out > 0.15, s_lo, s)      # out grows with s
    return mu, (s_lo + s_hi) / 2


def error_bars(F, bulk, offset, cls, rng):
    """Crowd, joint and full percentiles and rank percentiles for every row of fit F (theta already aligned)."""
    rows = F['rows']; R = {r: i for i, r in enumerate(rows)}; th = F['theta'] + offset; S = F['cov']
    U = np.array([R[u] for u in bulk]); m = S[:, U].mean(axis=1); se = np.sqrt(np.maximum(np.diag(S) - 2 * m + m[U].mean(), 0))
    lad = [R[F['anchor']], R['Human'], R['Dakotaraptor steini'], R['Utahraptor ostrommaysorum']]
    mu, sig = (float(v[0]) for v in elicit_vec(*[th[[i]] for i in lad]))
    k = np.array([1.0 if c == 'dinosaur' else 0.5 if c == 'mesozoic-other' else 0.0 for c in cls])
    crowd = np.exp(th[:, None] + Z[None, :] * se[:, None]) * 100
    joint = np.exp(th[:, None] + k[:, None] * mu + Z[None, :] * np.sqrt(se**2 + (k * sig)**2)[:, None]) * 100
    L = linalg.cholesky(S + 1e-12 * np.eye(len(rows)), lower=True); draws = np.empty((N_DRAWS, len(rows)))
    for b0 in range(0, N_DRAWS, 1000):
        e = (L @ rng.standard_normal((len(rows), min(1000, N_DRAWS - b0)))).T; draws[b0:b0 + len(e)] = th + e - e[:, U].mean(axis=1, keepdims=True)
    mu_d, sig_d = elicit_vec(*[draws[:, i] for i in lad]); logF = mu_d + sig_d * rng.standard_normal(N_DRAWS)
    corr = draws + logF[:, None] * k[None, :]
    full = np.exp(np.percentile(corr, LEVELS, axis=0).T) * 100
    ranks = (-corr).argsort(axis=1).argsort(axis=1) + 1
    rank_p = np.percentile(ranks, [5, 50, 95], axis=0).T
    ladder = dict(mu=mu, sigma=sig, median=float(np.exp(mu)), draws_mu_sd=float(mu_d.std()), draws_sigma_mean=float(sig_d.mean()),
                  draws_logF_sd=float(logF.std()), draws_F_percentiles=[float(v) for v in np.exp(np.percentile(logF, LEVELS))])
    return dict(theta=th, se=se, crowd=crowd, joint=joint, full=full, rank=rank_p, ladder=ladder, k=k)


# ---------------------------------------------------------------- downstream: classes, anatomy model, weight-score
def classify_rows(rows):
    out = [c4.classify(r) for r in rows]; return [o[0] for o in out], [o[1] for o in out]


def weight_analysis(S, F, sig, mammals, generic):
    """Step 6's analysis (main() of 6_curve_fit.py: the same arithmetic and output keys) on the scores S, with a given
    mammal list and the generic names left out of its main mammal fit."""
    lad, pr = c6.lad, c6.pr
    th_all = [(w, S[n]) for n, (w, c) in c6.THEROPODS.items()]; th_carn = [(w, S[n]) for n, (w, c) in c6.THEROPODS.items() if c]
    mam = [(w, S[n]) for n, w in mammals.items() if n not in generic]; mam_gen = [(w, S[n]) for n, w in mammals.items()]
    fT, fC, fM, fMg = lad(th_all), lad(th_carn), lad(mam), lad(mam_gen)
    out = dict(fits=dict(theropods=fT, theropods_carnivorous=fC, mammals=fM, mammals_with_generic_lion_tiger=fMg,
                         theropods_median_calibrated=(fT[0] * F, fT[1]), theropods_median_band=(fT[0] * F * np.exp(-sig), fT[0] * F * np.exp(sig))))
    rows = []
    for w, ctx in [(.02, 'Mouse-sized'), (.1, 'Rat-sized illustrative mammal'), (2, 'Squirrel-sized'), (15, 'Fox-sized (Velociraptor)'),
                   (75, 'Human-sized (Deinonychus)'), (250, 'Lion-sized (Dakotaraptor)'), (500, 'Bear-sized (Utahraptor)')]:
        t = pr(fT, w) * F; rows.append(dict(weight_kg=w, theropod_median=t, theropod_band_low=t * np.exp(-sig), theropod_band_high=t * np.exp(sig),
                                            mammal=pr(fM, w), ratio=t / pr(fM, w), context=ctx))
    out['dark_era_table'] = rows
    out['median_ratio_1kg'] = pr(fT, 1) * F / pr(fM, 1); out['mammal_score_100g'] = pr(fM, .1)
    out['cross_mass_ratios_vs_100g_mammal'] = {f'{w} kg': pr(fT, w) * F / pr(fM, .1) for w in (.4, 3, 15)}
    rng = np.random.default_rng(7); eq = {}
    for name, tp in [('carnivorous', th_carn), ('all', th_all)]:
        eq[name] = {'without_generic': {f'{w} kg': pr(lad(tp), w) / pr(fM, w) for w in (1, 30, 300)},
                    'with_generic': {f'{w} kg': pr(lad(tp), w) / pr(fMg, w) for w in (1, 30, 300)}}
        boot = {30: [], 300: []}
        for _ in range(1000):
            a = lad([tp[i] for i in rng.integers(0, len(tp), len(tp))]); m = lad([mam[i] for i in rng.integers(0, len(mam), len(mam))])
            for w in boot: boot[w].append(pr(a, w) / pr(m, w))
        eq[name]['bootstrap_90'] = {f'{w} kg': [float(np.percentile(v, 5)), float(np.percentile(v, 95))] for w, v in boot.items()}
    out['equal_mass_crowd_ratio'] = eq; out['mammal_points'] = len(mam)
    return out


def icon_inflation(path):
    """Step 7's skew-normal fit to the iconic generic names' log-gaps over their populations, on the unpooled fit (the
    arithmetic of main() in 7_cultural_inflation.py); returns the one-sided inflation scale s_I."""
    names, idx, th, Sig, deg, votes, _ = bt.fit(path)
    T = pd.DataFrame([dict(eta=float(th[idx[g]] - np.mean([th[idx[p]] for p in pops])), icon=g in c7.ICONS) for g, pops in c7.VET.items()])
    a, xi, om = stats.skewnorm.fit(T.sort_values('eta', ascending=False)[lambda d: d.icon].eta.values)
    return float(om * a / np.sqrt(1 + a * a))


def felt_strength(mu, sig, s, crowd):
    """Step 7's felt strength, log felt factor ~ SN(mu, sqrt(sigma^2 + s^2), s / sigma), on a given anatomy model; with the felt
    median and 90% band of the given animals' scores (anatomy-factor and inflation uncertainty, as in the paper's table)."""
    om, al = np.sqrt(sig**2 + s**2), s / sig; SN = stats.skewnorm(al, loc=mu, scale=om)
    mc = np.random.default_rng(1); draws = mc.normal(mu, sig, 2_000_000) + np.abs(mc.normal(0, s, 2_000_000))
    f = lambda q: float(np.exp(SN.ppf(q)))
    return dict(xi=float(mu), omega=float(om), alpha=float(al), delta=float(s / om), median=f(.5), geometric_mean=float(np.exp(SN.mean())),
                quantiles_5_16_50_84_95=[f(q) for q in (.05, .1587, .5, .8413, .95)],
                monte_carlo_check=[float(np.exp(np.percentile(draws, q))) for q in (5, 15.87, 50, 84.13, 95)],
                animals={n: dict(crowd=c, actual=c * float(np.exp(mu)), felt=c * f(.5), felt_p05=c * f(.05), felt_p95=c * f(.95)) for n, c in crowd.items()})


def merged_mammals(root):
    groups = defaultdict(list)
    for n, w in c6.MAMMALS.items(): groups[root.get(n, n)].append(w)
    return {r: float(np.exp(np.mean(np.log(ws)))) for r, ws in groups.items()}


# ---------------------------------------------------------------- main
def main(path):
    os.makedirs(OUT, exist_ok=True); parent, sex, root = read_graph(); rng = np.random.default_rng(SEED)
    phi, disp = dispersion(path); print(f"dispersion: Pearson chi2 {disp['pearson_chi2']:.0f} on {disp['df']} df -> phi {phi:.3f}")
    fits = [fit_original(path, phi), fit_merge(path, root, phi), fit_coupled(path, parent, sex, phi, disp['start'])]
    o, a, b = fits; s = b['summary']
    print(f"merge: {a['summary']['animals']} rows, {a['summary']['within_category_dropped']} duels inside a tree dropped")
    print(f"coupled: {s['stand_ins']} stand-ins, {s['taxon_couplings']} taxon and {s['sex_couplings']} sex couplings; tau_taxon {s['tau_taxon']:.3f}, tau_sex "
          f"{s['tau_sex']:.3f}; female offset {s['offset_female']:+.3f} ± {s['offset_female_se']:.3f}, male {s['offset_male']:+.3f} ± {s['offset_male_se']:.3f}")
    linked = set(parent) | set(parent.values()) | {f for f, _, _ in sex} | {x for _, x, _ in sex}
    bulk = sorted(set.intersection(*[{r for r, k in zip(F['rows'], F['kind']) if k == 'entry'} for F in fits]) - linked)
    ref = dict(zip(o['rows'], o['theta'])); s_icon = icon_inflation(path)
    summary = dict(dispersion={k: v for k, v in disp.items() if k != 'start'}, bulk_animals=len(bulk), icon_one_sided_scale=s_icon, variants={})
    tables = {}
    for F in fits:
        R = dict(zip(F['rows'], F['theta'])); offset = -float(R[F['anchor']])
        x_ = np.array([ref[u] for u in bulk]); y_ = np.array([R[u] + offset for u in bulk]); slope = float(np.polyfit(x_, y_, 1)[0])
        cls, perm = classify_rows(F['rows']); E = error_bars(F, bulk, offset, cls, rng)
        S = dict(zip(F['rows'], 100 * np.exp(E['theta'])))
        model = c5.elicit(S[F['anchor']], S['Human'], S['Dakotaraptor steini'], S['Utahraptor ostrommaysorum'])
        alt = c5.elicit(S[F['alt_anchor']], S['Human'], S['Dakotaraptor steini'], S['Utahraptor ostrommaysorum']) if F['alt_anchor'] else None
        mu, sig = model['mu'], model['sigma']; fac = np.exp(E['k'] * mu)
        mam, gen = (merged_mammals(root), set()) if F is a else (c6.MAMMALS, c6.GENERIC)
        # step 6's masses describe particular animals, so B regresses on each listed animal's own coupled entry, not on the
        # stand-ins, which average over sub-categories of different sizes
        Sw = S if F is not b else {r: float(100 * np.exp((e if k == 'category' and np.isfinite(e) else t) + offset))
                                   for r, k, t, e in zip(F['rows'], F['kind'], F['theta'], F['entry_theta'])}
        W = weight_analysis(Sw, model['median'], sig, mam, gen)
        t = pd.DataFrame(dict(animal=F['rows'], kind=F['kind'], **{'class': cls}, permian=perm, score=100 * np.exp(E['theta']), log_score=E['theta'], se_log=E['se'],
                              **{f'crowd_p{q:02d}': E['crowd'][:, i] for i, q in enumerate(LEVELS)}, median_factor=fac, median_score=100 * np.exp(E['theta']) * fac,
                              **{f'joint_p{q:02d}': E['joint'][:, i] for i, q in enumerate(LEVELS)}, **{f'full_p{q:02d}': E['full'][:, i] for i, q in enumerate(LEVELS)},
                              rank_p05=E['rank'][:, 0], rank_p50=E['rank'][:, 1], rank_p95=E['rank'][:, 2], real_matchups=F['matchups'], real_votes=F['votes'],
                              entry_score=100 * np.exp(F['entry_theta'] + offset), members=['; '.join(F['members'][r]) if len(F['members'][r]) > 1 else '' for r in F['rows']]))
        t = t.sort_values('median_score', ascending=False); t.insert(0, 'rank', range(1, len(t) + 1)); tables[F['label']] = t
        t.to_csv(FINAL if F is b else f"{OUT}/scores_{F['label']}.csv", index=False, float_format='%.6g')
        v = dict(fit=F['summary'], anchor=F['anchor'], scale_slope_vs_paper=slope, anatomy_model=model, anatomy_model_alt_anchor=alt, alt_anchor=F['alt_anchor'],
                 ladder_redrawn=E['ladder'], weight_score=W, felt_strength=felt_strength(mu, sig, s_icon, {n: S[n] for n in FELT}))
        v['headline'] = {r['animal']: {k: (float(r[k]) if not isinstance(r[k], str) else r[k]) for k in ['score', 'crowd_p05', 'crowd_p95', 'median_score', 'joint_p05', 'joint_p95',
                         'full_p05', 'full_p50', 'full_p95', 'rank', 'rank_p05', 'rank_p50', 'rank_p95', 'kind']} for _, r in t.iterrows() if r['animal'] in HEADLINE}
        if F is b: v['eb_path'] = F['eb_path']
        summary['variants'][F['label']] = v
        c = W['equal_mass_crowd_ratio']['carnivorous']
        print(f"{F['label']:9s} slope vs paper {slope:.3f}; anchor {F['anchor']}: F median {model['median']:.3f} (sigma {sig:.3f}); ladder redrawn: logF sd {E['ladder']['draws_logF_sd']:.3f}; "
              f"carnivorous equal-mass 30 kg {c['without_generic']['30 kg']:.2f}, 300 kg {c['without_generic']['300 kg']:.2f}; felt median {v['felt_strength']['median']:.2f}")
    # the categories side by side: the paper's broad entry and populations, the merge, the stand-in
    O, A, B = (tables[k].set_index('animal') for k in ('original', 'merge', 'coupled')); rows = []
    for c in B.index[B.kind == 'category']:
        mem = B.loc[c, 'members'].split('; '); others = [m for m in mem if m != c and m in O.index]
        rows.append(dict(category=c, members=len(mem), paper_broad=O.score.get(c, np.nan), paper_members_geomean=float(np.exp(np.mean(np.log(O.score[others])))) if others else np.nan,
                         merge=A.score.get(root.get(c, c), np.nan) if c not in parent else np.nan, coupled_standin=B.loc[c, 'score'], coupled_p05=B.loc[c, 'crowd_p05'],
                         coupled_p95=B.loc[c, 'crowd_p95'], coupled_broad_entry=B.loc[c, 'entry_score'], paper_broad_se=O.se_log.get(c, np.nan), coupled_se=B.loc[c, 'se_log'],
                         real_matchups=B.loc[c, 'real_matchups']))
    pd.DataFrame(rows).sort_values('coupled_standin', ascending=False).to_csv(f'{OUT}/categories.csv', index=False, float_format='%.6g')
    sens = {}
    for lam in (0.01, 0.001, 1e-6):
        save = bt.LAMBDA; bt.LAMBDA = lam; P = prepare(path); th, _ = solve_plain(P); bt.LAMBDA = save
        Sx = dict(zip(P['names'], 100 * np.exp(th - th[P['idx']['African Lion']])))
        m = c5.elicit(100.0, Sx['Human'], Sx['Dakotaraptor steini'], Sx['Utahraptor ostrommaysorum'])
        sens[str(lam)] = dict(anatomy_median=m['median'], **{n: Sx[n] for n in ['Tyrannosaurus rex', 'African Bush Elephant', 'Utahraptor ostrommaysorum', 'Dakotaraptor steini', 'Human', 'Red Fox']})
    summary['ridge_sensitivity_paper_fit'] = sens
    print('ridge sensitivity (paper fit): ' + '; '.join(f"lambda {k}: T. rex {v['Tyrannosaurus rex']:.0f}, Human {v['Human']:.2f}, F {v['anatomy_median']:.2f}" for k, v in sens.items()))
    json.dump(summary, open(f'{OUT}/summary.json', 'w'), indent=1, default=float)
    print(f'wrote {os.path.abspath(FINAL)} (the end result) and {OUT}/scores_original.csv, scores_merge.csv, categories.csv, summary.json')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'duels.csv')
