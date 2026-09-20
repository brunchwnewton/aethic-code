# Projective Gravity — Version 15.2

## Canonical Total Space First:
## the Complex Hopf Lift of Worldline Shells, a Derived Full Middle Space, and Two Base Spaces

> **Status.** Architectural draft. Version 15.2 corrects the hierarchy of v15 and replaces the provisional real-shell Hopf construction by its natural **complex-isotropic analogue**.
>
> **Axiomatic object.** The fundamental object is the **canonical total space**
> \[
> E.
> \]
> The full middle space is not fundamental. It is derived by quotienting the canonical spin/Hopf fiber:
> \[
> \boxed{
> E\xrightarrow{/\,U(1)_H}\mathcal M.
> }
> \]
> Analytically, the corresponding complex construction is modeled shellwise by
> \[
> \boxed{
> \mathbb C^\times
> \longrightarrow
> SL(2,\mathbb C)
> \longrightarrow
> Q_{\rm aff}^2
> \cong
> SL(2,\mathbb C)/\mathbb C^\times.
> }
> \]
> The ordinary Hopf fibration is its compact real form:
> \[
> \boxed{
> U(1)
> \longrightarrow
> SU(2)\simeq S^3
> \longrightarrow
> S^2.
> }
> \]
>
> **Why this is the right replacement for the old Hopf shell.** A shell of fixed nonzero complex radius around a complex worldline is not a real \(S^2\). In the complexified three-dimensional normal space it is an affine complex quadric
> \[
> \Sigma_{\gamma,R}^{\mathbb C}
> =
> \{\xi:g_{\mathbb C}(\xi,\xi)=R^2,\;
> g_{\mathbb C}(\xi,\dot\gamma)=0\},
> \]
> a complex surface. After rescaling \(R\), its isotropic homogeneous model is
> \[
> Q_{\rm aff}^2\simeq SL(2,\mathbb C)/\mathbb C^\times.
> \]
> Thus the complex spin group itself supplies the shell's canonical total-space lift. On the physical Lorentzian real slice about a timelike worldline, the normal space becomes ordinary Euclidean \(\mathbb R^3\), the shell becomes \(S^2\), \(SL(2,\mathbb C)\) reduces to its compact spatial spin subgroup \(SU(2)\), and the fiber becomes the usual \(U(1)\) Hopf circle.
>
> **The resulting division of labor**
> \[
> \boxed{
> \begin{array}{rcl}
> SL(2,\mathbb C) &:& \text{complex-isotropic spin lift of a complex shell},\\
> \mathbb C^\times &:& \text{complexified axial/spin-fiber stabilizer},\\
> SU(2) &:& \text{physical compact spin lift},\\
> U(1)_H &:& \text{physical Hopf/spin phase fiber},\\
> \text{Law I} &:& \text{metric length of that physical fiber},\\
> \text{Law III candidate} &:& \text{its connection/odd-placement content}.
> \end{array}
> }
> \]
>
> The crucial point is that the Hopf character is no longer topological decoration. It is the **compact real form of the complex spin homogeneous space appropriate to an isotropic complex shell**.
>
> **The two base spaces.** After the first quotient produces the full middle space \(\mathcal M\), that middle space has two physically distinct four-dimensional readouts:
>
> - the **representational base space** \(B_{\rm rep}\), where matter and light are localized;
> - the **quotiented base space** \(B_{\rm grav}\), obtained by quotienting the middle-space meridians and used by gravity.
>
> Therefore
> \[
> \boxed{
> E
> \xrightarrow{/\,U(1)_H}
> \mathcal M
> \quad
> \begin{matrix}
> \supset B_{\rm rep}\\[-2pt]
> \downarrow /\,U_{\rm mer}
> \end{matrix}
> \quad
> B_{\rm grav}.
> }
> \]
>
> **The seed**
>
> > **Light resolves a representative in \(B_{\rm rep}\); gravity resolves only its meridian class in \(B_{\rm grav}\).**
>
> **The axiom order**
>
> > **Canonical total space first. Full middle space second. The two base spaces third.**
>
> **Tags.** **[T]** standard/cited mathematics or physics · **[D]** derived from the adopted definitions · **[S]** structural proposal/sketch · **[O]** open · **[R]** retired.

---

# PART 0 — THE CORRECTED HIERARCHY

## 0.1 Four layers, not three

The v15.2 hierarchy is:

\[
\boxed{
\text{canonical total space}
\to
\text{full middle space}
\to
\begin{cases}
\text{representational base}\\
\text{quotiented gravity base}
\end{cases}
}
\]

More precisely,

\[
\boxed{
E
\xrightarrow{\pi_H}
\mathcal M=E/U(1)_H.
}
\]

The full middle space carries a one-dimensional real meridian foliation \(U_{\rm mer}\). Its quotient is

\[
\boxed{
q:\mathcal M\to B_{\rm grav}
=
\mathcal M/U_{\rm mer}.
}
\]

The representational base is instead an embedded resolved hypersurface,

\[
\boxed{
\iota:B_{\rm rep}\hookrightarrow\mathcal M.
}
\]

