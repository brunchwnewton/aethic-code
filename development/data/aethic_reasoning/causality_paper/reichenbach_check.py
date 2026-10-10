# Reichenbach's principle as a theorem of product-form (multiplicatively composed) states, checked exactly.
# A state is a product of entry-factors over the families each entry touches (the framework's multiplicative
# update); zero weight is joint invalidity. For every mixture-level correlated pair (A, B) we check:
#   (i)   demand: A and B are connected through entries;
#   (ii)  disjunction: some entry touches both, or the families sharing an entry with A separate A from B;
#   (iii) certificate: every separating family screens; so an unscreenable pair has a direct entry;
#         and screening by C is equivalent to W(a,b,c) = f(a,c) g(b,c) on the (A,B,C)-marginal;
#   (iv)  fork: every screener is dependent on A and on B and carries the whole covariance; binary forks
#         satisfy Reichenbach's inequalities; and
#   (v)   presentation invariance: merging entries changes no screening verdict and no theorem instance.
import itertools, random, collections
from fractions import Fraction as Fr

rng = random.Random(474)
def state(card, entries):
    """Joint weight over all families, as a dict value-tuple -> Fraction (a product of entry factors)."""
    fams = list(card); W = {}
    for vals in itertools.product(*[range(card[f]) for f in fams]):
        v = dict(zip(fams, vals)); w = Fr(1)
        for scope, tab in entries: w *= tab[tuple(v[f] for f in scope)]
        if w: W[vals] = w
    return fams, W
def marg(fams, W, keep):
    idx = [fams.index(f) for f in keep]; M = collections.defaultdict(Fr)
    for vals, w in W.items(): M[tuple(vals[i] for i in idx)] += w
    return M
def indep(fams, W, A, B, C):
    """A independent of B given C (C a tuple of families), at every C-pocket of positive weight."""
    M = marg(fams, W, (A, B) + C); MC = marg(fams, W, C); MA = marg(fams, W, (A,) + C); MB = marg(fams, W, (B,) + C)
    for key, wc in MC.items():
        for a, b in itertools.product(range(card[A]), range(card[B])):
            if M[(a, b) + key] * wc != MA[(a,) + key] * MB[(b,) + key]: return False
    return True
def connected(entries, A, B, removed=()):
    adj = collections.defaultdict(set)
    for scope, _ in entries:
        live = [f for f in scope if f not in removed]
        for x in live: adj[x] |= set(live)
    seen, todo = {A}, [A]
    while todo:
        x = todo.pop()
        for y in adj[x] - seen: seen.add(y); todo.append(y)
    return B in seen
def cov_identity(fams, W, A, B, C):
    """Cov(1[A=a], 1[B=b]) = Cov(E[1[A=a]|C], E[1[B=b]|C]) for all a, b (total covariance with zero within-pocket term)."""
    Z = sum(W.values()); PA = marg(fams, W, (A,)); PB = marg(fams, W, (B,)); PAB = marg(fams, W, (A, B))
    MC = marg(fams, W, C); MAC = marg(fams, W, (A,) + C); MBC = marg(fams, W, (B,) + C)
    for a, b in itertools.product(range(card[A]), range(card[B])):
        lhs = PAB[(a, b)] / Z - (PA[(a,)] / Z) * (PB[(b,)] / Z)
        e_ab = sum((MAC[(a,) + k] / wc) * (MBC[(b,) + k] / wc) * (wc / Z) for k, wc in MC.items())
        rhs = e_ab - (PA[(a,)] / Z) * (PB[(b,)] / Z)
        if lhs != rhs: return False
    return True

