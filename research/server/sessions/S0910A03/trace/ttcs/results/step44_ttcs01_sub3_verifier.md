# TTCS Independent Branch Record

```json
{
  "step_id": 44,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step44_normalized_yang_tame_start_restart.md",
    "Sessions/S0910A03/workspace/notes/step37_transported_deturck_existence.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md",
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md"
  ]
}
```

## Task

Verify the normalized transported-coefficient Yang/DeTurck start-restart construction in Step 44 against Yang Theorem 8.2 itself. Focus on mathematical sufficiency: exact pullback/gauge transport; variation delta(a_hat) with the diffeomorphism variable; the coupled H^k energy estimate for Yang's linearized metric-transport system with epsilon^2 Delta h; whether integration by parts removes derivative loss in chi C nabla psi; whether constants are uniform in epsilon; whether these estimates really give the smooth tame inverse needed by Yang's fixed-point/Nash-Moser argument after adding -2 a_hat g_hat; coupled uniqueness when transported coefficients differ; and restart from a smooth endpoint. Identify any missing regularity, derivative, compatibility, or nonlinear argument. The goal is a rigorous scientific verdict, not a generic review.

## Output

## Scientific verification memo

### Overall verdict

The normalized term
\[
-2\widehat a\,\widehat g,\qquad
\widehat a=(\chi\circ\varphi^{-1})^2,
\]
is a smooth-tame zeroth-order perturbation of Yang’s transported-coefficient system. It introduces no new principal derivative, no inverse power of \(\widehat\chi\), and no change to Yang’s diffeomorphism equation. Consequently, Yang’s short-time construction extends to
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g)
\]
provided the hatted gauge quantities are interpreted exactly as in Yang’s equations.

Step 44 has the correct central mechanism. Its present exposition is not a fully independent reconstruction of Yang’s Nash–Moser or fixed-point proof: the exact transport structure in the \(\psi\)-equation, the high–low smooth-tame estimates, smooth dependence of the linear inverse on the reference pair, and endpoint gluing require additional statements. These additions preserve the argument rather than changing it.

---

## 1. Exact pullback and gauge transport

Yang defines the gauge so that, with
\[
Z_t=\partial_t\varphi_t\circ\varphi_t^{-1},
\]
the source equations imply
\[
\mathcal L_{Z_t}\widehat g
=-2\widehat\delta^*
 \bigl(\widehat a\,S^{-1}\delta G(S)\bigr).
\tag{1}
\]
Equivalently, the gauge term in the hatted metric equation is the Lie derivative by \(-Z_t\). Since
\[
2\widehat\delta^*\omega=\mathcal L_{\omega^{\sharp_{\widehat g}}}\widehat g,
\]
placing \(\widehat a\) *inside* \(\widehat\delta^*\) is essential: it automatically contains the \(d\widehat a\)-terms that would be absent from the expression \(\widehat a\mathcal L_W\widehat g\).

Thus
\[
\begin{aligned}
\frac d{dt}\varphi_t^*\widehat g
&=\varphi_t^*\bigl(\partial_t\widehat g+
\mathcal L_{Z_t}\widehat g\bigr)\\
&=-2\varphi_t^*\bigl[
\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
\bigr]\\
&=-2\chi^2(\operatorname{Ric}_{g}+g),
\end{aligned}
\tag{2}
\]
because
\[
\varphi_t^*\widehat a=\chi^2,\qquad
\varphi_t^*\operatorname{Ric}_{\widehat g}
=\operatorname{Ric}_{\varphi_t^*\widehat g}.
\]

This is correct in Step 44. One notation point should be made explicit: the objects \(S^{-1}\delta G(S)\), their sharps, and their pushforwards must retain Yang’s exact source/target conventions. Reading the same symbols as independently defined hatted tensors need not reproduce (1). Defining the system through the identity (1), or reproducing Yang’s precise definitions, removes that ambiguity.

