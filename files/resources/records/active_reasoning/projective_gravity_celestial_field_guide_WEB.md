*Here's a note from Ajax:* Ok hello! So what this document is is a snippet of some of my active reasoning dynamical ideas I'm trying to string together. Specifically how it was made was that on August 31, 2026 and the week leading up to it I inputted about a dozen different intuitive constraints into Claude that I had been building up to throughout 2026. Note that in my journal entries I have the records of all of these intuitions as I first stated them months ago through more recently, plus the actual prompts to Claude itself in which I reveal them. A couple of examples are that I was really stuck two months ago with trying to imagine in my 3-sphere model a kind of "shaft" of matter to get at the kind of antipodal-pair dynamics I was looking for, however in quick succession over a couple of days in early August I had the thought that I could instead just use equivalence classes over lines in R4 space, then use the EFEs as a constraint ON THOSE LINES IN THE DEEPER SPACE, and then simply have the base space to it as a kind of RP3 over which orbits actually occur gravitationally. So yeah, basically the process was me having hidden biases in my reasoning together with a clear win condition, and then me gradually figuring out how to shed the biases to bring out the highlights in the win condition. And, well, that brings us to right now---only after I had all these constraints, (like for example I had intuited already that the fibers "bunch up" around mass so as to keep the primary object in the idealized model as defining the "radial direction" for the fibers while at once not actually contributing to the gravity dynamics directly accordingly, so it was meant to be a kind of trade-off between the primary and secondary following the same law while the secondary itself feels the effects of it only and then within those effects actual EFE stuff getting their scope---so yeah to be clear I entirely established the intricate graph-structure of constraints and then fed THAT into the AI, since I can make those graphs due to the months of bias-shedding, while it can simply implement them rather than create them), did I feed them as prompts into Claude, and ecstatically I got to watch it render them into real equations by deducing from what I had set up as well as formalizing some of my looser intuitions (like "bunching" became "dielectric" after my guess to the AI that it might be Poisson's equation was wrong). But yeah, I have all the records of everything in case there's ever a question, but to be clear I'm a guy who designed a very specific painting in my head without owning the paint to actually draw it in equations. Claude provided that paint, and indeed corrected some of my formalism guesses of the constraints, but the painting existed well before Claude painted it. (And indeed I still have a bunch of biases as we speak in things that didn’t yet make it into this brief doc here, as even in the last couple of days I shifted associating one thing with the total space to associating it with the base space, which gives me another angle on inductively landing the next unification of two concepts in the sequence. So in other words it’s still an ongoing process, so much of what will show up in the next draft is something I already have intuited right now, but just haven’t rendered and posted yet).

# Projective Gravity — Dielectric Formulation

### A Field Guide, third edition

> **Status tags.** **[V]** verified symbolically or numerically in this program · **[M]** measured in a numerical experiment (softened potentials, 2D slices unless noted) · **[T]** established theorem, cited · **[D]** derived here from **[V]/[T]** material · **[S]** sketch · **[O]** open.
>
> **Conventions.** $G = c = 1$ unless restored; $\ell$ = radius of the base 3-sphere; "total space" = the higher-dimensional arena where matter lives; "base" = the space of fibers, where gravity lives.
>
> **Reading guide.** The idea and its purpose: §0–§0.5. The mechanism: §6. Gravity, the emergent constant, and the stabilized dilaton: §7, §7.5, §10. The seed as a prediction: §12; the electrodynamics that makes it consistent: §12.5. What the celestial detour taught and why it was retired: §13.

---

## 0 · The idea in one paragraph

Gravity lives not on spacetime's full arena but on the **space of fibers** of a foliation; matter inhabits the total space, and gravity sees only its fiber-averaged projection. The founding example fibers Euclidean $\mathbb{R}^4$ by lines through the origin, with base $S^3/\pm = \mathbb{RP}^3$: each line meets the physical 3-sphere at two antipodal points, so the base cannot tell them apart. The first formulation coupled the fibration field to matter as a *charge* and failed catastrophically — every gravitating object captured the fibers around it and smeared into fog. The present formulation repairs this with one structural change: **matter couples to the fibration as a dielectric, not a charge.** It bends and bunches fibers without ever terminating them, the background fibration being supplied *topologically* by a winding condition. The result keeps everything that worked — the cone-generated $\Lambda$, the Kaluza–Klein reduction, the trace taxonomy, the two-population geodesics, the exact-GR limit — while restoring localized masses and Keplerian orbits.

## 0.5 · The seed, and what it is for

The founding requirement — the *seed* — is stated here exactly, because a later formulation lost it and the loss was decisive.

> **The seed.** Place a star at a point $\hat n$ of the physical 3-sphere inside the total space. Travel to the antipode $-\hat n$. **There is nothing there** — no matter, nothing to emit, absorb, or reflect light. Yet the base point $[\hat n] = \{\hat n, -\hat n\}$ carries the star's mass, so gravity, living on the base, acts at $-\hat n$ exactly as it acts at $\hat n$. *The star speaks gravitationally for every point of its fiber, and materially for one.*

**Its purpose is dark matter.** If light propagates in the total space while gravity reads the base, then every luminous mass has a projection-image that gravitates and lenses but neither emits, absorbs, nor scatters — the observed phenomenology of dark matter, produced by the geometry of the projection rather than by a new particle. Section 12 states this as a prediction with its tensions.

**The condition the seed imposes** on any formulation, stated as a theorem-shaped requirement **[D]**: a projection $\pi: E\to B$ with (i) matter on $E$, localized on a fiber; (ii) gravity on $B$ sourced by the fiber-integral of matter; (iii) **each fiber meeting physical 3-space at more than one point.** Conditions (ii)+(iii) together say $G_{\mu\nu} = 8\pi\langle T_{\mu\nu}\rangle_{\rm fiber}$ — gravity sourced by the *orbit-averaged* stress tensor, a genuine nonlocal modification of general relativity. **That modification is the projective postulate.** A formulation in which the postulate becomes automatic (§13) has lost the seed.

---

## 1 · The founding move and its two constraints

The Newtonian recipe: project the 4-space density onto the base along the radial lines; run Poisson's equation on the sphere. Two constraints were laid down for any dynamical fibration: (1) fibers respond to matter, bunching toward concentrations; (2) symmetric matter corresponds to radial fibers, deviations in one-to-one correspondence.

The dielectric theory answers them thus. Fibers *exist* for a topological reason (the winding, §6) and are *oriented* by matter two ways. A spherically symmetric central concentration preserves exact radiality: a uniform high-permittivity slab transverse to the flow transmits field lines straight through **[V]**. And in the conduction analogy (permittivity as conductivity, the winding as an EMF around the fiber circle) Thomson-type variational principles concentrate flux along high-conductance channels, so a dominant central mass actively *recruits* the fibers through itself **[S]**. Asymmetries bend fibers toward the excess by the funneling of §6.

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

The total metric decomposes as $15 = 10 + 4 + 1$: base metric $g^{(4)}$, tilt connection $A_\mu$, fiber length $\psi$. Because the fibration is the flow of a closed one-form $df$ — multivalued $f$ is fine; winding does not spoil closedness — the fibers are hypersurface-orthogonal, Frobenius applies, and $A_\mu\equiv0$ **is a theorem**. The sole fiber degree of freedom is the dilaton $\psi$, and "fibers bunching" is a property of the projection map, realized by refraction.

---

## 5 · The total space: the Hopf choice, doubly load-bearing

The candidate total spaces are conformal rescalings of one cylinder $\mathbb{R}_u\times S^3$ **[V]**: the bare cone (noncompact fiber), the Hopf manifold $S^1\times S^3$ (dilation quotient $u\sim u+\ln\lambda$), and $S^4\setminus\{p,\bar p\}$ (degenerate at the poles). The working choice is the Hopf manifold, load-bearing twice: compactness makes the fiber average $\oint du$ well-defined, and $\chi(S^1\times S^3) = 0$ **permits a nowhere-vanishing closed one-form** — exactly what a sourceless fibration requires (Poincaré–Hopf forbids it on $S^4$). The "origin" of $\mathbb{R}^4$ sits at $u = -\infty$ and is removed: the central concentration is matter localized at one region of the fiber circle across all base directions — a slab, not a point. **The primary is the background.**

---

## 6 · The fiber law: from charge to dielectric

### 6.1 The monopole disease

The original law $\Box_5 f = \kappa T$ makes matter a *charge* of the fibration: every trace-full object is a flow endpoint. The failure was quantitative **[M]**: basin radius $\theta = 1.644\,(m/M)^{1/3}$ — the Hill scaling — so mass fraction and volume fraction coincide and the density contrast is $\approx 1$ (measured $1.03$–$1.27$): *a point mass smears itself to background density.* No shape or extension escapes. The verdict is the **terminus theorem**: under monopole coupling, sourcing the fibration and being orbitable are mutually exclusive. A sign flip repairs nothing — an endpoint is an endpoint.

### 6.2 The dielectric law

> ### ◆ THE FIBRATION LAW
> $$\boxed{\;\nabla_\mu\big[\varepsilon(T)\,\nabla^\mu f\big] = 0, \qquad \oint_{\rm fiber} df = \ln\lambda, \qquad \varepsilon = 1 - \alpha T\;}$$
> A **conservation law**: the flux $\varepsilon\nabla f$ is divergence-free, so **fibers never begin or end anywhere** **[M: $\min|\nabla f| > 0$ along every traced line]**. The winding replaces the matter source. Matter *refracts* the flow: an object with $\varepsilon > 1$ draws field lines in and passes them through — funneling half-width $b = 2\varepsilon R/(1+\varepsilon)$ in the 2D slice **[M: predicted $1.667R$ at $\varepsilon = 5$, measured $1.6$–$1.7R$]**.

### 6.3 The boundedness theorem

For a ball of permittivity $\varepsilon$ in $n$ spatial dimensions **[V]**:

$$E_{\rm in} = \frac{n E_0}{\varepsilon + n - 1}, \qquad \frac{\varepsilon E_{\rm in}}{E_0} = \frac{n\varepsilon}{\varepsilon + n - 1}\;\to\; n$$

**No object, however massive, can concentrate fibers onto itself by more than a factor of 4.** A mass's base footprint is its fiber-tube, spread by an order-one, dimension-fixed factor. Verified directly: at $\varepsilon = 2, 6, 50, 1000$ in a 2D test the concentration ran $1.36, 1.82, 2.15, 2.20$ — climbing to the ceiling and stopping **[V]**. Localized base masses are generic; the base contains solar systems.

### 6.4 The taxonomy

| matter | trace $T$ | $\varepsilon$ | fiber behavior |
|---|---|---|---|
| dust | $-\rho$ | $1+\alpha\rho > 1$ | **paramagnet** — bunches fibers |
| **radiation** | $0$ | $=1$ | **blind** — passes unrefracted |
| stiff | $+2\rho$ | $1-2\alpha\rho<1$ | **diamagnet** — expels fibers |
| vacuum energy | $-4\rho$ | $1+4\alpha\rho$ | strongly paramagnetic |

The stiff sector has a sharp threshold at $\alpha\rho = \tfrac12$: $\varepsilon\to0$, a **fibration insulator**. $\varepsilon > 0$ joins the admissibility list — it is exactly ellipticity of the fiber equation.

### 6.5 The susceptibility channel

$\varepsilon(T)|\nabla f|^2$ is an interaction energy: trace-full matter is drawn toward fiber bunches, hence toward other masses' funnels. Matter attracts matter through the fiber field, with strength set by $\alpha$ and bounded by the concentration theorem. Benign, interesting, or fatal is the first computation the branch owes **[O]**.

---

## 7 · Gravity: the 5D reduction

With the twist-free ansatz $g_5 = g^{(4)} + \psi^2 du^2$, the 5D Einstein equations reduce to **[V]**:

> ### ◆ LAW I — GRAVITY
> **Budget-normalized ($G$-free) form — the default.** With $\ell \equiv (V/2\pi^2)^{1/3}$ the volume radius and $\bar\epsilon \equiv \mathcal{E}/V$ the mean energy density of the closed slice — global invariants of the solution, privileging no node — and $\tau_{\mu\nu} \equiv S_{\mu\nu}/\bar\epsilon$ the fiber-averaged stress tensor as a fraction of the budget:
> $$\boxed{\;\ell^2 R^{(4)}_{\mu\nu} \;=\; \ell^2\,\psi^{-1}\nabla_\mu\nabla_\nu\psi \;+\; 2\Big(\tau_{\mu\nu} - \tfrac13\,\tau\,g^{(4)}_{\mu\nu}\Big)\;}$$
> $$\ell^2\,\Box\psi \;=\; -\frac43\,\psi\Big(\tau_u - \tfrac12\tau\Big) \;\;\to\;\; -\frac23\,\psi\,(\hat\rho - \hat p)\quad\text{under } p_u = p$$
> Both sides dimensionless; the couplings are the pure numbers $2$ and $\tfrac43$, fixed by the Mach lock $8\pi G\bar\epsilon\ell^2/c^4 = 2$ on the homogeneous background, where the dilaton term vanishes because $\psi_0$ tracks a uniform $\varepsilon$ **[V]**. $G$ appears nowhere; it is a theorem of the solution, $G = \pi c^2\ell/2M_{\rm tot}$ (§10). The unit-conversion job $G$ performed is reassigned to the pair $(\ell,\mathcal{E})$: one length from geometry, one energy from inventory.
>
> **With the stabilized dilaton (§7.5)** the fiber term becomes $-\tfrac{\hat\alpha}{2}\ell^2\nabla_\mu\nabla_\nu\tau$ with $\hat\alpha = \alpha\bar\epsilon$ a pure number, so the full field equation is
> $$\boxed{\;\ell^2 R^{(4)}_{\mu\nu} + \frac{\hat\alpha}{2}\,\ell^2\,\nabla_\mu\nabla_\nu\tau \;=\; 2\Big(\tau_{\mu\nu} - \tfrac13\,\tau\,g^{(4)}_{\mu\nu}\Big)\;}$$
> — GR's structure with the five-dimensional $\tfrac13$ and one susceptibility correction, every coefficient a pure number, every dimension carried by $\ell$ and $\tau$.
>
> *Equivalent conventional form* ($G = c = 1$): $R^{(4)}_{\mu\nu} = \psi^{-1}\nabla_\mu\nabla_\nu\psi + 8\pi(S_{\mu\nu} - \tfrac13 S g_{\mu\nu})$, $\;\Box\psi = -\tfrac{16\pi}{3}\psi(p_u - \tfrac12 S)$. Structurally the reduction of static vacuum gravity along a Killing vector; the $\tfrac13$ is the fingerprint of the five-dimensional origin. The source is the **fiber-averaged** stress tensor $S_{\mu\nu} = \oint T_{\mu\nu}\,du$ — the projective postulate at work.

**The dictionary seam [O].** The fiber proper length per unit $f$ is $1/|\nabla f|$, so $\psi$ and $|\nabla f|$ are tied; the dielectric equation fixes $|\nabla f|$ from $\varepsilon$ and the winding, the reduced Einstein equation fixes $\psi$ from matter. Their compatibility is the theory's central consistency question.

**The lesson from the celestial detour, acted on.** A massless fiber-size modulus is a long-range fifth force. The dilaton $\psi$ is exactly such a modulus — and this theory already contains the flux that stabilizes it. §7.5 does the computation.

### 7.5 Dilaton stabilization by the winding

**The problem.** In vacuum $\Box\psi = 0$: the dilaton is a Brans–Dicke scalar with $\omega = 0$, whose fifth force has Yukawa strength $\alpha = 1/(2\omega+3) = \tfrac13$ and infinite range **[T]** — excluded by solar-system tests at the $10^{-5}$ level. The celestial detour's lesson was that a flux threading the fiber gives the modulus a mass. Here the flux is already present: **the winding of $f$.**

**The dictionary closes first [V].** $f = wu$ is an *exact* solution of the dielectric law $\nabla_\mu[\varepsilon\nabla^\mu f] = 0$ for any base-dependent $\varepsilon(x)$ and $\psi(x)$, with $|\nabla f| = w/\psi$. So the §7 seam — $\psi$ versus $1/|\nabla f|$ — is closed by the winding for fiber-smeared matter; refraction is a fiber-*localized*-matter effect ($\varepsilon$ depending on $u$), consistent with the GR dial.

**The reduction with the winding energy [V].** With $g_5 = g^{(4)} + \psi^2du^2$, $u\sim u+\ln\lambda$, a 5D cosmological constant $\Lambda_5$, and the winding energy $\tfrac12\varepsilon(\nabla f)^2 = \varepsilon w^2/2\psi^2$, the 5D action reduces to Brans–Dicke with $\omega = 0$ and a potential:

$$S_4 = \ln\lambda\int\sqrt{g_4}\,\Big[\psi R_4 - U(\psi)\Big], \qquad U(\psi) = 2\Lambda_5\,\psi + \frac{\varepsilon w^2}{2\psi}$$

In the Einstein frame $\tilde g = (\psi/\psi_0)\,g$, with $x = \psi/\psi_0$ and canonical field $\phi = \sqrt3\ln x$, the potential is $V(x) = 2\Lambda_5/x + \varepsilon w^2/(2\psi_0^2x^3)$.

**The result [V].** A minimum exists if and only if $\Lambda_5 < 0$, and then

$$\boxed{\;\psi_0^2 = \frac{3\,\varepsilon w^2}{4|\Lambda_5|}, \qquad m_\psi^2 = \frac43|\Lambda_5| = \frac{\varepsilon w^2}{\psi_0^2}, \qquad m_\psi\,\psi_0 = w\sqrt{\varepsilon}\;}$$

Three readings. The fiber size is set by the winding, and $w$ is quantized — so $\psi_0$ is fixed by an integer, exactly as the flux integer fixed the fiber in the celestial theory. The modulus Compton wavelength equals the fiber size: $m_\psi\psi_0 = 1$ for one winding in vacuum, the same law $m\lambda\to1$ found there. And the fifth force becomes a Yukawa of strength $\tfrac13$ and range $\psi_0$: torsion-balance searches then bound the fiber at roughly tens of microns.

**The modulus tracks matter [D].** Since $\psi_0^2\propto\varepsilon = 1-\alpha T$, the stabilized fiber size responds to the local trace, $\delta\psi_0/\psi_0 = -\alpha T/2$. For fibers far smaller than the matter's variation scale the response is adiabatic, and Law I's dilaton term becomes

$$\psi^{-1}\nabla_\mu\nabla_\nu\psi \;\longrightarrow\; -\frac{\alpha}{2}\,\nabla_\mu\nabla_\nu T$$

**the susceptibility channel of §6.5, now a computable correction** — second derivatives of the trace, negligible for smooth distributions, largest at sharp density edges.

**The price [O].** At the minimum $\Lambda_4 = \tfrac23\Lambda_5 = -\tfrac12 m_\psi^2 < 0$: the winding-stabilized vacuum is anti-de Sitter, with $|\Lambda_4|$ of order the modulus mass squared. The observed small positive $\Lambda$ needs an uplift of that size — the cosmological-constant problem in Kaluza–Klein dress, shared with the celestial theory's $\Lambda_6$ tuning. The cone theorem's positive $\Lambda = 1/\ell^2$ (§3) belongs to the cone geometry; reconciling it with the Hopf-compactified vacuum's negative $\Lambda_4$ is the open uplift problem.

---

## 8 · Geodesics: the two populations

Because $\partial_u$ is Killing, fiber momentum $p_u = \psi^2\dot u$ is conserved and quantized ($p_u\propto n/\ln\lambda$), and the base projection of the 5D geodesic equation gives **[V]**:

$$\frac{D\dot x^\mu}{d\lambda} = \frac{p_u^2}{\psi^3}\,\nabla^\mu\psi, \qquad m_{\rm eff} = \sqrt{1 + p_u^2/\psi^2}$$

**Neutral matter ($p_u = 0$)** follows base geodesics exactly. Trace-full lumps project to compact base masses (§6.3), so the base contains Schwarzschild-like wells in the closed background, and the closed-universe orbit machinery — exact static solver, rosettes, trapped orbits — describes this theory's actual solar systems.

**Charged matter ($p_u\neq0$)** feels the scalar fifth force, sliding toward large $\psi$. The pinch points of the monopole era **no longer exist**: divergence-free flux with $\varepsilon > 0$ admits no critical points. Particles are gently expelled from paramagnetic interiors and drawn to funnel throats, all effects capped by the factor-$n$ theorem.

---

## 9 · The projective postulate and the GR dial

> ### ■ THE PROJECTIVE POSTULATE
> Mass at $B$ acts as if at $A$ along the same fiber; base gravity reads only $S_{\mu\nu} = \oint T_{\mu\nu}\,du$.

Its distance from GR is a dial: a source of fiber-width $w$ on a fiber of circumference $L$ puts zero-mode share $0.18/0.53/0.95/1.00$ at $w/L = 0.05/0.15/0.3/0.5$ **[M]**. Fiber-smeared matter reproduces GR exactly; fiber-localized matter is maximally projective. The base Bianchi identity forces $\nabla^\mu S_{\mu\nu} = 0$, and the compact fiber converts 5D conservation into conservation of fiber averages, with $\langle p_u\rangle = \langle p\rangle$ and $\partial_u p_u = 0$ absent fiber flux.

**This postulate is load-bearing.** It is the nonlocality that the seed requires (§0.5). It is a *postulate* precisely because it is not automatic — and its not being automatic is what makes the antipodal image gravitate.

---

## 10 · The idealized universe — a $G$-free dossier (salvaged)

*Everything in this section is closed-universe physics on the base, independent of the fiber law, and transfers to any formulation with a closed 3-sphere spatial section. Stated in the GR limit of the dial; dilaton corrections are §7's seam.*

**The Mach lock [V].** The static closure relation fixes $\bar\rho = c^2/4\pi G\ell^2$ and $\Lambda = 1/\ell^2$; multiplying by the 3-sphere's volume:

$$\boxed{\;\frac{G\,M_{\rm tot}}{c^2\,\ell} = \frac{\pi}{2}\;}$$

Sciama's order-unity Machian relation with its coefficient supplied, exactly.

**The $k$-dial [V — dynamically confirmed, wobble $10^{-13}$].** With the lumps carrying fraction $k$ of the budget at antipodal nodes, the circular-orbit speed at colatitude $\chi = d/\ell$ is

$$\boxed{\;\frac{v^2(\chi)}{c^2} = k\,\frac{\pi - 2\chi + \sin 2\chi}{2\sin 2\chi}\;}$$

Landmarks: near a node $v^2\to G(M_l/2)/d$ (Kepler, the $\tfrac12$ being the budget's split between the poles); at the equator $v^2/c^2 = k$ exactly, a stationary minimum — **the budget meter**; at parity $k = 1$, light speed at the midpoint, mass-independent. The lone-mass Kepler continuation would give $\tfrac12$ there: the factor of $2$ is the antipode speaking.

**$G$ as theorem [V].**

$$G = \frac{\pi c^2\ell}{2M_{\rm tot}} = \frac{\pi\ell\,v^2_{\rm eq}}{2M_{\rm lumps}} = \frac{c^2}{4\pi\bar\rho\,\ell^2}$$

Measurement protocol: circumference $\to\ell$; midpoint orbit $\to v^2$; inventory $\to M$. A hidden $G$ is recovered to $10^{-10}$.

**Role democracy [V].** In the stereographic chart $r = \tan(\chi/2)$ the two-node potential is $\Phi/c^2 = k(\pi r/8 + \tfrac12 - \pi/8r)$, **identical** under $r\to1/r$: a $-\pi/8r$ pole (the visible mass) plus an isotropic $+\pi r/8$ pull toward chart-infinity (the antipodal node, smeared over the sky only by the chart). "Primary" and "secondary" are frame labels; any node can be sent to infinity, none is privileged. This is the Kelvin transform: the MP metric's constant "1" is a point mass at infinity, exactly.

**Locality [V].** The weak-field equation holds pointwise for a random 8-lump configuration with the coupling fixed by the total budget alone: a local PDE, two global scalars, no primary. Staticity adds the global filter "zero dipole" (§2) — a constraint on configurations, not a nonlocality of the law.

**The charged secondary [V].** On the closed background, Maxwell's total-charge-zero forces a $-Q$ somewhere; its field lines run pole to pole as a conserved tube inside the 3-sphere. With the partner at the symmetric antipode:

$$\phi_e = \frac{Q}{4\pi\epsilon_0\ell}\cot\chi, \qquad \Phi = -\frac{2GM}{\pi\ell}\Big(\frac{\pi}{2}-\chi\Big)\cot\chi + \frac{GQ^2}{8\pi\epsilon_0 c^2\ell^2}\csc^2\chi$$

Near the charge this is Reissner–Nordström, **deduced**: the field's own energy gravitates with the universal $G$. Budget form: $\Phi/c^2 = -(M/M_{\rm tot})(\tfrac\pi2-\chi)\cot\chi + \tfrac{\pi^2}{8}(Q/Q_{\rm ext})^2\csc^2\chi$ with $Q_{\rm ext} = M_{\rm tot}\sqrt{4\pi\epsilon_0 G}$. The two operators fix the two partner signs: mass obeys $\Delta+3$ (same-sign poles, same-sign twin); charge obeys $\Delta$ (opposite-sign poles, $\pm Q$).

**The E-series.**

| # | identity | status |
|:--|:--|:--|
| E1 | $\Lambda\ell^2 = 1$ (closure eigenvalue) | [V] |
| E2 | $GM_{\rm tot}/c^2\ell = \pi/2$ (Mach lock) | [V] |
| E3 | $v^2_{\rm eq}/c^2 = M_{\rm lumps}/M_{\rm tot}$ ($k$-dial) | [V] |
| E4 | $\bar\rho = c^2/4\pi G\ell^2$ | [V] |
| E5 | $M_{\rm each}(k{=}1) = \pi c^2\ell/4G$ | [V] |
| E6 | null rays refocus at the antipode at $t = \pi\ell/c$; period $2\pi\ell/c$ | [V] |
| E7 | $\ker(\Delta_{S^3}+3)$ = dipoles; $u = \Phi\sin\chi$ gives $u''+4u = 0$ | [V] |
| E8 | a single lump circulating a great circle has zero time-averaged dipole | [V] |
| E9 | charged secondary: $\phi_e\propto\cot\chi$, mass $\propto(\chi-\tfrac\pi2)\cot\chi$, charge $\propto\csc^2\chi$ | [V] |
| E10 | stereographic self-duality $r\to1/r$ of the two-node potential | [V] |
| E11 | budget-normalized couplings: $8\pi G\bar\epsilon\ell^2/c^4 = 2$ (Law I), $\tfrac43$ (dilaton), $\hat\alpha$ (susceptibility) — all pure numbers | [V] |
| E12 | fiber-escape identity: $\sigma = -\partial_r(r^3E_r)$ on the slice; net zero for off-slice sources | [V] |
| E13 | $f = wu$ solves the dielectric law for any $\varepsilon(x),\psi(x)$; $\lvert\nabla f\rvert = w/\psi$ | [V] |
| E14 | stabilization: $\psi_0^2 = 3\varepsilon w^2/4\lvert\Lambda_5\rvert$; $m_\psi\psi_0 = w\sqrt\varepsilon$ | [V] |
| E15 | $\Lambda_4 = \tfrac23\Lambda_5 = -\tfrac12 m_\psi^2$ at the stabilized vacuum | [V] |
| E16 | charged node: gravity's force vanishes at the equator (both terms); electric force $Q/4\pi\epsilon_0\ell$ there | [V] |
| E17 | a lump of index contrast $0.03$ shifts the null-ray refocus $0.56°$ off the antipode and blurs it | [V] |
| E18 | 5D Maxwell reduces to $\nabla_\mu(\psi\mathcal{F}^{\mu\nu}) = \psi\mathcal{J}^\nu - \partial_u(\psi^{-1}\mathcal{F}_u{}^\nu)$: a medium with $\epsilon = 1/\mu = \psi$, $\epsilon\mu = 1$ | [V] |
| E19 | fiber photon modes are Proca with $m_n = 2\pi n/C_{\rm fiber}$ ($\approx 25$ meV at $50\,\mu$m) | [D] |
| E20 | light lives on the double cover $S^3$, in the antipodally symmetric metric: lensed at the image, not emitted there | [D] |

---

## 11 · The axioms, third edition

> ### ■ ARENA
> - **A1.** Total spacetime $M_5 = \mathbb{R}_t\times S^1_u\times S^3$, fiber spacelike and compact.
> - **A2.** Base $B_4 = \mathbb{R}_t\times\mathbb{RP}^3$ (or $\mathbb{R}_t\times S^3/\Gamma$).
> - **A3.** $\chi(M_5) = 0$, enabling the winding form.
> - **A3′.** A 5D cosmological constant $\Lambda_5 < 0$ (required for the winding to stabilize the fiber, §7.5).

> ### ■ FIELDS
> - **A4.** Base metric $g^{(4)}$ (10).
> - **A5.** Compact fiber scalar $f$, winding $\oint df = \ln\lambda$; dilaton $\psi$ with $|\nabla f| = w/\psi$ on the winding solution, stabilized at $\psi_0^2 = 3\varepsilon w^2/4|\Lambda_5|$ with mass $1/\psi_0$ (§7.5).
> - **A6.** $A_\mu\equiv0$ by Frobenius.

> ### ◆ LAW I — GRAVITY
> - **A7.** The projective postulate: base gravity reads $S_{\mu\nu} = \oint T_{\mu\nu}\,du$.
> - **A8.** $\ell^2 R^{(4)}_{\mu\nu} = \ell^2\psi^{-1}\nabla_\mu\nabla_\nu\psi + 2(\tau_{\mu\nu} - \tfrac13\tau g_{\mu\nu})$; $\;\ell^2\Box\psi = -\tfrac43\psi(\tau_u - \tfrac12\tau)$, with $\tau = S/\bar\epsilon$. No coupling constant: $G$ is a theorem (D5).
> - **A9.** Conservation with exchange: $p' + (\rho+p)\Psi' + (p - p_u)\psi'/\psi = 0$; matter condition $p_u = p$.

> ### ◆ LAW II — FIBRATION
> - **A10.** Fibers are the flow lines of $\nabla f$.
> - **A11.** $\nabla_\mu[\varepsilon(T)\nabla^\mu f] = 0$, $\varepsilon = 1-\alpha T$: **no monopole coupling of matter to $f$.**

> ### ◇ LAW III — ELECTROMAGNETISM (candidate slot)
> - **A12 (adopted, §12.5).** The electromagnetic 2-form lives on $M_5$ — the double cover $\mathbb{R}_t\times S^1_u\times S^3$, not the gravitational base — with its 5D current supported on charged matter: $d\mathcal{F} = 0$, $d\star_5\mathcal{F} = \star_5\mathcal{J}$. The source-free case $\mathcal{J} = 0$, with charges as winding defects, is the Wheeler option **[S]**. Its reduction is derived in §12.5: ordinary Maxwell survives.
> - **Gauss's law as fiber escape [V].** In this geometry the fiber *is* the radial direction of $\mathbb{R}^4$ — transverse to the physical 3-sphere. The 4D divergence in polar form, $\nabla\!\cdot\!E = r^{-3}\partial_r(r^3E_r) + r^{-1}\nabla_{S^3}\!\cdot E_\parallel$, gives a source-free field an apparent 3-charge on the slice
> $$\sigma(\hat n) = -\,\partial_r\big(r^3E_r\big)\big|_{r=1}$$
> — Gauss's law on the 3-sphere read as **flux escaping along the fiber, through the interior of the 3-sphere**. For a 4D Coulomb charge just off the slice this yields a sharp positive apparent charge beneath it and a diffuse negative sea, netting zero by Gauss's theorem on the 4-ball. This is the derivation the celestial fibers could not support: there the fiber was directions at a point, and the escape identity had no direction to escape along.
> - **The loophole.** Net base charge from plumbing alone needs either a drain at the cone point or a **multivalued potential** (the balance theorem holds only for single-valued fields). This theory's fiber field is multivalued by construction, so the winding sector is the natural home of Wheeler's charge-without-charge **[S]**. Its consequence for base electrodynamics is open problem 3.

> ### ▣ DERIVED
> - **D1.** $\Lambda = 1/\ell^2$ from the cone (§3). **D2.** No fiber endpoints; concentration $\le n$ (§6.3). **D3.** $p_u = 0$ geodesics are base geodesics. **D4.** The static twin is the quotient (§2). **D5.** Mach lock, $k$-dial, $G$ as theorem (§10).

**Admissibility.** $\nabla f$ spacelike, nowhere zero; $\varepsilon > 0$ everywhere; fiber compact; energy conditions on $(\rho, p, p_u)$.

**Free parameters (budget-normalized ledger).** $\hat\alpha$ (susceptibility, pure number) · the winding integer $w$ · one scale, $|\Lambda_5|$ (equivalently the stabilized fiber size $\psi_0$, bounded by fifth-force searches at tens of microns) · the quotient group $\Gamma$ · the equation of state. $G$ is a theorem; $\Lambda\ell^2$ an eigenvalue; $c$ from the causal structure of $M_5$; the dilaton mass is $1/\psi_0$, not a dial.

---

## 12 · The seed as a prediction: dark matter as projection shadow

**The mechanism [D].** Let a cloud of luminous matter occupy a region $R$ of the physical 3-sphere inside $M_5$. Under the quotient, the base region $[R]$ carries its mass. Lift the base gravitational field back to the 3-sphere: it has wells at $R$ **and at the image $\bar R$**. Now let light propagate on $M_5$ (A12). At $\bar R$ there is no matter in the total space: nothing emits, nothing absorbs, nothing scatters — but the well is there, so light passing $\bar R$ is **lensed**. The image region is, operationally, dark matter: gravitation and lensing without luminosity or interaction.

$$\boxed{\;\text{dark matter} = \text{the projection image of luminous matter}\;}$$

Its properties are inherited, not fitted: collisionless (nothing there to collide), non-luminous, non-absorbing, gravitating and lensing with the full mass of its source, and tracking its source exactly through the quotient map.

**Three consistency facts already in hand.**
- *Radiation is the natural dweller of the total space.* It is blind to the fibration ($\varepsilon = 1$), needs no fiber stress, and cannot source $f$ — the radiation-blindness ledger's six entries are all reasons A12 costs nothing.
- *The image is diluted, not copied* **[M]**: the base footprint of a dust cloud is spread by a factor $0.25$–$0.75$, of stiff matter concentrated by $\sim15\times$. **The dark image of ordinary matter is more diffuse than its source** — halo-like rather than cusp-like.
- *The static sector forces symmetric sources* (§2), so in the static idealization luminous matter at $R$ is accompanied by luminous matter at $\bar R$, and each is the other's image: dark matter is then **co-located** with luminous matter, image-for-image.

**The ratio, and an arithmetic worth flagging [S].** With $\Gamma = \mathbb{Z}_2$ each luminous lump has one image, so $\Omega_{\rm dark}/\Omega_{\rm lum} = 1$ in the co-located static picture. With a general free quotient $S^3/\Gamma$ (all admitted by the cone theorem) each lump has $|\Gamma| - 1$ images and the ratio is $|\Gamma| - 1$. The observed $\Omega_c/\Omega_b \approx 5.4$ sits between $|\Gamma| = 6$ and $7$. This is a curiosity, not a fit: it assumes exact $\Gamma$-symmetry of the luminous distribution, which the static sector demands and the dynamical sector does not.

**The tensions, stated honestly [O].**
1. *Distribution.* Dynamically, the image of a galaxy is a dark galaxy at the antipode, not a halo around the luminous one. Flat rotation curves around *luminous* galaxies are not produced by this mechanism unless the luminous distribution is itself (nearly) $\Gamma$-symmetric — a strong assumption about the universe, or a statement that the fundamental domain exceeds the observable one.
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

**Residuals [O].** The extra scalar's contribution to the radiation budget; the Proca tower's phenomenology if ordinary charges have fiber structure; the $O(\alpha T)$ impedance variation inside matter, a small computable correction to field strengths.

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

**The specification any successor must meet.** Conditions (i)–(iii) of §0.5, *and* dielectric rather than charge coupling. A 2-dimensional fiber meeting the 3-sphere in more than one point wants a 5-dimensional spatial total space; that is the honest generalization of the line-meets-$S^3$-twice picture, not a substitute for it.

---

## 14 · Differences from the neighbors

**Versus the monopole formulation.** Same arena, gravity sector, postulate, dial; the sole change is charge $\to$ dielectric, matter source $\to$ winding. Endpoints $\to$ none; basins $\to$ funnels; fog $\to$ localized masses; orbitability inverted from "only trace-free" to "everything."

**Versus straight 5D GR.** Exact agreement iff matter is fiber-smeared; the flat-along-the-ray response of a localized source is the isolated new physics.

**Versus Kaluza–Klein.** Reduction along a homothety-turned-winding rather than an isometry; graviphoton dead by theorem; the fiber field axion-like with a matter-dependent kinetic function — k-essence/disformal-adjacent, second order, ghost-free at $\varepsilon>0$ **[S]**.

**Versus screening theories.** Those suppress a scalar's sourcing; this abolishes sourcing and keeps refraction — closer to metamaterial optics than to modified gravity.

**Versus particle dark matter.** No new species; the dark component is the quotient image of the luminous one, with distribution and ratio fixed by the topology (§12).

---

## 15 · The radiation-blindness ledger

Six appearances of one selection rule: radiation cannot source the old $f$; needs no fiber stress ($p_u = \tfrac12 T = 0$); was the unique capture-free matter of the monopole era; hence alone localized there; is the unique transparent matter of the dielectric era ($\varepsilon = 1$); and is the natural inhabitant of the total space, which is what lets light see the image region as empty (§12). One asterisk: through $\rho - p$ radiation does source the dilaton under $p_u = p$.

---

## 16 · Open problems

1. **The $f\leftrightarrow\psi$ dictionary** — *closed* for fiber-smeared matter by the winding solution ($|\nabla f| = w/\psi$, §7.5); open for fiber-localized matter, where refraction and the Bianchi condition on $\varepsilon(T)$ interact.
2. **The uplift** — the winding-stabilized vacuum is AdS with $|\Lambda_4|\sim m_\psi^2$; the observed small positive $\Lambda$ requires an uplift of that size (§7.5). Dilaton *stabilization itself* is done.
3. **Light on $M_5$** — *done* (§12.5): ordinary Maxwell survives on the double cover in the dilaton medium, unrefracted; the dark image is lensed and dark. Residuals: the extra scalar $A_u$ in the radiation budget; the Proca tower if charges are fiber-localized.
4. **The dark-matter distribution** — halo-like images require near-$\Gamma$-symmetric luminous matter; determine whether the dielectric dilution plus the dynamical sector can produce it (§12).
5. **The susceptibility channel** — its strength and sign versus observation.
6. **The insulator frontier** — solutions with $\varepsilon\to0$ surfaces and their base images.
7. **The winding sector's dynamics** — can the winding number change?
8. **Inherited** — the $S^4$ pole question, the tensor-sector projection weight, the lapse-sector correspondence.

---

## 17 · Glossary

**Winding** — the period $\oint df = \ln\lambda$ that creates the fibration topologically. · **Permittivity $\varepsilon(T)$** — matter's refractive coupling to the fiber field. · **Paramagnet / blind / diamagnet / insulator** — dust / radiation / stiff / critical-stiff. · **Funnel** — the bunched fiber tube through a paramagnetic mass; concentration $\le n$. · **Terminus theorem** — the monopole-era no-go, now historical. · **The dial** — zero-mode share vs fiber smearing. · **Projective postulate** — base gravity reads the fiber average; the load-bearing nonlocality. · **The seed** — matter at one point of a fiber, gravity at all of them. · **Projection image** — the gravitational-only copy of a mass at its quotient-mates; the dark-matter candidate. · **Mach lock** — $GM_{\rm tot}/c^2\ell = \pi/2$. · **$p_u$** — conserved, quantized fiber momentum.

## 18 · Reference card

| topic | statement |
|:--|:--|
| **Mellin** | $\Delta_4[r^s\Phi] = r^{s-2}[\Delta_{S^3}+s(s+2)]\Phi$; weight $\int\rho\,r\,dr$ |
| **cone** | $\mathrm{Ric}_{ij} = \mathrm{Ric}(h)_{ij} - [aa''+(n-1)a'^2]h_{ij}$; vacuum $\iff\mathrm{Ric}(h) = 2h$; $\Lambda = 1/\ell^2$ |
| **fiber law** | $\nabla\cdot(\varepsilon\nabla f) = 0$, $\varepsilon = 1-\alpha T$, $\oint df = \ln\lambda$; no endpoints; $A_\mu\equiv0$ |
| **funneling** | $b = 2\varepsilon R/(1+\varepsilon)$; concentration $n\varepsilon/(\varepsilon+n-1)\le n$ |
| **Law I ($G$-free)** | $\ell^2R_{\mu\nu} = \ell^2\psi^{-1}\nabla\nabla\psi + 2(\tau - \tfrac13\tau g)$; $\ell^2\Box\psi = -\tfrac43\psi(\tau_u - \tfrac12\tau)$; stabilized: $+\tfrac{\hat\alpha}{2}\ell^2\nabla\nabla\tau$ on the left |
| **Law I (conventional)** | $R_{\mu\nu} = \psi^{-1}\nabla\nabla\psi + 8\pi(S - \tfrac13 Sg)$; $\Box\psi = -\tfrac{16\pi}{3}\psi(p_u - \tfrac12 S)$ |
| **geodesics** | $a^\mu = (p_u^2/\psi^3)\nabla^\mu\psi$; $m_{\rm eff} = \sqrt{1+p_u^2/\psi^2}$ |
| **GR dial** | zero-mode share $0.18/0.53/0.95/1.00$ at $w/L = 0.05/0.15/0.3/0.5$ |
| **twin theorem** | $u = \Phi\sin\chi$: $u''+4u = 0$; same-sign poles; $\ker(\Delta+3)$ = dipoles |
| **Mach lock** | $GM_{\rm tot}/c^2\ell = \pi/2$; $\bar\rho = c^2/4\pi G\ell^2$; $\Lambda\ell^2 = 1$ |
| **$k$-dial** | $v^2/c^2 = k(\pi-2\chi+\sin2\chi)/2\sin2\chi$; $v^2_{\rm eq} = kc^2$ |
| **$G$ theorem** | $G = \pi c^2\ell/2M_{\rm tot} = \pi\ell v^2_{\rm eq}/2M_{\rm lumps}$ |
| **charged node** | $\phi_e\propto\cot\chi$; RN near-zone; opposite-sign partner |
| **stabilization** | $\psi_0^2 = 3\varepsilon w^2/4\lvert\Lambda_5\rvert$; $m_\psi\psi_0 = w\sqrt\varepsilon$; $\Lambda_4 = \tfrac23\Lambda_5$; Yukawa $\alpha = \tfrac13$, range $\psi_0$ |
| **fiber escape** | $\sigma = -\partial_r(r^3E_r)$ on $S^3$; winding evades the balance theorem |
| **electrodynamics** | $\nabla_\mu(\psi\mathcal{F}^{\mu\nu}) = \psi\mathcal{J}^\nu - \partial_u(\psi^{-1}\mathcal{F}_u{}^\nu)$; $\epsilon\mu = 1$; Proca tower $2\pi n/C$; light on the cover, gravity on the quotient |
| **dark matter** | image of luminous matter under $S^3\to S^3/\Gamma$; ratio $|\Gamma|-1$ if co-located |
| **legacy** | basin $\theta = 1.644(m/M)^{1/3}$, contrast $\approx1$; pinch anisotropy $3$ |

*Numerics: softened potentials and 2D slices for the [M] items; coefficients are estimates at that fidelity. The concentration bound, the cone theorem, the reduction, the twin theorem, the Mach lock, and the endpoint-freeness are exact.*
