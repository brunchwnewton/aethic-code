# F10, the author's instinct: does the union of determinate Aethae carry "X holds a single peg"?
# Variant 0: no carvings entailed.  Variant 1: every determinate [A:{a}] entails A's single-peg carving (semantic mining).
# Variant 2 (over-reach test): additionally, every state within a block entails that block's carving, for all 2|1 partitions of X.
# Irreducibility is included: E={e1,e2}, with declarations {e1, [X:T]} for nonempty T strictly inside S (|S|>=2).
import random, itertools
fs = frozenset
BASE = {'X': ['x1','x2','x3'], 'Y': ['y1','y2','y3'], 'W': ['w1','w2'], 'H': ['h1','h2'], 'E': ['e1','e2']}

def build(variant):
    ATTR = dict(BASE); carv = {}; D_extra = []
    if variant >= 1:
        for A in ['X', 'Y', 'W', 'H']:
            ka = 'K' + A; ATTR[ka] = ['k_' + A, 'kb_' + A]
            carv[(ka, fs({'k_' + A}))] = (A, [fs({p}) for p in BASE[A]])
            for p in BASE[A]: D_extra.append(fs({p, 'kb_' + A}))           # determinate [A:{p}] excludes "not single-pegged"
    if variant == 2:
        for i, c in enumerate(BASE['X']):
            rest = [q for q in BASE['X'] if q != c]; pa = 'P' + str(i); ATTR[pa] = ['p_' + str(i), 'pb_' + str(i)]
            blocks = [fs(rest), fs({c})]
            carv[(pa, fs({'p_' + str(i)}))] = ('X', blocks)
            for B in blocks:
                for k in range(1, len(B) + 1):
                    for T in itertools.combinations(sorted(B), k):
                        D_extra.append(fs({('X', fs(T)), 'pb_' + str(i)}))   # a state within a block entails that carving
    OF = {p: a for a, ps in ATTR.items() for p in ps}
    ALL = (fs((a, fs(c)) for a, ps in ATTR.items() for k in range(len(ps)) for c in itertools.combinations(ps, k)), fs(OF))
    return ATTR, OF, ALL, carv, D_extra

def make_closure(ATTR, OF, ALL, carv, D):
    memo = {}
    def is_state(m): return isinstance(m, tuple)
    def isblank(x): return isinstance(x, tuple) and x[1] == fs(ATTR[x[0]])
    def closure(S, Ex):
        key = (fs(S), fs(Ex))
        if key in memo: return memo[key]
        C, E = {x for x in S if not isblank(x)}, set(Ex)
        while True:
            while True:
                new, newE = set(), set(); by = {}
                for a, F in C: by.setdefault(a, []).append(F)
                for a, Fs in by.items():
                    for F in Fs:
                        for G in Fs: new.add((a, F & G))
                held = {next(iter(F)) for a, F in C if len(F) == 1}
                h = lambda m: (m in C) if is_state(m) else (m in held)
                for Dset in D:
                    for p in Dset:
                        if not is_state(p) and all(h(q) for q in Dset if q != p): newE.add(p)
                    if any(is_state(m) for m in Dset) and all(h(m) for m in Dset):
                        st = next(m for m in Dset if is_state(m)); new.add((st[0], fs()))      # invalidation
                for p in E | newE:
                    for F in by.get(OF[p], []): new.add((OF[p], F - {p}))
                for a, ps in ATTR.items():
                    for p in ps:
                        if all(q in (E | newE) for q in ps if q != p): new.add((a, fs({p})))
                new = {x for x in new if not isblank(x)}
                if new <= C and newE <= E: break
                C |= new; E |= newE
            if any(len(F) == 0 for a, F in C): memo[key] = ALL; return ALL
            grew = False
            for cst, (X, blocks) in carv.items():
                if cst not in C: continue
                iS = iE = None
                for B in blocks:
                    st = (X, B)
                    bS, bE = (fs(C), fs(E)) if st in C else closure(C | {st}, E)
                    iS = bS if iS is None else iS & bS; iE = bE if iE is None else iE & bE
                iS = fs(x for x in iS if not isblank(x))
                if not (iS <= C and iE <= E): C |= iS; E |= iE; grew = True
            if not grew: break
        memo[key] = (fs(C), fs(E)); return memo[key]
    return closure

