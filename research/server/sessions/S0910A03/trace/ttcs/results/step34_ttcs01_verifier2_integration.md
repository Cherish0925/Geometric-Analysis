# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step34_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step34_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the continuation subproblem at the lowest two derivative levels for the shifted variable U=a(Rm+G), a=chi^2. Starting from the equations and high-term expansions in the supplied files, determine whether one can rigorously obtain datum-dependent finite-time Lp control of the coupled base pair (nabla U, Hess chi), then (nabla^2 U, nabla^3 chi), including the residual integral int chi |Hess chi| |nabla^2 U|^p. Track connection evolution, norm/measure variation, required unweighted T moments, Sobolev factors, and derivative counts. If the proposed Gronwall closure fails, identify the precise first uncontrolled term; if it can close, give a term-level lemma with explicit assumptions. Do not appeal to initial smoothness alone or coefficient regularization a+epsilon.

## Integrated Scientific Memo

## Verification result: the lowest two shifted-continuation derivative levels can close, but only in the coupled \(L^p\) formulation, not by pointwise cutoff-Hessian control

Work with the normalized fixed-cutoff flow
\[
\partial_t g=-2a(\operatorname{Ric}+g),\qquad a=\chi^2,
\]
and the shifted variables
\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\operatorname{Rm}+G,\qquad U=aT,\qquad V=aE=\operatorname{Ric}(U).
\]
The continuation hypothesis relevant here is the terminal one
\[
\sup_{M\times[0,T_0)} |U|_g\le K<\infty
\tag{H0}
\]
on a finite interval. Under (H0), the metric, measure, finite \(L^q\) norms, and Sobolev constants remain mutually comparable on \([0,T_0)\), because
\[
\partial_t g=-2V,\qquad |V|\le C_n|U|\le C_nK.
\]
Thus
\[
e^{-CKt}g(0)\le g(t)\le e^{CKt}g(0),
\]
and for some datum-dependent Sobolev constant \(\mathcal S_*\),
\[
\|f\|_{4}^{2}\le \mathcal S_*\bigl(\|\nabla f\|_2^2+r^{-2}\|f\|_2^2\bigr)
\tag{S}
\]
in dimension four. Norm and measure variation contributes only zeroth-order terms:
\[
\partial_t d\mu=-(\operatorname{tr}V)d\mu,\qquad \partial_t g^{-1}=2V^\sharp,
\]
so every \(L^p\) tensor energy receives at most \(CK\int |Z|^p\).

The conclusion is:

* the base pair \((\nabla U,\nabla^2\chi)\) admits datum-dependent finite-time \(L^p\) control;
* after that, the required unweighted moment \(\nabla T\) admits finite-time \(L^p\) control;
* then the next pair \((\nabla^2U,\nabla^3\chi)\) admits datum-dependent finite-time \(L^p\) control;
* the residual term
  \[
  I=\int_M \chi|\nabla^2\chi|\,|\nabla^2U|^p\,d\mu_t
  \tag{R}
  \]
  is controlled by the already obtained finite \(L^4\) bound for \(\nabla^2\chi\), the moving Sobolev inequality, and the weighted dissipation. No coefficient regularization \(a\mapsto a+\varepsilon\) is needed or allowed.

This corrects the incomplete/incorrect shortcut in A01 Step 31: bounding \(I\) by \(\|\nabla^2\chi\|_\infty\|\nabla^2U\|_p^p\) is not legitimate at the base of the coupled induction, because pointwise control of the evolving Hessian of the fixed scalar \(\chi\) is precisely one of the quantities being produced. Branch 1’s replacement by the \(L^4\)-Sobolev estimate agrees with Step 32/34 and is the valid route.

---

## 1. Equations and connection evolution used

