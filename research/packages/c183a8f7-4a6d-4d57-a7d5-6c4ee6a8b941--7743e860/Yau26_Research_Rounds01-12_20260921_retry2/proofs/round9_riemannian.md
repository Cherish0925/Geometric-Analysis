# A Riemannian exclusion of every nonzero-charge torus connector

21 September 2026.

This is a second proof of the charged part of the nonexistence theorem
in [round9_connector.md](round9_connector.md). It uses a stable minimal
surface in a **circle quotient**, not the invariant minimal three-torus
used in earlier rounds. The distinction changes the stability identity.

## 1. Statement

Let the interior of `[0,1] x T^3` carry a complete Einstein four-metric
`Ric_g=-3g`, smoothly conformally compact at both boundary components.
Assume a free marked isometric `T^2` action extends freely to the entire
compactification, with quotient an annulus. In the notation

\[
g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\qquad
\rho=\sqrt{\det G},\qquad dA^a=f^a\,d\mu_\gamma,
\]

the mixed Einstein equation makes `q=rho G f` a constant covector on
the marked torus Lie algebra.

**Theorem.** Such a metric cannot have `q != 0`.
Together with the charge-free exclusion in
[round8_global.md, Theorem 2.1](round8_global.md), this excludes the
entire stated free-torus class. No assumption of diagonal shape,
orthogonal transitivity, half-conformal flatness, flat infinity, or
nonnegative boundary Yamabe class is added.

## 2. Circle reduction and the global separator

After interchanging the two marked primitive circles if necessary,
assume `q_1 != 0`. Reduce along the first circle, writing

\[
g=V^2(d\xi^1+\alpha)^2+h,
\quad V^2=G_{11},\quad s=G_{12}/G_{11},
\]
\[
h=\gamma+\frac{\rho^2}{G_{11}}(d\xi^2+A^2)^2,
\qquad \alpha=A^1+s(d\xi^2+A^2).
\tag{2.1}
\]

The circle quotient is `N=(0,1) x T^2`. Its metric `h` is itself
smoothly conformally compact at both ends. Indeed for a torus-invariant
defining function `x`, the Schur complement of the positive compactified
matrix `x^2 g` is `x^2 h`, smooth and positive through the boundary.
Also `xV` extends smoothly and positively.

There is a nonempty compact, smooth, two-sided stable minimal surface
`Sigma` in `(N,h)` separating the two ends. To see this, truncate both
ends at sufficiently small defining-function levels. Their outward mean
curvatures are positive, approaching `2`: the invariant defining function
has `|dx|^2_(x^2 h)=|dx|^2_(x^2 g)->1` by the normalized Einstein
asymptotics. Minimize area in the nonzero
oriented separating homology class of the resulting compact cylinder.
Codimension-one area minimization gives a nonempty integral minimizer;
in dimension three its support is smooth. The strictly mean-convex
boundary is a barrier, so the support is interior. Any oriented
component is a compact two-sided stable minimal surface. Multiplicities
or multiple components do not affect the argument below.

This compact variational argument requires both conformal ends. It is
not an assertion that an arbitrary local Einstein neck already has
such a stable separator in its circle quotient.

## 3. The lapse is a strictly destabilizing test function

Set `F=d alpha`. Use the full tensor norm

\[
 |F|_{\rm tens}^2=\sum_{i,j}F_{ij}^2
                 =2|F|_{\Lambda^2}^2.
\]

The exact circle-reduction identities are

\[
\operatorname{Ric}_h
=-3h+V^{-1}\operatorname{Hess}_h V
       +\frac{V^2}{2}F_{ik}F_j{}^k,
\qquad
\frac{\Delta_hV}{V}=3+\frac{V^2}{4}|F|_{\rm tens}^2.
\tag{3.1}
\]

