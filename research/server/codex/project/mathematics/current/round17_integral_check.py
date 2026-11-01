#!/usr/bin/env python3
"""Exact algebra for arbitrary-scalar monopole calibration.

The checks are independent of old checking functions. Existence of an
actual monopole solution and the analytic chain rule are proof inputs.
"""
import sympy as s

k, V, A, T, B, P, L = s.symbols("k V A T B P L", positive=True)
K, Fm, scalar2, rho2, scalar_rho = s.symbols(
    "K Fm scalar2 rho2 scalar_rho", real=True)

def check(name, expression):
    remainder = s.factor(s.expand(expression))
    assert remainder == 0, (name, remainder)
    print("PASS:", name)

check("exact arbitrary-scalar defect decomposition",
      (scalar2 + 2*scalar_rho + rho2 + 8*K + 8*Fm
       - (scalar2 - 32*s.pi**2*A)).subs(
           scalar_rho, -rho2-4*K).subs(rho2, 32*s.pi**2*A+8*Fm))

# Differential of the quadratic spinor map, without imported functions.
x = s.symbols("x0:4", real=True)
y = s.symbols("y0:4", real=True)
hopf = s.Matrix([2*(x[0]*x[2]+x[1]*x[3]),
                 2*(x[1]*x[2]-x[0]*x[3]),
                 x[0]**2+x[1]**2-x[2]**2-x[3]**2])
d_hopf = hopf.jacobian(x)*s.Matrix(y)
imaginary_pairing = x[0]*y[1]-x[1]*y[0]+x[2]*y[3]-x[3]*y[2]
check("Hopf differential with vertical component retained",
      d_hopf.dot(d_hopf)-4*sum(z*z for z in x)*sum(z*z for z in y)
      +4*imaginary_pairing**2)

rho, beta, bp, dr, u, v = s.symbols(
    "rho beta bp dr u v", real=True, nonzero=True)
clipped_derivative = s.Matrix([bp*dr, beta*u/rho, beta*v/rho])
check("radial clipping derivative",
      clipped_derivative.dot(clipped_derivative)
      -bp**2*dr**2-beta**2*(u*u+v*v)/rho**2)

phi = s.Matrix([beta, 0, 0])
model = beta**2*s.eye(3)/(48*k)-phi*phi.T/(16*k)
check("smooth capped Weyl-model norm",
      s.trace(model*model)-beta**4/(384*k*k))
orbit = s.diag(-2*k/3, k/3, k/3)
check("amplitude distance to product Weyl orbit",
      s.trace((model-orbit)**2)-(beta**2-16*k*k)**2/(384*k*k))

grad, ext, moment4, scalar_phi2 = s.symbols(
    "grad ext moment4 scalar_phi2", real=True)
Wenergy = 2*s.pi**2*T-scalar2/48+P/4
Wpair = grad/2-ext+scalar_phi2/6
Renergy = Wenergy+moment4/(384*k*k)+Wpair/(8*k)
square = (moment4+8*k*scalar_phi2+16*k*k*scalar2)/(384*k*k)
check("exact capped Hodge-Chern-Weil identity",
      (Renergy+ext/(8*k)-2*s.pi**2*(T-A)-P/4+B/16
       -grad/(16*k)-square).subs(B, scalar2-32*s.pi**2*A))

assert s.Rational(-1,16)+s.Rational(1,4)+s.Rational(576,384) == s.Rational(27,16)
assert s.Rational(608,384) == s.Rational(19,12)
assert 2*s.Rational(27,16)+2*s.Rational(288,384) == s.Rational(39,8)
assert 2*s.Rational(19,12)+2*s.Rational(288,384) == s.Rational(14,3)
assert 2*s.Rational(14,3)+s.Rational(1,24) == s.Rational(75,8)
print("PASS: one- and two-orientation constants")

D, scalar_mean_error = s.symbols("D scalar_mean_error", real=True)
check("mean-scalar normalization",
      (scalar2-32*s.pi**2*A).subs(
          scalar2, 16*k*k*V-8*k*scalar_mean_error+L).subs(
              A, (k*k*V-D)/(2*s.pi**2)).subs(scalar_mean_error, 0)
      -(16*D+L))
assert s.Rational(39,4)*16 == 156
assert s.Rational(39,4)+s.Rational(75,8) == s.Rational(153,8)
print("PASS: normalized arbitrary-metric product estimate")

# Classical equality remains an exact test, not a numerical trend.
assert model.subs(beta,4*k) == orbit
assert (16*D+L).subs({D:0,L:0}) == 0
print("PASS: negative Kahler-Einstein/product equality normalization")
print("All Round-17 integral-calibration checks passed.")