The stationary test with \(S=g_0\) and \(\operatorname{Ric}_{g_0}=-g_0\) is also correct.

---

## 2. Variation of the transported coefficient

For a variation \(\varphi_s\), let
\[
\zeta=\left.\frac d{ds}\right|_{0}\varphi_s\circ\varphi^{-1}.
\]
Then
\[
\delta(\chi\circ\varphi^{-1})
=-\mathcal L_\zeta(\chi\circ\varphi^{-1})
=-d\widehat\chi(\zeta),
\]
and hence
\[
\boxed{\delta\widehat a
=-d\widehat a(\zeta)
=-2\widehat\chi\,d\widehat\chi(\zeta).}
\tag{3}
\]
Therefore
\[
\delta(-2\widehat a\,\widehat g)
=-2\widehat a\,h
+4\widehat\chi\,d\widehat\chi(\zeta)\,\widehat g.
\tag{4}
\]

This is algebraic in the Eulerian diffeomorphism variation \(\zeta\). If Yang’s chart variable is denoted by \(\psi=\delta\varphi\), then \(\zeta=\psi\circ\varphi^{-1}\), up to the smooth pointwise bundle map associated with the chosen chart. No spatial derivative of \(\psi\) is introduced.

Consequently, after \(k\) spatial derivatives, (4) contains at most \(k\) derivatives of \(h\) or \(\psi\). Its coefficient structure is
\[
\widehat\chi^2*h+
\widehat\chi\,d\widehat\chi*\psi,
\tag{5}
\]
exactly as stated in Step 44. This also corrects the earlier Step 37 suggestion that the new term might be placed in a \(\widehat\chi C\nabla\psi\) contribution.

---

## 3. Coupled \(H^k\) estimate

### 3.1 Metric diffusion

Using a fixed smooth reference connection and measure,
\[
2\langle\nabla^kh,\nabla^k(\widehat\chi^2\Delta h)\rangle
\]
has leading part
\[
-2\|\widehat\chi\nabla^{k+1}h\|_2^2
-4\int \widehat\chi\,d\widehat\chi*
\nabla^kh*\nabla^{k+1}h.
\]
Young’s inequality gives
\[
\le -c\|\widehat\chi\nabla^{k+1}h\|_2^2
+C_k\|h\|_{H^k}^2.
\tag{6}
\]
When at least two derivatives hit \(\widehat\chi^2\), the remaining derivative order on \(h\) is at most \(k\). No division by \(\widehat\chi\) occurs.

For \(0<\varepsilon\le1\), the regularizer contributes
\[
-c\varepsilon^2\|\nabla^{k+1}h\|_2^2
+C_k\varepsilon^2\|h\|_{H^k}^2.
\tag{7}
\]
The constants in (6)–(7) are independent of \(\varepsilon\).

### 3.2 The \(\widehat\chi C\nabla\psi\) term

Its top part is
\[
I_k=\int\nabla^kh*
\widehat\chi C\nabla^{k+1}\psi.
\]
Integrating the final derivative off \(\psi\),
\[
I_k=
-\int\widehat\chi C\nabla^{k+1}h*\nabla^k\psi
-\int\nabla(\widehat\chi C)\nabla^kh*\nabla^k\psi
+\text{commutators}.
\]
Thus
\[
|I_k|
\le \rho\|\widehat\chi\nabla^{k+1}h\|_2^2
+C_{k,\rho}\bigl(\|h\|_{H^k}^2+\|\psi\|_{H^k}^2\bigr).
\tag{8}
\]
This does remove the apparent derivative loss. Closedness of \(M\) removes edge integrals.

### 3.3 Transport equation

The schematic notation \(P\nabla\psi\) is not by itself enough to justify Step 44 equation (3.7): a general matrix-valued first-order system need not admit that integration by parts.

