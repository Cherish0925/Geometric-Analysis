# Step 19 — Exact CH exterior response, stationary large-collar cells, and the far-field charge λ

Normalization: Ric_CH = −6g, values of P and J₆ divided by 8π² (threshold 1).
Fixed perpendicular slot g = dx²/(4G) + F σ₁² + x σ₂² + x e^w σ₃², Step-7 axes
(a₁,a₂,a₃) = (√x, √(x e^w), √F), CH: F = x, G = x(1+x), w = log(1+x), u = (0,3x,0).

## 1. Exact linearized Einstein modes of CH in the diagonal class

`scripts/ch_linear_einstein_modes.py`, `ch_linear_mode_solve.py`, `check_xgauge_mass_mode.py`,
`calabi_ke_check.py` (all SymPy, zero residuals).

* The exchange a₁↔a₃ splits the linearization. In the antisymmetric sector (θ = δlog(a₁/a₃),
  v₋ = δu₁ − δu₃) the linear scalar curvature vanishes identically, and the Step-7 torsion relation
  d/dx[(x/(1+x))²θ] = ½ f₋ v₋, f₋ = x/(1+x)^{5/2}, is an identity (it *defines* v₋ from θ).
  The linearized trace-free Ricci is (2/(x(1+x)))·L[θ] (z₁ = −z₃, z₂ = 0) with
  L[θ] = x²(1+x)²θ'' + x(1+x)(3x+2)θ' + 2(x−1)θ.
* Its kernel is exactly the two-parameter family θ = k⁻¹[C + (c/2)∫₀ˣ f₋²], k = (x/(1+x))².
  C is the non-decaying squashing of the conformal infinity (v₋ = 0, θ → C).
  The decaying member is the **antisymmetric Einstein mass mode**
  v₋ = c f₋,  θ = −c(6x²+4x+1)/(24x²(1+x)²) ~ −c/(4x²),
  which is linearized Einstein (dz = 0, ds = 0), singular at the centre, and in the x-gauge reads
  F = x e^{−2θ}, δw = −θ(1+2x)/(1+x), δG = θx + 2x²(1+x)θ'.  ∫₀^∞ f₋² = 1/12.
* U(2)-invariant sector: besides the gauge mode and a non-decaying squashing mode
  σ = (8x²+4x−1)/(16x²), β = (8x²+1)/(8x²), the Calabi family
  a₁ = a₃ = √x, a₂² = G = x + x² + m/x is **exactly** Kähler–Einstein (Ric = −6g) for every m,
  with u = (0,3x,0) unchanged. A smooth O(−1) bolt needs F'G' = 1 at G(x₀) = 0, but this family
  has G'(x₀) = 2 + 3x₀: the cone angle is forced, consistent with the Kähler period obstruction.

## 2. Exact exterior response (the null line)

