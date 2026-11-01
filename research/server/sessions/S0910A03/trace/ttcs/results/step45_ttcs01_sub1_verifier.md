# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A03/workspace/notes/step44_arbitrary_order_tensor_ledger.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently check the corrected coordinate-time tensor ledger for the normalized coefficient flow. The active equations are ∂_t g=-2 Ric(U), T=Rm+g∧g/[2(n-1)], U=bT, b=χ²+ε². Read the new Step 45 note, the superseded Step 44 ledger, Wang's exact coordinate-time local Ricci-flow formulas, and the zero-order seed. Verify: (i) consistency of the ∂_t convention, ∂_t G, ∂_tΓ, [∂_t,∇^m], and cutoff-jet evolution; (ii) the base T and division-free U equations including all coefficient weights; (iii) the corrected differentiated family ∇^{r+1}b*∇^{s+1}b*T_t and its χ factors; (iv) exhaustive current-variable allocations, spatial/time commutators, and signed integrations; (v) whether the staggered finite-Lp estimates really close uniformly for b=χ²+ε² without hidden T∞, current-exponent escalation, ε^{-1}, or an omitted current derivative. Give explicit corrections to any formula or inference; do not infer correctness from schematic notation alone.

## Output

# Scientific verification memo

## Main conclusion

The coordinate-time reformulation repairs the substantive inconsistency in Step 44, and the retained family  
\[
B_{r+1}*B_{s+1}*T_t
\]
correctly preserves the two \(\chi\)-factors needed at the current \(T_m\) and \(C_{m+1}\) allocations. Subject to a smooth fixed-\(\varepsilon\) solution and the bootstrap assumptions \(\|U_0\|_\infty\le K\) and metric equivalence, the staggered finite-\(L^p\) induction closes with constants independent of \(0<\varepsilon\le1\). It does not require \(T_0\in L^\infty\), does not create a current-level \(p\mapsto2p\) loop, and introduces no inverse power of \(\varepsilon\).

Three literal corrections are needed:

1. Step 45 equation (1.2) has a factor-of-two error in \(\partial_tG\).
2. The “complete” current tables (4.2) and (4.6) omit the bounded normalization terms \(bT_m\) and \(bU_m\), respectively.
3. The spatial-commutator families should retain \(\operatorname{Rm}\) explicitly at derivative order zero; in the \(U_m\) equation the extremal term \(bT_m*U_0\) must be displayed and reduced to \(U_m*U_0\) plus previous levels.

These corrections alter neither the triangular ordering nor the \(\varepsilon\)-uniform estimates.

---

## 1. Coordinate-time convention

Let \(S=\operatorname{Ric}(U)\), so \(\partial_tg=-2S\).

### 1.1 Variation of \(G\)

With
\[
G=\frac{g\owedge g}{2(n-1)},
\]
bilinearity gives
\[
\begin{aligned}
\partial_tG
&=\frac{(-2S)\owedge g+g\owedge(-2S)}{2(n-1)}\\
&=-\frac{S\owedge g+g\owedge S}{n-1}
=-\frac{2}{n-1}S\owedge g ,
\end{aligned}
\]
where the last equality uses symmetry of the Kulkarni–Nomizu product on symmetric two-tensors.

Thus Step 45 (1.2), which has denominator \(2(n-1)\) after differentiation, is smaller by a factor two. A direct scaling test confirms this: if \(S=g\), then \(\partial_tg=-2g\) and \(G\), quadratic in \(g\), satisfies \(\partial_tG=-4G\); the displayed Step 45 formula would give \(-2G\).

This affects only fixed numerical coefficients in the lower algebraic normalization terms. The weight remains algebraic in \(U\).

### 1.2 Connection and tensor commutators

The coordinate variation
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}\bigl(\nabla_iS_{j\ell}+\nabla_jS_{i\ell}
-\nabla_\ell S_{ij}\bigr)
\]
is correct. Since \(S=\operatorname{Ric}(U)\) and \(\nabla g^{-1}=0\),
\[
\nabla^r(\partial_t\Gamma)=g^{-1}*U_{r+1}
\]
for an ordered covariant derivative.

