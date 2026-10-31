# TTCS Independent Branch Record

```json
{
  "step_id": 36,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/step36_cap_perp_transplant.py",
    "Sessions/S1003A01/workspace/data/step36/cap_perp_baseline_scan.json",
    "Sessions/S1003A01/workspace/data/step36/cap_perp_width_scan.json",
    "Sessions/S1003A01/workspace/data/step36/cap_perp_response_opt_pilot.json",
    "Sessions/S1003A01/workspace/data/step36/cap_perp_response_validation.json",
    "Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md",
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py"
  ]
}
```

## Task

Independently read the corrected Step-35 note and the Step-36 transplant script/data. Check the mathematical realization and numerical interpretation of the finite-amplitude perpendicular cap trial: scale from Ric=-6 to Ric=-1; CH exponential chart reconstruction; exact Calabi cap in proper normal Cartesian coordinates; smoothness/positivity of the convex interpolation and response tensors; core-plus-annulus integration; normalization of D, P, scalar moments, and the relative chiral ledger. Identify any formula or implementation error that could change the reported conclusion. The key reported observation is that the direct baseline costs D/(8pi^2) about 2.44 at the best scanned pair (a,b)=(0.5,1.5), while three response modes lower it only to about 2.26 on independent QMC seeds, still far above both 1 and the certified CH cell 0.99567003. Also assess what this finite trial establishes about cap geometry and what it leaves open. Do not assume the withdrawn same-class Theorem N.

## Output

# Independent scientific verification memo

## 1. Main result

The scale conversion, coordinate reconstructions, curvature normalization, core-plus-annulus decomposition, and relative chiral formulas in `step36_cap_perp_transplant.py` are mathematically consistent. I do not find a factor, sign, Jacobian, or Einstein-constant error capable of moving the reported values
\[
\frac{D}{8\pi^2}\simeq2.44\quad\text{or}\quad 2.26
\]
toward \(1\).

The supplied computation supports the following narrower statement:

- The direct convex transplant at \((a,b)=(0.5,1.5)\) has
  \[
  \frac{D}{8\pi^2}=2.44057,\qquad
  \frac{P}{8\pi^2}=1.68279.
  \]
- The three fitted transition tensors reduce the independently sampled values to
  \[
  \frac{D}{8\pi^2}=2.25792,\ 2.26806,\ 2.26950,
  \]
  with mean \(2.26516\) and seed-to-seed range about \(0.0116\).
- The corresponding annular contributions remain about \(1.80\), compared with the preserved core contribution \(0.459454\). Thus the transition, rather than the bolt core, dominates this construction.
- These values lie well above both \(1\) and the certified CH value \(0.995670030355131\).

This is evidence about the specified finite-dimensional transplant family. It is not a lower bound for the cap-cell infimum and does not exclude a cap-adapted \(U(1)_-\)-invariant cell, another marking, a different interpolation, or a richer finite-amplitude response.

---

## 2. Rescaling from \(\operatorname{Ric}=-6g\) to \(\operatorname{Ric}=-g\)

Let \(g_1=6g_6\), where \(\operatorname{Ric}(g_6)=-6g_6\). Constant rescaling leaves the covariant Ricci tensor unchanged, so
\[
\operatorname{Ric}(g_1)=\operatorname{Ric}(g_6)=-6g_6=-g_1.
\]
In dimension four,
\[
dV_{g_1}=36\,dV_{g_6},\qquad s_{g_1}=\frac{s_{g_6}}6.
\]
Consequently,
\[
\begin{aligned}
\int |\operatorname{Ric}(g_1)+g_1|_{g_1}^{2}\,dV_{g_1}
 &=\int |\operatorname{Ric}(g_6)+6g_6|_{g_6}^{2}\,dV_{g_6},\\
\int |\operatorname{Ric}^{\circ}(g_1)|_{g_1}^{2}\,dV_{g_1}
 &=\int |\operatorname{Ric}^{\circ}(g_6)|_{g_6}^{2}\,dV_{g_6},\\
V(g_1)&=36V(g_6),\\
\int s_{g_1}\,dV_{g_1}&=6\int s_{g_6}\,dV_{g_6},\\
\int s_{g_1}^{2}\,dV_{g_1}&=\int s_{g_6}^{2}\,dV_{g_6}.
\end{aligned}
\]
These are exactly the transformations used in `core_integrals`.

