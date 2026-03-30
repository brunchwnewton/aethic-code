"""
Dinosaur Recalibration Script
==============================
Demonstrates how crowd-sourced animal combat ratings systematically
underestimate Mesozoic dinosaurs by applying a Cenozoic weight-based
paradigm. Corrects by rescaling dinosaurs using an "anatomy paradigm"
where Dakotaraptor:BigCat ≈ BigCat:NakedHuman.

Pipeline:
  1. Compute "big cat" score = geometric mean of top lion & tiger
  2. Normalize all scores so big cat = 100
  3. Find naked human score
  4. Compute dino scale factor so geomean(Dakotaraptor, Human) = 100
  5. Apply scale factor to dinosaurs, sqrt(factor) to mesozoic-other
  6. Output rescaled CSV

Usage:
    python rescale_dinos.py duels_ratings_classified.csv
"""

import csv
import math
import sys


def load_classified(csv_path):
    """Load the classified ratings CSV."""
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["power"] = float(row["power"])
            rows.append(row)
    return rows


def find_big_cat_score(rows):
    """Compute big cat benchmark as geometric mean of clustered lion & tiger scores.

    Filters out groups, females, non-cat animals with 'lion'/'tiger' in name,
    small/pygmy subspecies, and statistical outliers (>2x the next entry).
    Takes geometric mean of each cluster, then geometric mean of the two.
    """
    # Exclusion patterns
    exclude_lion = [
        "coalition", "pride", "pack", "clan", "(2)", "(3)", "(4)", "(5)",
        "(6)", "(7)", "(8)", "(9)", "(10)",
        "female", "lioness",
        "sea lion", "marsupial lion", "plionarctos", "jellyfish",
        "cave lion", "american lion", "natodomeri", "pleistocene",
        "mountain lioness", "stallion", "sambir",
    ]
    exclude_tiger = [
        "coalition", "pride", "pack", "(2)", "(3)", "(4)", "(5)",
        "female", "tigress",
        "tiger shark", "tigerfish", "tiger beetle", "tiger quoll",
        "sand tiger", "quoll",
    ]
    small_subspecies = [
        "bali", "south china", "sumatran", "bornean", "longdan",
        "trinil", "wanhsien", "ngandong",
    ]

    def eligible(name, excludes):
        nl = name.lower()
        return (not any(x in nl for x in excludes) and
                not any(x in nl for x in small_subspecies))

    lions = [(r["animal"], r["power"]) for r in rows
             if r["category"] == "non-mesozoic"
             and "lion" in r["animal"].lower()
             and eligible(r["animal"], exclude_lion)]
    lions.sort(key=lambda x: -x[1])

    tigers = [(r["animal"], r["power"]) for r in rows
              if r["category"] == "non-mesozoic"
              and "tiger" in r["animal"].lower()
              and eligible(r["animal"], exclude_tiger)]
    tigers.sort(key=lambda x: -x[1])

    def drop_outliers(entries):
        """Drop entries that are >2x the next entry (outlier high)."""
        if len(entries) < 2:
            return entries
        clean = list(entries)
        while len(clean) > 1 and clean[0][1] > 2 * clean[1][1]:
            print(f"    Dropping outlier: {clean[0][0]} ({clean[0][1]:.2f})")
            clean = clean[1:]
        return clean

    print("Eligible lions:")
    for name, p in lions:
        print(f"  {p:>10.4f}  {name}")
    lions = drop_outliers(lions)

    print("\nEligible tigers:")
    for name, p in tigers:
        print(f"  {p:>10.4f}  {name}")
    tigers = drop_outliers(tigers)

    if not lions or not tigers:
        raise ValueError("Could not find eligible lion and tiger entries!")

    lion_gm = math.exp(sum(math.log(p) for _, p in lions) / len(lions))
    tiger_gm = math.exp(sum(math.log(p) for _, p in tigers) / len(tigers))
    big_cat = math.sqrt(lion_gm * tiger_gm)

    print(f"\nLion cluster geomean:  {lion_gm:.4f} (n={len(lions)})")
    print(f"Tiger cluster geomean: {tiger_gm:.4f} (n={len(tigers)})")
    print(f"Big Cat score = geomean({lion_gm:.2f}, {tiger_gm:.2f}) = {big_cat:.4f}")
    return big_cat


