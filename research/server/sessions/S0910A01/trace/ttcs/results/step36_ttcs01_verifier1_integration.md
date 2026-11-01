# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 36,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step36_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step36_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 36 analytic-platform note for the restricted four-dimensional negative Ishida--LeBrun cutoff-flow route. Read the new note and script, A03's Step 36 Preceptor review, the Step 35 tensor identity note, and the Yang/Wang source objects. Please check: (i) whether the transported-coefficient normalized DeTurck formulation correctly pulls back to the fixed-cutoff flow and whether the linearized lower-order normalization discussion is sound; (ii) whether the quantifier separation between per-datum short-time existence, maximal-time extension, and sequence-uniform bootstrap quantities is mathematically appropriate; (iii) whether the separate global Q propagation estimate is correctly weighted and genuinely independent of J6/aE; (iv) whether the shifted-U extension target is stated without smuggling in unweighted curvature or pointwise cutoff-Hessian control; and (v) what concrete analytic calculation would most strengthen the route next. Do not treat the note as a completed proof of existence or of Yau Problem 26; identify exact hidden assumptions or equation-level gaps.

## Integrated Scientific Memo

## Step 36 verification memo: analytic-platform note and global \(Q\) bridge

The Step 36 note is a useful correction of the analytic architecture for the restricted four-dimensional negative Ishida–LeBrun cutoff-flow route. Its established parts are largely coherent: the transported DeTurck pullback is right; the per-datum / maximal-time / sequence-uniform quantifier separation is the correct logical framework; and the separate unweighted \(Q=\int |E|^{2}\) propagation is genuinely needed and weighted in the right way. It is still not a proof of short-time existence or continuation, and it does not decide Yau Problem 26. The two true analytic interfaces remain: Yang-type tame existence for the transported normalized system, and a shifted-\(U\) Wang-style extension theorem with full normalization/\(G\)-term accounting.

Below are the requested checks and exact equation-level cautions.

---

### 1. Transported-coefficient normalized DeTurck formulation

For the target fixed-cutoff normalized local flow
\[
\partial_t g=-2a(\operatorname{Ric}_g+g),\qquad a=\chi^2,
\]
the Step 36 hatted system
\[
\partial_t\widehat g
=-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{\widehat a W(\widehat g,S)}\widehat g,
\]
with
\[
\partial_t\varphi_t\circ\varphi_t^{-1}=-\widehat a W,
\qquad
\widehat a=a\circ\varphi_t^{-1},
\]
does pull back exactly to the fixed-cutoff flow. Indeed,
\[
\frac d{dt}\varphi_t^*\widehat g
=
\varphi_t^*\left(\partial_t\widehat g+
\mathcal L_{\partial_t\varphi_t\circ\varphi_t^{-1}}\widehat g\right)
=
\varphi_t^*\left(-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)\right)
=
-2a(\operatorname{Ric}_{g}+g).
\]
The coefficient transport is essential:
\[
\varphi_t^*\widehat a=a,
\]
and the gauge vector must be \(\widehat a W\), not merely \(W\) with a scalar prefactor outside the Lie derivative. The product rule gives
\[
\mathcal L_{\widehat a W}\widehat g
=
\widehat a\,\mathcal L_W\widehat g
+d\widehat a\otimes W^\flat+W^\flat\otimes d\widehat a.
\]
Thus a gauge term \(\widehat a\mathcal L_W\widehat g\) alone would leave uncancelled \(d\widehat a\)-terms and would not be the correct pulled-back equation.

This matches Yang’s Section 8 local Ricci-flow construction in substance: Yang solves a gauged system with the transported cutoff \((\chi\circ\varphi_t^{-1})^2\), then pulls back by the moving diffeomorphism. Yang’s source also makes clear that the existence proof is not ordinary strictly parabolic Schauder theory for the degenerate equation; it relies on linearized regularization plus energy/tame estimates.

#### Linearized normalization: one correction

Step 36’s schematic conclusion that normalization is lower order is right, but its displayed description of the “new normalized term” is slightly imprecise.

