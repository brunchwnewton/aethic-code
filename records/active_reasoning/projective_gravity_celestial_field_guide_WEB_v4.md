# Projective Gravity — Version 4

### The Contact Formulation: a field guide

> **What this version is.** Version 3 built the second-order structure as a $U(1)$-bundle over the spatial 3-sphere, Hopf-lifted shell by shell about every mass. It delivered the spin identification, the partition theorem, and an observational bound — and it owed two debts it could not pay: a second fiber modulus with no joint stabilization, and a quantization fork it could not decide. Version 4 pays both by relocating the second-order structure from a bundle *over* the 3-sphere to a **contact structure *on* it** — the Hopf fibration of $S^3 = SU(2)$ itself, deformed by matter. The first-order theory is unchanged. The seed is unchanged. What is new: **Law I is, in the sector where it can be, the equation for the Hopf fiber length.** The Einstein constraint on the base acts on the fibers directly, and the twin appears as fiber geometry before it appears as a well.
>
> **Tags.** **[V]** verified · **[M]** measured numerically · **[T]** cited theorem · **[D]** derived · **[S]** sketch · **[O]** open · **[R]** retired.
>
> **Conventions.** $G = c = 1$ unless restored; $\ell$ the spatial 3-sphere radius; $T_\pm(\hat n) = T(\hat n)\pm T(-\hat n)$; $\alpha_H$ the standard Hopf contact form on $S^3$; $\phi$ the Lichnerowicz conformal factor, $g_3 = \phi^4 g_{S^3}$.
>
> **Reading guide.** What was retired and why: §II.1. The arena and its complex structure: §II.2. Law I as the fiber equation: §II.4 — the version's central result. The two checks that had to pass: §II.5. The partition in v4: §II.6. What changed for electromagnetism: §II.8. Non-privileging and the mirror law: §II.12. The polarization check and the birefringence dichotomy: §II.13. Laws: §II.14. Status: Part III.

---

# PART I — THE FIRST-ORDER THEORY (unchanged)

## I.1 Arena, seed, and laws

$M_5 = \mathbb{R}_t\times S^1_u\times S^3$; $\partial_u$ is the radial direction of $\mathbb{R}^4\setminus\{0\}$ in polar form, nowhere vanishing because the manifold is a product **[T]**. The scaling group is $\mathbb{R}^* = \mathbb{R}^+\times\mathbb{Z}_2$, so the base is $\mathbb{RP}^3$ and the fiber over $[\hat n]$ is disconnected — the $u$-circle at $+\hat n$ and at $-\hat n$ — with the projective postulate integrating over both **[D]**.

> **The seed.** Matter at $(u_0,+\hat n)$ sources the base at $[\hat n]$, whose lift has wells at both $\pm\hat n$; nothing is at $-\hat n$. Blindness, not crossing.

$S^3\cong SU(2)$, $\mathbb{RP}^3\cong SO(3)$, the antipodal map $= -1$: **gravity lives on the rotation group and cannot see the sign of a spinor; light lives on the spin group and can** **[V]**. Space is three-dimensional.

> ### ◆ LAW I — GRAVITY
> $$\ell^2R^{(4)}_{\mu\nu} = \ell^2\psi^{-1}\nabla_\mu\nabla_\nu\psi + 2\Big(\tau_{\mu\nu} - \tfrac13\tau g_{\mu\nu}\Big), \qquad \tau = S/\bar\epsilon, \quad S = T_+$$

> ### ◆ LAW II — THE FIRST-ORDER FIBRATION
> $$\Box f = 0, \qquad \oint df = \ln\lambda, \qquad f = wu$$

## I.2 Theorems carried forward

Terminus theorem **[M/D]**; cone theorem, $\Lambda = 1/\ell^2$ **[V]**; **twin theorem** — the static operator is $\Delta_{S^3}+3$, $u = \Phi\sin\chi$ gives $u''+4u = 0$, same-sign poles at both ends, $\ker(\Delta+3)$ = dipoles, and the $\mathbb{RP}^3$ quotient satisfies zero-dipole identically **[V]**; Mach relation $GM_{\rm tot}/c^2\ell = \pi/2$ as a consistency relation **[V]**; $k$-dial **[V]**; **winding stabilization** $\psi_0^2 = 3w^2/4|\Lambda_5|$, $m_\psi\psi_0 = w$, restoring PPN $\gamma$ from $\tfrac12$ to $1$ — the result that lets the theory survive the solar system **[V/D]**; Bianchi closure and descent **[V/D]**; the two-speed cover **[D]**; the Tully–Fisher square root with $a_0 = 4\pi G\Sigma_{\rm mean}$ **[D/V]**; the $r = 1/\sqrt2$ signpost **[D]**.

---

# PART II — THE SECOND ORDER AS A CONTACT STRUCTURE

## II.1 What was retired, and the trade

**The bundle formulation (v3) is retired [R]**, for two reasons that no patch resolved.

