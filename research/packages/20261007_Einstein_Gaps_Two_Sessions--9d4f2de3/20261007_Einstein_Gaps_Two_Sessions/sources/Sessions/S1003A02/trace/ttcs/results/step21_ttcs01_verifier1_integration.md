# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 21,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step21_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step21_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the actual Kotschick PDF and verify the exact Sambusetti/BCG statement relevant to a closed oriented real-hyperbolic four-manifold Y and X=Y#k CPbar. Extract the precise topological calculation showing whether an Einstein metric on X is excluded for each k>=1. Distinguish existence obstruction from any quantitative lower bound on the L2 Einstein defect or near-Einstein sequences. Also assess whether the PDF gives any result about Yamabe invariants of these blow-ups.

## Integrated Scientific Memo

# Scientific integration memo

## 1. Exact Kotschick–Sambusetti/BCG statement

Kotschick’s Theorem 1 (equation (5), p. 6) states that if a closed oriented four-manifold \(X\) admits an Einstein metric, then
\[
\chi(X)\ge \frac32|\sigma(X)|
+\frac{\lambda(X)^4}{108\pi^2},
\]
where \(\lambda(X)\) is the minimal volume entropy.

Corollary 3 (equation (14), p. 8), attributed to Sambusetti, combines this with the Besson–Courtois–Gallot degree estimate:

> If a closed oriented Einstein four-manifold \(X\) admits a map of nonzero degree \(d\) to a closed oriented real-hyperbolic four-manifold \(Y\), then
> \[
> \boxed{\chi(X)\ge \frac32|\sigma(X)|+|d|\,\chi(Y).}
> \]
> Equality can occur only if \(X\) is itself real hyperbolic.

For the hyperbolic metric \(g_0\) on \(Y\), normalized by sectional curvature \(K_{g_0}=-1\),
\[
\lambda(X)^4\ge |d|\,\lambda(Y)^4
=|d|\,3^4\operatorname{Vol}(Y,g_0).
\]
The proof on p. 9 prints \(d\) rather than \(|d|\), whereas the corollary correctly states \(|d|\). One may reverse the orientation to make the degree positive; in the connected-sum application below the relevant degree is already \(d=1\).

Since \(Y\) has \(s=-12\), \(W=0\), and \(\operatorname{Ric}_0=0\), Gauss–Bonnet gives
\[
\chi(Y)
=\frac1{8\pi^2}\int_Y\frac{s^2}{24}\,d\mu
=\frac{3}{4\pi^2}\operatorname{Vol}(Y,g_0),
\]
and hence
\[
\operatorname{Vol}(Y,g_0)=\frac{4\pi^2}{3}\chi(Y).
\]
Therefore
\[
3^4\operatorname{Vol}(Y,g_0)
=81\cdot\frac{4\pi^2}{3}\chi(Y)
=108\pi^2\chi(Y),
\]
which produces precisely the final term in (14).

## 2. Application to \(X=Y\#k\overline{\mathbb{CP}}^{\,2}\)

There is a canonical pinch map
\[
p:Y\#k\overline{\mathbb{CP}}^{\,2}\longrightarrow Y
\]
which collapses the \(\overline{\mathbb{CP}}^{\,2}\) summands to points. With compatible orientations,
\[
\deg p=1.
\]

