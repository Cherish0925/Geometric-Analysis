"""Direct test of A01's k0^W = (3/2)sym(h_W k_B) - (1/4)tr(h_W k_B) delta in our chiral residual Y."""
import sys, os
sys.argv = ['x', sys.argv[1] if len(sys.argv) > 1 else 'Wm']
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import step60_corrector_columns as C

K0 = sp.Rational(3, 2) * C.sym(C.H * C.A) - sp.Rational(1, 4) * (C.H * C.A).trace() * sp.eye(4)
C.terms['k0W'] = K0; C.names.append('k0W')
pt = (sp.Rational(1), sp.Rational(2, 3), sp.Rational(-1, 2), sp.Rational(3, 5))
Aj = C.jets(C.A, pt); Hj = C.jets(C.H, pt)
Y0, d0 = C.Yvec(Aj, Hj, None)
Yk, dk = C.Yvec(Aj, Hj, C.jets(K0, pt))
print('|Y0|^2 =', sum(v ** 2 for v in Y0), ' density sig2 (K=0):', sp.nsimplify(d0))
print('|Y(k0W)|^2 =', sum(v ** 2 for v in Yk), ' density sig2:', sp.nsimplify(dk))
print('Y0 nonzero entries', [(i, v) for i, v in enumerate(Y0) if v != 0][:12])
print('Yk nonzero entries', [(i, v) for i, v in enumerate(Yk) if v != 0][:12])
# also the x-direction check: h_W x = 0 (Gauss lemma) and tr h_W = 0 at pt
xv = sp.Matrix(pt); Hp = C.H.subs(dict(zip(C.X, pt)))
print('h x =', list(Hp * xv), ' tr h =', Hp.trace())
