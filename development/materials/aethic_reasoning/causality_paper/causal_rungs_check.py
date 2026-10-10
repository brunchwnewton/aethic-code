# Interventional rung for quant_causal, checked exactly. A "mechanism history" states entries in order: entry k touches
# its family V_k and earlier families (its inputs), summing to one over V_k. Default binding: settling V_k suspends
# exactly its establishing entry e_k. Claims: (a) parity: one joint, two histories, two interventional laws;
# (b) settling = Pearl's truncated factorization; (c) the Markov-equivalent triple gives three do-laws from one joint;
# (d) the back-door adjustment over X's inputs, a theorem of the do-calculus, holds for settling (inherited).
import itertools, random
from fractions import Fraction as Fr
rng = random.Random(477); V = {}
def bad(k, x): V[k] = V.get(k, 0) + bool(x)
def joint(order, ins, cpt, settle=None):
    W = {}
    for vals in itertools.product([0, 1], repeat=len(order)):
        v = dict(zip(order, vals)); w = Fr(1)
        for f in order:
            if settle and f == settle[0]: w *= 1 if v[f] == settle[1] else 0     # the settled family: its entry suspended
            else: w *= cpt[f][tuple(v[i] for i in ins[f])][v[f]]
        if w: W[tuple(v[f] for f in sorted(order))] = W.get(tuple(v[f] for f in sorted(order)), 0) + w
    return W
def marg(W, fams, keep):
    idx = [sorted(fams).index(k) for k in keep]; M = {}
    for k, w in W.items(): key = tuple(k[i] for i in idx); M[key] = M.get(key, 0) + w
    return M
def rnd_cpt(ins):
    return {k: (lambda p: {0: 1 - p, 1: p})(Fr(rng.randint(0, 10), 10)) for k in itertools.product([0, 1], repeat=len(ins))}

# (a) parity: A = U, B = A  versus  B = U, A = B.
h1 = joint(['A', 'B'], {'A': [], 'B': ['A']}, {'A': {(): {0: Fr(1, 2), 1: Fr(1, 2)}}, 'B': {(0,): {0: 1, 1: 0}, (1,): {0: 0, 1: 1}}})
h2 = joint(['B', 'A'], {'B': [], 'A': ['B']}, {'B': {(): {0: Fr(1, 2), 1: Fr(1, 2)}}, 'A': {(0,): {0: 1, 1: 0}, (1,): {0: 0, 1: 1}}})
d1 = joint(['A', 'B'], {'A': [], 'B': ['A']}, {'A': {(): {0: Fr(1, 2), 1: Fr(1, 2)}}, 'B': {(0,): {0: 1, 1: 0}, (1,): {0: 0, 1: 1}}}, settle=('A', 0))
d2 = joint(['B', 'A'], {'B': [], 'A': ['B']}, {'B': {(): {0: Fr(1, 2), 1: Fr(1, 2)}}, 'A': {(0,): {0: 1, 1: 0}, (1,): {0: 0, 1: 1}}}, settle=('A', 0))
print("parity: same joint:", h1 == h2, "| settle A=0 -> P(B):", marg(d1, ['A', 'B'], ['B']), "vs", marg(d2, ['A', 'B'], ['B']))

