# Step 94 product branch: source-compatible next calculation

> **Step 95 correction:** A02 Step93 (#640) proved R^± = diag(1,0,0), NOT I/3.
> The product is NOT conformally flat. The "combined equation 1/3 + t² K_adj = 0"
> and critical scale t*² are WITHDRAWN. See `workspace/notes/step95_gauge_obstruction_and_kernel_plane.md`
> for the corrected obstruction structure.

## Current computed object

The corrected principal product-background pure odd adjacent response uses
\[
K_{ij}^{11,principal}
=\frac{\pi^2}{2}\sum_{e\in K\text{-odd}}
\frac{R_i(e)R_j(e)}{P_e\|e\|^2}.
\]
For receiver \(NN\) and an adjacent source:
\[
K^{AB}_{adj}\approx -0.03144249732,
\]
from Steps 91--92, and Step 94 gives
\[
K^{AA}_{NN,NS}\approx -0.00400249866,
\quad K^{BB}_{NN,NS}=0,
\]
\[
K^{AA}_{NN,SN}=0,
\quad K^{BB}_{NN,SN}\approx -0.00400249866.
\]
Thus the presently computed total principal adjacent value is
\[
K^{principal}_{adj}\approx -0.03544499598
\]
for the two adjacent directions from \(NN\), before applying node-exchange symmetries to all ordered adjacent pairs.

## Why this may already be the right principal source normalization

Step 89 proved the flat boundary identity
\[
S_{odd}(V_2)=\frac{\pi^2}{2}R_{odd}(H),\qquad V_2=\frac12H_{ijpq}x_px_q,
\]
using the Ozuch convention
\[
3\int_{S^3/\mathbb Z_2}\langle H^4_\pm,V_2\rangle.
\]
For the product insertion direction \(\zeta=\omega_2\), this exactly corresponds to the odd part of the Eguchi--Hanson asymptotic
\[
H^4(\zeta^+)=-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4}
\]
in Ozuch lines 283--321. Therefore, **under the assumptions** that the first obstruction \(\lambda_k\) vanishes at every node, \(H_2^4\) can be omitted in the boundary coefficient, and the K-equivariant slice preserves the Step 89 adjoint identity, the Step 94 sum is the physical principal off-diagonal odd response.

Those assumptions still require explicit checking in the actual product-orbifold chart.

## Next exact checks

1. **First obstruction at the product nodes.** In the product background, verify in the Ozuch convention that for insertion \(\zeta=\omega_2^\pm\), all \(\lambda_k^j=0\). This should follow because the curvature block is rank-one in the \(\omega_1\) direction, but it must be written with the same SD/ASD basis and orientation used for every node.

2. **Absence of \(H_2^4\) in the principal coefficient.** Ozuch line 638 says that when the relevant \(\lambda_k=0\), Lemma 2.3 allows plugging \(H_2^4=0\) into the boundary formula. Confirm this applies to the product row and not only to kernel projections onto compact obstruction modes.

3. **Node-frame transport.** Transport \(H^4(\omega_2^\pm)\), the sparse receiver, and the electric/magnetic tensor bases from \(NN\) to \(NS,SN,SS\). Establish that all eight ordered adjacent values are equal in the normalized radial variables, or record the exact signed matrix if not.

4. **Kernel and negative-mode projection.** K-symmetry eliminates K-even negative/zero modes for the pure odd source. Verify that the full Bianchi-projected singular source, cutoff, and product chart remain K-equivariant so no hidden even component enters the odd radial equation.

5. **Radial Kuranishi map.** Insert the normalized adjacent coefficient into
\[
\Delta_i=t_i\sum_jt_j^2(\varepsilon_i\varepsilon_j-1)K_{ij}^{11}
\]
for \(\varepsilon=(+,-,-,+)\). If all adjacent \(K_{ij}^{11}=K_{adj}<0\), then
\[
\Delta_i=-2K_{adj}t_i\sum_{j\sim i}t_j^2>0
\]
for positive scales. Determine whether any global deformation variable, scale-ratio term, or same-chirality calibration branch contributes at the same order and can cancel this sign. Without this finite-dimensional map, the coefficient sign is only a local obstruction/enabler signal.

## Relation to Yau--26

This product calculation concerns one local positive-Einstein desingularization branch on a candidate smooth four-manifold. It cannot by itself prove that \(\#_3(S^2\times S^2)\) has no Einstein metric, nor can it prove the all-dimensional Yau--26 proposition. Its value is that it turns a previously vague positive-collapse question into a concrete Ozuch-chart finite-dimensional calculation with a now-corrected principal adjacent coefficient.
