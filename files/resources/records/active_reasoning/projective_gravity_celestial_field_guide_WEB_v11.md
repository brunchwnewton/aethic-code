# Projective Gravity — Version 11

### Three Spaces, and the Chirality of Light

> **What this document is.** A complete, self-contained statement of the theory: arena, laws, identities, the spinor sector, the electromagnetic sector, and the construction of visible space. It assumes no earlier document. Every term is defined in Part 0; every law is stated with its equation; every result imported from an earlier version is restated in full rather than cited.
>
> **What is new relative to version 10.** Three things, each following from the one before. **(1) A third space:** a *fermionic base*, obtained from the canonical total space not by a fibration but by a free involution — the one the second order already supplies. Spinors on it are automatically Dirac spinors, with their two chiral halves at a point and at its twin. **(2) A new form for electromagnetism:** on the canonical total space it is not a 1-form but a 2-form with self-dual field strength. Six dimensions is exactly where that is possible; self-duality is a chirality for a boson; it is consumed in the reduction to four dimensions; and the same involution exchanges it that exchanges fermion chiralities. **(3) A visible space:** with both matter and light carrying a chirality that the involution flips, the seed is recovered *without* the twin being empty — matter is at both twins, but light reaches only its own sheet. This is constructed relationally, since a global sorting provably does not exist.
>
> **Tags.** **[V]** verified by computation · **[T]** cited theorem · **[D]** derived here · **[S]** sketch · **[O]** open · **[R]** retired, with reason.

---

# PART 0 — VOCABULARY AND CONVENTIONS

## 0.1 The spaces

| term | definition | dim | role |
|:--|:--|:--:|:--|
| **canonical total space** | $\mathbb{R}_t\times E$, where $E$ is the Hopf circle bundle over $S^4$ minus the secondary meridians. Carries the $u$-meridians *and* the Hopf fibers | 6 | where the full structure lives |
| **cover** | $\mathbb{R}_t\times S^4$: the canonical total space with the Hopf fibers quotiented away. Where matter and light live | 5 | matter, light |
| **gravity base** | $\mathbb{R}_t\times\mathbb{RP}^3$: the space of meridians. Where gravity lives | 4 | Law I |
| **fermionic base** | $\mathbb{R}_t\times E/\sigma$: the canonical total space modulo the involution of Part VI. Not a reduction — an identification | 6 | where a Dirac spinor is one local object |

The unqualified phrase "total space" is retired in favor of *canonical total space*. The fibration tower is

$$\mathbb{R}_t\times E\ (6)\ \longrightarrow\ \mathbb{R}_t\times S^4\ (5)\ \longrightarrow\ \mathbb{R}_t\times\mathbb{RP}^3\ (4)$$

each arrow a quotient by one circle. The fermionic base sits off this tower, mapping from the canonical total space and onto the gravity base.

## 0.2 Points and places

| term | meaning |
|:--|:--|
| **primary** | the dominant central mass $M_c$, at the south pole of $S^4$ |
| **poles** | the south pole $0$ (the primary) and the north pole $\infty$. The two points where the fibration degenerates. **Not** twins of each other; each is its own twin |
| **equator** | the 3-sphere $\chi = \pi/2$; the reference copy of space |
| **latitude** (**level 3-sphere**) | a surface $\chi = $ const in $S^4$ |
| **secondary** | any ordinary mass — a galaxy, a star, Earth — sitting on a latitude |
| **shell** | a 2-sphere of constant distance around a secondary, within its latitude |
| **twin** (**antipode**) | given $\hat n$ on a latitude, the point $-\hat n$ of the same latitude. The two are the two equatorial crossings of one meridian, and they are **one point of the gravity base**. This is the only sense of "twin" used here |
| **sheet** | one of the two meridian arcs over a gravity-base point. Exchanged by $\sigma$. There is **no global sheet label** (§X.2) — only one relative to a source and a path |

## 0.3 The two fibrations

There are exactly two, and it matters which is which.

| fibration | fibers | pairs twins? |
|:--|:--|:--|
| **meridians** (**$u$-fibers**) | fibers of $S^4\to\mathbb{RP}^3$: great circles through both poles | **yes** — a meridian crosses the equator at $\hat n$ and at $-\hat n$ |
| **Hopf circles** | fibers of $E\to S^4$: one circle over each point of the cover | **no** — two points of one Hopf circle lie over the *same* point of the cover |

The twin comes from the meridians and from nothing else.

## 0.4 Fields and quantities

| term | meaning |
|:--|:--|
| $T_\pm$ | $T_\pm(\hat n) = T(\hat n)\pm T(-\hat n)$: the even and odd parts of matter under the twin map |
| **even sector** | $T_+$; what gravity reads |
| **odd sector** | $T_-$; what the second-order connection reads |
| **jellium** | the uniform background density of the gravity base, supplied by the primary |
| **conformal factor** $\phi$ | defined by $g_3 = \phi^4g_{S^3}$; $\Omega\equiv\phi^2$ |
| **fiber length** $L_E$ | the local length scale of the Hopf circle, locked to gravity by $L_E = \Omega L^{\rm ref}$ |
| **permeability** $\mu(\rho)$ | how matter deflects the meridians in Law II without sourcing them |
| **Hopf charge** $n$ | a field's momentum around the Hopf circle; an integer |
| **flux quantum** $m_{\rm unit}$ | the mass carrying one unit of second-order flux |
| **Chern number** $N$ | $M_-/m_{\rm unit}$: the winding of $E$'s fiber around a secondary's meridian |
| **zero mode** | a field component with $n = 0$; the only kind a base detector registers |
| **twin parity** $\tau$ | $\pm1$ in $\psi(-\hat n) = \tau\psi(\hat n)$, for fields that descend to the gravity base |
| **odd chirality** | the ordinary chirality of a Weyl spinor: the eigenvalue of the Clifford volume element $\gamma_5$ |
| **even chirality** | the self-duality of a middle-degree form: whether $H = +\star H$ or $H = -\star H$ |
| **the seed** | matter sources a gravitational well at both $\pm\hat n$, while light reaches only one of them |
| **visible space** | not a fourth manifold: the canonical total space *with a basepoint*, sheets labeled by lifting light paths from a source (§X.3) |

## 0.5 Conventions

$G = c = 1$ unless restored. $\ell$ is the gravity-base radius; $\chi\in[0,\pi]$ the polar angle on $S^4$; $\hat n\in S^3$ a point of a latitude; $\theta$ the Hopf fiber angle. $\alpha$ is the second-order connection with curvature $F = d\alpha$; $B$ the electromagnetic 2-form with strength $H = dB$; $\star$ the Hodge star of the canonical total space. $\Phi$ is the Newtonian potential.

---

# PART I — THE ARENA AND THE THREE SPACES

## I.1 The cover, and why a 4-sphere [T/D]

The cover is $\mathbb{R}_t\times S^4$, with the primary $M_c$ at the south pole and its antipode at the north. Matter and light live here; gravity does not.

**The primary is compulsory.** Poincaré–Hopf: any vector field on $S^4$ has zeros of total index $\chi(S^4) = 2$, and a gradient flow with one source and one sink has index $(+1)+(+1) = 2$ — the minimum. So the fibration *must* degenerate at exactly two points, and the central mass sits at one of them. On $S^1\times S^3$ (Euler characteristic zero) a center is optional; on $S^4$ it is forced.

