# Step 96: source-compatible kernel-plane map reconstruction for the product branch

Session `S0910A01`. Agent3 / Actuator. Phase Execute.

> **Step 97 repair.** Step 96's first local interpretation compared ordered `23` and `32` coefficients. The physical source variable is in \(\operatorname{Sym}^2(K)\), so the off-diagonal entry is the symmetrized `23/32` coefficient. After this correction the odd half-difference of the Ozuch \(H^4\) source satisfies \(S_{\rm odd}=\frac12R_{\rm odd}\) on all physical entries \(22,33,23_{\rm sym}\). The even source and individual plus/minus sources still contain components outside the simple odd receiver span. The regenerated `workspace/data/step96_kernel_plane_ab_map.json` and `workspace/data/step96_source_receiver_decomposition.json` are the current data.

## 1. Correction to the Step 95 interpretation

The Step 95 gauge identity
\[
R_{\rm odd}(\mathcal L_X g_0)=0
\]
remains useful and is retained. It says that a pure gauge change smooth at the receiving node cannot change the sparse odd receiver. It does **not** say that the singular Ozuch source is the whole adjoint of that receiver. The missing object remains a distributional identity
\[
P\bar h^4_{\rm phys}=c\,R_{\rm odd}^*+T,
\]
with extension, projection, and kernel normalization fixed. The term \(T\) is not removed by the gauge lemma unless it is gauge or its propagated receiver response vanishes.

The Step 95 mixed-row obstruction is therefore not carried forward as established. The correct object is the reduced kernel-plane map produced by the actual Eguchi--Hanson source
\[
H^4(\zeta^+)=-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4},
\]
polarized on \(\operatorname{Sym}^2(K)\), propagated by the projected product Green operator, and then evaluated by the receiving first-obstruction derivative.

## 2. Local H4 source versus receiver adjoint

The script `workspace/scripts/step96_source_receiver_decomposition.py` implements the Ozuch boundary source against a general homogeneous quadratic test tensor \(V_2=\frac12H_{ijpq}x_px_q\):
\[
\frac{S^+(\zeta,\zeta)}{\pi^2}=-\frac1{16}\sum_b
(C_{\zeta b})_{ij}(C_{\zeta b})_{pq}H_{ijpq},
\]
\[
\frac{S^-(\zeta,\zeta)}{\pi^2}=-\frac1{16}\sum_b
(C_{b\zeta})_{ij}(C_{b\zeta})_{pq}H_{ijpq}.
\]
This uses Ozuch lines 318--321 and 625--638 with the \(\mathbb{RP}^3\) boundary factor.

The corrected result is:

- On all physical kernel-plane entries,
  \[
  S_{\rm odd,22}=\frac12R_{\rm odd,22},\qquad
  S_{\rm odd,33}=\frac12R_{\rm odd,33},\qquad
  S_{\rm odd,23_{sym}}=\frac12R_{\rm odd,23_{sym}},
  \]
  with zero residual on the full 100-dimensional symmetric-Hessian basis.
- The ordered `23` and `32` residuals of size `0.125` recorded in the first run are coordinate artifacts; they cancel in the symmetrized off-diagonal coefficient.
- The even source components still have components outside the simple receiver span: for the diagonal entries the relative coordinate-basis residual is about `0.7527726527`; the symmetrized off-diagonal even entry is represented by `0.5 R_even,23sym` in this local basis.
- Individual plus/minus source components have residual relative size about `0.739` for the diagonal entries, while the symmetrized off-diagonal plus/minus entries are represented by `0.5 R^+_{23sym}` or `0.5 R^-_{23sym}` respectively.

Thus the odd physical source is cleaner than the first Step 96 note stated, but this does not restore the Step 95 scalar model. The complete \(H^4\) source still has even and individual-chirality components that must be propagated or eliminated by a real symmetry/projection argument.

Data: `workspace/data/step96_source_receiver_decomposition.json`.

## 3. AB-sector propagated sample of the full H4 source

The repaired script `workspace/scripts/step96_kernel_plane_ab_map.py` propagates the actual quadratic \(H^4\) source through the product AB one-form spectral sector. It keeps all source/receiver chiralities separate and only forms even/odd combinations after the raw maps are computed.

