"""Aethic deduction battery.

Each check encodes a worked example of 1_Aethic_Reasoning.tex in the peg/state formalism of Sections 3.1-3.2,
computes its verdict from the axioms alone (closure without explosion, carvings with enforced splitting over
all branches, rendering to the validity quotient, weighted sums for probability), and compares it with the
verdict the paper states. Exit code 0 iff every check reproduces the paper.
"""
import itertools, sys
from fractions import Fraction as Fr
fs = frozenset


class Rulebook:
    """Attributes with pegs; declared jointly invalid sets (pegs, or pegs with states); carvings with blocks."""
    def __init__(self, attrs, decls=(), carvings=None):
        self.A = {a: list(p) for a, p in attrs.items()}
        self.of = {p: a for a, ps in self.A.items() for p in ps}
        self.D = [fs(pr) for ps in self.A.values() for pr in itertools.combinations(ps, 2)] + [fs(d) for d in decls]
        self.carv = carvings or {}                      # carving state (attr, filling) -> (attr carved, [blocks])

    def cl(self, R, E0=()):
        """Closure: narrowing, propagation, elimination, invalidation (the empty filling is a tag), splitting."""
        C, E = set(R), set(E0)
        while True:
            while True:
                new, newE, by = set(), set(), {}
                for a, F in C: by.setdefault(a, []).append(F)
                for a, Fs in by.items():
                    for F in Fs:
                        for G in Fs: new.add((a, F & G))
                held = {next(iter(F)) for a, F in C if len(F) == 1}
                h = lambda m: (m in C) if isinstance(m, tuple) else (m in held)
                for Dset in self.D:
                    for p in Dset:
                        if not isinstance(p, tuple) and all(h(q) for q in Dset if q != p): newE.add(p)
                    if any(isinstance(m, tuple) for m in Dset) and all(h(m) for m in Dset):
                        st = next(m for m in Dset if isinstance(m, tuple)); new.add((st[0], fs()))
                EE = E | newE
                for p in EE:
                    for F in by.get(self.of[p], []): new.add((self.of[p], F - {p}))
                for a, ps in self.A.items():
                    for p in ps:
                        if all(q in EE for q in ps if q != p): new.add((a, fs({p})))
                if new <= C and newE <= E: break
                C |= new; E |= newE
            grew = False
            for cst, (X, blocks) in self.carv.items():
                if cst not in C: continue
                parts = [(fs(C), fs(E)) if (X, B) in C else self.cl(C | {(X, B)}, E) for B in blocks]
                iS, iE = fs.intersection(*[p[0] for p in parts]), fs.intersection(*[p[1] for p in parts])
                if not (iS <= C and iE <= E): C |= iS; E |= iE; grew = True
            if not grew: return fs(C), fs(E)

    @staticmethod
    def invalid(c): return any(len(F) == 0 for a, F in c[0])


def st(a, *pegs): return (a, fs(pegs))
def core(terms): return (fs.intersection(*[t[0] for t in terms]), fs.intersection(*[t[1] for t in terms]))
results = []
def check(name, ok, detail): results.append((name, ok, detail))


# ---------------------------------------------------------------------------------------------------------------
# 1. Cautious Monotony on the sprinklers ledger (Section: The Sprinklers, Walked Through; Prop. cm_residues)
# ---------------------------------------------------------------------------------------------------------------
rb = Rulebook({'S': ['s', '~s'], 'Y': ['y', '~y'], 'X': ['x', '~x'], 'Z': ['z', '~z']}, decls=[{'s', '~y'}, {'x', 's', '~z'}])
def supports(rep, attr):
    """Stated attributes whose held pegs, in a declared set, excluded the other pegs of attr."""
    C, E = rb.cl(rep); held = {next(iter(F)) for a, F in C if len(F) == 1}; out = set()
    for p in rb.A[attr]:
        if p in E:
            for Dset in rb.D:
                if p in Dset and all(q in held for q in Dset if q != p): out |= {rb.of[q] for q in Dset if q != p}
    return out - {attr}
