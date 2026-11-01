# TTCS Independent Branch Record

```json
{
  "step_id": 98,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step98_trace_obstruction_theorem.md",
    "Sessions/S0910A01/workspace/notes/step97_ab_physical_cone_interpretation.md",
    "Sessions/S0910A01/workspace/scripts/step98_full_chirality_tensor_maps.py",
    "Sessions/S0910A01/workspace/notes/step96_source_compatible_kernel_map.md"
  ]
}
```

## Task

Verify the mathematical content and logical soundness of the Step 98 trace obstruction theorem for the product-orbifold Ozuch desingularization. The key claims to verify are:

1. SAME-CHIRALITY VANISHING: B_{++} = B_{--} = 0 for all spectral sectors and pairs. The argument is that B_ee = -B_oo exactly (verified computationally) and cross-parity blocks vanish by K-symmetry. Is this a structural identity or a numerical coincidence? Is there a representation-theoretic reason that same-chirality pairs should give zero response?

2. TRACE OBSTRUCTION: The AB sector gives cross-chirality trace c0 = 4a ≈ 0.1258 for adjacent pairs. For the mixed pattern, this sums to 0.503 t^2 at equal scales. The argument that this is a genuine obstruction relies on: (a) self-terms are pattern-independent, (b) all-same has zero inter-node trace (by B_same=0), (c) KE existence implies self-trace is solvable independently. Does this argument work? Are there loopholes?

3. TRACE VS P/Q: The claim that the trace channel is independent of the P/Q (traceless) channel and that the trace obstruction alone suffices. Is this correct in the Ozuch framework?

4. The P/Q channel structure: NN←NS has pure Q (anti-holomorphic from AA tensor on factor A), while NN←SN has pure P (holomorphic from BB tensor on factor B). Is this consistent with the product structure and chirality conventions?

## Output

# Scientific verification memo: Step 98 product-orbifold trace obstruction

## Main assessment

The supplied computation reveals a potentially useful **relative inter-node interaction** for the checkerboard chirality pattern, but it does not yet establish the stated Ozuch desingularization theorem. Four points are decisive:

1. \(B_{++}=B_{--}=0\) is numerically observed in the selected mode calculations, but \(B_{ee}=-B_{oo}\) is an additional identity not implied by \(K\)-parity. No exact modewise or representation-theoretic derivation is supplied.
2. The trace arithmetic in Step 98 §5 has an extra factor \(2\): the two adjacent AB contributions give \(8a\,t^{2}\approx0.25154\,t^{2}\), not \(0.50308\,t^{2}\). The symbolic coefficient \(8a\) in theorem part (b) is the consistent one.
3. Existence of an all-same Kähler–Einstein filling does not imply that the self term vanishes separately. It only constrains the complete all-same gluing equation at the parameters of that family.
4. According to Step 97, the physical receiving equation is \(A_i u_i=0\), equivalently its radial and angular projections, rather than \(A_i=0\). Trace and traceless components therefore interact in the radial equation. The reported coefficients nevertheless make the computed **inter-node matrix positive definite**, which is stronger and more relevant than its trace being nonzero.

---

## 1. Same-chirality vanishing

Let \(B_{rs}\), \(r,s\in\{+,-\}\), denote the raw maps. The parity transforms used in `step98_full_chirality_tensor_maps.py` give

\[
\begin{aligned}
B_{ee}&=\frac14(B_{++}+B_{+-}+B_{-+}+B_{--}),\\
B_{eo}&=\frac14(B_{++}-B_{+-}+B_{-+}-B_{--}),\\
B_{oe}&=\frac14(B_{++}+B_{+-}-B_{-+}-B_{--}),\\
B_{oo}&=\frac14(B_{++}-B_{+-}-B_{-+}+B_{--}).
\end{aligned}
\]

Thus \(B_{eo}=B_{oe}=0\) implies

\[
B_{++}=B_{--}=B_{ee}+B_{oo},\qquad
B_{+-}=B_{-+}=B_{ee}-B_{oo}.
\]

This algebra is correct. However,

\[
B_{ee}=-B_{oo}
\]

is logically independent of cross-parity vanishing. It is exactly the extra identity needed to obtain \(B_{++}=B_{--}=0\).

### What \(K\)-symmetry can prove

If an involutive isometry \(\kappa\)

- fixes the ordered receiver/source pair,
- commutes with the projected Green operator,
- preserves the node-frame conventions, and
- gives opposite parity to the source and receiver factors,

then \(B_{eo}=B_{oe}=0\) follows exactly. If \(\kappa\) exchanges nodes or rotates the kernel planes, it instead gives a conjugacy relation between different ordered blocks; individual mixed-parity blocks need not vanish without incorporating that transport.

