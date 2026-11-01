#!/usr/bin/env python3
"""
Step 20: finite-exponent route after the closed curvature-power inequality.

This script models the exponent bookkeeping suggested by Li's Theorem 3.4 proof:
critical L^2 smallness is used to keep local L^2 energy small and obtain a
positive-time L^3 curvature potential, rather than to absorb a reaction at every
unbounded exponent.  It is a bookkeeping model, not a PDE proof.
"""
import math

print("="*78)
print("FINITE-EXPONENT ROUTE BOOKKEEPING")
print("="*78)
print("Li source lines 245-255: after local L2 persistence, the proof derives")
print("  int_{B_r} f^3 <= C A e0^3 t^{-1}")
print("then applies a linear Moser theorem.  This is finite-exponent, not an")
print("all-exponent critical absorption at t=0.")

# Symbols normalized to Whitney radius/time.
# Let e0 = ||F||_2 on a Whitney ball, A2 = squared Sobolev coefficient S.
# beta = S e0.  The Li L3 potential scale is mu^3 ~ S e0^3 / t.
for beta in [0.02, 0.01, 0.005, 0.001]:
    print(f"\nAssume beta=S||F||_2 = {beta:g}")
    for tau in [1e-3, 1e-2, 1e-1]:
        # normalized time tau = t/r^2.  Potential coefficient for L^3 scales beta*e0^2/t,
        # but e0 is hidden in beta; we display the t^{-1} singularity and beta dependence.
        mu_scale = beta / tau
        print(f"  tau={tau:7.1e}: finite L3 potential scale ~ beta/tau = {mu_scale:8.3e}")

print("\nDirect all-exponent route would need beta < const/q at each exponent q:")
for beta in [0.02, 0.01, 0.005, 0.001]:
    qmax = 1.0/(20.0*beta)  # schematic from previous script C=20
    print(f"  beta={beta:g}: schematic direct absorption stops near q ~ {qmax:.1f}")

print("\nInterpretation:")
print("  - Critical smallness can plausibly create one positive-time L3 (or fixed q0>2) bound.")
print("  - It should not be assumed to run an unlimited q-doubling iteration with the same beta.")
print("  - The missing theorem is a localized Li/Wang mean-value step using the finite")
print("    supercritical curvature potential on nested Whitney cylinders.")
print("PASS")
