# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/notes/step32_preceptor_analytic_review.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step31_m2_continuation_analysis.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Check the continuation subproblem at the lowest two derivative levels for the shifted variable U=a(Rm+G), a=chi^2. Starting from the equations and high-term expansions in the supplied files, determine whether one can rigorously obtain datum-dependent finite-time Lp control of the coupled base pair (nabla U, Hess chi), then (nabla^2 U, nabla^3 chi), including the residual integral int chi |Hess chi| |nabla^2 U|^p. Track connection evolution, norm/measure variation, required unweighted T moments, Sobolev factors, and derivative counts. If the proposed Gronwall closure fails, identify the precise first uncontrolled term; if it can close, give a term-level lemma with explicit assumptions. Do not appeal to initial smoothness alone or coefficient regularization a+epsilon.

## Output

# Scientific verification memo: the \(m=1,2\) continuation levels

## 1. Conclusion

For the shifted variable
\[
T=\operatorname{Rm}+G,\qquad U=aT,\qquad a=\chi^2,
\]
the first two coupled derivative levels do close on every finite interval on which
\[
\sup_{M\times[0,T_0)}|U|\le K.
\]

More precisely, in dimension four one obtains uniform, datum-dependent bounds for
\[
(\nabla U,\nabla^2\chi),\qquad
\nabla T,\qquad
(\nabla^2U,\nabla^3\chi)
\]
in finite \(L^p\) spaces. The integral
\[
\int_M\chi|\nabla^2\chi|\,|\nabla^2U|^p\,d\mu
\]
does not require \(\|\nabla^2\chi\|_\infty\). It is bounded by one Sobolev factor, the already established \(L^4\) norm of \(\nabla^2\chi\), a small multiple of weighted dissipation, and the unweighted \(L^p\) norm of \(\nabla^2U\).

The derivative order is genuinely triangular:
\[
(T)\longrightarrow (\nabla U,\nabla^2\chi)
\longrightarrow \nabla T
\longrightarrow(\nabla^2U,\nabla^3\chi).
\]
No \(\nabla^3\chi\) input is needed for the first pair or for \(\nabla T\), and no \(\nabla^4\chi\) input is needed for the second pair.

---

## 2. Precise assumptions and notation

Let \(M^4\) be closed and let \(g(t)\), \(0\le t<T_0<\infty\), be a smooth solution of
\[
\partial_tg=-2a(\operatorname{Ric}+g)=-2V,
\qquad
V=\operatorname{Ric}(U),\qquad a=\chi^2,
\]
where \(0\le\chi\le1\) is fixed as a scalar function. Write
\[
W_j=\nabla^jU,\qquad C_j=\nabla^j\chi.
\]

Fix \(p\ge4\). It is enough to enter the argument with the explicit initial quantities
\[
\begin{aligned}
&\|T(0)\|_{4p},\\
&\|W_1(0)\|_{4p},\quad \|C_2(0)\|_{4p},\\
&\|\nabla T(0)\|_{2p},\\
&\|W_2(0)\|_p,\quad \|C_3(0)\|_p
\end{aligned}
\tag{2.1}
\]
finite, together with an initial Sobolev constant and \(\|d\chi\|_{\infty,g(0)}\). Thus the proof uses named initial norms rather than smoothness as an unexplained substitute.

For \(j=1,2\), set
\[
X_{j,q}=\int_M|W_j|^q\,d\mu_t,
\qquad
D_{j,q}=\int_M\chi^2|\nabla W_j|^2|W_j|^{q-2}\,d\mu_t.
\tag{2.2}
\]

---

## 3. Moving geometry and connection terms

Since \(V=\operatorname{Ric}(U)\),
\[
|V|\le c_4|U|\le c_4K.
\]
Consequently,
\[
e^{-cKt}g(0)\le g(t)\le e^{cKt}g(0),
\tag{3.1}
\]
and the volume forms, finite \(L^q\) norms, and Sobolev constants remain uniformly comparable for \(t<T_0\). In particular, for some datum-dependent \(\mathcal S_*\) and fixed \(r>0\),
\[
\|f\|_4^2
\le \mathcal S_*
\left(\|\nabla f\|_2^2+r^{-2}\|f\|_2^2\right).
\tag{3.2}
\]
Also
\[
L:=\sup_{t<T_0}\|d\chi\|_{\infty,g(t)}<\infty.
\tag{3.3}
\]

The exact connection variation is
\[
P^k{}_{ij}:=\partial_t\Gamma^k{}_{ij}
=-g^{k\ell}
\bigl(\nabla_iV_{j\ell}+\nabla_jV_{i\ell}-\nabla_\ell V_{ij}\bigr).
\tag{3.4}
\]
Because \(\nabla V=\operatorname{Ric}(\nabla U)\),
\[
|P|\le C|W_1|,
\qquad
|\nabla P|\le C|W_2|.
\tag{3.5}
\]

