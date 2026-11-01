# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step55_darboux_ricci_compatibility.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md",
    "Sessions/S1003A01/workspace/notes/step48_problems1_4_goldberg_bochner_and_supply.md",
    "Sessions/S1003A01/workspace/notes/step53_goldberg_jets_and_canonical_form.md"
  ]
}
```

## Task

Read the Step-55 Goldberg note as a differential geometer. Check the tensor algebra and conventions in the Darboux Ricci-symbol relation, its divergence expansion, the Einstein specialization of AAD equation (33), and the Einstein specialization of AAD equation (47). In particular decide whether eta may be identified with rho_*'', whether coefficients 3/8, 1/4, 3s/4, 1/2, and the term 2 nabla_{J eta(X)} Omega are correct, and whether the conclusion that the bare scalar compatibility is a differential consequence rather than a negative-lambda obstruction is justified. Report corrections and any sharper global identity suggested by the checked equations. Ground the review in the supplied primary-source text; do not invent literature.

## Output

## Differential-geometric verification memo

### 1. Main findings

1. The Darboux-gauge Ricci-symbol relation (1.1) is correct on the tangent space of compatible metrics. The displayed Ricci symbol should be understood after imposing \(\operatorname{tr}h=0\); the unrestricted Ricci symbol has one additional term.
2. The divergence expansion (2.3) and its integrated form (2.4) are correct.
3. With
   \[
   \eta:=\bigl(W^+(\Omega)\bigr)_{\Omega^\perp},
   \]
   the identification
   \[
   \eta=\rho_*''
   \]
   is exact in the AAD normalization; there is no factor of \(2\) or \(\sqrt2\).
4. The coefficients \(3/8\) and \(1/4\) in (3.6), and \(3s/4\), \(1/2\), and the term \(2\nabla_{J\eta(X)}\Omega\) in (3.8), all agree with the supplied AAD text.
5. One substantive correction is needed: for an Einstein metric, the third Gray condition is already \(\eta=0\). It does **not** require \(W_3^+=0\). AAD’s Bianchi equation cancels the \(dq\) and \(\delta W_3^+\) terms when \(\eta=0\), even when \(W_3^+\neq0\).
6. The bare scalar symbol relation contains no information specific to \(\lambda<0\). Once its lower-order remainder is explicitly resolved, however, it may contain \(s\)-dependent torsion-curvature terms. Thus the principal-symbol count gives no \(\lambda<0\)-specific obstruction, while the resolved compatibility equation can still carry sign-dependent geometry.

---

## 2. Darboux Ricci symbol

For an unrestricted symmetric tensor \(h\), the principal symbol of the linearized Ricci tensor is, up to the overall Fourier-sign convention,
\[
\sigma_{\mathrm{Ric}}(\xi)h
=\frac12\left(
\xi\otimes h\xi+h\xi\otimes\xi
-|\xi|^2h-\xi\otimes\xi\,\operatorname{tr}h
\right).
\]
For a variation through metrics compatible with a fixed symplectic form,
\[
HJ+JH=0,\qquad h(X,Y)=g(HX,Y),
\]
and hence \(\operatorname{tr}h=0\). The formula in Step 55 is therefore the correct restricted symbol.

Put \(A=\sigma_{\mathrm{Ric}}(\xi)h\). Since
\[
\xi(J\xi)=0,\qquad h(J\xi,J\xi)=-h(\xi,\xi),
\]
one obtains
\[
A(J\xi,J\xi)=\frac12|\xi|^2h(\xi,\xi).
\]
Also,
\[
\operatorname{tr}A
=h(\xi,\xi)-\frac12|\xi|^2\operatorname{tr}h
=h(\xi,\xi).
\]
Consequently
\[
A(J\xi,J\xi)-\frac12|\xi|^2\operatorname{tr}A=0,
\]
which verifies (1.1).

This scalar relation is linearly distinct from the contracted-Bianchi symbol. For example, with \(\xi=e_1\) and \(J\xi=e_2\), contracted Bianchi fixes
\[
A_{11}=\frac12\operatorname{tr}A,\qquad A_{1j}=0\quad(j\ne1),
\]
whereas (1.1) fixes
\[
A_{22}=\frac12\operatorname{tr}A.
\]
Thus it supplies an additional scalar symbol relation.

Its composite symbol with Ricci is quartic in \(\xi\), so the stated \(n_{N-4}\) prolongation count has the correct order. The arithmetic is also correct:
\[
\begin{aligned}
&12n_N-4n_{N+1}-4n_{N-1}-9n_{N-2}+4n_{N-3}+n_{N-4}\\
&\hspace{4cm}=N^2+8N-5.
\end{aligned}
\]

---

## 3. The operator \(\mathcal C_J\) and the divergence formula

Strictly speaking,
\[
\mathcal C_J(S)
=J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}
-\frac12\Delta(\operatorname{tr}S)
\]
is second order in \(S\), and becomes fourth order in the metric only after setting \(S=\operatorname{Ric}(g)\).

Expanding the divergence gives
\[
\begin{aligned}
\nabla^i\!\left(J_i{}^aJ_j{}^b\nabla^jS_{ab}\right)
={}&(\nabla^iJ_i{}^a)J_j{}^b\nabla^jS_{ab}\\
&+J_i{}^a(\nabla^iJ_j{}^b)\nabla^jS_{ab}\\
&+J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}.
\end{aligned}
\]
On an almost-Kähler four-manifold, \(\Omega\) is self-dual and closed, hence co-closed, so
\[
\nabla^iJ_i{}^a=0.
\]
Therefore
\[
J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}
=
\nabla^i\!\left(J_i{}^aJ_j{}^b\nabla^jS_{ab}\right)
-J_i{}^a(\nabla^iJ_j{}^b)\nabla^jS_{ab},
\]
which is exactly (2.3). On a closed manifold the divergence integrates to zero, giving (2.4). The trace-Laplacian term in \(\mathcal C_J(S)\) also integrates to zero.

If \(S=\operatorname{Ric}=\lambda g\), then \(\lambda\) is constant and
\[
\nabla S=0,\qquad \nabla(\operatorname{tr}S)=0,
\]
so \(\mathcal C_J(\operatorname{Ric})=0\) pointwise.

The resulting interpretation needs one distinction. The unreduced expression \(\mathcal C_J(\operatorname{Ric})=0\) is indeed a differential consequence of the Einstein equation and has no sign-specific content. But after the fourth derivatives cancel and the remainder is written in \(J,\nabla J,R\), the resulting lower-order identity may contain terms such as \(s|\nabla\Omega|^2\). Such an identity can carry sign-dependent information. What the symbol calculation rules out is an obstruction inferred merely from the previously incomplete dimension count.

The supplied material does not contain a component-by-component identification of this particular remainder with a fixed combination of AAD equations (23), (24), and (33). It establishes the same geometric mechanism, but not an explicit equality of coordinate expressions.

---

## 4. Identification \(\eta=\rho_*''\)

AAD equation (8) gives
\[
W_2^+
=\frac12\left(\rho_*''\otimes\Omega+\Omega\otimes\rho_*''\right).
\]
Since \(|\Omega|^2=2\) and \(\rho_*''\perp\Omega\),
\[
W_2^+(\Omega)=\rho_*''.
\]
Moreover, AAD’s \(W_1^+\) satisfies
\[
W_1^+(\Omega)=\frac{\kappa}{6}\Omega,
\]
and \(W_3^+(\Omega)=0\). Hence
\[
W^+(\Omega)=\frac{\kappa}{6}\Omega+\rho_*''.
\]
Therefore, with the Step-53 convention
\[
\eta=\bigl(W^+(\Omega)\bigr)_{\Omega^\perp},
\]
one has exactly
\[
\boxed{\eta=\rho_*''.}
\]

This also matches the block matrix
\[
W^+
=
\begin{pmatrix}
\nu & \eta^*/\sqrt2\\
\eta/\sqrt2 & -\nu I/2+V
\end{pmatrix},
\qquad e_0=\Omega/\sqrt2.
\]

---

## 5. Einstein specialization of AAD equation (33)

AAD Lemma 4, equation (33), is
\[
\begin{aligned}
0={}&-\frac14(d^J(\kappa-s))_Z\Omega
+\frac16(d(\kappa-s)\wedge Z^\flat)^+
+(\delta\rho_*'')_Z\Omega\\
&+\frac\kappa4\nabla_{JZ}\Omega
-\nabla_{\rho_0(Z)}\Omega
+\nabla_{\rho_*''(Z)}\Omega
+\nabla_{JZ}\rho_*''
+2(\delta W_3^+)_Z+A_Z^+.
\end{aligned}
\]

For an Einstein metric,
\[
\operatorname{Ric}=\frac{s}{4}g,\qquad \rho=\frac{s}{4}\Omega,
\]
with \(s\) constant. Thus
\[
\rho_0=0,\qquad \operatorname{Ric}''=0,\qquad d\rho=0,
\]
and from AAD’s definition
\[
A_Z=(d^\nabla\operatorname{Ric}'')_Z+\iota_{JZ}(d\rho)=0.
\]

AAD equation (20) says
\[
s^*-s=|\nabla\Omega|^2=q,
\qquad
s^*=\frac{2\kappa+s}{3},
\]
so
\[
\kappa-s=\frac32q.
\]
Substitution gives
\[
\boxed{
\begin{aligned}
0={}&-\frac38(d^Jq)_Z\Omega
+\frac14(dq\wedge Z^\flat)^+
+(\delta\eta)_Z\Omega\\
&+\frac\kappa4\nabla_{JZ}\Omega
+\nabla_{\eta(Z)}\Omega
+\nabla_{JZ}\eta
+2(\delta W_3^+)_Z .
\end{aligned}}
\]
Thus both questioned coefficients,
\[
-\frac38,\qquad \frac14,
\]
are correct.

---

## 6. Einstein specialization of AAD equation (47)

The general AAD formula (47) contains
\[
-\frac{3s}{4}\nabla_X\Omega
+\left[
\frac13d(\kappa-s)_X
-2\langle(\delta W_3^+)_{JX},\Omega\rangle
\right]\Omega
+2(\nabla_X\rho_*'')''
+2\nabla_{J\rho_*''(X)}\Omega
\]
together with terms involving \(\operatorname{Ric}_0\), \(\operatorname{Ric}''\), and \(A\). All those additional terms vanish in the Einstein setting. Hence
\[
\begin{aligned}
(\nabla^*\nabla(\nabla\Omega))_X
={}&-\frac{3s}{4}\nabla_X\Omega\\
&+\left[
\frac13d(\kappa-s)_X
-2\langle(\delta W_3^+)_{JX},\Omega\rangle
\right]\Omega\\
&+2(\nabla_X\eta)''
+2\nabla_{J\eta(X)}\Omega.
\end{aligned}
\]
Using \(d(\kappa-s)=\frac32dq\) and moving the scalar-curvature term to the left gives
\[
\boxed{
\begin{aligned}
(\nabla^*\nabla(\nabla\Omega))_X
+\frac{3s}{4}\nabla_X\Omega
={}&
\left[
\frac12dq_X
-2\langle(\delta W_3^+)_{JX},\Omega\rangle
\right]\Omega\\
&+2(\nabla_X\eta)''
+2\nabla_{J\eta(X)}\Omega .
\end{aligned}}
\]
Therefore:

- \(3s/4\) is correct;
- \(1/2\) is correct;
- \(2\nabla_{J\eta(X)}\Omega\) is correct.

The last direction is specifically \(J(\eta(X))\). It should not be silently replaced by \(\eta(JX)\); because \(\eta\) is \(J\)-anti-invariant,
\[
\eta(JX)=-J\eta(X).
\]
The sign is therefore sensitive to the ordering.

The source’s curvature-action computation immediately before equation (47) also confirms this term:
\[
(W_2^+\cdot\nabla\Omega)_X
=
-\nabla_{J\rho_*''(X)}\Omega
-\frac12\langle\rho_*'',\nabla_X\Omega\rangle\Omega.
\]
The factor \(-2\) multiplying the curvature action in equation (46) produces
\[
+2\nabla_{J\rho_*''(X)}\Omega.
\]

---

## 7. Correction concerning the Gray branch

AAD Lemma 1 says that the third Gray condition is equivalent to
\[
\operatorname{Ric}''=0,\qquad \rho_*''=0.
\]
For an Einstein metric, \(\operatorname{Ric}''=0\) automatically, so the third Gray condition is simply
\[
\boxed{\eta=\rho_*''=0.}
\]
No assumption \(W_3^+=0\) is present.

Indeed, AAD Corollary 1, equation (37), specializes to
\[
0=
-\frac12(d^Jq)_Z
+2\langle(\delta W_3^+)_Z,\Omega\rangle
+2(\delta\eta)_Z
-\langle\eta,\nabla_{JZ}\Omega\rangle.
\]
Setting \(Z=JX\) gives
\[
\boxed{
\frac12dq_X
-2\langle(\delta W_3^+)_{JX},\Omega\rangle
=
2(\delta\eta)_{JX}
+\langle\eta,\nabla_X\Omega\rangle.}
\]
Thus equation (3.8) can be rewritten without the displayed \(\delta W_3^+\) component:
\[
\begin{aligned}
(\nabla^*\nabla(\nabla\Omega))_X
+\frac{3s}{4}\nabla_X\Omega
={}&
\left[
2(\delta\eta)_{JX}
+\langle\eta,\nabla_X\Omega\rangle
\right]\Omega\\
&+2(\nabla_X\eta)''
+2\nabla_{J\eta(X)}\Omega.
\end{aligned}
\]
When \(\eta=0\), the entire right-hand side vanishes:
\[
\boxed{
\nabla^*\nabla(\nabla\Omega)
+\frac{3s}{4}\nabla\Omega=0.}
\]
This is AAD Proposition 1 in the Einstein case. The cancellation uses the Bianchi equation and does not require \(W_3^+=0\).

The supplied AAD classification then identifies the strictly almost-Kähler Einstein metrics in this Gray class with the Ricci-flat local models. That conclusion uses the full local classification, not merely the Helmholtz equation.

---

## 8. A sharper global energy identity

Let
\[
T=\nabla\Omega,\qquad q=|T|^2.
\]
Pair the verified equation (3.8) with \(T\) and integrate over a closed manifold.

First,
\[
\langle\Omega,T_X\rangle
=\frac12X|\Omega|^2=0,
\]
so the \(\Omega\)-valued scalar term contributes zero.

Second, because \(\eta\) is \(J\)-anti-invariant, its skew endomorphism \(E_\eta\) anti-commutes with \(J\). Hence \(JE_\eta\) is skew. Since
\[
B(X,Y):=\langle T_X,T_Y\rangle
\]
is symmetric,
\[
\sum_i\langle T_{J\eta(e_i)},T_{e_i}\rangle=0
\]
pointwise.

Finally, AAD equation (41) gives in the Einstein case
\[
\nabla^*\nabla\Omega
=2\eta+\frac q2\Omega.
\]
Therefore
\[
\begin{aligned}
2\int_M\sum_i
\langle(\nabla_{e_i}\eta)'',T_{e_i}\rangle\,d\mu
&=
2\int_M\langle\nabla\eta,\nabla\Omega\rangle\,d\mu\\
&=
2\int_M\langle\eta,\nabla^*\nabla\Omega\rangle\,d\mu\\
&=
4\int_M|\eta|^2\,d\mu.
\end{aligned}
\]
The resulting exact identity is
\[
\boxed{
\int_M|\nabla(\nabla\Omega)|^2\,d\mu
+\frac{3s}{4}\int_M q\,d\mu
=
4\int_M|\eta|^2\,d\mu.}
\]
For \(s<0\), this becomes
\[
\boxed{
\int_M|\nabla(\nabla\Omega)|^2\,d\mu
=
\frac{3|s|}{4}\int_M q\,d\mu
+4\int_M|\eta|^2\,d\mu.}
\]

Using the closed canonical form \(\beta\) from Step 53, for which
\[
\int_M|\eta|^2\,d\mu=\int_M\beta\wedge\beta=[\beta]^2,
\]
one obtains the topological-analytic form
\[
\boxed{
\int_M|\nabla(\nabla\Omega)|^2\,d\mu
+\frac{3s}{4}\int_M|\nabla\Omega|^2\,d\mu
=
4[\beta]^2.}
\]

This identity precisely exhibits what the scalar-symbol discussion alone cannot see: after the leading derivatives cancel, the surviving global relation couples the Hessian of \(\Omega\), scalar curvature, torsion energy, and the transverse canonical curvature \(\eta\).