*The moduli obstruction.* Hopf-lifting shells about a mass gives a fiber of length $L_2 = 4\pi\ell\sin\chi$. Treated dynamically it is a second radion whose Einstein-frame potential $2\Lambda_5/L + L^3|F|^2/4$ needs $\Lambda_5>0$, while the winding stabilization of $\psi$ needs $\Lambda_5<0$; the joint potential $\Lambda_6/\psi L + w^2/2\psi^3L + \psi L^3F^2/4$ has *no critical point* — its conditions reduce to $A = -B$ with both positive **[V]**. Treated kinematically the fiber length is undetermined inside matter.

*The quantization fork.* A $U(1)$ bundle needs integer flux; a continuous $\rho_-$ does not supply it; and the one bound available, $m_{\rm unit}\gtrsim10^{14}M_\odot$, made mass quantization in $m_{\rm unit}$ untenable.

**The trade.** The contact formulation removes both — and the two things it costs are the Dirac monopoles and the *enclosed-mass law* for two-path phases. The twin is no longer a topological anti-charge but a region of negative deformation; the phase between paths around a mass is a shape-dependent functional, not $2\pi m_-/m_{\rm unit}$. Version 4 accepts that trade with eyes open: the quantization was, on reflection, excessive structure, and one stabilized modulus is worth more than a quantized charge whose quantum was already forced to be cosmological.

## II.2 The arena and its complex structure

The spatial total space $S^1_u\times S^3$ carries two commuting circle actions — $U(1)_u$ on the $u$-circle and $U(1)_{\rm Hopf}$ by right-multiplication on $S^3 = SU(2)$ — a $T^2$-action with quotient $S^2$. It is a $T^2$-bundle over $S^2$ with Chern numbers $(0,1)$ **[T]**. And it is the **Hopf surface**, $(\mathbb{C}^2\setminus\{0\})/\langle z\mapsto\lambda z\rangle$: a compact complex surface, elliptically fibered over $\mathbb{CP}^1$, with elliptic fiber of periods $(\ln\lambda,\,2\pi i)$ and modular parameter

$$\tau = \frac{2\pi i}{\ln\lambda}$$

**The $u$-circle is the real period; the Hopf circle is the imaginary period.** They are $\mathrm{Re}\,w$ and $\mathrm{Im}\,w$ of one complex coordinate, and $SL(2,\mathbb{Z})$ exchanges them **[T]**. The stabilized metric $S^3(\ell)\times S^1(\psi_0\ln\lambda)$ is conformally the Hopf surface with $|\tau_{\rm eff}| = 2\pi\ell/\psi_0\ln\lambda\approx3\times10^{25}$: a needle, one period fifty microns and the other fifty kiloparsecs. **The two fibers are the same kind of object; their apparent difference is one modulus far from the self-dual point** **[D]**.

## II.3 The contact structure

The Hopf connection on $S^3$ is a contact form: in Hopf coordinates $\alpha_H = d\psi + \cos\vartheta\,d\varphi$ (up to scale) and $\alpha_H\wedge d\alpha_H = -\sin\vartheta\,d\vartheta\wedge d\varphi\wedge d\psi\neq0$ everywhere **[V]**. Its Reeb field generates the Hopf circles — great circles of the round $S^3$, of length $2\pi\ell$, set by the sphere's radius and **not a modulus**. The contact planes $\ker\alpha_H$ are the distinct-allowable directions of the distinctness principle; their non-integrability is the twist; two contact-tangent paths from $p$ to $q$ end at points differing by $\int d\alpha$ over the enclosed surface — holonomy without a bundle.

> ### ◆ LAW III′ — THE CONTACT STRUCTURE
> The second-order structure is a contact form $\alpha$ on the spatial $S^3$, with vacuum $\alpha_H$, decomposed as
> $$\alpha = \phi^2\,f\,\alpha_H$$
> where $\phi$ is the conformal factor of the 3-metric, determined by Law I from *even* matter, and $f$ is the odd-sector deformation, $f = f[\rho_-]$, with $f = 1$ in vacuum. The Reeb field $R = R_H/\phi^2$ is unit in the physical metric, and the twist density relative to the physical volume is
> $$\frac{\alpha\wedge d\alpha}{\mathrm{vol}_g} = \frac{f^2}{\phi^2}$$

## II.4 Law I acting on the fibers — the central result

*This is what the version is for.* The question was whether the Einstein constraint on the base could be read as a dynamic on the fibers. In the sector where the 3-metric is conformally round — all weak-field statics — the answer is exact.

**The conformally-round sector.** Write $g_3 = \phi^4 g_{S^3}$. The Hamiltonian constraint on the closed static background is the Lichnerowicz equation

$$-8\Delta\phi + 6\phi = \big(16\pi\rho + 2\Lambda\big)\phi^5$$

Linearize about the Einstein-static universe ($\phi = 1+\delta\phi$, $\rho = \bar\rho+\delta\rho$, $\Lambda\ell^2 = 1$): the left side is $6 + (-8\Delta+6)\delta\phi$, the right is $6 + 30\delta\phi + 16\pi\delta\rho$, hence

