"""Projective Gravity v41.0: the idle galaxies on the root law, and tilts against the stretches fitted -- the companion computation of Sections
XXXIX.3 and XXXIX.8(g).  It fits nothing: it reads v40.4's and v40.5's saved results (results/ and results405/, unchanged) and prints.

Usage, from the directory of pg_v41_numerics.py, after pg_v404_sparc.py and pg_v405_sparc.py have run:
    python3 -I galaxy_sims/sparc175/pg_v41_sparc.py            # the report (a few seconds)
An unknown mode prints the usage line and exits with status 2.

v41.0-S1  the 36 galaxies whose leaves v40.4 found idle (v40.4-3: the hybrid's leaf, no floor, beyond 10 R_last): what the root the light sets,
          B and the push each do on them, against NFW and B times Newton at SPARC's ratios.
v41.0-S2  three tilt forms against the stretches v40.5 fitted (v40.5-11, the root law, three numbers, the potential law, B = 1): the averaged
          quotient of a squashed shell (Section XXVI.9), the normal ray's lane mismatch made a stretch (Section XXXVIII.12(f)), and a uniform
          tilt of the reference; and the lanes' cosine, the leaf's radius and the stretch against Hubble type.
Every number the archive quotes from this computation is printed below as a whole token.  Fits are fits: these are v40.4's and v40.5's."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SUITE = os.path.abspath(os.path.join(HERE, '..', '..'))
if HERE not in sys.path: sys.path.insert(0, HERE)
if SUITE not in sys.path: sys.path.insert(0, SUITE)
import math, pickle
import numpy as np
from scipy.optimize import minimize_scalar
import pg_v405_sparc as PG
import sp_nuis as nuis
P = nuis.P; G = PG.G; T1 = PG.T1; su = PG.su; nY = PG.nY; med = PG.med


def load(stage, res): return pickle.load(open(os.path.join(HERE, res, stage + '.pkl'), 'rb'))


def head(t): print('\n== ' + t)


def main():
    Bs = load('base', 'results'); S1 = load('sin', 'results405'); T = load('tan', 'results405'); RF = load('refine', 'results405')
    BF = load('bfree', 'results405'); HB = load('hybrid', 'results405'); PR = load('profiles', 'results405')
    print('Projective Gravity v41.0: the idle galaxies on the root law, and tilts against the fitted stretches; SPARC (Lelli, McGaugh and Schombert '
          '2016), %d galaxies; v40.4\'s and v40.5\'s saved results, read, not refitted' % len(G))
    AN = {n: Bs[n]['nfw']['chi2'] + Bs[n]['nfw']['pri'] + 2*(2 + nY(n) + 2) for n in G}
    k3 = ('leaf', 'tanmix', 'potential', False, 2)
    final = {n: (RF[n][k3] if RF[n][k3]['obj'] < T[n][k3]['obj'] else T[n][k3]) for n in G}

    # ------------------------------------------------------------------ v41.0-S1
    head('v41.0-S1. The idle galaxies (v40.4-3: the hybrid\'s leaf beyond 10 R_last with no floor) on the root law (Section XXXIX.3)')
    idle = [n for n in G if Bs[n]['free']['ell'] > 10*su(n)['R'][-1]]; rest = [n for n in G if n not in idle]
    RL = {n: su(n)['R'][-1] for n in G}; R1 = {n: su(n)['R'][0] for n in G}; Rd = {n: T1[n]['Rd'] for n in G}; N = {n: su(n)['g']['N'] for n in G}
    print('-- %d idle, %d others; points per idle galaxy, median %.0f' % (len(idle), len(rest), med([N[n] for n in idle])))
    nfw = sum(Bs[n]['nfw']['chi2'] for n in idle); nfwA = sum(AN[n] for n in idle)
    bn = {}
    for n in idle:
        s = su(n); c2, B, _ = P._v43_amp(P._v43_sq(s['g']['vb2']), s['V'], s['E']); c2b, Bb, _ = P._v43_amp(P._v43_sq(nuis.vbar2(s, 0.5, 0.7)), s['V'], s['E'])
        assert abs(c2 - c2b) < 1e-9*max(1, c2) and abs(B - Bb) < 1e-9*max(1, B), n
        bn[n] = (c2, B)
    print('   NFW with the nuisances: chi2 %.0f, AIC-like %.0f' % (nfw, nfwA))
    print('   B times Newton at SPARC\'s ratios (v40.4-3), B in closed form: chi2 %.0f, AIC-like (chi2 + 2) %.0f, better than NFW (AIC-like) for %d; '
          'B median %.2f (16-84%% %.2f-%.2f)' % (sum(v[0] for v in bn.values()), sum(v[0] + 2 for v in bn.values()),
                                                 sum(bn[n][0] + 2 < AN[n] for n in idle), med([v[1] for v in bn.values()]),
                                                 PG.q16([v[1] for v in bn.values()]), PG.q84([v[1] for v in bn.values()])))
    top = max(idle, key=lambda n: bn[n][0])
    print('   the same: median chi2/(N - 1) %.3f; %s alone carries chi2 %.0f, the other %d %.0f' % (med([bn[n][0]/max(N[n] - 1, 1) for n in idle]), top,
          bn[top][0], len(idle) - 1, sum(bn[n][0] for n in idle if n != top)))
    k1 = ('leaf', 'one', 'potential', False, 'n')
    rows = [('one exponential in sin chi set by the light, no push, B = 1 (the root of v40.4\'s form)', {n: S1[n][k1]
                                                                                                         for n in idle}, 2, 0),
            ('the mixture in tan chi set by the light, no push, B = 1 (the root law)', {n: T[n][('leaf', 'tanmix', 'potential', False, 'n')]
                                                                                         for n in idle}, 2, 0),
            ('the root law, no push, B free', {n: BF[n][('leaf', 'tanmix', 'potential', True, 'n')] for n in idle}, 3, 0),
            ('the root law, three numbers of push, B = 1', {n: final[n] for n in idle}, 2, 3)]
    for lab, q, base, npush in rows:
        a = {n: q[n]['obj'] + 2*(base + nY(n) + npush) for n in idle}
        extra = ''
        if base == 3: extra = '; B median %.2f (16-84%% %.2f-%.2f)' % (med([q[n]['B'] for n in idle]), PG.q16([q[n]['B'] for n in idle]),
                                                                      PG.q84([q[n]['B'] for n in idle]))
        print('   %s: chi2 %.0f, AIC-like %.0f, better than NFW (AIC-like) for %d, in chi2 for %d; median chi2/N %.2f; ell over R_last median %.2f; '
              'ell beyond 10 R_last for %d, beyond 100 R_d for %d; the light beyond the tolerance for %d%s' % (
                  lab, sum(q[n]['chi2'] for n in idle), sum(a.values()), sum(a[n] < AN[n] for n in idle),
                  sum(q[n]['chi2'] < Bs[n]['nfw']['chi2'] for n in idle), med([q[n]['chi2']/N[n] for n in idle]), med([q[n]['ell']/RL[n] for n in idle]),
                  sum(q[n]['ell'] > 10*RL[n] for n in idle), sum(q[n]['ell'] > 100*Rd[n] for n in idle), sum(q[n]['ex'] > 9.5 for n in idle), extra))
    st = {n: PG.stretches(final[n], n) for n in G}
    print('   the root law, three numbers: the stretch at mid radius, median %.2f on the idle (16-84%% %.2f-%.2f), %.2f on the other %d' % (
          med([st[n][1] for n in idle]), PG.q16([st[n][1] for n in idle]), PG.q84([st[n][1] for n in idle]), med([st[n][1] for n in rest]), len(rest)))
    hl = {n: HB[n]['light'] for n in idle}; hf = {n: HB[n]['free'] for n in idle}; h4 = {n: Bs[n][('light', 9.0)] for n in idle}
    col = [n for n in idle if hf[n]['ell'] < R1[n]]
    print('   the hybrid (Section XXXVIII.38\'s model) with the root law, held to the light: chi2 %.0f against v40.4\'s %.0f; the leaf beyond 10 R_last '
          'for %d, beyond 100 R_d for %d; B median %.2f' % (sum(v['chi2'] for v in hl.values()), sum(v['chi2'] for v in h4.values()),
                                                           sum(hl[n]['ell'] > 10*RL[n] for n in idle), sum(hl[n]['ell'] > 100*Rd[n] for n in idle),
                                                           med([v['B'] for v in hl.values()])))
    print('   the same, any leaf: chi2 %.0f; the leaf inside the first measured radius for %d, its B there median %.4f; beyond 10 R_last for %d' % (
          sum(v['chi2'] for v in hf.values()), len(col), med([hf[n]['B'] for n in col]) if col else float('nan'),
          sum(hf[n]['ell'] > 10*RL[n] for n in idle)))

    # ------------------------------------------------------------------ v41.0-S2
    head('v41.0-S2. Tilts against the stretches fitted in v40.5 (v40.5-11), nine radii per galaxy along each fitted push (Section XXXIX.8(g))')
    H = [n for n in sorted(PR) if not PR[n]['synth']]

    def prof(p, f):
        Lr = math.log(p['RN']/p['R1']); Rv = p['R1']*math.exp(f*Lr)
        s = p['s_in']*math.exp((1 - p['q1'])*f*Lr) if f <= 0.5 else p['s_mid']*math.exp((1 - p['q2'])*(f - 0.5)*Lr); return Rv, s
    F9 = np.linspace(0, 1, 9)
    shell = lambda ch, be: 0.5*np.log(1 + 0.5*np.sin(be)**2*(1/(4*np.sin(ch)**2) - 1))
    phase = lambda ch, ka: ka*2*np.pi*(1 - np.cos(ch))
    rows = {}; cnt = dict(in30_gt=0, in30=0, out30_gt=0, out30=0)
    for n in H:
        p = PR[n]; pts = [prof(p, f) for f in F9]; xs = np.array([Rv/p['ell'] for Rv, s in pts]); ls = np.log(np.array([s for Rv, s in pts]))
        chi = np.degrees(np.arctan(xs/np.exp(ls)))
        for c1, l1 in zip(chi, ls):
            if c1 < 30: cnt['in30'] += 1; cnt['in30_gt'] += l1 > 0
            else: cnt['out30'] += 1; cnt['out30_gt'] += l1 > 0
        rms = lambda m: float(np.sqrt(np.mean((ls - m)**2)))
        cr = np.radians(chi); fS = minimize_scalar(lambda be: rms(shell(cr, be)), bounds=(0, np.pi/2), method='bounded')
        fP = minimize_scalar(lambda ka: rms(phase(cr, ka)), bounds=(-30, 30), method='bounded')
        rows[n] = dict(r0=rms(0), rC=rms(ls.mean()), rS=fS.fun, be=fS.x, rP=fP.fun, ka=fP.x, rP1=rms(phase(cr, 1.0)), chi_mid=chi[4], chi_out=chi[8],
                       trend=ls[8] - ls[0], A_mid=-np.cos(2*np.radians(chi[4])), A_out=-np.cos(2*np.radians(chi[8])))
    md = lambda k: float(np.median([rows[n][k] for n in H]))
    print('-- %d galaxies with measured light; the fitted points\' leaf angle, arctan(r/ell) at the pre-push radius r: median %.1f deg at mid radius, '
          '%.1f deg at the last' % (len(H), md('chi_mid'), md('chi_out')))
    print('   the averaged quotient of a squashed shell, ln s = (1/2) ln(1 + (1/2) sin^2 beta (1/(4 sin^2 chi) - 1)), stretches inside chi = 30 deg and '
          'squeezes outside: the fits stretch %d of %d points inside 30 deg and %d of %d outside' % (cnt['in30_gt'], cnt['in30'], cnt['out30_gt'],
                                                                                                     cnt['out30']))
    print('   it falls outward for every galaxy; the lane mismatch made a stretch, ln s = kappa 2 pi (1 - cos chi), rises for every kappa > 0; the '
          'fitted stretch rises from the first radius to the last for %d of %d' % (sum(rows[n]['trend'] > 0 for n in H), len(H)))
    print('   rms misfit in ln(stretch), median over galaxies: no stretch %.3f; one constant per galaxy %.3f; one tilt beta per galaxy on the squashed '
          'shells %.3f; one factor kappa per galaxy on the lane mismatch %.3f; kappa = 1 %.3f' % (md('r0'), md('rC'), md('rS'), md('rP'), md('rP1')))
    print('   better than one constant per galaxy: the squashed shell\'s tilt for %d of %d, the lane mismatch for %d; the tilts fitted, median %.1f deg, '
          'at the 90 deg bound for %d; the factors fitted, median %.2f' % (sum(rows[n]['rS'] < rows[n]['rC'] for n in H), len(H),
                                                                            sum(rows[n]['rP'] < rows[n]['rC'] for n in H), np.degrees(md('be')),
                                                                            sum(rows[n]['be'] > np.pi/2 - 1e-3 for n in H), md('ka')))
    sm = np.array([PR[n]['s_mid'] for n in H])
    print('   a tilt p of the reference at fixed Ernst data scales every length by 1/cos p (Section XXXVII.7(a)): the fitted mid-radius stretches '
          'read so would be tilts of median %.1f deg, for the %d of %d that exceed 1' % (np.degrees(np.arccos(1/np.median(sm[sm > 1]))), (sm > 1).sum(),
                                                                                          len(H)))
    Tt = [T1[n]['T'] for n in H]; Mb = [math.log(su(n)['g']['Mb']) for n in H]; bul = np.array([bool(su(n)['bul']) for n in H])

    def part(x, y, z):
        rxy, rxz, ryz = PG.spear(x, y), PG.spear(x, z), PG.spear(y, z); return (rxy - rxz*ryz)/math.sqrt((1 - rxz**2)*(1 - ryz**2))
    print('   against Hubble type, rank correlation (P by 3000 permutations), the same at fixed baryonic mass, and the medians with and without a '
          'bulge:')
    for nm, v in (('leaf radius over R_d', [PR[n]['ell']/PR[n]['Rd'] for n in H]), ('lanes\' cosine at mid radius', [rows[n]['A_mid'] for n in H]),
                  ('lanes\' cosine at the last radius', [rows[n]['A_out'] for n in H]), ('stretch at mid radius', list(sm))):
        v = np.array(v)
        print('   %-32s %+.2f (P %.3f), %+.2f; with a bulge %.2f (%d), without %.2f (%d)' % (nm, PG.spear(v, Tt), PG.perm_p(list(v), Tt, 3000, 11),
                                                                                         part(list(v), Tt, Mb), np.median(v[bul]), bul.sum(),
                                                                                         np.median(v[~bul]), (~bul).sum()))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'report'
    if mode != 'report':
        print('usage: python3 -I galaxy_sims/sparc175/pg_v41_sparc.py [report]'); sys.exit(2)
    main()
