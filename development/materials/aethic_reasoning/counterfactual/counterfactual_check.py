#!/usr/bin/env python3
"""counterfactual_check.py -- reference implementation for
"Counterfactual Evaluation by Reopening Information States".

Implements Definition 1 on finite, fully supported models (every consistent
completion is a pocket of positive weight, so Vis(R) = R) and reproduces every
countermodel in the paper.  Run with no arguments; the output should match
counterfactual_check_expected_output.txt exactly (the random test is seeded).

MODEL
  attributes      name -> tuple of values
  laws            constraint layer: each law is a set of literals (attr, value)
                  declared jointly invalid; laws are never retracted
  state A         its STATED entries; the state is their deductive closure
  Dep             the DECLARED support relation, attribute -> the attributes it
                  rests on (its grounds); its converse gives the dependents.
                  Entailment is not support: an entry that entails a value of an
                  attribute without being declared a ground of it is not among its
                  grounds (the proceeding record of the streetlight entails that
                  the light was green and is a dependent of the light, not a ground).
                  When no Dep is declared the script uses the entailment-derived
                  default of the random tests: a stated attribute has no grounds,
                  and a derived attribute's grounds are the attributes of the
                  minimal stated subsets entailing its derived entries.

OPERATOR (Definition 1)
  scope sigma     fixes two things for a reopening of the attributes Q:
     Blank(Q)      the attributes that must be blank: Q at the evidential-minimal
                   scope; Q and its declared dependents (transitively, forward) at
                   the unidirectional scope; Q and everything Dep-connected to it at
                   the bidirectional scope
     K(A, Q)       the protected content: the closure of the stated entries of A
                   whose attributes lie outside Blank(Q) and outside Supp(Q), the
                   declared grounds of Q (transitively).  Protected content may
                   entail a value of Q; that is what makes a reopening infeasible.
  B_{sigma,Q}(A)   the closed B with K(A,Q) <= C(B) <= C(A), blank on Blank(Q); blank
                   means UNRESOLVED, no value stated (blank_on), not that every value
                   of the attribute remains admissible under the retained content
  A (-) Q          its inclusion-maximal members, all kept (tie-keeping priorities);
                   INFEASIBLE when B_{sigma,Q}(A) is empty
  antecedent       its targets are the attributes it restricts to a PROPER subset of
                   their value space (normalized form); an unrestricted coordinate
                   such as y or not-y contributes no target and no restated content
                   (NORMALIZE = True; the un-normalized reading is run once for the
                   Left Logical Equivalence test)
  perturbation     pi_X(A) = union over intermediates B of R_X(B), where
                   R_X(B) = MaxCons{P : C(B) <= C(P), P |= X}: the maximal consistent
                   refinements (here: completions) of B satisfying the antecedent's
                   constraint, which is imposed on the completions directly (perturb);
                   for an assignment this is the residue of Restate_X(B) = Cl(B + X),
                   and a constrained disjunction q in {x1, x2} persists as a constraint
                   on the pockets (the excluded value cannot return); pockets are
                   identified by content; X |~ Y iff every pocket affirms Y

COMPARATORS (on the same finite model)
  premise-MAX     evaluation over the maximal subsets of A's stated facts consistent
                  with the antecedent, laws retained (the paper's named comparator)
  basis-retract   world-by-world: for each completion w of A, each minimal basis of w
                  (a subset of w's literals generating w under the laws) is retracted
                  to its maximal subsets consistent with the antecedent, the antecedent
                  is added, and the resulting worlds are collected; X []-> Y holds iff
                  every resulting world satisfies Y.  A Veltman-TYPE clause (retraction
                  from bases of individual worlds, then extension under the laws); it is
                  the script's encoding, not a transcription of Veltman 2005.
"""
from itertools import product, combinations
import random

NORMALIZE = True
SCOPES = ('evidential', 'unidirectional', 'bidirectional')


