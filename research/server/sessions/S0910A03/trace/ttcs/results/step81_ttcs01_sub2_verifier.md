# TTCS Independent Branch Record

```json
{
  "step_id": 81,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/data/step81_evolution.json",
    "Sessions/S0910A03/workspace/data/step81_contraction_analysis.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step78_rotating_eigenframe_barrier.md",
    "Sessions/S0910A03/workspace/notes/step80_joint_base_response_and_inner_layer.md"
  ]
}
```

## Task

Verify the following chain of results for the reflected Einstein evolution from T²-invariant constant-area centers on T³ with Ric=-3g:

1. ORBIT MATRIX PARAMETRIZATION: In SL(2,R)/SO(2) with metric ds²=(1/2)tr((M⁻¹dM)²), geodesic polar gives M=cosh(d)I+sinh(d)n(θ) with n=[[cosθ,sinθ],[sinθ,-cosθ]], n²=I. The metric is dd²+sinh²(d)dθ² (curvature -1). A rotating loop d=d*, θ=kz has energy k²sinh²(d*). Setting this to 12 gives R(q₀)=-6 for constant area.

2. S'(0) EIGENVALUES: The reflected Einstein germ has S(0)=0, S'(0)=Ric(q₀)+3I. For constant-area centers: the z-eigenvalue is -|A|²+3=-3 (universal). The orbit eigenvalues have trace 6 but split depending on k and d*. Numerical: k=2 gives orbit eigenvalues ≈(9.93,-3.93); k=8 gives ≈(18.09,-12.09). Derive the exact analytical formula for the orbit eigenvalues.

3. ANGULAR-SLIP ENERGY PRESERVATION: For the perturbation d=d*+εcos(k̃z), θ=k₀z+εB₀sin(k̃z)/k̃ with B₀=-(k₀/k̃)coth(d*), the H² speed² deviates from 12 by O(ε²) with coefficient ~20. Verify this cancellation analytically: what is the exact O(ε²) coefficient? Does the cancellation extend to the orbit Ricci components, not just the trace?

4. UNIVERSAL AVERAGE CONTRACTION: For ANY constant-area center with R(q₀)=-6: ⟨|A|²⟩=6, hence ⟨u'(0)⟩=-3. For non-constant area: ⟨u'(0)⟩=-3+⟨h²⟩. Is this derivation correct? What are the assumptions?

5. VII₀ COLLAPSE: The ODE evolution for the Bianchi VII₀ system shows finite-distance collapse at r≈0.3-0.4 for all k=2,...,8. The cascade is K>3→u'<0→a↓→K↑. Does this collapse persist in the z-dependent (non-VII₀) case? Specifically: if u'(0,z)=-3+O(ε²) everywhere (from result 3), can the z-dependent evolution avoid collapse through spatial redistribution?

6. IMPLICATIONS FOR GRAPH CONSTRUCTION: Does the collapse force O(1) Ricci defect near the center, preventing ||E||_∞→0? Or is there an escape through non-constant-area centers, non-OT geometry, or non-reflected metrics?

## Output

## Verifier memo — reflected Einstein evolution from T²-invariant centers on T³

I reproduced each item from the equations and cross-checked against `step81_evolution.json` and `step81_contraction_analysis.json`. Items 1, 2, and 4 are exactly correct and I supply the closed forms requested; item 3 is correct with one internal inconsistency in the stated perturbation and an exact coefficient I derive; items 5 and 6 are open, and I state precisely what is settled and what is not.

---

### Item 1 — orbit parametrization and the R(q₀) = −6 relation: correct

With `M = cosh d·I + sinh d·n(θ)`, `n(θ)=[[cosθ,sinθ],[sinθ,−cosθ]]`, one has `n²=I`, `tr n=0`, eigenvalues of `M` equal `e^{±d}`, so `det M=1` and `M⁻¹=cosh d·I − sinh d·n`. Writing `n'=∂_θ n`, direct evaluation gives `nn'=J`, `n'n=−J`, `n'J+Jn'=0`, and

`M⁻¹dM = dd·n + dθ·(cosh d sinh d·n' − sinh²d·J)`.

Using `tr n²=tr n'²=2`, `tr J²=−2`, `tr(n n')=tr(nJ)=tr(n'J)=0`, the invariant `(1/2)tr((M⁻¹dM)²)` collapses to `dd² + sinh²d·dθ²`, a space of curvature −1, and the cross term vanishes. A loop `d=d*`, `θ=kz` has `|∂_zU|²_{H²}=k²sinh²d*`.

