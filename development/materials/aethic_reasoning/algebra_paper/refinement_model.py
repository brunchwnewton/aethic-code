"""The refinement collapse, computed on the referee's requested small model.

Model: X = {a, b} (the system attribute), R = {ra, rb} (a record correlated with X), W = {w1, w2} (independent),
E = {e, ne} (the irreducibility peg: holding e makes X's blank two-peg superposition irreducible).
Declared invalid: pegs of one attribute pairwise; {a, rb}, {b, ra} (the record); {e, [X:{a}]}, {e, [X:{b}]}.
Closure: narrowing, propagation, elimination, invalidation; the empty filling a tag (no explosion).

Two relations for the safety rule  F(Y) = {A not in Base : exists B desc A, forall C desc B, C in Y}:
  (1) CONTENT INCLUSION (the papers' current reading), with the all-statements Aethus adjoined, as the tree paper does;
  (2) ADMISSIBLE DESCENT: one step narrows an attribute within its current filling (never inserts a peg the
      filling excludes), and never narrows an attribute that a held irreducibility peg protects; reflexive-transitive.
"""
import itertools
fs = frozenset

def build(with_record):
    ATTR = {'X': ['a', 'b'], 'W': ['w1', 'w2'], 'E': ['e', 'ne']}
    decls = [fs({'e', ('X', fs({'a'}))}), fs({'e', ('X', fs({'b'}))})]
    if with_record:
        ATTR['R'] = ['ra', 'rb']; decls += [fs({'a', 'rb'}), fs({'b', 'ra'})]
    OF = {p: a for a, ps in ATTR.items() for p in ps}
    D = [fs(pr) for ps in ATTR.values() for pr in itertools.combinations(ps, 2)] + decls
    PROTECT = {'e': 'X'}                                      # the irreducibility peg and the attribute it protects

    def cl(R):
        C, E = set(R), set()
        while True:
            new, by = set(), {}
            for a, F in C: by.setdefault(a, []).append(F)
            for a, Fs in by.items():
                for F in Fs:
                    for G in Fs: new.add((a, F & G))
            held = {next(iter(F)) for a, F in C if len(F) == 1}
            h = lambda m: (m in C) if isinstance(m, tuple) else (m in held)
            newE = set()
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
            if new <= C and newE <= E: return (fs(C), fs(E))
            C |= new; E |= newE

    invalid = lambda c: any(len(F) == 0 for a, F in c[0])
    def filling(c, a):
        F = fs(ATTR[a])
        for b, G in c[0]:
            if b == a: F &= G
        return F - c[1]
    atoms = [(a, fs({p})) for a, ps in ATTR.items() for p in ps]
    U = {cl(set(S)) for k in range(len(atoms) + 1) for S in itertools.combinations(atoms, k)}
    return ATTR, cl, invalid, filling, U, PROTECT

def safety(U, desc, Base):
    """Greatest fixed point of F by iteration from U (finite)."""
    Y = set(U)
    while True:
        nY = {A for A in U if A not in Base and any(all(C in Y for C in desc[B]) for B in desc[A])}
        if nY == Y: return Y
        Y = nY

def run(with_record):
    ATTR, cl, invalid, filling, U, PROTECT = build(with_record)
    ALLITEMS = (fs().union(*[A[0] for A in U]) | fs((a, fs()) for a in ATTR), fs().union(*[A[1] for A in U]))
    U1 = U | {ALLITEMS}                                                        # the all-statements Aethus, adjoined
    Base1 = {A for A in U1 if invalid(A)}
    desc1 = {A: [B for B in U1 if A[0] <= B[0] and A[1] <= B[1]] for A in U1}  # (1) content inclusion
    safe1 = safety(U1, desc1, Base1)
    def steps(A):
        if invalid(A): return []
        held = {next(iter(F)) for a, F in A[0] if len(F) == 1}
        out = []
        for a in ATTR:
            if any(PROTECT.get(p) == a for p in held): continue                   # an irreducibility peg protects it
            F = filling(A, a)
            if len(F) >= 2:
                for p in F: out.append(cl(set(A[0]) | {(a, fs({p}))}))            # narrow within the filling only
        return out
    desc2 = {}
    for A in U:                                                                  # (2) admissible descent, reflexive-transitive
        seen, todo = {A}, [A]
        while todo:
            for B in steps(todo.pop()):
                if B not in seen: seen.add(B); todo.append(B)
        desc2[A] = list(seen)
    Base2 = {A for A in U if invalid(A)}
    safe2 = safety(U, desc2, Base2)
    top, Xa, Xb, Agr = cl(set()), cl({('X', fs({'a'}))}), cl({('X', fs({'b'}))}), cl({('E', fs({'e'}))})
    name = lambda A: ('top (valid blank)' if A == top else 'X=a' if A == Xa else 'X=b' if A == Xb else 'e: X irreducibly agreeing' if A == Agr else '?')
    print(f"\n=== model {'WITH' if with_record else 'WITHOUT'} the record R: {len(U)} Aethae, {len(Base2)} invalid")
    print(f"(1) content inclusion + all-statements Aethus: safe set {len(safe1)} of {len(U1)}  -> {'COLLAPSE: nothing is valid' if not safe1 else 'no collapse'}")
    print(f"(2) admissible descent:                      safe set {len(safe2)} of {len(U)}; doomed but not base-invalid: {len(U) - len(safe2) - len(Base2)}")
    for A in [top, Xa, Xb, Agr]: print(f"      {name(A):<28} safe under (2): {A in safe2}")
    # the valid blank's surviving refinement cone
    cone = [B for B in desc2[top] if B in safe2]
    print(f"      the valid blank's admissible descendants: {len(desc2[top])}, of which safe: {len(cone)}")
    # exhaustiveness: old condition vs terminal coverage, for the partition {X=a, X=b} of the blank
    old = all(any(B[0] >= Ai[0] for Ai in [Xa, Xb]) for B in desc2[top])
    terminal = [B for B in desc2[top] if not steps(B) and not invalid(B)]
    new = all(any(B[0] >= Ai[0] for Ai in [Xa, Xb]) for B in terminal)
    print(f"      exhaustiveness 'every descendant of L descends from some A_i': {old} (fails at L itself: degenerate)")
    print(f"      terminal coverage 'every complete valid resolution of L lies below some A_i': {new} ({len(terminal)} complete resolutions)")
    # the partition identity: as sums in the contracted semiring vs as a core
    core = (Xa[0] & Xb[0], Xa[1] & Xb[1])
    print(f"      partition identity as sums, [L] = [La] + [Lb]: {{L}} == {{La, Lb}} -> {({top} == {Xa, Xb})}; as a core, L = core(La + Lb): {core == top}")

run(with_record=True)
run(with_record=False)
