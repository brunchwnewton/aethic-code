# Projective Gravity — Version 10

### The Complete Statement

> **What this document is.** A self-contained statement of the theory: arena, laws, identities, and the spinor sector. It assumes no earlier document. Every term is defined in Part 0, every law is stated with its equation, and results imported from earlier versions are restated in full rather than cited.
>
> **Where it branches.** From version 6 — the last version before the null-fiber and Wick-rotation experiments — with one addition from version 9: the principle that which-path information exists only on the base. Everything else from versions 7 through 9 is recorded in Part X and not assumed.
>
> **Tags.** **[V]** verified by computation · **[T]** cited theorem · **[D]** derived here · **[S]** sketch · **[O]** open · **[R]** retired, with reason.

---

# PART 0 — VOCABULARY AND CONVENTIONS

## 0.1 The three spaces

| term | what it is | dimension |
|:--|:--|:--|
| **cover** | $\mathbb{R}_t\times S^4$. Where matter and light live. Gravity does not live here. | 5 |
| **base** | $\mathbb{R}_t\times\mathbb{RP}^3$, the space of meridians. Where gravity lives. | 4 |
| **second-order total space** $E$ | a circle bundle over $S^4$ (minus the secondary meridians), carrying the odd sector | 5 spatial, 6 with time |

The tower is $\mathbb{R}_t\times E\;(6)\;\to\;\mathbb{R}_t\times S^4\;(5)\;\to\;\mathbb{R}_t\times\mathbb{RP}^3\;(4)$, each arrow a quotient by one circle.

## 0.2 Points and places

| term | meaning |
|:--|:--|
| **primary** | the dominant central mass $M_c$, at the south pole of $S^4$ |
| **poles** | the south pole $0$ (the primary) and the north pole $\infty$ (its antipode on $S^4$). The two points where the fibration degenerates. **Not** twins of each other in the sense below |
| **equator** | the 3-sphere $\chi = \pi/2$ of $S^4$; the reference copy of space |
| **latitude** (or **level 3-sphere**) | a surface $\chi = $ const in $S^4$; a 3-sphere |
| **secondary** | any ordinary mass — a galaxy, a star, Earth — sitting on a latitude |
| **shell** | a 2-sphere of constant distance around a secondary, within its latitude |
| **twin** (or **antipode**) | given a point $\hat n$ of a latitude, the point $-\hat n$ of the same latitude. The two are the two equatorial crossings of one meridian, and they are **one point of the base**. This is the only sense of "twin" used in this document |

## 0.3 The two fibrations

There are exactly two, and it matters which is which.

| fibration | fibers | pairs twins? |
|:--|:--|:--|
| **meridians** (also **$u$-fibers**) | fibers of $S^4\to\mathbb{RP}^3$: great circles through both poles | **Yes.** A meridian crosses the equator at $\hat n$ and at $-\hat n$. This is where the twin comes from |
| **Hopf circles** | fibers of $E\to S^4$: one circle over each point of the cover | **No.** Two points of one Hopf circle sit over the *same* point of the cover |

## 0.4 Field vocabulary

| term | meaning |
|:--|:--|
| **$T_\pm$** | $T_\pm(\hat n) = T(\hat n)\pm T(-\hat n)$: the even and odd parts of matter under the twin map |
| **even sector** | $T_+$; what gravity reads |
| **odd sector** | $T_-$; what the second-order connection reads |
| **jellium** | the uniform background density of the base, supplied by the primary |
| **conformal factor** $\phi$ | defined by $g_3 = \phi^4g_{S^3}$; $\Omega\equiv\phi^2$ |
| **fiber length** $L_E$ | the local length scale of the Hopf circle, locked to gravity by $L_E = \Omega L^{\rm ref}$ |
| **permeability** $\mu(\rho)$ | how matter deflects the meridians in Law II, without sourcing them |
| **Hopf charge** $n$ | a field's momentum around the Hopf circle; an integer |
| **flux quantum** $m_{\rm unit}$ | the mass carrying one unit of second-order flux |
| **Chern number** $N$ | $M_-/m_{\rm unit}$: the winding of $E$'s fiber around a secondary's meridian |
| **zero mode** | a field component with $n = 0$; the only kind a base detector can register |
| **twin parity** $\tau$ | $\pm1$ in $\psi(-\hat n) = \tau\psi(\hat n)$, for fields that descend to the base |
| **the seed** | matter at $\hat n$ sources a gravitational well at both $\pm\hat n$, while nothing is at $-\hat n$ |

## 0.5 Conventions

$G = c = 1$ unless restored. $\ell$ is the base radius; $\chi\in[0,\pi]$ the polar angle on $S^4$; $\hat n\in S^3$ a point of a latitude. $\alpha$ is the second-order connection with curvature $F = d\alpha$. $\Phi$ is the Newtonian potential. Spinor conventions are stated where used (Part V).

---

# PART I — THE ARENA

## I.1 The cover, and why a 4-sphere [T/D]

The cover is $\mathbb{R}_t\times S^4$, with the primary $M_c$ at the south pole and its antipode at the north. Matter and light live here.

**The primary is compulsory.** Poincaré–Hopf: any vector field on $S^4$ has zeros of total index $\chi(S^4) = 2$, and a gradient flow with one source and one sink has index $(+1) + (+1) = 2$ — the minimum. So the fibration *must* degenerate at exactly two points, and the central mass sits at one of them. On $S^1\times S^3$ ($\chi = 0$) a center is optional; on $S^4$ it is forced.

## I.2 Law II and the meridians [D/V]

