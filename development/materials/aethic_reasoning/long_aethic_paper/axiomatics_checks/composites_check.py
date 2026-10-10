# Option (b): composition rules (projection, combination, exclusion up/down) for K = X∧Y, and linkage rules for an
# attribute Xi whose pegs are Aethae, on the full rulebook (narrowing, propagation incl. mixed sets, elimination,
# invalidation, explosion, splitting over carvings incl. single-peg carvings, conceptually blank states asserting nothing).
import random, itertools, sys
fs = frozenset
BASE = {'X': ['x1','x2','x3'], 'Y': ['y1','y2'], 'W': ['w1','w2'], 'H': ['h1','h2'], 'E': ['e1','e2']}
ATTR = dict(BASE); ATTR['K'] = [f'k_{x}_{y}' for x in BASE['X'] for y in BASE['Y']]; ATTR['Xi'] = ['xi1', 'xi2']
EXT = {f'k_{x}_{y}': (x, y) for x in BASE['X'] for y in BASE['Y']}
carv = {}
for A in ['X', 'Y', 'W', 'H']:
    ATTR['K' + A] = ['k' + A, 'kb' + A]; carv[('K' + A, fs({'k' + A}))] = (A, [fs({p}) for p in BASE[A]])
OF = {p: a for a, ps in ATTR.items() for p in ps}
isblank = lambda s: isinstance(s, tuple) and s[1] == fs(ATTR[s[0]])
ALL = (fs((a, fs(c)) for a, ps in ATTR.items() for k in range(len(ps)) for c in itertools.combinations(ps, k)), fs(OF))
R1 = {('X', fs({'x1', 'x2'})), ('W', fs({'w1'}))}          # A_1: agreeing on X
R2 = {('X', fs({'x3'}))}                                   # A_2, disjoint from A_1
def make(D, links):
    memo = {}
    def cl(S, Ex=()):
        key = (fs(S), fs(Ex))
        if key in memo: return memo[key]
        C, E = {x for x in S if not isblank(x)}, set(Ex)
        while True:
            while True:
                new, newE, by = set(), set(), {}
                for a, F in C: by.setdefault(a, []).append(F)
                for a, Fs in by.items():
                    for F in Fs:
                        for G in Fs: new.add((a, F & G))
                held = {next(iter(F)) for a, F in C if len(F) == 1}
                h = lambda m: (m in C) if isinstance(m, tuple) else (m in held)
                for Dset in D:
                    for p in Dset:
                        if not isinstance(p, tuple) and all(h(q) for q in Dset if q != p): newE.add(p)
                    if any(isinstance(m, tuple) for m in Dset) and all(h(m) for m in Dset):
                        st = next(m for m in Dset if isinstance(m, tuple)); new.add((st[0], fs()))
                EE = E | newE
                for p in EE:
                    for F in by.get(OF[p], []): new.add((OF[p], F - {p}))
                for a, ps in ATTR.items():
                    for p in ps:
                        if all(q in EE for q in ps if q != p): new.add((a, fs({p})))
                # composition: projection, combination, exclusion up and down
                for F in by.get('K', []):
                    new.add(('X', fs(EXT[k][0] for k in F))); new.add(('Y', fs(EXT[k][1] for k in F)))
                for S in by.get('X', []):
                    for T in by.get('Y', []): new.add(('K', fs(f'k_{x}_{y}' for x in S for y in T)))
                for k, (x, y) in EXT.items():
                    if x in EE or y in EE: newE.add(k)
                for x in BASE['X']:
                    if all(k in EE for k, e in EXT.items() if e[0] == x): newE.add(x)
                for y in BASE['Y']:
                    if all(k in EE for k, e in EXT.items() if e[1] == y): newE.add(y)
                # linkage: a held peg licenses its Aethus's content; holding a representation licenses the peg
                for peg, (Ri, Ci) in links.items():
                    if ('Xi', fs({peg})) in C: new |= Ci[0]; newE |= Ci[1]
                    if Ri <= C: new.add(('Xi', fs({peg})))
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
                    bS, bE = (fs(C), fs(E)) if st in C else cl(C | {st}, E)
                    iS = bS if iS is None else iS & bS; iE = bE if iE is None else iE & bE
                iS = fs(x for x in iS if not isblank(x))
                if not (iS <= C and iE <= E): C |= iS; E |= iE; grew = True
            if not grew: break
        memo[key] = (fs(C), fs(E)); return memo[key]
    return cl
