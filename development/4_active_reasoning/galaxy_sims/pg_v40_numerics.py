"""Projective Gravity v40 -- standalone numerical suite for Part XXXVIII: the leaf between the horizons -- the C-metric beside Kerr, Law I on the
leaf, the galaxy as a rendering and the two Hopf structures -- Entries 489-521 with the responses to them, of 18-20 November 2026 (v40.0); the
follow-up of 20-21 November on the galaxy's falloff, its Newtonian reading and a leaf per galaxy (v40.1); the quick falloff, the point source's
apparent halo, the image's density against the exponential and the density near the equator, of 22 November (v40.2) (NumPy imported for the shared header only;
every number is computed in plain Python arithmetic, the curvature exactly by truncated Taylor series where it is taken by jets, a few derivatives
by stated finite differences; Python 3.11-3.13 tested).
Part XXXVII is frozen at v39.0 with its suite pg_v39_numerics.py; Part XXXVI at v38.2 with pg_v38_numerics.py; Part XXXV at v37.9 with
pg_v37_numerics.py; Parts XXXIII-XXXIV at v36.16 with pg_v36_numerics.py; Parts XXX-XXXII at v35.8 with pg_v35_numerics.py; Part XXIX's frozen suite
is pg_v34_numerics.py (v34.10).

Run (from the directory holding this file):
    python3 -I pg_v40_numerics.py              # the regression suite of Part XXXVIII, v40.0-v40.2 (check summary; about a minute and a quarter)
    python3 -I pg_v40_numerics.py v40_0        # the v40.0 sections only (a few seconds)
    python3 -I pg_v40_numerics.py v40_1        # the v40.1 sections only (about a minute)
    python3 -I pg_v40_numerics.py v40_2        # the v40.2 sections only (under a minute)
Every mode exits with status 1 if any check fails; an unknown mode prints the usage line and exits with status 2.

v40_0_suite(): Entry 489, the sphere of references read again -- its center, a reference at a point of the line and its complement's signature,
the tilt read from the far end as Harrison's boost, the null basis, the clock factors, the entropy over the sphere; Entries 518-519 and the
response titled Entry 521, the Hopf circle of references, a tilt that varies, two bodies' references, the shared far reference, a move that keeps
it and two moves in either order.  Entries 489-490, the C-metric
beside Kerr -- Weyl's rods, one polynomial's three roots and the identity deficit = T_R/T_hole, the swap of time and angle, two holes, the foci,
Kerr's rods.  Entries 491-492, the region between the horizons -- the rectangle and its corners, the accelerating Kerr hole and the sum rule with
four roots, a light ring that a reference does not carry.  Entry 493, the throat, the entropy along the sphere, the electroweak temperature, the
Higgs condition as a reversed Cauchy-Schwarz inequality.  The type D structure -- a conformal Killing-Yano form, Psi2, its Killing vector -- and
strip, constrain, restore.  Entry 495, the charged C-metric, the offset as a cosmological constant, the isotropic member.  Entry 497, Law I on the
leaf -- the two-sided hole as two antipodal poles, charge as their mismatch -- and the mirror acceleration.  Entries 498-499, the galaxy's image on
a leaf, its tail, and the trade-off with the rotation curve (the frozen v36 thin-disk solver ported to plain arithmetic).  Entries 500-501, the
conformal factor that the constraint fixes, the hyperbolic rendering, the projective readouts.  Entries 502-506, the two Hopf fields as the two
structures and the flashlight.  Entries 507-510, the rays as pairs, incidence, Kepler's hidden symmetry, Kustaanheimo-Stiefel, Gibbons-Hawking,
the five-dimensional throat, the leaf's local corrections.  Entries 512-513, the closed-leaf hole with acceleration and the deck test.
Data embedded, attributed where printed: CODATA 2022's hbar, G, k_B, the Planck length, alpha and the proton and electron masses (Mohr et al.
2025, Rev. Mod. Phys. 97, 025002); the IAU's nominal solar mass parameter and parsec; the electroweak crossover temperature 159.5 GeV (D'Onofrio
and Rummukainen 2016); the Milky Way's stellar halo mass (Deason, Belokurov and Sanders 2019) and the cool circumgalactic mass (Werk et al. 2014);
the thin disk's scale length and height (Bland-Hawthorn and Gerhard 2016); the circular speed at the Sun and its gradient (Eilers et al. 2019).

v40_1_suite(): the follow-up of 20-21 November.  Entry 326's falloff on a leaf -- one shape for each k = ell/h, the scan from k = 0.01 to 100, the
shape classes (a monotonic rise, a wiggle below the plateau, a bump above it) and their boundaries, the small-k limit, and Entry 322's classes for
the eight galaxies of v36.1.  The Newtonian reading -- the image's own thin disk, the driven remainder and its density, decompositions with the NFW,
Burkert and pseudo-isothermal halos, and the halos against the remainder alone.  A leaf per galaxy -- the frozen leaf with other scale lengths, the
Milky Way with its leaf set by the speed at the Sun, the two dwarfs with the leaf free.  v40.0's thin-disk solver is evaluated through kernel rows
computed once per point, with 256 azimuths in its ring kernel's bounded remainder (64 in v40.0); extrema, crossings and slopes from an eight-point
polynomial in ln R.  Data embedded for v40.1, attributed where printed: SPARC's rotation curves of DDO 154 and IC 2574 and the pilot's disk scale
lengths and radii (Lelli, McGaugh and Schombert 2016, as the frozen pg_v36_numerics.py embeds them), with the baryonic masses, arena leaves and
source breadths of v36.0-v36.1; Eilers et al. 2019's circular velocity curve (their Table 1) and adopted R_sun = 8.122 kpc; the thin disk's scale
length 2.6 +- 0.5 kpc (Bland-Hawthorn and Gerhard 2016).

v40_2_suite(): the second follow-up of 22 November.  The quick falloff, k = 100, against Freeman's peak; the point source's apparent halo,
its mass and density in closed form; the image's density against the exponential, the radius where it departs and the mass inside and
beyond; and the density near the leaf's equator changed beyond 36 kpc, by v40.0's thin-disk solver, against Eilers et al.'s errors.
"""
import numpy as np
PI = np.pi
_CHECKS = []
def check(cond, msg):
    _CHECKS.append((bool(cond), msg))
    print(f"   [{'PASS' if cond else 'FAIL'}] {msg}")

# ==================================================================================================== v40 body
# (the toy file appends everything below this line, reusing its own check and _CHECKS)
import math
import cmath
import random
import itertools

# ---------------------------------------------------------------------------------------------------- the library
# Copied verbatim from the frozen pg_v39_numerics.py (v39.0) and renamed with the v40 prefix: the residual and decimal printers, the jets
# (truncated Taylor series in four variables, exact to their order), the inverse and Ricci tensor of an n-dimensional metric of jets, and
# a Jacobi eigen-solver for real symmetric matrices.

def _v40_r(x):
    """A residual, printed in coarse bins so that the print does not depend on the machine's last bits: '<1e-12', '<1e-10', '<1e-8', else 1 digit."""
    x = float(abs(x))
    for b in (1e-12, 1e-10, 1e-8):
        if x < b: return f"<{b:.0e}"
    return f"{x:.1e}"

def _v40_z(x, nd=6):
    """x rounded to nd decimals, with the sign of a zero dropped, so that a print of zero never depends on the machine's last bits."""
    return round(float(x), nd) + 0.0

def _v40_f(x, nd=6):
    return f"{_v40_z(x, nd):.{nd}f}"

def _v40_c(z, nd=6):
    """A complex number printed as a + bi with nd decimals."""
    a, b = _v40_z(z.real, nd), _v40_z(z.imag, nd)
    return f"{a:.{nd}f}{'+' if b >= 0 else '-'}{abs(b):.{nd}f}i"

def _v40_wrap(text, first="     ", rest="     ", width=158):
    """Print text wrapped at width, the first line after first, the others after rest; a ~ is a space that does not break."""
    words = text.split(" "); line = first
    for w_ in words:
        if len(line) + len(w_) + 1 > width and line.strip():
            print(line.rstrip().replace("~", " ")); line = rest
            if not w_: continue
        line += w_ + " "
    print(line.rstrip().replace("~", " "))

def _v40_monos(N, nv=4):
    out = []
    def rec(prefix, left, k):
        if k == nv - 1:
            out.append(tuple(prefix + [left])); return
        for e in range(left, -1, -1):
            rec(prefix + [e], left - e, k + 1)
    for d in range(N + 1):
        rec([], d, 0)
    return out

class _V40JetSpace:
    """Truncated Taylor series in four variables to total order N: the monomials by degree, the product tables for each order m <= N (the
    pairs whose degrees add up to at most m) and the derivative tables."""
    def __init__(self, N, nv=4):
        self.N, self.nv = N, nv
        self.mono = _v40_monos(N, nv); self.idx = {m: i for i, m in enumerate(self.mono)}
        self.deg = [sum(m) for m in self.mono]; self.size = len(self.mono)
        self.mul = []
        for m in range(N + 1):
            tab = []
            for i, a in enumerate(self.mono):
                if self.deg[i] > m: continue
                for j, b in enumerate(self.mono):
                    if self.deg[i] + self.deg[j] > m: continue
                    tab.append((i, j, self.idx[tuple(x + y for x, y in zip(a, b))]))
            self.mul.append(tab)
        self.der = []
        for v in range(nv):
            tab = []
            for k, a in enumerate(self.mono):
                if a[v] == 0: continue
                b = list(a); b[v] -= 1
                tab.append((k, self.idx[tuple(b)], a[v]))
            self.der.append(tab)

class _V40Jet:
    """A truncated Taylor series about a point: c[k] the coefficient of the monomial mono[k] of the displacement, valid to total order n.  Its
    arithmetic is exact to that order, so a derivative at the point is exact up to rounding, with no step size."""
    __slots__ = ('S', 'c', 'n')
    def __init__(self, S, c, n):
        self.S, self.c, self.n = S, c, n
    @staticmethod
    def const(S, v, n=None):
        c = [0.0]*S.size; c[0] = v; return _V40Jet(S, c, S.N if n is None else n)
    @staticmethod
    def var(S, k, x0, n=None):
        c = [0.0]*S.size; c[0] = x0; e = [0]*S.nv; e[k] = 1; c[S.idx[tuple(e)]] = 1.0; return _V40Jet(S, c, S.N if n is None else n)
    def _trim(self, n):
        if n >= self.S.N: return self.c
        return [x if self.S.deg[k] <= n else 0.0 for k, x in enumerate(self.c)]
    def __add__(self, o):
        if isinstance(o, _V40Jet):
            n = min(self.n, o.n); return _V40Jet(self.S, [a + b for a, b in zip(self._trim(n), o._trim(n))], n)
        c = list(self.c); c[0] += o; return _V40Jet(self.S, c, self.n)
    __radd__ = __add__
    def __neg__(self):
        return _V40Jet(self.S, [-a for a in self.c], self.n)
    def __sub__(self, o):
        return self + (-o)
    def __rsub__(self, o):
        return (-self) + o
    def __mul__(self, o):
        if isinstance(o, _V40Jet):
            n = min(self.n, o.n); out = [0.0]*self.S.size; a, b = self.c, o.c
            for i, j, k in self.S.mul[n]:
                out[k] += a[i]*b[j]
            return _V40Jet(self.S, out, n)
        return _V40Jet(self.S, [a*o for a in self.c], self.n)
    __rmul__ = __mul__
    def series(self, coeffs):
        """sum_k coeffs[k] (self - self(point))^k."""
        d = _V40Jet(self.S, [0.0] + list(self.c[1:]), self.n)
        out = _V40Jet.const(self.S, coeffs[0], self.n); p = None
        for k in range(1, self.n + 1):
            p = d if p is None else p*d
            out = out + p*coeffs[k]
        return out
    def __truediv__(self, o):
        if isinstance(o, _V40Jet): return self*o.recip()
        return self*(1.0/o)
    def __rtruediv__(self, o):
        return self.recip()*o
    def recip(self):
        a = self.c[0]; return self.series([(-1)**k/a**(k + 1) for k in range(self.n + 1)])
    def powr(self, p):
        a = self.c[0]; co = []; b = 1.0
        for k in range(self.n + 1):
            co.append(b*a**(p - k)); b *= (p - k)/(k + 1)
        return self.series(co)
    def sqrt(self):
        return self.powr(0.5)
    def exp(self):
        e = math.exp(self.c[0]); return self.series([e/math.factorial(k) for k in range(self.n + 1)])
    def sin(self):
        s, c = math.sin(self.c[0]), math.cos(self.c[0]); d = [s, c, -s, -c]
        return self.series([d[k % 4]/math.factorial(k) for k in range(self.n + 1)])
    def cos(self):
        s, c = math.sin(self.c[0]), math.cos(self.c[0]); d = [c, -s, -c, s]
        return self.series([d[k % 4]/math.factorial(k) for k in range(self.n + 1)])
    def d(self, v):
        """The partial derivative in the variable v, valid to order n - 1."""
        out = [0.0]*self.S.size; c = self.c
        for k, kb, f in self.S.der[v]:
            if self.S.deg[k] <= self.n:
                out[kb] += f*c[k]
        return _V40Jet(self.S, out, self.n - 1)
    def val(self):
        if self.n < 0: raise ValueError("the value of a jet read beyond its order")      # a derivative past the jet's order is not known
        return self.c[0]

def _v40_zero(S, n):
    return _V40Jet.const(S, 0.0, n)

def _v40_jsum(terms, S, n):
    out = _v40_zero(S, n)
    for t in terms:
        out = out + t
    return out

def _v40_minv(G):
    """The inverse of an n x n matrix of jets: Gauss-Jordan at the point, then the Neumann series in the displacement."""
    m = len(G); S = G[0][0].S; n = min(G[i][j].n for i in range(m) for j in range(m)); R = range(m)
    A = [[G[i][j].c[0] for j in R] + [1.0 if i == j else 0.0 for j in R] for i in R]
    for c in R:
        p = max(range(c, m), key=lambda r: abs(A[r][c])); A[c], A[p] = A[p], A[c]
        piv = A[c][c]; A[c] = [x/piv for x in A[c]]
        for r in R:
            if r != c:
                f = A[r][c]; A[r] = [x - f*y for x, y in zip(A[r], A[c])]
    I0 = [[A[i][m + j] for j in R] for i in R]
    D = [[_V40Jet(S, [0.0] + list(G[i][j]._trim(n)[1:]), n) for j in R] for i in R]
    T = [[_v40_jsum((D[k][j]*(-I0[i][k]) for k in R), S, n) for j in R] for i in R]
    term = [[_V40Jet.const(S, I0[i][j], n) for j in R] for i in R]; out = [row[:] for row in term]
    for _ in range(n):
        term = [[_v40_jsum((T[i][k]*term[k][j] for k in R), S, n) for j in R] for i in R]
        out = [[out[i][j] + term[i][j] for j in R] for i in R]
    return out

def _v40_ricci(G, act):
    """The Ricci tensor, its scalar and the Einstein tensor of an n-dimensional metric G, an n x n matrix of jets in the variables act[k] -- the
    coordinates the metric depends on; along the others it is constant.  R_bd = d_a Gamma^a_db - d_d Gamma^a_ab + Gamma^a_ae Gamma^e_db -
    Gamma^a_de Gamma^e_ab.  Returns the values at the point: (Ric, R, Ein, g, gi)."""
    m = len(G); S = G[0][0].S; Gi = _v40_minv(G); R = range(m)
    def dd(J, a):
        return J.d(act.index(a)) if a in act else _v40_zero(S, J.n - 1)
    dG = [[[dd(G[b][c], a) for c in R] for b in R] for a in R]
    n1 = dG[0][0][0].n
    low = [[[(dG[b][d][c] + dG[c][d][b] - dG[d][b][c])*0.5 for c in R] for b in R] for d in R]
    Gam = [[[_v40_jsum((Gi[a][d]*low[d][b][c] for d in R), S, n1) for c in R] for b in R] for a in R]
    tr = [_v40_jsum((Gam[a][a][e] for a in R), S, n1) for e in R]
    G0 = [[[Gam[a][b][c].val() for c in R] for b in R] for a in R]
    Ric = [[0.0]*m for _ in R]
    for b in R:
        for d in R:
            if d < b:
                Ric[b][d] = Ric[d][b]; continue
            t = sum(dd(Gam[a][d][b], a).val() for a in R) - dd(tr[b], d).val()
            t += sum(tr[e].val()*G0[e][d][b] for e in R) - sum(G0[a][d][e]*G0[e][a][b] for a in R for e in R)
            Ric[b][d] = t
    g = [[G[i][j].val() for j in R] for i in R]; gi = [[Gi[i][j].val() for j in R] for i in R]
    Rs = sum(gi[i][j]*Ric[i][j] for i in R for j in R)
    Ein = [[Ric[i][j] - 0.5*g[i][j]*Rs for j in R] for i in R]
    return Ric, Rs, Ein, g, gi

def _v40_inv(A):
    """The inverse of a real or complex n x n matrix of numbers (Gauss-Jordan with pivoting)."""
    m = len(A); R = range(m); M = [list(A[i]) + [1.0 if i == j else 0.0 for j in R] for i in R]
    for c in R:
        p = max(range(c, m), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        piv = M[c][c]; M[c] = [x/piv for x in M[c]]
        for r in R:
            if r != c:
                f = M[r][c]; M[r] = [x - f*y for x, y in zip(M[r], M[c])]
    return [row[m:] for row in M]

def _v40_mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def _v40_T(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def _v40_eig(A, sweeps=60):
    """The eigenvalues of a real symmetric matrix, by Jacobi rotations."""
    m = len(A); a = [list(map(float, r)) for r in A]
    for _ in range(sweeps):
        off = sum(a[i][j]**2 for i in range(m) for j in range(m) if i != j)
        if off < 1e-30: break
        for p in range(m):
            for q in range(p + 1, m):
                if abs(a[p][q]) < 1e-300: continue
                th = 0.5*math.atan2(2*a[p][q], a[q][q] - a[p][p]); c, s = math.cos(th), math.sin(th)
                for k in range(m):
                    akp, akq = a[k][p], a[k][q]; a[k][p] = c*akp - s*akq; a[k][q] = s*akp + c*akq
                for k in range(m):
                    apk, aqk = a[p][k], a[q][k]; a[p][k] = c*apk - s*aqk; a[q][k] = s*apk + c*aqk
    return sorted(a[i][i] for i in range(m))

# ---------------------------------------------------------------------------------------------------- the v40 helpers
# New in v40.0: quadrature, roots, elliptic integrals by the arithmetic-geometric mean, quaternions, and metrics of jets built from functions.

def _v40_simpson(f, a, b, n=2000):
    """Simpson's rule with n (even) panels."""
    n += n % 2; h = (b - a)/n
    return (f(a) + f(b) + sum((4 if i % 2 else 2)*f(a + i*h) for i in range(1, n)))*h/3

def _v40_bisect(f, a, b, it=200):
    """A root of f in [a, b], f(a) and f(b) of opposite signs, by bisection to the last bit."""
    fa = f(a)
    for _ in range(it):
        c = 0.5*(a + b); fc = f(c)
        if c == a or c == b: break
        if (fc < 0) == (fa < 0): a, fa = c, fc
        else: b = c
    return 0.5*(a + b)

def _v40_roots(f, lo, hi, n=20000):
    """Every sign change of f on a grid of n cells in [lo, hi], each refined by bisection."""
    out = []; h = (hi - lo)/n; x0 = lo; f0 = f(x0)
    for i in range(1, n + 1):
        x1 = lo + i*h; f1 = f(x1)
        if (f0 < 0) != (f1 < 0): out.append(_v40_bisect(f, x0, x1))
        x0, f0 = x1, f1
    return out

def _v40_ellipK(m):
    """The complete elliptic integral of the first kind K(m), m = k^2 < 1, by the arithmetic-geometric mean."""
    a, b = 1.0, math.sqrt(1.0 - m)
    for _ in range(60):
        a, b = 0.5*(a + b), math.sqrt(a*b)
        if abs(a - b) < 1e-16*a: break
    return math.pi/(2*a)

def _v40_ellipE(m):
    """The complete elliptic integral of the second kind E(m), by the arithmetic-geometric mean with its sum of squared differences."""
    a, b = 1.0, math.sqrt(1.0 - m); s = 0.5*m; p = 0.5
    for _ in range(60):
        c = 0.5*(a - b); a, b = 0.5*(a + b), math.sqrt(a*b); p *= 2; s += p*c*c
        if abs(c) < 1e-17: break
    return math.pi/(2*a)*(1.0 - s)

def _v40_qmul(a, b):
    return [a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3], a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2],
            a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1], a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]]

def _v40_qconj(a):
    return [a[0], -a[1], -a[2], -a[3]]

def _v40_dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def _v40_add(a, b, s=1.0):
    return [x + s*y for x, y in zip(a, b)]

def _v40_scale(a, s):
    return [x*s for x in a]

def _v40_norm(a):
    return math.sqrt(_v40_dot(a, a))

def _v40_unit(a):
    return _v40_scale(a, 1.0/_v40_norm(a))

def _v40_cross(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]

def _v40_rot(q, v3):
    """The rotation of a unit quaternion q applied to a 3-vector: q v q^-1."""
    return _v40_qmul(_v40_qmul(q, [0.0] + list(v3)), _v40_qconj(q))[1:]

def _v40_rand_unit(rng, n=4):
    return _v40_unit([rng.gauss(0, 1) for _ in range(n)])

def _v40_rand_tangent(rng, x):
    w = [rng.gauss(0, 1) for _ in range(len(x))]
    return _v40_unit(_v40_add(w, x, -_v40_dot(w, x)))

def _v40_jet_metric(fun, S, x0, act):
    """An n x n metric of jets: fun(X) returns the matrix of jets for the jet coordinates X, X[k] the jet of coordinate act[k] at x0[k]."""
    X = [_V40Jet.var(S, k, x0[k]) for k in range(len(act))]
    return fun(X)

def _v40_maxabs(M):
    return max(abs(x) for row in M for x in row)

def _v40_sector_ricci(Gt, Ga, A, y0, x0, restored=True, N=2):
    """The mixed Ricci tensor of s^2 [Gt(y) dt^2 - dy^2/Gt(y) + dx^2/Ga(x) + Ga(x) dphi^2], s = 1/(A(x - y)) (or s = 1 unstripped), coordinates
    (t, y, x, phi), the derivatives exact by jets; returns the mixed Ricci tensor, the metric's value and its inverse."""
    S = _V40JetSpace(N)
    def fun(V):
        y, x = V[0], V[1]; Gy, Hx = Gt(y), Ga(x); z = _v40_zero(S, S.N)
        pre = (A*A*(x - y)*(x - y)).recip() if restored else _V40Jet.const(S, 1.0)
        g = [[z for _ in range(4)] for _ in range(4)]
        g[0][0] = pre*Gy; g[1][1] = -1*pre*Gy.recip(); g[2][2] = pre*Hx.recip(); g[3][3] = pre*Hx
        return g
    G = _v40_jet_metric(fun, S, (y0, x0), [1, 2]); Ric, Rs, Ein, g, gi = _v40_ricci(G, [1, 2])
    return [[sum(gi[i][k]*Ric[k][j] for k in range(4)) for j in range(4)] for i in range(4)], g, gi

# ==================================================================================================== v40.0 (18-20 November 2026): sections

def _v40_form(z):
    """Kinnersley's form <z, z> = |u|^2 + |v|^2 - |w|^2 on the three channels (v39.0-4)."""
    return abs(z[0])**2 + abs(z[1])**2 - abs(z[2])**2

def _v40_herm(x, y):
    return x[0]*y[0].conjugate() + x[1]*y[1].conjugate() - x[2]*y[2].conjugate()

class _V40CJ:
    """A complex jet in one variable to second order, (f, f', f''), for the Ernst residual of v40.0-1(g) (as v39's _V39CJ, with cos and sin)."""
    def __init__(s, a, b=0.0, c=0.0):
        s.a, s.b, s.c = complex(a), complex(b), complex(c)
    def __add__(s, o):
        o = o if isinstance(o, _V40CJ) else _V40CJ(o); return _V40CJ(s.a + o.a, s.b + o.b, s.c + o.c)
    __radd__ = __add__
    def __neg__(s):
        return _V40CJ(-s.a, -s.b, -s.c)
    def __sub__(s, o):
        return s + (-(o if isinstance(o, _V40CJ) else _V40CJ(o)))
    def __rsub__(s, o):
        return (-s) + o
    def __mul__(s, o):
        o = o if isinstance(o, _V40CJ) else _V40CJ(o); return _V40CJ(s.a*o.a, s.a*o.b + s.b*o.a, s.a*o.c + 2*s.b*o.b + s.c*o.a)
    __rmul__ = __mul__
    def inv(s):
        return _V40CJ(1/s.a, -s.b/s.a**2, 2*s.b**2/s.a**3 - s.c/s.a**2)
    def __truediv__(s, o):
        o = o if isinstance(o, _V40CJ) else _V40CJ(o); return s*o.inv()
    def __rtruediv__(s, o):
        return _V40CJ(o)*s.inv()
    def cos(s):
        return _V40CJ(cmath.cos(s.a), -cmath.sin(s.a)*s.b, -cmath.cos(s.a)*s.b*s.b - cmath.sin(s.a)*s.c)
    def sin(s):
        return _V40CJ(cmath.sin(s.a), cmath.cos(s.a)*s.b, -cmath.sin(s.a)*s.b*s.b + cmath.cos(s.a)*s.c)

def _v40_ernst2(zfun, M, a, r, th):
    """The Ernst equations of z = zfun(s, r) on Kerr's three-metric (v39.0-5's _v39_ernst), for a line that may depend on r as well as on s =
    r - ia cos theta: the r- and theta-derivatives are taken by two one-variable jets.  Returns the relative residual."""
    def EF(sj, rj):
        z = zfun(sj, rj); den = z[0] + z[2]; return (z[0] - z[2])/den, z[1]/den
    Er, Pr = EF(_V40CJ(r, 1.0) - 1j*a*math.cos(th), _V40CJ(r, 1.0))
    ct = _V40CJ(th, 1.0).cos(); Et, Pt = EF(_V40CJ(r) - 1j*a*ct, _V40CJ(r))
    Dl = r*r - 2*M*r + a*a; cot = math.cos(th)/math.sin(th)
    lap = lambda x, y: Dl*x.c + (2*r - 2*M)*x.b + y.c + cot*y.b
    dot = lambda x, y, u, v: Dl*x.b*u.b + y.b*v.b
    E, P = Er.a, Pr.a; f = E.real + abs(P)**2
    r1 = f*lap(Er, Et) - (dot(Er, Et, Er, Et) + 2*P.conjugate()*dot(Pr, Pt, Er, Et))
    r2 = f*lap(Pr, Pt) - (dot(Er, Et, Pr, Pt) + 2*P.conjugate()*dot(Pr, Pt, Pr, Pt))
    sc = abs(f*lap(Er, Et)) + abs(dot(Er, Et, Er, Et)) + abs(dot(Pr, Pt, Er, Et)) + abs(f*lap(Pr, Pt)) + abs(dot(Pr, Pt, Pr, Pt)) + 1e-300
    return (abs(r1) + abs(r2))/sc

def v40_0_sphere():
    """Entry 489: the sphere of references read again (R564).  (a) On Kerr-Newman's line z(s) = (s - M, q, M), <z, z> = |s - M|^2 - b^2 with
    b^2 = M^2 - |q|^2, which is Delta - a^2 sin^2 theta: the null set of the line is the stationary limit.  The sheet swap s -> 2M - s fixes
    s = M, the equatorial circle r = M; for q = 0 the line there is the negative channel, whose complement is the two positive channels, the
    round sphere of v39.0-5.  (b) A reference at a point of the line: its complement has signature (1, 1) where <z, z> > 0 and (2, 0) where
    <z, z> < 0, so its stabilizer is U(1, 1) outside the stationary limit and U(2) inside; det of the complement's form is -<z, z>/|z_w|^2.
    (c) Seen from the far reference the tilt p of v39.0-5 is Harrison's boost b with sin p = tanh b, up to a gauge shift and a clock scale
    cos p; the right angle is at infinite rapidity.  (d) The null basis n+ = (1, 0, 1), n- = (1, 0, -1): z = (s - M)(n+ + n-)/2 + M(n+ - n-)/2
    + q e2.  (e) The clock factors of two references, Omega = |<z, n1>/<z, n2>|^2, compose.  (f) The horizon entropy over the tilted family
    Kerr-Newman(M, M sin p, a cos p): S(p) = pi[(M + c0 cos p)^2 + a^2 cos^2 p], S''(0) = -2 pi M r+; with a weight e^S the tilt's spread is
    (4 pi M^2)^(-1/2), about 3e-39 rad at a solar mass, and the charge's spread 1/(2 sqrt(pi alpha)) electron charges at any mass.
    Entry 518: (g) the overall phase of a reference is the NUT phase, M -> M e^(-i alpha), and its half-turn is the other sheet; the Kerr-NUT
    circle e2 = 0 and the throat circle e1 = 0 are the two circles the tori |e1| = cos p close down on.  (h) A tilt that varies with r is not a
    solution: a constant tilt keeps the Ernst equations to rounding, p = p0 (2M/r) breaks them.  Entry 519: (i) two bodies' references leave
    open two planes, their complements, which share one line and span the three channels; their projectors commute only for form-orthogonal
    references, and Tr(P_A P_B) = 1 + |<zA, zB>|^2/(<zA, zA><zB, zB>).  (j) Every body's reference tends far out to the same line e1, at the
    hyperbolic angle sinh d = b/sqrt(<z, z>): about b/r far out, infinite at the stationary limit.  (k) The moves that keep the far reference,
    its stabilizer's Harrison boosts, keep asymptotic flatness only on an uncharged seed or along its charge phase; on a two-body static seed
    they re-render every body at once, each body's Gauss charge m_i sinh b.  (l) Two boosts with different charge phases do not commute:
    applied to Kerr in the two orders they give the same charge and the same |w| with opposite phases arg(1 + tanh b1 tanh b2 e^(i(d2 - d1)))
    -- NUT charges of opposite sign, neither composite asymptotically flat, the two mirror images."""
    print("\n== v40.0-1. Entry 489: the sphere of references read again -- its center, a reference at a point of the line, the tilt as "
          "Harrison's boost, the null basis, the clock factors, the entropy over the sphere; Entries 518-519: the Hopf circle of references, a tilt "
          "that varies, two bodies' references, the shared far reference, a move that keeps it, and two moves in either order (R564) ==")
    rng = random.Random(4001); w = [0.0]*6; sig = {'out': [0, 0], 'in': [0, 0]}
    for _ in range(400):
        M = rng.uniform(0.5, 2.0); a = rng.uniform(0.0, 0.9)*M; q = complex(rng.uniform(-0.4, 0.4), rng.uniform(-0.4, 0.4))*M
        r = rng.uniform(-3.0, 6.0)*M; th = rng.uniform(0.05, 3.09); s = complex(r, -a*math.cos(th)); z = [s - M, q, M]
        b2 = M*M - abs(q)**2; Dl = r*r - 2*M*r + a*a + abs(q)**2
        w[0] = max(w[0], abs(_v40_form(z) - (abs(s - M)**2 - b2)), abs(_v40_form(z) - (Dl - (a*math.sin(th))**2)))
        s2 = 2*M - s; w[1] = max(w[1], abs(_v40_form([s2 - M, q, M]) - _v40_form(z)))
        x1 = [1.0 + 0j, 0j, (z[0]/z[2]).conjugate()]; x2 = [0j, 1.0 + 0j, (z[1]/z[2]).conjugate()]
        w[2] = max(w[2], abs(_v40_herm(x1, z)), abs(_v40_herm(x2, z)))
        g = [[_v40_herm(x, y) for y in (x1, x2)] for x in (x1, x2)]
        det = (g[0][0]*g[1][1] - g[0][1]*g[1][0]).real; tr = (g[0][0] + g[1][1]).real
        w[3] = max(w[3], abs(det + _v40_form(z)/abs(z[2])**2))
        if abs(_v40_form(z)) > 1e-6:
            key = 'out' if _v40_form(z) > 0 else 'in'
            ok_sig = (det < 0) if key == 'out' else (det > 0 and tr > 0)
            sig[key][0 if ok_sig else 1] += 1
    _v40_wrap(f"(a) The center [T/V].  On Kerr-Newman's line z(s) = (s - M, q, M), s = r - ia cos theta, Kinnersley's form is <z, z> = |s - M|^2 - "
              f"b^2 with b^2 = M^2 - |q|^2, and equals Delta - a^2 sin^2 theta (400 random points with spin and both charges, {_v40_r(w[0])}): the "
              f"line's null set |s - M| = b is the stationary limit, where -g_tt = 0.  The sheet swap s -> 2M - s keeps the form ({_v40_r(w[1])}) "
              f"and fixes s = M, which is the circle r = M in the equatorial plane -- a point of the line, not an invariant midpoint of the "
              f"spacetime.  For q = 0 the line there is (0, 0, M), the negative channel, whose complement is the two positive channels: the round "
              f"3-sphere of unit references of v39.0-5, on which U(2) acts.")
    _v40_wrap(f"(b) A reference at a point of the line [T/V].  The complement of z (two vectors with <x, z> = 0, {_v40_r(w[2])}) carries the form "
              f"with determinant -<z, z>/|z_w|^2 ({_v40_r(w[3])}).  Outside the stationary limit, <z, z> > 0, its signature is (1, 1) at "
              f"{sig['out'][0]} of {sum(sig['out'])} points; inside, (2, 0) at {sig['in'][0]} of {sum(sig['in'])}.  So the reference's stabilizer is "
              f"U(1, 1) outside -- boosts, which at the far end are Harrison's charging (v39.0-4(c)) -- and U(2) inside, which mixes the two positive "
              f"channels freely: a rule that reads only an inside reference's own position cannot prefer one positive channel to the other.  The "
              f"counts check the code: the form has signature (2, 1), so by Sylvester's law of inertia they cannot come out otherwise.")
    Mm, a0 = 1.0, 0.7; wt = 0.0
    for _ in range(300):
        r = rng.uniform(2.2, 7.0); th = rng.uniform(0.1, 3.0); s = complex(r, -a0*math.cos(th))
        p = rng.uniform(0.05, 1.5); d = rng.uniform(0, 2*math.pi); k = cmath.exp(1j*d)*math.tan(p)
        u_, v_, w_ = (s - Mm)*math.cos(p), cmath.exp(1j*d)*(s - Mm)*math.sin(p), Mm
        Ep, Fp = (u_ - w_)/(u_ + w_), v_/(u_ + w_); lam = math.cos(p)
        E1 = lam**2*(Ep + 2*k.conjugate()*Fp - abs(k)**2); F1 = lam*(Fp - k)
        bb = math.acosh(1/math.cos(p))
        ub, vb, wb = s - Mm, cmath.exp(1j*(d + math.pi))*Mm*math.sinh(bb), Mm*math.cosh(bb)
        Eb, Fb = (ub - wb)/(ub + wb), vb/(ub + wb)
        wt = max(wt, abs(E1 - Eb), abs(F1 - Fb), abs(math.sin(p) - math.tanh(bb)))
    raps = [(pd, math.atanh(math.sin(math.radians(pd)))) for pd in (30.0, 60.0, 85.0, 89.0, 89.9)]
    _v40_wrap(f"(c) The far reference [T/V].  The tilt by p of v39.0-5 -- the reference (cos p, e^(i d) sin p, 0) applied to Kerr's line, M = 1, "
              f"a = 0.7 -- is, read from the far end, a gauge shift Phi -> Phi - k with k = e^(i d) tan p, a clock scale cos p, and Harrison's boost "
              f"of rapidity b with sin p = tanh b, which takes Kerr to Kerr-Newman with M cosh b and |q| = M sinh b (v39.0-4(c)); the Ernst potentials "
              f"agree at 300 random points ({_v40_r(wt)}).  The rapidities: " + ", ".join(f"b = {_v40_f(b_, 4)} at {pd:g} degrees" for pd, b_ in raps)
              + ".  The right angle, the throat, is at infinite rapidity: the far reference has v39's sphere minus its circle of throats.")
    wn = 0.0
    for _ in range(200):
        M = rng.uniform(0.5, 2.0); q = complex(rng.gauss(0, 0.3), rng.gauss(0, 0.3)); s = complex(rng.uniform(-4, 6), rng.uniform(-1, 1))
        z = [s - M, q, M]; npl = [1.0, 0.0, 1.0]; nmi = [1.0, 0.0, -1.0]
        zz = [(s - M)*(npl[i] + nmi[i])/2 + M*(npl[i] - nmi[i])/2 + (q if i == 1 else 0.0) for i in range(3)]
        wn = max(wn, sum(abs(x - y) for x, y in zip(z, zz)), abs(_v40_form(npl)), abs(_v40_form(nmi)))
    wc = 0.0
    for _ in range(200):
        z = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]
        ns = [[complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)] for _ in range(3)]
        Om = lambda i, j: abs(_v40_herm(z, ns[i])/_v40_herm(z, ns[j]))**2
        wc = max(wc, abs(Om(0, 1)*Om(1, 2) - Om(0, 2))/Om(0, 2))
    _v40_wrap(f"(d) The null basis [D/V].  With n+ = (1, 0, 1) and n- = (1, 0, -1), both null, z = (s - M)(n+ + n-)/2 + M(n+ - n-)/2 + q e2 "
              f"({_v40_r(wn)}): the background rides the sum of the two null directions, the mass their difference, the charge the third "
              f"direction -- the sum and difference of v38.2's lanes S and D in form, nothing yet making the two null directions lanes.  "
              f"(e) The clock factors [T/V]: two references read the same line with -g_tt in the ratio Omega = |<z, n1>/<z, n2>|^2, and three "
              f"such factors compose, Omega_12 Omega_23 = Omega_13, an identity of ratios, checked as such ({_v40_r(wc)}, 200 random triples).")
    c0 = math.sqrt(Mm*Mm - a0*a0); rp = Mm + c0
    Sf = lambda p: math.pi*((Mm + c0*math.cos(p))**2 + (a0*math.cos(p))**2)
    S2 = _V40JetSpace(2, 1); P = _V40Jet.var(S2, 0, 0.0); Sj = math.pi*((Mm + c0*P.cos())*(Mm + c0*P.cos()) + a0*a0*P.cos()*P.cos())
    Spp = 2*Sj.c[S2.idx[(2,)]]
    wf = 0.0
    for _ in range(200):
        M = rng.uniform(0.5, 2.0); a = rng.uniform(0, 0.95)*M; p = rng.uniform(0, 1.5); cc = math.sqrt(M*M - a*a)
        Mq, aq = M*math.sin(p), a*math.cos(p); rpk = M + math.sqrt(M*M - Mq*Mq - aq*aq)
        wf = max(wf, abs(math.pi*(rpk*rpk + aq*aq) - math.pi*((M + cc*math.cos(p))**2 + (a*math.cos(p))**2)))
    GMsun, cl, lP, alpha = 1.3271244e20, 299792458.0, 1.616255e-35, 7.2973525643e-3
    Msun = GMsun/cl**2/lP; spread = 1/math.sqrt(4*math.pi*Msun*Msun); qspread = 1/(2*math.sqrt(math.pi*alpha))
    sp_kerr, sp_schw = 1/math.sqrt(-Spp), 1/math.sqrt(4*math.pi)
    _v40_wrap(f"(f) The entropy over the sphere [T/V].  The tilted closing Kerr-Newman(M, M sin p, a cos p) has r+ = M + c0 cos p, c0 = sqrt(M^2 - "
              f"a^2), so S(p) = pi[(M + c0 cos p)^2 + a^2 cos^2 p] (200 random holes, {_v40_r(wf)}).  For M = 1, a = 0.7: S(0) = {_v40_f(Sf(0.0), 6)}, "
              f"S(90 degrees) = {_v40_f(Sf(math.pi/2), 6)} = pi M^2, and S''(0) = {_v40_f(Spp, 6)} = -2 pi M r+ = {_v40_f(-2*math.pi*Mm*rp, 6)}, by "
              f"a jet.  For Schwarzschild, S(0) - S(90 degrees) = 3 pi M^2 = {_v40_f(3*math.pi, 6)} M^2.  Under the weight e^S that v38.2 assumed "
              f"(an assumption, not a measure on references), the untilted reference is the peak, and the tilt's spread is (-S''(0))^(-1/2) = "
              f"(2 pi M r+)^(-1/2) in Planck units: {_v40_f(sp_kerr, 6)} for M = 1, a = 0.7, against Schwarzschild's (4 pi M^2)^(-1/2) = "
              f"{_v40_f(sp_schw, 6)} at M = 1 -- for Schwarzschild, {spread:.3e} rad at a solar mass (GM/c^2 = {GMsun/cl**2:.3f} m from the IAU's "
              f"nominal GM, the Planck length CODATA 2022's) -- and, for Schwarzschild, the charge's spread, M times it, is 1/(2 sqrt(pi alpha)) = "
              f"{_v40_f(qspread, 4)} electron charges at any mass (alpha from CODATA 2022); the throat is suppressed by e^(-3 pi M^2).")
    wg = 0.0
    for _ in range(200):
        p = rng.uniform(0.05, 1.5); d = rng.uniform(0, 2*math.pi); al = rng.uniform(0, 2*math.pi); s = complex(rng.uniform(2.2, 7.0), rng.uniform(-0.7, 0.7))
        ph = cmath.exp(1j*al); z1 = [(s - Mm)*ph*math.cos(p), (s - Mm)*ph*cmath.exp(1j*d)*math.sin(p), Mm]
        z2 = [(s - Mm)*math.cos(p), (s - Mm)*cmath.exp(1j*d)*math.sin(p), Mm*ph.conjugate()]
        E1, F1 = (z1[0] - z1[2])/(z1[0] + z1[2]), z1[1]/(z1[0] + z1[2]); E2, F2 = (z2[0] - z2[2])/(z2[0] + z2[2]), z2[1]/(z2[0] + z2[2])
        z3 = [-(s - Mm)*math.cos(p), -(s - Mm)*cmath.exp(1j*d)*math.sin(p), Mm]; z4 = [(s - Mm)*math.cos(p), (s - Mm)*cmath.exp(1j*d)*math.sin(p), -Mm]
        E3, E4 = (z3[0] - z3[2])/(z3[0] + z3[2]), (z4[0] - z4[2])/(z4[0] + z4[2])
        wg = max(wg, abs(E1 - E2), abs(F1 - F2), abs(E3 - E4))
    _v40_wrap(f"(g) The Hopf circle of references [T/V].  Entry 518 asks where the ordinary/ortho choice sits relative to the sphere of references.  "
              f"The sphere of v39.0-5 is the unit 3-sphere |e1|^2 + |e2|^2 = 1 of the two positive channels, and its Hopf circle, the overall phase "
              f"e -> e^(i alpha) e, is the NUT phase: the line with e^(i alpha) e has the Ernst potentials of the line with e and mass M e^(-i alpha) "
              f"an identity of the projective line, the two lines differing by the overall factor e^(i alpha) (checked at 200 random references and "
              f"phases, {_v40_r(wg)}), and the half-turn alpha = pi gives mass -M, the other sheet.  So on the sphere of "
              f"references, as on the canonical space, the Hopf half-turn is the antipodal map.  The tori |e1| = cos p close down on two linked "
              f"circles, the Kerr-NUT circle e2 = 0 and the throat circle e1 = 0.  That a map from the canonical Hopf and meridian data sends the "
              f"ordinary reading to the first and the ortho reading to the second is a conjecture; nothing here tests it, and v37.8's two "
              f"obstructions to a global exchange stand.")
    res_c, res_v, prof = 0.0, [], (("p0 (2M/r)", lambda rj, p0: p0*2*Mm/rj), ("p0 (2M/r)^2", lambda rj, p0: p0*(2*Mm/rj)*(2*Mm/rj)))
    for _ in range(300):
        r = rng.uniform(2.6, 8.0); th = rng.uniform(0.3, 2.8); p = rng.uniform(0.05, 1.45); d = rng.uniform(0, 6.28); ed = cmath.exp(1j*d)
        res_c = max(res_c, _v40_ernst2(lambda sj, rj: [(sj - Mm)*math.cos(p), (sj - Mm)*(ed*math.sin(p)), _V40CJ(Mm)], Mm, a0, r, th))
    for lab, pf in prof:
        vals = []
        for _ in range(100):
            r = rng.uniform(2.6, 8.0); th = rng.uniform(0.3, 2.8); p0 = rng.uniform(0.2, 0.8); d = rng.uniform(0, 6.28); ed = cmath.exp(1j*d)
            vals.append(_v40_ernst2(lambda sj, rj: [(sj - Mm)*pf(rj, p0).cos(), (sj - Mm)*(ed*pf(rj, p0).sin()), _V40CJ(Mm)], Mm, a0, r, th))
        res_v.append((lab, min(vals), max(vals)))
    qr = [(rr, Mm*math.sin(0.6*2*Mm/rr)) for rr in (2.6, 8.0, 50.0)]
    _v40_wrap(f"(h) A tilt that varies [T/V].  The tilt is a symmetry only as a constant: on Kerr's three-metric (M = 1, a = 0.7), the tilted line keeps "
              f"the Ernst equations at 300 random points and references ({_v40_r(res_c)}, exact derivatives by jets), while a tilt that falls off "
              f"with r breaks them -- relative residual " + "; ".join(f"{lab}: {mn:.2e} to {mx:.2e}" for lab, mn, mx in res_v) + " (100 random "
              f"points each, p0 from 0.2 to 0.8).  The charge such a tilt would read, M sin p(r), is " + ", ".join(f"{_v40_f(q_, 6)} at r = {rr:g}"
              for rr, q_ in qr) + " for p = 0.6 (2M/r): it would need charge spread through space.  So a reference that turns toward the throat "
              f"near the hole is not a member of the family read at each radius; it needs a field of its own with its own equation, which the "
              f"archive does not have (the response's caution).")
    def proj(z):
        zz = _v40_form(z); return [[(1.0 if i == j else 0.0) - z[i]*(z[j].conjugate()*(1 if j < 2 else -1))/zz for j in range(3)] for i in range(3)]
    def mm(A_, B_): return [[sum(A_[i][k]*B_[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    def kn(M_):
        a_ = rng.uniform(0, 0.9)*M_; q_ = complex(rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3))*M_
        s_ = complex(rng.uniform(-2, 8)*M_, -a_*math.cos(rng.uniform(0.1, 3.0))); return [s_ - M_, q_, complex(M_)]
    wi, span3, pos_ov, neg_ov, comm_min = 0.0, 0, 0, 0, 1e9; npair = 400
    for _ in range(npair):
        zA, zB = kn(1.0), kn(rng.uniform(0.3, 3.0))
        if min(abs(_v40_form(zA)), abs(_v40_form(zB))) < 1e-6: continue
        eA = [zA[0], zA[1], -zA[2]]; eB = [zB[0], zB[1], -zB[2]]
        x = [(eA[1]*eB[2] - eA[2]*eB[1]).conjugate(), (eA[2]*eB[0] - eA[0]*eB[2]).conjugate(), (eA[0]*eB[1] - eA[1]*eB[0]).conjugate()]
        nx = sum(abs(c)**2 for c in x); x = [c/math.sqrt(nx) for c in x]
        wi = max(wi, abs(_v40_herm(x, zA))/math.sqrt(sum(abs(c)**2 for c in zA)), abs(_v40_herm(x, zB))/math.sqrt(sum(abs(c)**2 for c in zB)))
        PA, PB = proj(zA), proj(zB)
        PAx = [sum(PA[i][k]*x[k] for k in range(3)) for i in range(3)]; PBx = [sum(PB[i][k]*x[k] for k in range(3)) for i in range(3)]
        wi = max(wi, max(abs(PAx[i] - x[i]) for i in range(3)), max(abs(PBx[i] - x[i]) for i in range(3)))
        cA = [[PA[i][j] for i in range(3)] for j in range(3)]; cB = [[PB[i][j] for i in range(3)] for j in range(3)]
        # the two complements span C^3: zA, zB are not parallel, so the planes are distinct
        det = abs(zA[0]*(zB[1]*x[2] - zB[2]*x[1]) - zA[1]*(zB[0]*x[2] - zB[2]*x[0]) + zA[2]*(zB[0]*x[1] - zB[1]*x[0]))
        span3 += det > 1e-9
        nxx = _v40_form(x); pos_ov += nxx > 1e-12; neg_ov += nxx < -1e-12
        C1, C2 = mm(PA, PB), mm(PB, PA); comm_min = min(comm_min, max(abs(C1[i][j] - C2[i][j]) for i in range(3) for j in range(3)))
        tr = sum(C1[i][i] for i in range(3)); ab = _v40_herm(zA, zB)
        wi = max(wi, abs(tr - (1 + abs(ab)**2/(_v40_form(zA)*_v40_form(zB)))))
    nin = gin = 0; rmin = 1e9
    for _ in range(2000):
        zA = [complex(rng.uniform(1.0, 1.9) - 1.0, -0.7*math.cos(rng.uniform(1.2, 1.9))), 0.3 + 0j, 1.0 + 0j]
        zB = [complex(rng.uniform(1.0, 1.9) - 1.0, -0.6*math.cos(rng.uniform(1.2, 1.9))), 0.2 + 0j, 1.0 + 0j]
        if _v40_form(zA) < 0 and _v40_form(zB) < 0:
            nin += 1; rr_ = abs(_v40_herm(zA, zB))**2/(_v40_form(zA)*_v40_form(zB)); gin += rr_ >= 1 - 1e-12; rmin = min(rmin, rr_)
    z1 = [complex(3.0, -0.3), 0.2 + 0j, 1.0 + 0j]; w1 = [1.0 + 0j, 0.3j, 0.7 + 0j]; c1 = _v40_herm(w1, z1)/_v40_form(z1)
    w1 = [w1[i] - c1*z1[i] for i in range(3)]
    P1, P2 = proj(z1), proj(w1); D1, D2 = mm(P1, P2), mm(P2, P1); comm_orth = max(abs(D1[i][j] - D2[i][j]) for i in range(3) for j in range(3))
    _v40_wrap(f"(i) Two bodies' references [T/V; premise].  Entry 519 proposes that tilting into ortho about one body reveals other degrees of "
              f"freedom than about another.  Premise: what a body's located reference z leaves open is its complement, the plane <x, z> = 0, "
              f"with the form-orthogonal projector P = 1 - z <., z>/<z, z>.  For {npair} random pairs of Kerr-Newman lines at random points, "
              f"masses 1 and 0.3 to 3: the two planes span the three channels in {span3} of {npair}, and share one line, orthogonal to both "
              f"references and kept by both projectors ({_v40_r(wi)}) -- positive in {pos_ov} pairs and negative in {neg_ov}: two bodies together "
              f"miss nothing, since each misses only its own reference line.  The projectors commute only when the references are form-orthogonal "
              f"(commutator {_v40_r(comm_orth)} for such a pair; at least {comm_min:.2e} over the random pairs), and Tr(P_A P_B) = 1 + |<zA, zB>|^2/"
              f"(<zA, zA><zB, zB>) (the same {npair} pairs).  When both references lie inside their stationary limits -- two holes, M = 1 with a = 0.7, "
              f"q = 0.3 and a = 0.6, q = 0.2, at random points inside, {nin} pairs -- the ratio is at least 1 in {gin} (smallest {_v40_f(rmin, 6)}): two "
              f"negative vectors obey the reversed Cauchy-Schwarz inequality, so the count checks the code, and the ratio is cosh^2(rho/2), rho "
              f"their distance in the complex "
              f"hyperbolic plane with the Bergman metric of curvature between -1 and -1/4 (Goldman's normalization).  This is the response's "
              f"three-mode example in Kinnersley's channels; the premise, and a "
              f"parent mode space larger than three channels, are not derived.")
    wj = 0.0; rows_j = []
    for _ in range(300):
        M_ = rng.uniform(0.5, 2.0); a_ = rng.uniform(0, 0.9)*M_; q_ = complex(rng.uniform(-0.4, 0.4), rng.uniform(-0.4, 0.4))*M_
        r_ = rng.uniform(2.2, 50.0)*M_; th_ = rng.uniform(0.05, 3.09); s_ = complex(r_, -a_*math.cos(th_)); z = [s_ - M_, q_, M_]; zz = _v40_form(z)
        if zz <= 0: continue
        R_ = abs(_v40_herm(z, [1.0, 0.0, 0.0]))**2/zz; d_ = math.acosh(math.sqrt(R_))
        wj = max(wj, abs(math.sinh(d_) - math.sqrt(M_*M_ - abs(q_)**2)/math.sqrt(zz)))
    bq = math.sqrt(1.0 - 0.25)
    for r_ in (1.87, 2.0, 3.0, 10.0, 100.0):
        zz = _v40_form([complex(r_ - 1.0), 0.5 + 0j, 1.0 + 0j]); rows_j.append((r_, math.asinh(bq/math.sqrt(zz))))
    _v40_wrap(f"(j) The shared far reference [T/V].  Far out every asymptotically flat body's line tends to e1 = (1, 0, 0), the far reference.  A "
              f"located reference z with <z, z> > 0 and e1 span a plane of signature (1, 1), and |<z, e1>|^2/<z, z> = cosh^2 d with sinh d = "
              f"b/sqrt(<z, z>), b^2 = M^2 - |q|^2 (300 random points, {_v40_r(wj)}).  For M = 1, a = 0.7, Q = 0.5 on the equator: " + ", ".join(
              f"d = {_v40_f(d_, 4)} at r = {r_:g}" for r_, d_ in rows_j) + f" (b/r = {_v40_f(bq/100, 5)} at r = 100), infinite at the stationary "
              f"limit, r = {_v40_f(1 + math.sqrt(1 - 0.25), 6)}.  So every body's reference is the same where space is nearly flat and peels "
              f"away from it toward the "
              f"stationary limit; the shared mode is fixed by the condition at infinity, which is global, not by local flatness.")
    hm1, hm2, hz1, hz2, hb = 1.0, 0.5, 3.0, -3.0, 0.8; hs, hc = math.sinh(hb), math.cosh(hb); hM = hm1 + hm2
    def hU(rho, z): return -hm1/math.hypot(rho, z - hz1) - hm2/math.hypot(rho, z - hz2)
    def hgradU(rho, z):
        g = [0.0, 0.0]
        for m_, zc in ((hm1, hz1), (hm2, hz2)):
            d3 = math.hypot(rho, z - zc)**3; g[0] += m_*rho/d3; g[1] += m_*(z - zc)/d3
        return g
    def hfields(rho, z):
        f = math.exp(2*hU(rho, z)); u_, w_ = 1 + f, 1 - f; D = u_ + hc*w_
        return (u_ - hc*w_)/D, hs*w_/D, f, D
    far, farR = [], {}
    for R_ in (1e4, 1e7):
        for th_ in (0.3, 1.2):
            E_, P_, _, _ = hfields(R_*math.sin(th_), R_*math.cos(th_)); far.append(((1 - E_)*R_/2/(hM*hc) - 1, P_*R_/(hM*hs) - 1))
            farR[R_] = max(farR.get(R_, 0.0), abs(far[-1][0]), abs(far[-1][1]))
    e1 = [1.0, 0.0, 0.0]; Bm = [[1, 0, 0], [0, hc, hs], [0, hs, hc]]
    fixes = max(abs(sum(Bm[i][j]*e1[j] for j in range(3)) - e1[i]) for i in range(3))
    def hgauss(zc, a, n=2000):
        def integrand(t_):
            rho, z = a*math.sin(t_), zc + a*math.cos(t_); E_, P_, f, D = hfields(rho, z); g = hgradU(rho, z)
            dPdn = (-2*hs/D**2)*(2*f)*(g[0]*math.sin(t_) + g[1]*math.cos(t_))
            return dPdn/(E_ + P_*P_)*2*math.pi*rho*a
        return _v40_simpson(integrand, 0.0, math.pi, n)/(4*math.pi)
    hq = [(m_, hgauss(zc, 2.0)) for m_, zc in ((hm1, hz1), (hm2, hz2))]; hq_all = hgauss(0.0, 20.0)
    wk = max(abs(-q_/(m_*hs) - 1) for m_, q_ in hq)
    wk1 = math.cosh(0.5); wk2 = cmath.exp(-1.2j)*math.sinh(0.7)*math.sinh(0.5) + math.cosh(0.7)*math.cosh(0.5)
    _v40_wrap(f"(k) A move that keeps the far reference [T/V].  The mid-build message after Entry 519 proposes that a tilt about one mass, followed by "
              f"moving the reference back out, locks in a new Minkowski mode.  A tilt with the clock and gauge reset at infinity is a Harrison "
              f"boost, which lies in the far reference's stabilizer (it fixes e1, {_v40_r(fixes)}); applied to an uncharged seed, or with its phase "
              f"equal to the seed's charge phase modulo pi, it maps one asymptotically flat solution to another.  With any other phase it gives "
              f"the mass channel a phase, a NUT charge: B(0, 0.5) leaves Kerr's w = {_v40_f(wk1, 6)} real, and B(1.2, 0.7) after it gives "
              f"w = {_v40_f(wk2.real, 6)} - {_v40_f(-wk2.imag, 6)} i; the stabilizer's phase diag(1, 1, e^(i gamma)) likewise turns Schwarzschild "
              f"into Taub-NUT.  Fixing the far reference does not by itself keep asymptotic flatness.  On a static seed of two Curzon bodies, "
              f"uncharged, masses {hm1:g} and {hm2:g} at z = {hz1:g} and {hz2:g}, a boost of rapidity {hb:g}: far "
              f"out the mass is M cosh b and the charge M sinh b, the relative departures falling as 1/r ({farR[1e4]:.1e} at r = 1e4, "
              f"{farR[1e7]:.1e} at r = 1e7, two directions); and Gauss's law about each body, the flux of f^-1 grad Phi "
              f"through a sphere of radius 2 about it with exact derivatives, gives charges " + ", ".join(f"{_v40_f(-q_, 6)}" for _, q_ in hq) +
              f" = m_i sinh b = " + ", ".join(f"{_v40_f(m_*hs, 6)}" for m_, _ in hq) + f" ({_v40_r(wk)} relative), and {_v40_f(-hq_all, 6)} "
              f"about both.  So on this seed a boost that keeps the far reference and asymptotic flatness re-renders every mass at once, each "
              f"charged in proportion to its own mass; it cannot act on one body alone.  Bringing bodies in and out, as the message pictures, needs "
              f"transformations beyond SU(2,1), such as "
              f"the dressing maps of the stationary axisymmetric equations (Belinski and Zakharov; Geroch's group), not computed here.")
    def hB(d_, b_):
        return [[math.cosh(b_), cmath.exp(1j*d_)*math.sinh(b_)], [cmath.exp(-1j*d_)*math.sinh(b_), math.cosh(b_)]]
    def m2(A_, C_): return [[sum(A_[i][k]*C_[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    def a2(A_, x_): return [A_[0][0]*x_[0] + A_[0][1]*x_[1], A_[1][0]*x_[0] + A_[1][1]*x_[1]]
    rows_l, wl = [], 0.0
    for d1, b1, d2, b2 in ((0.0, 0.5, 1.2, 0.7), (0.3, 1.0, 2.0, 1.0), (0.0, 0.2, math.pi/2, 0.2)):
        vAB, wAB = a2(m2(hB(d1, b1), hB(d2, b2)), [0j, 1.0 + 0j]); vBA, wBA = a2(m2(hB(d2, b2), hB(d1, b1)), [0j, 1.0 + 0j])
        alpha = cmath.phase(1 + math.tanh(b1)*math.tanh(b2)*cmath.exp(1j*(d2 - d1)))
        wl = max(wl, abs(vAB - vBA), abs(abs(wAB) - abs(wBA)), abs(cmath.phase(wAB) - alpha), abs(cmath.phase(wBA) + alpha),
                 abs(abs(vAB)**2 - abs(wAB)**2 + 1))
        for vv, ww in ((vAB, wAB), (vBA, wBA)):
            for _ in range(20):
                r = rng.uniform(2.6, 8.0); th = rng.uniform(0.3, 2.8)
                wl = max(wl, _v40_ernst2(lambda sj, rj: [sj - 1.0, _V40CJ(vv), _V40CJ(ww)], 1.0, a0, r, th))
        rows_l.append((d1, b1, d2, b2, abs(vAB), abs(wAB), alpha))
    _v40_wrap(f"(l) Two moves in either order [T/V].  The response titled Entry 521 asks whether excursions about two bodies commute, U_A U_B against "
              f"U_B U_A.  In the far reference's stabilizer, two Harrison boosts with charge phases d1, d2 and rapidities b1, b2 -- each keeping e1 "
              f"-- applied to Kerr's line (M = 1, a = 0.7) in the two orders give the same charge v, the same |w| and opposite phases of w, "
              f"arg(1 + tanh b1 tanh b2 e^(i(d2 - d1))), each a solution (Ernst equations at 20 random points each; {_v40_r(wl)} over all): "
              + "; ".join(f"d = {d1:g}, {_v40_f(d2, 4)}, b = {b1:g}, {b2:g}: |v| = {_v40_f(av, 6)}, |w| = {_v40_f(aw, 6)}, phases "
                          f"+{_v40_f(al, 6)} and -{_v40_f(al, 6)}" for d1, b1, d2, b2, av, aw, al in rows_l) + ".  A phase of the mass "
              f"channel against the reference is a NUT charge (v39.0-5(a)), so both composites carry one, each with its Misner string, and neither is "
              f"asymptotically flat; the two orders give NUT charges of opposite sign at the same charge.  The two are mirror images: the second "
              f"line is the complex conjugate of the first at theta -> pi - theta with the charge's phase rotated, and a NUT charge is a "
              f"pseudoscalar, so the sign is physical relative to an orientation fixed beforehand, the seed's, and not otherwise.  This is a "
              f"holonomy of the kind the response proposes, within SU(2,1), with that proviso on its test that source data change; whether the "
              f"archive's excursions are these moves is not derived.")
    ok = (max(w[:4]) < 1e-12 and sig['out'][1] == 0 and sig['in'][1] == 0 and min(sig['out'][0], sig['in'][0]) > 20 and wt < 1e-12 and wn < 1e-12
          and wc < 1e-12 and wf < 1e-12 and abs(Spp + 2*math.pi*Mm*rp) < 1e-12 and abs(Sf(math.pi/2) - math.pi) < 1e-12 and 3.0e-39 < spread < 3.2e-39
          and wg < 1e-12 and res_c < 1e-12 and min(mn for _, mn, _ in res_v) > 1e-4 and wi < 1e-12 and span3 == npair and comm_orth < 1e-12
          and comm_min > 1e-3 and wj < 1e-12 and pos_ov + neg_ov == npair and nin > 500 and gin == nin and fixes < 1e-15 and wk < 1e-9
          and abs(-hq_all/(hM*hs) - 1) < 1e-9 and abs(wk2.imag + 0.368430) < 1e-6 and farR[1e4] < 1e-3 and farR[1e7] < 1e-6 and wl < 1e-12
          and min(r_[6] for r_ in rows_l) > 0.03)
    check(ok, "v40.0-1: <z, z> = |s - M|^2 - b^2 is the stationary limit, the sheet swap fixes s = M; a reference's complement is (1, 1) "
              "outside and (2, 0) inside; the far reference reads the tilt as Harrison's boost, sin p = tanh b; S''(0) = -2 pi M r+; the Hopf "
              "half-turn of a reference is the other sheet; a tilt that varies with r breaks the Ernst equations; two bodies' complements share one "
              "line and span the channels; sinh d = b/sqrt(<z, z>) from the far reference; a Harrison boost charges every body, m_i sinh b; two "
              "boosts in either order differ by opposite NUT phases")

def _v40_cG(xi, m, A):
    return (1 - xi*xi)*(1 + 2*m*A*xi)

def _v40_cdG(xi, m, A):
    return -2*xi*(1 + 2*m*A*xi) + 2*m*A*(1 - xi*xi)

def _v40_cweyl(x, y, m, A):
    """The C-metric's Weyl data in Hong and Teo's form: f = -G(y)/(A^2 (x - y)^2), rho = sqrt(-G(x) G(y))/(A^2 (x - y)^2),
    z = (1 - x y)(1 + m A (x + y))/(A^2 (x - y)^2); x and y may be jets."""
    pre = 1.0/(A*A*(x - y)*(x - y))
    Gx = (1 - x*x)*(1 + 2*m*A*x); Gy = (1 - y*y)*(1 + 2*m*A*y)
    return -1*Gy*pre, (-1*Gx*Gy).sqrt()*pre, (1 - x*y)*(1 + m*A*(x + y))*pre

def _v40_rodC(rho, z, m, A):
    """The C-metric's clock factor as rods: Schwarzschild's rod [-m/A, m/A] times the semi-infinite (Rindler) rod from 1/(2A^2)."""
    z1, z2, z3 = -m/A, m/A, 1/(2*A*A); R = lambda zi: math.sqrt(rho*rho + (z - zi)**2)
    return (R(z1) - (z - z1))/(R(z2) - (z - z2))*(R(z3) - (z - z3))

def v40_0_cmetric():
    """Entries 489-490: the C-metric beside Kerr (R565).  (a) Hong and Teo's form: (rho, z) are isothermal for the (x, y) two-metric, and the
    clock factor is Schwarzschild's rod [-m/A, m/A] times the semi-infinite rod from 1/(2A^2), the Rindler horizon's.  (b) One polynomial, three
    roots: the hole's horizon y = -1/(2mA), the Rindler horizon y = -1 sharing its root with the outer axis x = -1, and the inner axis x = 1;
    sum 1/G'(root) = 0 gives 1/kappa_R = 1/kappa_hole + 1/kappa_inner, so with the inner axis regular the outer axis's deficit fraction equals
    T_R/T_hole = 4 mu, mu = mA/(1 + 2mA), the string; with the outer axis regular the inner axis carries the strut's excess.
    (c) The swap of time and angle, f -> rho^2/f, maps the C-metric to a C-metric with 2mA -> (1 - 2mA)/(1 + 6mA), the two tensions adding to
    1/4, 2mA = 1/3 self-dual.  (d) Two Schwarzschild holes on the axis (Bach-Weyl): as the second grows the clock factor tends to the
    C-metric's, the strut's force to mA/(1 - 2mA); the rods' cross-ratio is (1 + 2mA)/(1 - 2mA).  (e) Without mass the slice is flat, the
    bispherical pair of foci at +-1/A.  (f) Kerr's s - M is the two rod-end distances with opposite phases, sin lam = a/M."""
    print("\n== v40.0-2. Entries 489-490: the C-metric beside Kerr -- rods, one polynomial's three roots, the swap of time and angle, two holes, "
          "the foci, and Kerr's rods (R565) ==")
    rng = random.Random(4002); m, A = 1.0, 0.12; u = 2*m*A
    S1 = _V40JetSpace(1); wi = 0.0; rat = []
    for _ in range(200):
        x0 = rng.uniform(-0.9, 0.9); y0 = rng.uniform(-1/u + 0.2, -1.1)
        X = _V40Jet.var(S1, 0, x0); Y = _V40Jet.var(S1, 1, y0)
        f, rho, z = _v40_cweyl(X, Y, m, A)
        rx, ry, zx, zy = rho.d(0).val(), rho.d(1).val(), z.d(0).val(), z.d(1).val()
        gx, gy = _v40_cG(x0, m, A), -_v40_cG(y0, m, A)
        nr, nz, cr = gx*rx*rx + gy*ry*ry, gx*zx*zx + gy*zy*zy, gx*rx*zx + gy*ry*zy
        wi = max(wi, abs(nr - nz)/nr, abs(cr)/nr)
    for _ in range(400):
        x0 = rng.uniform(-0.95, 0.95); y0 = rng.uniform(-1/u + 0.05, -1.02)
        pre = 1/(A*A*(x0 - y0)**2); f = -_v40_cG(y0, m, A)*pre; rho = math.sqrt(-_v40_cG(x0, m, A)*_v40_cG(y0, m, A))*pre
        z = (1 - x0*y0)*(1 + m*A*(x0 + y0))*pre; rat.append(f/_v40_rodC(rho, z, m, A))
    spread = (max(rat) - min(rat))/abs(rat[0])
    _v40_wrap(f"(a) Rods [T/V].  In Hong and Teo's form, m = 1, A = 0.12, the coordinates (rho, z) are isothermal for the two-metric dx^2/G(x) - "
              f"dy^2/G(y), G = (1 - xi^2)(1 + 2mA xi) (200 random points, the derivatives exact by jets, {_v40_r(wi)}); the clock factor f is a "
              f"constant times Schwarzschild's rod [-m/A, m/A] = [-{_v40_f(m/A, 6)}, {_v40_f(m/A, 6)}] times the semi-infinite rod from 1/(2A^2) = "
              f"{_v40_f(1/(2*A*A), 6)}, the Rindler horizon's (relative spread of the ratio at 400 points {_v40_r(spread)}).  The inertial background "
              f"is the limit in which the Rindler rod recedes to infinity.")
    kh, kR, ki = A*abs(_v40_cdG(-1/u, m, A))/2, A*abs(_v40_cdG(-1.0, m, A))/2, A*abs(_v40_cdG(1.0, m, A))/2
    res = 1/_v40_cdG(-1/u, m, A) + 1/_v40_cdG(-1.0, m, A) + 1/_v40_cdG(1.0, m, A)
    defr = 1 - kR/ki; mu = m*A/(1 + 2*m*A); wr = 0.0; exc = ki/kR - 1
    zax = lambda x0, y0: (1 - x0*y0)*(1 + m*A*(x0 + y0))/(A*A*(x0 - y0)**2)
    rz = random.Random(40021)
    zout = [zax(-1.0, rz.uniform(-1/u + 1e-3, -1.0 - 1e-3)) for _ in range(100)]
    zin = [zax(1.0, rz.uniform(-1/u + 1e-3, -1.0 - 1e-3)) for _ in range(100)]
    zfar = zax(-1.0, -1.0 - 1e-6)
    for _ in range(300):
        mm = rng.uniform(0.2, 3.0); AA = rng.uniform(0.01, 0.49)/mm; uu = 2*mm*AA
        rs = 1/_v40_cdG(-1/uu, mm, AA) + 1/_v40_cdG(-1.0, mm, AA) + 1/_v40_cdG(1.0, mm, AA)
        a1, a2, a3 = [abs(_v40_cdG(xx, mm, AA)) for xx in (-1/uu, -1.0, 1.0)]
        wr = max(wr, abs(rs), abs((1 - a2/a3) - a2/a1), abs((1 - a2/a3)/4 - mm*AA/(1 + 2*mm*AA)))
    _v40_wrap(f"(b) One polynomial, three roots [T/V].  The hole's horizon y = -1/(2mA), the Rindler horizon y = -1 -- the root it shares with the "
              f"outer axis x = -1 -- and the inner axis x = 1: surface gravities kappa_hole = {_v40_f(kh, 6)} and kappa_R = {_v40_f(kR, 6)} (v38.2's "
              f"0.235600 and 0.091200), the inner axis's factor {_v40_f(ki, 6)}.  The reciprocals of G' at the three roots sum to zero ({_v40_r(res)}; "
              f"300 random (m, A), {_v40_r(wr)}), which is 1/kappa_R = 1/kappa_hole + 1/kappa_inner: the periods 2 pi/kappa_R = "
              f"{_v40_f(2*math.pi/kR, 6)} and 2 pi/kappa_hole + 2 pi/kappa_inner = {_v40_f(2*math.pi/kh + 2*math.pi/ki, 6)}.  In Weyl's z the outer "
              f"axis is the half-axis z < -m/A that runs to infinity ({sum(v < -m/A for v in zout)} of 100 random points below -m/A, the point "
              f"next to the corner at {zfar:.2e}) and the inner axis the segment between the hole's rod and the Rindler rod "
              f"({sum(m/A < v < 1/(2*A*A) for v in zin)} of 100 between m/A and 1/(2A^2)).  With the inner axis regular, the outer axis carries "
              f"the deficit, as a fraction of the circle, 1 - kappa_R/kappa_inner = {_v40_f(defr, 6)} = kappa_R/kappa_hole = T_R/T_hole = "
              f"{_v40_f(kR/kh, 6)} = 4 mu, mu = mA/(1 + 2mA) = {_v40_f(mu, 6)}: v38.2's string, on the half-axis that reaches infinity.  "
              f"With the outer axis regular instead, the inner axis carries an excess, kappa_inner/kappa_R - 1 = {_v40_f(exc, 6)}, the strut.  No string "
              f"means a Rindler horizon infinitely colder "
              f"than the hole; equal temperatures need the whole circle as deficit, at 2mA = 1.")
    u2 = (1 - u)/(1 + 3*u); A2 = A*math.sqrt(2/(1 + 6*m*A)); m2 = u2/(2*A2); zs = (m/A + 1/(2*A*A))/2; vals = []
    for _ in range(400):
        x0 = rng.uniform(-0.95, 0.95); y0 = rng.uniform(-1/u + 0.05, -1.02)
        pre = 1/(A*A*(x0 - y0)**2); f = -_v40_cG(y0, m, A)*pre; rho = math.sqrt(-_v40_cG(x0, m, A)*_v40_cG(y0, m, A))*pre
        z = (1 - x0*y0)*(1 + m*A*(x0 + y0))*pre; vals.append((rho*rho/f)/_v40_rodC(rho, -z + zs, m2, A2))
    sp2 = (max(vals) - min(vals))/abs(vals[0]); mu2 = u2/(2*(1 + u2)); uback = (1 - u2)/(1 + 3*u2)
    _v40_wrap(f"(c) The swap of time and angle [T/V].  f -> rho^2/f, which turns horizons into axes and axes into horizons, maps the C-metric to a "
              f"C-metric, the hole's rod and the gap to the Rindler rod exchanged: 2mA = {_v40_f(u, 6)} -> (1 - 2mA)/(1 + 6mA) = {_v40_f(u2, 6)}, "
              f"m' = {_v40_f(m2, 6)}, A' = {_v40_f(A2, 6)} (the ratio's relative spread at 400 points {_v40_r(sp2)}); the map is an involution "
              f"(back to {_v40_f(uback, 6)}), the tensions mu = {_v40_f(mu, 6)} and mu' = {_v40_f(mu2, 6)} add to {_v40_f(mu + mu2, 6)}, and 2mA = "
              f"1/3 is self-dual.  The C-metric, not Kerr, is the self-dual object of this swap.")
    d = 1/(2*m*A); pts = [(rng.uniform(0.2, 3.0), rng.uniform(-3.0, 3.5)) for _ in range(200)]; two = []
    def f_two(rho, z, mb):
        R = lambda zi: math.sqrt(rho*rho + (z - zi)**2)
        return (R(-1.0) - (z + 1.0))/(R(1.0) - (z - 1.0))*(R(d) - (z - d))/(R(d + 2*mb) - (z - d - 2*mb))
    def f_one(rho, z):
        R = lambda zi: math.sqrt(rho*rho + (z - zi)**2)
        return (R(-1.0) - (z + 1.0))/(R(1.0) - (z - 1.0))*(R(d) - (z - d))
    for mb in (1e2, 1e4, 1e6):
        err = max(abs(f_two(r_, z_, mb)*2*(d + 2*mb)/f_one(r_, z_) - 1) for r_, z_ in pts)
        zc = d + mb; two.append((mb, err, 1.0*mb/(zc*zc - (1.0 + mb)**2)))
    chi = (d + 1)/(d - 1)
    _v40_wrap(f"(d) Two holes [T/V].  Bach and Weyl's two Schwarzschild holes on the axis, the first's rod [-1, 1] in units of its half-length and "
              f"the second's starting at 1/(2mA): as the second grows, the clock factor tends to the C-metric's, " + "; ".join(
              f"{err:.2e} at a mass ratio of {mb:.0e} (strut force {_v40_f(F, 6)})" for mb, err, F in two) + f", against the C-metric's strut "
              f"mA/(1 - 2mA) = {_v40_f(m*A/(1 - 2*m*A), 6)}, its defect placed between the horizons instead of outside them.  The rods' cross-ratio "
              f"is (1 + 2mA)/(1 - 2mA) = {_v40_f(chi, 6)}, the string (1 - 1/chi)/4 = {_v40_f((1 - 1/chi)/4, 6)} and the strut (chi - 1)/4 = "
              f"{_v40_f((chi - 1)/4, 6)}.  So the C-metric is a Schwarzschild hole near the horizon of a huge companion, Astorino's reading "
              f"(arXiv:2312.00865).")
    wfl = 0.0
    for _ in range(200):
        x0 = rng.uniform(-0.9, 0.9); y0 = rng.uniform(-6.0, -1.1)
        X = _V40Jet.var(S1, 0, x0); Y = _V40Jet.var(S1, 1, y0)
        Zc = (Y*Y - 1).sqrt()/(A*(X - Y)); Rc = (1 - X*X).sqrt()/(A*(X - Y))
        zx, zy, rx, ry = Zc.d(0).val(), Zc.d(1).val(), Rc.d(0).val(), Rc.d(1).val(); pre = 1/(A*A*(x0 - y0)**2)
        wfl = max(wfl, abs((zx*zx + rx*rx)/(pre/(1 - x0*x0)) - 1), abs((zy*zy + ry*ry)/(pre/(y0*y0 - 1)) - 1),
                  abs(zx*zy + rx*ry)*math.sqrt((1 - x0*x0)*(y0*y0 - 1))/pre)
    Mk, ak = 1.0, 0.7; ck = math.sqrt(Mk*Mk - ak*ak); lam = math.asin(ak/Mk); wk = 0.0
    for _ in range(200):
        r = rng.uniform(Mk + ck + 0.05, 8.0); th = rng.uniform(0.05, 3.09)
        Dl = r*r - 2*Mk*r + ak*ak; rho = math.sqrt(Dl)*math.sin(th); z = (r - Mk)*math.cos(th)
        Rp, Rm = math.hypot(rho, z + ck), math.hypot(rho, z - ck); s = complex(r, -ak*math.cos(th))
        wk = max(wk, abs((s - Mk) - (Mk/(2*ck))*(cmath.exp(-1j*lam)*Rp + cmath.exp(1j*lam)*Rm)))
    _v40_wrap(f"(e) Without mass [T/V]: the C-metric's slice is flat, (z, rho) = (sqrt(y^2 - 1), sqrt(1 - x^2))/(A(x - y)) its bispherical "
              f"coordinates (exact by jets, {_v40_r(wfl)}), with the foci at z = +-1/A = +-{_v40_f(1/A, 6)}: the hole and its mirror partner, a real "
              f"pair, where Kerr's massless limit has the imaginary pair +-ia (v38.2).  (f) Kerr's rods [T/V]: Kerr's rod is [-c, c], c = sqrt(M^2 - "
              f"a^2) = {_v40_f(ck, 6)} at M = 1, a = 0.7, and s - M = (M/2c)(e^(-i lam) R+ + e^(i lam) R-), R+- the distances to the rod's ends, "
              f"sin lam = a/M ({_v40_r(wk)}, 200 points): spin gives the two ends opposite phases, while acceleration adds a rod and leaves the line "
              f"alone.  [D] The rotation's plane x-y and the boost's plane t-z are Hodge duals; every static Killing horizon has Ernst potential E = 0, "
              f"so the two horizons share their image in the target space, a finite rod and a semi-infinite one mapping onto it.")
    ok = (wi < 1e-12 and spread < 1e-12 and abs(res) < 1e-12 and wr < 1e-12 and abs(defr - kR/kh) < 1e-12 and abs(defr - 4*mu) < 1e-12
          and all(v < -m/A for v in zout) and zfar < -1e5 and all(m/A < v < 1/(2*A*A) for v in zin) and abs(exc - m*A/(1 - 2*m*A)*4) < 1e-12
          and sp2 < 1e-12 and abs(mu + mu2 - 0.25) < 1e-12 and abs(uback - u) < 1e-12 and two[2][1] < 2e-6 and abs(two[2][2] - m*A/(1 - 2*m*A)) < 1e-5
          and wfl < 1e-12 and wk < 1e-12)
    check(ok, "v40.0-2: the C-metric's clock is Schwarzschild's rod times Rindler's; sum 1/G' = 0 makes the deficit fraction T_R/T_hole = 4 mu; "
              "the time-angle swap maps it to a C-metric with mu + mu' = 1/4; two holes tend to it, the strut to mA/(1 - 2mA)")

def _v40_acc_kerr(S, r0, th0, M, a, A, L=None, q=0.0):
    """The accelerating Kerr(-Newman)(-de Sitter) metric in Griffiths and Podolsky's form, jets in (r, theta) -- the jet variables 0 and 1:
    ds^2 = Omega^-2 {-(Q/rho^2)(dt - a sin^2 th dphi)^2 + rho^2 dr^2/Q + rho^2 dth^2/P + (P sin^2 th/rho^2)(a dt - (r^2 + a^2) dphi)^2},
    Omega = 1 - A r cos th, rho^2 = r^2 + a^2 cos^2 th, P = 1 - 2AM cos th + (A^2 (a^2 + q^2) + Lam a^2/3) cos^2 th,
    Q = (r^2 - 2Mr + a^2 + q^2)(1 - A^2 r^2) - (Lam/3)(a^2 + r^2) r^2, Lam = 3/L^2 (zero when L is None)."""
    lam3 = 0.0 if L is None else 1.0/(L*L)
    r = _V40Jet.var(S, 0, r0); th = _V40Jet.var(S, 1, th0); c = th.cos(); sn = th.sin(); s2 = sn*sn
    Om = 1 - A*r*c; rho2 = r*r + a*a*c*c
    P = 1 - 2*A*M*c + (A*A*(a*a + q*q) + lam3*a*a)*c*c
    Q = (r*r - 2*M*r + a*a + q*q)*(1 - A*A*r*r) - lam3*(a*a + r*r)*r*r
    z = _v40_zero(S, S.N); g = [[z for _ in range(4)] for _ in range(4)]; W = (Om*Om).recip()
    g[0][0] = (-1*Q + P*s2*a*a)/rho2*W
    g[0][3] = g[3][0] = (Q*a*s2 - P*s2*a*(r*r + a*a))/rho2*W
    g[3][3] = (-1*Q*a*a*s2*s2 + P*s2*(r*r + a*a)*(r*r + a*a))/rho2*W
    g[1][1] = rho2/Q*W; g[2][2] = rho2/P*W
    return g

def v40_0_rectangle():
    """Entries 491-492 and the follow-up of 20 November: the region between the two horizons (R566).  (a) The static C-metric's region between
    the hole's horizon and the Rindler horizon, with time made periodic, is a conformal rectangle with sides hole horizon, inner axis, Rindler
    horizon, outer axis; its elliptic modulus k^2 = 2u/(1 + u) = 4 mu = T_R/T_hole (u = 2mA), k'^2 the ratio of the axes' conical factors; its
    aspect K(k')/K(k); the time-angle swap a quarter turn (k <-> k'); the square at 2mA = 1/3; a conformal midline.  (b) Its corners: the
    regular periods, the corner at infinity flat C^2 turned inside out with equal periods, the finite corners' shares k^2 and k'^2; the string
    k^2/4 and the strut k^2/(4 k'^2).  (c) The accelerating Kerr hole (Griffiths and Podolsky): vacuum; each horizon turning at
    Omega = a/(r^2 + a^2) at its own radius; the surface gravities; four roots and the sum rule with the inner horizon's minus sign; the
    charged static version; with spin the rectangle's k^2 no longer the deficit.  (d) A change of reference does not carry probes: the light
    ring of the tilted closing in the line's coordinate."""
    print("\n== v40.0-3. Entries 491-492 and the follow-up of 20 November: the region between the two horizons -- the rectangle, its corners, "
          "the accelerating Kerr hole and the sum rule with four roots, and a light ring that a reference does not carry (R566) ==")
    m, A = 1.0, 0.12; u = 2*m*A; k2 = 2*u/(1 + u); kk = math.sqrt(k2)
    def rect(uu):
        e1, e2, e3 = -1/uu, -1.0, 1.0
        X = _v40_simpson(lambda p: 2/math.sqrt(uu*((e2 + (e3 - e2)*math.sin(p)**2) - e1)), 0, math.pi/2, 4000)
        Y = _v40_simpson(lambda p: 2/math.sqrt(uu*(e3 - (e1 + (e2 - e1)*math.sin(p)**2))), 0, math.pi/2, 4000)
        return X, Y
    X, Y = rect(u); asp = _v40_ellipK(1 - k2)/_v40_ellipK(k2); u2 = (1 - u)/(1 + 3*u); X2, Y2 = rect(u2); Xs, Ys = rect(1/3)
    e1, e2 = -1/u, -1.0; ymid = e1 + (e2 - e1)/(1 + kk)
    hint = lambda p: (2*math.cos(p)/math.sqrt(u*(1.0 - (e1 + (ymid - e1)*math.sin(p)**2)))
                      *math.sqrt((ymid - e1)/(e2 - (e1 + (ymid - e1)*math.sin(p)**2))))
    half = _v40_simpson(hint, 0, math.pi/2, 4000)
    G = lambda xi: _v40_cG(xi, m, A); dG = lambda xi: _v40_cdG(xi, m, A)
    ax_out, ax_in = abs(dG(-1.0)), abs(dG(1.0))
    _v40_wrap(f"(a) The rectangle [T/V].  With time periodic, the static C-metric's two-metric between the horizons, m = 1, A = 0.12, is conformal "
              f"to a rectangle whose sides are the hole's horizon, the inner axis, the Rindler horizon and the outer axis: width (axis to axis) "
              f"{_v40_f(X, 6)} and height (horizon to horizon) {_v40_f(Y, 6)} by quadrature, aspect {_v40_f(Y/X, 6)} = K(k')/K(k) = {_v40_f(asp, 6)}, "
              f"the complete elliptic integrals by the arithmetic-geometric mean, with k^2 = 2u/(1 + u) = {_v40_f(k2, 6)}, u = 2mA, which is 4 mu "
              f"and T_R/T_hole (v40.0-2(b)), and k'^2 = {_v40_f(1 - k2, 6)} = the axes' conical factors' ratio {_v40_f(ax_out/ax_in, 6)}.  The swap "
              f"of time and angle (v40.0-2(c)) turns the rectangle a quarter turn: the dual's aspect is {_v40_f(Y2/X2, 6)} = 1/{_v40_f(Y/X, 6)}, and "
              f"2mA = 1/3 is the square ({_v40_f(Ys/Xs, 6)}).  The conformal midline between the horizons is y = {_v40_f(ymid, 6)}, r = -1/(Ay) = "
              f"{_v40_f(-1/(A*ymid), 6)}, between the hole at 2 and the Rindler horizon at {_v40_f(1/A, 6)} (the integral to it over the whole: "
              f"{_v40_f(half/Y, 6)}) -- a conformal midpoint, not a proper-distance one.  The string determines the shape.")
    kh, k1, kp = abs(dG(-1/u))/2, abs(dG(-1.0))/2, abs(dG(1.0))/2
    Pinf, bh, din = 2*math.pi/k1, 2*math.pi/kh, 2*math.pi/kp
    def eu(x, y):
        pre = 1/(A*A*(x - y)**2); return (-G(y)*pre, pre/(-G(y)), pre/G(x), G(x)*pre)
    rinf = []; rfin = []
    for eps in (1e-2, 1e-4, 1e-6):
        a_, b_ = math.sqrt(eps), math.sqrt(2*eps)
        x, y = -1 + (1 - u)*a_*a_/2, -1 - (1 - u)*b_*b_/2; gtt, gyy, gxx, gpp = eu(x, y)
        pref = 4/(A*A*(1 - u)**2*(a_*a_ + b_*b_)**2); dyb, dxa = -(1 - u)*b_, (1 - u)*a_
        rinf.append(max(abs(v - 1) for v in (gtt/(pref*(1 - u)**2*b_*b_), gyy*dyb*dyb/pref, gxx*dxa*dxa/pref, gpp/(pref*(1 - u)**2*a_*a_))))
        x, y = 1 - kp*a_*a_/2, -1/u + kh*b_*b_/2; gtt, gyy, gxx, gpp = eu(x, y); pref = 1/(A*A*(1 + 1/u)**2)
        rfin.append(max(abs(v - 1) for v in (gtt/(pref*kh**2*b_*b_), gyy*(kh*b_)**2/pref, gxx*(kp*a_)**2/pref, gpp/(pref*kp**2*a_*a_))))
    _v40_wrap(f"(b) The corners [T/V].  Regular periods, in Hong and Teo's t and phi: the Rindler horizon {_v40_f(Pinf, 6)}, the same as the outer "
              f"axis's (one root); the hole's horizon {_v40_f(bh, 6)}; the inner axis {_v40_f(din, 6)}; the last two add to {_v40_f(bh + din, 6)}, "
              f"their shares of the period at infinity {_v40_f(bh/Pinf, 6)} = k^2 and {_v40_f(din/Pinf, 6)} = k'^2.  Each corner is locally flat "
              f"C^2 with its two complex lines a horizon and an axis, and the Hopf rotation is boost and rotation turning together: at the corner at "
              f"infinity the metric is flat C^2 turned inside out, 4|dz|^2/(A^2 (1 - u)^2 |z|^4), with equal periods (exact over model within "
              + ", ".join(f"{e:.1e}" for e in rinf) + f" at |z|^2 = 3e-2, 3e-4, 3e-6), so the quarter turn is the leaf's own swap there; at the finite "
              f"corner of the hole and the inner axis the weights are unequal (within " + ", ".join(f"{e:.1e}" for e in rfin) + f").  The string "
              f"(defect outside) is k^2/4 = {_v40_f(k2/4, 6)} and the strut (defect between) k^2/(4 k'^2) = {_v40_f(k2/(4*(1 - k2)), 6)}.")
    M, a = 1.0, 0.7; rp, rm = M + math.sqrt(M*M - a*a), M - math.sqrt(M*M - a*a)
    S2 = _V40JetSpace(2); wv = 0.0; rng = random.Random(4003)
    for _ in range(4):
        r0 = rng.uniform(rp + 0.3, 1/A - 1.0); th0 = rng.uniform(0.4, 2.7)
        Ric = _v40_ricci(_v40_acc_kerr(S2, r0, th0, M, a, A), [1, 2])[0]; wv = max(wv, _v40_maxabs(Ric))
    Omf = lambda r: a/(r*r + a*a)
    kpf = (rp - rm)*(1 - A*A*rp*rp)/(2*(rp*rp + a*a)); kaf = A*(1 - 2*M*A + a*a*A*A)/(1 + a*a*A*A)
    S1 = _V40JetSpace(1)
    def kap(rh, side):
        out = []
        for th0 in (0.7, 1.9):
            for eps in (1e-5, 2e-5):
                g = _v40_acc_kerr(S1, rh + side*eps, th0, M, a, A); Oh = Omf(rh)
                N = -1*(g[0][0] + 2*Oh*g[0][3] + Oh*Oh*g[3][3]); grr = 1/g[1][1].val()
                out.append((eps, math.sqrt(grr*N.d(0).val()**2/(4*N.val()))))
        return [2*out[2*i][1] - out[2*i + 1][1] for i in range(2)]
    kh_num, ka_num = kap(rp, +1), kap(1/A, -1)
    Gq = lambda xi, r1, r2: (1 - xi*xi)*(1 + r1*A*xi)*(1 + r2*A*xi)
    def dGq(xi, r1, r2):
        X1 = _V40Jet.var(S1, 0, xi); return ((1 - X1*X1)*(1 + r1*A*X1)*(1 + r2*A*X1)).d(0).val()
    roots = [-1/(rm*A), -1/(rp*A), -1.0, 1.0]; sres = sum(1/dGq(x, rp, rm) for x in roots)
    kq = [A*abs(dGq(x, rp, rm))/2 for x in roots]; defi = 1 - kq[2]/kq[3]; kmf = kq[0]*rm*rm/(rm*rm + a*a)
    rhs = (kaf/(1 - a*Omf(1/A)))*((1 - a*Omf(rp))/kpf - (1 - a*Omf(rm))/kmf); four_mu = 4*M*A/(1 + 2*M*A + a*a*A*A)
    q = 0.5; Rp, Rm = M + math.sqrt(M*M - q*q), M - math.sqrt(M*M - q*q)
    kc = [A*abs(dGq(x, Rp, Rm))/2 for x in (-1/(Rm*A), -1/(Rp*A), -1.0, 1.0)]
    e1, e2, e3, e4 = -1/(rm*A), -1/(rp*A), -1.0, 1.0; lead = rp*rm*A*A
    Xa = _v40_simpson(lambda t: 2/math.sqrt(lead*((e3 + (e4 - e3)*math.sin(t)**2) - e1)*((e3 + (e4 - e3)*math.sin(t)**2) - e2)), 0, math.pi/2, 4000)
    Ya = _v40_simpson(lambda t: 2/math.sqrt(lead*((e2 + (e3 - e2)*math.sin(t)**2) - e1)*(e4 - (e2 + (e3 - e2)*math.sin(t)**2))), 0, math.pi/2, 4000)
    k2a = (e4 - e3)*(e2 - e1)/((e4 - e2)*(e3 - e1))
    _v40_wrap(f"(c) With spin [T/V].  The accelerating Kerr hole in Griffiths and Podolsky's form, M = 1, A = 0.12, a = 0.7, is vacuum (Ricci at "
              f"four points, exact by jets, {_v40_r(wv)}).  Each horizon turns at Omega = a/(r^2 + a^2) at its own radius: the hole at "
              f"{_v40_f(Omf(rp), 6)}, the Rindler horizon r = 1/A at {_v40_f(Omf(1/A), 6)}, their difference {_v40_f(Omf(rp) - Omf(1/A), 6)} the "
              f"part independent of the rotating frame.  Their surface gravities, from the metric (the limit by two offsets): hole "
              + ", ".join(_v40_f(x, 6) for x in kh_num) + f" against (r+ - r-)(1 - A^2 r+^2)/(2(r+^2 + a^2)) = {_v40_f(kpf, 6)}; Rindler "
              + ", ".join(_v40_f(x, 6) for x in ka_num) + f" against A(1 - 2MA + a^2 A^2)/(1 + a^2 A^2) = {_v40_f(kaf, 6)}.  The angular polynomial "
              f"has four roots, -1/(r- A), -1/(r+ A), -1 and 1, and the reciprocals of its derivative there sum to zero ({_v40_r(sres)}); with "
              f"the inner horizon's minus sign the sum rule reads deficit/2 pi = [kappa_R/(1 - a Omega_R)] [(1 - a Omega+)/kappa+ - (1 - a "
              f"Omega-)/kappa-] = {_v40_f(rhs, 6)} = 1 - (axes' factors) = {_v40_f(defi, 6)} = 4MA/(1 + 2MA + a^2 A^2) = {_v40_f(four_mu, 6)}, where "
              f"the two horizons alone give {_v40_f(kaf/kpf, 6)}.  Charge without spin, q = 0.5: deficit/2 pi = {_v40_f(1 - kc[2]/kc[3], 6)} = "
              f"T_R/T_outer - T_R/T_inner = {_v40_f(kc[2]/kc[1] - kc[2]/kc[0], 6)}.  With spin the rectangle's modulus and the string separate: "
              f"k^2 = {_v40_f(k2a, 6)} (aspect {_v40_f(Ya/Xa, 6)} = K(k')/K(k) = {_v40_f(_v40_ellipK(1 - k2a)/_v40_ellipK(k2a), 6)}) against the "
              f"deficit {_v40_f(four_mu, 6)}; at a = 0 both are {_v40_f(k2, 6)}.")
    def ring(p, M=1.0):
        c = math.cos(p)
        F = lambda r: 4*c/((r - M)*c + M) - (2*r - 2*M)/(r*r - 2*M*r)
        return _v40_bisect(F, 2.0001, 50.0)
    rows = []
    for pd in (0.0, 10.0, 30.0, 60.0):
        p = math.radians(pd); cc = 1/math.cos(p)
        rows.append((pd, ring(p), (3*cc + math.sqrt(9*cc*cc - 8*math.tan(p)**2))/2 - (cc - 1)))
    _v40_wrap(f"(d) A light ring that the reference does not carry [T/V].  Tilt Schwarzschild's reference by p: the tilted closing's clock is "
              f"f = -g_tt = Delta/|(r - M) cos p + M|^2 in the line's own coordinate r, the closing keeping Weyl's rho^2 = Delta sin^2 theta, so "
              f"its light ring, where g_phiphi/(-g_tt) = rho^2/f^2 is extremal in the equatorial plane, d ln(Delta/f^2)/dr = 0, sits at r = "
              f"" + ", ".join(f"{_v40_f(x, 6)} at {pd:g} degrees" for pd, x, y in rows) + " (the charged "
              f"hole's formula moved back to r: " + ", ".join(_v40_f(y, 6) for pd, x, y in rows) + "), where Schwarzschild's is at r = 3: a "
              f"change of reference relocates points of the line exactly, but a probe's orbit has to be recomputed in each closing.  The "
              f"round's first numbers, 3.154701 and 3.259576 at 30 degrees, were in the tilted hole's own coordinate.")
    ok = (abs(Y/X - asp) < 1e-9 and abs(k2 - 4*m*A/(1 + 2*m*A)) < 1e-12 and abs(1 - k2 - ax_out/ax_in) < 1e-12 and abs(Y2/X2 - X/Y) < 1e-9
          and abs(Ys/Xs - 1) < 1e-9 and abs(half/Y - 0.5) < 1e-6 and abs(bh + din - Pinf) < 1e-9 and abs(bh/Pinf - k2) < 1e-12
          and rinf[2] < 1e-5 and rfin[2] < 1e-5 and wv < 1e-10 and max(abs(x - kpf) for x in kh_num) < 1e-6 and max(abs(x - kaf) for x in ka_num) < 1e-6
          and abs(sres) < 1e-12 and abs(rhs - defi) < 1e-12 and abs(defi - four_mu) < 1e-12 and abs((1 - kc[2]/kc[3]) - (kc[2]/kc[1] - kc[2]/kc[0])) < 1e-12
          and abs(Ya/Xa - _v40_ellipK(1 - k2a)/_v40_ellipK(k2a)) < 1e-8 and all(abs(x - y) < 1e-9 for pd, x, y in rows) and abs(rows[0][1] - 3) < 1e-9)
    check(ok, "v40.0-3: the region between the horizons is a rectangle of modulus k^2 = 4 mu = T_R/T_hole, turned a quarter turn by the swap, "
              "square at 2mA = 1/3; accelerating Kerr is vacuum and its four roots give the sum rule 4MA/(1 + 2MA + a^2 A^2); a tilt moves the "
              "light ring")

def v40_0_throat():
    """Entry 493 and the follow-up of 20 November: the throat, the entropy along the sphere, and the Higgs condition (R567).  (a) Along the
    sphere of references at fixed mass, without spin, the hole (M, M sin p): S/S_Schw = (1 + cos p)^2/4 and T/T_Schw = 4 cos p/(1 + cos p)^2 --
    the throat is the cold, low-entropy end.  (b) The Hawking temperature equals the electroweak crossover, 159.5 GeV, only for holes of at most
    6.6e7 kg.  (c) The Higgs closing of v39.0-11 breaks the symmetry when |kappa|^2 > m0^2 M_perp^2; with the Higgs and its response field two
    positive-norm directions in a located reference's complement and the mass form the reference's, m_eff^2 = -mu^2 <h, h> sinh^2 d outside the
    stationary limit and +mu^2 <h, h> sin^2 theta inside -- a reversed and an ordinary Cauchy-Schwarz inequality."""
    print("\n== v40.0-4. Entry 493 and the follow-up of 20 November: the throat, the entropy along the sphere, the electroweak temperature, and "
          "the Higgs condition as a reversed Cauchy-Schwarz inequality (R567) ==")
    rows = []
    for pd in (0.0, 30.0, 60.0, 89.0, 90.0):
        cp = max(math.cos(math.radians(pd)), 0.0); rows.append((pd, (1 + cp)**2/4, 4*cp/(1 + cp)**2))
    wst = 0.0; rng = random.Random(4004)
    for _ in range(200):
        p = rng.uniform(0, 1.55); M = rng.uniform(0.5, 3); q = M*math.sin(p); rp = M + math.sqrt(M*M - q*q); rm = M - math.sqrt(M*M - q*q)
        S = math.pi*rp*rp; T = (rp - rm)/(4*math.pi*rp*rp)
        wst = max(wst, abs(S/(4*math.pi*M*M) - (1 + math.cos(p))**2/4), abs(T*8*math.pi*M - 4*math.cos(p)/(1 + math.cos(p))**2))
    _v40_wrap(f"(a) The throat's end [T/V].  Without spin, the tilted hole of mass M has charge M sin p, r+ = M(1 + cos p), S/S_Schw = (1 + cos "
              f"p)^2/4 and T/T_Schw = 4 cos p/(1 + cos p)^2 (200 random holes, {_v40_r(wst)}): " + "; ".join(
              f"{pd:g} degrees: S {_v40_f(s_, 6)}, T {_v40_f(t_, 6)}" for pd, s_, t_ in rows) + ".  The entropy falls from 4 pi M^2 to pi M^2 and "
              f"the temperature to zero: the throat is the cold, low-entropy end, and by the only entropy the archive computes the ordinary "
              f"reference is the maximum.")
    hbar, cl, Gn, kB, eV = 1.054571817e-34, 299792458.0, 6.67430e-11, 1.380649e-23, 1.602176634e-19
    Tc = 159.5e9*eV/kB; Mew = hbar*cl**3/(8*math.pi*Gn*kB*Tc); Msun = 1.3271244e20/Gn; Tsun = hbar*cl**3/(8*math.pi*Gn*kB*Msun)
    _v40_wrap(f"(b) The electroweak temperature [V].  A hole is hotter than the electroweak crossover, 159.5 GeV (D'Onofrio and Rummukainen "
              f"2016), only below M = hbar c^3/(8 pi G k_B T) = {Mew:.3e} kg (CODATA 2022's constants); a solar-mass hole is at {Tsun:.2e} K.  So "
              f"the lever does nothing in practice.")
    def herm(x, y): return x[0]*y[0].conjugate() + x[1]*y[1].conjugate() - x[2]*y[2].conjugate()
    Mk, ak, qk = 1.0, 0.7, 0.5; stats = {}
    for label, pts in (("outside", [(6.0, 1.0), (3.0, 0.4), (2.2, 1.5)]), ("inside", [(1.7, 1.0), (1.0, 1.5708), (1.3, 1.2)])):
        neg = pos = 0; worst = 0.0; ffs = []
        for r, th in pts:
            s = complex(r, -ak*math.cos(th)); z = [s - Mk, qk, Mk]; zz = herm(z, z).real; ffs.append(zz)
            def draw():
                while True:
                    v = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]; c_ = herm(v, z)/zz; v = [v[i] - c_*z[i] for i in range(3)]
                    if herm(v, v).real > 1e-6: return v
            for _ in range(2000):
                h, x = draw(), draw(); ghh, gxx, ghx = herm(h, h).real, herm(x, x).real, herm(h, x)
                schur = ghh - abs(ghx)**2/gxx; c2 = abs(ghx)**2/(ghh*gxx)
                if label == "outside": worst = max(worst, abs(schur/ghh + math.sinh(math.acosh(math.sqrt(c2)))**2)/(1 + c2))
                else: worst = max(worst, abs(schur/ghh - math.sin(math.acos(math.sqrt(min(c2, 1.0))))**2))
                neg += schur < 0; pos += schur > 0
        stats[label] = (neg, pos, worst, ffs)
    o, i_ = stats["outside"], stats["inside"]
    _v40_wrap(f"(c) The Higgs condition [T/V/S].  v39.0-11's closing turns the mass term negative when |kappa|^2 > m0^2 M_perp^2.  Premise: the "
              f"Higgs h and its response field x are two positive-norm directions in the complement of a located reference z (v40.0-1(b)), with "
              f"m0^2 = mu^2 <h, h>, M_perp^2 = mu^2 <x, x> and kappa = mu^2 <h, x>.  Then m_eff^2 = mu^2 (<h, h> - |<h, x>|^2/<x, x>).  At three "
              f"references outside the stationary limit (<z, z> = " + ", ".join(_v40_f(v, 4) for v in o[3]) + f"), m_eff^2 < 0 in {o[0]} of "
              f"{o[0] + o[1]} random pairs, equal to -mu^2 <h, h> sinh^2 d, d their hyperbolic angle ({_v40_r(o[2])}): the reversed Cauchy-Schwarz "
              f"inequality of a form of signature (1, 1), so that this count and the next check the code, not the claim.  At three inside "
              f"(" + ", ".join(_v40_f(v, 4) for v in i_[3]) + f"), m_eff^2 > 0 in "
              f"{i_[1]} of {i_[0] + i_[1]}, equal to +mu^2 <h, h> sin^2 theta ({_v40_r(i_[2])}): no breaking.  Given the premise, v39's inequality "
              f"among three parameters becomes one statement about signature; the premise, and where the positive kinetic form comes from, are "
              f"not derived, and the reading is indexed by where the reference sits, not by a place in spacetime.")
    ok = (wst < 1e-12 and abs(rows[2][1] - 0.5625) < 1e-12 and 6.6e7 < Mew < 6.7e7 and o[0] == 6000 and i_[1] == 6000 and o[2] < 1e-12 and i_[2] < 1e-12
          and all(v > 0 for v in o[3]) and all(v < 0 for v in i_[3]))
    check(ok, "v40.0-4: along the sphere S/S_Schw = (1 + cos p)^2/4 and T/T_Schw = 4 cos p/(1 + cos p)^2; the crossover hole is 6.6e7 kg; with the "
              "premise, m_eff^2 < 0 outside the stationary limit and > 0 inside, 6000 of 6000 each")

_V40_ETA = (-1.0, 1.0, 1.0, 1.0)

def _v40_ks_funcs(x, M, a, A):
    t, r, th, ph = x; c, s = cmath.cos(th), cmath.sin(th)
    Om = 1 - A*r*c; rho = cmath.sqrt(r*r + a*a*c*c); P = 1 - 2*A*M*c + A*A*a*a*c*c; Q = (a*a - 2*M*r + r*r)*(1 - A*A*r*r)
    return c, s, Om, rho, P, Q

def _v40_ks_coframe(x, M, a, A):
    """The accelerating Kerr hole's coframe: e0 = sqrt(Q)/(rho Omega)(dt - a sin^2 dphi), e1 = rho/(sqrt(Q) Omega) dr, e2 = rho/(sqrt(P) Omega)
    dtheta, e3 = sqrt(P) sin/(rho Omega)(a dt - (r^2 + a^2) dphi); complex arithmetic, so that a complex step differentiates it."""
    c, s, Om, rho, P, Q = _v40_ks_funcs(x, M, a, A); r = x[1]; sq, sp = cmath.sqrt(Q), cmath.sqrt(P)
    e = [[0j]*4 for _ in range(4)]
    e[0][0] = sq/rho/Om; e[0][3] = -a*s*s*sq/rho/Om; e[1][1] = rho/sq/Om; e[2][2] = rho/sp/Om
    e[3][0] = a*sp*s/rho/Om; e[3][3] = -(r*r + a*a)*sp*s/rho/Om
    return e

def _v40_ks_metric(x, M, a, A):
    e = _v40_ks_coframe(x, M, a, A)
    return [[sum(_V40_ETA[B]*e[B][i]*e[B][j] for B in range(4)) for j in range(4)] for i in range(4)]

def _v40_ks_christoffel(x, M, a, A):
    g0 = [[v.real for v in row] for row in _v40_ks_metric(x, M, a, A)]; gi = [[v.real for v in row] for row in _v40_inv(g0)]
    dg = [[[0.0]*4 for _ in range(4)] for _ in range(4)]
    for k in (1, 2):
        xs = list(map(complex, x)); xs[k] += 1e-30j; gs = _v40_ks_metric(xs, M, a, A)
        for i in range(4):
            for j in range(4): dg[k][i][j] = gs[i][j].imag/1e-30
    Gm = [[[sum(gi[l][q]*(dg[j][q][k] + dg[k][q][j] - dg[q][j][k]) for q in range(4))/2 for k in range(4)] for j in range(4)] for l in range(4)]
    return Gm, g0, gi

def _v40_ks_d4(f, x, k, h=2e-3):
    """A fourth-order central difference along coordinate k of an array-valued function."""
    def at(d):
        y = list(x); y[k] += d; return f(y)
    fp2, fp1, fm1, fm2 = at(2*h), at(h), at(-h), at(-2*h)
    def comb(a2, a1, b1, b2):
        if isinstance(a2, list): return [comb(*z) for z in zip(a2, a1, b1, b2)]
        return (-a2 + 8*a1 - 8*b1 + b2)/(12*h)
    return comb(fp2, fp1, fm1, fm2)

def _v40_ks_sg(x, M, a, A, eps):
    c, s, Om, rho, P, Q = _v40_ks_funcs(x, M, a, A); return (x[1] + 1j*eps*a*c)/Om

def _v40_ks_Y(x, M, a, A, eps, sig):
    e = _v40_ks_coframe(x, M, a, A); S = _v40_ks_sg(x, M, a, A, eps)
    return [[S*((e[0][i]*e[1][j] - e[0][j]*e[1][i]) + 1j*sig*(e[2][i]*e[3][j] - e[2][j]*e[3][i])) for j in range(4)] for i in range(4)]

def _v40_ks_cky(x, M, a, A, eps, sig):
    """The conformal Killing-Yano residual of Y, relative to the size of its covariant derivative, and its divergence xi = (1/3) div Y."""
    G, g, gi = _v40_ks_christoffel(x, M, a, A); Y = _v40_ks_Y(x, M, a, A, eps, sig)
    dY = [None]*4; z = [[0j]*4 for _ in range(4)]; dY[0] = z; dY[3] = z
    for k in (1, 2): dY[k] = _v40_ks_d4(lambda y: _v40_ks_Y(y, M, a, A, eps, sig), x, k)
    nab = [[[dY[a_][b][c] - sum(G[d][a_][b]*Y[d][c] + G[d][a_][c]*Y[b][d] for d in range(4)) for c in range(4)] for b in range(4)] for a_ in range(4)]
    xl = [sum(gi[a_][b]*nab[a_][b][c] for a_ in range(4) for b in range(4))/3 for c in range(4)]
    sc = max(abs(nab[a_][b][c]) for a_ in range(4) for b in range(4) for c in range(4)); res = 0.0
    for a_ in range(4):
        for b in range(4):
            for c in range(4):
                res = max(res, abs(nab[a_][b][c] + nab[b][a_][c] - (2*g[a_][b]*xl[c] - g[a_][c]*xl[b] - g[b][c]*xl[a_]))/sc)
    return res, [sum(gi[q][n]*xl[n] for n in range(4)) for q in range(4)]

def _v40_ks_psi2(x, M, a, A):
    """Psi2 = R_abcd k^a m^b mbar^c l^d on the principal tetrad (e0 +- e1)/sqrt2, (e2 + i e3)/sqrt2."""
    G0, g, gi = _v40_ks_christoffel(x, M, a, A)
    dG = [None]*4; z = [[[0.0]*4 for _ in range(4)] for _ in range(4)]; dG[0] = z; dG[3] = z
    for k in (1, 2): dG[k] = _v40_ks_d4(lambda y: _v40_ks_christoffel(y, M, a, A)[0], x, k, h=1e-3)
    Rup = [[[[dG[j][l][k][i] - dG[k][l][j][i] + sum(G0[l][j][q]*G0[q][k][i] - G0[l][k][q]*G0[q][j][i] for q in range(4)) for k in range(4)]
             for j in range(4)] for i in range(4)] for l in range(4)]
    R = [[[[sum(g[l][q]*Rup[q][i][j][k] for q in range(4)) for k in range(4)] for j in range(4)] for i in range(4)] for l in range(4)]
    E = _v40_inv([[v for v in row] for row in _v40_ks_coframe(x, M, a, A)]); vec = lambda B: [E[mu][B] for mu in range(4)]
    e0, e1, e2, e3 = vec(0), vec(1), vec(2), vec(3); r2 = math.sqrt(2)
    kk = [(e0[i] + e1[i])/r2 for i in range(4)]; ll = [(e0[i] - e1[i])/r2 for i in range(4)]
    mm = [(e2[i] + 1j*e3[i])/r2 for i in range(4)]; mb = [v.conjugate() for v in mm]
    return sum(R[a_][b][c][d]*kk[a_]*mm[b]*mb[c]*ll[d] for a_ in range(4) for b in range(4) for c in range(4) for d in range(4))

def v40_0_typeD():
    """The follow-up of 20 November on Entry 493's response: the type D structure, and strip-constrain-restore (R568).  (a) Y = s_g (e0^e1 - i
    e2^e3), s_g = (r - ia cos theta)/(1 - A r cos theta), is a conformal Killing-Yano form for Schwarzschild, Kerr, the C-metric and accelerating
    Kerr; Psi2 conj(s_g)^3/M = -1, and -(1 - i a A) for accelerating Kerr; its divergence xi is d_t for Kerr, d_t - iA d_phi for the C-metric
    and (1 - i a A) d_t - iA d_phi for accelerating Kerr.  (b) The static accelerated family as g = s^2 g_hat, s = 1/(A(x - y)), g_hat = [G(y)
    dt^2 - dy^2/G(y)] + [dx^2/H(x) + H(x) dphi^2]: m = 0 strips to Bertotti-Robinson geometry and restores to flat space; one cubic in both
    sectors restores to vacuum, the stripped Ricci scalar 12 m/s; a common quartic term keeps the trace zero; a quintic fails; an offset
    between the sectors is a cosmological constant (v40.0-6)."""
    print("\n== v40.0-5. The follow-up of 20 November: the type D structure -- a conformal Killing-Yano form, Psi2 and the Killing vector it "
          "gives -- and strip, constrain, restore (R568) ==")
    rng = random.Random(4005)
    cases = (("Schwarzschild", 1.0, 0.0, 0.0), ("Kerr", 1.0, 0.7, 0.0), ("the C-metric", 1.0, 0.0, 0.12), ("accelerating Kerr", 1.0, 0.7, 0.12))
    tri = [(_v40_ks_cky([0.0, 4.0, 1.1, 0.0], 1.0, 0.7, 0.0, e_, s_)[0], e_, s_) for e_ in (1, -1) for s_ in (1, -1)]
    best = min(tri); eps, sig = best[1], best[2]; out = []
    for name, M, a, A in cases:
        rp = M + math.sqrt(M*M - a*a); rmax = (1/A - 0.8) if A > 0 else 7.0
        pts = [[0.0, rng.uniform(rp + 0.4, rmax), rng.uniform(0.5, 2.6), 0.0] for _ in range(4)]; res = []; xis = []; pr = []
        for x in pts:
            r_, xi = _v40_ks_cky(x, M, a, A, eps, sig); res.append(r_); xis.append(xi)
            p2 = _v40_ks_psi2(x, M, a, A); S = _v40_ks_sg(x, M, a, A, eps); pr.append(p2*S.conjugate()**3/M)
        spread = max(max(abs(v[0] - xis[0][0]) for v in xis), max(abs(v[3] - xis[0][3]) for v in xis), max(abs(v[1]) + abs(v[2]) for v in xis))
        wps = max(abs(v - pr[0]) for v in pr); out.append((name, max(res), pr[0], wps, xis[0][0], xis[0][3], spread))
    _v40_wrap(f"(a) The conformal Killing-Yano form [T/V].  On the principal coframe of the accelerating Kerr family, Y = s_g (e0^e1 "
              f"{'-' if sig < 0 else '+'} i e2^e3) with s_g = (r {'-' if eps < 0 else '+'} i a cos theta)/(1 - A r cos theta), the orientation fixed "
              f"on Kerr by the smallest residual of the four choices (" + ", ".join(_v40_r(t_[0]) for t_ in tri) + "); covariant derivatives by "
              f"fourth-order central differences of exact first derivatives (a complex step), so the residuals measure the differences, at four "
              f"points each:")
    for name, res, p2, wps, xt, xp, spread in out:
        print(f"       {name}: CKY residual {_v40_r(res)}; Psi2 conj(s_g)^3/M = {_v40_c(p2, 6)} (spread {_v40_r(wps)}); xi = ({_v40_c(xt, 6)}) d_t + "
              f"({_v40_c(xp, 6)}) d_phi (spread {_v40_r(spread)})")
    _v40_wrap(f"     So Psi2 = -M/conj(s_g)^3 for Kerr and the C-metric, and -M(1 - i a A)/conj(s_g)^3 with spin and acceleration together (a A = "
              f"{_v40_f(0.7*0.12, 6)}); the Killing vector xi is the time translation for Kerr, d_t - iA d_phi for the C-metric and (1 - i a A) d_t - "
              f"iA d_phi for accelerating Kerr.  One complex scalar s_g, whose real and imaginary parts are the radius and Kerr's a cos theta "
              f"divided by the acceleration's conformal factor, carries both deformations.  This is the Plebanski-Demianski family's "
              f"Killing-Yano structure (Kubiznak and Krtous 2007).")
    A0 = 0.12; S2 = _V40JetSpace(2)
    def strip(Gf, Hf, X0, restored, m):
        def fun(V):
            y, x = V[0], V[1]; Gy, Hx = Gf(y), Hf(x); z = _v40_zero(S2, S2.N)
            pre = (A0*A0*(x - y)*(x - y)).recip() if restored else _V40Jet.const(S2, 1.0)
            g = [[z for _ in range(4)] for _ in range(4)]
            g[0][0] = pre*Gy; g[1][1] = -1*pre*Gy.recip(); g[2][2] = pre*Hx.recip(); g[3][3] = pre*Hx
            return g
        G = _v40_jet_metric(fun, S2, X0, [1, 2]); Ric, Rs, Ein, g, gi = _v40_ricci(G, [1, 2])
        return [[sum(gi[i][k]*Ric[k][j] for k in range(4)) for j in range(4)] for i in range(4)], Rs
    m0 = 1.0; u0 = 2*m0*A0
    cubic = lambda xi: (1 - xi*xi)*(1 + u0*xi); flat = lambda xi: (1 - xi*xi)
    pts = [(rng.uniform(-1/u0 + 0.3, -1.3), rng.uniform(-0.8, 0.8)) for _ in range(4)]
    wbr = wfl = wv = wsc = 0.0; samp = None
    for y0, x0 in pts:
        Rm, Rs = strip(flat, flat, (y0, x0), False, 0.0); want = [-1, -1, 1, 1]
        wbr = max(wbr, max(abs(Rm[i][j] - (want[i] if i == j else 0)) for i in range(4) for j in range(4)))
        Rm, Rs = strip(flat, flat, (y0, x0), True, 0.0); wfl = max(wfl, _v40_maxabs(Rm))
        Rm, Rs = strip(cubic, cubic, (y0, x0), True, m0); s = 1/(A0*(x0 - y0)); wv = max(wv, _v40_maxabs(Rm)*s*s)
        Rm, Rs = strip(cubic, cubic, (y0, x0), False, m0); wsc = max(wsc, abs(Rs - 12*m0/s)); samp = (Rs, 12*m0/s)
    tests = (("the same quartic term in both sectors, -0.01 xi^4", lambda xi: cubic(xi) - 0.01*(xi*xi*xi*xi), lambda xi: cubic(xi) - 0.01*(xi*xi*xi*xi)),
             ("the same quintic term, 0.002 xi^5", lambda xi: cubic(xi) + 0.002*(xi*xi*xi*xi*xi), lambda xi: cubic(xi) + 0.002*(xi*xi*xi*xi*xi)),
             ("different functions in the two sectors, H = G + 0.01", cubic, lambda xi: cubic(xi) + 0.01))
    trows = []
    for lab, Gf, Hf in tests:
        y0, x0 = -2.2, 0.3; Rm, Rs = strip(Gf, Hf, (y0, x0), True, m0); s2 = 1/(A0*A0*(x0 - y0)**2)
        trows.append((lab, _v40_maxabs(Rm)*s2, Rs*s2, sum(Rm[i][i] for i in range(4))*s2))
    _v40_wrap(f"(b) Strip, constrain, restore [T/V].  Write the static accelerated family as g = s^2 g_hat with s = 1/(A(x - y)) -- the real part "
              f"of s_g above -- and g_hat = [G(y) dt^2 - dy^2/G(y)] + [dx^2/H(x) + H(x) dphi^2], a product of two two-dimensional spaces (A = 0.12, "
              f"Ricci by jets, four points).  With m = 0 and G = H = 1 - xi^2 the stripped metric's mixed Ricci tensor is diag(-1, -1, +1, +1) "
              f"({_v40_r(wbr)}): Bertotti-Robinson geometry, AdS2 x S^2 of equal radii, without its field; restored, it is flat ({_v40_r(wfl)}).  "
              f"With m = 1, one cubic G = H = (1 - xi^2)(1 + 2mA xi) in both sectors restores to vacuum (|Ricci| s^2 {_v40_r(wv)}) while the "
              f"stripped Ricci scalar is 12m/s ({_v40_r(wsc)}; for example {_v40_f(samp[0], 6)} against {_v40_f(samp[1], 6)}).  At x = 0.3, y = -2.2, "
              f"restored: " + "; ".join(f"{lab}: |Ricci| s^2 = {v1:.2e}, trace s^2 = {_v40_r(v3) if abs(v3) < 1e-8 else f'{v3:.2e}'}" for lab, v1, v2,
                  v3 in trows)
              + ".  So the constraint on the stripped data is a low-degree polynomial shared by the two sectors: a common quartic term keeps the "
              f"trace zero (the charge's term, v40.0-6), a quintic fails, and a constant offset between the sectors is a cosmological constant "
              f"(v40.0-6).  With spin s is complex and the sectors twist.")
    ok = (best[0] < 1e-8 and all(o_[1] < 1e-8 for o_ in out) and all(abs(o_[2] + (1 - 1j*0.7*0.12 if o_[0] == 'accelerating Kerr' else 1)) < 1e-6 for o_ in out)
          and abs(out[2][5] + 0.12j) < 1e-6 and abs(out[3][4] - (1 - 0.084j)) < 1e-6 and wbr < 1e-10 and wfl < 1e-10 and wv < 1e-10 and wsc < 1e-10
          and trows[0][1] > 1e-3 and abs(trows[0][3]) < 1e-10 and trows[1][1] > 1e-3 and abs(trows[1][3]) > 1e-3 and trows[2][1] > 1e-4)
    check(ok, "v40.0-5: Y = s_g (e0^e1 - i e2^e3) is a conformal Killing-Yano form across the accelerating Kerr family, Psi2 conj(s_g)^3/M = -1 "
              "(-(1 - iaA) with both); stripping the conformal factor leaves Bertotti-Robinson at m = 0 and a product constrained to one cubic")

def v40_0_charged():
    """Entry 495: the charged C-metric, the offset as a cosmological constant, and the isotropic member (R569).  (a) With charge the polynomial is
    G = (1 - xi^2)(1 + r+ A xi)(1 + r- A xi), r+- = M +- sqrt(M^2 - q^2 - g^2): Einstein-Maxwell holds with the field the area form of a sector --
    F = q dt^dy electric, F = g dx^dphi magnetic, both for a dyon -- R^a_b = (q^2 + g^2)/s^4 diag(-1, -1, 1, 1); the Gauss charge is the flux of
    *F through any angular sphere, the same at every y.  (b) A constant offset between the two sectors' polynomials is a cosmological constant,
    Lambda = 3 A^2 offset; it moves the far horizon off the outer axis and the corner at infinity closes.  (c) The isotropic member, A -> 0 at
    fixed Lambda: Schwarzschild- and Reissner-Nordstrom-de Sitter, the equal-temperature (lukewarm) case at |Q| = M."""
    print("\n== v40.0-6. Entry 495: the charged C-metric -- the field as a sector's area form, Gauss's charge, the offset as a cosmological "
          "constant, and the isotropic member (R569) ==")
    rng = random.Random(4006); m, A = 1.0, 0.12; rows = []
    for label, qe, qm in (("electric, F = q dt^dy", 0.5, 0.0), ("magnetic, F = g dx^dphi", 0.0, 0.5), ("a dyon, both", 0.3, 0.4)):
        Q2 = qe*qe + qm*qm; rp, rm = m + math.sqrt(m*m - Q2), m - math.sqrt(m*m - Q2)
        Gq = lambda xi, rp=rp, rm=rm: (1 - xi*xi)*(1 + rp*A*xi)*(1 + rm*A*xi); worst = wT = wmx = 0.0; wbad = 1e9
        for _ in range(4):
            y0 = rng.uniform(-1/(rp*A) + 0.3, -1.3); x0 = rng.uniform(-0.8, 0.8)
            Rm, g, gi = _v40_sector_ricci(Gq, Gq, A, y0, x0); pre = 1/(A*A*(x0 - y0)**2); T = Q2/pre**2
            worst = max(worst, max(abs(Rm[i][j] - ((-T if i < 2 else T) if i == j else 0.0)) for i in range(4) for j in range(4))/T)
            for fac in (1.0, 1.2):
                Fm = [[0.0]*4 for _ in range(4)]; Fm[0][1], Fm[1][0], Fm[2][3], Fm[3][2] = fac*qe, -fac*qe, fac*qm, -fac*qm
                Fu = [[sum(gi[a][c]*gi[b][d]*Fm[c][d] for c in range(4) for d in range(4)) for b in range(4)] for a in range(4)]
                F2 = sum(Fm[a][b]*Fu[a][b] for a in range(4) for b in range(4))
                Tl = [[2*(sum(Fm[a][c]*Fm[b][d]*gi[c][d] for c in range(4) for d in range(4)) - 0.25*g[a][b]*F2) for b in range(4)] for a in range(4)]
                Tm = [[sum(gi[a][e]*Tl[e][b] for e in range(4)) for b in range(4)] for a in range(4)]
                dev = max(abs(Rm[i][j] - Tm[i][j]) for i in range(4) for j in range(4))/T
                if fac == 1.0: wT = max(wT, dev)
                else: wbad = min(wbad, dev)
            sg = math.sqrt(abs(g[0][0]*g[1][1]*g[2][2]*g[3][3]))
            wmx = max(wmx, abs(sg*gi[0][0]*gi[1][1]*qe + qe), abs(sg*gi[2][2]*gi[3][3]*qm - qm))
        rows.append((label, worst, wT, wbad, wmx))
    Gq = lambda xi: (1 - xi*xi)*(1 + (m + math.sqrt(m*m - 0.25))*A*xi)*(1 + (m - math.sqrt(m*m - 0.25))*A*xi)
    S1 = _V40JetSpace(1); X1 = _V40Jet.var(S1, 0, -1.0)
    dGm1 = ((1 - X1*X1)*(1 + (m + math.sqrt(m*m - 0.25))*A*X1)*(1 + (m - math.sqrt(m*m - 0.25))*A*X1)).d(0).val()
    dphi = 4*math.pi/abs(dGm1); stars = []
    for y0, x0 in ((-2.0, 0.3), (-5.0, -0.6), (-3.3, 0.8)):
        Rm, g, gi = _v40_sector_ricci(Gq, Gq, A, y0, x0); detg = g[0][0]*g[1][1]*g[2][2]*g[3][3]
        stars.append(math.sqrt(abs(detg))*gi[0][0]*gi[1][1]*0.5)
    wstar = max(abs(v + 0.5) for v in stars); flux = [2*abs(v)*dphi for v in stars]
    _v40_wrap(f"(a) Charge [T/V].  The charged C-metric's polynomial is G = (1 - xi^2)(1 + r+ A xi)(1 + r- A xi), r+- = M +- sqrt(M^2 - q^2 - g^2), "
              f"the same in both sectors (m = 1, A = 0.12).  Einstein-Maxwell holds, R^a_b = (q^2 + g^2)/s^4 diag(-1, -1, +1, +1), with the field "
              f"the area form of a sector of the stripped metric (Ricci by jets at four points each, relative residual): " + "; ".join(
              f"{lab}, {_v40_r(wr)}" for lab, wr, _, _, _ in rows) + ".  The field itself: R^a_b equals the stress tensor 2(F_ac F_b^c - g_ab "
              f"F^2/4) of each F, " + "; ".join(f"{lab.split(',')[0]} {_v40_r(wt_)}" for lab, _, wt_, _, _ in rows) + ", while with F scaled by 1.2 "
              f"the residual is at least {_v40_f(min(r_[3] for r_ in rows), 2)} -- and Maxwell's equations hold, sqrt|g| F^ty = -q and sqrt|g| "
              f"F^xphi = g being constants -- an identity of the metric's form, for any G, H and s, checked as such (" + ", ".join(
              f"{_v40_r(r_[4])}" for r_ in rows) + " at the same points) -- with dF = 0 since F's "
              f"components are constants.  The polynomial sees only q^2 + g^2 (and a^2 + q^2 + g^2 with spin).  The Hodge dual "
              f"of a 2-form is conformally invariant in four dimensions: from the metric, (*F)_x phi = sqrt|g| F^ty = -q at y = -2, -5 and -3.3 "
              f"({_v40_r(wstar)} for q = 0.5), so the flux of *F through an angular sphere y = const is 2q Delta_phi = "
              f"" + ", ".join(_v40_f(f_, 6) for f_ in flux)
              + f", the same at every y, with Delta_phi = {_v40_f(dphi, 6)} regular at the outer axis: Gauss's charge needs one sphere, and a second "
              f"horizon adds only a second closed surface.  "
              f"The accelerating charge radiates: its Bondi news and electromagnetic radiation field are not zero (Ashtekar and Dray 1981).")
    u = 2*m*A; G0 = lambda xi: (1 - xi*xi)*(1 + u*xi)
    def dG0(xi): return _v40_cdG(xi, m, A)
    off = []
    for delta in (0.0, 0.2):
        Gt = lambda xi, d=delta: G0(xi) + d; Lam = 3*A*A*delta; worst = 0.0
        yb = _v40_bisect(lambda y: G0(y) + delta, -1/u - 1e-9, -2.5) if delta > 0 else -1/u
        yc = _v40_bisect(lambda y: G0(y) + delta, -2.0, -1.0 + 1e-12) if delta > 0 else -1.0
        for _ in range(4):
            y0 = rng.uniform(yb + 0.2, yc - 0.15); x0 = rng.uniform(-0.8, 0.8)
            Rm, g, gi = _v40_sector_ricci(Gt, G0, A, y0, x0)
            worst = max(worst, max(abs(Rm[i][j] - (Lam if i == j else 0.0)) for i in range(4) for j in range(4)))
        per = lambda root: 4*math.pi/abs(dG0(root))
        off.append((delta, Lam, worst, yb, yc, per(yb), per(yc), per(-1.0), per(1.0), -1.0 - yc))
    _v40_wrap(f"(b) The offset [T/V].  Add a constant to the time-radial sector's polynomial only, Gt = G + delta: the restored metric has Ricci = "
              f"Lambda g with Lambda = 3 A^2 delta (jets, four points).  " + "; ".join(
              f"delta = {d:g}: Lambda = {_v40_f(L_, 6)} ({_v40_r(w_)}), horizons at y = {_v40_f(yb, 6)} and {_v40_f(yc, 6)}, regular periods hole "
              f"{_v40_f(pb, 6)}, far horizon {_v40_f(pc, 6)}, outer axis {_v40_f(po, 6)}, inner axis {_v40_f(pi_, 6)}, gap between the far horizon and "
              f"the outer axis {_v40_f(gap, 6)}" for d, L_, w_, yb, yc, pb, pc, po, pi_, gap in off) + ".  With an offset the far horizon leaves the "
              f"outer axis, so the corner at infinity is cut off: a positive cosmological constant closes the region.  For Lambda to stay finite as "
              f"A -> 0 the offset must grow as 1/A^2.")
    iso = []
    for Q in (0.0, 0.6, 1.0):
        Mh, l = 1.0, 10.0; f = lambda r: 1 - 2*Mh/r + Q*Q/(r*r) - r*r/(l*l); df = lambda r: 2*Mh/(r*r) - 2*Q*Q/r**3 - 2*r/(l*l)
        rts = _v40_roots(f, 0.02, 2*l, 40000); rb, rc = rts[-2], rts[-1]; iso.append((Q, rb, rc, abs(df(rb))/2, abs(df(rc))/2))
    _v40_wrap(f"(c) The isotropic member [T/V/L].  Letting A -> 0 at fixed Lambda gives Schwarzschild- and Reissner-Nordstrom-de Sitter (the "
              f"limit Podolsky and Griffiths's, quoted, not computed here), f = 1 - "
              f"2M/r + Q^2/r^2 - r^2/L^2; for M = 1 and L = 10: " + "; ".join(
              f"Q = {Q:g}: the hole's horizon r = {_v40_f(rb, 6)}, the equatorial horizon r = {_v40_f(rc, 6)}, surface gravities {_v40_f(kb, 6)} and "
              f"{_v40_f(kc, 6)} (ratio {_v40_f(kc/kb, 6)})" for Q, rb, rc, kb, kc in iso) + ".  At |Q| = M the two temperatures are equal, the "
              f"lukewarm solution (Romans 1992); the two antipodal appearances of one source then carry the same mass and opposite charges "
              f"(v40.0-7), so identifying them needs charge conjugation.")
    ok = (all(wr < 1e-10 and wt_ < 1e-10 and wb_ > 0.1 and wm_ < 1e-12 for lab, wr, wt_, wb_, wm_ in rows) and wstar < 1e-12
        and abs(flux[0] - flux[1]) < 1e-12 and all(o_[2] < 1e-10 for o_ in off)
        and abs(off[1][1] - 0.00864) < 1e-12
          and abs(off[0][9]) < 1e-12 and off[1][9] > 0.1 and abs(iso[2][3] - iso[2][4]) < 1e-9 and abs(iso[0][1] - 2.091488) < 1e-6)
    check(ok, "v40.0-6: the charged C-metric solves Einstein-Maxwell with the field a sector's area form (electric, magnetic, dyon), its Gauss "
              "charge the same through every angular sphere; an offset between the sectors is Lambda = 3 A^2 offset; RN-de Sitter is lukewarm at |Q| = M")

def _v40_lap3(fun, chi0):
    """The Laplacian on the unit 3-sphere of a function of the colatitude, f'' + 2 cot(chi) f', exact by a jet; returns (Lap f, f)."""
    S = _V40JetSpace(2, 1); X = _V40Jet.var(S, 0, chi0); F = fun(X)
    return 2*F.c[S.idx[(2,)]] + 2*math.cos(chi0)/math.sin(chi0)*F.c[S.idx[(1,)]], F.c[0]

def v40_0_lawone():
    """Entry 497: Law I on the leaf, and the mirror acceleration (R570).  (a) Schwarzschild's time-symmetric two-sided slice is the round 3-sphere
    times psi^4, psi = (sqrt(M)/2)[1/sin(chi/2) + 1/cos(chi/2)], which solves (Laplacian - 3/4) psi = 0 away from the two antipodal poles; areal
    radius M(1 + 1/sin chi), the horizon the equator, the mass 4 times the product of the poles' weights; the antipodal quotient is the RP^3 geon.
    (b) Reissner-Nordstrom: psi^2 = psi+ psi-, each factor solving the same equation, areal radius M + c/sin chi; a factor's pole weights in the
    ratio e^b with tanh b = Q/M; the antipodal map exchanges the factors -- charge conjugation.  (c) The closed leaf: Law I's even point source
    F = cos 2chi/sin chi solves (Laplacian + 3) F = 0, while csc chi alone solves (Laplacian - 1) f = 0, the weight-8 operator.  (d) The C-metric
    with charge or spin: at A = c/(a^2 + q^2), c = sqrt(M^2 - a^2 - q^2), the polynomial is symmetric about the midpoint of the hole's and the
    Rindler horizon's roots; it exists only for a^2 + q^2 > 3M^2/4.  With charge alone that symmetry is a reflection of the stripped geometry and
    the two temperatures are equal, kappa+ - kappa_A = (1 - A r+)^2 (c - A q^2)/r+^2 exactly; with the square too, q^2 = 7M^2/8 and
    MA = 2 sqrt(2)/7.  With spin only the polynomial is symmetric: the reflection is not an isometry of the stripped metric.  (e) The lukewarm
    Reissner-Nordstrom-de Sitter hole: its stripped metric is symmetric under 1/r -> 1/M - 1/r, fixed at r = 2M."""
    print("\n== v40.0-7. Entry 497: Law I on the leaf -- the two-sided hole as two antipodal poles, charge as their mismatch, the closed leaf -- "
          "and the mirror acceleration (R570) ==")
    M = 1.0; pts = (0.3, 0.9, 1.5708, 2.2, 2.9)
    psiS = lambda X: (math.sqrt(M)/2)*((X*0.5).sin().recip() + (X*0.5).cos().recip())
    wa = max(abs(_v40_lap3(psiS, c_)[0] - 0.75*_v40_lap3(psiS, c_)[1])/_v40_lap3(psiS, c_)[1] for c_ in pts)
    pv = lambda c_: (math.sqrt(M)/2)*(1/math.sin(c_/2) + 1/math.cos(c_/2))
    wr = max(abs(pv(c_)**2*math.sin(c_) - M*(1 + 1/math.sin(c_))) for c_ in pts)
    w_pole = math.sqrt(M)/2; mass_from_poles = 4*w_pole*w_pole
    _v40_wrap(f"(a) Schwarzschild as two antipodal poles [T/V].  The time-symmetric slice of the two-sided hole is the round unit 3-sphere times "
              f"psi^4 with psi = (sqrt(M)/2)[1/sin(chi/2) + 1/cos(chi/2)], which solves (Laplacian - 3/4) psi = 0 away from the poles (exact by jets, "
              f"{_v40_r(wa)}): a linear equation on the sphere, one pole at each antipode.  Its areal radius psi^2 sin chi is M(1 + 1/sin chi) "
              f"({_v40_r(wr)}), {_v40_f(pv(math.pi/2)**2, 6)} = 2M at the equator, {_v40_f(pv(0.3)**2*math.sin(0.3), 6)} at chi = 0.3 and "
              f"{_v40_f(pv(math.pi - 0.3)**2*math.sin(math.pi - 0.3), 6)} at pi - 0.3: the horizon is the equator, the two poles are the two far "
              f"regions.  The mass is 4 times the product of the poles' weights, here 4 (sqrt(M)/2)^2 = {_v40_f(mass_from_poles, 6)}.  The antipodal "
              f"quotient is the RP^3 geon, Schwarzschild with one exterior.  In this exact picture the poles are the far regions and the hole is the "
              f"equator -- the reverse of v34's mass at a pole, whose closed-leaf form is (c).")
    Q = 0.6; c = math.sqrt(M*M - Q*Q); rho0 = c/2
    psi_pm = lambda X, sg: math.sqrt(rho0/2)*((X*0.5).cos().recip() + ((M + sg*Q)/(2*rho0))*(X*0.5).sin().recip())
    pvm = lambda c_, sg: math.sqrt(rho0/2)*(1/math.cos(c_/2) + ((M + sg*Q)/(2*rho0))/math.sin(c_/2))
    wb1 = max(abs(_v40_lap3(lambda X: psi_pm(X, s_), c_)[0] - 0.75*pvm(c_, s_))/pvm(c_, s_) for c_ in (0.3, 0.9, 2.2) for s_ in (1, -1))
    wb2 = max(abs(pvm(c_, 1)*pvm(c_, -1)*math.sin(c_) - (M + c/math.sin(c_))) for c_ in pts)
    ratio = (M + Q)/(2*rho0); wb3 = max(abs(pvm(math.pi - c_, 1)/pvm(c_, -1) - ratio) for c_ in (0.3, 0.9, 2.2))
    _v40_wrap(f"(b) Charge as the poles' mismatch [T/V].  For Reissner-Nordstrom (M = 1, Q = 0.6) the factor splits, psi^2 = psi+ psi-, each "
              f"factor solving the same equation ({_v40_r(wb1)}), the areal radius psi+ psi- sin chi = M + c/sin chi, c = sqrt(M^2 - Q^2) "
              f"({_v40_r(wb2)}).  One factor's weights at its two poles are in the ratio {_v40_f(ratio, 6)} = e^b with tanh b = Q/M (e^(atanh "
              f"0.6) = {_v40_f(math.exp(math.atanh(Q)), 6)}), the rapidity of the tilt (v40.0-1(c)); the antipodal map turns one factor into the "
              f"other ({_v40_r(wb3)}): mass is the symmetric part of the two appearances, charge the antisymmetric part, and the map is charge "
              f"conjugation.  The quotient exists with a twisted bundle for the field; a rotating geon in four dimensions, if one exists, cannot be "
              f"deformed to zero spin (Louko, Mann and Marolf 2005).")
    fS = lambda X: X.sin().recip(); wc = max(abs(_v40_lap3(fS, c_)[0] - _v40_lap3(fS, c_)[1])/_v40_lap3(fS, c_)[1] for c_ in pts)
    fF = lambda X: (X*2.0).cos()*X.sin().recip()
    wF = max(abs(_v40_lap3(fF, c_)[0] + 3*_v40_lap3(fF, c_)[1])/(abs(_v40_lap3(fF, c_)[0]) + 3*abs(_v40_lap3(fF, c_)[1])) for c_ in pts)
    w4 = max(abs((_v40_lap3(fS, c_)[0] + 3*_v40_lap3(fS, c_)[1])/_v40_lap3(fS, c_)[1] - 4) for c_ in pts)
    wFd = max(abs(math.cos(2*c_)/math.sin(c_) - (1/math.sin(c_) - 2*math.sin(c_))) for c_ in pts)
    _v40_wrap(f"(c) The closed leaf [T/V].  Law I's linearized potential on the leaf obeys (Laplacian + 3) dphi = -2 pi drho (IV.3), and its "
              f"even point source, a mass at a pole with its twin at the antipode, is F = cos 2chi/sin chi = csc chi - 2 sin chi (XXV.2; "
              f"{_v40_r(wFd)}): (Laplacian + 3) F = 0 away from the poles ({_v40_r(wF)}, exact by jets), while (Laplacian + 3) csc chi = "
              f"4 csc chi ({_v40_r(w4)}).  The profile csc chi alone, -M/r with r = l sin chi, solves (Laplacian - 1) f = 0 ({_v40_r(wc)}), "
              f"the weight-8 linearization of v40.0-9(b), not Law I's.  With f = y/sin chi, (Laplacian + 3) f = (y'' + 4y)/sin chi: Law I's "
              f"operator is not screened, its radial solutions oscillating.")
    def mirror(Z, A, a):
        cc = math.sqrt(M*M - Z); rp, rm = M + cc, M - cc
        G = lambda xi: (1 - xi*xi)*(1 + rp*A*xi)*(1 + rm*A*xi)
        S1 = _V40JetSpace(1)
        dG = lambda xi: ((1 - _V40Jet.var(S1, 0, xi)*_V40Jet.var(S1, 0, xi))*(1 + rp*A*_V40Jet.var(S1, 0, xi))*(1 + rm*A*_V40Jet.var(S1, 0, xi))).d(0).val()
        e1, e2, e3, e4 = -1/(rm*A), -1/(rp*A), -1.0, 1.0; rng = random.Random(4007)
        sym = max(abs(G(e2 + e3 - x) - G(x)) for x in [rng.uniform(-6, 2) for _ in range(50)])
        k2 = (e4 - e3)*(e2 - e1)/((e4 - e2)*(e3 - e1)); q2 = Z - a*a
        kp = (rp - rm)*(1 - A*A*rp*rp)/(2*(rp*rp + a*a)); kA = A*(1 - 2*M*A + Z*A*A)/(1 + a*a*A*A)
        kk = [A*abs(dG(e))/2 for e in (e1, e2, e3, e4)]
        return dict(c=cc, rp=rp, rm=rm, A=A, rpA=rp*A, gaps=(e2 - e1, e4 - e3), sym=sym, k2=k2, kp=kp, kA=kA, defi=1 - kk[2]/kk[3], rmid=2/(1/rp + A))
    cases = [("Charge alone, q = 0.95", 0.95**2, 0.0), ("Spin 0.7 with q = 0.6", 0.6**2 + 0.7**2, 0.7)]
    res = []
    for lab, Z, a in cases:
        A = math.sqrt(M*M - Z)/Z; res.append((lab, mirror(Z, A, a)))
    sq = mirror(7/8, 2*math.sqrt(2)/7, 0.0)
    wfac = 0.0; rng = random.Random(4017)
    for _ in range(300):
        Mm = rng.uniform(0.5, 2.0); q = rng.uniform(0.0, 0.99)*Mm; A = rng.uniform(0.01, 0.9)/Mm; cc = math.sqrt(Mm*Mm - q*q); rp = Mm + cc
        kp = cc*(1 - A*A*rp*rp)/(rp*rp); kA = A*(1 - 2*Mm*A + q*q*A*A)
        wfac = max(wfac, abs((kp - kA) - (1 - A*rp)**2*(cc - A*q*q)/(rp*rp)))
    def rstrip(a_, q_, A_, y_, x_, rho=False):
        S_ = _V40JetSpace(2); r0 = -1/(A_*y_); th0 = math.acos(-x_); G_ = _v40_acc_kerr(S_, r0, th0, M, a_, A_, q=q_)
        rj = _V40Jet.var(S_, 0, r0); tj = _V40Jet.var(S_, 1, th0); Om = 1 - A_*rj*tj.cos()
        fac = (Om*Om)*((rj*rj + a_*a_*tj.cos()*tj.cos()) if rho else rj*rj).recip()
        return _v40_ricci([[G_[i][j]*fac for j in range(4)] for i in range(4)], [1, 2])[1]
    mp = []
    for (lab, d), (_, Z, a_) in zip(res, cases):
        mid = (-1/(d['rp']*d['A']) - 1.0)/2; y1, y2 = mid - 0.1163, mid + 0.1163; q_ = math.sqrt(Z - a_*a_)
        mp.append((lab, y1, y2, [rstrip(a_, q_, d['A'], y_, 0.35, rh) for rh in (False, True) for y_ in (y1, y2)]))
    _v40_wrap(f"(d) The mirror acceleration [T/V].  The polynomial G = (1 - xi^2)(1 + r+ A xi)(1 + r- A xi) is symmetric about the midpoint of "
              f"the roots of the hole's horizon and the Rindler horizon when A = c/(a^2 + q^2), c = sqrt(M^2 - a^2 - q^2), which needs charge or "
              f"spin.  " + "; ".join(
              f"{lab}: A = {_v40_f(d['A'], 6)}, r+ A = {_v40_f(d['rpA'], 6)}, root gaps {_v40_f(d['gaps'][0], 6)} and {_v40_f(d['gaps'][1], 6)}, "
              f"symmetry {_v40_r(d['sym'])}, surface gravities {_v40_f(d['kp'], 6)} (hole) and {_v40_f(d['kA'], 6)} (Rindler), deficit/2 pi "
              f"{_v40_f(d['defi'], 6)}, the roots' midpoint at r = {_v40_f(d['rmid'], 6)} between {_v40_f(d['rp'], 6)} and {_v40_f(1/d['A'], 6)}"
              for lab, d in res) + f".  It exists only if r+ A < 1, a^2 + q^2 > 3M^2/4 (at 3/4 exactly, r+ A = {_v40_f(1.5*0.5/0.75, 6)}).  With "
              f"charge alone the temperatures are equal, because kappa+ - kappa_A = (1 - A r+)^2 (c - A q^2)/r+^2 exactly (300 random charged "
              f"holes, {_v40_r(wfac)}; the factorization of the response titled Entry 515), whose root A = c/q^2 is the mirror; with spin they "
              f"differ.  For charge alone the stripped metric is a product and the symmetry of G is a reflection of it, the horizon-swapping "
              f"mirror, with the sphere at the roots' midpoint as its fixed set; with spin the stripped metric is not a product (the sectors "
              f"twist, v40.0-5(b)) and the reflection is not an isometry of it.  Its scalar curvature at a mirror pair, 0.1163 on either side "
              f"of the roots' midpoint in y, x = 0.35 (x = -cos theta), with the factor Omega^2/r^2 and then Omega^2/rho^2, is "
              f"{_v40_f(mp[0][3][0], 6)} and {_v40_f(mp[0][3][1], 6)}, and {_v40_f(mp[0][3][2], 6)} and {_v40_f(mp[0][3][3], 6)}, for charge "
              f"alone (y = {_v40_f(mp[0][1], 4)} and {_v40_f(mp[0][2], 4)}), but {_v40_f(mp[1][3][0], 6)} and {_v40_f(mp[1][3][1], 6)}, and "
              f"{_v40_f(mp[1][3][2], 6)} and {_v40_f(mp[1][3][3], 6)}, with spin (y = {_v40_f(mp[1][1], 4)} and {_v40_f(mp[1][2], 4)})"
              + f".  With spin only the polynomial's roots are symmetric.  Mirror and square together, for charge alone: q^2 = 7M^2/8, "
              f"MA = 2 sqrt(2)/7 = {_v40_f(sq['A'], 6)}, k^2 = {_v40_f(sq['k2'], 6)}, surface gravities {_v40_f(sq['kp'], 6)} and "
              f"{_v40_f(sq['kA'], 6)}.  The mirror is a symmetry of the stripped geometry, not of the restored metric, and the string remains -- "
              f"{_v40_f(res[0][1]['defi'], 6)} of the circle in the first example.")
    l = 10.0; F = lambda u: u*u*(1 - M*u)**2 - 1/(l*l)
    rts = _v40_roots(lambda r: (1 - M/r)**2 - r*r/(l*l), 0.5, 2*l, 40000); rb, rc = rts[-2], rts[-1]
    wm = max(abs(F(1/M - u) - F(u)) for u in (0.05, 0.2, 0.37, 0.6, 0.83))
    _v40_wrap(f"(e) The isotropic counterpart [T/V].  The lukewarm Reissner-Nordstrom-de Sitter hole, |Q| = M, has f = (1 - M/r)^2 - r^2/L^2; its "
              f"stripped metric r^-2 g = -H(u) dt^2 + du^2/H(u) + dOmega^2, u = 1/r, H = u^2 (1 - Mu)^2 - 1/L^2, is symmetric under u -> 1/M - u "
              f"({_v40_r(wm)}), which exchanges the horizons r = {_v40_f(rb, 6)} and {_v40_f(rc, 6)} (1/r_b + 1/r_c = {_v40_f(1/rb + 1/rc, 6)} = 1/M) "
              f"and fixes r = 2M.")
    ok = (wa < 1e-10 and wr < 1e-12 and abs(pv(math.pi/2)**2 - 2) < 1e-12 and wb1 < 1e-10 and wb2 < 1e-12 and abs(ratio - 2) < 1e-12 and wb3 < 1e-12
          and wc < 1e-10 and wF < 1e-10 and w4 < 1e-10 and wFd < 1e-12 and abs(mp[0][3][0] - mp[0][3][1]) < 1e-9
          and abs(mp[0][3][2] - mp[0][3][3]) < 1e-9 and abs(mp[1][3][0] - mp[1][3][1]) > 1e-3 and abs(mp[1][3][2] - mp[1][3][3]) > 1e-3
          and all(abs(d['gaps'][0] - d['gaps'][1]) < 1e-9 and d['sym'] < 1e-12 for lab, d in res) and abs(res[0][1]['kp'] - res[0][1]['kA']) < 1e-12
          and abs(res[1][1]['kp'] - res[1][1]['kA']) > 1e-3 and wfac < 1e-12 and abs(sq['k2'] - 0.5) < 1e-12 and abs(sq['kp'] - sq['kA']) < 1e-12
          and wm < 1e-12 and abs(1/rb + 1/rc - 1/M) < 1e-9)
    check(ok, "v40.0-7: Schwarzschild's slice is the round 3-sphere with two antipodal poles, charge their mismatch e^b, tanh b = Q/M; the mirror "
              "A = c/(a^2 + q^2) makes the polynomial symmetric, the temperatures equal with charge alone; lukewarm RN-dS mirrors 1/r -> 1/M - 1/r")

# ---------------------------------------------------------------------------------------------------- the thin-disk solver on the leaf
# A plain-arithmetic port of the frozen v36 suite's thin-disk solver (pg_v36_numerics.py, _v36_ring_kernel, _v36_graded, _v36_disk_psi,
# _v36_disk_v2, _v36_C_solver): the twin Green function cos 2theta/(4 pi sin theta) averaged over a ring, its two chord terms by complete
# elliptic integrals (here by the arithmetic-geometric mean, where v36 used SciPy), the bounded remainder by the midpoint rule in 64 angles, and
# Gauss-Legendre pieces of 32 nodes graded toward the logarithmic singularity -- the same rules, so that its numbers reproduce v36's.

_V40_GK = 4.300917270e-6                        # G in kpc (km/s)^2 / Msun, as v36's

def _v40_gauss_legendre(n):
    """Nodes and weights of n-point Gauss-Legendre quadrature on [-1, 1], by Newton's iteration on the Legendre polynomial."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi*(i - 0.25)/(n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1): p0, p1 = p1, ((2*k - 1)*x*p1 - (k - 1)*p0)/k
            dp = n*(x*p1 - p0)/(x*x - 1); dx = p1/dp; x -= dx
            if abs(dx) < 1e-16: break
        p0, p1 = 1.0, x
        for k in range(2, n + 1): p0, p1 = p1, ((2*k - 1)*x*p1 - (k - 1)*p0)/k
        dp = n*(x*p1 - p0)/(x*x - 1); xs.append(x); ws.append(2/((1 - x*x)*dp*dp))
    return xs, ws

_V40_GLX, _V40_GLW = _v40_gauss_legendre(32)
_V40_NPHI = 64
_V40_COSPHI = [math.cos((k + 0.5)*(2*math.pi/_V40_NPHI)) for k in range(_V40_NPHI)]

def _v40_ellipkm1(p):
    """K(1 - p), v36's ellipkm1, by the arithmetic-geometric mean."""
    a, b = 1.0, math.sqrt(max(p, 1e-300))
    for _ in range(80):
        a, b = 0.5*(a + b), math.sqrt(a*b)
        if abs(a - b) <= 1e-16*a: break
    return math.pi/(2*a)

def _v40_ring_kernel(x, xp):
    sp, sm, cp, cm = math.sin((x + xp)/2), math.sin((x - xp)/2), math.cos((x + xp)/2), math.cos((x - xp)/2)
    p1 = max((sm/sp)**2, 1e-300); p2 = max((cp/cm)**2, 1e-300)
    sing = (_v40_ellipkm1(p1)/abs(sp) + _v40_ellipkm1(p2)/abs(cm))/(2*math.pi)
    cx, sx, cxp, sxp = math.cos(x), math.sin(x), math.cos(xp), math.sin(xp); acc = 0.0
    for cph in _V40_COSPHI:
        th = math.acos(max(-1.0, min(1.0, cx*cxp + sx*sxp*cph)))
        acc += -1/(8*math.pi) if (th < 1e-6 or th > math.pi - 1e-6) else (math.cos(2*th) - math.cos(th/2) - math.sin(th/2))/(4*math.pi*math.sin(th))
    return sing + acc/_V40_NPHI*2*math.pi

def _v40_graded(a, b, ga, gb, p=3):
    out = []
    for x, w in zip(_V40_GLX, _V40_GLW):
        u = 0.5*(x + 1); ww = 0.5*w
        if ga: out.append((a + (b - a)*u**p, (b - a)*p*u**(p - 1)*ww))
        elif gb: out.append((b - (b - a)*u**p, (b - a)*p*u**(p - 1)*ww))
        else: out.append((a + (b - a)*u, (b - a)*ww))
    return out

def _v40_disk_psi(Sig, x, xmax, brk, nref=12):
    dmin = x*2.0**(-nref)
    pts = [0.0, xmax] + [p for p in brk if 0 < p < xmax and abs(p - x) > dmin]
    pts += [x + s*x*2.0**(-k) for k in range(1, nref + 1) for s in (-1, 1) if 0 < x + s*x*2.0**(-k) < xmax]
    if 0 < x < xmax: pts.append(x)
    e = sorted(set(pts)); tot = 0.0
    for a, b in zip(e[:-1], e[1:]):
        for t, w in _v40_graded(a, b, abs(a - x) < 1e-15*x, abs(b - x) < 1e-15*x):
            tot += w*Sig(t)*math.sin(t)*_v40_ring_kernel(x, t)
    return 2*math.pi*tot

def _v40_disk_norm(Sig, brk, xmax=math.pi/2):
    e = sorted(set([0.0, xmax] + [p for p in brk if 0 < p < xmax])); tot = 0.0
    for a, b in zip(e[:-1], e[1:]):
        for t, w in _v40_graded(a, b, False, False): tot += w*Sig(t)*math.sin(t)
    return 2*math.pi*tot

def _v40_disk_v2(Sig, ell, M, xs, brk, rel_h=0.02, hmax=1e-4, xmax=math.pi/2):
    norm = _v40_disk_norm(Sig, brk, xmax); out = []
    for x in xs:
        h = min(hmax, rel_h*x)
        dps = (_v40_disk_psi(Sig, x + h, xmax, brk) - _v40_disk_psi(Sig, x - h, xmax, brk))/(2*h)
        out.append((_V40_GK*M/ell)*(-2*math.tan(x)*dps/norm))
    return out

def _v40_C_solver(Sig, brk, hs=(0.02, 0.01, 0.005)):
    norm = _v40_disk_norm(Sig, brk); p0 = _v40_disk_psi(Sig, math.pi/2, math.pi/2, brk)/norm
    vals = [4*(_v40_disk_psi(Sig, math.pi/2 - h, math.pi/2, brk)/norm - p0)/h**2 for h in hs]
    r = (hs[-2]/hs[-1])**2
    return (r*vals[-1] - vals[-2])/(r - 1)

def _v40_sin_source(a):
    S = lambda x, a=a: math.exp(-a*math.sin(min(x, math.pi/2)))
    brk = [math.asin(min(1.0, k/a)) for k in (1, 2, 4)] if a > 0 else []
    return S, [b for b in brk if b < math.pi/2 - 1e-9]

def _v40_bessel(n, y, kind):
    """The modified Bessel functions I_n(y) = (1/pi) int_0^pi e^(y cos t) cos(nt) dt and K_n(y) = int_0^inf e^(-y cosh t) cosh(nt) dt."""
    if kind == 'I': return _v40_simpson(lambda t: math.exp(y*math.cos(t))*math.cos(n*t), 0.0, math.pi, 2000)/math.pi
    T = math.acosh(max(1.0, 1 + 60.0/y))
    return _v40_simpson(lambda t: math.exp(-y*math.cosh(t))*math.cosh(n*t), 0.0, T, 4000)

# ---------------------------------------------------------------------------------------------------- the gnomonic image
def _v40_lnratio(x, k):
    """ln of the thin disk's image Sigma_leaf cos^3 chi over the exponential Sigma_0 e^(-R/h), at R = x h, the leaf profile e^(-k sin chi),
    k = ell/h, R = ell tan chi."""
    chi = math.atan(x/k); return k*(math.tan(chi) - math.sin(chi)) + 3*math.log(math.cos(chi))

def _v40_lnimage(x, k):
    chi = math.atan(x/k); return -k*math.sin(chi) + 3*math.log(math.cos(chi))

def _v40_leafmass(k, a=0.0, b=math.pi/2, n=4000):
    return _v40_simpson(lambda c: math.exp(-k*math.sin(c))*math.sin(c), a, b, n)

def v40_0_galaxy():
    """Entries 498-499: the galaxy's image on a leaf (R571).  (a) The leaf profile Sigma_leaf = Sigma_0 exp(-k sin chi), k = ell/h -- Entry 326's
    family (v36.3) -- rendered by the mass-conserving gnomonic map, Sigma_vis = Sigma_leaf cos^3 chi at R = ell tan chi: v36.3's ratios and the
    response's table reproduced; ln(Sigma_vis/Sigma_exp) = x^2 (x - 3)/(2k^2) + ..., x = R/h, the two corrections canceling near three scale
    lengths.  (b) Where the image leaves the exponential, what a fit sees, the leaf needed for a tolerance, and the arena law's leaves.
    (c) The tail against the stellar halo and the circumgalactic medium.  (d) The trade-off: the same source's rotation curve, by v36's solver
    ported to plain arithmetic, as the leaf grows at fixed mass and scale length, against Freeman's flat disk."""
    print("\n== v40.0-8. Entries 498-499: the galaxy's image on a leaf -- how close the sine-exponential source renders to an exponential disk, "
          "where it leaves it, its tail, and the trade-off with the rotation curve (R571) ==")
    ell, h = 16.0, 3.0
    r36 = [math.exp(_v40_lnratio(R/h, ell/h)) for R in (1, 3, 5, 8, 16, 32)]
    tab = [(L_, [math.exp(_v40_lnratio(R/h, L_/h)) for R in (12, 15, 18)]) for L_ in (16.0, 32.0, 48.0, 64.0)]
    fr = []
    for L_ in (16.0, 32.0, 48.0, 64.0):
        k = L_/h; tot = _v40_leafmass(k); fr.append((L_, _v40_leafmass(k, math.atan(15/L_))/tot, _v40_leafmass(k, math.atan(100/L_))/tot))
    k0 = ell/h; tot0 = _v40_leafmass(k0); f36 = _v40_leafmass(k0, math.atan(36/ell))/tot0; feq = _v40_leafmass(k0, math.pi/2 - math.radians(10))/tot0
    lead = [(k, [(x, _v40_lnratio(x, k), x*x*(x - 3)/(2*k*k)) for x in (1, 2, 3, 4, 6)]) for k in (16/3, 16.0)]
    _v40_wrap(f"(a) The image [T/V].  Entry 326's leaf profile e^(-k sin chi), k = ell/h, finite and smooth across the equator, renders with mass "
              f"conserved as Sigma_vis = Sigma_leaf cos^3 chi at R = ell tan chi.  Its ratio to e^(-R/h) on ell = 16, h = 3 kpc at R = 1, 3, 5, 8, 16, "
              f"32 kpc: " + ", ".join(_v40_f(v, 3) for v in r36) + " (v36.3's 0.995, 0.966, 0.938, 0.948, 1.686, 32.532).  The response's table, "
              f"ratios at 12, 15, 18 kpc for h = 3: " + "; ".join(f"ell = {L_:g}: " + ", ".join(_v40_f(v, 2) for v in vs) for L_, vs in tab)
              + ".  Its mass beyond 15 and 100 kpc: " + "; ".join(f"ell = {L_:g}: {a_*100:.2f}%, {b_*100:.6f}%" for L_, a_, b_ in fr)
              + f" (a pure exponential holds {(1 + 15/h)*math.exp(-15/h)*100:.2f}% beyond 15 kpc); on ell = 16 the image holds {f36*100:.1f}% beyond 36 "
              f"kpc and {feq*100:.2f}% within 10 degrees of the equator (v36.3's 5.8% and 2.16%).  The leading law: ln(Sigma_vis/e^(-R/h)) = "
              f"x^2 (x - 3)/(2 k^2) + ..., x = R/h -- " + "; ".join(f"k = {_v40_f(k, 3)}: " + ", ".join(
              f"x = {x}: {v:+.4f} against {w_:+.4f}" for x, v, w_ in rows) for k, rows in lead) + " -- the cos^3 chi and the tan-sine corrections "
              f"cancel near three scale lengths (for a volume density the Jacobian is cos^4 chi and the law x^2 (x - 4)/(2k^2)).")
    MAG = 2.5/math.log(10.0)
    def cross(k, t):
        f = lambda x: MAG*_v40_lnratio(x, k) - t; x0, x1 = 1e-6, 0.01
        while x1 < 400 and f(x1) < 0: x0, x1 = x1, x1 + 0.01
        return _v40_bisect(f, x0, x1)
    def dip(k):
        best = (0.0, 0.0)
        for i in range(1, 6000):
            x = i*0.01; v = MAG*_v40_lnratio(x, k)
            if v < best[0]: best = (v, x)
        return best
    cases = (("ell = 16, h = 3", 16/3), ("ell = 16, h = 2.6", 16/2.6), ("ell = 32, h = 3", 32/3), ("ell = 48, h = 3", 16.0),
             ("ell = 64, h = 3", 64/3), ("k = 40", 40.0), ("k = 64", 64.0))
    crs = []
    for lab, k in cases:
        d = dip(k); xs_ = [cross(k, t) for t in (0.1, 0.3, 1.0)]; crs.append((lab, k, d, xs_, -MAG*_v40_lnimage(xs_[1], k)))
    def fit(k, x1, x2, n=400):
        xs = [x1 + (x2 - x1)*i/(n - 1) for i in range(n)]; ys = [-MAG*_v40_lnimage(x, k) for x in xs]
        mx, my = sum(xs)/n, sum(ys)/n; sxx = sum((x - mx)**2 for x in xs); sxy = sum((x - mx)*(y - my) for x, y in zip(xs, ys))
        sl = sxy/sxx; ic = my - sl*mx; res = [y - (ic + sl*x) for x, y in zip(xs, ys)]
        return MAG/sl, math.sqrt(sum(r*r for r in res)/n), max(abs(r) for r in res)
    fits = [(lab, [fit(k, a_, b_) for a_, b_ in ((1, 5), (1, 8), (0.5, 10))]) for lab, k in cases[:1] + cases[2:5]]
    def kneed(X, tol):
        worst = lambda k: max(abs(MAG*_v40_lnratio(X*i/600.0, k)) for i in range(1, 601)); lo, hi = 0.5, 4000.0
        for _ in range(70):
            mid = math.sqrt(lo*hi)
            if worst(mid) > tol: lo = mid
            else: hi = mid
        return hi
    kn = [(tol, [(X, kneed(X, tol)) for X in (4, 5, 6, 8, 10)]) for tol in (0.1, 0.3)]
    arena = []
    for S0, hl in ((1000, 0.12), (300, 0.23), (100, 0.42), (50, 0.66), (30, 0.98)):
        k = 1/hl; hl_ = lambda x, k=k: 1.0/(math.cos(math.atan(x/k))**3 + 3*math.sin(math.atan(x/k))*math.cos(math.atan(x/k))/k)
        arena.append((S0, k, [math.exp(_v40_lnratio(x, k)) for x in (2, 3, 4, 5)], [hl_(x) for x in (1, 3, 5)]))
    _v40_wrap("(b) Where the image leaves the exponential [V].  Deepest dip below the central exponential; radius, in scale lengths, where the image is "
              "0.1, 0.3 and 1.0 mag above it; the image's surface brightness there below the center: " + "; ".join(
              f"{lab} (k = {_v40_f(k, 3)}): dip {d[0]:+.3f} mag at {_v40_f(d[1], 1)} h, {_v40_f(xs_[0], 2)}, {_v40_f(xs_[1], 2)} and "
              f"{_v40_f(xs_[2], 2)} h, {_v40_f(dep, 2)} mag below the center at the 0.3 mag point" for lab, k, d, xs_, dep in crs) + ".  A straight "
              "line through the image's magnitudes over 1-5, 1-8 and 0.5-10 scale lengths (fitted scale length over h; rms and largest residual, "
              "mag): " + "; ".join(f"{lab}: " + ", ".join(f"{_v40_f(a_, 3)} ({_v40_f(b_, 3)}, {_v40_f(c_, 3)})" for a_, b_, c_ in rs) for lab, rs in fits)
              + ".  The leaf needed, k = ell/h, for the image to stay within a tolerance of the exponential out to X scale lengths: " + "; ".join(
              f"{tol} mag: " + ", ".join(f"X = {X}: k >= {_v40_f(kv, 1)}" for X, kv in rows) for tol, rows in kn) + ".  Under the frozen arena "
              "law h/ell is fixed by the central surface density (Part XII's table): ratios to the exponential at 2, 3, 4, 5 scale lengths, and the "
              "local scale length -1/(d ln Sigma_vis/dR) = h/(cos^3 chi + 3 sin chi cos chi/k) at 1, 3, 5: " + "; ".join(
              f"Sigma_0 = {S0} Msun/pc^2 (k = {_v40_f(k, 2)}): " + ", ".join(_v40_f(v, 2) for v in rs) + "; " + ", ".join(_v40_f(v, 2) for v in ls) + " h"
              for S0, k, rs, ls in arena) + ".")
    M, hh, L0 = 6e10, 3.0, 16.0; kk = L0/hh; I = _v40_leafmass(kk); S0 = M/(2*math.pi*(L0*1e3)**2*I)
    Msun_g, pc_cm, mH = 1.3271244e20/6.67430e-11*1e3, 3.0856776e18, (1.67262192595e-27 + 9.1093837139e-31)*1e3
    col = Msun_g/mH/pc_cm**2
    tails = [(R, S0*math.exp(_v40_lnimage(R/hh, kk)), S0*math.exp(-R/hh)) for R in (8, 16, 25, 36, 50, 100, 250)]
    beyond = [(R, _v40_leafmass(kk, math.atan(R/L0))/I) for R in (36, 100)]
    cgm = 6.5e10/(math.pi*(300.0*1e3)**2)
    Rcgm = _v40_bisect(lambda R: S0*math.exp(_v40_lnimage(R/hh, kk)) - cgm, 16.0, 400.0)
    _v40_wrap(f"(c) The tail [V].  For the benchmark disk, 6e10 Msun, h = 3 kpc, ell = 16 kpc: Sigma_0 = {_v40_f(S0, 0)} Msun/pc^2 (the flat "
              f"exponential's M/(2 pi h^2) is {_v40_f(M/(2*math.pi*(hh*1e3)**2), 0)}; 1 Msun/pc^2 = {col:.3e} hydrogen atoms per cm^2, the solar mass "
              f"the IAU's nominal GM over CODATA 2022's G, the parsec the IAU's, and the atom's mass m_p + m_e from CODATA 2022, its binding "
              f"energy below the printed digits).  The image against the exponential, Msun/pc^2: " + "; ".join(
              f"R = {R} kpc: {sv:.4g} against {se:.4g}" for R, sv, se in tails) + ".  Beyond 36 kpc the image holds " + ", beyond 100 kpc ".join(
              f"{f_*100:.2f}% = {f_*M:.2e} Msun" for R, f_ in beyond) + ".  Against the Milky Way's whole stellar halo, 1.4 +- 0.4 e9 Msun (Deason, "
              f"Belokurov and Sanders 2019), the tail beyond 36 kpc is {_v40_f(beyond[0][1]*M/1.4e9, 1)} times larger and lies in the disk's plane; against "
              f"the cool "
              f"circumgalactic gas of L* galaxies, more than 6.5e10 Msun within the virial radius (Werk et al. 2014), spread over a disk of 300 kpc "
              f"(an assumed radius) -- a mean column of {_v40_f(cgm, 2)} Msun/pc^2 -- the tail falls below that column beyond R = {_v40_f(Rcgm, 0)} kpc.  "
              f"As surface density the tail disappears into the circumgalactic medium; as mass it does not.")
    Rs = [5.0, 8.0, 16.0, 24.0, 36.0, 60.0]; trade = []
    for L_ in (16.0, 24.0, 32.0, 48.0, 64.0, 96.0):
        a = L_/hh; S, brk = _v40_sin_source(a); xs = [math.atan(R/L_) for R in Rs]
        v = [math.sqrt(max(x, 0.0)) for x in _v40_disk_v2(S, L_, M, xs, brk)]
        C = _v40_C_solver(S, brk); trade.append((L_, a, C, math.sqrt(C*_V40_GK*M/L_), v))
    def freeman(R):
        y = R/(2*hh); S0f = M/(2*math.pi*hh*hh)
        return math.sqrt(4*math.pi*_V40_GK*S0f*hh*y*y*(_v40_bessel(0, y, 'I')*_v40_bessel(0, y, 'K') - _v40_bessel(1, y, 'I')*_v40_bessel(1, y, 'K')))
    vf = [freeman(R) for R in Rs]
    _v40_wrap(f"(d) The trade-off [V].  The same source as the whole gravitating disk, 6e10 Msun, h = 3 kpc, on leaves of growing radius, by v36's "
              f"thin-disk solver ported to plain arithmetic (plateau coefficient C, v_inf = sqrt(C G M/ell), and the circular speed in km/s at R = 5, "
              f"8, 16, 24, 36, 60 kpc): " + "; ".join(f"ell = {L_:g} kpc (a = {_v40_f(a, 3)}): C = {_v40_f(C, 4)}, v_inf = {_v40_f(vi, 1)}, v = "
              + ", ".join(_v40_f(x, 1) for x in v) for L_, a, C, vi, v in trade) + "; Freeman's flat exponential disk, the large-leaf limit: "
              + ", ".join(_v40_f(x, 1) for x in vf) + ".  The archive's Milky Way reference is 229 km/s at the Sun, falling 1.7 km/s per kpc "
              f"(Eilers et al. 2019, v36.0-1): the leaves that make the image exponential lose the flat curve.")
    ok = (abs(r36[1] - 0.966) < 6e-4 and abs(r36[5] - 32.532) < 1e-3 and abs(fr[0][1] - 0.1693) < 1e-4 and abs(f36 - 0.058) < 1e-3
          and abs(lead[1][1][0][1] - lead[1][1][0][2]) < 1e-4 and abs(trade[0][2] - 2.6434) < 2e-4 and abs(trade[0][4][0] - 178.7) < 0.2
          and abs(vf[0] - 178.8) < 0.2 and trade[3][4][3] < 140 and 30 < Rcgm < 60 and 0.05 < beyond[0][1] < 0.06)
    check(ok, "v40.0-8: Entry 326's sine-exponential renders as exponential to 0.3 mag out to 4.6 h on ell = 16 kpc and 6.7 h on 48; its tail holds "
              "5.8% beyond 36 kpc; v36's solver ported reproduces C = 2.6434, and the leaves that fix the image lose the flat curve")

def _v40_Rconf(psi, c):
    """The scalar curvature of psi^4 (dchi^2 + sin^2 chi dOmega^2) by the conformal formula psi^-5 (6 psi - 8 Lap psi), unit sphere, by jets."""
    lap, val = _v40_lap3(psi, c); return (6*val - 8*lap)/val**5

def _v40_Rwarp(psi, c):
    """The same curvature from the warped form dr^2 + S(r)^2 dOmega^2, dr = psi^2 dchi, S = psi^2 sin chi: R = -4 S''/S + 2(1 - S'^2)/S^2,
    the r-derivatives by the chain rule on jets in chi (order 3)."""
    Sp = _V40JetSpace(3, 1); X = _V40Jet.var(Sp, 0, c); P = psi(X); P2 = P*P; S = P2*X.sin()
    S1 = S.d(0)*P2.recip(); S2 = S1.d(0)*P2.recip()
    return -4*S2.val()/S.val() + 2*(1 - S1.val()**2)/S.val()**2

def v40_0_conformal():
    """Entries 500-501: the conformal factor that the constraint fixes, and the readouts (R572).  (a) The scalar curvature of psi^4 times the
    round 3-sphere, by the conformal formula and from the warped form: the round leaf, the hemisphere made hyperbolic by psi^2 = 1/cos chi,
    Schwarzschild's psi of v40.0-7 (zero), and a control.  (b) The time-symmetric constraint -8 Lap psi + 6 psi = (16 pi G rho + 2 Lambda) psi^5
    holds with psi = 1 on the uniform leaf; its linearization is (Lap + 3 - n/2) u = -2 pi G d rho for a density of conformal weight n -- n = 0
    the frozen operator of IV.3, n = 6 the plain Laplacian -- checked against the nonlinear equation by shooting, and against the frozen
    F = cos 2chi/sin chi; the kernels at weights 0 and 6.  (c) Its size for a galaxy, psi - 1 ~ 5e-7.  (d) The one conformal rendering of
    constant curvature with the equator at infinity, psi^4 = sec^2 chi: hyperbolic space of the leaf's radius, tanh(r/ell) = sin chi,
    sinh(r/ell) = tan chi, the tilt's law sin p = tanh b again.
    (e) The straight-line-preserving charts of RP^3 are its 15-parameter projective group, X -> gnomonic(AX); after a conformal adjustment
    no chart straightens the geodesics exactly (Beltrami), the failure for an on-shell factor the galaxy's own light bending."""
    print("\n== v40.0-9. Entries 500-501: the conformal factor that the constraint fixes -- the curvature, the linearized operator and its "
          "weight, the size for a galaxy -- the one conformal rendering of constant curvature with the equator at infinity, and the projective "
          "readouts (R572) ==")
    cases = (("psi = 1, the round leaf", lambda X: 1.0 + 0.0*X), ("psi^2 = 1/cos chi, the hemisphere made hyperbolic", lambda X: X.cos().powr(-0.5)),
             ("v40.0-7's psi, Schwarzschild", lambda X: (X*0.5).sin().recip() + (X*0.5).cos().recip()),
             ("psi = 1 + 0.1 cos^2 chi, a control", lambda X: 1.0 + 0.1*X.cos()*X.cos()))
    curv = [(lab, [(_v40_Rconf(f, c), _v40_Rwarp(f, c)) for c in (0.4, 0.9, 1.3)]) for lab, f in cases]
    _v40_wrap("(a) The curvature [T/V].  The scalar curvature of psi^4 x (the round unit 3-sphere), by psi^-5 (6 psi - 8 Lap psi) and from the "
              "warped form dr^2 + S^2 dOmega^2 (exact by jets), at chi = 0.4, 0.9, 1.3: " + "; ".join(
              f"{lab}: " + ", ".join(f"{_v40_f(a_, 6)} / {_v40_f(b_, 6)}" for a_, b_ in vs) for lab, vs in curv) + ".")
    def shoot(p, src, n, N=6000):
        rhs = lambda c, y: (6*y - (4*y**(-n)*(1 + src(c)) + 2)*y**5)/8
        c0 = 1e-6; f0 = rhs(0.0, p); y, v = p + f0*c0*c0/6, f0*c0/3; hs = (math.pi/2 - c0)/N; c = c0
        F = lambda c, y, v: (v, rhs(c, y) - 2*math.cos(c)/math.sin(c)*v)
        for _ in range(N):
            a1, b1 = F(c, y, v); a2, b2 = F(c + hs/2, y + hs/2*a1, v + hs/2*b1); a3, b3 = F(c + hs/2, y + hs/2*a2, v + hs/2*b2)
            a4, b4 = F(c + hs, y + hs*a3, v + hs*b3); y += hs/6*(a1 + 2*a2 + 2*a3 + a4); v += hs/6*(b1 + 2*b2 + 2*b3 + b4); c += hs
        return y, v
    def solve(src, n, guess):
        p0, p1 = guess, guess*(1 + 1e-4) + 1e-9; f0, f1 = shoot(p0, src, n)[1], shoot(p1, src, n)[1]
        for _ in range(40):
            if f1 == f0: break
            p2 = p1 - f1*(p1 - p0)/(f1 - f0); p0, f0, p1 = p1, f1, p2; f1 = shoot(p1, src, n)[1]
            if abs(p1 - p0) < 1e-14: break
        return p1, shoot(p1, src, n)[0]
    k = 16/3; lin = []
    for n in (0, 8):
        for eps in (1e-1, 1e-2):
            src = lambda c, eps=eps: eps*math.exp(-k*math.sin(c))
            if n == 0:
                u0 = 0.5*_v40_simpson(lambda c: math.cos(2*c)*math.sin(c)*src(c), 0, math.pi/2)
                ue = 0.25*_v40_simpson(lambda c: math.sin(2*c)*math.cos(math.pi)*math.sin(c)*src(c), 0, math.pi/2)
            else:
                u0 = 0.5*_v40_simpson(lambda c: math.sin(c)*src(c), 0, math.pi/2); ue = 0.5*_v40_simpson(lambda c: c*math.sin(c)*src(c), 0, math.pi/2)
            p, pe = solve(src, n, 1 + u0); lin.append((n, eps, (p - 1)/u0, (pe - 1)/ue))
    kk = 400.0; srcc = lambda c: math.exp(-kk*math.sin(c))
    def ulin(c):
        g = 0.25*(_v40_simpson(lambda x: math.sin(2*x)*math.cos(2*c)*math.sin(x)*srcc(x), 0, c, 20000)
                  + _v40_simpson(lambda x: math.sin(2*c)*math.cos(2*x)*math.sin(x)*srcc(x), c, math.pi/2, 2000))
        return g/math.sin(c)
    ref = ulin(0.3)/(math.cos(0.6)/math.sin(0.3)); shape = [ulin(c)/(math.cos(2*c)/math.sin(c))/ref for c in (0.3, 0.6, 1.0, 1.4)]
    _v40_wrap(f"(b) The constraint and its weight [T/V].  The time-symmetric Hamiltonian constraint -8 Lap psi + 6 psi = (16 pi G rho + 2 Lambda) "
              f"psi^5 holds with psi = 1 when 16 pi G rho_b + 2 Lambda = 6/ell^2 (the Einstein-static split, 4 and 2 in units of 1/ell^2).  With psi "
              f"= 1 + u and a density prescribed at conformal weight n -- rho = psi^-n rho_n with rho_n given: n = 0 the physical density, n = 6 the "
              f"mass in each leaf cell (the volume element is psi^6 dV), n = 8 York's scaling -- the linear equation is (Lap + 3 - n/2) u = -2 pi G "
              f"d rho_n: n = 0 is the frozen operator of IV.3, Delta + 3, "
              f"and n = 6 the plain Laplacian, Poisson's equation on the 3-sphere in the literal sense, with the constant solutions' double root "
              f"psi^6 - 3 psi^2 + 2 = (psi^2 - 1)^2 (psi^2 + 2) at 1.  Lap + c has a kernel on the 3-sphere exactly when c = k(k + 2), its spectrum "
              f"being -k(k + 2): at n = 0, c = 3, the k = 1 harmonics, odd under the antipodal map, so on the leaf, the even sector, every density "
              f"has its u; at n = 6, c = 0, the constants, so a source needs total d rho_6 zero, and a single mass has no linear solution; at "
              f"n = 8, c = -1, the operator is invertible, and York's scaling gives every density a unique u.  The nonlinear solution, shooting from the "
              f"pole, against the linear one, for the source eps "
              f"e^(-k sin chi), k = 16/3, (psi - 1)/u at the pole and at the equator: " + "; ".join(
              f"n = {n}, eps = {eps:g}: {_v40_f(a_, 5)}, {_v40_f(b_, 5)}" for n, eps, a_, b_ in lin) + ".  For a compact source (k = 400) the n = 0 "
              f"solution's shape is the frozen F = cos 2chi/sin chi, u/F normalized at chi = 0.3, 0.6, 1.0, 1.4: "
              f"" + ", ".join(_v40_f(v, 6) for v in shape) + ".")
    G, cl = 4.30091e-6, 299792.458; Mg, hg = 6e10, 3.0
    _v40_wrap(f"(c) Its size for a galaxy [V].  psi = 1 - Phi/(2c^2): for 6e10 Msun and h = 3 kpc, GM/(h c^2) = {G*Mg/hg/cl**2:.2e} and (206 km/s)^2/c^2 "
              f"= {(206/cl)**2:.2e}, so psi - 1 is of order {G*Mg/hg/cl**2/2:.0e}: the conformal factor that the visible density fixes through the "
              f"constraint cannot reshape a profile, and with conserved matter its area factors cancel in the image (the response's point).")
    rows = []
    for Rl in (0.25, 1.0, 5.0, 20.0):
        c = math.atan(Rl); r = math.asinh(Rl); rows.append((Rl, math.degrees(c), r, math.tanh(r), math.sin(c), math.cosh(r), 1/math.cos(c)))
    ellg, kg = 16.0, 16/3
    hloc = [(r, ellg/(kg/math.cosh(r/ellg)**2 + 2*math.tanh(r/ellg))) for r in (0.5, 3, 8, 16, 32, 80)]
    hyp = _v40_Rconf(lambda X: X.cos().powr(-0.5), 1.1); sec4 = [(c_, _v40_Rconf(lambda X: X.cos().powr(-1.0), c_)) for c_ in (0.3, 0.8, 1.3)]
    _v40_wrap(f"(d) The hyperbolic rendering [T/V].  Of flat, conformal and equator at infinity, a rendering of the leaf can have any two: "
              f"stereographic projection is flat and conformal, with the antipode at infinity; gnomonic projection is flat with the equator at "
              f"infinity and keeps straight lines, not angles; dividing the leaf's metric by cos^2 chi is conformal with the equator at infinity, and "
              f"gives hyperbolic space of the leaf's radius (curvature {_v40_f(hyp, 6)}, -6 for the unit radius) -- the one such rendering of "
              f"constant curvature, the complete conformal metric of constant negative curvature on the hemisphere being unique (Loewner and "
              f"Nirenberg 1974).  Others exist: sec^4 chi times the leaf is conformal with the equator at infinite distance, its curvature " + ", ".join(
              f"{_v40_f(v, 2)} at chi = {c_:g}" for c_, v in sec4) + ".  The hyperbolic rendering's proper radius is r = ell "
              f"asinh(tan chi), so tanh(r/ell) = sin chi, sinh(r/ell) = tan chi and cosh(r/ell) = sec chi: " + "; ".join(
              f"R/ell = {Rl:g} ({_v40_f(dg, 2)} degrees): r/ell = {_v40_f(r, 4)}, tanh {_v40_f(th_, 6)} = sin {_v40_f(sn, 6)}, cosh {_v40_f(ch, 6)} = sec "
              f"{_v40_f(sc, 6)}" for Rl, dg, r, th_, sn, ch, sc in rows) + f".  The tilt's law again: asinh(tan 89 degrees) = "
              f"{_v40_f(math.asinh(math.tan(math.radians(89))), 4)} = atanh(sin 89 degrees) = {_v40_f(math.atanh(math.sin(math.radians(89))), 4)}, the "
              f"equator in the right angle's place.  The disk's image there, mass conserved, is Sigma_0 e^(-k tanh(r/ell)) sech^2(r/ell): a "
              f"hyperbolic secant, exponential only asymptotically, its local scale length in proper radius (ell = 16, h = 3 kpc) " + ", ".join(
              f"{_v40_f(v, 2)} kpc at r = {r:g}" for r, v in hloc) + f", tending to ell/2 = {_v40_f(ellg/2, 0)} kpc.  Read as positions this "
              f"space is curved at 16 kpc, which positions do not show; read as velocities, with sin chi = v/c, it is the velocity hyperboloid the "
              f"frozen core already has.  Neither reading is derived.")
    rng = random.Random(4009); worst = wanti = 0.0
    for _ in range(6):
        Am = [[rng.gauss(0, 1) for _ in range(4)] for _ in range(4)]
        def chart(X):
            Y = [sum(Am[i][j]*X[j] for j in range(4)) for i in range(4)]; return [Y[1]/Y[0], Y[2]/Y[0], Y[3]/Y[0]]
        for _ in range(6):
            a_ = _v40_rand_unit(rng); b_ = _v40_rand_tangent(rng, a_); pts = []
            for t in (0.11, 0.37, 0.52, 0.83, 1.07):
                X = [math.cos(t)*x + math.sin(t)*y for x, y in zip(a_, b_)]; P = chart(X); pts.append(P)
                Q = chart([-x for x in X]); wanti = max(wanti, max(abs(p - q) for p, q in zip(P, Q)))
            d = [q - p for p, q in zip(pts[0], pts[-1])]; nd = _v40_norm(d)
            for P in pts[1:-1]:
                w_ = [p - p0 for p, p0 in zip(P, pts[0])]; worst = max(worst, _v40_norm(_v40_cross(w_, d))/nd/nd)
    alpha = 2*math.pi*(206/cl)**2
    _v40_wrap(f"(e) The readouts [T/V].  Every chart X -> gnomonic(A X), A an invertible 4 x 4 matrix, sends great circles to straight lines "
              f"(6 random A, 6 random great circles each, {_v40_r(worst)}) and gives X and -X the same point ({_v40_r(wanti)}): RP^3's projective group, 15 "
              f"parameters, of which the rotations are 6, the stretches and shears 6, and the choice of the great sphere at infinity 3.  The only "
              f"conformal maps of RP^3 are its rotations (v36.3), so a conformal step happens on the leaf, before the readout.  After a conformal "
              f"adjustment no chart straightens the geodesics exactly unless the curvature stays constant (Beltrami); for the on-shell factor of "
              f"(c) the failure is the galaxy's own light bending, 2 pi v^2/c^2 = {alpha:.2e} rad = {_v40_f(math.degrees(alpha)*3600, 2)} arcsec for "
              f"a flat 206 km/s curve.  A stretch in the readout is a choice of chart, not a flattening.")
    ok = (all(abs(a_ - b_) < 1e-9 for lab, vs in curv for a_, b_ in vs) and all(abs(a_ - 6) < 1e-12 for a_, b_ in curv[0][1])
          and all(abs(a_ + 6) < 1e-9 for a_, b_ in curv[1][1]) and all(abs(a_) < 1e-9 for a_, b_ in curv[2][1])
          and all(abs(a_ - 1) < 5e-3 and abs(b_ - 1) < 5e-3 for n, eps, a_, b_ in lin) and all(abs(v - 1) < 1e-4 for v in shape)
          and abs(hyp + 6) < 1e-9 and max(v for _, v in sec4) < -1 and max(v for _, v in sec4) - min(v for _, v in sec4) > 1 and worst < 1e-12
          and wanti < 1e-12 and abs(hloc[-1][1] - 8) < 0.1)
    check(ok, "v40.0-9: the constraint's linearization is (Lap + 3 - n/2) u = -2 pi G d rho, the frozen Delta + 3 at weight 0; its factor for a "
              "galaxy is 5e-7; sec^2 chi times the leaf is hyperbolic space with tanh(r/ell) = sin chi; RP^3's projective charts are the readouts")

def _v40_XL(x): return [-x[1], x[0], -x[3], x[2]]        # (z1, z2) -> e^(it)(z1, z2): d/dxi1 + d/dxi2
def _v40_XR(x): return [-x[1], x[0], x[3], -x[2]]        # (z1, z2) -> (e^(it) z1, e^(-it) z2): d/dxi1 - d/dxi2
def _v40_Km(x): return _v40_add(_v40_XL(x), _v40_XR(x), -1.0)
def _v40_Kp(x): return _v40_add(_v40_XL(x), _v40_XR(x))
def _v40_geo(x, w, t): return _v40_add(_v40_scale(x, math.cos(t)), _v40_scale(w, math.sin(t)))
def _v40_geo_dot(x, w, t): return _v40_add(_v40_scale(x, -math.sin(t)), _v40_scale(w, math.cos(t)))

def _v40_tangent_basis(x):
    b = []
    for e in ([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]):
        v = _v40_add(e, x, -_v40_dot(e, x))
        for u in b: v = _v40_add(v, u, -_v40_dot(v, u))
        if _v40_norm(v) > 1e-6: b.append(_v40_unit(v))
        if len(b) == 3: break
    return b

def _v40_theta_dtheta(field, x):
    """(theta ^ d theta)(e1, e2, e3) for theta = <K, .>, K(x) = M x linear and skew: d theta(a, b) = 2 <K(a), b> on tangent vectors."""
    e = _v40_tangent_basis(x); th = [_v40_dot(field(x), v) for v in e]; d = lambda a, b: 2*_v40_dot(field(a), b)
    return th[0]*d(e[1], e[2]) - th[1]*d(e[0], e[2]) + th[2]*d(e[0], e[1])

def v40_0_lanes():
    """Entries 502-506: the two Hopf fields as the two structures, and the flashlight (R573).  (a) On the round leaf two rays from one point meet
    again only at the antipode.  (b) The left and right Hopf fields X_L, X_R: unit, odd under x -> -x (so they descend to RP^3), <X_L, X_R> =
    cos 2 eta; each alone is a contact structure; their difference and their sum are integrable, the difference's surfaces the great 2-spheres
    through a hinge circle, where X_L = X_R, and the relative transport vanishes on them.  (c) Along a light ray p1 = <v, X_L + X_R>/2 and
    p2 = <v, X_L - X_R>/2 are conserved; the two transports around the circuit are 2 pi (p1 +- p2), their difference the relative phase.
    (d) The flashlight: from a point at angular distance eta0 from the hinge a ray at angle a from the admissible sphere's normal has p2 =
    cos a sin eta0; only rays in the admissible sphere reach the hinge.  (e) The lanes as rays carried by the two fields at a rate w: apart by
    2 sin eta |sin wt|.  (f) Seen from a galaxy on the dual circle the admissible spheres are the planes Z = const of gnomonic space, X_L + X_R
    the rotation about the Z axis; a normal ray from radius R returns with the lanes 1 - cos chi of a turn apart, and the relative phase to a
    point a height z above the plane is 2 atan(z/ell) near the center.  (g) The response's ring: E_min = 4 sin^2(Phi/6) on three sites, 4
    sin^2(Phi/2N) on N, (Phi/L)^2 in the continuum.  (h) An isotropic reservoir with the disk's radial profile, seen only in its plane, would
    weigh 4h/t times the disk."""
    print("\n== v40.0-10. Entries 502-506: the two Hopf fields as the two structures -- their difference integrable, the admissible planes, the "
          "conserved relative phase, the flashlight, the lanes as carried rays, the response's ring, and the reservoir's mass (R573) ==")
    rng = random.Random(4010); worst = 0.0
    for _ in range(200):
        x = _v40_rand_unit(rng); w1, w2 = _v40_rand_tangent(rng, x), _v40_rand_tangent(rng, x)
        for t in (0.3, 1.1, 2.0, 2.9):
            d = _v40_norm(_v40_add(_v40_geo(x, w1, t), _v40_geo(x, w2, t), -1.0))
            worst = max(worst, abs(d - abs(math.sin(t))*_v40_norm(_v40_add(w1, w2, -1.0))))
    _v40_wrap(f"(a) The round leaf alone [T/V].  Two rays leaving one point in directions w1, w2 are |sin t| |w1 - w2| apart after an arc t (200 "
              f"random pairs, {_v40_r(worst)}): they meet again only at t = pi, the antipode -- on RP^3 the starting point itself -- whatever the "
              f"directions.  With one round geometry for both lanes there is no closing elsewhere and nothing that depends on direction; on a 16 kpc "
              f"leaf pi ell = {_v40_f(math.pi*16, 1)} kpc.")
    e = [0.0]*4
    for _ in range(200):
        x = _v40_rand_unit(rng); eta = math.atan2(math.hypot(x[2], x[3]), math.hypot(x[0], x[1])); mx = [-v for v in x]
        e[0] = max(e[0], abs(_v40_norm(_v40_XL(x)) - 1), abs(_v40_norm(_v40_XR(x)) - 1), abs(_v40_dot(_v40_XL(x), x)), abs(_v40_dot(_v40_XR(x), x)))
        e[1] = max(e[1], abs(_v40_dot(_v40_XL(x), _v40_XR(x)) - math.cos(2*eta)))
        e[2] = max(e[2], _v40_norm(_v40_add(_v40_XL(mx), _v40_scale(_v40_XL(x), -1.0), -1.0)), _v40_norm(_v40_add(_v40_XR(mx), _v40_scale(_v40_XR(x), -1.0),
            -1.0)))
        e[3] = max(e[3], abs(_v40_norm(_v40_Km(x)) - 2*math.sin(eta)), abs(_v40_norm(_v40_Kp(x)) - 2*math.cos(eta)))
    cL = [abs(_v40_theta_dtheta(_v40_XL, _v40_rand_unit(rng))) for _ in range(5)]
    cM = max(abs(_v40_theta_dtheta(_v40_Km, _v40_rand_unit(rng))) for _ in range(5))
    cP = max(abs(_v40_theta_dtheta(_v40_Kp, _v40_rand_unit(rng))) for _ in range(5))
    wpl = wco = 0.0
    for _ in range(100):
        x = _v40_rand_unit(rng); k_ = _v40_Km(x)
        if _v40_norm(k_) < 0.2: continue
        m_ = _v40_unit(k_); w = _v40_rand_tangent(rng, x); w = _v40_unit(_v40_add(w, m_, -_v40_dot(w, m_)))
        for t in (0.4, 1.3, 2.2, 3.0, 4.4):
            y = _v40_geo(x, w, t); wpl = max(wpl, abs(_v40_dot(y, m_))); wco = max(wco, abs(_v40_dot(_v40_geo_dot(x, w, t), _v40_Km(y))))
    _v40_wrap(f"(b) The two fields [T/V].  The leaf's left and right Hopf fields, X_L(z1, z2) = (iz1, iz2) and X_R = (iz1, -iz2) -- the archive's "
              f"two so(4) sectors (XXXIII.41) -- are unit and tangent ({_v40_r(e[0])}), odd under x -> -x as tangent vectors must be, so they "
              f"descend to RP^3 ({_v40_r(e[2])}), with <X_L, X_R> = cos 2 eta ({_v40_r(e[1])}), |X_L - X_R| = 2 sin eta and |X_L + X_R| = 2 cos eta "
              f"({_v40_r(e[3])}): they agree on the great circle eta = 0, the hinge, and are opposite on the dual circle eta = pi/2.  theta ^ d theta "
              f"on a tangent frame: X_L alone " + ", ".join(_v40_f(v, 6) for v in cL) + f" at five points (a contact structure, XXXIII.41's result); "
              f"X_L - X_R {_v40_r(cM)}; X_L + X_R {_v40_r(cP)}.  So neither field has a surface everywhere perpendicular to it, and their difference "
              f"does: a ray that starts perpendicular to X_L - X_R stays so ({_v40_r(wco)}) and stays on the great 2-sphere through its starting "
              f"point and the hinge ({_v40_r(wpl)}), on which the relative transport vanishes.  These are the admissible spheres.")
    def loops(x, w, n=2000):
        sL = sR = 0.0
        for i in range(n):
            t = 2*math.pi*(i + 0.5)/n; y = _v40_geo(x, w, t); v = _v40_geo_dot(x, w, t); sL += _v40_dot(_v40_XL(y), v); sR += _v40_dot(_v40_XR(y), v)
        return sL*2*math.pi/n, sR*2*math.pi/n
    wl = 0.0
    for _ in range(30):
        x = _v40_rand_unit(rng); w = _v40_rand_tangent(rng, x); p1, p2 = _v40_dot(w, _v40_Kp(x))/2, _v40_dot(w, _v40_Km(x))/2
        iL, iR = loops(x, w); wl = max(wl, abs(iL - 2*math.pi*(p1 + p2)), abs(iR - 2*math.pi*(p1 - p2)))
    fl = []
    for eta0 in (10, 30, 60, 90):
        sn = math.sin(math.radians(eta0)); fl.append((eta0, [(a, math.cos(math.radians(a))*sn) for a in (0, 30, 60, 85, 90)], sn/2))
    x0 = [math.cos(0.7), 0.0, math.sin(0.7), 0.0]; nrm = _v40_unit(_v40_Km(x0)); rad = [-math.sin(0.7), 0.0, math.cos(0.7), 0.0]; reach = []
    for a in (90, 60, 30, 0):
        w = _v40_add(_v40_scale(nrm, math.cos(math.radians(a))), _v40_scale(rad, math.sin(math.radians(a)))); p2 = _v40_dot(w, _v40_Km(x0))/2
        mn = min(math.hypot(*_v40_geo(x0, w, math.pi*i/20000)[2:]) for i in range(20001)); reach.append((a, p2, math.degrees(math.asin(min(1.0, mn)))))
    _v40_wrap(f"(c) The relative phase [T/V].  Along a light ray, a great circle, p1 = <v, X_L + X_R>/2 and p2 = <v, X_L - X_R>/2 are conserved, and "
              f"the two transports around the whole circle are 2 pi (p1 + p2) and 2 pi (p1 - p2) (30 random rays, {_v40_r(wl)}): their difference, 4 "
              f"pi p2, is the relative phase, 2 pi p2 on RP^3, whose circuit is half as long; zero for rays in an admissible sphere.  (d) The "
              f"flashlight [T/V].  From a point at angular distance eta0 from the hinge, a ray at angle a from the admissible sphere's normal has p2 = "
              f"cos a sin eta0 -- relative phase per RP^3 circuit, in turns: " + "; ".join(f"eta0 = {e0} degrees: " + ", ".join(
              f"a = {a}: {_v40_f(v, 3)}" for a, v in vs) + f" (the two lanes on the normal ray +{_v40_f(hv, 3)} and -{_v40_f(hv, 3)})" for e0, vs, hv in fl)
              + ".  Rays launched toward the hinge from eta0 = 0.7 rad reach it only in the admissible sphere (closest approach, degrees: " + ", ".join(
              f"a = {a}: p2 = {_v40_f(p, 3)}, {_v40_f(m_, 2)}" for a, p, m_ in reach) + "), the others' closest approach asin|p2|.")
    om = 0.37; ws = 0.0
    for _ in range(40):
        x = _v40_rand_unit(rng); w = _v40_rand_tangent(rng, x)
        for t in (0.5, 1.7, 3.3, 6.1):
            y = _v40_geo(x, w, t)
            zL = (complex(y[0], y[1])*cmath.exp(1j*om*t), complex(y[2], y[3])*cmath.exp(1j*om*t))
            zR = (complex(y[0], y[1])*cmath.exp(1j*om*t), complex(y[2], y[3])*cmath.exp(-1j*om*t))
            sep = math.sqrt(abs(zL[0] - zR[0])**2 + abs(zL[1] - zR[1])**2); ws = max(ws, abs(sep - 2*math.hypot(y[2], y[3])*abs(math.sin(om*t))))
    gn = lambda y: [y[0]/y[2], y[1]/y[2], y[3]/y[2]]; wz = wr = 0.0
    for _ in range(100):
        x = _v40_rand_unit(rng)
        if abs(x[2]) < 0.2 or math.hypot(x[2], x[3]) < 0.2: continue
        m_ = _v40_unit(_v40_Km(x)); w = _v40_rand_tangent(rng, x); w = _v40_unit(_v40_add(w, m_, -_v40_dot(w, m_))); Z0 = gn(x)[2]
        for t in (0.05, 0.15, 0.3):
            y = _v40_geo(x, w, t)
            if abs(y[2]) > 0.1: wz = max(wz, abs(gn(y)[2] - Z0))
        g0 = gn(x); z1 = complex(x[0], x[1])*cmath.exp(2j*0.23); g1 = gn([z1.real, z1.imag, x[2], x[3]])
        wr = max(wr, abs(g1[2] - g0[2]), abs(math.hypot(g1[0], g1[1]) - math.hypot(g0[0], g0[1])))
    ell = 16.0; ret = [(R, 1 - 1/math.sqrt(1 + (R/ell)**2)) for R in (0.5, 3, 8, 16, 32)]
    def rel_phase(R, z, n=4000):
        a_ = _v40_unit([R/ell, 0.0, 1.0, 0.0]); b_ = _v40_unit([R/ell, 0.0, 1.0, z/ell]); ang = math.acos(max(-1.0, min(1.0, _v40_dot(a_, b_))))
        w = _v40_unit(_v40_add(b_, a_, -_v40_dot(a_, b_))); tot = 0.0
        for i in range(n):
            t = ang*(i + 0.5)/n; tot += _v40_dot(_v40_Km(_v40_geo(a_, w, t)), _v40_geo_dot(a_, w, t))
        return tot*ang/n
    rp_ = [(z, [rel_phase(R, z) for R in (0, 8, 16)], 2*math.atan(z/ell)) for z in (0.3, 1.0, 8.0)]
    _v40_wrap(f"(e) The lanes as carried rays [T/V; premise].  Take each lane to be the ray carried along by its field at a rate w: they are 2 sin "
              f"eta(t) |sin wt| apart ({_v40_r(ws)}), so they meet where the ray crosses the hinge, or everywhere after one whole relative turn, t = "
              f"pi/w; with unequal rates w1 and w2 the relative motion turns two planes, by (w1 - w2)t and (w1 + w2)t, and has no fixed circle at "
              f"all unless one angle is a whole turn (an algebraic fact of SO(4), not computed) -- the response's torus, whose dense "
              f"winding makes never meeting exactly different from never meeting observably.  (f) Seen from a galaxy on the dual circle, gnomonic coordinates "
              f"(X, Y, Z) = ell (x1, x2, x4)/x3 [T/V]: the admissible spheres are the planes Z = const ({_v40_r(wz)}) and X_L + X_R is the rotation "
              f"about the Z axis ({_v40_r(wr)}), so X_L and X_R are the two screw motions about the axis, of opposite hand.  A ray sent along the "
              f"normal from radius R in the central plane returns, on RP^3, with the lanes 1 - cos chi of a turn apart (tan chi = R/ell; ell = 16 "
              f"kpc): " + ", ".join(f"{_v40_f(v, 4)} at R = {R:g} kpc" for R, v in ret) + ".  The relative phase to the point a height z above, "
              f"radians, at R = 0, 8, 16 kpc: " + "; ".join(f"z = {z:g} kpc: " + ", ".join(_v40_f(v, 4) for v in vs) + f" (2 atan(z/ell) = "
              f"{_v40_f(at, 4)})" for z, vs, at in rp_) + f": 2 atan(z/ell) at the center, about 2z/ell for z small against ell "
              f"({_v40_f([at for z, vs, at in rp_ if z == 8.0][0], 4)} rad, not one radian, at z = ell/2), falling outward as cos^2 chi for z "
              f"small; two "
              f"points of one plane Z = const have none.")
    def emin(N, Phi, sweeps=4000):
        C = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(N)]
        def H(C):
            out = []
            for j in range(N):
                up = C[(j + 1) % N]*(cmath.exp(-1j*Phi) if j == N - 1 else 1); dn = C[(j - 1) % N]*(cmath.exp(1j*Phi) if j == 0 else 1)
                out.append(2*C[j] - up - dn)
            return out
        for _ in range(sweeps):
            h_ = H(C); C = [4*c - x for c, x in zip(C, h_)]; nn = math.sqrt(sum(abs(c)**2 for c in C)); C = [c/nn for c in C]
        h_ = H(C); return sum((c.conjugate()*x).real for c, x in zip(C, h_))
    ring3 = [(P, emin(3, P), 4*math.sin(P/6)**2) for P in (0.0, 0.5, 1.5, 2.5, math.pi)]
    ringN = [(N, (N/(2*math.pi))**2*4*math.sin(2.0/(2*N))**2) for N in (3, 12, 48)]
    hd, hz, Mv, Gk = 2.6, 0.3, 6e10, 4.30091e-6; t_ = 2*hz; ratio = 4*hd/t_; Mg = ratio*Mv; xx = 8.0/hd; Min = Mg*(1 - math.exp(-xx)*(1 + xx + xx*xx/2))
    _v40_wrap(f"(g) The response's ring [T/V].  E = kappa sum |C_j - U_ij C_i|^2 on a ring with total phase Phi: on three sites its least value, by "
              f"power iteration, against 4 sin^2(Phi/6): " + ", ".join(f"Phi = {_v40_f(P, 2)}: {_v40_f(a_, 6)} / {_v40_f(b_, 6)}" for P, a_, b_ in ring3)
              + f"; on N sites 4 sin^2(Phi/2N), with spacing L/N and kappa = (N/L)^2 tending to (Phi/L)^2: " + ", ".join(
              f"N = {N}: {_v40_f(v, 6)}" for N, v in ringN) + f" at Phi = 2, L = 2 pi (limit {_v40_f((2.0/(2*math.pi))**2, 6)}).  On a light ray the "
              f"relative connection is the constant 2 p2.  Around the closed ray on the 3-sphere, length 2 pi and phase 4 pi p2, the least "
              f"alignment energy is the squared distance of 2 p2 from an integer; around the leaf's circuit, length pi and phase 2 pi p2, it is four "
              f"times the squared distance of p2 from an integer.  The two differ at half-integer p2 -- the normal ray at eta0 = 30 degrees, p2 = "
              f"0.500: {_v40_f(min(abs(1.0 - k_) for k_ in range(3))**2, 0)} on the 3-sphere, {_v40_f(4*min(abs(0.5 - k_) for k_ in range(3))**2, 0)} "
              f"on the leaf -- and agree at zero in the admissible spheres, p2 = 0.  (h) The reservoir [V].  If the disk we see were the admissible slice "
              f"of an isotropic "
              f"distribution with the same radial profile, rho = rho_0 e^(-r/h), the whole would weigh 4h/t times the slice of full effective "
              f"thickness t: {_v40_f(ratio, 1)} for h = 2.6 kpc and t = 2 x 0.3 kpc, the thin disk's scale length and height (Bland-Hawthorn and "
              f"Gerhard 2016), and {_v40_f(4*hd/hz, 1)} if t were the scale height alone -- "
              f"{Mg:.2e} Msun for 6e10 Msun seen, {Min:.2e} of it inside 8 kpc, a Newtonian circular speed of {_v40_f(math.sqrt(Gk*Min/8.0), 0)} km/s "
              f"there against the archive's 229; 229 km/s allows {229**2*8/Gk:.2e} Msun inside 8 kpc, {_v40_f(229**2*8/Gk/Min, 2)} of it.  Unseen "
              f"matter must be far lighter or far more spread out than the disk.")
    ok = (worst < 1e-12 and max(e) < 1e-12 and all(abs(v - 2) < 1e-12 for v in cL) and cM < 1e-12 and cP < 1e-12 and wco < 1e-12 and wpl < 1e-12
          and wl < 1e-9 and reach[0][2] < 0.1 and all(r_[2] > 10 for r_ in reach[1:]) and ws < 1e-12 and wz < 1e-12 and wr < 1e-12
          and all(abs(vs[0] - at) < 1e-6 for z, vs, at in rp_) and all(abs(a_ - b_) < 1e-9 for P, a_, b_ in ring3) and abs(ratio - 17.333333) < 1e-5)
    check(ok, "v40.0-10: the difference of the left and right Hopf fields is integrable, its surfaces the great spheres through a hinge; along a "
              "ray the relative phase 4 pi p2 is conserved, zero in those spheres; the normal ray returns 1 - cos chi of a turn apart")

def _v40_ray(rng):
    q = _v40_rand_unit(rng); w = _v40_rand_tangent(rng, q); return q, w

def _v40_labels(q, w):
    """A great circle through q with unit tangent w: u = q^-1 w and v = w q^-1, both unit imaginary, its left and right labels."""
    return _v40_qmul(_v40_qconj(q), w)[1:], _v40_qmul(w, _v40_qconj(q))[1:]

def _v40_principal(r1, r2):
    """The two principal angles between the planes of two great circles; the first is their closest approach on the 3-sphere."""
    (q1, w1), (q2, w2) = r1, r2
    Mx = [[_v40_dot(q1, q2), _v40_dot(q1, w2)], [_v40_dot(w1, q2), _v40_dot(w1, w2)]]
    a = Mx[0][0]**2 + Mx[1][0]**2; b = Mx[0][0]*Mx[0][1] + Mx[1][0]*Mx[1][1]; d = Mx[0][1]**2 + Mx[1][1]**2
    tr, det = a + d, a*d - b*b; disc = math.sqrt(max(0.0, tr*tr/4 - det))
    cl = lambda x: max(-1.0, min(1.0, x))
    return math.acos(cl(math.sqrt(max(0.0, tr/2 + disc)))), math.acos(cl(math.sqrt(max(0.0, tr/2 - disc))))

def _v40_gh(S, r0, th0, Vf, Af):
    """g = V (dr^2 + r^2 dtheta^2 + r^2 sin^2 theta dphi^2) + (dpsi + A dphi)^2/V in (r, theta, phi, psi), V and A jets in (r, theta)."""
    r = _V40Jet.var(S, 0, r0); th = _V40Jet.var(S, 1, th0); V = Vf(r, th); A = Af(r, th); Vi = V.recip(); s2 = th.sin()*th.sin()
    z = _v40_zero(S, S.N); g = [[z for _ in range(4)] for _ in range(4)]
    g[0][0] = V; g[1][1] = V*r*r; g[2][2] = V*r*r*s2 + A*A*Vi; g[2][3] = g[3][2] = A*Vi; g[3][3] = Vi
    return g

def _v40_mp5(S, r0, th0, Uf):
    """The five-dimensional Majumdar-Papapetrou form -dt^2/U^2 + U x (flat C^2 in Hopf form, (dr^2 + r^2 dOmega^2)/r + r (dpsi + cos theta
    dphi)^2) in (t, r, theta, phi, psi), r = |z|^2/4, U a jet in (r, theta); returns the metric and the potential A_t = (sqrt(3)/2)/U."""
    r = _V40Jet.var(S, 0, r0); th = _V40Jet.var(S, 1, th0); U = Uf(r, th); c = th.cos(); s2 = th.sin()*th.sin()
    z = _v40_zero(S, S.N); g = [[z for _ in range(5)] for _ in range(5)]
    g[0][0] = -1*(U*U).recip(); g[1][1] = U*r.recip(); g[2][2] = U*r; g[3][3] = U*(r*s2 + r*c*c); g[3][4] = g[4][3] = U*r*c; g[4][4] = U*r
    return g, (math.sqrt(3)/2)*U.recip()

def v40_0_rays():
    """Entries 507-510: the leaf's rays as pairs, Kepler's hidden symmetry, and the Hopf quotient with gravity (R574).  (a) A ray is a pair (u, v)
    in S^2 x S^2, the shared fiber of one left and one right Hopf structure; the rays through q are the graph of q's rotation; (R_q u).v = cos 2
    eta.  (b) Two rays meet exactly when u.u' = v.v'; their closest approach is |d_L - d_R|/2; the rays inside a great 2-sphere with pole m are
    the graph of -R_m; a ray's relative transport against a structure pair (U, V) is u.U - v.V, so zero relative phase is incidence with the
    hinge.  (c) Kepler (Fock, Moser): a bound orbit's velocity curve is a great circle of the 3-sphere, its labels along L + A and L - A (dot
    product 1 - 2e^2; the quaternion labels give 2e^2 - 1, one sphere's orientation reversed); unbound orbits are geodesics of hyperbolic space,
    their labels the asymptotes, dot product 1 - 2/e^2.  (d) Kustaanheimo-Stiefel: a four-dimensional oscillation read through the Hopf quotient
    and a time change is an exact Kepler orbit.  (e) Gibbons-Hawking: V (flat 3-metric) + (dpsi + A)^2/V is Ricci-flat exactly when V is
    harmonic and dA = *dV; a fiber mode exp(i n psi) carries n^2 V^2.  (f) The five-dimensional Majumdar-Papapetrou family, base and Hopf fiber
    scaled together by sqrt(U): Einstein-Maxwell when U is harmonic; its throat AdS2 x S^3, whose Hopf quotient is AdS2 x S^2 of equal radii,
    Bertotti-Robinson.  (g) The frozen point-source potential against 1/x: the relative corrections at second order, 11/6, 3/2, 7/4; exact at 8
    kpc on a 16 kpc leaf."""
    print("\n== v40.0-11. Entries 507-510: the leaf's rays as pairs, their incidence, Kepler's hidden symmetry, Kustaanheimo-Stiefel, "
          "Gibbons-Hawking and the fiber modes, the five-dimensional throat, and the leaf's local corrections (R574) ==")
    rng = random.Random(4011); e = [0.0]*4
    for _ in range(200):
        q, w = _v40_ray(rng); u, v = _v40_labels(q, w)
        e[0] = max(e[0], abs(_v40_norm(u) - 1), abs(_v40_norm(v) - 1))
        for t in (0.7, 1.9, 4.0):
            p = _v40_geo(q, w, t); dp = _v40_geo_dot(q, w, t)
            e[1] = max(e[1], _v40_norm(_v40_add(_v40_qmul(_v40_qconj(p), dp)[1:], u, -1.0)), _v40_norm(_v40_add(_v40_qmul(dp, _v40_qconj(p))[1:], v, -1.0)))
        e[2] = max(e[2], _v40_norm(_v40_add(_v40_rot(q, u), v, -1.0)))
        uu, vv = [0.0] + _v40_rand_unit(rng, 3), [0.0] + _v40_rand_unit(rng, 3); x = _v40_rand_unit(rng)
        p0 = _v40_add(_v40_qmul(vv, x), _v40_qmul(x, uu))
        if _v40_norm(p0) < 0.3: continue
        b1 = _v40_unit(p0); b2 = _v40_unit(_v40_qmul(b1, uu)); ce2 = _v40_dot(q, b1)**2 + _v40_dot(q, b2)**2
        e[3] = max(e[3], abs(_v40_dot(_v40_rot(q, uu[1:]), vv[1:]) - (2*ce2 - 1)))
    _v40_wrap(f"(a) Rays as pairs [T/V].  A great circle of the leaf through q with unit tangent w has the labels u = q^-1 w and v = w q^-1, unit "
              f"imaginary quaternions ({_v40_r(e[0])}), constant along the ray ({_v40_r(e[1])}): its tangent is at once the left field q u and the "
              f"right field v q, so each ray is the shared fiber of exactly one left and one right Hopf structure, and oriented rays are S^2 x S^2.  "
              f"The rays through q are the pairs (u, R_q u), R_q the rotation of q ({_v40_r(e[2])}): an observer's sky is the graph of a rotation, the "
              f"leaf RP^3 = SO(3) the set of such rotations, and q and -q give the same one.  For any ray (u, v) and any point q, (R_q u).v = cos 2 "
              f"eta, eta the angular distance from q to the ray ({_v40_r(e[3])}).")
    f = [0.0]*5
    for _ in range(300):
        r1, r2 = _v40_ray(rng), _v40_ray(rng); (u1, v1), (u2, v2) = _v40_labels(*r1), _v40_labels(*r2)
        cl = lambda x: max(-1.0, min(1.0, x)); dL, dR = math.acos(cl(_v40_dot(u1, u2))), math.acos(cl(_v40_dot(v1, v2)))
        f[0] = max(f[0], abs(_v40_principal(r1, r2)[0] - abs(dL - dR)/2))
        q = _v40_rand_unit(rng); wa, wb = _v40_rand_tangent(rng, q), _v40_rand_tangent(rng, q); (ua, va), (ub, vb) = _v40_labels(q, wa), _v40_labels(q, wb)
        f[1] = max(f[1], abs(_v40_dot(ua, ub) - _v40_dot(va, vb)))
        m_ = _v40_rand_unit(rng); p = _v40_rand_tangent(rng, m_); w = _v40_rand_tangent(rng, m_); w = _v40_unit(_v40_add(w, p, -_v40_dot(w, p)))
        u, v = _v40_labels(p, w); f[2] = max(f[2], _v40_norm(_v40_add(v, _v40_rot(m_, u))))
        U, V = [0.0] + _v40_rand_unit(rng, 3), [0.0] + _v40_rand_unit(rng, 3); qq, ww = r1
        f[3] = max(f[3], abs(_v40_dot(ww, _v40_add(_v40_qmul(qq, U), _v40_qmul(V, qq), -1.0)) - (_v40_dot(u1, U[1:]) - _v40_dot(v1, V[1:]))))
    _v40_wrap(f"(b) Incidence [T/V].  Two rays' closest approach on the leaf is |d_L - d_R|/2, half the difference of their separations on the "
              f"two spheres (300 random pairs, {_v40_r(f[0])}); they meet exactly when u.u' = v.v' (two rays through one point, {_v40_r(f[1])}), and "
              f"then at one point of RP^3: in the metric g_L - g_R of signature (2, 2) on S^2 x S^2, meeting rays are null-separated.  The rays inside "
              f"a great 2-sphere with pole m are the graph of -R_m ({_v40_r(f[2])}): points and planes of the leaf are the two families of null "
              f"spheres, and reversing one label's orientation exchanges them -- a sky becomes a disk.  Against a structure pair (U, V), a ray's "
              f"relative transport <tangent, X_L - X_R> is u.U - v.V ({_v40_r(f[3])}), so v40.0-10's closing, zero relative phase, is incidence with "
              f"the hinge, and the relative phase is cos d_L - cos d_R.  Every direction of a sky is a ray, so no direction is geometrically empty "
              f"(the second assessment's point): an obstruction has to come after incidence.")
    kep = []
    for ecc in (0.0, 0.3, 0.6, 0.9):
        Rq = _v40_rand_unit(rng); Lh, Ah = _v40_rot(Rq, [0, 0, 1]), _v40_rot(Rq, [1, 0, 0]); Lm = math.sqrt(1 - ecc*ecc)
        def xi(th):
            vv = _v40_rot(Rq, [-math.sin(th)/Lm, (ecc + math.cos(th))/Lm, 0.0]); v2 = _v40_dot(vv, vv)
            return [(v2 - 1)/(v2 + 1)] + _v40_scale(vv, 2/(v2 + 1))
        pts = [xi(th) for th in (0.3, 1.1, 2.0, 2.9, 4.2, 5.5)]; b1 = _v40_unit(pts[0]); b2 = _v40_unit(_v40_add(pts[1], b1, -_v40_dot(pts[1], b1)))
        plan = max(_v40_norm(_v40_add(_v40_add(p, b1, -_v40_dot(p, b1)), b2, -_v40_dot(p, b2))) for p in pts)
        q = xi(0.9); w = _v40_unit(_v40_add(xi(0.9 + 1e-6), xi(0.9 - 1e-6), -1.0)); u, v = _v40_labels(q, w)
        Jp = _v40_add(_v40_scale(Lh, Lm), _v40_scale(Ah, ecc)); Jm = _v40_add(_v40_scale(Lh, Lm), _v40_scale(Ah, -ecc))
        kep.append((ecc, plan, _v40_dot(u, Jp), _v40_dot(v, Jm), _v40_dot(u, v), _v40_dot(Jp, Jm)))
    unb = []
    for ecc in (1.2, 2.0, 5.0):
        Rq = _v40_rand_unit(rng); Lm = math.sqrt(ecc*ecc - 1); thi = math.acos(-1/ecc)
        vel = lambda th: _v40_rot(Rq, [-math.sin(th)/Lm, (ecc + math.cos(th))/Lm, 0.0])
        def xh(th):
            vv = vel(th); v2 = _v40_dot(vv, vv); return [(v2 + 1)/(v2 - 1)] + _v40_scale(vv, 2/(v2 - 1))
        pts = [xh(fr*thi) for fr in (-0.8, -0.5, -0.1, 0.3, 0.6, 0.85)]; hyp = max(abs(p[0]**2 - _v40_dot(p[1:], p[1:]) - 1) for p in pts)
        b1 = _v40_unit(pts[0]); b2 = _v40_unit(_v40_add(pts[2], b1, -_v40_dot(pts[2], b1)))
        plan = max(_v40_norm(_v40_add(_v40_add(p, b1, -_v40_dot(p, b1)), b2, -_v40_dot(p, b2)))/_v40_norm(p) for p in pts)
        unb.append((ecc, hyp, plan, _v40_dot(vel(-thi), vel(thi)), 1 - 2/ecc**2))
    _v40_wrap("(c) Kepler's hidden symmetry [T/V/L].  Bound orbits (mu = 1, E = -1/2): velocities sent to the 3-sphere by Fock's map xi = (v^2 - 1, "
              "2v)/(v^2 + 1) trace great circles (departure from a plane, then the ray's labels against the unit vectors along L + A and L - A, L and "
              "A the angular momentum and Runge-Lenz vectors at unit energy): " + "; ".join(
              f"e = {ecc:g}: {_v40_r(pl)}, u.(L+A) = {_v40_f(a_, 6)}, v.(L-A) = {_v40_f(b_, 6)}, u.v = {_v40_f(c_, 6)}, (L+A).(L-A) = {_v40_f(d_, 6)}"
              for ecc, pl, a_, b_, c_, d_ in kep) + ".  So the labels lie along -(L + A) and L - A: with the labels taken along L + A and L - A "
              "themselves the dot product is 1 - 2e^2, as the response and the assessment say, and the quaternion convention's 2e^2 - 1 is one "
              "sphere's orientation reversed -- the reversal that exchanges a sky and a disk in (b).  Their sum gives the orbit plane's normal, their "
              "difference the axis toward periapsis.  Unbound orbits (E = +1/2): xi = (v^2 + 1, 2v)/(v^2 - 1) lies on the hyperboloid and in a plane "
              "through the origin, a geodesic of hyperbolic 3-space (on it, then planar), and the two labels are the incoming and outgoing "
              "directions: " + "; ".join(f"e = {ecc:g}: {_v40_r(hy)}, {_v40_r(pl)}, n_in.n_out = {_v40_f(d_, 6)} against 1 - 2/e^2 = {_v40_f(x_, 6)}"
              for ecc, hy, pl, d_, x_ in unb) + " -- Rutherford's deflection.  The sign of the energy chooses the real form: the sphere for bound "
              "orbits, hyperbolic space for unbound ones.  The symmetry is exact for the inverse-square law only, not for a galaxy's potential.")
    i_ = [0.0, 1.0, 0.0, 0.0]; ks = []
    for trial in range(3):
        om = 0.4 + 0.3*trial; a = [rng.gauss(0, 1) for _ in range(4)]; b = [rng.gauss(0, 1) for _ in range(4)]
        ai = _v40_qmul(a, i_); b = _v40_add(b, ai, -_v40_dot(ai, b)/_v40_dot(ai, ai)); mu = 2*om*om*(_v40_dot(a, a) + _v40_dot(b, b))
        Ls, As, Es = [], [], []; hz = rr = 0.0
        for s in (0.0, 0.6, 1.7, 2.9, 4.4):
            q = _v40_add(_v40_scale(a, math.cos(om*s)), _v40_scale(b, math.sin(om*s)))
            dq = _v40_add(_v40_scale(a, -om*math.sin(om*s)), _v40_scale(b, om*math.cos(om*s)))
            X = _v40_qmul(_v40_qmul(q, i_), _v40_qconj(q))
            dX = _v40_add(_v40_qmul(_v40_qmul(dq, i_), _v40_qconj(q)), _v40_qmul(_v40_qmul(q, i_), _v40_qconj(dq)))
            r = _v40_dot(q, q); V = _v40_scale(dX[1:], 1/r); Xv = X[1:]
            hz = max(hz, abs(_v40_dot(_v40_qmul(q, i_), dq))); rr = max(rr, abs(_v40_norm(Xv) - r), abs(X[0]))
            Lv = _v40_cross(Xv, V); Av = _v40_add(_v40_cross(V, Lv), _v40_scale(Xv, 1/_v40_norm(Xv)), -mu)
            Ls.append(Lv); As.append(Av); Es.append(_v40_dot(V, V)/2 - mu/_v40_norm(Xv))
        ks.append((om, hz, rr, mu, max(_v40_norm(_v40_add(x, Ls[0], -1.0)) for x in Ls), max(_v40_norm(_v40_add(x, As[0], -1.0)) for x in As),
                   Es[0], max(Es) - min(Es), _v40_norm(As[0])/mu))
    _v40_wrap("(d) Kustaanheimo-Stiefel [T/V/L].  X = q i qbar, |X| = |q|^2, time dt = |q|^2 ds: a free oscillation q(s) of the four-dimensional "
              "space, horizontal (<q i, q'> = 0), read through the Hopf quotient and the time change, is an exact Kepler orbit with mu = 2(|q'|^2 + "
              "omega^2 |q|^2) -- " + "; ".join(f"omega = {om:g}: horizontal {_v40_r(hz)}, |X| = |q|^2 {_v40_r(rr)}, mu = {_v40_f(mu, 4)}, the angular "
              f"momentum and the Runge-Lenz vector constant ({_v40_r(dl)}, {_v40_r(da)}), the energy {_v40_f(E0, 6)} at every point (spread "
              f"{_v40_r(sp)}) against -2 omega^2, eccentricity {_v40_f(ec, 4)}" for om, hz, rr, mu, dl, da, E0, sp, ec in ks) + ".")
    S2 = _V40JetSpace(2); m = 1.0; d = 0.8; m2 = 0.6
    def twoV(r, th):
        z = r*th.cos(); s2 = r*r*th.sin()*th.sin()
        return 1 + m*(s2 + (z - d)*(z - d)).powr(-0.5) + m2*(s2 + (z + d)*(z + d)).powr(-0.5)
    def twoA(r, th):
        z = r*th.cos(); s2 = r*r*th.sin()*th.sin()
        return m*(z - d)*(s2 + (z - d)*(z - d)).powr(-0.5) + m2*(z + d)*(s2 + (z + d)*(z + d)).powr(-0.5)
    gh_cases = (("V = m/r, A = m cos theta dphi (flat four-space in Hopf form)", lambda r, th: m*r.recip(), lambda r, th: m*th.cos()),
                ("V = 1 + m/r, the same A (one source)", lambda r, th: 1 + m*r.recip(), lambda r, th: m*th.cos()),
                ("V = 1 + m/r1 + 0.6 m/r2, A the sum (two sources)", twoV, twoA),
                ("V = 1 + m/r, A halved (the twist not matched)", lambda r, th: 1 + m*r.recip(), lambda r, th: 0.5*m*th.cos()),
                ("V = 1 + m/r^2, not harmonic", lambda r, th: 1 + m*(r*r).recip(), lambda r, th: m*th.cos()))
    ghp = ((1.7, 0.9), (2.6, 1.8), (1.3, 2.3), (3.4, 0.6)); ghr = []
    for lab, Vf, Af in gh_cases:
        ghr.append((lab, max(_v40_maxabs(_v40_ricci(_v40_gh(S2, r0, th0, Vf, Af), [0, 1])[0]) for r0, th0 in ghp)))
    nV = [(r, (1 + 1/r)**2) for r in (0.1, 0.3, 1, 3, 10, 100)]
    _v40_wrap("(e) Gibbons-Hawking [T/V/L].  g = V (dr^2 + r^2 dOmega^2) + (dpsi + A dphi)^2/V, the base flat space times V and the fiber's length "
              "1/sqrt(V): largest Ricci component at four points, exact by jets -- " + "; ".join(f"{lab}: {_v40_r(w_) if w_ < 1e-8 else f'{w_:.1e}'}"
              for lab, w_ in ghr) + ".  The four-dimensional vacuum equation holds exactly when V is harmonic on the flat visible space and the "
              "fiber's twist is its dual, dA = *dV; solutions add.  It is Riemannian, its V the twist potential, and its fiber shrinks near a source "
              "(length 1/sqrt V).  A mode exp(i n psi) phi on it has Lap = exp(i n psi)[(grad - i n A)^2 phi/V - n^2 V phi]: against the flat visible "
              "metric it carries n^2 V^2, with V = 1 + m/r " + ", ".join(f"{_v40_f(v, 2)} at r = {r:g} m" for r, v in nV) + " (n = 1): fiber-dependence "
              "costs most near sources.")
    S2b = _V40JetSpace(2); a_, b_, d_ = 0.8, 0.5, 1.3
    mp_cases = (("one source, U = 1 + a/r", lambda r, th: 1 + a_*r.recip()),
                ("a second source uniform along one Hopf circle, U = 1 + a/r + b/|x - x0|",
                 lambda r, th: 1 + a_*r.recip() + b_*(r*r + d_*d_ - 2*d_*r*th.cos()).powr(-0.5)),
                ("U = 1 + a/r^2, not harmonic", lambda r, th: 1 + a_*(r*r).recip()))
    mpp = ((0.7, 0.9), (2.1, 1.8), (0.9, 2.4)); mpr = []
    for lab, Uf in mp_cases:
        wmax = wmxw = 0.0
        for r0, th0 in mpp:
            g, At = _v40_mp5(S2b, r0, th0, Uf); Ric, Rs, Ein, gv, gi = _v40_ricci(g, [1, 2])
            sdet = (-1*g[0][0]*g[1][1]*g[2][2]*(g[3][3]*g[4][4] - g[3][4]*g[4][3])).sqrt(); gtti = g[0][0].recip()
            j1 = (sdet*g[1][1].recip()*gtti*At.d(0)).d(0).val(); j2 = (sdet*g[2][2].recip()*gtti*At.d(1)).d(1).val()
            k1 = abs((sdet*g[1][1].recip()*gtti*At.d(0)).val()) + abs((sdet*g[2][2].recip()*gtti*At.d(1)).val())
            wmxw = max(wmxw, abs(j1 + j2)/(abs(j1) + abs(j2) + k1))
            Fl = [[0.0]*5 for _ in range(5)]; dAr, dAth = At.d(0).val(), At.d(1).val(); Fl[1][0], Fl[0][1], Fl[2][0], Fl[0][2] = dAr, -dAr, dAth, -dAth
            Fu = [[sum(gi[i][k]*gi[j][l]*Fl[k][l] for k in range(5) for l in range(5)) for j in range(5)] for i in range(5)]
            F2 = sum(Fl[i][j]*Fu[i][j] for i in range(5) for j in range(5))
            Rm = [[sum(gi[i][k]*Ric[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
            Em = [[2*(sum(Fu[i][k]*Fl[j][k] for k in range(5)) - (F2/6 if i == j else 0.0)) for j in range(5)] for i in range(5)]
            wmax = max(wmax, max(abs(Rm[i][j] - Em[i][j]) for i in range(5) for j in range(5)))
        mpr.append((lab, wmax, wmxw))
    aa = 0.8; Rt = []; Rq = []
    for r0, th0 in ((0.7, 0.9), (2.1, 1.8)):
        g, At = _v40_mp5(S2b, r0, th0, lambda r, th: aa*r.recip()); Ric, Rs, Ein, gv, gi = _v40_ricci(g, [1, 2])
        Rt.append([sum(gi[i][k]*Ric[k][i] for k in range(5)) for i in range(5)])
        def quot(V):
            r, th = V[0], V[1]; z = _v40_zero(S2b, S2b.N); g4 = [[z for _ in range(4)] for _ in range(4)]
            g4[0][0] = -1*r*r*(1/aa**2); g4[1][1] = aa*(r*r).recip(); g4[2][2] = _V40Jet.const(S2b, aa); g4[3][3] = aa*th.sin()*th.sin()
            return g4
        G4 = _v40_jet_metric(quot, S2b, (r0, th0), [1, 2]); R4, Rs4, E4, g4, gi4 = _v40_ricci(G4, [1, 2])
        Rq.append([sum(gi4[i][k]*R4[k][i] for k in range(4)) for i in range(4)])
    wt = max(abs(Rt[j][i] - [-1/aa, -1/aa, 1/(2*aa), 1/(2*aa), 1/(2*aa)][i]) for j in range(2) for i in range(5))
    wq = max(abs(Rq[j][i] - [-1/aa, -1/aa, 1/aa, 1/aa][i]) for j in range(2) for i in range(4))
    _v40_wrap("(f) A family that scales base and fiber together [T/V/L].  -dt^2/U^2 + U x (flat C^2), U uniform along the Hopf fibers and "
              "harmonic on the quotient three-space, is the five-dimensional Majumdar-Papapetrou form: every spatial length, base and fiber alike, "
              "is the background's times sqrt(U), the clock runs at 1/U.  Largest component of Ricci - 2(F F - g F^2/6), A = (sqrt(3)/2) dt/U, at "
              "three points, exact by jets, and the relative residual of Maxwell's equation d_i(sqrt|g| F^it) = 0: " + "; ".join(
              f"{lab}: {_v40_r(w_) if w_ < 1e-8 else f'{w_:.1e}'} and {_v40_r(wx_) if wx_ < 1e-8 else f'{wx_:.1e}'}" for lab, w_, wx_ in mpr)
              + f" (F wedge F = 0 for this static field, so the Chern-Simons term of five-dimensional supergravity does not enter).  Its "
              f"throat, U = a/r (a = {aa:g}), is a dr^2/r^2 - r^2 dt^2/a^2 + a[dOmega^2 + (dpsi + cos theta dphi)^2]: a round 3-sphere of radius "
              f"ell = 2 sqrt(a) with its Hopf fibers times AdS2 of radius ell/2 (mixed Ricci " + ", ".join(_v40_f(v, 6) for v in Rt[0]) + f"; "
              f"{_v40_r(wt)}).  Its Hopf quotient, a dr^2/r^2 - r^2 dt^2/a^2 + a dOmega^2, is AdS2 x S^2 with both radii ell/2, the Bertotti-Robinson "
              f"geometry (mixed Ricci " + ", ".join(_v40_f(v, 6) for v in Rq[0]) + f"; {_v40_r(wq)}) -- its metric; the reduced fields, a "
              f"Kaluza-Klein vector from the Hopf twist with the reduced Maxwell field, are not computed.  To first order in a source m: the frozen law "
              f"L_H = 2 pi ell phi^2, phi = 1 + m/2r, gives a fiber 1 + m/r; sqrt(U) with U = 1 + 2m/r gives 1 + m/r; Gibbons-Hawking's V^(-1/2), V "
              f"= 1 + 2m/r, gives 1 - m/r.  The family is charged and extremal, and five-dimensional; it is not Law I.")
    loc = []
    for lab, xf, lim in (("arc length, x = chi", lambda c: c, -11/6), ("gnomonic, x = tan chi", math.tan, -1.5), ("stereographic, x = 2 tan(chi/2)",
        lambda c: 2*math.tan(c/2), -1.75)):
        loc.append((lab, [((math.cos(2*c)/math.sin(c))*xf(c) - 1)/xf(c)**2 for c in (0.01, 0.001)], lim))
    lP = 16000.0; sizes = [(lab, 1.5*(r/lP)**2) for lab, r in (("1 AU", 4.848137e-6), ("1 pc", 1.0), ("1 kpc", 1000.0), ("8 kpc", 8000.0))]
    t8 = 0.5; c8 = math.atan(t8); F8 = math.cos(2*c8)/math.sin(c8); ex8 = F8*t8 - 1
    Fp = lambda c: -2*math.sin(2*c)/math.sin(c) - math.cos(2*c)*math.cos(c)/math.sin(c)**2
    force8 = (Fp(c8)*math.cos(c8)**2)/(-1/t8**2) - 1
    _v40_wrap("(g) The leaf's local corrections [T/V].  The frozen point-source potential F = cos 2chi/sin chi against 1/x: the relative "
              "correction (F x - 1)/x^2 at chi = 0.01 and 0.001 -- " + "; ".join(f"{lab}: " + ", ".join(_v40_f(v, 6) for v in vs) + f" (limit "
              f"{_v40_f(lim, 6)})" for lab, vs, lim in loc) + " -- so there is no first-order correction, and on a 16 kpc leaf the gnomonic one, "
              "(3/2)(R/ell)^2, is " + ", ".join(f"{v:.1e} at {lab}" for lab, v in sizes) + f".  At 8 kpc the leading estimate is not the answer: "
              f"the exact potential differs from ell/R by {_v40_f(ex8, 6)} against the leading -0.375, and the radial force from the inverse "
              f"square by +{_v40_f(force8, 6)} against the leading +0.375 -- the force stronger, the potential shallower (the second assessment's caution). "
              f" The visible Einstein condition is met by nineteen orders in the "
              f"solar system; at galactic radii the correction is the effect itself.")
    ok = (max(e) < 1e-12 and max(f) < 1e-12 and all(abs(a_ + 1) < 1e-6 and abs(b_ - 1) < 1e-6 and abs(c_ - (2*ecc*ecc - 1)) < 1e-6
        and abs(d_ - (1 - 2*ecc*ecc)) < 1e-9
          for ecc, pl, a_, b_, c_, d_ in kep) and all(abs(dv - xv) < 1e-9 for ecc, hy, pl, dv, xv in unb)
          and all(dl < 1e-12 and da < 1e-12 and sp < 1e-12 for om, hz, rr, mu, dl, da, E0, sp, ec in ks)
          and all(w_ < 1e-10 for lab, w_ in ghr[:3]) and all(w_ > 1e-3 for lab, w_ in ghr[3:])
          and all(w_ < 1e-10 and wx_ < 1e-10 for lab, w_, wx_ in mpr[:2]) and mpr[2][1] > 0.1 and mpr[2][2] > 1e-3 and wt < 1e-10 and wq < 1e-10
          and all(abs(vs[1] - lim) < 1e-5 for lab, vs, lim in loc) and -0.34 < ex8 < -0.32)
    check(ok, "v40.0-11: rays are pairs (u, v), a sky the graph of R_q, meeting when u.u' = v.v'; Kepler's labels L + A and L - A, 1 - 2e^2; KS and "
              "Gibbons-Hawking exact; the 5D throat's Hopf quotient is Bertotti-Robinson; the leaf's corrections start at (R/ell)^2")

def v40_0_overlay():
    """Entries 512-513, the two questions after them, and the responses to them: the closed-leaf hole with acceleration (R575).  (a) The
    non-accelerating member on a closed leaf, Schwarzschild- (Kerr-) de Sitter: one period of its time-symmetric slice runs from the hole's
    throat through a third horizon on the equator to the twin's throat, S^2 x [-D, D]; no singularity lies on the slice; the antipodal map
    (y, n) -> (-y, -n) is a free isometry, the quotient RP^3 with one ball removed, extending to the spacetime as U <-> V with the sphere's
    antipode, reversing the static Killing field and the sign of a charge.  (b) Accelerating Kerr-de Sitter (Podolsky and Griffiths): a solution;
    its rings at r = 0 on each pole's equatorial plane kept; the middle horizon moving inward with A, the others barely; without mass only
    A^2 + Lambda/3 appears;
    the two halves of the axis disagree by P(pi) - P(0) = 4AM whatever the spin and the curvature, the deficit 4AM/(1 + 2AM).  (c) Without mass
    the middle horizon is the round sphere of radius L read from a displaced position, A = tan(p)/L.  (d) With mass and acceleration the
    antipodal map exchanges two unequal axis points: it takes A to -A; the reflection across the middle horizon, a different map from
    v40.0-7(d)'s mirror, stays a symmetry for every A.  (e) An offset
    of convention: the matching rotations at two positions differ by twice their separation.  (f) A collective selection of a plane, under a
    product premise: width 1/sqrt(N gamma).  (g) A mode uniform along a Hopf direction is even under the antipodal map: the antipodal map is
    the Hopf rotation by pi."""
    print("\n== v40.0-12. Entries 512-513, the two questions after them and the responses: the closed-leaf hole with acceleration -- three "
          "horizons, the two-pole leaf and its antipodal map, the axis mismatch, acceleration as a held reference, the deck test, and the "
          "convention's offset (R575) ==")
    M, L = 1.0, 10.0; sds = []
    for Q in (0.0, 1.0):
        f = lambda r: 1 - 2*M/r + Q*Q/r**2 - r*r/L**2; df = lambda r: 2*M/r**2 - 2*Q*Q/r**3 - 2*r/L**2
        rts = _v40_roots(f, 0.05, 12.0, 40000); rb, rc = rts[-2], rts[-1]
        def integ(t, f=f, df=df, rb=rb, rc=rc):
            if t <= 0.0: return 2*math.sqrt((rc - rb)/abs(df(rb)))
            if t >= math.pi/2: return 2*math.sqrt((rc - rb)/abs(df(rc)))
            r = rb + (rc - rb)*math.sin(t)**2; return 2*(rc - rb)*math.sin(t)*math.cos(t)/math.sqrt(f(r))
        dist = _v40_simpson(integ, 0.0, math.pi/2, 20000)
        sds.append((Q, rb, abs(df(rb))/2, rc, abs(df(rc))/2, dist))
    rb, rc = sds[0][1], sds[0][3]; rn = -(rb + rc)
    D = _v40_simpson(lambda t: 2*L*math.sqrt((rb + (rc - rb)*math.sin(t)**2)/((rb + (rc - rb)*math.sin(t)**2) - rn)), 0.0, math.pi/2, 20000)
    _v40_wrap(f"(a) The non-accelerating member on a closed leaf [T/V].  f = 1 - 2M/r + Q^2/r^2 - r^2/L^2, M = 1, L = 10: " + "; ".join(
              f"Q = {Q:g}: the hole's horizon r = {_v40_f(b_, 6)} (surface gravity {_v40_f(kb, 6)}), the equatorial horizon r = {_v40_f(c_, 6)} "
              f"({_v40_f(kc, 6)}), proper distance between them {_v40_f(dd, 3)}" for Q, b_, kb, c_, kc, dd in sds) + f" (a quarter circle of the "
              f"leaf, pi L/2, is {_v40_f(math.pi*L/2, 3)}).  The time-symmetric slice between two neighboring hole horizons is S^2 x [-D, D], D = "
              f"{_v40_f(D, 4)} for Q = 0: the hole's throat, a smallest sphere, at one end, the equatorial horizon, a largest sphere, in the middle, "
              f"the twin's throat at the other end -- pole to pole 2D = {_v40_f(2*D, 4)} against pi L = {_v40_f(math.pi*L, 4)}.  The slice runs "
              f"throat to throat, so no singularity lies on the leaf; the rings and the central singularities are inside, off the slice.  The "
              f"antipodal map (y, n) -> (-y, -n) is an isometry, because r(-y) = r(y), and free; the quotient is RP^3 with one ball removed -- one "
              f"hole, Law I's one source -- with the equatorial sphere folded to RP^2.  It extends to the spacetime as the reflection U <-> V of "
              f"the equatorial horizon's Kruskal coordinates (the metric depends on UV only) with the sphere's antipode; it keeps the direction of "
              f"time and reverses the static Killing field, so the quotient is static locally but not globally, and it reverses an electric charge "
              f"(v40.0-7(b)).  The frozen arena is static throughout with no equatorial horizon: there the comparison still differs.  Matching only "
              f"the cosmological constants, Lambda = 1/ell^2 for the Einstein-static leaf against 3/L^2, would need L = sqrt(3) ell (the response's "
              f"point); the matter differs too.")
    S2 = _V40JetSpace(2); a = 0.7; Lam = 3/L**2; wsol = []
    for A in (0.0, 0.05):
        w_ = 0.0
        for r0, th0 in ((2.6, 0.8), (4.1, 1.9), (5.5, 2.5)):
            Ric = _v40_ricci(_v40_acc_kerr(S2, r0, th0, M, a, A, L=L), [1, 2]); gi = Ric[4]
            Rm = [[sum(gi[i][k]*Ric[0][k][j] for k in range(4)) for j in range(4)] for i in range(4)]
            w_ = max(w_, max(abs(Rm[i][j] - (Lam if i == j else 0.0)) for i in range(4) for j in range(4)))
        wsol.append((A, w_))
    tab = []
    for A in (0.0, 0.05, 0.12):
        Qf = lambda r, A=A: (r*r - 2*M*r + a*a)*(1 - A*A*r*r) - (Lam/3)*(a*a + r*r)*r*r; rts = _v40_roots(Qf, 0.01, 12.0, 60000)
        tab.append((A, rts[0], rts[1], rts[2], 1/math.sqrt(A*A + 1/L**2)))
    wcomb = 0.0
    for A in (0.0, 0.05, 0.12):
        Q0 = lambda r: (r*r + a*a)*(1 - A*A*r*r) - (Lam/3)*(a*a + r*r)*r*r; P0 = lambda t: 1 + (A*A + Lam/3)*a*a*math.cos(t)**2
        wcomb = max(wcomb, max(abs(Q0(r) - (r*r + a*a)*(1 - (A*A + Lam/3)*r*r)) for r in (0.5, 2.0, 5.0, 9.0)))
    mis = []
    for A in (0.0, 0.05, 0.12):
        P = lambda t: 1 - 2*A*M*math.cos(t) + (A*A*a*a + (Lam/3)*a*a)*math.cos(t)**2; mis.append((A, P(0.0), P(math.pi), P(math.pi) - P(0.0)))
    _v40_wrap(f"(b) Accelerating Kerr-de Sitter [T/V/L].  The family in Podolsky and Griffiths's form, with Omega = 1 - A r cos theta, P = 1 - 2AM cos "
              f"theta + (A^2 a^2 + Lambda a^2/3) cos^2 theta and Q = (r^2 - 2Mr + a^2)(1 - A^2 r^2) - (Lambda/3)(a^2 + r^2) r^2, is a solution, "
              f"mixed Ricci = Lambda (M = 1, a = 0.7, L = 10; jets at three points): " + "; ".join(f"A = {A:g}: {_v40_r(w_)}" for A, w_ in wsol)
              + ".  From one pole to the other the roots of Q are the inner horizon, the outer horizon and the horizon between the poles, then "
              f"their mirror copies: " + "; ".join(f"A = {A:g}: {_v40_f(r1, 6)}, {_v40_f(r2, 6)}, {_v40_f(r3, 6)} (1/sqrt(A^2 + 1/L^2) = {_v40_f(rh, 6)})"
              for A, r1, r2, r3, rh in tab) + ".  The rings, r = 0 on each pole's equatorial plane, where rho^2 = 0 and Omega = 1, are kept: the "
              f"C-metric built before is this family, consistent with a ring at each pole.  The inner and outer horizons barely move -- with "
              f"Lambda = 0 they would not move at all, Q being then (r^2 - 2Mr + a^2)(1 - A^2 r^2) -- while the middle horizon moves inward, "
              f"from {_v40_f(tab[0][3], 6)} to {_v40_f(tab[2][3], 6)}.  Without mass, Q = (r^2 + "
              f"a^2)(1 - (A^2 + Lambda/3) r^2) and P = 1 + (A^2 + Lambda/3) a^2 cos^2 theta ({_v40_r(wcomb)}): only A^2 + Lambda/3 appears -- in the "
              f"horizon's coordinate size, not in the curvature, which stays 4 Lambda.  The two halves of the axis need the periods 2 pi/P(0) and 2 "
              f"pi/P(pi): " + "; ".join(f"A = {A:g}: P(0) = {_v40_f(p0, 6)}, P(pi) = {_v40_f(pp, 6)}, difference {_v40_f(dd, 6)}" for A, p0, pp, dd in mis)
              + " -- 4AM whatever the spin and the curvature: no string exactly when MA = 0.  4AM is a difference of the polynomial's values; the "
              f"deficit itself, one axis regular, is 1 - P(0)/P(pi), 4AM/(1 + 2AM) = {_v40_f(0.48/1.24, 6)} at A = 0.12 without spin, v40.0-2(b)'s "
              f"0.387097.")
    hold = []
    for A in (0.05, 0.12, 0.30):
        rc_ = 1/math.sqrt(A*A + 1/L**2); E = lambda th: rc_/(1 - A*rc_*math.cos(th))
        def gauss(th, h=1e-4):
            Gm = lambda t: E(t)*math.sin(t); dv = lambda t: (Gm(t + h) - Gm(t - h))/(2*h)/E(t)
            return -((dv(th + h) - dv(th - h))/(2*h)/E(th))/Gm(th)
        p = math.atan(A*L); hold.append((A, rc_, [gauss(t) for t in (0.4, 1.3, 2.6)], math.degrees(p), L*math.cos(p), A*rc_, math.sin(p)))
    _v40_wrap(f"(c) Acceleration as a held reference [T/V].  Without mass the middle horizon r = 1/sqrt(A^2 + 1/L^2) carries the metric "
              f"E(theta)^2 (dtheta^2 + sin^2 theta dphi^2), E = r/(1 - A r cos theta); its Gauss curvature (fourth-order differences) is 1/L^2 at "
              f"every latitude: " + "; ".join(f"A = {A:g}: r = {_v40_f(r_, 6)}, " + ", ".join(_v40_f(k_, 6) for k_ in ks) + f"; p = atan(AL) = "
              f"{_v40_f(pd, 2)} degrees, L cos p = {_v40_f(lc, 6)}, A r = {_v40_f(ar, 6)} = sin p {_v40_f(sp, 6)}" for A, r_, ks, pd, lc, ar, sp in hold)
              + ".  It is the round sphere of radius L in coordinates shifted by the boost with tanh s = A r (v36.3's Moebius factor): A = tan(p)/L "
              f"is the acceleration of a reference held at the angle p from the leaf's pole.  So without mass a reference offset is an acceleration, "
              f"and the horizon is the leaf's equator seen from the offset; this is an acceleration of a held reference, not a recession of the "
              f"static leaf's poles.  With mass, holding the hole at that offset costs, to first order in MA, a force MA; the string's exact "
              f"tension is the deficit over four, MA/P(pi) = MA/(1 + 2MA) without spin, {_v40_f(0.12/1.24, 6)} at A = 0.12 against MA = 0.12.")
    asy = []
    for Mm, A in ((0.0, 0.12), (1.0, 0.0), (1.0, 0.05), (1.0, 0.12)):
        if Mm > 0:
            Qr = lambda r, A=A: (r*r - 2*Mm*r)*(1 - A*A*r*r) - r**4/L**2; rts = _v40_roots(Qr, 2.5*Mm + 0.2, 2*L, 40000); rc_ = rts[-1]
        else: rc_ = 1/math.sqrt(A*A + 1/L**2)
        P = lambda th: 1 - 2*A*Mm*math.cos(th); Om = lambda th: 1 - A*rc_*math.cos(th)
        ds = lambda th: rc_/(Om(th)*math.sqrt(P(th))); C = lambda th: rc_*math.sqrt(P(th))*math.sin(th)/Om(th)
        N = 400; ths = [math.pi*i/N for i in range(N + 1)]; ss = [0.0]
        for i in range(N): ss.append(ss[-1] + _v40_simpson(ds, ths[i], ths[i + 1], 20))
        Stot = ss[-1]
        def Cat(s):
            for i in range(N):
                if ss[i] <= s <= ss[i + 1]:
                    w_ = (s - ss[i])/(ss[i + 1] - ss[i]); return (1 - w_)*C(ths[i]) + w_*C(ths[i + 1])
            return 0.0
        asym = max(abs(Cat(s) - Cat(Stot - s)) for s in [Stot*j/200 for j in range(1, 200)])/max(C(t) for t in ths)
        asy.append((Mm, A, rc_, P(0.0), P(math.pi), 1 - P(0.0)/P(math.pi), asym))
    fas = lambda x_: _v40_r(x_) if x_ < 1e-12 else format(x_, ".1e")
    _v40_wrap(f"(d) The deck test [T/V].  On the middle horizon, the leaf's antipodal map must exchange the two points where the axis pierces it and "
              f"reverse the sphere's profile (circumference radius against proper distance from one axis point; the asymmetry is relative): " + "; ".join(
              f"M = {Mm:g}, A = {A:g}: horizon r = {_v40_f(r_, 6)}, cone factors {_v40_f(p0, 4)} and {_v40_f(pp, 4)}, deficit {_v40_f(df_, 6)}, profile "
              f"asymmetry {fas(as_)}" for Mm, A, r_, p0, pp, df_, as_ in asy) + ".  It can when MA = 0 (the M = 0 value is the profile's "
              f"discretization).  With mass and acceleration the cone factors differ and the profile is lopsided: the antipodal map takes the "
              f"solution with A to the one with -A, so acceleration is odd under it, as charge is -- it belongs to the chosen representative on the "
              f"covering sphere, not to the gravity base; the even effects, like the A^2 shift of the middle horizon, are compatible with one "
              f"source.  The reflection y -> -y alone, across the middle horizon (U <-> V in its Kruskal coordinates), fixes that horizon "
              f"pointwise and is a symmetry for every A, as for any static bifurcate Killing horizon -- the case here, a = 0 -- while with spin "
              f"it is one only together with phi -> -phi (a standard property, not computed here); it is a "
              f"different map from v40.0-7(d)'s mirror, which exchanges the hole's horizon with the Rindler horizon and exists, as an isometry, "
              f"only for charge alone, at A = c/q^2.")
    rng = random.Random(4012); wrot = 0.0; E3 = ([1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0])
    for _ in range(300):
        q = _v40_rand_unit(rng); p = _v40_rand_unit(rng); d = math.acos(min(1.0, abs(_v40_dot(q, p))))
        Rp = [_v40_rot(p, e) for e in E3]; Rq = [_v40_rot(q, e) for e in E3]; Mx = [[_v40_dot(Rp[i], Rq[j]) for j in range(3)] for i in range(3)]
        sn = 0.5*math.sqrt((Mx[2][1] - Mx[1][2])**2 + (Mx[0][2] - Mx[2][0])**2 + (Mx[1][0] - Mx[0][1])**2)
        ang = math.atan2(sn, (Mx[0][0] + Mx[1][1] + Mx[2][2] - 1)/2); wrot = max(wrot, abs(ang - 2*d))
    from fractions import Fraction
    def hrank(rows, ncol):
        R_ = [r_[:] for r_ in rows if any(r_)]; rk = 0
        for c_ in range(ncol):
            piv = next((i for i in range(rk, len(R_)) if R_[i][c_] != 0), None)
            if piv is None: continue
            R_[rk], R_[piv] = R_[piv], R_[rk]
            for i in range(len(R_)):
                if i != rk and R_[i][c_] != 0:
                    f_ = R_[i][c_]/R_[rk][c_]; R_[i] = [x - f_*y for x, y in zip(R_[i], R_[rk])]
            rk += 1
        return rk
    def hmodes(n):
        B_ = [e for e in itertools.product(range(n + 1), repeat=4) if sum(e) == n]; col = {e: k for k, e in enumerate(B_)}
        def op(terms):
            out = {}
            for k, e in enumerate(B_):
                for (i, j, sg) in terms:
                    if e[i] == 0: continue
                    e2 = list(e); e2[i] -= 1; e2[j] += 1; out.setdefault(tuple(e2), [Fraction(0)]*len(B_))[k] += sg*e[i]
            return list(out.values())
        lap = {}
        for k, e in enumerate(B_):
            for i in range(4):
                if e[i] >= 2:
                    e2 = list(e); e2[i] -= 2; lap.setdefault(tuple(e2), [Fraction(0)]*len(B_))[k] += e[i]*(e[i] - 1)
        L_ = list(lap.values())
        XL = op([(0, 1, -1), (1, 0, 1), (2, 3, -1), (3, 2, 1)]); XR = op([(0, 1, -1), (1, 0, 1), (2, 3, 1), (3, 2, -1)])
        nb = len(B_); h = nb - hrank(L_, nb); hl = nb - hrank(L_ + XL, nb); hb = nb - hrank(L_ + XL + XR, nb)
        return n, h, hl, hb
    hh, ell = 3.0, 16.0
    num = _v40_simpson(lambda R: R*R/(1 + R*R/ell**2)**2*math.exp(-R/hh)*R, 0.0, 200.0, 40000)
    den = _v40_simpson(lambda R: math.exp(-R/hh)*R, 0.0, 200.0, 40000)
    gam = num/den/(2*ell**2); widths = [(N, 1/math.sqrt(N*gam)) for N in (1, 1e6, 1e11)]
    whopf = 0.0
    for _ in range(100):
        x = _v40_rand_unit(rng); z = (complex(x[0], x[1])*cmath.exp(1j*math.pi), complex(x[2], x[3])*cmath.exp(1j*math.pi))
        whopf = max(whopf, abs(z[0].real + x[0]) + abs(z[0].imag + x[1]) + abs(z[1].real + x[2]) + abs(z[1].imag + x[3]))
    modes = [hmodes(n) for n in range(0, 7)]
    _v40_wrap(f"(e) An offset of convention [T/V].  The rotations R_p and R_q that match the two spheres of rays at two positions, as 3 x 3 "
              f"matrices, differ by R_p^T R_q, a rotation through twice the leaf distance between p and q (300 random pairs, the angle from the "
              f"matrix against 2 d(p, q), {_v40_r(wrot)}): a convention read from a position displaced by eta mismatches every sky "
              f"direction's pair of labels by a turn of 2 eta about the displacement, while rotating the sky in place changes nothing.  Whether "
              f"such a mismatch is felt as an A is not derived: it must change an invariant, and with mass the C-metric needs its string.  (f) A "
              f"collective selection [T/V; premise].  If the joint weight of N constituents is the product of their two-lane weights cos^2(phase/2) "
              f"(a toy model), a tilt eps of the reference plane gives the weight exp(-N gamma eps^2) with gamma = <R^2 cos^4 chi>/(2 ell^2) = "
              f"{_v40_f(gam, 4)} for the exponential disk, h = 3 kpc, ell = 16 kpc, from v40.0-10's lane phase; the width 1/sqrt(N gamma) is " + ", ".join(
              f"{w_:.2e} rad at N = {N:.0e}" for N, w_ in widths) + f" ({_v40_f(math.degrees(widths[1][1]), 3)} degrees at 1e6, "
              f"{_v40_f(math.degrees(widths[2][1])*3600, 2)} arcsec at 1e11): one constituent selects nothing, many select sharply, a continuous "
              f"classical family notwithstanding.  The width is in the reference's tilt, not the disk's thickness, and N_eff and gamma are not derived.  "
              f"(g) Uniform along the fiber [T/V].  The Hopf rotation by pi is the antipodal map (an identity, e^(i pi) = -1; {_v40_r(whopf)}), so "
              f"a mode uniform along a Hopf direction is even under it, which is Law I's one-source condition.  The harmonics of degree n on the "
              f"3-sphere, the kernel of the Laplacian on the homogeneous polynomials of degree n in four variables, and among them those killed by "
              f"the generator of the left Hopf rotation, and by both the left and the right (exact rational ranks): " + "; ".join(
              f"n = {n}: {a_} in all, {b_} uniform along one Hopf direction, {c_} along both" for n, a_, b_, c_ in modes)
              + " -- the uniform ones have even degree, (n + 1) of (n + 1)^2, by bidegree (p, q) with p = q.")
    ok = (abs(sds[0][1] - 2.091488) < 1e-6 and abs(sds[1][2] - sds[1][4]) < 1e-9 and abs(D - sds[0][5]) < 1e-3 and all(w_ < 1e-10 for A, w_ in wsol)
          and abs(tab[0][3] - 8.798382) < 1e-5 and tab[2][3] < tab[1][3] < tab[0][3] and wcomb < 1e-12 and all(abs(dd - 4*A*M) < 1e-12 for A, p0, pp, dd in mis)
          and all(max(abs(k_*L*L - 1) for k_ in ks) < 1e-5 for A, r_, ks, pd, lc, ar, sp in hold) and all(abs(ar - sp) < 1e-12 for A, r_, ks, pd, lc, ar,
              sp in hold)
          and asy[1][6] < 1e-9 and asy[2][6] > 0.05 and asy[3][6] > asy[2][6] and abs(asy[3][5] - 0.387097) < 1e-6 and wrot < 1e-12
          and abs(gam - 0.0498) < 1e-3 and whopf < 1e-15
          and all(h_ == (n + 1)**2 and hl == (n + 1 if n % 2 == 0 else 0) and hb == (1 if n % 2 == 0 else 0) for n, h_, hl, hb in modes))
    check(ok, "v40.0-12: on the closed leaf one period of the slice runs throat - equatorial horizon - throat, the antipodal map a free isometry; "
              "acceleration keeps the rings, moves the middle horizon, costs 4AM on the axis, and is odd under the deck map; A = tan(p)/L without mass")

def v40_0_suite():
    """The v40.0 sections: Entry 489's sphere of references; the C-metric beside Kerr; the region between the horizons; Entry 493's throat and the
    Higgs condition; the type D structure and strip-constrain-restore; Entry 495's charged C-metric; Entry 497's Law I on the leaf and the mirror;
    Entries 498-499's galaxy image and its trade-off; Entries 500-501's conformal factor and readouts; Entries 502-506's two Hopf fields; Entries
    507-510's rays and reductions; and Entries 512-513's closed-leaf hole with acceleration."""
    v40_0_sphere(); v40_0_cmetric(); v40_0_rectangle(); v40_0_throat(); v40_0_typeD(); v40_0_charged(); v40_0_lawone(); v40_0_galaxy()
    v40_0_conformal(); v40_0_lanes(); v40_0_rays(); v40_0_overlay()


# ==================================================================================================== v40.1 (20-21 November 2026): sections
# The follow-up of 20-21 November: Entry 326's falloff k = ell/h on a leaf and the curve's shape classes (R581); the Newtonian reading of the
# leaf's curve -- the image's own thin disk and a driven remainder -- against the halo families, a leaf per galaxy, and the two dwarfs with the
# leaf free (R582).  The ported thin-disk solver of v40.0-8 is used through kernel rows computed once per field point: the source enters only
# through its values at a row's nodes, so that one row serves every k.  The rows take 256 azimuths in the ring kernel's bounded remainder, where
# v40.0's solver takes 64: that rule's error falls as the inverse cube of the number of azimuths and is about 2e-5 of v^2 at 64 for broad
# sources.  Extrema, crossings and slopes are read from an eight-point interpolating polynomial in ln R on the rows' grid.

_V41_BRK = tuple(0.0025*2.0**m for m in range(10))     # fixed panel breaks in chi, 0.0025 ... 1.28, for every source
_V41_NPHI = 256                                         # azimuths in the ring kernel's bounded remainder for the rows (v40.0: 64)

def _v41_at_nphi(nphi, fn):
    """fn() with nphi azimuths in the bounded remainder of v40.0's ring kernel; the module's 64 are restored afterward."""
    global _V40_NPHI, _V40_COSPHI
    keep = (_V40_NPHI, _V40_COSPHI)
    try:
        _V40_NPHI = nphi; _V40_COSPHI = [math.cos((k + 0.5)*(2*math.pi/nphi)) for k in range(nphi)]
        return fn()
    finally:
        _V40_NPHI, _V40_COSPHI = keep

def _v41_row(x, xmax=math.pi/2, nref=12):
    """At chi = x, the sines of the nodes and the coefficients 2 pi w sin(t) K(x, t) of v40.0's ring kernel, so that the potential of a leaf
    density Sigma(chi) at x is sum(c Sigma(t)): v40.0's panels, graded toward x and refined twelve times, with the breaks _V41_BRK for every
    source in place of a source's own."""
    dmin = x*2.0**(-nref)
    pts = [0.0, xmax] + [p for p in _V41_BRK if 0 < p < xmax and abs(p - x) > dmin]
    pts += [x + s*x*2.0**(-k) for k in range(1, nref + 1) for s in (-1, 1) if 0 < x + s*x*2.0**(-k) < xmax]
    if 0 < x < xmax: pts.append(x)
    e = sorted(set(pts)); ss, cs = [], []
    for a, b in zip(e[:-1], e[1:]):
        for t, w in _v40_graded(a, b, abs(a - x) < 1e-15*x, abs(b - x) < 1e-15*x):
            ss.append(math.sin(t)); cs.append(2*math.pi*w*math.sin(t)*_v40_ring_kernel(x, t))
    return ss, cs

def _v41_nrow(R, nref=12):
    """At radius R in the flat image plane (unit leaf), the coefficients of a thin disk's Newtonian potential (G = 1), Phi(R) = -4 int
    Sigma(R') R' K(m)/(R + R') dR', m = 4 R R'/(R + R')^2, over R' = tan t on the panels of _v41_row: the nodes' t and coefficients."""
    c0 = math.atan(R); dmin = c0*2.0**(-nref); cmax = math.pi/2
    pts = [0.0, cmax] + [p for p in _V41_BRK if 0 < p < cmax and abs(p - c0) > dmin]
    pts += [c0 + s*c0*2.0**(-k) for k in range(1, nref + 1) for s in (-1, 1) if 0 < c0 + s*c0*2.0**(-k) < cmax]
    pts.append(c0); e = sorted(set(pts)); ts, cs = [], []
    for a, b in zip(e[:-1], e[1:]):
        for t, w in _v40_graded(a, b, abs(a - c0) < 1e-15*c0, abs(b - c0) < 1e-15*c0):
            Rp = math.tan(t); cs.append(-4*w*Rp*_v40_ellipkm1(((R - Rp)/(R + Rp))**2)/(R + Rp)/math.cos(t)**2); ts.append(t)
    return ts, cs

def _v41_dot(row, k):
    """The potential at a row's point of e^(-k sin chi) - e^(-k): a uniform density on the leaf's great sphere, invariant under its rotations,
    has a constant potential there and exerts no force in the plane, so that the source less its equatorial value gives the same field; for
    small k this removes the nearly uniform bulk whose cancellation would cost digits."""
    ss, cs = row; e = math.exp(-k); return sum(c*(math.exp(-k*s) - e) for s, c in zip(ss, cs))

def _v41_ndot(row, k):
    ss, cs = row; return sum(c*math.exp(-k*s) for s, c in zip(ss, cs))

def _v41_image_row(nrow):
    """A Newtonian row recast for the image of e^(-k sin chi): Sigma_vis = e^(-k sin t) cos^3 t/(2 pi I(k)) at R' = tan t."""
    ts, cs = nrow; return [math.sin(t) for t in ts], [c*math.cos(t)**3 for t, c in zip(ts, cs)]

_V41_NJ = 150                                           # the common grid: tan chi_j = 10^(-3.7 + j/25), j = 0..149, to R = 182 ell
_V41_LG = [(-3.7 + j/25)*math.log(10.0) for j in range(_V41_NJ)]
_V41_CACHE = {}

def _v41_grid():
    """The rows at the common grid's points chi_j -- each point's two rows at chi_j -/+ dh, dh = min(1e-4, 0.02 chi_j), of v40.0's centered
    difference, for the leaf (with _V41_NPHI azimuths) and for the image plane -- the equator's rows for C(k), and the nodes of the
    normalization; computed once."""
    if 'grid' in _V41_CACHE: return _V41_CACHE['grid']
    row = lambda x: _v41_at_nphi(_V41_NPHI, lambda: _v41_row(x))
    pts = []
    for lg in _V41_LG:
        x = math.atan(math.exp(lg)); dh = min(1e-4, 0.02*x)
        pts.append((x, dh, row(x - dh), row(x + dh), _v41_image_row(_v41_nrow(math.tan(x - dh))), _v41_image_row(_v41_nrow(math.tan(x + dh)))))
    eq = (row(math.pi/2), [row(math.pi/2 - d) for d in (0.02, 0.01, 0.005)], [row(math.pi/2 - d) for d in (0.04, 0.08, 0.12, 0.16)])
    e = sorted(set([0.0, math.pi/2] + [p for p in _V41_BRK if p < math.pi/2])); ss, cs = [], []
    for a, b in zip(e[:-1], e[1:]):
        for t, w in _v40_graded(a, b, False, False): ss.append(math.sin(t)); cs.append(2*math.pi*w*math.sin(t))
    _V41_CACHE['grid'] = (pts, eq, (ss, cs)); return _V41_CACHE['grid']

def _v41_curves(k, newton=True):
    """For e^(-k sin chi) on the unit leaf (G M/ell = 1): v^2 on the common grid by Law I (u) and, with newton, by Newton for its image (un);
    C(k), the equatorial ratio psi''''/psi'' and the far-field coefficient A/(v_inf^2 ell^2) = psi''''/(6 psi'') - 1/3."""
    if ('k', k, True) in _V41_CACHE: return _V41_CACHE[('k', k, True)]
    if not newton and ('k', k, False) in _V41_CACHE: return _V41_CACHE[('k', k, False)]
    pts, eq, nrm = _v41_grid(); nk = _v41_ndot(nrm, k)
    u, un = [], []
    for x, dh, rm, rp, nm, np_ in pts:
        u.append(-2*math.tan(x)*(_v41_dot(rp, k) - _v41_dot(rm, k))/(2*dh)/nk)
        if newton:
            R1, R2 = math.tan(x - dh), math.tan(x + dh)
            un.append(math.tan(x)*(_v41_ndot(np_, k) - _v41_ndot(nm, k))/(R2 - R1)/nk)
    p0 = _v41_dot(eq[0], k)/nk; hs = (0.02, 0.01, 0.005)
    vals = [4*(_v41_dot(r, k)/nk - p0)/h**2 for r, h in zip(eq[1], hs)]; rr = (hs[-2]/hs[-1])**2
    C = (rr*vals[-1] - vals[-2])/(rr - 1)
    ds = (0.04, 0.08, 0.12, 0.16); dif = [_v41_dot(r, k)/nk - p0 for r in eq[2]]
    co = _v40_mm(_v40_inv([[d**(2*m) for m in range(1, 5)] for d in ds]), [[v] for v in dif])
    ratio = 12*co[1][0]/co[0][0]
    out = dict(k=k, u=u, un=un, C=C, ratio=ratio, A=ratio/6 - 1/3, norm=nk)
    _V41_CACHE[('k', k, newton)] = out; return out

def _v41_interp(vals, lg):
    """Four-point Lagrange interpolation in ln(R/ell) on the common grid."""
    t = (lg - _V41_LG[0])/(_V41_LG[1] - _V41_LG[0]); j = min(max(int(math.floor(t)) - 1, 0), _V41_NJ - 4); s = t - j
    w = [-(s - 1)*(s - 2)*(s - 3)/6, s*(s - 2)*(s - 3)/2, -s*(s - 1)*(s - 3)/2, s*(s - 1)*(s - 2)/6]
    return sum(wi*vals[j + i] for i, wi in enumerate(w))

def _v41_basis(m):
    """The Lagrange basis polynomials on the nodes 0, 1, ..., m - 1, as coefficient lists in ascending powers."""
    out = []
    for i in range(m):
        c = [1.0]; den = 1.0
        for j in range(m):
            if j != i: c = [(c[n - 1] if n else 0.0) - j*(c[n] if n < len(c) else 0.0) for n in range(len(c) + 1)]; den *= i - j
        out.append([x/den for x in c])
    return out

_V41_LPB = _v41_basis(8)

def _v41_lp(vals, lg):
    """The eight-point interpolating polynomial in ln(R/ell) through the grid values nearest lg (centered where the grid allows): its value
    and its first and second derivatives in ln R."""
    D = _V41_LG[1] - _V41_LG[0]; t = (lg - _V41_LG[0])/D; j = min(max(int(math.floor(t)) - 3, 0), len(vals) - 8); s = t - j
    v = d1 = d2 = 0.0
    for i, c in enumerate(_V41_LPB):
        a = b = e = 0.0
        for n in range(len(c) - 1, -1, -1): e = e*s + 2*b; b = b*s + a; a = a*s + c[n]
        v += vals[j + i]*a; d1 += vals[j + i]*b; d2 += vals[j + i]*e
    return v, d1/D, d2/(D*D)

def _v41_bisect(f, a, b, it=60):
    """A root of f in [a, b], where f changes sign, by bisection."""
    fa = f(a)
    for _ in range(it):
        m = 0.5*(a + b); fm = f(m)
        if (fm > 0) == (fa > 0): a, fa = m, fm
        else: b = m
    return 0.5*(a + b)

def _v41_extrema(vals):
    """The interior extrema of the grid values vals, each where the eight-point polynomial's slope vanishes between the grid's neighbors of a
    grid extremum: (R/ell, the polynomial's value there, +1 for a maximum or -1 for a minimum)."""
    out = []
    for j in range(1, len(vals) - 1):
        if (vals[j] - vals[j - 1])*(vals[j + 1] - vals[j]) >= 0 or vals[j] == vals[j - 1]: continue
        g = lambda s: _v41_lp(vals, s)[1]; a, b = _V41_LG[j - 1], _V41_LG[j + 1]
        if (g(a) > 0) == (g(_V41_LG[j]) > 0): a = _V41_LG[j]
        else: b = _V41_LG[j]
        s = _v41_bisect(g, a, b); out.append((math.exp(s), _v41_lp(vals, s)[0], 1 if vals[j] > vals[j - 1] else -1))
    return out

def _v41_crossings(vals, level=0.0):
    """The radii R/ell where the eight-point polynomial through vals crosses level, one for each change of side between grid neighbors."""
    return [math.exp(_v41_bisect(lambda s: _v41_lp(vals, s)[0] - level, _V41_LG[j - 1], _V41_LG[j])) for j in range(1, len(vals))
            if (vals[j] > level) != (vals[j - 1] > level)]

def _v41_u_at(k, X, which='u'):
    """v^2 ell/(G M) at R/ell = X, interpolated."""
    return _v41_interp(_v41_curves(k)[which], math.log(X))

def _v41_u_direct(k, X, nphi=_V41_NPHI):
    """v^2 ell/(G M) at R/ell = X by v40.0's solver itself, with nphi azimuths, for the controls."""
    S, brk = _v40_sin_source(k); return _v41_at_nphi(nphi, lambda: _v40_disk_v2(S, 1.0, 1.0/_V40_GK, [math.atan(X)], brk)[0])

def _v41_mass(k, chi):
    """int_0^chi e^(-k sin c) sin c dc by 32-node Gauss-Legendre pieces between the breaks _V41_BRK."""
    e = sorted(set([0.0, chi] + [p for p in _V41_BRK if p < chi])); tot = 0.0
    for a, b in zip(e[:-1], e[1:]):
        for t, w in _v40_graded(a, b, False, False): tot += w*math.exp(-k*math.sin(t))*math.sin(t)
    return tot

def _v41_half(k):
    """The image's half-mass radius over ell -- the leaf's mass within chi is the image's within ell tan chi -- by Newton's iteration."""
    half = _v41_mass(k, math.pi/2)/2; c = min(math.atan(_V41_RHALF_EXP/k), math.pi/3)
    for _ in range(60):
        dc = (_v41_mass(k, c) - half)/(math.exp(-k*math.sin(c))*math.sin(c)); c = min(max(c - dc, 0.5*c), 0.5*(c + math.pi/2))
        if abs(dc) < 1e-15: break
    return math.tan(c)

def _v41_k_of_half(rh):
    """The k whose image has half-mass radius rh ell (rh below sqrt(3), the uniform leaf's), by bisection in ln k."""
    lo, hi = math.log(1e-4), math.log(1e4)
    for _ in range(100):
        mid = 0.5*(lo + hi)
        if _v41_half(math.exp(mid)) > rh: lo = mid
        else: hi = mid
    return math.exp(0.5*(lo + hi))

_V41_RHALF_EXP = 1.6783469900166605                     # (1 + y) e^(-y) = 1/2: the exponential disk's half-mass radius over h

def _v41_prominent(v, thr):
    """Indices of local maxima of v whose topographic prominence exceeds thr times the size of the value there."""
    out = []
    for i in range(1, len(v) - 1):
        if not (v[i] > v[i - 1] and v[i] >= v[i + 1]): continue
        l = i
        while l > 0 and v[l - 1] <= v[i]: l -= 1
        r = i
        while r < len(v) - 1 and v[r + 1] <= v[i]: r += 1
        base = max(min(v[l:i + 1]), min(v[i:r + 1]))
        if v[i] - base > thr*abs(v[i]): out.append(i)
    return out

_V41_HALOS = (("NFW", lambda y: (math.log(1 + y) - y/(1 + y))/y, lambda y: 1/(y*(1 + y)**2)),
              ("Burkert", lambda y: (math.log(1 + y) + 0.5*math.log(1 + y*y) - math.atan(y))/y, lambda y: 1/((1 + y)*(1 + y*y))),
              ("pseudo-isothermal", lambda y: 1 - math.atan(y)/y, lambda y: 1/(1 + y*y)))

def _v41_golden(f, a, b, n=60):
    """The minimum of a unimodal f on [a, b] by golden-section search: (f, x)."""
    g = (math.sqrt(5) - 1)/2; c, d = b - g*(b - a), a + g*(b - a); fc, fd = f(c), f(d)
    for _ in range(n):
        if fc < fd: b, d, fd = d, c, fc; c = b - g*(b - a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a + g*(b - a); fd = f(d)
    x = 0.5*(a + b); return f(x), x

def _v41_scan(f, lo, hi, n=41, it=60):
    """A grid of n points on [lo, hi], then golden-section between the neighbors of the grid's minimum: (f, x, at an end of the grid)."""
    xs = [lo + (hi - lo)*i/(n - 1) for i in range(n)]; fs = [f(x) for x in xs]; i = min(range(n), key=lambda j: fs[j])
    fv, x = _v41_golden(f, xs[max(i - 1, 0)], xs[min(i + 1, n - 1)], it)
    return (fv, x, i in (0, n - 1)) if fv <= fs[i] else (fs[i], xs[i], i in (0, n - 1))

def _v41_fit(Rs, v2, a, f, sig=0.03, ups=None):
    """Least squares in v, with errors sig*v, of v_model^2 = Ups a + V^2 f(R/r_s) to v^2 at the radii Rs: Ups >= 0 free (or fixed),
    V^2 >= 0 and r_s free.  For a mixing w in [0, 1] the model is A [(1 - w) a/a_bar + w f/f_bar], whose best sqrt(A) is closed-form; w and
    ln r_s by grids and golden sections.  Returns (chi^2/N, rms of v_model/v - 1, the largest |v_model/v - 1|, Ups, V^2, r_s, r_s at a grid's
    end)."""
    vs = [math.sqrt(x) for x in v2]; N = len(Rs)
    def amp(g):
        q = [math.sqrt(max(gi, 0.0))/vi for gi, vi in zip(g, vs)]; s = sum(q)/sum(qi*qi for qi in q)
        return s, sum((s*qi - 1)**2 for qi in q)/sig**2
    def inner(lrs):
        fy = [f(R/math.exp(lrs)) for R in Rs]
        if ups is None:
            ab, fb = sum(a)/N, sum(fy)/N
            def h(w):
                return amp([(1 - w)*ai/ab + w*fi/fb for ai, fi in zip(a, fy)])[1]
            c2, w = _v41_scan(h, 0.0, 1.0, 21, 50)[:2]
            s, c2 = amp([(1 - w)*ai/ab + w*fi/fb for ai, fi in zip(a, fy)]); A = s*s
            return c2, A*(1 - w)/ab, A*w/fb
        fb = sum(fy)/N; vmax = max(x/fi for x, fi in zip(v2, fy))
        def h(t):
            V2 = t*vmax; return sum((math.sqrt(max(ups*ai + V2*fi, 0.0))/vi - 1)**2 for ai, fi, vi in zip(a, fy, vs))/sig**2
        c2, t = _v41_scan(h, 0.0, 2.0, 41, 50)[:2]
        return c2, ups, t*vmax
    lo, hi = math.log(min(Rs)/30), math.log(max(Rs)*300)
    c2, lrs, edge = _v41_scan(lambda t: inner(t)[0], lo, hi, 41, 50)
    c2, U, V2 = inner(lrs); rs = math.exp(lrs)
    dev = [math.sqrt(max(U*ai + V2*f(R/rs), 0.0))/vi - 1 for R, ai, vi in zip(Rs, a, vs)]
    return c2/N, math.sqrt(sum(d*d for d in dev)/N), max(abs(d) for d in dev), U, V2, rs, edge

def _v41_u_fast(k, X):
    """v^2 ell/(G M) at R/ell = X for e^(-k sin chi), from the four grid points around X only."""
    pts, eq, nrm = _v41_grid(); nk = _v41_ndot(nrm, k); lg = math.log(X)
    t = (lg - _V41_LG[0])/(_V41_LG[1] - _V41_LG[0]); j = min(max(int(math.floor(t)) - 1, 0), _V41_NJ - 4); s = t - j
    w = [-(s - 1)*(s - 2)*(s - 3)/6, s*(s - 2)*(s - 3)/2, -s*(s - 1)*(s - 3)/2, s*(s - 1)*(s - 2)/6]
    tot = 0.0
    for i, wi in enumerate(w):
        x, dh, rm, rp = pts[j + i][:4]; tot += wi*(-2*math.tan(x)*(_v41_dot(rp, k) - _v41_dot(rm, k))/(2*dh)/nk)
    return tot

# SPARC (Lelli, McGaugh & Schombert 2016, AJ 152, 157), the Rotmod_LTG files as the frozen pg_v36_numerics.py embeds them: R [kpc], Vobs,
# errV [km/s]; the baryonic masses and arena leaves of v36.0-4 (Section XXXIII.5).
_V41_DWARFS = (
    ("DDO 154", 3.90e8, 2.02,
     ((0.49, 13.80, 1.60), (0.99, 21.60, 0.80), (1.48, 28.90, 0.70), (1.97, 34.30, 0.50), (2.47, 38.20, 0.40), (2.96, 42.00, 0.20),
      (3.46, 44.60, 0.20), (3.95, 46.30, 0.20), (4.44, 47.40, 0.30), (4.94, 48.20, 0.60), (5.43, 47.40, 0.70), (5.92, 45.50, 1.30))),
    ("IC 2574", 1.95e9, 4.51,
     ((0.85, 10.30, 0.20), (1.14, 12.90, 2.70), (1.42, 16.40, 1.80), (1.71, 18.60, 2.10), (1.99, 19.80, 2.00), (2.28, 26.10, 0.60),
      (2.55, 27.70, 2.70), (2.84, 29.70, 2.60), (3.13, 33.00, 3.40), (3.41, 34.80, 1.20), (3.70, 35.00, 0.90), (3.98, 39.00, 10.20),
      (4.26, 35.90, 5.40), (4.55, 40.00, 4.10), (4.84, 38.70, 1.40), (5.12, 41.80, 0.50), (5.41, 42.90, 0.40), (5.68, 44.40, 1.70),
      (5.97, 46.10, 1.30), (6.26, 49.00, 0.90), (6.54, 51.90, 0.60), (6.83, 53.10, 2.10), (7.10, 54.00, 0.50), (7.39, 55.90, 1.10),
      (7.68, 58.80, 3.60), (7.96, 57.30, 4.60), (8.25, 54.00, 9.00), (8.52, 63.80, 12.00), (8.81, 60.50, 6.20), (9.10, 61.00, 5.70),
      (9.38, 66.00, 1.30), (9.67, 65.20, 3.40), (9.96, 67.10, 4.70), (10.23, 67.50, 9.30))))

def _v41_chi2(data, M, ell, k, floor=0.0, amp=False):
    """chi^2/N of the leaf's curve for e^(-k sin chi) with mass M on a leaf ell against (R, V, err), the errors floored at floor; with
    amp, v^2 times a free factor f, its best sqrt(f) closed-form: (chi^2/N, f, the model speeds)."""
    c = _v41_curves(k, False)['u']; GM = _V40_GK*M
    vm = [math.sqrt(max(GM/ell*_v41_interp(c, math.log(R/ell)), 0.0)) for R, V, e in data]
    er = [max(e, floor) for R, V, e in data]; f = 1.0
    if amp:
        s = sum(m*V/x**2 for m, (R, V, e), x in zip(vm, data, er))/sum((m/x)**2 for m, x in zip(vm, er)); f = s*s; vm = [s*m for m in vm]
    return sum(((m - V)/x)**2 for m, (R, V, e), x in zip(vm, data, er))/len(data), f, vm

# Eilers, Hogg, Rix & Ness 2019 (ApJ 871, 120), Table 1 as the frozen pg_v36_numerics.py embeds it: R [kpc], v_c, sigma-, sigma+ [km/s]; their
# adopted R_sun = 8.122 kpc (GRAVITY 2018) and published line v_c = 229.0 - 1.7 (R - R_sun) km/s over 5-25 kpc.
_V41_EILERS = ((5.27, 226.83, 1.91, 1.90), (5.74, 230.80, 1.43, 1.35), (6.23, 231.20, 1.70, 1.10), (6.73, 229.88, 1.44, 1.32),
               (7.22, 229.61, 1.37, 1.11), (7.82, 229.91, 0.92, 0.88), (8.19, 228.86, 0.80, 0.67), (8.78, 226.50, 1.07, 0.95),
               (9.27, 226.20, 0.72, 0.62), (9.76, 225.94, 0.42, 0.52), (10.26, 225.68, 0.44, 0.40), (10.75, 224.73, 0.38, 0.41),
               (11.25, 224.02, 0.33, 0.54), (11.75, 223.86, 0.40, 0.39), (12.25, 222.23, 0.51, 0.37), (12.74, 220.77, 0.54, 0.46),
               (13.23, 220.92, 0.57, 0.40), (13.74, 217.47, 0.64, 0.51), (14.24, 217.31, 0.77, 0.66), (14.74, 217.60, 0.65, 0.68),
               (15.22, 217.07, 1.06, 0.80), (15.74, 217.38, 0.84, 1.07), (16.24, 216.14, 1.20, 1.48), (16.74, 212.52, 1.39, 1.43),
               (17.25, 216.41, 1.44, 1.85), (17.75, 213.70, 2.22, 1.65), (18.24, 207.89, 1.76, 1.88), (18.74, 209.60, 2.31, 2.77),
               (19.22, 206.45, 2.54, 2.36), (19.71, 201.91, 2.99, 2.26), (20.27, 199.84, 3.15, 2.89), (20.78, 198.14, 3.33, 3.37),
               (21.24, 195.30, 5.99, 6.50), (21.80, 213.67, 15.38, 12.18), (22.14, 176.97, 28.58, 18.57), (22.73, 193.11, 27.64, 19.05),
               (23.66, 176.63, 18.67, 16.74), (24.82, 198.42, 6.50, 6.12))
_V41_RSUN = 8.122

def _v41_uniform_force(X, nphi):
    """v40.0's solver's v^2 ell/(G M) at R/ell = X for a uniform leaf, which exerts no force in the plane, with nphi azimuths in the bounded
    remainder of its ring kernel (64 in v40.0)."""
    return _v41_at_nphi(nphi, lambda: _v40_disk_v2(lambda t: 1.0, 1.0, 1.0/_V40_GK, [math.atan(X)], [])[0])

_V41_SCAN = (0.01, 0.03, 0.1, 0.3, 0.5, 1.0, 2.0, 3.2, 16/3, 6.0, 7.0, 8.0, 12.0, 16.0, 32.0, 64.0, 100.0)

def _v41_shape(k):
    """The curve's shape for e^(-k sin chi) on the common grid: the interior maxima and minima (where the eight-point polynomial's slope
    vanishes), the image's half-mass radius and h_eff = R_half/1.678 (h for an exponential disk), Section XXXIII.23's overshoot B over 0.03-12
    h_eff against v(12 h_eff), v(40 h_eff)/v_inf, and the first radius where v = 0.9 v_inf (where the polynomial crosses it)."""
    c = _v41_curves(k); vinf = math.sqrt(c['C'])
    ex = [(X, math.sqrt(max(q, 0.0))/vinf, t) for X, q, t in _v41_extrema(c['u'])]
    mx = [(X, q) for X, q, t in ex if t > 0]; mn = [(X, q) for X, q, t in ex if t < 0]
    rh = _v41_half(k); he = rh/_V41_RHALF_EXP
    xs = [0.03*he*400.0**(i/199) for i in range(200)]; vv = [math.sqrt(max(_v41_interp(c['u'], math.log(x)), 0.0)) for x in xs]
    B = max(vv)/vv[-1] - 1
    r90 = _v41_crossings(c['u'], 0.81*c['C'])[0]
    v40 = math.sqrt(max(_v41_interp(c['u'], math.log(40*he)), 0.0))/vinf
    return dict(c=c, mx=mx, mn=mn, rh=rh, he=he, B=B, r90=r90, v40=v40)

def v40_1_falloff():
    """The follow-up of 20-21 November on Entry 326's falloff (R581).  (a) The scaling v^2 = (G M/ell) u(R/ell; k) with k = ell/h -- ell already in
    the exponent, the profile exponential in the leaf's areal radius -- and the controls of the rows against v40.0's solver.  (b) The scan from
    k = 0.01, a falloff length of 100 ell, to k = 100: the plateau, the far field, the image's scale, the extrema.  (c) The shape classes and
    their boundaries.  (d) The small-k limit.  (e) Entry 322's classes for the eight galaxies of Section XXXIII.23 under two indices."""
    print("\n== v40.1-1. The follow-up of 20-21 November: Entry 326's falloff on a leaf -- one shape for each k = ell/h, the scan from k = 0.01 to "
          "100, the shape classes and their boundaries, the small-k limit, and Entry 322's classes for the eight galaxies (R581) ==")
    _v41_grid()
    # (a) the scaling and the controls
    XS = (0.05, 0.3, 1.0, 3.0)
    ctl = [(k, [_v41_lp(_v41_curves(k)['u'], math.log(X))[0]/_v41_u_direct(k, X) - 1 for X in XS]) for k in (16/3, 100.0)]
    prow = {}
    for X in XS:
        x = math.atan(X); dh = min(1e-4, 0.02*x)
        prow[X] = (x, dh, [_v41_at_nphi(_V41_NPHI, lambda y=y: _v41_row(y)) for y in (x - dh, x + dh)])
    def u_rows(k, X):
        x, dh, (rm, rp) = prow[X]; return -2*math.tan(x)*(_v41_dot(rp, k) - _v41_dot(rm, k))/(2*dh)/_v41_curves(k)['norm']
    pairs = [(k, X, u_rows(k, X)) for k in (0.03, 0.5, 16/3, 100.0) for X in XS]
    itp = max(abs(_v41_u_at(k, X)/u0 - 1) for k, X, u0 in pairs)
    itp8 = max(abs(_v41_lp(_v41_curves(k)['u'], math.log(X))[0]/u0 - 1) for k, X, u0 in pairs)
    unif = [(X, _v41_uniform_force(X, 64)) for X in (0.5, 1.0, 3.0, 30.0)]; unif2 = [_v41_uniform_force(3.0, n) for n in (128, 256)]
    small = [(k, _v41_u_at(k, 3.0)/_v41_u_direct(k, 3.0, 64) - 1, _v41_u_at(k, 3.0)/_v41_u_direct(k, 3.0) - 1) for k in (0.03, 0.5)]
    n0 = _v41_ndot(_v41_grid()[2], 0.0)
    rest = [(k, [u_rows(k, 3.0)/(_v41_u_direct(k, 3.0, n) - math.exp(-k)*n0/_v41_curves(k)['norm']*u1) - 1
                 for n, u1 in ((64, unif[2][1]), (128, unif2[0]), (256, unif2[1]))])
            for k in (0.03, 0.5)]
    GM = _V40_GK*6e10; Cb = _v41_curves(16/3)['C']; vb = [math.sqrt(GM/16*_v41_u_at(16/3, R/16)) for R in (5, 8, 16, 24, 36, 60)]
    _v40_wrap("(a) The scaling [T/V].  Entry 326's profile e^(-k sin chi), k = ell/h, is the exponential e^(-rho/h) in the leaf's areal radius rho = "
              "ell sin chi -- in gnomonic radius rho = R/sqrt(1 + R^2/ell^2) -- so ell already stands in the exponent; the source depends on chi through "
              "k alone, and v^2(R) = (G M/ell) u(R/ell; k): k sets the shape, the leaf the radial unit and the amplitude G M/ell [T].  The computation: "
              f"v40.0's solver through kernel rows computed once, at the two points chi -/+ dh of v40.0's centered difference around each of {_V41_NJ} "
              f"grid points tan chi = 10^(-3.7 + j/25), to R = {math.exp(_V41_LG[-1]):.0f} ell, with the panel breaks 0.0025 x 2^m (m = 0-9) for every source, "
              f"{_V41_NPHI} azimuths in the ring kernel's bounded remainder (v40.0's solver takes 64), and the source less its "
              "equatorial value e^(-k) -- a uniform density on the leaf's great sphere, invariant under its rotations, has a constant potential "
              "there and exerts no force in the plane [T].  Against v40.0's solver itself with the same azimuths, at R/ell = 0.05, 0.3, 1, 3 "
              "(the eight-point polynomial between grid points), the relative differences in v^2 are at most "
              + " and ".join(f"{max(abs(d) for d in ds):.1e} for k = {_v40_f(k, 3)}" for k, ds in ctl)
              + ".  v40.0's own error, its 64-point azimuthal rule's, shows for a uniform leaf, which exerts no force: its v^2 "
              "ell/(G M) is " + ", ".join(f"{u_:.2e} at R/ell = {X:g}" for X, u_ in unif) + f", and at R/ell = 3 {unif2[0]:.2e} with 128 azimuths and "
              f"{unif2[1]:.2e} with 256, falling as the inverse cube; for broad sources v40.0's solver, which keeps the uniform part, differs "
              "from the rows at R/ell = 3, relatively, by " + ", ".join(f"{d:+.1e} at k = {k:g}" for k, d, d2 in small) + " with its 64 azimuths and by "
              + ", ".join(f"{d2:+.1e}" for k, d, d2 in small) + " with 256 -- that part's error, which the subtraction removes.  With that part "
              "taken from the solver's own result too, the rows and the solver differ relatively on the rest of the source by " + ", ".join(
              f"{a:+.1e} with 64 azimuths and {b:+.1e} with 128 at k = {k:g}" for k, (a, b, c_) in rest) + " -- the solver's rule's error there "
              "less the rows' own, which the inverse cube puts at 1/64 and 1/8 of it, so that the rows' own is a seventh of the difference at "
              "128, " + " and ".join(f"{b/7:.1e}" for k, (a, b, c_) in rest) + " -- and by "
              + ("less than 1e-09" if all(abs(c_) < 1e-9 for k, (a, b, c_) in rest) else " and ".join(f"{c_:+.1e}" for k, (a, b, c_) in rest))
              + " with 256 in both.  "
              f"The interpolation against rows at the point itself: at most {itp:.1e} (four points), {itp8:.1e} (the "
              f"eight-point polynomial).  On ell = 16 kpc with h = 3 kpc and 6e10 Msun, v40.0-8(d)'s plateau coefficient C = 2.6434 and "
              f"curve 178.7, 194.1, 201.1, 203.0, 204.5, 205.7 km/s at 5, 8, 16, 24, 36, 60 kpc: C = {Cb:.6f}, " + ", ".join(f"{x:.2f}" for x in vb)
              + " km/s.")
    # (b) the scan
    rows = [(k, _v41_shape(k)) for k in _V41_SCAN]
    _v40_wrap("(b) The scan [V].  For each k: the plateau coefficient C = v_inf^2 ell/(G M) and C/k; the far field v^2 = v_inf^2 [1 + A (ell/R)^2 "
              "+ ...], A = psi''''/(6 psi'') - 1/3 at the equator; the image's half-mass radius R_half/ell and its scale h_eff = R_half/1.678 over h "
              "(h for an exponential disk); the curve's interior maxima and minima (R/h_eff, R/ell, v/v_inf); the radius where v first reaches 0.9 "
              "v_inf; Section XXXIII.23's overshoot B over 0.03-12 h_eff against v(12 h_eff); v(40 h_eff)/v_inf:")
    for k, s in rows:
        c = s['c']; ext = "; ".join([f"max at {R/s['he']:.2f} h_eff = {R:.4f} ell, v/v_inf = {q:.4f}" for R, q in s['mx']]
                                    + [f"min at {R/s['he']:.2f} h_eff = {R:.4f} ell, v/v_inf = {q:.4f}" for R, q in s['mn']]) or "none"
        _v40_wrap(f"k = {_v40_f(k, 3)}: C = {c['C']:.6f}, C/k = {c['C']/k:.5f}, A = {c['A']:+.4f}; R_half = {s['rh']:.4f} ell, h_eff = "
                  f"{s['he']*k:.4f} h; extrema: {ext}; v = 0.9 v_inf at {s['r90']/s['he']:.3f} h_eff = {s['r90']:.4f} ell; B = {s['B']:+.4f}; "
                  f"v(40 h_eff)/v_inf = {s['v40']:.4f}", first="       ", rest="         ")
    # (c) the classes
    def gmin(k):
        u = _v41_curves(k)['u']; return _v41_golden(lambda s: _v41_lp(u, s)[1], math.log(0.5), math.log(1.5), 60)
    def over(k):
        m = _v41_shape(k)['mx']; return max(q for R, q in m) - 1 if m else -1.0
    kw = _v41_root(lambda k: gmin(k)[0], 5.6, 6.2); gw = gmin(kw); cw = _v41_curves(kw)
    xw, vw = math.exp(gw[1]), math.sqrt(_v41_lp(cw['u'], gw[1])[0]/cw['C'])
    kb = _v41_root(over, 6.2, 6.8); xb = _v41_shape(kb)['mx'][0][0]
    Aall = max(s['c']['A'] for k, s in rows); Amax, kA = _v41_golden(lambda k: -_v41_curves(k)['A'], 6.0, 8.0, 40); Amax = -Amax
    A0 = _v41_curves(1e-4)['A']
    pk = [(k, s['mx'][0]) for k, s in rows if s['mx'] and k >= 7]
    mn7 = [s['mn'][0][0] for k, s in rows if s['mn'] and k >= 7]; deg = lambda X: math.degrees(math.atan(X))
    _v40_wrap(f"(c) The classes [V].  Below k_w = {kw:.4f} the curve rises to its plateau without an interior extremum; at k_w a stationary "
              f"inflection appears below the plateau (at R = {xw:.4f} ell, v/v_inf = {vw:.4f}) and for larger k a maximum and a minimum, and from "
              f"k_b = {kb:.4f} the maximum stands above the plateau (it crosses v_inf at R = {xb:.4f} ell) -- k_w where the least slope of v^2 in "
              "0.5-1.5 ell vanishes and k_b where the maximum reaches v_inf, both by the false position on the eight-point polynomial: a monotonic "
              "rise, a wiggle below the plateau and a bump above it, the three regimes Section XXXIII.23(b) found for Part XXV's spheres; the "
              f"benchmark's k = 16/3 lies in the first.  A is negative for every k: at most {Aall:+.4f} among the scan's k and {Amax:+.4f} over all, "
              f"near k = {kA:.2f}, tending to {A0:+.4f} at k = 1e-4 and to -1/6, the point source's (Section XXXI.38(a)), as k grows.  So the "
              "plateau is approached from below at large R in every class, and the equator, the plateau's endpoint, is a maximum of the far curve, "
              "not a low point; above k_w the curve falls from its maximum -- past the plateau from k_b -- to a minimum near R = ell, at "
              f"{min(mn7):.4f}-{max(mn7):.4f} ell (chi = {deg(min(mn7)):.1f}-{deg(max(mn7)):.1f} degrees) for k = 7-100, and rises to the plateau "
              "again.  On a fixed leaf a quicker falloff -- a larger k -- puts the bump earlier and higher: " + ", ".join(
              f"k = {k:g}: {R:.4f} ell ({R/_v41_shape(k)['he']:.2f} h_eff), {q:.4f} v_inf" for k, (R, q) in pk) + ".  v40.0-8(d)'s statement that "
              "the leaves that make the image exponential lose the flat curve is corrected here: those leaves, ell = 32, 48 and 96 kpc with h = 3 "
              "kpc, have k = 10.67, 16 and 32, in the bump class, with a plateau below the frozen leaf's.")
    # (d) small k
    sk = [(k, _v41_curves(k)['C']/k) for k in (0.001, 0.002, 0.005)]; lim = 2*sk[0][1] - sk[1][1]
    s01 = _v41_shape(0.01); rhu = _v41_half(1e-4)
    _v40_wrap(f"(d) The small-k limit [V].  C/k = " + ", ".join(f"{c_:.7f} at k = {k:g}" for k, c_ in sk) + f", linear in k (the line through "
              f"the first two gives {sk[0][1] + (sk[1][1] - sk[0][1])*4:.7f} at k = 0.005), toward {lim:.5f}: for a slow falloff v_inf^2 -> "
              f"{lim:.4f} G M/h, set by the falloff length and not by the leaf; the source tends to the uniform leaf, whose image (1 + R^2/ell^2)^(-3/2) "
              f"has R_half = sqrt(3) ell = {math.sqrt(3):.4f} ell ({rhu:.4f} ell at k = 1e-4), so that the light too takes the leaf's scale.  The "
              f"falloff length 1/0.01 = 100 ell: R_half = {s01['rh']:.4f} ell, v reaches 0.9 v_inf at {s01['r90']:.4f} ell, and v_inf = "
              f"{math.sqrt(s01['c']['C']/3):.4f} of the point source's plateau speed sqrt(3 G M/ell).")
    # (e) Entry 322's classes for the eight galaxies
    GAL = (("DDO 154", 0.37, 2.02, 0.49, 5.92, 1.68, "no overshoot"), ("IC 2574", 2.78, 4.51, 0.85, 10.23, 1.58, "no overshoot"),
           ("NGC 2403", 1.39, 9.85, 0.16, 20.87, 0.42, "no overshoot"), ("NGC 3198", 3.14, 18.69, 0.32, 44.08, 0.51, "no overshoot"),
           ("NGC 6503", 2.16, 9.44, 0.76, 23.50, 0.24, "no overshoot"), ("NGC 2841", 3.64, 34.37, 3.44, 63.64, 0.16, "bump"),
           ("UGC 2885", 11.40, 52.85, 1.70, 74.07, 0.29, "no overshoot"), ("NGC 7814", 2.54, 22.62, 0.63, 19.53, 0.07, "declining"))
    def klass(k, x1, x2, n=50):
        c = _v41_curves(k)['u']; xs = [x1*(x2/x1)**(i/(n - 1)) for i in range(n)]
        v = [math.sqrt(max(_v41_interp(c, math.log(x)), 0.0)) for x in xs]; B = max(v)/v[-1] - 1; i = max(range(n), key=lambda j: v[j])
        ext = len(_v41_prominent(v, 0.005)) + len(_v41_prominent([-a for a in v], 0.005))
        return B, ext, "no overshoot" if B <= 0.02 else ("declining" if i == 0 else "bump")
    cls = []
    for nm, Rd, L, R1, R2, rh, obs in GAL:
        k1 = L/Rd; k2 = _v41_k_of_half(rh); cls.append((nm, k1, klass(k1, R1/L, R2/L), k2, klass(k2, R1/L, R2/L), obs))
    ex = lambda n: f"{n} extrem{'um' if n == 1 else 'a'}"
    ag1 = sum(1 for r in cls if r[2][2] == r[5]); ag2 = sum(1 for r in cls if r[4][2] == r[5]); base = sum(1 for r in cls if r[5] == "no overshoot")
    _v40_wrap("(e) Entry 322's classes for the eight galaxies [V/O].  Section XXXIII.23 sorted the pilot's eight curves by shape and found no "
              "monotonic member in the gnomonic disk family; here the whole source is Entry 326's profile on each galaxy's arena leaf (Section "
              "XXXIII.5's ell), with no free parameter, its k from either of two indices -- (i) the stellar disk, k = ell/R_disk (SPARC's R_disk), "
              "(ii) the whole source's breadth, the k whose image has Section XXXIII.23(d)'s R_half/ell -- and the curve read over the galaxy's own "
              "measured radii against v(R_last), with Section XXXIII.23(a)'s and (d)'s rules for model curves (no overshoot for B <= 2%, a maximum at "
              "the first "
              "radius a declining curve; extrema at 0.5% prominence): " + "; ".join(
              f"{nm}: (i) k = {k1:.2f}, B = {b1[0]:+.3f}, {ex(b1[1])}, {b1[2]}; (ii) k = {k2:.3f}, B = {b2[0]:+.3f}, {ex(b2[1])}, {b2[2]}; "
              f"observed {obs}" for nm, k1, b1, k2, b2, obs in cls) + f".  Agreement: {ag1} of 8 under (i), {ag2} of 8 under (ii) -- and {base} of 8 "
              "for a rule that calls every curve 'no overshoot': with this sample the indices do not yet carry information beyond the base rate; the "
              "bump of NGC 2841 is the one feature both reproduce, and both make NGC 7814's maximum a bump inside its range where the data decline "
              "from the first radius.")
    ok = (round(Cb, 4) == 2.6434 and abs(Cb - 2.643445) < 3e-6 and all(abs(a_ - b_) < 0.05 for a_, b_ in zip(vb, (178.7, 194.1, 201.1, 203.0, 204.5, 205.7)))
          and all(abs(d) < 1e-6 for k, ds in ctl for d in ds) and itp < 1e-5 and itp8 < 1e-7 and 6 < unif[2][1]/unif2[0] < 10 and 6 < unif2[0]/unif2[1] < 10
          and abs(lim - 0.7294796) < 3e-6 and abs(sk[0][1] - 0.7294635) < 3e-6 and Aall < 0 and Amax < 0 and abs(kw - 5.989) < 1e-3 and abs(kb - 6.503) < 1e-3
          and all(6 < a/b < 10 and abs(c_) < 1e-8 for k, (a, b, c_) in rest)
          and all(not s['mx'] for k, s in rows if k <= 16/3) and all(s['mx'] and s['mx'][0][1] > 1 for k, s in rows if k >= 7)
          and all(pk[i + 1][1][0] < pk[i][1][0] and pk[i + 1][1][1] > pk[i][1][1] for i in range(len(pk) - 1)) and (ag1, ag2, base) == (6, 6, 6))
    check(ok, "v40.1-1: e^(-k sin chi) with k = ell/h gives v^2 = (G M/ell) u(R/ell; k); the rows reproduce v40.0's solver and C = 2.6434; the "
              "classes: monotonic below k_w = 5.989, a wiggle, a bump above v_inf from k_b = 6.503; A < 0 for every k; C/k -> 0.7295 for slow falloffs")

_V41_NK = (0.01, 0.1, 0.5, 1.0, 2.0, 3.2, 16/3, 8.0, 16.0, 32.0, 100.0)

def v40_1_newton():
    """The Newtonian reading of the leaf's curve (R582, (a)-(e)).  (a) The flat thin-disk solver for the image, against Freeman's disk.  (b) The
    driven remainder v_d^2 = v^2 - v_N^2, the leaf's curve less the image's own Newtonian curve: its share, its sign, no maximum; the bump the
    image's own.  (c) Its spherical-equivalent density (1/(4 pi G R^2)) d(R v_d^2)/dR: the slopes, the depressed center, the outer -2.
    (d) Decompositions of the leaf's curve as Ups v_N^2 + a halo of the three families, with 3% errors over 0.5-10 h_eff, and fits of the
    families to the remainder alone.  (e) The point source's remainder, (5/2) G M R/ell^2 near the center."""
    print("\n== v40.1-2. The Newtonian reading: the image's own thin disk, the driven remainder and its density, and the halo families (R582) ==")
    _v41_grid(); D = _V41_LG[1] - _V41_LG[0]
    # (a) Freeman
    fr = []
    for R in (0.3, 1.0, 2.2, 5.0, 12.0):
        c0 = math.atan(R); dh = min(1e-4, 0.02*c0); R1, R2 = math.tan(c0 - dh), math.tan(c0 + dh)
        f = lambda row: sum(c*math.exp(-math.tan(t))/(2*math.pi) for t, c in zip(*row))
        v2 = R*(f(_v41_nrow(R2)) - f(_v41_nrow(R1)))/(R2 - R1); y = R/2
        vf = 2*y*y*(_v40_bessel(0, y, 'I')*_v40_bessel(0, y, 'K') - _v40_bessel(1, y, 'I')*_v40_bessel(1, y, 'K')); fr.append((R, v2/vf - 1))
    _v40_wrap("(a) The image's own Newtonian curve [V].  The image Sigma_vis = Sigma_leaf cos^3 chi at R' = ell tan chi in a flat plane, its potential "
              "-4 G int Sigma(R') R' K(m)/(R + R') dR' with m = 4 R R'/(R + R')^2 (K by the arithmetic-geometric mean) over R' = ell tan t on the rows' "
              "panels, and v_N^2 = R dPhi/dR by the same centered difference in chi.  Against Freeman's exponential disk, v^2 = 2 (G M/h) y^2 [I0 K0 - "
              "I1 K1](y), y = R/2h, at R = " + ", ".join(f"{R:g}" for R, d in fr) + " h: " + ", ".join(f"{d:+.1e}" for R, d in fr) + ".")
    # (b) the driven remainder
    out = []
    for k in _V41_NK:
        c = _v41_curves(k); he = _v41_half(k)/_V41_RHALF_EXP; u, un = c['u'], c['un']; ud = [a - b for a, b in zip(u, un)]
        at = lambda arr, f: _v41_lp(arr, math.log(f*he))[0]
        share = [at(ud, f)/at(u, f) for f in (0.5, 1, 2, 5, 10)]
        zr = [X/he for X in _v41_crossings(ud)]
        dmax = [e for e in _v41_extrema(ud) if e[2] > 0]
        jn = max(range(len(un)), key=lambda j: un[j]); fN, sN = _v41_golden(lambda s: -_v41_lp(un, s)[0], _V41_LG[jn - 1], _V41_LG[jn + 1], 60)
        X = [math.exp(l) for l in _V41_LG]; m = [x*d for x, d in zip(X, ud)]
        rho = lambda s, m=m: math.exp(-3*s)*_v41_lp(m, s)[1]/(4*math.pi)
        def slope(f, m=m, he=he):
            w, w1, w2 = _v41_lp(m, math.log(f*he)); return None if w1 <= 0 else -3 + w2/w1
        sl = [slope(f) for f in (0.5, 1, 2, 5, 10, 30)]
        w1g = [_v41_lp(m, l)[1] for l in _V41_LG]
        rz = [math.exp(_v41_bisect(lambda s, m=m: _v41_lp(m, s)[1], _V41_LG[j - 1], _V41_LG[j]))/he for j in range(1, len(w1g))
              if (w1g[j] > 0) != (w1g[j - 1] > 0)]
        jr = max(range(1, len(w1g) - 1), key=lambda j: math.exp(-3*_V41_LG[j])*w1g[j])
        fr_, sr = _v41_golden(lambda s: -rho(s), _V41_LG[jr - 1], _V41_LG[jr + 1], 60)
        core = [rho(math.log(f*he))/(-fr_) for f in (0.01, 0.03, 0.1, 0.3, 0.5)] if k in (16/3, 8.0, 16.0) else None
        out.append(dict(k=k, he=he, share=share, neg=ud[0] < 0, zr=zr, dmax=dmax, vn=(math.exp(sN)/he, math.sqrt(-fN/c['C'])), sl=sl, rz=rz,
                        rmax=math.exp(sr)/he, core=core, c=c))
    _v40_wrap("(b) The driven remainder [V].  The leaf's curve less the image's own Newtonian curve, v_d^2 = v^2 - v_N^2 with the image's whole "
              "mass (Ups = 1), as the share v_d^2/v^2 at R = 0.5, 1, 2, 5, 10 h_eff; where v_d^2 < 0; the image's Newtonian maximum (R/h_eff, "
              "v_N/v_inf): " + "; ".join(f"k = {_v40_f(o['k'], 3)}: " + ", ".join(f"{x:+.3f}" for x in o['share'])
              + (f", negative inside {o['zr'][-1]:.4g} h_eff" if o['neg'] else ", positive throughout")
              + f", v_N peaking at {o['vn'][0]:.2f} h_eff with {o['vn'][1]:.3f} v_inf" for o in out) + ".  The remainder has no interior maximum "
              "for any of these k: it rises to v_inf^2 without a bump of its own, so that the bump of the larger k is the image's own disk, whose "
              "Newtonian curve peaks near Freeman's 2.15 h; for k <= 3.2 the leaf pulls less than the image's own Newtonian gravity inside a radius "
              "that grows as k falls, and for a slow falloff nearly everywhere -- at k = 0.01 the image's Newtonian v^2 is "
              f"{1 - out[0]['share'][0]:.1f} times the leaf's at 0.5 h_eff.")
    cores = [o for o in out if o['core']]
    _v40_wrap("(c) The driven density [V].  Its spherical equivalent rho_d = (1/(4 pi G R^2)) d(R v_d^2)/dR, from the eight-point polynomial "
              "through R v_d^2: its logarithmic slope at R = 0.5, 1, 2, 5, 10, 30 h_eff (n/a where rho_d <= 0), where it is negative, and the "
              "radius of its maximum: " + "; ".join(f"k = {_v40_f(o['k'], 3)}: " + ", ".join("n/a" if s is None else f"{s:+.2f}" for s in o['sl'])
              + (f", negative inside {o['rz'][-1]:.4g} h_eff" if o['rz'] else ", positive") + f", largest at {o['rmax']:.2f} h_eff" for o in out)
              + ".  Its value against its maximum at R = 0.01, 0.03, 0.1, 0.3, 0.5 h_eff: " + "; ".join(f"k = {_v40_f(o['k'], 3)}: " + ", ".join(
              f"{x:.3f}" for x in o['core']) for o in cores) + ".  The halo families' slopes are NFW's -1 inside and -3 outside, Burkert's 0 and "
              "-3, the pseudo-isothermal sphere's 0 and -2.  The driven density is depressed at the center for every k -- negative inside for k <= "
              f"3.2, and for k = 16/3, 8, 16 a core at {min(o['core'][0] for o in cores):.2f}-{max(o['core'][0] for o in cores):.2f} of its maximum, "
              f"which lies at {min(o['rmax'] for o in cores):.2f}-{max(o['rmax'] for o in cores):.2f} h_eff -- and falls toward -2 beyond R = ell, "
              "the slope of any flat curve; for the larger k it falls about as 1/R between a few h_eff and ell, the point source's cusp (e) seen "
              "from outside the disk.  Inside, it is unlike each family.")
    # (d) decompositions
    fits = []
    for o in out:
        k, he, c = o['k'], o['he'], o['c']
        idx = [j for j, lg in enumerate(_V41_LG) if 0.5*he <= math.exp(lg) <= 10*he]
        Rs = [math.exp(_V41_LG[j]) for j in idx]; v2 = [c['u'][j] for j in idx]; a = [c['un'][j] for j in idx]
        fits.append((k, he, len(idx), [(nm, _v41_fit(Rs, v2, a, f), _v41_fit(Rs, v2, a, f, ups=1.0)) for nm, f, rho in _V41_HALOS]))
    _v40_wrap("(d) Decompositions [V].  The leaf's curve at the grid's radii in 0.5-10 h_eff (32 or 33 of them) fitted as Ups v_N^2 + v_h^2, the "
              "halo NFW's V^2 [ln(1 + y) - y/(1 + y)]/y, Burkert's V^2 [ln(1 + y) + ln(1 + y^2)/2 - arctan y]/y or the pseudo-isothermal V^2 [1 - "
              "arctan(y)/y], y = R/r_s, by least squares in v with errors of 3% of v -- Ups >= 0 free, then Ups = 1: the rms and the largest "
              "deviation of the fit from the leaf's curve, Ups, r_s/h_eff (* at the end of r_s's range, 1/30 of the first radius to 300 times the "
              "last): " + "; ".join(f"k = {_v40_f(k, 3)}: " + ", ".join(
              f"{nm} {100*r1[1]:.2f}% ({100*r1[2]:.2f}%), Ups {r1[3]:.3f}, r_s {r1[5]/he:.2f}{'*' if r1[6] else ''} / Ups = 1: {100*r2[1]:.2f}% "
              f"({100*r2[2]:.2f}%), r_s {r2[5]/he:.2f}{'*' if r2[6] else ''}" for nm, r1, r2 in fr_) for k, he, n, fr_ in fits) + ".")
    worst_free = max(r1[1] for k, he, n, fr_ in fits for nm, r1, r2 in fr_)
    ups_small = max(r1[3] for k, he, n, fr_ in fits if k <= 0.1 for nm, r1, r2 in fr_)
    good1 = [k for k, he, n, fr_ in fits if all(r2[1] < 0.03 for nm, r1, r2 in fr_ if nm != "NFW")]
    goodn = [(k, r2[6]) for k, he, n, fr_ in fits for nm, r1, r2 in fr_ if nm == "NFW" and r2[1] < 0.03]
    rem = []
    for o in out:
        if o['neg']: continue
        k, he, c = o['k'], o['he'], o['c']
        idx = [j for j, lg in enumerate(_V41_LG) if 0.5*he <= math.exp(lg) <= 10*he]
        Rs = [math.exp(_V41_LG[j]) for j in idx]; vd2 = [c['u'][j] - c['un'][j] for j in idx]
        rr = []
        for nm, f, rho in _V41_HALOS:
            r = _v41_fit(Rs, vd2, [0.0]*len(idx), f, ups=0.0)
            dv = [abs(math.sqrt(max(r[4]*f(R/r[5]), 0.0)/x) - 1) for R, x in zip(Rs, vd2)]; rr.append((nm, r, Rs[dv.index(max(dv))]/he))
        rem.append((k, rr))
    _v40_wrap(f"So with Ups free every family follows the leaf's curve for every k, to rms {100*worst_free:.2f}% at worst -- the disk-halo "
              f"degeneracy at work -- but for a slow falloff only with a nearly massless disk (Ups <= {ups_small:.3f} at k <= 0.1); with the image's "
              "whole mass, Ups = 1, Burkert's and the pseudo-isothermal halos follow it to better than 3% rms for k = " + ", ".join(
              f"{k:.4g}" for k in good1) + ", NFW less well, under 3% only for k = " + ", ".join(f"{k:.4g}" for k, e in goodn) + (", its scale "
              "radius there at the end of its range" if all(e for k, e in goodn) else "") + "; for k <= 1 no halo can, the leaf's curve lying below "
              "the image's own.  Fitted to the remainder alone where it is positive throughout -- v_h^2 against v_d^2 over the same radii, with "
              "errors of 3% of v_d -- no family follows it: " + "; ".join(f"k = {_v40_f(k, 3)}: " + ", ".join(f"{nm} {100*r[1]:.1f}% "
              f"({100*r[2]:.1f}% at {x:.2f} h_eff)" for nm, r, x in rr) for k, rr in rem) + ", the rms and the largest deviation and its radius: the "
              "largest at the inner radii, where the remainder rises faster than any family's curve.")
    # (e) the point source
    t = 1e-3; up = (1 + 3*t*t)/(t*math.sqrt(1 + t*t)); u0 = up/(1 + t*t)
    _v40_wrap(f"(e) The point source [T/V].  v^2/(G M/ell) = (1 + 3t^2)/(t sqrt(1 + t^2)), t = R/ell (Section XXXI.38(a)), against Newton's 1/t: "
              f"the remainder (5/2) t + O(t^3) -- at t = 1e-3, {(up - 1/t)/t:.6f} t -- of which t comes from the readout's factor 1 + R^2/ell^2 and "
              f"(3/2) t from Law I's term: without the factor, {(u0 - 1/t)/t:.6f} t.  The remainder is a uniform pull, (5/2) G M/ell^2 toward the "
              "source, whose driven density g/(2 pi G R) is a cusp falling as 1/R [T]; for the disks of (c) the remainder vanishes faster at the "
              "center, as R^2, and the driven density has no cusp there [V].")
    ok = (max(abs(d) for R, d in fr) < 1e-5 and all(not o['dmax'] for o in out) and all(o['neg'] and len(o['zr']) == 1 for o in out if o['k'] <= 3.2)
          and all(not o['neg'] and not o['zr'] for o in out if o['k'] >= 16/3) and worst_free < 0.02 and ups_small < 0.1
          and all(k in good1 for k in (2.0, 3.2, 16/3, 8.0, 16.0, 32.0, 100.0)) and [k for k, e in goodn] == [8.0, 16.0, 32.0, 100.0]
          and all(r[1] > 0.05 and x < 1 for k, rr in rem for nm, r, x in rr) and all(0.1 < o['core'][0] < o['core'][-1] < 1 for o in cores)
          and all(o['sl'][0] is not None and o['sl'][0] > 0 for o in out if o['k'] >= 16/3)
          and all(abs(o['sl'][-1] + 2) < 0.05 for o in out if 0.1 <= o['k'] <= 8) and abs((up - 1/t)/t - 2.5) < 1e-5 and abs((u0 - 1/t)/t - 1.5) < 1e-5)
    check(ok, "v40.1-2: the Newtonian reading -- Freeman reproduced; the driven remainder rises without a bump for each k computed, negative inside for "
              "k <= 3.2; its density depressed at the center, -2 outside; every halo family follows the leaf's curve with Ups free, to under 2% "
              "rms, and none the remainder alone")

def _v41_root(f, a, b, it=60):
    """A root of f in [a, b], where f changes sign, by the Illinois variant of the false position."""
    fa, fb = f(a), f(b); side = 0; c = a
    for _ in range(it):
        c = (a*fb - b*fa)/(fb - fa); fc = f(c)
        if fc == 0 or abs(b - a) < 1e-12*abs(c): return c
        if (fc > 0) == (fb > 0):
            b, fb = c, fc
            if side == -1: fa *= 0.5
            side = -1
        else:
            a, fa = c, fc
            if side == 1: fb *= 0.5
            side = 1
    return c

def _v41_mw_leaf(h, M=6e10, v0=229.0, lo=3.0, hi=30.0, scan=True):
    """The leaf on which e^(-k sin chi), k = ell/h, with mass M turns at v0 at R_sun: with scan, every root of v(R_sun) = v0 for ell in
    [lo, hi], by a scan in steps of 4% and the false position; without, the one root in [lo, hi]."""
    GM = _V40_GK*M; f = lambda L: math.sqrt(GM/L*_v41_u_fast(L/h, _V41_RSUN/L)) - v0
    if not scan: return [_v41_root(f, lo, hi)]
    Ls = [lo*1.04**i for i in range(int(math.log(hi/lo)/math.log(1.04)) + 1)]; fs = [f(L) for L in Ls]
    return [_v41_root(f, Ls[i], Ls[i + 1]) for i in range(len(Ls) - 1) if (fs[i] > 0) != (fs[i + 1] > 0)]

def _v41_wline(pts):
    """The weighted least-squares straight line through (R, v, weight): its value at R_sun and its gradient."""
    W = sum(w for x, y, w in pts); mx = sum(w*x for x, y, w in pts)/W; my = sum(w*y for x, y, w in pts)/W
    b = sum(w*(x - mx)*(y - my) for x, y, w in pts)/sum(w*(x - mx)**2 for x, y, w in pts); return my + b*(_V41_RSUN - mx), b

def _v41_mw_stats(h, L, M=6e10):
    """On the leaf L with scale h: the curve, its slope at the Sun, the gradient of the weighted line through its speeds at Eilers et al.'s
    radii (their errors' weights), its deviations from their line and points, the tail, the image's fitted scale length (v40.0-8(b)'s
    straight line through the magnitudes over 1-5 h)."""
    GM = _V40_GK*M; k = L/h; c = _v41_curves(k, False); vv = lambda R: math.sqrt(GM/L*_v41_interp(c['u'], math.log(R/L)))
    dev = [vv(R) - v for R, v, a, b in _V41_EILERS]; MAG = 2.5/math.log(10.0)
    xs = [1 + 4*i/399 for i in range(400)]; ys = [-MAG*_v40_lnimage(x, k) for x in xs]; mx, my = sum(xs)/400, sum(ys)/400
    sl = sum((x - mx)*(y - my) for x, y in zip(xs, ys))/sum((x - mx)**2 for x in xs)
    grad = _v41_wline([(R, vv(R), 1/(0.5*(a + b))**2) for R, v, a, b in _V41_EILERS])[1]
    return dict(k=k, v=[vv(R) for R in (5.0, _V41_RSUN, 16.0, 24.0, 36.0, 60.0)], slope=vv(_V41_RSUN + 0.5) - vv(_V41_RSUN - 0.5), grad=grad,
                line=[vv(R) - (229.0 - 1.7*(R - _V41_RSUN)) for R in (5.0, 16.0, 24.0)], rms=math.sqrt(sum(d*d for d in dev)/len(dev)),
                chi2=sum((d/(0.5*(a + b)))**2 for d, (R, v, a, b) in zip(dev, _V41_EILERS)), vinf=math.sqrt(GM/L*c['C']),
                tail=_v40_leafmass(k, math.atan(36/L))/_v40_leafmass(k), hfit=MAG/sl*h)

def v40_1_leaves():
    """A leaf per galaxy (R582, (f)-(h)).  (f) The frozen 16 kpc leaf with h = 2, 2.6 and 3 kpc: the curves, their peaks and tails.  (g) The Milky
    Way: for each h the leaf on which the benchmark turns at 229 km/s at the Sun, its slope there, its deviations from Eilers et al.'s curve, its
    tail and its image's scale length.  (h) The two dwarfs with the leaf free: Section XXXIII.37's arena leaves reproduced; ell and k free with
    the baryonic mass; and with a free factor on v^2."""
    print("\n== v40.1-3. A leaf per galaxy: the frozen leaf with other scale lengths, the Milky Way with its leaf set by the speed at the Sun, and "
          "the two dwarfs with the leaf free (R582) ==")
    _v41_grid(); M = 6e10; GM = _V40_GK*M
    # (f) the frozen leaf with three scale lengths
    fz = []
    for h in (2.0, 2.6, 3.0):
        k = 16/h; s = _v41_shape(k); vv = [math.sqrt(GM/16*_v41_u_at(k, R/16)) for R in (5, 8, 16, 24, 36, 60)]
        tail = _v40_leafmass(k, math.atan(36/16))/_v40_leafmass(k)
        fz.append((h, k, vv, [(16*R, q*math.sqrt(GM/16*s['c']['C'])) for R, q in s['mx']], math.sqrt(GM/16*s['c']['C']), tail))
    sw2 = _v41_shape(8.0)
    _v40_wrap("(f) The frozen leaf with other scale lengths [V].  ell = 16 kpc, 6e10 Msun: the circular speed at R = 5, 8, 16, 24, 36, 60 kpc, the "
              "maximum, the plateau and the image's mass beyond 36 kpc against the stellar halo's 1.4e9 Msun (Deason, Belokurov and Sanders 2019): "
              + "; ".join(f"h = {h:g} kpc (k = {_v40_f(k, 3)}): " + ", ".join(f"{x:.1f}" for x in vv) + " km/s, "
              + (", ".join(f"a maximum of {q:.1f} km/s at {R:.1f} kpc, {q/vi - 1:+.2%} on the plateau" for R, q in pk) if pk else "no maximum")
              + f", v_inf = {vi:.1f}; beyond 36 kpc {100*tl:.2f}% = {tl*M:.2e} Msun, {tl*M/1.4e9:.2f} times the halo" for h, k, vv, pk, vi, tl in fz)
              + ".  Below the stellar halo's mass only for h near 2 kpc; at 2.6 kpc 1.5 times it.  The shorter scale length gives the higher, "
              f"peaked curve: at h = 2 kpc it rises {sw2['mx'][0][1] - 1:.2%} above its plateau at {16*sw2['mx'][0][0]:.1f} kpc, dips "
              f"{1 - sw2['mn'][0][1]:.2%} below it at {16*sw2['mn'][0][0]:.1f} kpc, and so varies by {sw2['mx'][0][1] - sw2['mn'][0][1]:.2%} of it.")
    # (g) the Milky Way, a leaf per scale length
    hs = (1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.4, 2.6, 2.8, 3.0, 3.1); tab = []
    for h in hs:
        rts = _v41_mw_leaf(h); tab.append((h, rts, [_v41_mw_stats(h, L) for L in rts]))
    def leaf1(h): return _v41_mw_leaf(h, lo=10.0, hi=20.0, scan=False)[0]
    def one(h): return _v41_mw_stats(h, leaf1(h))
    a_, b_ = 1.9, 2.2
    for _ in range(14):
        m = 0.5*(a_ + b_)
        if one(m)['slope'] < -1.7: a_ = m
        else: b_ = m
    h17 = 0.5*(a_ + b_); s17 = one(h17); L17 = leaf1(h17)
    rbest, hbest = _v41_golden(lambda h: one(h)['rms'], 1.5, 2.2, 20); sbest = one(hbest); Lbest = leaf1(hbest)
    a_, b_ = 2.1, 2.2
    for _ in range(14):
        m = 0.5*(a_ + b_)
        if one(m)['slope'] < 0: a_ = m
        else: b_ = m
    h0 = 0.5*(a_ + b_)
    dline = _v41_wline([(R, v, 1/(0.5*(a + b))**2) for R, v, a, b in _V41_EILERS])
    loc = [_v41_wline([(R, v, wt(a, b)) for R, v, a, b in _V41_EILERS if lo <= R <= hi])[1] for lo, hi in ((6.5, 10.0), (7.0, 9.5))
           for wt in (lambda a, b: 1/(0.5*(a + b))**2, lambda a, b: 1.0)]
    hg = _v41_root(lambda h: one(h)['grad'] - dline[1], 1.8, 2.0); sg = one(hg)
    _v40_wrap("(g) The Milky Way with a leaf per scale length [V/S].  For each h the benchmark's 6e10 Msun as e^(-k sin chi) on the leaf where it "
              f"turns at 229 km/s at R_sun = {_V41_RSUN} kpc (Eilers et al. 2019's v_c and adopted R_sun; v40.0-8(d)'s reading, the leaf's speeds in "
              "gnomonic radius taken as the published ones, without Section XXXIII.19's corrections for the leaf's optics): the leaf (every root "
              "between 3 and 30 kpc), k; the speed at 5, R_sun, 16, 24, 36, 60 kpc; the local slope at the Sun, v(R_sun + 0.5) - v(R_sun - 0.5) "
              "(km/s per kpc); the gradient of the straight line through the leaf's speeds at their 38 radii, weighted by their errors as their "
              "points give their line's -1.7; the "
              "deviation from their line 229.0 - 1.7 (R - R_sun) at 5, 16, 24 kpc; the rms deviation from their 38 points at 5.27-24.82 kpc and chi^2 "
              "with their mean errors; v_inf; the tail beyond 36 kpc; the image's fitted scale length (against the thin disk's 2.6 +- 0.5 kpc, "
              "Bland-Hawthorn and Gerhard 2016): " + "; ".join(f"h = {h:g}: " + " / ".join(
              f"ell = {L:.2f} kpc, k = {s['k']:.2f}, v = "
              + ", ".join(f"{x:.1f}" for x in s['v']) + f", slope {s['slope']:+.2f}, gradient {s['grad']:+.2f}, line "
              + ", ".join(f"{d:+.1f}" for d in s['line']) + f", rms {s['rms']:.1f} km/s, chi^2 = {s['chi2']:.0f}, v_inf = {s['vinf']:.1f}, tail "
              f"{s['tail']*M:.2e} Msun, scale {s['hfit']:.2f} kpc" for L, s in zip(rts, ss)) for h, rts, ss in tab) + ".")
    _v40_wrap(f"One leaf for each h, and it shrinks as h grows.  The data themselves: the weighted line through their 38 points is {dline[0]:.2f} "
              f"{dline[1]:+.3f} (R - R_sun) km/s, their published line; lines through their points within 6.5-10 and 7-9.5 kpc, the data's own "
              f"local slope, have slopes {loc[0]:+.2f} and {loc[2]:+.2f} weighted, {loc[1]:+.2f} and {loc[3]:+.2f} unweighted.  The leaf's local "
              f"slope at the Sun is their line's -1.7 km/s per kpc at h = {h17:.3f} kpc, on ell = {L17:.2f} kpc (k = {s17['k']:.3f}), with a tail of "
              f"{s17['tail']*M:.2e} Msun, {s17['tail']*M/1.4e9:.2f} of the stellar halo, and an image of scale length {s17['hfit']:.2f} kpc -- but "
              f"its own line through their radii falls at only {s17['grad']:+.2f} km/s per kpc, and the curve flattens, {s17['line'][1]:+.1f} km/s "
              f"off their line at 16 kpc and {s17['line'][2]:+.1f} at 24 kpc, rms {s17['rms']:.1f} km/s over their points.  The leaf's line has "
              f"their gradient at h = {hg:.3f} kpc, where the local slope at the Sun is {sg['slope']:+.2f} and the rms {sg['rms']:.1f} km/s.  "
              f"The smallest rms, {sbest['rms']:.1f} km/s, is at "
              f"h = {hbest:.2f} kpc (ell = {Lbest:.2f} kpc), with a slope of {sbest['slope']:+.2f} at the Sun and an image of scale length "
              f"{sbest['hfit']:.2f} kpc; for h above {h0:.3f} kpc the curve rises at the Sun.  No scale length gives the Sun's speed, the slope there "
              "and the decline to 25 kpc together: the leaf's curve peaks and flattens where the Milky Way's keeps falling.")
    # (h) the dwarfs
    dres = []
    for nm, Mb, ella, data in _V41_DWARFS:
        ka = 4.0 if nm == "DDO 154" else 1.5
        arena = (_v41_chi2(data, Mb, ella, ka), _v41_chi2(data, Mb, ella, ka, floor=1.0))
        best = lambda k, amp: _v41_scan(lambda t: _v41_chi2(data, Mb, math.exp(t), k, amp=amp)[0], math.log(0.2), math.log(1000.0), 61, 40)
        perk = []
        for k in (0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 8.0, 16.0):
            b = best(k, False); L = math.exp(b[1]); perk.append((k, L, b[2], _v41_chi2(data, Mb, L, k)[0], _v41_chi2(data, Mb, L, k, floor=1.0)[0]))
        g = _v41_scan(lambda lk: best(math.exp(lk), False)[0], math.log(0.25), math.log(32.0), 15, 25); kg = math.exp(g[1])
        Lg = math.exp(best(kg, False)[1]); glob = (kg, Lg, _v41_chi2(data, Mb, Lg, kg), _v41_chi2(data, Mb, Lg, kg, floor=1.0))
        amps = []
        for k in (1.0, 3.0, 8.0, 32.0, 100.0):
            b = best(k, True); L = math.exp(b[1]); p = _v41_chi2(data, Mb, L, k, amp=True); Rl = data[-1][0]
            amps.append((k, L, b[2], p[0], p[1], p[1]*_v41_mass(k, math.atan(Rl/L))/_v41_mass(k, math.pi/2), Rl/L))
        mdyn = data[-1][1]**2*data[-1][0]/_V40_GK/Mb
        dres.append((nm, Mb, ella, ka, arena, perk, glob, amps, mdyn, data))
    for nm, Mb, ella, ka, arena, perk, glob, amps, mdyn, data in dres:
        _v40_wrap(f"(h) {nm} [V/S]: Section XXXIII.37's arena leaf, ell = {ella} kpc with k = {ka:g} and M_b = {Mb:.2e} Msun, gives chi^2/N = "
                  f"{arena[0][0]:.1f} with SPARC's errors and {arena[1][0]:.1f} with them floored at 1 km/s (v36.3's {'142/49' if ka == 4 else '87/37'}), "
                  f"v = " + ", ".join(f"{x:.1f}" for x in arena[0][2]) + " km/s against " + ", ".join(f"{d[1]:g}" for d in data) + " (Lelli, McGaugh "
                  "and Schombert 2016).  With M_b and the leaf free for each k, the best leaf and chi^2/N (published / floored): " + ", ".join(
                  f"k = {k:g}: ell = {L:.3f}{'*' if e else ''} kpc, {p:.1f}/{q:.1f}" for k, L, e, p, q in perk) + f"; the best over k, k = "
                  f"{glob[0]:.3f} on ell = {glob[1]:.3f} kpc, {glob[2][0]:.1f}/{glob[3][0]:.1f}, v = " + ", ".join(f"{x:.1f}" for x in glob[2][2])
                  + ".  With a free factor f on v^2 as well (f M_b the gravitating mass): " + ", ".join(
                  f"k = {k:g}: ell = {L:.1f}{'*' if e else ''} kpc (R_last/ell = {rr:.3f}), f = {f:.2f}, chi^2/N = {p:.2f}, mass inside R_last "
                  f"{mi:.2f} M_b" for k, L, e, p, f, mi, rr in amps) + f"; the Newtonian dynamical mass V^2 R/G at R_last is {mdyn:.2f} M_b.",
                  first="     ", rest="     ")
    c2s = [a[3] for d in dres for a in d[7]]; mis = [a[5] for d in dres for a in d[7]]
    small = [(d[0], a[0], a[6], a[3]) for d in dres for a in d[7] if a[6] > 1 and a[3] < 5]
    _v40_wrap("Freeing the leaf does little for the dwarfs with their baryons alone: the best chi^2/N fall from Section XXXIII.37's arena values "
              f"by {dres[0][4][0][0]/dres[0][6][2][0]:.2f} and {dres[1][4][0][0]/dres[1][6][2][0]:.2f} times, to {dres[0][6][2][0]:.0f} and "
              f"{dres[1][6][2][0]:.0f}, because the leaf small enough to reach the outer speed with M_b brings the curve to its plateau too soon.  With "
              f"the amplitude free the curves are followed, chi^2/N from {min(c2s):.2f} to {max(c2s):.2f}, the best of them on leaves many times "
              "larger than the data's radii, where the leaf's gravity is Newtonian to (R/ell)^2 -- though " + ", ".join(f"{nm}'s fit at k = {k:g} lies "
              f"on a leaf smaller than its last radius (R_last/ell = {rr:.3f}, chi^2/N = {p:.2f})" for nm, k, rr, p in small) + " -- and with "
              f"{min(mis):.2f}-{max(mis):.2f} times the baryons inside the last radius, near the Newtonian dynamical mass there: unseen matter by "
              "another name.")
    pk = {nm: perk for nm, Mb, ella, ka, arena, perk, glob, amps, mdyn, data in dres}
    ok = (abs(fz[1][5] - 0.0355) < 5e-4 and fz[0][5]*M < 1.4e9 < fz[1][5]*M and abs(fz[2][5] - 0.0576) < 5e-4 and all(len(r) == 1 for h, r, s in tab)
          and abs(h17 - 2.021) < 0.002 and s17['line'][2] > 10 and sbest['rms'] > 9 and abs(dline[0] - 229.02) < 0.05 and abs(dline[1] + 1.737) < 0.005
          and s17['grad'] > -1.2 and 1.8 < hg < 2.0 and [(nm, k) for nm, k, rr, p in small] == [("DDO 154", 1.0)]
          and abs(dres[0][4][0][0] - 142) < 1 and abs(dres[0][4][1][0] - 49) < 1 and abs(dres[1][4][0][0] - 87) < 1 and abs(dres[1][4][1][0] - 37) < 1
          and dres[0][6][2][0] > 100 and dres[1][6][2][0] > 50 and all(a[3] < 5 and a[4] > 5 for d in dres for a in d[7][1:4]))
    check(ok, "v40.1-3: a leaf per galaxy -- on the frozen leaf the tail is below the stellar halo only for h near 2 kpc; for the Milky Way one "
              "leaf per h, the local slope at the Sun right at h = 2.021 kpc but the curve flat beyond; the dwarfs need several times their baryons")

def v40_1_suite():
    """The v40.1 sections: the follow-up of 20-21 November -- Entry 326's falloff on a leaf and the shape classes; the Newtonian reading and the
    halo families; a leaf per galaxy, the Milky Way and the two dwarfs."""
    v40_1_falloff(); v40_1_newton(); v40_1_leaves()

# ==================================================================================================== v40.2 (22 November 2026)
# The second follow-up: the quick falloff the third message of 20 November asked for, the point source's apparent halo in closed form, the
# image's apparent density against the exponential, and what the density near the leaf's equator does to the curve (R587-R590).

def _v42_freeman_peak():
    """Freeman's exponential disk, v^2 = 2 (G M/h) y^2 [I0 K0 - I1 K1] with y = R/(2h): its maximum, by golden section, (R/h, v^2 h/(G M))."""
    vf = lambda y: 2*y*y*(_v40_bessel(0, y, 'I')*_v40_bessel(0, y, 'K') - _v40_bessel(1, y, 'I')*_v40_bessel(1, y, 'K'))
    f, y = _v41_golden(lambda y: -vf(y), 0.8, 1.4, 60); return 2*y, -f

def _v42_point(t):
    """The point source on the leaf at R/ell = t (Section XXXI.38(a)): v^2 ell/(G M) = (1 + 3t^2)/(t sqrt(1 + t^2)); its apparent dark mass
    M_d(<R)/M = R v_d^2/(G M) = (1 + 3t^2)/sqrt(1 + t^2) - 1, v_d^2 = v^2 - G M/R; and its driven density rho_d ell^3/M = (5 + 3t^2)/(4 pi t (1 +
    t^2)^(3/2)), the spherical equivalent (1/(4 pi G R^2)) d(R v_d^2)/dR."""
    u = (1 + 3*t*t)/(t*math.sqrt(1 + t*t)); md = (1 + 3*t*t)/math.sqrt(1 + t*t) - 1; rho = (5 + 3*t*t)/(4*math.pi*t*(1 + t*t)**1.5)
    return u, md, rho

def _v42_image_ratio(k, X):
    """The image's surface density against the exponential of the same falloff, Sigma_vis/(Sigma_0 e^(-R/h)) at R/ell = X, with Sigma_vis =
    e^(-k sin chi) cos^3 chi and R/h = k X (Entry 326's source on the leaf, seen in the gnomonic plane)."""
    s = X/math.sqrt(1 + X*X); return math.exp(-k*s + k*X)/(1 + X*X)**1.5

def _v42_mass_beyond(k, X):
    """The fraction of the source's mass beyond R/ell = X: int e^(-k sin t) sin t dt from atan X to pi/2 over the same from 0 (graded panels)."""
    def part(a, b):
        e = sorted(set([a, b] + [p for p in (0.0025*2.0**m for m in range(10)) if a < p < b])); tot = 0.0
        for lo, hi in zip(e[:-1], e[1:]):
            for t, w in _v40_graded(lo, hi, False, False): tot += w*math.exp(-k*math.sin(t))*math.sin(t)
        return tot
    c = math.atan(X); return part(c, math.pi/2)/part(0.0, math.pi/2)

def v40_2_quick():
    """v40.2-1 (R588-R589).  (a) The quick falloff: k = 100, the falloff length 0.01 ell, against Freeman's peak over the point source's plateau.
    (b) The point source's apparent halo in closed form.  (c) The image's apparent density against the exponential, on the Milky Way's leaf of
    Section XXXVIII.22(g) and on larger leaves with the same scale length."""
    print("\n== v40.2-1. The quick falloff, the point source's apparent halo, and the image's density against the exponential")
    # (a) the quick end
    yF, vF = _v42_freeman_peak()
    rows = []
    for k in (16.0, 32.0, 64.0, 100.0):
        s = _v41_shape(k); c = s['c']; R, q = s['mx'][0]; est = math.sqrt(vF*k/c['C'])
        jn = min(max(max(range(len(c['un'])), key=lambda j: c['un'][j]), 1), len(c['un']) - 2)
        fN, sN = _v41_golden(lambda x: -_v41_lp(c['un'], x)[0], _V41_LG[jn - 1], _V41_LG[jn + 1], 60)
        he = s['he']; ud = [a - b for a, b in zip(c['u'], c['un'])]
        dmax = max(_v41_lp(ud, math.log(f*he))[0]/_v41_lp(c['u'], math.log(f*he))[0] for f in (0.5, 1, 2, 5, 10))
        rows.append((k, R/he, q, est, math.sqrt(-fN/c['C']), dmax, c['C']))
    _v40_wrap("(a) The quick falloff [V].  The third message of 20 November, as the author's correction of 22 November reads it, asks to check "
              "falloff lengths as short as 0.01 ell, k = 100, the quick end of v40.1-1's scan, where the curve's bump comes earliest and highest.  "
              "Freeman's exponential disk peaks at R = "
              f"{yF:.4f} h with v^2 = {vF:.5f} G M/h; over the leaf's plateau C G M/ell that peak is sqrt({vF:.5f} k/C) times v_inf.  The bump, its "
              "radius in h_eff and its height; that estimate; the image's own Newtonian peak; the remainder's largest share v_d^2/v^2 at 0.5, 1, 2, "
              "5 and 10 h_eff: " + "; ".join(f"k = {k:g}: {r:.2f} h_eff, {q:.4f} v_inf; {e:.4f}; {n:.4f}; {d:+.3f}" for k, r, q, e, n, d, C in rows) + ".  So "
              "for a quick falloff the bump is the image's own disk at Freeman's peak, as v40.1-2(b) found, its height over the plateau growing as "
              "sqrt(k), and the "
              "leaf's remainder at those radii falls as k grows, to a few percent of v^2 at k = 64 and 100.")
    # (b) the point source's apparent halo
    ts = (0.01, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0)
    num = []
    for t in ts:
        d = 1e-5*t; m = lambda x: x*(_v42_point(x)[0] - 1/x)
        num.append(abs(((m(t + d) - m(t - d))/(2*d))/(4*math.pi*t*t)/_v42_point(t)[2] - 1))
    slope = lambda t: (math.log(_v42_point(t*1.0001)[2]) - math.log(_v42_point(t/1.0001)[2]))/(2*math.log(1.0001))
    _v40_wrap("(b) The point source's apparent halo [T].  A point mass M on the leaf gives v^2 = (G M/ell)(1 + 3t^2)/(t sqrt(1 + t^2)), t = R/ell; "
              "read as Newton's G M/R plus a halo, the halo's mass inside R is M_d = M[(1 + 3t^2)/sqrt(1 + t^2) - 1] and its density, the "
              "spherical equivalent, rho_d = (M/ell^3)(5 + 3t^2)/(4 pi t (1 + t^2)^(3/2)), in closed form (the numerical derivative agrees to "
              f"{max(num):.1e}).  M_d/M at t = " + ", ".join(f"{t:g}: {_v42_point(t)[1]:.4f}" for t in ts) + f" -- {_v42_point(1.0)[1]:.4f}, 2 sqrt 2 "
              "- 1, inside R = ell -- and the density's logarithmic slope " + ", ".join(f"{slope(t):+.3f}" for t in ts) + ": a cusp falling as "
              "1/R for R << ell, NFW's inner slope, turning near R = ell to 1/R^2, the isothermal sphere's, with no free parameter; its mass grows "
              "as 3 M R/ell without bound.")
    # (c) the image's apparent density against the exponential
    h, M = 2.021, 6e10; GM = _V40_GK*M
    leaves = []
    for L in (14.95, 50.0, 100.0):
        k = L/h; Rs = (5.0, 10.0, 15.0, 25.0, 50.0)
        rat = [_v42_image_ratio(k, R/L) for R in Rs]
        dep = lambda R: abs(_v42_image_ratio(k, R/L) - 1) - 0.1
        r10 = _v41_bisect(dep, 0.5*h, 200.0) if dep(0.5*h) < 0 < dep(200.0) else math.nan
        fin = 1 - _v42_mass_beyond(k, r10/L) if r10 == r10 else math.nan
        leaves.append((L, k, rat, r10, _v42_mass_beyond(k, 36.0/L), math.sqrt(_v41_curves(k)['C']*GM/L), fin))
    _v40_wrap(f"(c) The image's density against the exponential [T/V].  With h = {h} kpc and 6e10 Msun, the Milky Way's leaf of Section "
              "XXXVIII.22(g), with ell and h as printed there, and two larger leaves: the image's surface density against Sigma_0 e^(-R/h) at R = 5, "
              "10, 15, 25, 50 kpc; the radius where it first departs from the exponential by 10%, and the fraction of the mass inside it; the "
              "fraction beyond 36 kpc; the plateau speed sqrt(C G M/ell): "
              + "; ".join(f"ell = {L:g} kpc (k = {k:.3f}): " + ", ".join(f"{x:.3g}" for x in rat) + f"; 10% at {r10:.2f} kpc, inside it "
              f"{100*fi:.1f}%; beyond 36 kpc {100*f:.3g}%; v_inf = {v:.1f} km/s" for L, k, rat, r10, f, v, fi in leaves)
              + ".  The image is exponential while R << ell, the areal radius ell sin chi being R there; beyond R = ell it falls as cos^3 chi, as "
              "(ell/R)^3 for R >> ell, its exponent saturating toward e^(-k) once R^2 >> k ell^2.  The leaf that gives the Milky Way's speed at the "
              "Sun keeps the exponential only to four scale lengths, though that part holds most of the mass; a leaf large enough to keep it to nine "
              "gives a plateau far below the Milky Way's speed.")
    ok = (abs(yF - 2.1501) < 1e-3 and abs(vF - 0.38705) < 1e-4 and all(abs(e/q - 1) < 2e-3 and abs(n/q - 1) < 2e-3 for k, r, q, e, n, d, C in rows if k >= 64)
          and all(rows[i + 1][2] > rows[i][2] for i in range(len(rows) - 1)) and rows[-1][5] < 0.03
          and max(num) < 1e-6 and abs(_v42_point(1.0)[1] - (2*math.sqrt(2) - 1)) < 1e-12 and abs(slope(0.01) + 1) < 0.01 and abs(slope(100.0) + 2) < 0.01
          and leaves[0][3] < 10 < leaves[1][3] < leaves[2][3] and leaves[0][2][3] > 10 and leaves[0][4] < 0.02 and leaves[2][5] < 100 < leaves[0][5]
          and abs(leaves[0][3]/h - 4) < 0.1 and abs(leaves[2][3]/h - 9) < 0.1 and leaves[0][6] > 0.5)
    check(ok, "v40.2-1: the quick falloff's bump is the image's own Freeman peak, growing as sqrt(k); the point source's apparent halo in closed form, "
              "1/R for R << ell and 1/R^2 for R >> ell; the image exponential only while R << ell")

def v40_2_equator():
    """v40.2-2 (R589).  The density near the leaf's equator and the curve: on the Milky Way's leaf (ell = 14.95 kpc, h = 2.021 kpc, 6e10 Msun)
    and on the same leaf with a slow falloff (h = ell), the curve with the source as it is and with its part beyond R = 36 kpc removed, doubled
    and held at its value there, the inner density fixed, by v40.0's thin-disk solver (64 azimuths); for the Milky Way's falloff the changes at
    Eilers et al.'s 38 radii against their mean errors, and the tail's mass against the stellar halo's; for the slow falloff the doubled tail's
    v^2 beyond its last circular orbit."""
    print("\n== v40.2-2. The density near the equator and the curve")
    L, M = 14.95, 6e10; GM = _V40_GK*M; Rs = (5.0, 8.0, 16.0, 24.0, 60.0); cut = math.atan(36.0/L); HALO = 1.4e9
    ER = [math.atan(e[0]/L) for e in _V41_EILERS]; ES = [0.5*(e[2] + e[3]) for e in _V41_EILERS]
    out = []; ev = []
    for h in (2.021, L):
        k = L/h; S0, b0 = _v40_sin_source(k); brk = sorted(set(b0 + [cut]))
        tails = (("as it is", lambda x: S0(x)), ("removed", lambda x: S0(x) if x < cut else 0.0), ("doubled", lambda x: S0(x)*(2.0 if x >= cut else 1.0)),
                 ("held at its value at 36 kpc", lambda x: S0(min(x, cut))))
        n0 = _v40_disk_norm(S0, brk); res = []
        for nm, S in tails:
            n = _v40_disk_norm(S, brk); v2 = _v40_disk_v2(S, L, M*n/n0, [math.atan(R/L) for R in Rs], brk)
            C = _v40_C_solver(S, brk)
            res.append((nm, n/n0, [math.sqrt(x) if x > 0 else None for x in v2], math.sqrt(C*GM*(n/n0)/L) if C > 0 else None, C))
            if h != L: ev.append([math.sqrt(x) for x in _v40_disk_v2(S, L, M*n/n0, ER, brk)])
        if h != L:
            tail = M*(1 - res[1][1]); held = M*(res[3][1] - res[1][1])
            z = [[(a - b)/s for a, b, s in zip(e, ev[0], ES)] for e in ev[1:]]
            zmax = [max(range(len(q)), key=lambda i: abs(q[i])) for q in z]
            own = [(a - e[1])/s for a, e, s in zip(ev[0], _V41_EILERS, ES)]
        else:
            Sd = tails[2][1]; nd = _v40_disk_norm(Sd, brk); f = lambda R: _v40_disk_v2(Sd, L, M*nd/n0, [math.atan(R/L)], brk)[0]
            fa, fb = f(16.0), f(24.0); r0 = _v41_bisect(f, 16.0, 24.0, 30)
            far = (18.5, 20.0, 30.0, 50.0, 100.0, 300.0, 1000.0); vfar = _v40_disk_v2(Sd, L, M*nd/n0, [math.atan(R/L) for R in far], brk)
        out.append((h, k, res))
    fv = lambda x: "none" if x is None else f"{x:.1f}"
    dv = lambda x, y: "-" if x is None or y is None else f"{x - y:+.2f}"
    _v40_wrap("(a) The equator's density [V].  The density near the leaf's equator, R >> ell in the gnomonic plane, changed beyond R = 36 kpc "
              f"(chi = {math.degrees(cut):.2f} degrees) with the density inside it fixed; the mass against the source's own, the speed at 5, 8, 16, "
              "24, 60 kpc (none where v^2 < 0) and the plateau, and the changes from the source as it is: " + "; ".join(f"h = {h:g} kpc (k = {k:.3f}): "
              + "; ".join(f"{nm}: mass {m:.4f}, v = " + ", ".join(fv(x) for x in v) + f", v_inf = {fv(vi)}" + ("" if nm == "as it is" else
              " (" + ", ".join(dv(x, y) for x, y in zip(v, res[0][2])) + f"; {dv(vi, res[0][3])})") for nm, m, v, vi, C in res) for h, k, res in out)
              + ".  Mass near the equator pulls the inner disk outward, as the outer rings of any thin disk do: removing it raises the curve, "
              "doubling it lowers it.")
    _v40_wrap("(b) Against the data and the census [V].  For the Milky Way's falloff, at the 38 radii of Eilers et al. (2019), against their mean "
              "errors: the largest change removed, doubled and held is " + ", ".join(f"{abs(q[i]):.2f}" for q, i in zip(z, zmax)) + " times the error, "
              "at " + ", ".join(f"{_V41_EILERS[i][0]:g}" for i in zmax) + " kpc; the sum of (change/error)^2 is " + ", ".join(f"{sum(x*x for x in q):.1f}"
              for q in z) + f", against the leaf's own misfit to the same points, {sum(x*x for x in own):.1f} (rms "
              f"{math.sqrt(sum((a - e[1])**2 for a, e in zip(ev[0], _V41_EILERS))/len(ev[0])):.1f} km/s).  The tail beyond 36 kpc, "
              f"{tail:.3g} Msun, is {tail/HALO:.2f} of the Milky Way's stellar halo, 1.4e9 Msun (Deason, Belokurov and Sanders 2019); held at its "
              f"value at 36 kpc it would be {held/HALO:.2f} of it, doubled {2*tail/HALO:.2f}.  For the slow falloff the doubled "
              f"tail's v^2 is {fa:+.0f} and {fb:+.0f} (km/s)^2 at 16 and 24 kpc, zero at {r0:.2f} kpc, and negative at 18.5, 20, 30, 50, "
              "100, 300 and 1000 kpc (" + ", ".join(f"{x:+.0f}" for x in vfar) + f"), its plateau coefficient C = {out[1][2][2][4]:.3f}: no "
              "circular orbit beyond.  So for the Milky Way's falloff the region beyond 36 kpc, 1.46% of the mass, moves the curve inside 24 kpc by "
              "under 2 km/s, about the statistical errors of the measured curve at 11-15 kpc and far below the leaf's own misfit, and the plateau "
              "by about 1 km/s, or 3 if held; the curve constrains it only weakly, the stellar census more.  For the slow falloff the same region "
              "holds 31% of the mass, and removing or doubling it moves the curve by more than 10 km/s from 8 kpc out and by tens of km/s from 16 "
              "kpc, holding it by under 4 km/s inside 24 kpc.")
    dq = [abs(x - y) for nm, m, v, vi, C in out[0][2][1:] for x, y in zip(v[:4], out[0][2][0][2][:4])]
    sl = out[1][2]; d8 = [abs(sl[i][2][1] - sl[0][2][1]) for i in (1, 2)]
    d16 = [abs(sl[i][2][2] - sl[0][2][2]) for i in (1, 2)] + [abs(sl[1][2][3] - sl[0][2][3])]
    ok = (max(dq) < 2.0 and abs(1 - out[0][2][1][1] - 0.0146) < 0.0005 and abs(1 - out[1][2][1][1] - 0.309) < 0.005
          and all(x is not None for nm, m, v, vi, C in out[0][2] for x in v) and abs(out[0][2][1][3] - out[0][2][0][3] - 1) < 0.2
          and abs(out[0][2][3][3] - out[0][2][0][3] + 3) < 0.2
          and 1.0 < max(abs(q[i]) for q, i in zip(z, zmax)) < 1.5 and max(sum(x*x for x in q) for q in z) < 0.05*sum(x*x for x in own)
          and 0.5 < tail/HALO < 0.8 < held/HALO < 1 < 2*tail/HALO
          and fa > 0 > fb and 16 < r0 < 24 and all(x < 0 for x in vfar) and out[1][2][2][4] < 0
          and sl[2][2][3] is None and sl[2][2][4] is None and sl[2][3] is None and min(d8) > 10.0 and min(d16) > 20.0
          and max(abs(sl[3][2][j] - sl[0][2][j]) for j in range(4)) < 4.0)
    check(ok, "v40.2-2: the density beyond 36 kpc moves the Milky Way leaf's curve inside 24 kpc by under 2 km/s, about the data's errors and far "
              "below the leaf's own misfit, its tail 0.63 of the stellar halo; a slow falloff's by tens of km/s, the doubled tail leaving no orbit")

def v40_2_suite():
    """The v40.2 sections: v40.2-1 and v40.2-2 (R587-R590)."""
    v40_2_quick(); v40_2_equator()

def current_suite_v40():
    """The regression suite of Part XXXVIII (v40.0, v40.1 and v40.2), followed by the check summary."""
    v40_0_suite(); v40_1_suite(); v40_2_suite()
    npass = sum(1 for ok, _ in _CHECKS if ok); nfail = len(_CHECKS)-npass
    print(f"\n== check summary (Part XXXVIII): {npass} passed, {nfail} failed ==")
    for ok, msg in _CHECKS:
        if not ok: print("   FAILED:", msg)
    return nfail == 0
# ==================================================================================================== end of v40 body

if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else "current"
    suites = {"current": current_suite_v40, "v40_0": v40_0_suite, "v40_1": v40_1_suite, "v40_2": v40_2_suite}
    if arg not in suites:
        print("usage: python3 -I pg_v40_numerics.py [" + " | ".join(suites) + "]"); sys.exit(2)
    suites[arg]()
    if arg != "current":
        npass = sum(1 for ok, _ in _CHECKS if ok); print(f"\n== check summary ({arg}): {npass} passed, {len(_CHECKS)-npass} failed ==")
    if any(not ok for ok, _ in _CHECKS):
        sys.exit(1)