Linearizing
\[
-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
\]
gives
\[
-2\widehat a\,D\operatorname{Ric}_{\widehat g}[h]
-2(\delta\widehat a)(\operatorname{Ric}_{\widehat g}+\widehat g)
-2\widehat a h.
\]
Relative to Yang’s unnormalized local Ricci-flow term \(-2\widehat a\operatorname{Ric}_{\widehat g}\), the genuinely new normalization contribution is only
\[
\delta(-2\widehat a\,\widehat g)
=
-2\widehat a h-2(\delta\widehat a)\widehat g.
\]
The \(-2(\delta\widehat a)\operatorname{Ric}_{\widehat g}\) part is already present in the coefficient variation of Yang’s Ricci term. This bookkeeping correction does not change the analytic conclusion: \(\delta\widehat a\) comes from variation of the diffeomorphism/transport and is schematically \(-d\widehat a(\psi)\), so it contains no second derivatives of \(h\). The principal \(2\chi^2\Delta h\)-type part and Yang’s triangular \((h,\psi)\) structure are unchanged. But a full proof still must reproduce Yang’s tame estimates for the transported normalized coupled system, including the lower-order normalized terms and the variation of the transport equation.

The Step 36 script correctly checks the Lie-derivative product identity algebraically, but many other script entries are hard-coded structural assertions. It is useful as a consistency check, not a proof of Yang-type existence.

---

### 2. Quantifier separation

The Step 36 separation into three quantifier levels is mathematically appropriate.

1. **Per-datum short-time existence.**  
   For each fixed smooth pair \((g_0,\chi)\), one needs a smooth solution on some interval \([0,T_0(g_0,\chi))\). The time may depend on all geometry and all derivatives of this single input. It need not be uniform over the near-critical collapsing sequence.

2. **Maximal-time extension.**  
   Given one smooth solution on \([0,T_{\max})\), the goal is to exclude \(T_{\max}<\theta r^2\) using zero-order bounds plus a per-datum higher-derivative continuation theorem. Those higher-derivative constants may depend on \(\tau>0\), \(g(\tau)\), \(\chi\), and the fixed datum. They need only remain finite as \(t\uparrow T_{\max}\); they need not be sequence-uniform.

3. **Sequence-uniform downstream quantities.**  
   Curvature smoothing, terminal plateau curvature, retained volume, Sobolev comparison, metric drift, and global unweighted \(Q(t)\) must be controlled uniformly along the selected sequence.

This avoids circularity provided two missing analytic theorems are later supplied: transported normalized short-time existence, and shifted-\(U\) extension.

One quantifier should be sharpened in the maximal-time discussion. The condition
\[
\int_0^t\|aE(s)\|_\infty\,ds<\infty
\quad\text{for each }t<T_{\max}
\]
is automatic on proper compact subintervals of a smooth solution. To obtain terminal bilipschitz comparison as \(t\uparrow T_{\max}\), one needs the uniform-in-terminal-time bound
\[
\sup_{t<T_{\max}}\int_0^t\|aE(s)\|_\infty\,ds<\infty.
\]
The Step 36 Moser estimate
\[
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}
\]
does give this stronger statement up to \(\theta r^2\), since
\[
\int_0^{\theta r^2}\delta(r^2/t)^{1/3}\,dt
=
\frac32\,\delta r^2\theta^{2/3}.
\]
Likewise, for every \(\tau>0\),
\[
\|aF(t)\|_\infty\le C\gamma/t
\]
gives a finite bound for \(|U|=|a(\operatorname{Rm}+G)|\) on \([\tau,T_{\max})\), assuming bilipschitz control keeps the algebraic \(aG\)-part bounded.

---

### 3. Separate global \(Q\) propagation

The Step 36 \(Q\)-propagation mechanism is essentially correct and genuinely independent of \(J_6\) and \(\|aE\|_\infty\).

