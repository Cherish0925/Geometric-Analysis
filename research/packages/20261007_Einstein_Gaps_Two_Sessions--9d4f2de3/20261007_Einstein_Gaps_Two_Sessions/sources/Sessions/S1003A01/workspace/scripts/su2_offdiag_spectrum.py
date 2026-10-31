"""Generalized spectrum of the non-diagonal SU(2) Hessian in a fixed geometric norm.

Reads the Hessian blocks produced by su2_offdiag_hessian.py and solves H v = mu M v with
    M_ab = int_0^1 env(u)^2 T_a(2u-1) T_b(2u-1) du,   env = u^2 (1-u)^3,
i.e. the L^2(du) norm of the relative off-diagonal amplitude k_ij/N_ij in the log-radial
variable u = log(x/x0)/log(X/x0).  A basis-independent positive limit of mu_min under
refinement indicates a positive second variation in that norm (numerical evidence only).
Usage: python su2_offdiag_spectrum.py HESS.json [HESS2.json ...]
"""
import json, sys
import numpy as np
from scipy.linalg import eigh


def gram(n, m=4000):
    e, w = np.polynomial.legendre.leggauss(m); u = .5*(e+1); w = .5*w
    T = np.polynomial.chebyshev.chebvander(2*u-1, n-1)
    env = u**2*(1-u)**3
    return (T*(env**2*w)[:, None]).T @ T


for path in sys.argv[1:]:
    d = json.load(open(path)); n = d['n']
    # Hessian blocks are not stored in full; recompute from the JSON if present.
    if 'H_blocks' not in d:
        print(path, 'no full blocks stored'); continue
    M = gram(n)
    for k, Hb in d['H_blocks'].items():
        Hb = np.array(Hb)
        if Hb.shape[0] == n+1:
            # bolt-rotation coefficient is the last entry: Schur complement = minimal second
            # variation for unit bolt rotation psi=1 (others optimized); eig of full block.
            A = Hb[:n, :n]; b = Hb[:n, n]; S = Hb[n, n]-b@np.linalg.solve(A, b)
            print(path, k, 'bolt-rot raw=%.4e schur=%.4e  full_eig_min=%.4e' % (Hb[n, n], S, np.linalg.eigvalsh(Hb)[0]))
            Hb = A
        mu, V = eigh(Hb, M)
        print(path, k, 'mu_min=%.4e mu_2=%.4e' % (mu[0], mu[1]))
