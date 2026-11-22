"""Projective Gravity v40.2 -- the figures of Section XXXVIII.27, drawn from pg_v40_numerics.py's own functions (the kernel rows of v40.1, v40.0's
thin-disk solver, the closed forms of v40.2-1).  Needs matplotlib.  It lives in galaxy_sims/, beside the archive and pg_v40_numerics.py:

    python3 -I galaxy_sims/pg_v40_figures.py   # writes galaxy_sims/v402_fig1.png ... v402_fig13.png, the archive's links (two minutes)

Every number quoted in the archive is printed by pg_v40_numerics.py; this script draws the same quantities on finer radii."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pg_v40_numerics as P

HERE = os.path.dirname(os.path.abspath(__file__))
SURF, INK, INK2, MUTED, GRID, BASE = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
SER = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
LW = 1.5
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF, "axes.edgecolor": BASE, "axes.labelcolor": INK2,
                     "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 9.5, "axes.titlesize": 11, "axes.titleweight": "bold",
                     "legend.frameon": False, "legend.fontsize": 8.5, "axes.titlelocation": "left"})

def save(fig, name, note):
    fig.text(0.01, -0.035, note, fontsize=7.5, color=MUTED, ha="left", va="top")
    p = os.path.join(HERE, name); fig.savefig(p, dpi=200, bbox_inches="tight", metadata={"Software": None}); plt.close(fig); print("wrote", p)

def curve(k, X):
    """The leaf's v^2 ell/(G M) and its image's Newtonian v^2 ell/(G M) at R/ell = X, from the rows' grid by the eight-point polynomial."""
    c = P._v41_curves(k); s = math.log(X); return P._v41_lp(c['u'], s)[0], P._v41_lp(c['un'], s)[0]

def logspace(a, b, n): return [a*(b/a)**(i/(n - 1)) for i in range(n)]

GM = P._V40_GK*6e10; H, L = 2.021, 14.95; K = L/H

# 1. The Milky Way's leaf against Newton and the data
R = [0.3 + 0.1*i for i in range(298)]
leaf = [math.sqrt(GM/L*curve(K, r/L)[0]) for r in R]; newt = [math.sqrt(GM/L*curve(K, r/L)[1]) for r in R]
vinf = math.sqrt(P._v41_curves(K)['C']*GM/L)
fig, ax = plt.subplots(figsize=(7.5, 4.4))
ax.plot(R, leaf, color=SER[0], lw=LW, label=f"the leaf: $h$ = {H} kpc, $\\ell$ = {L} kpc, " + "$6\\times10^{10}M_\\odot$")
ax.plot(R, newt, color=SER[1], lw=LW, ls="--", label="Newton, the same visible disk")
E = P._V41_EILERS
ax.errorbar([e[0] for e in E], [e[1] for e in E], yerr=[[e[2] for e in E], [e[3] for e in E]], fmt="o", ms=3.2, color=INK2, ecolor=MUTED, elinewidth=0.8,
            capsize=0, label="Eilers et al. (2019)")
ax.axhline(vinf, color=SER[0], lw=0.8, ls=":"); ax.text(29.5, vinf + 3, "the leaf's plateau", color=INK2, ha="right", fontsize=8)
ax.set_xlim(0, 30); ax.set_ylim(0, 290); ax.set_xlabel("gnomonic radius R (kpc)"); ax.set_ylabel("circular speed (km/s)")
ax.set_title("A finite mass with a flat curve: the leaf holds the curve up where Newton's falls")
ax.legend(loc="lower right")
save(fig, "v402_fig1.png", "Section XXXVIII.22(g)'s leaf; the curve from v40.1's kernel rows, Newton's from the image's own thin-disk potential.")

# 2. The falloff sets the shape
X = logspace(2e-3, 60, 400)
fig, ax = plt.subplots(figsize=(7.5, 4.4))
for i, (k, lab) in enumerate(((1.0, "$\\ell/h$ = 1, monotonic"), (16/3, "$\\ell/h$ = 16/3, monotonic"), (6.0, "$\\ell/h$ = 6, wiggle"), (7.0,
    "$\\ell/h$ = 7, bump"),
                              (16.0, "$\\ell/h$ = 16, bump"), (100.0, "$\\ell/h$ = 100, bump"))):
    C = P._v41_curves(k)['C']; ax.plot(X, [math.sqrt(max(curve(k, x)[0], 0)/C) for x in X], color=SER[i], lw=LW, label=lab)