The identification with `R(q₀)=−6` also holds. For the constant-area slice `q₀ = dz² + M(z)` on T³ (flat T² fibers, `det M=1`, mean curvature `H≡0`), the intrinsic scalar splits as `R(q₀)=R_{fiber} − |K|² − H² − 2∂_zH = −|K|²` with `K=½∂_zM`, and `|K|² = ½|∂_zU|²_{H²}`. Hence

**`R(q₀) = −½·(H² energy)`**, so energy `=12 ⟹ R=−6`.

I confirmed this on the diagonal model `dz²+e^{v}dx²+e^{−v}dy²`: direct diagonal-metric computation gives `R=−v'²/2`, `|∂_zU|²=v'²`, so `R=−½|∂_zU|²`. ✓

---

### Item 2 — S′(0) eigenvalues: correct, exact formula supplied

The germ relation `S(0)=0`, `S'(0)=Ric(q₀)+3I` follows from the tangential Einstein equation at a totally geodesic reflection face: `Ric_g^{tan}(0)=Ric(q₀)−S'(0)=−3q₀`.

**z-eigenvalue.** For `H≡0`, Raychaudhuri gives `Ric(q₀)(∂_z,∂_z)=−∂_zH−|K|²=−|K|²=−|A|²`. Since `|A|²=−R(q₀)=6`, the z-eigenvalue is `−|A|²+3=−3`, universal. ✓

**Orbit eigenvalues.** Because `H≡0`, `tr Ric_orbit = R − Ric_z = −6−(−6)=0`, so the orbit eigenvalues are `±L`. In the rotating orthonormal frame the slice Ricci is `diag(−K, L, −L)` with `K=6` at the center and `L=K coth d*`. Fixing area (`k²sinh²d*=12`, so `sinh d*=2√3/k`, `cosh d*=√(k²+12)/k`) gives the closed form

**`L = 6 coth d* = √3·√(k²+12) = √(3k²+36) = (k²/4) sinh(2d*)`,**
**orbit eigenvalues of S′(0) = `3 ± √(3k²+36)`.**

This matches `step81_evolution.json` across every recorded k:

| k | √(3k²+36) | data S_orbit_plus / minus |
|---|---|---|
| 1 | √39 = 6.245 | 9.2449 / −3.2449 |
| 2 | √48 = 6.928 | 9.9279 / −3.9279 |
| 3 | √63 = 7.937 | 10.936 / −4.936 |
| 8 | √228 = 15.10 | 18.088 / −12.088 |

The small residual at k=12 (formula 21.63 vs. data 21.59) tracks the discrete center's `Ric_zz=−5.989≠−6`, i.e. discretization, not a structural mismatch.

---

### Item 3 — angular-slip preservation: coefficient is exactly −20; one inconsistency to correct

Write `d=d*+ε cos(k̃z)`, `θ=k₀z + (osc)`, with the slip amplitude chosen to cancel the first variation. Setting the `cos(k̃z)` coefficient of `speed²` to zero requires the oscillation amplitude of `∂_zθ` to equal `−εk₀ coth(d*)`, independent of `k̃`. This is exactly Step 80's `B(0)=−(m/k̃)coth(d*)A(0)` applied to `θ=k₀z+εB₀ sin(k̃z)` with `B₀=−(k₀/k̃)coth(d*)` (so `∂_zθ` oscillation `= εB₀k̃ = −εk₀coth d*`).

**Correction to the perturbation as written.** The task's `θ = k₀z + εB₀ sin(k̃z)/k̃` carries an extra `1/k̃`; combined with `B₀=−(k₀/k̃)coth d*` it produces `∂_zθ` oscillation `−ε(k₀/k̃)coth d*`, which cancels the first variation only at `k̃=1`. All `slip_kt1_*` runs use `k̃=1`, so the tested data are consistent; the general-`k̃` statement needs the `sin(k̃z)` form without the `1/k̃`.

**Exact O(ε²) coefficient.** With the correct amplitude,

`speed² − 12 = ε²[ k̃² sin²(k̃z) − k₀²(cosh²d*+1) cos²(k̃z) ] + O(ε³).`