def residue(ledger, ante):
    reopen = {a for a, F in ante}
    while True:
        grow = set().union(*[supports(ledger, a) for a in reopen]) & {a for a, F in ledger}
        if grow <= reopen: break
        reopen |= grow
    rep = {(a, F) for a, F in ledger if a not in reopen} | set(ante)
    free = [a for a in rb.A if not any(b == a for b, F in rep)]
    terms = [rb.cl(rep | {st(a, p) for a, p in zip(free, ch)}) for ch in itertools.product(*[rb.A[a] for a in free])]
    valid = [t for t in terms if not rb.invalid(t)]
    pockets = sorted(tuple(sorted((a, next(iter(F))) for a, F in t[0] if len(F) == 1 and a in 'XSYZ')) for t in valid)
    return reopen - {a for a, F in ante}, pockets, core(valid)
L = {st('S', 's')}
_, P1, K1 = residue(L, {st('X', 'x')})
sup, P3, K3 = residue(L, {st('X', 'x'), st('Y', 'y')})
exp1 = [(('S', 's'), ('X', 'x'), ('Y', 'y'), ('Z', 'z'))]
exp3 = sorted([(('S', 's'), ('X', 'x'), ('Y', 'y'), ('Z', 'z')), (('S', '~s'), ('X', 'x'), ('Y', 'y'), ('Z', 'z')), (('S', '~s'), ('X', 'x'), ('Y', 'y'), ('Z', '~z'))])
q1, q2, q3 = st('Y', 'y') in K1[0], st('Z', 'z') in K1[0], st('Z', 'z') in K3[0]
check("Cautious Monotony (sprinklers)",
      P1 == exp1 and P3 == exp3 and sup == {'S'} and q1 and q2 and not q3,
      f"R(x) = {len(P1)} pocket, R(x&y) = {len(P3)} pockets (paper: 1 and 3, exact match: {P1 == exp1 and P3 == exp3}); "
      f"support reopened by derivation: {sorted(sup)}; Q1 {q1}, Q2 {q2}, Q3 {q3} (paper: T, T, F) -> CM fails")


# ---------------------------------------------------------------------------------------------------------------
# 2. Powerset Invalidation Theorem on the four-slit case (detector fires iff A or B; Theorem thm:powerset)
# ---------------------------------------------------------------------------------------------------------------
slits = ['A', 'B', 'C', 'D']
records = [{'A', 'nofire'}, {'B', 'nofire'}, {'C', 'fire'}, {'D', 'fire'}]           # the detector's correlations
sig = {s: next(r for r in ['fire', 'nofire'] if {s, r} not in [set(x) for x in records]) for s in slits}
classes = sorted({fs(s for s in slits if sig[s] == r) for r in sig.values()}, key=sorted)  # record-induced partition
cands = [fs(c) for k in range(1, 5) for c in itertools.combinations(slits, k)]
attrs = {'X': slits, 'Det': ['fire', 'nofire'], 'Kc': ['kc', 'kbc']}
decls = [set(r) for r in records]
for T in cands:                                                                     # irreducibility of every claim
    if len(T) >= 2:
        e = 'e_' + ''.join(sorted(T)); attrs['E' + e] = [e, '~' + e]
        for k in range(1, len(T)):
            for Tp in itertools.combinations(sorted(T), k): decls.append({e, ('X', fs(Tp))})
rbp = Rulebook(attrs, decls, carvings={st('Kc', 'kc'): ('X', list(classes))})
eid = lambda T: st('Ee_' + ''.join(sorted(T)), 'e_' + ''.join(sorted(T)))
claim = lambda T: {st('X', *T)} | ({eid(T)} if len(T) >= 2 else set())
carving = {st('Kc', 'kc')}                                                          # third postulate, via the fundamental theorem
blocks = {eid(E) for E in classes if len(E) >= 2}                                    # second postulate: classes as irreducible blocks
computed, expected = {}, {}
for T in cands:
    full = not rbp.invalid(rbp.cl(claim(T) | carving | blocks))
    p3_only = not rbp.invalid(rbp.cl(claim(T) | carving))                           # carving alone
    p2_only = not rbp.invalid(rbp.cl(claim(T) | blocks))                            # blocks alone
    computed[T] = 'valid' if full else ('xP3' if (not p3_only and p2_only) else ('xP2' if (not p2_only and p3_only) else 'both'))
    expected[T] = 'valid' if T in classes else ('xP2' if any(T < E for E in classes) else 'xP3')
