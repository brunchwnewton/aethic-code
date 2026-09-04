# Projective Gravity — Version 3

### The Spin Structure: a field guide

> **What this version is.** Version 2 was the *minimal theory*: Kaluza–Klein on $\mathbb{R}_t\times S^1_u\times S^3$ with a rigid fibration, a winding-stabilized radion, electromagnetism on the double cover, and one postulate — gravity reads the fiber average. Version 3 keeps all of it unchanged, adds a **second-order fibration** built by Hopf-extending the concentric shells about every mass, and records a recognition that reorganizes the whole: **the first-order theory was already a spin structure.** The gravitational base is $SO(3)$; the cover on which light and matter live is $SU(2)$; the antipodal map is the spinor sign flip. The seed — matter at $\hat n$, gravity at both $\pm\hat n$ — is the statement that gravity lives on the rotation group and cannot see the sign of a spinor. The second-order structure repeats this pattern one level down and captures exactly the information the first-order projection discards.
>
> **Tags.** **[V]** verified symbolically or numerically · **[M]** measured numerically · **[T]** established theorem, cited · **[D]** derived here · **[S]** sketch · **[O]** open · **[R]** retired.
>
> **Conventions.** $G = c = 1$ unless restored; $\ell$ = radius of the spatial 3-sphere; $\hat n\in S^3$, $[\hat n]\in\mathbb{RP}^3$; $T_\pm(\hat n) \equiv T(\hat n)\pm T(-\hat n)$ the antipodally even and odd parts of any field on the cover.
>
> **Reading guide.** The spin identification: §I.5. Distinctness and the root, realized: §II.2b. The second-order construction: §II.3–§II.5. The selection rule: §II.4. The partition theorem: §II.6. What sources it: §II.7. The quantization fork: §II.9. Black holes: §II.10. Laws and axioms of version 3: §II.13. Status and open problems: Part III.

---

# PART I — THE FIRST-ORDER THEORY

## I.1 Arena

$M_5 = \mathbb{R}_t\times S^1_u\times S^3$, the Hopf compactification of $\mathbb{R}^4\setminus\{0\}$ in polar form. With $u = \ln r$, $ds^2 = e^{2u}[du^2 + d\Omega_3^2]$: the radial direction is $\partial_u$, globally defined and nowhere zero because the manifold is a product **[T]**. $\chi(S^1\times S^3) = 0$ permits the nowhere-vanishing closed one-form the winding requires; $\chi(S^4) = 2$ forbids the naive "fibers radiating from a point of $S^4$" **[T]**. The Einstein-static lock needs positive spatial curvature, so $T^4$ would lose both the Mach relation and the twin theorem **[V]**.

## I.2 The seed

The scaling group of $\mathbb{R}^4\setminus\{0\}$ is $\mathbb{R}^* = \mathbb{R}^+\times\mathbb{Z}_2$. A punctured line is two rays, $(r,\hat n)$ and $(r,-\hat n)$; the base is $\mathbb{RP}^3$; the fiber over $[\hat n]$ is **disconnected** — the $u$-circle at $+\hat n$ and the one at $-\hat n$ — and the projective postulate integrates over both **[D]**.

> A star at $(u_0,+\hat n)$ sources the base at $[\hat n]$, whose lift to $S^3$ has wells at **both** $\pm\hat n$. At $-\hat n$ there is nothing to emit, absorb, or reflect. **Blindness, not crossing:** the antipodal link is the discrete $\mathbb{Z}_2$ factor, not a path; the origin was removed precisely because every line meets there. That is what keeps the antipode materially empty.

The two localizations are independent: $\mathbb{Z}_2$-component controls the seed (matter in one component), $u$-position controls the photon tower and the GR dial (matter smeared) **[D]**.

## I.3 Laws

> ### ◆ LAW I — GRAVITY
> $$\ell^2 R^{(4)}_{\mu\nu} = \ell^2\psi^{-1}\nabla_\mu\nabla_\nu\psi + 2\Big(\tau_{\mu\nu} - \tfrac13\tau g_{\mu\nu}\Big), \qquad \ell^2\Box\psi = -\tfrac43\psi\Big(\tau_u - \tfrac12\tau\Big)$$
> with $\tau = S/\bar\epsilon$ and **$S_{\mu\nu} = \oint T_{\mu\nu}\,du$ over both fiber components** — i.e. $S = T_+$, the even part. Couplings $2$ and $\tfrac43$, pure numbers, fixed by the static lock **[V]**. Fully dynamical; the reduction of 5D Einstein with the five-dimensional $\tfrac13$.

> ### ◆ LAW II — THE FIBRATION
> $$\Box f = 0, \qquad \oint df = \ln\lambda, \qquad f = wu$$
> Unsourced, rigid, topological **[V]**.