## I.2 The quotient, the base, and the seed [D]

The gravity base is the space of meridians, $\mathbb{RP}^3$. Each of its points is one great circle through both poles, crossing the equator at $\pm\hat n$. Gravity is defined on $\mathbb{R}_t\times\mathbb{RP}^3$ and reads the fiber average — the integral of the cover's stress-energy along the meridian — which includes both twins by construction.

> **The seed.** Matter at $(\chi_0,\hat n)$ sources the gravity base at $[\hat n]$, whose lift to the cover has wells at both $\hat n$ and $-\hat n$. Light reaches only one of them.

**This is derived, not postulated:** a great circle through the poles crosses the equator twice. The projective postulate of the earliest versions is a theorem of the arena. (Version 10 stated the seed as "nothing is at $-\hat n$." Part X refines this: matter may be at both, with light reaching one.)

## I.3 The primary is the jellium [D]

Both poles lie on **every** meridian, so $M_c$ contributes equally to every fiber average: seen from the gravity base it is uniform. The uniform background density of the Einstein static universe is the primary's column density, with value fixed by closure (§V.2).

## I.4 The three spaces, related [D]

Since $\sigma$ (Part VI) descends to the twin map on $S^4$, and the gravity base already identifies $\hat n$ with $-\hat n$, the fermionic base also maps onto the gravity base. The three form a commuting triangle with the canonical total space at the apex. **The fermionic base is not a dimensional reduction:** $\sigma$ is a free involution, so $E/\sigma$ has the same dimension as $E$; they differ in global structure, not size.

---

# PART II — THE LAWS

> ### ◆ LAW I — GRAVITY
> $$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi\,T^+_{\mu\nu}\quad\text{on }\mathbb{R}_t\times\mathbb{RP}^3,\qquad \Lambda = 1/\ell^2$$
> General relativity on the gravity base, sourced by the meridian-averaged, pair-summed stress-energy. There is no dilaton, no radion, and no extra scalar with a $1/r$ coupling, so PPN $\gamma = 1$ holds trivially.

> ### ◆ LAW II — THE FIBRATION
> $$\nabla\cdot\big(\mu(\rho)\,\nabla\Phi_u\big) = M_c\,\big[\delta^4(0) - \delta^4(\infty)\big]\quad\text{on }S^4$$
> The $u$-fibers are the gradient lines of $\Phi_u$. The poles are the only flux endpoints; all other matter enters through the permeability $\mu(\rho)$. The fibration is **kinematic**: it has no action, and nothing couples to it dynamically.

> ### ◆ LAW III — THE SECOND-ORDER CONNECTION
> $$dF = 2\pi\star J_-,\qquad J_- = \frac{\rho_-}{m_{\rm unit}}\ \text{smeared along the meridians},\qquad F = d\alpha$$
> $\alpha$ is a $U(1)$ connection on $E\to S^4$; its fiber length is locked to gravity by $L_E = \Omega L^{\rm ref}$. Kinematic.

> ### ◆ LAW IV — ELECTROMAGNETISM
> On the canonical total space, a 2-form gauge field $B_{MN}$ with 3-form strength $H = dB$, subject to self-duality:
> $$H = \star_6 H$$
> Its anti-self-dual partner is the opposite even chirality, exchanged with it by $\sigma$. Below, this reduces to ordinary Maxwell with $\epsilon = \mu_{\rm EM} = 1$ (Part VIII).

## II.1 Why Law II weaves rather than sources [D/V]

With secondary masses as additional same-sign sources of $\Phi_u$, a secondary becomes a critical point; its own field lines are repelled by the center and die at a saddle; and **no fiber through it reaches its antipode** — the twin is lost. With secondaries entering as permeability, the maximum principle forbids interior critical points: every point of $S^4$ lies on exactly one meridian from $0$ to $\infty$, a secondary sits *on* a twin-pair fiber, and the latitudes deform without pinching. In a two-dimensional test with $\mu = 7$ at a mass, seven of seven field lines launched at it passed through and continued **[V]**.

"The center has most of the mass" then reads correctly: $M_c$ sets the total flux, and the meridians are radial to the extent that $\mu$ is uniform.

## II.2 The action

$$S = \int_{\mathbb{R}_t\times\mathbb{RP}^3}\!\!d^4x\,\sqrt{-g}\,\frac{R - 2\Lambda}{16\pi G}\;+\;\int_{\mathbb{R}_t\times E}\!\!d^6x\,\sqrt{-\hat g}\,\Big[\mathcal{L}_B + \bar\Psi\big(i\Gamma^MD_M - m\big)\Psi + \mathcal{L}_{\rm matter}\Big]$$

with $\hat g$ the gravity-base metric pulled back plus the fiber parts. Varying $g$ on the base integrates matter over both fibers of each base point, so $T_+$ is the *structure of the action*, not an added rule. **Laws II and III have no action.** The constants are $G$, $\Lambda = 1/\ell^2$, the function $\mu(\rho)$, and $m_{\rm unit}$.

$\mathcal{L}_B$ is written for the self-dual 2-form with the standard caveat that a chiral form admits no simple covariant Lagrangian; Law IV is imposed as a field equation, which is sufficient here since Law IV is not varied against the metric (§VIII.7).

## II.3 No preferred foliation [D]

Law I is generally covariant on the four-manifold $\mathbb{R}_t\times\mathbb{RP}^3$. Law II has a covariant five-dimensional form with $\mu$ a function of the trace and the poles two worldlines; its static presentation is a gauge choice. What is preferred is a *fibration of the cover*, which is the theory's definition and is invisible from the gravity base.

---

# PART III — THE SECOND ORDER

## III.1 The Hopfian construction over shells [D/V]

On a latitude sits a secondary at $\hat n_0$; its shells are 2-spheres within that latitude. Each shell is the base of a Hopf 3-sphere, $S^3\to S^2$, and the union over shells and latitudes is $E$.

The Hopf lift is not a separate construction: it is the **symmetric solution of Law III** about one meridian. Over a shell of angular radius $\vartheta$,

$$F\big|_{\rm shell} = \tfrac{c}{2}\sin\vartheta\,d\vartheta\wedge d\varphi,\qquad \int_{\rm shell}F = 2\pi c,\qquad c = M_-/m_{\rm unit}$$

verified **[V]**. Many secondaries superpose; a continuous $\rho_-$ gives a smooth $J_-$ and real-valued flux.

## III.2 Why Law III requires $S^4$ [D]

In four dimensions a 2-form's source is a 1-form, and consistency $d(dF) = 0$ requires $d\star J_- = 0$: the source must be a conserved current supported on closed lines. On $S^4$ every meridian is a closed circle, so this holds automatically. On $\mathbb{R}^4$ the rays have endpoints and the law is inconsistent. **$S^4$ is what makes Law III well-posed.**

## III.3 The monopole is the meridian [T/D]

A 2-sphere cannot link a point in a four-space ($H^2(S^4\setminus\text{points}) = 0$); it links a *circle* ($H^2(S^4\setminus\text{great circle}) = \mathbb{Z}$). So the Chern class lives on the meridian through the secondary — the mass smeared along its fiber, exactly as gravity sees it. Orienting the meridian once around, its two equatorial crossings are traversed in opposite senses, giving linking numbers $+1$ at $\hat n_0$ and $-1$ at $-\hat n_0$.

