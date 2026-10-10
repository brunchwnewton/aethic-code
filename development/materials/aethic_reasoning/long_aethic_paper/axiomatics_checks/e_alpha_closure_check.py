# Repair E + (alpha): closure as derivability with narrowing, propagation (records exclusions), elimination,
# invalidation (not exercised: peg-only declarations here), explosion, and SPLITTING over carvings.
import random, itertools
ATTR = {'X': ['x1','x2','x3'], 'Y': ['y1','y2','y3'], 'W': ['w1','w2'], 'H': ['h1','h2'], 'K': ['k1','k2'], 'L': ['l1','l2']}
OF = {p: a for a, ps in ATTR.items() for p in ps}
fs = frozenset
ALL = (fs((a, fs(c)) for a, ps in ATTR.items() for k in range(len(ps) + 1) for c in itertools.combinations(ps, k)), fs(OF))

def partition(rng, ps):
    ps = ps[:]; rng.shuffle(ps); blocks = []
    for p in ps:
        if blocks and rng.random() < 0.4: rng.choice(blocks).append(p)
        else: blocks.append([p])
    return [fs(b) for b in blocks]

def rulebook(rng):
    D = [fs(pr) for ps in ATTR.values() for pr in itertools.combinations(ps, 2)]
    for _ in range(rng.randint(2, 6)):
        attrs = rng.sample(list(ATTR), rng.choice([2, 2, 3])); D.append(fs(rng.choice(ATTR[a]) for a in attrs))
    carv = {}
    if rng.random() < 0.85: carv[('K', fs({'k1'}))] = ('X', partition(rng, ATTR['X']))   # [K:{k1}] carves X
    if rng.random() < 0.6:  carv[('L', fs({'l1'}))] = ('Y', partition(rng, ATTR['Y']))   # [L:{l1}] carves Y
    return D, carv

def rep(rng, n=None, avoid=()):
    R = set()
    for _ in range(n if n is not None else rng.randint(1, 3)):
        a = rng.choice([x for x in ATTR if x not in avoid]); ps = ATTR[a]
        R.add((a, fs(rng.sample(ps, rng.randint(1, len(ps))))))
    return R

def closure(S, Ex, D, carv, memo):
    key = (fs(S), fs(Ex))
    if key in memo: return memo[key]
    C, E = set(S), set(Ex)
    while True:
        while True:                                                   # local rules to a fixed point
            new, newE = set(), set(); by = {}
            for a, F in C: by.setdefault(a, []).append(F)
            for a, Fs in by.items():
                for F in Fs:
                    for G in Fs: new.add((a, F & G))                 # narrowing
            held = {next(iter(F)) for a, F in C if len(F) == 1}
            for Dset in D:
                for p in Dset:
                    if all(q in held for q in Dset if q != p): newE.add(p)   # propagation records the exclusion
            for p in E | newE:
                for F in by.get(OF[p], []): new.add((OF[p], F - {p}))       # ... and narrows present states
            for a, ps in ATTR.items():
                for p in ps:
                    if all(q in (E | newE) for q in ps if q != p): new.add((a, fs({p})))   # elimination
            if new <= C and newE <= E: break
            C |= new; E |= newE
        if any(len(F) == 0 for a, F in C):                           # explosion: the one invalid Aethus
            memo[key] = ALL; return ALL
        grew = False
        for cst, (X, blocks) in carv.items():                         # splitting
            if cst not in C: continue
            iS = iE = None
            for B in blocks:
                st = (X, B)
                bS, bE = (fs(C), fs(E)) if st in C else closure(C | {st}, E, D, carv, memo)
                iS = bS if iS is None else iS & bS; iE = bE if iE is None else iE & bE
            if not (iS <= C and iE <= E): C |= iS; E |= iE; grew = True
        if not grew: break
    memo[key] = (fs(C), fs(E)); return memo[key]

