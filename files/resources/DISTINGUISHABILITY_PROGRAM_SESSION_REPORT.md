# The Distinguishability Program: Session Report and the Worked Closure Route

**Status header, read first.** This document reports the session's developments on the
Englert/optimality frontier of the quantum boundary-classification paper, and then works
the proposed closure route in full. Its grade is mixed by design and stamped throughout:
some sections are **checkable translations** of standard-formalism facts, some are
**in-formalism derivations at the papers' own rigor grade**, one item is a **new named
premise** (booked exactly as record-individuation is booked in the paper), and the n-slit
material is a **research program**. The companion to read alongside is the boundary paper's
Section "Beyond the Circle" (sec:beyond), which names the frontier this document proposes
to close. Following the referee's report (same-family review; independent human refereeing
remains non-optional before submission), a compressed conditional form of §5 has been
absorbed into the paper's sec:beyond per M4/Q3, with this document remaining the full
companion record; the revisions of M1–M6 and Minors 9–10 are incorporated below.

---

## 1. The base already in the papers (pre-session state)

- The circle **V² + D² ≤ 1**, equality for pure markers (Englert 1996; Greenberger–Yasin
  1988), with the paper deriving: V = c directly from the kernel's cross-term overlap;
  the analyzer family D(θ) = |sin2θ|·sin2α; the family supremum landing on √(1−c²) at
  the Bloch-orthogonal straddle; the exact per-setting port identity V_θ² + D_θ² = 1 as
  raw algebra; and the saturation c² + sin²2α = 1.
- The booked open construction: "one in-formalism definition of that supremum" — i.e.,
  the paper claimed the family-supremum and left open both the definition of an
  *arbitrary* record placement and the proof that the family attains the global optimum.

## 2. The strictness analysis (why the inequality goes strict) — *standard-formalism-checkable*

Two ways below the circle, only one of which is physics:

