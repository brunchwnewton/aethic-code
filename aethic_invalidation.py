"""
Aethic Reasoning — Powerset Invalidation Algorithm
====================================================

Given n slits and a set of detectors (each an OR over some subset of slits),
this script classifies every element of the powerset of slits as:

  VALID : legitimate agreeing superposition
  P2    : invalidated by the Second Postulate (unknowing / over-specific)
  P3    : invalidated by the Third Postulate (checkmate / contradictory)

The algorithm:
  1. Compute each slit's "detector signature" — which detectors fire when
     only that slit is open.
  2. Group slits into equivalence classes by identical signature. Slits in
     the same class are observationally indistinguishable.
  3. For each subset of the powerset:
     - Empty set → always VALID.
     - Exactly matches a full equivalence class → VALID.
     - Proper subset within a single equivalence class → P2.
       (Asserts specificity the detectors cannot support.)
     - Spans multiple equivalence classes → P3.
       (Detectors can distinguish members, creating an accessible
       contradiction — the "checkmate" condition.)

Usage:
  python3 aethic_invalidation.py

For custom configurations, call classify_powerset() or print_results()
directly. Each detector is specified as a set of slit indices (0-indexed)
representing which slits cause it to fire (OR logic).

Reference:
  Benander, A. (2024). Aethic Reasoning: A Comprehensive Solution to the
  Quantum Measurement Problem. https://philpapers.org/rec/BENARA-5
"""

from itertools import combinations


def classify_powerset(n_slits: int, detectors: list[set[int]]) -> tuple:
    """
    Parameters
    ----------
    n_slits   : number of slits (labelled 0 .. n_slits-1)
    detectors : list of sets; each set contains the slit indices
                that cause that detector to fire (OR logic).

    Returns
    -------
    results     : list of dicts with 'subset', 'label', 'status'
    eq_classes  : list of frozensets (the equivalence classes)
    slit_names  : list of single-character slit labels
    """
    slit_names = [chr(ord('A') + i) for i in range(n_slits)]

    # Step 1: detector signature per slit
    signatures = []
    for s in range(n_slits):
        sig = tuple(s in det for det in detectors)
        signatures.append(sig)

    # Step 2: equivalence classes
    class_map = {}
    for s, sig in enumerate(signatures):
        class_map.setdefault(sig, []).append(s)
    eq_classes = [frozenset(members) for members in class_map.values()]

    # Step 3: classify each powerset element
    results = []
    for size in range(n_slits + 1):
        for combo in combinations(range(n_slits), size):
            subset = frozenset(combo)

            if len(subset) == 0:
                status = "VALID"
            elif subset in eq_classes:
                status = "VALID"
            elif _within_one_class(subset, signatures):
                status = "P2"
            else:
                status = "P3"

            label = _format_subset(subset, slit_names)
            results.append({"subset": subset, "label": label, "status": status})

    return results, eq_classes, slit_names


def _within_one_class(subset, signatures):
    """True if every slit in the subset shares the same detector signature."""
    members = list(subset)
    first = signatures[members[0]]
    return all(signatures[s] == first for s in members)


def _format_subset(subset, names):
    if not subset:
        return "∅"
    return "{" + ", ".join(names[i] for i in sorted(subset)) + "}"


# ── Pretty-printing ──────────────────────────────────────────

_SYMBOLS = {"VALID": "✓", "P2": "✗ P2", "P3": "✗ P3"}


def print_results(n_slits, detectors):
    """Run classification and print a formatted table."""
    results, eq_classes, names = classify_powerset(n_slits, detectors)

    print(f"\n{'═' * 56}")
    print(f"  Slits : {', '.join(names)}")
    print(f"  Detectors:")
    for i, det in enumerate(detectors):
        det_label = " ∨ ".join(names[s] for s in sorted(det)) if det else "(none)"
        print(f"    {chr(0x03B1 + i)} blinks if : {det_label}")
    print(f"  Equivalence classes: ", end="")
    print(", ".join(_format_subset(cls, names) for cls in eq_classes))
    print(f"{'═' * 56}\n")

    counts = {"VALID": 0, "P2": 0, "P3": 0}
    for r in results:
        sym = _SYMBOLS[r["status"]]
        print(f"  {sym:>6}  {r['label']}")
        counts[r["status"]] += 1

    print(f"\n  Summary: {counts['VALID']} valid, "
          f"{counts['P2']} pruned by P2 (unknowing), "
          f"{counts['P3']} pruned by P3 (checkmate)")
    print(f"  Total:   {sum(counts.values())} / 2^{n_slits} = {2**n_slits}\n")


# ── Examples ─────────────────────────────────────────────────

if __name__ == "__main__":

    print("▸ Example 1 — 4 slits, detector on A ∨ B")
    print_results(4, [{0, 1}])

    print("▸ Example 2 — 3 slits, no detectors (full agreeing superposition)")
    print_results(3, [])

    print("▸ Example 3 — 3 slits, fully observed (particle pattern)")
    print_results(3, [{0}, {1}, {2}])

    print("▸ Example 4 — 5 slits, two detectors")
    print_results(5, [{0, 1}, {2, 3, 4}])
