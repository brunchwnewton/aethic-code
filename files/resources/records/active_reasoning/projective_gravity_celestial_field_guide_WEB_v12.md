# Projective Gravity — Version 12

### The Complexified Arena: twistor space, and time as latitude

> **What this document is.** A complete, self-contained statement of the theory: arena, laws, identities, the spinor sector, the electromagnetic sector, and the construction of visible space. It assumes no earlier document. Every term is defined in Part 0; every law is stated with its equation; every result imported from an earlier version is restated in full rather than cited.
>
> **What is new relative to version 11.** The arena is complexified, and time stops being an input. Version 11's canonical total space was $\mathbb{R}_t\times E$: an external time factor times a circle bundle over the 4-sphere. Version 12 replaces both with a single object — **the twistor space of the 4-sphere, with two sections removed.** Its fibers are cylinders $\mathbb{C}^* = S^1\times\mathbb{R}$, and the two directions of that cylinder are the Hopf circle and time. Nothing is deleted: the same six directions appear, packaged as one structure instead of two, and the 4-sphere with its meridians is the *base* of the fibration, untouched.
>
> Three things follow. **(1) Time is emergent and geometric:** the twistor fiber over a point is its sphere of compatible complex structures, and time is *latitude* on that sphere, running from a distinguished complex structure to its conjugate. **(2) The anti-self-dual law is native:** the Penrose–Ward correspondence makes anti-self-dual solutions equivalent to holomorphic data on twistor space, and the Kerr metric becomes the real slice of a point mass displaced along a *complex worldline*. **(3) The surgery pays twice:** removing the two sections is what turns the fibers into cylinders *and* what permits a Lorentzian metric at all, since $\chi(\mathbb{CP}^3) = 4\neq0$ forbids one on the compact space.
>
> **Two reversions, in the interest of staying conservative.** Version 11's self-dual 2-form electromagnetism and its chirality-selective reading of the twin are both **set aside** (§XII.1). Electromagnetism returns to an ordinary Maxwell 1-form, and the twin returns to being **empty of matter**, as in every version before 11. Neither was forced; both were introduced to support a quantum-flavoured programme that this version does not pursue, and the incentive for them went with it. They remain coherent alternatives and can be restored if a later version needs them.
>
> **Carried unchanged from version 11.** The fermionic base and its involution; every law, theorem and identity of the gravity base; the base-resolution principle.
>
> **Tags.** **[V]** verified by computation · **[T]** cited theorem · **[D]** derived here · **[S]** sketch · **[O]** open · **[R]** retired, with reason.

---

# PART 0 — VOCABULARY AND CONVENTIONS

## 0.1 The spaces

| term | definition | dim | role |
|:--|:--|:--:|:--|
| **canonical total space** $\mathbb{PT}^*$ | the twistor space $\mathbb{CP}^3$ of $S^4$ with two sections removed, restricted over $S^4$ minus the secondary meridians. Fibers are cylinders $\mathbb{C}^* = S^1\times\mathbb{R}$ | 6 | where the full structure lives |
| **cover** | $S^4$: the canonical total space with the twistor fibers quotiented away. Where matter and light live | 4 | matter, light |
| **gravity base** | $\mathbb{RP}^3$: the space of meridians. Where gravity lives; time is restored from the fiber | 3 | Law I |
| **fermionic base** | $\mathbb{PT}^*/\sigma$: the canonical total space modulo the involution of Part VI. Not a reduction — an identification | 6 | where a Dirac spinor is one local object |
| **twistor fiber** | over $x\in S^4$, the sphere $\mathbb{CP}^1$ of complex structures compatible with the metric and orientation at $x$, minus two antipodal points | 2 | supplies the Hopf circle and time |
| **the removed pair** | at each point a complex structure $J$ and its conjugate $-J$. Their removal makes the fiber a cylinder *and* makes a Lorentzian metric possible | — | §I.2 |

The unqualified phrase "total space" is retired in favor of *canonical total space*. The fibration tower is

$$\mathbb{PT}^*\ (6)\ \longrightarrow\ S^4\ (4)\ \longrightarrow\ \mathbb{RP}^3\ (3)$$

the first arrow a quotient by the cylinder fiber, the second by the meridians. **Time is not a factor of the tower — it is one of the two fiber directions of the first arrow** (§I.2), restored whenever a four-dimensional spacetime is wanted below. The fermionic base sits off this tower, mapping from the canonical total space and onto the gravity base.

