# TTCS Independent Branch Record

```json
{
  "step_id": 74,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step74_graph_center_and_positive_flux_rebalance.md",
    "Sessions/S0910A01/workspace/data/step74_torus_yamabe_center.json",
    "Sessions/S0910A01/workspace/scripts/step74_torus_yamabe_center.py",
    "Sessions/S0910A02/workspace/notes/step73_global_positive_proof_allocation.md",
    "Skills/qiushi-yau26/references/research/20260912.tex",
    "Sessions/S0910A01/workspace/notes/step73_preissmann_koiso_anisotropy.md"
  ]
}
```

## Task

Verify the Step 74 route correction for the Yau--26 research. Read the Step74 note and supporting data, together with A02's positive-branch allocation and the 20260912 manuscript source. Check two load-bearing mathematical points: (1) the graph-neck repair: does the construction h0=dtheta^2+e^{2f}dx^2+e^{-2f}dy^2 with negative Yamabe normalization really give analytic T^2-invariant scalar -6 torus metrics suitable as Koiso center data S(0)=0, S'(0)=Ric_h^#+3I, and what assumptions or caveats remain? (2) the positive flux scale critique: does FND:flux / constant-scalar refinement only give a c/L lower bound, so that nonzero obstruction coefficient is compatible with delta->0 along L->infty unless an additional sequence-scale mechanism is proved? Compare with the manuscript's |log a| delta_+ -> 1/6 construction. Please identify any mathematical errors, missing hypotheses, or sharper next theorem statement that would materially improve the research direction.

## Output

## Verification memo — Step 74 route correction (Yau‑26)

I checked the two load‑bearing points against the Step 74 note, the `step74_torus_yamabe_center` data and script, the Step 73 Preissmann/Koiso note, A02's Step 73 allocation, and the flux material in `20260912.tex`. Both points are mathematically sound; the flux critique in fact reproduces a statement the manuscript already makes. Details, one arithmetic re‑derivation that matters for A02's mode lemma, and a sharper next‑theorem follow.

---

### Part 1 — The Yamabe center construction is correct; the open work is global extension

**Scalar‑curvature identity.** For the diagonal three‑metric `ds²+e^{2b}dx²+e^{2c}dy²` the formula
`R = -2(b''+c'') - 2(b'²+c'²+b'c')` is the correct specialization of
`R = -2Σφ_i'' - Σ(φ_i')² - (Σφ_i')²`. With `b=f, c=-f`: `Σφ''=0`, `Σ(φ')²=2(f')²`, `Σφ'=0`, so `R(h₀)=-2(f')²`. Verified.

**Sign of the conformal invariant.** Since `f` is nonconstant, `∫R(h₀)dV = -2∫(f')² < 0`. The test function `u≡1` in the conformal‑Laplacian Rayleigh quotient then gives `λ₁(L) < 0`, hence `Y([h₀]) < 0`. The chain "total `R<0` ⇒ `Y<0`" is valid (the reverse implication would not be, but it is not used). Correct.

**`T²`‑invariance of the minimizer.** In the `Y<0` case the constant‑scalar metric with a *fixed* constant `-6` is unique (fixing the constant fixes the scale). The `x,y`‑translations are isometries of `h₀` because its coefficients depend only on `θ`; they permute the (one‑element) solution set, so `ψ=ψ(θ)`. This symmetry‑uniqueness step is correct.

**The reduced ODE.** With `√det h₀ = 1` and `ψ=ψ(θ)`, `Δ_{h₀}ψ = ψ''`, and `n=3` gives `a=8`, exponent `5`: `R(h)=ψ^{-5}(-8ψ''-2(f')²ψ)`. Setting `=-6` gives `-8ψ''-2(f')²ψ=-6ψ⁵`. Analytic `f` ⇒ analytic RHS ⇒ analytic `ψ`. Arclength `ds=ψ²dθ`, `b=2logψ+f`, `c=2logψ-f`, both periodic. This genuinely resolves the Step 73 zero‑mean obstruction: the anisotropy lives in the periodic `f` and the volume factor in the periodic `ψ`, so `h` is a bona‑fide `T³` metric. Correct and cleaner than the `v=Bsinθ` Riccati branch.

**Koiso constraints.** At a totally geodesic slice `S(0)=0` of a Gaussian collar with `Ric_g=-3g` (dim 4):
- Hamiltonian: `R_h = R_g - 2Ric_g(ν,ν) = -12 - 2(-3) = -6`. This is exactly the scalar the Yamabe step produces — the construction is designed to hit the constraint, not to assume it.
- Momentum `div S - dH = 0` holds trivially at `S=0`.
- Riccati at `S=0`: `Ric_g(ν,ν) = -tr S'(0)`, so `tr S'(0)=3`.
- Tangential, with `II=0`: `Ric_g|_tan = Ric_h - S'(0)` (lowered). Setting `Ric_g|_tan = -3h` gives `S'(0)=Ric_h^♯+3I`. Trace check: `R_h - tr S'(0) = -6-3 = -9 = tr(-3h)`. ✓

