#!/usr/bin/env python3
"""counterfactual_check.py -- reference implementation for
"Counterfactual Evaluation by Reopening Information States".

Implements Definition 1 on finite, fully supported models (every consistent
completion is a pocket of positive weight, so Vis(R) = R) and reproduces every
countermodel in the paper.  Run with no arguments; see README_counterfactual_check.md
for the expected output.

MODEL
  attributes      name -> tuple of values
  laws            constraint layer: each law is a set of literals (attr, value)
                  declared jointly invalid; laws are never retracted
  state A         its BASIC (stated) entries; the state is their deductive closure
  support (Dep)   base-shaped: a stated entry is supported by itself alone (an
                  observation grounds nothing but itself), and a derived entry's grounds
                  are the minimal basic subsets entailing it under the laws;
                  "fully supported" means every pocket has positive weight

OPERATOR (Definition 1, with the retention clause made explicit)
  reopening of Q at the bare-attribute scope:
     clearable  Q's own stated entries and Supp(Q); Q's deductive cone follows them
     retained   K_Q = closure of the stated entries outside the clearable set
     B_Q(A)     closed restrictions B with K_Q <= C(B) <= C(A), blank on Q
     A (-) Q    inclusion-maximal members of B_Q(A)  (priority policy: tie-keeping)
     infeasible when B_Q(A) is empty (a retained entry with a law forces Q)
  antecedent targets: the attributes an antecedent restricts to a PROPER subset of
     their value space ("normalized"); an unrestricted coordinate such as y or not-y
     contributes no target and no restated content (NORMALIZE = True); the script can
     also run the un-normalized reading to exhibit the Left Logical Equivalence test
  perturbation  pi_X(A) = union over intermediates B of the consistent completions
     of Cl(B + X): the pockets; X |~ Y iff every pocket affirms Y

COMPARATORS (all on the same finite model)
  premise-MAX   evaluation over the maximal subsets of A's stated facts consistent
                with the antecedent, laws retained  (the paper's named comparator)
  basis-retract world-by-world: for each completion w of A, each minimal basis of w
                (a subset of w's literals generating w under the laws) is retracted
                to its maximal subsets consistent with the antecedent, the antecedent
                is added, and the resulting worlds are collected; X []-> Y holds iff
                every resulting world satisfies Y.  This is a Veltman-TYPE clause
                (retraction from bases of individual worlds, then extension under the
                laws); it is the script's encoding, not a transcription of Veltman 2005.
"""
from itertools import product, combinations
import random

NORMALIZE = True  # antecedent targets are the attributes restricted to a proper subset


