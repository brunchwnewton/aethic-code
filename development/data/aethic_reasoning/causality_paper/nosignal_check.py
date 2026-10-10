# R494 (causality paper): no-signaling at the level of the far wing's product.
from fractions import Fraction as Fr
import random, itertools, math
# (1) the referee's counterexample: two factors 1 + t_y a b, each balanced, product not
def marg(t):
    S = {a: sum((1 + t * a * b) ** 2 for b in (-1, 1)) for a in (0, 1)}
    return S[1] / (S[0] + S[1])
print("(1) factorwise sums:", {t: [sum(1 + t * a * b for b in (-1, 1)) for a in (0, 1)] for t in (Fr(0), Fr(1, 2))},
      "| P(a=1) at t=0:", marg(Fr(0)), " at t=1/2:", marg(Fr(1, 2)))
# (2) the singlet's far wing is one factor, 1 - a b x.y, summing over b to 2 for every a, x, y
random.seed(494); worst = 0
for _ in range(2000):
    x = [random.gauss(0, 1) for _ in range(3)]; y = [random.gauss(0, 1) for _ in range(3)]
    nx, ny = math.sqrt(sum(v * v for v in x)), math.sqrt(sum(v * v for v in y)); dot = sum(p * q for p, q in zip(x, y)) / (nx * ny)
    for a in (-1, 1): worst = max(worst, abs(sum(1 - a * b * dot for b in (-1, 1)) - 2))
print("(2) singlet far wing: max |sum_b - 2| over 2000 random setting pairs =", worst)
# (3) both directions of the equivalence on random strictly positive tables
bad = 0
for _ in range(3000):
    A, Bn, Y = random.randint(2, 3), random.randint(2, 3), random.randint(2, 3)
    F = [Fr(random.randint(1, 9)) for _ in range(A)]
    fac = random.random() < 0.5
    if fac:   # G built so that S = g(a) h(y): scale a random base table per (a, y)
        g = [Fr(random.randint(1, 9)) for _ in range(A)]; h = [Fr(random.randint(1, 9)) for _ in range(Y)]
        base = [[[Fr(random.randint(1, 9)) for _ in range(Bn)] for _ in range(Y)] for _ in range(A)]
        G = [[[base[a][y][b] * g[a] * h[y] / sum(base[a][y]) for b in range(Bn)] for y in range(Y)] for a in range(A)]
    else:
        G = [[[Fr(random.randint(1, 9)) for _ in range(Bn)] for _ in range(Y)] for _ in range(A)]
    S = [[sum(G[a][y]) for y in range(Y)] for a in range(A)]
    margs = [tuple(F[a] * S[a][y] / sum(F[k] * S[k][y] for k in range(A)) for a in range(A)) for y in range(Y)]
    no_sig = len(set(margs)) == 1
    factors = all(S[a][y] * S[0][0] == S[a][0] * S[0][y] for a in range(A) for y in range(Y))
    bad += no_sig != factors
print(f"(3) no-signaling iff the far-wing sum factors as g(a)h(y): {bad} disagreements in 3000 random tables")
