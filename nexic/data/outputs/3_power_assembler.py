"""
Bradley-Terry Model Fitting for Animal Power Ratings
=====================================================
Given pairwise duel data (win probabilities + vote counts), fits a strength
parameter π_i to each animal such that P(i beats j) ≈ π_i / (π_i + π_j).

Works in log-space (λ_i = log π_i) for numerical stability. One animal's
λ is fixed to 0 to resolve the arbitrary scaling.
"""

import csv
import re
import sys
import unicodedata
import numpy as np
from scipy.optimize import minimize
from collections import defaultdict


def normalize_name(name):
    """Normalize an animal name to merge unicode-mangled duplicates.

    Uses an allowlist approach: keeps only characters that belong in animal
    names (letters, digits, ASCII punctuation, standard space) and replaces
    everything else — including U+FFFD replacement chars, zero-width spaces,
    non-breaking spaces, and any other encoding artifacts — with a space.
    """
    # NFC normalization: compose characters canonically
    name = unicodedata.normalize("NFC", name)
    # Allowlist: keep letters, digits, and common ASCII punctuation used in names.
    # Replace everything else with a space.
    # Valid chars: letters (any script), digits, space, and: ( ) - / ' , . & "
    cleaned = []
    for ch in name:
        if ch.isalpha() or ch.isdigit() or ch in " ()-/,.'\"&!":
            cleaned.append(ch)
        else:
            cleaned.append(" ")
    name = "".join(cleaned)
    # Collapse all whitespace runs to a single space
    name = re.sub(r" +", " ", name)
    return name.strip()


def load_duels(csv_path, p_min=0.05, p_max=0.95):
    """Load duel data from CSV: animal1, animal2, win_prob, num_votes.

    Drops matchups where win probability falls outside [p_min, p_max]
    to filter out lopsided results likely dominated by human error.
    Names are unicode-normalized to merge invisible-character duplicates.
    """
    duels = []
    dropped = 0
    raw_to_normalized = {}  # track raw->normalized mappings for diagnostics
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 4:
                continue
            raw1 = row[0].strip()
            raw2 = row[1].strip()
            a1 = normalize_name(row[0])
            a2 = normalize_name(row[1])
            # Track any names where normalization changed something
            if raw1 != a1:
                raw_to_normalized[raw1] = a1
            if raw2 != a2:
                raw_to_normalized[raw2] = a2
            try:
                p = float(row[2])
                n = float(row[3])
            except ValueError:
                continue
            if n <= 0:
                continue
            if p < p_min or p > p_max:
                dropped += 1
                continue
            duels.append((a1, a2, p, n))
    print(f"Dropped {dropped} matchups outside [{p_min}, {p_max}] win-prob range.")
    if raw_to_normalized:
        print(f"\nUnicode normalization changed {len(raw_to_normalized)} name(s):")
        for raw, norm in sorted(raw_to_normalized.items(), key=lambda x: x[1]):
            chars = [f"U+{ord(c):04X}({unicodedata.name(c, '?')})"
                     for c in raw if ord(c) > 127 or unicodedata.category(c)[0] in ("C", "Z") and c != " "]
            print(f"  {repr(raw)[:60]:60s} -> {repr(norm)}")
            if chars:
                print(f"    special chars: {', '.join(chars)}")
    else:
        print("\nNo names were changed by normalization (no invisible chars detected).")
    return duels


def build_index(duels):
    """Assign each unique animal name an integer index."""
    animals = set()
    for a1, a2, _, _ in duels:
        animals.add(a1)
        animals.add(a2)
    animals = sorted(animals)
    idx = {name: i for i, name in enumerate(animals)}
    return animals, idx


def neg_log_likelihood(lam_free, fixed_idx, duel_arrays, n_animals, reg=0.01):
    """
    Negative log-likelihood of the Bradley-Terry model with L2 regularization.

    lam_free: array of length (n_animals - 1), the free log-strength params.
    fixed_idx: index of the animal whose λ is fixed to 0.
    duel_arrays: (idx1, idx2, wins1, wins2) arrays.
    reg: L2 regularization strength (prevents infinite params for 0/1 outcomes).
    """
    # Reconstruct full λ vector
    lam = np.zeros(n_animals)
    lam[:fixed_idx] = lam_free[:fixed_idx]
    lam[fixed_idx] = 0.0
    lam[fixed_idx + 1:] = lam_free[fixed_idx:]

    idx1, idx2, w1, w2 = duel_arrays
    diff = lam[idx1] - lam[idx2]

    # log P(1 beats 2) = log σ(diff) = diff - log(1 + exp(diff))
    # Use numerically stable log-sigmoid
    log_sig_pos = -np.logaddexp(0, -diff)   # log σ(diff)
    log_sig_neg = -np.logaddexp(0, diff)    # log σ(-diff)

    nll = -np.sum(w1 * log_sig_pos + w2 * log_sig_neg)
    nll += reg * np.sum(lam ** 2)  # L2 penalty keeps params finite
    return nll


