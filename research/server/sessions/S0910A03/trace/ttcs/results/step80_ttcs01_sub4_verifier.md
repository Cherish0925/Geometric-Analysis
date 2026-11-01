# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step80_base_identity_verify.py",
    "Sessions/S0910A03/workspace/data/step80_base_identity.json",
    "Sessions/S0910A03/workspace/scripts/step80_joint_base_response.py",
    "Sessions/S0910A03/workspace/data/step80_joint_base_response_summary.json",
    "Sessions/S0910A03/workspace/data/step80_residual_atlas.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md"
  ]
}
```

## Task

Independently read and assess the Step 80 joint reflected-core finite-mode experiment for the Yau 26 negative graph-manifold route. Check (i) the invariant base equation and physical-coordinate source/measure corrections; (ii) whether the script really enforces the scalar-minus-six reflected center and projected Koiso second jet and evaluates all five Ricci components; (iii) what the paired shape-only versus joint base/area runs actually establish about compensation, especially the persistent residual layer near physical r≈0.2 and the fact that exit data become favorable while sup residual does not; (iv) identify any formula, parameterization, optimization, sampling, or interpretation error that would invalidate or sharply narrow the result. Derive the most informative next finite-mode or analytic test aimed at the inner compensation layer rather than the already solved exterior tail. Treat all numerical failures as finite-dimensional evidence, not a theorem.

## Output

## Verification memo — Step 80 joint reflected-core finite-mode experiment

### 1. The Ricci algebra, Koiso jet, and operator norm are correct

I re-derived the five orthonormal components `E0…E4 = (Ric+3g)` for
`g = dr² + e^{2a}dz² + e^{2b}dx² + e^{2c}dy²` and checked them against three exact configurations:

- **H⁴** (`a=b=c=r`): all five vanish. ✓
- **Flat base × warped orbit** (`b=b(z)`, `a=c=0`): the 2-plane `(z,x)` has Gauss curvature `K=−(b_{zz}+b_z²)`, giving `E_zz = E_x = 3 − b_{zz} − b_z²`, `E_y = E_rr = 3`, `E_rz = 0`. The formulas reproduce this exactly. ✓
- **Scaled hyperbolic tail** (`a=r`, `b=c=r−log N`): `E≡0`. ✓

The `step80_base_identity_verify.py` symbolic check independently confirms `E_rr, E_rz, E_zz` against the invariant base-tensor form `Ric(γ_B) − Hess σ − ½dσ² − ½ U*h + 3γ_B` (all three residuals exactly 0). Note that this symbolic file validates only the three base components; the two orbit components `E_x=E3`, `E_y=E4` are not covered there, but my hand-checks above verify them in the discriminating cases. The `exp(−a)` factor on `E1` is the correct coordinate→orthonormal conversion, and `exact_op` correctly returns `max(|½(tr±disc)|, |E3|, |E4|)` for the block-diagonal `E` (the base-orbit and `x–y` cross Ricci components vanish by the T² isometry plus the diagonal/reflection symmetry of `G`, so no component is omitted).

**The Koiso second jet is genuinely and correctly enforced.** I verified that setting `E3(0)=0` at a reflected center (`a_r=b_r=c_r=0`) gives `b_{rr}(0) = 3 + em(a_z b_z − b_z² − b_z c_z − b_{zz}) = Ric^{slice}_b + 3`, and likewise `a_{rr}(0)=Ric^{slice}_a+3`, `c_{rr}(0)=Ric^{slice}_c+3`. This is exactly `J2_raw`. In `fields()`, `car(0)=car'(0)=0`, `car''(0)=1`, `common(0)=0`, `common'(0)=0`, `common''(0)=(1,2,0)=basejet`, and the free modes vanish to third order in `r`; hence `L(0)=l0`, `L_r(0)=0`, `L_{rr}(0)=basejet+corr2=J2` are held as hard constraints independent of the optimizer. The construction is even in `r`, so reflection is exact. The scalar-minus-six center is imposed via the validated Step 69 Yamabe ODE `u''=¾u⁵−¼A²cos²z·u`, projected onto `KZ=4` Fourier modes (projection residual ≈0.011, visible as `op_max_z(r=0)=0.011`). All of this is sound.

The physical source/measure correction is also internally consistent: `d_r(e^{3r}v_r)+d_z(e^r v_z)=0` is exactly `v_{rr}+3v_r+e^{-2r}v_{zz}=0` (Step 73 tail), and `det(N^{-2}G)` gives the stated `σ→σ−2log N`. But `e^{3r}` is the weight of the **frozen tail gauge `a=r`**, not of the inner region where `a≠r`; the script labels it correctly, so no error, but it does not describe the inner-layer operator.

### 2. What the paired runs actually establish

Reading the data directly:

- Entry `operator_sup ≈ 14.6–15.4` for **both** variants at **all** `R∈{2,4,6}`; `joint/shape_only` sup ratio 1.008–1.05 (marginally worse), RMS ratio 0.89–0.94 (marginally better). The joint base/area freedom does not move the peak.
- The peak is pinned at physical `r≈0.2` for every run; the atlas shows `E` rising from ≈0.01 at `r=0` to ≈5 at `r=0.068` to ≈15 at `r=0.2`, then decaying below 1 by `r≈1`.
- The exterior is resolved: at `R=6`, `exit S−I sup = 0.006`, `intrinsic Ric sup = 0.0004`. This re-confirms the Step 73 tail, not a new result.
- The inner peak is `R`-independent because it lives in the fixed germ region; increasing `R` only lengthens the already-good tail. **This is the one solid qualitative conclusion the experiment supports: the exterior connector length is not the bottleneck; the inner turnaround at `r≈0.2` is.** It is consistent with the Step 75 center theorem (`λ_min(S'(0))≤−3+3δ`) and the Step 76 order-one center energy (the measured `orbit_stress_half_sup≈12.5`, `map_energy_sup≈25`).

### 3. Why the runs do not show that base/area compensation cannot reduce the inner layer

Three features of the parameterization and optimization prevent the "joint does not help" reading:

**(a) No run converged.** Every solver stage reports `nfev=85=MAX_NFEV` with "maximum number of function evaluations exceeded," for a 108-parameter (`shape_only`) to 324-parameter (`joint`) Gauss–Newton. The reported `operator_sup` is therefore an upper estimate of what the basis can reach, not a stationary value; `optimality` ranges 0.003–0.15 but the stop was the evaluation cap, not `ftol/xtol/gtol`.

**(b) The inner residual is dominated by jets above second order that the germ sets to non-Einstein values.** The fields are even in `r`, so odd jets vanish and `E(r)=½E''(0)r²+O(r⁴)`. `E''(0)` is fixed by the **fourth** jet `L⁗(0,z)`, which the cosh-common + carrier germ does **not** set to its Einstein value. From `∂_r²E_{rr}|_0=0` one gets the trace relation `a⁗+b⁗+c⁗ = −2(a_{rr}²+b_{rr}²+c_{rr}²)` at the center, and the remaining components fix the individual fourth jets from `z`-derivatives of the known second jet. The germ ignores this, so `E''(0)≈15/0.04≈4×10²` is a germ-truncation artifact. The free basis reaches `L⁗(0)` only through the `r⁴` tails of the local/global modes, and the identical fixed germ is shared by both variants — so the near-invariance of the `r≈0.2` peak across `shape_only`, `joint`, and `R` is partly forced by the shared germ, not by a compensation principle.

**(c) The interpretive ledger is not a clean measure.** `base_response_needed := (orbit_stress_half_sup > operator_sup)` compares 12.5 to 15 and returns `False`; this does not carry a compensation meaning. The paired ratios likewise mix an unconverged sup with an integrated RMS.

Net: the experiment conflates three distinct things — germ jet error above order 2, optimizer non-convergence, and the compensation question — and cannot separate them. It is *consistent with* an inner-layer obstruction (magnitude matches the order-one center energy, not a small defect), but it does not establish one. It also does not probe the regime that matters (`‖E‖→0`); at `‖E‖≈15` it is far from the asymptotic connector the Step 79 convex-distance maximum-principle argument concerns, and Step 75 (1.7) already forces the physical length to grow as the target defect shrinks — which fixed-`R`, fixed-germ runs cannot exhibit.

### 4. Most informative next test — the analytic even-jet cascade at the reflected center

Because the Einstein Cauchy problem in `r` is elliptic (formally solvable, analytically ill-posed), the decisive move is to compute the formal even-jet expansion exactly and thereby remove the germ-truncation contamination:

- Write `L(r,z)=Σ_k L_{2k}(z) r^{2k}/(2k)!` with `L_0` = Step 69 center, `L_2 = Ric^{slice}+3` (Koiso). Impose `E=0` order by order. Each even order determines `L_{2k}(z)` **explicitly** from `z`-derivatives and products of lower jets (algebraic in the top jet, with the `e^{-2a}` factor from `a''(0)`); no `z`-ODE is solved and periodicity is inherited automatically. Compute `L_4(z)` and `L_6(z)`.
- Rebuild the germ matching Einstein formally through `r⁶` (parameterize `L_4, L_6` coefficients directly rather than via the untuned cosh/carrier), then evaluate `E` on `r∈(0,0.4)`.

Two outcomes, both informative:
- If `E` on the inner interval collapses to `O(r⁸)`, the `≈15` residual was a truncation artifact and the inner layer has no formal obstruction — the real question is the *global* connection to the tail with `‖E‖→0`, which should then be tested by growing both the matched jet order `K` and the connector length `R` and watching whether `‖E‖` decreases.
- If the jet coefficients `L_{2k}(z)` grow super-geometrically or the anisotropy `v`-jets do not decay with `k`, that is a genuine local mechanism far stronger than any finite-mode residual, and it directly quantifies the transport problem.

A complementary analytic test, aimed at the transport rather than the jets: multiply the **forced** anisotropy equation `div(e^σ∇v) = −e^σ·(source in E)` by `v`, integrate over the reflected cylinder, and combine with the Step 75 (2.5) boundary-pairing identity to bound how much of the order-one center energy `⟨d_s²⟩_ρ≥12−8δ` must reappear at the exit for a given `‖E‖_∞`. This makes the Step 79 §8 maximum-principle question quantitative and is the sharp inner-layer statement, independent of any basis.

If a finite-mode run is still wanted, the minimal fixes so that it means something are: (i) parameterize the fourth/sixth center jets as free variables (or match them from the cascade above); (ii) refine the radial grid and add small-`ℓ` local modes (`ℓ` down to ≈0.05) so the `r∈(0,0.4)` layer is resolved; (iii) run the solver to genuine convergence (raise `MAX_NFEV` far above 85 and let `ftol/gtol` terminate); (iv) minimize an equalized per-point operator norm rather than the radial-`L²` functional, so the `r≈0.2` peak is actually targeted. Only after (i)–(iii) does a persistent inner peak carry evidential weight about compensation.

### 5. Summary

The Ricci algebra, Koiso second jet, scalar-minus-six center, five-component evaluation, operator norm, and physical-gauge source/measure factor are all correct and internally cross-checked. The runs correctly localize the difficulty to an `R`-independent inner turnaround layer near `r≈0.2` whose magnitude matches the order-one center energy — consistent with the Step 75/76 center results. They do **not** establish that base/area compensation cannot reduce that layer, because the fixed germ mis-sets all jets above order 2, the free basis has weak leverage there, the two variants share that germ, and no run reached convergence. The highest-information next step is the explicit even-jet cascade `L_4, L_6` at the reflected center, which cleanly separates germ truncation from optimization noise from the actual (global, `‖E‖→0`) connection question.