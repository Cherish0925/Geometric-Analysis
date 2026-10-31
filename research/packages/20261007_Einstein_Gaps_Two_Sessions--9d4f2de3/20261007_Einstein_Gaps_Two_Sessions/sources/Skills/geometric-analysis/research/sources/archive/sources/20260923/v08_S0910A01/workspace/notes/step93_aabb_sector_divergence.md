# Step 93: AA/BB trace-free sector divergence and the limits of the principal spectral approach

> **Step 94 correction.** This note is superseded as a conclusion about the principal product-background AA/BB response. Step 93 used the electric norm \(\mu(\mu-2)/2\) for the full-Lie magnetic tensor even though \(L_{(*df)^\#}g\) has twice the pole amplitude and four times the norm. After correcting this normalization, the separated-pole tensor electric and magnetic contributions cancel mode by mode, so the claimed \(BB_{NS}/AA_{SN}\) coincident divergence is not intrinsic. The corrected result is recorded in `workspace/notes/step94_corrected_aabb_and_route_reassessment.md`, `workspace/scripts/step94_corrected_aabb_principal_response.py`, and `workspace/data/step94_corrected_aabb_principal_response.json`.

Session `S0910A01`.  Agent2 / Constructor.  Phase Execute.

## 1. Summary

The AA/BB trace-free tensor sectors of the product-orbifold chirality-odd Green coefficient have a **coincident-point divergence** that prevents independent sector-by-sector computation.  The AB sector (Step 92) remains the only cleanly computable sector in the principal Step 89/91 normalization.

The following Step 93 interpretation is now withdrawn: the apparent divergence is a relative electric/magnetic normalization artifact, not a demonstrated structural consequence of the TF tensor spectral gap. The raw receiver reduction and pole-selection rules remain useful, but the divergence conclusion below should be read only as a record of the superseded computation.

## 2. Receiver reduction for AA/BB modes

For an AA mode $h=\phi_B\, T_A$ (TF tensor on $S^2_A$, scalar on $S^2_B$) in product normal coordinates with $\{0,1\}$ tangent to $A$ and $\{2,3\}$ tangent to $B$:
$$
h_{03}=h_{12}=h_{23}=0,\qquad h_{01}=\phi_B\,T_{01}.
$$
The sparse odd receiver $R_{\rm odd}=\frac12(H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01})$ reduces to a single surviving term:
$$
R_{\rm odd}(h)=\frac12(\nabla_2\nabla_3\phi_B)(0)\cdot T_{01}(0).
$$
Similarly, for BB modes $h=\phi_A\,T_B$:
$$
R_{\rm odd}(h)=\frac12(\nabla_0\nabla_1\phi_A)(0)\cdot T_{23}(0).
$$
This uses the Step 91 result that frame, Hodge, normalization, and background-curvature variations contribute no additional term.  Verified on the full 100-dimensional basis of symmetric Hessians.

Data: `workspace/data/step93_aabb_tensor_sector_analysis.json`.

## 3. Electric and magnetic pole-selection rules

At a pole, only $m=2$ modes have nonzero off-diagonal Hessians.  The two TF polarizations select complementary $m=2$ types:
- **Electric** (scalar TF Hessian $T=(\nabla^2f)^{\rm TF}$): $T_{01}\neq0$ only for sine $m=2$ modes.
- **Magnetic** (Lie derivative $T=\operatorname{sym}\nabla(*df)$): $T_{01}\neq0$ only for cosine $m=2$ modes.

Both have the same rough eigenvalue $\ell(\ell+1)-4$ and the same $L^2$ norm $\|T\|^2=\mu(\mu-2)/2$ from a unit-norm scalar $f$.

## 4. The coincident-point divergence

For the NS adjacent pair (receiver at $NN$, source at $NS$):
- **AA sector**: tensor on $A$ at same pole $N$ (both receiver and source), scalar on $B$ at different poles $N,S$.  The separated $B$-factor provides alternating signs from $(-1)^{\ell_B}$.  Result: $K^{AA}_{NS}\approx-0.002$, **convergent and finite**.
- **BB sector**: tensor on $B$ at different poles $N,S$, scalar on $A$ at **same** pole $N$.  The coincident $A$-factor gives a divergent sum.  Result: $K^{BB}_{NS}\to\infty$.

The divergence rate is captured by the dimension-raising identity:
$$
\partial_x^2 p_t^{S^2}(x)\big|_{x=1}=4\pi^2 e^{-6t}p_t^{S^6}(1)\sim\frac{1}{16\pi t^3}\qquad(t\to0).
$$
Verified to $10^{-15}$ relative precision.  Data: `workspace/data/step93_aabb_analytic_divergence.json`.

## 5. Why the reorganized integral still diverges

Following the TTCS qualification, I attempted a reorganized computation using factor heat kernels.  The idea was that $\Phi(t)=\partial_x^2 p_{t/2}(1)\sim t^{-3}$ (divergent) times $\Psi(t)$ (containing the separated antipodal kernel, expected to vanish as $t\to0$) might yield an integrable product.

The factor-resolved tensor-norm-weighted sum is:
$$
\Psi(t)=\frac{3}{16\pi}\sum_{\ell\ge2}(-1)^\ell(2\ell+1)e^{-t\mu_\ell/2}
=\frac34p_{t/2}^{S^2}(-1)-\frac{3}{16\pi}+\frac{9e^{-t}}{16\pi}.
$$
As $t\to0$: the heat-kernel part $p_{t/2}(-1)\to0$ exponentially, but the correction terms approach:
$$
\Psi(t)\to -\frac{3}{16\pi}+\frac{9}{16\pi}=\frac{3}{8\pi}\approx0.1194\neq0.
$$
These corrections come from subtracting the absent $\ell=0,1$ modes.  On $S^2$, trace-free tensors exist only for $\ell\ge2$; the $\ell<2$ spectral gap means the off-diagonal suppression that makes the full scalar heat kernel vanish between antipodal points does not apply to the TF tensor sector.

Consequently the product $\Phi(t)\Psi(t)\sim 0.12\cdot t^{-3}$ is **not integrable** at $t=0$, and the reorganized integral diverges.  This was verified numerically: the integral over $[\varepsilon,10]$ grows as $\varepsilon\to0$.

Data: `workspace/data/step93_aabb_reorganized_integral.json`.

## 6. Structural interpretation

The divergence has a clean mathematical meaning:

1. The full product Green function $G_P(x_i,x_j)$ between separated nodes is smooth.  The **total** sum over all eigenmodes converges because the complete spectrum provides cancellation at separated product points.

2. The **AB sector** sum converges independently because both factor evaluations involve separated points (antipodal poles in each $S^2$).  This is why $K_{\rm adj}^{AB}<0$ is a well-defined quantity.

3. The **AA/BB sector** sums diverge because one factor involves coincident-point evaluation.  The spectral decomposition introduces an artificial coincident-point singularity that the full Green function does not have.  The $\ell<2$ gap in the TF tensor spectrum prevents the off-diagonal suppression from compensating.

4. The **trace sector** ($h=f\,g_A$ or $f\,g_B$) has $R_{\rm odd}=0$, so it contributes nothing to the odd coefficient.

Therefore:
$$
K_{\rm adj}^{\rm total}=K_{\rm adj}^{AB}+K_{\rm adj}^{AA+BB},
$$
where $K_{\rm adj}^{AB}<0$ is finite and proved, but $K_{\rm adj}^{AA+BB}$ is not independently computable as a convergent spectral sum.  The sign of $K_{\rm adj}^{\rm total}$ cannot be determined from the AB sector alone.

## 7. Consequences for the research program

The AB sign theorem ($K_{\rm adj}^{AB}<0$, Steps 91--92) is the **strongest result obtainable from the principal spectral approach** to the product-orbifold chirality-odd coefficient.  Advancing further requires:

(a) **Working with the full Ozuch/Biquard source structure**: The ALE Eguchi–Hanson $H^4$ multipole has a specific tensor structure that determines the physical combination of sectors.  The Bianchi/gauge projection may regulate the AA/BB divergence by prescribing a finite-part extraction.

(b) **Computing $K_{\rm adj}^{\rm total}$ without sector decomposition**: Using the Ozuch boundary pairing formula directly, which involves a boundary integral of the second jet of $H^4$ against the background Green kernel — not individual sector sums.

(c) **Bounding the regulated $K^{AA+BB}$ relative to $K^{AB}$**: If a structural argument can show that the Ozuch-regulated AA/BB contribution is smaller than $|K^{AB}|$, the total sign would be determined.

## 8. Peer context

A02's Step 90 "triple disjointness theorem" (#625, #627) establishes that every orbifold+ALE resolution automatically satisfies the Sambusetti inequality (Chern–Weil neutrality + BCG).  This means:
- The product-orbifold desingularization program is separated from the negative branch.
- On the positive side, the analytic desingularization coefficient is the sole remaining obstruction/enabler.
- On the negative side, the connector construction on $N\#N$ (A03's forced Bochner) is the decisive tool.

A03's Step 85--86 (#618, #621, #624) develops the forced Bochner comparison and coupled energy bootstrap for non-warped OT connectors, aiming for a universal threshold.

## Files

- `workspace/scripts/step93_aabb_tensor_sector_analysis.py` → `workspace/data/step93_aabb_tensor_sector_analysis.json`
- `workspace/scripts/step93_aabb_divergence_diagnosis.py` → `workspace/data/step93_aabb_divergence_diagnosis.json`
- `workspace/scripts/step93_aabb_analytic_divergence.py` → `workspace/data/step93_aabb_analytic_divergence.json`
- `workspace/scripts/step93_aabb_reorganized_integral.py` → `workspace/data/step93_aabb_reorganized_integral.json`
- TTCS: `trace/ttcs/results/step93_ttcs01_verifier1_integration.md`
