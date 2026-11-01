"""
Mixed Seiberg-Witten bound analysis for Yau Problem 26 (negative branch).

This script verifies the improved quantitative bounds using LeBrun's 
Proposition 4 (mixed s^2+|W+|^2 estimate) instead of the scalar-only bound.

Key result: For LeBrun manifolds X#k CP̄² with A=c₁²(X) and k/A > 1/3:
  δ/(1-δ) ≥ √((k/A - 1/3)/2)
  
This gives a UNIFORM lower bound on δ depending only on k/A (not A separately).
"""

import numpy as np
from sympy import *

# ============================================================
# PART 1: Symbolic derivation of the mixed bound
# ============================================================

print("=" * 70)
print("MIXED SW BOUND ANALYSIS FOR YAU 26 (NEGATIVE BRANCH)")
print("=" * 70)

delta, p, A_sym = symbols('delta p A', positive=True, real=True)
k_sym = symbols('k', positive=True, real=True)

print("\n--- Setup ---")
print("M = X # k CP̄², A = c₁²(X), p = k/A")
print("Metric g with δ_-(g) = δ: Ric eigenvalues in (-(1+δ), -(1+δ))")
print("n = 4 (dimension)")

# Key identities for M = X # k CPbar^2:
# (2χ+3τ)(M) = c₁²(X) - k = A - k = A(1-p)
# α = c₁(X), α² = A
# Monopole class a = c₁(X) + Σ ε_j E_j, optimized: (a⁺)² ≥ A

print("\n--- Proposition 4 (LeBrun's mixed estimate) ---")
print("For monopole class a on M:")
print("  (1/4π²)∫(s²/24 + 2|W₊|²)dμ ≥ (2/3)(a⁺)²")
print("With optimized sign choice: (a⁺)² ≥ (α⁺)² ≥ α² = A")

print("\n--- Chern-Gauss-Bonnet ---")
print("  (2χ+3τ) = (1/4π²)∫(s²/24 + 2|W₊|² - |r̊|²/2)dμ")
print("  A - k = (1/4π²)∫(s²/24 + 2|W₊|² - |r̊|²/2)dμ")

print("\n--- Combining ---")
print("  (1/8π²)∫|r̊|²dμ ≥ (2A/3) - (A-k)/2 = k - A/3")
print("  Wait, let me redo: subtract CGB from SW mixed:")
print("  (1/4π²)∫(|r̊|²/2)dμ ≥ (2A/3) - (A-k)")
print("  = (2A/3) - A + k = k - A/3")

q_prime = k_sym - A_sym / 3
B = A_sym - k_sym

print(f"\n  Key quantity: q' = k - A/3")
print(f"  Nontrivial iff q' > 0, i.e., k > A/3 (= k/A > 1/3)")

print("\n--- Pointwise bound on traceless Ricci ---")
print("  |r̊|² = |Ric - (s/4)g|² ≤ |Ric - σg|² = |E|² ≤ 4δ²")
print("  (since |E|² = Σ e_i², |e_i| ≤ δ, and traceless part ≤ full)")
print("  Actually: |r̊|² = |E|² - (trE)²/4 ≤ |E|² ≤ 4δ²")

# Volume upper bound from CGB (using 2χ-3τ side):
# (2χ-3τ) = (1/4π²)∫(s²/24 + 2|W₋|² - |r̊|²/2)dμ
# Using s²/24 ≥ (2/3)(1-δ)² pointwise and |W₋|² ≥ 0:
# But simpler: from 2χ+3τ side:
# A-k = (1/4π²)∫(s²/24 + 2|W₊|² - |r̊|²/2)dμ
# Since s²/24 ≥ (16(1-δ)²/24) = 2(1-δ)²/3 pointwise:
# (A-k) ≥ (1/4π²)V(2(1-δ)²/3 - 2δ²) + (1/4π²)∫2|W₊|²dμ
# ≥ (1/4π²)V(2(1-δ)²/3 - 2δ²)

print("\n--- Volume upper bound ---")
print("  From CGB: A-k ≥ V/(4π²) · (2(1-δ)²/3 - 2δ²)")
print("  V ≤ 4π²(A-k) / (2(1-δ)²/3 - 2δ²)")

