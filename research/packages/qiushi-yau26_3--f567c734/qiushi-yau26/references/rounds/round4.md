# Yau26: integral rigidity and nonlinear global matching

20 September 2026.

The central improvement in this round is an integral rigidity theorem:
the selected monopole families have a uniform near-critical Ricci-energy
gap without any pointwise curvature assumption. On the construction side,
the exact noncompact Einstein family acquires a nonlinear conserved-charge
law. This also gives a precise obstruction to inserting that family
unchanged into a closed Einstein metric. A separate connector argument
excludes full-matrix homogeneous Nil models and clarifies why radial twist
alone cannot complete the remaining torus connector.

These are results about specified four-dimensional families and models.
The dimension-only Yau26 existence statement, and a counterexample
defeating both signs in one dimension, remain unresolved.

## 1. From pointwise pinching to integral rigidity

Let X be a closed minimal complex surface of general type with b+(X)>1,
A=c1(X)^2>0, and let M=X#k CPbar^2. For any smooth Riemannian metric set

\[
 \mathcal E(g)=\inf_{\lambda\ne0}
 \frac{\int_M|\operatorname{Ric}_g-\lambda g|_g^2\,dV_g}
 {\lambda^2\operatorname{Vol}_g(M)}.
\]

The [integral monopole theorem](round4_rigidity.md) and its
[all-sign corollary](round4_all_sign_gap.md) yield

\[
 \boxed{\mathcal E(g)+\left(\frac13-\frac{k}{A}\right)_+
                 \ge c_*>0,}
\tag{1}
\]

with one constant independent of X,k,g. No pointwise scalar or Ricci bound,
curvature derivative, diameter, volume lower bound, Sobolev constant,
injectivity radius or Euler/A bound is imposed. The constant is existential,
not optimized.

The functional has the exact expression

\[
 \mathcal E(g)=
 \frac{4\int|\operatorname{Ric}^{\circ}|^2
             +\int(s-\bar s)^2}{\int|\operatorname{Ric}|^2},
 \qquad \bar s=\frac{\int s}{\operatorname{Vol}(M)}.
\tag{2}
\]

The denominator is nonzero under the monopole hypothesis. Thus (1) is an
obstruction in curvature energy, even when the error concentrates and no
pointwise bound is available. It excludes the near-critical band of these
topologies as sources of arbitrarily tight normalized Ricci input for
either sign. The substantive new analytic argument concerns the negative
sign; the positive integral bound follows from classical scalar monopole
and Chern--Weil estimates.

### The mechanism that removes pointwise control

Set q=-s+sqrt(6)|W+|. The previous rescaling f=sqrt(q) controlled a spinor
only under a pointwise scalar bound. Replace it by smooth majorants of

\[
 f_0=\max\left\{\sqrt{\max(q,3)},\frac{(-s)_+}{4}\right\}.
\]

The rescaled monopole solution then satisfies |Phi|^2<=4. The additional
weight cost is bounded by a constant times (s+4)^2. Comparing the actual
curvature moment with an ideal moment using Q=max(q,3) preserves the
near-equality information without requiring a fourth-power weight bound.

For a bounded bundle section u, covariant integration by parts gives

\[
 \|\nabla^2u\|_2^2\le2\|\nabla^*\nabla u\|_2^2
 +32\|u\|_\infty^2\|\operatorname{Ric}\|_2^2
 +33\|u\|_\infty^2\|F\|_2^2.
\tag{3}
\]

The positive-spinor connection has the required integral curvature budget
without any W-minus bound. Consequently the weak Bianchi source may be
tested against itself. Its upper bound tends to zero, whereas the weighted
Hodge identity retains the positive calibrated value 1/16. This is the
intrinsic contradiction. It needs neither smoothing nor geometric
compactness. All scalar-positive regions are included using the signed
lowest-eigenvalue monopole estimate.

The general theorem uses an actual selected monopole class with
(a+)^2>=A and a controlled negative square. The full-sign connected-sum
families stated in the previous round also qualify. An arbitrary formal
cohomology vector does not supply this input.

## 2. A nonlinear charge law for the exact Einstein family

The preceding round constructed exact complete metrics G[z] on (R x S1)^2,
with Ric(G[z])=-G[z]. They have prescribed cylinder length and shear data.
Write their torus reduction as

\[
 G=h+H_{ab}(d\theta^a+\mathcal A^a)(d\theta^b+\mathcal A^b),
 \quad v=\sqrt{\det H},\quad F=d\mathcal A,
 \quad q=vH*_hF.
\]

