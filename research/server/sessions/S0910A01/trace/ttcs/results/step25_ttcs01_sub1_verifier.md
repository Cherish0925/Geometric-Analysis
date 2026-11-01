# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step25_tensor_energy_derivation.md",
    "Sessions/S0910A01/workspace/notes/step25_first_exit_formulation.md",
    "Sessions/S0910A01/workspace/notes/step24_buffered_support_energy_test.md",
    "Sessions/S0910A01/workspace/scripts/step25_tensor_energy_verification.py"
  ]
}
```

## Task

Verify the q=2 curvature energy derivation in workspace/notes/step25_tensor_energy_derivation.md. The note claims that under the buffered cutoff flow d_t g = -2 chi^2(Ric+g) on a closed 4-manifold with supp(chi) compactly inside {eta=1} and supp(grad eta) in {chi=0}, the energy H_2 = int eta^2 F^2 dmu satisfies H_2' + c D_2 <= C int(eta^2 a F^3) + C r^{-2} H_2, where D_2 = int(eta^2 a |grad Rm|^2). Check: (1) Is the term classification (Types A-D, metric variation, volume form) complete? Are there missing terms from the curvature variation formula under h = -2aE? (2) Is the integration by parts of the Hessian(a) terms correct? Does the cross term grad a . grad eta genuinely vanish? (3) Are the Young inequality absorptions correct with the coefficient |grad a|^2/a = 4|grad chi|^2? (4) Is the global defect identity Q_global(t) <= e^{C theta} Q_global(0) correct? (5) For the first-exit Approach A: is it correct that the short-time existence interval theta r^2 <= c/K_0 is compatible with the maximal-function good center hypothesis K_0 ~ r^{-2}? Identify any errors, missing terms, or logical gaps.

## Output

# Scientific verification memo

## Main findings

The \(q=2\) energy inequality is structurally correct under the following hypotheses:

- \(a=\chi^2\) and \(\eta\) are fixed smooth functions;
- the cutoff derivative bound \(|\nabla\chi|_{g(t)}\le Cr^{-1}\) holds, for example via metric comparability with \(g_0\);
- the modified flow exists smoothly;
- \(\eta\equiv1\) on a neighborhood of \(\operatorname{supp}\chi\), with \(\operatorname{supp}d\eta\subset\{\chi=0\}^{\circ}\).

There is no missing tensor class in the curvature evolution. Two displayed details need repair: the tensor formula for \(\nabla^2a\), and the inequality direction in (2.11). The global defect estimate is valid with disjoint buffered supports and a precisely defined weighted local energy. The short-time argument in the first-exit note is not supplied by the maximal-function hypothesis.

---

## 1. Curvature-variation term ledger

For a general variation \(h=\partial_tg\), the all-lowered curvature tensor satisfies schematically

\[
D\operatorname{Rm}(h)
=\frac12\mathcal S(\nabla^2h)+\operatorname{Rm}*h,
\]

where \(\mathcal S\) denotes the usual four-term index symmetrization. With

\[
h=-2aE,\qquad E=\operatorname{Ric}+g,
\]

expansion gives

\[
\nabla^2(aE)
=a\nabla^2E+(\nabla a)*\nabla E+(\nabla^2a)*E.
\]

Using \(\nabla E=\nabla\operatorname{Ric}\) and the Bianchi commutations in the \(a\nabla^2\operatorname{Ric}\) part yields the schematic evolution

\[
\partial_t\operatorname{Rm}
=
a\Delta\operatorname{Rm}
+a\,\operatorname{Rm}*\operatorname{Rm}
+(\nabla a)*\nabla E
+(\nabla^2a)*E
+a\,\operatorname{Rm}*E .
\]

The normalized component \(-2ag\) contributes

\[
(\nabla^2a)*g
\quad\text{and}\quad
a\,\operatorname{Rm},
\]

which are already contained in the last two classes. Thus the note’s Types A–D cover all terms. Its discussion places \((\nabla^2a)*g\) partly under Type A and partly under Type C, but this is label overlap rather than an omitted contribution.

After contraction with \(2\operatorname{Rm}\),

\[
2a\langle \operatorname{Rm},\Delta\operatorname{Rm}\rangle
=
a\Delta|\operatorname{Rm}|^2
-2a|\nabla\operatorname{Rm}|^2.
\]

The remaining algebraic curvature terms are bounded by

\[
Ca\bigl(|\operatorname{Rm}|^3+|\operatorname{Rm}|^2\bigr)
\le CaF^3,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

The four inverse-metric variations in the norm produce

\[
aE*\operatorname{Rm}*\operatorname{Rm},
\]

bounded by \(CaF^3\). The volume variation is

\[
\partial_t d\mu=-a\,\operatorname{tr}(E)\,d\mu
\]

and contributes at most \(CaF^3\). Since \(a,\eta\) are fixed scalar functions, there are no \(\partial_ta\) or \(\partial_t\eta\) terms.

Consequently, no additional evolution term is missing at the schematic tensor level. The Python script verifies elementary cutoff and Young identities, but it does not instantiate the indexed curvature-variation formula, so it is not an independent index-level derivation.

---

## 2. Hessian-of-\(a\) integration by parts

The exact tensor identity is

\[
\nabla^2a
=2\,d\chi\otimes d\chi+2\chi\,\nabla^2\chi,
\]

not \(2|\nabla\chi|^2+2\chi\nabla^2\chi\) as written in (0.2). The later proof does not use the incorrect scalar version because it integrates these terms by parts.

A typical Hessian term has indexed form

\[
I_C=\int_M \eta^2(\nabla_i\nabla_j a)\,T^{ij}\,d\mu.
\]

Integration by parts gives

\[
I_C
=
-\int_M\eta^2(\nabla_j a)\nabla_iT^{ij}\,d\mu
-2\int_M\eta(\nabla_i\eta)(\nabla_j a)T^{ij}\,d\mu.
\]

The second integrand is not generally a scalar multiple of
\(\nabla a\cdot\nabla\eta\). Mere orthogonality of these two covectors would not suffice. Here the stronger support fact does suffice:

\[
d\eta(x)\ne0
\Longrightarrow \chi(x)=0
\Longrightarrow da(x)=2\chi(x)d\chi(x)=0.
\]

Therefore every tensor contraction containing both \(d\eta\) and \(da\) vanishes pointwise. The buffered geometry genuinely removes this term.

For the first integral,

\[
T=\operatorname{Rm}*E
\quad\text{or}\quad
T=\operatorname{Rm}*g,
\]

so

\[
|\nabla T|
\le C\bigl(|\nabla\operatorname{Rm}|\,|E|
+|\operatorname{Rm}|\,|\nabla E|
+|\nabla\operatorname{Rm}|\bigr)
\le CF|\nabla\operatorname{Rm}|.
\]

This gives exactly the Young structure used in (2.16).

---

## 3. Young absorption and the sign in (2.11)

It is cleaner to avoid the formal quotient at points where \(a=0\). Since

\[
|da|=2|\chi||d\chi|=2\sqrt a\,|d\chi|,
\]

one has pointwise

\[
C|da|F|\nabla\operatorname{Rm}|
\le
\varepsilon a|\nabla\operatorname{Rm}|^2
+C_\varepsilon |d\chi|^2F^2.
\]

Thus

\[
C|da|F|\nabla\operatorname{Rm}|
\le
\varepsilon a|\nabla\operatorname{Rm}|^2
+\frac{C_\varepsilon}{r^2}F^2.
\]

Equivalently, \(|da|^2/a=4|d\chi|^2\) on \(\{a>0\}\), with the preceding direct formula supplying the extension across \(\{a=0\}\). The same estimate applies to:

1. the derivative of the weighted Bochner term;
2. Type B, using \(|\nabla E|\le C|\nabla\operatorname{Rm}|\);
3. Type C after integration by parts.

Equation (2.11) has the wrong displayed inequality direction for the subsequent deduction. What is needed is

\[
\int\eta^2a\Delta|\operatorname{Rm}|^2
\le
\varepsilon D_2+\frac{C}{\varepsilon r^2}H_2.
\]

In fact, the preceding absolute-value estimate proves both directions, so the final estimate (2.12) remains valid after replacing (2.11) by the upper estimate above.

The dimension-dependent multiplicities in Types B and C must be absorbed into the Young constants. Formally, each group can be assigned any prescribed dissipation cost \(\varepsilon_iD_2\), with a corresponding \(C_{\varepsilon_i}r^{-2}H_2\). With \(\sum_i\varepsilon_i=\delta_0\), the final coefficient is \(2-\delta_0\). The script’s numerical \(2-3\varepsilon\) illustration is schematic rather than a tensor-constant computation.

Hence the corrected result is

\[
\boxed{
H_2'+(2-\delta_0)D_2
\le
C\int_M\eta^2aF^3\,d\mu
+\frac{C}{r^2}H_2 .
}
\]

---

## 4. Global defect identity

Let the global flow coefficient be \(A=\sum_j a_j\), with disjoint buffered domains \(\Omega_{\eta,j}\), and define

\[
q_j(t)=\int_M\eta_j^2|E|^2\,d\mu.
\]

Because \(\eta_j=1\) on a neighborhood of \(\operatorname{supp}a_j\), while the region where \(d\eta_j\ne0\) is stationary, the time variation of \(q_j\) equals the full defect-energy variation produced by the \(j\)-th active coefficient. Differential operators do not enlarge support, so derivatives of \(a_jE\) remain supported in \(\operatorname{supp}a_j\).

Under these hypotheses,

\[
Q_{\mathrm{global}}'(t)=\sum_j q_j'(t),
\]

and therefore

\[
Q_{\mathrm{global}}(t)-Q_{\mathrm{global}}(0)
=
\sum_j\bigl(q_j(t)-q_j(0)\bigr).
\]

If

\[
q_j(t)\le e^{Ct/r^2}q_j(0)
\]

and \(t\le\theta r^2\), then

\[
Q_{\mathrm{global}}(t)
\le Q_{\mathrm{global}}(0)
+(e^{C\theta}-1)\sum_jq_j(0).
\]

Disjointness and \(0\le\eta_j\le1\) give

\[
\sum_jq_j(0)\le Q_{\mathrm{global}}(0),
\]

hence

\[
\boxed{
Q_{\mathrm{global}}(t)
\le e^{C\theta}Q_{\mathrm{global}}(0).
}
\]

Thus Section 4 is correct provided \(Q_j\) is understood as the weighted \(q_j\) above and the buffered domains are disjoint. With overlapping \(\eta_j\)-supports, a multiplicity factor would enter.

---

## 5. First-exit Approach A

The maximal-function input in Step 24 is an averaged squared-curvature estimate:

\[
\mathcal M_{R_0}(|\operatorname{Rm}|^2)(p)\le K_{\mathrm{av}},
\]

which yields

\[
\int_{B_{L_\eta r}(p)}|\operatorname{Rm}|^2
\le K_{\mathrm{av}}\operatorname{Vol}(B_{L_\eta r}(p)).
\]

It does not yield

\[
\sup_{B_{L_\chi r}(p)}|\operatorname{Rm}|
\le Cr^{-2}.
\]

A very high curvature peak in a small region away from the selected center is compatible with the centered average estimate. The pointwise condition \(|E|=|\operatorname{Ric}+g|\le\delta\) also does not control the Weyl tensor.

There is additionally a dimensional notation mismatch. The maximal-function threshold for \(|\operatorname{Rm}|^2\) has curvature-squared scale. Its square root has the same scale as \(|\operatorname{Rm}|\). Thus the scale relation would be

\[
\sqrt{K_{\mathrm{av}}}\sim r^{-2},
\]

not \(K_{\mathrm{av}}\sim r^{-2}\).

A Ricci-flow existence time \(c/K\) uses a pointwise curvature bound \(K=\sup|\operatorname{Rm}|\). For the degenerate cutoff equation \(\partial_tg=-2\chi^2(\operatorname{Ric}+g)\), a standard global Ricci-flow theorem also does not directly supply the stated interval; a local-flow existence result with dependence on \(\sup|\operatorname{Rm}|\), \(r^{-1}\), and \(r^{-2}\) is needed.

Likewise, smoothness alone does not give a sequence-uniform estimate

\[
|E(t)-E(0)|=O(\delta).
\]

The homogeneous defect equation suggests, under a pointwise curvature estimate,

\[
\|E(t)\|_\infty
\lesssim
\exp\!\bigl(C(\|\operatorname{Rm}\|_\infty+r^{-2}+1)t\bigr)
\|E(0)\|_\infty.
\]

If \(\|\operatorname{Rm}\|_\infty\lesssim r^{-2}\) were separately available, then \(t\lesssim r^2\) would preserve \(\|E(t)\|_\infty\lesssim\delta\), and the metric displacement would indeed be small. That pointwise curvature input is not furnished by the selected-good-center hypothesis.

One further issue appears in the first-exit formulation: from metric comparability and \(H_2(t)\le2H_2(0)\), the note obtains

\[
\beta_a(t)\le C_{\mathrm{met}}\sqrt2\,\beta_0.
\]

The bootstrap threshold \(2\beta_0\) improves only if
\(C_{\mathrm{met}}\sqrt2<2\), which is not implied by
\(\tfrac12g_0\le g(t)\le2g_0\). A larger bootstrap factor, together with correspondingly smaller initial \(\beta_0\), or much tighter metric comparability would be mathematically consistent.

## Conclusion

The buffered-support \(q=2\) energy estimate survives verification after two local repairs:

1. replace the Hessian identity by
   \(\nabla^2a=2\,d\chi\otimes d\chi+2\chi\nabla^2\chi\);
2. replace the direction in (2.11) by the required upper estimate.

The tensor classes, metric-norm variation, and volume variation are complete. The Hessian cross terms vanish because \(da\) itself vanishes wherever \(d\eta\ne0\), not merely because of scalar orthogonality. The global defect estimate is valid for disjoint buffered domains. The unresolved analytic point is the uniform \(r^2\)-time existence and metric control: an averaged \(L^2\) curvature estimate at one selected center does not provide the pointwise curvature estimate used in Approach A.