# TTCS Independent Branch Record

```json
{
  "step_id": 18,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step18_weighted_cutoff_system.md",
    "Sessions/S0910A01/workspace/notes/step17_support_scale_li_bootstrap.md",
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Sessions/S0910A01/workspace/scripts/step18_weighted_cutoff_algebra.py",
    "Sessions/S0910A01/workspace/scripts/step18_energy_absorption_terms.py",
    "Sessions/S0910A01/workspace/scripts/step18_degenerate_model_heat_kernel.py",
    "Sessions/S0910A01/workspace/scripts/step18_constant_diffusivity_weight_scaling.py"
  ]
}
```

## Task

Verify the Step 18 refined cutoff-flow analysis for the four-dimensional negative LeBrun route. Please read the corrected Step 18 note, the patched Step 17 support-scale note, the A03 Step 17 cutoff-flow note, Li's source theorem passages, and the Step 18 scripts. Check: (1) the weighted scalar identity for f=a|Rm| and the conclusion that the quadratic reaction is f^2 rather than f^2/a; (2) whether the integrated principal energy can avoid pointwise Hessian cutoff assumptions at least in the scalar model and what remains tensorially; (3) whether the coupled L2 layer is legitimately separated from the remaining pointwise smoothing problem; (4) whether unweighted Q(t) is correctly kept distinct from weighted aE; (5) whether the model computations support but do not prove degenerate epsilon-regularity. Give a direct scientific memo with corrections or a sharper theorem target; do not turn this into final-route control.

## Output

# Scientific verification memo: Step 18 cutoff-flow analysis

## 1. Weighted scalar identity

Let \(a=\chi ^2\) be time-independent, \(K=|\mathrm{Rm}|\), and \(f=aK\). On \(\{a>0\}\),

\[
f_t=aK_t\le a^2\Delta(f/a)+ca^2K^2+aT.
\]

The quotient rule gives

\[
a^2\Delta(f/a)
=a\Delta f-2\langle \nabla a,\nabla f\rangle
+\left(\frac{2|\nabla a|^2}{a}-\Delta a\right)f,
\]

and therefore

\[
f_t\le a\Delta f-2\langle \nabla a,\nabla f\rangle
+\left(\frac{2|\nabla a|^2}{a}-\Delta a\right)f
+cf^2+aT.
\]

Thus the main curvature reaction is exactly \(cf^2\), not \(cf^2/a\). The symbolic calculation in `step18_weighted_cutoff_algebra.py` verifies this correctly.

For \(a=\chi^2\),

\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2,
\qquad
\frac{2|\nabla a|^2}{a}-\Delta a
=6|\nabla\chi|^2-2\chi\Delta\chi .
\]

Hence there is no inverse power of \(\chi\), although the pointwise equation still contains \(\chi\Delta\chi\). The quotient derivation is initially valid where \(a>0\); for smooth curvature it extends to \(a=0\) by continuity. Since \(K=|\mathrm{Rm}|\) is only Lipschitz where \(\mathrm{Rm}=0\), a rigorous scalar argument uses \(K_\varepsilon=(|\mathrm{Rm}|^2+\varepsilon^2)^{1/2}\) or the tensor equation followed by Kato’s inequality.

This calculation concerns the principal curvature reaction only. The actual cutoff-flow tensor equation also produces terms schematically of the form

\[
\nabla a*\nabla E,\qquad \nabla^2a*E,\qquad
aE*\mathrm{Rm},
\]

so the scalar identity by itself does not establish the desired weighted pointwise estimate.

## 2. Integrated principal energy and Hessian terms

At a fixed time, integration against \(\eta^2f\) gives the exact principal identity

\[
\begin{aligned}
\int \eta^2f L_af
={}&-\int a\eta^2|\nabla f|^2
-2\int a\eta f\langle\nabla\eta,\nabla f\rangle\\
&-\int \eta^2f\langle\nabla a,\nabla f\rangle
+2\int \eta f^2\langle\nabla\eta,\nabla a\rangle
+2\int\eta^2f^2\frac{|\nabla a|^2}{a},
\end{aligned}
\]

where

\[
L_af=a\Delta f-2\langle\nabla a,\nabla f\rangle
+\left(2|\nabla a|^2/a-\Delta a\right)f.
\]

Young inequalities therefore yield

\[
\int \eta^2f L_af
\le -c\int a\eta^2|\nabla f|^2
+C\int\left(a|\nabla\eta|^2
+\eta^2\frac{|\nabla a|^2}{a}\right)f^2.
\]

This confirms the scalar conclusion recorded by the script: the spatial energy identity needs only first derivatives of \(a\). Time variation of the metric, volume form, and tensor norms produces additional lower-order terms and is not represented by that script.

The analogous tensor integration is plausible. For example,

\[
\int\eta^2\langle \mathrm{Rm},(\nabla^2a)*E\rangle
\]

