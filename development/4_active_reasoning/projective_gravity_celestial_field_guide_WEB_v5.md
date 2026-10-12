# Projective Gravity — Version 5

### The Two-Circle Formulation: a field guide

> **What this version is.** It is version 3 revised. Version 3 built the second order as an extra $U(1)$ fiber over the spatial 3-sphere and gave it physics — monopoles at masses, a gauge field sourced by the odd sector, a partition theorem, black-hole charges. Version 4 removed the extra fiber to fix a stabilization problem and turned out to have no second-order physics at all: nothing couples to a structure that is merely a description of space. Running the checks properly shows the stabilization problem was an artifact, that the extra fiber is consistent when it is a genuine Kaluza–Klein circle with its own winding, and that in that form the two fibers are *exactly* alike — the non-privileging principle holds as an identity. Version 5 is that theory, with version 4's one durable result (the seed's postulate derived; Law I as the equation for the spatial Hopf fiber length) absorbed as geometry.
>
> **Four corrections** are made to earlier versions and stated in §IV.1: the ordinary photon is Hopf-neutral (helicity is not Kaluza–Klein charge), so the polarization law and the lensed-image bound of v3 are retracted; the Tully–Fisher closure result is a statement about a toy universe; the joint-stabilization "obstruction" was double-counting; and version 4's second order was inert.
>
> **Tags.** **[V]** verified · **[M]** measured numerically · **[T]** cited theorem · **[D]** derived · **[S]** sketch · **[O]** open · **[R]** retired.
>
> **Conventions.** $G = c = 1$ unless restored; $\ell$ the spatial 3-sphere radius; $\psi$ and $L_2$ the two circle lengths; $w_1, w_2$ their windings; $T_\pm(\hat n) = T(\hat n)\pm T(-\hat n)$; $\phi$ the conformal factor of the 3-metric, $g_3 = \phi^4 g_{S^3}$.
>
> **Reading guide.** First order: Part I. The spatial sphere's own Hopf structure — the seed derived, Law I as a fiber equation: Part II. The second circle — stabilization, the mirror, monopoles, the dynamic sector: Part III. Corrections and status: Part IV.

---

# PART I — THE FIRST-ORDER THEORY (unchanged)

## I.1 Arena, seed, and laws

$M_5 = \mathbb{R}_t\times S^1_u\times S^3$; $\partial_u$ is the radial direction of $\mathbb{R}^4\setminus\{0\}$, nowhere vanishing **[T]**. The scaling group is $\mathbb{R}^* = \mathbb{R}^+\times\mathbb{Z}_2$, so the base is $\mathbb{RP}^3$ and the fiber over $[\hat n]$ is disconnected — the $u$-circle at $+\hat n$ and at $-\hat n$ **[D]**. $S^3\cong SU(2)$, $\mathbb{RP}^3\cong SO(3)$, the antipodal map $=-1$: gravity lives on the rotation group and cannot see the sign of a spinor **[V]**.

> **The seed.** Matter at $(u_0,+\hat n)$ sources the base at $[\hat n]$, whose lift has wells at both $\pm\hat n$; nothing is at $-\hat n$. Blindness, not crossing.

> ### ◆ LAW I — GRAVITY
> $$\ell^2R^{(4)}_{\mu\nu} = \ell^2\psi^{-1}\nabla_\mu\nabla_\nu\psi + 2\Big(\tau_{\mu\nu} - \tfrac13\tau g_{\mu\nu}\Big), \qquad \tau = S/\bar\epsilon, \quad S = T_+$$

> ### ◆ LAW II — THE FIRST-ORDER FIBRATION
> $$\Box f = 0, \qquad \oint df = \ln\lambda, \qquad f = w_1u$$

## I.2 Theorems carried forward

