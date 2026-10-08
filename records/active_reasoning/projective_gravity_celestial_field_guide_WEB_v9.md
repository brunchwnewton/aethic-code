# Projective Gravity — Version 9

### The Base-Resolution Principle, on the Null Fiber

> **What this version is.** Versions 6 through 8 fixed the arena and its laws. Version 9 adds no metric, no law, and no field. It adds one principle about *what decoherence is allowed to use*, adopts the null reading of the $u$-fiber from version 7, and follows both to their consequences. The principle: a detector lives on the base, so the only which-path information it can record is base information; fiber position, fiber direction, and fiber phase are not base observables; therefore two paths that agree on the base within the detector's resolution and differ only in fiber data cannot decohere — they interfere, with a relative phase set by their fiber difference. **The fiber is a decoherence-free subspace.**
>
> **What follows, in order.** The loosened Born rule — paths from distinct terminal points on one fiber — lives inside the second-order total space with no new structure. A base detector integrates over the fiber it cannot resolve; the integral selects the zero modes, so light sources from every fiber point at once while charged modes average to invisibility. The twist is seen only through paths, as the Aharonov–Bohm phase. On the null fiber, the fiber coordinate is the action and the fiber phase is $e^{iS/\hbar}$ — **the path-integral weight itself** — with the Schrödinger equation as its null reduction; the two fibers carry the two halves of a charged particle's action; and mass is a fiber charge, which is Bargmann's superselection rule. The fiber average that gravity reads is the quantum expectation value: **Law I is semiclassical and the projective quotient is the classical limit.** The seed becomes a superposition the base cannot resolve, and the factor of two that has followed the projective postulate since version 1 is shown to have been a miscount. The Hopf–spinor correspondence is exact at two levels and open at the third, where it is the strongest and least-selected claim in the program.
>
> **Tags.** **[V]** verified · **[T]** cited theorem · **[D]** derived · **[S]** sketch · **[O]** open · **[R]** retired.
>
> **Conventions.** As v6–v7. $n$ the Hopf charge; $m$ the mass, which is the $u$-fiber charge; $\Delta_\theta$, $\Delta_u$ the fiber separations of two terminal points; $\alpha$ the second-order connection, $F = d\alpha$; $\Sigma$ the surface between two base paths; $\langle\cdot\rangle$ the quantum expectation value.

---

# I. THE PRINCIPLE

## I.1 Statement

> ### ◆ THE BASE-RESOLUTION PRINCIPLE
> A detector is a base object. It can record base position and base direction, within its resolution, and nothing else. Two paths in the second-order total space that (i) end at terminal points projecting to the same base point and (ii) arrive with directions whose base projections lie within the detector's resolution **cannot be distinguished by the detector, and therefore do not decohere.** They contribute to one amplitude, with relative phase set by their fiber difference.

Condition (i) is the fiber-product condition; (ii) is the direction condition. Neither is an assumption about matter or light; both are statements about what a quotient forgets.

## I.2 The domain [T]

The valid pairs are $V = \{(p,q)\in E\times E : \pi(p) = \pi(q)\} = E\times_BE$, the fiber product. Its relative fiber coordinate is flat and untwisted: the connection acts on the center-of-mass phase and cancels in the difference. $V$ is where the Born rule sums; it is not given a metric and is not a spacetime.

## I.3 Why it is a theorem [D]

Decoherence is the recording of which-path information in degrees of freedom the detector correlates with. A base detector's degrees of freedom are base functions. A fiber datum is, by definition of the quotient, invariant under the fiber action, hence not a base function, hence not recordable. What cannot be recorded cannot decohere. **The fiber is decoherence-free because the base is a quotient — the same fact that made gravity blind to it.**

---

# II. WHAT A BASE DETECTOR SEES

## II.1 The fiber-integrated amplitude [V]

For a field of fiber charge $n$, two terminal points separated by $\Delta$ contribute $e^{in\Delta}$, and