The old-core formula
\[
|\operatorname{Ric}+6g|^2
=|\operatorname{Ric}^{\circ}|^2+\frac{(s+24)^2}{4}
\]
is also correct in four dimensions.

---

## 3. CH exponential-chart reconstruction

Writing \(r=|\xi|\) for distance in the scaled CH metric,
\[
x=\sinh^2\!\left(\frac r{\sqrt6}\right),\qquad
\frac{dx}{dr}=\frac{2\sqrt{x(1+x)}}{\sqrt6}.
\]
Hence the scaled radial term satisfies
\[
6\,\frac{dx^2}{4G}
=\frac{x(1+x)}{G}\,dr^2,
\]
which is the first entry of `lam` in `metric_xi`.

The four vectors in `frames0` are mutually orthogonal in the Euclidean metric, each has length \(r\), and the final vector \(iz\) is the Hopf direction. Therefore the remaining scaled eigenvalues are correctly represented as
\[
\frac{6h_{11}}{r^2},\qquad
\frac{6h_{22}}{r^2},\qquad
\frac{6h_{33}}{r^2}.
\]
At an exact CH profile,
\[
G=x(1+x),\qquad h=\operatorname{diag}(x,x,x(1+x)),
\]
so this gives radial eigenvalue \(1\), two horizontal eigenvalues \(6x/r^2\), and Hopf eigenvalue \(6x(1+x)/r^2\), as required for scaled complex hyperbolic space in exponential coordinates.

There is also an exact volume consistency. After angular integration, the old cell volume element is
\[
\pi^2\sqrt{\frac{\det h}{G}}\,dx.
\]
The Cartesian determinant of the reconstructed scaled metric, together with \(d^4\xi\), gives
\[
36\pi^2\sqrt{\frac{\det h}{G}}\,dx,
\]
precisely the factor used in `core_integrals`. Thus the one-dimensional core integral and four-dimensional Cartesian annulus integral have compatible measures.

One interpretive point is important: at the best pair,
\[
x_a=0.0422486,\qquad X=128.
\]
For \(b=1.5\),
\[
x_b=\sinh^2(1.5/\sqrt6)\approx0.424.
\]
Thus the preserved core is only the early part of the certified CH cell; the transition occurs far before the exact CH collar at \(X=128\). The calculation is a genuine finite-amplitude truncation and interpolation, not the full \(0.99567\) cell plus a small cap correction.

---

## 4. Exact Calabi cap in normal Cartesian coordinates

Let
\[
n=\sqrt{Z^2+W^2},\qquad
u(n)=\cosh\!\left(\sqrt{\frac32}\,n\right)^{2/3}.
\]
Direct differentiation gives
\[
\frac{du}{dn}=\sqrt{q(u)},\qquad
q(u)=\frac23(u^2-u^{-1}),
\]
so
\[
\frac{du^2}{q}=dn^2.
\]
With
\[
d\Psi=\frac{-W\,dZ+Z\,dW}{Z^2+W^2}
\]
and
\[
A=\frac12(X\,dY-Y\,dX),
\]
the matrix blocks in `cap_metric` are exactly those obtained from
\[
u(dX^2+dY^2)+dn^2+q(d\Psi+A)^2.
\]
In particular,
\[
\begin{aligned}
g_{hh}&=uI_2+q\,v_hv_h^T,\\
g_{nn}&=\frac q{n^2}I_2+\frac{1-q/n^2}{n^2}v_rv_r^T,\\
g_{hn}&=\frac q{n^2}v_hv_n^T,
\end{aligned}
\]
matching the code.

The apparent quotients at \(n=0\) have a smooth analytic extension. If \(s=n^2\), then
\[
u=1+\frac{s}{2}+\frac{s^3}{120}+O(s^4),\qquad
q=s+\frac{s^3}{10}+O(s^4),
\]
and therefore
\[
\frac qs=1+\frac{s^2}{10}+O(s^3),\qquad
\frac{1-q/s}{s}=-\frac{s}{10}+O(s^2).
\]
Thus the geometric formula is smooth across the divisor.

The literal JAX function nevertheless evaluates \(0/0\) at \(Z=W=0\). The scrambled Sobol sets used here evidently avoid those points, since all output is finite, but the Python function is not defined on the divisor itself. A series-based branch would make the implementation equal to the global analytic metric. This does not alter the displayed QMC values.