The six directions, and where each lives:

| direction | count | where |
|:--|:--:|:--|
| gravity base $\mathbb{RP}^3$ | 3 | the bottom of the tower |
| meridian $u$ | 1 | in $S^4$, fibered over $\mathbb{RP}^3$ |
| Hopf angle $\theta$ | 1 | the **angular** direction of the twistor fiber |
| time $t$ | 1 | the **radial** direction of the twistor fiber |

Version 11 had the same six, with time an external factor and the Hopf circle a separate bundle. Version 12 packages the last two as one cylinder. **Nothing is added and nothing is deleted.**

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
| **Hopf circles** | fibers of $E\to S^4$: one circle over each point of the cover | **no** — two points of one Hopf circle lie over the *same* point of the cover |

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

The cover is $S^4$, with the primary at one pole of the fibration and its antipode at the other. Matter and light live here; gravity does not. Time is not part of the cover — it is supplied by the twistor fiber above it (§I.2).

**The primary is compulsory.** Poincaré–Hopf: any vector field on $S^4$ has zeros of total index $\chi(S^4) = 2$, and a gradient flow with one source and one sink has index $(+1)+(+1) = 2$ — the minimum. So the fibration *must* degenerate at exactly two points, and the central mass sits at one of them. On $S^1\times S^3$ (Euler characteristic zero) a center is optional; on $S^4$ it is forced.

## I.2 The complexified arena: twistor space, and where time comes from [T/D]

**The twistor fibration.** The complexification of the arena carries a *holomorphic* metric — complex-bilinear, with no conjugation in it — so it is neither Riemannian nor Lorentzian. Those are its **real slices**, the fixed sets of antiholomorphic involutions, and $S^4$ is the Euclidean one. Attached to $S^4$ canonically, with nothing chosen, is its **twistor space**

$$\mathbb{CP}^3\ \longrightarrow\ S^4 = \mathbb{HP}^1,\qquad\text{fiber } \mathbb{CP}^1 = S^2$$

Over a point $x$, the fiber is the **sphere of complex structures** compatible with the metric and orientation at $x$ — equivalently the sphere of anti-self-dual null directions, the Euclidean celestial sphere of that point. $\mathbb{CP}^3$ is six real dimensions.

**Remove two points from each fiber.** Take a complex structure $J$ and its conjugate $-J$, antipodal on the fiber, and delete them. What remains is $\mathbb{CP}^1\setminus\{2\text{ pts}\} = \mathbb{C}^* = S^1\times\mathbb{R}$. Writing the stereographic coordinate as $\zeta = e^{\rho + i\phi}$:

$$\phi\in S^1:\ \text{rotation about the }J\text{-axis}\ \longrightarrow\ \textbf{the Hopf circle}$$
$$\rho\in\mathbb{R}:\ \text{latitude, from }J\text{ to }-J\ \longrightarrow\ \textbf{time}$$

> **Time is latitude on the sphere of complex structures**, running from one distinguished complex structure to its conjugate, infinitely far in each direction. It is not an added real line; it is the radial direction of a fiber the arena already carries.

Write $\mathbb{PT}^*$ for the result. The picture: *meridians against a 3-sphere, with a cylinder of complex structures erected over every point — its angle the Hopf phase, its height the time.*

## I.3 The surgery is required twice [T/V]

Removing the two sections is not a convenience. It is forced, independently, by two things.

**(i) To make the fibers cylinders.** Only then do the Hopf circle and time appear, as §I.2.

**(ii) To permit a Lorentzian metric at all.** A *compact* manifold admits a Lorentzian metric if and only if its Euler characteristic vanishes. Since $\chi(\mathbb{CP}^n) = n+1$, we have $\chi(\mathbb{CP}^3) = 4\neq0$: **$\mathbb{CP}^3$ admits no Lorentzian metric whatever.** Removing the sections makes it non-compact, and every non-compact manifold admits one. The requirement is not a technicality imported from a field equation: **time is one of the fiber's two directions (§I.2), and it must be timelike.** Without the surgery the arena cannot carry time at all.

## I.4 The sections exist, and the linking is even [T/V]