The relevant Step 35 identity is
\[
B_{\rm def}^{ij}
=
|E|^2g^{ij}+(\operatorname{tr}E)E^{ij}-2(E^2)^{ij},
\]
with
\[
|B_{\rm def}|\le C|E|^2,\qquad
|\nabla B_{\rm def}|\le C|E|\,|\nabla E|.
\]
Thus the Hessian-\(a\) term in \(Q'=\frac d{dt}\int |E|^2\) is handled by signed integration by parts:
\[
\int \nabla^2a:B_{\rm def}
=
-\int da\cdot \operatorname{div}B_{\rm def},
\]
so
\[
\left|\int \nabla^2a:B_{\rm def}\right|
\le
\varepsilon\int a|\nabla E|^2
+
C_\varepsilon\int \frac{|da|^2}{a}|E|^2.
\]
Since \(a=\chi^2\),
\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2}.
\]
This is exactly the right way to avoid pointwise control of the evolving Hessian of the cutoff. The quadratic vanishing of \(B_{\rm def}\) at \(E=0\) is crucial: there is no curvature-only or cutoff-Hessian-only source.

The resulting inequality
\[
Q_U'+cX_U
\le
C\int_U\left(\frac{|da|^2}{a}+a\right)|E|^2
+
C\int_U aF|E|^2
\]
has the right weights. The potential term closes by
\[
\int_U aF|E|^2
=
\int_U F|\chi E|^2
\le
\|F\|_{L^2(U)}\|\chi E\|_{L^4(U)}^2.
\]
In dimension four, using the local Sobolev inequality,
\[
\|\chi E\|_4^2
\le
C\mathcal S
\left(
\int_U |\nabla(\chi E)|^2+r^{-2}\int_U\chi^2|E|^2
\right)
\le
C\mathcal S(X_U+r^{-2}Q_U).
\]
With \(K_2^\eta\) controlling \(\int_{\operatorname{supp}\chi}F^2\) and
\[
\gamma=\mathcal S(K_2^\eta)^{1/2},
\]
one obtains
\[
\int_U aF|E|^2
\le
C\gamma(X_U+r^{-2}Q_U).
\]
For \(C\gamma\) small, the \(X_U\)-term is absorbed.

A few hidden assumptions/notation points should be explicit:

- The active cutoff support must sit inside the Sobolev/support region, e.g.
  \[
  \operatorname{supp}a\Subset U,
  \]
  or a buffer cutoff \(\eta\equiv1\) on \(\operatorname{supp}\chi\) must be used so that no uncontrolled boundary term appears.
- If \(K_2^\eta\) is the usual buffered energy, it should be written as
  \[
  K_2^\eta=\int_U \eta^2F^2,\qquad \eta\equiv1\text{ on }\operatorname{supp}\chi,
  \]
  rather than simply \(\int_UF^2\), unless the stronger unbuffered control is actually assumed.
- Before simplifying, the zeroth-order Gronwall coefficient is more safely
  \[
  C(1+r^{-2})Q_U
  \]
  because the inequality contains both \(\int a|E|^2\le Q_U\) and the \(r^{-2}\)-term. The displayed \(Cr^{-2}Q_U\) is valid if the chosen scale has \(r\le1\). Otherwise the global propagation should be stated as
  \[
  Q(t)\le \exp(C(1+r^{-2})t)Q(0),
  \]
  which at \(t=\theta r^2\) gives
  \[
  Q(\theta r^2)\le e^{C\theta(1+r^2)}Q(0).
  \]
  This is still sequence-uniform if selected radii have a fixed upper bound.

For macro-disjoint active supports, the estimates sum with the same coefficient. On regions where \(a=0\) in a neighborhood, the metric is stationary and so \(E=\operatorname{Ric}+g\) is stationary there. Therefore exterior \(Q\) is constant.

The independence from \(J_6\) and \(\|aE\|_\infty\) is real. Weighted quantities can miss unweighted energy near the zero set of \(a\). A scalar model already shows no functional implication:
\[
a=x^2,\qquad E\sim x^{-1}
\]
gives bounded \(aE\) and finite \(a^4E^6\) in one dimension near \(0\), while \(\int E^2\) diverges. This is not a geometric counterexample, but it correctly demonstrates the weight issue. Thus terminal calibration requiring \(Q(T)/A\to0\) must carry \(Q\) as a separate first-exit component; it cannot be recovered from \(J_6\) persistence or the \(aE\)-Moser bound.

---

### 4. Shifted-\(U\) extension target

