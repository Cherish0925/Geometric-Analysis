# TTCS Independent Branch Record

```json
{
  "step_id": 56,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md"
  ]
}
```

## Task

Attack the earliest positive-time continuation interface for the exact cutoff flow, not the start theorem. On a fixed smooth terminal slab [tau,T*) assume sup|U|<K, metric bilipschitz equivalence, fixed smooth chi, and finite initial norms at tau, where T=Rm+g∧g/(2(n−1)), U=chi^2 T. Verify in detail the m=1 coupled pair (U_1=∇U,C_2=∇²chi), then the unweighted T_1=∇T estimate. List every highest-order term, especially chi C_3 U, chi C_2 U_1, dchi C_2 U, ∇³a T, and connection variation; perform the needed signed integrations by parts and state exact L^p inequalities. Determine whether any estimate divides by chi, needs unweighted pointwise T, introduces a ratio of regularization parameters, or fails near the small-chi collar. Ground the answer in the attached Step 40/44/45 notes and correct them if needed.

## Output

# Scientific memo: the \(m=1\) positive-time continuation module

## 1. Setting and zero-order input

Let
\[
a=\chi^2,\qquad
T=\operatorname{Rm}+G,\qquad
G=\frac{g\owedge g}{2(n-1)},\qquad
U=aT,
\]
and
\[
\partial_tg=-2S,\qquad S=\operatorname{Ric}(U)=a(\operatorname{Ric}+g).
\]
Work on a fixed slab \([\tau,T_*)\), with
\[
\|U\|_{L^\infty(M\times[\tau,T_*))}\le K,
\]
uniform metric equivalence, and smooth data at \(t=\tau\). All norms below use \(g(t)\). Put
\[
C_j=\nabla^j\chi,\qquad B_j=\nabla^ja,\qquad
V=U_1=\nabla U,\qquad Z=C_2=\nabla^2\chi,\qquad X=T_1=\nabla T.
\]
Metric equivalence gives
\[
L:=\sup_{M\times[\tau,T_*)}|C_1|<\infty,
\qquad \sup_t\operatorname{Vol}_{g(t)}M<\infty.
\]

The identities needed repeatedly are
\[
B_1=2\chi C_1,\qquad
B_2=2\chi C_2+2C_1*C_1,
\]
\[
B_3=2\chi C_3+C_1*C_2,
\tag{1.1}
\]
where the last star denotes the finite sum over ordered slot allocations.

The Step 44 zero-order estimate is indispensable. Bounded \(U=aT\) alone does not algebraically imply an unweighted \(T\)-bound near \(\chi=0\). Instead, for every finite \(q\ge2\),
\[
\frac d{dt}\|T\|_q^q
+c_{n,q}\int_Ma|\nabla T|^2|T|^{q-2}
\le
C_{n,q,K,L}\bigl(\|T\|_q^q+\operatorname{Vol}_{g(t)}M\bigr).
\tag{1.2}
\]
The \(\nabla^2a*T\) contraction is integrated by parts while retaining its tensor sign; only \(da=2\chi\,d\chi\) remains. The quadratic reaction uses
\[
a|T|^{q+1}=|U|\,|T|^q\le K|T|^q.
\]
Thus
\[
M_q^T:=\sup_{\tau\le t<T_*}\|T(t)\|_q<\infty
\qquad\text{for every finite }q.
\tag{1.3}
\]

## 2. The signed Hessian identity

For either \(Y=V\) or \(Y=X\), every current Hessian contraction occurring below has the form
\[
\mathsf H_p(Y)=\int_M\chi(C_2)_{ij}\,\mathcal B^{ij}(Y)\,d\mu,
\]
where
\[
|\mathcal B(Y)|\le C_{n,p}|Y|^p,\qquad
|\nabla\mathcal B(Y)|
\le C_{n,p}|Y|^{p-1}|\nabla Y|.
\]
Since \(M\) is closed,
\[
\mathsf H_p(Y)
=
-\int C_{1,i}C_{1,j}\mathcal B^{ij}(Y)
-\int\chi C_{1,j}\nabla_i\mathcal B^{ij}(Y).
\]
Consequently, for every \(\varepsilon>0\),
\[
\boxed{
|\mathsf H_p(Y)|
\le
\varepsilon\int a|\nabla Y|^2|Y|^{p-2}
+C_{n,p}\varepsilon^{-1}L^2\|Y\|_p^p.}
\tag{2.1}
\]
This estimate uses no \(L^\infty\)-bound for \(C_2\).