$$\int_0^{2\pi}e^{in\Delta}\,d\Delta = 2\pi\,\delta_{n0}$$

**$n = 0$:** every fiber position adds coherently. Light sources from all fiber points at once and the detector registers the full sum — Law IV unchanged. **$n\neq0$:** fiber-separated sources average to zero. Not decohered — invisible, because the base cannot resolve the phase that would make them add. "The base sees zero modes" is what a base detector can register, not an assumption about matter.

## II.2 The twist, through the paths [T]

Two base paths $\gamma_1,\gamma_2$ enclose $\Sigma$; their horizontal lifts arrive with fiber phases differing by $n\int_\Sigma F$; the detector cannot resolve the fiber velocities that would distinguish them; they interfere; the fringe shifts by $n\int_\Sigma F$. This is the Aharonov–Bohm effect, and it is condition (ii) stated as physics.

---

# III. THE FIBER IS THE ACTION — THE NULL READING

## III.1 The Bargmann reduction [V]

On the null-fiber cover (v7), the Bargmann metric $g = -2\Phi\,dt^2 + 2\,dt\,du + dx^2$ has $g^{tt} = 0$, $g^{tu} = 1$, $g^{uu} = 2\Phi$, $\sqrt{|g|} = 1$. Fourier-decompose a massless field along the null fiber with fiber momentum $m$: $\Psi = e^{imu/\hbar}\psi(t,x)$. Then $\Box_5\Psi = 0$ becomes, exactly,

$$i\hbar\,\partial_t\psi = -\frac{\hbar^2}{2m}\nabla^2\psi + m\Phi\,\psi$$

**The Schrödinger equation is the null reduction of a wave equation** (Duval–Burdet–Künzle–Perrin 1985). This is a packaging statement; the primary one is next.

## III.2 The fiber phase is the path-integral weight [D]

Along a trajectory the fiber advances by $du = (L/m)\,dt$, so $m\,u = \int L\,dt = S$ and

$$\boxed{\;e^{imu/\hbar} = e^{iS/\hbar}\;}$$

**The fiber phase is the path-integral weight.** The primary fact is that the fiber coordinate is the action; summing over lifts of base paths with their fiber phases *is* the path integral; Schrödinger is what that sum becomes as a differential equation. The ordering you insisted on — path integral first, Schrödinger derived — is the one the geometry gives. To be clear about provenance: this is the known Eisenhart–Bargmann correspondence, inherited by any theory with a null fiber; what the present theory adds is the twin structure and the principle of §I, not the correspondence itself.

The parallel with the Hopf fiber is exact in form:

| fiber | charge | coordinate | phase |
|:--|:--|:--|:--|
| Hopf | $n$ | $\theta$ | $e^{in\theta}$ |
| $u$ (null) | $m$ | $u$ | $e^{imu/\hbar}$ |

## III.3 Which fiber carries which action [D]

For a particle of mass $m$ and Hopf charge $n$ on a base path $\gamma$,

$$S = \underbrace{m\,\Delta_u}_{\int(\tfrac12mv^2 - m\Phi)\,dt} + \underbrace{n\hbar\,\Delta_\theta}_{-n\hbar\int_\gamma\alpha}$$

**The $u$-fiber carries the mechanical action — kinetic plus gravitational; the Hopf fiber carries the gauge action — the coupling to Law III's connection.** Both, and they split cleanly. The electromagnetic phase is *not* a fiber of $E$: Law IV is Maxwell on the cover, a separate $U(1)$.

## III.4 Mass is a fiber charge: Bargmann's superselection rule [T/D]

$p_u = m$ is the central charge of the Galilei group's central extension. Because the base cannot resolve the fiber, $\int e^{i(m_1 - m_2)u/\hbar}du$ vanishes unless $m_1 = m_2$: states of different mass cannot be coherently superposed. That is **Bargmann's 1954 mass superselection rule**, and it is §II.1 with $n\to m$. The principle reproduces a known superselection rule rather than resembling one.