> ### ◆ LAW II — THE FIBRATION
> $$\nabla\cdot\big(\mu(\rho)\,\nabla\Phi_u\big) = M_c\,\big[\delta^4(0) - \delta^4(\infty)\big]$$
> The $u$-fibers are the gradient lines of $\Phi_u$ on $S^4$. The poles are the only flux endpoints; all other matter enters through the permeability $\mu(\rho)$. The fibration is **kinematic**: it has no action, and nothing couples to it dynamically.

**Why all matter weaves and only the poles source.** With secondary masses as additional same-sign sources, a secondary becomes a critical point of $\Phi_u$; its own lines are repelled by the center and die at a saddle; and no fiber through it reaches its antipode — **the twin is lost.** With secondaries entering as permeability, the maximum principle forbids interior critical points: every point of $S^4$ lies on exactly one meridian from $0$ to $\infty$, a secondary sits *on* a twin-pair fiber, and the latitudes deform without pinching. In a two-dimensional test with $\mu = 7$ at a mass, seven of seven field lines launched at it passed through and continued **[V]**.

"The center has most of the mass" then reads correctly: $M_c$ sets the total flux, and the meridians are radial to the extent that $\mu$ is uniform.

## I.3 The quotient and the seed [D]

The base is the space of meridians: $\mathbb{RP}^3$. Each of its points is one great circle through both poles, crossing the equator at $\pm\hat n$. Gravity is defined on $\mathbb{R}_t\times\mathbb{RP}^3$ and reads the fiber average — the integral of the cover's stress-energy along the meridian — which includes both twins by construction.

> **The seed.** Matter at $(\chi_0,\hat n)$ sources the base at $[\hat n]$, whose lift to the cover has wells at both $\hat n$ and $-\hat n$. Nothing is at $-\hat n$. Blindness to which ray, not crossing between them.

**This is derived, not postulated:** a great circle through the poles crosses the equator twice. The projective postulate of the earliest versions is a theorem of the arena.

## I.4 The primary is the jellium [D]

Both poles lie on **every** meridian, so $M_c$ contributes equally to every fiber average: seen from the base it is uniform. The uniform background density of the Einstein static universe is the primary's column density, and its value is fixed by closure (§IV.2).

---

# PART II — THE LAWS

> ### ◆ LAW I — GRAVITY
> $$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi\,T^+_{\mu\nu}\quad\text{on }\mathbb{R}_t\times\mathbb{RP}^3,\qquad \Lambda = 1/\ell^2$$
> General relativity on the quotient, sourced by the meridian-averaged, pair-summed stress-energy. There is no dilaton, no radion, and no extra scalar, so PPN $\gamma = 1$ holds trivially.

> ### ◆ LAW II — THE FIBRATION
> As §I.2.

> ### ◆ LAW III — THE SECOND-ORDER CONNECTION
> $$dF = 2\pi\star J_-,\qquad J_- = \frac{\rho_-}{m_{\rm unit}}\ \text{smeared along the meridians},\qquad F = d\alpha$$
> $\alpha$ is a $U(1)$ connection on $E\to S^4$; its fiber length is locked to gravity by $L_E = \Omega L^{\rm ref}$. Kinematic.

> ### ◆ LAW IV — ELECTROMAGNETISM
> Maxwell on $\mathbb{R}_t\times S^4$ with $\epsilon = \mu_{\rm EM} = 1$. The cover is compact, so total charge on it is zero. The photon is the zero mode on every fiber and couples to none of them.

## II.1 The action

$$S = \int_{\mathbb{R}_t\times\mathbb{RP}^3}\!\!d^4x\,\sqrt{-g}\,\frac{R - 2\Lambda}{16\pi G}\;+\;\int_{\mathbb{R}_t\times S^4}\!\!d^5x\,\sqrt{-\hat g}\,\Big[-\tfrac14\mathcal{F}_{MN}\mathcal{F}^{MN} + \bar\Psi\big(i\Gamma^MD_M - m\big)\Psi + \mathcal{L}_{\rm matter}\Big]$$

with $\hat g = \pi^*g + (\text{fiber part})$, the cover metric being the base metric pulled back plus the spindle factor over the latitudes. Varying $g$ on the base integrates matter over both fibers of each base point, so $T_+$ is the *structure of the action*, not an added rule. **Laws II and III have no action.** The constants are $G$, $\Lambda = 1/\ell^2$, the function $\mu(\rho)$, and $m_{\rm unit}$.

## II.2 No preferred foliation [D]

Law I is generally covariant on the four-manifold $\mathbb{R}_t\times\mathbb{RP}^3$. Law II has a covariant five-dimensional form with $\mu$ a function of the trace and the poles two worldlines; its static presentation is a gauge choice. What is preferred is a *fibration of the cover*, which is the theory's definition and is invisible from the base.

---

# PART III — THE SECOND ORDER

## III.1 The Hopfian construction over shells [D/V]

On a latitude sits a secondary at $\hat n_0$; its shells are 2-spheres within that latitude. Each shell is the base of a Hopf 3-sphere, $S^3\to S^2$, and the union over shells and latitudes is $E$.

The Hopf lift is not a separate construction: it is the **symmetric solution of Law III** about one meridian. Over a shell of angular radius $\vartheta$,

$$F\big|_{\rm shell} = \tfrac{c}{2}\sin\vartheta\,d\vartheta\wedge d\varphi,\qquad \int_{\rm shell}F = 2\pi c,\qquad c = M_-/m_{\rm unit}$$

verified **[V]**. Many secondaries superpose. A continuous $\rho_-$ gives a smooth $J_-$ and real-valued flux.

## III.2 Why Law III requires $S^4$ [D]

