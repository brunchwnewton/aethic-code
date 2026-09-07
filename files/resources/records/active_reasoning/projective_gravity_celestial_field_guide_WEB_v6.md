# Projective Gravity — Version 6

### The Contraction, on the 4-Sphere: a field guide

> **What this version is.** The original arena, with four laws and one identity. A dominant central mass at one pole of a 4-sphere; its field lines the meridians, each a great circle through both poles, so the fiber through $\hat n$ *is* the fiber through $-\hat n$. Sphere-matter enters the fibration as a permeability, never a source. Gravity on the quotient by meridians. About each secondary mass, a local law fixes a $U(1)$ connection whose flux is the mass's odd part smeared along its meridian; the bundle it defines is the second-order total space $E$. Nothing compactified, nothing dynamical but gravity and light.
>
> **The identity.** At every level, the degrees of freedom of a total space are exactly base plus fiber length plus connection; even matter fills the first two, odd matter fills the third. *The projection discards; the twist recovers; together they see all of $T$.*
>
> **One identity carried since v2 is retracted (§IV.1): the twin's opposite electric charge.** It was the $\cot\chi$ Green's function, which puts a charge at the antipode where the seed puts nothing; with the compensating charge elsewhere the field *vanishes* at the twin. The twin is gravitationally a copy and electromagnetically empty.
>
> **Two verdicts from the record are inverted here, with reasons (§V.1):** the dielectric fibration law, retired in v2 because it made the fine-structure constant vary, is legal in v6 because v6 has no dilaton; and $S^4$, rejected in the dielectric era because it cannot carry a nowhere-vanishing fibration, is *required* in v6 because its Euler characteristic forces exactly the two degenerate points that a sourced fibration has.
>
> **Tags.** **[V]** verified · **[T]** cited theorem · **[D]** derived · **[S]** sketch · **[O]** open · **[R]** retired.
>
> **Conventions.** $G = c = 1$; $\ell$ the base radius; $M_c$ at the south pole $0$, its antipode $\infty$; $\chi$ the polar angle on $S^4$, latitudes the level sets; $T_\pm(\hat n) = T(\hat n)\pm T(-\hat n)$; $\phi$ the base conformal factor, $g_3 = \phi^4g_{S^3}$, $\Omega = \phi^2$.

---

# I. THE LAWS

> ### ◆ LAW I — GRAVITY
> $$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T^+_{\mu\nu}\quad\text{on }\mathbb{R}_t\times\mathbb{RP}^3,\qquad\Lambda = 1/\ell^2$$
> General relativity on the quotient, sourced by the meridian-averaged, pair-summed stress-energy.

> ### ◆ LAW II — THE FIBRATION
> $$\nabla\cdot\big(\mu(\rho)\,\nabla\Phi_u\big) = M_c\,\big[\delta^4(0) - \delta^4(\infty)\big]\quad\text{on }S^4$$
> The $u$-fibers are the gradient lines of $\Phi_u$. The poles are the only flux endpoints; all matter enters through $\mu(\rho)$. Kinematic.

> ### ◆ LAW III — THE SECOND-ORDER CONNECTION
> $$dF = 2\pi\star J_-,\qquad J_- = \frac{\rho_-}{m_{\rm unit}}\;\text{smeared along the meridians},\qquad F = d\alpha$$
> $\alpha$ is a $U(1)$ connection over $S^4$; its fiber length is locked to gravity, $L_E = \Omega\,L^{\rm ref}$. Kinematic.

> ### ◆ LAW IV — ELECTROMAGNETISM
> Maxwell on $\mathbb{R}_t\times S^4$, $\epsilon = \mu_{\rm EM} = 1$. Total charge zero on the compact cover.

Four laws. The projective postulate is not among them: it is derived (§II.3).

## I.1 The action

$$S = \int_{\mathbb{R}_t\times\mathbb{RP}^3}\!d^4x\,\sqrt{-g}\,\frac{R - 2\Lambda}{16\pi G} \;+\; \int_{\mathbb{R}_t\times S^4}\!d^5x\,\sqrt{-\hat g}\,\Big[-\tfrac14\mathcal{F}_{MN}\mathcal{F}^{MN} + \bar\Psi\big(i\Gamma^MD_M - m\big)\Psi + \mathcal{L}_{\rm matter}\Big], \qquad \hat g = \pi^*g + (\text{fiber part})$$

