# Projective Gravity — Version 13

### The Twistor Fiber as Fundamental

> **What this document is.** A complete, self-contained statement of the theory: arena, laws, identities, the spinor sector, the electromagnetic sector, and the construction of visible space. It assumes no earlier document. Every term is defined in Part 0; every law is stated with its equation; every result imported from an earlier version is restated in full rather than cited.
>
> **What is new relative to version 12.** The **fiber is replaced.** Versions 6 through 12 hung a Hopf circle over the cover and made gravity's fiber reading a statement about that circle's length. The circle was a gesture — nothing required it. Version 13 replaces it with the fiber that the Newman–Janis construction actually demands: the **twistor fiber**, the 2-sphere of complex structures on the tangent space at each point of the cover. The canonical total space becomes $\mathbb{R}_t\times\mathbb{CP}^3$.
>
> **What the replacement buys.** **(1) Law III stops being postulated.** A 2-sphere has $SO(3)$, not $U(1)$; a $U(1)$ appears once an axis is chosen — a *section* — and sections exist over the cover minus the secondary meridians, which is the removal Law III already required. **The Hopf circle is no longer an input: it is the twistor fiber's rotation subgroup.** **(2) Kerr becomes a statement about the canonical total space itself.** A real source's twistor line *is* a fiber, standing vertical; a rotating source's line is **tilted**, and $a = J/M$ measures the tilt. **(3) Law I transfers intact** — a round 2-sphere is fixed by one number, its radius, exactly as a circle is fixed by its length.
>
> **What it costs, stated up front.** Twistor space is *conformally invariant*, so the fiber's radius is not determined by the construction: the locking $\lambda = \Omega\lambda^{\rm ref}$ is posited, exactly as the Hopf version was. And the partition **no longer closes**: four connection components — the tilt field, where Kerr's parameter lives — are unassigned, where version 11's count was exactly filled.
>
> **Time is still an input**, a factor $\mathbb{R}_t$, as in versions 6 through 12. Version 12's attempt to make it emergent is retracted, for a reason of type rather than of detail (§IX.6).
>
> **Carried unchanged.** The Maxwell 1-form and the empty twin; the seed and the meridian quotient; every law, theorem and identity of the gravity base; the Machian form of Law II.

> **Tags.** **[V]** verified by computation · **[T]** cited theorem · **[D]** derived here · **[S]** sketch · **[O]** open · **[R]** retired, with reason.

---

# PART 0 — VOCABULARY AND CONVENTIONS

## 0.1 The spaces

| term | definition | dim | role |
|:--|:--|:--:|:--|
| **canonical total space** | $\mathbb{R}_t\times\mathbb{CP}^3$: the twistor space of the cover, times time. Its fiber over $x\in S^4$ is the 2-sphere of complex structures on $T_xS^4$ compatible with metric and orientation | 7 | where the full structure lives |
| **twistor fiber** | that 2-sphere, $SO(4)/U(2) = S^2$. **Tangent-space data, attached pointwise — not a lifted shell** | 2 | Laws I and III both read it |
| **middle space** | $\mathbb{R}_t\times S^4$: the canonical total space with the twistor fibers quotiented away. Where matter and light live | 5 | matter, light |
| **cover** | $S^4$: the middle space with its time factor set aside | 4 | the spatial cover |
| **gravity base** | $\mathbb{R}_t\times\mathbb{RP}^3$: the space of meridians, times time. Where gravity lives | 4 | Law I |
| **section** | a choice of complex structure at each point — a section of $\mathbb{CP}^3\to S^4$. Exists over the cover minus the secondary meridians, not over all of it. **Choosing one is what produces Law III's $U(1)$** | — | §III.1 |
| **fermionic base** | the canonical total space modulo the involution of Part VI | 7 | where a Dirac spinor is one local object |

The unqualified phrase "total space" is retired in favor of *canonical total space*. The fibration tower is

$$\mathbb{R}_t\times\mathbb{CP}^3\ (7)\ \xrightarrow{\ /\,\text{twistor fiber}\ }\ \mathbb{R}_t\times S^4\ (5)\ \xrightarrow{\ /\,\text{meridians}\ }\ \mathbb{R}_t\times\mathbb{RP}^3\ (4)$$

with **time a factor throughout** — an input, not a derivation. The second arrow is the meridian quotient, $S^4\ (4)\to\mathbb{RP}^3\ (3)$, and it is where the seed lives: matter sits on a ray, gravity on the line.

The seven directions:

| direction | count | where | fate |
|:--|:--:|:--|:--|
| gravity base $\mathbb{RP}^3$ | 3 | the bottom of the tower | kept |
| meridian $u$ | 1 | in $S^4$ | **quotiented** — the seed |
| twistor fiber | 2 | over each point of $S^4$ | **quotiented** — why gravity cannot see Law III |
| time $t$ | 1 | an external factor | kept |

## 0.2 Points and places

| term | meaning |
|:--|:--|
| **primary** | matter sitting at a pole. Not a mass threshold: the role is positional, and the poles are set by the matter's own principal axis (§II.4) |
| **poles** | $\pm\hat d$, the two points where the fibration degenerates, located at the matter distribution's principal axis. **Not** twins of each other; each is its own twin. Choosing the polar axis is the same act as choosing the twin map |
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
| **Law III's circles** | orbits of the $U(1)$ that rotates the **twistor fiber** about a section (§III.1): one circle inside each fiber | **no** — two points of one such circle lie over the *same* point of the cover |

The twin comes from the meridians and from nothing else.

## 0.4 Fields and quantities

| term | meaning |
|:--|:--|
| $T_\pm$ | $T_\pm(\hat n) = T(\hat n)\pm T(-\hat n)$: the even and odd parts of matter under the twin map |
| **even sector** | $T_+$; what gravity reads |
| **odd sector** | $T_-$; what the second-order connection reads |
| **jellium** | the uniform part of the base density. Produced either by matter at a pole (which lies on every meridian) or by matter spread evenly over a latitude. Requires no primary |
| **conformal factor** $\phi$ | defined by $g_3 = \phi^4g_{S^3}$; $\Omega\equiv\phi^2$ |
| **fiber length** $L_E$ | the local length scale of the Hopf circle, locked to gravity by $L_E = \Omega L^{\rm ref}$ |
| **permeability** $\mu(\rho)$ | how matter deflects the meridians in Law II without sourcing them |
| **Hopf charge** $n$ | a field's momentum around the Hopf circle; an integer |
| **flux quantum** $m_{\rm unit}$ | the mass carrying one unit of second-order flux |
| **Chern number** $N$ | $M_-/m_{\rm unit}$: the winding of $E$'s fiber around a secondary's meridian |
| **zero mode** | a field component with $n = 0$; the only kind a base detector registers |
| **twin parity** $\tau$ | $\pm1$ in $\psi(-\hat n) = \tau\psi(\hat n)$, for fields that descend to the gravity base |
| **odd chirality** | the ordinary chirality of a Weyl spinor: the eigenvalue of the Clifford volume element $\gamma_5$ |
| **even chirality** | the self-duality of a 2-form field strength. In four Lorentzian dimensions it is **complex**: $\mathcal{F}^\pm = \tfrac12(\mathcal{F}\mp i\star\mathcal{F})$ |
| **the seed** | matter sources a gravitational well at both $\pm\hat n$, while light reaches only one of them |


## 0.5 Conventions

$G = c = 1$ unless restored. $\ell$ is the gravity-base radius; $\chi\in[0,\pi]$ the polar angle on $S^4$; $\hat n\in S^3$ a point of a latitude; $\theta$ the Hopf fiber angle. $\alpha$ is the second-order connection with curvature $F = d\alpha$; $B$ the electromagnetic 2-form with strength $H = dB$; $\star$ the Hodge star of the canonical total space. $\Phi$ is the Newtonian potential.

---

# PART I — THE ARENA AND THE THREE SPACES

## I.1 The cover, and why a 4-sphere [T/D]

The cover is $\mathbb{R}_t\times S^4$, with the primary at one pole of the fibration and its antipode at the other. Matter and light live here; gravity does not.

**The primary is compulsory.** Poincaré–Hopf: any vector field on $S^4$ has zeros of total index $\chi(S^4) = 2$, and a gradient flow with one source and one sink has index $(+1)+(+1) = 2$ — the minimum. So the fibration *must* degenerate at exactly two points, and the central mass sits at one of them. On $S^1\times S^3$ (Euler characteristic zero) a center is optional; on $S^4$ it is forced.

## I.2 The twistor fiber, and why it is the right one [T/D]

Attached canonically to the cover, with nothing chosen, is its **twistor space**

$$\mathbb{CP}^3\ \longrightarrow\ S^4 = \mathbb{HP}^1,\qquad \text{fiber } \mathbb{CP}^1 = S^2$$

Over $x$ the fiber is the set of complex structures on $T_xS^4$ compatible with the metric and orientation — $SO(4)/U(2) = S^2$, equivalently the sphere of unit self-dual 2-forms. Concretely: $\mathbb{C}^4$ is the same real vector space as $\mathbb{H}^2$; $S^4 = \mathbb{HP}^1$ is the quaternionic lines through the origin, $\mathbb{CP}^3$ the complex ones, and each quaternionic line contains a $\mathbb{CP}^1$ of complex lines.

**Why this fiber and not another.** The Newman–Janis construction *requires* it: complexifying the cover turns a real point into a **vertical** line of $\mathbb{CP}^3$ and a complex point into a **tilted** one, which is what makes rotation a geometric statement (§IX.4). Nothing required the Hopf circle of earlier versions; it was a gesture at a structure not yet identified. **This is that structure.**

> **What the fiber is not.** It is **tangent-space data, attached pointwise** — one sphere of complex structures per point. It is *not* a lifted shell. Version 11's "each shell is the base of a Hopf 3-sphere" described a 2-sphere *of points in space*; this is a 2-sphere *of complex structures at a point*. The two are different in kind, and conflating them is the error this version exists to correct.

**What survives of the shell story [D].** Shells remain the surfaces Law III's flux is *integrated through*, unchanged. And "a Hopf 3-sphere over a shell" survives as the **restriction** of the $U(1)$ bundle of §III.1 to a shell, whose total space is the lens space $L(|c|,1)$ — a consequence of the construction, not a separate one. (In four-dimensional space the set at fixed distance from a point is an $S^3$; shells are 2-spheres *inside* a latitude 3-sphere, as always.)

## I.3 The quotient, the base, and the seed [D]