ax.axhline(1, color=MUTED, lw=0.8); ax.axvline(1, color=MUTED, lw=0.8, ls="--")
ax.text(1.1, 0.12, "$R = \\ell$: $\\chi = 45^\\circ$ on the leaf", color=INK2, fontsize=8)
ax.set_xscale("log"); ax.set_ylim(0, 3.8); ax.set_xlim(2e-3, 60)
ax.set_xlabel("gnomonic radius $R/\\ell$"); ax.set_ylabel("$v/v_\\infty$, the plateau 1")
ax.set_title("The falloff $k = \\ell/h$ sets the shape: quicker falloffs peak earlier and higher")
ax.legend(loc="center right", bbox_to_anchor=(1, 0.62))
save(fig, "v402_fig2.png", "v40.1-1: no extremum below $k_w = 5.9890$; a wiggle; a bump above the plateau from $k_b = 6.5029$; the dip near $R = \\ell$.")

# 3. Leaf against Newton, log-log, with the point source
X = logspace(1e-3, 1e3, 400)
fig, ax = plt.subplots(figsize=(7.5, 4.6))
for i, k in enumerate((0.1, 1.0, 16/3, 100.0)):
    ax.plot(X, [curve(k, x)[0] for x in X], color=SER[i], lw=LW, label=f"$\\ell/h$ = {k:g}" if k != 16/3 else "$\\ell/h$ = 16/3")
    ax.plot(X, [curve(k, x)[1] for x in X], color=SER[i], lw=LW*0.8, ls="--")
ax.plot(X, [P._v42_point(x)[0] for x in X], color=INK, lw=LW, label="point mass")
ax.plot(X, [1/x for x in X], color=INK, lw=LW*0.8, ls="--")
ax.plot([], [], color=MUTED, lw=LW, label="the leaf (solid)"); ax.plot([], [], color=MUTED, lw=LW*0.8, ls="--", label="Newton, same mass (dashed)")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(1e-3, 3e2); ax.set_xlim(1e-3, 1e3)
ax.set_xlabel("gnomonic radius $R/\\ell$"); ax.set_ylabel("$v^2\\ell/GM$")
ax.set_title("Newton falls as $1/R$; the leaf levels off at $C(k)\\,GM/\\ell$")
ax.legend(loc="upper right", ncol=2)
save(fig, "v402_fig3.png", "For slow falloffs the leaf's curve lies below Newton's at small R: it pulls less than the visible mass alone.")

# 4. The apparent halo's density
fig, ax = plt.subplots(figsize=(7.5, 4.6))
X = logspace(1e-3, 1e3, 400)
ax.plot(X, [P._v42_point(x)[2] for x in X], color=INK, lw=LW, label="point mass (closed form)")
for i, k in enumerate((16/3, 16.0, 100.0)):
    c = P._v41_curves(k); ud = [a - b for a, b in zip(c['u'], c['un'])]; m = [math.exp(l)*d for l, d in zip(P._V41_LG, ud)]
    xs = [x for x in logspace(max(3e-4, 0.03/k), 150, 300)]
    rho = [P._v41_lp(m, math.log(x))[1]/(4*math.pi*x**3) for x in xs]
    pts = [(x, r) for x, r in zip(xs, rho) if r > 0]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=SER[i], lw=LW, label=f"disk, $\\ell/h$ = {'16/3' if k == 16/3 else f'{k:g}'}")
for s_, lab, xa, xb, ya in ((-1, "slope -1, NFW inside", 1.5e-3, 1e-1, 3e3), (-2, "slope -2, isothermal", 5, 500, 2e-2),
                            (-3, "slope -3, NFW outside", 3, 40, 3e-5)):
    ax.plot([xa, xb], [ya, ya*(xb/xa)**s_], color=MUTED, lw=0.9, ls=":")
    ax.text(xb*1.15, ya*(xb/xa)**s_, lab, color=INK2, fontsize=7.5, va="center")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(1e-3, 2e3); ax.set_ylim(1e-9, 1e3)
ax.set_xlabel("gnomonic radius $R/\\ell$"); ax.set_ylabel("apparent dark density $\\rho_d\\ell^3/M$")
ax.set_title("The apparent halo: a $1/R$ cusp for $R\\ll\\ell$, $1/R^2$ beyond")
ax.legend(loc="lower left")
save(fig, "v402_fig4.png", "$\\rho_d = (4\\pi GR^2)^{-1}\\,d(Rv_d^2)/dR$ with $v_d^2 = v^2 - v_N^2$; the disks' cores are depressed (v40.1-2(c)).")