For the fixed scalar \(\chi\),
\[
\partial_t C_2=-P*C_1,
\tag{3.6}
\]
and
\[
\partial_t C_3=-(\nabla P)*C_1-P*C_2.
\tag{3.7}
\]
Thus
\[
|\partial_tC_2|\le CL|W_1|,
\qquad
|\partial_tC_3|\le C\bigl(L|W_2|+|W_1||C_2|\bigr).
\tag{3.8}
\]

For every time-dependent covariant tensor \(Z\), the variation of its norm and the measure contributes at most
\[
C K\int |Z|^q\,d\mu_t,
\tag{3.9}
\]
because
\[
\partial_t d\mu=-(\operatorname{tr}V)d\mu,
\qquad
\partial_tg^{-1}=2V^\sharp.
\]
These contributions are zeroth-order terms in all energy estimates below.

---

## 4. Required unweighted \(T\)-moments

The supplied shifted equation is
\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T).
\tag{4.1}
\]
Testing against \(|T|^{q-2}T\), integrating the Hessian of \(a\) once, and using
\[
\frac{|da|^2}{a}=4|d\chi|^2
\tag{4.2}
\]
gives
\[
\frac d{dt}\int|T|^q
+c_q\int a|\nabla T|^2|T|^{q-2}
\le C_q(K+1+L^2)\int|T|^q.
\tag{4.3}
\]
Indeed, the quadratic term satisfies
\[
a|T|^{q+1}=|aT|\,|T|^q=|U|\,|T|^q\le K|T|^q.
\]
Hence
\[
\sup_{t<T_0}\|T(t)\|_q<\infty
\tag{4.4}
\]
for every exponent whose initial norm is included. In particular, \(q=4p\) suffices for the two levels considered here.

---

## 5. First coupled pair \((W_1,C_2)\)

### 5.1 High derivative terms in the \(W_1\)-equation

At \(m=1\), the high-cutoff part of the supplied differentiated \(U\)-equation consists schematically of
\[
\chi C_3*U,\quad
C_1*C_2*U,\quad
\chi C_2*W_1,\quad
C_1*C_1*W_1,\quad
\chi C_1*W_2.
\tag{5.1}
\]

Let \(P_q(W_1)=|W_1|^{q-2}W_1\).

The last term in (5.1) is absorbed directly:
\[
\left|\int P_q(W_1)*\chi C_1*W_2\right|
\le \varepsilon D_{1,q}
+C_{\varepsilon,q}L^2X_{1,q}.
\tag{5.2}
\]

For \(\chi C_3*U\), one integration by parts gives descendants bounded by
\[
\begin{aligned}
&\varepsilon D_{1,q}
+C_{\varepsilon,q}K^2
 \int |C_2|^2|W_1|^{q-2},\\
&CKL\int |C_2||W_1|^{q-1},\\
&\left|\int P_q(W_1)*\chi C_2*W_1\right|.
\end{aligned}
\tag{5.3}
\]
The first two expressions satisfy
\[
\int |C_2|^2|W_1|^{q-2}
\le \|C_2\|_q^2\|W_1\|_q^{q-2},
\tag{5.4}
\]
and
\[
\int |C_2||W_1|^{q-1}
\le \|C_2\|_q\|W_1\|_q^{q-1}.
\tag{5.5}
\]
Young’s inequality converts these into a multiple of
\[
\|C_2\|_q^q+\|W_1\|_q^q.
\]

The remaining Hessian expression is treated while preserving its tensor contraction. Since \(C_2=\nabla C_1\),
\[
\left|\int P_q(W_1)*\chi C_2*W_1\right|
\le \varepsilon D_{1,q}
+C_{\varepsilon,q}L^2X_{1,q}.
\tag{5.6}
\]
Here the derivative moved from \(C_2\) either hits \(W_1\), producing the weighted factor \(\chi\nabla W_1\), or hits \(\chi\), producing \(C_1*C_1\).

The remaining \(m=1\) terms are:

- \(U*W_1\), including connection variation: bounded by \(KX_{1,q}\);
- \(aW_1*T=U*W_1\): again bounded by \(KX_{1,q}\);
- \(da*U*T\): bounded using \(\|T\|_q\);
- derivatives of \(aG*U\): bounded by \(C(1+K)\), \(C_1\), \(C_2\), and \(W_1\).

Therefore
\[
X_{1,q}'+cD_{1,q}
\le C_q\bigl(1+\|T\|_q^q+X_{1,q}+\|C_2\|_q^q\bigr).
\tag{5.7}
\]

### 5.2 The \(C_2\)-equation