denom = Rational(2, 3) * (1 - delta)**2 - 2 * delta**2
V_upper = 4 * pi**2 * B / denom

# From the integral bound: (1/4π²)∫(|r̊|²/2) ≥ q' = k - A/3
# And |r̊|² ≤ 4δ²:
# (1/4π²) · (4δ²/2) · V ≥ k - A/3
# i.e., δ²V/(2π²) ≥ k - A/3
# i.e., V ≥ 2π²(k-A/3)/δ²

V_lower = 2 * pi**2 * q_prime / delta**2

print("\n--- Combining volume bounds ---")
print("  V ≥ 2π²(k-A/3)/δ²  AND  V ≤ 4π²(A-k)/(2(1-δ)²/3 - 2δ²)")

# Combining:
# 2π²(k-A/3)/δ² ≤ 4π²(A-k)/(2(1-δ)²/3 - 2δ²)
# (k-A/3)(2(1-δ)²/3 - 2δ²) ≤ 2δ²(A-k)
# Let q' = k-A/3, B = A-k
# q'(2(1-δ)²/3 - 2δ²) ≤ 2Bδ²

print("\n--- Deriving δ lower bound ---")
print("  q'(2(1-δ)²/3 - 2δ²) ≤ 2Bδ²")
print("  q'·2(1-δ)²/3 ≤ 2(B+q')δ² + 2q'δ²... wait, expanding:")
print("  q'·2(1-δ)² ≤ 6(B+q')δ²")
print("  Note: B + q' = (A-k) + (k-A/3) = 2A/3")
print("  So: q'·2(1-δ)² ≤ 6·(2A/3)·δ² = 4Aδ²")
print("  i.e., 2Aδ²/(1-δ)² ≥ q' = k - A/3")
print("  δ/(1-δ) ≥ √(q'/(2A)) = √((k/A - 1/3)/2)")

# Substituting p = k/A:
expr = sqrt((p - Rational(1, 3)) / 2)
print(f"\n  FINAL RESULT: δ/(1-δ) ≥ √((p-1/3)/2) where p = k/A")
print(f"  Equivalently: δ ≥ √((p-1/3)/2) / (1 + √((p-1/3)/2))")

# ============================================================
# PART 2: Numerical verification at key points
# ============================================================

print("\n" + "=" * 70)
print("NUMERICAL VERIFICATION")
print("=" * 70)

def delta_bound_mixed(p_val):
    """Lower bound on δ from mixed SW bound, function of p = k/A only."""
    if p_val <= 1/3:
        return 0.0
    t = np.sqrt((p_val - 1/3) / 2)
    return t / (1 + t)

def delta_bound_scalar_only(p_val, A_val):
    """Old lower bound from scalar-only SW bound, depends on A."""
    if p_val <= 2/3:
        return 0.0
    q = A_val * (p_val - 2/3)
    return np.sqrt(q) / (np.sqrt(A_val) + np.sqrt(q))

print("\n--- Comparison: Mixed vs Scalar-only bounds ---")
print(f"{'p=k/A':>8} {'A':>8} {'δ(mixed)':>12} {'δ(scalar)':>12} {'Ratio':>8}")
print("-" * 52)

for p_val in [0.34, 0.4, 0.5, 0.6, 2/3, 0.7, 0.8, 0.9]:
    for A_val in [100, 1000, 10000]:
        dm = delta_bound_mixed(p_val)
        ds = delta_bound_scalar_only(p_val, A_val)
        ratio = dm / ds if ds > 0 else float('inf')
        print(f"{p_val:8.3f} {A_val:8d} {dm:12.6f} {ds:12.6f} {ratio:8.2f}")

print("\n--- KEY VALUES ---")
print(f"At p=2/3: δ_mixed ≥ {delta_bound_mixed(2/3):.6f} = 1/(1+√6) = {1/(1+np.sqrt(6)):.6f}")
print(f"  Compare: 1/(1+√6) = (√6-1)/5 = {(np.sqrt(6)-1)/5:.6f}")