def neg_log_likelihood_grad(lam_free, fixed_idx, duel_arrays, n_animals, reg=0.01):
    """Gradient of the negative log-likelihood w.r.t. lam_free."""
    lam = np.zeros(n_animals)
    lam[:fixed_idx] = lam_free[:fixed_idx]
    lam[fixed_idx] = 0.0
    lam[fixed_idx + 1:] = lam_free[fixed_idx:]

    idx1, idx2, w1, w2 = duel_arrays
    diff = lam[idx1] - lam[idx2]

    # σ(diff) = predicted P(1 beats 2)
    sig = 1.0 / (1.0 + np.exp(-diff))

    # Residual: observed fraction minus predicted
    grad_full = np.zeros(n_animals)
    residual = w1 - (w1 + w2) * sig  # = w1*(1-sig) - w2*sig

    np.add.at(grad_full, idx1, -residual)
    np.add.at(grad_full, idx2, residual)
    grad_full += 2 * reg * lam  # L2 gradient

    # Remove the fixed index
    grad = np.concatenate([grad_full[:fixed_idx], grad_full[fixed_idx + 1:]])
    return grad


def fit_bradley_terry(csv_path):
    """
    Fit the Bradley-Terry model and return sorted power ratings.

    Returns:
        list of (animal_name, power_rating) sorted descending by rating.
    """
    duels = load_duels(csv_path)
    print(f"Loaded {len(duels)} matchups.")

    animals, idx = build_index(duels)
    n = len(animals)
    print(f"Found {n} unique animals.")

    # Build arrays for vectorized computation
    idx1 = np.array([idx[a1] for a1, a2, p, nv in duels], dtype=int)
    idx2 = np.array([idx[a2] for a1, a2, p, nv in duels], dtype=int)
    wins1 = np.array([p * nv for a1, a2, p, nv in duels])
    wins2 = np.array([(1 - p) * nv for a1, a2, p, nv in duels])
    duel_arrays = (idx1, idx2, wins1, wins2)

    # Fix animal 0 to λ=0 (arbitrary reference)
    fixed_idx = 0
    lam0 = np.zeros(n - 1)

    print("Optimizing (L-BFGS-B)...")
    result = minimize(
        neg_log_likelihood,
        lam0,
        args=(fixed_idx, duel_arrays, n),
        jac=neg_log_likelihood_grad,
        method="L-BFGS-B",
        options={"maxiter": 10000, "ftol": 1e-12},
    )

    if not result.success:
        print(f"Warning: optimizer did not fully converge: {result.message}")
    print(f"Converged in {result.nit} iterations.")

    # Reconstruct full λ vector
    lam = np.zeros(n)
    lam[:fixed_idx] = result.x[:fixed_idx]
    lam[fixed_idx] = 0.0
    lam[fixed_idx + 1:] = result.x[fixed_idx:]

    # Convert to power ratings: π = exp(λ), then normalize so median = 1
    power = np.exp(lam)
    median_power = np.median(power)
    power /= median_power  # rescale so median animal has power = 1.0

    # Sort descending
    rankings = sorted(zip(animals, power), key=lambda x: -x[1])
    return rankings


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "duels.csv"
    rankings = fit_bradley_terry(csv_path)

    print(f"\n{'Rank':<6} {'Power':>10}  Animal")
    print("-" * 60)
    for rank, (name, pw) in enumerate(rankings, 1):
        print(f"{rank:<6} {pw:>10.4f}  {name}")

    # Also save to file
    out_path = csv_path.rsplit(".", 1)[0] + "_ratings.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["rank", "animal", "power"])
        for rank, (name, pw) in enumerate(rankings, 1):
            writer.writerow([rank, name, f"{pw:.6f}"])
    print(f"\nRatings saved to {out_path}")
