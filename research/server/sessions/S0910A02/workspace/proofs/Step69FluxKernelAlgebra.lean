import Mathlib

/-!
# Step 69 algebraic kernels for the Yau--26 A1 log-flux review

This file formalizes only the small algebraic cores used in Step 69:

* the four-dimensional clean-annulus flux coefficient from `FND:flux`;
* the two sharp spherical-model constants `1/8` and `1/6` from the manuscript;
* the scalar `l=1` reduction in the `S^2 x S^2` kernel audit, under the
  geometric input `Hess f = -Λ f g` already checked outside Lean;
* the Ozuch-convention sign for a parallel relative product tensor.

It does **not** formalize differential geometry, Ricci linearization, Ozuch's
operator, or the full Yau--26 proposition.  Those remain mathematical inputs to
be formalized only after the analytic statements are stabilized.
-/

namespace Yau26Step69

/-- In dimension four, the clean log-annulus flux coefficient is `-3` when
`∫ eta'' = 0` and `∫ eta' = 1`. -/
theorem fluxCoeff4 :
    -((1 : ℚ) / 2) * ((0 : ℚ) + 6 * (1 : ℚ)) = -3 := by
  norm_num

/-- The general symbolic coefficient `-(n+2)/2` specializes to `-3` at `n=4`. -/
theorem generalFluxCoeffAt4 : -(((4 : ℚ) + 2) / 2) = -3 := by
  norm_num

/-- With `I_K = v/216` and `J_K = v/9`, the linear lower-bound constant is `1/8`. -/
theorem sphericalUnconstrainedConstant (v : ℚ) (hv : v ≠ 0) :
    (3 * (v / 216)) / (v / 9) = (1 : ℚ) / 8 := by
  field_simp [hv]
  ring

/-- With numerator `v/72` and denominator `v/12`, the constant-scalar sharp
constant is `1/6`. -/
theorem sphericalConstantScalarConstant (v : ℚ) (hv : v ≠ 0) :
    (v / 72) / (v / 12) = (1 : ℚ) / 6 := by
  field_simp [hv]
  ring

/-- For the manuscript's spherical model spectrum
`(0,-σ/18,σ/36,σ/36)`, after taking absolute values the Hilbert--Schmidt
square per unit volume is `1/216`. -/
theorem sphericalHSSquare :
    (0 : ℚ)^2 + ((1 : ℚ) / 18)^2 + ((1 : ℚ) / 36)^2 + ((1 : ℚ) / 36)^2
      = (1 : ℚ) / 216 := by
  norm_num

/-- For the same model the nuclear norm per unit volume is `1/9`. -/
theorem sphericalNuclearNorm :
    (0 : ℚ) + (1 : ℚ) / 18 + (1 : ℚ) / 36 + (1 : ℚ) / 36 = (1 : ℚ) / 9 := by
  norm_num

/-- Algebraic core of the direct `S^2 x S^2` scalar-sector TT audit.

For a first spherical harmonic on the first `S^2`, the geometric identity
`Hess f = -Λ f g_1` reduces
`A f g_1 + B f g_2 + C Hess f` to
`(A - CΛ) f g_1 + B f g_2`.  The TT conditions are represented here as
`A - CΛ = 0` (divergence-free) and `(A - CΛ) + B = 0` (trace-free).  They force
both reduced coefficients to vanish. -/
theorem scalarSectorTTCoefficientsZero {A B C Λ : ℝ}
    (hdiv : A - C * Λ = 0) (htrace : (A - C * Λ) + B = 0) :
    (A - C * Λ = 0) ∧ B = 0 := by
  constructor
  · exact hdiv
  · nlinarith

/-- The same scalar-sector statement phrased with named reduced coefficients. -/
theorem scalarSectorReducedZero {H1 H2 : ℝ}
    (hdiv : H1 = 0) (htrace : H1 + H2 = 0) : H1 = 0 ∧ H2 = 0 := by
  constructor
  · exact hdiv
  · nlinarith

/-- Algebraic sign convention for a parallel relative product tensor in Ozuch's
operator: if the rough term is zero and `R° h = Λ h`, then
`P h = 1/2*0 - Λ h = -Λ h`. -/
theorem ozuchParallelRelativeMode (Λ h : ℝ) :
    ((1 : ℝ) / 2) * 0 - Λ * h = -Λ * h := by
  ring

/-- One audit target collecting the rational constants and two algebraic kernels
formalized in this file. -/
theorem auditedCore :
    (-((1 : ℚ) / 2) * ((0 : ℚ) + 6 * (1 : ℚ)) = -3) ∧
    (-(((4 : ℚ) + 2) / 2) = -3) ∧
    ((3 * ((1 : ℚ) / 216)) / ((1 : ℚ) / 9) = (1 : ℚ) / 8) ∧
    (((1 : ℚ) / 72) / ((1 : ℚ) / 12) = (1 : ℚ) / 6) ∧
    ((0 : ℚ)^2 + ((1 : ℚ) / 18)^2 + ((1 : ℚ) / 36)^2 + ((1 : ℚ) / 36)^2
      = (1 : ℚ) / 216) ∧
    ((0 : ℚ) + (1 : ℚ) / 18 + (1 : ℚ) / 36 + (1 : ℚ) / 36 = (1 : ℚ) / 9) ∧
    (∀ {H1 H2 : ℝ}, H1 = 0 → H1 + H2 = 0 → H1 = 0 ∧ H2 = 0) ∧
    (∀ Λ h : ℝ, ((1 : ℝ) / 2) * 0 - Λ * h = -Λ * h) := by
  constructor
  · exact fluxCoeff4
  constructor
  · exact generalFluxCoeffAt4
  constructor
  · simpa using (sphericalUnconstrainedConstant (1 : ℚ) (by norm_num))
  constructor
  · simpa using (sphericalConstantScalarConstant (1 : ℚ) (by norm_num))
  constructor
  · exact sphericalHSSquare
  constructor
  · exact sphericalNuclearNorm
  constructor
  · intro H1 H2 hdiv htrace
    exact scalarSectorReducedZero hdiv htrace
  · intro Λ h
    exact ozuchParallelRelativeMode Λ h

end Yau26Step69
