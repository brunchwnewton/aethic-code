# Projective Gravity — Version 9

### Visual Spacetime: the space of terminal pairs

> **What this version is.** Entry 23's proposal, worked out: take a light ray's two terminal points, read off the local $u$-direction at each, and declare their *sum* the time direction and their *difference* the space direction — as if the two $u$-directions were an incoming and an outgoing ray. The set of all such pairs is "visual spacetime," distinct from the base where gravity acts. Worked out, the proposal is a theorem rather than a construction: the rule holds automatically for any pair of causal vectors; applied to *twin* pairs it reproduces version 8's time direction from version 7's null fibers with no complexification; the Hopf-fiber constraint you suggested to cut the dimension selects exactly the twins; and visual spacetime, for twin pairs, is the flat five-dimensional space in which de Sitter is the unit hyperboloid. **Versions 7 and 8 are the same structure, and v9 is the proof.**
>
> **Tags.** **[V]** verified · **[T]** cited theorem · **[D]** derived · **[S]** sketch · **[O]** open · **[R]** retired.

---

# I. THE RULE IS A THEOREM

## I.1 Sum is timelike, difference is spacelike — automatically [T/V]

For two future null vectors $l, n$ normalized to $g(l,n) = -1$: $g(l+n,l+n) = -2$, $g(l-n,l-n) = +2$. For two future unit timelike vectors with relative Lorentz factor $\gamma = -g(u,v)\geq1$: $g(u+v,u+v) = -2-2\gamma<0$, $g(u-v,u-v) = -2+2\gamma\geq0$, zero iff parallel. **The rule needs no imposition; it is what causal pairs do.** The two directions must therefore already be causal — null (v7) or timelike (v8). On version 6's Euclidean $S^4$ the construction fails: unit vectors in $\mathbb{R}^5$ have spacelike sums and differences, and at the equator every meridian tangent is $-\hat e_5$, so every equatorial pair has *zero* difference.

## I.2 Twin pairs in v7: the fiber and its twin are the in/out pair [V]

In the null-fiber cover with the primary at the origin, the outgoing null ray at $r\hat n$ is $u_p = \partial_t + \hat n\cdot\nabla$ and the outgoing ray at the twin position $-r\hat n$ is $u_q = \partial_t - \hat n\cdot\nabla$ — outgoing from the origin *is* incoming along $\hat n$. Then

$$u_p + u_q = 2\partial_t,\qquad u_p - u_q = 2\,\hat n\cdot\nabla$$

**The twin supplies the incoming partner of the outgoing fiber**, and their sum and difference are the $(t,r)$ axes of the line through the primary: the Bondi double-null decomposition with the twin as the second null direction.

## I.3 Twin pairs in v8: the same, and it is the Wick rotation [V]

On de Sitter the worldline at $\hat n$ is $X = (\sinh t,\cosh t\,\hat n)$ and its twin is at $-\hat n$. Tangents: $u_p + u_q = (2\cosh t,0)$ along $x_0$ — time; $u_p - u_q = (0,2\sinh t\,\hat n)$ along $\hat n$ — space, **vanishing at the throat** where the tangents are parallel. The plane they span is ${\rm span}(\hat e_0,\hat n)\subset\mathbb{R}^{1,4}$, the plane through the origin containing *both* twin worldlines, meeting de Sitter in the hyperbola $x_n^2 - x_0^2 = 1$. Declaring that plane Lorentzian with $\hat e_0$ timelike is exactly $x_5\to ix_0$ restricted to the meridian's plane.

> **Entry 23 on twin pairs is version 8's Wick rotation, derived from version 7's null fibers by pairing each ray with its twin.** The complexification and the twin-pairing are two descriptions of one Lorentzian structure.

## I.4 The Hopf constraint selects the twins [T/V]

The Hopf circle through $\hat n$ contains $-\hat n$ at Hopf angle $\theta = \pi$ — the $-1$ in $U(1)$. "Terminal points on the same Hopf fiber, maximally separated" *is* the twin pair. The space of twin pairs is $S^4/\sigma_s$: four-dimensional, the base. Your dimensional cut lands on exactly the right object. For a non-twin pair on the same Hopf circle, both fibers are outgoing; the difference is spatial along the chord, and the sum carries a spatial part $\propto\cos(\theta/2)$ along the midpoint direction — a boosted frame. The twin is the rest frame of the line.

---

