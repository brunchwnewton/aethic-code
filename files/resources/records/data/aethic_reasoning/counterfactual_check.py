#!/usr/bin/env python3
"""Reproducible check for "Counterfactual Evaluation by Perturbation of Information States".

The finite scenario fragment, implemented exactly as the paper defines it:
  attributes with finite value sets; a constraint layer of nogoods (sets of assignments jointly invalid; laws, never
  retracted); a state given by stated base entries, its content C(A) the assignments entailed by them; reopening
  attributes Q at the bare scope = the inclusion-maximal closed restrictions of A blank on every attribute in Q
  (dual-peg reading: each conjunct's attribute an argument), selected by an antecedent-independent priority policy
  (default: none, so ties are kept as a set); restatement = closure with the antecedent; the residue's pockets = the
  valid total assignments extending some restated intermediate (all visible: every terminal pocket carries positive
  weight); would (X |~ Y) = every pocket affirms Y.
Prints: (1) the four-attribute witness under the dual-peg and Boolean readings; (2) the Cut-without-nesting
countermodel; (3) the witness under five competitor semantics; (4) a random-model test of Cut, pocket monotonicity,
the Cautious-Monotony characterization and Or.   Usage: python3 counterfactual_check.py [n_models] [seed]"""
import itertools, random, sys

class Model:
    def __init__(self, attrs, nogoods):
        self.attrs = dict(attrs); self.names = list(attrs); self.nogoods = [frozenset(n) for n in nogoods]
        self.worlds = [w for w in (dict(zip(self.names, vals)) for vals in itertools.product(*[self.attrs[a] for a in self.names]))
                       if not any(all(w[q] == v for q, v in ng) for ng in self.nogoods)]
    def ext(self, entries):                      # valid total assignments extending a set of entries
        return [w for w in self.worlds if all(w[q] == v for q, v in entries)]
    def closure(self, entries):                  # the entailed assignments (None if inconsistent)
        ws = self.ext(entries)
        if not ws: return None
        return frozenset((q, ws[0][q]) for q in self.names if all(w[q] == ws[0][q] for w in ws))
    def blank(self, content, q): return not any(a == q for a, _ in content)

def reopen(M, content, Q, priority=None):
    """Inclusion-maximal closed restrictions of `content` blank on every attribute in Q; priority, if given, is a list of
    entries most-protected first, and selects among the maximal ones lexicographically by which protected entries they keep."""
    C = sorted(content); cands = set()
    for r in range(len(C) + 1):
        for S in itertools.combinations(C, r):
            cl = M.closure(S)
            if cl is not None and cl <= content and all(M.blank(cl, q) for q in Q): cands.add(cl)
    maxi = sorted((c for c in cands if not any(c < d for d in cands)), key=lambda c: sorted(c))   # deterministic order
    if priority:
        key = lambda c: tuple(e in c for e in priority); best = max(key(c) for c in maxi); maxi = [c for c in maxi if key(c) == best]
    return maxi

def pockets(M, content, X, Q=None, priority=None):
    """Residue of the perturbation by antecedent X (a dict of assignments): reopen X's attributes (or Q), restate X, prune."""
    Q = list(X) if Q is None else Q; out = []
    for I in reopen(M, content, Q, priority):
        for w in M.ext(set(I) | set(X.items())):
            if w not in out: out.append(w)
    return out

def would(P, Y): return bool(P) and all(all(w[q] == v for q, v in Y.items()) for w in P)
def show(P, order): return ', '.join('(' + ', '.join(('' if w[q] else '¬') + q.lower() for q in order) + ')' for w in P)

