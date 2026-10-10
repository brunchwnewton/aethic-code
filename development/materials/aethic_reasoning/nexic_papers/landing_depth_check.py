# landing_depth_check.py (R489): checks the landing-depth route to M in optimal_earth (sec:landing-depths) and the long
# Nexic paper (sec:nx-landing-depths), and computes the figures quoted there.
import numpy as np
from math import erf, sqrt, pi, log10, exp
rng = np.random.default_rng(489)
Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
viol = {}

# 1. prop:landing-gap: t_C = theta_C - log10 y_C - log10 F_C and R = (theta_A' - theta_A) + zeta, exactly, on random finite cells
bad = 0
for _ in range(4000):
    def cell():
        k = rng.integers(1, 12); w = rng.dirichlet(np.ones(k)) * rng.uniform(1e-6, 1); yld = rng.uniform(0, 1, k) ** rng.uniform(1, 30)
        succ = w * yld; o = np.argmax(succ); PC = w.sum(); F = succ.sum() / succ[o]
        theta = -log10(w[o] / PC); t = -log10(succ.sum() / PC)
        return t, theta, yld[o], F
    tA, thA, yA, FA = cell(); tB, thB, yB, FB = cell()
    bad += abs(tA - (thA - log10(yA) - log10(FA))) > 1e-9 or abs((tB - tA) - ((thB - thA) + log10(yA * FA / (yB * FB)))) > 1e-9 or FA < 1 - 1e-12
viol['landing-gap identity (4,000 cell pairs)'] = bad

# 2. (i): t_A with a piecewise-constant density <= h, t_A' arbitrary (atoms allowed): sup density of R = t_A' - t_A <= h
bad = 0
for _ in range(1500):
    edges = np.sort(rng.uniform(0, 60, rng.integers(2, 9))); dens = rng.uniform(0, 1, len(edges) - 1); dens /= (dens * np.diff(edges)).sum()
    h = dens.max(); atoms = rng.uniform(-40, 80, rng.integers(1, 7)); pw = rng.dirichlet(np.ones(len(atoms)))
    grid = np.linspace(-120, 120, 6001)
    f_tA = lambda x: np.select([(x >= edges[i]) & (x < edges[i + 1]) for i in range(len(dens))], dens, 0.0)
    fR = sum(p * f_tA(a - grid) for a, p in zip(atoms, pw))          # density of R at r is sum_j p_j f_tA(a_j - r)
    bad += fR.max() > h * (1 + 1e-9)
viol['(i) difference density <= h (1,500 laws)'] = bad

# 3. (ii): the minimum of K independent depths, each with density <= 1/W, has density <= K/W
bad = 0
for _ in range(800):
    K = rng.integers(2, 7); W = rng.uniform(5, 200); x = np.linspace(0, 3 * W, 4001); fmin = np.zeros_like(x); surv = []
    laws = []
    for _k in range(K):
        a = rng.uniform(0, 2 * W); laws.append((a, a + W))                  # uniform on [a, a+W): density exactly 1/W
    for i, (a, b) in enumerate(laws):
        f = ((x >= a) & (x < b)) / W
        others = np.prod([np.clip((b2 - x) / W, 0, 1) if True else 1 for j, (a2, b2) in enumerate(laws) if j != i] or [np.ones_like(x)], axis=0)
        others = np.prod([np.where(x < a2, 1.0, np.clip((b2 - x) / W, 0, 1)) for j, (a2, b2) in enumerate(laws) if j != i], axis=0)
        fmin += f * others
    bad += fmin.max() > K / W * (1 + 1e-9)
viol['(ii) top-cell gap density <= K/W (800 partitions)'] = bad

# 4. (iii): Var of m equicorrelated costs = sigma^2 m (1 + (m-1) rho)
bad = 0
for _ in range(60):
    m, s, r = rng.integers(2, 60), rng.uniform(0.1, 2), rng.uniform(0, 0.9)
    X = s * (np.sqrt(r) * rng.standard_normal((40000, 1)) + np.sqrt(1 - r) * rng.standard_normal((40000, m)))
    bad += abs(X.sum(1).var() / (s * s * m * (1 + (m - 1) * r)) - 1) > 0.05
viol['(iii) equicorrelated variance (60 laws, MC 5%)'] = bad

