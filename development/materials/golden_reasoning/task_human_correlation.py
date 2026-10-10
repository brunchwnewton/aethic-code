# task_human_correlation.py — minimum score correlation implied by a realized single task-human
# (long Golden Reasoning paper, task-objects: "Minimum score correlation from the realized coincidence").
# Scores (S_A, S_M) bivariate normal with correlation r; a person qualifies for task-object A (M) iff S_A > z_A (S_M > z_M),
# thresholds set by per-person tail probabilities p_A, p_M. Among N people the counts of (both, A-only, M-only) qualifiers are
# independent Poisson (the binomial limit). Each task-object is realized by one of its qualifiers, uniformly (first-to-derive
# with exchangeable clearing times). The realized Aethus is "same": both task-objects realized by one person. The Accordance
# Principle at level kappa, on the binary partition {same, different} with "same" realized, requires
#     P(same | both realized) >= 1/(1 + kappa),
# which in the small-count regime is rho/N >= 1/kappa with rho = p_AM/(p_A p_M), and in general is computed exactly below.
import numpy as np
from scipy.stats import norm, poisson
from scipy.integrate import quad

def p_joint(r, zA, zM):
    if r >= 1.0: return norm.sf(max(zA, zM))
    s = np.sqrt(1 - r * r)
    val, _ = quad(lambda x: norm.pdf(x) * norm.sf((zM - r * x) / s), zA, zA + 12, limit=200)
    return val

