# TTCS Independent Branch Record

```json
{
  "step_id": 36,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A01/workspace/scripts/step36_platform_Q_verify.py",
    "Sessions/S0910A03/workspace/notes/step36_preceptor_interface_review.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify the Step 36 analytic-platform note for the restricted four-dimensional negative Ishida--LeBrun cutoff-flow route. Read the new note and script, A03's Step 36 Preceptor review, the Step 35 tensor identity note, and the Yang/Wang source objects. Please check: (i) whether the transported-coefficient normalized DeTurck formulation correctly pulls back to the fixed-cutoff flow and whether the linearized lower-order normalization discussion is sound; (ii) whether the quantifier separation between per-datum short-time existence, maximal-time extension, and sequence-uniform bootstrap quantities is mathematically appropriate; (iii) whether the separate global Q propagation estimate is correctly weighted and genuinely independent of J6/aE; (iv) whether the shifted-U extension target is stated without smuggling in unweighted curvature or pointwise cutoff-Hessian control; and (v) what concrete analytic calculation would most strengthen the route next. Do not treat the note as a completed proof of existence or of Yau Problem 26; identify exact hidden assumptions or equation-level gaps.

## Output

# Scientific verification memo

## 1. Transported normalized DeTurck system

The coupled formulation
\[
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{\widehat aW(\widehat g,S)}\widehat g,
\qquad
\partial_t\varphi_t\circ\varphi_t^{-1}=-\widehat aW,
\qquad
\widehat a=a\circ\varphi_t^{-1},
\]
does pull back exactly to
\[
\partial_tg=-2a(\operatorname{Ric}_g+g).
\]
Indeed, \(\varphi_t^*\widehat a=a\), and
\[
\frac d{dt}\varphi_t^*\widehat g
=\varphi_t^*\!\left(\partial_t\widehat g
+\mathcal L_{-\widehat aW}\widehat g\right)
=-2a(\operatorname{Ric}_g+g).
\]
The distinction
\[
\mathcal L_{\widehat aW}\widehat g
=\widehat a\mathcal L_W\widehat g
+d\widehat a\otimes W^\flat+W^\flat\otimes d\widehat a
\]
is essential. Yang’s Theorem 8.2 uses precisely the transported coefficient inside the formal adjoint term; after identifying \(2\widehat\delta^*(\widehat a\,\omega)\) with a Lie derivative, this agrees with \(\mathcal L_{\widehat aW}\widehat g\).

There is one formula error in Step 36 §1.1. Let
\[
\alpha=\delta\widehat a,\qquad h=\delta\widehat g.
\]
The variation of the full geometric term is
\[
\delta[-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)]
=-2\widehat a\,D\operatorname{Ric}_{\widehat g}[h]
-2\alpha(\operatorname{Ric}_{\widehat g}+\widehat g)
-2\widehat a h.
\]
Relative to Yang’s unnormalized system, the added normalized contribution is only
\[
\boxed{\delta[-2\widehat a\,\widehat g]
=-2\widehat a h-2\alpha\,\widehat g.}
\]
Thus (1.7), which assigns \(-2\alpha(\operatorname{Ric}+\widehat g)\) to the new normalized term, mixes the coefficient variation already present in Yang’s Ricci term with the new zeroth-order term.

This correction does not alter the principal structure. If
\[
\zeta=\delta\varphi\circ\varphi^{-1},
\]
then
\[
\alpha=-d\widehat a(\zeta),
\]
which contains no derivatives of \(h\) or \(\zeta\). Consequently the added term contributes no second spatial derivatives of \(h\). The normalization is therefore a lower-order perturbation of Yang’s triangular linearized system. A complete existence argument still needs the tame estimates for the coupled \((h,\psi)\) equations, including the variation of the transport equation and of \(\mathcal L_{\widehat aW}\widehat g\); ordinary Schauder estimates with ellipticity constant \(\varepsilon^2\) do not supply the required uniform passage as \(\varepsilon\to0\).

## 2. Quantifier separation

The three-level separation is mathematically appropriate:

1. For each fixed smooth datum \((g_0,\chi)\), Yang-type theory may produce a time \(T_0(g_0,\chi)>0\) depending on every derivative of that datum.
2. On the maximal interval \([0,T_{\max})\), sequence-level zero-order estimates may provide the hypotheses needed for a per-datum extension argument.
3. Only quantities entering the terminal geometric construction need constants uniform along the near-critical family.

No common initial lifespan is required. For each datum one starts on its own interval, derives the first-exit estimates on every proper subinterval, and uses extension at a hypothetical \(T_{\max}<\theta r^2\).

One quantifier in (2.1) should be strengthened. The assertion
\[
\int_0^t\|aE(s)\|_\infty\,ds<\infty
\quad\text{for every }t<T_{\max}
\]
is automatic for a smooth solution on proper subintervals and does not yield terminal metric comparison. What is needed is
\[
\boxed{
\sup_{t<T_{\max}}
\int_0^t\|aE(s)\|_\infty\,ds<\infty.}
\]
Estimate (4.4) supplies this stronger statement whenever \(T_{\max}\leq\theta r^2\). It then gives a uniform-in-\(t\) constant \(\Lambda<\infty\) such that
\[
\Lambda^{-1}g(\tau)\le g(t)\le\Lambda g(\tau),
\qquad \tau\le t<T_{\max}.
\]

Similarly, for any fixed \(\tau>0\),
\[
\|aF(t)\|_\infty\le \frac{C\gamma}{t}
\]
implies
\[
\sup_{\tau\le t<T_{\max}}|U(t)|
\le C\left(1+\frac{\gamma}{\tau}\right),
\qquad U=a(\operatorname{Rm}+G).
\]
Thus the proposed terminal hypotheses are genuinely produced by the uniform bootstrap rather than by smoothness on proper subintervals.

## 3. Separate propagation of \(Q=\int|E|^2\)

The weighting mechanism is sound. Step 35 establishes
\[
B_{\rm def}^{ij}
=|E|^2g^{ij}+(\operatorname{tr}E)E^{ij}-2(E^2)^{ij},
\]
with
\[
|B_{\rm def}|\le C|E|^2,\qquad
|\nabla B_{\rm def}|\le C|E||\nabla E|.
\]
Hence the Hessian-\(a\) contribution to \(Q'\) can be treated as
\[
2\int \nabla^2a:B_{\rm def}
=-2\int da\cdot\operatorname{div}B_{\rm def},
\]
and therefore
\[
\left|2\int \nabla^2a:B_{\rm def}\right|
\le \varepsilon\int a|\nabla E|^2
+C_\varepsilon\int\frac{|da|^2}{a}|E|^2.
\]
This directly supports the structure
\[
Q_U'+cX_U
\le C\int_U\left(\frac{|da|^2}{a}+a\right)|E|^2
+C\int_UaF|E|^2.
\]

The potential estimate is also correctly weighted:
\[
\int aF|E|^2=\int F|\chi E|^2
\le \|F\|_2\|\chi E\|_4^2,
\]
and in four dimensions
\[
\|\chi E\|_4^2
\le C\mathcal S\left(
X_U+r^{-2}Q_U\right).
\]
Thus
\[
\int aF|E|^2
\le C\gamma(X_U+r^{-2}Q_U),
\qquad
\gamma=\mathcal S(K_2^\eta)^{1/2},
\]
and small \(\gamma\) absorbs \(X_U\).

Three assumptions should be made explicit.

* The local integration region must satisfy \(\operatorname{supp}a\Subset U\), so no spatial-edge contribution appears.
* If \(K_2^\eta\) denotes the buffered curvature energy, the precise definition should be
  \[
  K_2^\eta=\int_U\eta^2F^2,
  \qquad \eta\equiv1\ \text{on }\operatorname{supp}\chi.
  \]
  Hölder then uses
  \[
  \int_{\operatorname{supp}\chi}F^2\le K_2^\eta.
  \]
  Writing \(K_2^\eta=\int_UF^2\) is stronger and is not the usual buffered definition from Step 35.
* Before simplifying the zeroth-order coefficient, the result is
  \[
  Q_U'\le C(1+r^{-2})Q_U.
  \]
  The displayed \(Cr^{-2}Q_U\) requires \(r\le1\). Otherwise the global estimate is
  \[
  Q(t)\le
  \exp\!\bigl(C(1+r^{-2})t\bigr)Q(0),
  \]
  which at \(t=\theta r^2\) becomes
  \[
  Q(\theta r^2)\le e^{C\theta(1+r^2)}Q(0).
  \]
  Uniform propagation still follows if the selected radii have a fixed upper bound.

For disjoint buffered supports, the inequalities sum with the same coefficient. On the open exterior where \(a\equiv0\), the metric is unchanged in a neighborhood of each point and hence \(E\) is unchanged there. This justifies the global Gronwall estimate.

The independence from \(J_6\) and \(\|aE\|_\infty\) is genuine. A smooth scalar model makes the separation particularly clear. On \((-1,1)\), let
\[
\chi=x^2,\qquad a=x^4,\qquad
E_\varepsilon=(x^2+\varepsilon^2)^{-1}.
\]
Then
\[
\|aE_\varepsilon\|_\infty\le C,\qquad
\int a^4E_\varepsilon^6\,dx\le C,
\]
uniformly in \(\varepsilon\), whereas
\[
\int E_\varepsilon^2\,dx\asymp\varepsilon^{-3}.
\]
This is only a model of the weights, not a geometric tensor construction, but it proves that no uniform functional implication from the weighted quantities to \(Q\) exists.

The Python script correctly verifies the Lie-derivative product identity, exponent arithmetic, and the hand-entered dependency graph. Several entries, including D2–D4, Q1, Q3, Q5, S2, and G5, are hard-coded Boolean assertions. It therefore supplies symbolic consistency evidence, not verification of the defect evolution or its integration-by-parts estimate.

## 4. Shifted-\(U\) extension target

The stated theorem uses neither \(\|T\|_\infty\) nor a pointwise bound for \(\nabla^2\chi\). Its basic identity is correct:
\[
\operatorname{Ric}(U)=aE,\qquad
\partial_tg=-2\operatorname{Ric}(U),
\]
and therefore, more explicitly,
\[
\partial_t\Gamma^k_{ij}
=-g^{k\ell}\left(
\nabla_i\operatorname{Ric}(U)_{j\ell}
+\nabla_j\operatorname{Ric}(U)_{i\ell}
-\nabla_\ell\operatorname{Ric}(U)_{ij}\right).
\]
For the fixed scalar \(\chi\),
\[
\partial_t(\nabla_i\nabla_j\chi)
=-(\partial_t\Gamma^k_{ij})\nabla_k\chi,
\]
so the cutoff Hessian is coupled to \(\nabla U\), not to a split expression containing \(da*\operatorname{Rm}+a\nabla\operatorname{Rm}\).

The normalization of \(G\) should be fixed componentwise because conventions for \(g\owedge g\) differ. The desired identity is ensured by writing
\[
\boxed{
G_{ijkl}
=\frac1{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}),}
\]
with the Ricci contraction convention used in Step 35. Then \(\operatorname{Ric}(G)=g\).

The roadmap still contains two equation-level gaps.

First, the “previously controlled unweighted \(L^p\) norms of \(T\)” must be derived from \(\sup|U|\), rather than inserted as an additional hypothesis. The normalized analogue of Wang’s Lemma 4.10 should establish an inequality of the form
\[
\frac d{dt}\int_M(1+|T|^2)^{p/2}
\le C_{p,\tau,K,\chi,g(\tau)}
\int_M(1+|T|^2)^{p/2},
\]
using signed integration by parts for the Hessian-\(a\) terms. This would provide finite \(L^p\) norms for every fixed \(p\) on \([\tau,T_{\max})\) without any pointwise estimate for \(T\).

Second, the base pair
\[
Z=\nabla U,\qquad H=\nabla^2\chi
\]
does not close from the displayed schematic terms alone. Testing the source
\[
\chi\nabla^3\chi*U
\]
against \(|Z|^{p-2}Z\) and integrating one derivative away from \(\nabla^3\chi\) produces, among other terms,
\[
\int \chi\,|H|\,|Z|^p.
\]
This expression is not controlled merely by \(\|H\|_{L^p}\) and \(\|Z\|_{L^p}\). An exact tensor cancellation with the \(\chi\nabla\chi*\nabla^2U\) terms, a weighted Sobolev estimate with staggered exponents, or a coupled cross-energy is required. Wang’s Lemma 4.11 contains the same delicate interaction, so citing its induction pattern does not replace this calculation.

Thus the shifted theorem is formulated with the right geometric variables, but its core derivative estimate remains unresolved.

## 5. Most informative next calculation

The strongest single calculation would be the full index-level \(L^p\) energy identity for
\[
(\nabla U,\nabla^2\chi)
\]
under
\[
\partial_tg=-2\operatorname{Ric}(U),\qquad
U=a(\operatorname{Rm}+G).
\]
It should retain all contractions from the normalized \(G\)-terms and isolate the combined contribution of
\[
\chi\nabla^3\chi*U,\quad
\nabla\chi*\nabla^2\chi*U,\quad
\chi\nabla^2\chi*\nabla U,\quad
\chi\nabla\chi*\nabla^2U.
\]
The decisive mathematical object is an estimate such as
\[
\frac d{dt}\mathcal E_p
+c\int_M\chi^2|Z|^{p-2}|\nabla Z|^2
\le C\bigl(1+\mathcal E_p\bigr),
\]
where \(\mathcal E_p\) is an explicitly chosen staggered-exponent energy involving \(Z\) and \(H\), and every coefficient is expressed through \(\sup|U|\), finite \(L^q\) norms of \(T\), the fixed cutoff, and the terminal bilipschitz constant. The calculation must show exactly how the term \(\int\chi|H||Z|^p\) is controlled.

That computation would determine whether the shifted extension mechanism actually closes. The normalized Yang existence argument is still unwritten, but its new term is genuinely zeroth order; the base-pair interaction is the less routine analytic obstruction.

Overall, Step 36 substantially improves the architecture and correctly separates \(Q\) from the weighted defect estimates. With the correction to (1.7), the \(K_2^\eta\) notation, the retained \(1+r^{-2}\) coefficient, and the terminal-uniform drift quantifier, its established parts are mathematically coherent. The supplied material concerns only the specified four-dimensional Ishida–LeBrun family and contains neither a proof nor a refutation of the dimension-wide Yau statement.