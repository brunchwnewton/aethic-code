# Aethic Reasoning — data and verification scripts

Supplementary code for the Aethic papers. Every script is Python 3, needs only the standard library, and prints the figures the papers quote. Run each from inside this folder. Runtimes were measured on a single core.

`weight_algebra_model_stated.py` and `weight_algebra_broad_check.py` import `weight_algebra_model.py`, so keep all files together. Three scripts' outputs are fully deterministic, and their exact outputs are in `expected_output/`: for example `python3 settling_benchmarks.py | diff - expected_output/settling_benchmarks.txt` prints nothing, and likewise for `weight_algebra_current_model.py` and for `counterfactual_check.py` run with the arguments `12000 20261005`.

## Counterfactual Evaluation by Perturbation of Information States

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `counterfactual_check.py` | The operator of Definition `def:operator` on finite models: the four-attribute witness under the dual-peg and Boolean readings; the Cut-without-nesting countermodel; the witness under premise semantics, AGM revision, Winslett's update (targets satisfying the antecedent and the standing constraints) and Pearl's SCM; and a random-model test of Cut, pocket monotonicity, the Cautious-Monotony characterization and Or | Run as `python3 counterfactual_check.py 12000 20261005` (sample size, seed): Cut 690 instances, 0 failures; pocket monotonicity 2,858, 0; characterization 737, 0 mismatches, 47 Cautious-Monotony failures; Or 550, 0. Exact output in `expected_output/` | about 10 s |

The program computes what each competitor's stated clause yields; that each clause faithfully renders the cited account is checked against the paper's text, not by the program.

## The decision paper

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `settling_benchmarks.py` | The settling rule of Definition `def:settle` (frozen original kernels; point mass on the act; binding couplings retained; non-binding couplings detached jointly over their outputs given their external parents; condition, normalize; zero normalizer = inadmissible under the model) run on each benchmark, with every input listed in the paper's supplement README | Opaque Newcomb 990,000 vs 11,000 (500,000 vs 501,000 when the accuracy coupling does not bind); transparent, full box: two-box at ε = 0.01, two-boxing inadmissible at ε = 0; lesion: P(cancer) 0.66 under both acts; psychopath button −0.8 vs 0 | under 1 s |
| `transparent_newcomb_shared_model.py` | The shared transparent-predictor model: both theories' verdicts over the predictor's error rate | FDT one-boxes on a full box iff ε < (M−t)/(2M−t) ≈ 0.4998; the settling rule two-boxes for every ε > 0 and one-boxes at ε = 0; both two-box on an empty box | under 1 s |

## The Weight Algebra of Aethae

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `weight_algebra_current_model.py` | **The paper's worked example** (current rules): closure-independence, coefficient additivity, the join-semilattice of the nine proper children, doom, the reduced form and the quotient | All 36 pairs have joins, 16 have no common proper child; doom = the tagged set; reduced form 0.3/0.4/0.1. Exact output in `expected_output/` | under 1 s |
| `weight_algebra_model.py` | The finite model under the **superseded** descent rules, the countermodel the paper keeps in its appendix | Lists carriers in *I* but not in *D* | about 1 min |
| `weight_algebra_model_stated.py` | The same model under the current rules: a blank splits only through a held carving, and closure runs the splitting rule | `\|U\| = 900  tagged 782  \|D\| = 782  \|I\| = 782  I == D: True` | about 1.5 min |
| `weight_algebra_broad_check.py` | Broad agreeing states: the passive reading against peg-wise splitting | Passive: `\|D\|=1006 \|I\|=1006 I==D:True`; peg-wise: a gap of 3 | about 2.5 min |
| `declared_descent_check.py` | Declared descent on the worked cases and on 400 random models | All violation counts 0 | about 1 s |

## Aethic Reasoning (the long paper) and Quantum Mechanics from Records

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `frauchiger_renner_mixture.py` | The Frauchiger–Renner two-laboratory joint distribution: the coherent assignment against the record-separated mixture | (ok₁, ok₂), (ok₁, fail₂), (fail₁, ok₂), (fail₁, fail₂): (1/12, 1/12, 1/12, 3/4) coherent against (1/4, 1/4, 1/4, 1/4) for the mixture | under 1 s |
| `decomposability_check.py` | The decomposability grades read in the peg formalism, and the correlated-composite example | 0 violations | about 3 s |

## Provenance

The scripts were written by Claude (Anthropic) with the author in 2026.

## License

The code in this package is released under the MIT License; see `LICENSE`.