# II. WHAT VISUAL SPACETIME IS

## II.1 For twin pairs: the flat embedding [T]

Each twin pair's (sum, difference) plane is a 2-plane through the origin of $\mathbb{R}^{1,4}$. As $\hat n$ ranges over $\mathbb{RP}^3$, these planes sweep out all of $\mathbb{R}^{1,4}$ minus the $x_0$-axis — every point lies in exactly one plane ${\rm span}(\hat e_0,\hat n)$.

> **Visual spacetime is the five-dimensional Minkowski space in which de Sitter is the unit hyperboloid.** Light in de Sitter follows null straight lines of the ambient space that happen to lie on the hyperboloid; gravity is the hyperboloid's curvature. Visual (flat, five-dimensional) is not physical (curved, four-dimensional) — the distinction you asked for, realized as embedding-versus-hyperboloid.

With matter the base departs from exact de Sitter and the embedding is approximate; the statement is exact for the arena.

## II.2 The throat as the degenerate point [D]

At $t = 0$ the twin worldlines' tangents coincide and the difference vanishes: **visual space has zero extent at the throat and grows as $\sinh t$.** In the Euclidean picture the same fact reads: meridian tangents are parallel at the equator and diverge toward the poles. Visual space is born at nucleation with the scale factor.

## II.3 The general pair [D]

For an arbitrary terminal pair the rule still holds (§I.1), but the (sum, difference) plane is pair-dependent — the $(t,r)$ plane of *that* ray, with the ray's chord as its spatial axis. The full space of terminal pairs is eight-dimensional and carries only this fibered family of Lorentzian 2-planes, not a single metric. Visual spacetime is a manifold only after the twin (or Hopf-maximal) restriction; before it, it is a bundle of local frames over the space of rays.

---

# III. THE SHIFTS

1. **v7 $=$ v8.** The null fiber (v7) with twin pairing yields the timelike fiber (v8). The Wick rotation's content was: pair each outgoing ray with its incoming twin. The complex quadric is a bookkeeping for that pairing.
2. **The twin acquires a causal role.** In v6 it was a gravitational copy; in v8 it was beyond the horizon; in v9 it is the *incoming half* of the frame in which the line through the primary is at rest. The seed's $\mathbb{Z}_2$ is the in/out $\mathbb{Z}_2$ of a null pair.
3. **Visual spacetime is the embedding.** The "physical versus visible space" distinction of Entry 17 has a precise home: physical is the hyperboloid, visible is the ambient flat space.
4. **The Hopf constraint is exact.** Your dimensional cut selects the twins by the $-1$ in $U(1)$, the same fact that derived the projective postulate in v6.

---

# IV. STATUS

**Standing.** A theorem about v7 and v8, not a new theory: they are one structure. Canonical version remains 8, with v9 as the proof of its equivalence to 7 and the identification of visual spacetime.

**What it does not do [D].** It does not restore the half-orbit selection of Entry 17 — visual spacetime is flat and symmetric — and it does not change the physics of v8. It changes what the fiber, the twin, and the ambient space are *for*.

**Open [O].** The general-pair family of frames (§II.3) is a structure on the space of light rays; whether it carries a natural connection — a way to compare the frames of neighboring rays — is unexamined, and it is where anything beyond v8 would come from.

---

## Reference card, version 9

| topic | statement |
|:--|:--|
| **the rule** | sum timelike, difference spacelike, for any pair of causal vectors; a theorem |
| **needs** | causal fibers: v7 (null) or v8 (timelike); fails on Euclidean v6 |
| **twin pairs, v7** | $u_p + u_q = 2\partial_t$, $u_p - u_q = 2\hat n\cdot\nabla$: the twin is the incoming ray |
| **twin pairs, v8** | sum along $x_0$, difference along $\hat n$, vanishing at the throat; the plane ${\rm span}(\hat e_0,\hat n)$ |
| **v7 $=$ v8** | twin pairing $=$ Wick rotation |
| **Hopf constraint** | maximal separation on the Hopf circle $=$ the twin ($-1\in U(1)$); dimension 4 |
| **visual spacetime** | $\mathbb{R}^{1,4}$, the embedding; de Sitter the hyperboloid; light straight in one, curved in the other |
| **throat** | visual space vanishes there, grows as $\sinh t$ |
| **general pairs** | a bundle of Lorentzian 2-planes over the space of rays; no single metric |