All three are internally consistent, and the JSON is internally consistent: `Ric`‑eigenvalues = `S'`‑eigenvalues `-3` in every direction (e.g. circle `S'∈[-5.32,0]` ↦ `Ric∈[-8.32,-3]`), `tr S'≈3.000`, anisotropy `|S'-I|≈7.15` (from the `x`/`y` range top `8.146`). The `1.1e-16` residual is the ODE‑definition re‑substituted and is therefore circular; the meaningful independent check is the spectral (FFT) one at `~1.5e-5`, which confirms `R≈-6`. I would rely only on the FFT number when reporting.

**What remains genuinely open (assumptions still to be discharged).**
1. Ammann–Moroianu–Moroianu supplies an *exact* analytic Einstein collar on some interval `|t|<ε`; `ε` need not be uniform, and the solution can develop curvature concentration before reaching a cusp. Existence of a global half‑core is not delivered.
2. Cusp flattening: a `Ric=-3g` cusp end is `dt²+e^{2t}h_flat` with `S→I`, `H→3`, and a *flat* cross‑section. The center fiber has `R_h=-6≠0`, so `Ric_{h_t}→0` must hold along the collar. Step 73 models this as `Ric_{h_t}~e^{-2t}` with fitted anisotropy‑decay rate `≈2.00`; but the Step 73 note itself records a `√3` vs `3` mean‑curvature tension between the `a=0` two‑factor gauge and the full three‑factor system. Which asymptotic the true PDE selects, and whether the mean curvature actually reaches the cusp value, is not settled.
3. The center datum is necessarily anisotropic (Preissmann: a `Ric=-2h` `T³` is impossible), and the Yamabe datum satisfies this — but higher‑Fourier‑mode stability of the linearized Einstein–DeTurck operator with gauge and coupling terms is, as the note states, unproven.

So Part 1 is a correct existence statement for *admissible center data*; the substantive physics — a compact graph metric with small operator‑norm Ricci defect — is exactly the unproven part, and the note says so.

---

### Part 2 — The flux scale critique is correct and already latent in the manuscript

**The `c/L` bound is genuine.** For `o=r^{-n-2}K` (degree‑2 `K`), the nuclear mass is
`∫_A ‖o‖_* dV = ∫_b^R r^{-1}dr · J_K = L·J_K` (the `r` power is `-(n+2)+2+(n-1) = -1`). Operator/nuclear duality on the flux identity `∫_A⟨DRic_e u, o⟩ = -(n+2)I_K/2` gives
`‖DRic_e u‖_{op,∞} ≥ (n+2)I_K / (2 L J_K)`. Verified. The `1/L` arises because the dual test tensor's `L¹`‑mass grows like `L` while the flux numerator is a fixed model constant.

**Compatibility with `δ→0`.** With `L≍|log a|→∞`, a nonzero `K` is compatible with `δ→0` at rate `1/L`. The manuscript's constant‑scalar refinement gives `liminf L·δ_σ ≥ 1/6`, and its football double‑resolution model achieves `s_{ĝ_a}=4`, `|log a|·δ₊(ĝ_a)→1/6` with `L/T_a→1`. So `δ~1/(6L)→0` while `K≠0`. The manuscript states this explicitly ("误差本身趋零，绝非原题的普遍正间隙"). The Step 74 note reproduces exactly this reading — no error. `1/6` is a matched constant (flux floor `≥1/6`, models sit at the floor), so `δ` decays no faster than `1/(6L)` and no slower than the model realizes; the phrase "best possible behavior is `δL→1/6`" is better stated as "the floor `1/6` is simultaneously forced from below and realized."

**The dichotomy is `L` bounded vs `L→∞`.** If a tightly‑pinched sequence could be forced onto annuli with *bounded* `L`, `δ` would have a positive floor `∼1/(6L)` and the first obstruction would be forced to vanish, closing the `P_n^+` side. The constructed fillings evade this precisely by placing the obstruction on `L→∞` necks with a scale‑flat ramp `η'=1/L`. So the flux is a real necessity mechanism but does not close `P_n^+` by itself; an additional relation tying `δ` to `L` on the obstruction‑carrying annuli is needed. This is the correct logical structure.

**One point that sharpens A02's proposed mode lemma.** A02's dual indicial root `-((d-2)+ℓ)` and Wronskian coefficient `-(d+2ℓ-2)I_{K_ℓ}/2` are consistent with the manuscript at `ℓ=2` (`o=r^{-n-2}K`, root `-n`, coefficient `-(n+2)I_K/2`). But the nuclear‑mass scaling is *mode‑dependent* and this changes what the higher‑mode lemma can deliver:
`∫_A ‖o_ℓ‖_* dV = ∫_b^R r^{1-ℓ}dr · J_{K_ℓ}`.
- `ℓ=2`: `∫ r^{-1} = L` (logarithmic — the marginal case).
- `ℓ≥3`: `∫ r^{1-ℓ} ≈ b^{2-ℓ}/(ℓ-2) → ∞` as `b→0`, so the flux lower bound is `δ ≳ const·b^{ℓ-2} → 0` — power‑law weaker.
- `ℓ≤1`: trace/gauge.

