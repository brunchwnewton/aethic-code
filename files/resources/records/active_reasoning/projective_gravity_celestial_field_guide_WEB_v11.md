# Projective Gravity — Version 11

### Three Spaces, and the Chirality of Light

> **What this version adds to version 10.** Three things, each following from the one before.
>
> **A third space.** Version 10 has a *canonical total space* carrying both fiber families and a *gravity base* obtained by quotienting both away. Version 11 adds a **fermionic base**, obtained from the same total space not by a fibration but by a free involution — the one the second order already supplies. Spinors on it are automatically Dirac spinors, with their two chiral halves at a point and at its twin.
>
> **A new form for electromagnetism.** On the canonical total space the electromagnetic field is not a 1-form but a **2-form with self-dual field strength**. Six dimensions is exactly where that is possible. Self-duality is a chirality for a boson: it exists upstairs, it is *consumed* in the reduction to four dimensions, and it is exchanged by the same involution that exchanges fermion chiralities. Electric charge becomes winding on the meridian; magnetic charge becomes winding on the Hopf circle; and a massless axion falls out for free without the fifth-force problem that plagued earlier versions' scalars.
>
> **A visible space.** With both matter and light carrying a chirality that the involution flips, the seed can be recovered *without* the twin being empty: matter is at both twins, but light of one chirality reaches only its own sheet. Part VI constructs this and states, precisely, the one thing it still needs.
>
> **Tags.** **[V]** verified by computation · **[T]** cited theorem · **[D]** derived here · **[S]** sketch · **[O]** open.

---

# PART 0 — VOCABULARY

Version 10's Part 0 stands. The terms this document adds or redefines:

| term | meaning |
|:--|:--|
| **canonical total space** | $\mathbb{R}_t\times E$, six-dimensional: time, the 4-sphere with its meridians, and the Hopf fibers. The *unqualified* phrase "total space" is retired in favor of this |
| **gravity base** | $\mathbb{R}_t\times\mathbb{RP}^3$, four-dimensional: both fiber families quotiented away. Where Law I acts |
| **fermionic base** | $\mathbb{R}_t\times E/\sigma$, six-dimensional: the canonical total space modulo the involution $\sigma$. Not a reduction — an identification |
| **the involution** $\sigma$ | $(\chi,\hat n,\theta)\mapsto(\chi,-\hat n,-\theta)$: go to the twin, conjugate the fiber |
| **odd chirality** | the ordinary chirality of a Weyl spinor: the eigenvalue of the Clifford volume element $\gamma_5$ |
| **even chirality** | the self-duality of a middle-degree form: whether $H = +\star H$ or $H = -\star H$. The bosonic analogue, existing only in the middle degree |
| **visible space** | not a fourth manifold: the canonical total space *with a basepoint*. Defined relative to a source event by lifting light paths (§VI.3) |
| **sheet** | one of the two meridian arcs over a gravity-base point; exchanged by $\sigma$. There is no global sheet label (§VI.2) — only a relative one, fixed by a source and a path |

Conventions as version 10. $B$ is the 2-form gauge field, $H = dB$ its 3-form strength, $\star$ the Hodge star of the canonical total space.

---

# PART I — THE THREE SPACES

## I.1 Definitions

| space | definition | dim | role |
|:--|:--|:--|:--|
| canonical total space | $\mathbb{R}_t\times E$, $E$ the Hopf bundle over $S^4$ minus the secondary meridians | 6 | where the full structure lives |
| gravity base | $\mathbb{R}_t\times\mathbb{RP}^3$ | 4 | Law I |
| fermionic base | $\mathbb{R}_t\times E/\sigma$ | 6 | where a Dirac spinor is one local object |

**The fermionic base is not a dimensional reduction.** $\sigma$ is a free involution, so $E/\sigma$ has the same dimension as $E$; the two differ in global structure, not size. Since $\sigma$ descends to the twin map on $S^4$, and the gravity base already identifies $\hat n$ with $-\hat n$, the fermionic base also maps to the gravity base. The three form a commuting triangle with the canonical total space at the apex.

## I.2 The two fibrations, restated

The distinction matters throughout and is easy to lose.

