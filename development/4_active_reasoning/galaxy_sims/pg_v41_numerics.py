"""Projective Gravity v41 -- standalone numerical suite for Part XXXIX: the moment form upstream -- the references' relations, modes and
legibility, the leaf's rays in the form of the Born rule, the orbit across the equator, the ortho image of a galaxy, the association's germ and
the forgotten circle as an augmentation -- Entries 549-556 with the responses to them and the reviews of the replies, of 24 November 2026
(v41.0).  Unlike the frozen suites, which compute in plain Python arithmetic, it uses NumPy's linear algebra and SciPy's quadrature, root
finders, optimizers, ODE integrator and special functions: its decimals are rounded so as not to depend on a library's last bits, and its
residuals are printed as bounds (Python 3.13 with NumPy 2.5 and SciPy 1.18 run; Python 3.11-3.13 parse it).
Part XXXVIII is frozen at v40.5 with its suite pg_v40_numerics.py and its galaxy computations galaxy_sims/sparc175/pg_v404_sparc.py and
pg_v405_sparc.py; Part XXXVII at v39.0 with pg_v39_numerics.py; Part XXXVI at v38.2 with pg_v38_numerics.py; Part XXXV at v37.9 with
pg_v37_numerics.py; Parts XXXIII-XXXIV at v36.16 with pg_v36_numerics.py; Parts XXX-XXXII at v35.8 with pg_v35_numerics.py; Part XXIX's frozen
suite is pg_v34_numerics.py (v34.10).

Run (from the directory holding this file):
    python3 -I pg_v41_numerics.py              # the regression suite of Part XXXIX, v41.0 (check summary; under half a minute)
    python3 -I pg_v41_numerics.py v41_0        # the v41.0 sections only
Every mode exits with status 1 if any check fails; an unknown mode prints the usage line and exits with status 2.

v41_0_suite(): Entry 549, the matter's second-moment form pushed upstream -- the references' relation matrix and its signature, the
collective reference as the timelike eigenvector, dust's energy frame, a reference on Kerr-Newman's line and on its stationary limit, the
positive channels' block and its gap, the sphere of references' form, the pole's form and the order of normalization, handedness in the
Hermitian form, constraints at symmetric configurations and the momentum maps.  Entries 550-551, modes, legibility and occupancy -- the
entropy over the sphere of references as the two horizons', a fixed form's four modes, the Boltzmann and the oscillating weightings, several
modes from one ensemble, occupancy off a mode, the blow-up about an offset axis, the maps that keep the modes, legibility's entropy and its
asymmetry.  Entry 552 and the message after it, the leaf's rays in the form of the Born rule -- a ray as a pair of spin states, its wave,
incidence as equal transition probabilities, waves of higher spin and their overlaps, the relation forced on a sphere of labels, the
reference's split, fields as matrices, the disk's form and the two Hopf fields, rays as involutions, the closing rule and the frame from
one law, the two lanes' overlap.  The orbit across the leaf's equator -- the leaf's speed and the chart's, the returning half as the mirror
image, the two-armed resonance and its width.  Entry 554, the ortho image of a galaxy -- the Hopf quotient and the two lanes, the tilted
quotient's ring and its Legendre factors, a two-armed disk read through a tilt, which pair of directions is forgotten and time's survival,
the averaged quotient of a squashed shell, a tilt of the reference.  Entry 555, the association's germ -- the association as the point, its
turn across a distance, the Maurer-Cartan limit with Pauli values, the Dirac operator built from it on the 3-sphere and on the leaf's two spin
structures.  Entry 556, the forgotten circle as a Markov augmentation -- a geodesic's image, the rendered state that is not closed, the
charge that closes it and the phase that inverts it, transforming before and after the blow-up, a move anchored at one reference.
Data embedded, attributed where printed: the IAU's astronomical unit (2012) and its parsec (2015).
"""
import numpy as np
PI = np.pi
_CHECKS = []
def check(cond, msg):
    _CHECKS.append((bool(cond), msg))
    print(f"   [{'PASS' if cond else 'FAIL'}] {msg}")

# ==================================================================================================== v41 body
# (the toy file appends everything below this line, reusing its own check and _CHECKS)
import math
import itertools
import textwrap
from scipy import optimize as _P39_OPT
from scipy import integrate as _P39_INT
from scipy import special as _P39_SP
from scipy import interpolate as _P39_IPL

# ---------------------------------------------------------------------------------------------------- the library
# Printers, quaternions and the association R_q, the Hopf quotient, Pauli matrices, the three-channel form, homogeneous polynomials on R^4
# with linear vector fields acting on them, Law I's point-mass orbits on the leaf, and the two-armed disk read through a tilted quotient.
# Each section draws from its own seeded generator, so a section run alone prints what it prints in the suite.

def _p39_say(text, first="   ", rest="     "):
    """Print one statement, wrapped at 150 columns without breaking a token."""
    print(textwrap.fill(text, width=150, initial_indent=first, subsequent_indent=rest, break_long_words=False, break_on_hyphens=False))

def _p39_head(label, title):
    print(); _p39_say(f"== {label}. {title}", first="", rest="   ")

def _p39_lt(x, bound):
    """A residual as a bound: 'below 1e-12' when it is below the bound, else its value."""
    b = f"{bound:.0e}".replace("e-0", "e-")
    return f"below {b}" if x < bound else f"{x:.1e} (not below {b})"

def _p39_qm(a, b):
    return np.array([a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3], a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2],
                     a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1], a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]])

def _p39_qc(a):
    return np.array([a[0], -a[1], -a[2], -a[3]])

def _p39_unit(v):
    return v/np.linalg.norm(v)

def _p39_ex(a, t):
    """exp(t a) for a unit imaginary quaternion a, given as a 3-vector."""
    return np.r_[np.cos(t), np.sin(t)*np.asarray(a)]

def _p39_rot(q):
    """The association at q: the rotation u -> q u q* of the imaginary quaternions, the graph of an observer's sky (XXXVIII.13(a))."""
    return np.array([_p39_qm(_p39_qm(q, np.r_[0, e]), _p39_qc(q))[1:] for e in np.eye(3)]).T

def _p39_hop(q, n3=(1.0, 0.0, 0.0)):
    """The quotient by the circle q -> exp(n t) q: q* n q, a point of the unit 2-sphere."""
    return _p39_qm(_p39_qm(_p39_qc(q), np.r_[0, np.asarray(n3)]), q)[1:]

_P39_S = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
_P39_ETA = np.diag([1.0, 1.0, -1.0])

def _p39_ip(z, u):
    """Kinnersley's form on the three channels, <z, u> = z^dagger eta u, eta = diag(1, 1, -1)."""
    return np.conj(z) @ _P39_ETA @ u

def _p39_tl(rng, n):
    """n unit timelike vectors of the three channels: <z, z> = -1."""
    x = rng.normal(size=(n, 2)) + 1j*rng.normal(size=(n, 2)); x *= rng.uniform(0.1, 1.5, size=(n, 1))
    return np.column_stack([x, np.sqrt(1 + (abs(x)**2).sum(1))])

def _p39_mons(n):
    return [m for m in itertools.product(range(n + 1), repeat=4) if sum(m) == n]

def _p39_act(Mv, n):
    """The vector field V(x) = Mv x acting on the homogeneous polynomials of degree n in four variables, as a matrix on monomials."""
    B = _p39_mons(n); ix = {m: i for i, m in enumerate(B)}; X = np.zeros((len(B), len(B)))
    for j, m in enumerate(B):
        for i in range(4):
            if m[i] == 0: continue
            for k in range(4):
                if Mv[i, k] == 0: continue
                mm = list(m); mm[i] -= 1; mm[k] += 1; X[ix[tuple(mm)], j] += m[i]*Mv[i, k]
    return X

def _p39_harm(n):
    """An orthonormal basis (in monomial coefficients) of the harmonic polynomials of degree n: the Laplacian's kernel, by SVD."""
    B = _p39_mons(n)
    if n < 2: return np.eye(len(B))
    Bl = _p39_mons(n - 2); il = {m: i for i, m in enumerate(Bl)}; Lp = np.zeros((len(Bl), len(B)))
    for j, m in enumerate(B):
        for i in range(4):
            if m[i] >= 2: mm = list(m); mm[i] -= 2; Lp[il[tuple(mm)], j] += m[i]*(m[i] - 1)
    u, s_, vt = np.linalg.svd(Lp); Hb = vt[(s_ > 1e-9).sum():].T
    return np.linalg.qr(Hb)[0]

def _p39_veff(ch, L):
    s = np.sin(ch); return L*L/(2*s*s) - 1/s + 2*s

def _p39_rhs(L):
    """Law I's even point source on the leaf in units of ell and GM/ell (XXXVIII.48(a)): (chi, d chi/dt, phi)."""
    return lambda t, y: [y[1], np.cos(y[0])*(L*L/np.sin(y[0])**3 - 1/np.sin(y[0])**2 - 2), L/np.sin(y[0])**2]

def _p39_pericenter(E, L):
    top = np.arcsin(_P39_OPT.brentq(lambda s: s + 2*s**3 - L*L, 1e-6, 1.0)) if L*L < 3 else np.pi/2 - 1e-9
    return _P39_OPT.brentq(lambda c_: _p39_veff(c_, L) - E, 1e-3, top)

def _p39_half(E, L):
    """From the pericenter near the pole across the equator to the twin pericenter near the antipodal pole, on the 3-sphere."""
    chp = _p39_pericenter(E, L)
    ev1 = lambda t, y: y[0] - np.pi/2
    ev1.direction = 1
    ev2 = lambda t, y: y[1]
    ev2.direction = -1; ev2.terminal = True
    return chp, _P39_INT.solve_ivp(_p39_rhs(L), [0, 400], [chp, 1e-12, 0.0], events=[ev1, ev2], rtol=1e-11, atol=1e-13, dense_output=True)

def _p39_sweep(E, L):
    """The turn between the two pericenters on the 3-sphere, in radians; in the readout successive pericenters are this plus pi apart."""
    chp, so = _p39_half(E, L); return so.sol(so.t_events[1][0])[2]

def _p39_arm_disk(rng, n, pitch=20.0, contrast=0.5):
    """A thin exponential disk with two logarithmic arms: radii with surface density e^(-R), azimuths with weight 1 + c cos 2(phi - ln R/tan i)."""
    R = rng.gamma(2.0, 1.0, n); pit = np.radians(pitch); ph = np.empty(n); todo = np.arange(n)
    while len(todo):
        p_ = rng.uniform(0, 2*np.pi, len(todo)); ok = rng.uniform(0, 1 + contrast, len(todo)) < 1 + contrast*np.cos(2*(p_ - np.log(R[todo])/np.tan(pit)))
        ph[todo[ok]] = p_[ok]; todo = todo[~ok]
    return R, ph

def _p39_tilt(rng, R, ph, beta):
    """Each point moved to a uniformly random point of the ring of angular radius beta about its direction, at its own distance from the center."""
    n = len(R); xh = np.column_stack([np.cos(ph), np.sin(ph), 0*ph]); tg = np.column_stack([-np.sin(ph), np.cos(ph), 0*ph]); zh = np.array([0, 0, 1.0])
    al = rng.uniform(0, 2*np.pi, n); d = np.cos(beta)*xh + np.sin(beta)*(np.cos(al)[:, None]*zh + np.sin(al)[:, None]*tg)
    return R[:, None]*d