# 5. The image's density against the exponential, and the mass beyond R
R = [0.25*i for i in range(1, 241)]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 4.2))
a1.plot(R, [math.exp(-r/H) for r in R], color=INK, lw=LW, ls="--", label=f"exponential, $h$ = {H} kpc")
for i, Lx in enumerate((14.95, 50.0, 100.0)):
    k = Lx/H
    a1.plot(R, [math.exp(-r/H)*P._v42_image_ratio(k, r/Lx) for r in R], color=SER[i], lw=LW, label=f"the image, $\\ell$ = {Lx:g} kpc")
    a2.plot(R, [max(P._v42_mass_beyond(k, r/Lx), 1e-12) for r in R], color=SER[i], lw=LW, label=f"$\\ell$ = {Lx:g} kpc")
a2.plot(R, [math.exp(-r/H)*(1 + r/H) for r in R], color=INK, lw=LW, ls="--", label="exponential disk")
for a in (a1, a2): a.set_yscale("log"); a.set_xlim(0, 60); a.set_xlabel("gnomonic radius R (kpc)")
a1.set_ylim(1e-12, 2); a2.set_ylim(1e-9, 2)
a1.set_ylabel("surface density / central"); a2.set_ylabel("fraction of the mass beyond R")
a1.set_title("The image is exponential only while $R\\ll\\ell$"); a2.set_title("Mass beyond R")
a1.legend(loc="upper right"); a2.legend(loc="lower left")
save(fig, "v402_fig5.png", "$\\Sigma_{vis} = e^{-k\\sin\\chi}\\cos^3\\chi$ against $e^{-R/h}$; plateau speeds 222.8, 124.3, 88.0 km/s for $\\ell$ = "
     "14.95, 50, 100 kpc "
     "(v40.2-1(c)).")

# 6. The equator's density and the curve
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 4.2))
cut = math.atan(36.0/L); Rs = [1.0 + 0.5*i for i in range(59)]
for ax, h, title in ((a1, H, "The Milky Way's falloff, $h$ = 2.021 kpc"), (a2, L, "A slow falloff, $h = \\ell$ = 14.95 kpc")):
    k = L/h; S0, b0 = P._v40_sin_source(k); brk = sorted(set(b0 + [cut])); n0 = P._v40_disk_norm(S0, brk)
    def speeds(S):
        n = P._v40_disk_norm(S, brk)
        return [math.sqrt(x) if x > 0 else float("nan") for x in P._v40_disk_v2(S, L, 6e10*n/n0, [math.atan(r/L) for r in Rs], brk)]
    base = speeds(S0)
    for i, (lab, S) in enumerate((("removed", lambda x: S0(x) if x < cut else 0.0), ("doubled", lambda x: S0(x)*(2.0 if x >= cut else 1.0)),
                                  ("held at its value at 36 kpc", lambda x: S0(min(x, cut))))):
        ax.plot(Rs, [a - b for a, b in zip(speeds(S), base)], color=SER[i], lw=LW, label=lab)
    ax.axhline(0, color=MUTED, lw=0.8); ax.set_xlabel("gnomonic radius R (kpc)"); ax.set_ylabel("change in circular speed (km/s)"); ax.set_title(title)
a1.set_ylim(-3.5, 3.5); a2.set_ylim(-100, 100); a1.legend(loc="lower left", title="density beyond 36 kpc", title_fontsize=8.5, alignment="left")
a2.text(19.5, -62, "doubled: no circular orbit\nbeyond 18.14 kpc (v40.2-2)", color=INK2, fontsize=7.5, ha="left", va="top")
save(fig, "v402_fig6.png", "v40.0's thin-disk solver, the inner density fixed; beyond 36 kpc lies 1.46% of the mass for $h$ = 2.021 kpc and 31% for "
     "$h = \\ell$ "
     "(v40.2-2).")

# 7. v^2 across the families: the leaf, Newton for the same light, and the apparent halo between them
X = logspace(1e-3, 50, 400)
fig, axs = plt.subplots(2, 3, figsize=(10.5, 6.4))
for ax, (k, lab) in zip(axs.flat, ((1.0, "$\\ell/h$ = 1, monotonic"), (3.2, "$\\ell/h$ = 3.2, monotonic"), (16/3, "$\\ell/h$ = 16/3, monotonic"),
    (7.0, "$\\ell/h$ = 7, bump"),
                                   (16.0, "$\\ell/h$ = 16, bump"), (100.0, "$\\ell/h$ = 100, bump"))):
    C = P._v41_curves(k)['C']; uu = [curve(k, x) for x in X]
    ax.plot(X, [a/C for a, b in uu], color=SER[0], lw=LW, label="the leaf, $v^2$")
    ax.plot(X, [b/C for a, b in uu], color=SER[1], lw=LW, ls="--", label="Newton for the same light")
    ax.plot(X, [(a - b)/C for a, b in uu], color=SER[2], lw=LW, label="the difference: the apparent halo")
    ax.axhline(1, color=MUTED, lw=0.8, ls=":"); ax.axhline(0, color=BASE, lw=0.8); ax.axvline(1, color=MUTED, lw=0.8, ls="--")
    ax.set_xscale("log"); ax.set_xlim(1e-3, 50); ax.set_title(lab, fontsize=10)
    lo = min(0.0, min((a - b)/C for a, b in uu)); hi = max(a/C for a, b in uu)
    ax.set_ylim(lo - 0.08*(hi - lo), hi + 0.12*(hi - lo))