def find_human_score(rows):
    """Find naked human score as geometric mean of clustered solo human entries.

    Excludes: armed, archaic, Homo (other species), groups, female (outlier low).
    """
    exclude = ["archaic", "homo ", "armed", "spear", "club", "(2)", "humans",
               "female", "neanderthal", "floresiensis", "erectus"]
    humans = []
    for r in rows:
        nl = r["animal"].lower()
        if "human" not in nl:
            continue
        if any(x in nl for x in exclude):
            continue
        humans.append((r["animal"], r["power"]))

    humans.sort(key=lambda x: -x[1])
    print("Eligible naked human entries:")
    for name, p in humans:
        print(f"  {p:>10.4f}  {name}")

    if not humans:
        raise ValueError("Could not find naked human entries!")

    human_gm = math.exp(sum(math.log(p) for _, p in humans) / len(humans))
    print(f"Human geomean: {human_gm:.4f} (n={len(humans)})")
    return human_gm


def find_entry(rows, target, category=None):
    """Find a specific entry by name (case-insensitive exact match)."""
    target_lower = target.lower()
    for r in rows:
        if r["animal"].lower() == target_lower:
            if category is None or r["category"] == category:
                return r
    # Try partial match
    for r in rows:
        if target_lower in r["animal"].lower():
            if category is None or r["category"] == category:
                return r
    return None


