import Mathlib

namespace RiccatiShift

/-- The scalar algebra behind the shifted transverse HJ Riccati variable:
if `y = k + a/2`, then the unshifted quadratic expression
`kdot/2 + k*d*a + k*d*k` equals
`ydot/2 + y*d*y - (a*d*a + adot)/4`. -/
theorem qiushi_scalar_shift (k a d kdot adot : ℝ) :
    let y := k + a / 2
    let ydot := kdot + adot / 2
    kdot / 2 + k * d * a + k * d * k =
      ydot / 2 + y * d * y - (a * d * a + adot) / 4 := by
  dsimp
  ring

/-- Boundary translation for the relative seed: `k=-a` becomes `y=-a/2`. -/
theorem qiushi_seed_boundary (a : ℝ) : (-a) + a / 2 = -a / 2 := by ring

/-- Boundary translation for the zero function: `k=0` becomes `y=a/2`. -/
theorem qiushi_zero_boundary (a : ℝ) : 0 + a / 2 = a / 2 := by ring

end RiccatiShift
