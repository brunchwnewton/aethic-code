# Verification scripts: Nexic Reasoning, the Copernican paper, and the Optimal Earth

Supplementary code and data for the Nexic papers. Each script is self-contained, runs with Python 3 and no arguments, and prints the figures the papers quote. Runtimes below were measured on a single core.

## Requirements

Python 3.9 or later, with `numpy`, `scipy` and `pandas`:

```
pip install numpy scipy pandas
```

## Running

Keep all files in one folder and run, for example:

```
python3 sealevel_surrogates.py
```

`sealevel_surrogates.py` and `sealevel_three_curves.py` read their data files from the same folder, and `sealevel_three_curves.py` imports `sealevel_surrogates.py` from it.

## What each script checks

### The Optimal Earth (and the long Nexic paper)

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `strong_accordance_check.py` | The Strong Accordance bound: closed form, quadrature and Monte Carlo compared | Bound attained, maximum ratio 1.000000006 | about 30 s |
| `placement_check.py` | The placement extension | *P*(*H*) ≤ 10^*T* in all 40,000 draws; Pr[*P*(*H*) > 10^−20] = 0.045 against the bound 0.05 | about 12 s |
| `landing_depth_check.py` | The landing-depth route to the spread parameter | Failure probabilities against log10(2)/*M*_eff, and the landing depths quoted | about 1.5 min |

### Nexic Reasoning, the Copernican paper, and the Optimal Earth

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `contingent_bounds_mc.py` | Computed coordinates: the impact–province coincidence and the size window's upper edge | Coincidence at ±100 kyr: Monte Carlo median 0.0418, 95th percentile 0.0494 | about 30 s |
| `impact_example.py` | The impact chain as one fully specified event, at the declared inputs (Phanerozoic window, 3 impacts of *D* > 10 km per Gyr), with sensitivity rows | *P*(*E*) = 0.0022; bound on *P*(*H*) 0.044 (conjunction rule) and 0.354 (realized-cell rule) | under 1 s |
| `sealevel_surrogates.py` | The Intrinsic Frequency sea-level surrogate test, re-implemented from the paper's stated procedure | `77/5000 fired -> P_LC=0.0154 Wilson95=[0.0123,0.0192]` | about 1 min |
| `sealevel_three_curves.py` | The same test on records independent of the Haq synthesis, with the band and smoothing rescaled to each record's sampling | New Jersey (Kominz 2008): `65/5000 fired -> P_LC=0.0130`; Ray 2019: `274/5000`; the long-term combined curve: `3611/5000`, the case the test does not apply to | under 1 min |

The sea-level script's options reproduce the robustness table: `--sigma` (smoothing width), `--low` and `--high` (band edges), `--ddof`, `--col 2` (GTS2012 ages), `--resample` (uniform grid spacing in Myr), `--n` (number of surrogates) and `--seed`.

## Data

`kominz2008_newjersey.txt`, `ray2019_cretaceous.txt` and `longterm_combined_curve.txt` were extracted from the supplementary sea-level compilation of van der Meer, D. G., Stap, L. B., Scotese, C. R., Mills, B. J. W., Sluijs, A., and van Hinsbergen, D. J. J. (2025), Phanerozoic orbital-scale glacio-eustatic variability, *Earth and Planetary Science Letters* 667, 119526, https://doi.org/10.1016/j.epsl.2025.119526 (file `SI_SeaLevel_curves_v20250614_Fig6_7_S4.xlsx`); each file's header names its sheet and columns. Please cite that compilation and the primary sources:

- Kominz, M. A., Browning, J. V., Miller, K. G., Sugarman, P. J., Mizintseva, S., and Scotese, C. R. (2008). Late Cretaceous to Miocene sea-level estimates from the New Jersey and Delaware coastal plain coreholes: an error analysis. *Basin Research* 20, 211–226.
- Ray, D. C., van Buchem, F. S. P., Baines, G., Davies, A., Gréselle, B., Simmons, M. D., and Robson, C. (2019). The magnitude and cause of short-term eustatic Cretaceous sea-level change: A synthesis. *Earth-Science Reviews* 197, 102901.

`haq1987_sealevel.txt` is the eustatic sea-level curve of Haq, Hardenbol and Vail (1987) as digitized by Miller et al. (2005), archived by NOAA's World Data Service for Paleoclimatology; the source URL is in the file's header. Please cite the original sources:

- Haq, B. U., Hardenbol, J., and Vail, P. R. (1987). Chronology of fluctuating sea levels since the Triassic. *Science* 235, 1156–1167.
- Miller, K. G., et al. (2005). The Phanerozoic record of global sea-level change. *Science* 310, 1293–1298.

## Provenance

The scripts were written by Claude Fable 5.1 (Anthropic) with the author in 2026. The sea-level script re-implements the long Nexic paper's stated procedure without access to the original code; its random seed is fixed at 1987, so the quoted run reproduces exactly.