The stated extension target is formulated in the right variables and does not explicitly smuggle in unweighted pointwise curvature or pointwise cutoff-Hessian control.

Define
\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad
U=aT.
\]
Because conventions for \(g\owedge g\) vary, the safest component formula is
\[
G_{ijkl}
=
\frac{1}{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}),
\]
with the Step 35 Ricci contraction convention; then
\[
\operatorname{Ric}(G)=g,
\qquad
\operatorname{Ric}(T)=\operatorname{Ric}+g=E,
\qquad
\operatorname{Ric}(U)=aE.
\]
Hence
\[
\partial_tg=-2\operatorname{Ric}(U),
\]
and the connection variation is
\[
\partial_t\Gamma^k_{ij}
=
-g^{k\ell}\left(
\nabla_i\operatorname{Ric}(U)_{j\ell}
+\nabla_j\operatorname{Ric}(U)_{i\ell}
-\nabla_\ell\operatorname{Ric}(U)_{ij}
\right),
\]
schematically
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U).
\]
For fixed scalar \(\chi\),
\[
\partial_t(\nabla_i\nabla_j\chi)
=
-(\partial_t\Gamma^k_{ij})\nabla_k\chi,
\]
so the cutoff Hessian evolves through \(\nabla U\), not through an uncontrolled split \(da*\operatorname{Rm}+a\nabla\operatorname{Rm}\).

This is exactly the reason the extension theorem should be written in terms of \(U=a(\operatorname{Rm}+G)\). Wang’s extension theorem for local Ricci flow assumes \(\sup|\chi^2\operatorname{Rm}|<\infty\) and then controls higher derivatives by a coupled induction involving \(\nabla(\chi^2\operatorname{Rm})\) and \(\nabla^2\chi\). The Step 36 shifted target is the normalized analogue.

However, the extension proof is not present. Two equation-level gaps remain.

#### Gap A: unweighted \(L^p\) norms of \(T\)

Step 36 mentions “previously controlled unweighted \(L^p\) norms of \(T\).” These cannot simply be assumed unless they are added as hypotheses. In Wang’s proof, an analogue of Lemma 4.10 first propagates \(\| \operatorname{Rm}\|_{L^p}\) from \(\sup|\chi^2\operatorname{Rm}|\) and cutoff control. For the shifted normalized route, one needs an explicit lemma of the form
\[
\frac d{dt}\int_M (1+|T|^2)^{p/2}
\le
C_{p,\tau,g(\tau),\chi,\sup|U|,\Lambda}
\int_M(1+|T|^2)^{p/2},
\]
on \([\tau,T_{\max})\), again using signed integration by parts for Hessian-\(a\) terms. Without this, “finite unweighted \(L^p\) norms of \(T\)” are an unproved input.

#### Gap B: base-pair closure for \((\nabla U,\nabla^2\chi)\)

The displayed troublesome terms
\[
\chi\nabla^3\chi*U,\qquad
\nabla\chi*\nabla^2\chi*U,\qquad
\chi\nabla^2\chi*\nabla U,\qquad
\chi\nabla\chi*\nabla^2U
\]
are the correct type of terms to isolate, and the proposed signed integration by parts is plausible and Wang-like. But the base estimate is not yet proved.

Testing the \(\chi\nabla^3\chi*U\) source against \(|\nabla U|^{p-2}\nabla U\) and integrating by parts can produce terms of the schematic form
\[
\int \chi\,|\nabla^2\chi|\,|\nabla U|^p,
\]
or related mixed terms. These are not automatically controlled merely from
\[
\|\nabla^2\chi\|_{L^p},\qquad \|\nabla U\|_{L^p}.
\]
One needs either a precise tensor cancellation with the \(\chi\nabla\chi*\nabla^2U\) terms, a staggered-exponent Sobolev/Volterra argument as in Wang, or a carefully chosen coupled energy with cross terms. Citing Wang’s induction pattern does not replace this calculation.

#### Gap C: normalization \(G\)-terms

