# The two-tier design: terms = closures WITHOUT explosion (empty filling = tag); sums = finite sets of terms
# (idempotent; meet distributes pairwise); core = common content (last common ancestor); rendering deletes invalid terms.
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
R1 = {('X', fs({'x1', 'x2'})), ('W', fs({'w1'}))}; R2 = {('X', fs({'x3'}))}
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
                for F in by.get('K', []):
                    new.add(('X', fs(EXT[k][0] for k in F))); new.add(('Y', fs(EXT[k][1] for k in F)))
                for S_ in by.get('X', []):
                    for T in by.get('Y', []): new.add(('K', fs(f'k_{x}_{y}' for x in S_ for y in T)))
                for k, (x, y) in EXT.items():
                    if x in EE or y in EE: newE.add(k)
                for x in BASE['X']:
                    if all(k in EE for k, e in EXT.items() if e[0] == x): newE.add(x)
                for y in BASE['Y']:
                    if all(k in EE for k, e in EXT.items() if e[1] == y): newE.add(y)
                for peg, (Ri, Ci) in links.items():
                    if ('Xi', fs({peg})) in C: new |= Ci[0]; newE |= Ci[1]
                    if Ri <= C: new.add(('Xi', fs({peg})))
                new = {x for x in new if not isblank(x)}
                if new <= C and newE <= E: break
                C |= new; E |= newE
            # NO explosion: an empty filling stays as a tag. Splitting ranges over ALL branches, invalid ones included.
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
invalid = lambda c: any(len(F) == 0 for a, F in c[0])
core = lambda terms: (fs.intersection(*[t[0] for t in terms]), fs.intersection(*[t[1] for t in terms]))
rng = random.Random(1789)
f = dict(monotone=0, idem=0, meet_indep=0, moore=0, enforced_core=0, thm2_i=0, thm2_ii=0, blank=0, classical=0, shadow=0,
         distinct_invalid=0, render_congruence=0, dist_sums=0, dist_core_first_tier=0, rendered_stronger=0)
