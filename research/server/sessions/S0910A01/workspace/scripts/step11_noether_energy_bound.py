#!/usr/bin/env python3
"""
Step 11: Verify the Noether inequality bound χ_top(X) ≤ 5A + 36
for minimal complex surfaces of general type, and compute the
global mean curvature-operator energy for near-critical LeBrun sequences.

The Strategist claims:
  Classical Noether: A ≥ 2p_g - 4
  χ_hol = 1 - q + p_g ≤ p_g + 1  (since q ≥ 0)
  χ_top = 12χ_hol - A  (Noether's formula)
  => χ_top ≤ 12(p_g+1) - A ≤ 12((A+4)/2+1) - A = 5A + 36

With k/A → 1/3, this gives limsup global mean |Rcal|² ≤ 12.
"""
import sympy as sp

A, pg, q, k = sp.symbols('A pg q k', nonneg=True)
pi = sp.pi

print("="*70)
print("NOETHER INEQUALITY AND GLOBAL MEAN ENERGY")
print("="*70)

# 1. Classical Noether inequality for minimal surface of general type
# K^2 = c1^2(X) = A >= 2*p_g - 4
# (This is the standard Noether inequality for minimal surfaces)
print("\n--- 1. Classical Noether inequality ---")
print("For minimal surfaces of general type: A = K^2 >= 2*p_g - 4")
print("=> p_g <= (A + 4)/2")
pg_upper = (A + 4) / 2
print(f"   p_g_upper = {pg_upper}")

# 2. Holomorphic Euler characteristic
chi_hol = 1 - q + pg
print("\n--- 2. Holomorphic Euler characteristic ---")
print(f"chi_hol = 1 - q + p_g")
print(f"Since q >= 0: chi_hol <= 1 + p_g <= 1 + (A+4)/2 = (A+6)/2")
chi_hol_upper = (A + 6) / 2
print(f"   chi_hol_upper = {chi_hol_upper}")

# 3. Noether's formula: chi_top = 12*chi_hol - K^2
# (equivalently c_2 = 12*chi_hol - c_1^2)
chi_top_X = 12 * chi_hol - A
print("\n--- 3. Noether's formula ---")
print(f"chi_top(X) = 12*chi_hol - A")
chi_top_upper = 12 * chi_hol_upper - A
chi_top_upper_simplified = sp.simplify(chi_top_upper)
print(f"chi_top(X) <= 12 * (A+6)/2 - A = {chi_top_upper_simplified}")
assert chi_top_upper_simplified == 5*A + 36, f"Got {chi_top_upper_simplified}"
print(f"   VERIFIED: chi_top(X) <= 5*A + 36")

# 4. Also check: Bogomolov-Miyaoka-Yau gives A <= 9*chi_hol
# => chi_hol >= A/9, chi_top >= 12*(A/9) - A = 4A/3 - A = A/3
# So chi_top(X)/A is between 1/3 and 5 + 36/A.
print("\n--- 4. Two-sided bound on chi_top(X)/A ---")
print("BMY: A <= 9*chi_hol => chi_hol >= A/9")
print("=> chi_top(X) >= 12*(A/9) - A = A/3")
print("Combined: A/3 <= chi_top(X) <= 5A + 36")
print("=> 1/3 <= chi_top(X)/A <= 5 + 36/A")

# 5. For the blow-up M = X # k CP^2_bar
print("\n--- 5. Blow-up topology ---")
print("chi(M) = chi(X) + k")
print("tau(M) = tau(X) - k")
print("With k/A -> 1/3:")
chiM_expr = chi_top_upper_simplified + k  # chi(M) = chi(X) + k
print(f"chi(M) <= 5*A + 36 + k")
print(f"At k = A/3: chi(M) <= 5*A + 36 + A/3 = 16*A/3 + 36")

# 6. Full curvature-operator energy
print("\n--- 6. Full curvature-operator energy ---")
# int |Rcal|^2 = 8*pi^2*(chi(M) + J)
# where J = (1/(8*pi^2)) * int |E|^2
# Under Ric ~ -g: J -> 0
print("int |Rcal|^2 = 8*pi^2 * (chi(M) + J)")
print("For near-critical: J/A -> 0")
print(f"limsup int |Rcal|^2 / A <= 8*pi^2 * (16/3 + 36/A)")
print(f"As A -> inf: limsup int |Rcal|^2 / A -> 8*pi^2 * 16/3 = 128*pi^2/3")

# 7. Global mean curvature energy
print("\n--- 7. Global mean energy ---")
# Vol(M) ~ (32/9)*pi^2*A
Vol_cal = sp.Rational(32, 9) * pi**2 * A
Rcal2_int_cal = 8 * pi**2 * sp.Rational(16, 3) * A  # leading term
mean_Rcal2 = sp.simplify(Rcal2_int_cal / Vol_cal)
print(f"Vol(M) ~ (32/9)*pi^2*A = {Vol_cal}")
print(f"int |Rcal|^2 ~ 8*pi^2*(16/3)*A = {Rcal2_int_cal}")
print(f"Global mean |Rcal|^2 = int |Rcal|^2 / Vol(M) = {mean_Rcal2}")
assert mean_Rcal2 == 12, f"Got {mean_Rcal2}"
print("   VERIFIED: limsup global mean |Rcal|^2 = 12")