**The obstruction on the whole sphere.** Two *global* sections of $\mathbb{CP}^3\to S^4$ do not exist: a section is an almost complex structure, and $S^4$ admits none — an almost complex 4-manifold needs $c_1^2 = 2\chi+3\sigma = 4$, but $H^2(S^4) = 0$ forces $c_1 = 0$.

**But the arena is not the whole sphere, and there the sections exist [T].** Write $\mathbb{CP}^3 = \mathbb{P}(S^-)$, the projectivization of the negative spinor bundle. Removing two sections requires $S^-$ to split as a sum of line bundles $L_1\oplus L_2$. Over all of $S^4$ a split would force $c_2 = c_1(L_1)c_1(L_2) = 0$, against $c_2(S^-) = 1$ — no split. But the arena is $S^4$ minus the secondary meridians, and

$$S^4\setminus\text{circle}\ \simeq\ S^2$$

over which **every** rank-2 complex bundle splits. **So the sections exist, and the meridian removal already demanded by Law III is exactly the surgery that supplies them.**

**The price: the linking number is even [V].** With $c_1(S^-) = 0$ the splitting needs $c_1(L_2) = -c_1(L_1) = -a$, and the cylinder's circle bundle is $\mathrm{Hom}(L_1,L_2) = L_1^*\otimes L_2$, whose Chern number is

$$c = c_1(L_2) - c_1(L_1) = -2a \qquad\textbf{always even}$$

There is no natural square root: the fiber coordinate $\zeta = w_2/w_1$ *is* a section of $L_1^*\otimes L_2$, and there is nothing to halve. Restricted to a shell — a 2-sphere linking the secondary's meridian once — the total space is therefore the lens space $L(|c|,1)$, with fibers linking $|c|$ times:

| $c$ | total space over a shell | fibers link |
|:--:|:--|:--:|
| $1$ | $S^3$ — the genuine Hopf fibration | 1 |
| $2$ | $L(2,1) = \mathbb{RP}^3$ | 2 |
| $3$ | $L(3,1)$ | 3 |

> **The fibers do link, so the structure is Hopf-*like*; but the minimal case here is linking 2, not 1.** Consequently **Law III's Chern number $M_-/m_{\rm unit}$ must be even** — the same parity that decides the spin-structure count of §VII.1. Two independent structures imposing one condition **[D]**.

**Still assumed [O].** A Lorentzian metric is *admitted* by non-compactness, but none has been constructed; whether a natural one exists with the fiber's radial direction timelike is open.

## I.5 The quotient, the base, and the seed [D]

The gravity base is the space of meridians, $\mathbb{RP}^3$. Each of its points is one great circle through both poles, crossing the equator at $\pm\hat n$. Gravity is defined on $\mathbb{R}_t\times\mathbb{RP}^3$ and reads the fiber average — the integral of the cover's stress-energy along the meridian — which includes both twins by construction.

> **The seed.** Matter at $(\chi_0,\hat n)$ sources the gravity base at $[\hat n]$, whose lift to the cover has wells at both $\hat n$ and $-\hat n$. **Nothing is at $-\hat n$.** Blindness to which ray, not crossing between them.

**This is derived, not postulated:** a great circle through the poles crosses the equator twice. The projective postulate of the earliest versions is a theorem of the arena. 

## I.6 The primary is the jellium [D]

Both poles lie on **every** meridian, so $M_c$ contributes equally to every fiber average: seen from the gravity base it is uniform. The uniform background density of the Einstein static universe is the primary's column density, with value fixed by closure (§V.2).

## I.7 The three spaces, related [D]

Since $\sigma$ (Part VI) descends to the twin map on $S^4$, and the gravity base already identifies $\hat n$ with $-\hat n$, the fermionic base also maps onto the gravity base. The three form a commuting triangle with the canonical total space at the apex. **The fermionic base is not a dimensional reduction:** $\sigma$ is a free involution, so $E/\sigma$ has the same dimension as $E$; they differ in global structure, not size.

---

# PART II — THE LAWS

> ### ◆ LAW I — GRAVITY
> $$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi\,T^+_{\mu\nu}\quad\text{on }\mathbb{RP}^3\times\mathbb{R}_t,\qquad \Lambda = 1/\ell^2$$
> where the time factor is **restored from the twistor fiber's radial direction** (§I.2), not posited.
> General relativity on the gravity base, sourced by the meridian-averaged, pair-summed stress-energy. There is no dilaton, no radion, and no extra scalar with a $1/r$ coupling, so PPN $\gamma = 1$ holds trivially.

