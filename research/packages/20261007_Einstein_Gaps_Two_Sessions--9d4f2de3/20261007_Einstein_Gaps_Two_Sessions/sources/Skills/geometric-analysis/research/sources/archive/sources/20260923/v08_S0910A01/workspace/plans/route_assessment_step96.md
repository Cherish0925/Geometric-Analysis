# Route assessment: Step 96, repaired in Step 97

## Corrected product-branch status

1. On the local cover of `(S^2 x S^2)/Z2`,
   \[
   R^+=R^-={\rm diag}(1,0,0),
   \]
   so allowed Eguchi--Hanson directions lie in the kernel plane `K=span{e2,e3}`.

2. The Step 95 gauge lemma remains valid and useful:
   \[
   R_{odd}(\mathcal L_X g_0)=0
   \]
   for smooth vector fields at the receiver. It removes pure-gauge ambiguity in sparse odd receiver values, but it does not identify the full Ozuch source with that receiver adjoint.

3. The Step 95 mixed-row obstruction theorem is withdrawn. The correct object is a source-compatible kernel-plane map with physical source constraint `M=t^2 u u^T`.

## Repaired Step 96 evidence

- `workspace/scripts/step96_source_receiver_decomposition.py` and `workspace/data/step96_source_receiver_decomposition.json` implement the actual Ozuch `H^4` boundary source on the 100-dimensional space of symmetric Hessians. After the TTCS/Step 97 symmetrization repair, they show:
  - the odd source identity holds on all physical entries: `S_odd=(1/2)R_odd` for `22`, `33`, and `23sym`;
  - the ordered `23`/`32` residuals are coordinate artifacts and not physical double-angle failures;
  - the even and individual plus/minus source components still contain residual components outside the simple odd receiver span.

- `workspace/scripts/step96_kernel_plane_ab_map.py` now reruns successfully and regenerates `workspace/data/step96_kernel_plane_ab_map.json`. For adjacent `NN <- NS`, the AB sector map at `tau=0.01` has rank-one diagonal structure:
  \[
  B^{AB}_{even,even}=+0.03144249732\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix},
  \quad
  B^{AB}_{odd,odd}=-0.03144249732\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix},
  \]
  in the compact `(R22,R33,R23)` by `(M22,M33,M23)` representation; mixed even/odd blocks vanish in this restricted sector.

## Step 97 interpretation added

`workspace/scripts/step97_ab_physical_cone_row.py` and `workspace/data/step97_ab_physical_cone_row.json` convert the adjacent AB block to physical scale--angle variables. With `a=-K_adj^AB=0.03144249732>0`, the odd adjacent map is
\[
A^{AB}_{ij,odd}(M_j)=-a\,\operatorname{tr}(M_j)I_K.
\]
For physical \(M_j=t_j^2u_ju_j^T\), \(\operatorname{tr}(M_j)=t_j^2>0\) unless the bubble is absent. Therefore the traceless kernel of the unrestricted AB block contains no nonzero physical insertion. The AB sector supplies an angle-independent scale response and no angular response.

Under the checkerboard adjacent identification, the AB part of the mixed-minus-all-compatible row contributes
\[
\mathrm{Radial}^{AB}_i=2a\,t_i\sum_{j\sim i}t_j^2,
\qquad
\mathrm{Angular}^{AB}_i=0.
\]
At equal scale this is `0.12576998928 t^3` per receiver. This is one sector only, not the complete reduced equation.

## Implications

- A scalar adjacent coefficient is not enough, but the AB rank-one block is not useless: on the physical cone it is a genuine nonzero scale term.
- Angular alignment must be supplied or constrained by AA/BB tensor sectors, self and opposite-corner finite parts, deformation variables, frame/projector motion, or higher-order terms.
- The all-compatible del Pezzo KE row calibrates the complete equation, not an individual adjacent pair. Do not infer `K_even=-K_adj` from it without reconstructing the full row.
- The existing Ozuch necessary estimate has an `O(t_max^(5/2))` remainder, above the `O(t^3)` inter-node signal for comparable scales. A cubic coefficient becomes decisive only after a projected expansion with smaller remainder or explicit cubic-log terms.

## Next high-value work

1. Complete AA/BB tensor-sector propagation with the full `H^4` source and evaluate radial/angular components on `M=t^2u u^T`.
2. Build explicit node-frame transport matrices and residual symmetry representation for the four nodes and both chirality conventions.
3. Assemble the full finite-dimensional row equations retaining all source classes until exact symmetries remove them.
4. Study Ozuch's higher-order expansion mechanisms to obtain a projected remainder below cubic order in the kernel-plane sector.
5. Keep the restricted IL negative theorem as the mature independent Yau-26-adjacent line; product work remains a local desingularization laboratory, not a resolution of the global proposition.