Terminus and cone theorems, $\Lambda = 1/\ell^2$ **[V]**; the **twin theorem** — static operator $\Delta_{S^3}+3$, same-sign poles at both ends, kernel the dipoles, zero-dipole identically satisfied on $\mathbb{RP}^3$ **[V]**; the Mach relation $GM_{\rm tot}/c^2\ell = \pi/2$ as a consistency relation **[V]**; the $k$-dial **[V]**; **winding stabilization** $\psi_0^2\propto w_1^2/|\Lambda|$, restoring PPN $\gamma$ from $\tfrac12$ to $1$ **[V/D]**; Bianchi closure and descent **[V/D]**; the two-speed cover **[D]**; the $r = 1/\sqrt2$ signpost **[D]**. The Tully–Fisher closure result is retained as a toy-universe theorem only (§IV.1).

---

# PART II — THE SPATIAL SPHERE'S OWN HOPF STRUCTURE

*This part is geometry, not dynamics. It concerns the Hopf fibration of the spatial $S^3 = SU(2)$ itself — the right-$U(1)$ orbits, great circles of length $2\pi\ell$ — which is not an extra dimension and to which nothing couples. Its value is two theorems about the first-order theory.*

## II.1 The projective postulate is derived [D]

The Hopf $U(1)$ is $z\mapsto e^{i\theta}z$ on $\mathbb{C}^2$, and at $\theta = \pi$ it is $-1$: **the Hopf circle through $\hat n$ passes through $-\hat n$** (verified pointwise). Any average of matter over a Hopf circle automatically includes both twins. The $u$-fibration must share this property if the two fibrations are not to be privileged against each other — and in $\mathbb{R}^4$ it does, since a line through the origin meets $S^3$ at $\pm\hat n$. The disconnected fiber (A2), the seed's load-bearing assumption since the first version, follows from A1 and non-privileging. It is no longer a postulate.

## II.2 Law I is the equation for the spatial fiber length [D/V]

Weak-field statics are conformally round, $g_3 = \phi^4g_{S^3}$, and the Hamiltonian constraint linearized about the Einstein-static universe is

$$\boxed{\;(\Delta_{S^3}+3)\,\delta\phi = -2\pi\,\delta\rho_+\;}$$

— the twin-theorem operator, whose Green's function has the same-sign pole at the antipode. The Hopf circles are great circles of the round metric, so their physical length is $L_H = 2\pi\ell\,\phi^2$. **Law I, in the sector containing every weak-field static configuration, is the equation for the spatial Hopf fiber length**, and the twin is inherited: for a uniform ball with its twin, $\phi^2 = 2.017$ at the ball's center, $1.620$ at its surface, $1$ at the equator, and identically $2.017$ at the *empty* antipode, to $10^{-11}$ **[V]**. A lone ball has dipole $0.169\neq0$ and the equation has no solution — the numerical solver returns the kernel mode as its symptom. The seed, as fiber geometry.

## II.3 What this structure does not do [D]

The Hopf circles are directions *in* space. A field on $S^3$ is a field on $S^3$; its "Hopf charge" is angular momentum about the Reeb axis — a Fourier label, not a coupling. The contact form $\alpha_H$ is a description of the round metric's fibration, and its deformation by matter is the metric's, already in Law I. **Nothing couples to it; it has no observables beyond Law I; light is blind to it.** Version 4's second order was this structure alone, which is why it was inert (§IV.1).

---

# PART III — THE SECOND CIRCLE

## III.1 The second circle, and why it must have a winding [V]

The second-order total space is $\mathcal{E} = \mathbb{R}_t\times S^1_u\times S^1_2\times S^3$: a second compact circle of length $L_2$, fibered over the spatial 3-sphere with a connection $\alpha$ and monopoles at masses. Reducing on both circles gives 4-D gravity with two dilatons and two graviphotons.

Two circles need two stabilizations. Version 3 gave the second circle a *flux* (the Hopf monopole field) and found no joint minimum with the winding on the first: a flux pushes its circle *down* and needs $\Lambda>0$, a winding pushes its circle *up* and needs $\Lambda<0$ **[V]**. But that computation treated the fiber length as an independent modulus in the very sector where it is locked to gravity's conformal factor (§III.7), and, more to the point, a winding on the second circle is what non-privileging requires. With windings $w_1, w_2$ on both circles and $\Lambda_6<0$,

$$V(\psi,L_2) = -\frac{|\Lambda_6|}{\psi L_2} + \frac{w_1^2}{2\psi^3L_2} + \frac{w_2^2}{2\psi L_2^3}$$

