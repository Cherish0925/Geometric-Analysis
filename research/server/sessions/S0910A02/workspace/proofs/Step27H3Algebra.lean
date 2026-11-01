import Mathlib

/-!
# Step 27 H3 cohomogeneity-one algebra kernels

This file formalizes the real-algebra part of the Step 26--27 Heisenberg
cohomogeneity-one audit.  It does **not** formalize Ricci geometry; the link
from the geometric model to these variables is supplied by the separately
checked moving-frame computation.

Variables:
* `Λ` is the Einstein constant.
* `b` is the orthonormal Heisenberg bracket size.
* `k1 = a'/a`, `k3 = c'/c`.
* `C Λ b k1 k3 = 0` is the Hamiltonian constraint obtained from Ric00=Λ after
  imposing the three vertical Ricci equations.
-/

namespace Yau26Step27

noncomputable section

open Real

/-- Hamiltonian constraint expression for the diagonal H3 model. -/
def C (Λ b k1 k3 : ℝ) : ℝ := b ^ 2 + 4 * k1 ^ 2 + 8 * k1 * k3 + 4 * Λ

/-- The derivative-free part `S = C - 4Λ`. -/
def S (b k1 k3 : ℝ) : ℝ := b ^ 2 + 4 * k1 ^ 2 + 8 * k1 * k3

/-- Squared norm of the diagonal shape operator in the H3 model. -/
def T2 (k1 k3 : ℝ) : ℝ := 2 * k1 ^ 2 + k3 ^ 2

/-- Relative logarithmic bracket derivative `(log b)' = k3 - 2k1`. -/
def rate (k1 k3 : ℝ) : ℝ := k3 - 2 * k1

/-- Algebraic identity behind the lower bound on the shape operator. -/
theorem T_identity (Λ b k1 k3 : ℝ) :
    2 * T2 k1 k3 - (b ^ 2 + 4 * Λ) =
      2 * (2 * k1 + k3) ^ 2 - C Λ b k1 k3 := by
  unfold T2 C
  ring

/-- Algebraic identity behind the lower bound on the relative bracket rate. -/
theorem rate_identity (Λ b k1 k3 : ℝ) :
    4 * (rate k1 k3) ^ 2 - 5 * (b ^ 2 + 4 * Λ) =
      4 * (3 * k1 + k3) ^ 2 - 5 * C Λ b k1 k3 := by
  unfold rate C
  ring

/-- On the exact Einstein constraint surface, `|T|^2 >= (b^2+4Λ)/2`. -/
theorem T_lower_on_constraint {Λ b k1 k3 : ℝ} (hC : C Λ b k1 k3 = 0) :
    b ^ 2 + 4 * Λ ≤ 2 * T2 k1 k3 := by
  have hid := T_identity Λ b k1 k3
  have hdiff : 2 * T2 k1 k3 - (b ^ 2 + 4 * Λ) = 2 * (2 * k1 + k3) ^ 2 := by
    rw [hid, hC]
    ring
  have hs : 0 ≤ 2 * (2 * k1 + k3) ^ 2 := by
    nlinarith [sq_nonneg (2 * k1 + k3)]
  have hnonneg : 0 ≤ 2 * T2 k1 k3 - (b ^ 2 + 4 * Λ) := by
    rw [hdiff]
    exact hs
  linarith

/-- On the exact Einstein constraint surface, `((log b)')^2 >= 5/4 (b^2+4Λ)`. -/
theorem rate_lower_on_constraint {Λ b k1 k3 : ℝ} (hC : C Λ b k1 k3 = 0) :
    5 * (b ^ 2 + 4 * Λ) ≤ 4 * (rate k1 k3) ^ 2 := by
  have hid := rate_identity Λ b k1 k3
  have hdiff :
      4 * (rate k1 k3) ^ 2 - 5 * (b ^ 2 + 4 * Λ) =
        4 * (3 * k1 + k3) ^ 2 := by
    rw [hid, hC]
    ring
  have hs : 0 ≤ 4 * (3 * k1 + k3) ^ 2 := by
    nlinarith [sq_nonneg (3 * k1 + k3)]
  have hnonneg : 0 ≤ 4 * (rate k1 k3) ^ 2 - 5 * (b ^ 2 + 4 * Λ) := by
    rw [hdiff]
    exact hs
  linarith

/-- For positive Einstein constant, the relative bracket rate cannot vanish. -/
theorem rate_ne_zero_on_positive_constraint {Λ b k1 k3 : ℝ}
    (hC : C Λ b k1 k3 = 0) (hΛ : 0 < Λ) :
    rate k1 k3 ≠ 0 := by
  have hrate := rate_lower_on_constraint (Λ := Λ) (b := b) (k1 := k1) (k3 := k3) hC
  have hpos : 0 < 5 * (b ^ 2 + 4 * Λ) := by
    nlinarith [sq_nonneg b, hΛ]
  intro hz
  have hzero : 4 * (rate k1 k3) ^ 2 = 0 := by
    rw [hz]
    ring
  nlinarith