for ax in axs[1]: ax.set_xlabel("gnomonic radius $R/\\ell$")
for ax in axs[:, 0]: ax.set_ylabel("$v^2/v_\\infty^2$")
h_, l_ = axs[0, 0].get_legend_handles_labels()
fig.legend(h_, l_, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 0.975))
fig.suptitle("$v^2$ across the families: the leaf against Newton for the same light", fontweight="bold", x=0.01, ha="left", y=1.0)
fig.tight_layout(rect=(0, 0, 1, 0.93))
save(fig, "v402_fig7.png", "v40.1's kernel rows; the plateau $v_\\infty^2 = C(k)\\,GM/\\ell$ dotted, $R = \\ell$ dashed; for $\\ell/h\\leq3.2$ the "
     "difference is negative inside: "
     "the leaf pulls less than its light (v40.1-2(b)).")

# 8 and 9 (with 12 and 13 for the quicker families): the families on linear and logarithmic radii, and one visible disk on leaves ell = k h
def families(KS, name, title, xmax):
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(12.6, 4.3))
    XL = [xmax/750*i for i in range(1, 751)]; XG = logspace(1e-3, 50, 400)
    for i, k in enumerate(KS):
        a1.plot(XL, [curve(k, x)[0] for x in XL], color=SER[i], lw=LW, label=f"$\\ell/h$ = {k:g}")
        a2.plot(XG, [curve(k, x)[0] for x in XG], color=SER[i], lw=LW)
        a3.plot(XG, [curve(k, x)[0] - curve(k, x)[1] for x in XG], color=SER[i], lw=LW)
    for a in (a1, a2): a.axhline(3, color=MUTED, lw=0.8, ls=":")
    a1.set_xlim(0, xmax); a1.set_title("Linear radius: the familiar rotation curve", fontsize=10)
    a2.set_xscale("log"); a2.set_xlim(1e-3, 50); a2.set_title("Logarithmic radius: every scale at once", fontsize=10)
    a3.set_xscale("log"); a3.set_xlim(1e-3, 50); a3.set_title("The apparent halo: the leaf less Newton", fontsize=10)
    for a in (a1, a2, a3): a.set_xlabel("gnomonic radius $R/\\ell$")
    a1.set_ylabel("$v^2\\ell/GM$"); a3.set_ylabel("$v_d^2\\ell/GM$")
    a1.legend(loc="upper right", fontsize=7.5)
    fig.suptitle(title, fontweight="bold", x=0.01, ha="left", y=1.02)
    fig.tight_layout()
    save(fig, name, "v40.1's kernel rows; the point source's plateau $3GM/\\ell$ dotted; the apparent halo rises to the plateau without a peak "
         "of its own (v40.1-2(b)).")

def one_disk(KS, name, title):
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    RK = [0.25*i for i in range(1, 241)]
    for i, k in enumerate(KS):
        Lk = k*H
        ax.plot(RK, [math.sqrt(GM/Lk*curve(k, r/Lk)[0]) for r in RK], color=SER[i], lw=LW, label=f"$\\ell$ = {Lk:.0f} kpc ($\\ell/h$ = {k:g})")
    fr = lambda y: 2*y*y*(P._v40_bessel(0, y, 'I')*P._v40_bessel(0, y, 'K') - P._v40_bessel(1, y, 'I')*P._v40_bessel(1, y, 'K'))
    ax.plot(RK, [math.sqrt(GM/H*fr(r/(2*H))) for r in RK], color=INK, lw=LW, ls="--", label="Newton: the exponential disk alone")
    ax.set_xlim(0, 60); ax.set_ylim(0, 300); ax.set_xlabel("gnomonic radius $R$ (kpc)"); ax.set_ylabel("circular speed (km/s)")
    ax.set_title(title); ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=7.5)
    save(fig, name, "$h$ = 2.021 kpc, " + "$6\\times10^{10}M_\\odot$ as in Figure 1.  The peak is Freeman's, $0.38705\\,GM/h$; the plateau "
         "$C\\,GM/\\ell$ falls as the leaf grows (v40.2-1(a), (c)).")