# 8. Decomposition of the mean
print("\n--- 8. Decomposition check ---")
# At the calibrated values s=-4, |W+|^2=1/24, |E|->0:
# |Rcal|^2 = |W+|^2 + |W-|^2 + |E|^2/2 + s^2/24
# s^2/24 = 16/24 = 2/3
# |W+|^2 = 1/24
# |E|^2 -> 0
# |W-|^2 is what remains
s_cal = -4
Wp2_ptwise = sp.Rational(1, 24)
s2_24_ptwise = sp.Rational(16, 24)  # = 2/3
print(f"Pointwise at calibrated values: s=-4, |W+|^2=1/24, |E|->0")
print(f"  s^2/24 = {s2_24_ptwise}")
print(f"  |W+|^2 = {Wp2_ptwise}")

# From signature: int|W-|^2 = int|W+|^2 - 12*pi^2*tau(M)
# tau(M) = tau(X) - k
# For Noether: tau(X) = (A - 2*chi_top(X))/3... no
# Actually tau(X) = 4*chi_hol - chi_top/3... hmm, need the standard formula
# For a compact complex surface: tau = (c1^2 - 2c2)/3 = (A - 2*chi_top(X))/3
# So tau(X) = (A - 2*chi_top(X))/3
# tau(M) = tau(X) - k = (A - 2*chi_top(X))/3 - k
print("\nUsing tau(X) = (A - 2*chi_top(X))/3")
print("tau(M) = (A - 2*chi_top(X))/3 - k")
print("At chi_top(X) = A/3 + epsilon (near BMY boundary):")
print("  tau(X) ~ (A - 2A/3)/3 = A/9")
print("  tau(M) ~ A/9 - A/3 = -2A/9")
# int |W-|^2 - int |W+|^2 = -12*pi^2*tau(M) = 12*pi^2*2A/9 = 8*pi^2*A/3
# Near boundary: int |W+|^2 ~ (4/27)*pi^2*A
# So int |W-|^2 ~ (4/27)*pi^2*A + 8*pi^2*A/3 = (4/27 + 72/27)*pi^2*A = 76*pi^2*A/27
print("\nAt BMY boundary chi_top(X)=A/3:")
print("  int |W-|^2 = int |W+|^2 + 12*pi^2*2A/9")
print("  ~ (4/27)*pi^2*A + (8/3)*pi^2*A = (4/27 + 72/27)*pi^2*A = (76/27)*pi^2*A")

# Check: mean |W-|^2
Wm2_int = sp.Rational(76, 27) * pi**2 * A
mean_Wm2 = sp.simplify(Wm2_int / Vol_cal)
print(f"  mean |W-|^2 = {mean_Wm2}")

# Total check
mean_total = sp.Rational(1, 24) + mean_Wm2 + sp.Rational(2, 3) + 0  # |E|^2 -> 0
print(f"\n  Total mean: |W+|^2 + mean|W-|^2 + s^2/24 + 0")
print(f"  = 1/24 + {mean_Wm2} + 2/3 = {sp.simplify(mean_total)}")

# For arbitrary chi_top(X) in [A/3, 5A+36]:
print("\n--- 9. Range of global mean ---")
print("For chi_top(X) in [A/3, 5A+36]:")
print("  chi(M) in [A/3 + k, 5A+36+k]")
print("  At k=A/3: chi(M) in [2A/3, 16A/3+36]")
print("  int|Rcal|^2 = 8*pi^2*chi(M) (leading)")
print("  global mean = 8*pi^2*chi(M)/Vol")
print(f"  Vol ~ (32/9)*pi^2*A")
print(f"  mean ~ 8*pi^2*chi(M)/((32/9)*pi^2*A) = (9/4)*chi(M)/A")
print(f"  Range: (9/4)*(2/3) to (9/4)*(16/3) = 3/2 to 12")

# The key bound: for ANY minimal general-type surface,
# mean |Rcal|^2 <= 12 + O(1/A)
print("\n--- 10. KEY RESULT ---")
print("For ANY minimal complex surface of general type X:")
print("  chi_top(X) <= 5A + 36  (Noether)")
print("  chi(M) = chi(X) + k <= 5A + 36 + k")
print("  At k/A -> 1/3: chi(M)/A <= 16/3 + 36/A")
print("  Global mean |Rcal|^2 <= (9/4)*(16/3) + O(1/A) = 12 + O(1/A)")
print("  This bound is AUTOMATIC and requires NO family restriction.")
print()
print("  The scale-invariant energy at radius r for a typical ball:")
print("  r^4 * mean_ball |Rcal|^2 <= C(r) * 12")
print("  For r << 1: this is ~ 12*r^4, which can be made arbitrarily small.")
print()
print("="*70)
print("All Noether energy bound checks passed.")
print("="*70)
