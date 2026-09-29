# Strong Accordance, full modal form, checked. Model: contrast R ~ Uniform(-M, M) (the Hypothesis), prior log-odds
# l = log10(p/(1-p)) of side A, S = R + l (Aetherian log-odds of A). The realization lands on A with probability
# 1/(1+10^-S). Event E_kappa: the complement's Aetherian weight >= kappa times the realized side's.
# Claim: P(E_kappa) <= ( [log10(1/kappa)]^+ + log10(1 + min(kappa, 1/kappa)) ) / M, for every kappa > 0 and every prior.
import numpy as np
rng = np.random.default_rng(480)
def exact(kappa, M, l, n=400001):
    s = np.linspace(l - M, l + M, n); k = np.log10(kappa)
    qA = 1 / (1 + 10.0 ** (-s))
    f = qA * (s <= -k) + (1 - qA) * (s >= k)          # land on A and 10^-S >= kappa; or land on A' and 10^S >= kappa
    return np.trapezoid(f, s) / (2 * M)
bound = lambda kappa, M: (max(0.0, np.log10(1 / kappa)) + np.log10(1 + min(kappa, 1 / kappa))) / M
worst, rows = 0.0, []
for M in [5, 20, 100, 1000]:
    for p in [1e-12, 1e-4, 0.01, 0.3, 0.5, 0.9]:
        l = np.log10(p / (1 - p))
        for kappa in [1e-6, 1e-3, 0.1, 0.5, 1.0, 2.0, 10.0, 1e3]:
            e, b = exact(kappa, M, l), bound(kappa, M)
            worst = max(worst, e / b)
            if p in (1e-12, 0.3) and M == 20: rows.append((M, p, kappa, e, b, 1 / (1 + kappa) if kappa >= 1 else float('nan')))
print("max(exact / bound) over all M, priors, kappa:", round(worst, 6), "(<= 1 means the bound holds)")
print(f"{'M':>5} {'prior':>8} {'kappa':>8} {'exact':>12} {'bound':>12} {'Accordance':>11}")
for M, p, kappa, e, b, a in rows: print(f"{M:>5} {p:>8.0e} {kappa:>8.0e} {e:>12.3e} {b:>12.3e} {a:>11.3e}")
# Monte Carlo of the two-stage draw at one setting, as an independent cross-check of the exact integral.
M, p, kappa, N = 20, 1e-4, 1e-3, 2_000_000
S = rng.uniform(-M, M, N) + np.log10(p / (1 - p)); onA = rng.random(N) < 1 / (1 + 10.0 ** (-S))
ratio = np.where(onA, 10.0 ** (-S), 10.0 ** S)                 # complement weight / realized weight
print(f"Monte Carlo (M={M}, prior={p}, kappa={kappa}): {np.mean(ratio >= kappa):.5f}  exact {exact(kappa, M, np.log10(p/(1-p))):.5f}  bound {bound(kappa, M):.5f}")

# Closed-form exact probability (no quadrature). On [lo, hi] = [l-M, l+M]:
#   landing on A with 10^-S >= kappa: integral of 10^s/(1+10^s) over s <= -k   -> antiderivative log10(1+10^s)
#   landing on A' with 10^S >= kappa: integral of 1/(1+10^s) over s >= k       -> antiderivative -log10(1+10^-s)
def exact_cf(kappa, M, l):
    lo, hi, k = l - M, l + M, np.log10(kappa)
    F1 = lambda s: np.logaddexp(0, s * np.log(10)) / np.log(10)          # log10(1+10^s), stable
    F2 = lambda s: -np.logaddexp(0, -s * np.log(10)) / np.log(10)        # -log10(1+10^-s), stable
    a1, b1 = lo, min(hi, -k); a2, b2 = max(lo, k), hi
    tot = (F1(b1) - F1(a1) if b1 > a1 else 0.0) + (F2(b2) - F2(a2) if b2 > a2 else 0.0)
    return tot / (2 * M)
worst_cf, where = 0.0, None
for M in [5, 20, 100, 1000, 10**4]:
    for p in [1e-30, 1e-12, 1e-4, 0.01, 0.3, 0.5, 0.9, 1 - 1e-9]:
        l = np.log10(p / (1 - p))
        for kappa in np.logspace(-8, 8, 161):
            r = exact_cf(kappa, M, l) / bound(kappa, M)
            if r > worst_cf: worst_cf, where = r, (M, p, kappa)
print("closed form: max(exact / bound) =", round(worst_cf, 9), "at (M, prior, kappa) =", where)
print("agreement with quadrature at M=20, p=1e-4, kappa=1e-3:", exact_cf(1e-3, 20, np.log10(1e-4/(1-1e-4))))
