# TTCS Independent Branch Record

```json
{
  "step_id": 100,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step100_chirality_cancellation_proof.md",
    "Sessions/S0910A01/workspace/notes/step98_trace_obstruction_theorem.md",
    "Sessions/S0910A01/workspace/data/step100_chirality_cancellation_proof.json",
    "Sessions/S0910A01/workspace/plans/route_assessment_step100.md",
    "Sessions/S0910A01/workspace/notes/step99_geometric_mode_bridge_check.md"
  ]
}
```

## Task

Verify the structural proof of same-chirality vanishing B_{++} = B_{--} = 0 in the product-orbifold Ozuch desingularization calculation. The proof claims three algebraic mechanisms: (1) tensor-pole parity giving pairwise cancellation when tensor factors have different poles; (2) scalar-mode parity where Block_D = Block_O forces c2+s2 cancellation when tensor is at the same pole; (3) cross-chirality nonzero because R_minus(O,D) = +1/2 O changes sign from R_plus(O,D) = -1/2 O. The geometric root is the definite chirality of the EH curvature (Ozuch Prop 1.16: linearized curvature d_e R^+(H^4(zeta^+)) = 0). Check: (a) Are the three mechanisms correctly stated and do they cover all cases (sector AA/BB, pairs NS/SN/SS)? (b) Does the geometric interpretation correctly connect the algebraic identities to the EH definite chirality? (c) Are there hidden assumptions or gaps in the proof? (d) Does the result extend to the AB sector? (e) What does this mean for the full Ozuch equation — can the self/deformation terms break the positive inter-node response?

## Output

# Scientific verification memo

## 1. Algebraic result actually established

For receiver node \(NN\) and the three distinct source nodes, the \(AA/BB\) \(++\) cancellation is algebraically correct, provided the displayed polarization tables include the exact spectral normalization and multiplicity weights.

The six configurations divide exactly as follows:

| Sector | Source | Tensor poles | Algebraic mechanism |
|---|---:|---|---|
| \(AA\) | \(NS\) | same | scalar \(c_2/s_2\) cancellation |
| \(AA\) | \(SN\) | different | tensor-polarization pairing |
| \(AA\) | \(SS\) | different | tensor-polarization pairing |
| \(BB\) | \(NS\) | different | tensor-polarization pairing |
| \(BB\) | \(SN\) | same | scalar \(c_2/s_2\) cancellation |
| \(BB\) | \(SS\) | different | tensor-polarization pairing |

Thus the two vanishing mechanisms cover every distinct-source \(AA/BB\) case relative to \(NN\). They do not address the \(NN\leftarrow NN\) self term.

### Different tensor poles

Let \(X,Y\) denote arbitrary receiver/source scalar jets. For the pair
\(\{(E,c_2),(M,s_2)\}\), bilinearity gives
\[
R_+(D,X)\otimes S_+(\sigma D,Y)
+
R_+(-D,X)\otimes S_+(\sigma D,Y)=0.
\]
For \(\{(E,s_2),(M,c_2)\}\),
\[
R_+(O,X)\otimes S_+(-\sigma O,Y)
+
R_+(O,X)\otimes S_+(\sigma O,Y)=0.
\]
This cancellation is modewise in the scalar factor. In fact, it works for any receiver/source chirality combination, as long as each map is bilinear.

A necessary ingredient is equality of the spectral weights within each paired tensor family. If their weights are \(q_{Ec}\) and \(q_{Ms}\), the first expression becomes proportional to \(q_{Ec}-q_{Ms}\). Equality follows naturally from the rotational symmetry and matched normalization of the electric/magnetic polarization basis, but it is not stated in the proof.

### Same tensor pole

The quartet \(D,O,O,-D\) at both tensor poles gives
\[
2\left[
R_+(D,S)\otimes S_+(D,S)
+
R_+(O,S)\otimes S_+(O,S)
\right].
\]
For \(S=I\), all displayed mixed trace/trace-free maps vanish.

