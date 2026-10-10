# Cautious Monotony on the sprinklers ledger, computed by the axioms: closure (no explosion) finds supports,
# single-peg carvings split the reopened representation into a sum of total assignments (first tier),
# rendering deletes the invalid terms, WOULD = the rendered core, MIGHT = some rendered term.
import itertools
fs = frozenset
ATTR = {'S': ['s', '~s'], 'Y': ['y', '~y'], 'X': ['x', '~x'], 'Z': ['z', '~z']}
OF = {p: a for a, ps in ATTR.items() for p in ps}
LAWS = [fs({'s', '~y'}), fs({'x', 's', '~z'})]                        # l1, l2: jointly invalid
D = [fs(ps) for ps in ATTR.values()] + LAWS                             # pegs of an attribute pairwise disjoint (2 pegs each)
def cl(R):                                                              # narrowing, propagation (with provenance), elimination; tags, no explosion
    C, E, why = set(R), set(), {}
    while True:
        new, by = set(), {}
        for a, F in C: by.setdefault(a, []).append(F)
        for a, Fs in by.items():
            for F in Fs:
                for G in Fs: new.add((a, F & G))
        held = {next(iter(F)) for a, F in C if len(F) == 1}
        newE = set()
        for Dset in D:
            for p in Dset:
                if p not in E and all(q in held for q in Dset if q != p): newE.add(p); why.setdefault(p, fs(Dset - {p}))
        for p in E | newE:
            for F in by.get(OF[p], []): new.add((OF[p], F - {p}))
        for a, ps in ATTR.items():
            for p in ps:
                if all(q in E | newE for q in ps if q != p): new.add((a, fs({p})))
        if new <= C and newE <= E: return fs(C), fs(E), why
        C |= new; E |= newE
invalid = lambda c: any(len(F) == 0 for a, F in c[0])
def supports(rep, attr):                                                # stated attributes whose held pegs excluded the other pegs of attr
    C, E, why = cl(rep); return {OF[q] for p in ATTR[attr] if p in why for q in why[p]} - {attr}
def residue(ledger, antecedent):
    targets = {a for a, F in antecedent}; reopen = set(targets)
    while True:                                                         # reopen supports of reopened stated attributes, to a fixed point
        grow = set().union(*[supports(ledger, a) for a in reopen]) & {a for a, F in ledger}
        if grow <= reopen: break
        reopen |= grow
    kept = {(a, F) for a, F in ledger if a not in reopen}
    rep = kept | set(antecedent)
    free = [a for a in ATTR if not any(b == a for b, F in rep)]
    terms = []                                                          # enforced splitting on every free attribute: the first-tier sum
    for choice in itertools.product(*[ATTR[a] for a in free]):
        t = cl(rep | {(a, fs({p})) for a, p in zip(free, choice)}); terms.append((dict(zip(free, choice)), t))
    valid = [(ch, t) for ch, t in terms if not invalid(t)]              # rendering: delete invalid terms
    core = fs.intersection(*[t[0] for ch, t in valid])
    return reopen - targets, terms, valid, core
ledger = {('S', fs({'s'}))}                                              # observed: S at s; Y at y is derived by l1
print("ledger closure:", sorted((a, tuple(sorted(F))) for a, F in cl(ledger)[0]))
for name, ante, C in [("Q1: x |~ y", {('X', fs({'x'}))}, ('Y', 'y')), ("Q2: x |~ z", {('X', fs({'x'}))}, ('Z', 'z')), ("Q3: x & y |~ z", {('X', fs({'x'})), ('Y', fs({'y'}))}, ('Z', 'z'))]:
    extra, terms, valid, core = residue(ledger, ante)
    pockets = [tuple(sorted(dict({a: next(iter(F)) for a, F in t[0] if len(F) == 1}).items())) for ch, t in valid]
    would = (C[0], fs({C[1]})) in core; might_not = any((C[0], fs({C[1]})) not in t[0] for ch, t in valid)
    print(f"{name}: reopened supports {sorted(extra) or '-'}; first-tier terms {len(terms)}, rendered {len(valid)}; pockets {[dict(p) for p in pockets]}")
    print(f"      WOULD {C[1]}: {would}   |   MIGHT NOT {C[1]}: {might_not}")