info = dict(invalid_equal=0, rendered_strictly_stronger=0)
n = dict(f); dist_core_first_tier_fail = 0; dist_core_first_tier_n = 0
for _ in range(1500):
    D = [fs(pr) for A in ATTR for pr in itertools.combinations(ATTR[A], 2)]
    for A in ['X', 'Y', 'W', 'H']:
        for p in BASE[A]: D.append(fs({p, 'kb' + A}))
    for _ in range(rng.randint(1, 4)):
        attrs = rng.sample(['X', 'Y', 'W', 'H'], rng.choice([2, 2, 3])); D.append(fs(rng.choice(BASE[a]) for a in attrs))
    if rng.random() < 0.5:
        S = fs(rng.sample(BASE['X'], rng.choice([2, 3])))
        for k in range(1, len(S)):
            for T in itertools.combinations(sorted(S), k): D.append(fs({'e1', ('X', fs(T))}))
    base_cl = make(D, {}); cl = make(D, {'xi1': (R1, base_cl(R1)), 'xi2': (R2, base_cl(R2))})
    meet = lambda c, d: cl(c[0] | d[0], c[1] | d[1])
    def rep(k=None, avoid=()):
        R = set()
        for _ in range(k if k is not None else rng.randint(1, 3)):
            a = rng.choice([x for x in ['X', 'Y', 'W', 'H', 'E', 'K'] if x not in avoid]); ps = ATTR[a]
            R.add((a, fs(rng.sample(ps, rng.randint(1, len(ps))))))
        return R
    Ra = rep(); Rb = Ra | rep(1); ca, cb = cl(Ra), cl(Rb)
    f['monotone'] += not (ca[0] <= cb[0] and ca[1] <= cb[1]); f['idem'] += cl(ca[0], ca[1]) != ca
    RA, RB = rep(), rep(); cA, cB = cl(RA), cl(RB); f['meet_indep'] += cl(RA | RB) != meet(cA, cB)
    K_ = core([cA, cB]); f['moore'] += cl(K_[0], K_[1]) != K_
    for cst, (X, blocks) in carv.items():
        f['enforced_core'] += cl(Ra | {cst}) != core([cl(Ra | {cst, (X, B)}) for B in blocks])
    x, y = rng.choice(BASE['X']), rng.choice(BASE['Y']); Rw = rep(rng.randint(0, 2), avoid=('X', 'Y', 'K'))
    f['thm2_i'] += cl(Rw | {('X', fs({x})), ('Y', fs({y}))}) != cl(Rw | {('K', fs({f'k_{x}_{y}'}))})
    i = rng.choice([1, 2]); f['thm2_ii'] += cl(Rw | {('Xi', fs({f'xi{i}'}))}) != cl(Rw | (R1 if i == 1 else R2))
    Xb = rng.choice(list(BASE)); f['blank'] += cl(Ra | {(Xb, fs(BASE[Xb]))}) != ca
    Rd = {(a, fs({rng.choice(BASE[a])})) for a in rng.sample(['X', 'Y', 'W', 'H'], 2)}; cd = cl(Rd)
    if not invalid(cd):
        n['classical'] += 1; f['classical'] += any(len(F) >= 2 and a in BASE and not any(len(G) == 1 and G <= F for b, G in cd[0] if b == a) for a, F in cd[0])
    b0 = rep(rng.randint(0, 2), avoid=('X', 'E', 'K')); cb0 = cl(b0)
    if not invalid(cb0) and not any(a == 'X' for a, F in cb0[0]):
        b1, b2 = cl(cb0[0] | {('X', fs({'x1'}))}, cb0[1]), cl(cb0[0] | {('X', fs({'x2'}))}, cb0[1])
        if not invalid(b1) and not invalid(b2): n['shadow'] += 1; f['shadow'] += any(a == 'X' for a, F in core([b1, b2])[0])
    # distinctness of invalid Aethae: two different contradictions stay different terms
    i1, i2 = cl({('W', fs({'w1'})), ('W', fs({'w2'}))}), cl({('H', fs({'h1'})), ('H', fs({'h2'}))})
    if invalid(i1) and invalid(i2):
        n['distinct_invalid'] += 1; info['invalid_equal'] += i1 == i2
        f['distinct_invalid'] += (i1 == i2) and not ({('H', fs({'h1'})), ('H', fs({'h2'}))} <= i1[0] and {('W', fs({'w1'})), ('W', fs({'w2'}))} <= i2[0])
    # sums as sets of terms; rendering deletes invalid terms; check it is a congruence for + and pairwise meet
    xs = {cl(rep()) for _ in range(rng.randint(1, 3))}; ys = {cl(rep()) for _ in range(rng.randint(1, 3))}
    r = lambda s: {t for t in s if not invalid(t)}
    prod = lambda s, t: {meet(a, b) for a in s for b in t}
    f['render_congruence'] += (r(xs | ys) != r(xs) | r(ys)) or (r(prod(xs, ys)) != r(prod(r(xs), r(ys))))
    zs = {cl(rep()) for _ in range(rng.randint(1, 2))}
    f['dist_sums'] += prod(xs, ys | zs) != prod(xs, ys) | prod(xs, zs)
    # Prop 12's claim, meet over a sum of determinate alternatives, read on cores: first tier vs rendered
    A = cl(rep()); P = rng.sample(BASE['X'], rng.choice([2, 3])); Bs = [cl({('X', fs({p}))}) for p in P]
    lhs = meet(A, core(Bs)); prods = [meet(A, Bp) for Bp in Bs]
    dist_core_first_tier_n += 1; dist_core_first_tier_fail += lhs != core(prods)
    f['dist_core_first_tier'] += lhs != core(prods)
    valid_prods = [p for p in prods if not invalid(p)]
    if valid_prods:
        rc = core(valid_prods); n['rendered_stronger'] += 1
        f['rendered_stronger'] += not (core(prods)[0] <= rc[0] and core(prods)[1] <= rc[1]); info['rendered_strictly_stronger'] += rc != core(prods)
print("two-tier design (no explosion; sums keep terms; core = common content; rendering deletes invalid terms), 1500 rulebooks:")
for k in f: print(f"  {k:<20} violations: {f[k]}" + (f" / {n[k]}" if n.get(k) else ""))
print(f"  [info] distinct invalid pairs that were equal (each derives the other): {info['invalid_equal']}; rendered cores strictly stronger than first-tier cores (cases eliminated): {info['rendered_strictly_stronger']}")
sys.exit(0 if all(v == 0 for v in f.values()) else 1)
