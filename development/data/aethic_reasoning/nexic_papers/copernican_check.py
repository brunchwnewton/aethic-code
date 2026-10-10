# Checks for the R476 corrections to nexic.tex (Copernican) and optimal_earth.tex, in exact arithmetic.
import itertools, random
from fractions import Fraction as Fr
rng = random.Random(476)
V = {}
def v(k, bad): V[k] = V.get(k, 0) + bool(bad)

# 1. The referee's table: marginal ratio 1/99 each, neighbor-cell ratio 1/98; our corrected constant is exactly 1/98.
Q = {(0, 0): Fr(98, 100), (0, 1): Fr(1, 100), (1, 0): Fr(1, 100), (1, 1): Fr(0)}
r = [sum(q for c, q in Q.items() if c[i] == 1) / sum(q for c, q in Q.items() if c[i] == 0) for i in range(2)]
s = sum(ri / (1 + ri) for ri in r)
print("table: marginal ratios", r, "| neighbor ratio", Q[(0, 1)] / Q[(0, 0)], "| corrected constant", r[1] / ((1 + r[1]) * (1 - s)), "| union bound", 1 - s, "vs Q(C*) =", Q[(0, 0)])

# 2. Random observer-conditioned laws over n coordinates of b values, our cell C* = all zeros.
tight = 0
for trial in range(4000):
    n, b = rng.choice([2, 3, 4]), rng.choice([2, 2, 3])
    cells = list(itertools.product(range(b), repeat=n)); cstar = (0,) * n
    w = {c: Fr(rng.choice([0, 1, 2, 3, 5, 8])) for c in cells}; w[cstar] += Fr(rng.randint(1, 400))
    Z = sum(w.values()); Q = {c: x / Z for c, x in w.items()}
    rs = []
    for i in range(n):
        A = sum(q for c, q in Q.items() if c[i] == 0); Ac = 1 - A
        rs.append(Ac / A)                                   # the tightest ratio for which Q(A_i^c) <= r_i Q(A_i) holds
    s = sum(ri / (1 + ri) for ri in rs)
    v('union bound: Q(C*) < 1 - sum r/(1+r)', Q[cstar] < 1 - s)
    if s < 1:
        for i in range(n):
            for val in range(1, b):
                N = tuple(val if j == i else 0 for j in range(n)); bound = rs[i] / ((1 + rs[i]) * (1 - s))
                v('per-cell: Q(N_i)/Q(C*) exceeds r_i/((1+r_i)(1-s))', Q[N] / Q[cstar] > bound)
                tight += Q[N] / Q[cstar] == bound
    # the naive per-cell claim with constant r_i (the text's "a fortiori") fails somewhere?
    v('(expected failures) naive per-cell claim Q(N_i) <= r_i Q(C*)', any(Q[tuple(val if j == i else 0 for j in range(n))] > rs[i] * Q[cstar] for i in range(n) for val in range(1, b)))
print("tight per-cell cases:", tight)

# 3. The finite Rare Earth test: reject P(H) >= h when the realized cell has cosmic prior <= delta*h/K. Size <= delta.
for trial in range(3000):
    K = rng.choice([2, 4, 8, 16]); h = Fr(rng.randint(1, 9), 10); delta = Fr(rng.randint(1, 20), 100)
    P = [Fr(rng.randint(0, 50)) for _ in range(K)]; P = [x / sum(P) for x in P] if sum(P) else [Fr(1, K)] * K
    # an H-joint law: P(c and H) <= P(c), with total P(H) = h' >= h (the null)
    joint = [x * Fr(rng.randint(0, 100), 100) for x in P]; tot = sum(joint)
    if tot == 0: continue
    target = h + (1 - h) * Fr(rng.randint(0, 100), 100)      # P(H) in [h, 1]
    scale = target / tot
    if any(j * scale > p for j, p in zip(joint, P)): continue    # must stay a sub-measure of P
    Qc = [j * scale / target for j in joint]
    size = sum(q for q, p in zip(Qc, P) if p <= delta * h / K)
    v('realized-cell test size exceeds delta', size > delta)
# the binary all-rare case: the all-rare cell (prior <= p^m under A1) is rejected exactly when (2p)^m <= delta*eps
for p in [Fr(1, 10), Fr(1, 4), Fr(3, 10), Fr(2, 5), Fr(49, 100)]:
    for eps, delta in [(Fr(1, 100), Fr(1, 20)), (Fr(1, 10**6), Fr(1, 100))]:
        m = next(m for m in range(1, 10**4) if (2 * p) ** m <= delta * eps)
        v('finite m: all-rare prior not below delta*eps/2^m', p ** m > delta * eps / 2 ** m)
print("m needed at p=0.3, eps=1e-6, delta=0.01:", next(m for m in range(1, 999) if (2 * Fr(3, 10)) ** m <= Fr(1, 100) * Fr(1, 10**6)))

# 4. Coupling does not give cumulative suppression: W(00)=W(11)=1, W(01)=W(10)=eps.
eps = Fr(1, 10**6); W = {(0, 0): 1, (1, 1): 1, (0, 1): eps, (1, 0): eps}
print("two-peak: unit perturbations suppressed by", W[(0, 1)] / W[(0, 0)], "| double perturbation restores", W[(1, 1)] / W[(0, 0)], "(cumulative suppression fails)")

# 5. Point 2: for a fixed binary partition E[1/Q_i] = 2 exactly, whatever the split.
for q in [Fr(1, 10), Fr(1, 3), Fr(1, 2), Fr(9, 10)]:
    v('E[1/Q] != 2', q * (1 / q) + (1 - q) * (1 / (1 - q)) != 2)
for k, x in V.items(): print(f"  {k:<62} {'cases' if 'expected' in k else 'violations'}: {x}")
print("ALL CORRECTED CLAIMS HOLD" if all(x == 0 for k, x in V.items() if 'expected' not in k) else "VIOLATION")