# ---------------------------------------------------------------------------------------------------- v41.0-1: Entry 549
def v41_0_moments():
    """v41.0-1 (R617, Section XXXIX.4): Entry 549 -- the matter's second-moment form pushed upstream."""
    _p39_head("v41.0-1", "Entry 549: the matter's second-moment form pushed upstream -- the references' relation matrix and its signature, the "
              "collective reference, dust's energy frame, a reference on Kerr-Newman's line, the positive channels' block, the sphere of references, "
              "the pole's form, handedness, constraints at symmetric configurations (Section XXXIX.4)")
    rng = np.random.default_rng(549); eta = _P39_ETA; ip = _p39_ip
    # (a) the relation matrix and the collective reference
    N = 40; Z = _p39_tl(rng, N).T; w = rng.uniform(0.2, 2, N)
    T = ((Z*w) @ Z.conj().T) @ eta
    ev, V = np.linalg.eig(T); o = np.argsort(ev.real); ev, V = ev[o], V[:, o]; lam = ev.real
    nrm = [ip(V[:, i], V[:, i]).real for i in range(3)]; offd = max(abs(ip(V[:, i], V[:, j])) for i in range(3) for j in range(3) if i != j)
    vm = V[:, 0]/np.sqrt(-nrm[0])
    def f(p):
        xi = p[:2] + 1j*p[2:]; u = np.array([xi[0], xi[1], np.sqrt(1 + (abs(xi)**2).sum())])
        return float((w*abs(np.conj(Z).T @ eta @ u)**2).sum())
    r = _P39_OPT.minimize(f, np.zeros(4), method="BFGS", options={"gtol": 1e-12})
    xi = r.x[:2] + 1j*r.x[2:]; um = np.array([xi[0], xi[1], np.sqrt(1 + (abs(xi)**2).sum())])
    G = np.sqrt(w)[:, None]*(Z.conj().T @ eta @ Z)*np.sqrt(w)[None, :]
    g, Q = np.linalg.eigh(G); big = abs(g) > 1e-9; inert = (int((g > 1e-9).sum()), int((g < -1e-9).sum()), int((~big).sum()))
    c = Q[:, np.argmin(g)]; zb = Z @ (np.sqrt(w)*c); zb /= np.sqrt(-ip(zb, zb).real)
    Zr = (np.sqrt(abs(g[big]))[:, None]*Q[:, big].conj().T); sg = np.diag(np.sign(g[big]))
    rk = []
    for k in (1, 2, 3, 5):
        gk = np.linalg.eigvalsh(Z[:, :k].conj().T @ eta @ Z[:, :k]); rk.append(((abs(gk) > 1e-9).sum(), (gk > 1e-9).sum(), (gk < -1e-9).sum()))
    _p39_say(f"(a) Forty unit timelike references z_a in the three channels, <x, y> = x^dagger eta y with eta = diag(1, 1, -1), weights w_a from "
             f"0.2 to 2.  T = sum_a w_a z_a <z_a, .>: eigenvalues {lam[0]:.6f}, {lam[1]:.6f}, {lam[2]:.6f}, their imaginary parts "
             f"{_p39_lt(abs(ev.imag).max(), 1e-12)}; the eigenvectors' norms {', '.join('negative' if x < 0 else 'positive' for x in nrm)}, "
             f"their mutual products {_p39_lt(offd, 1e-12)}.")
    _p39_say(f"The least of sum_a w_a |<z_a, u>|^2 over <u, u> = -1, by search: {r.fun:.6f} = -lambda_- ({_p39_lt(abs(r.fun + lam[0]), 1e-6)}), "
             f"at T's timelike eigenvector (|<u, v_->| - 1 {_p39_lt(abs(abs(ip(um, vm)) - 1), 1e-9)}).")
    gnz = np.sort(g[big])
    _p39_say(f"The weighted relation matrix G_ab = sqrt(w_a w_b) <z_a, z_b>, {N} x {N}: its nonzero eigenvalues are T's "
             f"({_p39_lt(np.abs(gnz - np.sort(lam)).max(), 1e-9)}); inertia {inert} -- two positive, one negative, the rest zero.  Its negative mode "
             f"c gives z* = sum_a sqrt(w_a) c_a z_a, T's timelike eigenvector (|<z*, v_->| - 1 {_p39_lt(abs(abs(ip(zb, vm)) - 1), 1e-9)}); vectors "
             f"rebuilt from G's eigenvectors alone reproduce G ({_p39_lt(abs(Zr.conj().T @ sg @ Zr - G).max(), 1e-12)}), with the signature read "
             f"off G, ({', '.join('+' if x > 0 else '-' for x in np.sign(g[big])[::-1])}).")
    _p39_say("1, 2, 3 and 5 references: rank " + ", ".join(str(a) for a, _, _ in rk) + "; (positive, negative) " +
             ", ".join(f"({b}, {c_})" for _, b, c_ in rk) + ".")
    rx = np.random.default_rng(5490); bad = 0; worst = 0.0
    for _ in range(500):
        k = int(rx.integers(1, 9)); Zx = rx.normal(size=(3, k)) + 1j*rx.normal(size=(3, k)); gx = np.linalg.eigvalsh(Zx.conj().T @ eta @ Zx)
        bad += int((gx > 1e-9).sum() > 2 or (gx < -1e-9).sum() > 1)
    for _ in range(200):
        U = np.linalg.qr(rx.normal(size=(6, 6)) + 1j*rx.normal(size=(6, 6)))[0]
        d = np.array([rx.uniform(0.2, 3), rx.uniform(0.2, 3), -rx.uniform(0.2, 3), 0, 0, 0]); Gx = U @ np.diag(d) @ U.conj().T
        Zx = np.sqrt(np.abs(d[:3]))[:, None]*U[:, :3].conj().T; worst = max(worst, abs(Zx.conj().T @ eta @ Zx - Gx).max())
    z0 = np.array([1, 0, 1])/np.sqrt(2)
    _p39_say(f"500 random sets of 1 to 8 vectors of any kind: inertia beyond (2, 1) for {bad}.  200 random Hermitian 6 x 6 matrices with two "
             f"positive, one negative and three zero eigenvalues: each the relation matrix of six vectors of the channels "
             f"({_p39_lt(worst, 1e-12)}).  A null vector, (1, 0, 1)/sqrt 2, has the relation matrix ({abs(ip(z0, z0)):.0f}), as the zero vector "
             f"has: rebuilding from relations needs the vectors' span to carry the whole form.")
    ok_a = (inert == (2, 1, N - 3) and abs(r.fun + lam[0]) < 1e-6 and abs(abs(ip(um, vm)) - 1) < 1e-9 and np.abs(gnz - np.sort(lam)).max() < 1e-9
            and abs(abs(ip(zb, vm)) - 1) < 1e-9 and bad == 0 and worst < 1e-12 and [x < 0 for x in nrm] == [True, False, False])
    check(ok_a, "v41.0-1(a): the references' relation matrix has at most two positive and one negative eigenvalue, every such matrix is one; "
                "its nonzero eigenvalues are T's; T's one timelike eigenvector minimizes sum w |<z, u>|^2 and is G's negative mode")
    # (b) dust's energy frame
    e4 = np.diag([1.0, 1, 1, -1]); n = 4000
    v = rng.normal(size=(n, 3))*0.35; v[:, 0] += 0.3; v = v/np.maximum(1, np.linalg.norm(v, axis=1)[:, None]/0.95)
    gam = 1/np.sqrt(1 - (v**2).sum(1)); U = np.column_stack([gam[:, None]*v, gam]); m = rng.uniform(0.5, 2, n)
    T4 = (U.T*m) @ U @ e4; e, W = np.linalg.eig(T4); k = np.argmin(e.real); uL = W[:, k].real; uL /= np.sqrt(-(uL @ e4 @ uL)); uL *= np.sign(uL[3])
    uE = (m[:, None]*U).sum(0); uE /= np.sqrt(-(uE @ e4 @ uE))
    rho = [(m*(U @ e4 @ x)**2).sum()/m.sum() for x in (uL, uE, np.array([0, 0, 0, 1.0]))]
    sg4 = rng.choice([-1, 1], n); T4s = ((U*sg4[:, None]).T*m) @ (U*sg4[:, None]) @ e4
    fm0 = np.linalg.norm((m[:, None]*U).sum(0))/m.sum(); fm1 = np.linalg.norm((m[:, None]*U*sg4[:, None]).sum(0))/m.sum()
    es = np.sort(e.real)/m.sum()
    _p39_say(f"(b) Dust in Minkowski space, 4000 particles: the timelike eigenvector of T^mu_nu = sum m u^mu u_nu, the energy (Landau-Lifshitz) "
             f"frame, moves at ({uL[0]/uL[3]:.4f}, {uL[1]/uL[3]:.4f}, {uL[2]/uL[3]:.4f}), the first moment's frame at ({uE[0]/uE[3]:.4f}, "
             f"{uE[1]/uE[3]:.4f}, {uE[2]/uE[3]:.4f}); the eigenvalues over sum m {es[0]:.4f}, {es[1]:.4f}, {es[2]:.4f}, {es[3]:.4f}.  The energy "
             f"density sum m (u.w)^2/sum m seen from the energy frame {rho[0]:.5f}, the least; from the first moment's frame {rho[1]:.5f}; from "
             f"the lab {rho[2]:.5f}.  With u and -u identified (random signs) the first moment over sum m falls from {fm0:.3f} to {fm1:.3f} and T "
             f"is unchanged ({_p39_lt(abs(T4s - T4).max(), 1e-12)}).")
    check(rho[0] < rho[1] < rho[2] and abs(T4s - T4).max() < 1e-9, "v41.0-1(b): dust's T has one timelike eigenvector, the frame that sees the "
          "least energy density; the second moment survives the identification of u with -u, the first does not")
    # (c) one reference on Kerr-Newman's line
    M_, a, q, th = 1.0, 0.6, 0.5, np.pi/3; rE = M_ + np.sqrt(M_**2 - q**2 - a**2*np.cos(th)**2); rp = M_ + np.sqrt(M_**2 - a**2 - q**2)
    rows = []; ok_c = True
    for r_ in (3.0, rE, 0.5*(rE + rp)):
        z = np.array([r_ - 1j*a*np.cos(th) - M_, q, M_]); T1 = np.outer(z, z.conj()) @ eta; zz = ip(z, z).real
        dl = r_**2 - 2*M_*r_ + a*a + q*q - a*a*np.sin(th)**2
        ok_c &= abs(zz - dl) < 1e-12 and abs(T1 @ z - zz*z).max() < 1e-12
        rows.append(f"r = {r_:.6f}: <z, z> = {zz:+.6f}, Delta - a^2 sin^2 theta = {dl:+.6f}; Im z_1 z_3^* = {(z[0]*np.conj(z[2])).imag:+.4f}, "
                    f"Im z_1 z_2^* = {(z[0]*np.conj(z[1])).imag:+.4f}")
    z = np.array([rE - 1j*a*np.cos(th) - M_, q, M_]); T1 = np.outer(z, z.conj()) @ eta
    _p39_say(f"(c) One reference on Kerr-Newman's line, z = (s - M, q, M), s = r - i a cos theta, M = 1, a = 0.6, q = 0.5, theta = 60 deg, "
             f"T = z <z, .>: T z = <z, z> z ({'below 1e-12' if ok_c else 'FAILS'}); " + "; ".join(rows) + f" -- -M a cos theta = "
             f"{-M_*a*np.cos(th):+.4f} and -q a cos theta = {-q*a*np.cos(th):+.4f} at every radius.  On the stationary limit, r = {rE:.6f}: rank T = "
             f"{np.linalg.matrix_rank(T1, 1e-9)} and T^2 = 0 ({_p39_lt(abs(T1 @ T1).max(), 1e-12)}), a Jordan block: no timelike eigenvector.")
    ok_c &= np.linalg.matrix_rank(T1, 1e-9) == 1 and abs(T1 @ T1).max() < 1e-12
    check(ok_c, "v41.0-1(c): one reference's T has <z, z> as its eigenvalue on z, the line's Delta - a^2 sin^2 theta; on the stationary limit T "
                "is nilpotent and has no timelike eigenvector")
    # (d) the positive channels' block
    Q8 = np.array([[1, 0], [1j, 0], [0, 1], [0, 1j], [-1, 0], [-1j, 0], [0, -1], [0, -1j]], complex)
    def block(tilt, eps=0.0, Hp=None):
        zs = []
        for nq in Q8:
            dd = nq + tilt*np.array([1, 0]); dd = dd/np.linalg.norm(dd); zs.append(np.array([np.sinh(0.7)*dd[0], np.sinh(0.7)*dd[1], np.cosh(0.7)]))
        Zq = np.array(zs).T; Tq = (Zq @ Zq.conj().T) @ eta; e_, V_ = np.linalg.eig(Tq); k_ = np.argmin(e_.real); vb = V_[:, k_]
        vb /= np.sqrt(-ip(vb, vb).real); P = np.eye(3) - np.outer(vb, vb.conj() @ eta)/ip(vb, vb); Bq = P @ Tq @ P
        if Hp is not None: Bq = Bq + eps*Hp
        e2, V2 = np.linalg.eig(Bq); o2 = np.argsort(-e2.real); return e2.real[o2], V2[:, o2[0]]
    e0, _ = block(0.0); Hp = np.zeros((3, 3), complex); Hp[0, 1] = Hp[1, 0] = 1.0; rows = []
    for tilt in (0.3, 0.03, 0.003):
        eA, vA = block(tilt); eB, vB = block(tilt, 1e-4, Hp)
        ang = np.degrees(np.arccos(min(1, abs(np.vdot(vA, vB))/np.linalg.norm(vA)/np.linalg.norm(vB))))
        rows.append((tilt, eA[0] - eA[1], ang, np.degrees(1e-4/(eA[0] - eA[1]))))
    _p39_say(f"(d) Eight references whose directions in the positive channels are the quaternion units, +-1, +-i, +-j, +-k, at rapidity 0.7: on "
             f"the complement of their collective reference T's block has the eigenvalues {e0[0]:.6f} and {e0[1]:.6f}, the gap "
             f"{_p39_lt(abs(e0[0] - e0[1]), 1e-12)}: nothing selects a positive channel.  The directions tilted toward the first channel by " +
             "; ".join(f"{t_}: the gap {g_:.3g}, and a perturbation of 1e-4 turns the selected channel by {a_:.3f} deg (1e-4/gap = {d_:.3f} deg)"
                       for t_, g_, a_, d_ in rows) + ".")
    check(abs(e0[0] - e0[1]) < 1e-12 and rows[0][1] > rows[1][1] > rows[2][1] and rows[0][2] < rows[1][2] < rows[2][2],
          "v41.0-1(d): an even spread of references selects no positive channel; the smaller the gap the further a fixed perturbation turns the "
          "channel selected")
    # (h, computed here to keep the generator's order) constraints at symmetric configurations
    def rk_dJ(x, p):
        Jm = np.zeros((3, 6))
        for i in range(3):
            ei = np.zeros(3); ei[i] = 1; Jm[:, i] = np.cross(ei, p); Jm[:, 3 + i] = np.cross(x, ei)
        return np.linalg.matrix_rank(Jm, 1e-9)
    def stab(x, p):
        Gn = [np.array([[0, -c3[2], c3[1]], [c3[2], 0, -c3[0]], [-c3[1], c3[0], 0]]) for c3 in np.eye(3)]
        A = np.column_stack([np.r_[Gm @ x, Gm @ p] for Gm in Gn]); return 3 - np.linalg.matrix_rank(A, 1e-9)
    x = rng.normal(size=3); p = rng.normal(size=3)
    cases = [("generic (x, p)", x, p), ("x parallel to p", x, 2.5*x), ("x = p = 0", 0*x, 0*x)]
    hrow = [(nm, rk_dJ(x_, p_), stab(x_, p_)) for nm, x_, p_ in cases]
    # (e) the sphere of references
    def r4(e_): return np.array([e_[0].real, e_[0].imag, e_[1].real, e_[1].imag])
    Nb = 30; base = np.array([np.cos(0.4), np.exp(0.7j)*np.sin(0.4)]); es = []
    for _ in range(Nb):
        d_ = base + 0.25*(rng.normal(size=2) + 1j*rng.normal(size=2)); d_ /= np.linalg.norm(d_); es.append(d_*rng.choice([-1, 1]))
    es = np.array(es); wb = rng.uniform(0.5, 3, Nb)
    Mref = sum(w_*np.outer(r4(e_), r4(e_)) for w_, e_ in zip(wb, es))/wb.sum(); lm = np.sort(np.linalg.eigvalsh(Mref))[::-1]
    Sh = (es.T*wb) @ es.conj()/wb.sum(); lh, Vh = np.linalg.eigh(Sh); est = Vh[:, 1]
    Jm4 = np.zeros((4, 4)); Jm4[0, 1] = Jm4[2, 3] = -1; Jm4[1, 0] = Jm4[3, 2] = 1
    Mav = 0.5*(Mref + Jm4 @ Mref @ Jm4.T); herm = np.block([[Sh.real, -Sh.imag], [Sh.imag, Sh.real]])[np.ix_([0, 2, 1, 3], [0, 2, 1, 3])]/2
    def tilt2(e0_): return float((wb*(1 - abs(es.conj() @ e0_)**2)).sum()/wb.sum())
    rr = _P39_OPT.minimize(lambda p_: tilt2((p_[:2] + 1j*p_[2:])/np.linalg.norm(p_)), rng.normal(size=4), method="BFGS")
    fm = np.linalg.norm(sum(w_*r4(e_) for w_, e_ in zip(wb, es))/wb.sum())
    al_ = np.array([e_*np.sign((np.conj(base) @ e_).real) for e_ in es]); fma = np.linalg.norm(sum(w_*r4(e_) for w_, e_ in zip(wb, al_))/wb.sum())
    Sha = (al_.T*wb) @ al_.conj()/wb.sum()
    _p39_say(f"(e) Thirty bodies whose references cluster about (cos 0.4, e^(0.7 i) sin 0.4) in the positive channels, each on a random sheet: "
             f"the first moment's length {fm:.3f}; the real form on R^4 has the eigenvalues {lm[0]:.4f}, {lm[1]:.4f}, {lm[2]:.4f}, {lm[3]:.4f}, and "
             f"averaged over the circle of phases it is the Hermitian 2 x 2 form ({_p39_lt(abs(Mav - herm).max(), 1e-12)}), eigenvalues "
             f"{lh[1]:.4f} and {lh[0]:.4f}.  The mean squared charge-to-mass ratio, sin^2 of each body's tilt from a reference: from the "
             f"Hermitian form's principal reference {tilt2(est):.4f}, the least over all references ({rr.fun:.4f} by search); from the cluster's "
             f"center {tilt2(base):.4f}; from e_1 {tilt2(np.array([1, 0])):.4f}; from the best body's own reference "
             f"{min(tilt2(e_) for e_ in es):.4f}.  With every body on the center's sheet the first moment is {fma:.3f}, the Hermitian form the "
             f"same ({_p39_lt(abs(Sha - Sh).max(), 1e-12)}): the first moment keeps the sheets, the Hermitian form forgets them and the phase.")
    check(abs(tilt2(est) - rr.fun) < 1e-6 and abs(Mav - herm).max() < 1e-12 and abs(Sha - Sh).max() < 1e-12 and fma > fm,
          "v41.0-1(e): the Hermitian form's principal reference is the one from which the bodies' mean squared charge-to-mass ratio is least; the "
          "form forgets each body's sheet and phase, the first moment does not")
    # (f) the pole's form
    ps = np.linspace(0, np.pi, 20001)
    def ang(a_):
        wt = a_(np.cos(ps))*np.sin(ps)**2; n1 = (wt*np.cos(ps)**2).sum()/wt.sum(); return n1, (1 - n1)/3
    lines = []; okf = True
    for nm, a_ in (("a_0 = 1", lambda c_: 1 + 0*c_), ("a_2 = 1 + 2(n_1^2 - 1/4)", lambda c_: 1 + 2*(c_*c_ - 0.25))):
        n1, n2 = ang(a_); parts = []
        for dlt in (0.4, 0.2, 0.1, 0.05):
            t = np.linspace(dlt/2, dlt, 4001); wt = np.sin(t)**3; s2 = (wt*np.sin(t)**2).sum()/wt.sum()
            parts.append(f"delta = {dlt:.2f}: diag({1 - s2:.6f}; {s2*n1:.6f}, {s2*n2:.6f} x3), the transverse trace over delta^2 {s2/dlt**2:.4f}")
        lines.append(f"{nm}: " + "; ".join(parts) + f"; the transverse block over its trace ({n1:.4f}, {n2:.4f} x3) at every delta")
        okf &= abs(n1 - (0.25 if nm.startswith("a_0") else 0.375)) < 1e-6
    t = np.linspace(1e-4, 1.2, 20001); wt = np.sin(t)**3*np.exp(-t/0.3); n1a, _ = ang(lambda c_: 1 + 2*(c_*c_ - 0.25))
    prof = np.where(t < 0.3, n1a, 0.25); Mleaf = (wt*prof).sum()/wt.sum(); blk = (wt*np.sin(t)**2*prof).sum()/(wt*np.sin(t)**2).sum()
    _p39_say("(f) Matter near a pole p of the 4-sphere, Y = cos(theta) p + sin(theta) n, theta from delta/2 to delta with weight sin^3 theta, "
             "the angular profiles of Section XXIX.10(d): " + "; ".join(lines) + f"; the trace's limit (2/3)(63/64)/(15/16) = "
             f"{(2/3)*(63/64)/(15/16):.4f}.  A source whose profile changes with theta (a_2 inside 0.3, a_0 outside, weight e^(-theta/0.3)): the "
             f"leaf's <n_1^2> {Mleaf:.4f}, the transverse block normalized {blk:.4f}.")
    check(okf and abs(Mleaf - blk) > 1e-3, "v41.0-1(f): the pole's transverse block vanishes as delta^2 while its shape stays the profile's, "
          "0.25 or 0.375 at every delta; the leaf's form is the shape of each direction, not the normalized block")
    # (g) handedness
    kk = np.arange(2000) + 0.5; phi = np.arccos(1 - 2*kk/2000); lamb = np.pi*(1 + 5**0.5)*kk
    X = np.column_stack([np.cos(lamb)*np.sin(phi), np.sin(lamb)*np.sin(phi), np.cos(phi)]); rows = []
    for om in (0.5, -0.5):
        Pm = om*np.cross(np.array([0, 0, 1.0]), X); Zs = X + 1j*Pm; Shh = Zs.T @ Zs.conj()/2000
        rows.append((om, np.diag(X.T @ X)/2000, np.diag(Pm.T @ Pm)/2000, Shh[0, 1].imag, (X[:, 0]*Pm[:, 1] - X[:, 1]*Pm[:, 0]).mean()))
    def bloch(e_): return np.array([2*(np.conj(e_[0])*e_[1]).real, 2*(np.conj(e_[0])*e_[1]).imag, abs(e_[0])**2 - abs(e_[1])**2])
    trip = []
    for _ in range(3):
        E3 = rng.normal(size=(3, 2)) + 1j*rng.normal(size=(3, 2)); E3 /= np.linalg.norm(E3, axis=1)[:, None]
        bar = np.vdot(E3[0], E3[1])*np.vdot(E3[1], E3[2])*np.vdot(E3[2], E3[0]); b = [bloch(e_) for e_ in E3]
        om = 2*np.arctan2(np.dot(b[0], np.cross(b[1], b[2])), 1 + b[0] @ b[1] + b[1] @ b[2] + b[2] @ b[0]); trip.append((np.angle(bar), om/2))
    _p39_say(f"(g) Handedness.  z = x + i p on a shell of 2000 points rotating about the z axis: the position moments {rows[0][1][0]:.4f} each and "
             f"the momentum moments {rows[0][2][0]:.4f}, {rows[0][2][1]:.4f}, {rows[0][2][2]:.4f} for both senses; Im S_xy = {rows[0][3]:+.6f} for "
             f"omega = +0.5 and {rows[1][3]:+.6f} for -0.5, minus the angular momentum per particle, {rows[0][4]:+.6f} and {rows[1][4]:+.6f}.  Three "
             f"random triples of spin states: the phase of <e_1, e_2><e_2, e_3><e_3, e_1> " + ", ".join(f"{a_:+.6f}" for a_, _ in trip) +
             f", half the solid angle of their triangle on the sphere of rays ({_p39_lt(max(abs(a_ - b_) for a_, b_ in trip), 1e-12)}); "
             f"conjugating every state, the mirror, reverses it.")
    check(abs(rows[0][3] + rows[0][4]) < 1e-12 and abs(rows[1][3] + rows[1][4]) < 1e-12 and max(abs(a_ - b_) for a_, b_ in trip) < 1e-12,
          "v41.0-1(g): the Hermitian form's imaginary part is minus the angular momentum, and the loop product's phase is half the solid angle; "
          "the real positional form sees neither")
    # (h)
    ry = np.random.default_rng(5491); hm = 0.0
    for _ in range(50):
        Kx = ry.normal(size=(3, 3)) + 1j*ry.normal(size=(3, 3)); Kx = Kx - Kx.conj().T; Xg = eta @ Kx
        zx = ry.normal(size=3) + 1j*ry.normal(size=3); vx = ry.normal(size=3) + 1j*ry.normal(size=3)
        H_ = lambda z_: ((0.5j)*(np.conj(z_) @ eta @ (Xg @ z_))).real
        dH = (H_(zx + 1e-6*vx) - H_(zx - 1e-6*vx))/2e-6; om_ = ((np.conj(Xg @ zx)) @ eta @ vx).imag; hm = max(hm, abs(dH - om_))
    zx = ry.normal(size=3) + 1j*ry.normal(size=3); ph1 = ((0.5j)*(np.conj(zx) @ eta @ (1j*zx))).real
    _p39_say("(h) Constraints at symmetric configurations.  J = x cross p on (x, p) in R^6: " + "; ".join(
             f"{nm}, the rank of dJ {a_}, its stabilizer's dimension {b_}" for nm, a_, b_ in hrow) + " -- the rank is 3 less the stabilizer's "
             f"dimension, the range of dJ being the annihilator of the stabilizer's algebra (Arms, Marsden and Moncrief 1981).  On the three "
             f"channels, with omega(a, b) = Im <a, b>, H_X(z) = (i/2) <z, X z> for X in u(2, 1) has dH_X(v) = omega(X z, v) ({_p39_lt(hm, 1e-7)}, "
             f"50 random X, z, v): T is (-2i times) the sum of the references' momentum maps; for the phase rotation, X = i, H = -<z, z>/2 "
             f"({_p39_lt(abs(ph1 + 0.5*ip(zx, zx).real), 1e-12)}).")
    check([a_ for _, a_, _ in hrow] == [3, 2, 0] and [3 - b_ for _, _, b_ in hrow] == [3, 2, 0] and hm < 1e-7,
          "v41.0-1(h): dJ loses rank exactly by its stabilizer's dimension; Kinnersley's form is (minus twice) the phase rotation's momentum map "
          "and T a sum of the references' momentum maps")