# ----------------------------------------------------------------------------- core
class Model:
    def __init__(self, attributes, laws, dep=None):
        self.attrs = dict(attributes)                 # name -> values
        self.laws = [frozenset(l) for l in laws]      # jointly invalid literal sets
        self.names = list(self.attrs)
        self.dep = None if dep is None else {a: frozenset(g) for a, g in dep.items()}
        self.worlds = [w for w in self._all_worlds() if self.consistent(w)]

    def _all_worlds(self):
        for vals in product(*[self.attrs[a] for a in self.names]):
            yield frozenset(zip(self.names, vals))

    def consistent(self, lits):
        return not any(law <= lits for law in self.laws)

    def completions(self, lits):
        return [w for w in self.worlds if lits <= w]

    def closure(self, lits):
        """deductive closure under the laws: the literals true in every completion;
        None when there is no completion (the state is invalid)"""
        cs = self.completions(frozenset(lits))
        if not cs:
            return None
        return frozenset.intersection(*cs)

    def blank_on(self, closed, attrs):
        return all(all((a, v) not in closed for v in self.attrs[a]) for a in attrs)

    def closed_subsets(self, content):
        content = sorted(content)
        for k in range(0, len(content) + 1):
            for sub in combinations(content, k):
                sub = frozenset(sub)
                if self.closure(sub) == sub:
                    yield sub

    # --- support: declared Dep, or the entailment-derived default
    def minimal_stated_supports(self, basic, entry):
        basic = frozenset(basic); found = []
        for k in range(1, len(basic) + 1):
            for sub in combinations(sorted(basic), k):
                if any(set(f) <= set(sub) for f in found):
                    continue
                cl = self.closure(frozenset(sub))
                if cl is not None and entry in cl:
                    found.append(frozenset(sub))
        return found

    def grounds(self, basic, attr):
        """the attributes `attr` is declared to rest on"""
        if self.dep is not None:
            return set(self.dep.get(attr, ()))
        basic = frozenset(basic); cl = self.closure(basic); g = set()
        for v in self.attrs[attr]:                    # derived entries only
            if (attr, v) in cl and (attr, v) not in basic:
                for sup in self.minimal_stated_supports(basic, (attr, v)):
                    g |= {a for a, _ in sup}
        return g - {attr}

    def dependents(self, basic, attr):
        return {b for b in self.names if b != attr and attr in self.grounds(basic, b)}

    def _reach(self, basic, start, step):
        seen, frontier = set(start), set(start)
        while frontier:
            nxt = set()
            for a in frontier:
                nxt |= step(a)
            frontier = nxt - seen; seen |= nxt
        return seen

    def supp(self, basic, Q):
        """declared grounds of Q, transitively"""
        return self._reach(basic, set(Q), lambda a: self.grounds(basic, a)) - set(Q)

    def blank_set(self, basic, Q, scope):
        Q = set(Q)
        if scope == 'evidential':
            return Q
        if scope == 'unidirectional':
            return self._reach(basic, Q, lambda a: self.dependents(basic, a))
        if scope == 'bidirectional':
            return self._reach(basic, Q, lambda a: self.dependents(basic, a) | self.grounds(basic, a))
        raise ValueError(scope)

    # --- reopening (Definition 1(c))
    def reopen(self, basic, Q, scope='evidential', retention=True):
        basic = frozenset(basic); content = self.closure(basic)
        blank = self.blank_set(basic, Q, scope)
        clearable_attrs = blank | self.supp(basic, Q)
        protected_stated = frozenset(l for l in basic if l[0] not in clearable_attrs)
        K = self.closure(protected_stated) if retention else frozenset()
        candidates = [c for c in self.closed_subsets(content) if K <= c and self.blank_on(c, blank)]
        maxima = [c for c in candidates if not any(c < d for d in candidates)]
        return sorted(set(maxima), key=lambda c: sorted(c))   # tie-keeping priorities; [] = infeasible

    # --- antecedents: list of (attr, allowed values)
    def targets(self, antecedent):
        return [a for a, vals in antecedent if (set(vals) != set(self.attrs[a])) or not NORMALIZE]

    def perturb(self, basic, antecedent, scope='evidential', retention=True):
        inters = self.reopen(basic, self.targets(antecedent), scope, retention)
        if not inters:
            return None  # infeasible
        allowed = {a: set(vals) for a, vals in antecedent if (set(vals) != set(self.attrs[a])) or not NORMALIZE}
        pockets = set()
        for I in inters:                          # union over intermediates of each one's pockets
            for w in self.completions(I):
                if all(dict(w)[a] in vals for a, vals in allowed.items()):
                    pockets.add(w)
        return sorted(pockets, key=lambda w: sorted(w))

    def would(self, basic, antecedent, consequent, scope='evidential', retention=True):
        pockets = self.perturb(basic, antecedent, scope, retention)
        if pockets is None:
            return None
        return all(consequent <= w for w in pockets)


def lit(a, v):
    return (a, v)


def fmt_world(model, w):
    d = dict(w)
    return "(" + ", ".join(("" if d[a] is True else "~") + a if model.attrs[a] == (True, False) else f"{a}={d[a]}" for a in model.names) + ")"


