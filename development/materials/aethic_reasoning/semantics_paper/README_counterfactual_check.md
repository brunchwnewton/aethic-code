# Supplement: `counterfactual_check.py`

Reference implementation for *Counterfactual Evaluation by Reopening Information States*.
Pure Python 3 (standard library only). Run `python3 counterfactual_check.py` with no
arguments; the output should match `counterfactual_check_expected_output.txt` exactly
(the random test is seeded). It runs in a few minutes.

## What it implements

**The operator (Definition 1), on finite fully supported models.** Attributes with finite
value spaces; a constraint layer of jointly invalid literal sets (laws, never retracted);
a state given by its stated entries and identified with their deductive closure under the
laws; and a *declared* support relation `Dep`, attribute → the attributes it rests on
(its grounds), whose converse gives the dependents. Entailment is not support: an entry that
entails a value of an attribute without being declared a ground of it is not among its
grounds. When no `Dep` is declared the script uses the entailment-derived default of the
random tests (a stated attribute has no grounds; a derived attribute's grounds are the
attributes of the minimal stated subsets entailing its derived entries).

Reopening the attributes Q at a scope: the scope fixes the attributes that must be blank
(Q at the evidential-minimal scope; Q and its declared dependents, transitively forward, at
the unidirectional scope; Q and everything `Dep`-connected to it at the bidirectional scope)
and the protected content K, the closure of the stated entries whose attributes lie outside
that set and outside Supp(Q), the declared grounds of Q. The admissible restrictions are the
closed B with K ⊆ C(B) ⊆ C(A), blank on the required attributes, blank meaning
*unresolved* (no value stated; the retained content and the laws may still exclude some
values); the reopening is their inclusion-maximal members, all kept (tie-keeping
priorities); it is infeasible when there are none, as when protected content entails a
value of Q. Antecedent targets are the
attributes the antecedent restricts to a proper subset of its value space (`NORMALIZE =
True`); the un-normalized reading is run once for the Left Logical Equivalence test. The
perturbation is the union over intermediates B of R_X(B) = MaxCons{P : C(B) ⊆ C(P), P ⊨ X},
the consistent completions of B satisfying the antecedent's constraint, which is imposed on
the completions directly (so a constrained disjunction q ∈ {x1, x2} persists from
restatement to pruning without being an entry, and an antecedent inconsistent with the
intermediate under the laws contributes no pocket); for an assignment this is the residue
of Restate_X(B) = Cl(B ∪ {X}). Pockets are identified by content; `would` quantifies over
all of them, every pocket carrying positive weight here (Vis(R) = R).

**Comparators (each row of the paper's Table of neighboring semantics, from one clause).**
`premise_max`: evaluation over the maximal subsets of the stated facts consistent with the
antecedent, laws retained (Lewis 1981's premise sets; the paper's maximal-consistent-facts
comparator). `basis_retract`: retraction from the minimal bases of each completion of the
state to its maximal subsets consistent with the antecedent, then extension under the laws
(a Veltman-type clause: the script's encoding of Veltman 2005's construction, not a
transcription). `agm_expansion`: AGM (K*3)/(K*4), revision by an input consistent with the
belief set being expansion (the only case the witness needs). `pearl_structural`: abduction,
action and prediction (Pearl 2009) on the structural model stated in the paper,
S := U_S, X := U_X, Y := S ∨ U_Y, Z := (X ∧ S) ∨ U_Z, exogenous U binary.
`winslett_update`: Winslett 1988's possible-models approach, each model of the state moved to
the models of the antecedent and the standing laws at inclusion-minimal change, measured on
the set of attributes whose values change. `boolean_reading`: the Boolean reading of a
conjunctive antecedent, one two-valued attribute "is X true?", already blank on the witness
(where it is stated, true or false: the inclusion-maximal closed restrictions in which the
conjunction is neither entailed nor excluded). That each clause is the cited account's is for the reader
to check against the sources; the script establishes only what the clauses yield.

## Checks performed

1. The four-attribute witness, with the declared `Dep` making S the sole ground of Y and no
   other edges: one pocket under x, three under x ∧ y; Cautious Monotony and Rational Monotony
   fail at (x, y, z), at every scope (at the bidirectional scope the blank set for x ∧ y includes
   S; the intermediate and the verdicts are unchanged).
1b. The witness under the comprehensive framework's stronger openness requirement (`StrongModel`:
   every value of a blanked attribute must remain admissible at the intermediate, not merely no value
   stated): intermediates and pockets identical to the paper's operator at every scope, on A and on
   A' = Cl({s, ¬x}); the three-valued example (q ∈ {1,2,3}, r = 1 stated, {r = 1, q = 3} invalid, no
   declared dependencies) is feasible under the paper's unresolved grade (q ∈ {1,2}) and infeasible
   under the stronger requirement, so the two are different operations and the principal countermodel
   satisfies both.
2. The streetlight with the declared `Dep` (stopping rests on the light), in the stated-green
   and the derived-green versions: infeasible at the evidential-minimal scope, feasible at
   the unidirectional and bidirectional scopes (had it been red, stopped); feasible without
   protection.
2b. Cut without nesting, with the declared grounds (y rests on p; x rests on p and r) and the
   generalization-over-particular priority; the two tied intermediates' restated contents are
   jointly inconsistent, their pockets collected separately.
3. A three-attribute Cautious Monotony counterexample (law z → y, z declared the sole ground of
   y, state {z}).
3b. A Cautious Monotony failure through a cleared dependent: no laws, state {y, z}, z declared to
   rest on y; at the unidirectional scope reopening x ∧ y clears z, so x ∧ y ⊬ z although y has
   no grounds (holds at the evidential-minimal scope).
4. Left Logical Equivalence: x versus x ∧ (y ∨ ¬y), un-normalized and normalized.
4b. Or with an exhaustive disjunction: no target after normalization, perturbation = the
   standing residue.
5. Every row of the paper's table of neighboring semantics on the witness.
5b. The same comparison where the antecedent is known false, A' = Cl({s, ¬x}), kept apart
   from the table: the operator's verdicts are unchanged at every scope (reopening x clears
   ¬x and retains s); the Veltman-type clause affirms none of the three conditionals;
   Winslett affirms x → y only; the comparator and Pearl affirm all three; AGM expansion is
   inapplicable, the antecedent contradicting the belief set (revision is not computed).
6. Antecedent strengthening and contraposition on the witness; a three-attribute
   transitivity failure (law c → d, state {c, e}: d |~ e, e |~ c, d ⊬ c).
7. Random finite fully supported models (4–5 attributes, one three-valued, 1–4 laws,
   seed 20261008, 3,000 draws, entailment-derived `Dep`, evidential scope): the
   blankness claim of the conjunctive-reopening lemma; the proposition locating Cautious
   Monotony failures against the operator; Cut on nested instances; pocket monotonicity;
   Or, including the exhaustive-disjunction case.
