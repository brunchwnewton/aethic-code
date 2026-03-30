"""
Dark Era Hunting Dynamics: Weight vs. Combat Score
====================================================
Fits power-law curves (score = a * weight^b) via MEDIAN REGRESSION
separately for:
  1. Theropod dinosaurs
  2. Mammals (mouse-to-bear size range)

Median regression minimizes absolute errors instead of squared errors,
making it robust to crowd-data outliers while preserving the central
tendency (wisdom-of-the-crowd median, like a gumball-jar estimate).

Then extrapolates both curves to visualize the ecological gap that
defined the Mesozoic Dark Era for our ancestors.

Usage:
    python dark_era_curves.py duels_ratings_classified_rescaled.csv
"""

import csv
import math
import sys
import json


# ─────────────────────────────────────────────────────────────
# Weight estimates (kg) from paleontological literature
# Only including solo entries (no packs) with known weights
# ─────────────────────────────────────────────────────────────

# Theropod dinosaurs: genus → estimated weight in kg
THEROPOD_WEIGHTS = {
    # Large raptors / mid theropods
    "Utahraptor ostrommaysorum": 500,
    "Dakotaraptor steini": 250,
    "Achillobator giganticus": 250,
    "Deinonychus antirrhopus": 73,
    "Velociraptor mongoliensis": 15,
    "Dromaeosaurus albertensis": 15,
    "Linheraptor exquisitus": 12,
    "Suskityrannus hazelae": 30,
    "Moros intrepidus": 78,
    "Timurlengia euotica": 170,
    # Small theropods
    "Coelophysis bauri": 20,
    "Compsognathus longipes": 3,
    "Ornitholestes hermanni": 12,
    "Archaeopteryx lithographica": 0.9,
    "Yi qi": 0.4,
    "Eodromaeus murphi": 5,
    "Eoraptor lunensis": 10,
    "Liliensternus liliensterni": 130,
    # Ornithomimids and oviraptorosaurs
    "Gallimimus bullatus": 440,
    "Ornithomimus edmontonicus": 170,
    "Citipati osmolskae": 75,
    "Anzu wyliei": 200,
    # Troodontids
    "Stenonychosaurus inequalis": 50,  # = Troodon
    "Dromaeosauroides bornholmensis": 15,
    # Mid-size theropods
    "Dilophosaurus wetherilli": 400,
    "Herrerasaurus ischigualastensis": 210,
    "Monolophosaurus jiangi": 475,
    "Marshosaurus bicentesimus": 200,
    "Concavenator corcovatus": 350,
}

# Mammals: name → estimated weight in kg (extant or well-known extinct)
MAMMAL_WEIGHTS = {
    # Tiny
    "Etruscan Shrew": 0.002,
    "House Mouse": 0.02,
    "Meadow Vole": 0.04,
    "Northern Grasshopper Mouse": 0.035,
    "Four-toed Hedgehog": 0.35,
    "Snowshoe Hare": 1.5,
    "Brown Hare": 3.5,
    "Feral Cat": 4,
    "Red Fox": 6,
    "Arctic Fox": 4,
    "Fennec Fox": 1.2,
    "Honey Badger": 11,
    "Fisher": 4.5,
    "Wolverine": 14,
    "Bobcat": 9,
    "Canadian Lynx": 11,
    "Caracal": 13,
    "Coyote": 14,
    "Ocelot": 12,
    "Red Wolf": 27,
    "Grey Wolf": 40,
    "Dire Wolf": 68,
    "Leopard": 60,
    "Cheetah": 50,
    "Cougar": 70,
    "Spotted Hyena": 55,
    "Lion": 190,
    "Tiger": 220,
    "Siberian Tiger": 230,
    "Bengal Tiger": 220,
    "African Lion": 185,
    "Grizzly Bear": 270,
    "Polar Bear": 450,
    "Gorilla": 160,
    "Common Chimpanzee": 50,
    "Bonobo": 40,
    "Mandrill": 25,
    "Olive Baboon": 25,
    "Human": 70,
    # Extinct mammals
    "Smilodon fatalis": 220,
    "Dire Wolf": 68,
    "Arctodus simus": 800,
    "Thylacine": 25,
}