## III.5 The relativistic completion [D]

The null fiber gives Schrödinger — the Newtonian limit. On the timelike fiber of version 8 the same statement reads $e^{-imc^2\tau/\hbar}$ with $S = -mc^2\int d\tau$: fiber phase $= e^{iS/\hbar}$ still, and the reduction is Klein–Gordon. One sentence, two limits. Version 9 works on the null fiber, as chosen; the relativistic detector physics is v8's.

---

# IV. THE INTERPRETIVE PAYOFF

## IV.1 The fiber is the phase; the quotient is the classical limit [S/D]

The $u$-fiber is the mass phase (§III), the Hopf fiber the second-order charge phase. The base is where detectors live and gravity acts. Gravity reads the fiber-averaged stress-energy, and the average of a state's stress-energy over its phase is its expectation value:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi\,\big\langle T_{\mu\nu}\big\rangle$$

**Law I is the semiclassical Einstein equation. "Gravity is blind to the fiber" means gravity couples to expectation values, not to branches. The projective quotient is the classical limit.**

## IV.2 The seed as an unresolvable superposition [S]

$\hat n$ and $-\hat n$ are distinct on the cover and one point of the base. "Matter at $\hat n$" and "matter at $-\hat n$" are base-identical; no detector distinguishes them; by §I they never decohere. **The twin is the other branch of a superposition the base cannot resolve.** Gravity sees both; light, in one branch, sees only its own. Matter at $p$, gravity at $\pm p$, nothing at $-p$ — with "nothing" meaning *we are not in that branch.*

## IV.3 The factor of two, closed [V]

Reading P (projection): matter $M$ at $\hat n$, nothing at $-\hat n$; base source $T(\hat n) + T(-\hat n) = M$. Reading S (superposition): $\langle\rho\rangle = M/2$ at each twin; base source $M/2 + M/2 = M$. **Identical base source, identical base metric, identical lift.** The two full-depth wells at $\pm\hat n$ are one base well pulled back, not two sources. The earlier "total $2M$" counted lifted wells as masses. The only thing that differs between P and S is the matter content of the branch we are not in — unobservable. **The factor of two that has accompanied the projective postulate since version 1 was a miscount, and it is closed.**

## IV.4 Semiclassical gravity and signalling [D]

The Eppley–Hannah / Page–Geilker objection: $G = 8\pi\langle T\rangle$ plus *collapse* lets a distant measurement jump the source, hence signal. In v9 the source is the fiber-sum of $\langle T\rangle$, and fiber superpositions — including the twin branches — are decoherence-free by §I: no base measurement collapses them, so the source never jumps. **No signal in that sector.** For base-position superpositions v9 makes no semiclassical claim: base positions are resolvable, they collapse, and what gravity does then is whatever the underlying theory says. v9 is neither vulnerable there nor a cure. The richer space helps in exactly one way — it isolates a sector where semiclassical coupling is consistent *because* collapse is impossible there.

---

# V. THE HOPF–SPINOR CORRESPONDENCE, AT THREE LEVELS

**(a) One 2-spinor. Exact [T].** A unit spinor in $\mathbb{C}^2$ is a point of $S^3$; its Bloch direction is a point of $S^2$; the Hopf fibration $S^3\to S^2$ *is* the phase over the Bloch sphere. This is the level at which the correspondence feels obvious, and it is.

**(b) The spatial $S^3 = SU(2)$. Exact [T].** The right-$U(1)$ orbits are great circles, and spinors on $S^3$ carry charge $\pm\tfrac12$ under them — spin projection on the Reeb axis (v5 §III.5). But these circles are directions *in* space; the base sees them; **they are not a decoherence-free fiber.** Level (b) is about the spin structure of the arena, not about $E$.