The supplied shifted equation is
\[
(\partial_t-a\Delta)U
=da*\nabla U+\nabla^2a*U+d\chi*d\chi*U+U*U+aG*U.
\tag{1.1}
\]
Equivalently, after differentiating, the highest cutoff/weighted-curvature terms at order \(m\) include
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,\qquad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\]
\[
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,\qquad
\Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.
\tag{1.2}
\]
The exact point emphasized in the source files is that \(\Gamma_1\) really occurs; it is removed by integration by parts, not by pretending cutoff derivatives stop one order lower.

Since
\[
\partial_tg=-2\operatorname{Ric}(U),
\]
the connection variation is schematically
\[
\partial_t\Gamma=g^{-1}*\nabla \operatorname{Ric}(U)=\nabla U.
\tag{1.3}
\]
More precisely,
\[
\partial_t\Gamma^k{}_{ij}
=-g^{k\ell}\bigl(\nabla_iV_{j\ell}+\nabla_jV_{i\ell}-\nabla_\ell V_{ij}\bigr),
\qquad V=\operatorname{Ric}(U).
\tag{1.4}
\]
Therefore
\[
|\partial_t\Gamma|\le C|\nabla U|,\qquad
|\nabla\partial_t\Gamma|\le C|\nabla^2U|+C|\operatorname{Rm}|\,|\nabla U|,
\tag{1.5}
\]
with the curvature-commutator part handled through the already available finite unweighted \(T\)-moments. For the fixed scalar \(\chi\),
\[
\partial_t\nabla^2\chi=-(\partial_t\Gamma)*\nabla\chi,
\tag{1.6}
\]
and
\[
\partial_t\nabla^3\chi
=-(\nabla\partial_t\Gamma)*\nabla\chi
-(\partial_t\Gamma)*\nabla^2\chi.
\tag{1.7}
\]
Thus the derivative count is exactly:
\[
(\nabla U,\nabla^2\chi)
\quad\text{first, then}\quad
(\nabla^2U,\nabla^3\chi).
\]

---

## 2. Required unweighted \(T\)-moments

The \(T\)-equation is
\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T).
\tag{2.1}
\]
Testing against \(|T|^{q-2}T\), integrating the Hessian-\(a\) term once, and using
\[
\frac{|da|^2}{a}=4|d\chi|^2
\tag{2.2}
\]
gives
\[
\frac{d}{dt}\int |T|^q
+c_q\int a|\nabla T|^2|T|^{q-2}
\le C_q(K+1+\|\nabla\chi\|_\infty^2)\int |T|^q.
\tag{2.3}
\]
The quadratic reaction is harmless because
\[
a|T|^{q+1}=|aT|\,|T|^q=|U|\,|T|^q\le K|T|^q.
\]
Hence, for every finite \(q\) whose initial value is included,
\[
\sup_{t<T_0}\|T(t)\|_{L^q}<\infty.
\tag{2.4}
\]
For the first two derivative levels it is enough to keep \(T\) in exponents such as \(4p\) and \(\nabla T\) in \(2p\), depending on the Hölder allocation below.

After the base pair is controlled, differentiating (2.1) once and testing against \(|\nabla T|^{q-2}\nabla T\) gives
\[
\frac{d}{dt}\|\nabla T\|_q^q
+cD^T_{1,q}
\le C\bigl(1+\|\nabla T\|_q^q\bigr),
\tag{2.5}
\]
provided \(T,\nabla U,\nabla^2\chi\) are available in sufficiently high finite exponents. The potentially highest term \(\chi\nabla^3\chi*T\) is integrated by parts once; the resulting coefficients involve only \(\nabla^2\chi,T,\nabla T\) and weighted dissipation. Thus \(\nabla T\) is controlled before the \((\nabla^2U,\nabla^3\chi)\) pair.

---

## 3. First coupled base pair \((W_1,C_2)=(\nabla U,\nabla^2\chi)\)

Let
\[
W_1=\nabla U,\qquad C_2=\nabla^2\chi,
\]
\[
X_{1,q}=\int |W_1|^q,\qquad
D_{1,q}=\int \chi^2|\nabla W_1|^2|W_1|^{q-2}.
\]

