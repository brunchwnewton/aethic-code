#!/usr/bin/env python3
"""Supplement to "Causality from Indexed Information States": reference computations.

Run `python3 causality_checks.py` from the directory containing the five component scripts
(reichenbach_check.py, causal_rungs_check.py, causal_cf_check.py, nosignal_check.py,
regularity_check.py); the output should match causality_checks_expected_output.txt. Pure
Python 3, standard library, exact rational arithmetic; the component scripts are seeded.

Part A (this file): the three examples added in the October 2026 revision.
  A1. A setting-independent screener that is not Bell-local: lambda fair, a = lambda,
      P(b | x, y, lambda) = (1 + b lambda E_xy)/2 with E_xy = (-1)^{xy}/sqrt2 -- the outcomes
      factorize given lambda in every context, the marginals are unbiased and non-signaling,
      and CHSH = 2 sqrt 2; Bob's response depends on Alice's setting, so (D1)-(D3) fail.
  A2. A three-valued screener without a uniform relevance ordering: C uniform on three values,
      P(A=1|C) = (0.1, 0.5, 0.9), P(B=1|C) = (0.1, 0.9, 0.5); C screens, Cov(A,B) = 4/75 > 0,
      yet between the last two pockets A's probability rises while B's falls.
  A3. Two states with one probability table and different hard structure: X, Y fair bits with
      the mismatches at weight zero (soft), against the tie entry excluding them (hard). The
      probe stating a mismatch is admissible at zero weight in the first and structurally
      invalid in the second; adding an entry that excludes the matches leaves the first state
      with admissible total assignments and the second with none.
Part B: the component scripts, run in sequence (connectivity/separation/screening over 1,500
  random product-form states; settling = truncated factorization and the back-door adjustment
  over 1,500 random networks; counterfactual settling against a twin-world computation over
  3,000 random functional models; far-wing balance and the singlet; the regularity proposition
  over 600 random deterministic states).
"""
import itertools, math, runpy, sys
from fractions import Fraction as F

def section(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)

def check_screener_not_bell_local():
    section("A1. A setting-independent screener that is not Bell-local")
    s2 = math.sqrt(2)
    E = {(x, y): ((-1) ** (x * y)) / s2 for x in (0, 1) for y in (0, 1)}
    def p_a(a, lam): return 1.0 if a == lam else 0.0
    def p_b(b, x, y, lam): return (1 + b * lam * E[(x, y)]) / 2
    worst_fact = 0.0; worst_marg = 0.0
    for x, y in E:
        for a in (-1, 1):
            for b in (-1, 1):
                joint = sum(0.5 * p_a(a, lam) * p_b(b, x, y, lam) for lam in (-1, 1))
                worst_marg = max(worst_marg, abs(joint - (1 + a * b * E[(x, y)]) / 4))
                for lam in (-1, 1):   # factorization given lambda holds by construction; record it
                    worst_fact = max(worst_fact, abs(p_a(a, lam) * p_b(b, x, y, lam) - p_a(a, lam) * p_b(b, x, y, lam)))
    chsh = E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]
    pa = {(x, y): sum(sum(0.5 * p_a(1, lam) * p_b(b, x, y, lam) for lam in (-1, 1)) for b in (-1, 1)) for x, y in E}
    pb = {(x, y): sum(sum(0.5 * p_a(a, lam) * p_b(1, x, y, lam) for lam in (-1, 1)) for a in (-1, 1)) for x, y in E}
    print(f"  P(a,b|x,y) = (1 + ab E_xy)/4 reproduced: max error {worst_marg:.2e}")
    print(f"  marginals P(a=1|x,y) = {sorted(set(round(v, 12) for v in pa.values()))}, P(b=1|x,y) = {sorted(set(round(v, 12) for v in pb.values()))} (unbiased, non-signaling)")
    print(f"  CHSH = E00 + E01 + E10 - E11 = {chsh:.6f} = 2*sqrt(2) ({2 * s2:.6f})")
    dep = {y: [p_b(1, 0, y, 1), p_b(1, 1, y, 1)] for y in (0, 1)}
    print(f"  Bob's response given lambda=+1, P(b=1|x,y,lambda): y=0 -> {dep[0]}, y=1 -> {dep[1]}: depends on Alice's setting x")
    print("  => screening in every context by a setting-independent lambda; not Bell-local, so outside (D1)-(D3).")
    assert abs(chsh - 2 * s2) < 1e-12 and worst_marg < 1e-12

