# Brute-force check of the Cut counterexample under modal.tex's definitions (M1). Attributes, each two-valued:
#   P (a stated generalization, p / not-p), R (a particular, r / not-r), QX (v / x), QY (y / n).
# Constraint layer (laws, not retractable): {P=p, QY=n} invalid (p -> y); {P=p, R=r, QX=x} invalid (p & r -> v).
from itertools import product, combinations
ATTR = {'P': ('p', '-p'), 'R': ('r', '-r'), 'QX': ('v', 'x'), 'QY': ('y', 'n')}
INVALID = [{('P', 'p'), ('QY', 'n')}, {('P', 'p'), ('R', 'r'), ('QX', 'x')}]
def consistent(entries):                              # a partial assignment is valid iff it extends to a complete one avoiding every invalid set
    d = dict(entries)
    if len(d) < len(entries): return False
    free = [a for a in ATTR if a not in d]
    for vals in product(*(ATTR[a] for a in free)):
        full = set(d.items()) | set(zip(free, vals))
        if not any(inv <= full for inv in INVALID): return True
    return False
def closure(entries):                                 # add every forced entry: (a, v) is forced if the alternative value is inconsistent
    S = set(entries)
    for a in ATTR:
        if a in dict(S): continue
        ok = [v for v in ATTR[a] if consistent(S | {(a, v)})]
        if len(ok) == 1: S.add((a, ok[0]))
    return frozenset(S)
A = closure({('P', 'p'), ('R', 'r')}); print("A =", sorted(A))
def restrictions(blank):                              # closed restrictions of A in which every attribute in `blank` is blank
    out = set()
    for k in range(len(A) + 1):
        for S in combinations(sorted(A), k):
            S = frozenset(S)
            if closure(S) == S and not any(a in dict(S) for a in blank): out.add(S)
    return out
RANK = {'P': 2, 'R': 1, 'QX': 0, 'QY': 0}             # priorities: the generalization over the particular
def reopen(blank):
    rs = restrictions(blank); maxi = [S for S in rs if not any(S < T for T in rs)]
    best = max(maxi, key=lambda S: sorted((RANK[a] for a, _ in S), reverse=True))
    return maxi, best
def pockets(I, restated):                             # maximal consistent refinements (complete assignments) of I + restated
    base = set(I) | set(restated); d = dict(base)
    if len(d) < len(base): return []
    free = [a for a in ATTR if a not in d]
    return [frozenset(base | set(zip(free, vals))) for vals in product(*(ATTR[a] for a in free))
            if not any(inv <= (base | set(zip(free, vals))) for inv in INVALID)]
maxX, IX = reopen({'QX'}); maxXY, IXY = reopen({'QX', 'QY'})
print("maximal QX-blank restrictions:", [sorted(S) for S in maxX], "-> selected I_X =", sorted(IX))
print("maximal (QX,QY)-blank restrictions:", [sorted(S) for S in maxXY], "-> I_XY =", sorted(IXY))
print("nested (I_XY subset of I_X)?", IXY <= IX)
PX = pockets(IX, {('QX', 'x')}); PXY = pockets(IXY, {('QX', 'x'), ('QY', 'y')})
holds = lambda P, e: all(e in p for p in P) and len(P) > 0
print("X |~ Y :", holds(PX, ('QY', 'y')), "| X&Y |~ Z (Z = r):", holds(PXY, ('R', 'r')), "| X |~ Z :", holds(PX, ('R', 'r')), "| X |~ not-Z :", holds(PX, ('R', '-r')))
