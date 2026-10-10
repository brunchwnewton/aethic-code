"""Supplementary script for the sequential-achievement paper (howlong.tex).

Classifies Gumbel-process realizations of the top fifty latent scores by
whether the task is "in the air" (the collective of ranks #2 onward completes
it with near certainty) or "record-holder only", at the paper's calibration.

Model (paper, Part II):
  per-step success   p(s)   = 1 - (1 - p0)^s
  expected steps     E[M_n] = (p^-n - 1) / (1 - p)      (full restart)
  collective rate    R      = sum_{j>=2} lambda / E[M_n | s_j]   per on-task hour
  collective success P      = 1 - exp(-R * T)

Scores (paper, Part I): s = exp(sigma * z), median score 1, sigma = 0.5911.
Top order statistics of N standard normals are drawn by the Poisson-arrival
representation: upper-tail probabilities Gamma_j / N with Gamma_j a sum of
j unit exponentials, z_j = Phi^{-1}(1 - Gamma_j / N).

Check: the share of realizations whose record-holder gap exceeds 15% should
come out near the paper's "approximately 20% of draws" (it gives ~21%).
"""
import numpy as np
from scipy.stats import norm

N = 8e9            # population
SIGMA = 0.5911     # log-space dispersion
P0 = 0.1455        # baseline per-step success
LAM = 252.0        # steps per on-task hour
K = 50             # ranks simulated
T = 8.77e6         # horizon: 1,000 on-task years, in on-task hours (E2's unit)
NEAR = 0.95        # "near certainty"
REALIZATIONS = 200_000
SEED = 20261007


def log_expected_steps(n, s):
    """log of (p^-n - 1)/(1 - p) with q = 1 - p = (1 - P0)^s, computed stably."""
    q = (1.0 - P0) ** s
    a = -n * np.log1p(-q)
    return a + np.log1p(-np.exp(-a)) - np.log(q)


def main():
    rng = np.random.default_rng(SEED)
    arrivals = np.cumsum(rng.exponential(size=(REALIZATIONS, K)), axis=1)
    s = np.exp(SIGMA * norm.isf(arrivals / N))
    gap = s[:, 0] / s[:, 1] - 1.0
    print(f"record-holder gap > 15%: {np.mean(gap > 0.15):.1%} of realizations")
    for n, label in [(5949, "special relativity"), (7700, "base calibration"),
                     (8859, "general relativity"), (11453, "Newtonian mechanics")]:
        rate = np.exp(np.log(LAM) - log_expected_steps(n, s[:, 1:])).sum(axis=1)
        P = 1.0 - np.exp(-rate * T)
        print(f"n = {n:>6} ({label:19s}): in the air {np.mean(P >= NEAR):5.1%} | "
              f"intermediate {np.mean((P > 1 - NEAR) & (P < NEAR)):5.1%} | "
              f"record-holder only {np.mean(P <= 1 - NEAR):5.1%}")


if __name__ == "__main__":
    main()
