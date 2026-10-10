# Aethus--Peg Equivalence, determinate case, on the paper's closure (narrowing, propagation incl. mixed sets,
# elimination, invalidation, explosion). (i) composite: [X:{x}],[Y:{y}] ~ [K:{(x,y)}]. (ii) Aethic attribute: [Xi:{xi_i}] ~ R_i.
import random, itertools
fs = frozenset
ATTR = {'X': ['x1','x2','x3'], 'Y': ['y1','y2'], 'W': ['w1','w2'], 'H': ['h1','h2'], 'Xi': ['xi1','xi2']}
ATTR['K'] = [f'k_{x}_{y}' for x in ATTR['X'] for y in ATTR['Y']]
OF = {p: a for a, ps in ATTR.items() for p in ps}
EXT = {f'k_{x}_{y}': {x, y} for x in ATTR['X'] for y in ATTR['Y']}          # which component pegs a joint peg extends
ALL = (fs((a, fs(c)) for a, ps in ATTR.items() for k in range(len(ps)) for c in itertools.combinations(ps, k)) | fs((a, fs()) for a in ATTR), fs(OF))
def closure(S, D):
    C, E = set(S), set()
    while True:
        new, newE, by = set(), set(), {}
        for a, F in C: by.setdefault(a, []).append(F)
        for a, Fs in by.items():
            for F in Fs:
                for G in Fs: new.add((a, F & G))
        held = {next(iter(F)) for a, F in C if len(F) == 1}
        for Dset in D:
            for p in Dset:
                if all(q in held for q in Dset if q != p): newE.add(p)
        for p in E | newE:
            for F in by.get(OF[p], []): new.add((OF[p], F - {p}))
        for a, ps in ATTR.items():
            for p in ps:
                if all(q in (E | newE) for q in ps if q != p): new.add((a, fs({p})))
        if new <= C and newE <= E: break
        C |= new; E |= newE
    return ALL if any(len(F) == 0 for a, F in C) else (fs(C), fs(E))
base = [fs(pr) for ps in ATTR.values() for pr in itertools.combinations(ps, 2)]
composite = [fs({x, k}) for k, ext in EXT.items() for x in ATTR['X'] + ATTR['Y'] if x not in ext]   # peg vs non-extending joint peg
R1, R2 = [('X', 'x1'), ('W', 'w1')], [('X', 'x2')]                                                  # A_1, A_2 disjoint (x1 vs x2)
def ties(Ri, xi, others):
    t = [fs({xi, q}) for a, p in Ri for q in ATTR[a] if q != p]                                      # xi_i excludes what R_i excludes
    t += [fs({p for a, p in Ri} | {o}) for o in others]                                              # R_i's pegs together exclude other xi
    return t
tie = ties(R1, 'xi1', ['xi2']) + ties(R2, 'xi2', ['xi1'])
rng = random.Random(5); bad_i = bad_ii = n = 0
for _ in range(3000):
    D = base + composite + tie
    for _ in range(rng.randint(0, 4)):
        attrs = rng.sample(['X', 'Y', 'W', 'H'], rng.choice([2, 2, 3])); D.append(fs(rng.choice(ATTR[a]) for a in attrs))
    R = set()
    for _ in range(rng.randint(0, 2)):
        a = rng.choice(['W', 'H']); R.add((a, fs(rng.sample(ATTR[a], rng.randint(1, 2)))))
    x, y = rng.choice(ATTR['X']), rng.choice(ATTR['Y'])
    bad_i += closure(R | {('X', fs({x})), ('Y', fs({y}))}, D) != closure(R | {('K', fs({f'k_{x}_{y}'}))}, D)
    i = rng.choice([1, 2]); Ri = R1 if i == 1 else R2
    bad_ii += closure(R | {('Xi', fs({f'xi{i}'}))}, D) != closure(R | {(a, fs({p})) for a, p in Ri}, D)
    n += 1
print(f"{n} random rulebooks: (i) composite equivalence violations {bad_i}; (ii) peg-Aethus equivalence violations {bad_ii}")
import sys; sys.exit(0 if bad_i == bad_ii == 0 else 1)