agree = all(computed[T] == expected[T] for T in cands)
counts = {k: sum(1 for T in cands if computed[T] == k) for k in ['valid', 'xP2', 'xP3', 'both']}
check("Powerset Invalidation (four slits)", agree,
      f"record classes {[''.join(sorted(E)) for E in classes]}; 15 nonempty cases: valid {counts['valid']}, xP2 {counts['xP2']}, "
      f"xP3 {counts['xP3']}, overlapping {counts['both']} (theorem: 2, 4, 9, 0); every case matches the theorem: {agree}. "
      f"xP3 arises from the carving alone and xP2 from the class blocks alone.")


# ---------------------------------------------------------------------------------------------------------------
# 3. The double slit: the union of Case 2 and Case 3 is neither Case 4 nor Case 1 (Structuring the Outcome Cases)
# ---------------------------------------------------------------------------------------------------------------
rbd = Rulebook({'X': ['1', '2', 'none'], 'Kx': ['kx', 'kbx'], 'Ee12': ['e12', '~e12']},
               decls=[{p, 'kbx'} for p in ['1', '2', 'none']] + [{'e12', ('X', fs({'1'}))}, {'e12', ('X', fs({'2'}))}],
               carvings={st('Kx', 'kx'): ('X', [fs({'1'}), fs({'2'}), fs({'none'})])})
case1, case2, case3 = rbd.cl({st('X', 'none')}), rbd.cl({st('X', '1')}), rbd.cl({st('X', '2')})
case4 = rbd.cl({st('X', '1', '2'), st('Ee12', 'e12')})                               # both slits, irreducibly
U = core([case2, case3])                                                             # what the union of Cases 2 and 3 asserts
not4 = U != case4 and st('X', '1', '2') not in U[0]
not1 = U != case1 and 'none' in U[1]
mark = st('Kx', 'kx') in U[0]
incompatible = rbd.invalid(rbd.cl(case4[0] | case2[0])) and rbd.invalid(rbd.cl(case4[0] | case3[0]))
check("Double slit: union of Cases 2 and 3", not4 and not1 and mark and incompatible,
      f"core is not Case 4 (no agreeing state): {not4}; not Case 1 (excludes no-slit): {not1}; carries the single-peg "
      f"carving: {mark}; Case 4 with either single-slit case is invalid: {incompatible}")


# ---------------------------------------------------------------------------------------------------------------
# 4. Monty Hall: invalid terms deleted, weights loaned to surviving siblings (Aethic Bayesianism)
# ---------------------------------------------------------------------------------------------------------------
rbm = Rulebook({'C': ['c1', 'c2', 'c3'], 'H': ['h1', 'h2', 'h3']},
               decls=[{'h1'}] + [{f'c{i}', f'h{i}'} for i in (1, 2, 3)])                 # host never opens the pick or the car
terms = {}
for i in (1, 2, 3):
    child = rbm.cl({st('C', f'c{i}')})
    doors = [h for h in rbm.A['H'] if h not in child[1]]                              # the host's valid choices, from closure
    for h in doors: terms[(f'c{i}', h)] = Fr(1, 3) * Fr(1, len(doors))
observed = st('H', 'h3')
after = {k: w for k, w in terms.items() if not rbm.invalid(rbm.cl({st('C', k[0]), st('H', k[1]), observed}))}
Z = sum(after.values()); stay = after.get(('c1', 'h3'), 0) / Z; switch = after.get(('c2', 'h3'), 0) / Z
check("Monty Hall", stay == Fr(1, 3) and switch == Fr(2, 3),
      f"host weights from closure {dict((k, str(v)) for k, v in terms.items())}; after the reveal and rendering: "
      f"stay {stay}, switch {switch} (paper: 1/3, 2/3)")


# ---------------------------------------------------------------------------------------------------------------
print("Aethic deduction battery: the paper's worked examples, computed from the axioms\n")
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}\n       {detail}\n")
print(f"{sum(ok for _, ok, _ in results)} of {len(results)} examples reproduce the paper's verdicts")
sys.exit(0 if all(ok for _, ok, _ in results) else 1)