# 5. (iv): local M. Failure probability computed exactly for mixtures of Gaussians for S, against
#    ([log10(1/k)]^+ + log10(1 + min(k, 1/k))) / M(u) + 1/(1 + 10^u), M(u) = 1/(2 sup_{|s|<u} f_S)
def fail_prob(ws, ms, ss, kappa, grid=np.linspace(-400, 400, 1600001)):
    f = sum(w * np.exp(-0.5 * ((grid - m) / s) ** 2) / (s * sqrt(2 * pi)) for w, m, s in zip(ws, ms, ss))
    a = abs(log10(kappa)); a_abs = np.abs(grid)
    pf = np.where(a_abs < a, 1.0 if kappa < 1 else 0.0, 1 / (1 + 10.0 ** np.minimum(a_abs, 300)))
    pf = np.where((kappa >= 1) & (a_abs < a), 0.0, pf)
    return (pf * f).sum() * (grid[1] - grid[0]), grid, f
bad = worst = 0
for _ in range(300):
    k = rng.integers(1, 4); ws = rng.dirichlet(np.ones(k)); ms = rng.uniform(-30, 60, k); ss = rng.uniform(0.5, 25, k)
    for kappa in (0.1, 0.5, 1.0, 2.0, 10.0):
        pfail, grid, f = fail_prob(ws, ms, ss, kappa)
        for u in (abs(log10(kappa)) + 0.5, 3.0, 10.0):
            if u < abs(log10(kappa)): continue
            Mu = 1 / (2 * f[np.abs(grid) < u].max())
            bound = (max(log10(1 / kappa), 0) + log10(1 + min(kappa, 1 / kappa))) / Mu + 1 / (1 + 10 ** u)
            bad += pfail > bound * (1 + 1e-6) + 1e-12; worst = max(worst, pfail / bound)
viol['(iv) local-M bound (300 laws x 5 kappas x 3 windows)'] = bad

for k, v in viol.items(): print(f"  {k}: {v} violations")
print(f"  (iv) largest failure/bound ratio: {worst:.3f}")

# 6. The regime table: effective M at kappa = 1 is log10(2) / Pr[fail], computed exactly in the Gaussian model.
mu, sd, rho, om = 0.5, 0.5, 0.3, 0.3
def M_eff(depth, rho_x=0.0, omega=0.0):
    m = int(round(depth / mu)); v1 = sd**2 * m * (1 + (m - 1) * rho_x); v2 = (sd * (1 + omega))**2 * m * (1 + (m - 1) * rho_x)
    pfail, _, _ = fail_prob([1.0], [m * mu * omega], [sqrt(v1 + v2)], 1.0)
    return log10(2) / pfail
print("\n  table (effective M at kappa = 1):  depth | independent | coupled rho=0.3 | alternative 30% costlier")
for depth in (20, 50, 100):
    print(f"  {depth:>5} | {M_eff(depth):>8.1f} | {M_eff(depth, rho_x=rho):>8.1f} | {M_eff(depth, omega=om):>10.1f}")
print("  closed forms at depth 50:", f"sqrt(pi m) sd = {sqrt(pi * 100) * sd:.1f};  sqrt(pi rho) L = {sqrt(pi * rho) * 50:.1f}")

# 7. Which depths the placement examples (W = 400, W = 10^4 for the top-cell gap, binary partition) correspond to under
#    (ii): per-cell spread 2W; Gaussian per-cell depth with sd s has density <= 1/(s sqrt(2 pi)), i.e. width s sqrt(2 pi).
for Wp in (400, 1e4):
    Wc = 2 * Wp; s_needed = Wc / sqrt(2 * pi)
    L_coupled = s_needed / (sqrt(rho) * sd / mu)                      # s ~ sqrt(rho) (sd/mu) L for large m
    L_indep = (s_needed / sd) ** 2 * mu                               # s = sd sqrt(m), L = m mu
    print(f"  placement W = {Wp:g}: landing depth ~ {L_coupled:,.0f} orders with coupled costs, ~ {L_indep:,.0f} with independent costs")

# 8. End-to-end: two-stage draws from constructed costs; failure rate at kappa = 1 against log10(2)/M_eff
for name, r_x, w_x in (("independent", 0.0, 0.0), ("coupled", rho, 0.0), ("different decisions", 0.0, om)):
    m, N = 100, 400000
    def branch(scale):
        z0 = rng.standard_normal((N, 1)); z = rng.standard_normal((N, m))
        return (mu * scale + sd * scale * (np.sqrt(r_x) * z0 + np.sqrt(1 - r_x) * z)).sum(1)
    S = branch(1 + w_x) - branch(1.0)                                  # zeta = 0: S = theta_A' - theta_A
    landed_on_A = rng.uniform(size=N) < 1 / (1 + 10.0 ** np.clip(-S, -300, 300))
    fail = np.where(landed_on_A, S < 0, S > 0).mean()                 # kappa = 1: the side landed on is outweighed
    print(f"  end-to-end {name:>19}: failure {fail:.5f}  vs log10(2)/M_eff = {log10(2) / M_eff(50, r_x, w_x):.5f}")
