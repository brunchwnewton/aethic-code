# Projective Gravity — Version 8

### The Lorentzian Slice: time as the fiber

> **What this version is.** The arena is the complexified 4-sphere — the quadric $Q^4 = \{z\cdot z = 1\}\subset\mathbb{C}^5$ with its holomorphic metric — together with the Hopf bundle over it. Physics lives on its real slices. The Euclidean slice is version 6's $S^4$: the primary at the pole, the meridians as fibers, the Hopf lifts over shells. The Lorentzian slice is **de Sitter space**, and on it the meridians are comoving worldlines, the level 3-spheres are the expanding spatial sections, the equator is the throat, and the primary sits at the no-boundary cap where the Euclidean geometry closes. **The fiber coordinate $u$ is time.** Nothing is added; the two slices are two shadows of one complex object, and the Hartle–Hawking geometry is the gluing.
>
> **What it does that no earlier version could.** The static theorem — no redshift on a static geometry — is a theorem about the Euclidean slice. The Lorentzian slice expands. Hubble's law is the geometry.
>
> **What it changes.** The Einstein static universe becomes closed $\Lambda$CDM with a throat; the jellium becomes $\Lambda$; the primary becomes the instanton's cap rather than a mass; the twin of your own matter moves beyond your horizon and the dark wells in your patch become the twins of matter beyond it. Every identity is re-checked in Part III.
>
> **Tags.** **[V]** verified · **[T]** cited theorem · **[D]** derived · **[S]** sketch · **[O]** open · **[R]** retired.
>
> **Conventions.** $\ell$ the throat radius; global de Sitter $-dt^2 + \ell^2\cosh^2(t/\ell)\,d\Omega_3^2$; $\sigma_s:(t,\hat n)\mapsto(t,-\hat n)$ the spatial antipode; $\sigma:(t,\hat n)\mapsto(-t,-\hat n)$ the full antipode; $m\equiv4\pi G\rho_{\rm throat}\ell^2 = 2GM_{\rm throat}/\pi\ell$.

---

# I. THE CONSTRUCTION

## I.1 How the Lorentzian character is spat out [T/D]

A real slice of the complex quadric is the fixed set of an **antiholomorphic involution** $\varsigma$ with $\varsigma^*g = \bar g$; on it the metric is real, with signature determined by how many coordinates $\varsigma$ conjugates with a sign:

| involution | slice | signature |
|:--|:--|:--|
| $\varsigma(z) = \bar z$ | $x_1^2+\cdots+x_5^2 = 1$: $S^4$ | Euclidean |
| $\varsigma(z) = (\bar z_1,\ldots,\bar z_4,-\bar z_5)$ | $x_5 = ix_0$: $x_1^2+\cdots+x_4^2 - x_0^2 = 1$: $dS^4$ | Lorentzian |
| two coordinates flipped | signature $(2,2)$ | unphysical |

**The Lorentzian slice is a premise, not a patch**: it is the unique real structure with one time direction that commutes with the primary's residual $SO(4)$ — the coordinate it flips must be the polar axis through the primary. That is what ties time to the fibration: flipping $z_5$ makes the meridians timelike. The two signs $z_5 = \pm ix_0$ are the two time orientations, and the full antipode $\sigma$ exchanges them.

## I.2 The rotation, object by object [V]

With $\chi = \pi/2 + it/\ell$: $\sin\chi\to\cosh(t/\ell)$, and the spindle $d\chi^2 + \sin^2\chi\,d\Omega_3^2$ becomes $-dt^2 + \cosh^2t\,d\Omega_3^2$ — **global de Sitter**.

| Euclidean $S^4$ | Lorentzian $dS^4$ |
|:--|:--|
| meridians, the $u$-fibers | **comoving timelike geodesics** |
| level 3-spheres | spatial sections, radius $\ell\cosh(t/\ell)$, expanding |
| the equator $\chi = \pi/2$ | the throat $t = 0$ |
| the poles | $t = \pm i\pi\ell/2$: not on the real slice |
| the primary at the south pole | the no-boundary cap |
| base $\mathbb{RP}^3 = S^4/\text{meridians}$ | the space of comoving worldline pairs $=$ the throat mod antipode |