$$\boxed{\;(\Delta_{S^3}+3)\,\delta\phi = -2\pi\,\delta\rho_+\;}$$

**The conformal factor obeys the twin-theorem operator.** Its Green's function has the same-sign pole at the antipode; $\ker(\Delta+3)$ is the dipoles, so a source must have zero dipole — a lone ball at the pole has dipole $0.169\neq0$ and the equation has *no solution* (the numerical solver returns the kernel mode, $2A\cos\chi$ with $A\sim2000$, as its symptom) **[V]**. Include the twin and the solution is regular and symmetric.

**The fiber length.** The Hopf circles are great circles of the round metric, so in $g_3 = \phi^4g_{S^3}$ their length is

$$\boxed{\;L_H(x) = 2\pi\ell\,\phi(x)^2\;}$$

**The Hopf fiber length *is* the conformal factor, and Law I *is* the equation for it.** For a uniform ball of angular radius $0.35$ at the pole with its twin **[V]**:

| location | $\delta\phi$ | $L_H/2\pi\ell = \phi^2$ | $\Phi = -2\delta\phi$ |
|:--|:--|:--|:--|
| center of the ball | $+0.420$ | $2.017$ | $-0.840$ |
| surface of the ball | $+0.273$ | $1.620$ | $-0.546$ |
| equator | $0$ | $1.000$ | $0$ |
| center of the twin | $+0.420$ | $2.017$ | $-0.840$ |

**The fibers lengthen inside the well** — space is stretched where $\Phi<0$ — and are shortest at the equatorial saddle; and the profile at the *empty* twin is identical to the profile at the mass, to $10^{-11}$. The seed, as fiber geometry: the Hopf fibers cannot tell Earth from its antipode, because $\phi$ cannot, because $(\Delta+3)$ cannot. And $\Phi = -2\delta\phi$ reproduces the two-dimple potential of the Earth–twin solution exactly.

**Beyond the conformally-round sector.** A general 3-metric has six components and the Hopf circles' length is one of them, $g_{\theta\theta}$ in Hopf coordinates, determined by Law I like any other; the statement "Law I determines the fiber length" holds always, and the statement "Law I is *only* the fiber-length equation" holds in the conformally-round sector, which contains every weak-field static configuration. The residual five components carry the rest of gravity — tidal and dynamical content the fiber length alone does not encode. Law I is not reduced to a fiber equation in general; it *acts on the fibers* through $\phi$, and in the sector that matters it is nothing else.

## II.5 The two checks that had to pass

**Can the 3-metric be slaved to the contact form? No — PPN.** The contact metric associated to $(\alpha,J)$ is $g = d\alpha(\cdot,J\cdot) + \alpha\otimes\alpha$: Reeb direction unit, contact planes metrized by $d\alpha$. Near a mass, $\alpha = \Omega\alpha_H$ gives $\Omega\,g_H$ on the planes and $\Omega^2$ along the Reeb direction — an $O(\Phi)$ anisotropy between a *fixed cosmic direction* and its transverse plane, which would make light deflection's $\gamma$ direction-dependent at order one. VLBI and Cassini have $\gamma$ isotropic to $10^{-4}$. **Dead.** The 3-metric stays free; $\alpha$ rides on it; Law I is Einstein on the free metric **[D]**. (This is why §II.4 uses the conformally-round metric with $\alpha = \phi^2\alpha_H$ rather than a contact metric: the former is isotropic, the latter is not.)

**Is there a second radion? No.** Version 4 reduces on the $u$-circle only, giving $\psi$, stabilized. The Hopf circle is *not* reduced on: its length is a metric component, determined by Law I, with no potential of its own. One radion; the joint-stabilization obstruction of v3 does not arise **[D]**. The fiber length varies with matter — §II.4 is exactly how — but as geometry, not as a modulus.

## II.6 The partition in version 4

Gravity reads $T_+$ and produces $\phi$. The odd sector produces $f$. The contact form carries both:

| face | source | carried by | read by |
|:--|:--|:--|:--|
| even | $T_+$ | $\phi$ — the conformal factor, the fiber length | gravity (Law I) |
| odd | $\rho_-$ | $f$ — the contact deformation | light and fermions (holonomy) |

Even matter *lengthens* the fibers ($\phi^2>1$ in wells) and *reduces* the twist density ($1/\phi^2$); odd matter multiplies the twist density by $f^2$. The partition theorem of v3 survives with its two faces relocated: Ricci on the base $\leftarrow T_+$ becomes *fiber length* $\leftarrow T_+$, and $E$-Weyl $\leftarrow J_-$ becomes *contact deformation* $\leftarrow\rho_-$. The placement principle survives in the form **the placement is the deformation**: matter dents a global structure rather than owning a local one.

## II.7 What the odd sector keeps and loses

