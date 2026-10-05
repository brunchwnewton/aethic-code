#!/usr/bin/env python3
"""Step 5 — the probabilistic anatomy rescaling (replaces the earlier 5_rescale_dinos.py).

Usage:  python3 5_rescale_dinos.py     reads outputs/bt_scores_classified.csv
                                       -> outputs/bt_scores_african_lion_100.csv, outputs/anatomy_model.json

The earlier script normalized to a "big cat" (the geometric mean of lion and tiger clusters) and applied one fixed
dinosaur factor chosen so that geomean(Dakotaraptor, Human) = 100. This version follows the paper (Section 6):
  - scores stay on the African Lion = 100 scale of step 3;
  - the calibration ladder places Dakotaraptor above the African Lion by the African Lion's ratio over Human,
    D_target = 100^2 / Human; that strong factor is shrunk once in log space, L = sqrt(D_target / Dakotaraptor), and
    paired with the direct Utahraptor factor U = D_target / Utahraptor;
  - the anatomy factor is lognormal, log F ~ N(mu, sigma^2), with mu = (2/3) log L + (1/3) log U and sigma chosen so
    that 15% of the probability lies outside [L, U];
  - dinosaurs take F, Mesozoic-other animals sqrt(F), baseline animals 1; the table reports the median and the
    one-log-SD band.
The ladder runs on the African Lion, a population, not the generic Lion, whose cultural inflation would enter it
squared; the generic-Lion version is reported in anatomy_model.json as a sensitivity."""
import json
import numpy as np, pandas as pd
from scipy import stats, optimize


def elicit(anchor, human, dakota, utah):
    Dt = anchor**2 / human; strong = Dt / dakota; L = np.sqrt(strong); U = Dt / utah
    mu = (2 / 3) * np.log(L) + (1 / 3) * np.log(U)
    sigma = optimize.brentq(lambda s: stats.norm.cdf((np.log(L) - mu) / s) + 1 - stats.norm.cdf((np.log(U) - mu) / s) - .15, 1e-4, 5)
    return dict(anchor=anchor, human=human, D_target=Dt, strong=strong, L=L, U=U, mu=mu, sigma=sigma, median=np.exp(mu),
                one_sd_factor=np.exp(sigma), band_1sd=[np.exp(mu - sigma), np.exp(mu + sigma)], band_2sd=[np.exp(mu - 2 * sigma), np.exp(mu + 2 * sigma)],
                linear_mean=np.exp(mu + sigma**2 / 2), linear_sd=np.sqrt((np.exp(sigma**2) - 1) * np.exp(2 * mu + sigma**2)),
                mass_below_L=stats.norm.cdf((np.log(L) - mu) / sigma), mass_above_U=1 - stats.norm.cdf((np.log(U) - mu) / sigma))


def main():
    df = pd.read_csv('outputs/bt_scores_classified.csv'); S = dict(zip(df.animal, df.score))
    args = (S['Human'], S['Dakotaraptor steini'], S['Utahraptor ostrommaysorum'])
    model = elicit(S['African Lion'], *args); sens = elicit(S['Lion'], *args)
    mu, sigma = model['mu'], model['sigma']
    factor = {'dinosaur': np.exp(mu), 'mesozoic-other': np.exp(mu / 2), 'baseline': 1.0}
    log_sd = {'dinosaur': sigma, 'mesozoic-other': sigma / 2, 'baseline': 0.0}
    df['median_factor'] = df['class'].map(factor); df['median_score'] = df.score * df.median_factor
    df['band1_low'] = df.median_score * np.exp(-df['class'].map(log_sd)); df['band1_high'] = df.median_score * np.exp(df['class'].map(log_sd))
    df.to_csv('outputs/bt_scores_african_lion_100.csv', index=False, float_format='%.6g')
    json.dump(dict(model=model, sensitivity_generic_lion_ladder=sens), open('outputs/anatomy_model.json', 'w'), indent=1, default=float)
    print(f"log F ~ N({mu:.5f}, {sigma:.5f}^2): median {np.exp(mu):.3f}x, 2-log-SD band {model['band_2sd'][0]:.3f}-{model['band_2sd'][1]:.3f}x "
          f"(ladder: Human {args[0]:.3f}, D_target {model['D_target']:.1f}, strong {model['strong']:.2f}x, L {model['L']:.3f}, U {model['U']:.3f})")
    print(f"sensitivity, ladder on the generic Lion: median {sens['median']:.3f}x")
    for a in ['Tyrannosaurus rex', 'Utahraptor ostrommaysorum', 'Dakotaraptor steini', 'Deinonychus antirrhopus', 'Velociraptor mongoliensis']:
        r = df[df.animal == a].iloc[0]; print(f"  {a:28s} crowd {r.score:10.2f} -> median {r.median_score:10.1f}  ({r.band1_low:.1f}-{r.band1_high:.1f})")
    print("wrote outputs/bt_scores_african_lion_100.csv")


if __name__ == '__main__':
    main()