The raw quadratic P of the minus channel on CH is (Step 7 re-derived from the squares)
  E[v₋] = ∫ μ (w')² dx,  w = v₋/f₋,  μ = x(1+x)f₋²/4 = x³/(4(1+x)⁴).
The transverse sector does not see radius perturbations at quadratic order (H₁ = H₃ = 0 on CH).
With entrance data w(ρ) = w₀, θ(ρ) = Θ and an infinite CH collar (θ → 0), minimizing E subject to
the torsion constraint gives
  **E_ext(ρ; w₀, Θ) = δ²/I(ρ)**,  δ = −2k(ρ)Θ − w₀ G(ρ),  G(x) = ∫ₓ^∞ f₋² = (6x²+4x+1)/(12(1+x)⁴),
  I(ρ) = ∫_ρ^∞ G²/μ  (I(10) = 0.0042304).
The null line δ = 0 is the Einstein mass mode (zero cost; this is the Strategist's relation).
Off the null line the optimal exterior is μw' = −λG with constant λ = −δ/I, i.e.
  w(x) = w₀ − λ[2log(x/ρ) − (4/3)(1/x − 1/ρ) − (1/6)(1/x² − 1/ρ²)]:
v₋ decays like x^{−3/2}log x and the exterior carries a nonzero constant λ, the costate conjugate to
the cyclic variable θ of the quadratic exterior problem. The finite-X exact-collar version
(w(X) = θ(X) = 0) is solved in closed form in `scripts/exterior_null_line.py`; for fixed entrance data
its excess over E_ext behaves like (log X)²/X².

## 3. Stationary large-collar cells: the old terminal gradients were an optimizer artifact

`scripts/perp_lm.py` minimizes J₆ as a sum of squares of the exact Cartan spin residuals
(z/2, (s+24)/4)·√(weight) with a trust-region least-squares Jacobian method. Its residual sum agrees
with the independent DualCell curvature evaluation to 1e−7–2e−6 for X ≤ 512 (to 1e−5 at X = 1024,
where float cancellation at large x becomes visible; X = 1024 values are not used).
Converged in seconds from the earlier L-BFGS records (gradients 1e−6–1e−8 instead of 3e−3–8e−3):

| x₀ | X | deg | J₆ (float) | earlier L-BFGS |
|---|---|---|---|---|
| .03 | 64 | 16 | 0.9957372 | 0.9958547 |
| .03 | 128 | 24 | 0.9955740 | 0.9956702 (certified ≤0.9956711) |
| .03 | 256 | 24 | 0.9955188 | 0.9956012 |
| .03 | 512 | 28 | 0.9955003 | — |
| .038 | 128 | 24 | 0.9952870 | — |
| .038 | 256 | 24 | 0.9952045 | — |
| .038 | 512 | 28 | 0.9951812 | — |

Bolt-area scan at X = 256 (`data/perp_tail/area/`): x₀ = .015 → .99767, .02 → .99677,
.025 → .99604, .033 → .99532, .035 → .99524, .037 → .99521, .038 → .99520, .039 → .99521,
.04 → .99523, .043 → .99536, .046 → .99558, .05 → .99603, .07 → 1.00079.
At X = 512: .036 → .995196, .038 → .995181, .04 → .995210, .042 → .995274.
The optimal bolt area moved from ≈.03 (an artifact of unconverged optimization) to x₀ ≈ .038.

Exact autodiff Hessian at x₀ = .038, X = 256 (`scripts/cell_hessian.py`,
`data/perp_tail/hess_x00.038_X256_d24.json`): one exact null eigenvalue (the overwritten
coefficient cG[0], a parametrization redundancy), all others positive, the smallest 1.9e−6 and
3.8e−6, then 1.8e−4. The full Newton step predicts a further decrease of only 4×10⁻¹⁰. The record is
a strict local minimizer within the 72-parameter ansatz (modulo the redundancy).

Arb certification of the LM records is running (tasks s19_t25_tool1, s19_t32_tool1; outputs under
`data/perp_tail/rig/` and `rig038/`). Until those complete, the numbers above are floating values.

## 4. The far field of the stationary cells is the exact exterior response

`scripts/tail_mode_decomposition.py` computes the gauge-invariant θ = log(a₁/a₃), v₋, v₊,
u₂ − 3a₁a₃ along the cells. For the LM cells, v₋/f₋ is *not* a plateau but grows logarithmically,
and `exterior_null_line.py` shows that it is exactly the off-null exterior response:

| cell | λ fitted on [4, X/8] | λ = −δ/I from the trace at ρ = 10 | predicted cost beyond 10 | actual J beyond 10 |
|---|---|---|---|---|
| x₀=.03, X=512 | 0.1508 | 0.1498 | 1.030e−4 | 1.017e−4 |
| x₀=.038, X=512 | 0.1833 | 0.1827 | 1.531e−4 | 1.500e−4 |

(The sign convention is that λ_fit multiplies −L(x).) Beyond x = 10 the whole cost is the linear
antisymmetric exterior response to 1–2%; the symmetric sector and scalar curvature are negligible
there (|v₊| ≲ 4e−5, J − P ≈ 3e−8). The entrance trace is about 21% off the null line
(δ = −7.7e−4 against null moment −3.7e−3 for x₀ = .038). The core chooses to pay 1.4e−4 in the
exterior. The minimizer does **not** become asymptotically Einstein at the mass order: it carries the
constant far-field charge λ ≈ 0.18.

Finite-collar convergence follows from the same formula. For the x₀ = .03 trace the predicted
fixed-trace excesses are 9.45e−5, 2.70e−5, 8.0e−6 at X = 128, 256, 512. The predicted differences
j(256) − j(512) = 1.89e−5 match the observed 1.85e−5. The 128→256 prediction of 6.8e−5 is reduced to
the observed 5.5e−5 by core readjustment. For x₀ = .038 the excess at X = 512 is 1.2e−5.
Extrapolated infinite-collar diagonal value at x₀ ≈ .038: **j∞ ≈ 0.99517**
(η∞ ≈ 0.0048, balanced upper coefficient 4 − 8η/9 ≈ 3.99573). This is an extrapolation, not a
certified value.

## 5. Consequences

1. *Construction.* Converged diagonal cells improve the explicit deficit from η = .00433
   (certified X = 128, x₀ = .03) to ≈ .00480 (float, x₀ = .038, X = 512). Pending certification, the
   balanced coefficient is ≈ 3.9957 + ε. Earlier statements that large-collar profiles had
   "non-small terminal gradients" are superseded: the stationarity problem inside the ansatz is
   solved, and the Hessian is positive.
2. *Structure of the infinite-collar minimizer.* It is asymptotically CH with an anisotropic,
   contact-plane (weight-two, a₁↔a₃-odd) far field v₋ ≈ f₋(A − 2λ log x), θ ~ x⁻², at the ρ⁴ order of
   ACH asymptotics, with a nonzero conserved exterior charge λ. This is the far field that produced
   the phase-locked weight-four pair interaction of Steps 13–14; the interaction of two cells is
   therefore governed by λ and A, and the shared-exterior problem of Step 12 reduces in the minus
   channel to the explicit μ, G, I kernels above.
3. *Lower theory.* For the diagonal problem the unbounded collar can be replaced by the exact
   transparent condition E_ext = δ²/I(ρ), plus quadratic symmetric terms and nonlinear corrections.
   The minimization becomes a compact problem on [bolt, ρ] with a known terminal penalty, which is
   the finite-interface core problem needed for an HJ subsolution with a terminal cost.
   The terminal penalty is only justified for competitors that are in the linear regime at ρ. A
   lower theorem still needs an exterior bound for traces far from CH. A competitor ending far from
   CH at ρ is not penalized by this formula, and P_core with free end can vanish (local Einstein
   bolt solutions), so the global exterior estimate remains the essential missing piece.
4. *Where the saving is.* The x₀ = .038 split (X = 512) is J_core(x ≤ 5) = 0.99466,
   J(5 < x ≤ 10) = 3.7e−4, J(x > 10) = 1.5e−4. Essentially the whole deficit is made at x ≲ 5, where
   the Step-17 failure band of the Chern–Simons primitive lies (u₂ ≈ 2 around x ≈ 2/3).