A real-hyperbolic four-manifold is conformally flat, so \(W^\pm=0\). The signature formula therefore gives
\[
\sigma(Y)=0.
\]
For \(\overline{\mathbb{CP}}^{\,2}\),
\[
\chi(\overline{\mathbb{CP}}^{\,2})=3,
\qquad
\sigma(\overline{\mathbb{CP}}^{\,2})=-1.
\]
Using
\[
\chi(M\#N)=\chi(M)+\chi(N)-2
\]
and signature additivity,
\[
\boxed{\chi(X)=\chi(Y)+k,\qquad \sigma(X)=-k.}
\]

If \(X\) admitted an Einstein metric, Corollary 3 with \(d=1\) would imply
\[
\chi(Y)+k
\ge \frac32k+\chi(Y).
\]
After cancelling \(\chi(Y)\),
\[
k\ge\frac32k,
\]
which is impossible whenever \(k>0\). Equivalently, the left side of the required inequality falls short by exactly
\[
\chi(X)-\frac32|\sigma(X)|-\chi(Y)
=-\frac{k}{2}.
\]

Thus the exact conclusion is
\[
\boxed{
Y\#k\overline{\mathbb{CP}}^{\,2}
\text{ admits no Einstein metric for every }k\ge1.
}
\]

For \(k=0\), \(X=Y\) carries its hyperbolic Einstein metric and realizes equality.

This is strictly stronger than the ordinary Hitchin–Thorpe obstruction. Hitchin–Thorpe alone gives
\[
\chi(Y)+k\ge\frac32k
\quad\Longleftrightarrow\quad
k\le 2\chi(Y),
\]
so it rules out only \(k>2\chi(Y)\). The BCG entropy term excludes the entire remaining range \(1\le k\le2\chi(Y)\).

There is also an exact entropy observation. Connected sum with simply connected \(\overline{\mathbb{CP}}^{\,2}\) does not change \(\pi_1\), and the classifying images of the fundamental classes agree. By Brunnbauer’s homological invariance result quoted by Kotschick,
\[
\lambda(X)=\lambda(Y),
\qquad
\lambda(X)^4=108\pi^2\chi(Y).
\]
This strengthens the degree-one lower bound to equality for the minimal entropy itself, although that strengthening is unnecessary for the Einstein obstruction.

## 3. What the paper does—and does not—say about an \(L^2\) Einstein defect

The Sambusetti/BCG conclusion is an **exact existence obstruction**. It does not by itself prove that all metrics remain a uniform positive \(L^2\)-distance from the Einstein equation.

For an arbitrary metric \(g\), Kotschick’s curvature conventions give
\[
8\pi^2\chi(X)
=\int_X\left(
\frac{s_g^2}{24}+|W_g|^2-|\operatorname{Ric}_{0,g}|^2
\right)d\mu_g.
\]
Thus
\[
\int_X|\operatorname{Ric}_{0,g}|^2\,d\mu_g
=
\frac1{24}\int_Xs_g^2\,d\mu_g
+\int_X|W_g|^2\,d\mu_g
-8\pi^2\chi(X).
\]
The signature formula implies
\[
\int_X|W_g|^2\,d\mu_g
\ge
\left|\int_X(|W_g^+|^2-|W_g^-|^2)\,d\mu_g\right|
=12\pi^2|\sigma(X)|.
\]
Consequently,
\[
\int_X|\operatorname{Ric}_{0,g}|^2\,d\mu_g
\ge
\frac1{24}\int_Xs_g^2\,d\mu_g
+12\pi^2|\sigma(X)|-8\pi^2\chi(X).
\]
For \(X=Y\#k\overline{\mathbb{CP}}^{\,2}\), this becomes
\[
\boxed{
\int_X|\operatorname{Ric}_{0,g}|^2\,d\mu_g
\ge
\frac1{24}\int_Xs_g^2\,d\mu_g
+4\pi^2k-8\pi^2\chi(Y).
}
\]

Discarding the nonnegative scalar-curvature term yields the unconditional bound
\[
\boxed{
\int_X|\operatorname{Ric}_{0,g}|^2\,d\mu_g
\ge 4\pi^2\bigl(k-2\chi(Y)\bigr).
}
\]
This is a genuine positive, scale-invariant \(L^2\) lower bound when
\[
k>2\chi(Y),
\]
but it is merely the quantitative form of the ordinary Hitchin–Thorpe obstruction. It gives nothing positive for \(1\le k\le2\chi(Y)\).

To obtain a positive bound throughout the range \(k\ge1\), one would need additional scalar-curvature information. In particular, if one could prove for every metric on \(X\) that
\[
\int_Xs_g^2\,d\mu_g\ge192\pi^2\chi(Y),
\]
then substitution would give
\[
\int_X|\operatorname{Ric}_{0,g}|^2\,d\mu_g
\ge4\pi^2k.
\]
The constant \(192\pi^2\chi(Y)\) is exactly the scalar-curvature energy of the curvature-\(-1\) hyperbolic metric:
\[
\int_Ys_{g_0}^2\,d\mu_{g_0}
=144\operatorname{Vol}(Y,g_0)
=192\pi^2\chi(Y).
\]

Kotschick’s entropy proof does **not** establish this estimate for arbitrary metrics. Its crucial volume-entropy comparison is applied only after the Einstein metric has been rescaled so that
\[
\operatorname{Ric}_g=-\frac13g.
\]
That pointwise Ricci normalization allows Bishop comparison and gives
\[
\lambda(X,g)\le1.
\]
There is no argument in the paper converting small
\[
\int|\operatorname{Ric}_0|^2
\]
into an analogous pointwise Ricci lower bound or into a uniform lower bound for \(\int s^2\).

Accordingly:

* the PDF proves nonexistence of exact Einstein metrics for every \(k\ge1\);
* it gives an unconditional positive \(L^2\)-trace-free-Ricci gap only for \(k>2\chi(Y)\), via the raw Chern–Weil identities;
* it does not prove a positive \(L^2\) gap for \(1\le k\le2\chi(Y)\);
* it does not rule out or construct degenerating sequences with
  \[
  \int_X|\operatorname{Ric}_{0,g_j}|^2\,d\mu_{g_j}\to0;
  \]
* the Ledrappier–Wang theorem invoked in the equality case is an exact rigidity theorem under the Einstein/Ricci normalization, not a quantitative almost-rigidity theorem for near-Einstein metrics.

Thus the numerical deficit \(k/2\) in Corollary 3 must not be automatically interpreted as an \(L^2\) defect lower bound. Such an interpretation requires independent scalar-curvature or compactness input.

## 4. Yamabe invariants

The PDF contains no theorem computing or estimating the Yamabe invariant of
\[
Y\#k\overline{\mathbb{CP}}^{\,2}.
\]
Indeed, it neither defines the Yamabe invariant nor states a connected-sum or blow-up formula for it.

Section 5 does contain the monopole-class estimate
\[
c^2\le\frac1{32\pi^2}\int s_g^2\,d\mu_g,
\]
but it is applied to different manifolds,
\[
Y_k=Z_k\#(1+k)(S^1\times S^3),
\]
where \(Z_k\) is a symplectic manifold homeomorphic to \(k(S^2\times S^2)\). These \(Y_k\) are unrelated to the real-hyperbolic manifold \(Y\) and its \(\overline{\mathbb{CP}}^{\,2}\)-blow-ups. The purpose there is to obstruct collapse with bounded scalar curvature and establish positive minimal volume, not to determine a Yamabe invariant.

For context only—not as a result of this PDF—if \(\mathcal Y(X)\le0\), then the desired scalar-energy estimate would correspond to
\[
|\mathcal Y(X)|^2\ge192\pi^2\chi(Y),
\]
or equivalently
\[
\mathcal Y(X)\le-\sqrt{192\pi^2\chi(Y)}.
\]
No such assertion for these hyperbolic blow-ups appears in Kotschick’s paper.

## Conclusion

The source establishes the sharp topological obstruction
\[
\chi(X)\ge\frac32|\sigma(X)|+|d|\chi(Y)
\]
for an Einstein four-manifold mapping with nonzero degree to a real-hyperbolic four-manifold. Applied to the degree-one pinch map
\[
Y\#k\overline{\mathbb{CP}}^{\,2}\to Y,
\]
the identities
\[
\chi=\chi(Y)+k,\qquad \sigma=-k
\]
violate the required inequality by \(k/2\). Hence no Einstein metric exists for any \(k\ge1\).

That conclusion is not, within this PDF, a uniform quantitative \(L^2\) Einstein-gap theorem and does not settle near-Einstein degenerations in the range \(1\le k\le2\chi(Y)\). Nor does the paper provide a Yamabe-invariant result for these blow-ups.