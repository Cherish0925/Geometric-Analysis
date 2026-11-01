#!/usr/bin/env python3
"""
Step 7 CORRECTED: Bochner formula with correct coefficients and 
Derdziński conformal factor analysis.

CORRECTIONS from TTCS verifier + S0910A03 msg #224:
- Bochner coefficients: (s/2, -6) not (s/3, -4)
- Derdziński factor: g_K = C|W+|^{2/3}g (uniquely determined)
"""
import sympy as sp

print("=" * 70)
print("CORRECTED BOCHNER + DERDZIŃSKI ANALYSIS")
print("=" * 70)

# --- Corrected Bochner formula ---
# (1/2)Δ|W+|² = |∇W+|² + (s/2)|W+|² - 6·tr(W+³)
# Equivalently (A03): Δ|W+|² = 2|∇W+|² + s|W+|² - 36·det(W+)
# where det(W+) = αβγ, tr(W+³) = 3αβγ

print("\n1. CORRECTED BOCHNER FORMULA")
print("   (1/2)Δ|W+|² = |∇W+|² + (s/2)|W+|² - 6·tr(W+³)")
print("-" * 50)

alpha, beta = sp.symbols('alpha beta', real=True)
gamma = -alpha - beta  # trace-free
trW3 = 3 * alpha * beta * gamma

# Check ℂℍ²: s=-4, eigenvalues (1/3, 1/3, -2/3)
a_ke, b_ke, g_ke = sp.Rational(1,3), sp.Rational(1,3), sp.Rational(-2,3)
W2_ke = a_ke**2 + b_ke**2 + g_ke**2
trW3_ke = 3 * a_ke * b_ke * g_ke

# CORRECTED coefficients: s/2, -6
bochner_ke = (sp.Integer(-4)/2) * W2_ke - 6 * trW3_ke
print(f"ℂℍ² check: (s/2)|W+|² - 6·tr(W+³) = {bochner_ke}")
assert bochner_ke == 0
print("  ✓ Parallel W+ verified")

# Check ℂP² (Fubini-Study): s=12, eigenvalues (2, -1, -1)
a_fs, b_fs, g_fs = sp.Integer(2), sp.Integer(-1), sp.Integer(-1)
W2_fs = a_fs**2 + b_fs**2 + g_fs**2
trW3_fs = 3 * a_fs * b_fs * g_fs
bochner_fs = (sp.Integer(12)/2) * W2_fs - 6 * trW3_fs
print(f"ℂP² check: (s/2)|W+|² - 6·tr(W+³) = {bochner_fs}")
assert bochner_fs == 0
print("  ✓ Parallel W+ verified")

# Calibrated target: s=-4, eigenvalues (1/12, 1/12, -1/6)
a_t, b_t, g_t = sp.Rational(1,12), sp.Rational(1,12), sp.Rational(-1,6)
W2_t = a_t**2 + b_t**2 + g_t**2
trW3_t = 3 * a_t * b_t * g_t
print(f"\nCalibrated target: eigenvalues ({g_t}, {a_t}, {b_t})")
print(f"  |W+|² = {W2_t}")
print(f"  tr(W+³) = {trW3_t}")

nabW2_corrected = -(sp.Integer(-4)/2) * W2_t + 6 * trW3_t
print(f"  |∇W+|² = -(s/2)|W+|² + 6·tr(W+³) = {nabW2_corrected}")
assert nabW2_corrected == sp.Rational(1, 16)
print(f"  = 1/16 (CORRECTED from earlier 1/24)")
print(f"  ✓ Consistent: |∇W+|² > 0, W+ not parallel")

# --- Key claim: Derdziński conformal factor ---
print("\n\n2. DERDZIŃSKI CONFORMAL FACTOR ANALYSIS")
print("-" * 50)
print("Derdziński's theorem: Einstein 4-manifold with two-eigenvalue W+")
print("→ locally conformally Kähler with UNIQUE conformal factor")
print("   g_K = C·|w|^{2/3}·g  where w = lowest eigenvalue of W+")
print()

w_val = sp.Rational(-1, 6)  # lowest eigenvalue at calibrated target
f_factor = abs(w_val)**sp.Rational(2,3)
print(f"At calibrated target: w = {w_val}")
print(f"  |w|^{{2/3}} = {sp.simplify(f_factor)}")
print(f"  Since w is CONSTANT, f = C·|w|^{{2/3}} is CONSTANT")
print(f"  → g_K = const·g → g is itself Kähler!")

print()
print("For Kähler-Einstein with Ric = -g (s = -4):")
ke_W2 = sp.Rational(2, 3)
print(f"  |W+|² = s²/24 = {sp.Rational(16,24)} = {ke_W2}")
print(f"  But calibrated |W+|² = {W2_t}")
print(f"  {ke_W2} ≠ {W2_t}: CONTRADICTION!")

# --- Tensor slack controls the two-eigenvalue passage ---
print("\n\n3. TENSOR SLACK → TWO-EIGENVALUE → LOCAL CONTRADICTION")
print("-" * 50)

