# contingent_bounds_mc.py — first computed coordinates of the Nexic catalog (R509, September 25, 2026).
# 1. Impact–province coincidence: probability that a random impact falls within ±Δ of a large igneous province's main
#    eruptive phase, with main-phase durations varied over a factor of four and ages jittered.
# 2. Per-history joints: at least one Chicxulub-class impact that is lethal by site and angle AND coincides with a main phase.
# 3. Take rates with Jeffreys posterior bounds: provinces that coincide with a Big-Five mass extinction; large craters.
# 4. The size window's upper edge under a power-law size-frequency distribution.
import numpy as np
from scipy.stats import beta
rng = np.random.default_rng(509)

# Main-phase windows (Ma, rounded; assembled for this computation, not transcribed from one table; the geochronology is
# reviewed in Kasbohm, Schoene & Burgess 2021). kind: C = continental flood basalt, O = oceanic plateau.
# crisis: 'B5' = Big-Five mass extinction; 'minor' = a second-order biotic crisis or oceanic anoxic event; '' = none.
LIPS = [
    ("Columbia River",        16.6,  15.9, 'C', ''),
    ("Ethiopia-Yemen",        30.5,  29.5, 'C', ''),
    ("North Atlantic",        56.1,  55.3, 'C', 'minor'),   # PETM; benthic foraminiferal extinction
    ("Deccan",                66.3,  65.6, 'C', 'B5'),      # end-Cretaceous, with Chicxulub
    ("Madagascar",            88.5,  87.5, 'C', ''),
    ("Caribbean-Colombian",   94.5,  93.5, 'O', 'minor'),   # OAE2, Cenomanian-Turonian
    ("Kerguelen (first)",    119.0, 118.0, 'O', ''),
    ("Ontong Java",          121.0, 120.0, 'O', 'minor'),   # OAE1a
    ("Parana-Etendeka",      134.8, 134.0, 'C', ''),
    ("Karoo-Ferrar",         183.2, 182.4, 'C', 'minor'),   # Toarcian
    ("CAMP",                 201.6, 201.0, 'C', 'B5'),      # end-Triassic
    ("Siberian Traps",       252.3, 251.3, 'C', 'B5'),      # end-Permian
    ("Emeishan",             260.5, 259.6, 'C', 'minor'),   # Capitanian
]
T_SPAN = 261.0      # Myr covered by the list (0-261 Ma)
DELTAS = [0.0, 0.05, 0.10, 0.25]
N_MC = 20000

def coverage(windows, delta):
    iv = sorted((a - delta, b + delta) for a, b in windows)
    tot, cur = 0.0, None
    for a, b in iv:
        a, b = max(a, 0.0), min(b, T_SPAN)
        if cur is None: cur = [a, b]
        elif a <= cur[1]: cur[1] = max(cur[1], b)
        else: tot += cur[1] - cur[0]; cur = [a, b]
    if cur: tot += cur[1] - cur[0]
    return tot / T_SPAN

def sample_windows(kinds):
    out = []
    for name, old, young, kind, _ in LIPS:
        if kind not in kinds: continue
        mid = 0.5 * (old + young) + rng.uniform(-0.5, 0.5)            # age jitter ±0.5 Myr
        dur = (old - young) * np.exp(rng.uniform(np.log(0.5), np.log(2.0)))   # duration × [0.5, 2], log-uniform
        out.append((mid - dur / 2, mid + dur / 2))
    return out

def run():
    res = {}
    for label, kinds in [("continental", {'C'}), ("all", {'C', 'O'})]:
        nominal = [(y, o) for (_, o, y, k, _) in LIPS if k in kinds]
        res[label] = {'nominal': {d: coverage(nominal, d) for d in DELTAS}}
        draws = {d: [] for d in DELTAS}
        for _ in range(N_MC):
            w = sample_windows(kinds)
            for d in DELTAS: draws[d].append(coverage(w, d))
        res[label]['mc'] = {d: np.percentile(draws[d], [5, 50, 95]) for d in DELTAS}
    return res

if __name__ == '__main__':
    res = run()
    print("1. Probability a random impact falls within ±Δ of a province main phase (list 0-261 Ma)")
    for label in res:
        for d in DELTAS:
            p5, p50, p95 = res[label]['mc'][d]; nom = res[label]['nominal'][d]
            print(f"   {label:11s} Δ={int(d*1000):3d} kyr: nominal {nom:.4f} | MC median {p50:.4f} [5%: {p5:.4f}, 95%: {p95:.4f}]")
    print("\n2. Per history: P(at least one impact lethal by site and angle AND within ±100 kyr of a main phase)")
    LETHAL = 0.065                       # site 0.13 x angle 0.5, conservative
    for lamT, lab in [(10.0, "conservative flux, 1.5 Gyr window (the catalog's per-history setting)"), (1.6, "3 per Gyr over the 541 Myr Phanerozoic")]:
        for label in res:
            p5, p50, p95 = res[label]['mc'][0.10]
            f = lambda x: 1 - np.exp(-lamT * LETHAL * x)
            print(f"   {lab} | {label:11s}: median {f(p50):.4f}, 95%-coverage ceiling {f(p95):.4f}")
        print(f"   {lab} | lethal alone (no coincidence): {1 - np.exp(-lamT * LETHAL):.3f}")
    print("\n3. Take rates with Jeffreys posteriors (Beta(k+1/2, n-k+1/2))")
    n = len(LIPS); k_b5 = sum(1 for L in LIPS if L[4] == 'B5'); k_any = sum(1 for L in LIPS if L[4])
    for k, lab in [(k_b5, "province coincides with a Big-Five extinction"), (k_any, "province coincides with any listed biotic crisis")]:
        b = beta(k + 0.5, n - k + 0.5); print(f"   {lab}: {k}/{n} = {k/n:.3f}; posterior median {b.median():.3f}, 95% upper {b.ppf(0.95):.3f}")
    for k, n_c in [(1, 4), (1, 5)]:
        b = beta(k + 0.5, n_c - k + 0.5); print(f"   large crater followed by a mass extinction: {k}/{n_c}; posterior median {b.median():.3f}, 95% upper {b.ppf(0.95):.3f}")
    print("\n4. Size window, upper edge: fraction of D > 10 km impacts below a sterilizing diameter D_s, cumulative slope b")
    for Ds in [100, 300]:
        for bslope in [1.8, 2.0, 2.5]:
            print(f"   D_s = {Ds} km, b = {bslope}: {1 - (Ds / 10) ** (-bslope):.5f}")