In four dimensions a 2-form's source is a 1-form, and consistency $d(dF) = 0$ requires $d\star J_- = 0$: the source must be a conserved current, supported on closed lines. On $S^4$ every meridian is a closed circle, so this holds automatically. On $\mathbb{R}^4$ the rays have endpoints and the law is inconsistent. **$S^4$ is what makes Law III well-posed.**

## III.3 The monopole is the meridian [T/D]

A 2-sphere cannot link a point in a four-space ($H^2(S^4\setminus\text{points}) = 0$); it links a *circle* ($H^2(S^4\setminus\text{great circle}) = \mathbb{Z}$). So the Chern class lives on the meridian through the secondary — the mass smeared along its fiber, exactly as gravity sees it. Orienting the meridian once around, its two equatorial crossings are traversed in opposite senses, giving linking numbers $+1$ at $\hat n_0$ and $-1$ at $-\hat n_0$.

**The anti-monopole at the twin is the same circle seen from the other hemisphere**, and the Chern number on the meridian through $[\hat n]$ is $\big(M(\hat n) - M(-\hat n)\big)/m_{\rm unit}$ — the odd part, by construction.

## III.4 The topology of $E$ [T]

$E$ is the circle bundle over $S^4\setminus\Gamma$, where $\Gamma$ is the graph formed by the $N$ secondary meridians through the two poles. Alexander duality gives $H^2 = \mathbb{Z}^{2N-1}$; the physical bundle has equal flux on both arcs of each meridian and so lives in $\mathbb{Z}^N$, one integer per secondary. For $N = 1$, $S^4\setminus\text{circle}\simeq S^2$ and $E\simeq S^3$.

**$S^4$ does not become anything.** $E$ is a new five-dimensional space fibered over it; each 2-shell is *lifted* to a Hopf 3-sphere, not replaced.

## III.5 The partition principle [T/V/D]

**Geometric.** A metric on a circle bundle, in coordinates adapted to the fibration, is $h_{ab}dx^adx^b + L^2(d\theta + \alpha)^2$ — base, fiber length, connection — pointwise, with no remainder and no overlap:

| level | total | base | length | connection |
|:--|--:|--:|--:|--:|
| Hopf $S^3$ over a shell | 6 | 3 | 1 | 2 |
| $E\to S^4$ | 15 | 10 | 1 | 4 |
| $S^4\setminus\{\text{poles}\}\to\mathbb{RP}^3$ | 10 | 6 | 1 | 3 |

**Physical.** Even matter $T_+$ fills the base metric and the fiber length, through Law I. Odd matter $T_-$ fills the connection, through Law III, as the Chern class and its continuous deformation. The Hopf form itself is neither — it is the arena. Four even functions from gravity, two odd from the second order, nothing left over and nothing double-counted.

**Curvature.** Base Ricci $\leftarrow T_+$. The Weyl tensor of $E$ is exactly the connection's deviation from Hopf: $C_{abcd}C^{abcd} = 0$ for the Hopf connection, and $4\epsilon^2(16 - 13\sin^2\vartheta)/3\sin^4\chi$ for a perturbation $\epsilon\sin^2\vartheta$ **[V]**.

> **The projection discards the odd half; the twist recovers it; together they see all of $T$.**

## III.6 What sees $E$ [T/D]

Light does not: the photon is the zero mode, and Kaluza–Klein charge is fiber momentum, which is spin-independent. Gravity fixes $E$'s even half and is blind to its odd half. If the flux gravitates with coupling $g_2$, it adds a Reissner–Nordström term with $P = g_2M/m_{\rm unit}$, and Mercury's perihelion bounds $g_2/m_{\rm unit} < 0.024$ **[D]**.

---

# PART IV — IDENTITIES AND THEOREMS

## IV.1 The twin theorem [V]

The static operator on the closed base is $\Delta_{S^3} + 3$. Its Green's function has a **same-sign** pole at the antipode; its kernel is the dipoles; so a source must have zero dipole, and **a lone mass has no static solution.** A ball at the pole has dipole $0.169\neq0$, and a numerical solve returns the kernel mode as its symptom. The twin is forced, not permitted.

## IV.2 Closure and the $G$ identity [D]

The base is the Einstein static universe: $\Lambda = 1/\ell^2$ and $\bar\rho = 1/4\pi\ell^2$. The fibration flux through every latitude is $M_c$ — source at $0$, sink at $\infty$, nothing between — and closure fixes it:

$$\frac{GM_c}{c^2\ell} = \frac{\pi}{2}$$

$G$ is a constant of Law I, and the pair $(M_c,\ell)$ is constrained by the requirement that the base be static and closed. **A constraint, not a derivation.** The electric flux through every latitude is zero.

## IV.3 Law I as the fiber-length equation [V]

Weak-field statics are conformally round, $g_3 = \phi^4g_{S^3}$, and the Hamiltonian constraint linearizes about the Einstein static universe to

$$(\Delta_{S^3} + 3)\,\delta\phi = -2\pi\,\delta\rho_+$$

— the twin-theorem operator, acting on the conformal factor. The local Hopf length scale is $L_H = 2\pi\ell\phi^2$, so to first order $\delta L_H/L_H = -\Phi$ and $N\cdot L_H = $ constant: **fibers lengthen in wells by exactly the potential, and space stretches as much as time slows.** For a ball with its twin, $\phi^2 = 2.017$ at the ball's center and identically $2.017$ at the *empty* antipode, agreeing to $10^{-11}$ **[V]**. $L_H$ is the local length scale, not the circumference of any particular circle.

## IV.4 Weyl from the fiber length [V]

$$E_{ij} = -2\big[\nabla_i\nabla_j\phi\big]^{\rm TF},\qquad \phi = \sqrt{L_H/2\pi\ell}$$