The two base spaces have the same physical dimension but arise by fundamentally different operations:

\[
\boxed{
B_{\rm rep}=\text{resolved representative},
\qquad
B_{\rm grav}=\text{equivalence class}.
}
\]

---

## 0.2 Dimensions in the physical real form

The intended physical dimensions are

\[
\dim_{\mathbb R}B_{\rm rep}=4,
\]

\[
\dim_{\mathbb R}\mathcal M=5,
\]

\[
\dim_{\mathbb R}E=6,
\]

\[
\dim_{\mathbb R}B_{\rm grav}=4.
\]

Thus

\[
\boxed{
E^{(6)}
\xrightarrow{/U(1)}
\mathcal M^{(5)}
\xrightarrow{/U_{\rm mer}}
B_{\rm grav}^{(4)}
}
\]

while

\[
\boxed{
B_{\rm rep}^{(4)}
\hookrightarrow
\mathcal M^{(5)}.
}
\]

The complex shell geometry used to define the first lift is not obtained by naively doubling this dimension count. It is the analytic continuation of the **local shell structure** and is described separately in Part II.

---

## 0.3 What is axiomatic

The primitive data are provisionally

\[
\boxed{
(E,\hat g,\mathcal A_H,\rho_E,\mathcal U_{\rm mer},\ldots).
}
\]

Here:

- \(E\) is the canonical total space;
- \(\hat g\) is its physical metric;
- \(U(1)_H\) is the compact physical fiber action;
- \(\mathcal A_H\) is the corresponding principal connection;
- \(\rho_E\) denotes the analytic/real-structure data needed to extend to complexified shells;
- \(\mathcal U_{\rm mer}\) is the meridian structure after the Hopf quotient.

The full middle space is then

\[
\mathcal M=E/U(1)_H.
\]

Thus the theory is explicitly **top-down**.

It does not posit \(\mathcal M\) and then decorate it with a circle.

---

# PART I — THE REPRESENTATIONAL BASE

## I.1 Ordinary Lorentzian spacetime remains the conservative stopping point [T/S]

The representational base is a four-dimensional Lorentzian spin spacetime

\[
(B_{\rm rep},g_{\rm rep}),
\qquad
\operatorname{sig}(g_{\rm rep})=(-,+,+,+).
\]

Matter and Maxwell fields are localized here.

A detector event is

\[
x\in B_{\rm rep}.
\]

The representational base is therefore the operational spacetime of optical and material localization.

Where Newman–Janis is used, \(B_{\rm rep}\) is assumed real-analytic and extended locally to

\[
B_{{\rm rep},\mathbb C}.
\]

No twistor space is fundamental.

---

## I.2 Newman–Penrose spinors live here [T]

A Newman–Penrose null tetrad

\[
(\ell^a,n^a,m^a,\bar m^a)
\]

can be generated from a two-spinor dyad

\[
(o^A,\iota^A)
\]

by

\[
\ell^{AA'}=o^A\bar o^{A'},
\qquad
n^{AA'}=\iota^A\bar\iota^{A'},
\]

\[
m^{AA'}=o^A\bar\iota^{A'},
\qquad
\bar m^{AA'}=\iota^A\bar o^{A'}.
\]

This is sufficient for:

- null propagation;
- Weyl spinors;
- Petrov classification;
- principal null directions;
- Maxwell scalars;
- the repeated principal null congruences of Kerr.

Twistor theory may later encode special congruences, but none is required to define the v15.2 arena.

---

## I.3 Time [S/O]

Time is not appended as a fundamental factor

\[
\mathbb R_t.
\]

The physical representational base is selected as a Lorentzian real form of the analytic geometry.

Thus

\[
\boxed{
\text{time belongs to the Lorentzian real structure}.
}
\]

Version 15.2 does not yet claim to have derived the uniqueness of that real structure.

That remains an explicit open problem.

---

# PART II — COMPLEX WORLDLINES AND THEIR ISOTROPIC SHELLS

## II.1 The complex worldline [T/S]

Let

\[
\Gamma_{\mathbb C}
=
\{\gamma(\tau)\}
\subset
B_{{\rm rep},\mathbb C}
\]

be the analytic complex worldline associated with a source.

Assume its tangent is non-null in the region under consideration:

\[
g_{\mathbb C}(\dot\gamma,\dot\gamma)\neq0.
\]

At \(\gamma(\tau)\), define the complex normal space

\[
N_\gamma
=
\{\xi:
g_{\mathbb C}(\xi,\dot\gamma)=0\}.
\]

This is complex three-dimensional.

It is the complexification of the ordinary spatial rest space about a timelike real worldline.

---

## II.2 A complex shell is an affine quadric [T]

A shell of nonzero complex squared radius \(R^2\) is

\[
\boxed{
\Sigma_{\gamma,R}^{\mathbb C}
=
\{
\xi\in N_\gamma:
g_{\mathbb C}(\xi,\xi)=R^2
\}.
}
\]

