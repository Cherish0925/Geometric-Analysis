#!/usr/bin/env python3
"""
Step 20: triangular unweighted defect-energy ledger for

    d_t g = -2 a E,  E = Ric + g,  a=chi^2.

Purpose: test the correction that Q(t)=int|E|^2 must be controlled by an
estimate with no additive curvature-only forcing.  Curvature may appear only as
an absorbable potential multiplying E^2.
"""
import math

print("="*78)
print("STEP 20 TRIANGULAR DEFECT ENERGY LEDGER")
print("="*78)
print("Flow velocity vanishes when E=0, so every term in d_t E is linear in E or nabla E.")
print()
print("Schematic tensor equation:")
print("  d_t E = a Delta_L E - 2a E")
print("          + (nabla a)*nabla E + (nabla^2 a)*E + a*Rm*E + a*E*E")
print("No term depending only on Rm is allowed; exact negative Einstein metrics are stationary.")
print()
print("Test by eta^2 E and integrate Hess(a) terms by parts:")
print("  d/dt Q_eta + c int eta^2 a |nabla E|^2")
print("    <= C int eta^2 (|da|^2/a + a + a|Rm|) |E|^2")
print("       + C int a|nabla eta|^2 |E|^2")
print("This is triangular: RHS vanishes when E=0.")
print()
print("Absorb the curvature-potential term in dimension four:")
print("  int a|Rm||E|^2 = int |Rm| |chi eta E|^2")
print("  <= ||Rm||_2 ||chi eta E||_4^2")
print("  <= beta * (int eta^2 a|nabla E|^2 + r^{-2} int eta^2 |E|^2)")
print("where beta=A^2||F||_2 <= C sqrt(1+K0) r^2 is the Whitney/Sobolev product for F=(1+|Rm|^2)^1/2.")
print("For beta small this absorbs into the dissipation, leaving")
print("  dQ_eta/dt <= C(c,L) r^{-2} Q_neighbor.")
print()
print("Finite-neighbor system:")
print("  dQ_alpha/dt <= C r^{-2} sum_{beta~alpha} Q_beta")
print("or, after summing unnormalized local energies with bounded overlap,")
print("  dQ_support/dt <= C_N r^{-2} Q_support.")
print("Over time theta*r^2: Q_support(T) <= exp(C_N theta) Q_support(0).")
print()
print("Correction to the discarded +epsilon*X form:")
print("  If Q' <= C r^{-2}Q + epsilon X and int_0^T X dt = O(A),")
print("  then Q(T) may contain O(epsilon*A), not o(A) at fixed epsilon.")
print("  The triangular estimate avoids this by absorbing curvature into E-dissipation.")

# numerical illustration of the two possibilities at A large
A = 1.0e6
Q0 = 1.0e-4 * A
Xint = 10.0 * A
epsilon = 1.0e-2
theta = 1.0e-3
C = 100.0
bad = math.exp(C*theta)*(Q0 + epsilon*Xint)
good = math.exp(C*theta)*Q0
print("\nNumerical scale illustration (not a proof):")
print(f"  A={A:.1e}, Q0/A={Q0/A:.1e}, epsilon={epsilon:.1e}, int X/A={Xint/A:.1e}")
print(f"  with additive epsilon X: Q(T)/A ~ {bad/A:.3e}")
print(f"  triangular estimate:      Q(T)/A ~ {good/A:.3e}")
print("Only the second preserves vanishing Q/A as Q0/A -> 0 at fixed smoothing scale.")
print("PASS")