**(c) $E$'s fiber as the phase of a spinor field. Open [S], and the strong claim.** For $E$'s fiber to be a spinor's phase, the spinor field must have a definite polarization $\hat s:S^4\setminus\Gamma\to S^2$ with $E = \hat s^*(\text{Hopf})$, so that the monopoles on the meridians are **hedgehog lines** of the polarization field with winding $M_-/m_{\rm unit}$. "A spinor field over a Hopf fiber surrounding the whole Earth" is exactly this: a cosmic spin texture with a hedgehog of winding $M_\oplus/m_p$ at Earth. Two facts weigh against it landing automatically. The positive spin bundle of $S^4$ has $c_2 = 1$, so any Weyl spinor field on $S^4$ has a *point* zero, not line defects; and over $S^4$ minus a point the phase bundle is trivial, with no monopoles at all. So $E$ is not the phase bundle of a Weyl spinor field on $S^4$ as such; it would be the phase bundle of a *polarization texture* that nothing in the theory selects. Your instinct that this level is too good to be true is the right one. What is true at this level: $E$'s charge $n$ enters the Born-rule sum with exactly the algebra of a spin projection, and levels (a) and (b) are theorems. Level (c) is where the program would gain the most and where it currently has the least.

---

# VI. WHAT VERSION 9 KEEPS, DROPS, ADDS, AND CLOSES

| item | status |
|:--|:--|
| Laws I–IV; the arena of v6; the null fiber of v7 | **unchanged**, v7's reading adopted |
| the fiber product $E\times_BE$ | **kept** as the Born rule's domain |
| the visual metric, the sum/difference rule | **dropped** |
| the action rule | **absorbed**: the fiber coordinate *is* the action (§III) |
| photon Hopf-neutrality; $u$-smearing of matter | **reinterpreted**: properties of base detection, not of matter |
| the factor of two | **closed** (§IV.3) |
| **added** | the base-resolution principle; fiber phase $= e^{iS/\hbar}$; the action split; mass superselection; Law I as semiclassical; the seed as a branch; the three-level spinor verdict |

---

# VII. STATUS

**Settled [V/T/D].** Why the base sees zero modes; why the twist is a phase; that the loosened Born rule needs no new law; that the fiber phase is the path-integral weight and Schrödinger its null reduction; that mass is a fiber charge and is superselected; that the factor of two was a miscount; that the fiber sector is free of the semiclassical signalling problem.

**Proposed [S].** That the quotient is the classical limit; that the twin is a branch; that $E$'s fiber is a spinor phase (level c).

**Open [O].** What, if anything, selects a polarization texture at level (c). Whether the base-position sector has any semiclassical statement at all. The relativistic form of §III on the timelike fiber, joined to v8.

---

## Reference card, version 9

| topic | statement |
|:--|:--|
| **principle** | detectors are base objects; fiber data cannot be recorded; fiber-differing paths do not decohere |
| **detector sum** | $\int_0^{2\pi}e^{in\Delta}d\Delta = 2\pi\delta_{n0}$ |
| **twist** | seen only as $n\int_\Sigma F$ through paths (AB) |
| **Bargmann** | $\Box_5\Psi = 0$, $\Psi = e^{imu/\hbar}\psi$ $\Rightarrow$ Schrödinger; $mu = S$; fiber phase $= e^{iS/\hbar}$ |
| **action split** | $S = m\Delta_u$ (mechanical, $u$) $+\;n\hbar\Delta_\theta$ (gauge, Hopf) |
| **superselection** | mass is the $u$-charge; Bargmann 1954 |
| **Law I** | $G + \Lambda g = 8\pi\langle T\rangle$; the quotient is the classical limit |
| **seed** | the twin is the unresolvable other branch |
| **factor of two** | closed: one base well pulled back, not two sources |
| **signalling** | none in the fiber sector (no collapse there); no claim on the base sector |
| **Hopf–spinor** | (a) exact, (b) exact but spatial, (c) open: needs a cosmic polarization texture |