Gravity's action lives on the base; matter's on the cover, in the metric pulled back from the base. Varying $g$ on the base integrates matter over both fibers of each base point, which is how $T_+$ arises — the projective postulate is the structure of this action, not an added rule. **Laws II and III have no action**: they are kinematic, determined by the placement, with no independent dynamics. The constants are $G$, $\Lambda = 1/\ell^2$, the function $\mu(\rho)$, and $m_{\rm unit}$.

## I.2 No preferred foliation of spacetime [D]

Law I is Einstein's equation on the 4-manifold $\mathbb{R}_t\times\mathbb{RP}^3$: generally covariant, any slicing. Law II in its covariant form is $\nabla_A(\mu(T)\nabla^A\Phi_u) = $ source on the 5-dimensional cover, with $\mu$ a function of the trace and the poles two worldlines; the fibers are its gradient curves, spacelike by admissibility, and the quotient by them is a 4-dimensional spacetime with no distinguished time. The static presentation "Law II on $S^4$ at fixed $t$" is a gauge for static configurations. What v6 does select is a preferred *fibration of the cover* — that is what the theory is — and it is invisible from the base, where covariance is tested. Same verdict as v2's two-speed cover: a preferred structure upstairs, no preferred frame downstairs.

## I.3 The two Gauss laws on a 3-sphere [D]

Take any latitude $S^3$ between the poles.

- **The fibration flux through it is $M_c$, always.** Law II has its source at $0$ and sink at $\infty$ with nothing between, so every latitude carries the full flux — and closure fixes what that flux is:
$$\boxed{\;\frac{GM_c}{c^2\ell} = \frac{\pi}{2}\;}$$
the Mach relation with the central mass as the closure mass ($M_c = 2\times10^{24}M_\odot$ at $\ell = 63$ Gpc). This is the gravitational-constant identity of v6: $G$ is a constant of Law I, and the pair $(M_c,\ell)$ is constrained to one relation by the requirement that the base be static and closed.
- **The electric flux through it is zero.** Law IV on the compact cover has total charge zero; with charges paired on a latitude, every latitude encloses net nothing.

So every 3-sphere carries the full fibration flux and no electric flux; the primary is the $u$-source and electromagnetically neutral. "Zero divergence in the total space, divergence only on the base" is exactly right for the $u$-flow: $\nabla\cdot(\mu\nabla\Phi_u) = 0$ off the poles, and the poles' divergence appears on the base as the uniform jellium. For electromagnetism, $\nabla\cdot E = \rho_{\rm charge}$ on the cover with total zero, and there is no base electromagnetism at all.

---

# II. THE COVER AND THE FIRST ORDER

## II.1 The 4-sphere and its two forced poles [T/D]

The cover is $\mathbb{R}_t\times S^4$. Poincaré–Hopf says any vector field on $S^4$ has zeros of total index $\chi(S^4) = 2$. A gradient flow with one source and one sink has index $(+1)+(+1) = 2$ — the minimum. **The fibration must degenerate at exactly two points, and Law II puts the central mass at one and its antipode at the other.** On $S^1\times S^3$ ($\chi = 0$) a center is optional; on $S^4$ it is compulsory. The earlier rejection of $S^4$ — that it cannot carry a *nowhere*-vanishing fibration — is the same fact read for a sourceless law. A sourced law wants two zeros, and $S^4$ supplies exactly two.

## II.2 Law II: all matter weaves, only the poles source [D/V]

With sphere-matter as additional sources, a secondary mass becomes a critical point of $\Phi_u$, its lines are repelled by the center and die at a saddle, and no fiber through it reaches $-\hat n_0$: the twin is lost. With sphere-matter as permeability, the maximum principle forbids interior critical points: every point lies on exactly one meridian from $0$ to $\infty$, the mass sits *on* a twin-pair fiber, and the latitudes are deformed without pinching. Version 1's Poisson rule pinched the sphere into bubbles and made Keplerian sources impossible. "The center has most of the mass" means: $M_c$ sets the flux, and the meridians are radial to the extent $\mu$ is uniform. In a 2-D test with $\mu = 7$ at a mass, seven of seven lines launched at it passed through **[V]**.

## II.3 The quotient, the seed, the jellium [D]

The base is the space of meridians, $\mathbb{RP}^3$: each point one connected great circle through both poles, crossing the equator at $\pm\hat n$. Gravity reads the fiber average, which includes both twins by construction.