The mixed Einstein equation makes q constant. The
[nonlinear charge proof](round4_construction.md) establishes the exact law

\[
 \boxed{
 \frac{\pi^2}{2}(-b_1,B_1)^T=M[z]q[z],\qquad
 M[z]=\int_{\mathbb R^2}v^{-1}H^{-1}\,dA_h>0.}
\tag{4}
\]

Here the angular order is (y,x) and the quotient orientation is dt wedge du.
The matrix is finite, analytic and positive definite. In particular a
nonzero twist transfer gives a nonzero exact charge. The proof includes
the infinite-boundary Stokes limit and its parameter derivatives; (4) is
not only a quadratic Taylor calculation.

Its boundary energy is

\[
 \mathcal E_{\rm tw}=q^TMq=q\cdot\int F>0
\]

for nonzero transfer. Its quadratic coefficient agrees with the previous
total length response, and the cubic coefficient is computed. This does
not identify individual length receiver terms with this different boundary
quantity. The full nonlinear length response and the response of the
closed exterior remain separate tasks.

## 3. Why an exact local core still cannot simply be inserted

The [exact-core argument](round4_exact_core.md) proves that a nonzero-charge
G[z] has no compact quotient of its universal cover and cannot agree on
any nonempty open set with any closed Einstein four-manifold.

Its asymptotic product faces contain fixed-radius balls on which
|nabla Rm| tends uniformly to zero. If a cocompact isometry group existed,
translating these balls into a compact set would force nabla Rm=0 on a
fixed open ball and, by analyticity, everywhere. The universal cover would
be H2 x H2. Its two-dimensional abelian Killing actions have integrable
orthogonal complements, which contradicts nonzero q. The classical
extension theorem for local isometries then rules out exact open-set
agreement with a closed Einstein manifold.

This is an obstruction to leaving the core unchanged, not to using it as
an approximation. A global Einstein solution, if it exists, must correct
the core as well as the exterior. No uniform lower bound for the size of
that correction has been established when the global geometry degenerates.

## 4. A full-matrix homogeneous connector obstruction

For a Heisenberg lattice quotient with arbitrary positive-definite orbit
matrix G(t), put

\[
 v=\sqrt{\det G},\quad \ell^2=G(Z,Z),\quad
 \mu=\ell^4/(2v^2),\quad \chi=\tfrac12\log(2\mu).
\]

If epsilon=||Ric+lambda g||_(infinity,op), the tangential Einstein equations
give an upper bound mu<=lambda/3+epsilon at an interior maximum. The
scalar constraint gives mu>=2lambda-4epsilon at a volume minimum.
Accordingly, two ends with v tending to infinity and mu tending to zero
force

\[
 \boxed{\epsilon\ge\lambda/3.}
\tag{5}
\]

The [proof](round4_global.md) retains every matrix component. Mixing of the
central direction contributes a nonnegative term and cannot evade the
obstruction. This excludes a homogeneous Nil mechanism, not all twisted
torus connectors. Nil lattices and torus lattices cannot be interchanged.

The same note shows explicitly that arbitrary purely radial torus twist,
lapse and shape data still give flat three-dimensional slices. Their
two-ended obstruction is epsilon>=lambda/2. A successful connector must
therefore use genuinely two-variable geometry or a different orbit class;
adding more radial coefficients does not fix the problem.

## 5. The remaining work that can change the global conclusion

The rigidity theorem now covers an integral, not merely pointwise, notion
of almost-Einstein geometry on the stated near-critical monopole families.
Further progress toward unrestricted Yau26 requires another family or a
mechanism not dependent on that topology. Recomputing the same critical
constants would not supply that extension.

For the surface-bundle construction, the next issue is the global receiver
and complement response on the actual closed manifold, including a
correction in the charged core. Neither the local inverse nor the exact
charge law determines that response. A possible Einstein metric elsewhere
in the space of metrics remains allowed.

For graph-manifold candidates, the full two-variable twisted connector
remains the unresolved construction problem, with physical lattice, end
data and volume constraints imposed simultaneously. The Nil and radial
obstructions specify excluded approaches without prohibiting the remaining
geometric possibilities.

Complete proofs and supporting calculations are linked above.
[Verification](round4_verification.md) records what was actually recomputed.
The public sources are mathematical inputs, not a completed priority search
for these deductions. All work is local; running systems, Sessions and the
installed Skill were left unchanged.