> ### ◆ LAW II — THE FIBRATION (MACHIAN FORM)
> $$\nabla\cdot\big(\mu(\rho)\,\nabla\Phi_u\big) = M_{\rm tot}\,\big[\delta^4(\hat d) - \delta^4(-\hat d)\big]\quad\text{on }S^4$$
> The $u$-fibers are the gradient lines of $\Phi_u$. The two flux endpoints — **the poles** — sit at $\pm\hat d$, where $\hat d$ is the matter distribution's own principal axis: the direction of its dipole $d_A = \int\rho\,x_A\,dV$, or, where the dipole vanishes, the principal axis of its quadrupole. All other matter enters through the permeability $\mu(\rho)$. The fibration is **kinematic**: it has no action, and nothing couples to it dynamically.

**The poles are not an input.** Earlier versions placed them by hand. Here they are determined by the matter, which is what makes the arena Machian: *wherever matter is most concentrated, a pole sits there and at its antipode.* Since choosing the polar axis is the same act as choosing the twin map — the twin map is $-1$ on the 4-plane orthogonal to the axis — **the gravity base itself is determined by the matter distribution** (§II.4).

> ### ◆ LAW III — THE SECOND-ORDER CONNECTION
> $$dF = 2\pi\star J_-,\qquad J_- = \frac{\rho_-}{m_{\rm unit}}\ \text{smeared along the meridians},\qquad F = d\alpha$$
> $\alpha$ is a $U(1)$ connection on the **angular** direction of the twistor fiber over $S^4$; its circumference is locked to gravity by $L_E = \Omega L^{\rm ref}$. Kinematic.

> ### ◆ LAW IV — ELECTROMAGNETISM
> Maxwell on the cover: $\mathcal{F} = d\mathcal{A}$ with $\mathcal{A}$ a **1-form**, and $\epsilon = \mu_{\rm EM} = 1$. Light follows null geodesics; the photon is the zero mode on every fiber and couples to none of them. The cover is compact, so total charge on it is zero.

*Version 11 replaced this with a self-dual 2-form, in order to give light an "even chirality" that the involution could flip — machinery introduced to support a chirality-selective reading of the seed. That reading is set aside here (Part X), so the 1-form is restored. The 2-form remains a coherent alternative and is recorded in §XII.1.*

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

**Why the zeros must be antipodal.** The fibration must be preserved by the twin map, since that is the deck map of the gravity base. The twin map therefore permutes the zeros, and its fixed points on $S^4$ are exactly the two poles **[V]**. A source–sink pair placed at them lies on *every* meridian, which is why the poles project uniformly onto the base (§I.6) and the base stays smooth. Zeros *swapped* by the twin map would be a twin pair at one latitude — one point of the base, hence a singular point of it. Version 11 takes the first case.

**The three limits, verified [V]:**

| configuration | axis from | result |
|:--|:--|:--|
| one dominant mass at $p$ | dipole | axis points **at it**; the mass sits at a pole and its $S^4$-antipode is the empty pole |
| primary $+$ a $1\%$ secondary | dipole | axis tilts by $0.6°$, of order $M_s/M_p$; **the secondary stays at a latitude, acquires no axis, and captures no field lines** |
| two equal masses at $S^4$-antipodes | quadrupole | the dipole vanishes; the axis is their separation; **both masses sit at poles** |

**Mass confers no role.** There is no threshold anywhere in Law II: a secondary of any mass, up to and beyond the primary's, enters through $\mu$ and never sources. Growing it tilts the axis continuously, in proportion to its mass, and nothing else. **The small-secondary limit — Keplerian orbits with no capture — therefore holds at every mass ratio, not as an approximation but as a structural fact.**

**And the equal-mass limit dissolves the distinction entirely.** Matter at a pole projects *uniformly* onto the gravity base, because the poles lie on every meridian; that is the content of §I.3. So two equal masses at the two poles are **both jellium**: the base density is perfectly uniform, there are no lumps at all, the gravity base is the bare Einstein static universe, and there is no center of anything. Each mass has $GM/c^2\ell = \pi/4$ and $r_s = \pi\ell/2$, half the antipodal distance, so no horizon difficulty arises. **The primary/secondary distinction does not merely become symmetric — it disappears.**

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

