"""Sign structure of the slice transgression T (normalized Q = T/(8 pi^2)).
Biaxial form in geometric slice data  z = c/a, alpha = a', gamma = c' (t-derivatives):
  Q = gamma^2 - 4 gamma + 4 + z^2 alpha^2 - 2 gamma z alpha + gamma alpha^2
      + 3 gamma z^2 - 2 z^3 alpha + 2 z^4 - 4 z^2 .
Checks this against the general G formula, minimizes over gamma exactly, and
maps the sign of Q* = min_gamma Q on a (z, alpha) grid (bounded box).
"""
import numpy as np
import sympy as sp
import transgression_values as tv

z, al, ga = sp.symbols('z alpha gamma', real=True)
Q = ga**2 - 4*ga + 4 + z**2*al**2 - 2*ga*z*al + ga*al**2 + 3*ga*z**2 - 2*z**3*al + 2*z**4 - 4*z**2
G = tv.load()[1]
x, y, zz, a1, b1, c1 = [tv.loc[k] for k in ('x', 'y', 'z', 'a1', 'b1', 'c1')]
Qg = sp.expand((G.subs({x: 1, y: 1, zz: z, a1: al, b1: al, c1: ga}) + 32) / 4)
print('biaxial Q - G-form:', sp.simplify(Qg - Q))
gstar = sp.solve(sp.diff(Q, ga), ga)[0]
Qmin = sp.factor(sp.expand(Q.subs(ga, gstar)))
print('gamma* =', sp.factor(gstar))
print('Q* = min_gamma Q =', Qmin)
fq = sp.lambdify((z, al), Qmin, 'numpy')
Z, A = np.meshgrid(np.linspace(0.01, 3, 300), np.linspace(-3, 3, 601))
V = fq(Z, A)
print('fraction of grid with Q*<0:', float((V < 0).mean()))
for zv in (0.25, 0.5, 1.0, 1.5, 2.0):
    roots = sp.Poly(sp.expand(Qmin.subs(z, sp.Rational(zv).limit_denominator(100))), al).nroots()
    print('z=', zv, ' real roots in alpha of Q*:', [complex(r_).real for r_ in roots if abs(complex(r_).imag) < 1e-9])
# triaxial: restricted random sampling in a box
Gt = sp.lambdify((x, y, zz, a1, b1, c1), (G + 32) / 4, 'numpy')
rng = np.random.default_rng(1)
S = rng.uniform([0.2, 0.2, 0.2, -2, -2, -3], [2, 2, 2, 2, 2, 3], size=(200000, 6))
vals = Gt(*S.T)
print('triaxial box: min Q', vals.min(), ' frac negative', float((vals < 0).mean()))
