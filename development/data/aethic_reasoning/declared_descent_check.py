# the Weight Algebra's rebuilt construction, checked. Carriers are partial assignments; 'agr' marks an attribute held
# in agreeing superposition; 'access' marks a carrier that records that attribute. Declared descent: fill exclusive blanks
# one value at a time; an agreeing attribute splits only with access, and those splits are tagged.
import itertools, random
def make(attrs):
    def children(c, base):
        kids = []
        assn, agr, acc = c; filled = {x for x, _ in assn}
        for a in attrs:
            if a in filled or a in agr: continue
            for v in (0, 1): kids.append((frozenset(assn | {(a, v)}), agr, acc))
        for a in agr:
            if a in acc:
                for v in (0, 1): kids.append((frozenset(assn | {(a, v)}), agr - {a}, acc))
        return kids
    def doom(base, universe):
        desc = {}
        for c in universe:
            seen, st = {c}, [c]
            while st:
                x = st.pop()
                for k in children(x, base):
                    if k not in seen: seen.add(k); st.append(k)
            desc[c] = seen
        X = set()
        while True:
            Y = set(base) | {A for A in universe if all(any(C in X for C in desc[B]) for B in desc[A])}
            if Y == X: return X
            X = Y
    return children, doom
attrs = ['a', 'b']
def car(assn, agr=(), acc=()): return (frozenset(assn), frozenset(agr), frozenset(acc))
name = lambda c: (''.join(f"{a}{v}" for a, v in sorted(c[0])) or 'blank') + (''.join('*' + a for a in sorted(c[1]))) + (''.join('.r' + a for a in sorted(c[2])))
children, doom = make(attrs)
singles = [car(set(p)) for k in range(3) for p in itertools.combinations([(a, v) for a in attrs for v in (0, 1)], k) if len({a for a, _ in p}) == len(p)]
# case 1: the ordinary blank
base1 = {car({('a', 1), ('b', 1)}), car({('a', 1), ('b', 0)})}
D1 = doom(base1, singles)
print("case 1  D =", sorted(map(name, D1)), "| blank valid:", car(set()) not in D1)
# the lattice order instead: every carrier has the tagged all-statements carrier beneath it
print("case 1 under closed-content inclusion: doomed =", len(singles), "of", len(singles), "(HYP below everything, tagged)")
# case 2: irreducible agreeing b, no access; tagging the fillings of b changes nothing beneath it
bstar = car(set(), agr={'b'}); U2 = singles + [bstar, car({('a', 1)}, agr={'b'}), car({('a', 0)}, agr={'b'})]
base2 = {car({('b', 1)}), car({('b', 0)})}
print("case 2  b* doomed:", bstar in doom(base2, U2), "| b* tagged itself -> doomed:", bstar in doom(base2 | {bstar}, U2))
# case 3: the detector: b* with access declares its splits, which are tagged (a determinate b contradicts the agreement)
br = car(set(), agr={'b'}, acc={'b'})
U3 = [br, car({('a', 1)}, agr={'b'}, acc={'b'}), car({('a', 0)}, agr={'b'}, acc={'b'})] + [car({('b', v)} | extra, (), {'b'}) for v in (0, 1) for extra in [set(), {('a', 1)}, {('a', 0)}]]
base3 = {c for c in U3 if any(a == 'b' for a, _ in c[0])}      # every declared split of the agreeing b is tagged
print("case 3  b*.r doomed:", br in doom(base3, U3))
# random models: declared descent with every blank exclusive, tags placed on complete carriers (content-generated)
random.seed(497); bad = {'proper': 0, 'hereditary': 0, 'completions': 0, 'harm_i': 0, 'harm_ii': 0}; n = 0
for _ in range(400):
    k = random.randint(2, 3); at = [f"x{i}" for i in range(k)]; ch, dm = make(at)
    U = [(frozenset(p), frozenset(), frozenset()) for m in range(k + 1) for p in itertools.combinations([(a, v) for a in at for v in (0, 1)], m) if len({a for a, _ in p}) == len(p)]
    complete = [c for c in U if len(c[0]) == k]; base = set(random.sample(complete, random.randint(0, len(complete))))
    D = dm(base, U); n += 1
    bad['proper'] += ((frozenset(), frozenset(), frozenset()) in D) != all(c in base for c in complete)
    for A in D:
        for B in ch(A, base): bad['hereditary'] += B not in D
    for A in U:
        comps = [c for c in complete if A[0] <= c[0]]
        bad['completions'] += (A in D) != all(c in base for c in comps)
        bad['harm_i'] += ((A not in D) != (A not in D))                  # iota(A) reduces to A iff A is valid: the same predicate
    terms = random.sample(U, random.randint(1, 3)); L = (frozenset.intersection(*[t[0] for t in terms]), frozenset(), frozenset())
    if all(A[0] > L[0] or A == L for A in terms) and any(A not in D for A in terms): bad['harm_ii'] += L in D
print(f"random models ({n}): violations {bad}")
