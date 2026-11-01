# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step86_forced_bochner_superlevel_and_localization.md",
    "Sessions/S0910A03/workspace/data/step87_resolvent_comparison.json"
  ]
}
```

## Task

Verify the following forced reflected OT connector obstruction theorem. The setting: a complete 2D smooth weighted base (B², γ_B, dμ = e^σ dA) with σ-harmonic map U: B → H² (hyperbolic plane), orbit energy e = |dU|²_{H²}, weighted tension F = τ_σ(U), and the Einstein base equation gives Ric_f^4 = Ric_B - Hess σ - ½dσ⊗dσ ≥ -(3+δ)γ_B (finite-dimensional CD condition with N=4).

The argument chain:

1. FORCED BOCHNER (from Steps 85-86): ½Le ≥ |DdU|² + div_σ V - |F|² + ½e² - (3+δ)e, where V(X) = ⟨dU(X), F⟩, |V| ≤ |F|√e ≤ 2δ√e. Drop |DdU|² ≥ 0.

2. MASSIVE COMPARISON: With κ = 6+2δ = 2(3+δ), rearrange to get (-L+κ)e ≤ κ² + 2(2δ)² - 2div_σ V. Key step: 2κe - e² ≤ κ² (completing the square).

3. LI-YAU FISHER INFORMATION: On a complete smooth weighted manifold with CD(-K,N) [Ric_f^N ≥ -K], the heat kernel p_t of L satisfies the Li-Yau gradient estimate, hence I(t) := ∫ p_t |∇_y log p_t|² dμ ≤ N/(2t) + NK/2. By Cauchy-Schwarz and heat conservation ∫p_t dμ = 1: ∫|∇_y p_t(x,y)| dμ(y) ≤ √I(t) ≤ √(N/(2t) + NK/2).

4. RESOLVENT ESTIMATE: C_κ = sup_x ∫|∇_y G_κ(x,y)| dμ(y) ≤ ∫_0^∞ e^{-κt} √(N/(2t)+NK/2) dt = √(2πN/(2κ)) + √(NK/2)/κ. With N=4, K=3+δ: C_κ ≤ √(2π/κ) + √(2(3+δ))/κ.

5. COMPARISON PRINCIPLE: Since -L+κ has strictly positive potential (κ>0) on a complete manifold, if (-L+κ)(ψ-e) ≥ 0 and ψ-e is bounded below, then ψ-e ≥ 0 (Omori-Yau). Define ψ by (-L+κ)ψ = κ²+8δ²-2div_σ V. Then ψ = (κ²+8δ²)/κ + ψ_2 where |ψ_2| ≤ 2C_κ·2δ·√B (B=sup e). So B ≤ κ+8δ²/κ + 4δC_κ√B.

6. QUADRATIC CLOSURE: B ≤ α + β√B with α = κ+8δ²/κ, β = 4δC_κ. Solution: B ≤ (β/2+√(β²/4+α))². CENTER FLOOR: ⟨e(0,·)⟩_μ ≥ 12-8δ (from reflected center Gauss equation with defect). For δ < δ₀ ≈ 0.249, the ceiling B(δ) < 12-8δ = floor. Contradiction.

Verify each step. Particular attention to: (a) Is the Li-Yau Fisher information bound I(t) ≤ N/(2t)+NK/2 correct under CD(-K,N) with N > dim M? What is the standard reference? (b) Is stochastic completeness (∫p_t dμ = 1) guaranteed under CD(-(3+δ),4) on our complete weighted manifold? (c) Is the integration by parts for R_κ[div_σ V] justified when V vanishes at infinity? (d) Does the Omori-Yau maximum principle apply to -L+κ on this specific complete manifold (exponential weighted volume growth)? (e) Is the center floor 12-8δ correctly derived from the Gauss equation? Check all sign conventions.

## Output

## Verification memo — forced reflected OT connector obstruction

**Bottom line.** The algebra of Steps 1–2 and the resolvent closure of Steps 4–6 are correct and internally consistent, and I reproduced the detail-table arithmetic exactly. The one derivation step that is stated incorrectly is the Fisher-information bound in Step 3: the displayed inequality `I(t) ≤ N/(2t)+NK/2` is the small-`t` truncation of the actual Bakry-Émery/de Bruijn bound, not that bound itself. Correcting it does not remove the obstruction; it replaces the ad hoc numerics by a clean closed form and shifts the threshold from `δ₀≈0.249` to `δ₀≈0.246`. Details below, item by item.

---

### Steps 1–2 (forced Bochner + massive comparison): correct

I checked the constants. With `Q(A)=½e²+det A≥½e²`, `E_B:A≥−δe` (valid since `A⪰0`, so `E_B:A≥−‖E_B‖_op tr A`), and `|F|²=2 tr(Ê₀²)≤4δ²` (eigenvalues `±a`, `|a|≤δ`), Step 86 (3.2) gives `½Le ≥ |DdU|²+div_σV−|F|²+½e²−(3+δ)e`. Doubling and using `κ=2(3+δ)`:
`Le ≥ 2div_σV − 2|F|² + e² − κe`, hence `(−L+κ)e ≤ κ² + 2|F|² − 2div_σV ≤ κ²+8δ²−2div_σV`, since `2κe−e² = κ²−(e−κ)² ≤ κ²`. The `8δ²` is `2|F|²` with `|F|≤2δ`, and `κ=2(3+δ)` is used consistently. All correct.

### (a) The Li-Yau/Fisher bound is stated in truncated form; the correct bound is larger and cleaner

This is the substantive issue. The correct route on a stochastically complete weighted manifold with `CD(−K,N)` (finite `N`, here `N=4>dim=2`) is the de Bruijn identity plus the `N`-dimensional Γ₂ inequality:

`dI/dt = −2∫ p_t Γ₂(log p_t) dμ`, and `Γ₂(φ) ≥ (1/N)(Lφ)² − K|∇φ|²`.

With `∫p_t L log p_t dμ = 0` and Cauchy-Schwarz `∫p_t(L log p_t)² ≥ I(t)²`, this gives the Riccati inequality
`I'(t) ≤ 2K I(t) − (2/N) I(t)²`,
whose maximal solution starting from `I(0⁺)=∞` is

