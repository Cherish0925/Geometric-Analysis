# TTCS Independent Branch Record

```json
{
  "step_id": 50,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step50_normalized_yang_wang_verification.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently verify the normalized Wang continuation argument in Step 50. Read the actual Wang source and the Step 40/44/45 shifted-curvature notes. Focus on whether the equations for T=Rm+G, U=χ²T, evolving cutoff jets C_j, and connection difference really support the staggered inequalities (3.9),(3.11),(3.12), pointwise all-order bounds, fixed-coordinate convergence, and restart under only bounded |χ²Rm| on a positive-time slab. Look for hidden use of pointwise unweighted T, a prescribed Hessian cutoff, exponent escalation, missing current derivative, incorrect ∂tΓ, insufficient Sobolev order, or endpoint integrability. Give exact repairs if needed and state what is actually established.

## Output

# Scientific verification memo

## 1. Main mathematical finding

The normalized continuation statement is supported by Wang’s source together with the corrected tensor ledger in Steps 40, 44, and 45:

> Let \(M\) be closed, \(0<T_*<\infty\), and let
> \[
> \partial_tg=-2\chi^2(\operatorname{Ric}_g+g)
> \]
> be smooth on \([0,T_*)\). If, for some \(\tau<T_*\),
> \[
> \sup_{M\times[\tau,T_*)}|\chi^2\operatorname{Rm}|<\infty,
> \]
> then \(g(t)\) converges in every fixed-background \(C^k\) norm to a smooth positive-definite metric \(g_*\) as \(t\uparrow T_*\). Combined with the per-datum normalized Yang short-time theorem in Step 50 §2, the given solution can be smoothly continued past \(T_*\).

The terminal-slab formulation is slightly stronger and more precise than Step 50 Theorem 3.1: no estimate near \(t=0\) is needed. Constants depend on \(g(\tau)\), \(\chi\), \(K\), \(T_*-\tau\), and \(n\).

The proof does not require a pointwise estimate for unweighted \(T\) until after the full finite-exponent induction, does not treat \(\nabla^2\chi\) as fixed tensor data, and does not require integration of a \(t^{-1}\) estimate at zero.

---

## 2. Agreement with Wang’s actual source

Wang’s Theorem 4.1 states that an unnormalized local Ricci flow extends if \(\chi^2\operatorname{Rm}\) stays pointwise bounded. The mechanism is exactly the three-family dependence stated in Remark 4.2:

1. derivatives of \(\chi^2\operatorname{Rm}\);
2. derivatives of unweighted \(\operatorname{Rm}\);
3. evolving covariant derivatives of \(\chi\).

The relevant source formulas are:

- Lemma 4.4: the \(\nabla^m\operatorname{Rm}\) evolution;
- Lemma 4.5: the \(\nabla^m(\chi^2\operatorname{Rm})\) evolution;
- Lemma 4.6: evolution of \(\nabla^m\chi\);
- Lemma 4.10: the unweighted \(L^p\) curvature seed using signed integration of the Hessian-cutoff term;
- Propositions 4.13–4.14: alternating control of unweighted and weighted derivatives.

The shifted normalization preserves this structure. With
\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad U=aT,\qquad a=\chi^2,
\]
one has
\[
\operatorname{Ric}(G)=g,\qquad
\operatorname{Ric}(T)=\operatorname{Ric}+g,\qquad
\partial_tg=-2\operatorname{Ric}(U).
\]
Moreover, \(\nabla G=0\), while
\[
\partial_tG=-\frac{2a}{n-1}(E\owedge g),\qquad E=\operatorname{Ric}+g,
\]
is algebraic in \(U\). Thus the shift adds no new highest spatial derivative.

The source writes \(p>100\). For the endpoint Sobolev step one may simply choose
\[
p>\max\{100,n\}.
\]
The corrected energy calculations themselves work for every finite \(p\ge2\).

---

## 3. Exact tensor equations and current terms

### 3.1 Metric and connection

If \(S=\operatorname{Ric}(U)\), then
\[
\partial_tg=-2S
\]
and the coordinate-time connection variation is
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}\bigl(\nabla_iS_{j\ell}
+\nabla_jS_{i\ell}-\nabla_\ell S_{ij}\bigr). \tag{3.1}
\]
Since \(S\) is a contraction of \(U\) and \(\nabla g^{-1}=0\),
\[
\nabla^r(\partial_t\Gamma)=g^{-1}*\nabla^{r+1}U \tag{3.2}
\]
for ordered covariant derivatives. Reordering derivative slots adds curvature times strictly lower derivatives.

This verifies the derivative count used in Steps 45 and 50. In particular, there is no missing \(U_{m+1}\) in the evolution of \(C_{m+1}\).

### 3.2 Evolving cutoff jets

For \(C_j=\nabla^j\chi\), coordinate time gives
\[
\partial_tC_1=0,
\]
and, for \(m\ge1\),
\[
\partial_tC_{m+1}
=\sum_{r+s=m-1}U_{r+1}*C_{s+1}. \tag{3.3}
\]
The unique current allocation is
\[
U_m*C_1.
\]
An \(U_0*C_{m+1}\) contribution appears only when differentiating the tensor norm and volume measure in the \(L^p\) energy. It is not part of the raw tensor equation.

This matches Wang’s Lemma 4.6 after replacing \(\chi^2\operatorname{Rm}\) by \(U\).

### 3.3 Curvature equations

The coordinate-time structural equations are
\[
\partial_tT
=a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T+1), \tag{3.4}
\]
and
\[
\partial_tU
=a\Delta U+B_1*\nabla U+B_2*U
+(B_1*B_1)*T+U*U+aU+a^2, \tag{3.5}
\]
where \(B_j=\nabla^ja\).

The essential coefficient expansion is
\[
B_j=2\chi C_j+
\sum_{1\le q\le j-1}C_q*C_{j-q},\qquad
B_1=2\chi C_1. \tag{3.6}
\]

Two division-free conversions must remain explicit in the \(U_m\) equation:

\[
B_1*B_1*T_m
=4C_1*C_1*(aT_m)
=4C_1*C_1*
\left(U_m-\sum_{q=1}^mB_q*T_{m-q}\right), \tag{3.7}
\]
and
\[
aT_m=U_m-\sum_{q=1}^mB_q*T_{m-q}. \tag{3.8}
\]

Equation (3.8) also removes the apparent current \(T_m\) in the spatial curvature commutator \(a\nabla^m\operatorname{Rm}*U_0\). No division by \(a\) occurs.

The coordinate-time ledger in Step 45 §§1–5 is valid at \(a=\chi^2\). Its later nonlinear coefficient-regularization construction is not used in the Step 50 continuation proof.

---

## 4. Verification of the energy hierarchy

### 4.1 Metric equivalence and the \(T_0\) seed

If
\[
|\chi^2\operatorname{Rm}|\le K,
\]
then
\[
|U|\le K+c_n\|\chi\|_\infty^2.
\]
Step 50’s \(K+C_n\) assumes the usual normalization \(0\le\chi\le1\). Consequently
\[
|\partial_tg|_g\le c_n|U|,
\]
which gives uniform bilipschitz comparison on the finite terminal slab. Volume, scalar Sobolev constants, and \(|d\chi|\) are therefore uniformly controlled.

Testing (3.4) against \(|T|^{p-2}T\) gives the weighted dissipation
\[
\int a|\nabla T|^2|T|^{p-2}.
\]
The quadratic reaction is controlled by
\[
a|T|^{p+1}=|U|\,|T|^p.
\]
For the Hessian term,
\[
I_H=\int(\nabla_i\nabla_ja)\,
\mathcal B^{ij}(T,E)|T|^{p-2},
\]
where
\[
|\mathcal B|\le c_n|T|^2,\qquad
|\nabla\mathcal B|\le c_n|T||\nabla T|.
\]
Integration by parts gives only \(da=2\chi\,d\chi\), and
\[
|da|=2\sqrt a\,|d\chi|
\]
pairs directly with the weighted dissipation. This yields
\[
\frac d{dt}\|T\|_p^p
+c_p\int a|\nabla T|^2|T|^{p-2}
\le C_p\|T\|_p^p+C_p\operatorname{Vol}. \tag{4.1}
\]
Thus \(T_0\) is uniformly bounded in every finite \(L^p\) norm. No pointwise unweighted curvature enters here.

### 4.2 The pair \((U_m,C_{m+1})\)

Set
\[
V=U_m,\qquad Z=C_{m+1}.
\]
The only current derivative \(U_{m+1}\) occurs with
\[
B_1*U_{m+1}=2\chi C_1*U_{m+1},
\]
so it is absorbed into
\[
D_{m,p}=\int a|\nabla V|^2|V|^{p-2}.
\]

Every \(B_2*V\) contraction is integrated in signed form:
\[
\int(\nabla^2a)*\mathcal B(V),
\qquad
|\mathcal B(V)|\lesssim |V|^p,\quad
|\nabla\mathcal B(V)|\lesssim |V|^{p-1}|\nabla V|.
\]
Again only \(d\chi\) remains.

The highest cutoff source has the form
\[
\int\chi C_{m+2}*\mathcal A(U_0)*P(V),\qquad
P(V)=|V|^{p-2}V.
\]
After one integration by parts it produces
\[
C_1*Z*U_0*P(V),\qquad
\chi Z*U_1*P(V),\qquad
\chi Z*U_0*\nabla P(V). \tag{4.2}
\]
The last term leaves
\[
\int |Z|^2|V|^{p-2},
\]
and the pointwise Young inequality
\[
|Z|^2|V|^{p-2}
\le \frac2p|Z|^p+\frac{p-2}{p}|V|^p \tag{4.3}
\]
uses only the current exponent \(p\).

All occurrences of the middle term \(\chi Z*U_1*P(V)\) must be treated together. For \(m\ge2\), write \(Z=\nabla C_m\) and integrate once more. The resulting terms contain:

- \(d\chi*C_m*U_1*P(V)\);
- \(\chi C_m*U_2*P(V)\);
- \(\chi C_m*U_1*\nabla P(V)\);
- curvature-commutation terms involving only \(T_j\) with \(j<m\).

At \(m=2\), the second term is
\[
\chi\nabla^2\chi*U_2*P(U_2),
\]
which is another signed Hessian integral. At \(m=1\), the original expression already has this form. For \(m\ge3\), \(C_m\) and \(U_2\) are earlier spatial levels.

Combining this with (3.3) yields
\[
\frac d{dt}\left(\|U_m\|_p^p+\|C_{m+1}\|_p^p\right)
+c_{m,p}D_{m,p}
\le C_{m,p}\left(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\right). \tag{4.4}
\]
This verifies Step 50 equation (3.11).

### 4.3 The subsequent \(T_m\) estimate

After the pair has been controlled for every finite exponent, set \(X=T_m\). The top cutoff source is
\[
\int\chi C_{m+2}*T_0*P(X).
\]
One integration gives
\[
d\chi*C_{m+1}*T_0*P(X),
\quad
\chi C_{m+1}*T_1*P(X),
\quad
\chi C_{m+1}*T_0*\nabla P(X). \tag{4.5}
\]

The last term is absorbed into the weighted dissipation and leaves
\[
|C_{m+1}|^2|T_0|^2|X|^{p-2}.
\]
Here \(C_{m+1}\) and \(T_0\) may be used in \(L^{2p}\), because the current pair and the earlier levels have already been established for every finite exponent. This is not an ascent involving the still-unknown \(X\).

For \(m=1\), the middle term in (4.5) is
\[
\chi C_2*T_1*P(T_1),
\]
again a signed Hessian integral. For \(m\ge2\), \(T_1\) is an earlier level.

The time-connection term \(U_m*T_0\) is an \(L^p\) forcing obtained from \(U_m,T_0\in L^{2p}\); it is not used as a pointwise coefficient. Current quadratic curvature terms have coefficient \(aT_0=U_0\), which is pointwise bounded. Therefore
\[
\frac d{dt}\|T_m\|_p^p
+c_{m,p}\int a|\nabla T_m|^2|T_m|^{p-2}
\le C_{m,p}(1+\|T_m\|_p^p). \tag{4.6}
\]
This verifies Step 50 equation (3.12).

The induction is genuinely triangular:
\[
T_0\to(U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots.
\]
At each spatial level the statement is first proved for all finite exponents. Larger exponents are used only for already completed levels.

---

## 5. Pointwise estimates and fixed-coordinate convergence

Choose \(p>n\). Uniform scalar Sobolev embedding and Kato’s inequality give
\[
\|U_m\|_\infty
\le C\bigl(\|U_m\|_p+\|U_{m+1}\|_p\bigr),
\]
and similarly for \(T_m\) and \(C_m\). Thus every covariant derivative of all three tensor families is uniformly pointwise bounded.

For fixed-coordinate order \(k\), the connection argument uses pointwise \(U_{k+1}\), which in turn uses \(L^p\) control through \(U_{k+2}\). The all-order induction supplies these two additional \(L^p\) levels.

Let \(\bar\nabla=\nabla^{g(0)}\) and
\[
A=\nabla^g-\bar\nabla.
\]
Then
\[
\partial_tA=g^{-1}*\nabla\operatorname{Ric}(U). \tag{5.1}
\]
Iterating \(\bar\nabla=\nabla+A*\), one obtains
\[
\partial_t\bar\nabla^kA
=\bar\nabla^k\!\left(g^{-1}*\nabla\operatorname{Ric}(U)\right).
\]
The right side contains \(\nabla^{k+1}U\) and \(\bar\nabla^jA\) only for \(j<k\). This gives a triangular induction:
\[
\sup_{t<T_*}\|\bar\nabla^kA(t)\|_\infty<\infty.
\]
Consequently
\[
\sup_{t<T_*}\|\partial_t\bar\nabla^kg(t)\|_\infty<\infty. \tag{5.2}
\]
Since the terminal interval has finite length, (5.2) makes \(g(t)\) Cauchy in every fixed \(C^k\) norm. Metric equivalence preserves positive definiteness, so the limit \(g_*\) is smooth and Riemannian.

---

## 6. Restart and smooth joining

The Wang energy argument reaches the smooth terminal metric \(g_*\). The post-\(T_*\) segment comes from Step 50 Theorem 2.1, the normalized Yang per-datum short-time construction.

Smooth joining does not require uniqueness. Along the left segment,
\[
\partial_tg=F(g),\qquad F(g)=-2a(\operatorname{Ric}_g+g).
\]
Because \(g(t)\to g_*\) in every spatial \(C^k\) norm, every left time jet is obtained recursively as a differential polynomial in \(g_*\), \(g_*^{-1}\), and the fixed smooth function \(a\). The new Yang solution has the same recursively determined time jets at its initial time. Hence the concatenated metric is smooth across \(T_*\).

Thus the combined normalized Yang–Wang package establishes smooth continuation from the terminal-slab hypothesis alone.