# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/ENTROPIES-VOLUMES-AND-EINSTEIN-METRICS--0ee1eb110f9d--94203f883336/originals/ENTROPIES__VOLUMES__AND_EINSTEIN_METRICS.pdf"
  ]
}
```

## Task

Read the actual Kotschick PDF and verify the exact Sambusetti/BCG statement relevant to a closed oriented real-hyperbolic four-manifold Y and X=Y#k CPbar. Extract the precise topological calculation showing whether an Einstein metric on X is excluded for each k>=1. Distinguish existence obstruction from any quantitative lower bound on the L2 Einstein defect or near-Einstein sequences. Also assess whether the PDF gives any result about Yamabe invariants of these blow-ups.

## Output

## Scientific memo

### 1. Exact Kotschick–Sambusetti/BCG statement

Kotschick’s Theorem 1, equation (5) on printed page 6, states that every closed oriented Einstein four-manifold \(X\) satisfies
\[
\chi(X)\ge \frac32|\sigma(X)|+\frac{1}{108\pi^2}\lambda(X)^4,
\]
where \(\lambda(X)\) is the minimal volume entropy.

Corollary 3, equation (14) on printed page 8, specializes this using Besson–Courtois–Gallot:

> If \(X\) admits a map of nonzero degree \(d\) to a closed oriented real-hyperbolic four-manifold \(Y\), then an Einstein metric on \(X\) would require
> \[
> \chi(X)\ge \frac32|\sigma(X)|+|d|\,\chi(Y).
> \]
> Equality can occur only when \(X\) is itself real-hyperbolic.

The constants are verified on printed page 9. For the hyperbolic metric \(g_0\) normalized by \(K_{g_0}=-1\),
\[
\lambda(X)^4\ge |d|\,\lambda(Y)^4
   =|d|\,3^4\operatorname{Vol}(Y,g_0).
\]
The corollary prints \(|d|\); the proof line prints \(d\), which is harmless after choosing orientation, and in the present application \(d=1\).

For a real-hyperbolic four-manifold,
\[
\operatorname{Vol}(Y,g_0)=\frac{4\pi^2}{3}\chi(Y),
\]
so
\[
3^4\operatorname{Vol}(Y,g_0)
=81\frac{4\pi^2}{3}\chi(Y)
=108\pi^2\chi(Y).
\]
Consequently,
\[
\frac{\lambda(X)^4}{108\pi^2}\ge |d|\chi(Y),
\]
which is exactly the entropy contribution in Corollary 3.

### 2. Application to \(X=Y\#k\overline{\mathbb{CP}}^{\,2}\)

There is a canonical pinch map
\[
p:Y\#k\overline{\mathbb{CP}}^{\,2}\longrightarrow Y
\]
that sends the added summands to points. With compatible orientations,
\[
\deg p=1.
\]

Because a real-hyperbolic metric is conformally flat, \(W=0\). Kotschick’s signature formula (7) therefore gives
\[
\sigma(Y)=0.
\]
Also,
\[
\chi\!\left(\overline{\mathbb{CP}}^{\,2}\right)=3,
\qquad
\sigma\!\left(\overline{\mathbb{CP}}^{\,2}\right)=-1.
\]
Using
\[
\chi(M\#N)=\chi(M)+\chi(N)-2
\]
and additivity of the signature,
\[
\chi(X)=\chi(Y)+k,
\qquad
\sigma(X)=-k,
\qquad
|\sigma(X)|=k.
\]

If \(X\) admitted an Einstein metric, Corollary 3 with \(d=1\) would give
\[
\chi(Y)+k
=\chi(X)
\ge \frac32|\sigma(X)|+\chi(Y)
=\frac32k+\chi(Y).
\]
After cancelling \(\chi(Y)\),
\[
k\ge \frac32k,
\]
equivalently \(0\ge k/2\). This is impossible for every \(k\ge1\).

Thus the PDF gives the precise conclusion
\[
\boxed{Y\#k\overline{\mathbb{CP}}^{\,2}\ \text{admits no Einstein metric for every }k\ge1.}
\]
For \(k=0\), equality holds and the original hyperbolic metric is consistent with the equality statement.

The paper’s homological-invariance discussion also gives a sharper entropy observation. After identifying
\[
\pi_1(X)\cong\pi_1(Y),
\]
the classifying images of the fundamental classes agree because the simply connected added summands map trivially to \(B\pi_1(Y)\). Brunnbauer’s result quoted on pages 3–4 and in Remark 1 therefore yields
\[
\lambda(X)=\lambda(Y).
\]
The degree-one BCG estimate is already sufficient for the Einstein obstruction.

### 3. What this does not provide for an \(L^2\) Einstein defect

The result concerns exact Einstein metrics. The proof sets the trace-free Ricci tensor
\[
E=\operatorname{Ric}_0
\]
equal to zero and then uses the constant Einstein scalar curvature together with Bishop comparison. It does not define a scale-invariant Einstein-defect functional or estimate its infimum.

For a general four-dimensional metric, the Chern–Gauss–Bonnet formula is
\[
8\pi^2\chi(X)
=
\int_X
\left(
\frac{s_g^2}{24}+|W_g|^2-\frac12|E_g|^2
\right)d\mu_g.
\]
Hence
\[
\int_X |E_g|^2\,d\mu_g
=
\frac1{12}\int_X s_g^2\,d\mu_g
+2\int_X|W_g|^2\,d\mu_g
-16\pi^2\chi(X).
\]
The signature formula gives
\[
\int_X|W_g|^2\,d\mu_g\ge 12\pi^2|\sigma(X)|,
\]
and therefore, for the present connected sum,
\[
\int_X|E_g|^2\,d\mu_g
\ge
\frac1{12}\int_Xs_g^2\,d\mu_g
-16\pi^2\chi(Y)+8\pi^2k.
\]
To turn this into a metric-independent positive estimate, one would need an additional scalar-curvature estimate such as
\[
\int_Xs_g^2\,d\mu_g\ge 192\pi^2\chi(Y)
\]
for every metric under consideration. That would yield
\[
\int_X|E_g|^2\,d\mu_g\ge8\pi^2k.
\]
Kotschick’s entropy argument does not establish this scalar-curvature estimate for arbitrary metrics. Its Bishop comparison step is used only after the Einstein equation permits the normalization
\[
\operatorname{Ric}_g=-\frac13g.
\]

Accordingly, the topological shortfall \(k/2\) in Corollary 3 is not identified in the PDF with a multiple of \(\int|E|^2\). Equations (5) and (14) alone do not determine whether
\[
\inf_g\int_X|\operatorname{Ric}_{0,g}|^2\,d\mu_g
\]
is positive, nor whether a degenerating sequence could make a chosen scale-invariant Einstein defect tend to zero. The Ledrappier–Wang result used on pages 7–8 characterizes exact entropy equality under the Einstein/Ricci normalization; no quantitative almost-equality or near-Einstein sequence theorem is supplied.

### 4. Yamabe invariants

The PDF gives no computation or estimate for the Yamabe invariant of
\[
Y\#k\overline{\mathbb{CP}}^{\,2}.
\]
It does not define the Yamabe invariant or state a blow-up formula for it.

Section 5 contains the scalar-curvature estimate
\[
c^2\le \frac1{32\pi^2}\int s_g^2\,d\mu_g
\]
for certain monopole classes on manifolds denoted there by \(Y_k\). Those \(Y_k\) are
\[
Z_k\#(1+k)(S^1\times S^3),
\]
constructed from exotic smooth structures on \(k(S^2\times S^2)\); they are unrelated to the present real-hyperbolic \(Y\) and its \(\overline{\mathbb{CP}}^{\,2}\)-blow-ups. That estimate is used to obstruct collapse with bounded scalar curvature, not to evaluate a Yamabe invariant.

Hence any Yamabe value for the hyperbolic blow-ups, and any \(L^2\) trace-free Ricci estimate derived from such a value, requires input beyond this PDF.