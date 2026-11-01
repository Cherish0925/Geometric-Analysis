# TTCS Independent Branch Record

```json
{
  "step_id": 8,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step6_collapsed_unwrapping_route.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/step9_general_cover_transport.md",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md"
  ]
}
```

## Task

Independently verify and sharpen the proposed local mean transfer bridge for the fixed-topology critical Ishida–LeBrun sequence. Read the cited working notes and the Naber–Zhang source. Focus on: (i) whether the A01 normal-cover lemma is actually correct for local normal covers, including the closest-lift measurable section, disjoint translates, domain/buffer, and whether its RHS should use B_r(p) or a larger ball; (ii) whether combining that lemma with small base-ball means and Naber–Zhang Proposition 6.4 gives a fixed-scale harmonic chart on the cover for merely bounded Ricci; (iii) whether small mean of the full calibrated deficit on the cover is enough to force the forbidden Einstein germ through finite W^{2,p} convergence, including possible mismatch between the point selected for low mean and the point/scale where Naber–Zhang produces regularity. State a precise conditional theorem that is genuinely supported, and identify the exact unresolved hypothesis needed to apply it to almost all collapsed points. Do not assume Cheeger–Tian curvature decomposition or exact symmetric collapse models.

## Output

# Scientific verification memo

## 1. The normal-cover transport estimate

The estimate in `step9_general_cover_transport.md` is mathematically valid after repairing the covering-domain formulation and the measurable-section argument.

### Corrected statement

Let \(M^n\) be complete, let \(\operatorname{Ric}\ge -(n-1)K g\), and suppose an open set \(U\) contains \(\overline{B_{4r}(p)}\). Let

\[
\pi:(\widehat U,\hat g)\longrightarrow (U,g)
\]

be a connected regular Riemannian covering, with \(\pi(\hat p)=p\). Then every measurable \(\varphi\ge0\) on \(B_r(p)\) satisfies

\[
\fint_{B_r(\hat p)}\pi^*\varphi\,d\hat\mu
\le
\frac{V_{-K}^{(n)}(3r)}{V_{-K}^{(n)}(r)}
\fint_{B_r(p)}\varphi\,d\mu .
\tag{1}
\]

Here the cover balls use the lifted length metric. The extension over \(B_{4r}(p)\) ensures that \(B_{3r}(\hat p)\) is an interior metric ball on which local Bishop–Gromov comparison applies.

The condition written in A01 as merely \(B_{3r}(\hat p)\subset\widehat U\) is vacuous when \(\widehat U\) denotes the whole covering space. What is needed is an interior extension of that ball. Also, if \(\widehat U\) is merely a truncated subset of a larger cover, deck transformations need not preserve \(\widehat U\), so the translate argument does not apply. It applies to the full regular cover of a sufficiently large open base neighborhood.

### Measurable section

Every \(x\in B_r(p)\) has at least one lift in \(B_r(\hat p)\): lift a minimizing geodesic from \(p\) to \(x\). One may therefore choose a Borel map

\[
s:B_r(p)\longrightarrow B_r(\hat p),
\qquad \pi\circ s=\operatorname{id},
\]

using Borel uniformization for the countable-fiber relation

\[
\{(x,\hat x):\pi(\hat x)=x,\ d(\hat p,\hat x)<r\}.
\]

Its image \(S=s(B_r(p))\) is Borel, contains exactly one point over each base point, and the area formula for the local isometry gives

\[
\operatorname{Vol}(S)=\operatorname{Vol}(B_r(p)).
\tag{2}
\]

Thus no closest-lift construction is required. The A01 sentence asserting that equidistance sets are codimension-one submanifolds is not established in this generality: distance functions encounter cut loci, and coincidence sets can be more complicated. This does not affect (1), because an arbitrary Borel lift inside \(B_r(\hat p)\) suffices.

### Multiplicity and disjoint translates

Let

\[
N(2r)=\#\{\gamma\in\Gamma:
d(\hat p,\gamma\hat p)<2r\},
\]

