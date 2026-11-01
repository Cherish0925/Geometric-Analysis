import Mathlib

/-!
# Step 29 local twist-spike algebra kernel

This file formalizes only the elementary algebra in the Step 29 local jet test.
It does not formalize Riemannian geometry, Kaluza--Klein formulas, or any global
Yau-26 statement.

The symbolic computation for the local metric jet produced Ricci components at
the origin

  Ric_x = -(2H + S + 6pa + 2pc)/2,
  Ric_z = -H - 2pa - 2pc,
  Ric_theta = -(6H - S)/2,

where S=B^2 is the square of the connection-curvature spike, H is the dilaton
Hessian parameter, and pa, pc are base conformal 2-jet parameters.  The solution
below shows that these equations can equal an arbitrary target Lambda with S a
free parameter.  This machine-checks the algebraic core of the claim that a
pointwise horizontal-twist bound cannot be read off from the local Ricci equations
alone.
-/

namespace Yau26Step29

noncomputable section

variable (Λ S : ℝ)

/-- Dilaton Hessian parameter solving the vertical Ricci equation. -/
def Hsol : ℝ := (S - 2 * Λ) / 6

/-- Base 2-jet parameter in the two twist-plane directions. -/
def pasol : ℝ := - (4 * Λ + 7 * S) / 24

/-- Base 2-jet parameter in the transverse base direction. -/
def pcsol : ℝ := (5 * S - 4 * Λ) / 24

/-- Ricci component in the two twist-plane base directions. -/
def RicPlane (H pa pc S : ℝ) : ℝ := - (2 * H + S + 6 * pa + 2 * pc) / 2

/-- Ricci component in the transverse base direction. -/
def RicTransverse (H pa pc : ℝ) : ℝ := - H - 2 * pa - 2 * pc

/-- Ricci component in the circle fibre direction. -/
def RicCircle (H S : ℝ) : ℝ := - (6 * H - S) / 2

/-- The plane Ricci component is exactly the target value for arbitrary S. -/
theorem RicPlane_sol :
    RicPlane (Hsol Λ S) (pasol Λ S) (pcsol Λ S) S = Λ := by
  unfold RicPlane Hsol pasol pcsol
  ring

/-- The transverse base Ricci component is exactly the target value for arbitrary S. -/
theorem RicTransverse_sol :
    RicTransverse (Hsol Λ S) (pasol Λ S) (pcsol Λ S) = Λ := by
  unfold RicTransverse Hsol pasol pcsol
  ring

/-- The circle Ricci component is exactly the target value for arbitrary S. -/
theorem RicCircle_sol : RicCircle (Hsol Λ S) S = Λ := by
  unfold RicCircle Hsol
  ring

/-- The three component identities as one conjunction. -/
theorem all_Ricci_components_solved :
    RicPlane (Hsol Λ S) (pasol Λ S) (pcsol Λ S) S = Λ ∧
    RicTransverse (Hsol Λ S) (pasol Λ S) (pcsol Λ S) = Λ ∧
    RicCircle (Hsol Λ S) S = Λ := by
  exact ⟨RicPlane_sol Λ S, RicTransverse_sol Λ S, RicCircle_sol Λ S⟩

/-- If the twist square S dominates 2Λ, the required dilaton Hessian is positive. -/
theorem Hsol_pos_of_twist_large (h : 2 * Λ < S) : 0 < Hsol Λ S := by
  unfold Hsol
  nlinarith

/-- Frobenius norm square of the noncentral H3 Lie-derivative matrix. -/
def noncentralLieDerivativeNormSq (β : ℝ) : ℝ := 2 * β ^ 2

/-- The noncentral almost-Killing error has the same quadratic scale as the bracket. -/
theorem noncentral_error_same_scale (β : ℝ) :
    noncentralLieDerivativeNormSq β = 2 * β ^ 2 := by
  rfl

/-- Noncentral H3 directions have nonzero Lie-derivative error whenever the bracket is nonzero. -/
theorem noncentral_error_pos_of_bracket_ne_zero {β : ℝ} (hβ : β ≠ 0) :
    0 < noncentralLieDerivativeNormSq β := by
  unfold noncentralLieDerivativeNormSq
  nlinarith [sq_pos_of_ne_zero hβ]

end

end Yau26Step29