**Kept.** Distinctness: two contact-tangent paths from $p$ to $q$ that begin at different points along the Reeb direction differ by $\int_\Sigma d\alpha$ and interfere coherently — a phase, not decoherence, until the phase randomizes. The Machian criterion of v3 (distinct = separated by more than a quantum) becomes *distinct = separated by more than the twist scale*, now continuous.

**Lost.** The enclosed-mass law. With $\alpha = \phi^2 f\alpha_H$,

$$\Delta = n\int_\Sigma\big[\phi^2 f\,d\alpha_H + d(\phi^2 f)\wedge\alpha_H\big]$$

depends on the shape of $\Sigma$ and the profile of $\phi^2 f$, not on what $\Sigma$ encloses. A toy bump $f = 1+\epsilon e^{-r^2}$ in a flat patch gives a deformation term over a disc of radius $R$ equal to $\pi\epsilon(R^2+1-e^{R^2})e^{-R^2}$ — two path-pairs around the same bump at different radii acquire different phases **[V]**. Net flux through any closed surface is $\oint_{\partial S}\alpha = 0$ by Stokes: **no monopole, no quantized charge, fibers thread through a mass rather than wrapping it** **[T]**.

**Law III′ is kinematic.** A Chern–Simons action for $\alpha$ would have equation of motion $d\alpha = 0$ in vacuum, which the Hopf form violates; and in three dimensions a $2$-form $d\alpha$ can be sourced only by a $1$-form current, never by a static density. So $f$ is a record of the odd placement, as $\alpha$ was in v3, and the two-speed structure remains the absence of a kinetic term.

## II.8 Electromagnetism in version 4

Everything in the first-order electromagnetic law is unchanged: $\mathcal{F}$ on the cover, $\epsilon = 1/\mu = \psi$, $\epsilon\mu = 1$, light on null geodesics, the Proca tower unexcited by $u$-smeared matter. The photon is a section over the base, not a field propagating along the Hopf circle — the same inverse-square argument as before, now with the circle length $2\pi\ell\phi^2$ rather than $4\pi\ell\sin\chi$.

**Two circles, two quantum numbers.** By non-privileging (§II.12) the photon carries a Kaluza–Klein momentum $p_u$ on the $u$-circle and a Hopf charge $n_H$ on the Hopf circle, exchanged by $SL(2,\mathbb{Z})$:

| | circle | tower spacing $\hbar c/L$ | status |
|:--|:--|:--|:--|
| $p_u$ | $u$, $50\,\mu$m | $4\times10^{-3}$ eV | heavy — frozen out |
| $n_H$ | Hopf, $50$ kpc | $10^{-28}$ eV | ultralight — free |

The needle makes one expensive and the other free. **The photon we see is $p_u = 0$ — the massless zero mode — with $n_H = \pm1$, its helicity along the Reeb direction.** Hopf charge is angular momentum about the Reeb direction, now a *global* axis (the right-$U(1)$ of $SU(2)$) rather than a mass-centered one: fermions carry it intrinsically; a photon carries it through helicity when propagating along the Reeb direction. The two-path phase for Hopf charge $n$ is $n\int_\Sigma d\alpha$ with $\alpha$ as in Law III′. Its Hopf part reproduces, structurally, a geometric phase of the spin-redirection type; its deformation part is new, shape-dependent, and **[S]** pending the helicity identification.

**The bound of v3 must be re-derived.** The polarization-rotation law $2\pi m_-/m_{\rm unit}$ between lensed images was a consequence of the enclosed-mass law and does not survive as stated. Its replacement is a shape-dependent rotation, $\Delta\theta = \int_\Sigma d(\phi^2 f)\wedge\alpha_H + \ldots$, whose magnitude depends on the deformation profile $f[\rho_-]$; a lensed-image polarization comparison still bounds the deformation scale, but the clean integer-free number is gone. **[O]**

## II.9 Recentering in version 4

There is no $S^4$ root and no $O(5)$: the contact structure lives on $S^3$ and its symmetry group is that of the round sphere, $SO(4)$, broken by the Hopf choice to $SU(2)_L\times U(1)_R$. Recentering — moving a mass — is the $SO(4)$ action on placements, which moves the well and its twin together (the twin is at $-\hat n$, and $-1\in U(1)_R$). The Kelvin duality is the element $-1$. The symmetry chain is

$$SO(4)\;\xrightarrow{\;\text{Hopf axis}\;}\;SU(2)\times U(1)\;\xrightarrow{\;\text{matter}\;}\;\text{trivial}$$

and the conformal-root recentering of v3 (§II.17 there) is recorded as a feature of the bundle formulation that v4 does not carry.

## II.10 The elliptic unification and the graviphoton option