> ### ◆ ELECTROMAGNETISM
> $\mathcal{F}$ on $M_5$, the double cover. Reduction **[V]**: $\nabla_\mu(\psi\mathcal{F}^{\mu\nu}) = \psi\mathcal{J}^\nu - \partial_u(\psi^{-1}\mathcal{F}_u{}^\nu)$ — Maxwell in a medium with $\epsilon = 1/\mu = \psi$, so $\epsilon\mu = 1$ and light rides the null geodesics of $g^{(4)}$ unrefracted. Light lives on the cover, gravity on the quotient: the seed's optics are a consequence **[D]**.

## I.4 Theorems carried forward

**Terminus theorem [M/D].** A sourced fibration makes every mass a flow endpoint and smears it to background density. Sourcing and orbitability are exclusive.

**Cone theorem [V].** On the cone $a = r$, vacuum upstairs $\iff$ $\mathrm{Ric}(h) = 2h$; $\Lambda = 1/\ell^2$ from fiber spreading.

**Twin theorem [V].** The static operator is $\Delta_{S^3}+3$; $u = \Phi\sin\chi$ gives $u''+4u = 0$; the mass-carrying solution has same-sign poles at both ends. $\ker(\Delta+3)$ = dipoles; the $\mathbb{RP}^3$ quotient satisfies zero-dipole identically. *The projection is the twin mechanism.* Charge obeys plain $\Delta$: opposite-sign poles.

**Mach relation [V].** $GM_{\rm tot}/c^2\ell = \pi/2$ — a consistency relation on static solutions, not a derivation of $G$ ($G_4 = G_5/C$, both constants).

**$k$-dial [V].** $v^2/c^2 = k(\pi-2\chi+\sin2\chi)/2\sin2\chi$; $v^2_{\rm eq}/c^2 = k$.

**Stabilization [V].** Winding energy $w^2/2\psi^2$ gives $\psi_0^2 = 3w^2/4|\Lambda_5|$, $m_\psi\psi_0 = w$; PPN $\gamma$ restored from $\tfrac12$ to $1$ with suppression $e^{-3\times10^{15}}$ at 1 AU. **The result that lets the theory survive the solar system.** Price: $\Lambda_4 = -\tfrac12m_\psi^2$, AdS, $10^{60}$ off.

**Consistency [V/D].** Bianchi closes via the exchange term ($O(10^{-32})$ stabilized); the averaged source descends to $\mathbb{RP}^3$ conserved. Seen from the quotient: GR on $\mathbb{RP}^3$ with a $\mathbb{Z}_2$ sheet label, gravity blind to it, Maxwell diagonal in it.

**The price [D].** Two-speed cover: gravity links antipodes instantly, light in $\pi\ell/c$. Preferred frame, no paradox, unobservable, real.

**Galaxy-scale results [V/D].** Closure plateau $v^2_{\rm eq} = 4\pi G\bar\rho = 4GM/\pi\ell$; Tully–Fisher from two-dimensionality, $a_0 = 4\pi G\Sigma_{\rm mean}$ with $\Sigma_{\rm mean} = 69\,M_\odot/{\rm pc}^2$ a Freeman disk; $a_0\approx G\Sigma_0^{\rm central}$ for the Milky Way; four routes to $\ell\approx8$ kpc. Problems: the $\Sigma$-factor in TF; the rise beyond the equator.

**The signature [D].** $r = 1/\sqrt2$, bias-free; mildly disfavored; a drafting-phase signpost.

## I.5 The identification: the first-order theory is a spin structure

This is the recognition version 3 is built on, and it was in the model from the choice of $\mathbb{RP}^3$.

$$S^3 \cong SU(2) \quad\text{(unit quaternions)}, \qquad \mathbb{RP}^3 = S^3/\{\pm1\} \cong SO(3)$$

The quaternion-to-rotation map has kernel exactly $\{\pm1\}$: antipodal points of $S^3$ give the *same* rotation (verified: $|R(q) - R(-q)| = 0$, $\det R = 1$, $RR^T = I$ to machine precision) **[V]**. So:

> **The gravitational base $\mathbb{RP}^3$ is the rotation group $SO(3)$ — spin-1 data. The cover $S^3$ on which light and matter live is the spin group $SU(2)$ — spin-1/2 data. The antipodal map is $-1\in SU(2)$: the spinor sign flip.**