For \(S=D\),
\[
\mathrm{Block}^{++}_D
=\frac14(D\otimes D+O\otimes O),
\]
and for \(S=O\),
\[
\mathrm{Block}^{++}_O
=\frac14(O\otimes O+D\otimes D)
=\mathrm{Block}^{++}_D.
\]
The arithmetic is correct. Since the \(c_2\) and \(s_2\) values at the opposite scalar pole have equal magnitude and opposite parity sign, their sum vanishes.

The symbol \(\sigma\) is reused here even though it was previously defined from \(\ell_t\). In this case the relevant factor depends on \(\ell_s\); it should be renamed, for example \(\eta_s\). This does not affect the cancellation, which uses only
\[
(c_2,s_2)\longmapsto (\eta_s D,-\eta_s O).
\]

This step also requires equal \(c_2/s_2\) spectral weights and equal weights among the duplicated \(D/O\) tensor polarizations. These equalities are expected from the real two-dimensional \(m=2\) representation, but they belong explicitly in the derivation.

For \(\ell_s=0,1\), there are no \(m=2\) scalar modes, so only the \(I\) calculation remains and the block is zero.

## 2. The \(--\) identity has a skipped derivation

The written calculation explicitly proves only \(B_{++}=0\). The JSON artifact also contains only the field `B_pp_zero`; its 72 entries cover \(AA/BB\), not \(B_{--}\).

The displayed cross-chirality formulas implicitly correspond to the fuller minus table
\[
\begin{aligned}
&R_-(D,D)=-\tfrac12D,\qquad R_-(O,D)=+\tfrac12O,\\
&R_-(D,O)=-\tfrac12O,\qquad R_-(O,O)=-\tfrac12D,
\end{aligned}
\]
and
\[
\begin{aligned}
&S_-(D,D)=-\tfrac14D,\qquad S_-(O,D)=+\tfrac14O,\\
&S_-(D,O)=-\tfrac14O,\qquad S_-(O,O)=-\tfrac14D.
\end{aligned}
\]
If these are the exact form-algebra coefficients, then
\[
\mathrm{Block}^{--}_D
=\mathrm{Block}^{--}_O
=\frac14(D\otimes D+O\otimes O),
\]
and the same scalar parity argument proves \(B_{--}=0\). The text supplies only part of this table and no explicit conjugacy carrying \(++\) to \(--\). Thus the \(--\) half is correct conditional on the omitted minus-map entries, but it is not independently derived by the supplied proof or JSON.

Likewise, the calculation is written with receiver \(NN\). Extension to every receiver node requires covariance under the product isometries together with explicit transport of oriented node frames and chirality labels.

## 3. Cross-chirality calculation

Using
\[
S_-(O,D)=+\tfrac14O
\]
instead of \(S_+(O,D)=-\tfrac14O\), the stated computation gives
\[
\mathrm{Block}^{+-}_D
=\frac14(D\otimes D-O\otimes O),
\]
and, using the corresponding \(S_-(D,O)\) and \(S_-(O,O)\) entries,
\[
\mathrm{Block}^{+-}_O
=-\frac14(D\otimes D-O\otimes O).
\]
The opposite scalar-pole signs therefore reinforce:
\[
\eta_s\mathrm{Block}^{+-}_D
-\eta_s\mathrm{Block}^{+-}_O
=2\eta_s\mathrm{Block}^{+-}_D.
\]

This establishes a nonzero fixed-degree block only when:

- the tensor factor is at the same pole;
- \(\ell_s\ge 2\), so \(c_2/s_2\) modes exist;
- the relevant spectral coefficient is nonzero.

Consequently it applies to \(AA:NS\) and \(BB:SN\). It does not imply that every \(B_{+-}\) pair is nonzero. The different-tensor-pole configurations still cancel by the first mechanism, and the \(\ell_s=0,1\) slices vanish.

The third mechanism therefore explains the contrast with cross chirality; it is not an additional ingredient in the proof of same-chirality vanishing.

## 4. Relation to the Eguchi–Hanson chirality identity

The quoted Ozuch identity
\[
d_{\mathbf e}R^+\!\left(H^4(\zeta^+)\right)=0
\]
correctly identifies the local definite chirality of the leading Eguchi–Hanson asymptotic tensor and is consistent with the sign pattern in the finite-dimensional maps.

