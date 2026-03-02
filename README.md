# Aethic Reasoning — Code & Demos

Companion code for [*Aethic Reasoning: A Comprehensive Solution to the Quantum Measurement Problem*](https://philpapers.org/rec/BENARA-5) by Ajax Benander.

## Contents

- **[`demo.html`](demo.html)** — Interactive browser demo. Configure slits and detectors, then watch the Second and Third Postulates prune the powerset of candidate agreeing superpositions.
- **[`aethic_invalidation.py`](aethic_invalidation.py)** — The classification algorithm in plain Python (no dependencies). Run with `python3 aethic_invalidation.py`.

## The Algorithm

```
Given n slits and a set of detectors:

1. For each slit, compute its signature:
     sig(s) = which detectors fire when only s is open

2. Group slits into equivalence classes:
     slits with identical signatures are one class

3. For each subset S of the powerset:
     if S = ∅                        → VALID
     if S is exactly one full class  → VALID
     if S ⊂ one class (proper)      → INVALID (P2)
     if S spans multiple classes     → INVALID (P3)
```

**P2 (Second Postulate)** — the subset asserts a specificity the detectors cannot support.  
**P3 (Third Postulate)** — the detectors can distinguish members, creating an accessible contradiction (checkmate).

## Papers

- [Main Paper](https://philpapers.org/rec/BENARA-5) — *Aethic Reasoning: A Comprehensive Solution to the Quantum Measurement Problem*
- [Short Paper](https://philpapers.org/rec/BENARA-6) — *Aethic Reasoning: Addressing the Quantum Observer Effect with Abstract Relational Logic*
- [Acespective Paper](https://philpapers.org/rec/BENNRD) — *Acespective Reasoning: Defining a Generalized Calculus Over Anthropic Parameters*

## License

MIT
