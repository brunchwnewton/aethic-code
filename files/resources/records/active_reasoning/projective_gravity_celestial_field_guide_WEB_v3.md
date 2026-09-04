# Projective Gravity — Version 3

### The Spin Structure: a field guide

> **What this version is.** Version 2 was the *minimal theory*: Kaluza–Klein on $\mathbb{R}_t\times S^1_u\times S^3$ with a rigid fibration, a winding-stabilized radion, electromagnetism on the double cover, and one postulate — gravity reads the fiber average. Version 3 keeps all of it unchanged, adds a **second-order fibration** built by Hopf-extending the concentric shells about every mass, and records a recognition that reorganizes the whole: **the first-order theory was already a spin structure.** The gravitational base is $SO(3)$; the cover on which light and matter live is $SU(2)$; the antipodal map is the spinor sign flip. The seed — matter at $\hat n$, gravity at both $\pm\hat n$ — is the statement that gravity lives on the rotation group and cannot see the sign of a spinor. The second-order structure repeats this pattern one level down and captures exactly the information the first-order projection discards.
>
> **Tags.** **[V]** verified symbolically or numerically · **[M]** measured numerically · **[T]** established theorem, cited · **[D]** derived here · **[S]** sketch · **[O]** open · **[R]** retired.
>
> **Conventions.** $G = c = 1$ unless restored; $\ell$ = radius of the spatial 3-sphere; $\hat n\in S^3$, $[\hat n]\in\mathbb{RP}^3$; $T_\pm(\hat n) \equiv T(\hat n)\pm T(-\hat n)$ the antipodally even and odd parts of any field on the cover.
>
> **Reading guide.** The spin identification and the dimension bookkeeping: §I.5. Distinctness and the root, realized: §II.2b. The second-order construction: §II.3–§II.5. The selection rule: §II.4. The partition theorem: §II.6. What sources it: §II.7. The quantization fork: §II.9. Black holes: §II.10. The conformal root and the placement principle: §II.13. Electromagnetism at second order: §II.14. The geometry of $E$: §II.15. The Lagrangian: §II.16. Recentering: §II.17. Laws and axioms of version 3: §II.18. Status and open problems: Part III.

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

**Nothing is overwritten, and space stays three-dimensional.** The identification is a statement about what the spatial 3-sphere already *is* as a manifold; it adds no dimensions and replaces no structure. The gravitational base $\mathbb{RP}^3 = SO(3)$ is likewise three-dimensional. The bookkeeping, kept explicit because the group name will recur at the second order:

| object | dimension | what it is |
|:--|:--|:--|
| spatial slice | **3** | $S^3$, which *is* $SU(2)$ |
| gravitational base | **3** | $\mathbb{RP}^3 = S^3/\mathbb{Z}_2$, which *is* $SO(3)$ |
| a concentric shell about a mass | 2 | $S^2_\chi$ |
| the Hopf lift of one shell (§II.3) | 3 | $S^3_{{\rm Hopf},\chi}$ — a *different* 3-sphere, one per shell |
| the union of all Hopf lifts (§II.3) | **4** | $E$, a $U(1)$-bundle over the 3-D space |

Two different 3-spheres will wear the name $SU(2)$: the spatial one here, and each Hopf one in Part II. They are not the same object.

**The shells are the conjugacy classes [V].** Put the mass at the identity of the spatial $SU(2)$. A point $(\cos\chi,\sin\chi\,\vec m)$ of $S^3$ is the group element $e^{i\chi\,\vec m\cdot\vec\sigma}$ — a rotation by $2\chi$ about the axis $\vec m$ — and conjugacy classes of $SU(2)$ are fixed by $\mathrm{tr}\,U = 2\cos\chi$, i.e. by $\chi$ alone. So:

> **The concentric shells about a mass are the conjugacy classes of $SU(2)$ with the mass at the identity.** Distance from the mass is a rotation angle. The equator ($\mathrm{tr}\,U = 0$) is the class of rotations by $\pi$. The antipode ($\mathrm{tr}\,U = -2$) is $-1$.

Verified: $\mathrm{tr}\,U = 1.911$ at $\chi = 0.3$, exactly $0$ at the equator, exactly $-2$ at the antipode. "Travelling to the antipode is a $2\pi$ rotation" is thereby a statement about *space*, not only about spinors — and it makes the shells chosen for the Hopf lift the *canonical* 2-spheres of the group rather than an arbitrary foliation.

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

About a mass at $\hat n_0\in S^3$, the colatitude shells $\{\chi = \text{const}\}$ foliate $S^3\setminus\{\pm\hat n_0\}$ by 2-spheres — the conjugacy classes of §I.5. **Take each shell as the base of a Hopf fibration** $S^3_{{\rm Hopf},\chi}\to S^2_\chi$: each 2-sphere is lifted to its *own* 3-sphere. The union over shells is a 4-manifold $E$ — the second-order total space — which is fibered two ways at once:

$$E \;\to\; (0,\pi) \quad\text{with fiber } S^3_{{\rm Hopf},\chi}, \qquad\qquad E \;\to\; S^3\setminus\{\pm\hat n_0\} \quad\text{with fiber } S^1$$

The first slicing is "each shell lifted to a 3-sphere"; the second is "a Hopf circle over each point of space." **Physical space remains the 3-D $S^3$; $E$ is 4-D and sits over it.** The spatial $S^3$ (first order) and the Hopf $S^3_{{\rm Hopf},\chi}$ (second order, one per shell) are different manifolds that happen to be the same group.

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

The pattern is therefore the same at both levels — a spinor structure ($SU(2)$) projected to its direction data ($SO(3)$ at the first order, $S^2_\chi$ at the second), with the projection discarding a sign and gravity reading only what survives — *on different spaces*: the spatial 3-sphere at the first order, each Hopf 3-sphere over a shell at the second (§I.5, bookkeeping). Version 3's claim, stated once: *what we call spacetime is the direction data of a spinor structure; the sign is the distinct-disallowed direction; gravity is blind to it and light is not.*

## II.12 What the second-order structure does not do

