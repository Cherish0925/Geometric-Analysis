#!/usr/bin/env python3
"""
Numerical test of the functional-analytic claims in BUN:third (C3):
  H_A A = (c0^2/2) f r^2,   H_A = -P_t - P_u + 2
  H_C C =  c0^2    f r^2,   H_C = -P_t - P_u + 2 - 4 r
on (t,u) in R^2 with measure cosh t cosh u dt du  (L^2 solutions, even in t and u).
Finite-volume discretisation on [0,Tm]x[0,Um], Neumann at 0 (evenness), Dirichlet 0 at the far sides.

Checks:  0<=A<=min((c0^2/2) T r, f B),  0<=C<=c0^2 T r,  int A dmu0 = 1/(2 pi^2),
         M(t)=int C r cosh u du = (3 pi c0^2/8) T(t),  Bianchi: Z = C_u + 2 tanh u C - A_u = 0.
"""
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla

c0 = 2 / np.pi**2
import sys
Tm = Um = 14.0
h = float(sys.argv[1]) if len(sys.argv) > 1 else 0.02
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/yau26/work/audit_bundle/AC_solution.npz'
N = int(round(Tm / h))
tc = (np.arange(N) + 0.5) * h          # cell centres
uc = tc.copy()
tf = np.arange(N + 1) * h              # faces
wt_c, wt_f = np.cosh(tc), np.cosh(tf)


def oneD(w_c, w_f):
    """matrix of  -(1/w) d/dx ( w d/dx )  with Neumann at x=0 face and Dirichlet(0) at the far face"""
    main = np.zeros(N); lo = np.zeros(N - 1); up = np.zeros(N - 1)
    for i in range(N):
        wl = w_f[i] if i > 0 else 0.0      # Neumann: no flux through x=0
        wr = w_f[i + 1]
        main[i] = (wl + wr) / (w_c[i] * h * h)
        if i == N - 1:
            # Dirichlet ghost value = -value (zero at face): flux = w*(0 - v_i)/(h/2)
            main[i] = (wl + 2 * wr) / (w_c[i] * h * h)
        if i > 0: lo[i - 1] = -wl / (w_c[i] * h * h)
        if i < N - 1: up[i] = -wr / (w_c[i] * h * h)
    return sps.diags([lo, main, up], [-1, 0, 1], format='csr')


Pt = oneD(wt_c, wt_f)       # -P_t
Pu = oneD(wt_c, wt_f)       # -P_u (same grid)
I = sps.identity(N, format='csr')
f = 1 / np.cosh(tc)**2; r = 1 / np.cosh(uc)**2
F, Rr = np.meshgrid(f, r, indexing='ij')      # index [it, iu]
HA = sps.kron(Pt, I) + sps.kron(I, Pu) + 2 * sps.identity(N * N)
HC = HA - 4 * sps.diags(Rr.ravel())
rhs = (F * Rr**2).ravel()
print("solving H_A ..."); A = spla.spsolve(HA.tocsc(), c0**2 / 2 * rhs).reshape(N, N)
print("solving H_C ..."); C = spla.spsolve(HC.tocsc(), c0**2 * rhs).reshape(N, N)

gd = lambda x: np.arctan(np.sinh(x))
T = 0.5 * (np.pi**2 / 4 - gd(tc)**2)
B = c0**2 / 8 * (r + np.pi**2 / 4 - gd(uc)**2)
TT, _ = np.meshgrid(T, r, indexing='ij'); _, BB = np.meshgrid(f, B, indexing='ij')

print("min A = %.3e, min C = %.3e" % (A.min(), C.min()))
print("max(A - (c0^2/2) T r) = %.3e   (should be <= 0)" % (A - c0**2 / 2 * TT * Rr).max())
print("max(A - f B)          = %.3e   (should be <= 0)" % (A - F * BB).max())
print("max(C - c0^2 T r)     = %.3e   (should be <= 0)" % (C - c0**2 * TT * Rr).max())
print("A(0,0) = %.6f,  C(0,0) = %.6f,  B(0) = %.6f" % (A[0, 0], C[0, 0], B[0]))

W = np.outer(np.cosh(tc), np.cosh(uc))
print("int A dmu0 = %.6f   claimed 1/(2 pi^2) = %.6f" % (4 * np.sum(A * W) * h * h, 1 / (2 * np.pi**2)))
M = 2 * np.sum(C * (r * np.cosh(uc))[None, :], axis=1) * h
ratio = M / (3 * np.pi * c0**2 / 8 * T)
print("M(t)/((3 pi c0^2/8) T(t)) at t=0.01,1,3,6: ", [float("%.5f" % ratio[int(x / h)]) for x in (0.0, 1.0, 3.0, 6.0)])

# Bianchi: Z = C_u + 2 tanh u C - A_u  (centred differences in u)
Cu = np.gradient(C, h, axis=1); Au = np.gradient(A, h, axis=1)
Z = Cu + 2 * np.tanh(uc)[None, :] * C - Au
inner = (slice(1, int(8 / h)), slice(1, int(8 / h)))
print("sup|Z| on [0,8]^2 = %.3e   vs  sup|A_u| = %.3e, sup|C_u + 2 tanh u C| = %.3e" % (
    np.abs(Z[inner]).max(), np.abs(Au[inner]).max(), np.abs((Cu + 2 * np.tanh(uc)[None, :] * C)[inner]).max()))
# decay rates
for (tt, uu) in [(0, 4), (0, 6), (4, 0), (6, 0), (4, 4)]:
    it, iu = int(tt / h), int(uu / h)
    print("  (t,u)=(%d,%d):  A e^{t+2u} = %.4f   C e^{t+2u} = %.4f" % (tt, uu, A[it, iu] * np.exp(tc[it] + 2 * uc[iu]), C[it, iu] * np.exp(tc[it] + 2 * uc[iu])))
np.savez_compressed(OUT, A=A, C=C, tc=tc, uc=uc)