Every worldline converges on the cap in the Euclidean past. "The fibers point at the primary" becomes "all of time begins at the no-boundary origin." You had considered the radial direction as time; it is.

## I.3 The Hopf bundle under rotation [D]

$E$ over $S^4$ minus the secondary meridians becomes $E$ over $dS^4$ minus the secondary worldlines. The fiber stays a spacelike $U(1)$. In four Lorentzian dimensions a 2-sphere links a timelike curve, so the Chern class lives on **worldlines**: every massive body's worldline is a magnetic monopole of the second-order $U(1)$ with charge $M_-/m_{\rm unit}$, and $J_-$ is conserved because worldlines in de Sitter do not end. The Hopf lifts of 2-shells about a body at fixed $t$ are the Hopf 3-spheres over its shells in the spatial section. The complexification of $E$ is a $\mathbb{C}^*$-bundle over $Q^4$ whose real slices are $U(1)$ over $S^4$ and $U(1)$ over $dS^4$; the Chern data are topological and pass through unchanged.

---

# II. THE LAWS

> ### ◆ LAW I — GRAVITY
> General relativity on $dS^4/\sigma_s$ — equivalently on $dS^4$ with source $T_+(t,\hat n) = T(t,\hat n) + T(t,-\hat n)$ — with cosmological constant $\Lambda$. Time-orientable; spatial sections $\mathbb{RP}^3$. With dust this is closed $\Lambda$CDM.

> ### ◆ LAW II — THE FIBRATION
> The fibers are the comoving timelike geodesics of the base; the twin pairing is $\sigma_s$. Version 6's weaving law becomes the statement that comoving geodesics are deflected by matter — which Law I already says. Law II is a definition in v8, not an independent law; the permeability $\mu(\rho)$ survives only as an unobservable kinematic tilt. **[R as a law]**

> ### ◆ LAW III — THE SECOND-ORDER CONNECTION
> $dF = 2\pi\star J_-$ on $dS^4$, $J_-$ the odd mass current along worldlines, $F = d\alpha$ the curvature of $E$; fiber length $L_E = \Omega L^{\rm ref}$. Kinematic.

> ### ◆ LAW IV — ELECTROMAGNETISM
> Maxwell on $dS^4$. Spatial sections are closed, so total charge is zero on each; the compensating charge of any $Q$ is wherever the other charges are.

The action is v6's with the base $dS^4/\sigma_s$ and no separate $\mathbb{R}_t$: the cover is four-dimensional.

---

# III. EVERY IDENTITY, CHECKED

## III.1 The seed [D]

Matter on the comoving worldline at $\hat n$ sources the base at $[\hat n]$; the lift to $dS^4$ has wells on both the $\hat n$ and $-\hat n$ worldlines; nothing is on the latter. **Kept.** And sharpened: in global de Sitter, light from the spatial antipode at time $t$ arrives only as $t\to\infty$ (it must cover conformal angle $\pi$, and $\eta = 2\arctan e^{t/\ell}$ spans only $(0,\pi)$ over all time). **The twin of your own matter is beyond your horizon — forever.** What lies inside your horizon is the twins of matter in the antipodal patch. **The dark wells in our observable universe are the gravitational twins of galaxies we can never see**, and their uncorrelatedness with our matter — the $r = 1/\sqrt2$ signpost — is now a theorem of causal structure rather than an assumption about initial conditions.

## III.2 The twin theorem [V]