Read the seed in this language. "Matter at $\hat n$ but not at $-\hat n$" is a spinor with a definite sign. Gravity, living on $SO(3)$, cannot see the sign; it sees only the rotation both signs represent. Light, living on $SU(2)$, can. The projective postulate — gravity reads $T_+$ — is the statement that gravity reads the *rotation* a spinor determines and discards its sign. **The seed is "spin-1/2 underneath, spin-1 after the projection,"** and the "distinct-disallowed direction" of the distinctness principle (§II.1) is the sign of a spinor.

This is not an analogy. It is an isomorphism of the arena, and it was the first geometric choice made in the program.

---

# PART II — THE SECOND-ORDER STRUCTURE

## II.1 The distinctness principle, translated

The proposal (Entry 8): physical spacetime is obtained from a deeper space by quotienting *tangent spaces* — at each point some directions are "distinct-allowable," their orthogonal complement "distinct-disallowed," intermediate directions mixed. Photons move in the deeper space, and two paths count as distinct if they traverse the allowable subspace. In the "non-twisting" case both paths from a source must end at one terminal point (the QFT vertex is a single point); "twisting" lets the terminals separate, even to the far hemisphere.

Every phrase has a theorem-grade home **[T]**:

| Entry 8 | standard geometry |
|:--|:--|
| distinct-allowable directions at each point | a **distribution** $D\subset TM$ |
| distinct-disallowed; intermediate | $D^\perp$; the metric splitting $T = D\oplus D^\perp$ |
| non-twisting: two paths from $p$ end at one point | $D$ **integrable** (Frobenius): allowable paths stay on a leaf |
| twisting: terminals separate to the far hemisphere | $D$ **non-integrable** (bracket-generating): by Chow–Rashevskii, allowable paths reach everywhere |
| how far they separate | the **holonomy** of the loop the two paths enclose |

"Twist" is non-integrability; the separation of terminals is holonomy. The decoherence motivation — a camera's resolution deciding which directions register as distinct — becomes, once a holonomy scale is supplied (§II.8), a Machian criterion: directions are distinct when the loop between them encloses more than a quantum.

## II.2 The discrete twist is already present

The gravitational arena is $\mathbb{RP}^3$; light lives on $S^3$; $\pi_1(\mathbb{RP}^3) = \mathbb{Z}_2$. A non-contractible loop in the base lifts to a path from $\hat n$ to $-\hat n$ — a great semicircle, verified trivially **[V]**. Two light paths that differ by the generator of $\pi_1$ end at antipodal points of the cover: *the same point* to gravity, *different points* to light.

**With a $\mathbb{Z}_2$ fiber, the twist is the covering map**, and the two-speed cover is the distinctness structure itself: the antipode is distinct-disallowed for gravity (one point of $SO(3)$) and distinct-allowable for light (two points of $SU(2)$). The probe-dependence of distinctness — "Machian," as the proposal anticipated — is exactly that gravity and electromagnetism live on different spaces.

## II.2b Loosened distinctness and the reference point as root

The two methodological proposals of the program's speculative record — *loosening distinctness* (two seemingly separate points as one underlying point with different allowable structures) and *reference point as root* (position defined by what is invariant under moving between fiber-centers) — are both realized by the structure already built, at two levels each.

**Distinctness, level 0→1.** Same point of $SO(3)$, two sheets $\pm\hat n$ of $SU(2)$, different matter on each (matter on one, twin on the other), and — in this version — different second-order orientation ($+g$ versus $-g$). Two "physical points," one underlying point, different vicinities. The thought experiment "if one underlying point had two different allowable structures, humans would call them two places" is not a hypothesis about a possible universe here; it is the model's standing claim about $\pm\hat n$, made when $\mathbb{RP}^3$ was chosen **[D]**.

**Distinctness, level 1→2, the extreme form [V].** At the Hopf level the allowable structure at a spinor $\psi\in SU(2)$ is the choice of $U(1)$ subgroup to quotient by — an axis $\vec a\in S^2$ — and each choice assigns $\psi$ a different Bloch-sphere point, $\pi_{\vec a}(\psi) = \psi(\vec a\cdot\vec\sigma)\psi^{-1}$. One fixed $\psi$, sampled over 20,000 axes, reaches every point of $S^2$. **One underlying point is literally every physical point, depending on the structure.** This is the mechanism at full strength, too strong to be physics alone — and it shows what constrains it: the axis is not free. It is fixed by the mass the shells are concentric about. *Matter selects the structure.*

**Reference point as root [D].** Move between fiber-centers — a mass and its images — and what stays invariant is the orbit $\Gamma\psi$, i.e. the point $[\psi]\in S^3/\Gamma$. Gravity uses exactly that (the projective postulate); light uses the sheet. "Reference point as root" is therefore the postulate itself: gravity's reference point is $[\psi]$, and which sheet you occupy is structure gravity does not need. The Kelvin self-duality — any node as chart-infinity — is the two-node case.

