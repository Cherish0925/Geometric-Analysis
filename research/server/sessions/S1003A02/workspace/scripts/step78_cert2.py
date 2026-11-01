#!/usr/bin/env python3
"""Step 78: corrected certificate SDP for the order-6 quadratic system (degenerate multipliers allowed).

No real solution of Psi(y) = c + J y + Q(y) = 0 is certified by any l with
    f_l(y) = l.c + (l.J) y + y^T (l.H/2) y >= eps > 0   for all y,
equivalently  M(l) - eps e0 e0^T >= 0,  M(l) = [[l.c, (l.J)/2],[(l.J)^T/2, l.H/2]].
(The Step-78 first SDP maximised lambda_min(M), which is 0 whenever l.H has a kernel; that was the wrong test.)
Normalisation: trace(l.H/2) = 1 (l.Q nonzero PSD needed anyway).
Then the certificate is post-processed: Q_l eigenvalues, kernel K, |P_K (l.J)| (must be 0), exact minimum
f_min = l.c - g^T Q_l^+ g / 4.
Usage: python step78_cert2.py <npz> ; writes <npz>_cert2.json
"""
import sys, json
import numpy as np
import cvxpy as cp


def cert(c, J, H, solver='CLARABEL'):
    m, n = J.shape
    l = cp.Variable(m); eps = cp.Variable()
    Q = sum(l[i] * (H[i] / 2) for i in range(m))
    top = cp.reshape(c @ l - eps, (1, 1), order='C')
    lin = cp.reshape(J.T @ l / 2, (n, 1), order='C')
    M = cp.bmat([[top, lin.T], [lin, Q]])
    prob = cp.Problem(cp.Maximize(eps), [(M + M.T) / 2 >> 0, cp.trace(Q) == 1, eps <= 10])
    prob.solve(solver=solver)
    return prob.status, (None if eps.value is None else float(eps.value)), l.value


def post(c, J, H, l):
    Ql = np.tensordot(l, H, 1) / 2
    Ql = (Ql + Ql.T) / 2
    ev, V = np.linalg.eigh(Ql)
    tol = 1e-8 * abs(ev).max()
    K = V[:, abs(ev) <= tol]
    g = J.T @ l
    gK = K.T @ g
    pos = V[:, ev > tol]
    gpos = pos.T @ g
    fmin = l @ c - 0.25 * np.sum(gpos ** 2 / ev[ev > tol])
    return {'eig_min': float(ev[0]), 'n_neg': int((ev < -tol).sum()), 'n_zero': int(K.shape[1]), 'rank': int((ev > tol).sum()),
            'eig_pos_min': float(ev[ev > tol].min()), '|g_on_kernel|/|g|': float(np.linalg.norm(gK) / max(np.linalg.norm(g), 1e-300)),
            'f_min_on_range': float(fmin), 'l': l.tolist()}


if __name__ == '__main__':
    f = sys.argv[1]
    d = np.load(f); c, J, H = d['c'], d['J'], d['H']
    st, eps, l = cert(c, J, H)
    out = {'status': st, 'eps': eps}
    if l is not None:
        out.update(post(c, J, H, l))
    print(json.dumps({k: v for k, v in out.items() if k != 'l'}, indent=1))
    json.dump(out, open(f.replace('.npz', '_cert2.json'), 'w'), indent=1)
