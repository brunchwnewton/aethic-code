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

Places 47 human fighters on the scale and answers how many of them match a raptor: 30 with fists and blades (untrained, boxers, armed novices, hunters, gladiators by type, legionary, hoplite, knight, …) and 17 with bows and firearms (longbow, musket, pistol, revolver, shotgun, hunting rifles, assault rifle, machine guns, rocket launcher, field gun, howitzer, tank).

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
| B | hunting rifle, ordinary user: 182 (116–304) | 269 bear incidents in Alaska, in which a firearm stopped the bear in 76% (long guns) to 84% (handguns) of cases (Smith, Herrero et al. 2012), converted to the scale |
| C / D | every other bow and firearm | spaced from the rifle by Dupuy's Theoretical Lethality Index (C where he lists the weapon, D where the index is mine) |

Most fighters are grade D, with 90% bands near a factor of three either way. The order among them is firmer than the levels.

**Bows and firearms.** No vote covers them. A weapon's premium over the unarmed man is the spear's (measured) plus `BETA * log(index / 23)`, where 23 is Dupuy's index for sword or pike, and `BETA` (0.47, band 0.21–0.74) is whatever makes his 495 for the Springfield M1903 land on the bear measurement. Indices used: longbow 36, flintlock 43, M1903 495, machine gun 4,973, French 75 mm 386,530, 105 mm howitzer 657,215, medium tank 575,000 (Dupuy; a second reprint of his table gives 935,458 for the tank); pistol 150, .44 revolver 400, shotgun 450, double rifle 600, assault rifle 1,000, .50 rifle 1,200, rocket launcher 3,000, .50 machine gun 9,000 (mine). Two cautions. One number per fighter cannot say that a rifle loses less to a larger animal than a spear does, so these scores fit bear-sized animals best. And the field guns and the tank sit three orders of magnitude of index from the anchor: their 90% bands span a factor of ten either way.

In `human_duel_matrix.csv`, a fighter without a firearm who faces one keeps 30% of his blade skill and 10% of his pre-modern armour.

**Outputs:** `outputs/human_archetypes.csv`, `outputs/human_duel_matrix.csv`, `outputs/humans_vs_raptors.csv` (fighters for an even vote and vote shares at n = 1…50, for each raptor score and group exponent), `outputs/human_model.json` (every term and its spread).

**`../arena.html`** stages the bouts. Step 8 rewrites the page's data block (between `/*DATA*/` and `/*END DATA*/`) on every run. The page has no Jekyll front matter; add it if the site needs it.