The trace of the Hessian is fixed by the constraint and is the matter; the trace-free part is the tidal field. For Schwarzschild the eigenvalues are $(m/r^3)(1,-\tfrac12,-\tfrac12)$ — Petrov type D, with repeated principal null directions $\partial_t\pm\widehat{\nabla L_H}$, the directions of steepest fiber-length change. Type D here is forced by spherical symmetry rather than discovered. Beyond the weak-field static sector the fiber length is one of six metric components: magnetic Weyl lives in the shift, gravitational waves in the transverse-traceless part of the base 2-metric.

## IV.5 Charge and the twin [V/D]

Gauss on a closed section forces a compensating charge *somewhere*, and the seed puts nothing at the antipode. With the compensating charge wherever the other charges are, the field of a charge $Q$ is regular at the antipode and vanishes there — verified: $|E|\to0$ linearly. **The twin is electromagnetically empty.** A charged secondary's twin carries the $Q^2/r^2$ term of the metric as a *tidal* charge with $\nabla\cdot E = 0$ and $E = 0$: gravitational shape without electromagnetic content.

## IV.6 Orbits [V]

On the base a secondary is a well in the jellium, and closed-universe orbits are retrograde-precessing rosettes: apsidal advance $1.945\pi$ per radial period at small apocenter, falling to $1.836\pi$ in the mid-disk. The kinematic pattern speed $\Omega - \kappa/2$ falls by a factor 10 across a disk where Kepler alone would give 20 — the closure term halves the winding rate of kinematic spirals. At galactic radii in the cosmic arena the closure term is $10^{-7}$ of Kepler.

## IV.7 The static wall [T]

On a static geometry Killing energy is conserved and there is no redshift. This is a theorem about the arena, not a gap in it. Every route to Hubble's law within the static theory ends at the seed's own symmetry: the twin's well is *identical* to the source's, and identical wells cannot shift light between them.

---

# PART V — SPIN, FROM WEYL UP

## V.1 What a Weyl spinor is, and what mass is [T]

The smallest spinor in four dimensions is a **Weyl spinor**: two complex components, transforming in the $(\tfrac12,0)$ representation of $SL(2,\mathbb{C})$. It describes a massless fermion of definite handedness. Under a rotation of its frame by $2\pi$ it returns as $-\psi$; under $4\pi$, as $+\psi$.

A **Dirac spinor** is two Weyl spinors of *opposite* handedness: $\Psi = (\psi_L,\psi_R)$, four complex components. And the only thing that ties them together is the mass term,

$$\mathcal{L}_m = -m\big(\bar\psi_L\psi_R + \bar\psi_R\psi_L\big)$$

**A massless Dirac fermion is just two independent Weyl fermions; mass is the coupling between the two chiralities.** Everything in Parts V and VI is an elaboration of this one sentence.

## V.2 Two independent signs [T]

A particle on the base has a frame and a position, and each carries its own $\mathbb{Z}_2$. Since a Lie group is parallelizable, the frame bundle of $\mathbb{RP}^3 = SO(3)$ is $SO(3)\times SO(3)$, with $\pi_1 = \mathbb{Z}_2\times\mathbb{Z}_2$ and two **independent** generators:

| loop | sign | what it is |
|:--|:--|:--|
| rotate the frame by $2\pi$, position fixed | $(-1)^{2s}$ | spin — universal, present in any 3-manifold |
| carry the position once around the twin loop, frame fixed | $\tau$ | **twin parity** — the arena's own |

Keeping these apart is what the rest of this part depends on.

## V.3 What the arena does not do [T/R]

**A $2\pi$ rotation does not move anything.** Isometries of $S^3 = SU(2)$ are $g\mapsto agb^{-1}$; those fixing a point require $a = b$, so a rotation *about a point* is a conjugation $g\mapsto aga^{-1}$. A $2\pi$ rotation is $a = -1$, and $(-1)g(-1)^{-1} = g$: **the identity map on space** **[V]**. No matter is transported anywhere, and in particular none appears at the twin.

**The antipodal map is a translation, not a rotation.** It is left multiplication by the central element $-1$ — a Clifford translation, moving every point by $\pi$ and fixing none. Calling it "a $2\pi$ rotation" conflates the two loops of §V.2. **[R]**

**Spin does not emerge from scalars.** Peter–Weyl gives $L^2(SU(2)) = \bigoplus_jV_j\otimes V_j^*$ with $j$ half-integer, which looks like spin appearing in ordinary functions. But under rotations *about a point* — the diagonal, adjoint action — each block decomposes as $V_j\otimes V_j^* = \bigoplus_{k\le2j}V_k$: **integer spins only, for every $j$** **[T]**. As it must be, since a single-valued function carries integer angular momentum. The half-integer representations live under $SU(2)_L$ alone, which is a group of translations. **A spinor still needs its spinor index; the arena does not supply it.** **[R]**

So: none of the fermionic content can be shaved off by this route. What the arena offers is not a reduction of spin but an addition beside it.

## V.4 What the arena does do [T]

**The spin bundle is trivial and unique on the cover's spatial sphere.** $S^3$ is parallelizable, so spinor fields there are simply $\mathbb{C}^2$-valued functions with no patching, and the spin structure is unique. A convenience, not an emergence.

**Descent requires definite parity.** The antipodal map acts on the $j$-th Peter–Weyl block as $(-1)^{2j}$, so a field descends to $\mathbb{RP}^3$ only if built entirely from even blocks or entirely from odd ones. These are the two spin structures, and the two values of $\tau$.

