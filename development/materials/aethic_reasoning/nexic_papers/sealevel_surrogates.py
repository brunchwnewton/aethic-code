# sealevel_surrogates.py — the Intrinsic Frequency test of the long Nexic paper, re-implemented from its stated procedure.
# Floor curve: 4th-order Butterworth band-pass (synthetic fs=1000, 1–50) -> Hilbert envelope u; Gaussian blur (sigma=8
# samples) of the signal (midline m) and of u; f = m - u_s. Variability: 10-Myr moving std sigma1 of f, sigma2 of sigma1.
# Seven criteria read off the Late Cretaceous window (89.75–66 Ma); detection in non-overlapping windows of 23.75 Myr;
# IAAFT surrogates (Schreiber & Schmitz 1996) of the raw signal; P_LC = fraction of surrogates with >= 1 qualifying window.
import numpy as np, pandas as pd, sys, argparse
from scipy.signal import butter, filtfilt, hilbert
from scipy.ndimage import gaussian_filter1d

def load(path='/mnt/user-data/outputs/haq1987_sealevel.txt', col=0):
    d = np.loadtxt(path); return d[:, col], d[:, 1]

def floor_curve(x, sigma=8, fs=1000.0, low=1.0, high=50.0, order=4):
    b, a = butter(order, [low / (fs / 2), high / (fs / 2)], btype='band')
    u = np.abs(hilbert(filtfilt(b, a, x)))
    m = gaussian_filter1d(x, sigma); us = gaussian_filter1d(u, sigma)
    return m - us, us

def moving_std(y, w, ddof=1):
    return pd.Series(y).rolling(w, center=True, min_periods=2).std(ddof=ddof).bfill().ffill().to_numpy()

class Pipeline:
    def __init__(self, age, x, t_young=66.0, t_old=89.75, dur=23.75, var_win_myr=10.0, sigma=8, band=(1.0, 50.0), fs=1000.0, ddof=1):
        self.age, self.x, self.sigma, self.band, self.fs, self.ddof = age, x, sigma, band, fs, ddof
        N = len(x); self.dt = (age[-1] - age[0]) / (N - 1)
        self.wv = max(3, int(round(var_win_myr / self.dt))); self.W = int(np.floor(dur / self.dt))
        self.lc = (age >= t_young) & (age <= t_old)
        f, us, s1, s2 = self.series(x)
        L = self.lc
        self.thr = dict(fmin=f[L].min(), s1min=s1[L].min(), s2min=s2[L].min(), df=f[L].max() - f[L].min(),
                        umax=us[L].max(), s1max=s1[L].max(), s2max=s2[L].max())
    def series(self, x):
        f, us = floor_curve(x, self.sigma, self.fs, *self.band)
        s1 = moving_std(f, self.wv, self.ddof); s2 = moving_std(s1, self.wv, self.ddof)
        return f, us, s1, s2
    def detect(self, x):
        f, us, s1, s2 = self.series(x); t = self.thr; W = self.W; hits = []; i = 0; N = len(x)
        while i + W <= N:
            sl = slice(i, i + W); fw = f[sl]
            ok = (fw.min() >= t['fmin'] and s1[sl].min() <= t['s1min'] and s2[sl].min() <= t['s2min'] and
                  fw.max() - fw.min() <= t['df'] and us[sl].max() <= t['umax'] and s1[sl].max() <= t['s1max'] and s2[sl].max() <= t['s2max'])
            if ok: hits.append(i); i += W
            else: i += 1
        return hits

def iaaft(x, rng, max_iter=300, tol=1e-6):
    N = len(x); xs = np.sort(x); amp = np.abs(np.fft.rfft(x)); y = rng.permutation(x)
    for _ in range(max_iter):
        Y = np.fft.rfft(y); y2 = np.fft.irfft(amp * np.exp(1j * np.angle(Y)), n=N)
        y_new = np.empty(N); y_new[np.argsort(y2)] = xs
        if np.max(np.abs(y_new - y)) < tol: y = y_new; break
        y = y_new
    return y

def run(pipe, n_surr, seed=1987, surrogate_floor=False):
    rng = np.random.default_rng(seed); count = 0; windows = 0
    for _ in range(n_surr):
        y = iaaft(pipe.x, rng)
        hits = pipe.detect(y)
        count += bool(hits); windows += len(hits)
    return count, windows

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, default=1000); ap.add_argument('--col', type=int, default=0)
    ap.add_argument('--sigma', type=float, default=8); ap.add_argument('--low', type=float, default=1.0); ap.add_argument('--high', type=float, default=50.0)
    ap.add_argument('--ddof', type=int, default=1); ap.add_argument('--tyoung', type=float, default=66.0); ap.add_argument('--told', type=float, default=89.75); ap.add_argument('--resample', type=float, default=0.0); ap.add_argument('--seed', type=int, default=1987); ap.add_argument('--label', default='')
    a = ap.parse_args()
    age, x = load(col=a.col)
    if a.resample > 0:
        order = np.argsort(age, kind='stable'); ag, xs = age[order], x[order]
        grid = np.arange(ag[0], ag[-1], a.resample); x = np.interp(grid, ag, xs); age = grid
    pipe = Pipeline(age, x, t_young=a.tyoung, t_old=a.told, sigma=a.sigma, band=(a.low, a.high), ddof=a.ddof)
    t = pipe.thr
    print(f"[{a.label}] N={len(x)} dt={pipe.dt:.4f} Myr  var-window={pipe.wv} samples  W={pipe.W} samples")
    print(f"   thresholds: fmin={t['fmin']:.2f} s1min={t['s1min']:.2f} s2min={t['s2min']:.2f} df={t['df']:.2f} umax={t['umax']:.2f} s1max={t['s1max']:.2f} s2max={t['s2max']:.2f}")
    print(f"   paper:      fmin=164.16 s1min=3.68 s2min=0.59 df=41.21 umax=38.64 s1max=9.27 s2max=5.81")
    hits = pipe.detect(x); print("   empirical windows:", [(round(age[i], 2), round(age[min(i + pipe.W, len(x) - 1)], 2)) for i in hits])
    if a.n > 0:
        c, w = run(pipe, a.n, seed=a.seed); p = c / a.n
        z = 1.96; den = 1 + z * z / a.n; ctr = (p + z * z / (2 * a.n)) / den; half = z * np.sqrt(p * (1 - p) / a.n + z * z / (4 * a.n * a.n)) / den
        span = age[-1] - age[0]; ratio = (1 / span) / (p / span) if p > 0 else float('inf')
        print(f"   surrogates: {c}/{a.n} fired ({w} windows) -> P_LC={p:.4f} Wilson95=[{ctr-half:.4f},{ctr+half:.4f}]  realized/intrinsic={ratio:.1f}")