/-- If Ricci components are `δ`-pinched around `Λ`, the eliminated `S` is bounded. -/
theorem S_bound_from_rho_bounds {Λ δ ρ0 ρ1 ρ3 b k1 k3 : ℝ}
    (h0 : ρ0 ≤ Λ + δ) (h1 : Λ - δ ≤ ρ1) (h3 : Λ - δ ≤ ρ3)
    (hS : S b k1 k3 = 2 * ρ0 - 4 * ρ1 - 2 * ρ3) :
    S b k1 k3 ≤ -4 * Λ + 8 * δ := by
  rw [hS]
  nlinarith

/-- Pinched version of the `T` lower bound, assuming the eliminated `S` bound. -/
theorem T_lower_pinched_from_S_bound {Λ δ b k1 k3 : ℝ}
    (hS : S b k1 k3 ≤ -4 * Λ + 8 * δ) :
    b ^ 2 + 4 * Λ - 8 * δ ≤ 2 * T2 k1 k3 := by
  unfold S at hS
  unfold T2
  nlinarith [hS, sq_nonneg (2 * k1 + k3)]

/-- Pinched version of the relative-rate lower bound, assuming the eliminated `S` bound. -/
theorem rate_lower_pinched_from_S_bound {Λ δ b k1 k3 : ℝ}
    (hS : S b k1 k3 ≤ -4 * Λ + 8 * δ) :
    5 * (b ^ 2 + 4 * Λ - 8 * δ) ≤ 4 * (rate k1 k3) ^ 2 := by
  unfold S at hS
  unfold rate
  nlinarith [hS, sq_nonneg (3 * k1 + k3)]

/-- Combined pinched lower bound on the shape operator from component bounds. -/
theorem T_lower_pinched_from_rho_bounds {Λ δ ρ0 ρ1 ρ3 b k1 k3 : ℝ}
    (h0 : ρ0 ≤ Λ + δ) (h1 : Λ - δ ≤ ρ1) (h3 : Λ - δ ≤ ρ3)
    (hrel : S b k1 k3 = 2 * ρ0 - 4 * ρ1 - 2 * ρ3) :
    b ^ 2 + 4 * Λ - 8 * δ ≤ 2 * T2 k1 k3 := by
  exact T_lower_pinched_from_S_bound
    (S_bound_from_rho_bounds h0 h1 h3 hrel)

/-- Combined pinched lower bound on the relative bracket rate from component bounds. -/
theorem rate_lower_pinched_from_rho_bounds {Λ δ ρ0 ρ1 ρ3 b k1 k3 : ℝ}
    (h0 : ρ0 ≤ Λ + δ) (h1 : Λ - δ ≤ ρ1) (h3 : Λ - δ ≤ ρ3)
    (hrel : S b k1 k3 = 2 * ρ0 - 4 * ρ1 - 2 * ρ3) :
    5 * (b ^ 2 + 4 * Λ - 8 * δ) ≤ 4 * (rate k1 k3) ^ 2 := by
  exact rate_lower_pinched_from_S_bound
    (S_bound_from_rho_bounds h0 h1 h3 hrel)

/-- Combined pinched lower bounds on both the shape operator and relative bracket rate. -/
theorem both_lower_pinched_from_rho_bounds {Λ δ ρ0 ρ1 ρ3 b k1 k3 : ℝ}
    (h0 : ρ0 ≤ Λ + δ) (h1 : Λ - δ ≤ ρ1) (h3 : Λ - δ ≤ ρ3)
    (hrel : S b k1 k3 = 2 * ρ0 - 4 * ρ1 - 2 * ρ3) :
    (b ^ 2 + 4 * Λ - 8 * δ ≤ 2 * T2 k1 k3) ∧
      (5 * (b ^ 2 + 4 * Λ - 8 * δ) ≤ 4 * (rate k1 k3) ^ 2) := by
  exact ⟨T_lower_pinched_from_rho_bounds h0 h1 h3 hrel,
    rate_lower_pinched_from_rho_bounds h0 h1 h3 hrel⟩

/-- In the pinched positive regime `Λ > 2δ`, the relative bracket rate cannot vanish. -/
theorem rate_ne_zero_pinched_from_rho_bounds {Λ δ ρ0 ρ1 ρ3 b k1 k3 : ℝ}
    (hΛδ : 2 * δ < Λ)
    (h0 : ρ0 ≤ Λ + δ) (h1 : Λ - δ ≤ ρ1) (h3 : Λ - δ ≤ ρ3)
    (hrel : S b k1 k3 = 2 * ρ0 - 4 * ρ1 - 2 * ρ3) :
    rate k1 k3 ≠ 0 := by
  have hrate := rate_lower_pinched_from_rho_bounds h0 h1 h3 hrel
  have hpos : 0 < 5 * (b ^ 2 + 4 * Λ - 8 * δ) := by
    nlinarith [sq_nonneg b, hΛδ]
  intro hz
  have hzero : 4 * (rate k1 k3) ^ 2 = 0 := by
    rw [hz]
    ring
  nlinarith

end

end Yau26Step27