KF = (5.0, 6.0, 7.0, 8.0, 10.0, 12.0, 15.0, 20.0)
KQ = (10.0, 14.0, 20.0, 28.0, 40.0, 56.0, 80.0, 100.0)
families(KF, "v402_fig8.png", "$\\ell/h$ = 5 to 20 on one leaf: from a monotonic rise through the wiggle to a bump that climbs and moves in", 1.5)
one_disk(KF, "v402_fig9.png", "One visible disk on leaves of 5 to 20 scale lengths: a shared rise, a plateau set by the leaf")

# 10. Two readings of one plane: the gnomonic map from the leaf, and what it does to radii and to surface density
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.2, 4.2))
CH = [math.radians(0.05 + 0.4*i) for i in range(225)]
a1.plot([math.degrees(c) for c in CH], [math.tan(c) for c in CH], color=SER[0], lw=LW, label="gnomonic radius $R/\\ell = \\tan\\chi$")
a1.plot([math.degrees(c) for c in CH], [math.sin(c) for c in CH], color=SER[1], lw=LW, label="areal radius on the leaf, $\\sin\\chi$")
a1.plot([math.degrees(c) for c in CH], [c for c in CH], color=SER[2], lw=LW, ls="--", label="distance along the leaf, $\\chi$")
a1.set_yscale("log"); a1.set_ylim(1e-3, 1e3); a1.set_xlim(0, 90); a1.set_xlabel("polar angle $\\chi$ on the leaf (degrees)")
a1.set_ylabel("radius / $\\ell$"); a1.set_title("The equator, $\\chi = 90^\\circ$, is sent to $R = \\infty$", fontsize=10); a1.legend(loc="upper "
     "left", fontsize=7.5)
XR = logspace(1e-2, 1e2, 300)
a2.plot(XR, [(1 + x*x)**-1.5 for x in XR], color=SER[0], lw=LW, label="$\\cos^3\\chi$: leaf area per plane area, the density's dilution")
a2.plot(XR, [1/math.sqrt(1 + x*x) for x in XR], color=SER[1], lw=LW, label="$\\cos\\chi$: the ratio of the areal radius to $R$")
a2.set_xscale("log"); a2.set_yscale("log"); a2.set_ylim(1e-6, 2); a2.set_xlabel("gnomonic radius $R/\\ell$")
a2.set_title("Read as flat, the plane dilutes the leaf's density", fontsize=10); a2.legend(loc="lower left", fontsize=7.5)
fig.tight_layout()
save(fig, "v402_fig10.png", "The gnomonic map keeps great circles straight but not lengths or areas: an area element of the plane is $\\sec^3\\chi$ times "
     "the leaf's, so $\\Sigma_{vis} = \\Sigma_{leaf}\\cos^3\\chi$.")

# 11. The mass discrepancy a Newtonian would measure: v^2 over Newton's v^2 for the same light
fig, ax = plt.subplots(figsize=(7.8, 4.6))
XD = logspace(1e-3, 100, 300)
ax.plot(XD, [P._v42_point(x)[0]*x for x in XD], color=INK, lw=LW, label="point mass (closed form)")
for i, k in enumerate(KF):
    ax.plot(XD, [curve(k, x)[0]/curve(k, x)[1] for x in XD], color=SER[i], lw=LW*0.9, label=f"disk, $\\ell/h$ = {k:g}")
ax.axvline(1, color=MUTED, lw=0.8, ls="--"); ax.axhline(1, color=MUTED, lw=0.8, ls=":")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(1e-3, 100); ax.set_ylim(0.5, 1e3)
ax.set_xlabel("gnomonic radius $R/\\ell$"); ax.set_ylabel("mass discrepancy $v^2/v_N^2$")
ax.set_title("The discrepancy a Newtonian would measure: one in the disk, then rising without limit")
ax.legend(loc="upper left", ncol=2, fontsize=7.5)
save(fig, "v402_fig11.png", "$v^2$ over Newton's $v^2$ for the same image; for the point mass $1 + M_d/M$ of v40.2-1(b), $2\\sqrt{2}$ at $R = \\ell$, "
     "growing as "
     "$3R/\\ell$.")

# 12 and 13. The quicker families, ell/h = 10 to 100, the secondary look
families(KQ, "v402_fig12.png", "$\\ell/h$ = 10 to 100 on one leaf: the peak climbs and moves in; the plateau stays near $3GM/\\ell$", 0.6)
one_disk(KQ, "v402_fig13.png", "One visible disk on leaves of 10 to 100 scale lengths: the same peak, a lower plateau")
