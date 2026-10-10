# R491 (C8): counterfactuals need functional structure; with it, abduction-action-prediction by pruning equals Pearl's.
import itertools, random
from fractions import Fraction as F
# (i) M1: Y = U; M2: Y = X xor U; X, U independent fair bits.
def law(model):
    obs, do, cf = {}, {}, {}
    for x, u in itertools.product((0, 1), repeat=2):
        y = u if model == 1 else x ^ u; obs[(x, y)] = obs.get((x, y), 0) + F(1, 4)
    for x in (0, 1):
        for u in (0, 1):
            y = u if model == 1 else x ^ u; do[(x, y)] = do.get((x, y), 0) + F(1, 2)
    post = {u: F(1) for u in (0, 1) if (u if model == 1 else 0 ^ u) == 0}      # evidence X=0, Y=0 prunes U
    z = sum(post.values()); cfy = {u: (u if model == 1 else 1 ^ u) for u in post}
    return obs, do, {y: sum(w / z for u, w in post.items() if cfy[u] == y) for y in (0, 1)}
o1, d1, c1 = law(1); o2, d2, c2 = law(2)
print(f"(i) same observational law: {o1 == o2}; same interventional law: {d1 == d2}; counterfactual Y_(X<-1) given X=0,Y=0: M1 {c1}, M2 {c2}")
# (ii) random deterministic SCMs over a chain of binary variables with background bits; compare the pruning-based
#      counterfactual (prune by evidence, settle X=x' retaining background weights, recompute descendants) with a
#      brute-force twin-world computation that never shares code with it.
random.seed(491); bad = 0; trials = 3000
for _ in range(trials):
    n = random.randint(3, 5); parents = {k: [j for j in range(k) if random.random() < 0.5] for k in range(n)}
    funcs = {k: {key: random.randint(0, 1) for key in itertools.product((0, 1), repeat=len(parents[k]) + 1)} for k in range(n)}
    pu = [F(random.randint(1, 9), 10) for _ in range(n)]                     # P(u_k = 1)
    def solve(u, fix=None):
        v = {}
        for k in range(n):
            v[k] = fix[1] if fix and fix[0] == k else funcs[k][tuple(v[j] for j in parents[k]) + (u[k],)]
        return v
    X, Y = random.sample(range(n), 2); ev = {k: random.randint(0, 1) for k in random.sample(range(n), random.randint(1, n))}
    xp = random.randint(0, 1)
    # pruning route: the state's weights on background combinations, pruned by the evidence, then settle X = xp
    w = {}
    for u in itertools.product((0, 1), repeat=n):
        wt = F(1)
        for k in range(n): wt *= pu[k] if u[k] else 1 - pu[k]
        v = solve(u)
        if all(v[k] == val for k, val in ev.items()): w[u] = wt
    if not w: continue
    z = sum(w.values()); a = sum(wt for u, wt in w.items() if solve(u, (X, xp))[Y] == 1) / z
    # brute force twin world: enumerate (u, factual world, counterfactual world) jointly
    num = den = F(0)
    for u in itertools.product((0, 1), repeat=n):
        wt = F(1)
        for k in range(n): wt *= pu[k] if u[k] else 1 - pu[k]
        fact = {}; cfw = {}
        for k in range(n):
            fact[k] = funcs[k][tuple(fact[j] for j in parents[k]) + (u[k],)]
            cfw[k] = xp if k == X else funcs[k][tuple(cfw[j] for j in parents[k]) + (u[k],)]
        if all(fact[k] == val for k, val in ev.items()): den += wt; num += wt * cfw[Y]
    bad += a != num / den
print(f"(ii) pruning-based counterfactual vs brute-force twin world, {trials} random SCMs: {bad} disagreements")