**No redshift.** Holonomy is a phase, not a frequency. The Killing-energy theorem — in a static metric, $E = (1+2\Phi)\,dt/d\lambda$ is conserved along null rays and light returning to its source has exactly its emitted frequency — is untouched **[T]**. With two terminals at $\pm\hat n$ the amplitude is $A_{\hat n} + A_{-\hat n}$, interfering with relative phase $\omega\pi\ell/c$; the detection rate carries an intensity comb of spacing $2c/\ell\approx4\times10^{-13}$ Hz at 8 kpc, unobservably fine, and modulates intensity without shifting frequency **[V]**. Twist relocates endpoints; redshift needs a non-static geometry.

**The twin is no longer nothing.** It carries an anti-monopole — a topological defect. Light passing it on two sides picks up the defect's holonomy. Not matter, not reflection, but a phase signature. The antipode stays *materially* dark and becomes *topologically* marked. Whether this is a feature (light can finally see the twin, non-materially) or a cost (the seed wanted nothing there) is a choice, and it should be made deliberately **[D]**.


## II.13 The conformal root, the family of bases, and the placement principle

*This section takes the proposal that the conformal class of the second-order total space is the theory's actual root, and unpacks it to the end. Four computations settle what it means; the last of them turns a pair of earlier statements into a single structural principle.*

### II.13.1 $E$ is conformally $S^4$, and the rejected 4-sphere returns

Give $E$ its natural metric — the spatial $\ell^2d\chi^2$ in the interval direction, and over each shell of radius $\ell\sin\chi$ its Hopf 3-sphere at the Riemannian-submersion radius $2\ell\sin\chi$:

$$g_E = \ell^2\,d\chi^2 + 4\ell^2\sin^2\chi\;g_{S^3(1)}, \qquad \chi\in(0,\pi)$$