can be integrated once to obtain terms involving

\[
\nabla(\eta^2\mathrm{Rm})*\nabla a*E,
\qquad
\eta^2\mathrm{Rm}*\nabla a*\nabla E.
\]

These fit the weighted dissipations because

\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le Cr^{-2}.
\]

The resulting Young estimates have the expected forms

\[
\varepsilon\int a|\nabla\mathrm{Rm}|^2
+Cr^{-2}\int |E|^2,
\qquad
\varepsilon\int a|\nabla E|^2
+Cr^{-2}\int |\mathrm{Rm}|^2.
\]

What is not supplied is the complete tensor variation formula with every contraction, metric-norm term, volume term, localization term, and commutator written and summed. The Step 18 scripts verify algebra and scaling, rather than this full tensor derivation.

A pointwise defect maximum principle presents a separate Hessian issue: it contains \(|\nabla^2_{g(t)}a|\). A fixed smooth cutoff has a finite Hessian for each individual metric, but \(C^0\) metric comparability does not control the Christoffel contribution to \(\nabla^2_{g(t)}a\) uniformly across a collapsing sequence. The integrated approach avoids this object; a pointwise approach needs stronger cutoff geometry or a weak Moser formulation.

## 3. Coupled \(L^2\) layer versus pointwise smoothing

The proposed Sobolev absorption has the correct four-dimensional normalization. If

\[
R_U=\frac{r^4}{V_U}\int_U|\mathrm{Rm}|^2,
\qquad
A_U\lesssim \frac{r^2}{V_U^{1/2}},
\]

then

\[
A_U\|\mathrm{Rm}\|_{L^2(U)}
\lesssim
\frac{r^2}{V_U^{1/2}}
\frac{R_U^{1/2}V_U^{1/2}}{r^2}
= C R_U^{1/2}.
\]

Thus, with \(\eta\) included,

\[
\begin{aligned}
\int \eta^2a|\mathrm{Rm}|\,|E|^2
&\le \|\mathrm{Rm}\|_2\|\eta\chi E\|_4^2\\
&\le A_U\|\mathrm{Rm}\|_2
\left[
C\int\eta^2a|\nabla E|^2
+C\int(a|\nabla\eta|^2+\eta^2|\nabla\chi|^2)|E|^2
\right],
\end{aligned}
\]

and the first term is absorbable when \(R_U\) is sufficiently small. The curvature cubic term is handled similarly through \(\eta\chi|\mathrm{Rm}|\). The volume cancellation verified by `step18_energy_absorption_terms.py` is therefore mathematically correct.

This supports a coupled a priori system of the form

\[
\begin{aligned}
\dot R_\alpha+cX_\alpha
&\le Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)
+\varepsilon Y_\alpha,\\
\dot P_\alpha+cY_\alpha
&\le Cr^{-2}\sum_{\beta\sim\alpha}P_\beta.
\end{aligned}
\]

It remains distinct from pointwise smoothing: these inequalities only propagate critical energy. They do not supply a mean-value inequality for the degenerate operator or imply

\[
a|\mathrm{Rm}|\le C/t.
\]

The supplied material also leaves two prerequisites implicit:

1. The Sobolev coefficients, cutoff-gradient norms, and adjacent-ball volume comparisons are measured along \(g(t)\). The energy estimate is presently an a priori estimate on an interval where metric comparability is assumed. It can be used in a continuation bootstrap, but it is not yet independent of that geometric assumption.

2. The Step 17 construction controls curvature through the maximal function only up to \(4r_*\), while the active support reaches \(B_{5r_*}(p)\). The transition annulus \(B_{5r_*}\setminus B_{4r_*}\) therefore has no supplied initial curvature-energy estimate. Full-support energy propagation can be connected to the good-set construction by defining the maximal function at least through \(6r_*\): every radius-\(\le r_*\) ball centered in \(B_{5r_*}(p)\) then lies in \(B_{6r_*}(p)\), and Bishop–Gromov comparison converts the \(p\)-centered estimate into a uniform dimensionless estimate on those shifted balls.

Li’s Theorems 3.4 and 3.6 do not fill this step. Theorem 3.4 bootstraps a supremum over all centers, while Theorem 3.6 assumes normalized small energy at every center. Its principal operator is nondegenerate. The patched Step 17 discussion correctly identifies why merely placing the covering balls inside a plateau does not reproduce Li’s global supremum argument.

## 4. Unweighted \(Q(t)\) and weighted metric speed

The distinction between

\[
Q(t)=\int_M|E|^2\,d\mu_{g(t)}
\]

and \(aE\) is essential and is correctly maintained in Step 18. The flow speed satisfies

\[
|\partial_tg|=2|aE|,
\]

so a weighted pointwise estimate is the relevant quantity for metric drift. It gives no direct estimate for \(|E|\) where \(a\) is small.

