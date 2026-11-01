#!/usr/bin/env python3
"""Exact finite checks supporting the gauge-saturation realization note.

No compactness, monopole solvability, or nonlinear PDE claim is tested here.
"""
import sympy as sp

rho = sp.symbols("rho", positive=True)
w = sp.symbols("w", nonnegative=True)
assert sp.factor((w-2)**2 / 3 + sp.Rational(4, 3) - w*w/6) == (w-4)**2/6

# g_hat = rho**(-2) g in real dimension four.
curvature_norm_scale = rho**2
volume_scale = rho**(-4)
assert sp.simplify(curvature_norm_scale**2 * volume_scale) == 1

# Standard oriented self-dual basis: e12+e34, e13-e24, e14+e23.
a, b, c = sp.symbols("a b c", real=True)
W = sp.Matrix([[0, a, b, c], [-a, 0, c, -b],
               [-b, -c, 0, a], [-c, b, -a, 0]])
norm2 = sum(W[i, j] ** 2 for i in range(4) for j in range(i + 1, 4))
assert sp.simplify(norm2 - 2 * (a*a + b*b + c*c)) == 0
assert W * W == -(a*a + b*b + c*c) * sp.eye(4)
assert sp.expand(a*a + b*b + c*c - norm2/2) == 0

# Parameter-two normalization on Ric=-g Kähler–Einstein surfaces.
S_per_V, W_per_V, p_per_V = 16, sp.Rational(2, 3), 1 / (2 * sp.pi**2)
assert sp.simplify(sp.Rational(3, 2) * (S_per_V + 12*W_per_V)
                   - 72 * sp.pi**2 * p_per_V) == 0

# Exact Chern--Weil elimination and fixed-shear quantitative saturation.
S, W2, P, T, p, A, V, delta = sp.symbols("S W2 P T p A V delta")
cw = sp.Eq(4*sp.pi**2*T, S/24 + 2*W2 - P/2)
weyl_energy = sp.solve(cw, W2)[0]
deficit = sp.Rational(3, 2) * (S + 12*W2) - 72*sp.pi**2*p
eliminated = sp.Rational(9, 8)*S + 36*sp.pi**2*T + sp.Rational(9, 2)*P - 72*sp.pi**2*p
assert sp.expand(deficit.subs(W2, weyl_energy) - eliminated) == 0
upper = eliminated.subs({S:16*(1+delta)**2*V, P:4*delta**2*V, T:A, p:A}) / V
assert sp.simplify(upper.subs(V, 2*sp.pi**2*A) - 36*delta*(1+delta)) == 0

print("PASS: amplitude inequality, critical scaling, global-form algebra, KE normalization, shear saturation")