def fmt_set(S):
    return "{" + ", ".join(("" if v is True else "~") + a if isinstance(v, bool) else f"{a}={v}" for a, v in sorted(S, key=lambda t: (t[0], str(t[1])))) + "}"


# ------------------------------------------------------------------ comparators
def premise_max(model, basic, antecedent, consequent):
    basic = list(basic)
    ante = {(a, v) for a, vals in antecedent for v in vals if len(vals) == 1}
    consistent_subsets = []
    for k in range(0, len(basic) + 1):
        for sub in combinations(basic, k):
            if model.closure(frozenset(sub) | ante) is not None:
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


def agm_expansion(model, basic, antecedent, consequent):
    """AGM (K*3)/(K*4): revision by an input consistent with the belief set is expansion;
    returns None where the input is inconsistent with the closure (not needed on the witness)"""
    ante = {(a, v) for a, vals in antecedent for v in vals if len(vals) == 1}
    K = model.closure(frozenset(basic))
    if model.closure(K | ante) is None:
        return None
    return all(consequent <= w for w in model.completions(K | ante))


def winslett_update(model, basic, antecedent, consequent):
    """Winslett's possible-models approach: each model of the state is moved to the models of the
    antecedent (and the standing laws) at inclusion-minimal change, measured on the set of
    attributes whose values change; the update is the union of the results"""
    allowed = {a: set(vals) for a, vals in antecedent}
    ante_worlds = [w for w in model.worlds if all(dict(w)[a] in vals for a, vals in allowed.items())]
    results = set()
    for m in model.completions(frozenset(basic)):
        dm = dict(m)
        diffs = {w: frozenset(a for a, v in w if dm[a] != v) for w in ante_worlds}
        minimal = [w for w in ante_worlds if not any(diffs[u] < diffs[w] for u in ante_worlds)]
        results |= set(minimal)
    return all(consequent <= w for w in results), sorted(results, key=sorted)


def pearl_structural(basic, antecedent, consequent):
    """abduction, action, prediction on the structural model of the text:
    S := U_S, X := U_X, Y := S or U_Y, Z := (X and S) or U_Z, exogenous U binary"""
    stated = dict(basic)
    allowed = {a: set(vals) for a, vals in antecedent}
    results = set()
    for us, ux, uy, uz in product((False, True), repeat=4):
        s, x = us, ux; y = s or uy; z = (x and s) or uz
        world = {'s': s, 'x': x, 'y': y, 'z': z}
        if any(world[a] != v for a, v in stated.items()):
            continue                                   # abduction: keep the U consistent with the evidence
        for xv in allowed.get('x', {x}):               # action: set the intervened variables
            for yv in allowed.get('y', {None}):
                s2, x2 = us, xv
                y2 = yv if yv is not None else (s2 or uy)
                z2 = (x2 and s2) or uz
                results.add(frozenset({('s', s2), ('x', x2), ('y', y2), ('z', z2)}))
    return all(consequent <= w for w in results), sorted(results, key=sorted)


def boolean_reading(model, basic, antecedent, consequent):
    """the Boolean reading of a conjunctive antecedent: one two-valued attribute "is X true?",
    stated true when the closure entails every conjunct, stated false when the conjunction is
    inconsistent with the closure, blank otherwise; where it is blank the reopening is the
    identity; where it is stated, the inclusion-maximal closed restrictions in which it is
    blank again, the conjunction neither entailed nor excluded (no protected content)"""
    ante = {(a, v) for a, vals in antecedent for v in vals if len(vals) == 1}
    K = model.closure(frozenset(basic))
    stated = ante <= K or model.closure(K | ante) is None
    if not stated:
        inters = [K]
    else:
        cands = [c for c in model.closed_subsets(K) if not ante <= c and model.closure(c | ante) is not None]
        inters = [c for c in cands if not any(c < d for d in cands)]
    pockets = {w for I in inters for w in model.completions(I | ante)}
    return all(consequent <= w for w in pockets)


# ------------------------------------------------------------------- the checks
def section(title):
    print("\n" + "=" * 78 + f"\n{title}\n" + "=" * 78)


B = (True, False)