For receiver \(NN\) and adjacent source \(NS\), at \(\tau=0.01,L_{\max}=260\), the AB-sector compact maps in the basis
\[
(R_{22},R_{33},R_{23})\quad\text{versus}\quad(M_{22},M_{33},M_{23})
\]
are
\[
B^{AB}_{\rm even,even}=+0.03144249732
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix},
\]
\[
B^{AB}_{\rm odd,odd}=-0.03144249732
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix},
\]
with even--odd and odd--even blocks zero in this AB sector. The old Step 91 number is recovered as the single entry
\[
B^{AB}_{\rm odd,odd}(R_{22}\leftarrow M_{22})=-0.03144249732.
\]

For the other separated pair classes at \(\tau=0.02,L_{\max}=180\):

- \(NN\leftarrow SN\) gives the same adjacent AB map to displayed precision.
- \(NN\leftarrow SS\) gives
  \[
  B^{AB}_{\rm odd,odd}=+0.017726760721
  \begin{pmatrix}
  1&1&0\\
  1&1&0\\
  0&0&0
  \end{pmatrix},
  \]
  with the even-even block of opposite sign.

The all-compatible row constrains a complete sum over self, adjacent, opposite-corner, deformation, frame, and chart terms. It does not identify one adjacent even block with minus one adjacent odd block.

Data: `workspace/data/step96_kernel_plane_ab_map.json`.

## 4. Physical scale--angle reading of the AB map

Step 97 adds the geometric interpretation. A physical insertion is not an arbitrary matrix in \(\operatorname{Sym}^2(K)\), but
\[
M_j=t_j^2u_ju_j^T,
\qquad |u_j|=1.
\]
In trace/double-angle coordinates \((x,y,z)=(\operatorname{tr}M,M_{22}-M_{33},2M_{23})\), physical data obey
\[
x>0,\qquad y^2+z^2=x^2.
\]
The adjacent AB odd map is
\[
A^{AB}_{ij,\rm odd}(M_j)=-a\operatorname{tr}(M_j)I_K,
\qquad a=0.03144249732.
\]
Hence its unrestricted kernel is the traceless subspace, but this kernel contains no nonzero positive rank-one physical source. The AB sector is blind to angular anisotropy rather than geometrically ignorable: it contributes a nonzero scale-balance term for every nonzero bubble and no angular term.

At receiver direction \(u_i\), the reduced components are
\[
u_i^TA_i u_i\quad\text{and}\quad (u_i^\perp)^TA_iu_i.
\]
For the adjacent AB odd map these are \(-a t_j^2\) and \(0\), respectively. See `workspace/notes/step97_ab_physical_cone_interpretation.md` and `workspace/data/step97_ab_physical_cone_row.json`.

## 5. What the computation changes

The product calculation is now a finite-dimensional source problem
\[
\operatorname{Sym}^2(K_i)\longrightarrow\operatorname{Sym}^2(K_j)
\]
with a constrained physical cone \(M=t^2uu^T\). The \(H^4\) source is quadratic in the insertion direction and splits naturally into trace and double-angle variables. The odd source identity is exact after physical symmetrization, while even and individual source components still require full propagation.

The AB one-form sector is unusually simple: after propagation it has rank-one trace response and no angular output. It should not be extrapolated to the complete map. Tensor sectors, self finite parts, opposite-corner terms, frame/projector motion, deformation variables, and higher-order effects may be the source of angular equations.

## 6. Next executable mathematical work

1. **Trace-free tensor sectors with full H4 source.** Rebuild the AA/BB calculation using full jets of electric and magnetic tensor harmonics, not only sparse receiver values. Read the result by radial and angular components on \(M=t^2uu^T\).
2. **Node-frame transport.** Build explicit \(K_j\)-frame transport matrices for the four nodes and both chirality conventions, then transform each ordered block into common trace/double-angle variables.
3. **Full row equations.** Keep self, adjacent, and opposite-corner terms, plus deformation and projector/frame terms, until a symmetry or exact equation removes them. The checkerboard relative cancellation of odd self terms is useful, but it is not the all-compatible calibration.
4. **Remainder sharpening.** Use Ozuch's higher-order construction template to seek a projected expansion with a remainder below cubic order in the kernel-plane sector, or explicitly include any cubic logarithmic terms.

This product branch remains a local desingularization laboratory. It does not settle Einstein existence on the smooth resolution, and it is far from the full all-dimensional Yau--26 proposition.
