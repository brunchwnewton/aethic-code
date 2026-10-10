# transparent_newcomb_shared_model.py — the shared transparent-predictor model of the decision paper (Definition and
# Proposition "The two verdicts in the shared model"). The predictor targets the agent's policy upon seeing box B full,
# errs with probability eps, and B is filled iff the prediction is one-box; the agent sees B before acting.
# Functional decision theory evaluates the policy before the observation; the settling rule evaluates after it.
M, t = 1_000_000, 1_000

def fdt_values(eps):
    one = (1 - eps) * M + eps * t            # policy one-box-on-full: full w.p. 1-eps -> M ; empty w.p. eps -> t
    two = (1 - eps) * t + eps * (M + t)      # policy two-box-on-full: empty w.p. 1-eps -> t ; full w.p. eps -> M+t
    return one, two

def fdt_full(eps):      return "one-box" if fdt_values(eps)[0] > fdt_values(eps)[1] else "two-box"
def settling_full(eps): return "one-box" if eps == 0 else "two-box"   # eps>0: mismatch pocket admissible, M+t > M; eps=0: admissibility rule
def empty(eps):         return "two-box"                                # both rules: t over nothing

if __name__ == "__main__":
    thr = (M - t) / (2 * M - t)
    print(f"FDT one-boxes on a full box iff eps < (M-t)/(2M-t) = {thr:.4f}")
    print(f"{'eps':>6} | {'FDT (full)':>10} {'settling (full)':>16} {'both (empty)':>13} | {'EV one-box policy':>18} {'EV two-box policy':>18}")
    for eps in (0.0, 0.001, 0.01, 0.1, 0.3, 0.4998, 0.5, 0.6):
        one, two = fdt_values(eps)
        print(f"{eps:6.4f} | {fdt_full(eps):>10} {settling_full(eps):>16} {empty(eps):>13} | {one:18,.0f} {two:18,.0f}")
    print("Divergence on a full box exactly for 0 < eps < threshold: FDT one-boxes, the settling rule two-boxes; they agree at eps = 0 and on an empty box.")
