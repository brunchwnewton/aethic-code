"""Projective Gravity v41.0: the two figures of Sections XXXIX.7-8, drawn from the constructions of pg_v41_numerics.py (v41.0-4 and v41.0-5).

Usage, from the directory of pg_v41_numerics.py:
    python3 -I galaxy_sims/pg_v41_figures.py      # writes galaxy_sims/v41_fig1.png and galaxy_sims/v41_fig2.png
matplotlib (Agg) draws them, from samples and orbits computed here with the suite's own functions and seeded generators; nothing is fitted."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SUITE = os.path.abspath(os.path.join(HERE, '..'))
if SUITE not in sys.path: sys.path.insert(0, SUITE)
import numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import pg_v41_numerics as S
SURF, INK, INK2, MUTED, GRID, BASE = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
SER = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF, "axes.edgecolor": BASE, "axes.labelcolor": INK2,
                     "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK, "axes.grid": False, "font.size": 9, "axes.titlesize": 10,
                     "axes.titleweight": "bold", "axes.spines.top": False, "axes.spines.right": False})
SEQ = LinearSegmentedColormap.from_list('seq', [SURF, "#cfe0f6", "#7fb0ea", "#2a78d6", "#123f7a"])


def fig1():
    """The ortho image of a two-armed disk: face-on (top) and edge-on (bottom) at four tilts of the quotient, on one color scale per row."""
    rng = np.random.default_rng(5541); R, ph = S._p39_arm_disk(rng, 600000)
    tilts = [(0.0, '0 deg'), (20.0, '20 deg'), (54.7356, '54.74 deg'), (90.0, '90 deg')]
    ext = 6.0; bins = np.linspace(-ext, ext, 241); Hs = []
    for bd, lab in tilts:
        X = S._p39_tilt(rng, R, ph, np.radians(bd))
        Hs.append([np.log10(1 + np.histogram2d(X[:, a], X[:, b], bins=[bins, bins])[0].T) for a, b in ((0, 1), (0, 2))])
    top = [max(H[i].max() for H in Hs) for i in (0, 1)]
    fig, ax = plt.subplots(2, 4, figsize=(11.2, 5.8), constrained_layout=True)
    for j, (bd, lab) in enumerate(tilts):
        for i, nm in enumerate(('face-on', 'edge-on')):
            ax[i, j].imshow(Hs[j][i], origin='lower', extent=[-ext, ext, -ext, ext], cmap=SEQ, vmin=0, vmax=top[i], interpolation='nearest')
            ax[i, j].set_xticks([-5, 0, 5]); ax[i, j].set_yticks([-5, 0, 5]); ax[i, j].tick_params(length=2)
            for s_ in ('top', 'right', 'left', 'bottom'): ax[i, j].spines[s_].set_visible(True); ax[i, j].spines[s_].set_color(BASE)
            if i == 0: ax[i, j].set_title('(%s) tilt %s' % ('abcd'[j], lab))
            if j == 0: ax[i, j].set_ylabel('%s, in disk scale lengths' % nm)
    fig.savefig(os.path.join(HERE, 'v41_fig1.png'), dpi=150); plt.close(fig)


def readout(sol_t, sol_y):
    """Points of the 3-sphere's orbit read on the leaf: chi past the equator read as pi - chi, the azimuth turned by pi."""
    ch, phi = sol_y[0], sol_y[2]; far = ch > np.pi/2
    r = np.tan(np.where(far, np.pi - ch, ch)); a = np.where(far, phi + np.pi, phi)
    return r*np.cos(a), r*np.sin(a), r, far


def orbit_long(E, L, tmax):
    chp = S._p39_pericenter(E, L)
    return solve_ivp(S._p39_rhs(L), [0, tmax], [chp, 1e-12, 0.0], rtol=1e-11, atol=1e-13, dense_output=True)


