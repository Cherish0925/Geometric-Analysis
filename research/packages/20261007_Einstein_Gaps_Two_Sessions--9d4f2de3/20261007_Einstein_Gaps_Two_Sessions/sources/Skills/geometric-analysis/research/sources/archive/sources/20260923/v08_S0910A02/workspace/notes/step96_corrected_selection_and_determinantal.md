# Step 96/99: corrected selection rules and Step 99 trace-channel audit

Session `S0910A02`. Initial Step 96 by Agent2; **substantially superseded by Step 99 A02 audit** after A01 Step98.

This file is retained as the Gate-1/Gate-2/Gate-3 research note, but the old determinant-only and equal-phase criteria have been repaired.  The authoritative Step99 audit files are:

- `Sessions/S0910A02/workspace/notes/step99_a01_trace_obstruction_audit.md`
- `Sessions/S0910A02/workspace/data/step99_a01_trace_obstruction_audit.json`
- selected independent rerun: `Sessions/S0910A02/workspace/data/step99_selected_spectral_recompute.json`

## 1. Gate 1: local second obstruction vanishes on the kernel plane

**Retained conclusion.**  At each product-orbifold node,
\[
R^\pm=\operatorname{diag}(\Lambda,0,0),\qquad K^\pm=\ker R^\pm=\omega_1^{\pm\perp}.
\]
For every \(\zeta\in K^\pm\), the Biquard/Ozuch local second obstruction vanishes.  The determinant expression gives \(\mu_1=C\det R_\perp=0\), and the full projected quadratic map \(K\to K\) vanishes by the corrected \(T^2\)-weight-parity argument: the \(\beta=0\) subcircle acts with weight one on \(K\), and there is no degree-two monomial of weight one.

**Invalid arguments withdrawn.**  The old SO(2)-transitivity proof was invalid because an equivariant map \(K\to K\) need not vanish.  The earlier conformally-flat/product-\(I/3\) curvature and critical-scale story was false.

## 2. Node characters and what they still mean

At node \(j\), with pole signs \(s_A^j,s_B^j\) and EH chirality \(\varepsilon_j\),
\[
\theta_j=s_A^j\alpha+\varepsilon_j s_B^j\beta,
\qquad
\sigma_j=\varepsilon_js_A^js_B^j.
\]
The condition \(\sigma_i=\sigma_j\) is still a useful **selection rule for allowed traceless angular channels**.  It is not the whole coefficient calculation.  A01 Step98/A02 Step99 found a stronger physical statement at the checked leading inter-node order: physical same-chirality maps \(B_{++}\) and \(B_{--}\) vanish in AB and AA/BB sectors, while physical cross-chirality maps \(B_{+-}=B_{-+}\) may be nonzero.

Thus the old Step96 language that treated all pairs as having a universal isotropic coefficient plus optional \(\sigma\)-matched anisotropy is no longer accurate enough for Gate 3.  Gate 3 must track physical chirality, adjacency type, and trace versus traceless channels.

## 3. Correct linear algebra for the traceless P/Q map

For a real-linear map on a kernel plane written in complex notation as
\[
L(z)=Pz+Q\bar z,
\]
\[
\det_{\mathbb R}L=|P|^2-|Q|^2,
\qquad
\ker L\ne0\iff |P|=|Q|.
\]
Both strict inequalities \(|P|>|Q|\) and \(|P|<|Q|\) give an invertible map.  The old Step96 statement that \(|Q|>|P|\) meant solvability was wrong.

Moreover, Step99 separates the scalar trace/isotropic channel from the traceless P/Q channel.  The current leading diagonal-balanced obstruction is driven by a positive AB trace channel; it is not decided by the old frozen comparison
\[
|q_{\rm diag}|\quad\text{vs}\quad |2q_{\rm adj}+q_{\rm diag}|,
\]
which was only an equal-scale/equal-phase traceless slice.

## 4. Compatible KE calibration

Biquard--Rollin identifies the local smoothing/Kähler-class parameter as
\[
\zeta=(\zeta_r,\zeta_c)\in\mathfrak h_{\mathbb R}\oplus\mathfrak h_{\mathbb C},
\]
with \(\zeta_r\) representing the local Kähler class.  Lemma 6 says a root class is Lagrangian when \(\zeta_r\in\ker\theta\) and holomorphic when \(\zeta_c\in\ker\theta\).  At the product quotient, the compatible Kähler smoothing periods therefore lie in \(K=\omega^\perp\), while the excluded holomorphic resolution direction is the Kähler eigenline.

