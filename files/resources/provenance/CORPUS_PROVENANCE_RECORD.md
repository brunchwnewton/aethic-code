# Corpus Provenance Record — The Aethic/Nexic Collaboration (12 June – 24 July 2026)

## 0. What this document is, and how to read it

This is the analytical provenance companion to **two** verbatim conversation
exports, the author's two Claude conversations of this project in sequence. The
main export,
*AI-use provenance record — Aethic reasoning and counterfactual implications*
(1,697 messages, 2026-06-12T18:43 UTC through 2026-07-24T22:08 UTC; thread SHA-256
`ce14c407d43d22a96b402b3b9db463268605a76f5a966412d6ee460c446674eb`; source export
`conversations.json` SHA-256
`81b2529c489fc9ab041b4e40535d86a5c524881c08e493890dc693b245f7b161`), covers the
Aethic/Nexic corpus collaboration and is what the arc analysis below cites by
message number. The identity export, *Ajax Benander identity* (246 messages,
2026-06-11T01:54 UTC through 2026-06-12T19:08 UTC; thread SHA-256
`8c49b57c6cc3425a56e07daa0472324d5bbff83bb05663323e721f89e4583eb5`; same source
archive as the main export, record generated 2026-07-25), covers the
conversation the author designates as the very first, directly preceding the
main thread --- Arc 0 below. The export is the
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

### Arc 0 — The identity conversation (11–12 June 2026; the identity export's #1–#246)

The conversation the author designates as the very first, directly preceding the
main thread --- and overlapping its opening hour, running until 2026-06-12T19:08
UTC against the main thread's 18:43 start. It opens (identity-export #1) with the question ``Who is Ajax Benander?'' and
becomes, across 246 messages, the first technical engagement with the framework
--- the conversation in which the division of labor that governs everything
after was first rehearsed. Concretely, from the export:

- **Author clarifications correcting model readings of his own text.** When the
  model reported an inconsistency in the disagreeing-superposition treatment,
  the author identified it as ``just you misunderstanding the centric unfolding
  concept'' and supplied the correct reading (#9–#11): the time-travel thought
  experiments (Zoe, Jenny, the Battle of Brémule) are \emph{illustrative} of
  the extrusion principle --- past events in superposition within a block
  universe, centric unfolding determining their state --- not independent
  mechanisms. When the model developed a criterion problem about memory
  retention, the author introduced the distinction doing the real work: Aethic
  truth versus Protagorean truth/knowledge --- ``the latter is the memories,
  the former is metaphysically distinct... its own axiomatic layer established
  by and for the first postulate'' (#13). Both are cases of the author
  supplying conceptual structure the model's reading had missed; the model's
  contribution was pressing the objections that forced the articulation.
- **Model literature-placement of the author's independently derived concepts.**
  The conversation's model turns mapped framework ideas onto their literature
  counterparts by name --- the indexical character of actuality and
  counterpart-style identity (Lewis), the proper/improper mixture distinction
  (d'Espagnat), pure versus mixed states derived from first principles before
  the author knew the terminology, and the two-layer causal structure
  (Spekkens) --- convergences the model articulated precisely and the author
  had reached in isolation (#100 and surrounds).
- **Editorial execution under author direction, the author's voice preserved.**
  A representative exchange (#97–#98): the author rules on placement of a
  sentence in his own origin narrative --- ``that's supposed to go right after
  the curtain of reality line, otherwise it sounds like a hedge'' --- and the
  model repositions his wording (``hit me like a bullet in a single instant'')
  unchanged, an early instance of the author's-prose-is-the-spine convention
  before it had a name.

The identity conversation predates every convention the later record documents
--- no pass ledger, no referee process, no VERIFY flags, no count-guarded edits,
no provenance headers; the discipline documented in the arcs below was built,
not assumed, and this export preserves the collaboration's shape before it
existed.

### Arc I — Foundations and first editing rounds (12 June; #1–~#80)

Author: the manuscript itself; the reading program (#1, #3); and immediate
substantive corrections of the model, two worth unpacking as the pattern's first
instances. At #3, the model had claimed the framework *diverged* from Spekkens on
causality; the author corrected this to a *convergence* and directed the model to
"look up and read about Spekkens's causality papers" — the model searched,
verified, and retracted, the first documented case of an author correction
overturning a model's literature claim. At #7, the author made an architectural
decision with his reasoning stated: the Aethic-subtraction apparatus should be
dropped because he had since "settled on the idea of dropping negative values
from the Aethic tree altogether to maintain the ability for invalid Aethae to be
inequivalent/unique labels," proposing max(A,B) − min(A,B) or |A − B| to
preserve the disjointness seed-idea, and directing that the ring section be
softened "to instead construct the Aethic tree as a semiring from the get-go"
— the decision that fixed the corpus's algebraic signature, with the model then
executing the monus and semiring reform rounds. At #11 he retired his own earlier
vocabulary (the opaque/translucent concepts, explicitly dated as two-year-old
superseded formalization attempts) and commissioned the validity-equivalence
distinction. Model: the literature mapping; the
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
with his keys. A representative content exchange of this span (#59): the author
supplied his EPR resolution --- preferred-foliation based, locality as corollary
--- as a snippet from another paper of his own, directing near-verbatim
integration as a new subsubsection with the caution ``be extra careful about the
citations'': author content and author positioning, model installation and
citation verification. Provenance-detection and importance-tiering of the paper's own text —
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
anthropic framework are the author's pre-existing manuscripts --- at #179 he points
the model to its source directly: ``The accordance principle comes from my Nexic
reasoning document... if you want to familiarize yourself with it some more for
context'' --- the enhancement passes (theorem proofs, tier structure, differentia
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

**Author-originated, with export anchors and the key passages unpacked:** the
commission to integrate determinate nodes by name and to write out the Nexus
assembly integral (#1635). The V-versus-D "theft" question with the
counterpart-class framing (#1641) — whether toggling the leak *steals from* D or
switches *between counterpart classes*, a question the author posed and the
model's leak computations then answered (the marker-coupled distinguishability is
exactly invariant). The physical conception behind the region dial, in the
author's own words (#1643): a leak might "always be expressible as... creating a
kind of measurement error in the tags themselves, such that the polarizer
determinate nodes are not perfect pinpoints on the Bloch sphere, but rather
spread out regions of arbitrarily-short regional diameter... practically speaking
this is what I imagine the determinate nodes to look like" — with the
whole-sphere limit as the blank case and the joint-intersection third factor
alongside; the model formalized this as the two-dial mixture treatment with the
C→0 consistency check. The request to bring the long's proper/improper mixture
discussion up to date (#1645). The sequencing observation (#1651): the "any"
pre-shackled by joint-validity constraints, pre-analyzer to post-analyzer. The
method statement at #1653, which set the derivation's ground rules: the author
asked to see the standard definition of D "so I know what to riff off of,"
registered a reservation about the centroid's ontological standing while
accepting its equivalence, raised the triple-slit question (is D even standardly
defined there?), and proposed the subset-graded powerset lattice with the
mathematical-induction hypothesis for the n-slit case. And the directive that
named the whole approach (#1657): "we should, as usual, salvage the existing
mathematical structures but place the first principles where ideal" — the
centroid as establishing object — followed by the commission to work the route
in full (#1659).

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

### Arc VIII — Paper 8, the algebra face, and the symmetric error record (post-export; pass-ledger anchors 508–513)

**Scope note first**: this arc postdates the hashed export's window (which closes
2026-07-24T22:08 UTC), so its claims anchor to the pass ledger (passes 508–513), to
the paper's own in-file audit trail, and to the referee reports the author holds
verbatim; a refreshed export at the next deposit will extend the hash-attested
record over it.

**The commission and source**: the author commissioned Paper 8 as the canonical
``algebra face'' complementing the counterfactual extraction's modal face,
extracting the long manuscript's weighted-formulation section --- the author's
two-layer construction, dated May 16, 2026 in his own provenance footnote --- with
substance kept intact and vocabulary converted to the neutral idiom.

**The five review rounds, and why this arc is the corpus's most complete provenance
exhibit**: errors originated in *every* party of the loop, and each is logged.
(i) *Source-manuscript errors, faithfully extracted*: the piecewise
multiplication declaration (distributivity fails --- referee counterexample) and a
flawed uniqueness proof, both sitting in the long's author-with-ai-passages span;
byte-verified against the source before concession. (ii) *Drafting errors*: an
order-relation miswiring introduced in extraction, abstract overclaims, a third
recurrence of the fallback-bibliography bug, one garbled install self-caught
pre-delivery --- and a provenance mislabel in the *flattering* direction (a
review-proposed construction labeled ``drafting-original''), the mirror image of
the earlier false-provenance item, corrected with the admission in the header.
(iii) *Reviewer errors, twice, both ratified into the text by the next draft and
both then retracted by the reviewer*: a collapse two-liner that proved nothing
(its conclusion held between already-congruent states) and a structural-forcing
claim that silently dropped a non-negativity rider; the paper's header now carries
a reviewer-error log with the same visibility as drafting errors --- a convention
this arc established. (iv) *The author's repair, and its small wobble*: the
author's child/proper-child disambiguation --- in his words, a child is ``something
which you get by multiplying a new'' state in, while a proper child ``is
specifically a segment from the linear combination,'' weights strictly between
their totals and zero ``that way, intuitively it's like a segment for which we
can add back the remainder,'' with the containment fact (all proper children are
children) stated alongside --- killed a three-round vacuity
family at its actual root --- the strongest single repair in the paper's history,
so classified in the header as author-originated --- while its strict upper bound
was review-repaired for non-dense weight types, closed at the top and flagged for
the author's sign-off.

**The arc's closing tally (seven rounds, per the final reports)**: findings
originated in the source span (one), the drafting (several), the review (five,
counting the seventh round's review-adjacent tension between a review fix and
adjacent retained text; two verdict-relevant, the rest phrasing-level, each
ratified into a draft before retraction or repair), and the author's repair
(one, mild) --- the reviewer the most
frequent source in the last three rounds even as findings shrank from
verdict-flippers to phrasing, which the report itself calls the strongest
argument the log makes for the independent hour. **The mid-arc statement of the
same-family limit, quoted because it is the record's most precise**: across five rounds
``errors have originated in the source manuscript, the drafting, the reviewer
twice --- both times ratified into the text by the next draft --- and now, mildly,
in the author's own repair. Every party in the loop has generated at least one...
[independent review of the live definitions] is no longer merely advisable before
the next revision --- it's the only step that breaks the pattern the log now
documents.'' The live surface at close: the proper-child/proper-state/reduced-form
definitions, one weighted-layer paragraph, and the deletion convention --- an
afternoon for an independent algebraist, and the single highest-priority item for
outside human checking in the corpus.

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
- **Paper 8 (the weight algebra)**: the author's May-2026 two-layer construction,
  extracted and vocabulary-converted by the model; five review rounds with the
  complete four-party error record above; the paper's header carries its own
  per-artifact audit trail including the corpus's first reviewer-error log.
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

**Reviewer errors, logged with equal visibility** (the Paper-8 arc's addition to
the record): two review-proposed claims drafted into the text and refuted by the
subsequent review --- the collapse two-liner and the totalization claim --- plus a
review-proposed repair clause that jointly produced a definitional vacuity; the
convention that reviewer errors are logged beside drafting errors, in the
artifact's own header, dates from this arc and is itself part of the corpus's
provenance apparatus now.

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
  to the author's public repository with Wayback Machine snapshots; both exports
  likewise, their hashes binding this document's citations to fixed text
  (identity-export `#N` references are marked as such throughout).

*Record generated 24 July 2026 and updated the same date through the Paper-8 arc
(pass ledger through 513), within the collaboration it describes; the Paper-8 arc
postdates the hashed export's window and should be covered by a refreshed export
at the next deposit; subject throughout to the author's amendment and the
independent human review that no document in this corpus replaces --- with the
Paper-8 definitions named, by the review process itself, as where that review
should begin.*