1. **Definitional slack**: a non-straddle reading, closed by the supremum. Not physics.
2. **Leakage (Englert's strictness)**: a third system coupled in. The coupling geometry
   splits the analysis:
   - **Path-coupled leak** (global state |i⟩|m_i⟩|E_i⟩): the reduced marker states are
     *untouched*; marker-restricted D is **invariant** under the leak toggle (still
     √(1−c²)); visibility degrades multiplicatively, **V = c·γ** with γ = ⟨E₁|E₂⟩.
     Audit: V² + D² = c²γ² + (1−c²) < 1 strictly for γ < 1.
   - **Marker-coupled leak** (any interaction confined to the record sector, environment
     initially arbitrary): the screen visibility is *exactly invariant* — screen coherence
     is the trace of the record sector's cross operator, unchanged by record-sector
     dynamics, so V holds at c — while the marker-restricted D *contracts* (trace-distance
     monotonicity under the induced channel: the no-manufacturing principle of §5.5 read
     in the marker sector) and D_tot holds at √(1−c²); losses in both quantities at once
     require combined path-and-marker couplings. [CORRECTED per round-2 referee §2: the
     previous "both V and D can lose" clause was false for the pure marker-coupled
     geometry, and the round-1 statistic was inverted; both errors verified and re-verified
     numerically before this correction was installed.]
   - **The restoration closes in both geometries**: path-coupled c²γ² + (1−c²γ²) = 1;
     marker-coupled c² + (1−c²) = 1 — "leak on or off" extends across the split.
   - **Eraser statistics discriminate the two geometries** — scoped to environment-only
     conditioning with the marker traced (joint conditioning permits full per-branch
     erasure in every pure global state and separates nothing): under path-coupling the
     conditional visibility is capped at exactly c (unconditioned cγ, restored to c at
     unbiased environment outcomes, never beyond, the untouched marker overlap multiplying
     every branch); under marker-coupling it *starts* at c and conditioning can exceed it,
     up to full per-branch erasure for copy-type couplings. Numerical certificate
     (re-verified): copy-type marker leak — V = 0.825336 = c unchanged, D_marker → 0.000000,
     D_tot = 0.564642 invariant, per-branch conditional V = 1.000000 at probabilities
     0.9127/0.0873; path-coupled γ = 0.6 — V = 0.495201 = cγ; conditioned ceiling over a
     2001-point direction scan: run output 0.825336 (analytic value c = 0.825336; the
     round-2 referee's coarser scan printed 0.825335), never exceeded.
- **The restoration**: define D_tot over the *total* record sector (marker + environment):
  D_tot = √(1−c²γ²), and **V² + D_tot² = 1 identically, leak on or off**. The equality
  never broke; the strict inequality is an **incomplete audit** — the marker-restricted D
  is only the restriction of visibility's true counterpart. The third pocket evaluates to
  C² = c²(1−γ²) (path-coupled case), and V² + D² + C² = 1 closes the same books
  (presented per M6 as the chaining of two *bipartite* identities — D_tot² = D² + C² as an
  exact decomposition, 1 − c²γ² = (1 − c²) + c²(1 − γ²) — rather than a three-term unit.
  Referee-supplied citations, all **VERIFY before any bibliography entry**: Jakob & Bergou,
  Opt. Commun. 283, 827 (2010), from quant-ph/0302075 (2003), bipartite V² + D² + C² = 1
  with C the concurrence; their PRA 76, 052107 (2007) for qudits; Englert & Bergou,
  Opt. Commun. 179, 337 (2000) on quantitative quantum erasure, adjacent for the eraser
  claims).
- **Aethic reading**: the leak opens distinguishing avenues through environment-involving
  joint elements; the third postulate's invalidation-calling prunes the *agreeing
  element's weight* — the theft is from V's Aethic weight, paid into environment-involving
  exclusive elements — while the marker sector's own element family (hence its supremum)
  stands unmoved in the path-coupled geometry.

## 3. The two-dial formalization of mixture — *new this session; framework-native*

- **Proper mixture = the region-diameter dial.** A determinate node is an or-shaped
  *subset* of its space; being pruning residue rather than posit, it inherits whatever
  measurement-error fuzziness attends its generation. Diameter → 0: the pinpoint node.
  Diameter → the whole sphere: the or-condition is satisfiable by everything — **the node
  blanks** (region-expansion *is* blanking; the second postulate read from the region
  side) and its contribution drops out.
- **Improper mixture = the third-factor dial.** An environmental circumstance Aethically
  intersected into the configuration exactly as the Bloch sphere is already paired with
  the spacetime paths; pruning runs over the joint elements. Blank the third factor (open
  it to its full any-points space) and no avenues run through it: C → 0 and the
  construction reduces to the two-factor theory. Both limits check.
- **Centroid disambiguation (per M5)**: since record statistics see preparations only
  through centroids, region *diameter* is not the operative coordinate — two equal-diameter
  regions with different centroids differ, and shape enters not at all; the dial is stated
  in centroid terms, with diameter parametrizing the symmetric case only.
- **The classically-correlated boundary case (per M5)**: path-correlated fine structure
  realizing identical maximal spreads — tags marginally blank, jointly distinguishing —
  belongs to the **third-factor dial**, not the diameter dial; the two dials partition the
  cases only after this assignment. The blank-limit check accordingly splits into two true
  statements: an *uncorrelated* full-spread tag is (V, D)-equivalent to an absent
  attribute, while a *correlated* full-spread tag is the leak case. (The dials' empirical
  discrimination inherits the corrected eraser statistic of §2: unconditioned value and
  conditioning ceiling, each direction as re-stated there.)
- Grade: the computations above are standard-formalism-checkable; **the region dial
  as a primitive is proposal-grade and carried as such** (also now stated, with the
  same stamp, in the long's Quantum Nexus introduction).

## 4. The standard definition of D, and the centroid identification — *translation, verified numerically*

Englert's D is operational betting: choose any measurement on the marker; bet the likelier
path per outcome; the which-way knowledge is K = Σ_k p_k·|P(1|k) − P(2|k)|; and
**D := max K over every possible measurement**. Three standard theorems collapse it:

1. **Helstrom**: max K = ½·Tr|ρ₁ − ρ₂| (trace distance).
2. **Qubit representation**: trace distance = ½·(Euclidean distance between Bloch vectors).
3. **Linearity**: a mixed state's Bloch vector is the convex combination of its
   components' vectors — **the centroid**.

So the standard D, pushed through the Bloch representation, *is* the centroid-chord; the
centroid is not a smoothing device but the representation's own content, because record
statistics are linear in the state and can resolve nothing finer than the mean.

**Numerical verification (α = 0.3):** c = 0.825336; √(1−c²) = 0.564642; trace distance
= 0.564642; half Bloch chord = 0.564642; sin2α = 0.564642. Mixed case (w = 0.7):
mixed-vs-pure trace distance = 0.395250 = half centroid chord = 0.395250. Attainment:
the ±eigenvectors of Δ = ρ₁ − ρ₂ overlap the straddle direction at 1.000000, eigenvalues
±0.564642 — **the optimal placement's two cells are exactly the straddle's hemispheres.**

## 5. The worked closure route

### 5.1 Definition (Admissible record placement) — *the drawn domain*

An **admissible record placement** is: a cell family {R_k} over the record sector's
attribute space — a positive normalized measure over or-shaped cells, finite partitions
the exhibited case — optionally after Aethically intersecting in any
fixed helper factor and partitioning the joint space instead — together with the record
attribute stating *which cell*, subject to the joint-validity constraints inherited from
the configuration (the slit-tag correspondence enforced by pruning: a path through slit i
failing to thread tag-node i is a joint invalidity, whatever happens in between). The
placement's **score** on marker states m₁, m₂ is the answer-gap
K = Σ_k p_k·|P(1|k) − P(2|k)| (integral form over cell measures in general) —
**equal-prior convention** (Minor 9): the score as
written assumes equal beam weights; the asymmetric generalization replaces the cap by the
trace norm of the weighted difference. Equivalently, the score is the amount of
agreeing-to-disagreeing switching the record is capable of calling.

**The premise, restated per M3 as representational completeness** (all the theorem needs,
strictly weaker than exhaustiveness-as-a-class): every postulate-admissible placement's
statistics are matched by some placement of the drawn domain. Three edges of the domain's
boundary, fenced per M3: (i) *finiteness* — **discharged** (round-2 §4): Lemma 2 restated for cell families as
positive normalized measures, and the cap's proof integrates as it sums; (ii) *adaptivity* — sequential placements
conditioning later cells on earlier outcomes should collapse into single placements on a
helper-joint by the helper-intersection clause plus deductive closure, and this is stated
as part of P1's content rather than left silent, since Englert's "any measurement"
includes them; (iii) *helper-independence* — "uncorrelated with the path at preparation"
awaits an in-formalism formulation (which attributes are blank, in which joint state) in
place of the product-state gloss.

*The sequencing observation (author's, this session), placed beside the premise as the
referee directs: the "any" is pre-shackled — every placement's statistics are assembled
under joint-validity constraints inherited from the same configuration whose separation
budget c sets the chord. This is the correct intuition for why P1 should ultimately be
dischargeable rather than permanent.*

### 5.2 Lemma 1 (Kernel-affineness) — *in-formalism, at the papers' derivation grade*

**Claim.** Every admissible placement's cell-weights are affine functionals of the marker
state's centroid data.

**Derivation.** (i) The assembly law is the residue Σ_{T valid} W(T)·T: weights attach to
whole surviving elements, linearly, with no amplitude ever edited (the paper's own
whole-element discipline — the same structure that separates the framework from
decoherence is what delivers linearity here). A cell's outcome-weight is a sum of
surviving-element weights routed to it. (ii) The kernel is the sole quantitative coupling,
and it is *pairwise-bilinear* in states: every W is a paired-kernel squared modulus, so
each cell-weight is a quadratic form in the marker state — equivalently, a linear
functional of its density/centroid data (polarization identity). (iii) Proper mixtures
enter convexly by construction: a preparation mixture is a disagreeing superposition over
configurations, its residue the convex mix of the components' residues (exactly the chord
derivation's run-ensemble mechanics); hence region-nodes enter through their weighted
centroids only. ∎ *(Grade note: (ii) is argued at the same rigor as the paper's V = c
derivation — kernel-overlap bookkeeping — not at measure-theoretic rigor; flagged.)*

### 5.3 Lemma 2 (Effect conditions, measure form) — *in-formalism; finiteness edge discharged per round-2 §4*

Cell-weights are nonnegative (the paper's own no-negative-weight identity: every W is a
squared modulus, cosine cross-terms constituents of one square) and normalize over the
cell family (exhaustiveness; the proper-Aethae total-probability law excludes improper
assignments) — with the family given as a **positive normalized measure over cells** (at the papers'
rigor grade), finite partitions the special case. Hence each placement induces positive, normalized
affine functionals — effects, in salvaged vocabulary. Since the §5.4 step
|E_k(Δ)| ≤ E_k(Δ₊) + E_k(Δ₋) integrates exactly as it sums, nothing in the proof counts
cells: the finiteness edge of M3 closes outright rather than by approximation.

### 5.4 Theorem (The chord cap)

**Claim.** For every admissible placement, K ≤ ½|r₁ − r₂| = √(1−c²) — with **attainment
itself unconditional**, exhibited in-formalism by the analyzer family's straddle pair in
analyzer terms alone; what is conditional in the theorem is that nothing beats the
exhibited winner, not that the winner exists. (In P2's representation language, the
winning pair's cells are the difference functional's positive and negative regions.)

**Proof.** Let Δ be the difference of the two marker states' centroid data and decompose
Δ = Δ₊ − Δ₋ into its positive and negative parts. For each cell functional E_k
(Lemma 2: 0 ≤ E_k, Σ_k E_k = 1), |E_k(Δ)| ≤ E_k(Δ₊) + E_k(Δ₋) (sums read as integrals over the cell measure); summing over the
family, K = ½·Σ_k|E_k(Δ)| ≤ ½·[1(Δ₊) + 1(Δ₋)] = ½·|Δ|₁ = ½|r₁ − r₂| = √(1−c²).
Attainment: the two-cell placement aligned with Δ's positive/negative regions achieves
each bound with equality — and those regions are exactly the straddle hemispheres
(verified numerically above: eigen-axis overlap 1.000000). ∎

### 5.5 Extension (No-manufacturing) — *the helper-factor half*

A *fixed* helper factor (uncorrelated with the path at preparation) multiplies both
marker cases' joint weights identically; the induced cell functionals on the joint space
restrict to effects on the same two centroids, so the cap is unchanged — intersecting
factors in adds contestants but never budget. A helper *correlated to the path at
preparation* is a different preparation: that is the leak case of §2, where capacity
**relocates** (D_tot grows, marker-restricted D unchanged) but is never manufactured —
the conservation of §2 read in the other direction. ∎

### 5.6 Corollaries and status upgrade

- **D is well-defined in-formalism, conditionally on P1 and P2**: the tournament's winner
  exists, equals the chord, and is a property of the tags (the preparation's endowment),
  not of strategy — with both premises syntactically attached wherever the claim travels.
- **The circle upgrades**: V² + D² = 1 for pure markers becomes a theorem over the drawn
  domain — visibility (the screen's own unconditioned contrast, no optimization needed)
  against optimal distinguishability (the tournament's winner) — rather than an identity
  about one exhibited family.
- **The old open construction narrows**: from "define the supremum and prove the family
  optimal" to the **two named premises** P1 and P2 of the ledger below.

## 6. The honest-status ledger

| Item | Grade |
|---|---|
| §2 leak computations (V = cγ; D-invariance; D_tot; C²) | Standard-formalism facts, translated; checkable |
| §3 region dial as primitive (centroid-stated) | **Proposal-grade** (so stamped in the long) |
| §3 third-factor construction; blank-limit checks | Framework-native; consistent both limits |
| §4 betting → trace distance → Bloch → centroid chain | Standard results (Englert; Helstrom); numerics verified |
| §5.1 domain definition | New, framework-native; candidate |
| §5.2 Lemma 1 | In-formalism at the papers' derivation grade; rigor lift open |
| §5.3 Lemma 2 | In-formalism, measure form (no-negative-weight + normalized cell measure) |
| §5.4 theorem | **Salvaged skeleton** (the standard trace-distance variational proof) with first principles relocated: linearity as a *theorem of whole-element pruning*, positivity from the kernel's square structure, the domain drawn from region-nodes + helper intersection |
| §5.5 no-manufacturing | Salvaged (ancilla-invariance of trace distance) + the framework's relocation-not-manufacture reading |
| **P1: Representational completeness** (every postulate-admissible placement's statistics are matched within the drawn domain — the M3 restatement, strictly weaker than literal domain-exhaustiveness) | **NAMED PREMISE** — booked record-individuation-style |
| **P2: State-space identification** (marker preparations faithfully represented by the ball the kernel's overlaps generate — the M2 catch: §4's centroid chain is verification *through* the standard theorems, circular if consumed as an in-formalism premise) | **SECOND NAMED PREMISE** — repair route (a): the record-equivalence quotient (preparations identified iff no admissible placement separates their statistics; affineness near-definitional on the quotient) plus a completeness/tomography lemma that the two-node cosine overlaps generate statistics separating exactly the ball's points. **The next determinate target, ranked above the n-slit program per the referee** |
| n ≥ 3 | Research program (§7) |

**The candid framing for the referee (sharpened per M1)**: Lemmas 1–2 install exactly the
structure of a generalized probabilistic theory — a convex state space with measurements
as effect families — and §5.4 is that literature's base-norm
distinguishability argument; the claim with content is that the framework *derives* the
GPT premises (convexity from run-ensemble mechanics, positivity from the kernel's square
structure, normalization from cell-family exhaustiveness) rather than assuming them. The
skeleton of §5.4–5.5 parallels Helstrom deliberately — the method is salvage-with-relocated-first-principles, and the
relocation is the content: linearity is *derived from* the whole-element/never-edit
discipline rather than postulated of observables. The program remains open in principle (not in
execution) at exactly the two named premises, P1 and P2, of the ledger above.

## 7. The n-slit program (author's induction hypothesis, with its ally and obstruction)

- For n ≥ 3 paths, **no canonical D exists in the literature** (competing inequivalent
  generalizations; no closed form for minimum-error discrimination of ≥3 states). The
  author's proposal: replace the scalar with a **subset-graded lattice** of
  distinguishabilities indexed by the nonempty slit-subsets — exactly the surviving A(T)
  terms of the Nexus expansion — with induction building n-slit from (n−1)-slit, base
  case the two-slit analysis above.
- **The ally**: the kernel is pairwise (W integrates over T × T), aligning with the
  Sorkin sum rule — no irreducible triple-slit interference — so at the *weight* level
  the framework is already pairwise-complete; induction on subset-graded weights walks
  with the grain of both the Nexus and known physics.
- **The obstruction**: at the *discrimination* level, the ≥3-state optimum is not
  determined by pairwise chords alone (Gram-type mutual geometry enters irreducibly).
- **The sharp question to probe**: whether the lattice's pairwise data *plus the
  framework's joint-validity constraints* supply exactly the Gram-type information the
  bare chords lack — which would be the induction *and* an explanation of why the scalar
  definition failed the literature.

**Absorption note (Minor 10)**: session-record glosses of the "theft is from V's Aethic
weight" kind remain here and are kept out of the absorbed paper version.

## 7b. Dated delta audit (July 2026, per the verification round's item 3)

Provenance of the boundary draft's content beyond the deposited version, section by
section, for the human gate: **the triangle characterization and the monotone
re-classification theorem** — drafted by the model within the collaboration from the
author's postulate structure and classification framework. **The leakage-geometry
analysis (Beyond the Circle)** — the coupling-geometry split and its computations are
standard-formalism facts translated by the model; the two-dial decomposition is built
on the author's conversational contributions (the region-node dial and its blank-limit
identity; the third-factor intersection pattern); the corrected leak physics is the
referee's round-2 required correction. **The compressed conditional route** — a
relocated standard discrimination argument (Helstrom-skeleton, named as such in §6),
with the domain definition built on the author's sequencing constraint and region
vocabulary, the lemmas drafted by the model, and P2's isolation the round-1 referee's
catch. **The Frauchiger–Renner footnote and the placement prose** — model-drafted,
author-reviewable. The author's framework, postulates, two-tag conception, and
conversational contributions are the substrate throughout; the drafting, translations,
and formal assembly of the delta are the model's; the corrections are the referee
rounds'. The boundary draft's preamble and rendered provenance note now carry this
mixed-provenance statement in place of the stale blanket attribution.

## 8. Questions for the referee

1. Does the domain of §5.1 read as honestly drawn from the postulates — and is booking
   its exhaustiveness as a named premise (in the record-individuation style) acceptable,
   or does the premise need discharge before any of §5 enters a paper?
2. Is Lemma 1's rigor grade (the papers' kernel-bookkeeping grade) acceptable for a
   body claim, or should §5 stand in the open-constructions section as the announced
   route until the rigor lift is done?
3. Should the boundary paper's sec:beyond absorb §5 (as a worked route with the premise
   flagged), or remain frontier-only with this document as the companion record?
4. Any objection to the two-dial mixture formalization's grade-stamps as installed in
   the long's Quantum Nexus introduction?
5. The Jakob–Bergou citation (§2) awaits the author's verification before entering any
   bibliography.