rng = random.Random(924)
N = 3000
f = dict(monotone=0, idempotent=0, meet=0, identity=0, nonweakening=0, f1_q=0, f1_u=0, shadow_q=0, shadow_u=0)
n_id = n_f1q = n_f1u = n_shq = n_shu = 0
for _ in range(N):
    D, carv = rulebook(rng); memo = {}
    cl = lambda R, Ex=(): closure(set(R), set(Ex), D, carv, memo)
    R1 = rep(rng); R2 = R1 | rep(rng, 1); RA = rep(rng); RB = rep(rng)
    c1, c2 = cl(R1), cl(R2)
    if not (c1[0] <= c2[0] and c1[1] <= c2[1]): f['monotone'] += 1
    if cl(c1[0], c1[1]) != c1: f['idempotent'] += 1
    cA, cB = cl(RA), cl(RB)
    if cl(RA | RB) != cl(cA[0] | cB[0], cA[1] | cB[1]): f['meet'] += 1
    for cst, (X, blocks) in carv.items():                            # the enforced identity
        n_id += 1
        lhs = cl(R1 | {cst}); parts = [cl(R1 | {cst, (X, B)}) for B in blocks]
        rhs = (fs.intersection(*[p[0] for p in parts]), fs.intersection(*[p[1] for p in parts]))
        if lhs != rhs: f['identity'] += 1
    if c1 != ALL:                                                     # non-weakening, as the new Prop. 4 states it
        for a, F in c1[0]:
            if len(F) >= 2 and not (any(b == a and F <= G for b, G in R1) or
                                    any(X == a and any(F <= B for B in bl) for X, bl in carv.values())):
                f['nonweakening'] += 1; break
    multi_X = any(X == 'X' and any(len(B) >= 2 for B in bl) for X, bl in carv.values())
    other = rep(rng, rng.randint(0, 2), avoid=('X',))
    cw = cl(other | {('X', fs({'x1'}))})
    if cw != ALL:                                                     # F1 proof, with and without the new qualifier
        bad = any(a == 'X' and not F <= {'x1'} for a, F in cw[0])
        if multi_X: n_f1u += 1; f['f1_u'] += bad
        else: n_f1q += 1; f['f1_q'] += bad
    base = rep(rng, rng.randint(0, 2), avoid=('X',)); cb = cl(base)  # the 3.3 shadow claim
    if cb != ALL and not any(a == 'X' for a, F in cb[0]):
        b1, b2 = cl(cb[0] | {('X', fs({'x1'}))}, cb[1]), cl(cb[0] | {('X', fs({'x2'}))}, cb[1])
        if b1 != ALL and b2 != ALL:
            bad = any(a == 'X' for a, F in (b1[0] & b2[0]))
            if multi_X: n_shu += 1; f['shadow_u'] += bad
            else: n_shq += 1; f['shadow_q'] += bad
print(f"{N} random rulebooks with carvings; enforced identity tested {n_id} times\n")
rows = [('Cl monotone', 'monotone'), ('Cl idempotent', 'idempotent'), ('meet independent of representations', 'meet'),
        ('enforced identity [R+c] = sum_j [R+c+c_j]', 'identity'),
        ('non-weakening: agreeing states narrow an asserted state or a setting', 'nonweakening')]
for lab, k in rows: print(f"  {lab:<72} violations: {f[k]}")
print(f"  {'F1 proof, no carving of X with a block of 2+ pegs (' + str(n_f1q) + ' cases)':<72} violations: {f['f1_q']}")
print(f"  {'F1 proof, some carving of X with a block of 2+ pegs (' + str(n_f1u) + ' cases)':<72} violations: {f['f1_u']}")
print(f"  {'3.3 shadow, no carving of X with a block of 2+ pegs (' + str(n_shq) + ' cases)':<72} violations: {f['shadow_q']}")
print(f"  {'3.3 shadow, some carving of X with a block of 2+ pegs (' + str(n_shu) + ' cases)':<72} violations: {f['shadow_u']}")