After choosing an orthonormal complex frame in \(N_\gamma\) and rescaling \(R\neq0\),

\[
\Sigma_{\gamma,R}^{\mathbb C}
\cong
Q_{\rm aff}^2
=
\{
(z_1,z_2,z_3)\in\mathbb C^3:
z_1^2+z_2^2+z_3^2=1
\}.
\]

This is a **complex surface**, not a real two-sphere.

Its rotational symmetry is the complex rotation group

\[
SO(3,\mathbb C),
\]

and its spin double cover is

\[
Spin(3,\mathbb C)
\cong
SL(2,\mathbb C).
\]

---

## II.3 The complex Hopf analogue [T]

The affine complex quadric is the homogeneous space

\[
\boxed{
Q_{\rm aff}^2
\cong
SL(2,\mathbb C)/\mathbb C^\times,
}
\]

where \(\mathbb C^\times\) is the diagonal complex torus stabilizing a chosen direction.

Therefore there is a canonical principal bundle

\[
\boxed{
\mathbb C^\times
\hookrightarrow
SL(2,\mathbb C)
\twoheadrightarrow
Q_{\rm aff}^2.
}
\]

This is adopted as the **complex Hopf shell** of v15.2.

It is the correct sense in which the old Hopfian character survives complexification.

It is not obtained by pretending the complex shell is still \(S^2\).

It is obtained by complexifying the homogeneous-space relation itself.

---

## II.4 The physical real form is exactly Hopf [T]

For a timelike source on the physical Lorentzian real slice, the normal rest space is ordinary Euclidean three-space.

Then

\[
Q_{\rm aff}^2
\quad\longrightarrow\quad
S^2,
\]

the compact spin group is

\[
SL(2,\mathbb C)
\quad\longrightarrow\quad
SU(2)\simeq S^3,
\]

and

\[
\mathbb C^\times
\quad\longrightarrow\quad
U(1).
\]

Hence

\[
\boxed{
U(1)
\hookrightarrow
SU(2)\simeq S^3
\twoheadrightarrow
S^2.
}
\]

The old statement

> “every spherical shell lifts to a Hopf \(S^3\)”

is therefore recovered **as the physical real form of the new complex-isotropic statement**, rather than imposed before complexification.

---

## II.5 Why this is isotropic [T/D]

The shell is defined only by the invariant quadratic condition

\[
g_{\mathbb C}(\xi,\xi)=R^2.
\]

The complex rotation group acts transitively on it.

No angular direction is preferred.

The canonical shell lift is likewise homogeneous:

\[
SL(2,\mathbb C)
\to
SL(2,\mathbb C)/\mathbb C^\times.
\]

Thus the fiber is not attached by choosing a special longitude on a complex shell.

It is the stabilizer fiber of the spin-group action itself.

On the physical real form,

\[
SU(2)\to SU(2)/U(1)\simeq S^2
\]

is equally isotropic under ordinary rotations.

This is the sense in which the new construction preserves the magnetic/isotropic motivation of the original Hopf picture.

---

# PART III — WHY THIS FIBER IS NOT BOLTED ON

## III.1 The same spin group already underlies NP [T]

The group

\[
SL(2,\mathbb C)
\]

is not introduced solely to manufacture a shell bundle.

It is already the spin group underlying four-dimensional Lorentzian two-spinor geometry.

Thus the same algebraic object occurs in two places:

\[
\boxed{
SL(2,\mathbb C)
=
\text{spacetime spin group}
}
\]

and

\[
\boxed{
SL(2,\mathbb C)
=
\text{complex-isotropic total shell over }
Q_{\rm aff}^2.
}
\]

Version 15.2 treats this coincidence as structural evidence that the canonical shell fiber is closer to the correct type than the ad hoc \(U(1)\) of earlier versions.

It is not yet a proof that all of the canonical total space must be a spin bundle.

---

## III.2 The fiber's compact part is the spin/Hopf phase [T/S]

The complex fiber is

\[
\mathbb C^\times
\simeq
\mathbb R_+\times U(1)
\]

as a real Lie group.

The \(U(1)\) factor is the compact physical phase/stabilizer that survives on the real shell.

The \(\mathbb R_+\) factor belongs to complex scaling and is not interpreted as an additional compact physical dimension.

Thus the physical canonical fiber remains one circle:

\[
\boxed{
U(1)_H.
}
\]

This is exactly the dimensional economy wanted from v6.

---

## III.3 NP determines the type; gravity determines the metric size [S]

Spin geometry fixes the group and topology:

\[
U(1)_H
\hookrightarrow
SU(2)
\to
S^2.
\]

It does **not** determine a physically variable circumference for the \(U(1)\) orbit.

That is separate metric information.

Version 15.2 therefore imposes the division

\[
\boxed{
\text{spin geometry determines the fiber type;}
\qquad
\text{gravity determines its length.}
}
\]

This is the central bridge back to v6.

---

# PART IV — THE CANONICAL TOTAL SPACE

## IV.1 Axiom 0 [S/O]

The canonical total space \(E\) is the physical real form of an analytic spin-fibered geometry satisfying:

1. its quotient by \(U(1)_H\) is the full middle space,
   \[
   \mathcal M=E/U(1)_H;
   \]
2. near a source worldline, its analytic continuation restricted to every nonzero complex-radius shell is locally the complex homogeneous bundle
   \[
   \mathbb C^\times
   \to
   SL(2,\mathbb C)
   \to
   Q_{\rm aff}^2;
   \]
3. on the physical rest-space shell this reduces to
   \[
   U(1)
   \to
   SU(2)
   \to
   S^2;
   \]
4. the fiber has a canonical connection \(\mathcal A_H\);
5. the total-space metric \(\hat g\) gives the compact physical fiber a length \(L_H\).

The global existence and uniqueness of such an \(E\) over the complete middle geometry remain open.

---

## IV.2 The full middle space is derived [D]

The full middle space is

\[
\boxed{
\mathcal M
=
E/U(1)_H.
}
\]

Nothing in v15.2 is allowed to treat \(\mathcal M\) as more fundamental than \(E\).

The quotient discards the compact spin/Hopf phase while retaining the meridian-completed localization geometry.

This is the first information loss in the tower.

---

## IV.3 The first quotient versus the second quotient

There are two distinct quotients.

### Hopf/spin quotient

\[
\boxed{
E
\xrightarrow{/U(1)_H}
\mathcal M.
}
\]

What is forgotten: compact spin/Hopf phase.

### Gravitational meridian quotient

\[
\boxed{
\mathcal M
\xrightarrow{/U_{\rm mer}}
B_{\rm grav}.
}
\]

What is forgotten: where along the gravitational meridian the resolved matter sits.

These must not be conflated.

---

# PART V — THE TWO BASE SPACES

## V.1 The representational base [S]

The representational base is a Lorentzian hypersurface

\[
\boxed{
\iota:B_{\rm rep}\hookrightarrow\mathcal M.
}
\]

It is where:

- matter is localized;
- Maxwell fields are localized;
- detectors receive light;
- Newman–Janis is interpreted through the corresponding analytic continuation.

The representational base resolves a point on a meridian.

---

## V.2 It is generically a bisection [S/O]

The old \(S^4\) seed had an equatorial \(S^3\) meeting one meridian at two points

\[
\hat n,
\qquad
-\hat n.
\]

The abstract replacement is

\[
L_b\cap B_{\rm rep}
=
\{x,\tau x\},
\]

with

\[
\tau^2=1
\]

and

\[
q(x)=q(\tau x)=b.
\]

Thus \(B_{\rm rep}\) is more accurately a **bisection** than a one-point-per-fiber section.

The second point can be barren.

---

## V.3 The quotiented base [S]

The gravity base is

\[
\boxed{
B_{\rm grav}
=
\mathcal M/U_{\rm mer}.
}
\]

Gravity does not ask which representative in

\[
q^{-1}(b)
\]

contains the matter.

It asks only for the reduced source assigned to the class \(b\).

---

# PART VI — LAW I AS THE HOPF-FIBER-LENGTH EQUATION

## VI.1 Gravity on the quotiented base [S]

Einstein dynamics is imposed on

\[
B_{\rm grav}:
\]

\[
\boxed{
G_{\mu\nu}[g_G]
+
\Lambda g^G_{\mu\nu}
=
8\pi G_N T^{(g)}_{\mu\nu}.
}
\]

The gravitational source is obtained by meridian reduction of resolved matter.

In the discrete twin limit,

\[
\boxed{
T^{(g)}_{\mu\nu}([x])
=
T_{\mu\nu}(x)
+
T_{\mu\nu}(\tau x).
}
\]

The fully covariant tensor pushforward remains to be derived from the action.

---

## VI.2 Gravity constrains the canonical fiber length [S]

The canonical total-space metric is required to assign a physical circumference to the compact \(U(1)_H\) orbit.

In the conformal/static sector retain the v6 relation

\[
\boxed{
L_H
=
\Omega L_H^{\rm ref},
}
\]

where the quotient spatial metric is written

\[
g_{\rm spatial}
=
\Omega^2 g_{\rm ref}
\]

or, equivalently in the old notation,

\[
g_3=\phi^4g_{\rm ref},
\qquad
\Omega=\phi^2.
\]

In the weak field,

\[
\boxed{
\frac{\delta L_H}{L_H}
=
-\Phi.
}
\]

The interpretation is now cleaner than in v6:

> gravity does not create the \(U(1)\) fiber; the spin geometry supplies it. Gravity determines its metric size.

A future action should derive this locking rather than leave it as an independent rule.

---

## VI.3 The old degree-of-freedom split survives on the physical real shell [S]

On a real physical \(S^2\) shell, its canonical lift is \(S^3\).

A three-dimensional metric has six independent components.

Relative to the bundle decomposition, these split as

\[
\boxed{
6=3+1+2.
}
\]

Interpretation:

| block | count | candidate content |
|:--|--:|:--|
| shell 2-metric | 3 | even gravitational geometry |
| Hopf fiber length | 1 | even gravitational scale \(L_H\) |
| connection cross-terms | 2 | odd/placement sector |