- *Basic*: n fighters against m animals of one kind, with a button that sets n for an even bout.
- *Advanced*: two or three sides, each any mix. It opens on an empty arena: pick a kind from the list under a side to place one of it, then change how many, or which, in its row.
- *Battle*: the same with larger numbers (up to 300 of a kind) and a larger arena; it opens on sixty gladiators against twelve Dakotaraptors, which the scores make an even fight (49.6%). Several of its setups are built from the armies: a Roman century of eighty by rank against twelve Dakotaraptors, a Roman army against T. rexes or against the Adamantine Guard, and the Guard, fifty strong, against thirty-four Wolfpacks, which is even (50.3%).
- Every dinosaur is offered twice, and the page names the two **accurate** (the anatomy-corrected score of `final_scores.csv`) and **conventional belief** (the crowd score); accurate is listed first and is the default.
- The lists run: fighters, bows and firearms, companions (dogs, horses, a camel, a fighting bull, a cheetah, an eagle), dinosaurs, wild animals, and last the titles and training schools of the author's story (Alaarn Warrior, which comes as an Alaarn, and the Titan schools; see below).
- *Characters.* `10_characters.py` builds the page's named characters into it from `characters.json`: a character is placed by one figure (odds against a plain Titan Warrior, on the scale of the author's first table) and a few traits the page knows how to play (frail, a hard strike, swift, elusive, nimble, drawn as a shade); the file says what each means and which numbers were fitted to the author's description. Step 8 runs it whenever it rewrites the page. A checkout may also hold a private `rotg_characters.json`, from which the same script writes a themed copy, `arena_rotg.html`, with further characters; neither is in git.
- *Two tabs.* The page opens on Fights (up to four kinds a side, forty of each) with six gladiators against two Dakotaraptors; Battles is the same with up to 300 of a kind. The first setups in each list are the simple illustrative ones. The earlier Basic mode is retired: its links (`#b-…`) open as the same fight. "Make it even" changes the count of the first kind on one side to bring the odds as near 50% as whole numbers allow, and a checkbox starts the sides spread out over the sand (`-s` in a link). One battle setup is a hundred lions, spread out, against the twenty-six accurate Dakotaraptors that make it even (51%).
- *Armies.* First in the lists of the advanced and battle modes are armies: one row whose number is split among its ranks in fixed shares (`ARMIES` in the page's script). The Roman army is the manipular legion's 2 : 2 : 2 : 1 of velites, hastati, principes (the legionary) and triarii; the three extra ranks are page-only classes in step 8 (`CLASSES`), and the velites' javelins are not modelled. The Adamantine Guard is 10% veteran, 50% mid, 40% new (the author's) and the Wolfpacks 60% new, 40% veteran (a guess). Both modes also offer an empty arena to start from.
- *Race.* Every fighter has a race beside it: Human, or Titan or Alaarn (the fantasy race of the author's story ROTG). A fighter is a training, arms and armour; the race is the body under them. So a Titan legionary, a Titan gun crew or an Alaarn samurai is the same class on another body. A class picked into a human or an empty row comes as a human, except the schools, which come as Titans.
- *Links.* The setup is kept in the address after `#`, in letters, digits and hyphens only (for example `#w-60f28kt-v-12xtf91`: battle, sixty of one kind against twelve of another). Each kind's code is a letter and a hash of its name, so a saved link survives a change in the lists; for a fighter the letter is its race (`f` the race the class is at home in, `t` Titan, `l` Alaarn, `h` a human of a Titan school). Links made when the Titans were fighters of their own still open. "Copy a link to this setup" copies it.

How the page turns scores into a fight, when no bow or gun is on the sand:

- **Odds.** A side's strength is (Σ s^(1/k))^k over its members, which is n^k · s for n alike. Two sides: S_A / (S_A + S_B). Three sides: each in proportion to its strength (the Luce rule; the votes are all pairwise, so this is an extension). When every unit is human, Titan or Alaarn, the odds are real odds from the duel ratings.
- **The winner is drawn first, with exactly that share.** The long-run tally is therefore the Bradley–Terry share by construction, whatever the staging below does.
- **The fight is then drawn from a fight model until it ends with that winner.** A hit takes F0 · (attacker's strength / victim's strength)^RHO of the victim's staying power (F0 = 1/3, RHO = 0.4: a T. rex downs a gladiator in one bite, an accurate Utahraptor in two, and a gladiator needs 38 hits on the T. rex). For each pair, the chance of landing an exchange is solved so that one against one gives the pair's share exactly; one tilt per side, found by simulation, makes the group fight give the group's share. A side is beaten when its last fighter is down, so a side of many weak fighters and a few strong ones fights on after the strong ones fall. F0 and RHO are staging choices and do not move the odds.
- **Check.** Run headless over 20,000 bouts per setup, the page's own engine gave the model's share to within sampling error, and every played-out fight ended with its drawn winner.

With a bow or a gun on the sand none of that applies, because range changes everything; the fight is **simulated outright** and its odds are counted from a few hundred runs. Step 8's scores for the firearms are not used. The rules, all stated assumptions (weapons in `SIM` in step 8, the rest at the top of section 3b of the page's script):