def check_witness():
    section("1. The four-attribute witness (Theorem: Cautious Monotony fails)")
    M = Model({'x': B, 's': B, 'y': B, 'z': B},
              laws=[{lit('s', True), lit('y', False)},                  # s -> y
                    {lit('x', True), lit('s', True), lit('z', False)}],  # {x, s, ~z} invalid
              dep={'y': {'s'}})                                          # declared: S is the sole ground of Y; no other edges
    A = {lit('s', True)}
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]
    print("A states s; closure:", fmt_set(M.closure(frozenset(A))), "| declared grounds of y:", M.grounds(A, 'y'), "| no other dependency edges")
    for sc in SCOPES:
        print(f"  blank set for x & y at {sc:14s}: {sorted(M.blank_set(A, ['x', 'y'], sc))}; intermediates: {[fmt_set(I) for I in M.reopen(A, ['x', 'y'], sc)]}")
    for name, ante in [("x", X), ("x & y", XY)]:
        inters = M.reopen(A, M.targets(ante)); pockets = M.perturb(A, ante)
        print(f"  reopen for {name:5s}: intermediates {[fmt_set(I) for I in inters]}  (each blank on {M.targets(ante)}: {all(M.blank_on(I, M.targets(ante)) for I in inters)})")
        print(f"  pockets of pi_{name:5s}: {[fmt_world(M, w) for w in pockets]}")
    v = lambda ante, cons: M.would(A, ante, {cons})
    print("  x |~ y :", v(X, lit('y', True)), "| x |~ z :", v(X, lit('z', True)), "| x&y |~ z :", v(XY, lit('z', True)), "| x |~ ~y :", v(X, lit('y', False)))
    assert v(X, lit('y', True)) and v(X, lit('z', True)) and not v(XY, lit('z', True)) and not v(X, lit('y', False))
    for sc in SCOPES:
        assert M.would(A, X, {lit('z', True)}, sc) and not M.would(A, XY, {lit('z', True)}, sc)
    print("  => Cautious Monotony fails at (x, y, z) at every scope; Rational Monotony fails on the same instance.")
    return M, A, X, XY


class StrongModel(Model):
    """the comprehensive framework's stronger requirement at the intermediate: every value of each blanked
    attribute must remain admissible (consistent with the intermediate's content under the laws), not merely
    no value stated; used only by check 1b"""
    def blank_on(self, closed, attrs):
        for a in attrs:
            if any(l[0] == a for l in closed):
                return False
            for v in self.attrs[a]:
                if self.closure(closed | {(a, v)}) is None:
                    return False
        return True


def check_witness_strong(M, A):
    section("1b. The witness under the stronger openness requirement (every value of a blanked attribute admissible)")
    MS = StrongModel(M.attrs, M.laws, dep={'y': {'s'}})
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]
    for A2, label in ((A, "A = {s}"), ({lit('s', True), lit('x', False)}, "A' = {s, ~x}")):
        for sc in SCOPES:
            for name, ante in (("x", X), ("x & y", XY)):
                iu = [fmt_set(I) for I in M.reopen(A2, M.targets(ante), sc)]; istr = [fmt_set(I) for I in MS.reopen(A2, MS.targets(ante), sc)]
                pu = [fmt_world(M, w) for w in M.perturb(A2, ante, sc)]; pstr = [fmt_world(MS, w) for w in MS.perturb(A2, ante, sc)]
                assert iu == istr and pu == pstr, (label, sc, name)
        print(f"  {label:14s}: intermediates and pockets identical under both requirements at every scope, for x and for x & y")
    T = Model({'q': (1, 2, 3), 'r': (0, 1)}, laws=[{('r', 1), ('q', 3)}], dep={})
    TS = StrongModel({'q': (1, 2, 3), 'r': (0, 1)}, laws=[{('r', 1), ('q', 3)}], dep={})
    A3 = {('r', 1)}
    iu = TS.reopen(A3, ['q']); ir = T.reopen(A3, ['q'])
    print(f"  three-valued example (r = 1 stated, {{r = 1, q = 3}} invalid, no declared dependencies): unresolved grade -> intermediates {[fmt_set(I) for I in ir]},"
          f" pockets under q in {{1, 2}}: {[fmt_world(T, w) for w in T.perturb(A3, [('q', (1, 2))])]}; stronger requirement -> {'INFEASIBLE' if not iu else iu}")
    assert ir and not iu
    print("  => the two requirements are different operations (the three-valued example is feasible under one and infeasible under the other);")
    print("     the principal countermodel satisfies both, so the non-preferentiality result does not depend on the weaker grade.")