# ---------------------------------------------------------------------------------------------------- v41.0-2: Entries 550-551
def v41_0_modes():
    """v41.0-2 (R618, Section XXXIX.5): Entries 550-551 -- modes, legibility and occupancy."""
    _p39_head("v41.0-2", "Entries 550-551: modes, legibility and occupancy -- the entropy over the sphere of references as the two horizons', a "
              "fixed form's four modes, the Boltzmann and the oscillating weightings, occupancy off a mode, the blow-up about an offset axis, the maps "
              "that keep the modes (Section XXXIX.5)")
    rng = np.random.default_rng(550)
    # (a) the entropy over the sphere of references (Section XXXVIII.3(f))
    def S(p, M, a): c0 = np.sqrt(M*M - a*a); return np.pi*((M + c0*np.cos(p))**2 + a*a*np.cos(p)**2)
    worst = 0; worst2 = 0; worst3 = 0
    for _ in range(200):
        M = rng.uniform(0.5, 3); a = rng.uniform(0, 1)*M; p = rng.uniform(0, np.pi); c0 = np.sqrt(M*M - a*a)
        worst = max(worst, abs(S(p, M, a) - (np.pi*M*M*(1 + np.cos(p)**2) + 2*np.pi*M*c0*np.cos(p)))/S(0, M, a))
        Q = M*np.sin(p); a1 = a*np.cos(p); rp = M + np.sqrt(max(M*M - Q*Q - a1*a1, 0)); rm = 2*M - rp
        Sp, Sm = np.pi*(rp*rp + a1*a1), np.pi*(rm*rm + a1*a1)
        worst2 = max(worst2, abs(S(p, M, a) + S(np.pi - p, M, a) - (Sp + Sm))/S(0, M, a), abs(Sp + Sm - 2*np.pi*M*M*(1 + np.cos(p)**2))/S(0, M, a))
        hi, lo = (S(p, M, a), S(np.pi - p, M, a)) if np.cos(p) >= 0 else (S(np.pi - p, M, a), S(p, M, a))
        worst3 = max(worst3, abs(hi - Sp)/S(0, M, a), abs(lo - Sm)/S(0, M, a))
    M, a = 1.0, 0.7; c0 = np.sqrt(M*M - a*a); h = 1e-5
    sl = (S(np.pi/2 + h, M, a) - S(np.pi/2 - h, M, a))/(2*h)
    _p39_say(f"(a) The entropy over the sphere of references of Section XXXVIII.3(f), S(p) = pi[(M + c_0 cos p)^2 + a^2 cos^2 p], c_0 = sqrt(M^2 - "
             f"a^2): S = pi M^2 (1 + cos^2 p) + 2 pi M c_0 cos p ({_p39_lt(worst, 1e-12)} on 200 random holes, relative); S at the tilt p is the "
             f"outer horizon's pi(r_+^2 + a^2 cos^2 p) of the tilted closing, and at pi - p the inner horizon's pi(r_-^2 + a^2 cos^2 p) "
             f"({_p39_lt(worst3, 1e-12)}), their sum 2 pi M^2 (1 + cos^2 p) ({_p39_lt(worst2, 1e-12)}): the part even under the sheet swap is the "
             f"two horizons' mean, the odd part half their difference.  M = 1, a = 0.7: S(0) = {S(0, M, a):.6f}, S(180 deg) = {S(np.pi, M, a):.6f}, "
             f"their sum {S(0, M, a) + S(np.pi, M, a):.6f} = 4 pi; the slope at 90 deg {sl:.6f} = -2 pi M c_0 = {-2*np.pi*M*c0:.6f}, the even part's "
             f"slope there 0; the even part {2*np.pi:.6f} at 0 deg and {np.pi:.6f} at 90 deg, its least; at a = M the odd part vanishes.")
    check(worst < 1e-12 and worst2 < 1e-12 and worst3 < 1e-12 and abs(sl + 2*np.pi*M*c0) < 1e-6,
          "v41.0-2(a): the entropy over the sphere of references is the outer horizon's at p and the inner's at pi - p; its even part, a second "
          "moment, is stationary at the ortho reference, where the whole is not unless a = M")
    # (b) a fixed form's modes
    lam = np.array([1.0, 0.6, 0.3, 0.0]); R0 = np.linalg.qr(rng.normal(size=(4, 4)))[0]; Mm = R0 @ np.diag(lam) @ R0.T; found = set()
    for _ in range(300):
        e = rng.normal(size=4); e /= np.linalg.norm(e); mu = rng.choice(lam) + 0.05*rng.normal()
        for _ in range(60):
            if np.linalg.norm(Mm @ e - (e @ Mm @ e)*e) < 1e-12: break
            y = np.linalg.lstsq(Mm - mu*np.eye(4) + 1e-14*np.eye(4), e, rcond=None)[0]; e = y/np.linalg.norm(y); mu = e @ Mm @ e
        found.add(int(np.argmin(abs(lam - mu))))
    idx = [int((lam > l).sum()) for l in lam]
    _p39_say(f"(b) F(e) = e.M e on the unit 3-sphere, M with eigenvalues 1, 0.6, 0.3, 0: 300 random starts of a Newton search end on the axes "
             f"{sorted(found)}, the four eigen-axes, the only critical points; the unstable directions at each, {idx}: one maximum, two saddles, one "
             f"minimum.")
    check(sorted(found) == [0, 1, 2, 3] and idx == [0, 1, 2, 3], "v41.0-2(b): a form with distinct eigenvalues has four modes, the axes, of "
          "Morse index 0, 1, 2, 3: one stable")
    # (c) the two weightings
    def quad(eps, n=220):
        x, wq = np.polynomial.legendre.leggauss(n); A_ = 0.5*np.pi*(x + 1); wa = 0.5*np.pi*wq; c = 2*np.pi*(np.arange(2*n) + 0.5)/(2*n)
        Zb = 0; Iz = 0; M2 = np.zeros(4)
        for a_, w_ in zip(A_, wa):
            b = A_[:, None]; cc = c[None, :]
            u = np.array([np.cos(a_) + 0*b + 0*cc, np.sin(a_)*np.cos(b) + 0*cc, np.sin(a_)*np.sin(b)*np.cos(cc), np.sin(a_)*np.sin(b)*np.sin(cc)])
            Fv = np.tensordot(lam, u*u, 1); mu_ = w_*np.sin(a_)**2*wa[:, None]*np.sin(b)*(2*np.pi/(2*n)) + 0*cc
            wt = np.exp((Fv - lam[0])/eps)*mu_; Zb += wt.sum(); M2 += (wt[None]*u*u).sum((1, 2)); Iz += (np.exp(1j*Fv/eps)*mu_).sum()
        return Zb, Iz, M2/Zb
    def sp(eps, ks):
        tot = 0
        for k in ks:
            d = np.delete(lam, k) - lam[k]; tot += 2*np.exp(1j*lam[k]/eps)*np.prod(np.sqrt(np.pi*eps/abs(d))*np.exp(1j*np.pi*np.sign(d)/4))
        return tot
    rows = []
    for eps in (0.04, 0.02):
        Zb, Iz, M2 = quad(eps); lap = 2*np.prod(np.sqrt(np.pi*eps/(lam[0] - lam[1:])))
        rows.append((eps, Zb/lap, M2, M2[1:]/(eps/(2*(lam[0] - lam[1:]))), Iz, 100*abs(sp(eps, range(4)) - Iz)/abs(Iz),
                     100*abs(sp(eps, [0]) - Iz)/abs(Iz), 100*abs(sp(eps, [1, 2, 3]) - Iz)/abs(Iz)))
    _p39_say("(c) The same F under two weightings on the 3-sphere, by Gauss-Legendre quadrature: " + "; ".join(
             f"epsilon = {r_[0]:.2f}: the Boltzmann sum of e^(F/epsilon) over the top mode's Gaussian {r_[1]:.4f}, the mean e_k^2 "
             f"({', '.join(f'{x:.4f}' for x in r_[2])}), the transverse spreads over epsilon/(2 gap) ({', '.join(f'{x:.3f}' for x in r_[3])}); the "
             f"oscillating sum of e^(i F/epsilon) {r_[4].real:+.6f}{r_[4].imag:+.6f}i, stationary phase with all four modes off by {r_[5]:.1f}%, "
             f"with the top mode only by {r_[6]:.0f}%, without it by {r_[7]:.0f}%" for r_ in rows) + ".  The Boltzmann weighting keeps one mode, "
             "the oscillating one all four.")
    check(all(abs(r_[1] - 1) < 0.07 and r_[5] < 2 and r_[6] > 50 for r_ in rows) and rows[1][1] < rows[0][1],
          "v41.0-2(c): under e^(F/epsilon) the top mode alone carries the sum as epsilon falls; under e^(iF/epsilon) every mode contributes")
    # (d) occupancy off the mode
    outs = []
    for k in (None, 20.0):
        if k is None: c, tq = 1.0, 0.0
        else:
            ch = np.linspace(0, np.pi, 200001); wt = np.exp(-k*np.sin(ch))*np.sin(ch)**2; wt[ch > np.pi/2] = 0; c = (wt*np.cos(ch)**2).sum()/wt.sum()
            tq = (1 - c)/3
        outs.append((k, tq, [((c - tq)*np.sin(np.radians(pd))*np.cos(np.radians(pd))/(c*np.cos(np.radians(pd))**2 + tq*np.sin(np.radians(pd))**2),
                              np.tan(np.radians(pd))) for pd in (10, 30, 60)]))
    psi = 0.6; uu = np.array([np.sinh(psi), 0, 0, np.cosh(psi)]); T = np.outer(uu, uu)
    _p39_say("(d) Occupancy off the mode: a form read in a frame turned by p, its cross term over its diagonal term, at p = 10, 30, 60 deg: " +
             "; ".join(("a point mass at the pole" if k is None else f"the source e^(-20 sin chi), transverse moment {tq:.5f}") + ": " +
                       ", ".join(f"{x:.4f} (tan p = {y:.4f})" for x, y in rs) for k, tq, rs in outs) +
             f" -- for a point mass the identity sin p cos p/cos^2 p.  Cold dust read from a frame at rapidity 0.6 from its own: momentum density "
             f"over energy density {T[0, 3]/T[3, 3]:.6f} = tanh 0.6 = {np.tanh(psi):.6f}.")
    check(all(abs(x - y) < 1e-12 for x, y in outs[0][2]), "v41.0-2(d): a point mass's form turned by p has the cross term tan p times its diagonal "
          "term, a trigonometric identity")
    # (e) the blow-up about an offset axis
    dl = 0.05; n = 400000
    th = dl/2 + (dl/2)*rng.random(n); wth = np.sin(th)**3; nn = rng.normal(size=(n, 4)); nn /= np.linalg.norm(nn, axis=1)[:, None]
    Y = np.column_stack([np.sin(th)[:, None]*nn, np.cos(th)]); w0 = wth; w2 = wth*(1 + 2*(nn[:, 0]**2 - 0.25))
    def leaf(p0, w_, ax=0):
        b = np.zeros(5); b[4] = np.cos(p0); b[ax] = np.sin(p0); Yp = Y - np.outer(Y @ b, b); Yp /= np.linalg.norm(Yp, axis=1)[:, None]
        return (Yp.T*w_) @ Yp/w_.sum()
    tab = []
    for r_ in (0, 0.25, 0.5, 1, 2, 4, 8, 16):
        A0 = leaf(r_*dl, w0); A2 = leaf(r_*dl, w2); B2 = leaf(r_*dl, w2, 1); e0 = np.linalg.eigvalsh(A0)
        tab.append((r_, e0[-1], np.linalg.eigvalsh(A2)[-1], np.linalg.eigvalsh(B2)[-1], np.linalg.norm(A0 - A2), np.sort(e0)[1]))
    _p39_say("(e) The blow-up about an axis offset by p_0 from a core of size delta = 0.05 on the 4-sphere, the two cores of Section XXIX.10(d) -- "
             "the largest moment of the image's form, the round core, the elongated core offset along its long axis and across it; the two cores' "
             "forms' difference; the round core's smallest nonzero moment: " + "; ".join(
             f"p_0/delta = {r_[0]:.2f}: {r_[1]:.3f}, {r_[2]:.3f}, {r_[3]:.3f}; {r_[4]:.4f}; {r_[5]:.4f}" for r_ in tab) + ".")
    check(tab[0][1] < 0.26 and tab[-1][1] > 0.99 and tab[-1][4] < 0.001 and tab[0][4] > 0.1 and tab[-1][5] > 0,
          "v41.0-2(e): about its own axis a core's image keeps its directional shape; offset by many core sizes every core images near one "
          "direction and the cores' difference fades, the form of full rank at every finite offset")
    # (f) the maps that keep the modes
    axes = R0; cnt = 0
    for perm in itertools.permutations(range(4)):
        for sg in itertools.product([-1, 1], repeat=4):
            P = np.zeros((4, 4))
            for i, j in enumerate(perm): P[j, i] = sg[i]
            gg = axes @ P @ axes.T; cnt += int(np.allclose(gg @ gg.T, np.eye(4)))
    gq = np.linalg.qr(rng.normal(size=(4, 4)))[0]; img = gq @ axes[:, 0]; resid = np.linalg.norm(Mm @ img - (img @ Mm @ img)*img)
    tt = np.linspace(0, np.pi/2, 7); res = [(lam[0] - lam[1])*np.sin(x)*np.cos(x) for x in tt]
    _p39_say(f"(f) The orthogonal maps that carry the set of modes to itself: the {cnt} signed permutations of the four axes, a finite group, which "
             f"keep the set and not F; a random rotation sends the top mode to a point whose residual |M e - (e.M e) e| is {resid:.3f}, not a mode; "
             f"along the turn from the top mode to the next the residual is (lambda_0 - lambda_1) sin x cos x: " + ", ".join(f"{x:.3f}" for x in res) +
             " at x = 0, 15, ..., 90 deg.")
    check(cnt == 384 and resid > 0.1 and max(res) > 0.19, "v41.0-2(f): the maps that keep the set of modes are 2^4 4! = 384; every continuous "
          "path between modes passes through points that are not")