Conversely, the LeBrun recalibration uses the unweighted integral over the whole manifold. A support-summed version of the defect energy estimate can plausibly give

\[
Q'(t)\le Cr^{-2}Q(t)
\]

after the local curvature reaction is absorbed by the small \(R_\alpha\). On the frozen region \(a=0\), the metric and \(E\) remain unchanged. This route is stronger than estimating the reaction through a pointwise \(C/t\) curvature bound.

There is an important error in the A03 maximum-principle discussion:

\[
\int_0^T \frac{dt}{t}=\infty.
\]

Thus \(a|\mathrm{Rm}|\le C/t\) does not by itself produce a uniform estimate \(|E(t)|\le C\delta\) from time zero through the raw maximum principle. Starting at \(t_0>0\) produces constants depending on \(t_0\). A separate parabolic defect estimate with an integrable exponent is needed, for example

\[
|aE(t)|\le C_p\delta
\left(\frac{r^2}{t}\right)^{2/p},
\qquad p>2.
\]

Then

\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C_p\delta r^2,
\]

which genuinely controls metric drift. Step 18’s reference to both the maximum principle and parabolic estimates is therefore the correct direction; the maximum principle alone is insufficient.

## 5. Model computations

The constant-diffusivity calculation is correct:

\[
\|K(t)\|_\infty
\lesssim (at)^{-n/(2p)}\|K_0\|_p,
\qquad p=n/2,
\]

so

\[
\|aK(t)\|_\infty\lesssim t^{-1}\|K_0\|_{n/2}.
\]

This explains the natural weight but says nothing about variable coefficients or cutoff tensor terms.

For \(a=x^2\), the coordinate change \(y=\log x\) correctly gives

\[
u_t=u_{yy}-u_y.
\]

The heat kernel in `step18_degenerate_model_heat_kernel.py` has the drift sign reversed. The correct full-line kernel is

\[
G(y,z,t)
=(4\pi t)^{-1/2}
\exp\!\left[-\frac{(y-z-t)^2}{4t}\right].
\]

With the \(L^2(dx)=L^2(e^z\,dz)\) input measure, the corrected squared dual norm contains

\[
\int_{-\infty}^{0}G(y,z,t)^2e^{-z}\,dz
=
\frac{e^{-y+3t/2}}{4\pi t}
\sqrt{\frac{\pi t}{2}}
\left[
1+\operatorname{erf}
\left(\frac{2t-y}{\sqrt{2t}}\right)
\right].
\]

The small-time power \(t^{-1/4}\) remains, although the numerical constants and drift locations change.

Two further features restrict the interpretation:

- The script uses a full-line kernel with sources restricted to \(z\le0\), without specifying a half-line condition at \(y=0\).
- A smooth compactly supported nonnegative cutoff is flat where it meets the frozen exterior. The model \(\chi=x\), \(a=x^2\), is not the local profile of such a cutoff at that edge.

Accordingly, the constant-\(a\) and \(x^2\) calculations support the weighted scaling and show no elementary one-dimensional obstruction. They do not establish the four-dimensional nonlinear tensor estimate.

## 6. Sharper theorem object

The mathematically coherent target emerging from these notes is an a priori theorem for a smooth cutoff-flow solution on a bootstrap interval with:

- full-support, all-relevant-scale normalized curvature energy smallness;
- relative Sobolev inequalities and finite-overlap covers;
- only first-derivative cutoff control in the weak tensor energy formulation;
- coupled persistence of \(R_\alpha+\kappa P_\alpha\);
- direct support-summed control \(Q(t)\le C Q(0)\);
- weighted estimates
  \[
  \sup a|\mathrm{Rm}(t)|\le C/t,
  \qquad
  \sup a|E(t)|
  \le C_p\delta(r^2/t)^{2/p},\quad p>2.
  \]

A useful local geometry behind the pointwise part is

\[
|\nabla\chi|\le C/r
\quad\Longrightarrow\quad
\chi\asymp\chi(x)
\ \text{on}\ 
B_{c r\chi(x)}(x).
\]

For \(t\le\theta r^2\), the diffusion length
\(\sqrt{a(x)t}=\chi(x)\sqrt t\) lies inside such a ball. Thus every point with \(a(x)>0\) has a rescaled cylinder on which the operator is uniformly parabolic after division by \(a(x)\). Turning this Whitney-scale observation into a tensor Moser estimate, while retaining first-derivative cutoff control and the coupled \(E\) terms, is the precise missing pointwise mechanism.

In summary, the Step 18 algebraic correction, volume cancellation, separation of \(L^2\) persistence from pointwise smoothing, and distinction between \(Q\) and \(aE\) are sound. The present files provide a credible coupled energy architecture, but not yet the complete tensor derivation or the degenerate mean-value theorem. The support-scale maximal-function radius, the defect estimate near \(t=0\), and the heat-kernel drift sign are concrete corrections needed in the refined formulation.