where \(\Gamma\) is the deck group. If \(\hat x\in B_r(\hat p)\) projects to \(x\), regularity of the cover gives a unique \(\gamma\) such that \(\hat x=\gamma s(x)\). Then

\[
d(\hat p,\gamma\hat p)
\le d(\hat p,\hat x)+d(s(x),\hat p)<2r.
\]

Hence the multiplicity of \(\pi:B_r(\hat p)\to B_r(p)\) is at most \(N(2r)\).

For every such \(\gamma\),

\[
\gamma S\subset B_{3r}(\hat p),
\]

and the sets \(\gamma S\) are pairwise disjoint. Applying (2) first to finite subsets of the deck group and then taking the supremum gives

\[
N(2r)\operatorname{Vol}(B_r(p))
\le \operatorname{Vol}(B_{3r}(\hat p)).
\tag{3}
\]

The local-isometry area formula now yields

\[
\int_{B_r(\hat p)}\pi^*\varphi
\le N(2r)\int_{B_r(p)}\varphi.
\]

Combining this with (3) and Bishop–Gromov proves (1). The sheet count cancels exactly.

### Which base ball appears?

For a cover ball centered over \(p\), the right-hand side of (1) is genuinely the mean on \(B_r(p)\), not on a larger ball. If the available estimate is instead on \(B_R(p)\), \(R\ge r\), Bishop–Gromov gives

\[
\fint_{B_r(p)}\varphi
\le
\frac{V_{-K}^{(n)}(R)}{V_{-K}^{(n)}(r)}
\fint_{B_R(p)}\varphi.
\tag{4}
\]

If the cover chart is centered over \(q\) with \(d(p,q)\le d\), then

\[
\fint_{B_r(q)}\varphi
\le
\frac{V_{-K}^{(n)}(R+d)}{V_{-K}^{(n)}(r)}
\fint_{B_R(p)}\varphi
\]

whenever \(B_r(q)\subset B_R(p)\). Thus a shifted regularity point causes only a fixed comparison factor.

---

## 2. What Naber–Zhang Proposition 6.4 supplies

The supplied Naber–Zhang source, Proposition 6.4 in §6.2, states that under

\[
|\operatorname{Ric}|\le n-1,
\]

local relative compactness, GH closeness

\[
B_2(p)\simeq
B_2(0^{k-\ell},z^\ell)
\subset\mathbb R^{k-\ell}\times Z^\ell,
\qquad \ell\le3,
\]

and maximal fibered nilpotency rank

\[
\operatorname{rank}\Gamma_{\delta_0}(p)=n-k,
\]

there is a fixed \(h_0>0\) such that

\[
r_h(\tilde q)\ge h_0
\qquad\text{for every }q\in B_1(p),
\tag{5}
\]

where \(\tilde q\) lies in the universal cover of \(B_1(q)\). The constants depend on \(n\) and the model \(B_1(z^\ell)\); the introduction explains that this dependence can be expressed through the model noncollapsing radius \(r_c(z^\ell)\).

Three distinctions matter here.

1. **Bounded Ricci is enough for (5).** Exact Einstein structure and bounds on \(\nabla\operatorname{Ric}\) are not assumed in Proposition 6.4.

2. **The output is a \(C^1\) harmonic-radius bound.** A pointwise curvature estimate for the approximating metrics is not supplied under bounded Ricci alone. Naber–Zhang obtain curvature bounds for Einstein metrics, or with derivative control on Ricci.

3. **Proposition 6.4 is stated for local universal covers.** It does not automatically give the same harmonic radius on every intermediate regular cover. The transport lemma applies directly to the universal cover used in (5).

For the present sequence, \(\operatorname{Ric}_{g_i}+g_i\to0\) in \(L^\infty\), so \(|\operatorname{Ric}_{g_i}|\le3\) for large \(i\), matching the four-dimensional normalization.

Choose \(a<1/4\), for example \(a=1/8\). The universal cover of \(B_1(p_i)\) extends far enough for the transport estimate at radius \(a\). Taking \(q=p_i\) in (5) aligns the low-mean point and the harmonic-chart point exactly:

\[
\fint_{B_a(\tilde p_i)}\pi_i^*F_i
\le C(a)\fint_{B_a(p_i)}F_i.
\tag{6}
\]

After shrinking \(h_0\), a fixed harmonic chart around \(\tilde p_i\) lies inside \(B_a(\tilde p_i)\). Thus the proposed bridge works under the full Naber–Zhang GH/rank assumptions. Low mean plus bounded Ricci alone does not create such a chart.

---

## 3. Passage from cover mean to the forbidden Einstein germ

The explicit curvature density from A01 is sufficient. Set

\[
u_i=|W_i^+|,
\qquad
w_i=\lambda_{\min}(W_i^+),
\qquad
\alpha=\sqrt{\frac23},
\]

\[
f_i=\frac23s_i-2\alpha u_i,
\qquad
b_i=\frac23s_i+2w_i,
\]

and

\[
\mathcal G_i=f_i^2-\bigl(\min\{b_i,0\}\bigr)^2.
\]

The algebra in `step8_derdzinski_measure_local_theorem.md` gives \(\mathcal G_i\ge0\). The required full density may be taken as

\[
F_i=
|\operatorname{Ric}_{g_i}+g_i|^2
+(s_i+8\sqrt6\,|W_i^+|)^2
+\mathcal G_i.
\tag{7}
\]

For a fixed critical Ishida–LeBrun manifold, the supplied bookkeeping gives

\[
\int_M F_i\,d\mu_i\longrightarrow0,
\qquad
\operatorname{Vol}(M,g_i)\longrightarrow
\frac{32\pi^2A}{9}>0.
\tag{8}
\]

All terms in (7) pull back exactly under an orientation-preserving local isometry.

Suppose the right-hand side of (6) tends to zero. Bishop–Gromov gives a uniform upper volume bound on \(B_a(\tilde p_i)\), so

\[
\int_{B_a(\tilde p_i)}\pi_i^*F_i\longrightarrow0.
\tag{9}
\]

A fixed smaller harmonic chart therefore also has vanishing integral.

### Finite \(W^{2,p}\) convergence

The Naber–Zhang harmonic radius controls the metric and its first coordinate derivatives. In harmonic coordinates,

\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=
-2(\operatorname{Ric}_{g_i})_{jk}
+Q_{jk}(g_i^{-1},\partial g_i).
\tag{10}
\]

The coefficients are uniformly elliptic and Lipschitz, while the right-hand side is uniformly bounded in every finite \(L^p\). Interior estimates give uniform \(W^{2,p}\) bounds. Taking \(p>4\), compact embedding yields strong \(C^{1,\beta}\) convergence after shrinking the chart.

Writing

\[
\operatorname{Ric}_{g_i}=-g_i+e_i,
\qquad \|e_i\|_{L^\infty}\to0,
\]

shows that the right-hand side of (10) converges strongly in finite \(L^p\). The difference equation then gives strong \(W^{2,p}\) convergence on a still smaller chart. The limit satisfies

\[
\operatorname{Ric}_{g_\infty}=-g_\infty
\]

weakly and hence smoothly by harmonic-coordinate elliptic regularity. No uniform \(C^{2,\alpha}\) estimate for the approximating metrics and no derivative bound on Ricci are used.

Curvature consequently converges strongly in finite \(L^p\). Scalar curvature, \(|W^+|\), the smallest eigenvalue of \(W^+\), and \(\mathcal G\) therefore pass strongly in \(L^1\). Equation (9) gives

\[
s_\infty=-4,
\qquad
|W_\infty^+|=\frac1{2\sqrt6},
\qquad
\mathcal G_\infty=0.
\tag{11}
\]

At the values in (11),

\[
f_\infty=-3,
\qquad
\xi_\infty:=w_\infty+\sqrt{\frac23}|W_\infty^+|
=w_\infty+\frac16,
\]

and

\[
\mathcal G_\infty=4\xi_\infty(3-\xi_\infty).
\]