The gravity base is the space of meridians, $\mathbb{RP}^3$. Each of its points is one great circle through both poles, crossing the equator at $\pm\hat n$. Gravity is defined on $\mathbb{R}_t\times\mathbb{RP}^3$ and reads the fiber average — the integral of the cover's stress-energy along the meridian — which includes both twins by construction.

> **The seed.** Matter at $(\chi_0,\hat n)$ sources the gravity base at $[\hat n]$, whose lift to the cover has wells at both $\hat n$ and $-\hat n$. **Nothing is at $-\hat n$.** Blindness to which ray, not crossing between them.

**This is derived, not postulated:** a great circle through the poles crosses the equator twice. The projective postulate of the earliest versions is a theorem of the arena. 

## I.4 The primary is the jellium [D]

Both poles lie on **every** meridian, so $M_c$ contributes equally to every fiber average: seen from the gravity base it is uniform. The uniform background density of the Einstein static universe is the primary's column density, with value fixed by closure (§V.2).

## I.5 The three spaces, related [D]

Since $\sigma$ (Part VI) descends to the twin map on $S^4$, and the gravity base already identifies $\hat n$ with $-\hat n$, the fermionic base also maps onto the gravity base. The three form a commuting triangle with the canonical total space at the apex. **The fermionic base is not a dimensional reduction:** $\sigma$ is a free involution, so $E/\sigma$ has the same dimension as $E$; they differ in global structure, not size.

---

# PART II — THE LAWS

> ### ◆ LAW I — GRAVITY
> $$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi\,T^+_{\mu\nu}\quad\text{on }\mathbb{R}_t\times\mathbb{RP}^3,\qquad \Lambda = 1/\ell^2$$
> General relativity on the gravity base, sourced by the meridian-averaged, pair-summed stress-energy. There is no dilaton, no radion, and no extra scalar with a $1/r$ coupling, so PPN $\gamma = 1$ holds trivially. Its solution also fixes the twistor fiber's **radius**, by the locking $\lambda = \Omega\lambda^{\rm ref}$ (§V.3).

> ### ◆ LAW II — THE FIBRATION (MACHIAN FORM)
> $$\nabla\cdot\big(\mu(\rho)\,\nabla\Phi_u\big) = M_{\rm tot}\,\big[\delta^4(\hat d) - \delta^4(-\hat d)\big]\quad\text{on }S^4$$
> The $u$-fibers are the gradient lines of $\Phi_u$. The two flux endpoints — **the poles** — sit at $\pm\hat d$, where $\hat d$ is the matter distribution's own principal axis: the direction of its dipole $d_A = \int\rho\,x_A\,dV$, or, where the dipole vanishes, the principal axis of its quadrupole. All other matter enters through the permeability $\mu(\rho)$. The fibration is **kinematic**: it has no action, and nothing couples to it dynamically.

**The poles are not an input.** Earlier versions placed them by hand. Here they are determined by the matter, which is what makes the arena Machian: *wherever matter is most concentrated, a pole sits there and at its antipode.* Since choosing the polar axis is the same act as choosing the twin map — the twin map is $-1$ on the 4-plane orthogonal to the axis — **the gravity base itself is determined by the matter distribution** (§II.4).

> ### ◆ LAW III — THE SECOND-ORDER CONNECTION
> $$dF = 2\pi\star J_-,\qquad J_- = \frac{\rho_-}{m_{\rm unit}}\ \text{smeared along the meridians},\qquad F = d\alpha$$
> $\alpha$ is the connection of the $U(1)$ that **rotates the twistor fiber about a chosen section** (§III.1) — not an independent bundle, but the fiber's own rotation subgroup. Kinematic.

> ### ◆ LAW IV — ELECTROMAGNETISM
> Maxwell on the cover: $\mathcal{F} = d\mathcal{A}$ with $\mathcal{A}$ a **1-form**, and $\epsilon = \mu_{\rm EM} = 1$. Light follows null geodesics; the photon is the zero mode on every fiber and couples to none of them. The cover is compact, so total charge on it is zero.

*Version 11 replaced this with a self-dual 2-form, in order to give light an "even chirality" that the involution could flip — machinery introduced to support a chirality-selective reading of the seed. That reading is set aside here (Part X), so the 1-form is restored. The 2-form remains a coherent alternative and is recorded in §XII.1.*

## II.0 What each law is, and what you deduce from it [D]

*Stated once, so that the four are never confused with one another.*

| | **Law I** | **Law II** | **Law III** | **Law IV** |
|:--|:--|:--|:--|:--|
| **is** | Einstein's equations | an elliptic equation for a potential | a first-order equation for a curvature | Maxwell |
| **lives on** | the gravity base, 4-D | the cover $S^4$ | the fiber's **longitude** | the cover $S^4$ |
| **determines** | the base metric, hence $\Omega$, hence the fiber length | the meridians, hence the twin pairing and the base itself | the connection $\alpha$ | $\mathcal{F}$ |
| **sourced by** | $T_+$, the **even** part of matter | the poles only; other matter enters as permeability $\mu$ | $J_-$, the **odd** part of matter | electric charge |
| **status** | **dynamical** — it has an action and it back-reacts | **kinematic** — no action, nothing couples to it | **kinematic** — no action, nothing couples to it | dynamical |
| **what you deduce** | orbits, tides, redshift, black-hole exteriors, the $v^2$ plateau (Part V) | which points are twins, where the poles sit, what the jellium is (§I.6, §II.4) | Chern numbers on meridians, the Aharonov–Bohm phase, the $P^2/r^2$ term if it gravitates (§V.6) | the photon's kinematics, the twin's electromagnetic emptiness (Part VIII) |
| **partition slot** | base metric $+$ fiber metric | the meridian fibration itself | 4 of the connection's 8 | — |

**The two kinematic laws are kinematic in the same sense:** they have no action, receive no back-reaction, and are determined instantaneously by the placement of matter. Law I is the only one with dynamics.

**And the fiber-length locking belongs to Law I, not Law III.** $L_E = \Omega L^{\rm ref}$ constrains the fiber's *length*; the connection $\alpha$ is a 1-form on the base, entering the fiber–base cross terms and never the length. See §V.3 for the locking's scope, which is the weak field **[D]**.

## II.1 Why Law II weaves rather than sources [D/V]

With secondary masses as additional same-sign sources of $\Phi_u$, a secondary becomes a critical point; its own field lines are repelled by the center and die at a saddle; and **no fiber through it reaches its antipode** — the twin is lost. With secondaries entering as permeability, the maximum principle forbids interior critical points: every point of $S^4$ lies on exactly one meridian from $0$ to $\infty$, a secondary sits *on* a twin-pair fiber, and the latitudes deform without pinching. In a two-dimensional test with $\mu = 7$ at a mass, seven of seven field lines launched at it passed through and continued **[V]**.

"The center has most of the mass" then reads correctly: $M_c$ sets the total flux, and the meridians are radial to the extent that $\mu$ is uniform.

## II.2 The action

$$S = \int_{\mathbb{R}_t\times\mathbb{RP}^3}\!\!d^4x\,\sqrt{-g}\,\frac{R - 2\Lambda}{16\pi G}\;+\;\int_{\mathbb{PT}^*}\!\!d^6x\,\sqrt{-\hat g}\,\Big[\mathcal{L}_B + \bar\Psi\big(i\Gamma^MD_M - m\big)\Psi + \mathcal{L}_{\rm matter}\Big]$$

with $\hat g$ the gravity-base metric pulled back plus the fiber parts. Varying $g$ on the base integrates matter over both fibers of each base point, so $T_+$ is the *structure of the action*, not an added rule. **Laws II and III have no action.** The constants are $G$, $\Lambda = 1/\ell^2$, the function $\mu(\rho)$, and $m_{\rm unit}$.

$\mathcal{L}_B$ cannot be written in simple covariant form: the naive $-\tfrac12\int H\wedge\star H$ vanishes identically on self-dual configurations (§VIII.2). Law IV is therefore imposed as a *field equation*, which is sufficient here since it is not varied against the metric. The known covariant alternatives — Pasti–Sorokin–Tonin, Henneaux–Teitelboim, doubled formalisms — are recorded in §VIII.2 and not adopted.

## II.3 Covariance, and what Law II does prefer [D/O]

Law I is generally covariant on the four-manifold $\mathbb{R}_t\times\mathbb{RP}^3$.

**Law II is covariant as an equation but elliptic on slices.** Written $\nabla_A(\mu\nabla^A\Phi_u) = J$ it is a scalar equation built from the metric's covariant derivative and transforms correctly under any coordinate change. But it is elliptic on a four-dimensional spatial surface, which means $\Phi_u$ is determined *instantaneously* by the matter on that surface — no initial data, no propagation. **That instantaneity is the point**: it is what makes the fibration kinematic rather than a dynamical field. The price is that an elliptic equation on slices needs a slicing.

On **static** configurations nothing is added: the arena has a timelike Killing vector, and the Killing slicing is canonical — picked out by the geometry rather than imposed. That covers everything computed in this document. For **dynamical** configurations no canonical slicing exists, and Law II owes either a hyperbolic reformulation (losing its kinematic character) or a demonstration that the constraint form yields the same congruence for every slicing. Neither exists **[O]**.

This is the two-speed cover, stated as a property of Law II: gravity links antipodes instantly, light takes $\pi\ell/c$. There is a preferred frame at the level of the cover, and it is unreachable — one cannot access both ends of a twin pair.

---

## II.4 The Machian axis, and its limits [D/V]

**The flux strength is not the content.** Law II is linear in $\Phi_u$, so rescaling the source rescales $\Phi_u$ — and the gradient *lines* of $k\Phi_u$ are identically those of $\Phi_u$. The fibration *is* those lines, so the flux magnitude sets units and nothing else. **The primary's mass never enters the fibration.** What the law fixes is the *location* of the two zeros, and that is what has been made Machian.

**Some source structure is mandatory.** $\nabla\cdot(\mu\nabla\Phi_u) = 0$ everywhere on a compact manifold forces $\Phi_u$ constant — no fibration at all. Poincaré–Hopf then makes one source and one sink the minimum, since each has index $+1$ and the total must be $\chi(S^4) = 2$. Extra pairs cost saddles.

**Why the zeros must be antipodal.** The fibration must be preserved by the twin map, since that is the deck map of the gravity base. The twin map therefore permutes the zeros, and its fixed points on $S^4$ are exactly the two poles **[V]**. A source–sink pair placed at them lies on *every* meridian, which is why the poles project uniformly onto the base (§I.7) and the base stays smooth. Zeros *swapped* by the twin map would be a twin pair at one latitude — one point of the base, hence a singular point of it. Version 11 takes the first case.

