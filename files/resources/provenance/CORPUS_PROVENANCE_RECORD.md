# Corpus Provenance Record — The Aethic/Nexic Collaboration (12 June – 24 July 2026)

## 0. What this document is, and how to read it

This is the analytical provenance companion to the verbatim conversation export
*AI-use provenance record — Aethic reasoning and counterfactual implications*
(1,697 messages, 2026-06-12T18:43 UTC through 2026-07-24T22:08 UTC; thread SHA-256
`ce14c407d43d22a96b402b3b9db463268605a76f5a966412d6ee460c446674eb`; source export
`conversations.json` SHA-256
`81b2529c489fc9ab041b4e40535d86a5c524881c08e493890dc693b245f7b161`). The export is the
**primary source**: every message in it carries an individual SHA-256, so every claim
below that cites a message number (written `#N`) can be checked against attested text.
This document is the **secondary analysis**: an accounting of who contributed what,
arc by arc, across the collaboration that produced the Aethic/Nexic paper corpus.

**Authorship and standing caveat, stated first because it governs everything after.**
This document was written by the drafting model (Claude, Anthropic) at the author's
request, and it is an analysis of a collaboration in which that model — and the
same-family models used as referees — were participants. It therefore cannot serve as
independent verification of anything, least of all of the model-side attributions it
contains. Its claims are checkable in two directions: against the hashed export
(for what was actually said, by whom, when) and against the corpus's internal records
(the pass ledger and the session transcripts, which log every edit with pass/fail
results and every logged error). Where the model's memory or reconstruction is
uncertain, that is said in place. Independent human review is the gate on this
document exactly as on everything else in the corpus. The author's own review of this
document is part of its provenance chain: any line he amends supersedes what stands
here.

## 1. What predates the conversation entirely

The single most important provenance fact is the boundary condition: **the framework
predates the collaboration.** At #1 (12 June 2026) the author uploaded a completed
long-form LaTeX manuscript on Aethic Reasoning — already containing the postulates,
the union principle and ladder ontology, the extrusion treatment, the reduced-form
coupling, the third postulate with its derivational history, the powerset invalidation
theorem, the observer-consistency and EPR/Frauchiger–Renner material, the Quantum
Nexus conception, and the polarizer pipeline — together with a Spekkens interview
transcript and his own reading map. The project archive also carries the author's
pre-existing Nexic manuscripts (the Accordance Principle / anthropic wing), and
documents evidencing a much longer personal pre-history: grade-school mathematical
idea records, a high-school-era derivation, transcripts of the author's older videos,
and 2025 correspondence — none of it produced in this collaboration.