> **The seed.** Matter at $(\chi_0,\hat n)$ sources the base at $[\hat n]$, whose lift has wells at $\pm\hat n$; nothing is at $-\hat n$. A great circle through the poles crosses the equator twice. Geometry.

Both poles lie on every meridian, so $M_c$ contributes equally to every fiber average and is uniform on the base: **the jellium of the Einstein static universe is $M_c$'s column density**, and the Mach relation reads "the central mass sets the base radius."

## II.4 The partition at the first order [T/D]

$S^4\setminus\{\text{poles}\}\to\mathbb{RP}^3$ has interval fibers; the 10 components of the cover metric are $6$ (base) $+1$ (fiber length) $+3$ (connection). The base keeps $T_+$ and discards *which twin*. That discarded datum is odd, and it is what the second order recovers.

---

# III. THE SECOND ORDER — THE HOPFIAN CHARACTER

## III.1 Law III is local, and $S^4$ makes it well-posed [D]

In four dimensions a 2-form field strength has a **1-form source**: $dF$ is a 3-form, $\star J$ of a 1-form. Consistency $d(dF) = 0$ requires $d\star J = 0$ — the source must be a *conserved current*, supported on closed lines. $J_-$ is the odd mass density smeared along the meridians. On $S^4$ every meridian is a closed circle: $d\star J_- = 0$ automatically. On $\mathbb{R}^4$ the rays are open at $0$ and at $\infty$, the current has endpoints, and the law is inconsistent. **$S^4$ is not an option for Law III; it is what makes Law III well-posed.**

This is the local law you asked for. The "Hopf lift of each shell" is not a separate global construction; it is the **symmetric solution** of Law III about one meridian: over a shell of angular radius $\vartheta$, $F|_{\rm shell} = \tfrac{c}{2}\sin\vartheta\,d\vartheta\wedge d\varphi$, flux $2\pi c$ through every shell **[V]**, $c = M_-/m_{\rm unit}$. Many masses: superpose. A continuous $\rho_-$: $J_-$ smooth, flux real-valued, $E$ an $\mathbb{R}$-bundle — the quantization fork, idle in a kinematic theory.

## III.2 The monopole is the meridian [T/D]

A 2-sphere cannot link a point in a 4-space ($H^2(S^4\setminus\text{points}) = 0$); it links a circle ($H^2(S^4\setminus\text{circle}) = \mathbb{Z}$). The Chern class lives on the meridian through the secondary mass — the mass smeared along $u$, exactly as gravity sees it. Orient the meridian once around: its equatorial crossings at $\hat n_0$ and $-\hat n_0$ are traversed in opposite senses. **The anti-monopole at the twin is the same circle from the other hemisphere**, a linking number rather than an orientation argument, and the Chern number on the meridian through $[\hat n]$ is $(M(\hat n) - M(-\hat n))/m_{\rm unit}$: a lone mass gives $\pm1$, equal masses at both twins give $0$. **It is the odd part.**

## III.3 The topology of $E$ [T]

$E$ is the circle bundle over $S^4\setminus\Gamma$, $\Gamma$ the graph formed by the $N$ meridian circles through the two poles (2 vertices, $2N$ edges). Alexander duality gives $H^2(S^4\setminus\Gamma) = H_1(\Gamma) = \mathbb{Z}^{2N-1}$; the physical bundle has equal flux on both arcs of each meridian — flux is not created at the poles — and so lives in $\mathbb{Z}^N$: one integer per secondary mass. For $N = 1$, $S^4\setminus\text{circle}\simeq S^2$ and the Chern-1 bundle is Hopf: $E\simeq S^3$.

**$S^4$ does not become anything.** $E$ is a new 5-dimensional space fibered over it; each 2-shell in $S^4$ has as its preimage a Hopf 3-sphere in $E$. The shells are lifted, not replaced. Locally $E = S^4\times S^1$; globally twisted along $\Gamma$.

## III.4 The tower

$$E\;(15)\;\xrightarrow{/\,\text{Hopf circles}}\;S^4\;(10)\;\xrightarrow{/\,\text{meridians}}\;\mathbb{RP}^3\;(6)$$