The volume formula is also correct. In \((X,Y,n,\Psi)\),
\[
\sqrt{\det g_C}=u\sqrt q.
\]
Since \(dZ\,dW=n\,dn\,d\Psi\), the Cartesian density is \(u\sqrt q/n\). Integrating over the Euclidean coordinate ball \(|\xi|<b\) yields
\[
V_C(b)=2\pi^2\int_0^b(b^2-n^2)u(n)\sqrt{q(n)}\,dn,
\]
exactly `cap_ball_volume`.

The ball here is a coordinate ball in \((X,Y,Z,W)\); only \(Z,W\) are proper normal exponential coordinates. It need not be a geodesic ball for the full cap metric.

The generic Ricci routine gives \(\max|\operatorname{Ric}+g|\) between \(9\times10^{-16}\) and \(3\times10^{-15}\) at the supplied cap points, in agreement with the analytic calculation.

---

## 5. Interpolation regularity and positivity

### Baseline

For
\[
H(t)=35t^4-84t^5+70t^6-20t^7,
\]
one has
\[
H'(t)=140t^3(1-t)^3.
\]
Hence \(0\le H\le1\) on \([0,1]\), and
\[
g_{\rm base}=(1-H)g_{\rm cell}+Hg_C
\]
is positive definite everywhere on the annulus.

However, extension by the cell metric for \(t\le0\) and the cap metric for \(t\ge1\) is \(C^3\), not \(C^\infty\): derivatives through order three match, while the fourth derivative generally jumps. The same applies to
\[
256t^4(1-t)^4
\]
extended by zero. Thus the script’s use of “smooth” is stronger than the literal polynomial construction.

This does not create a curvature singularity: Ricci curvature uses two derivatives, and a uniformly positive \(C^3\) metric can be approximated in \(C^2\) by smooth metrics that retain the exact core and cap outside arbitrarily thin interface collars. The values of \(D\), \(P\), and the scalar moments then converge to those reported.

### Response metric

For the fitted value \(c_0=0.1122072\), the first response changes the interpolation weight to
\[
H(t)+c_0F(t),\qquad F(t)=256t^4(1-t)^4.
\]
The identity \(1-H(t)=H(1-t)\), together with
\[
\frac{H(t)}{F(t)}\ge\frac{35}{256}
\]
for \(0<t<1\), shows that \(c_0<35/256\) keeps this effective weight between \(0\) and \(1\). Thus the \(m_0\) response alone remains a convex interpolation for the fitted coefficient.

The tensors
\[
m_1=F\,g_{\rm base},\qquad
m_2=\frac F2(g_{\rm base}S+Sg_{\rm base})
\]
are symmetric and compactly supported in the \(C^3\) sense. In horizontal/normal block form, the \(m_2\) operation removes the cross blocks and changes the two diagonal blocks with opposite signs, as intended.

For the full fitted response, positivity is sampled rather than established over every point. Independent outputs give sampled minimum coordinate eigenvalues
\[
0.2791,\quad0.2715,\quad0.2777,
\]
which are comfortably above zero, but these are minima over 512 QMC points. A global minimum computation over the compact annulus would complete the positivity statement for this specific response metric.

---

## 6. Integration and curvature normalizations

The annulus QMC map is uniform with respect to Euclidean \(d^4\xi\):

- \(r^4\) is uniform on \([a^4,b^4]\);
- the Hopf variable \(v\) is uniform on \([0,1]\);
- both angular variables are uniform on \([0,2\pi]\);
- the Euclidean shell volume is
  \[
  \frac{\pi^2}{2}(b^4-a^4).
  \]

Multiplication by \(\sqrt{\det g}\) therefore gives the correct metric volume integral.

For each annulus point,
\[
P=|\operatorname{Ric}^{\circ}|^2,\qquad
D=|\operatorname{Ric}+g|^2
\]
are contracted correctly as
\[
\operatorname{tr}(g^{-1}Tg^{-1}T).
\]
The coordinate Ricci formula has the correct index contractions. Its agreement with the exact cap provides a strong implementation test.

The reference cap moments are
\[
D_C=P_C=0,\qquad
\int s_C=-4V_C,\qquad
\int s_C^2=16V_C,
\]
so `trial-bg` is the correct relative ledger.

---

## 7. Scalar residual and chiral ledger

The pointwise decomposition is
\[
D=P+\frac14\int(s+4)^2\,dV.
\]
Accordingly, the JSON field
```text
scalar_residual_square = trial[0] - trial[1]
```
is actually
\[
\frac14\int(s+4)^2\,dV,
\]
not the full residual square. For the best baseline,
\[
D-P=59.83237,
\]
whereas
\[
\int(s+4)^2\,dV=239.32947.
\]
This is a naming/factor-of-four issue only; it does not enter the reported \(D\), \(P\), or chiral reconstruction.