# ---------------------------------------------------------------------------------------------------- v41.0-3: Entry 552 and the note after it
def v41_0_rays():
    """v41.0-3 (R619, Section XXXIX.6): Entry 552 and the message after it -- the leaf's rays in the form of the Born rule; with (e)-(f), the
    review of the replies to Entries 550-551 that came with Entry 552: legibility's entropy and asymmetry, and several modes from one ensemble."""
    _p39_head("v41.0-3", "Entry 552 and the message after it: the leaf's rays in the form of the Born rule -- a ray as a pair of spin states, its "
              "wave, incidence as equal transition probabilities, waves of higher spin, the relation forced on a sphere of labels, the reference's "
              "split, fields as matrices, the disk's form and the two Hopf fields, rays as involutions, the closing rule and the frame from one law; "
              "with the review of the replies to Entries 550-551: legibility's entropy and asymmetry, several modes from one ensemble (Sections "
              "XXXIX.5-6)")
    rng = np.random.default_rng(552); qm, qc = _p39_qm, _p39_qc; sx, sy, sz = _P39_S; I2 = np.eye(2)
    def mat(a): return a[0]*I2 - 1j*(a[1]*sx + a[2]*sy + a[3]*sz)
    def up(u): w_, V_ = np.linalg.eigh(u[0]*sx + u[1]*sy + u[2]*sz); return V_[:, 1]
    def ray():
        q = rng.normal(size=4); q /= np.linalg.norm(q); w = rng.normal(size=4); w -= (w @ q)*q; w /= np.linalg.norm(w)
        return q, w, qm(qc(q), w)[1:], qm(w, qc(q))[1:]
    def rot(x, u): return qm(qm(x, np.r_[0, u]), qc(x))[1:]
    # (a) a ray as a pair of spin states
    e1 = e2 = e3 = e4 = 0; par = 0
    for _ in range(200):
        q, w, u, v = ray(); Nn = mat(q) + 1j*mat(w); ku, kv = up(u), up(v)
        s = np.linalg.svd(Nn, compute_uv=False); e1 = max(e1, s[1]/s[0], abs(abs(kv.conj() @ Nn @ ku) - 2), abs((q @ q - w @ w) + 2j*(q @ w)))
        x = rng.normal(size=4); x /= np.linalg.norm(x); psi = (q + 1j*w) @ x; eta = np.arccos(min(1, np.hypot(q @ x, w @ x)))
        e2 = max(e2, abs(abs(psi)**2 - abs(kv.conj() @ mat(x) @ ku)**2), abs(abs(psi)**2 - (1 + rot(x, u) @ v)/2), abs(abs(psi)**2 - np.cos(eta)**2))
        par = max(par, abs((q + 1j*w) @ (-x) + psi))
        q2, w2, u2, v2 = ray(); ku2, kv2 = up(u2), up(v2)
        e3 = max(e3, abs(abs(ku.conj() @ ku2)**2 - (1 + u @ u2)/2), abs(abs(kv.conj() @ kv2)**2 - (1 + v @ v2)/2))
        f = lambda p: -np.hypot(q @ (c := np.cos(p[0])*q2 + np.sin(p[0])*w2), w @ c)
        dmin = min(np.arccos(min(1, -_P39_OPT.minimize(f, [t0], method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-15}).fun))
                   for t0 in (0, 1.5, 3, 4.5))
        dL, dR = np.arccos(np.clip(u @ u2, -1, 1)), np.arccos(np.clip(v @ v2, -1, 1)); e4 = max(e4, abs(dmin - abs(dL - dR)/2))
    _p39_say(f"(a) A ray of the leaf through q with unit tangent w, its lane labels u = q* w and v = w q* (Section XXXVIII.13(a)), 200 random rays: "
             f"the null vector q + i w of the complexified 4-space is 2|v><u| up to a phase, of rank one ({_p39_lt(e1, 1e-12)}); the ray's wave at "
             f"a point x, |(q + i w).x|^2 = |<v|x|u>|^2 = [1 + (R_x u).v]/2 = cos^2 of x's distance from the ray ({_p39_lt(e2, 1e-12)}); each label "
             f"sphere a Bloch sphere, |<u|u'>|^2 = (1 + u.u')/2 ({_p39_lt(e3, 1e-12)}); two rays' closest approach, by search, |d_L - d_R|/2 "
             f"({_p39_lt(e4, 1e-6)}): two rays meet exactly when the transition probability between their left labels equals that between their "
             f"right labels.  The wave is odd under x -> -x ({_p39_lt(par, 1e-12)}), so it lives on the 3-sphere, and its square on the leaf.")
    check(e1 < 1e-12 and e2 < 1e-12 and e3 < 1e-12 and e4 < 1e-6 and par < 1e-12, "v41.0-3(a): a ray is a pair of spin states; its wave's "
          "square is the Born probability cos^2 of the distance; rays meet exactly when their two labels' transition probabilities agree")
    # (b) waves of higher spin and their overlaps
    def s3grid(n=70):
        x, wg = np.polynomial.legendre.leggauss(n); a = 0.5*np.pi*(x + 1); wa = 0.5*np.pi*wg; c = 2*np.pi*(np.arange(2*n) + 0.5)/(2*n)
        A, B, C = np.meshgrid(a, a, c, indexing="ij"); W = (wa[:, None, None]*np.sin(A)**2)*(wa[None, :, None]*np.sin(B))*(2*np.pi/(2*n)) + 0*C
        P = np.array([np.cos(A), np.sin(A)*np.cos(B), np.sin(A)*np.sin(B)*np.cos(C), np.sin(A)*np.sin(B)*np.sin(C)])
        return P.reshape(4, -1), W.ravel()
    P, W = s3grid(); e5 = e6 = 0
    for n in (2, 4):
        for _ in range(4):
            q, w, u, v = ray(); q2, w2, u2, v2 = ray(); p1 = ((q + 1j*w) @ P)**n; p2 = ((q2 + 1j*w2) @ P)**n
            ov = abs((W*p1.conj()*p2).sum())/np.sqrt((W*abs(p1)**2).sum()*(W*abs(p2)**2).sum())
            e5 = max(e5, abs(ov - (((1 + u @ u2)/2)*((1 + v @ v2)/2))**(n/2)))
            dL, dR = np.arccos(np.clip(u @ u2, -1, 1)), np.arccos(np.clip(v @ v2, -1, 1))
            g = lambda z: -(np.hypot(q @ (y := z/np.linalg.norm(z)), w @ y)*np.hypot(q2 @ y, w2 @ y))
            best = max(-_P39_OPT.minimize(g, rng.normal(size=4), method="Nelder-Mead", options={"xatol": 1e-11, "fatol": 1e-14, "maxiter": 4000}).fun
                       for _ in range(6))
            e6 = max(e6, abs(best - np.cos(abs(dL - dR)/4)**2))
    _p39_say(f"(b) Waves of spin n/2, ((q + i w).x)^n, along two random rays: their normalized overlap on the 3-sphere, by Gauss-Legendre "
             f"quadrature, is (P_L P_R)^(n/2), P_L = (1 + u.u')/2 and P_R = (1 + v.v')/2, for n = 2 and 4 ({_p39_lt(e5, 1e-12)}), Schur's "
             f"orthogonality for matrix elements; the largest value anywhere of the product of two rays' wave amplitudes, by search, is cos^2 of "
             f"half their closest approach ({_p39_lt(e6, 1e-6)}), and for spin n/2 its power n: at closest approach " + ", ".join(
             f"{d} deg, {np.cos(np.radians(d)/2)**2:.4f} for n = 1 and {np.cos(np.radians(d)/2)**200:.4f} for n = 100" for d in (0, 5, 10, 20)) +
             " -- as n grows only rays that meet keep a cross term.")
    check(e5 < 1e-12 and e6 < 1e-6, "v41.0-3(b): two rays' waves overlap by the product of their labels' transition amplitudes; their pointwise "
          "product is at most cos^(2n) of half their closest approach")
    # (c) the relation on a sphere of labels
    pts = rng.normal(size=(300, 3)); pts /= np.linalg.norm(pts, axis=1)[:, None]; c = np.clip(pts @ pts.T, -1, 1); rel = []
    xg, wg = np.polynomial.legendre.leggauss(200)
    for nm, X_, fn in (("1", 1 + 0*c, lambda t: 1 + 0*t), ("u.u'", c, lambda t: t), ("(3(u.u')^2 - 1)/2", (3*c*c - 1)/2, lambda t: (3*t*t - 1)/2),
                       ("1 + u.u'", 1 + c, lambda t: 1 + t)):
        ev = np.linalg.eigvalsh(X_); cz = lambda x_: 0.0 if abs(x_) < 5e-5 else x_
        rel.append((nm, int((abs(ev) > 1e-8).sum()), cz(ev.min()), cz((wg*fn(xg)).sum()/2)))
    labs = pts[:7]
    _p39_say("(c) Section XXXV.33(d)'s argument with a sphere of labels in place of a ring: the relation's rank, least eigenvalue and constant "
             "mode (its mean over the sphere), on 300 random labels -- " + "; ".join(f"{nm}: rank {r_}, least eigenvalue {l_:+.3f}, constant "
             f"mode {m_:+.4f}" for nm, r_, l_, m_ in rel) + f".  The least rank without a constant mode, normalized, is u.u', and it is positive: "
             f"with it the doubled count of a set of labels is the squared length of their sum, {(labs @ labs.T).sum():.6f} = "
             f"{np.linalg.norm(labs.sum(0))**2:.6f} for seven; two labels at 0, 90 and 180 deg count {2 + 2*1:.1f}, {2 + 0:.1f} and {2 - 2:.1f}: "
             f"agreement, a quarter turn, opposition.")
    check([r_ for _, r_, _, _ in rel] == [1, 3, 5, 4] and abs(rel[1][3]) < 1e-12 and rel[1][2] > -1e-9, "v41.0-3(c): on a sphere of labels the "
          "normalized relation of least rank without a constant mode is u.u', of rank 3, and positive")
    # (d) the reference's split
    e7 = e8 = 0; ki = np.array([1.0, 0, 0])
    for _ in range(200):
        q, w, u, v = ray(); XL = qm(np.array([0, 1.0, 0, 0]), q); XR = qm(q, np.array([0, 1.0, 0, 0]))
        e7 = max(e7, abs(w @ XL - v @ ki), abs(w @ XR - u @ ki))
        q2, w2, u2, v2 = ray(); up_, up2 = u - (u @ ki)*ki, u2 - (u2 @ ki)*ki
        e8 = max(e8, abs(u @ u2 - ((u @ ki)*(u2 @ ki) + np.linalg.norm(up_)*np.linalg.norm(up2)*np.cos(np.arctan2(u[2], u[1]) - np.arctan2(u2[2], u2[1])))))
    k3 = np.array([1.0, 0, 0]); parm = np.outer(pts @ k3, pts @ k3); trm = c - parm
    rp_, rt_ = int((abs(np.linalg.eigvalsh(parm)) > 1e-8).sum()), int((abs(np.linalg.eigvalsh(trm)) > 1e-8).sum())
    lst_ = min(np.linalg.eigvalsh(parm).min(), np.linalg.eigvalsh(trm).min())
    _p39_say(f"(d) The reference's split: a ray's lane momenta, <w, X_L> and <w, X_R> with X_L(q) = i q and X_R(q) = q i, are its labels' "
             f"components along the selected axis, v.i and u.i ({_p39_lt(e7, 1e-12)}, 200 rays); with that axis u.u' = p p' + |u_perp||u'_perp| "
             f"cos(Delta phi) ({_p39_lt(e8, 1e-12)}), the relation of rank 3 split into a part of rank {rp_}, the momenta's product, and one of rank "
             f"{rt_}, a cosine of the angle about the axis; both positive semidefinite, the least eigenvalue of either "
             f"{'above' if lst_ > -1e-12 else 'not above'} -1e-12.")
    check(e7 < 1e-12 and e8 < 1e-12 and (rp_, rt_) == (1, 2) and lst_ > -1e-12, "v41.0-3(d): the selected axis splits the labels' relation into "
          "the lane momenta's "
          "product, of rank 1, and a cosine about the axis, of rank 2")
    # (e) fields as matrices
    def grid(n):
        mons = [(a, b, c_, n - a - b - c_) for a in range(n + 1) for b in range(n + 1 - a) for c_ in range(n + 1 - a - b)]
        idx = {m: i for i, m in enumerate(mons)}
        low = [(a, b, c_, n - 2 - a - b - c_) for a in range(n - 1) for b in range(n - 1 - a) for c_ in range(n - 1 - a - b)]
        il = {m: i for i, m in enumerate(low)}; Lp = np.zeros((len(low), len(mons)))
        for (a, b, c_, d), i in idx.items():
            if a and b: Lp[il[(a - 1, b - 1, c_, d)], i] += a*b
            if c_ and d: Lp[il[(a, b, c_ - 1, d - 1)], i] += c_*d
        out = {}
        for (a, b, c_, d) in mons: out.setdefault((a - b + c_ - d, a - b - c_ + d), []).append(idx[(a, b, c_, d)])
        return {k: len(v) - np.linalg.matrix_rank(Lp[:, v]) for k, v in out.items()}
    gr = {}
    for n in (2, 4):
        g = grid(n); g = {k: v for k, v in g.items() if v}; gr[n] = (sum(g.values()), set(g.values()) == {1} and len(g) == (n + 1)**2,
                                                                   sum(1 for k in g if k[0] == k[1]))
    _p39_say("(e) Fields on the 3-sphere as matrices, in the complex coordinates z_1, z_2 and their conjugates, each harmonic of degree n labeled by "
             "its weights (m_L, m_R) under the two Hopf rotations: " + "; ".join(f"degree {n}: {a_} harmonics = (n + 1)^2, one for each pair of "
             f"weights from -n to n in steps of 2 ({'each pair once' if b_ else 'NOT'}), with the lanes in step, m_L = m_R, {c_}"
             for n, (a_, b_, c_) in gr.items()) + ".  Only even "
             "degrees descend to the leaf as functions.")
    check(all(gr[n][0] == (n + 1)**2 and gr[n][1] and gr[n][2] == n + 1 for n in gr), "v41.0-3(e): the harmonics of degree n are (n + 1) x "
          "(n + 1) matrices, the lanes acting on the two indices")
    # (f) the disk's form and the two Hopf fields
    Rr = np.linalg.qr(rng.normal(size=(4, 4)))[0]
    ch = np.linspace(0, np.pi/2, 4001); wt = np.exp(-10*np.sin(ch))*np.sin(ch); cc = (wt*np.cos(ch)**2).sum()/wt.sum(); tt = (1 - cc)/2
    Md = Rr @ np.diag([tt, tt, cc, 0]) @ Rr.T; lm, Vm = np.linalg.eigh(Md); o = np.argsort(lm); lm, Vm = lm[o], Vm[:, o]
    pair = [i for i in range(4) if min(abs(lm[i] - lm[j]) for j in range(4) if j != i) < 1e-9]; rest = [i for i in range(4) if i not in pair]
    J1 = np.outer(Vm[:, pair[1]], Vm[:, pair[0]]) - np.outer(Vm[:, pair[0]], Vm[:, pair[1]])
    J2 = np.outer(Vm[:, rest[1]], Vm[:, rest[0]]) - np.outer(Vm[:, rest[0]], Vm[:, rest[1]])
    XLt = np.zeros((4, 4)); XLt[1, 0] = 1; XLt[0, 1] = -1; XLt[3, 2] = 1; XLt[2, 3] = -1; XRt = XLt.copy(); XRt[3, 2] = -1; XRt[2, 3] = 1
    A, B = Rr @ XLt @ Rr.T, Rr @ XRt @ Rr.T
    dev = min(max(np.abs(s1*(J1 + s2*J2) - A).max(), np.abs(s3*(J1 - s2*J2) - B).max()) for s1 in (1, -1) for s2 in (1, -1) for s3 in (1, -1))
    c1_, c2_ = np.abs(Md @ (A + B) - (A + B) @ Md).max(), np.abs(Md @ (A - B) - (A - B) @ Md).max()
    _p39_say(f"(f) A thin disk e^(-10 sin chi) in a great sphere placed at random on the leaf, its form's eigenvalues {tt:.4f}, {tt:.4f}, {cc:.4f}, 0: "
             f"the unit rotations of the plane of its equal pair and of the plane of the rest, J_1 and J_2, give J_1 + J_2 and J_1 - J_2, Section "
             f"XXXVIII.12's X_L and X_R up to sign ({_p39_lt(dev, 1e-12)}); the form commutes with X_L + X_R, the disk's rotation "
             f"({_p39_lt(c1_, 1e-12)}), and not with X_L - X_R, the shift along its axis (by {c2_:.3f}).  Which of the two is the left-handed one the "
             f"real form does not fix.")
    check(dev < 1e-12 and c1_ < 1e-12 and c2_ > 0.1, "v41.0-3(f): a disk's own second-moment form selects the pair of Hopf fields of Section "
          "XXXVIII.12, its hinge and its dual circle, up to orientation")
    # (g) legibility's entropy and asymmetry (the review of the replies to Entries 550-551)
    def rho(ax, lm_):
        k = np.array([np.cos(ax/2), np.sin(ax/2)]); k2 = np.array([-np.sin(ax/2), np.cos(ax/2)]); return lm_*np.outer(k, k) + (1 - lm_)*np.outer(k2, k2)
    ent = []
    for lm_ in (0.5, 0.75, 0.931, 0.99, 1.0):
        ev = np.array([lm_, 1 - lm_]); ev = ev[ev > 0]; ent.append((lm_, abs(-(ev*np.log(ev)).sum())))
    ra, rb = rho(0.0, 0.99), rho(np.radians(60), 0.7); ka = np.array([1.0, 0]); kb = np.array([np.cos(np.radians(30)), np.sin(np.radians(30))])
    _p39_say("(g) Legibility as a normalized reference form of two eigenvalues: its entropy " + ", ".join(f"{e_:.4f} at ({l_:.3f}, {1 - l_:.3f})"
             for l_, e_ in ent) + f" -- ln 2 = {np.log(2):.4f} when nothing is selected, 0 when the selection is sharp.  A sharp conditioning "
             f"(0.99) and a broad one (0.70) whose axes are 60 deg apart on the sphere of rays: <b|rho_a|b> = {kb @ ra @ kb:.4f}, <a|rho_b|a> = "
             f"{ka @ rb @ ka:.4f}; both sharp, {(ka @ kb)**2:.4f} both ways.")
    check(abs(kb @ ra @ kb - ka @ rb @ ka) > 0.1 and abs(ent[0][1] - np.log(2)) < 1e-12, "v41.0-3(g): legibility read through a conditioning is "
          "symmetric between equally sharp conditionings and not otherwise")
    # (h) several stable modes from one ensemble
    c1 = np.array([1.0, 0, 0, 0]); c2 = np.array([np.cos(np.radians(70)), np.sin(np.radians(70)), 0, 0]); refs = []; ws = []
    for cen, wgt in ((c1, 0.6), (c2, 0.4)):
        for _ in range(40):
            d = cen + 0.14*rng.normal(size=4); refs.append(d/np.linalg.norm(d)); ws.append(wgt/40)
    refs = np.array(refs); ws = np.array(ws); modes = []
    for n in (1, 2, 3, 4, 8, 16, 64):
        ends = []
        for _ in range(300):
            e = rng.normal(size=4); e /= np.linalg.norm(e)
            for _ in range(4000):
                gr_ = (2*n*ws*(refs @ e)**(2*n - 1)) @ refs; gr_ -= (gr_ @ e)*e
                if np.linalg.norm(gr_) < 1e-13*max(1e-300, (ws*(refs @ e)**(2*n)).sum()): break
                e2_ = e + 0.5*gr_/max(1e-300, (ws*(refs @ e)**(2*n)).sum())/n; e = e2_/np.linalg.norm(e2_)
            if not any(abs(e @ x) > 1 - 1e-6 for x in ends): ends.append(e)
        ang = sorted(float(np.degrees(np.arccos(min(1, abs(e @ c1))))) for e in ends)
        modes.append((n, len(ends), ang))
    _p39_say("(h) Several stable modes from one ensemble: F_n(e) = sum_a w_a (e.e_a)^(2n) for two clusters of 40 references each, 70 deg apart, "
             "weights 0.6 and 0.4, spread 0.14; local maxima found by ascent from 300 random starts, at their angles from the first cluster: " +
             "; ".join(f"n = {n}: {k}" + (f", at {', '.join(f'{a_:.1f}' for a_ in an)} deg" if k <= 2 else "") for n, k, an in modes) +
             " -- the quadratic form, n = 1, has one; higher moments resolve the two clusters, and at n = 64 the references themselves.")
    check([k for _, k, _ in modes][:6] == [1, 1, 2, 2, 2, 2] and modes[-1][1] > 2, "v41.0-3(h): one ensemble's second moment has one stable mode; its "
          "higher moments have one for each cluster")
    # (i) the closing rule and the frame from one law
    def turn(x, th): z2 = (x[2] + 1j*x[3])*np.exp(1j*th); return np.array([x[0], x[1], z2.real, z2.imag])
    nH = 6; q, w, u, v = ray(); Nv = q + 1j*w; xs = [y/np.linalg.norm(y) for y in rng.normal(size=(5, 4))]; th = 2*np.pi*np.arange(256)/256; rows = []
    for kap in (0.0, 1.0, 4.0, 100.0):
        P_ = np.exp(kap*np.cos(th)); P_ /= P_.sum(); worst = 0
        for x in xs:
            vals = np.array([(Nv @ turn(x, t))**nH for t in th]); comp = np.fft.fft(vals)/256
            avg = (P_*vals).sum(); pred = sum(comp[k]*(_P39_SP.iv(abs(k if k <= 128 else k - 256), kap)/_P39_SP.iv(0, kap)) for k in range(256))
            worst = max(worst, abs(avg - pred))
        rows.append((kap, [_P39_SP.iv(k, kap)/_P39_SP.iv(0, kap) for k in (1, 2, 3)], worst))
    lab = np.arange(12); m12 = (np.exp(np.cos(2*np.pi*lab/12))*np.exp(2j*np.pi*lab/12)).sum()/np.exp(np.cos(2*np.pi*lab/12)).sum()
    _p39_say("(i) The closing rule and the frame from one law: the reference spread about the hinge's axis by a von Mises law of concentration "
             "kappa; a field's part whose lanes are q steps out of step survives the average by I_q(kappa)/I_0(kappa), checked on a ray's wave "
             "of degree 6 at five points -- " + "; ".join(f"kappa = {k_:.1f}: frame order {s_[0]:.4f}; out of step by 1, 2, 3, {s_[0]:.4f}, "
             f"{s_[1]:.4f}, {s_[2]:.4f} ({_p39_lt(w_, 1e-12)})" for k_, s_, w_ in rows) + f".  For q = 1 the survival is the frame's own order "
             f"parameter, Section XXXV.40's K = M on the leaf; at kappa = 1 on twelve labels the order is {abs(m12):.6f}, that section's aligned "
             f"room's |M|, and I_1(1)/I_0(1) = {_P39_SP.iv(1, 1)/_P39_SP.iv(0, 1):.6f}, its square {(_P39_SP.iv(1, 1)/_P39_SP.iv(0, 1))**2:.6f}.  The "
             f"average removes cross terms between lanes out of step; the intensities, the squared moduli, it keeps.")
    check(all(w_ < 1e-12 for _, _, w_ in rows) and abs(abs(m12) - 0.446390) < 5e-7, "v41.0-3(i): averaging the reference over a circle multiplies "
          "the part q steps out of step by the law's q-th characteristic value; for q = 1 it is the frame's order parameter")
    # (j) rays and points as involutions
    def lin(f_): return np.array([f_(e) for e in np.eye(4)]).T
    def angs(Mx): a = np.sort(abs(np.angle(np.linalg.eigvals(Mx)))); return a[0], a[-1]
    pq = lambda a3: np.r_[0, a3]; w1 = w2 = w3 = w4 = 0; fx = 0
    for _ in range(200):
        q, w, u, v = ray(); H = lin(lambda x: qm(qm(pq(v), x), pq(u)))
        x_on = np.cos(0.7)*q + np.sin(0.7)*w; z = rng.normal(size=4); z -= (z @ q)*q + (z @ w)*w; z /= np.linalg.norm(z)
        w1 = max(w1, np.abs(H @ H - np.eye(4)).max(), np.linalg.norm(H @ x_on + x_on), np.linalg.norm(H @ z - z))
        fx = max(fx, abs(np.linalg.matrix_rank(H + np.eye(4), 1e-9) - 2), abs(np.linalg.matrix_rank(H - np.eye(4), 1e-9) - 2))
        q2, w2_, u2, v2 = ray(); H2 = lin(lambda x: qm(qm(pq(v2), x), pq(u2))); a0, a1 = angs(H2 @ H)
        dL, dR = np.arccos(np.clip(u @ u2, -1, 1)), np.arccos(np.clip(v @ v2, -1, 1)); t1, t2 = sorted([abs(dL - dR), min(dL + dR, 2*np.pi - dL - dR)])
        w2 = max(w2, abs(a0 - t1), abs(a1 - t2))
        d = rng.uniform(0.1, 1.4); qb = np.cos(d)*q + np.sin(d)*w; S1 = lin(lambda x: qm(qm(q, qc(x)), q)); S2 = lin(lambda x: qm(qm(qb, qc(x)), qb))
        ev_ = np.r_[np.cos(d), np.sin(d)*v]; eu_ = np.r_[np.cos(d), np.sin(d)*u]; Tm = lin(lambda x: qm(qm(ev_, x), eu_))
        w3 = max(w3, np.abs(S2 @ S1 - Tm).max(), np.linalg.norm(S2 @ S1 @ q - (np.cos(2*d)*q + np.sin(2*d)*w)))
        wm = rng.normal(size=4); wm -= (wm @ q)*q; wm /= np.linalg.norm(wm); Hm = lin(lambda x: qm(qm(pq(qm(wm, qc(q))[1:]), x), pq(qm(qc(q), wm)[1:])))
        w4 = max(w4, angs(Hm @ H)[0])
    Sg = lin(lambda x: qm(qm(pq(k3), x), pq(k3))); rows = []
    for _ in range(2000):
        q, w, u, v = ray(); H = lin(lambda x: qm(qm(pq(v), x), pq(u))); ev = np.linalg.eigvals(H @ Sg)
        dLk, dRk = np.arccos(np.clip(u @ k3, -1, 1)), np.arccos(np.clip(v @ k3, -1, 1))
        rows.append((min(abs(dLk - dRk), abs(np.pi - dLk - dRk)), min(np.abs(np.abs(np.angle(ev)) - c0).min() for c0 in (0, np.pi))))
    rows = np.array(rows)
    _p39_say(f"(j) Rays and points as involutions of the leaf, 200 random pairs: a ray's half-turn x -> v x u, its two labels acting from the two "
             f"sides, is an involution that is -1 on the ray's plane and +1 on the polar plane ({_p39_lt(w1, 1e-12)}), each a ray of the leaf: it "
             f"fixes two rays, the ray and its polar, and the sign says which (eigenspaces of dimension two, {'every time' if fx == 0 else 'NOT'}). "
             f" Two rays' half-turns composed are a double turn by d_L - d_R and d_L + d_R, the two labels' separations ({_p39_lt(w2, 1e-12)}); "
             f"the first is twice the closest approach, zero for rays through one point ({_p39_lt(w4, 1e-12)}).  Two points' symmetries x -> q x* q "
             f"composed are the shift by twice their distance along the ray joining them, a left turn about v and a right turn about u, one lane "
             f"each ({_p39_lt(w3, 1e-12)}).  The reference's involution x -> i x i, -1 on the hinge's plane and +1 on the dual circle's, diag "
             f"{np.round(np.diag(Sg), 0).astype(int).tolist()}: composed with a ray's half-turn it has a fixed point on the leaf exactly when "
             f"min(|d_L - d_R|, |pi - d_L - d_R|) = 0, the labels' angles d from the axis -- when the ray meets the hinge (p_2 = 0) or the dual "
             f"circle (p_1 = 0) ({_p39_lt(np.abs(rows[:, 1] - rows[:, 0]).max(), 1e-12)}, 2000 rays).")
    check(w1 < 1e-12 and fx == 0 and w2 < 1e-12 and w3 < 1e-12 and w4 < 1e-12 and np.abs(rows[:, 1] - rows[:, 0]).max() < 1e-12,
          "v41.0-3(j): rays and points are involutions of the leaf; composing two gives the lanes' separations as turns; a ray meets the hinge or "
          "the dual circle exactly when its involution composed with the reference's has a fixed point")
    # (k) the two lanes' overlap at a point (the second response to Entry 552)
    rz = np.random.default_rng(5521); wk = 0
    for _ in range(200):
        z = rz.normal(size=2) + 1j*rz.normal(size=2); z /= np.linalg.norm(z); tau = rz.uniform(0, 2*np.pi)
        UL = np.exp(1j*tau)*z; UR = np.array([np.exp(1j*tau)*z[0], np.exp(-1j*tau)*z[1]]); K = np.vdot(UR, UL)
        wk = max(wk, abs(K - (abs(z[0])**2 + np.exp(2j*tau)*abs(z[1])**2)), abs(np.linalg.norm(UL - UR)**2 - 2*(1 - K.real)))
    kv = [np.cos(e_)**2 + np.exp(2j*np.pi/2)*np.sin(e_)**2 for e_ in (0, np.pi/4, np.pi/2)]
    _p39_say(f"(k) The two lanes' flows at one point z = (z_1, z_2), U_L(tau) z = e^(i tau) z and U_R(tau) z = (e^(i tau) z_1, e^(-i tau) z_2): their "
             f"overlap <U_R z, U_L z> = |z_1|^2 + e^(2 i tau) |z_2|^2 and |U_L z - U_R z|^2 = 2(1 - Re K) ({_p39_lt(wk, 1e-12)}, 200 points); at "
             f"tau = 90 deg, K = {kv[0].real:+.0f}, {abs(kv[1]):.0f}, {kv[2].real:+.0f} at eta = 0, 45 and 90 deg from the hinge -- the lanes equal, "
             f"orthogonal, and opposite, the last the same point of the leaf with the lifts differing by a sign.")
    check(wk < 1e-12, "v41.0-3(k): the lanes' overlap at a point carries their separation and their relative phase together")