**`I(t) ≤ NK / (1 − e^{−2Kt})`.**

Its small-`t` expansion is `I(t) ≤ N/(2t) + NK/2 + NK²t/6 + …`. So the displayed `N/(2t)+NK/2` is exactly the first two terms; the true bound is strictly **larger** for every `t>0`. Since the argument integrates `∫₀^∞ e^{−κt}√I(t) dt` with `K/κ = 1/2` (not small), the dropped terms are `O(1)`, not negligible. The label "Li-Yau under CD(−K,N)… standard, verified" is therefore not accurate for the clean form written; the citable rigorous object is the de Bruijn–Riccati bound above (this is the standard `N`-Bakry-Émery calculation; Li-Yau (1986) for `Ric≥−K` gives an `α>1` form whose `K`-term is worse still).

The correction is favorable, not damaging, and it simplifies the theorem. Compute the resolvent constant with the correct `I(t)`:

`C_κ ≤ ∫₀^∞ e^{−κt} √(NK/(1−e^{−2Kt})) dt = (√(NK)/(2K)) · B(κ/(2K), ½)`.

Here is the elegant point the note misses: **`κ = 6+2δ = 2(3+δ) = 2K` identically for all δ.** Hence `κ/(2K)=1`, `B(1,½)=2`, and

**`C_κ = √(NK)/K = √(N/K) = 2/√(3+δ)`** (exact, closed form).

At `δ=0` this is `2/√3 = 1.15470`, sitting between the note's `C_κ_numerical=1.13518` (which used the truncated integrand and is slightly too small) and `C_κ_upper_bound=1.43157` (subadditive split of the truncated integrand). Redoing the threshold with `C_κ=2/√(3+δ)`, `α=κ+8δ²/κ`, `β=4δC_κ`, `B=(β/2+√(β²/4+α))²` versus floor `12−8δ`:

- `δ=0.24`: `B≈9.909 < 10.08` (obstruction holds)
- `δ=0.245`: `B≈10.006 < 10.04` (holds)
- `δ=0.248`: `B≈10.064 > 10.016` (does not hold)

so the true threshold is `δ₀ ≈ 0.246`, versus `0.24885` reported. The obstruction survives; the numerology is nearly unchanged, and the corrected version is *cleaner* (exact `C_κ=2/√(3+δ)`, exact `β=8δ/√(3+δ)`) and fully rigorous. I recommend replacing the Step 3 statement by the Riccati bound and re-deriving `C_κ` from it.

### (b) Stochastic completeness: holds, but contingent on the completed extension

`∫p_t dμ = 1` is what makes `∫p_t L log p_t dμ = 0` (used in (a)) and the flux argument in (c)/(d) legitimate. On a geodesically complete weighted manifold, `CD(−K,4)` with finite `K` gives Bishop–Gromov weighted volume growth `V_μ(B_r) ≲ e^{√((N−1)K)\,r}` (exponential), so Grigor'yan's integral `∫^∞ r/log V_μ(r)\,dr = ∞` diverges and the semigroup is conservative. The cusp-benchmark check `V_μ(B_R)~e^{3R}` in the JSON is consistent with this. The genuine assumption is upstream: the reflected connector is compact with two exit faces, and completeness plus a *global* `CD(−(3+δ),4)` bound requires that the connector be glued to complete cusp ends on which the finite-dimensional curvature bound continues to hold and the metric/`U`/`σ`/defect extend smoothly. Step 86 §10 flags this. It is an interface assumption of the theorem, not automatic.

