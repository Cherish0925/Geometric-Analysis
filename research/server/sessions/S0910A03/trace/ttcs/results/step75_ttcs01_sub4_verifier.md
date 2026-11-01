# TTCS Independent Branch Record

```json
{
  "step_id": 75,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/scripts/step69_collapsed_koiso_center.py",
    "Sessions/S0910A03/workspace/scripts/step75_core_entry_gauss_newton.py",
    "Sessions/S0910A03/workspace/data/step75_core_entry_gauss_newton_pilot.json",
    "Sessions/S0910A03/workspace/scripts/step75_germ_to_entry_search.py",
    "Sessions/S0910A03/workspace/data/step75_germ_to_entry_pilot.json",
    "Sessions/S0910A03/workspace/scripts/step75_center_shape_search.py",
    "Sessions/S0910A03/workspace/data/step75_center_shape_search_pilot.json",
    "Sessions/S0910A03/workspace/data/step70_ricci_T2inv.json"
  ]
}
```

## Task

Independently read the Step-75 full-residual computation as a mathematical numerical experiment. Check whether the Gaussian Ricci component formulas and orthonormal normalization in the active scripts match g=dr^2+e^{2a}dz^2+e^{2b}dx^2+e^{2c}dy^2; whether the validated Step-69 Yamabe sign and center data are used consistently; whether boundary bases really impose the center and exit jets described; whether all five independent Ricci components enter; and whether the reported locations and sizes support only the stated finite-spectral interpretation. Identify any concrete formula, normalization, basis, or inference error that would change the scientific reading. Also assess whether the center-shape computation supports approach to the exact lower value 3 within its sampled reciprocal-warp family, without treating it as proof of a global infimum.

## Output

## Verifier memo — Step-75 full-residual experiment and center theorem

I reconstructed the Ricci algebra, the orthonormal normalization, the Yamabe center, the radial/Fourier bases, and the reported quantities independently, and cross-checked the analytic Sections 2–3 against the SymPy tensor in `step70_ricci_T2inv.json`. The central finding: the five-component formulas, the normalization, the Yamabe sign, and the center/exit jet construction are all correct, and the reported numbers reproduce the JSON. The one substantive reading issue is not a formula error but the status of the optimizer output, discussed in point 6.

### 1. The five orthonormal components match the exact tensor

For `g = dr² + e^{2a}dz² + e^{2b}dx² + e^{2c}dy²` (identifying `t↦r`, `θ↦z` with `step70`), the SymPy `Ric` gives, after adding `3g` and dividing each component by its metric factor to reach the orthonormal frame:

- `E_rr = 3 − a_r² − a_rr − b_r² − b_rr − c_r² − c_rr` (weight 1), matches `E00`.
- `E_zz = 3 − a_r² − a_r b_r − a_r c_r − a_rr + e^{−2a}(a_z b_z + a_z c_z − b_z² − b_zz − c_z² − c_zz)` (divide `R_{θθ}` by `e^{2a}`), matches `Ezz`.
- `E_x = 3 − a_r b_r − b_r² − b_r c_r − b_rr + e^{−2a}(a_z b_z − b_z² − b_z c_z − b_zz)` (divide `R_{xx}` by `e^{2b}`), matches `Ex`; `Ey` is the `b↔c` image and matches.
- `E_rz = e^{−a}(a_r b_z + a_r c_z − b_r b_z − c_r c_z − b_{rz} − c_{rz})` (divide `R_{rz}` by `√(g_{rr}g_{zz}) = e^{a}`), matches `E0z`.

All five are correct, and the normalization factors (`1`, `e^{−2a}`, `e^{−2b}`, `e^{−2c}`, `e^{−a}`) are the right orthonormal rescalings. The `√2` multiplying `E_rz` in the least-squares vector is the correct symmetric-tensor weight (the off-diagonal enters twice in the Frobenius/operator content). This is the same algebra in both the JAX residual and the NumPy `intrinsic_ric` used for the reported quantities, so there is no residual-vs-report mismatch.

### 2. Operator supremum is legitimately the max eigenvalue magnitude

Because `x,y` are Killing, `E_{rx}=E_{zx}=E_{ry}=E_{zy}=0`, so `E` block-diagonalizes as the `2×2` `(r,z)` block `[[E_rr,E_rz],[E_rz,E_zz]]` plus the scalars `E_x`, `E_y`. The reported `operator_sup = max(|(tr±disc)/2|, |E_x|, |E_y|)` is exactly the operator norm of `Ric+3g` relative to `g`. Valid.

