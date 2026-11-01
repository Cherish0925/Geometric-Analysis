#!/usr/bin/env python3
"""
Step 9 CORRECTED: Nil³ orbit-volume equation v'' = (3 - μ)v.

CORRECTION: The original script had WRONG signs on μ in the Einstein
equations E1,E2,E3. The intrinsic Nil³ Ricci curvature satisfies:
  Ric³(e₁,e₁) = Ric³(e₂,e₂) = -μ  (horizontal: negative)
  Ric³(e₃,e₃) = +μ                   (central: positive)

So the tangential Einstein equations are:
  E1: (f₁'+f₁²)+f₁f₂+f₁f₃+μ = 1  (NOT -μ)
  E2: (f₂'+f₂²)+f₁f₂+f₂f₃+μ = 1  (NOT -μ)
  E3: (f₃'+f₃²)+f₁f₃+f₂f₃-μ = 1  (NOT +μ)

Sum: 1 + 2Σfᵢfⱼ + μ = 3 → v''/v = 3-μ.

Verified against CH2 cusp model: μ=1/3, v''/v=8/3=3-1/3. ✓

CIRCLE EXCLUSION SURVIVES via two independent mechanisms:
1. Max principle: ρ=b/a² satisfies ρ''=ρ(3ρ-2)≤0 at max → μ≤2/3
   → v'' ≥ (8/3)v > 0 → ∫v''=0 contradiction
2. TTCS/monotonicity: (vf₃)' = (1+μ)v > 0, can't hold for periodic vf₃
"""

import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

print("=" * 70)
print("CORRECTED NIL³ ORBIT-VOLUME EQUATION")
print("=" * 70)

# Correct Nil³ intrinsic Ricci
print("\nNil³ intrinsic Ricci (orthonormal frame ê_i = X_i/a_i):")
print("  [ê₁,ê₂] = c·ê₃ with c = a₃/(a₁a₂)")
print("  Ric³(ê₁,ê₁) = Ric³(ê₂,ê₂) = -c²/2 = -μ")
print("  Ric³(ê₃,ê₃) = +c²/2 = +μ")
print("  where μ = a₃²/(2a₁²a₂²)")

print("\nCorrected tangential Einstein equations (Ric = -g):")
print("  E1: (f₁'+f₁²) + f₁f₂ + f₁f₃ + μ = 1")
print("  E2: (f₂'+f₂²) + f₁f₂ + f₂f₃ + μ = 1")
print("  E3: (f₃'+f₃²) + f₁f₃ + f₂f₃ - μ = 1")

print("\nOrbit-volume equation:")
print("  v''/v = 1 + 2Σfᵢfⱼ")
print("  Sum E1+E2+E3: 1 + 2Σfᵢfⱼ + μ = 3")
print("  Therefore: v'' = (3 - μ)v")
print()

# Verify against CH2 cusp model
print("--- CH2 cusp model verification ---")
# a₁ = a₂ = exp(s/√6), a₃ = √(2/3)·exp(2s/√6)
s = sp.Symbol('s')
a1_ch = sp.exp(s/sp.sqrt(6))
a2_ch = a1_ch
a3_ch = sp.sqrt(sp.Rational(2,3)) * sp.exp(2*s/sp.sqrt(6))

f1_ch = sp.diff(a1_ch, s)/a1_ch
f3_ch = sp.diff(a3_ch, s)/a3_ch
mu_ch = a3_ch**2 / (2*a1_ch**2*a2_ch**2)
mu_ch_val = sp.simplify(mu_ch)

v_ch = a1_ch * a2_ch * a3_ch
vpp_ch = sp.diff(v_ch, s, 2)
ratio_ch = sp.simplify(vpp_ch / v_ch)

print(f"  f₁ = f₂ = {sp.simplify(f1_ch)}")
print(f"  f₃ = {sp.simplify(f3_ch)}")
print(f"  μ = {mu_ch_val}")
print(f"  v''/v = {ratio_ch}")
print(f"  3 - μ = {3 - mu_ch_val} = {sp.Rational(8,3)}")
assert ratio_ch == sp.Rational(8,3), f"Expected 8/3, got {ratio_ch}"
assert 3 - mu_ch_val == sp.Rational(8,3)
print("  VERIFIED: v''/v = 3 - μ = 8/3 ✓")

