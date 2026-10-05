# Bradley–Terry refit (Dinosaur Recalibration, October 2026)

`bt_refit.py` regenerates the crowd ratings from the scraped matchup file, so the fitted CSV can always be rebuilt:

```
python3 bt_refit.py duels.csv
```

It needs Python 3 with `numpy`, `pandas`, `scipy` and `networkx`, runs in under a minute, and writes two files:

- `bt_scores_african_lion_100.csv` — every animal of the fitted graph (1,758), ranked.
- `bt_refit_summary.json` — pipeline counts and the elicited anatomy model.

## Columns of `bt_scores_african_lion_100.csv`

| column | meaning |
|---|---|
| `rank` | rank by crowd score |
| `animal` | cleaned name |
| `score` | crowd Bradley–Terry score, **African Lion = 100** |
| `log_score` | natural-log strength relative to the African Lion |
| `se_log` | standard error of `log_score` (inverse penalized observed information) |
| `real_matchups`, `real_votes` | retained real matchups and their votes |
| `class` | `dinosaur`, `mesozoic-other` or `baseline` (by genus; paper, Section 5) |
| `permian` | Permian control animal (baseline class) |
| `median_factor` | 3.451 for dinosaurs, 1.858 (its square root) for Mesozoic-other, 1 otherwise |
| `median_score` | `score × median_factor` |
| `band1_low`, `band1_high` | one-log-SD calibration band (×/÷1.206 dinosaurs, ×/÷1.098 Mesozoic-other) |

## Pipeline

As described in the paper (Sections 2–6):

1. **Name cleaning.** An ASCII allowlist, plus a corrections dictionary for the 24 names carrying U+FFFD. Ten corrupted names merge with their clean twins.
2. **Filtering.** Matchups outside [5%, 95%] are excluded from the fitted graph.
3. **Main component.** The largest connected component of the filtered graph is kept.
4. **Gender pseudo-matchups.** Male beats base and base beats female, each at p = 0.60, weight 10.
5. **Group-to-solo pseudo-matchups.** Group beats solo with probability N^0.7/(N^0.7+1), weight 3.
6. **Fit.** Weighted Bradley–Terry likelihood with an L2 penalty of 0.01 on log-strengths, maximized by L-BFGS; standard errors from the inverse Hessian.
7. **Normalization.** African Lion = 100.
8. **Classes and the anatomy model.** Genus-based scaling classes, then the elicited lognormal anatomy model: the ladder Dakotaraptor/African Lion = African Lion/Human, shrunk once in log space, with Utahraptor as the second anchor, 2:1 log centring and 15% outside the anchors. The result is log F ~ N(1.23870, 0.18756²), median 3.451×.

## Differences from the original (lost) export

- **Not reproduced: the original pipeline's three manual augmentations**, whose lists were not preserved:
  - the 12 island bridges;
  - the generic/regional duplicate links (50%, weight 20);
  - the subspecies links (size-adjusted, weight 10).
- **Fewer animals.** The refit keeps the 1,758-animal main component rather than 1,819. Four animals of the earlier paper tables sat in formerly bridged clusters and are absent: Water Buffalo, Savannah Cat, House Mouse, Etruscan Shrew.
- **Close agreement elsewhere.** Without the duplicate links every generic entry is placed by its own votes. Most animals agree with the earlier export to within about 5% on the African Lion scale (rank correlation 0.996). The culturally iconic generics, Lion and Tiger above all, sit much higher relative to their own populations than the linked fit had them. The paper's cultural-inflation section analyses exactly this.