# ----------------------------------------------------------------------------- core
class Model:
    def __init__(self, attributes, laws):
        self.attrs = dict(attributes)               # name -> values
        self.laws = [frozenset(l) for l in laws]    # jointly invalid literal sets
        self.names = list(self.attrs)
        self.worlds = [w for w in self._all_worlds() if self.consistent(w)]

    def _all_worlds(self):
        for vals in product(*[self.attrs[a] for a in self.names]):
            yield frozenset(zip(self.names, vals))

    def consistent(self, lits):
        return not any(law <= lits for law in self.laws)

    def completions(self, lits):
        """consistent total assignments extending a (consistent) set of literals"""
        return [w for w in self.worlds if lits <= w]

    def closure(self, lits):
        """deductive closure under the laws: literals true in every completion;
        None if there is no completion (the state is invalid)"""
        cs = self.completions(frozenset(lits))
        if not cs:
            return None
        return frozenset.intersection(*cs)

    def blank_on(self, closed, attrs):
        return all(all((a, v) not in closed for v in self.attrs[a]) for a in attrs)

    # --- support (Dep), base-shaped: a stated (basic) entry is supported by itself
    #     alone; a derived entry's grounds are the minimal basic subsets entailing it
    def supports(self, basic, entry):
        basic = frozenset(basic)
        if entry in basic:
            return [frozenset([entry])]
        found = []
        for k in range(1, len(basic) + 1):
            for sub in combinations(sorted(basic), k):
                if any(set(f) <= set(sub) for f in found):
                    continue
                cl = self.closure(frozenset(sub))
                if cl is not None and entry in cl:
                    found.append(frozenset(sub))
        return found

    def closed_subsets(self, content):
        content = sorted(content)
        for k in range(0, len(content) + 1):
            for sub in combinations(content, k):
                sub = frozenset(sub)
                if self.closure(sub) == sub:
                    yield sub

    # --- reopening (Definition 1(c), with the retention clause)
    def reopen(self, basic, targets, retention=True):
        basic = frozenset(basic)
        content = self.closure(basic)
        clearable_basic = set()                   # Q's own stated entries and Supp(Q)
        for a in targets:
            for v in self.attrs[a]:
                if (a, v) in content:
                    for sup in self.supports(basic, (a, v)):
                        clearable_basic |= sup
        # retained content K: what the retained stated entries entail (Q's cone is not retained)
        K = self.closure(basic - clearable_basic) if retention else frozenset()
        candidates = [c for c in self.closed_subsets(content) if K <= c and self.blank_on(c, targets)]
        maxima = [c for c in candidates if not any(c < d for d in candidates)]
        return sorted(set(maxima), key=lambda c: sorted(c))   # tie-keeping priorities

    # --- antecedents: list of (attr, allowed values)
    def targets(self, antecedent):
        return [a for a, vals in antecedent if (set(vals) != set(self.attrs[a])) or not NORMALIZE]

    def perturb(self, basic, antecedent, retention=True):
        targets = self.targets(antecedent)
        inters = self.reopen(basic, targets, retention)
        if not inters:
            return None  # infeasible
        pockets = set()
        for I in inters:
            allowed = {a: set(vals) for a, vals in antecedent if (set(vals) != set(self.attrs[a])) or not NORMALIZE}
            for w in self.completions(I):
                if all(dict(w)[a] in vals for a, vals in allowed.items()):
                    pockets.add(w)
        return sorted(pockets, key=lambda w: sorted(w))

    def would(self, basic, antecedent, consequent, retention=True):
        pockets = self.perturb(basic, antecedent, retention)
        if pockets is None:
            return None
        return all(consequent <= w for w in pockets)


def lit(a, v):
    return (a, v)


def fmt_world(model, w):
    d = dict(w)
    return "(" + ", ".join(("" if d[a] is True else "~") + a if model.attrs[a] == (True, False) else f"{a}={d[a]}" for a in model.names) + ")"


# ------------------------------------------------------------------ comparators
def premise_max(model, basic, antecedent, consequent):
    """maximal subsets of the stated facts consistent with the antecedent, laws retained"""
    basic = list(basic)
    ante = {(a, v) for a, vals in antecedent for v in vals if len(vals) == 1}
    consistent_subsets = []
    for k in range(0, len(basic) + 1):
        for sub in combinations(basic, k):
            s = frozenset(sub) | ante
            if model.closure(s) is not None:
                consistent_subsets.append(frozenset(sub))
    maxima = [s for s in consistent_subsets if not any(s < t for t in consistent_subsets)]
    worlds = [w for s in maxima for w in model.completions(s | ante)]
    return all(consequent <= w for w in worlds)


def minimal_bases(model, w):
    lits = sorted(w); found = []
    for k in range(0, len(lits) + 1):
        for sub in combinations(lits, k):
            if any(f <= frozenset(sub) for f in found):
                continue
            if model.closure(frozenset(sub)) == w:
                found.append(frozenset(sub))
    return found


def basis_retract(model, basic, antecedent, consequent):
    """Veltman-type clause: retract from the bases of each world, then extend"""
    ante = {(a, v) for a, vals in antecedent for v in vals if len(vals) == 1}
    results = set()
    for w in model.completions(frozenset(basic)):
        for base in minimal_bases(model, w):
            keep = []
            for k in range(0, len(base) + 1):
                for sub in combinations(sorted(base), k):
                    if model.closure(frozenset(sub) | ante) is not None:
                        keep.append(frozenset(sub))
            maxima = [s for s in keep if not any(s < t for t in keep)]
            for s in maxima:
                results |= set(model.completions(s | ante))
    return all(consequent <= v for v in results), sorted(results, key=sorted)


# ------------------------------------------------------------------- the checks
def section(title):
    print("\n" + "=" * 78 + f"\n{title}\n" + "=" * 78)


