# TTCS Independent Branch Record

```json
{
  "step_id": 72,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/step72_vary_H2_free.py",
    "Sessions/S1003A01/workspace/scripts/step71_fibre_split.py",
    "Sessions/S1003A01/workspace/scripts/step71_fibre_test.py",
    "Sessions/S1003A01/workspace/data/step72/vary_H2_free_K6.json",
    "Sessions/S1003A01/workspace/data/step72/vary_H2_free_K8.json",
    "Sessions/S1003A01/workspace/data/step71/fibre_split_K8.json"
  ]
}
```

## Task

Independently examine the computational linear algebra in the Step-72 scripts and outputs for hidden subspace/projection mistakes. Focus on the anti-J degree-2 coefficient space (dimension 60), the rank-20 (dE0,dN1) constraints, degree-2 Hamiltonian gauge rank 35, the five-dimensional quotient, the construction of Wphys=(I-GG^T)Z2, and the least-squares lower corrections. Determine whether the output values support a genuine rank-five map to P6/P8 and nonzero radial row, or whether basis normalization, inconsistent constraints, or coordinate gauge could create it. State concrete additional checks that would distinguish these possibilities without requiring a full new formal theory.

## Output

## Verification Memo: Step-72 Linear Algebra and the Rank-5 Physical H₂ Map

### 1. Dimensional Arithmetic

The anti-J part of Sym²(ℝ⁴) is 6-dimensional. Degree-2 monomials in 4 variables number $\binom{5}{3}=10$. So the H₂ coefficient space has dimension $6\times 10=60$, consistent with the code's `T.size[2]`.

The output chain:

| Quantity | K=6 | K=8 |
|---|---|---|
| rank(A₂) = rank(dE₀, dN₁)\|_{H₂} | 20 | 20 |
| dim ker(A₂) = Z₂ | 40 | 40 |
| gauge rank (degree-2 Hamiltonian) | 35 | 35 |
| physical = 40 − 35 | **5** | **5** |

The relation 60 − 20 = 40 and 40 − 35 = 5 is arithmetically consistent. The gauge rank 35 matches the number of degree-4 homogeneous polynomials in 4 variables, $\binom{7}{3}=35$, which parametrize Hamiltonian vector fields $X=\Omega\,\nabla f$ of degree 3 whose symmetrized derivative $\text{sym}(\partial X)$ is a degree-2 anti-J metric perturbation. This count is geometrically correct for the Darboux-fixed setup: lower-degree diffeomorphisms ($f$ of degree $\leq 3$) are consumed fixing the origin, linear frame, and $H_1=0$ normalization, so degree-4 is the first gauge freedom acting on $H_2$.

The 5-dimensional quotient matches $\dim W^-(0)=5$: the anti-self-dual Weyl tensor at a point in 4D is a trace-free symmetric endomorphism of $\Lambda^-\cong\mathbb{R}^3$, giving 5 independent real parameters.

### 2. The Wphys Construction: Correctness and Subtleties

The code computes:
```
Pperp = I_{60} - G₂ G₂ᵀ
W = Pperp · Z₂
SVD(W) → keep columns with σ > 10⁻⁹ σ_max
```

This is valid **only if** gauge ⊂ ker(A₂), so that the 35-dimensional gauge subspace lies entirely inside the 40-dimensional kernel. The data confirms this: `A2_on_gauge_norm = 8.0e-15`, which is unit roundoff for 60-dimensional vectors of order 1. Geometrically, Hamiltonian diffeomorphisms preserve both the Einstein equation and the Nijenhuis tensor (they are biholomorphisms of $(M, J_0, \Omega)$), so their linearizations must lie in ker(dE₀) ∩ ker(dN₁).

One subtle point: `gauge_projection_residual = 9.7e-14` is labeled as `resid` in the gauge_basis function, which actually measures `‖B^T U - G_flat‖` (the anti-J projection fidelity), not the orthonormality of G₂. The SVD truncation `u[:,:r]` produces orthonormal columns, so G₂ᵀG₂ = I₃₅ exactly in floating point. The projection $P_\perp$ is thus a valid orthogonal projector.

**The 5 Wphys vectors are orthogonal to the gauge by construction.** The check `A2_on_Wphys_norm ≈ 5e-15` (K=8) confirms they also lie in ker(A₂).

### 3. Lower Corrections and the Least-Squares Solve

For each physical H₂ direction $a$, the code solves:
$$A_h \cdot h = -A_2 \cdot a$$
where $A = [dE_0; dE_2; \ldots; dE_{K-2}]$ is the stacked Jacobian of lower Einstein equations, $A_2$ is its restriction to the H₂ block, and $A_h$ is the restriction to higher blocks (H₄,…,H_K).

The relative residuals are:
- K=6: $3.0\times 10^{-15}$ (machine precision)
- K=8: $4.1\times 10^{-14}$ (near machine precision given larger condition numbers)

This confirms the lower Einstein system is consistent: for each physical H₂ perturbation, there exist unique (minimum-norm) corrections at higher orders that maintain all lower Einstein equations through order $K-2$.

**Important structural observation:** The response block norms show the corrections grow with degree (K=8: H₂ norm 2.24, H₄ norm 37.3, H₆ norm 6328, H₈ norm 6907). This geometric growth is expected from the recursive tower structure but means the linearization becomes less reliable at high orders for finite perturbations.

### 4. Is the Rank-5 Map to $P_K(E_K)$ Genuine?

The singular values of $J_R \cdot \text{Resp}$ (the 5-column response matrix mapped through the scalar compatibility projection) are:

- K=6: [5792, 5059, 3316, 3205, 2304] — all within a factor 2.5
- K=8: [206079, 113048, 80699, 55702, 42087] — all within a factor 5