def segments(so, tmax, n=40000):
    t = np.linspace(0, tmax, n); y = so.sol(t); x, yy, r, far = readout(t, y); chd = y[1]
    # outward while |chi - pi/2| decreases toward the equator, inward after it
    outward = np.sign(np.where(y[0] < np.pi/2, chd, -chd)) > 0
    return x, yy, r, outward


def fig2():
    L = np.sqrt(2.0); Ec = L*L/2 + 1
    fig, ax = plt.subplots(1, 3, figsize=(11.6, 4.0), constrained_layout=True)
    # (a) one orbit across the equator, E - E_c = 0.05: out, and back from the opposite side, its mirror image
    chp, so = S._p39_half(Ec + 0.05, L); t1 = so.t_events[1][0]; t = np.linspace(0, t1, 20000); y = so.sol(t); x, yy, r, far = readout(t, y)
    lim = 6.0; m = r < lim
    ax[0].plot(np.where(m & ~far, x, np.nan), np.where(m & ~far, yy, np.nan), color=SER[1], lw=1.6, label='outward half')
    ax[0].plot(np.where(m & far, x, np.nan), np.where(m & far, yy, np.nan), color=SER[0], lw=1.6, label='returning half')
    ax[0].plot([0], [0], 'o', color=INK, ms=3); ax[0].set_aspect('equal'); ax[0].set_xlim(-lim, lim); ax[0].set_ylim(-lim, lim)
    ax[0].set_title('(a) across the equator, $E - E_c = 0.05$'); ax[0].set_xlabel('$x/\\ell$'); ax[0].set_ylabel('$y/\\ell$')
    ax[0].legend(loc='lower left', frameon=False, fontsize=8)
    # (b) at the resonance: successive passes
    Er = brentq(lambda E: S._p39_sweep(E, L) - 2*np.pi, Ec + 0.01, Ec + 1.0); chp, so1 = S._p39_half(Er, L); th = so1.t_events[1][0]
    so2 = orbit_long(Er, L, 4*th); x, yy, r, outw = segments(so2, 4*th); m = r < lim
    ax[1].plot(np.where(m & outw, x, np.nan), np.where(m & outw, yy, np.nan), color=SER[1], lw=1.2, label='outward passes')
    ax[1].plot(np.where(m & ~outw, x, np.nan), np.where(m & ~outw, yy, np.nan), color=SER[0], lw=1.2, label='inward passes')
    ax[1].plot([0], [0], 'o', color=INK, ms=3); ax[1].set_aspect('equal'); ax[1].set_xlim(-lim, lim); ax[1].set_ylim(-lim, lim)
    ax[1].set_title('(b) the resonance, $E - E_c = %.4f$' % (Er - Ec)); ax[1].set_xlabel('$x/\\ell$')
    ax[1].legend(loc='lower left', frameon=False, fontsize=8)
    # (c) the turn between successive pericenters in the readout against the energy
    dE = np.linspace(0.02, 0.6, 120); turn = [(np.degrees(S._p39_sweep(Ec + d, L)) + 180) % 360 for d in dE]
    ax[2].axhspan(170, 190, color=GRID, lw=0); ax[2].axhline(180, color=MUTED, lw=0.8)
    ax[2].plot(dE, turn, color=SER[2], lw=1.6); ax[2].set_ylim(0, 360); ax[2].set_yticks([0, 90, 180, 270, 360])
    ax[2].set_xlabel('$E - E_c$, $L^2 = 2$'); ax[2].set_ylabel('turn between successive pericenters, deg')
    ax[2].set_title('(c) the turn in the readout'); ax[2].grid(True, color=GRID, lw=0.6)
    fig.savefig(os.path.join(HERE, 'v41_fig2.png'), dpi=150); plt.close(fig)


if __name__ == '__main__':
    fig1(); fig2()
    print('wrote', os.path.join(HERE, 'v41_fig1.png'), 'and', os.path.join(HERE, 'v41_fig2.png'))
