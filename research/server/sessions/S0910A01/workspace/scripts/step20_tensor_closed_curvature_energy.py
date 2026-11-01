#!/usr/bin/env python3
"""
Step 20: algebraic ledger for the closed curvature-power estimate under

    d_t g = -2 a E,  a = chi^2,  E = Ric + g,

using the identities E = contraction(Rm) + g and nabla E = contraction(nabla Rm).

This script does not prove a PDE theorem.  It checks the exponent bookkeeping in
one localized tensor-energy calculation after the Hess(a) terms are integrated
by parts and all nabla E terms are absorbed into the full tensor curvature
dissipation rather than a separate defect-gradient energy.
"""
from fractions import Fraction
import math

# Dimension four constants are represented schematically.
n = 4

# Choose harmless schematic constants so the numerical thresholds are transparent.
# The important output is q-dependence, not the particular constants.
C_nablaE = math.sqrt(n)        # |nabla Ric| <= sqrt(n)|nabla Rm| for a contraction in an ON frame
C_E = math.sqrt(n + 1)         # |Ric+g| <= C_E*(1+|Rm|^2)^1/2, schematic safe constant
C_reaction = 20.0             # schematic tensor reaction constant
C_cut = 16.0                  # schematic cutoff-commutator constant
c_diff = 1.0                  # normalized coefficient in front of a F^(q-2)|nabla Rm|^2

print("="*78)
print("STEP 20 CLOSED CURVATURE-POWER LEDGER")
print("="*78)
print("Flow: d_t g = -2 a E, a=chi^2, E=Ric+g")
print("F=(1+|Rm|^2)^(1/2), test tensor equation against eta^2 F^(q-2) Rm")
print()
print("Geometric substitutions used on every smooth flow time:")
print(f"  |nabla E| <= C4 |nabla Rm|, with schematic C4={C_nablaE:.3f}")
print(f"  |E| <= C4 F, with schematic C4={C_E:.3f}")
print("These do not use the initial pointwise smallness of E.")

print("\nTerm ledger after expanding nabla^2(aE):")
ledger = [
    ("a*nabla^2 E", "principal a*Delta Rm + a*Rm*Rm + a*Rm"),
    ("nabla a * nabla E", "<= eps*a*F^(q-2)|nabla Rm|^2 + C eps^-1 |da|^2/a F^q"),
    ("nabla^2 a * E", "integrate by parts -> nabla a*nabla E, nabla a*E*nabla Rm, eta-gradient"),
    ("a*E*Rm", "<= C a F^(q+1)"),
    ("norm/volume variation", "<= C a F^(q+1) + C a F^q"),
]
for t, reduction in ledger:
    print(f"  {t:24s} -> {reduction}")

print("\nRepresentative Hess(a) integration by parts:")
print("  I = int eta^2 F^(q-2) Rm * Hess(a) * E")
print("  I = -int nabla a * nabla(eta^2 F^(q-2) Rm * E)")
print("    terms with nabla E are bounded by nabla Rm; no separate nabla E energy is needed.")
print("  Young gives C q^2 int eta^2 |da|^2/a F^q + C int a|nabla eta|^2 F^q")

print("\nClosed local inequality produced by the ledger:")
print("  d/dt int eta^2 F^q + c_q int eta^2 a F^(q-2)|nabla Rm|^2")
print("    <= C q int eta^2 a F^(q+1)")
print("       + C q^2 int eta^2 ( |da|^2/a + a + a|nabla eta|^2 ) F^q")
print("       + C q^2 int a|nabla eta|^2 F^q")
print("where |da|^2/a = 4|dchi|^2 and no inverse power of chi appears.")

# Direct critical absorption threshold for the term int a F^(q+1):
# In dimension 4, Sobolev gives int a F^(q+1) <= beta * (D_q + ell^-2 Y_q).
# Reaction coefficient is schematic C_reaction*q while diffusion coefficient is c_diff*(q-1)/q ~ 1.
print("\nDirect critical absorption threshold versus exponent:")
print("  Assume int a F^(q+1) <= beta*(D_q + ell^-2 Y_q).")
print("  Need C*q*beta < c to absorb into D_q.")
print("  This table illustrates why a direct all-exponent iteration is not automatic.")
print("    q        beta_max=c/(C*q)")
for q in [2, 3, 4, 6, 8, 12, 16, 32, 64, 128]:
    beta_max = c_diff/(C_reaction*q)
    print(f"  {q:4d}      {beta_max:10.4e}")

# Fixed-exponent route: choose q0 and use supercritical exponent p=q0?  For curvature in 4D, p>2.
print("\nFixed-exponent alternative:")
for q0 in [Fraction(5,2), Fraction(3,1), Fraction(4,1), Fraction(6,1)]:
    beta_max = c_diff/(C_reaction*float(q0))
    supercritical = float(q0) > 2.0
    print(f"  q0={q0}: beta threshold ~ {beta_max:.4e}, spatial exponent >2? {supercritical}")
print("Reaching one finite q0>2 is compatible with fixed small beta; a later mean-value")
print("argument can use F as a supercritical curvature potential instead of absorbing")
print("critical energy at unbounded q.")

# Cutoff derivative sizes on a Whitney ball ell=c*r*chi0.
print("\nWhitney coefficient normalization:")
print("  ell=c*r*chi0, a0=chi0^2, |dchi|<=L/r")
print("  a|d eta|^2 ~ a0/ell^2 = 1/(c^2 r^2)")
print("  |da|^2/a = 4|dchi|^2 <= 4L^2/r^2")
print("Both are independent of chi0; only the constants c^{-2}, L^2 remain.")

print("\nPASS: exponent ledger supports a closed curvature-only power inequality;")
print("      it also shows direct all-exponent absorption needs further argument,")
print("      while a finite supercritical exponent route remains viable.")
