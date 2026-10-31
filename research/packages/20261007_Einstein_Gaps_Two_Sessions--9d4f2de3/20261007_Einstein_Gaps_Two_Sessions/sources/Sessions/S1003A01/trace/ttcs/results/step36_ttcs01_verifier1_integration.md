# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 36,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step36_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step36_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently read the corrected Step-35 note and the Step-36 transplant script/data. Check the mathematical realization and numerical interpretation of the finite-amplitude perpendicular cap trial: scale from Ric=-6 to Ric=-1; CH exponential chart reconstruction; exact Calabi cap in proper normal Cartesian coordinates; smoothness/positivity of the convex interpolation and response tensors; core-plus-annulus integration; normalization of D, P, scalar moments, and the relative chiral ledger. Identify any formula or implementation error that could change the reported conclusion. The key reported observation is that the direct baseline costs D/(8pi^2) about 2.44 at the best scanned pair (a,b)=(0.5,1.5), while three response modes lower it only to about 2.26 on independent QMC seeds, still far above both 1 and the certified CH cell 0.99567003. Also assess what this finite trial establishes about cap geometry and what it leaves open. Do not assume the withdrawn same-class Theorem N.

## Integrated Scientific Memo

# Verification memo: Step‑36 perpendicular Calabi-cap transplant

## Verdict

The main numerical conclusion is supported for the **specific finite-dimensional trial family**:

\[
\frac{D}{8\pi^2}=2.44057
\]

for the best scanned direct interpolation \((a,b)=(0.5,1.5)\), while the three fitted transition modes give independent-seed values

\[
2.25792,\qquad 2.26806,\qquad 2.26950,
\]

with mean \(2.26516\). These remain far above both \(1\) and the certified CH-cell value

\[
0.995670030355131.
\]

No scaling, Jacobian, curvature-contraction, or ledger error was found that could plausibly move these values near \(1\). The annulus dominates the cost: the preserved core contributes \(0.459454\), whereas the optimized annulus contributes about \(1.80\), in units of \(8\pi^2\).

There are, however, three qualifications:

1. The polynomial gluing is literally \(C^3\), not \(C^\infty\), though it admits smooth \(C^2\)-close approximations with the same limiting defect.
2. Positivity of the response metric is verified only at QMC nodes, not globally on the compact annulus.
3. This trial does **not** isolate the cap-specific geometric penalty: it truncates the certified cell far before its CH collar, and no same-pipeline CH control was supplied.

None of these qualifications invalidates the reported \(2.44\) and \(2.26\) values as floating-point evaluations of the implemented trial.

---

## 1. Scaling and CH reconstruction

Let \(g_1=6g_6\), with \(\operatorname{Ric}(g_6)=-6g_6\). Since covariant Ricci is unchanged by constant scaling,

\[
\operatorname{Ric}(g_1)=\operatorname{Ric}(g_6)=-6g_6=-g_1.
\]

In dimension four,

\[
dV_{g_1}=36\,dV_{g_6},\qquad s_{g_1}=s_{g_6}/6.
\]

Therefore

\[
\begin{aligned}
D_1(g_1)&=\int|\operatorname{Ric}(g_1)+g_1|^2\,dV_{g_1}
 =\int|\operatorname{Ric}(g_6)+6g_6|^2\,dV_{g_6},\\
P(g_1)&=P(g_6),\\
V(g_1)&=36V(g_6),\\
\int s_{g_1}\,dV_{g_1}&=6\int s_{g_6}\,dV_{g_6},\\
\int s_{g_1}^2\,dV_{g_1}&=\int s_{g_6}^2\,dV_{g_6}.
\end{aligned}
\]

These are exactly the factors used by `core_integrals`. Its defect density

\[
|\operatorname{Ric}+6g|^2=|\operatorname{Ric}^{\circ}|^2+\frac{(s+24)^2}{4}
\]

is correct.

For the scaled CH exponential radius \(r=|\xi|\),

\[
x=\sinh^2(r/\sqrt6),\qquad
\frac{dx}{dr}=\frac{2\sqrt{x(1+x)}}{\sqrt6}.
\]

Thus

\[
6\frac{dx^2}{4G}=\frac{x(1+x)}{G}\,dr^2,
\]

which gives `lam[0]=(x+x*x)/G`. The vectors in `frames0` are Euclidean-orthogonal, have length \(r\), and supply the radial, two transverse, and Hopf directions. Hence the angular scaled eigenvalues \(6h_{ii}/r^2\) are also correct.

