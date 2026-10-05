#!/usr/bin/env python3
"""Step 6 — weight-score analysis (replaces the earlier 6_curve_fit.py).

Usage:  python3 6_curve_fit.py     reads outputs/bt_scores_african_lion_100.csv and outputs/anatomy_model.json
                                   -> outputs/weight_score.json, outputs/dark_era_table.csv

Power laws s = C w^b fitted in log-log space by median regression (least absolute deviations), solved exactly: an optimal
line passes through two data points, so every pair is tried. What changed from the earlier script: the exact solution
replaces a slope grid search; the small-mammal re-anchoring is dropped, mammals below 1 kg being excluded instead, as the
paper states; the mammal sample omits the culturally inflated generic Lion and Tiger (paper, Section 8); and the crowd's
own equal-mass ratio is computed for all and for carnivorous theropods, with bootstrap bands (paper, Section 9.3).
Masses are those of the paper's appendices and the interactive chart."""
import json, itertools
import numpy as np, pandas as pd

THEROPODS = {  # kg; the 23 theropods of the paper's Appendix A (False = excluded from the carnivorous subsample)
    'Yi qi': (0.4, False), 'Archaeopteryx lithographica': (0.9, True), 'Compsognathus longipes': (3, True), 'Ornitholestes hermanni': (12, True),
    'Linheraptor exquisitus': (12, True), 'Velociraptor mongoliensis': (15, True), 'Dromaeosaurus albertensis': (15, True), 'Coelophysis bauri': (20, True),
    'Suskityrannus hazelae': (30, True), 'Stenonychosaurus inequalis': (50, True), 'Deinonychus antirrhopus': (73, True), 'Citipati osmolskae': (75, False),
    'Moros intrepidus': (78, True), 'Liliensternus liliensterni': (130, True), 'Timurlengia euotica': (170, True), 'Ornithomimus edmontonicus': (170, False),
    'Marshosaurus bicentesimus': (200, True), 'Herrerasaurus ischigualastensis': (210, True), 'Dakotaraptor steini': (250, True),
    'Achillobator giganticus': (250, True), 'Dilophosaurus wetherilli': (400, True), 'Gallimimus bullatus': (440, False), 'Utahraptor ostrommaysorum': (500, True)}
MAMMALS = {  # kg; mammals of at least 1 kg
    'Fennec Fox': 1.2, 'Brown Hare': 3.5, 'Feral Cat': 4, 'Arctic Fox': 4, 'Fisher': 4.5, 'Red Fox': 6, 'Bobcat': 9, 'Honey Badger': 11, 'Canadian Lynx': 11,
    'Ocelot': 12, 'Caracal': 13, 'Wolverine': 14, 'Coyote': 14, 'Mandrill': 25, 'Thylacine': 25, 'Olive Baboon': 25, 'Red Wolf': 27, 'Grey Wolf': 40,
    'Cheetah': 50, 'Common Chimpanzee': 50, 'Spotted Hyena': 55, 'Leopard': 60, 'Dire Wolf': 68, 'Cougar': 70, 'Human': 70, 'African Lion': 185,
    'Lion': 190, 'Smilodon fatalis': 220, 'Tiger': 220, 'Bengal Tiger': 220, 'Siberian Tiger': 230, 'Grizzly Bear': 270, 'Polar Bear': 450, 'Arctodus simus': 800}
GENERIC = {'Lion', 'Tiger'}


def lad(pts):
    """Exact least-absolute-deviation line of log10 s on log10 w; returns (C, b)."""
    x = np.log10([p[0] for p in pts]); y = np.log10([max(p[1], 1e-3) for p in pts]); best = None
    for i, j in itertools.combinations(range(len(x)), 2):
        if abs(x[i] - x[j]) < 1e-12: continue
        b = (y[j] - y[i]) / (x[j] - x[i]); a = y[i] - b * x[i]; s = np.abs(y - a - b * x).sum()
        if best is None or s < best[0] - 1e-12: best = (s, a, b)
    return 10**best[1], best[2]


