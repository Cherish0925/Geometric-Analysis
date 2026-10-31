# Step 99: A02 audit of A01 Step98 trace-channel obstruction

Session `S0910A02`. Agent3 / Actuator. Execute.

## 1. Purpose and scope

This note records an independent A02 audit of A01 Step98's claim of universal same-chirality leading inter-node vanishing and a mixed-diagonal trace obstruction for the product orbifold
\[
\mathcal O=(S^2\times S^2)/\mathbb Z_2
\]
with four \(A_1\) singularities.

The audit is **not** a complete Ozuch/Biquard gluing theorem and is **not** a global no-Einstein result for Yau 26.  It checks what the available raw spectral inter-node data actually implies, and separates that from still-open Lyapunov--Schmidt, self/complement/global, and relative-remainder requirements.

Executable audit:

- Script: `Sessions/S0910A02/workspace/scripts/step99_a01_trace_obstruction_audit.py`
- Data: `Sessions/S0910A02/workspace/data/step99_a01_trace_obstruction_audit.json`
- Inputs: A01 `workspace/data/step98_full_chirality_tensor_maps.json`, A01 `workspace/data/step96_kernel_plane_ab_map.json`, and A02 `workspace/data/step96_corrected_selection_determinantal.json`.

## 2. Raw data checks

The A02 script parses A01's JSON and independently recomputes the compact trace/double-angle and complex \(P/Q\) decompositions.

### 2.1 Same-chirality vanishing

At every available A01 tensor rung
\[
(\tau,L_{\max})=(0.08,80),(0.04,120),(0.02,180),(0.01,260),
\]
for every checked pair `NS`, `SN`, `SS`, and for both AA and BB tensor sectors, the parsed raw physical same-chirality maps satisfy
\[
B_{++}=B_{--}=0
\]
to the stored precision.  The tensor checks also give
\[
B_{+-}=B_{-+},\qquad B_{eo}=B_{oe}=0.
\]
For the AB sector, the adjacent ladder and pair comparison likewise have same-chirality raw maps zero and cross-chirality symmetry exact in the stored data.

This is a genuine correction to the old A02 language: the older coefficients
\(-0.03144\) and \(+0.01773\) were parity odd/even components, **not** physical same-chirality coefficients.  Physical same-chirality leading inter-node coefficients vanish in the AB and AA/BB data now checked.

This agrees with the compatible Kähler smoothing calibration: Biquard--Rollin identifies compatible smoothing periods with the kernel plane \(K=\omega^\perp\), and OSS/Tian--Yau place an open smooth degree-4 del Pezzo KE locus adjacent to the four-node boundary.  The source geometry predicts that the full calibrated compatible-pattern reduced obstruction vanishes on an open set of smoothing parameters.  The present computation verifies the corresponding leading inter-node spectral statement; it does not by itself compute every self/complement/global term.

### 2.2 Cross-chirality coefficients

For physical cross-chirality pairs at receiver `NN`, the AB sector is pure trace:

| source | pair type | trace coefficient \(c_0\) | isotropic eigen coefficient \(c_0/2\) | traceless channel |
|---|---:|---:|---:|---:|
| `NS` | adjacent | \(+0.12576998928\) | \(+0.06288499464\) | 0 |
| `SN` | adjacent | \(+0.12576998928\) | \(+0.06288499464\) | 0 |
| `SS` | diagonal | \(-0.070907042884\) | \(-0.035453521442\) | 0 |

For AA/BB tensor sectors, the cross-chirality maps are traceless:

| source | sector contribution | coefficient magnitude |
|---|---|---:|
| `NS` | AA gives Q-type traceless channel | \(0.0080049973185\) |
| `SN` | BB gives P-type traceless channel | \(0.0080049973185\) |
| `SS` | no AA/BB tensor channel in the stored data | 0 |

Thus the trace channel and the old \(P/Q\) angular channel are separate.  The leading diagonal-balanced obstruction, if it survives the full LS and remainder analysis, is trace/isotropic rather than a determinant of a frozen traceless map.

## 3. Pattern consequences from the raw inter-node table

Write \(u_i=t_i^2>0\) for the scale-square of a nonzero bubble.  For a source with unit trace direction, the AB trace contributes an isotropic matrix \((c_0/2)u_i I_K\).  The tensor contribution is traceless with operator controlled by the recorded coefficient (the audit uses the conservative coefficient \(0.0080049973185\)).

### 3.1 Diagonal balanced row