**The three limits, verified [V]:**

| configuration | axis from | result |
|:--|:--|:--|
| one dominant mass at $p$ | dipole | axis points **at it**; the mass sits at a pole and its $S^4$-antipode is the empty pole |
| primary $+$ a $1\%$ secondary | dipole | axis tilts by $0.6°$, of order $M_s/M_p$; **the secondary stays at a latitude, acquires no axis, and captures no field lines** |
| two equal masses at $S^4$-antipodes | quadrupole | the dipole vanishes; the axis is their separation; **both masses sit at poles** |

**Mass confers no role.** There is no threshold anywhere in Law II: a secondary of any mass, up to and beyond the primary's, enters through $\mu$ and never sources. Growing it tilts the axis continuously, in proportion to its mass, and nothing else. **The small-secondary limit — Keplerian orbits with no capture — therefore holds at every mass ratio, not as an approximation but as a structural fact.**

**And the equal-mass limit dissolves the distinction entirely.** Matter at a pole projects *uniformly* onto the gravity base, because the poles lie on every meridian; that is the content of §I.4. So two equal masses at the two poles are **both jellium**: the base density is perfectly uniform, there are no lumps at all, the gravity base is the bare Einstein static universe, and there is no center of anything. Each mass has $GM/c^2\ell = \pi/4$ and $r_s = \pi\ell/2$, half the antipodal distance, so no horizon difficulty arises. **The primary/secondary distinction does not merely become symmetric — it disappears.**

## II.5 Many masses: the primary is a limiting case, not a role [V/D]

With $n$ comparable masses the dipole points at the **centroid direction**, which is generically empty. Random configurations of equal masses on $S^4$:

| masses | nearest mass to the polar axis |
|:--:|:--|
| 2 | $39.7°$ |
| 3 | $33.5°$ |
| 5 | $17.1°$ |
| 10 | $29.4°$ |

**No mass sits at a pole.** Every one is at a latitude, so **all are secondaries and none is the primary** — which is the intended reading, and stronger than the two-mass case.

**A pole is occupied only in the strict dominance limit.** For masses $M$ at $p$ and $m$ at $q$ orthogonal, the axis lies at $\arctan(m/M)$ from $p$: $0.6°$ at $m/M = 0.01$, $5.7°$ at $0.1$, $26.6°$ at $0.5$, $45°$ at $1$. **Any finite competitor displaces the pole off the big mass into empty space**, and only $m/M\to0$ puts it exactly on.

> **The pole is where the fibration degenerates — a geometric feature, like the pole of a latitude–longitude grid. Matter *locates* it, through the principal axis, but need not *occupy* it. The "primary" as a body exists only when one mass dominates strongly enough to sit there.**

**Masses refract; they do not puncture [D/V].** It is tempting to picture $n$ masses as $n$ singularities of the fibration, each with its antipodal partner. That is **not** what Law II gives, and the distinction is the law's whole purpose. The sources sit only at $\pm\hat d$; masses enter through $\mu(\rho)$, which is a *permeability*, and high permeability **concentrates** flux — so lines bend *into* a mass and out the far side without terminating. **$n$ masses give $n$ refraction centers and still exactly two singularities.** Verified in a two-dimensional test with three permeability bumps between a source and a sink: six of nine traced lines are drawn through a mass, and every one continues to the sink; none stops inside **[V]**.

The alternative picture — a singularity at each mass plus its antipode — is $2n$ zeros, which by Poincaré–Hopf requires $2n-2$ saddles: the **watershed foam**, in which each mass owns a basin quotienting to its own base, so a small secondary would acquire a nearby twin of its own and double its effective mass locally. That is precisely what the permeability rule exists to prevent.

**And the jellium does not require a primary.** Uniform base density needs uniformity over $\hat n$, and there are two ways to get it: matter **at a pole**, which lies on every meridian; or matter **spread evenly over a latitude**. The first is the special case; the second is what a realistic near-homogeneous universe does. So the smooth background survives with no primary at all, and closure still fixes the total at $\pi\ell/2$. This refines §I.6's identification of the primary with the jellium, which held for the single-mass configuration.

**The jellium/lump split is therefore a statement about position, not mass:** matter on every meridian (at a pole) or spread evenly over a latitude is jellium; matter concentrated at one $\hat n$ is a lump; closure fixes the sum at $\pi\ell/2$ (§V.2). The orbit parameter $f$ of §V.8 is exactly the lumped share.

**What the emergent-$G$ identity does with all this: nothing [D].** The relation $GM_{\rm tot}/c^2\ell = \pi/2$ follows from Law I and closure alone — the Einstein static universe requires $\bar\rho = 1/4\pi\ell^2$, hence a total of $\bar\rho\cdot2\pi^2\ell^3 = \pi\ell/2$. It never used Law II. **The Machian form leaves it untouched**, and when one mass dominates the theory is identical to the fixed-pole version in every respect.

**Cost, recorded [O].** A nearly homogeneous universe has a small dipole on a large total, and since the fibration's lines are independent of the flux magnitude, the axis is decided entirely by that small residual. As matter rearranges, the axis swings and the gravity base swings with it — so a body's twin would change over time. This touches the seed, the $r = 1/\sqrt2$ signpost, and the involution of Part VI, which is defined by the twin map. Not resolved here.

# PART III — THE SECOND ORDER

## III.1 Where Law III's $U(1)$ comes from [T/D]

*In earlier versions the Hopf circle was an input and Law III was written on it. Here it is derived.*

**A 2-sphere fiber has $SO(3)$, not $U(1)$.** A $U(1)$ appears only once an **axis** is chosen — that is, once a **section** of $\mathbb{CP}^3\to S^4$ is given, assigning a complex structure to each point. Then the rotations about that section form a $U(1)$, and its connection is Law III's $\alpha$.

**Sections exist exactly where Law III needs them [T].** Write $\mathbb{CP}^3 = \mathbb{P}(S^-)$. A section requires $S^-$ to split as $L_1\oplus L_2$. Over all of $S^4$ that would force $c_2 = c_1(L_1)c_1(L_2) = 0$ against $c_2(S^-) = 1$ — impossible, which is the statement that $S^4$ admits no almost complex structure. But over $S^4$ minus a secondary meridian,

$$S^4\setminus\text{circle}\ \simeq\ S^2$$

over which **every** rank-2 complex bundle splits. **The meridian removal that Law III already demanded is exactly the surgery that supplies its own gauge group.**

> **The Hopf circle is no longer an input. It is the twistor fiber's rotation subgroup about a section, and the section exists because the meridians are removed.**

**The Chern number is even [V].** With $c_1(S^-) = 0$ the splitting needs $c_1(L_2) = -c_1(L_1) = -a$, and the $U(1)$ bundle is $\mathrm{Hom}(L_1,L_2)$ with

$$c = c_1(L_2)-c_1(L_1) = -2a\qquad\textbf{always even}$$

with no natural square root, since the fiber coordinate $\zeta = w_2/w_1$ *is* a section of $L_1^*\otimes L_2$. Restricted to a shell the total space is the lens space $L(|c|,1)$, whose fibers link $|c|$ times — so the linking is even, and $M_-/m_{\rm unit}$ must be even with it. This is the same 2 that §IX.1 produces from $\mathbb{Z}_2\subset U(1)$, by an independent route **[O]**.

**The symmetric solution.** Over a shell of angular radius $\vartheta$ about a secondary,

$$F\big|_{\rm shell} = \tfrac{c}{2}\sin\vartheta\,d\vartheta\wedge d\varphi,\qquad \int_{\rm shell}F = 2\pi c$$

verified **[V]**. Many secondaries superpose; a continuous $\rho_-$ gives a smooth $J_-$.

## III.2 Why Law III requires $S^4$ [D]

In four dimensions a 2-form's source is a 1-form, and consistency $d(dF) = 0$ requires $d\star J_- = 0$: the source must be a conserved current supported on closed lines. On $S^4$ every meridian is a closed circle, so this holds automatically. On $\mathbb{R}^4$ the rays have endpoints and the law is inconsistent. **$S^4$ is what makes Law III well-posed.**

## III.3 The monopole is the meridian [T/D]

A 2-sphere cannot link a point in a four-space ($H^2(S^4\setminus\text{points}) = 0$); it links a *circle* ($H^2(S^4\setminus\text{great circle}) = \mathbb{Z}$). So the Chern class lives on the meridian through the secondary — the mass smeared along its fiber, exactly as gravity sees it. Orienting the meridian once around, its two equatorial crossings are traversed in opposite senses, giving linking numbers $+1$ at $\hat n_0$ and $-1$ at $-\hat n_0$.

**The anti-monopole at the twin is the same circle seen from the other hemisphere**, and the Chern number on the meridian through $[\hat n]$ is $\big(M(\hat n) - M(-\hat n)\big)/m_{\rm unit}$ — the odd part, by construction.

## III.4 The topology of $E$ [T]

Write $E$ for the $U(1)$ bundle of §III.1 — the twistor fiber's rotation subgroup about a section — over $S^4\setminus\Gamma$, with $\Gamma$ the graph formed by the $N$ secondary meridians through the two poles. Alexander duality gives $H^2 = \mathbb{Z}^{2N-1}$; the physical bundle has equal flux on both arcs of each meridian and so lives in $\mathbb{Z}^N$, one integer per secondary. For $N = 1$, $S^4\setminus\text{circle}\simeq S^2$ and $E\simeq S^3$.

**$S^4$ does not become anything.** $E$ is a new five-dimensional space fibered over it; each 2-shell is *lifted* to a Hopf 3-sphere, not replaced. Since every meridian contains both poles, the poles lie in $\Gamma$ and are removed from $E$'s base — which is what makes $\sigma$ act freely (§VI.2).

## III.5 The partition principle [T/V/D]

**Geometric.** A metric in coordinates adapted to a fibration splits into base, fiber, and connection, pointwise, with no remainder. For the two-dimensional twistor fiber:

| | | |
|:--|:--|--:|
| base metric on $S^4$ | $4\cdot5/2$ | 10 |
| fiber metric, $2\times2$ symmetric | $2\cdot3/2$ | 3 |
| connection: one 1-form per fiber direction | $2\times4$ | 8 |
| **total** | | **21** |

which is $6\cdot7/2$, the full count for a six-manifold **[V]**.

