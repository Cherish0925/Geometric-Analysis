# Step 93: TTCS audit of the corrected kernel-plane target and A01 Step 95

Session `S0910A02`. Agent1 / Execute.

## 1. What is now solid

The Step 93 curvature correction is independently verified by direct computation, older session records, A01 Step 95, A03 reply #643, and TTCS verifier `trace/ttcs/results/step93_ttcs01_verifier1_integration.md`.

For the product Einstein metric on \(S^2\times S^2\), with \(\operatorname{Ric}=\Lambda g\),
\[
R^+=R^-=\operatorname{diag}(\Lambda,0,0),
\qquad
W^\pm=\operatorname{diag}\left(\frac{2\Lambda}{3},-\frac{\Lambda}{3},-\frac{\Lambda}{3}\right).
\]
For the positive mirror \(\Lambda=1\); for the negative product mirror \(\Lambda=-1\).  The quotient does not alter the local cover curvature.  Therefore the old Step 92 claim \(R^\pm=(\Lambda/3)I\), the \(1/3+t^2K=0\) critical-scale story, and the \(e_1\)-axis ansatz are withdrawn.

The correct leading first-obstruction kernel is
\[
K_j=\ker R^{\epsilon_j}=\operatorname{span}\{e_{2,j},e_{3,j}\}.
\]
A more invariant wording is useful: in the standard complex orientation \(e_1^+\) is the product Kähler form, while \(e_1^-\) is the parallel form obtained after reversing one factor's complex structure.  It is safer to call \(e_1^\pm\) the rank-one parallel/image direction, and \(K_j=(e_1^{\epsilon_j})^\perp\), rather than saying both are literally Kähler directions.

## 2. What A01 Step 95 adds

A01 Step 95 claims and records:

1. A gauge-invariance theorem for the sparse odd receiver:
   \[
   R_{\rm odd}(\mathcal L_Xg_0)=0
   \]
   for all smooth vector fields \(X\) on the product.  The proof uses product structure and \(\nabla\operatorname{Rm}=0\) to reduce the relevant second jet to third derivatives of \(X\), which cancel in
   \[
   \tfrac12(H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}).
   \]
   A01's data verifies this algebraically/numerically.

2. An SO(2)-equivariance claim for the bilinear spectral response on the kernel plane: the computed bilinear receiver is isotropic, so the diagonal entries in \(e_2,e_3\) agree and the cross term vanishes.

3. A conditional mixed-chirality obstruction: calibrate an even response by the all-compatible KE row, infer \(K_{even}+K_{adj}=0\), then for the mixed row get \(K_{even}-K_{adj}=-2K_{adj}\ne0\).

Items (1) and the curvature part of (2) look valuable and should be preserved as inputs.  Item (3) is not yet theorem-grade; it depends on several assumptions that TTCS flagged and that the current files do not close.

## 3. TTCS verifier's main cautions

The TTCS integration gives a useful adversarial framing:

### 3.1 Prop. 2.10 is not directly the receiver block

Ozuch Proposition 2.10 gives a boundary pairing that controls global kernel projections and construction of \(\bar h^4\).  The node-to-node \(2\times2\) block is obtained only after solving for the global projected field \(\bar h_i^4\), expanding it at receiver node \(j\), extracting its regular second jet, and inserting that jet into the first-obstruction formula.  It is unsafe to identify the boundary integral itself with \(\Pi_KQ_{ji}\Pi_K\).

### 3.2 Do not pre-delete same-chirality pair contributions

The local EH near-field has chirality splitting, but Green propagation through the curved compact product and the chosen slice can mix how the regular receiver jet appears.  The all-compatible KE row calibrates the full sum, not each ordered node pair separately.  Until a preservation/vanishing theorem is proved, the correct projected equation must include
\[
\sum_{i\ne j} B_{ji},
\]
not only opposite-chirality sources.  A01's gauge theorem may remove some gauge/Bianchi ambiguity in the odd receiver, but it does not by itself prove every same-chirality physical kernel block is zero.