---

## 3. Complete \(m=1\) ledger for \(V=\nabla U\)

The division-free coordinate-time equation from Step 45 is
\[
\partial_tU
=
a\Delta U+B_1*U_1+B_2*U+(B_1*B_1)*T
+U*U+aU+a^2,
\tag{3.1}
\]
up to fixed contractions and lower normalization terms.

After applying one covariant derivative and adding the coordinate-time connection variation, all top allocations are:

\[
\begin{array}{c|l}
\text{source}&\text{\(m=1\) terms}\\ \hline
a\Delta U&a\Delta V,\quad B_1*U_2,\quad
a\operatorname{Rm}*V,\quad a\nabla\operatorname{Rm}*U\\
B_1*U_1&B_1*U_2,\quad B_2*V\\
B_2*U&B_3*U,\quad B_2*V\\
(B_1*B_1)*T&B_2*B_1*T,\quad B_1*B_2*T,\quad B_1*B_1*X\\
U*U&U*V\\
[\partial_t,\nabla]U&(\partial_t\Gamma)*U=V*U\\
aU+a^2&aV,\quad B_1*U,\quad aB_1.
\end{array}
\tag{3.2}
\]

Here
\[
(\partial_t\Gamma)^k{}_{ij}
=-g^{k\ell}\bigl(\nabla_iS_{j\ell}
+\nabla_jS_{i\ell}-\nabla_\ell S_{ij}\bigr),
\qquad |\partial_t\Gamma|\le C_n|V|.
\tag{3.3}
\]

### 3.1 Removal of the apparent \(T_1\) dependence

The three terms in the fourth row of (3.2) must be kept together. Since
\[
(B_1*B_1)*T=4(C_1*C_1)*U
\tag{3.4}
\]
for the exact coefficient \(a=\chi^2\),
\[
\nabla\bigl((B_1*B_1)*T\bigr)
=
C_1*C_2*U+C_1*C_1*V.
\tag{3.5}
\]
Thus the \(V\)-equation does not require \(T_1\) before the \(V,Z\) pair has been propagated. Estimating \(B_1*B_1*X\) separately would destroy the triangular order.

Likewise,
\[
a\nabla\operatorname{Rm}=a\nabla T=V-B_1*T,
\tag{3.6}
\]
so
\[
a\nabla\operatorname{Rm}*U
=
V*U-B_1*T*U.
\tag{3.7}
\]
The last term needs only the already propagated finite \(L^p\)-norm of \(T\).

### 3.2 Explicit highest cutoff terms

Using (1.1), the terms involving the largest cutoff jets are exactly
\[
B_1*U_2=2\chi C_1*\nabla V,
\tag{3.8}
\]
\[
B_2*V=2\chi C_2*V+2C_1*C_1*V,
\tag{3.9}
\]
\[
B_3*U=2\chi C_3*U+C_1*C_2*U,
\tag{3.10}
\]
together with the \(C_1*C_2*U\) term in (3.5). Thus the requested tensor types
\[
\chi C_3U,\qquad \chi C_2U_1,\qquad d\chi\,C_2U
\]
are all present, and there is no bare \(C_3U\).

### 3.3 Integration of \(\chi C_3U\)

Let
\[
P(V)=|V|^{p-2}V,\qquad
D_{V,p}=\int_Ma|\nabla V|^2|V|^{p-2}.
\]
For each ordered occurrence of \(C_3=\nabla C_2\),
\[
\begin{aligned}
I_U
&=\int_M P(V)*\chi C_3*U\\
&=-\int_M\nabla P(V)*\chi Z*U
-\int_M P(V)*C_1*Z*U
-\int_M P(V)*\chi Z*V.
\end{aligned}
\tag{3.11}
\]

