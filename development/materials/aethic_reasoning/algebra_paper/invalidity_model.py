# R494 (Weight Algebra): the referee's small explicit model. Two binary attributes a, b; carriers are the consistent
# partial assignments plus the all-statements carrier HYP. The doom set D = least fixed point of
# G(X) = Base u {A : for all B below A, some C below B lies in X}, computed under two readings of "below".
import itertools
atoms = [('a', '1'), ('a', '0'), ('b', '1'), ('b', '0')]
parts = [frozenset(c) for k in range(3) for c in itertools.combinations(atoms, k) if len({x for x, _ in c}) == len(c)]
U = parts + ['HYP']; name = lambda A: 'HYP' if A == 'HYP' else (''.join(x + v for x, v in sorted(A)) or 'blank')
below_cc = lambda B, A: B == 'HYP' or (A != 'HYP' and B >= A)                    # closed-content inclusion: HYP below all
below_adm = lambda B, A: B == A or (A != 'HYP' and B != 'HYP' and B >= A)         # admissible refinement: never reaches HYP
def doom(base, below):
    X = set()
    while True:
        Y = set(base) | {A for A in U if all(any(below(C, B) and C in X for C in U) for B in U if below(B, A))}
        if Y == X: return X
        X = Y
S1 = {'HYP', frozenset({('a', '1'), ('b', '1')})}
S2 = S1 | {frozenset({('a', '1'), ('b', '0')})}
for label, base in [('one joint invalidity tagged, {a1 b1}', S1), ('both branches of a1 tagged, a1 itself untagged', S2)]:
    Dcc, Dadm = doom(base, below_cc), doom(base, below_adm)
    print(f"Base = {sorted(map(name, base))}  ({label})")
    print(f"   closed-content inclusion: D has {len(Dcc)} of {len(U)} carriers" + ("  -> D = U, nothing valid" if len(Dcc) == len(U) else ""))
    print(f"   admissible refinement:    D = {sorted(map(name, Dadm))}; the blank is {'invalid' if frozenset() in Dadm else 'valid'}")
    untagged_doomed = [name(A) for A in Dadm if A not in base]
    print(f"   untagged but doomed under admissible refinement: {untagged_doomed or 'none'}"
          + ("  -> the Status reading (valid = untagged) calls these valid; harmonization (valid = outside D) does not" if untagged_doomed else ""))
print("Implication example (Base as in the first line): A = a1 leaves b open; its branch a1b1 is tagged, a1b0 survives.")
print("   residue A - A b0 = [a1 b1] = 0 in the quotient, yet [a1] and [a1 b0] are distinct carriers unless a closure rule identifies them.")