**The anti-monopole at the twin is the same circle seen from the other hemisphere**, and the Chern number on the meridian through $[\hat n]$ is $\big(M(\hat n) - M(-\hat n)\big)/m_{\rm unit}$ — the odd part, by construction.

## III.4 The topology of $E$ [T]

$E$ is the circle bundle over $S^4\setminus\Gamma$, where $\Gamma$ is the graph formed by the $N$ secondary meridians through the two poles. Alexander duality gives $H^2 = \mathbb{Z}^{2N-1}$; the physical bundle has equal flux on both arcs of each meridian and so lives in $\mathbb{Z}^N$, one integer per secondary. For $N = 1$, $S^4\setminus\text{circle}\simeq S^2$ and $E\simeq S^3$.

**$S^4$ does not become anything.** $E$ is a new five-dimensional space fibered over it; each 2-shell is *lifted* to a Hopf 3-sphere, not replaced. Since every meridian contains both poles, the poles lie in $\Gamma$ and are removed from $E$'s base — which is what makes $\sigma$ act freely (§VI.2).

## III.5 The partition principle [T/V/D]

**Geometric.** A metric on a circle bundle, in coordinates adapted to the fibration, is $h_{ab}dx^adx^b + L^2(d\theta+\alpha)^2$ — base, fiber length, connection — pointwise, with no remainder and no overlap:

| level | total | base | length | connection |
|:--|--:|--:|--:|--:|
| Hopf $S^3$ over a shell | 6 | 3 | 1 | 2 |
| $E\to S^4$ | 15 | 10 | 1 | 4 |
| $S^4\setminus\{\text{poles}\}\to\mathbb{RP}^3$ | 10 | 6 | 1 | 3 |

**Physical.** Even matter $T_+$ fills the base metric and the fiber length, through Law I. Odd matter $T_-$ fills the connection, through Law III, as the Chern class and its continuous deformation. The Hopf form itself is neither — it is the arena. Four even functions from gravity, two odd from the second order, nothing left over and nothing double-counted.

**Curvature.** Base Ricci $\leftarrow T_+$. The Weyl tensor of $E$ is exactly the connection's deviation from Hopf: $C_{abcd}C^{abcd} = 0$ for the Hopf connection, and $4\epsilon^2(16 - 13\sin^2\vartheta)/3\sin^4\chi$ for a perturbation $\epsilon\sin^2\vartheta$ **[V]**.

> **The projection discards the odd half; the twist recovers it; together they see all of $T$.**

## III.6 What sees $E$ [T/D]

Light does not: the photon is the zero mode, and Kaluza–Klein charge is fiber momentum, which is spin-independent. Gravity fixes $E$'s even half and is blind to its odd half. If the flux gravitates with coupling $g_2$, it adds a Reissner–Nordström term (§V.5).

---

# PART IV — SPIN, FROM WEYL UP

## IV.1 What a Weyl spinor is, and what mass is [T]

A fermion field attaches, to every point, a short list of complex numbers. How long is not a choice: it is fixed by the dimension, because the list must represent every rotation, and bigger spaces have more. Four-dimensional spacetime: **four** complex numbers — the ordinary Dirac spinor. Six dimensions: **eight**.

In even dimensions there is one extra operation, **chirality**, which splits the list exactly in half — and the halves *never mix*, under any rotation or boost. Each half is a self-contained field: a **Weyl spinor**. Four dimensions: two and two, the left- and right-handed fields. Six: four and four. Odd dimensions: no split.

The only thing that ever couples the halves is a **mass term**:

$$\mathcal{L}_m = -m\big(\bar\psi_L\psi_R + \bar\psi_R\psi_L\big)$$

**A massless Dirac fermion is two independent Weyl fermions written side by side; mass is what ties them into one object.** Everything in Parts IV and VII elaborates this sentence.

## IV.2 Two independent signs [T]

A particle on the gravity base has a frame and a position, each carrying its own $\mathbb{Z}_2$. Since a Lie group is parallelizable, the frame bundle of $\mathbb{RP}^3 = SO(3)$ is $SO(3)\times SO(3)$, with $\pi_1 = \mathbb{Z}_2\times\mathbb{Z}_2$ and two **independent** generators:

| loop | sign | what it is |
|:--|:--|:--|
| rotate the frame by $2\pi$, position fixed | $(-1)^{2s}$ | spin — universal, present in any 3-manifold |
| carry the position once around the twin loop, frame fixed | $\tau$ | **twin parity** — the arena's own |

## IV.3 What the arena does not do [T/R]

**A $2\pi$ rotation does not move anything.** Isometries of $S^3 = SU(2)$ are $g\mapsto agb^{-1}$; those fixing a point require $a = b$, so a rotation *about a point* is a conjugation $g\mapsto aga^{-1}$. A $2\pi$ rotation is $a = -1$, and $(-1)g(-1)^{-1} = g$: **the identity map on space** **[V]**. No matter is transported anywhere.

**The antipodal map is a translation, not a rotation.** It is left multiplication by the central element $-1$ — a Clifford translation, moving every point by $\pi$ and fixing none on the equator. Calling it "a $2\pi$ rotation" conflates the two loops of §IV.2. **[R]**

**Spin does not emerge from scalars.** Peter–Weyl gives $L^2(SU(2)) = \bigoplus_jV_j\otimes V_j^*$ with $j$ half-integer, which looks like spin appearing in ordinary functions. But under rotations *about a point* — the adjoint action — each block decomposes as $V_j\otimes V_j^* = \bigoplus_{k\le2j}V_k$: **integer spins only, for every $j$** **[T]**, as it must be, since a single-valued function carries integer angular momentum. The half-integer representations live under $SU(2)_L$ alone, a group of translations. **A spinor still needs its spinor index; the arena does not supply it.** **[R]**

## IV.4 What the arena does do [T]

**The spin bundle on the cover's spatial sphere is trivial and unique.** $S^3$ is parallelizable, so spinor fields there are $\mathbb{C}^2$-valued functions with no patching. A convenience, not an emergence.

**Descent requires definite parity.** The antipodal map acts on the $j$-th Peter–Weyl block as $(-1)^{2j}$, so a field descends to $\mathbb{RP}^3$ only if built entirely from even blocks or entirely from odd ones. These are the two spin structures and the two values of $\tau$.

**Fermions cannot be uniform.** The scalar Laplacian on $S^3(\ell)$ has a zero mode, the constant; the Dirac operator does not, its spectrum being $\pm(k+\tfrac32)/\ell$. **A fermion on the closed spatial sphere has an energy floor of $3\hbar c/2\ell$; a boson can sit at zero.**

## IV.5 Twin parity, and where it is fixed [T/D]

$\tau = \pm1$ is a discrete quantum number **independent of spin and of statistics**. For two particles, $\pi_1$ of the configuration space of $\mathbb{RP}^3$ is the dihedral group $D_4$, abelianizing to $\mathbb{Z}_2\times\mathbb{Z}_2$: four sectors, of which spin–statistics fixes the exchange sign and the model must supply $\tau$.

**Where it is fixed.** The generator of $\pi_1(\mathbb{RP}^3)$ lifts to a *path* from $\hat n$ to $-\hat n$ on the cover, and that path is a meridian arc — which runs through a pole. **The twin parity is the sign a field acquires on transport through the primary.** Which species are twin-odd is open **[O]**.

