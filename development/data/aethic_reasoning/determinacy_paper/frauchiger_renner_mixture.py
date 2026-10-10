#!/usr/bin/env python3
"""Frauchiger-Renner protocol: four-outcome joint distribution of the two superobservers' measurements
under (a) the coherent laboratory-state assignment and (b) the framework's disagreeing mixture over the
friends' record-separated outcome pockets; and the certainty inference (ok_1 implies spin up) that holds
under (a) and fails under (b). Companion to the long Aethic paper's Frauchiger-Renner subsubsection."""
import numpy as np
s3 = np.sqrt(1/3); idx = lambda c, s: 2*c + s          # coin {h=0,t=1}, spin {down=0,up=1}
Psi = np.zeros(4); Psi[idx(0,0)] = Psi[idx(1,0)] = Psi[idx(1,1)] = s3   # (|h,down> + |t,down> + |t,up>)/sqrt3
ok = np.array([1,-1])/np.sqrt(2); fail = np.array([1,1])/np.sqrt(2)
P = {(0,0): 1/3, (1,0): 1/3, (1,1): 1/3}                                  # record-separated pockets, weights
e = np.eye(2); rho = sum(p*np.outer(np.kron(e[c],e[s]), np.kron(e[c],e[s])) for (c,s), p in P.items())
print("outcome      coherent   mixture")
for a, A in (('ok1',ok),('fail1',fail)):
    for b, B in (('ok2',ok),('fail2',fail)):
        v = np.kron(A,B); print(f"{a+','+b:12s} {abs(v@Psi)**2:8.4f} {v@rho@v:9.4f}")
print("coherent: P(ok1,down)=%.4f P(ok1,up)=%.4f  -> ok1 implies up" % ((np.kron(ok,e[0])@Psi)**2, (np.kron(ok,e[1])@Psi)**2))
print("mixture:  P(ok1,down)=%.4f P(ok1,up)=%.4f  -> ok1 implies nothing about the spin" % (sum(p/2 for (c,s),p in P.items() if s==0), sum(p/2 for (c,s),p in P.items() if s==1)))
