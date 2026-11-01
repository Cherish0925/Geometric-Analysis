import Mathlib

/-!
Step 99 algebra certificate for the real-linear map
  z ↦ P z + Q * conjugate z.

If P = a + i b and Q = c + i d, then in real coordinates (x,y) the map has
matrix
  [[a+c, d-b], [b+d, a-c]]
and determinant |P|^2 - |Q|^2.  The second theorem proves the elementary
kernel consequence used in the Gate-3 correction: if these squared norms are
unequal, the kernel is trivial.  Hence a non-zero kernel can occur only at
|P|=|Q|; strict inequalities on either side are both invertible.
-/

namespace Yau26Step99

open Real

/-- Determinant of `z ↦ P z + Q conjugate z` in real coordinates. -/
theorem pq_real_det_formula (a b c d : ℝ) :
    (a + c) * (a - c) - (d - b) * (b + d)
      = (a^2 + b^2) - (c^2 + d^2) := by
  ring

/-- If `|P|^2 ≠ |Q|^2`, then the real-linear map has only the zero kernel. -/
theorem pq_kernel_trivial_of_normsq_ne
    (a b c d x y : ℝ)
    (h1 : (a + c) * x + (d - b) * y = 0)
    (h2 : (b + d) * x + (a - c) * y = 0)
    (hdet : (a^2 + b^2) - (c^2 + d^2) ≠ 0) :
    x = 0 ∧ y = 0 := by
  let A : ℝ := a + c
  let B : ℝ := d - b
  let C : ℝ := b + d
  let D : ℝ := a - c
  have hdetADBC : A * D - B * C = (a^2 + b^2) - (c^2 + d^2) := by
    dsimp [A, B, C, D]
    ring
  have hxmul : (A * D - B * C) * x = 0 := by
    calc
      (A * D - B * C) * x
          = D * (A * x + B * y) - B * (C * x + D * y) := by
              ring
      _ = D * 0 - B * 0 := by rw [show A * x + B * y = 0 by simpa [A, B] using h1,
                                  show C * x + D * y = 0 by simpa [C, D] using h2]
      _ = 0 := by ring
  have hymul : (A * D - B * C) * y = 0 := by
    calc
      (A * D - B * C) * y
          = A * (C * x + D * y) - C * (A * x + B * y) := by
              ring
      _ = A * 0 - C * 0 := by rw [show C * x + D * y = 0 by simpa [C, D] using h2,
                                  show A * x + B * y = 0 by simpa [A, B] using h1]
      _ = 0 := by ring
  have hdet' : A * D - B * C ≠ 0 := by
    intro h
    exact hdet (by rw [← hdetADBC, h])
  exact ⟨eq_zero_of_ne_zero_of_mul_left_eq_zero hdet' hxmul,
         eq_zero_of_ne_zero_of_mul_left_eq_zero hdet' hymul⟩

end Yau26Step99