## IV.6 Statistics and exclusion are untouched [T]

Finkelstein–Rubinstein: in any 3-manifold, exchanging two identical particles is *locally* homotopic to rotating one of them by $2\pi$ in place, so the exchange sign equals the frame-$2\pi$ sign, $(-1)^{2s}$. The argument is local and does not see the twin loop. **Anticommutation and the Pauli exclusion principle hold exactly as in ordinary quantum field theory.** Nothing in this arena reaches them.

## IV.7 Why a Weyl field on the canonical total space [T]

| space | Dirac | Weyl |
|:--|--:|--:|
| gravity base (4-D) | 4 complex | 2 complex |
| cover (5-D) | 4 complex | — (odd dimension) |
| canonical total space (6-D) | 8 complex | **4 complex** |

**A six-dimensional Weyl spinor has 4 complex $=$ 8 real components: exactly one four-dimensional Dirac spinor's worth.** Reduce on the Hopf circle and each mode is an ordinary four-dimensional field:

| upstairs | components | downstairs, per level |
|:--|--:|:--|
| 6-D Dirac | 8 | **two** four-dimensional Dirac fields |
| 6-D Weyl | 4 | **one** four-dimensional Dirac field |

> **With the Weyl choice, one field upstairs gives exactly one electron downstairs. With the Dirac choice it gives two identical copies, and an extra rule would be needed to delete one.**

That is the whole simplification. It is not a reframing of a spinor as a polarization vector — that cannot happen in six dimensions, since a spinor index becomes a vector index only in *eight*, through triality. It is that the Weyl box is the right size. Majorana–Weyl spinors exist only in dimensions $\equiv2\bmod8$, so not here; symplectic Majorana–Weyl exists in six but requires pairs. **The minimal chiral fermion on the canonical total space is a Weyl spinor.**

**The cost [O].** Chiral fields in even dimensions can suffer anomalies: a classical symmetry fails under quantization unless the field content is arranged so the failures cancel. In six dimensions this is restrictive, and the self-dual 2-form of Part VIII contributes to the same condition, so the two chiral sectors must be checked together. Unexamined.

---

# PART V — IDENTITIES AND THEOREMS

## V.1 The twin theorem [V]

The static operator on the closed gravity base is $\Delta_{S^3} + 3$. Its Green's function has a **same-sign** pole at the antipode; its kernel is the dipoles; so a source must have zero dipole, and **a lone mass has no static solution.** A ball at the pole has dipole $0.169\neq0$, and a numerical solve returns the kernel mode as its symptom. The twin is forced, not permitted.

## V.2 Closure and the $G$ identity [D]

The gravity base is the Einstein static universe: $\Lambda = 1/\ell^2$, $\bar\rho = 1/4\pi\ell^2$. The fibration flux through every latitude is $M_c$ — source at $0$, sink at $\infty$, nothing between — and closure fixes it:

$$\frac{GM_c}{c^2\ell} = \frac{\pi}{2}$$

$G$ is a constant of Law I, and the pair $(M_c,\ell)$ is constrained by the requirement that the gravity base be static and closed. **A constraint, not a derivation.** The electric flux through every latitude is zero.

## V.3 Law I as the fiber-length equation [V]

Weak-field statics are conformally round, $g_3 = \phi^4g_{S^3}$, and the Hamiltonian constraint linearizes about the Einstein static universe to

$$(\Delta_{S^3} + 3)\,\delta\phi = -2\pi\,\delta\rho_+$$

— the twin-theorem operator, acting on the conformal factor. The local Hopf length scale is $L_H = 2\pi\ell\phi^2$, so to first order $\delta L_H/L_H = -\Phi$ and $N\cdot L_H = $ constant: **fibers lengthen in wells by exactly the potential, and space stretches as much as time slows.** For a ball with its twin, $\phi^2 = 2.017$ at the ball's center and identically at the twin, agreeing to $10^{-11}$ **[V]**. $L_H$ is the local length scale, not a circumference.

## V.4 Weyl from the fiber length [V]

$$E_{ij} = -2\big[\nabla_i\nabla_j\phi\big]^{\rm TF},\qquad \phi = \sqrt{L_H/2\pi\ell}$$

The trace of the Hessian is fixed by the constraint and is the matter; the trace-free part is the tidal field. For Schwarzschild the eigenvalues are $(m/r^3)(1,-\tfrac12,-\tfrac12)$ — Petrov type D, with repeated principal null directions $\partial_t\pm\widehat{\nabla L_H}$, the directions of steepest fiber-length change. Type D here is forced by spherical symmetry. Beyond the weak-field static sector the fiber length is one of six metric components: magnetic Weyl lives in the shift, gravitational waves in the transverse-traceless part of the base 2-metric.

## V.5 Charged and rotating black holes [D/O]

**Electric charge.** A charged secondary has the ordinary Reissner–Nordström exterior on the gravity base, since Law IV reduces to ordinary Maxwell (§VIII.4).

**The second-order flux.** If $E$'s flux gravitates with coupling $g_2$, it adds a Reissner–Nordström-type term with an *effective magnetic charge*:

$$f(r) = 1 - \frac{2GM}{c^2r} + \frac{G\,P^2}{c^4r^2},\qquad P = g_2\,\frac{M}{m_{\rm unit}}$$

The Newtonian term is untouched; the horizon moves, $r_\pm = (GM/c^2)\big(1\pm\sqrt{1 - P^2/M^2}\big)$; and the extremality bound becomes $M^2 \geq Q^2 + P^2$. Every black hole carries $P$ proportional to its own mass, so extremality is tightened universally.

**The bound.** The repulsive $P^2/r^2$ term shifts a perihelion by $-(P/M)^2/6$ relative to general relativity's advance. Mercury agrees with general relativity to $10^{-4}$, hence

$$g_2/m_{\rm unit} = P/M < 0.024$$

Lunar laser ranging gives nothing useful ($M/r\sim10^{-11}$ at the Moon); ringdowns test $P/M$ at the $0.1$–$0.3$ level, weaker. The double pulsar can tighten it **[O]**.

**The twin of a hole.** Same mass (gravity reads $T_+$, chirality- and sign-blind); opposite second-order monopole, $-M_-/m_{\rm unit}$, by the linking number of §III.3; and no independent electromagnetic charge, since the twin's $Q^2/r^2$ term is a **tidal charge** with $\nabla\cdot E = 0$ and $E = 0$ there (§V.6). Rotation is untouched: magnetic Weyl lives in the shift, which no fiber carries (§V.4).

## V.6 Charge and the twin [V/D]

Gauss on a closed section forces a compensating charge *somewhere*, and the seed puts no *interacting* charge at the antipode. With the compensating charge wherever the other charges are, the field of a charge $Q$ is regular at the antipode and vanishes there — verified: $|E|\to0$ linearly. **The twin carries gravitational shape without electromagnetic content.** In version 10 this was read as "the twin is empty"; Part X refines it to "the twin's matter is on the other sheet."

## V.7 Orbits [V]

On the gravity base a secondary is a well in the jellium, and closed-universe orbits are retrograde-precessing rosettes: apsidal advance $1.945\pi$ per radial period at small apocenter, falling to $1.836\pi$ in the mid-disk. The kinematic pattern speed $\Omega - \kappa/2$ falls by a factor 10 across a disk where Kepler alone would give 20 — the closure term halves the winding rate of kinematic spirals. At galactic radii in the cosmic arena the closure term is $10^{-7}$ of Kepler.