has the critical point

$$\boxed{\;\psi_0^2 = \frac{2w_1^2}{|\Lambda_6|}, \qquad L_{2,0}^2 = \frac{2w_2^2}{|\Lambda_6|}, \qquad \frac{L_{2,0}}{\psi_0} = \frac{w_2}{w_1}\;}$$

with Hessian eigenvalues $(\tfrac14,\tfrac12)\times$positive — **a joint minimum, from one cosmological constant** **[V]**. The two circles are stabilized together, and *their length ratio is the winding ratio*.

> ### ◆ LAW II′ — THE SECOND-ORDER FIBRATION
> $$\Box f_2 = 0, \qquad \oint df_2 = \ln\lambda_2, \qquad f_2 = w_2\theta_2, \qquad L_{2,0}/\psi_0 = w_2/w_1$$

## III.2 The mirror principle, exact [V/T]

The spatial total space of $\mathcal{E}$ carries a $T^2$-action; its fiber is an elliptic curve with modular parameter

$$\tau = i\,\frac{w_2}{w_1}$$

and $SL(2,\mathbb{Z})$ exchanges the two circles. For the untwisted torus the orthonormal fiber components of the Ricci tensor are

$$R_{uu} = -\frac{e^{-2h}}{L_2\psi}\Big[L_2\nabla^2\psi + \nabla L_2\cdot\nabla\psi\Big], \qquad R_{\theta\theta} = -\frac{e^{-2h}}{L_2\psi}\Big[\psi\nabla^2L_2 + \nabla L_2\cdot\nabla\psi\Big]$$

and swapping $\psi\leftrightarrow L_2$ in one gives the other with difference identically zero **[V]**. Reducing 6-D Einstein on $u$ writes matter's $u$-average on $L_2$; reducing on $\theta_2$ writes matter's $\theta_2$-average on $\psi$. **The length of each circle is sourced by matter averaged over the other.** Unlike versions 3 and 4, where the "mirror" paired a micron circle with a kiloparsec one, here both are Kaluza–Klein circles of comparable size, the needle is $w_2/w_1$, and the principle holds as stated. What breaks the exact symmetry is only the monopole flux on the second circle (Chern classes at masses; the first circle has none), which $SL(2,\mathbb{Z})$ can redistribute but not remove.

## III.3 Masses are Kaluza–Klein monopoles [T/D]

A mass at $\hat n$ carries Chern number $\lfloor M/m_{\rm unit}\rfloor$ on the second circle: the bundle over a small sphere about it is the Hopf bundle taken $N$ times, and the total space near the mass is the **Gross–Perry–Sorkin** geometry — the circle fibered over shells with the fiber pinching to zero at the core, asymptotically of length $L_{2,0}$ **[T]**. Version 3's "Hopf lift of each shell about the mass" is exactly this local geometry, with the fiber length now set by the winding rather than by the Riemannian-submersion normalization $4\pi\ell\sin\chi$; the $S^4$ conformal root, the $O(5)$ recentering group, and the Easter eggs of v3 §II.13–17 belonged to that normalization and are retired **[R]**.

**The anti-monopole is automatic.** Chern number $+N$ at $\hat n$ and $-N$ at $-\hat n$ by orientation reversal; net charge zero on the closed sphere **[V]**. **The $O(2)$-descent selection rule** stands: the construction produces $\Gamma = \mathbb{Z}_2$ and nothing else **[D]**. **The partition theorem** stands: gravity reads $T_+$; the second circle's flux reads $\rho_-/m_{\rm unit}$; together they see all of $T$ **[D]**.

**The quantization fork, resolved by the photon's neutrality.** Every constraint that made $m_{\rm unit}$ cosmological — the lensed-image bound, the Poisson-spot argument — assumed the ordinary photon carried second-circle charge. It does not (§III.6). With light blind to the second circle, $m_{\rm unit}$ is constrained only gravitationally (§III.4), and the natural option is the simplest: **$m_{\rm unit}$ is a particle mass, every particle is one monopole, and macroscopic bodies carry $N = M/m_{\rm unit}$ quanta**. The holonomy $2\pi N$ around any body is then effectively random — for the second circle's KK modes, which decohere around everything, invisibly. Nothing observed is touched. The alternative — $m_{\rm unit}\sim10^{14}M_\odot$, superclusters only — remains coherent and is recorded as option (c) **[O]**.