At \(m=1\), the dangerous differentiated cutoff terms are schematically
\[
\chi\nabla^3\chi*U,\quad
\nabla\chi*\nabla^2\chi*U,\quad
\chi\nabla^2\chi*\nabla U,\quad
\chi\nabla\chi*\nabla^2U.
\tag{3.1}
\]
The last term is absorbed:
\[
\left|\int |W_1|^{q-2}W_1*(\chi\nabla\chi*\nabla W_1)\right|
\le \varepsilon D_{1,q}+C_{\varepsilon,q}\|\nabla\chi\|_\infty^2X_{1,q}.
\tag{3.2}
\]
The \(\chi\nabla^3\chi*U\) term is integrated by parts once. Its descendants are bounded by
\[
\varepsilon D_{1,q}
+C_{\varepsilon,q}K^2\int |C_2|^2|W_1|^{q-2}
+CK\|\nabla\chi\|_\infty\int |C_2||W_1|^{q-1},
\tag{3.3}
\]
plus terms of the same or lower type. Hölder gives
\[
\int |C_2|^2|W_1|^{q-2}
\le \|C_2\|_q^2\|W_1\|_q^{q-2},
\tag{3.4}
\]
\[
\int |C_2||W_1|^{q-1}
\le \|C_2\|_q\|W_1\|_q^{q-1},
\tag{3.5}
\]
and Young converts these to \(C(\|C_2\|_q^q+\|W_1\|_q^q)\).

The connection, norm, measure, \(U*U\), and \(aG*U\) differentiated terms add only controlled lower-order quantities involving \(K\), \(T\), and \(W_1\). Hence
\[
X_{1,q}'+cD_{1,q}
\le C_q\bigl(1+\|T\|_q^q+X_{1,q}+\|C_2\|_q^q\bigr).
\tag{3.6}
\]

For the cutoff tensor, (1.6) gives
\[
\frac{d}{dt}\|C_2\|_q^q
\le C_q\bigl(1+X_{1,q}+\|C_2\|_q^q\bigr),
\tag{3.7}
\]
including moving norm/measure variation.

Combining (3.6), (3.7), and (2.4),
\[
\frac{d}{dt}\bigl(X_{1,q}+\|C_2\|_q^q\bigr)+cD_{1,q}
\le C_q\bigl(1+X_{1,q}+\|C_2\|_q^q\bigr),
\tag{3.8}
\]
so Gronwall yields
\[
\sup_{t<T_0}\bigl(\|\nabla U(t)\|_{L^q}+\|\nabla^2\chi(t)\|_{L^q}\bigr)<\infty,
\qquad
\int_0^{T_0}D_{1,q}\,dt<\infty.
\tag{3.9}
\]
This is the first closed datum-dependent base pair. To feed the second level, run it at least at \(q=4p\) or sufficiently large finite exponents.

---

## 4. Second coupled pair \((W_2,C_3)=(\nabla^2U,\nabla^3\chi)\)

Let
\[
W_2=\nabla^2U,\qquad C_3=\nabla^3\chi,
\]
\[
X_{2,p}=\int |W_2|^p,\qquad
D_{2,p}=\int \chi^2|\nabla W_2|^2|W_2|^{p-2}.
\]

At \(m=2\), the highest raw cutoff terms include
\[
\chi\nabla^4\chi*U,\quad
\nabla\chi*\nabla^3\chi*U,\quad
\chi\nabla^3\chi*\nabla U,\quad
\chi\nabla\chi*\nabla^3U,
\tag{4.1}
\]
and lower allocations such as
\[
\nabla^2\chi*\nabla^2\chi*U,\qquad
\nabla\chi*\nabla^2\chi*\nabla U,\qquad
\chi\nabla^2\chi*\nabla^2U.
\tag{4.2}
\]
The \(\chi\nabla\chi*\nabla^3U\) term is absorbed by \(D_{2,p}\). The \(\chi\nabla^4\chi*U\) term is integrated by parts once and yields current-pair terms
\[
\varepsilon D_{2,p}
+C_{\varepsilon,p}K^2\int |C_3|^2|W_2|^{p-2}
+CK\|\nabla\chi\|_\infty\int |C_3||W_2|^{p-1},
\tag{4.3}
\]
which are controlled by \(\|C_3\|_p^p+X_{2,p}\) after Hölder and Young.