def check_streetlight():
    section("2. The streetlight: declared Dep, protected evidence, infeasibility  (r = red, t = stopped; law r -> t)")
    dep = {'t': {'r'}}                                                      # stopping rests on the light
    for label, A in [("green stated, proceeding recorded: A = {~r, ~t}", {lit('r', False), lit('t', False)}),
                     ("green derived from the proceeding record: A = {~t}", {lit('t', False)})]:
        M = Model({'r': B, 't': B}, laws=[{lit('r', True), lit('t', False)}], dep=dep)
        print(f"  {label}; closure {fmt_set(M.closure(frozenset(A)))}; grounds of r: {M.grounds(A, 'r')}, dependents of r: {M.dependents(A, 'r')}")
        for sc in SCOPES:
            inters = M.reopen(A, ['r'], sc)
            P = M.perturb(A, [('r', (True,))], sc)
            print(f"     {sc:14s}: " + ("INFEASIBLE (protected content entails ~r)" if not inters else f"intermediates {[fmt_set(I) for I in inters]} -> pockets under r: {[fmt_world(M, w) for w in P]}"))
        assert not M.reopen(A, ['r'], 'evidential') and M.reopen(A, ['r'], 'unidirectional')
        assert M.would(A, [('r', (True,))], {lit('t', True)}, 'unidirectional')
        nr = M.reopen(A, ['r'], 'evidential', retention=False)
        print(f"     without protection (retention off): intermediates {[fmt_set(I) for I in nr]} -> feasible; the protection is what makes the evidential scope infeasible")
    print("  => the proceeding record is a declared dependent of the light, not a ground: protected at the evidential-minimal scope,")
    print("     where its closure with the law excludes red; cleared as posterity at the causal scopes, where had-it-been-red yields stopped.")


def check_cut_failure():
    section("2b. Cut without nesting (Proposition): priorities keep the generalization p over the particular r")
    M = Model({'p': B, 'r': B, 'x': B, 'y': B},
              laws=[{lit('p', True), lit('y', False)},                   # p -> y
                    {lit('p', True), lit('r', True), lit('x', True)}],   # {p, r, x} invalid
              dep={'y': {'p'}, 'x': {'p', 'r'}})                          # declared: p the sole ground of y; p and r the joint grounds of x
    A = {lit('p', True), lit('r', True)}
    print("  declared grounds: y rests on p; x rests on p and r; the priority keeps the generalization p over the particular r")
    inters = M.reopen(A, ['x'])
    print("  reopening x, tie-keeping maxima:", [fmt_set(I) for I in inters])
    keep_p = [I for I in inters if lit('p', True) in I]
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]
    px = sorted({w for I in keep_p for w in M.completions(I | {lit('x', True)})}, key=sorted)
    pxy = M.perturb(A, XY)
    print("  priority selects:", [fmt_set(I) for I in keep_p], "-> pockets under x:", [fmt_world(M, w) for w in px])
    print("  reopening x & y:", [fmt_set(I) for I in M.reopen(A, ['x', 'y'])], "-> pockets:", [fmt_world(M, w) for w in pxy])
    xy_ = all(lit('y', True) in w for w in px); xyr = all(lit('r', True) in w for w in pxy); xr = all(lit('r', True) in w for w in px)
    print(f"  x |~ y: {xy_} | x&y |~ r: {xyr} | x |~ r: {xr} (x |~ ~r: {all(lit('r', False) in w for w in px)})")
    assert xy_ and xyr and not xr
    print("  => Cut fails where the priorities select among inclusion-incomparable maximal restrictions.")
    print("     Branch-wise union: the two tied intermediates' restated contents are jointly inconsistent"
          f" ({fmt_set(M.closure(inters[0] | {lit('x', True)}))} vs {fmt_set(M.closure(inters[1] | {lit('x', True)}))}); their pockets are collected separately.")


def check_three_attributes():
    section("3. Minimality: a three-attribute Cautious Monotony counterexample (law z -> y; A states z)")
    M = Model({'x': B, 'y': B, 'z': B}, laws=[{lit('z', True), lit('y', False)}], dep={'y': {'z'}})   # declared: z the sole ground of y
    A = {lit('z', True)}
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]
    print("  pockets of pi_x  :", [fmt_world(M, w) for w in M.perturb(A, X)])
    print("  pockets of pi_x&y:", [fmt_world(M, w) for w in M.perturb(A, XY)])
    ok = M.would(A, X, {lit('y', True)}) and M.would(A, X, {lit('z', True)}) and not M.would(A, XY, {lit('z', True)})
    print("  x |~ y, x |~ z, x&y |/~ z :", ok)
    assert ok
    print("  => three attributes suffice; the four-attribute witness is not the smallest instance.")
    section("3b. Cautious Monotony failure through a cleared dependent (no laws; z declared to rest on y; unidirectional scope)")
    M2 = Model({'x': B, 'y': B, 'z': B}, laws=[], dep={'z': {'y'}})
    A2 = {lit('y', True), lit('z', True)}
    for sc in SCOPES:
        px = M2.perturb(A2, X, sc); pxy = M2.perturb(A2, XY, sc)
        print(f"  {sc:14s}: pi_x {[fmt_world(M2, w) for w in px]} | pi_x&y {[fmt_world(M2, w) for w in pxy]} | x|~y {M2.would(A2, X, {lit('y', True)}, sc)}, x|~z {M2.would(A2, X, {lit('z', True)}, sc)}, x&y|~z {M2.would(A2, XY, {lit('z', True)}, sc)}")
    assert M2.would(A2, XY, {lit('z', True)}, 'evidential') and not M2.would(A2, XY, {lit('z', True)}, 'unidirectional')
    print("  => at the unidirectional scope reopening x & y clears z as y's dependent; Cautious Monotony fails although y has no grounds.")