**What "several fiber-centers are one point" would require.** Enlarging $\mathbb{Z}_2$ to $\Gamma$. The second-order structure constrains this sharply (§II.4, the selection rule), and the lensing signpost worsens as $1/\sqrt{|\Gamma|}$.

**A genuine third order — deferred.** $SU(2)$ is simply connected, so the tower of covers stops at $S^3$; going up means a bigger fiber, not a bigger cover. Two candidates exist: the Hopf tower $S^3\to S^7\to S^4$ (a bundle of physical 3-spheres over a 4-sphere), and the spin-2 second metric on the cover (the fork of §II.7). **No verdict is recorded on either**; the question is held open pending further probing, and nothing in this version depends on it.

## II.3 The second-order construction: Hopf over the concentric shells

About a mass at $\hat n_0\in S^3$, the colatitude shells $\{\chi = \text{const}\}$ foliate $S^3\setminus\{\pm\hat n_0\}$ by 2-spheres. **Take each shell as the base of a Hopf fibration** $S^3_{\rm Hopf}\to S^2_{\rm shell}$. The union over shells is a 4-manifold $E$ with $S^1$ fibers over $S^3\setminus\{\pm\hat n_0\}$: the second-order total space.

What this is, exactly **[T]**: the Hopf fibration $S^3\to S^2$ is the **charge-1 Dirac monopole bundle** over $S^2$. In $S^3\subset\mathbb{C}^2$ with $(z_1,z_2)\sim(e^{i\phi}z_1,e^{i\phi}z_2)$, the connection is $\alpha = \mathrm{Im}(\bar z_1dz_1 + \bar z_2dz_2)$, its curvature is $F = d\alpha = \tfrac12\,\omega_{S^2}$, and the flux through $S^2$ is $2\pi$ — one quantum. So "Hopf over every concentric shell about a mass" is **a monopole sitting at the mass.** The shells are homotopic, so each carries Chern number $+1$ seen from $\hat n_0$.

**The anti-monopole at the twin is automatic [V].** The shell at colatitude $\chi$ from $\hat n_0$ is the shell at colatitude $\pi-\chi$ from $-\hat n_0$, and the outward normal of the ball about $\hat n_0$ is the *inward* normal of the ball about $-\hat n_0$. Its Chern number seen from $-\hat n_0$ is therefore $-1$. The construction places monopole $+1$ at the mass and $-1$ at its twin, and the total charge on the closed $S^3$ is zero — which is the balance theorem (a closed space carries no net monopole charge), satisfied not by fiat but by the geometry of concentric shells on a sphere.

**The fiber degenerates at the mass and at the twin.** With the Hopf metric $S^3(2R)\to S^2(R)$ over a shell of radius $\ell\sin\chi$, the fiber circle has length $4\pi\ell\sin\chi$, vanishing at $\chi = 0,\pi$. The second-order total space is punctured at every mass and every twin — the monopole and anti-monopole singularities. These are bundle defects, not matter.

## II.4 Descent to the gravity-visible base

Does the second-order structure survive both quotients? The antipodal map $\sigma$ of $S^3$ sends shell $\chi$ to shell $\pi-\chi$ *and*, on each shell, acts as that $S^2$'s own antipodal map: $(\cos\chi,\sin\chi\,\vec m)\mapsto(\cos(\pi-\chi),\sin(\pi-\chi)(-\vec m))$. The antipodal map of $S^2$ is orientation-reversing, so it pulls the Chern-$(+1)$ bundle back to Chern-$(-1)$:

$$\sigma^*E \cong \bar E \not\cong E \;\text{ as } U(1)\text{-bundles}, \qquad \sigma^*E\cong E \;\text{ as } O(2)\text{-bundles}$$

via fiber conjugation. **The second-order total space descends to $\mathbb{RP}^3$ as an $O(2)$-bundle whose fiber orientation reverses around the non-contractible loop [D].** The base is $\mathbb{RP}^3 = SO(3)$, the same as gravity's. No conflict. The orientation reversal is "the twin carries opposite monopole charge," said topologically — and it is the second-order image of the first-order sign flip.

**The selection rule: why $\mathbb{Z}_2$ and not a larger quotient [D].** The cone theorem admits any $S^3/\Gamma$ with $\Gamma\subset SO(4)$ acting freely. The second-order structure narrows this. Hopf-over-shells about a mass at $\hat n_0$ produces charge $+1$ at $\hat n_0$ and $-1$ at $-\hat n_0$ *and nothing anywhere else* — the shells about $\hat n_0$ close up only on its antipode. For the bundle to descend to $S^3/\Gamma$ it must be $\Gamma$-invariant, so every image $\gamma\hat n_0$ must carry charge $\pm1$; closure then requires the charges to sum to zero over each orbit. Hence:

- **$|\Gamma|$ odd is excluded outright** — no sign assignment sums to zero.
- **$|\Gamma| > 2$ even is admissible only with alternating signs imposed by hand** — the construction does not supply them.
- **$\Gamma = \mathbb{Z}_2$ is the unique case the construction produces on its own.**

So the second-order structure *selects the antipodal quotient* among everything the first-order theory allowed. This is the first place in the program where $\mathbb{Z}_2$ is explained rather than chosen. (A larger even $\Gamma$ would also worsen the lensing signpost of §I.4 to $r = 1/\sqrt{|\Gamma|}$.)

## II.5 The generalization

For $N$ point masses, $N$ monopoles at the masses and $N$ anti-monopoles at their twins. For a continuous distribution, a $U(1)$ connection with curvature sourced by a monopole density:

$$dF = \star\rho_{\rm mono}, \qquad \int_{S^3}\rho_{\rm mono} = 0$$

the second condition forced by closure. Hopf-over-shells applied to each element of mass gives, for each $\rho(\hat n)$, a monopole at $\hat n$ and an anti-monopole at $-\hat n$:

$$\boxed{\;\rho_{\rm mono}(\hat n) = \frac{1}{m_{\rm unit}}\big[\rho(\hat n) - \rho(-\hat n)\big] = \frac{\rho_-(\hat n)}{m_{\rm unit}}\;}$$

**the antipodally odd part of matter**, with $m_{\rm unit}$ a new constant, the mass per flux quantum. Monte Carlo on a two-lump distribution: $\langle\rho_+\rangle = 0.150$, $\langle\rho_-\rangle = -2\times10^{-4}$, i.e. zero as closure requires **[V]**.

## II.6 The partition theorem

Gravity on $\mathbb{RP}^3$ reads $S = \rho_+$ — the even part (Law I). The second-order fiber reads $\rho_-$ — the odd part (§II.5). Since $\rho = \tfrac12(\rho_+ + \rho_-)$:

> ### ■ THE PARTITION
> **The two fibrations partition matter.** Gravity sees what the projection keeps; the twist sees what it discards. Together they see everything. The second-order structure carries exactly the information the projective postulate throws away. **[D]**

In spin language: gravity on $SO(3)$ reads the rotation a spinor determines; the second-order fiber reads its sign. Neither alone is the spinor; together they are.

**On the analogy to Ricci and Weyl.** The Ricci–Weyl split is *sourced-versus-free*: Ricci is fixed by local matter, Weyl propagates. Here both pieces are *sourced* — $\rho_+$ sources the base Ricci, $\rho_-$ sources the second-order $F$. The tighter analogy is therefore **electric and magnetic**: $\rho_+$ is gravito-electric (sources Ricci through a Gauss-type law), $\rho_-$ is second-order-magnetic (sources a monopole field through the magnetic Gauss law). The free part of the theory is the base Weyl tensor, which is even; the odd sector, as a $U(1)$ structure, has no free part.

## II.7 What sources the second-order fiber: matter, directly

**Curvature side or matter side?** The base curvature is sourced by $S = T_+$ and is therefore antipodally even; the cover metric is its pullback, also even. **$T_-$ has no curvature representative anywhere in the first-order theory.** So the second-order fiber cannot take the base curvature as its source — it would see only the even part again — and must take matter, specifically the odd part, directly **[D]**.

The elegant statement survives in the right form: **the full stress-energy is encoded in two curvatures,**

$$\text{base Ricci} \;\leftarrow\; T_+ \;\;(\text{Law I}), \qquad \text{second-order } F \;\leftarrow\; J_- \;\;(dF = \star J_-)$$

where $J_-$ is the odd part of the mass *current*. A $U(1)$ connection couples covariantly to a current — four components — not to a stress tensor — ten. So the Hopf extension captures the odd mass current; the six odd stress and pressure components are invisible to both structures. **Capturing all of $T_-$ requires a spin-2 second-order structure — a second metric on the cover, sourced by $T_-$ — at which point the theory approaches general relativity on the cover.** That fork is real and is recorded as open (§III.2).

## II.8 Holonomy and the Machian distinctness criterion

Two light paths from $p$ to $q$ enclosing odd-mass $m_-$ end at second-order-fiber positions differing by

$$\Delta = 2\pi\,\frac{m_-}{m_{\rm unit}}$$

