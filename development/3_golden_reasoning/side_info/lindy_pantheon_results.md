# Most Influential People and the Lindy Effect

**Model and results on Pantheon 2025** · November 25, 2026

Data: Pantheon (pantheon.world), 2025 version, read from the public API on November 25, 2026. The scripts, extracts and outputs are in the `lindy/` folder listed at the end. Appendix A gives the 2025 ranking to rank 1,067.

## Summary

- **Data.** The 2025 ranking to rank 1,067 with each person's previous-version values; the 174 people of the previous top 1,000 who are now below rank 1,067; and the HPI components (L, L*, PVne, CV, raw HPI) of the 2024 record for 1,053 people.
- **Model.** Each person's score S sits below a ceiling M, a peak object. The ceilings are held in disagreeing superposition, the parameter is θ = −d ln(M − S)/dt, and θ moves as Brownian motion whose volatility is itself held in superposition (the Golden form). The record prunes the superposition: the score never exceeded the ceiling, and the person has stayed above or below a score threshold for as long as they have.
- **What emerges from it.**
  1. The Aethic Lindy law: P(hold a further s | held t) = (t/(t+s))^k, hazard k/t, with k = 1 at the weight the mediocrity step selects.
  2. Memoryless headroom, P(M − S ≥ Δ) = e^(−βΔ): the peak is a child Aethus selected in proportion to its weight.
  3. Falls that outnumber and outsize rises at every detectable size, with no asymmetry put in.
  4. After a fall beyond the band, a partial reset of tenure and a return toward a baseline.
  5. "Nobody rises to the same peak twice" as an emergent regularity rather than a law: after a reset the chance of regaining an old peak is about rank(peak)/rank(now), 1 in 20 for a former #1 now at #20.
  6. Each database version as a draw from a small distribution around the latent score. For people dead more than about 30 years, the typical change from one version to the next is draw noise.
- **Age structure.** The top 1,000 has roughly equal numbers of people per doubling of age from 50 to 3,200 years. The fitted Lindy exponent is k ≈ 1.4 if entry was constant over history and k ≈ 0.55 if entry grew with world population; k = 1 lies between.
- **Transients.** 2 of the top 10 (Trump, Pope Francis), 9 of the top 100 and 131 of the top 1,000 are alive or died after 1995.
- **Tenure.** Typical attention changes are the same size at every tenure. Changes beyond ×2 are 8 times as common in the 30 years after death (15.6%) as among people dead over 1,000 years (1.9%).
- **Top end.** The top four lie within 0.26 raw points of each other, closer than an exponential tail allows (chance 1.4%), and the order of the top three is within draw noise.
- **Trump.** Rank 4 (previous 17) on a ×4.31 rise in relative non-English attention; without that rise his score would rank 20. His tenure at this level is 2–10 years, and the band noise the model gives him is 140–700 times Muhammad's.
- **Alexander.** Rank 16 in both versions. His own number held while 7 people rose past him and 7 fell below him. At 2,348 years of tenure, his median remaining tenure above his present level is 2,348 years at k = 1.
- **Drops of 10 places.** With each person as an index, the model sets the wait by the tenure above the score 10 places down. The mean wait is infinite; the median is T at k = 1 and 15T at k = 1/4. 43 of the top 50 are held by long tenures (Muhammad about 1,390 years at k = 1). Trump, Pope Francis, Jimmy Carter, Benedict XVI and John Paul II rose across their thresholds within one version: a median of 1 year at k = 1 and 15 years at k = 1/4 (section 5).
- **The exponent in superposition.** With k held blank under a lognormal generic weight with its mode at 1/4 and k = 1 at its 75th percentile (median 0.55), the median waits are about 64,000 years for Muhammad and 2.2 years for anyone who has just risen across the line, such as Trump. The filtering removes the exponents above 1 from those who hold and leaves them to the just-arrived (2.11). The percentiles of the wait for the top 50 are in section 5.
- **Higher before?** For people who died within the last century the model expects a peak, a fall over 20–30 years and no return, and the version-step data agree: slightly negative change for people dead 2–30 years, flat for 30–100. For the long dead it expects no large recent fall; their rank losses between the two versions come from the formula and from others' rises (section 6).
- **2075.** With no new entrants, the median ranking fifty years on keeps the long-held at the top (Muhammad, Newton, the Buddha) and returns this year's risers toward where they stood before: Trump 13, Pope Francis 77. Pantheon's own age terms move the twentieth-century figures up by several places. The ranking is the verdict of the general Aethus; adjusted by what is known of particular people, as a matter of judgment, Trump moves to 23 (section 7).
- **Not testable yet.** Two versions with a formula change between them cannot test the gap dynamics; Pantheon's multi-year snapshots can (section 8).

## 1. Data

### 1.1 What was read

From `api.pantheon.world`:

- `person_ranks`, 2025 version: ranks 1–1,067 with HPI, previous rank and HPI, L (number of Wikipedia language editions), PVne (non-English page views), CV (coefficient of variation of the page views), birth and death years, occupation, birth country and gender. The L* field of this table is empty.
- The 174 people who were in the previous version's top 1,000 and are now below rank 1,067, with their 2025 ranks.
- `person_hpi` components (raw HPI, L, L*, PVne, CV): the 2024 record for 1,053 people, covering 998 of the previous top 1,000; the 2025 record for 30 people; the 2023 record for 29.

The 2025 HPI is 100 × raw/35.680, with Muhammad at 100. Score differences in this file are in raw 2025 points; one raw point is 2.80 HPI points.

### 1.2 Caveats

- **The formula.** Pantheon's published form, HPI = ln L + ln L* + log₄A + ln PVne − ln CV, less (70 − A)/7 when the age A is under 70 [Pantheon methods; Yu et al. 2016], does not reproduce the 2025 raw values. On the 30 people checked, raw minus formula runs from 5.21 to 9.33 (median 7.42), so the 2025 computation contains a term the API does not display. Statements about components below use the displayed components and report the remainder.
- **The step between versions.** Between the previous version and 2025, L* entered the formula and CV was redefined, so changes in raw HPI and rank from one version to the next mix an instrument change with real change. Of the previous top 1,000, 777 fell in rank and 216 rose. The 207 people who entered the top 1,000 have a median CV of 2.53 against 3.79 for the cohort they joined; 131 of them died before 1900 and 40 are popes.
- **The page-view window.** The median Δ ln PVne over the cohort is −0.153 (80.2% fell), a difference of window and coverage. Attention changes below are relative: δ = Δ ln PVne minus that median.

## 2. The model

### 2.1 Specification

The note of November 25 and its refinements the same day. Choices of formalization made here are marked (F) and listed in 2.9.

1. **Score.** S(t), a person's attention score. Each database version is one draw from a small distribution around it (2.8).
2. **Ceilings.** M, the highest score the person's attributes could carry: a peak object. The person's generic distribution over ceilings is held in disagreeing superposition. (F) Its tail is exponential with rate β, estimated from the cross-section as ln rank ≈ c − β·raw; at the very top a non-parametric form replaces it (2.3). (F) Ceilings are functions of time, so the record constrains a ceiling at the times it records and not afterwards.
3. **Parameter.** The gap G = M − S and θ = −d ln G/dt. In the Golden form θ performs Brownian motion, and its volatility σ is itself held in disagreeing superposition, (F) with weight proportional to σ^(a−1). Each volatility pocket is constant in time, as each hazard pocket is in the long paper's law. The volatility's time variation lies in the filtering: holding concentrates the weight on small σ, and a reset reopens it to larger values (2.5).
4. **Pruning.** Hypotheses that conflict with the record are invalidated: the score never exceeded the ceiling, and the person has stayed above or below a score threshold for their tenure t. (F) Staying is modelled as ln G remaining inside a band |Δ ln G| < w around its level.

### 2.2 The Aethic Lindy law emerges

Pruning the volatility superposition by survival in the band for a tenure t gives

> P(hold a further s | held t) = (t/(t+s))^k, with k = 3a/2 and hazard k/t,

and at a = 2/3 the survivors' slope noise obeys t·E|θ| ≈ 1.12 w. The 3/2 is the scaling of the Golden form: a band of half-width w is crossed on the time scale (w/σ)^(2/3), and substituting u = tσ^(2/3) in the mixture gives the law exactly for the untruncated superposition. At a = 2/3, k = 1, and the result is the long paper's Aethic Lindy law with the exponent its mediocrity step selects (Proposition "The Aethic Lindy law", in "A Further Note on the Lindy Effect"). With a one-sided threshold, staying above with no upper limit, a single σ already gives a polynomial tail, t^(−1/4): the persistence exponent of integrated Brownian motion and the critical-case tail of the Golden paper.

Simulation: integrated Brownian motion in the band, 200,000 paths, time step 0.002, seed 1042; the mixture over σ on a grid from 10⁻⁹ to 10³.

| a | k = 3a/2 | tenure t | P(hold to 2t), simulated | law, 2^(−k) | t × hazard | t × slope noise (in w) |
|---|---:|---:|---:|---:|---:|---:|
| 2/3 | 1 | 10 | 0.5000 | 0.5000 | 1.000 | 1.121 |
| 2/3 | 1 | 100 | 0.5000 | 0.5000 | 1.000 | 1.121 |
| 2/3 | 1 | 1,000 | 0.4998 | 0.5000 | 1.000 | 1.122 |
| 2/3 | 1 | 10,000 | 0.4978 | 0.5000 | 1.004 | 1.126 |
| 1/6 | 0.25 | 10 | 0.8331 | 0.8409 | 0.262 | 0.367 |
| 1/6 | 0.25 | 100 | 0.8264 | 0.8409 | 0.273 | 0.381 |
| 1/6 | 0.25 | 1,000 | 0.8132 | 0.8409 | 0.294 | 0.410 |
| 1/6 | 0.25 | 10,000 | 0.7838 | 0.8409 | 0.340 | 0.474 |

At a = 1/6 the values drift away from the law at long tenure because the grid's smallest σ sets a longest survival time. The untruncated mixture follows the law exactly.

### 2.3 The peak as a child Aethus: memoryless headroom

With an exponential tail, P(M − S ≥ Δ | M ≥ S) = e^(−βΔ) at every S. The child Aethus "the ceiling is at least Δ above the present score" carries this weight relative to its parent. It is the ratio f(S + Δ)/f(S) of the generic density, the Metropolis acceptance min(1, f(s′)/f(s)) of an upward move, and it is the selection in proportion to the child Aethus's weight.

- **Estimates.** β = 0.78 over ranks 1–1,067, 1.06 over ranks 1–100 and 0.70 over ranks 100–1,067. The mean headroom 1/β is 1.28 raw points (0.94 in the top 100).
- **Non-parametric form.** If the generic distribution is read off the cross-section, P(M ≥ s′ | M ≥ s) = N(≥ s′)/N(≥ s) = rank(s′)/rank(s). Where the tail is exponential the two forms agree: the local β is 1.07 over ranks 4–16, 1.02 over 16–50, 0.91 over 50–100 and 0.73 over 100–1,000.
- **The very top.** There the forms part. The top four (Muhammad 35.680, the Buddha 35.495, Newton 35.480, Trump 35.419) span 0.262 raw points, a local β of 5.3. Under an exponential tail with β = 1.06, the chance that the top four would lie this close is 1.4%. The tail flattens near raw 35.7, a soft maximum, and the rank-ratio form is the one to use there.

### 2.4 Falls outnumber and outsize rises

A move of x in ln G changes the score by ΔS = G(1 − e^x). A move of −x raises S by G(1 − e^(−x)), which is less than G and shrinks as the ceiling nears. A move of +x lowers S by G(e^x − 1), which has no bound and grows faster than x. Symmetric moves in ln G therefore give falls that outnumber rises at every detectable size. Simulation, with headroom drawn from the pruned exponential (β = 0.78, mean 1.28) and symmetric normal moves in ln G, 400,000 draws:

| sd of the move in ln G | share of moves that are rises | rise > 0.5 | fall > 0.5 | rise > 1 | fall > 1 | rise > 2 | fall > 2 | mean rise | mean fall |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.3 | 49.9% | 7.5% | 11.3% | 2.1% | 4.7% | 0.3% | 1.2% | 0.26 | 0.37 |
| 1 | 49.9% | 19.6% | 29.0% | 9.8% | 21.3% | 2.9% | 13.7% | 0.61 | 2.26 |
| 2 | 50.0% | 25.4% | 37.5% | 14.6% | 32.1% | 5.4% | 25.9% | 0.85 | 17.08 |

### 2.5 After the peak: a partial reset of tenure and a return to baseline

A person's Lindy advantage at a high score is the generic distribution conditioned on having stayed at that score that long. A fall beyond the band is a record that conflicts with the "stay" child, the hypotheses in which the person holds the old level. Those are invalidated, the tenure at that level restarts, and what remains is the generic distribution conditioned on the person's durable attributes and the new score: the baseline. The score heads toward it because the slope persists; θ is Brownian, not white noise.

The reset is partial, in two ways (F):

- **Graded by the push.** Tenure and slope noise are tied by t·E|θ| ≈ 1.12 w, so a push with slope |θ| leaves an effective tenure t_eff ≈ min(t, 1.12 w/|θ|). A small push changes nothing; a hard one sets the clock near zero.
- **Per threshold.** Each threshold keeps its own clock. A fall resets the clocks of the thresholds it crosses and leaves the clocks of the lower thresholds running.

**The volatility reopens, for the future only.** Nothing in the past is reopened. Under centric unfolding the record is stamped segment by segment, like a tape: each stretch between resets keeps the superposition as it was filtered while that stretch lasted. What a reset changes is the reference for the future. Let N be the generic superposition, A the Aethus of a generic member who has just arrived at the person's present level with the person's present threshold statistics, and B the rest of the person's stamped record. The reset licenses the transfer

> w(F | B∘A∘N) = w(F | A∘N) for every further-time attribute F,

so the person proceeds exactly as if they were that generic member, without being one. The transfer is exact when the pockets that bear on the future are renewed at the reset, one set of pockets per segment of the tape. If a person's pockets were constant over the whole record, the long hold would be evidence about a volatility that persists, and the transfer would fail. Under renewal, the effective slope noise returns from 1.12 w/t to about 1.12 w per version, a factor of t/τ: about 200 for Napoleon (2.10, item 13). The result is calm stretches that grow calmer, broken by turbulent ones after a push, the same shape as the volatility clustering of market prices.

This is the Aethic form of memorylessness, and it is not tied to time: B∘A∘N may refer to A∘N for F whenever B carries no weight on F relative to A∘N. Each constant-hazard pocket has the property with A the Aethus of an item just begun, which is the exponential distribution's memorylessness. Within a segment the superposition lacks it, and that lack is the Lindy effect: survival skews the pockets, so the past keeps weight on the future. A reset is where the transfer holds again, at what probability theory calls a regeneration point.

The reset is what keeps a reversal from forcing a return to the old peak. If the ceiling were fixed and the old peak kept as a floor under it (M at least the highest score ever recorded), a reversal of θ would carry the score back toward the old peak. With the reset, the ceiling is redrawn relative to the present score, so a reversal heads toward S_now + 1/β on average. If a weight π stays on the old ceiling,

> P(the ceiling still reaches the old peak) = π + (1 − π)·rank(peak)/rank(now).

Long tenure keeps the reset from starting. The survivors' slope noise is E|θ| ≈ 1.12 w/t:

|  | tenure t | slope noise, band half-widths per year | hazard of leaving the band, k = 1 |
|---|---:|---:|---:|
| Muhammad, since death | 1,393 years | 8.05 × 10⁻⁴ | 1/1,393 per year |
| Trump, tenure 2 years | 2 years | 0.561 | 1/2 per year |
| Trump, tenure 10 years | 10 years | 0.112 | 1/10 per year |

The slope noise the model gives Trump is 140–700 times Muhammad's.

### 2.6 No second peak, as an emergent regularity

After a reset, the chance that the redrawn ceiling reaches the old peak is about rank(peak)/rank(now): 1/16 for a former #1 now at #16, 1/20 for one at #20, 1/25 for a former #4 now at #100. Reaching the ceiling also needs the gap to close, and rises slow as it closes, so the chance of getting near the old peak is lower still.

- At 1/20 per draw it takes 14 draws for an even chance, and 45 for a 90% chance, that at least one person at that score has a ceiling at the old #1 level.
- Summed over everyone below, the expected number of people whose redrawn ceilings reach the #1 score is the harmonic sum of 1/rank: 2.60 from ranks 2–20, 1.59 from ranks 21–100 and 2.36 from ranks 101–1,067. Each doubling of the pool adds about ln 2 ≈ 0.69, so the wider population supplies most of the candidates; a former #1 now at #20 is 0.76% of the candidates within the top 1,067 alone. The sum counts only people whose ceilings are open. Long tenure pins a ceiling near its score, so the candidates are mostly the living, the recently arrived and the recently reset.
- Nothing in the model forbids a second peak. After the reset the old peak has no standing, and the odds of reaching it are the odds of anyone at the same score. The regularity follows from memoryless headroom and the reset rule together; under a fixed ceiling with the old peak as a floor, a second rise would be the expected outcome of a reversal.

### 2.7 Durable and perishable parts

Event spikes are perishable. Attention to cultural products decays biexponentially, from communicative to cultural memory, and biographies stay in communicative memory the longest, about 20–30 years [Candia et al. 2019]. In the model the ceiling is M(t) = D + P(t), with P a perishable part that decays on that time scale. For the living and the recently dead, part of the present score is P.

### 2.8 Each database version is a draw

Relative to a given Aethus at a given time, a person's score is a small distribution rather than a point, and each database version is one draw from it. A change from one version to the next is then the latent change plus the difference of two draws.

**The size of a draw.** For people dead over 1,000 years the latent score barely moves (slope noise of order 10⁻³ band half-widths per year), so their changes estimate the draw noise. The robust standard deviation of δ among them is 0.172, so one draw has a standard deviation of about 0.122 in ln PVne: ±12% in non-English page views, or 0.12 raw points from this component alone.

**Typical moves are flat in tenure; large moves are not.**

| group | n | median size of δ | robust sd of δ | beyond ×1.5 | beyond ×2 | share of the typical move's variance from draws |
|---|---:|---:|---:|---:|---:|---:|
| alive | 64 | 0.220 | 0.349 | 25.0% | 10.9% | 0.24 |
| 0–30 years since death | 77 | 0.152 | 0.222 | 24.7% | 15.6% | 0.60 |
| 30–100 | 204 | 0.117 | 0.176 | 11.3% | 4.9% | 0.96 |
| 100–300 | 229 | 0.105 | 0.151 | 8.7% | 6.1% | 1.00 |
| 300–1,000 | 206 | 0.110 | 0.154 | 11.2% | 5.3% | 1.00 |
| 1,000–4,000 | 211 | 0.136 | 0.172 | 7.6% | 1.9% | 1.00 |

For people dead more than about 30 years, the typical change from one update to the next is draw noise. The large moves are not: Gaussian draws of this size would put 0.006% of changes beyond ×2, against 1.9% among people dead over 1,000 years and 15.6% in the 30 years after death.

**Rank jitter from draws alone.** 4,000 pairs of draws around the 2025 scores, against the moves observed in this version step:

| 2025 rank | draws alone: median rank move | observed in this step: median rank move | ratio |
|---|---:|---:|---:|
| 1–5 | 0.8 | 2 | 2.4 |
| 6–20 | 1.6 | 7 | 4.3 |
| 21–50 | 3.8 | 10.5 | 2.8 |
| 51–100 | 7.6 | 15 | 2.0 |
| 101–250 | 15.6 | 60 | 3.8 |
| 251–500 | 28.7 | 98.5 | 3.4 |

The observed moves are two to four times the draw jitter; the formula change and real movement make up the rest.

**The top three are within draw noise.** The same person comes out #1 in two independent draws 59% of the time, Muhammad is #1 in 76% of draws, and the top three come out in the same order in 10% of pairs.

**What it does to the pruning** (F). The record conditions apply to the latent score through the likelihood of the draws, not to the raw database values. Applied to the raw values, the highest draw would set a spurious peak and a floor under the ceiling; applied through the likelihood, update noise leaves the no-second-peak regularity intact. The band must also be wider than a draw: at G ≈ 1.28 raw points a draw of 0.12 is about 0.1 in ln G, so w of 0.3 or more.

### 2.9 Formalization choices, for the author's verdict