def check_lle(M, A):
    global NORMALIZE
    section("4. Left Logical Equivalence: x versus x & (y or ~y) on the witness")
    X = [('x', (True,))]; XT = [('x', (True,)), ('y', (True, False))]
    for norm in (False, True):
        NORMALIZE = norm
        print(f"  NORMALIZE={norm!s:5s}: targets of x&(y|~y) = {M.targets(XT)};  x&(y|~y) |~ z : {M.would(A, XT, {lit('z', True)})}  (x |~ z : {M.would(A, X, {lit('z', True)})})")
    NORMALIZE = True
    print("  => un-normalized, the unrestricted conjunct reopens y and LLE fails; normalized, it contributes no target and LLE holds.")


def check_or_exhaustive(M, A):
    section("4b. Or with an exhaustive disjunction (normalization removes the target)")
    Z = {lit('z', True)}
    full = [('x', (True, False))]
    print("  targets of (x or ~x):", M.targets(full), "-> perturbation = standing residue:", [fmt_world(M, w) for w in M.perturb(A, full)])
    print("  x |~ z:", M.would(A, [('x', (True,))], Z), "| ~x |~ z:", M.would(A, [('x', (False,))], Z), "| (x or ~x) |~ z:", M.would(A, full, Z))
    print("  => Or's hypothesis fails here (~x does not yield z), consistently with the standing residue not yielding z; the random test counts the exhaustive instances.")


def check_comparators(M, A, X, XY):
    section("5. Comparators on the witness (Table: neighboring semantics)")
    z, y = {lit('z', True)}, {lit('y', True)}
    rows = []
    rows.append(("This paper, dual-peg reading", M.would(A, X, y), M.would(A, X, z), M.would(A, XY, z)))
    rows.append(("This paper, Boolean reading", boolean_reading(M, A, X, y), boolean_reading(M, A, X, z), boolean_reading(M, A, XY, z)))
    rows.append(("Maximal-consistent-facts comparator", premise_max(M, A, X, y), premise_max(M, A, X, z), premise_max(M, A, XY, z)))
    r1, w1 = basis_retract(M, A, X, y); r2, _ = basis_retract(M, A, X, z); r3, _ = basis_retract(M, A, XY, z)
    rows.append(("Basis retraction, Veltman-type", r1, r2, r3))
    rows.append(("AGM revision (expansion)", agm_expansion(M, A, X, y), agm_expansion(M, A, X, z), agm_expansion(M, A, XY, z)))
    p1, _ = pearl_structural(A, X, y); p2, _ = pearl_structural(A, X, z); p3, _ = pearl_structural(A, XY, z)
    rows.append(("Pearl, the model in the text", p1, p2, p3))
    u1, uw = winslett_update(M, A, X, y); u2, _ = winslett_update(M, A, X, z); u3, _ = winslett_update(M, A, XY, z)
    rows.append(("Update (Winslett)", u1, u2, u3))
    yn = lambda b: {True: 'yes', False: 'no', None: '-'}[b]
    print(f"  {'semantics':38s} x->y  x->z  x&y->z  Cautious Monotony")
    for name, a, b, c in rows:
        cm = 'fails' if (a and b and not c) else ('holds' if (a and b and c) else 'not instantiated')
        print(f"  {name:38s} {yn(a):5s} {yn(b):5s} {yn(c):7s} {cm}")
    print(f"     basis-retraction worlds reached under x: {[fmt_world(M, w) for w in w1]}")
    print(f"     Winslett update by x: {[fmt_world(M, w) for w in uw]}")
    expected = [(True, True, False), (True, True, True), (True, True, True), (False, False, False), (True, True, True), (True, True, True), (True, False, False)]
    assert [(a, b, c) for _, a, b, c in rows] == expected
    print("  => the maximal-consistent-facts comparator, AGM and Pearl keep s and validate the instance; basis retraction and Winslett's")
    print("     update do not reach it (the former affirms neither x->y nor x->z, the latter not x->z); the dual-peg reading alone fails it.")


