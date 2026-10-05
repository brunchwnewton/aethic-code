#!/usr/bin/env python3
"""Step 7 — cultural score inflation (paper, Section 8; new in this revision).

Usage:  python3 7_cultural_inflation.py [duels.csv]
        reads outputs/anatomy_model.json, refits step 3 for the covariance
        -> outputs/cultural_inflation.csv, outputs/cultural_inflation.json

For each culturally named generic entry (e.g. "Lion") and its vetted populations (e.g. "African Lion", "Asiatic Lion",
"West African Lion"), the log-gap eta = log S_generic - mean log S_populations, with its standard error from the fit's
covariance. Vetting keeps only extant populations or subspecies of the species the generic name denotes. The gaps are
summarized by random-effects (DerSimonian-Laird) means for all generics, for the culturally iconic ones and for the
rest; a skew-normal SN(xi, omega, alpha) is fitted to the icons, whose location xi is the "actual" gap with the skew
turned off and whose one-sided component omega*delta*|Z| is the inflation. Composing that one-sided inflation with the
anatomy lognormal gives the "felt strength" multiplier, exactly skew-normal: SN(mu, sqrt(sigma^2 + s^2), s/sigma)."""
import sys, json, importlib.util
import numpy as np, pandas as pd
from scipy import stats

VET = {
 'Lion': ['African Lion', 'Asiatic Lion', 'West African Lion'],
 'Tiger': ['Bengal Tiger', 'Siberian Tiger', 'Sumatran Tiger', 'Indochinese Tiger'],
 'Leopard': ['African Leopard', 'Amur Leopard', 'Arabian Leopard', 'Cape Leopard', 'Indian Leopard', 'Indochinese Leopard', 'Persian Leopard', 'Sri Lankan Leopard'],
 'Jaguar': ['Mexican Jaguar', 'North American Jaguar', 'Pantanal Jaguar'],
 'Brown Bear': ['Alaskan Peninsula Brown Bear', 'Cantabrian Brown Bear', 'Coastal Brown Bear', 'East Siberian Brown Bear', 'Eurasian Brown Bear', 'Himalayan Brown Bear', 'Kamchatka Brown Bear', 'Syrian Brown Bear', 'Ussuri Brown Bear'],
 'Grizzly Bear': ['Barren Ground Grizzly Bear', 'Inland Grizzly Bear', 'Interior Grizzly Bear'],
 'Lioness': ['African Lioness', 'Asiatic Lioness'], 'Leopardess': ['African Leopardess', 'Arabian Leopardess', 'Cape Leopardess'], 'Jaguaress': ['Mexican Jaguaress'],
 'Cheetah': ['Asiatic Cheetah', 'Kalahari Cheetah'], 'Elk': ['Rocky Mountain Elk', 'Roosevelt Elk', 'Tule Elk'], 'Coyote': ['Eastern Coyote', 'Mexican Coyote', 'Northern Coyote'],
 'Red Fox': ['American Red Fox', 'Arabian Red Fox'], 'Walrus': ['Atlantic Walrus', 'Pacific Walrus'], 'Wild Boar': ['Indonesian Wild Boar', 'Ussuri Wild Boar'],
 'Gaur': ['Indian Gaur'], 'Sloth Bear': ['Sri Lankan Sloth Bear'], 'African Wild Dog': ['East African Wild Dog'], 'Mountain Zebra': ['Cape Mountain Zebra'],
 'Bighorn Sheep': ['Rocky Mountain Bighorn Sheep'], 'Mule Deer': ['Rocky Mountain Mule Deer'], 'Red Panda': ['Himalayan Red Panda'], 'Carpet Python': ['Coastal Carpet Python'],
 'Water Monitor': ['Asian Water Monitor'], 'White-throated Monitor': ['Angolan White-throated Monitor'], 'Wedge-tailed Eagle': ['Tasmanian Wedge-tailed Eagle'],
 'Leopard Cat': ['Amur Leopard Cat'], 'American Bison': ['Wood Bison'],
}
ICONS = ['Lion', 'Tiger', 'Leopard', 'Jaguar', 'Brown Bear', 'Grizzly Bear', 'Lioness', 'Leopardess', 'Jaguaress', 'Cheetah', 'American Bison', 'Walrus', 'Gaur']