No analogous consequence forces \(B_{ee}=-B_{oo}\). Product symmetry permits nonzero equivariant maps such as

\[
M\longmapsto \operatorname{tr}(M)I_K
\]

and spin-two maps on \(\operatorname{Sym}^2_0(K)\). Therefore the usual product isotropy does not by itself prohibit same-chirality response. An exact vanishing would need an additional chiral involution whose action pairs the even and odd spectral contributions with opposite signs, or a pointwise algebraic identity in the receiver/source tensors.

### What the script currently establishes

The script evaluates floating-point spectral sums and rounds stored matrices to twelve decimal places. It does not store a direct unrounded norm of \(B_{ee}+B_{oo}\) or \(B_{++}\); the explicit numerical tests recorded in the code concern \(B_{eo},B_{oe}\), \(B_{++}-B_{--}\), and \(B_{+-}-B_{-+}\). A modewise identity such as

\[
B_{++}^{(\ell_t,\ell_s,\mathrm{polarization})}=0
\]

would turn the observation into exact algebra, but that identity is not derived in the supplied files.

There is also a completeness issue visible directly in the code. For the AA/BB sectors, `tensor_scalar_hessian` includes only the component

\[
H_{ab\,mn}=T_{ab}\,(\nabla^2 f)_{mn},
\]

built from the tensor value on one factor and a scalar Hessian on the other. Step 96 §6 explicitly states that full electric and magnetic tensor jets were still absent. Low modes, deformation modes, projector motion, and other product eigentensor components are not incorporated here. Consequently “all spectral sectors” is stronger than what this script computes.

Finally, the ladder changes both \(\tau\) and \(L_{\max}\). It supplies useful numerical stability evidence, but no estimate controls the joint limits \(\tau\to0\) and \(L_{\max}\to\infty\). The `tail_indicator` is an absolute shell sum at fixed heat regularization, not a certified estimate for the unregularized Green kernel.

---

## 2. AB trace normalization and the factor-of-two error

From Step 96,

\[
B^{AB}_{ee}=aJ,\qquad B^{AB}_{oo}=-aJ,
\qquad
J(M)=\operatorname{tr}(M)I_K.
\]

Therefore the cross-chirality map is

\[
B^{AB}_{+-}=B^{AB}_{ee}-B^{AB}_{oo}
=2aJ,
\]

so for \(M_j=t_j^2u_ju_j^T\),

\[
A^{AB}_{ij}=2a\,t_j^2 I_K.
\]

Hence

\[
\operatorname{tr}A^{AB}_{ij}=4a\,t_j^2.
\]

This agrees with the script’s definition

\[
c_0=A_{xyz}[0,0]=\frac{\operatorname{tr}A}{\operatorname{tr}M}=4a.
\]

For the two adjacent cross-chirality sources at NN,

\[
\operatorname{tr}A_{\rm NN}^{\rm inter}
=4a(t_{\rm NS}^2+t_{\rm SN}^2).
\]

At equal scales,

\[
\operatorname{tr}A_{\rm NN}^{\rm inter}
=8a\,t^2
\approx 0.25154\,t^2.
\]

Thus Step 98 §5’s value \(0.50308\,t^2\) counts the matrix trace twice. The theorem’s symbolic expression \(8a\,t^2\) is consistent with the definitions.

The physical radial AB contribution is half the trace:

\[
u_i^TA^{AB}_{ij}u_i=2a\,t_j^2.
\]

For two adjacent equal-scale sources this is \(4a\,t^2\); after the receiver factor \(t_i=t\), it becomes

\[
4a\,t^3\approx0.12577\,t^3,
\]

exactly matching Step 97.

---

## 3. Why the all-same comparison does not isolate the self term

A schematic leading gluing equation has the form

\[
F_i^\varepsilon(p)
=
F_i^{\rm local}(p)
+
F_i^{\rm deformation,\varepsilon}(p)
+
\sum_{j\ne i}B_{ij}^{\varepsilon_i\varepsilon_j}(M_j)
+
R_i^\varepsilon(p),
\]

where \(p\) contains scales, directions, orbifold deformation variables, chart choices, and correction parameters.

Even assuming all same-chirality inter-node blocks vanish, existence of an all-same desingularizing family only gives

\[
F_i^{\rm local}(p_{\rm KE})
+
F_i^{\rm deformation,+}(p_{\rm KE})
+
R_i^+(p_{\rm KE})=0
\]

along that particular family. It does not imply that any one summand vanishes separately, nor that their sum vanishes at parameter values relevant to the mixed pattern.

Pattern independence as an algebraic formula is also insufficient for cancellation between two solutions evaluated at different scales, directions, or deformation parameters. Moreover, a background deformation tensor may be independent of the chirality assignment before projection while its projections into \(R^+\) and \(R^-\), and then into \(K_i\), depend on \(\varepsilon_i\).

