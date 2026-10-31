"""Numerical check of the closed form of the slice transgression:
  T/(8 pi^2) = Y^2 + Pi,
  Y  = c' - 2 cosh 2w + z^2 + p_+ p_- / 2,
  Pi = e^{2w} p_+^2 + e^{-2w} p_-^2 - (p_+ p_-)^2 / 4,
  p_+ = (b a' - c + (a^2-b^2)/c)/sqrt(ab),  p_- = (a b' - c - (a^2-b^2)/c)/sqrt(ab),
  e^{2w} = a/b,  z = c/sqrt(ab)   (a,b,c slice radii; ' = d/dt, t arclength).
against the Cartan-derived G of bianchi_transgression.py.
"""
import numpy as np
import sympy as sp
import transgression_values as tv

G = tv.load()[1]
syms = [tv.loc[k] for k in ('x', 'y', 'z', 'a1', 'b1', 'c1')]
Gf = sp.lambdify(syms, (G + 32) / 4, 'numpy')
rng = np.random.default_rng(7)
N = 100000
a, b, c = rng.uniform(0.2, 3, (3, N))
a1, b1, c1 = rng.normal(0, 1.5, (3, N))
Q = Gf(a, b, c, a1, b1, c1)
s = np.sqrt(a * b)
pp = (b * a1 - c + (a**2 - b**2) / c) / s
pm = (a * b1 - c - (a**2 - b**2) / c) / s
e2w = a / b
z = c / s
cosh2w = (e2w + 1 / e2w) / 2
Y = c1 - 2 * cosh2w + z**2 + pp * pm / 2
Pi = e2w * pp**2 + pm**2 / e2w - (pp * pm)**2 / 4
err = np.abs(Q - (Y**2 + Pi)) / (1 + np.abs(Q))
print('max relative error of closed form over', N, 'random slices:', err.max())
print('bolt Y:', -1, ' CH collar Y = R^2/2 (analytic)')
