# Projective Gravity — Version 15.5

### The Canonical Space First: a complex Hopf lift of source shells, a derived middle space, and two bases

> **What this document is.** A complete, self-contained statement of the theory. It assumes no earlier document: every term is defined in Part 0, every law is stated with its equation, and every identity imported from an earlier version is restated in full rather than cited.
>
> **The architectural change.** Versions 6 through 14 posited a space and then decorated it with a fiber. Version 15 inverts the order. The **canonical space** $E$ is the axiom; the middle space is *derived* from it by quotienting a circle; and the middle space then has **two** four-dimensional readouts, which earlier versions ran together — one where matter and light are localized, one where gravity acts.
>
> **What the fiber now is.** A shell of fixed nonzero radius about a *complex* source worldline is not a real 2-sphere: in the complexified normal space it is the affine quadric $Q^2_{\rm aff}$, a complex surface. And that surface is a homogeneous space of the complex spin group,
> $$\mathbb{C}^\times\ \longrightarrow\ SL(2,\mathbb{C})\ \longrightarrow\ Q^2_{\rm aff}\cong SL(2,\mathbb{C})/\mathbb{C}^\times$$
> whose compact real form is the ordinary Hopf fibration $U(1)\to SU(2)\simeq S^3\to S^2$. **So the Hopf character is no longer decoration. It is the compact real form of the complex spin geometry belonging to an isotropic shell**, and it was the right guess for the wrong reason in every version that assumed it.
>
> **The centrepiece.**
> $$\boxed{\ \text{spin geometry fixes the fiber's topology;}\qquad\text{gravity fixes only its metric length.}\ }$$
> These are different kinds of information. The spin structure says what the fiber **is** — $U(1)\hookrightarrow SU(2)\simeq S^3\to S^2$, the **unit Hopf class** — and Law I says how large that already-existing circle is at each base point, $L_H = \mathcal{F}[g_G]$. Changing $L_H$ does not change the Chern class or make it a different bundle. One fixed spin-derived Hopf bundle, whose fibers stretch and contract with the gravitational geometry.
>
> **What this version retires.** Because the fiber is now *derived*, its Chern class is **fixed at the unit Hopf class** — not a free integer. That contradicts the inherited second-order sector, in which $c_1 = M_-/m_{\rm unit}$ was mass-dependent with a free parameter. **The whole flux branch therefore goes** (§X.1): the quantum $m_{\rm unit}$, the quantization fork, mass-proportional winding counts, the Reissner–Nordström-like charge $P$ and its Mercury bound, and the candidate source law $dF_H = 2\pi\star J_-$. This is not a loss of content but the removal of an inconsistency — and it takes two free parameters with it.
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
| **gravity base** | $B_{\rm grav} = \mathcal{M}/U_{\rm mer}$ | a *quotient* by the meridian structure. Where Law I acts | 4 |

The two bases have the same dimension and arise by opposite operations:

$$B_{\rm rep} = \text{a resolved representative},\qquad B_{\rm grav} = \text{an equivalence class}$$

Conflating them was the error that made the seed look like a postulate.

## 0.2 Terms

| term | meaning |
|:--|:--|
| **shell** | the set of points at fixed nonzero distance from a source worldline, within its normal space |
| **complex shell** $\Sigma^\mathbb{C}_{\gamma,R}$ | the same at fixed *complex* radius about a *complex* worldline: an affine quadric, a complex surface |
| **spin phase** $U(1)_H$ | the compact fiber of the shell lift; the physical real form of the complex stabilizer $\mathbb{C}^\times$ |
| **meridian** | a leaf of the one-dimensional **meridian structure** $U_{\rm mer}$. *Standard usage in this document:* $U_{\rm mer}$ is a **meridian structure**; its **regular part** is a foliation; its **static singular case** is a **pencil**, since distinct meridians meet at the poles. In the static limit a leaf is a great circle of $S^4$ through both poles |
| **twin** | given $x\in B_{\rm rep}$, the other point $\tau x$ of the same meridian, with $\tau^2 = 1$ and $q(x) = q(\tau x)$ |
| **barren twin** | a twin carrying no matter, at which gravitational curvature is nevertheless nonzero. **The seed** |
| **$T_\pm$** | $T_\pm(x) = T(x)\pm T(\tau x)$: the even and odd parts of matter under the twin map |
| **jellium** | the uniform background density of the gravity base, supplied by the primary |
| **primary** | the dominant mass at a degeneracy of the meridian structure |
| **conformal factor** | $\phi$, with $g_3 = \phi^4g_{\rm ref}$ and $\Omega\equiv\phi^2$ |
| **fiber length** $L_H$ | the circumference the canonical metric assigns the $U(1)_H$ orbit |

## 0.3 The tower

$$E^{(6)}\ \xrightarrow{\ /\,U(1)_H\ }\ \mathcal{M}^{(5)}\ \xrightarrow{\ /\,U_{\rm mer}\ }\ B_{\rm grav}^{(4)},\qquad B_{\rm rep}^{(4)}\hookrightarrow\mathcal{M}^{(5)}$$

Verified consistent: a circle quotient drops one dimension, a one-dimensional meridian quotient drops one more, and an embedded hypersurface of a five-manifold is four-dimensional **[V]**. Two distinct losses of information occur, and they must not be confused:

| quotient | what is forgotten |
|:--|:--|
| $E\to\mathcal{M}$ | the **spin phase** |
| $\mathcal{M}\to B_{\rm grav}$ | **where along the meridian** the matter sits |

## 0.4 What is axiomatic

The primitive data are $\big(E,\ \hat g,\ U(1)_H,\ \mathcal{A}_H,\ \rho_E,\ \mathcal{U}_{\rm mer}\big)$: the canonical space, its metric, the fiber action, its connection, the real-analytic structure needed to complexify shells, and the meridian structure of the quotient. Everything else — the middle space, both bases, the seed — is derived. **The theory is top-down.**

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

## I.6 The shell fiber *is* the spinor phase [T/V]

*Noting that the same group appears twice would be a coincidence-of-names argument. The identification can be made explicit, and it is an equality of **actions**, not of group labels.*

$SL(2,\mathbb{C})$ is already the spin group of four-dimensional Lorentzian two-spinor geometry — the group under which Newman–Penrose spinors transform. The question is whether the $U(1)$ that the shell quotients is the *same* circle as the spinor's phase. It is.

**The construction.** Identify a normalized spinor $\psi = (z_1,z_2)^{\mathsf T}\in S^3\subset\mathbb{C}^2$ with the group element

$$U(\psi) = \begin{pmatrix} z_1 & -\bar z_2\\ z_2 & \bar z_1\end{pmatrix}\ \in\ SU(2)$$

which is unitary with unit determinant precisely because $|z_1|^2+|z_2|^2 = 1$ **[V]**. Now act on the right by the diagonal stabilizer

$$h_\theta = \begin{pmatrix} e^{i\theta} & 0\\ 0 & e^{-i\theta}\end{pmatrix}$$

The first column of $U(\psi)h_\theta$ is $e^{i\theta}\psi$ **[V]**.

> **The stabilizer $U(1)$ of $SU(2)/U(1)\simeq S^2$ acts on the normalized spinor column as ordinary phase multiplication.** Not the same group twice — *the same action*.

**And the Hopf map is the quotient by exactly that action [V].** With $n(\psi) = \big(2\,\mathrm{Re}(z_1\bar z_2),\,2\,\mathrm{Im}(z_1\bar z_2),\,|z_1|^2-|z_2|^2\big)$, one has $n(e^{i\theta}\psi) = n(\psi)$ identically — verified. So the shell $S^2$ is the space of spinors modulo phase, and the fiber is the phase.

**The complex version is the same statement [V].** $h_\lambda = \operatorname{diag}(\lambda,\lambda^{-1})\in SL(2,\mathbb{C})$ scales the first column by $\lambda\in\mathbb{C}^\times$ — verified. So the complex stabilizer is complex phase-and-scale on the spinor, and the compact real form recovers pure phase.

**This is the "not bolted on" claim, discharged.** Every earlier version had to *posit* a circle. Here the circle is the spinor phase of a group the theory already contains, acting in the way it already acts.

## I.7 What the complex shell is **not** [T]

At a point of complexified four-dimensional spacetime, the projectivized complex null cone is a different object — a projective quadric built from two independent chiral spinors, natural for **null directions**. The shell used here represents **fixed nonzero radius in the complexified rest space of a non-null worldline**. These must not be conflated:

$$\text{null-direction quadric}\ \neq\ \text{fixed-radius worldline shell}$$

The affine quadric is preferred because its three pieces complexify *together* and its real limits are exactly the three wanted (§I.4). The projective version does not have the $S^2$ limit for a source shell.

---

# PART II — THE CANONICAL SPACE AND THE TWO BASES

## II.1 Law 0 [S/O]

> ### ◆ LAW 0 — THE CANONICAL SPACE
> There exists a canonical space $E$ such that: (i) its quotient by the compact fiber action is the middle space, $\mathcal{M} = E/U(1)_H$; (ii) near a source worldline, its analytic continuation restricted to every nonzero-radius complex shell is the homogeneous bundle $\mathbb{C}^\times\to SL(2,\mathbb{C})\to Q^2_{\rm aff}$; (iii) on the physical rest-space shell this reduces to $U(1)\to SU(2)\to S^2$; (iv) the fiber carries a connection $\mathcal{A}_H$; (v) the metric $\hat g$ gives the compact fiber a length $L_H$.

**Two obstructions, and the second is the real problem.**

**(a) The cohomological one [V].** Condition (iii) cannot hold over an *unpunctured* static middle space: $H^2(S^4) = 0$, so every circle bundle over $\mathbb{R}_t\times S^4$ is trivial, and a trivial bundle restricts to $S^2\times S^1$ on each shell — **not** $S^3$. The Hopf lift needs a nontrivial class on the shell, which needs the secondary meridians removed. What the argument requires is precisely the **cohomological** statement, and no more: by Alexander duality,

$$H^2\big(S^4\setminus S^1;\mathbb{Z}\big)\ \cong\ \tilde H_1(S^1;\mathbb{Z})\ \cong\ \mathbb{Z}$$

which permits a nontrivial circle bundle **[T]**. *Earlier drafts asserted the stronger claim that the complement is homotopy equivalent to $S^2$. That holds for the standard unknotted embedding but not in general — 1-knots in $S^4$ exist, and a knotted complement can differ in $\pi_1$ and in higher homotopy. Duality sees only the homology of the removed circle, so it gives $H^2 = \mathbb{Z}$ either way, and the weaker statement carries no embedding debt* **[R]**. **Law 0 must therefore be stated over $\mathcal{M}$ minus the secondary meridians**; the architecture inherits that surgery rather than escaping it.

**(b) The global one, which is now the main construction problem [O].** Part I builds its shell on the **normal space** $N_\gamma$ — a space of *vectors*, not of spacetime points. Passing from normal vectors to nearby points of the middle space uses the exponential map, and that identification is **local**: curvature, cut loci and caustics obstruct it globally. So even granting (a), it does not follow that **one** global six-dimensional $E$ restricts to the unit Hopf bundle around **every** source worldline simultaneously.

> **That is the version's central open construction**, and it is a sharper problem than the ones it replaces. The local spin geometry of Part I is settled mathematics; whether it glues is not.

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
> with the source obtained by meridian reduction of resolved matter. Writing $r := q\circ\iota : B_{\rm rep}\to B_{\rm grav}$, which away from the singular set is a local diffeomorphism on each branch of the bisection, the reduction is
> $$T^{(g)}_b = \sum_{x\in r^{-1}(b)}\big((dr_x)^{-1}\big)^*T_x$$
> up to whatever density factor an action supplies. **The map $dr$ is what makes the sum well-typed**: tensors at $x$ and $\tau x$ live in different tangent spaces and cannot be added until the quotient supplies the identification. The shorthand $T^{(g)}([x]) = T(x)+T(\tau x)$ is this expression with that step suppressed. The same solution fixes the canonical fiber length (§III.2). Law I introduces **no additional scalar degree of freedom** — no dilaton, no radion, nothing with a $1/r$ coupling. **But recovery of the observed PPN parameters does not follow from that alone here**, because photons and detectors live on $B_{\rm rep}$ while Law I solves on $B_{\rm grav}$: it additionally requires the induced metric on $B_{\rm rep}$ to reproduce general relativity's optical metric, and the map $g_G\to g_{\rm rep}$ has not been derived **[O]**.

> ### ◆ LAW II — THE MERIDIANS
> The middle space carries a one-dimensional **meridian structure** $U_{\rm mer}$, regular as a foliation away from controlled singular sets. (In the static limit it is a *pencil*: distinct meridians meet at the poles, so it is not a foliation of all of $S^4$ — §VIII.1.) The representational base resolves its representatives; gravity quotients it. In the static spherical limit it must reduce to the great circles of $S^4$ through both poles, with quotient $\mathbb{RP}^3$. The general equation selecting the meridian structure is **open** **[O]**.

> ### ◆ STRUCTURE III — THE CANONICAL CONNECTION
> *Numbered III for continuity with earlier versions, but **not a law**: there is no field equation here, and calling it one would misdescribe the document's own architecture.*
> The canonical fiber carries a connection $\mathcal{A}_H$ with curvature $F_H = d\mathcal{A}_H$. Its **topological class is fixed by the spin geometry**: each oriented shell carries the **unit Hopf class $c_1 = 1$** — or $c_1 = -1$ under the opposite *global* orientation convention, which is one convention for the whole construction and not a choice made shell by shell. It is independent of the source's mass and of any parameter. The reference connection is the canonical Hopf connection, and deformations away from it leave $c_1$ untouched, since $\int_{S^2}d\alpha = 0$. In an adapted metric they appear as **two local connection cross-components**, whose gauge-invariant content is fixed only after quotienting the $U(1)$ gauge freedom $A\mapsto A+d\lambda$ (§III.3). **Nothing in this version sources them, and no matter-coupling law is asserted** **[O]**.

> ### ◆ LAW IV — ELECTROMAGNETISM
> Maxwell on $B_{\rm rep}$, with $\epsilon = \mu_{\rm EM} = 1$. Light resolves meridian representatives and does **not** perform the gravity quotient. The field lives downstairs, so its pullback to $E$ is **$U(1)_H$-invariant** — it does not couple to the fiber. (Earlier drafts called it a "zero mode," which implies a Kaluza–Klein expansion this version does not perform; see §X.1.)

## III.1 What each is, and what you deduce from it [D]

The epistemic architecture, at a glance:

| | role |
|:--|:--|
| **Law 0** | existence and ontology |
| **Law I** | dynamics |
| **Law II** | meridian structure |
| **Structure III** | canonical connection — no dynamics |
| **Law IV** | electromagnetism |


| | **Law 0** | **Law I** | **Law II** | **Structure III** | **Law IV** |
|:--|:--|:--|:--|:--|:--|
| **is** | an existence axiom | Einstein's equations | a meridian structure, a **pencil** where singular | a **connection structure**, not a field equation | Maxwell |
| **lives on** | $E$ | $B_{\rm grav}$ | $\mathcal{M}$ | the canonical fiber | $B_{\rm rep}$ |
| **determines** | the arena and its fiber | $g_G$, hence $\Omega$, hence $L_H$ | the twin pairing and $B_{\rm grav}$ | $\mathcal{A}_H$ | $\mathcal{F}$ |
| **sourced by** | — | $T_+$, the **even** part | the primary's degeneracies | **nothing** — the class is the fixed unit Hopf class | charge |
| **status** | structural | **dynamical** | kinematic | kinematic, **unsourced** | dynamical |
| **what you deduce** | the Hopf lift on every shell, with the unit Hopf class (§I.4) | orbits, tides, redshift, black-hole exteriors, the $v^2$ plateau (Part IV) | which points are twins; the seed (Part V) | connection holonomy relative to the canonical Hopf connection | the photon's kinematics; the twin's optical barrenness |

## III.2 Law I locks the fiber length [S]

In the conformal/static sector, with $g_{\rm spatial} = \Omega^2g_{\rm ref}$ and $\Omega = \phi^2$:

$$L_H = \Omega\,L_H^{\rm ref},\qquad\text{so to first order}\qquad \frac{\delta L_H}{L_H} = -\Phi$$

> **To first order, the fiber-length increase tracks the Newtonian potential**, and space stretches as much as time slows. The qualifier is not decorative: the relation parts company with Schwarzschild at $O(m^2/r^2)$, as the scope box below shows.

> **Gravity does not create the fiber — the spin geometry supplies it (Part I). Gravity determines its metric size.**

**The direction, stated carefully [D/O].** The defensible relation is **one-way**:

$$g_G\ \longmapsto\ L_H = \mathcal{F}[g_G]$$

Law I solves the base geometry; the canonical metric is then constrained so that its fiber length records part of that solution.

> **A two-way relation would be much stronger, and is not claimed.** $g_G$ is a metric; $L_H$ is a single scalar function. One scalar cannot in general reconstruct four-dimensional geometry — this document itself separately carries a lapse $N$, a conformal factor $\phi$, and a meridian scale $\kappa$ (§IV.5). A statement $L_H\Leftrightarrow g_G$ would hold only in a restricted one-function sector, and no such sector has been isolated here **[O]**.

**And the future emergence claim is a different one.** If an action is later exhibited in which varying the *full* canonical metric yields Einstein's equation downstairs, what that would establish is

$$\hat g\ \Longrightarrow\ g_G$$

**not** $L_H\Rightarrow g_G$. The six-dimensional metric carries far more than its fiber length, and conflating the two would claim emergence from a scalar that only emergence from the whole metric could support. That distinction is likely to matter later.

*Scope.* This is a first-order statement. Isotropic Schwarzschild has $N = (1-m/2r)/(1+m/2r)$ while $N = \Omega^{-1}$ would require $(1+m/2r)^{-2}$; expanding, $1-m/r+m^2/2r^2$ against $1-m/r+3m^2/4r^2$ — they agree to first order and part at $O(m^2/r^2)$, with $N\Omega = 1-m^2/4r^2$ **[V]**. Imposing $N\Omega = 1$ exactly gives the Majumdar–Papapetrou form and hence extremal Reissner–Nordström, $Q = M$ — every body an extremal black hole, **excluded** **[V/T]**. Deriving the locking from an action, rather than imposing it, is open **[O]**.

## III.3 The metric-component decomposition, on the physical real shell [V/S]

A metric on the three-manifold $S^3$ has $3\cdot4/2 = 6$ components. Adapted to the circle bundle $S^3\to S^2$ they decompose as below. **This is a block count of metric components, not of physical propagating degrees of freedom** — gauge and diffeomorphism freedom would have to be removed for that, and is not:

| block | count | content |
|:--|--:|:--|
| shell 2-metric | 3 | the base geometry, from Law I |
| fiber length $L_H$ | 1 | the gravitational fiber scale, from Law I |
| connection cross-components | 2 | **open** — and *local components*, not gauge-invariant content |
| **total** | **6** | ✓ **[V]** |

So the attractive $3+1+2$ partition survives — **on the physical real slice**. Version 15 does not assert it for the full complex shell; the complex homogeneous bundle is the analytic parent, and the real slice is where the metric count is performed.

**Four of the six are assigned; two are not [D].** Gravity determines the shell geometry and Law I locks the fiber length to it — that is the $3+1$. The remaining $2$ are **left open**, deliberately.

> Earlier versions assigned those two to the odd matter sector, $T_-\to2$. **That assignment is retired** (§X.1) — it was made because there happened to be two of them, which is not a reason.
>
> **A stronger claim would be wrong, and is not made.** A connection may vary freely while its class stays fixed: under $F\mapsto F+d\alpha$ with $\alpha$ a global 1-form, $\int_{S^2}d\alpha = 0$ by Stokes, so $c_1$ is untouched **[T]**. Connections form an affine space over the 1-forms, all sharing one class. **So fixed $c_1$ does not forbid connection dynamics.** What it forbids is specifically the old *integrated flux law* $c_1\propto M_-/m_{\rm unit}$, which made the class itself mass-dependent. The position here is simply that **the connection is unsourced and its deformations unassigned** — no impossibility claim is needed or made.

The two are **local connection cross-components** of an adapted metric, not two physical degrees of freedom: a $U(1)$ connection on an $S^2$ patch has two local components, but $A\mapsto A+d\lambda$ is gauge, and the gauge-invariant content is fixed only after that freedom is quotiented. The same discipline applies here as to the six above. They may remain unassigned until the theory itself says what they do.

---

# PART IV — IDENTITIES AND THEOREMS

> ### ◆ A NOTE ON THE TAGS IN THIS PART
> Every result below was verified or derived **in the architecture of versions 6 through 14**. They are stated in full because they are the theory's content, but within version 15 they carry the tag **[C]** — *conditional on the static regression of §VIII.1*. Where a bracket below reads $[V]$ or $[D]$, it records the status of the original computation, not a claim that the result has been re-established here.
>
> **What the condition amounts to.** §VIII.1 splits the static limit into two parts: an **assumption [S]** that the meridian structure is the antipodal great-circle pencil, and a **derivation [D]** that such a pencil has quotient $\mathbb{RP}^3$. *The static limit as a whole is therefore not derived* — only its quotient is, and only given the pencil. Everything below is conditional on the assumption as well as on the remaining regression steps.

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

with $N$ and $L_H$ from Law I, $\alpha$ the connection of Structure III, $u$ the meridian and $\kappa$ its scale. For a point mass, $\phi = 1 + GM/2r + O(r^2/\ell^2)$, and the four-dimensional part is **isotropic Schwarzschild exactly**:

$$ds^2_4 = -\left(\frac{1-GM/2r}{1+GM/2r}\right)^2dt^2 + \left(1+\frac{GM}{2r}\right)^4\big(dr^2+r^2d\Omega_2^2\big)$$

with closure corrections at $O(r^2/\ell^2)$ — $4\times10^{-15}$ at 10 kpc for $\ell = 63$ Gpc. Shells have proper area $4\pi r^2(1+GM/2r)^4$. The meridian scale $\kappa$ remains undetermined **[O]**.

## IV.6 Black holes [T]

Nothing in this version adds a charge to a black hole. A neutral secondary has the ordinary Schwarzschild exterior on the gravity base; a charged one has ordinary Reissner–Nordström,

$$f(r) = 1 - \frac{2GM}{c^2r} + \frac{GQ^2}{c^4r^2},\qquad M^2\geq Q^2$$

with $Q$ the ordinary electric charge and no additional contribution.

> Earlier versions carried a second charge $P = g_2M/m_{\rm unit}$, built from the flux sector, which tightened extremality to $M^2\geq Q^2+P^2$ universally and was bounded by Mercury at $g_2/m_{\rm unit}<0.024$. **All of that is retired** (§X.1): with the fiber's Chern class fixed at $\pm1$ by spin geometry, there is no mass-proportional flux to gravitate and no parameter to bound.

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

## IV.11 The static wall [T/V]

> **Identical twin wells cannot generate a relative gravitational redshift between themselves.**

A static geometry has a timelike Killing vector, so Killing energy is conserved along null geodesics and $1+z = \sqrt{g_{tt}(\text{receiver})/g_{tt}(\text{emitter})}$. When emitter and receiver sit in **identical** wells the lapses are equal and $z = 0$ identically **[V]**. Since the seed makes the twin's well identical to the source's, no shift can arise between them, and every route to Hubble's law within the static theory ends there.

*A stronger sentence carried by earlier drafts — "on a static geometry there is no redshift" — is **false** and is retired (§X.1): Schwarzschild is static and redshifts ($z = 0.21$ from $6M$ to $100M$, $0.73$ from $3M$ to infinity)* **[V]**. *What staticity forbids is cosmological redshift from expansion, not gravitational redshift.*

---

# PART V — THE SEED

## V.1 Light resolves; gravity quotients [S/T]

Matter and Maxwell fields live on $B_{\rm rep}$. An optical event is a point $x\in B_{\rm rep}$, so **light distinguishes $x$ from $\tau x$**: the electromagnetic field is not meridian-averaged.

Gravity first applies $q:\mathcal{M}\to B_{\rm grav}$, and $q(x) = q(\tau x)$. So its operation is

$$\text{gravity} = r^*\circ\,\text{Einstein}\,\circ r_*$$

push the resolved source down to the class, solve, pull the solution back up — with **$r = q\circ\iota$ throughout, not $q$** **[T]**. The distinction matters: $q:\mathcal{M}^5\to B_{\rm grav}^4$ is a *submersion*, so $dq$ annihilates the meridian direction and $q^*g_G$ is **degenerate** on $\mathcal{M}$ — a rank-4 form, not a metric. Whereas $r$ is a local diffeomorphism on each branch, so

$$g^{(G)}_{\rm rep} = r^*g_G$$

is a genuine Lorentzian metric on the representational base. **This is the object that determines what light does**, and its relation to general relativity's optical metric is the open PPN question of Law I.

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

**3.** Complexify and displace the source along the imaginary axis, $z\to z-ia$. **This step supplies the characteristic Kerr complex structure; it is not by itself the whole derivation** — see the caveat below.

$$\frac{1}{\sqrt{x^2+y^2+z^2} }\ \longrightarrow\ \frac{1}{\sqrt{x^2+y^2+(z-ia)^2} }$$

still harmonic **[V]**.

**4.** The complex distance vanishes where $-2az = 0$ and $x^2+y^2+z^2 = a^2$, i.e. $z = 0$ and $x^2+y^2 = a^2$: **a ring of radius $a$** **[V]**. Schwarzschild's point singularity has become Kerr's ring.

**5.** With the oblate radius $R$ defined by $\frac{x^2+y^2}{R^2+a^2}+\frac{z^2}{R^2} = 1$, the complex distance is $R+ia\cos\theta$ and $H = MR^3/(R^4+a^2z^2)$ — **Kerr in Kerr–Schild form**.

**6.** The angular momentum is $J = Ma$, so $a = J/M$: **the imaginary displacement is the spin per unit mass.**

> ### ◆ WHAT THIS SEQUENCE DOES AND DOES NOT ESTABLISH [T/O]
> **The complex displacement supplies the characteristic Kerr complex structure; recovery of the full metric additionally uses the Kerr–Schild null-congruence construction.** The original Newman–Janis prescription also manipulates a null tetrad and applies a *reality prescription*, and generalized Newman–Janis algorithms are known to be ambiguous away from special cases — different reality prescriptions give different metrics. The six steps above are a faithful account of the *complex-structure* content, not a self-contained derivation, and the earlier phrase "nothing is added; a source is moved" overstated that **[R]**.

## VI.2 Where this happens, and where it does not [S/D]

Newman–Janis acts on the **complexification of the representational base**:

$$B_{\rm rep}\hookrightarrow B_{ {\rm rep},\mathbb{C} }\xrightarrow{\text{shift} }B_{ {\rm rep},\mathbb{C} }\xrightarrow{\text{real slice} }B_{\rm rep}^{\rm Kerr}$$

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

## VII.3 Statistics and exclusion are inputs, unchanged [T]

Spin–statistics, anticommutation and the Pauli exclusion principle enter this theory **exactly as they enter ordinary quantum field theory**, and nothing in v15 modifies, derives or threatens them.

*A note on what is not claimed.* Earlier drafts invoked the Finkelstein–Rubinstein argument — that exchanging two identical particles is locally homotopic to rotating one by $2\pi$ — to say statistics proceed as usual. **That invocation is withdrawn** (§X.1). FR is a statement about loops in the configuration space of extended topological solitons, and the exchange/rotation identification depends on that configuration space's topology; it is not a theorem that a spacetime spin bundle by itself delivers fermionic statistics. Unless and until actual soliton configuration spaces are constructed here, the safe and sufficient statement is the one above, resting on §VII.2.

## VII.4 Twin parity [O]

The frame bundle of $\mathbb{RP}^3 = SO(3)$ is $SO(3)\times SO(3)$, with $\pi_1 = \mathbb{Z}_2\times\mathbb{Z}_2$: **two independent** generators, a frame rotation (giving spin) and a trip around the twin loop (giving a parity $\tau = \pm1$). It is tempting to read the two $\mathbb{Z}_2$ factors as two independent particle quantum numbers. **That reading is not established, and the section is tagged open for that reason.** $\mathbb{RP}^3$ does have two spin structures, since $H^1(\mathbb{RP}^3;\mathbb{Z}_2) = \mathbb{Z}_2$; but the relation between the base loop, the frame rotation, the *chosen* spin structure, and a genuinely independent label on a field is subtler than reading off two factors of $\pi_1$. Settling it is an associated-bundle representation problem, not a homotopy count, and it has not been worked through here **[O]**.

---

# PART VIII — STATIC REGRESSION AND TESTS

## VIII.1 The static great-circle realization [S/D]

*An earlier draft claimed to **derive** this from topology. That claim is withdrawn — three steps of it were wrong (§X.1). What follows is an exact construction of the realization, with its one assumption marked as an assumption.*

The intended specialization is

$$\mathcal{M}_{\rm static}\sim\mathbb{R}_t\times S^4,\qquad B_{\rm rep}^{\rm static}\sim\mathbb{R}_t\times S^3,\qquad B_{\rm grav}^{\rm static}\sim\mathbb{R}_t\times\mathbb{RP}^3$$

with dimensions $1+4 = 5$, $1+3 = 4$, $1+3 = 4$ **[V]**.

### The assumption [S]

> **In the static limit, the meridian structure is the antipodal great-circle pencil.** It is a *pencil*, not a foliation: distinct meridians meet at the two poles, which form a common singular set. Nothing in Law 0 or in the topology of $S^4$ forces this, and it is adopted as a structural choice.

### The construction, and the quotient [D/V]

Embed $S^4\subset\mathbb{R}^5$ and fix an axis $p\in S^4$, with poles $\pm p$. For each unit vector $n$ in the 3-sphere of $p^\perp$, form the **2-plane**

$$P_n = \operatorname{span}(p,n),\qquad C_n = P_n\cap S^4$$

Then $C_n$ is a great circle through both poles — verified: every point $\cos t\,p+\sin t\,n$ has unit norm, and $t = 0,\pi$ give $\pm p$ **[V]**. And since a plane is unchanged by negating a spanning vector,

$$P_n = P_{-n}\quad\Longrightarrow\quad C_n = C_{-n}$$

verified pointwise **[V]**. So the meridians are in bijection with $S^3$ modulo the antipodal map:

$$\boxed{\ \text{space of meridians} = S^3/\{\pm1\} = \mathbb{RP}^3\ }$$

**exactly**, with no index theory, no foliation language, and no claim about closed orbits. And the bisection follows immediately: $C_n$ meets the equatorial $S^3$ at $n$ and at $-n$, the two points of §II.3.

### What is derived, and what is not

$$\text{antipodal great-circle pencil}\ \Longrightarrow\ \mathbb{RP}^3\qquad\textbf{[D]}$$
$$\text{Law 0} + \text{topology}\ \Longrightarrow\ \text{antipodal great-circle pencil}\qquad\textbf{[O]}$$

The first is exact. The second is **not available**, and the attempt to supply it is retired (§X.1).

**The remaining regression, in order [O]:** derive the quotient metric and its Green's function on $\mathbb{RP}^3$; recover the geodesic and orbit equations; **then** reassert the numbers of §IV.8.

## VIII.2 The golf ball [D]

*The question was: does a small body get a Hopf structure of its own, or does a large nearby body dominate?*

**In this version the question has a clean answer, and a different one from before.** The fiber is supplied by spin geometry, and every shell about every worldline carries the same class:

$$c_1 = 1\quad\text{(one global orientation convention; }-1\text{ under the opposite)}$$

independent of the body's mass, its neighbours, or any parameter — and **not** a sign chosen afresh on each shell. **A golf ball's shells carry exactly what Earth's shells carry.** There is no competition, no crossover radius, no dependence on what else is nearby — because the structure is a fact about the rotation group acting on a shell, not a tally of matter.

> Earlier versions answered this with a mass-proportional winding number, $M/m_{\rm unit}$ — $2.7\times10^{25}$ for the ball and $3.6\times10^{51}$ for Earth — together with a "quantization fork" over the value of $m_{\rm unit}$ and a crossover at $0.56\,\mu$m where Earth's flux overtook the ball's. **All of that is retired** (§X.1). It presupposed a posited circle whose class matter was free to set; here the circle is derived and its class is fixed.

**What remains testable is nothing, here.** The class is the same everywhere, so it distinguishes no two situations, and Maxwell's pullback is $U(1)_H$-invariant in any case.

## VIII.3 The Machian direction [T/D/V]

Vacuum general relativity already has the symmetry $(g,M)\to(\lambda^2g,\lambda M)$: every Schwarzschild exterior *is* a rescaled copy of every other, with mass the scale. So "isomorphic shells up to scale" is true and yields nothing new — the scale it fixes is mass, not size, and compactness $r_s/R$ ($1.4\times10^{-9}$ for Earth, $3.2\times10^{-27}$ for a golf ball) is untouched.

Rescaling $r_s$ with $GM$ fixed is **inconsistent**, since $r_s = 2GM/c^2$ is one number whenever the exterior has a single source. Separating the horizon from the far-field coupling would require the near field to be sourced by something the far field does not see.

> Earlier versions offered one: the flux energy $|F_\oplus+F_g|^2$ has a cross term present only when Earth is, giving the ball a near field that differs alone and in company, bounded by Mercury at $3\times10^{-4}$. **That is retired with the flux sector** (§X.1). **So the Machian proposal now has no realizable form in the theory at all** — which is the honest position, and worth stating rather than leaving a retired mechanism standing in for one.

**A local Mach relation fails [V]:** reading $GM/c^2\ell = \pi/2$ with $\ell$ a sphere of influence gives $5\times10^{11}G$ for Earth and $3\times10^{22}G$ for the golf ball. The Mach relation closes a *universe*.

**Emergent $G$ [O]:** an open coupling problem, not a theorem. ADM and Komar masses carry $G$ in the conventional normalization, but matter Lagrangians contain inertial and rest-mass parameters that require no solution of Einstein's equations. The real difficulty is to define an operationally appropriate mass variable and show that a candidate emergent coupling reproduces **both** the inertial and the gravitational roles. *An earlier categorical claim — that $G$ is emergent iff mass has a $G$-free definition, and general relativity has none — is too strong and is retired* (§X.1).

## VIII.4 The required constructions [O]

1. Construct an explicit $E$ whose shell restrictions are the stated $SL(2,\mathbb{C})$ lifts, over $\mathcal{M}$ minus the secondary meridians (§II.1), with a smooth five-dimensional quotient away from controlled singular loci.
2. Show the complex bundle's reduction to $U(1)\to SU(2)\to S^2$ on the Lorentzian slice, covariantly.
3. Define the complex normal bundle and shell lift along a general non-null complex worldline.
4. Carry the shell lift consistently through Schwarzschild $\to$ Kerr.
5. **Derive** $L_H = \Omega L_H^{\rm ref}$ rather than impose it.
6. Determine whether the two open connection components have any role at all, from the action rather than by assignment.
7. Derive the meridian structure from canonical data.
8. Recover $S^4\to\mathbb{RP}^3$ and the barren twin.
9. Re-derive the $v^2$ family in the recovered static sector.
10. Compute what stress-energy an observer infers by applying Einstein's equation on $B_{\rm rep}$ instead of $B_{\rm grav}$ — **the dark-sector target**, and the calculation that would make the architecture phenomenological.
11. Verify the twin stays optically barren.
12. Keep the spin-statistics firewall: do not identify the geometric spin lift with Grassmann parity.

---

# PART IX — THE ACTION TARGET [O]

A successful action should make both information reductions automatic:

$$S = S_{\rm EH}[B_{\rm grav},g_G] + S_{\rm matter}[B_{\rm rep},\psi,A] + S_{\rm can}[E,\hat g,\mathcal{A}_H,U_{\rm mer}]$$

Variation with respect to $g_G$ should produce the meridian-reduced source; constraints on the canonical metric should produce the fiber-length locking; and if the canonical connection's two open components are to acquire a role, it must come from there rather than from an assignment made by hand. **Until such an action exists, the split is architectural rather than final.**

---

# PART X — RETIRED AND OPEN

## X.1 Retired, with reasons

| item | reason |
|:--|:--|
| the middle space as the axiom | it is **derived** from the canonical space (§II.2) |
| "representational middle space" / "quotiented middle space" | both are **bases**; the middle space is the single derived five-dimensional layer |
| a real $S^2$ shell used *before* complexification | at the analytic level it is the affine quadric; the 2-sphere is its real form (§I.2) |
| the projective null-cone quadric as the default source shell | that object belongs to null-direction geometry, not fixed-radius shells (§I.7) |
| $TS^4$ as the arena (version 14) | replaced; it made the fiber contractible and cost the connection structure its home |
| an external fundamental $\mathbb{R}_t$ | time belongs to the Lorentzian real structure |
| the Hopf fiber *as* Kerr rotation | rotation is complex worldline displacement; the fiber is the shell's spin lift (§VI.2) |
| an extra $U(1)$ with no spin-geometric origin | the circle is now the compact real form of $\mathbb{C}^\times\subset SL(2,\mathbb{C})$ (§I.3) |
| geometric Weyl spinor $\Rightarrow$ quantum Grassmann fermion | blocked by type (§VII.2) |
| **the entire second-order flux sector** | **inconsistent with this version's own foundation.** A derived fiber has a *fixed* Chern class, the unit Hopf class; the flux sector required $c_1 = M_-/m_{\rm unit}$, mass-dependent with a free parameter. Both cannot hold, and it is the posited one that goes |
| the flux quantum $m_{\rm unit}$ | no role: $c_1$ is not a ratio of masses |
| the quantization fork ($m_p$ versus $\sim10^{14}M_\odot$) | there is nothing left to quantize |
| mass-proportional winding counts ($2.7\times10^{25}$ for a golf ball) | every shell carries the unit Hopf class whatever the body's mass (§VIII.2) |
| the charge $P = g_2M/m_{\rm unit}$, its $P^2/r^2$ term, and $M^2\geq Q^2+P^2$ | no such charge exists (§IV.6) |
| the Mercury bound $g_2/m_{\rm unit}<0.024$ | it bounded a parameter that is gone |
| the Machian cross term $2F_\oplus\!\cdot\!F_g$ | built from the flux energy; the Machian proposal now has **no** realizable form (§VIII.3) |
| the *integrated flux law* $c_1 = M_-/m_{\rm unit}$ | it makes the Chern class mass-dependent, and spin geometry has fixed it at the unit Hopf class. *(Note the narrow scope: a connection may still vary with $c_1$ fixed — $\int d\alpha = 0$. What is retired is the flux law, not connection dynamics as such.)* |
| the assignment $T_-\to$ the two connection components | made because there happened to be two of them, which is not a reason (§III.3) |
| the claim that the static meridian structure was **derived** from topology | three errors: Poincaré–Hopf gives only the index *sum*, not two index-$+1$ zeros; "foliation" is the wrong word, since distinct meridians meet at the poles (it is a singular **pencil**); and closed orbits need not pass through zeros at all — integral curves do not continue through them (§VIII.1) |
| "on a static geometry there is no redshift" | **false.** Schwarzschild is static and redshifts: $z = 0.21$ from $6M$ to $100M$ **[V]**. Staticity forbids *cosmological* redshift; the true statement is the narrower twin one (§IV.11) |
| the permeability $\mu(\rho)$ | orphaned: the old Law II equation it belonged to is not part of this version |
| "$G$ is emergent iff mass has a $G$-free definition, and GR has none" | too categorical; matter Lagrangians carry rest-mass parameters independently. An open coupling problem (§VIII.3) |
| calling Maxwell's field a **zero mode** on the fiber | implies a Kaluza–Klein expansion this version does not perform; the field lives downstairs and its pullback is $U(1)_H$-invariant (Law IV) |
| calling the fixed Hopf class an **Aharonov–Bohm phase** | a class gives a nontrivial bundle and a connection gives holonomy, but an observable phase needs a coupled field — and nothing couples here (§III.1) |
| "degree-of-freedom split" as a label for $6 = 3+1+2$ | it is a block count of metric *components*; physical degrees of freedom require removing gauge and diffeomorphism freedom (§III.3) |
| "two geometrical degrees of freedom" for the connection | same error one level down: two *local components*, with $A\mapsto A+d\lambda$ still to be quotiented (§III.3) |
| "nothing is added; a source is moved" | the complex shift supplies the Kerr complex structure, but the full metric also needs the Kerr–Schild null-congruence construction and a reality prescription, and generalized Newman–Janis is ambiguous away from special cases (§VI.1) |
| $q^*g_G$ as the metric felt on the representational base | $q$ is a submersion, so $q^*g_G$ is **degenerate** along the meridian. The right object is $r^*g_G$ with $r = q\circ\iota$ (§V.1) |
| reading the two $\pi_1$ factors as two independent quantum numbers | an associated-bundle representation problem, not a homotopy count; §VII.4 is now tagged open |
| the biconditional $g_G\Leftrightarrow L_H$ | a single scalar cannot in general reconstruct a four-dimensional metric; only the one-way map $g_G\mapsto L_H$ is defensible (§III.2) |
| describing the **static limit** as derived | only its *quotient* is derived, and only given the antipodal great-circle pencil, which remains an assumption (§VIII.1) |
| calling $U_{\rm mer}$ a foliation without qualification | in the static case distinct meridians meet at the poles, so it is a **pencil**, not a foliation of all of $S^4$ (Law II) |
| "$S^4\setminus\text{circle}\simeq S^2$" | true for the unknotted embedding but stronger than needed; 1-knots in $S^4$ exist. Alexander duality gives $H^2 = \mathbb{Z}$ regardless, which is all the argument uses (§II.1) |
| "$c_1 = \pm1$ on every shell" | reads as a per-shell binary choice. One *global* orientation convention fixes the unit Hopf class everywhere (Structure III) |
| $v^2_{\rm eq} = 4GM/\pi\ell$ | 15% low; the converged value is $1.497\,GM/\ell$ (§IV.8) |
| $N\Omega = 1$ as an **exact** condition | it gives Majumdar–Papapetrou and hence extremal charge for every body (§III.2) |
| time as emergent from a fiber's latitude (version 12) | a type error: a complex structure has $J^2 = -1$, no real eigenvectors, and *pairs* directions where time must *select* one |

## X.2 Open

1. **The global $E$** (§II.1b). Part I's shell lives on the *normal space*, a space of vectors; passing to nearby points of the middle space uses the exponential map, which is local, with curvature, cut loci and caustics obstructing it globally. Whether **one** six-dimensional $E$ restricts to the unit Hopf bundle around **every** worldline at once is unproved. **The version's central construction problem** — and a sharper one than what it replaces, since the local spin geometry is settled and only the gluing is not. (The cohomological obstruction of §II.1a is separate and is handled by the meridian removal.)
2. **Deriving the fiber-length locking** from an action (§III.2). Until then $g_G\mapsto L_H$ remains an **imposed encoding constraint**, not a derived consequence of any canonical dynamics — and the arrow cannot be reversed. Note also that the reversal a future action would supply is $\hat g\Rightarrow g_G$, from the *full* canonical metric, not $L_H\Rightarrow g_G$.
3. **The two open connection components** (§III.3). Deliberately unassigned. If the theory later says what they do, that will be a result; asserting it now would not be.
4. **What selects the meridian structure** (Law II) — in the static case *and* the general one. §VIII.1 derives the quotient $S^3/\pm = \mathbb{RP}^3$ **given** the antipodal great-circle pencil, but nothing derives the pencil: it is an assumption there, and away from maximal symmetry nothing selects the leaves at all. **Why the leaves are closed** remains the sharpest sub-question, since closure is what forces the bisection and hence the seed (§II.3).
5. **Time:** an input, belonging to the Lorentzian real structure; its uniqueness is not derived, and three routes to deriving it have failed.
6. **The remainder of the static regression** (§VIII.1): the quotient metric, its Green's function, and the orbit equations. The *geometric* link — great circles with quotient $\mathbb{RP}^3$ — is now discharged.
7. **The dark-sector calculation** (§VIII.4, item 10) — what stress-energy an observer infers by applying Einstein's equation on $B_{\rm rep}$ instead of $B_{\rm grav}$. **The theory's sharpest quantitative target.** It is not a prediction until it is computed, and computing it is what would turn this architecture into phenomenology.
8. **The meridian scale $\kappa$** (§IV.5), which the eventual Law II dynamics must fix.
9. **Twin parity assignments** (§VII.4).
10. **Emergent $G$** (§VIII.3): an open coupling problem — define an operationally appropriate mass variable and show a candidate coupling fills both the inertial and gravitational roles.
11. **Inherited:** the AdS uplift; the two arenas; the literature review.

**A research branch worth opening, not folding in [T/O].** Kim, *Phys. Rev. Lett.* **136**, 231401 (9 June 2026), "Newman–Janis Algorithm from Taub–Newman–Unti–Tamburino Instantons," derives the Kerr metric as a **nonlinear superposition of self-dual and anti-self-dual Taub–NUT instantons** and interprets this as a physical derivation of the Newman–Janis relation. *(This post-dates the present author's reliable knowledge; the citation was supplied and verified by a referee.)*

It bears directly on the motivation for looking at self-dual structure in the first place, and it addresses exactly the gap flagged in §VI.1 — that the complex shift alone is not a complete derivation. **It does not validate the canonical construction here**, and this version is not restructured around it. It is the natural next branch.

**The constant count.** The theory's explicit constants are now just $G$ and $\Lambda = 1/\ell^2$, plus whatever the eventual Law II dynamics introduces. **$m_{\rm unit}$ and $g_2$ went with the flux sector**, and the permeability function $\mu(\rho)$ went with the old Law II, whose equation this version no longer contains — it was an orphan in the previous draft and is removed (§X.1).

---

## X.3 Chiral composition: two bridges and two obstructions [T/V/O]

*Kim's result (§X.2) suggests a bridge to the chiral sector. Two parts of it are established, two are blocked, and one is a stated theorem target. None is folded into the architecture.*

### Bridge 1 — the shell group is the diagonal of the chiral pair [T]

Complexified four-dimensional spin geometry factorizes, and the stabilizer of a non-null direction $u$ sits **diagonally** inside it:

$$Spin(4,\mathbb{C})\cong SL(2,\mathbb{C})_L\times SL(2,\mathbb{C})_R\ \supset\ \Delta SL(2,\mathbb{C}) = SL(2,\mathbb{C})_{\rm shell},\qquad g\mapsto(g,g)$$

whose compact form is the familiar $Spin(3)\cong SU(2)\hookrightarrow Spin(4)\cong SU(2)_L\times SU(2)_R$. **This is standard group theory, and it places the shell group of Part I rather than positing it.** The whole chain reads

$$Spin(4,\mathbb{C})\ \xrightarrow{\ \text{stabilize }u\ }\ SL(2,\mathbb{C})_{\rm diag}\ \xrightarrow{\ /\,\mathbb{C}^\times\ }\ Q^2_{\rm aff}\ \xrightarrow{\ \text{real form}\ }\ S^2$$

with dimensions $12\to6\to4\to2$ **[V]**. Given $u$, the rest of §I.2–§I.4 is much less arbitrary than it looked: **one shell spin group is the diagonal residue of two chiral spin groups.**

### Bridge 2 — self-dual Taub–NUT carries the same shell type [T]

In Gibbons–Hawking form $ds^2 = V^{-1}(d\tau+\omega)^2+V\,d\mathbf{x}^2$ with $\nabla\times\omega = \nabla V$, the potential $\omega$ is a Dirac monopole and each constant-radius three-surface is a circle bundle over the angular $S^2$ — for unit charge, the Hopf fibration $S^1\to S^3\to S^2$. **So the elementary chiral constituents of Kim's construction carry the same shell *type* as the canonical shells here.** More than a coincidence of names.

### Obstruction 1 — but not the same shell *geometry*, in two independent ways [V]

**(a) The scaling is inverse.** Taub–NUT has fiber length $\propto V^{-1/2}$ against base scale $\propto V^{+1/2}$, so approaching the source the **fiber shortens**:

| $r/m$ | $V$ | fiber | base |
|--:|--:|--:|--:|
| 10 | 1.200 | 0.913 | 1.095 |
| 1 | 3.000 | 0.577 | 1.732 |
| 0.3 | 7.667 | 0.361 | 2.769 |

Law I says the opposite: $L_H = \Omega L_H^{\rm ref}$ with base scale also $\propto\Omega$, and $\delta L_H/L_H = -\Phi$ with $\Phi<0$ in a well, so **the canonical fiber lengthens inward**.

**(b) The shell is squashed.** A round $S^3$ in Hopf form has equal fiber and base coefficients; Taub–NUT's ratio is $1/V^2r^2 = (2m+r)^{-2}$, equal to one only at an isolated radius. Generically a **Berger sphere**, not a round one **[V]**.

> **The shells agree as bundles and disagree as geometries.** So "derive the fiber-length locking inside the chiral Taub–NUT sector" is not available: done naively it gives the wrong sign *and* the wrong metric. The sharp question is instead **why the same Hopf topology should carry a reciprocal metric law** — and no answer should be adopted merely because it repairs the sign.

### Obstruction 2 — this branch cannot derive time [D]

The timelike direction $u$ is presupposed **three times over**: by $N_\gamma = \{\xi:g_\mathbb{C}(\xi,\dot\gamma) = 0\}$, which needs $\dot\gamma$; by Kim's stationary composition, which uses $u^\mu$; and by Bridge 1 itself, since *which* diagonal depends on which direction is stabilized.

> **A composition law defined on this shell architecture cannot derive $u$, because $u$ already defines the architecture on which it acts.** This closes the chiral route to time in the present version. Rebuilding $E$ *prior* to choosing a real form or a non-null direction, and showing a diagonal reduction emerges dynamically, would be a different and more foundational version — not a result available here.

### The theorem target — an equivariance test, stated without prejudging [O]

Kim's composition contains a bilinear $\ell^{\dot\alpha\alpha}\propto\tilde o_+^{\dot\alpha}o_-^{\alpha}$. Let $U(1)_H\subset SL(2,\mathbb{C})_{\rm diag}$ act on the two principal-spinor lines with weights $q_\pm$. Then the composed null field descends through the Hopf quotient exactly when

$$\boxed{\ q_+ + q_- = 0\ }$$

verified as the condition: with $h_\theta = \operatorname{diag}(e^{i\theta},e^{-i\theta})$ acting diagonally, opposite-weight lines give an invariant bilinear and same-weight lines do not **[V]**.

*An earlier formulation of this test — "identify $U(1)_H$ with the anti-diagonal of $U(1)_L\times U(1)_R$" — is retired* **[R]**. It conflated two different objects: the **diagonal $SL(2,\mathbb{C})$**, which is a spacetime spin-group embedding, with an **anti-diagonal $\mathbb{C}^\times$**, which is the projective rescaling redundancy of a bilinear's two representatives. $U(1)_H$ lies in the diagonal, and the cancellation must come from *representation content*, not from relocating the subgroup by fiat. Stated as a weight condition, it is something to prove rather than to assume.

### What the branch is actually for [S]

Not time, and not the fiber-length locking. The natural job is

$$\star:\ \mathcal{D}_{\rm SD}\times\mathcal{D}_{\rm ASD}\ \longrightarrow\ \mathcal{D}_{\rm real}$$

— **how non-chiral gravitational geometry is assembled from chiral constituents** — and whether $\star$ lifts to $E$ and commutes with both reductions:

$$\pi_H(D_+\star_E D_-) \overset{?}{=} \pi_H(D_+)\star_\mathcal{M}\pi_H(D_-),\qquad q(D_+\star_\mathcal{M}D_-)\overset{?}{=} q(D_+)\star_G q(D_-)$$

If that diagram commutes, chiral composition would be intrinsic enough to survive **both** of this theory's information-losing maps. That is a better prize than another account of the fiber.

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
| **why not bolted on** | not a coincidence of group names: right multiplication by $\operatorname{diag}(e^{i\theta},e^{-i\theta})$ sends the spinor column to $e^{i\theta}\psi$, so the shell's $U(1)$ **is** the spinor phase, acting as it already acts (§I.6) |
| **why isotropic** | shell and lift are homogeneous; the fiber is a stabilizer, not a chosen longitude |
| **the centrepiece** | **spin geometry fixes the fiber's topology; gravity fixes only its metric length** |
| **Law I** | Einstein on $B_{\rm grav}$, source $T^{(g)}_b = \sum_{r^{-1}(b)}((dr)^{-1})^*T$ with $r = q\circ\iota$; also fixes $L_H = \Omega L_H^{\rm ref}$ |
| **the metric light feels** | $g^{(G)}_{\rm rep} = r^*g_G$, **not** $q^*g_G$ — the latter is degenerate along the meridian |
| **the arrow** | one-way: $g_G\mapsto L_H = \mathcal{F}[g_G]$. A scalar cannot reconstruct a metric, so no biconditional is claimed; and a future emergence result would be $\hat g\Rightarrow g_G$, not $L_H\Rightarrow g_G$ |
| **$G$ identity** | $GM_c/c^2\ell = \pi/2$; equivalently $r_s(M_c) = \pi\ell$, the antipodal distance |
| **metric decomposition** | $6 = 3+1+2$ on the real shell ✓ — a block count of *components*, not propagating degrees of freedom. $3+1$ from Law I; the last **2 left open** |
| **black holes** | ordinary Schwarzschild, or Reissner–Nordström with the ordinary $Q$. No second charge |
| **$v^2$ plateau** | $1.497\,GM/\ell$, packing-independent; at $f = 1$, $r_s = \pi\ell$ and no exterior |
| **Keplerian limit** | corrections $4\times10^{-15}$ at 10 kpc; jellium crossover at 1.2 Mpc for a galaxy |
| **Kerr** | complex worldline displacement, $a = J/M$; ring at $x^2+y^2 = a^2$; shells follow the displaced center |
| **rotation vs fiber** | rotation is **not** winding around the fiber; four jobs, four structures |
| **time** | an input, from the Lorentzian real structure |
| **Grassmann parity** | not derived, and blocked by type |
| **Chern class** | the **unit Hopf class** on every oriented shell, fixed by spin geometry. One global orientation convention, not a per-shell sign; not mass-dependent, no $m_{\rm unit}$, no fork |
| **golf ball** | its shells carry exactly what Earth's do. No competition, no crossover, no winding counts |
| **free constants** | $G$ and $\Lambda$, plus whatever Law II's dynamics brings. $m_{\rm unit}$, $g_2$ and $\mu(\rho)$ all retired |
| **the static limit** | pencil **[S]** $+$ quotient $S^3/\pm = \mathbb{RP}^3$ **[D]**. The limit as a whole is *not* derived — only its quotient, and only given the pencil |
| **Structure III** | a connection structure, **not a law**: no field equation, the unit Hopf class fixed, two local cross-components with $A\mapsto A+d\lambda$ unquotiented |
| **the obstruction** | $H^2(S^4) = 0$: Law 0 needs the secondary meridians removed, as every earlier version did |
| **chiral bridge** | $SL(2,\mathbb{C})_{\rm shell} = \Delta SL(2,\mathbb{C})\subset SL(2,\mathbb{C})_L\times SL(2,\mathbb{C})_R$; SD Taub–NUT shells are Hopf. But inverse scaling *and* Berger squashing block the metric, and $u$ is presupposed, so no time (§X.3) |