## V.8 The static wall [T]

On a static geometry Killing energy is conserved and there is no redshift. This is a theorem about the arena, not a gap in it. Every route to Hubble's law within the static theory ends at the seed's own symmetry: the twin's well is *identical* to the source's, and identical wells cannot shift light between them.

---

# PART VI — THE INVOLUTION

## VI.1 Definition [D]

$$\sigma:\ (\chi,\hat n,\theta)\ \longmapsto\ (\chi,\,-\hat n,\,-\theta)$$

**Go to the twin, and conjugate the fiber.** Both halves are already in the theory: the twin map is the seed's pairing, and the fiber conjugation is the statement — established by the linking-number argument of §III.3 — that the twin carries the anti-monopole, $N\to-N$.

## VI.2 Why this involution and no other [V]

Everything turns on one determinant.

| involution | det | free? | verdict |
|:--|:--:|:--|:--|
| twin alone, $\hat n\to-\hat n$ | $+1$ | yes | orientation-**preserving** — why the gravity base is orientable |
| fiber conjugation alone, $\theta\to-\theta$ | $-1$ | **no** ($\theta = 0,\pi$ fixed) | reversing, but has fixed points |
| fiber half-turn, $\theta\to\theta+\pi$ | $+1$ | yes | orientation-**preserving** |
| **twin $\times$ conjugation** | $-1$ | yes | **orientation-reversing and free** |
| twin $\times$ half-turn | $+1$ | yes | preserving |
| full $S^4$ antipode | $-1$ | yes | reversing, but swaps the poles — identifies the primary with infinity |

The bookkeeping: $\hat n\to-\hat n$ acts on four embedding coordinates and contributes $(-1)^4 = +1$; a **reflection** of the fiber circle contributes $-1$; a **rotation** of it contributes $+1$. Only a reflection flips the orientation, and a reflection alone has fixed points. **The twin is what makes the reflection free; the reflection is what makes the twin orientation-reversing. Neither half works alone.**

The fiber half-turn is the natural rival and deserves separate mention. It is a rotation, not a reflection, so it preserves orientation; its quotient is an orientable circle bundle with doubled Chern number, keeping chirality and giving no Dirac structure. What it does give is a spin-structure choice sorting Hopf charges by parity — the same parity that decides $E$'s spin-structure count (§VII.1). A real $\mathbb{Z}_2$, a different one.

## VI.3 What $\sigma$ is, in field-theory language [D]

