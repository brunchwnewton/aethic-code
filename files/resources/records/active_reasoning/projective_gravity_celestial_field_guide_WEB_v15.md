# Projective Gravity — Version 15

### The Canonical Space First: a complex Hopf lift of source shells, a derived middle space, and two bases

> **What this document is.** A complete, self-contained statement of the theory. It assumes no earlier document: every term is defined in Part 0, every law is stated with its equation, and every identity imported from an earlier version is restated in full rather than cited.
>
> **The architectural change.** Versions 6 through 14 posited a space and then decorated it with a fiber. Version 15 inverts the order. The **canonical space** $E$ is the axiom; the middle space is *derived* from it by quotienting a circle; and the middle space then has **two** four-dimensional readouts, which earlier versions ran together — one where matter and light are localized, one where gravity acts.
>
> **What the fiber now is.** A shell of fixed nonzero radius about a *complex* source worldline is not a real 2-sphere: in the complexified normal space it is the affine quadric $Q^2_{\rm aff}$, a complex surface. And that surface is a homogeneous space of the complex spin group,
> $$\mathbb{C}^\times\ \longrightarrow\ SL(2,\mathbb{C})\ \longrightarrow\ Q^2_{\rm aff}\cong SL(2,\mathbb{C})/\mathbb{C}^\times$$
> whose compact real form is the ordinary Hopf fibration $U(1)\to SU(2)\simeq S^3\to S^2$. **So the Hopf character is no longer decoration. It is the compact real form of the complex spin geometry belonging to an isotropic shell**, and it was the right guess for the wrong reason in every version that assumed it.
>
> **The seed, in one line.**
> > Light resolves a representative in $B_{\rm rep}$; gravity resolves only its meridian class in $B_{\rm grav}$.
>
> **Tags.** **[T]** standard or cited · **[V]** verified by computation here · **[D]** derived from the adopted definitions · **[S]** structural proposal · **[O]** open · **[R]** retired, with reason.

---

# PART 0 — VOCABULARY AND THE HIERARCHY

## 0.1 The four layers

Earlier versions had three layers and conflated two of them. Version 15 has four.

| layer | symbol | what it is | $\dim_\mathbb{R}$ |
|:--|:--|:--|:--:|
| **canonical space** | $E$ | the axiom. A circle bundle whose restriction to every source shell is the compact real form of the complex spin lift | 6 |
| **middle space** | $\mathcal{M} = E/U(1)_H$ | **derived**, by forgetting the spin phase | 5 |
| **representational base** | $B_{\rm rep}\hookrightarrow\mathcal{M}$ | an *embedded* Lorentzian hypersurface. Where matter, light and detectors live | 4 |
| **gravity base** | $B_{\rm grav} = \mathcal{M}/U_{\rm mer}$ | a *quotient* by the meridian foliation. Where Law I acts | 4 |

The two bases have the same dimension and arise by opposite operations:

$$B_{\rm rep} = \text{a resolved representative},\qquad B_{\rm grav} = \text{an equivalence class}$$

Conflating them was the error that made the seed look like a postulate.

## 0.2 Terms

| term | meaning |
|:--|:--|
| **shell** | the set of points at fixed nonzero distance from a source worldline, within its normal space |
| **complex shell** $\Sigma^\mathbb{C}_{\gamma,R}$ | the same at fixed *complex* radius about a *complex* worldline: an affine quadric, a complex surface |
| **spin phase** $U(1)_H$ | the compact fiber of the shell lift; the physical real form of the complex stabilizer $\mathbb{C}^\times$ |
| **meridian** | a leaf of the one-dimensional foliation $U_{\rm mer}$ of the middle space. In the static limit, a great circle of $S^4$ through both poles |
| **twin** | given $x\in B_{\rm rep}$, the other point $\tau x$ of the same meridian, with $\tau^2 = 1$ and $q(x) = q(\tau x)$ |
| **barren twin** | a twin carrying no matter, at which gravitational curvature is nevertheless nonzero. **The seed** |
| **$T_\pm$** | $T_\pm(x) = T(x)\pm T(\tau x)$: the even and odd parts of matter under the twin map |
| **jellium** | the uniform background density of the gravity base, supplied by the primary |
| **primary** | the dominant mass at a degeneracy of the meridian foliation |
| **conformal factor** | $\phi$, with $g_3 = \phi^4g_{\rm ref}$ and $\Omega\equiv\phi^2$ |
| **fiber length** $L_H$ | the circumference the canonical metric assigns the $U(1)_H$ orbit |

## 0.3 The tower

$$E^{(6)}\ \xrightarrow{\ /\,U(1)_H\ }\ \mathcal{M}^{(5)}\ \xrightarrow{\ /\,U_{\rm mer}\ }\ B_{\rm grav}^{(4)},\qquad B_{\rm rep}^{(4)}\hookrightarrow\mathcal{M}^{(5)}$$

Verified consistent: a circle quotient drops one dimension, a one-dimensional foliation quotient drops one more, and an embedded hypersurface of a five-manifold is four-dimensional **[V]**. Two distinct losses of information occur, and they must not be confused:

| quotient | what is forgotten |
|:--|:--|
| $E\to\mathcal{M}$ | the **spin phase** |
| $\mathcal{M}\to B_{\rm grav}$ | **where along the meridian** the matter sits |

## 0.4 What is axiomatic