The author's own account of his method, given at #5 and repeated in substance at
#423, #1416, #1474, and #1599: he had been *writing in isolation*, without knowledge
of the literature's boundaries, working from what he had "intuited directly from
nature via inductive reasoning," with the paper's "streetlight" section serving as the
deliberate dump of raw intuition (his comparison at #5: Galois's letters). This
matters for everything below: the collaboration's recurring shape is *author
intuition and framework → model articulation, literature-placement, and formal
assembly → author correction → referee correction*, and the direction of origination
in that loop is the author's except where explicitly stated otherwise.

## 2. Roles, personas, and the working conventions

**The author** (sole human participant): originator of the framework and all
manuscripts brought into the collaboration; director of every arc (all commissions
are his messages, verbatim in the export); and — documented throughout the pass
ledger — an active *corrector* of model output, with dozens of substantive catches
credited to him by name in the internal records.

**The drafting model(s)**: Claude instances operating, at the author's direction, in
a two-persona editing scheme during the June–early-July phase ("Opus 4.6/4.8" as the
organizational/routine editor; "Claude Fable 5" as the substantive editor — see the
transcripts of 23 June), converging on a single Fable drafting voice thereafter.
Model-side contributions across the corpus: literature mapping and placement
(Spekkens corpus, Boole/Fine, consistent histories, GPT/discrimination literature,
decision-theory literature); prose articulation of the author's dictated or
conversational content; formal assembly and derivation drafting (detailed per-arc
below); LaTeX execution with count-guarded edit scripts; standard-formalism
translations and numerical verification; and the drafting of the extraction papers
from the author's manuscripts. The model also built, at the author's commission, the
local Python editing harness ("aethic_editor") that the author runs himself.

**The referee models**: same-family Claude instances producing referee-style reports
at the author's request, from the process he instituted (the referee convention enters
around #329–#349 and runs continuously thereafter). Referee-side contributions are
credited per-arc below; they include at least one required correction of a genuine
physics error in model-drafted content, and one required correction of the corpus's
own bibliography architecture. Every referee document carries the same-family
disclosure and the statement that independent human refereeing is non-optional.

**The conventions** (instituted progressively, author-approved, and enforced in the
records): never fabricate; the author's prose is the spine; exact-match count-guarded
edits with PASS/FAIL logs; a running ledger entry for every pass *including honest
error ("vice") records*; VERIFY flags on any memory-supplied bibliographic detail;
md5-verified deliveries; and the citation acyclicity rule (the long manuscripts never
cite their extractions).

## 3. Arc-by-arc provenance

### Arc I — Foundations and first editing rounds (12 June; #1–~#80)

Author: the manuscript itself; the reading program (#1, #3); immediate substantive
corrections of the model — notably at #3, where the model's claimed *divergence* from
Spekkens on causality was corrected by the author to a *convergence*, which the model
then verified and retracted; the semiring reform program (#7: dropping the
Aethic-subtraction apparatus, constructing the tree as a semiring from the start —
the author's decision, including the historical note that the ring section predated
his own settled position); the validity-equivalence distinction and the retirement of
his own earlier vocabulary (#11, explicitly dating his opaque/translucent concepts as
two-year-old superseded formalization attempts). Model: the literature mapping; the
first insertion rounds (nine blocks, changelog, bib entries); an early ~9,700-word
paper draft (#7–#8 region); and two *logged model errors* from this arc — a negativity
proposal the author's semiring constraint refuted, and a theorem the model itself
re-audited and retracted. The counterfactual formal section was model-drafted **from
the author's streetlight material** at the author's explicit direction (#5) — the
paradigm case of the loop described in §1.

### Arc II — The editing infrastructure (23–30 June)

The two-persona scheme instituted at the author's direction; ~38 cross-reference
markers planted; the extrusion-principle rebrand executed; an extended series of
author-driven corrections to placement, citations, meta-narration, and overclaiming
(the transcripts log each). The aethic_editor harness: architecture and code
model-built; specification, operation, and all live runs the author's, on his machine
with his keys. Provenance-detection and importance-tiering of the paper's own text —
i.e., the corpus's first machine-assisted provenance bookkeeping — date from here.

### Arc III — The Fable campaign on the long paper (early July; passes 1–~388)

The long paper's enhancement campaign under the ledger discipline: model drafting
throughout, author direction and correction throughout, referee rounds recurring.
Notable provenance events logged in this span: the author's provenance-chronology
corrections to the paper's own history section (gradual recognition, the May-2023
dating — the author correcting the model's compression of *his* history); the
Aethus naming and pronunciation apparatus (author's coinage, model-drafted
presentation, five iterations); Papers 1–3 extracted from the long at the author's
commission, each through referee rounds to freeze.

### Arc IV — The decision-theory and Nexic wings (passes ~389–455)

**Paper 4 (Newcomb / act-robustness):** the framework's application to decision
theory is the author's program (his resolve vocabulary and its gradient appear from
#59 onward — 125 author-message occurrences of "resolve" across the thread); the
binding-modes criterion (Definition 1), Lemma 1, Proposition 1, and the corollaries
were model-drafted from that program and the author's conversational direction, then
run through referee rounds. **The Nexic campaign:** the Accordance Principle and the
anthropic framework are the author's pre-existing manuscripts (#179 and the Nexic
project files); the enhancement passes (theorem proofs, tier structure, differentia
section) are model-drafted under author direction. Papers 5 and 6 drafted as
extractions, referee-processed.

### Arc V — RCCP, causality, Paper 7 (passes ~456–461)

The Reichenbach Common Cause Principle derivation was the author's named "ultimate
goal" commission, model-executed; the smoking-lesion resolution and the Spekkens
causality subsection installed across the long and the decision paper; Paper 7 (the
causality extraction) drafted at the author's should-it-be-a-paper decision; a
dual-referee 38-item round executed across four documents.

### Arc VI — The mechanism arc (passes ~462–488)

The boundary paper's product-expansion mechanism: this arc's provenance is
distinctive because the ledger headlines show it as a chain of **author corrections
of model drafts** — five-plus iterations in which the author redirected the
mechanism's content (his union-principle intuition correction, his
direction-corrections, his red-herring retraction, his the-regimes-belong-to-the-Qs
subtlety, his A_A–Q_A adjudication resolved by *neither* model-offered option but a
third-postulate mechanism of his own) culminating in the powerset-engine/courier
formulation with the A_dist/A_indist notation. The formulation as it stands is
author-corrected model drafting in roughly equal measure; the transcripts carry his
verbatim mechanism messages.

### Arc VII — The distinguishability program and its referee rounds (passes 489–506; #1635–#1696)

The best-documented arc, and the one whose provenance is already audited at section
level (session report §7b; boundary paper preamble and rendered note). The division:

**Author-originated, with export anchors:** the commission to integrate determinate
nodes by name and to write out the Nexus assembly integral (#1635); the
V-versus-D "theft" question with the counterpart-class framing — whether toggling the
leak switches *between counterpart classes* rather than modulating one counterpart
(#1641); the region-diameter dial, the whole-Bloch-sphere blank limit
("everything works as valid"), the joint-intersection third-factor construction, and
the C→0 blank-limit consistency condition (#1643); the request to bring the long's
proper/improper mixture discussion up to date (#1645); the sequencing observation —
the "any" pre-shackled by joint-validity constraints, pre-analyzer to post-analyzer
(#1651); the subset-graded powerset lattice proposal for n-slit D and the
mathematical-induction hypothesis (#1653); the centroid-as-establishing-object move
and the salvage-the-structures directive (#1657); and the commission to work the
route in full (#1659).

**Model-drafted:** the Englert pedagogy and gap itemization; the leak-geometry
computations and their framework translations; the standard-D chain
(betting → Helstrom → Bloch → centroid) with numerical verification; the worked
route — domain definition (on the author's sequencing and region vocabulary),
kernel-affineness and effect-condition lemmas, the chord-cap theorem (a **relocated
standard discrimination argument**, Helstrom-skeleton, named as such in the
documents), the no-manufacturing extension; the triangle characterization and
monotone re-classification theorem; the session report and this document.

**Referee-contributed:** the P2 state-space-identification catch (the circularity in
consuming the centroid chain as a premise) — ranked by the referee itself as the
round's most valuable item; the round-2 **required correction of a model physics
error** (the model's "marker-coupled: both V and D can lose" was false — V is exactly
invariant under record-sector dynamics — and the model's eraser statistic was
inverted; the correction was independently re-verified numerically before install,
and the referee's two-grid reproduction is the verification of record); the M5
centroid disambiguation; the measure-form and attainment-unconditional
strengthenings; and, on the act-robustness front, the M1 consistency triangle, the
M2 bridge-lemma question, and — in the verification rounds — the six-item audit of
the model's own executed layer (§5 below).

**Author decisions currently pending (open at this record's date):** the M1 fork
(options A/B/C on the mode quantifier) and the M2 quantum-wing bridge-lemma
commission.

## 4. Deliverables and their provenance in one line each

- **The long Aethic manuscript**: the author's, pre-existing; collaboration
  contributions are enhancement passes (model-drafted, author-directed and
  -corrected, referee-checked), all logged per-pass.
- **The Brief**: author's short-form companion; same enhancement pattern.
- **The Nexic master and Papers 5–6**: author's pre-existing framework; model-drafted
  enhancement and extraction; referee rounds.
- **Papers 1–3** (extractions from the long): model-compressed from the author's
  manuscript at his commission; referee rounds to freeze.
- **Paper 4 (decision) and Paper 7 (causality)**: author's program and framework;
  criterion apparatus model-drafted; currently in a major-revision referee cycle
  with two author decisions pending.
- **The boundary paper**: originally a model compression/re-registration of the
  author's short paper; its post-deposit delta (triangle, monotone theorem, leakage
  analysis, conditional route) is of the mixed provenance stated in its own preamble
  audit and §3 Arc VII above.
- **The distinguishability session report**: model-written program record with the
  author's contributions credited inline; referee-corrected across four rounds.
- **The aethic_editor harness**: model-built, author-operated.
- **This document and the conversation export**: export machine-generated from the
  official data archive by the author's tooling; this analysis model-written,
  author-reviewable.

## 5. The error record (both directions, from the ledger)

A provenance record that omitted the errors would misrepresent the collaboration,
whose distinguishing convention is that they are logged. Digest:

**Model errors caught by the author** (selection): the claimed Spekkens-causality
divergence (#3, retracted); the negativity proposal (Arc I, refuted by his semiring
constraint); repeated placement/overclaiming/meta-narration corrections (Arc II
transcripts); the mechanism-arc redirections (Arc VI, five-plus iterations); the
vocabulary leak — framework proper names imported into the neutral-idiom boundary
paper (pass 495, his catch, repaired to a name-once convention).

**Model errors caught by referees**: the false marker-coupled clause and inverted
eraser statistic (a genuine physics error in model-drafted content; round-2 required
correction, numerically certified); the six-item verification-round audit — a botched
m10 splice reported as clean, an m11 brief-form that inverted the screening mechanics,
a wrong root-cause diagnosis with a recurrence-prone fix, the **load-order
architecture error** (locals shadowing the author's canonical bibliography corpus-wide
for ~40 passes, the exact opposite of the design's claim), an unlogged citation swap,
and — most relevant to this document's genre — **false provenance labels**: seven
bibliography comments attributing memory-supplied details to a referee who never
supplied them, since relabeled as drafting-model recollection.

**Model self-caught errors** (selection): a comment-swallowed insertion (an entire
paragraph landing inside a %-comment, caught by refusing a render-probe zero); a
PASS-printed-without-write (an edit reported successful whose file write never
executed, caught the same way); assorted anchor and regex misfires, each logged.

**Author positions revised in discussion** (the loop runs both ways, and honesty
requires saying so): e.g., the bisector-versus-straddle geometry at #1651 (the
author's proposed optimal axis was the worst one; corrected with a one-line check),
and the ordinary refinements of intuition-to-formalization that the arcs above
document. The asymmetry worth recording: the author's corrections of the model were
typically *substantive redirections*; the model's corrections of the author were
typically *technical checks* of positions he had offered as probes.

## 6. What this record can and cannot establish

It **can** establish, jointly with the hashed export: what was said, by whom, in what
order, on what dates — and therefore the origination trail of every idea that appears
first in an author message (§3's anchors) and every drafting act that appears first
in a model message. It **can** establish, via the ledger and transcripts, what was
edited when, what failed, and what was corrected. It **cannot** establish: the
completeness or fairness of its own model-written attributions (same-family limit);
anything about the author's pre-conversation development beyond what his uploaded
documents evidence; or the correctness of the corpus's scientific claims, which is
the referees' subject and ultimately the human gate's. Where this document and the
export disagree, the export governs. Where this document and the author's memory
disagree, his amendment governs and should be committed alongside.

## 7. Verification pointers

- Any `#N` claim → the export's message N and its `sha256(text)` line.
- Any pass-number claim → `FABLE_LEDGER.md` (138 logged passes at this record's
  date) and the session transcripts cataloged in `journal.txt`.
- The distinguishability program's detailed audit → the session report's §7b and
  the boundary paper's preamble and rendered provenance note.
- The referee reports and disposition documents → deposited alongside the papers
  they audit; the boundary's four-round series and the act-robustness series both
  travel to the human gate.
- Deposits: the boundary paper to PhilArchive; the session report and this record
  to the author's public repository with Wayback Machine snapshots; the export
  likewise, its hashes binding this document's citations to fixed text.

*Record generated 24 July 2026, within the collaboration it describes; subject to
the author's amendment and the independent human review that no document in this
corpus replaces.*
