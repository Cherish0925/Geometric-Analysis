import Mathlib

namespace QiushiPerp

/-- Rational Riccati identity underlying the exact-CH minus-channel zero mode
`f=x/(1+x)^(5/2)`.  Here `q=f'/f`; clearing denominators reduces the
Sturm equation `-(p f')' + V f = 0` to this identity. -/
theorem qiushi_minus_riccati (x : ℝ) (hx : x ≠ 0) (h1 : 1 + x ≠ 0) :
    let p : ℝ := x * (1 + x) / 4
    let dp : ℝ := (1 + 2*x) / 4
    let q : ℝ := (2 - 3*x) / (2*x*(1+x))
    let dq : ℝ := ((-3)*(2*x*(1+x)) - (2-3*x)*(2+4*x)) /
      (2*x*(1+x))^2
    let V : ℝ := (4 - 18*x + 3*x^2) / (16*x*(1+x))
    (-1) * (dp*q + p*(dq + q^2)) + V = 0 := by
  dsimp
  field_simp
  ring

/-- Companion rational Riccati identity for the exact-CH plus-channel zero
mode `f=x*sqrt(1+x)`. -/
theorem qiushi_plus_riccati (x : ℝ) (hx : x ≠ 0) (h1 : 1 + x ≠ 0) :
    let p : ℝ := x * (1 + x) / 4
    let dp : ℝ := (1 + 2*x) / 4
    let q : ℝ := (2 + 3*x) / (2*x*(1+x))
    let dq : ℝ := ((3)*(2*x*(1+x)) - (2+3*x)*(2+4*x)) /
      (2*x*(1+x))^2
    let V : ℝ := (4 + 18*x + 15*x^2) / (16*x*(1+x))
    (-1) * (dp*q + p*(dq + q^2)) + V = 0 := by
  dsimp
  field_simp
  ring

end QiushiPerp