Equations (3.6), (3.9), and Hölder give
\[
\frac d{dt}\int|C_2|^q
\le CK\int|C_2|^q
+C_qL\int |W_1||C_2|^{q-1},
\tag{5.8}
\]
and hence
\[
\frac d{dt}\|C_2\|_q^q
\le C_q\bigl(1+X_{1,q}+\|C_2\|_q^q\bigr).
\tag{5.9}
\]

Combining (5.7) and (5.9),
\[
\frac d{dt}\left(X_{1,q}+\|C_2\|_q^q\right)
+cD_{1,q}
\le C_q\left(1+\|T\|_q^q+X_{1,q}+\|C_2\|_q^q\right).
\tag{5.10}
\]
Using (4.4) and Gronwall,
\[
\sup_{t<T_0}
\left(\|W_1(t)\|_q+\|C_2(t)\|_q\right)<\infty,
\qquad
\int_0^{T_0}D_{1,q}\,dt<\infty.
\tag{5.11}
\]
This may be run at \(q=4p\).

---

## 6. The intervening unweighted estimate for \(\nabla T\)

The \(W_2\)-equation contains \(\nabla T\), so this stage is required before the second pair.

Differentiating (4.1), the highest cutoff term is
\[
\chi C_3*T.
\tag{6.1}
\]
After one integration by parts, it produces
\[
\begin{aligned}
&\varepsilon D^T_{1,q}
+C_{\varepsilon,q}
 \int |C_2|^2|T|^2|\nabla T|^{q-2},\\
&C\int |C_2||T||\nabla T|^{q-1},\\
&\int P_q(\nabla T)*\chi C_2*\nabla T.
\end{aligned}
\tag{6.2}
\]
The last tensor expression is integrated once more through \(C_2=\nabla C_1\), giving
\[
\varepsilon D^T_{1,q}+C_{\varepsilon,q}L^2\|\nabla T\|_q^q.
\tag{6.3}
\]

The first expression in (6.2) satisfies
\[
\int |C_2|^2|T|^2|\nabla T|^{q-2}
\le
\|C_2\|_{2q}^2\|T\|_{2q}^2
\|\nabla T\|_q^{q-2}.
\tag{6.4}
\]
Other differentiated terms contain \(W_1*T\), \(C_1*T*T\), or bounded multiples of \(\nabla T\). They require
\[
W_1,C_2,T\in L^{2q}.
\]
Taking \(q=2p\), these are supplied by the first pair and the \(T\)-estimate at exponent \(4p\). Thus
\[
\frac d{dt}\|\nabla T\|_{2p}^{2p}
+cD^T_{1,2p}
\le C\left(1+\|\nabla T\|_{2p}^{2p}\right),
\tag{6.5}
\]
so
\[
\sup_{t<T_0}\|\nabla T(t)\|_{2p}<\infty.
\tag{6.6}
\]
No \(C_3\) estimate is used here.

---

## 7. Second coupled pair \((W_2,C_3)\)

### 7.1 Term structure in the \(W_2\)-equation

The connection contribution is
\[
(\nabla P)*U+P*W_1
=W_2*U+W_1*W_1.
\tag{7.1}
\]
The first term is a bounded potential; the second is controlled by
\(\|W_1\|_{2p}^2\).

The high-cutoff terms are
\[
\begin{aligned}
&\chi C_4*U,\qquad C_1*C_3*U,\qquad
\chi C_3*W_1,\qquad \chi C_1*W_3,\\
&C_2*C_2*U,\qquad
C_1*C_2*W_1,\qquad
\chi C_2*W_2,\qquad
C_1*C_1*W_2.
\end{aligned}
\tag{7.2}
\]

Integrating \(\chi C_4*U\) once gives the current-pair terms
\[
\varepsilon D_{2,p}
+C_{\varepsilon,p}K^2
 \int |C_3|^2|W_2|^{p-2}
+CKL\int |C_3||W_2|^{p-1},
\tag{7.3}
\]
together with a term containing \(\chi C_3*W_1\). Integrating the latter through \(C_3=\nabla C_2\) gives

- a dissipative term with coefficient \(C_2W_1\);
- terms involving \(C_1C_2W_1\);
- the residual expression with \(\chi C_2W_2\).

The dissipative descendant is bounded by
\[
\varepsilon D_{2,p}
+C_{\varepsilon,p}
\int |C_2|^2|W_1|^2|W_2|^{p-2}.
\tag{7.4}
\]
Using \(C_2,W_1\in L^{2p}\),
\[
\int |C_2|^2|W_1|^2|W_2|^{p-2}
\le
\|C_2\|_{2p}^2\|W_1\|_{2p}^2\|W_2\|_p^{p-2}.
\tag{7.5}
\]