def witness():
    M = Model({'X': (1, 0), 'S': (1, 0), 'Y': (1, 0), 'Z': (1, 0)}, [{('S', 1), ('Y', 0)}, {('X', 1), ('S', 1), ('Z', 0)}])
    A = M.closure({('S', 1)}); order = ['X', 'S', 'Y', 'Z']
    print("1. The four-attribute witness. Constraints: {s,¬y} and {x,s,¬z} invalid; A states s (content:", sorted(A), ")")
    Px = pockets(M, A, {'X': 1}); Pxy = pockets(M, A, {'X': 1, 'Y': 1})
    Ib = [I for I in reopen(M, A, [])]               # Boolean reading: the coarse attribute 'X and Y?' is already blank in A
    Pb = [w for I in Ib for w in M.ext(set(I) | {('X', 1), ('Y', 1)})]
    print("   intermediate for x:", [sorted(I) for I in reopen(M, A, ['X'])], "| pockets:", show(Px, order))
    print("   intermediate for x∧y (dual peg):", [sorted(I) for I in reopen(M, A, ['X', 'Y'])], "| pockets:", show(Pxy, order))
    print("   x∧y under the Boolean reading: pockets:", show(Pb, order))
    print(f"   X|~y: {would(Px, {'Y': 1})}   X|~z: {would(Px, {'Z': 1})}   X∧y|~z (dual peg): {would(Pxy, {'Z': 1})}   X∧y|~z (Boolean): {would(Pb, {'Z': 1})}   X|~¬y: {would(Px, {'Y': 0})}")
    return M, A

def cutfail():
    M = Model({'P': (1, 0), 'R': (1, 0), 'X': (1, 0), 'Y': (1, 0)}, [{('P', 1), ('Y', 0)}, {('P', 1), ('R', 1), ('X', 1)}])
    A = M.closure({('P', 1), ('R', 1)}); pri = [('P', 1)]
    Px = pockets(M, A, {'X': 1}, priority=pri); Pxy = pockets(M, A, {'X': 1, 'Y': 1}, priority=pri)
    print("\n2. Cut without nesting. A states p and r; {p,¬y}, {p,r,x} invalid; priority keeps the generalization p.")
    print("   maximal x-blank restrictions:", [sorted(I) for I in reopen(M, A, ['X'])], "→ selected", [sorted(I) for I in reopen(M, A, ['X'], pri)])
    print("   intermediate for x∧y:", [sorted(I) for I in reopen(M, A, ['X', 'Y'], pri)])
    print(f"   X|~y: {would(Px, {'Y': 1})}   X∧y|~r: {would(Pxy, {'R': 1})}   X|~r: {would(Px, {'R': 1})}   X|~¬r: {would(Px, {'R': 0})}")

def competitors(M, A):
    print("\n3. The witness under competitor semantics (verdicts on X□→y, X□→z, X∧y□→z):")
    base = {('S', 1)}
    def premise(X):                               # Veltman/Kratzer-style: maximal subsets of the stated facts consistent with X, laws kept
        subs = [set(S) for r in range(len(base), -1, -1) for S in itertools.combinations(sorted(base), r) if M.ext(set(S) | set(X.items()))]
        maxs = [S for S in subs if not any(S < T for T in subs)]
        return [w for S in maxs for w in M.ext(S | set(X.items()))]
    def agm(X):                                   # AGM revision; X is consistent with the belief set, so revision is expansion
        ws = M.ext(set(A) | set(X.items())); return ws if ws else M.ext(set(X.items()))
    def pma(X):                                   # Winslett's PMA update: each model of A moves to its ⊆-closest X-models
        out = []
        for w in M.ext(set(A)):
            cands = M.ext(set(X.items())); d = {i: frozenset(q for q in M.names if c[q] != w[q]) for i, c in enumerate(cands)}
            for i, c in enumerate(cands):
                if not any(d[j] < d[i] for j in d) and c not in out: out.append(c)
        return out
    def pearl(X):                                 # SCM: S:=U_S, X:=U_X, Y:=S∨U_Y, Z:=(X∧S)∨U_Z; evidence s; do(X); U's not fixed by evidence range freely
        out = []
        for us, ux, uy, uz in itertools.product((1, 0), repeat=4):
            if us != 1: continue                  # abduction: the evidence s fixes U_S = 1
            v = {'S': us, 'X': X.get('X', ux)}; v['Y'] = X['Y'] if 'Y' in X else int(v['S'] or uy); v['Z'] = int((v['X'] and v['S']) or uz)
            if v not in out: out.append(v)
        return out
    rows = [("this paper, dual-peg reading", lambda X: pockets(M, A, X)),
            ("this paper, Boolean reading", lambda X: pockets(M, A, X, Q=['X']) if 'Y' in X else pockets(M, A, X)),
            ("premise semantics (maximal consistent premise sets)", premise), ("AGM revision", agm),
            ("PMA update (Winslett)", pma), ("Pearl, SCM Y:=S∨U_Y, Z:=(X∧S)∨U_Z", pearl)]
    for name, f in rows:
        a, b, c = would(f({'X': 1}), {'Y': 1}), would(f({'X': 1}), {'Z': 1}), would(f({'X': 1, 'Y': 1}), {'Z': 1})
        cm = 'fails' if (a and b and not c) else ('holds' if (a and b) else 'not instantiated')
        print(f"   {name:52s} {str(a):5s} {str(b):5s} {str(c):5s}  Cautious Monotony: {cm}")