def run(variant, N=1500, seed=10):
    rng = random.Random(seed)
    f = dict(monotone=0, idem=0, meet=0, identity=0, dist_det=0, dist_agree=0, shadow=0); n = dict(dist_det=0, dist_agree=0, shadow=0, identity=0)
    for _ in range(N):
        ATTR, OF, ALL, carv, Dx = build(variant)
        D = [fs(pr) for A in BASE for pr in itertools.combinations(BASE[A], 2)] + Dx
        for _ in range(rng.randint(1, 4)):
            attrs = rng.sample(['X', 'Y', 'W', 'H'], rng.choice([2, 2, 3])); D.append(fs(rng.choice(BASE[a]) for a in attrs))
        S_irr = None
        if rng.random() < 0.6:                                             # irreducibility over S
            S_irr = fs(rng.sample(BASE['X'], rng.choice([2, 3])))
            for k in range(1, len(S_irr)):
                for T in itertools.combinations(sorted(S_irr), k): D.append(fs({'e1', ('X', fs(T))}))
        cl0 = make_closure(ATTR, OF, ALL, carv, D)
        cl = lambda R, Ex=(): cl0(set(R), set(Ex))
        def rep(k=None, avoid=()):
            R = set()
            for _ in range(k if k is not None else rng.randint(1, 3)):
                a = rng.choice([x for x in BASE if x not in avoid]); ps = BASE[a]; R.add((a, fs(rng.sample(ps, rng.randint(1, len(ps))))))
            if S_irr and rng.random() < 0.5: R |= {('E', fs({'e1'})), ('X', S_irr)}   # an irreducible superposition
            return R
        R1 = rep(); R2 = R1 | rep(1); c1, c2 = cl(R1), cl(R2)
        f['monotone'] += not (c1[0] <= c2[0] and c1[1] <= c2[1]); f['idem'] += cl(c1[0], c1[1]) != c1
        RA, RB = rep(), rep(); cA, cB = cl(RA), cl(RB)
        f['meet'] += cl(RA | RB) != cl(cA[0] | cB[0], cA[1] | cB[1])
        for cst, (X, blocks) in carv.items():
            n['identity'] += 1; lhs = cl(R1 | {cst}); parts = [cl(R1 | {cst, (X, B)}) for B in blocks]
            f['identity'] += lhs != (fs.intersection(*[p[0] for p in parts]), fs.intersection(*[p[1] for p in parts]))
        Xb = rng.choice(list(BASE)); f['blank_identity'] = f.get('blank_identity', 0) + (cl(R1 | {(Xb, fs(BASE[Xb]))}) != c1); n['blank_identity'] = n.get('blank_identity', 0) + 1
        A = rep(); cAA = cl(A)
        def dist(opnds):                                                    # A . (sum B) == sum (A . B) ?
            cs = [cl(o) for o in opnds]
            U = (fs.intersection(*[c[0] for c in cs]), fs.intersection(*[c[1] for c in cs]))
            lhs = cl(cAA[0] | U[0], cAA[1] | U[1])
            prods = [cl(cAA[0] | c[0], cAA[1] | c[1]) for c in cs]
            return lhs == (fs.intersection(*[p[0] for p in prods]), fs.intersection(*[p[1] for p in prods]))
        P = rng.sample(BASE['X'], rng.choice([2, 3]))
        n['dist_det'] += 1; f['dist_det'] += not dist([{('X', fs({x}))} for x in P])
        blk = rng.choice([(fs({'x1','x2'}), fs({'x3'})), (fs({'x1','x3'}), fs({'x2'})), (fs({'x2','x3'}), fs({'x1'}))])
        n['dist_agree'] += 1; f['dist_agree'] += not dist([{('X', blk[0])}, {('X', blk[1])}])
        base = rep(rng.randint(0, 2), avoid=('X', 'E')); cb = cl(base)
        if cb != ALL and not any(a == 'X' for a, F in cb[0]):
            b1, b2 = cl(cb[0] | {('X', fs({'x1'}))}, cb[1]), cl(cb[0] | {('X', fs({'x2'}))}, cb[1])
            if b1 != ALL and b2 != ALL:
                n['shadow'] += 1; f['shadow'] += any(a == 'X' for a, F in (b1[0] & b2[0]))
    return f, n

f, n = run(1)
print("rulebook: single-peg carvings, irreducibility, and conceptually blank states asserting nothing (F12)")
for k in ['monotone', 'idem', 'meet', 'identity', 'dist_det', 'shadow', 'blank_identity']:
    print(f"  {k:<16} violations: {f.get(k, 0)}" + (f" / {n[k]}" if k in n else ""))
import sys; sys.exit(0 if all(f.get(k, 0) == 0 for k in ['monotone', 'idem', 'meet', 'identity', 'dist_det', 'shadow', 'blank_identity']) else 1)