**And the jellium does not require a primary.** Uniform base density needs uniformity over $\hat n$, and there are two ways to get it: matter **at a pole**, which lies on every meridian; or matter **spread evenly over a latitude**. The first is the special case; the second is what a realistic near-homogeneous universe does. So the smooth background survives with no primary at all, and closure still fixes the total at $\pi\ell/2$. This refines §I.5's identification of the primary with the jellium, which held for the single-mass configuration.

**The jellium/lump split is therefore a statement about position, not mass:** matter on every meridian (at a pole) or spread evenly over a latitude is jellium; matter concentrated at one $\hat n$ is a lump; closure fixes the sum at $\pi\ell/2$ (§V.2). The orbit parameter $f$ of §V.8 is exactly the lumped share.

**What the emergent-$G$ identity does with all this: nothing [D].** The relation $GM_{\rm tot}/c^2\ell = \pi/2$ follows from Law I and closure alone — the Einstein static universe requires $\bar\rho = 1/4\pi\ell^2$, hence a total of $\bar\rho\cdot2\pi^2\ell^3 = \pi\ell/2$. It never used Law II. **The Machian form leaves it untouched**, and when one mass dominates the theory is identical to the fixed-pole version in every respect.

**Cost, recorded [O].** A nearly homogeneous universe has a small dipole on a large total, and since the fibration's lines are independent of the flux magnitude, the axis is decided entirely by that small residual. As matter rearranges, the axis swings and the gravity base swings with it — so a body's twin would change over time. This touches the seed, the $r = 1/\sqrt2$ signpost, and the involution of Part VI, which is defined by the twin map. Not resolved here.

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

**Geometric.** A metric in coordinates adapted to a fibration splits into base, fiber, and connection, pointwise, with no remainder and no overlap. For the two-dimensional twistor fiber of version 12 the count is

| | | |
|:--|:--|--:|
| base metric on $S^4$ | $4\cdot5/2$ | 10 |
| fiber metric, $2\times2$ symmetric | $2\cdot3/2$ | 3 |
| connection: one 1-form per fiber direction | $2\times4$ | 8 |
| **total** | | **21** |

which is $6\cdot7/2$, the full count for a six-manifold **[V]**. Version 11's one-dimensional fiber gave $15 = 10+1+4$; the extra fiber direction adds two to the fiber metric and four to the connection, and **neither addition is spare**:

- **The fiber metric's three reduce to one.** Area-preservation (§V.3) fixes the determinant, and diagonality kills the $\phi$–$t$ cross term: $3-1-1 = 1$. One function, $\Omega$ — and Law I in the conformally-round sector determines exactly one function, $\phi$, with $\Omega = \phi^2$. **The counts match exactly**, so the fiber's shape is fully fixed by Law I and carries no independent information. *That is the precise sense in which the field equations see only the base: gravity determines the fiber and is not informed by it.* **[V/D]**
- **The connection's eight split as four and four.** The circle's 1-form is Law III's $\alpha$. **The time direction's 1-form $\beta$, appearing as $-\Omega^{-2}(dt+\beta)^2$, is the shift vector** — so frame dragging, rotation, and magnetic Weyl now live *inside* the fiber structure. Version 11 stated flatly that magnetic Weyl lives in the shift, "which no fiber carries"; the time fiber carries it, and it is the same slot the complex worldline of §IX.2 deforms **[D]**.

The older, one-dimensional form of the count, still valid level by level:

| level | total | base | length | connection |
|:--|--:|--:|--:|--:|
| Hopf $S^3$ over a shell | 6 | 3 | 1 | 2 |
| $E\to S^4$ | 15 | 10 | 1 | 4 |
| $S^4\setminus\{\text{poles}\}\to\mathbb{RP}^3$ | 10 | 6 | 1 | 3 |

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

## V.3 Law I on the fiber: an area-preserving squeeze [V/D]

Weak-field statics are conformally round, $g_3 = \phi^4g_{S^3}$, and the Hamiltonian constraint linearizes about the Einstein static universe to

$$(\Delta_{S^3} + 3)\,\delta\phi = -2\pi\,\delta\rho_+$$

— the twin-theorem operator, acting on the conformal factor. Write $\Omega\equiv\phi^2$.

**The fiber metric.** Version 11 recorded two separate facts: the Hopf length was $L_H = 2\pi\ell\Omega$, and the lapse obeyed $N\cdot L_H = $ constant. On the twistor cylinder these are **one** fact. Put on the fiber

