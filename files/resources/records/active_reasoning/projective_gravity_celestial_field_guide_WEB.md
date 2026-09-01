*Here's a note from Ajax:* Ok hello! So what this document is is a snippet of some of my active reasoning dynamical ideas I'm trying to string together. Specifically how it was made was that on August 31, 2026 and the week leading up to it I inputted about a dozen different intuitive constraints into Claude that I had been building up to throughout 2026. Note that in my journal entries I have the records of all of these intuitions as I first stated them months ago through more recently, plus the actual prompts to Claude itself in which I reveal them. A couple of examples are that I was really stuck two months ago with trying to imagine in my 3-sphere model a kind of "shaft" of matter to get at the kind of antipodal-pair dynamics I was looking for, however in quick succession over a couple of days in early August I had the thought that I could instead just use equivalence classes over lines in R4 space, then use the EFEs as a constraint ON THOSE LINES IN THE DEEPER SPACE, and then simply have the base space to it as a kind of RP3 over which orbits actually occur gravitationally. So yeah, basically the process was me having hidden biases in my reasoning together with a clear win condition, and then me gradually figuring out how to shed the biases to bring out the highlights in the win condition. And, well, that brings us to right now---only after I had all these constraints, (like for example I had intuited already that the fibers "bunch up" around mass so as to keep the primary object in the idealized model as defining the "radial direction" for the fibers while at once not actually contributing to the gravity dynamics directly accordingly, so it was meant to be a kind of trade-off between the primary and secondary following the same law while the secondary itself feels the effects of it only and then within those effects actual EFE stuff getting their scope---so yeah to be clear I entirely established the intricate graph-structure of constraints and then fed THAT into the AI, since I can make those graphs due to the months of bias-shedding, while it can simply implement them rather than create them), did I feed them as prompts into Claude, and ecstatically I got to watch it render them into real equations by deducing from what I had set up as well as formalizing some of my looser intuitions (like "bunching" became "dielectric" after my guess to the AI that it might be Poisson's equation was wrong). But yeah, I have all the records of everything in case there's ever a question, but to be clear I'm a guy who designed a very specific painting in my head without owning the paint to actually draw it in equations. Claude provided that paint, and indeed corrected some of my formalism guesses of the constraints, but the painting existed well before Claude painted it. (And indeed I still have a bunch of biases as we speak in things that didn’t yet make it into this brief doc here, as even in the last couple of days I shifted associating one thing with the total space to associating it with the base space, which gives me another angle on inductively landing the next unification of two concepts in the sequence. So in other words it’s still an ongoing process, so much of what will show up in the next draft is something I already have intuited right now, but just haven’t rendered and posted yet).

# Projective Gravity — The Minimal Theory

### A Field Guide, fourth edition

> **Status tags.** **[V]** verified symbolically or numerically in this program · **[M]** measured in a numerical experiment (softened potentials, 2D slices unless noted) · **[T]** established theorem, cited · **[D]** derived here from **[V]/[T]** material · **[S]** sketch · **[O]** open.
>
> **Conventions.** $G = c = 1$ unless restored; $\ell$ = radius of the base 3-sphere; "total space" = the higher-dimensional arena where matter lives; "base" = the space of fibers, where gravity lives.
>
> **Reading guide.** Why the fibration exists and why it is rigid: §0.6. The idea and its purpose: §0–§0.5. Why it must not be sourced: §6. Gravity and the stabilized dilaton (the result that saves the theory): §7, §7.5. The Machian relation and what it does and does not deliver: §10. The postulate's consistency and its price: §9.5; the one observable it will eventually face: §9.6. Electrodynamics: §12.5. What the celestial detour taught: §13.
>
> **What this theory is.** Kaluza–Klein on $\mathbb{R}_t\times S^1_u\times S^3$ with a **topologically rigid fibration**, a stabilized massive radion, and one postulate: **gravity reads the fiber average.** That postulate is the entire departure from general relativity. **The theory is internally consistent** (§9.5: the Bianchi identity closes, the source descends to the quotient conserved, and on the quotient it is an ordinary local causal field theory). Its status with respect to *our* universe is a separate question: this guide is a **drafting-phase** document for a fiber-based projective idea, not a cosmology, and it has no perturbation theory on an expanding background. §9.6 records the one observable the idea will eventually have to face — a bias-free lensing–clustering statistic — as a *signpost*, with the naive extrapolation and the current data both stated, and with the explicit caveat that the extrapolation is heuristic. The fibration is not sourced by matter and does not respond to it — it is supplied by the winding of a compact scalar, and its existence is a fact about the arena. Earlier editions coupled matter to the fibration as a permittivity; that coupling is bounded by the constancy of the fine-structure constant to be unobservable (§12.5) and has been removed.

---

## 0 · The idea in one paragraph

Gravity lives not on spacetime's full arena but on the **space of fibers** of a foliation; matter inhabits the total space, and gravity sees only its fiber-averaged projection. The founding example fibers Euclidean $\mathbb{R}^4$ by lines through the origin, with base $S^3/\pm = \mathbb{RP}^3$: each line meets the physical 3-sphere at two antipodal points, so the base cannot tell them apart. The first formulation coupled the fibration field to matter as a *charge* and failed catastrophically — every gravitating object captured the fibers around it and smeared into fog (§6.1). The repair is structural: **the fibration is not sourced at all.** It is supplied topologically by the winding of a compact scalar, legal precisely because $\chi(S^1\times S^3) = 0$. Nothing terminates fiber lines, so localized masses and Keplerian orbits survive; and everything the theory derives — the cone-generated $\Lambda$, the Kaluza–Klein reduction, the two-population geodesics, the emergent $G$, the antipodal twin — follows from the arena and the projective postulate, never from a coupling.

## 0.5 · The seed, and what it is for

The founding requirement — the *seed* — is stated here exactly, because a later formulation lost it and the loss was decisive.

> **The seed.** Place a star at a point $\hat n$ of the physical 3-sphere inside the total space. Travel to the antipode $-\hat n$. **There is nothing there** — no matter, nothing to emit, absorb, or reflect light. Yet the base point $[\hat n] = \{\hat n, -\hat n\}$ carries the star's mass, so gravity, living on the base, acts at $-\hat n$ exactly as it acts at $\hat n$. *The star speaks gravitationally for every point of its fiber, and materially for one.*

**Its purpose is dark matter.** If light propagates in the total space while gravity reads the base, then every luminous mass has a projection-image that gravitates and lenses but neither emits, absorbs, nor scatters — the observed phenomenology of dark matter, produced by the geometry of the projection rather than by a new particle. Section 12 states this as a prediction with its tensions.

**The condition the seed imposes** on any formulation, stated as a theorem-shaped requirement **[D]**: a projection $\pi: E\to B$ with (i) matter on $E$, localized on a fiber; (ii) gravity on $B$ sourced by the fiber-integral of matter; (iii) **each fiber meeting physical 3-space at more than one point.** Conditions (ii)+(iii) together say $G_{\mu\nu} = 8\pi\langle T_{\mu\nu}\rangle_{\rm fiber}$ — gravity sourced by the *orbit-averaged* stress tensor, a genuine nonlocal modification of general relativity. **That modification is the projective postulate.** A formulation in which the postulate becomes automatic (§13) has lost the seed.

---

## 0.6 · Why the fibration exists, and why it is rigid

**The cylinder is the fibration [T].** In polar form $\mathbb{R}^4\setminus\{0\}$ is conformally a cylinder:

$$ds^2 = dr^2 + r^2 d\Omega_3^2 = e^{2u}\big[du^2 + d\Omega_3^2\big], \qquad u = \ln r$$

so the **radial direction becomes $\partial_u$**, globally defined and nowhere vanishing because the manifold is a product. The fibration exists for the same reason the cylinder is a cylinder. It is a property of the arena, not of the matter in it — and that is why it exists at all rather than needing to be sourced.

**The one topology this forbids.** Poincaré–Hopf: a nowhere-vanishing vector field exists iff $\chi(M) = 0$. Since $\chi(S^4) = 2$, "fibers radiating from a point of $S^4$" is impossible without two singular poles — precisely the rejected $S^4\setminus\{p,\bar p\}$ candidate. $\chi(S^1\times S^3) = \chi(T^4) = 0$: both admissible. The cylinder is the repair for an intuition that cannot be realized on the sphere.

**The fiber is disconnected, and that is the seed [D].** The scaling group is $\mathbb{R}^*$, *including negatives*, so a punctured line through the origin is **two rays**, $(r,\hat n)$ and $(r,-\hat n)$, and the base is $\mathbb{RP}^3$. Hence:

> The fiber over $[\hat n]$ has **two components** — the $u$-circle at $+\hat n$ and the one at $-\hat n$. The projective postulate integrates over both. A star at $(u_0, +\hat n)$ sources the base at $[\hat n]$, whose lift to $S^3$ has wells at **both** $\pm\hat n$.

**The seed is topology plus the projective postulate.** It requires no coupling and no dynamical response of the fibration whatsoever.

**Action, not crossing [T].** The scaling group factorizes, $\mathbb{R}^* = \mathbb{R}^+\times\mathbb{Z}_2$, so the fiber is (scale circle) $\times\;\mathbb{Z}_2$: **the antipodal link is the discrete $\mathbb{Z}_2$ factor, not a continuous path.** Travelling along the fiber from $(u, +\hat n)$ wraps the $u$-circle and returns at the *same* $\hat n$; the origin, where a line would cross, is not in the manifold at all — it was removed precisely because every line meets there and the fibration degenerates. So:

| concept | holds? | why |
|:--|:--|:--|
| antipodal gravitational **action** | **yes** | gravity lives on $\mathbb{RP}^3$, where $\pm\hat n$ *are* one point; the source integrates over both components |
| antipodal **material** crossing | **no** | components disjoint; no path; origin removed |
| flux escape into the fiber | **yes** | the radial direction *is* the fiber; $\sigma = -\partial_r(r^3E_r)$ |
| flux emerging at the **antipode** | **no** | it wraps the compact fiber and returns at the same $\hat n$ |

**The seed is blindness, not crossing** — and that is exactly what keeps the antipode materially empty. A crossing would deliver matter there and destroy the property the seed exists to provide.

**Two independent localizations [D].** A source has a position on the $u$-circle and a choice of $\mathbb{Z}_2$ component. These are unrelated, and they control different physics:

| localization | controls | what the theory needs |
|:--|:--|:--|
| **$\mathbb{Z}_2$ component** ($+\hat n$ vs $-\hat n$) | the seed: antipodal gravitational action | matter in **one** component — maximally localized |
| **$u$-position** on the scale circle | excitation of the massive photon tower (§12.5) and the GR dial (§9) | matter **smeared** — the natural state, since nothing localizes matter internally |

Because the two are independent, ordinary matter can be $u$-smeared (exciting no tower, no Coulomb-law violation) *and* $\mathbb{Z}_2$-localized (full seed) simultaneously. The disconnected fiber decouples what the seed requires from what experiment constrains.

**Why the fibration is not sourced [V].** Two independent reasons. Structurally, sourcing it is fatal: a charge coupling makes every mass a flow endpoint and smears it to background density (§6.1, the terminus theorem). Observationally, even the gentler permittivity coupling of earlier editions is dead: since $\alpha_{\rm fine}\propto1/\psi$, a matter-tracking fiber size would make the fine-structure constant density-dependent, and its constancy forces the response below $2\times10^{-5}$ in ordinary matter — while the cosmic background would need a fiber extent of $10^{-4}$ Planck lengths to orient the fibers at all (§12.5). The fibration is rigid, and the data say so.

**What a rigid fibration costs, and what it does not.** It costs only the *bending*: matter does not bunch fibers, and there is no channel between masses through the fiber field. Every structural result is untouched, because none was ever carried by a coupling:

| survives with a rigid fibration | why |
|:--|:--|
| the seed (antipodal gravitational action) | topology + projective postulate (above) |
| no endpoints, no capture, orbits exist | $f$ is unsourced: $\Box f = 0$ has no flow termini |
| $\Lambda = 1/\ell^2$ from the cone | pure geometry (§3) |
| Mach lock, $k$-dial, $G = \pi c^2\ell/2M_{\rm tot}$ | closure of the base (§10) |
| the $(\Delta_{S^3}+3)$ twin theorem | curvature of $S^3$ (§2) |
| dilaton stabilization, $m_\psi\psi_0 = w$ | the winding energy (§7.5) |
| the projective postulate and the GR dial | §9 |

**The minimal theory, in one line.** Kaluza–Klein on $\mathbb{R}_t\times S^1_u\times S^3$ with a topologically rigid fibration, a stabilized massive radion, and one postulate: **gravity reads the fiber average.** That postulate is the theory's entire departure from general relativity.

**On Machian content.** The fibration does not track matter — it is fixed by the arena. The theory's Machian statement is elsewhere and is exact: *the gravitational coupling is determined by the total matter content of the universe*, $GM_{\rm tot}/c^2\ell = \pi/2$ (§10). Closure does the Machian work, not refraction.

**Why not $T^4$ [V].** $\chi(T^4) = 0$ and the arena is flat and parallelizable, but no static matter-filled flat universe exists — solving $\dot a = \ddot a = 0$ at $k = 0$ gives no solution with $\rho > 0$, while $k = +1$ gives the lock $\Lambda = 1/\ell^2$, $\bar\rho = 1/4\pi\ell^2$. The Einstein-static balance *requires* positive spatial curvature. $T^4$ would therefore destroy the Mach lock and with it the emergent $G$; and its flat Laplacian has constants, not dipoles, in its kernel, so the twin theorem would go too. Closure is load-bearing.

---

## 1 · The founding move and its two constraints

The Newtonian recipe: project the 4-space density onto the base along the radial lines; run Poisson's equation on the sphere. Two constraints were laid down for any dynamical fibration: (1) fibers respond to matter, bunching toward concentrations; (2) symmetric matter corresponds to radial fibers, deviations in one-to-one correspondence.

The minimal theory answers them by relocating both. Fibers *exist* for a topological reason — the winding of $f$ (§6) — and are *oriented* by the arena rather than by matter: on $\mathbb{R}_u\times S^3$ the fiber direction is $\partial_u$, globally defined and nowhere vanishing because the manifold is a product (§0.6). Constraint 2 therefore holds exactly and by construction — radiality is not maintained against matter, it is what the product structure *is*. Constraint 1 is the one the data retired: matter does not bunch the fibers (§6.3). What replaces it is the projective postulate — matter does not move the fibers, but gravity cannot tell where on a fiber matter sits, and that blindness is what the theory runs on.

---

## 2 · The exact Newtonian dictionary

Flat $\mathbb{R}^4\setminus\{0\}$ in polar form splits the Laplacian by homogeneity degree **[V]**:

$$\Delta_4\big[r^s\,\Phi(\hat n)\big] = r^{s-2}\big[\Delta_{S^3} + s(s+2)\big]\Phi(\hat n)$$

The $s=0$ sector is the base Poisson equation, with the projection weight *forced* to be $\sigma(\hat n)\propto\int\rho_4\,r\,dr$ — simultaneously the Machian integral and the conformal-cylinder fiber average: one integral, three derivations.

**The antipodal twin as a theorem of the operator [V].** The $s=1$ operator $\Delta_{S^3}+3$ governs static perturbations of the closed background (derived directly from the linearized Einstein tensor: $G^{(1)}_{00} = -\tfrac{1}{\ell^2}[\Delta_{S^3}\Phi + 3\Phi]$). Substituting $u = \Phi\sin\chi$ collapses it to

$$u'' + 4u = 0 \qquad\Longrightarrow\qquad \Phi = \frac{A\cos 2\chi + B\sin 2\chi}{\sin\chi}$$

The $A$-solution behaves as $+1/\chi$ at the pole and $+1/\epsilon$ at the antipode — **same coefficient, same sign** (flux through a small sphere: $-4\pi$ at both ends). A static point mass cannot be alone; the operator manufactures an equal same-sign singularity at the antipode. In integral form: the kernel of $\Delta+3$ is the four dipole harmonics, so static sources need **zero dipole**, and for two bodies that forces the antipodal equal-mass pair uniquely.

**How the quotient and the theorem agree.** On $\mathbb{RP}^3$ the odd harmonics are absent by construction, so the dipole obstruction is satisfied identically: the projection *is* the twin mechanism. The twin the operator demands is supplied by the quotient — gravitationally, without a second body. This is the seed, expressed as the compatibility of a theorem with a topology.

---

## 3 · The Einstein analogue: the cone theorem

For $g = dr^2 + a(r)^2 h$ over an $n$-dimensional base **[V]**:

$$\mathrm{Ric}_{rr} = -\frac{n a''}{a}, \qquad \mathrm{Ric}_{ij} = \mathrm{Ric}(h)_{ij} - \big[a a'' + (n-1)a'^2\big]h_{ij}$$

The bracket's terms are fiber *acceleration* and fiber *spreading*. The cone $a = r$ kills the first and makes the second the pure number $n-1 = 2$, so vacuum upstairs $\iff$ $\mathrm{Ric}(h) = 2h$ $\iff$ the base is the unit round $S^3/\Gamma$, including $\mathbb{RP}^3$ and every lens space. Rewritten, $G(h) + \Lambda h = 0$ with $\Lambda = 1/\ell^2$:

$$\boxed{\;\text{the cosmological constant is the memory of the fibers spreading apart}\;}$$

generated, never inserted. The fiber direction is a homothety, not a Killing vector, which is why scaling weights pervade the theory.

---

## 4 · Field content and the twist-free collapse

The total metric decomposes as $15 = 10 + 4 + 1$: base metric $g^{(4)}$, tilt connection $A_\mu$, fiber length $\psi$. Because the fibration is the flow of a closed one-form $df$ — multivalued $f$ is fine; winding does not spoil closedness — the fibers are hypersurface-orthogonal, Frobenius applies, and $A_\mu\equiv0$ **is a theorem**. The sole fiber degree of freedom is the dilaton $\psi$, and "fibers bunching" is not a force field but a property of the projection map.

---

## 5 · The total space: the Hopf choice, doubly load-bearing

The candidate total spaces are conformal rescalings of one cylinder $\mathbb{R}_u\times S^3$ **[V]**: the bare cone (noncompact fiber), the Hopf manifold $S^1\times S^3$ (dilation quotient $u\sim u+\ln\lambda$), and $S^4\setminus\{p,\bar p\}$ (degenerate at the poles). The working choice is the Hopf manifold, load-bearing twice: compactness makes the fiber average $\oint du$ well-defined, and $\chi(S^1\times S^3) = 0$ **permits a nowhere-vanishing closed one-form** — exactly what a sourceless fibration requires (Poincaré–Hopf forbids it on $S^4$). The "origin" of $\mathbb{R}^4$ sits at $u = -\infty$ and is removed: the central concentration is matter localized at one region of the fiber circle across all base directions — a slab, not a point. **The primary is the background.**

---

## 6 · The fiber law: why the fibration is not sourced

### 6.1 The monopole disease

The original law $\Box_5 f = \kappa T$ makes matter a *charge* of the fibration: every trace-full object is a flow endpoint. The failure was quantitative **[M]**: basin radius $\theta = 1.644\,(m/M)^{1/3}$ — the Hill scaling — so mass fraction and volume fraction coincide and the density contrast is $\approx 1$ (measured $1.03$–$1.27$): *a point mass smears itself to background density.* No shape or extension escapes. The verdict is the **terminus theorem**: under charge coupling, sourcing the fibration and being orbitable are mutually exclusive. A sign flip repairs nothing — an endpoint is an endpoint.

> **The general lesson.** Whether a field is *sourced* or *unsourced* decides whether localized structure can exist in it at all. Source laws create termini; termini destroy the projection; a destroyed projection means no orbits. This is a design principle for any theory carrying an auxiliary geometric field.

### 6.2 The repair: topology instead of a source

> ### ◆ THE FIBER LAW
> $$\boxed{\;\Box f = 0, \qquad \oint_{\rm fiber} df = \ln\lambda\;}$$
> The fibration field is **not sourced by anything.** It exists because $f$ wraps the compact fiber direction with period $\ln\lambda$ — an angle-like compact scalar, legal precisely because $\chi(S^1\times S^3) = 0$ permits a nowhere-vanishing closed one-form (§5). The solution is $f = wu$ exactly, for any base metric and any dilaton profile **[V]**.

Three consequences. **No endpoints, ever** — an unsourced field has no flow termini, so the entire basin apparatus of §6.1 is abolished by construction and localized masses are generic. **The fibration is rigid** — fixed by the product structure of the arena, not responding to matter (§0.6). **The dictionary closes** — $|\nabla f| = w/\psi$ on the winding solution, tying the fiber field to the dilaton exactly (§7.5).

### 6.3 The retired coupling

Earlier editions promoted the law to $\nabla_\mu[\varepsilon(T)\nabla^\mu f] = 0$ with $\varepsilon = 1-\alpha T$, letting matter refract the fibration. It is recorded here as retired, with the bound that retired it: since the stabilized fiber size would track $\varepsilon$ and $\alpha_{\rm fine}\propto1/\psi$, the constancy of the fine-structure constant forces $\varepsilon - 1 < 2\times10^{-5}$ in ordinary matter, and the cosmic background would need a sub-Planckian fiber extent to orient the fibers at $O(1)$ (§12.5) **[V]**. The refraction sector is unobservable, and removing it makes $\alpha_{\rm fine}$ *exactly* constant rather than merely constant to $10^{-5}$. *Radiation was blind to that coupling in any case* ($T = 0 \Rightarrow \varepsilon = 1$) — the fourth appearance of the selection rule (§15).


---

## 7 · Gravity: the 5D reduction

With the twist-free ansatz $g_5 = g^{(4)} + \psi^2 du^2$, the 5D Einstein equations reduce to **[V]**:

> ### ◆ LAW I — GRAVITY
> **Budget-normalized ($G$-free) form — the default.** With $\ell \equiv (V/2\pi^2)^{1/3}$ the volume radius and $\bar\epsilon \equiv \mathcal{E}/V$ the mean energy density of the closed slice — global invariants of the solution, privileging no node — and $\tau_{\mu\nu} \equiv S_{\mu\nu}/\bar\epsilon$ the fiber-averaged stress tensor as a fraction of the budget:
> $$\boxed{\;\ell^2 R^{(4)}_{\mu\nu} \;=\; \ell^2\,\psi^{-1}\nabla_\mu\nabla_\nu\psi \;+\; 2\Big(\tau_{\mu\nu} - \tfrac13\,\tau\,g^{(4)}_{\mu\nu}\Big)\;}$$
> $$\ell^2\,\Box\psi \;=\; -\frac43\,\psi\Big(\tau_u - \tfrac12\tau\Big) \;\;\to\;\; -\frac23\,\psi\,(\hat\rho - \hat p)\quad\text{under } p_u = p$$
> Both sides dimensionless; the couplings are the pure numbers $2$ and $\tfrac43$, fixed by the Mach lock $8\pi G\bar\epsilon\ell^2/c^4 = 2$ on the homogeneous background, where the dilaton term vanishes because $\psi_0$ tracks a uniform $\varepsilon$ **[V]**. $G$ appears nowhere in the equation; on the static background it equals $\pi c^2\ell/2M_{\rm tot}$ (§10 — a rearrangement, not a derivation). **This is an exact rewriting valid on the static background, not a dynamical law**: normalizing by $\ell(t)$ in an expanding universe would give $\dot G/G = H \approx 7\times10^{-11}$/yr against a lunar-laser-ranging bound of $10^{-13}$/yr, too big by $\sim700\times$ **[V]**. The dynamical theory keeps $G = G_5/C$ constant; §7.5's stabilization is what makes that consistent. The unit-conversion job $G$ performed is reassigned to the pair $(\ell,\mathcal{E})$: one length from geometry, one energy from inventory.
>
> **With the stabilized dilaton (§7.5)** the fiber term becomes $-\tfrac{\hat\alpha}{2}\ell^2\nabla_\mu\nabla_\nu\tau$ with $\hat\alpha = \alpha\bar\epsilon$ a pure number, so the full field equation is
> $$\boxed{\;\ell^2 R^{(4)}_{\mu\nu} + \frac{\hat\alpha}{2}\,\ell^2\,\nabla_\mu\nabla_\nu\tau \;=\; 2\Big(\tau_{\mu\nu} - \tfrac13\,\tau\,g^{(4)}_{\mu\nu}\Big)\;}$$
> — GR's structure with the five-dimensional $\tfrac13$, every coefficient a pure number, every dimension carried by $\ell$ and $\tau$. ($\hat\alpha = 0$ in this theory; the term is displayed only to locate where a susceptibility coupling would enter.)
>
> *Equivalent conventional form* ($G = c = 1$): $R^{(4)}_{\mu\nu} = \psi^{-1}\nabla_\mu\nabla_\nu\psi + 8\pi(S_{\mu\nu} - \tfrac13 S g_{\mu\nu})$, $\;\Box\psi = -\tfrac{16\pi}{3}\psi(p_u - \tfrac12 S)$. Structurally the reduction of static vacuum gravity along a Killing vector; the $\tfrac13$ is the fingerprint of the five-dimensional origin. The source is the **fiber-averaged** stress tensor $S_{\mu\nu} = \oint T_{\mu\nu}\,du$ — the projective postulate at work.

**The dictionary [V].** The fiber proper length per unit $f$ is $1/|\nabla f|$, so $\psi$ and $|\nabla f|$ are tied. On the winding solution the tie is exact — $|\nabla f| = w/\psi$ (§7.5) — so what earlier editions carried as the theory's central consistency seam is closed identically.

**The lesson from the celestial detour, acted on.** A massless fiber-size modulus is a long-range fifth force. The dilaton $\psi$ is exactly such a modulus — and this theory already contains the flux that stabilizes it. §7.5 does the computation.

### 7.5 Dilaton stabilization by the winding

**The problem, and it is fatal without a fix.** In vacuum $\Box\psi = 0$: the dilaton is a Brans–Dicke scalar with $\omega = 0$. Two consequences, both lethal. Its fifth force has Yukawa strength $\alpha = 1/(2\omega+3) = \tfrac13$ at infinite range **[T]**. And the PPN light-deflection parameter is

$$\gamma = \frac{1+\omega}{2+\omega}\bigg|_{\omega=0} = \frac12$$

against Cassini's $\gamma - 1 = (2.1\pm2.3)\times10^{-5}$ **[T]**. That is not a tension; it is exclusion by twenty thousand standard deviations. **An unstabilized theory is dead on arrival.** The celestial detour's lesson was that a flux threading the fiber gives the modulus a mass. Here the flux is already present: **the winding of $f$.**

**The dictionary closes first [V].** $f = wu$ is an *exact* solution of $\Box f = 0$ for any base metric and any $\psi(x)$, with $|\nabla f| = w/\psi$. The §7 seam — $\psi$ versus $1/|\nabla f|$ — is therefore closed by the winding, identically.

**The reduction with the winding energy [V].** With $g_5 = g^{(4)} + \psi^2du^2$, $u\sim u+\ln\lambda$, a 5D cosmological constant $\Lambda_5$, and the winding energy $\tfrac12(\nabla f)^2 = w^2/2\psi^2$, the 5D action reduces to Brans–Dicke with $\omega = 0$ and a potential:

$$S_4 = \ln\lambda\int\sqrt{g_4}\,\Big[\psi R_4 - U(\psi)\Big], \qquad U(\psi) = 2\Lambda_5\,\psi + \frac{w^2}{2\psi}$$

In the Einstein frame $\tilde g = (\psi/\psi_0)\,g$, with $x = \psi/\psi_0$ and canonical field $\phi = \sqrt3\ln x$, the potential is $V(x) = 2\Lambda_5/x + w^2/(2\psi_0^2x^3)$.

**The result [V].** A minimum exists if and only if $\Lambda_5 < 0$, and then

$$\boxed{\;\psi_0^2 = \frac{3\,w^2}{4|\Lambda_5|}, \qquad m_\psi^2 = \frac43|\Lambda_5| = \frac{w^2}{\psi_0^2}, \qquad m_\psi\,\psi_0 = w\;}$$

Three readings. The fiber size is set by the winding, and $w$ is quantized — so $\psi_0$ is fixed by an integer, exactly as the flux integer fixed the fiber in the celestial theory. The modulus Compton wavelength equals the fiber size: $m_\psi\psi_0 = 1$ for one winding, the same law $m\lambda\to1$ found there. And the fifth force becomes a Yukawa of strength $\tfrac13$ and range $\psi_0$: torsion-balance searches then bound the fiber at roughly tens of microns.

**The modulus responds only gravitationally [D].** With the fibration rigid, $\psi_0$ is a pure constant, and the only response to matter is through Law I's own source: $(\Box - m_\psi^2)\,\delta\psi = \tfrac14\kappa T\psi_0$, saturating deep inside a body at $\delta\psi/\psi_0 = 2\pi G\rho\psi_0^2/c^2$ — about $6\times10^{-32}$ for Earth at a $50\,\mu$m fiber (§12.5). Law I's dilaton term is negligible everywhere outside extreme compact objects.

**PPN is restored exactly [D].** With mass $m_\psi = 1/\psi_0$ the scalar is Yukawa-suppressed by $e^{-r/\psi_0}$; at $1$ AU with $\psi_0 = 50\,\mu$m that factor is $e^{-3\times10^{15}}$ — zero for any purpose. The exterior of a body is vacuum Einstein: $\gamma = 1$, Schwarzschild, no fifth force, and the $\tfrac13$ trace-reversal of the 5D reduction never surfaces outside matter. Fifth-force searches then bound $\psi_0$ at roughly tens of microns. **§7.5 is not a tidying step — it is what makes the theory survive the solar system at all**, and it does so with a mechanism the framework already contained.

**The price [O].** At the minimum $\Lambda_4 = \tfrac23\Lambda_5 = -\tfrac12 m_\psi^2 < 0$: the winding-stabilized vacuum is anti-de Sitter, with $|\Lambda_4|$ of order the modulus mass squared. The observed small positive $\Lambda$ needs an uplift of that size — the cosmological-constant problem in Kaluza–Klein dress, shared with the celestial theory's $\Lambda_6$ tuning. **And an internal tension to record [D].** §3 and §10 assume the closed static arena with $\Lambda_4 = +1/\ell^2 > 0$; the stabilized vacuum here has $\Lambda_4 = -m_\psi^2/2 < 0$. So the static closed universe of the Mach lock is *not* a solution of the stabilized theory. The two sections describe different vacua, and reconciling them *is* the uplift problem.

---

## 8 · Geodesics: the two populations

Because $\partial_u$ is Killing, fiber momentum $p_u = \psi^2\dot u$ is conserved and quantized ($p_u\propto n/\ln\lambda$), and the base projection of the 5D geodesic equation gives **[V]**:

$$\frac{D\dot x^\mu}{d\lambda} = \frac{p_u^2}{\psi^3}\,\nabla^\mu\psi, \qquad m_{\rm eff} = \sqrt{1 + p_u^2/\psi^2}$$

**Neutral matter ($p_u = 0$)** follows base geodesics exactly. Trace-full lumps project to compact base masses (§6.3), so the base contains Schwarzschild-like wells in the closed background, and the closed-universe orbit machinery — exact static solver, rosettes, trapped orbits — describes this theory's actual solar systems.

**Charged matter ($p_u\neq0$)** feels the scalar fifth force, sliding toward large $\psi$. The pinch points of the monopole era **no longer exist**: divergence-free flux with $\varepsilon > 0$ admits no critical points. With the fibration rigid, $\psi$ varies only through its own stabilized field equation, so the force is a Yukawa of range $\psi_0$ and is bounded everywhere (§7.5).

---

## 9 · The projective postulate and the GR dial

> ### ■ THE PROJECTIVE POSTULATE
> Mass at $B$ acts as if at $A$ along the same fiber; base gravity reads only $S_{\mu\nu} = \oint T_{\mu\nu}\,du$.

Its distance from GR is a dial: a source of fiber-width $w$ on a fiber of circumference $L$ puts zero-mode share $0.18/0.53/0.95/1.00$ at $w/L = 0.05/0.15/0.3/0.5$ **[M]**. Fiber-smeared matter reproduces GR exactly; fiber-localized matter is maximally projective. The base Bianchi identity forces $\nabla^\mu S_{\mu\nu} = 0$, and the compact fiber converts 5D conservation into conservation of fiber averages, with $\langle p_u\rangle = \langle p\rangle$ and $\partial_u p_u = 0$ absent fiber flux.

**This postulate is load-bearing.** It is the nonlocality that the seed requires (§0.5). It is a *postulate* precisely because it is not automatic — and its not being automatic is what makes the antipodal image gravitate.

### 9.5 Consistency of the postulate

*Four questions, settled in order. The first two are computations; the last two are the honest reading of what they establish.*

**Does fiber-averaging respect the Bianchi identity? [V]** Integrate 5D conservation $\nabla_A T^{AB} = 0$ over the closed fiber; the $\partial_u$ term drops. With $\sqrt{g_5} = \psi\sqrt{g_4}$ and $\Gamma^\nu_{uu} = -\psi\nabla^\nu\psi$, the base component is

$$\nabla_\mu S^{\mu\nu} = -\frac{\nabla_\mu\psi}{\psi}\,S^{\mu\nu} + \psi\,\nabla^\nu\psi\;S^{uu}$$

— exactly the exchange term of A9, vanishing for constant $\psi$ or for $p_u = p$. In the stabilized theory $\delta\psi/\psi\sim10^{-32}$, so the Bianchi identity holds to that order. The conservation web closes.

**Does it descend to the quotient? [D]** $S([\hat n]) = \oint_{+\hat n} + \oint_{-\hat n}$ is antipodally symmetric by construction; each term is conserved with respect to the pulled-back (symmetric) metric; the covering map is a local isometry. The sum descends to $\mathbb{RP}^3$ and is conserved there.

**What the theory is, seen from the quotient [D].** General relativity on $\mathbb{R}_t\times\mathbb{RP}^3$ (times a stabilized fiber), sourced by the **pushforward** of matter living on the double cover, with light propagating on the cover. Equivalently: GR on $\mathbb{RP}^3$ in which every matter field carries a $\mathbb{Z}_2$ sheet label — gravity blind to the label, Maxwell diagonal in it. On the quotient this is a consistent, local, causal field theory with nothing exotic in it. The seed, viewed from here, is the statement that gravity ignores the sheet label.

**The cost, which the quotient hides and the cover exposes [D].** In the cover, wiggling a lump at $+\hat n$ changes the gravitational field at $-\hat n$ **instantly** — they are one point of the quotient — while light from $+\hat n$ reaches $-\hat n$ only after $t = \pi\ell/c$. **Gravity and light have different causal structures on the cover: a two-speed spacetime.** This is not paradoxical: the static universe supplies a preferred frame, so no tachyonic antitelephone can be built, and the antipode lies $\sim14\times$ beyond the horizon, so nothing of it is observable. But it is a genuine conceptual departure from general relativity, it is the true price of the projective postulate, and it belongs on the record rather than in a footnote.

### 9.6 The local trace — a signpost for eventual testing

*Does the two-speed structure leave any trace a local observer could measure? Under a naive extension to an expanding universe, it does, and the trace is a specific bias-free statistic. This section records what that statistic is, what the theory would predict for it, and what current data say — as a signpost. The extrapolation is heuristic: the guide has no perturbation theory on an expanding background, and none of this bears on the theory's internal consistency (§9.5).*

**The correction to §12's fork.** I previously wrote that in a large fundamental domain "the images are outside the horizon." That is the image *of local matter*. The image *of antipodal matter* is **here**: the postulate sources gravity at $[\hat n]$ from matter at both $\pm\hat n$ at the same time, so the local gravitational potential is

$$\Phi_{\rm here} = \Phi_{\rm local} + \Phi_{\rm image}$$

where $\Phi_{\rm image}$ is the potential of the matter at our antipode, $\sim14$ horizons away — an **independent realisation of the same statistics.**

**The consequence [D, robust to normalisation].** With $\delta_1$ (local) and $\delta_2$ (antipodal) independent fields of equal power, whether the postulate sums or averages them:

| | $\mathrm{Var}(S)/\mathrm{Var}(\delta_1)$ | lensing amplitude ratio | gravity–galaxy cross-correlation $r$ |
|:--|:--|:--|:--|
| sum $S = \delta_1+\delta_2$ | $2$ | $\sqrt2$ (41% high) | $1/\sqrt2 = 0.707$ |
| mean $S = \tfrac12(\delta_1+\delta_2)$ | $\tfrac12$ | $1/\sqrt2$ (29% low) | $1/\sqrt2 = 0.707$ |

**The statistic, pedagogically.** Surveys measure three two-point correlations: galaxy clustering $\langle\delta_g\delta_g\rangle$ (where the light is), cosmic shear $\langle\kappa\kappa\rangle$ (where the gravitating mass is, all of it), and galaxy–galaxy lensing $\langle\delta_g\kappa\rangle$ (where light and mass coincide). Galaxies are biased tracers, $\delta_g = b\,\delta_m$ with $b$ unknown, so $\langle gg\rangle = b^2P$, $\langle g\kappa\rangle = bP$, $\langle\kappa\kappa\rangle = P$, and the ratio

$$r^2 \equiv \frac{\langle g\kappa\rangle^2}{\langle gg\rangle\,\langle\kappa\kappa\rangle}$$

is **bias-free**. $r = 1$ means every piece of gravitating mass has light sitting on it; $r < 1$ means some mass gravitates with no light tracing it. That is exactly what an antipodal image is, which is why $r$ is the right diagnostic and why the prediction cannot be absorbed into $b$.

**The naive prediction.** Galaxies trace $\delta_1$; lensing traces $S$; the sheets are uncorrelated (antipodal correlation of a field with power at $\ell\gtrsim10$ is below $10^{-2}$, computed from the $(-1)^\ell$ parity of $S^3$ harmonics). Hence $r = 1/\sqrt2 \approx 0.71$ (Monte Carlo: $0.7068$), with the lensing amplitude off from clustering by $\sqrt2$ in whichever direction the normalization puts it. In words: **half the lensing power would come from structures with no optical counterpart, uncorrelated with galaxies.**

**Current data, stated carefully.** Galaxy positions come from redshift surveys (SDSS, BOSS, DESI); lensing from imaging surveys (DES, KiDS, HSC) via coherent distortions of background galaxy shapes; the cross-correlation from combining the catalogs. Most "3×2pt" analyses *assume* $r = 1$ on large scales through linear bias rather than measure it, and fit well. Where $r$ is allowed to float it comes out consistent with 1 at roughly the $10$–$20\%$ level. So $r = 0.71$ is **in tension at a couple of sigma — not excluded.** The decisive test would be a dedicated large-scale measurement of $r$. (An earlier draft of this section said "excluded at many sigma"; that overstated the constraint and is withdrawn.)

**The escapes, and what each costs.**
- *Antipodally symmetric initial conditions* ($\delta_2 = \delta_1$): $r = 1$, the factor is absorbed into $G$, and the theory becomes **general relativity with a redefined constant** — every distinctive feature evaporates.
- *A time-shifted quotient* $(t,\hat n)\sim(t+\pi\ell/c,-\hat n)$: the image is retarded by $\pi\ell/c \approx 645$ Gyr, $47\times$ the age of the universe — before structure existed. The image is empty, the seed never operates, and the theory is again GR.

$$\boxed{\;\text{Signpost: under naive extension, the seed predicts } r = 1/\sqrt2\text{, bias-free; current data mildly disfavor it; each escape switches the seed off.}\;}$$

*Scope, restated:* this is a heuristic extrapolation of a static model to an expanding universe with an uncorrelated antipode. In the static closed arena of §10 the antipodal twin is forced by the $(\Delta+3)$ theorem and the issue does not arise. The theory's mathematical consistency is settled in §9.5 and untouched here. What §9.6 supplies is the observable the idea will have to meet once it *is* developed into a cosmology — and, at the drafting stage, that is the right thing to know and the wrong thing to be ruled by.

---

## 10 · The idealized universe — a $G$-free dossier (salvaged)

*Everything in this section is closed-universe physics on the base, independent of the fiber law, and transfers to any formulation with a closed 3-sphere spatial section. Stated in the GR limit of the dial; dilaton corrections are §7's seam.*

**The Mach lock [V].** The static closure relation fixes $\bar\rho = c^2/4\pi G\ell^2$ and $\Lambda = 1/\ell^2$; multiplying by the 3-sphere's volume:

$$\boxed{\;\frac{G\,M_{\rm tot}}{c^2\,\ell} = \frac{\pi}{2}\;}$$

Sciama's order-unity Machian relation with its coefficient supplied, exactly.

> **What this relation is, and is not [D].** It is a **consistency relation on static solutions**, not a derivation of $G$. In the reduced theory $G_4 = G_5/C$ with $C = \psi_0\ln\lambda$ the stabilized fiber circumference — both factors constants — so $G$ enters as an input exactly as in general relativity. The static sector has four quantities $(G, \Lambda, \bar\rho, \ell)$ and two equations ($\dot a = \ddot a = 0$), leaving two free: the natural reading takes $G$ and $\Lambda$ as inputs and returns $\ell = 1/\sqrt\Lambda$ and $\bar\rho$. Writing $G = \pi c^2\ell/2M_{\rm tot}$ inverts the same equation; the two readings are algebraically identical and neither is privileged. Earlier editions of this guide presented the inverted form as though $G$ were an *output*. It is not. What the relation genuinely delivers: **$G$ is not independently specifiable in a closed static universe** — one fewer free quantity than a naive count — and the coefficient is $\pi/2$ exactly rather than Sciama's $\sim1$.

**The $k$-dial [V — dynamically confirmed, wobble $10^{-13}$].** With the lumps carrying fraction $k$ of the budget at antipodal nodes, the circular-orbit speed at colatitude $\chi = d/\ell$ is

$$\boxed{\;\frac{v^2(\chi)}{c^2} = k\,\frac{\pi - 2\chi + \sin 2\chi}{2\sin 2\chi}\;}$$

Landmarks: near a node $v^2\to G(M_l/2)/d$ (Kepler, the $\tfrac12$ being the budget's split between the poles); at the equator $v^2/c^2 = k$ exactly, a stationary minimum — **the budget meter**; at parity $k = 1$, light speed at the midpoint, mass-independent. The lone-mass Kepler continuation would give $\tfrac12$ there: the factor of $2$ is the antipode speaking.

**$G$ from the other three [V].**

$$G = \frac{\pi c^2\ell}{2M_{\rm tot}} = \frac{\pi\ell\,v^2_{\rm eq}}{2M_{\rm lumps}} = \frac{c^2}{4\pi\bar\rho\,\ell^2}$$

Measurement protocol: circumference $\to\ell$; midpoint orbit $\to v^2$; inventory $\to M$. A hidden $G$ is recovered to $10^{-10}$ — a genuine constraint, though (per the caveat above) a rearrangement rather than a derivation.

**The inversion: what the theory could predict instead [D, conditional].** The Machian ambition is not dead — it points the other way. Every link in this chain is a derived relation of the theory:

$$\psi_0 = \sqrt{\frac{3w^2}{4|\Lambda_5|}} \;\to\; C = \psi_0\ln\lambda \;\to\; G_4 = \frac{G_5}{C}, \qquad \Lambda_4 = \tfrac23\Lambda_5 \;\to\; \ell = \frac{1}{\sqrt{\Lambda_4}}$$

Feeding both into the Mach lock returns

$$\boxed{\;M_{\rm tot} = \frac{3\sqrt2\,\pi\,c^2\,\ln\lambda\;w}{8\,G_5\,\Lambda_5}\;}$$

with **every symbol on the right a theory parameter** — $G_5$, $\Lambda_5$, $w$, $\ln\lambda$; nothing observational. So the statement is not "the universe determines $G$" but "**the theory determines the universe**": it would *predict the total mass*. That is the stronger claim of the two, because it can be wrong.

**The condition, not undersold [O].** The inversion requires $\Lambda_4 > 0$, and the stabilized vacuum gives $\Lambda_4 = -m_\psi^2/2 < 0$. The magnitude is worse than the sign:

| $\psi_0$ | $\vert\Lambda_4\vert$ | vs observed $1.1\times10^{-52}\,\mathrm{m^{-2}}$ |
|:--|:--|:--|
| $50\,\mu$m | $2\times10^{8}\,\mathrm{m^{-2}}$ | off by $10^{60}$ |
| $1\,\mu$m | $5\times10^{11}\,\mathrm{m^{-2}}$ | off by $10^{63}$ |

That is the cosmological-constant problem at full strength, and this framework has no special claim on solving it. **The prediction exists in the structure and is unreachable in practice** — one problem stands between the framework and a real prediction, and it is the hardest unsolved problem in the subject.

**Role democracy [V].** In the stereographic chart $r = \tan(\chi/2)$ the two-node potential is $\Phi/c^2 = k(\pi r/8 + \tfrac12 - \pi/8r)$, **identical** under $r\to1/r$: a $-\pi/8r$ pole (the visible mass) plus an isotropic $+\pi r/8$ pull toward chart-infinity (the antipodal node, smeared over the sky only by the chart). "Primary" and "secondary" are frame labels; any node can be sent to infinity, none is privileged. This is the Kelvin transform: the MP metric's constant "1" is a point mass at infinity, exactly.

**Locality [V].** The weak-field equation holds pointwise for a random 8-lump configuration with the coupling fixed by the total budget alone: a local PDE, two global scalars, no primary. Staticity adds the global filter "zero dipole" (§2) — a constraint on configurations, not a nonlocality of the law.

**The charged secondary [V].** On the closed background, Maxwell's total-charge-zero forces a $-Q$ somewhere; its field lines run pole to pole as a conserved tube inside the 3-sphere. With the partner at the symmetric antipode:

$$\phi_e = \frac{Q}{4\pi\epsilon_0\ell}\cot\chi, \qquad \Phi = -\frac{2GM}{\pi\ell}\Big(\frac{\pi}{2}-\chi\Big)\cot\chi + \frac{GQ^2}{8\pi\epsilon_0 c^2\ell^2}\csc^2\chi$$

Near the charge this is Reissner–Nordström, **deduced**: the field's own energy gravitates with the universal $G$. Budget form: $\Phi/c^2 = -(M/M_{\rm tot})(\tfrac\pi2-\chi)\cot\chi + \tfrac{\pi^2}{8}(Q/Q_{\rm ext})^2\csc^2\chi$ with $Q_{\rm ext} = M_{\rm tot}\sqrt{4\pi\epsilon_0 G}$. The two operators fix the two partner signs: mass obeys $\Delta+3$ (same-sign poles, same-sign twin); charge obeys $\Delta$ (opposite-sign poles, $\pm Q$).

**The E-series.**

| # | identity | status |
|:--|:--|:--|
| E1 | $\Lambda\ell^2 = 1$ (closure eigenvalue) | [V] |
| E2 | $GM_{\rm tot}/c^2\ell = \pi/2$ (Mach lock — a consistency relation on static solutions, §10) | [V] |
| E3 | $v^2_{\rm eq}/c^2 = M_{\rm lumps}/M_{\rm tot}$ ($k$-dial) | [V] |
| E4 | $\bar\rho = c^2/4\pi G\ell^2$ | [V] |
| E5 | $M_{\rm each}(k{=}1) = \pi c^2\ell/4G$ | [V] |
| E6 | null rays refocus at the antipode at $t = \pi\ell/c$; period $2\pi\ell/c$ | [V] |
| E7 | $\ker(\Delta_{S^3}+3)$ = dipoles; $u = \Phi\sin\chi$ gives $u''+4u = 0$ | [V] |
| E8 | a single lump circulating a great circle has zero time-averaged dipole | [V] |
| E9 | charged secondary: $\phi_e\propto\cot\chi$, mass $\propto(\chi-\tfrac\pi2)\cot\chi$, charge $\propto\csc^2\chi$ | [V] |
| E10 | stereographic self-duality $r\to1/r$ of the two-node potential | [V] |
| E11 | budget-normalized couplings: $8\pi G\bar\epsilon\ell^2/c^4 = 2$ (Law I), $\tfrac43$ (dilaton) — pure numbers | [V] |
| E12 | fiber-escape identity: $\sigma = -\partial_r(r^3E_r)$ on the slice; net zero for off-slice sources | [V] |
| E13 | $f = wu$ solves $\Box f = 0$ for any base metric and any $\psi(x)$; $\lvert\nabla f\rvert = w/\psi$ | [V] |
| E14 | stabilization: $\psi_0^2 = 3w^2/4\lvert\Lambda_5\rvert$; $m_\psi\psi_0 = w$ | [V] |
| E15 | $\Lambda_4 = \tfrac23\Lambda_5 = -\tfrac12 m_\psi^2$ at the stabilized vacuum | [V] |
| E16 | charged node: gravity's force vanishes at the equator (both terms); electric force $Q/4\pi\epsilon_0\ell$ there | [V] |
| E17 | a lump of index contrast $0.03$ shifts the null-ray refocus $0.56°$ off the antipode and blurs it | [V] |
| E18 | 5D Maxwell reduces to $\nabla_\mu(\psi\mathcal{F}^{\mu\nu}) = \psi\mathcal{J}^\nu - \partial_u(\psi^{-1}\mathcal{F}_u{}^\nu)$: a medium with $\epsilon = 1/\mu = \psi$, $\epsilon\mu = 1$ | [V] |
| E19 | fiber photon modes are Proca with $m_n = 2\pi n/C_{\rm fiber}$ ($\approx 25$ meV at $50\,\mu$m) | [D] |
| E20 | light lives on the double cover $S^3$, in the antipodally symmetric metric: lensed at the image, not emitted there | [D] |
| E21 | $\chi(S^4) = 2$: fibers radiating from a point of $S^4$ are forbidden; $\chi(S^1\times S^3) = 0$ | [T] |
| E22 | fiber over $[\hat n]$ has two components ($\pm\hat n$): the seed, from topology alone | [D] |
| E23 | retired coupling: $\delta\alpha_{\rm fine}/\alpha_{\rm fine} = -\alpha\rho/2 \Rightarrow \varepsilon - 1 < 2\times10^{-5}$; primary needs $<10^{-4}\,\ell_{\rm P}$ fiber extent | [V] |
| E24 | no static matter-filled flat universe: the lock needs $k = +1$ | [V] |
| E25 | $\mathbb{R}^* = \mathbb{R}^+\times\mathbb{Z}_2$: the antipodal link is the discrete factor, not a path | [T] |
| E26 | $\mathbb{Z}_2$-localization $\Rightarrow$ the seed; $u$-localization $\Rightarrow$ the Proca tower; independent | [D] |
| E28 | $G_4 = G_5/C$, $C = \psi_0\ln\lambda$: $G$ is a constant of the theory, not an output | [D] |
| E29 | unstabilized: $\gamma = 1/2$ (excluded); stabilized: $\gamma = 1$ to $e^{-3\times10^{15}}$ at 1 AU | [T/D] |
| E30 | conditional inversion: $M_{\rm tot} = 3\sqrt2\pi c^2\ln\lambda\,w/8G_5\Lambda_5$, needs $\Lambda_4>0$ | [D] |
| E31 | $\nabla_\mu S^{\mu\nu} = -(\nabla_\mu\psi/\psi)S^{\mu\nu} + \psi\nabla^\nu\psi\,S^{uu}$: Bianchi closes to $10^{-32}$ | [V] |
| E32 | the averaged source descends to $\mathbb{RP}^3$ conserved (covering map a local isometry) | [D] |
| E33 | two-speed cover: gravity links antipodes instantly, light in $\pi\ell/c$; preferred frame, no paradox | [D] |
| E34 | uncorrelated antipode: $r_{\rm grav,gal} = 1/\sqrt2$, bias-free; mildly disfavored, not excluded (signpost) | [D] |
| E35 | escapes (symmetric IC; time-shifted quotient) each reduce the theory to GR | [D] |
| E36 | $w$ conserved by admissibility; $A_u$ not thermally populated | [D] |
| E27 | $\delta\alpha_{\rm fine}/\alpha_{\rm fine} = 2\pi G\rho\psi_0^2/c^2 \approx 6\times10^{-32}$ (Earth, $50\,\mu$m) | [V] |

---

## 11 · The axioms, third edition

> ### ■ ARENA
> - **A1.** Total spacetime $M_5 = \mathbb{R}_t\times S^1_u\times S^3$, fiber spacelike and compact.
> - **A2.** Base $B_4 = \mathbb{R}_t\times\mathbb{RP}^3$ (or $\mathbb{R}_t\times S^3/\Gamma$). The fiber over $[\hat n]$ has $|\Gamma|$ components (§0.6) — the source of the seed.
> - **A3.** $\chi(M_5) = 0$, enabling the winding form.
> - **A3′.** A 5D cosmological constant $\Lambda_5 < 0$ (required for the winding to stabilize the fiber, §7.5).

> ### ■ FIELDS
> - **A4.** Base metric $g^{(4)}$ (10).
> - **A5.** Compact fiber scalar $f$, winding $\oint df = \ln\lambda$; dilaton $\psi$ with $|\nabla f| = w/\psi$, stabilized at $\psi_0^2 = 3w^2/4|\Lambda_5|$ with mass $m_\psi = 1/\psi_0$ (§7.5).
> - **A6.** $A_\mu\equiv0$ by Frobenius.

> ### ◆ LAW I — GRAVITY
> - **A7.** The projective postulate: base gravity reads $S_{\mu\nu} = \oint T_{\mu\nu}\,du$.
> - **A8.** $\ell^2 R^{(4)}_{\mu\nu} = \ell^2\psi^{-1}\nabla_\mu\nabla_\nu\psi + 2(\tau_{\mu\nu} - \tfrac13\tau g_{\mu\nu})$; $\;\ell^2\Box\psi = -\tfrac43\psi(\tau_u - \tfrac12\tau)$, with $\tau = S/\bar\epsilon$. No coupling constant: $G$ is a theorem (D5).
> - **A9.** Conservation with exchange: $p' + (\rho+p)\Psi' + (p - p_u)\psi'/\psi = 0$; matter condition $p_u = p$.

> ### ◆ LAW II — FIBRATION
> - **A10.** Fibers are the flow lines of $\nabla f$.
> - **A11.** $\Box f = 0$ with $\oint df = \ln\lambda$: the fibration is **unsourced and rigid**, $f = wu$ exactly. Matter does not couple to $f$ (§6).

> ### ◇ LAW III — ELECTROMAGNETISM (candidate slot)
> - **A12 (adopted, §12.5).** The electromagnetic 2-form lives on $M_5$ — the double cover $\mathbb{R}_t\times S^1_u\times S^3$, not the gravitational base — with its 5D current supported on charged matter: $d\mathcal{F} = 0$, $d\star_5\mathcal{F} = \star_5\mathcal{J}$. The source-free case $\mathcal{J} = 0$, with charges as winding defects, is the Wheeler option **[S]**. Its reduction is derived in §12.5: ordinary Maxwell survives.
> - **Gauss's law as fiber escape [V].** In this geometry the fiber *is* the radial direction of $\mathbb{R}^4$ — transverse to the physical 3-sphere, so flux genuinely leaves 3-space along it. (It does **not** emerge at the antipode: the compact fiber closes on itself at the same $\hat n$, §0.6.) The 4D divergence in polar form, $\nabla\!\cdot\!E = r^{-3}\partial_r(r^3E_r) + r^{-1}\nabla_{S^3}\!\cdot E_\parallel$, gives a source-free field an apparent 3-charge on the slice
> $$\sigma(\hat n) = -\,\partial_r\big(r^3E_r\big)\big|_{r=1}$$
> — Gauss's law on the 3-sphere read as **flux escaping along the fiber**. For a 4D Coulomb charge just off the slice this yields a sharp positive apparent charge beneath it and a diffuse negative sea, netting zero by Gauss's theorem on the 4-ball. This is the derivation the celestial fibers could not support: there the fiber was directions at a point, and the escape identity had no direction to escape along.
> - **The loophole.** Net base charge from plumbing alone needs either a drain at the cone point or a **multivalued potential** (the balance theorem holds only for single-valued fields). This theory's fiber field is multivalued by construction, so the winding sector is the natural home of Wheeler's charge-without-charge **[S]**. Its consequence for base electrodynamics is open problem 3.

> ### ▣ DERIVED
> - **D1.** $\Lambda = 1/\ell^2$ from the cone (§3). **D2.** No fiber endpoints; concentration $\le n$ (§6.3). **D3.** $p_u = 0$ geodesics are base geodesics. **D4.** The static twin is the quotient (§2). **D5.** Mach lock, $k$-dial, $G$ as theorem (§10).

**Admissibility.** $\nabla f$ spacelike and nowhere zero (automatic on the winding solution); fiber compact; energy conditions on $(\rho, p, p_u)$.

**Free parameters of the minimal theory.** The winding integer $w$ · one scale, $|\Lambda_5|$ (equivalently the stabilized fiber size $\psi_0$, bounded by fifth-force searches at tens of microns) · the quotient group $\Gamma$ · the equation of state. That is **one integer, one scale, one discrete choice.** $G$ is a theorem; $\Lambda\ell^2$ an eigenvalue; $c$ from the causal structure of $M_5$; $m_\psi = 1/\psi_0$, not a dial; $\alpha_{\rm fine}$ exactly constant.

---

## 12 · The seed as a prediction: dark matter as projection shadow

**The mechanism [D].** Let a cloud of luminous matter occupy a region $R$ of the physical 3-sphere inside $M_5$. Under the quotient, the base region $[R]$ carries its mass. Lift the base gravitational field back to the 3-sphere: it has wells at $R$ **and at the image $\bar R$**. Now let light propagate on $M_5$ (A12). At $\bar R$ there is no matter in the total space: nothing emits, nothing absorbs, nothing scatters — but the well is there, so light passing $\bar R$ is **lensed**. The image region is, operationally, dark matter: gravitation and lensing without luminosity or interaction.

$$\boxed{\;\text{dark matter} = \text{the projection image of luminous matter}\;}$$

Its properties are inherited, not fitted: collisionless (nothing there to collide), non-luminous, non-absorbing, gravitating and lensing with the full mass of its source, and tracking its source exactly through the quotient map.

**Three consistency facts already in hand.**
- *Radiation is the natural dweller of the total space.* It needs no fiber stress and cannot source $f$ — the radiation-blindness ledger's six entries are all reasons A12 costs nothing.
- *The image is diluted, not copied* **[M]**: the base footprint of a dust cloud is spread by a factor $0.25$–$0.75$, of stiff matter concentrated by $\sim15\times$. **The dark image of ordinary matter is more diffuse than its source** — halo-like rather than cusp-like.
- *The static sector forces symmetric sources* (§2), so in the static idealization luminous matter at $R$ is accompanied by luminous matter at $\bar R$, and each is the other's image: dark matter is then **co-located** with luminous matter, image-for-image.

**The ratio, and an arithmetic worth flagging [S].** With $\Gamma = \mathbb{Z}_2$ each luminous lump has one image, so $\Omega_{\rm dark}/\Omega_{\rm lum} = 1$ in the co-located static picture. With a general free quotient $S^3/\Gamma$ (all admitted by the cone theorem) each lump has $|\Gamma| - 1$ images and the ratio is $|\Gamma| - 1$. The observed $\Omega_c/\Omega_b \approx 5.4$ sits between $|\Gamma| = 6$ and $7$. This is a curiosity, not a fit: it assumes exact $\Gamma$-symmetry of the luminous distribution, which the static sector demands and the dynamical sector does not.

**The tensions, stated honestly [O].**
1. *Distribution.* The image of a local galaxy is a dark galaxy at the antipode; the images *here* are of antipodal matter, uncorrelated with local galaxies. Neither produces halos around luminous galaxies, and the uncorrelated local image field is the $r = 1/\sqrt2$ signpost of §9.6.
2. *Light on $M_5$.* A12 is a genuine postulate about where the electromagnetic field lives. Its consequences for the base — effective Maxwell equations with fiber-flux charges — must be derived and checked against ordinary electrodynamics.
3. *The dilaton.* The image gravitates through $S_{\mu\nu}$, but $\psi$ is sourced by $\rho - p$ of the *total-space* matter, which is not $\Gamma$-symmetric. The dark image and its source therefore differ in their dilaton coupling — a distinguishing signature if $\psi$ is light, and irrelevant if it is stabilized (§7).

**What would falsify it.** Any dark-matter concentration with no luminous counterpart at its $\Gamma$-image; any luminous concentration whose $\Gamma$-images carry no dark mass. The map is fixed by the topology, so the prediction is rigid.

### 12.5 The electrodynamics check — verdict

*A12 is the load-bearing assumption under the dark-matter reading. Here 5D Maxwell is reduced on the actual geometry $g_5 = g^{(4)} + \psi^2du^2$, $u\sim u+L$, and the base's electrodynamics is read off. The decomposition was checked symbolically on a flat base with $x$-dependent $\psi$ and an arbitrary fiber mode; residual identically zero **[V]**.*

**The reduction [V].** Since $\sqrt{g_5} = \psi\sqrt{g_4}$ and $g^{uu} = \psi^{-2}$, the two components of $\nabla_M\mathcal{F}^{MN} = \mathcal{J}^N$ are exactly

$$\boxed{\;\nabla_\mu\big(\psi\,\mathcal{F}^{\mu\nu}\big) = \psi\,\mathcal{J}^\nu - \partial_u\big(\psi^{-1}\mathcal{F}_u{}^{\nu}\big), \qquad \nabla_\mu\big(\psi^{-1}\mathcal{F}^{\mu}{}_u\big) = \psi\,\mathcal{J}^u\;}$$

The base sees **Maxwell in a medium of permittivity $\psi$**, sourced by the fiber current plus the **fiber-flux escape rate** $-\partial_u(\psi^{-1}\mathcal{F}_u{}^\nu)$ — Gauss's law as plumbing, the structure §A12 anticipated, now derived.

**Four results.**
1. **Ordinary Maxwell survives.** For the zero mode, $\nabla_\mu(\psi\mathcal{F}^{\mu\nu}) = \psi\mathcal{J}^\nu$ is electrodynamics in a medium with $\epsilon = 1/\mu = \psi$, so $\epsilon\mu = 1$: in the eikonal limit $k^2 = 0$ and **light rides the null geodesics of $g^{(4)}$, unrefracted by the dilaton**, which changes impedance only. With $\psi = \psi_0(1-\alpha T/2)$ the medium is uniform to $O(\alpha T)$ **[V]**.
2. **The fiber modes form a Proca tower.** In the gauge $A^{(n)}_u = 0$ the escape term becomes a mass, $\nabla_\mu(\psi\mathcal{F}^{\mu\nu}) = (k/\psi)^2A^\nu$ with $m_n = 2\pi n/C_{\rm fiber}$: for a fiber circumference of $50\,\mu$m, $m_1c^2 \approx 25$ meV; for $1\,\mu$m, $1.2$ eV. Sourced only by fiber-*localized* charge; fiber-smeared matter never excites it **[D]**.
3. **One extra scalar.** The $u$-component's zero mode obeys $\nabla_\mu(\psi^{-1}\nabla^\mu A_u) = \psi\mathcal{J}^u$: a massless base scalar whose Wilson line $\oint A_u\,du$ is the winding loophole of Law III made explicit. A new radiation species **[O]**.
4. **Apparent charges obey the balance theorem.** The escape term is a total $u$-derivative, so its fiber average vanishes for single-valued fields: smooth source-free configurations put no net charge into the zero-mode photon. Wheeler charges need winding or singular configurations — hence A12's working form admits a 5D current, with the source-free version as an option.

**The dark-matter verdict [D].** The reduction runs along the $u$-circle *only* and lands on $\mathbb{R}_t\times S^3$ — **the double cover**, not the gravitational base $\mathbb{R}_t\times\mathbb{RP}^3$. The electromagnetic field is therefore sourced by the current at $\hat n$ alone, and is under no obligation to be antipodally symmetric. The metric it propagates in is $g^{(4)}$ pulled back from the quotient: **antipodally symmetric, with wells at both $\hat n$ and $-\hat n$** — because the projective postulate symmetrizes every stress tensor it reads, the electromagnetic field's own included. So at the image, light is **lensed and not emitted, absorbed, or scattered.** Two equations on two spaces, with no contradiction: gravity reads the pushforward, Maxwell reads the cover.

$$\boxed{\;\text{A12 passes: the seed's optics are a consequence of the reduction, not an assumption.}\;}$$

**The only permittivity here is the dilaton [D].** $\varepsilon_{\rm EM} = \psi$ is the electromagnetic permittivity of the reduced theory; it is unrelated to the retired susceptibility of §6.3, and every result in this section is independent of that coupling.

**Does the photon reveal the fiber? [V]** With the fibration rigid, $\psi_0 = \sqrt{3w^2/4|\Lambda_5|}$ is a **pure constant**, so nothing makes $\alpha_{\rm fine}$ density-dependent. What remains is the *gravitational* sourcing of $\psi$: deep inside a body the response saturates at $\delta\psi/\psi_0 = 2\pi G\rho\psi_0^2/c^2$, hence

| | Earth | neutron star |
|:--|:--|:--|
| $\psi_0 = 50\,\mu$m | $6\times10^{-32}$ | $1\times10^{-18}$ |
| $\psi_0 = 1\,\mu$m | $3\times10^{-35}$ | $5\times10^{-22}$ |

against an observational reach of $10^{-5}$–$10^{-7}$. **Dissolved with roughly 24 orders of margin** — and note the mechanism: the effect scales as $\psi_0^2$, so the same smallness of the fiber that makes the fifth force short-range also kills the varying-$\alpha$ signal. One stabilization, two rescues.

**The tower is not excited [D].** Fully $u$-localized charge would give $O(1)$ Yukawa corrections to Coulomb's law at $r\sim C/2\pi \approx 8\,\mu$m for a $50\,\mu$m fiber — squarely where Casimir and Coulomb-law experiments look, and a genuine problem if it arose. It does not: the seed requires $\mathbb{Z}_2$-localization, not $u$-localization (§0.6), and those are independent. $u$-smeared matter has only the $n=0$ Fourier mode and sources no massive vector, while sitting in one $\mathbb{Z}_2$ component gives the full seed. Both at once, no tension.

**The bound that retired the susceptibility coupling [V].** By Kaluza–Klein counting $1/e_4^2 = \psi L/g_5^2$, so $\alpha_{\rm fine}\propto1/\psi$; and the stabilized fiber tracks matter, $\psi_0\propto\sqrt\varepsilon$. Hence

$$\frac{\delta\alpha_{\rm fine}}{\alpha_{\rm fine}} = -\frac{\alpha\rho}{2}$$

The fine-structure constant would vary with local density. Comparing terrestrial and quasar-absorber values across a $10^{29}$ density contrast at a conservative $10^{-5}$ gives $\alpha\rho_{\rm Earth} < 2\times10^{-5}$, i.e. $\varepsilon - 1 < 2\times10^{-5}$ in ordinary matter. And the primary fares far worse: for the cosmic background to refract at $O(1)$ while local matter stays under bound, it would need a fiber extent below $10^{-4}$ Planck lengths **[V]**. Note the structure — A12 is what lets light see the total space, and A12 is equally what makes the photon a fiber-size meter: one postulate, both consequences. **With the fibration rigid the whole issue vanishes and $\alpha_{\rm fine}$ is exactly constant.**

**Residuals [O].** The extra scalar's contribution to the radiation budget; the Proca tower's phenomenology if ordinary charges have fiber structure.

---

## 13 · What the celestial detour taught, and why it was retired

A second formulation replaced the scale circle by the celestial 2-sphere of null directions (the twistor space). It delivered verified machinery, and it lost the seed. Both facts belong in the record.

**What it delivered, and what transfers.** The Mach lock, the $k$-dial, the $G$-free field equation, the charged secondary, the $(\Delta+3)$ twin theorem, the Kelvin role-democracy, the locality test, the antipodal refocusing of null rays, and the zero time-averaged dipole of a circulating lump — all base physics, all in §10. Three lessons: a massless fiber modulus is an $\alpha\sim\tfrac12$ fifth force (§7); the two partner signs are set by the two operators $\Delta+3$ and $\Delta$; and "staticity in the space of rays" is a weaker condition than staticity in the base.

**Why it was retired [D].** Its fibers are directions at a point; each meets physical 3-space at *one* point, so condition (iii) of §0.5 fails structurally — for any choice of matter or law. Its stress tensor $\int f\,k k\,d\Omega$ integrates over the fiber *at* $x$ and discards direction, never position. And its most elegant result — "the projective postulate dissolves into geometry," both legs of the twistor double fibration turning out to be things general relativity already respects — was the seed's death certificate: a postulate that has become automatic no longer sources gravity at the image. The twin it produced was verified to be real matter (flux $-4\pi$ at both poles), the opposite of what the seed requires. The detour bought its machinery by trading away the requirement, and the trade is reversed here.

**Transfer ledger — every central identity of the celestial guide, and its fate here.**

| celestial identity | status in this guide |
|:--|:--|
| Lorentz $=\mathrm{Conf}(S^2)$; null cone fixes $g$ up to scale; $20 = 10_{\rm Weyl}+10_{\rm Ricci}$ | general facts, no celestial fiber here — not needed |
| dof transfer $21 = 10+8+3$; $T$ = $\ell\le2$ moments; $Z$ complex $\iff$ ASD; $\star^2 = \mathrm{sign}\det g$ | celestial-specific; the 1D count is $15 = 10+4+1$ (§4) |
| Einstein constants $\mu_H,\mu_V$; $\lambda^2/a^2\in\{\tfrac12,1\}$; Hitchin rigidity; O'Neill blocks; reduction with matter | celestial-specific; the 1D reduction is §7 |
| Wong force, cyclotron radius $1/J$, $J$-linear precession | celestial-specific; the 1D force is the scalar fifth force (§8) |
| $PN$ leg; function on $PN$ = free streaming | celestial-specific; the 1D antipodal mechanism is the quotient (§2) |
| flux stabilization $\lambda^2\simeq\kappa f_0^2$, $m\lambda\to1$ | **reproduced** as §7.5 with the winding as the flux; $m_\psi\psi_0 = w\sqrt\varepsilon$ |
| Mach lock, $k$-dial, $G$ theorem, $\bar\rho$, $M_{\rm each}$ | E1–E5 |
| antipodal refocusing; lensed exit | E6, E17 |
| $\ker(\Delta+3)$ = dipoles; $u''+4u = 0$ | E7, §2 |
| zero time-averaged dipole of a circulating lump | E8 |
| charged secondary; RN deduced; opposite-sign partner; equator landmarks | E9, E16, §10 |
| Kelvin self-duality $r\to1/r$; role democracy | E10 |
| budget-normalized couplings; locality on a chaotic configuration | E11, §7, §10 |
| Law III (source-free $\mathcal{F}$, fiber-flux charges) | A12, **with** the fiber-escape derivation the celestial geometry could not supply |
| $\lambda = a$ (no-flux Kähler point) | superseded there and here: $\psi_0$ from the winding |

**The specification any successor must meet.** Conditions (i)–(iii) of §0.5, *and* an unsourced fibration rather than a charge coupling. A 2-dimensional fiber meeting the 3-sphere in more than one point wants a 5-dimensional spatial total space; that is the honest generalization of the line-meets-$S^3$-twice picture, not a substitute for it.

---

## 14 · Differences from the neighbors

**Versus the monopole formulation.** Same arena, gravity sector, postulate, dial; the sole change is that $f$ is unsourced — matter source $\to$ winding. Endpoints $\to$ none; basins $\to$ nothing at all; fog $\to$ localized masses; orbitability inverted from "only trace-free" to "everything."

**Versus straight 5D GR.** Exact agreement iff matter is fiber-smeared; the flat-along-the-ray response of a localized source is the isolated new physics.

**Versus Kaluza–Klein.** Reduction along a homothety-turned-winding rather than an isometry; graviphoton dead by theorem; the fiber field axion-like (compact, winding) and unsourced. The distinctive addition is not the field content but the **projective postulate** on the source.

**Versus screening theories.** Those suppress a scalar's sourcing with a new scale and a new tuning; here the fibration field is simply never sourced, and the one scalar that *is* sourced (the dilaton) is made harmless by a mass the winding supplies. Cheaper by a mechanism.

**Versus particle dark matter.** No new species; the dark component is the quotient image of the luminous one, with distribution and ratio fixed by the topology (§12).

---

## 15 · The radiation-blindness ledger

Six appearances of one selection rule: radiation cannot source the old $f$; needs no fiber stress ($p_u = \tfrac12 T = 0$); was the unique capture-free matter of the monopole era; hence alone localized there; was blind to the retired susceptibility coupling ($\varepsilon = 1$); and is the natural inhabitant of the total space, which is what lets light see the image region as empty (§12). One asterisk: through $\rho - p$ radiation does source the dilaton under $p_u = p$.

---

## 16 · Open problems

1. **The conservation web** — *closed* (§9.5): $\nabla_\mu S^{\mu\nu}$ equals the exchange term of A9, which is $O(10^{-32})$ in the stabilized theory, and the averaged source descends to the quotient conserved. (The $f\leftrightarrow\psi$ dictionary is likewise closed, §7.5.)
2. **The $A_u$ scalar** — *closed* (§12.5): it couples only to the fiber current, which vanishes for $u$-smeared matter, so it is never thermally populated; thermal $\Delta N_{\rm eff} = 0$. Inflationary production not addressed.
3. **Light on $M_5$** — *done* (§12.5): ordinary Maxwell survives on the double cover in the dilaton medium, unrefracted; $\alpha_{\rm fine}$ is constant to $10^{-32}$; the tower is unexcited by $u$-smeared matter. Residual: the extra scalar $A_u$ in the radiation budget, and whether any process $u$-localizes charge enough to excite the tower.
4. **The dark-matter application** — *retired* (§12): the topology fork and the acoustic peaks each exclude it independently. The projection-image mechanism stands as a theorem; its observational use does not.
5. **The projective postulate's consistency** — *settled with a cost* (§9.5): consistent and causal on the quotient; on the cover, gravity connects antipodes instantly while light takes $\pi\ell/c$ — a two-speed causal structure, non-paradoxical in the preferred frame and unobservable beyond the horizon, but a genuine departure from GR. **Its local trace is identified** (§9.6): under naive extension the uncorrelated antipodal image gives $r = 1/\sqrt2$, bias-free, mildly disfavored by current data; each escape switches the seed off. A signpost for when the theory is developed into a cosmology, not a verdict on the draft.
6. **The AdS uplift — the single blocking problem.** The stabilized vacuum has $\Lambda_4 = -\tfrac12 m_\psi^2 < 0$, off the observed value by $10^{60}$ (§10). Solving it would convert the Mach lock from a consistency relation into a genuine prediction of $M_{\rm tot}$; leaving it unsolved is what keeps the theory's Machian content uncashed. This framework has no special claim on it. And it is now also an *internal* problem: §10's arena has $\Lambda_4>0$, §7.5's vacuum has $\Lambda_4<0$ (see §7.5).
7. **The winding sector's dynamics** — *closed*: $w$ is the degree of $f: S^1\to S^1$, changeable only through $|\nabla f| = 0$, which admissibility forbids. Conserved.
8. **Inherited** — the $S^4$ pole question, the tensor-sector projection weight, the lapse-sector correspondence.

---

## 17 · Glossary

**Winding** — the period $\oint df = \ln\lambda$ that creates the fibration topologically. · **Rigid fibration** — the fiber field is unsourced; $f = wu$, fixed by the arena. · **Terminus theorem** — the monopole-era no-go, now historical. · **The dial** — zero-mode share vs fiber smearing. · **Projective postulate** — base gravity reads the fiber average; the load-bearing nonlocality. Equivalent to GR on $\mathbb{RP}^3$ with a $\mathbb{Z}_2$ sheet label that gravity ignores and Maxwell respects. · **Two-speed cover** — on $S^3$, gravity connects antipodes instantly while light takes $\pi\ell/c$; the postulate's true price. · **The seed** — matter at one point of a fiber, gravity at all of them. · **Projection image** — the gravitational-only copy of a mass at its quotient-mates; the dark-matter candidate. · **Mach lock** — $GM_{\rm tot}/c^2\ell = \pi/2$. · **$p_u$** — conserved, quantized fiber momentum.

## 18 · Reference card

| topic | statement |
|:--|:--|
| **Mellin** | $\Delta_4[r^s\Phi] = r^{s-2}[\Delta_{S^3}+s(s+2)]\Phi$; weight $\int\rho\,r\,dr$ |
| **cone** | $\mathrm{Ric}_{ij} = \mathrm{Ric}(h)_{ij} - [aa''+(n-1)a'^2]h_{ij}$; vacuum $\iff\mathrm{Ric}(h) = 2h$; $\Lambda = 1/\ell^2$ |
| **fiber law** | $\Box f = 0$, $\oint df = \ln\lambda$, $f = wu$ exactly — unsourced, rigid |
| **seed** | fiber over $[\hat n]$ = two components $\pm\hat n$; topology + projective postulate, no $\alpha$ |
| **action vs crossing** | antipodal *action* yes (blindness); antipodal *crossing* no (fiber components disjoint, origin removed) |
| **consistency** | Bianchi closes via the A9 exchange term; descends to $\mathbb{RP}^3$; = GR on $\mathbb{RP}^3$ with a $\mathbb{Z}_2$ sheet label gravity ignores |
| **the price** | two-speed cover: gravity instant between antipodes, light $\pi\ell/c$; preferred frame; unobservable |
| **two localizations** | $\mathbb{Z}_2$ $\to$ seed (localized); $u$ $\to$ photon tower (smeared). Independent |
| **$\alpha_{\rm fine}$** | exactly constant at $\alpha=0$ up to $2\pi G\rho\psi_0^2/c^2 \sim 10^{-32}$ |
| **Law I ($G$-free)** | $\ell^2R_{\mu\nu} = \ell^2\psi^{-1}\nabla\nabla\psi + 2(\tau - \tfrac13\tau g)$; $\ell^2\Box\psi = -\tfrac43\psi(\tau_u - \tfrac12\tau)$; stabilized: $+\tfrac{\hat\alpha}{2}\ell^2\nabla\nabla\tau$ on the left |
| **Law I (conventional)** | $R_{\mu\nu} = \psi^{-1}\nabla\nabla\psi + 8\pi(S - \tfrac13 Sg)$; $\Box\psi = -\tfrac{16\pi}{3}\psi(p_u - \tfrac12 S)$ |
| **geodesics** | $a^\mu = (p_u^2/\psi^3)\nabla^\mu\psi$; $m_{\rm eff} = \sqrt{1+p_u^2/\psi^2}$ |
| **GR dial** | zero-mode share $0.18/0.53/0.95/1.00$ at $w/L = 0.05/0.15/0.3/0.5$ |
| **twin theorem** | $u = \Phi\sin\chi$: $u''+4u = 0$; same-sign poles; $\ker(\Delta+3)$ = dipoles |
| **Mach lock** | $GM_{\rm tot}/c^2\ell = \pi/2$ (static consistency relation, not a derivation of $G$); $\bar\rho = c^2/4\pi G\ell^2$; $\Lambda\ell^2 = 1$ |
| **$k$-dial** | $v^2/c^2 = k(\pi-2\chi+\sin2\chi)/2\sin2\chi$; $v^2_{\rm eq} = kc^2$ |
| **$G$** | input, $= G_5/C$ with $C = \psi_0\ln\lambda$; on the static background $= \pi c^2\ell/2M_{\rm tot}$ |
| **PPN** | unstabilized $\gamma = 1/2$ (dead); stabilized $\gamma = 1$ exactly |
| **inversion** | if $\Lambda_4>0$: $M_{\rm tot}$ predicted from $(G_5,\Lambda_5,w,\ln\lambda)$ — blocked by the $10^{60}$ uplift |
| **charged node** | $\phi_e\propto\cot\chi$; RN near-zone; opposite-sign partner |
| **stabilization** | $\psi_0^2 = 3w^2/4\lvert\Lambda_5\rvert$; $m_\psi\psi_0 = w$; $\Lambda_4 = \tfrac23\Lambda_5$; Yukawa $\alpha = \tfrac13$, range $\psi_0$ |
| **fiber escape** | $\sigma = -\partial_r(r^3E_r)$ on $S^3$; winding evades the balance theorem |
| **electrodynamics** | $\nabla_\mu(\psi\mathcal{F}^{\mu\nu}) = \psi\mathcal{J}^\nu - \partial_u(\psi^{-1}\mathcal{F}_u{}^\nu)$; $\epsilon\mu = 1$; Proca tower $2\pi n/C$; light on the cover, gravity on the quotient |
| **dark matter** | image of luminous matter under $S^3\to S^3/\Gamma$; ratio $|\Gamma|-1$ if co-located |
| **legacy** | basin $\theta = 1.644(m/M)^{1/3}$, contrast $\approx1$; pinch anisotropy $3$ |

*Numerics: softened potentials and 2D slices for the [M] items; coefficients are estimates at that fidelity. The concentration bound, the cone theorem, the reduction, the twin theorem, the Mach lock, and the endpoint-freeness are exact.*
