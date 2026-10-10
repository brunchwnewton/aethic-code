# Supplement: `causality_checks.py`

Reference computations for *Causality from Indexed Information States: Screening, Intervention,
and the Bell Obstruction*. Pure Python 3 (standard library only, exact rational arithmetic where
the claim is exact). Run `python3 causality_checks.py` in a directory containing the five
component scripts listed below; the output should match `causality_checks_expected_output.txt`
(every random enumeration is seeded). It runs in a few minutes.

## Part A — the examples added in the October 2026 revision (in `causality_checks.py`)

- A1. A setting-independent screener that is not Bell-local: λ a fair ±1 variable, a = λ,
  P(b | x, y, λ) = (1 + bλE_xy)/2 with E_xy = (−1)^{xy}/√2. The outcomes factorize given λ in
  every context, the marginals are unbiased and non-signaling, and CHSH = 2√2; Bob's response
  depends on Alice's setting, so the model is outside the (D1)–(D3) class of the deflation theorem.
- A2. A three-valued screener without a uniform relevance ordering: C uniform on three values,
  P(A=1|C) = (0.1, 0.5, 0.9), P(B=1|C) = (0.1, 0.9, 0.5); C screens, Cov(A,B) = 4/75 > 0 and the
  covariance identity holds, yet between the last two pockets A's probability rises while B's falls.
- A3. Two states with one probability table and different hard structure (the mismatches of two
  fair bits at weight zero, against the tie entry excluding them): the probe stating a mismatch is
  admissible at zero weight in one and structurally invalid in the other, and an added entry
  excluding the matches leaves the first state with admissible total assignments and the second
  with none.

## Part B — the enumerations reported in the text (component scripts)

| Script | Claim | Enumeration (seed) |
|---|---|---|
| `reichenbach_check.py` | Theorem (connectivity, separation, screening, fork): parts (i)–(iv) and merged presentations | 1,500 random product-form states on 3–5 families, zero weights as joint invalidity (seed 474): 4,208 correlated pairs, 3,692 separating families, 2,908 screeners |
| `causal_rungs_check.py` | Settling = truncated factorization; the Markov-equivalent triple; back-door adjustment | 1,500 random four-family networks (seed 477) |
| `causal_cf_check.py` | Counterfactuals need functional structure; pruning-based counterfactual = twin-world computation | 3,000 random functional models (seed 491) |
| `nosignal_check.py` | Far-wing balance: the two-factor counterexample (1/2 → 5/9), the singlet's balance, the factorization equivalence | 2,000 random setting pairs; 3,000 random positive tables (seed 494) |
| `regularity_check.py` | Regularity proposition (i) and (iii) | 600 random deterministic states on four binary attributes, 118,450 condition–outcome pairs (seed 478) |