| fibration | fibers | pairs twins? |
|:--|:--|:--|
| **meridians** ($u$-fibers) | fibers of $S^4\to\mathbb{RP}^3$: great circles through both poles | **yes** — a meridian crosses the equator at $\hat n$ and at $-\hat n$ |
| **Hopf circles** | fibers of $E\to S^4$: one circle over each point of the cover | **no** — two points of one Hopf circle lie over the *same* point of the cover |

The twin comes from the meridians and from nothing else.

---

# PART II — THE INVOLUTION

## II.1 Definition [D]

$$\sigma:\ (\chi,\hat n,\theta)\ \longmapsto\ (\chi,\,-\hat n,\,-\theta)$$

**Go to the twin, and conjugate the fiber.** Both halves are already in the theory: the twin map is the seed's pairing, and the fiber conjugation is the statement — established by version 10's linking-number argument — that the twin carries the anti-monopole, $N\to-N$.

## II.2 Why this involution and no other [V]

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

The fiber half-turn deserves separate mention, since it is the natural rival. It is a rotation, not a reflection, so it preserves orientation; its quotient is an orientable circle bundle with doubled Chern number, keeping chirality and giving no Dirac structure. What it does give is a spin-structure choice sorting Hopf charges by parity — the same parity that decides $E$'s spin-structure count. A real $\mathbb{Z}_2$, a different one.

## II.3 What $\sigma$ is, in field-theory language [D]

