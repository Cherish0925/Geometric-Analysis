# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 100,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step100_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step100_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the structural proof of same-chirality vanishing B_{++} = B_{--} = 0 in the product-orbifold Ozuch desingularization calculation. The proof claims three algebraic mechanisms: (1) tensor-pole parity giving pairwise cancellation when tensor factors have different poles; (2) scalar-mode parity where Block_D = Block_O forces c2+s2 cancellation when tensor is at the same pole; (3) cross-chirality nonzero because R_minus(O,D) = +1/2 O changes sign from R_plus(O,D) = -1/2 O. The geometric root is the definite chirality of the EH curvature (Ozuch Prop 1.16: linearized curvature d_e R^+(H^4(zeta^+)) = 0). Check: (a) Are the three mechanisms correctly stated and do they cover all cases (sector AA/BB, pairs NS/SN/SS)? (b) Does the geometric interpretation correctly connect the algebraic identities to the EH definite chirality? (c) Are there hidden assumptions or gaps in the proof? (d) Does the result extend to the AB sector? (e) What does this mean for the full Ozuch equation — can the self/deformation terms break the positive inter-node response?

## Integrated Scientific Memo

# Verification verdict

The structural argument proves a valid **\(AA/BB\), distinct-node, \(++\)** cancellation identity for the implemented finite-dimensional spectral model, subject to explicit normalization and node-frame assumptions. As written, however, it overclaims three points:

1. \(B_{--}=0\) is not actually derived from the displayed minus-chirality table.
2. The proof does not cover the \(AB\) sector.
3. Eguchi–Hanson definite chirality explains the algebra but has not been shown to imply the global orbifold Green-response identity.

## 1. \(AA/BB\) case analysis

With receiver \(NN\), all six distinct-source configurations are covered:

\[
\begin{array}{c|ccc}
 & NS & SN & SS\\ \hline
AA & \text{same tensor pole} & \text{different} & \text{different}\\
BB & \text{different} & \text{same} & \text{different}.
\end{array}
\]

The theorem does **not** cover the self interaction \(NN\leftarrow NN\).

### Different tensor poles

The two polarization pairings cancel by bilinearity:

\[
\{(E,c_2),(M,s_2)\}:
\quad
R(D,X)\otimes S(\sigma D,Y)
+
R(-D,X)\otimes S(\sigma D,Y)=0,
\]

\[
\{(E,s_2),(M,c_2)\}:
\quad
R(O,X)\otimes
\bigl(S(-\sigma O,Y)+S(\sigma O,Y)\bigr)=0.
\]

Thus this cancellation occurs separately for every scalar mode and, algebraically, for any receiver/source chirality combination. It requires equal total coefficients within each paired family—spectral normalization, Green denominator, multiplicity, quotient factor, and isotropy weight must all agree.

### Same tensor pole

For \(++\), the arithmetic is correct:

\[
\begin{aligned}
\operatorname{Block}^{++}_{D}
&=2\left[
R_+(D,D)\otimes S_+(D,D)
+R_+(O,D)\otimes S_+(O,D)
\right]\\
&=\frac14(D\otimes D+O\otimes O),
\end{aligned}
\]

and

\[
\operatorname{Block}^{++}_{O}
=\frac14(D\otimes D+O\otimes O)
=\operatorname{Block}^{++}_{D}.
\]

For \(S=I\), all mixed trace/trace-free entries vanish, so the \(m=0\) contribution is zero.

The final \(c_2/s_2\) cancellation requires more than block equality:

\[
\eta_c w_c\,\operatorname{Block}_{D}
+\eta_s w_s\,\operatorname{Block}_{O}=0
\]

uses

\[
\eta_s=-\eta_c,\qquad w_s=w_c.
\]

The proof should not reuse the tensor parity symbol \(\sigma=(-1)^{\ell_t+1}\) here: the relevant sign comes from the scalar pole and should be denoted separately, say \(\eta_s(\ell_s)\).