def load_rescaled(csv_path):
    """Load the rescaled ratings CSV."""
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def match_weights(rows, weight_dict, category):
    """Match animals to their weight estimates."""
    matched = []
    for r in rows:
        name = r["animal"]
        if r["category"] != category:
            continue
        # Skip groups
        nl = name.lower()
        if any(x in nl for x in ["pack", "coalition", "pride", "group", "troop",
                                   "pair", "romp", "(2)", "(3)", "(4)", "(5)"]):
            continue
        if name in weight_dict:
            matched.append({
                "name": name,
                "weight_kg": weight_dict[name],
                "rescaled": float(r["rescaled"]),
                "crowd": float(r["normalized"]),
            })
    return matched


def fit_power_law(data):
    """Fit log(score) = a + b*log(weight) via MEDIAN regression.

    Minimizes sum of absolute errors instead of squared errors,
    making the fit robust to outliers (wisdom-of-the-crowd median).
    Returns (a, b) where score = exp(a) * weight^b.
    """
    n = len(data)
    if n < 3:
        return None, None

    xs = [math.log(d["weight_kg"]) for d in data]
    ys = [math.log(d["rescaled"]) for d in data]

    def median_val(vals):
        s = sorted(vals)
        n = len(s)
        return s[n // 2] if n % 2 == 1 else (s[n // 2 - 1] + s[n // 2]) / 2

    # Grid search: for each slope b, optimal intercept = median(y - b*x)
    best_b, best_a, best_err = 0, 0, float("inf")
    for b_int in range(0, 3000):
        b = b_int / 1000
        residuals = [y - b * x for x, y in zip(xs, ys)]
        a = median_val(residuals)
        err = sum(abs(y - a - b * x) for x, y in zip(xs, ys))
        if err < best_err:
            best_err = err
            best_b = b
            best_a = a

    # Compute pseudo-R² (based on absolute deviations)
    median_y = median_val(ys)
    total_abs = sum(abs(y - median_y) for y in ys)
    r_pseudo = 1 - best_err / total_abs if total_abs > 0 else 0

    return best_a, best_b, r_pseudo


def predict(a, b, weight_kg):
    """Predict score from weight using fitted power law."""
    return math.exp(a + b * math.log(weight_kg))


def main(csv_path):
    rows = load_rescaled(csv_path)
    print(f"Loaded {len(rows)} entries.\n")

    # ── Match weights ──
    theropods = match_weights(rows, THEROPOD_WEIGHTS, "dinosaur")
    mammals = match_weights(rows, MAMMAL_WEIGHTS, "non-mesozoic")

    theropods.sort(key=lambda d: d["weight_kg"])
    mammals.sort(key=lambda d: d["weight_kg"])

    print(f"{'=' * 70}")
    print(f"THEROPODS WITH WEIGHT ESTIMATES ({len(theropods)} matched)")
    print(f"{'=' * 70}")
    print(f"  {'Name':<40s} {'Weight (kg)':>12s} {'Rescaled':>10s}")
    print(f"  {'-'*40} {'-'*12} {'-'*10}")
    for d in theropods:
        print(f"  {d['name']:<40s} {d['weight_kg']:>10.1f}kg {d['rescaled']:>10.1f}")

    print(f"\n{'=' * 70}")
    print(f"MAMMALS WITH WEIGHT ESTIMATES ({len(mammals)} matched)")
    print(f"{'=' * 70}")
    print(f"  {'Name':<40s} {'Weight (kg)':>12s} {'Rescaled':>10s}")
    print(f"  {'-'*40} {'-'*12} {'-'*10}")
    for d in mammals:
        print(f"  {d['name']:<40s} {d['weight_kg']:>10.2f}kg {d['rescaled']:>10.1f}")

    # ── Fit theropod power law (median regression, full range) ──
    print(f"\n{'=' * 70}")
    print("MEDIAN POWER LAW FITS: score = C × weight^b")
    print("(Robust to outliers — tracks the crowd's central tendency)")
    print(f"{'=' * 70}")

    a_t, b_t, r2_t = fit_power_law(theropods)
    C_t = math.exp(a_t) if a_t is not None else None

    print(f"\n  Theropods:  score = {C_t:.3f} × weight^{b_t:.3f}   (pseudo-R² = {r2_t:.3f}, n={len(theropods)})")

    # ── Fit mammals with re-anchoring ──
    # The crowd can't calibrate tiny mammals against large ones (comedy votes),
    # but CAN relatively rank animals within a size class. Strategy:
    #   1. Fit the reliable range (>= threshold) with median regression
    #   2. Re-anchor small mammals onto that slope, preserving relative differences
    #   3. Refit on the full corrected dataset

    RELIABLE_THRESHOLD = 9  # kg (bobcat and up)
    print(f"\n  Mammal re-anchoring (reliable threshold: {RELIABLE_THRESHOLD}kg):")

    reliable = [d for d in mammals if d["weight_kg"] >= RELIABLE_THRESHOLD]
    unreliable = [d for d in mammals if d["weight_kg"] < RELIABLE_THRESHOLD]

    # Fit reliable range only
    a_rel, b_rel, r2_rel = fit_power_law(reliable)
    C_rel = math.exp(a_rel)
    print(f"    Reliable fit (n={len(reliable)}): score = {C_rel:.4f} × weight^{b_rel:.3f}")

    # Fit unreliable range locally (to extract relative differences)
    if len(unreliable) >= 3:
        a_loc, b_loc, _ = fit_power_law(unreliable)
    else:
        a_loc, b_loc = a_rel, b_rel  # fallback

    print(f"    Local small-mammal fit (n={len(unreliable)}): exponent = {b_loc:.3f} (vs reliable {b_rel:.3f})")

    # Re-anchor: sigmoid blend from corrected (small) to original (large)
    log_thresh = math.log(RELIABLE_THRESHOLD)
    k_blend = 1.5  # sigmoid steepness

    for d in mammals:
        lw = math.log(d["weight_kg"])
        ls = math.log(d["rescaled"])
        blend = 1 / (1 + math.exp(k_blend * (lw - log_thresh)))

        # Residual from local fit (relative position among peers)
        local_residual = ls - (a_loc + b_loc * lw)
        # Re-anchored = global prediction + local residual
        reanchored = (a_rel + b_rel * lw) + local_residual
        # Blend between original and re-anchored
        corrected_log = (1 - blend) * ls + blend * reanchored
        d["corrected"] = math.exp(corrected_log)
        d["blend"] = blend

    # Refit on corrected values
    corrected_mammals = [{"weight_kg": d["weight_kg"], "rescaled": d["corrected"]}
                         for d in mammals]
    a_m, b_m, r2_m = fit_power_law(corrected_mammals)
    C_m = math.exp(a_m) if a_m is not None else None

    print(f"    Corrected full fit (n={len(mammals)}): score = {C_m:.4f} × weight^{b_m:.3f}  (pseudo-R² = {r2_m:.3f})")

    # Show re-anchoring effect on small mammals
    print(f"\n    Re-anchored small mammals:")
    for d in mammals:
        if d["weight_kg"] < RELIABLE_THRESHOLD:
            print(f"      {d['name']:<30s} {d['weight_kg']:>7.3f}kg  "
                  f"crowd={d['rescaled']:>8.2f} → corrected={d['corrected']:>8.4f}  "
                  f"(blend={d['blend']:.0%})")

    print(f"\n  FINAL FITS:")
    print(f"    Theropods:  score = {C_t:.3f} × weight^{b_t:.3f}")
    print(f"    Mammals:    score = {C_m:.4f} × weight^{b_m:.3f}")
    print(f"    Intercept ratio at 1kg: {C_t/C_m:.1f}× theropod advantage")
    if b_m != b_t:
        cross = (C_t / C_m) ** (1 / (b_m - b_t))
        print(f"    Theoretical crossover: {cross:.0f} kg ({'never' if cross > 1e6 else f'{cross:.0f}kg'})")

    # ── Compare at key weight classes ──
    print(f"\n{'=' * 70}")
    print("DARK ERA DYNAMICS: Theropod vs Mammal at same weight")
    print(f"{'=' * 70}")
    print(f"  {'Weight':>10s}  {'Theropod':>12s}  {'Mammal':>12s}  {'Ratio':>8s}  {'Context'}")
    print(f"  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*8}  {'-'*30}")

    comparisons = [
        (0.02, "Mouse-sized"),
        (0.1, "Shrew-sized"),
        (0.5, "Rat-sized"),
        (2, "Squirrel-sized"),
        (5, "Rabbit-sized"),
        (15, "Fox-sized (Velociraptor)"),
        (40, "Wolf-sized"),
        (75, "Human-sized (Deinonychus)"),
        (250, "Lion-sized (Dakotaraptor)"),
        (500, "Bear-sized (Utahraptor)"),
    ]

    for weight, context in comparisons:
        t_score = predict(a_t, b_t, weight)
        m_score = predict(a_m, b_m, weight)
        ratio = t_score / m_score
        print(f"  {weight:>8.1f}kg  {t_score:>12.1f}  {m_score:>12.1f}  {ratio:>7.1f}×  {context}")

    # ── Dark Era ancestor scenario ──
    print(f"\n{'=' * 70}")
    print("THE DARK ERA: What our ancestors faced")
    print(f"{'=' * 70}")
    ancestor_weight = 0.1  # ~100g, rat-sized Mesozoic mammal
    ancestor_score = predict(a_m, b_m, ancestor_weight)

    print(f"\n  Our Mesozoic ancestor (~{ancestor_weight}kg, rat-sized):")
    print(f"    Predicted score: {ancestor_score:.6f}")

    # What size theropod is an equal match?
    # solve: C_t * w^b_t = ancestor_score
    # w = (ancestor_score / C_t)^(1/b_t)
    equal_theropod_weight = math.exp((math.log(ancestor_score) - a_t) / b_t)
    print(f"    Equally matched theropod weight: {equal_theropod_weight*1000:.1f}g")
    print(f"    (A theropod just {equal_theropod_weight*1000:.0f}g could take our ancestor)")

    # What theropod was actually hunting them?
    hunter_weights = [0.5, 3, 15]  # Tiny raptor to Velociraptor class
    print(f"\n  Likely hunters of rat-sized mammals:")
    for hw in hunter_weights:
        h_score = predict(a_t, b_t, hw)
        ratio = h_score / ancestor_score
        print(f"    {hw}kg theropod: score {h_score:.4f} vs ancestor {ancestor_score:.6f} = {ratio:.0f}× mismatch")

    # ── Export data for visualization ──
    print(f"\n{'=' * 70}")
    print("EXPORTING DATA FOR VISUALIZATION")
    print(f"{'=' * 70}")

    viz_data = {
        "theropods": {
            "points": [{"name": d["name"], "weight": d["weight_kg"], "score": d["rescaled"]}
                       for d in theropods],
            "fit": {"C": C_t, "b": b_t, "r2": r2_t},
        },
        "mammals": {
            "points": [{"name": d["name"], "weight": d["weight_kg"],
                        "score_crowd": d["rescaled"],
                        "score_corrected": d.get("corrected", d["rescaled"])}
                       for d in mammals],
            "fit": {"C": C_m, "b": b_m, "r2": r2_m},
            "reliable_threshold_kg": RELIABLE_THRESHOLD,
        },
        "comparisons": [
            {"weight": w, "theropod": predict(a_t, b_t, w),
             "mammal": predict(a_m, b_m, w), "context": c}
            for w, c in comparisons
        ],
    }

    out_json = csv_path.rsplit(".", 1)[0] + "_dark_era.json"
    with open(out_json, "w") as f:
        json.dump(viz_data, f, indent=2)
    print(f"  Saved to {out_json}")

    # Also write a simple CSV of the comparison table
    out_csv = csv_path.rsplit(".", 1)[0] + "_dark_era_comparison.csv"
    with open(out_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["weight_kg", "theropod_score", "mammal_score", "ratio", "context"])
        for weight, context in comparisons:
            t_score = predict(a_t, b_t, weight)
            m_score = predict(a_m, b_m, weight)
            writer.writerow([weight, f"{t_score:.2f}", f"{m_score:.2f}",
                           f"{t_score/m_score:.2f}", context])
    print(f"  Saved to {out_csv}")


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "duels_ratings_classified_rescaled.csv"
    main(csv_path)