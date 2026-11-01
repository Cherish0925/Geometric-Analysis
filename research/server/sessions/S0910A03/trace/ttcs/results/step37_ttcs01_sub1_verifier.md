# TTCS Independent Branch Record

```json
{
  "step_id": 37,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step37_base_pair_continuation.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md",
    "Sessions/S0910A03/workspace/notes/step36_preceptor_interface_review.md"
  ]
}
```

## Task

Verify the Step 37 base-pair continuation estimate for (∇U, ∇²χ) in the normalized cutoff flow ∂_tg = -2a(Ric+g), a=χ², with U=a(Rm+G). The note claims that assuming sup|U|<∞ on [0,T), the four dangerous terms R_1=χ∇³χ*U, R_2=∇χ*∇²χ*U, R_3=χ∇²χ*∇U, R_4=χ∇χ*∇²U can be handled in the L^p energy of W=∇U by: (i) integrating by parts on R_1 to produce three terms I_{1a}, I_{1b}, I_{1c}, using the χ factor to match diffusion a=χ²; (ii) absorbing I_{1a} via Young with the identity χ²/a=1; (iii) treating R_4 via χ≤√a and Young; (iv) coupling to the Θ=∇²χ evolution via the cutoff-jet equation ∂_tΘ ~ K|Θ| + |W||∇χ|; (v) closing by Gronwall for Y_1=||W||_p^p+||Θ||_p^p with only the known inhomogeneity ||T||_p^p from Step 27 §5. Check whether: (a) the IBP in eq (3.3)-(3.4) correctly produces all three product-rule terms; (b) the χ²/a=1 identity is valid at a=0 (where both vanish); (c) the R_4 estimate does not lose a derivative; (d) the Young conversion from mixed powers in (3.15) to (3.16) is valid; (e) no hidden ||T||_∞ or ||a∇Rm||_∞ coefficient appears; (f) the Gronwall constant C_1(p,K,g_0,χ,T) is indeed finite for each fixed smooth datum.

## Output

# Scientific verification memo

## Main finding

The finite-\(L^p\) base-pair estimate is recoverable, but Step 37 as written has a substantive exponent error in \(I_{1c}\) and \(I_3\). Both terms contain \(|W|^p\), not \(|W|^{p-1}\), and the Hölder estimate (3.11) is false. A second integration by parts on the factor \(\chi\nabla^2\chi\) repairs both terms and yields the stated Grönwall structure without \(\|T\|_\infty\) or \(\|a\nabla\operatorname{Rm}\|_\infty\).

## 1. The \(R_1\) integration by parts

Let
\[
P(W)=|W|^{p-2}W,\qquad
D_p=\int_M a|\nabla W|^2|W|^{p-2}\,d\mu.
\]
Schematically,
\[
I_1=\int_M P(W)*\chi U*\nabla\Theta\,d\mu,
\qquad \Theta=\nabla^2\chi .
\]
Since \(M\) is closed and \(\nabla g=0\),
\[
I_1=-\int_M\Theta*
 \left(\chi U*\nabla P(W)+d\chi*U*P(W)+\chi W*P(W)\right)d\mu .
\]
Thus (3.3)–(3.4) correctly identify the three product-rule contributions: the derivative lands on \(P(W)\), on \(\chi\), or on \(U\).

The first two estimates are valid:
\[
|I_{1a}|
 \le \varepsilon D_p+
 C_{p,\varepsilon}K^2\int|\Theta|^2|W|^{p-2},
\]
and
\[
|I_{1b}|
 \le CK\|d\chi\|_\infty
       \|\Theta\|_p\|W\|_p^{p-1}.
\]

For \(I_{1c}\), however,
\[
|P(W)|\,|\nabla U|
=|W|^{p-1}|W|=|W|^p.
\]
Consequently the correct raw estimate is
\[
|I_{1c}|\le C\int |\chi|\,|\Theta|\,|W|^p,
\]
not (3.9).

## 2. The same error occurs in \(R_3\)