$\sigma$ flips **odd chirality** (by reversing orientation), flips **even chirality** (same reason — the Hodge star's sign follows the orientation), and flips the Hopf charge $n\to-n$ (by conjugating the fiber). Flipping chirality and charge together is what charge conjugation does. So $\sigma$ is a geometric realization of $C$, and "the twin carries the anti-monopole" is that same statement seen topologically.

> **One map exchanges the fermionic chirality, the bosonic chirality, and the sign of the second-order charge. They are three faces of orientation reversal.**

---

# PART VII — THE FERMIONIC BASE

## VII.1 Spinors on $E$, and how many structures [T]

$E$ is a circle bundle over $B = S^4\setminus\Gamma$, so $TE = \pi^*TB\oplus V$ with the vertical $V$ trivialized by the fiber generator; hence $w_2(E) = \pi^*w_2(S^4) = 0$ and **$E$ is a spin manifold.**

How many spin structures? $H^1(E;\mathbb{Z}_2)$. Alexander duality gives $H^1(B;\mathbb{Z}_2) = H_2(\Gamma;\mathbb{Z}_2) = 0$ since $\Gamma$ is a graph, and the Gysin sequence makes $H^1(E;\mathbb{Z}_2)$ the kernel of cup product with $e\bmod2$. **The count depends on the parity of the flux**: unique when the Chern number is odd, two when even. With $m_{\rm unit}$ a particle mass a body's Chern number is astronomically large and its parity is not a controlled datum, so whether the second order fixes $\tau$ depends on the quantization fork **[T/O]**.

## VII.2 Non-orientable, hence Pin, hence no chirality [T]

$\sigma$ is free and orientation-reversing, so $E/\sigma$ is **non-orientable**. The chirality operator on an even-dimensional manifold is the product of all the gamma matrices, and its sign depends on the orientation. A non-orientable space has no global orientation, hence **no global chirality operator**: it carries Pin structures rather than Spin, and a spinor field on it cannot be chirally projected. Equivalently, $\sigma_*$ maps $S^+$ to $S^-$.

## VII.3 The result [D]

> **A Weyl spinor on the canonical total space is a Dirac spinor on the fermionic base, with its two chiral halves at a point and at its twin.**

The Dirac mass term is the only thing coupling the chiralities, so **mass becomes a coupling between a point and its twin — local on the fermionic base, twin-connecting seen from the canonical total space.** The fermionic base is where fermion physics is ordinary; the hundred-gigaparsec separation is an artifact of describing it upstairs.

## VII.4 The twin's field is not independent [D]

A field descending to $E/\sigma$ satisfies $\Psi(\sigma x) = \sigma_*\Psi(x)$: its value at the twin is *determined*. There are not two particles; there is one field whose left-handed description sits at $\hat n$ and whose right-handed description sits at $-\hat n$. Gravity therefore reads

$$T_+ = T(\hat n) + T(-\hat n) = T_L + T_R = \text{one Dirac field's full stress-energy}$$

**No doubling.** The two things at the two twins are two descriptions of one object.

## VII.5 The Dirac field's extra structure [D]

Fourier-decompose along the Hopf fiber, $\Psi = \sum_n\psi_n(x)e^{in\theta}$:

| datum | what it becomes below |
|:--|:--|
| $n$ | the Hopf charge: the mode couples to $\alpha$ with charge $n$ |
| $\lvert n\rvert/L_E$ | a Kaluza–Klein mass |
| $n = 0$ | the ordinary Dirac field — Hopf-neutral |

**Chirality becomes motion along the fiber.** In five dimensions the Clifford algebra needs a fifth gamma matrix, and it is forced: $\Gamma^4 = \pm i\gamma^0\gamma^1\gamma^2\gamma^3 = \pm\gamma_5$. **The fifth gamma matrix is the four-dimensional chirality operator**, so the five-dimensional Dirac equation reads $(i\gamma^\mu\partial_\mu + i\gamma_5\partial_u - m)\Psi = 0$: momentum along the meridian couples through $\gamma_5$, and the four-dimensional mass is $\sqrt{m^2+p_u^2}$.

**The mass tower is set by gravity.** Since $L_E = \Omega L^{\rm ref}$ and $\delta L/L = -\Phi$, $\delta m_n/m_n = +\Phi$: Kaluza–Klein masses are **lower in gravitational wells** — by $7\times10^{-10}$ at Earth's surface, $0.2$ at a neutron star. The $n = 0$ mode has no such mass, so the ratio $m_n/m_e$ varies with the potential: a local-position-invariance violation confined to the hidden sector, unobservable because $n\neq0$ is invisible to base detectors (Part IX).

## VII.6 What is not different [D]

Statistics, exclusion, and the Lorentz structure. A Dirac spinor is $(\tfrac12,0)\oplus(0,\tfrac12)$ of $SL(2,\mathbb{C})$, and the boosts are not in $SU(2)_{\rm spatial}$. **The spinor index, the Clifford algebra, the boosts, and the exclusion principle are inputs from ordinary quantum field theory.**

---

# PART VIII — ELECTROMAGNETISM AND EVEN CHIRALITY

## VIII.1 Why a 2-form, and why six dimensions [T]

For spinors, chirality is the eigenvalue of the Clifford volume element. Tensors have no such operator — but **middle-degree forms have the Hodge star**, which plays the identical role: it squares to $\pm1$, and where it squares to $+1$ there is a real split into self-dual and anti-self-dual halves. The condition is $\star^2 = (-1)^{p(n-p)+t} = +1$ with $p = n/2$.

| field, dimension, signature | $\star^2$ | verdict |
|:--|:--:|:--|
| 4-D Lorentzian, 2-form $F$ | $-1$ | no real split |
| 6-D Euclidean, 3-form | $-1$ | no real split |
| **6-D Lorentzian, 3-form $H$** | $+1$ | **real self-dual / anti-self-dual split exists** |
| any dimension, 1-form $A$ | — | not middle degree: no self-duality ever |

**Six-dimensional Lorentzian is exactly where a gauge field can be chiral** — the dimension of the canonical total space. A 1-form, the photon as ordinarily written, can never carry this index, which is why the structure must be placed upstairs on a 2-form.

## VIII.2 The reduction: exactly one photon [T]

| component | gives | dof |
|:--|:--|:--:|
| $B_{\mu\nu}$ | a 4-D 2-form, dual to a scalar | 1 |
| $B_{\mu u}$ | a 4-D vector $A_\mu$ — **the photon** | 2 |
| $B_{\mu\theta}$ | a 4-D vector $\tilde A_\mu$ — its magnetic dual | 2 |
| $B_{u\theta}$ | a 4-D pseudoscalar | 1 |

Unconstrained total: 6, which is $\binom42$ **[V]**. Self-duality relates the $(\mu\nu u)$ and $(\mu\nu\theta)$ components:

$$H_{\mu\nu u} = \tfrac12\epsilon_{\mu\nu\rho\sigma}H^{\rho\sigma}{}_\theta \qquad\Longleftrightarrow\qquad F = \star_4\tilde F$$

so $\tilde A$ is not independent — it is $A$'s magnetic dual. Three degrees of freedom survive: **one photon and one scalar.**

## VIII.3 Charge is winding [T/D]

A $p$-form couples minimally to a $(p-1)$-brane, so a 2-form couples to **strings**. A string wrapping the meridian looks, from four dimensions, like a point particle charged under $A_\mu = B_{\mu u}$; one wrapping the Hopf circle is charged under $\tilde A_\mu$, hence magnetically under $A$.

$$\textbf{electric charge} = \text{winding on the meridian},\qquad \textbf{magnetic charge} = \text{winding on the Hopf circle}$$

The meridian *is* the passage route for electric flux — as the cycle a charge winds rather than a field line it travels. And the two windings are exchanged by self-duality, which $\sigma$ flips: **electric–magnetic duality is orientation reversal, the same operation that flips fermion chirality.**

## VIII.4 What survives below [D]

Ordinary Maxwell: $F = dA$, $\epsilon = \mu_{\rm EM} = 1$, light on null geodesics. The photon comes from $B_{\mu u}$, which carries no Hopf index, so it is the $n = 0$ mode and remains **Hopf-neutral**. Total charge on the compact cover is zero by Gauss. The self-duality is gone, since a four-dimensional 1-form has no middle-degree duality. **Every electromagnetic result of version 10 survives; what is added is the upstairs chirality and the charge–winding identification.**

## VIII.5 The leftover scalar is an axion [D]

$B_{u\theta}$ is a component of a 2-form along two *spatial* directions, so it reduces to a **pseudoscalar**. Pseudoscalars couple derivatively, $\partial_\mu a\,\bar\psi\gamma^\mu\gamma_5\psi$, or topologically, $a\,F\tilde F$ — neither producing a static $1/r$ potential between unpolarized masses.

> **It produces no fifth force and does not spoil PPN $\gamma$** — unlike the radion of versions 2 through 5, which was a true scalar with a direct $1/r$ coupling and required the entire winding-stabilization apparatus to survive the solar system. Moving electromagnetism to a 2-form adds a massless field *for free*.

## VIII.6 Even and odd chirality, side by side

| | odd chirality (fermions) | even chirality (light) |
|:--|:--|:--|
| carried by | a Weyl spinor | a self-dual 2-form |
| defined by | the eigenvalue of $\gamma_5$ | whether $H = +\star H$ or $H = -\star H$ |
| exists when | the dimension is even | the form is middle degree and $\star^2 = +1$ |
| in the canonical total space | yes: 4 complex components | yes: $\star^2 = +1$ on 3-forms |
| in the gravity base | **survives** — a fermion is still a fermion | **lost** — consumed relating the two vectors |
| flipped by $\sigma$ | yes | yes |
| visible to gravity | via $T_+$, chirality-blind | via $T_{\mu\nu}$, helicity-blind |

The asymmetry in the fifth row is the point, and it is not imposed: a spinor's chirality survives because spinors exist in every dimension and the operator descends; a form's self-duality does not, because the middle degree changes when the dimension does.

## VIII.7 What must be rechecked [O]

Whether ordinary point-particle charge is realizable as string winding, and whether winding quantization matches charge quantization. Whether the self-dual 2-form's lack of a simple covariant Lagrangian obstructs anything, given that Law IV is imposed as a field equation. And the joint anomaly condition with the Weyl fermions (§IV.7).

---

# PART IX — DETECTION, AND THE VISIBLE SPACE

## IX.1 The base-resolution principle

> ### ◆ THE BASE-RESOLUTION PRINCIPLE
> A detector is a base object. It can record base position and base direction, within its resolution, and nothing else. Two paths in the canonical total space that end at terminal points projecting to the same base point, and arrive with directions whose base projections lie within the detector's resolution, **cannot be distinguished by the detector.** They contribute to one amplitude.

**Why it is a theorem [D].** A fiber datum is, by definition of the quotient, invariant under the fiber action, hence not a function on the base, hence not recordable. The fiber is unresolvable because the base is a quotient — the same fact that makes gravity blind to it.

**What a detector sees [V].** For a field of fiber charge $n$, terminal points separated by $\Delta$ contribute $e^{in\Delta}$, and $\int_0^{2\pi}e^{in\Delta}d\Delta = 2\pi\delta_{n0}$. Zero modes add coherently; charged modes average to zero — invisible, not decohered. **"The base sees zero modes" is what a base detector can register, not an assumption about matter.**

**The twist, through paths [T].** Two base paths enclosing $\Sigma$ arrive with fiber phases differing by $n\int_\Sigma F$; the detector cannot resolve the fiber velocities that would distinguish them; they interfere, and the fringe shifts by the flux. This is the Aharonov–Bohm effect. For the photon $n = 0$, and there is no fringe.

## IX.2 Two corrections to the naive picture of sheets [V/T]

**The twin map fixes the poles, so there are no hemispheres.** A point of $S^4$ is $x = \cos\chi\,e_5 + \sin\chi\,\hat n$, and the twin map sends $\hat n\to-\hat n$ at fixed $\chi$. At $\chi = 0$ and $\pi$ the point does not move: **the primary is its own twin, and so is infinity** **[V]**. North and south are never exchanged. (Consistent with $\sigma$ acting freely on $E$: the poles lie on every secondary meridian and are already removed.)

**There is no global sheet label.** To say "this arc is the positive sheet, everywhere" is to give a **section** of the double cover $E\to E/\sigma$. A covering map admits a section exactly when its total space is disconnected; $E$ is a circle bundle over a connected base, hence connected. **No section exists** **[T]**. The obstruction is precisely $\pi_1(\mathbb{RP}^3) = \mathbb{Z}_2$:

> **The same $\mathbb{Z}_2$ that creates the twin structure forbids sorting the sheets globally.**

## IX.3 Visible space is relational [D]

A covering map has no global section, but it always has **unique path lifting**: given $s\in E$ and a path $\gamma$ in $E/\sigma$ beginning at $\pi(s)$, there is exactly one lift beginning at $s$ **[T]**. That is strictly weaker than a section, and it is all the construction needs.

> ### ◆ VISIBLE SPACE, RELATIVE TO A SOURCE
> Fix a source event $s\in E$ — a point together with its sheet. For each light path $\gamma$ emitted from $\pi(s)$, lift $\gamma$ starting at $s$; the lift terminates at one of the two preimages of its endpoint. That endpoint is
> - **on the source's sheet** if the lift lands where the local matter's chirality matches the light's — interaction occurs, matter is seen;
> - **the opposite sheet** if it lands on the other preimage — no interaction, and the point reads as **void**.

**Visible space is therefore not a fourth manifold. It is the canonical total space with a basepoint.** The relational structure *is* the basepoint; path lifting makes the labeling well defined without the section that does not exist. This is the precise sense in which a single point of the canonical total space is decoupled from a single point of visible space: what a point is, visually, depends on where it stands relative to the source of the light passing through it.

## IX.4 What an observer sees [D]

Each photon travels a definite path, so its lift is definite, so its sheet is definite. **An observer has a definite sky, assembled photon by photon, with no global choice needed.**

A visible source sits at $\hat m$; its twin at $-\hat m$ is a **different sky direction**. Light from the twin arrives on the opposite sheet and does not interact. But gravity reads $T_+$ and is sourced by both.

> **The observer infers mass in a direction where they see nothing.** Gravitational attraction from a direction with no light in it — the seed, stated observationally, with matter present at both twins.

## IX.5 The monodromy [D]

Two sources on opposite sheets assign opposite labels — not an inconsistency, but the same physics in opposite-handed labelings. What is absolute is the *relation*: whether a given light path's endpoint matches or does not. Carrying light around a loop generating $\pi_1(\mathbb{RP}^3)$ returns it on the other sheet, so **visibility is path-dependent in principle**. That loop is $\pi\ell/c = 646$ Gyr at $\ell = 63$ Gpc, forty-seven times the age of the universe.

## IX.6 What the construction still needs [O]

**If the chirality-matching rule is about individual particle handedness**, it is a maximally parity-violating electromagnetism. Atomic parity violation in cesium is a weak-force effect of relative size $10^{-11}$, matching the Standard Model to half a percent; a chiral photon would make it order one. **Excluded by roughly eleven orders of magnitude.**

**If it is about sheets rather than handedness** — our light couples normally to both chiralities of matter *on our sheet*, and not at all to the other — local physics is unchanged and the bound does not apply. This is the version that can work.

**The obstacle is mass.** A massive fermion's chirality oscillates at $mc^2/\hbar$, which is $8\times10^{20}$ Hz for an electron. If chirality itself were the sheet label, a massive particle would change sheets that fast. Two ways out: **(a)** the mass term *is* the twin coupling (§VII.3), so chirality change is not motion but description at the other end; **(b)** the sheet label is **topological rather than chiral** — which lift of the path the light's history followed — with chirality merely correlated. **(b) is what §IX.3 naturally supplies**, since path lifting is a labeling on histories rather than states. Making it a *coupling* rather than a bookkeeping device is the unfinished work.

## IX.7 What is doing the work regardless [V]

Light takes $646$ Gyr to cross to the twin against 13.8 Gyr of cosmic age. **The twin is unobserved whether it is empty or full, and whether or not any coupling rule holds.** Part IX is a construction about what the theory *says*, to be held to a structural standard rather than an observational one.

---

# PART X — TWO TESTS

## X.1 The golf ball [V/D]

A golf ball hovering in a vacuum chamber on Earth's surface: does it enclose its own fibers?

**Topologically, yes.** Law III is linear, $F = F_\oplus + F_g$, and for a small sphere around the ball $\frac{1}{2\pi}\int F = M_g/m_{\rm unit}$ exactly. Chern numbers add and are localized; Earth cannot smear away an integer.

**Geometrically, Earth dominates.** The flux falls as $N/2r^2$ — the same law as gravity — and the ball's field exceeds Earth's only inside $r = R_\oplus\sqrt{M_g/M_\oplus} = 0.56\,\mu$m, which is precisely the ball's gravitational neutral point, since both fields are sourced by mass with the same falloff.

**The quantization fork decides whether there is any winding.** With $m_{\rm unit} = m_p$ the ball winds $2.7\times10^{25}$ times and Earth $3.6\times10^{51}$; with $m_{\rm unit}\sim10^{14}M_\odot$ both wind zero times and the second order is absent from the solar system.

A spherically symmetric chamber contributes nothing inside, by the shell theorem, which applies because the flux obeys an inverse-square law. And nothing in the laboratory detects either answer: the photon is Hopf-neutral.

## X.2 The Machian direction [T/D/V]

*The proposal: a body fully enclosing its own fibers should be a rescaled copy of any other such body, so an isolated golf ball would have Earth's compactness while one near Earth has general relativity's, with the Newtonian force invariant.*

**What is already true.** Vacuum general relativity has the symmetry $(g,M)\to(\lambda^2g,\lambda M)$: every Schwarzschild exterior *is* a rescaled copy of every other, with mass as the scale. The Hopf bundle is one universal object with $N = M/m_{\rm unit}$ as its only body-dependent datum. So "isomorphic fibers up to scale" is true and yields nothing new — the scale it fixes is mass, not size, and compactness $r_s/R$ ($1.4\times10^{-9}$ for Earth, $3.2\times10^{-27}$ for a golf ball) is untouched.

**The proposal as stated is inconsistent [D].** Giving the isolated ball Earth's compactness means $r_s\to4\times10^{17}r_s$ with $GM$ fixed. But $r_s = 2GM/c^2$: horizon and Newtonian coupling are **one number** whenever the exterior has a single source. Separating them requires the near field to be sourced by something the far field does not see.

**The realizable form is already present [D].** Law III's flux is such a second source (§V.5). And the flux energy $|F_\oplus + F_g|^2$ contains a **cross term** $2F_\oplus\cdot F_g$ — a source at the ball that exists only when Earth is present, $1.5\times10^9$ times the ball's own term at its surface. In isolation only the self term survives. **The ball's near field genuinely differs alone and near Earth — a Machian effect from the dynamic sector with no new law**, bounded by Mercury at $\delta r_s/r_s < 3\times10^{-4}$.

**A local Mach relation fails [V].** Reading $GM/c^2\ell = \pi/2$ with $\ell$ a body's sphere of influence gives $5\times10^{11}G$ for Earth and $3\times10^{22}G$ for the golf ball. The Mach relation closes a *universe*; spheres of influence are not closed universes.

**Emergent $G$ [D].** $G$ is emergent if and only if mass has a $G$-free definition. General relativity has none — ADM and Komar masses are defined *through* $G$. The Hamiltonian constraint $H^2 = \tfrac{8\pi G}{3}\rho - \tfrac{1}{a^2} + \tfrac{\Lambda}{3}$ holds on every slice of every spacetime and is the invariant extending beyond the static case, but it constrains the product $G\rho$ and cannot separate the factors. The only $G$-free mass the program has produced is the fiber momentum $p_u = m$ of the null-fiber reading, set aside in this version. **On a spacelike $u$, $G$ is a constant constrained by closure, and emergence is not available.**

---

# PART XI — SET ASIDE, RETIRED, OPEN

## XI.1 Set aside: recorded, not assumed

The null fiber and its Bondi reading; the Eisenhart–Bargmann lift and the identification of the fiber coordinate with the classical action; the Lorentzian real slice of the complexified cover and its de Sitter geometry; the fiber as quantum phase; Law I as semiclassical; the twin as a superposition branch; the fiber product as "visual space." Each is a coherent branch; none is part of version 11.

## XI.2 Retired, with reasons

| item | reason |
|:--|:--|
| compactification, dilaton, winding, $G_4$ from $G_5$, sub-millimeter scale | dynamical-reading machinery; the kinematic reading has no radion |
| the dielectric coupling $\epsilon(T)$ as an electromagnetic law | it varied $\alpha_{\rm fine}$ through the dilaton; legal now only as Law II's $\mu(\rho)$, which touches nothing electromagnetic |
| monopoles at points | on $S^4$ they are meridians, and the descent is a linking number |
| the twin's opposite *electric* charge | assumed the $\cot\chi$ Green's function, which places an interacting charge where the seed puts none |
| Tully–Fisher from closure, as a result about our universe | needs $\ell\approx8$ kpc; a toy for the reflection-sky arena |
| the half-orbit selection of spiral arms by chirality | chirality oscillates at $mc^2/\hbar$ and cannot label macroscopic objects |
| spin emerging from scalars on $SU(2)$ | rotations about a point are conjugations, under which all functions carry integer angular momentum (§IV.3) |
| "a $2\pi$ rotation is the antipodal map" | conjugation by $-1$ is the identity; the antipodal map is a translation (§IV.3) |
| "northern light / southern light" | the twin map fixes the poles, and no global sheet label exists (§IX.2) |
| the Machian rescaling as stated | inconsistent (§X.2) |
| electromagnetism as a 1-form on the cover | replaced by the self-dual 2-form, which has an even chirality a 1-form cannot carry (§VIII.1) |

## XI.3 Open

1. **The coupling rule of §IX.6**, in form (b): make the path-lifted sheet label a *coupling* rather than a bookkeeping device. The most substantive unfinished work.
2. **Point charges as windings** (§VIII.7), and whether winding quantization matches charge quantization.
3. **Anomalies:** the six-dimensional Weyl fermions and the self-dual 2-form must cancel together (§IV.7).
4. **The Pin structure:** which of Pin$^\pm$ the fermionic base admits, and whether the choice is physical.
5. **Reading (a) versus (b) of the seed:** whether fermions are $\sigma$-equivariant or merely use the fermionic base to define the spinor bundle.
6. **The quantization fork:** $m_{\rm unit}$ a particle mass or $\sim10^{14}M_\odot$.
7. **$g_2/m_{\rm unit}$:** below $0.024$ from Mercury; the double pulsar can tighten it.
8. **$\mu(\rho)$:** nothing selects it; observable only through footprint dilation, bounded by 4.
9. **Twin parity assignments:** which species are twin-odd.
10. **Emergent $G$:** requires a $G$-free definition of mass (§X.2).
11. **Inherited:** the AdS uplift; the two arenas; the literature review.

---

## Reference card, version 11

| topic | statement |
|:--|:--|
| **canonical total space** | $\mathbb{R}_t\times E$, 6-D: time, $S^4$ with its meridians, and the Hopf fibers |
| **gravity base** | $\mathbb{R}_t\times\mathbb{RP}^3$, 4-D; Law I |
| **fermionic base** | $\mathbb{R}_t\times E/\sigma$, 6-D; an identification, non-orientable |
| **arena** | primary at the south pole, forced by $\chi(S^4) = 2$; latitudes the level sets |
| **Law I** | $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T^+_{\mu\nu}$, $\Lambda = 1/\ell^2$; $\gamma = 1$ trivially |
| **Law II** | $\nabla\cdot(\mu\nabla\Phi_u) = M_c[\delta(0)-\delta(\infty)]$; meridians; weaves, never captures |
| **Law III** | $dF = 2\pi\star J_-$; $L_E = \Omega L^{\rm ref}$; kinematic |
| **Law IV** | self-dual 2-form $H = dB = \star_6H$; reduces to one photon $+$ one axion |
| **$G$ identity** | $GM_c/c^2\ell = \pi/2$: a constraint, not a derivation |
| **twin theorem** | $(\Delta+3)$; dipole kernel; a lone mass has no static solution |
| **fiber reading** | $L_H = 2\pi\ell\phi^2$; $\delta L/L = -\Phi$; $E_{ij} = -2[\nabla\nabla\phi]^{\rm TF}$; PNDs along $\nabla L$ |
| **black holes** | $f = 1 - 2GM/c^2r + GP^2/c^4r^2$, $P = g_2M/m_{\rm unit}$; $M^2\ge Q^2+P^2$; Mercury: $P/M<0.024$ |
| **partition** | base $+$ length $+$ connection; even fills the first two, odd the third; $E$-Weyl $=$ the twist |
| **the involution** | $\sigma:(\chi,\hat n,\theta)\mapsto(\chi,-\hat n,-\theta)$; det $=-1$; twin makes it free, reflection makes it reversing |
| **what $\sigma$ is** | one map flipping odd chirality, even chirality, and the second-order charge |
| **Dirac from Weyl** | chiral halves at twin points; mass is the twin coupling, local downstairs |
| **why Weyl** | 6-D Weyl $=$ 4 complex $=$ 8 real $=$ exactly one 4-D Dirac; no phantom duplicate |
| **charge** | electric $=$ meridian winding; magnetic $=$ Hopf winding; exchanged by $\sigma$ |
| **the axion** | pseudoscalar, derivative coupling, no fifth force — unlike the retired radion |
| **even vs odd** | fermion chirality survives the quotient; form self-duality cannot |
| **detection** | which-path is base-only; zero modes add; $n\neq0$ invisible; Aharonov–Bohm through paths |
| **no global sort** | $E\to E/\sigma$ is a connected double cover: no section; the twin's $\mathbb{Z}_2$ forbids it |
| **visible space** | the canonical total space with a basepoint; sheets labeled by lifting light paths |
| **the seed** | matter at both twins; gravity sees all, light sees half; mass inferred from a dark direction |
| **golf ball** | winds $M_g/m_{\rm unit}$ times; Earth dominates beyond $0.56\,\mu$m |
| **Machian** | literal form inconsistent; the cross term is the realizable form, $<3\times10^{-4}$ |
| **emergent $G$** | requires $G$-free mass; only the set-aside null fiber supplies one |
| **regardless** | $\pi\ell/c = 646$ Gyr: the twin is unobserved either way |
