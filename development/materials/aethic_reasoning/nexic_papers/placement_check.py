# Concentration is rarity, simulated. Profiles over K = 2^n cells: shape from HCEH contrasts (differences), level placed
# by the placement clause (top log-productivity T ~ Uniform(-W, 0]). Random priors. Check: P(H) <= 10^T always;
# Pr[P(H) > 10^-t] <= t/W; and the joint event (our cell the Aetherian majority AND P(H) <= 10^-t).
import numpy as np
rng = np.random.default_rng(481); n, M, W, t, N = 6, 40.0, 400.0, 20.0, 40000
K = 2 ** n; bits = (np.arange(K)[:, None] >> np.arange(n)) & 1
viol, rare, joint = 0, 0, 0
for _ in range(N):
    R = rng.uniform(-M, M, n)                                    # difference clause: per-attribute contrasts
    shape = (bits * R).sum(1); shape -= shape.max()              # log-productivity profile, top at 0
    T = -rng.uniform(0, W)                                       # placement clause: the level
    logprod = shape + T
    prior = rng.dirichlet(np.ones(K))
    logw = logprod + np.log10(prior); m = logw.max(); w = 10 ** (logw - m); Q = w / w.sum()
    logPH = m + np.log10(w.sum())                                # log10 P(H), computed stably
    viol += logPH > T + 1e-9
    rare += logPH <= -t
    ours = rng.choice(K, p=Q)
    joint += (logPH <= -t) and (Q[ours] > 0.5)
print(f"P(H) <= 10^T violations: {viol} of {N}")
print(f"Pr[P(H) > 10^-{t:.0f}] = {1 - rare / N:.4f}   bound t/W = {t / W:.4f}")
print(f"joint: our cell is the Aetherian majority AND P(H) <= 10^-{t:.0f}: {joint / N:.4f}")