**Fermions cannot be uniform.** The scalar Laplacian on $S^3(\ell)$ has a zero mode, the constant. The Dirac operator does not: its spectrum is $\pm(k + \tfrac32)/\ell$, $k = 0,1,2,\ldots$ **A fermion on the closed spatial sphere has an energy floor of $3\hbar c/2\ell$; a boson can sit at zero.** Negligible at cosmic $\ell$.

## V.5 Twin parity, and where it is fixed [T/D]

$\tau = \pm1$, defined by $\psi(-\hat n) = \tau\,\psi(\hat n)$, is a discrete quantum number **independent of spin and of statistics**. For two particles, $\pi_1$ of the configuration space of $\mathbb{RP}^3$ is the dihedral group $D_4$, whose abelianization is $\mathbb{Z}_2\times\mathbb{Z}_2$: four sectors, of which spin–statistics fixes the exchange sign and the model must supply $\tau$.

**Where it is fixed.** The generator of $\pi_1(\mathbb{RP}^3)$ lifts to a *path* from $\hat n$ to $-\hat n$ on the cover, and that path is a meridian arc — which runs through a pole. **The twin parity is the sign a field acquires on transport through the primary.** Which species are twin-odd is open **[O]**.

## V.6 Statistics and exclusion are untouched [T]

Finkelstein–Rubinstein: in any 3-manifold, exchanging two identical particles is *locally* homotopic to rotating one of them by $2\pi$ in place, so the exchange sign equals the frame-$2\pi$ sign, $(-1)^{2s}$. The argument is local and does not see the twin loop. **Anticommutation and the Pauli exclusion principle hold exactly as in ordinary quantum field theory**, on the cover and on the base. Nothing in this arena reaches them.

## V.7 The seed forces matter onto the cover [D]

A field **defined on the base** has, necessarily, equal magnitude at $\hat n$ and $-\hat n$: those are one point of $\mathbb{RP}^3$, and the two cover values are one value lifted. Any such field is antipodally symmetric in $|\psi|^2$, whatever its parity $\tau$.

Matter is therefore not a field on the base. In the action (§II.1) the Dirac and Maxwell terms are integrals over the **cover**. A lump at $\hat n$ with nothing at $-\hat n$ is a perfectly good cover configuration: it has no definite twin parity and does not descend. What descends is the *source*, $T_+ = T(\hat n) + T(-\hat n) = T(\hat n)$, and that is what gravity reads.

> **The seed forces matter onto the cover.** It is not a modelling choice: matter living on the base would have equal density at both twins by construction, and there would be no seed. The split — gravity on the base, matter on the cover — is what makes the seed possible.

---

# PART VI — THE DIRAC FIELD ON THE SECOND-ORDER TOTAL SPACE

## VI.1 Spinors exist on $E$ [T]

$E$ is a circle bundle over $B = S^4\setminus\Gamma$, so $TE = \pi^*TB\oplus V$ with the vertical $V$ trivialized by the fiber generator. Hence $w_2(E) = \pi^*w_2(S^4) = 0$ and **$E$ is a spin manifold.**

How many spin structures? $H^1(E;\mathbb{Z}_2)$. Alexander duality gives $H^1(B;\mathbb{Z}_2) = H_2(\Gamma;\mathbb{Z}_2) = 0$ since $\Gamma$ is a graph, and the Gysin sequence makes $H^1(E;\mathbb{Z}_2)$ the kernel of cup product with $e\bmod2$. **The count therefore depends on the parity of the flux**: a unique spin structure when the Chern number is odd, two when it is even. With $m_{\rm unit}$ a particle mass, a body's Chern number is astronomically large and its parity is not a controlled datum, so whether the second order fixes $\tau$ depends on the quantization fork **[T/O]**.

## VI.2 Why a Weyl field, and the exact count [T]

| space | Dirac | Weyl |
|:--|--:|--:|
| $\mathbb{R}_t\times\mathbb{RP}^3$ (4-D) | 4 complex | 2 complex |
| $\mathbb{R}_t\times S^4$ (5-D) | 4 complex | — (odd dimension: no Weyl condition) |
| $\mathbb{R}_t\times E$ (6-D) | 8 complex | **4 complex** |

**A six-dimensional Weyl spinor has 4 complex $=$ 8 real components: exactly one four-dimensional Dirac spinor's worth.** A six-dimensional *Dirac* field would give two 4-D Diracs per Kaluza–Klein level — a species doubling requiring a projection. Majorana–Weyl spinors exist only in dimensions $\equiv2\bmod8$, so not here; symplectic Majorana–Weyl exists in six dimensions but requires pairs. **The minimal chiral fermion on $E$ is a Weyl spinor, and enforcing it is a genuine simplification.** Its cost: six-dimensional Weyl fermions are chiral and carry anomalies — an eight-form condition on the model's fermion content, unexamined **[O]**.

## VI.3 Chirality becomes motion along the fiber [T]

This is the substantive difference, and it is not the one intuition suggests.

In five dimensions the Clifford algebra needs five gamma matrices, and the fifth is *forced*:

$$\Gamma^0,\ldots,\Gamma^3 = \gamma^0,\ldots,\gamma^3,\qquad \Gamma^4 = \pm\,i\gamma^0\gamma^1\gamma^2\gamma^3 = \pm\gamma_5$$

**The fifth gamma matrix is the four-dimensional chirality operator.** So the five-dimensional Dirac equation reads

$$\big(i\gamma^\mu\partial_\mu + i\gamma_5\partial_u - m\big)\Psi = 0$$

Momentum along the meridian couples through $\gamma_5$. A left-handed and a right-handed fermion differ by *which way they move along the fiber*; $p_u$ flips chirality; and the four-dimensional mass is $\sqrt{m^2 + p_u^2}$. **What is called chirality downstairs is velocity along the fiber upstairs.** Going up to six dimensions adds the correlation $\mathbf{4} = (\mathbf{2}_L,+\tfrac12)\oplus(\mathbf{2}_R,-\tfrac12)$ under $SO(1,3)\times SO(2)$: the two chiralities carry opposite charge under rotation in the plane of the extra directions.