Terms involving previous levels, for example
\[
|C_2|^2|W_1|^2|W_2|^{p-2},
\qquad
|W_1|^2|W_2|^{p-1},
\qquad
|C_2||W_1||W_2|^{p-1},
\tag{4.4}
\]
are controlled using the first pair in sufficiently high finite exponents, e.g.
\[
C_2,W_1\in L^{2p}\quad\text{or higher}.
\]
Terms involving \(T\) and \(\nabla T\), such as
\[
C_2*U*T,\quad C_1*W_1*T,\quad C_1*U*\nabla T,\quad aW_1*\nabla T,\quad U*W_2,
\tag{4.5}
\]
are controlled using (2.4), (2.5), and \(|U|\le K\).

The only delicate residual is exactly
\[
I=\int \chi|C_2|\,|W_2|^p.
\tag{4.6}
\]
It is not directly absorbable into \(D_{2,p}\), because naive Young would introduce a negative power of \(\chi\). It is also not legitimate at this point to estimate it by \(\|C_2\|_\infty X_{2,p}\), since \(\|C_2\|_\infty\) has not yet been produced.

Instead set
\[
u=\chi |W_2|^{p/2}.
\]
Then
\[
I=\int |C_2|\,u\,|W_2|^{p/2}
\le \|C_2\|_4\|u\|_4X_{2,p}^{1/2}.
\tag{4.7}
\]
Moreover
\[
\|\nabla u\|_2^2
\le C p^2D_{2,p}+C\|\nabla\chi\|_\infty^2X_{2,p}.
\tag{4.8}
\]
By the moving Sobolev inequality (S),
\[
\|u\|_4^2
\le C\mathcal S_*\bigl(p^2D_{2,p}+(\|\nabla\chi\|_\infty^2+r^{-2})X_{2,p}\bigr).
\tag{4.9}
\]
Consequently, for every \(\varepsilon>0\),
\[
\boxed{
I\le \varepsilon D_{2,p}
+C_{\varepsilon,p}\mathcal S_*\|C_2\|_4^2
(1+\|\nabla\chi\|_\infty^2+r^{-2})X_{2,p}.
}
\tag{4.10}
\]
A slightly sharper two-term version keeps the square-root lower-order contribution, but (4.10) is sufficient. The first pair, run at exponent \(4\) or higher, gives
\[
\sup_{t<T_0}\|C_2(t)\|_4<\infty.
\tag{4.11}
\]
Thus (4.10) has a finite datum-dependent coefficient.

Therefore the \(W_2\)-energy closes as
\[
X_{2,p}'+cD_{2,p}
\le C_p\bigl(1+X_{2,p}+\|C_3\|_p^p\bigr).
\tag{4.12}
\]

For \(C_3\), using (1.7),
\[
|\partial_t C_3|
\le C\bigl(|W_2||\nabla\chi|+|W_1||C_2|+\text{commutator terms controlled by }T,W_1\bigr).
\]
Thus
\[
\frac{d}{dt}\|C_3\|_p^p
\le C_p\left(
\|C_3\|_p^p
+\int |C_3|^{p-1}|W_2|
+\int |C_3|^{p-1}|W_1||C_2|
+1
\right).
\tag{4.13}
\]
Since
\[
\|W_1C_2\|_p\le \|W_1\|_{2p}\|C_2\|_{2p},
\tag{4.14}
\]
Young gives
\[
\frac{d}{dt}\|C_3\|_p^p
\le C_p\bigl(1+X_{2,p}+\|C_3\|_p^p\bigr).
\tag{4.15}
\]
Combining (4.12) and (4.15),
\[
\frac{d}{dt}\bigl(X_{2,p}+\|C_3\|_p^p\bigr)+cD_{2,p}
\le C_p\bigl(1+X_{2,p}+\|C_3\|_p^p\bigr),
\tag{4.16}
\]
and Gronwall yields
\[
\sup_{t<T_0}\bigl(
\|\nabla^2U(t)\|_{L^p}
+\|\nabla^3\chi(t)\|_{L^p}
\bigr)<\infty,
\qquad
\int_0^{T_0}D_{2,p}\,dt<\infty.
\tag{4.17}
\]

