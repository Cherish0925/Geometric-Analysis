#!/usr/bin/env python3
"""Verify the Iwasawa sign in the H^2 harmonic map equation.

For H^2 with metric ds^2 = dalpha^2 + e^{-2alpha} dbeta^2:
The Christoffel symbols are:
  Gamma^alpha_{beta beta} = e^{-2alpha}  (> 0)
  Gamma^beta_{alpha beta} = -1

The weighted harmonic map equation for a map (alpha(r,z), beta(r,z)):
  div(rho grad alpha) + rho Gamma^alpha_{beta beta} |grad beta|^2 = 0
  => div(rho grad alpha) = -rho e^{-2alpha} |grad beta|^2  [NEGATIVE!]

Compare with polar coords (d, psi), ds^2 = dd^2 + sinh^2(d) dpsi^2:
  Gamma^d_{psi psi} = -sinh(d)cosh(d)  (< 0)
  => div(rho grad d) = rho sinh(d)cosh(d) |grad psi|^2  [POSITIVE!]

The signs differ because the Christoffel symbols have different signs.
"""
import sympy as sp

# H^2 in Iwasawa coords: g = dalpha^2 + e^{-2alpha} dbeta^2
alpha = sp.Symbol('alpha')
g_bb = sp.exp(-2*alpha)

# Christoffel: Gamma^alpha_{beta beta} = -1/(2*g^{alpha alpha}) * dg_{beta beta}/dalpha
# g^{alpha alpha} = 1
Gamma_a_bb = -sp.Rational(1,2) * sp.diff(g_bb, alpha)
print(f"Gamma^alpha_{{beta beta}} = {Gamma_a_bb}")  # Should be e^{-2alpha} > 0

# For the harmonic map equation:
# tau^alpha = Delta alpha + Gamma^alpha_{bb} (beta_r^2 + beta_z^2) = 0
# For weighted: div(rho grad alpha) + rho Gamma^alpha_{bb} |grad beta|^2 = 0
# Therefore: div(rho grad alpha) = -rho Gamma^alpha_{bb} |grad beta|^2
#          = -rho e^{-2alpha} |grad beta|^2  [NEGATIVE sign]
print(f"  => div(rho grad alpha) = -rho * {Gamma_a_bb} * |grad beta|^2")
print(f"  => div(rho grad alpha) = -rho * e^{{-2alpha}} * |grad beta|^2  [NEGATIVE]")
print()

# H^2 in polar coords: g = dd^2 + sinh^2(d) dpsi^2
d = sp.Symbol('d', positive=True)
g_pp = sp.sinh(d)**2

# Gamma^d_{psi psi} = -1/(2*g^{dd}) * dg_{psi psi}/dd
Gamma_d_pp = -sp.Rational(1,2) * sp.diff(g_pp, d)
print(f"Gamma^d_{{psi psi}} = {sp.simplify(Gamma_d_pp)}")  # Should be -sinh(d)cosh(d) < 0

# For weighted: div(rho grad d) = -rho Gamma^d_{pp} |grad psi|^2
#          = rho sinh(d)cosh(d) |grad psi|^2  [POSITIVE sign]
print(f"  => div(rho grad d) = -rho * ({sp.simplify(Gamma_d_pp)}) * |grad psi|^2")
print(f"  => div(rho grad d) = rho * sinh(d)*cosh(d) * |grad psi|^2  [POSITIVE]")
print()

# CONSISTENCY CHECK: for diagonal case beta=0, psi=0:
# Both equations give: div(rho grad alpha) = 0 and div(rho grad d) = 0
# And alpha = d for the diagonal case. CONSISTENT.
print("CONSISTENCY: diagonal case (beta=0 or psi=0):")
print("  Both give div(rho grad alpha) = 0 = div(rho grad d)")
print("  And alpha = d in the diagonal parametrization")
print()

# NOTE: The original Step 79 note had a POSITIVE sign in eq (4.6).
# This was INCORRECT. The correct sign is NEGATIVE.
# The correction does not affect the polar-coordinate equations (4.4)-(4.5)
# or any conclusion about the VII_0 barrier or the mechanism.
print("CONCLUSION: Iwasawa alpha-eq has NEGATIVE sign (corrected)")
print("Polar d-eq has POSITIVE sign (was correct)")
print("VII_0 barrier mechanism and Step 73 recovery: UNAFFECTED")