**The fiber's three reduce to one.** Roundness is two constraints, leaving the **radius** $\lambda$ — and Law I determines exactly one function, $\Omega = \phi^2$, with $\lambda = \Omega\lambda^{\rm ref}$ (§V.3). One in, one out, exactly as the Hopf *length* did. **The fiber's shape is fully fixed by Law I and carries no independent information**, which is the sense in which the field equations see only the base.

**The connection's eight split once a section is chosen — and only four are assigned [D/O].**

| | what it is | status |
|:--|:--|:--|
| 4 | rotations about the section | **Law III's $U(1)$** — assigned |
| 4 | how the section itself varies — the **tilt field** | **unassigned** |

> **Version 11's partition closed exactly, $15 = 10+1+4$ with every slot filled. Version 13's does not.** Four components — precisely the tilt data in which Kerr's parameter $a$ lives (§IX.4) — have no law sourcing them. The natural candidate is angular momentum, which version 11 kept in the shift, inside the base metric's ten; if so the two descriptions overlap and must be reconciled. **This is the sharpest open problem the overhaul creates**, and it is a named slot with a named occupant, which it was not before.

**Physical.** Even matter $T_+$ fills the base metric and the fiber length, through Law I. Odd matter $T_-$ fills the connection, through Law III, as the Chern class and its continuous deformation. The Hopf form itself is neither — it is the arena. Four even functions from gravity, two odd from the second order, nothing left over and nothing double-counted.

**Curvature.** Base Ricci $\leftarrow T_+$. The Weyl tensor of $E$ is exactly the connection's deviation from Hopf: $C_{abcd}C^{abcd} = 0$ for the Hopf connection, and $4\epsilon^2(16 - 13\sin^2\vartheta)/3\sin^4\chi$ for a perturbation $\epsilon\sin^2\vartheta$ **[V]**.

> **The projection discards the odd half; the twist recovers it; together they see all of $T$.**

## III.6 What sees $E$ [T/D]

Light does not: the photon is the zero mode, and Kaluza–Klein charge is fiber momentum, which is spin-independent. Gravity fixes $E$'s even half and is blind to its odd half. If the flux gravitates with coupling $g_2$, it adds a Reissner–Nordström term (§V.6).

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

## V.3 Law I as the fiber-length equation [V/D]

Weak-field statics are conformally round, $g_3 = \phi^4g_{S^3}$, and the Hamiltonian constraint linearizes about the Einstein static universe to

$$(\Delta_{S^3} + 3)\,\delta\phi = -2\pi\,\delta\rho_+$$

— the twin-theorem operator, acting on the conformal factor. Write $\Omega\equiv\phi^2$.

**The locking, on the twistor fiber.** A round 2-sphere is fixed by one number, its radius, exactly as a circle is fixed by its length. So the reading transfers with a change of word and not of structure:

| | fiber | the one number | locking |
|:--|:--|:--|:--|
| versions 6–12 | Hopf circle | length $L_E$ | $L_E = \Omega L^{\rm ref}$ |
| **version 13** | twistor 2-sphere | **radius** $\lambda$ | $\lambda = \Omega\lambda^{\rm ref}$ |

and the fiber's **area** follows as $4\pi\lambda^2\propto\Omega^2 = \phi^4$, the square of the old length scaling. To first order

$$\frac{\delta\lambda}{\lambda} = -\Phi,\qquad N\cdot\lambda = \text{constant}$$

**Fibers swell in wells by exactly the potential, and space stretches as much as time slows.** For a ball with its twin, $\Omega = 2.017$ at the ball's center and identically at the empty twin, agreeing to $10^{-11}$ **[V]**. $L_H$ is the local length scale, not a circumference.

> ### ◆ THE SCOPE OF THE LOCKING — read this before using it
> **Both statements are first-order and neither is exact.** Isotropic Schwarzschild has $N = (1-m/2r)/(1+m/2r)$ while $N = \Omega^{-1}$ would demand $(1+m/2r)^{-2}$. Expanding,
> $$N_{\rm Schw} = 1 - \frac{m}{r} + \frac{m^2}{2r^2},\qquad \Omega^{-1} = 1 - \frac{m}{r} + \frac{3m^2}{4r^2}$$
> They agree to first order and **part at $O(m^2/r^2)$**; the exact product is $N_{\rm Schw}\Omega = 1 - m^2/4r^2$, not $1$ **[V]**.
>
> **Imposing $N\Omega = 1$ exactly would change the spacetime.** The line element becomes $ds^2 = -U^{-2}dt^2 + U^2dx^2$ with $U = \Omega$ — the **Majumdar–Papapetrou** form, giving *extremal* Reissner–Nordström, $Q = M$. Every body an extremal black hole. **Excluded**, and not rescuable through the second-order flux, since Mercury bounds $g_2/m_{\rm unit}<0.024$ **[V/T]**.
>
> **So the fiber reading holds where it always has: the weak-field static sector.** Beyond it $\Omega$ and $N$ are two independent functions, both determined by Law I but not by $N\Omega = 1$ **[D]**.
>
> **And one further caveat specific to this version.** Twistor space is **conformally invariant**: a complex structure compatible with a metric depends only on the conformal class, so the fiber as a *manifold* does not see $\Omega$ at all. The radius is therefore extra data, not supplied by the construction. Worse, the *canonical* twistor metric fixes it by the scalar curvature, $\lambda\propto1/\sqrt{s}$, and in a vacuum region with $\Lambda$ that is constant — the canonical choice would give **no wells**. So $\lambda = \Omega\lambda^{\rm ref}$ is a **posited locking**, exactly as the Hopf version was: same status, neither better nor worse, but now attached to the fiber Newman–Janis requires rather than to one gestured at **[D/O]**.

## V.4 The metric, written out [V/D]

*The level of definiteness every law in this document is held to.*

**The six-dimensional line element**, in the conformally-round sector:

$$ds^2_7 = -N^2dt^2 + \lambda^2\,g_{S^2}^{(\alpha)} + \kappa^2du^2 + \phi^4g_{S^3}$$

with $N$ the lapse and $\lambda = \Omega\lambda^{\rm ref}$ the twistor fiber's radius, both determined by Law I with $\Omega = \phi^2$; $g^{(\alpha)}_{S^2}$ the round fiber metric with its horizontal distribution twisted by the connection of §III.1; $u$ the meridian and $\kappa$ its scale; $g_{S^3}$ the round metric of the latitude.

**A secondary point mass.** Solve $(\Delta_{S^3}+3)\delta\phi = -2\pi\delta\rho_+$ for a point mass at $\chi = 0$ with its twin. Near the mass the Green's function goes as $1/\sin\chi$, so with $r = \ell\chi$

$$\phi = 1 + \frac{GM}{2r} + O(r^2/\ell^2)$$

— the isotropic Schwarzschild conformal factor. The four-dimensional part of the line element is then

$$ds^2_4 = -\left(\frac{1-GM/2r}{1+GM/2r}\right)^2dt^2 + \left(1+\frac{GM}{2r}\right)^4\big(dr^2 + r^2d\Omega_2^2\big)$$

**isotropic Schwarzschild exactly**, with the closed-universe corrections entering at $O(r^2/\ell^2)$ — $4\times10^{-15}$ at 10 kpc for $\ell = 63$ Gpc (§V.10).

**The shells, metrically.** A shell at coordinate radius $r$ has proper area

$$A = 4\pi r^2\left(1+\frac{GM}{2r}\right)^4$$

the standard areal radius. Over each shell sits the restricted $U(1)$ bundle of §III.1, with total space the lens space $L(|c|,1)$ for even Chern number $c$, and twistor-fiber radius $\lambda\propto\phi^2$ — largest where the shell is deepest in the well.

**What remains undetermined [O].** The meridian scale $\kappa$, inherited unfixed; and the four unassigned connection components of §III.5.

## V.5 Weyl from the fiber length [V]

$$E_{ij} = -2\big[\nabla_i\nabla_j\phi\big]^{\rm TF},\qquad \phi = \sqrt{L_H/2\pi\ell}$$

The trace of the Hessian is fixed by the constraint and is the matter; the trace-free part is the tidal field. For Schwarzschild the eigenvalues are $(m/r^3)(1,-\tfrac12,-\tfrac12)$ — Petrov type D, with repeated principal null directions $\partial_t\pm\widehat{\nabla L_H}$, the directions of steepest fiber-length change. Type D here is forced by spherical symmetry. Beyond the weak-field static sector the fiber length is one of six metric components: magnetic Weyl lives in the shift, gravitational waves in the transverse-traceless part of the base 2-metric.

## V.6 Charged and rotating black holes [D/O]

**Electric charge.** A charged secondary has the ordinary Reissner–Nordström exterior on the gravity base, since Law IV is ordinary Maxwell (§VIII.1).

**The second-order flux.** If $E$'s flux gravitates with coupling $g_2$, it adds a Reissner–Nordström-type term with an *effective magnetic charge*:

$$f(r) = 1 - \frac{2GM}{c^2r} + \frac{G\,P^2}{c^4r^2},\qquad P = g_2\,\frac{M}{m_{\rm unit}}$$

The Newtonian term is untouched; the horizon moves, $r_\pm = (GM/c^2)\big(1\pm\sqrt{1 - P^2/M^2}\big)$; and the extremality bound becomes $M^2 \geq Q^2 + P^2$. Every black hole carries $P$ proportional to its own mass, so extremality is tightened universally.

**The bound.** The repulsive $P^2/r^2$ term shifts a perihelion by $-(P/M)^2/6$ relative to general relativity's advance. Mercury agrees with general relativity to $10^{-4}$, hence

$$g_2/m_{\rm unit} = P/M < 0.024$$

Lunar laser ranging gives nothing useful ($M/r\sim10^{-11}$ at the Moon); ringdowns test $P/M$ at the $0.1$–$0.3$ level, weaker. The double pulsar can tighten it **[O]**.

**The twin of a hole.** Same mass (gravity reads $T_+$, chirality- and sign-blind); opposite second-order monopole, $-M_-/m_{\rm unit}$, by the linking number of §III.3; and no independent electromagnetic charge, since the twin's $Q^2/r^2$ term is a **tidal charge** with $\nabla\cdot E = 0$ and $E = 0$ there (§V.7). Rotation is untouched: magnetic Weyl lives in the shift, which no fiber carries (§V.5).

## V.7 Charge and the twin [V/D]

