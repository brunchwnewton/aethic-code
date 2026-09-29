# Verification scripts: the Weight Algebra of Aethae and Aethic Reasoning

Supplementary code for the Aethic papers. Each script is self-contained, runs with Python 3 and no arguments, needs no packages beyond the standard library, and prints the counts the papers quote. Runtimes below were measured on a single core.

## Running

Keep all files in one folder and run, for example:

```
python3 weight_algebra_model_stated.py
```

`weight_algebra_model_stated.py` and `weight_algebra_broad_check.py` import `weight_algebra_model.py` from the same folder.

## What each script checks

### The Weight Algebra of Aethae

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `weight_algebra_model.py` | The fully specified finite model under the superseded default rules, the countermodel the paper keeps labeled as such | Lists carriers in *I* but not in *D* | about 1 min |
| `weight_algebra_model_stated.py` | The same model under the current rules: a blank splits only through a held carving, and closure runs the splitting rule | `\|U\| = 900  tagged 782  \|D\| = 782  \|I\| = 782  I == D: True` | about 1.5 min |
| `weight_algebra_broad_check.py` | Broad agreeing states: the passive reading against peg-wise splitting | Passive: `\|D\|=1006 \|I\|=1006 I==D:True`; peg-wise: a gap of 3 | about 2.5 min |
| `declared_descent_check.py` | Declared descent on the worked cases and on 400 random models | All violation counts 0 | about 1 s |

### Aethic Reasoning

| Script | What it checks | Expected output | Runtime |
|---|---|---|---|
| `decomposability_check.py` | The decomposability grades read in the peg formalism, and the correlated-composite example | 0 violations | about 3 s |


## Provenance

The scripts were written by Claude Fable 5.1 (Anthropic) with the author in 2026.
