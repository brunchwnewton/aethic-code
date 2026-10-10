# Supplement: `settling_benchmarks.py`

Reference computations for *Newcomb's Problem Without a Fixed Past: A Decision Rule From
Observer-Indexed Determinacy*. Pure Python 3 (standard library only, exact rational
arithmetic). Run `python3 settling_benchmarks.py` with no arguments; the output should match
`settling_benchmarks_expected_output.txt` exactly.

## What it implements

**The settling rule (Definition), on finite acyclic factor models.** Variables in topological
order with kernel tables; the act with its production entry; couplings (children of the act)
carrying mode sets; an evaluation mode, stated evidence and a candidate act. Fix replaces the
production entry by the point mass at the act; couplings whose mode set contains the
evaluation mode are retained reading the act; the others are detached jointly through one
shared auxiliary copy of the act carrying the original production entry (the
auxiliary-variable representation of the paper's Proposition), evidence is conditioned on,
and the copy is marginalized. An act is inadmissible when its settled residue has no
admissible pocket.

**Comparators on the same models and information.** EDT: conditioning on the act in the
observational law. The fixed-marginal (marginal-preserving) rule: every coupling detached.

## Checks performed

1. Opaque Newcomb at ε = 0.01, 0.4995, 0.5: settled prize laws under the retained
   branch-conditional accuracy, the one-box threshold ε < (M − t)/(2M) = 0.4995, the
   fixed-marginal rule's two-boxing, and EDT's agreement with the retained-accuracy verdict.
2. The separating example against EDT: a predictor whose accuracy is stated as robust to
   habit alone. The habitual agent one-boxes under the rule; the deliberating agent two-boxes
   (the coupling is detached in that mode); EDT one-boxes for both on the same record.
3. Transparent boxes in the shared model: ex-ante policy values (990,010 and 11,000 at
   ε = 0.01, difference 979,010), the settling of the policy component π_full with the full
   box stated (two-box at ε > 0), and the perfect endpoint (two-boxing inadmissible).
4. The smoking lesion: with the resolve stated the settled lesion law is P(L | R) under both
   acts and both the rule and EDT smoke; with the resolve blank the rule's fix severs the act's
   dependence on the desire, the settled law is the prior and the rule smokes, while EDT refrains.
5. Egan's button: the self-settled static verdict under (J2); the projected additive flow's
   interior fixed point for the affine trait law; the logistic variant's additional endpoint
   fixed points.
6. Joint detachment: the appendix's two-coupling example computed through the shared copy and
   through the explicit joint-detachment sum (equal), against separate copies (dependence
   lost); the d-separation sufficient condition for across-act invariance on Newcomb (a
   nonbinding box reads the copy and is invariant; a binding box is act-dependent).
7. The factorization lemma on a numerical instance.
8. Why statedness does not block a path: independent fair bits C, Y with a binding coupling S
   reading both (P(S=1 | C=Y) = 0.9, else 0.1) and S = 1 stated; the settled laws of Y differ
   across acts (0.1 against 0.9, normalizers 1/2), the collider C → S ← Y being opened by the
   conditioning, and coincide at 1/2 when S is nonbinding and reads the auxiliary copy.
