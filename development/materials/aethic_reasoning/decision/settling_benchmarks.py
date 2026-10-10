#!/usr/bin/env python3
"""The settling rule of Definition def:settle, run on each benchmark.  Python 3, standard library only.
A model: variables with finite domains, one kernel per variable given its parents (a DAG), the act C with production
kernel P0(c | pa(C)), couplings = kernels of C's children, each with a mode set.  Settling act a in mode mu:
every replacement kernel is computed from the ORIGINAL model; (1) C's production kernel -> point mass at a; (2) couplings
with mu in m(e) retained; (3) couplings with mu not in m(e) replaced jointly by K(o | pa(C), z) =
sum_c P0(c | pa(C)) prod_e f_e(o_e | c, o_[pa(e) in O], z_[pa(e) in Z]), O their outputs, Z their parents outside O and C;
then restrict to the evidence E, marginalize to Y, normalize; a zero normalizer = inadmissible under the model."""
import itertools
def settle(V, dom, par, ker, act, a, modes, mu, E, Y):
    children = [v for v in V if act in par[v]]
    O = [v for v in children if mu not in modes[v]]
    def P0(c, assign): return ker[act](c, {p: assign[p] for p in par[act]})
    total = {}; norm = 0.0
    for vals in itertools.product(*[dom[v] for v in V]):
        s = dict(zip(V, vals))
        if s[act] != a or any(s[k] != v for k, v in E.items()): continue
        w = 1.0
        for v in V:
            if v == act or v in O: continue                      # act fixed (point mass); detached block handled jointly
            w *= ker[v](s[v], {p: s[p] for p in par[v]})       # retained kernels, original
        if O:                                                    # joint detached kernel, act integrated out under P0
            kj = sum(P0(c, s) * __import__('math').prod(ker[o](s[o], {p: (c if p == act else s[p]) for p in par[o]}) for o in O) for c in dom[act])
            w *= kj
        key = tuple(s[y] for y in Y); total[key] = total.get(key, 0.0) + w; norm += w
    return None if norm == 0 else {k: v / norm for k, v in total.items()}
M, t = 1e6, 1e3
def newcomb(binding, eps=0.01, evidence=None):
    V = ['C', 'B']; dom = {'C': ('one', 'two'), 'B': ('full', 'empty')}; par = {'C': [], 'B': ['C']}
    ker = {'C': lambda c, p: 0.5, 'B': lambda b, p: (1 - eps if (b == 'full') == (p['C'] == 'one') else eps)}
    modes = {'B': {'deliberation', 'habit', 'randomizer'} if binding else {'habit'}}
    out = {}
    for a in dom['C']:
        Q = settle(V, dom, par, ker, 'C', a, modes, 'deliberation', evidence or {}, ['B'])
        if Q is None: out[a] = 'inadmissible'; continue
        pay = lambda b: (M if b == 'full' else 0) + (t if a == 'two' else 0)
        out[a] = round(sum(q * pay(b) for (b,), q in Q.items()), 2)
    return out
print("Opaque Newcomb, accuracy 0.99 binding:     ", newcomb(True))
print("Opaque Newcomb, accuracy not binding:      ", newcomb(False))
print("Transparent, full box, eps = 0.01:         ", newcomb(True, 0.01, {'B': 'full'}))
print("Transparent, full box, eps = 0:            ", newcomb(True, 0.0, {'B': 'full'}))
def lesion():
    V = ['L', 'R', 'C', 'K']; dom = {'L': (1, 0), 'R': (1, 0), 'C': ('smoke', 'refrain'), 'K': (1, 0)}
    par = {'L': [], 'R': ['L'], 'C': ['R'], 'K': ['L']}
    ker = {'L': lambda l, p: 0.5, 'R': lambda r, p: (0.9 if r == p['L'] else 0.1), 'C': lambda c, p: (0.8 if (c == 'smoke') == (p['R'] == 1) else 0.2), 'K': lambda k, p: (0.7 if k == p['L'] else 0.3)}
    out = {}
    for a in dom['C']:
        Q = settle(V, dom, par, ker, 'C', a, {}, 'deliberation', {'R': 1}, ['K'])
        out[a] = round(Q[(1,)], 4)
    return out
print("Lesion, resolve stated, P(cancer):         ", lesion(), "(equal: dominance, smoke)")
def button(q0=0.1, q1=0.9, Bv=1.0, Dv=1.0):
    V = ['C', 'T']; dom = {'C': ('press', 'refrain'), 'T': ('psycho', 'not')}; par = {'C': [], 'T': ['C']}
    ker = {'C': lambda c, p: 0.5, 'T': lambda tt, p: ((q1 if p['C'] == 'press' else q0) if tt == 'psycho' else (1 - (q1 if p['C'] == 'press' else q0)))}
    out = {}
    for a in dom['C']:
        Q = settle(V, dom, par, ker, 'C', a, {'T': {'deliberation', 'habit', 'randomizer'}}, 'deliberation', {}, ['T'])
        out[a] = round(sum(q * ((-Dv if tt == 'psycho' else Bv) if a == 'press' else 0) for (tt,), q in Q.items()), 3)
    return out
print("Psychopath button, (J2) binding, B=D=1:    ", button(), "(refrain iff q1 > B/(B+D))")
def internal():
    V = ['C', 'O1', 'O2']; dom = {'C': (1, 0), 'O1': (1, 0), 'O2': (1, 0)}; par = {'C': [], 'O1': ['C'], 'O2': ['C', 'O1']}
    ker = {'C': lambda c, p: 0.5, 'O1': lambda o, p: 1.0 if o == p['C'] else 0.0, 'O2': lambda o, p: 1.0 if o == p['O1'] else 0.0}
    return settle(V, dom, par, ker, 'C', 1, {'O1': set(), 'O2': set()}, 'deliberation', {}, ['O1', 'O2'])
print("Detached block with O1 -> O2 inside O:     ", internal(), "(O1 = O2 kept; act integrated out)")