def check_comparators_known_false(M):
    section("5b. The comparison where the antecedent is known false: A' = Cl({s, ~x}) (kept apart from the table)")
    A2 = {lit('s', True), lit('x', False)}
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]
    z, y = {lit('z', True)}, {lit('y', True)}
    print("  closure of A':", fmt_set(M.closure(frozenset(A2))), "| the antecedent x contradicts the state")
    for sc in SCOPES:
        print(f"  {sc:14s}: reopen x -> {[fmt_set(I) for I in M.reopen(A2, ['x'], sc)]} (~x cleared, s retained); pi_x {[fmt_world(M, w) for w in M.perturb(A2, X, sc)]};"
              f" pi_x&y {[fmt_world(M, w) for w in M.perturb(A2, XY, sc)]}")
        assert M.would(A2, X, y, sc) and M.would(A2, X, z, sc) and not M.would(A2, XY, z, sc)
    rows = []
    rows.append(("This paper, dual-peg reading", M.would(A2, X, y), M.would(A2, X, z), M.would(A2, XY, z)))
    rows.append(("Maximal-consistent-facts comparator", premise_max(M, A2, X, y), premise_max(M, A2, X, z), premise_max(M, A2, XY, z)))
    r1, w1 = basis_retract(M, A2, X, y); r2, _ = basis_retract(M, A2, X, z); r3, _ = basis_retract(M, A2, XY, z)
    rows.append(("Basis retraction, Veltman-type", r1, r2, r3))
    rows.append(("AGM revision (expansion)", agm_expansion(M, A2, X, y), agm_expansion(M, A2, X, z), agm_expansion(M, A2, XY, z)))
    p1, _ = pearl_structural(A2, X, y); p2, _ = pearl_structural(A2, X, z); p3, _ = pearl_structural(A2, XY, z)
    rows.append(("Pearl, the model in the text", p1, p2, p3))
    u1, uw = winslett_update(M, A2, X, y); u2, _ = winslett_update(M, A2, X, z); u3, _ = winslett_update(M, A2, XY, z)
    rows.append(("Update (Winslett)", u1, u2, u3))
    yn = lambda b: {True: 'yes', False: 'no', None: '-'}[b]
    print(f"  {'semantics':38s} x->y  x->z  x&y->z  Cautious Monotony")
    for name, a, b, c in rows:
        cm = '-' if None in (a, b, c) else ('fails' if (a and b and not c) else ('holds' if (a and b and c) else 'not instantiated'))
        print(f"  {name:38s} {yn(a):5s} {yn(b):5s} {yn(c):7s} {cm}")
    print(f"     basis-retraction worlds reached under x: {[fmt_world(M, w) for w in w1]}")
    print(f"     Winslett update by x: {[fmt_world(M, w) for w in uw]}")
    expected = [(True, True, False), (True, True, True), (False, False, False), (None, None, None), (True, True, True), (True, False, False)]
    assert [(a, b, c) for _, a, b, c in rows] == expected
    print("  => on A' the operator's three verdicts are unchanged at every scope and Cautious Monotony fails as before; the Veltman-type")
    print("     clause affirms none of the three; Winslett affirms x->y only; the comparator and Pearl affirm all three; AGM expansion is")
    print("     inapplicable (the antecedent contradicts the belief set, so revision rather than expansion is required: not computed).")


def check_inference_patterns(M, A):
    section("6. Antecedent strengthening, contraposition and transitivity")
    X = [('x', (True,))]; XY = [('x', (True,)), ('y', (True,))]; NY = [('y', (False,))]
    print("  strengthening on the witness: x |~ z", M.would(A, X, {lit('z', True)}), "| x&y |~ z", M.would(A, XY, {lit('z', True)}))
    print("  contraposition on the witness: x |~ y", M.would(A, X, {lit('y', True)}), "| ~y |~ ~x", M.would(A, NY, {lit('x', False)}),
          "| pockets under ~y:", [fmt_world(M, w) for w in M.perturb(A, NY)])
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
    n = rng.choice([4, 5])
    names = ['a', 'b', 'c', 'd', 'e'][:n]
    attrs = {a: B for a in names}
    tri = rng.choice(names); attrs[tri] = (0, 1, 2)                 # one three-valued attribute
    lits = [(a, v) for a in names for v in attrs[a]]
    laws = []
    for _ in range(rng.randint(1, 4)):
        k = rng.choice([2, 3])
        law = set(rng.sample(lits, k))
        if len({a for a, _ in law}) == k:
            laws.append(law)
    M = Model(attrs, laws)                                         # entailment-derived Dep
    if not M.worlds:
        return None
    basic = set()
    for a in rng.sample(names, rng.randint(1, max(1, n - 2))):
        basic.add((a, rng.choice(attrs[a])))
    if M.closure(frozenset(basic)) is None:
        return None
    return M, basic, tri