Pairing \(R_3=\chi\Theta*W\) with \(P(W)\) gives
\[
|I_3|\le C\int|\chi|\,|\Theta|\,|W|^p.
\]
The displayed Hölder step (3.11) is invalid. Hölder actually gives
\[
\int |\Theta||W|^p
\le \|\Theta\|_p
   \||W|^p\|_{p/(p-1)}
=\|\Theta\|_p\,
  \|W\|_{p^2/(p-1)}^p,
\]
which is not controlled by \(\|\Theta\|_p\|W\|_p^p\).

Therefore (3.15) does not follow from the estimates currently written: its right-hand side omits the degree-\(p\) terms produced by \(I_{1c}\) and \(I_3\).

## 3. Repair by another signed integration by parts

Both problematic terms have the form
\[
J=\int_M \chi\,\nabla_i\nabla_j\chi\,
           B^{ij}(W)\,d\mu,
\]
where, after the usual \((|W|^2+\delta)^{(p-2)/2}\) regularization if needed,
\[
|B(W)|\le C_p|W|^p,\qquad
|\nabla B(W)|\le C_p|W|^{p-1}|\nabla W|.
\]
Integrating one derivative from \(\nabla^2\chi\),
\[
J=-\int_M \nabla_i\chi\nabla_j\chi\,B^{ij}(W)\,d\mu
  -\int_M\chi\nabla_j\chi\,\nabla_iB^{ij}(W)\,d\mu .
\]
Hence
\[
\begin{aligned}
|J|
&\le C_p\|d\chi\|_\infty^2\int|W|^p
 +C_p\int|\chi||d\chi||W|^{p-1}|\nabla W|\\
&\le \varepsilon D_p+
 C_{p,\varepsilon}\|d\chi\|_\infty^2\int|W|^p .
\end{aligned}
\]
This applies separately to \(I_{1c}\) and \(I_3\). It uses only \(d\chi\), \(W\), and the weighted dissipation; no estimate for \(\Theta\) is needed for these two terms.

With this correction, the intended \(W\)-energy inequality becomes
\[
\begin{aligned}
\frac d{dt}\|W\|_p^p
\le{}&
C_pK^2\|\Theta\|_p^2\|W\|_p^{p-2}
+C_pK\|\Theta\|_p\|W\|_p^{p-1}\\
&+C_p(1+K^p)\|W\|_p^p
+C_p(1+K^p)\|T\|_p^p+C_p .
\end{aligned}
\]

## 4. Behavior at \(a=0\)

The expression \(\chi^2/a\) is literally undefined where \(a=\chi^2=0\). The estimate itself is valid without forming this quotient:
\[
|\chi|=\sqrt a
\]
everywhere, so
\[
\begin{aligned}
K|\chi||\Theta||W|^{p-2}|\nabla W|
={}&K\bigl(\sqrt a|\nabla W||W|^{(p-2)/2}\bigr)
       \bigl(|\Theta||W|^{(p-2)/2}\bigr)\\
\le{}&\varepsilon a|\nabla W|^2|W|^{p-2}
+C_{\varepsilon}K^2|\Theta|^2|W|^{p-2}.
\end{aligned}
\]
Thus no division by \(a\) occurs.

It is also true, for each \(t<T\), that
\[
W=\nabla(aT)=da*T+a\nabla T=0
\quad\text{on }\{\chi=0\},
\]
because \(a=0\) and \(da=2\chi\,d\chi=0\) there. This observation is unnecessary for the Young estimate and is less suitable when \(p=2\), where the factor \(|W|^{p-2}\) is \(1\).

## 5. The \(R_4\) term

The estimate for
\[
R_4=\chi\,d\chi*\nabla^2U
\]
does not lose a derivative. Since \(W=\nabla U\), the relevant second derivative is \(\nabla W\), up to an ordering convention:
\[
\begin{aligned}
|I_4|
&\le C\int |\chi||d\chi||\nabla W||W|^{p-1}\\
&\le \varepsilon D_p+
C_{p,\varepsilon}\|d\chi\|_\infty^2\int|W|^p .
\end{aligned}
\]
If derivatives are reordered, the commutator is \(\operatorname{Rm}*U\). Its contribution carries the existing bounded cutoff factors and is an \(L^p\) source involving \(K|T|\), rather than a pointwise coefficient involving \(T\).

