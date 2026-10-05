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

`sealevel_surrogates.py` and `sealevel_three_curves.py` read their data files from the same folder, and `sealevel_three_curves.py` imports `sealevel_surrogates.py` from it. `sealevel_three_curves.py` also needs three records that are not included; see Data for how to create them.

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
| `sealevel_sensitivity.py` | Run-to-run spread across ten seeds, and the loosened-criteria family (thresholds relaxed by 0.10, 0.25 and 0.50 sd; touch criteria dropped) | spread sd 0.0032 vs binomial 0.0035; ratio 74 at the exact extremes, 22 at the 0.10-sd tolerance (the paper's canonical figure), 9, 4; 40 without the touch criteria | about 3 min |
| `sealevel_three_curves.py` | The same test on records independent of the Haq synthesis, with the band and smoothing rescaled to each record's sampling. Needs the three records described under Data, which are not included | New Jersey (Kominz 2008): `65/5000 fired -> P_LC=0.0130`; Ray 2019: `274/5000`; the long-term combined curve: `3611/5000`, the case the test does not apply to | under 1 min |

The sea-level script's options reproduce the robustness table: `--sigma` (smoothing width), `--low` and `--high` (band edges), `--ddof`, `--col 2` (GTS2012 ages), `--resample` (uniform grid spacing in Myr), `--n` (number of surrogates) and `--seed`.

## The original script

`original/surrogate_analysis.py` is the author's original analysis script, included unmodified, with its data file `original/sea levels.csv` (the same NOAA digitization as `haq1987_sealevel.txt`, with column headers). It runs the same pipeline with the same parameters as `sealevel_surrogates.py`, differing in three details: its variability is a population standard deviation through a uniform filter rather than a centered sample standard deviation, it averages duplicate ages, and it is unseeded, so its count varies from run to run by about ±8 at this rate. Run it from inside the `original` folder, since it reads its data file from the working directory:

```
cd original && python3 surrogate_analysis.py run
```

A rerun gave `59/5000 surrogates fired, P = 0.0118 (Wilson 95% CI 0.0092 – 0.0152)`, against the paper's original 67 and the re-implementation's 77; all three lie within one another's intervals. `python3 surrogate_analysis.py diagnose` prints the calibrated thresholds.

## Data

`haq1987_sealevel.txt` is the Haq et al. (1987) eustatic sea-level curve as digitized by Miller et al. (2005) and archived at NOAA/WDC Paleoclimatology as `miller2005-haq87.txt`, the file the long Nexic paper names: 2,225 samples, with the source URL and fetch date in its header. `original/sea levels.csv` is the same digitization with column headers.

**Not included: the three independent records.** `sealevel_three_curves.py` reads three records from the supplementary sea-level compilation of van der Meer, D. G., Stap, L. B., Scotese, C. R., Mills, B. J. W., Sluijs, A., and van Hinsbergen, D. J. J. (2025), Phanerozoic orbital-scale glacio-eustatic variability, *Earth and Planetary Science Letters* 667, 119526, https://doi.org/10.1016/j.epsl.2025.119526. They are not redistributed here. To run that script, download the workbook `SI_SeaLevel_curves_v20250614_Fig6_7_S4.xlsx` from the article's supplementary material and save three text files in this folder. Each file has whitespace-separated columns, and lines beginning with `#` are ignored.

| File to create | From | Columns | Range and rows |
|---|---|---|---|
| `kominz2008_newjersey.txt` | sheet `Kominz2008_ST` | age (Ma), midpoint, minimum, maximum (m), where the midpoint is the middle of the minimum–maximum envelope | 10–108 Ma at 1 Myr, 99 rows |
| `ray2019_cretaceous.txt` | sheet `Ray2019` | age (Ma), 3-Myr window median sea level (m) | 65–145 Ma at 0.5 Myr, 161 rows |
| `longterm_combined_curve.txt` | sheet `CALC_STvar_20241010`, column `ALL effects` | age (Ma), sea level (m) | 0–540 Ma at 1 Myr, 541 rows |

The script checks that the three files exist, printing these instructions if they don't, and warns if a file's row count differs from the paper's run. Please cite that compilation and the primary sources:

- Kominz, M. A., Browning, J. V., Miller, K. G., Sugarman, P. J., Mizintseva, S., and Scotese, C. R. (2008). Late Cretaceous to Miocene sea-level estimates from the New Jersey and Delaware coastal plain coreholes: an error analysis. *Basin Research* 20, 211–226.
- Ray, D. C., van Buchem, F. S. P., Baines, G., Davies, A., Gréselle, B., Simmons, M. D., and Robson, C. (2019). The magnitude and cause of short-term eustatic Cretaceous sea-level change: A synthesis. *Earth-Science Reviews* 197, 102901.

`haq1987_sealevel.txt` is the eustatic sea-level curve of Haq, Hardenbol and Vail (1987) as digitized by Miller et al. (2005), archived by NOAA's World Data Service for Paleoclimatology; the source URL is in the file's header. Please cite the original sources:

- Haq, B. U., Hardenbol, J., and Vail, P. R. (1987). Chronology of fluctuating sea levels since the Triassic. *Science* 235, 1156–1167.
- Miller, K. G., et al. (2005). The Phanerozoic record of global sea-level change. *Science* 310, 1293–1298.

## Provenance

The scripts were written by Claude Fable 5.1 (Anthropic) with the author in 2026. The sea-level script re-implements the long Nexic paper's stated procedure and was written independently of the original script, which is included unmodified in `original/`; its random seed is fixed at 1987, so the quoted run reproduces exactly.

## License

The code in this package is released under the MIT License; see `LICENSE`. The MIT License does not cover the data files. `haq1987_sealevel.txt` and `original/sea levels.csv` are the Miller et al. (2005) digitization of the Haq et al. (1987) curve, distributed freely by NOAA's World Data Service for Paleoclimatology; please cite the sources listed under Data.