### (c) Integration by parts for `R_κ[div_σ V]`: justified, and it is what removes `DF`

`R_κ[div_σ V](x) = ∫ G_κ(x,y) div_σ V(y) dμ(y) = −∫ ⟨∇_y G_κ(x,y), V(y)⟩ dμ(y)`, so `F` is never differentiated — this is the correct way past the pointwise obstacle noted in Steps 85–86 (`div_σ V` contains `DF`). The pairing is well defined because `C_κ<∞` puts `G_κ(x,·)∈W^{1,1}(μ)`, and `|V|≤f_0√e ≤ 2δ√B` with `V→0` at infinity. The surface term at infinity vanishes from exponential decay of `G_κ` (mass `κ>0`) against decaying `V`. Then `|R_κ[div_σ V](x)| ≤ 2δ√B·C_κ`, giving `B ≤ α + β√B` with `α=κ+8δ²/κ`, `β=4δC_κ`. Verified.

### (d) Omori-Yau / comparison: valid, with one point worth making explicit

The weak maximum principle for `L` on this class is equivalent to the stochastic completeness established in (b) (Grigor'yan / Pigola–Rigoli–Setti), and exponential weighted volume growth is compatible with it. The comparison then runs as follows, and it is worth writing out because `R_κ` of a constant does **not** vanish at infinity. Set `S=κ²+8δ²−2div_σV` and `w=e−R_κ[S]`. Then `(−L+κ)w≤0`. As `x→∞`, `e→0` while `R_κ[S]→(κ²+8δ²)/κ>0`, so `w→−(κ²+8δ²)/κ<0`; and `w` is bounded above because `e→0` at infinity forces `e` bounded (a continuous function tending to `0` on a complete manifold attains its max, giving `B<∞` a priori — this also removes the apparent circularity in `|V|≤f_0√B`). The weak maximum principle then yields `w≤0`, i.e. `e≤R_κ[S]≤α+β√B` pointwise, and taking the sup gives `B≤α+β√B`. Sound.

### (e) Center floor `12−8δ`: sign structure correct; the constants rest on unshown steps

The logical structure is right for an obstruction: floor `12−8δ` decreases in `δ`, ceiling `B(δ)` increases, they cross at `δ₀`, and for `δ<δ₀` floor `>` ceiling excludes the connector. The exact-case core (`δ=0`) is checkable from the material given: at an interior max `∇e=0, Le≤0`, so `½e(e−6)≤0` gives `e≤6` (Step 85 §4), while the center identity gives `⟨e(0,·)⟩≥12`; the factor-2 tension between `6` and `12` is the geometric heart, and `δ₀` simply measures its robustness. What I cannot verify from the supplied files is the absolute value `12` (via `R=−6` on the totally geodesic center) and, more importantly, the **linear coefficient `8`** in `12−8δ`: both depend on the Einstein base equation and the Gauss/center identity of Steps 79/82/84, which are not in the provided notes. Internal consistency is maintained (the table uses `12−8δ` uniformly), but the coefficient `8` should be re-derived against those steps, since `δ₀` depends on it as directly as on `C_κ`. No sign error is visible in what is shown.

---

### On value and the class addressed

Taken with the correction in (a) and the assumption in (b), this is a valid quantitative obstruction, and cleaner than presented: it excludes reflected, free-`T²`, orthogonally transitive approximate-Einstein connectors whose exits extend to exact cusp ends, for `‖E‖≤δ<δ₀≈0.246`, on the idealized complete extension. Three points determine how far it reaches.

1. `δ₀≈0.246` is an `O(1)` smallness, not asymptotic; it is meaningful but does not reach fixed-`δ` metrics.
2. The hypotheses `e→0 at infinity` + complete `CD(−(3+δ),4)` idealize the exit as an exact cusp; a connector matching only an *approximate* expanding tail is not directly covered, and neither is approximate twist, singular `T²` orbits, non-OT graph metrics, nor `N#N` `S³` necks. Steps 85 §9 and 86 §10 already state this.
3. It is one obstruction within the disproof-direction analysis, complementary to the warped-waist and `N#N` BCG results; it does not by itself resolve Yau 26 or the existence direction.

The most useful next mathematical object, consistent with Step 86 §8–9, is whether the exact-cusp weighted spectral gap (`λ₁(−L)→9/4`, exponential area growth) survives the coupled forced geometry — that is the input that would let the global superlevel estimate (5.2) propagate without a length loss and would make the resolvent ceiling here a consequence rather than an assumption about the completed manifold. The clean identity `κ=2K` found above also suggests the resolvent constant is genuinely tied to the effective dimension `N=4` and the base curvature `K=3+δ` in a rigid way worth exploiting.