The primitive data are $\big(E,\ \hat g,\ U(1)_H,\ \mathcal{A}_H,\ \rho_E,\ \mathcal{U}_{\rm mer}\big)$: the canonical space, its metric, the fiber action, its connection, the real-analytic structure needed to complexify shells, and the meridian foliation of the quotient. Everything else — the middle space, both bases, the seed — is derived. **The theory is top-down.**

---

# PART I — THE COMPLEX SHELL AND ITS SPIN LIFT

*This part supplies the fiber. It is the version's substantive addition, and it is the reason the Hopf structure is no longer an assumption.*

## I.1 The complex worldline and its normal space [T/S]

Let $\Gamma_\mathbb{C} = \{\gamma(\tau)\}$ be the analytic complex worldline of a source, with non-null tangent, $g_\mathbb{C}(\dot\gamma,\dot\gamma)\neq0$. At each $\gamma(\tau)$ the **complex normal space** is

$$N_\gamma = \{\xi : g_\mathbb{C}(\xi,\dot\gamma) = 0\}$$

complex three-dimensional — the complexification of the ordinary spatial rest space about a real timelike worldline.

## I.2 A complex shell is an affine quadric [T]

A shell of nonzero complex squared radius $R^2$ is

$$\Sigma^\mathbb{C}_{\gamma,R} = \{\xi\in N_\gamma : g_\mathbb{C}(\xi,\xi) = R^2\}$$

Choosing an orthonormal complex frame and rescaling,

$$\Sigma^\mathbb{C}_{\gamma,R}\ \cong\ Q^2_{\rm aff} = \{(z_1,z_2,z_3)\in\mathbb{C}^3 : z_1^2+z_2^2+z_3^2 = 1\}$$

**a complex surface, not a real 2-sphere.** Its symmetry group is the complex rotation group $SO(3,\mathbb{C})$, whose spin double cover is $Spin(3,\mathbb{C})\cong SL(2,\mathbb{C})$.

## I.3 The complex Hopf lift [T/V]

$SO(3,\mathbb{C})$ acts **transitively** on the affine quadric — any non-null vector of given norm rotates to any other — with stabilizer the complex torus $SO(2,\mathbb{C}) = \mathbb{C}^\times$. Lifting to the double cover:

$$\boxed{\ \mathbb{C}^\times\ \hookrightarrow\ SL(2,\mathbb{C})\ \twoheadrightarrow\ Q^2_{\rm aff}\cong SL(2,\mathbb{C})/\mathbb{C}^\times\ }$$

Checked by dimension: $\dim_\mathbb{R}SL(2,\mathbb{C}) - \dim_\mathbb{R}\mathbb{C}^\times = 6-2 = 4 = \dim_\mathbb{R}Q^2_{\rm aff}$ **[V]**.

**This is the complex Hopf shell.** The old Hopfian character survives complexification not by pretending the complex shell is still a 2-sphere, but by complexifying the *homogeneous-space relation itself*.

## I.4 The physical real form is exactly the Hopf fibration [T/V]

For a timelike source on the Lorentzian real slice, the normal rest space is ordinary Euclidean three-space, and each piece passes to its compact real form:

| complex | real | check |
|:--|:--|:--|
| $Q^2_{\rm aff}$ | $S^2$ | $z_1^2+z_2^2+z_3^2 = 1$ with $z$ real *is* the unit 2-sphere |
| $SL(2,\mathbb{C})$ | $SU(2)\simeq S^3$ | maximal compact subgroup |
| $\mathbb{C}^\times$ | $U(1)$ | maximal compact subgroup |

$$\boxed{\ U(1)\ \hookrightarrow\ SU(2)\simeq S^3\ \twoheadrightarrow\ S^2\ }$$

with $3-1 = 2 = \dim S^2$ **[V]**. So the earlier versions' assertion — *every spherical shell lifts to a Hopf 3-sphere* — is **recovered as the physical real form** of the complex statement, rather than imposed before complexification.

## I.5 Why this is isotropic [T/D]

The shell is defined by the invariant condition $g_\mathbb{C}(\xi,\xi) = R^2$ alone. The rotation group acts transitively on it, so no angular direction is preferred; and the lift $SL(2,\mathbb{C})\to SL(2,\mathbb{C})/\mathbb{C}^\times$ is likewise homogeneous. **The fiber is not attached by choosing a longitude. It is the stabilizer of the spin-group action.** On the real form, $SU(2)\to SU(2)/U(1)\simeq S^2$ is equally isotropic under ordinary rotations — which is the precise sense in which the magnetic/isotropic motivation of the original picture is preserved.

## I.6 Why the fiber is not bolted on [T]

$SL(2,\mathbb{C})$ is not introduced to manufacture a bundle. **It is already the spin group of four-dimensional Lorentzian two-spinor geometry** — the group under which Newman–Penrose spinors transform. The same algebraic object appears in two places at once:

$$SL(2,\mathbb{C}) = \text{the spacetime spin group} = \text{the isotropy lift of a complex shell}$$

That coincidence is the argument. Every earlier version had to *assume* a circle; here the circle is the compact part of a group the theory already contains.

## I.7 What the complex shell is **not** [T]

At a point of complexified four-dimensional spacetime, the projectivized complex null cone is a different object — a projective quadric built from two independent chiral spinors, natural for **null directions**. The shell used here represents **fixed nonzero radius in the complexified rest space of a non-null worldline**. These must not be conflated:

$$\text{null-direction quadric}\ \neq\ \text{fixed-radius worldline shell}$$

The affine quadric is preferred because its three pieces complexify *together* and its real limits are exactly the three wanted (§I.4). The projective version does not have the $S^2$ limit for a source shell.