### 3. Yamabe sign and center data are used consistently

`h_f = dz² + e^{2f}dx² + e^{−2f}dy²` has `R_h = −2(f')²` (confirmed by the Section-3 formula `R_q = −2h'−|A|²−h²` with `h≡0`, `|A|²=2f'²`). The 3-dimensional conformal law gives `R_q = u^{−5}(R_h u − 8Δ_h u)`, so `R_q=−6` reads `−8u'' − 2(f')²u = −6u⁵`, i.e. `u'' = ¾u⁵ − ¼(f')²u`. Both `step69_collapsed_koiso_center.py` and the Section-4 statement carry this sign; the opposite-sign Step-74 variant is marked superseded. The Yamabe residual is at machine level. Consistent throughout the active scripts.

### 4. The center jet is exactly the Step-69 value, zero first jet, and the Koiso second jet

The free radial modes carry factors `x⁴e^{−x²}` and `s⁴T_j`, all vanishing to third order at `r=0`; the carrier `ρ` has `ρ(0)=ρ'(0)=0`, `ρ''(0)=1`; the `log cosh r` piece has value/first derivative zero and second derivative `1` at `0`. Hence `L(0)=` Step-69 center, `L_r(0)=0` (totally geodesic reflection), and `L_{rr}(0)=1+G = Ric_q+3I`. I verified `req = 1+Gval = Ric_q+3` from `Gcoef = center_ric+2`, and that setting `L_{rr}(0)=Ric_q+3` makes each center component vanish: e.g. `E_x(0)=(Ric_q^x+3)−b_{rr}` from the formula above, which is zero at the imposed jet. The reported `second_jet_error_sup ≈ 1.8e−15` and center component sups `≤3e−3` confirm this; the residual `~3e−3` is the `K_z=5` Fourier truncation of the Step-69 scalar-minus-six center (`center_scalar_projection_error ≈ 1.2e−3`), a truncation effect, not a formula effect.

The exit is genuinely free (`interface_weight=0`) or softly penalized toward `S→I` and intrinsic `Ric→0` (`interface_weight>0`); it is never pinned. This matches the "free exit flux" description, and it avoids the exactly-umbilic exit that Section 2 rules out. All five components enter the residual (`E00, √2 E01, E22, E_x, E_y`); no three-equation subsystem is used.

### 5. Reported locations and sizes reproduce the data

Core-entry residual-only `operator_sup = 16.027, 16.035, 15.964` for `R=2,4,6`; soft-entry `16.053, 15.989, 15.975`; `argmax_r ≈ 0.19`; at `R=6` soft, exit `|S−I|_∞=0.106`, intrinsic `Ric_∞=0.181`. Germ-to-entry residual-only `23.520, 22.124, 21.596`; soft `23.482, 22.863, 22.273`; `argmax_r` at the inner interface `0.15` (or `0.225`). Germ constraints `ham=0.00324`, `mom=0.00564`. Every one of these matches the note. The germ evolution `S_i' = Ric_i + 3 − H·S_i` is the correct reduced form of `E_x=E_y=E_zz=0` (I checked all three components against the tensor), with `E_rr`, `E_rz` carried as constraints whose drift to `t*=0.15` is the reported `~10^{-3}`.

### 6. What the operator suprema actually mean — the one point that changes the reading

Every solver row reports `"The maximum number of function evaluations is exceeded"` with `nfev = 75` (or `70`), i.e. the run stopped at the hard evaluation cap `MAX0`/`MAX1`, not at a stationary point (`optimality` at `R=2` is still `12.5`). Two consequences a reader should hold explicitly:

- The objective actually minimized is the physically-weighted `L²` residual (`sqrtw ∝ √(dr/R)`), which downweights the fine inner grid near `r≈0.19` where the `E_zz` cascade lives. Between the pure-carrier initialization and the stopped iterate the operator sup *rose* from `12.78` to `16.03` while the `L²` residual fell (`7.29→5.13`). So the `~16` is not a minimum of the operator sup and is not even a converged `L²` value; it is an incidental measurement at a capped iterate. The germ-run `~22` has the same status.

- Therefore the number `16` should not be read as a residual floor of the finite basis. It measures only that a short `L²`-weighted run with this basis left a large pointwise `E_zz` near the center. The note's phrasing — "did not resolve the center-to-expansion transition; it does not show that the transition is impossible" and "these finite failures have no nonexistence meaning" — is the correct reading and, if anything, is on the strong side of caution: nothing here even approximates a stationary configuration. A center-weighted objective and far more iterations would be needed before the finite basis could be said to have been tested against the inner cascade at all. This is the substance I would surface most, because it prevents mistaking `16`/`22` for a structural residual bound.