They also follow from the Riemannian submersion formulas in
[Hwang, *A note on the circle actions on Einstein manifolds*, Lemma 1](https://doi.org/10.1017/S0004972700019134).
The following cancellation is independent of the value of the Einstein
constant; the two occurrences of `3` cancel, rather than being discarded.

For a unit normal `n` to the minimal surface,
`Delta_Sigma V=Delta_h V-Hess_h V(n,n)`. Thus its Jacobi operator

\[
J_\Sigma=-\Delta_\Sigma
 -(\operatorname{Ric}_h(n,n)+|\mathrm{II}|^2)
\]

satisfies exactly

\[
\boxed{
 J_\Sigma V
 =-V\left[
 |\mathrm{II}|^2+\frac{V^2}{4}|F|_{\rm tens}^2
                    +\frac{V^2}{2}|\iota_nF|^2
       \right].}
\tag{3.2}
\]

Stability and the legitimate smooth positive test function `V|_Sigma`
therefore imply

\[
0\le\int_\Sigma VJ_\Sigma V
=-\int_\Sigma V^2\left[
 |\mathrm{II}|^2+\frac{V^2}{4}|F|_{\rm tens}^2
                    +\frac{V^2}{2}|\iota_nF|^2
       \right].
\tag{3.3}
\]

In particular `F` must vanish at every point of `Sigma`.

## 4. Conserved nonzero charge forbids that vanishing

Differentiating the actual one-form in (2.1) gives

\[
F=(f^1+s f^2)d\mu_\gamma
       +ds\wedge(d\xi^2+A^2),
\qquad
f^1+s f^2=\frac{q_1}{\rho G_{11}}.
\tag{4.1}
\]

Evaluate on the horizontal lifts of an oriented `gamma`-orthonormal
pair. The second summand vanishes on this pair, while the first is
nonzero everywhere because `q_1 != 0`, `rho>0`, and `G_11>0`.
Consequently `F` has no zero anywhere on `N`, contradicting (3.3).
This proves the theorem.

## 5. Consequences and compatibility with the earlier constructions

The analytic charged Einstein throat constructed in round 6 is still
valid. Its central **three-dimensional** hypersurface is strictly
stable in the four-metric. Here the contradiction instead uses a
globally obtained **two-dimensional** stable surface in a different
metric, the circle quotient `h`, and the test function `V`. Local
existence supplies neither this global minimizer nor two complete AH
ends. The two statements do not conflict.

For the graph-manifold program the conclusion is precise: one cannot
close the exact two-ended connector while retaining the specified free
isometric torus action, even with general connection curvature and
rotating fibre shape. This does not prohibit small-error connectors,
connectors with degenerating or singular orbits, or nonsymmetric
Einstein connectors. It does not decide the existence of any Einstein
metric on a closed graph manifold.

The proof applies classical submersion and minimal-surface tools to
the conserved charge in this problem. A literature comparison beyond
the primary sources checked here is still needed before asserting
priority for this particular consequence. The independent signature-
change argument gives a broader free-circle theorem without
the four-dimensional minimal-surface restriction.

## 6. What survives for small Ricci error

The same calculation gives an exact condition for a prospective approximate
connector. Retain the free circle and a compact stable quotient separator,
but write

\[
\operatorname{Ric}_g=-3g+E,\qquad |g^{-1}E|_{\rm op}\le\epsilon.
\]

Let `U=V^{-1} partial_phi` be the vertical unit vector and lift `n`
horizontally. The Jacobi identity becomes

\[
J_\Sigma V=-V\left[
|\mathrm{II}|^2+\frac{V^2}{4}|F|_{\rm tens}^2
+\frac{V^2}{2}|\iota_nF|^2+E(n,n)-E(U,U)\right].
\tag{6.1}
\]

In particular stability forces the weighted estimate

\[
\boxed{
\frac{\int_\Sigma V^2\left(
|\mathrm{II}|^2+V^2|F|_{\rm tens}^2/4
+V^2|\iota_nF|^2/2\right)}{\int_\Sigma V^2}
\le2\epsilon.}
\tag{6.2}
\]

Thus a vanishing-defect connector would have to make its quotient
separator nearly totally geodesic and its lapse-weighted twist small
in this precise averaged sense. The estimate is not a dimension-only
positive lower bound for `epsilon`: neither denominator nor the
weighted twist has been bounded from the other side uniformly over
degenerating connectors. Also the exact conserved charge used in
Section 4 need not survive an arbitrary mixed Ricci error. These are
specific differences between the exact no-connector theorem and the
near-Einstein construction question, not exceptions silently removed
from the original problem.