## 6. Young conversion and the coupled inequality

For the terms that actually occur in the corrected inequality,
\[
K^2\|\Theta\|_p^2\|W\|_p^{p-2}
\le C K^p\|\Theta\|_p^p+C\|W\|_p^p,
\]
using exponents \(p/2\) and \(p/(p-2)\), and
\[
K\|\Theta\|_p\|W\|_p^{p-1}
\le CK^p\|\Theta\|_p^p+C\|W\|_p^p,
\]
using \(p\) and \(p/(p-1)\). These conversions are valid.

The cutoff-jet equation follows directly from
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U):
\]
for the tensor \(\Theta=\nabla^2\chi\),
\[
|\partial_t\Theta|\le C|W||d\chi|,
\]
while variation of its norm and of \(d\mu_t\) adds \(CK|\Theta|\). Therefore
\[
\frac d{dt}\|\Theta\|_p^p
\le C_pK\|\Theta\|_p^p
+C_p\|d\chi\|_\infty
   \|W\|_p\|\Theta\|_p^{p-1},
\]
and hence
\[
\frac d{dt}\|\Theta\|_p^p
\le C_p(1+K)
 \bigl(\|\Theta\|_p^p+\|W\|_p^p\bigr).
\]

After the corrected treatment of \(I_{1c}\) and \(I_3\),
\[
Y_1' \le C_1\bigl(1+Y_1+\|T\|_p^p\bigr),
\qquad
Y_1=\|W\|_p^p+\|\Theta\|_p^p,
\]
is justified.

## 7. Absence of pointwise unweighted curvature coefficients

The potentially troublesome commutator terms can be grouped as
\[
a\operatorname{Rm}*W=(U-aG)*W,
\]
and
\[
a\nabla\operatorname{Rm}*U
=a\nabla T*U
=(W-da*T)*U.
\]
Also,
\[
(\partial_t\Gamma)*U=\nabla\operatorname{Ric}(U)*U=W*U.
\]
Thus the resulting terms are bounded by combinations of
\[
K|W|,\qquad K|da||T|,\qquad K^2,\qquad 1,
\]
and pairing with \(|W|^{p-2}W\) uses only \(\|T\|_p^p\) through Young’s inequality. Neither \(\|T\|_\infty\) nor \(\|a\nabla\operatorname{Rm}\|_\infty\) is required.

## 8. Finiteness of the Grönwall data

For finite \(T\) and fixed smooth \((g_0,\chi)\):

- \(|\partial_tg|_g\le C_nK\) gives metric equivalence with constants depending on \(K,T,g_0\);
- this controls volume comparison and \(\|d\chi\|_\infty\);
- \(W(0)\) and \(\Theta(0)\) have finite \(L^p\) norms;
- Step 27 equation (5.4), if taken as established, gives
  \(\sup_{t<T}\|T(t)\|_p<\infty\).

Therefore \(C_1(p,K,g_0,\chi,T)\) and
\[
\int_0^T(1+\|T(s)\|_p^p)\,ds
\]
are finite. The corrected Grönwall argument yields the stated finite-\(L^p\) base-pair bound. Direct energy arguments cover \(p\ge2\); lower finite exponents follow from a higher-\(p\) estimate and uniform volume comparison.

## 9. Separate issue in Step 37 §6

The sentence asserting that \(p>n\) and \(L^p\) bounds alone imply
\[
\|W\|_\infty+\|\Theta\|_\infty<\infty
\]
is mathematically incorrect. Sobolev embedding requires
\[
\|W\|_{W^{1,p}},\qquad \|\Theta\|_{W^{1,p}},
\]
whereas Step 37 supplies only spatial \(L^p\) bounds and a time-integrated, \(a\)-weighted gradient term for \(W\). Bounds for every finite \(p\), with constants depending on \(p\), also do not imply \(L^\infty\).

Thus the repaired argument establishes the boxed finite-\(L^p\) base-pair theorem, but the later pointwise upgrade and full continuation still depend on a complete higher-order staggered-exponent derivation.