#!/usr/bin/env python3
"""Projective Gravity v35.8 -- comparison plots for Entries 312-313: Part XXV's solved rotation curves (the twin-symmetrized exponential
source exp(-tan(chi/2)/(r_d/ell)) on the round leaf, the rigid closure's first-order equations) read in four radial coordinates.  The
physics is fixed; only the horizontal coordinate changes.  Following the author's mid-round note, the figures lead with a sharp source
(r_d/ell = 0.02, a physical e-folding scale 2 r_d = 0.64 kpc), with the requested r_d/ell = 0.1, 0.01, 0.05, 0.2 and 0.3 alongside.
Past the equator the stereographic radius continues into the far hemisphere, where v^2 mirrors the near side; it is drawn dashed.
Needs pg_v35_numerics.py (v35.8) in the same directory, NumPy, SciPy and Matplotlib.

    python3 -I pg_v35_8_gnomonic_plots.py
        # writes pg_v35_8_four_radii.png, pg_v35_8_four_radii_family.png, pg_v35_8_gnomonic_family.png and pg_v35_8_mass_discrepancy.png
"""
import os, importlib.util
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import quad
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("pg", os.path.join(here, "pg_v35_numerics.py")); pg = importlib.util.module_from_spec(spec); spec.loader.exec_module(pg)
ell = 16.0; PI = np.pi; Gk = 4.300917270e-6; M = 6e10                    # kpc, G in kpc (km/s)^2/M_sun, the leaf's mass
radii = [("arc length  $\\ell\\chi$", lambda c: ell*c, "tab:gray"), ("areal  $\\ell\\sin\\chi$", lambda c: ell*np.sin(c), "tab:green"),
         ("stereographic  $2\\ell\\tan(\\chi/2)$", lambda c: 2*ell*np.tan(c/2), "tab:blue"), ("gnomonic  $\\ell\\tan\\chi$", lambda c: ell*np.tan(c), "tab:red")]
chi = np.concatenate([np.geomspace(1e-5, 0.05, 1500), np.linspace(0.05, PI/2-1e-5, 6000)[1:]])
rho_far = np.linspace(32.0, 100.0, 600); chi_far = 2*np.arctan(rho_far/(2*ell))      # the far hemisphere in the stereographic reading

def four_readings(axv, axv2, al, vmax, title=True):
    """One physical curve in the four readings: v on axv, v^2/v_eq^2 on axv2; the far hemisphere dashed in the stereographic reading."""
    v, veq, a2, mu, unit = pg._v358_pg_curve(al, ell); vv = v(chi)
    vf = np.where(np.abs(chi_far-PI/2) < 1e-9, veq, v(np.where(np.abs(chi_far-PI/2) < 1e-9, PI/2+1e-6, chi_far)))   # v at the equator is v_eq
    for lab, f, col in radii:
        axv.plot(f(chi), vv, color=col, label=lab); axv2.plot(f(chi), (vv/veq)**2, color=col, label=lab)
        if "gnomonic" not in lab:                                            # where the reading reaches the equator
            axv.plot(f(PI/2), veq, "o", color=col, ms=4.5); axv2.plot(f(PI/2), 1.0, "o", color=col, ms=4.5)
    axv.plot(rho_far, vf, color="tab:blue", ls="--", lw=1.2, label="stereographic, far hemisphere")
    axv2.plot(rho_far, (vf/veq)**2, color="tab:blue", ls="--", lw=1.2, label="stereographic, far hemisphere")
    for a in (axv, axv2):
        a.set_xlim(0, 100); a.set_xlabel("radius (kpc), $\\ell = 16$ kpc"); a.grid(alpha=0.3)
    axv.axhline(veq, color="k", lw=0.8, ls=":"); axv.set_ylabel("$v$ (km/s)"); axv.set_ylim(0, vmax)
    axv2.axhline(1.0, color="k", lw=0.8, ls=":"); axv2.set_ylabel("$v^2/v_{\\rm eq}^2$"); axv2.set_ylim(0, (vmax/veq)**2)
    if title:
        axv.set_title(f"one PG curve, $r_d/\\ell = {al}$ ($2r_d$ = {2*al*ell:.2f} kpc, $v_{{\\rm eq}}$ = {veq:.1f} km/s), four readings of its radius", fontsize=9)
        axv2.set_title("the same in $v^2$; dots: where the arc, areal and stereographic readings reach the equator", fontsize=9)
    return veq

# figure 1: one physical curve in four radial coordinates; top row sharp (r_d/ell = 0.02), bottom row the requested benchmark 0.1
fig, ax = plt.subplots(2, 2, figsize=(12, 9))
for row, (al, vmax) in enumerate(((0.02, 310), (0.1, 230))):
    four_readings(ax[row, 0], ax[row, 1], al, vmax); ax[row, 1].legend(loc="lower right", fontsize=7.5)
fig.tight_layout(); fig.savefig(os.path.join(here, "pg_v35_8_four_radii.png"), dpi=150)

# figure 2: the same comparison for the rest of the requested family, r_d/ell = 0.01, 0.05, 0.2 and 0.3
fig, ax = plt.subplots(4, 2, figsize=(12, 17))
for row, (al, vmax) in enumerate(((0.01, 420), (0.05, 240), (0.2, 200), (0.3, 165))):
    four_readings(ax[row, 0], ax[row, 1], al, vmax); ax[row, 1].legend(loc="upper right" if al == 0.01 else "lower right", fontsize=7)
fig.tight_layout(); fig.savefig(os.path.join(here, "pg_v35_8_four_radii_family.png"), dpi=120)

