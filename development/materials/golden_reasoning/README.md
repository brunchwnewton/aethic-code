# Golden Reasoning — verification scripts

Scripts reproducing numerical claims of the long Golden Reasoning paper. Each runs standalone with numpy and scipy.

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `task_human_correlation.py` | (1) Minimum score correlation implied by a realized single task-human under the Accordance Principle at level κ, exact realizer model (Poisson counts, uniform choice among qualifiers); (2) chain lengths reproducing N/α; (3) the three-type chain model with link steepness: r_ab,min by scenario, the pure-chain rows computed exactly (two-dimensional quadrature; a one-dimensional integral at s = ∞), the mixed rows on a Gauss–Hermite grid of 96 nodes per axis, good to about 0.01 | Part (1): feasibility iff E[1/K \| K ≥ 1] ≥ 1/(1+κ); r_min from 0.71 to 0.996. Part (3), at κ = 4/9/19/99: pure chains s = 1 → —/0.977/0.921/0.801, s = 3 → 0.918/0.864/0.814/0.708, s = ∞ → 0.897/0.844/0.795/0.692; mixed chains s = 1 → —/—/0.966/0.421, s = 3 → 0.028/−0.365/−0.537/−0.736 (weak but not vacuous); three shared type-c steps s = 1 → —/0.865/0.646/0.185. These are the paper's table to two decimals | about 25 min |

| `newton_timing.py` | Timing as a trait: eligible-exposure model of the Newton window (declared demographic inputs, sensitivity grid, lattice anchor) | Baseline R ≈ 2e-3, α(T,W) ≈ 0.002 (bound 0.005 at k = 0), Bayes factor ≈ 570, required jointness ≈ 570; across the grid α(T,W) from 1e-4 to 0.05 and Bayes factor from ~20 to ~9000; π(T | S_calc) ≤ 0.3% | under 1 s |

## Provenance
The model and the question it answers follow the author's note of 2026-10-02 (1:27 PM ET), quoted verbatim in the paper; the computation is by Claude Fable 5.1 the same day. The timing model follows the author's note of 2026-10-03 on the Newton window, quoted verbatim in the paper; demographic inputs are order-of-magnitude and declared in the script.

The pure-chain rows were checked against an independent fine-grid quadrature at two spacings, and the grid's accuracy on the mixed rows by comparing 64 and 96 nodes per axis with an independent three-dimensional grid. An earlier version of the script integrated every row on a 32-node grid, which overstated the pure-chain values at s = 3 by up to 0.019.

## License

The code in this package is released under the MIT License; see `LICENSE`.
