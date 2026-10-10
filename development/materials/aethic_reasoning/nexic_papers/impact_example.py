# RATIFIED DEFAULTS (author, 2026-09-29): window = Phanerozoic (0.541 Gyr); flux = 3 per Gyr central (2-4, Nesvorny et al. 2021);
# family = site 0.13/0.20, angle bin 45-60 deg 0.25, LIP +/-100 kyr 0.042/0.049; timing attribute dropped. Earlier 1.5 Gyr / N=10 rows are superseded sensitivity.
# impact_example.py (R519) — the impact chain as one fully specified event, on declared inputs.
# History model: Chicxulub-class (>= 10 km) impacts arrive as a Poisson process over a window W; each impact independently
# realizes the declared attributes with the stated probabilities (thinning). The complete event E: at least one impact in
# the history realizes every rare side. The rules of the Copernican paper then give P(H) <= P(E)/delta (predeclared
# conjunction) and P(H) <= P(E) * K / delta (realized cell, K = number of cells of the declared family).
# Declared family (binary reads of each attribute; the realized cell is the rare side of each):
#   site     : target rock hydrocarbon/sulfate-rich (Kaiho & Oshima 2017: 13% of the surface; conservative 20%)
#   angle    : impact angle in [45, 60] degrees from horizontal; isotropic arrival gives sin^2(60) - sin^2(45) = 0.25
#              (the wide bin [30, 60] gives 0.5); the bin is a declared partition, not a threshold read off Chicxulub
#   lip      : main phase of a continental flood basalt within +-100 kyr (contingent_bounds_mc.py: 0.042, Wilson upper 0.049)
#   timing   : (optional, operationally undefined) successor lineages "ready"; catalog range 10-20%, conservative 30%
# These defaults were set by Claude Fable 5.1 on 2026-09-25 and count as predeclared only once the author ratifies them.
import numpy as np
delta = 0.05
def P_event(N, q): return 1 - np.exp(-N * q)            # N = expected number of class impacts in the window
cases = [
 ("central, 1.5 Gyr, 10 impacts",              dict(N=10,  site=0.13, angle=0.25, lip=0.042, timing=None)),
 ("central + timing 0.2",                       dict(N=10,  site=0.13, angle=0.25, lip=0.042, timing=0.2)),
 ("conservative (upper inputs), 15 impacts",    dict(N=15,  site=0.20, angle=0.25, lip=0.049, timing=None)),
 ("conservative + timing 0.3",                  dict(N=15,  site=0.20, angle=0.25, lip=0.049, timing=0.3)),
 ("Phanerozoic window, 3/Gyr (N=1.6)",          dict(N=1.6, site=0.13, angle=0.25, lip=0.042, timing=None)),
 ("wide angle bin 30-60 deg",                   dict(N=10,  site=0.13, angle=0.50, lip=0.042, timing=None)),
 ("no coincidence attribute (site x angle)",    dict(N=10,  site=0.13, angle=0.25, lip=1.0,   timing=None)),
]
print(f"{'setting':44s} {'q/impact':>9s} {'P(E)':>8s} {'conj':>8s} {'realized-cell (K)':>18s}")
for name, c in cases:
    q = c['site'] * c['angle'] * c['lip'] * (c['timing'] if c['timing'] else 1.0)
    m = 2 + (c['lip'] < 1.0) + (c['timing'] is not None); K = 2 ** m
    PE = P_event(c['N'], q); conj = PE / delta; rc = PE * K / delta
    print(f"{name:44s} {q:9.2e} {PE:8.4f} {min(conj,1):8.3f} {min(rc,1):10.3f} (K={K})")
print("\nP(H) <= 1 means the rule returns no bound at that setting.")


if __name__ == "__main__":
    import math
    print("\n=== Ratified rows (2026-09-29) ===")
    for lab, N, site, ang, lip in [("Ratified: Phanerozoic @3/Gyr", 0.541*3, 0.13, 0.25, 0.042), ("Ratified conservative: Phanerozoic @4/Gyr", 0.541*4, 0.20, 0.25, 0.049),
                                   ("Sensitivity: 1.5 Gyr @3/Gyr", 4.5, 0.13, 0.25, 0.042), ("Sensitivity: 1.5 Gyr @4/Gyr conservative", 6.0, 0.20, 0.25, 0.049)]:
        q = site*ang*lip; P_E = 1 - math.exp(-N*q)
        print(f"{lab:44s} q={q:.2e} P(E)={P_E:.4f} conjunction={min(1,P_E/0.05):.3f} realized-cell(K=8)={min(1,8*P_E/0.05):.3f}")