— a relative phase between the paths **[D]**. For $m_-\gg m_{\rm unit}$ the phase is effectively random: **paths on opposite sides of a large mass decohere.** For $m_-\ll m_{\rm unit}$ they interfere. This is the camera-decoherence criterion of Entry 8 with a threshold set by enclosed matter rather than by the instrument: *distinct* means separated by more than a quantum of odd-mass. "Twist negligible at Earth scale" is then the statement that $m_{\rm unit}$ is large. The fiber-antipode is reached by enclosing half a quantum. In the Hopf model with a single point mass, holonomy is exactly half the enclosed solid angle at every colatitude — the spin-1/2 Berry phase — verified numerically at $30°, 60°, 90°, 120°$ **[V]**.

## II.9 The quantization fork

Dirac's condition: the flux through any closed surface is an integer number of quanta. With $\rho_{\rm mono} = \rho_-/m_{\rm unit}$, the flux through a surface enclosing odd-mass $m_-$ is $m_-/m_{\rm unit}$ — integer only if odd-masses are quantized in $m_{\rm unit}$. Point masses with one quantum each sidestep this; continuous distributions force a choice **[O]**:

- **(a) $U(1)$ fiber, masses quantized in $m_{\rm unit}$.** Then $m_{\rm unit}$ must be tiny (Planck-scale) to hide the quantization, holonomy is random at *all* scales, decoherence is universal, and "twist negligible at Earth scale" fails.
- **(b) $\mathbb{R}$ fiber (non-compact).** No quantization, continuous holonomy, the odd-part coupling intact — but no fiber-antipode and no spinor sign flip at the second-order level. (The first-order $SU(2)/SO(3)$ reading of §I.5 is untouched either way.)

This is the first genuine decision version 3 owes.

## II.10 Black holes

Three operators fix three twin signs:

| sector | operator | twin |
|:--|:--|:--|
| mass | $\Delta_{S^3}+3$ | same sign |
| electric charge | $\Delta$ | opposite sign |
| second-order monopole | Hopf orientation | opposite sign |

**A Reissner–Nordström hole $(M,Q)$ at $\hat n$ has twin $(M,-Q)$ at $-\hat n$: its charge conjugate.** Extremality $|Q| = M$ is preserved under conjugation, so extremal twins are extremal **[D]**.

**Every black hole is magnetically charged in the second-order $U(1)$.** Its horizon 2-sphere carries Chern number $M/m_{\rm unit}$ (in option (a); continuous flux in option (b)). If the second-order field strength gravitates with coupling $g_2$, the exterior is of Reissner–Nordström type with an effective magnetic charge $P_{\rm eff} = g_2M/m_{\rm unit}$ and the extremality bound becomes

$$M^2 = Q^2 + P_{\rm eff}^2$$

**The ratio $g_2/m_{\rm unit}$ decides whether Schwarzschild holes exist at all**: for $P_{\rm eff}\ll M$ neutral holes are Schwarzschild to the observed precision; at $P_{\rm eff} = M$ no neutral hole is sub-extremal **[D]**. Solar-system and gravitational-wave data bound $g_2/m_{\rm unit}$ from above; this is a computable constraint not yet computed.

## II.11 The second-order structure as spin-1/2, one level down

The Hopf fibration is $SU(2)\to SU(2)/U(1) = S^2$: **unit spinors mapped to their spin direction** (the Bloch sphere). The fiber is the spinor phase. Its holonomy — half the enclosed solid angle — is the spin-1/2 Berry phase, and around a loop enclosing a hemisphere it is $\pi$: **the spinor changes sign.** So the second-order fiber-antipode is again a spinor sign flip, and the second-order total space over each concentric shell is the space of unit spinors whose direction lies on that shell **[T/V]**.

The pattern is therefore the same at both levels: a spinor structure ($SU(2)$) projected to its direction data ($S^2$ or $SO(3)$), with the projection discarding a $\mathbb{Z}_2$ (the sign) and gravity reading only what survives. Version 3's claim, stated once: *what we call spacetime is the direction data of a spinor structure; the sign is the distinct-disallowed direction; gravity is blind to it and light is not.*

## II.12 What the second-order structure does not do

**No redshift.** Holonomy is a phase, not a frequency. The Killing-energy theorem — in a static metric, $E = (1+2\Phi)\,dt/d\lambda$ is conserved along null rays and light returning to its source has exactly its emitted frequency — is untouched **[T]**. With two terminals at $\pm\hat n$ the amplitude is $A_{\hat n} + A_{-\hat n}$, interfering with relative phase $\omega\pi\ell/c$; the detection rate carries an intensity comb of spacing $2c/\ell\approx4\times10^{-13}$ Hz at 8 kpc, unobservably fine, and modulates intensity without shifting frequency **[V]**. Twist relocates endpoints; redshift needs a non-static geometry.