From §II.2, the two fibers are the two periods of one elliptic curve and $SL(2,\mathbb{Z})$ exchanges them. Making the $u$-fiber respond to matter as the Hopf fiber does means switching on its connection — the Kaluza–Klein graviphoton $A_\mu$ that A6 switched off. Then both connections are 1-forms on $S^3$, and the natural symmetric action is $U(1)^2$ Chern–Simons with a level matrix on which $SL(2,\mathbb{Z})$ acts **[S]**. Version 4 leaves $A_\mu = 0$ as the vacuum and records the option, with its costs: A6 becomes a solution rather than a theorem, the stabilization must be rechecked with the $w^2A^2$ term, and the graviphoton needs its own coupling bound. **[O]**

## II.11 The Lagrangian of version 4

$$S = \int_{M_5}\!\sqrt{-g_5}\left[\frac{R_5 - 2\Lambda_5}{16\pi G_5} - \frac12(\nabla f)^2\right] + \int_{\rm cover}\!\sqrt{-g_4}\left[-\frac14\mathcal{F}_{\mu\nu}\mathcal{F}^{\mu\nu} + \bar\Psi\big(i\gamma^\mu D_\mu - m\big)\Psi\right]$$

$$D_\mu = \partial_\mu - ie\,\mathcal{A}_\mu - in\,\alpha_\mu, \qquad \alpha = \phi^2 f\,\alpha_H, \quad \phi = \phi[\text{Law I}], \quad f = f[\rho_-]$$

The only change from v3 is the form of $\alpha$: it is no longer a bundle connection over $S^3\setminus\{\text{masses}\}$ but a contact form on $S^3$, with its even part *derived from the gravitational solution* and its odd part a record of the placement. No new field, no new modulus, no new coupling constant. **The theory's parameter ledger is the same as version 2's — $w$, $|\Lambda_5|$, $\Gamma$, the equation of state — plus one function $f[\rho_-]$ whose form is the open content of Law III′.**


## II.12 Non-privileging: the mirror law, and the origin of the projective postulate

*The two fibers are the two periods of one elliptic curve (§II.2). Law I reads matter averaged over the $u$-circle and writes the result on the Hopf fiber's length. Non-privileging demands the converse: a law that reads matter averaged over the Hopf circle and writes it on the $u$-fiber's length. It exists, it is an identity, and it explains where the seed's postulate came from.*

### II.12.1 One 5-D equation, two reductions [T]

Five-dimensional Einstein on $\mathbb{R}_t\times S^1_u\times S^3$, with $S^3$ Hopf-fibered over $S^2$, can be reduced on either circle:

$$\text{on } u:\;\; R_5 = R_4 - 2\psi^{-1}\Box\psi \qquad\qquad \text{on Hopf}:\;\; R_4 = R_3 - 2L_H^{-1}\Box L_H - \tfrac14L_H^2F_{\rm Hopf}^2$$

The first is Law I, with $L_H$ a component of the 3-metric. The second is the **mirror**, with $\psi$ a component of its base $\mathbb{R}_t\times S^1_u\times S^2$. Same equation; which is "gravity" is which circle you reduce on.

### II.12.2 The symmetry is exact on the untwisted torus [V]

For the diagonal 5-metric $-dt^2 + \psi^2du^2 + L^2d\theta^2 + e^{2h}(dx^2+dy^2)$ with $\psi, L, h$ functions on the base, the orthonormal fiber components of the Ricci tensor are

$$R_{uu} = -\frac{e^{-2h}}{L\psi}\Big[L\,\nabla^2\psi + \nabla L\cdot\nabla\psi\Big], \qquad R_{\theta\theta} = -\frac{e^{-2h}}{L\psi}\Big[\psi\,\nabla^2L + \nabla L\cdot\nabla\psi\Big]$$

and swapping $\psi\leftrightarrow L$ in one gives the other exactly — difference identically zero. Each fiber's Einstein component has the same form in its own length and the other's; the $u$-fiber's is sourced by $T_{uu}$, the Hopf fiber's by $T_{\theta\theta}$. In the torus language, one statement:

> **The length of each cycle is sourced by matter averaged over the other.**

### II.12.3 What breaks it, and only that [D]

*The Hopf twist.* The Hopf circle has Chern number $1$ over $S^2$; the $u$-circle has $0$. The $\tfrac14L_H^2F_{\rm Hopf}^2$ term appears in one reduction and not the other; $SL(2,\mathbb{Z})$ can redistribute $(0,1)$ but not remove the total.

*The needle.* $|\tau_{\rm eff}|\approx3\times10^{25}$. A Kaluza–Klein reduction is valid on the small circle; the large one is geometry you see. So "reduce on $u$" is our gravity, and "reduce on Hopf" is the same 5-D solution viewed from a world in which $u$ is a visible 50-micron dimension and the Hopf circle is hidden. At $\tau = i$, with the twist redistributed, neither would be privileged.

### II.12.4 The surprise: the projective postulate is a theorem for the Hopf fiber [D]

The Hopf $U(1)$ is $z\mapsto e^{i\theta}z$ on $\mathbb{C}^2$, and at $\theta = \pi$ it is $-1$: **the Hopf circle through $\hat n$ passes through $-\hat n$** (verified pointwise). The Hopf-average of matter over a fiber automatically includes both twins. For the Hopf reduction, "gravity sums over $\pm\hat n$" needs no postulate — it is the geometry.

