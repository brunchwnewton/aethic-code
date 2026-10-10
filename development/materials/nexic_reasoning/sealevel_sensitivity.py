# sealevel_sensitivity.py — two checks on the Intrinsic Frequency test of sealevel_surrogates.py.
# (1) Run-to-run spread: the surrogate count under the canonical criteria across independent seeds.
# (2) Loosened criteria: the seven thresholds are read off the Late Cretaceous window's own extremes; here each threshold is
#     relaxed by a fraction `tol` of that quantity's standard deviation over the whole record (floors lowered, ceilings raised),
#     and two structural loosenings are run: dropping the two "touch" criteria (first- and second-order variability minima),
#     and keeping only the four "throughout" criteria. Looser criteria can only raise the surrogate rate, so these are the
#     conservative direction for the paper's ratio.
import os, math, copy, importlib.util, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('sl', os.path.join(HERE, 'sealevel_surrogates.py')); sl = importlib.util.module_from_spec(spec); spec.loader.exec_module(sl)

def detect_with(pipe, x, thr, use_touch=True, use_range=True):
    f, us, s1, s2 = pipe.series(x); W = pipe.W; hits = []; i = 0; N = len(x)
    while i + W <= N:
        sl_ = slice(i, i + W); fw = f[sl_]
        ok = (fw.min() >= thr['fmin'] and us[sl_].max() <= thr['umax'] and s1[sl_].max() <= thr['s1max'] and s2[sl_].max() <= thr['s2max'])
        if ok and use_touch: ok = s1[sl_].min() <= thr['s1min'] and s2[sl_].min() <= thr['s2min']
        if ok and use_range: ok = fw.max() - fw.min() <= thr['df']
        if ok: hits.append(i); i += W
        else: i += 1
    return hits

def relaxed(pipe, tol):
    f, us, s1, s2 = pipe.series(pipe.x); sd = dict(f=f.std(), us=us.std(), s1=s1.std(), s2=s2.std()); t = dict(pipe.thr)
    t['fmin'] -= tol * sd['f']; t['s1min'] += tol * sd['s1']; t['s2min'] += tol * sd['s2']; t['df'] += tol * sd['f']
    t['umax'] += tol * sd['us']; t['s1max'] += tol * sd['s1']; t['s2max'] += tol * sd['s2']; return t

def wilson(c, n, z=1.96):
    p = c / n; den = 1 + z*z/n; ctr = (p + z*z/(2*n))/den; half = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/den; return p, ctr-half, ctr+half

if __name__ == '__main__':
    age, x = sl.load(); pipe = sl.Pipeline(age, x)
    print("(1) run-to-run spread, canonical criteria, 1000 surrogates per seed")
    ps = []
    for seed in range(1, 11):
        c, w = sl.run(pipe, 1000, seed=seed); ps.append(c / 1000); print(f"    seed {seed:2d}: {c}/1000  P={c/1000:.4f}")
    print(f"    mean P = {np.mean(ps):.4f}  sd across seeds = {np.std(ps, ddof=1):.4f}  (binomial sd at 1000 would be {math.sqrt(np.mean(ps)*(1-np.mean(ps))/1000):.4f})")
    print("(2) loosened criteria on one surrogate set (seed 1987, 2000 surrogates)")
    rng = np.random.default_rng(1987); surr = [sl.iaaft(pipe.x, rng) for _ in range(2000)]
    span = age[-1] - age[0]
    for label, tol, touch, rangec in [("canonical (window extremes)", 0.0, True, True), ("tol 0.10 sd", 0.10, True, True), ("tol 0.25 sd", 0.25, True, True), ("tol 0.50 sd", 0.50, True, True),
                                      ("no touch criteria", 0.0, False, True), ("throughout criteria only", 0.0, False, False), ("throughout only, tol 0.25 sd", 0.25, False, False)]:
        thr = relaxed(pipe, tol); emp = detect_with(pipe, pipe.x, thr, touch, rangec)
        c = sum(bool(detect_with(pipe, y, thr, touch, rangec)) for y in surr); p, lo, hi = wilson(c, 2000)
        ratio = (1 / span) / (p / span) if p > 0 else float('inf')
        print(f"    {label:32s} empirical windows {len(emp)}  surrogates {c:4d}/2000  P={p:.4f} [{lo:.4f},{hi:.4f}]  realized/intrinsic={ratio:6.1f}")
