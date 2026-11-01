# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/data/step93_aabb_tensor_sector_analysis.json",
    "Sessions/S0910A01/workspace/data/step93_aabb_analytic_divergence.json",
    "Sessions/S0910A01/workspace/notes/step92_route_comparison_and_ab_heat_sign.md",
    "Sessions/S0910A01/workspace/data/step91_receiver_simplification.json",
    "Sessions/S0910A01/workspace/data/step91_corrected_spectral_ledger.json"
  ]
}
```

## Task

Verify the Step 93 finding that the AA/BB trace-free tensor sectors of the product-orbifold chirality-odd Green coefficient have a coincident-point divergence that prevents independent sector-by-sector computation, while the AB sector remains finite and has a strict negative sign.

The specific claims to check:
1. For an AA mode h = phi_B(x_B) T_A(x_A) where T is a TF symmetric 2-tensor on S^2_A, the sparse odd receiver R_odd(H) = (1/2)(H_{01,23} - H_{03,12} - H_{12,03} + H_{23,01}) reduces to a single term R_odd = (1/2)(d_2 d_3 phi_B)(0) * T_{01}(0), because h has no components with tensor indices crossing factors.
2. Electric TF tensor (from scalar TF Hessian) has T_{01}(pole) != 0 only for m=2 sin modes; magnetic TF tensor (from Lie derivative of coexact 1-form) has T_{01}(pole) != 0 only for m=2 cos modes.
3. For the NS adjacent pair (receiver NN, source NS), the BB sector has the scalar factor on A evaluated at the SAME pole (N) in both source and receiver, creating a coincident-point spectral sum that diverges.
4. The divergence is characterized by the dimension-raising identity: d_x^2 p_t^{S^2}(x)|_{x=1} = 4*pi^2 * e^{-6t} * p_t^{S^6}(1), giving short-time behavior ~ 1/(16*pi*t^3).
5. By contrast, the AB sector uses d_x p_t^{S^2}(-1) = 2*pi*e^{-2t}*p_t^{S^4}(-1) which is finite for t>0, so the AB adjacent sector K_adj^AB converges and is strictly negative.
6. The implication that the full inter-node coefficient requires the ALE source normalization from Ozuch's framework and cannot be extracted from a naive sector-by-sector mode sum.

Check whether the receiver reduction for AA/BB is correct, whether the divergence diagnosis is real (not a normalization error), and whether the dimension-raising identities are applied correctly.

## Output

## Verifier Memo — Step 93 AA/BB coincident-point structure and AB sign

I worked through each of the six items against the receiver algebra, the ladder numerics, and the heat-kernel identities. The arithmetic and the structural reasoning hold together, and the identification of the AA/BB divergence as an artifact of naive per-mode summation (rather than a real singularity of the physical inter-node coupling) is sound. Details below, plus the substance that is not yet settled.

### 1. Receiver reduction for AA/BB — correct

Reading `H_{ij,pq}` as the second jet `∂_p∂_q h_{ij}(0)`, the reduction follows directly. An AA mode `h = φ_B(x_B) T_A(x_A)` populates only `h_{01} = φ_B T_{01}` (indices 0,1 = factor A; 2,3 = factor B). In the sparse receiver `R_odd = ½(H_{01,23} − H_{03,12} − H_{12,03} + H_{23,01})`:
- `H_{01,23} = T_{01}(0)·(∂_2∂_3 φ_B)(0)` survives (derivatives in B directions act on the B scalar);
- `H_{03,12}, H_{12,03}` need the crossing components `h_{03}, h_{12}`, which vanish for a pure AA mode;
- `H_{23,01}` needs the BB component `h_{23}`, which vanishes.

So `R_odd = ½ T_{01}(0)(∂_2∂_3 φ_B)(0)`, and by factor exchange `R_odd = ½ T_{23}(0)(∂_0∂_1 φ_A)(0)` for BB. This is exactly the JSON's single-surviving-term statement. The one input I take from Step 91 is the sparse identity itself; that file records 0 mismatches over the 100-dimensional symmetric basis, so I accept it.

### 2. Electric via sin(2φ), magnetic via cos(2φ) — consistent with the C/S/J algebra

The off-diagonal pole value `T_{01}` is nonzero exactly when the tensor's derivative matrix is S-type `[[0,1],[1,0]]`. In pole Cartesian coordinates, `cos2φ·r² = x²−y² → C = diag(1,−1)` and `sin2φ·r² = 2xy → S`. For the electric (TF Hessian of scalar) tensor the derivative matrix equals the scalar Hessian, so `T_{01}≠0` requires the sin mode. For the magnetic (coexact-1-form / Lie-derivative) tensor the derivative matrix is `JH`, and with `JC=S`, `JS=−C` from Step 92, the cos mode maps to S-type and gives `T_{01}≠0`. This matches "electric via s2, magnetic via c2." Trace removal only touches diagonal entries, so it does not disturb `T_{01}`; that step is clean.

### 3. Coincident-point divergence — real and geometrically coherent

The identification is not a normalization slip, and the ladder numerics settle this. With receiver fixed at NN and source at NS/SN/SS, the divergent sector is exactly the one whose *scalar* factor (the one carrying the two receiver derivatives) sits at a shared pole:

- NS (source A at N, B at S): BB carries `∂_0∂_1 φ_A` at coincident A → diverges; AA carries `∂_2∂_3 φ_B` at antipodal B → finite.
- SN: mirror — AA diverges, BB finite.
- SS: both factors antipodal → both finite.

The numbers confirm this precisely. NS `K_AA` is stable at `−0.00202768950…` to ~10 digits across τ = 0.1→0.005 (Lmax 60→280), while `K_BB` climbs 0.386 → 188.1. The SN ladder is the exact swap, and SS gives both `≈ −0.00087`, finite. A uniform normalization error would not produce this AA↔BB asymmetry keyed to the shared pole. Moreover the growth rate is right: `K_BB` roughly quadruples per halving of τ (46.55→188.08, ×4.04), i.e. `K_BB ~ τ⁻²`, which is exactly the once-integrated form of a `t⁻³` coincident-point singularity. This is internally consistent to a degree that makes the identification convincing.

### 4. Dimension-raising identity — verified numerically and structurally

`d_x² p_t^{S²}(1) = 4π² e^{−6t} p_t^{S⁶}(1)` matches to relative error ~1e-16 across four t values. It is also consistent with the Gegenbauer derivative ladder: `∂_x C_l^{(ν)} = 2ν C_{l−1}^{(ν+1)}` shifts `n→n+2, l→l−1`, and the eigenvalue difference `l(l+n−1) − (l−1)(l+n) = n` gives the factor `e^{−nt}` per derivative. Two derivatives from `S²` therefore give `e^{−2t}·e^{−4t} = e^{−6t}` and constant `(2π)² = 4π²`. The short-time leading term checks twice over: from the identity, `4π²(4π t)^{−3} = 1/(16π) t⁻³`, and from the direct fit, `ratio_aabb_to_pred → 1` as t→0 (0.998 at t=0.002). Both routes give `1/(16π t³)`. This item is solid.

One point to confirm from the scripts: the machine-precision agreement demonstrates the identity only if `direct_spectral` (the `S²` second-derivative series) and `dimension_raising_prediction` (the `S⁶` coincident kernel) are computed by genuinely independent code paths. If both internally reduce to the same `S⁶` sum, the check is circular. The JSON does not show the code; worth a glance at the step93 script to confirm two distinct summations.

### 5. AB finite and strictly below zero — sound

The sign argument is valid. After the exact `m=2` polarization cancellation (the `+,−,+,−` pattern with mode-by-mode equal amplitudes), the residual is the `m=0` coexact–coexact double series, and the heat chain gives `B(s) = −16π² e^{−s} p^{S⁴}_{s/2}(−1)`. The chain checks: at `x=−1`, `Δ = 2∂_x`, so `∂_t p^{S²}(−1) = 2∂_x p^{S²}(−1) = 2·2π e^{−2t} p^{S⁴}(−1) = 4π e^{−2t} p^{S⁴}(−1)`, hence `B(s) = −16π² e^{−s} p^{S⁴}_{s/2}(−1)`. Strict positivity of `p^{S⁴}_{s/2}(−1)` is the heat-kernel positivity on connected `S⁴` (strong maximum principle), so `B(s)<0`; `A(s)>0` termwise; the integrand is positive and the prefactor `−π²/32` is minus, giving `K^{AB} < 0`. The numerical `−0.0314` and the finite antipodal first-derivative column (`AB_finite: true`, values decaying to ~1e-15) are consistent. The sign here is robust to any positive rescaling of the normalization.

### 6. Implication (ALE source needed; naive mode sum insufficient) — correct interpretation

The divergence lives in a *within-node* (coincident-factor) evaluation, not in the genuine inter-node coupling, which uses the Green function between distinct nodes and is smooth. The naive full harmonic sum reinstates a self-energy-type singularity that the localized ALE source (Ozuch's `H⁴`, with fixed finite multipole content) would regulate. The AB sector escapes because its structure pairs separated points (antipodal in both factors) even at the naive level. So the correct reading is: the method must inject the localized source profile before summing; the divergence marks the place where completeness-of-harmonics overcounts.

### What is not yet settled (substance to carry forward)

- **The total coefficient's sign is not determined.** The AB value `−0.0314` and the whole computation are in the "principal" normalization, not Ozuch's `H⁴` normalization. The AB *sign* survives positive rescaling, but the *relative weight* of AB against a properly regulated AA/BB is unknown. The regulated AA/BB contributions could be finite of either sign. The research question — whether the symmetric desingularization branch carries a nonzero obstruction — needs the regulated AA/BB, not the divergent naive versions. The present result establishes one sector's sign, not the total.

- **"Only cleanly computable sector" is a statement about the naive method.** It is accurate that AB is the sole sector computable by direct per-mode summation, but this does not make AB the physical answer; it makes the AA/BB path require the finite source before it can be summed.

- **Contribution-column bookkeeping.** In `low_degree_NS`, `R_rec·R_src/(P·quotient_norm)` gives −0.0119 for the (l_A,l_B)=(2,2) AA electric row versus the listed −0.01158 (~2.5% apart), suggesting an extra amplitude/degeneracy factor enters the contribution formula. This is a minor point, but the exact contribution formula should be reconciled with the heat-weighted ladder sum so that the low-degree table and the convergent `K_AA = −0.00203` use the same weights. Note the raw low-degree contributions grow with l_B (−0.012, +0.050, −0.126, …); convergence of `K_AA` relies on the antipodal-B heat suppression `e^{−sμ}`, which is absent from the raw table — so the table is display-only, not a convergence witness.

- **Sign-parity field.** The `sign_pattern` field tracks `−(−1)^{l_B}` for NS (antipodal B parity) and swaps for SN, which is exactly the expected antipodal-factor parity and reinforces the geometric identification. The separate `parity_check_lA/lB` fields are just `(−1)^l` labels; they do not multiply into `sign_pattern` by a single rule, so do not read them as the driver of the sign.

Overall: items 1–6 hold. The AA/BB coincident-point divergence is a genuine feature of the naive per-mode method with the correct geometric fingerprint (keyed to the shared pole, mirror-symmetric under factor exchange, `τ⁻²` growth consistent with a `t⁻³` core), and the AB sign `K^{AB}<0` is a valid sector result. The unresolved mathematical object is the regulated AA/BB contribution under Ozuch's localized `H⁴` source, without which the sign of the full adjacent Green coefficient — the quantity that would actually bear on the desingularization branch — stays open.