# Verify symbolically
t_23 = sqrt(Rational(1, 6))
delta_23 = t_23 / (1 + t_23)
print(f"  Symbolic: δ ≥ √(1/6)/(1+√(1/6)) = 1/(√6+1) = (√6-1)/5 = {float(delta_23):.6f}")

print(f"\nAt p=1/2: δ_mixed ≥ {delta_bound_mixed(0.5):.6f}")
print(f"At p=1/3+0.01: δ_mixed ≥ {delta_bound_mixed(1/3+0.01):.6f}")
print(f"At p=1/3+0.001: δ_mixed ≥ {delta_bound_mixed(1/3+0.001):.6f}")

# ============================================================
# PART 3: Verify the algebra symbolically
# ============================================================

print("\n" + "=" * 70)
print("SYMBOLIC VERIFICATION")
print("=" * 70)

# Variables
d, p_s, A_s = symbols('d p A', positive=True)

# The inequality to verify:
# q'(2(1-d)^2/3 - 2d^2) ≤ 2B*d^2
# where q' = A(p-1/3), B = A(1-p)
q_p = A_s * (p_s - Rational(1, 3))
B_s = A_s * (1 - p_s)

lhs = q_p * (Rational(2, 3) * (1 - d)**2 - 2 * d**2)
rhs = 2 * B_s * d**2

# The condition is lhs ≤ rhs, i.e., rhs - lhs ≥ 0
diff_expr = expand(rhs - lhs)
print(f"\nrhs - lhs = {diff_expr}")

# Factor out A
diff_over_A = simplify(diff_expr / A_s)
print(f"(rhs - lhs)/A = {diff_over_A}")

# Substitute d = t/(1+t) where t = √((p-1/3)/2)
t = symbols('t', positive=True)
d_sub = t / (1 + t)
diff_at_boundary = diff_over_A.subs(d, d_sub)
diff_simplified = simplify(diff_at_boundary)
print(f"\nAt δ = t/(1+t): (rhs-lhs)/A = {diff_simplified}")

# At the critical point t = √((p-1/3)/2), this should be exactly 0
t_crit = sqrt((p_s - Rational(1, 3)) / 2)
check = diff_simplified.subs(t, t_crit)
check_simplified = simplify(check)
print(f"At t = √((p-1/3)/2): {check_simplified}")
print(f"  (Should be 0: boundary is tight)")

# ============================================================
# PART 4: Compare with old scalar-only bound
# ============================================================

print("\n" + "=" * 70)
print("COMPARISON WITH OLD SCALAR-ONLY BOUND")
print("=" * 70)

print("\nOLD (scalar-only): No Einstein iff k > 2A/3")
print("  δ/(1-δ) ≥ √(q/(3B)) where q = k-2A/3, B = A-k")
print("  For fixed p=k/A > 2/3: δ ~ √((p-2/3)/(3(1-p)))/√A → 0")
print("  DEPENDS ON A! Not uniform.")

print("\nNEW (mixed SW): No Einstein iff k > A/3")
print("  δ/(1-δ) ≥ √((p-1/3)/2)")
print("  For fixed p=k/A > 1/3: δ ≥ f(p) > 0")
print("  INDEPENDENT OF A! Uniform.")

print("\n--- Implications for Yau 26 negative branch ---")
print("1. For k/A ≥ 2/3: δ ≥ 1/(√6+1) ≈ 0.290 UNIFORMLY")
print("   The old analysis said δ ~ 1/√A → 0. THIS IS NOW EXCLUDED.")
print("2. For 1/3 < k/A < 2/3: NEW no-Einstein range, δ ≥ f(k/A) > 0")
print("3. Only at k/A → 1/3: δ → 0 (boundary of no-Einstein region)")
print("4. At k/A ≤ 1/3: Mixed bound does NOT exclude Einstein metrics")

print("\n--- What this means ---")
print("The naive 'varying manifold' counterexample route (take A→∞ with")
print("fixed k/A > 2/3) is KILLED by the mixed bound.")
print("The only surviving possibility is k/A → 1/3 from above,")
print("where the manifold approaches the Einstein-existence boundary.")