## VI.4 Not a polarization: there is no triality in six dimensions [T]

Photon polarization is a **vector** index — two transverse directions. A spinor index becomes a vector index only where an outer automorphism identifies them, and that happens **only in eight dimensions**, where Spin(8) triality makes $\mathbf{8}_v$, $\mathbf{8}_s$, $\mathbf{8}_c$ all eight-dimensional and permuted. In six dimensions Spin(6) $= SU(4)$ has vector $\mathbf{6}$ and Weyl spinor $\mathbf{4}$: not isomorphic, no reframing. What *is* true is the bilinear $\mathbf{4}\wedge\mathbf{4} = \mathbf{6}$ — **two** spinors make a vector, which is the ordinary Dirac current $\bar\Psi\Gamma^M\Psi$, not a rewriting of one spinor as a polarization.

What photon and fermion already share: for a massless particle in four dimensions the little group is $SO(2)$, and the physical states are its charges — helicity $\pm1$ for the photon, $\pm\tfrac12$ for a Weyl fermion. Same transverse plane, same group, different charge. **They were already the same kind of object; the total space does not make the fermion more like the photon, it makes chirality geometric.**

## VI.5 The tower, and what is different [D]

Fourier-decompose along the Hopf fiber, $\Psi = \sum_n\psi_n(x)e^{in\theta}$:

| datum | what it becomes below |
|:--|:--|
| $n$ | the Hopf charge: the mode couples to $\alpha$ with charge $n$ |
| $\lvert n\rvert/L_E$ | a Kaluza–Klein mass |
| $n = 0$ | the ordinary Dirac field — Hopf-neutral, coupling to nothing in the second order |

**The mass tower is set by gravity.** Since $L_E = \Omega L^{\rm ref}$ and $\delta L/L = -\Phi$ (§IV.3),

$$\frac{\delta m_n}{m_n} = +\Phi$$

Kaluza–Klein masses are **lower in gravitational wells** — by $7\times10^{-10}$ at Earth's surface, $2\times10^{-6}$ at the Sun's, $0.2$ at a neutron star. The $n = 0$ mode has no Kaluza–Klein mass, so the ratio $m_n/m_e$ varies with the potential: a local-position-invariance violation confined to the hidden sector, and unobservable because $n\neq0$ is invisible to base detectors (Part VII).

## VI.6 What is not different [D]

Statistics, exclusion, and the Lorentz structure. A Dirac spinor is $(\tfrac12,0)\oplus(0,\tfrac12)$ of $SL(2,\mathbb{C})$, and the boosts are not in $SU(2)_{\rm spatial}$ — the cover's time direction is not a group direction. The arena supplies the extra fiber directions and the twin structure; **the spinor index, the Clifford algebra, the boosts, and the exclusion principle are inputs from ordinary quantum field theory on the cover, exactly as they were.**

---

# PART VII — THE BASE-RESOLUTION PRINCIPLE

> ### ◆ THE BASE-RESOLUTION PRINCIPLE
> A detector is a base object. It can record base position and base direction, within its resolution, and nothing else. Two paths in the second-order total space that end at terminal points projecting to the same base point, and arrive with directions whose base projections lie within the detector's resolution, **cannot be distinguished by the detector.** They contribute to one amplitude.

**Why it is a theorem [D].** A fiber datum is, by definition of the quotient, invariant under the fiber action, hence not a function on the base, hence not recordable by a base detector. The fiber is unresolvable because the base is a quotient — the same fact that makes gravity blind to it.

**What a detector sees [V].** For a field of fiber charge $n$, terminal points separated by $\Delta$ contribute $e^{in\Delta}$, and

$$\int_0^{2\pi}e^{in\Delta}\,d\Delta = 2\pi\,\delta_{n0}$$

Zero modes add coherently: light sources from every fiber point at once, with Law IV unchanged. Charged modes average to zero: invisible, not decohered. **"The base sees zero modes" is what a base detector can register, not an assumption about matter.**

**The twist, through paths [T].** Two base paths enclosing a surface $\Sigma$ arrive with fiber phases differing by $n\int_\Sigma F$; the detector cannot resolve the fiber velocities that would distinguish them; they interfere, and the fringe shifts by the flux. This is the Aharonov–Bohm effect. For the photon $n = 0$, and there is no fringe.

---

# PART VIII — THE GOLF BALL [V/D]

A test of what the second order says at laboratory scale: a golf ball hovering in a vacuum chamber on Earth's surface. Does it enclose its own fibers?

**Topologically, yes.** Law III is linear, $F = F_\oplus + F_g$, and for a small sphere around the ball $\frac{1}{2\pi}\int F = M_g/m_{\rm unit}$ exactly. Chern numbers add and are localized; Earth cannot smear away an integer.

**Geometrically, Earth dominates.** The flux falls as $N/2r^2$ — the same law as gravity — and the ball's field exceeds Earth's only inside

$$r = R_\oplus\sqrt{M_g/M_\oplus} = 0.56\ \mu\text{m}$$

which is precisely the ball's gravitational neutral point, since both fields are sourced by mass with the same falloff. Outside it the fibers are Earth's, with the golf ball's contribution as a dip.

**The quantization fork decides whether there is any winding at all.** With $m_{\rm unit} = m_p$ the ball winds $2.7\times10^{25}$ times and Earth $3.6\times10^{51}$. With $m_{\rm unit}\sim10^{14}M_\odot$ both wind zero times and the second order is absent from the solar system entirely.