Yang’s actual diffeomorphism linearization has transport principal part. At top order it is differentiation along a vector field, acting as a scalar transport operator on the components of \(\psi\), modulo lower-order bundle terms. Hence
\[
\int\langle\nabla^k\psi,\widehat a V^i\nabla_i\nabla^k\psi\rangle
=-\frac12\int \operatorname{div}(\widehat aV)
|\nabla^k\psi|^2+\text{lower-order terms}.
\tag{9}
\]
This gives the asserted \(C_k\|\psi\|_{H^k}^2\) estimate. Step 44 should record this transport/symmetrizer fact explicitly rather than infer it from an arbitrary symbol \(P\).

The \(h\)-coupling satisfies
\[
\left|
\int\nabla^k\psi*\widehat\chi^2Q\nabla^{k+1}h
\right|
\le \rho\|\widehat\chi\nabla^{k+1}h\|_2^2
+C_{k,\rho}\|\psi\|_{H^k}^2,
\tag{10}
\]
using \(0\le\widehat\chi\le1\).

### 3.4 Normalization contribution

For a fixed smooth reference pair,
\[
\|\widehat a h\|_{H^k}
+\|\widehat\chi\,d\widehat\chi(\zeta)\widehat g\|_{H^k}
\le C_k\bigl(\|h\|_{H^k}+\|\psi\|_{H^k}\bigr).
\tag{11}
\]
Therefore it contributes only \(C_k\mathcal E_k\).

After choosing the energy weight and the Young parameters coherently, one obtains
\[
\frac d{dt}\mathcal E_k
+c_k\|\widehat\chi\nabla^{k+1}h\|_2^2
+c_k\varepsilon^2\|\nabla^{k+1}h\|_2^2
\le C_k\mathcal E_k+C_k\|(f,\eta)\|_{H^k}^2.
\tag{12}
\]
The phrase “choose \(A_k\) large” is slightly too brief: the transport coupling is multiplied by \(A_k\), so its Young parameter must then be chosen depending on that fixed \(A_k\). This still gives (12), with no \(\varepsilon\)-dependence.

---

## 4. Removal of the regularizer and smooth tame inversion

Equation (12), at every spatial order, gives uniform bounds for \(h_\varepsilon,\psi_\varepsilon\). The equations then give
\[
\partial_t h_\varepsilon
\quad\text{uniformly in }H^{k-2},
\qquad
\partial_t\psi_\varepsilon
\quad\text{uniformly in }H^{k-1}.
\]
Higher time derivatives follow recursively from the equations and the all-order spatial bounds. A diagonal compactness argument therefore produces a smooth limit, and
\[
\varepsilon^2\Delta h_\varepsilon\longrightarrow0
\]
in every fixed lower Sobolev topology. Thus the regularized linear systems yield a smooth solution of the unregularized linearized pair.

For Yang’s nonlinear machinery, the coarse estimate (12) is not the entire smooth-tame statement. One needs a high–low form such as
\[
\mathcal E_k'
\le C(\|u\|_{k_0+r})\mathcal E_k
+C_k(1+\|u\|_{k+r})\mathcal E_{k_0}
+\text{corresponding forcing terms},
\tag{13}
\]
where \(u=(\widehat g,\varphi)\), \(k_0\) is fixed above the Sobolev multiplication threshold, and \(r\) is fixed.

The new normalization obeys the standard tame product estimates:
\[
\|\widehat a h\|_{H^k}
\lesssim
\|\widehat a\|_{H^{k_0}}\|h\|_{H^k}
+\|\widehat a\|_{H^k}\|h\|_{H^{k_0}},
\]
with an analogous formula for
\(\widehat\chi\,d\widehat\chi(\zeta)\widehat g\). Composition and inversion on the diffeomorphism group are precisely the smooth-tame operations already present in Yang’s \(\widehat a=\chi\circ\varphi^{-1}\).