**The twin is no longer nothing.** It carries an anti-monopole — a topological defect. Light passing it on two sides picks up the defect's holonomy. Not matter, not reflection, but a phase signature. The antipode stays *materially* dark and becomes *topologically* marked. Whether this is a feature (light can finally see the twin, non-materially) or a cost (the seed wanted nothing there) is a choice, and it should be made deliberately **[D]**.

## II.13 Laws and axioms, version 3

> ### ■ ARENA
> - **A1.** $M_5 = \mathbb{R}_t\times S^1_u\times S^3$, with $S^3\cong SU(2)$.
> - **A2.** Gravitational base $B_4 = \mathbb{R}_t\times\mathbb{RP}^3$, with $\mathbb{RP}^3\cong SO(3)$; the fiber over $[\hat n]$ has two components (§I.2).
> - **A3.** $\chi(M_5) = 0$; $\Lambda_5<0$ for stabilization.
> - **A3′ (new).** A second-order $U(1)$ (or $\mathbb{R}$, §II.9) bundle $E\to M_5$, defined by Hopf-extending the concentric shells about every element of mass; over $B_4$ it is an $O(2)$-bundle.

> ### ■ FIELDS
> - **A4.** Base metric $g^{(4)}$; compact fiber scalar $f$ with winding $\ln\lambda$; dilaton $\psi$ stabilized at $\psi_0^2 = 3w^2/4|\Lambda_5|$, $m_\psi = 1/\psi_0$.
> - **A5.** Electromagnetic 2-form $\mathcal{F}$ on $M_5$.
> - **A6 (new).** Second-order connection $\alpha$ on $E$ with curvature $F = d\alpha$.

> ### ◆ LAW I — GRAVITY
> - **A7.** Projective postulate: the source is $S = T_+$, the even part.
> - **A8.** $\ell^2R_{\mu\nu} = \ell^2\psi^{-1}\nabla\nabla\psi + 2(\tau - \tfrac13\tau g)$; $\ell^2\Box\psi = -\tfrac43\psi(\tau_u - \tfrac12\tau)$.

> ### ◆ LAW II — THE FIBRATION
> - **A9.** $\Box f = 0$, $\oint df = \ln\lambda$: unsourced, rigid.

> ### ◆ LAW III — THE SECOND-ORDER CONNECTION (new)
> - **A10.** $dF = \star J_-/m_{\rm unit}$: **the curvature of the second-order bundle is sourced by the antipodally odd mass current.** Closure ($\int\rho_- = 0$) is automatic. Holonomy around a loop is $2\pi m_-/m_{\rm unit}$.
> - **A11.** Whether $F$ gravitates (coupling $g_2$) is open; if it does, black holes acquire $P_{\rm eff} = g_2M/m_{\rm unit}$.

> ### ◆ ELECTROMAGNETISM
> - **A12.** $d\mathcal{F} = 0$, $d\star_5\mathcal{F} = \star_5\mathcal{J}$ on the cover.

> ### ▣ DERIVED
> - **D1.** $\Lambda = 1/\ell^2$ (cone). **D2.** No endpoints (unsourced $f$). **D3.** The static twin is the quotient. **D4.** Mach relation, $k$-dial. **D5.** $\gamma = 1$ (stabilization). **D6 (new).** The partition: $T_+$ to gravity, $J_-$ to the second-order fiber. **D7 (new).** Twin signs: $(M,Q,g)\to(M,-Q,-g)$. **D8 (new).** The seed is $SU(2)\to SO(3)$.

**Free parameters of version 3.** The winding integer $w$ · one scale $|\Lambda_5|$ (equivalently $\psi_0$) · the quotient $\Gamma$ · the equation of state · **and, new: $m_{\rm unit}$ (mass per flux quantum) and $g_2$ (whether and how strongly $F$ gravitates).** Two new constants, both bounded by observation in principle and neither yet bounded in practice.

---

# PART III — STATUS

## III.1 The ledger of version 3

