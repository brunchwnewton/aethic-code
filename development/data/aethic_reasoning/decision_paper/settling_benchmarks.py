#!/usr/bin/env python3
"""settling_benchmarks.py -- reference computations for
"Newcomb's Problem Without a Fixed Past: A Decision Rule From Observer-Indexed Determinacy".

Pure Python 3 (standard library only). Run with no arguments; the output should match
settling_benchmarks_expected_output.txt.

THE OPERATOR (Definition: the settling rule), on finite acyclic factor models
  variables in topological order, each with parents and a kernel table;
  the act C with its production entry P0(c | pa(C));
  a coupling = the kernel of a child of C, carrying a mode set m(e);
  inputs: the evaluation mode mu, stated evidence E, candidate act a.
  (1) Fix:     the production entry is replaced by the point mass at a.
  (2) Retain:  every coupling with mu in m(e) is kept, reading C = a.
  (3) Detach:  the couplings with mu not in m(e) are replaced JOINTLY by the kernel of
               their outputs O given the act's parents and their other parents Z,
               computed from the original kernels with the act integrated out under
               the original production entry.
  Evidence E is then conditioned on; the settled law Q_a is the law of the payoff-relevant
  attributes; an act is inadmissible when its settled residue has no admissible pocket.

AUXILIARY-VARIABLE REPRESENTATION (checked numerically below)
  Step (3) equals: add one copy C* with the original production kernel P0(c* | pa(C)),
  fix C = a, let retained couplings read C and detached couplings read the SAME C*,
  leave every other kernel unchanged, condition on E, marginalize C*.  With an
  independent full-support prior on C in that augmented graph, Q_a(Y) = P^(Y | C = a, E),
  and d-separation of Y from C given E in the augmented graph is sufficient for
  across-act invariance.

COMPARATORS on the same models and information
  EDT:            P(Y | C = a, E) in the observational law (every coupling kept, C's
                  parents kept: conditioning, no fix)
  fixed-marginal: the causal theorist's rule in this encoding, every coupling detached
                  (the prediction keeps its marginal)
"""
from itertools import product
from fractions import Fraction as F

MODES = ('deliberation', 'habit', 'randomizer')


# ------------------------------------------------------------------ factor models
class FactorModel:
    """variables: list of (name, values, parents, kernel) in topological order;
    kernel: dict mapping a tuple of parent values -> dict value -> probability"""
    def __init__(self, variables, act, modes=None):
        self.vars = variables
        self.names = [v[0] for v in variables]
        self.spec = {v[0]: v for v in variables}
        self.act = act
        self.modes = dict(modes or {})            # child of C -> set of modes in which it binds

    def joint(self, overrides=None, extra=None):
        """the joint law as {assignment dict: prob}; overrides: name -> kernel replacing the
        variable's own; extra: additional variables appended (name, values, parents, kernel)"""
        variables = self.vars + (extra or [])
        overrides = overrides or {}
        law = {}
        for vals in product(*[v[1] for v in variables]):
            w = dict(zip([v[0] for v in variables], vals)); p = F(1)
            for name, values, parents, kernel in variables:
                k = overrides.get(name, kernel)
                p *= k[tuple(w[q] for q in parents)].get(w[name], F(0))
                if p == 0:
                    break
            if p:
                law[frozenset(w.items())] = p
        return law

    @staticmethod
    def condition(law, evidence):
        sub = {w: p for w, p in law.items() if all((k, v) in w for k, v in evidence.items())}
        Z = sum(sub.values())
        return ({w: p / Z for w, p in sub.items()}, Z) if Z else ({}, F(0))

    @staticmethod
    def marginal(law, name):
        out = {}
        for w, p in law.items():
            v = dict(w)[name]; out[v] = out.get(v, F(0)) + p
        return out

    # --- the settling rule
    def settle(self, a, mu, evidence):
        """returns (settled law over all variables, normalizer); normalizer 0 = inadmissible"""
        C = self.act
        name, values, parents, kernel = self.spec[C]
        point = {pa: {v: F(1) if v == a else F(0) for v in values} for pa in kernel}
        detached = [v for v in self.names if C in self.spec[v][2] and mu not in self.modes.get(v, set())]
        extra, overrides = [], {C: point}
        if detached:
            # shared auxiliary copy with the original production entry; detached couplings read it
            extra.append((C + '*', values, parents, kernel))
            for v in detached:
                vn, vv, vp, vk = self.spec[v]
                overrides[v] = vk                                    # same table, parents renamed
                self.spec[v] = (vn, vv, [C + '*' if q == C else q for q in vp], vk)
        variables = [self.spec[v] for v in self.names]
        law = {}
        for vals in product(*[v[1] for v in variables], *[e[1] for e in extra]):
            allnames = self.names + [e[0] for e in extra]
            w = dict(zip(allnames, vals)); p = F(1)
            for nm, vv, vp, vk in variables + extra:
                k = overrides.get(nm, vk)
                p *= k[tuple(w[q] for q in vp)].get(w[nm], F(0))
                if p == 0:
                    break
            if p:
                law[frozenset(w.items())] = p
        for v in detached:                                           # restore the model
            vn, vv, vp, vk = self.spec[v]
            self.spec[v] = (vn, vv, [C if q == C + '*' else q for q in vp], vk)
        return self.condition(law, evidence)

    def settled_marginal(self, a, mu, evidence, name):
        law, Z = self.settle(a, mu, evidence)
        return (self.marginal(law, name) if Z else None), Z

    def edt(self, a, evidence, name):
        """EDT: conditioning on the act in the observational law"""
        law, Z = self.condition(self.joint(), {**evidence, self.act: a})
        return (self.marginal(law, name) if Z else None), Z

    def expected(self, dist, u):
        return sum(p * u(v) for v, p in dist.items())


