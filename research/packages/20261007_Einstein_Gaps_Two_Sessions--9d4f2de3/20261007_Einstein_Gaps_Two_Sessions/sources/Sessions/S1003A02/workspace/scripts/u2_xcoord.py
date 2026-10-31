"""U(2)-invariant metrics in the coordinate x = b^2:
    g = dx^2/(4 G(x)) + F(x) s3^2 + x (s1^2+s2^2),
Kahler (complex orientation) iff F = G.  Bolt (blown-up point, O(-1)) at x0:
F(x0)=G(x0)=0, F'(x0) G'(x0) = 1.  Complex hyperbolic (Ric=-6g): F=G=x+x^2.
Burns (scalar-flat Kahler, AF): F=G=x-x0.  FS: F=G=x-x^2.

Produces lambdified numerical functions for
    ric0sq, s, wpsq_c (|W+|^2 in complex orientation), wmsq_c
in terms of (x, F, F1, F2, G, G1) [F1=F', F2=F'', G1=G'], and the volume
density dV = pi^2 * x * sqrt(F/G) dx  (after integrating over S^3, vol 2pi^2).
"""
import sympy as sp
import pickle, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u2_curvature as U

x = sp.symbols('x', positive=True)
F, F1, F2, F3, G, G1, G2 = sp.symbols('F F1 F2 F3 G G1 G2')
t = U.t
a, b = U.a, U.b
# derivatives along t: d/dt = 2 sqrt(G) d/dx.  Represent functions of x via symbols,
# with chain rule d/dx F = F1, d/dx F1 = F2, d/dx G = G1.
def ddx(expr):
    return (sp.diff(expr, x) + sp.diff(expr, F)*F1 + sp.diff(expr, F1)*F2 + sp.diff(expr, F2)*F3
            + sp.diff(expr, G)*G1 + sp.diff(expr, G1)*G2)
def ddt(expr):
    return 2*sp.sqrt(G)*ddx(expr)
A0 = sp.sqrt(F); A1 = ddt(A0); A2 = ddt(A1)
B0 = sp.sqrt(x); B1 = ddt(B0); B2 = ddt(B1)
def conv(e):
    e = e.subs({sp.Derivative(a, (t, 2)): A2, sp.Derivative(b, (t, 2)): B2})
    e = e.subs({sp.Derivative(a, t): A1, sp.Derivative(b, t): B1})
    e = e.subs({a: A0, b: B0})
    return sp.simplify(e)
exprs = {'s': conv(U.s), 'ric0sq': conv(U.ric0sq), 'wpsq_c': conv(U.wmsq), 'wmsq_c': conv(U.wpsq)}
if __name__ == '__main__':
    for k, v in exprs.items():
        print(k, '=', v)
        print('  free:', v.free_symbols)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, '..', 'data', 'u2_x_exprs.pkl'), 'wb') as f:
        pickle.dump({k: sp.srepr(v) for k, v in exprs.items()}, f)
    # checks
    for name, FF, GG in [('CH', x + x**2, x + x**2), ('FS', x - x**2, x - x**2),
                         ('Burns', x - sp.Symbol('x0'), x - sp.Symbol('x0')),
                         ('Kahler generic', sp.Function('K')(x), sp.Function('K')(x))]:
        sub = {F: FF, F1: sp.diff(FF, x), F2: sp.diff(FF, x, 2), G: GG, G1: sp.diff(GG, x)}
        print(name, {k: sp.simplify(v.subs(sub)) for k, v in exprs.items()})
