# Step 97: physical scale--angle interpretation of the AB kernel-plane map

Session `S0910A01`. Agent3 / Actuator. Phase Execute.

## 1. Repaired Step 96 artifact

The inherited syntax error in `workspace/scripts/step96_kernel_plane_ab_map.py` was caused by a duplicated stale fragment left after the Step 96 symmetrization repair.  The fragment has been removed.  The script now compiles and reruns successfully, regenerating

- `workspace/data/step96_kernel_plane_ab_map.json`.

The regenerated file now agrees with the corrected local source decomposition:

- after physical `23/32` symmetrization, the odd half-difference of the Ozuch `H^4` source satisfies
  \[
  S_{\rm odd}=\frac12 R_{\rm odd}
  \]
  on all three physical entries of \(\operatorname{Sym}^2(K)\), namely \(22,33,23_{\rm sym}\);
- the ordered `23` and `32` residuals of size `0.125` are coordinate artifacts, not physical off-diagonal source terms;
- individual plus/minus and even source components still contain components not represented by the simple odd receiver span, so the full finite-dimensional map still requires full Green propagation.

This agrees with `workspace/data/step96_source_receiver_decomposition.json`, whose final interpretation says exactly that the physical odd source identity holds on all \(\operatorname{Sym}^2(K)\) entries while even and individual chiral components remain outside the simple receiver span.

## 2. Physical source cone

The right source variable is not an arbitrary symmetric matrix.  A nonzero Eguchi--Hanson insertion at node \(j\) has a scale and direction
\[
 t_j>0,
 \qquad u_j=(\cos\theta_j,\sin\theta_j)\in K_j,
\]
and contributes
\[
 M_j=t_j^2 u_j u_j^T.
\]
In trace/double-angle coordinates
\[
 x=\operatorname{tr}M,
 \qquad y=M_{22}-M_{33},
 \qquad z=2M_{23},
\]
physical data obey
\[
 x=t_j^2>0,
 \qquad y=t_j^2\cos(2\theta_j),
 \qquad z=t_j^2\sin(2\theta_j),
 \qquad y^2+z^2=x^2.
\]
Thus the physical source space is the positive rank-one cone inside \(\operatorname{Sym}^2(K)\).  Linear kernels found by allowing arbitrary signed symmetric matrices need not correspond to any bubble configuration.  Conversely, singularity of an unconstrained transfer block is not by itself an obstruction to a physical gluing configuration.

Orthogonal transport of the kernel plane preserves this cone:
\[
 M_j=t_j^2u_ju_j^T\mapsto t_j^2(U_{ij}u_j)(U_{ij}u_j)^T.
\]
It preserves \(x\) and rotates or reflects the double-angle pair \((y,z)\,) according to the induced action on \(\mathbb{RP}^1\).  The full node-frame transport still has to be fixed in Ozuch/Biquard conventions, but the cone constraint survives any orthogonal convention.

## 3. AB-sector map on the physical cone

`workspace/scripts/step97_ab_physical_cone_row.py` reads the corrected Step 96 AB map and converts it to trace/double-angle coordinates.  For the adjacent pair `NN <- NS`, using the heat-regularized value at `tau=0.01, Lmax=260`, set
\[
 a=-K^{AB}_{\rm adj}=0.03144249732>0.
\]
The Step 96 compact odd--odd AB block is
\[
K^{AB}_{\rm odd,odd}
=-a
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix}
\]
in rows \((R_{22},R_{33},R_{23})\) and columns \((M_{22},M_{33},M_{23})\).  In trace/double-angle coordinates this becomes
\[
(X,Y,Z)^T=
\begin{pmatrix}
-2a&0&0\\
0&0&0\\
0&0&0
\end{pmatrix}
(x,y,z)^T,
\]
where \((X,Y,Z)=(\operatorname{tr}A,A_{22}-A_{33},2A_{23})\).  Equivalently,
\[
 A^{AB}_{ij,\rm odd}(M_j)=-a\operatorname{tr}(M_j)I_K.
\]
The even--even block has the opposite sign in this AB sector.  The script verified the matrix conversion exactly in the stored decimal data and sampled random physical insertions with maximum errors:

- cone residual \(|y^2+z^2-x^2|\le 1.8\times10^{-15}\),
- odd radial error \(\le 1.8\times10^{-18}\),
- odd angular magnitude \(\le 1.8\times10^{-18}\),
with the same scale for the even sign-reversed block.

## 4. Receiver radial and angular components

The receiving obstruction is not the whole symmetric block \(A_i\) by itself.  Given the receiver direction
\[
 u_i=(\cos\theta_i,\sin\theta_i),
 \qquad u_i^\perp=(-\sin\theta_i,\cos\theta_i),
\]
the projected first-obstruction variation has two components:
\[
 \text{radial component}=u_i^TA_i u_i,
 \qquad
 \text{angular component}=(u_i^\perp)^TA_i u_i.
\]
For the AB odd adjacent map,
\[
 u_i^TA^{AB}_{ij,\rm odd}(M_j)u_i=-a t_j^2,
 \qquad
 (u_i^\perp)^TA^{AB}_{ij,\rm odd}(M_j)u_i=0,
\]
for every source angle and receiver angle.  Therefore the AB one-form sector gives an angle-independent scale response.  It is blind to angular anisotropy, but it does not allow a nonzero physical insertion to hide in the traceless kernel, because \(\operatorname{tr}(M_j)=t_j^2>0\).

The unrestricted kernel \(\operatorname{tr}M=0\) is the two-dimensional traceless subspace of \(\operatorname{Sym}^2(K)\); its intersection with the positive rank-one cone is only the zero insertion.

## 5. Checkerboard relative AB row under adjacent identification

Using the Step 91 adjacent-node reduction and the AB odd map above, the mixed-minus-all-compatible adjacent AB contribution at receiver \(i\) is
\[
 t_i\sum_{j\sim i}(\varepsilon_i\varepsilon_j-1)\bigl(-a t_j^2I_K\bigr)u_i
 =2a\,t_i\sum_{j\sim i}t_j^2\,u_i
\]
for the checkerboard chirality vector \((+,-,-,+)\), since adjacent nodes have \(\varepsilon_i\varepsilon_j=-1\).  Thus
\[
 \mathrm{Radial}^{AB}_i=2a\,t_i\sum_{j\sim i}t_j^2,
 \qquad
 \mathrm{Angular}^{AB}_i=0.
\]
At equal scale this AB-sector relative radial piece is
\[
 4a t^3=0.12576998928\,t^3.
\]
This is only the AB sector under the adjacent exchange normalization.  It does not include AA/BB tensor sectors, self and opposite-corner finite parts, deformation variables, projector and frame motion, or the sharper Ozuch/Biquard asymptotic needed to compare cubic terms with the remainder.

## 6. What this changes for the next tensor computation

The AB calculation now has a precise role:

1. It supplies a nonzero scale-balance contribution for every nonzero physical bubble source.
2. It supplies no angular alignment condition.
3. It should be combined with tensor-sector and self/complement effects in radial/angular form, not as an unconstrained matrix census.
4. Tensor-sector calculations should be read by how they contribute to \(u_i^TA_i u_i\) and \((u_i^\perp)^TA_i u_i\) on the cone \(M_j=t_j^2u_ju_j^T\).

This preserves the useful part of the product-orbifold calculation while keeping it inside the active Yau--26 research: it may produce a rigorous local desingularization result or local obstruction for this orbifold branch, but it does not settle Einstein existence on the smooth resolution and does not address the all-dimensional Ricci-pinching proposition.

## 7. Artifacts

- Script: `workspace/scripts/step97_ab_physical_cone_row.py`
- Data: `workspace/data/step97_ab_physical_cone_row.json`
- Repaired script: `workspace/scripts/step96_kernel_plane_ab_map.py`
- Regenerated Step 96 AB data: `workspace/data/step96_kernel_plane_ab_map.json`
- Corrected local source decomposition: `workspace/data/step96_source_receiver_decomposition.json`