With time: $\mathbb{R}_t\times E\,(6)\to\mathbb{R}_t\times S^4\,(5)\to\mathbb{R}_t\times\mathbb{RP}^3\,(4)$ — **the second-order total spacetime is six-dimensional**: time, the Hopf circle, and the 4-sphere. Two fibrations, two circle quotients. The $H$-circles of earlier versions — the spatial Hopf fibration of each latitude — are dropped as a named structure: what they gave (the seed via $-1\in U(1)_R$; Law I as a fiber-length equation) now follows from Law II and from $E$'s own fiber respectively.

## III.5 The partition at the second order [V/D]

Over a shell, the Hopf 3-sphere's six functions split $3+1+2$:

| degrees of freedom | filled by | parity |
|:--|:--|:--|
| shell 2-metric (3) | Law I: $\Omega^2\times$round | even |
| fiber length (1) | Law I: $L_E = \Omega L^{\rm ref}$ | even |
| connection, Hopf form | the arena | neither |
| connection, flux and deformation (2) | Law III: $J_-$ | **odd** |

Four even from gravity, two odd from Law III, nothing left over. And the two halves source two curvatures: base Ricci $\leftarrow T_+$; **the Weyl tensor of $E$ is exactly the connection's deviation from Hopf** — $C_{abcd}C^{abcd} = 0$ for the Hopf connection, $4\epsilon^2(16-13\sin^2\vartheta)/3\sin^4\chi$ for a perturbation $\epsilon\sin^2\vartheta$ **[V]**. Base Ricci is the even face, $E$-Weyl the odd face.

## III.6 Encoding, not sourcing — and what $E$ has that $S^4$ has forgotten [D]

**The Hopf fibers do not source Law I's curvature.** Matter does: base Ricci $\leftarrow T_+$. What $E$'s fibers do is *encode* the even half — the fiber length $L_E = \Omega L^{\rm ref}$ is the conformal factor by another name, so $E_{ij} = -2[\nabla\nabla\phi]^{\rm TF}$ can be read off it — and *carry* the odd half in the connection, which sources $E$'s own Weyl tensor and which Law I never sees. Versions 4 and 5 established this as the verdict; v6 states it as the partition. Sourcing runs from matter to two curvatures; the fibers are where the two halves are kept.

**The significance of $E$ over $S^4$.** Quotienting $E$ by its Hopf circles loses the fiber length (redundant with $\Omega$) and the connection (not redundant with anything). So $S^4$ carries the 10 components of a spatial 4-metric and has *forgotten which twin holds the matter*; $E$ carries 15 and remembers. Pre-quotienting is the full placement; post-quotienting is its even half.

**Does quotienting reveal curvature $E$ lacked?** No — it discards. Law I's Ricci on $\mathbb{RP}^3$ is present in $E$ as the pullback through the tower; $E$ has that *and* its own Weyl from the connection. $E\to S^4$ removes the second; $S^4\to\mathbb{RP}^3$ removes the $u$-position. Nothing is created by a quotient; each step forgets one datum, and Law I is what is left when both are forgotten.

## III.7 What sees $E$ [T/D]

Light does not: the photon is the Hopf-neutral zero mode, and helicity is not circle momentum. Gravity fixes $E$'s even half and is blind to its odd half. If $E$ were made dynamical, its fiber length is already locked to $\Omega$ in the conformally-flat sector (no separate stabilization **[V]**) and its flux gravitates with $g_2/m_{\rm unit}<0.024$ from Mercury **[D]**. In the kinematic theory $E$ is a record of the placement's odd half — which is what the partition principle says it must be.

---

# IV. IDENTITIES AND THEOREMS