On the throat ($K_{ij} = 0$) the Hamiltonian constraint is $R^{(3)}[\phi^4g] = 16\pi\rho + 2\Lambda$ with background $6/\ell^2 = 16\pi\bar\rho + 2\Lambda$. Linearized: $(\Delta_{S^3}+3)\delta\phi = -2\pi\delta\rho_+$ — **the same operator as the ESU's**, for every split of the background curvature between matter and $\Lambda$. Same-sign antipodal pole, dipole kernel, a lone mass has no static solution. **Kept, exactly, at the throat.** Off the throat the constraint acquires $K$-terms and the exact statement is replaced by Law I's evolution, which preserves $\sigma_s$-symmetry of the source.

## III.3 The emergent-$G$ identity [D]

At the throat, Friedmann with $H = 0$ gives

$$\boxed{\;\Lambda\ell^2 + 2m = 3,\qquad m = \frac{2GM_{\rm throat}}{\pi\ell}\;}$$

**Version 6's Mach relation $GM_c/c^2\ell = \pi/2$ is the point $m = 1$, $\Lambda\ell^2 = 1$ of this family** — the Einstein static universe, the boundary case with zero acceleration. A bounce requires $\ddot a>0$, i.e. $m<1$: the throat carries *less* matter than the ESU. Pure de Sitter is $m = 0$, $\Lambda\ell^2 = 3$. $G$ remains a constant of Law I, constrained through one relation among $(M_{\rm throat},\ell,\Lambda)$. Constraint, not derivation — as in every version.

## III.4 The charge and the monopole [D/V]

**Electric charge:** the twin is electromagnetically empty. v6's retraction stands and strengthens: Maxwell on the cover with $Q$ at $\hat n$ needs $-Q$ somewhere on the closed section; the seed puts nothing at $-\hat n$; and $-\hat n$ is beyond the horizon anyway. The charged secondary's twin carries the $Q^2/r^2$ term as a tidal charge, no field.

**Second-order monopole:** the worldline at $\hat n$ carries Chern number $M_-/m_{\rm unit}$; $\sigma_s$ is orientation-preserving on $dS^4$ but reverses the linking sense of a 2-sphere about the antipodal worldline (it maps the ball about $\hat n$ to the ball about $-\hat n$ with the worldline's direction unchanged and the section's orientation reversed), so the twin worldline carries $-M_-/m_{\rm unit}$. **Kept.** The odd current is conserved on eternal worldlines.

## III.5 The partition [V]

$E$ over $dS^4$: $10$ (metric) $+\,1$ (fiber length) $+\,4$ (connection) $= 15$. Even: metric and length, from $T_+$ through Law I, with $L_E = \Omega L^{\rm ref}$ and $\Omega = \phi^2$ from the throat constraint. Odd: the connection, from $J_-$ through Law III. **Kept.** The Weyl tensor of $E$ is the connection's deviation from Hopf; the base Weyl is $-2[\nabla\nabla\phi]^{\rm TF}$ at the throat. **Kept.**

## III.6 The laws, one by one

| law | v6 | v8 | status |
|:--|:--|:--|:--|
| I | GR on $\mathbb{R}_t\times\mathbb{RP}^3$, $T_+$, $\Lambda = 1/\ell^2$, static | GR on $dS^4/\sigma_s$, $T_+$ at equal times, $\Lambda\ell^2 = 3-2m$, expanding | **kept**, closure generalized |
| II | weaving, $\nabla\cdot(\mu\nabla\Phi_u) = M_c[\delta(0)-\delta(\infty)]$ | comoving geodesics; sources at imaginary time | **demoted to a definition** |
| III | $dF = 2\pi\star J_-$ on meridians | $dF = 2\pi\star J_-$ on worldlines | **kept** |
| IV | Maxwell on $S^4$ | Maxwell on $dS^4$ | **kept** |

## III.7 What is lost [R]

- **The primary as a mass.** On the real slice there is no mass at the cap; the Euclidean action of the instanton, $I = -\pi\ell^2/G$, is what the pole carries. The Nariai bound would forbid a mass with $GM/\ell = \pi/2$ in de Sitter in any case.
- **The jellium.** Replaced by $\Lambda$ (and by throat matter with $m<1$).
- **The static wall.** Gone: $1+z = \cosh t_o/\cosh t_e$.
- **v7's null identification.** The primary is at imaginary time; its light cones are not on the real slice. Entry 20's instinct pointed at the throat: the constraint that picks the slice is the reality condition there.
- **Visibility of the twin.** In v6 light crossed the sphere in $\pi\ell/c$ and lensed at the twin. In v8 the twin is beyond the horizon. The lensing signpost changes meaning (§III.1) rather than disappearing.