For the tested center (k₀=2 ⟹ `sinh d*=√3`, `cosh d*=2`, `cosh²d*=4`, k̃=1):

`speed² − 12 = ε²(sin²z − 20 cos²z)`,

so the extremal deviation is `−20ε²` (at cos²=1) and `+ε²` (at sin²=1). This reproduces `speed_sq_range=[11.99799, 12.0001]` and `dev_over_eps2≈20.09` at ε=0.01 exactly. It also propagates cleanly to the contraction rate: `u'(0,z)=3−½speed²=−3−½ε²(sin²z−20cos²z)`, mean `−3+4.75ε²=−2.99953`, matching `u_prime_mean=−2.9995`. The excess of `20.09` over `20` is the O(ε³/eps) higher-order piece (it grows monotonically in the `eps2_scaling` table: 20.09→20.18→20.45→20.88→21.62→22.36), consistent with a `−20ε² + O(ε³)` law.

**Does cancellation extend to the orbit Ricci components?** Partly. The base component `E_zz = 3 − ½ speed²` is a pure function of the energy, so it is preserved to O(ε²). The same slip amplitude also cancels the **first** variation of the tangential orbit stress at r=0 (Step 80 eq 7.3). What is *not* preserved: the second-order center terms and the radial evolution — `A''(0)=(k²−m²)A(0)≠0` — and the constant-`R=−6` condition at second order additionally fixes zero-mode and `2k̃`-mode responses in σ and the base conformal factor that the bare slip does not supply. So the preservation is first-order at the center for both trace and traceless parts, and does not by itself carry into the evolution.

---

### Item 4 — universal average contraction: correct, with the corrected splitting sign

`u'(0,z)=Ric_z(q₀)+3 = 3 − ∂_zH − |K|²`. Averaging over the circle kills `⟨∂_zH⟩`, so `⟨u'(0)⟩ = 3 − ⟨|K|²⟩`. Imposing `⟨R⟩=−6` with the **correct** decomposition `R=−|K|²−H²−2∂_zH` (both `|K|²` and `H²` enter with a minus sign — I verified this by direct diagonal computation and by the traced Gauss equation on the breathing model `dz²+e^{2φ}(dx²+dy²)`, where both give `R=−4φ''−6φ'²`) yields `⟨|K|²⟩ = 6 − ⟨H²⟩`, hence

**`⟨u'(0)⟩ = −3 + ⟨h²⟩`,  h = H = mean curvature of the orbit tori (= ∂_z log area).**

Constant area ⟹ `h≡0` ⟹ `⟨u'(0)⟩=−3`; `⟨|A|²⟩=6`. The breathing model checks numerically: `⟨φ'²⟩=1`, `⟨H²⟩=4`, giving `⟨u'⟩=−3+4=1`, equal to the direct value `−2⟨φ'²⟩+3=1`. The sign is `+`, i.e. moving curvature into area-breathing *reduces* the z-contraction and can even make the average positive. This agrees with the `conclusion` field `expansion_from_area: requires h_rms>√3` (from `−3+⟨h²⟩>0`).

Assumptions: (i) reflection face, `S(0)=0`; (ii) the germ relation `S'(0)=Ric(q₀)+3I`; (iii) flat T² fibers (T³ with free T² action); (iv) periodic z so `⟨∂_zH⟩=0`; (v) the average `⟨R⟩=−6` is the quantity fixed.

**One reconciliation for the data.** The `nonconst_c*` runs report `u_prime_mean` *more* contracting than −3 (−3.19, −3.75). These do not contradict item 4: they add area variation without re-fixing `⟨R⟩=−6`, so they increase total curvature rather than redistribute at fixed R. The clean test of the `−3+⟨h²⟩` mechanism — hold `⟨R⟩=−6`, move energy from orbit shape into area breathing — is a distinct computation and is what would exhibit the average expansion.

---

### Item 5 — VII₀ collapse vs. z-dependence: collapse verified; z-dependent persistence unresolved

The VII₀ ODE collapse is real in the data: for k=2, `H_min≈−5.3×10¹¹` at r≈0.362, `a_min≈1.85×10⁻⁴`, `K_final≈5.6×10²³`, `d_final≈19.1`; collapse radius drifts from ≈0.36 (k=2) down to ≈0.24 (k=8). The cascade `K(0)=6>3 ⟹ u'(0)=3−K=−3<0 ⟹ a↓ ⟹ K=2k²a⁻²sinh²d↑` is exactly the frozen-angular-momentum feedback of Step 78.