For one inserted \(\overline{\mathbb{CP}}^2\), the relative Chern–Weil formulas are
\[
b-a=12\pi^2,\qquad
P=8\pi^2+4a+\frac{\delta S}{12},
\]
where \(\delta S=\delta\int s^2\). Solving gives
\[
a=\frac14\left(P-8\pi^2-\frac{\delta S}{12}\right),\qquad
b=a+12\pi^2,
\]
exactly as implemented. Thus
\[
\frac{b-a}{8\pi^2}=\frac32
\]
is automatic and is not an independent curvature computation, as the script correctly states.

The data are internally consistent. For example, the baseline gives
\[
\frac{a}{8\pi^2}=0.0920594,\qquad
\frac{b}{8\pi^2}=1.5920594,
\]
while the response seeds give \(a/(8\pi^2)\approx0.071\)–\(0.074\) and \(b/(8\pi^2)\approx1.571\)–\(1.574\).

### Textual inconsistency in the corrected Step-35 note

The opening correction in §2 is right:
\[
\delta S=12P+480\pi^2-48b.
\]
Later in the same section, the older sentence saying that \(b<0\) together with \(P\le8\pi^2\) forces
\[
\delta S>576\pi^2
\]
is not implied by this identity. From \(b<0\) and \(P\ge0\), one obtains only
\[
\delta S>480\pi^2+12P\ge480\pi^2.
\]
A value above \(576\pi^2\) follows from \(P\ge8\pi^2\), not from \(P\le8\pi^2\). The opening Step-36 correction and the section’s later retained sentence therefore contradict one another. The transplant script uses the correct ledger formula, so this prose inconsistency does not affect its numerical output.

---

## 8. Numerical interpretation

The pilot value
\[
D/(8\pi^2)=2.20827
\]
was optimized on the same 128 Sobol points used to report it. It is not reproduced on independent node sets. The 512-point independent values \(2.258\)–\(2.270\) are the appropriate numerical summary.

The randomized-seed spread is small compared with the distance from \(1\). Nevertheless, these are floating QMC estimates rather than interval enclosures. The supplied files contain no deterministic quadrature convergence table, pointwise integrand extrema, or rigorous global positivity calculation for the response metric.

For the baseline at \((0.5,1.5)\),
\[
\frac{D_{\rm core}}{8\pi^2}=0.459454,\qquad
\frac{D_{\rm ann}}{8\pi^2}=1.981120.
\]
For the response validation,
\[
\frac{D_{\rm ann}}{8\pi^2}=1.79846,\ 1.80860,\ 1.81005.
\]
The scientific content is therefore clear: these three response tensors recover only a modest portion of the interpolation cost, and the mismatch between the truncated CH cell profile and the Calabi cap remains an \(O(1)\) effect.

---

## 9. What the finite trial says about cap geometry

The computation gives a concrete local blow-up metric, up to the \(C^3\)-to-smooth approximation and the global positivity verification for the response version, that equals the exact Calabi cap outside the chosen coordinate ball. It shows:

1. Proper normal coordinates remove the large chart artifact associated with the earlier algebraic normal marking, but do not make the direct perpendicular transplant inexpensive.
2. The positive \(R^-\) eigenvalue at the cap divisor does not automatically lower the cost of this naive finite-amplitude perpendicular insertion.
3. For the supplied profile and radial interpolation, the transition cost is substantially larger than the preserved bolt-core cost.
4. Conformal, interpolation-path, and horizontal/normal trace-free amplitudes provide some reduction but do not approach the topological scale \(8\pi^2\).

It does not determine:

- the infimum over all cap-cell metrics;
- a general \(U(1)_-\)-invariant cap-adapted core;
- the toric branch;
- optimization over radial markings or compactly supported diffeomorphisms;
- richer tensor responses or functions of both toric variables;
- the best continuous choice of \(a,b\), especially the narrow region near the bolt radius \(r_0\approx0.422\);
- whether a core optimized directly in the Calabi environment can reach or beat the certified CH value;
- a lower bound excluding values below \(1\).

No part of this direct calculation needs the withdrawn same-collar Theorem N. The metric, its Ricci tensor, and its relative moments are evaluated directly against the exact cap exterior.