At the exact CH profile,

\[
G=x(1+x),\qquad h=\operatorname{diag}(x,x,x(1+x)),
\]

the reconstructed metric has the expected exponential-coordinate eigenvalues

\[
1,\quad \frac{6x}{r^2},\quad \frac{6x}{r^2},\quad
\frac{6x(1+x)}{r^2}.
\]

The one-dimensional core and Cartesian annulus measures are compatible: reconstruction of the scaled metric yields the factor \(36\) multiplying

\[
\pi^2\sqrt{\det h/G}\,dx,
\]

exactly as used for the core volume and scalar moments.

The realized frame is genuinely the perpendicular branch: the bolt collapses one transverse quaternionic direction while the CH Hopf direction is another, so the bolt’s \(\Lambda^+\) direction is perpendicular to the CH Kähler form. The construction shares the required \(U(1)_-\) symmetry with the cap.

### Important geometric interpretation

At the best pair,

\[
x_a=\sinh^2(0.5/\sqrt6)=0.0422486,
\]

whereas the certified cell reaches its exact CH collar only at \(X=128\), corresponding to \(r\approx7.6\). Even the outer transition radius \(b=1.5\) corresponds only to \(x_b\approx0.424\). Therefore this calculation does not retain the complete \(0.99567\) cell and perturb its collar slightly: it cuts through an early, finite-amplitude part of the optimized profile.

That fact is central to interpreting the annulus cost.

---

## 2. Calabi cap in Cartesian divisor-normal coordinates

Set

\[
n=\sqrt{Z^2+W^2},\qquad
u(n)=\cosh(\sqrt{3/2}\,n)^{2/3},
\qquad q(u)=\frac23(u^2-u^{-1}).
\]

Direct differentiation gives

\[
\frac{du}{dn}=\sqrt{q(u)},
\]

so \(du^2/q=dn^2\). With

\[
A=\frac12(X\,dY-Y\,dX),\qquad
d\Psi=\frac{-W\,dZ+Z\,dW}{Z^2+W^2},
\]

the code’s three matrix blocks are exactly those of

\[
g_C=u(dX^2+dY^2)+dn^2+q(d\Psi+A)^2.
\]

