#!/usr/bin/env python3
"""Exact algebra for the conformal-neck note; no PDE/existence certification."""

import sympy as s


def check(label, expression):
    remainder = s.factor(s.expand(expression))
    assert remainder == 0, (label, remainder)
    print("PASS:", label)


pi = s.pi
A, p, T, D, B, P, V = s.symbols("A p T D B P V", real=True)
scalar2 = B + 32 * pi**2 * p
R2 = 8 * pi**2 * (2 * p - T) + 32 * pi**2 * D
check("non-Kahler Ricci bridge",
      R2 - scalar2 / 4 + B / 4 - 8 * pi**2 * (p - T) - 32 * pi**2 * D)

scalar, mismatch = s.symbols("scalar mismatch", real=True)
w = (mismatch - scalar) / 2
check("scalar-band Bp expansion density",
      s.Rational(2, 3) * (scalar**2 + 2 * w**2)
      + s.Rational(2, 3) * scalar * mismatch
      - mismatch**2 / 3 - scalar**2)
assert s.simplify(s.Rational(2, 3) * s.sqrt(288) - 8 * s.sqrt(2)) == 0
print("PASS: scalar-band square-root coefficient")

lap, grad2 = s.symbols("lap grad2", real=True)
check("conformal scalar-square expansion before integration",
      (-4 - 6 * (lap + grad2))**2 - 16
      - 48 * lap - 48 * grad2 - 36 * (lap + grad2)**2)

V0 = 2 * pi**2 * A
scalar2_neck = 16 * V0 + B
Wplus2 = s.Rational(2, 3) * V0
D_neck = (scalar2_neck / 24 + Wplus2 / 2) / (4 * pi**2) - A / 2
P_neck = 2 * (2 * Wplus2 + scalar2_neck / 24 - 4 * pi**2 * A)
R_neck = P_neck + scalar2_neck / 4
check("exact conformal LB remainder", D_neck - B / (96 * pi**2))
check("exact conformal trace-free Ricci energy", P_neck - B / 12)
check("exact conformal total Ricci energy", R_neck - 8 * pi**2 * A - B / 3)
check("consistency with valid non-Kahler bridge",
      P_neck + B / 4 - 32 * pi**2 * D_neck)

Vm, Vp, cm, cp = s.symbols("Vm Vp cm cp", positive=True)
H0 = Vm + Vp
H2 = Vm * cm**2 + Vp * cp**2
H4 = Vm * cm**4 + Vp * cp**4
L_limit = 16 * (H0 - H2**2 / H4)
E_limit = 4 * (1 - H2**2 / (H0 * H4))
check("strict positive two-bulk variance factorization",
      H0 * H4 - H2**2 - Vm * Vp * (cm**2 - cp**2)**2)
assert s.simplify(L_limit / (4 * H0) - E_limit) == 0
print("PASS: relative Einstein-defect limit")
assert s.simplify(E_limit.subs({Vp: Vm, cm: 1, cp: s.sqrt(2)})) == s.Rational(2, 5)
print("PASS: equal-side concrete limit 2/5")
Q_limit = L_limit / 4
kappa_limit = H2 / H4
assert s.simplify(Q_limit / (kappa_limit**2 * H4)
                  - 4 * (H0 * H4 / H2**2 - 1)) == 0
print("PASS: scale-aware mean-normalized residual")

t, ell, radius = s.symbols("t ell radius", positive=True)
collar_primitive = ell * s.sinh(t)
check("collar area primitive", s.diff(collar_primitive, t) - ell * s.cosh(t))
check("fixed-window collar area",
      collar_primitive.subs(t, radius) - collar_primitive.subs(t, -radius)
      - 2 * ell * s.sinh(radius))
f1, f2 = s.symbols("f1 f2", real=True)
hessian = s.diag(f2, s.tanh(t) * f1, 0, 0)
df_tensor = s.diag(f1**2, 0, 0, 0)
raw = hessian - df_tensor
ricci0 = -2 * (raw - s.trace(raw) * s.eye(4) / 4)
check("optional conformal Ricci block is trace-free", s.trace(ricci0))

gm, gp, h = s.symbols("gm gp h", integer=True, positive=True)
side_sum = 8 * pi**2 * (2 * gm - 1) * (h - 1) + 8 * pi**2 * (2 * gp - 1) * (h - 1)
check("fixed-topology side volumes", side_sum - 16 * pi**2 * (gm + gp - 1) * (h - 1))
print("All exact checks passed; collar existence and SW nonvanishing remain proof inputs.")