| identity | status | mechanism |
|:--|:--|:--|
| twin at $-\hat n$, same mass, full tidal field | **[V]** | same meridian; $(\Delta+3)$ same-sign Green's function; $E_{ij}$ identical at the empty antipode to $10^{-11}$ |
| twin has opposite electric charge | **[R]** — retracted | was the $\cot\chi$ Green's function, which places $-Q$ at the antipode; the seed puts nothing there. With the compensating charge elsewhere (uniform background, or other matter), $E\to0$ *linearly* at the antipode **[V]**. **The twin is electromagnetically empty** |
| charged secondary and its twin | **[D]** | RN at $\hat n$ from its own field ($T_{\rm EM}(-\hat n)\approx0$, so $T_+\approx T_{\rm EM}(\hat n)$); the twin's metric carries the same $Q^2/r^2$ term with $\nabla\cdot E = 0$ and $E = 0$ — a **tidal charge**, not an electromagnetic one |
| twin has opposite second-order charge | **[D]** | the linking number, §III.2 — this one survives: it is odd *mass*, not charge |
| $GM_c/c^2\ell = \pi/2$ | **[D]** | §I.3: the fibration flux through every latitude is $M_c$, and closure fixes it |
| $G$ a constraint, not a derivation | **[D]** | Mach relation with $M_c$ as jellium |
| $\alpha_{\rm fine}$ exactly constant | **[D]** | Law IV with $\epsilon = 1$; no dilaton |
| PPN $\gamma = 1$ | **[D]** | no radion; trivially |
| Bianchi | **[T]** | Law I is GR; conservation fiber-averages |
| $\mathbb{Z}_2$ on fermions $= (-1)$ | **[D]** | $S^3 = SU(2)$, antipode $= -1$; the $2\pi$ spinor sign only — the former $C$ was the retracted charge |
| photon Hopf-neutral | **[T]** | zero mode |
| projective postulate | **derived** | §II.3 |

## IV.1 The retraction, stated once

Since v2 every version has said the twin carries opposite electric charge, by "Gauss on the closed sphere." Gauss forces the compensating charge *somewhere*; the $\cot\chi$ field puts it at the antipode, and that is a choice — one that requires charged matter exactly where the seed says there is none. With the compensating charge wherever the other charges are, the field of $Q$ is regular at the antipode and vanishes there. The twin is a gravitational copy with no electromagnetic presence: the meridian's field line from $\hat n$ passes through the primary and *dies out* at $-\hat n$ rather than terminating on a charge. What survives of the picture you liked: the meridian is still the passage, the primary is still neutral pass-through, and the *fibration* flux — not the electric flux — is what the meridians carry through every 3-sphere.

## IV.2 Orbits, the $v^2$ family, and its limits [D]

On the base the secondary is a well of mass $M$ in the jellium $M_c$, and the closed-universe orbit machinery of v2 applies unchanged: Keplerian orbits with closure corrections near the well; confinement and precession globally; the closure plateau $v^2_{\rm eq} = 4GM/\pi\ell$ at the equator in the idea-B arena, kept as a shape with its scale open. The family is valid for $M\ll M_c$ and ends where $M\to M_c$: a secondary as heavy as the primary has $GM/c^2\ell = \pi/2$, is relativistic at every radius, and the plateau formula would read $2c^2$. A secondary is a $\mu$-bump and a primary a flux source; mass does not convert one into the other, because the option in which it does loses the twin (§II.2).

**Other primaries.** Poincaré–Hopf allows $k$ sources and $k$ sinks with $2k-2$ index-$(-1)$ saddles. Each primary owns a basin; the basins are separated by saddle surfaces; each basin quotients to its *own* base. This is version 1's watershed foam, returning for sources only — secondaries never create basins. A universe of several primaries is several closed universes glued along watersheds, which is the one place idea B's "every galaxy its own sphere" has a structural home **[S]**.

**Twin theorem [V]** — $(\Delta+3)$, dipole kernel, a lone mass has no static solution. **Closure [T/V]** — ESU with $\bar\rho$ as $M_c$'s column density. **Law I as the fiber-length equation [V]** — $\delta L_E/L_E = -\Phi$, $N L_E = $ const, $E_{ij} = -2[\nabla\nabla\phi]^{\rm TF}$, PNDs along $\widehat{\nabla L_E}$, Petrov type as the Hessian's degeneracy. **The static wall [T]** — no redshift; idea B's routes end at the seed's symmetry; the magnifier $D_A = \ell\sin\chi$ and the Tully–Fisher toy remain.

---

# V. RETIRED, INVERTED, OPEN

## V.1 Two verdicts inverted, with reasons

**The dielectric law.** Retired in v2 (transcript 09-04, §2362): $\epsilon(T)$ entered the winding energy, so the stabilized dilaton scaled as $\psi_0\propto\sqrt\epsilon$; the Kaluza–Klein reduction of Maxwell on the fiber gave $\alpha_{\rm fine}\propto1/\psi_0$; hence $\alpha_{\rm fine}$ tracked local density, and varying-$\alpha$ bounds at $10^{-7}$ forced $\epsilon - 1<2\times10^{-5}$. **Every link ran through the dilaton.** Version 6 has no dilaton and no reduction of Maxwell on any fiber: $\mu(\rho)$ enters Law II only, sets the direction of the meridians, and touches nothing electromagnetic. The chain has no first link. Same equation, different theory.