# figure 3: the family in gnomonic radius, sharp to broad, with the point source, and the asymptotic law
fig, ax = plt.subplots(1, 2, figsize=(12, 4.8))
R = np.logspace(-1.3, 3, 2000); t = R/ell; ps = (1+3*t*t)/(t*np.sqrt(1+t*t))
fam = ((0.005, "tab:purple"), (0.01, "tab:blue"), (0.02, "tab:red"), (0.05, "tab:olive"), (0.1, "tab:gray"), (0.2, "tab:orange"), (0.3, "tab:brown"))
for al, col in fam:
    v, veq, a2, mu, unit = pg._v358_pg_curve(al, ell); vg = v(np.arctan(R/ell))
    ax[0].semilogx(R, vg, color=col, label=f"$r_d/\\ell = {al}$  ($2r_d$ = {2*al*ell:.2f} kpc, $v_{{\\rm eq}}$ = {veq:.1f} km/s)")
    ax[1].semilogx(R, (veq**2-vg**2)*R**2/(veq**2*ell**2), color=col, label=f"$r_d/\\ell = {al}$: $-A/(v_{{\\rm eq}}^2\\ell^2)$ = {-a2/veq**2:.4f}")
ax[0].semilogx(R, np.sqrt(ps*unit), color="k", ls="--", lw=1, label="point source ($v_{\\rm eq}$ = %.1f km/s)" % np.sqrt(3*unit))
ax[0].axhline(np.sqrt(3*unit), color="k", lw=0.5, ls=":")
ax[0].set_xlabel("gnomonic radius $R = \\ell\\tan\\chi$ (kpc)"); ax[0].set_ylabel("$v$ (km/s)"); ax[0].set_ylim(0, 600); ax[0].grid(alpha=0.3, which="both")
ax[0].legend(fontsize=7, loc="upper right"); ax[0].set_title("PG's curves in gnomonic radius, sharp to broad: the equator at $R\\to\\infty$", fontsize=10)
ax[1].semilogx(R, (3-ps)*t*t/3, color="k", ls="--", label="point source: $\\to 1/6$")
ax[1].set_xlabel("gnomonic radius $R$ (kpc)"); ax[1].set_ylabel("$(v_{\\rm eq}^2-v^2)R^2/(v_{\\rm eq}^2\\ell^2)$"); ax[1].set_ylim(-0.1, 0.85)
ax[1].grid(alpha=0.3, which="both"); ax[1].legend(fontsize=7, loc="upper left")
ax[1].set_title("the approach to the plateau: $v^2 = v_{\\rm eq}^2 + A/R^2$, $A<0$", fontsize=10)
fig.tight_layout(); fig.savefig(os.path.join(here, "pg_v35_8_gnomonic_family.png"), dpi=150)

# figure 4: what a Newtonian reading in gnomonic radius infers for the sharp source (r_d/ell = 0.02)
al = 0.02; v, veq, a2, mu, unit = pg._v358_pg_curve(al, ell)
raw = lambda x: np.exp(-np.tan(x/2)/al)
tot = quad(lambda x: raw(x)*np.sin(x)**2, 0, PI, epsabs=1e-15, limit=400, points=[0.02, 0.1, 0.5])[0]
Rl = np.linspace(0.05, 100, 1200); cl = np.arctan(Rl/ell)
Fin = np.array([quad(lambda x: raw(x)*np.sin(x)**2, 0, c, epsabs=1e-15, limit=400)[0] for c in cl])/tot   # the leaf's mass inside, a fraction of M
vpg = v(cl); vn = np.sqrt(Gk*M*Fin/Rl)
fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
ax[0].plot(Rl, vpg, color="tab:red", label="PG (Part XXV), read in gnomonic radius")
ax[0].plot(Rl, vn, color="k", ls="--", label="Newtonian, from the leaf's own mass at its gnomonic radii")
ax[0].fill_between(Rl, vn, vpg, where=vpg > vn, color="tab:red", alpha=0.08)
ax[0].set_xlim(0, 100); ax[0].set_ylim(0, 310); ax[0].set_xlabel("gnomonic radius $R$ (kpc)"); ax[0].set_ylabel("$v$ (km/s)"); ax[0].grid(alpha=0.3)
ax[0].legend(fontsize=8, loc="upper right"); ax[0].set_title(f"$r_d/\\ell = {al}$: the curve stays flat where the leaf's mass has run out", fontsize=10)
ax[1].plot(Rl, Rl*vpg**2/(Gk*M), color="tab:red", label="$Rv^2/(GM)$: the mass a Newtonian reading infers")
ax[1].plot(Rl, Fin, color="k", ls="--", label="the leaf's own mass inside $R$")
ax[1].set_xlim(0, 100); ax[1].set_ylim(0, 20); ax[1].set_xlabel("gnomonic radius $R$ (kpc)"); ax[1].set_ylabel("$M(<R)/M$, $M = 6\\times10^{10}M_\\odot$")
ax[1].grid(alpha=0.3); ax[1].legend(fontsize=8, loc="upper left")
ax[1].set_title("a Newtonian reading: $M(<R)\\propto R$, as an isothermal halo's", fontsize=10)
fig.tight_layout(); fig.savefig(os.path.join(here, "pg_v35_8_mass_discrepancy.png"), dpi=150)
print("wrote pg_v35_8_four_radii.png, pg_v35_8_four_radii_family.png, pg_v35_8_gnomonic_family.png and pg_v35_8_mass_discrepancy.png")
print(f"  r_d/ell = {al}: R v^2/(G M) at 10, 20, 50, 100 kpc = " + ", ".join(f"{float(r*v(np.arctan(r/ell))**2/(Gk*M)):.1f}" for r in (10.0, 20.0, 50.0, 100.0)))