Two practical notes: a spherically symmetric chamber contributes nothing inside, by the shell theorem, which applies because the flux obeys an inverse-square law; and nothing in the laboratory could detect either answer, since the photon is Hopf-neutral.

---

# PART IX — THE MACHIAN DIRECTION

*The proposal: a body that fully encloses its own fibers should be a rescaled copy of any other such body, so that an isolated golf ball has Earth's compactness while a golf ball near Earth has general relativity's, with the Newtonian force invariant. The hope: that this shakes $G$ loose in Law I.*

## IX.1 What is already true [T]

Vacuum general relativity has the symmetry $(g,M)\to(\lambda^2g,\lambda M)$: every Schwarzschild exterior *is* a rescaled copy of every other, with mass as the scale. The Hopf-over-shells bundle is likewise one universal object with $N = M/m_{\rm unit}$ its only body-dependent datum. So "isomorphic fibers up to scale" is true and yields nothing new — the scale it fixes is mass, not size, and compactness $r_s/R$ ($1.4\times10^{-9}$ for Earth, $3.2\times10^{-27}$ for a golf ball) is untouched.

## IX.2 The proposal as stated is inconsistent [D]

Giving the isolated ball Earth's compactness means $r_s\to4\times10^{17}r_s$ with $GM$ fixed. But $r_s = 2GM/c^2$: the horizon and the Newtonian coupling are **one number** in any theory whose exterior has a single source. Not general relativity, not Brans–Dicke, not any single scalar. Separating them requires the near field to be sourced by something the far field does not see.

## IX.3 The realizable form is already present, and it is small [D]

Law III's flux, when it gravitates, is exactly such a second source. Reissner–Nordström,

$$f(r) = 1 - \frac{2GM}{c^2r} + \frac{GP^2}{c^4r^2},\qquad P = g_2M/m_{\rm unit}$$

leaves the Newtonian term untouched and moves the horizon. And the flux energy $|F_\oplus + F_g|^2$ contains a **cross term** $2F_\oplus\cdot F_g$ — a source at the golf ball that exists only when Earth is present, $1.5\times10^9$ times the ball's own term at its surface. In isolation only the self term survives.

**The ball's near field genuinely differs alone and near Earth. That is the Machian effect, realized by the dynamic sector with no new law.** Its size is bounded by Mercury: $P/M < 0.024$, so $\delta r_s/r_s < 3\times10^{-4}$ — the right shape, twenty-one orders of magnitude short of the compactness rescaling.

## IX.4 A local Mach relation fails [V]

Reading $GM/c^2\ell = \pi/2$ with $\ell$ a body's sphere of influence gives $G_{\rm loc} = 5\times10^{11}G$ for Earth and $3\times10^{22}G$ for the golf ball. The Mach relation closes a *universe*; spheres of influence are not closed universes.

## IX.5 Emergent $G$: what it would take [D]

$G$ is emergent if and only if mass has a $G$-free definition. In general relativity it does not — ADM and Komar masses are defined *through* $G$. The Hamiltonian constraint,

$$H^2 = \frac{8\pi G}{3}\rho - \frac{1}{a^2} + \frac{\Lambda}{3}$$

holds on every slice of every spacetime and is the invariant that extends beyond the static case — but it constrains the product $G\rho$ and cannot separate the factors. The only $G$-free mass the program has produced is the fiber momentum $p_u = m$ of the null-fiber reading, where $G$ becomes a conversion factor between curvature and fiber-momentum density. **That reading is set aside in this version. On a spacelike $u$, $G$ is a constant constrained by closure, and emergence is not available.** This is the tension version 10 carries forward rather than resolves.

---

# PART X — SET ASIDE, RETIRED, OPEN

## X.1 Set aside (versions 7–9): recorded, not assumed

The null fiber and its Bondi reading; the Eisenhart–Bargmann lift and the identification of the fiber coordinate with the classical action; the Lorentzian real slice of the complexified cover and its de Sitter geometry; the fiber as quantum phase; Law I as semiclassical; the twin as a superposition branch; the fiber product as "visual space." Each is a coherent branch; none is part of version 10.

## X.2 The Dirac-quotient proposal, assessed [T/D/O]

*A proposed version 11: alongside the gravitational base, define a second quotient of $E$ by an involution chosen so that the two Weyl halves of a Dirac spinor are carried by identified points.*

**The involution already exists in the theory.** The physical twin map takes $\hat n\to-\hat n$ on a latitude **and** $N\to-N$ on the fiber, since the twin carries the anti-monopole. On $E$ with coordinates $(\chi,\hat n,\theta)$ this is

$$\sigma:\ (\chi,\hat n,\theta)\;\longmapsto\;(\chi,-\hat n,-\theta)$$

**It is orientation-reversing** [V]: $\hat n\to-\hat n$ on the four embedding coordinates contributes $(-1)^4 = +1$, and the fiber conjugation $\theta\to-\theta$ contributes $-1$, for a total determinant of $-1$. It is free, since $\hat n\neq-\hat n$. By contrast the twin map *alone* has determinant $+1$ — orientation-preserving — which is why the gravitational base $\mathbb{RP}^3$ is orientable and carries two spin structures. **The fiber conjugation is what flips it.**

**Why that gives Dirac spinors [T/D].** The chirality operator on an even-dimensional manifold is the product of all gamma matrices, whose sign depends on the orientation. A non-orientable quotient has no global orientation, hence **no global chirality operator**: it carries Pin structures rather than Spin, and a spinor field on it cannot be chirally projected. Equivalently, $\sigma_*$ maps $S^+$ to $S^-$, so a $\sigma$-equivariant field is of one chirality at a point and the other at its image.