def random_effects(eta, se):
    w = 1 / se**2; m = (w * eta).sum() / w.sum(); Q = (w * (eta - m)**2).sum(); C = w.sum() - (w**2).sum() / w.sum()
    tau2 = max(0.0, (Q - len(eta) + 1) / C); wr = 1 / (se**2 + tau2); mr = (wr * eta).sum() / wr.sum()
    return dict(n=int(len(eta)), mean=float(mr), se=float(np.sqrt(1 / wr.sum())), tau=float(np.sqrt(tau2)), fixed_effect_mean=float(m))


def main(path):
    spec = importlib.util.spec_from_file_location('bt', '3_bt_fit.py'); bt = importlib.util.module_from_spec(spec); spec.loader.exec_module(bt)
    names, idx, th, Sig, deg, votes, _ = bt.fit(path); S = {n: 100 * np.exp(th[idx[n]]) for n in names}
    rows = []
    for g, pops in VET.items():
        c = np.zeros(len(names)); c[idx[g]] += 1
        for p in pops: c[idx[p]] -= 1 / len(pops)
        eta = float(th[idx[g]] - np.mean([th[idx[p]] for p in pops]))
        rows.append(dict(generic=g, generic_score=S[g], populations='; '.join(pops), population_geomean=float(np.exp(np.mean([np.log(S[p]) for p in pops]))),
                         ratio=float(np.exp(eta)), eta=eta, se=float(np.sqrt(c @ Sig @ c)), generic_real_matchups=deg[g], icon=g in ICONS))
    T = pd.DataFrame(rows).sort_values('eta', ascending=False); T.to_csv('outputs/cultural_inflation.csv', index=False, float_format='%.6g')
    out = dict(all=random_effects(T.eta.values, T.se.values), icons=random_effects(T[T.icon].eta.values, T[T.icon].se.values),
               others=random_effects(T[~T.icon].eta.values, T[~T.icon].se.values),
               mann_whitney_p_icons_greater=float(stats.mannwhitneyu(T[T.icon].eta, T[~T.icon].eta, alternative='greater').pvalue))
    a, xi, om = stats.skewnorm.fit(T.eta.values)
    out['skew_normal_all'] = dict(xi=float(xi), omega=float(om), alpha=float(a), lr_vs_normal=float(2 * (stats.skewnorm(a, xi, om).logpdf(T.eta).sum() - stats.norm(T.eta.mean(), T.eta.std()).logpdf(T.eta).sum())))
    ic = T[T.icon].eta.values; a, xi, om = stats.skewnorm.fit(ic); de = a / np.sqrt(1 + a * a); s = om * de
    out['skew_normal_icons'] = dict(xi=float(xi), omega=float(om), alpha=float(a), delta=float(de), one_sided_scale=float(s), symmetric_sd=float(om * np.sqrt(1 - de * de)),
                                    mean_excess=float(s * np.sqrt(2 / np.pi)), lr_vs_normal=float(2 * (stats.skewnorm(a, xi, om).logpdf(ic).sum() - stats.norm(ic.mean(), ic.std()).logpdf(ic).sum())))
    m = json.load(open('outputs/anatomy_model.json'))['model']; mu, sig = m['mu'], m['sigma']
    om_f, al_f = np.sqrt(sig**2 + s**2), s / sig; SN = stats.skewnorm(al_f, loc=mu, scale=om_f)
    mc = np.random.default_rng(1); draws = mc.normal(mu, sig, 2_000_000) + np.abs(mc.normal(0, s, 2_000_000))
    out['felt_strength'] = dict(xi=mu, omega=float(om_f), alpha=float(al_f), location_factor=float(np.exp(mu)), median=float(np.exp(SN.median())), geometric_mean=float(np.exp(SN.mean())),
                                quantiles_5_16_50_84_95=[float(np.exp(SN.ppf(q))) for q in (.05, .1587, .5, .8413, .95)],
                                monte_carlo_check=[float(np.exp(np.percentile(draws, q))) for q in (5, 15.87, 50, 84.13, 95)])
    json.dump(out, open('outputs/cultural_inflation.json', 'w'), indent=1, default=float)
    print(f"random-effects mean log-gap: all {out['all']['mean']:+.3f}, icons {out['icons']['mean']:+.3f} ± {out['icons']['se']:.3f}, others {out['others']['mean']:+.3f}; Mann-Whitney p {out['mann_whitney_p_icons_greater']:.3f}")
    si = out['skew_normal_icons']; print(f"icon skew-normal: xi {si['xi']:+.3f}, omega {si['omega']:.3f}, alpha {si['alpha']:.2f}; felt median {out['felt_strength']['median']:.2f}x vs actual {np.exp(mu):.2f}x")
    print("wrote outputs/cultural_inflation.csv, outputs/cultural_inflation.json")


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'duels.csv')
