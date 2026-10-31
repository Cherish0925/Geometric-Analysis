# Step 93: curvature correction and corrected kernel-plane target

Session `S0910A02`. Agent1 / Execute.

## 1. Error corrected

Step 92's note `workspace/notes/step92_ozuch_spectral_connection_and_transversality.md` contained a load-bearing false premise in §§2.5 and 3.1: it treated the product orbifold
\((S^2\times S^2)/\mathbb Z_2\) as conformally flat and wrote
\[
R^\pm=W^\pm+\frac{\Lambda}{3}I=\frac13 I \quad (\Lambda=1).
\]
This is wrong.  It contradicts both the elementary curvature computation and the session's older records (Steps 44, 45, 48--50, 64, 67--69, 77).

For the product of two constant-curvature surfaces with Einstein constant \(\Lambda\), choose an oriented orthonormal frame \((e_1,e_2,e_3,e_4)\), with \((e_1,e_2)\) tangent to the first factor and \((e_3,e_4)\) tangent to the second.  The curvature operator on \(\Lambda^2\) has eigenvalue \(\Lambda\) on \(e^{12}\) and \(e^{34}\), and zero on mixed planes.  Passing to the self-dual/anti-self-dual bases gives
\[
R^+=R^-=\operatorname{diag}(\Lambda,0,0).
\]
Since \(s=4\Lambda\), the Weyl blocks are
\[
W^\pm=R^\pm-\frac{s}{12}I
=\operatorname{diag}\left(\frac{2\Lambda}{3},-\frac{\Lambda}{3},-\frac{\Lambda}{3}\right).
\]
Thus \(W^\pm\ne0\); the product is not conformally flat.  For the positive mirror, \(\Lambda=1\), so \(R^\pm=\operatorname{diag}(1,0,0)\).  For the negative product mirror, \(\Lambda=-1\), so \(R^\pm=\operatorname{diag}(-1,0,0)\).

Two independent sanity checks: (i) an Einstein four-manifold with \(W=0\) has constant sectional curvature, while \(S^2\times S^2\) has zero sectional curvature on mixed planes; (ii) if the product node had invertible \((1/3)I\) obstruction, no nontrivial EH insertion would be possible even in the all-compatible \(r=0\) row, contradicting the known Kähler--Einstein del Pezzo control desingularization.

The computation is recorded in `workspace/scripts/step93_product_curvature_and_kernel_audit.py` and data `workspace/data/step93_product_curvature_and_kernel_audit.json`.

## 2. What this invalidates from Step 92

The following Step 92 interpretations are withdrawn:

1. The product mirror is not conformally flat.
2. The background obstruction is not \((1/3)I\).
3. There is no scale equation \(1/3+t^2K=0\) and no critical gluing scale \(t_*^2=-1/(3K)\) for the product mirror.
4. The ansatz \(\zeta_i=t e_1\) is invalid for the product-mirror obstruction problem: \(e_1\) is the Kähler/image direction of \(R^\pm\), not an allowed kernel direction.
5. The sign of A01's old scalar/e1 principal response should not be interpreted as an adjacent insertion racing against a positive \(I/3\) background.

I patched `step92_ozuch_spectral_connection_and_transversality.md` directly so later agents reading that file see the correction in place, and I marked `workspace/data/step92_ozuch_spectral_crossverification.json` as superseded in its interpretation.  The raw toy Ozuch matrix values in that JSON (eigenvalues \(+8,-4,-4\) for a single flat image) remain algebraically correct, but they were evaluated on the excluded \(e_1\) direction and do not decide the product mixed-row gluing question.

## 3. Corrected obstruction problem

The product mirror has a rank-one chiral curvature block.  Its first-obstruction kernel is the Kähler-orthogonal two-plane
\[
K=\ker R^\pm=\omega^\perp=\operatorname{span}\{e_2,e_3\}.
\]
Allowed EH parameters must be written
\[
\zeta_j=t_j\xi_j,
\qquad \xi_j\in K,
\qquad |\xi_j|=1,
\]
up to higher-order corrections.  The leading mixed-chirality equation is not a scale equation but an angular kernel-projection equation:
\[
\Pi_K\left(\sum_{i\ne j} t_i^2 Q_{ji}(\xi_i)\right)\Pi_K\xi_j=0,
\]
where \(Q_{ji}\) is the physical Ozuch/Biquard Green response produced by the source node \(i\), including the EH \(H^4\) source, Bianchi/gauge projection, quotient/isotropy normalization, and ordered frame transport.  For equal scales, the common scale cancels from the direction equation.

Therefore the decisive coefficient is a \(2\times2\) symmetric response form on \(K\) at each receiver.  In the diagonal balanced symmetry sector it may reduce to a one-variable angular function, but only after explicitly defining the residual group \(G_{sym}\), its node permutations, and its transports on the kernel planes; otherwise it remains a small vector system.  It is not a single number along \(e_1\).

## 4. Corrected outcome logic

A computed invariant-sector coefficient can decide a *nearby gluing branch* in either direction:

- If the restricted response is nondegenerate/no-kernel on the invariant directions, the selected mixed-chirality product-orbifold desingularization branch is obstructed.  This does **not** prove the smooth mixed row has no Einstein metric; it only rules out metrics arising near this degeneration and selected Ozuch branch.
- If the restricted response vanishes along an angular ray with nonzero angular derivative, equivariant gluing becomes plausible in the invariant sector and the diagonal balanced pattern becomes a serious candidate for a positive Einstein metric with \(\min(b_+,b_-)\ge2\).
- If symmetry makes the restricted response vanish identically, the next obstruction level must be computed.

The analytic caveat that remains is the scale of the known remainder.  The pattern-dependent inter-node term enters at order \(t_jt_i^2\), hence \(O(t^3)\) at equal scales, while the available necessary-equation remainder in the current record is only \(O(t^{5/2})\).  A coefficient computation is decisive only after an adapted higher-order/Ozuch §3.3 expansion or a precise \(G_{sym}\)-parity argument gives a projected \(t^3\mathcal C+o(t^3)\) expansion, with possible \(t^3\log t\) terms handled.  This should be the next A01/A02 cross-verification target.

## 5. Immediate next work

1. Send a correction to A01/A03 superseding the relevant parts of A02 messages #637/#639 and the old §2.5/§3.1 Step 92 framing.
2. Ask A01 to ensure its product-orbifold coefficient work is restricted to \(\omega^\perp\) and calibrated against the all-compatible \(r=0\) KE row before trusting any mixed-row number.
3. The next constructive task is to derive or compute the physical Ozuch/Biquard response form \(\Pi_K Q\Pi_K\) in an explicitly defined \(G_{sym}\)-invariant kernel-plane sector, including all pair/self/frame/complement terms, and simultaneously adapt the higher-order expansion so the projected remainder is below \(t^3\) (or its \(t^3\log t\) part is explicit).

No Yau--26 branch is solved by this correction.  It repairs the positive-branch target and prevents the group from pursuing a nonperturbative critical-scale artifact.
