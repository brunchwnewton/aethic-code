# newton_timing.py — timing as a trait of a task-human: the Newton case (long Golden Reasoning paper, task-objects,
# "Timing, the lattice, and the Newton case"). Exposure is measured in ELIGIBLE births, E(t) = e(t) b(t), with b the birth
# rate and e the fraction of births with the opportunity to develop and express the traits. Under aimless optimation the
# count of T-qualified people born in a window W is Poisson with mean alpha_W = pi(T) E(W), and the timing trait is
# independent of the trait set (jointness 1). All demographic inputs are order-of-magnitude and declared below.
import numpy as np

# --- demographic inputs (order of magnitude; vary them) ----------------------------------------------------------
B_total = 1.17e11          # humans ever born, to 2022 (PRB-type estimate)
B_by_1650 = 6.1e10         # cumulative births by about 1650 (same source family)
births_per_year_1642 = 2.2e7   # world population ~5.5e8 at a crude birth rate ~40/1000
window_years = 20          # width of the "right time" window around 1642 (vary 10..30)
e_W = 0.02                 # eligible fraction of world births in the window (access to mathematics; vary 0.005..0.05)
E_post = 5.0e9             # eligible births since 1650, worldwide (vary 2e9..1e10)
k_since = 0                # Newton-class people (full trait set T) born since; the author's premise is 0; vary 0..3

def report(window_years=window_years, e_W=e_W, E_post=E_post, k_since=k_since):
    B_W = births_per_year_1642 * window_years
    E_W = e_W * B_W
    R = E_W / E_post                                   # window's share of eligible exposure since 1650
    # upper bound on pi(T) from k_since realizations among E_post: 95% Poisson upper bound on the mean
    ub = {0: 3.0, 1: 4.74, 2: 6.30, 3: 7.75}[k_since]   # Poisson 95% upper limits on the mean for k observed
    pi_T_ub = ub / E_post
    pi_T_pt = max(k_since, 1) / E_post                 # point estimate (at least one such person existed: Newton)
    alpha_W_ub, alpha_W_pt = pi_T_ub * E_W, pi_T_pt * E_W
    p_realized_aimless = 1 - np.exp(-alpha_W_pt)      # aimless probability that a qualified person is born in W
    bayes_factor = 1 / p_realized_aimless              # if Golden conditioning makes the realization in W ~certain
    f_rank = B_W / B_total                             # window as a fraction of all births (rank-space width)
    return dict(B_W=B_W, E_W=E_W, R=R, pi_T_ub=pi_T_ub, pi_T_pt=pi_T_pt, alpha_W_ub=alpha_W_ub, alpha_W_pt=alpha_W_pt,
                p_realized_aimless=p_realized_aimless, bayes_factor=bayes_factor, f_rank=f_rank,
                jointness_required=1 / R, kappa_equiv=1 / R - 1)

if __name__ == "__main__":
    r = report()
    print("Baseline (20-yr window, e_W = 0.02, E_post = 5e9, k_since = 0):")
    for key, val in r.items(): print(f"  {key:22s} {val:.3g}")
    print("\nSensitivity: alpha_W (point) and Bayes factor over the ranges")
    print(f"{'window':>7} {'e_W':>6} {'E_post':>8} {'k':>2} | {'R':>8} {'alpha_W':>8} {'BF':>8} {'pi(T) ub':>9}")
    for w in (10, 20, 30):
        for e in (0.005, 0.02, 0.05):
            for Ep in (2e9, 5e9, 1e10):
                for k in (0, 1, 3):
                    r = report(w, e, Ep, k)
                    print(f"{w:7d} {e:6.3f} {Ep:8.0e} {k:2d} | {r['R']:8.2e} {r['alpha_W_pt']:8.3f} {r['bayes_factor']:8.1f} {r['pi_T_ub']:9.1e}")
    # the lattice anchor: Leibniz in the window for the calculus sub-task
    r = report()
    alpha_calc_W = 2.0                                  # two realizers of the calculus sub-task in the window (Newton, Leibniz)
    pi_calc = alpha_calc_W / r['E_W']
    cond_top = r['pi_T_ub'] / pi_calc
    print(f"\nLattice anchor: pi(S_calc) ~ 2/E_W = {pi_calc:.2e}; conditional pi(T | S_calc) <= {cond_top:.3g} (95%): "
          f"a calculus-capable person of the window completes the full set with probability at most ~{100*cond_top:.1f}%.")

# ---------------------------------------------------------------------------------------------------------------
# Nexic coupling: why the species did not evolve around the fluke (Proposition "Evolutionary locking").
# The top-lattice tail pi(T) = Phibar(z) responds to a shift dmu of the species' trait mean (in sd units) at the hazard
# rate h(z) = phi(z)/Phibar(z) ~ z nats per sd. Erasing a fluke of F nats needs dmu = F/h. Under Golden conditioning the
# realized route (no shift, fluke paid) is accordance-admissible at level kappa only if the evolutionary cost V(dmu) of
# the shift (plus integration side effects S) satisfies V + S >= h dmu - ln(1+kappa) for every dmu: the "lock".
from scipy.stats import norm as _norm
def hazard(z): return float(np.exp(_norm.logpdf(z) - _norm.logsf(z)))
if __name__ == "__main__":
    r = report(); F = -np.log(r['alpha_W_pt'])
    print(f"\nNexic coupling / evolutionary lock: fluke cost F = -ln(alpha_W) = {F:.2f} nats")
    for p in (1e-8, 1e-9, 1e-10):
        z = _norm.isf(p); h = hazard(z)
        print(f"  pi(T) = {p:.0e}: z = {z:.2f} sd, hazard h = {h:.2f} nats/sd, shift erasing the fluke = F/h = {F/h:.2f} sd; "
              f"lock at kappa=9: V(1 sd) >= {h - np.log(10):.1f} nats ({np.exp(h - np.log(10)):.0f}-fold), V(2 sd) >= {2*h - np.log(10):.1f} nats ({np.exp(2*h - np.log(10)):.0e}-fold)")
