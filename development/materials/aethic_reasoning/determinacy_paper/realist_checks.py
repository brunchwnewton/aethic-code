#!/usr/bin/env python3
"""Checks for "Determinacy as a Two-Place Relation" (the determinacy paper), October 2026 revision.

Requires numpy. Run `python3 realist_checks.py`.
  1. The converse of the conditional record-exclusion lemma: for a candidate outside the base,
     A is invalid under V = nu Phi exactly when every declared refinement has a base-reaching
     descendant (random reflexive-transitive descent relations; reflexivity and transitivity only).
  2. The worked laboratory model: internal record only gives P(+) = 1 at the SM boundary; a
     separating external record gives 1/2; enclosing it restores 1.
  3. Frauchiger-Renner: P(ok,ok) = 1/12 coherent, 1/4 fully dephased in the product record basis,
     1/12 with either single laboratory dephased; the two (Q) inferences the account rejects.
"""
import random, itertools
import numpy as np

# ---------- 1. Greatest fixed point V = nu Phi, and the converse of the record-exclusion lemma ----------
def gfp(U, le, Base):
    # Phi(S) = {A in U\Base : exists B<=A forall C<=B, C in S}; V = greatest fixed point, iterate from U.
    S = set(U)
    while True:
        T = {A for A in U if A not in Base and any(all(C in S for C in U if le(C, B)) for B in U if le(B, A))}
        if T == S: return S
        S = T
def random_preorder(n, p, rng):
    # random reflexive-transitive relation: start from random DAG edges plus some cycles, then take reflexive-transitive closure
    R = [[i == j for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and rng.random() < p: R[i][j] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if R[i][k] and R[k][j]: R[i][j] = True
    return lambda b, a: R[b][a]   # le(B, A): B is a declared descendant of A  (encode R[B][A])
rng = random.Random(20261009); bad = 0; tested = 0; base_cases = 0
for trial in range(4000):
    n = rng.randint(2, 7); le = random_preorder(n, rng.random() * 0.5, rng)
    U = list(range(n)); Base = {x for x in U if rng.random() < 0.3}
    V = gfp(U, le, Base)
    # universal predicate satisfies the safety implication trivially; check V excludes Base and is a fixed point
    assert not (V & Base)
    for A in U:
        cond = all(any(C in Base for C in U if le(C, B)) for B in U if le(B, A))   # forall B<=A exists C<=B in Base
        if cond: assert A not in V            # the lemma (sufficiency)
        if A not in Base:
            tested += 1
            if (A not in V) != cond: bad += 1  # converse, for A outside Base, without hereditary Base
        else:
            base_cases += 1
print(f"converse of the lemma on {tested} non-base candidates over 4000 random preorders: failures = {bad}; base cases skipped = {base_cases}")
# also show that WITHOUT restricting to A notin Base the equivalence can fail unless Base is hereditary
fails_nonhered = 0
for trial in range(4000):
    n = rng.randint(2, 7); le = random_preorder(n, rng.random() * 0.5, rng)
    U = list(range(n)); Base = {x for x in U if rng.random() < 0.3}
    V = gfp(U, le, Base)
    for A in Base:
        cond = all(any(C in Base for C in U if le(C, B)) for B in U if le(B, A))
        if not cond: fails_nonhered += 1
print(f"base candidates whose descendants are not all base-reaching (equivalence needs A outside Base or hereditary Base): {fails_nonhered}")

# ---------- 2. Worked model: internal record (SM) vs separating record (E outside the boundary) ----------
k0 = np.array([1,0]); k1 = np.array([0,1])
def kron(*v):
    out = np.array([1.0])
    for x in v: out = np.kron(out, x)
    return out
psi_SM = (kron(k0,k0) + kron(k1,k1)) / np.sqrt(2)
plus_SM = (kron(k0,k0) + kron(k1,k1)) / np.sqrt(2)
print("case (a) internal record only: P(+) at boundary SM =", round(abs(plus_SM @ psi_SM)**2, 6))
psi_SME = (kron(k0,k0,k0) + kron(k1,k1,k1)) / np.sqrt(2)      # E = orthogonal external copy of the outcome
rho = np.outer(psi_SME, psi_SME.conj()).reshape(4,2,4,2); rho_SM = np.einsum('iaja->ij', rho)
print("case (b) separating record in E: P(+) at boundary SM =", round(float(plus_SM @ rho_SM @ plus_SM), 6),
      "; reduced SM state diagonal in the record basis:", np.allclose(rho_SM, np.diag(np.diag(rho_SM))))
plus_SME = (kron(k0,k0,k0) + kron(k1,k1,k1)) / np.sqrt(2)
print("case (b) at boundary SME (control encloses E): P(+) =", round(abs(plus_SME @ psi_SME)**2, 6))

# ---------- 3. Frauchiger-Renner: 1/12 coherent, 1/4 fully dephased (product record basis), 1/12 single-lab dephasing ----------
h, t = k0, k1; dn, up = k0, k1
Psi = (kron(h,dn) + kron(t,dn) + kron(t,up)) / np.sqrt(3)
okbar = (h - t)/np.sqrt(2); ok = (dn - up)/np.sqrt(2); failbar = (h + t)/np.sqrt(2); fail = (dn + up)/np.sqrt(2)
proj = lambda v: np.outer(v, v)
P = lambda rho, a, b: float(np.real(np.trace(rho @ np.kron(proj(a), proj(b)))))
rho_coh = np.outer(Psi, Psi)
rho_mix = sum(np.outer(v, v) for v in [kron(h,dn), kron(t,dn), kron(t,up)]) / 3
def dephase(rho, which):   # dephase in the record basis of lab 'which' (0 = coin lab Fbar, 1 = spin lab F)
    out = np.zeros_like(rho)
    for v in [k0, k1]:
        Pv = np.kron(proj(v), np.eye(2)) if which == 0 else np.kron(np.eye(2), proj(v))
        out += Pv @ rho @ Pv
    return out
print("FR P(okbar,ok): coherent =", round(P(rho_coh, okbar, ok), 6), "; fully dephased product record basis =", round(P(rho_mix, okbar, ok), 6),
      "; dephase Fbar only =", round(P(dephase(rho_coh, 0), okbar, ok), 6), "; dephase F only =", round(P(dephase(rho_coh, 1), okbar, ok), 6))
# the two (Q) inferences the account locates: coherent 'if t then W sees fail' (certain) and 'if okbar then spin up' (certain); under full dephasing neither is certain
rho_t = np.outer(kron(t, fail), kron(t, fail))      # conditional on coin t, lab F in state (dn+up)/sqrt2 = fail  (coherent)
print("coherent P(W=fail | coin t) =", round(P(rho_t, t, fail)/P(rho_t, t, dn) if False else float(np.real(np.trace(rho_t @ np.kron(np.eye(2), proj(fail))))), 6))
rho_t_deph = dephase(rho_t, 1)
print("dephased-F P(W=fail | coin t) =", round(float(np.real(np.trace(rho_t_deph @ np.kron(np.eye(2), proj(fail))))), 6))
p_okbar_up = P(rho_coh, okbar, up); p_okbar = float(np.real(np.trace(rho_coh @ np.kron(proj(okbar), np.eye(2)))))
print("coherent P(spin up | okbar) =", round(p_okbar_up / p_okbar, 6))
p_okbar_up_m = P(rho_mix, okbar, up); p_okbar_m = float(np.real(np.trace(rho_mix @ np.kron(proj(okbar), np.eye(2)))))
print("fully dephased P(spin up | okbar) =", round(p_okbar_up_m / p_okbar_m, 6))