def check_witness():
    section("1. The four-attribute witness (Theorem: Cautious Monotony fails)")
    B = (True, False)
    M = Model({'x': B, 's': B, 'y': B, 'z': B},
              laws=[{lit('s', True), lit('y', False)},                  # s -> y
                    {lit('x', True), lit('s', True), lit('z', False)}])  # {x, s, ~z} invalid
    A = {lit('s', True)}
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]
    print("A states s; closure:", sorted(M.closure(frozenset(A))))
    print("y's minimal supports:", [sorted(s) for s in M.supports(A, lit('y', True))])
    for name, ante in [("x", X), ("x & y", XY)]:
        inters = M.reopen(A, M.targets(ante))
        pockets = M.perturb(A, ante)
        print(f"  reopen for {name:5s}: intermediates {[sorted(I) for I in inters]}")
        print(f"  pockets of pi_{name:5s}: {[fmt_world(M, w) for w in pockets]}")
    v = lambda ante, cons: M.would(A, ante, {cons})
    print("  x |~ y :", v(X, lit('y', True)), "| x |~ z :", v(X, lit('z', True)),
          "| x&y |~ z :", v(XY, lit('z', True)), "| x |~ ~y :", v(X, lit('y', False)))
    assert v(X, lit('y', True)) and v(X, lit('z', True)) and not v(XY, lit('z', True)) and not v(X, lit('y', False))
    print("  => Cautious Monotony fails at (x, y, z); Rational Monotony fails on the same instance.")
    return M, A, X, XY


def check_retention():
    section("2. Retention: the streetlight-type example  (r = red, t = stopped; law r -> t; A = {~r, ~t})")
    B = (True, False)
    M = Model({'r': B, 't': B}, laws=[{lit('r', True), lit('t', False)}])
    A = {lit('r', False), lit('t', False)}
    R = [('r', (True,))]
    with_ret = M.reopen(A, ['r'], retention=True)
    without = M.reopen(A, ['r'], retention=False)
    print("  declared supports of ~r:", [sorted(s) for s in M.supports(A, lit('r', False))], "(a stated entry; ~t is not among its grounds)")
    print("  with retention   : intermediates", with_ret, "->", "INFEASIBLE" if not with_ret else "feasible")
    print("  without retention: intermediates", [sorted(I) for I in without], "->",
          "pockets", [fmt_world(M, w) for w in M.perturb(A, R, retention=False)])
    assert not with_ret and without
    print("  => the retention clause is what makes the evidential-minimal streetlight infeasible.")


def check_cut_failure():
    section("2b. Cut without nesting (Proposition): priorities keep the generalization p over the particular r")
    B = (True, False)
    M = Model({'p': B, 'r': B, 'x': B, 'y': B},
              laws=[{lit('p', True), lit('y', False)},                   # p -> y
                    {lit('p', True), lit('r', True), lit('x', True)}])   # {p, r, x} invalid
    A = {lit('p', True), lit('r', True)}
    inters = M.reopen(A, ['x'])
    print("  reopening x, tie-keeping maxima:", [sorted(I) for I in inters])
    keep_p = [I for I in inters if lit('p', True) in I]                   # the declared priority
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]
    px = sorted({w for I in keep_p for w in M.completions(I | {lit('x', True)})}, key=sorted)
    pxy = M.perturb(A, XY)
    print("  priority selects:", [sorted(I) for I in keep_p], "-> pockets under x:", [fmt_world(M, w) for w in px])
    print("  reopening x & y:", [sorted(I) for I in M.reopen(A, ['x', 'y'])], "-> pockets:", [fmt_world(M, w) for w in pxy])
    xy_ = all(lit('y', True) in w for w in px); xyr = all(lit('r', True) in w for w in pxy); xr = all(lit('r', True) in w for w in px)
    print(f"  x |~ y: {xy_} | x&y |~ r: {xyr} | x |~ r: {xr} (x |~ ~r: {all(lit('r', False) in w for w in px)})")
    assert xy_ and xyr and not xr
    print("  => Cut fails where the priorities select among inclusion-incomparable maximal restrictions.")


def check_three_attributes():
    section("3. Minimality: a three-attribute Cautious Monotony counterexample (law z -> y; A states z)")
    B = (True, False)
    M = Model({'x': B, 'y': B, 'z': B}, laws=[{lit('z', True), lit('y', False)}])
    A = {lit('z', True)}
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]
    print("  pockets of pi_x  :", [fmt_world(M, w) for w in M.perturb(A, X)])
    print("  pockets of pi_x&y:", [fmt_world(M, w) for w in M.perturb(A, XY)])
    ok = M.would(A, X, {lit('y', True)}) and M.would(A, X, {lit('z', True)}) and not M.would(A, XY, {lit('z', True)})
    print("  x |~ y, x |~ z, x&y |/~ z :", ok)
    assert ok
    print("  => three attributes suffice; the four-attribute witness is not the smallest instance.")