For the $u$-reduction it *had* to be postulated (A2, the disconnected fiber). Non-privileging says why: the $u$-fibration must pass through both $\pm\hat n$ because the Hopf fibration does — and in $\mathbb{R}^4$ it does, since a line through the origin meets $S^3$ at $\pm\hat n$. **The projective postulate was the $u$-fiber catching up to a property the Hopf fiber has for free.** It is now derived rather than stated: A2 follows from A1 and non-privileging.

### II.12.5 The mirror law's content [D]

The mirror is v2's dilaton equation, read with a Hopf-averaged source:

$$\ell^2\Box\psi = -\tfrac43\psi\Big(\tau_u - \tfrac12\tau\Big), \qquad \tau = \langle T\rangle_{\rm Hopf}/\bar\epsilon$$

For a localized mass the Hopf average dilutes it by (extent)$/2\pi\ell$; the response of $\psi$ is smaller than through Law I ($6\times10^{-32}$ for Earth) and for the cosmic background is $10^{-61}$. **$G$ remains a constant.** Where the mirror has content is the background itself: $\psi_0$ is set by $\langle\rho\rangle_{\rm Hopf} = \bar\rho$ together with the winding and $\Lambda_5$ — the Mach relation read from the other fiber, still a consistency relation, now with two faces.

## II.13 The polarization check

*The $\phi^2$-dressing of the geometric phase (§II.8) is a prediction about polarization transport in gravitational wells, and general relativity has its own answer: for a static, non-rotating mass, zero net rotation, by parity. The contact structure is chiral — $\alpha_H\wedge d\alpha_H>0$ fixes a handedness — so v4 is not bound by that parity argument, and the check is whether its rotation is consistent with GR's zero to observational precision. Three pieces.*

**A. The gravitational dressing passes [D].** The term $\int_\Sigma d(\phi^2)\wedge\alpha_H$ is of order $\Phi\times(\text{path length})/\ell$: $10^{-22}$ rad for light grazing the Sun, $10^{-8}$ for a galaxy lens over a Gpc, $10^{-6}$ in a galaxy-scale arena. GR's zero is reproduced to every measured precision.

**B. The vacuum phase is the live item [D].** Along an *open* path, a Hopf-charged photon's polarization rotates by the vacuum term $\int_{\rm path}\alpha = \int\cos\theta\,ds/\ell$, $\theta$ the angle between the path and the local Reeb direction. This does not vanish when $\Phi = 0$. For the cosmic microwave background it is an **anisotropic cosmic birefringence** with a dipole-like sky pattern,

$$\beta(\hat n)\sim\frac{D}{\ell}\,\langle\cos\theta\rangle: \qquad 6.4°\ (\ell = 63\text{ Gpc}), \quad 0.64°\ (630\text{ Gpc}), \quad 0.29°\ (1400\text{ Gpc})$$

against an observed isotropic $\beta = 0.35°\pm0.14°$ and anisotropic components bounded near $0.3°$. Hence

$$\boxed{\;\beta<0.3°\;\Longrightarrow\;\ell\gtrsim1400\text{ Gpc}\approx95\times\text{the horizon}\;\Longrightarrow\;|\Omega_k|\lesssim10^{-5}\;}$$

The current bound is $|\Omega_k|<5\times10^{-3}$, so v4 survives — and **predicts flatness more than four hundred times tighter than measured**, with an anisotropic birefringence just below present sensitivity. This is new in v4 because the Hopf structure became global: every photon sees it. It is a **dichotomy** to be resolved: either the photon is Hopf-neutral (the helicity identification of §II.8 fails, and the second order has no polarization physics), or the universe is flat to $10^{-5}$ and the birefringence is there to be found. Either outcome is decisive; the pair is the sharpest observational statement the second order has made.

**C. Closed loops are clean [D].** For two paths forming a loop, the vacuum flux is $2A/\ell^2$: $5\times10^{-10}$ rad for a galaxy lens, $10^{-10}$ for a microlens, $10^{-55}$ in a laboratory. The enclosed-mass law of v3 is gone, and nothing replaces it with a spurious vacuum signal.

## II.14 Laws and axioms, version 4

> ### ■ ARENA
> - **A1.** $M_5 = \mathbb{R}_t\times S^1_u\times S^3$, $S^3\cong SU(2)$; the spatial total space is the Hopf surface with elliptic fiber $\tau = 2\pi i/\ln\lambda$.
> - **A2.** Base $\mathbb{R}_t\times\mathbb{RP}^3$, $\mathbb{RP}^3\cong SO(3)$; disconnected fiber (the seed) — **now derived** from A1 and non-privileging (§II.12.4).
> - **A3.** $\chi(M_5) = 0$; $\Lambda_5<0$ for the winding stabilization.

