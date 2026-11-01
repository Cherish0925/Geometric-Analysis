# TTCS Independent Branch Record

```json
{
  "step_id": 27,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md",
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Resolve one exact derivative-index discrepancy that emerged after the prior review. Wang Proposition 4.14 assumes cutoff derivatives only through order m when proving an L^p bound for ∇^m(χ²Rm), even though its raw Γ1,Γ2,Γ3 terms contain χ∇^{m+2}χ·U, ∇χ∇^{m+1}χ·U, and χ∇^{m+1}χ·∇U. The Step 27 theorem draft instead introduced a current-order pair ∇^mU ↔ ∇^{m+1}χ after only one integration by parts. Read Wang lines 622–659 and the shifted-curvature equations. Determine which dependency is actually justified. Reconstruct the grouped integration-by-parts reduction of Γ1–Γ3 far enough to show whether all ∇^{m+1}χ terms reduce to diffusion-controlled terms plus ∇²χ·∇^mχ·U (as Wang states), or whether Wang implicitly needs ∇^{m+1}χ/current Volterra closure. Then state the correct induction order for shifted T=Rm+G, U=aT, and identify any exact coefficient/cancellation needed rather than relying only on schematic stars.

## Output

## Scientific verification memo

### 1. Resolution

The dependency justified by the displayed energy calculation is

\[
\nabla^mU\;\longleftrightarrow\;\nabla^{m+1}\chi ,
\]

not a one-way estimate of \(\nabla^mU\) from cutoff derivatives only through order \(m\).

The first term on the right of Step 27 equation (3.5),

\[
-\int \nabla\!\left(|W|^{p-2}W\right)
       *\chi\nabla^{m+1}\chi*U ,
\qquad W=\nabla^mU,
\tag{1.1}
\]

survives every favorable grouping of Wang’s \(\Gamma _1,\Gamma _2,\Gamma _3\). Diffusion controls the derivative of \(W\), but the resulting Young estimate contains \(\nabla^{m+1}\chi\):

\[
\begin{aligned}
|(1.1)|
&\le
\varepsilon\int \chi^2|\nabla W|^2|W|^{p-2}\\
&\quad+C_{n,p,\varepsilon}
\int |\nabla^{m+1}\chi|^2|U|^2|W|^{p-2}.
\end{aligned}
\tag{1.2}
\]

Thus Step 27 equations (3.5)–(3.6) retain the correct derivative index. Wang Proposition 4.14’s sentence asserting dependence only on cutoff derivatives through order \(m\) does not follow from its displayed integrations.

---

### 2. Exact highest-cutoff operator for the shifted system

Define, for a symmetric \(2\)-tensor \(S\) and a symmetric Hessian \(H\),

\[
\mathcal K(H,S)_{ijkl}
=
H_{ik}S_{jl}+H_{jl}S_{ik}
-H_{il}S_{jk}-H_{jk}S_{il}.
\tag{2.1}
\]

With Wang’s curvature convention, the exact Hessian-of-\(a\) part of the curvature evolution for

\[
T=\operatorname{Rm}+G,\qquad E=\operatorname{Ric}(T)
\]

is

\[
\bigl[(\partial_t-a\Delta)T\bigr]_{\nabla^2a}
=
-\mathcal K(\nabla^2a,E).
\tag{2.2}
\]

There is no derivative contribution from \(\partial_tG\), since \(\partial_tG\) is algebraic in \(U=aT\) and \(g\).

For \(U=aT\),

\[
a\Delta U
=a^2\Delta T+2a\,da*\nabla T+a(\Delta a)T.
\]

Consequently, the complete Hessian-of-\(a\) coefficient in the \(U\)-equation is

\[
\boxed{
\mathcal P_U(H)
=
-\mathcal K(H,\operatorname{Ric}U)-(\operatorname{tr}_gH)\,U,
}
\tag{2.3}
\]

so that

\[
\bigl[(\partial_t-a\Delta)U\bigr]_{\nabla^2a}
=\mathcal P_U(\nabla^2a).
\tag{2.4}
\]

This is the exact version of the schematic term \(\nabla^2a*U\) in Step 27 equation (2.8). It also displays the shifted cancellation correctly: every term contains \(U\); there is no independent \(\nabla^2a*G\) contribution.

The operator \(\mathcal P_U\) is not identically zero. At an orthonormal point, take \(U=G\) and \(H=e^1\otimes e^1\). Then \(\operatorname{Ric}U=g\) and

\[
\bigl(\mathcal P_G(H)\bigr)_{1212}
=-1-\frac1{n-1}
=-\frac n{n-1}\neq0.
\tag{2.5}
\]

Therefore no algebraic identity can remove the highest Hessian channel.

Because \(a=\chi^2\),

\[
\nabla^{m+2}a
=
2\chi\nabla^{m+2}\chi
+2(m+2)\operatorname{Sym}
   (\nabla\chi\otimes\nabla^{m+1}\chi)
+\{\text{cutoff derivatives of order at most }m\}.
\tag{2.6}
\]

In particular, the coefficient of the \(\chi\nabla^{m+2}\chi\) channel is exactly \(2\), applied through the nonzero operator \(\mathcal P_U\).

---

### 3. Grouped integration of Wang’s \(\Gamma _1,\Gamma _2,\Gamma _3\)

Set

\[
Z=|W|^{p-2}W,\qquad W=\nabla^mU,\qquad
\Phi=\nabla^m\chi.
\]

Suppressing only curvature commutators involving cutoff derivatives through order \(m\), a fixed contraction channel of the three highest terms has the form

\[
\begin{aligned}
\Gamma_1&=c_1\int Z*\chi\nabla^2\Phi*U,\\
\Gamma_2&=c_2\int Z*\nabla\chi*\nabla\Phi*U,\\
\Gamma_3&=c_3\int Z*\chi\nabla\Phi*\nabla U.
\end{aligned}
\tag{3.1}
\]

For the channel arising from (2.3)–(2.6), \(c_1\) contains the exact factor \(2\) and is nonzero. Integrating \(\Gamma _1\) once gives

\[
\begin{aligned}
\Gamma_1
={}&-c_1\int \nabla Z*\chi\nabla\Phi*U\\
&-c_1\int Z*\nabla\chi*\nabla\Phi*U\\
&-c_1\int Z*\chi\nabla\Phi*\nabla U
+L_m,
\end{aligned}
\tag{3.2}
\]

where \(L_m\) uses cutoff derivatives through order \(m\).

Even in the most favorable coefficient matching, where the last two terms in (3.2) cancel the corresponding parts of \(\Gamma _2+\Gamma _3\), one is left with

\[
-c_1\int \nabla Z*\chi\nabla^{m+1}\chi*U.
\tag{3.3}
\]

This is precisely Step 27 equation (3.5)’s first integral.

The remaining \(Z\)-level terms can indeed be reduced to order \(m\). For example,

\[
\begin{aligned}
\int Z*\nabla\chi*\nabla\Phi*U
={}&-\int \nabla Z*\nabla\chi*\Phi*U\\
&-\int Z*\nabla^2\chi*\Phi*U\\
&-\int Z*\nabla\chi*\Phi*\nabla U+L_m,
\end{aligned}
\tag{3.4}
\]

which produces Wang’s displayed exceptional term

\[
\int Z*\nabla^2\chi*\nabla^m\chi*U.
\tag{3.5}
\]

Likewise,

\[
\begin{aligned}
\int Z*\chi\nabla\Phi*\nabla U
={}&-\int\nabla Z*\chi\Phi*\nabla U\\
&-\int Z*\nabla\chi*\Phi*\nabla U\\
&-\int Z*\chi\Phi*\nabla^2U+L_m.
\end{aligned}
\tag{3.6}
\]

These expressions use cutoff derivatives through order \(m\). However, applying the same operation to (3.3) differentiates \(\nabla Z\) and produces \(\nabla^2Z\), for which the first-order diffusion energy gives no estimate. Hence (3.3) cannot be reduced by this argument.

For Wang’s asserted \(m\)-only dependency to hold, the evolution would need an additional term with the exact form and coefficient

\[
+c_1\int \nabla Z*\chi\nabla^{m+1}\chi*U.
\tag{3.7}
\]

Neither \(\Gamma _2,\Gamma _3,\Gamma _4\), the differentiated diffusion term, nor the \(G\)-reaction produces (3.7). Coefficient matching among \(\Gamma _1,\Gamma _2,\Gamma _3\) can cancel only the two \(Z\)-level terms in the last two lines of (3.2), not the derivative-on-\(Z\) term.

Thus Wang’s lines 622–659 implicitly require the current cutoff jet \(\nabla^{m+1}\chi\), followed by a Volterra coupling with \(\nabla^mU\).

---

### 4. Exact current-order cutoff coupling

The identity

\[
aE=\operatorname{Ric}(U)
\tag{4.1}
\]

is exact because the contraction is spatially parallel. For

\[
S=\operatorname{Ric}(U),\qquad \partial_tg=-2S,
\]

the connection variation is exactly

\[
\partial_t\Gamma^k_{ij}
=
-g^{k\ell}
\left(
\nabla_iS_{j\ell}
+\nabla_jS_{i\ell}
-\nabla_\ell S_{ij}
\right).
\tag{4.2}
\]

Since \(\chi\) is a fixed scalar, the highest term in
\(\partial_t\nabla^{m+1}\chi\) is therefore

\[
\nabla^mS*\nabla\chi
=
\operatorname{Ric}(\nabla^mU)*\nabla\chi.
\tag{4.3}
\]

After including lower derivatives, norm variation, and the volume form,

\[
\|\nabla^{m+1}\chi(t)\|_{L^p}
\le
C+C\int_0^t
\left(1+\|\nabla^mU(s)\|_{L^p}\right)\,ds,
\tag{4.4}
\]

with a finite staggered family of exponents when required by products.

If

\[
X_{m,p}=\|\nabla^mU\|_{L^p}^2,\qquad
H_{m,p}=\|\nabla^{m+1}\chi\|_{L^p}^2,
\]

then (1.2) and the other energy terms give

\[
X_{m,p}'\le C(1+X_{m,p}+H_{m,p}),
\tag{4.5}
\]

while (4.4), Cauchy–Schwarz in time, and \(T<\infty\) give

\[
H_{m,p}(t)
\le C+C\int_0^tX_{m,p}(s)\,ds.
\tag{4.6}
\]

Hence

\[
X_{m,p}'(t)
\le
C\left(
1+X_{m,p}(t)+\int_0^tX_{m,p}(s)\,ds
\right),
\tag{4.7}
\]

which is the required current-order Volterra closure.

---

### 5. Correct shifted induction order

For each \(m\ge1\), the coherent order is:

1. **Data already available**
   \[
   \nabla^jU,\ j\le m-1;\qquad
   \nabla^r\chi,\ r\le m;\qquad
   \nabla^jT,\ j\le m-1,
   \]
   in the required finite \(L^p\) families.

2. **Current weighted pair**
   Estimate simultaneously
   \[
   \nabla^mU
   \quad\text{and}\quad
   \nabla^{m+1}\chi
   \]
   through (4.5)–(4.7). The term (3.3) is the reason this pairing is necessary.

3. **Current unweighted curvature**
   With \(\nabla^{m+1}\chi\) now controlled, estimate \(\nabla^mT\). Its raw
   \(\chi\nabla^{m+2}\chi*T\) term is integrated once and therefore uses
   \(\nabla^{m+1}\chi\), exactly as in Wang Proposition 4.13.

4. **Pointwise upgrade**
   After all finite \(L^p\) levels are established, apply Sobolev to adjacent derivative levels to obtain pointwise bounds for every \(\nabla^mU\).

The base \(m=1\) is Wang Lemma 4.11’s joint estimate for
\(\nabla U\) and \(\nabla^2\chi\), followed by the estimate of \(\nabla T\).

The parallel shift introduces no higher cutoff jet: \(\nabla G=0\), and differentiating \(aG*U\) uses cutoff derivatives only through order \(m\) together with the current \(\nabla^mU\). Thus the accurate dependency recorded in Step 27 equation (6.7),

\[
\nabla^mU\longleftrightarrow\nabla^{m+1}\chi,
\]

is the mathematically supported one. The attribution to Wang’s printed \(m\)-only reduction should be understood as a repair of its derivative indexing, not as a literal consequence of the Proposition 4.14 paragraph.