The first term satisfies
\[
\begin{aligned}
\left|\int\nabla P(V)*\chi Z*U\right|
&\le
\varepsilon D_{V,p}
+C_{n,p}\varepsilon^{-1}K^2
 \int |Z|^2|V|^{p-2}\\
&\le
\varepsilon D_{V,p}
+C_{n,p,K,\varepsilon}
\bigl(\|Z\|_p^p+\|V\|_p^p\bigr),
\end{aligned}
\tag{3.12}
\]
using pointwise
\[
|Z|^2|V|^{p-2}
\le \frac2p|Z|^p+\frac{p-2}{p}|V|^p.
\tag{3.13}
\]

The second term obeys
\[
\left|\int P(V)*C_1*Z*U\right|
\le
C_{n,p}LK
\left(\frac1p\|Z\|_p^p+\frac{p-1}{p}\|V\|_p^p\right).
\tag{3.14}
\]

The last term in (3.11) is a signed Hessian contraction:
\[
\left|\int\chi Z*V*P(V)\right|
\le
\varepsilon D_{V,p}
+C_{n,p}\varepsilon^{-1}L^2\|V\|_p^p.
\tag{3.15}
\]

The direct \(\chi C_2*V\) terms in (3.9) satisfy the same estimate (3.15), while every \(C_1*C_2*U\) term satisfies (3.14).

Finally,
\[
\left|\int P(V)*B_1*\nabla V\right|
\le
\varepsilon D_{V,p}
+C_{n,p}\varepsilon^{-1}L^2\|V\|_p^p.
\tag{3.16}
\]

### 3.4 Remaining terms and the \(V\)-inequality

The current curvature coefficients are bounded:
\[
a\operatorname{Rm}=U-aG,\qquad |U|\le K.
\]
The term from (3.7) satisfies
\[
\int |B_1|\,|T|\,|U|\,|V|^{p-1}
\le C LK\,\|T\|_p\|V\|_p^{p-1}
\le C_{p,L,K}\bigl(\|T\|_p^p+\|V\|_p^p\bigr).
\tag{3.17}
\]
Connection, norm, and volume variations have bounded coefficient \(U\).

After choosing the finitely many \(\varepsilon\)'s small,
\[
\boxed{
\frac d{dt}\|V\|_p^p+c_{n,p}D_{V,p}
\le
C_{n,p,K,L}
\left(
1+\|T\|_p^p+\|V\|_p^p+\|Z\|_p^p
\right).}
\tag{3.18}
\]

---

## 4. Evolution of \(Z=C_2=\nabla^2\chi\)

Because \(\chi\) is fixed as a scalar,
\[
\partial_tC_1=0,\qquad
\partial_tC_2=-(\partial_t\Gamma)*C_1.
\tag{4.1}
\]
Using (3.3),
\[
|\partial_tZ|\le C_nL|V|.
\tag{4.2}
\]
There is no raw \(U*Z\) term. Such a term enters only through variation of the tensor norm and \(d\mu_g\), both controlled by \(|S|\le C_nK\). Hence
\[
\boxed{
\frac d{dt}\|Z\|_p^p
\le
C_{n,p,K,L}
\bigl(\|V\|_p^p+\|Z\|_p^p\bigr).}
\tag{4.3}
\]

Combining (3.18) and (4.3), with
\[
Y_p=\|V\|_p^p+\|Z\|_p^p,
\]
gives
\[
\boxed{
Y_p'+c_{n,p}D_{V,p}
\le
C_{n,p,K,L}
\bigl(1+\|T\|_p^p+Y_p\bigr).}
\tag{4.4}
\]
Using (1.3) and Grönwall,
\[
\sup_{\tau\le t<T_*}
\left(\|\nabla U(t)\|_p+\|\nabla^2\chi(t)\|_p\right)<\infty
\tag{4.5}
\]
for every finite \(p\).

---

## 5. Complete \(m=1\) ledger for \(X=\nabla T\)

From the Step 45 coordinate-time \(T\)-equation,
\[
\partial_tT
=
a\Delta T+B_1*T_1+B_2*T+a(T*T+T+1),
\tag{5.1}
\]
including the lower shifted and \(G\)-variation contractions.