---

# IV. THE COSMOLOGICAL SCALE, HONESTLY

Pure de Sitter from a throat of the late-time radius $\ell = c/(H_0\sqrt{\Omega_\Lambda}) = 5.4$ Gpc would need $t_0\geq3.2\,\ell/c = 56$ Gyr to reach today's curvature radius of $\geq63$ Gpc. The universe is $13.8$ Gyr old. **v8's throat is therefore not the late-time de Sitter; it is the nucleation surface at the inflationary scale**, and connecting it to the observed universe requires the standard history — inflation from the throat, reheating, matter and radiation eras, late-time $\Lambda$. Law I with dust and $\Lambda$ *is* closed $\Lambda$CDM, so the history is available; but the seed is planted at the throat, and its survival to today rests on Law I preserving the $\sigma_s$-symmetry of the source through that history, which it does. **[D/O]**

The three scales that earlier versions conflated — the base radius of v6 ($\geq63$ Gpc), the late-time de Sitter radius (5.4 Gpc), and the throat — are now distinct objects.

---

# V. STATUS

**Premise, not patch.** The arena is one complex object; Euclidean and Lorentzian are its real slices; the Lorentzian slice is the unique one compatible with the primary's symmetry. Time is the fiber.

**What v8 owes [O].** The inflationary connection: what plays the inflaton, and whether the throat's $m$ is set by anything. The fate of the odd sector through reheating. And Entry 17's spirals, idea B's magnifier, and the Tully–Fisher toy, all of which were results on a *static* base — they need re-deriving on the expanding one, where the closure plateau becomes a cosmological-time-dependent object.

**The one-line summary.** Version 6's arena, complexified, has de Sitter as its Lorentzian shadow. On that shadow the fiber is time, the sphere expands, the primary is the beginning, the twin is beyond the horizon, and every identity that was a theorem on the Euclidean side is a theorem at the throat.

---

## Reference card, version 8

| topic | statement |
|:--|:--|
| **arena** | complex quadric $Q^4$ with the Hopf bundle; real slices $S^4$ (Euclidean) and $dS^4$ (Lorentzian) |
| **signature** | fixed by the antiholomorphic involution; Lorentzian $=$ flip the polar axis; unique given the primary's $SO(4)$ |
| **dictionary** | meridians $\to$ comoving worldlines; latitudes $\to$ expanding sections; equator $\to$ throat; primary $\to$ no-boundary cap |
| **Law I** | GR on $dS^4/\sigma_s$ with $T_+$; closed $\Lambda$CDM |
| **throat relation** | $\Lambda\ell^2 + 2m = 3$; ESU at $m = 1$; bounce needs $m<1$ |
| **twin theorem** | $(\Delta+3)\delta\phi = -2\pi\delta\rho_+$ at the throat, for the whole family |
| **seed** | kept; the twin is beyond the horizon; dark wells $=$ twins of matter beyond it; $r = 1/\sqrt2$ uncorrelatedness a theorem |
| **Law III** | monopoles on worldlines, $M_-/m_{\rm unit}$; twin $-M_-/m_{\rm unit}$; current conserved |
| **partition** | $10+1+4$; even $\leftarrow T_+$, odd $\leftarrow J_-$ |
| **charge** | twin EM-empty; tidal charge on the charged secondary's twin |
| **redshift** | $1+z = \cosh t_o/\cosh t_e$ |
| **scales** | throat (inflationary), late dS ($5.4$ Gpc), curvature today ($\geq63$ Gpc): distinct |
| **lost** | primary as mass; jellium; static wall; v7's null rays; twin visibility |
