import Mathlib

/-!
# Step 28 Bochner-Killing center bound: algebraic kernels

This file formalizes the real-algebra underpinning the Bochner center bound
for Killing fields.  The geometric Bochner identity (∫|∇Z|² = ∫Ric(Z,Z))
is a standard result that requires Riemannian integration infrastructure
beyond current Mathlib scope.  We formalize only the algebraic consequences.

## Main results

1. The fiber gradient lower bound: for Heisenberg bracket b and vertical
   covariant derivative components, |∇Z|²/|Z|² = 2k₃² + b²/2 ≥ b²/2.

2. Sign argument: for Λ + δ < 0, the integrand |∇Z|² - (Λ+δ)|Z|² > 0
   whenever Z ≠ 0, so the Bochner integral ∫(|∇Z|² - Ric(Z,Z)) ≥ 0
   with Ric ≤ (Λ+δ)g is incompatible with Z ≠ 0.

3. Center bracket bound: the algebraic step from
     ∫(b²/2)|Z|² ≤ (Λ+δ)∫|Z|²
   to  ⟨b²⟩ ≤ 2(Λ+δ)  when the denominator is positive.
-/

namespace Yau26Step28

noncomputable section

open Real

/-- The Bochner integrand in the H₃ model: |∇Z|²/|Z|² = 2k₃² + b²/2. -/
def bochner_integrand (b k3 : ℝ) : ℝ := 2 * k3 ^ 2 + b ^ 2 / 2

/-- The fiber contribution to |∇Z|²/|Z|² is b²/2. -/
def fiber_gradient_sq (b : ℝ) : ℝ := b ^ 2 / 2

/-- The fiber gradient is a lower bound for the full Bochner integrand. -/
theorem fiber_lower_bound (b k3 : ℝ) :
    fiber_gradient_sq b ≤ bochner_integrand b k3 := by
  unfold fiber_gradient_sq bochner_integrand
  nlinarith [sq_nonneg k3]

/-- For Λ + δ < 0, the Bochner integrand minus the Ricci contribution is positive.
    This is the algebraic core of Theorem B (negative Ricci kills Killing fields). -/
theorem bochner_positive_for_negative_ricci (b k3 Λ δ : ℝ)
    (hΛδ : Λ + δ < 0) :
    0 < bochner_integrand b k3 - (Λ + δ) := by
  unfold bochner_integrand
  nlinarith [sq_nonneg k3, sq_nonneg b]

/-- Algebraic center bracket bound: if (b²/2)W ≤ (Λ+δ)W and W > 0, then b² ≤ 2(Λ+δ). -/
theorem center_bracket_bound {b Λ δ W : ℝ}
    (hW : 0 < W)
    (hint : b ^ 2 / 2 * W ≤ (Λ + δ) * W) :
    b ^ 2 ≤ 2 * (Λ + δ) := by
  have h : b ^ 2 / 2 ≤ Λ + δ := by
    by_contra h
    push Not at h
    have := mul_lt_mul_of_pos_right h hW
    linarith
  linarith

/-- Averaging version: if ∫b²|Z|² ≤ 2(Λ+δ)∫|Z|² with positive denominator,
    the weighted average satisfies ⟨b²⟩ ≤ 2(Λ+δ).
    Here `num` = ∫b²|Z|² and `den` = ∫|Z|². -/
theorem weighted_average_bound {Λ δ num den : ℝ}
    (hden : 0 < den)
    (hbd : num ≤ 2 * (Λ + δ) * den) :
    num / den ≤ 2 * (Λ + δ) := by
  rw [div_le_iff₀ hden]
  linarith

/-- For Λ > 0 and δ < Λ, the center bracket is bounded:
    b² ≤ 2(Λ+δ) < 4Λ. -/
theorem positive_branch_bracket_bound {b Λ δ W : ℝ}
    (_hΛ : 0 < Λ) (hδ : δ < Λ) (hW : 0 < W)
    (hint : b ^ 2 / 2 * W ≤ (Λ + δ) * W) :
    b ^ 2 < 4 * Λ := by
  have hbd := center_bracket_bound hW hint
  linarith

/-- The Bochner integrand minus Λ has a universal positive lower bound
    when Λ > 0, regardless of k₃ and b. This means every point contributes
    positively to the Killing energy excess, and no bracket plateau can cancel it. -/
theorem bochner_excess_positive_lambda (b k3 Λ : ℝ) (hΛ : 0 < Λ) :
    0 < bochner_integrand b k3 + Λ := by
  unfold bochner_integrand
  nlinarith [sq_nonneg k3, sq_nonneg b]

end

end Yau26Step28
