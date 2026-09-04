*Here's a note from Ajax:* Ok hello! So what this document is is a snippet of some of my active reasoning dynamical ideas I'm trying to string together. Specifically how it was made was that on August 31, 2026 and the week leading up to it I inputted about a dozen different intuitive constraints into Claude that I had been building up to throughout 2026. Note that in my journal entries I have the records of all of these intuitions as I first stated them months ago through more recently, plus the actual prompts to Claude itself in which I reveal them. A couple of examples are that I was really stuck two months ago with trying to imagine in my 3-sphere model a kind of "shaft" of matter to get at the kind of antipodal-pair dynamics I was looking for, however in quick succession over a couple of days in early August I had the thought that I could instead just use equivalence classes over lines in R4 space, then use the EFEs as a constraint ON THOSE LINES IN THE DEEPER SPACE, and then simply have the base space to it as a kind of RP3 over which orbits actually occur gravitationally. So yeah, basically the process was me having hidden biases in my reasoning together with a clear win condition, and then me gradually figuring out how to shed the biases to bring out the highlights in the win condition. And, well, that brings us to right now---only after I had all these constraints, (like for example I had intuited already that the fibers "bunch up" around mass so as to keep the primary object in the idealized model as defining the "radial direction" for the fibers while at once not actually contributing to the gravity dynamics directly accordingly, so it was meant to be a kind of trade-off between the primary and secondary following the same law while the secondary itself feels the effects of it only and then within those effects actual EFE stuff getting their scope---so yeah to be clear I entirely established the intricate graph-structure of constraints and then fed THAT into the AI, since I can make those graphs due to the months of bias-shedding, while it can simply implement them rather than create them), did I feed them as prompts into Claude, and ecstatically I got to watch it render them into real equations by deducing from what I had set up as well as formalizing some of my looser intuitions (like "bunching" became "dielectric" after my guess to the AI that it might be Poisson's equation was wrong). But yeah, I have all the records of everything in case there's ever a question, but to be clear I'm a guy who designed a very specific painting in my head without owning the paint to actually draw it in equations. Claude provided that paint, and indeed corrected some of my formalism guesses of the constraints, but the painting existed well before Claude painted it. (And indeed I still have a bunch of biases as we speak in things that didn’t yet make it into this brief doc here, as even in the last couple of days I shifted associating one thing with the total space to associating it with the base space, which gives me another angle on inductively landing the next unification of two concepts in the sequence. So in other words it’s still an ongoing process, so much of what will show up in the next draft is something I already have intuited right now, but just haven’t rendered and posted yet).

# Projective Gravity — A Program Brief

### The whole effort, situated: what stands, what is unfinished, and where it sits

> **How to read this.** This is a *brief*, not the field guide: it states results and their standing, and points to the guide for derivations. It is split in two on purpose. **Part I** contains only what has been verified, derived, or established by cited theorem, and it records what was *retired* and why. **Part II** contains the speculative material — not to discount it, but to mark it accurately as unfinished: it carries the same kind of category-error noise that the Part I material carried before it was cleared, and the point of the split is to make that noise visible rather than to hide it. **Part III** situates the program against the landscape.
>
> **Tags.** **[V]** verified symbolically or numerically in this program · **[M]** measured in a numerical experiment · **[T]** established theorem, cited · **[D]** derived here · **[S]** sketch · **[O]** open · **[R]** retired, with the reason.

---

# PART I — WHAT STANDS

## I.1 The founding move

Gravity lives on the **space of fibers** of a foliation; matter inhabits the **total space**; gravity reads only the fiber-averaged projection of matter. That single postulate — *base gravity reads* $S_{\mu\nu} = \oint T_{\mu\nu}\,du$ — is the theory's entire departure from general relativity. Everything else was either derived from it plus a choice of arena, or removed.

## I.2 The arena, and why it is rigid

The total space is $M_5 = \mathbb{R}_t\times S^1_u\times S^3$, the Hopf compactification of $\mathbb{R}^4\setminus\{0\}$ in polar form: $ds^2 = e^{2u}[du^2 + d\Omega_3^2]$ with $u = \ln r$, so the **radial direction is $\partial_u$**, globally defined and nowhere zero because the manifold is a product **[T]**. The fibration therefore exists for the same reason the cylinder is a cylinder; it does not need to be sourced, and it is not.

Two theorems fix this arena. Poincaré–Hopf forbids the naive "fibers radiating from a point of $S^4$": $\chi(S^4) = 2$, so any such fibration has two singular poles; $\chi(S^1\times S^3) = 0$ admits the nowhere-vanishing closed one-form the winding requires **[T]**. And the Einstein-static lock — the closure relation that gives the program its constants — requires positive spatial curvature: a flat $T^3$ has no static matter-filled solution, so $T^4$ would lose the Mach lock and the twin theorem both **[V]**.

The fiber field is a compact scalar $f$ with winding $\oint df = \ln\lambda$ and law $\Box f = 0$; the solution is $f = wu$ exactly, for any base metric and any dilaton profile **[V]**. The fibration is rigid: matter does not bend it.

## I.3 The seed, exactly

The scaling group of $\mathbb{R}^4\setminus\{0\}$ is $\mathbb{R}^* = \mathbb{R}^+\times\mathbb{Z}_2$, so a punctured line through the origin is **two rays**, $(r,\hat n)$ and $(r,-\hat n)$, and the base is $\mathbb{RP}^3$. The fiber over $[\hat n]$ is therefore **disconnected** — the $u$-circle at $+\hat n$ and the one at $-\hat n$ — and the projective postulate integrates over both **[D]**.

> **The seed.** A star at $(u_0,+\hat n)$ sources the base at $[\hat n]$, whose lift to $S^3$ has gravitational wells at **both** $\pm\hat n$. Travel to $-\hat n$: nothing is there to emit, absorb, or reflect. The star speaks gravitationally for every point of its fiber and materially for one.

It is **blindness, not crossing** **[T]**: the antipodal link is the discrete $\mathbb{Z}_2$ factor, not a path. Moving along the fiber wraps the $u$-circle and returns at the same $\hat n$; the origin, where a line would cross, was removed precisely because every line meets there. That is what keeps the antipode materially empty. And the two localizations are independent: $\mathbb{Z}_2$-position controls the seed (matter in one component), $u$-position controls the photon tower and the GR dial (matter smeared) — so ordinary matter can be $u$-smeared and $\mathbb{Z}_2$-localized at once **[D]**.

## I.4 The laws

> ### ◆ LAW I — GRAVITY (budget-normalized, $G$-free form)
> With $\ell = (V/2\pi^2)^{1/3}$, $\bar\epsilon = \mathcal{E}/V$, and $\tau = S/\bar\epsilon$:
> $$\ell^2 R^{(4)}_{\mu\nu} = \ell^2\psi^{-1}\nabla_\mu\nabla_\nu\psi + 2\Big(\tau_{\mu\nu} - \tfrac13\tau g_{\mu\nu}\Big), \qquad \ell^2\Box\psi = -\tfrac43\psi\Big(\tau_u - \tfrac12\tau\Big)$$
> Couplings $2$ and $\tfrac43$, pure numbers, fixed by the Mach lock on the static background **[V]**. Conventional form: $R_{\mu\nu} = \psi^{-1}\nabla\nabla\psi + 8\pi(S - \tfrac13 Sg)$, the reduction of 5D Einstein; the $\tfrac13$ is the five-dimensional trace-reversal. Fully dynamical — nothing in the derivation assumes staticity.

> ### ◆ LAW II — THE FIBRATION
> $$\Box f = 0, \qquad \oint df = \ln\lambda, \qquad f = wu$$
> Unsourced, rigid, topological **[V]**.

> ### ◆ ELECTROMAGNETISM (adopted)
> $\mathcal{F}$ lives on $M_5$ — the double cover — with 5D current on charged matter. Reduction **[V]**:
> $$\nabla_\mu\big(\psi\mathcal{F}^{\mu\nu}\big) = \psi\mathcal{J}^\nu - \partial_u\big(\psi^{-1}\mathcal{F}_u{}^{\nu}\big)$$
> Maxwell in a medium with $\epsilon = 1/\mu = \psi$, so $\epsilon\mu = 1$: light rides the null geodesics of $g^{(4)}$ unrefracted. Fiber modes form a Proca tower $m_n = 2\pi n/C$, unexcited by $u$-smeared matter. Light lives on the cover, gravity on the quotient — so the seed's optics (lensed at the image, not emitted there) are a *consequence*, not an assumption **[D]**.

## I.5 The theorems

**T1 — Terminus theorem [M/D].** Under charge coupling $\Box f = \kappa T$, every trace-full object is a flow endpoint; basins scale as $\theta = 1.644(m/M)^{1/3}$ (the Hill scaling), so mass and volume fractions coincide and the density contrast is $\approx1$: *a point mass smears itself to background density.* Sourcing the fibration and being orbitable are mutually exclusive. General lesson: whether a field is sourced or unsourced decides whether localized structure can exist in it.

**T2 — Cone theorem [V].** For $g = dr^2 + a(r)^2h$, $\mathrm{Ric}_{ij} = \mathrm{Ric}(h)_{ij} - [aa'' + (n-1)a'^2]h_{ij}$; on the cone $a = r$, vacuum upstairs $\iff$ $\mathrm{Ric}(h) = 2h$: the base is the unit $S^3/\Gamma$ and $\Lambda = 1/\ell^2$ is generated by fiber spreading.

**T3 — Twin theorem [V].** The static perturbation operator on the closed background is $\Delta_{S^3}+3$ (derived from the linearized Einstein tensor). Substituting $u = \Phi\sin\chi$ gives $u'' + 4u = 0$, so $\Phi = (A\cos2\chi + B\sin2\chi)/\sin\chi$; the mass-carrying solution has **same-sign poles at both ends** (flux $-4\pi$ at each). A static point mass cannot be alone; for two bodies the antipodal equal-mass pair is unique. Integral form: $\ker(\Delta+3)$ is the dipoles, so static sources need zero dipole — and the $\mathbb{RP}^3$ quotient satisfies this identically. *The projection is the twin mechanism.* Charge obeys plain $\Delta$ instead, with opposite-sign poles: mass gets a same-sign twin, charge a $\pm Q$ pair.

**T4 — Mach lock [V], honestly stated.** The static closure relation gives $\bar\rho = c^2/4\pi G\ell^2$, $\Lambda = 1/\ell^2$, hence
$$\frac{GM_{\rm tot}}{c^2\ell} = \frac{\pi}{2}$$
Sciama's order-unity Machian relation with its coefficient supplied. **It is a consistency relation on static solutions, not a derivation of $G$**: in the reduced theory $G_4 = G_5/C$ with both factors constants, so $G$ enters as an input. Earlier editions overclaimed this; the record now says so. What survives: $G$ is not independently specifiable in a closed static universe, and the coefficient is exact. Dynamical extension by $\ell(t)$ is excluded ($\dot G/G = H$, $700\times$ over the lunar-ranging bound), so $G$ stays constant and the $G$-free form is a static rewriting.

**T5 — The $k$-dial [V, dynamically confirmed to $10^{-13}$].** With the lump sector carrying fraction $k$ of the budget at antipodal nodes,
$$\frac{v^2(\chi)}{c^2} = k\,\frac{\pi - 2\chi + \sin2\chi}{2\sin2\chi}$$
Kepler near a node, $v^2_{\rm eq}/c^2 = k$ exactly at the equator — the budget meter — light speed at parity. The lone-mass Kepler continuation gives $\tfrac12$ there; the factor 2 is the antipode speaking. Stereographically the potential is self-dual under $r\to1/r$: any node can be chart-infinity, "primary" is a frame label **[V]**.

**T6 — Dilaton stabilization by the winding [V].** In vacuum the dilaton is Brans–Dicke $\omega = 0$: massless, fifth force $\alpha = \tfrac13$, and PPN $\gamma = (1+\omega)/(2+\omega) = \tfrac12$ against Cassini's $1\pm2\times10^{-5}$ — **an unstabilized theory is dead on arrival** **[T]**. The winding energy $\tfrac12(\nabla f)^2 = w^2/2\psi^2$ reduces to Brans–Dicke with a potential; in the Einstein frame a minimum exists iff $\Lambda_5 < 0$, and
$$\psi_0^2 = \frac{3w^2}{4|\Lambda_5|}, \qquad m_\psi^2 = \tfrac43|\Lambda_5| = \frac{w^2}{\psi_0^2}, \qquad m_\psi\psi_0 = w$$
The fiber size is set by an integer; the modulus Compton wavelength equals the fiber size (the same $m\lambda\to1$ law the celestial detour found independently); the fifth force becomes a Yukawa of range $\psi_0$, bounded at tens of microns; and $\gamma = 1$ is restored exactly — suppression $e^{-3\times10^{15}}$ at 1 AU **[D]**. **This is the result that lets the theory survive the solar system.** Price: $\Lambda_4 = \tfrac23\Lambda_5 = -\tfrac12 m_\psi^2 < 0$, AdS, off the observed value by $10^{60}$ — the cosmological-constant problem in Kaluza–Klein dress, and an *internal* tension with the $\Lambda>0$ static arena of T4.

**T7 — Consistency [V/D].** Integrating 5D conservation over the closed fiber gives $\nabla_\mu S^{\mu\nu} = -(\nabla_\mu\psi/\psi)S^{\mu\nu} + \psi\nabla^\nu\psi\,S^{uu}$ — the exchange term, $O(10^{-32})$ when stabilized. The averaged source is antipodally symmetric and descends to $\mathbb{RP}^3$ conserved. Seen from the quotient the theory is **GR on $\mathbb{R}_t\times\mathbb{RP}^3$ in which every matter field carries a $\mathbb{Z}_2$ sheet label — gravity blind to the label, Maxwell diagonal in it**: local, causal, ordinary.

**T8 — The price [D].** On the cover, wiggling a lump at $+\hat n$ changes the field at $-\hat n$ instantly (one point of the quotient) while light takes $\pi\ell/c$. A **two-speed cover**. Non-paradoxical — the static universe supplies a preferred frame — and unobservable beyond the horizon, but a genuine departure from GR and the true cost of the postulate.

**T9 — Charged node [V].** On the closed background Maxwell's total-charge-zero forces a $-Q$ somewhere; with it at the symmetric antipode, $\phi_e = (Q/4\pi\epsilon_0\ell)\cot\chi$ and the potential's near zone is **Reissner–Nordström, deduced**, the field's own energy gravitating with the universal $G$. Budget form: both terms are budget fractions, $M/M_{\rm tot}$ and $(Q/Q_{\rm ext})^2$ with $Q_{\rm ext} = M_{\rm tot}\sqrt{4\pi\epsilon_0 G}$.

## I.6 The two galaxy-scale results

**Rotation curves on the closed sphere [V].** For an exponential source and its projective twin, the circular-orbit law $v^2 = \Phi'\tan\chi$ gives curves that **always flatten** to the same equatorial value,
$$v^2_{\rm eq} = 4\pi G\bar\rho = \frac{4GM}{\pi\ell}$$
— the closure-compensating mean density, i.e. Gauss's theorem on the compact space, not a halo. The source scale $\chi_0/\ell$ dials the shape: concentrated sources give a Keplerian peak at $0.22$ of the equator and a decline to the plateau (massive spirals); extended ones give a slow monotonic rise (dwarfs, LSBs). One parameter, the observed diversity of shapes. *Scale caveat:* with the Milky Way's luminous mass a 220 km/s plateau needs $\ell\approx7$ kpc — the equator at 11 kpc, far too early, and rising beyond it. Shape yes, scale no, without dark mass.

**Tully–Fisher from closure and two-dimensionality [D/V].** Three ingredients: the plateau $v^2 = 4GM/\pi\ell$; the galaxy filling a hemisphere, $\ell = 2R/\pi$; and disks being 2-D at surface density $\Sigma$, $M = \pi\Sigma R^2$. Then $v^2 = 4\pi G\Sigma R$ with $R\propto\sqrt M$, so
$$v_{\rm flat}^4 = G\,M\,a_0, \qquad a_0 = 4\pi G\,\Sigma_{\rm mean}$$
**The baryonic Tully–Fisher relation, MOND's deep-regime law, with the square root forced by dimension counting** — $M\sim R^2$ from two-dimensionality, $v^2\sim M/R$ from closure. The number: $a_0 = 1.2\times10^{-10}$ m/s² needs $\Sigma_{\rm mean} = 69\,M_\odot/{\rm pc}^2$, which *is* a Freeman disk's mean surface density. This reproduces Milgrom's own unexplained numerology $a_0\approx2\pi G\Sigma_0$ with a mechanism: the acceleration scale is the closure mean density, and for a disk filling a hemisphere that is the disk's surface density in disguise. *The problem:* the model predicts $v^4 = 4\pi G\Sigma M$ — TF *with a surface-density factor* — so a population with 0.35 dex $\Sigma$-scatter has TF residuals tracking $\log\Sigma$ at $r = 1.000$, and LSB galaxies fall below the line. Observation: BTFR is tight (~0.1 dex) and LSBs sit on it. The fix wanted is a law making the *actual* $\ell\propto\sqrt M$ universally (Part II.3).

## I.7 The one prediction, and its status

Extended naively to an expanding universe with an independent antipode, the postulate sources local gravity from matter at *both* $\pm\hat n$; the antipodal sheet is an independent realization (sheet correlation from the $(-1)^\ell$ parity of $S^3$ harmonics is $<10^{-2}$ for any power at $\ell\gtrsim10$ **[V]**). Galaxies trace $\delta_{\rm local}$; lensing traces the sum. The bias-free statistic
$$r^2 = \frac{\langle g\kappa\rangle^2}{\langle gg\rangle\langle\kappa\kappa\rangle}$$
is predicted at $r = 1/\sqrt2 = 0.707$ (Monte Carlo $0.7068$): **half the lensing power from structures with no optical counterpart, uncorrelated with galaxies.** Current status: most 3×2pt analyses *assume* $r = 1$; where it floats, it is consistent with 1 at the 10–20% level, so $0.71$ is disfavored at a couple of sigma — **in tension, not excluded**. Every escape (antipodally symmetric initial conditions; a time-shifted quotient) switches the seed off. This is a drafting-phase signpost: the observable the idea must eventually face, recorded, not a verdict.

## I.8 What was retired, and why

| idea | status | reason |
|:--|:--|:--|
| Monopole coupling $\Box f = \kappa T$ | **[R]** | terminus theorem: capture, fog, no orbits |
| Celestial (twistor) formulation | **[R]** | fibers are directions at a point; condition (iii) of the seed — each fiber meeting 3-space at more than one point — fails structurally. Its best result, "the projective postulate dissolves into geometry," was the seed's death certificate. Delivered the flux-stabilization lesson. |
| Dielectric coupling $\varepsilon = 1-\alpha T$ | **[R]** | $\alpha_{\rm fine}\propto1/\psi$ and $\psi_0\propto\sqrt\varepsilon$ make the fine-structure constant density-dependent; its constancy bounds $\varepsilon-1 < 2\times10^{-5}$, and the primary would need a sub-Planckian fiber extent to orient the fibers. Removed; $\alpha_{\rm fine}$ now constant to $10^{-32}$. |
| Dark matter as projection image | **[R]** | topology fork (small domain $\Rightarrow$ matched circles, excluded by Planck; large domain $\Rightarrow$ images uncorrelated with local galaxies) and the acoustic peaks (an image of oscillating baryons oscillates) |
| "Emergent $G$" as a derivation | **[R]** | $G_4 = G_5/C$; the Mach lock is a consistency relation (T4) |
| $\lambda = a$ (no-flux Kähler point) | **[R]** | massless modulus; superseded by flux/winding stabilization |
| CMB dipole $=$ solar orbit direction | **[R]** | dipole apex $(264°,+48°)$, solar orbit toward $(90°,0°)$: $131°$ apart |

## I.9 The recurring themes

**Radiation blindness** (eight appearances): radiation cannot source $f$, needs no fiber stress, was the unique capture-free matter, was transparent to the retired coupling, lives naturally on the cover, and is the reason the electromagnetic postulate costs nothing. **Eigenvalue quantization**: $\Lambda$ from closure, $\psi_0$ from the winding integer — both looked like inputs. **Pay for the stage**: $\Lambda$ from spreading, $\pm\lambda^2/a^4$ from twisting, $\Lambda_4 = \tfrac23\Lambda_5$ from stabilizing; nothing geometric is free. **Frame democracy**: the Kelvin self-duality, any node as chart-infinity. **The structure gets the constraint**: the antipodal twin, the seed's optics, the TF square root — each arrived by a route other than the one guessed for it.

---

# PART II — THE FUZZ

> **What this part is.** Everything below is unfinished. Some of it is a vision with measured walls; some is a methodology with proven structure waiting for a definition; some is a thread. None of it is defended. It is recorded here in the same spirit as Part I's retired table: the defendable core was made from material exactly like this, cleared one category error at a time, and the only way to clear the next one is to have it written down.

## II.1 The reflection sky

**The vision.** The 3-sphere is galaxy-sized; our galaxy fills one hemisphere; the other holds its gravitational twin and no light. The "other galaxies" are our own galaxy's light, wrapped around the sphere and scrambled by structure in the dark hemisphere — a sky of optical images, not separate objects.

**Three walls, with heights [V].**
1. *Lensing strength.* Scrambling a sky into distinct images needs deflections $\sim1$ rad. A galaxy-mass twin at impact parameter $\sim\ell$ deflects by $4GM/c^2b\approx10^{-6}$ rad; order-unity deflection needs $b\sim4GM/c^2$, the twin's Schwarzschild radius. Gravity is $10^6$ too weak.
2. *The cavity.* Every ray returns to its source after $2\pi\ell/c$ (0.2 Myr at 10 kpc); the Sun's whole luminosity refocuses onto a waist $\sim R_\odot$, delivering the Sun's *surface* flux, $6\times10^7$ W/m², from every direction. Escape needs scattering (too weak, wall 1) or absorption (which kills the returns).
3. *The redshift theorem.* In any static metric the Killing energy is conserved along null rays, so light that leaves us and returns to us has exactly its emitted frequency. A static antipodal well cannot make Hubble's law.

The walls interlock: strong scattering without absorption, in a non-static geometry, from a galaxy-mass object. No standard physics supplies it. Behind the geometric walls stand three that no geometry touches: primordial helium (the Sun is 25% He; stars cannot have made it), the acoustic peaks (sound in a photon–baryon fluid, not scrambled starlight), and spectral diversity (reflections of one galaxy have one spectrum). **[S]** throughout.

## II.2 Hubble's law without expansion

The idea: cosmological redshift as light climbing out of a static well at the antipodal "infinity point." The theorem forbids it (II.1, wall 3), and the program's author knows this and proposes perturbing *definitions* rather than geometry. The honest map of the doors: non-staticity is expansion (the standard answer); a non-geometric frequency shift would need light not to follow null geodesics of the metric it gravitates in (the two-speed cover does not help — light's own metric is static); a many-circuit slowly-expanding small universe accumulates $z$ but is blocked by the cavity. **[S]**

## II.3 The apparent-scale parameter

Aimed at the one problem in I.6: the model's Tully–Fisher carries a $\Sigma$-factor that data forbid. The proposal: the *actual* $\ell$ tracks $\sqrt M$ universally, and observed surface-density scatter (Freeman scatter, LSB versus HSB) is an *apparent* factor from the reference-point setup — a physically $2\times$ galaxy at $0.5\times$ apparent scale registers the same. Then TF is exact and $\Sigma$-scatter is optical. **What it needs:** a law for $\ell_{\rm actual}$. The one law in hand, the Mach lock, gives $\ell\propto M_{\rm tot}$ — linear, which would make every galaxy's $v_{\rm flat}$ the same, wrong the other way. Either $M_{\rm tot}\propto\sqrt{M_{\rm gal}}$ for a reason not yet in the model, or the galaxy-scale universe is not static and $\ell$ is set by something else (angular momentum, formation history, a fiber quantum). Well-posed and open. **[S/O]**

## II.4 Reference point as root

The proposal: take the multi-throat Majumdar–Papapetrou metric with the "1" as a throat, use the optical metric as a local positioning scheme, study what fails to distinguish positions under throat-swapping, and put *that* invariance at the root of "position" rather than having it emerge. Moving between throats becomes going in a circle. **Proven structure this connects to:** the Kelvin self-duality — the two-node potential identical under $r\to1/r$, any node sendable to chart-infinity, "primary" a frame label (T5). The invariance exists as a property of solutions; the proposal is to promote it to a definition. Precedent: the move from "coordinates are labels" to "diffeomorphism invariance is the content." **[S]**

## II.5 Loosening distinctness

The proposal: two nearby spacetime points are one "actual" point whose direction space has been partitioned two ways — the celestial sphere quotiented differently — giving just enough illusion to register as two places. **Proven structure this connects to:** on the Einstein-static universe, $\{$rays through $p\} = \{$rays through $\bar p\}$ — two points sharing one celestial sphere in the space of null rays. **Obstacle:** in flat space two spacelike-separated points share no null rays, so the identification has nothing to grip. Where it grips is the fiber: two points on one fiber *do* share a base point — the projective postulate seen as an ontology rather than a source rule. The further hope that Feynman-diagram structure simplifies once spacetime is emergent in this sense is recorded as a hope. **[S]**

## II.6 The double path at the antipode

The proposal: photons as closed paths that go out and return; generalize the Born rule's $\cos(\Delta S)$ double-path structure to this picture; have nearby closed paths "not open" while paths enclosing the opposite mass point search many routes, generating Hubble's law. **Real geometric fact:** on the closed sphere the direct path and the around-the-back path both connect $p$ to $\bar p$ — a genuine two-path structure at the antipode. **Obstacle:** the static phases along those paths give no frequency shift (II.1, wall 3). The route to Hubble's law would need the two paths to differ in a way that is not a static phase — that is the definitional perturbation being sought, and it has not been found. **[S]**

## II.7 Smaller threads

The 3-sphere as genuinely spherical, with the disk we see as a projection and geodesics veering between spheres in the "up" direction; the circumgalactic medium as a soft boundary where the projection blends sources. Recorded; not developed. **[S]**

## II.8 Checked within the fuzz, and retired

The CMB dipole was proposed to coincide with the Sun's galactic orbit. Checked: the dipole apex is $(l,b) = (264°,+48°)$, the solar orbit is toward $(90°,0°)$; separation $131°$, nearly opposite. The real coincidence in the neighborhood is the dipole's rough alignment with the Local Group's infall toward Virgo and the Great Attractor — standard cosmology. **[R]**

## II.9 The blocking problem, and what it blocks

**The AdS uplift.** The stabilized vacuum has $\Lambda_4 = -\tfrac12m_\psi^2$, off the observed value by $10^{60}$; this framework has no special claim on solving it, and it is now an *internal* tension with the $\Lambda>0$ static arena. **What solving it would unlock:** the Machian ambition, inverted. Every link is a derived relation — $\psi_0$ from the winding, $C = \psi_0\ln\lambda$, $G_4 = G_5/C$, $\Lambda_4 = \tfrac23\Lambda_5$, $\ell = 1/\sqrt{\Lambda_4}$ — and the Mach lock then returns
$$M_{\rm tot} = \frac{3\sqrt2\,\pi c^2\ln\lambda\,w}{8\,G_5\Lambda_5}$$
with every symbol a theory parameter. Not "the universe fixes $G$" but "**the theory fixes the universe**": it would predict the total mass. The stronger claim of the two, because it can be wrong. Unreachable until the uplift is solved. **[D, conditional]**

**Law III.** A second source-free 2-form on $M_5$ with base charges as fiber-flux escape — Wheeler's charge-without-charge. The fiber-escape identity $\sigma = -\partial_r(r^3E_r)$ is geometry the celestial version could not supply; net charge needs a multivalued potential, and $f$ is multivalued by construction. Candidate slot. **[S]**

---

# PART III — SITUATING

## III.1 What the program is, in one paragraph

A Kaluza–Klein model on a closed static universe — $\mathbb{R}_t\times S^1_u\times S^3$ with a topologically rigid fibration, a winding-stabilized massive radion, and electromagnetism on the double cover — carrying **one postulate** that general relativity lacks: gravity reads the fiber-averaged source, which on the quotient $\mathbb{RP}^3$ means gravity is blind to a $\mathbb{Z}_2$ sheet label that Maxwell respects. It is internally consistent, passes the solar system by virtue of its own stabilization mechanism, reproduces the closed-universe results of general relativity with exact coefficients, and derives the Tully–Fisher square root from dimension counting with an acceleration scale that lands on a Freeman surface density. Its distinctive postulate has one cosmological signature, a bias-free lensing–clustering coherence of $1/\sqrt2$, currently in mild tension with data. Its blocking problem is the cosmological constant.

## III.2 What is genuinely new, and what is reproduced

*Reproduced, correctly, with the machinery visible:* the Einstein-static lock and its Machian relation (Einstein 1917, Sciama 1953), Kaluza–Klein reduction with a radion, O'Neill's formulas, the Brans–Dicke $\gamma$, Freund–Rubin-type stabilization, Wheeler's charge-without-charge, the twin theorem's operator (standard perturbation theory on the ESU). These are load-bearing and they are not new.

*Candidate-new, pending a literature review that has not been done:* the terminus theorem as a stated design principle; the seed as a topological consequence of the disconnected fiber; the fiber-averaged source as a postulate and its quotient reading as sheet-label blindness; the $r = 1/\sqrt2$ signature; the rotation-curve family from closure; and — the best of them — **Tully–Fisher's square root from closure plus two-dimensionality, with $a_0 = 4\pi G\Sigma_{\rm mean}$** explaining a numerology that has sat unexplained in the MOND literature.

*Not claimed:* novelty of any of the above, until the review is done.

## III.3 The stage-one / stage-two criterion

The program's own test for a patch worth keeping: *does it subtract assumptions and make more click into place than you started with?* Applied to the record —

- **Passed:** the dielectric-to-unsourced move (subtracted a coupling, kept every theorem, made $\alpha_{\rm fine}$ exactly constant); the winding stabilization (one existing structure fixed the fifth force, the PPN disaster, and the varying-$\alpha$ signal at once); the seed-as-topology reading (subtracted the need for any dynamical response).
- **Failed, and retired:** the celestial detour (added structure, lost the seed); dark matter as image (added no assumption but met two independent walls).
- **Pending:** the apparent-scale parameter (adds a parameter; would remove a $\Sigma$-factor; needs a law); Law III (adds a field; would explain charge; needs a loophole to be exercised).

By its own criterion the program is at stage one, with two results — stabilization and Tully–Fisher — that are the kind of thing stage two is made of.

## III.4 The next three moves

1. **A law for $\ell$.** The Tully–Fisher result is one missing relation away from being a prediction rather than a coincidence. What sets a galaxy's closed-universe radius? Non-static dynamics, angular momentum, or a fiber quantum are the candidates. This is the highest-value open computation.
2. **A dedicated $r$ measurement.** The program's one cosmological signature is a specific bias-free number that existing surveys could measure rather than assume. Knowing whether $r$ is 1 or $0.71$ on large scales would settle the postulate's status as physics of our universe.
3. **The literature review.** Before any of Part I is described as new.

---

## Reference card

| result | statement | tag |
|:--|:--|:--|
| arena | $\mathbb{R}_t\times S^1_u\times S^3$; $\partial_u$ = radial direction; $\chi = 0$ | [T] |
| seed | fiber over $[\hat n]$ = two rays $\pm\hat n$; blindness, not crossing | [D] |
| Law I | $\ell^2R_{\mu\nu} = \ell^2\psi^{-1}\nabla\nabla\psi + 2(\tau - \tfrac13\tau g)$ | [V] |
| Law II | $\Box f = 0$, $\oint df = \ln\lambda$, $f = wu$ | [V] |
| Maxwell | $\nabla_\mu(\psi\mathcal{F}^{\mu\nu}) = \psi\mathcal{J}^\nu - \partial_u(\psi^{-1}\mathcal{F}_u{}^\nu)$; $\epsilon\mu = 1$ | [V] |
| twin | $u = \Phi\sin\chi \Rightarrow u''+4u = 0$; same-sign poles | [V] |
| Mach lock | $GM_{\rm tot}/c^2\ell = \pi/2$ (consistency relation) | [V] |
| $k$-dial | $v^2/c^2 = k(\pi-2\chi+\sin2\chi)/2\sin2\chi$ | [V] |
| stabilization | $\psi_0^2 = 3w^2/4\lvert\Lambda_5\rvert$; $m_\psi\psi_0 = w$; $\gamma = 1$ | [V/D] |
| plateau | $v^2_{\rm eq} = 4\pi G\bar\rho = 4GM/\pi\ell$ | [V] |
| Tully–Fisher | $v^4 = GMa_0$, $a_0 = 4\pi G\Sigma_{\rm mean}$, $\Sigma_{\rm mean} = 69\,M_\odot/{\rm pc}^2$ | [D/V] |
| signature | $r = 1/\sqrt2$, bias-free; mildly disfavored | [D] |
| price | two-speed cover; $\Lambda_4 = -\tfrac12 m_\psi^2$ | [D] |
| reflection sky | deflection $10^{-6}$ vs 1 rad; cavity $6\times10^7$ W/m²; redshift ratio $= 1$ | [V] walls |
| inversion | $M_{\rm tot} = 3\sqrt2\pi c^2\ln\lambda\,w/8G_5\Lambda_5$, needs $\Lambda_4>0$ | [D, conditional] |
