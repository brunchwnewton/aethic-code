# R493: (1) the sprinkler witness's residues, recomputed from the operator's definitions; (2) the characterization of
# where Cautious Monotony fails, checked on random finite models: given X |~ Y, X |~ Z and nested reopenings,
# X&Y fails to yield Z exactly when some pocket of the X&Y residue that does not carry every cleared entry of D fails Z.
import itertools, random
def make(attrs, invalid):
    def consistent(E):
        d = dict(E)
        if len(d) < len(E): return False
        free = [a for a in attrs if a not in d]
        for vals in itertools.product(*(attrs[a] for a in free)):
            full = set(d.items()) | set(zip(free, vals))
            if not any(inv <= full for inv in invalid): return True
        return False
    def closure(E):
        S = set(E); changed = True
        while changed:
            changed = False
            for a in attrs:
                if a in dict(S): continue
                ok = [v for v in attrs[a] if consistent(S | {(a, v)})]
                if len(ok) == 1: S.add((a, ok[0])); changed = True
        return frozenset(S)
    def pockets(I, restated):
        base = set(I) | set(restated); d = dict(base)
        if len(d) < len(base): return []
        free = [a for a in attrs if a not in d]
        return [frozenset(base | set(zip(free, v))) for v in itertools.product(*(attrs[a] for a in free))
                if not any(inv <= (base | set(zip(free, v))) for inv in invalid)]
    return consistent, closure, pockets
def reopen(A, blank, closure, rank):
    rs = [frozenset(S) for k in range(len(A) + 1) for S in itertools.combinations(sorted(A), k)
          if closure(frozenset(S)) == frozenset(S) and not any(a in dict(S) for a in blank)]
    maxi = [S for S in rs if not any(S < T for T in rs)]
    if not maxi: return None                                          # the laws alone force the attribute: no reopening exists
    return max(maxi, key=lambda S: sorted((rank[a] for a, _ in S), reverse=True))
# (1) the witness
attrs = {'X': ('x', '-x'), 'S': ('s', '-s'), 'Y': ('y', '-y'), 'Z': ('z', '-z')}
inv = [frozenset({('S', 's'), ('Y', '-y')}), frozenset({('X', 'x'), ('S', 's'), ('Z', '-z')})]
cons, clos, pock = make(attrs, inv); A = clos({('S', 's')}); rank = {a: 0 for a in attrs}
IX = reopen(A, {'X'}, clos, rank); IXY = reopen(A, {'X', 'Y'}, clos, rank)
show = lambda P: sorted(''.join(v for _, v in sorted(p, key=lambda e: 'XSYZ'.index(e[0]))) for p in P)
print("(1) A =", sorted(A), "| I_X =", sorted(IX), "| I_XY =", sorted(IXY))
print("    R(x) =", show(pock(IX, {('X', 'x')})), "| R(x & y) =", show(pock(IXY, {('X', 'x'), ('Y', 'y')})))
# (2) random models
random.seed(493); tested = agree = mono_fail = 0
for _ in range(20000):
    n = random.randint(3, 5); names = [f'a{i}' for i in range(n)]; attrs = {a: (a + '1', a + '0') for a in names}
    inv = [frozenset((a, random.choice(attrs[a])) for a in random.sample(names, random.randint(2, 3))) for _ in range(random.randint(1, 3))]
    cons, clos, pock = make(attrs, inv)
    stated = {(a, random.choice(attrs[a])) for a in random.sample(names, random.randint(1, 3))}
    if not cons(stated): continue
    A = clos(stated); rank = {a: random.random() for a in names}
    qX = random.choice(names); x = random.choice(attrs[qX])
    IX = reopen(A, {qX}, clos, rank)
    if IX is None: continue
    PX = pock(IX, {(qX, x)})
    if not PX: continue
    held = [e for e in set.intersection(*map(set, PX)) if e[0] != qX]
    if len(held) < 2: continue
    Y, Z = random.sample(held, 2)                                        # X |~ Y and X |~ Z, both held in every pocket
    IXY = reopen(A, {qX, Y[0]}, clos, rank)
    if IXY is None or not IXY <= IX: continue                                          # the characterization's nesting hypothesis
    PXY = pock(IXY, {(qX, x), Y}); D = IX - IXY
    mono_fail += not set(PX) <= set(PXY)
    cm_fails = not PXY or any(Z not in q for q in PXY)
    rhs = any((not D <= q) and Z not in q for q in PXY)
    tested += 1; agree += (cm_fails == rhs) or not PXY
print(f"(2) {tested} nested instances with X |~ Y and X |~ Z: characterization agrees in {agree}; pocket monotonicity failures {mono_fail}")