def random_test(n, seed):
    rng = random.Random(seed); stats = dict(models=0, cut_nested=0, cut_fail_nested=0, pm_nested=0, pm_fail=0, cm_char=0, cm_char_fail=0, cm_fail=0, or_tests=0, or_fail=0, cut_unnested_fail=0)
    while stats['models'] < n:
        k = rng.choice([4, 5]); attrs = {f'A{i}': (0, 1, 2) if i == 0 else (0, 1) for i in range(k)}; names = list(attrs)
        nogoods = []
        for _ in range(rng.randint(1, 4)):
            qs = rng.sample(names, rng.choice([2, 3])); nogoods.append({(q, rng.choice(attrs[q])) for q in qs})
        M = Model(attrs, nogoods)
        if len(M.worlds) < 2: continue
        base = {(q, rng.choice(attrs[q])) for q in rng.sample(names, rng.randint(1, 3))}; A = M.closure(base)
        if A is None: continue
        stats['models'] += 1
        qx, qy, qz = rng.sample(names, 3); X = {qx: rng.choice(attrs[qx])}; Y = {qy: rng.choice(attrs[qy])}; Z = {qz: rng.choice(attrs[qz])}
        Rx, Rxy = reopen(M, A, [qx]), reopen(M, A, [qx, qy])
        Px, Pxy = pockets(M, A, X), pockets(M, A, {**X, **Y})
        if not Px or not Pxy: continue
        nested = len(Rx) == 1 and len(Rxy) == 1 and Rxy[0] <= Rx[0]
        if would(Px, Y):
            if nested:
                stats['pm_nested'] += 1; stats['pm_fail'] += any(w not in Pxy for w in Px)
                if would(Pxy, Z): stats['cut_nested'] += 1; stats['cut_fail_nested'] += not would(Px, Z)
                if would(Px, Z):                        # the Cautious-Monotony characterization (Proposition cmwhere)
                    D = Rx[0] - Rxy[0]; added = [w for w in Pxy if not all(w[q] == v for q, v in D)]
                    predicted = any(not all(w[q] == v for q, v in Z.items()) for w in added)
                    actual = not would(Pxy, Z); stats['cm_char'] += 1; stats['cm_char_fail'] += predicted != actual; stats['cm_fail'] += actual
            elif would(Pxy, Z) and not would(Px, Z): stats['cut_unnested_fail'] += 1
        if attrs[qx] == (0, 1, 2):                       # Or, within the three-valued attribute
            v1, v2 = rng.sample((0, 1, 2), 2); P1, P2 = pockets(M, A, {qx: v1}), pockets(M, A, {qx: v2})
            Pd = [w for I in reopen(M, A, [qx]) for w in M.ext(set(I)) if w[qx] in (v1, v2)]
            if P1 and P2 and would(P1, Z) and would(P2, Z): stats['or_tests'] += 1; stats['or_fail'] += not would(Pd, Z)
    print(f"\n4. Random finite models (n = {n}, seed = {seed}; 4-5 attributes, one three-valued; 1-4 nogoods; fully supported):")
    print(f"   Cut, nested intermediates: {stats['cut_nested']} instances, {stats['cut_fail_nested']} failures")
    print(f"   pocket monotonicity, nested: {stats['pm_nested']} instances, {stats['pm_fail']} failures")
    print(f"   Cautious-Monotony characterization (Proposition cmwhere): {stats['cm_char']} instances, {stats['cm_char_fail']} mismatches; Cautious Monotony failed in {stats['cm_fail']} of them")
    print(f"   Or, within one attribute: {stats['or_tests']} instances, {stats['or_fail']} failures")
    print(f"   Cut failing where the intermediates are not nested: {stats['cut_unnested_fail']} instances (Proposition cutfail's phenomenon)")

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5000; seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20261005
    M, A = witness(); cutfail(); competitors(M, A); random_test(n, seed)
