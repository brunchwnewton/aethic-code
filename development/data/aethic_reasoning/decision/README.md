# Supplement: the decision paper's settling rule

`settling_benchmarks.py` is Python 3 with the standard library only. **Invocation:** `python3 settling_benchmarks.py`. There is no randomness; the output is `expected_output.txt` exactly.

## What `settle` implements (Definition `def:settle`)

On a finite DAG with one kernel per variable:
1. every replacement kernel is computed from the original kernels;
2. the act's production kernel becomes the point mass at the candidate act;
3. couplings binding in the evaluation mode (deliberation) are retained;
4. non-binding couplings are replaced jointly by K(o | pa(C), z), the act integrated out under the original production kernel, O being their outputs and Z their parents outside O and the act, so dependencies inside O are kept;
5. the result is restricted to the evidence, marginalized to the payoff-relevant variables, and normalized; a zero normalizer reports the act as inadmissible under the model.

## The benchmarks, with every input

Stakes M = 10^6 and t = 10^3 throughout. "Binding" means the coupling's mode set contains deliberation.

| Benchmark | Graph and kernels | Evidence | Binding modes | Utility | Result |
|---|---|---|---|---|---|
| Opaque Newcomb | C ∈ {one, two}, P0(C) = ½; B ∈ {full, empty} with P(B = full \| C) = 0.99 if C = one, 0.01 if C = two | none | B's coupling binding | one: M if full else 0; two: M + t if full else t | 990,000 vs 11,000 |
| Opaque, contrast | same | none | B's coupling **not** binding | same | 500,000 vs 501,000 |
| Transparent, ε = 0.01 | same, with accuracy 1 − ε | B = full | binding | same | 1,000,000 vs 1,001,000 |
| Transparent, ε = 0 | same, accuracy 1 | B = full | binding | same | two-boxing inadmissible (zero normalizer) |
| Smoking lesion | L fair; P(R = L) = 0.9; P(C = smoke \| R = 1) = 0.8, 0.2 otherwise; P(K = L) = 0.7 | R = 1 | no couplings leave C | not needed: equal settled laws of K | P(K = 1) = 0.66 under both acts |
| Psychopath button | C ∈ {press, refrain}, P0 = ½; T ∈ {psycho, not} with P(T = psycho \| C) = q1 = 0.9 if press, q0 = 0.1 if refrain | none | T's coupling binding, which is assumption (J2) in the operator's terms | press: −D if psycho, B if not (B = D = 1); refrain: 0 | −0.8 vs 0 |
| Internal dependency | C fair; O1 := C; O2 := O1, both non-binding | none | neither binding | — | the joint detached kernel keeps O1 = O2 |

Every value reproduces Table `tab:benchmarks` of the paper. The opaque contrast row shows the verdict reversing when the accuracy coupling does not bind, which is where the dependence assumption enters.

## License

The code is released under the MIT License; see `LICENSE` at the top of this supplement.