**$S^4$.** Rejected in the dielectric era (transcript 08-31, §3437) because a sourceless fibration needs a nowhere-vanishing 1-form and $\chi(S^4) = 2$. A sourced fibration needs exactly two zeros, and $\chi(S^4) = 2$ is exactly two. The objection is the requirement.

## V.2 Retired

| item | why not in v6 |
|:--|:--|
| compactification, dilaton, winding, PPN rescue, $G_4$ from $G_5$, sub-mm scale, cone theorem | dynamical-reading machinery |
| monopoles at points, $O(2)$ descent by orientation | monopoles are meridians; descent is a linking number |
| the $H$-circles as a named structure | redundant with Law II and $E$'s fiber |
| second KK circle, joint stabilization, $\tau$, mirror | $E$ is kinematic |
| Scherk–Schwarz neutrinos | never approved; gauge-illegal |
| $S^7\to\mathbb{CP}^3\to S^4$ | the bases of the Hopfian character are shells |
| separate $f[\rho_-]$ | absorbed into Law III: $J_-$ continuous or discrete |
| the twin's opposite electric charge; $C$ in the fermion $\mathbb{Z}_2$ | §IV.1: the $\cot\chi$ choice contradicts the seed |

## V.3 Open

1. $\mu(\rho)$ — any increasing function weaves; nothing selects one; in a kinematic theory it is observable only through the footprint dilation, bounded by $4$.
2. What couples to $E$ — nothing at the zero mode; dynamical $E$ is the only way it acts.
3. The poles for matter.
4. Idea B — unchanged.

---

## Reference card, version 6

| topic | statement |
|:--|:--|
| **laws** | I: GR on $\mathbb{RP}^3$, $T_+$. II: $\nabla\cdot(\mu\nabla\Phi_u) = M_c[\delta(0)-\delta(\infty)]$. III: $dF = 2\pi\star J_-$, $L_E = \Omega L^{\rm ref}$. IV: Maxwell on $S^4$ |
| **the identity** | total $=$ base $+$ length $+$ connection; even $\to$ base $+$ length, odd $\to$ connection |
| **cover** | $S^4$; two zeros forced by $\chi = 2$; $M_c$ at one, $\infty$ at the other |
| **seed** | a meridian crosses the equator at $\pm\hat n$; derived; $M_c$ is the jellium |
| **Hopfian character** | Law III's symmetric solution about a meridian $=$ Hopf over each shell; monopole $=$ the meridian; Chern $= M_-/m_{\rm unit}$ |
| **$E$** | circle bundle over $S^4\setminus\Gamma$, class in $\mathbb{Z}^N\subset\mathbb{Z}^{2N-1}$; $E\simeq S^3$ for one mass; 5-D; shells lifted, not replaced |
| **tower** | $E(15)\to S^4(10)\to\mathbb{RP}^3(6)$; two fibrations |
| **curvatures** | base Ricci $\leftarrow T_+$; $E$-Weyl $=$ connection's deviation from Hopf $\leftarrow T_-$ |
| **action** | EH on the base $+$ Maxwell, Dirac, matter on the cover in $\pi^*g$; Laws II, III kinematic |
| **$G$ identity** | $GM_c/c^2\ell = \pi/2$: fibration flux through every latitude $= M_c =$ closure mass |
| **Gauss pair** | every 3-sphere: full fibration flux, zero electric flux |
| **twin, EM** | empty: $E\to0$ at the antipode; charged secondary's twin has a tidal charge |
| **foliation** | none preferred on the base; a preferred fibration of the cover, invisible below |
| **spacetime dims** | $\mathbb{R}_t\times E\,(6)\to\mathbb{R}_t\times S^4\,(5)\to\mathbb{R}_t\times\mathbb{RP}^3\,(4)$ |
| **primaries** | $k$ primaries $=$ $k$ basins $=$ $k$ bases, glued at watersheds |
| **inverted verdicts** | dielectric legal (no dilaton); $S^4$ required (Poincaré–Hopf) |
| **wall** | static theorem |
| **open** | $\mu(\rho)$; what couples to $E$; the poles |