## III.4 The dynamic sector [D]

The second circle's connection $\alpha$ is a Kaluza–Klein gauge field with kinetic term $-\tfrac14L_2^2F^2$ and coupling $g_2\propto1/L_{2,0}$. It is sourced by the odd sector, $dF = \star J_-/m_{\rm unit}$, and its flux energy gravitates. Consequences carried over from v3, now with a definite fiber length:

- **Black holes.** A hole of mass $M$ carries second-circle magnetic charge $N = M/m_{\rm unit}$ on its horizon; if the flux gravitates with coupling $g_2$, the extremality bound is $M^2 = Q^2 + P_{\rm eff}^2$ with $P_{\rm eff} = g_2M/m_{\rm unit}$. Observed holes are Schwarzschild/Kerr to the precision of ringdowns and shadows, so $g_2/m_{\rm unit}\ll1$ in the natural units — a bound on the one new coupling, computable from the data **[O]**.
- **Three operator signs.** Mass (same), charge (opposite), second-circle monopole (opposite): the twin of a hole $(M,Q,N)$ is $(M,-Q,-N)$ **[D]**.
- **Holonomy and Machian decoherence.** Two paths enclosing $N$ quanta differ by $2\pi N$ for a KK mode of unit charge; the threshold at which paths decohere is set by enclosed odd mass in units of $m_{\rm unit}$ **[S]**.
- **The first bound.** The repulsive $P^2/r^2$ term shifts a perihelion by $-(P/M)^2/6$ relative to GR's advance. Mercury agrees with GR to $10^{-4}$, hence in option (a)
$$\boxed{\;g_2/m_{\rm unit} = P/M < 0.024\;}$$
Lunar laser ranging gives nothing useful ($M/r\sim10^{-11}$ at the Moon); ringdowns test $P/M$ at $0.1$–$0.3$, weaker. Option (c) is unconstrained by this **[D]**.
- **Earth in option (a).** The second circle winds Earth $N = M_\oplus/m_p\approx3.6\times10^{51}$ times: the bundle over any enclosing sphere is the Hopf bundle taken $N$ times, the fiber pinches at every nucleus, and the connection outside carries $|F| = N/2r^2$. Topology of the extra dimension; nothing in the light sector sees it. The spatial Hopf circles of Part II still thread through Earth — two different structures called Hopf, one winding and one threading.

## III.5 Electromagnetism

$\mathcal{F}$ lives on $\mathcal{E}$, reduced on both circles: $\epsilon = 1/\mu = \psi$ from the first, $\epsilon\mu = 1$, light on null geodesics **[V]**; a Proca tower on each circle at $\hbar c/\psi_0$ and $\hbar c/L_{2,0}$ — both meV-scale if $w_2/w_1 = O(1)$ — unexcited by circle-smeared matter. The reduction on the second circle gives the standard result

$$\mathcal{F}_{\rm eff} = \mathcal{F}_B + \varphi\,F_\alpha$$

with $\varphi$ the fiber component of $\mathcal{A}$, and $\varphi_0 = 0$ because a constant would make every mass an electromagnetic magnetic monopole **[D]**. **The zero-mode photon does not couple to $\alpha$.**

## III.6 The photon is Hopf-neutral — the correction that reorganizes the second order [D]

In Kaluza–Klein reduction, a field's charge under the graviphoton is its momentum around the circle, $n$, independent of spin. A vector field on the total space gives base vectors $\mathcal{A}^{(n)}_\mu$, carrying *both* helicities at every $n$. The ordinary photon is $n = 0$. **Its helicity is not its Kaluza–Klein charge.** Version 3's identification of the two (§II.14.4 there, tagged [S]) was wrong, and with it fall the polarization-rotation law between lensed images, the $m_{\rm unit}\gtrsim10^{14}M_\odot$ bound, and the Poisson-spot exclusion of a particle-mass quantum.