Thus v6's attractive partition can survive **on the physical real slice**.

Version 15.2 does not naively assert a \(3+1+2\) count for the full complex shell. The complex homogeneous bundle is its analytic parent; the real slice is where the physical metric count is performed.

---

# PART VII — THE CONNECTION AND THE OLD SECOND ORDER

## VII.1 The canonical connection [T/S]

A principal \(U(1)\) bundle carries a connection

\[
\mathcal A_H
\]

with curvature

\[
F_H=d\mathcal A_H.
\]

On a symmetric physical shell, the reference connection is the ordinary Hopf connection.

Analytically it extends to the \(\mathbb C^\times\) connection on the complex homogeneous lift.

---

## VII.2 Candidate odd-placement law [S/O]

The old v6 second-order law was

\[
dF
=
2\pi\star J_-,
\]

with odd/twin-asymmetric matter sourcing the connection sector.

Version 15.2 retains this only as a **candidate**:

\[
\boxed{
dF_H
\stackrel{?}{=}
2\pi\star J_-.
}
\]

The reason for retaining it is now stronger than before:

- the connection is no longer attached to an arbitrary circle bundle;
- the circle is the compact real fiber of the complex spin-shell lift;
- the real-shell metric naturally leaves exactly two connection components beyond the base metric and fiber length.

What remains unproved is why \(T_-\) or \(J_-\) must source this particular connection.

That bridge is open.

---

## VII.3 Magnetic interpretation [S]

The magnetic analogy is geometric, not merely verbal.

The physical compact fiber is \(U(1)\).

Its connection can have nontrivial holonomy and curvature.

The complex parent is the \(\mathbb C^\times\) stabilizer inside the complex spin lift.

The construction is rotationally isotropic on the real shell and \(SO(3,\mathbb C)\)-homogeneous on the complex shell.

This is the precise v15.2 meaning of **analogue-isotropy**.

---

# PART VIII — NEWMAN–JANIS AND KERR

## VIII.1 Kerr remains a representational-base complex deformation [T]

The Newman–Janis construction acts on the complexification of the four-dimensional representational base.

Schematically,

\[
\boxed{
B_{\rm rep}
\hookrightarrow
B_{{\rm rep},\mathbb C}
\xrightarrow{\text{complex shift}}
B_{{\rm rep},\mathbb C}
\xrightarrow{\text{real slice}}
B_{\rm rep}^{\rm Kerr}.
}
\]

For Schwarzschild,

\[
a\to0
\quad\Rightarrow\quad
\text{Kerr}\to\text{Schwarzschild}.
\]

The spin parameter is

\[
a=J/M.
\]

---

## VIII.2 The canonical shells follow the complex worldline [S]

If the source center is represented by a complex worldline

\[
\Gamma_{\mathbb C},
\]

then the canonical shell construction is centered on that worldline.

At every worldline point and radius,

\[
\Sigma_{\gamma,R}^{\mathbb C}
\cong
Q_{\rm aff}^2
\]

and its lift is

\[
SL(2,\mathbb C).
\]

Thus Kerr's complex displacement moves the **center of the entire complex-isotropic shell system**.

It does not require interpreting rotation as literal winding around the Hopf fiber.

This keeps the roles separate:

\[
\boxed{
\text{Kerr rotation}
=
\text{complex worldline displacement},
}
\]

\[
\boxed{
\text{Hopf fiber}
=
\text{spin/isotropy lift of the shell}.
}
\]

---

## VIII.3 Why this is better than v14's \(TS^4\) picture

Version 14 tried to interpret Kerr as lifting a source off the zero section of a tangent bundle.

Version 15.2 instead says:

- complexified spacetime handles the Newman–Janis move;
- \(SL(2,\mathbb C)\) spin geometry handles the isotropic shell lift;
- the meridian structure handles the dark-matter seed;
- Einstein dynamics handles fiber length.

No one construction is asked to do all four jobs.

---

## VIII.4 The \(g=2\) signpost [T/O]

Kerr–Newman satisfies

\[
J=Ma,
\qquad
\mu=Qa,
\]

hence

\[
\mu=\frac{Q}{M}J,
\]

the conventional \(g=2\) relation.

Complex-worldline approaches to Einstein–Maxwell theory provide a further reason to keep the complex center structure visible.

Version 15.2 treats this as a **future bridge target**, not a derivation of the electron.

---

# PART IX — LIGHT VERSUS GRAVITY

## IX.1 Light resolves before the meridian quotient [S/T]

Matter and Maxwell fields live on

\[
B_{\rm rep}.
\]

An optical event is

\[
x\in B_{\rm rep}.
\]

Light therefore distinguishes

\[
x
\neq
\tau x.
\]

The electromagnetic field is not meridian-averaged.

---

## IX.2 Gravity sources after the meridian quotient [S]

Gravity first applies

\[
q:\mathcal M\to B_{\rm grav}.
\]

Thus

\[
q(x)=q(\tau x).
\]

