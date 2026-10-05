#!/usr/bin/env python3
"""Optional check that step 3 fits a Bradley-Terry model, and fits it exactly.

Usage:  python3 verify_bradley_terry.py [duels.csv]          (needs scikit-learn)

  1. step 3's objective equals the Bradley-Terry log-likelihood, P(i beats j) = pi_i / (pi_i + pi_j), plus the penalty;
  2. the fitted strengths satisfy the Bradley-Terry score equations (observed wins = expected wins + penalty term);
  3. an independent solver (scikit-learn's penalized logistic regression on the Bradley-Terry design) gives the same fit;
  4. if the old 3_power_assembler.py is present beside this file, its ratings are compared with the refit's."""
import sys, os, io, contextlib, importlib.util, numpy as np, pandas as pd, scipy.sparse as sp
from scipy import optimize
DUELS = sys.argv[1] if len(sys.argv) > 1 else 'duels.csv'
spec = importlib.util.spec_from_file_location('bt3', '3_bt_fit.py'); bt = importlib.util.module_from_spec(spec); spec.loader.exec_module(bt)
captured = {}; real_minimize = optimize.minimize
def spy(fun, x0, **kw):                       # capture the exact objective step 3 optimizes
    captured['fun'] = fun; res = real_minimize(fun, x0, **kw); captured['x'] = res.x; return res
bt.optimize.minimize = spy
names, idx, th_rel, Sig, deg, votes, summ = bt.fit(DUELS)
fun = captured['fun']; cl = dict(zip(fun.__code__.co_freevars, [c.cell_contents for c in fun.__closure__]))
I, J, Wi, Wj, K, LAM = cl['I'], cl['J'], cl['Wi'], cl['Wj'], cl['K'], bt.LAMBDA
th = np.array([th_rel[idx[n]] for n in names]); th = th - th.mean()   # step 3's final (polished) answer; the penalty makes the optimum's mean log-strength exactly zero
print(f"captured step 3's objective: {K} animals, {len(I)} weighted comparisons (real matchups + pseudo-matchups), penalty λ = {LAM}")
# 1. the objective is the Bradley-Terry log-likelihood: P(i beats j) = pi_i / (pi_i + pi_j)
pi = np.exp(th); bt_ll = (Wi*np.log(pi[I]/(pi[I]+pi[J])) + Wj*np.log(pi[J]/(pi[I]+pi[J]))).sum()
f_code = fun(th)[0]; print(f"1. step 3 objective at the fit = {f_code:.6f}; -(BT log-likelihood) + λΣθ² written directly in π form = {-bt_ll + LAM*(th**2).sum():.6f}")
# 2. Bradley-Terry score equations: observed wins - expected wins = 2λθ for every animal
P = pi[I]/(pi[I]+pi[J]); obs = np.zeros(K); exp_ = np.zeros(K)
np.add.at(obs, I, Wi); np.add.at(obs, J, Wj); np.add.at(exp_, I, (Wi+Wj)*P); np.add.at(exp_, J, (Wi+Wj)*(1-P))
r = obs - exp_ - 2*LAM*th; print(f"2. score equations: max |observed wins - expected wins - 2λθ| over {K} animals = {np.abs(r).max():.2e} (total votes {(Wi+Wj).sum():,.0f})")
# 3. independent solver: the same problem as penalized logistic regression in scikit-learn
from sklearn.linear_model import LogisticRegression
m = len(I); rows = np.r_[np.arange(m), np.arange(m)]; X1 = sp.csr_matrix((np.r_[np.ones(m), -np.ones(m)], (rows, np.r_[I, J])), shape=(m, K))
X = sp.vstack([X1, X1]).tocsr(); y = np.r_[np.ones(m), np.zeros(m)]; w = np.r_[Wi, Wj]; keep = w > 0
lr = LogisticRegression(C=1/(2*LAM), fit_intercept=False, solver='newton-cholesky', tol=1e-14, max_iter=200).fit(X[keep], y[keep], sample_weight=w[keep])
d = np.abs(lr.coef_[0] - th); print(f"3. scikit-learn logistic regression on the BT design (x = e_i - e_j, no intercept, C = 1/(2λ), exact Newton solver): max |Δθ| = {d.max():.2e}, median {np.median(d):.1e}")
# 4. the original 3_power_assembler.py on the same duels file
if os.path.exists('3_power_assembler.py'):
    spec2 = importlib.util.spec_from_file_location('pa', '3_power_assembler.py'); pa = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(pa)
    with contextlib.redirect_stdout(io.StringIO()): rk = pa.fit_bradley_terry(DUELS)
    orig = {n: np.log(p) for n, p in rk}; com = [n for n in names if n in orig and n != 'African Lion']
    a = np.array([th_rel[idx[n]] for n in com]); b = np.array([orig[n] - orig['African Lion'] for n in com])
    print(f"4. original 3_power_assembler.py: {len(orig)} animals; on the {len(com)} shared with the refit, correlation of log-strengths {np.corrcoef(a, b)[0,1]:.4f}, median |difference| {np.median(np.abs(a-b)):.3f} (preprocessing differs: no main-component restriction, no pseudo-matchups, no alias merging)")
else:
    print('4. (skipped: 3_power_assembler.py not present)')
# calibration on the real matchups
real = slice(0, summ['real_matchups']); pr = P[real]; po = Wi[real]/(Wi[real]+Wj[real]); n = (Wi+Wj)[real]
print(f"   fit quality on the {summ['real_matchups']} real matchups: vote-weighted mean |observed - predicted win probability| = {np.average(np.abs(po-pr), weights=n):.3f}")
