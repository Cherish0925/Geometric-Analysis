#!/usr/bin/env python3
"""
Step 26: exponent and scaling ledger for the support-wide weighted velocity route.

This script checks the powers in the fixed-p defect energy

    J_p = int eta^2 a^(p-2) |E|^p,
    z_p = a^((p-1)/2) |E|^(p/2),  a = chi^2,

under the buffered selected-support cutoff flow.  It does not prove the PDE
Moser theorem; it verifies the weights and the collapse/scale cancellation that
make the theorem plausible and precise.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import sympy as sp


p = sp.symbols("p", positive=True)
a, F, Eabs, dchi2, r, delta, V, theta, t = sp.symbols(
    "a F E dchi2 r delta V theta t", positive=True
)

# Densities, suppressing eta^2.
J_density = a ** (p - 2) * Eabs**p
z_sq = a ** (p - 1) * Eabs**p
potential = a ** (p - 1) * F * Eabs**p
assert sp.simplify(potential - F * z_sq) == 0

# gradient cutoff in |grad z_p|^2: a^(p-3) |da|^2 |E|^p with |da|^2=4a|dchi|^2.
grad_cutoff = a ** (p - 3) * (4 * a * dchi2) * Eabs**p
assert sp.simplify(grad_cutoff - 4 * dchi2 * J_density) == 0

# Desired velocity variable.  Pointwise |aE|^p is dominated by J_density because a<=1.
weighted_velocity_p = a**p * Eabs**p
ratio_velocity_to_J = sp.simplify(weighted_velocity_p / J_density)  # a^2
assert ratio_velocity_to_J == a**2

# Critical Sobolev/Moser scaling in dimension four.
# Relative Sobolev coefficient: ||u||_4^2 <= A2 (||grad u||_2^2+r^-2||u||_2^2),
# with A2 ~ r^2 V^{-1/2}; heat/Moser L^p->Linf factor ~ A2^(2/p) t^(-2/p).
A2 = r**2 * V ** sp.Rational(-1, 2)
Jp_norm = delta * V ** (1 / p)  # J_p(0)^(1/p) from |E|<=delta.
linf_bound = sp.simplify(A2 ** (sp.Rational(2, 1) / p) * t ** (-sp.Rational(2, 1) / p) * Jp_norm)
# Expected collapse cancellation: delta*r^(4/p)*t^(-2/p)
expected = delta * r ** (sp.Rational(4, 1) / p) * t ** (-sp.Rational(2, 1) / p)
print("Fixed-p defect weights")
print("J_density         =", J_density)
print("z_p^2             =", z_sq)
print("potential          =", potential, "= F*z_p^2")
print("grad cutoff        =", grad_cutoff, "= 4|dchi|^2*J_density")
print("(|aE|^p)/J_density=", ratio_velocity_to_J, "<= 1 for 0<=a<=1")
print()
print("Dimension-4 Moser scaling")
print("A2 ~", A2)
print("J_p(0)^(1/p) ~", Jp_norm)
print("A2^(2/p) t^(-2/p) J_p^(1/p) =", linf_bound)
print("expected collapse-free form       =", expected)
assert sp.simplify(linf_bound / expected - 1) == 0

# Integrability of t^{-2/p}; compute representative p values.
def integral_factor(pval: float, theta_val: float = 1e-3, r_val: float = 1.7e-3) -> float:
    if pval <= 2:
        return math.inf
    # integral of delta*r^(4/p)*t^(-2/p) from 0 to theta*r^2, without delta and constants.
    return (pval / (pval - 2.0)) * (r_val ** (4.0 / pval)) * ((theta_val * r_val**2) ** (1.0 - 2.0 / pval))

for pval in [2.1, 3.0, 4.0, 6.0, 8.0, 12.0]:
    fac = integral_factor(pval)
    print(f"integral prefactor for p={pval:4.1f}: {fac:.6e}")

# p=6 recovers the exponent used earlier: |aE| <= C delta (r^2/t)^(1/3), up to constants.
p6_bound = sp.simplify(expected.subs(p, 6))
p6_expected = delta * r ** sp.Rational(2, 3) * t ** sp.Rational(-1, 3)
assert sp.simplify(p6_bound / p6_expected - 1) == 0
print()
print("p=6 bound:", p6_bound, "= delta*r^(2/3)*t^(-1/3)")
print("PASS: fixed-p J_p weights and the support-wide weighted-velocity scaling are consistent.")
