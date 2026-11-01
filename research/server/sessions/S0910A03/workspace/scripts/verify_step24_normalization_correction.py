#!/usr/bin/env python3
"""
Step 24 CORRECTION: The normalization -2ag DOES produce a linear Rm reaction
for the fully-lowered (0,4) tensor R_{ijkl}.

DECISIVE TEST (from TTCS):
If a≡1 and dg/dt = -2g, then g(t) = e^{-2t}g_0.
The Christoffel symbols and R^l_{ijk} are unchanged (conformal invariance).
But R_{ijkl} = g_{lm} R^m_{ijk}, so:
  R_{ijkl}(t) = e^{-2t} R_{ijkl}(0)
  => d/dt R_{ijkl} = -2 R_{ijkl}.

This is the linear reaction I missed!

The correct complete evolution under dg/dt = -2a(Ric+g) is:
  dRm/dt = a·ΔRm + a·Q(Rm) - 2a·Rm + (∇a)*(∇E) - (∇²a ∧ E)

where -2a·Rm is a DAMPING term (beneficial for energy estimates).

When E=0 (Einstein with Ric=-g): the Einstein-Lichnerowicz identity
  ΔRm + Q(Rm) = 2Rm
makes the total evolution vanish: a(2Rm) - 2aRm = 0. ✓
"""
import numpy as np

print("=" * 78)
print("STEP 24 CORRECTION: Linear normalization reaction -2a·Rm")
print("=" * 78)

# Decisive test: conformal dg/dt = phi·g => R_{ijkl}(t) = e^{phi t} R_{ijkl}(0)
# (for constant phi)
# Here phi = -2a with a=1: g(t) = e^{-2t}g_0.
# Christoffel: Gamma^k_{ij}(cg) = Gamma^k_{ij}(g) for constant conformal factor.
# R^l_{ijk}(cg) = R^l_{ijk}(g)  (upper index immune to constant scaling)
# R_{ijkl}(cg) = c R_{ijkl}(g)  (lowering adds one power of g)
# So d/dt R_{ijkl} = -2 R_{ijkl}. NOT zero.

phi = -2.0
T = 0.5
c = np.exp(phi * T)
print(f"\nTest: dg/dt = {phi}g, t={T}")
print(f"  g(t)/g(0) = e^({phi}·{T}) = {c:.6f}")
print(f"  R^l_ijk: unchanged (Christoffel invariant)")
print(f"  R_ijkl(t) = {c:.6f} R_ijkl(0)")
print(f"  d/dt R_ijkl = {phi} R_ijkl  (LINEAR reaction)")
print()

# For the full flow h=-2a(Ric+g), the lower-order terms decompose:
# From -2a·Ric: standard quadratic a·Q(Rm) (same as Wang's LRF)
# From -2a·g: coefficient of R_{ijkl} in (0,4) variation
#   = phi·R_{ijkl} from index lowering + phi·R_{ijkl} from formula
#   Wait, let me redo this carefully.

# The Chow-Lu-Ni formula for d(R^l_{ijk})/dt has lower-order terms
# involving h^p_l. For h=phi·g, h^p_l = phi·delta^p_l.
# These DO cancel for R^l_{ijk} (mixed tensor).
# But for R_{ijkl} = g_{lm}R^m_{ijk}:
#   d/dt R_{ijkl} = h_{lm}R^m_{ijk} + g_{lm}·d/dt(R^m_{ijk})
#                 = phi g_{lm}R^m_{ijk} + g_{lm}·(...)
#                 = phi R_{ijkl} + (terms without linear reaction)
# So the NET linear reaction for (0,4) tensor is phi·Rm = -2a·Rm.

print("SOURCE OF THE ERROR:")
print("  The Chow-Lu-Ni formula gives dR^l_{ijk}/dt (mixed tensor).")
print("  For conformal h=phi·g, the lower-order R·h terms DO cancel")
print("  for R^l_{ijk}.")
print("  But for R_{ijkl} = g_{lm}R^m_{ijk}, the INDEX LOWERING adds:")
print("  h_{lm}·R^m_{ijk} = phi·g_{lm}·R^m_{ijk} = phi·R_{ijkl}")
print("  This is the missing linear reaction -2a·Rm.")
print()