---

# PART II — THE CANONICAL SPACE AND THE TWO BASES

## II.1 Law 0 [S/O]

> ### ◆ LAW 0 — THE CANONICAL SPACE
> There exists a canonical space $E$ such that: (i) its quotient by the compact fiber action is the middle space, $\mathcal{M} = E/U(1)_H$; (ii) near a source worldline, its analytic continuation restricted to every nonzero-radius complex shell is the homogeneous bundle $\mathbb{C}^\times\to SL(2,\mathbb{C})\to Q^2_{\rm aff}$; (iii) on the physical rest-space shell this reduces to $U(1)\to SU(2)\to S^2$; (iv) the fiber carries a connection $\mathcal{A}_H$; (v) the metric $\hat g$ gives the compact fiber a length $L_H$.

**An obstruction that must be stated [V/O].** Condition (iii) cannot hold over an *unpunctured* static middle space. Since $H^2(S^4) = 0$, every circle bundle over $\mathbb{R}_t\times S^4$ is trivial, and a trivial bundle restricts to $S^2\times S^1$ on each shell — **not** to $S^3$. The Hopf lift requires Chern number $1$ on the shell, which requires the secondary meridians to be removed, exactly as versions 6 through 14 did: $S^4\setminus\text{circle}\simeq S^2$ has $H^2 = \mathbb{Z}$. **So Law 0 must be stated over $\mathcal{M}$ minus the secondary meridians**, and the draft architecture inherits that surgery rather than escaping it. Global existence and uniqueness of $E$ remain open.

## II.2 The middle space is derived [D]

$$\mathcal{M} = E/U(1)_H$$

Nothing in this version may treat $\mathcal{M}$ as more fundamental than $E$. The quotient discards the spin phase while retaining the meridian-completed localization geometry. **This is the first loss of information in the tower.**

## II.3 The representational base is a bisection, not a section [S/O]

$B_{\rm rep}$ is an embedded Lorentzian hypersurface $\iota:B_{\rm rep}\hookrightarrow\mathcal{M}$ where matter is localized, Maxwell fields live, detectors receive light, and Newman–Janis is interpreted.

In the old static picture, the equatorial $S^3$ met each meridian at **two** points, $\hat n$ and $-\hat n$. The general statement is

$$L_b\cap B_{\rm rep} = \{x,\ \tau x\},\qquad \tau^2 = 1,\qquad q(x) = q(\tau x) = b$$

so $B_{\rm rep}$ is a **bisection**: two points per gravity fiber, not one. **And the second point may be barren.** This is where the seed lives, and stating it as a bisection rather than a section is what makes the seed a consequence instead of a postulate.

## II.4 The gravity base is a quotient [S]

$$B_{\rm grav} = \mathcal{M}/U_{\rm mer}$$

Gravity does not ask which representative in $q^{-1}(b)$ holds the matter. It asks only for the reduced source assigned to the class.

---

# PART III — THE LAWS

> ### ◆ LAW I — GRAVITY
> $$G_{\mu\nu}[g_G] + \Lambda g^G_{\mu\nu} = 8\pi G\,T^{(g)}_{\mu\nu}\qquad\text{on } B_{\rm grav},\qquad \Lambda = 1/\ell^2$$
> with the source obtained by meridian reduction of resolved matter. In the discrete twin limit, $T^{(g)}([x]) = T(x) + T(\tau x)$. The same solution fixes the canonical fiber length (§III.2). There is no dilaton, no radion, and no extra scalar with a $1/r$ coupling, so PPN $\gamma = 1$ holds trivially.

> ### ◆ LAW II — THE MERIDIANS
> The middle space carries a one-dimensional foliation $U_{\rm mer}$. The representational base resolves its representatives; gravity quotients it. In the static spherical limit it must reduce to the great circles of $S^4$ through both poles, with quotient $\mathbb{RP}^3$. The general equation selecting the foliation is **open** **[O]**.

> ### ◆ LAW III — THE CONNECTION
> The canonical fiber carries a connection $\mathcal{A}_H$ with curvature $F_H = d\mathcal{A}_H$. The candidate odd-sector law is $dF_H \overset{?}{=} 2\pi\star J_-$, with $J_- = \rho_-/m_{\rm unit}$. **Not promoted to a law until the source coupling is derived** **[O]**.

> ### ◆ LAW IV — ELECTROMAGNETISM
> Maxwell on $B_{\rm rep}$, with $\epsilon = \mu_{\rm EM} = 1$. Light resolves meridian representatives and does **not** perform the gravity quotient. The photon is the zero mode on the canonical fiber and couples to none of it.

## III.1 What each law is, and what you deduce from it [D]

| | **Law 0** | **Law I** | **Law II** | **Law III** | **Law IV** |
|:--|:--|:--|:--|:--|:--|
| **is** | an existence axiom | Einstein's equations | a foliation | a first-order curvature law | Maxwell |
| **lives on** | $E$ | $B_{\rm grav}$ | $\mathcal{M}$ | the canonical fiber | $B_{\rm rep}$ |
| **determines** | the arena and its fiber | $g_G$, hence $\Omega$, hence $L_H$ | the twin pairing and $B_{\rm grav}$ | $\mathcal{A}_H$ | $\mathcal{F}$ |
| **sourced by** | — | $T_+$, the **even** part | the primary's degeneracies | $J_-$, the **odd** part (candidate) | charge |
| **status** | structural | **dynamical** | kinematic | kinematic, **unproved coupling** | dynamical |
| **what you deduce** | the Hopf lift on every shell (§I.4) | orbits, tides, redshift, black-hole exteriors, the $v^2$ plateau (Part IV) | which points are twins; the seed (Part V) | Chern numbers on meridians; the Aharonov–Bohm phase | the photon's kinematics; the twin's optical barrenness |

