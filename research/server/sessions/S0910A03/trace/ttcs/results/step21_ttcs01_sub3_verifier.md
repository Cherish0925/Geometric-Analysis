# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step21_derivative_free_first_exit_and_plateau_regularity.md",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/scripts/verify_step21_derivative_free_first_exit.py"
  ]
}
```

## Task

Verify the following mathematical chain for the 4D negative-branch cutoff-flow program on a critical Ishida-LeBrun manifold M.

(1) NORMALIZATION LOWER-ORDER: Under dt g = -2 chi^2 (Ric+g), the normalization -2 chi^2 g changes the curvature evolution by: (a) volume form -a(s+4)dmu with |s+4| ≤ 4 delta; (b) curvature: -(nabla^2 a) ☐ g + O(|nabla a||Rm|), which is lower order than the critical cubic reaction a|Rm|^2 in H_q. Verify that the critical parameter beta = A_0^2 ||Rm||_2 is unchanged, and that the normalization contributes only an exponential Gronwall factor e^{CT_0}.

(2) INTERIOR REGULARITY ON PLATEAU: After the first-exit gives |chi^2 Rm| ≤ C gamma/t uniformly on [0, T_0], on the plateau {chi=1} the flow becomes dt g = -2(Ric+g), a normalized Ricci flow. Since a=1 there, |Rm| ≤ C gamma/t. Standard Shi interior estimates on [T_0/2, T_0] x B_{rho/32}(p) should give |nabla^k Rm| ≤ C_k (T_0/2)^{-k/2}. Verify: (a) Does the normalized Ricci flow (with the -2g term) satisfy standard Shi estimates? (b) Are the Shi constants independent of the sequence index? (c) Does this give smooth compactness on the exponential chart?

(3) EXPONENTIAL CHART TO CONTRADICTION: For the limit h_inf on B_{R/2}(0) from Arzela-Ascoli: (a) Does |E_i(T_0)| → 0 follow from |chi^2 E| ≤ C delta_i (r^2/T_0)^{1/3}? (b) Does the 7/24 calibration inequality transfer through the flow and chart, giving |W+| = 1/(2sqrt6) on the limit? (c) Is the projector obstruction (simple eigenform → parallel → nabla W+ = 0 vs |nabla W+|^2 = 1/16) correctly stated?

(4) POTENTIAL GAPS: Are there any gaps in the chain from the first-exit output to the projector contradiction? In particular: does metric comparability correctly transfer the global Q control through the exponential chart? Does the good-center selection correctly provide nontrivial monopole data on the limit? Does the chart pullback preserve the all-derivative bounds from Shi?

## Output

# Scientific verification memo

## Overall assessment

The plateau regularity and exponential-chart compactness mechanisms are mathematically sound once the stated first-exit outputs, terminal \(L^2\)-defect control, and a quantitatively good chart center are available. Several formulas in the normalization discussion need correction, and the final projector step requires monopole eigenline data in addition to the Weyl-modulus calibration.

The most important discontinuities are:

1. \(|s+4|\le 4\delta\) is available at the initial slice, not automatically throughout the first-exit interval.
2. The cutoff normalization produces a cutoff-scale coefficient \(r^{-2}\); the resulting factor is generally \(e^{C(T_0/r^2+T_0)}\), not merely \(e^{CT_0}\).
3. The \(7/24\) inequality does not pass directly to a possibly many-sheeted exponential chart. The exponential averaging lemma is essential.
4. Constant \(|W^+|\) and \(s=-4\) do not determine the spectrum of \(W^+\). A nonzero limiting monopole form in the lowest eigenspace is essential.
5. Step 21 uses the defect-energy system \(Q_\alpha\) to improve an exit condition stated for curvature energy \(H_2\). These are different quantities.

---

## 1. Effect of the normalization

Let
\[
E=\operatorname{Ric}+g,\qquad a=\chi^2,\qquad \partial_tg=-2aE.
\]

### 1.1 Volume form

The exact formula in dimension four is
\[
\partial_t d\mu
=\frac12\operatorname{tr}_g(\partial_tg)d\mu
=-a(s+4)d\mu
=-a\,\operatorname{tr}_gE\,d\mu.
\]

If \(|E(g_0)|\le\delta\), then at \(t=0\)
\[
|s+4|=|\operatorname{tr}E|\le 2|E|\le2\delta
\]
for the Hilbert–Schmidt tensor norm; \(4\delta\) is also a valid looser estimate. At later times, however, an unweighted estimate \(|s+4|\le4\delta\) has not been established. What follows from the defect Moser output is
\[
|a(s+4)|\le C|aE|
\le C\delta\left(\frac{r^2}{t}\right)^{1/3},
\]
which is integrable at \(t=0\).

Before the defect estimate has been derived, the evolving-measure term must instead be included in the curvature reaction using
\[
|a\,\operatorname{tr}E|\le CaF.
\]
Thus the initial pinching constant cannot be inserted into the measure evolution during the curvature-first part of the argument without circularity.

### 1.2 Curvature variation from \(-2ag\)

For covariant curvature, the conformal variation has schematic form
\[
D\operatorname{Rm}_g[-2ag]
=-2a\,\operatorname{Rm}
+\mathcal K_g(\nabla^2a),
\]
where \(\mathcal K_g(\nabla^2a)\) is a Kulkarni–Nomizu expression; its overall sign depends on curvature convention. There is no intrinsic
\[
|\nabla a|\,|\operatorname{Rm}|
\]
term in this isolated tensor variation. First derivatives of \(a\) appear after integrating the Hessian term by parts, or when differentiating higher-order equations.

For the weighted \(H_q\) calculation, integration by parts and
\[
\frac{|da|^2}{a}=4|d\chi|^2
\]
give terms of the form
\[
\varepsilon D_q
+C_{\varepsilon,q}(r^{-2}+1)H_q,
\]
in addition to the usual critical curvature reaction. With
\[
F=(1+|\operatorname{Rm}|^2)^{1/2},
\]
the apparent constant source from \(\nabla^2a\) can be absorbed into \(H_q\), since \(F\ge1\). Without this regularization it appears as an explicit volume term.

Consequently, for fixed \(q\), the lower-order growth factor is naturally
\[
\exp\!\left[C_q\left(\frac{T_0}{r^2}+T_0\right)\right].
\]
At \(T_0=\theta r^2\), this becomes
\[
e^{C_q(\theta+\theta r^2)}.
\]
It introduces no new critical Sobolev smallness requirement, but it is not accurately represented by \(e^{CT_0}\) unless the cutoff scale has already been absorbed into \(C\).

There is also a useful structural cancellation: the full velocity is \(-2aE\), so if \(E=0\), the metric is stationary even when \(a\) varies. Treating \(-2ag\) separately creates a Hessian-\(a\) source which cancels the corresponding part from \(-2a\operatorname{Ric}\) at \(E=0\). The full homogeneous \(E\)-equation is therefore the cleaner object.

### 1.3 The critical parameter

The initial quantity
\[
\beta=A_0^2\|\operatorname{Rm}(g_0)\|_{L^2}
\]
is independent of which evolution equation is subsequently used. In that sense the normalization does not alter \(\beta\).

It is not dynamically invariant: the evolving quantity
\[
A(t)^2\|\operatorname{Rm}(g(t))\|_2
\]
still requires the Sobolev and local-energy estimates in the first-exit construction. Moreover, because the curvature hierarchy uses \(F=(1+|\operatorname{Rm}|^2)^{1/2}\), the actual parameter is
\[
\gamma=A_0^2\|F\|_2,
\qquad
\gamma\le \beta+Cr^2.
\]
Thus the normalization does not change the critical absorption mechanism, but the rigorous hierarchy is expressed using \(\gamma\), not solely \(\beta\).

---

## 2. Shi regularity on the plateau

### 2.1 Normalized Ricci flow satisfies Shi estimates

On an open region where \(\chi=1\),
\[
\partial_tg=-2(\operatorname{Ric}+g).
\]
This is locally equivalent to ordinary Ricci flow. Define
\[
\widetilde g(\tau)=e^{2t}g(t),
\qquad
\tau=\frac{e^{2t}-1}{2}.
\]
Then
\[
\frac{\partial\widetilde g}{\partial\tau}
=-2\operatorname{Ric}_{\widetilde g}.
\]
Ordinary local Shi estimates therefore transfer to \(g(t)\), with harmless factors depending on the finite interval \(0\le t\le T_0\). Equivalently, one may prove the estimates directly from the normalized curvature equation, whose extra terms are linear in curvature and its derivatives.

No finite-propagation assertion is needed. One only needs a spatially buffered region on which \(\chi\equiv1\) throughout the parabolic cylinder.

### 2.2 Correct form of the estimate

Set
\[
K=\frac{2C\gamma}{T_0}.
\]
On \(t\in[T_0/2,T_0]\), the first-exit estimate gives
\[
|\operatorname{Rm}|\le K
\]
on the plateau. If \(p\) lies a uniform distance \(d>0\) from \(M\setminus\{\chi=1\}\), a standard local estimate has the form
\[
|\nabla^k\operatorname{Rm}|(p,T_0)
\le C(n,k,T_0)\,
K\left(K^{k/2}+(T_0/2)^{-k/2}+d^{-k}\right).
\]
Thus the displayed expression
\[
C_k(T_0/2)^{-k/2}
\]
is acceptable only as shorthand when \(K\), \(d^{-1}\), and \(T_0\) have already been absorbed into \(C_k\).

The constants are independent of the sequence index provided the following quantities are uniform:

- \(T_0=\theta r^2>0\);
- \(\gamma/T_0\);
- the plateau buffer \(d\);
- metric equivalence between \(g_i(t)\) and \(g_i(0)\);
- the cutoff-scale parameters.

If \(r_i\) or the plateau buffer tends to zero, Shi constants need not remain uniform. The notes intend \(r\) and the nested plateau widths to be fixed from the uniform local-energy construction; that uniformity must be part of the first-exit theorem.

### 2.3 Exponential-chart compactness

Choose an oriented \(g_i(T_0)\)-orthonormal frame at \(p_i\) and identify \(T_{p_i}M\cong\mathbb R^4\). If
\[
R<\min\left\{c\,d,\frac{\pi}{2\sqrt K}\right\},
\]
then
\[
h_i=(\exp_{p_i}^{g_i(T_0)})^*g_i(T_0)
\]
is a smooth Riemannian metric on \(B_R(0)\), even if the exponential map is not globally injective. Rauch comparison excludes conjugate points on this ball.

Because the exponential map is a local isometry,
\[
\nabla_{h_i}^k\operatorname{Rm}_{h_i}
=(\exp_{p_i})^*
\nabla_{g_i(T_0)}^k\operatorname{Rm}_{g_i(T_0)}
\]
wherever the map is nonsingular. Hence the intrinsic derivative bounds are preserved exactly.

For coordinate \(C^\infty\) compactness, one also uses the Jacobi equation:

- Rauch comparison gives uniform ellipticity of \(h_i\) relative to the Euclidean metric;
- bounds on all covariant derivatives of curvature give bounds on all coordinate derivatives of \(h_i\) in exponential coordinates.

The chart-volume lower estimate alone would not imply smooth compactness, but the exponential-coordinate and Jacobi estimates do. After reducing the radius, a \(C^\infty\) subsequence exists.

---

## 3. Passage to the Einstein germ and the projector contradiction

### 3.1 Vanishing of the terminal defect

On the plateau, \(a=1\), so
\[
|E_i(T_0)|
\le C\delta_i\left(\frac{r^2}{T_0}\right)^{1/3}
=C\delta_i\theta^{-1/3}\longrightarrow0.
\]
This remains true after exponential pullback. Smooth metric convergence then gives
\[
\operatorname{Ric}_{h_\infty}+h_\infty=0.
\]

### 3.2 Calibration is reapplied at the terminal metric

The \(7/24\) estimate is metric-by-metric:
\[
\int_M
\left(|W^+_{g_i(T_0)}|-\frac1{2\sqrt6}\right)^2d\mu_{g_i(T_0)}
\le\frac7{24}Q_i(T_0).
\]
It is not an evolution identity. It is applied anew to the terminal metric.

To make its right side tend to zero one needs
\[
Q_i(T_0)\le C Q_i(0).
\]
Metric comparability alone does not provide this, since \(E(T_0)\) and \(E(0)\) are different tensors. The triangular defect-energy system is the relevant input.

At the initial slice,
\[
Q_i(0)\le\delta_i^2\operatorname{Vol}(g_i(0)).
\]
A uniform volume upper estimate can be obtained from
\[
4\pi^2(2\chi+3\tau)
=\int_M\left(
2|W^+|^2+\frac{s^2}{24}
-\frac{|\operatorname{Ric}_0|^2}{2}
\right)d\mu.
\]
Since \(s=-4+O(\delta_i)\) and \(\operatorname{Ric}_0=O(\delta_i)\),
\[
c\,\operatorname{Vol}(g_i)
\le 4\pi^2(2\chi+3\tau)
+C\delta_i^2\operatorname{Vol}(g_i),
\]
and the final term is absorbed for small \(\delta_i\). Thus \(Q_i(0)\to0\) on a fixed manifold.

### 3.3 Global calibration does not directly imply chart calibration

The exponential map may have arbitrarily many sheets. Therefore
\[
\int_M d_i\to0
\]
does not by itself imply
\[
\int_{B_R(0),h_i}d_i\circ\exp_{p_i}\to0
\]
for an arbitrary center.

The exponential averaging lemma is exactly what repairs this. It requires
\[
\frac{\int_M\mathcal D_i\,d\mu_i}
     {\operatorname{Vol}(P_i)}
\longrightarrow0
\]
for the allowed center set \(P_i\), together with geodesic containment in the bounded-curvature plateau. A uniform lower volume for \(P_i\), or a relation
\[
\operatorname{Vol}(P_i)\ge c\,\operatorname{Vol}(M,g_i)
\]
combined with \(\int\mathcal D_i=O(\delta_i^2\operatorname{Vol}M)\), would suffice. Step 21 does not explicitly establish either relation.

### 3.4 Weyl modulus alone does not determine the spectrum

The inference
\[
\operatorname{Ric}=-g,\qquad
|W^+|=\frac1{2\sqrt6}
\quad\Longrightarrow\quad
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
is not valid without additional information. For instance, the trace-free spectrum
\[
\left(
-\frac1{4\sqrt3},\,0,\,\frac1{4\sqrt3}
\right)
\]
has the same squared norm \(1/24\).

The needed extra information is the nonzero monopole eigenline. With
\[
\mathscr A_i
=W_i^++\sqrt{\frac23}|W_i^+|I,
\]
the joint density from Step 16 must select a terminal-metric harmonic form \(H_i\) such that, after pullback and elliptic extraction,
\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0,
\qquad
\mathscr A_\infty H_\infty=0.
\]
Since
\[
\sqrt{\frac23}|W_\infty^+|=\frac16,
\]
\(H_\infty\) is an eigenform with eigenvalue \(-1/6\). Trace zero and \(|W^+|^2=1/24\) then force the other two eigenvalues to equal \(1/12\).

Thus the good-center argument must use the full joint density \(\mathcal D_i\), not only the \(7/24\) density. The monopole objects must also be reconstructed for \(g_i(T_0)\); transporting initial harmonic representatives through the flow would not suffice.

### 3.5 Projector obstruction

Once the spectrum
\[
\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
is established, the local obstruction is correct.

For an Einstein four-metric, \(\delta W^+=0\). Writing
\[
W^+=\frac1{12}I-\frac14P,
\]
where \(P\) is the rank-one spectral projector, the divergence-free Weyl equation together with constant eigenvalues gives \(\nabla P=0\) by the standard Derdziński/projector calculation. Hence
\[
\nabla W^+=0.
\]

On the other hand, the Einstein–Weyl identity is
\[
\frac12\Delta|W^+|^2
=|\nabla W^+|^2+\frac{s}{2}|W^+|^2
-18\det W^+.
\]
Here
\[
s=-4,\qquad |W^+|^2=\frac1{24},
\qquad \det W^+=-\frac1{864}.
\]
Since \(|W^+|\) is constant,
\[
0=|\nabla W^+|^2-\frac1{12}+\frac1{48},
\]
so
\[
|\nabla W^+|^2=\frac1{16}.
\]
This contradicts \(\nabla W^+=0\).

---

## 4. Remaining discontinuities in the written chain

1. **Curvature versus defect exit quantity.**  
   Step 21 defines (F3) using curvature energy \(H_2\), but Step V invokes equation (4.1) for defect energy \(Q_\alpha\). The latter cannot improve the former. Curvature \(H_2\) persistence needs its own finite-neighbor estimate derived from the \(q=2\) curvature hierarchy.

2. **Terminal \(Q\) estimate.**  
   The relation \(Q(T_0)\le C Q(0)\) comes from the homogeneous defect-energy system, not from metric comparability. The finite-neighbor implementation remains unwritten in the supplied notes.

3. **Chart-center denominator.**  
   The averaging lemma selects a useful center only when \(\int\mathcal D_i/\operatorname{Vol}(P_i)\to0\). A shrinking plateau can obstruct this even when \(\int_M\mathcal D_i\to0\).

4. **Monopole eigenline.**  
   The Step 21 contradiction paragraph omits the nonzero limiting harmonic form. Without it, the Weyl spectrum is undetermined.

5. **Spatial buffers.**  
   The Shi cylinder, the exponential geodesics, and the larger chart needed for elliptic estimates on \(H_i\) must all remain inside \(\{\chi=1\}\). Nested fixed radii provide this if stated explicitly.

6. **First-exit PDE recurrence.**  
   The notes themselves leave the finite-neighbor Moser recurrence and triangular defect estimate unresolved. The Python script verifies exponent arithmetic and sample growth factors only; it does not derive the tensor inequalities, smooth continuation, or chart selection.

Subject to these missing derivations and the corrected center selection, the passage
\[
\text{first-exit outputs}
\;\Longrightarrow\;
\text{plateau Shi regularity}
\;\Longrightarrow\;
\text{smooth exponential-chart limit}
\;\Longrightarrow\;
\text{monopole spectral saturation}
\;\Longrightarrow\;
\text{projector contradiction}
\]
is mathematically coherent.