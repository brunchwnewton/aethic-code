# Invalid Aethae kept distinct (no explosion; the empty filling is a tag) + union as last common ancestor (common content).
# Question: can the validity congruence (invalid ~ additive identity) then be imposed without collapsing valid Aethae?
import itertools
fs = frozenset
ATTR = {'X': ['a', 'b'], 'Y': ['y1', 'y2']}
OF = {p: A for A, ps in ATTR.items() for p in ps}
D = [fs(pr) for ps in ATTR.values() for pr in itertools.combinations(ps, 2)]          # pegs of one attribute disjoint
def cl(S):                                                                              # narrowing, propagation, elimination; NO explosion
    C, E = set(S), set()
    while True:
        new, by = set(), {}
        for A, F in C: by.setdefault(A, []).append(F)
        for A, Fs in by.items():
            for F in Fs:
                for G in Fs: new.add((A, F & G))
        held = {next(iter(F)) for A, F in C if len(F) == 1}
        newE = {p for Dset in D for p in Dset if all(q in held for q in Dset if q != p)}
        for p in E | newE:
            for F in by.get(OF[p], []): new.add((OF[p], F - {p}))
        for A, ps in ATTR.items():
            for p in ps:
                if all(q in E | newE for q in ps if q != p): new.add((A, fs({p})))
        if new <= C and newE <= E: return fs(C), fs(E)
        C |= new; E |= newE
invalid = lambda c: any(len(F) == 0 for A, F in c[0])
meet = lambda c, d: cl(c[0] | d[0])
join = lambda c, d: (c[0] & d[0], c[1] & d[1])                                          # last common ancestor: common content
B     = cl({('X', fs({'a'}))})                                                          # valid: X = a
A_inv = cl({('Y', fs({'y1'})), ('Y', fs({'y2'}))})                                      # invalid: Y exactly y1 and exactly y2 (tagged, not exploded)
Dd    = cl({('X', fs({'b'}))})                                                          # valid: X = b
J = join(A_inv, B)
print("A_inv invalid:", invalid(A_inv), "| B valid:", not invalid(B))
print("A_inv + B (last common ancestor): valid =", not invalid(J), "| still holds X = a:", ('X', fs({'a'})) in J[0])
print("(A_inv + B) . D  valid =", not invalid(meet(J, Dd)), "|  B . D  valid =", not invalid(meet(B, Dd)))
print("=> the validity congruence must identify A_inv + B with B (drop the invalid term), hence (A_inv + B).D with B.D:")
print("   a VALID Aethus identified with an INVALID one, so the congruence collapses the valid Aethae as well.")
print("\nWith explosion instead (invalid content = every item): A_inv + B = B exactly, and nothing collapses; but then invalid terms are not kept.")
print("With terms kept in a formal sum {A_inv, B}: deleting the invalid term gives exactly {B}; its common-content core is taken after.")