---

## 5. Term-level continuation lemma

In dimension four, fix \(p\ge4\). Assume:

1. \(g(t)\) is a smooth solution on \([0,T_0)\), \(T_0<\infty\);
2. \(a=\chi^2\), with \(\chi\) fixed as a scalar function;
3. \(\sup_{M\times[0,T_0)}|U|\le K\);
4. the initial norms needed in the finite Hölder schedule are finite, for example
   \[
   \|T(0)\|_{4p},\quad
   \|\nabla U(0)\|_{4p},\quad
   \|\nabla^2\chi(0)\|_{4p},\quad
   \|\nabla T(0)\|_{2p},\quad
   \|\nabla^2U(0)\|_p,\quad
   \|\nabla^3\chi(0)\|_p;
   \]
5. the initial Sobolev constant and \(\|\nabla\chi\|_{\infty,g(0)}\) are finite.

Then there is a finite constant \(C\), depending on these data, \(p,T_0,K\), and the initial metric/cutoff, such that
\[
\sup_{t<T_0}\left[
\|\nabla U\|_{4p}
+\|\nabla^2\chi\|_{4p}
+\|\nabla T\|_{2p}
+\|\nabla^2U\|_p
+\|\nabla^3\chi\|_p
\right]\le C.
\tag{5.1}
\]
Moreover the corresponding weighted dissipations
\[
\int_0^{T_0}\int \chi^2|\nabla^2U|^2|\nabla U|^{4p-2},
\quad
\int_0^{T_0}\int \chi^2|\nabla^2T|^2|\nabla T|^{2p-2},
\quad
\int_0^{T_0}\int \chi^2|\nabla^3U|^2|\nabla^2U|^{p-2}
\]
are finite, with the evident exponent adjustments.

The key residual estimate is exactly
\[
\int \chi|\nabla^2\chi|\,|\nabla^2U|^p
\le
\varepsilon\int\chi^2|\nabla^3U|^2|\nabla^2U|^{p-2}
+C_{\varepsilon,p}\mathcal S_*
\|\nabla^2\chi\|_4^2
(1+\|\nabla\chi\|_\infty^2+r^{-2})
\int|\nabla^2U|^p.
\tag{5.2}
\]
This is the precise repair needed for the single-\(\chi\) term.

---

## 6. What would fail without the coupled base pair

The first uncontrolled term in the naive Gronwall closure is not \(\chi\nabla^4\chi*U\); that term can be integrated by parts. The first genuinely uncontrolled term, if one does not first produce \(\nabla^2\chi\in L^4\), is
\[
\boxed{
\int \chi|\nabla^2\chi|\,|\nabla^2U|^p.
}
\]
It cannot be absorbed directly into
\[
D_{2,p}=\int\chi^2|\nabla^3U|^2|\nabla^2U|^{p-2}
\]
without negative powers of \(\chi\), and it cannot be bounded by \(\|\nabla^2\chi\|_\infty\int|\nabla^2U|^p\) at this stage. Once the first coupled pair gives finite evolving \(L^4\) control of \(\nabla^2\chi\), (5.2) closes it.

Coefficient regularization \(a\mapsto a+\varepsilon\) remains invalid for this purpose: it changes the exterior stationary region, destroys the exact identity \(|da|^2/a=4|d\chi|^2\), and would require exterior-independent curvature estimates not supplied here. Kato regularization of tensor norms is harmless; coefficient regularization is not.