The conceptual operation is

\[
\boxed{
T_{\rm resolved}
\xrightarrow{q_*}
T_{\rm grav}
\xrightarrow{\rm Einstein}
g_G
\xrightarrow{q^*}
g_{\rm resolved}^{\rm grav}.
}
\]

In shorthand,

\[
\boxed{
\text{gravity}
=
q^*
\circ
{\rm Einstein}
\circ
q_*.
}
\]

---

## IX.3 The barren twin [D/S]

Take

\[
T(x)\neq0,
\qquad
T(\tau x)=0.
\]

The quotiented source is nevertheless

\[
T^{(g)}([x])
=
T(x).
\]

The gravity metric solved at \([x]\) lifts to both resolved representatives.

Therefore

\[
\boxed{
T(\tau x)=0
\quad\text{while}\quad
\text{gravitational curvature at }\tau x\neq0.
}
\]

This is the seed.

No dark particle has been placed at the twin.

The discrepancy is a difference in **resolution**.

---

# PART X — STATIC \(S^4\) REGRESSION

## X.1 The old geometry must be recovered, not assumed [S/O]

The intended static real specialization is

\[
\boxed{
\mathcal M_{\rm static}
\sim
\mathbb R_t\times S^4
}
\]

at the level of the derived full middle space.

The representational base becomes

\[
\boxed{
B_{\rm rep}^{\rm static}
\sim
\mathbb R_t\times S^3,
}
\]

and the quotient base becomes

\[
\boxed{
B_{\rm grav}^{\rm static}
\sim
\mathbb R_t\times\mathbb{RP}^3.
}
\]

Spatially,

\[
S^3
\hookrightarrow
S^4
\xrightarrow{/\,\text{meridians}}
\mathbb{RP}^3.
\]

Above every physical \(S^2\) shell in the representational geometry sits the compact real canonical shell

\[
S^3
\]

through

\[
U(1)\to S^3\to S^2.
\]

Thus the full v6 picture is recovered as the **compact real/static specialization** of the new complex spin-shell architecture.

---

## X.2 Orbit laws are regression tests [O]

The old closed-universe orbit laws, closure relation, and \(v^2\) family do not automatically survive an architectural rewrite.

They must be recovered in this order:

1. derive the static real form of the middle space;
2. recover the meridian quotient;
3. derive the quotient metric and Green function;
4. recover the old geodesic/orbit equations;
5. only then reassert the \(v^2\) family.

This is a regression test, not an assumption.

---

# PART XI — WHAT THE COMPLEX SHELL IS NOT

## XI.1 Not merely the projectivized null cone

At a point of fully complexified four-dimensional spacetime, the projectivized complex null cone is a different useful object, a projective quadric related to two independent chiral projective spinors.

That object is natural for **null directions**.

The shell used here instead represents **fixed nonzero complex spatial radius in the complexified rest space of a non-null worldline**.

Thus:

\[
\boxed{
\text{null-direction quadric}
\neq
\text{fixed-radius worldline shell}.
}
\]

Version 15.2 uses the latter for the canonical shell lift.

This prevents a type confusion between optical null directions and spatial shells around the source.

---

## XI.2 Why the affine quadric is preferable here

The fixed-radius shell has exactly the desired real limit:

\[
Q_{\rm aff}^2
\rightsquigarrow
S^2.
\]

Its spin-homogeneous lift has exactly the desired real limit:

\[
SL(2,\mathbb C)
\rightsquigarrow
SU(2)\simeq S^3.
\]

Its fiber has exactly the desired real limit:

\[
\mathbb C^\times
\rightsquigarrow
U(1).
\]

So the three pieces complexify together:

\[
\boxed{
\begin{array}{ccc}
\mathbb C^\times &\to& SL(2,\mathbb C)\\
&&\downarrow\\
&&Q_{\rm aff}^2
\end{array}
}
\]

becomes

\[
\boxed{
\begin{array}{ccc}
U(1)&\to&S^3\\
&&\downarrow\\
&&S^2.
\end{array}
}
\]

That is the isotropic complex analogue sought here.

---

# PART XII — CATEGORY FIREWALL

## XII.1 Spin geometry does not yet derive Grassmann parity [T]

The appearance of \(SL(2,\mathbb C)\), \(SU(2)\), and spinors does not derive quantum fermionic statistics.

NP spinors are classical commuting geometric spinors.

Grassmann-odd quantum fields are a further quantum/statistical structure.

Therefore

\[
\boxed{
\text{spinorial shell geometry}
\not\Rightarrow
\text{fermionic anticommutation}.
}
\]

Any such derivation remains open.

---

## XII.2 What can legitimately emerge geometrically

The new canonical total space may plausibly constrain:

- spin structures;
- phase holonomy;
- chirality;
- principal spinors;
- allowed bundle connections;
- topological charge;
- geometric relations among mass, charge, and rotation;
- the availability of particular zero modes.

Those are the appropriate next targets.

---

# PART XIII — MINIMAL LAW SET

## LAW 0 — CANONICAL TOTAL SPACE [S/O]