# From LeBrun's proof:
# ∫((2/3)s - 2√(2/3)|W+|)² ≥ ∫((2/3)s + 2w)² ≥ 32π²(a+)²
# The tensor slack ξ = w + √(2/3)|W+| ≥ 0
# Near-equality forces ∫ξ = O(D_a) → 0 in A-normalized sense

xi = sp.Symbol('xi', nonneg=True)  # tensor slack
c = sp.sqrt(sp.Rational(2,3))

# At the calibrated target: ξ = w + √(2/3)|W+| = -1/6 + √(2/3)·1/(2√6)
xi_target = w_val + c * sp.sqrt(W2_t)
print(f"ξ = w + √(2/3)|W+| at target = {sp.simplify(xi_target)}")
assert sp.simplify(xi_target) == 0
print("  ✓ ξ = 0 at the two-eigenvalue target")

print()
print("Proof chain for the negative branch:")
print("  1. Near-equality: D_a/A → 0")
print("  2. Cauchy-Schwarz remainder: ∫(s+8√6|W+|)² ≤ 864π²D_a")
print("  3. Tensor slack integral: ∫ξ·(Q+P) ≤ 48π²D_a")
print("     where Q+P ≈ 6 at calibrated target")
print("  4. Volume-random basepoint: typical ball has ∫ξ → 0")
print("  5. Cheeger-Naber: noncollapsed ball has smooth Einstein limit")
print("  6. On smooth limit: ξ = 0 pointwise (from L¹ vanishing + C²)")
print("  7. ξ = 0 + |W+| = const → Derdziński factor = const → Kähler")
print("  8. Kähler + Ric = -g → |W+|² = 2/3 ≠ 1/24")
print("  9. CONTRADICTION on every noncollapsed smooth region!")
print()
print("Remaining gap: does a near-pinching sequence have to have")
print("noncollapsed regions? (collapse under Ric ≈ -g has no Myers bound)")

# --- Tensor slack estimate derivation ---
print("\n\n4. TENSOR SLACK ESTIMATE (detailed)")
print("-" * 50)

# From Step 5 algebraic identity:
# ∫(s-√6|W+|)² = 72π²(a+)² + R₁/8
# where R₁ = 864π²D_a - ∫(s+8√6|W+|)² ≥ 0
#
# The w-version of Thm 2.3:
# ∫((2/3)s + 2w)_-² ≥ 32π²(a+)²
#
# The |W+|-version:
# ∫((2/3)s - 2√(2/3)|W+|)² ≥ 32π²(a+)²
#
# Difference = ∫2ξ(Q+P) where ξ = w+√(2/3)|W+|
# and Q+P = -(4/3)s + 2√(2/3)|W+| - 2w ≥ 0
#
# Upper bound: ∫Q² ≤ (4/9)(72π²(a+)² + R₁/8) = 32π²(a+)² + R₁/18
# So: ∫2ξ(Q+P) = ∫Q² - ∫P² ≤ 32π²(a+)² + R₁/18 - 32π²(a+)² = R₁/18
# And R₁ ≤ 864π²D_a
# Therefore: ∫ξ(Q+P) ≤ R₁/36 ≤ 24π²D_a

print("∫ξ·(Q+P) ≤ R₁/36 ≤ 24π²·D_a")
print("Since Q+P → 6 on good regions:")
print("∫ξ ≤ 4π²·D_a (on good regions, approximately)")
print("With D_a/A → 0: ∫ξ/A → 0")
print()
print("Combined with volume-random basepoint:")
print("E[∫_{B_R(p)} ξ] ≤ C(R)/Vol · ∫ξ → 0")
print("So typical balls have ∫ξ → 0")
print()
print("On smooth Einstein limit (C² convergence):")
print("∫_{B_R} ξ_∞ = lim ∫ξ_i = 0, ξ_∞ ≥ 0 continuous")
print("Therefore ξ_∞ = 0 pointwise → TWO-EIGENVALUE W+ on limit")

print("\n\n5. SUMMARY OF CORRECTED CONCLUSIONS")
print("=" * 70)
print("CORRECTED (from initial Step 7 analysis):")
print("  1. Bochner coefficients: (s/2, -6) giving |∇W+|² = 1/16")
print("  2. Derdziński factor IS uniquely |w|^{1/3}, NOT arbitrary f")
print("  3. Constant |W+| + two-eigenvalue → f = const → LOCALLY KÄHLER")
print("  4. LOCAL CONTRADICTION: |W+|² = 1/24 ≠ 2/3 (Kähler-Einstein)")
print("  5. The argument IS local, NOT inherently global")
print()
print("CORRECTED STRUCTURAL PICTURE:")
print("  - Near-equality → tensor slack ξ → 0 in normalized L¹")
print("  - Noncollapsed smooth limit: ξ = 0 + |W+| = const → Kähler → ⊥")
print("  - Therefore: noncollapsed smooth regions CANNOT exist")
print("  - Remaining: must the sequence have noncollapsed regions?")
print()
print("  This is a STRONGER result than the initial (wrong) analysis.")
print("  The negative branch now needs only: show near-pinching sequences")
print("  cannot be ENTIRELY collapsed (no noncollapse at any scale).")
print()
print("All corrected checks passed.")
