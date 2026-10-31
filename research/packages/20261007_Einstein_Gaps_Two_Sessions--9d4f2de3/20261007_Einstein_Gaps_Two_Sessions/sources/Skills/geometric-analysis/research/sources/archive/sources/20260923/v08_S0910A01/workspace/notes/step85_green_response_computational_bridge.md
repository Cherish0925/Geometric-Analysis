# Step 85: computational bridge toward the product Green-response coefficient

Session `S0910A01`. Agent3 / Actuator. Phase Execute.

## 1. Purpose and correction of the execution target

The Step 84 angular calculation is useful, but it is not the mixed-row obstruction coefficient.  The coefficient that matters has the form
\[
  c_{ij}^{\epsilon_i\epsilon_j}=L_i\,G_{P}^{\perp}\,S_j^{\epsilon_j},
\]
where:

- \(S_j^{\epsilon_j}\) is the normalized, gauge-compatible multipole source created by the bubble at source node \(j\), including the flat \(H^4\) singular model, cutoff/matching correction, Bianchi correction, and projection away from the compact orbifold kernel;
- \(G_P^\perp\) is the pseudo-inverse of Ozuch's compact product operator
  \(P=\frac12\nabla^*\nabla-\mathring R\), not a product of one-factor Green functions and not a scalar pole value;
- \(L_i\) is the receiving radial curvature-jet functional at node \(i\), with the receiver frame and EH radial-kernel normalization fixed.

Thus a spectral numerator has the actual form
\[
  \sum_\alpha \frac{(L_i\psi_\alpha)\,\langle S_j^{\rm opp}-S_j^{\rm same},\psi_\alpha\rangle}{\lambda_\alpha},
\]
with zero modes separated and the negative shape/scale directions handled in the full inverse.  The Step 84 value \(8/3\) is the identity-transfer/local angular Gram control obtained by replacing this spectral transfer by a pointwise Frobenius pairing.  It is not evidence by itself that \(c_{\rm opp}\ne c_{\rm same}\).

## 2. Source and receiver factors derived from the Ozuch \(H^4\) algebra

Using the SD/ASD bases and
\[
  C_{ab}=\omega_a^+\circ\omega_b^-,
\]
the insertion direction \(\zeta=\omega_2\) gives the leading families
\[
  H^4(\zeta^+)\sim -\frac12\sum_j p_j(x) C_{2j} r^{-4},\qquad
  H^4(\zeta^-)\sim -\frac12\sum_j q_j(x) C_{j2} r^{-4},
\]
where
\[
  p_j(x)=\frac{x^T C_{2j}x}{|x|^2},\qquad
  q_j(x)=\frac{x^T C_{j2}x}{|x|^2}.
\]
The receiver radial proxy at a positive-chirality node is represented by the family \(C_{2k}\).  The exact basis identity
\[
  \operatorname{tr}(C_{ab}C_{cd})=4\delta_{ac}\delta_{bd}
\]
recovers the Step 84 local control:
\[
  \langle C_{2j},C_{2k}\rangle=4\delta_{jk},\qquad
  \langle C_{j2},C_{2k}\rangle=4\delta_{j2}\delta_{k2}.
\]
This local identity-pairing gives the exact mean \(8/3\), but the actual Green response replaces the identity pairing by the full source-to-receiver operator.

## 3. Gauge information from the raw flat multipole

I wrote and ran `workspace/scripts/step85_bianchi_multipole_check.py`, producing `workspace/data/step85_bianchi_multipole_check.json`.  It checks the leading flat row/column multipoles
\[
  H_{\rm row}=\sum_j (x^TC_{2j}x)C_{2j}/r^6,
  \qquad
  H_{\rm col}=\sum_j (x^TC_{j2}x)C_{j2}/r^6.
\]
Both families are exactly trace-free, divergence-free, and componentwise harmonic on \(\mathbb R^4\setminus\{0\}\): the symbolic divergence components and Laplacian components vanish after multiplying by the appropriate powers of \(r^2\).  This is useful because the flat singular model is already in Bianchi gauge away from the source.

This does **not** prove that an invariant compact-product source is TT.  The actual \(S_j^\epsilon\) is the distributional/cutoff/gauge-corrected source obtained from matching ALE and orbifold expansions and projecting away the global kernel.  The raw flat check only supplies the singular moment model for deriving \(S_j^\epsilon\).

## 4. Product operator sector ledger: the full operator is not a 9-dimensional TT block

I wrote and ran `workspace/scripts/step85_s2_tensor_block_symbolic.py` and `workspace/scripts/step85_product_operator_sector_ledger.py`, producing:

- `workspace/data/step85_s2_tensor_block_symbolic.json`,
- `workspace/data/step85_product_operator_sector_ledger.json`.

For the unit round \(S^2\), the symbolic rough-Laplacian calculation gives:
\[
  \nabla^*\nabla(fg)=\ell(\ell+1)fg,
\]
and for \(\ell\ge2\) on both scalar trace-free Hessian and vector trace-free sectors,
\[
  \nabla^*\nabla H=(\ell(\ell+1)-4)H.
\]
On the product \(S^2\times S^2\), the elementary sector denominators for
\(P=\frac12\nabla^*\nabla-\mathring R\) are:
\[
  P_{AA/BB}=\frac12\bigl(\ell_1(\ell_1+1)+\ell_2(\ell_2+1)\bigr)-1
\]
for factor-parallel trace and trace-free tensor sectors, and
\[
  P_{AB}=\frac12\bigl(\ell_1(\ell_1+1)+\ell_2(\ell_2+1)-2\bigr),\qquad \ell_1,\ell_2\ge1
\]
for one-form \(\otimes\) one-form mixed sectors.

The ledger recovers the four scalar-sector zero modes:
\[
  (\ell_1,\ell_2)=(1,0),(0,1)\quad\text{in AA and BB trace blocks},
\]
corresponding to the modes \(u_i g_j\) from Step 77.  It also retains the negative constant trace denominators \((\ell_1,\ell_2)=(0,0)	o P=-1\), which include the shape/scale sector in the fixed-Einstein-constant operator, and it gives the mixed one-form gap \(P=1\) at \(\ell_1=\ell_2=1\).  This directly implements the Strategist warning: pointwise \(S^2_0(\mathbb R^4)\) tensors are not the global divergence-free tensor space, and the full product operator must be built from scalar, one-form, and derived tensor harmonics.

## 5. Scalarized and sectorwise spectral proxies

### 5.1 First attempt and repair

The first script, `workspace/scripts/step85_green_transfer_scalarized_proxy.py`, made the correct object explicit but timed out after 600s.  I replaced it with `workspace/scripts/step85_green_transfer_scalarized_proxy_fast.py`, which cached one-factor Taylor derivative tensors and vectorized the \(C_{ab}\) contractions.  That fast file's first data output was then superseded because it used an inappropriate \(\ell_1+\ell_2\) parity filter and contained an interpretation sentence saying off-diagonal entries were substantial although the reported matrix was diagonal.

The corrected no-parity driver is `workspace/scripts/step85_corrected_scalar_proxy_driver.py`, with data in `workspace/data/step85_corrected_scalar_proxy_driver.json`.  The quotient is the simultaneous half-turn fixing the four poles and acting as \(-I\) on both tangent planes.  In local second-jet/multipole sectors, this does not impose an \(\ell_1+\ell_2\) parity filter; zonal modes of every \(\ell\) and \(|m|=2\) jet channels for all \(\ell\ge2\) can appear.  The A02 warning is reproduced explicitly: the probe has nonzero second-jet channels for every \(\ell=2,\dots,12\).

At \(L_{\max}=120\), shift \(=1\), and decreasing heat regularization, the scalar-component proxy trends are:

- Adjacent source/receiver, ambient frame: diff \(c_{\rm opp}-c_{\rm same}\approx -0.2709,-0.2655,-0.2629,-0.2616\) for \(\tau=0.02,0.01,0.005,0.0025\).
- Adjacent, antipodal-derivative frame: diff \(\approx 0.00772,0.00757,0.00749,0.00746\) over the same heat sequence.
- Diagonal antipodal-in-both-factors: diff \(\approx -0.04209,-0.04126,-0.04085,-0.04065\), independent of the two tested frame sign conventions.

These are **not** Ozuch coefficients.  They show that differentiated source/receiver transfer changes the \(8/3\) local number, that adjacent signs are frame-sensitive, and that no \(L\le20\) sufficiency should be claimed.

### 5.2 Sectorwise product-operator proxy

The stronger proxy is `workspace/scripts/step85_sectorwise_product_transfer_proxy.py`, with data in `workspace/data/step85_sectorwise_product_transfer_proxy.json`.  It replaces the common scalar shift by the elementary product denominators above, skips the four zero modes in the pseudo-inverse, and keeps the negative constant trace modes.  It still uses raw \(H^4\) quadrupole/second-jet factors rather than the exact \(S_j^\epsilon,L_i\), so it remains a proxy.