$\sigma$ flips **odd chirality** (by reversing orientation), flips **even chirality** (same reason — the Hodge star's sign follows the orientation), and flips the Hopf charge $n\to-n$ (by conjugating the fiber). Flipping chirality and charge together is what charge conjugation does. So $\sigma$ is a geometric realization of $C$, and the long-standing statement "the twin carries the anti-monopole" is that same statement seen topologically.

> **One map exchanges the fermionic chirality, the bosonic chirality, and the sign of the second-order charge. They are three faces of orientation reversal.**

---

# PART III — THE FERMIONIC BASE

## III.1 Non-orientable, hence Pin, hence no chirality [T]

$\sigma$ is free and orientation-reversing, so $E/\sigma$ is **non-orientable**. The chirality operator on an even-dimensional manifold is the product of all the gamma matrices, and its sign depends on the orientation. A non-orientable space has no global orientation, hence **no global chirality operator**: it carries Pin structures rather than Spin structures, and a spinor field on it cannot be chirally projected. Equivalently, $\sigma_*$ maps $S^+$ to $S^-$, so a $\sigma$-equivariant field is of one chirality at a point and the other at its image.

## III.2 The result [D]

> **A Weyl spinor on the canonical total space is a Dirac spinor on the fermionic base, with its two chiral halves at a point and at its twin.**

The Dirac mass term is the only thing coupling the two chiralities:

$$\mathcal{L}_m = -m\big(\bar\psi_L\psi_R + \bar\psi_R\psi_L\big)$$

so mass becomes a coupling between a point and its twin — **local on the fermionic base, twin-connecting seen from the canonical total space.** The fermionic base is where fermion physics is ordinary; the hundred-gigaparsec separation is an artifact of describing it upstairs.

## III.3 The twin's field is not independent [D]

A field descending to $E/\sigma$ satisfies $\Psi(\sigma x) = \sigma_*\Psi(x)$: its value at the twin is *determined*. There are not two particles; there is one field whose left-handed description sits at $\hat n$ and whose right-handed description sits at $-\hat n$. Gravity therefore reads

$$T_+ = T(\hat n) + T(-\hat n) = T_L + T_R = \text{one Dirac field's full stress-energy}$$

**No doubling.** The two things at the two twins are two descriptions of one object.

---

# PART IV — ELECTROMAGNETISM ON THE CANONICAL TOTAL SPACE

*This part replaces version 10's Law IV. What is gained is stated in §IV.6; what must be rechecked, in §IV.7.*

## IV.1 Why a 2-form, and why six dimensions [T]

For spinors, chirality is the eigenvalue of the Clifford volume element. Tensors have no such operator — but **middle-degree forms have the Hodge star**, which plays the identical role: it squares to $\pm1$, and where it squares to $+1$ there is a real split into self-dual and anti-self-dual halves. The condition is $\star^2 = (-1)^{p(n-p)+t} = +1$ with $p = n/2$.

| field, dimension, signature | $\star^2$ | verdict |
|:--|:--:|:--|
| 4-D Lorentzian, 2-form $F$ | $-1$ | needs complexification: no real split |
| 6-D Euclidean, 3-form | $-1$ | no real split |
| **6-D Lorentzian, 3-form $H$** | $+1$ | **real self-dual / anti-self-dual split exists** |
| 6-D, 1-form $A$ | — | not middle degree: no self-duality in any dimension |

**Six-dimensional Lorentzian is exactly where a gauge field can be chiral** — and it is the dimension of the canonical total space. A 1-form, the photon as ordinarily written, can never carry this index, which is why the structure must be placed upstairs on a 2-form rather than attached to $A_\mu$.

## IV.2 Law IV′ [D]

> ### ◆ LAW IV′ — ELECTROMAGNETISM
> The electromagnetic field on the canonical total space is a 2-form gauge field $B_{MN}$ with 3-form strength $H = dB$, subject to self-duality:
> $$H = \star_6 H$$
> Its anti-self-dual partner $H = -\star_6H$ is the opposite even chirality, exchanged with it by $\sigma$.

## IV.3 The reduction: exactly one photon [T]

Decompose $B_{MN}$ on the two fiber directions, $u$ (meridian) and $\theta$ (Hopf):

| component | gives | dof |
|:--|:--|:--:|
| $B_{\mu\nu}$ | a 4-D 2-form, dual to a scalar | 1 |
| $B_{\mu u}$ | a 4-D vector $A_\mu$ — **the photon** | 2 |
| $B_{\mu\theta}$ | a 4-D vector $\tilde A_\mu$ — its magnetic dual | 2 |
| $B_{u\theta}$ | a 4-D pseudoscalar | 1 |

Unconstrained total: 6, which is $\binom{4}{2}$, the physical count of a six-dimensional 2-form **[V]**. Self-duality relates the $(\mu\nu u)$ and $(\mu\nu\theta)$ components of $H$:

$$H_{\mu\nu u} = \tfrac12\epsilon_{\mu\nu\rho\sigma}H^{\rho\sigma}{}_\theta\qquad\Longleftrightarrow\qquad F = \star_4\tilde F$$

so $\tilde A$ is not independent — it is $A$'s magnetic dual. Three degrees of freedom survive: **one photon and one scalar.**

## IV.4 Charge is winding [T/D]

A $p$-form couples minimally to a $(p-1)$-brane, so a 2-form couples to **strings**. A string wrapping the $u$-meridian looks, from four dimensions, like a point particle charged under $A_\mu = B_{\mu u}$; a string wrapping the Hopf circle is charged under $\tilde A_\mu$, hence magnetically under $A$.

$$\textbf{electric charge} = \text{winding on the meridian},\qquad \textbf{magnetic charge} = \text{winding on the Hopf circle}$$

This is the identification the theory has been circling since the flux-through-the-center picture: the meridian *is* the passage route for electric flux, now as the cycle a charge winds rather than as a field line it travels. And the two windings are exchanged by self-duality, which $\sigma$ flips — so **electric–magnetic duality is orientation reversal, the same operation that flips fermion chirality.**

## IV.5 The leftover scalar is an axion, and that is why it is harmless [D]

$B_{u\theta}$ is a component of a 2-form along two *spatial* directions, so it reduces to a **pseudoscalar**. Pseudoscalars couple derivatively, $\partial_\mu a\,\bar\psi\gamma^\mu\gamma_5\psi$, or topologically, $a\,F\tilde F$. Neither produces a static $1/r$ potential between unpolarized masses.

> **It produces no fifth force and does not spoil PPN $\gamma$** — unlike the radion of versions 2 through 5, which was a true scalar with a direct $1/r$ coupling and required the entire winding-stabilization apparatus to survive the solar system.

Moving electromagnetism from a 1-form to a 2-form therefore adds a massless field *for free*. This is the strongest incidental argument for the change.

## IV.6 What is gained

1. A bosonic chirality exists, in the right dimension, on the right object (§IV.1).
2. It is consumed by the reduction and is unrecoverable below (§IV.3): the "even-like chirality lost in the gravity base" is not imposed but forced.
3. Electric and magnetic charge acquire a geometric definition as windings on the two fibers (§IV.4).
4. The leftover scalar is an axion, not a radion (§IV.5).
5. The same involution flips both chiralities and the second-order charge (§II.3).

## IV.7 What must be rechecked, and what survives [D/O]

**Survives.** Below, $F = dA$ with the ordinary Maxwell action, $\epsilon = \mu_{\rm EM} = 1$, light on null geodesics. The photon comes from $B_{\mu u}$, which carries no Hopf index, so it is the $n = 0$ mode and remains **Hopf-neutral** as version 10 requires. Total charge on the compact cover is zero by Gauss. The self-duality is gone below, since a four-dimensional 1-form has no middle-degree duality. **Every electromagnetic result of version 10 survives; what is added is the upstairs chirality and the charge–winding identification.**

**To be rechecked [O].** Whether ordinary point-particle charges can be realized as string windings in this arena, or whether a coupling must be constructed. Whether the self-dual 2-form's well-known difficulty — it admits no simple covariant Lagrangian — obstructs anything here, given that Law IV′ is a field equation rather than an action principle. And the quantization of winding charge against the observed quantization of electric charge.

---

# PART V — EVEN AND ODD CHIRALITY, SIDE BY SIDE

| | odd chirality (fermions) | even chirality (light) |
|:--|:--|:--|
| carried by | a Weyl spinor | a self-dual 2-form |
| defined by | the eigenvalue of $\gamma_5$, the Clifford volume element | whether $H = +\star H$ or $H = -\star H$ |
| exists when | the dimension is even | the form is middle degree and $\star^2 = +1$ |
| in the canonical total space | yes: 6-D Weyl, 4 complex components | yes: 3-form in 6-D Lorentzian, $\star^2 = +1$ |
| in the gravity base | **survives** — a fermion is still a fermion below | **lost** — no self-duality for a 4-D 1-form; it is consumed relating the two vectors |
| flipped by $\sigma$ | yes ($S^+\leftrightarrow S^-$) | yes (SD $\leftrightarrow$ ASD) |
| visible to gravity | via $T_+$, chirality-blind | via $T_{\mu\nu}$, helicity-blind |

The asymmetry in the fifth row is the whole point, and it is not imposed. A spinor's chirality survives the quotient because spinors exist in every dimension and the operator descends; a form's self-duality does not survive because the middle degree changes when the dimension does. **The fermionic degree of freedom persists below and the bosonic one cannot.**

---

# PART VI — THE VISIBLE SPACE AND THE SEED

## VI.1 The problem [D]

Version 10's seed requires matter at $\hat n$ and *nothing* at $-\hat n$. The fermionic base makes $\hat n$ and $-\hat n$ the same place, so it cannot have one full and one empty. Stated structurally: the fiber of the canonical total space over a gravity-base point is **two** meridian arcs — two sheets — and the seed lives in their disconnectedness, while $\sigma$ identifies them.

The resolution is to stop trying to make visible space a *quotient* and make it *relational* instead. Two corrections come first, because the naive picture fails in ways that shape the construction.

## VI.2 Two corrections to the naive picture [V/T]

**The twin map fixes the poles, so there are no hemispheres.** A point of the 4-sphere is $x = \cos\chi\,e_5 + \sin\chi\,\hat n$, and the twin map sends $\hat n\to-\hat n$ at fixed $\chi$. At $\chi = 0$ and $\chi = \pi$ the point does not move at all: **the primary is its own twin, and so is infinity** **[V]**. North and south are not exchanged; everything between them is. A polar hemisphere split is simply not the twin structure. (This is consistent with $\sigma$ acting freely on $E$: the poles lie on every secondary meridian, so they are already removed from $E$'s base.)

**There is no global sheet label.** To say "this arc is the positive sheet, everywhere" is to give a **section** of the double cover $E\to E/\sigma$. A covering map admits a section exactly when its total space is disconnected; $E$ is a circle bundle over a connected base, hence connected. **No section exists** **[T]**. And the obstruction is precisely $\pi_1(\mathbb{RP}^3) = \mathbb{Z}_2$:

> **The same $\mathbb{Z}_2$ that creates the twin structure is what forbids sorting the sheets globally.** One cannot have the twin pairing be nontrivial *and* have an absolute "our light / their light."

## VI.3 The resolution: visual space is relational [D]

A covering map has no global section, but it always has **unique path lifting**: given a point $s\in E$ and a path $\gamma$ in $E/\sigma$ beginning at $\pi(s)$, there is exactly one lift of $\gamma$ in $E$ beginning at $s$ **[T]**. That is strictly weaker than a section, and it is all the construction needs.

> ### ◆ VISUAL SPACE, RELATIVE TO A SOURCE
> Fix a source event $s\in E$ — a point together with its sheet. For each light path $\gamma$ emitted from $\pi(s)$, lift $\gamma$ starting at $s$; the lift terminates at one of the two preimages of its endpoint. That endpoint is
> - **on the source's sheet** if the lift lands where the local matter's chirality matches the light's — interaction occurs, and matter is seen;
> - **the opposite sheet** if the lift lands on the other preimage — no interaction occurs, and the point reads as **void**.

**Visual space is therefore not a fourth manifold. It is the canonical total space with a basepoint.** The relational structure *is* the basepoint; path lifting is what makes the labeling well defined without ever needing the section that does not exist. This is the precise sense in which "a single point of the total space" is decoupled from "a single point of visual space": what a point is, visually, depends on where it stands relative to the source of the light passing through it.

## VI.4 What an observer sees [D]

Each photon travels a definite path, so its lift is definite, so its sheet is definite. **An observer therefore has a definite sky, assembled photon by photon, with no global choice made or needed.**

And the seed's observational content sharpens. A visible source sits at $\hat m$; its twin sits at $-\hat m$, which from the observer is a **different sky direction**, not the same one. Light from the twin does not interact, since it arrives on the opposite sheet. But gravity reads $T_+$ and is sourced by both.

> **The observer infers mass in a direction where they see nothing.** Gravitational attraction from a direction with no light in it — the seed, stated observationally, with matter present at both twins.

## VI.5 The monodromy, and what it costs [D]

Two sources on opposite sheets assign opposite labels. This is not an inconsistency: they describe the same physics the way two opposite-handed coordinate systems do, and nothing about the labeling is absolute. What is absolute is the *relation* — whether a given light path's endpoint matches or does not.

Carrying light around a loop generating $\pi_1(\mathbb{RP}^3)$ — a path from $\hat n$ to $-\hat n$ on the cover — returns it on the other sheet. So **visibility is path-dependent in principle**: a source can be visible along one path and dark along another, if the two differ by a twin loop. That loop is half the circumference, $\pi\ell/c = 646$ Gyr at $\ell = 63$ Gpc, forty-seven times the age of the universe.

## VI.6 What the construction still needs [O]

The chirality-matching rule of §VI.3 is the one unearned step, and its difficulty is specific.

**If the rule is about individual particle handedness**, it is a maximally parity-violating electromagnetism. Atomic parity violation in cesium is a weak-force effect of relative size $10^{-11}$, matching the Standard Model to half a percent; a chiral photon would make it order one. **Excluded by roughly eleven orders of magnitude.**

**If the rule is about sheets rather than handedness** — our light couples normally to both chiralities of matter *on our sheet*, and not at all to the other — local physics is unchanged and the parity bound does not apply. This is the version that can work.

**The obstacle is mass.** A massive fermion's chirality oscillates at $mc^2/\hbar$, which is $8\times10^{20}$ Hz for an electron. If chirality itself were the sheet label, a massive particle would change sheets that fast, which is either meaningless or a hundred-gigaparsec teleportation. Two ways out:

- **(a)** The mass term *is* the twin coupling (§III.2), so "changing chirality" is not motion but the field being described at its other end. The sheet label is then a coordinate on the description rather than a property carried, and the coupling rule must be reformulated accordingly.
- **(b)** The sheet label is **topological rather than chiral** — which lift of the path the light's history has followed — with chirality merely correlated. The parity bound is then evaded and the oscillation is irrelevant, because the label lives on the path, not on the particle.

**(b) is both the more promising and the one the relational construction of §VI.3 naturally supplies**, since path lifting is exactly a labeling that lives on histories rather than on states. Making it a *coupling* rather than a bookkeeping device is the unfinished work.

## VI.7 What is doing the work regardless [V]

Independent of everything above: light takes $\pi\ell/c = 646$ Gyr to cross to the twin, against 13.8 Gyr of cosmic age. **The twin is unobserved whether it is empty or full, and whether or not any coupling rule holds.** No measurement now or in any foreseeable future distinguishes the readings. Part VI is therefore a construction about what the theory *says*, and should be held to a structural standard rather than an observational one.

# PART VII — WHY WEYL, FROM THE BOTTOM

*No prior vocabulary assumed.*

## VII.1 What a fermion field is

A fermion field attaches, to every point of space and time, a short list of complex numbers. How long the list must be is not a choice: it is fixed by the dimension, because the list has to represent every possible rotation, and bigger spaces have more rotations. Four-dimensional spacetime: **four** complex numbers — the ordinary Dirac spinor of the electron. Six dimensions: **eight**.

## VII.2 The halving that only even dimensions allow

In even-dimensional spaces there is one extra operation, **chirality**, which splits the list exactly in half — and the halves *never mix*, under any rotation or boost. Each half is a self-contained field: a **Weyl spinor**. Four dimensions: four splits into two and two, the left- and right-handed electron fields. Six: eight into four and four. Odd dimensions: no split at all.

The only thing that ever couples the halves is a **mass term**. A massless Dirac fermion is genuinely two independent Weyl fermions written side by side; mass is what ties them into one object.

## VII.3 The choice and the bookkeeping

On the canonical total space, use the full eight-long list (a 6-D Dirac field) or one half, four long (a 6-D Weyl field). Reduce: the Hopf fiber is a circle, so any field on it becomes a tower of ordinary four-dimensional fields, and the list length carries down.

| upstairs | complex components | downstairs, per level |
|:--|--:|:--|
| 6-D Dirac | 8 | **two** four-dimensional Dirac fields |
| 6-D Weyl | 4 | **one** four-dimensional Dirac field |

## VII.4 The simplification

> **With the Weyl choice, one field upstairs gives exactly one electron downstairs. With the Dirac choice it gives two identical copies, and an extra rule would be needed to delete one.**

That is the whole of it. It is not the reframing that would turn a spinor into a polarization vector — that cannot happen in six dimensions, since a spinor index becomes a vector index only in *eight*, through the exceptional symmetry called triality. It is simply that the Weyl box is the right size for the thing being shipped: four complex components is **eight real numbers**, precisely the eight real numbers of a four-dimensional Dirac field. Not one more, not one fewer. **The arena carries no fermionic degree of freedom that does not appear as ordinary physics below.**

## VII.5 Why it matters here [D]

A Weyl field is chiral, so it *has* a chirality for the involution to exchange; the orientation reversal exchanges it; a Dirac field on the quotient results. A six-dimensional Dirac field would already carry both chiralities at every point, and $\sigma$ would have nothing to do — producing a duplicate rather than a pairing.

> **Weyl upstairs, Dirac downstairs. The involution turns one into the other, and the exactness of the count makes the exchange lossless.**

## VII.6 The cost [O]

Chiral fields in even dimensions can suffer **anomalies**: a classical symmetry fails once quantum effects are included, and the theory is inconsistent unless the collection of fields is arranged so the failures cancel. In six dimensions this is restrictive. Whether the model's content satisfies it is unexamined, and it is the price of the economy. The self-dual 2-form of Part IV contributes to the same condition, so the two chiral sectors must be checked together.

---

# PART VIII — STATUS

**Established [V/T/D].** The involution is orientation-reversing, free, and the unique natural candidate (§II.2). Its quotient is non-orientable, carries Pin structures, admits no global chirality (§III.1). A Weyl field upstairs is a Dirac field on the fermionic base, with chiral halves at twin points and a twin-coupling mass term (§III.2), with no doubled stress-energy (§III.3). Six-dimensional Lorentzian is exactly where a gauge field can be chiral (§IV.1). A self-dual 2-form reduces to one photon plus one axion, with self-duality consumed in the reduction (§IV.3). Electric charge is meridian winding, magnetic charge is Hopf winding, and $\sigma$ exchanges them (§IV.4). The leftover scalar is an axion and produces no fifth force (§IV.5). The Weyl restriction is exactly one 4-D Dirac's worth (§VII.4).

**Carried from version 10 unchanged.** Laws I, II, III; the arena; the seed's derivation from the meridian structure; the partition principle; the twin theorem; the fiber-length reading of Law I; the Weyl tensor from the fiber length; the base-resolution principle; statistics and exclusion untouched.

**Changed.** Law IV becomes Law IV′ (§IV.2): a self-dual 2-form replaces the 1-form on the cover. All four-dimensional consequences survive (§IV.7).

**Open [O].**

1. **The coupling rule of §VI.6**, in form (b): make the path-lifted sheet label a *coupling* rather than a bookkeeping device. The relational construction supplies the label; what is missing is its dynamics. The most substantive unfinished work in this version.
2. **Point charges as windings** (§IV.7): whether ordinary charge is realizable this way, and whether winding quantization matches charge quantization.
3. **Anomalies** (§VII.6): the six-dimensional Weyl fermions and the self-dual 2-form must cancel together.
4. **The Pin structure**: which of Pin$^\pm$ the fermionic base admits, and whether the choice is physical.
5. **Reading (a) versus (b) of the seed**: whether fermions are $\sigma$-equivariant or merely use the fermionic base to define the spinor bundle.
6. **Inherited.** The quantization fork; $g_2/m_{\rm unit}$; $\mu(\rho)$; twin parity assignments; emergent $G$; the AdS uplift; the literature review.

---

## Reference card, version 11

| topic | statement |
|:--|:--|
| **canonical total space** | $\mathbb{R}_t\times E$, 6-D: time, $S^4$ with its meridians, and the Hopf fibers |
| **gravity base** | $\mathbb{R}_t\times\mathbb{RP}^3$, 4-D; Law I |
| **fermionic base** | $\mathbb{R}_t\times E/\sigma$, 6-D; an identification, non-orientable |
| **the involution** | $\sigma:(\chi,\hat n,\theta)\mapsto(\chi,-\hat n,-\theta)$; det $=-1$; twin makes it free, reflection makes it reversing |
| **what $\sigma$ is** | one map flipping odd chirality, even chirality, and the second-order charge |
| **Dirac from Weyl** | chiral halves at twin points; mass is the twin coupling, local downstairs |
| **Law IV′** | self-dual 2-form $B$, $H = dB = \star_6H$; 6-D Lorentzian is the unique home |
| **reduction** | one photon ($B_{\mu u}$) $+$ one axion ($B_{u\theta}$); self-duality consumed relating $A$ to $\tilde A$ |
| **charge** | electric $=$ meridian winding; magnetic $=$ Hopf winding; exchanged by $\sigma$ |
| **the axion** | pseudoscalar, derivative coupling, no fifth force — unlike the retired radion |
| **even vs odd** | fermion chirality survives the quotient; form self-duality cannot, since middle degree changes with dimension |
| **visible space** | the canonical total space with a basepoint; sheets labelled by lifting light paths from a source |
| **no global sort** | $E\to E/\sigma$ is a connected double cover: no section. The twin's $\mathbb{Z}_2$ forbids an absolute split |
| **poles** | fixed by the twin map — the primary is its own twin; there are no hemispheres |
| **the seed, recovered** | matter at both twins; gravity sees all, light sees half; the observer infers mass from a direction with no light |
| **what it needs** | a sheet-selective coupling derived, not postulated; handedness-based versions die by atomic parity at $10^{11}$ |
| **regardless** | $\pi\ell/c = 646$ Gyr: the twin is unobserved either way |
