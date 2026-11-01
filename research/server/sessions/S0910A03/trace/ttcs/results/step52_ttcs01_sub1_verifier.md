# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step52_normalized_local_flow_start_repair.md",
    "Sessions/S0910A03/workspace/scripts/step52_flat_cutoff_forcing_test.py",
    "Sessions/S0910A03/workspace/data/step52_flat_cutoff_forcing_test.json",
    "Sessions/S0910A03/staging/processing/xu_local_ricci_flow.txt",
    "Sessions/S0910A03/workspace/notes/step50_normalized_yang_wang_verification.md",
    "Sessions/S0910A03/workspace/notes/step51_normalized_yang_precise_estimate.md"
  ]
}
```

## Task

Independently check the new Step 52 normalized local-flow start. The scientific question is whether Guoyi Xu's detailed fixed-point proof for the degenerate local Ricci-DeTurck equation remains valid after adding the algebraic metric reaction -2 chi^2 g. Reconstruct the exact changes to Xu's frozen strictly parabolic map, positivity/eigenvalue estimates, high-Sobolev invariant ball, contraction estimate, epsilon-uniform compactness, and DeTurck pullback. Look specifically for hidden derivative loss, epsilon dependence, boundary/interface mismatch, wrong sign, or a failure to recover the exact geometric normalized flow. Also verify that the flat-torus test really falsifies Step 51's homogeneous critical-energy closure. Give a direct mathematical judgment and any exact repairs needed.

## Output

# Scientific verification memo

## Mathematical judgment

The modification of Xu’s **gauge-fixed metric equation** is sound: adding
\[
-2\chi^2 g
\]
produces only a zeroth-order linear term in the frozen parabolic map. The eigenvalue estimates, Sobolev energies, contraction estimate, and \(\varepsilon\)-uniform bounds acquire ordinary Grönwall contributions, with no extra spatial derivative and no factor \(\varepsilon^{-1}\).

There is, however, a decisive defect in the DeTurck pullback. In general,
\[
\varphi^*(\chi^2 g)=(\chi^2\circ\varphi)\,\varphi^*g,
\]
not \(\chi^2\varphi^*g\). Consequently Step 52 constructs the normalized local **Ricci–DeTurck** solution, but its stated pullback does not produce the geometric flow with the original fixed cutoff. It produces a flow with a transported cutoff. Thus Proposition 3.1, as written, does not follow from the metric-only Xu map.

The flat-torus calculation is correct and does rule out every estimate of the form
\[
E'(t)\le C E(t)
\]
with bounded \(C\) for the unshifted critical curvature energy near \(t=0\).

---

## 1. Frozen strictly parabolic map

Write \(a=\chi^2\). Xu’s gauge-fixed equation is
\[
\partial_t g
=a\,g^{\alpha\beta}\widetilde\nabla_\alpha
 \widetilde\nabla_\beta g
+D(g,g)+B(g,\widetilde\nabla g).
\]
Adding the normalization gives
\[
\partial_t g
=a\,g^{-1}*\widetilde\nabla^2g
+D(g,g)+B(g,\widetilde\nabla g)-2ag. \tag{1}
\]

For frozen \(U\), the correct regularized linear problem is exactly
\[
\partial_tV
=(a+\varepsilon)U^{-1}*\widetilde\nabla^2V
+D(U,V)+B(U,\widetilde\nabla U)-2aV. \tag{2}
\]
At a fixed point \(U=V=g_\varepsilon\), this becomes
\[
\partial_tg_\varepsilon
=(a+\varepsilon)g_\varepsilon^{-1}*
 \widetilde\nabla^2g_\varepsilon
+D(g_\varepsilon,g_\varepsilon)
+B(g_\varepsilon,\widetilde\nabla g_\varepsilon)
-2ag_\varepsilon,
\]
and the limit \(\varepsilon\to0\) solves (1).

The term \(-2aV\) is linear in \(V\), fixed in space-time coefficient, and independent of \(\varepsilon\). Its placement in (2) is therefore exact. Replacing it by \(-2aU\) would also have the same fixed points, but Step 52’s choice is better for positivity and contraction.

---

## 2. Positivity and eigenvalue estimates

At a point diagonalize \(V\) relative to \(\widetilde g\), with eigenvalues \(\lambda_i\). For
\[
\phi_m=\operatorname{tr}\bigl((V^{-1}\widetilde g)^m\bigr)
       =\sum_i\lambda_i^{-m},
\qquad
\psi_m=\operatorname{tr}\bigl((\widetilde g^{-1}V)^m\bigr)
       =\sum_i\lambda_i^m,
\]
the reaction alone gives
\[
\dot V=-2aV,\qquad \dot V^{-1}=2aV^{-1}.
\]
Hence
\[
(\partial_t\phi_m)_{\rm react}=2ma\phi_m,
\qquad
(\partial_t\psi_m)_{\rm react}=-2ma\psi_m. \tag{3}
\]

These signs and coefficients are correct. The first term increases the trace controlling small eigenvalues, but only by
\[
2m\|a\|_\infty\phi_m.
\]
The second term improves the upper-eigenvalue estimate and may simply be discarded when deriving an upper differential inequality. Xu’s maximum-principle ODEs therefore remain valid after shortening the time by an amount depending on \(\|a\|_\infty\). No derivative of \(a\) and no \(\varepsilon^{-1}\) enters (3).

For Xu’s original normalization \(0\le\chi\le1\), \(\|a\|_\infty\le1\). For an arbitrary smooth \(\chi\) on a closed manifold, the same calculation uses \(\|\chi\|_\infty^2\).

---

## 3. High-Sobolev invariant ball

For the fixed-background energy
\[
E_m(V)=\sum_{|\alpha|\le m}
\|\widetilde\nabla^\alpha V\|_{L^2(\widetilde g)}^2,
\]
the new contribution is
\[
-4\sum_{|\alpha|\le m}
\int
\left\langle\widetilde\nabla^\alpha V,
\widetilde\nabla^\alpha(aV)\right\rangle d\mu_{\widetilde g}.
\]
Leibniz expansion gives
\[
\bigl|E_m'(V)\bigr|_{\rm react}
\le C_m\|a\|_{W^{m,\infty}}E_m(V)
\le C_m\|\chi\|_{C^m}^2E_m(V). \tag{4}
\]
The top piece \(-4\int a|\widetilde\nabla^mV|^2\) actually has a favorable sign; estimating all pieces by absolute value is sufficient.

Equation (4) uses derivatives of \(\chi\) only through order \(m\), exactly the current energy order. It introduces neither \(m+1\) derivatives of \(V\) nor any division by \(a+\varepsilon\). Xu’s inequality (2.22) therefore changes by a bounded multiple of \(E_m(V)\), and Propositions 2.5 and 2.7 retain their form after reducing the time.

There is also no new issue in terms containing \(\widetilde\nabla(a+\varepsilon)\), since
\[
\frac{|\widetilde\nabla a|^2}{a+\varepsilon}
=\frac{4\chi^2|\widetilde\nabla\chi|^2}
       {\chi^2+\varepsilon}
\le4|\widetilde\nabla\chi|^2. \tag{5}
\]
Thus the weighted absorptions used in Xu’s principal-part estimates remain uniform in \(\varepsilon\).

---

## 4. Contraction estimate

For
\[
V=\Phi_\varepsilon^N(U),\qquad
\widetilde V=\Phi_\varepsilon^N(\widetilde U),\qquad
W=V-\widetilde V,
\]
the new term in the difference equation is exactly
\[
-2aW. \tag{6}
\]
There is no term involving \(U-\widetilde U\), because \(a\) is fixed in this metric-only construction.

At Sobolev order \(m\),
\[
\left|
\sum_{|\alpha|\le m}
\left\langle
\widetilde\nabla^\alpha W,
\widetilde\nabla^\alpha(-2aW)
\right\rangle
\right|
\le C_m\|a\|_{W^{m,\infty}}\|W\|_{H^m}^2. \tag{7}
\]
Consequently Xu’s (2.49) becomes
\[
\frac{d}{dt}\|W\|_{H^{\widetilde p}}^2
\le (C_1+C_a)\|W\|_{H^{\widetilde p}}^2
+C_2\|U-\widetilde U\|_{H^{\widetilde p}}^2. \tag{8}
\]
Since \(W(0)=0\),
\[
\sup_{s\le T}\|W(s)\|_{H^{\widetilde p}}^2
\le C_2Te^{(C_1+C_a)T}
\sup_{s\le T}\|U(s)-\widetilde U(s)\|_{H^{\widetilde p}}^2. \tag{9}
\]
Choosing the coefficient in (9) below \(1/4\) gives contraction factor \(1/2\) in the unsquared norm. Step 52’s contraction calculation is therefore correct.

---

## 5. Compactness and smoothness at \(\{\chi=0\}\)

The reaction causes no new compactness issue. One point in Step 52 needs a more explicit argument: smoothness across the zero set should come from all-order estimates on one common time interval, not merely from separate regularity on \(\{\chi>0\}\) and stationarity on the interior of \(\{\chi=0\}\).

This common-time estimate follows directly after constructing the fixed point. For the fixed point \(U=V=g_\varepsilon\), Xu’s (2.22), with the already obtained low-order bound inserted, yields for every \(m\)
\[
\frac{d}{dt}E_m(g_\varepsilon)
\le C_m\bigl(1+E_m(g_\varepsilon)\bigr), \tag{10}
\]
where \(C_m\) depends on the low-order bilipschitz/Sobolev bound, the smooth initial data, \(\chi\), and \(\widetilde g\), but not on \(\varepsilon\). The reaction adds only (4). Grönwall gives an \(H^m\) bound on the original fixed-point time \(T\), rather than a new time \(T_m\).

The equation then gives
\[
\|\partial_tg_\varepsilon\|_{H^{m-2}}\le C_m,
\]
again uniformly in \(\varepsilon\). Repeating with time derivatives and taking a diagonal subsequence produces global \(C^\infty\) convergence on the same interval. This supplies smoothness at all points of \(\{\chi=0\}\), including nontrivial zero-set interfaces.

In Xu’s domain formulation, \(\chi\in C_c^\infty(\Omega)\), so \(a=0\) in a collar of \(\partial\Omega\). The reaction therefore adds no compatibility term there. On a closed manifold with an arbitrary smooth \(\chi\), one may instead formulate (2) directly on \(M\), with the usual compact-manifold Sobolev inequality including an \(L^2\) term. That removes all domain-edge issues.

Thus the \(\varepsilon\)-uniform analytic construction of the gauge-fixed metric is repairable in full detail.

---

## 6. DeTurck pullback does not preserve the fixed cutoff

This is the central defect.

Let \(\widehat g\) solve
\[
\partial_t\widehat g
=-2a(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{aW}\widehat g, \qquad a=\chi^2, \tag{11}
\]
and let
\[
\partial_t\varphi=-(aW)\circ\varphi,\qquad \varphi(0)=\mathrm{id}. \tag{12}
\]
For \(h=\varphi^*\widehat g\), the pullback formula gives
\[
\begin{aligned}
\partial_t h
&=\varphi^*\left(
\partial_t\widehat g+\mathcal L_{-aW}\widehat g
\right)\\
&=-2\varphi^*\!\left(a(\operatorname{Ric}_{\widehat g}+\widehat g)\right)\\
&=-2(a\circ\varphi)\bigl(\operatorname{Ric}_h+h\bigr). \tag{13}
\end{aligned}
\]
Thus the resulting coefficient is
\[
a_t=a\circ\varphi,
\]
not the original fixed \(a\). The identity used in Step 52,
\[
\varphi^*(\chi^2\widehat g)=\chi^2\varphi^*\widehat g,
\]
is false unless \(\chi\circ\varphi=\chi\).

Xu’s displayed ODE in the supplied text is even more delicate:
\[
\partial_t\varphi_t(p)=-a(p)W(\varphi_t(p),t).
\]
If read literally, its Eulerian generator is
\[
Y=-(a\circ\varphi^{-1})W.
\]
Then the Lie term remaining in the pullback is
\[
\mathcal L_{[a-a\circ\varphi^{-1}]W}\widehat g,
\]
so the pullback is not even equation (13). If Xu intended the standard notation \(-(aW)\circ\varphi\), equation (13) is the result.

For a nonconstant \(a\), there is no general reason for \(W(a)=0\). The metric-only Xu construction therefore proves the following precise statement:
\[
\widehat g \text{ solves (11),}
\]
and its standard DeTurck pullback solves a normalized flow with transported coefficient \(a_t=a\circ\varphi\). It does not establish the fixed-cutoff equation
\[
\partial_t h=-2a(\operatorname{Ric}_h+h). \tag{14}
\]

The special cases \(a\equiv\text{constant}\) or \(W(a)=0\) along the entire evolution do recover (14).

### Exact coupled formulation for fixed \(a\)

To obtain (14), the DeTurck-coordinate coefficient must itself evolve. Introduce \(\widehat a\) and solve
\[
\begin{cases}
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{\widehat aW}\widehat g,\\[2mm]
\partial_t\widehat a=\widehat a\,W(\widehat a),\\
\widehat a(0)=a.
\end{cases} \tag{15}
\]
With
\[
\partial_t\varphi=-(\widehat aW)\circ\varphi,
\]
one has
\[
\frac{d}{dt}(\widehat a\circ\varphi)=0,
\qquad
\widehat a\circ\varphi=a,
\]
and therefore
\[
\partial_t(\varphi^*\widehat g)
=-2a\bigl(\operatorname{Ric}_{\varphi^*\widehat g}
+\varphi^*\widehat g\bigr). \tag{16}
\]

System (15) is no longer Xu’s metric-only map. The coefficient is a transported unknown; differences contain terms such as
\[
-2(\widehat a-\widetilde{\widehat a})\,\widetilde V,
\]
and the scalar equation contains first derivatives through \(W(\widehat a)\). A coupled fixed-point or tame inverse estimate is needed for (15). The algebraic reaction remains harmless, but Xu’s fixed-\(\chi\) argument alone does not provide this coupled estimate.

---

## 7. Flat-torus computation

On the flat \(T^4=(\mathbb R/2\pi\mathbb Z)^4\), let
\[
\chi(x_1)=\frac{1+\cos x_1}{2},\qquad a=\chi^2.
\]
At \(t=0\),
\[
\operatorname{Ric}=0,\qquad \dot g=-2ag.
\]
For the standard full four-index tensor convention, conformal variation gives
\[
\dot{\operatorname{Rm}}=g\owedge\operatorname{Hess}a. \tag{17}
\]
Here
\[
a''(x_1)=-\frac{\cos x_1+\cos2x_1}{2}. \tag{18}
\]
Since the Hessian has only the \(11\)-component,
\[
|g\owedge\operatorname{Hess}a|^2
=4\bigl((n-2)|\operatorname{Hess}a|^2+(\Delta a)^2\bigr)
=12(a'')^2 \quad(n=4). \tag{19}
\]
Also,
\[
\int_0^{2\pi}(a'')^2\,dx_1=\frac{\pi}{2}. \tag{20}
\]
Therefore
\[
\begin{aligned}
\int_{T^4}|\operatorname{Rm}(g(t))|^2\,d\mu_{g(t)}
&=t^2\cdot12\cdot\frac{\pi}{2}\cdot(2\pi)^3+O(t^3)\\
&=48\pi^4t^2+O(t^3). \tag{21}
\end{aligned}
\]
The script and JSON values agree with this direct calculation.

Thus
\[
\frac{E'(t)}{E(t)}=\frac2t+O(1). \tag{22}
\]
No bounded constant \(C\) can satisfy \(E'\le CE\) for all sufficiently small positive \(t\). Equivalently, such an inequality with \(E(0)=0\) would force \(E\equiv0\) by Grönwall, contradicting (21).

The constant-homothety cancellation
\[
(2p-n)\int a|\operatorname{Rm}|^p
\]
at \(p=n/2\) remains correct, but it does not remove the spatial forcing \(g\owedge\nabla^2a\).

After one integration by parts, the source
\[
4p\int F^{p-2}\operatorname{Ric}_{ij}\nabla_i\nabla_j a
\]
contains terms bounded by
\[
\varepsilon\int aF^{p-2}|\nabla\operatorname{Rm}|^2
+C_\varepsilon\int\frac{|da|^2}{a}F^{p-2}, \tag{23}
\]
not by a multiple of \(\int F^p\). For \(p=2\), the second integral is a genuine zeroth-power forcing. A further integration by parts introduces \(\Delta_g a\). This is exactly the mechanism seen in (21).

---

## Final scientific status

1. The reaction \(-2\chi^2V\) preserves Xu’s eigenvalue, Sobolev, contraction, and \(\varepsilon\)-uniform estimates.
2. Global smoothness of the gauge-fixed limit follows after adding the same-time all-order estimate (10).
3. The DeTurck pullback in Step 52 changes the cutoff to \(\chi^2\circ\varphi\). The fixed-cutoff normalized flow requires the coupled transported-coefficient system (15), which is not contained in the metric-only argument.
4. The flat-torus calculation and its coefficient \(48\pi^4\) are correct, and the homogeneous critical-energy closure from Step 51 is mathematically impossible.