There exists a canonical total space \(E\) whose local analytic shell geometry around every admissible complex source worldline is the complex Hopf homogeneous bundle

\[
\boxed{
\mathbb C^\times
\to
SL(2,\mathbb C)
\to
SL(2,\mathbb C)/\mathbb C^\times.
}
\]

Its physical compact real shell is

\[
\boxed{
U(1)\to SU(2)\to S^2.
}
\]

The full middle space is derived by quotienting the physical \(U(1)\) fiber.

---

## LAW I — GRAVITY [S]

Einstein dynamics is imposed on the quotiented base

\[
B_{\rm grav}
=
\mathcal M/U_{\rm mer}
\]

with meridian-reduced source.

The same gravitational solution constrains the canonical Hopf-fiber length:

\[
\boxed{
L_H=\Omega L_H^{\rm ref}
}
\]

in the conformal/static sector.

---

## LAW II — MERIDIANS [S/O]

The derived full middle space carries a one-dimensional meridian foliation \(U_{\rm mer}\).

The representational base resolves its representatives.

Gravity quotients it.

In the static spherical limit this structure must reduce to the great-circle meridians of \(S^4\) with quotient \(\mathbb{RP}^3\).

The general dynamical equation selecting the meridians remains open.

---

## LAW III — CONNECTION / ODD SECTOR [O]

The canonical Hopf connection is \(\mathcal A_H\) with

\[
F_H=d\mathcal A_H.
\]

The candidate old odd-sector law is

\[
dF_H
\stackrel{?}{=}
2\pi\star J_-.
\]

This is not promoted to a law until the source coupling is derived.

---

## LAW IV — LIGHT [T/S]

Maxwell and matter fields live on \(B_{\rm rep}\).

Light resolves meridian representatives and does not perform the gravity quotient.

---

# PART XIV — THE DEGREE-OF-FREEDOM TARGET

The old v6 counting was attractive because on each real shell the total metric data split naturally into

\[
\boxed{
6=3+1+2.
}
\]

Version 15.2 gives those slots cleaner geometric names:

\[
\boxed{
\begin{array}{ccl}
3&=&\text{metric of the physical shell }S^2,\\
1&=&\text{metric length of the spin/Hopf }U(1),\\
2&=&\text{connection cross-terms}.
\end{array}
}
\]

The intended assignment remains

\[
\boxed{
T_+
\longrightarrow
(3+1)
}
\]

and

\[
\boxed{
T_-
\longrightarrow
2.
}
\]

But only the first half is currently structurally motivated:

- quotient gravity determines the even base geometry;
- Law I locks the Hopf-fiber length to it.

The second half remains a conjecture until odd matter is shown to source the canonical connection.

---

# PART XV — THE ACTION TARGET

A successful action should make both information reductions automatic.

Schematically,

\[
S
=
S_{\rm EH}[B_{\rm grav},g_G]
+
S_{\rm matter}[B_{\rm rep},\psi,A;\ldots]
+
S_{\rm can}[E,\hat g,\mathcal A_H,U_{\rm mer};\ldots].
\]

Variation with respect to \(g_G\) should produce the meridian-reduced source.

Variation or constraint equations involving the canonical metric should produce the fiber-length locking.

The connection equation should either derive the old \(J_-\) law or show that it was the wrong use of the remaining degrees of freedom.

Until such an action exists, the split is architectural rather than final.

---

# PART XVI — REQUIRED TESTS

1. **Global canonical space.** Construct an explicit \(E\) whose shell restrictions are the stated \(SL(2,\mathbb C)\) homogeneous lifts and whose physical quotient is a smooth five-dimensional middle space away from controlled singular loci.
2. **Real structure.** Show explicitly how the complex shell bundle reduces to \(U(1)\to SU(2)\to S^2\) on the Lorentzian physical slice.
3. **Worldline covariance.** Define the complex normal bundle and shell lift covariantly along a general non-null complex worldline.
4. **Kerr regression.** Perform Schwarzschild \(\to\) Kerr by Newman–Janis or equivalent complex-worldline methods while carrying the canonical shell lift consistently.
5. **Fiber-length law.** Derive rather than merely impose \(L_H=\Omega L_H^{\rm ref}\).
6. **Connection law.** Determine whether \(T_-\) genuinely occupies the two real connection degrees of freedom.
7. **Meridian construction.** Derive the one-dimensional middle-space meridian foliation from canonical data.
8. **Static \(S^4\) regression.** Recover \(S^4\to\mathbb{RP}^3\) and the barren twin.
9. **Orbit regression.** Re-derive the old \(v^2\) family in the recovered static sector.
10. **Dark-sector calculation.** Compute what stress-energy a local observer would infer by applying Einstein's equation on the representational base instead of the quotiented base.
11. **Electromagnetic separation.** Verify that the twin remains optically/electromagnetically barren.
12. **Spin-statistics firewall.** Do not identify the geometric spin lift with Grassmann parity without a separate quantum derivation.

---

# PART XVII — WHAT v15.2 RETIRES