What the second circle does to light, honestly: **nothing at the zero mode.** The distinctness principle — two paths at different fiber positions are physically distinct and interfere — is realized for the *charged Kaluza–Klein modes* on either circle: the Proca towers. That is real physics at the meV scale, and it is where Entry 8's idea lives. It is not a property of the light we see.

## III.7 The conformally-flat sector as a lemma [V]

For one monopole and its twin, the second-circle total space is conformally $\mathbb{C}^2\setminus\{0\}$, and the Hermitian condition locks the fiber length to the conformal factor of the base: $L_2 = \Omega\,L^{\rm ref}$, $g_B = \Omega^2g_{\rm ref}$, one function. Here the second dilaton is not an independent modulus — it is gravity's conformal factor, fixed by the Hamiltonian constraint — and the first circle's stabilization with the flux present is

$$\psi^2 = \frac{-2|\Lambda_6| + \sqrt{4\Lambda_6^2 + 6w_1^2L_2^4F^2}}{L_2^4F^2}\;\longrightarrow\;\frac{3w_1^2}{2|\Lambda_6|}\quad(F\to0)$$

a genuine minimum **[V]**. This is the sector in which v3's "$G_B = G[\Omega]$" holds and in which Law I is the second fiber's length equation as well as the spatial one's. Beyond it, §III.1's two-winding stabilization is what makes every quantity defined.

## III.8 The Lagrangian of version 5

$$S = \int_{\mathcal{E}}\sqrt{-g_6}\left[\frac{R_6 - 2\Lambda_6}{16\pi G_6} - \frac12(\nabla f_1)^2 - \frac12(\nabla f_2)^2\right] + \int\sqrt{-g}\left[-\frac14\mathcal{F}_{MN}\mathcal{F}^{MN} + \bar\Psi\big(i\Gamma^MD_M - m\big)\Psi\right]$$

Both circles enter alike: a winding scalar each, one cosmological constant, the metric carrying both graviphotons (the first set to zero by Frobenius, the second the field $\alpha$ sourced by monopoles). New constants relative to version 2: $w_2$ and $m_{\rm unit}$; $g_2$ is $1/L_{2,0}$ up to normalization and is not independent.

## III.9 Laws and axioms, version 5

> ### ■ ARENA
> - **A1.** $\mathcal{E} = \mathbb{R}_t\times S^1_u\times S^1_2\times S^3$, $S^3\cong SU(2)$; the two circles form an elliptic fiber with $\tau = iw_2/w_1$.
> - **A2.** Base $\mathbb{R}_t\times\mathbb{RP}^3$, $\mathbb{RP}^3\cong SO(3)$; disconnected fiber — **derived** (§II.1).
> - **A3.** $\Lambda_6<0$.

> ### ■ FIELDS
> - **A4.** Metric on $\mathcal{E}$; windings $f_1 = w_1u$, $f_2 = w_2\theta_2$; dilatons stabilized at $\psi_0^2 = 2w_1^2/|\Lambda_6|$, $L_{2,0}^2 = 2w_2^2/|\Lambda_6|$.
> - **A5.** $\mathcal{F}$ on $\mathcal{E}$; Dirac $\Psi$ on $\mathcal{E}$.
> - **A6.** Second-circle Chern number $\lfloor M/m_{\rm unit}\rfloor$ at each mass; $m_{\rm unit}$ a particle mass (option a) or $\sim10^{14}M_\odot$ (option c).

> ### ◆ LAW I — GRAVITY
> - **A7.** Source $S = T_+$. In the conformally-round sector $(\Delta+3)\delta\phi = -2\pi\delta\rho_+$ and $L_H = 2\pi\ell\phi^2$.

> ### ◆ LAWS II, II′ — THE FIBRATIONS
> - **A8.** $\Box f_i = 0$, $\oint df_i = \ln\lambda_i$; first graviphoton $A_\mu = 0$; second graviphoton $\alpha$ with $dF = \star J_-/m_{\rm unit}$.