So the quadratic mode `ℓ=2` is the *unique* logarithmically‑marginal mode; it is both the geometrically leading obstruction (the Biquard–Ozuch degree‑2 Weyl term `K=-⅓C_{ikjl}x^k x^l`) and the one the flux constrains most strongly, yet still only at `1/L`. Higher modes are individually *less* constrained by their own flux. A02's "mode‑by‑mode necessity lemma" should therefore not expect the higher‑`ℓ` fluxes to force their own coefficients to vanish; the control on `ℓ≥3` must come from elliptic subordination to `ℓ=2`, not from the analogous flux. This is worth stating in the lemma to avoid an inflated expectation of what the mode expansion buys.

---

### Sharper next‑theorem statement (the precise missing input)

The manuscript's energy‑flux version already contains the positive mechanism:
`δ_σ(g) ≥ [ (n+2)I_K/2 - C(ε+ℰ+R√ℰ+R²) ] / [ J_K L + CR(√ℰ+R) ]`, `ℰ=∫_A r^{-n}|Dq|²`.
On a **fixed** annulus `{1<r<R}` (so `L=log R` fixed) with a rescaled bubble sequence for which `ℰ_i→0`, `ε_i→0`, and `R` small enough that `CR² < (n+2)I_K/4`, this gives `δ_i ≥ (n+2)I_K / (4(J_K log R + CR²)) =: c₀(K,R) > 0`. Hence if `K≠0` survives in the limit bubble, `δ_i` cannot tend to `0`. So the flux **does** kill the first obstruction *provided the obstruction is captured at a fixed scale with vanishing weighted energy*.

The single unproven fact standing between the flux and `P_n^+` is therefore a **geometric neck‑decay (three‑annulus) estimate for the degree‑2 TT mode**:

> There exist `λ>1`, `θ<1` such that on any scale‑`λ` sub‑annulus of a maximal neck of a tightly‑pinched noncollapsed sequence,
> `‖K‖_{[λr,λ²r]} ≤ θ·max{ ‖K‖_{[r,λr]}, ‖K‖_{[λ²r,λ³r]} } + C δ_i`,
> where `K` is the degree‑2 TT Fourier component of `g_i − model`.

If such a `θ<1` holds, the quadratic content is concentrated near the endpoints, `Σ_scales |K| ≤ Cδ_i → 0`, and the fixed‑annulus flux forces the total first obstruction to vanish. The constructed `A_1`/football fillings are exactly the `θ=1` configurations (their `η'=1/L` ramp makes `K` scale‑flat, spreading it uniformly in `log r`) — i.e. they are the precise stress test the estimate must survive, and any genuine no‑Einstein tightly‑pinched sequence would also need such scale‑flat marginal necks to evade the flux. This tells the research where the real fork is:
1. prove the `θ<1` neck decay under tight positive pinching + scalar normalization (this closes `P_n^+` through the flux), or
2. build a *compact, no‑Einstein* manifold supporting scale‑flat quadratic necks (a refutation, if it can carry the positive‑pinch class: strict Hitchin–Thorpe in dim 4, finite `π₁`, `b₁=0`, PSC).

A02's stratified extension is compatible with this: for `N≥5` the transverse cone dimension `d=4`, stratum dimension `m=N-4`, and the correct condition along the stratum is the pointwise/elliptic bundle‑valued vanishing (Step 53), not the stratum‑integrated one — because `C⁰` pinching leaves an `O(1)` defect at each stratum point that integration cannot cancel. The neck‑decay estimate above would need a fibered version over the stratum.

---

### Minor points

- The Step 74 §6 topology correction is right: `#₅ℂP²` has `χ=7, τ=5`, so `2χ=14 < 15=3|τ|` violates Hitchin–Thorpe and it carries no Einstein metric, yet Prop FND:HT (tight positive pinching ⇒ strict HT for `δ<1/(1+√3)`) excludes it from the tight‑positive class. It is a PSC no‑Einstein manifold that is nonetheless not a `P_4^+` counterexample, so the relevant unknown reservoir is correctly narrowed to (no Einstein) ∩ (strict HT, finite `π₁`, `b₁=0`, PSC).
- Report the Yamabe center's numerical support using the FFT residual (`~1.5e-5`) and the spectral scalar range, not the `1.1e-16` figure, which is self‑referential.
- The `√3` vs `3` mean‑curvature tension between the two gauges in Step 73 should be resolved before the cusp‑matching asymptotics are used quantitatively; it affects the anisotropy decay rate (`e^{-2t}` forced vs `e^{-3t}` unforced) that any half‑core existence argument will rely on.

Net: both load‑bearing points hold. Part 1 is a correct construction of admissible anisotropic Koiso center data, with global half‑core existence and cusp flattening as the true unresolved content. Part 2 correctly identifies that the flux is sharp at `c/L` and cannot by itself close `P_n^+`; the exact missing input is a three‑annulus geometric‑decay estimate for the marginal quadratic TT mode, with the manuscript's `δL→1/6` fillings as the `θ=1` stress test.