$$ds^2_{\rm fiber} = \Omega^2\big(d\phi + \alpha\big)^2 - \Omega^{-2}\,dt^2$$

Then the longitude's circumference is $2\pi\Omega$ — the old $L_H$ — the lapse along the latitude is $\Omega^{-1}$, and their product is $2\pi$, **independent of $\Omega$** **[V]**.

> **Gravity acts on the fiber as an area-preserving squeeze: the circle stretches by $\Omega$, time contracts by $\Omega^{-1}$, and the cylinder's area element is untouched.**

So it is **not the longitude alone** that carries the gravitational field, and not the fiber uniformly either: the two directions carry it **oppositely**. "Space stretches as much as time slows" was version 11's way of saying this with the halves separated.

**The weak-field dictionary is unchanged.** $\delta L/L = \delta\Omega/\Omega = 2\delta\phi = -\Phi$, hence $\delta N/N = +\Phi$: ordinary gravitational redshift, now read off the same fiber as the length. For a ball with its twin, $\Omega = 2.017$ at the ball's center and identically at the empty twin, agreeing to $10^{-11}$ **[V]**.

## V.4 The metric, written out [V/D]

*The level of definiteness every law in this document is held to.*

**The six-dimensional line element**, in the conformally-round sector:

$$ds^2_6 = -\Omega^{-2}dt^2 + \Omega^2(d\phi+\alpha)^2 + \lambda^2du^2 + \phi^4g_{S^3}$$

with $\Omega = \phi^2$ from Law I, $\alpha$ the Law III connection (even Chern number, §I.4), $u$ the meridian and $\lambda$ its scale, and $g_{S^3}$ the round metric of the latitude.

**A secondary point mass.** Solve $(\Delta_{S^3}+3)\delta\phi = -2\pi\delta\rho_+$ for a point mass at $\chi = 0$ with its twin. Near the mass the Green's function goes as $1/\sin\chi$, so with $r = \ell\chi$

$$\phi = 1 + \frac{GM}{2r} + O(r^2/\ell^2)$$

— the isotropic Schwarzschild conformal factor. The four-dimensional part of the line element is then

$$ds^2_4 = -\left(\frac{1-GM/2r}{1+GM/2r}\right)^2dt^2 + \left(1+\frac{GM}{2r}\right)^4\big(dr^2 + r^2d\Omega_2^2\big)$$

**isotropic Schwarzschild exactly**, with the closed-universe corrections entering at $O(r^2/\ell^2)$ — $4\times10^{-15}$ at 10 kpc for $\ell = 63$ Gpc (§V.10).

**The shells, metrically.** A shell at coordinate radius $r$ has proper area

$$A = 4\pi r^2\left(1+\frac{GM}{2r}\right)^4$$

the standard areal radius. Over each shell sits the longitude circle bundle of §I.4, of even Chern number, with total space the lens space $L(|c|,1)$ and fiber circumference $2\pi\Omega = 2\pi\phi^2$ — longest where the shell is deepest in the well.

**What remains undetermined [O].** The meridian scale $\lambda$, inherited unfixed from version 11; and the Lorentzian metric's global existence (§I.4).

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

# PART IX — THE ANTI-SELF-DUAL LAW, AND KERR

*The twistor fibration is not decoration: it is the home of a correspondence that makes one chirality half of gravity into holomorphic data, and turns rotation into a displacement in imaginary space.*

## IX.1 The Penrose–Ward correspondence [T]

> **Anti-self-dual solutions on a four-manifold are equivalent to holomorphic data on its twistor space.**

For gauge fields this is Ward's construction; for gravity it is Penrose's *nonlinear graviton*. The content: the ASD half of a field, which in spacetime obeys a nonlinear equation, becomes on twistor space a purely complex-analytic object — a holomorphic vector bundle, or a deformation of the complex structure. Since the arena's twistor space is $\mathbb{CP}^3$ over $S^4$, and the theory's cover *is* $S^4$, this correspondence is native rather than imported.

It is also the reason the self-dual / anti-self-dual split keeps recurring. Version 12 now has three instances of one $\mathbb{Z}_2$, all exchanged by $\sigma$:

| sector | chirality | where it lives |
|:--|:--|:--|
| gravity | Weyl tensor $C^+$ / $C^-$ | the base; the ASD half is holomorphic on $\mathbb{PT}^*$ |
| light | $\mathcal{F}^\pm = \tfrac12(\mathcal{F}\mp i\star\mathcal{F})$ | Maxwell's **complex** self-dual split; the Newman–Penrose scalars (§VIII.3) |
| matter | $S^+$ / $S^-$ | Weyl spinors, Part VII |

## IX.2 Kerr from a complex worldline [T/V]

Take the Schwarzschild potential and displace the source into **imaginary** space:

$$\frac{1}{\sqrt{x^2+y^2+z^2}}\ \longrightarrow\ \frac{1}{\sqrt{x^2+y^2+(z-ia)^2}}$$

The real slice of the resulting field is exactly the **Kerr metric**, with $a = J/M$ the spin per unit mass. The complex distance vanishes where $z = 0$ and $x^2+y^2 = a^2$ — Kerr's **ring singularity**, verified **[V]** — and $a = 0$ recovers Schwarzschild. This is the Newman–Janis shift, and in the present arena it says:

> **A rotating body is a non-rotating body whose worldline has been displaced along an imaginary direction.** Rotation is not extra structure; it is a position in the complexification.

**Why it is an anti-self-dual statement.** The shift acts *holomorphically*, so it deforms one chirality half of the Weyl tensor and leaves the other alone. Kerr's Petrov type D is the real slice of a purely one-chirality complex field — the nonlinear graviton in its simplest instance.

**What it changes downstream [D].** Version 11's black-hole section (§V.6) treated rotation as untouched by the fiber structure, since magnetic Weyl lives in the shift vector. That remains true of the *base* reading. What is new is that rotation now has a home in the arena: the imaginary displacement is a displacement along the twistor fiber's own complex direction, whose real part is time and whose angular part is the Hopf phase. Whether the Kerr parameter $a$ is literally a displacement in that fiber — rather than an analogy — is the second thing this version owes **[O]**.

# PART X — DETECTION

## X.1 The base-resolution principle

> ### ◆ THE BASE-RESOLUTION PRINCIPLE
> A detector is a base object. It can record base position and base direction, within its resolution, and nothing else. Two paths in the canonical total space that end at terminal points projecting to the same base point, and arrive with directions whose base projections lie within the detector's resolution, **cannot be distinguished by the detector.** They contribute to one amplitude.

**Why it is a theorem [D].** A fiber datum is, by definition of the quotient, invariant under the fiber action, hence not a function on the base, hence not recordable. The fiber is unresolvable because the base is a quotient — the same fact that makes gravity blind to it.

**What a detector sees [V].** For a field of fiber charge $n$, terminal points separated by $\Delta$ contribute $e^{in\Delta}$, and $\int_0^{2\pi}e^{in\Delta}d\Delta = 2\pi\delta_{n0}$. Zero modes add coherently; charged modes average to zero — invisible, not decohered. **"The base sees zero modes" is what a base detector can register, not an assumption about matter.**

**The twist, through paths [T].** Two base paths enclosing $\Sigma$ arrive with fiber phases differing by $n\int_\Sigma F$; the detector cannot resolve the fiber velocities that would distinguish them; they interfere, and the fringe shifts by the flux. This is the Aharonov–Bohm effect. For the photon $n = 0$, and there is no fringe.

## X.2 The twin, and why it is unobserved [V/D]

The seed is as stated in §I.5: matter at $\hat n$, a gravitational well at both $\pm\hat n$, and **nothing at $-\hat n$**. No selection rule on light is invoked, and none is needed.

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
| poles assigned by hand at fixed coordinates | replaced by the Machian axis (§II.4): the poles follow the matter's principal axis |
| $v^2_{\rm eq} = 4GM/\pi\ell$ | $15\%$ low; the converged value is $1.497\,GM/\ell$ (§V.8) |
| "Law II's static presentation is a gauge choice" | too strong: Law II is elliptic on slices, hence instantaneous and frame-preferring; canonical only on static solutions (§II.3) |

| self-dual 2-form electromagnetism, and charge as winding | set aside (§XII.1), not refuted: the incentive was a chirality-selective seed that this version does not pursue |
| the chirality-selective visible space | set aside (§XII.1): its coupling rule was never derived, and the natural form died to atomic parity violation at $10^{11}$ |

