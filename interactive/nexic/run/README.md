# Dinosaur Recalibration — data pipeline

Everything needed to go from the Carnivora.net Interspecific Conflict Directory to the numbers in *Dinosaur Recalibration* (revised October 2026) and on the interactive pages.

**End result: `../final_scores.csv`**, in the nexic folder beside the paper. It holds every animal's score from the coupled model (last section): its crowd score once the entries that name one animal are pooled, its anatomy-corrected score, and error bars on both. `outputs/bt_scores_african_lion_100.csv` is the paper's own version, before the pooling; it stays as it is because the paper cites it.

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

`python3 run_3_to_7.py` runs the same five steps in order, from any folder.

Steps 3–7 run offline and take about a minute each. `verify_bradley_terry.py` (optional; needs scikit-learn) checks that step 3's objective is the Bradley–Terry likelihood, that its solution satisfies the Bradley–Terry score equations, and that an independent solver reproduces it. Steps 1–2 re-scrape the forum and need the internet. The forum's polls keep changing, so a fresh scrape will not reproduce `duels.csv` exactly.

## The paper's output: `outputs/bt_scores_african_lion_100.csv`

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

## Category graph, merged and coupled fits, error bars (added November 2026)

Two new scripts. They leave the files above unchanged: `coupled_fit.py` imports the code of steps 3–6 and refits from `duels.csv` itself, so it does not need their outputs, and its own copy of step 3's preprocessing reproduces step 3's scores exactly.

| file | does | writes |
|---|---|---|
| `category_graph.py` | links entries that name one animal: populations and subspecies under their species (taxon trees, nested: *West African Lion → African Lion → Lion*) and female or male forms to their base (*Lioness → Lion*, *Human (male) → Human*) | `category_graph.csv` (every candidate link with status, how it was found, reason), `category_graph.txt` (readable trees) |
| `coupled_fit.py` | refits under the graph, puts error bars on every score, and reruns the anatomy factor and weight–score analysis for each fit | `../final_scores.csv` (the end result), `outputs/graph/` |

```
python3 category_graph.py
python3 coupled_fit.py duels.csv      # writes ../final_scores.csv; under a minute
```

**The graph.** Taxon links come from names (a qualifier plus another entry's name, or a bracketed population such as *African Leopard (Congo)*) and from a short hand list of subspecies whose names hide the species (*Kodiak Bear → Brown Bear*, the grey wolf subspecies → *Grey Wolf*). They are vetted by step 7's rule: living populations or subspecies of the species the parent names. Other species, extinct and fossil forms and settings are cut, each with its reason. Sex links use plain sex qualifiers only; groups are left to step 3's pseudo-matchups. To switch a link on or off, flip `status` in `category_graph.csv` (rerunning `category_graph.py` rebuilds it from the tables in the script).

**Three fits**, written in the same layout:
- *original* (`outputs/graph/scores_original.csv`): the paper's fit, now with error bars.
- *merge*, variant A (`outputs/graph/scores_merge.csv`): each taxon tree becomes one animal named by its top entry; duels inside a tree are dropped.
- *coupled*, variant B (`../final_scores.csv`, the end result): every entry keeps its own score; each category gets a stand-in, a latent score tied to its members by a normal coupling (SD `tau_taxon`); each sex form is tied to its base around a common offset (SD `tau_sex`). The couplings and offsets are estimated from the votes by empirical Bayes. A broad name's row reports its stand-in, which sits at the geometric mean of its members (the Lion row is the geometric mean of the generic Lion entry, the African Lion category and the Asiatic Lion), and its own entry's score is in `entry_score`.

Each fit is on its own lion scale: the row holding the African Lion's votes reads 100.

**Columns:** `score` crowd score; `se_log` its standard error against the field (the animals outside the graph), widened for overdispersion (phi = 1.85); `crowd_p05…p95` its percentiles; `median_factor`, `median_score` as in step 5; `joint_p05…p95` percentiles of the corrected score with the elicited factor at the ladder's point estimates; `full_p05…p95` the same with the ladder redrawn with the scores (one factor per draw, shared by all dinosaurs); `rank_p05/p50/p95` percentiles of the corrected-score rank; `members` the entries behind a merged or category row. `categories.csv` sets each category's paper scores beside the merged and coupled ones. `summary.json` holds the fit settings, the anatomy model and weight–score results for each fit, the redrawn-ladder spread, the coupling estimates and the paper fit's sensitivity to step 3's ridge penalty.

## Step 8: human archetypes, and the arena page (added November 2026; exploratory, not part of the paper)

```
python3 8_human_archetypes.py      # reads ../final_scores.csv; a second or two
```

Places 30 human fighters on the scale (untrained, boxers, armed novices, hunters, gladiators by type, legionary, hoplite, knight, …) and answers how many of them match a raptor.

**Two numbers per fighter.** `score` is where the fighter stands among the animals (African Lion = 100). `duel_elo` is how the fighter does against other humans, in real odds, the untrained 70 kg man at 1000; `human_duel_matrix.csv` holds every pairing. One number cannot do both: skill between humans is worth far more against a human than against an animal.

**What is measured and what is not.** The `evidence` column grades each fighter by its weakest term.

| grade | term | source |
|---|---|---|
| A | "Human" 6.45, "Human (female)" × 0.49 | the votes |
| A | spear × 6.4, club × 1.7 | hominin entries with and without the weapon, five pairs |
| A | n animals count as n^1.44 one animal (± 0.03) | all 259 group entries against their solo entries; step 3 assumes n^0.7 |
| B | body mass | the fit's mammal exponent (1.29) on the scale; combat-sport weight studies for duels |
| C | other weapons | set relative to the spear |
| D | skill, its carry-over against animals, armour, the crowd-to-real conversion | judgment; no data set gives win rates |

Most fighters are grade D, with 90% bands near a factor of three either way. The order among them is firmer than the levels.

**Outputs:** `outputs/human_archetypes.csv`, `outputs/human_duel_matrix.csv`, `outputs/humans_vs_raptors.csv` (fighters for an even vote and vote shares at n = 1…50, for each raptor score and group exponent), `outputs/human_model.json` (every term and its spread).

**`../arena.html`** stages the bouts: n fighters against a lion, a bear or a dinosaur, the animal on its crowd score or its anatomy-corrected score. Each bout's winner is drawn with the model's vote share; the exchanges are choreography. Step 8 rewrites the page's data block (between `/*DATA*/` and `/*END DATA*/`) on every run. The page has no Jekyll front matter; add it if the site needs it.