For the z-dependent (non-VII₀) case the situation is genuinely open, and item 3+item 4 sharpen *why*:

- Spatial redistribution at a **constant-area** center cannot alter the average initial contraction: `⟨u'(0)⟩=−3` is pinned by `⟨|A|²⟩=6`, independent of how the H² loop is arranged (item 4). Item 3 shows the pointwise value can be flattened to `−3+O(ε²)` but the mean stays `−3+O(ε²)`.
- What is *not* controlled by these center identities is the subsequent nonlinear evolution. The structural mechanism that could avoid collapse is the one in Step 79 §6: in the full weighted harmonic map to H² (target curvature −1) the angular current is redistributable via the conservation law `(e^σ sinh²d·ψ_i)_{,i}=0`, and the area equation `Δρ=6e^{2λ}ρ` (driven by Λ=−3) forces area growth that can dilute orbit-shape energy density. The angular-slip sign `A''(0)=(k²−m²)A(0)` shows a `k̃<m` mode bends toward smaller hyperbolic radius at the center — the direction that lowers K — but this is a first/second-order center statement, not an evolution.

No solution, and no computation, currently demonstrates either that the collapse persists in the z-dependent case or that redistribution defeats it. The `graph_route_status: blocked at center unless z-dependent escape exists` correctly records this state.

---

### Item 6 — implications for the construction: no obstruction and no construction is established

The finite-distance collapse does **not** rigorously force an O(1) center defect for the general problem. Two facts hold simultaneously:

1. The collapse is proven only inside the frozen VII₀ (fixed-helicoid, single-base-variable) ansatz, which the Step 78 barrier already isolates as special.
2. The persistent Step 80 numerical peak (`‖E‖_op,sup≈15` fixed at r≈0.2, independent of R) has explicitly identified non-geometric sources: only the second center jet is fixed while the exact fourth jet `w_i=D Ric[2p♭]_i−6p_i` is large (`‖w‖_sup≈149`, trace identity `Σw_i=−2Σp_i²` satisfied only to ≈1.85 because of the ≈1.2×10⁻³ scalar projection error); the objective is an averaged L² residual; the solves exhausted their iteration allocation; the grid gives no off-grid supremum; and the ansatz is diagonal-only, with no full H² angular/off-diagonal variable.

Consequently the memo-level reading is: neither an obstruction (`‖E‖_∞ ↛ 0`) nor a connector has been established. The open escape routes are concrete:

- **Non-constant-area centers** (item 4): `⟨u'(0)⟩=−3+⟨h²⟩` gives average expansion for `h_rms>√3` while keeping `⟨R⟩=−6`. This is a clean, untested mechanism that directly attacks the −3 pinning.
- **Full matrix (d,ψ) H² freedom** with the `k̃<m` angular slip, solved through order ≥6 on a separate inner domain with matched outgoing Cauchy data rather than a prescribed cutoff (the v2 cosh-cutoff splice produced `‖E‖≈73–87`, an artifact of the cutoff, not evidence about the germ).
- Non-OT and non-reflected metrics remain entirely unexamined.

The decisive object is the first O(1) layer after the center under a properly matched high-order germ and full angular freedom; the present evidence selects this question and answers neither side. And even a successful hyperbolic (Λ=−3) graph construction would leave the positive normalized branch and the all-dimension quantifiers of Yau 26 untouched.

---

### Summary of verification status

- Items 1, 2, 4: exact and correct; closed forms `orbit eig = 3±√(3k²+36)` (item 2) and `⟨u'(0)⟩=−3+⟨h²⟩` with `h=H` (item 4) confirmed analytically and against the data.
- Item 3: exact O(ε²) coefficient `−k₀²(cosh²d*+1) = −20` for the tested center, matching `dev_over_eps2`; the `1/k̃` factor in the stated perturbation should be removed (the consistent form is `θ=k₀z+εB₀ sin(k̃z)`, `B₀=−(k₀/k̃)coth d*`), and first-order cancellation of orbit stress holds at the center but not through the evolution.
- Items 5, 6: VII₀ collapse verified; z-dependent persistence and the graph construction remain unresolved, with the −3 center pinning and the non-constant-area/full-H² mechanisms delineating exactly where the question lives.