Gauss on a closed section forces a compensating charge *somewhere*, and the seed puts nothing at the antipode. With the compensating charge wherever the other charges are, the field of a charge $Q$ is regular at the antipode and vanishes there — verified: $|E|\to0$ linearly. **The twin carries gravitational shape without electromagnetic content, because it carries no matter at all** (§VIII.2).

## V.8 Orbits and the $v^2$ family [V]

**Rosettes and precession.** On the gravity base a secondary is a well in the jellium, and closed-universe orbits are retrograde-precessing rosettes: apsidal advance $1.945\pi$ per radial period at small apocenter, falling to $1.836\pi$ in the mid-disk. The kinematic pattern speed $\Omega-\kappa/2$ falls by a factor 10 across a disk where Kepler alone would give 20 — the closure term halves the winding rate of kinematic spirals. At galactic radii in the cosmic arena the closure term is $10^{-7}$ of Kepler.

**The closure plateau.** For a circular orbit at colatitude $\chi$ on $S^3(\ell)$ the effective potential is $\Phi(\chi) + L^2/2\sin^2\chi$; stationarity gives $L^2 = \Phi'(\chi)\sin^3\chi/\cos\chi$, and with $v = L/\sin\chi$,

$$v^2(\chi) = \Phi'(\chi)\tan\chi$$

At the equator $\Phi'(\pi/2) = 0$ by twin symmetry, so by L'Hôpital $v^2_{\rm eq} = -\Phi''(\pi/2)$. Solving the twin-theorem equation for a lump holding a fraction $f = M/M_{\rm tot}$ of the closure mass gives, numerically and converged as the lump shrinks,

$$v^2_{\rm eq} = 2.352\,f = 1.497\,\frac{GM}{\ell}\qquad\text{(consistent with }3GM/2\ell\text{ to }0.2\%)$$

**The value is independent of how the lump is packed** — only the monopole term survives at the equator — and is linear in the lumped mass. **This corrects an earlier quotation of $4GM/\pi\ell = 1.273\,GM/\ell$, which was $15\%$ low [V/R].** Sign and scaling are unchanged: linear in $M$, inverse in $\ell$.

## V.9 The lumped-mass limit [V/D]

The jellium is the pole matter's projection and closure fixes the total at $M_{\rm tot} = \pi\ell/2$, so a secondary of mass $M$ is a lump holding a fraction $f = M/M_{\rm tot}$ of that total — not matter added on top of it. The limit $f\to1$ means *all* of the universe's mass is in one lump at a latitude, with no smooth background left.

| $f$ | $r_s = 2GM/c^2$ | orbital range in $\chi$ |
|:--:|:--:|:--|
| $0.1$ | $0.314\,\ell$ | $(0.31,\ \pi)$ |
| $0.5$ | $1.571\,\ell$ | $(1.57,\ \pi)$ |
| $0.9$ | $2.827\,\ell$ | $(2.83,\ \pi)$ |
| $1.0$ | $\pi\ell$ | **none** |

At $f = 1$ the lump's Schwarzschild radius equals $\pi\ell$, the antipodal distance — **the diameter of the universe.** Nothing is outside it; there are no orbits because there is no exterior. The plateau formula reads $v^2_{\rm eq} = 2.352\,c^2$, which is its way of saying the same thing.

**The Keplerian limit, quantified [V].** Near a point mass the Green's function of $(\Delta+3)$ behaves as $1/\sin\chi$, so with $r = \ell\chi$

$$\Phi(r) = -\frac{Gm}{r}\left[1 + \frac{r^2}{6\ell^2} + O(r^4/\ell^4)\right]$$

The closed-universe correction is $4\times10^{-15}$ at $10$ kpc and $4\times10^{-45}$ at $1$ AU, for $\ell = 63$ Gpc. The other correction is the jellium: a uniform background gives a force $\sim+\tfrac{4\pi}{3}G\bar\rho\,r$, which overtakes $Gm/r^2$ only where the enclosed background mass equals $m$ — at $1.2$ Mpc for a $10^{12}M_\odot$ galaxy, and $0.12$ kpc for the Sun. **Inside a galaxy, and throughout any planetary system, motion is Keplerian to parts in $10^{14}$ or better.** The closure terms matter only near the crossover scale and at the equator, where they produce the plateau of §V.8.

**Law II is untroubled by the limit.** A secondary is a permeability bump at any mass, so the flux endpoints stay at the poles and the fibration is intact at $f = 1$. What fails is the *base geometry* — gravity, not the fibration. Under the old reading, where masses sourced $\Phi_u$, a large secondary would have become a rival source and the twin would have been lost; the permeability rule is what makes the limit harmless. Contrast §II.4's *other* limit, two equal masses at the **poles**, where the base stays perfectly homogeneous and no lump exists at all.

## V.10 The two fluxes, compared [V/D]

The fibration flux of Law II and the second-order flux of Law III are both Gauss charges — conserved quantities obtained by integrating a field over an enclosing surface, both additive, both obeying a divergence law. They differ in three ways, and the differences explain why one appears in the metric as a $1/r^2$ term and the other as a background.

| | fibration flux (Law II) | second-order flux (Law III) |
|:--|:--|:--|
| sourced by | matter at the poles | secondaries, on their meridians |
| odd mass $\rho_-$ | **zero** — a pole is its own twin | $M(\hat n) - M(-\hat n)$ |
| falloff on the cover | $1/r^3$ (four spatial dimensions) | $1/r^2$ (flux through 2-spheres) |
| image on the gravity base | **uniform: the jellium** | **localized: the $P^2/r^2$ term** |
| total | $M_{\rm tot} = \pi\ell/2$ | Chern numbers summing to zero |

**The primary carries no second-order charge, for a structural reason.** Law III is sourced by $\rho_- = \rho(\hat n)-\rho(-\hat n)$, and the twin map *fixes* the poles, so at a pole $\rho_- = \rho - \rho = 0$. **The primary's Chern number is zero because the primary is its own twin.** It sources the fibration flux and nothing else; secondaries source the second-order flux and contribute nothing uniform. Cleanly complementary.

**The difference is localization.** Both poles lie on every meridian, so the fibration flux contributes equally to every fiber average and its base image is uniform — and a uniform source gives a background term, not a $1/r^2$ one. The second-order flux is concentrated on a single meridian, so its base image is localized and its energy $|F|^2\sim c^2/r^4$ integrates to the $P^2/r^2$ metric term of §V.6. **Same kind of object; different spread.**

**And the totals coincide exactly [V].** $\bar\rho\cdot\mathrm{Vol}(S^3) = (1/4\pi\ell^2)(2\pi^2\ell^3) = \pi\ell/2 = M_{\rm tot}$, with difference identically zero. The fibration flux *is* the total jellium mass — which is what the $G$ identity says, read as a flux statement.

**The Mach relation is a horizon statement [V].** $r_s(M_{\rm tot}) = 2GM_{\rm tot}/c^2 = \pi\ell$, and $\pi\ell$ is exactly the antipodal distance on $S^3(\ell)$. **The closure mass's Schwarzschild radius is the diameter of the universe:** a closed static universe is marginally its own horizon, and $GM_{\rm tot}/c^2\ell = \pi/2$ is that fact written as a mass.

## V.11 The static wall [T]

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

# PART VIII — ELECTROMAGNETISM

## VIII.1 The law, and what survives [D]

Maxwell on the cover, $\mathcal{F} = d\mathcal{A}$, with $\epsilon = \mu_{\rm EM} = 1$ and light on null geodesics. The photon is the **zero mode** on every fiber — it carries no Hopf charge and no fiber momentum — and therefore couples to nothing in the second order. On the compact cover, total charge is zero by Gauss, and the electric flux through every latitude vanishes (§V.2).

## VIII.2 The twin is electromagnetically empty [V/D]

Gauss on a closed section forces a compensating charge somewhere, and the seed puts no matter — and hence no charge — at the antipode. With the compensating charge wherever the other charges are, the field of a charge $Q$ is regular at the antipode and vanishes there, verified: $|E|\to0$ **linearly**. So the twin carries gravitational shape and no electromagnetic content. A charged secondary's twin carries the $Q^2/r^2$ term of the metric as a **tidal charge**, with $\nabla\cdot E = 0$ and $E = 0$ there.

## VIII.3 Light still has a chirality — a complex one [T]

Reverting to a 1-form does not cost light its chirality; it makes it complex rather than real. In four Lorentzian dimensions $\star^2 = -1$ on 2-forms, so the eigenvalues of $\star$ are $\pm i$ and the self-dual split is

$$\mathcal{F}^\pm = \tfrac12\big(\mathcal{F} \mp i\star\mathcal{F}\big)$$

complex, and standard — it is what the Newman–Penrose scalars $\phi_0,\phi_1,\phi_2$ describe. **In a complexified arena this is native rather than awkward**, and it is the electromagnetic entry in the three-fold chirality table of §IX.1. What is lost relative to version 11 is only the *real* self-duality that a middle-degree form would have carried, and with it the machinery that required six-dimensional Lorentzian signature to exist at all.

# PART IX — THE COMPLEX STRUCTURE

*The complexification is no longer a layer beside the arena: since version 13 the twistor fiber **is** the arena's fiber. This part states what that buys, what it does not, and the retraction that keeps time out of it.*

## IX.1 The ray–line principle, run twice [D]

The seed's logic is: **matter lives on a ray, gravity lives on the space of lines, so gravity reads the fiber of the map rays $\to$ lines.** Run that logic in each of the two fields in which projective space exists:

| | over $\mathbb{R}$ | over $\mathbb{C}$ |
|:--|:--|:--|
| ambient | $\mathbb{R}^4$ | $\mathbb{C}^4$ |
| unit sphere — the **rays** | $S^3$ | $S^7$ |
| projective space — the **lines** | $\mathbb{RP}^3$ | $\mathbb{CP}^3$ |
| fiber of rays $\to$ lines | $\mathbb{Z}_2 = \{\pm1\}$ | $U(1)$ |
| what gravity cannot see | **which ray** — the twin | **which phase** — the Hopf charge |
| what gravity reads | $T(\hat n)+T(-\hat n)$, the $\mathbb{Z}_2$ sum | the $U(1)$ average — the zero mode |

> **The twin and the Hopf charge are the same blindness, one real and one complex.** "Gravity reads $T_+$" and "gravity is blind to the Hopf fiber" are a single statement: *gravity integrates over the fiber of rays $\to$ lines.* The theory has carried both since version 6 without knowing they were one thing.

**And they are nested, not parallel [V].** Since $\mathbb{Z}_2\subset U(1)$, the two quotients of $S^3$ chain:

$$S^3\ \xrightarrow{\ /\mathbb{Z}_2\ }\ \mathbb{RP}^3\ \xrightarrow{\ /(U(1)/\mathbb{Z}_2)\ }\ \mathbb{CP}^1 = S^2$$

so **$\mathbb{RP}^3$ is itself a circle bundle over $S^2$**, of Chern number 2 — the lens space $L(2,1)$. The gravity base is not merely a quotient of $S^3$; it is a Hopf-type bundle in its own right, and the 2 is the same even number the complex side produces independently (§IX.4).

## IX.2 Why the seed's base must be real projective [T/D]

$\mathbb{RP}^n$ takes every dimension; $\mathbb{CP}^n$ has dimension $2n$ and is **always even**. Space is three-dimensional. So:

| candidate | dimension | verdict |
|:--|:--:|:--|
| $\mathbb{CP}^1$ | 2 | too small |
| $\mathbb{CP}^2$ | 4 | a spacetime, not a space |
| $\mathbb{CP}^3$ | 6 | too big |
| $\mathbb{RP}^3$ | **3** | the only fit |

> **The seed's base is real projective because space is odd-dimensional.** Not a modelling choice, and not replaceable by any complex projective space. The complex version of the principle can only sit *above* the real one — which is exactly where Law III sits.

## IX.3 The Penrose–Ward correspondence [T]

> **Anti-self-dual solutions on a four-manifold are equivalent to holomorphic data on its twistor space.**

For gauge fields this is Ward's construction; for gravity, Penrose's *nonlinear graviton*. The twistor space of $S^4$ is

$$\mathbb{CP}^3\longrightarrow S^4 = \mathbb{HP}^1,\qquad\text{fiber }\mathbb{CP}^1 = S^2$$

canonical, with nothing chosen: over $x$ the fiber is the sphere of complex structures on $T_xS^4$ compatible with metric and orientation, $SO(4)/U(2) = S^2$ — equivalently the sphere of unit self-dual 2-forms.

**Why this applies here.** $S^4$ is the cover, a conformal four-manifold; the correspondence needs nothing more. In particular it does **not** require $S^4$ to be a spacetime, and the theory's $S^4$ is *space*.

**The chirality table.** With the layer in place, one $\mathbb{Z}_2$ appears in three sectors:

| sector | chirality | where |
|:--|:--|:--|
| gravity | $C^+ / C^-$ | the ASD half is holomorphic on $\mathbb{CP}^3$ |
| light | $\mathcal{F}^\pm = \tfrac12(\mathcal{F}\mp i\star\mathcal{F})$ | Maxwell's complex self-dual split (§VIII.3) |
| matter | $S^+ / S^-$ | Weyl spinors (Part VII) |

## IX.4 Kerr from a complex worldline [T/V]

**This is a construction in complexified *space*, and that is why it fits.** The Newman–Janis shift displaces a *spatial* coordinate and leaves time untouched — so the complexification it needs is of space, and the theory's $S^4$ is space. Six steps:

**Step 1 — put Schwarzschild in Kerr–Schild form.** Write the metric as flat plus a null-squared term,

$$g_{ab} = \eta_{ab} + 2H\,k_ak_b,\qquad H = \frac{M}{r},\qquad k = \Big(1,\ \frac{x}{r},\frac{y}{r},\frac{z}{r}\Big)$$

with $k$ null and geodesic with respect to *both* $\eta$ and $g$. This is exact, not linearized **[T]**.

**Step 2 — notice the whole solution rests on one harmonic function.** $H$ is built from the Coulomb function $1/r$, and $\nabla^2(1/r) = 0$ away from the origin **[V]**. Everything else in Kerr–Schild form is determined by $k$.

**Step 3 — complexify, and displace the source.** $1/r$ continues holomorphically in $z$, so shift the source along the *imaginary* axis, $z\to z - ia$:

$$\frac{1}{\sqrt{x^2+y^2+z^2}}\ \longrightarrow\ \frac{1}{\sqrt{x^2+y^2+(z-ia)^2}}$$

The displaced function is still harmonic — verified, the Laplacian remains zero **[V]** — so it solves the same equation. **Nothing has been added; a source has been moved.**

**Step 4 — find where it becomes singular.** The complex distance vanishes when $x^2+y^2+(z-ia)^2 = 0$. Separating real and imaginary parts gives $-2az = 0$ and $x^2+y^2+z^2 = a^2$, hence

$$z = 0\quad\text{and}\quad x^2+y^2 = a^2$$

**a ring of radius $a$** **[V]**. Schwarzschild's point singularity has become **Kerr's ring**, and $a = 0$ collapses it back to a point.

**Step 5 — read off the real slice.** Introduce the oblate radius $R$ by $\frac{x^2+y^2}{R^2+a^2} + \frac{z^2}{R^2} = 1$. The complex distance is then exactly $R + ia\cos\theta$, and

$$H = \frac{MR^3}{R^4 + a^2z^2}$$

which together with the corresponding null $k$ **is the Kerr metric in Kerr–Schild form** **[T]**.

**Step 6 — identify the parameter.** Computing the angular momentum of the result gives $J = Ma$, so $a = J/M$: **the imaginary displacement *is* the angular momentum per unit mass** **[T]**.

**What the shift *is*, in plain terms [D].** The source's **position acquires an imaginary part**. Writing the displaced position as $(x,y,z) - i(0,0,a)$:

| part | what it is |
|:--|:--|
| **real** | where the body sits |
| **imaginary** | a **vector**: its direction is the spin axis, its magnitude is $a = J/M$ |

> **Rotation is the imaginary part of a position.** And the *type* matters: the imaginary part is a **vector**, which can point along an axis. Contrast §IX.6, where a complex structure — a 2-form — cannot select a direction and so cannot be time. The theory's two complex objects are of genuinely different kinds, and that is why one carries spin and the other cannot carry time.

**And the same fact, read geometrically: rotation is misalignment with a fibration [T/D].** This is what the complex layer is *for*. Euclidean twistor theory gives an exact dictionary:

| in $S^4$ and its complexification | in $\mathbb{CP}^3$ |
|:--|:--|
| a **real** point of $S^4$ | a line that **is a fiber** — $\varsigma$-invariant, "vertical" |
| a **complex** point, off the real slice | a line that is **not** a fiber — "tilted" |

So *"the source's position has an imaginary part"* and *"the source's twistor line fails to be vertical"* are **the same statement in two languages**.

> Without the layer, $a = J/M$ is an algebraic fact: a coordinate acquired an imaginary part. With it, the same fact is geometric — **the source's line has come out of alignment with a fibration, and $a$ measures the misalignment.** *Rotation is misalignment with a fibration.*

**And the tilt is in the canonical total space itself [D].** This is what the version-13 overhaul buys. The canonical total space **is** $\mathbb{R}_t\times\mathbb{CP}^3$, so a source's twistor line is an object *of the arena*, not of an auxiliary construction:

| source | its line | relative to the fibration |
|:--|:--|:--|
| Schwarzschild | **is** a fiber | **vertical** — aligned |
| Kerr | is **not** a fiber | **tilted** — misaligned by $a$ |

In versions before this one the tilt lived in a layer bolted on beside the arena, and had to be kept carefully distinct from the Hopf structure. With the twistor fiber made fundamental there is only one fibration to be misaligned with, and the misalignment is $a$.

**Where the shift happens.** In the complexification of $S^4$ — the complex quadric, eight real dimensions, with $S^4$ its real slice. The source moves off that slice, and its line comes off vertical.

**Where the tilt data lives in the partition [O].** In the four unassigned connection components of §III.5 — how the section varies from point to point. Nothing yet sources them.

**Two six-dimensional spaces sit over $S^4$, and they are not the same [D].**

| | fiber | role |
|:--|:--|:--|
**And what the real slice shows is a ring [V].** In the middle space the Kerr source has **no location at all** — its position is complex. What appears in the real slice is the singular set, $z = 0$ and $x^2+y^2 = a^2$: a **one-dimensional ring** of radius $a$. *One picture from version 12 is retired: the source as a 2-sphere in $S^4$. That 2-sphere is the tilted line's **projection**, a different object from the ring, and no relation between them was established* **[R]**. The tilt itself stands.

## IX.5 What the complex layer earns, and what it does not [D]

*Stated plainly, because the layer is a large addition and should be held to account.*

| job | verdict |
|:--|:--|
| geometrize complex position as misalignment | **earned**, and now internal: the tilt is misalignment with the arena's own fiber (§IX.4) |
| supply Law III's gauge group | **earned** — the $U(1)$ is the fiber's rotation subgroup about a section, and the section exists because the meridians are removed (§III.1) |
| the ray–line unification, $\mathbb{Z}_2$ and $U(1)$ (§IX.1) | earned, but it needs only "projective space $=$ space of lines," not twistor space |
| the parity theorem (§IX.2) | earned, but it is dimension counting |
| Penrose–Ward for anti-self-dual solutions (§IX.3) | **available and unused** — the theory solves no anti-self-dual equations |
| time | **no** — a type error (§IX.6) |

Two jobs squarely — the geometric reading of rotation and the derivation of Law III — two that it frames without requiring, one capability standing idle, one failure. **And one new debt: the partition no longer closes (§III.5).**

**The even Chern number [V].** Removing two sections of $\mathbb{CP}^3 = \mathbb{P}(S^-)$ requires $S^-$ to split as $L_1\oplus L_2$. Over all of $S^4$ that would force $c_2 = 0$ against $c_2(S^-) = 1$ — impossible. Over $S^4$ minus a meridian, homotopy-equivalent to $S^2$, every rank-2 bundle splits, so it is possible — and with $c_1(S^-) = 0$ the associated circle bundle has $c = -2a$, **always even**. The same 2 that §IX.1 produced from $\mathbb{Z}_2\subset U(1)$.

**What it does not change.** Rotation still sits in the shift vector on the base, as version 11 said. What the overhaul adds is a second home for it upstairs — the tilt field — and the two must be reconciled (§III.5).

## IX.6 The retraction: why the layer supplies no time [T/D]

*Version 12 read the twistor fiber's latitude as the time direction. This is retracted, and the reason is worth stating because it is structural rather than a matter of adjustment.*

**There is no time in twistor theory.** Euclidean twistor space fibers over a **Riemannian** $S^4$, signature $(+,+,+,+)$. Time appears only on choosing a Lorentzian real structure on the complexification, and that choice is external to the twistor geometry. What the geometry supplies is a holomorphic object of which both signatures are real slices.

