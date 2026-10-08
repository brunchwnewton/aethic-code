# Supplement: `counterfactual_check.py`

Reference implementation for *Counterfactual Evaluation by Reopening Information States*.
Pure Python 3 (standard library only). Run `python3 counterfactual_check.py`; the output
should match `counterfactual_check_expected_output.txt` exactly (the random test is seeded).

## What it implements

**The operator (Definition 1), on finite fully supported models.** Attributes with finite
value spaces; a constraint layer of jointly invalid literal sets (laws, never retracted);
a state given by its stated entries and identified with their deductive closure under the
laws. Support is base-shaped: a stated entry is supported by itself alone, and a derived
entry's grounds are the minimal stated subsets entailing it.

Reopening of attributes Q at the bare-attribute scope (the setting every example in the
paper uses, nothing in them having recorded posterity): the clearable stated entries are
Q's own and Supp(Q); the retained content K is the closure of the stated entries outside
that set; the admissible restrictions are the closed subsets B of the state's content with
K ⊆ B, blank on Q; the reopening is their inclusion-maximal members, all kept (tie-keeping
priorities), and it is infeasible when there are none. Antecedent targets are the attributes
the antecedent restricts to a proper subset of their value space (`NORMALIZE = True`); the
un-normalized reading is run once to exhibit the Left Logical Equivalence test. Pockets are
the consistent completions of the restated intermediates; `would` quantifies over all of
them, every pocket carrying positive weight here (Vis(R) = R).

**Comparators.** `premise_max`: maximal subsets of the stated facts consistent with the
antecedent, laws retained (the paper's narrowly named comparator). `basis_retract`: a
Veltman-type clause, retracting from the minimal bases of each completion of the state
and extending under the laws; it is the script's own encoding, not a transcription.

## Checks performed

1. The four-attribute witness: one pocket under x, three under x ∧ y; Cautious Monotony
   and Rational Monotony fail at (x, y, z).
2. Retention: with the retention clause the streetlight-type example (law r → t,
   state {¬r, ¬t}) is infeasible; without it, bare blanking succeeds.
2b. Cut without nesting, with the generalization-over-particular priority.
3. A three-attribute Cautious Monotony counterexample (law z → y, state {z}).
4. Left Logical Equivalence: x versus x ∧ (y ∨ ¬y), un-normalized and normalized.
5. The two comparators on the witness.
6. Antecedent strengthening and contraposition on the witness; a three-attribute
   transitivity failure (law c → d, state {c, e}: d |~ e, e |~ c, d ⊬ c).
7. Random finite fully supported models (4–5 attributes, one three-valued, 1–4 laws,
   seed 20261008): the proposition locating Cautious Monotony failures against the
   operator; Cut on nested instances; pocket monotonicity; Or.