| previous idea | v15.2 verdict |
|:--|:--|
| full middle space as the axiom | **[R]** — it is derived from the canonical total space |
| representational “middle space” terminology | **[R]** — it is the representational **base space** |
| quotiented “middle space” terminology | **[R]** — it is the quotiented **base space** |
| real \(S^2\) shell used before complexification | **[R]** at the analytic level |
| provisional \(\mathbb{CP}^1_L\times\mathbb{CP}^1_R\) bi-Hopf shell as the default | **[R]** for fixed-radius source shells; that projective quadric belongs to null/projective-direction geometry |
| \(TS^4\) as the canonical arena | **[R]** |
| external fundamental \(\mathbb R_t\) | **[R]** |
| Hopf fiber as Kerr rotation itself | **[R]** |
| arbitrary extra \(U(1)\) with no spin-geometric origin | **[R]** |
| geometric Weyl spinor \(\Rightarrow\) quantum Grassmann fermion | **[R]** |

---

# PART XVIII — WHAT v15.2 RECOVERS FROM v6

Version 6 had the durable insight that a physical \(S^2\) shell about a secondary could lift to a Hopf \(S^3\), with total-space metric data splitting into

\[
3+1+2.
\]

It also treated gravity on the meridian quotient and matter/light on the resolved geometry.

Version 15.2 keeps both ideas but changes their foundation.

The old real Hopf shell

\[
U(1)\to S^3\to S^2
\]

is now the compact real form of

\[
\boxed{
\mathbb C^\times
\to
SL(2,\mathbb C)
\to
Q_{\rm aff}^2.
}
\]

Thus the original Hopfian intuition survives, but at a deeper and more natural level.

---

# PART XIX — REFERENCE CARD, VERSION 15.2

| topic | statement |
|:--|:--|
| **axiom** | canonical total space \(E\), not the middle space |
| **first quotient** | \(E/U(1)_H=\mathcal M\), the full middle space |
| **representational base** | \(B_{\rm rep}\hookrightarrow\mathcal M\), Lorentzian spacetime where matter/light localize |
| **gravity base** | \(B_{\rm grav}=\mathcal M/U_{\rm mer}\) |
| **seed** | distinct resolved representatives lie on one gravity meridian |
| **complex source shell** | fixed-radius affine complex quadric \(Q_{\rm aff}^2\) in the complexified normal 3-space |
| **complex Hopf analogue** | \(\mathbb C^\times\to SL(2,\mathbb C)\to SL(2,\mathbb C)/\mathbb C^\times\cong Q_{\rm aff}^2\) |
| **physical Hopf shell** | \(U(1)\to SU(2)\simeq S^3\to S^2\) |
| **why isotropic** | shell and lift are homogeneous under \(SO(3,\mathbb C)\) / \(SL(2,\mathbb C)\); no direction selected |
| **why spinorial** | the total shell uses the same \(SL(2,\mathbb C)\) spin group as 4D Lorentzian two-spinors |
| **fiber length** | supplied by canonical metric; constrained by gravity, \(L_H=\Omega L_H^{\rm ref}\) in static/conformal sector |
| **connection** | canonical \(U(1)\) connection; old \(T_-\) sourcing remains a candidate |
| **Kerr** | complex worldline/Newman–Janis deformation of representational spacetime; shells follow the displaced complex worldline |
| **time** | belongs to Lorentzian real structure; uniqueness not derived |
| **twistors** | optional later encoding, not fundamental |
| **Grassmann parity** | not derived |
| **static target** | \(\mathcal M_{\rm static}\sim\mathbb R_t\times S^4\), \(B_{\rm rep}\sim\mathbb R_t\times S^3\), \(B_{\rm grav}\sim\mathbb R_t\times\mathbb{RP}^3\) |
| **next construction** | explicit global \(E\) whose shell restrictions are \(SL(2,\mathbb C)\to Q_{\rm aff}^2\) and whose middle-space meridians recover the seed |

---

# External anchors

1. The affine quadric \(Q_{[2]}\) is a homogeneous complex surface
   \[
   Q_{[2]}=SL(2,\mathbb C)/\mathbb C^\times,
   \]
   with compact real orbit \(S^2\).
2. The ordinary Hopf fibration may be written in homogeneous-space form
   \[
   U(1)\to SU(2)\to SU(2)/U(1)\simeq S^2.
   \]
3. Four-dimensional Lorentzian two-spinors transform under \(SL(2,\mathbb C)\), the same complex spin group appearing in the shell lift.
4. Newman–Janis acts at the level of complexified four-dimensional spacetime/null tetrads; twistor space is not required for the Schwarzschild-to-Kerr step.

---

# One-sentence version

> **Version 15.2 axiomatizes a canonical total space whose shells around complex source worldlines are lifted by the complexified Hopf geometry \(\mathbb C^\times\to SL(2,\mathbb C)\to Q_{\rm aff}^2\); quotienting its compact physical \(U(1)\) gives the full middle space, whose resolved Lorentzian bisection is the representational base for light and matter while its meridian quotient is the base seen by gravity.**
