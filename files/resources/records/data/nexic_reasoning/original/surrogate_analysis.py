"""
Surrogate-data intrinsic-frequency analysis matching the original pipeline
(no resampling, sample-based smoothing) with seven self-calibrated criteria.

Pipeline is intentionally identical to the original analysis script:
  - no resampling of the input data
  - bandpass: fs=1000, lowcut=1, highcut=50
  - Gaussian smoothing: sigma=8 samples
  - local-std window: 10 Myr (converted to samples via mean dt)

Seven criteria, calibrated from the LC itself:
  (1) trough              >= min(trough_LC)        throughout
  (2) first_var           <= min(first_var_LC)     at some point
  (3) second_var          <= min(second_var_LC)    at some point
  (4) max(trough) - min(trough) over window <= range(trough_LC)
  (5) smoothed_envelope   <= max(envelope_LC)      throughout
  (6) first_var           <= max(first_var_LC)     throughout
  (7) second_var          <= max(second_var_LC)    throughout

Window size for detection is fixed at the number of samples spanning the
LC's own duration (using the mean dt of the dataset).

Usage:
    python paper_surrogate.py diagnose
    python paper_surrogate.py run
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import hilbert, butter, filtfilt
from scipy.ndimage import gaussian_filter1d, uniform_filter1d


CSV              = "sea levels.csv"
LC_START_MYA     = 66.0
LC_END_MYA       = 89.75
N_SURROGATES     = 5000
RNG_SEED         = None


# ---------- pipeline (matches the original analysis script verbatim) ----------

def local_std(x, window):
    x2 = x ** 2
    mean_x2 = uniform_filter1d(x2, size=window)
    mean_x = uniform_filter1d(x, size=window)
    return np.sqrt(np.maximum(mean_x2 - mean_x ** 2, 0))


def bandpass_filter(signal, fs, lowcut, highcut, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [lowcut / nyq, highcut / nyq], btype="band")
    return filtfilt(b, a, signal)


def run_pipeline(signal, dt, fs=1000, lowcut=1, highcut=50,
                 smoothing=8, time_breadth=10):
    """Returns (trough, first_var, second_var, smoothed_envelope).
    Parameters intentionally match the original analysis script."""
    filtered = bandpass_filter(signal, fs, lowcut, highcut)
    envelope = np.abs(hilbert(filtered))
    smoothed_envelope = gaussian_filter1d(envelope, sigma=smoothing)
    smoothed_signal = gaussian_filter1d(signal, sigma=smoothing)
    trough = smoothed_signal - smoothed_envelope
    w = max(1, int(time_breadth / dt))
    return trough, local_std(trough, w), local_std(local_std(trough, w), w), smoothed_envelope


# ---------- data loading (no resampling) ----------

def load_signal(csv_path=CSV):
    """Load, dedupe (average ties), sort. No resampling."""
    df = pd.read_csv(csv_path)
    time_col, sig_col = df.columns[0], df.columns[1]
    df = df.groupby(time_col, as_index=False)[sig_col].mean()
    df = df.sort_values(by=time_col)
    return df[time_col].values, df[sig_col].values


# ---------- calibration ----------

def calibrate_from_lc(time, trough, fv, sv, env):
    in_lc = (time >= LC_START_MYA) & (time <= LC_END_MYA)
    if not in_lc.any():
        raise ValueError("LC interval not present")
    return {
        "floor_t":    float(np.min(trough[in_lc])),
        "var_min_t":  float(np.min(fv[in_lc])),
        "sec_min_t":  float(np.min(sv[in_lc])),
        "range_t":    float(np.max(trough[in_lc]) - np.min(trough[in_lc])),
        "env_t":      float(np.max(env[in_lc])),
        "var_max_t":  float(np.max(fv[in_lc])),
        "sec_max_t":  float(np.max(sv[in_lc])),
        "duration":   float(LC_END_MYA - LC_START_MYA),
    }


# ---------- detection ----------

def find_windows(trough, fv, sv, env, dt, c):
    n = len(trough)
    W = int(c["duration"] / dt)
    if W >= n:
        return []
    floor_ok   = trough >= c["floor_t"]
    var_min_ok = fv     <= c["var_min_t"]
    sec_min_ok = sv     <= c["sec_min_t"]
    env_ok     = env    <= c["env_t"]
    var_max_ok = fv     <= c["var_max_t"]
    sec_max_ok = sv     <= c["sec_max_t"]
    cs_bad_floor   = np.concatenate([[0], np.cumsum((~floor_ok).astype(np.int64))])
    cs_bad_env     = np.concatenate([[0], np.cumsum((~env_ok).astype(np.int64))])
    cs_bad_var_max = np.concatenate([[0], np.cumsum((~var_max_ok).astype(np.int64))])
    cs_bad_sec_max = np.concatenate([[0], np.cumsum((~sec_max_ok).astype(np.int64))])
    cs_var_min     = np.concatenate([[0], np.cumsum(var_min_ok.astype(np.int64))])
    cs_sec_min     = np.concatenate([[0], np.cumsum(sec_min_ok.astype(np.int64))])
    windows = []
    i = 0
    while i + W < n:
        j = i + W
        if (cs_bad_floor[j]   - cs_bad_floor[i]   == 0 and
            cs_var_min[j]     - cs_var_min[i]     >= 1 and
            cs_sec_min[j]     - cs_sec_min[i]     >= 1 and
            cs_bad_env[j]     - cs_bad_env[i]     == 0 and
            cs_bad_var_max[j] - cs_bad_var_max[i] == 0 and
            cs_bad_sec_max[j] - cs_bad_sec_max[i] == 0):
            if (trough[i:j].max() - trough[i:j].min()) <= c["range_t"]:
                windows.append((i, j))
                i = j
                continue
        i += 1
    return windows


# ---------- IAAFT ----------

def iaaft_surrogate(x, n_iter=200, rng=None, tol=1e-8):
    if rng is None: rng = np.random.default_rng()
    n = len(x)
    sorted_x = np.sort(x)
    target_mag = np.abs(np.fft.rfft(x))
    y = rng.permutation(x).astype(float)
    prev = None
    for _ in range(n_iter):
        Y = np.fft.rfft(y)
        y = np.fft.irfft(target_mag * np.exp(1j * np.angle(Y)), n=n)
        ranks = np.argsort(np.argsort(y))
        y = sorted_x[ranks]
        if prev is not None and np.max(np.abs(y - prev)) < tol:
            break
        prev = y.copy()
    return y


# ---------- diagnose ----------

def diagnose():
    time, signal = load_signal()
    dt = float(np.mean(np.diff(time)))
    n = len(signal)
    print(f"loaded {n} samples; mean dt ≈ {dt:.4f} Myr; span = {time[-1]-time[0]:.1f} Myr")

    trough, fv, sv, env = run_pipeline(signal, dt)
    c = calibrate_from_lc(time, trough, fv, sv, env)

    print(f"\ncalibrated from LC ({LC_START_MYA} – {LC_END_MYA} Mya):")
    print(f"  (1) floor          >= {c['floor_t']:.3f} m   (throughout)")
    print(f"  (2) first-var min  <= {c['var_min_t']:.3f} m   (touch)")
    print(f"  (3) second-var min <= {c['sec_min_t']:.3f} m   (touch)")
    print(f"  (4) trough range   <= {c['range_t']:.3f} m")
    print(f"  (5) envelope       <= {c['env_t']:.3f} m   (throughout)")
    print(f"  (6) first-var max  <= {c['var_max_t']:.3f} m   (throughout)")
    print(f"  (7) second-var max <= {c['sec_max_t']:.3f} m   (throughout)")
    print(f"  window: {c['duration']:.2f} Myr ≈ {int(c['duration']/dt)} samples")

    wins = find_windows(trough, fv, sv, env, dt, c)
    print(f"\ndetected {len(wins)} window(s) in real signal:")
    for (a, b) in wins:
        print(f"  {time[a]:.1f} → {time[b-1]:.1f} Mya")

    fig, axs = plt.subplots(4, 1, figsize=(12, 11), sharex=True)
    axs[0].plot(time, signal, lw=0.6, color="gray", label="signal")
    axs[0].plot(time, trough, lw=1.0, color="blue", label="trough")
    axs[0].axhline(c["floor_t"], color="red", ls="--",
                   label=f"floor ≥ {c['floor_t']:.1f}")
    axs[0].set_ylabel("sea level"); axs[0].grid(alpha=0.3); axs[0].legend(loc="upper right", fontsize=8)
    axs[1].plot(time, env, color="purple", label="envelope")
    axs[1].axhline(c["env_t"], color="red", ls="--", label=f"≤ {c['env_t']:.1f}")
    axs[1].set_ylabel("envelope"); axs[1].grid(alpha=0.3); axs[1].legend(loc="upper right", fontsize=8)
    axs[2].plot(time, fv, color="C2", label="first-order var")
    axs[2].axhline(c["var_min_t"], color="red", ls="--",
                   label=f"min ≤ {c['var_min_t']:.2f}")
    axs[2].axhline(c["var_max_t"], color="orange", ls=":",
                   label=f"max ≤ {c['var_max_t']:.2f}")
    axs[2].set_ylabel("first-order var"); axs[2].grid(alpha=0.3); axs[2].legend(loc="upper right", fontsize=8)
    axs[3].plot(time, sv, color="C3", label="second-order var")
    axs[3].axhline(c["sec_min_t"], color="red", ls="--",
                   label=f"min ≤ {c['sec_min_t']:.2f}")
    axs[3].axhline(c["sec_max_t"], color="orange", ls=":",
                   label=f"max ≤ {c['sec_max_t']:.2f}")
    axs[3].set_ylabel("second-order var"); axs[3].set_xlabel("Mya")
    axs[3].grid(alpha=0.3); axs[3].legend(loc="upper right", fontsize=8)
    for ax in axs:
        ax.axvspan(LC_START_MYA, LC_END_MYA, alpha=0.15, color="red")
        for (a, b) in wins:
            ax.axvspan(time[a], time[b-1], alpha=0.25, color="green")
    fig.suptitle("Seven-criterion detection (original pipeline)")
    plt.tight_layout()
    plt.savefig("criteria_diagnostic.png", dpi=120)
    plt.show()


# ---------- run surrogates ----------

def run_surrogates():
    time, signal = load_signal()
    dt = float(np.mean(np.diff(time)))
    span_myr = float(time[-1] - time[0])

    trough, fv, sv, env = run_pipeline(signal, dt)
    c = calibrate_from_lc(time, trough, fv, sv, env)

    print(f"loaded {len(signal)} samples, mean dt = {dt:.4f}, span {span_myr:.1f} Myr")
    print(f"thresholds:  floor≥{c['floor_t']:.2f}, "
          f"var_min≤{c['var_min_t']:.2f}, sec_min≤{c['sec_min_t']:.2f}, "
          f"range≤{c['range_t']:.2f}, env≤{c['env_t']:.2f}, "
          f"var_max≤{c['var_max_t']:.2f}, sec_max≤{c['sec_max_t']:.2f}, "
          f"window={c['duration']:.2f} Myr")

    real_wins = find_windows(trough, fv, sv, env, dt, c)
    print(f"real signal: {len(real_wins)} window(s) detected")
    for (a, b) in real_wins:
        print(f"  {time[a]:.1f} → {time[b-1]:.1f} Mya")
    if not real_wins:
        print("ERROR: LC isn't firing — abort.")
        return

    rng = np.random.default_rng(RNG_SEED)
    n_hit = 0
    n_total = 0
    for k in range(N_SURROGATES):
        sur = iaaft_surrogate(signal, rng=rng)
        t, f1, f2, e = run_pipeline(sur, dt)
        wins = find_windows(t, f1, f2, e, dt, c)
        if wins:
            n_hit += 1
            n_total += len(wins)
        if (k + 1) % 100 == 0:
            print(f"  {k+1}/{N_SURROGATES}: {n_hit} hits "
                  f"(P ≈ {n_hit/(k+1):.4f})")

    p = n_hit / N_SURROGATES
    z = 1.96
    denom = 1 + z**2 / N_SURROGATES
    center = (p + z**2 / (2*N_SURROGATES)) / denom
    half = z * np.sqrt(p*(1-p)/N_SURROGATES + z**2/(4*N_SURROGATES**2)) / denom

    print(f"\n--- result ---")
    print(f"{n_hit}/{N_SURROGATES} surrogates fired ({n_total} windows total)")
    print(f"P = {p:.4f}  (Wilson 95% CI {center-half:.4f} – {center+half:.4f})")
    if p > 0:
        print(f"intrinsic rate ≈ 1 per {span_myr/p:.2e} Myr")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "diagnose"
    if mode == "diagnose":
        diagnose()
    elif mode == "run":
        run_surrogates()
    else:
        print("Usage: python paper_surrogate.py [diagnose|run]")