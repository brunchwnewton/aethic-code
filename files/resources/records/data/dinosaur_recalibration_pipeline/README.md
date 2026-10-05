# Dinosaur Recalibration — data pipeline

Everything needed to go from the Carnivora.net Interspecific Conflict Directory to the numbers in *Dinosaur Recalibration* (revised October 2026) and on the interactive pages.

| step | file | does | writes |
|---|---|---|---|
| 1 | `1_link_scraper.py` | collects the matchup thread links (original scraper) | `versus_links.txt` |
| 2 | `2_scrape_duels.py` | scrapes each matchup's poll (original scraper) | `duel.csv` (tab-separated) |
| 3 | `3_bt_fit.py` | Bradley–Terry fit, African Lion = 100, standard errors | `outputs/bt_scores.csv` |
| 4 | `4_categorize.py` | dinosaur / Mesozoic-other / baseline classes, Permian flag | `outputs/bt_scores_classified.csv` |
| 5 | `5_rescale_dinos.py` | the lognormal anatomy model and median rescaling | `outputs/bt_scores_african_lion_100.csv`, `outputs/anatomy_model.json` |
| 6 | `6_curve_fit.py` | weight–score fits, equal-mass ratios, Dark Era table | `outputs/weight_score.json`, `outputs/dark_era_table.csv` |
| 7 | `7_cultural_inflation.py` | cultural inflation of iconic generic names, felt strength | `outputs/cultural_inflation.csv`, `outputs/cultural_inflation.json` |

`duels.csv` is the scraped data the paper uses (comma-separated, no header: animal A, animal B, P(A beats B), votes); step 3 also accepts step 2's tab-separated output directly. The `outputs/` folder holds the results of a full run, so nothing needs re-running to read them.

## Running

```
pip install -r requirements.txt
python3 3_bt_fit.py duels.csv
python3 4_categorize.py
python3 5_rescale_dinos.py
python3 6_curve_fit.py
python3 7_cultural_inflation.py duels.csv
```

Steps 3–7 run offline and take about a minute each. `verify_bradley_terry.py` (optional; needs scikit-learn) checks that step 3's objective is the Bradley–Terry likelihood, that its solution satisfies the Bradley–Terry score equations, and that an independent solver reproduces it. Steps 1–2 re-scrape the forum and need the internet. The forum's polls keep changing, so a fresh scrape will not reproduce `duels.csv` exactly.

## The main output: `outputs/bt_scores_african_lion_100.csv`

| column | meaning |
|---|---|
| `score` | crowd Bradley–Terry score, African Lion = 100 |
| `log_score`, `se_log` | natural-log strength relative to the African Lion, and its standard error |
| `real_matchups`, `real_votes` | retained real matchups and their votes |
| `class` | `dinosaur`, `mesozoic-other` or `baseline` |
| `permian` | Permian control animal (baseline class) |
| `median_factor` | 3.473 for dinosaurs, 1.864 for Mesozoic-other, 1 for baseline |
| `median_score` | `score × median_factor` |
| `band1_low`, `band1_high` | one-log-SD calibration band |

## What replaced what

The earlier processing scripts (`3_power_assembler.py`, `4_categorizer.py`, `5_rescale_dinos.py`, `6_curve_fit.py`) are superseded by steps 3–6 here.

- **Step 3** keeps the earlier script's model: a penalized Bradley–Terry fit, which `3_power_assembler.py` already was. It adds:
  - restriction to the largest connected component, since a Bradley–Terry scale is only defined within a connected graph;
  - the gender and group-to-solo pseudo-matchups;
  - ASCII name cleaning with explicit corrections, plus an alias list merging 24 spelling, case and alternate-name variants of one animal, such as *Spinosaurus aegypticus* into *aegyptiacus* and "Orca" into "Orca (Killer Whale)", so that each animal's votes land on one entry, and correcting six plain typos;
  - exact Newton polishing after L-BFGS, so the Bradley–Terry score equations hold to machine precision;
  - normalization to African Lion = 100 instead of median = 1;
  - standard errors.

  The original export's manual island bridges, generic/regional duplicate links and subspecies links are not reproduced, because their lists were not preserved. As a result, 1,743 animals are fitted rather than 1,819, and generic entries such as "Lion" are placed by their own votes.
- **Step 4** keeps the earlier categorizer's 537 manual overrides, genus lists, name suffixes and group-stripping rule verbatim. It drops the Wikipedia lookup, so classification is offline and reproducible. Eight names that no rule decides default to baseline: dogs, a bird, a lizard and a Pleistocene snake, all correctly. Six fixes, each listed in the file with its reason, correct five cases where the name rules misfire and one override: *Trochosuchus acutus*, a Permian therocephalian that the original override had filed as a Mesozoic crocodile.
- **Step 5** replaces the "big cat = 100" benchmark and the single fixed dinosaur factor with the elicited lognormal anatomy model, log F ~ N(1.24511, 0.18923²) with median 3.473×. The calibration ladder is anchored on the African Lion; the generic-Lion version, 6.92×, is reported as a sensitivity.
- **Step 6** replaces the slope grid search with exact median regression. It also drops the small-mammal re-anchoring, excluding mammals below 1 kg instead as the paper states, and adds the crowd's own equal-mass ratio.
- **Step 7** is new: the cultural-inflation analysis of Section 8.

## License

The code in this package is released under the MIT License; see `LICENSE`. The MIT License does not cover `duels.csv` or the outputs derived from it, which are results of public matchup polls on the forum carnivora.net, collected by steps 1–2.