> ### ◆ ELECTROMAGNETISM
> - **A9.** $d\mathcal{F} = 0$, $d\star\mathcal{F} = \star\mathcal{J}$ on $\mathcal{E}$; zero-mode photon neutral under both graviphotons.

> ### ▣ DERIVED
> - **D1–D5** as before (cone, no endpoints, static twin = quotient, Mach relation, $\gamma = 1$).
> - **D6.** Joint stabilization of two winding circles by one $\Lambda_6<0$; $L_{2,0}/\psi_0 = w_2/w_1$.
> - **D7.** The mirror: each circle's length sourced by matter averaged over the other; exact on the untwisted torus.
> - **D8.** A2 from $-1\in U(1)_{\rm Hopf}$ and non-privileging.
> - **D9.** Law I as the spatial fiber-length equation; twin inherited.
> - **D10.** Anti-monopole automatic; $\Gamma = \mathbb{Z}_2$ selected; partition theorem.
> - **D11.** Ordinary photon Hopf-neutral; distinctness lives in the Kaluza–Klein towers.

---

# PART IV — CORRECTIONS AND STATUS

## IV.1 Corrections to earlier versions

| claim | version | status | reason |
|:--|:--|:--|:--|
| helicity $=$ Hopf (KK) charge | v3 §II.14.4 | **retracted** | KK charge is circle momentum, spin-independent; the photon is $n = 0$ |
| polarization rotation $2\pi m_-/m_{\rm unit}$ between lensed images; $m_{\rm unit}\gtrsim10^{14}M_\odot$ | v3 §II.14.5 | **retracted** | depended on the above |
| Poisson-spot exclusion of a particle-mass $m_{\rm unit}$ | this session | **retracted** | same |
| anisotropic birefringence, $\lvert\Omega_k\rvert\lesssim10^{-5}$ | v4 §II.13 | **retracted** | nothing couples to the spatial Hopf structure |
| no joint stabilization of two fibers | v3 §II.16 | **corrected** | flux vs winding; two windings have a joint minimum (§III.1); and in the flat sector the second length is gravity's $\Omega$ (§III.7) |
| Tully–Fisher from closure, $a_0 = 4\pi G\Sigma$ | v2 | **reclassified as the idea-B toy** | it belongs to the reflection-sky arena ($\ell\approx8$ kpc, the galaxy filling a hemisphere), where it is the correct gravitational consequence of the antipodal magnifier $D_A = \ell\sin\chi$ — a turnover of the same shape as $\Lambda$CDM's at $z = 1.6$, with no expansion. It was always detachable from the cosmic arena, where $\Omega_k$ would be $3\times10^{11}$ and the plateau at 30 kpc is 2.5 km/s. What the idea-B arena still lacks is a redshift |
| the $S^4$ conformal root, $O(5)$ recentering, Easter eggs | v3 §II.13–17 | **retired** | belonged to the $4\pi\ell\sin\chi$ normalization; the GPS geometry replaces it |
| v4's contact structure as the second order | v4 | **retired** | inert: no coupling, no observables beyond Law I. Its two geometric results are kept (Part II) |

## IV.2 The ledger

| result | tag |
|:--|:--|
| $-1\in U(1)_{\rm Hopf}$; A2 derived from non-privileging | **[V/D]** |
| $(\Delta+3)\delta\phi = -2\pi\delta\rho_+$; $L_H = 2\pi\ell\phi^2$; twin to $10^{-11}$ | **[V]** |
| two-winding potential: joint minimum, Hessian $(\tfrac14,\tfrac12)$, $L_{2,0}/\psi_0 = w_2/w_1$ | **[V]** |
| $R_{uu}\leftrightarrow R_{\theta\theta}$ under $\psi\leftrightarrow L_2$: difference $0$ | **[V]** |
| flux-vs-winding: flux needs $\Lambda>0$, winding $\Lambda<0$; no mixed joint minimum | **[V]** |
| flat-sector locking: $\psi$ stabilized with flux present, $\to3w_1^2/2\lvert\Lambda_6\rvert$ | **[V]** |
| KK charge is circle momentum, spin-independent; photon $n = 0$ | **[T]** |
| anti-monopole automatic; $\Gamma = \mathbb{Z}_2$ only; partition theorem | **[V/D]** |
| galaxy arena $\Omega_k = 3\times10^{11}$; cosmic-arena plateau 2.5 km/s | **[V]** |
| Mercury: $g_2/m_{\rm unit}<0.024$ in option (a) | **[D]** |
| static $S^3$: $D_A = \ell\sin\chi$ turns over like $\Lambda$CDM's $D_A(z)$ at $z = 1.6$, without expansion | **[V]** |
| Earth winds the second circle $3.6\times10^{51}$ times in option (a) | **[D]** |
| Poisson-spot and lensing bounds do not apply to the zero-mode photon | **[D]** |