**And the fiber cannot supply time, by type.** A complex structure satisfies $J^2 = -1$, so it has **no real eigenvectors** **[V]** — it *pairs* the four directions into two complex ones. Time requires *selecting one direction out of four*, the opposite operation, and a 2-form cannot do it; only a vector or 1-form can.

> **The fiber's data is of the wrong type to be time. This is a type error, not a gap.**

**Two repairs were tried and both fail.** Wick-rotating the polar direction $\chi$ is blocked, because $\chi$ is exactly what the meridian quotient removes — and splitting that quotient to save it would gut the seed. Taking the ray$\to$line circle of $S^7\to\mathbb{CP}^3$ as time is blocked because **time must be a line and that fiber is a circle**: keep it circular and every worldline closes; unwrap it and, since $\mathbb{R}$-bundles are always trivial, the twist one wanted to use vanishes, leaving a universal time-connection — a Gödel-like rotating universe, and the causal problem returns by another door **[D]**.

**So time is an input**, as in versions 6 through 11. One smaller claim survives: the Lorentzian real structure singles out the polar axis, and under the Machian Law II (§II.4) that axis is the matter's own principal axis — so the **direction** of time would be Machian even though the signature itself is posited **[S]**.

# PART X — DETECTION

## X.1 The base-resolution principle

> ### ◆ THE BASE-RESOLUTION PRINCIPLE
> A detector is a base object. It can record base position and base direction, within its resolution, and nothing else. Two paths in the canonical total space that end at terminal points projecting to the same base point, and arrive with directions whose base projections lie within the detector's resolution, **cannot be distinguished by the detector.** They contribute to one amplitude.

**Why it is a theorem [D].** A fiber datum is, by definition of the quotient, invariant under the fiber action, hence not a function on the base, hence not recordable. The fiber is unresolvable because the base is a quotient — the same fact that makes gravity blind to it.

**What a detector sees [V].** For a field of fiber charge $n$, terminal points separated by $\Delta$ contribute $e^{in\Delta}$, and $\int_0^{2\pi}e^{in\Delta}d\Delta = 2\pi\delta_{n0}$. Zero modes add coherently; charged modes average to zero — invisible, not decohered. **"The base sees zero modes" is what a base detector can register, not an assumption about matter.**

**The twist, through paths [T].** Two base paths enclosing $\Sigma$ arrive with fiber phases differing by $n\int_\Sigma F$; the detector cannot resolve the fiber velocities that would distinguish them; they interfere, and the fringe shifts by the flux. This is the Aharonov–Bohm effect. For the photon $n = 0$, and there is no fringe.

## X.2 The twin, and why it is unobserved [V/D]

The seed is as stated in §I.3: matter at $\hat n$, a gravitational well at both $\pm\hat n$, and **nothing at $-\hat n$**. No selection rule on light is invoked, and none is needed.

Two facts make the twin unobservable, independently of each other and of any reading.

**It is empty.** There is no matter there to emit, absorb or scatter. Light passes through the twin's well lensed and unobstructed (§V.8).

**And its light could not have reached us in any case.** Light takes $\pi\ell/c$ to cross to the antipode, which at $\ell = 63$ Gpc is **646 Gyr** — forty-seven times the age of the universe. Even matter placed there would be unobserved for this reason alone.

*Version 11 explored a reading in which matter sits at both twins and light reaches only its own chirality sheet, requiring a sheet-selective coupling that was never derived and that faced an eleven-order atomic-parity bound in its natural form. That construction is set aside in §XII.1; version 12 keeps the empty twin, which needs no new coupling and no new law.*

# PART XI — TWO TESTS

## XI.1 The golf ball [V/D]

A golf ball hovering in a vacuum chamber on Earth's surface: does it enclose its own fibers?

**Topologically, yes.** Law III is linear, $F = F_\oplus + F_g$, and for a small sphere around the ball $\frac{1}{2\pi}\int F = M_g/m_{\rm unit}$ exactly. Chern numbers add and are localized; Earth cannot smear away an integer.

**Geometrically, Earth dominates.** The flux falls as $N/2r^2$ — the same law as gravity — and the ball's field exceeds Earth's only inside $r = R_\oplus\sqrt{M_g/M_\oplus} = 0.56\,\mu$m, which is precisely the ball's gravitational neutral point, since both fields are sourced by mass with the same falloff.

**The quantization fork decides whether there is any winding.** With $m_{\rm unit} = m_p$ the ball winds $2.7\times10^{25}$ times and Earth $3.6\times10^{51}$; with $m_{\rm unit}\sim10^{14}M_\odot$ both wind zero times and the second order is absent from the solar system.

A spherically symmetric chamber contributes nothing inside, by the shell theorem, which applies because the flux obeys an inverse-square law. And nothing in the laboratory detects either answer: the photon is Hopf-neutral.

## XI.2 The Machian direction [T/D/V]

*The proposal: a body fully enclosing its own fibers should be a rescaled copy of any other such body, so an isolated golf ball would have Earth's compactness while one near Earth has general relativity's, with the Newtonian force invariant.*

**What is already true.** Vacuum general relativity has the symmetry $(g,M)\to(\lambda^2g,\lambda M)$: every Schwarzschild exterior *is* a rescaled copy of every other, with mass as the scale. The Hopf bundle is one universal object with $N = M/m_{\rm unit}$ as its only body-dependent datum. So "isomorphic fibers up to scale" is true and yields nothing new — the scale it fixes is mass, not size, and compactness $r_s/R$ ($1.4\times10^{-9}$ for Earth, $3.2\times10^{-27}$ for a golf ball) is untouched.

**The proposal as stated is inconsistent [D].** Giving the isolated ball Earth's compactness means $r_s\to4\times10^{17}r_s$ with $GM$ fixed. But $r_s = 2GM/c^2$: horizon and Newtonian coupling are **one number** whenever the exterior has a single source. Separating them requires the near field to be sourced by something the far field does not see.

**The realizable form is already present [D].** Law III's flux is such a second source (§V.6). And the flux energy $|F_\oplus + F_g|^2$ contains a **cross term** $2F_\oplus\cdot F_g$ — a source at the ball that exists only when Earth is present, $1.5\times10^9$ times the ball's own term at its surface. In isolation only the self term survives. **The ball's near field genuinely differs alone and near Earth — a Machian effect from the dynamic sector with no new law**, bounded by Mercury at $\delta r_s/r_s < 3\times10^{-4}$.

**A local Mach relation fails [V].** Reading $GM/c^2\ell = \pi/2$ with $\ell$ a body's sphere of influence gives $5\times10^{11}G$ for Earth and $3\times10^{22}G$ for the golf ball. The Mach relation closes a *universe*; spheres of influence are not closed universes.

**Emergent $G$ [D].** $G$ is emergent if and only if mass has a $G$-free definition. General relativity has none — ADM and Komar masses are defined *through* $G$. The Hamiltonian constraint $H^2 = \tfrac{8\pi G}{3}\rho - \tfrac{1}{a^2} + \tfrac{\Lambda}{3}$ holds on every slice of every spacetime and is the invariant extending beyond the static case, but it constrains the product $G\rho$ and cannot separate the factors. The only $G$-free mass the program has produced is the fiber momentum $p_u = m$ of the null-fiber reading, set aside in this version. **On a spacelike $u$, $G$ is a constant constrained by closure, and emergence is not available.**

---

# PART XII — SET ASIDE, RETIRED, OPEN

## XII.1 Set aside: recorded, not assumed

