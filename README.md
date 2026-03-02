# Aethic Reasoning — Code & Demos

Companion code for [*Aethic Reasoning: A Comprehensive Solution to the Quantum Measurement Problem*](https://philpapers.org/rec/BENARA-5) by Ajax Benander.

## Contents

- **[`demo.html`](demo.html)** — Interactive browser demo. Configure slits and detectors, then watch the Second and Third Postulates prune the powerset of candidate agreeing superpositions.
- **[`aethic_invalidation.py`](aethic_invalidation.py)** — The classification algorithm in plain Python (no dependencies). Run with `python3 aethic_invalidation.py`.

## The Algorithm

```
Given n slits and a set of detectors (each fires for some subset of slits):

1. For each slit, compute its detector signature:
     sig(s) = which detectors fire when only s is open

2. Group slits by identical signature into equivalence classes.
     Slits in the same class are observationally indistinguishable.

3. For each subset S of the powerset (each candidate superposition):
     if S = ∅                   → VALID
     if S = one full class      → VALID  (no contradiction reachable)
     if S ⊂ one class (proper)  → P2: specificity no observer can access
     if S spans multiple classes → P3: future observer could find contradiction
```

## Papers

- [Main Paper](https://philpapers.org/rec/BENARA-5) — *Aethic Reasoning: A Comprehensive Solution to the Quantum Measurement Problem*
- [Short Paper](https://philpapers.org/rec/BENARA-6) — *Aethic Reasoning: Addressing the Quantum Observer Effect with Abstract Relational Logic*
- [Acespective Paper](https://philpapers.org/rec/BENNRD) — *Acespective Reasoning: Defining a Generalized Calculus Over Anthropic Parameters*

## License

MIT

## Note on Scope and Attribution

The Aethic postulates are fully general, inductive principles governing the logical structure of reality. The code in this repository does not implement the postulates themselves — it is an AI-generated algorithm (produced by Claude Opus 4.6) for a more narrow special case: OR-type detector configurations in multi-slit setups. This special case was devised by Ajax Benander as a pedagogical tool in [*A Prelude to Active Reasoning*](https://philpapers.org/archive/BENARA-5.pdf#:~:text=A%20Prelude%20to%20Active%20Reasoning) (§10 of the [main paper](https://philpapers.org/rec/BENARA-5)), serving as an accessible interface to the full integral. The underlying physics of partial which-path information affecting interference is well-established in quantum mechanics; what is original to Benander is the Aethic formulation — framing the problem as powerset pruning over equivalence classes derived from detector signatures, classified by the Second and Third Postulates. In particular, the Third Postulate carries a two-generational ontological structure (the "checkmate" condition) that this simplified algorithm streamlines into a direct check. These demonstrations are a stress-test for the postulates against a tractable case, not a logically equivalent reduction of them.