# ============================================================  
# PART 5: S0910A02's basic class square question
# ============================================================

print("\n" + "=" * 70)
print("BASIC CLASS SQUARE ANALYSIS (responding to S0910A02)")
print("=" * 70)

print("\nMonopole class: a = c₁(X) + Σ εⱼ Eⱼ")
print("Topological square: a² = c₁²(X) + Σ Eⱼ² = A - k")
print("  (since c₁(X)·Eⱼ = 0 and Eⱼ² = -1)")
print("  S0910A02 is CORRECT: a² = A - k for ALL basic classes")
print()
print("Self-dual projection square: (a⁺)² ≥ a² (since (a⁻)² ≤ 0)")
print("  With Ishida-LeBrun sign trick: (a⁺)² ≥ (α⁺)² ≥ α² = A")
print("  (where α = c₁(X), using Ê_j·α⁺ ≥ 0)")
print()
print("RECONCILIATION:")
print("  a² = A-k (topological, can be negative)")
print("  (a⁺)² ≥ A (self-dual projection, metric-dependent)")  
print("  Both correct. Prop 4 uses (a⁺)², not a².")
print("  The difference (a⁺)² - a² = -(a⁻)² ≥ k (from E_j contributions)")
print()
print("S0910A02's concern about a²=A-k is valid but doesn't weaken the bound")
print("because the SW estimate uses (a⁺)², which is LARGER.")

# ============================================================
# PART 6: Topology correction (Strategist's note)
# ============================================================

print("\n" + "=" * 70)
print("TOPOLOGY CORRECTIONS")
print("=" * 70)

print("\n#_m CP²: χ = m+1 (each CP² has χ=3, gluing removes 2 per summand)")
print("  Wait: χ(#_m CP²) = mχ(CP²) - (m-1)χ(S⁴) = 3m - (m-1)·2 = m+2")
print("  τ(#_m CP²) = m")
print("  2χ - 3|τ| = 2(m+2) - 3m = 4-m")
print("  HT violated iff 4-m < 0, i.e., m ≥ 5")
print("  m=3: 2χ-3|τ| = 1 > 0 (HT SATISFIED, NOT violated!)")
print("  m=4: 2χ-3|τ| = 0 (HT equality)")
print("  m=5: 2χ-3|τ| = -1 < 0 (HT violated)")
print()
print("Correction: The prior note had '2-m' instead of '4-m'")
print("This means #_3 CP² satisfies strict HT and is NOT excluded by HT!")
print("However, #_3 CP² = CP²#CP²#CP² is simply connected with b₊=3.")
print("Does it admit an Einstein metric? This is an open question.")

# ============================================================
# PART 7: Summary of δ bounds across all no-Einstein families
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY: δ LOWER BOUNDS FOR ALL KNOWN NO-EINSTEIN 4-MANIFOLDS")
print("=" * 70)

print("\nPositive branch (σ = +1):")
print("  - LeBrun manifolds: δ₊ ≥ 1 (no positive scalar curvature)")
print("  - HT violators (#_m CP², m≥5): δ₊ ≥ 1/(1+√3) ≈ 0.366")
print("  - #_3 CP²: HT satisfied! δ₊ bound needs separate analysis")
print()
print("Negative branch (σ = -1), MIXED SW bound:")
print("  - LeBrun X#k CPbar², k/A ≥ 2/3: δ₋ ≥ 1/(√6+1) ≈ 0.290 UNIFORM")
print("  - LeBrun X#k CPbar², 1/3 < k/A < 2/3: δ₋ ≥ f(k/A) > 0 UNIFORM")
print("  - As k/A → 1/3⁺: δ₋ → 0 (boundary)")
print("  - Ishida-LeBrun X#Y#k CPbar²: similar but with Σc₁² replacing A")
print()
print("CRITICAL CHANGE: The mixed bound eliminates the 'δ→0 with A→∞'")
print("route that was the main counterexample hope in Step 2.")
print("The only remaining δ→0 possibility requires k/A→1/3,")
print("i.e., approaching the Einstein-existence boundary.")