def check_lle(M, A):
    global NORMALIZE
    section("4. Left Logical Equivalence: x versus x & (y or ~y) on the witness")
    X = [('x', (True,))]; XT = [('x', (True,)), ('y', (True, False))]
    for norm in (False, True):
        NORMALIZE = norm
        vz = M.would(A, XT, {lit('z', True)})
        print(f"  NORMALIZE={norm!s:5s}: targets of x&(y|~y) = {M.targets(XT)};  x&(y|~y) |~ z : {vz}  (x |~ z : {M.would(A, X, {lit('z', True)})})")
    NORMALIZE = True
    print("  => un-normalized, the unrestricted conjunct reopens y and LLE fails; normalized, it contributes no target and LLE holds.")


def check_comparators(M, A, X, XY):
    section("5. Comparators on the witness")
    z, y = {lit('z', True)}, {lit('y', True)}
    print(f"  premise-MAX (maximal consistent stated facts): x []-> y {premise_max(M, A, X, y)}, x []-> z {premise_max(M, A, X, z)}, x&y []-> z {premise_max(M, A, XY, z)}")
    r1, w1 = basis_retract(M, A, X, y); r2, w2 = basis_retract(M, A, X, z); r3, w3 = basis_retract(M, A, XY, z)
    print(f"  basis-retraction (Veltman-type): x []-> y {r1}, x []-> z {r2}, x&y []-> z {r3}")
    print(f"     worlds reached under x: {[fmt_world(M, w) for w in w1]}")
    print("  => the maximal-consistent-facts comparator keeps s and validates the instance; the basis-retraction")
    print("     clause affirms neither x []-> y nor x []-> z, so the Cautious Monotony instance does not arise for it.")


def check_inference_patterns(M, A):
    section("7. Antecedent strengthening, contraposition and transitivity")
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]; NY = [('y', (False,))]
    print("  strengthening on the witness: x |~ z", M.would(A, X, {lit('z', True)}), "| x&y |~ z", M.would(A, XY, {lit('z', True)}))
    print("  contraposition on the witness: x |~ y", M.would(A, X, {lit('y', True)}), "| ~y |~ ~x", M.would(A, NY, {lit('x', False)}),
          "| pockets under ~y:", [fmt_world(M, w) for w in M.perturb(A, NY)])
    B = (True, False)
    T = Model({'c': B, 'd': B, 'e': B}, laws=[{lit('c', True), lit('d', False)}])     # c -> d
    S = {lit('c', True), lit('e', True)}
    d, e, c = [('d', (True,))], [('e', (True,))], {lit('c', True)}
    print("  transitivity (law c -> d; state {c, e}): d |~ e", T.would(S, d, {lit('e', True)}), "| e |~ c", T.would(S, e, c), "| d |~ c", T.would(S, d, c),
          "| pockets under d:", [fmt_world(T, w) for w in T.perturb(S, d)])
    assert M.would(A, X, {lit('z', True)}) and not M.would(A, XY, {lit('z', True)})
    assert M.would(A, X, {lit('y', True)}) and not M.would(A, NY, {lit('x', False)})
    assert T.would(S, d, {lit('e', True)}) and T.would(S, e, c) and not T.would(S, d, c)
    print("  => all three patterns fail, each by a witness: reopening d clears its ground c, so d |~ e and e |~ c do not chain.")


# ----------------------------------------------------------- random-model tests
def random_model(rng):
    B = (True, False)
    n = rng.choice([4, 5])
    names = ['a', 'b', 'c', 'd', 'e'][:n]
    attrs = {a: B for a in names}
    attrs[rng.choice(names)] = (0, 1, 2)                          # one three-valued attribute
    lits = [(a, v) for a in names for v in attrs[a]]
    laws = []
    for _ in range(rng.randint(1, 4)):
        k = rng.choice([2, 3])
        law = set(rng.sample(lits, k))
        if len({a for a, _ in law}) == k:                          # distinct attributes
            laws.append(law)
    M = Model(attrs, laws)
    if not M.worlds:
        return None
    basic = set()
    for a in rng.sample(names, rng.randint(1, max(1, n - 2))):
        basic.add((a, rng.choice(attrs[a])))
    if M.closure(frozenset(basic)) is None:
        return None
    return M, basic