def p_same(N, pA, pM, pAM):
    """Exact P(same | both realized) under the Poisson model with uniform choice of realizer among qualifiers."""
    pAM = min(pAM, pA, pM)
    mb, ma, mm = N * pAM, max(N * (pA - pAM), 0.0), max(N * (pM - pAM), 0.0)
    K = lambda m: np.arange(0, int(m + 10 * np.sqrt(m) + 12))
    kb, ka, km = K(mb), K(ma), K(mm)
    Pb, Pa, Pm = poisson.pmf(kb, mb), poisson.pmf(ka, ma), poisson.pmf(km, mm)
    # P(same, both realized) = sum over counts with kb >= 1 of kb / ((ka+kb)(km+kb))
    KB, KA, KM = np.meshgrid(kb, ka, km, indexing='ij')
    W = Pb[:, None, None] * Pa[None, :, None] * Pm[None, None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        same = np.where(KB >= 1, KB / ((KA + KB) * (KM + KB)), 0.0)
    both = ((KA + KB) >= 1) & ((KM + KB) >= 1)
    return float((W * same).sum() / (W * both).sum())

def r_min(N, kappa, pA, pM):
    zA, zM = norm.isf(pA), norm.isf(pM)
    share = lambda r: p_same(N, pA, pM, p_joint(r, zA, zM))
    if share(1.0) < 1 / (1 + kappa): return None      # infeasible even at perfect correlation
    lo, hi = 0.0, 1.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if share(mid) >= 1 / (1 + kappa): hi = mid
        else: lo = mid
    return hi

def chain_length(N, alpha, q):
    """Steps of common pass probability q needed for N q^L = alpha (Proposition "Chains, the shared sub-chain, and the rarity figure")."""
    return np.log(N / alpha) / np.log(1 / q)

if __name__ == "__main__":
    print("Chain lengths reproducing alpha = 1/2 at N = 8e9:", {q: round(float(chain_length(8e9, 0.5, q)), 1) for q in (0.5, 0.2, 0.1)})
    print("Shared sub-chain bound (homogeneous, small-count): rho = 1/p_S >= N/kappa  <=>  p_S <= kappa/N =", {k: f"{k/8e9:.1e}" for k in (4, 9, 19)})
    N = 8e9
    print(f"N = {N:.0e}; realizer uniform among qualifiers; accordance: P(same | both) >= 1/(1+kappa).")
    print(f"{'kappa':>6} {'p_A = p_M':>10} {'alpha = N p':>11} {'feasible':>9} {'r_min':>8} {'P(M | A) at r_min':>18} {'share at r=1':>13}")
    for kappa in (1, 4, 9, 19, 99):
        for p in (1e-10, 3e-10, 1e-9, 3e-9, 1e-8):
            rm = r_min(N, kappa, p, p); z = norm.isf(p)
            s1 = p_same(N, p, p, p)
            cond = p_joint(rm, z, z) / p if rm is not None else float('nan')
            print(f"{kappa:6d} {p:10.0e} {N*p:11.2f} {str(rm is not None):>9} {rm if rm is not None else float('nan'):8.4f} {cond:18.3f} {s1:13.3f}")
    print("Small-count check: p = 1e-10, kappa = 9 -> rho/N criterion gives", end=" ")
    z = norm.isf(1e-10); print(f"r_min ~ {r_min(N, 9, 1e-10, 1e-10):.4f} (compare 0.8720 from the small-count formula)")

# ---------------------------------------------------------------------------------------------------------------
# Three achievement types (a, b, c). A person has latent type-scores theta = (theta_a, theta_b, theta_c), standard normal
# with correlation matrix R; a step of type t is passed with probability Phi(s (theta_t - d)): probit link of steepness s
# (s -> inf: a step is passed iff theta_t > d, completion deterministic given ability; finite s: execution noise). Steps are
# independent given theta. Chain A has counts nA of steps by type, M has nM, and the chains share nS steps (counted once in
# the joint completion). The difficulty d is recalibrated at every correlation so that alpha_A = N p_A is held fixed.
# rho = p_AM/(p_A p_M); the small-count Accordance bound rho >= N/kappa is solved for the minimum type correlation r_ab.
from numpy.polynomial.hermite_e import hermegauss

# The three-type rows are integrated on a Gauss-Hermite grid with 96 nodes per axis. Validated against the exact pure-chain
# values below, 32 nodes overstate r_ab,min by up to 0.019 at s = 3, 64 nodes by 0.003, 96 nodes by 0.001; on the mixed rows
# 64 and 96 nodes differ by up to 0.013, so the mixed rows are good to about 0.01.
def set_nodes(n):
    global _x, _w, _X, _W
    _x, _w = hermegauss(n); _w = _w / _w.sum()
    _X = np.stack(np.meshgrid(_x, _x, _x, indexing='ij'), -1).reshape(-1, 3)
    _W = (_w[:, None, None] * _w[None, :, None] * _w[None, None, :]).reshape(-1)
set_nodes(96)

def completion(counts, d, R, slope):
    Lc = np.linalg.cholesky(R); theta = _X @ Lc.T
    logq = np.where(theta > d, 0.0, -np.inf) if slope == np.inf else norm.logcdf(slope * (theta - d))
    return float(np.sum(_W * np.exp(logq @ np.asarray(counts, float))))

def _R(r_ab, r_ac, r_bc): return np.array([[1, r_ab, r_ac], [r_ab, 1, r_bc], [r_ac, r_bc, 1]])

def calibrate_d(nA, alpha, N, R, slope):
    lo, hi = -3.0, 8.0
    for _ in range(28):
        mid = 0.5 * (lo + hi)
        if N * completion(nA, mid, R, slope) > alpha: lo = mid
        else: hi = mid
    return hi

def rho_types(nA, nM, nS, r_ab, r_ac, r_bc, slope, alpha, N):
    R = _R(r_ab, r_ac, r_bc); d = calibrate_d(nA, alpha, N, R, slope)
    m = np.asarray(nA) + np.asarray(nM) - np.asarray(nS)
    pA, pM, pAM = completion(nA, d, R, slope), completion(nM, d, R, slope), completion(m, d, R, slope)
    return pA, pM, pAM, pAM / (pA * pM), d

def r_ab_min_pure(n, slope, N, kappa, alpha, r_ac=0.3, r_bc=0.3, h=0.01):
    """Pure chains (n steps of type a against n of type b) exactly: the problem is two-dimensional in (theta_a, theta_b).
    Finite slope: trapezoid quadrature on a fine grid over the region where the completion factor is not negligible;
    slope = inf: P(theta_a > d, theta_b > d) by a one-dimensional integral. A threshold within 1e-3 of the positive-definite
    upper limit is reported as infeasible, the coincidence then requiring essentially perfect correlation."""
    if slope == np.inf:
        d = norm.isf(alpha / N); pA = norm.sf(d)
        def pAM(r):
            sr = np.sqrt(1 - r * r)
            return quad(lambda x: norm.pdf(x) * norm.sf((d - r * x) / sr), d, d + 12, limit=400, epsabs=0, epsrel=1e-11)[0]
    else:
        pa = lambda d: quad(lambda x: norm.pdf(x) * norm.cdf(slope * (x - d))**n, d - 4 * max(1.0, 3.0 / slope), d + 10, limit=400, epsabs=0, epsrel=1e-12)[0]
        lo, hi = -3.0, 12.0
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            if N * pa(mid) > alpha: lo = mid
            else: hi = mid
        d = 0.5 * (lo + hi)
        x = np.arange(d - 3.0 * max(1.0, 3.0 / slope), d + 5.0 + h / 2, h)
        wq = norm.cdf(slope * (x - d))**n * h; wq[0] *= 0.5; wq[-1] *= 0.5
        pA = float(np.sum(wq * norm.pdf(x)))
        Xg, Yg = np.meshgrid(x, x, indexing='ij')
        def pAM(r):
            dens = np.exp(-(Xg**2 - 2 * r * Xg * Yg + Yg**2) / (2 * (1 - r * r))) / (2 * np.pi * np.sqrt(1 - r * r))
            return float(wq @ dens @ wq)
    lo_pd = r_ac * r_bc - np.sqrt((1 - r_ac**2) * (1 - r_bc**2)) + 1e-6
    hi_pd = r_ac * r_bc + np.sqrt((1 - r_ac**2) * (1 - r_bc**2)) - 1e-6
    f = lambda r: pAM(r) / pA**2 >= N / kappa
    if not f(hi_pd): return None
    a, b = lo_pd, hi_pd
    for _ in range(30):
        m = 0.5 * (a + b)
        if f(m): b = m
        else: a = m
    return None if b > hi_pd - 1e-3 else b

def r_ab_min(nA, nM, nS, N, kappa, alpha, slope, r_ac=0.3, r_bc=0.3):
    lo_pd = r_ac * r_bc - np.sqrt((1 - r_ac**2) * (1 - r_bc**2)) + 1e-6
    hi_pd = r_ac * r_bc + np.sqrt((1 - r_ac**2) * (1 - r_bc**2)) - 1e-6
    f = lambda r: rho_types(nA, nM, nS, r, r_ac, r_bc, slope, alpha, N)[3] >= N / kappa
    if not f(hi_pd): return None
    lo, hi = lo_pd, hi_pd
    for _ in range(14):
        mid = 0.5 * (lo + hi)
        if f(mid): hi = mid
        else: lo = mid
    return hi

if __name__ == "__main__":
    N, alpha = 8e9, 0.5
    fmt = lambda vals: " ".join(f"{(v if v is not None else float('nan')):9.3f}" for v in vals)
    print(f"\nThree-type chain model, N = {N:.0e}, alpha_A = {alpha} (d recalibrated at each r_ab), r_ac = r_bc = 0.3; entries r_ab,min")
    print("Pure chains exactly (two-dimensional quadrature); mixed rows on the 96-node grid, good to about 0.01; nan = infeasible.")
    print(f"{'scenario':>32} {'link s':>6} | " + " ".join(f"kappa={k:>3}" for k in (4, 9, 19, 99)))
    for slope in (1.0, 3.0, np.inf):
        vals = [r_ab_min_pure(20, slope, N, k, alpha) for k in (4, 9, 19, 99)]
        print(f"{'pure chains, no shared steps':>32} {('inf' if slope == np.inf else str(slope)):>6} | " + fmt(vals), flush=True)
    rows = [("mixed chains, no shared steps", dict(nA=(16, 2, 4), nM=(2, 16, 4), nS=(0, 0, 0)), 1.0),
            ("mixed chains, no shared steps", dict(nA=(16, 2, 4), nM=(2, 16, 4), nS=(0, 0, 0)), 3.0),
            ("mixed, 3 shared type-c steps", dict(nA=(16, 2, 4), nM=(2, 16, 4), nS=(0, 0, 3)), 1.0)]
    for name, sc, slope in rows:
        vals = [r_ab_min(N=N, kappa=k, alpha=alpha, slope=slope, **sc) for k in (4, 9, 19, 99)]
        print(f"{name:>32} {str(slope):>6} | " + fmt(vals), flush=True)
    print("In the sharp limit s = inf, mixed chains drawing on the same types bound r_ab not at all (rho = N/alpha after recalibration).")