For the diagonal balanced pattern
\[
\varepsilon=(+,-,-,+),
\]
each node has two opposite-chirality adjacent neighbours and one same-chirality diagonal neighbour.  The same-chirality diagonal term vanishes at the checked inter-node order.  At each receiver,
\[
A_j^{\rm inter}=0.06288499464\,(u_{\rm adj,1}+u_{\rm adj,2})I_K+T_j,
\]
with
\[
\|T_j\|\le 0.0080049973185\,(u_{\rm adj,1}+u_{\rm adj,2}).
\]
The margin is
\[
0.06288499464-0.0080049973185=0.0548799973215>0.
\]
Therefore the **raw leading inter-node matrix is uniformly positive definite/invertible for all positive scales and all phases** in this row.  This verifies A01's leading inter-node diagonal-balanced obstruction candidate, more strongly than an equal-scale trace check.

This statement is conditional at the gluing level: full self terms, complement Schur terms, frame/projector motion, global deformation coupling, and a relative \(o(t^3)\) remainder still have to be proved not to cancel or reorder this inter-node contribution.

### 3.2 Adjacent balanced row

For the adjacent balanced pattern represented by
\[
\varepsilon=(+,+,-,-),
\]
each receiver sees one opposite-chirality adjacent source and one opposite-chirality diagonal source, plus one same-chirality zero source.  A representative scalar part is
\[
P=0.06288499464\,u_{\rm adj}-0.035453521442\,u_{\rm diag}.
\]
The tensor bound from the adjacent source is
\[
|Q|\le 0.0080049973185\,u_{\rm adj}.
\]
Hence determinant equality \(|P|=|Q|\) is not uniformly excluded.  The scale-square ratios are
\[
\frac{u_{\rm diag}}{u_{\rm adj}}
\approx 1.54794206864\quad\text{or}\quad 1.99951906257,
\]
with \(P=0\) near
\[
\frac{u_{\rm diag}}{u_{\rm adj}}
\approx 1.77373056560.
\]
Thus the raw leading pair table **splits the two balanced rows**: it supports a uniform diagonal-balanced obstruction candidate, but leaves an adjacent-balanced scale-ratio window where the leading determinant condition could be met.  This does not prove an adjacent-balanced Einstein branch; it only shows that A01's trace obstruction is not uniform across all mixed rows.

## 4. Corrections to the A02 Gate-3 framework

1. The old statement "\(|Q|>|P|\) gives a kernel/solvability" is false.  For \(L(z)=Pz+Q\bar z\),
   \[
   \ker L\ne0\iff |P|=|Q|.
   \]
   Both strict inequalities give an invertible real-linear map.

2. The old criterion \(|q_{\rm diag}|\) versus \(|2q_{\rm adj}+q_{\rm diag}|\) is only a special traceless/equal-scale/equal-phase slice and is no longer the Gate-3 decision.

3. The \(\sigma\)-matching selection rule remains useful as an allowance rule for traceless angular channels, but actual leading coefficients have stronger vanishing: **physical same-chirality inter-node maps vanish** in the AB and AA/BB data.  Chirality, adjacency type, and trace/traceless splitting must all be tracked.

4. The correct current Gate-3 target is a calibrated leading inter-node table plus a full LS/remainder theorem.  For the positive mirror, the table currently says: diagonal balanced is obstructed at raw leading inter-node order; adjacent balanced is not uniformly obstructed by the same argument.

## 5. Relation to Yau 26

This is important progress for the strict positive branch laboratory, but it does not resolve the active problem.  Even a full local obstruction theorem would only exclude an Einstein branch with this product-orbifold limit, this bubble tree, and this chirality pattern.  It would not rule out a distant positive Einstein metric on the same smooth four-manifold, nor any negative or Ricci-flat Einstein metric.  A dimension-four refutation of Yau 26 still requires defeating both strict branches globally, or finding another all-sign no-Einstein reservoir with near-pinched metrics.

Immediate mathematical needs:

- prove the relative \(o(t^3)\) expansion and identify all self/complement/frame/global terms in the same calibrated slice;
- formulate the diagonal-balanced obstruction as a conditional theorem with exact hypotheses;
- analyze the adjacent-balanced scale-ratio window as a possible constructive route;
- build the corresponding coefficient table for the negative product mirror, where the strict negative branch is still required for any dimension-four refutation.

## 6. Small formal algebra certificate

To prevent the determinant mistake from recurring, Step99 also added a Lean algebra certificate:

- Lean source: `Sessions/S0910A02/workspace/proofs/Step99RealLinearPQ.lean`
- strict dependency check: `Sessions/S0910A02/workspace/proofs/Step99RealLinearPQ.check.json`

The theorem `Yau26Step99.pq_real_det_formula` proves the real determinant identity for
\[
L(z)=Pz+Q\bar z,
\]
and `Yau26Step99.pq_kernel_trivial_of_normsq_ne` proves that if \(|P|^2\ne |Q|^2\), then the real kernel is trivial.  The strict `qiushi-yau26 lean` audit accepted the theorem with only the allowed Mathlib axioms `propext`, `Classical.choice`, and `Quot.sound`.  This formalizes only the finite-dimensional algebraic correction; it is not a Lean formalization of any curvature or gluing claim.
