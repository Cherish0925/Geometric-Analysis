"""Profile the pieces of step59_exact_wminus_ric_correctors.py (timing only, no output files)."""
import sys, os, time
sys.argv = ['x', 'Wm']
t0 = time.time()
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step59_exact_log_coefficient import (X, r2, A_field, riemann_from_ops, h2_field, density_sig2)
print('import', time.time() - t0, flush=True)
Z3 = sp.zeros(3, 3)
R = riemann_from_ops(Z3, sp.Matrix([[1, 2, 0], [2, -3, 1], [0, 1, 2]]), 0, Z3)
H = h2_field(R)
pt = (sp.Rational(1), sp.Rational(2, 3), sp.Rational(-1, 2), sp.Rational(3, 5))
sub = dict(zip(X, pt))
t = time.time()
def jets_fast(M):
    J0 = [[M[i, j].subs(sub) for j in range(4)] for i in range(4)]
    D1 = [[[sp.diff(M[i, j], X[k]) for k in range(4)] for j in range(4)] for i in range(4)]
    J1 = [[[D1[i][j][k].subs(sub) for k in range(4)] for j in range(4)] for i in range(4)]
    J2 = [[[[sp.diff(D1[i][j][k], X[l]).subs(sub) for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]
    return J0, J1, J2
Aj = jets_fast(A_field); print('A jets', time.time() - t, flush=True)
t = time.time(); Hj = jets_fast(H); print('H jets', time.time() - t, flush=True)
sig = sp.Symbol('sig')
t = time.time()
Pj = [[[Hj[0][i][j] for j in range(4)] for i in range(4)],
      [[[Hj[1][i][j][k] for k in range(4)] for j in range(4)] for i in range(4)],
      [[[[Hj[2][i][j][k][l] for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]]
dens, spr = density_sig2(Aj, Pj)
print('density numeric (K=0)', time.time() - t, flush=True)
c = sp.Symbol('c')
t = time.time()
Pj2 = [[[Hj[0][i][j] + sig * c * (1 if i == j else 0) for j in range(4)] for i in range(4)], Pj[1], Pj[2]]
dens, spr = density_sig2(Aj, Pj2)
print('density 1 symbol', time.time() - t, flush=True)