1. The threshold condition as a band |Δ ln G| < w.
2. The weight σ^(a−1) over volatilities, with a = 2/3 for k = 1. (Settled November 25: each pocket is constant in time, and the volatility's time variation is the reset reopening the filtering, 2.5.)
3. An exponential tail for the ceilings, replaced by the rank ratio at the very top.
4. Ceilings as functions of time, constrained by the record only at the times recorded.
5. The two forms of partial reset (graded by the push; per threshold) and the redraw with weight π left on the old ceiling.
6. Gaussian draws with the size estimated from the long dead, and the record conditions applied through the draws' likelihood.
7. What A contains at a reset (2.5). If A carries the clocks of thresholds the fall did not cross, those clocks keep their tenure, and Napoleon keeps 204 years for the line 10 places below him. If they belong to B, the transfer screens them off, and Napoleon is at one version, as section 5 has it.

### 2.10 The model in equations

Each person i is an index; nothing enters but the record.

1. **Score and gap.** S_i(t) = M_i − G_i(t).
2. **Golden form.** d ln G_i = −θ_i dt and dθ_i = σ_i dW_i.
3. **Generic distribution**, held in disagreeing superposition as the product of two families of pockets: ceilings, with P(M_i − S_i ≥ Δ | M_i ≥ S_i) = e^(−βΔ), and volatilities, with weight σ^(a−1) dσ. The volatility acts on the gap to the ceiling, so its pockets are contingent on the ceiling's.
4. **Each volatility pocket is a constant-hazard pocket.** Inside a band of half-width w, the pocket σ leaves at the constant rate λ(σ) = 0.731 (σ/w)^(2/3) once it has settled. The weight σ^(a−1) dσ is therefore λ^(k−1) dλ with k = 3a/2, the weight of the long paper's Proposition. The volatility's time variation is not put into the pockets: it is the filtering, which a reset reopens (2.5). Pockets that were themselves functions of time with no timescale, σ₀·t^γ, would keep the law's form with k = a(γ + 3/2).
5. **Validity selection** (the Nexus product with the survival Aethus). Holding for t multiplies each pocket by e^(−λt), which gives the weight t^k λ^(k−1) e^(−λt)/Γ(k).
6. **Aethic Lindy law.** P(hold a further s | held t) = (t/(t+s))^k. The expected hazard is k/t, the median further time is (2^(1/k) − 1)t, and the mean further time is t/(k − 1) for k > 1 and infinite for k ≤ 1.
7. **Survivors' slope noise** (a = 2/3). t·E|θ| ≈ 1.12 w.
8. **One-sided threshold.** P(stay above a further s | above for t) → (t/(t+s))^(1/4), with median 15t. Here the exponent comes from the evolution and not from the superposition.
9. **Score move** from a move x in ln G. ΔS = G(1 − e^x): a rise is at most G, a fall is G(e^x − 1).
10. **Headroom and regaining a peak.** P(M ≥ s′ | M ≥ s) = e^(−β(s′−s)) ≈ rank(s′)/rank(s).
11. **Observation.** X_i(v) = S_i(t_v) + ε with ε ~ N(0, σ_d²) and σ_d ≈ 0.122. A change between versions from draws alone has standard deviation √2·σ_d ≈ 0.172.
12. **Real move or draw.** P_real = p·f(δ)/[p·f(δ) + (1 − p)·φ(δ)], with p = 1/T, f(δ) = e^(−|δ|/μ)/(2μ), μ = 1/β, and φ the normal density of item 11.
13. **A drop of 10 places**, with threshold u the score 10 places down. P(no drop within s) = P_act·(τ/(τ+s))^k + (1 − P_act)·(T/(T+s))^k.

14. **A reset as a transfer** (2.5). w(F | B∘A∘N) = w(F | A∘N) for every further-time attribute F, where N is the generic superposition, A the arrival at the present level with the present threshold statistics, and B the stamped record. It is exact when the pockets that bear on the future are renewed per segment.

Items 1–3 are the specification, 4–10 follow from it, and 11–14 add the observation layer, the reading of the record and the reset as a transfer (F: the size density f and the one-version tenure τ after a real move).

### 2.11 The exponent in superposition

The exponent k can itself be left blank and so held in disagreeing superposition, with weight π(k). Each k-pocket is a Lindy law counted from the record's resolution τ (one version), and the record filters these pockets as it filters the volatilities:

> π_t(k) ∝ π(k)·(τ/t)^k and P(hold a further s | held t) = L(ln((t+s)/τ)) / L(ln(t/τ)), where L(x) = E_π[e^(−kx)].

The hazard is k̄(t)/t, where k̄(t) is the filtered mean of k. Surviving long is evidence for a small exponent, so k̄ falls with tenure, and the median wait is no longer a fixed multiple of the tenure: it grows faster than the tenure does. A reset refers the future to the generic weight again (2.5). That is why the medians of Saint Peter and Napoleon sit near the centre of the weight while Muhammad's sits at the low end.

**The generic weight** (the author's, November 25). A lognormal on (0, ∞), ln k ~ N(μ, s²), with its mode, e^(μ − s²), at 1/4 and k = 1 at its 75th percentile. The two conditions fix s = 0.888 and μ = −0.599. The median is 0.55 and the mean 0.81; 25% of the weight lies above 1 and 18.7% below 1/4; P(k > 2) = 7.3%, P(k > 10) = 0.05%, P(k < 0.1) = 2.7% and P(k < 0.01) = 3.2 × 10⁻⁶. A first version had μ = 0, with the median at the mediocrity value 1, half the weight above it, and s = √(ln 4) = 1.18; narrowing it to put 1 at the 75th percentile shrinks the part above 1.

**Exponents above 1.** The band form gives k = 3a/2, which exceeds 1 whenever the volatility weight has a > 2/3, and the long paper's Proposition admits any k > 0; it is the mediocrity step that selects 1. Only the one-sided form caps k, at 1/4. So the weight allows k > 1, and the filtering removes those pockets from anyone who holds: survival for t multiplies each pocket by (τ/t)^k, and the share of k > 1 falls from 25% at a tenure of one year to 2.9% at 10 years, 0.37% at 100 and 0.05% at 1,000. They matter only for people who have just arrived at their level, whose median wait is 2.2 years.

**Under filtering** the filtered mean of k is 0.81 at a tenure of one year, 0.36 at 10 years, 0.26 at 100, 0.21 at 1,000, 0.19 at 3,000 and 0.14 at 10⁶.

**The left tail sets how durable the long-held become.** Filtering amplifies whatever weight lies at small k. A lognormal vanishes at 0 faster than any power, so over very long spans survival decays faster than any power of 1/ln t. With s = 0.89, 2.7% of the weight still lies below 0.1, and Muhammad's median wait is about 64,000 years; under the wider first version (μ = 0) it was about 104,000.

**The earlier forms.** Before the lognormal the author tried a smooth family, exp(−((m+1)/2)·√(a² + u²) + ((m−1)/2)·u) with u = ln 4k. As a → 0 it tends to min((4k)^m, 1/(4k)), log-uniform from 1/4 to 1 with a root of multiplicity m at 0, and at a = 4/3 it already looks lognormal. The root's multiplicity sets the long-span decay, (ln t)^(−(m+1)): Muhammad's median wait is about 85,000 years at m = 1 and 31,000 at m = 2 (a = 1/3), against about 2 million under a uniform weight on (0, 1].

**The age data.** The age structure of 3.1 is the only evidence on k, and its verdict turns on how entry grew. The weights below are applied from age 50, the youngest age in the top 1,000, except in the column marked otherwise.

- **Entry proportional to world population.** The best single exponent is 0.56, and weights confined to [1/4, 1] fit about as well (uniform −0.1, log-uniform −3.9 in log-likelihood). The adopted lognormal fits at −14.0, close to the piecewise quadratic (−13.4) and a little below the first, μ = 0 version (−10.4) and the smooth double root (−11.8). The best-fitting lognormal has s = 1.18 and a median near 3 (mode 0.76), and fits slightly better than any single exponent (+1.6).
- **Entry growing as population^1.5.** The best single exponent drops to 0.15. The adopted lognormal fits at −10.8, better than the μ = 0 version (−13.9) and the smooth double root (−12.9); the best-fitting lognormal is much wider (median 0.78, s = 2.5, the edge of the grid searched) and fits at +0.7.
- **Constant entry.** Every weight centred at or below 1 fails, because the best single exponent is then 1.38; the adopted lognormal is at −364.9.

Differences in log-likelihood from the best single exponent:

| weight over k | population entry | population entry, from age 1 | entry as population^1.5 | constant entry |
|---|---:|---:|---:|---:|
| **adopted: lognormal, mode 1/4, k = 1 at the 75th percentile** | −14.0 | −37.8 | −10.8 | −364.9 |
| lognormal, μ = 0, mode 1/4 (first version) | −10.4 | −40.9 | −13.9 | −351.3 |
| lognormal, mode 1/4, median 1/2 | −14.9 | −37.2 | −10.1 | −368.4 |
| smooth, m = 2, a = 1/3 | −11.8 | −29.8 | −12.9 | −350.7 |
| smooth, m = 1, a = 1/3 | −18.7 | −40.1 | −7.5 | −383.2 |
| piecewise quadratic (64k² below 1/4) | −13.4 | −29.8 | −11.5 | −357.9 |
| uniform [1/4, 1] (median 5/8) | −0.1 | −8.1 | −37.4 | −258.6 |
| log-uniform [1/4, 1] (median 1/2) | −3.9 | −12.3 | −24.7 | −298.4 |
| two points 1/4 and 1, equal weight | −13.6 | −29.6 | −11.1 | −362.7 |
| log-uniform [1/16, 1] (median 1/4) | −37.6 | −55.0 | −0.8 | −451.8 |
| uniform (0, 1] | −20.4 | −53.8 | −6.2 | −394.2 |
| fixed k = 1/4 | −30.9 | −30.9 | −2.9 | −423.3 |
| fixed k = 1/2 | −1.1 | −1.1 | −35.5 | −260.0 |
| fixed k = 1 | −55.8 | −55.8 | −191.5 | −48.2 |

**The top 20 under the adopted weight**, with filtering from one version and the regimes of section 5:

| rank | name | regime | filtered mean k | median wait, adopted lognormal (years) | first lognormal, μ = 0 | smooth m = 2 | fixed k = 1 | fixed k = 1/4 | P(drop within 100 y), adopted |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Muhammad | held | 0.205 | 63,702 | 103,612 | 31,003 | 1,391 | 20,836 | 1.5% |
| 2 | The Buddha | held | 0.196 | 133,802 | 230,494 | 62,623 | 2,476 | 37,141 | 0.8% |
| 3 | Isaac Newton | held | 0.233 | 8,682 | 12,082 | 4,726 | 299 | 4,476 | 6.5% |
| 4 | Donald Trump | risen across the threshold | 0.815 | 2.2 | 0.9 | 3.7 | 1.0 | 15 | 84.4% |
| 5 | Genghis Khan | held | 0.214 | 31,173 | 47,990 | 15,764 | 798 | 11,962 | 2.5% |
| 6 | Cleopatra | held | 0.199 | 103,086 | 173,625 | 49,038 | 2,040 | 30,414 | 1.2% |
| 7 | Mahatma Gandhi | held | 0.268 | 1,366 | 1,626 | 842 | 75 | 1,111 | 20.1% |
| 8 | Pope Francis | risen across the threshold | 0.815 | 2.2 | 0.9 | 3.7 | 1.0 | 15 | 84.4% |
| 9 | Mary, mother of Jesus | held | 0.199 | 101,229 | 170,699 | 48,060 | 1,992 | 29,869 | 1.0% |
| 10 | Ludwig van Beethoven | held | 0.243 | 5,071 | 6,760 | 2,851 | 198 | 2,970 | 9.3% |
| 11 | Leonardo da Vinci | held | 0.222 | 17,263 | 25,373 | 9,026 | 506 | 7,582 | 3.9% |
| 12 | Aristotle | held | 0.197 | 124,817 | 213,876 | 58,625 | 2,346 | 35,177 | 0.8% |
| 13 | Marco Polo | held | 0.216 | 26,347 | 40,028 | 13,449 | 701 | 10,504 | 2.9% |
| 14 | Elizabeth I | held | 0.226 | 13,654 | 19,703 | 7,235 | 422 | 6,330 | 4.7% |
| 15 | Plato | held | 0.197 | 126,589 | 217,148 | 59,414 | 2,372 | 35,567 | 0.8% |
| 16 | Alexander the Great | held | 0.197 | 124,953 | 214,127 | 58,685 | 2,348 | 35,207 | 0.8% |
| 17 | Saint Peter | risen across the threshold | 0.815 | 8.0 | 2.6 | 13 | 2.0 | 82 | 63.0% |
| 18 | Homer | held | 0.194 | 154,715 | 269,493 | 71,882 | 2,774 | 41,610 | 0.7% |
| 19 | Wolfgang Amadeus Mozart | held | 0.239 | 6,316 | 8,570 | 3,504 | 234 | 3,510 | 8.0% |
| 20 | Napoleon | falling (graded reset) | 0.815 | 30 | 9.5 | 40 | 3.8 | 163 | 55.9% |

## 3. What the 2025 data show

### 3.1 Age structure and the Lindy exponent

People per doubling of age, A = 2025 − birth year. No one in the top 1,000 is under 50.

| age (years) | top 50 | top 100 | top 250 | top 1,000 |
|---|---:|---:|---:|---:|
| 50–100 | 5 | 7 | 26 | 126 |
| 100–200 | 8 | 21 | 58 | 276 |
| 200–400 | 9 | 22 | 56 | 164 |
| 400–800 | 11 | 23 | 42 | 177 |
| 800–1,600 | 2 | 6 | 17 | 75 |
| 1,600–3,200 | 14 | 20 | 45 | 163 |
| 3,200–6,400 | 1 | 1 | 6 | 19 |

Under the Aethic Lindy law the count per doubling of age goes as entry × A^(1−k), so flat counts with constant entry mean k = 1. Fits over ages 150–4,800 years, which leaves out the perishable phase, with 2-unit likelihood intervals:

| entry over history | top 100 | top 1,000 |
|---|---:|---:|
| constant | k = 1.34 [1.11, 1.58] | k = 1.38 [1.31, 1.46] |
| proportional to world population (HYDE) | k = 0.52 [0.29, 0.76] | k = 0.56 [0.49, 0.64] |

k = 1 lies between the two entry assumptions. The age structure brackets the exponent; it does not identify it.

Per century, the top 1,000 has 10.19 people born 1175 BC–425 CE, 9.25 born 425–1225 and 44.5 born 1225–1625. The medieval dip in the doubling table is mostly the binning, since per century it is 9.3 against 10.2; the change is the step after 1225, a factor of 4.8. The 74 born 425–1225 are mostly politicians (31) and religious figures (15); by birth country, Saudi Arabia 10, Italy 8, United Kingdom 6, Iran 5, France 5 and Iraq 4.

### 3.2 Transients

|  | top 10 | top 50 | top 100 | top 250 | top 1,000 |
|---|---:|---:|---:|---:|---:|
| alive | 1 | 1 | 2 | 10 | 56 |
| alive or died since 1995 | 2 | 6 | 9 | 25 | 131 |

Alive or died since 1995, in the top 100: Trump 4 (previous 17), Pope Francis 8 (67), Jimmy Carter 29 (59), Benedict XVI 30 (499), Mother Teresa 44 (436), John Paul II 49 (153), Charles III 63 (870), Muhammad Ali 87 (56), Nelson Mandela 96 (68).

With a residence in communicative memory of about 20–30 years, these counts imply roughly one new transient every 12 years in the top 10, every 4 years in the top 50 and every 3 years in the top 100.

### 3.3 The age bonus and an age-free ranking

The log₄A term adds 2.88–6.20 raw points across the top 1,000. Without it (the age-free list is complete to rank 250):

| age-free rank | name | 2025 rank | raw | age bonus log₄A | age-free score |
|---:|---|---:|---:|---:|---:|
| 1 | Donald Trump | 4 | 35.42 | 3.15 | 32.27 |
| 2 | Pope Francis | 8 | 34.63 | 3.24 | 31.39 |
| 3 | Mahatma Gandhi | 7 | 34.86 | 3.64 | 31.22 |
| 4 | Isaac Newton | 3 | 35.48 | 4.29 | 31.19 |
| 5 | Ludwig van Beethoven | 10 | 34.57 | 4.00 | 30.57 |
| 6 | Muhammad | 1 | 35.68 | 5.25 | 30.43 |
| 7 | Adolf Hitler | 22 | 33.89 | 3.54 | 30.35 |
| 8 | Genghis Khan | 5 | 35.12 | 4.88 | 30.24 |
| 9 | Albert Einstein | 25 | 33.83 | 3.59 | 30.24 |
| 10 | Pope Benedict XVI | 30 | 33.50 | 3.31 | 30.20 |
| 11 | Jimmy Carter | 29 | 33.50 | 3.33 | 30.18 |
| 12 | Napoleon | 20 | 34.00 | 4.00 | 30.00 |
| 13 | Marie Curie | 27 | 33.65 | 3.65 | 30.00 |
| 14 | Wolfgang Amadeus Mozart | 19 | 34.03 | 4.04 | 29.99 |
| 15 | Leonardo da Vinci | 11 | 34.54 | 4.58 | 29.96 |
| 16 | Che Guevara | 41 | 33.21 | 3.30 | 29.91 |
| 17 | The Buddha | 2 | 35.50 | 5.67 | 29.83 |
| 18 | Elizabeth I | 14 | 34.27 | 4.47 | 29.80 |
| 19 | Mother Teresa | 44 | 33.18 | 3.42 | 29.75 |
| 20 | Martin Luther King Jr. | 50 | 33.00 | 3.29 | 29.71 |

### 3.4 One version step

- **Cohort** (the previous top 1,000): 777 fell in rank, 216 rose and 7 kept their rank; 174 are now below 1,067. The 207 entrants into the top 1,000 had a median previous rank of 1,764; 71 are politicians and 52 religious figures.
- **Relative attention** (n = 998): the standard deviation of δ is 0.366 and its skew +1.82. Rises are the large moves: beyond ×1.5, 74 up and 44 down; beyond ×2, 41 and 17; beyond ×4, 14 and 2. Raw HPI fell for 534 and rose for 464.
- **Largest relative rises:** Pope Leo XIII ×17.9, Pope Francis ×10.4, John Paul I ×9.3, Benedict XVI ×8.0, Paul VI ×6.6, Benedict XV ×6.5, Pius XI ×6.4, John Paul II ×6.1, John XXIII ×5.9, Caracalla ×5.5. All 11 popes born after 1800 rose, by ×4.4 to ×17.9, in the year of the 2025 conclave; Pope Leo XIV entered at rank 127 from 118,563.
- **Largest relative falls:** Toto Cutugno ×0.17, Franz Beckenbauer ×0.23, Henry Kissinger ×0.26, Margrethe II ×0.27, Mahmoud Abbas ×0.27, Yasser Arafat ×0.29, Golda Meir ×0.30, Joséphine de Beauharnais ×0.30, Yitzhak Rabin ×0.34, Princess Margaret ×0.35, mostly the decay of spikes in the previous window.
- **What this step cannot test.** The durable asymmetry of 2.4 concerns the latent gap. In this step, ranks are dominated by the formula change and attention by spikes and their decay. A spike is a rise within one window, which is why δ is skewed upward.

### 3.5 Large moves and tenure

P(|δ| > ln 2) falls with years since death as D^(−0.34), shallower than the 1/t of the band hazard; per person, log|δ| regressed on log A has slope −0.045, close to flat. With the draw layer of 2.8 the two fit together: the typical move is the draw and does not depend on tenure, and the tail is latent movement, which does.

### 3.6 Exits by age

Share of the previous top 250 and top 1,000 now outside it, by age:

| age (years) | previous top 250: n | now outside the top 250 | previous top 1,000: n | now outside the top 1,000 |
|---|---:|---:|---:|---:|
| 50–100 | 29 | 41.4% | 136 | 26.5% |
| 100–200 | 52 | 32.7% | 284 | 21.5% |
| 200–400 | 59 | 22.0% | 172 | 23.3% |
| 400–800 | 37 | 13.5% | 157 | 15.9% |
| 800–1,600 | 14 | 35.7% | 73 | 23.3% |
| 1,600–6,400 | 59 | 25.4% | 177 | 15.3% |

### 3.7 Durability of the current top 20

Tenure t is years since death, a proxy for tenure at the present level (deaths in 2025 count as half a year). P(hold 100 years) and the median remaining tenure follow from the Aethic Lindy law; δ is the relative attention change in this step.

| rank | name | t (years) | P(hold 100 y), k = 1 | k = 0.25 | median remaining (y), k = 1 | k = 1.38 | k = 0.56 | δ |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Muhammad | 1,393 | 0.933 | 0.983 | 1,393 | 909 | 3,410 | −0.36 |
| 2 | The Buddha | 2,477 | 0.961 | 0.990 | 2,477 | 1,616 | 6,063 | −0.21 |
| 3 | Isaac Newton | 299 | 0.749 | 0.930 | 299 | 195 | 732 | −0.12 |
| 4 | Donald Trump | alive | – | – | – | – | – | +1.46 |
| 5 | Genghis Khan | 798 | 0.889 | 0.971 | 798 | 521 | 1,953 | −0.11 |
| 6 | Cleopatra | 2,055 | 0.954 | 0.988 | 2,055 | 1,341 | 5,030 | −0.50 |
| 7 | Mahatma Gandhi | 77 | 0.435 | 0.812 | 77 | 50 | 188 | −0.35 |
| 8 | Pope Francis | 0.5 | 0.005 | 0.266 | 0.5 | 0.3 | 1.2 | +2.34 |
| 9 | Mary, mother of Jesus | 1,992 | 0.952 | 0.988 | 1,992 | 1,300 | 4,876 | 0.00 |
| 10 | Ludwig van Beethoven | 198 | 0.664 | 0.903 | 198 | 129 | 485 | +0.02 |
| 11 | Leonardo da Vinci | 506 | 0.835 | 0.956 | 506 | 330 | 1,239 | −0.04 |
| 12 | Aristotle | 2,346 | 0.959 | 0.990 | 2,346 | 1,531 | 5,743 | −0.15 |
| 13 | Marco Polo | 701 | 0.875 | 0.967 | 701 | 457 | 1,716 | −0.14 |
| 14 | Elizabeth I | 422 | 0.808 | 0.948 | 422 | 275 | 1,033 | +0.21 |
| 15 | Plato | 2,372 | 0.960 | 0.990 | 2,372 | 1,548 | 5,806 | −0.17 |
| 16 | Alexander the Great | 2,348 | 0.959 | 0.990 | 2,348 | 1,532 | 5,748 | −0.23 |
| 17 | Saint Peter | 1,958 | 0.951 | 0.988 | 1,958 | 1,278 | 4,793 | +0.81 |
| 18 | Homer | 2,775 | 0.965 | 0.991 | 2,775 | 1,811 | 6,793 | −0.10 |
| 19 | Wolfgang Amadeus Mozart | 234 | 0.701 | 0.915 | 234 | 153 | 573 | +0.09 |
| 20 | Napoleon | 204 | 0.671 | 0.905 | 204 | 133 | 499 | −0.70 |

## 4. Cases

### 4.1 Donald Trump

- Rank 4 (previous 17). PVne 17,028,468 against 4,602,003 in the previous record, ×3.70, or ×4.31 relative to the cohort's median change. Raw 35.419 (previous 33.922).
- Without the relative rise his raw score would be 33.957, rank 20. The gap to #1 is 0.262 raw points.
- **Headroom.** The rank-ratio form gives P(ceiling at or above #1's present score) ≈ 1/4. The exponential fits give 0.76 (β from the top 100) and 0.82 (β from the top 1,067); they overstate it, because the top four lie closer together than an exponential tail allows (2.3).

**Holding the present level**, by the Aethic Lindy law with tenure T at this level:

| tenure T at this level | horizon s | P(hold), k = 1 | P(hold), k = 0.25 |
|---|---:|---:|---:|
| 2 years | 5 years | 0.286 | 0.731 |
| 2 years | 15 years | 0.118 | 0.586 |
| 2 years | 50 years | 0.038 | 0.443 |
| 10 years | 5 years | 0.667 | 0.904 |
| 10 years | 15 years | 0.400 | 0.795 |
| 10 years | 50 years | 0.167 | 0.639 |

**After the peak** the model returns the score toward the baseline set by whichever of his attributes outlast the perishable part (2.5, 2.7). Two comparison sets from the 2025 data, defined without reference to him, follow.

*US presidents who died before 1975* (35 people). 12 are in the 2025 top 1,067 and the other 23 are below it, so the median of the class lies below rank 1,067.

| 2025 rank | president | died | previous rank |
|---:|---|---:|---:|
| 40 | Thomas Jefferson | 1826 | 47 |
| 98 | Andrew Jackson | 1845 | 114 |
| 136 | William McKinley | 1901 | 4,636 |
| 145 | Ulysses S. Grant | 1885 | 173 |
| 158 | Martin Van Buren | 1862 | 172 |
| 206 | Abraham Lincoln | 1865 | 154 |
| 209 | James K. Polk | 1849 | 209 |
| 325 | George Washington | 1799 | 310 |
| 328 | John F. Kennedy | 1963 | 246 |
| 338 | Franklin D. Roosevelt | 1945 | 245 |
| 592 | Harry S. Truman | 1972 | 410 |
| 814 | Dwight D. Eisenhower | 1969 | 610 |
| 1,183 | Theodore Roosevelt | 1919 | 811 |
| 3,393 | Andrew Johnson | 1875 | 171 |
| 3,835 | Franklin Pierce | 1869 | 238 |

Below rank 1,067 and not in the extract: John Adams, James Madison, James Monroe, John Quincy Adams, William Henry Harrison, John Tyler, Zachary Taylor, Millard Fillmore, James Buchanan, Rutherford B. Hayes, James A. Garfield, Chester A. Arthur, Grover Cleveland, Benjamin Harrison, William Howard Taft, Woodrow Wilson, Warren G. Harding, Calvin Coolidge, Herbert Hoover, Lyndon B. Johnson.

Presidents alive or died since 1975: Jimmy Carter 29 (died 2024), Ronald Reagan 307, Joe Biden 329, George W. Bush 441, Bill Clinton 704, Richard Nixon 748, George H. W. Bush 788; Gerald Ford and Barack Obama are below 1,067.

*Politicians born in 1750 or later*, highest 2025 ranks:

| 2025 rank | name | born | died | previous rank |
|---:|---|---:|---:|---:|
| 4 | Donald Trump | 1946 | – | 17 |
| 20 | Napoleon | 1769 | 1821 | 11 |
| 22 | Adolf Hitler | 1889 | 1945 | 13 |
| 29 | Jimmy Carter | 1924 | 2024 | 59 |
| 54 | Joseph Stalin | 1879 | 1953 | 45 |
| 67 | Indira Gandhi | 1917 | 1984 | 1,264 |
| 68 | Vladimir Lenin | 1870 | 1924 | 57 |
| 74 | Mustafa Kemal Atatürk | 1881 | 1938 | 64 |
| 88 | George VI | 1895 | 1952 | 1,059 |
| 90 | Franz Joseph I | 1830 | 1916 | 386 |
| 95 | Louis XVI of France | 1754 | 1793 | 123 |
| 98 | Andrew Jackson | 1767 | 1845 | 114 |

Which comparison set applies is not something the data in hand settle; the model's statement is conditional on the durable part.

### 4.2 Alexander the Great: dropped from #1, and not further

Rank 16 in both versions; raw 34.123; relative attention change −0.234, inside the draw noise (the robust standard deviation of a change among people dead over 1,000 years is 0.172). Of the 15 above him, 13 died before 1950; the other two are Trump (alive) and Pope Francis (died 2025).

| 2025 rank | name | born | died | previous rank |
|---:|---|---:|---:|---:|
| 1 | Muhammad | 570 | 632 | 1 |
| 2 | The Buddha | 566 BC | 452 BC | 21 |
| 3 | Isaac Newton | 1643 | 1726 | 2 |
| 4 | Donald Trump | 1946 | – | 17 |
| 5 | Genghis Khan | 1162 | 1227 | 3 |
| 6 | Cleopatra | 69 BC | 30 BC | 66 |
| 7 | Mahatma Gandhi | 1869 | 1948 | 75 |
| 8 | Pope Francis | 1936 | 2025 | 67 |
| 9 | Mary, mother of Jesus | 18 BC | 33 | 37 |
| 10 | Ludwig van Beethoven | 1770 | 1827 | 6 |
| 11 | Leonardo da Vinci | 1452 | 1519 | 5 |
| 12 | Aristotle | 384 BC | 321 BC | 7 |
| 13 | Marco Polo | 1254 | 1324 | 9 |
| 14 | Elizabeth I | 1533 | 1603 | 115 |
| 15 | Plato | 427 BC | 347 BC | 8 |
| 16 | **Alexander the Great** | 356 BC | 323 BC | 16 |

- In this step 7 people rose past him (the Buddha 21→2, Trump 17→4, Cleopatra 66→6, Gandhi 75→7, Pope Francis 67→8, Mary 37→9, Elizabeth I 115→14) and 7 fell below him (Jesus 4→28, Galileo 10→21, Napoleon 11→20, Socrates 12→24, Hitler 13→22, Columbus 14→23, Charlemagne 15→113). His own rank did not move.
- The model's account, taking his ancient #1 as given (Pantheon has no record that far back):
  - **His score held.** At a tenure of 2,348 years since death, his hazard of leaving his band is k/t ≈ 1/2,348 per year at k = 1, his slope noise is about 4.8 × 10⁻⁴ band half-widths per year, and his probability of holding another century is 0.959. His median remaining tenure above his present level is (2^(1/k) − 1)·t: 2,348 years at k = 1, 1,532 at k = 1.38 and 5,748 at k = 0.56.
  - **His rank fell to people placed above him.** A held score loses rank only to arrivals and risers. Of the 15 above him, 12 were born after him; the other 3 (the Buddha, Plato, Aristotle) are older figures whose scores rose past his.
  - **Why not further.** At k = 1 with constant entry, the people above a fixed score spread evenly over doublings of age. Above Alexander's score in 2025 there are 1, 2, 3 and 2 people at ages 100–200, 200–400, 400–800 and 800–1,600 years, about 2 per doubling. The count above him then grows like the logarithm of elapsed time: adding Δ to an elapsed time τ adds about 2·log₂(1 + Δ/τ) people. Counting τ from his death, the next 2,348 years add about two places; counting from the start of writing, about 5,000 years ago, about one. At k > 1 the count levels off; at k < 1, or with entry growing with population, it keeps growing slowly. The two transients above him are the ones the model expects to drop below him first.

### 4.3 Muhammad and Alexander: what separates #1 from #16

From the 2025 components:

| component | Muhammad | Alexander | contribution to the gap (raw points) |
|---|---:|---:|---:|
| language editions L | 223 | 213 | +0.046 |
| effective languages L* | 26.6 | 16.4 | +0.484 |
| age bonus log₄A (A = 1,455 and 2,381 years) | 5.25 | 5.61 | −0.355 |
| non-English page views PVne | 3,732,407 | 3,446,525 | +0.080 |
| CV (enters as −ln CV) | 3.73 | 5.66 | +0.418 |
| undisplayed term |  |  | +0.885 |
| raw HPI | 35.680 | 34.123 | 1.557 |

- The measured difference lies in the breadth and steadiness of attention, not its volume. L* (the effective number of language editions carrying the attention, 26.6 against 16.4) and CV (3.73 against 5.66) account for 0.90 raw points, while the page views differ by 8% (0.08 points). The age bonus favours Alexander by 0.36, and 0.885 points sit in the undisplayed term.
- Attention to Muhammad is carried by a living community across many languages, which is what L* and a low CV register. Antiquity is not erased in the attention data: Alexander's non-English page views are 92% of Muhammad's.
- Pantheon measures attention. An argument that an older figure's influence is screened off by later carriers concerns influence, and these numbers do not test it.

## 5. Waiting time to a drop of 10 places

**What the model fixes.** A drop of 10 places is a fall below a score threshold: the present score of the person 10 places down. The model sets the wait by the tenure above that threshold, not by the size of the cushion. Under the Aethic Lindy law, P(no drop for a further s | above it for t) = (t/(t+s))^k. The mean wait is infinite for k ≤ 1 (it is t/(k − 1) for k > 1), so the number the model fixes is the median, t(2^(1/k) − 1).

**Which exponent.** A drop is one-sided: only falling ends it. For a one-sided threshold the model's exponent is the persistence exponent of integrated Brownian motion, k = 1/4, and the superposition over volatilities does not raise it: the exponent is min(3a/2, 1/4), which is 1/4 at a = 2/3. The median wait is then 15t. The band form of 2.2 gives k = 1 and a median of t. The age structure of 3.1 brackets k at 0.5–1.4 under the two entry assumptions tested, which favours the band form unless entry grew faster than world population. The table gives both.

**Each person as an index.** The pure model knows a person by three numbers only: the score now, the last version's move δ, and the tenure T above the threshold (years since death; for the living, the time since rising above it). It asks first whether the last move was real or a draw (2.10, item 12). A real move has prior rate p = 1/T per version, the Lindy hazard, and a size of the order of the headroom, μ = 1/β = 1.28; a draw's change has standard deviation 0.172. A real rise that carried the person across the threshold, and any real fall (the graded reset of 2.5), leave an effective tenure of one version, τ ≈ 1 year; otherwise the tenure is T. With P_act the weight on the one-version regime,

> P(no drop within s) = P_act·(τ/(τ+s))^k + (1 − P_act)·(T/(T+s))^k.

| rank | name | δ | cushion (raw) | T (years) | P_real | regime | median wait, k = 1 (years) | median wait, k = 1/4 (years) | P(drop within 1 y), k = 1 | within 10 y | within 100 y | draws-only dip, next version |
|---:|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Muhammad | −0.36 | 1.14 | 1,393 | 0.00 | held | 1,391 | 20,837 | 0.1% | 0.8% | 6.8% | 0.0% |
| 2 | The Buddha | −0.21 | 1.15 | 2,477 | 0.00 | held | 2,476 | 37,139 | 0.1% | 0.4% | 3.9% | 0.0% |
| 3 | Isaac Newton | −0.12 | 1.15 | 299 | 0.00 | held | 299 | 4,476 | 0.4% | 3.3% | 25.1% | 0.0% |
| 4 | Donald Trump | +1.46 | 1.15 | alive | 1.00 | risen across the threshold | 1.0 | 15 | 50.0% | 90.9% | 99.0% | 0.0% |
| 5 | Genghis Khan | −0.11 | 0.89 | 798 | 0.00 | held | 798 | 11,960 | 0.1% | 1.3% | 11.2% | 0.0% |
| 6 | Cleopatra | −0.50 | 0.96 | 2,055 | 0.00 | held | 2,040 | 30,413 | 0.2% | 0.8% | 5.0% | 0.0% |
| 7 | Mahatma Gandhi | −0.35 | 0.80 | 77 | 0.01 | held | 75 | 1,111 | 1.9% | 12.6% | 57.1% | 0.0% |
| 8 | Pope Francis | +2.34 | 0.58 | 0.5 | 1.00 | risen across the threshold | 1.0 | 15 | 50.0% | 90.9% | 99.0% | 0.1% |
| 9 | Mary, mother of Jesus | 0.00 | 0.56 | 1,992 | 0.00 | held | 1,992 | 29,871 | 0.1% | 0.5% | 4.8% | 0.1% |
| 10 | Ludwig van Beethoven | +0.02 | 0.57 | 198 | 0.00 | held | 198 | 2,970 | 0.5% | 4.8% | 33.6% | 0.0% |
| 11 | Leonardo da Vinci | −0.04 | 0.62 | 506 | 0.00 | held | 506 | 7,582 | 0.2% | 2.0% | 16.5% | 0.1% |
| 12 | Aristotle | −0.15 | 0.45 | 2,346 | 0.00 | held | 2,346 | 35,178 | 0.1% | 0.4% | 4.1% | 0.9% |
| 13 | Marco Polo | −0.14 | 0.46 | 701 | 0.00 | held | 701 | 10,504 | 0.2% | 1.4% | 12.5% | 0.6% |
| 14 | Elizabeth I | +0.21 | 0.41 | 422 | 0.00 | held | 422 | 6,330 | 0.2% | 2.3% | 19.2% | 0.7% |
| 15 | Plato | −0.17 | 0.40 | 2,372 | 0.00 | held | 2,372 | 35,567 | 0.1% | 0.4% | 4.1% | 0.7% |
| 16 | Alexander the Great | −0.23 | 0.35 | 2,348 | 0.00 | held | 2,347 | 35,201 | 0.1% | 0.4% | 4.1% | 1.6% |
| 17 | Saint Peter | +0.81 | 0.41 | 1,958 | 0.74 | risen across the threshold | 2.0 | 82 | 37.2% | 67.7% | 74.8% | 1.8% |
| 18 | Homer | −0.10 | 0.42 | 2,775 | 0.00 | held | 2,775 | 41,615 | 0.0% | 0.4% | 3.5% | 1.1% |
| 19 | Wolfgang Amadeus Mozart | +0.09 | 0.52 | 234 | 0.00 | held | 234 | 3,510 | 0.4% | 4.1% | 29.9% | 0.6% |
| 20 | Napoleon | −0.70 | 0.50 | 204 | 0.62 | falling (graded reset) | 3.8 | 163 | 31.3% | 58.4% | 74.1% | 0.7% |
| 21 | Galileo Galilei | −0.12 | 0.46 | 383 | 0.00 | held | 383 | 5,735 | 0.3% | 2.6% | 20.7% | 1.1% |
| 22 | Adolf Hitler | +0.02 | 0.43 | 80 | 0.00 | held | 80 | 1,200 | 1.2% | 11.1% | 55.6% | 0.9% |
| 23 | Christopher Columbus | −0.21 | 0.48 | 519 | 0.00 | held | 518 | 7,770 | 0.2% | 1.9% | 16.2% | 0.9% |
| 24 | Socrates | −0.17 | 0.48 | 2,424 | 0.00 | held | 2,424 | 36,347 | 0.1% | 0.4% | 4.0% | 0.6% |
| 25 | Albert Einstein | −0.33 | 0.51 | 70 | 0.01 | held | 68 | 1,017 | 2.0% | 13.4% | 59.3% | 0.5% |
| 26 | Henry VIII | +0.52 | 0.46 | 478 | 0.02 | held | 458 | 6,689 | 1.2% | 3.9% | 19.0% | 0.8% |
| 27 | Marie Curie | +0.11 | 0.37 | 91 | 0.00 | held | 91 | 1,365 | 1.1% | 9.9% | 52.4% | 3.1% |
| 28 | Jesus | −0.10 | 0.35 | 1,992 | 0.00 | held | 1,992 | 29,870 | 0.1% | 0.5% | 4.8% | 3.3% |
| 29 | Jimmy Carter | +0.80 | 0.25 | 1.0 | 1.00 | risen across the threshold | 1.0 | 15 | 50.0% | 90.9% | 99.0% | 9.1% |
| 30 | Pope Benedict XVI | +2.08 | 0.26 | 3.0 | 1.00 | risen across the threshold | 1.0 | 15 | 50.0% | 90.9% | 99.0% | 7.4% |
| 31 | Nicolaus Copernicus | +0.12 | 0.25 | 482 | 0.00 | held | 482 | 7,230 | 0.2% | 2.0% | 17.2% | 8.7% |
| 32 | Julius Caesar | +0.01 | 0.27 | 2,069 | 0.00 | held | 2,069 | 31,035 | 0.1% | 0.5% | 4.6% | 6.9% |
| 33 | Confucius | −0.11 | 0.21 | 2,504 | 0.00 | held | 2,504 | 37,550 | 0.0% | 0.4% | 3.9% | 11.4% |
| 34 | Michelangelo | +0.03 | 0.20 | 461 | 0.00 | held | 461 | 6,915 | 0.2% | 2.1% | 17.8% | 9.4% |
| 35 | Archimedes | −0.33 | 0.23 | 2,237 | 0.00 | held | 2,235 | 33,511 | 0.1% | 0.5% | 4.3% | 13.0% |
| 36 | Pythagoras | −0.17 | 0.21 | 2,520 | 0.00 | held | 2,520 | 37,787 | 0.0% | 0.4% | 3.8% | 12.3% |
| 37 | Vincent van Gogh | −0.11 | 0.23 | 135 | 0.00 | held | 135 | 2,016 | 0.8% | 7.0% | 42.6% | 13.8% |
| 38 | Moses | −0.29 | 0.24 | 3,298 | 0.00 | held | 3,297 | 49,440 | 0.0% | 0.3% | 3.0% | 11.3% |
| 39 | Fyodor Dostoevsky | +0.08 | 0.23 | 144 | 0.00 | held | 144 | 2,160 | 0.7% | 6.5% | 41.0% | 10.8% |
| 40 | Thomas Jefferson | +0.13 | 0.24 | 199 | 0.00 | held | 199 | 2,985 | 0.5% | 4.8% | 33.4% | 9.2% |
| 41 | Che Guevara | −0.08 | 0.22 | 58 | 0.00 | held | 58 | 863 | 1.8% | 14.9% | 63.4% | 10.4% |
| 42 | Louis XIV of France | +0.03 | 0.24 | 310 | 0.00 | held | 310 | 4,650 | 0.3% | 3.1% | 24.4% | 11.6% |
| 43 | Adam Smith | −0.28 | 0.27 | 235 | 0.00 | held | 234 | 3,501 | 0.5% | 4.3% | 30.0% | 9.6% |
| 44 | Mother Teresa | −0.07 | 0.27 | 28 | 0.01 | held | 28 | 414 | 3.7% | 26.7% | 78.3% | 8.2% |
| 45 | Johann Sebastian Bach | +0.42 | 0.21 | 275 | 0.01 | held | 270 | 4,011 | 0.8% | 4.3% | 27.3% | 13.3% |
| 46 | Martin Luther | −0.01 | 0.23 | 479 | 0.00 | held | 479 | 7,177 | 0.2% | 2.1% | 17.3% | 11.3% |
| 47 | Ferdinand Magellan | −0.29 | 0.18 | 504 | 0.00 | held | 503 | 7,533 | 0.2% | 2.0% | 16.6% | 16.1% |
| 48 | William Shakespeare | −0.03 | 0.19 | 409 | 0.00 | held | 409 | 6,127 | 0.3% | 2.4% | 19.7% | 15.0% |
| 49 | Pope John Paul II | +1.81 | 0.19 | 20 | 1.00 | risen across the threshold | 1.0 | 15 | 50.0% | 90.9% | 99.0% | 13.7% |
| 50 | Martin Luther King Jr. | +0.05 | 0.18 | 57 | 0.00 | held | 57 | 855 | 1.7% | 14.9% | 63.7% | 14.0% |

**What it says.**

- **Held (43 of the 50).** The last move is a draw (P_real under 3%) and the wait is set by the long tenure: a median of about T years at k = 1 and 15T at k = 1/4. Muhammad's −0.36 is read as a draw because, at a tenure of 1,393 years, a real move is far rarer than a two-sigma draw.
- **Risen across the threshold.** Trump, Pope Francis, Jimmy Carter, Benedict XVI and John Paul II (P_real = 1) and Saint Peter (0.74) were below their thresholds one version ago. Their tenure above them is one version, so the median wait is 1 year at k = 1 and 15 years at k = 1/4 (Saint Peter 2.1 and 82, the mixture with his long tenure).
- **Falling.** Napoleon's −0.70 is read as real (0.62): a median of 3.8 years at k = 1 and 163 at k = 1/4.
- **Read as draws.** Henry VIII (+0.52) and Bach (+0.42): at tenures of 478 and 275 years a real move is rarer than a draw of that size.

**Trump as an index.** The cushion is 1.151 raw points. His relative attention would have to fall to 1/3.16 of its 2025 level, about four-fifths of the 2025 rise (×4.31) in log terms, to put him below the present #14 (Elizabeth I, raw 34.268). In the previous record (raw 33.922) he was below that threshold, so the record is a rise from below it within one version. With nothing else entering, the median wait is 1 year at k = 1 and 15 years at k = 1/4, and the probability of no drop for 5 years is 0.17 and 0.64:

| further years s | P(no drop), k = 1 | P(no drop), k = 1/4 |
|---:|---:|---:|
| 1 | 0.50 | 0.84 |
| 2 | 0.33 | 0.76 |
| 5 | 0.17 | 0.64 |
| 10 | 0.09 | 0.55 |
| 20 | 0.05 | 0.47 |
| 50 | 0.02 | 0.37 |

After the drop, the odds of regaining #4 are at most about the rank ratio of 2.6: 0.29 from #14, 0.20 from #20, 0.04 from #100.

**Draws.** The cushion decides how often a version shows a 10-place drop that is not one. From draws alone (a change with standard deviation 0.172 raw points), ranks 1–11 essentially never dip 10 places in a version, ranks 12–28 do so 0.5–3% of the time, and ranks 29–50 7–16% of the time, because their cushions are only 0.18–0.27 raw points, a loss of 16–24% of relative attention.

**Extra information beyond the pure model.** The data also show how spikes with a known cause have faded. People whose deaths fell in the previous record lost most of the spike in the next one: Toto Cutugno ×0.17, Franz Beckenbauer ×0.23, Henry Kissinger ×0.26. Against that pace, Pope Francis's 2025 rise was ×10.4 against a cushion of ÷1.79, Benedict XVI's ×8.0 against ÷1.29, John Paul II's ×6.1 against ÷1.21, Saint Peter's ×2.25 against ÷1.51 and Jimmy Carter's ×2.2 against ÷1.28, which points to a drop within a version or two. Henry VIII (×1.68 against ÷1.58) and Bach (×1.53 against ÷1.23) have smaller rises that still exceed their cushions. For Trump, the extra attention comes with an office running to January 2029, and Biden's first record after leaving office shows a relative change of ×0.79 (δ = −0.242). At that rate the loss takes about 4.7 years after leaving office, around 2033–34. For scale, a drop of 10 HPI points rather than 10 places (3.57 raw points) would put him at about rank 138.

**Percentiles of the wait under the adopted weight over k** (2.11). With k held blank, each person's wait has a whole distribution. Its percentiles from the 5th to the 75th, in years:

| rank | name | regime | 5th | 10th | 25th | 40th | 50th | 60th | 75th |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Muhammad | held | 395 | 953 | 4,721 | 20,170 | 63,702 | 275,526 | 8.4 × 10⁶ |
| 2 | The Buddha | held | 747 | 1,805 | 9,146 | 40,711 | 133,802 | 610,874 | 2.1 × 10⁷ |
| 3 | Isaac Newton | held | 74 | 174 | 802 | 3,064 | 8,682 | 32,385 | 698,347 |
| 4 | Donald Trump | risen across the threshold | 0.07 | 0.15 | 0.51 | 1.2 | 2.2 | 4.4 | 19 |
| 5 | Genghis Khan | held | 218 | 520 | 2,501 | 10,261 | 31,173 | 127,912 | 3.5 × 10⁶ |
| 6 | Cleopatra | held | 567 | 1,412 | 7,220 | 31,785 | 103,086 | 461,929 | 1.5 × 10⁷ |
| 7 | Mahatma Gandhi | held | 13 | 33 | 153 | 532 | 1,366 | 4,433 | 68,317 |
| 8 | Pope Francis | risen across the threshold | 0.07 | 0.15 | 0.51 | 1.2 | 2.2 | 4.4 | 19 |
| 9 | Mary, mother of Jesus | held | 590 | 1,422 | 7,135 | 31,266 | 101,229 | 452,884 | 1.5 × 10⁷ |
| 10 | Ludwig van Beethoven | held | 47 | 111 | 498 | 1,843 | 5,071 | 18,161 | 355,611 |
| 11 | Leonardo da Vinci | held | 132 | 314 | 1,479 | 5,868 | 17,263 | 67,795 | 1.7 × 10⁶ |
| 12 | Aristotle | held | 704 | 1,701 | 8,598 | 38,119 | 124,817 | 566,983 | 1.9 × 10⁷ |
| 13 | Marco Polo | held | 189 | 450 | 2,153 | 8,752 | 26,347 | 106,770 | 2.8 × 10⁶ |
| 14 | Elizabeth I | held | 109 | 257 | 1,201 | 4,701 | 13,654 | 52,687 | 1.2 × 10⁶ |
| 15 | Plato | held | 713 | 1,721 | 8,706 | 38,632 | 126,589 | 575,625 | 2.0 × 10⁷ |
| 16 | Alexander the Great | held | 705 | 1,702 | 8,606 | 38,159 | 124,953 | 567,647 | 1.9 × 10⁷ |
| 17 | Saint Peter | risen across the threshold | 0.09 | 0.21 | 0.85 | 2.8 | 8.0 | 44 | 5,152 |
| 18 | Homer | held | 845 | 2,043 | 10,409 | 46,709 | 154,715 | 713,835 | 2.5 × 10⁷ |
| 19 | Wolfgang Amadeus Mozart | held | 57 | 133 | 605 | 2,269 | 6,316 | 22,999 | 468,496 |
| 20 | Napoleon | falling (graded reset) | 0.11 | 0.27 | 1.2 | 5.9 | 30 | 213 | 3,311 |
| 21 | Galileo Galilei | held | 97 | 230 | 1,070 | 4,161 | 12,002 | 45,870 | 1.0 × 10⁶ |
| 22 | Adolf Hitler | held | 17 | 40 | 171 | 592 | 1,525 | 4,983 | 78,316 |
| 23 | Christopher Columbus | held | 135 | 322 | 1,520 | 6,044 | 17,813 | 70,119 | 1.7 × 10⁶ |
| 24 | Socrates | held | 730 | 1,763 | 8,924 | 39,659 | 130,151 | 593,013 | 2.0 × 10⁷ |
| 25 | Albert Einstein | held | 12 | 31 | 138 | 476 | 1,215 | 3,905 | 58,874 |
| 26 | Henry VIII | held | 79 | 234 | 1,224 | 4,913 | 14,382 | 55,830 | 1.3 × 10⁶ |
| 27 | Marie Curie | held | 20 | 46 | 200 | 697 | 1,811 | 5,997 | 97,301 |
| 28 | Jesus | held | 590 | 1,422 | 7,135 | 31,266 | 101,229 | 452,884 | 1.5 × 10⁷ |
| 29 | Jimmy Carter | risen across the threshold | 0.07 | 0.15 | 0.51 | 1.2 | 2.2 | 4.4 | 19 |
| 30 | Pope Benedict XVI | risen across the threshold | 0.07 | 0.15 | 0.51 | 1.2 | 2.2 | 4.4 | 19 |
| 31 | Nicolaus Copernicus | held | 126 | 298 | 1,400 | 5,537 | 16,233 | 63,453 | 1.5 × 10⁶ |
| 32 | Julius Caesar | held | 616 | 1,484 | 7,455 | 32,757 | 106,334 | 477,424 | 1.6 × 10⁷ |
| 33 | Confucius | held | 756 | 1,826 | 9,260 | 41,249 | 135,670 | 620,027 | 2.2 × 10⁷ |
| 34 | Michelangelo | held | 120 | 284 | 1,330 | 5,242 | 15,319 | 59,623 | 1.4 × 10⁶ |
| 35 | Archimedes | held | 665 | 1,609 | 8,128 | 35,921 | 117,230 | 530,110 | 1.8 × 10⁷ |
| 36 | Pythagoras | held | 761 | 1,839 | 9,327 | 41,568 | 136,779 | 625,467 | 2.2 × 10⁷ |
| 37 | Vincent van Gogh | held | 30 | 71 | 315 | 1,136 | 3,039 | 10,471 | 186,839 |
| 38 | Moses | held | 1,016 | 2,464 | 12,658 | 57,511 | 192,759 | 903,625 | 3.3 × 10⁷ |
| 39 | Fyodor Dostoevsky | held | 33 | 77 | 343 | 1,239 | 3,332 | 11,557 | 209,694 |
| 40 | Thomas Jefferson | held | 47 | 111 | 501 | 1,855 | 5,105 | 18,291 | 358,584 |
| 41 | Che Guevara | held | 11 | 27 | 115 | 389 | 978 | 3,090 | 44,709 |
| 42 | Louis XIV of France | held | 77 | 183 | 840 | 3,214 | 9,130 | 34,182 | 743,716 |
| 43 | Adam Smith | held | 55 | 131 | 601 | 2,256 | 6,283 | 22,875 | 465,575 |
| 44 | Mother Teresa | held | 4.8 | 11 | 47 | 151 | 360 | 1,053 | 12,606 |
| 45 | Johann Sebastian Bach | held | 57 | 146 | 695 | 2,653 | 7,471 | 27,576 | 579,158 |
| 46 | Martin Luther | held | 124 | 295 | 1,387 | 5,483 | 16,067 | 62,761 | 1.5 × 10⁶ |
| 47 | Ferdinand Magellan | held | 129 | 310 | 1,465 | 5,815 | 17,102 | 67,117 | 1.6 × 10⁶ |
| 48 | William Shakespeare | held | 104 | 247 | 1,155 | 4,514 | 13,081 | 50,318 | 1.2 × 10⁶ |
| 49 | Pope John Paul II | risen across the threshold | 0.07 | 0.15 | 0.51 | 1.2 | 2.2 | 4.4 | 19 |
| 50 | Martin Luther King Jr. | held | 12 | 27 | 114 | 386 | 968 | 3,054 | 44,086 |

The spread is the heavy tail of the Lindy law. The mean wait is infinite, and past the 75th percentile the waits of the long-held run beyond millions of years (their 90th percentiles reach 10⁶–10¹¹), which says only that the model sets no horizon by which their drop becomes likely. The lower percentiles carry the usable information: a 5% chance of a 10-place drop within about 390 years for Muhammad, 74 for Newton, 13 for Gandhi and 0.07 (about three and a half weeks) for anyone who has just risen across the line, and a 10% chance within about 950, 170, 33 and 0.15.

## 6. Were today's top 50 higher before?

The model's answer turns on tenure.

**The recently dead and the event-driven: yes.** Attention peaks at the event or at death and falls on the communicative-memory time scale of about 20–30 years (2.7). Falls outsize rises, and after the reset the odds of regaining the peak are about rank(peak)/rank(now) (2.6), so the model expects these people to have been higher and not to return. In this version step the signed relative change is slightly negative on average for people dead 2–30 years and flat for people dead 30–100 years: the fall is concentrated in the first decades, and after them the level holds.

| group | n | median δ | mean δ | share negative |
|---|---:|---:|---:|---:|
| alive | 64 | +0.026 | +0.018 | 43.8% |
| 0–2 years since death | 5 | −0.535 | +0.115 | 60.0% |
| 2–10 | 31 | −0.031 | −0.100 | 54.8% |
| 10–30 | 41 | −0.008 | −0.057 | 53.7% |
| 30–60 | 101 | +0.023 | +0.018 | 47.5% |
| 60–100 | 103 | +0.029 | +0.072 | 40.8% |
| 100–300 | 229 | −0.011 | +0.032 | 55.5% |
| 300–1,000 | 206 | +0.040 | +0.083 | 38.8% |
| 1,000–4,000 | 211 | −0.047 | −0.014 | 60.7% |

In the top 50 this covers the six who died 1925–1975 (Marie Curie, Hitler, Gandhi, Einstein, Che Guevara, Martin Luther King Jr.), who on this account are past most of their fall, and Mother Teresa (died 1997), near the end of it. Trump, Pope Francis, Jimmy Carter, Benedict XVI and John Paul II are at or near a peak now, on the 2025 spikes of section 5.

**The long dead: the model says no.** Long tenure keeps the slope noise near 1.12 w/t and the hazard of a reset near k/t, so a large fall in the last few decades would be rare for someone dead for centuries. On the model's account they are where they are because they held, not because they fell.

**The rank losses between the two versions are mostly the instrument and other people's rises.** Splitting each change in raw score (relative to the cohort's median change) into page views, CV, L and the rest, where the rest is the formula's new terms (L* and the undisplayed term):

| name | rank, previous → 2025 | relative raw change | page views (δ) | −ln CV | ln L | rest: L* and the undisplayed term |
|---|---:|---:|---:|---:|---:|---:|
| Jesus | 4 → 28 | −1.418 | −0.097 | −0.075 | +0.033 | −1.279 |
| Galileo Galilei | 10 → 21 | −0.316 | −0.122 | −0.022 | +0.025 | −0.197 |
| Napoleon | 11 → 20 | −0.188 | −0.696 | +0.107 | +0.043 | +0.358 |
| Socrates | 12 → 24 | −0.302 | −0.169 | −0.010 | +0.025 | −0.147 |
| Adolf Hitler | 13 → 22 | −0.164 | +0.022 | −0.037 | +0.034 | −0.183 |
| Christopher Columbus | 14 → 23 | −0.085 | −0.207 | +0.012 | +0.029 | +0.081 |
| Charlemagne | 15 → 113 | −1.871 | −0.076 | −0.488 | +0.025 | −1.333 |
| Cleopatra | 66 → 6 | +2.492 | −0.500 | +0.756 | +0.027 | +2.209 |
| Mahatma Gandhi | 75 → 7 | +2.454 | −0.354 | +0.771 | +0.030 | +2.007 |
| Elizabeth I | 115 → 14 | +2.462 | +0.213 | +0.663 | +0.027 | +1.559 |
| The Buddha | 21 → 2 | +1.914 | −0.207 | +0.643 | +0.024 | +1.454 |

Jesus and Charlemagne lost 1.28 and 1.33 raw points to the new terms while their relative page views changed by −0.10 and −0.08; Galileo, Socrates and Hitler lost 0.15–0.20 that way; Napoleon and Columbus lost attention instead. Most of the rank lost came from others rising past them: 24 people passed Jesus, among them Cleopatra, Gandhi and Elizabeth I, who gained 1.6–2.2 raw points from the same new terms.

## 7. The median ranking in 2075

With no new people entering, each person's median score fifty years on follows from three of the model's rules.

- **A last move read as a draw** (P_real below 1/2, the test of section 5) is averaged out: the latent level is the mean of the two versions, S − δ/2.
- **A last move read as a real rise** is a perishable excess. Someone who has just risen leaves that level within 50 years with probability above 3/4 (under the adopted weight over k, the 75th percentile of the wait is 19 years), so the median is the baseline before the rise, S − δ.
- **Otherwise the median change is zero.** Future moves are symmetric in ln G and the score is a monotone function of ln G, so the median score does not move, even though falls outsize rises and the mean declines.

Pantheon's formula adds the rest. Its age term grows by log₄((A + 50)/A): 0.35 raw points for Trump, 0.21 for Einstein, and about 0.1 or less for anyone born before 1700. Its youth penalty, (70 − A)/7, expires for the nine people now under 70. The penalty appears to be in the 2025 scores: without it, Elon Musk's residual against the displayed formula would be 4.71, below the range of the 28 people over 70 checked (5.21–9.33); with it, 6.99.

| 2075 | name | 2025 | 2075 on attention alone | gain from the formula's age terms (raw) | median projected score (HPI, 2025 scale) |
|---:|---|---:|---:|---:|---:|
| 1 | Muhammad | 1 | 1 | +0.02 | 100.57 |
| 2 | Isaac Newton | 3 | 3 | +0.09 | 99.85 |
| 3 | The Buddha | 2 | 2 | +0.01 | 99.81 |
| 4 | Cleopatra | 6 | 4 | +0.02 | 99.09 |
| 5 | Mahatma Gandhi | 7 | 6 | +0.20 | 98.77 |
| 6 | Genghis Khan | 5 | 5 | +0.04 | 98.71 |
| 7 | Ludwig van Beethoven | 10 | 8 | +0.13 | 97.23 |
| 8 | Leonardo da Vinci | 11 | 9 | +0.06 | 97.02 |
| 9 | Mary, mother of Jesus | 9 | 7 | +0.02 | 96.99 |
| 10 | Marco Polo | 13 | 11 | +0.05 | 96.53 |
| 11 | Aristotle | 12 | 10 | +0.01 | 96.50 |
| 12 | Plato | 15 | 12 | +0.01 | 96.22 |
| 13 | Donald Trump | 4 | 21 | +0.35 | 96.16 |
| 14 | Alexander the Great | 16 | 13 | +0.01 | 96.00 |
| 15 | Elizabeth I | 14 | 14 | +0.07 | 95.94 |
| 16 | Albert Einstein | 25 | 16 | +0.21 | 95.88 |
| 17 | Napoleon | 20 | 17 | +0.13 | 95.65 |
| 18 | Wolfgang Amadeus Mozart | 19 | 18 | +0.12 | 95.59 |
| 19 | Adolf Hitler | 22 | 23 | +0.23 | 95.59 |
| 20 | Homer | 18 | 15 | +0.01 | 95.58 |
| 21 | Galileo Galilei | 21 | 19 | +0.07 | 95.46 |
| 22 | Christopher Columbus | 23 | 20 | +0.06 | 95.37 |
| 23 | Socrates | 24 | 22 | +0.01 | 95.18 |
| 24 | Marie Curie | 27 | 25 | +0.20 | 94.71 |
| 25 | Jesus | 28 | 24 | +0.02 | 94.42 |
| 26 | Henry VIII | 26 | 26 | +0.06 | 94.11 |
| 27 | Che Guevara | 41 | 36 | +0.30 | 94.04 |
| 28 | Vincent van Gogh | 37 | 34 | +0.18 | 93.93 |
| 29 | Archimedes | 35 | 27 | +0.02 | 93.91 |
| 30 | Mother Teresa | 44 | 39 | +0.26 | 93.81 |
| 31 | Julius Caesar | 32 | 28 | +0.02 | 93.81 |
| 32 | Nicolaus Copernicus | 31 | 31 | +0.06 | 93.80 |
| 33 | Confucius | 33 | 29 | +0.01 | 93.76 |
| 34 | Adam Smith | 43 | 35 | +0.11 | 93.70 |
| 35 | Moses | 38 | 30 | +0.01 | 93.69 |
| 36 | Michelangelo | 34 | 33 | +0.06 | 93.69 |
| 37 | Pythagoras | 36 | 32 | +0.01 | 93.64 |
| 38 | Fyodor Dostoevsky | 39 | 38 | +0.16 | 93.53 |
| 39 | Thomas Jefferson | 40 | 41 | +0.12 | 93.33 |
| 40 | Martin Luther King Jr. | 50 | 46 | +0.30 | 93.27 |
| 41 | Saint Peter | 17 | 37 | +0.02 | 93.23 |
| 42 | Louis XIV of France | 42 | 42 | +0.09 | 93.21 |
| 43 | Ferdinand Magellan | 47 | 40 | +0.06 | 93.20 |
| 44 | Martin Luther | 46 | 43 | +0.06 | 92.96 |
| 45 | William Shakespeare | 48 | 44 | +0.07 | 92.84 |
| 46 | Frédéric Chopin | 51 | 47 | +0.15 | 92.80 |
| 47 | Immanuel Kant | 52 | 45 | +0.11 | 92.78 |
| 48 | Karl Marx | 53 | 49 | +0.16 | 92.78 |
| 49 | Charles III | 63 | 63 | +0.36 | 92.71 |
| 50 | Joseph Stalin | 54 | 56 | +0.21 | 92.64 |

Where this year's risers land: Trump 13 (21 on attention alone), Saint Peter 41, Jimmy Carter 53, Pope Francis 77, Benedict XVI 168 and John Paul II 200. Elon Musk would climb from 273 to 63, all of it from the formula's age terms; on attention alone he would fall to 461. The long-held barely move. Muhammad stays first, and Newton and the Buddha, 0.01 raw points apart, are well within one draw of each other.

**The general Aethus.** The projection is the verdict of the general Aethus. Each person enters only as the generic member who has reached their score, with their last move and their tenure, at this time. Information about the particular person moves their quantile within that superposition. In the author's reading, what is known of Trump in particular puts him well below the median of the generic member with his record, so the model's 2075 placement of him is higher than his own Aethus would give.

**Adjusted by what is known of particular people.** The table below moves the model's medians by information specific to particular people. The moves are judgments, applied by fixed rules, and not outputs of the model:

- **J1.** A dated event sits in one of the two records, and the model averaged it as a draw. The averaging is undone: −|δ|/2.
- **J2.** A dated event sits in the baseline to which a real riser is returned. An anniversary-sized spike is removed: −0.14 raw points, the median one-version fall after the three anniversaries in the data (Marco Polo 2024, Adam Smith 2023, Kant 2024).
- **J3.** A living head of state whose median would put them above every past holder of the same office is placed halfway between that median and the 2075 projection of the highest past holder. This applies to Trump (Jefferson), Charles III (George VI) and Putin (Boris Yeltsin).
- **J4.** An anniversary falls in 2075: +0.14. This applies to Michelangelo, born on 6 March 1475.
- **J5.** Above the median, not quantified: Muhammad. Pew projects the Muslim population to grow 70% from 2015 to 2060, against 32% for the world [Pew Research Center 2017]; he stays first either way.

| judged | name | model | 2025 | judgment | shift (raw) | reason |
|---:|---|---:|---:|---|---:|---|
| 1 | Muhammad | 1 | 1 | above the median | not quantified | J5: Pew projects the Muslim population to grow 70% from 2015 to 2060, against 32% for the world |
| 2 | Isaac Newton | 2 | 3 | at the median | – | – |
| 3 | The Buddha | 3 | 2 | at the median | – | – |
| 4 | Mahatma Gandhi | 5 | 7 | at the median | – | – |
| 5 | Genghis Khan | 6 | 5 | at the median | – | – |
| 6 | Cleopatra | 4 | 6 | below the median | −0.25 | J1: the 2024 record held the attention to Netflix's Queen Cleopatra (2023) |
| 7 | Ludwig van Beethoven | 7 | 10 | at the median | – | – |
| 8 | Leonardo da Vinci | 8 | 11 | at the median | – | – |
| 9 | Mary, mother of Jesus | 9 | 9 | at the median | – | – |
| 10 | Aristotle | 11 | 12 | at the median | – | – |
| 11 | Marco Polo | 10 | 13 | below the median | −0.07 | J1: the 2024 record held the 700th anniversary of his death |
| 12 | Plato | 12 | 15 | at the median | – | – |
| 13 | Alexander the Great | 14 | 16 | at the median | – | – |
| 14 | Elizabeth I | 15 | 14 | at the median | – | – |
| 15 | Napoleon | 17 | 20 | at the median | – | – |
| 16 | Wolfgang Amadeus Mozart | 18 | 19 | at the median | – | – |
| 17 | Adolf Hitler | 19 | 22 | at the median | – | – |
| 18 | Homer | 20 | 18 | at the median | – | – |
| 19 | Galileo Galilei | 21 | 21 | at the median | – | – |
| 20 | Albert Einstein | 16 | 25 | below the median | −0.16 | J1: the 2024 record held the attention from the film Oppenheimer (2023) |
| 21 | Christopher Columbus | 22 | 23 | at the median | – | – |
| 22 | Socrates | 23 | 24 | at the median | – | – |
| 23 | Donald Trump | 13 | 4 | below the median | −0.50 | J3: above every past US president in the median; placed halfway to Thomas Jefferson |
| 24 | Marie Curie | 24 | 27 | at the median | – | – |
| 25 | Jesus | 25 | 28 | at the median | – | – |
| 26 | Michelangelo | 36 | 34 | above the median | +0.14 | J4: the 600th anniversary of his birth falls in March 2075 |
| 27 | Che Guevara | 27 | 41 | at the median | – | – |
| 28 | Vincent van Gogh | 28 | 37 | at the median | – | – |
| 29 | Archimedes | 29 | 35 | at the median | – | – |
| 30 | Mother Teresa | 30 | 44 | at the median | – | – |
| 31 | Julius Caesar | 31 | 32 | at the median | – | – |
| 32 | Nicolaus Copernicus | 32 | 31 | at the median | – | – |
| 33 | Confucius | 33 | 33 | at the median | – | – |
| 34 | Moses | 35 | 38 | at the median | – | – |
| 35 | Pythagoras | 37 | 36 | at the median | – | – |
| 36 | Fyodor Dostoevsky | 38 | 39 | at the median | – | – |
| 37 | Henry VIII | 26 | 26 | below the median | −0.26 | J1: the 2025 record held the BBC's Wolf Hall: The Mirror and the Light (2024) |
| 38 | Thomas Jefferson | 39 | 40 | at the median | – | – |
| 39 | Adam Smith | 34 | 43 | below the median | −0.14 | J1: the 2024 record held the 300th anniversary of his birth |
| 40 | Martin Luther King Jr. | 40 | 50 | at the median | – | – |
| 41 | Saint Peter | 41 | 17 | at the median | – | – |
| 42 | Louis XIV of France | 42 | 42 | at the median | – | – |
| 43 | Ferdinand Magellan | 43 | 47 | at the median | – | – |
| 44 | Martin Luther | 44 | 46 | at the median | – | – |
| 45 | William Shakespeare | 45 | 48 | at the median | – | – |
| 46 | Frédéric Chopin | 46 | 51 | at the median | – | – |
| 47 | Karl Marx | 48 | 53 | at the median | – | – |
| 48 | Immanuel Kant | 47 | 52 | below the median | −0.05 | J1: the 300th anniversary of his birth (2024) |
| 49 | Joseph Stalin | 50 | 54 | at the median | – | – |
| 50 | Nikola Tesla | 51 | 61 | at the median | – | – |

Moved by the rules: Trump 13 → 23, Charles III 49 → 67, Putin 88 → 193, Jimmy Carter 53 → 63, Henry VIII 26 → 37, Adam Smith 34 → 39, Einstein 16 → 20, Cleopatra 4 → 6 and Michelangelo 36 → 26. Which event sits in which record (J1) depends on Pantheon's page-view windows, which the data do not state.

## 8. Limits and next tests

- Two versions with a formula change between them cannot test the gap dynamics, the tenure dependence of the hazards or the reset rule.
- Pantheon publishes earlier snapshots (person_2019_update.csv.bz2, person_2020_update.csv.bz2 and the 2025 file, at pantheon.world/data/datasets). Attached to the conversation, they can be read with Python's bz2 module here, and they would allow:
  1. survival curves of rank bands by tenure, to estimate k;
  2. the draw noise across steps without a formula change;
  3. dips against falls: dips of a few draw sizes should recover and falls beyond the band should not, and among people who fell from rank r₀ to beyond rank r, the share later back at r₀ should be at most about r₀/r;
  4. where new entries into the top 20 come from: mostly from outside the current top 20, the model says, and rarely from former members.
- Daily page views from Wikimedia would give the decay of spikes, P(t), person by person.

## Files

In `lindy/`:

| File | Content |
|---|---|
| `lindy_pantheon_results.md` | this file |
| `pantheon_2025_top1067.csv` | 2025 ranks 1–1,067, with previous values and 2024 components |
| `pantheon_previous_top1000_dropouts.csv` | the 174 who left the top 1,067 |
| `top_2025.psv`, `exits.psv`, `hpi_components.psv` | the extracts as read from the API |
| `extract.py`, `load.py` | parsing and loading |
| `analysis.py` → `results.json` | the data figures |
| `sim.py` → `sim_results.json` | the simulations of 2.2 and 2.4 (seed 1042) |
| `extras.py` → `durability_top20.json` | the durability column and the CSVs |
| `extras2.py` → `extras2.json` | Alexander, the regain odds, the top end, the presidents |
| `extras3.py` → `extras3.json` | the draw layer of 2.8 (seed 1050) |
| `extras4.py` → `extras4.json` | the waiting times of section 5 and the comparisons of section 6 (seed 1051) |
| `extras5.py` → `extras5.json` | the pure-model deduction of section 5 |
| `extras6.py` → `extras6.json` | the comparison weights over k in 2.11 |
| `extras7.py` → `extras7.json` | the piecewise quadratic weight over k in 2.11 |
| `extras8.py` → `extras8.json` | the author's smooth weights over k in 2.11 |
| `extras9.py` → `extras9.json` | the comparison lognormals over k in 2.11 |
| `extras10.py` → `extras10.json` | the adopted lognormal over k (2.11) and the percentiles of the wait for the top 50 (section 5) |
| `extras11.py` → `extras11.json` | the median ranking in 2075 (section 7) |
| `extras12.py` → `extras12.json` | the judgment-adjusted ranking in 2075 (section 7) |
| `build_md.py` | assembles this file from the outputs |

## Sources

- Pantheon: datasets, API and methods. pantheon.world; api.pantheon.world.
- Yu, A. Z., Ronen, S., Hu, K., Lu, T. and Hidalgo, C. A. (2016). Pantheon 1.0, a manually verified dataset of globally famous biographies. *Scientific Data* 3, 150075.
- Candia, C., Jara-Figueroa, C., Rodriguez-Sickert, C., Barabási, A.-L. and Hidalgo, C. A. (2019). The universal decay of collective memory and attention. *Nature Human Behaviour* 3, 82–91.
- Pew Research Center (2017). Why Muslims are the world's fastest-growing religious group. pewresearch.org.
- HYDE estimates of world population (Klein Goldewijk et al. 2011), as tabulated in Wikipedia, "Estimates of historical world population".
- The long Aethic paper: Proposition "The Aethic Lindy law". The Golden reasoning paper: noise placed on −d/dt log h, and the t^(−1/4) tail.

## Appendix A. Pantheon 2025, ranks 1–1,067

From `person_ranks` (2025 version). HPI is the 2025 normalized index (Muhammad = 100); L is the number of Wikipedia language editions; PVne is non-English page views; CV is the coefficient of variation of the page views; previous rank is the rank in the previous version. Every row is also in `pantheon_2025_top1067.csv`, with raw HPI and the 2024 components.

| rank | name | born | died | occupation | birth country | HPI | previous rank | L | PVne | CV |
|---:|---|---:|---:|---|---|---:|---:|---:|---:|---:|
| 1 | Muhammad | 570 | 632 | Religious figure | Saudi Arabia | 100.00 | 1 | 223 | 3,732,407 | 3.73 |
| 2 | The Buddha | 566 BC | 452 BC | Philosopher | Nepal | 99.48 | 21 | 209 | 2,038,657 | 3.09 |
| 3 | Isaac Newton | 1643 | 1726 | Physicist | United Kingdom | 99.44 | 2 | 235 | 2,508,822 | 3.78 |
| 4 | Donald Trump | 1946 | – | Politician | United States | 99.27 | 17 | 253 | 17,028,468 | 4.19 |
| 5 | Genghis Khan | 1162 | 1227 | Military personnel | Mongolia | 98.43 | 3 | 176 | 2,506,097 | 3.04 |
| 6 | Cleopatra | 69 BC | 30 BC | Politician | Egypt | 98.34 | 66 | 151 | 11,936,188 | 3.45 |
| 7 | Mahatma Gandhi | 1869 | 1948 | Social activist | India | 97.71 | 75 | 203 | 2,628,164 | 3.11 |
| 8 | Pope Francis | 1936 | 2025 | Religious figure | Argentina | 97.04 | 67 | 175 | 21,779,849 | 3.91 |
| 9 | Mary, mother of Jesus | 18 BC | 33 | Religious figure | Israel | 96.94 | 37 | 154 | 1,743,390 | 2.71 |
| 10 | Ludwig van Beethoven | 1770 | 1827 | Composer | Germany | 96.89 | 6 | 210 | 2,365,134 | 3.58 |
| 11 | Leonardo da Vinci | 1452 | 1519 | Inventor | Italy | 96.80 | 5 | 239 | 3,273,509 | 5.38 |
| 12 | Aristotle | 384 BC | 321 BC | Philosopher | Greece | 96.25 | 7 | 223 | 2,064,018 | 4.90 |
| 13 | Marco Polo | 1254 | 1324 | Explorer | Italy | 96.21 | 9 | 180 | 1,132,881 | 3.09 |
| 14 | Elizabeth I | 1533 | 1603 | Nobleman | United Kingdom | 96.04 | 115 | 149 | 2,448,515 | 3.09 |
| 15 | Plato | 427 BC | 347 BC | Philosopher | Greece | 95.94 | 8 | 217 | 1,880,518 | 4.78 |
| 16 | Alexander the Great | 356 BC | 323 BC | Military personnel | Greece | 95.63 | 16 | 213 | 3,446,525 | 5.66 |
| 17 | Saint Peter | 1 BC | 67 | Religious figure | NA | 95.46 | 20 | 128 | 2,614,821 | 2.88 |
| 18 | Homer | 800 BC | 750 BC | Writer | Greece | 95.41 | 42 | 194 | 910,867 | 3.68 |
| 19 | Wolfgang Amadeus Mozart | 1756 | 1791 | Composer | Austria | 95.37 | 22 | 222 | 2,944,272 | 4.90 |
| 20 | Napoleon | 1769 | 1821 | Politician | France | 95.29 | 11 | 214 | 5,230,908 | 5.46 |
| 21 | Galileo Galilei | 1564 | 1642 | Astronomer | Italy | 95.08 | 10 | 203 | 2,020,893 | 4.69 |
| 22 | Adolf Hitler | 1889 | 1945 | Politician | Austria | 94.99 | 13 | 242 | 7,771,929 | 6.25 |
| 23 | Christopher Columbus | 1451 | 1506 | Explorer | Italy | 94.91 | 14 | 208 | 2,652,017 | 5.34 |
| 24 | Socrates | 470 BC | 399 BC | Philosopher | Greece | 94.90 | 12 | 201 | 1,808,911 | 4.72 |
| 25 | Albert Einstein | 1879 | 1955 | Physicist | Germany | 94.83 | 18 | 228 | 4,679,204 | 5.55 |
| 26 | Henry VIII | 1491 | 1547 | Nobleman | United Kingdom | 94.65 | 270 | 106 | 2,858,372 | 2.56 |
| 27 | Marie Curie | 1867 | 1934 | Physicist | Poland | 94.30 | 126 | 189 | 3,356,078 | 4.10 |
| 28 | Jesus | 4 BC | 33 | Religious figure | Israel | 94.24 | 4 | 274 | 4,105,287 | 6.75 |
| 29 | Jimmy Carter | 1924 | 2024 | Politician | United States | 93.90 | 59 | 164 | 4,140,037 | 3.30 |
| 30 | Pope Benedict XVI | 1927 | 2022 | Religious figure | Germany | 93.90 | 499 | 149 | 10,452,618 | 3.85 |
| 31 | Nicolaus Copernicus | 1473 | 1543 | Astronomer | Poland | 93.78 | 28 | 174 | 1,568,538 | 4.16 |
| 32 | Julius Caesar | 100 BC | 44 BC | Politician | Italy | 93.78 | 29 | 215 | 2,846,870 | 6.13 |
| 33 | Confucius | 551 BC | 479 BC | Philosopher | China | 93.57 | 33 | 234 | 1,193,478 | 5.60 |
| 34 | Michelangelo | 1475 | 1564 | Painter | Italy | 93.54 | 30 | 210 | 2,085,973 | 5.38 |
| 35 | Archimedes | 287 BC | 212 BC | Mathematician | Italy | 93.41 | 43 | 189 | 1,066,245 | 4.71 |
| 36 | Pythagoras | 570 BC | 495 BC | Philosopher | Greece | 93.36 | 26 | 158 | 1,219,084 | 3.87 |
| 37 | Vincent van Gogh | 1853 | 1890 | Painter | Netherlands | 93.26 | 27 | 211 | 2,713,578 | 5.05 |
| 38 | Moses | 1393 BC | 1273 BC | Religious figure | Egypt | 93.26 | 19 | 160 | 1,773,663 | 4.39 |
| 39 | Fyodor Dostoevsky | 1821 | 1881 | Writer | Russia | 93.20 | 77 | 178 | 2,124,272 | 4.14 |
| 40 | Thomas Jefferson | 1743 | 1826 | Politician | United States | 93.18 | 47 | 159 | 822,449 | 2.98 |
| 41 | Che Guevara | 1928 | 1967 | Social activist | Argentina | 93.09 | 31 | 169 | 2,476,508 | 3.30 |
| 42 | Louis XIV of France | 1638 | 1715 | Politician | France | 93.01 | 35 | 141 | 2,324,963 | 3.69 |
| 43 | Adam Smith | 1723 | 1790 | Economist | United Kingdom | 92.99 | 34 | 162 | 629,020 | 3.22 |
| 44 | Mother Teresa | 1910 | 1997 | Social activist | North Macedonia | 92.98 | 436 | 144 | 1,476,875 | 2.86 |
| 45 | Johann Sebastian Bach | 1685 | 1750 | Composer | Germany | 92.78 | 24 | 217 | 2,364,783 | 5.76 |
| 46 | Martin Luther | 1483 | 1546 | Religious figure | Germany | 92.77 | 32 | 187 | 1,728,947 | 5.19 |
| 47 | Ferdinand Magellan | 1480 | 1521 | Explorer | Portugal | 92.62 | 25 | 176 | 1,101,452 | 4.51 |
| 48 | William Shakespeare | 1564 | 1616 | Writer | United Kingdom | 92.59 | 49 | 230 | 2,317,463 | 7.12 |
| 49 | Pope John Paul II | 1920 | 2005 | Religious figure | Poland | 92.56 | 153 | 146 | 10,198,483 | 4.23 |
| 50 | Martin Luther King Jr. | 1929 | 1968 | Social activist | United States | 92.49 | 937 | 178 | 2,145,984 | 3.73 |
| 51 | Frédéric Chopin | 1810 | 1849 | Composer | Poland | 92.48 | 52 | 163 | 1,278,363 | 3.41 |
| 52 | Immanuel Kant | 1724 | 1804 | Philosopher | Russia | 92.35 | 44 | 178 | 1,360,909 | 4.32 |
| 53 | Karl Marx | 1818 | 1883 | Economist | Germany | 92.24 | 40 | 206 | 2,206,657 | 5.52 |
| 54 | Joseph Stalin | 1879 | 1953 | Politician | Georgia | 92.22 | 45 | 202 | 4,398,791 | 5.75 |
| 55 | Akbar | 1542 | 1605 | Politician | Pakistan | 92.19 | 552 | 153 | 436,563 | 3.42 |
| 56 | Dante Alighieri | 1265 | 1321 | Writer | Italy | 92.13 | 46 | 192 | 1,169,648 | 4.95 |
| 57 | René Descartes | 1596 | 1650 | Philosopher | France | 92.12 | 41 | 178 | 1,146,776 | 4.59 |
| 58 | Avicenna | 980 | 1037 | Philosopher | Uzbekistan | 92.05 | 48 | 157 | 1,417,942 | 3.97 |
| 59 | Augustus | 63 BC | 14 | Politician | Italy | 92.03 | 60 | 206 | 1,841,935 | 6.12 |
| 60 | Gottfried Wilhelm Leibniz | 1646 | 1716 | Mathematician | Germany | 92.00 | 155 | 156 | 520,030 | 3.26 |
| 61 | Nikola Tesla | 1856 | 1943 | Inventor | Croatia | 91.90 | 39 | 169 | 2,903,743 | 4.86 |
| 62 | Laozi | 604 BC | 600 BC | Philosopher | China | 91.85 | 455 | 149 | 484,300 | 3.16 |
| 63 | Charles III | 1948 | – | Nobleman | United Kingdom | 91.70 | 870 | 156 | 3,486,442 | 3.30 |
| 64 | Pablo Picasso | 1881 | 1973 | Painter | Spain | 91.68 | 55 | 204 | 2,196,154 | 5.29 |
| 65 | Thomas Edison | 1847 | 1931 | Inventor | United States | 91.65 | 54 | 189 | 1,666,698 | 5.10 |
| 66 | Suleiman the Magnificent | 1494 | 1566 | Politician | Türkiye | 91.58 | 38 | 131 | 1,952,126 | 3.47 |
| 67 | Indira Gandhi | 1917 | 1984 | Politician | India | 91.54 | 1,264 | 129 | 761,386 | 2.35 |
| 68 | Vladimir Lenin | 1870 | 1924 | Politician | Russia | 91.51 | 57 | 209 | 2,821,509 | 5.70 |
| 69 | Charles Darwin | 1809 | 1882 | Biologist | United Kingdom | 91.48 | 53 | 205 | 1,470,062 | 5.44 |
| 70 | Carl Friedrich Gauss | 1777 | 1855 | Mathematician | Germany | 91.44 | 78 | 160 | 593,007 | 3.24 |
| 71 | Saladin | 1138 | 1193 | Politician | Iraq | 91.36 | 51 | 141 | 1,962,054 | 4.35 |
| 72 | Paul the Apostle | 5 | 66 | Religious figure | Türkiye | 91.31 | 58 | 150 | 1,595,104 | 4.73 |
| 73 | Jean-Jacques Rousseau | 1712 | 1778 | Philosopher | Switzerland | 91.27 | 63 | 157 | 1,083,180 | 4.01 |
| 74 | Mustafa Kemal Atatürk | 1881 | 1938 | Politician | Greece | 91.26 | 64 | 205 | 2,044,380 | 5.18 |
| 75 | Kublai Khan | 1215 | 1294 | Politician | China | 91.15 | 738 | 101 | 692,771 | 2.42 |
| 76 | Sigmund Freud | 1856 | 1939 | Psychologist | Czechia | 91.09 | 83 | 188 | 1,951,355 | 5.08 |
| 77 | Vasco da Gama | 1460 | 1524 | Explorer | Portugal | 91.06 | 50 | 167 | 778,821 | 4.67 |
| 78 | Blaise Pascal | 1623 | 1662 | Mathematician | France | 91.04 | 71 | 136 | 667,804 | 3.34 |
| 79 | Joan of Arc | 1412 | 1431 | Military personnel | France | 91.02 | 80 | 154 | 2,150,982 | 5.04 |
| 80 | Antonio Vivaldi | 1678 | 1741 | Composer | Italy | 91.00 | 74 | 147 | 886,226 | 3.69 |
| 81 | Raphael | 1483 | 1520 | Painter | Italy | 90.99 | 72 | 169 | 773,466 | 4.55 |
| 82 | Qin Shi Huang | 258 BC | 210 BC | Politician | China | 90.99 | 158 | 181 | 1,086,683 | 4.87 |
| 83 | Johann Wolfgang von Goethe | 1749 | 1832 | Writer | Germany | 90.96 | 65 | 188 | 1,142,818 | 4.89 |
| 84 | J. Robert Oppenheimer | 1904 | 1967 | Physicist | United States | 90.85 | 429 | 101 | 3,673,331 | 2.82 |
| 85 | Saint Joseph | 18 BC | 33 | Religious figure | Israel | 90.76 | 90 | 88 | 969,063 | 2.43 |
| 86 | Timur | 1336 | 1405 | Military personnel | Uzbekistan | 90.74 | 69 | 139 | 1,575,136 | 4.31 |
| 87 | Muhammad Ali | 1942 | 2016 | Boxer | United States | 90.72 | 56 | 139 | 1,826,586 | 3.08 |
| 88 | George VI | 1895 | 1952 | Politician | United Kingdom | 90.71 | 1,059 | 108 | 1,875,371 | 2.62 |
| 89 | J. R. R. Tolkien | 1892 | 1973 | Writer | South Africa | 90.69 | 82 | 156 | 1,403,495 | 3.52 |
| 90 | Franz Joseph I | 1830 | 1916 | Politician | Austria | 90.65 | 386 | 84 | 3,679,563 | 2.60 |
| 91 | Baruch Spinoza | 1632 | 1677 | Philosopher | Netherlands | 90.63 | 333 | 117 | 803,286 | 2.90 |
| 92 | Muhammad ibn Musa al-Khwarizmi | 780 | 850 | Mathematician | Turkmenistan | 90.62 | 109 | 148 | 793,489 | 3.80 |
| 93 | Rembrandt | 1606 | 1669 | Painter | Netherlands | 90.59 | 79 | 175 | 672,488 | 4.61 |
| 94 | Johannes Gutenberg | 1394 | 1468 | Inventor | Germany | 90.58 | 81 | 160 | 585,424 | 4.30 |
| 95 | Louis XVI of France | 1754 | 1793 | Politician | France | 90.50 | 123 | 109 | 1,695,704 | 3.17 |
| 96 | Nelson Mandela | 1918 | 2013 | Social activist | South Africa | 90.45 | 68 | 230 | 2,217,739 | 6.38 |
| 97 | Niccolò Machiavelli | 1469 | 1527 | Philosopher | Italy | 90.45 | 87 | 151 | 1,098,037 | 4.71 |
| 98 | Andrew Jackson | 1767 | 1845 | Politician | United States | 90.45 | 114 | 136 | 441,023 | 2.71 |
| 99 | Augustine of Hippo | 354 | 430 | Philosopher | Algeria | 90.39 | 94 | 157 | 1,778,823 | 4.87 |
| 100 | Edgar Allan Poe | 1809 | 1849 | Writer | United States | 90.35 | 70 | 148 | 1,071,091 | 3.72 |
| 101 | Francis Bacon | 1561 | 1626 | Philosopher | United Kingdom | 90.32 | 111 | 116 | 491,991 | 2.88 |
| 102 | Hippocrates | 460 BC | 370 BC | Physician | Greece | 90.19 | 88 | 121 | 581,740 | 3.36 |
| 103 | Friedrich Nietzsche | 1844 | 1900 | Philosopher | Germany | 90.17 | 92 | 174 | 1,829,924 | 5.02 |
| 104 | Carl Linnaeus | 1707 | 1778 | Biologist | Sweden | 90.16 | 85 | 182 | 578,868 | 4.80 |
| 105 | Hans Christian Andersen | 1805 | 1875 | Writer | Denmark | 90.14 | 96 | 180 | 987,100 | 4.68 |
| 106 | Herodotus | 484 BC | 425 BC | Historian | Türkiye | 90.06 | 73 | 143 | 610,129 | 4.18 |
| 107 | Vladimir Putin | 1952 | – | Politician | Russia | 90.03 | 116 | 229 | 6,744,940 | 6.06 |
| 108 | Euclid | 350 BC | 240 BC | Mathematician | Egypt | 90.02 | 120 | 166 | 470,244 | 4.57 |
| 109 | Abraham | 1813 BC | 1638 BC | Religious figure | Iraq | 89.99 | 23 | 170 | 1,570,446 | 4.52 |
| 110 | Salvador Dalí | 1904 | 1989 | Painter | Spain | 89.93 | 101 | 201 | 1,335,098 | 5.07 |
| 111 | Charles I of England | 1600 | 1649 | Politician | United Kingdom | 89.90 | 1,746 | 93 | 763,304 | 2.45 |
| 112 | Charlie Chaplin | 1889 | 1977 | Actor | United Kingdom | 89.85 | 105 | 197 | 2,183,221 | 5.91 |
| 113 | Charlemagne | 748 | 814 | Politician | Germany | 89.85 | 15 | 161 | 1,751,329 | 5.65 |
| 114 | George V | 1865 | 1936 | Politician | United Kingdom | 89.85 | 1,516 | 98 | 1,474,359 | 2.53 |
| 115 | James VI and I | 1566 | 1625 | Politician | United Kingdom | 89.83 | 2,155 | 86 | 941,512 | 2.43 |
| 116 | Leo Tolstoy | 1828 | 1910 | Writer | Russia | 89.82 | 98 | 183 | 1,717,518 | 5.35 |
| 117 | Pope John Paul I | 1912 | 1978 | Religious figure | Italy | 89.80 | 417 | 110 | 5,870,712 | 3.57 |
| 118 | Commodus | 161 | 192 | Politician | Italy | 89.79 | 104 | 79 | 1,318,723 | 2.47 |
| 119 | Fibonacci | 1170 | 1240 | Mathematician | Italy | 89.74 | 518 | 115 | 352,144 | 2.73 |
| 120 | Elizabeth II | 1926 | 2022 | Nobleman | United Kingdom | 89.72 | 84 | 208 | 4,338,557 | 6.94 |
| 121 | Edward VII | 1841 | 1910 | Nobleman | United Kingdom | 89.68 | 1,852 | 96 | 1,185,747 | 2.42 |
| 122 | Edward VI of England | 1537 | 1553 | Politician | United Kingdom | 89.67 | 1,157 | 83 | 734,369 | 2.29 |
| 123 | Franz Kafka | 1883 | 1924 | Writer | Czechia | 89.62 | 125 | 171 | 1,773,701 | 5.03 |
| 124 | Empress Elisabeth of Austria | 1837 | 1898 | Companion | Germany | 89.61 | 184 | 72 | 6,431,011 | 2.88 |
| 125 | Victor Hugo | 1802 | 1885 | Writer | France | 89.52 | 103 | 179 | 1,353,705 | 5.17 |
| 126 | Albrecht Dürer | 1471 | 1528 | Painter | Germany | 89.52 | 137 | 158 | 500,569 | 4.38 |
| 127 | Pope Leo XIV | 1955 | – | Religious figure | United States | 89.52 | 118,563 | 143 | 12,696,097 | 1.16 |
| 128 | Mehmed the Conqueror | 1432 | 1481 | Politician | Türkiye | 89.49 | 273 | 106 | 2,008,617 | 4.07 |
| 129 | Voltaire | 1694 | 1778 | Writer | France | 89.44 | 95 | 174 | 960,379 | 5.18 |
| 130 | Huang Xianfan | 1899 | 1982 | Politician | China | 89.40 | 131 | 170 | 43,386 | 2.51 |
| 131 | Solomon | 1011 BC | 931 BC | Religious figure | NA | 89.40 | 76 | 107 | 1,378,046 | 3.88 |
| 132 | Pyotr Ilyich Tchaikovsky | 1840 | 1893 | Composer | Russia | 89.39 | 271 | 155 | 1,357,097 | 4.69 |
| 133 | James Joyce | 1882 | 1941 | Writer | Ireland | 89.38 | 855 | 155 | 390,314 | 3.13 |
| 134 | Sophocles | 497 BC | 406 BC | Writer | Greece | 89.32 | 110 | 148 | 345,565 | 4.06 |
| 135 | Ali | 601 | 661 | Religious figure | Saudi Arabia | 89.31 | 252 | 122 | 1,668,658 | 4.42 |
| 136 | William McKinley | 1843 | 1901 | Politician | United States | 89.29 | 4,636 | 124 | 764,881 | 2.90 |
| 137 | Giuseppe Verdi | 1813 | 1901 | Composer | Italy | 89.28 | 102 | 147 | 631,032 | 3.63 |
| 138 | Umar | 585 | 644 | Politician | Saudi Arabia | 89.27 | 148 | 135 | 1,259,774 | 4.59 |
| 139 | Al Pacino | 1940 | – | Actor | United States | 89.27 | 397 | 122 | 2,021,209 | 3.08 |
| 140 | Louis Pasteur | 1822 | 1895 | Chemist | France | 89.24 | 112 | 164 | 726,591 | 4.37 |
| 141 | Johannes Kepler | 1571 | 1630 | Astronomer | Germany | 89.24 | 117 | 149 | 477,640 | 4.26 |
| 142 | Edward VIII | 1894 | 1972 | Politician | United Kingdom | 89.23 | 1,720 | 96 | 1,387,680 | 2.48 |
| 143 | Sylvester Stallone | 1946 | – | Actor | United States | 89.20 | 93 | 107 | 2,641,496 | 2.85 |
| 144 | Clint Eastwood | 1930 | – | Actor | United States | 89.20 | 511 | 108 | 3,020,273 | 3.06 |
| 145 | Ulysses S. Grant | 1822 | 1885 | Politician | United States | 89.19 | 173 | 135 | 418,216 | 2.89 |
| 146 | Frida Kahlo | 1907 | 1954 | Painter | Mexico | 89.13 | 167 | 166 | 2,728,542 | 4.83 |
| 147 | George III | 1738 | 1820 | Nobleman | United Kingdom | 89.11 | 1,009 | 92 | 955,869 | 2.55 |
| 148 | Kim Il-sung | 1912 | 1994 | Politician | South Korea | 89.10 | 301 | 139 | 973,202 | 3.23 |
| 149 | Andrew the Apostle | 6 BC | 70 | Religious figure | NA | 89.10 | 220 | 93 | 491,856 | 2.63 |
| 150 | Abu Bakr | 573 | 634 | Religious figure | Saudi Arabia | 89.08 | 334 | 110 | 977,586 | 3.72 |
| 151 | John the Baptist | 20 BC | 31 | Religious figure | Israel | 89.07 | 97 | 112 | 1,104,002 | 4.13 |
| 152 | Thales of Miletus | 623 BC | 546 BC | Philosopher | Türkiye | 89.06 | 100 | 115 | 714,227 | 3.74 |
| 153 | Heraclitus | 535 BC | 470 BC | Philosopher | Türkiye | 89.05 | 99 | 95 | 466,257 | 2.63 |
| 154 | Constantine the Great | 272 | 337 | Politician | Serbia | 89.00 | 135 | 134 | 1,138,173 | 4.94 |
| 155 | David | 1010 BC | 970 BC | Politician | NA | 88.96 | 86 | 108 | 1,593,834 | 4.27 |
| 156 | George Frideric Handel | 1685 | 1759 | Composer | Germany | 88.95 | 174 | 135 | 619,385 | 3.89 |
| 157 | Lady Jane Grey | 1537 | 1554 | Nobleman | United Kingdom | 88.92 | 3,869 | 77 | 663,007 | 2.16 |
| 158 | Martin Van Buren | 1782 | 1862 | Politician | United States | 88.89 | 172 | 130 | 242,995 | 2.65 |
| 159 | Alfred Nobel | 1833 | 1896 | Chemist | Sweden | 88.86 | 107 | 159 | 612,488 | 4.30 |
| 160 | Steve Jobs | 1955 | 2011 | Designer | United States | 88.84 | 108 | 168 | 2,483,741 | 3.36 |
| 161 | Tutankhamun | 1341 BC | 1323 BC | Religious figure | Egypt | 88.82 | 118 | 109 | 1,174,341 | 4.05 |
| 162 | Joseph Goebbels | 1897 | 1945 | Politician | Germany | 88.81 | 776 | 103 | 1,704,093 | 2.91 |
| 163 | Narendra Modi | 1950 | – | Politician | India | 88.81 | 263 | 145 | 899,110 | 2.89 |
| 164 | Hillary Clinton | 1947 | – | Politician | United States | 88.79 | 163 | 143 | 705,150 | 2.82 |
| 165 | Winston Churchill | 1874 | 1965 | Politician | United Kingdom | 88.76 | 141 | 180 | 2,720,756 | 6.46 |
| 166 | Thomas Aquinas | 1225 | 1274 | Philosopher | Italy | 88.70 | 121 | 158 | 921,097 | 5.27 |
| 167 | Mao Zedong | 1893 | 1976 | Politician | China | 88.70 | 129 | 181 | 2,337,537 | 5.85 |
| 168 | Claude Monet | 1840 | 1926 | Painter | France | 88.69 | 128 | 131 | 1,054,375 | 3.73 |
| 169 | Otto von Bismarck | 1815 | 1898 | Politician | Germany | 88.67 | 113 | 155 | 1,210,848 | 4.78 |
| 170 | Charles II of England | 1630 | 1685 | Politician | United Kingdom | 88.62 | 2,846 | 84 | 576,739 | 2.29 |
| 171 | Giordano Bruno | 1548 | 1600 | Astronomer | Italy | 88.57 | 132 | 111 | 664,079 | 3.33 |
| 172 | Marilyn Monroe | 1926 | 1962 | Actor | United States | 88.57 | 122 | 195 | 2,626,920 | 6.30 |
| 173 | Pope Leo XIII | 1810 | 1903 | Religious figure | Italy | 88.51 | 520 | 92 | 4,794,006 | 3.54 |
| 174 | James Watt | 1736 | 1819 | Inventor | United Kingdom | 88.47 | 147 | 143 | 312,990 | 3.99 |
| 175 | "Wilhelm II, German Emperor" | 1859 | 1941 | Politician | Germany | 88.47 | 370 | 107 | 1,194,427 | 3.09 |
| 176 | Aaron | 1396 BC | 1274 BC | Religious figure | Jordan | 88.47 | 150 | 86 | 300,465 | 2.11 |
| 177 | Diogenes | 404 BC | 322 BC | Philosopher | Türkiye | 88.38 | 321 | 84 | 655,445 | 2.56 |
| 178 | Jacob | 1653 BC | 1506 BC | Religious figure | NA | 88.37 | 119 | 95 | 872,749 | 3.36 |
| 179 | "Anne, Queen of Great Britain" | 1665 | 1714 | Politician | United Kingdom | 88.37 | 1,781 | 86 | 633,651 | 2.45 |
| 180 | Benito Mussolini | 1883 | 1945 | Politician | Italy | 88.36 | 124 | 153 | 3,173,196 | 5.39 |
| 181 | Stephen Hawking | 1942 | 2018 | Physicist | United Kingdom | 88.36 | 239 | 151 | 2,718,891 | 5.06 |
| 182 | Erasmus | 1466 | 1536 | Philosopher | Netherlands | 88.33 | 307 | 101 | 467,862 | 2.81 |
| 183 | Jules Verne | 1828 | 1905 | Writer | France | 88.32 | 140 | 125 | 967,766 | 3.62 |
| 184 | Matthew the Apostle | 10 | 74 | Religious figure | Israel | 88.31 | 319 | 90 | 468,599 | 2.65 |
| 185 | Joseph Haydn | 1732 | 1809 | Composer | Austria | 88.30 | 165 | 130 | 538,517 | 3.73 |
| 186 | "John, King of England" | 1166 | 1216 | Politician | United Kingdom | 88.29 | 2,149 | 85 | 534,571 | 2.39 |
| 187 | Peter Paul Rubens | 1577 | 1640 | Painter | Germany | 88.29 | 162 | 150 | 416,443 | 4.26 |
| 188 | Georg Wilhelm Friedrich Hegel | 1770 | 1831 | Philosopher | Germany | 88.27 | 139 | 137 | 688,995 | 4.13 |
| 189 | Leif Erikson | 970 | 1020 | Explorer | Iceland | 88.25 | 1,693 | 100 | 288,215 | 2.56 |
| 190 | Cicero | 106 BC | 43 BC | Politician | Italy | 88.19 | 130 | 131 | 842,502 | 4.58 |
| 191 | Saint Nicholas | 270 | 342 | Religious figure | Türkiye | 88.17 | 106 | 97 | 1,441,928 | 3.94 |
| 192 | Richard Wagner | 1813 | 1883 | Composer | Germany | 88.15 | 151 | 158 | 827,762 | 4.67 |
| 193 | Karl Benz | 1844 | 1929 | Inventor | Germany | 88.12 | 512 | 110 | 315,808 | 2.51 |
| 194 | Richard III of England | 1452 | 1485 | Politician | United Kingdom | 88.10 | 152 | 78 | 662,166 | 2.43 |
| 195 | Aisha | 605 | 678 | Companion | Saudi Arabia | 88.09 | 548 | 96 | 844,754 | 3.29 |
| 196 | Virgil | 70 BC | 19 BC | Writer | Italy | 88.05 | 159 | 172 | 560,925 | 5.45 |
| 197 | Pope Paul VI | 1897 | 1978 | Religious figure | Italy | 88.00 | 794 | 108 | 3,052,217 | 3.62 |
| 198 | Cnut the Great | 995 | 1035 | Politician | Denmark | 87.99 | 1,285 | 74 | 537,795 | 2.16 |
| 199 | Pope John XXIII | 1881 | 1963 | Religious figure | Italy | 87.98 | 504 | 111 | 2,738,931 | 3.69 |
| 200 | Xerxes I | 519 BC | 475 BC | Politician | Iran | 87.97 | 538 | 84 | 575,194 | 2.57 |
| 201 | Nicholas II of Russia | 1868 | 1918 | Politician | Russia | 87.96 | 272 | 110 | 1,887,540 | 3.95 |
| 202 | John Locke | 1632 | 1704 | Philosopher | United Kingdom | 87.94 | 134 | 147 | 681,991 | 5.10 |
| 203 | Pelé | 1940 | 2022 | Soccer player | Brazil | 87.93 | 133 | 145 | 1,824,127 | 4.34 |
| 204 | Saint Anne | 49 BC | 4 | Religious figure | NA | 87.93 | 729 | 69 | 344,697 | 1.82 |
| 205 | Henry Kissinger | 1923 | 2023 | Politician | Germany | 87.92 | 91 | 104 | 777,264 | 2.45 |
| 206 | Abraham Lincoln | 1809 | 1865 | Politician | United States | 87.87 | 154 | 204 | 2,118,601 | 7.84 |
| 207 | Molière | 1622 | 1673 | Writer | France | 87.83 | 187 | 163 | 844,723 | 5.93 |
| 208 | Ada Lovelace | 1815 | 1852 | Mathematician | United Kingdom | 87.83 | 1,677 | 111 | 700,044 | 3.15 |
| 209 | James K. Polk | 1795 | 1849 | Politician | United States | 87.82 | 209 | 129 | 209,077 | 2.74 |
| 210 | William III of England | 1650 | 1702 | Politician | Netherlands | 87.81 | 2,818 | 79 | 510,464 | 2.19 |
| 211 | Franz Schubert | 1797 | 1828 | Composer | Austria | 87.80 | 170 | 137 | 643,051 | 3.92 |
| 212 | Francis of Assisi | 1182 | 1226 | Religious figure | Italy | 87.80 | 183 | 104 | 1,214,077 | 3.96 |
| 213 | James II of England | 1633 | 1701 | Politician | United Kingdom | 87.79 | 3,726 | 78 | 456,192 | 2.18 |
| 214 | Pope Pius XII | 1876 | 1958 | Religious figure | Italy | 87.71 | 568 | 102 | 2,588,967 | 3.42 |
| 215 | Pompey | 106 BC | 48 BC | Politician | Italy | 87.68 | 1,518 | 87 | 404,454 | 2.54 |
| 216 | Darius the Great | 550 BC | 486 BC | Politician | Georgia | 87.66 | 371 | 95 | 536,846 | 3.28 |
| 217 | Steven Spielberg | 1946 | – | Film director | United States | 87.65 | 143 | 143 | 1,696,466 | 3.82 |
| 218 | Mikhail Gorbachev | 1931 | 2022 | Politician | Russia | 87.63 | 177 | 156 | 1,986,974 | 5.21 |
| 219 | Miguel de Cervantes | 1547 | 1616 | Writer | Spain | 87.60 | 138 | 180 | 868,533 | 6.57 |
| 220 | Leonhard Euler | 1707 | 1783 | Mathematician | Switzerland | 87.60 | 175 | 161 | 533,790 | 5.32 |
| 221 | Kim Jong-il | 1941 | 2011 | Politician | Russia | 87.59 | 416 | 117 | 922,018 | 2.94 |
| 222 | Bob Marley | 1945 | 1981 | Musician | Jamaica | 87.58 | 156 | 132 | 1,934,261 | 3.90 |
| 223 | Caravaggio | 1571 | 1610 | Painter | Italy | 87.57 | 186 | 98 | 921,862 | 3.49 |
| 224 | Elvis Presley | 1935 | 1977 | Singer | United States | 87.57 | 243 | 184 | 3,432,481 | 6.64 |
| 225 | Saint George | 280 | 303 | Religious figure | Türkiye | 87.57 | 190 | 88 | 1,008,615 | 3.51 |
| 226 | Pope Pius IX | 1792 | 1878 | Religious figure | Italy | 87.55 | 498 | 95 | 1,598,908 | 3.26 |
| 227 | Arthur Schopenhauer | 1788 | 1860 | Philosopher | Poland | 87.55 | 157 | 106 | 910,988 | 3.39 |
| 228 | Charles V, Holy Roman Emperor | 1500 | 1558 | Politician | Belgium | 87.50 | 181 | 100 | 1,433,890 | 3.91 |
| 229 | Montesquieu | 1689 | 1755 | Philosopher | France | 87.46 | 169 | 104 | 495,668 | 3.16 |
| 230 | Attila | 406 | 453 | Politician | Georgia | 87.44 | 144 | 105 | 957,450 | 4.21 |
| 231 | Maria Theresa | 1717 | 1780 | Politician | Austria | 87.44 | 149 | 91 | 1,041,758 | 3.14 |
| 232 | Marie Antoinette | 1755 | 1793 | Nobleman | Austria | 87.43 | 36 | 101 | 2,781,379 | 4.60 |
| 233 | Francisco Goya | 1746 | 1828 | Painter | Spain | 87.42 | 212 | 158 | 612,402 | 4.85 |
| 234 | Osman I | 1254 | 1327 | Politician | Türkiye | 87.41 | 146 | 97 | 1,194,853 | 3.58 |
| 235 | Marcus Aurelius | 121 | 180 | Politician | Italy | 87.41 | 233 | 112 | 1,993,592 | 5.16 |
| 236 | Maximilien Robespierre | 1758 | 1794 | Politician | France | 87.37 | 679 | 97 | 801,082 | 3.06 |
| 237 | Igor Stravinsky | 1882 | 1971 | Composer | Russia | 87.34 | 691 | 133 | 410,066 | 3.35 |
| 238 | Gustav Mahler | 1860 | 1911 | Composer | Czechia | 87.34 | 269 | 122 | 496,086 | 3.16 |
| 239 | Jean-Paul Sartre | 1905 | 1980 | Writer | France | 87.31 | 211 | 147 | 897,253 | 4.26 |
| 240 | Johannes Vermeer | 1632 | 1675 | Painter | Netherlands | 87.28 | 216 | 107 | 542,947 | 3.36 |
| 241 | Nefertiti | 1400 BC | 1330 BC | Companion | Egypt | 87.28 | 136 | 99 | 641,843 | 3.64 |
| 242 | T. S. Eliot | 1888 | 1965 | Writer | United States | 87.25 | 5,856 | 112 | 225,790 | 2.31 |
| 243 | Sandro Botticelli | 1445 | 1510 | Painter | Italy | 87.24 | 257 | 101 | 448,160 | 3.17 |
| 244 | Mansa Musa | 1280 | 1337 | Politician | Mali | 87.24 | 2,304 | 70 | 396,575 | 1.96 |
| 245 | Max Weber | 1864 | 1920 | Sociologist | Germany | 87.20 | 164 | 136 | 578,983 | 3.79 |
| 246 | Yuri Gagarin | 1934 | 1968 | Astronaut | Russia | 87.19 | 161 | 171 | 1,478,164 | 5.41 |
| 247 | Hafez al-Assad | 1930 | 2000 | Politician | Syria | 87.19 | 2,178 | 85 | 2,886,957 | 3.01 |
| 248 | Nero | 37 | 68 | Politician | Italy | 87.19 | 185 | 111 | 1,282,294 | 4.81 |
| 249 | Edvard Munch | 1863 | 1944 | Painter | Norway | 87.17 | 142 | 102 | 532,518 | 2.73 |
| 250 | Wilhelm Röntgen | 1845 | 1923 | Physicist | Germany | 87.15 | 182 | 139 | 293,230 | 3.65 |
| 251 | Jack the Ripper | 1850 | – | Extremist | NA | 87.14 | 202 | 81 | 1,582,985 | 2.53 |
| 252 | Giuseppe Garibaldi | 1807 | 1882 | Politician | France | 87.09 | 291 | 110 | 1,250,926 | 3.76 |
| 253 | Ptolemy | 100 | 170 | Astronomer | Egypt | 87.07 | 145 | 118 | 443,806 | 4.17 |
| 254 | Francis II, Holy Roman Emperor | 1768 | 1835 | Politician | Italy | 87.05 | 259 | 78 | 637,946 | 2.29 |
| 255 | Henry VI of England | 1421 | 1471 | Politician | United Kingdom | 87.03 | 1,865 | 70 | 427,387 | 2.10 |
| 256 | Freddie Mercury | 1946 | 1991 | Musician | Tanzania | 87.00 | 192 | 147 | 3,481,800 | 5.46 |
| 257 | Diego Velázquez | 1599 | 1660 | Painter | Spain | 86.97 | 283 | 152 | 382,027 | 4.66 |
| 258 | Louis XV of France | 1710 | 1774 | Politician | France | 86.93 | 176 | 93 | 1,241,031 | 3.61 |
| 259 | Dmitri Mendeleev | 1834 | 1907 | Chemist | Russia | 86.92 | 188 | 154 | 631,019 | 4.80 |
| 260 | Antoni Gaudí | 1852 | 1926 | Architect | Spain | 86.92 | 191 | 116 | 894,099 | 3.60 |
| 261 | William IV of the United Kingdom | 1765 | 1837 | Politician | United Kingdom | 86.91 | 203 | 87 | 505,880 | 2.48 |
| 262 | Edward IV of England | 1442 | 1483 | Politician | France | 86.91 | 1,447 | 74 | 370,184 | 2.26 |
| 263 | Cyrus the Great | 600 BC | 530 BC | Politician | Iran | 86.91 | 452 | 131 | 1,103,395 | 5.79 |
| 264 | Peter the Great | 1672 | 1725 | Politician | Russia | 86.89 | 205 | 151 | 1,584,919 | 6.04 |
| 265 | Muhammad Ali Jinnah | 1876 | 1948 | Politician | Pakistan | 86.88 | 7,675 | 99 | 260,923 | 2.15 |
| 266 | Ovid | 43 BC | 17 | Writer | Italy | 86.87 | 214 | 134 | 335,145 | 4.31 |
| 267 | Democritus | 460 BC | 360 BC | Philosopher | Greece | 86.85 | 180 | 102 | 346,775 | 3.26 |
| 268 | Le Corbusier | 1887 | 1965 | Architect | Switzerland | 86.85 | 224 | 169 | 549,192 | 4.44 |
| 269 | Haile Selassie | 1892 | 1975 | Politician | Ethiopia | 86.85 | 2,557 | 102 | 567,897 | 2.60 |
| 270 | Hammurabi | 1810 BC | 1750 BC | Politician | Iraq | 86.84 | 127 | 109 | 301,626 | 3.66 |
| 271 | Alexandre Dumas | 1802 | 1870 | Writer | France | 86.83 | 332 | 115 | 1,253,927 | 3.97 |
| 272 | James, son of Zebedee | 1 | 44 | Religious figure | NA | 86.83 | 556 | 88 | 469,801 | 3.13 |
| 273 | Elon Musk | 1971 | – | Inventor | South Africa | 86.81 | 303 | 153 | 17,144,804 | 3.38 |
| 274 | Seneca the Younger | 4 BC | 65 | Philosopher | Spain | 86.81 | 231 | 97 | 686,850 | 3.51 |
| 275 | Albert Camus | 1913 | 1960 | Writer | Algeria | 86.77 | 178 | 139 | 1,225,399 | 4.47 |
| 276 | Ibn Khaldun | 1332 | 1406 | Historian | Tunisia | 86.74 | 277 | 134 | 431,092 | 4.34 |
| 277 | Hesiod | 800 BC | 700 BC | Writer | Türkiye | 86.72 | 647 | 88 | 209,007 | 2.43 |
| 278 | Charles de Gaulle | 1890 | 1970 | Military personnel | France | 86.70 | 199 | 169 | 1,414,445 | 5.61 |
| 279 | Omar Khayyam | 1048 | 1131 | Mathematician | Iran | 86.69 | 204 | 115 | 722,982 | 4.22 |
| 280 | Margrethe II of Denmark | 1940 | – | Nobleman | Denmark | 86.69 | 328 | 100 | 524,273 | 2.30 |
| 281 | Anton Chekhov | 1860 | 1904 | Writer | Russia | 86.67 | 196 | 168 | 1,058,463 | 5.74 |
| 282 | Pope Pius XI | 1857 | 1939 | Religious figure | Italy | 86.66 | 743 | 101 | 1,402,048 | 3.35 |
| 283 | Epicurus | 341 BC | 269 BC | Philosopher | Greece | 86.65 | 193 | 95 | 419,680 | 3.19 |
| 284 | Ho Chi Minh | 1890 | 1969 | Politician | Vietnam | 86.64 | 677 | 126 | 1,292,151 | 4.44 |
| 285 | Nostradamus | 1503 | 1566 | Occultist | France | 86.64 | 292 | 101 | 932,509 | 4.06 |
| 286 | Rumi | 1207 | 1273 | Writer | Afghanistan | 86.64 | 215 | 109 | 940,861 | 4.31 |
| 287 | Isaac | 1900 BC | 1533 BC | Religious figure | Israel | 86.63 | 225 | 93 | 489,377 | 3.35 |
| 288 | Ramesses II | 1303 BC | 1213 BC | Nobleman | Israel | 86.63 | 229 | 95 | 883,590 | 4.02 |
| 289 | Ögedei Khan | 1185 | 1241 | Politician | NA | 86.62 | 1,291 | 80 | 305,275 | 2.36 |
| 290 | Hannibal | 247 BC | 183 BC | Politician | Tunisia | 86.62 | 223 | 114 | 932,175 | 4.88 |
| 291 | Catherine the Great | 1729 | 1796 | Nobleman | Poland | 86.60 | 226 | 119 | 2,306,668 | 5.17 |
| 292 | Petrarch | 1304 | 1374 | Writer | Italy | 86.60 | 200 | 109 | 420,393 | 3.63 |
| 293 | Grace Kelly | 1929 | 1982 | Actor | United States | 86.59 | 236 | 101 | 1,162,902 | 2.87 |
| 294 | Solon | 638 BC | 558 BC | Politician | Greece | 86.59 | 1,051 | 78 | 202,882 | 2.17 |
| 295 | Khufu | 2700 BC | 2570 BC | Architect | Egypt | 86.57 | 1,263 | 77 | 246,146 | 2.12 |
| 296 | George IV | 1762 | 1830 | Politician | United Kingdom | 86.56 | 1,933 | 82 | 564,896 | 2.48 |
| 297 | Khadija bint Khuwaylid | 556 | 619 | Companion | Saudi Arabia | 86.56 | 592 | 89 | 526,603 | 3.12 |
| 298 | Amerigo Vespucci | 1454 | 1512 | Explorer | Italy | 86.55 | 210 | 105 | 617,000 | 3.95 |
| 299 | Richard I of England | 1157 | 1199 | Politician | United Kingdom | 86.55 | 242 | 97 | 960,137 | 4.08 |
| 300 | Josip Broz Tito | 1892 | 1980 | Politician | Croatia | 86.53 | 194 | 110 | 985,161 | 3.76 |
| 301 | Fatimah | 604 | 632 | Companion | Saudi Arabia | 86.48 | 208 | 92 | 750,704 | 3.61 |
| 302 | Malcolm X | 1925 | 1965 | Social activist | United States | 86.43 | 221 | 97 | 1,036,431 | 2.80 |
| 303 | Honoré de Balzac | 1799 | 1850 | Writer | France | 86.38 | 206 | 112 | 657,074 | 3.70 |
| 304 | Vlad the Impaler | 1431 | 1476 | Inspiration | Romania | 86.37 | 262 | 82 | 1,521,558 | 4.03 |
| 305 | Pericles | 494 BC | 429 BC | Politician | Greece | 86.36 | 179 | 94 | 415,194 | 3.30 |
| 306 | Anne Boleyn | 1501 | 1536 | Companion | United Kingdom | 86.36 | 362 | 90 | 1,859,283 | 4.66 |
| 307 | Ronald Reagan | 1911 | 2004 | Politician | United States | 86.36 | 300 | 249 | 2,256,755 | 9.30 |
| 308 | Aesop | 620 BC | 564 BC | Writer | Bulgaria | 86.32 | 207 | 102 | 340,286 | 3.66 |
| 309 | Queen Victoria | 1819 | 1901 | Politician | United Kingdom | 86.29 | 237 | 146 | 2,347,790 | 6.56 |
| 310 | Mary II of England | 1662 | 1694 | Politician | United Kingdom | 86.29 | 318 | 76 | 217,032 | 1.99 |
| 311 | Geta | 189 | 211 | Politician | Italy | 86.28 | 3,226 | 64 | 878,955 | 2.46 |
| 312 | Caligula | 12 | 41 | Politician | Italy | 86.28 | 280 | 115 | 1,039,675 | 4.98 |
| 313 | Henri Matisse | 1869 | 1954 | Painter | France | 86.28 | 219 | 151 | 523,340 | 4.42 |
| 314 | Bruce Lee | 1940 | 1973 | Actor | United States | 86.28 | 228 | 128 | 2,132,829 | 4.86 |
| 315 | Chiang Kai-shek | 1887 | 1975 | Military personnel | China | 86.25 | 905 | 123 | 1,188,768 | 4.45 |
| 316 | Leon Trotsky | 1879 | 1940 | Politician | Ukraine | 86.25 | 247 | 136 | 1,385,364 | 4.88 |
| 317 | Antoine de Saint-Exupéry | 1900 | 1944 | Writer | France | 86.21 | 235 | 113 | 906,054 | 3.40 |
| 318 | Gabriel García Márquez | 1927 | 2014 | Writer | Colombia | 86.19 | 453 | 162 | 1,574,369 | 5.49 |
| 319 | Caracalla | 188 | 217 | Politician | France | 86.14 | 818 | 85 | 1,650,642 | 4.12 |
| 320 | Édith Piaf | 1915 | 1963 | Singer | France | 86.11 | 306 | 128 | 933,906 | 3.98 |
| 321 | Eleanor Roosevelt | 1884 | 1962 | Social activist | United States | 86.11 | 268 | 95 | 384,124 | 2.51 |
| 322 | Michael Faraday | 1791 | 1867 | Physicist | United Kingdom | 86.08 | 250 | 151 | 416,907 | 5.20 |
| 323 | Averroes | 1126 | 1198 | Philosopher | Spain | 86.05 | 251 | 109 | 331,236 | 3.59 |
| 324 | Antoine Lavoisier | 1743 | 1794 | Chemist | France | 86.04 | 284 | 108 | 458,197 | 3.55 |
| 325 | George Washington | 1732 | 1799 | Politician | United States | 86.03 | 310 | 210 | 1,441,559 | 8.81 |
| 326 | Pierre-Auguste Renoir | 1841 | 1919 | Painter | France | 86.02 | 698 | 96 | 402,844 | 2.68 |
| 327 | Pope Pius X | 1835 | 1914 | Religious figure | Italy | 86.02 | 880 | 96 | 1,166,155 | 3.28 |
| 328 | John F. Kennedy | 1917 | 1963 | Politician | United States | 86.01 | 246 | 175 | 2,898,677 | 7.41 |
| 329 | Joe Biden | 1942 | – | Politician | United States | 86.00 | 232 | 224 | 3,135,028 | 8.92 |
| 330 | Pope Clement I | 40 | 99 | Religious figure | Italy | 86.00 | 1,221 | 95 | 330,118 | 3.11 |
| 331 | Al-Ghazali | 1058 | 1111 | Philosopher | Iran | 85.99 | 298 | 121 | 436,928 | 3.99 |
| 332 | Giovanni Boccaccio | 1313 | 1375 | Writer | Italy | 85.98 | 248 | 110 | 279,906 | 3.63 |
| 333 | Neil Armstrong | 1930 | 2012 | Astronaut | United States | 85.96 | 253 | 170 | 1,145,287 | 6.01 |
| 334 | Pope Benedict XV | 1854 | 1922 | Religious figure | Italy | 85.96 | 771 | 98 | 1,120,024 | 3.29 |
| 335 | Julian | 331 | 363 | Politician | Türkiye | 85.95 | 1,212 | 81 | 227,701 | 2.37 |
| 336 | Saddam Hussein | 1937 | 2006 | Politician | Iraq | 85.93 | 166 | 133 | 2,373,893 | 5.46 |
| 337 | Akhenaten | 1400 BC | 1336 BC | Politician | Egypt | 85.92 | 198 | 93 | 589,577 | 3.79 |
| 338 | Franklin D. Roosevelt | 1882 | 1945 | Politician | United States | 85.92 | 245 | 180 | 2,437,641 | 7.63 |
| 339 | Benjamin Franklin | 1706 | 1790 | Politician | United States | 85.90 | 260 | 141 | 1,192,305 | 6.11 |
| 340 | Edward V of England | 1470 | 1483 | Politician | United Kingdom | 85.88 | 2,288 | 66 | 203,176 | 1.83 |
| 341 | Fidel Castro | 1926 | 2016 | Politician | Cuba | 85.86 | 254 | 153 | 1,441,030 | 5.59 |
| 342 | Trajan | 53 | 117 | Politician | Spain | 85.85 | 311 | 110 | 607,125 | 4.39 |
| 343 | Mumtaz Mahal | 1593 | 1631 | Companion | India | 85.84 | 5,933 | 66 | 159,681 | 1.70 |
| 344 | Frederick I, Holy Roman Emperor | 1122 | 1190 | Politician | France | 85.83 | 433 | 90 | 521,343 | 3.29 |
| 345 | Selim II | 1524 | 1574 | Politician | Türkiye | 85.83 | 244 | 75 | 933,663 | 3.10 |
| 346 | Agatha Christie | 1890 | 1976 | Writer | United Kingdom | 85.80 | 293 | 141 | 1,286,217 | 5.39 |
| 347 | Eratosthenes | 276 BC | 194 BC | Geographer | Libya | 85.80 | 197 | 101 | 321,512 | 3.58 |
| 348 | Frederick the Great | 1712 | 1786 | Politician | Germany | 85.80 | 240 | 91 | 609,393 | 3.41 |
| 349 | Johannes Brahms | 1833 | 1897 | Composer | Germany | 85.79 | 295 | 129 | 462,054 | 4.00 |
| 350 | Alain Delon | 1935 | 2024 | Actor | France | 85.79 | 217 | 123 | 1,251,342 | 3.96 |
| 351 | John Forbes Nash Jr. | 1928 | 2015 | Mathematician | United States | 85.78 | 1,227 | 95 | 615,337 | 2.61 |
| 352 | Cher | 1946 | – | Singer | United States | 85.78 | 508 | 100 | 1,130,035 | 2.94 |
| 353 | H. G. Wells | 1866 | 1946 | Writer | United Kingdom | 85.76 | 1,665 | 112 | 381,370 | 3.05 |
| 354 | Helena | 250 | 330 | Companion | Türkiye | 85.76 | 762 | 67 | 233,047 | 2.02 |
| 355 | Thomas Hobbes | 1588 | 1679 | Philosopher | United Kingdom | 85.75 | 294 | 108 | 426,187 | 4.14 |
| 356 | Madonna | 1958 | – | Musician | United States | 85.74 | 1,287 | 153 | 1,754,096 | 3.30 |
| 357 | Galen | 129 | 215 | Physician | Türkiye | 85.73 | 285 | 113 | 269,274 | 3.85 |
| 358 | Giacomo Puccini | 1858 | 1924 | Composer | Italy | 85.72 | 327 | 123 | 490,734 | 3.76 |
| 359 | Friedrich Engels | 1820 | 1895 | Philosopher | Germany | 85.72 | 249 | 127 | 532,828 | 4.28 |
| 360 | Francisco Franco | 1892 | 1975 | Politician | Spain | 85.72 | 276 | 117 | 1,487,884 | 4.37 |
| 361 | Elijah | 1000 BC | 900 BC | Religious figure | Israel | 85.72 | 227 | 87 | 513,549 | 3.60 |
| 362 | Ivana Trump | 1949 | 2022 | Businessperson | Czechia | 85.70 | 12,960 | 56 | 2,867,480 | 1.85 |
| 363 | Justinian I | 482 | 565 | Politician | North Macedonia | 85.69 | 189 | 101 | 554,389 | 4.27 |
| 364 | Gregor Mendel | 1822 | 1884 | Biologist | Czechia | 85.69 | 265 | 114 | 603,565 | 3.99 |
| 365 | Antonín Dvořák | 1841 | 1904 | Composer | Czechia | 85.64 | 267 | 128 | 420,733 | 3.97 |
| 366 | Angela Merkel | 1954 | – | Politician | Germany | 85.63 | 380 | 169 | 1,770,401 | 4.57 |
| 367 | Carl Jung | 1875 | 1961 | Psychologist | Switzerland | 85.60 | 484 | 110 | 1,274,418 | 4.35 |
| 368 | Nikita Khrushchev | 1894 | 1971 | Politician | Russia | 85.59 | 258 | 126 | 1,515,763 | 4.88 |
| 369 | Hernán Cortés | 1485 | 1547 | Explorer | Spain | 85.59 | 347 | 145 | 613,307 | 5.54 |
| 370 | Khalil Gibran | 1883 | 1931 | Writer | Lebanon | 85.57 | 2,046 | 105 | 345,390 | 2.82 |
| 371 | Edmond Halley | 1656 | 1742 | Astronomer | United Kingdom | 85.55 | 3,803 | 90 | 67,640 | 1.99 |
| 372 | Pocahontas | 1595 | 1617 | Diplomat | United States | 85.50 | 302 | 61 | 557,407 | 2.12 |
| 373 | Muammar Gaddafi | 1942 | 2011 | Politician | Libya | 85.50 | 218 | 142 | 1,943,440 | 5.56 |
| 374 | Niels Bohr | 1885 | 1962 | Physicist | Denmark | 85.49 | 389 | 141 | 556,296 | 4.63 |
| 375 | Guru Nanak | 1469 | 1539 | Religious figure | Pakistan | 85.46 | 3,017 | 94 | 172,836 | 3.09 |
| 376 | Pope Alexander VI | 1431 | 1503 | Religious figure | Spain | 85.46 | 459 | 90 | 986,672 | 3.86 |
| 377 | Harald V | 1937 | 2026 | Politician | Norway | 85.45 | 288 | 90 | 559,701 | 2.42 |
| 378 | Jeremiah | 650 BC | 586 BC | Religious figure | NA | 85.44 | 1,952 | 58 | 267,507 | 1.82 |
| 379 | Auguste Comte | 1798 | 1857 | Philosopher | France | 85.43 | 278 | 97 | 352,073 | 3.05 |
| 380 | Martin Scorsese | 1942 | – | Film director | United States | 85.42 | 195 | 96 | 1,114,546 | 2.93 |
| 381 | Jean-Auguste-Dominique Ingres | 1780 | 1867 | Painter | France | 85.42 | 593 | 121 | 173,972 | 3.47 |
| 382 | Zoroaster | 2000 BC | 2000 BC | Religious figure | Iran | 85.42 | 341 | 122 | 798,221 | 4.04 |
| 383 | Hans Christian Ørsted | 1777 | 1851 | Physicist | Denmark | 85.42 | 336 | 90 | 88,566 | 2.07 |
| 384 | Max Planck | 1858 | 1947 | Physicist | Germany | 85.41 | 261 | 147 | 368,711 | 4.64 |
| 385 | Leonid Brezhnev | 1906 | 1982 | Politician | Ukraine | 85.38 | 314 | 114 | 1,488,959 | 4.40 |
| 386 | Nebuchadnezzar II | 630 BC | 562 BC | Politician | Iraq | 85.35 | 289 | 89 | 626,729 | 3.83 |
| 387 | Joseph Smith | 1805 | 1844 | Religious figure | United States | 85.34 | 562 | 94 | 514,197 | 3.04 |
| 388 | Alessandro Volta | 1745 | 1827 | Physicist | Italy | 85.34 | 297 | 107 | 269,578 | 3.31 |
| 389 | Rosa Luxemburg | 1871 | 1919 | Social activist | Poland | 85.33 | 405 | 137 | 768,639 | 4.46 |
| 390 | Mark the Evangelist | 10 | 68 | Religious figure | Libya | 85.33 | 418 | 84 | 365,198 | 3.16 |
| 391 | Basil II | 958 | 1025 | Politician | Türkiye | 85.33 | 2,989 | 66 | 181,881 | 1.87 |
| 392 | Brutus the Younger | 85 BC | 42 BC | Politician | Italy | 85.32 | 960 | 63 | 395,396 | 2.28 |
| 393 | Nicolae Ceaușescu | 1918 | 1989 | Politician | Romania | 85.32 | 266 | 99 | 1,456,137 | 3.92 |
| 394 | Bernhard Riemann | 1826 | 1866 | Mathematician | Germany | 85.32 | 469 | 101 | 124,476 | 2.32 |
| 395 | Paul Cézanne | 1839 | 1906 | Painter | France | 85.32 | 234 | 112 | 408,894 | 3.55 |
| 396 | Anne Frank | 1929 | 1945 | Writer | Germany | 85.31 | 335 | 127 | 1,832,576 | 5.06 |
| 397 | Alexander Graham Bell | 1847 | 1922 | Inventor | United Kingdom | 85.31 | 400 | 128 | 633,322 | 4.96 |
| 398 | George Orwell | 1903 | 1950 | Writer | India | 85.28 | 454 | 145 | 1,071,507 | 5.49 |
| 399 | Sigismund, Holy Roman Emperor | 1368 | 1437 | Politician | Germany | 85.25 | 1,210 | 66 | 803,167 | 2.74 |
| 400 | Coco Chanel | 1883 | 1971 | Fashion designer | France | 85.25 | 527 | 89 | 1,240,698 | 3.45 |
| 401 | Hirohito | 1901 | 1989 | Politician | Japan | 85.25 | 313 | 135 | 1,414,378 | 5.13 |
| 402 | John Calvin | 1509 | 1564 | Religious figure | France | 85.23 | 230 | 111 | 416,869 | 4.44 |
| 403 | Mary I of England | 1516 | 1558 | Politician | United Kingdom | 85.22 | 428 | 89 | 1,366,943 | 4.69 |
| 404 | Charles Dickens | 1812 | 1870 | Writer | United Kingdom | 85.20 | 351 | 169 | 1,004,820 | 6.79 |
| 405 | Ötzi | 3345 BC | 3255 BC | Celebrity | Italy | 85.20 | 601 | 67 | 454,708 | 2.58 |
| 406 | Louis XIII of France | 1601 | 1643 | Politician | France | 85.19 | 447 | 84 | 660,663 | 3.51 |
| 407 | Grigori Rasputin | 1869 | 1916 | Occultist | Russia | 85.15 | 340 | 93 | 1,681,480 | 4.11 |
| 408 | Paul Gauguin | 1848 | 1903 | Painter | France | 85.15 | 312 | 111 | 531,032 | 3.79 |
| 409 | Matsuo Bashō | 1644 | 1694 | Writer | Japan | 85.14 | 796 | 163 | 213,121 | 5.35 |
| 410 | Alan Turing | 1912 | 1954 | Computer scientist | United Kingdom | 85.14 | 305 | 159 | 1,365,091 | 6.25 |
| 411 | Émile Durkheim | 1858 | 1917 | Sociologist | France | 85.14 | 326 | 100 | 403,975 | 3.17 |
| 412 | Selim I | 1470 | 1520 | Politician | Türkiye | 85.13 | 286 | 81 | 813,120 | 3.71 |
| 413 | Hermann Hesse | 1877 | 1962 | Writer | Germany | 85.13 | 357 | 114 | 619,999 | 3.70 |
| 414 | Emily Dickinson | 1830 | 1886 | Writer | United States | 85.12 | 2,903 | 99 | 275,140 | 2.83 |
| 415 | Ferdinand Marcos | 1917 | 1989 | Politician | Philippines | 85.12 | 5,269 | 127 | 307,451 | 3.51 |
| 416 | Michael Jackson | 1958 | 2009 | Musician | United States | 85.12 | 61 | 279 | 3,784,843 | 8.14 |
| 417 | Joséphine de Beauharnais | 1763 | 1814 | Companion | Saint Lucia | 85.10 | 766 | 72 | 688,427 | 2.69 |
| 418 | Ashoka | 304 BC | 232 BC | Politician | India | 85.09 | 315 | 161 | 479,137 | 6.79 |
| 419 | Paracelsus | 1493 | 1541 | Physician | Switzerland | 85.08 | 309 | 78 | 358,656 | 2.68 |
| 420 | Ibn Battuta | 1304 | 1368 | Explorer | Morocco | 85.06 | 264 | 140 | 364,111 | 5.41 |
| 421 | Napoleon III | 1808 | 1873 | Politician | France | 85.06 | 304 | 109 | 1,246,699 | 4.61 |
| 422 | Pope Urban VII | 1521 | 1590 | Religious figure | Italy | 85.06 | 1,101 | 77 | 395,966 | 2.64 |
| 423 | Giotto | 1267 | 1337 | Painter | Italy | 85.03 | 709 | 90 | 293,415 | 3.25 |
| 424 | Roald Amundsen | 1872 | 1928 | Explorer | Norway | 84.99 | 279 | 160 | 384,930 | 5.02 |
| 425 | Ernest Hemingway | 1899 | 1961 | Writer | United States | 84.99 | 325 | 151 | 1,251,160 | 6.22 |
| 426 | Franz Liszt | 1811 | 1886 | Musician | Austria | 84.99 | 316 | 101 | 571,728 | 3.75 |
| 427 | Al Gore | 1948 | – | Politician | United States | 84.97 | 524 | 106 | 431,007 | 2.47 |
| 428 | Otto I, Holy Roman Emperor | 912 | 973 | Politician | Germany | 84.97 | 490 | 83 | 343,798 | 3.11 |
| 429 | Pablo Escobar | 1949 | 1993 | Mafioso | Colombia | 84.96 | 330 | 99 | 3,384,413 | 3.91 |
| 430 | Pope Clement VII | 1478 | 1534 | Religious figure | Italy | 84.95 | 529 | 77 | 347,647 | 2.80 |
| 431 | Ivan the Terrible | 1530 | 1584 | Politician | Russia | 84.95 | 358 | 104 | 1,121,129 | 4.88 |
| 432 | Martin Heidegger | 1889 | 1976 | Philosopher | Germany | 84.92 | 353 | 113 | 581,315 | 3.68 |
| 433 | Karl Dönitz | 1891 | 1980 | Military personnel | Germany | 84.90 | 329 | 78 | 905,182 | 2.82 |
| 434 | Boris Yeltsin | 1931 | 2007 | Politician | Russia | 84.88 | 368 | 135 | 1,241,186 | 4.97 |
| 435 | Heinrich Himmler | 1900 | 1945 | Politician | Germany | 84.86 | 372 | 93 | 1,709,036 | 3.91 |
| 436 | Hypatia | 350 | 415 | Mathematician | Egypt | 84.85 | 384 | 96 | 565,234 | 3.96 |
| 437 | Juan Carlos I of Spain | 1938 | – | Nobleman | Italy | 84.83 | 925 | 109 | 927,900 | 3.88 |
| 438 | Donatello | 1386 | 1466 | Painter | Italy | 84.83 | 440 | 100 | 263,047 | 3.69 |
| 439 | Tiberius | 42 BC | 37 | Politician | Italy | 84.83 | 439 | 101 | 701,182 | 4.61 |
| 440 | Harald Hardrada | 1015 | 1066 | Politician | Norway | 84.83 | 5,811 | 56 | 274,497 | 1.83 |
| 441 | George W. Bush | 1946 | – | Politician | United States | 84.81 | 619 | 212 | 2,197,628 | 8.44 |
| 442 | Horace | 65 BC | 8 BC | Writer | Italy | 84.80 | 322 | 101 | 238,732 | 3.60 |
| 443 | Jonah | 850 BC | 810 BC | Religious figure | Israel | 84.79 | 402 | 68 | 405,680 | 2.61 |
| 444 | Philip II of Spain | 1527 | 1598 | Politician | Spain | 84.79 | 320 | 96 | 876,042 | 4.34 |
| 445 | Alexander Fleming | 1881 | 1955 | Biologist | United Kingdom | 84.76 | 365 | 116 | 444,271 | 4.02 |
| 446 | Camilla, Duchess of Cornwall | 1947 | – | Nobleman | United Kingdom | 84.73 | 349 | 75 | 886,237 | 2.20 |
| 447 | Queen of Sheba | 1000 BC | 1000 BC | Religious figure | NA | 84.73 | 427 | 89 | 554,900 | 3.90 |
| 448 | Hurrem Sultan | 1502 | 1558 | Politician | Ukraine | 84.73 | 299 | 76 | 1,199,309 | 2.85 |
| 449 | Pope Gregory XVI | 1765 | 1846 | Religious figure | Italy | 84.71 | 1,084 | 81 | 618,169 | 2.89 |
| 450 | Hassanal Bolkiah | 1946 | – | Politician | Brunei | 84.69 | 3,139 | 87 | 438,504 | 2.18 |
| 451 | Hulagu Khan | 1217 | 1265 | Politician | Mongolia | 84.69 | 542 | 76 | 294,778 | 2.71 |
| 452 | Murad II | 1404 | 1451 | Politician | Türkiye | 84.67 | 489 | 74 | 779,608 | 3.16 |
| 453 | Bartolomeu Dias | 1450 | 1500 | Explorer | Portugal | 84.66 | 296 | 77 | 189,774 | 2.66 |
| 454 | Louis XVIII of France | 1755 | 1824 | Politician | France | 84.65 | 1,162 | 81 | 761,273 | 3.42 |
| 455 | Sulla | 138 BC | 78 BC | Politician | Italy | 84.65 | 1,002 | 67 | 288,413 | 2.36 |
| 456 | F. Scott Fitzgerald | 1896 | 1940 | Writer | United States | 84.65 | 420 | 83 | 466,394 | 2.44 |
| 457 | Claudius | 10 BC | 54 | Politician | France | 84.64 | 607 | 95 | 531,272 | 4.17 |
| 458 | Alexander Pushkin | 1799 | 1837 | Writer | Russia | 84.64 | 343 | 172 | 2,040,634 | 8.16 |
| 459 | Johann Strauss II | 1825 | 1899 | Composer | Austria | 84.64 | 1,088 | 81 | 518,563 | 3.06 |
| 460 | Simone de Beauvoir | 1908 | 1986 | Writer | France | 84.63 | 413 | 133 | 737,639 | 4.40 |
| 461 | Titian | 1488 | 1576 | Painter | Italy | 84.62 | 367 | 91 | 311,988 | 3.49 |
| 462 | Hokusai | 1760 | 1849 | Artist | Japan | 84.61 | 385 | 155 | 558,890 | 5.54 |
| 463 | Walt Disney | 1901 | 1966 | Producer | United States | 84.61 | 339 | 170 | 1,190,415 | 6.76 |
| 464 | Maria Montessori | 1870 | 1952 | Philosopher | Italy | 84.59 | 364 | 93 | 658,783 | 3.13 |
| 465 | Hadrian | 76 | 138 | Politician | Spain | 84.58 | 412 | 96 | 621,640 | 4.37 |
| 466 | Friedrich Schiller | 1759 | 1805 | Writer | Germany | 84.57 | 345 | 114 | 417,170 | 4.22 |
| 467 | Pontius Pilate | 12 BC | 38 | Politician | Italy | 84.56 | 414 | 84 | 931,645 | 4.21 |
| 468 | Gustav Klimt | 1862 | 1918 | Painter | Austria | 84.52 | 378 | 92 | 629,919 | 3.39 |
| 469 | Robert Schumann | 1810 | 1856 | Composer | Germany | 84.50 | 241 | 102 | 424,704 | 3.52 |
| 470 | Pope Julius II | 1443 | 1513 | Religious figure | Italy | 84.50 | 654 | 87 | 464,402 | 3.36 |
| 471 | Albert A. Michelson | 1852 | 1931 | Physicist | Poland | 84.49 | 3,400 | 93 | 37,459 | 1.73 |
| 472 | Carl XVI Gustaf of Sweden | 1946 | – | Politician | Sweden | 84.47 | 682 | 90 | 706,986 | 2.71 |
| 473 | Parmenides | 501 BC | 470 BC | Philosopher | Italy | 84.47 | 324 | 86 | 239,970 | 3.03 |
| 474 | Aristophanes | 448 BC | 386 BC | Writer | Greece | 84.47 | 393 | 97 | 198,459 | 3.56 |
| 475 | Søren Kierkegaard | 1813 | 1855 | Philosopher | Denmark | 84.47 | 421 | 113 | 499,995 | 4.43 |
| 476 | Origen | 185 | 254 | Philosopher | Egypt | 84.46 | 479 | 68 | 207,664 | 2.19 |
| 477 | Pope Gregory XIII | 1502 | 1585 | Religious figure | Italy | 84.42 | 755 | 88 | 246,225 | 3.07 |
| 478 | Thomas Hardy | 1840 | 1928 | Writer | United Kingdom | 84.42 | 9,004 | 89 | 128,174 | 2.19 |
| 479 | Charles Baudelaire | 1821 | 1867 | Writer | France | 84.42 | 359 | 106 | 484,184 | 3.72 |
| 480 | Rodrigo Duterte | 1945 | – | Politician | Philippines | 84.40 | 890 | 96 | 548,551 | 2.70 |
| 481 | Marcel Proust | 1871 | 1922 | Writer | France | 84.39 | 523 | 138 | 523,308 | 4.67 |
| 482 | Severus Alexander | 208 | 235 | Politician | Lebanon | 84.39 | 1,528 | 75 | 258,345 | 2.60 |
| 483 | Niccolò Paganini | 1782 | 1840 | Musician | Italy | 84.38 | 363 | 88 | 398,941 | 3.09 |
| 484 | Strabo | 64 BC | 23 | Geographer | Türkiye | 84.37 | 390 | 93 | 164,908 | 3.36 |
| 485 | Henry IV of France | 1553 | 1610 | Politician | France | 84.36 | 391 | 85 | 902,681 | 3.87 |
| 486 | Pierre Curie | 1859 | 1906 | Physicist | France | 84.35 | 373 | 114 | 336,575 | 3.77 |
| 487 | Uthman | 574 | 656 | Politician | Saudi Arabia | 84.34 | 282 | 96 | 792,365 | 4.56 |
| 488 | Josef Mengele | 1911 | 1979 | Physician | Germany | 84.33 | 609 | 70 | 2,037,122 | 3.17 |
| 489 | Prince Henry the Navigator | 1394 | 1460 | Explorer | Portugal | 84.33 | 884 | 66 | 167,489 | 2.02 |
| 490 | Pope Leo XI | 1535 | 1605 | Religious figure | Italy | 84.32 | 1,218 | 79 | 288,633 | 2.74 |
| 491 | Denis Diderot | 1713 | 1784 | Writer | France | 84.31 | 290 | 100 | 266,086 | 3.40 |
| 492 | André-Marie Ampère | 1775 | 1836 | Physicist | France | 84.30 | 560 | 105 | 150,449 | 3.07 |
| 493 | Murad III | 1546 | 1595 | Politician | Türkiye | 84.29 | 323 | 74 | 703,836 | 3.25 |
| 494 | Pope Pius VII | 1742 | 1823 | Religious figure | Italy | 84.28 | 1,244 | 84 | 494,153 | 3.03 |
| 495 | Evangelista Torricelli | 1608 | 1647 | Physicist | Italy | 84.27 | 497 | 84 | 101,685 | 2.43 |
| 496 | El Greco | 1541 | 1614 | Painter | Greece | 84.26 | 281 | 105 | 284,819 | 3.90 |
| 497 | Jan Hus | 1369 | 1415 | Social activist | Czechia | 84.26 | 381 | 80 | 425,202 | 3.38 |
| 498 | Émile Zola | 1840 | 1902 | Writer | France | 84.25 | 374 | 114 | 718,442 | 4.49 |
| 499 | Ahmed I | 1590 | 1617 | Politician | Türkiye | 84.23 | 275 | 72 | 757,395 | 3.15 |
| 500 | Erwin Schrödinger | 1887 | 1961 | Physicist | Austria | 84.23 | 577 | 137 | 404,169 | 4.76 |
| 501 | Saint Barbara | 300 | 306 | Religious figure | Türkiye | 84.23 | 376 | 57 | 437,569 | 2.26 |
| 502 | Al-Farabi | 872 | 951 | Philosopher | Afghanistan | 84.23 | 352 | 80 | 469,391 | 3.06 |
| 503 | Herod the Great | 73 BC | 3 BC | Politician | Israel | 84.23 | 475 | 71 | 965,072 | 3.83 |
| 504 | Pope Leo X | 1475 | 1521 | Religious figure | Italy | 84.22 | 814 | 79 | 600,325 | 3.37 |
| 505 | Zheng He | 1387 | 1433 | Explorer | China | 84.21 | 486 | 140 | 286,354 | 5.30 |
| 506 | Bernard Montgomery | 1887 | 1976 | Military personnel | United Kingdom | 84.19 | 2,995 | 71 | 285,747 | 1.97 |
| 507 | Silvio Berlusconi | 1936 | 2023 | Politician | Italy | 84.19 | 411 | 128 | 865,639 | 4.57 |
| 508 | Pope Leo XII | 1760 | 1829 | Religious figure | Italy | 84.18 | 1,302 | 81 | 549,277 | 2.94 |
| 509 | John the Apostle | 6 | 100 | Religious figure | NA | 84.17 | 448 | 86 | 569,182 | 4.02 |
| 510 | Joseph-Louis Lagrange | 1736 | 1813 | Mathematician | Italy | 84.17 | 1,191 | 90 | 134,043 | 2.46 |
| 511 | Wassily Kandinsky | 1866 | 1944 | Painter | Russia | 84.16 | 496 | 84 | 650,505 | 2.97 |
| 512 | Prince Albert of Saxe-Coburg and Gotha | 1819 | 1861 | Nobleman | Germany | 84.15 | 2,579 | 62 | 480,209 | 2.15 |
| 513 | Piet Mondrian | 1872 | 1944 | Painter | Netherlands | 84.15 | 348 | 73 | 351,380 | 2.18 |
| 514 | Lorenzo de' Medici | 1449 | 1492 | Politician | Italy | 84.14 | 392 | 73 | 416,338 | 3.02 |
| 515 | James Cook | 1728 | 1779 | Explorer | United Kingdom | 84.14 | 375 | 161 | 510,813 | 6.75 |
| 516 | Gustave Flaubert | 1821 | 1880 | Writer | France | 84.13 | 387 | 105 | 330,138 | 3.46 |
| 517 | Euripides | 480 BC | 406 BC | Writer | Greece | 84.12 | 383 | 98 | 239,536 | 3.77 |
| 518 | Brigitte Bardot | 1934 | 2025 | Actor | France | 84.12 | 255 | 119 | 1,160,925 | 4.34 |
| 519 | Li Bai | 701 | 762 | Writer | China | 84.11 | 584 | 151 | 332,690 | 5.68 |
| 520 | Matthias the Apostle | 1 | – | Religious figure | Israel | 84.11 | 1,950 | 64 | 196,128 | 2.19 |
| 521 | Édouard Manet | 1832 | 1883 | Painter | France | 84.08 | 466 | 99 | 346,627 | 3.39 |
| 522 | Octave Mirbeau | 1848 | 1917 | Writer | France | 84.08 | 419 | 144 | 60,245 | 3.93 |
| 523 | Henri Becquerel | 1852 | 1908 | Physicist | France | 84.07 | 549 | 105 | 136,641 | 2.89 |
| 524 | James, brother of Jesus | 20 BC | 69 | Religious figure | Israel | 84.07 | 5,115 | 52 | 206,605 | 1.68 |
| 525 | Titus | 41 | 81 | Politician | Italy | 84.07 | 662 | 89 | 499,662 | 4.00 |
| 526 | Diocletian | 244 | 311 | Politician | Croatia | 84.07 | 350 | 85 | 482,510 | 4.01 |
| 527 | Hatshepsut | 1507 BC | 1458 BC | Politician | Egypt | 84.03 | 528 | 88 | 417,794 | 3.85 |
| 528 | Johan Cruyff | 1947 | 2016 | Soccer player | Netherlands | 84.03 | 449 | 102 | 1,081,369 | 3.56 |
| 529 | Maria Callas | 1923 | 1977 | Singer | United States | 84.02 | 482 | 74 | 3,198,357 | 3.87 |
| 530 | Hermann Göring | 1893 | 1946 | Politician | Germany | 84.02 | 463 | 84 | 1,412,859 | 3.72 |
| 531 | George Marshall | 1880 | 1959 | Politician | United States | 84.01 | 3,203 | 80 | 161,168 | 2.01 |
| 532 | Mary, Queen of Scots | 1542 | 1587 | Politician | United Kingdom | 84.01 | 646 | 92 | 1,368,327 | 5.14 |
| 533 | Saint Stephen | 1 | 36 | Religious figure | Greece | 84.00 | 369 | 64 | 445,754 | 2.95 |
| 534 | Elizabeth | 100 BC | 100 | Religious figure | NA | 83.98 | 966 | 55 | 164,152 | 1.68 |
| 535 | J. J. Thomson | 1856 | 1940 | Physicist | United Kingdom | 83.98 | 1,740 | 107 | 205,685 | 3.63 |
| 536 | Samson | 1118 BC | 1078 BC | Religious figure | Israel | 83.97 | 308 | 69 | 464,182 | 3.15 |
| 537 | Mark Antony | 83 BC | 30 BC | Politician | Italy | 83.97 | 690 | 90 | 666,083 | 4.46 |
| 538 | Saint Lucy | 283 | 304 | Religious figure | Italy | 83.96 | 559 | 64 | 598,882 | 2.85 |
| 539 | Lucretius | 94 BC | 55 BC | Philosopher | Italy | 83.96 | 534 | 81 | 138,916 | 2.57 |
| 540 | Astrid Lindgren | 1907 | 2002 | Writer | Sweden | 83.96 | 458 | 99 | 603,385 | 3.33 |
| 541 | Oscar Wilde | 1854 | 1900 | Writer | Ireland | 83.95 | 477 | 127 | 996,863 | 5.60 |
| 542 | Catherine de' Medici | 1519 | 1589 | Companion | Italy | 83.94 | 723 | 77 | 849,011 | 3.77 |
| 543 | Mark Twain | 1835 | 1910 | Writer | United States | 83.94 | 444 | 157 | 776,734 | 6.79 |
| 544 | Henrik Ibsen | 1828 | 1906 | Writer | Norway | 83.92 | 650 | 114 | 271,259 | 4.21 |
| 545 | Aretha Franklin | 1942 | 2018 | Singer | United States | 83.92 | 361 | 100 | 783,301 | 3.13 |
| 546 | Eugène Delacroix | 1798 | 1863 | Painter | France | 83.92 | 443 | 93 | 301,679 | 3.22 |
| 547 | Pope Pius VIII | 1761 | 1830 | Religious figure | Italy | 83.92 | 1,159 | 79 | 457,937 | 2.92 |
| 548 | Muhammad al-Bukhari | 810 | 870 | Religious figure | Uzbekistan | 83.91 | 457 | 75 | 516,212 | 3.19 |
| 549 | Pope Adrian VI | 1459 | 1523 | Religious figure | Netherlands | 83.91 | 1,486 | 76 | 372,887 | 2.90 |
| 550 | Vespasian | 9 | 79 | Politician | Italy | 83.91 | 606 | 90 | 472,473 | 4.01 |
| 551 | James Prescott Joule | 1818 | 1889 | Physicist | United Kingdom | 83.91 | 395 | 119 | 160,352 | 3.56 |
| 552 | Janis Joplin | 1943 | 1970 | Singer | United States | 83.91 | 408 | 85 | 682,118 | 2.63 |
| 553 | Gioachino Rossini | 1792 | 1868 | Composer | Italy | 83.90 | 483 | 87 | 328,361 | 3.00 |
| 554 | Ragnar Lodbrok | 800 | 801 | Nobleman | Norway | 83.90 | 287 | 55 | 968,559 | 3.02 |
| 555 | Ignatius of Loyola | 1491 | 1556 | Religious figure | Spain | 83.89 | 546 | 86 | 446,878 | 3.64 |
| 556 | Skanderbeg | 1405 | 1468 | Politician | Albania | 83.87 | 500 | 75 | 388,068 | 3.12 |
| 557 | Rollo | 846 | 930 | Nobleman | Norway | 83.87 | 2,997 | 54 | 311,787 | 2.02 |
| 558 | Anthony Hopkins | 1937 | – | Actor | United Kingdom | 83.87 | 201 | 104 | 1,728,001 | 4.43 |
| 559 | John Major | 1943 | – | Politician | United Kingdom | 83.84 | 474 | 92 | 204,763 | 2.22 |
| 560 | Stendhal | 1783 | 1842 | Writer | France | 83.83 | 377 | 91 | 296,717 | 3.03 |
| 561 | Mary of Teck | 1867 | 1953 | Companion | United Kingdom | 83.82 | 4,505 | 53 | 564,864 | 1.86 |
| 562 | Robert De Niro | 1943 | – | Actor | United States | 83.81 | 407 | 123 | 2,753,366 | 5.74 |
| 563 | Amenhotep III | 1403 BC | 1350 BC | Politician | Egypt | 83.80 | 726 | 63 | 152,946 | 1.93 |
| 564 | Hieronymus Bosch | 1450 | 1516 | Painter | Netherlands | 83.79 | 505 | 85 | 494,326 | 3.78 |
| 565 | Margaret Thatcher | 1925 | 2013 | Politician | United Kingdom | 83.79 | 355 | 152 | 1,284,104 | 6.44 |
| 566 | Yasser Arafat | 1929 | 2004 | Politician | Egypt | 83.78 | 168 | 119 | 810,146 | 4.70 |
| 567 | Khafra | 2550 BC | 2479 BC | Politician | Egypt | 83.77 | 1,250 | 62 | 121,173 | 1.79 |
| 568 | Rajneesh | 1931 | 1990 | Philosopher | India | 83.75 | 437 | 68 | 527,287 | 2.20 |
| 569 | Ayn Rand | 1905 | 1982 | Writer | Russia | 83.74 | 536 | 86 | 455,508 | 2.78 |
| 570 | Theodosius I | 340 | 395 | Politician | Spain | 83.74 | 450 | 86 | 351,714 | 3.88 |
| 571 | Al-Biruni | 973 | 1048 | Mathematician | Uzbekistan | 83.73 | 356 | 94 | 570,755 | 4.09 |
| 572 | Honorius | 384 | 423 | Politician | Türkiye | 83.72 | 1,764 | 73 | 116,435 | 2.24 |
| 573 | Ecgberht, King of Wessex | 800 | 839 | Politician | United Kingdom | 83.72 | 5,049 | 54 | 157,297 | 1.63 |
| 574 | Thucydides | 460 BC | 397 BC | Historian | Greece | 83.71 | 493 | 93 | 244,445 | 3.84 |
| 575 | Baldwin IV of Jerusalem | 1161 | 1185 | Politician | Israel | 83.71 | 575 | 48 | 1,345,056 | 2.93 |
| 576 | Domitian | 51 | 96 | Politician | Italy | 83.71 | 839 | 90 | 458,578 | 4.05 |
| 577 | Anthony the Great | 251 | 356 | Religious figure | Egypt | 83.70 | 446 | 66 | 355,953 | 2.66 |
| 578 | Gustavus Adolphus of Sweden | 1594 | 1632 | Politician | Sweden | 83.70 | 530 | 75 | 227,182 | 2.65 |
| 579 | Pope Urban VIII | 1568 | 1644 | Religious figure | Italy | 83.69 | 1,005 | 81 | 261,372 | 2.89 |
| 580 | Mary Magdalene | 10 BC | 100 | Religious figure | Israel | 83.67 | 317 | 90 | 1,362,055 | 4.21 |
| 581 | Aeschylus | 525 BC | 456 BC | Writer | Greece | 83.66 | 409 | 102 | 343,624 | 4.48 |
| 582 | Ernest Rutherford | 1871 | 1937 | Physicist | New Zealand | 83.66 | 388 | 139 | 319,347 | 4.99 |
| 583 | Michel de Montaigne | 1533 | 1592 | Philosopher | France | 83.66 | 797 | 87 | 294,610 | 3.41 |
| 584 | John Wilkes Booth | 1838 | 1865 | Extremist | United States | 83.65 | 611 | 57 | 279,622 | 1.69 |
| 585 | Bayezid II | 1447 | 1512 | Politician | Greece | 83.64 | 502 | 72 | 692,879 | 3.45 |
| 586 | Edward Victor Appleton | 1892 | 1965 | Physicist | United Kingdom | 83.64 | 3,991 | 81 | 12,511 | 0.97 |
| 587 | Bertolt Brecht | 1898 | 1956 | Writer | Germany | 83.64 | 574 | 107 | 601,705 | 3.92 |
| 588 | Husayn ibn Ali | 626 | 680 | Religious figure | Saudi Arabia | 83.63 | 382 | 85 | 643,957 | 4.06 |
| 589 | Bayezid I | 1354 | 1403 | Politician | Türkiye | 83.62 | 712 | 77 | 488,501 | 3.60 |
| 590 | Pope Pius VI | 1717 | 1799 | Religious figure | Italy | 83.62 | 1,192 | 78 | 412,114 | 2.90 |
| 591 | John Lennon | 1940 | 1980 | Musician | United Kingdom | 83.61 | 451 | 138 | 1,888,968 | 6.22 |
| 592 | Harry S. Truman | 1884 | 1972 | Politician | United States | 83.61 | 410 | 154 | 1,161,389 | 6.87 |
| 593 | Recep Tayyip Erdoğan | 1954 | – | Politician | Türkiye | 83.60 | 551 | 145 | 2,135,335 | 4.97 |
| 594 | Christina, Queen of Sweden | 1626 | 1689 | Politician | Sweden | 83.60 | 1,813 | 67 | 233,766 | 2.25 |
| 595 | Sun Tzu | 544 BC | 496 BC | Philosopher | China | 83.60 | 425 | 110 | 319,386 | 4.84 |
| 596 | Empedocles | 490 BC | 430 BC | Philosopher | Italy | 83.60 | 476 | 83 | 188,404 | 3.11 |
| 597 | Pieter Bruegel the Elder | 1525 | 1569 | Painter | Netherlands | 83.58 | 461 | 83 | 304,767 | 3.44 |
| 598 | Franz Beckenbauer | 1945 | 2024 | Soccer player | Germany | 83.54 | 366 | 97 | 937,103 | 3.50 |
| 599 | Theodora | 500 | 548 | Companion | Cyprus | 83.54 | 2,948 | 58 | 178,900 | 1.90 |
| 600 | Gian Lorenzo Bernini | 1598 | 1680 | Architect | Italy | 83.54 | 532 | 76 | 348,063 | 3.10 |
| 601 | John Dalton | 1766 | 1844 | Chemist | United Kingdom | 83.53 | 481 | 103 | 265,825 | 3.80 |
| 602 | Murad I | 1326 | 1389 | Politician | Türkiye | 83.53 | 470 | 74 | 415,445 | 3.20 |
| 603 | Sima Qian | 145 BC | 86 BC | Historian | China | 83.52 | 635 | 118 | 174,695 | 3.99 |
| 604 | Felix Mendelssohn | 1809 | 1847 | Composer | Germany | 83.51 | 547 | 103 | 393,020 | 3.80 |
| 605 | Plutarch | 46 | 127 | Philosopher | Greece | 83.51 | 394 | 99 | 319,455 | 4.30 |
| 606 | Werner Heisenberg | 1901 | 1976 | Physicist | Germany | 83.50 | 472 | 113 | 788,408 | 4.39 |
| 607 | Christian IX of Denmark | 1818 | 1906 | Politician | Germany | 83.50 | 1,728 | 62 | 221,004 | 1.82 |
| 608 | Anaximander | 610 BC | 546 BC | Philosopher | Türkiye | 83.48 | 344 | 87 | 221,547 | 3.37 |
| 609 | Joan Baez | 1941 | – | Singer | United States | 83.48 | 1,237 | 80 | 1,313,791 | 3.10 |
| 610 | Edvard Grieg | 1843 | 1907 | Composer | Norway | 83.48 | 478 | 98 | 298,129 | 3.36 |
| 611 | Selma Lagerlöf | 1858 | 1940 | Writer | Sweden | 83.47 | 338 | 115 | 234,770 | 3.56 |
| 612 | Robert Koch | 1843 | 1910 | Physician | Germany | 83.47 | 456 | 114 | 268,908 | 3.83 |
| 613 | Rabindranath Tagore | 1861 | 1941 | Writer | India | 83.47 | 553 | 164 | 690,939 | 6.74 |
| 614 | Tycho Brahe | 1546 | 1601 | Astronomer | Sweden | 83.46 | 622 | 105 | 228,665 | 4.33 |
| 615 | Pierre de Fermat | 1601 | 1665 | Mathematician | France | 83.45 | 665 | 97 | 141,226 | 3.26 |
| 616 | Giovanni Pierluigi da Palestrina | 1520 | 1594 | Composer | France | 83.45 | 888 | 102 | 125,295 | 3.43 |
| 617 | Hayao Miyazaki | 1941 | – | Film director | Japan | 83.44 | 360 | 99 | 1,708,129 | 4.10 |
| 618 | Arnold Schwarzenegger | 1947 | – | Actor | Austria | 83.44 | 399 | 122 | 2,928,840 | 5.77 |
| 619 | Marlene Dietrich | 1901 | 1992 | Actor | Germany | 83.42 | 522 | 163 | 704,952 | 5.79 |
| 620 | Puyi | 1906 | 1967 | Politician | China | 83.41 | 1,548 | 77 | 1,208,194 | 3.16 |
| 621 | Simón Bolívar | 1783 | 1830 | Politician | Venezuela | 83.41 | 516 | 150 | 1,252,992 | 6.86 |
| 622 | Guglielmo Marconi | 1874 | 1937 | Inventor | Italy | 83.41 | 598 | 117 | 350,650 | 4.26 |
| 623 | Claudio Monteverdi | 1567 | 1643 | Composer | Italy | 83.41 | 633 | 76 | 175,645 | 2.65 |
| 624 | Jorge Luis Borges | 1899 | 1986 | Writer | Argentina | 83.40 | 623 | 144 | 593,904 | 5.16 |
| 625 | Abu Hanifa | 698 | 767 | Religious figure | Iraq | 83.39 | 398 | 77 | 412,845 | 3.25 |
| 626 | Philip IV of France | 1268 | 1314 | Politician | France | 83.39 | 464 | 79 | 438,754 | 3.46 |
| 627 | William Thomson, 1st Baron Kelvin | 1824 | 1907 | Physicist | United Kingdom | 83.39 | 1,972 | 85 | 126,014 | 2.59 |
| 628 | Pepin the Short | 715 | 768 | Politician | Belgium | 83.38 | 406 | 79 | 400,655 | 3.41 |
| 629 | Alexander von Humboldt | 1769 | 1859 | Geographer | Germany | 83.38 | 473 | 106 | 359,086 | 3.90 |
| 630 | Isaiah | 800 BC | 700 BC | Religious figure | Israel | 83.38 | 462 | 71 | 383,821 | 3.24 |
| 631 | Protagoras | 486 BC | 420 BC | Philosopher | Greece | 83.37 | 492 | 71 | 129,644 | 2.42 |
| 632 | Salman of Saudi Arabia | 1935 | – | Politician | Saudi Arabia | 83.36 | 693 | 95 | 1,272,482 | 4.06 |
| 633 | Stefan Zweig | 1881 | 1942 | Writer | Austria | 83.35 | 487 | 83 | 596,246 | 2.97 |
| 634 | Thomas Mann | 1875 | 1955 | Writer | Germany | 83.34 | 438 | 119 | 875,940 | 4.92 |
| 635 | Pope Innocent III | 1160 | 1216 | Religious figure | Italy | 83.33 | 929 | 82 | 425,343 | 3.45 |
| 636 | Henry Dunant | 1828 | 1910 | Social activist | Switzerland | 83.32 | 426 | 93 | 191,943 | 2.95 |
| 637 | Napoleon II | 1811 | 1832 | Politician | France | 83.31 | 274 | 74 | 644,738 | 3.16 |
| 638 | David Hume | 1711 | 1776 | Philosopher | United Kingdom | 83.28 | 422 | 108 | 359,727 | 4.60 |
| 639 | Akihito | 1933 | – | Nobleman | Japan | 83.28 | 617 | 116 | 970,765 | 4.50 |
| 640 | Pope Pius III | 1439 | 1503 | Religious figure | Italy | 83.27 | 845 | 74 | 240,807 | 2.68 |
| 641 | Lee Kuan Yew | 1923 | 2015 | Politician | Singapore | 83.27 | 629 | 100 | 376,451 | 3.34 |
| 642 | Ludwig Wittgenstein | 1889 | 1951 | Philosopher | Austria | 83.27 | 503 | 121 | 487,744 | 4.58 |
| 643 | Orhan | 1288 | 1362 | Politician | Türkiye | 83.26 | 570 | 79 | 511,117 | 3.69 |
| 644 | Lord Mountbatten | 1900 | 1979 | Politician | United Kingdom | 83.26 | 3,388 | 57 | 418,742 | 1.89 |
| 645 | Sophia Loren | 1934 | – | Actor | Italy | 83.26 | 657 | 100 | 1,289,298 | 4.22 |
| 646 | Louis XVII of France | 1785 | 1795 | Politician | France | 83.26 | 735 | 59 | 522,863 | 2.41 |
| 647 | Gerd Müller | 1945 | 2021 | Soccer player | Germany | 83.25 | 819 | 85 | 457,764 | 2.65 |
| 648 | Gustave Eiffel | 1832 | 1923 | Engineer | France | 83.25 | 579 | 95 | 558,385 | 3.77 |
| 649 | Eusebius | 265 | 339 | Religious figure | Israel | 83.24 | 2,165 | 65 | 128,478 | 2.08 |
| 650 | Florence Nightingale | 1820 | 1910 | Physician | Italy | 83.23 | 445 | 119 | 739,553 | 5.42 |
| 651 | Luciano Pavarotti | 1935 | 2007 | Singer | Italy | 83.23 | 659 | 96 | 783,185 | 3.57 |
| 652 | Arthur Conan Doyle | 1859 | 1930 | Writer | United Kingdom | 83.22 | 554 | 120 | 594,915 | 5.02 |
| 653 | Enrico Fermi | 1901 | 1954 | Physicist | Italy | 83.22 | 550 | 147 | 378,200 | 5.17 |
| 654 | Imelda Marcos | 1929 | – | Companion | Philippines | 83.21 | 10,940 | 95 | 154,174 | 2.39 |
| 655 | Cardinal Richelieu | 1585 | 1642 | Politician | France | 83.21 | 583 | 81 | 548,082 | 3.64 |
| 656 | James V of Scotland | 1512 | 1542 | Politician | United Kingdom | 83.19 | 4,658 | 63 | 152,502 | 2.13 |
| 657 | Howard Hughes | 1905 | 1976 | Businessperson | United States | 83.19 | 589 | 68 | 634,232 | 2.44 |
| 658 | Anders Celsius | 1701 | 1744 | Astronomer | Sweden | 83.19 | 588 | 93 | 131,974 | 3.01 |
| 659 | Robert Frost | 1874 | 1963 | Writer | United States | 83.18 | 595 | 81 | 86,386 | 1.94 |
| 660 | Pope Benedict XIV | 1675 | 1758 | Religious figure | Italy | 83.17 | 1,551 | 80 | 322,658 | 2.98 |
| 661 | 14th Dalai Lama | 1935 | – | Religious figure | China | 83.17 | 681 | 118 | 1,059,225 | 4.96 |
| 662 | Harald Bluetooth | 935 | 986 | Politician | Denmark | 83.17 | 4,300 | 55 | 190,389 | 1.88 |
| 663 | Maurice Ravel | 1875 | 1937 | Composer | France | 83.16 | 945 | 88 | 628,337 | 3.32 |
| 664 | Wallis Simpson | 1896 | 1986 | Celebrity | United States | 83.16 | 517 | 60 | 407,517 | 1.95 |
| 665 | Romain Rolland | 1866 | 1944 | Writer | France | 83.15 | 573 | 94 | 186,466 | 2.68 |
| 666 | Philip II of Macedon | 382 BC | 336 BC | Politician | Greece | 83.15 | 460 | 80 | 334,148 | 3.80 |
| 667 | Audrey Hepburn | 1929 | 1993 | Actor | Belgium | 83.14 | 509 | 115 | 1,780,763 | 5.43 |
| 668 | Charles Perrault | 1628 | 1703 | Writer | France | 83.14 | 586 | 82 | 309,967 | 3.14 |
| 669 | James Watson | 1928 | 2025 | Biologist | United States | 83.14 | 2,083 | 86 | 163,616 | 2.24 |
| 670 | William I, German Emperor | 1797 | 1888 | Politician | Germany | 83.14 | 701 | 82 | 496,146 | 3.47 |
| 671 | Maximilian II, Holy Roman Emperor | 1527 | 1576 | Politician | Austria | 83.14 | 2,427 | 63 | 172,294 | 2.08 |
| 672 | Aleister Crowley | 1875 | 1947 | Occultist | United Kingdom | 83.14 | 2,490 | 58 | 507,852 | 2.02 |
| 673 | Umberto Eco | 1932 | 2016 | Writer | Italy | 83.13 | 564 | 115 | 433,028 | 3.77 |
| 674 | Judas Iscariot | 50 | 30 | Religious figure | Israel | 83.13 | 578 | 84 | 1,106,648 | 3.89 |
| 675 | Pope Pius V | 1504 | 1572 | Religious figure | Italy | 83.13 | 731 | 81 | 274,739 | 3.11 |
| 676 | Adolf Eichmann | 1906 | 1962 | Military personnel | Germany | 83.12 | 543 | 76 | 1,357,478 | 3.62 |
| 677 | John William Strutt, 3rd Baron Rayleigh | 1842 | 1919 | Physicist | United Kingdom | 83.12 | 4,016 | 90 | 39,130 | 1.91 |
| 678 | Edward the Black Prince | 1330 | 1376 | Nobleman | United Kingdom | 83.11 | 3,467 | 60 | 215,386 | 2.17 |
| 679 | Ruhollah Khomeini | 1902 | 1989 | Religious figure | Iran | 83.10 | 415 | 108 | 1,068,129 | 4.60 |
| 680 | Hector Berlioz | 1803 | 1869 | Composer | France | 83.08 | 961 | 108 | 222,094 | 3.83 |
| 681 | Georg Ohm | 1789 | 1854 | Physicist | Germany | 83.08 | 634 | 96 | 136,770 | 3.06 |
| 682 | Kösem Sultan | 1590 | 1651 | Politician | Greece | 83.07 | 337 | 55 | 686,561 | 2.72 |
| 683 | Giacomo Casanova | 1725 | 1798 | Writer | Italy | 83.07 | 525 | 76 | 554,322 | 3.34 |
| 684 | Auguste Rodin | 1840 | 1917 | Sculptor | France | 83.07 | 533 | 95 | 335,315 | 3.58 |
| 685 | Zechariah | 90 BC | 100 | Religious figure | NA | 83.06 | 1,109 | 59 | 229,703 | 2.28 |
| 686 | Ivan Pavlov | 1849 | 1936 | Biologist | Russia | 83.05 | 521 | 99 | 369,402 | 3.75 |
| 687 | Georges Bizet | 1838 | 1875 | Composer | France | 83.04 | 557 | 87 | 267,624 | 2.99 |
| 688 | Pope Paul III | 1468 | 1549 | Religious figure | Italy | 83.04 | 898 | 83 | 299,025 | 3.23 |
| 689 | Pope Linus | 1 | 79 | Religious figure | Italy | 83.03 | 1,433 | 94 | 510,910 | 4.29 |
| 690 | Sappho | 630 BC | 570 BC | Writer | Greece | 83.03 | 435 | 109 | 317,010 | 4.93 |
| 691 | Hildegard of Bingen | 1098 | 1179 | Religious figure | Germany | 83.03 | 615 | 88 | 492,705 | 3.95 |
| 692 | Isabella I of Castile | 1451 | 1504 | Politician | Spain | 83.02 | 480 | 93 | 700,847 | 4.62 |
| 693 | Saint Valentine | 226 | 273 | Religious figure | Italy | 83.01 | 590 | 65 | 751,484 | 3.76 |
| 694 | Saint Lawrence | 225 | 258 | Religious figure | Spain | 83.00 | 897 | 62 | 159,604 | 2.15 |
| 695 | Claude Debussy | 1862 | 1918 | Composer | France | 82.99 | 835 | 101 | 451,018 | 4.04 |
| 696 | Amedeo Modigliani | 1884 | 1920 | Painter | Italy | 82.99 | 825 | 79 | 394,767 | 2.80 |
| 697 | Pope Pius II | 1405 | 1464 | Religious figure | Italy | 82.97 | 1,032 | 77 | 197,311 | 2.77 |
| 698 | Pope Innocent XI | 1611 | 1689 | Religious figure | Italy | 82.96 | 1,411 | 75 | 221,548 | 2.75 |
| 699 | Anthony of Padua | 1195 | 1231 | Religious figure | Portugal | 82.94 | 600 | 70 | 530,970 | 3.21 |
| 700 | Charles XIV John of Sweden | 1763 | 1844 | Military personnel | France | 82.94 | 904 | 70 | 276,770 | 2.45 |
| 701 | Andy Warhol | 1928 | 1987 | Artist | United States | 82.94 | 576 | 140 | 975,764 | 5.94 |
| 702 | Artaxerxes I of Persia | 500 BC | 424 BC | Politician | NA | 82.94 | 1,539 | 64 | 123,586 | 2.16 |
| 703 | Robert Hooke | 1635 | 1703 | Physicist | United Kingdom | 82.93 | 404 | 95 | 255,175 | 3.87 |
| 704 | Bill Clinton | 1946 | – | Politician | United States | 82.93 | 809 | 172 | 1,789,527 | 7.81 |
| 705 | Marlon Brando | 1924 | 2004 | Actor | United States | 82.91 | 645 | 134 | 1,457,129 | 6.16 |
| 706 | Toni Morrison | 1931 | 2019 | Writer | United States | 82.91 | 765 | 108 | 143,246 | 2.88 |
| 707 | Joan Miró | 1893 | 1983 | Painter | Spain | 82.90 | 730 | 88 | 365,585 | 3.03 |
| 708 | Anaxagoras | 500 BC | 428 BC | Philosopher | Türkiye | 82.89 | 603 | 79 | 195,745 | 3.05 |
| 709 | Oda Nobunaga | 1534 | 1582 | Military personnel | Japan | 82.89 | 763 | 75 | 1,052,845 | 4.07 |
| 710 | Pol Pot | 1925 | 1998 | Politician | Cambodia | 82.87 | 535 | 114 | 1,250,589 | 5.21 |
| 711 | George R. R. Martin | 1948 | – | Writer | United States | 82.87 | 5,290 | 91 | 562,197 | 2.74 |
| 712 | Basil of Caesarea | 329 | 379 | Physician | Türkiye | 82.87 | 514 | 70 | 221,377 | 2.81 |
| 713 | Phidias | 490 BC | 430 BC | Sculptor | Greece | 82.85 | 541 | 68 | 131,935 | 2.40 |
| 714 | John Amos Comenius | 1592 | 1670 | Philosopher | Czechia | 82.84 | 507 | 66 | 272,865 | 2.72 |
| 715 | Sejong the Great | 1397 | 1450 | Politician | South Korea | 82.84 | 1,133 | 68 | 365,726 | 2.93 |
| 716 | Lord Byron | 1788 | 1824 | Writer | United Kingdom | 82.84 | 89 | 152 | 508,447 | 6.64 |
| 717 | Francis I of France | 1494 | 1547 | Politician | France | 82.84 | 604 | 80 | 633,341 | 3.93 |
| 718 | Nikolai Gogol | 1809 | 1852 | Writer | Ukraine | 82.82 | 582 | 107 | 938,106 | 5.18 |
| 719 | Xi Jinping | 1953 | – | Politician | China | 82.81 | 737 | 144 | 3,661,661 | 5.69 |
| 720 | Pope Leo I | 390 | 461 | Religious figure | Italy | 82.81 | 1,762 | 84 | 695,487 | 4.27 |
| 721 | Lucius Tarquinius Superbus | 600 BC | 495 BC | Politician | Italy | 82.80 | 705 | 55 | 148,267 | 1.93 |
| 722 | D. H. Lawrence | 1885 | 1930 | Writer | United Kingdom | 82.80 | 6,394 | 76 | 126,706 | 2.07 |
| 723 | Pope Clement XII | 1652 | 1740 | Religious figure | Italy | 82.80 | 1,330 | 77 | 242,490 | 2.89 |
| 724 | Haakon VII of Norway | 1872 | 1957 | Politician | Denmark | 82.79 | 734 | 66 | 205,165 | 1.94 |
| 725 | Benedict of Nursia | 480 | 543 | Religious figure | Italy | 82.79 | 748 | 79 | 511,614 | 3.53 |
| 726 | Prince Philip, Duke of Edinburgh | 1921 | 2021 | Nobleman | Greece | 82.77 | 465 | 114 | 1,393,317 | 5.50 |
| 727 | John Maynard Keynes | 1883 | 1946 | Economist | United Kingdom | 82.77 | 434 | 135 | 393,040 | 5.31 |
| 728 | Sun Yat-sen | 1866 | 1925 | Politician | China | 82.77 | 513 | 127 | 829,285 | 5.29 |
| 729 | Lech Wałęsa | 1943 | – | Politician | Poland | 82.76 | 612 | 152 | 709,468 | 5.56 |
| 730 | Akira Kurosawa | 1910 | 1998 | Film director | Japan | 82.76 | 676 | 150 | 643,684 | 5.70 |
| 731 | Daniel Defoe | 1660 | 1731 | Writer | United Kingdom | 82.76 | 692 | 102 | 246,168 | 4.18 |
| 732 | Maximilian I, Holy Roman Emperor | 1459 | 1519 | Politician | Austria | 82.74 | 711 | 74 | 417,484 | 3.37 |
| 733 | Cecil Rhodes | 1853 | 1902 | Businessperson | United Kingdom | 82.74 | 572 | 84 | 144,660 | 2.43 |
| 734 | Swami Vivekananda | 1863 | 1902 | Philosopher | India | 82.73 | 2,287 | 92 | 569,813 | 3.73 |
| 735 | Pope Sixtus V | 1520 | 1590 | Religious figure | Italy | 82.73 | 1,350 | 74 | 277,632 | 3.03 |
| 736 | Bob Dylan | 1941 | – | Musician | United States | 82.73 | 1,076 | 143 | 4,983,745 | 7.86 |
| 737 | Maria Goeppert Mayer | 1906 | 1972 | Physicist | Poland | 82.73 | 2,550 | 97 | 46,947 | 2.13 |
| 738 | Ayrton Senna | 1960 | 1994 | Racing driver | Brazil | 82.72 | 1,771 | 90 | 7,457,237 | 3.38 |
| 739 | Rudolf, Crown Prince of Austria | 1858 | 1889 | Nobleman | Austria | 82.72 | 988 | 47 | 1,292,989 | 2.34 |
| 740 | Ferdinand I, Holy Roman Emperor | 1503 | 1564 | Politician | Spain | 82.71 | 616 | 70 | 338,781 | 3.11 |
| 741 | Bertrand Russell | 1872 | 1970 | Mathematician | United Kingdom | 82.69 | 488 | 125 | 482,071 | 5.31 |
| 742 | Mehmed III | 1566 | 1603 | Politician | Türkiye | 82.68 | 430 | 69 | 633,131 | 3.39 |
| 743 | Joanna of Castile | 1479 | 1555 | Politician | Spain | 82.66 | 720 | 68 | 626,692 | 3.33 |
| 744 | Benjamin Netanyahu | 1949 | – | Politician | Israel | 82.66 | 494 | 125 | 1,990,658 | 5.49 |
| 745 | Archduke Franz Ferdinand of Austria | 1863 | 1914 | Nobleman | Austria | 82.65 | 555 | 96 | 886,225 | 4.69 |
| 746 | Pierre de Coubertin | 1863 | 1937 | Businessperson | France | 82.65 | 739 | 91 | 186,911 | 2.97 |
| 747 | Marc Chagall | 1887 | 1985 | Painter | Belarus | 82.65 | 680 | 84 | 575,117 | 3.26 |
| 748 | Richard Nixon | 1913 | 1994 | Politician | United States | 82.64 | 62 | 152 | 1,465,714 | 7.38 |
| 749 | Pope Gregory I | 540 | 604 | Religious figure | Italy | 82.64 | 531 | 94 | 305,063 | 4.24 |
| 750 | Pope Sylvester I | 300 | 335 | Religious figure | Italy | 82.64 | 764 | 84 | 222,149 | 3.19 |
| 751 | Erwin Rommel | 1891 | 1944 | Military personnel | Germany | 82.62 | 441 | 88 | 898,549 | 4.15 |
| 752 | Pope Innocent X | 1574 | 1655 | Religious figure | Italy | 82.62 | 1,336 | 74 | 218,526 | 2.83 |
| 753 | Ferenc Puskás | 1927 | 2006 | Soccer player | Hungary | 82.61 | 563 | 86 | 530,099 | 3.25 |
| 754 | Victor Emmanuel II of Italy | 1820 | 1878 | Politician | Italy | 82.61 | 938 | 77 | 480,545 | 3.25 |
| 755 | Thomas the Apostle | 1 | 72 | Religious figure | Israel | 82.61 | 800 | 82 | 396,090 | 4.13 |
| 756 | Deng Xiaoping | 1904 | 1997 | Politician | China | 82.61 | 567 | 106 | 1,091,637 | 4.62 |
| 757 | Charles X of France | 1757 | 1836 | Politician | France | 82.61 | 672 | 76 | 583,421 | 3.66 |
| 758 | Charles IV, Holy Roman Emperor | 1316 | 1378 | Politician | Czechia | 82.60 | 892 | 75 | 471,268 | 3.64 |
| 759 | Pope Gregory XV | 1554 | 1623 | Religious figure | Italy | 82.59 | 1,297 | 78 | 173,373 | 2.83 |
| 760 | Abu Nuwas | 762 | 814 | Writer | Iran | 82.59 | 865 | 142 | 160,044 | 5.13 |
| 761 | Michel Foucault | 1926 | 1984 | Philosopher | France | 82.59 | 649 | 93 | 684,959 | 3.81 |
| 762 | Bedřich Smetana | 1824 | 1884 | Composer | Czechia | 82.59 | 860 | 86 | 284,128 | 3.13 |
| 763 | Frederick II, Holy Roman Emperor | 1194 | 1250 | Politician | Italy | 82.59 | 608 | 77 | 590,095 | 3.63 |
| 764 | Mithridates VI of Pontus | 132 BC | 63 BC | Politician | Türkiye | 82.58 | 2,042 | 63 | 155,576 | 2.23 |
| 765 | Bill Gates | 1955 | – | Businessperson | United States | 82.58 | 666 | 172 | 1,905,995 | 6.32 |
| 766 | Charles Thomson Rees Wilson | 1869 | 1959 | Physicist | United Kingdom | 82.58 | 3,359 | 87 | 16,521 | 1.48 |
| 767 | Bartholomew the Apostle | 100 BC | 100 | Religious figure | Israel | 82.57 | 624 | 85 | 310,313 | 4.12 |
| 768 | Tokugawa Ieyasu | 1542 | 1616 | Military personnel | Japan | 82.57 | 1,256 | 76 | 906,886 | 4.04 |
| 769 | Murad IV | 1612 | 1640 | Politician | Türkiye | 82.57 | 396 | 71 | 686,786 | 3.73 |
| 770 | Manmohan Singh | 1932 | 2024 | Politician | Pakistan | 82.56 | 15,316 | 100 | 621,707 | 4.48 |
| 771 | Jacques Chirac | 1932 | 2019 | Politician | France | 82.56 | 740 | 130 | 765,745 | 5.08 |
| 772 | Diego Maradona | 1960 | 2020 | Soccer player | Argentina | 82.55 | 591 | 142 | 2,298,868 | 4.34 |
| 773 | Harold Harefoot | 1016 | 1040 | Nobleman | United Kingdom | 82.54 | 872 | 55 | 101,351 | 1.72 |
| 774 | David Lynch | 1946 | 2025 | Film director | United States | 82.53 | 2,880 | 85 | 4,543,631 | 4.74 |
| 775 | Jan van Eyck | 1395 | 1441 | Painter | Belgium | 82.52 | 631 | 79 | 209,617 | 3.25 |
| 776 | Bhumibol Adulyadej | 1927 | 2016 | Politician | United States | 82.52 | 1,251 | 131 | 609,570 | 5.37 |
| 777 | Mata Hari | 1876 | 1917 | Dancer | Netherlands | 82.51 | 1,016 | 78 | 648,754 | 3.34 |
| 778 | Kālidāsa | 400 | 420 | Writer | India | 82.51 | 2,526 | 137 | 193,750 | 4.86 |
| 779 | Richard Harris | 1930 | 2002 | Actor | Ireland | 82.51 | 3,737 | 66 | 741,962 | 2.45 |
| 780 | Owen Willans Richardson | 1879 | 1959 | Physicist | United Kingdom | 82.49 | 3,949 | 78 | 13,877 | 1.16 |
| 781 | Sonia Gandhi | 1946 | – | Politician | Italy | 82.49 | 770 | 83 | 127,481 | 2.03 |
| 782 | Federico Fellini | 1920 | 1993 | Film director | Italy | 82.49 | 626 | 127 | 462,332 | 4.45 |
| 783 | Pope Pius IV | 1499 | 1565 | Religious figure | Italy | 82.49 | 1,327 | 78 | 171,310 | 2.87 |
| 784 | Pope Urban II | 1042 | 1099 | Religious figure | France | 82.49 | 753 | 86 | 199,689 | 3.57 |
| 785 | Pope Gregory XII | 1335 | 1417 | Religious figure | Italy | 82.48 | 1,404 | 72 | 215,889 | 2.73 |
| 786 | Edgar Degas | 1834 | 1917 | Painter | France | 82.47 | 669 | 94 | 276,536 | 3.60 |
| 787 | Antonie van Leeuwenhoek | 1632 | 1723 | Biologist | Netherlands | 82.46 | 621 | 99 | 195,780 | 4.05 |
| 788 | George H. W. Bush | 1924 | 2018 | Politician | United States | 82.46 | 728 | 156 | 1,572,513 | 7.56 |
| 789 | Khalid ibn al-Walid | 592 | 642 | Military personnel | Saudi Arabia | 82.46 | 515 | 65 | 702,806 | 3.42 |
| 790 | Ingmar Bergman | 1918 | 2007 | Film director | Sweden | 82.46 | 222 | 134 | 466,780 | 5.11 |
| 791 | Vitruvius | 75 BC | 15 BC | Architect | Italy | 82.46 | 671 | 78 | 181,844 | 3.16 |
| 792 | Anni-Frid Lyngstad | 1945 | – | Singer | Norway | 82.46 | 703 | 63 | 629,967 | 2.31 |
| 793 | Maxim Gorky | 1868 | 1936 | Writer | Russia | 82.46 | 640 | 113 | 632,829 | 5.11 |
| 794 | Hosni Mubarak | 1928 | 2020 | Politician | Egypt | 82.43 | 710 | 116 | 514,382 | 4.52 |
| 795 | Abdul Hamid II | 1842 | 1918 | Politician | Türkiye | 82.43 | 537 | 88 | 828,867 | 4.04 |
| 796 | Ibn al-Haytham | 965 | 1039 | Physicist | Iraq | 82.42 | 1,129 | 89 | 248,174 | 4.02 |
| 797 | Möngke Khan | 1209 | 1259 | Politician | Iraq | 82.42 | 3,741 | 51 | 168,472 | 1.87 |
| 798 | Henry III of France | 1551 | 1589 | Politician | France | 82.41 | 707 | 71 | 528,973 | 3.37 |
| 799 | Du Fu | 712 | 770 | Writer | China | 82.41 | 876 | 117 | 181,772 | 4.64 |
| 800 | Ibrahim of the Ottoman Empire | 1615 | 1648 | Politician | Türkiye | 82.40 | 581 | 70 | 489,723 | 3.37 |
| 801 | Lev Yashin | 1929 | 1990 | Soccer player | Russia | 82.39 | 580 | 78 | 934,322 | 3.25 |
| 802 | Clovis I | 466 | 511 | Politician | Belgium | 82.38 | 467 | 86 | 404,212 | 4.05 |
| 803 | Jacques Offenbach | 1819 | 1880 | Composer | Germany | 82.37 | 891 | 92 | 163,206 | 3.10 |
| 804 | William Ewart Gladstone | 1809 | 1898 | Politician | United Kingdom | 82.36 | 11,942 | 77 | 90,016 | 2.19 |
| 805 | Girolamo Savonarola | 1452 | 1498 | Religious figure | Italy | 82.36 | 777 | 71 | 352,232 | 3.14 |
| 806 | Pope Paul V | 1552 | 1621 | Religious figure | Italy | 82.36 | 1,248 | 79 | 242,438 | 3.09 |
| 807 | Louis IX of France | 1214 | 1270 | Politician | France | 82.35 | 751 | 85 | 459,577 | 4.09 |
| 808 | Empress Matilda | 1102 | 1167 | Nobleman | United Kingdom | 82.35 | 3,070 | 64 | 155,290 | 2.36 |
| 809 | Heinrich Hertz | 1857 | 1894 | Physicist | Germany | 82.34 | 1,014 | 101 | 137,029 | 3.45 |
| 810 | Yuri Andropov | 1914 | 1984 | Politician | Russia | 82.33 | 785 | 99 | 759,549 | 4.20 |
| 811 | Henry Ford | 1863 | 1947 | Inventor | United States | 82.33 | 596 | 148 | 622,217 | 6.60 |
| 812 | Justin Martyr | 100 | 165 | Religious figure | NA | 82.33 | 7,436 | 57 | 101,439 | 1.95 |
| 813 | Gamal Abdel Nasser | 1918 | 1970 | Politician | Egypt | 82.33 | 571 | 110 | 733,745 | 4.53 |
| 814 | Dwight D. Eisenhower | 1890 | 1969 | Politician | United States | 82.31 | 610 | 146 | 1,244,214 | 7.22 |
| 815 | Jabir ibn Hayyan | 721 | 815 | Chemist | Iran | 82.30 | 992 | 89 | 249,084 | 3.92 |
| 816 | Vallabhbhai Patel | 1875 | 1950 | Politician | India | 82.30 | 4,995 | 76 | 213,258 | 2.58 |
| 817 | Draco | 650 BC | 600 BC | Public worker | Greece | 82.30 | 1,299 | 51 | 86,370 | 1.54 |
| 818 | Hannah Arendt | 1906 | 1975 | Philosopher | Germany | 82.29 | 597 | 91 | 741,753 | 3.81 |
| 819 | Pablo Neruda | 1904 | 1973 | Writer | Chile | 82.29 | 716 | 127 | 587,916 | 4.93 |
| 820 | Jean Piaget | 1896 | 1980 | Psychologist | Switzerland | 82.27 | 585 | 87 | 401,618 | 3.41 |
| 821 | Charles Martel | 688 | 741 | Military personnel | Belgium | 82.26 | 506 | 79 | 400,578 | 3.77 |
| 822 | Emperor Meiji | 1852 | 1912 | Politician | Japan | 82.26 | 689 | 83 | 675,715 | 4.00 |
| 823 | Pope Clement VIII | 1536 | 1605 | Religious figure | Italy | 82.25 | 1,173 | 73 | 204,314 | 2.87 |
| 824 | Danny DeVito | 1944 | – | Actor | United States | 82.24 | 696 | 82 | 575,556 | 2.83 |
| 825 | James Stewart | 1908 | 1997 | Actor | United States | 82.24 | 697 | 87 | 575,356 | 3.22 |
| 826 | Mikhail Bakunin | 1814 | 1876 | Philosopher | Russia | 82.22 | 688 | 92 | 271,797 | 3.45 |
| 827 | Bashar al-Assad | 1965 | – | Politician | Syria | 82.22 | 2,701 | 119 | 9,806,654 | 4.47 |
| 828 | Henri Bergson | 1859 | 1941 | Philosopher | France | 82.22 | 664 | 96 | 226,252 | 3.40 |
| 829 | Eva Braun | 1912 | 1945 | Companion | Germany | 82.22 | 808 | 81 | 1,050,949 | 4.01 |
| 830 | Prince Eugene of Savoy | 1663 | 1736 | Military personnel | France | 82.21 | 1,761 | 64 | 214,227 | 2.53 |
| 831 | Tacitus | 54 | 120 | Historian | France | 82.21 | 1,439 | 89 | 238,543 | 4.13 |
| 832 | Jacques Cartier | 1491 | 1557 | Explorer | France | 82.21 | 1,362 | 147 | 168,280 | 5.95 |
| 833 | Pope Clement XI | 1649 | 1721 | Religious figure | Italy | 82.21 | 1,821 | 75 | 229,185 | 2.89 |
| 834 | George Bernard Shaw | 1856 | 1950 | Writer | Ireland | 82.20 | 964 | 118 | 459,833 | 5.10 |
| 835 | Jerome | 345 | 420 | Religious figure | Serbia | 82.20 | 614 | 86 | 309,323 | 4.12 |
| 836 | Harun al-Rashid | 766 | 809 | Politician | Iran | 82.20 | 757 | 83 | 389,408 | 4.25 |
| 837 | Ay | 1380 BC | 1400 BC | Politician | Egypt | 82.19 | 1,358 | 52 | 120,503 | 1.79 |
| 838 | Gilbert du Motier, Marquis de Lafayette | 1757 | 1834 | Military personnel | France | 82.19 | 2,445 | 62 | 510,978 | 2.93 |
| 839 | Mustafa I | 1591 | 1639 | Politician | Türkiye | 82.18 | 569 | 70 | 520,682 | 3.41 |
| 840 | Barbara Bush | 1925 | 2018 | Politician | United States | 82.18 | 9,273 | 68 | 173,117 | 1.78 |
| 841 | Irène Joliot-Curie | 1897 | 1956 | Chemist | France | 82.18 | 784 | 99 | 331,691 | 3.63 |
| 842 | Joseph II, Holy Roman Emperor | 1741 | 1790 | Politician | Austria | 82.18 | 613 | 72 | 399,347 | 3.26 |
| 843 | Aspasia | 470 BC | 400 BC | Companion | Türkiye | 82.17 | 1,328 | 53 | 249,682 | 2.18 |
| 844 | Maurice Maeterlinck | 1862 | 1949 | Writer | Belgium | 82.17 | 916 | 93 | 112,468 | 2.66 |
| 845 | Alfred Hitchcock | 1899 | 1980 | Film director | United Kingdom | 82.16 | 442 | 145 | 785,199 | 6.25 |
| 846 | Marie Louise, Duchess of Parma | 1791 | 1847 | Companion | Austria | 82.16 | 432 | 61 | 382,454 | 2.50 |
| 847 | Pope Clement XIII | 1693 | 1769 | Religious figure | Italy | 82.16 | 1,560 | 74 | 272,327 | 2.96 |
| 848 | Masaccio | 1401 | 1428 | Painter | Italy | 82.16 | 767 | 74 | 116,628 | 2.70 |
| 849 | Kurt Vonnegut | 1922 | 2007 | Writer | United States | 82.15 | 4,588 | 83 | 248,438 | 2.75 |
| 850 | Maximilian I of Mexico | 1832 | 1867 | Politician | Austria | 82.14 | 1,507 | 59 | 1,229,224 | 3.13 |
| 851 | Pope Clement XIV | 1705 | 1774 | Religious figure | Italy | 82.13 | 1,707 | 73 | 304,404 | 2.91 |
| 852 | Lucrezia Borgia | 1480 | 1519 | Nobleman | Italy | 82.13 | 670 | 70 | 519,844 | 3.60 |
| 853 | Alexander II of Russia | 1818 | 1881 | Politician | Russia | 82.13 | 978 | 91 | 1,127,540 | 5.29 |
| 854 | Heraclius | 575 | 641 | Politician | Türkiye | 82.13 | 724 | 83 | 263,149 | 3.85 |
| 855 | Pope Sixtus IV | 1414 | 1484 | Religious figure | Italy | 82.12 | 789 | 76 | 245,141 | 3.16 |
| 856 | Pope Clement V | 1264 | 1314 | Religious figure | France | 82.11 | 1,204 | 70 | 199,461 | 2.74 |
| 857 | Luke the Evangelist | 31 | 84 | Religious figure | Türkiye | 82.11 | 561 | 82 | 402,377 | 3.19 |
| 858 | José Mujica | 1935 | 2025 | Politician | Uruguay | 82.11 | 1,591 | 91 | 2,601,916 | 4.67 |
| 859 | Jacques-Louis David | 1748 | 1825 | Painter | France | 82.11 | 687 | 85 | 249,550 | 3.51 |
| 860 | Anne, Princess Royal | 1950 | – | Nobleman | United Kingdom | 82.10 | 5,598 | 62 | 768,147 | 2.02 |
| 861 | Spartacus | 109 BC | 71 BC | Military personnel | Greece | 82.09 | 519 | 85 | 693,511 | 3.80 |
| 862 | Samuel | 1100 BC | 1010 BC | Religious figure | NA | 82.09 | 501 | 63 | 366,653 | 3.24 |
| 863 | Plotinus | 203 | 270 | Philosopher | Egypt | 82.09 | 648 | 77 | 165,466 | 3.19 |
| 864 | Ferdinand de Saussure | 1857 | 1913 | Linguist | Switzerland | 82.09 | 732 | 94 | 194,290 | 3.34 |
| 865 | Tom Jones | 1940 | – | Singer | United Kingdom | 82.08 | 10,834 | 58 | 460,594 | 2.04 |
| 866 | Lawrence Bragg | 1890 | 1971 | Physicist | Australia | 82.07 | 2,921 | 87 | 33,422 | 1.85 |
| 867 | Giorgio Vasari | 1511 | 1574 | Writer | Italy | 82.06 | 725 | 76 | 158,605 | 2.99 |
| 868 | Moses in Islam | 1392 BC | 1272 BC | Religious figure | Egypt | 82.06 | 1,223 | 40 | 266,976 | 1.63 |
| 869 | Jean-Baptiste Lamarck | 1744 | 1829 | Biologist | France | 82.06 | 733 | 89 | 180,478 | 3.34 |
| 870 | L. L. Zamenhof | 1859 | 1917 | Physician | Poland | 82.06 | 882 | 115 | 129,069 | 3.76 |
| 871 | Milan Kundera | 1929 | 2023 | Writer | Czechia | 82.06 | 594 | 83 | 306,105 | 2.82 |
| 872 | Xenophon | 430 BC | 354 BC | Historian | Greece | 82.05 | 630 | 90 | 199,214 | 4.05 |
| 873 | Pope Innocent VIII | 1432 | 1492 | Religious figure | Italy | 82.05 | 1,261 | 70 | 233,812 | 2.91 |
| 874 | Francisco Pizarro | 1478 | 1541 | Explorer | Spain | 82.05 | 684 | 87 | 321,266 | 3.95 |
| 875 | Christiaan Huygens | 1629 | 1695 | Physicist | Netherlands | 82.04 | 685 | 100 | 144,693 | 4.02 |
| 876 | Septimius Severus | 145 | 211 | Politician | Libya | 82.04 | 997 | 85 | 634,160 | 4.75 |
| 877 | Ip Man | 1893 | 1972 | Martial arts | China | 82.04 | 1,222 | 50 | 486,484 | 1.89 |
| 878 | Mohammad Reza Pahlavi | 1919 | 1980 | Politician | Iran | 82.03 | 628 | 98 | 1,634,168 | 4.74 |
| 879 | Anastasius I Dicorus | 430 | 518 | Politician | Albania | 82.03 | 2,778 | 59 | 69,093 | 1.82 |
| 880 | Dmitri Shostakovich | 1906 | 1975 | Composer | Russia | 82.02 | 885 | 82 | 575,677 | 3.41 |
| 881 | James Clerk Maxwell | 1831 | 1879 | Physicist | United Kingdom | 82.02 | 949 | 134 | 280,466 | 5.67 |
| 882 | Marie de' Medici | 1575 | 1642 | Nobleman | Italy | 82.02 | 1,831 | 65 | 313,201 | 2.94 |
| 883 | Saparmurat Niyazov | 1940 | 2006 | Politician | Turkmenistan | 82.01 | 4,021 | 84 | 242,431 | 2.79 |
| 884 | Methuselah | 3074 BC | 2105 BC | Religious figure | NA | 82.01 | 1,019 | 55 | 486,431 | 2.91 |
| 885 | Golda Meir | 1898 | 1978 | Politician | Ukraine | 82.01 | 423 | 100 | 524,621 | 4.29 |
| 886 | Æthelwulf, King of Wessex | 795 | 858 | Politician | Germany | 82.01 | 5,020 | 46 | 106,164 | 1.46 |
| 887 | Pope Alexander VIII | 1610 | 1691 | Religious figure | Italy | 82.00 | 1,750 | 73 | 188,515 | 2.83 |
| 888 | Louis de Broglie | 1892 | 1987 | Physicist | France | 82.00 | 3,076 | 93 | 113,553 | 2.86 |
| 889 | Pope Innocent XII | 1615 | 1700 | Religious figure | Italy | 81.98 | 1,687 | 73 | 206,616 | 2.88 |
| 890 | Warren Buffett | 1930 | – | Businessperson | United States | 81.98 | 1,069 | 102 | 1,638,217 | 5.47 |
| 891 | Pope Julius III | 1487 | 1555 | Religious figure | Italy | 81.98 | 1,393 | 74 | 188,170 | 2.88 |
| 892 | Louis Braille | 1809 | 1852 | Inventor | France | 81.98 | 714 | 87 | 183,111 | 3.44 |
| 893 | Muhammad Ali of Egypt | 1769 | 1849 | Politician | Greece | 81.97 | 838 | 70 | 430,364 | 3.26 |
| 894 | Tintoretto | 1518 | 1594 | Painter | Italy | 81.96 | 859 | 76 | 136,638 | 2.88 |
| 895 | Livy | 59 BC | 17 | Historian | Italy | 81.96 | 775 | 87 | 172,923 | 3.70 |
| 896 | Saul | 1079 BC | 1010 BC | Religious figure | Israel | 81.96 | 468 | 68 | 498,675 | 3.78 |
| 897 | Heinrich Heine | 1797 | 1856 | Writer | Germany | 81.96 | 566 | 97 | 323,248 | 4.08 |
| 898 | Richard Burton | 1925 | 1984 | Actor | United Kingdom | 81.95 | 618 | 74 | 503,445 | 2.81 |
| 899 | Louisa May Alcott | 1832 | 1888 | Writer | United States | 81.95 | 6,694 | 73 | 167,702 | 2.34 |
| 900 | Mehmed IV | 1642 | 1693 | Politician | Türkiye | 81.94 | 587 | 68 | 417,364 | 3.16 |
| 901 | Erich Maria Remarque | 1898 | 1970 | Writer | Germany | 81.94 | 782 | 93 | 552,493 | 3.84 |
| 902 | Pope Gregory VII | 1020 | 1085 | Religious figure | Italy | 81.93 | 850 | 79 | 201,925 | 3.36 |
| 903 | Jean-Paul Belmondo | 1933 | 2021 | Actor | France | 81.93 | 653 | 93 | 672,858 | 3.59 |
| 904 | Patrick Swayze | 1952 | 2009 | Actor | United States | 81.93 | 799 | 74 | 1,329,462 | 2.59 |
| 905 | Edgar de Wahl | 1867 | 1948 | Linguist | Ukraine | 81.92 | 2,974 | 102 | 8,070 | 1.77 |
| 906 | Charles Lindbergh | 1902 | 1974 | Pilot | United States | 81.92 | 746 | 74 | 323,736 | 2.55 |
| 907 | Saint Timothy | 17 | 97 | Religious figure | Türkiye | 81.91 | 5,528 | 52 | 105,277 | 1.69 |
| 908 | Enver Hoxha | 1908 | 1985 | Politician | Albania | 81.91 | 798 | 91 | 423,694 | 3.72 |
| 909 | Konrad Adenauer | 1876 | 1967 | Politician | Germany | 81.91 | 909 | 114 | 696,127 | 5.50 |
| 910 | Frederik IX | 1899 | 1972 | Politician | Denmark | 81.91 | 1,386 | 62 | 169,942 | 1.81 |
| 911 | Pope Alexander VII | 1599 | 1667 | Religious figure | Italy | 81.91 | 1,427 | 72 | 197,477 | 2.79 |
| 912 | Paul von Hindenburg | 1847 | 1934 | Politician | Poland | 81.91 | 658 | 86 | 776,213 | 4.19 |
| 913 | Pope Marcellus II | 1501 | 1555 | Religious figure | Italy | 81.90 | 1,576 | 69 | 184,969 | 2.66 |
| 914 | Mehmed I | 1386 | 1421 | Politician | Türkiye | 81.90 | 715 | 69 | 353,981 | 3.29 |
| 915 | Ursula K. Le Guin | 1929 | 2018 | Writer | United States | 81.89 | 7,240 | 82 | 260,877 | 2.52 |
| 916 | Alfredo Di Stéfano | 1926 | 2014 | Soccer player | Argentina | 81.89 | 768 | 78 | 642,096 | 3.18 |
| 917 | Helen Keller | 1880 | 1968 | Social activist | United States | 81.88 | 758 | 109 | 983,257 | 5.66 |
| 918 | Louis de Funès | 1914 | 1983 | Actor | France | 81.86 | 642 | 87 | 886,592 | 3.81 |
| 919 | Karl Popper | 1902 | 1994 | Philosopher | Austria | 81.86 | 667 | 92 | 364,530 | 3.63 |
| 920 | Isaac Asimov | 1920 | 1992 | Writer | Russia | 81.85 | 674 | 118 | 786,344 | 5.25 |
| 921 | Elagabalus | 203 | 222 | Politician | Syria | 81.84 | 957 | 79 | 563,926 | 4.36 |
| 922 | Ramakrishna | 1836 | 1886 | Philosopher | India | 81.84 | 1,040 | 82 | 136,578 | 2.82 |
| 923 | Ludwig Mies van der Rohe | 1886 | 1969 | Architect | Germany | 81.84 | 3,030 | 74 | 213,518 | 2.48 |
| 924 | Olav V of Norway | 1903 | 1991 | Politician | United Kingdom | 81.84 | 736 | 61 | 239,813 | 1.94 |
| 925 | Gustave Courbet | 1819 | 1877 | Painter | France | 81.84 | 772 | 72 | 263,744 | 2.77 |
| 926 | Jackie Chan | 1954 | – | Actor | Hong Kong | 81.82 | 656 | 144 | 2,130,589 | 5.70 |
| 927 | Edward the Martyr | 962 | 978 | Politician | United Kingdom | 81.82 | 6,980 | 52 | 82,912 | 1.62 |
| 928 | Paulo Coelho | 1947 | – | Writer | Brazil | 81.81 | 857 | 97 | 408,801 | 3.32 |
| 929 | Virginia Woolf | 1882 | 1941 | Writer | United Kingdom | 81.81 | 856 | 115 | 757,317 | 5.35 |
| 930 | Guy de Maupassant | 1850 | 1893 | Writer | France | 81.81 | 1,013 | 102 | 481,475 | 4.89 |
| 931 | Hendrik Lorentz | 1853 | 1928 | Physicist | Netherlands | 81.81 | 1,045 | 104 | 99,057 | 3.59 |
| 932 | Catherine of Aragon | 1485 | 1536 | Religious figure | Spain | 81.80 | 940 | 75 | 914,454 | 4.81 |
| 933 | Kofi Annan | 1938 | 2018 | Diplomat | Ghana | 81.80 | 899 | 139 | 269,730 | 5.24 |
| 934 | William the Conqueror | 1028 | 1087 | Nobleman | France | 81.79 | 694 | 102 | 730,592 | 5.85 |
| 935 | Pope Formosus | 816 | 896 | Religious figure | Italy | 81.79 | 1,163 | 72 | 221,446 | 2.97 |
| 936 | Pope Paul IV | 1476 | 1559 | Religious figure | Italy | 81.79 | 1,405 | 73 | 192,726 | 2.92 |
| 937 | B.B. King | 1925 | 2015 | Musician | United States | 81.79 | 3,483 | 83 | 221,009 | 2.53 |
| 938 | Lucius Verus | 130 | 169 | Politician | Italy | 81.78 | 1,839 | 69 | 478,751 | 3.72 |
| 939 | Slobodan Milošević | 1941 | 2006 | Politician | Serbia | 81.78 | 1,036 | 86 | 626,201 | 3.83 |
| 940 | Pope Callixtus III | 1379 | 1458 | Religious figure | Spain | 81.78 | 1,383 | 77 | 215,814 | 3.25 |
| 941 | Pratibha Patil | 1934 | – | Politician | India | 81.77 | 13,799 | 87 | 84,029 | 2.36 |
| 942 | Augusto Pinochet | 1915 | 2006 | Politician | Chile | 81.77 | 526 | 101 | 768,661 | 4.51 |
| 943 | Mahavira | 599 BC | 527 BC | Religious figure | India | 81.77 | 1,186 | 78 | 197,687 | 3.88 |
| 944 | Alexandre Dumas fils | 1824 | 1895 | Writer | France | 81.76 | 1,124 | 68 | 279,600 | 2.62 |
| 945 | Miyamoto Musashi | 1584 | 1645 | Writer | Japan | 81.76 | 668 | 73 | 575,046 | 3.90 |
| 946 | Louis Philippe I | 1773 | 1850 | Politician | France | 81.75 | 639 | 78 | 630,530 | 3.78 |
| 947 | Brigham Young | 1801 | 1877 | Religious figure | United States | 81.74 | 2,231 | 52 | 515,556 | 2.25 |
| 948 | Arthur Rimbaud | 1854 | 1891 | Writer | France | 81.74 | 632 | 104 | 586,938 | 4.58 |
| 949 | Reinhard Heydrich | 1904 | 1942 | Politician | Germany | 81.74 | 802 | 72 | 1,075,615 | 3.62 |
| 950 | Ennio Morricone | 1928 | 2020 | Composer | Italy | 81.73 | 722 | 85 | 597,209 | 3.38 |
| 951 | François Rabelais | 1494 | 1553 | Writer | France | 81.73 | 651 | 91 | 216,561 | 4.07 |
| 952 | Jack London | 1876 | 1916 | Writer | United States | 81.73 | 759 | 96 | 466,992 | 4.19 |
| 953 | Charles I of Austria | 1887 | 1922 | Politician | Austria | 81.72 | 1,017 | 65 | 778,699 | 3.26 |
| 954 | Darius III | 380 BC | 330 BC | Politician | Iran | 81.71 | 718 | 76 | 234,262 | 3.52 |
| 955 | Francis Drake | 1540 | 1596 | Explorer | United Kingdom | 81.71 | 641 | 110 | 345,878 | 5.49 |
| 956 | Knut Hamsun | 1859 | 1952 | Writer | Norway | 81.71 | 706 | 103 | 139,118 | 3.41 |
| 957 | Stanley Kubrick | 1928 | 1999 | Film director | United States | 81.71 | 655 | 131 | 1,036,837 | 5.99 |
| 958 | Demosthenes | 384 BC | 322 BC | Politician | Greece | 81.70 | 678 | 74 | 163,758 | 3.19 |
| 959 | Louis XII of France | 1462 | 1515 | Politician | France | 81.70 | 1,068 | 76 | 332,146 | 3.84 |
| 960 | Wu Zetian | 624 | 705 | Politician | China | 81.68 | 930 | 66 | 730,466 | 3.58 |
| 961 | Mimar Sinan | 1490 | 1588 | Architect | Türkiye | 81.67 | 843 | 129 | 306,753 | 6.08 |
| 962 | Amedeo Avogadro | 1776 | 1856 | Chemist | Italy | 81.67 | 895 | 92 | 100,818 | 3.20 |
| 963 | Oskar Schindler | 1908 | 1974 | Businessperson | Czechia | 81.66 | 817 | 73 | 1,242,701 | 3.72 |
| 964 | Jude the Apostle | 15 | 70 | Religious figure | Israel | 81.66 | 928 | 79 | 504,558 | 4.24 |
| 965 | Jacob Bernoulli | 1654 | 1705 | Mathematician | Switzerland | 81.66 | 4,936 | 72 | 58,562 | 2.09 |
| 966 | Robin Williams | 1951 | 2014 | Comedian | United States | 81.66 | 868 | 133 | 2,495,755 | 5.97 |
| 967 | Alphonse Mucha | 1860 | 1939 | Painter | Czechia | 81.66 | 1,410 | 62 | 325,354 | 2.29 |
| 968 | Zeno of Elea | 490 BC | 425 BC | Philosopher | Italy | 81.64 | 675 | 78 | 129,401 | 3.30 |
| 969 | Zhuang Zhou | 369 BC | 286 BC | Philosopher | China | 81.63 | 1,451 | 70 | 179,898 | 2.98 |
| 970 | Henry II of France | 1519 | 1559 | Politician | France | 81.63 | 907 | 71 | 504,419 | 3.73 |
| 971 | Hayreddin Barbarossa | 1478 | 1546 | Pirate | Greece | 81.62 | 605 | 63 | 309,410 | 2.84 |
| 972 | Vasily Zaitsev | 1915 | 1991 | Military personnel | Russia | 81.62 | 1,796 | 51 | 369,394 | 1.92 |
| 973 | Ferdinand I of Austria | 1793 | 1875 | Politician | Austria | 81.62 | 854 | 63 | 390,317 | 2.86 |
| 974 | Pope Gregory XIV | 1535 | 1591 | Religious figure | Italy | 81.61 | 1,679 | 73 | 147,969 | 2.83 |
| 975 | Mihrimah Sultan | 1522 | 1578 | Companion | Türkiye | 81.60 | 721 | 45 | 399,379 | 2.20 |
| 976 | Babur | 1483 | 1530 | Politician | Uzbekistan | 81.60 | 673 | 94 | 664,021 | 5.06 |
| 977 | W. Somerset Maugham | 1874 | 1965 | Writer | France | 81.60 | 5,986 | 76 | 216,461 | 2.91 |
| 978 | Naruhito | 1960 | – | Nobleman | Japan | 81.60 | 1,308 | 181 | 1,277,797 | 5.26 |
| 979 | Pāṇini | 500 BC | 460 BC | Linguist | Pakistan | 81.60 | 5,848 | 70 | 60,892 | 2.58 |
| 980 | Charles Babbage | 1791 | 1871 | Inventor | United Kingdom | 81.59 | 695 | 98 | 315,125 | 4.59 |
| 981 | António de Oliveira Salazar | 1889 | 1970 | Politician | Portugal | 81.59 | 778 | 84 | 492,890 | 3.42 |
| 982 | Antoninus Pius | 86 | 161 | Politician | Italy | 81.59 | 875 | 88 | 292,696 | 4.35 |
| 983 | Tomyris | 600 BC | 600 BC | Politician | Kazakhstan | 81.59 | 741 | 56 | 346,789 | 2.59 |
| 984 | John Glenn | 1921 | 2016 | Astronaut | United States | 81.58 | 7,006 | 76 | 165,793 | 2.27 |
| 985 | Romulus Augustulus | 460 | 527 | Military personnel | Serbia | 81.58 | 1,588 | 81 | 262,850 | 3.84 |
| 986 | David Ben-Gurion | 1886 | 1973 | Politician | Poland | 81.57 | 491 | 104 | 492,490 | 4.58 |
| 987 | Ezekiel | 621 BC | 569 BC | Religious figure | Israel | 81.57 | 840 | 62 | 288,938 | 3.09 |
| 988 | Jean le Rond d'Alembert | 1717 | 1783 | Mathematician | France | 81.57 | 1,108 | 87 | 92,662 | 2.94 |
| 989 | Catherine of Alexandria | 287 | 305 | Religious figure | Egypt | 81.57 | 510 | 62 | 276,826 | 3.06 |
| 990 | A. P. J. Abdul Kalam | 1931 | 2015 | Politician | India | 81.57 | 704 | 85 | 461,017 | 3.39 |
| 991 | Louis the Pious | 778 | 840 | Politician | France | 81.56 | 702 | 82 | 274,081 | 3.84 |
| 992 | Al Capone | 1899 | 1947 | Mafioso | United States | 81.56 | 827 | 82 | 1,308,934 | 4.55 |
| 993 | Pope Urban V | 1310 | 1370 | Religious figure | France | 81.56 | 1,464 | 74 | 114,406 | 2.70 |
| 994 | Margaret I of Denmark | 1353 | 1412 | Politician | Denmark | 81.56 | 1,824 | 60 | 124,715 | 2.21 |
| 995 | Francis Xavier | 1506 | 1552 | Religious figure | Spain | 81.55 | 883 | 77 | 400,991 | 3.91 |
| 996 | Mary Pickford | 1892 | 1979 | Actor | Canada | 81.55 | 10,101 | 88 | 123,773 | 2.53 |
| 997 | Princess Alice of Battenberg | 1885 | 1969 | Nobleman | United Kingdom | 81.55 | 5,522 | 47 | 357,639 | 1.73 |
| 998 | Epictetus | 50 | 135 | Philosopher | Türkiye | 81.53 | 790 | 70 | 270,777 | 3.39 |
| 999 | Pope Clement VI | 1291 | 1352 | Religious figure | France | 81.53 | 1,563 | 71 | 118,379 | 2.62 |
| 1000 | Olaf II of Norway | 993 | 1030 | Politician | Norway | 81.52 | 3,470 | 47 | 107,697 | 1.61 |
| 1001 | Thomas More | 1478 | 1535 | Philosopher | United Kingdom | 81.52 | 661 | 97 | 505,578 | 5.49 |
| 1002 | Alvar Aalto | 1898 | 1976 | Architect | Finland | 81.52 | 780 | 84 | 150,835 | 2.65 |
| 1003 | Ursula von der Leyen | 1958 | – | Politician | Belgium | 81.50 | 1,282 | 96 | 2,305,721 | 3.25 |
| 1004 | Stephen King | 1947 | – | Writer | United States | 81.49 | 906 | 111 | 1,373,833 | 5.12 |
| 1005 | Pope Nicholas V | 1397 | 1455 | Religious figure | Italy | 81.49 | 1,711 | 75 | 155,487 | 3.08 |
| 1006 | Madame de Pompadour | 1721 | 1764 | Companion | France | 81.49 | 539 | 56 | 409,924 | 2.63 |
| 1007 | Alexandra Feodorovna | 1872 | 1918 | Nobleman | Germany | 81.49 | 2,960 | 58 | 501,925 | 2.66 |
| 1008 | Henri Poincaré | 1854 | 1912 | Mathematician | France | 81.48 | 1,070 | 96 | 197,796 | 3.66 |
| 1009 | Aleksandr Solzhenitsyn | 1918 | 2008 | Writer | Russia | 81.48 | 744 | 119 | 567,721 | 4.96 |
| 1010 | Amitabh Bachchan | 1942 | – | Actor | India | 81.47 | 545 | 113 | 392,153 | 4.33 |
| 1011 | Wangari Maathai | 1940 | 2011 | Politician | Kenya | 81.47 | 3,001 | 103 | 112,641 | 2.84 |
| 1012 | Balian of Ibelin | 1143 | 1193 | Politician | NA | 81.46 | 5,806 | 34 | 311,539 | 1.43 |
| 1013 | Joseph Lister | 1827 | 1912 | Physician | United Kingdom | 81.46 | 7,122 | 73 | 58,008 | 2.05 |
| 1014 | Pope John XXII | 1244 | 1334 | Religious figure | France | 81.45 | 1,267 | 71 | 202,200 | 2.83 |
| 1015 | Rudolf Hess | 1894 | 1987 | Politician | Egypt | 81.45 | 887 | 68 | 986,441 | 3.51 |
| 1016 | Paolo Veronese | 1528 | 1588 | Painter | Italy | 81.44 | 1,091 | 70 | 109,663 | 2.55 |
| 1017 | Pope Clement X | 1590 | 1676 | Religious figure | Italy | 81.44 | 1,609 | 74 | 178,146 | 2.93 |
| 1018 | Luiz Inácio Lula da Silva | 1945 | – | Politician | Brazil | 81.43 | 994 | 125 | 989,720 | 5.21 |
| 1019 | Güyük Khan | 1206 | 1248 | Politician | NA | 81.42 | 4,130 | 50 | 122,567 | 1.84 |
| 1020 | Maimonides | 1138 | 1204 | Religious figure | Spain | 81.42 | 867 | 87 | 283,057 | 4.20 |
| 1021 | Pope Clement IX | 1600 | 1669 | Religious figure | Italy | 81.41 | 1,526 | 73 | 179,002 | 2.87 |
| 1022 | Martin of Tours | 316 | 397 | Religious figure | Hungary | 81.41 | 401 | 75 | 208,156 | 3.18 |
| 1023 | Eusébio | 1942 | 2014 | Soccer player | Mozambique | 81.41 | 849 | 88 | 381,566 | 3.24 |
| 1024 | Johann Gottlieb Fichte | 1762 | 1814 | Philosopher | Germany | 81.40 | 933 | 80 | 134,862 | 2.92 |
| 1025 | Antonio Stradivari | 1644 | 1737 | Designer | Italy | 81.39 | 793 | 62 | 226,249 | 2.59 |
| 1026 | Nurbanu Sultan | 1525 | 1583 | Companion | Greece | 81.39 | 847 | 47 | 352,773 | 2.22 |
| 1027 | George Soros | 1930 | – | Businessperson | Hungary | 81.39 | 1,365 | 81 | 1,768,245 | 4.77 |
| 1028 | Constantine XI Palaiologos | 1404 | 1453 | Politician | Türkiye | 81.38 | 1,189 | 69 | 378,457 | 3.73 |
| 1029 | Pope Boniface VIII | 1235 | 1303 | Religious figure | Italy | 81.37 | 1,107 | 73 | 296,259 | 3.35 |
| 1030 | Ali Khamenei | 1939 | 2026 | Politician | Iran | 81.36 | 699 | 101 | 1,787,354 | 5.13 |
| 1031 | Caitlyn Jenner | 1949 | – | Celebrity | United States | 81.36 | 941 | 53 | 914,806 | 1.96 |
| 1032 | Huldrych Zwingli | 1484 | 1531 | Religious figure | Switzerland | 81.35 | 1,004 | 86 | 131,266 | 3.69 |
| 1033 | Klara Hitler | 1860 | 1907 | Companion | Austria | 81.35 | 760 | 52 | 281,829 | 1.96 |
| 1034 | Sarah Bernhardt | 1844 | 1923 | Actor | France | 81.34 | 599 | 162 | 535,061 | 6.83 |
| 1035 | Marquis de Sade | 1740 | 1814 | Writer | France | 81.34 | 807 | 74 | 563,466 | 3.87 |
| 1036 | Niki Lauda | 1949 | 2019 | Racing driver | Austria | 81.34 | 1,342 | 71 | 1,637,372 | 3.24 |
| 1037 | Pierre-Simon Laplace | 1749 | 1827 | Mathematician | France | 81.34 | 805 | 103 | 171,588 | 4.18 |
| 1038 | Bahá'u'lláh | 1817 | 1892 | Religious figure | Iran | 81.34 | 3,169 | 86 | 179,278 | 3.64 |
| 1039 | Pope Innocent IX | 1519 | 1591 | Religious figure | Italy | 81.33 | 1,650 | 67 | 147,843 | 2.69 |
| 1040 | Pope Innocent VI | 1282 | 1362 | Religious figure | France | 81.33 | 1,835 | 70 | 93,612 | 2.53 |
| 1041 | José Saramago | 1922 | 2010 | Writer | Portugal | 81.32 | 727 | 109 | 292,682 | 3.76 |
| 1042 | Anwar Sadat | 1918 | 1981 | Politician | Egypt | 81.32 | 683 | 106 | 582,694 | 4.52 |
| 1043 | Václav Havel | 1936 | 2011 | Writer | Czechia | 81.32 | 627 | 110 | 314,894 | 3.97 |
| 1044 | Nasreddin | 1208 | 1284 | Comedian | Türkiye | 81.31 | – | 75 | 60,508 | 1.90 |
| 1045 | Philip the Apostle | 5 | 80 | Religious figure | NA | 81.30 | 923 | 74 | 185,064 | 3.51 |
| 1046 | John D. Rockefeller | 1839 | 1937 | Businessperson | United States | 81.30 | 934 | 79 | 849,026 | 4.39 |
| 1047 | Philip I of Castile | 1478 | 1506 | Politician | Belgium | 81.29 | 1,382 | 56 | 383,742 | 2.94 |
| 1048 | Baba Vanga | 1911 | 1996 | Occultist | North Macedonia | 81.29 | 1,412 | 61 | 668,913 | 3.11 |
| 1049 | Hu Jintao | 1942 | – | Politician | China | 81.29 | 995 | 108 | 999,228 | 4.87 |
| 1050 | Carl Gustaf Emil Mannerheim | 1867 | 1951 | Politician | Finland | 81.28 | 1,564 | 78 | 383,405 | 3.37 |
| 1051 | Pope-elect Stephen | 700 | 752 | Religious figure | Italy | 81.28 | 4,249 | 57 | 207,583 | 2.35 |
| 1052 | Alexander III of Russia | 1845 | 1894 | Politician | Russia | 81.27 | 810 | 88 | 997,168 | 4.62 |
| 1053 | Bartholomew I of Constantinople | 1940 | – | Religious figure | Türkiye | 81.27 | 2,767 | 57 | 279,180 | 1.85 |
| 1054 | Erich Fromm | 1900 | 1980 | Psychologist | Germany | 81.27 | 912 | 70 | 311,127 | 2.67 |
| 1055 | Zhu Xi | 1130 | 1200 | Philosopher | China | 81.27 | 1,768 | 109 | 107,671 | 4.28 |
| 1056 | Park Chung-hee | 1917 | 1979 | Politician | South Korea | 81.27 | 1,142 | 86 | 736,248 | 3.67 |
| 1057 | Ambrose | 340 | 397 | Religious figure | Germany | 81.26 | 886 | 76 | 217,527 | 3.50 |
| 1058 | Pope Innocent XIII | 1655 | 1724 | Religious figure | Italy | 81.26 | 1,712 | 74 | 246,996 | 3.10 |
| 1059 | John Chrysostom | 349 | 407 | Religious figure | Türkiye | 81.25 | 686 | 72 | 227,901 | 3.54 |
| 1060 | Anatole France | 1844 | 1924 | Writer | France | 81.25 | 990 | 96 | 153,947 | 3.49 |
| 1061 | Esther | 600 BC | 500 BC | Religious figure | Iran | 81.25 | 1,043 | 60 | 354,838 | 3.06 |
| 1062 | Albertus Magnus | 1206 | 1280 | Religious figure | Germany | 81.25 | 946 | 74 | 143,837 | 3.20 |
| 1063 | Flavius Aetius | 390 | 454 | Military personnel | Bulgaria | 81.25 | 1,717 | 64 | 121,947 | 2.55 |
| 1064 | Beatrix of the Netherlands | 1938 | – | Politician | Netherlands | 81.24 | 1,060 | 94 | 464,755 | 3.81 |
| 1065 | Marina Abramović | 1946 | – | Artist | Serbia | 81.24 | 6,431 | 56 | 511,929 | 2.05 |
| 1066 | François Mitterrand | 1916 | 1996 | Politician | France | 81.24 | 869 | 109 | 646,108 | 4.81 |
| 1067 | Carlo Ancelotti | 1959 | – | Coach | Italy | 81.23 | 1,441 | 78 | 3,963,319 | 3.09 |
