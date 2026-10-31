"""Exact minimum of P = int |Ric0|^2 over U(2)-invariant KAHLER cells on the
blown-up ball glued C^1 (H^2) to complex hyperbolic space (Ric=-6g, F=x+x^2)
at x = X (geodesic radius R with X = sinh^2 R).
Kahler: F=G=K=x+H, P = 4 pi^2 int_{x0}^X L^2/x^3 dx, L = x^2 H'' - 2H.
Euler-Lagrange: L = c1 x^3 + c2, H = c1 x^3/4 - c2/2 + al x^2 + be/x.
BC: H(x0)=-x0, H'(x0)=0 (bolt), H(X)=X^2, H'(X)=2X (CH).
"""
import sympy as sp
x, x0, X = sp.symbols('x x0 X', positive=True)
c1, c2, al, be = sp.symbols('c1 c2 al be')
H = c1*x**3/4 - c2/2 + al*x**2 + be/x
eqs = [H.subs(x, x0) + x0, sp.diff(H, x).subs(x, x0), H.subs(x, X) - X**2, sp.diff(H, x).subs(x, X) - 2*X]
sol = sp.solve(eqs, [c1, c2, al, be], dict=True)[0]
L = sp.simplify((x**2*sp.diff(H, x, 2) - 2*H).subs(sol))
P = sp.simplify(4*sp.pi**2*sp.integrate(sp.expand(L**2/x**3), (x, x0, X)))
print('L =', sp.factor(L))
print('P/(8pi^2) =', sp.simplify(P/(8*sp.pi**2)))
import numpy as np
Pf = sp.lambdify((x0, X), P/(8*sp.pi**2), 'numpy')
for XX in [0.01, 0.1, 1.0, 10.0, 100.0]:
    xs = np.geomspace(1e-6*XX, 0.999*XX, 4000)
    v = Pf(xs, XX)
    i = np.nanargmin(v)
    print(f'X={XX:8.3g}  min_x0 P/8pi^2 = {v[i]:.6f} at x0/X={xs[i]/XX:.4g};  small x0: {Pf(1e-6*XX, XX):.6f}')
# small-x0 expansion
ser = sp.series(sp.simplify(P/(8*sp.pi**2)).subs(x0, sp.Symbol('e')*X), sp.Symbol('e'), 0, 3)
print('series in e=x0/X:', sp.simplify(ser))
