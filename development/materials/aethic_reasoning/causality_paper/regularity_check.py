# Regularity as the deterministic endpoint, checked by brute force. Binary attributes; a literal is (attribute, value).
# The state's content is deterministic: a set of declared jointly invalid literal sets. A combination (full assignment)
# is valid iff it contains no declared set. A literal set is JOINTLY INVALID iff no valid combination contains it
# (the closure-level notion, not merely "declared"). Claims:
#  (i)   a consistent S is a minimal sufficient condition for e  <=>  S + {not-e} is a minimal jointly invalid set;
#  (iii) each minimal jointly invalid set {x_1..x_k} gives, for every j, a minimal sufficient condition {x_i: i != j} for not-x_j.
import itertools, random
rng = random.Random(478); ATT = ['a', 'b', 'c', 'd']; V = {}
def bad(k, x): V[k] = V.get(k, 0) + bool(x)
lits = [(x, v) for x in ATT for v in (0, 1)]
neg = lambda l: (l[0], 1 - l[1])
cons = lambda S: len({x for x, _ in S}) == len(S)
checked = 0
for trial in range(600):
    declared = [frozenset(rng.sample([l for l in lits], rng.randint(2, 3))) for _ in range(rng.randint(1, 4))]
    declared = [d for d in declared if cons(d)]
    combos = [dict(zip(ATT, vals)) for vals in itertools.product((0, 1), repeat=4)]
    valid = [c for c in combos if not any(all(c[x] == v for x, v in d) for d in declared)]
    if not valid: continue                                   # an invalid state: every set is jointly invalid
    holds = lambda S, c: all(c[x] == v for x, v in S)
    jinv = lambda S: cons(S) and not any(holds(S, c) for c in valid)
    subsets = [frozenset(S) for r in range(0, 5) for S in itertools.combinations(lits, r) if cons(S)]
    min_inv = {S for S in subsets if jinv(S) and not any(jinv(T) for T in subsets if T < S)}
    for e in lits:
        for S in subsets:
            if e[0] in {x for x, _ in S} or not any(holds(S, c) for c in valid): continue      # S must not mention E, and be consistent (realizable)
            suff = all(c[e[0]] == e[1] for c in valid if holds(S, c))
            minimal = suff and not any(all(c[e[0]] == e[1] for c in valid if holds(T, c)) for T in subsets if T < S and any(holds(T, c) for c in valid))
            bad('(i) minimal sufficient  !=  S + not-e minimal jointly invalid', minimal != (frozenset(S | {neg(e)}) in min_inv))
            checked += 1
    for M in min_inv:
        if len(M) < 2: continue
        for xj in M:
            T = M - {xj}; target = neg(xj)
            suff = all(c[target[0]] == target[1] for c in valid if holds(T, c))
            minimal = suff and not any(all(c[target[0]] == target[1] for c in valid if holds(U, c)) for U in subsets if U < T and any(holds(U, c) for c in valid))
            bad('(iii) a reading of a minimal invalid set is not minimal sufficient', not (any(holds(T, c) for c in valid) and minimal))
print(f"checked {checked} (S, e) pairs over 600 random deterministic states")
for k, x in V.items(): print(f"  {k:<66} violations: {x}")
print("REGULARITY PROPOSITION HOLDS" if not any(V.values()) else "VIOLATION")