The smallest singular value is well above zero with no gap suggesting a hidden near-rank-deficiency. The absolute scale grows with K (as expected: $P_K(E_K)$ involves $K$-th order derivatives).

The nonzero radial norm (165.6 at K=6, 522.6 at K=8) confirms the image is not confined to the "non-radial" subspace of the scalar target — the $\Delta^{(K-2)/2}$ moment (the U(2)-invariant component) is hit.

### 5. Cross-Consistency with fibre_split_K8 Data

From `fibre_split_K8.json`:
- S_top (H₄=H₆=0, only H₈ varies): rank_R = 28 with radial_norm ≈ 7.5e-10 ≈ 0
- S_gauge (lower jets in gauge only): rank_R = 28, radial_norm ≈ 3.6e-9 ≈ 0
- S_Nfixed (lower torsion fixed): rank_R = 69, radial_norm ≈ 3.0e-9 ≈ 0
- S_release_hi_only (H₆ free, H₄ fixed): rank_R = 83, radial_norm = 0.77

The vanishing radial norms in S_top, S_gauge, and S_Nfixed versus the nonzero radial norm in Step-72's H₂ variation (165.6 at K=6) highlight that **the radial scalar obstruction is accessed through H₂ perturbation, not through higher-order adjustments alone**. This is structurally consistent and not trivially explained by a coordinate artifact: if the rank-5 map were gauge, the radial component would vanish (gauge perturbations produce zero Einstein residual).

The Step-71 data shows that S_release_hi_only gives rank 83 (almost full 84) with nonzero radial norm 0.77, meaning releasing H₆ opens the radial direction. The Step-72 data shows H₂ perturbation (with all lower corrections) also opens it. These are consistent: both modify the lower jets that feed the coupled tower.

### 6. Potential Artifacts to Rule Out

**a) Incomplete gauge removal.** The gauge_basis function uses a specific symplectic form $\Omega$ (and tests both $\Omega$ and $\Omega^T$). If the code's $\Omega$ matrix doesn't match the Tower's Darboux convention, some gauge directions could be misidentified. The check `dN_on_gauge_norm ≈ 0` in fibre_split confirms that the identified gauge directions do not move the Nijenhuis tensor, consistent with them being genuine symplectomorphisms.

**b) E₀ using only anti-J components.** The Tower's `Evec` returns the Einstein equation in the 6-component anti-J basis. The full Einstein equation is a 10-component symmetric tensor. If the 4 "J-part" components of E₀ impose additional constraints on H₂ that are not captured, then ker(A₂) could be too large. However, for a Kähler deformation (H in anti-J), the J-part of the Einstein equation is automatically satisfied to first order (the linearized Einstein operator preserves the type decomposition), so using only anti-J components is correct.

**c) dN₁ might be redundant with dE₀.** If dN₁ imposed no constraints beyond dE₀, then rank(A₂) would be 6 (from E₀ alone), giving ker = 54, quotient = 54-35 = 19. The observed rank 20 means N₁ adds 14 independent constraints, reducing the quotient to 5. This 14-constraint count from the Nijenhuis condition is the key non-trivial ingredient. It would be worth verifying by computing rank(dE₀|_{H₂}) and rank(dN₁|_{H₂}) separately.

### 7. Concrete Additional Checks

**Check 1 — Separate constraint ranks.** Compute rank(dE₀|_{H₂}) and rank(dN₁|_{H₂}) individually. Expected: rank(dE₀) = 6 (all anti-J components independent), rank(dN₁) = 14 to 20 (with 14 new directions beyond E₀). If rank(dN₁) alone is already 20, the E₀ constraint is redundant. This distinguishes the geometric roles.

**Check 2 — λ-dependence.** Run at λ = −3, −7, −10. If rank stays 5 at all values, the result is structural. If it changes, the W⁻(0) interpretation needs refinement.

**Check 3 — Finite perturbation.** For one Wphys direction $a$, set $H_2(\varepsilon) = H_2^{(0)} + \varepsilon\, a$, re-solve the tower via Gauss-Newton, and measure $\|P_K(E_K)\|$ as a function of $\varepsilon$. The linearization predicts $P_K(E_K) = \varepsilon \cdot J_R a + O(\varepsilon^2)$. Comparing with the actual nonlinear value at $\varepsilon = 10^{-3}, 10^{-2}, 10^{-1}$ would test whether the 5 directions survive nonlinearly or are an artifact of the tangent approximation.

**Check 4 — Direct W⁻(0) extraction.** Compute the anti-self-dual Weyl tensor at the origin from the 5 Wphys directions. If each direction produces a distinct trace-free symmetric 3×3 matrix (i.e., the map H₂ → W⁻(0) has rank 5 on Wphys), this confirms the geometric identification and also provides a coordinate-free characterization independent of the tower machinery.

**Check 5 — Orthogonality audit.** Verify $\|G_2^T w_q\| < \epsilon_{\text{mach}}$ for each of the 5 Wphys columns $w_q$. This is implicitly guaranteed by construction but an explicit check guards against accumulated roundoff in the SVD chain.

### 8. Assessment

The rank-5 result is consistent across K=6 and K=8, matches the geometric prediction $\dim W^-(0) = 5$, has well-conditioned singular values with no near-degeneracy, survives gauge removal, and produces a nonzero radial component in the scalar target. The dimensional arithmetic (60 − 20 = 40, 40 − 35 = 5) is correct and geometrically grounded. The lower correction residuals are at machine precision. No indication of a hidden projection or normalization error is visible in the outputs. The cross-check with fibre_split data shows consistent radial behavior.

The most informative single additional computation would be **Check 3** (finite perturbation), as it simultaneously tests whether the linearization is accurate, the gauge removal is complete, and the rank-5 image persists nonlinearly.