Most importantly, the opposite \(c_2/s_2\) signs are not automatic under the ordinary antipodal map, which gives both real \(m=2\) harmonics the same \((-1)^{\ell_s}\) factor. The required relative minus sign comes from the chosen oriented node-frame transport, apparently including a reflection that is even on \(\cos 2\phi\) and odd on \(\sin 2\phi\). This transport rule is the load-bearing geometric input and remains assumed rather than derived in Step 100.

For \(\ell_s=0,1\), no \(m=2\) scalar Hessian modes occur; the remaining \(I\)-type/zero-Hessian slice vanishes separately. It should not be treated using an \(m=2\) normalization.

## 2. Status of \(B_{--}\)

The written proof and JSON artifact explicitly verify only `B_pp_zero`. The supplied minus table is incomplete, so \(B_{--}=0\) is not established from the text alone.

If the exact minus maps are

\[
\begin{aligned}
R_-(D,D)&=-\tfrac12D,&
R_-(O,D)&=+\tfrac12O,\\
R_-(D,O)&=-\tfrac12O,&
R_-(O,O)&=-\tfrac12D,
\end{aligned}
\]

with the analogous quarter-scaled source maps, then direct calculation gives

\[
\operatorname{Block}^{--}_{D}
=\operatorname{Block}^{--}_{O}
=\frac14(D\otimes D+O\otimes O),
\]

and the same scalar parity argument proves \(B_{--}=0\). Therefore \(B_{--}\) is credible and conditionally correct, but the theorem needs either:

- the complete exact minus-map table and this calculation, or
- an explicitly proved chirality-conjugacy carrying the \(++\) identity to \(--\).

Extension from receiver \(NN\) to arbitrary receiver nodes likewise needs product-isometry covariance together with oriented-frame and chirality-label transport, not just an assertion of symmetry.

## 3. Cross-chirality mechanism

The sign change in the tensor-\(O\) entries of the minus source map yields

\[
\operatorname{Block}^{+-}_{D}
=\frac14(D\otimes D-O\otimes O),
\]

\[
\operatorname{Block}^{+-}_{O}
=-\operatorname{Block}^{+-}_{D}.
\]

The opposite scalar-pole signs now reinforce:

\[
\eta\,\operatorname{Block}^{+-}_{D}
-\eta\,\operatorname{Block}^{+-}_{O}
=2\eta\,\operatorname{Block}^{+-}_{D}\neq0.
\]

This explains nonzero cross chirality only for same-tensor-pole cases with genuine \(m=2\) content and nonzero spectral coefficient: \(AA:NS\) and \(BB:SN\). It does not prove every \(B_{+-}\) block is nonzero; different-tensor-pole cases still cancel, and low scalar degrees vanish.

The phrase “minus maps differ only in K-odd cross terms” is inaccurate because \(R_-(O,O)\) also changes. The rule consistent with the displayed cross-chirality blocks is that entries with **tensor argument \(O\)** change sign. The exact convention should be stated via the complete coefficient table rather than verbally.

This cross-chirality sign change is a contrast mechanism, not a third mechanism needed to prove same-chirality vanishing.

## 4. Relation to Eguchi–Hanson definite chirality

The identity

\[
d_{\mathbf e}R^+\!\left(H^4(\zeta^+)\right)=0
\]

correctly states that the leading EH asymptotic perturbation has definite linearized curvature chirality. It is consistent with the \(D/O\) sign pattern and gives a persuasive geometric explanation for why same-chirality channels disappear while opposite chirality survives.

It is not yet a derivation of the inter-node identity. The computed block has schematic form

\[
B_{++}^{ij}
=
\mathcal R_{+,i}\,
G_{\mathcal O}\,
\mathcal S_{+,j},
\]