def random_tests(n_models=3000, seed=20261008):
    section(f"7. Random finite, fully supported models ({n_models} draws, seed {seed}; entailment-derived Dep; evidential scope)")
    rng = random.Random(seed)
    st = dict(models=0, cm_instances=0, cm_fail=0, prop_agree=0, cut_nested=0, cut_fail=0, mono=0, mono_fail=0,
              or_inst=0, or_fail=0, orx_inst=0, orx_fail=0, lemma_blank_viol=0)
    for _ in range(n_models):
        rm = random_model(rng)
        if rm is None:
            continue
        M, basic, tri = rm; st['models'] += 1
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
                        if not all(M.blank_on(J, [xa, ya]) for J in IXY):
                            st['lemma_blank_viol'] += 1               # Lemma (Conjunctive reopening): blankness claim
                        nested = all(any(J <= I for J in IXY) for I in IX)
                        if nested:
                            st['mono'] += 1
                            if not set(PX) <= set(PXY):
                                st['mono_fail'] += 1
                        for za in M.names:
                            if za in (xa, ya):
                                continue
                            for zv in M.attrs[za]:
                                Z = {(za, zv)}
                                xz = all(Z <= w for w in PX); xyz = all(Z <= w for w in PXY)
                                if nested and xyz:                   # Cut
                                    st['cut_nested'] += 1
                                    if not xz:
                                        st['cut_fail'] += 1
                                if xz and len(IX) == 1 and len(IXY) == 1 and IXY[0] <= IX[0]:
                                    st['cm_instances'] += 1           # Proposition (where CM fails)
                                    D = IX[0] - IXY[0]
                                    predicted = any(not (D <= w) and not (Z <= w) for w in PXY)
                                    if not xyz:
                                        st['cm_fail'] += 1
                                    if predicted == (not xyz):
                                        st['prop_agree'] += 1
                # Or: a disjunction within one attribute against its disjuncts
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
                                st['or_inst'] += 1
                                if not all(Z <= w for w in POR):
                                    st['or_fail'] += 1
        # Or, exhaustive: all three values of the three-valued attribute against the standing residue
        Ps = [M.perturb(basic, [(tri, (v,))]) for v in M.attrs[tri]]
        if all(Ps):
            PALL = M.perturb(basic, [(tri, tuple(M.attrs[tri]))])
            for za in M.names:
                if za == tri:
                    continue
                for zv in M.attrs[za]:
                    Z = {(za, zv)}
                    if all(all(Z <= w for w in P) for P in Ps):
                        st['orx_inst'] += 1
                        if not all(Z <= w for w in PALL):
                            st['orx_fail'] += 1
    print(f"  valid models: {st['models']}")
    print(f"  Lemma (Conjunctive reopening), blankness of every conjunctive intermediate on both constituents: violations {st['lemma_blank_viol']}")
    print(f"  Proposition (where Cautious Monotony fails): {st['cm_instances']} nested singleton instances, "
          f"criterion agrees with the operator in {st['prop_agree']}, Cautious Monotony fails in {st['cm_fail']}")
    print(f"  Cut, nested instances: {st['cut_nested']}, failures {st['cut_fail']}")
    print(f"  pocket monotonicity, nested instances: {st['mono']}, failures {st['mono_fail']}")
    print(f"  Or, instances: {st['or_inst']}, failures {st['or_fail']}; exhaustive disjunction (no target after normalization): {st['orx_inst']} instances, failures {st['orx_fail']}")
    assert st['prop_agree'] == st['cm_instances'] and st['cut_fail'] == 0 and st['mono_fail'] == 0 and st['or_fail'] == 0 and st['orx_fail'] == 0 and st['lemma_blank_viol'] == 0
    return st


if __name__ == "__main__":
    M, A, X, XY = check_witness()
    check_witness_strong(M, A)
    check_streetlight()
    check_cut_failure()
    check_three_attributes()
    check_lle(M, A)
    check_or_exhaustive(M, A)
    check_comparators(M, A, X, XY)
    check_comparators_known_false(M)
    check_inference_patterns(M, A)
    random_tests()
    print("\nAll checks passed.")