After one covariant derivative, all highest allocations are
\[
\begin{array}{c|l}
\text{source}&\text{\(m=1\) terms}\\ \hline
a\Delta T&a\Delta X,\quad B_1*T_2,\quad
a\operatorname{Rm}*X,\quad a\nabla\operatorname{Rm}*T\\
B_1*T_1&B_1*T_2,\quad B_2*X\\
B_2*T&B_3*T,\quad B_2*X\\
aT*T&B_1*T*T,\quad aX*T\\
[\partial_t,\nabla]T&(\partial_t\Gamma)*T=V*T\\
\text{shift terms}&aX,\quad B_1*T,\quad B_1.
\end{array}
\tag{5.2}
\]

The current reaction coefficients are bounded:
\[
aT*X=U*X,\qquad
a\nabla\operatorname{Rm}*T=aX*T=X*U,
\]
and
\[
a\operatorname{Rm}*X=(U-aG)*X.
\tag{5.3}
\]
The unweighted \(T\) occurs only in forcing products such as
\[
B_1*T*T,\qquad V*T,\qquad C_1*C_2*T.
\]

### 5.1 The \(\nabla^3a*T\) term

By (1.1),
\[
\nabla^3a*T=2\chi C_3*T+C_1*C_2*T.
\tag{5.4}
\]
Set
\[
P(X)=|X|^{p-2}X,\qquad
D_{X,p}=\int_Ma|\nabla X|^2|X|^{p-2}.
\]
For the top term,
\[
\begin{aligned}
I_T
&=\int P(X)*\chi C_3*T\\
&=-\int C_1*Z*T*P(X)
-\int\chi Z*X*P(X)
-\int\chi Z*T*\nabla P(X).
\end{aligned}
\tag{5.5}
\]

The first term is estimated by
\[
\begin{aligned}
\int |C_1||Z||T||X|^{p-1}
&\le L\|Z\|_{2p}\|T\|_{2p}\|X\|_p^{p-1}\\
&\le \delta\|X\|_p^p
+C_{p,\delta}L^p
 \bigl(\|Z\|_{2p}\|T\|_{2p}\bigr)^p.
\end{aligned}
\tag{5.6}
\]

The second is a signed Hessian term:
\[
\left|\int\chi Z*X*P(X)\right|
\le
\varepsilon D_{X,p}
+C_{n,p}\varepsilon^{-1}L^2\|X\|_p^p.
\tag{5.7}
\]

For the third,
\[
\begin{aligned}
\left|\int\chi Z*T*\nabla P(X)\right|
&\le
\varepsilon D_{X,p}
+C_{n,p}\varepsilon^{-1}
 \int |Z|^2|T|^2|X|^{p-2}\\
&\le
\varepsilon D_{X,p}
+C_{n,p,\varepsilon}
 \|Z\|_{2p}^2\|T\|_{2p}^2\|X\|_p^{p-2}\\
&\le
\varepsilon D_{X,p}
+\delta\|X\|_p^p
+C_{n,p,\varepsilon,\delta}
 \bigl(\|Z\|_{2p}\|T\|_{2p}\bigr)^p.
\end{aligned}
\tag{5.8}
\]
For \(p=2\), the middle expression is read directly without the \(X^{p-2}\) factor.

The lower part \(C_1*C_2*T\) in (5.4) satisfies the same Hölder estimate as (5.6). No \(C_3\)-norm is used.

### 5.2 Other highest terms

The derivative term obeys
\[
\left|\int P(X)*B_1*T_2\right|
\le
\varepsilon D_{X,p}
+C_{n,p}\varepsilon^{-1}L^2\|X\|_p^p.
\tag{5.9}
\]

Every \(B_2*X\) term splits into a signed \(\chi C_2*X\) contraction and a bounded \(C_1*C_1*X\) term, hence
\[
\left|\int P(X)*B_2*X\right|
\le
\varepsilon D_{X,p}
+C_{n,p}\varepsilon^{-1}L^2\|X\|_p^p.
\tag{5.10}
\]

The reaction forcing satisfies
\[
\int |B_1||T|^2|X|^{p-1}
\le
\delta\|X\|_p^p
+C_{p,\delta}L^p\|T\|_{2p}^{2p}.
\tag{5.11}
\]