### 3.3 Do not claim a one-angle equation before writing the group representation

On each \(K_j\cong\mathbb R^2\), the projected equation generally has radial and angular components
\[
f_{rad}=\langle F_j,\xi_j\rangle,
\qquad
f_{ang}=\langle F_j,J\xi_j\rangle.
\]
It reduces to one scalar equation only after specifying the actual symmetry group, node permutations, and frame-transport matrices \(U_{\gamma,j}:K_j\to K_{\gamma j}\), then proving one component vanishes or is dependent.  The notation \(D_8\times K\) is also confusing because \(K\) denotes the kernel plane; use \(G_{sym}\) for the residual symmetry.

### 3.4 The lower-order obstruction terms must be closed

Current record still has gaps at the same order or above the desired coefficient:

- \(\mu_1=0\) follows from the rank-one determinant formula, but \(\mu_2,\mu_3\) still need a direct Biquard/Ozuch formula check or an equivalent invariant argument.
- The global \(\nu_l\) equations and any orbifold deformation variable \(v_2\) must be solved or shown to vanish in the chosen equivariant sector.
- The kernel projection itself moves at order \(t_i^2\) because the receiver frame and rank-one image line change under the regular jet; this projector/frame correction is of the same order as the target coefficient.
- The full third-order term can include self-node, chart, frame, complement-solution, nonlinear, and \(v_2\) terms, not only pairwise Green response.

### 3.5 Remainder ordering is still the bottleneck

The mixed inter-node term is \(O(t_jt_i^2)\), hence \(O(t^3)\) at equal scale, while the existing crude Ozuch necessary equation in our record only has an \(O(t_{max}^{5/2})\) remainder.  Since \(t^3=o(t^{5/2})\), a nonzero three-order coefficient does not decide existence/nonexistence unless one proves an expansion
\[
\Pi_{K_j}\mathfrak F_j=t^3\mathcal C_j+o(t^3)
\]
(or includes any \(t^3\log t\) terms explicitly).  Merely saying the residual symmetry is equivariant is not enough; the lower-order projected residuals must vanish identically in the invariant kernel directions or the approximation must be sharpened.

The full TTCS branch records emphasize that Ozuch §3.3 provides a real higher-order-template rather than a mere hope: Proposition 3.14 and Corollary 3.25 build improved Einstein-modulo-obstruction metrics using higher jets (\(\bar h^4,\bar h^8\), ALE expansions, and obstruction-cancellation lemmas) and give smaller residual controls in the mixed-scale \(T^4/\mathbb Z_2\) context (source lines 986--990, 1244--1246, 1281--1284).  This cannot be imported verbatim to the positive product orbifold without adapting the background, kernel-plane projection, and scale conventions, but it is the most concrete route for pushing the projected remainder below the cubic inter-node term.  The next analysis should therefore combine coefficient computation with an adapted §3.3-style high-order expansion, not rely only on unproved parity annihilation of the old \(O(t^{5/2})\) remainder.

## 4. Corrected mathematical target

A formulation that avoids the current overclaims is:

Fix all nodes \(j\), chiralities \(\epsilon_j\), rank-one image lines \(L_j=\mathbb R e_{1,j}^{\epsilon_j}\), kernel planes \(K_j=L_j^\perp\), orbifold charts, ordered frame transports, and the projected inverse/slice for \(P_{g_o}\).  For \(\zeta_j=t_j\xi_j\), \(\xi_j\in K_j\), prove a projected obstruction expansion
\[
\begin{aligned}
\Pi_{K_j}\mathfrak F_j={}&
 t_j^2\Pi_{K_j}\boldsymbol\mu_j(\xi_j) \\
&+t_j\Pi_{K_j}\left[DR_j(v_2)+\sum_{i\ne j}t_i^2 Q_{ji}(\xi_i)+\mathcal S_j^{(2)}\right]\Pi_{K_j}\xi_j
+\mathcal R_j,
\end{aligned}
\]
with \(\mathcal R_j=o(t_{max}^3)\) in the chosen equivariant sector, or with the full \(t^3\log t\) structure displayed if present.  Here \(\mathcal S_j^{(2)}\) denotes self-node, chart, frame/projector, complement-solution, and nonlinear terms at the same physical order.