# Effect on energy estimates:
# The linear reaction -2a·Rm contributes to d|Rm|^2/dt:
#   2·R^{ijkl}·(-2a R_{ijkl}) = -4a|Rm|^2
# This is DAMPING (beneficial)!
#
# For F^2 = 1 + |Rm|^2:
#   -4a|Rm|^2 = -4a(F^2-1) = -4aF^2 + 4a
#
# In the integrated H_2 inequality, this becomes:
#   +4∫η²aF² on the LEFT side (helps)
#   -4∫η²a ≥ -4Vol on the RIGHT side (bounded source)

print("EFFECT ON ENERGY FRAMEWORK:")
print("  d|Rm|²/dt gets -4a|Rm|² = -4a(F²-1)")
print("  In the H₂ inequality:")
print("    LEFT:  +4∫η²aF² (damping, BENEFICIAL)")
print("    RIGHT: -4∫η²a ≥ -4Vol (bounded source)")
print()
print("  The Wang q=2 estimate is IMPROVED, not worsened.")
print("  The cubic reaction CaF³ is partially cancelled by -4aF²")
print("  for moderate F.")
print()

# Einstein-Lichnerowicz identity check:
# For Ric=-g (Einstein), ΔRm + Q(Rm) = 2Rm.
# So: a(ΔRm + Q(Rm)) - 2aRm = a·2Rm - 2aRm = 0. ✓
print("STATIONARITY CHECK (Einstein, Ric=-g):")
print("  ΔRm + Q(Rm) = 2Rm  (Einstein-Lichnerowicz)")
print("  a(ΔRm + Q(Rm)) - 2aRm = a·2Rm - 2aRm = 0  ✓")
print()

# Verify the metric-norm variation contribution:
# dg^{ij}/dt = -g^{ia}g^{jb}h_{ab} = 2aE^{ij}
# For |Rm|² = g^{ia}g^{jb}g^{kc}g^{ld}R_{abcd}R_{ijkl}:
# metric variation: 4 × 2aE × Rm² = O(aF³)
# plus the d(R_{ijkl})/dt contribution including the linear term.
# Total: a(ΔRm + Q(Rm) - 2Rm) + cutoff + metric variation
#       = aΔ|Rm|² - 2a|∇Rm|² + a·(quadratic in Rm) - 4a|Rm|²
#         + O(aF³) + cutoff terms

# Combined reaction for d(F²)/dt:
# = -2a|∇F|² (dissipation)
# + a·(Q + 8E·Rm²) (cubic reaction, ≤ CaF³)
# - 4a|Rm|² (linear damping)
# + 4a (from |Rm|² = F²-1)
# + cutoff terms

print("COMPLETE d(F²)/dt STRUCTURE:")
print("  = a·ΔF² - 2a|∇F|²")
print("  + a·Q(Rm)                     (cubic, ≤ CaF³)")
print("  + 8aE·Rm²                     (metric variation, ≤ CaF³)")
print("  - 4aF²                        (normalization DAMPING)")
print("  + 4a                           (bounded source)")
print("  + (∇a)*(∇E)·Rm                (IBP → Young)")
print("  + (∇²a ∧ E)·Rm                (IBP → regular)")
print()
print("Net reaction: ≤ CaF³ - 4aF² + 4a + lower order")
print("  The -4aF² HELPS: it offsets the cubic for moderate F.")

# Correction summary
print()
print("=" * 78)
print("CORRECTION SUMMARY:")
print("  Step 22's 'reaction a*(Rm*Rm + Rm)' was partially correct but")
print("  for the WRONG REASON: the +Rm is NOT from the lower-order R·h")
print("  terms (which cancel for the mixed tensor), but from the INDEX")
print("  LOWERING of the metric variation h_{lm}R^m_{ijk} = phi·R_{ijkl}.")
print()
print("  Corrected: dRm/dt = a·ΔRm + a·Q(Rm) - 2a·Rm + cross terms")
print("  The -2a·Rm is a DAMPING term that IMPROVES energy estimates.")
print("  Einstein stationarity holds by the Lichnerowicz identity.")
print("=" * 78)