For a covariant tensor \(A\),
\[
\partial_t(\nabla^mA)
=\nabla^m(\partial_tA)
+\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA
\]
is the correct universal-contraction formula. Reordering derivative slots can add derivatives of \(\operatorname{Rm}\) multiplying lower derivatives of \(A\), but no \(U_{m+1}\) is created by this reordering.

### 1.3 Cutoff jets

Because \(\chi\) is fixed as a scalar in the chosen coordinates,
\[
\partial_t(d\chi)=0.
\]
Writing \(C_{m+1}=\nabla^m(d\chi)\), one obtains
\[
\partial_tC_{m+1}
=\sum_{r+s=m-1}U_{r+1}*C_{s+1}.
\]
The unique current allocation is \(U_m*C_1\). There is no raw \(U_0*C_{m+1}\), \(U_{m+1}\), or \(C_{m+2}\) term. The \(U_0|C_{m+1}|^p\) contribution arises only when differentiating the tensor norm and volume form. This resolves the Step 44 mixing between a metric-compatible time derivative and coordinate time.

---

## 2. Base \(T\) and \(U\) equations

Wang’s exact coordinate formula in §4 for
\[
\partial_tg=-2\chi^2\operatorname{Ric}
\]
contains precisely:

- \(\chi^2\Delta\operatorname{Rm}\);
- first derivatives of \(\chi^2\) multiplying \(\nabla\operatorname{Ric}\);
- Hessians of \(\chi^2\) multiplying \(\operatorname{Ric}\);
- quadratic curvature terms carrying \(\chi^2\).

Replacing \(\chi^2\) by \(b\), putting \(E=\operatorname{Ric}(T)=\operatorname{Ric}+g\), and adding the corrected algebraic variation of \(G\) gives
\[
\partial_tT
=b\Delta T+B_1*\nabla T+B_2*T+b(T*T+T+1).
\]
The numerical coefficients and contractions are not determined by this shorthand, but every displayed coefficient weight is correct. In particular, every quadratic curvature reaction carries \(b\), and the only second coefficient derivatives are signed \(\nabla^2b\)-contractions.

Multiplying by \(b\), using \(\partial_tb=0\), and substituting
\[
\nabla U=b\nabla T+B_1*T,\qquad
\Delta U=b\Delta T+2B_1*\nabla T+(\Delta b)T,
\]
gives
\[
\partial_tU
=b\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+bU+b^2.
\]
This is genuinely division-free. The only unweighted curvature factor is in \((B_1*B_1)*T\). No \(B_2*T\) remains after the change to \(U\), because \(bB_2*T=B_2*U\).

The factor-two correction in \(\partial_tG\) changes only the universal coefficients hidden in \(bU\) and the other lower algebraic terms.

---

## 3. Differentiated families and current allocations

### 3.1 Spatial commutators

The precise commutator family is
\[
b\sum_{r+s=m}\nabla^r\operatorname{Rm}*\nabla^sA.
\]
For \(r\ge1\), \(\nabla^r\operatorname{Rm}=T_r\). For \(r=0\),
\[
b\operatorname{Rm}=b(T-G)=U-bG.
\]
Thus the Step 45 notation \(b*T_r*A_s\) is valid only after recording this bounded \(G\)-correction.

In the \(U_m\) equation, the extremal allocation \(r=m,s=0\) is
\[
bT_m*U_0.
\]
It must be reduced using
\[
bT_m
=U_m-\sum_{q=1}^m B_q*T_{m-q},
\]
with the usual universal multiplicities. It therefore contributes \(U_m*U_0\) plus previous spatial levels. No current \(T_m\) norm is needed.

### 3.2 Corrected \(B*B*T\) family

Differentiating \((B_1*B_1)*T\) gives exactly
\[
B_{r+1}*B_{s+1}*T_t,\qquad r+s+t=m.
\]
It must not be replaced globally by \(C_{r+1}*C_{s+1}*T_t\), because
\[
B_k=2\chi C_k+\sum_{\mathcal P_k}'C_{|I|}*C_{k-|I|}.
\]

The current \(T_m\) allocation is uniquely \(r=s=0,t=m\):
\[
\begin{aligned}
B_1*B_1*T_m
&=4\chi^2(C_1*C_1)*T_m\\
&=4\frac{\chi^2}{b}(C_1*C_1)*
\left(U_m-\sum_{q=1}^m B_q*T_{m-q}\right).
\end{aligned}
\]
Hence the current coefficient is bounded by \(4|C_1|^2\).