rng = random.Random(77)
f = dict(monotone=0, idem=0, meet=0, identity=0, dist_det=0, shadow=0, blank=0, thm_i=0, thm_ii=0, classical=0); n = dict(f)
for _ in range(2000):
    D = [fs(pr) for A in ATTR for pr in itertools.combinations(ATTR[A], 2)]
    for A in ['X', 'Y', 'W', 'H']:
        for p in BASE[A]: D.append(fs({p, 'kb' + A}))                      # determinate state entails its single-peg carving
    for _ in range(rng.randint(1, 4)):
        attrs = rng.sample(['X', 'Y', 'W', 'H'], rng.choice([2, 2, 3])); D.append(fs(rng.choice(BASE[a]) for a in attrs))
    if rng.random() < 0.5:
        S = fs(rng.sample(BASE['X'], rng.choice([2, 3])))
        for k in range(1, len(S)):
            for T in itertools.combinations(sorted(S), k): D.append(fs({'e1', ('X', fs(T))}))
    base_cl = make(D, {})
    links = {'xi1': (R1, base_cl(R1)), 'xi2': (R2, base_cl(R2))}
    cl = make(D, links)
    def rep(k=None, avoid=()):
        R = set()
        for _ in range(k if k is not None else rng.randint(1, 3)):
            a = rng.choice([x for x in ['X', 'Y', 'W', 'H', 'E', 'K'] if x not in avoid]); ps = ATTR[a]
            R.add((a, fs(rng.sample(ps, rng.randint(1, len(ps))))))
        return R
    R1r = rep(); R2r = R1r | rep(1); c1, c2 = cl(R1r), cl(R2r)
    f['monotone'] += not (c1[0] <= c2[0] and c1[1] <= c2[1]); f['idem'] += cl(c1[0], c1[1]) != c1
    RA, RB = rep(), rep(); cA, cB = cl(RA), cl(RB); f['meet'] += cl(RA | RB) != cl(cA[0] | cB[0], cA[1] | cB[1])
    for cst, (X, blocks) in carv.items():
        lhs = cl(R1r | {cst}); parts = [cl(R1r | {cst, (X, B)}) for B in blocks]
        f['identity'] += lhs != (fs.intersection(*[p[0] for p in parts]), fs.intersection(*[p[1] for p in parts]))
    A = rep(); cAA = cl(A); P = rng.sample(BASE['X'], rng.choice([2, 3]))
    cs = [cl({('X', fs({x}))}) for x in P]; U = (fs.intersection(*[c[0] for c in cs]), fs.intersection(*[c[1] for c in cs]))
    prods = [cl(cAA[0] | c[0], cAA[1] | c[1]) for c in cs]
    f['dist_det'] += cl(cAA[0] | U[0], cAA[1] | U[1]) != (fs.intersection(*[p[0] for p in prods]), fs.intersection(*[p[1] for p in prods]))
    b0 = rep(rng.randint(0, 2), avoid=('X', 'E', 'K')); cb = cl(b0)
    if cb != ALL and not any(a == 'X' for a, F in cb[0]):
        b1, b2 = cl(cb[0] | {('X', fs({'x1'}))}, cb[1]), cl(cb[0] | {('X', fs({'x2'}))}, cb[1])
        if b1 != ALL and b2 != ALL: n['shadow'] += 1; f['shadow'] += any(a == 'X' for a, F in (b1[0] & b2[0]))
    Xb = rng.choice(list(BASE)); f['blank'] += cl(R1r | {(Xb, fs(BASE[Xb]))}) != c1
    x, y = rng.choice(BASE['X']), rng.choice(BASE['Y']); Rw = rep(rng.randint(0, 2), avoid=('X', 'Y', 'K'))
    f['thm_i'] += cl(Rw | {('X', fs({x})), ('Y', fs({y}))}) != cl(Rw | {('K', fs({f'k_{x}_{y}'}))})
    i = rng.choice([1, 2]); Ri = R1 if i == 1 else R2
    f['thm_ii'] += cl(Rw | {('Xi', fs({f'xi{i}'}))}) != cl(Rw | Ri)
    Rd = {(a, fs({rng.choice(BASE[a])})) for a in rng.sample(['X', 'Y', 'W', 'H'], 2)}; cd = cl(Rd)    # classical collapse
    if cd != ALL: n['classical'] += 1; f['classical'] += any(len(F) >= 2 and a in ('X', 'Y', 'W', 'H', 'K') and not any(len(G) == 1 and G <= F for b, G in cd[0] if b == a) for a, F in cd[0])
print("option (b) on the full rulebook, 2000 random rulebooks:")
for k in f: print(f"  {k:<10} violations: {f[k]}" + (f" / {n[k]}" if n.get(k) else ""))
sys.exit(0 if all(v == 0 for v in f.values()) else 1)