def rescale(rows, csv_path):
    """Full rescaling pipeline."""
    print("=" * 70)
    print("STEP 1: Compute Big Cat Benchmark")
    print("=" * 70)
    big_cat = find_big_cat_score(rows)

    print(f"\n{'=' * 70}")
    print("STEP 2: Normalize (Big Cat = 100)")
    print("=" * 70)
    norm_factor = 100.0 / big_cat
    print(f"Normalization factor: {norm_factor:.6f}")

    # Apply normalization to all
    for r in rows:
        r["normalized"] = r["power"] * norm_factor

    # Show some landmarks
    landmarks = [
        ("Lion", None), ("Tiger", None), ("African Lion", None),
        ("Bengal Tiger", None), ("Siberian Tiger", None),
        ("Grey Wolf", None), ("Grizzly Bear", None),
        ("Human", None), ("Tyrannosaurus rex", None),
        ("Dakotaraptor steini", None),
    ]
    print("\nLandmark scores (normalized, big cat = 100):")
    for name, cat in landmarks:
        entry = find_entry(rows, name, cat)
        if entry:
            print(f"  {entry['normalized']:>10.2f}  {entry['animal']}")

    print(f"\n{'=' * 70}")
    print("STEP 3: Find Naked Human")
    print("=" * 70)
    human_raw = find_human_score(rows)
    human_norm = human_raw * norm_factor
    print(f"Human (normalized): {human_norm:.4f}")

    print(f"\n{'=' * 70}")
    print("STEP 4: Compute Dinosaur Scale Factor")
    print("=" * 70)
    dakotaraptor = find_entry(rows, "Dakotaraptor steini")
    if not dakotaraptor:
        raise ValueError("Could not find Dakotaraptor!")

    dako_norm = dakotaraptor["normalized"]
    print(f"Dakotaraptor (normalized): {dako_norm:.4f}")
    print(f"Human (normalized):        {human_norm:.4f}")
    print(f"Target: geomean(Dakotaraptor_rescaled, Human) = 100")
    print(f"  → Dakotaraptor_rescaled = 100² / Human = {100**2 / human_norm:.4f}")

    # geomean(dako_rescaled, human) = 100
    # sqrt(dako_rescaled * human) = 100
    # dako_rescaled = 10000 / human
    # dino_factor * dako_norm = 10000 / human
    # dino_factor = 10000 / (human * dako_norm)
    dino_factor = 10000.0 / (human_norm * dako_norm)
    meso_other_factor = math.sqrt(dino_factor)

    print(f"\nDino scale factor:         {dino_factor:.4f}")
    print(f"Mesozoic-other factor:     {meso_other_factor:.4f} (√dino_factor)")

    # Verify
    dako_rescaled = dako_norm * dino_factor
    check = math.sqrt(dako_rescaled * human_norm)
    print(f"\nVerification: geomean({dako_rescaled:.2f}, {human_norm:.4f}) = {check:.2f} ✓")

    print(f"\n{'=' * 70}")
    print("STEP 5: Apply Rescaling")
    print("=" * 70)

    for r in rows:
        if r["category"] == "dinosaur":
            r["rescaled"] = r["normalized"] * dino_factor
        elif r["category"] == "mesozoic-other":
            r["rescaled"] = r["normalized"] * meso_other_factor
        else:
            r["rescaled"] = r["normalized"]

    # Show the effect
    print("\nBefore and after rescaling (selected animals):")
    print(f"  {'Animal':<45s} {'Category':<15s} {'Before':>10s} {'After':>10s} {'Factor':>8s}")
    print(f"  {'-'*45} {'-'*15} {'-'*10} {'-'*10} {'-'*8}")

    showcase = [
        "Tyrannosaurus rex", "Dakotaraptor steini", "Velociraptor mongoliensis",
        "Triceratops horridus", "Allosaurus fragilis",
        "Mosasaurus hoffmannii", "Pliosaurus funkei", "Pteranodon longiceps",
        "Lion", "Tiger", "African Bush Elephant",
        "Grizzly Bear", "Grey Wolf", "Human",
        "Smilodon fatalis", "Woolly Mammoth",
    ]
    for name in showcase:
        entry = find_entry(rows, name)
        if entry:
            before = entry["normalized"]
            after = entry["rescaled"]
            factor = after / before if before > 0 else 0
            cat_short = entry["category"][:12]
            print(f"  {entry['animal']:<45s} {cat_short:<15s} {before:>10.2f} {after:>10.2f} {factor:>7.2f}x")

    print(f"\n{'=' * 70}")
    print("STEP 6: Write Output")
    print("=" * 70)

    # Sort by rescaled score descending
    rows.sort(key=lambda r: -r["rescaled"])

    out_path = csv_path.rsplit(".", 1)[0] + "_rescaled.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["rank", "animal", "crowd_score", "normalized", "rescaled", "category"])
        for i, r in enumerate(rows, 1):
            writer.writerow([
                i,
                r["animal"],
                f"{r['power']:.6f}",
                f"{r['normalized']:.4f}",
                f"{r['rescaled']:.4f}",
                r["category"],
            ])

    print(f"Saved {len(rows)} entries to {out_path}")

    # Summary stats
    dino_rows = [r for r in rows if r["category"] == "dinosaur"]
    meso_rows = [r for r in rows if r["category"] == "mesozoic-other"]
    nonm_rows = [r for r in rows if r["category"] == "non-mesozoic"]

    print(f"\nMedian rescaled scores by category:")
    for label, subset in [("Dinosaur", dino_rows), ("Mesozoic-other", meso_rows), ("Non-Mesozoic", nonm_rows)]:
        scores = sorted([r["rescaled"] for r in subset])
        median = scores[len(scores) // 2] if scores else 0
        print(f"  {label:<15s}: {median:>10.2f}")

    # How many dinosaurs now outrank the top non-mesozoic?
    top_nonmeso = max(r["rescaled"] for r in nonm_rows)
    dinos_above = sum(1 for r in dino_rows if r["rescaled"] > top_nonmeso)
    print(f"\nDinosaurs scoring above top non-Mesozoic ({top_nonmeso:.0f}): {dinos_above}")

    return out_path


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "duels_ratings_classified.csv"
    rows = load_classified(csv_path)
    print(f"Loaded {len(rows)} entries.\n")
    out_path = rescale(rows, csv_path)
