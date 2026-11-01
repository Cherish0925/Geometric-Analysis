"""Antisymmetric part of X1 (should vanish for a G-self-adjoint linearised W+ operator) in several sectors."""
import sys, os
sys.argv = ['x', 'Wm']
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import step60_corrector_columns as C
from step59_exact_log_coefficient import riemann_from_ops, h2_field

Z3 = sp.zeros(3, 3)
cases = {
    'Wplus': riemann_from_ops(sp.Matrix([[2, 0, 0], [0, -1, 1], [0, 1, -1]]), Z3, 0, Z3),
    's': riemann_from_ops(Z3, Z3, -24, Z3),
    'Wminus': riemann_from_ops(Z3, sp.Matrix([[1, 2, 0], [2, -3, 1], [0, 1, 2]]), 0, Z3),
}
B = sp.zeros(3, 3); B[0, 0] = 1; B[0, 1] = 2; B[0, 2] = -1
cases['Ric_z'] = riemann_from_ops(Z3, Z3, 0, B)
pt = (sp.Rational(1), sp.Rational(2, 3), sp.Rational(-1, 2), sp.Rational(3, 5))
Aj = C.jets(C.A, pt)
for lab, R in cases.items():
    H = h2_field(R); Hj = C.jets(H, pt)
    try:
        Y, d = C.Yvec(Aj, Hj, None); X1 = sp.Matrix(6, 6, Y[:36])
        print(lab, 'sigma0 ok;  |anti X1| =', sp.N((X1 - X1.T).norm() / 2), ' |sym X1| =', sp.N((X1 + X1.T).norm() / 2))
    except AssertionError:
        from step59_exact_log_coefficient import density_sig2
        P0 = [[Hj[0][i][j] for j in range(4)] for i in range(4)]
        dens, spr = density_sig2(Aj, [P0, Hj[1], Hj[2]])
        Xm = density_sig2.last_X
        X0 = sp.Matrix(6, 6, lambda I, J: Xm[I, J].coef(0, 0)); X1 = sp.Matrix(6, 6, lambda I, J: Xm[I, J].coef(1, 0))
        print(lab, '|anti X0| =', sp.N((X0 - X0.T).norm() / 2), ' |anti X1| =', sp.N((X1 - X1.T).norm() / 2),
              ' tr(X0 antiX1) =', sp.N((X0 * (X1 - X1.T)).trace()))