> **The two Weyl components of a Dirac spinor would be the field at a point and at its twin.** And the Dirac mass term, which couples the chiralities, becomes a coupling between a point and its twin — *local* on the fermionic quotient, twin-connecting seen from the cover.

**The obstacle [O].** By §V.7, a field defined on a quotient has equal magnitude at identified points. If fermions live on $E/\sigma$ then $|\Psi(-\hat n)|^2 = |\Psi(\hat n)|^2$ and there *is* matter at the twin: the seed breaks for fermions. Two escapes are worth testing. **(a)** The twin carries only the *opposite* chirality; if that chirality is sterile — a right-handed neutrino-like state — the twin would be dark rather than empty, changing the seed's meaning rather than killing it. **(b)** Fermions remain on $E$, and $E/\sigma$ is used only to define the spinor bundle, not the density. Either is a real branch; neither is free.

**Assessment.** The construction is sound and the involution is the one the second order already supplies, which is a point in its favor. Whether it can be reconciled with the seed is the question a version 11 would have to answer first.

## X.3 Retired, with reasons

| item | reason |
|:--|:--|
| compactification, dilaton, winding, $G_4$ from $G_5$, sub-millimeter scale | dynamical-reading machinery; the kinematic reading has no radion |
| the dielectric coupling $\epsilon(T)$ as an electromagnetic law | it varied $\alpha_{\rm fine}$ through the dilaton; legal now only as Law II's $\mu(\rho)$, which touches nothing electromagnetic |
| monopoles at points | on $S^4$ they are meridians, and the descent is a linking number |
| the twin's opposite electric charge | assumed the $\cot\chi$ Green's function, which places a charge where the seed puts nothing |
| Tully–Fisher from closure, as a result about our universe | needs $\ell\approx8$ kpc; a toy for the reflection-sky arena |
| the half-orbit selection of spiral arms | every chiral structure in the theory is light-blind |
| spin emerging from scalars on $SU(2)$ | rotations about a point are conjugations, under which all functions carry integer angular momentum (§V.3) |
| "a $2\pi$ rotation is the antipodal map" | conjugation by $-1$ is the identity; the antipodal map is a translation (§V.3) |
| the Machian rescaling as stated | inconsistent (§IX.2) |

## X.4 Open

1. **The quantization fork.** $m_{\rm unit}$ a particle mass (everything winds) or $\sim10^{14}M_\odot$ (only superclusters). Light-blind either way; distinguishable only by Kaluza–Klein modes or by $g_2$.
2. **$g_2/m_{\rm unit}$.** Below $0.024$ from Mercury; the double pulsar can tighten it.
3. **$\mu(\rho)$.** Nothing selects it; observable only through footprint dilation, bounded by 4.
4. **Twin parity assignments.** Which species are twin-odd, and whether six-dimensional Weyl anomalies cancel.
5. **Emergent $G$.** Requires a $G$-free definition of mass; see §IX.5.
6. **The Dirac quotient.** Whether §X.2 can be reconciled with the seed.
7. **Inherited.** The AdS uplift; the two arenas; the literature review.

---

## Reference card

| topic | statement |
|:--|:--|
| **arena** | $\mathbb{R}_t\times S^4$; primary at the south pole, forced by $\chi(S^4) = 2$; latitudes are the level sets |
| **Law I** | GR on $\mathbb{R}_t\times\mathbb{RP}^3$, source $T_+$, $\Lambda = 1/\ell^2$; $\gamma = 1$ trivially |
| **Law II** | $\nabla\cdot(\mu\nabla\Phi_u) = M_c[\delta(0)-\delta(\infty)]$; meridians; weaves, never captures; kinematic |
| **Law III** | $dF = 2\pi\star J_-$ on meridians; $L_E = \Omega L^{\rm ref}$; kinematic; $g_2/m_{\rm unit}<0.024$ if it gravitates |
| **Law IV** | Maxwell on $S^4$; photon Hopf-neutral; twin electromagnetically empty |
| **seed** | derived from the meridian structure; forces matter onto the cover |
| **twin** | $\pm\hat n$ on a latitude: the two equatorial crossings of one meridian, one point of the base |
| **$G$** | $GM_c/c^2\ell = \pi/2$: a constraint, not a derivation |
| **twin theorem** | $(\Delta+3)$; dipole kernel; a lone mass has no static solution |
| **fiber reading** | $L_H = 2\pi\ell\phi^2$; $\delta L/L = -\Phi$; $E_{ij} = -2[\nabla\nabla\phi]^{\rm TF}$; PNDs along $\nabla L$ |
| **partition** | base $+$ length $+$ connection; even fills the first two, odd the third; $E$-Weyl $=$ the twist |
| **spin** | frame $\mathbb{Z}_2$ and position $\mathbb{Z}_2$ independent; $2\pi$ rotation moves nothing; spin does **not** emerge from scalars; statistics untouched |
| **Dirac on $E$** | 6-D Weyl, 4 complex $=$ one 4-D Dirac; chirality $=$ motion along the fiber ($\Gamma^4 = \gamma_5$); no triality, so not a polarization; $m_n = n\hbar/cL_E$, lower in wells |
| **detection** | which-path is base-only; zero modes add; $n\neq0$ invisible; Aharonov–Bohm through paths |
| **golf ball** | winds $M_g/m_{\rm unit}$ times; Earth dominates beyond $0.56\,\mu$m; the fork decides if it winds at all |
| **Machian** | literal form inconsistent; the cross term in the dynamic sector is the realizable form, $<3\times10^{-4}$ |
| **emergent $G$** | requires $G$-free mass; only the set-aside null fiber supplies one |
