"""Space-form bulk: universal first-order change of the total scalar curvature of a conformally
Kaehler blow-up cell.

Kaehler cell with flat collar: K(y) = y - y0 (1 - chi(y)),  g_K = dy^2/(4K) + y(s1^2+s2^2) + K s3^2,
dV_K = pi^2 y dy (independent of K),  s_K = 4(2-(yK)'')/y,  Delta_K w = (4/y)(y K w')'.
Space-form conformal factor (flat ball -> S^4/H^4 with Ric = lam g): w = 2/(1+c y), c = lam/3.
G = w^2 g_K.  s_G dV_G = (-6 w Delta_K w + s_K w^2) dV_K.
Claim: int_{y0}^{Y} s_G dV_G - int_0^{Y} s_flat-ball... = -4 pi t_G + O(y0^2), with t_G = pi y0 w(y0)^2,
for every cutoff chi (chi=0 near y0, chi=1 near Y): the chi-dependence cancels because
2 w w'' - 4 w'^2 = 0 for the space-form factor.
"""
import sympy as sp

y, y0, c, Y = sp.symbols('y y0 c Y', positive=True)
w = 2 / (1 + c * y)
print('2ww\'\'-4w\'^2 =', sp.simplify(2 * w * sp.diff(w, y, 2) - 4 * sp.diff(w, y)**2))

def total_scalar(K, lo, hi):
    dK = (4 / y) * sp.diff(y * K * sp.diff(w, y), y)
    sK = 4 * (2 - sp.diff(y * K, y, 2)) / y
    dens = (-6 * w * dK + sK * w**2) * sp.pi**2 * y
    return sp.integrate(sp.expand(sp.simplify(dens)), (y, lo, hi))

# explicit C^2 cutoff on [a, Y]: chi = 0 for y<a, smoothstep in between; take a = Y/2
a = Y / 2
z = (y - a) / (Y - a)
chi_mid = z**3 * (10 - 15 * z + 6 * z**2)
flat_mid = total_scalar(y, a, Y)
flat_in = total_scalar(y, 0, a)
cell_in = total_scalar(y - y0, y0, a)
cell_mid = total_scalar(y - y0 * (1 - chi_mid), a, Y)
delta = sp.simplify(cell_in + cell_mid - flat_in - flat_mid)
tG = sp.pi * y0 * w.subs(y, y0)**2
ser = sp.series(delta, y0, 0, 2).removeO()
print('Delta int s_G dV_G, series in y0:', sp.simplify(ser))
print('-4 pi t_G series                :', sp.simplify(sp.series(-4 * sp.pi * tG, y0, 0, 2).removeO()))
print('difference at first order       :', sp.simplify(sp.series(delta + 4 * sp.pi * tG, y0, 0, 2).removeO()))
