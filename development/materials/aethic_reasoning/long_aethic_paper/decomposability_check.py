# The 2024 decomposability grades, read in the peg formalism: X1 = {a, b}, X2 = {c, d}, their composite K = X1 ^ X2,
# closure with the composition rule (projection, combination, exclusion transfer). Grades are read off fillings.
import itertools, random, collections
fs = frozenset
ATTR = {'X1': ['a', 'b'], 'X2': ['c', 'd'], 'Y': ['y1', 'y2']}
ATTR['K'] = [f'{x}{z}' for x in ATTR['X1'] for z in ATTR['X2']]
EXT = {f'{x}{z}': (x, z) for x in ATTR['X1'] for z in ATTR['X2']}
OF = {p: a for a, ps in ATTR.items() for p in ps}
def cl(R, D):
    C, E = set(R), set()
    while True:
        new, by = set(), {}
        for a, F in C: by.setdefault(a, []).append(F)
        for a, Fs in by.items():
            for F in Fs:
                for G in Fs: new.add((a, F & G))
        held = {next(iter(F)) for a, F in C if len(F) == 1}
        newE = {p for Dset in D for p in Dset if all(q in held for q in Dset if q != p)}
        EE = E | newE
        for p in EE:
            for F in by.get(OF[p], []): new.add((OF[p], F - {p}))
        for a, ps in ATTR.items():
            for p in ps:
                if all(q in EE for q in ps if q != p): new.add((a, fs({p})))
        for F in by.get('K', []): new.add(('X1', fs(EXT[k][0] for k in F))); new.add(('X2', fs(EXT[k][1] for k in F)))
        for S in by.get('X1', []):
            for T in by.get('X2', []): new.add(('K', fs(f'{x}{z}' for x in S for z in T)))
        for k, (x, z) in EXT.items():
            if x in EE or z in EE: newE.add(k)
        for x in ATTR['X1']:
            if all(k in EE for k, e in EXT.items() if e[0] == x): newE.add(x)
        for z in ATTR['X2']:
            if all(k in EE for k, e in EXT.items() if e[1] == z): newE.add(z)
        new = {s for s in new if s[1] != fs(ATTR[s[0]])}                       # conceptually blank states assert nothing
        if new <= C and newE <= E: return fs(C), fs(E)
        C |= new; E |= newE
def filling(c, a):
    F = fs(ATTR[a])
    for b, G in c[0]:
        if b == a: F &= G
    return F - c[1]
grade = lambda F, a: 'invalid' if not F else 'determinate' if len(F) == 1 else 'blank' if F == fs(ATTR[a]) else 'partial'
rng = random.Random(3); tally = collections.Counter(); viol = collections.Counter(); n = 0
for _ in range(4000):
    D = [fs(pr) for ps in ATTR.values() for pr in itertools.combinations(ps, 2)]
    for _ in range(rng.randint(0, 2)): D.append(fs({rng.choice(ATTR['Y']), rng.choice(ATTR['X1'] + ATTR['X2'])}))
    R = set()
    for _ in range(rng.randint(0, 3)):
        a = rng.choice(['X1', 'X2', 'K', 'Y']); R.add((a, fs(rng.sample(ATTR[a], rng.randint(1, len(ATTR[a]) - 1)))))
    c = cl(R, D)
    g1, g2, gk = grade(filling(c, 'X1'), 'X1'), grade(filling(c, 'X2'), 'X2'), grade(filling(c, 'K'), 'K')
    if 'invalid' in (g1, g2, gk): continue
    n += 1
    FK = filling(c, 'K')                                                          # R474: Proposition (i), the projection identity
    viol['component filling != projection of composite filling'] += (filling(c, 'X1') != fs(EXT[k][0] for k in FK)) + (filling(c, 'X2') != fs(EXT[k][1] for k in FK))
    comp = 'state' if g1 == g2 == 'determinate' else 'blank' if g1 == g2 == 'blank' else 'mixed' if {g1, g2} == {'determinate', 'blank'} else 'partial-component'
    tally[(comp, gk)] += 1
    viol['state-decomposable but composite not determinate'] += comp == 'state' and gk != 'determinate'
    viol['composite determinate but not state-decomposable'] += gk == 'determinate' and comp != 'state'
    viol['composite blank but a component not blank'] += gk == 'blank' and comp != 'blank'
    viol['mixed-decomposable but composite not partial'] += comp == 'mixed' and gk != 'partial'
    if comp == 'mixed':
        x = next(iter(filling(c, 'X1'))) if g1 == 'determinate' else None
        want = fs(k for k, e in EXT.items() if (x is None or e[0] == x) and (x is not None or e[1] == next(iter(filling(c, 'X2')))))
        viol['mixed composite not the product {x} x pegs'] += filling(c, 'K') != want
print(f"{n} valid Aethae over X1, X2 and K = X1^X2:")
for k, v in viol.items(): print(f"   {k:<52} violations: {v}")
print("   (component-wise class, composite grade) counts:", dict(sorted(tally.items())))
cor = cl({('K', fs({'ac', 'bd'}))}, [fs(pr) for ps in ATTR.values() for pr in itertools.combinations(ps, 2)])
print(f"\nCorrelation: R = {{[K:{{ac, bd}}]}} -> X1 {grade(filling(cor,'X1'),'X1')}, X2 {grade(filling(cor,'X2'),'X2')}, K {grade(filling(cor,'K'),'K')}"
      f"  (both components blank, composite partial: the 2024 rule 'all components blank => conceptually blank' misreads it)")