# (b) and (d) on random networks over four binary families.
for trial in range(1500):
    order = rng.sample(['W', 'X', 'Y', 'Z'], 4)
    ins = {f: [g for g in order[:order.index(f)] if rng.random() < 0.5] for f in order}
    cpt = {f: rnd_cpt(ins[f]) for f in order}
    W = joint(order, ins, cpt); fams = order
    for X in order:
        for x in [0, 1]:
            S = joint(order, ins, cpt, settle=(X, x))
            bad('(b) settling not normalized', sum(S.values()) != 1)
            # Pearl's truncated factorization, written independently
            T = {}
            for vals in itertools.product([0, 1], repeat=4):
                v = dict(zip(sorted(fams), vals))
                if v[X] != x: continue
                w = Fr(1)
                for f in order:
                    if f != X: w *= cpt[f][tuple(v[i] for i in ins[f])][v[f]]
                if w: T[vals] = w
            bad('(b) settling != truncated factorization', S != T)
            # (d) back-door adjustment over X's inputs: P(y | do(x)) = sum_z P(y | x, z) P(z)
            Z = ins[X]
            for Y in [f for f in order if f != X and f not in Z]:
                PY_do = marg(S, fams, [Y])
                PZ = marg(W, fams, Z) if Z else {(): sum(W.values())}; PXZ = marg(W, fams, [X] + Z); PYXZ = marg(W, fams, [Y, X] + Z)
                tot = sum(W.values())
                for y in [0, 1]:
                    adj = Fr(0)
                    for z, pz in PZ.items():
                        if PXZ.get((x,) + z, 0): adj += PYXZ.get((y, x) + z, 0) / PXZ[(x,) + z] * pz / tot
                    positivity = all(PXZ.get((x,) + z, 0) for z in PZ)
                    if positivity: bad('(d) back-door adjustment fails', PY_do.get((y,), 0) != adj)
# (c) the Markov-equivalent triple: one joint, three histories, three do-laws for settling A.
pA, pCa, pBc = Fr(3, 10), {0: Fr(2, 10), 1: Fr(7, 10)}, {0: Fr(1, 10), 1: Fr(8, 10)}
g1 = (['A', 'C', 'B'], {'A': [], 'C': ['A'], 'B': ['C']}, {'A': {(): {0: 1 - pA, 1: pA}}, 'C': {(a,): {0: 1 - pCa[a], 1: pCa[a]} for a in [0, 1]}, 'B': {(c,): {0: 1 - pBc[c], 1: pBc[c]} for c in [0, 1]}})
J = joint(*g1); PC = marg(J, ['A', 'B', 'C'], ['C']); PAC = marg(J, ['A', 'B', 'C'], ['A', 'C']); PBC = marg(J, ['A', 'B', 'C'], ['B', 'C']); PB = marg(J, ['A', 'B', 'C'], ['B'])
cA = {(c,): {a: PAC[(a, c)] / PC[(c,)] for a in [0, 1]} for c in [0, 1]}; cB = {(c,): {b: PBC[(b, c)] / PC[(c,)] for b in [0, 1]} for c in [0, 1]}
cC_b = {(b,): {c: PBC[(b, c)] / PB[(b,)] for c in [0, 1]} for b in [0, 1]}
g2 = (['C', 'A', 'B'], {'C': [], 'A': ['C'], 'B': ['C']}, {'C': {(): {c: PC[(c,)] for c in [0, 1]}}, 'A': cA, 'B': cB})
g3 = (['B', 'C', 'A'], {'B': [], 'C': ['B'], 'A': ['C']}, {'B': {(): {b: PB[(b,)] for b in [0, 1]}}, 'C': cC_b, 'A': cA})
print("triple: one joint:", joint(*g1) == joint(*g2) == joint(*g3))
def profile(g):
    J0 = joint(*g); fams = ['A', 'B', 'C']; tot = sum(J0.values())
    pB = marg(J0, fams, ['B'])[(1,)] / tot; pA = marg(J0, fams, ['A'])[(1,)] / tot
    doA = marg(joint(*g, settle=('A', 1)), fams, ['B'])[(1,)]; doB = marg(joint(*g, settle=('B', 1)), fams, ['A'])[(1,)]
    return (doA != pB, doB != pA)          # (settling A moves B, settling B moves A)
profiles = [profile(g) for g in (g1, g2, g3)]
print("profiles (settle A moves B, settle B moves A) for A->C->B, A<-C->B, A<-C<-B:", profiles, "| distinct:", len(set(profiles)) == 3)
laws = profiles
for k, x in V.items(): print(f"  {k:<44} violations: {x}")
print("ALL CAUSAL CLAIMS HOLD" if not any(V.values()) and len(set(laws)) == 3 and h1 == h2 else "PROBLEM")