V = collections.Counter(); T = collections.Counter()
for trial in range(1500):
    fams = ['A', 'B', 'C', 'D', 'E'][:rng.choice([3, 4, 5])]
    card = {f: rng.choice([2, 2, 3]) for f in fams}
    entries = []
    for _ in range(rng.randint(1, 5)):
        scope = tuple(sorted(rng.sample(fams, rng.choice([1, 2, 2, 3]))))
        tab = {k: Fr(rng.choice([0, 1, 1, 2, 3, 5])) for k in itertools.product(*[range(card[f]) for f in scope])}
        entries.append((scope, tab))
    fams_, W = state(card, entries)
    if not W: continue
    presentations = [entries]
    if len(entries) >= 2:   # a coarser presentation of the same state: merge two entries into one
        i, j = rng.sample(range(len(entries)), 2); (s1, t1), (s2, t2) = entries[i], entries[j]
        s = tuple(sorted(set(s1) | set(s2)))
        t = {k: t1[tuple(k[s.index(f)] for f in s1)] * t2[tuple(k[s.index(f)] for f in s2)] for k in itertools.product(*[range(card[f]) for f in s])}
        presentations.append([e for n, e in enumerate(entries) if n not in (i, j)] + [(s, t)])
        V['(v) merged presentation changes the state'] += state(card, presentations[1])[1] != W
    for A, B in itertools.combinations(fams_, 2):
        if indep(fams_, W, A, B, ()): continue                      # not correlated at the mixture level
        T['correlated pairs'] += 1
        others = [f for f in fams_ if f not in (A, B)]
        cands = [C for r in range(1, len(others) + 1) for C in itertools.combinations(others, r)]
        screens = {C: indep(fams_, W, A, B, C) for C in cands}
        unscreenable = not any(screens.values()); T['unscreenable'] += unscreenable
        for P in presentations:
            V['(i) correlated but not connected through entries'] += not connected(P, A, B)
            direct = any(A in s and B in s for s, _ in P)
            NA = tuple(sorted({f for s, _ in P if A in s for f in s} - {A, B}))
            if not direct:
                V['(ii) no direct entry, yet N(A) fails to separate'] += connected(P, A, B, removed=NA)
                V['(iii) no direct entry, yet N(A) fails to screen'] += not indep(fams_, W, A, B, NA)
            for C in cands:
                if not connected(P, A, B, removed=C):
                    T['separating families'] += 1; V['(iii) a separating family fails to screen'] += not screens[C]
            V['(iii) unscreenable without a direct entry'] += unscreenable and not direct
            T['direct entry but screenable (absorbed)'] += direct and not unscreenable and P is presentations[0]
        for C, s in screens.items():
            if not s: continue
            T['screeners'] += 1
            # dependence of the (compound) screener on each correlate: A independent of C would force A independent of B
            dep_A = not all(marg(fams_, W, (A,) + C)[(a,) + k] * sum(W.values()) == marg(fams_, W, (A,))[(a,)] * wc
                            for k, wc in marg(fams_, W, C).items() for a in range(card[A]))
            dep_B = not all(marg(fams_, W, (B,) + C)[(b,) + k] * sum(W.values()) == marg(fams_, W, (B,))[(b,)] * wc
                            for k, wc in marg(fams_, W, C).items() for b in range(card[B]))
            V['(iv) a screener independent of A or of B'] += not (dep_A and dep_B)
            V['(iv) total-covariance identity fails'] += not cov_identity(fams_, W, A, B, C)
            if len(C) == 1 and card[A] == card[B] == card[C[0]] == 2:
                Z = sum(W.values()); PAB = marg(fams_, W, (A, B)); PA = marg(fams_, W, (A,)); PB = marg(fams_, W, (B,))
                MC = marg(fams_, W, C); MAC = marg(fams_, W, (A,) + C); MBC = marg(fams_, W, (B,) + C)
                if len(MC) == 2:
                    T['binary forks'] += 1
                    cov = PAB[(1, 1)] / Z - PA[(1,)] / Z * PB[(1,)] / Z
                    dA = MAC[(1, 1)] / MC[(1,)] - MAC[(1, 0)] / MC[(0,)]; dB = MBC[(1, 1)] / MC[(1,)] - MBC[(1, 0)] / MC[(0,)]
                    V['(iv) binary fork: Cov != P(C)P(~C) dA dB'] += cov != (MC[(1,)] / Z) * (MC[(0,)] / Z) * dA * dB
            # (iii) converse of the factorization theorem: screening gives W(a,b,c) = f(a,c) g(b,c) on the marginal
            M3 = marg(fams_, W, (A, B) + C); MAC_ = marg(fams_, W, (A,) + C); MBC_ = marg(fams_, W, (B,) + C); MC_ = marg(fams_, W, C)
            V['(iii) screening without pairwise factorization'] += any(M3[(a, b) + k] * wc != MAC_[(a,) + k] * MBC_[(b,) + k]
                                                                       for k, wc in MC_.items() for a in range(card[A]) for b in range(card[B]))
print("tallies:", dict(T))
for k in sorted(V): print(f"  {k:<58} violations: {V[k]}")
print("ALL CLAIMS HOLD" if not any(V.values()) else "VIOLATIONS FOUND")