| result | tag |
|:--|:--|
| $S^3\cong SU(2)$, $\mathbb{RP}^3\cong SO(3)$, antipodal $= -1$: the seed is spin-1/2 vs spin-1 | **[V]** |
| Entry 8 = distribution / Frobenius / Chow / holonomy | **[T]** |
| the discrete twist is $\pi_1(\mathbb{RP}^3) = \mathbb{Z}_2$; two-speed = distinctness | **[V/D]** |
| Hopf over shells = Dirac monopole at the mass; anti-monopole at the twin, automatically | **[T/V]** |
| descent to $\mathbb{RP}^3$ as an $O(2)$-bundle; base unchanged | **[D]** |
| $\rho_{\rm mono} = \rho_-/m_{\rm unit}$; closure automatic | **[V]** |
| the partition: $T_+$ to gravity, $J_-$ to the second-order fiber | **[D]** |
| source is matter directly; $T_-$ has no first-order curvature representative | **[D]** |
| $U(1)$ captures the odd current; full $T_-$ needs spin-2 | **[D]** |
| holonomy $= 2\pi m_-/m_{\rm unit}$; Hopf holonomy $= \Omega/2$ | **[V]** |
| Machian decoherence criterion | **[S]** |
| quantization fork | **[O]** |
| RN twin is the charge conjugate; extremal twins extremal | **[D]** |
| every hole magnetically charged; $M^2 = Q^2 + P_{\rm eff}^2$ | **[D]** |
| no redshift from the twist | **[T]** |
| the twin is topologically marked | **[D]** |
| loosened distinctness realized at levels 0→1 and 1→2; one spinor reaches all of $S^2$ over axis choices | **[D/V]** |
| reference point as root = the projective postulate; Kelvin duality its two-node case | **[D]** |
| selection rule: Hopf-over-shells produces $\mathbb{Z}_2$ alone; odd $\Gamma$ excluded; even $\Gamma>2$ needs hand-imposed signs | **[D]** |

## III.2 Open problems of version 3

1. **The quantization fork** (§II.9) — $U(1)$ with quantized masses, or $\mathbb{R}$ with continuous holonomy. The first decision the version owes.
2. **Does $F$ gravitate, and how strongly?** — $g_2$, and the bound on $g_2/m_{\rm unit}$ from the existence of near-Schwarzschild black holes.
3. **The spin-2 fork** (§II.7) — whether the six odd stress components need a second metric, and whether that collapses the theory to GR on the cover.
4. **What sets $m_{\rm unit}$** — the scale at which paths decohere by enclosed matter. Galactic, if the twist is to be negligible locally.
5. **The twin's marking** — feature or cost; a deliberate decision about the seed's character.
6. **The third order** — Hopf tower or spin-2 second metric; *deliberately held open* pending more probing.
7. **Inherited from version 2** — the AdS uplift ($10^{60}$, the single blocking problem); a law for $\ell$ in the Tully–Fisher sector; the rise beyond the equator; the literature review before anything is called new.

## III.3 The next three moves

1. **Bound $g_2/m_{\rm unit}$ from black-hole observations.** The extremality shift $M^2 = Q^2 + P_{\rm eff}^2$ is a concrete prediction; near-Schwarzschild ringdowns and shadow measurements constrain it.
2. **Decide the quantization fork by computing both.** Take a smooth distribution, build the $\mathbb{R}$-connection and the $U(1)$-connection with the nearest integer flux, and see which one produces consistent holonomy for the two-path amplitude.
3. **Write the spin-2 version and check whether it is GR.** If a second metric on the cover sourced by $T_-$ reproduces Einstein on $S^3$, the $U(1)$ choice is what keeps the theory distinct, and that should be known before anything else is built on it.

---

## Reference card, version 3

| topic | statement |
|:--|:--|
| **spin identification** | $S^3 = SU(2)$, $\mathbb{RP}^3 = SO(3)$, antipodal $= -1$; the seed is the spinor sign |
| **distinctness** | distribution $D$; twist = non-integrability; separation = holonomy |
| **discrete twist** | $\pi_1(\mathbb{RP}^3) = \mathbb{Z}_2$; two-speed cover |
| **Hopf extension** | monopole at mass, anti-monopole at twin; fiber length $4\pi\ell\sin\chi$ |
| **descent** | $O(2)$-bundle over $\mathbb{RP}^3$; base unchanged |
| **Law III** | $dF = \star J_-/m_{\rm unit}$; closure automatic |
| **partition** | $T_+\to$ Ricci, $J_-\to F$; electric/magnetic, not Ricci/Weyl |
| **holonomy** | $2\pi m_-/m_{\rm unit}$; Hopf: $\Omega/2$ = Berry phase |
| **black holes** | twin $(M,-Q,-g)$; $M^2 = Q^2 + P_{\rm eff}^2$, $P_{\rm eff} = g_2M/m_{\rm unit}$ |
| **new constants** | $m_{\rm unit}$, $g_2$ |
| **fork** | $U(1)$ + quantized mass, or $\mathbb{R}$ + continuous holonomy |
| **selection rule** | Hopf-over-shells yields $\mathbb{Z}_2$ only; $\lvert\Gamma\rvert$ odd excluded |
| **distinctness** | sheets at level 0→1; axis choice at level 1→2 (one $\psi$ reaches all $S^2$); matter fixes the axis |
| **third order** | Hopf tower $S^7\to S^4$ or spin-2; held open |
| **does not** | shift frequency (static theorem); keep the twin unmarked |
