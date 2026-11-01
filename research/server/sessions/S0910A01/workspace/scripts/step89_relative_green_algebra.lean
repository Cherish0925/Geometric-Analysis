import Mathlib

/-!
Step 89 small formal lemma: in a relative mixed-minus-all-same comparison,
the odd--odd diagonal coefficient vanishes because ε_i^2=1.
This is only algebra for the finite comparison, not a geometry theorem.
-/

namespace Yau26Step89

/-- A chirality sign is represented by an integer satisfying `ε^2=1`. -/
def IsSign (ε : Int) : Prop := ε * ε = 1

/-- Odd--odd diagonal terms cancel in the relative coefficient `ε_i ε_i - 1`. -/
theorem oddOddDiagonalCancels {ε : Int} (hε : IsSign ε) : ε * ε - 1 = 0 := by
  dsimp [IsSign] at hε
  rw [hε]
  norm_num

/-- For two sign assignments that both square to one at the same node, their
odd--odd self coefficients agree. -/
theorem oddOddSelfSameForSigns {ε δ : Int} (hε : IsSign ε) (hδ : IsSign δ) :
    ε * ε - δ * δ = 0 := by
  dsimp [IsSign] at hε hδ
  rw [hε, hδ]
  norm_num

/-- If the all-same assignment has sign `1`, the mixed-minus-all-same odd--odd
coefficient on the diagonal is zero for any chirality sign. -/
theorem mixedMinusAllSameDiagonal {ε : Int} (hε : IsSign ε) : ε * ε - 1 * 1 = 0 := by
  dsimp [IsSign] at hε
  rw [hε]
  norm_num

end Yau26Step89