Thus `cap_metric` correctly realizes the symmetric-gauge Calabi cap. The gauge agrees with the note’s original expression through \(\Psi'=\Psi+XY/2\).

Near \(s=n^2=0\),

\[
u=1+\frac{s}{2}+\frac{s^3}{120}+O(s^4),\qquad
q=s+\frac{s^3}{10}+O(s^4),
\]

and hence

\[
\frac qs=1+\frac{s^2}{10}+O(s^3),\qquad
\frac{1-q/s}{s}=-\frac{s}{10}+O(s^2).
\]

Therefore the metric has a smooth analytic extension across the divisor.

The literal implementation nevertheless contains \(0/0\) at \(Z=W=0\). The Sobol samples avoid the axis, so this did not affect the supplied outputs, but a Taylor branch should replace the raw quotients for robust evaluation and differentiation near the divisor.

The cap reference volume is also correct. In \((X,Y,n,\Psi)\),

\[
\sqrt{\det g_C}=u\sqrt q,
\]

and integration of the coordinate ball \(|\xi|<b\) gives

\[
V_C(b)=2\pi^2\int_0^b (b^2-n^2)u(n)\sqrt{q(n)}\,dn,
\]

which is `cap_ball_volume`.

The generic coordinate-Ricci routine returns residuals of order \(10^{-15}\) at the test points, consistent with \(\operatorname{Ric}(g_C)=-g_C\). The two smoke-test points happen to have the same normal radius, so this numerical test is narrow, but the algebraic reconstruction independently confirms the formula.

The domain \(|\xi|<b\) is a coordinate ball. Only \(Z,W\) are proper exponential coordinates normal to the divisor; \((X,Y,Z,W)\) are not full Riemannian normal coordinates at the center.

---

## 3. Interpolation, regularity, and positivity

For

\[
H(t)=t^4(35-84t+70t^2-20t^3),
\]

\[
H'(t)=140t^3(1-t)^3.
\]

Thus \(0\le H\le1\) on \([0,1]\), and the baseline

\[
g_{\mathrm{base}}=(1-H)g_{\mathrm{cell}}+Hg_C
\]

is pointwise positive definite.

Both \(H\) and

\[
F(t)=256t^4(1-t)^4
\]

vanish to fourth order at the appropriate interfaces. When extended by the exact cell and cap outside the annulus, the resulting metric is \(C^3\), not \(C^\infty\): derivatives through order three match, while a fourth derivative generally jumps. Since Ricci uses two derivatives, this metric has ordinary continuous Ricci curvature and can be smoothed in thin interface collars with arbitrarily small change in \(D\), \(P\), and the scalar moments. The script’s description as “smooth” should therefore be read as “smoothable without changing the reported limiting cost.”

The three response tensors are symmetric and compactly supported in the same \(C^3\) sense:

\[
m_0=F(g_C-g_{\mathrm{cell}}),\qquad
m_1=Fg_{\mathrm{base}},\qquad
m_2=\frac F2(g_{\mathrm{base}}S+Sg_{\mathrm{base}}).
\]

For the fitted \(c_0=0.112207\), the effective cap weight \(H+c_0F\) remains in \([0,1]\); in particular \(c_0<35/256\), which is sufficient from the endpoint-symmetric ratio bound. The \(m_1\) and \(m_2\) coefficients are small. Independent samples report minimum coordinate eigenvalues

\[
0.2791,\qquad0.2715,\qquad0.2777.
\]

This is strong numerical evidence for positivity but not a proof over the whole annulus. A deterministic minimization or interval bound for the smallest generalized eigenvalue would close this point.

---

## 4. Core-plus-annulus integration

The annulus Sobol transformation is uniform for Euclidean \(d^4\xi\):

\[
r^4=a^4+(b^4-a^4)U_0,
\]

with the Hopf angular parameterization giving uniform \(S^3\) measure. The shell volume

\[
\frac{\pi^2}{2}(b^4-a^4)
\]

is correct. Multiplying the pointwise densities by \(\sqrt{\det g}\) consequently gives the proper Riemannian integrals.

There is no gap or overlap:

- the core is integrated over \(x\in[x_0,x_a]\);
- the annulus is integrated over \(a<|\xi|<b\);
- the exterior is exact cap and has zero \(D\) and \(P\).

For a symmetric covariant tensor \(T\), the contraction

\[
\operatorname{tr}(g^{-1}Tg^{-1}T)
\]

is \(|T|_g^2\). Thus the code correctly computes

\[
P=\int|\operatorname{Ric}^{\circ}|^2,\qquad
D=\int|\operatorname{Ric}+g|^2.
\]

The coordinate Ricci formula has consistent indices and is independently tested against the exact cap.

Two useful implementation checks remain absent from the supplied files:

1. evaluating the Cartesian cell metric alone at selected radii and comparing its pointwise curvature density and volume density against `metric_from`;
2. integrating `core_integrals` to \(x=X\) and reproducing \(0.99567003\).

The formulas predict agreement, but these would directly test the interface between the two curvature implementations.

---

## 5. Scalar moments and chiral ledger

The cap reference moments are

\[
D_C=P_C=0,\qquad
\int s_C=-4V_C,\qquad
\int s_C^2=16V_C.
\]

Thus `trial-bg` correctly computes relative volume, scalar integral, and scalar-square changes.

Pointwise,

\[
|\operatorname{Ric}+g|^2
=|\operatorname{Ric}^{\circ}|^2+\frac{(s+4)^2}{4},
\]

so

\[
D-P=\frac14\int(s+4)^2\,dV.
\]

Accordingly, the JSON field named `scalar_residual_square` is misnamed: it stores one quarter of the residual square, not the full \(\int(s+4)^2\). This naming/factor-of-four issue does not enter \(D\), \(P\), or the ledger.

For one inserted \(\overline{\mathbb{CP}}^2\), relative Chern–Weil gives

\[
b-a=12\pi^2,\qquad
P=8\pi^2+4a+\frac{\delta S}{12},
\qquad \delta S=\delta\!\int s^2.
\]

Hence

\[
a=\frac14\left(P-8\pi^2-\frac{\delta S}{12}\right),
\qquad b=a+12\pi^2,
\]

exactly as implemented. The reported identity

\[
\frac{b-a}{8\pi^2}=\frac32
\]

is therefore automatic and is not an independent curvature check, as the script correctly warns.

### Remaining contradiction in the corrected Step‑35 note

The correction at the start of §2 is correct:

\[
\delta S=12P+480\pi^2-48b.
\]

But a later retained sentence claims that \(b<0\) and \(P\le8\pi^2\) force \(\delta S>576\pi^2\). That does not follow. From \(b<0\),

\[
\delta S>12P+480\pi^2,
\]

which gives only \(\delta S>480\pi^2\) if merely \(P\ge0\). The \(576\pi^2\) bound would follow from \(P\ge8\pi^2\), not \(P\le8\pi^2\). This is a prose inconsistency in the note; the script uses the correct formula.

---

## 6. Numerical interpretation

The baseline scan gives

\[
\frac{D_{\rm core}}{8\pi^2}=0.459454,\qquad
\frac{D_{\rm ann}}{8\pi^2}=1.981120,
\]

hence

\[
\frac D{8\pi^2}=2.440574.
\]

The response coefficients were optimized on only 128 fixed Sobol points, producing the in-sample value \(2.20827\). This number is optimistically biased and should not be quoted as the achieved cost. On independent 512-point seeds, the same coefficients yield

\[
2.257916,\quad2.268059,\quad2.269501,
\]

with annular contributions

\[
1.798462,\quad1.808605,\quad1.810047.
\]

The improvement over the baseline is therefore approximately \(0.17\)–\(0.18\), not \(0.23\), and the annulus remains the dominant cost.

For an exact-collar one-blow-up modification, writing \(\sigma=s+4\), one may combine the ledger with

\[
\delta\!\int s^2=\int\sigma^2-8\int\sigma+16\delta V
\]

to obtain

\[
D
=8\pi^2+4a+\frac43\delta V
 +\frac13\int \sigma(\sigma-2)\,dV.
\]

For optimized seed 1, in units of \(8\pi^2\), the excess over \(1\) decomposes approximately as

\[
4a:\ 0.284,\qquad
\frac43\delta V:\ -0.018,\qquad
\frac13\int\sigma(\sigma-2):\ 0.992.
\]

Thus most of the excess is scalar-sector cost, with a further positive self-dual ledger contribution. The single conformal response mode barely accesses the large scalar contribution; this is evidence that the chosen response space is thin, not that such scalar cost is unavoidable.

These are floating QMC values, not certified numerical enclosures. Nevertheless, the seed variation is tiny compared with the distance from \(1\), so ordinary integration noise cannot explain that gap.

---

## 7. What this says—and does not say—about cap geometry

The calculation establishes the following limited but useful facts.

- The proper divisor-normal cap chart removes the earlier algebraic-chart artifact, yet the naive perpendicular transplant remains expensive.
- In this radial interpolation family, the transition costs much more than the retained bolt core.
- The positive \(R^-\) eigenvalue at the cap divisor does not automatically produce a cheap finite-amplitude transplant.
- The three tested modes—path, conformal, and horizontal/normal trace-free—recover only a modest fraction of the mismatch cost.
- There exists, after arbitrarily small smoothing, an explicit \(U(1)_-\)-compatible cap insertion with \(D/(8\pi^2)\approx2.27\).

It does **not** provide:

- a lower bound for the cap-cell infimum;
- an exclusion of values below \(1\) or below \(0.99567003\);
- the optimum over \(U(1)_-\)-invariant cap-adapted cores;
- information about the toric/aligned branch;
- optimization over markings, compactly supported diffeomorphisms, placement, or richer response fields.

Most importantly, it does not cleanly measure the difference between CH and cap geometry. The trial cuts the certified cell near the bolt, long before its exact CH collar. Moreover, the cap coordinates are Fermi-type about the divisor, not full normal coordinates at the marked point. The rapid growth with larger \(b\) is consistent with accumulating bulk profile/chart mismatch rather than merely paying cutoff derivatives.

The decisive control missing from the supplied data is to replace `cap_metric` by exact CH in the same exponential chart and rerun the identical \((a,b)\), interpolation, and response pipeline. That separates:

\[
\text{core truncation/interpolation cost}
\quad\text{from}\quad
\text{cap-specific cost}.
\]

A complementary separation is to optimize a short-collar cell that is already exact CH near \(r=a\), then interpolate only from CH to the cap. Directly integrating \(|W^+|^2\) over core and annulus would also determine whether the certified cell’s favorable self-dual depletion is lost by early truncation or generated adversely by the transition.

Since CH and the cap have the same \(s\) and \(W^+\), while their local curvature difference is entirely \(W^-\), the genuinely unresolved object is the perpendicular cell’s response to this \(W^-\) environment—at finite size, or its quadratic susceptibility in a small-cell expansion. The present three-mode trial does not determine its sign.

No part of this verification uses the withdrawn same-class Theorem N. The metric and all reported moments are evaluated directly against the exact cap exterior.