"""Consistency: is [sig^2] density == 4 tr(X1^2) + s1^2/12 in the pure W^- sector?  Is X1 symmetric?"""
import sys, os
mode = sys.argv[1] if len(sys.argv) > 1 else 'Wm'
sys.argv = ['x', mode]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import step60_corrector_columns as C
from step59_exact_log_coefficient import density_sig2

K0 = sp.Rational(3, 2) * C.sym(C.H * C.A) - sp.Rational(1, 4) * (C.H * C.A).trace() * sp.eye(4)
pt = (sp.Rational(1), sp.Rational(2, 3), sp.Rational(-1, 2), sp.Rational(3, 5))
Aj = C.jets(C.A, pt); Hj = C.jets(C.H, pt)
for lab, Tj in [('K=0', None), ('k0W', C.jets(K0, pt))]:
    Y, d = C.Yvec(Aj, Hj, Tj)
    X1 = sp.Matrix(6, 6, Y[:36]); s1 = Y[36]
    print(lab, 'dens', sp.N(d), ' 4trX1^2+s1^2/12 =', sp.N(4 * (X1 * X1).trace() + s1 ** 2 / 12),
          ' |X1-X1^T| =', sp.N((X1 - X1.T).norm()), ' 4|X1|_F^2 =', sp.N(4 * sum(v ** 2 for v in Y[:36])))
    print('   X1 =', [[sp.N(X1[i, j], 4) for j in range(6)] for i in range(6)])