The connection variation is
\[
[\partial_t,\nabla]T=(\partial_t\Gamma)*T=V*T,
\]
and therefore
\[
\int |V||T||X|^{p-1}
\le
\delta\|X\|_p^p
+C_{p,\delta}
 \bigl(\|V\|_{2p}\|T\|_{2p}\bigr)^p.
\tag{5.12}
\]

Since
\[
(A B)^p\le \tfrac12(A^{2p}+B^{2p}),
\]
the products in (5.6), (5.8), and (5.12) may be reduced to completed \(2p\)-norms. The resulting differential inequality is
\[
\boxed{
\begin{aligned}
\frac d{dt}\|X\|_p^p+c_{n,p}D_{X,p}
\le C_{n,p,K,L}\bigl[
1+\|X\|_p^p
+\|T\|_{2p}^{2p}
+\|V\|_{2p}^{2p}
+\|Z\|_{2p}^{2p}
\bigr].
\end{aligned}}
\tag{5.13}
\]
The \(2p\)-norms on the right have already been propagated: first (1.2) at exponent \(2p\), then (4.4) at exponent \(2p\). Thus Grönwall yields
\[
\sup_{\tau\le t<T_*}\|\nabla T(t)\|_p<\infty
\tag{5.14}
\]
for every finite \(p\).

---

## 6. Answers to the four collar questions

1. **Division by \(\chi\): none.**  
   The proof uses
   \[
   B_1=2\chi C_1,\qquad |B_1|^2=4a|C_1|^2,
   \]
   directly. The identities
   \[
   (B_1*B_1)*T=4(C_1*C_1)*U,\qquad
   a\nabla T=V-B_1*T
   \]
   are global algebraic identities and contain no quotient.

2. **Unweighted pointwise \(T\): not used.**  
   The argument does use unweighted finite norms
   \[
   T\in L^q\quad\text{for all finite }q,
   \]
   supplied by the Step 44 zero-order energy. The \(T_1\) estimate uses \(T\), \(V\), and \(Z\) at exponent \(2p\), never \(T\in L^\infty\).

3. **Ratio of regularization parameters: none.**  
   This is the exact \(a=\chi^2\) flow. Expressions such as \(\chi^2/b\) from the regularized Step 45 presentation are unnecessary here. At \(\chi=0\), one should use (3.4), not interpret \(\chi^2/a\) as a quotient.

4. **Small-\(\chi\) collar:** every term containing a derivative of the current variable carries the factor \(\chi\):
   \[
   B_1*\nabla V,\qquad B_1*\nabla X,\qquad
   \chi Z*U*\nabla P(V),\qquad
   \chi Z*T*\nabla P(X).
   \]
   These pair directly with the weighted dissipations \(D_{V,p}\) and \(D_{X,p}\). Signed Hessian integration likewise leaves \(\chi\,d\chi\,\nabla\mathcal B\). Hence no unweighted \(|\nabla V|\) or \(|\nabla X|\) term remains in the collar.

## 7. Corrections and reconciliation of the attached notes

- Step 44 supplies the necessary \(T_0\) seed; it cannot be replaced by the algebraic relation \(U=aT\).
- In Step 40 equation (2.10), at \(m=1\) the raw cutoff equation is precisely
  \[
  \partial_tC_2=U_1*C_1.
  \]
  The schematic \(U_0*C_2\) belongs to norm and measure variation, not to the coordinate evolution of \(C_2\).
- The \(m=1\) \(U\)-equation must group the entire derivative of \((B_1*B_1)*T\) as in (3.4)–(3.5). Separating its apparent \(B_1*B_1*T_1\) component introduces a circular dependence that is absent from the full tensor expression.
- Step 40’s integrations for \(\chi C_3U\) and \(\chi C_3T\), and Step 45’s coordinate-time connection ledger, agree with (3.11) and (5.5).
- The verified triangular order at the earliest stage is
  \[
  T_0\text{ in every finite }L^q
  \;\longrightarrow\;
  (\nabla U,\nabla^2\chi)\text{ in every finite }L^q
  \;\longrightarrow\;
  \nabla T\text{ in every finite }L^p.
  \]

This establishes the complete \(m=1\) positive-time propagation module without using the start construction or any regularized equation.