# ---------------------------------------------------------------------------------------------------- v41.0-4: the orbit across the equator
def v41_0_orbit():
    """v41.0-4 (R620, Section XXXIX.7): the orbit across the leaf's equator -- the speeds, the returning half, the two-armed resonance."""
    _p39_head("v41.0-4", "The orbit across the leaf's equator: the leaf's speed and the chart's, the returning half as the mirror image, the "
              "two-armed resonance and its width (Section XXXIX.7)")
    sp = []
    for t in (2.0, 5.0, 30.0):
        ch = np.arctan(t); Om = np.sqrt((1 + 2*np.sin(ch)**2)/np.sin(ch)**3); sp.append((t, Om, Om*np.sin(ch), Om*np.tan(ch), Om*np.sin(ch)*np.cos(ch)))
    _p39_say("(a) Circular orbits around Law I's point mass (Section XXXVIII.48(a)), at R = 2, 5 and 30 ell, units ell and GM/ell: the angular "
             "speed Omega; the leaf's own speed Omega sin chi, which the archive reads out at R, its point-mass curve; the chart's coordinate speed "
             "R Omega = Omega tan chi, which keeping the angular speed through the readout would give, as Section XXXVIII.42(c)'s rule does through "
             "a push; and Omega sin chi cos chi, which Section XXXVIII.42(d)'s weak-field law would give applied to the readout's own stretch, "
             "R/(ell sin chi) = 1/cos chi: " + "; ".join(f"{a_:.0f} ell: {b_:.4f}, {c_:.4f}, {d_:.4f}, {e_:.4f}" for a_, b_, c_, d_, e_ in sp) +
             f" -- the leaf's speed tends to sqrt 3 = {np.sqrt(3):.4f}, the chart's grows as R, the ratio 1/cos chi.")
    check(all(abs(d_/c_ - np.sqrt(1 + a_*a_)) < 1e-12 for a_, b_, c_, d_, e_ in sp), "v41.0-4(a): the chart's coordinate speed is the leaf's "
          "speed over cos chi")
    L = np.sqrt(2.0); Ec = L*L/2 + 1; chp, so = _p39_half(Ec + 0.05, L); t0 = so.t_events[0][0]; ph0 = so.sol(t0)[2]; tend = so.t_events[1][0]
    worst = 0; pit = []
    for tau in np.linspace(0.05, min(t0, tend - t0)*0.98, 40):
        a_, b_ = so.sol(t0 - tau), so.sol(t0 + tau); Ra, Rb = np.tan(a_[0]), np.tan(np.pi - b_[0]); pa, pb = a_[2], b_[2] + np.pi
        worst = max(worst, abs(Ra - Rb)/Ra, abs(np.angle(np.exp(1j*(pa + pb - 2*ph0 - np.pi)))))
        pit.append((np.degrees(np.arctan2(a_[1]/(np.sin(a_[0])*np.cos(a_[0])), L/np.sin(a_[0])**2)),
                    np.degrees(np.arctan2(b_[1]/(np.sin(b_[0])*np.cos(b_[0])), L/np.sin(b_[0])**2))))
    mir = np.degrees(ph0) % 180 + 90 if np.degrees(ph0) % 180 < 90 else np.degrees(ph0) % 180 - 90
    _p39_say(f"(b) An orbit with L^2 = 2 and energy 0.05 above the critical, L^2/2 + 1, the effective potential's value at the equator: its "
             f"pericenter at {np.tan(chp):.3f} ell; it reaches the equator, visible infinity, after turning {np.degrees(ph0):.1f} deg and returns "
             f"from the opposite side of the sky, the twin hemisphere read through the antipodal identification.  The returning half is the mirror "
             f"image of the outgoing half about the line at {mir:.1f} deg (radii and angles {_p39_lt(worst, 1e-8)}): its pitch at one radius "
             f"{pit[len(pit)//2][0]:+.1f} deg out and {pit[len(pit)//2][1]:+.1f} deg back.")
    rows = [(dE, np.degrees(_p39_sweep(Ec + dE, L))) for dE in (1.0, 0.3, 0.05, 0.01)]
    Er = _P39_OPT.brentq(lambda E: _p39_sweep(E, L) - 2*np.pi, Ec + 0.01, Ec + 1.0)
    sw2 = np.degrees(_p39_sweep(3.0 + 1e-4, 2.0))
    _p39_say("(c) The turn between the pericenter near the pole and the twin pericenter near the antipodal pole, on the 3-sphere, and so between "
             "successive pericenters in the readout, that turn plus 180 deg: " + "; ".join(f"E - E_c = {d_:.2f}: {s_:.1f} deg and {(s_ + 180) % 360:.1f}"
             f" deg" for d_, s_ in rows) + f".  The turn is a whole one at E - E_c = {Er - Ec:.4f}: there one particle's successive inward passes "
             f"come in along two opposite arms of one hand, and its outward passes along two of the other.  For L = 2, whose orbits all cross the "
             f"equator, a small swing turns by {sw2:.2f} deg against the small-amplitude 180 L/sqrt(L^2 - 3) = {180*2/np.sqrt(1.0):.2f} deg.")
    win = []
    for L2 in (1.0, 2.0, 2.8):
        L_ = np.sqrt(L2); Ec_ = L2/2 + 1; sw = lambda E: np.degrees(_p39_sweep(E, L_))
        Er_ = _P39_OPT.brentq(lambda E: sw(E) - 360, Ec_ + 1e-3, Ec_ + 3.0)
        lo = _P39_OPT.brentq(lambda E: sw(E) - 370, Ec_ + 1e-3, Er_); hi = _P39_OPT.brentq(lambda E: sw(E) - 350, Er_, Ec_ + 3.0)
        chp_, so_ = _p39_half(Er_, L_); chq = so_.sol(so_.t_events[1][0])[0]
        win.append((L2, Er_ - Ec_, lo - Ec_, hi - Ec_, np.degrees(chp_), np.degrees(chq)))
    _p39_say("(d) The resonance's width: " + "; ".join(f"L^2 = {a_:.1f}: opposite arms at E - E_c = {b_:.4f}, within 10 deg of opposite for E - E_c "
             f"from {c_:.4f} to {d_:.4f}; its pericenters at {e_:.1f} and {f_:.1f} deg from the pole" for a_, b_, c_, d_, e_, f_ in win) +
             " -- off the poles: the centrifugal barrier keeps every orbit with L away from them.")
    check(worst < 1e-8 and abs(pit[len(pit)//2][0] + pit[len(pit)//2][1]) < 1e-6 and all(c_ < b_ < d_ for _, b_, c_, d_, _, _ in win),
          "v41.0-4(b)-(d): an orbit across the equator returns from the opposite side as the mirror image of its outward half; at one energy for "
          "each L successive inward passes are opposite, within 10 deg over a band of energy")

# ---------------------------------------------------------------------------------------------------- v41.0-5: Entry 554
def v41_0_ortho():
    """v41.0-5 (R621, Section XXXIX.8): Entry 554 -- the ortho image of a galaxy."""
    _p39_head("v41.0-5", "Entry 554: the ortho image of a galaxy -- the Hopf quotient and the two lanes, the tilted quotient's ring and its Legendre "
              "factors, a two-armed disk read through a tilt, which pair of directions is forgotten and time's survival, the averaged quotient of a "
              "squashed shell, a tilt of the reference (Section XXXIX.8)")
    rng = np.random.default_rng(554); qm, qc, ex = _p39_qm, _p39_qc, _p39_ex; I3 = np.array([1.0, 0, 0]); hop = _p39_hop
    e = 0
    for _ in range(200):
        q = rng.normal(size=4); q /= np.linalg.norm(q); t = rng.uniform(0, 6.28); s = rng.uniform(0, 6.28)
        e = max(e, np.linalg.norm(hop(qm(ex(I3, t), q)) - hop(q)))
        a = hop(q); b = hop(qm(q, ex(I3, s))); c_, s_ = np.cos(2*s), np.sin(2*s)
        e = max(e, abs(b[0] - a[0]), abs(np.hypot(b[1], b[2]) - np.hypot(a[1], a[2])), abs((a[1]*b[1] + a[2]*b[2]) - c_*(a[1]**2 + a[2]**2)))
    lanes = []
    for ed in (0, 15, 45, 75, 90):
        et = np.radians(ed); q = np.array([np.cos(et), 0, np.sin(et), 0]); XL = qm(np.r_[0, I3], q); XR = qm(q, np.r_[0, I3]); hz = XR - (XR @ XL)*XL
        lanes.append((ed, np.linalg.norm(XL - XR), np.linalg.norm(hz), XL @ XR))
    nt = np.array([np.cos(0.9), np.sin(0.9), 0]); q = rng.normal(size=4); q /= np.linalg.norm(q); dl = []; dr = []
    for th in np.linspace(0, 2*np.pi, 24, endpoint=False):
        qq = qm(ex(I3, th), q); h_ = 1e-6
        dl.append((hop(qm(ex(nt, h_), qq)) - hop(qm(ex(nt, -h_), qq)))/(2*h_)); dr.append((hop(qm(qq, ex(nt, h_))) - hop(qm(qq, ex(nt, -h_))))/(2*h_))
    dl, dr = np.array(dl), np.array(dr)
    _p39_say(f"(a) The canonical shell's Hopf quotient, h(q) = q* i q, forgets the left field i q along whose circles it quotients, and the right "
             f"field q i descends to a turn of the quotient sphere about its axis at twice the rate ({_p39_lt(e, 1e-12)}, 200 points).  The two "
             f"lanes' separation on the shell, 2 sin eta, against the right lane's speed after the quotient, sin 2 eta on the quotient sphere of "
             f"radius one half, and their cosine, at eta from the hinge: " + "; ".join(f"{a_} deg: {b_:.4f}, {c_:.4f}, {d_:+.4f}" for a_, b_, c_, d_
             in lanes) + f" -- opposite on the shell at the dual circle and one point after the quotient.  Every right field descends, its image "
             f"the same all along a fiber ({_p39_lt(np.abs(dr - dr[0]).max(), 1e-8)}); a second left field tilted by 0.9 rad does not: along one "
             f"fiber its image has length {np.linalg.norm(dl, axis=1).mean():.4f} = 2 sin 0.9 = {2*np.sin(0.9):.4f} and points every way round "
             f"(mean {_p39_lt(np.linalg.norm(dl.mean(0)), 1e-8)}).")
    check(e < 1e-12 and np.abs(dr - dr[0]).max() < 1e-8 and np.linalg.norm(dl.mean(0)) < 1e-8, "v41.0-5(a): the Hopf quotient forgets its own "
          "field, keeps every field of the other hand as a rotation, and smears a tilted field of its own hand round a circle")
    e1 = e2 = 0
    for _ in range(100):
        be = rng.uniform(0.1, 3.0); ax = rng.normal(size=3); ax -= (ax @ I3)*I3; ax /= np.linalg.norm(ax); n3 = np.cos(be)*I3 + np.sin(be)*ax
        q = rng.normal(size=4); q /= np.linalg.norm(q); x0 = hop(q)
        ring = np.array([hop(qm(ex(I3, th), q), n3) for th in np.linspace(0, 2*np.pi, 48, endpoint=False)])
        e1 = max(e1, np.abs(ring @ x0 - np.cos(be)).max(), np.linalg.norm(ring.mean(0) - np.cos(be)*x0))
        a3 = rng.normal(size=3); a3 /= np.linalg.norm(a3)
        for l in range(1, 9):
            cf = np.zeros(l + 1); cf[l] = 1; Lv = np.polynomial.legendre.legval
            e2 = max(e2, abs(Lv(ring @ a3, cf).mean() - Lv(np.cos(be), cf)*Lv(x0 @ a3, cf)))
    fac = [[np.polynomial.legendre.legval(np.cos(np.radians(b_)), np.eye(5)[l]) for b_ in (30, 54.7356, 90, 180)] for l in (1, 2, 3, 4)]
    _p39_say(f"(b) Matter uniform along one Hopf circle, read through the quotient by a circle tilted by beta: each fiber's images lie evenly on "
             f"the ring of angular radius beta about the point ({_p39_lt(e1, 1e-12)}, 100 random tilts), so an angular pattern of degree l is "
             f"multiplied by P_l(cos beta) ({_p39_lt(e2, 1e-12)}, l = 1 to 8); at beta = 30, 54.74, 90 and 180 deg: " + "; ".join(
             f"l = {l}: " + ", ".join(f"{(0.0 if abs(x) < 5e-4 else x):+.3f}" for x in fac[l - 1]) for l in (1, 2, 3, 4)) + ".")
    check(e1 < 1e-12 and e2 < 1e-12, "v41.0-5(b): a tilted quotient spreads each point over a ring and multiplies the angular harmonics by "
          "Legendre polynomials of the tilt")
    N = 600000; R, ph = _p39_arm_disk(rng, N)
    def conc(r): r = np.sort(r); return r[int(0.9*len(r))]/r[int(0.5*len(r))]
    def arms(rp, az):
        b = np.floor(np.log(rp/0.5)/0.1).astype(int); out = []
        for k in range(int(np.log(8)/0.1)):
            m = b == k
            if m.sum() > 2000: out.append(abs(np.exp(2j*az[m]).mean()))
        return float(np.median(out))
    arm0 = arms(R, ph); tab = []
    for bd in (0, 10, 20, 40, 54.7356, 70, 90):
        be = np.radians(bd); X = _p39_tilt(rng, R, ph, be)
        ca = np.sqrt((X[:, 2]**2).mean()/(X[:, 0]**2).mean()); th_ = np.sin(be)/np.sqrt(1 - np.sin(be)**2/2)
        band = (np.abs(X[:, 2]) < 0.1*R).mean(); arm = arms(np.hypot(X[:, 0], X[:, 1]), np.arctan2(X[:, 1], X[:, 0]))/arm0
        tab.append((bd, ca, th_, arm, band, conc(np.hypot(X[:, 0], X[:, 1])), conc(np.hypot(X[:, 0], X[:, 2]))))
    cexp = _P39_SP.gammaincinv(2, 0.9)/_P39_SP.gammaincinv(2, 0.5); cdv = (_P39_SP.gammaincinv(8, 0.9)/_P39_SP.gammaincinv(8, 0.5))**4
    _p39_say(f"(c) A thin exponential disk with two logarithmic arms, pitch 20 deg, contrast 0.5, 600,000 points, its face-on R_90/R_50 "
             f"{conc(R):.3f} (an exponential profile's {cexp:.4f}, de Vaucouleurs' {cdv:.2f}, from the incomplete gamma function), each point "
             f"moved to a random point of its ring of angular radius beta at its own distance from the center -- at beta, the rms thickness over "
             f"the rms width (the formula sin beta/sqrt(1 - sin^2 beta/2)), the two-armed pattern kept face-on, the share within 5.7 deg of the "
             f"plane, R_90/R_50 face-on and edge-on: " + "; ".join(f"{a_:.2f} deg: {b_:.3f} ({c_:.3f}), {d_:.3f}, {e_:.3f}, {f_:.2f}, {g_:.2f}"
             for a_, b_, c_, d_, e_, f_, g_ in tab) + ".  At 54.74 deg, where P_2 vanishes, the image is as thick as it is wide; beyond, prolate "
             "along the old normal.")
    check(all(abs(b_ - c_) < 0.01 for _, b_, c_, _, _, _, _ in tab) and tab[0][3] > 0.99 and tab[4][3] < 0.4 and tab[-1][5] < 3.1,
          "v41.0-5(c): read through a tilted quotient a thin two-armed disk thickens to round at the magic angle and loses most of its arms, while "
          "its light's concentration stays near an exponential's, far from de Vaucouleurs'")
    g6 = rng.normal(size=(6, 6)); g6 = g6 @ g6.T + 6*np.eye(6); g6[0, 0] -= 40.0
    def quo(g, K): Gm = K.T @ g @ K; return g - g @ K @ np.linalg.inv(Gm) @ K.T @ g, np.linalg.det(Gm)
    K = np.zeros((6, 2)); K[4, 0] = K[5, 1] = 1; h0, d0 = quo(g6, K); Mx = rng.normal(size=(2, 2)); h1, d1 = quo(g6, K @ Mx)
    sig = np.sign(np.linalg.eigvalsh(h0[:4, :4])).astype(int).tolist(); tl_ = []
    for v in (0.0, 0.5, 0.9, 0.99, 1.1):
        gg = np.diag([-1.0, 1, 1, 1, 1, 1]); Kt = np.zeros((6, 2)); Kt[4, 0] = 1; Kt[0, 0] = v; Kt[5, 1] = 1; hh, dd = quo(gg, Kt)
        evh = np.linalg.eigvalsh(hh); tl_.append((v, 1 - v*v, hh[0, 0], np.sign(np.round(evh[np.abs(evh) > 1e-9], 9)).astype(int).tolist()))
    _p39_say(f"(d) Which pair of directions is forgotten: on a six-dimensional metric of signature (1, 5), quotienting two commuting directions, "
             f"the base metric depends only on the plane they span ({_p39_lt(np.abs(h0 - h1).max(), 1e-12)}), the fibers' area squared scaling by "
             f"the change of basis's determinant squared ({_p39_lt(abs(d1/d0 - np.linalg.det(Mx)**2), 1e-12)}): Hopf and meridian exchanged or mixed "
             f"give one base, of signature {sig}.  One forgotten direction tilted toward time by v, in a flat metric: " + "; ".join(
             f"v = {a_:.2f}, its squared length {b_:+.3f}, the base's time-time part {c_:+.3f}, the base's signature {d_}" for a_, b_, c_, d_ in tl_) +
             " -- time survives while the forgotten plane is spacelike, and past v = 1 the base has none.")
    check(np.abs(h0 - h1).max() < 1e-12 and sig == [-1, 1, 1, 1] and tl_[-1][3] == [1, 1, 1, 1] and abs(tl_[1][2] + 1/0.75) < 1e-12,
          "v41.0-5(d): a quotient depends on the forgotten plane, not on its basis; time survives a quotient exactly while the forgotten "
          "directions are spacelike")
    sB = lambda be, ch: np.sqrt(1 + 0.5*np.sin(be)**2*(1/(4*np.sin(ch)**2) - 1))
    sF = lambda be, ch: np.sqrt(np.sin(be)**2*4*np.sin(ch)**2 + np.cos(be)**2)
    b4 = np.pi/4; base_ = [sB(b4, ch) for ch in (np.pi/4, np.pi/2, 0.3)]; fib = [sF(b4, ch) for ch in (np.pi/4, np.pi/2, 0.3)]
    kq = 1/(0.5*(1 + np.cos(b4)**2) + 0.25*0.5*np.sin(b4)**2); s2 = np.sqrt(1 + 0.5*(4 - 1)*np.sin(np.radians(45))**2)
    _p39_say(f"(e) The averaged quotient of Section XXVI.9 on the arena's squashed shells, fiber over base rho_f/rho_b = 1/(2 sin chi): the "
             f"rendered length's factor s = sqrt(1 + (1/2) sin^2 beta (rho_f^2/rho_b^2 - 1)), at beta = pi/4, {base_[0]:.3f} at chi = pi/4, "
             f"{base_[1]:.3f} at pi/2 and {base_[2]:.2f} at 0.3, the fiber's {fib[0]:.3f}, {fib[1]:.2f} and {fib[2]:.2f}, and the quotient's "
             f"curvature at the equator {kq:.4f} times the untilted -- that section's values, which it gives for the tilt it calls a quarter turn; "
             f"the response's {s2:.3f} for a ratio 2 at 45 deg.  s exceeds 1 exactly where 1/(4 sin^2 chi) does, inside chi = 30 deg, and falls "
             f"outward on every shell.")
    check(abs(base_[0] - 0.935) < 5e-4 and abs(base_[1] - 0.901) < 5e-4 and abs(base_[2] - 1.21) < 5e-3 and abs(s2 - 1.323) < 5e-4,
          "v41.0-5(e): Section XXVI.9's averaged quotient reproduced; its stretch falls outward and exceeds 1 only inside chi = 30 deg")
    tp = [(pd, 1 - np.sin(np.radians(pd))**2, np.cos(np.radians(pd))) for pd in (0, 30, 60, 85, 90)]
    b = 0.8; M1, M2 = 1.0, 0.5
    _p39_say("(f) A tilt p of the reference (Section XXXVII.7(a)): every body's charge over mass is sin p, and at fixed mass the static pull "
             "between two bodies, M_1 M_2 - Q_1 Q_2, is cos^2 p times Newton's and every length cos p times: " + "; ".join(
             f"{a_} deg, {b_:.4f} and {c_:.4f}" for a_, b_, c_ in tp) + f".  At fixed relations, the boost that keeps the far reference "
             f"(Section XXXVIII.3(k)), rapidity 0.8: masses {M1*np.cosh(b):.4f} and {M2*np.cosh(b):.4f}, charges {M1*np.sinh(b):.6f} and "
             f"{M2*np.sinh(b):.6f}, and M_1 M_2 - Q_1 Q_2 = {M1*M2*(np.cosh(b)**2 - np.sinh(b)**2):.6f}, as before, {M1*M2:.6f}.")
    check(abs(M1*np.sinh(b) - 0.888106) < 5e-7 and abs(M1*M2*(np.cosh(b)**2 - np.sinh(b)**2) - M1*M2) < 1e-12, "v41.0-5(f): a tilt at fixed mass "
          "weakens the pull as cos^2 p; the far reference's boost keeps every pair's M_i M_j - Q_i Q_j")

# ---------------------------------------------------------------------------------------------------- v41.0-6: Entry 555
def v41_0_germ():
    """v41.0-6 (R622, Section XXXIX.9): Entry 555 -- the association as the inertial indicator and its antisymmetric germ."""
    _p39_head("v41.0-6", "Entry 555: the association's germ -- the association as the point, its turn across a distance, the Maurer-Cartan limit "
              "with Pauli values, the Dirac operator built from it on the 3-sphere and on the leaf's two spin structures (Section XXXIX.9)")
    rng = np.random.default_rng(555); qm, qc, R, unit, ex, S = _p39_qm, _p39_qc, _p39_rot, _p39_unit, _p39_ex, _P39_S
    e1 = 0
    for _ in range(200):
        q = unit(rng.normal(size=4)); g = unit(rng.normal(size=4)); Rq = R(q)
        e1 = max(e1, np.abs(Rq.T @ Rq - np.eye(3)).max(), abs(np.linalg.det(Rq) - 1), np.abs(R(-q) - Rq).max(), np.abs(R(qm(q, g)) - Rq @ R(g)).max())
    qs = [unit(rng.normal(size=4)) for _ in range(100)]
    e2 = max(np.abs(np.array([qm(q, np.r_[0, e]) - qm(np.r_[0, R(q) @ e], q) for e in np.eye(3)])).max() for q in qs)
    _p39_say(f"(a) The association at a point q of the leaf, u -> R_q u = q u q*, the rotation whose graph is the sky there (Section XXXVIII.13(a)): "
             f"a rotation, the same for q and -q, composing as R_(qg) = R_q R_g ({_p39_lt(e1, 1e-12)}, 200 random points and rotations) -- the leaf "
             f"is the set of associations, and a uniform change of association by g is the translation q -> q g.  At q the two Hopf frames, the "
             f"right-multiplied q e_a and the left-multiplied e_a q, are related by it, q e_a = (R_q e_a) q ({_p39_lt(e2, 1e-12)}, 100 points).")
    rows = []
    for eps in (1e-1, 1e-3, 1e-5):
        worst = 0
        for _ in range(50):
            q = unit(rng.normal(size=4)); a = unit(rng.normal(size=3)); q2 = qm(q, ex(a, eps)); Mx = R(q).T @ R(q2)
            ang = np.arccos(np.clip((np.trace(Mx) - 1)/2, -1, 1)); A = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
            worst = max(worst, abs(ang - 2*eps), np.abs((Mx - np.eye(3))/eps - 2*A).max())
        rows.append((eps, worst))
    au = 149597870700.0; pc = au*648000/np.pi; kpc = 1000*pc; ell = 16*kpc
    turns = [(nm, 2*d/ell) for nm, d in (("1 au", au), ("1 pc", pc), ("1 kpc", kpc), ("8 kpc", 8*kpc))]
    _p39_say("(b) Nearby associations, q' = q exp(eps a) at leaf distance eps: R_q^T R_q' is a turn by 2 eps about a, and (R_q^T R_q' - 1)/eps tends "
             "to 2[a]x, a finite limit -- the germ, the leaf's Maurer-Cartan form q* dq: " + "; ".join(f"eps = {e_:.0e}, the turn less 2 eps and "
             f"the normalized difference less 2[a]x at most {w_:.1e}" for e_, w_ in rows) + ", falling as eps.  On a 16 kpc leaf the association "
             "turns across " + ", ".join(f"{nm} by {t_:.3e} rad" for nm, t_ in turns) + " (the IAU's astronomical unit and parsec): the lanes "
             "agree at small scales.")
    check(rows[-1][1] < 1e-4 and abs(turns[1][1] - 1.25e-4) < 1e-12, "v41.0-6(a)-(b): the association is the point; nearby associations differ by "
          "a turn of twice their distance, and the normalized difference has the finite limit 2[a]x")
    e3 = 0
    for _ in range(200):
        q = unit(rng.normal(size=4)); v1, v2 = rng.normal(size=4), rng.normal(size=4); v1 -= (v1 @ q)*q; v2 -= (v2 @ q)*q
        sg = lambda v: sum(c*P for c, P in zip(qm(qc(q), v)[1:], S))
        e3 = max(e3, np.abs(sg(v1) @ sg(v2) + sg(v2) @ sg(v1) - 2*(v1 @ v2)*np.eye(2)).max())
    _p39_say(f"(c) The germ's values as Pauli matrices: sigma(v) = Im(q* v).sigma for v tangent at q satisfies sigma(v_1) sigma(v_2) + sigma(v_2) "
             f"sigma(v_1) = 2 <v_1, v_2> ({_p39_lt(e3, 1e-12)}, 200 points and pairs): the Clifford relation with the leaf's own metric.")
    F = [np.array([qm(b, np.r_[0, np.eye(3)[a]]) for b in np.eye(4)]).T for a in range(3)]
    br = lambda i, j: F[i] @ F[j] - F[j] @ F[i]
    cm = max(np.abs(br(0, 1) + 2*F[2]).max(), np.abs(br(1, 2) + 2*F[0]).max(), np.abs(br(2, 0) + 2*F[1]).max())
    spec = {}; imax = 0
    for n in range(0, 7):
        Q = _p39_harm(n); Xs = [Q.T @ _p39_act(Fa, n) @ Q for Fa in F]; Dn = sum(np.kron(1j*S[a], Xs[a]) for a in range(3)); evn = np.linalg.eigvals(Dn)
        imax = max(imax, np.abs(evn.imag).max()); vals, cnt = np.unique(np.round(evn.real, 8), return_counts=True)
        spec[n] = {float(k): int(v) for k, v in zip(vals, cnt)}
    sph = {}
    for n in range(0, 7):
        for k, v in spec[n].items(): sph[k + 1.5] = sph.get(k + 1.5, 0) + v
    full = sorted((k, v) for k, v in sph.items() if abs(k) <= 6.5)
    lv = {}
    for par in (0, 1):
        d = {}
        for n in range(par, 7, 2):
            for k, v in spec[n].items(): d[k + 1.5] = d.get(k + 1.5, 0) + v
        lv[par] = sorted(((k, v) for k, v in d.items() if abs(k) < 7), key=lambda t: abs(t[0]))
    fmt = lambda ls: ", ".join(f"{k:+.1f} ({v})" for k, v in ls)
    _p39_say(f"(d) The operator i sigma^a X_a built from the germ, X_a(q) = q e_a the left-invariant unit fields ([X_i, X_j] = 2 X_k as matrices, "
             f"{_p39_lt(cm, 1e-12)}), on spinor fields on the unit 3-sphere whose two components are harmonic polynomials of degree n: " + "; ".join(
             f"n = {n}: " + ", ".join(f"{k:+.0f} ({v})" for k, v in sorted(spec[n].items())) for n in range(0, 7)) + f" -- n with multiplicity "
             f"(n + 1)(n + 2) and -(n + 2) with n(n + 1), imaginary parts {_p39_lt(imax, 1e-12)}.  With the spin connection's constant 3/2, D = i "
             f"sigma.X + 3/2 has on the 3-sphere the eigenvalues, with multiplicities, " + fmt(sorted(full, key=lambda t: (abs(t[0]), -t[0]))) +
             " -- +-(k + 3/2), (k + 1)(k + 2), the round 3-sphere's Dirac spectrum (Baer 1996).  On the leaf, spinors even under x -> -x (n even): " +
             fmt(lv[0]) + "; odd (n odd): " + fmt(lv[1]) + " -- the leaf's two spin structures, each spectrum the other's mirror and neither "
             "symmetric about zero.")
    okd = (cm < 1e-12 and imax < 1e-12 and all(spec[n].get(float(n), 0) == (n + 1)*(n + 2) and spec[n].get(float(-(n + 2)), 0) == n*(n + 1)
                                                for n in range(1, 7))
           and lv[0][0] == (1.5, 2) and lv[1][0] == (-1.5, 2))
    check(okd, "v41.0-6(c)-(d): the germ's Pauli values satisfy the Clifford relation with the leaf's metric; the Dirac operator built from them "
               "has the 3-sphere's spectrum +-(k + 3/2), and on the leaf's two spin structures spectra that are mirror images, neither symmetric")
    n_ = unit(rng.normal(size=3)); d_ = rng.normal(size=3); d_ -= (d_ @ n_)*n_; d_ = unit(d_)
    Ps = lambda u: 0.5*(np.eye(2) + sum(c*P for c, P in zip(u, S))); lim = []
    for eps in (1e-2, 1e-4):
        upp, umm = n_*np.cos(eps) + d_*np.sin(eps), n_*np.cos(eps) - d_*np.sin(eps)
        lim.append((eps, np.abs((Ps(upp) - Ps(umm))/eps - sum(c*P for c, P in zip(d_, S))).max()))
    Ra = R(unit(rng.normal(size=4))); a3 = unit(rng.normal(size=3)); Agen = np.array([[0, -a3[2], a3[1]], [a3[2], 0, -a3[0]], [-a3[1], a3[0], 0]])
    u0 = unit(rng.normal(size=3)); dl_ = []
    for eps in (1e-2, 1e-4):
        Rb = Ra @ (np.eye(3) + np.sin(eps)*Agen + (1 - np.cos(eps))*Agen @ Agen); vv = Rb @ u0
        dl_.append((eps, np.linalg.norm((Ra.T @ vv - u0)/eps - Agen @ u0)))
    _p39_say(f"(e) The response's numbers: sin 25 deg = {np.sin(np.radians(25)):.4f}, and over 25 deg in radians {np.sin(np.radians(25))/np.radians(25):.4f}; "
             f"(P_+ - P_-)/eps tends to d.sigma, " + ", ".join(f"{w_:.1e} at eps = {e_:.0e}" for e_, w_ in lim) + "; with R_b = R_a e^(eps A), "
             f"(R_a^-1 v - u)/eps tends to A u, " + ", ".join(f"{w_:.1e} at eps = {e_:.0e}" for e_, w_ in dl_) + ".")
    check(lim[-1][1] < 1e-6 and dl_[-1][1] < 1e-3, "v41.0-6(e): the response's two limits, the projectors' and the association's, hold")

# ---------------------------------------------------------------------------------------------------- v41.0-7: Entry 556
def v41_0_augment():
    """v41.0-7 (R623, Section XXXIX.10): Entry 556 -- the forgotten circle as a Markov augmentation; before and after the blow-up."""
    _p39_head("v41.0-7", "Entry 556: the forgotten circle as a Markov augmentation -- a geodesic's image, the rendered state that is not closed, "
              "the charge that closes it and the phase that inverts it; transforming before and after the blow-up; a move anchored at one reference "
              "(Section XXXIX.10)")
    rng = np.random.default_rng(556); qm, qc, unit = _p39_qm, _p39_qc, _p39_unit; I_ = np.array([0, 1.0, 0, 0])
    hop = lambda q: qm(qm(qc(q), I_), q)[1:]; X = lambda q: qm(I_, q)
    worst = 0
    for _ in range(200):
        q = unit(rng.normal(size=4)); w = rng.normal(size=4); w -= (w @ q)*q; w = unit(w); p = w @ X(q)
        ts = np.linspace(0, 3, 31); xs = np.array([hop(np.cos(t)*q + np.sin(t)*w) for t in ts])
        c = np.linalg.svd(xs - xs.mean(0))[2][-1]; c = c*np.sign(c @ xs[0]) if abs(c @ xs[0]) > 1e-12 else c
        rad = np.arccos(np.clip(xs @ c, -1, 1)); worst = max(worst, np.ptp(rad), abs(np.cos(rad.mean()) - abs(p)))
    _p39_say(f"(a) A geodesic of the unit 3-sphere through q with unit tangent w, read through the Hopf quotient h(q) = q* i q: a circle on the "
             f"quotient sphere, its angular radius arccos |p|, p = <w, i q> the momentum along the forgotten circle, conserved "
             f"({_p39_lt(worst, 1e-12)}, 200 geodesics): the motion of a charge in a monopole's field, p its charge -- Kaluza and Klein's reading.")
    q = unit(rng.normal(size=4)); hh = rng.normal(size=4); hh -= (hh @ q)*q + (hh @ X(q))*X(q); hh = unit(hh); outs = []
    for p in (0.0, 0.5, 0.9):
        w = hh + p*X(q); sp = np.linalg.norm(w); g = lambda t: np.cos(sp*t)*q + np.sin(sp*t)*w/sp
        outs.append((p, hop(g(0)), (hop(g(1e-6)) - hop(g(-1e-6)))/2e-6, hop(g(2.0))))
    d0 = max(np.abs(o[1] - outs[0][1]).max() for o in outs); d1 = max(np.abs(o[2] - outs[0][2]).max() for o in outs)
    def lift(xpath, ts, q0, p):
        cs = _P39_IPL.CubicSpline(ts, xpath)
        def f(t, y):
            y = y/np.linalg.norm(y); xd = cs(t, 1)
            J = np.array([(hop(unit(y + 1e-7*e)) - hop(unit(y - 1e-7*e)))/2e-7 for e in np.eye(4)]).T
            Hb = np.linalg.svd(np.column_stack([y, X(y)]))[0][:, 2:]
            return Hb @ np.linalg.lstsq(J @ Hb, xd, rcond=None)[0] + p*X(y)
        return _P39_INT.solve_ivp(f, [ts[0], ts[-1]], q0, t_eval=ts, rtol=1e-10, atol=1e-12).y.T
    worst = 0
    for _ in range(5):
        q = unit(rng.normal(size=4)); w = rng.normal(size=4); w -= (w @ q)*q; w = unit(w); p = w @ X(q)
        ts = np.linspace(0, 2.5, 251); upst = np.array([np.cos(t)*q + np.sin(t)*w for t in ts]); xp = np.array([hop(u) for u in upst])
        worst = max(worst, np.abs(lift(xp, ts, q, p) - upst).max())
    _p39_say(f"(b) Three geodesics through one point with one horizontal velocity and p = 0, 0.5, 0.9 have the same rendered start "
             f"({_p39_lt(d0, 1e-12)}) and rendered velocity ({_p39_lt(d1, 1e-8)}), and at t = 2 their rendered positions are "
             f"{np.linalg.norm(outs[1][3] - outs[0][3]):.4f} apart (p = 0 and 0.5) and {np.linalg.norm(outs[2][3] - outs[0][3]):.4f} (p = 0 and 0.9): "
             f"the rendered position and velocity are not a closed state, and with p they are.  Rebuilt from the rendered path, p and the starting "
             f"point upstairs -- the horizontal lift by the connection, plus p along the circle -- five geodesics come back to "
             f"{_p39_lt(worst, 1e-7)}: the rendered worldline, its charge and one phase are an invertible packaging of the history upstairs.")
    check(worst < 1e-7 and np.linalg.norm(outs[2][3] - outs[0][3]) > 1, "v41.0-7(a)-(b): a geodesic upstairs is a charge's circle below; the "
          "rendered state needs the charge to be closed and one phase more to be inverted")
    dl = 0.05; n = 200000
    th = dl/2 + (dl/2)*rng.random(n); nn = rng.normal(size=(n, 4)); nn /= np.linalg.norm(nn, axis=1)[:, None]
    Y = np.column_stack([np.sin(th)[:, None]*nn, np.cos(th)]); wt = np.sin(th)**3*(1 + 2*(nn[:, 0]**2 - 0.25))
    def leaf(p0):
        b = np.zeros(5); b[4] = np.cos(p0); b[0] = np.sin(p0); Yp = Y - np.outer(Y @ b, b); Yp /= np.linalg.norm(Yp, axis=1)[:, None]
        return np.sort(np.linalg.eigvalsh((Yp.T*wt) @ Yp/wt.sum()))[::-1]
    e0 = leaf(0.0); rows = [(r_, leaf(r_*dl)) for r_ in (0.5, 1.0, 2.0)]
    _p39_say("(c) Transforming before the blow-up against after it: the elongated core of Section XXIX.10(d), size 0.05, resolved about an axis "
             "offset from it by 0.5, 1 and 2 core sizes, has the moments " + "; ".join(f"{', '.join(f'{x:.4f}' for x in e_[:4])}" for _, e_ in rows) +
             f"; resolved about its own axis and then turned, by any turn, it keeps {', '.join(f'{x:.4f}' for x in e0[:4])}.  No turn after the "
             f"resolution is the tilt before it.")
    check(all(abs(e_[0] - e0[0]) > 0.02 for _, e_ in rows), "v41.0-7(c): a tilt before the blow-up changes the resolved form's eigenvalues, which "
          "no rotation after it changes")
    rr = []
    for b in (0.3, 0.8, 2.0):
        m = np.array([1.0, 0.5, 2.0]); M, Qc = m*np.cosh(b), m*np.sinh(b)
        rr.append((b, Qc/M, [M[i]*M[j] - Qc[i]*Qc[j] for i, j in ((0, 1), (0, 2), (1, 2))], [m[i]*m[j] for i, j in ((0, 1), (0, 2), (1, 2))]))
    _p39_say("(d) A move anchored at one reference acts on every body (Section XXXVIII.3(k)): three bodies of masses 1, 0.5 and 2, the far "
             "reference's boost of rapidity b gives masses m cosh b and charges m sinh b -- " + "; ".join(
             f"b = {b:.1f}: every charge over mass {qm_[0]:.4f}, the pairs' M_i M_j - Q_i Q_j {', '.join(f'{x:.6f}' for x in pp)} as before"
             for b, qm_, pp, p0 in rr) + ": no pair's static pull changes, so no body can signal another by it.")
    check(all(max(abs(a_ - b_) for a_, b_ in zip(pp, p0)) < 1e-9 and np.ptp(qm_) < 1e-12 for _, qm_, pp, p0 in rr), "v41.0-7(d): the far "
          "reference's boost charges every body to one charge-to-mass ratio and keeps every pair's M_i M_j - Q_i Q_j")

# ---------------------------------------------------------------------------------------------------- the suites
def v41_0_suite():
    """The v41.0 sections: v41.0-1 to v41.0-7 (R617-R623)."""
    v41_0_moments(); v41_0_modes(); v41_0_rays(); v41_0_orbit(); v41_0_ortho(); v41_0_germ(); v41_0_augment()

def current_suite_v41():
    """The regression suite of Part XXXIX (v41.0), followed by the check summary."""
    v41_0_suite()
    npass = sum(1 for ok, _ in _CHECKS if ok); nfail = len(_CHECKS)-npass
    print(f"\n== check summary (Part XXXIX): {npass} passed, {nfail} failed ==")
    for ok, msg in _CHECKS:
        if not ok: print("   FAILED:", msg)
    return nfail == 0
# ==================================================================================================== end of v41 body

if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else "current"
    suites = {"current": current_suite_v41, "v41_0": v41_0_suite}
    if arg not in suites:
        print("usage: python3 -I pg_v41_numerics.py [" + " | ".join(suites) + "]"); sys.exit(2)
    suites[arg]()
    if arg != "current":
        npass = sum(1 for ok, _ in _CHECKS if ok); print(f"\n== check summary ({arg}): {npass} passed, {len(_CHECKS)-npass} failed ==")
    if any(not ok for ok, _ in _CHECKS):
        sys.exit(1)