## XII.3 Open

1. **Construct the Lorentzian metric** (§I.4). Non-compactness *admits* one; none has been written down, and whether a natural one exists with the fiber's radial direction timelike is the first thing version 12 owes. *(The section question of the first draft is settled affirmatively — §I.4.)*
2. **Even flux** (§I.4). The twistor identification forces $M_-/m_{\rm unit}$ to be even. Whether that constrains $m_{\rm unit}$, constrains the admissible masses, or signals that the two circle bundles should not be identified, is open.
3. **Is the Kerr parameter literally a fiber displacement?** (§IX.2) The complex worldline is a theorem; whether $a$ lives in the shift $\beta$ — the time fiber's own connection (§III.5) — rather than being an analogy, is open, and §III.5 makes it more promising than it looked.
4. **The meridian scale $\lambda$** (§V.4), inherited unfixed from version 11.
5. **Anomalies:** whether the six-dimensional Weyl fermions cancel their own (§IV.7).
6. **The Pin structure:** which of Pin$^\pm$ the fermionic base admits, and whether the choice is physical.
7. **The quantization fork:** $m_{\rm unit}$ a particle mass or $\sim10^{14}M_\odot$.
8. **$g_2/m_{\rm unit}$:** below $0.024$ from Mercury; the double pulsar can tighten it.
9. **$\mu(\rho)$:** nothing selects it; observable only through footprint dilation, bounded by 4.
10. **Twin parity assignments:** which species are twin-odd.
11. **Emergent $G$:** requires a $G$-free definition of mass (§XI.2).
12. **Law II in dynamical settings** (§II.3): a hyperbolic reformulation, or a proof that the constraint form gives a slicing-independent congruence.
13. **The swinging axis** (§II.4): a nearly homogeneous universe fixes the polar axis by a small residual, so the gravity base — and every body's twin — would drift as matter rearranges.
14. **Inherited:** the AdS uplift; the two arenas; the literature review.

*(Retired with the 2-form: the charge-carrier question, point charges as windings, and the joint anomaly condition. See §XII.1.)*

---

## Reference card, version 11

| topic | statement |
|:--|:--|
| **canonical total space** | $\mathbb{PT}^*$, 6-D: twistor space of $S^4$ with two sections removed; fibers $\mathbb{C}^* = S^1\times\mathbb{R}$ |
| **time** | the **radial** direction of the twistor fiber — latitude on the sphere of complex structures, from $J$ to $-J$. Emergent, not posited |
| **Hopf circle** | the **angular** direction of the same fiber |
| **tower** | $\mathbb{PT}^*(6)\to S^4(4)\to\mathbb{RP}^3(3)$; time is inside the first fiber |
| **the surgery** | removing two sections does two jobs: cylinder fibers, and a Lorentzian metric ($\chi(\mathbb{CP}^3) = 4\neq0$ forbids one on the compact space) |
| **sections exist** | over $S^4\setminus\Gamma\simeq S^2$ every rank-2 bundle splits, so $S^- = L_1\oplus L_2$: the meridian removal supplies them |
| **even linking** | the cylinder's circle bundle is $L_1^*\otimes L_2$ with $c = -2a$: fibers link an **even** number of times, so $M_-/m_{\rm unit}$ must be even |
| **ASD law** | Penrose–Ward: anti-self-dual solutions $=$ holomorphic data on twistor space. Native here |
| **Kerr** | the real slice of a mass on a **complex worldline**: $z\to z-ia$; ring singularity at $x^2+y^2 = a^2$; rotation is a position in the complexification |
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




| **$G$ identity** | $GM_{\rm tot}/c^2\ell = \pi/2$: from Law I and closure alone; untouched by the Machian form |
| **twin theorem** | $(\Delta+3)$; dipole kernel; a lone mass has no static solution |
| **Law I on the fiber** | $ds^2_{\rm fiber} = \Omega^2(d\phi+\alpha)^2 - \Omega^{-2}dt^2$: an **area-preserving squeeze**. Circumference $2\pi\Omega$, lapse $\Omega^{-1}$, product fixed. Both directions, oppositely |
| **the metric** | $ds^2_6 = -\Omega^{-2}dt^2 + \Omega^2(d\phi+\alpha)^2 + \lambda^2du^2 + \phi^4g_{S^3}$; near a mass, isotropic Schwarzschild exactly |
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