For a trace-free self-dual Weyl endomorphism, \(\xi_\infty\ge0\), while \(w_\infty\le0\), so \(\xi_\infty\le1/6\). Hence \(\mathcal G_\infty=0\) implies \(w_\infty=-1/6\). Trace and norm then give

\[
\operatorname{Spec}(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\tag{12}
\]

No lifted monopole field is needed once the explicit term \(\mathcal G_i\) is included.

### Local inconsistency

Since \(g_\infty\) is Einstein, \(\delta W_\infty^+=0\). The constant two-eigenvalue projector calculation from A03 gives

\[
\nabla W_\infty^+=0.
\]

On the other hand, the Einstein–Weyl scalar identity

\[
\Delta |W^+|^2
=
2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]

with

\[
s=-4,\qquad |W^+|^2=\frac1{24},
\qquad \det W^+=-\frac1{864}
\]

gives

\[
|\nabla W^+|^2=\frac1{16}.
\]

Thus the smooth limit germ cannot exist.

There is no point/scale mismatch in this construction: choose \(q=p_i\) in Proposition 6.4. If another point \(q_i\) is used, either (4) transports the base mean to \(q_i\), or one transports the integral on a cover ball large enough to contain the harmonic chart; positivity of \(F_i\) then passes smallness to the chart.

---

## 4. Precise conditional theorem

**Theorem.** Let \(M^4\) be a fixed closed oriented smooth manifold and let \(g_i\) satisfy

\[
\|\operatorname{Ric}_{g_i}+g_i\|_{L^\infty}\to0,
\qquad
\fint_M F_i\,d\mu_i\to0,
\]

with \(F_i\) given by (7). Fix \(r_*>0\). For each \(i\), let \(S_i\subset M\) consist of points \(p\) for which there are integers \(k,\ell\), \(\ell\le3\), and a pointed \(\ell\)-dimensional Ricci-limit model \((Z^\ell,z^\ell)\) such that:

\[
r_c(z^\ell)\ge r_*,
\]

\[
d_{GH}\!\left(
B_2(p),
B_2(0^{k-\ell},z^\ell)
\right)<\delta_*(4,r_*),
\]

and

\[
\operatorname{rank}
\operatorname{Image}\!\left[
\pi_1(B_{\delta_*}(p))
\to\pi_1(B_2(p))
\right]
=4-k.
\]

Then

\[
\frac{\operatorname{Vol}_{g_i}(S_i)}
{\operatorname{Vol}_{g_i}(M)}
\longrightarrow0.
\tag{13}
\]

Indeed, if the ratio in (13) stayed above some \(\eta>0\), the local-mean averaging identity would select \(p_i\in S_i\) with

\[
\fint_{B_{1/8}(p_i)}F_i\to0.
\]

Naber–Zhang Proposition 6.4 gives a uniform harmonic radius at the lift of \(p_i\) in the universal cover of \(B_1(p_i)\). The corrected transport estimate gives (9), and the finite-\(W^{2,p}\) passage produces the impossible germ (12).

## 5. Exact unresolved hypothesis for volume-typical collapsed points

The transport component no longer requires deck-counting, a nilpotent coordinate model, or a sheet-multiplicity assumption. The missing geometric statement is:

> At a fixed geometric scale, a set of collapsed points with positive volume proportion has maximal fibered nilpotency rank and lower-dimensional GH models whose Naber–Zhang model radius stays uniformly positive.

Equivalently, it would suffice to obtain constants \(\rho,\eta>0\) such that

\[
\operatorname{Vol}\left\{
p:
r_h(\tilde p;\widetilde{B_1(p)})\ge\rho
\right\}
\ge \eta\,\operatorname{Vol}(M,g_i)
\]

along a subsequence. To cover volume-typical points, the left-hand proportion would tend to one.

The supplied Ishida–LeBrun estimates give small global defect and base collapse, but they do not establish prevalence of maximal rank or a uniform model radius. Naber–Zhang proves regularity once those geometric inputs are present; it does not show that they occur on a positive-volume set. Rank-drop regions, singular fibers, and degenerating model scales remain compatible with the currently supplied information.