### 7. Section 2 (flux) and Section 3 (center theorem) are exact and correct

- Section 2: `div_{t,z}(e^σ∇d)=0` with `d_n=0` at the reflection center and `d_n=0` at an exactly orbit-umbilic exit forces `d≡const`; the induced core metric is then conformal to a flat `T³`, and `−8Δu=−6u⁵` integrated over `T³` gives `0 = −6∫u⁵ < 0`, impossible. Valid; this correctly rules out the exactly-umbilic exit and explains why the active runs keep `d_r(R)` free.

- Theorem 3.1: I reverified each step. `h=(log√det G)'` has mean zero; at a downward zero `h'≤0`, `R_q=−6` gives `|A|²=6−2h'≥6`; `A` traceless self-adjoint on a plane gives `K_orb=−det A=½|A|²≥3`; and in dimension three `R_q=2(K_{v e_1}+K_{v e_2}+K_orb)` yields `(Ric_q+3q)(v,v)=−K_orb≤−3`, hence `λ_min(Ric_q+3I)≤−3`. Since `S'(0)=Ric_q+3I` at a totally geodesic reflection center, some principal direction contracts with rate `≥3`. The small-defect refinement `λ_min(S'(0))≤−3+5δ` follows correctly: `(Ric_q+3q)(v,v)≤e−3≤−3+4δ` with `|e|≤4δ`, plus a further `δ` from `|E_T^♯|`. This is a genuine exact result, not a numerical one, and the note treats it as such.

### 8. The center-shape search does support approach to 3 within the sampled family, and correctly stops short of an infimum statement

Two clarifications for the reading. First, the objective is the max positive sectional curvature of the *Yamabe-rescaled* `q` (with `R_q=−6`), not of the flat seed `h`; the binding eigenvalue is the normal-direction `P_0=−K_orb`, consistent with (3.6). For the seed itself `h≡0` and `|A|²` is non-constant, but for `q` the mean curvature `h_q=4u'/u` is not identically zero, so the theorem's equality case (`h≡0`) does not occur and `K_orb>3` strictly at each finite amplitude — there is no contradiction with the seed being flat-fibered.

Second, the numbers do behave as approach-from-above to the proven lower bound `3`: single-mode `max K = 5.32, 4.33, 3.74, 3.28, 3.13` at `A=1,2,3,5,8`; three-mode optimum `3.033` (`P_component_min = [−3.033, −2.474, −2.474]`, so the orbit-normal sectional is the binding `3.033`). The Yamabe and scalar residuals are `~10^{-15}`, so these are faithful curvature values of exact `R_q=−6` metrics. This supports "the high-amplitude family approaches the sharp value 3" and "does not reveal a route to small initial shear," exactly as stated. It does not establish attainment of `3` or an infimum over all `T³` metrics (or even over the Fourier family), and the note disclaims both; the disclaimer is warranted because the trend flattens slowly (still `3.13` at `A=8`) and the search is finite-dimensional with a smooth `p=16` surrogate objective.

### 9. Open scientific substance

The exact center theorem is solid and it is the strongest new object here: it converts "the Step-69 seed happens to have large positive orbit curvature" into a structural statement about the whole `T²`-cohomogeneity-one center class. What the numerical Section 5 does not yet contain, and what would change the reading, is a computation that actually drives the inner `E_zz` cascade down — a center-weighted objective, resolved second/third jets, and iteration counts well beyond the current cap — so that one could distinguish "this finite basis cannot carry the center contraction into a small-defect exit" from "a short weighted `L²` run did not try to." As written, the runs establish neither existence nor nonexistence of the flux-carrying interface; they are consistent with the note's stated reading and with the exact obstructions in Sections 2–3, which are the parts carrying real mathematical force. The two exact identities that would most sharpen the program next are (i) whether `e^{2R}η + (δ/2)(e^{2R}−1) ≥ 3` (eq. 1.7) combined with the `λ_min(S'(0))≤−3+5δ` bound forces a definite growth rate of physical length with target defect, and (ii) whether the weighted flux `e^σ|∇d|²` energy from (2.2) can be made to vanish in the limit while `d_r(R)≠0` at each finite stage — the mechanism the note names as missing.