The reparametrization $\tan(\chi'/2) = \sqrt{\tan(\chi/2)}$ is a smooth bijection of $(0,\pi)$ under which the radial and angular terms match a single conformal factor at every $\chi$ **[V]**. Hence

$$\boxed{\;E \;\text{is conformal to}\; S^4\setminus\{p,\bar p\}, \qquad p = \text{the mass},\;\; \bar p = \text{its twin}\;}$$

The 4-sphere that the program rejected at first order — "fibers radiating from a point of $S^4$," forbidden because $\chi(S^4) = 2$ leaves no room for a nowhere-vanishing fiber — **returns at second order with the obstruction made physical.** The fiber degenerates at exactly two points, the monopole and the anti-monopole, each with index $+1$; their sum is $\chi(S^4) = 2$ **[T]**. Poincaré–Hopf is no longer a veto. It is the reason there are two marked points, and it says which two.

### II.13.2 One conformal root carries the first-order fibration too

The first-order cylinder $\mathbb{R}_u\times S^3 = \mathbb{R}^4\setminus\{0\}$ is likewise conformal to $S^4$ minus two points. So both total spaces are the same conformal 4-manifold, fibered differently:

| order | fibers | removed points | base |
|:--|:--|:--|:--|
| first | circles *through* the two points (the radial lines) | $\{0,\infty\}$ | $\mathbb{RP}^3$ — *directions* |
| second | Hopf circles on the latitude 3-spheres, *avoiding* them | $\{p,\bar p\}$ | $S^3\setminus\{p,\bar p\}$ — *space* |

The conformal group of $S^4$ is $SO(5,1)$, 2-transitive on points, so $\{0,\infty\}$ and $\{p,\bar p\}$ are equivalent pairs **[T]**. **One root, two fibrations, two bases.** The first-order and second-order theories are two members of the family this section is about. *Caveat, held open:* the first-order theory then quotients by the dilation $u\to u+\ln\lambda$, and $E$ carries no such quotient — the conformal roots coincide, the compactifications do not.

### II.13.3 The family of bases, exactly

Free circle actions on the latitude $S^3$, up to conjugacy, are the $(p,q)$ actions $(z_1,z_2)\mapsto(e^{ipt}z_1,e^{iqt}z_2)$ with $\gcd(p,q) = 1$ **[T]**. The $(1,1)$ action is Hopf and its base is a smooth $S^2$ — the member the program started from. Every other $(p,q)$ gives an orbifold base, a weighted projective line with cone points of orders $p$ and $q$. Within $(1,1)$ there is the continuous axis choice of §II.2b, which yields isometric bases with different point-identifications. So:

$$\text{family of bases} \;=\; \{(p,q)\}_{\gcd = 1}\;\times\;S^2_{\rm axis}, \qquad \text{original base} = (1,1)$$

discrete times continuous, with the theory's first base as one point of it. The first-order $\mathbb{Z}_2$ quotient must still be available on whatever base is chosen, which restricts the family to bases admitting a free involution.

### II.13.4 The fiber partition is the Weyl tensor of $E$ [V]

This is the computation that makes the rest of the section true. With the Hopf connection $A = \cos\theta\,d\varphi$ on each latitude, $C_{abcd}C^{abcd} = 0$: conformally flat, as §II.13.1 says. **Perturb the circle partition with the same centers** — $A = (\cos\theta + \epsilon\sin^2\theta)\,d\varphi$, a different way of laying circles between the same monopole and anti-monopole — and

$$C_{abcd}C^{abcd} = \frac{4\epsilon^2\,(16 - 13\sin^2\theta)}{3\sin^4\chi} \;>\; 0$$

$$\boxed{\;\text{The deviation of the fiber partition from Hopf is the Weyl tensor of } E.\;}$$

Any other circle partition between the same centers makes $E$ non-conformally-flat, by an amount equal to how far the fibers were moved. Two consequences follow immediately.

**The Ricci–Weyl partition, realized one level up.** §II.6 said the even/odd split of matter was electric/magnetic rather than Ricci/Weyl, because both pieces are sourced. That was true at the level of the *base*. One level up it is Ricci/Weyl after all:

$$\text{base Ricci} \;\longleftarrow\; T_+, \qquad\qquad E\text{-Weyl} \;\longleftarrow\; J_-$$

The odd mass current does not merely source a $U(1)$ curvature; that curvature *is* the Weyl tensor of the second-order total space in Kaluza–Klein dress. The even part of matter is Ricci on the base; the odd part is Weyl on $E$. The original intuition was correct, with the Weyl tensor living one floor above where it was first sought.

**The conformal class is not fixed; it is the vacuum of the odd sector.** $E\sim S^4$ exactly when there is one mass and its twin — one monopole per shell, the Hopf value. Any additional odd matter deforms the conformal class by the formula above. So the root is not a fixed conformal 4-manifold but *conformally flat $E$ plus a Weyl deformation sourced by $J_-$*, and "the family of fibrations of a fixed root" is the family for fixed odd matter.

### II.13.5 What moves the Einstein tensor, and what does not

The proposal was that shifting the fibration on $E$ yields a new first-order total space, hence a new base, hence a new Einstein tensor — and that by complementarity this is the same as shifting the Hopf fibers. Both halves are correct, with one precision each.

**What does not move it.** Within isometric $U(1)$-fibrations, the curvature $F$ is fixed by the monopole positions; changes of the connection $A$ at fixed $F$ are gauge; and the quotient metric $g_B$ (the horizontal metric of the Kaluza–Klein decomposition) is independent of $A$ **[D]**. So rearranging circles between *fixed* centers changes neither $F$ nor $g_B$ nor the Einstein tensor. "Same centers, different circles" is a relabelling. This is why the base-level partition of §II.6 holds: the Einstein tensor sees only $T_+$, and no gauge motion of the odd sector can reach it.

**What does move it.** For conformally flat $E$ the isometry group is $SO(5)$, and the Hopf-type fibrations are its orbit on point-pairs $\{p,\bar p\}$: **the family of fibrations is the family of where the mass is** **[D]**. Move through it and the gravitational well moves from $p$ to $q$ *and* the monopole moves from $p$ to $q$, by the same rotation of $S^4$. Nothing else can move them, and nothing can move one without the other. With more masses, $E$ acquires Weyl, the isometry group shrinks, the family narrows — and the lockstep persists on what remains.

So the complementarity is exact and it is this: **the Einstein tensor on the base and the Weyl tensor of $E$ are the even and odd faces of one placement of matter.** They are not two dials. They are two shadows of a single choice, and the choice is where the matter is.

### II.13.6 The placement principle

The program has, at several points, stated a pair of facts as though they were separate: that gravity reads the even part and the twist reads the odd part (the partition, §II.6), and that matter selects the fibration (§II.2b). §II.13 shows they are one fact seen twice. Stated once, as a principle of the model's structure:

> ### ■ THE PLACEMENT PRINCIPLE
> The arena is one conformal 4-manifold — conformally flat in the absence of odd matter, and deformed by it. A placement of matter on this arena is not described by a metric and separately by a fibration; **the placement *is* the fibration.** Its even face is the Ricci curvature of the quotient base, read by gravity through Law I. Its odd face is the Weyl curvature of the total space, read by light through the second-order holonomy. Moving the matter moves both faces together, and nothing else moves either. The fibration is therefore not a convention imposed on the arena: it is the arena's record of where everything is. What *is* conventional is the axis label within the Hopf class — a relabelling of points, not a change of physics — and the conformal factor, which is not conventional at all but is the one scalar the conformal root cannot supply: the dilaton, which the first-order theory already carries for exactly this reason.

**Three things the principle explains that were previously separate.** Why the fibration was found to be rigid at first order (§I.1): rigidity is what "the placement is the fibration" looks like when the placement is homogeneous. Why the dilaton had to exist (§I.4): a conformal class has no scale and Law I needs one, so the metric is conformal class times one field, and that field is $\psi$. And why every attempt to make the fibration respond to matter as a *separate* coupling failed and was retired (the dielectric, §I.8): the fibration already *is* the matter's placement, and a second coupling was a second copy of the same information, which the constancy of $\alpha_{\rm fine}$ duly bounded to zero.

**What the principle does not do.** It does not shift frequencies — the static theorem stands, and a placement is a static datum. It does not choose between the $U(1)$ and $\mathbb{R}$ fibers (§II.9). It does not decide the third order, which remains held open. And it does not, by itself, tell you the placement: it says that once you know where the matter is, you know everything the two fibrations know, and nothing more.


## II.14 Electromagnetism on the second-order total space

*The first-order electromagnetic law put $\mathcal{F}$ on the cover $S^3$ and derived that light rides the base's null geodesics unrefracted, sourced only where charge is. The question is how that law adapts to $E$ — and specifically how the distinctness principle acts on light: whether a photon's two paths may begin at different points of the second-order fiber. The answer keeps the first-order photon exactly, identifies which fields see the fiber, reproduces a known optical effect, and produces the first observational bound on $m_{\rm unit}$.*

### II.14.1 The reduction on a non-trivial circle bundle [T/V]

Write the electromagnetic potential on $E$ in the horizontal–vertical frame of the Hopf bundle, $e \equiv d\psi_2 + \alpha$ with $\alpha$ the Hopf connection:

$$\mathcal{A}_E = \mathcal{A}_B + \phi\,e, \qquad d\mathcal{A}_E = \big[\mathcal{F}_B + \phi\,F_{\rm Hopf}\big] + d\phi\wedge e$$

using $de = d\alpha = F_{\rm Hopf}$. The effective field strength on the base is

$$\boxed{\;\mathcal{F}_{\rm eff} = \mathcal{F}_B + \phi\,F_{\rm Hopf}\;}$$

**The second-order monopole field enters the electromagnetic field strength, multiplied by the fiber-component scalar $\phi$.** This is the standard Kaluza–Klein reduction on a bundle with curvature, verified explicitly on the Hopf bundle (the coordinate components differ from the frame components by exactly the horizontal part of $d\phi\wedge\alpha$, as they must). The scalar $\phi$ — the fiber component of $\mathcal{A}_E$ — is new; its zero mode is the Wilson line $\oint\mathcal{A}_E$ around the Hopf circle.

### II.14.2 The photon does not propagate in the fiber [D]

The Hopf fiber over a shell has length $L_2 = 4\pi\ell\sin\chi$ — about $100$ kpc at the equator for $\ell = 8$ kpc. A field free to move along a fiber that long would spread through *four* spatial dimensions at every sub-100-kpc distance, with flux falling as $1/r^3$. Every inverse-square test excludes this. **The photon is therefore a section over the base, labelled by a Hopf charge $n$, not a field propagating in $E$.** The Hopf-neutral photon, $n = 0$, is the first-order photon *exactly*: $\epsilon\mu = 1$, on the cover, unrefracted, sourced only where charge is. First-order behaviour is retained in full.

### II.14.3 The fiber-component scalar has no background [D]

Since $\mathcal{F}_{\rm eff} = \mathcal{F}_B + \phi F_{\rm Hopf}$, a constant $\phi_0$ would make every mass an *electromagnetic* magnetic monopole of charge $\phi_0M/m_{\rm unit}$. No magnetic monopoles are observed, so $\phi_0 = 0$. The scalar survives only as a fluctuation, coupling photons to the odd-sector field through $\phi\,F_{\rm Hopf}$ — a new but suppressed interaction. (This is the Wheeler charge-without-charge option of Law III, and observation switches it off.)

### II.14.4 Which fields see the fiber: the distinct-allowable sector [D/T]

The Hopf $U(1)$ at a point is rotation about the *radial axis from the mass* — the shells are the conjugacy classes of §I.5. **Hopf charge is angular momentum about that axis.** Spin-1/2 matter carries it intrinsically: the fiber *is* the spinor phase, and a fermion is Hopf-charged by construction. A photon carries it through its **helicity** when propagating radially: $n = \pm1$ for the two circular polarizations.

For a field of Hopf charge $n$, two paths from $p$ to $q$ that begin at different points of the second-order fiber and together enclose odd-mass $m_-$ acquire the relative phase — and they remain **coherent**: a definite phase is interference, not decoherence, and it becomes effective decoherence only when $m_-\gg m_{\rm unit}$ randomizes it. This is a consequence of the path integral on a bundle, not an additional quantum postulate; the only non-deducible input is *which* fields carry $n$ —

$$\Delta = n\Big[\frac{\Omega_{\rm enc}}{2} + \frac{2\pi\,m_-}{m_{\rm unit}}\Big]$$

The first term is the Hopf part of the holonomy — half the enclosed solid angle. For a **fermion** this is exact: the fiber *is* its spinor phase, and transport around a loop on a shell gives the spin-1/2 Berry phase $\Omega/2$ **[T]**. For a **photon** the identification of Hopf charge with helicity is a proposal **[S]**: it has the *form* of the known Rytov–Vladimirskii–Berry spin-redirection phase (a geometric phase proportional to a solid angle) but on the spatial shell rather than the sphere of propagation directions, and with the spin-1/2 coefficient rather than the spin-1 one. It is a structural consistency, not a coefficient-level reproduction, and it is recorded as such. The second term is new.

So the distinctness principle acts on light as follows: **two photon paths beginning at different points of the second-order fiber are distinct exactly when the photon carries Hopf charge** — helicity, for radial propagation — and indistinguishable for the Hopf-neutral mode. The first-order photon never sees the fiber; its circularly polarized components do. Spin-1 is the distinct-disallowed projection, as the program's spin reading says, and helicity is the spinorial residue that survives it.

### II.14.5 The new effect, and the first bound on $m_{\rm unit}$ [D]

Helicity $\pm1$ acquire opposite odd-mass phases, so linear polarization — their superposition — is **rotated** between two paths that enclose odd-mass:

$$\Delta\theta = \frac{2\pi\,m_-}{m_{\rm unit}}$$

a polarization rotation sourced by the antipodally odd part of the enclosed mass, with no counterpart in general relativity for a static, non-rotating mass (the gravitational Faraday effect there requires frame-dragging). The cleanest test is a gravitationally lensed polarized source: its two images enclose the lens, so their polarization angles should differ by $2\pi M_{\rm lens}/m_{\rm unit}$ (the lens's antipodal image being uncorrelated, $m_-\approx M_{\rm lens}$). Lensed-quasar images agree in polarization to a few degrees. Hence:

| lens | bound | $m_{\rm unit}$ |
|:--|:--|:--|
| galaxy, $10^{12}M_\odot$ | $\lvert\Delta\theta\rvert < 3°$ | $> 1\times10^{14}M_\odot$ |
| galaxy, $10^{12}M_\odot$ | $\lvert\Delta\theta\rvert < 0.5°$ | $> 7\times10^{14}M_\odot$ |
| cluster, $10^{15}M_\odot$ | $\lvert\Delta\theta\rvert < 3°$ | $> 1\times10^{17}M_\odot$ |
| cluster, $10^{15}M_\odot$ | $\lvert\Delta\theta\rvert < 0.5°$ | $> 7\times10^{17}M_\odot$ |

**$m_{\rm unit}$ exceeds $10^{14}$–$10^{17}M_\odot$: galactic to cosmological** — *conditional on the helicity identification of §II.14.4* **[S→D]**; a fermion-interferometric version of the same bound would be unconditional but has no comparable data. The requirement of §II.8 that the twist be negligible at Earth scale — which needed $m_{\rm unit}$ large — is now a measured statement rather than a hope. This also bears on the quantization fork (§II.9): a $U(1)$ fiber with masses quantized in $m_{\rm unit}\gtrsim10^{14}M_\odot$ is untenable (stars exist), which pushes toward the $\mathbb{R}$ fiber, or toward a $U(1)$ whose quantum is not a mass quantization. The fork remains open, but one of its tines has been bent.

### II.14.6 Summary of the electromagnetic law at second order

> ### ◆ ELECTROMAGNETISM, VERSION 3
> - $\mathcal{F}$ lives on the cover $S^3$ as before; the photon is a **section** over the base with Hopf charge $n$, not a field in $E$.
> - Effective field strength $\mathcal{F}_{\rm eff} = \mathcal{F}_B + \phi F_{\rm Hopf}$, with $\phi_0 = 0$.
> - The $n = 0$ photon is the first-order photon exactly.
> - Hopf charge $=$ angular momentum about the radial axis; helicity for radial photons; intrinsic for fermions.
> - Two-path phase $\Delta = n[\Omega_{\rm enc}/2 + 2\pi m_-/m_{\rm unit}]$: the known spin-redirection phase plus an odd-mass term.
> - Prediction: polarization rotation $2\pi m_-/m_{\rm unit}$ between lensed images. Bound: $m_{\rm unit}\gtrsim10^{14}$–$10^{17}M_\odot$.


## II.15 The geometry of $E$: invariants and Easter eggs

*$E$ was built, not chosen. What it turns out to be is worth recording in full.* Set $\ell = 1$; $g_E = d\chi^2 + 4\sin^2\chi\,g_{S^3}$, a warped product over the unit 3-sphere.

**Curvature [V].** By the warped-product formulas of §I.4 with $f = 2\sin\chi$:

| quantity | value |
|:--|:--|
| radial Ricci $\mathrm{Ric}_{\chi\chi}$ | $3$ — *constant, and equal to round $S^4$'s* |
| shell Ricci (orthonormal eigenvalue) | $\tfrac32 - \tfrac32\cot^2\chi = -\dfrac{3\cos2\chi}{2\sin^2\chi}$ |
| scalar curvature $R$ | $\tfrac{15}{2} - \tfrac92\cot^2\chi$ |
| Einstein $G_{\chi\chi}$, $G_{\rm shell}$ | $-\tfrac34 + \tfrac94\cot^2\chi$, $\;\;-\tfrac94 + \tfrac34\cot^2\chi$ |
| $\mathrm{Ric}_{ab}\mathrm{Ric}^{ab}$ | $\tfrac{63}{4} - \tfrac{27}{2}\cot^2\chi + \tfrac{27}{4}\cot^4\chi$ |
| Weyl | $0$ (§II.13.4) |

$E$ is not Einstein — the shell Ricci is not proportional to the radial one — but it is **conformally Einstein**, being conformal to round $S^4$. Its scalar curvature is $7.5$ at the equator, changes sign on the shells $\sin^2\chi = 3/8$ ($37.8°$ and $142.2°$ from the mass), and diverges to $-\infty$ at the poles: the monopole singularities read as curvature.

**Easter eggs [V].**
1. **Volume.** $\mathrm{vol}(E) = 64\pi^2/3$, exactly *half* the round $S^4$ of radius 2.
2. **The equator carries a round 3-sphere of radius 2** — twice the spatial sphere's radius. The Hopf 3-sphere over the equator is the largest and roundest slice.
3. **Fiber length** $4\pi\sin\chi$, maximal $4\pi$ at the equator: twice a spatial great circle.
4. **The radial direction thinks it is on round $S^4$** ($\mathrm{Ric}_{\chi\chi} = 3$ everywhere); only the shells know otherwise.
5. **Isometry.** $g_E$ has the full $SO(4)$ of the round $S^3$ factor; the Hopf *choice* breaks it to $SU(2)\times U(1)$. The symmetry the fibration breaks is the symmetry the axis label (§II.2b) is a coordinate on.
6. **Two circle fibers coexist.** The topological $S^1_u$ of the first order (winding, dilaton, the fiber-escape identity) and the geometric $S^1_{\rm Hopf}$ of the second (spinor phase, monopoles). **Electric charge escapes along $S^1_u$; the second-order monopole charge lives on $S^1_{\rm Hopf}$.** The two fibers are the model's electric/magnetic split, realized as two different circles — one nowhere-degenerate and quantized by winding, one degenerating at every mass and quantized by Chern number.
7. **Conformal to $S^4$ with the mass and twin removed**, Poincaré–Hopf index $+1$ at each (§II.13.1).

## II.16 The Lagrangian, and the second order as kinematics

*The full action of version 3, and the honest status of each term.*

**The full space.** With both fibers, $\mathcal{E} = \mathbb{R}_t\times S^1_u\times E$, six-dimensional, with

$$g_6 = g_4 + \psi^2\,du^2 + L_2^2\,(d\psi_2 + \alpha)^2, \qquad L_2 = 4\pi\ell\sin\chi$$

**The two reductions are not alike.** Reducing on $S^1_u$ is the first-order theory: Law I with the dilaton $\psi$, stabilized by the winding — dynamical, and done. Reducing on $S^1_{\rm Hopf}$ *as Kaluza–Klein* would produce a gauge field $\alpha$ with kinetic term $-\tfrac14L_2^2F_{\rm Hopf}^2$ and a **second radion** $L_2$. But $L_2 = 4\pi\ell\sin\chi$ is fixed by the Hopf geometry; honest KK would make it dynamical and demand a second stabilization, and would make $F_{\rm Hopf}$ a field to be solved for rather than a record of where the masses are. The placement principle (§II.13.6) says the opposite: **$E$ is a kinematic consequence of the placement, and the second order has no independent Lagrangian** **[D]**. The Hopf connection is a functional of the matter configuration, $\alpha = \alpha[\text{placement}]$, not a field with its own action.

**The action of version 3.**

$$S = \underbrace{\int_{M_5}\!\sqrt{-g_5}\,\frac{R_5 - 2\Lambda_5}{16\pi G_5}}_{\text{gravity + dilaton}} \;+\; \underbrace{\int_{M_5}\!\sqrt{-g_5}\,\Big(-\tfrac12(\nabla f)^2\Big)}_{\text{winding}} \;+\; \underbrace{\int_{\rm cover}\!\sqrt{-g_4}\,\Big(-\tfrac14\mathcal{F}_{\mu\nu}\mathcal{F}^{\mu\nu}\Big)}_{\text{EM}} \;+\; \underbrace{\int_{\rm cover}\!\sqrt{-g_4}\,\bar\Psi\big(i\gamma^\mu D_\mu - m\big)\Psi}_{\text{matter}}$$

with the one modification the second order makes: the covariant derivative on the cover is

$$D_\mu = \partial_\mu - ie\,\mathcal{A}_\mu - in\,\alpha_\mu[\text{placement}]$$

Matter and (under §II.14.4's identification) helicity-carrying light couple to the Hopf connection as a **background determined by where matter is**, with integer Hopf charge $n$. Gravity reads the placement's even face through Law I; the holonomy of $\alpha$ reads its odd face. The action is self-referential in the way gravity always is — matter determines the structure it moves in — with one difference: $\alpha$ has no kinetic term, so it responds to the placement *instantaneously*. That is the two-speed structure of §I.4 appearing in the Lagrangian as the absence of a term.

**The fork, recorded.** One may instead promote $\alpha$ to a dynamical KK gauge field with coupling $g_2$ and let the Hopf-charge current source it. Then $F_{\rm Hopf}$ is solved for, Hopf charge is a new quantum number rather than a function of mass and sheet, the odd-mass reading of Law III is lost unless charge correlates with sheet, and $g_2$ enters black-hole extremality (§II.10). This is a different theory — one in which the placement principle fails — and it is the theory §II.10's $g_2$ belongs to. Version 3 as written is the kinematic one.

**The EFE-family constraint as a Lagrangian.** The family of bases is the family of placements (§II.13.5). Classically, the action above selects one member: the placement that appears as the source in Law I. There is no separate "family constraint" — the Einstein equation on the selected base *is* the equation of motion of the gravitational term with the actual matter as source. Quantum mechanically, the path integral over matter configurations is a sum over the family: every placement contributes, weighted by $e^{iS}$, and the two-path phases of §II.14 are the interference between placements that differ by where a single quantum sits on the fiber. **Classical: the Lagrangian picks the family element. Quantum: it sums them.** That is the cleanest statement of what the family is for.


## II.17 Recentering

*The transformation that moves the fibration — first seen in §II.13.5 as the motion through the family of bases — is a definite geometric object with a definite group structure. This section defines it, names it, and records what it does at each level of the theory.*

### II.17.1 Definition and group structure [T]

For one mass, the root is $E\sim S^4$ with isometry group $O(5)$. The Hopf structure on $E$ is fixed by a **pole pair** $\{p,\bar p\}$ — the mass and its twin — together with a Hopf axis on the latitude 3-spheres. The stabilizers:

| structure fixed | stabilizer | dimension |
|:--|:--|:--|
| nothing | $O(5)$ | $10$ |
| the pole pair | $SO(4)$ — the isometry group of the spatial $S^3$ | $6$ |
| pole pair and Hopf axis | $SU(2)_L\times U(1)_R$ | $4$ |

So the family of Hopf structures is $O(5)/(SU(2)_L\times U(1)_R)$, of dimension $6 = 4 + 2$: four for *where the mass is*, two for the axis label of §II.2b. Stripping the relabelling, the physical family is the orbit of pole pairs, $O(5)/SO(4)$.

> **Definition.** A **recentering** is an element of $O(5)$ acting on the conformal root by moving the pole pair. Everything the fibration is built on — the concentric shells (conjugacy classes), the Hopf circles, the monopole and anti-monopole, the gravitational well and its twin — is defined relative to the pole pair, and moves with it.

### II.17.2 What it does at each order [D]

**Second order.** It moves the center of the concentric shells — the mass — and carries the twin, the well, and the monopole with it by the same rotation. This is the lockstep of §II.13.5, named: recentering is the operation under which the even and odd faces of a placement move together.

**First order.** It moves the pole pair $\{0,\infty\}$ of the radial fibration — that is, it moves the **origin of the projective structure**. "Reference point as root" (§II.2b) is thereby a group action: the reference point is the center of the fibration, and recentering is what moves it.

At both orders the fibration has a center and recentering moves it. Hence the name.

### II.17.3 The Kelvin transform is a recentering [V]

The Kelvin transform $x\mapsto -x/|x|^2$ on $\mathbb{R}^4$, pushed to $S^4$ by stereographic projection, is exactly the antipodal map of $S^4$ — the element $-1\in O(5)$ — verified pointwise. So the role democracy of §I.4 (any node as chart-infinity, $r\to1/r$) is the *special* recentering that exchanges the two poles; general recentering moves them anywhere. The first-order Kelvin duality was the $\mathbb{Z}_2$ shadow of a four-dimensional orbit, seen before the root was known.

**Orientation and the twin's sign.** $\det(-1) = -1$ in five dimensions: the pole-swap is orientation-reversing on the root. Orientation reversal flips Chern numbers. So "the twin carries opposite second-order charge" (§II.3) and "the recentering that reaches the twin is a reflection" are the same fact. The anti-monopole is the parity of the transformation that gets you there.

### II.17.4 Conformal, and when isometric [D]

$E$'s metric is $g_E = \Omega_p^2\,g_{S^4}$ — conformal to round, not round, with the factor centered on $p$. An element $\phi\in O(5)$ is an isometry of $g_{S^4}$, hence acts on $g_E$ as

$$\phi^*g_E = \Big(\frac{\Omega_p\circ\phi}{\Omega_p}\Big)^2\,g_E$$

**Recentering is a conformal transformation of the total space**, with a computable factor: the ratio of the conformal factor seen from the new center to that seen from the old. It is a genuine isometry of $g_E$ only when that ratio is $1$ — for the $SO(4)$ fixing the pole pair, and for the Kelvin pole-swap (since $\Omega_{\bar p} = \Omega_p$ by the $p\leftrightarrow\bar p$ symmetry). Every other recentering is conformal but not isometric.

A second, equally true reading: as a map from $E$ to the recentered space $E'$ (Hopf-over-shells about $q$, with metric $\Omega_q^2 g_{S^4}$), recentering is an **isometry** — $\phi^*g_{E'} = g_E$. *Conformal on a fixed $E$; isometric between $E$ and $E'$.* Which one you see depends on whether the metric is carried along or left behind.

### II.17.5 Action on the Ricci tensor of $E$ [V/D]

Two readings, matching the two above.

**Passive (metric carried along).** $\mathrm{Ric}[g_{E'}] = (\phi^{-1})^*\mathrm{Ric}[g_E]$: the curvature pattern of §II.15 — radial Ricci $3$, shell Ricci $-3\cos2\chi/2\sin^2\chi$, $R = 0$ on the shells at $37.8°$ and $142.2°$ — is *translated* to be centered on the new mass. At a fixed point $x$ the Ricci tensor changes because $x$'s distance from the center changed: a point at $\chi = 1.0$ has $R = 5.64$; move the pole $0.2$ toward it and $R(x) = R(0.8) = 3.26$ **[V]**.

**Active (metric left behind).** With $\phi^*g_E = e^{2\omega}g_E$ and $\omega = \ln[(\Omega_p\circ\phi)/\Omega_p]$, the four-dimensional conformal law gives

$$\mathrm{Ric}[e^{2\omega}g] = \mathrm{Ric}[g] - 2\nabla\nabla\omega - (\Box\omega)\,g + 2\,d\omega\otimes d\omega - 2\,|d\omega|^2 g$$

For the Kelvin pole-swap $\omega = 0$ and Ricci is invariant; for a general recentering the correction is nonzero and is the difference between the two centers' curvature patterns.

**Invariants.** The Weyl tensor stays zero — conformal flatness is $O(5)$-invariant. The scalar curvature, $\mathrm{Ric}_{ab}\mathrm{Ric}^{ab}$, and the $R = 0$ shells are the same functions of distance-from-center, recentered. The Poincaré–Hopf indices $(+1,+1)$ move with the poles. The radial Ricci is $3$ from whichever pole is the center.

### II.17.6 When it is a symmetry and when it is a change [D]

With one mass the root is conformally flat, $O(5)$ acts, and recentering is a *symmetry*: every member of the family is the same universe seen from a different center. With many masses the root is not conformally flat (§II.13.4), $O(5)$ is not even conformal, and recentering is a *change of placement* — no transformation law relates $\mathrm{Ric}[E']$ to $\mathrm{Ric}[E]$; both $E'$ and its now-nonzero Weyl tensor are recomputed from the new Hopf-over-shells superposition. The placement principle is the only law that survives: base Ricci (from $T_+$) and $E$-Weyl (from $J_-$) still move together.

The symmetry chain of the vacuum, read as successive breakings:

$$O(5)\;\xrightarrow{\;\text{one mass}\;}\;SO(4)\;\xrightarrow{\;\text{Hopf axis}\;}\;SU(2)\times U(1)\;\xrightarrow{\;\text{many masses}\;}\;\text{trivial}$$

The first arrow is worth pausing on: **the spatial 3-sphere's isometry group $SO(4)$ is what remains of the root's $O(5)$ after a single mass is placed.** The symmetries of space are the symmetries of the arena that one mass failed to break.

### II.17.7 Where it bites: the compactification [D]

Recentering is a symmetry of $E$, but the first-order theory compactifies its root by the dilation $u\to u+\ln\lambda$, and only the $SO(4)$ fixing $\{0,\infty\}$ preserves that quotient. A recentering that moves the origin *off* the spatial 3-sphere — the extra direction of $S^4$ — breaks the compactification. This is open problem 7 as a group fact: **the first order admits only $SO(4)$ of the $O(5)$ recenterings; the second order admits all of them.** Whether the first order should be un-compactified or the second order quotiented is the question that decides which recenterings are physical.

## II.18 Laws and axioms, version 3

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
> - **A11.** In version 3 as written, $\alpha$ is **kinematic** — a functional of the placement with no action of its own (§II.16); matter couples to it through $D_\mu = \partial_\mu - ie\mathcal{A}_\mu - in\alpha_\mu$. Promoting it to a dynamical KK gauge field with coupling $g_2$ is the recorded fork, in which black holes acquire $P_{\rm eff} = g_2M/m_{\rm unit}$ (§II.10).

> ### ◆ ELECTROMAGNETISM
> - **A12.** $d\mathcal{F} = 0$, $d\star_5\mathcal{F} = \star_5\mathcal{J}$ on the cover; the photon is a section over the base with Hopf charge $n$ (§II.14), $\mathcal{F}_{\rm eff} = \mathcal{F}_B + \phi F_{\rm Hopf}$ with $\phi_0 = 0$.

> ### ▣ DERIVED
> - **D1.** $\Lambda = 1/\ell^2$ (cone). **D2.** No endpoints (unsourced $f$). **D3.** The static twin is the quotient. **D4.** Mach relation, $k$-dial. **D5.** $\gamma = 1$ (stabilization). **D6 (new).** The partition: $T_+$ to gravity, $J_-$ to the second-order fiber. **D7 (new).** Twin signs: $(M,Q,g)\to(M,-Q,-g)$. **D8 (new).** The seed is $SU(2)\to SO(3)$. **D9 (new).** $E$ is conformally $S^4\setminus\{p,\bar p\}$; the fiber partition is $E$'s Weyl tensor; the placement principle (§II.13.6). **D10 (new).** Recentering: $O(5)$ on the root, moving the pole pair; conformal on $E$, isometric $E\to E'$; Kelvin is the pole-swap; $SO(4)$ of space is its residue after one mass (§II.17).

**Free parameters of version 3.** The winding integer $w$ · one scale $|\Lambda_5|$ (equivalently $\psi_0$) · the quotient $\Gamma$ · the equation of state · **and, new: $m_{\rm unit}$ (mass per flux quantum) and $g_2$ (whether and how strongly $F$ gravitates).** Two new constants, both bounded by observation in principle and neither yet bounded in practice.

---

# PART III — STATUS

## III.1 The ledger of version 3

| result | tag |
|:--|:--|
| $S^3\cong SU(2)$, $\mathbb{RP}^3\cong SO(3)$, antipodal $= -1$: the seed is spin-1/2 vs spin-1; space stays 3-D | **[V]** |
| concentric shells about a mass = conjugacy classes of $SU(2)$; equator = rotations by $\pi$; antipode $= -1$ | **[V]** |
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
| $E$ conformal to $S^4\setminus\{p,\bar p\}$; Poincaré–Hopf obstruction = the two monopoles | **[V/T]** |
| first- and second-order total spaces share one conformal root, fibered by circles through vs. avoiding the poles | **[D]** |
| family of bases $= \{(p,q)\}\times S^2_{\rm axis}$; original base is $(1,1)$ | **[T]** |
| Weyl$^2(E) = 0$ for Hopf, $= 4\epsilon^2(16-13\sin^2\theta)/3\sin^4\chi$ for a moved partition: the fiber partition is $E$'s Weyl | **[V]** |
| Ricci–Weyl realized one level up: base Ricci $\leftarrow T_+$, $E$-Weyl $\leftarrow J_-$ | **[D]** |
| the placement principle: the placement is the fibration; even/odd faces move in lockstep | **[D]** |
| $\mathcal{F}_{\rm eff} = \mathcal{F}_B + \phi F_{\rm Hopf}$ on the Hopf bundle | **[T/V]** |
| photon cannot propagate in the $\sim100$ kpc fiber ($1/r^3$); it is a section; $n=0$ is the first-order photon | **[D]** |
| $\phi_0 = 0$, else every mass is an EM monopole | **[D]** |
| Hopf charge = angular momentum about the radial axis; helicity for radial photons; the Hopf holonomy reproduces the spin-redirection phase | **[D/T]** |
| polarization rotation $2\pi m_-/m_{\rm unit}$ between lensed images; $m_{\rm unit}\gtrsim10^{14}$–$10^{17}M_\odot$ | **[S→D]** (conditional on helicity = Hopf charge) |
| $E$: $\mathrm{Ric}_{\chi\chi} = 3$, $R = \tfrac{15}{2} - \tfrac92\cot^2\chi$, $R = 0$ at $\sin^2\chi = 3/8$; conformally Einstein; vol $= \tfrac12$ round $S^4$ | **[V]** |
| two fibers: electric charge on $S^1_u$, monopole charge on $S^1_{\rm Hopf}$ | **[D]** |
| second order is kinematic: $\alpha = \alpha[\text{placement}]$, no independent action; the two-speed structure is the absence of a kinetic term | **[D]** |
| classical action selects the family element; the path integral sums the family | **[D]** |
| recentering $= O(5)$ moving the pole pair; family $O(5)/(SU(2)_L\times U(1)_R)$, physical part $O(5)/SO(4)$ | **[T]** |
| Kelvin transform $=$ antipodal map of $S^4$ $= -1\in O(5)$, orientation-reversing; hence the twin's opposite charge | **[V/D]** |
| recentering is conformal on $E$ ($\phi^*g_E = (\Omega_p\circ\phi/\Omega_p)^2 g_E$), isometric $E\to E'$; Ricci translated | **[D/V]** |
| $SO(4)$ of the spatial sphere $=$ residue of the root's $O(5)$ after one mass | **[D]** |

## III.2 Open problems of version 3

1. **The quantization fork** (§II.9) — $U(1)$ with quantized masses, or $\mathbb{R}$ with continuous holonomy. The first decision the version owes; the $m_{\rm unit}$ bound of §II.14.5 makes mass-quantization in $m_{\rm unit}$ untenable and tilts it toward $\mathbb{R}$, or toward a $U(1)$ whose quantum is not a mass.
2. **Does $F$ gravitate, and how strongly?** — $g_2$, and the bound on $g_2/m_{\rm unit}$ from the existence of near-Schwarzschild black holes.
3. **The spin-2 fork** (§II.7) — whether the six odd stress components need a second metric, and whether that collapses the theory to GR on the cover.
4. **What sets $m_{\rm unit}$** — now bounded below at $10^{14}$–$10^{17}M_\odot$ by lensed-image polarization (§II.14.5); what fixes it from the theory's side is open.
5. **The twin's marking** — feature or cost; a deliberate decision about the seed's character.
6. **The third order** — Hopf tower or spin-2 second metric; *deliberately held open* pending more probing.
7. **The compactification mismatch** — the first-order theory quotients its conformal root by the dilation; $E$ does not. Whether $E$ admits a compatible quotient, and what it would mean, is open (§II.13.2).
8. **Inherited from version 2** — the AdS uplift ($10^{60}$, the single blocking problem); a law for $\ell$ in the Tully–Fisher sector; the rise beyond the equator; the literature review before anything is called new.

## III.3 The next three moves

1. **Measure the polarization difference between lensed images** — the cleanest test of the second-order structure, already bounding $m_{\rm unit}$; a dedicated measurement on a high-signal lensed quasar or FRB would tighten it by orders of magnitude.
2. **Bound $g_2/m_{\rm unit}$ from black-hole observations.** The extremality shift $M^2 = Q^2 + P_{\rm eff}^2$ is a concrete prediction; near-Schwarzschild ringdowns and shadow measurements constrain it.
3. **Decide the quantization fork by computing both.** Take a smooth distribution, build the $\mathbb{R}$-connection and the $U(1)$-connection with the nearest integer flux, and see which one produces consistent holonomy for the two-path amplitude.
4. **Write the spin-2 version and check whether it is GR.** If a second metric on the cover sourced by $T_-$ reproduces Einstein on $S^3$, the $U(1)$ choice is what keeps the theory distinct, and that should be known before anything else is built on it.

---

## Reference card, version 3

| topic | statement |
|:--|:--|
| **spin identification** | $S^3 = SU(2)$, $\mathbb{RP}^3 = SO(3)$, antipodal $= -1$; the seed is the spinor sign; space stays 3-D |
| **shells** | conjugacy classes of $SU(2)$, mass at the identity; distance = rotation angle |
| **dimensions** | space 3; base 3; shell 2; Hopf lift of a shell 3; $E$ 4 |
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
| **conformal root** | $E\sim S^4\setminus\{p,\bar p\}$; $g_E = \ell^2d\chi^2 + 4\ell^2\sin^2\chi\,g_{S^3}$; $\tan(\chi'/2) = \sqrt{\tan(\chi/2)}$ |
| **Weyl of $E$** | $=$ deviation of the fiber partition from Hopf; sourced by $J_-$ |
| **family of bases** | $\{(p,q)\}\times S^2_{\rm axis}$; the $SO(5)$-orbit of point-pairs for one mass |
| **placement principle** | the placement is the fibration; Ricci on the base $\leftarrow T_+$, Weyl on $E$ $\leftarrow J_-$, in lockstep |
| **EM at second order** | $\mathcal{F}_{\rm eff} = \mathcal{F}_B + \phi F_{\rm Hopf}$; photon a section, $n=0$ first-order exactly; $\phi_0 = 0$ |
| **who sees the fiber** | Hopf charge = $J$ about the radial axis; fermions intrinsically; photon helicity radially |
| **two-path phase** | $n[\Omega_{\rm enc}/2 + 2\pi m_-/m_{\rm unit}]$: spin-redirection phase (known) + odd-mass term (new) |
| **$m_{\rm unit}$ bound** | polarization of lensed images: $m_{\rm unit} > 10^{14}$–$10^{17}M_\odot$ (conditional on helicity identification) |
| **$E$ invariants** | $\mathrm{Ric}_{\chi\chi} = 3$; $R = \tfrac{15}{2} - \tfrac92\cot^2\chi$; Weyl $0$; vol $64\pi^2/3$; isometry $SO(4)\to SU(2)\times U(1)$ |
| **two fibers** | $S^1_u$: winding, dilaton, electric escape; $S^1_{\rm Hopf}$: spinor phase, monopoles |
| **action** | 5D EH + winding + EM + Dirac on the cover, with $D = \partial - ie\mathcal{A} - in\alpha[\text{placement}]$; $\alpha$ kinematic |
| **recentering** | $O(5)$ on the root; moves mass, twin, well, monopole together; conformal on $E$; Kelvin $= -1$ |
| **symmetry chain** | $O(5)\to SO(4)\to SU(2)\times U(1)\to$ trivial (root, one mass, Hopf axis, many masses) |
| **does not** | shift frequency (static theorem); keep the twin unmarked |