- Everyone with a weapon that shoots fires as fast as it allows, empties its magazine and reloads. A round hits with the weapon's chance for a man-sized target, more for a larger one, less beyond its sure range.
- A bullet stops what it hits with a chance that depends on its energy against 250 J × kg^0.4 (the usual minimums for game: 1,350 J for a 70 kg deer, about 7,500 J for a 5 t elephant): about one in four when the energy just meets that, one in fifty at a fifth of it. A hit that does not stop wounds, and a wound slows. A shell or a rocket kills what it hits and wounds what stands near.
- Animals and fighters without guns charge at their own speeds and strike as in the fight model above.
- A gun crew that an enemy on foot gets within seven metres of leaves its gun and is that many men with pistols; its side has then usually lost. Nothing gets into the tank but a shell or a rocket. Here too a side is beaten only when its last fighter is down.
- A Titan or an Alaarn with a firearm fires the same weapon as a human. He is a larger target and harder to stop (a share 0.7 or 0.8 of an animal's stopping energy at his weight, against a human's 0.4; `STOP`), runs faster (speed as the square root of height), draws a bow of 2.4 or 2.9 times the energy (draw weight times draw length) and, in a crew, swings a gun round 1.8 or 2.4 times as fast.
- The starting distance is a slider (10 to 200 m). It decides most of these fights: a hunter with a .30-06 stops a charging brown bear in 48% of runs from 15 m, 70% from 40 m and 97% from 100 m (the Alaskan incidents, mostly at short range, give 76% for long guns); a 75 mm gun always kills one T. rex and never survives four Dakotaraptors that start 40 m away.
- Not modelled yet: unmanned guns that fighters can run to, grenades, and tactics beyond "those trained together fire on one target".

**ROTG Titans** (`outputs/titan_classes.csv`; `TITANS`, `CLASSES` and `race_delta` in step 8). A fantasy race from the author's story ROTG, nothing to do with Attack on Titan. Placed by the rules above at the author's body sizes (Titan man 132 kg, woman 118 kg; human man 66 kg, woman 56 kg), with two added terms. `BUILD` = 1.54 is strength over a human of the same mass, set between a Neanderthal's on this scale (1.25) and a gorilla's (1.9); it counts in full with a weapon in hand. `REACH` is real log-odds per log of height (3 unarmed, 4 armed): among fighters of like size reach counts for little (in UFC records a deficit of seven inches or more still wins 37% of the time), but a Titan stands a third taller than a human. Alaarn are "the Neanderthals of the Titans": 4% shorter and 21% heavier for their height (as Neanderthal men, 78–83 kg at 164–168 cm, were against humans of this story's build), which makes a man 144 kg at 2.10 m, and stronger for their mass by the premium a Neanderthal has over a human on this scale (×1.25 on top of the Titan's). Adamantine Guard, Wolfpacks and Ascendent are training schools: the author's ladder of ratios to a Titan Warrior is kept, read as odds in a duel between two Titans, since skill carries over to animals only in part. The csv sets each class beside the author's own first guess. Those figures have no scale of their own, so `authors_rescaled` puts them on this one by making the armed, untrained man agree; only the differences between rows mean anything.

On the arena page the race is separate from the class. For every archetype step 8 computes what a Titan's or an Alaarn's body adds (`race_delta`): the race's mass and height in place of the reference man's (a class keeps its own build, so a 78 kg murmillo becomes a 147 kg Titan), the build premium, and reach; behind a bow or a gun mass and build count a quarter and reach not at all. An unarmed class gains about ×4.5 in score as a Titan, an armed one ×3.3, a rifleman ×1.4 (`race_body` in `human_model.json`). The story's plain warrior and the schools are page-only classes at the human reference body (`CLASSES`), and the page's Titans agree with `titan_classes.csv` to the last digit (step 8 asserts it). Skin colours are the author's (Titan `#ab81e4`, Alaarn `#3e3748`). How the schools are drawn is for the eye only: the Wolfpacks in black with two blades, the Adamantine Guard in bright steel behind large shields; the black is the author's, the rest are guesses (`LOOK`).