**Self-dual 2-form electromagnetism (version 11's Law IV).** On a six-dimensional Lorentzian space a 2-form $B$ with $H = dB = \star_6H$ is *chiral*: six dimensions is the unique place a gauge field can be, since self-duality needs middle degree and $\star^2 = +1$. Its dynamics is first order — self-duality *is* the field equation, as for a Weyl spinor — with no simple covariant action, since the naive $-\tfrac12\int H\wedge\star H$ vanishes identically on self-dual configurations. Reducing on the two fiber directions gives one photon plus one shift-symmetric scalar, with both Maxwell equations descending as Bianchi identities of $A$ and its magnetic dual. Charge would be carried by strings winding a cycle, or by the graviphoton, or by a separately specified $U(1)$; none was forced. **Set aside because its purpose — giving light an even chirality for the involution to flip — served a reading of the seed that this version does not take.** Coherent, and restorable.

**The chirality-selective visible space (version 11's Part IX).** Matter at both twins, with light of one chirality reaching only its own sheet, so that gravity sees all the matter and light half of it. Built relationally, by lifting light paths from a source, since no global sheet label exists ($E\to E/\sigma$ is a connected double cover). **Set aside because its coupling rule was never derived**: a handedness-based version is excluded by atomic parity violation at eleven orders, and a sheet-based version needs a label that survives the $8\times10^{20}$ Hz chirality oscillation of a massive fermion. The empty twin of §X.2 needs no such rule.

**From versions 7 through 9.**

The null fiber and its Bondi reading; the Eisenhart–Bargmann lift and the identification of the fiber coordinate with the classical action; the Lorentzian real slice of the complexified cover and its de Sitter geometry; the fiber as quantum phase; Law I as semiclassical; the twin as a superposition branch; the fiber product as "visual space." Each is a coherent branch; none is part of version 11.

## XII.2 Retired, with reasons

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
| "northern light / southern light" | the twin map fixes the poles, and no global sheet label exists (§X.2) |
| the Machian rescaling as stated | inconsistent (§X.2) |
| the Kerr source pictured as a 2-sphere in $S^4$ | that 2-sphere is the projection of a tilted twistor line, a different object from the ring, with no relation established (§IX.4) |
| the Hopf circle as a **primitive** | it was a gesture at a structure not yet identified. It is now derived: the twistor fiber's rotation subgroup about a section (§III.1) |
| **time as the twistor fiber's latitude** (version 12) | a type error: a complex structure has $J^2 = -1$, so no real eigenvectors — it *pairs* directions where time must *select* one (§IX.6) |
| Wick-rotating $\chi$ to get time | $\chi$ is exactly what the meridian quotient removes; saving it would gut the seed (§IX.6) |
| the ray$\to$line circle of $S^7\to\mathbb{CP}^3$ as time | time must be a line; that fiber is a circle. Circular gives closed timelike curves, unwrapping trivializes the twist (§IX.6) |
| $N\Omega = 1$ as an **exact** condition | it parts from Schwarzschild at $O(m^2/r^2)$, and imposing it exactly gives Majumdar–Papapetrou — every body extremally charged. The fiber-length reading is weak-field (§V.3) |
| poles assigned by hand at fixed coordinates | replaced by the Machian axis (§II.4): the poles follow the matter's principal axis |
| $v^2_{\rm eq} = 4GM/\pi\ell$ | $15\%$ low; the converged value is $1.497\,GM/\ell$ (§V.8) |
| "Law II's static presentation is a gauge choice" | too strong: Law II is elliptic on slices, hence instantaneous and frame-preferring; canonical only on static solutions (§II.3) |

| self-dual 2-form electromagnetism, and charge as winding | set aside (§XII.1), not refuted: the incentive was a chirality-selective seed that this version does not pursue |
| the chirality-selective visible space | set aside (§XII.1): its coupling rule was never derived, and the natural form died to atomic parity violation at $10^{11}$ |

## XII.3 Open

1. **The four unassigned connection components** (§III.5) — the tilt field, where Kerr's $a$ lives. No law sources them, and the natural candidate, angular momentum, already sits in the shift inside the base metric. **The sharpest problem this version creates**, and the first thing a version 14 owes.
2. **The locking $\lambda = \Omega\lambda^{\rm ref}$** (§V.3). Twistor space is conformally invariant, so the fiber radius is extra data; the canonical twistor metric would fix it by the scalar curvature and give no wells. Whether anything selects the locking is open.
3. **Time.** Still an input; version 12's attempt is retracted on grounds of type (§IX.6), and both repairs tried fail for stated reasons.
4. **Even flux.** Two independent routes force an even Chern number (§III.1, §IX.1). Whether that constrains $m_{\rm unit}$, constrains the admissible masses, or signals a mismatch, is open.
5. **The meridian scale $\kappa$** (§V.4), inherited unfixed.
6. **Anomalies:** whether the six-dimensional Weyl fermions cancel their own (§IV.7).
7. **The Pin structure:** which of Pin$^\pm$ the fermionic base admits.
8. **The quantization fork:** $m_{\rm unit}$ a particle mass or $\sim10^{14}M_\odot$.
9. **$g_2/m_{\rm unit}$:** below $0.024$ from Mercury.
10. **$\mu(\rho)$:** nothing selects it.
11. **Twin parity assignments:** which species are twin-odd.
12. **Emergent $G$:** requires a $G$-free definition of mass (§XI.2).
13. **Law II in dynamical settings** (§II.3); **the swinging axis** (§II.4).
14. **Inherited:** the AdS uplift; the two arenas; the literature review.

---

## Reference card, version 11

| topic | statement |
|:--|:--|
| **canonical total space** | $\mathbb{PT}^*$, 6-D: twistor space of $S^4$ with two sections removed; fibers $\mathbb{C}^* = S^1\times\mathbb{R}$ |
| **time** | an input, a factor $\mathbb{R}_t$, as in versions 6–11. The complex layer supplies none (§IX.6) |
| **tower** | $\mathbb{R}_t\times\mathbb{CP}^3\,(7)\to\mathbb{R}_t\times S^4\,(5)\to\mathbb{R}_t\times\mathbb{RP}^3\,(4)$; the meridian quotient is the seed |
| **the fiber** | the **twistor 2-sphere**: complex structures on $T_xS^4$. Tangent-space data attached pointwise — **not a lifted shell** |
| **Law III derived** | a 2-sphere has $SO(3)$; a $U(1)$ appears once a **section** is chosen, and sections exist over the cover minus the meridians. The Hopf circle is the fiber's rotation subgroup, not an input |
| **Law I on the fiber** | $\lambda = \Omega\lambda^{\rm ref}$: a sphere's **radius** where a circle had a length. Area $\propto\phi^4$. Posited, since twistor space is conformally invariant |
| **partition** | $21 = 10+3+8$. Fiber $3\to1$ by roundness, matching Law I. Connection $8 = 4$ (Law III) $+\,4$ (**the tilt field, unassigned**) — it no longer closes |
| **ray–line principle** | gravity reads the fiber of rays $\to$ lines: $\mathbb{Z}_2$ over $\mathbb{R}$ (**the twin**), $U(1)$ over $\mathbb{C}$ (**the Hopf charge**). One blindness, two fields, nested |
| **parity theorem** | the seed's base is real projective *because space is odd-dimensional*; $\mathbb{CP}^n$ is always even |

| **even Chern number** | two routes give 2: $\mathbb{RP}^3\to S^2$ has $c_1 = 2$ (§IX.1), and the twistor splitting gives $c = -2a$ (§IX.4) |
| **ASD law** | Penrose–Ward: anti-self-dual solutions $=$ holomorphic data on twistor space. Native here |
| **Kerr** | the source's position gains an **imaginary part**, a *vector*: direction $=$ spin axis, magnitude $= a = J/M$. Equivalently its twistor line comes off **vertical** — and since the twistor fiber is now the arena's own, **the tilt is in the canonical total space** (§IX.4) |
| **rotation as misalignment** | Schwarzschild's line **is** a fiber (vertical); Kerr's is **tilted**, by $a$. One fibration, one misalignment |
| **where the shift happens** | in the complexification of $S^4$. Two different 6-D spaces sit over $S^4$: circle fibers (Law III) and sphere fibers (Penrose–Ward) |
| **what the complex structure earns** | rotation read geometrically, and Law III derived; the ray–line unification and parity theorem framed; Penrose–Ward idle; time not at all; and one new debt, the unclosed partition (§IX.5) |
| **Kerr, in six steps** | Kerr–Schild form $\to$ one harmonic function $\to$ displace $z\to z-ia$ $\to$ the singularity becomes a **ring** of radius $a$ $\to$ oblate slice gives $H = MR^3/(R^4+a^2z^2)$ $\to$ $J = Ma$. **Rotation is a position in the complexification** (§IX.2) |
| **gravity base** | $\mathbb{RP}^3$, 3-D; Law I, with time restored from the fiber |
| **fermionic base** | $\mathbb{PT}^*/\sigma$, 6-D; an identification, non-orientable |
| **arena** | primary at the south pole, forced by $\chi(S^4) = 2$; latitudes the level sets |
| **Law I** | $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T^+_{\mu\nu}$, $\Lambda = 1/\ell^2$; $\gamma = 1$ trivially |
| **Law II** | $\nabla\cdot(\mu\nabla\Phi_u) = M_{\rm tot}[\delta(\hat d)-\delta(-\hat d)]$; poles at the matter's principal axis; weaves, never captures |
| **Machian axis** | poles at $\pm\hat d$; flux strength is normalization only; no mass threshold; secondary tilts the axis by $O(M_s/M_p)$ |
| **equal masses at poles** | both are jellium; the base is homogeneous; the primary/secondary distinction dissolves |
| **$n$ masses** | the axis points at the centroid direction, generically empty: **all are secondaries, none is primary**. A pole is occupied only as $m/M\to0$ |
| **what a pole is** | the fibration's degeneracy — a geometric feature matter locates but need not occupy |
| **masses refract** | $n$ masses give $n$ refraction centers and still exactly **two** singularities; lines bend in and out, never terminate |
| **Keplerian limit** | $\Phi = -Gm/r[1 + r^2/6\ell^2]$; corrections $4\times10^{-15}$ at 10 kpc; jellium crossover at 1.2 Mpc for a galaxy |
| **$v^2$ plateau** | $v^2_{\rm eq} = 1.497\,GM/\ell$, packing-independent; $f\to1$ gives $r_s = \pi\ell$ and no exterior |
| **two fluxes** | fibration flux $\to$ uniform (jellium); second-order flux $\to$ localized ($P^2/r^2$). Same Gauss law, different spread |
| **Mach as horizon** | $r_s(M_{\rm tot}) = \pi\ell$, the antipodal distance |
| **Law III** | $dF = 2\pi\star J_-$; $L_E = \Omega L^{\rm ref}$; kinematic |
| **Law IV** | Maxwell 1-form on the cover, $\epsilon\mu = 1$; photon Hopf-neutral; total charge zero; light's chirality is the complex split $\mathcal{F}^\pm$ |




| **what each law is** | I: Einstein on the base, dynamical, from $T_+$. II: the meridians, kinematic, poles only. III: the connection, kinematic, from $J_-$. IV: Maxwell on the cover. Table at §II.0 |
| **$G$ identity** | $GM_{\rm tot}/c^2\ell = \pi/2$: from Law I and closure alone; untouched by the Machian form |
| **twin theorem** | $(\Delta+3)$; dipole kernel; a lone mass has no static solution |
| **shells** | proper area $4\pi r^2(1+GM/2r)^4$; fiber circumference $2\pi\phi^2$, longest deepest in the well |
| **fiber reading** | $\delta L/L = -\Phi$; $E_{ij} = -2[\nabla\nabla\phi]^{\rm TF}$; PNDs along $\nabla L$ |
| **black holes** | $f = 1 - 2GM/c^2r + GP^2/c^4r^2$, $P = g_2M/m_{\rm unit}$; $M^2\ge Q^2+P^2$; Mercury: $P/M<0.024$ |
| **partition** | $21 = 10 + 3 + 8$ for the 2-D fiber. Fiber metric $3\to1$ by area-preservation and diagonality, matching Law I's one function. Connection $8 = 4$ (Law III's $\alpha$) $+\,4$ (**the shift** $\beta$: frame dragging now inside the fiber) |
| **the involution** | $\sigma:(\chi,\hat n,\theta)\mapsto(\chi,-\hat n,-\theta)$; det $=-1$; twin makes it free, reflection makes it reversing |
| **what $\sigma$ is** | one map flipping odd chirality, even chirality, and the second-order charge |
| **Dirac from Weyl** | chiral halves at twin points; mass is the twin coupling, local downstairs |
| **why Weyl** | 6-D Weyl $=$ 4 complex $=$ 8 real $=$ exactly one 4-D Dirac; no phantom duplicate |




| **detection** | which-path is base-only; zero modes add; $n\neq0$ invisible; Aharonov–Bohm through paths |


| **the seed** | matter at $\hat n$, a well at both $\pm\hat n$, **nothing at $-\hat n$**; the twin is empty, and its light could not have arrived anyway ($646$ Gyr) |
| **golf ball** | winds $M_g/m_{\rm unit}$ times; Earth dominates beyond $0.56\,\mu$m |
| **Machian** | literal form inconsistent; the cross term is the realizable form, $<3\times10^{-4}$ |
| **emergent $G$** | requires $G$-free mass; only the set-aside null fiber supplies one |
| **regardless** | $\pi\ell/c = 646$ Gyr: the twin is unobserved either way |
