# TTCS Independent Branch Record

```json
{
  "step_id": 27,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Check the logical interface between a normalized local-flow extension theorem and the existing Step 26 first-exit chain. Determine whether a terminal-time assumption sup|a Rm|<∞ really supplies all hypotheses needed for the shifted-curvature Wang induction on a closed manifold, with constants allowed to depend on the individual smooth initial metric/cutoff, and whether bounds for all ∇^m(a(Rm+G)) suffice for smooth extension. Identify any overlooked issue involving zeros of a, unweighted L^p curvature, evolving contraction Ric(aT)=a Ric(T), transported DeTurck coefficient, or support collar. Also assess whether the claimed whole-support Moser bound is strong enough near a terminal time despite its C/t form.

## Output

## Scientific verification memo

### 1. Terminal weighted-curvature control supplies the analytic input data

Set
\[
S=\widetilde R=\operatorname{Rm}+G,\qquad U=aS,\qquad a=\chi^2.
\]
If
\[
K=\sup_{M\times[0,T)}|a\operatorname{Rm}|<\infty,
\]
then, since \(|G|_g\) is dimensional,
\[
\sup|U|\le K+C_n\|a\|_\infty<\infty.
\]
The key identity is exact:
\[
\operatorname{Ric}(U)=a\operatorname{Ric}(S)=a(\operatorname{Ric}+g)=aE.
\]
Consequently the velocity is
\[
\partial_tg=-2\operatorname{Ric}(U),
\]
and hence
\[
|\partial_tg|_g\le C_n|U|.
\]
For finite \(T\), this gives
\[
e^{-CT}g_0\le g(t)\le e^{CT}g_0.
\]
Thus the following quantities are uniform on the individual flow interval:

- volume-form comparison;
- an inhomogeneous Sobolev constant relative to the fixed closed manifold \((M,g_0)\);
- \(|d\chi|_{g(t)}\);
- norms of fixed smooth tensors such as \(G\).

No sequence-uniform estimates for higher derivatives of \(\chi\) are required. Their initial norms are finite, and Wang’s coupled induction is precisely what propagates their evolving covariant derivatives.

### 2. Unweighted \(L^p\) curvature is recoverable despite zeros of \(a\)

This is an essential input, because \(|U|\) does not control \(S\) pointwise where \(a\) is small. On a closed manifold it follows from the shifted evolution.

Let
\[
Y_p(t)=\int_M(1+|S|^2)^{p/2}\,d\mu_t .
\]
Testing
\[
\partial_tS
=a\Delta S+a\mathcal Q_G(S)
 +(da)*\nabla\operatorname{Ric}(S)
 +(\nabla^2a)*\operatorname{Ric}(S)
\]
against \((1+|S|^2)^{p/2-1}S\), and integrating the Hessian-\(a\) term once, gives schematically
\[
Y_p'
+c_p\int a(1+|S|^2)^{p/2-1}|\nabla S|^2
\le C_{p,K,g_0,\chi,T}Y_p.
\]
The two relevant estimates are
\[
a|S|^{p+1}=|aS|\,|S|^p\le \|U\|_\infty |S|^p
\]
and
\[
|da|\,|\nabla S|\,|S|^{p-1}
\le \varepsilon a|\nabla S|^2|S|^{p-2}
 +C_\varepsilon\frac{|da|^2}{a}|S|^p.
\]
For \(a=\chi^2\),
\[
\frac{|da|^2}{a}=4|d\chi|^2
\]
on \(\{\chi\ne0\}\), with the smooth extension \(4|d\chi|^2\) across the zero set. Tensorially,
\[
\frac{da\otimes da}{a}=4\,d\chi\otimes d\chi.
\]
Thus no singular coefficient occurs at zeros of \(a\). Gronwall yields
\[
\sup_{0\le t<T}\|S(t)\|_{L^p}<\infty
\]
for every finite \(p\), with constants depending on the individual smooth input and on \(K,T\). This supplies the unweighted curvature family used in Wang’s higher-order argument.

The argument must preserve paired expressions such as \(da\otimes da/a\); expressions involving \(da/a\) alone would be singular and are not justified.

### 3. The contraction relation is stronger than stated in Step 27

For spatial covariant derivatives,
\[
\nabla^m(aE)=\nabla^m\operatorname{Ric}(U)
           =\operatorname{Ric}(\nabla^mU)
\]
exactly, because \(\nabla g^{-1}=0\). There are no lower-order terms coming from an “evolving contraction convention” in this identity. Algebraic metric-variation terms arise only if one differentiates the contraction in time.

Similarly,
\[
\partial_t\Gamma=g^{-1}*\nabla(aE)
                =g^{-1}*\nabla\operatorname{Ric}(U).
\]
Hence the evolution of \(\nabla^r\chi\) has highest input \(\nabla^{r-1}U\), exactly matching Wang’s cyclic induction. It is preferable to formulate the pointwise estimate using \(|\nabla^r\chi|^2\), or a regularized norm, at points where \(\nabla^r\chi=0\).

### 4. Normalization introduces no new derivative family, but the detailed induction is still absent

The normalized additions have the following forms:

- terms linear in \(U\), with coefficients made from \(a\), \(G\), and their covariant derivatives;
- quadratic \(U*U\) terms;
- terms involving derivatives of \(\chi\) paired with derivatives of \(U\);
- the same unweighted \(\nabla^jS\) commutator terms that occur in Wang’s argument.

Since \(\nabla G=0\) and
\[
\partial_tG=aE*g=\operatorname{Ric}(U)*g,
\]
the shift does not introduce a tensor family independent of \(U\), \(S\), and \(\chi\). The top cutoff terms remain
\[
\chi\nabla^{m+2}\chi*U,\qquad
\nabla\chi*\nabla^{m+1}\chi*U,\qquad
\chi\nabla^{m+1}\chi*\nabla U,
\]
which are precisely the terms requiring Wang’s integration by parts.

There is one algebraic correction to Step 27: consistency forces
\[
\mathcal Q_G(0)=0.
\]
Indeed, \(S=0\) means \(\operatorname{Ric}+g=0\), so the velocity vanishes for every \(a\), and all derivative terms in the shifted evolution vanish. Therefore an uncancelled degree-zero term in \(\mathcal Q_G\) cannot remain. The loose estimate
\[
|\mathcal Q_G(S)|\le C(1+|S|+|S|^2)
\]
is analytically usable, but the exact polynomial should have its constant part cancelled.

At the level of hypotheses, the terminal assumption provides everything Wang’s induction uses:

\[
U\in L^\infty,\qquad S\in L^p\ \forall p<\infty,\qquad
|d\chi|\in L^\infty,
\]
uniform metric/Sobolev comparison, and finite smooth initial jets. The extension theorem itself still requires explicit shifted versions of Wang Lemma 4.11 and Propositions 4.13–4.14, with every term in \(\mathcal L_{G,m}\) assigned to these families. Equations (3.2)–(3.3) currently describe the correct structure but do not constitute those estimates.

### 5. Bounds for all \(\nabla^mU\) do suffice for smooth extension

Assume
\[
\sup_{M\times[0,T)}|\nabla^mU|<\infty
\qquad\text{for every }m.
\]
Then
\[
\sup|\nabla^m(aE)|\le C_{n,m}\sup|\nabla^mU|.
\]
Let \(A(t)=\nabla^{g(t)}-\nabla^{g_0}\). Since
\[
\partial_tA=g^{-1}*\nabla(\partial_tg)
           =g^{-1}*\nabla\operatorname{Ric}(U),
\]
the bound for \(\nabla U\) controls \(A\). Differentiating this identity relative to \(g_0\) and proceeding inductively controls every \(\nabla_{g_0}^kA\). Therefore all fixed-coordinate derivatives of
\[
\partial_tg=-2\operatorname{Ric}(U)
\]
are uniformly bounded. They are integrable in time, so \(g(t)\) converges in \(C^\infty\) to a smooth positive metric \(g(T)\). Short-time existence from \(g(T)\), with the same fixed scalar \(a\), then extends the original solution. No separate terminal estimate for unweighted pointwise curvature is needed after the full \(U\)-jet bounds have been obtained.

### 6. DeTurck transport and the support collar

The hatted coefficient must satisfy
\[
\widehat a=a\circ\varphi_t^{-1}.
\]
Then
\[
\varphi_t^*\widehat a=a.
\]
Keeping \(\widehat a\) fixed in hatted coordinates would produce a different original-gauge equation. Step 27 uses the correct transported coefficient. The added term \(-2\widehat a\,\widehat g\) is zeroth order in the metric and leaves Yang’s principal regularized operator unchanged; the Lie-derivative and diffeomorphism signs must be paired so that they cancel under pullback.

The outer collar where \(a=0\) contributes only fixed, finite unweighted curvature norms. These may vary greatly across a sequence, but the extension argument permits dependence on the individual initial metric. The weighted tensor \(U\) vanishes in the open exterior of \(\operatorname{supp}\chi\). No collar smallness is needed for terminal continuation.

### 7. The \(C/t\) Moser estimate is sufficient near a positive terminal time

Suppose a maximal time \(T_* \le \theta r^2\) were finite and positive, and Step 26 supplies
\[
\|aF(t)\|_\infty\le \frac{C\bar\beta_*}{t},
\qquad 0<t<T_*.
\]
Although this expression diverges as \(t\downarrow0\), smooth short-time existence gives
\[
\sup_{M\times[0,T_*/2]}|a\operatorname{Rm}|<\infty.
\]
For the later interval,
\[
\sup_{M\times[T_*/2,T_*)}|a\operatorname{Rm}|
\le \frac{2C\bar\beta_*}{T_*}.
\]
Hence
\[
\sup_{M\times[0,T_*)}|a\operatorname{Rm}|<\infty.
\]
Because \(a=0\) outside the active support, a whole-support estimate on \(\operatorname{supp}\chi\) is already a global weighted-curvature estimate. Thus the \(C/t\) behavior near the initial time does not obstruct application of the terminal extension theorem.

**Overall:** the interface between Step 26 and the proposed normalized extension theorem is logically sound at the level of input estimates. Zeros of \(a\), the outer collar, the evolving contraction, and the \(C/t\) estimate introduce no additional hypothesis. The remaining mathematical substance is the full termwise shifted-curvature reproduction of Wang’s coupled high-order estimates.