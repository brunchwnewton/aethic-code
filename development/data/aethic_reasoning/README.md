# Aethic reasoning — computational supplements

Every checking script produced during the referee-driven revision of the Aethic/Nexic paper suite, collected
by paper. All scripts are Python 3 with the standard library only (exact rational arithmetic where a claim is
exact), except `determinacy_paper/realist_checks.py`, which also needs `numpy`. Random enumerations are seeded,
so each run should reproduce the reported counts; where an `*_expected_output.txt` file is present, running the
script with no arguments should match it exactly.

Assembled 9 October 2026. The revision ledger (`FABLE_LEDGER.md`, delivered separately) records the round in
which each script was written and what it was used to verify.

## Submission supplements (cited in the papers)

| Paper (file) | Folder | Entry point | Companion files |
|---|---|---|---|
| Newcomb's Problem Without a Fixed Past (`decision.tex`) | `decision_paper/` | `settling_benchmarks.py` | README, expected output |
| Counterfactual Evaluation by Reopening Information States (`modal.tex`) | `semantics_paper/` | `counterfactual_check.py` | README, expected output; earlier-round checks `cm_check.py`, `cm_characterization_check.py`, `cut_counterexample.py` |
| Causality from Indexed Information States (`quant_causal.tex`) | `causality_paper/` | `causality_checks.py` (runs the five component scripts in the same folder) | README, expected output |
| Determinacy as a Two-Place Relation (`realist.tex`) | `determinacy_paper/` | `realist_checks.py` (needs numpy) | expected output |
| Quantum Mechanics from Records (`quant.tex`) | `quantum_paper/` | `readings_check.py` | — |
| The algebra paper (`aethic_tree.tex`) | `algebra_paper/` | `declared_descent_check.py`, `weight_algebra_broad_check.py`, `weight_algebra_model.py`, `weight_algebra_model_stated.py` | `invalidity_model.py`, `refinement_model.py` (the referee's small models) |
| Aethic Reasoning, the long paper (`1_Aethic_Reasoning.tex`) | `long_aethic_paper/` | `decomposability_check.py`, `deduction_battery.py` | `axiomatics_checks/` (closure, pegs, composition, sums and tiers, F10–F12, E+α) |
| Nexic Reasoning, the Copernican and Optimal Earth papers (`3_Nexic_Reasoning.tex`, `nexic.tex`, `optimal_earth.tex`) | `nexic_papers/` | `impact_example.py`, `sealevel_surrogates.py`, `copernican_check.py` | `contingent_bounds_mc.py`, `landing_depth_check.py`, `placement_check.py`, `strong_accordance_check.py` |
| Sequential achievement (`howlong.tex`) | `howlong_paper/` | `howlong_realizations.py` | — |

Running times on an ordinary laptop: most scripts finish in seconds; `counterfactual_check.py`,
`causality_checks.py`, `weight_algebra_broad_check.py`, `weight_algebra_model_stated.py`, `landing_depth_check.py`,
`sums_check.py`, `f10_distributivity_check.py` and `composites_check.py` take one to three minutes each.

## Referenced in a paper but not in this bundle

The following script names are cited in the papers' text but were not among the files produced in these revision
sessions; they should be located on the author's side or the citations removed before submission:
`frauchiger_renner_mixture.py` (long Aethic paper), `sealevel_three_curves.py` and `surrogate_analysis.py`
(long Nexic paper), `weight_algebra_current_model.py` (algebra paper), `newton_timing.py` and
`task_human_correlation.py` (Golden reasoning paper).

## Tools

`tools/` holds two revision utilities that take command-line arguments and are not paper supplements:
`inventory.py SRC.tex OUT.json` (baseline paragraph inventory) and `check_noloss.py INVENTORY.json NEW.tex [LEDGER.json]`
(no-loss checker for a restructured section).

## Notes

- The auxiliary checks from earlier rounds print their own conclusions, including negative ones that were recorded in
  the ledger at the time (for example `e_alpha_closure_check.py` reports the carving cases in which the "3.3 shadow"
  claim fails); they are included unchanged.
- Each supplement's README states which clause of a cited account its comparator rows implement; the scripts
  establish what those clauses yield, and their fidelity to the cited sources is a scholarly claim to be checked
  against the sources.