def pr(f, w): return f[0] * w**f[1]


def main():
    df = pd.read_csv('outputs/bt_scores_african_lion_100.csv'); S = dict(zip(df.animal, df.score))
    model = json.load(open('outputs/anatomy_model.json'))['model']; F, sig = model['median'], model['sigma']
    th_all = [(w, S[n]) for n, (w, c) in THEROPODS.items()]; th_carn = [(w, S[n]) for n, (w, c) in THEROPODS.items() if c]
    mam = [(w, S[n]) for n, w in MAMMALS.items() if n not in GENERIC]; mam_gen = [(w, S[n]) for n, w in MAMMALS.items()]
    fT, fC, fM, fMg = lad(th_all), lad(th_carn), lad(mam), lad(mam_gen)
    out = dict(fits=dict(theropods=fT, theropods_carnivorous=fC, mammals=fM, mammals_with_generic_lion_tiger=fMg,
                         theropods_median_calibrated=(fT[0] * F, fT[1]), theropods_median_band=(fT[0] * F * np.exp(-sig), fT[0] * F * np.exp(sig))))
    rows = []
    for w, ctx in [(.02, 'Mouse-sized'), (.1, 'Rat-sized illustrative mammal'), (2, 'Squirrel-sized'), (15, 'Fox-sized (Velociraptor)'),
                   (75, 'Human-sized (Deinonychus)'), (250, 'Lion-sized (Dakotaraptor)'), (500, 'Bear-sized (Utahraptor)')]:
        t = pr(fT, w) * F; rows.append(dict(weight_kg=w, theropod_median=t, theropod_band_low=t * np.exp(-sig), theropod_band_high=t * np.exp(sig), mammal=pr(fM, w), ratio=t / pr(fM, w), context=ctx))
    out['dark_era_table'] = rows; pd.DataFrame(rows).to_csv('outputs/dark_era_table.csv', index=False, float_format='%.6g')
    out['median_ratio_1kg'] = pr(fT, 1) * F / pr(fM, 1); out['mammal_score_100g'] = pr(fM, .1)
    out['cross_mass_ratios_vs_100g_mammal'] = {f'{w} kg': pr(fT, w) * F / pr(fM, .1) for w in (.4, 3, 15)}
    rng = np.random.default_rng(7); eq = {}
    for name, tp in [('carnivorous', th_carn), ('all', th_all)]:
        eq[name] = {'without_generic': {f'{w} kg': pr(lad(tp), w) / pr(fM, w) for w in (1, 30, 300)},
                    'with_generic': {f'{w} kg': pr(lad(tp), w) / pr(fMg, w) for w in (1, 30, 300)}}
        boot = {30: [], 300: []}
        for _ in range(1000):
            a = lad([tp[i] for i in rng.integers(0, len(tp), len(tp))]); m = lad([mam[i] for i in rng.integers(0, len(mam), len(mam))])
            for w in boot: boot[w].append(pr(a, w) / pr(m, w))
        eq[name]['bootstrap_90'] = {f'{w} kg': [float(np.percentile(v, 5)), float(np.percentile(v, 95))] for w, v in boot.items()}
    out['equal_mass_crowd_ratio'] = eq
    json.dump(out, open('outputs/weight_score.json', 'w'), indent=1, default=float)
    print(f"theropods (median-calibrated) s = {fT[0]*F:.4f} w^{fT[1]:.3f} | mammals s = {fM[0]:.4f} w^{fM[1]:.3f} | carnivorous (crowd) s = {fC[0]:.4f} w^{fC[1]:.3f}")
    c = eq['carnivorous']; print(f"crowd equal-mass ratio, carnivorous: 30 kg {c['without_generic']['30 kg']:.2f} {c['bootstrap_90']['30 kg']}, 300 kg {c['without_generic']['300 kg']:.2f} {c['bootstrap_90']['300 kg']}")
    print("wrote outputs/weight_score.json, outputs/dark_era_table.csv")


if __name__ == '__main__':
    main()