def random_tests(n_models=3000, seed=20261008):
    section(f"8. Random finite, fully supported models ({n_models} draws, seed {seed})")
    rng = random.Random(seed)
    stats = dict(models=0, cm_instances=0, cm_fail=0, prop_agree=0, cut_nested=0, cut_fail=0, mono=0, mono_fail=0, or_inst=0, or_fail=0)
    for _ in range(n_models):
        rm = random_model(rng)
        if rm is None:
            continue
        M, basic = rm; stats['models'] += 1
        cl = M.closure(frozenset(basic))
        for xa in M.names:
            for xv in M.attrs[xa]:
                X = [(xa, (xv,))]
                PX = M.perturb(basic, X)
                if not PX:
                    continue
                IX = M.reopen(basic, [xa])
                for ya in M.names:
                    if ya == xa:
                        continue
                    for yv in M.attrs[ya]:
                        Y = {(ya, yv)}
                        if not all(Y <= w for w in PX):
                            continue                                 # need X |~ Y
                        XY = [(xa, (xv,)), (ya, (yv,))]
                        PXY = M.perturb(basic, XY)
                        if not PXY:
                            continue
                        IXY = M.reopen(basic, [xa, ya])
                        nested = all(any(J <= I for J in IXY) for I in IX)
                        if nested:                                   # pocket monotonicity
                            stats['mono'] += 1
                            if not set(PX) <= set(PXY):
                                stats['mono_fail'] += 1
                        for za in M.names:
                            if za in (xa, ya):
                                continue
                            for zv in M.attrs[za]:
                                Z = {(za, zv)}
                                xz = all(Z <= w for w in PX); xyz = all(Z <= w for w in PXY)
                                if nested and xyz:                   # Cut
                                    stats['cut_nested'] += 1
                                    if not xz:
                                        stats['cut_fail'] += 1
                                if xz and len(IX) == 1 and len(IXY) == 1 and IXY[0] <= IX[0]:
                                    stats['cm_instances'] += 1       # Proposition (where CM fails)
                                    D = IX[0] - IXY[0]
                                    predicted = any(not (D <= w) and not (Z <= w) for w in PXY)
                                    if not xyz:
                                        stats['cm_fail'] += 1
                                    if predicted == (not xyz):
                                        stats['prop_agree'] += 1
                # Or: disjunction within one attribute against the two disjuncts
                for xv2 in M.attrs[xa]:
                    if xv2 == xv:
                        continue
                    PX2 = M.perturb(basic, [(xa, (xv2,))]); POR = M.perturb(basic, [(xa, (xv, xv2))])
                    if not PX2 or not POR:
                        continue
                    for za in M.names:
                        if za == xa:
                            continue
                        for zv in M.attrs[za]:
                            Z = {(za, zv)}
                            if all(Z <= w for w in PX) and all(Z <= w for w in PX2):
                                stats['or_inst'] += 1
                                if not all(Z <= w for w in POR):
                                    stats['or_fail'] += 1
    print(f"  valid models: {stats['models']}")
    print(f"  Proposition (where Cautious Monotony fails): {stats['cm_instances']} nested singleton instances, "
          f"criterion agrees with the operator in {stats['prop_agree']}, Cautious Monotony fails in {stats['cm_fail']}")
    print(f"  Cut, nested instances: {stats['cut_nested']}, failures {stats['cut_fail']}")
    print(f"  pocket monotonicity, nested instances: {stats['mono']}, failures {stats['mono_fail']}")
    print(f"  Or, instances: {stats['or_inst']}, failures {stats['or_fail']}")
    assert stats['prop_agree'] == stats['cm_instances'] and stats['cut_fail'] == 0 and stats['mono_fail'] == 0 and stats['or_fail'] == 0
    return stats


if __name__ == "__main__":
    M, A, X, XY = check_witness()
    check_retention()
    check_cut_failure()
    check_three_attributes()
    check_lle(M, A)
    check_comparators(M, A, X, XY)
    check_inference_patterns(M, A)
    random_tests()
    print("\nAll checks passed.")
