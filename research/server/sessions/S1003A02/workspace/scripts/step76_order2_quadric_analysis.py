#!/usr/bin/env python3
"""Step 76: fast analysis of the order-2 AKE compatibility quadric at a torsion zero.

Input: workspace/data/step76_prolong_order2.pkl (from step76_prolong_order2_fast.py).
Parameters t1..t15 = ker(L0) modulo Hamiltonian gauge on the 2-jet H2 (+ lam*hp).
We map t -> linear torsion jet D (4x4 real, a_k = D_km x_m), convert to complex
f(z) = C z + B zbar, check C = c*Id, split B = S + A, and write the quadric Q(t)
in coordinates (c, S, A, kernel).  Output: workspace/data/step76_order2_quadric.json
"""
import json, pickle
from pathlib import Path
import numpy as np
import sympy as sp

DATA = Path(__file__).resolve().parents[1] / 'data'
d = pickle.load(open(DATA/'step76_prolong_order2.pkl', 'rb'))
obs = [o for o in d['obs'] if o != 0]
assert len(obs) == 1
Qp = obs[0]
nv = len(d['vecs']); n = nv-1
t = sp.symbols('t1:%d' % nv)
P = sp.Poly(Qp, *t)
Q = np.zeros((n, n))
for (i, j) in [(i, j) for i in range(n) for j in range(i, n)]:
    e = [0]*n; e[i] += 1; e[j] += 1
    cf = float(P.coeff_monomial(tuple(e)))
    if i == j: Q[i, i] = cf
    else: Q[i, j] = Q[j, i] = cf/2
T = np.array([[float(x) for x in d['TorC'][a]] for a in range(1, nv)]).T   # 16 x n
out = {'n_params': n, 'Tor_rank': int(np.linalg.matrix_rank(T, 1e-9))}
U, sv, Vt = np.linalg.svd(T)
r = out['Tor_rank']
K = Vt[r:].T                      # torsion-free directions (n x (n-r))
out['Q_on_torsion_kernel_norm'] = float(np.abs(K.T@Q@K).max()) if K.size else 0.0
out['Q_cross_kernel_norm'] = float(np.abs(K.T@Q).max()) if K.size else 0.0
out['Q_eigs'] = sorted(np.linalg.eigvalsh(Q).tolist())


def CB(Dflat, s):
    D = np.array(Dflat, dtype=float).reshape(4, 4)
    M = np.vstack([D[0]+1j*s*D[1], D[2]+1j*s*D[3]])    # w = M x
    C = np.array([[(M[k, 0]-1j*M[k, 1])/2, (M[k, 2]-1j*M[k, 3])/2] for k in range(2)])
    B = np.array([[(M[k, 0]+1j*M[k, 1])/2, (M[k, 2]+1j*M[k, 3])/2] for k in range(2)])
    return C, B

for s in (1, -1):
    good = True
    for a in range(n):
        C, B = CB(T[:, a], s)
        if abs(C[0, 1]) > 1e-9 or abs(C[1, 0]) > 1e-9 or abs(C[0, 0]-C[1, 1]) > 1e-9:
            good = False
    out['C_scalar_s=%d' % s] = good
    if good: S_ = s
s = S_
# linear jet coordinates: c, S11, S12, S22, A12 (complex) -> 10 real
rows = []
for a in range(n):
    C, B = CB(T[:, a], s)
    Sm = (B+B.T)/2; Am = (B-B.T)/2
    z = [C[0, 0], Sm[0, 0], Sm[0, 1], Sm[1, 1], Am[0, 1]]
    rows.append(sum([[x.real, x.imag] for x in z], []))
Jc = np.array(rows).T   # 10 x n
out['jet_rank'] = int(np.linalg.matrix_rank(Jc, 1e-9))
# Q in jet coordinates restricted: Q = Jc^T M Jc on complement of K (if Q kills K)
Jp = np.linalg.pinv(Jc)
M = Jp.T@Q@Jp; M = (M+M.T)/2
out['reconstruct_err'] = float(np.abs(Jc.T@M@Jc - Q).max())
# fit invariant form a|c|^2 + b||S||^2 + g||A||^2 (+ cross)
names = ['cr', 'ci', 'S11r', 'S11i', 'S12r', 'S12i', 'S22r', 'S22i', 'Ar', 'Ai']
out['M_jet'] = np.round(M, 10).tolist()
diag = np.diag(M)
out['coef_|c|^2'] = float(diag[0]); out['coef_|c|^2_check'] = float(diag[1])
out['coef_S11'] = float(diag[2]); out['coef_S12(per |S12|^2 i.e. ||S||^2 has 2|S12|^2)'] = float(diag[4]); out['coef_S22'] = float(diag[6])
out['coef_A12(||A||^2=2|A12|^2)'] = float(diag[8])
off = M - np.diag(diag)
out['max_offdiag'] = float(np.abs(off).max())
big = [(names[i], names[j], float(off[i, j])) for i in range(10) for j in range(i+1, 10) if abs(off[i, j]) > 1e-8]
out['offdiag_entries'] = big
(DATA/'step76_order2_quadric.json').write_text(json.dumps(out, indent=1)+'\n')
print(json.dumps({k: v for k, v in out.items() if k != 'M_jet'}, indent=1))