It is not, by itself, equivalent to the inter-node identity. Schematically the latter is a curved-background Green response
\[
B_{++}^{ij}\sim
\mathcal R_{+,i}\,G_{\mathcal O}\,\mathcal S_{+,j},
\]
summed over a complete degenerate eigenspace. The Euclidean identity concerns \(H^4\) near one EH end, whereas \(G_{\mathcal O}\) is the global product-orbifold resolvent. A locally anti-self-dual singular tensor need not automatically produce a globally vanishing \(R^+\) response after solving on the curved product background.

A direct geometric derivation would require an intertwining statement showing that the relevant Lichnerowicz Green operator preserves the linearized Kähler/anti-self-dual subspace and that the complete Ozuch source belongs to that subspace, including motion of the \(K^+\) plane. The supplied finite algebra proves the selected \(AA/BB\) matrix elements without such an operator theorem. Thus the EH proposition is a persuasive geometric explanation, not yet a derivation of the entire inter-node identity.

## 5. AB sector

The structural proof does not extend to \(AB\) as written:

- the proof explicitly treats “\(AA\) or \(BB\)”;
- both mechanisms use the quartet of trace-free tensor polarizations \(D,O,O,-D\);
- the AB family consists of mixed one-form products and has different polarization algebra;
- `step100_chirality_cancellation_proof.json` contains no AB entries.

The earlier record reports numerical AB same-chirality vanishing from Step 96 data, but no exact AB coefficient identity is supplied here. An AB result requires its own exact relation
\[
\sum_{\text{AB polarizations}}
R_\pm^{AB}\otimes S_\pm^{AB}=0
\]
at each degree pair, or a proved global chirality intertwining theorem that includes mixed components.

## 6. Unstated mathematical ingredients

The all-degree \(AA/BB\) result depends on:

1. equal normalized spectral weights for the paired electric/magnetic tensor modes;
2. equal weights for real \(c_2/s_2\) scalar modes;
3. common Green eigenvalue factors across each degenerate polarization family;
4. exact pole-parity and oriented-frame transport formulas;
5. completeness of the selected tensor families in the relevant eigenspaces;
6. the Step 96 source functional being the actual Ozuch singular-source pairing;
7. quotient and isotropy multiplicities preserving the paired weights.

Step 99 addresses same-factor tensor jets for the selected electric/full-Lie magnetic families and mixed-derivative support, but it does not establish items 5–7 in full geometric form.

The JSON provides useful finite-degree regression evidence. Its `mechanism` string is metadata rather than an algebraic certificate, and its finite list does not itself prove all degrees, \(B_{--}\), or AB.

## 7. Consequence for the full Ozuch equation

The complete projected equation contains
\[
F_i=
F_i^{\rm self}
+F_i^{\rm deform}
+\sum_{j\ne i}B_{ij}
+F_i^{\rm complement}
+F_i^{\rm projector}
+R_i.
\]
The proved inter-node cancellation leaves the separately defined \(B_{++}\) block unchanged, and the computed mixed-chirality AB contribution may remain positive as an isolated matrix. Nevertheless, self, deformation, complement, and projector-motion terms can contribute to the same kernel-plane trace and spin-2 directions and can neutralize that inter-node component in the total equation.

In particular, existence of an all-same Kähler–Einstein smoothing only states that the complete projected expression vanishes along that deformation path. It does not imply that the self term vanishes separately. Positivity of the full leading equation would require a computation of the images of all adjustment terms and proof that they cannot supply the opposing trace direction. No such result is contained in the supplied material.

**Bottom line:** the \(AA/BB\), receiver-\(NN\), distinct-source \(++\) identity is a sound finite-dimensional cancellation under exact normalization symmetry. The \(--\) result needs the omitted minus-map table or a chirality conjugacy; AB needs a separate exact calculation; and the EH curvature identity presently explains rather than derives the global spectral cancellation. The result alone does not establish positivity or insolubility of the complete Ozuch equation.