> ### ■ FIELDS
> - **A4.** Base metric $g^{(4)}$; winding scalar $f$; dilaton $\psi$ stabilized at $\psi_0^2 = 3w^2/4|\Lambda_5|$.
> - **A5.** Electromagnetic $\mathcal{F}$ on the cover.
> - **A6.** Contact form $\alpha = \phi^2 f\alpha_H$ on the spatial $S^3$ — *not* an independent field.

> ### ◆ LAW I — GRAVITY
> - **A7.** Projective postulate: source $S = T_+$.
> - **A8.** $\ell^2R_{\mu\nu} = \ell^2\psi^{-1}\nabla\nabla\psi + 2(\tau - \tfrac13\tau g)$; in the conformally-round sector, $(\Delta+3)\delta\phi = -2\pi\delta\rho_+$ and $L_H = 2\pi\ell\phi^2$.

> ### ◆ LAW II — THE FIRST-ORDER FIBRATION
> - **A9.** $\Box f = 0$, $\oint df = \ln\lambda$; graviphoton $A_\mu = 0$ (vacuum; §II.10 the option).

> ### ◆ LAW III′ — THE CONTACT STRUCTURE
> - **A10.** $\alpha = \phi^2 f\alpha_H$, twist density $f^2/\phi^2$; $f[\rho_-]$ kinematic, $f = 1$ in vacuum.

> ### ◆ ELECTROMAGNETISM
> - **A11.** $d\mathcal{F} = 0$, $d\star_5\mathcal{F} = \star_5\mathcal{J}$ on the cover; photon a section with Hopf charge $n$.

> ### ▣ DERIVED
> - **D1–D5** as v3 (cone, no endpoints, static twin = quotient, Mach relation, $\gamma = 1$).
> - **D6.** The partition: fiber length $\leftarrow T_+$, contact deformation $\leftarrow\rho_-$.
> - **D7.** The seed is $SU(2)\to SO(3)$.
> - **D8.** **Law I is the fiber-length equation in the conformally-round sector**, with the twin inherited from $(\Delta+3)$.
> - **D9.** One radion; no quantization; contact-metric slaving excluded by PPN.
> - **D10.** The mirror law: each cycle's length is sourced by matter averaged over the other (§II.12); exact on the untwisted torus.
> - **D11.** Gravitational dressing of the geometric phase $\lesssim10^{-6}$ rad; vacuum birefringence $\beta\sim D/\ell$; flatness $|\Omega_k|\lesssim10^{-5}$ or a Hopf-neutral photon (§II.13).

---

# PART III — STATUS

## III.1 What changed from version 3

| | v3 (bundle) | v4 (contact) |
|:--|:--|:--|
| second-order object | $U(1)$-bundle $E$ over $S^3\setminus\{\text{masses}\}$ | contact form on $S^3$ |
| Hopf structure | one per mass | one, global, deformed |
| twin (second order) | anti-monopole | negative deformation |
| moduli | $\psi$, $\Omega$ — no joint minimum | $\psi$ only |
| quantization | fork, open | absent |
| Law I on the fibers | $G_B = G[\Omega]$ in the conformally-flat $E$ | $(\Delta+3)\delta\phi = -2\pi\delta\rho_+$, $L_H = 2\pi\ell\phi^2$ |
| two-path phase | $2\pi m_-/m_{\rm unit}$, enclosed mass | shape-dependent functional |
| $m_{\rm unit}$ bound | $\gtrsim10^{14}$–$10^{17}M_\odot$ | to be re-derived |
| selection rule for $\mathbb{Z}_2$ | from $O(2)$ descent | to be re-derived |
| conformal root, $O(5)$, $S^4$ Easter eggs | present | not carried |
| new constants | $m_{\rm unit}$, $g_2$ | none |
| seed | postulated (A2) | **derived** (§II.12.4) |
| mirror law | — | exact on the untwisted torus |
| birefringence | — | $\beta\sim D/\ell$; $\lvert\Omega_k\rvert\lesssim10^{-5}$ or Hopf-neutral photon |

## III.2 The ledger

