# Supplement: the Weight Algebra's worked finite model

`weight_algebra_current_model.py` is Python 3 with the standard library only. **Invocation:** `python3 weight_algebra_current_model.py`. It is deterministic, and its output is `expected_output.txt`.

**The model** (the worked-model section of the paper):
- A carrier P holds the single-peg carvings of two binary attributes a and b, with nothing declared between them.
- These two carvings are the fixed family, and all the splitting P declares.
- The finest cells have parent-conditional weights a1b1 0.2, a1b0 0.3, a0b1 0.4 and a0b0 0.1, at real weights.
- The tagged carriers lie outside the cone: T_a = P_a1·P_a0 and T_b = P_b1·P_b0, which hold rival values, and the all-statements carrier.

**What it checks:**
1. **Closure-independence:** the cell map is injective, and content inclusion between cells is extension of fillings.
2. **Additivity (S3)** of the coefficients.
3. **The join-semilattice:** all 36 pairs of the nine proper children have joins, and 16 pairs have no common proper child.
4. **Sample lattice operations:** a1 ∨ a0 = P and a1 ∧ b1 = a1b1.
5. **Doom** equals the tagged set, and no cell of P is doomed.
6. **The reduced form** of x = 0.2 T_a + 0.3 a1b0 + 0.4 a0b1 + 0.1 a0b0 is the truncation 0.3/0.4/0.1, and [x] = [x_V].
7. **The fully doomed combination** y = 0.5 T_a + 0.5 Hyp has no reduced form.

It computes this fragment only. It does not construct the ambient closed universe, which the paper declares rather than builds.

## License

The code is released under the MIT License; see `LICENSE` at the top of this supplement.