where \(G_{\mathcal O}\) is the global product-orbifold Green operator. A local Euclidean statement about \(H^4\) does not by itself imply that the global curved-background response remains in a subspace annihilated by \(\mathcal R_+\).

A geometric proof would need an intertwining result showing that:

1. the complete Ozuch singular source belongs to the appropriate linearized Kähler/definite-chirality subspace;
2. the gauge-fixed Lichnerowicz Green operator preserves that subspace;
3. kernel-plane motion does not introduce a receiver component;
4. quotient projection and node-frame transport preserve the statement.

Thus the exact \(AA/BB\) coefficient cancellation is currently the proof; EH chirality is its interpretation.

## 5. The \(AB\) sector is not covered

The Step 100 proof uses the tensor quartet

\[
D,\ O,\ O,\ -D
\]

and scalar Hessian modes \(I,D,O\). Those mechanisms are specific to the \(AA/BB\) tensor–scalar families. The \(AB\) sector consists of mixed one-form products and has different representation algebra.

This is confirmed by the artifacts: the 72 JSON cases are exactly

\[
2\ \text{sectors}\times3\ \text{sources}\times12\ \text{degree pairs},
\]

with no \(AB\) entries. Earlier notes report numerical or stored-data evidence for \(AB\) same-chirality vanishing, but no exact \(AB\) identity is supplied here.

An \(AB\) theorem requires either an exact degreewise polarization identity

\[
\sum_{\alpha\in AB}
R_\pm^{AB}(\alpha)\otimes S_\pm^{AB}(\alpha)=0
\]

or the missing global chirality-intertwining theorem. The main theorem’s claim “every spectral sector (AA, BB, AB)” must therefore be reduced to \(AA/BB\) pending that argument.

## 6. Remaining assumptions and gaps

The implemented-model identity depends on:

- exact bilinearity of the leading receiver/source maps;
- complete exact \(R_\pm,S_\pm\) tables;
- equal normalized weights in cancelling polarization pairs;
- equal \(c_2/s_2\) weights;
- common Green eigenvalue factors across degenerate modes;
- the reflected node-frame transport producing \(\eta_c=-\eta_s\);
- correct quotient and isotropy multiplicities;
- completeness of the selected electric/full-Lie magnetic families;
- identification of the Step 96 \(H^4\) boundary functional with the actual Ozuch distributional source.

Step 99 does establish useful partial bridge facts: mixed derivative support is invisible, and omitted same-factor tensor jets for the selected electric/full-Lie magnetic families contract exactly to zero. It does not settle completeness, geometric source identification, quotient normalization, or frame transport.

The finite JSON tests are regression evidence, not an all-degree proof; they test neither \(--\) nor \(AB\).

## 7. Consequence for the full Ozuch equation

The cancellation controls only selected inter-node terms in

\[
F_i=
F_i^{\rm self}
+F_i^{\rm deform}
+\sum_{j\ne i} B_{ij}
+F_i^{\rm complement}
+F_i^{\rm projector}
+R_i.
\]

It does not imply positivity or insolubility of the total projected equation. Self, deformation, complement, and projector-motion terms may have components in the same trace or spin-2 directions as the positive mixed-chirality inter-node response and can cancel it. Chirality-independence of a self term does not make that term zero.

In particular, the positive isotropic response reported in the earlier calculation is carried by the \(AB\) sector—the sector not proved structurally here. To turn that response into an obstruction one would need to compute the remaining leading terms in the same normalization and show that their attainable image excludes the positive direction, together with compatible remainder estimates.

## Corrected theorem statement

A defensible statement is:

> For receiver \(NN\), each distinct source node, and every degree pair, the implemented \(AA/BB\) tensor–scalar \(++\) inter-node block vanishes, assuming the stated exact coefficient maps, polarization weights, quotient factors, and reflected node-frame transport. The same proof gives \(--\) once the complete minus-map table is supplied. No \(AB\) conclusion or conclusion about the full Ozuch projected equation follows from this argument alone.