## III.2 Law I locks the fiber length [S]

In the conformal/static sector, with $g_{\rm spatial} = \Omega^2g_{\rm ref}$ and $\Omega = \phi^2$:

$$L_H = \Omega\,L_H^{\rm ref},\qquad\text{so to first order}\qquad \frac{\delta L_H}{L_H} = -\Phi$$

**Fibers lengthen in wells by exactly the potential, and space stretches as much as time slows.**

> The reading is cleaner than in earlier versions: **gravity does not create the fiber — the spin geometry supplies it (Part I). Gravity determines its metric size.**

*Scope.* This is a first-order statement. Isotropic Schwarzschild has $N = (1-m/2r)/(1+m/2r)$ while $N = \Omega^{-1}$ would require $(1+m/2r)^{-2}$; expanding, $1-m/r+m^2/2r^2$ against $1-m/r+3m^2/4r^2$ — they agree to first order and part at $O(m^2/r^2)$, with $N\Omega = 1-m^2/4r^2$ **[V]**. Imposing $N\Omega = 1$ exactly gives the Majumdar–Papapetrou form and hence extremal Reissner–Nordström, $Q = M$ — every body an extremal black hole, **excluded** **[V/T]**. Deriving the locking from an action, rather than imposing it, is open **[O]**.

## III.3 The degree-of-freedom split, on the physical real shell [V/S]

A metric on the three-manifold $S^3$ has $3\cdot4/2 = 6$ components. Adapted to the circle bundle $S^3\to S^2$:

| block | count | candidate content |
|:--|--:|:--|
| shell 2-metric | 3 | even gravitational geometry |
| fiber length $L_H$ | 1 | even gravitational scale |
| connection cross-terms | 2 | odd / placement sector |
| **total** | **6** | ✓ **[V]** |

So the attractive $3+1+2$ partition survives — **on the physical real slice**. Version 15 does not assert it for the full complex shell; the complex homogeneous bundle is the analytic parent, and the real slice is where the metric count is performed.

**Only half is structurally motivated [O].** Quotient gravity determines the even base geometry and Law I locks the fiber length to it — that is the $3+1$. That odd matter must occupy the remaining $2$ is a conjecture until the coupling is derived. **The reason for retaining it is stronger than before**: the connection is no longer attached to an arbitrary circle, but to the compact real fiber of the spin-shell lift, and the real-shell metric leaves exactly two components beyond base and length.

---

# PART IV — IDENTITIES AND THEOREMS

*These are the durable results of versions 6 through 14. They are stated here in full because they are the theory's content; each must be re-derived in the new architecture rather than assumed, and Part VIII lists that as a regression test.*

## IV.1 The twin theorem [V]

The static operator on the closed gravity base is $\Delta_{S^3}+3$. Its Green's function has a **same-sign** pole at the antipode; its kernel is the dipoles; so a source must have zero dipole, and **a lone mass has no static solution**. A ball at the pole has dipole $0.169\neq0$, and a numerical solve returns the kernel mode as its symptom. **The twin is forced, not permitted.**

## IV.2 Closure and the $G$ identity [D]

The gravity base is the Einstein static universe: $\Lambda = 1/\ell^2$, $\bar\rho = 1/4\pi\ell^2$. The meridian flux through every latitude is $M_c$, and closure fixes it:

$$\frac{GM_c}{c^2\ell} = \frac{\pi}{2}$$

**A constraint, not a derivation.** And it is a horizon statement: $r_s(M_c) = 2GM_c/c^2 = \pi\ell$, exactly the antipodal distance on $S^3(\ell)$ — a closed static universe is marginally its own horizon.

## IV.3 Law I as the fiber-length equation [V]

Weak-field statics are conformally round, and the Hamiltonian constraint linearizes to

$$(\Delta_{S^3}+3)\,\delta\phi = -2\pi\,\delta\rho_+$$

the twin-theorem operator acting on the conformal factor. For a ball with its twin, $\phi^2 = 2.017$ at the ball's center and identically at the **empty** twin, agreeing to $10^{-11}$ **[V]**.

## IV.4 Weyl from the fiber length [V]

$$E_{ij} = -2\big[\nabla_i\nabla_j\phi\big]^{\rm TF},\qquad \phi = \sqrt{L_H/2\pi\ell}$$

The Hessian's trace is the matter; its trace-free part is the tidal field. For Schwarzschild the eigenvalues are $(m/r^3)(1,-\tfrac12,-\tfrac12)$ — Petrov type D, with repeated principal null directions along $\partial_t\pm\widehat{\nabla L_H}$, the directions of steepest fiber-length change.

## IV.5 The metric, written out [V/D]

$$ds^2 = -N^2dt^2 + L_H^2\big(d\theta+\alpha\big)^2 + \kappa^2du^2 + \phi^4g_{S^3}$$

with $N$ and $L_H$ from Law I, $\alpha$ the Law III connection, $u$ the meridian and $\kappa$ its scale. For a point mass, $\phi = 1 + GM/2r + O(r^2/\ell^2)$, and the four-dimensional part is **isotropic Schwarzschild exactly**:

$$ds^2_4 = -\left(\frac{1-GM/2r}{1+GM/2r}\right)^2dt^2 + \left(1+\frac{GM}{2r}\right)^4\big(dr^2+r^2d\Omega_2^2\big)$$

with closure corrections at $O(r^2/\ell^2)$ — $4\times10^{-15}$ at 10 kpc for $\ell = 63$ Gpc. Shells have proper area $4\pi r^2(1+GM/2r)^4$. The meridian scale $\kappa$ remains undetermined **[O]**.

## IV.6 Black holes [D/O]

If the canonical flux gravitates with coupling $g_2$, it adds a Reissner–Nordström term with an effective charge:

$$f(r) = 1 - \frac{2GM}{c^2r} + \frac{GP^2}{c^4r^2},\qquad P = g_2\frac{M}{m_{\rm unit}}$$

The Newtonian term is untouched; the horizon moves to $r_\pm = (GM/c^2)(1\pm\sqrt{1-P^2/M^2})$; extremality tightens to $M^2\geq Q^2+P^2$ **universally**, since every hole carries $P\propto M$. Mercury's perihelion bounds it: the repulsive term shifts the advance by $-(P/M)^2/6$, and agreement to $10^{-4}$ gives

$$g_2/m_{\rm unit} = P/M < 0.024$$

Lunar ranging gives nothing useful; ringdowns test $P/M$ only at the $0.1$–$0.3$ level. The double pulsar can tighten it **[O]**.

## IV.7 Charge and the twin [V/D]

Gauss on a closed section forces a compensating charge somewhere, and the seed puts nothing at the twin. With the compensator wherever the other charges are, the field of a charge $Q$ is regular at the twin and vanishes there — verified, $|E|\to0$ **linearly**. **The twin carries gravitational shape with no electromagnetic content**; a charged secondary's twin holds the $Q^2/r^2$ term as a *tidal* charge with $\nabla\cdot E = 0$ and $E = 0$.

## IV.8 Orbits and the $v^2$ family [V]

On the gravity base a secondary is a well in the jellium, and closed-universe orbits are retrograde-precessing rosettes: apsidal advance $1.945\pi$ per radial period at small apocenter, falling to $1.836\pi$ mid-disk. The kinematic pattern speed $\Omega-\kappa/2$ falls by a factor 10 across a disk where Kepler alone gives 20 — **the closure term halves the winding rate of kinematic spirals.**

For circular orbits at colatitude $\chi$, $v^2(\chi) = \Phi'(\chi)\tan\chi$, and at the equator $\Phi'(\pi/2) = 0$ by twin symmetry, so $v^2_{\rm eq} = -\Phi''(\pi/2)$. Solving for a lump holding a fraction $f$ of the closure mass gives, converged as the lump shrinks,

$$v^2_{\rm eq} = 2.352\,f = 1.497\,\frac{GM}{\ell}$$

**independent of how the lump is packed** — only the monopole survives at the equator. *(This corrects an earlier quotation of $4GM/\pi\ell$, which was 15% low* **[V/R]***.)*

## IV.9 The lumped-mass limit [V/D]

Closure fixes the total at $M_{\rm tot} = \pi\ell/2$, so a secondary of mass $M$ holds a fraction $f = M/M_{\rm tot}$ of it. At $f = 1$ the lump's Schwarzschild radius is $\pi\ell$ — **the antipodal distance, the diameter of the universe.** Nothing is outside it; there are no orbits because there is no exterior. Law II is untroubled: the foliation is intact at $f = 1$; what fails is the base geometry.

## IV.10 The Keplerian limit, quantified [V]

Near a point mass the Green's function goes as $1/\sin\chi$, so with $r = \ell\chi$,

$$\Phi(r) = -\frac{Gm}{r}\left[1+\frac{r^2}{6\ell^2}+O(r^4/\ell^4)\right]$$

The closure correction is $4\times10^{-15}$ at 10 kpc and $4\times10^{-45}$ at 1 AU. The jellium's correction overtakes $Gm/r^2$ only where the enclosed background mass equals $m$: **1.2 Mpc for a $10^{12}M_\odot$ galaxy, 0.12 kpc for the Sun.** Inside any galaxy and throughout any planetary system, motion is Keplerian to better than a part in $10^{14}$.

## IV.11 The static wall [T]

On a static geometry Killing energy is conserved and there is no redshift. **A theorem about the arena, not a gap in it.** Every route to Hubble's law within the static theory ends at the seed's own symmetry: the twin's well is identical to the source's, and identical wells cannot shift light between them.

---

# PART V — THE SEED

## V.1 Light resolves; gravity quotients [S/T]

Matter and Maxwell fields live on $B_{\rm rep}$. An optical event is a point $x\in B_{\rm rep}$, so **light distinguishes $x$ from $\tau x$**: the electromagnetic field is not meridian-averaged.

Gravity first applies $q:\mathcal{M}\to B_{\rm grav}$, and $q(x) = q(\tau x)$. So its operation is

$$\text{gravity} = q^*\circ\,\text{Einstein}\,\circ q_*$$

push the resolved source down to the class, solve, pull the solution back up.

## V.2 The barren twin [D/S]

Take $T(x)\neq0$ and $T(\tau x) = 0$. The quotiented source is $T^{(g)}([x]) = T(x)$, and the metric solved at $[x]$ lifts to **both** representatives. Therefore

$$T(\tau x) = 0\qquad\text{while}\qquad \text{curvature at }\tau x\neq0$$

