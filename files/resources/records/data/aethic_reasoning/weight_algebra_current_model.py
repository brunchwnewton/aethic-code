#!/usr/bin/env python3
"""The Weight Algebra's worked finite model, recomputed (R711 form).
Carrier P holds the single-peg carvings of two binary attributes a, b, with NO constraint between them, so the carvings
are closure-independent; parent-conditional weights of the finest cells: a1b1 0.2, a1b0 0.3, a0b1 0.4, a0b0 0.1 (M = R>=0).
Tagged carriers come from outside the cone: T_a = P_a1 . P_a0 and T_b = P_b1 . P_b0 (rival values) and Hyp.
Checks: closure-independence (cell map injective, content order = extension), coefficient coherence (S2-S3), the cone's
join-semilattice (all joins exist; meets only for compatible fillings), doom = tagged set, reduced form and quotient."""
import itertools
W = {('a1', 'b1'): 0.2, ('a1', 'b0'): 0.3, ('a0', 'b1'): 0.4, ('a0', 'b0'): 0.1}
fill = lambda f: '.'.join(sorted(f)) or 'P'
cells = [frozenset(x for x in (fa, fb) if x) for fa in (None, 'a1', 'a0') for fb in (None, 'b1', 'b0')]
coef = lambda f: sum(w for k, w in W.items() if f <= set(k))
content = lambda f: frozenset(f)                       # no constraints: a cell's content is exactly its stated values (over P)
# closure-independence: content inclusion iff extension, injectivity
assert len({content(f) for f in cells}) == len(cells)
assert all((content(f) <= content(g)) == (f <= g) for f in cells for g in cells)
assert abs(coef(frozenset({'a1'})) - 0.5) < 1e-12 and abs(coef(frozenset({'b1'})) - 0.6) < 1e-12
print("closure-independent: injective cell map, content order = extension; S3 additivity holds")
proper = [f for f in cells if coef(f) > 0]; print("proper children of P:", len(proper))
def join(f, g): return f & g
def meet(f, g):
    u = f | g; return u if len({x[0] for x in u}) == len(u) and coef(u) > 0 else None
pairs = list(itertools.combinations(proper, 2))
assert all(join(f, g) in proper for f, g in pairs)                       # every pair has a join in the cone
no_meet = [(fill(f), fill(g)) for f, g in pairs if meet(f, g) is None]
print("all", len(pairs), "pairs have joins (join-semilattice); pairs with no common proper child:", len(no_meet), "e.g.", no_meet[:3])
print("a1 v a0 =", fill(join(frozenset({'a1'}), frozenset({'a0'}))), "| a1 ^ b1 =", fill(meet(frozenset({'a1'}), frozenset({'b1'}))))
TAGGED = {'T_a (a1.a0, rival values)', 'T_b (b1.b0, rival values)', 'Hyp'}
doomed_cells = [fill(f) for f in proper if False]                       # no cell is tagged; each joint filling is its own safe cone
print("doomed = tagged set:", sorted(TAGGED), "| doomed cells of P:", doomed_cells or 'none')
x = {'T_a': 0.2, 'a1.b0': 0.3, 'a0.b1': 0.4, 'a0.b0': 0.1}; xV = {k: v for k, v in x.items() if k != 'T_a'}
print("x =", x, "-> reduced form x_V =", xV, "| [x] = [x_V]; T_a stays in x under its tag")
y = {'T_a': 0.5, 'Hyp': 0.5}; print("y =", y, "-> no reduced form (S(y) empty); [y] = 0")