The current cutoff jet occurs only for
\[
(r,s,t)=(m,0,0)\quad\text{or}\quad(0,m,0).
\]
Its leading part is
\[
(2\chi C_{m+1})*(2\chi C_1)*T_0
=4\frac{\chi^2}{b}C_{m+1}*C_1*U_0.
\]
This is the decisive repair: its coefficient uses \(U_0\in L^\infty\), not \(T_0\in L^\infty\).

For \(\varepsilon=0\), the literal quotient \(\chi^2/b\) is undefined where \(\chi=0\). The identities should then be written directly as
\[
B_1B_1T_m=4C_1C_1\,(bT_m),
\qquad
4\chi^2C_{m+1}C_1T_0=4C_{m+1}C_1U_0,
\]
or one may set the symbolic coefficient \(q_0\equiv1\). The regularized estimates themselves use \(\varepsilon>0\).

### 3.3 Missing bounded entries in the current tables

The \(T_m\) row of Step 45 (4.2) also contains
\[
bT_m,
\]
coming from (T6) with \(r=0\). The full zeroth-order current structures are therefore
\[
B_2*T_m,\qquad U_0*T_m,\qquad b*T_m,
\]
together with the bounded \(bG*T_m\) correction from the spatial commutator.

Likewise, the \(U_m\) row of (4.6) also contains
\[
bU_m,
\]
from (U7) with \(r=0\). Before reduction, it also contains \(bT_m*U_0\) from the extremal spatial commutator. After the identity above, this joins the \(U_0*U_m\) row.

Both omitted entries are harmless because \(0<b\le2\), but the tables are not literally exhaustive without them.

No further current derivative is missing:

- \(T_{m+1}\) and \(U_{m+1}\) arise only with \(B_1=2\chi C_1\);
- \(C_{m+2}\) arises only from the leading term \(2\chi C_{m+2}\);
- the time commutator produces \(U_m*T_0\) in the \(T_m\) equation and at most \(U_m*U_0\) in the \(U_m\) equation;
- the cutoff evolution contains \(U_m*C_1\), but no \(U_{m+1}\).

---

## 4. Signed integrations and finite-exponent closure

Let \(V=U_m\), \(Z=C_{m+1}\), and \(P(V)=|V|^{p-2}V\), \(p\ge2\).

### 4.1 First derivative of the coefficient

Every \(B_1*\nabla V\) term is absorbed through
\[
\frac{|B_1|^2}{b}
=4\frac{\chi^2}{b}|C_1|^2
\le4|C_1|^2.
\]
The same estimate handles the derivative of \(b\) produced when integrating \(b\Delta V\).

### 4.2 Hessian terms

A current \(B_2*V\) contribution has the form
\[
\int(\nabla_i\nabla_jb)\,\mathcal B^{ij}(V),
\]
with
\[
|\mathcal B(V)|\le C_p|V|^p,\qquad
|\nabla\mathcal B(V)|\le C_p|V|^{p-1}|\nabla V|.
\]
Integration by parts gives
\[
\left|\int\nabla^2b*\mathcal B(V)\right|
\le \delta\int b|\nabla V|^2|V|^{p-2}
 +C_{\delta,p}\|C_1\|_\infty^2\int|V|^p.
\]
This uses only \(|db|^2/b\le4|C_1|^2\), not a pointwise estimate for \(C_2\).

The \(m=1\) term \(\chi C_2*U_1*P(U_1)\), and the \(m=2\) term arising after the second integration,
\(\chi C_2*U_2*P(U_2)\), have the same signed-Hessian form.

### 4.3 Top cutoff jet

Integrating
\[
\chi C_{m+2}*U_0*P(V)
\]
once yields
\[
C_1*Z*U_0*P(V),\quad
\chi Z*U_1*P(V),\quad
\chi Z*U_0*\nabla P(V).
\]
The last term leaves
\[
|Z|^2|V|^{p-2},
\]
which uses only current \(L^p\) norms:
\[
\int |Z|^2|V|^{p-2}
\le \frac2p\|Z\|_p^p+\frac{p-2}{p}\|V\|_p^p.
\]