Hence the new term does preserve Yang’s tame derivative count. What Step 44 omits is the explicit high–low estimate (13) and the standard argument that the inverse depends smoothly and tamely on the reference pair. Those facts can be obtained by differentiating the linear solution with respect to the reference pair and repeatedly applying the same inverse estimate. The source itself only summarizes this part as “standard arguments using energy integrals and interpolation inequalities.”

Accordingly:

* As an adaptation of Yang’s established construction, Step 44 is mathematically sufficient after recording the tame product estimate.
* As a self-contained proof of the full inverse theorem, §§3–4 still need (13), temporal seminorm estimates, and smooth-tame dependence on \((\widehat g,\varphi)\).

---

## 5. Coupled uniqueness

Transported coefficients require comparing the metric and diffeomorphism variables together. In a local diffeomorphism chart, let \(u_s\) be a smooth segment joining the two pairs. Then the exact identity is
\[
\widehat a_1-\widehat a_2
=\int_0^1D_\varphi\widehat a(u_s)
[\varphi_1-\varphi_2]\,ds,
\tag{14}
\]
with
\[
D_\varphi\widehat a(u_s)[\Psi]
=-d\widehat a_s(\zeta_s).
\]
Thus the coefficient difference is a zeroth-order linear expression in the diffeomorphism difference, with smooth coefficients depending on the segment.

Using (14), the full nonlinear difference is exactly the integral of its linearization along \(u_s\). It therefore has Yang’s coupled linear form with zero forcing and zero initial data. Estimate (12) gives
\[
\mathcal E_k(t)=0.
\]
Step 44’s “quadratic remainder” language is unnecessary and slightly obscures this exact mean-value representation.

For geometric uniqueness, each smooth geometric solution must first be converted, using Yang’s gauge ODE and the same background tensor \(S\), into a solution of the transported hatted system. Coupled uniqueness then identifies the hatted pairs. Local equality can be propagated along the common time interval by repeating this argument on short subintervals.

---

## 6. Restart from a smooth endpoint

Suppose
\[
g(t)\longrightarrow g_*
\quad\text{in }C^\infty
\quad\text{as }t\uparrow T_*,
\]
and \(g_*\) is positive definite. Yang’s normalized local theorem applied to \((g_*,\chi)\), with \(S=g_*\), gives a solution beginning at \(T_*\).

There is generally no literal overlap between the old interval \([0,T_*)\) and the newly started interval \([T_*,T_*+\delta]\). Smooth gluing follows directly from the autonomous equation
\[
\partial_tg=F(g):=-2\chi^2(\operatorname{Ric}_g+g).
\]
Indeed,
\[
\partial_tg(t)=F(g(t))\longrightarrow F(g_*),
\]
which equals the initial time derivative of the restarted solution. Repeated differentiation of the equation shows equality of all one-sided time derivatives at \(T_*\). The concatenated family is therefore smooth. Geometric uniqueness then identifies any two such extensions.

Thus Step 44’s restart conclusion is correct, but “uniqueness on their overlap” should be replaced by this endpoint-jet argument. Also, “smooth limit” must mean \(C^\infty\) convergence, not merely convergence to a metric that happens to be smooth.

---

## Final assessment

The transported gauge, pullback, coefficient variation, derivative-loss removal, and \(\varepsilon\)-uniform energy mechanism are correct. The normalization preserves Yang’s principal system and smooth-tame derivative count, so the normalized start/restart theorem follows from Yang Theorem 8.2.

For a fully self-contained presentation, the concrete additions are:

1. reproduce Yang’s exact source/target gauge conventions or state identity (1);
2. expose the scalar transport or symmetrizer structure behind the \(P\nabla\psi\) term;
3. write a high–low tame estimate such as (13), including temporal seminorms and tame dependence of the inverse;
4. use the exact mean-value formula (14) for coupled uniqueness;
5. replace the restart “overlap” sentence by smooth endpoint gluing through the evolution equation.

These are presentation and completion issues around a mathematically sound normalized adaptation.