def pct(x):
    return f"{float(x):.4f}"


def section(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


# ------------------------------------------------------------------ benchmarks
M, T = 10**6, 10**3


def newcomb_model(eps, modes):
    """act C in {one, two} with a fair production entry; box B child of C under the
    branch-conditional accuracy law (B = full iff predicted one-box)"""
    e = F(eps)
    return FactorModel([
        ('C', ('one', 'two'), [], {(): {'one': F(1, 2), 'two': F(1, 2)}}),
        ('B', ('full', 'empty'), ['C'], {('one',): {'full': 1 - e, 'empty': e}, ('two',): {'full': e, 'empty': 1 - e}}),
    ], 'C', modes)


def payoff(a, b):
    return (M if b == 'full' else 0) + (T if a == 'two' else 0)


def check_opaque():
    section("1. Opaque Newcomb: retained branch-conditional accuracy vs the fixed-marginal rule")
    for eps in (F(1, 100), F(4995, 10000), F(1, 2)):
        Mdl = newcomb_model(eps, {'B': set(MODES)})            # act-robust: binds in every mode
        vals = {}
        for a in ('one', 'two'):
            d, _ = Mdl.settled_marginal(a, 'deliberation', {}, 'B')
            vals[a] = Mdl.expected(d, lambda b, a=a: payoff(a, b))
        Mfix = newcomb_model(eps, {'B': set()})                   # nonbinding: the prediction keeps its marginal
        fix = {a: Mfix.expected(Mfix.settled_marginal(a, 'deliberation', {}, 'B')[0], lambda b, a=a: payoff(a, b)) for a in ('one', 'two')}
        print(f"  eps = {pct(eps)}: retained accuracy  V(one) = {float(vals['one']):>12,.1f}  V(two) = {float(vals['two']):>12,.1f}  -> {'one-box' if vals['one'] > vals['two'] else 'two-box' if vals['two'] > vals['one'] else 'tie'}"
              f" | fixed marginal: V(one) = {float(fix['one']):>10,.1f} V(two) = {float(fix['two']):>10,.1f} -> two-box")
    thr = F(M - T, 2 * M)
    print(f"  threshold: one-box iff eps < (M - t)/(2M) = {pct(thr)}")
    edt, _ = newcomb_model(F(1, 100), {}).edt('one', {}, 'B')
    print(f"  EDT on the same model (conditioning on the act): P(full | one) = {pct(edt['full'])} -> one-box, agreeing with the retained-accuracy settling")
    assert thr == F(4995, 10000)


def check_habit_reader():
    section("2. Separating example against EDT: the habit-reading predictor (accuracy stated as robust only to habit)")
    Mdl = newcomb_model(F(1, 100), {'B': {'habit'}})
    for mu in ('habit', 'deliberation'):
        vals = {a: Mdl.expected(Mdl.settled_marginal(a, mu, {}, 'B')[0], lambda b, a=a: payoff(a, b)) for a in ('one', 'two')}
        print(f"  settling, act produced by {mu:13s}: V(one) = {float(vals['one']):>10,.1f}  V(two) = {float(vals['two']):>10,.1f}  -> {'one-box' if vals['one'] > vals['two'] else 'two-box'}")
    e = {a: Mdl.expected(Mdl.edt(a, {}, 'B')[0], lambda b, a=a: payoff(a, b)) for a in ('one', 'two')}
    print(f"  EDT (the predictor's record is the observational law):   V(one) = {float(e['one']):>10,.1f}  V(two) = {float(e['two']):>10,.1f}  -> one-box")
    print("  => same model, same record: the deliberating agent two-boxes under the rule and one-boxes under EDT;")
    print("     the mode-indexed binding set is the input that separates them.")


def check_transparent():
    section("3. Transparent boxes (shared model): policy values, settling on the observed box, the endpoint")
    for eps in (F(1, 100), F(1, 10)):
        e = eps
        one_policy = (1 - e) * M + e * T; two_policy = (1 - e) * T + e * (M + T)
        print(f"  eps = {pct(e)}: ex-ante policy values  one-box policy {float(one_policy):,.0f}  two-box policy {float(two_policy):,.0f}  difference {float(one_policy - two_policy):,.0f}"
              f"  (FDT one-boxes iff eps < (M-t)/(2M-t) = {pct(F(M - T, 2 * M - T))})")
    # the post-observation state: the act at the full box is the policy component pi_full;
    # the prediction is a binding coupling of pi_full; B = full is stated
    e = F(1, 100)
    Mdl = FactorModel([
        ('PF', ('one', 'two'), [], {(): {'one': F(1, 2), 'two': F(1, 2)}}),                  # pi_full, the act settled at the full box
        ('Pred', ('one', 'two'), ['PF'], {('one',): {'one': 1 - e, 'two': e}, ('two',): {'one': e, 'two': 1 - e}}),
        ('B', ('full', 'empty'), ['Pred'], {('one',): {'full': F(1)}, ('two',): {'empty': F(1)}}),
    ], 'PF', {'Pred': set(MODES)})
    vals = {}
    for a in ('one', 'two'):
        d, Z = Mdl.settled_marginal(a, 'deliberation', {'B': 'full'}, 'B')
        vals[a] = Mdl.expected(d, lambda b, a=a: payoff(a, b)) if Z else None
    print(f"  eps = 0.01, full box stated, settling pi_full: V(one) = {float(vals['one']):,.0f}  V(two) = {float(vals['two']):,.0f}  -> two-box (every mismatch pocket positive)")
    # the perfect endpoint: the mismatch is jointly invalid, two-boxing with the full box stated is inadmissible
    Mp = FactorModel([
        ('PF', ('one', 'two'), [], {(): {'one': F(1, 2), 'two': F(1, 2)}}),
        ('Pred', ('one', 'two'), ['PF'], {('one',): {'one': F(1)}, ('two',): {'two': F(1)}}),
        ('B', ('full', 'empty'), ['Pred'], {('one',): {'full': F(1)}, ('two',): {'empty': F(1)}}),
    ], 'PF', {'Pred': set(MODES)})
    adm = {a: Mp.settled_marginal(a, 'deliberation', {'B': 'full'}, 'B')[1] for a in ('one', 'two')}
    print(f"  eps = 0, full box stated: normalizers one {float(adm['one'])}, two {float(adm['two'])} -> two-boxing inadmissible, one-box only")
    assert vals['two'] > vals['one'] and adm['two'] == 0 and adm['one'] > 0
    print("  => the act settled at the box is the policy component pi_full; settling it sets that component and leaves pi_empty as the policy had it.")


def check_lesion():
    section("4. The smoking lesion: Fix severs the act's parents; EDT separates where the resolve is not stated")
    Mdl = FactorModel([
        ('L', (1, 0), [], {(): {1: F(1, 10), 0: F(9, 10)}}),
        ('R', (1, 0), ['L'], {(1,): {1: F(9, 10), 0: F(1, 10)}, (0,): {1: F(1, 5), 0: F(4, 5)}}),
        ('C', ('smoke', 'refrain'), ['R'], {(1,): {'smoke': F(9, 10), 'refrain': F(1, 10)}, (0,): {'smoke': F(1, 10), 'refrain': F(9, 10)}}),
    ], 'C', {})
    u = lambda a: (lambda l: (1 if a == 'smoke' else 0) - 100 * l)
    for label, ev in [("resolve stated, R = 1", {'R': 1}), ("resolve blank", {})]:
        s = {a: Mdl.expected(Mdl.settled_marginal(a, 'deliberation', ev, 'L')[0], u(a)) for a in ('smoke', 'refrain')}
        e = {a: Mdl.expected(Mdl.edt(a, ev, 'L')[0], u(a)) for a in ('smoke', 'refrain')}
        pl = {a: Mdl.settled_marginal(a, 'deliberation', ev, 'L')[0][1] for a in ('smoke', 'refrain')}
        print(f"  {label:22s}: settled P(L) smoke {pct(pl['smoke'])} refrain {pct(pl['refrain'])} (invariant: {pl['smoke'] == pl['refrain']}) ->"
              f" V(smoke) = {float(s['smoke']):.2f} V(refrain) = {float(s['refrain']):.2f} -> smoke | EDT: V(smoke) = {float(e['smoke']):.2f} V(refrain) = {float(e['refrain']):.2f} -> {'smoke' if e['smoke'] > e['refrain'] else 'refrain'}")
    print("  => with the resolve stated and screening, EDT also smokes; with the resolve blank the rule smokes and EDT refrains.")


def check_egan():
    section("5. Egan's button: self-settled evaluation, the projected comparison flow, and a logistic variant")
    B, D = F(1), F(10); qc = B / (B + D); q0, q1 = F(1, 20), F(1, 2)
    V_press = B - (B + D) * q1
    print(f"  B = {B}, D = {D}, q_c = {pct(qc)}, q0 = {pct(q0)}, q1 = {pct(q1)}: V(press) at its own settled state = {float(V_press):.3f}, V(refrain) = 0 -> refrain")
    q = lambda r: q0 + r * (q1 - q0)                                  # affine law, by total probability
    r_star = (qc - q0) / (q1 - q0)
    print(f"  projected additive flow r' = B - (B+D) q(r), affine q: interior fixed point r* = {pct(r_star)}; the flow is positive below and negative above (globally attracting)")
    # logistic variant: both endpoints are fixed points as well
    g = lambda r: r * (1 - r) * (B - (B + D) * q(r))
    print(f"  logistic variant r' = r(1-r)[B - (B+D) q(r)]: g(0) = {g(F(0))}, g(1) = {g(F(1))}, g(r*) = {g(r_star)} -> endpoints fixed too; interior attracts the interior")
    print("  => the uniqueness statement belongs to the projected additive flow, not to deliberational dynamics as such.")
    assert V_press < 0 and g(F(0)) == 0 and g(F(1)) == 0 and g(r_star) == 0


def check_auxiliary_representation():
    section("6. Joint detachment = marginalizing one shared auxiliary copy; separate copies destroy dependence")
    # the appendix's example: fair act C without inputs, two nonbinding couplings Y1 := C, Y2 := C, Y1 = 1 stated
    Mdl = FactorModel([
        ('C', (0, 1), [], {(): {0: F(1, 2), 1: F(1, 2)}}),
        ('Y1', (0, 1), ['C'], {(0,): {0: F(1)}, (1,): {1: F(1)}}),
        ('Y2', (0, 1), ['C'], {(0,): {0: F(1)}, (1,): {1: F(1)}}),
    ], 'C', {})
    for a in (0, 1):
        d, _ = Mdl.settled_marginal(a, 'deliberation', {'Y1': 1}, 'Y2')
        print(f"  settle C = {a}, Y1 = 1 stated: P(Y2 = 1) = {pct(d[1])} via the shared copy (joint detachment)")
    # explicit joint-detachment sum, as in Definition: K(o) = sum_c P0(c) prod_e f_e(o_e | c)
    K = {}
    for c in (0, 1):
        for y1, y2 in product((0, 1), (0, 1)):
            K[(y1, y2)] = K.get((y1, y2), F(0)) + F(1, 2) * (1 if y1 == c else 0) * (1 if y2 == c else 0)
    print(f"  explicit sum: K(y1, y2) = {{(0,0): {pct(K[(0,0)])}, (1,1): {pct(K[(1,1)])}, mixed: 0}} -> P(Y2 = 1 | Y1 = 1) = 1, as above")
    # separate copies: each coupling reads its own copy -> Y1, Y2 independent fair bits
    sep = F(1, 2)
    print(f"  separate copies would give P(Y2 = 1 | Y1 = 1) = {pct(sep)}: the dependence the shared act induced is lost")
    # d-separation sufficient condition, on Newcomb: nonbinding B reads C* (d-separated from C) -> invariant; binding reads C -> varies
    for label, modes in [("B nonbinding (reads C*)", set()), ("B binding (reads C)", set(MODES))]:
        Mn = newcomb_model(F(1, 100), {'B': modes})
        ds = [Mn.settled_marginal(a, 'deliberation', {}, 'B')[0]['full'] for a in ('one', 'two')]
        print(f"  Newcomb, {label:24s}: Q_one(full) = {pct(ds[0])}, Q_two(full) = {pct(ds[1])} -> {'invariant' if ds[0] == ds[1] else 'act-dependent'}")
    print("  => Q_a(Y) = P^(Y | C = a, E) in the augmented graph; d-separation of Y from C given E there is sufficient for invariance.")


def check_dominance_lemma():
    section("7. Factorization lemma: proportional unnormalized settled laws <=> equal settled laws")
    h = {'y1': F(3, 10), 'y2': F(7, 10)}
    tilde = {'a': {y: F(2) * p for y, p in h.items()}, 'b': {y: F(5) * p for y, p in h.items()}}
    norm = {a: {y: p / sum(t.values()) for y, p in t.items()} for a, t in tilde.items()}
    print(f"  tilde Q_a = 2h, tilde Q_b = 5h -> normalized laws equal: {norm['a'] == norm['b']}; conversely equal laws with positive finite normalizers are proportional.")
    assert norm['a'] == norm['b']


def check_collider():
    section("8. Why statedness does not block a path: a stated binding output reading the act and Y")
    half = {(): {0: F(1, 2), 1: F(1, 2)}}
    S_kernel = {(c, y): ({1: F(9, 10), 0: F(1, 10)} if c == y else {1: F(1, 10), 0: F(9, 10)})
                for c in (0, 1) for y in (0, 1)}
    for label, modes in [("S binding (reads C)", {'S': set(MODES)}), ("S nonbinding (reads C*)", {'S': set()})]:
        M = FactorModel([('C', (0, 1), (), half), ('Y', (0, 1), (), half), ('S', (0, 1), ('C', 'Y'), S_kernel)],
                        act='C', modes=modes)
        rows = []
        for a in (0, 1):
            law, Z = M.settle(a, 'deliberation', {'S': 1})
            rows.append((Z, M.marginal(law, 'Y').get(1, F(0))))
        print(f"  {label:24s}: normalizers {pct(rows[0][0])}, {pct(rows[1][0])}; Q_0(Y=1) = {pct(rows[0][1])}, Q_1(Y=1) = {pct(rows[1][1])}"
              f" -> {'act-dependent (collider C -> S <- Y opened by conditioning on S)' if rows[0][1] != rows[1][1] else 'invariant (S reads C*, path closed)'}")
        if modes['S']:
            assert rows[0][1] == F(1, 10) and rows[1][1] == F(9, 10) and rows[0][0] == F(1, 2)
        else:
            assert rows[0][1] == rows[1][1] == F(1, 2)
    print("  => a stated attribute between the act and Y does not block the dependence; d-separation in the augmented graph decides.")


if __name__ == "__main__":
    check_opaque()
    check_habit_reader()
    check_transparent()
    check_lesion()
    check_egan()
    check_auxiliary_representation()
    check_dominance_lemma()
    check_collider()
    print("\nAll checks passed.")