def check_three_valued_screener():
    section("A2. A three-valued screener: screens, positive covariance, no uniform relevance ordering")
    pA = [F(1, 10), F(1, 2), F(9, 10)]; pB = [F(1, 10), F(9, 10), F(1, 2)]
    EA = sum(pA) / 3; EB = sum(pB) / 3; EAB = sum(a * b for a, b in zip(pA, pB)) / 3
    cov = EAB - EA * EB
    print(f"  E[A] = {EA}, E[B] = {EB}, E[AB] = {EAB}, Cov(A,B) = {cov} (= 4/75: {cov == F(4, 75)})")
    print(f"  pockets c1 -> c2: P(A=1|C) {pA[1]} -> {pA[2]} (rises), P(B=1|C) {pB[1]} -> {pB[2]} (falls)")
    # covariance identity through conditional expectations (law of total covariance, within-pocket term zero)
    cov_between = sum((a - EA) * (b - EB) for a, b in zip(pA, pB)) / 3
    print(f"  Cov(E[A|C], E[B|C]) = {cov_between} = Cov(A,B): {cov_between == cov}")
    print("  => the covariance identity holds for every screener; the fork inequalities are the binary case.")
    assert cov == F(4, 75) and cov_between == cov

def check_two_states_one_table():
    section("A3. One probability table, two hard structures")
    vals = [(x, y) for x in (0, 1) for y in (0, 1)]
    # soft state: all four combinations admissible, mismatches at weight zero
    adm_soft = set(vals); w_soft = {(0, 0): F(1, 2), (1, 1): F(1, 2), (0, 1): F(0), (1, 0): F(0)}
    # hard state: the tie entry excludes the mismatches
    adm_hard = {(0, 0), (1, 1)}; w_hard = {(0, 0): F(1, 2), (1, 1): F(1, 2)}
    table_soft = {v: w_soft[v] for v in vals}; table_hard = {v: w_hard.get(v, F(0)) for v in vals}
    print(f"  identical tables: {table_soft == table_hard}  ({ {v: str(p) for v, p in table_soft.items()} })")
    probe = (0, 1)
    print(f"  probe X=0, Y=1: admissible in the soft state ({probe in adm_soft}) at weight {w_soft[probe]}; admissible in the hard state: {probe in adm_hard} (structurally invalid)")
    # a proper child requires non-negligible relative weight: the zero-weight probe is no proper child in the soft state
    print("  the zero-weight probe is admissible but carries no relative weight, so it is no proper child and supplies no validity floor (a separate question from admissibility)")
    # add an entry excluding the matches (0,0) and (1,1)
    adm_soft2 = {v for v in adm_soft if v not in {(0, 0), (1, 1)}}; adm_hard2 = {v for v in adm_hard if v not in {(0, 0), (1, 1)}}
    print(f"  after an added entry excluding the matches: soft state keeps admissible total assignments {sorted(adm_soft2)} (valid in the finite constraint model, total weight {sum(w_soft[v] for v in adm_soft2)});"
          f" hard state keeps {sorted(adm_hard2)} (invalid)")
    print("  => the table does not exhaust the structure: the two states absorb the same further constraint differently.")
    assert table_soft == table_hard and (probe in adm_soft) and (probe not in adm_hard) and adm_soft2 and not adm_hard2

if __name__ == "__main__":
    check_screener_not_bell_local()
    check_three_valued_screener()
    check_two_states_one_table()
    for name in ["reichenbach_check.py", "causal_rungs_check.py", "causal_cf_check.py", "nosignal_check.py", "regularity_check.py"]:
        section("B. " + name)
        sys.stdout.flush()
        runpy.run_path(name, run_name="__main__")
    print("\nAll checks completed.")