OSS/Tian--Yau place the four-node surface \((\mathbb P^1\times\mathbb P^1)/\mathbb Z_2\) on the degree-4 KE compactification boundary, with an open smooth degree-4 del Pezzo KE locus adjacent to it.  In a full calibrated variational LS reduction, the compatible-pattern leading quartic obstruction should vanish on that open smoothing locus.  A01 Step98 and A02 Step99 cross-verified the corresponding **raw leading inter-node** fact: physical same-chirality maps vanish in all checked AB and AA/BB sectors.

Honesty rider: this is a calibration of the leading inter-node table, not a complete proof that all self/complement/frame/global terms have been accounted for, and not a solvability criterion for every compatible boundary stratum.

## 5. Audited leading cross-chirality coefficients

A02 Step99 parsed A01's JSON and then reran selected spectral computations from A01's scripts.  The selected rerun matched the stored A01 data exactly to stored precision.

For physical cross-chirality pairs at receiver `NN` in the positive product mirror:

| source | pair type | AB trace coefficient \(c_0\) | isotropic eigen coefficient \(c_0/2\) | AA/BB traceless coefficient |
|---|---:|---:|---:|---:|
| `NS` | adjacent | \(+0.12576998928\) | \(+0.06288499464\) | Q-type \(0.0080049973185\) |
| `SN` | adjacent | \(+0.12576998928\) | \(+0.06288499464\) | P-type \(0.0080049973185\) |
| `SS` | diagonal | \(-0.070907042884\) | \(-0.035453521442\) | 0 in the stored AA/BB data |

Same-chirality coefficients are zero at every available rung.  The older numbers \(-0.03144\) and \(+0.01773\) are parity components, not physical same-chirality pair coefficients.

## 6. Pattern consequences from the raw inter-node table

Let \(u_i=t_i^2>0\) be the scale-square of a bubble.

### 6.1 Diagonal balanced pattern

For
\[
\varepsilon=(+,-,-,+),
\]
each receiver has two opposite-chirality adjacent sources and one same-chirality diagonal source.  The diagonal same term vanishes at this order, and
\[
A_j^{\rm inter}=0.06288499464\,(u_{\rm adj,1}+u_{\rm adj,2})I_K+T_j,
\]
with
\[
\|T_j\|\le 0.0080049973185\,(u_{\rm adj,1}+u_{\rm adj,2}).
\]
The positive margin is
\[
0.0548799973215>0.
\]
So the **raw leading inter-node matrix is uniformly positive definite/invertible for all positive scales and all phases** in the diagonal-balanced row.  This supports a strong local obstruction candidate for the \(\#_3(S^2\times S^2)\) product-orbifold degeneration, subject to full LS and remainder checks.

### 6.2 Adjacent balanced pattern

For the adjacent balanced representative
\[
\varepsilon=(+,+,-,-),
\]
each receiver sees one opposite-chirality adjacent source and one opposite-chirality diagonal source.  The scalar part has the form
\[
P=0.06288499464\,u_{\rm adj}-0.035453521442\,u_{\rm diag},
\]
while the adjacent tensor contribution has size at most
\[
|Q|\le0.0080049973185\,u_{\rm adj}.
\]
Therefore determinant equality \(|P|=|Q|\) is possible for positive scale-square ratios
\[
\frac{u_{\rm diag}}{u_{\rm adj}}\approx1.54794206864
\quad\text{or}\quad
1.99951906257,
\]
with \(P=0\) near \(1.77373056560\).  The raw pair table does **not** give a uniform obstruction for the adjacent-balanced row; it leaves a scale-ratio window that could become a constructive route after the coupled LS equations are understood.

## 7. Current Gate-3 standard

The next theorem-shaped object is not a single coefficient inequality.  It is a calibrated leading-order LS statement:

1. prove or import a slice-compatible variational LS reduction for this product-orbifold boundary problem;
2. assemble self, inter-node, complement, frame/projector, and any global deformation terms in the same normalization;
3. prove a relative remainder strong enough to make the \(O(t^3)\) leading table decisive;
4. then conclude a local diagonal-balanced obstruction or analyze the adjacent-balanced kernel window.

Even a successful local obstruction theorem would not show that the same smooth four-manifold has no distant Einstein metric, and therefore would not by itself refute Yau 26.