Subtasks:

1. Directly prove \(\Pi_{K_j}\boldsymbol\mu_j(\xi_j)=0\) for \(\mu_2,\mu_3\), not only \(\mu_1\).
2. Solve or eliminate all relevant \(\nu_l\) and \(v_2\) equations in the symmetry sector.
3. Compute the complete physical \(B_{ji}=\Pi_{K_j}Q_{ji}\Pi_{K_j}\), with all pair contributions retained until a vanishing theorem removes them.
4. Calibrate the entire third-order response on the all-compatible degree-4 del Pezzo KE row; use it to fix normalizations, but do not infer pairwise identities unless symmetry proves them.
5. Specify the residual group \(G_{sym}\), node permutations, and \(K_j\)-frame transports; then reduce the projected system to its actual invariant finite-dimensional form.
6. Adapt Ozuch §3.3's higher-jet construction, or otherwise prove lower-order/remainder cancellation, to make the \(t^3\) coefficient decisive with an \(o(t^3)\) projected remainder.

## 5. Relation to A01's conditional obstruction

A01's conditional obstruction is plausible as a heuristic if all of the following hold: the bilinear odd response is the whole physical kernel-plane response in the relevant sector; same-chirality and even terms are calibrated only through the scalar relation \(K_{even}=-K_{adj}\); the all-compatible row fixes the response in a way that transfers signwise to the mixed row; and all lower-order/remainder terms vanish in the invariant sector.  These are exactly the points that remain to be proved.

Therefore the current honest status is not yet "mixed desingularization obstructed".  It is: **the product-mirror mixed branch has been reduced to a sharply formulated kernel-plane third-order obstruction problem, with A01 providing a promising gauge-invariant odd receiver and isotropic bilinear component, but the physical coefficient and decisive remainder ordering remain open.**

## 6. Negative-side update from A03 Step 88

A03 Step 88 strengthens the negative connector side within a restricted symmetry class: reflection is no longer needed for the complete free-\(T^2\) orthogonally transitive cylinder with two exact outward-expanding ends.  A weighted-length minimizer in \(\widehat\gamma=\rho^2\gamma_B\) gives an invariant minimal \(T^3\) separator and the exact average identity
\[
\langle e_s\rangle=12-2\langle D\rangle+2\langle |II|^2\rangle+\langle h^2\rangle\ge 12-8\delta.
\]
Combined with the Step 87 resolvent ceiling this gives the same \(\delta<0.246249763690668\) obstruction in the complete free-OT two-outward-end class.  The scope remains correctly limited: it does not touch the diffuse non-OT/non-warped \(S^3\)-neck mechanism for \(N\#N\).

## 7. Files and evidence

- Curvature audit: `workspace/scripts/step93_product_curvature_and_kernel_audit.py`, `workspace/data/step93_product_curvature_and_kernel_audit.json`.
- Correction note: `workspace/notes/step93_curvature_correction_and_kernel_plane_target.md`.
- Patched Step 92 note: `workspace/notes/step92_ozuch_spectral_connection_and_transversality.md`.
- TTCS verifier: `trace/ttcs/results/step93_ttcs01_verifier1_integration.md` with branches `step93_ttcs01_sub1_verifier.md`, `step93_ttcs01_sub2_verifier.md`; branch 2 particularly points to Ozuch §3.3 (Prop. 3.14, Cor. 3.25) as the high-order remainder template.
- A01 Step 95: `Sessions/S0910A01/workspace/notes/step95_gauge_obstruction_and_kernel_plane.md`, `Sessions/S0910A01/workspace/data/step95_gauge_invariance_and_bridge.json`.
- A03 Step 88: `Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md`.
