# weight_algebra_model.py: the Weight Algebra's fully specified finite model (R507).
# Attributes: X with pegs {1,2,3}; b with pegs {0,1}; e: the irreducibility peg on b (b filled by exactly {0,1}).
# Items: states ('S', attr, frozenset pegs) for proper nonempty fillings; exclusions ('E', attr, peg); carvings ('C', attr);
# the irreducibility item ('e',). Closure: narrowing, exact fillings derive exclusions, elimination, semantic mining of the
# single-peg carving, and invalidation by the relation structure (a tag, licensing nothing further).
import itertools
PEGS = {'X': (1, 2, 3), 'b': (0, 1)}
BASE_SETS = [frozenset({('S', 'X', frozenset({1})), ('S', 'b', frozenset({0}))}),
             frozenset({('S', 'X', frozenset({1})), ('S', 'b', frozenset({1}))}),
             frozenset({('e',), ('S', 'b', frozenset({0}))}),
             frozenset({('e',), ('S', 'b', frozenset({1}))})]

def close(items):
    items = set(items); tag = False
    while True:
        new = set(items)
        for a in PEGS:
            sts = [it[2] for it in new if it[0] == 'S' and it[1] == a]
            exc = {it[2] for it in new if it[0] == 'E' and it[1] == a}
            if sts:
                f = frozenset.intersection(*sts) - exc
                if not f: tag = True; f = None
                if f is not None and len(f) < len(PEGS[a]): new.add(('S', a, f))
                for s in sts:
                    for p in PEGS[a]:
                        if p not in s: new.add(('E', a, p))
            live = [p for p in PEGS[a] if p not in {it[2] for it in new if it[0] == 'E' and it[1] == a}]
            if len(live) == 1: new.add(('S', a, frozenset(live)))
            if not live: tag = True
            if any(it[0] == 'S' and it[1] == a and len(it[2]) == 1 for it in new): new.add(('C', a))
        for bs in BASE_SETS:
            if bs <= new: tag = True
        if new == items: return frozenset(items), tag
        items = new

def carrier(items):
    c, t = close(items); return (c, t)
def prod(A, B):
    c, t = close(A[0] | B[0]); return (c, A[1] or B[1] or t)
def join(A, B):
    c, t = close(A[0] & B[0]); return (c, t and A[1] and B[1])

S = lambda a, *ps: ('S', a, frozenset(ps))
gens = [carrier(set())] + [carrier({S('X', p)}) for p in PEGS['X']] + [carrier({S('X', *q)}) for q in [(1, 2), (1, 3), (2, 3)]] \
     + [carrier({S('b', v)}) for v in PEGS['b']] + [carrier({('e',)})]
U = set(gens)
while True:
    new = set(U)
    for A, B in itertools.product(list(U), repeat=2):
        new.add(prod(A, B)); new.add(join(A, B))
    if new == U: break
    U = new
U = sorted(U, key=lambda c: (c[1], len(c[0]), sorted(map(str, c[0]))))

def filling(c, a):
    sts = [it[2] for it in c[0] if it[0] == 'S' and it[1] == a]; exc = {it[2] for it in c[0] if it[0] == 'E' and it[1] == a}
    f = frozenset(PEGS[a]) if not sts else frozenset.intersection(*sts)
    return f - exc
def children(c):
    if c[1]: return []
    kids = []
    for a in PEGS:
        f = filling(c, a)
        if len(f) <= 1: continue
        if a == 'b' and ('e',) in c[0]: continue             # irreducible agreeing superposition: no access, no declared split
        kids += [prod(c, carrier({S(a, p)})) for p in sorted(f)]  # exclusive blanks and broad agreeing states split peg by peg
    return kids
desc = {}
for c in U:
    seen, st = {c}, [c]
    while st:
        x = st.pop()
        for k in children(x):
            if k not in seen: seen.add(k); st.append(k)
    desc[c] = seen
base = {c for c in U if c[1]}
D = set()
while True:
    Dn = base | {A for A in U if all(any(C in D for C in desc[B]) for B in desc[A])}
    if Dn == D: break
    D = Dn
I = {prod(A, B) for A in D for B in U}
names = {}
def name(c):
    parts = []
    for a in PEGS:
        sts = sorted((it[2] for it in c[0] if it[0] == 'S' and it[1] == a), key=len)
        exc = sorted(it[2] for it in c[0] if it[0] == 'E' and it[1] == a)
        if sts: parts.append(f"{a}{''.join(map(str, sorted(sts[0])))}")
        elif exc: parts.append(f"{a}!{''.join(map(str, exc))}")
        if ('C', a) in c[0] and not (sts and len(sts[0]) == 1): parts.append(f"c{a}")
    if ('e',) in c[0]: parts.append('b*')
    return ('·'.join(parts) or 'blank') + (' [tag]' if c[1] else '')
if __name__ == '__main__':
    print(f"|U| = {len(U)}  (tagged: {len(base)})  |D| = {len(D)}  |I| = {len(I)}  |I \\ D| = {len(I - D)}")
    print("D, untagged members:", sorted(name(c) for c in D - base))
    print("I \\ D:", sorted(name(c) for c in I - D))
    X1, X2, X23, blank = carrier({S('X', 1)}), carrier({S('X', 2)}), carrier({S('X', 2, 3)}), carrier(set())
    j12 = join(X1, X2); j123 = join(join(X1, X2), carrier({S('X', 3)})); j1_23 = join(X1, X23)
    print("X1 + X2 =", name(j12), "| is blank:", j12 == blank, "| items:", sorted(map(str, j12[0])))
    print("X1 + X2 + X3 =", name(j123), "| is blank:", j123 == blank)
    print("X1 + X23 =", name(j1_23), "| is blank:", j1_23 == blank)
    ab = prod(X1, carrier({('e',)})); print("X1·b*:", name(ab), "| in D:", ab in D, "| in I:", ab in I, "| X1 in D:", X1 in D)