The supplied material also does not include a source establishing that the known Kähler–Einstein metric on the all-same smooth filling occurs in a family degenerating to this precise orbifold with the same Ozuch parameterization. Existence of an Einstein metric elsewhere on the same smooth manifold does not by itself provide that asymptotic calibration.

Thus the current calculation proves that, at the same parameter point, the mixed row differs from the all-same row by the displayed inter-node matrix. It does not yet exclude cancellation after the mixed scales and deformation variables are varied.

---

## 4. Trace versus \(P/Q\) in the physical equation

Write

\[
A=
\frac{X}{2}I+
\frac12
\begin{pmatrix}
Y&Z\\
Z&-Y
\end{pmatrix},
\qquad X=\operatorname{tr}A.
\]

For \(u=(\cos\theta,\sin\theta)\),

\[
u^TAu
=
\frac12\left(
X+Y\cos2\theta+Z\sin2\theta
\right),
\]

and

\[
(u^\perp)^TAu
=
\frac12\left(
-Z_{\!0}\right)
=
\frac12\left(
Z\cos2\theta-Y\sin2\theta
\right).
\]

Therefore trace and traceless components are independent coordinates in
\(\operatorname{Sym}^2(K)\), but they are **not independent physical equations** when the receiving equation is \(Au=0\). A traceless component can offset \(X/2\) in the radial projection.

A nonzero trace alone excludes \(A=0\), but it does not exclude \(Au=0\) for some \(u\). For example, a rank-one matrix has nonzero trace and a one-dimensional kernel.

### Stronger consequence of the reported coefficients

The Step 98 coefficients nevertheless give a useful angle-independent lower bound. With

\[
\zeta=\frac{Y+iZ}{2}=Pw+Q\bar w,\qquad |w|=t_j^2,
\]

the operator norm of the traceless matrix equals \(|\zeta|\). Thus the adjacent NS block has the form

\[
A_{\rm NS}
=
2a\,t_{\rm NS}^2 I+T_Q,
\qquad
\|T_Q\|=|Q|t_{\rm NS}^2,
\]

and similarly

\[
A_{\rm SN}
=
2a\,t_{\rm SN}^2 I+T_P,
\qquad
\|T_P\|=|P|t_{\rm SN}^2.
\]

Using \(2a\approx0.062885\) and \(|P|=|Q|\approx0.00800\),

\[
u^TA_{\rm inter}u
\ge
(2a-|Q|)t_{\rm NS}^2+
(2a-|P|)t_{\rm SN}^2>0
\]

for every receiver and source angle. At equal scales, the lower bound is approximately

\[
0.10977\,t^2.
\]

Thus the computed relative inter-node matrix is positive definite, not merely nonzero in trace. This is the appropriate matrix statement for the physical cone. It still concerns only the included inter-node blocks and does not eliminate local or deformation contributions of the opposite sign.

---

## 5. \(P/Q\) product structure

The support pattern is compatible with product separation:

- AA is active for \(NN\leftarrow NS\), where source and receiver share the A pole.
- BB is active for \(NN\leftarrow SN\), where they share the B pole.
- The selected tensor-scalar mixed jets vanish for the opposite corner \(NN\leftarrow SS\).

The equality of the two reported magnitudes also agrees with factor-exchange symmetry.

The distinction “AA is pure \(Q\), BB is pure \(P\)” is more delicate. Under orientation-preserving rotations of the kernel frames, \(P\) and \(Q\) acquire phases but remain holomorphic and antiholomorphic, respectively. A reflection at either source or receiver interchanges these roles. Step 97 explicitly records that the node-frame transport matrices were not yet fixed, and the Step 98 script contains no \(U_{ij}\) transport. Consequently:

- the zero/nonzero pattern and absolute magnitudes are meaningful numerical features;
- the labels \(P\) versus \(Q\) are not yet invariant geometric statements;
- factor exchange can naturally turn one into the other through conjugation of the double-angle coordinate.

## Conclusion

The strongest mathematically supported interpretation is a **numerically observed, angle-uniform, positive-definite relative inter-node contribution** for the mixed diagonal pattern in the selected AB/AA/BB mode model. The complete Ozuch obstruction theorem additionally needs:

- an exact derivation of \(B_{ee}=-B_{oo}\);
- a complete product spectral decomposition with full tensor jets and low/deformation modes;
- explicit node and chirality frame transport;
- controlled Green-kernel limits;
- the full leading projected gluing equation, including parameter dependence and a remainder smaller than the displayed cubic term;
- a precise degeneration statement for the all-same Kähler–Einstein family.

Without those ingredients, the all-same comparison does not yet turn the computed relative interaction into nonexistence of the mixed desingularization.