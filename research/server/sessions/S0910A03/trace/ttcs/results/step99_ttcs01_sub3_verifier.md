# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step98_full_matrix_matching_pressure_test.md",
    "Sessions/S0910A03/workspace/data/step99_raychaudhuri_floor.json",
    "Sessions/S0910A03/workspace/data/step99_cost_structure_analysis.json"
  ]
}
```

## Task

Verify the following Raychaudhuri normal-cost analysis and assess whether a tangential cost floor exists.

For a Gaussian 4-metric g = dr² + q(r,s) with H = tr(q⁻¹q_r/2), W° = W - (H/3)I, and E = Ric + 3g:

(1) The Raychaudhuri identity H' + H²/3 + |W°|² = 3 - E_rr gives, with u = H - 3tanh r and integration against cosh²(r):
   ∫₀ᴿ cosh²(r)(-E_rr)dr = 3cosh²(R)(1-tanh R) + ∫₀ᴿ cosh²(r)[|W°|²+u²/3]dr
for any trial with H(0)=0 (minimal center), H(R)=3 (expanding). This identity was numerically verified with residual 3.4×10⁻³.

(2) The comparison ODE h'=(3+δ)-h²/3, h(0)=0, h(R)=3 forces 1≤k tanh(kR) where k=√(1+δ/3). At R=1: δ_min≈1.318. Asymptotically: δ_min~12e^{-2R}.

(3) For the conformal expansion q = cosh²(r)q₀(s) of a charged Koiso separator (scalar curvature -7, winding 2, S=1, Qmax=0.5):
   E_rr = E_ri = 0 exactly
   E_T = Ric(q₀) + 2q₀, with operator norm 9.94 at r=0, decaying as sech²(r)
   The metric has H(0)=0 and K(0)=0, so it does NOT match the charged Koiso Weingarten.

(4) For the quintic jet-preserving transition on [0,1] matching the charged center jets to expanding exterior:
   E_T dominates: peak 28.7 at r≈0.28, while Enn peaks at 10.7
   The dominant E_T term is Ric(q): the quintic creates intermediate metrics with spatial curvature up to 21.4

QUESTION: Is there a tangential-block analog of the Raychaudhuri floor? Specifically, must ‖E_T‖_op exceed some positive lower bound on [0,R] for any metric with H(0)=0 matching the charged Koiso center and H(R)=3? Or could the exact Einstein continuation (if it exists) achieve E_T=0 throughout, with the actual transition cost depending only on where the germ domain ends?

The conformal expansion suggests the tangential cost is 9.94·sech²(r_transition), which goes to zero as the transition point moves to larger r. This would mean the tangential cost has no floor — it depends on how far the exact Einstein germ extends.

## Output

## Scientific verification memo

### 1. Raychaudhuri identity

For \(K=\frac12q_r\), \(W=q^{-1}K\), and \(H=\operatorname{tr}W\),
\[
\operatorname{Ric}_{rr}=-\partial_rH-\operatorname{tr}(W^2)
=-\partial_rH-\frac{H^2}{3}-|W^\circ|^2.
\]
Hence
\[
\partial_rH+\frac{H^2}{3}+|W^\circ|^2=3-E_{rr}.
\]
Set \(a=3\tanh r\) and \(u=H-a\). Since
\[
a'+\frac{a^2}{3}=3,
\]
subtraction gives
\[
u'+2\tanh r\,u+\frac{u^2}{3}+|W^\circ|^2=-E_{rr}.
\]
Multiplication by \(\cosh^2r\) therefore yields the exact derivative identity
\[
\bigl(\cosh^2r\,u\bigr)'
+\cosh^2r\left(\frac{u^2}{3}+|W^\circ|^2\right)
=\cosh^2r(-E_{rr}).
\]
The general integrated form is
\[
\int_0^R\cosh^2r(-E_{rr})\,dr
=
\cosh^2R\,u(R)-u(0)
+\int_0^R\cosh^2r
\left(\frac{u^2}{3}+|W^\circ|^2\right)dr.
\]
Thus \(H(0)=0\), \(H(R)=3\) gives exactly
\[
\int_0^R\cosh^2r(-E_{rr})\,dr
=
3\cosh^2R(1-\tanh R)
+\int_0^R\cosh^2r
\left(\frac{u^2}{3}+|W^\circ|^2\right)dr.
\]

This is pointwise in the slice coordinate \(s\). Averaging over \(s\) preserves it when a fixed coordinate quadrature is used; an \(r\)-dependent slice-volume average would introduce additional terms.

For the \(R=1\) quintic data,
\[
1.7030029+0.9641074+1.7295474=4.3966577,
\]
versus \(4.3932304\) on the left, giving the recorded discrepancy \(3.427\times10^{-3}\), about \(7.8\times10^{-4}\) relative to the left side.

The JSON entry named `hyperbolic_validation` does not satisfy \(H(0)=0\): it records \(u(0)=3\). Its displayed residual near \(3.000112\) is exactly the omitted lower-end term. Using the general formula gives
\[
1.5037181-3+1.4963941=1.12\times10^{-4},
\]
consistent with numerical quadrature.

### 2. Riccati comparison and normal floor

Suppose
\[
E_{rr}\ge -\delta
\]
throughout the cylinder. Dropping the nonnegative shear term gives
\[
H'\le 3+\delta-\frac{H^2}{3}.
\]
The comparison solution with \(h(0)=0\) is
\[
h(r)=3k\tanh(kr),\qquad
k=\sqrt{1+\frac{\delta}{3}}.
\]
Therefore \(H(R)=3\) requires
\[
1\le k\tanh(kR).
\]
The unique equality value defines
\[
\delta_*(R)=3(k_R^2-1),\qquad k_R\tanh(k_RR)=1.
\]
At \(R=1\),
\[
\delta_*(1)=1.317686519\ldots,
\]
matching the supplied table. More precisely, every admissible metric has some point with
\[
-E_{rr}\ge \delta_*(R),
\]
and consequently the full operator norm of \(E\) is at least \(\delta_*(R)\).

For large \(R\), writing \(k=1+\varepsilon\) gives
\[
\varepsilon=2e^{-2R}+O(Re^{-4R}),
\qquad
\delta_*(R)=12e^{-2R}+O(Re^{-4R}),
\]
again matching the numerical ratios.

The weighted identity alone gives the weaker estimate
\[
\sup(-E_{rr})
\ge
\frac{3\cosh^2R(1-\tanh R)}
{\int_0^R\cosh^2r\,dr},
\]
which is \(1.2106239\) at \(R=1\). The Riccati comparison correctly improves this to \(1.3176865\).

### 3. Conformal expansion

For
\[
q(r)=\cosh^2r\,q_0,
\]
one has
\[
W=\tanh r\,I,\qquad H=3\tanh r.
\]
Direct substitution gives
\[
E_{rr}=E_{ri}=0,
\qquad
(E_T)_{ij}=\operatorname{Ric}(q_0)_{ij}+2(q_0)_{ij}.
\]
The covariant tangential tensor is independent of \(r\), while its endomorphism is
\[
q(r)^{-1}E_T
=
\operatorname{sech}^2r\,
q_0^{-1}\bigl(\operatorname{Ric}(q_0)+2q_0\bigr).
\]
Thus the operator norm is
\[
9.9372539\,\operatorname{sech}^2r,
\]
giving \(4.1733917\) at \(r=1\), exactly as recorded.

Two distinctions are essential:

1. \(H(R)=3\tanh R<3\) for every finite \(R\). This family does not meet the expanding endpoint condition.
2. At the center \(K=0\), whereas the charged data have nonzero traceless \(W\).

Indeed, the center constraint relation is
\[
\operatorname{tr}_qE_T-E_{rr}
=
R(q)+6-H^2+|W|^2.
\]
For the charged center, \(R(q_0)=-7\), \(H=0\), and all residual blocks vanish, so
\[
|W^\circ(0)|^2=|W(0)|^2=1.
\]
The conformal family replaces this charged shear by zero. Its decaying tangential residual therefore does not itself realize a connector from the charged center.

### 4. What can be concluded about a tangential floor?

There is no direct tangential counterpart of the scalar Raychaudhuri identity. Taking the tangential trace gives
\[
\operatorname{tr}_qE_T
=
R(q)+9-H'-H^2.
\]
The slice scalar curvature \(R(q)\) has no suitable sign, and the tracefree part of \(E_T\) supplies no nonnegative integral analogous to \(|W^\circ|^2+u^2/3\). The Raychaudhuri calculation therefore yields no quantitative lower bound for \(\|E_T\|_{\mathrm{op}}\).

There is, however, a useful exact-zero statement. Let
\[
C=E_{rr},\qquad J_i=E_{ri}.
\]
When \(E_T=0\), the divergence-free tensor
\[
E-\frac12(\operatorname{tr}_gE)g
\]
gives the propagation system
\[
\partial_rC=-2D^iJ_i-2HC,
\qquad
\partial_rJ_i=\frac12D_iC-HJ_i.
\]
The charged center constraints give \(C(0)=J(0)=0\). In the analytic Einstein-germ setting, uniqueness therefore gives \(C=J=0\) wherever a smooth \(E_T=0\) continuation exists. Such a continuation is fully Einstein there.

It cannot reach \(H(R)=3\) at finite \(R\), because \(E=0\) would make the Raychaudhuri identity read
\[
0=
3\cosh^2R(1-\tanh R)
+\int_0^R\cosh^2r
\left(|W^\circ|^2+\frac{u^2}{3}\right)dr,
\]
whose right side is strictly positive. Equivalently,
\[
H(r)\le 3\tanh r<3.
\]

Thus:

- An exact Einstein germ can have \(E_T=0\) throughout its own interval.
- It cannot remain \(E_T=0\) all the way to a finite endpoint with \(H=3\).
- Every smooth connector must have \(E_T\ne0\) somewhere.
- This does **not** by itself produce a shared positive infimum for
  \[
  \sup_{[0,R]}\|E_T\|_{\mathrm{op}}
  \]
  over all smooth connectors.

The last distinction matters because the Bianchi equations with nonzero \(E_T\) contain derivatives of \(E_T\). A small \(C^0\) tangential residual can have large spatial or radial derivatives at high frequency and can drive substantial \(C\) and \(J\). Without uniform ellipticity and higher-derivative control, exact-zero uniqueness does not yield a quantitative \(C^0\) estimate. With a precompact family having uniform \(C^{2,\alpha}\) control, compactness would convert the absence of an exact-zero connector into a positive infimum depending on those geometric bounds, \(R\), and the charged data.

### 5. Dependence on the chosen expanding exterior

If the endpoint conditions include the particular exterior
\[
q(R)=e^{2R}q_0,\qquad K(R)=q(R),\qquad K_r(R)=2q(R),
\]
then the endpoint itself has
\[
E_T(R)=\operatorname{Ric}(q_0)
\]
as a covariant tensor, so
\[
\sup_{[0,R]}\|E_T\|_{\mathrm{op}}
\ge
e^{-2R}\,
\bigl\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\bigr\|_{\mathrm{op}}.
\]
The data give \(1.0741905\) at \(R=1\) and \(0.0534808\) at \(R=2.5\), with the exact \(e^{-3}\) ratio. This is a genuine fixed-\(R\) floor arising from that nonflat exterior. It disappears if the endpoint is changed to an exact flat-slice cusp.

### 6. Quintic decomposition

The supplied decomposition supports
\[
\sup\|E_T\|_{\mathrm{op}}=28.6630567,
\qquad
\sup\|\operatorname{Ric}(q)\|_{\mathrm{op}}=21.4218849.
\]
The other radial terms are also substantial:
\[
\sup\|K_r\|_{\mathrm{op}}=11.94,\quad
\sup\|HK\|_{\mathrm{op}}=9.79,\quad
\sup\|2Kq^{-1}K\|_{\mathrm{op}}=9.64.
\]
Thus the intermediate slice-curvature amplification is the largest individual contribution, but the peak is produced by its interaction with several radial terms. The sampled profile places the largest displayed \(E_T\) value near \(r=0.36\), while \(r\approx0.28\) is where \(\operatorname{Ric}(q)\) is near its peak; those two locations should not be conflated. The cited \(E_{rr}\) supremum \(10.7\) is not included in either supplied JSON file, so its independent numerical verification requires the full residual profile or script output.

### Overall assessment

The normal floor is exact and well supported. A connector with \(H(0)=0\), \(H(R)=3\) must pay a one-sided normal residual of at least \(\delta_*(R)\).

For the tangential block, exact vanishing over the whole interval is incompatible with the charged constraints and finite \(H(R)=3\). A uniform positive \(C^0\) floor under only the stated smooth endpoint data has not been established. The conformal family illustrates exponential scaling of a particular tangential residual, but because it has \(K(0)=0\) and \(H(R)<3\), it does not prove that the charged connector infimum is zero. Any transition cost also depends on the induced \(q\), \(W\), shear, and spatial curvature at the end of the Einstein germ—not only on the radial location where that germ stops.