| result | tag |
|:--|:--|
| joint stabilization of two radions has no critical point ($A = -B$) | **[V]** |
| $S^1_u\times S^3$ = Hopf surface; elliptic fiber $\tau = 2\pi i/\ln\lambda$; $\lvert\tau_{\rm eff}\rvert\approx3\times10^{25}$ | **[T/D]** |
| Hopf connection is a contact form, $\alpha\wedge d\alpha\neq0$ everywhere | **[V]** |
| Lichnerowicz on the ESU linearizes to $(\Delta+3)\delta\phi = -2\pi\delta\rho_+$ | **[D]** |
| lone ball: dipole $0.169$, no solution; with twin: regular, symmetric to $10^{-11}$ | **[V]** |
| $L_H = 2\pi\ell\phi^2$: fibers lengthen in wells ($2.017\times$ at the ball's center), identically at the twin | **[V]** |
| $\Phi = -2\delta\phi$ reproduces the two-dimple potential | **[V]** |
| contact-metric slaving gives $O(\Phi)$ anisotropy in $\gamma$: excluded | **[D]** |
| one radion; Hopf length is a metric component | **[D]** |
| twist density $f^2/\phi^2$; even reduces, odd multiplies | **[D]** |
| no net flux through closed surfaces; two-path phase shape-dependent | **[T/V]** |
| $R_{uu}\leftrightarrow R_{\theta\theta}$ under $\psi\leftrightarrow L$: difference $0$ on the untwisted torus | **[V]** |
| $-1\in U(1)_{\rm Hopf}$: the Hopf circle through $\hat n$ contains $-\hat n$; A2 derived | **[V/D]** |
| mirror sourcing of $\psi_0$ by $\bar\rho$: $10^{-61}$; $G$ constant | **[V]** |
| gravitational dressing of polarization $\le10^{-6}$ rad; GR's zero reproduced | **[D]** |
| vacuum birefringence $\beta\sim D/\ell$: $6.4°$ at $63$ Gpc; $\beta<0.3°\Rightarrow\ell>1400$ Gpc, $\lvert\Omega_k\rvert<10^{-5}$ | **[D]** |
| closed-loop vacuum flux $2A/\ell^2$: $\le5\times10^{-10}$ rad in any lensing geometry | **[D]** |

## III.3 Open problems of version 4

1. **The birefringence dichotomy** (§II.13) — Hopf-neutral photon, or $|\Omega_k|\lesssim10^{-5}$ with an anisotropic $\beta$ just below sensitivity. Decidable by the next generation of CMB polarization data, and by whether the helicity identification can be derived rather than assumed.
2. **The form of $f[\rho_-]$** — Law III′'s content. The rescaling $f = \sqrt{1+\epsilon\rho_-}$ is the simplest choice; whether a variational principle selects it, and what $\epsilon$ is, are open.
3. **Re-derive the observational bound** — the lensed-image polarization comparison as a functional of $f$; recover a number to replace $m_{\rm unit}$.
4. **Re-derive the $\mathbb{Z}_2$ selection rule** — v3's argument used Chern classes; v4 needs one from contact topology or must give it up.
5. **Beyond the conformally-round sector** — how the five non-conformal metric components relate to the contact structure, if at all; whether dynamical (radiative) configurations have a fiber reading.
6. **The graviphoton option** (§II.10) — whether to switch on $A_\mu$; the $U(1)^2$ Chern–Simons dynamics.
7. **Inherited** — the AdS uplift ($10^{60}$); a law for $\ell$ in the Tully–Fisher sector; the rise beyond the equator; the literature review.

## III.4 The next three moves

1. **Decide whether the photon is Hopf-charged.** If helicity $=$ Hopf charge can be derived from the spin structure rather than assumed, v4 predicts $|\Omega_k|\lesssim10^{-5}$ and a dipole birefringence; if not, the second order is silent on light and the constraint evaporates. This is now the highest-value question in the program.
2. **Fix $f$.** Try the rescaling ansatz and one alternative, compute the two-path phase for a lensed configuration under each, and see which gives a bound comparable to v3's.
3. **Extend §II.4 to first order in dynamics.** Take a slowly rotating or slowly evolving source and ask whether $L_H$ still tracks a single scalar; find where the fiber-length reading of Law I stops.
4. **The literature review**, now overdue by two versions.

---

## Reference card, version 4

| topic | statement |
|:--|:--|
| **arena** | Hopf surface; $T^2$ periods $(\ln\lambda,2\pi i)$; $S^3 = SU(2)$, $\mathbb{RP}^3 = SO(3)$ |
| **contact form** | $\alpha = \phi^2 f\alpha_H$; Reeb $= R_H/\phi^2$; twist $f^2/\phi^2$ |
| **Law I on the fibers** | $(\Delta+3)\delta\phi = -2\pi\delta\rho_+$; $L_H = 2\pi\ell\phi^2$; twin inherited |
| **numbers** | ball $R = 0.35$: $\phi^2 = 2.017$ at center, $1.620$ at surface, $1$ at equator; same at the twin |
| **partition** | fiber length $\leftarrow T_+$; contact deformation $\leftarrow\rho_-$ |
| **moduli** | $\psi$ only, stabilized; Hopf length is geometry |
| **excluded** | contact-metric slaving ($\gamma$ anisotropy); second radion; quantized flux |
| **lost from v3** | monopoles; enclosed-mass law; $m_{\rm unit}$; $O(5)$ recentering; $S^4$ root |
| **mirror law** | each cycle's length $\leftarrow$ matter averaged over the other; A2 derived from $-1\in U(1)_{\rm Hopf}$ |
| **polarization** | dressing $\le10^{-6}$; vacuum $\beta\sim D/\ell$; $\ell>1400$ Gpc or Hopf-neutral photon |
| **open** | the dichotomy; $f[\rho_-]$; the bound; the selection rule; beyond conformally-round; graviphoton |
