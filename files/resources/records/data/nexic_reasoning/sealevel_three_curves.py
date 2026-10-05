# sealevel_three_curves.py — the Intrinsic Frequency test of sealevel_surrogates.py run on independent sea-level records.
# The test's parameters are set in samples; here they are rescaled to each record's sampling so that the band-pass keeps the
# same physical periods (about 2.2-110 Myr) and the Gaussian smoothing the same physical width (0.88 Myr) as on the Haq record.
# Thresholds are read off the Late Cretaceous window (89.75-66 Ma) of each record itself; surrogates are IAAFT (seed 1987).
import os, math, numpy as np, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('sl', os.path.join(HERE, 'sealevel_surrogates.py')); sl = importlib.util.module_from_spec(spec); spec.loader.exec_module(sl)
RECORDS = [('Kominz 2008 New Jersey (min/max midpoint)', 'kominz2008_newjersey.txt'), ('Ray 2019 Cretaceous (3-Myr medians)', 'ray2019_cretaceous.txt'),
           ('Long-term combined curve (all effects)', 'longterm_combined_curve.txt')]
def wilson(c, n, z=1.96):
    p = c / n; den = 1 + z*z/n; ctr = (p + z*z/(2*n))/den; half = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/den; return p, ctr-half, ctr+half
EXPECTED_ROWS = {'kominz2008_newjersey.txt': 99, 'ray2019_cretaceous.txt': 161, 'longterm_combined_curve.txt': 541}
RECIPE = """These three records are not redistributed with this package. Download the supplementary workbook
SI_SeaLevel_curves_v20250614_Fig6_7_S4.xlsx of van der Meer et al. (2025), Earth and Planetary Science Letters 667, 119526,
https://doi.org/10.1016/j.epsl.2025.119526, and save, in this folder, whitespace-separated columns (lines starting with # are ignored):
  kominz2008_newjersey.txt     sheet Kominz2008_ST: age_Ma, midpoint_m, min_m, max_m for 10-108 Ma at 1 Myr (99 rows),
                               midpoint_m being the midpoint of the minimum-maximum envelope
  ray2019_cretaceous.txt       sheet Ray2019: age_Ma, 3-Myr window median sea level (m), 65-145 Ma at 0.5 Myr (161 rows)
  longterm_combined_curve.txt  sheet CALC_STvar_20241010, column 'ALL effects': age_Ma, sea level (m), 0-540 Ma at 1 Myr (541 rows)
See README.md, section Data."""
def check_records():
    missing = [fn for fn in EXPECTED_ROWS if not os.path.exists(os.path.join(HERE, fn))]
    if missing:
        print("Missing input records: " + ", ".join(missing) + "\n" + RECIPE); raise SystemExit(1)
    for fn, n in EXPECTED_ROWS.items():
        rows = len(np.loadtxt(os.path.join(HERE, fn), ndmin=2))
        if rows != n: print(f"Warning: {fn} has {rows} rows; the paper's run used {n}, so results may differ.")
if __name__ == '__main__':
    check_records()
    n_surr = 5000
    for name, fn in RECORDS:
        d = np.loadtxt(os.path.join(HERE, fn)); age, val = d[:, 0], d[:, 1]; o = np.argsort(age); age, val = age[o], val[o]
        dt = float(np.median(np.diff(age))); sigma = max(0.5, 0.88 / dt); low, high = 1000 * dt / 110.0, min(1000 * dt / 2.2, 499.0)
        pipe = sl.Pipeline(age, val, sigma=sigma, band=(low, high)); hits = pipe.detect(val)
        c, w = sl.run(pipe, n_surr); p, lo, hi = wilson(c, n_surr)
        print(f"{name}: N={len(age)} dt={dt:.2f} Myr span={age[-1]-age[0]:.0f} Myr (~{(age[-1]-age[0])/23.75:.1f} detection windows)")
        print(f"    empirical qualifying windows: {[(round(age[i],1), round(age[min(i+pipe.W, len(age)-1)],1)) for i in hits]}")
        print(f"    surrogates: {c}/{n_surr} fired -> P_LC={p:.4f} Wilson95=[{lo:.4f},{hi:.4f}]")