The lower \(T\)-terms at \(m=2\) are combinations of
\[
\begin{gathered}
C_2*U*T,\quad C_1*W_1*T,\quad
C_1*U*\nabla T,\quad
aW_1*\nabla T,\\
aW_2*T=U*W_2.
\end{gathered}
\tag{7.6}
\]
They are controlled by
\[
T,\nabla T,W_1,C_2\in L^{2p}
\tag{7.7}
\]
and the bound on \(U\).

### 7.2 The residual integral

Set
\[
W=W_2,\qquad B=C_2,\qquad
X=\int|W|^p,\qquad
D=\int\chi^2|\nabla W|^2|W|^{p-2}.
\]
For
\[
I=\int\chi|B||W|^p,
\tag{7.8}
\]
put
\[
u=\chi|W|^{p/2}.
\]
Then Hölder with exponents \((4,4,2)\) gives
\[
I\le \|B\|_4\|u\|_4X^{1/2}.
\tag{7.9}
\]
The gradient satisfies
\[
\|\nabla u\|_2^2
\le Cp^2D+CL^2X.
\tag{7.10}
\]
Using (3.2),
\[
\|u\|_4^2
\le
\mathcal S_*
\left(Cp^2D+C(L^2+r^{-2})X\right).
\tag{7.11}
\]
Consequently, for every \(\varepsilon>0\),
\[
\boxed{
I\le
\varepsilon D
+C_p\left[
\varepsilon^{-1}\mathcal S_*\|B\|_4^2
+\mathcal S_*^{1/2}(L+r^{-1})\|B\|_4
\right]X.}
\tag{7.12}
\]
The first pair at exponent \(4p\), together with volume comparability, gives
\[
\sup_{t<T_0}\|C_2(t)\|_4<\infty.
\tag{7.13}
\]
Thus the coefficient in (7.12) is uniformly finite. Only one power of the squared Sobolev coefficient \(\mathcal S_*\) appears in the quadratic term.

After applying Hölder and Young to (7.3)–(7.7), the \(W_2\)-energy has the form
\[
X_{2,p}'+cD_{2,p}
\le C\left(1+X_{2,p}+\|C_3\|_p^p\right).
\tag{7.14}
\]

### 7.3 The \(C_3\)-equation

From (3.7)–(3.8),
\[
\begin{aligned}
\frac d{dt}\|C_3\|_p^p
\le{}& CK\|C_3\|_p^p\\
&+C_pL\int |C_3|^{p-1}|W_2|\\
&+C_p\int |C_3|^{p-1}|W_1||C_2|.
\end{aligned}
\tag{7.15}
\]
Since
\[
\|W_1C_2\|_p
\le\|W_1\|_{2p}\|C_2\|_{2p},
\tag{7.16}
\]
Young’s inequality gives
\[
\frac d{dt}\|C_3\|_p^p
\le C\left(1+X_{2,p}+\|C_3\|_p^p\right).
\tag{7.17}
\]

Combining (7.14) and (7.17),
\[
\frac d{dt}
\left(X_{2,p}+\|C_3\|_p^p\right)
+cD_{2,p}
\le
C\left(1+X_{2,p}+\|C_3\|_p^p\right).
\tag{7.18}
\]
Therefore
\[
\boxed{
\sup_{t<T_0}
\left(\|\nabla^2U(t)\|_p+\|\nabla^3\chi(t)\|_p\right)<\infty,
\qquad
\int_0^{T_0}D_{2,p}\,dt<\infty.}
\tag{7.19}
\]

---

## 8. Term-level lemma

**Lemma.**  
Under the assumptions in Section 2, including \(\sup|U|\le K\) and the explicit initial norms (2.1), there is a finite constant
\[
C=C\!\left(
p,T_0,K,g(0),\chi,
\|T(0)\|_{4p},
\|W_1(0)\|_{4p},
\|C_2(0)\|_{4p},
\|\nabla T(0)\|_{2p},
\|W_2(0)\|_p,
\|C_3(0)\|_p
\right)
\]
such that
\[
\sup_{t<T_0}
\left[
\|\nabla U\|_{4p}
+\|\nabla^2\chi\|_{4p}
+\|\nabla T\|_{2p}
+\|\nabla^2U\|_p
+\|\nabla^3\chi\|_p
\right]\le C.
\tag{8.1}
\]
The corresponding weighted dissipations for \(\nabla U\), \(\nabla T\), and \(\nabla^2U\) are integrable in time.

The direct estimate
\[
I\le\|\nabla^2\chi\|_\infty\|\nabla^2U\|_p^p
\]
would stop because no pointwise Hessian estimate has yet been produced. Formula (7.12) is the needed replacement. With it, there is no uncontrolled term at either of these two levels.

At tensor zero sets one may use
\[
(|Z|^2+\eta^2)^{p/2}
\]
and pass to \(\eta\downarrow0\). The flow coefficient remains exactly \(a=\chi^2\) throughout.