## IV.3 Open problems

1. **$g_2/m_{\rm unit}$** — now bounded below $0.024$ by Mercury (option a). Tightening it needs a system with larger $M/r$ than Mercury and a perihelion measured to better than $10^{-4}$: the double pulsar, or S2 at the Galactic center.
2. **Option (a) versus (c) for $m_{\rm unit}$** — particle mass or supercluster mass. Both light-blind; distinguishable only by the second-circle KK tower's phenomenology, if it can be produced.
3. **$w_2/w_1$** — the modular parameter. Nothing fixes it; $O(1)$ is natural and makes both towers meV-scale.
4. **A per-galaxy closed structure** — the only route by which Tully–Fisher from closure could apply to our universe.
5. **The meV towers** — the Proca modes on both circles are the second order's real physics and the home of the distinctness principle. What produces them, and whether the first circle's tower (v2's 4 meV) is already constrained.
6. **Inherited** — the AdS uplift ($10^{60}$); the rise beyond the equator; the literature review, now three versions overdue.

## IV.4 The next three moves

1. **Tighten $g_2/m_{\rm unit}$** below Mercury's $0.024$ using the double pulsar's periastron advance ($M/r$ larger, precision $10^{-5}$) — a computation, not a construction.
2. **Write the two-circle Proca phenomenology.** Two towers, one at 4 meV from the first circle. If the second is comparable, the distinctness principle has a laboratory scale.
3. **The literature review.** Kaluza–Klein monopoles, two-torus compactifications, and the $\mathbb{RP}^3$ quotient have each been studied; the combination has not been checked against what exists.

---

## Reference card, version 5

| topic | statement |
|:--|:--|
| **arena** | $\mathbb{R}_t\times S^1_u\times S^1_2\times S^3$; base $\mathbb{RP}^3$; elliptic fiber $\tau = iw_2/w_1$ |
| **seed** | matter at $p$, gravity at $\pm p$; A2 **derived** |
| **stabilization** | $\psi_0^2 = 2w_1^2/\lvert\Lambda_6\rvert$, $L_{2,0}^2 = 2w_2^2/\lvert\Lambda_6\rvert$; joint minimum |
| **mirror** | each circle's length $\leftarrow$ matter averaged over the other; exact |
| **Law I on fibers** | spatial: $L_H = 2\pi\ell\phi^2$, $(\Delta+3)\delta\phi = -2\pi\delta\rho_+$; second circle: the $\theta\theta$ component |
| **monopoles** | masses are GPS monopoles, Chern $\lfloor M/m_{\rm unit}\rfloor$; twin $-N$; $\Gamma = \mathbb{Z}_2$ |
| **dynamic sector** | $\alpha$ with $-\tfrac14L_2^2F^2$; $dF = \star J_-/m_{\rm unit}$; $P_{\rm eff} = g_2M/m_{\rm unit}$; **Mercury: $g_2/m_{\rm unit}<0.024$** |
| **photon** | zero mode, neutral under both circles; $\epsilon\mu = 1$; towers at $\hbar c/\psi_0$, $\hbar c/L_{2,0}$ |
| **distinctness** | realized for the KK towers, not for ordinary light |
| **retracted** | polarization law; $m_{\rm unit}$ lensing bound; Poisson kill; birefringence; TF (demoted); $S^4$ root |
| **open** | $g_2/m_{\rm unit}$; option a/c; $w_2/w_1$; per-galaxy closure; the towers |
