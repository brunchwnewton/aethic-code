# weight_algebra_model_stated.py: option (iii) -- exclusivity must be stated (the single-peg carving held); closure runs the splitting rule. Result on the completed model: every doomed carrier is tagged by closure, the doomed set is an ideal, I = D.
# Option (iii): a blank splits only where its exclusivity is stated (its single-peg carving held), and closure runs the
# splitting rule over held carvings (a carrier is tagged when every setting of a held carving is tagged).
import itertools, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location('m', __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'weight_algebra_model.py')); m = importlib.util.module_from_spec(spec); sys.argv = ['x']; spec.loader.exec_module(m)
PEGS, BASE_SETS, S = m.PEGS, m.BASE_SETS, m.S
def close_split(items, depth=0):
    c, tag = m.close(items)
    if tag or depth > 3: return c, tag
    for a in PEGS:
        if ('C', a) not in c: continue
        live = [p for p in PEGS[a] if ('E', a, p) not in c]
        if any(it[0] == 'S' and it[1] == a and len(it[2]) == 1 for it in c): continue
        if live and all(close_split(set(c) | {S(a, p)}, depth + 1)[1] for p in live):
            return c, True                       # every setting of the held carving is tagged: splitting licenses the tag
    return c, tag
carrier = lambda items: close_split(items)
prod = lambda A, B: (lambda r: (r[0], A[1] or B[1] or r[1]))(close_split(A[0] | B[0]))
join = lambda A, B: (lambda r: (r[0], r[1] and A[1] and B[1]))(close_split(A[0] & B[0]))
gens = [carrier(set())] + [carrier({S('X', p)}) for p in PEGS['X']] + [carrier({S('X', *q)}) for q in [(1, 2), (1, 3), (2, 3)]] \
     + [carrier({S('b', v)}) for v in PEGS['b']] + [carrier({('e',)})] + [carrier({('C', 'b')})]
U = set(gens)
while True:
    new = set(U)
    for A, B in itertools.product(list(U), repeat=2): new.add(prod(A, B)); new.add(join(A, B))
    if new == U: break
    U = new
def children(c):
    if c[1]: return []
    kids = []
    for a in PEGS:
        f = m.filling(c, a)
        if len(f) <= 1: continue
        if a == 'b' and ('e',) in c[0]: continue
        stated_exclusive = ('C', a) in c[0]
        broad_agreeing = any(it[0] == 'S' and it[1] == a and len(it[2]) >= 2 for it in c[0])
        if stated_exclusive: kids += [prod(c, carrier({S(a, p)})) for p in sorted(f)]   # fillings are passive: only a held carving splits
    return kids
desc = {}
for c in U:
    seen, st = {c}, [c]
    while st:
        x = st.pop()
        for k in children(x):
            if k not in seen: seen.add(k); st.append(k)
    desc[c] = seen
base = {c for c in U if c[1]}; D = set()
while True:
    Dn = base | {A for A in U if all(any(C in D for C in desc[B]) for B in desc[A])}
    if Dn == D: break
    D = Dn
I = {prod(A, B) for A in D for B in U}
X1 = carrier({S('X', 1)}); X1cb = prod(X1, carrier({('C', 'b')})); X1e = prod(X1, carrier({('e',)}))
print(f"|U| = {len(U)}  tagged {len(base)}  |D| = {len(D)}  |I| = {len(I)}  I == D: {I == D}  |D \\ tagged| = {len(D - base)}")
print("X1 (b unstated):   tagged", X1[1], "| doomed", X1 in D)
print("X1·c_b (b single): tagged", X1cb[1], "| doomed", X1cb in D)
print("X1·b*  (b agree):  tagged", X1e[1], "| doomed", X1e in D, "| in I", X1e in I)
print("products of doomed carriers that are not doomed:", len(I - D))