For \(m\ge2\), integrating \(\chi Z*U_1*P(V)\) again gives
\[
C_1*C_m*U_1*P(V),\quad
\chi C_m*U_2*P(V),\quad
\chi C_m*U_1*\nabla P(V),
\]
plus derivative-reordering terms. Those reordering terms contain
\[
\nabla^q\operatorname{Rm}*C_s*U_1*P(V),\qquad q\le m-1,
\]
and therefore use previous \(T\)-levels. The derivative term is absorbed by weighted dissipation and leaves products of previous factors against \(|V|^{p-2}\).

The corrected \(B*B*T\) current-jet term is
\[
\frac{\chi^2}{b}C_1*Z*U_0*P(V),
\]
which is another same-exponent \(Z\,|V|^{p-1}\) term.

Thus the pair estimate has the stated form
\[
\frac d{dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+c_{m,p}\int b|\nabla U_m|^2|U_m|^{p-2}
\le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
\]

### 4.4 Subsequent \(T_m\) estimate

After the pair is known for every finite exponent, put \(X=T_m\). The top cutoff term yields
\[
C_1*C_{m+1}*T_0*P(X),\quad
\chi C_{m+1}*T_1*P(X),\quad
\chi C_{m+1}*T_0*\nabla P(X).
\]
The last term leaves
\[
|C_{m+1}|^2|T_0|^2|X|^{p-2}.
\]
It is controlled without \(T_0\in L^\infty\):
\[
\begin{aligned}
\int |C_{m+1}|^2|T_0|^2|X|^{p-2}
&\le C_p\|C_{m+1}T_0\|_p^p+C_p\|X\|_p^p\\
&\le C_p\|C_{m+1}\|_{2p}^p\|T_0\|_{2p}^p+C_p\|X\|_p^p.
\end{aligned}
\]
Similarly, the time-commutator forcing \(U_m*T_0\) uses \(U_m,T_0\in L^{2p}\), both already available.

At \(m=1\), \(\chi C_2*T_1*P(T_1)\) is again a signed Hessian contraction. Hence
\[
\frac d{dt}\|T_m\|_p^p
+c_{m,p}\int b|\nabla T_m|^2|T_m|^{p-2}
\le C_{m,p}(1+\|T_m\|_p^p).
\]

There is no current-level exponent loop. The \((U_m,C_{m+1})\) estimate at exponent \(p\) uses those two tensors only in \(L^p\). The later \(T_m\) estimate at exponent \(p\) may use the already completed pair at \(2p\) or another finite exponent.

---

## 5. Zero-order seed and \(\varepsilon\)-uniformity

The zero-order argument extends from \(a=\chi^2\) to
\[
b=\chi^2+\varepsilon^2
\]
by replacing
\[
\frac{|\nabla a|^2}{a}=4|d\chi|^2
\]
with
\[
\frac{|\nabla b|^2}{b}
=4\frac{\chi^2}{b}|d\chi|^2
\le4|d\chi|^2.
\]
The quadratic term remains
\[
b|T|^{p+1}=|U|\,|T|^p,
\]
and the signed Hessian integration uses \(db=2\chi\,d\chi\), independent of \(\varepsilon\). Therefore the zero-order \(T_0\) estimates are uniform for \(0<\varepsilon\le1\).

At every higher stage the constants use only
\[
0<b\le2,\qquad
B_r=\nabla^r(\chi^2)\quad(r\ge1),\qquad
\frac{|B_1|^2}{b}\le4|C_1|^2,\qquad
0\le\frac{\chi^2}{b}\le1.
\]
No derivative of \(b^{-1}\) occurs. Initial derivatives of \(U=bT\) are also uniform because \(B_0=b\le2\) and \(B_r\), \(r\ge1\), is independent of \(\varepsilon\).

Thus the regularized finite-\(L^p\) propagation is supported on a common per-datum bootstrap interval. The fixed-\(\varepsilon\) DeTurck start and the transport of the coefficient under the gauge diffeomorphism remain an external analytic input; Wang’s supplied paper cites Yang’s short-time theorem but does not contain the normalized coefficient-regularized construction itself.