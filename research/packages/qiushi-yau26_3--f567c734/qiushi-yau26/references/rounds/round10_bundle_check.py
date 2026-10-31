"""Exact algebra for round10_bundle.md; geometric existence is proved there."""

import sympy as s


def check(expr, label):
    assert s.simplify(expr) == 0, (label, expr)
    print(f"PASS {label}")


p, q, m = s.symbols("p q m", positive=True)
c, tau = s.symbols("c tau", positive=True)
qm = 2*q-1+m
cm = 4*(p-1)*(qm-1)
check(2*qm-2-(2*(2*q-2)+2*m), "Riemann-Hurwitz genus")
check(cm-(2*(4*(p-1)*(q-1))+4*m*(p-1)), "Euler characteristic base change")

V0 = 4*s.pi**2*c
V = 2*s.pi**2*(2*c+3*tau)
v = 1+3*tau/(2*c)
check(V/V0-v, "normalized Einstein volume")
check(V-V0-6*s.pi**2*tau, "absolute volume excess")

omega_sq = 4*s.pi**2*(2*c+3*tau)
b_dot_omega = -2*s.pi*c
hodge_sq = 2*b_dot_omega**2/omega_sq
check(hodge_sq-c/v, "null (1,1) Hodge norm")
H = 4*s.pi**2*hodge_sq
Gamma = V0-H
check(Gamma-V0*(1-1/v), "optimized energy gap")
check(Gamma-6*s.pi**2*tau/v, "signature expression for absolute gap")
check(Gamma/V-(v-1)/v**2, "averaged exact geometric defect")
check(Gamma/V0-(v-1)/v, "relative energy gap")

check(s.limit(v, c, s.oo)-1, "relative volume limit")
check(s.limit(Gamma/V0, c, s.oo), "normalized gap limit")
check(s.limit(Gamma, c, s.oo)-6*s.pi**2*tau, "nonzero absolute gap limit")

# The branched covers have fixed signature 2*tau0, not zero signature.
tau0 = s.symbols("tau0", positive=True)
vm = 1+3*(2*tau0)/(2*cm)
Gammam = 6*s.pi**2*(2*tau0)/vm
check(s.limit(Gammam, m, s.oo)-12*s.pi**2*tau0,
      "base-change absolute gap limit")
check(s.limit((vm-1)/vm**2, m, s.oo),
      "base-change averaged defect limit")

# Algebraic consistency witness for the exact tau=0 scalar budgets.
vv = s.symbols("vv", positive=True)
x, y, z, w = c*vv/2, c/(2*vv), c/2, -c/2
check(z-w-c, "zero-signature intersection identity")
check(x*y-c**2/4, "Cauchy-Schwarz admissibility")
slack = c*(vv-1)*(3*vv+1)/(2*vv)
check(2*c*vv-(x+y+2*z)-slack, "positive-orientation scalar budget")
check(2*c*vv-(x+y-2*w)-slack, "negative-orientation scalar budget")
check(V0-4*s.pi**2*(2*y)-V0*(1-1/vv),
      "positive energy gap remains algebraically admissible")

print("All 19 exact checks passed; no Einstein metric on E_D is asserted.")