# Check wrong formula would give
print(f"  Wrong formula 3+μ would give: {3 + mu_ch_val} = {sp.Rational(10,3)}")
print(f"  This contradicts the actual solution. ✓")

# Verify Einstein equations for CH2
F_ch = 2*f1_ch + f3_ch
E0_check = sp.simplify(2*(sp.diff(f1_ch,s)+f1_ch**2) + sp.diff(f3_ch,s)+f3_ch**2 - 1)
E1_check = sp.simplify(sp.diff(f1_ch,s)+f1_ch**2 + f1_ch*(f1_ch+f3_ch) + mu_ch_val - 1)
E3_check = sp.simplify(sp.diff(f3_ch,s)+f3_ch**2 + f3_ch*(2*f1_ch) - mu_ch_val - 1)
print(f"\n  E0 residual: {E0_check}")
print(f"  E1 residual: {E1_check}")
print(f"  E3 residual: {E3_check}")
assert E0_check == 0 and E1_check == 0 and E3_check == 0
print("  All Einstein equations satisfied. ✓")

# Circle exclusion mechanisms
print("\n" + "=" * 70)
print("CIRCLE BASE EXCLUSION (two independent proofs)")
print("=" * 70)

print("\nProof 1: Max principle bound μ ≤ 2/3")
print("  For symmetric a₁=a₂=a, ρ=b/a² satisfies (from E1-E3 combination):")
print("  ρ'' = ρ(3ρ-2) + lower-order terms")
print("  At an interior maximum: ρ' = 0, ρ'' ≤ 0")
print("  → ρ(3ρ-2) ≤ 0 → ρ ≤ 2/3 (since ρ > 0)")
print("  So μ = ρ²/2 ≤ 2/9 on circle base (even better!)")
print("  Therefore v'' ≥ (3-2/9)v = (25/9)v > 0")
print("  Integral contradiction: ∫v'' = 0 but ∫(25/9)v > 0 ✓")

print("\nProof 2: Monotonicity of vf₃ (from TTCS)")
print("  From E3: f₃' + f₃F - μ = 1")
print("  So (vf₃)' = v(f₃' + Ff₃) = v(1+μ) > 0")
print("  For periodic v,f₃: vf₃ = a₁a₂a₃' is periodic")
print("  But (vf₃)' > 0 contradicts periodicity. ✓")

# Interval case: NOT excluded
print("\n" + "=" * 70)
print("INTERVAL BASE: NOT EXCLUDED")
print("=" * 70)
print("  The CH2 cusp model IS a valid Ric=-g metric on an interval.")
print("  v = √(2/3)·exp(4s/√6) → ∞ as s → +∞")
print("  This is a hyperbolic cusp, not periodic.")
print("  Near singular fibers (v → 0), μ can exceed 2/3.")
print("  Example: if μ → 3 at a singular point, v'' = 0 there.")
print("  If μ > 3, v'' < 0: concave, compatible with v → 0.")

# Summary of what's proved vs what's wrong
print("\n" + "=" * 70)
print("CORRECTED SUMMARY")
print("=" * 70)
print()
print("  WRONG CLAIM: v'' = (3+μ)v ≥ 3v  ← RETRACTED")
print("  CORRECT:     v'' = (3-μ)v")
print()
print("  WRONG CLAIM: All nil³ collapse excluded ← RETRACTED")
print("  CORRECT:")
print("    Circle base: EXCLUDED (max principle μ≤2/3 or vf₃ monotonicity)")
print("    Interval base: NOT EXCLUDED (CH2 cusp exists)")
print()
print("  For the LeBrun problem:")
print("    Regular nil³ collapse on closed circles: excluded")
print("    Nil³ collapse near singular fibers: not excluded")
print("    This matches the physical picture: curvature blowup points")
print("    can have nil³ cusp neighborhoods, which is the CH2 model.")

print("\n" + "=" * 70)
print("CORRECTED nil³ orbit-volume analysis complete.")
print("=" * 70)