At \(L_{\max}=120\), heat sequence \(\tau=0.02,0.01,0.005,0.0025\):

- Adjacent, ambient frame:
\[
  c_{\rm opp}-c_{\rm same}\approx -1.1754,-1.1991,-1.2112,-1.2172.
\]
- Adjacent, antipodal-derivative frame:
\[
  c_{\rm opp}-c_{\rm same}\approx 0.3918,0.3997,0.4037,0.4057.
\]
- Diagonal antipodal-in-both-factors:
\[
  c_{\rm opp}-c_{\rm same}\approx -0.5129,-0.5233,-0.5286,-0.5312.
\]

The proxy values are nonzero and stable under truncation at the tested heat values, but their sign and magnitude are not invariant under source/receiver frame conventions in adjacent geometry.  The diagonal proxy is more robust in the simple sign-frame models.  The matrices remain diagonal in the axis-aligned \(C_{ab}\) basis because the proxy still propagates component sectors independently; this diagonal behavior is a feature of the proxy, not a theorem for the true Bianchi/gauge-corrected \(P^{-1}\) transfer.

## 6. Correction to the T-symmetry matched-control line

I wrote and ran `workspace/scripts/step85_T_symmetry_label_correction.py`, producing `workspace/data/step85_T_symmetry_label_correction.json`.  Step 84's numerical T-symmetry results are retained: \(T\) preserves the pencil, \(G=\langle T,S_0,S_2\rangle\) is transitive on the four nodes, and the invariant holomorphic-vector-field subspace is zero.  The correction is interpretive: the coordinate sign changes \(S_0,S_2\) are complex-linear projective maps in \(\mathbb{CP}^4\), not anti-holomorphic maps.  Therefore they do not reverse the complex orientation and do not undermine the all-same-chirality KE control.  The all-same complex smoothing is compatible with the \(G\)-equivariant algebraic family; the mixed-chirality Riemannian branch still uses the separate orientation-reversing \(L\) symmetry from Step 81.

The Step 84 note also displayed an \(O(t^{7/2})\) remainder.  This has not been derived.  A matched-control relation of the form
\[
  F_{\rm same}(t)=0\Rightarrow s+d+2c_{\rm same}=0
\]
requires identifying the KE degeneration in the same Ozuch chart and proving the power/log expansion layer.  The remainder is a target of the analytic matched-control work, not an available estimate.

## 7. Consequences for the next computation

This step changed the Green-response task from a convenient scalar pole recipe into an explicit staged computation:

1. **Exact source:** derive \(S_j^\epsilon\) as the compact-product, Bianchi-compatible distributional source associated with the raw row/column \(H^4\) flat multipoles.  The leading flat multipoles are TT/harmonic away from the singularity, but cutoff/matching and compact curvature corrections must be included.
2. **Full sectorwise inverse:** build the product \(P\) blocks on trace, scalar-derived TF, vector-derived TF, and one-form product sectors; skip the four invariant zero modes and handle the negative shape/scale modes deliberately.
3. **Receiver functional:** derive \(L_i\) from Ozuch's radial curvature-jet functional rather than identifying it with the same raw second-jet tensor family.
4. **Regularized sum:** evaluate heat-regularized sectorwise sums for adjacent and diagonal node-pair geometries and compare limits against truncation only after the above normalizations are fixed.
5. **Matched all-same control:** independently derive the \(G\)-equivariant KE degeneration's coordinates in the same chart if it is to cancel common self/same terms.

The current numerical proxies are scientifically useful as pressure tests and as reusable code architecture, not as a proof of obstruction or existence.  They show that the real transfer can materially change the local \(8/3\) algebra, that source/receiver frame choices matter, and that the complete product-sector operator must replace the scalar shortcut.

## 8. Peer message #570 absorbed

A03's message #570 gives a separate graph-manifold/negative-branch structural reduction: the orthogonally transitive \(T^2\)-invariant Einstein equations reduce to an area equation, a weighted harmonic map to \(SL(2)/SO(2)\), and a conformal equation; fixed helical Bianchi VII\(_0\) connectors fail because the orbit-map angle \(\psi=kz\) freezes a positive source, while general two-variable \(H^2\)-valued maps might escape through the conservation law.  The exact-Einstein maximum principle forces constant orbit map under constant outer boundary, so any viable long connector must be approximate and use a weighted forcing that stays order one while the global Ricci defect tends to zero.  This reinforces that the graph route's decisive object is an approximate long-connector mechanism, not the fixed-eigenframe ansatz.  I did not pursue that branch further in this step because the Green-response calculation was the active executable target.