> **This is the seed.** No dark particle has been placed at the twin. The discrepancy is a difference in **resolution** — light resolves a representative, gravity resolves a class — and the two bases of Part 0 are what make that sentence sayable.

## V.3 Why the twin is unobserved, twice over [V]

It is **empty**: no matter to emit, absorb or scatter, and electromagnetically barren by §IV.7. And its light could not have arrived in any case: the crossing time is $\pi\ell/c = 646$ Gyr at $\ell = 63$ Gpc, forty-seven times the age of the universe. **Two independent reasons, neither requiring a new coupling.**

---

# PART VI — NEWMAN–JANIS AND KERR

## VI.1 The construction, in six steps [T/V]

**1.** Put Schwarzschild in Kerr–Schild form, $g_{ab} = \eta_{ab}+2Hk_ak_b$ with $H = M/r$ and $k$ null and geodesic for both metrics. Exact, not linearized.

**2.** Note the whole solution rests on one harmonic function: $\nabla^2(1/r) = 0$ away from the origin **[V]**.

**3.** Complexify and displace the source along the imaginary axis, $z\to z-ia$:

$$\frac{1}{\sqrt{x^2+y^2+z^2}}\ \longrightarrow\ \frac{1}{\sqrt{x^2+y^2+(z-ia)^2}}$$

still harmonic **[V]** — *nothing is added; a source is moved.*

**4.** The complex distance vanishes where $-2az = 0$ and $x^2+y^2+z^2 = a^2$, i.e. $z = 0$ and $x^2+y^2 = a^2$: **a ring of radius $a$** **[V]**. Schwarzschild's point singularity has become Kerr's ring.

**5.** With the oblate radius $R$ defined by $\frac{x^2+y^2}{R^2+a^2}+\frac{z^2}{R^2} = 1$, the complex distance is $R+ia\cos\theta$ and $H = MR^3/(R^4+a^2z^2)$ — **Kerr in Kerr–Schild form**.

**6.** The angular momentum is $J = Ma$, so $a = J/M$: **the imaginary displacement is the spin per unit mass.**

## VI.2 Where this happens, and where it does not [S/D]

Newman–Janis acts on the **complexification of the representational base**:

$$B_{\rm rep}\hookrightarrow B_{{\rm rep},\mathbb{C}}\xrightarrow{\text{shift}}B_{{\rm rep},\mathbb{C}}\xrightarrow{\text{real slice}}B_{\rm rep}^{\rm Kerr}$$

And the canonical shells **follow the complex worldline**: at every point and radius the shell is $Q^2_{\rm aff}$ with lift $SL(2,\mathbb{C})$, so the displacement moves the center of the entire shell system. Two roles stay separate:

$$\text{Kerr rotation} = \text{complex worldline displacement},\qquad \text{the fiber} = \text{the shell's spin lift}$$

> **Rotation is not winding around the fiber.** Earlier versions tried to make one construction carry rotation, the seed, the fiber and the dynamics at once. Here complexified spacetime handles Newman–Janis, spin geometry handles the shell lift, the meridians handle the seed, and Einstein's equations handle the fiber length. **No single construction is asked to do all four jobs.**

## VI.3 The $g = 2$ signpost [T/O]

Kerr–Newman satisfies $J = Ma$ and $\mu = Qa$, hence $\mu = (Q/M)J$ — the conventional $g = 2$ relation. Complex-worldline approaches to Einstein–Maxwell give a further reason to keep the complex center visible. **A future bridge target, not a derivation of the electron.**

---

# PART VII — SPIN, AND THE CATEGORY FIREWALL

## VII.1 What the spin geometry does supply [T]

Newman–Penrose two-spinors transform under $SL(2,\mathbb{C})$ — the same group that lifts the complex shell (§I.6). The canonical fiber's compact part is therefore the spin phase, and the theory may legitimately constrain: spin structures, phase holonomy, chirality, principal spinors, allowed connections, topological charge, geometric relations among mass, charge and rotation, and the availability of zero modes.

## VII.2 What it does not [T]

$$\text{spinorial shell geometry}\ \not\Rightarrow\ \text{fermionic anticommutation}$$

Newman–Penrose spinors are **classical, commuting** geometric spinors. Grassmann-odd quantum fields are a further structure, and the implication is blocked by type, not by difficulty: a Grassmann number satisfies $\theta^2 = 0$, which is what makes $\psi^\dagger(x)^2 = 0$ and hence the exclusion principle, and nothing in a spin bundle produces it. **Any such derivation remains open.**

## VII.3 Statistics and exclusion, unchanged [T]

Finkelstein–Rubinstein: in any 3-manifold, exchanging two identical particles is *locally* homotopic to rotating one by $2\pi$ in place, so the exchange sign equals the frame-$2\pi$ sign $(-1)^{2s}$. The argument is local and does not see the twin loop. **Anticommutation and the Pauli exclusion principle hold exactly as in ordinary quantum field theory.**

## VII.4 Twin parity [T/D]

The frame bundle of $\mathbb{RP}^3 = SO(3)$ is $SO(3)\times SO(3)$, with $\pi_1 = \mathbb{Z}_2\times\mathbb{Z}_2$: **two independent** generators, a frame rotation (giving spin) and a trip around the twin loop (giving a parity $\tau = \pm1$). $\tau$ is a discrete quantum number independent of spin and statistics, and it is fixed by the sign a field acquires on transport through the primary. Which species are twin-odd is open **[O]**.

---

# PART VIII — STATIC REGRESSION AND TESTS

## VIII.1 The old geometry must be recovered, not assumed [S/O]

The intended static specialization is

$$\mathcal{M}_{\rm static}\sim\mathbb{R}_t\times S^4,\qquad B_{\rm rep}^{\rm static}\sim\mathbb{R}_t\times S^3,\qquad B_{\rm grav}^{\rm static}\sim\mathbb{R}_t\times\mathbb{RP}^3$$

with $S^3\hookrightarrow S^4\xrightarrow{/\text{meridians}}\mathbb{RP}^3$ spatially, and over every physical shell the compact canonical lift $U(1)\to S^3\to S^2$. Dimensions check: $1+4 = 5$, $1+3 = 4$, $1+3 = 4$ **[V]**.

**Order of recovery, as a regression test and not an assumption [O]:** derive the static real form of the middle space; recover the meridian quotient; derive the quotient metric and its Green's function; recover the geodesic and orbit equations; **only then** reassert the results of Part IV.

## VIII.2 The golf ball [V/D]

Does a golf ball in a vacuum chamber on Earth enclose its own flux? **Topologically yes** — Law III is linear, and for a small sphere around it $\frac{1}{2\pi}\int F = M_g/m_{\rm unit}$ exactly; Chern numbers add and are localized, and Earth cannot smear away an integer. **Geometrically Earth dominates** — the flux falls as $N/2r^2$, the same law as gravity, and the ball's field exceeds Earth's only inside $r = R_\oplus\sqrt{M_g/M_\oplus} = 0.56\,\mu$m, which is precisely its gravitational neutral point.

**The quantization fork decides whether there is any winding at all.** With $m_{\rm unit} = m_p$ the ball winds $2.7\times10^{25}$ times and Earth $3.6\times10^{51}$; with $m_{\rm unit}\sim10^{14}M_\odot$ both wind zero times and the whole sector is absent from the solar system. A spherically symmetric chamber contributes nothing inside, by the shell theorem. Nothing in the laboratory detects either answer: the photon is neutral under the fiber.

## VIII.3 The Machian direction [T/D/V]

Vacuum general relativity already has the symmetry $(g,M)\to(\lambda^2g,\lambda M)$: every Schwarzschild exterior *is* a rescaled copy of every other, with mass the scale. So "isomorphic shells up to scale" is true and yields nothing new — the scale it fixes is mass, not size, and compactness $r_s/R$ ($1.4\times10^{-9}$ for Earth, $3.2\times10^{-27}$ for a golf ball) is untouched.

Rescaling $r_s$ with $GM$ fixed is **inconsistent**, since $r_s = 2GM/c^2$ is one number whenever the exterior has a single source. The realizable version is already present: the flux energy $|F_\oplus+F_g|^2$ has a **cross term** that exists only when Earth is present, $1.5\times10^9$ times the ball's own term at its surface — so the ball's near field genuinely differs alone and near Earth. Bounded by Mercury at $\delta r_s/r_s<3\times10^{-4}$ **[D]**.

**A local Mach relation fails [V]:** reading $GM/c^2\ell = \pi/2$ with $\ell$ a sphere of influence gives $5\times10^{11}G$ for Earth and $3\times10^{22}G$ for the golf ball. The Mach relation closes a *universe*.

**Emergent $G$ [D]:** $G$ is emergent iff mass has a $G$-free definition, and general relativity has none — ADM and Komar masses are defined through $G$. The Hamiltonian constraint holds on every slice but constrains the product $G\rho$ and cannot separate the factors.

## VIII.4 The required constructions [O]

1. Construct an explicit $E$ whose shell restrictions are the stated $SL(2,\mathbb{C})$ lifts, over $\mathcal{M}$ minus the secondary meridians (§II.1), with a smooth five-dimensional quotient away from controlled singular loci.
2. Show the complex bundle's reduction to $U(1)\to SU(2)\to S^2$ on the Lorentzian slice, covariantly.
3. Define the complex normal bundle and shell lift along a general non-null complex worldline.
4. Carry the shell lift consistently through Schwarzschild $\to$ Kerr.
5. **Derive** $L_H = \Omega L_H^{\rm ref}$ rather than impose it.
6. Determine whether $T_-$ genuinely occupies the two connection components.
7. Derive the meridian foliation from canonical data.
8. Recover $S^4\to\mathbb{RP}^3$ and the barren twin.
9. Re-derive the $v^2$ family in the recovered static sector.
10. Compute what stress-energy an observer infers by applying Einstein's equation on $B_{\rm rep}$ instead of $B_{\rm grav}$ — **the dark-sector prediction**.
11. Verify the twin stays optically barren.
12. Keep the spin-statistics firewall: do not identify the geometric spin lift with Grassmann parity.

---

# PART IX — THE ACTION TARGET [O]

A successful action should make both information reductions automatic:

$$S = S_{\rm EH}[B_{\rm grav},g_G] + S_{\rm matter}[B_{\rm rep},\psi,A] + S_{\rm can}[E,\hat g,\mathcal{A}_H,U_{\rm mer}]$$

Variation with respect to $g_G$ should produce the meridian-reduced source; constraints on the canonical metric should produce the fiber-length locking; and the connection equation should either derive the $J_-$ law or show that it was the wrong use of the remaining freedom. **Until such an action exists, the split is architectural rather than final.**

---

# PART X — RETIRED AND OPEN

## X.1 Retired, with reasons

| item | reason |
|:--|:--|
| the middle space as the axiom | it is **derived** from the canonical space (§II.2) |
| "representational middle space" / "quotiented middle space" | both are **bases**; the middle space is the single derived five-dimensional layer |
| a real $S^2$ shell used *before* complexification | at the analytic level it is the affine quadric; the 2-sphere is its real form (§I.2) |
| the projective null-cone quadric as the default source shell | that object belongs to null-direction geometry, not fixed-radius shells (§I.7) |
| $TS^4$ as the arena (version 14) | replaced; it made the fiber contractible and cost Law III its home |
| an external fundamental $\mathbb{R}_t$ | time belongs to the Lorentzian real structure |
| the Hopf fiber *as* Kerr rotation | rotation is complex worldline displacement; the fiber is the shell's spin lift (§VI.2) |
| an extra $U(1)$ with no spin-geometric origin | the circle is now the compact real form of $\mathbb{C}^\times\subset SL(2,\mathbb{C})$ (§I.3) |
| geometric Weyl spinor $\Rightarrow$ quantum Grassmann fermion | blocked by type (§VII.2) |
| $v^2_{\rm eq} = 4GM/\pi\ell$ | 15% low; the converged value is $1.497\,GM/\ell$ (§IV.8) |
| $N\Omega = 1$ as an **exact** condition | it gives Majumdar–Papapetrou and hence extremal charge for every body (§III.2) |
| time as emergent from a fiber's latitude (version 12) | a type error: a complex structure has $J^2 = -1$, no real eigenvectors, and *pairs* directions where time must *select* one |

## X.2 Open

1. **Global existence of $E$**, and the meridian-removal obstruction of §II.1 — Law 0 cannot hold over an unpunctured $S^4$, since $H^2(S^4) = 0$ makes every circle bundle trivial and every shell restriction $S^2\times S^1$ rather than $S^3$ **[V]**. **The first thing this version owes.**
2. **The odd-sector coupling** (§III.3): whether $T_-$ occupies the two connection components.
3. **Deriving the fiber-length locking** from an action (§III.2).
4. **The meridian foliation's equation** (Law II).
5. **Time:** an input, belonging to the Lorentzian real structure; its uniqueness is not derived.
6. **The static regression** (§VIII.1), in the stated order.
7. **The dark-sector calculation** (§VIII.4, item 10) — the theory's sharpest available prediction.
8. **The quantization fork:** $m_{\rm unit}$ a particle mass or $\sim10^{14}M_\odot$.
9. **$g_2/m_{\rm unit}$:** below $0.024$ from Mercury; the double pulsar can tighten it.
10. **The meridian scale $\kappa$** (§IV.5).
11. **Twin parity assignments** (§VII.4).
12. **Emergent $G$** (§VIII.3): requires a $G$-free definition of mass.
13. **Inherited:** the AdS uplift; the two arenas; the literature review.

---

## Reference card, version 15

| topic | statement |
|:--|:--|
| **axiom** | the canonical space $E$, not the middle space |
| **first quotient** | $E/U(1)_H = \mathcal{M}$, the middle space; forgets the spin phase |
| **second quotient** | $\mathcal{M}/U_{\rm mer} = B_{\rm grav}$; forgets where along the meridian |
| **representational base** | $B_{\rm rep}\hookrightarrow\mathcal{M}$, a **bisection**: two points per gravity fiber |
| **the seed** | light resolves a representative, gravity resolves a class; the second point may be **barren** |
| **complex shell** | $\Sigma^\mathbb{C}_{\gamma,R}\cong Q^2_{\rm aff}$, an affine quadric in the complexified normal 3-space |
| **complex Hopf lift** | $\mathbb{C}^\times\to SL(2,\mathbb{C})\to SL(2,\mathbb{C})/\mathbb{C}^\times$; $6-2 = 4$ ✓ |
| **physical real form** | $U(1)\to SU(2)\simeq S^3\to S^2$; the Hopf fibration, **recovered not assumed** |
| **why not bolted on** | $SL(2,\mathbb{C})$ is already the Newman–Penrose spin group |
| **why isotropic** | shell and lift are homogeneous; the fiber is a stabilizer, not a chosen longitude |
| **Law I** | Einstein on $B_{\rm grav}$ with $T^{(g)} = T(x)+T(\tau x)$; also fixes $L_H = \Omega L_H^{\rm ref}$ |
| **$G$ identity** | $GM_c/c^2\ell = \pi/2$; equivalently $r_s(M_c) = \pi\ell$, the antipodal distance |
| **partition** | $6 = 3+1+2$ on the real shell $S^3\to S^2$ ✓; only $3+1$ is motivated |
| **black holes** | $f = 1-2GM/c^2r+GP^2/c^4r^2$, $P = g_2M/m_{\rm unit}$; $M^2\geq Q^2+P^2$; $P/M<0.024$ |
| **$v^2$ plateau** | $1.497\,GM/\ell$, packing-independent; at $f = 1$, $r_s = \pi\ell$ and no exterior |
| **Keplerian limit** | corrections $4\times10^{-15}$ at 10 kpc; jellium crossover at 1.2 Mpc for a galaxy |
| **Kerr** | complex worldline displacement, $a = J/M$; ring at $x^2+y^2 = a^2$; shells follow the displaced center |
| **rotation vs fiber** | rotation is **not** winding around the fiber; four jobs, four structures |
| **time** | an input, from the Lorentzian real structure |
| **Grassmann parity** | not derived, and blocked by type |
| **the obstruction** | $H^2(S^4) = 0$: Law 0 needs the secondary meridians removed, as every earlier version did |
