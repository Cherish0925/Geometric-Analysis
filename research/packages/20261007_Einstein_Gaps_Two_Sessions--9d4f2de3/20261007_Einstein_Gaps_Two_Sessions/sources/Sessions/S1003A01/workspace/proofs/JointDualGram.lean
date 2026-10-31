import Mathlib

namespace JointDualGram

/-- Scalar square completion underlying the dual calibration inequality. -/
theorem qiushi_scalar_dual (x y : ℝ) : 2 * x * y - y^2 ≤ x^2 := by
  nlinarith [sq_nonneg (x - y)]

/-- Two orthogonal channels are combined before estimating, so neither is counted twice. -/
theorem qiushi_two_channel_dual (x₁ x₂ y₁ y₂ : ℝ) :
    (2 * x₁ * y₁ - y₁^2) + (2 * x₂ * y₂ - y₂^2) ≤ x₁^2 + x₂^2 := by
  nlinarith [sq_nonneg (x₁ - y₁), sq_nonneg (x₂ - y₂)]

/-- The optimized scalar coefficient: for positive `g`, the dual quadratic is bounded by
`m²/g`, with equality at `c=m/g`.  Finite Gram optimization is this identity after
orthogonalizing the positive Gram matrix. -/
theorem qiushi_gram_eigenchannel (g m c : ℝ) (hg : 0 < g) :
    2 * m * c - g * c^2 ≤ m^2 / g := by
  have hs : 0 ≤ (m - g * c)^2 := sq_nonneg (m - g * c)
  field_simp
  nlinarith

end JointDualGram
