# Does I = D survive broad agreeing states? Extension of the completed model: X2 also excludes a definite b, an
# irreducibility marker eX over X in {1,2}, and a record rX of X's value (holding X's carving). Two readings compared:
#   passive  -- a filling declares no children; only held carvings split (the author's reading of 2026-09-25)
#   peg-wise -- as passive, plus every multi-peg state splits peg by peg unless its attribute is held irreducibly
import itertools, sys, importlib.util
spec = importlib.util.spec_from_file_location('m', '/mnt/user-data/outputs/weight_algebra_model.py'); m = importlib.util.module_from_spec(spec); sys.argv = ['x']; spec.loader.exec_module(m)
S, PEGS = m.S, m.PEGS
m.BASE_SETS += [frozenset({S('X', 2), S('b', 0)}), frozenset({S('X', 2), S('b', 1)})]
m.BASE_SETS += [frozenset({('eX',), S('X', p)}) for p in PEGS['X']]
m.BASE_SETS += [frozenset({('eX',), S('X', 3)})]
def close_split(items, depth=0):
    c, tag = m.close(items)
    if tag or depth > 4: return c, tag
    for a in PEGS:
        if ('C', a) not in c or any(it[0] == 'S' and it[1] == a and len(it[2]) == 1 for it in c): continue
        live = [p for p in PEGS[a] if ('E', a, p) not in c]
        if live and all(close_split(set(c) | {S(a, p)}, depth + 1)[1] for p in live): return c, True
    return c, tag
carrier = lambda items: close_split(items)
prod = lambda A, B: (lambda r: (r[0], A[1] or B[1] or r[1]))(close_split(A[0] | B[0]))
join = lambda A, B: (lambda r: (r[0], r[1] and A[1] and B[1]))(close_split(A[0] & B[0]))
gens = [carrier(set())] + [carrier({S('X', p)}) for p in PEGS['X']] + [carrier({S('X', 1, 2)})] \
     + [carrier({S('b', v)}) for v in PEGS['b']] + [carrier({('e',)}), carrier({('C', 'b')}), carrier({('eX',)}), carrier({('rX',), ('C', 'X')})]
U = set(gens)
while True:
    new = set(U)
    for A, B in itertools.product(list(U), repeat=2): new.add(prod(A, B)); new.add(join(A, B))
    if new == U: break
    U = new
irr = {'b': ('e',), 'X': ('eX',)}
def children(c, pegwise):
    if c[1]: return []
    kids = []
    for a in PEGS:
        f = m.filling(c, a)
        if len(f) <= 1: continue
        carved = ('C', a) in c[0]
        multi = any(it[0] == 'S' and it[1] == a and len(it[2]) >= 2 for it in c[0])
        if carved or (pegwise and multi and irr[a] not in c[0]): kids += [prod(c, carrier({S(a, p)})) for p in sorted(f)]
    return kids
def analyse(pegwise):
    desc = {}
    for c in U:
        seen, st = {c}, [c]
        while st:
            x = st.pop()
            for k in children(x, pegwise):
                if k not in seen: seen.add(k); st.append(k)
        desc[c] = seen
    base = {c for c in U if c[1]}; D = set()
    while True:
        Dn = base | {A for A in U if all(any(C in D for C in desc[B]) for B in desc[A])}
        if Dn == D: break
        D = Dn
    I = {prod(A, B) for A in D for B in U}
    A = prod(carrier({S('X', 1, 2)}), carrier({('C', 'b')}))
    print(f"{'peg-wise' if pegwise else 'passive '}: |U|={len(U)} tagged={len(base)} |D|={len(D)} |I|={len(I)} I==D:{I == D} doomed-untagged={len(D - base)} |I\\D|={len(I - D)}")
    for lab, c in [("[X:{1,2}]·c_b (X filling, b definite)", A), ("[X:{1,2}]·c_b·c_X (X definite too)", prod(A, carrier({('C', 'X')}))),
                   ("[X:{1,2}]·c_b·eX (X irreducible)", prod(A, carrier({('eX',)}))), ("eX·rX (irreducible X, recorded)", prod(carrier({('eX',)}), carrier({('rX',), ('C', 'X')})))]:
        print(f"    {lab:42s} tagged={c[1]!s:5s} doomed={c in D!s:5s} in I={c in I}")
analyse(False); analyse(True)