The normalized shift introduces
\[
U=a(\operatorname{Rm}+G)=a\operatorname{Rm}+aG.
\]
The \(aG\) part is algebraic in \(g\), but its derivatives involve metric/connection jets and cutoff derivatives. Step 36 says all \(G\)-terms must be written through the induction; that is exactly right, but it has not been done. One must verify explicitly that differentiating \(aG\), evolving \(G\), and commuting derivatives do not introduce a new highest-order source outside the Wang-style triangle. In particular, the extension proof must show that \(\nabla^m(aG)\)-terms are controlled by bilipschitz drift, lower cutoff jets, lower \(U\)-derivatives, and already propagated \(T\)-norms, not by unweighted pointwise curvature or uncontrolled Christoffel derivatives.

Thus the shifted-\(U\) extension theorem is correctly stated as a target, but remains a genuine theorem to prove.

---

### 5. Most strengthening next analytic calculation

The most valuable next calculation is the full index-level normalized shifted-curvature evolution and base-pair energy estimate.

Concretely, derive \(\partial_tU\) for
\[
U=a(\operatorname{Rm}+G),\qquad
\partial_tg=-2\operatorname{Ric}(U),
\]
including:

1. the \(a\operatorname{Rm}\) terms corresponding to Wang’s \(\chi^2\operatorname{Rm}\) equation;
2. all \(aG\) normalization terms;
3. all derivatives of \(a=\chi^2\);
4. all connection/metric-variation terms produced by differentiating \(U\);
5. the coupled cutoff equation
   \[
   \partial_t\nabla^2\chi
   =
   -(\partial_t\Gamma)*\nabla\chi
   =
   g^{-1}*\nabla\operatorname{Ric}(U)*\nabla\chi.
   \]

Then prove or disprove closure of a base-pair estimate for
\[
Z=\nabla U,\qquad H=\nabla^2\chi.
\]
The desired output is a precise inequality of Wang/Volterra type, for \(p\) large:
\[
\frac d{dt}\mathcal E_p(Z,H)
+
c\int \chi^2 |Z|^{p-2}|\nabla Z|^2
\le
C\bigl(1+\mathcal E_p(Z,H)\bigr)
+
C\int_0^t \mathcal E_p(Z,H)(s)\,ds,
\]
or an equivalent staggered-exponent version, where every coefficient depends only on the fixed datum after \(\tau>0\), the bilipschitz constant, \(\sup|U|\), fixed cutoff geometry, and propagated finite \(L^q\)-norms of \(T\). The calculation must explicitly handle the mixed group
\[
\chi\nabla^3\chi*U
+\nabla\chi*\nabla^2\chi*U
+\chi\nabla^2\chi*\nabla U
+\chi\nabla\chi*\nabla^2U,
\]
especially any term of the form
\[
\int \chi |H||Z|^p.
\]
This is the decisive obstruction: if it closes, the shifted extension route becomes substantially credible; if it fails, the continuation platform needs a different energy or additional hypothesis.

The lowest-cost precursor is the explicit \(\partial_tU\) computation with all \(G\)-terms. It will immediately reveal whether the Step 36 schematic term list is complete.

---

### Bottom line

- **Correct/sound:** transported coefficient DeTurck pullback; need for \(\mathcal L_{\widehat aW}\); lower-order nature of normalization after correcting bookkeeping; quantifier separation; independent unweighted \(Q\)-propagation mechanism; shifted-\(U\) as the right continuation variable.

- **Needs correction/clarification:** the linearized “new normalized term” should be separated from the already-existing coefficient variation of the Ricci term; terminal metric drift needs a uniform integral up to \(T_{\max}\), not merely finite integrals on proper subintervals; \(K_2^\eta\) should be buffered precisely; the \(Q\)-Gronwall coefficient is safely \(C(1+r^{-2})\) unless \(r\le1\).

- **Still unproved:** Yang-type tame short-time existence for the transported normalized system; shifted-\(U\) continuation, starting with the \((\nabla U,\nabla^2\chi)\) base pair; propagation of unweighted \(L^p\)-norms of \(T\); full handling of \(G\)-normalization terms.

Even if these are completed, the result would only advance the restricted four-dimensional negative Ishida–LeBrun laboratory route. It would not prove or refute the full dimension-wide Yau Problem 26.