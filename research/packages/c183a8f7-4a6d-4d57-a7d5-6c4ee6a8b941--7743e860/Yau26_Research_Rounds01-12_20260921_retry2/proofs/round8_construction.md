# What rank-one representations can see on the Dehn-twist surface bundle

21 September 2026.

## 1. A global result on the actual candidate

Let `E_D` be the fixed surface bundle already carrying the explicit
pointwise near-negative-Einstein metrics. Its fibre and base have genera
`p,q>=2`, and its monodromy is one nonseparating positive Dehn twist,
raised to a primitive integer-valued homomorphism on the base group.

This note determines a restriction on **every** representation of its
fundamental group into `PSL(2,R)`, not just those arising from a chosen
metric or ansatz. All such representations kill the twisting curve.
Consequently the largest product-hyperbolic representation volume is

\[
 \boxed{\quad
 \sup_{\rho:\pi_1(E_D)\to\operatorname{PSL}(2,\mathbb R)^2}
       |\operatorname{Vol}(\rho)|
 =16\pi^2(p-2)(q-1)
 =\frac{p-2}{p-1}V_0,
 \quad V_0=16\pi^2(p-1)(q-1).
 \quad}                                                     \tag{1}
\]

In particular, this representation volume is identically zero when
`p=2`, although `chi(E_D)>0` and the near-Einstein construction has
positive limiting volume `V0`.

A parallel group argument proves:

> Every continuous map from `E_D` to a closed oriented four-manifold
> of strictly negative sectional curvature has degree zero, for all
> `p,q>=2`.

The previous entropy estimate in the long manuscript proved this
vanishing for real-hyperbolic targets only in the smallest-genus case.
The argument below removes the genus restriction and includes complex
hyperbolic and other negatively curved targets. It does not require
an Einstein assumption on the source metric.

These results close specific proposed global methods: ordinary
nonzero-degree entropy bounds with negatively curved targets have no
target on this candidate, and the actual vertical Euler class cannot
be replaced by the Euler class of a `PSL(2,R)` representation. They do
**not** exclude an arbitrary Einstein metric on `E_D`. An Einstein
metric is not known to supply either the forbidden representation or
a nonzero-degree map of the above kind.

## 2. The based Dehn-twist presentation

Write the fibre group as

\[
 \Pi_p=\langle a,b,a_2,b_2,\ldots,a_p,b_p\mid
                 [a,b]\prod_{i=2}^p[a_i,b_i]=1\rangle.
                                                               \tag{2}
\]

Choose the base point outside the twist support and the usual based
generators so that its induced automorphism is

\[
 D(a)=a,\qquad D(b)=ba,\qquad
 D(a_i)=a_i,\quad D(b_i)=b_i\quad (i\ge2).                  \tag{3}
\]

Indeed `[a,ba]=[a,b]`, so (3) preserves the surface relator. Reversing
the twist changes `a` to `a^{-1}` in the second formula and does not
change any conclusion below.

The actual bundle has a section and

\[
 G=\pi_1(E_D)=\Pi_p\rtimes_{D^{u(\cdot)}}\Pi_q,
 \qquad u:\Pi_q\twoheadrightarrow\mathbb Z.                \tag{4}
\]

Choose `t in Pi_q` with `u(t)=1`. Then

\[
 tat^{-1}=a,\quad tbt^{-1}=ba,\quad
 ta_it^{-1}=a_i,\quad tb_it^{-1}=b_i\quad(i\ge2).           \tag{5}
\]

No assumption that the whole base group is cyclic is used.
These are the actual hypotheses of the fixed candidate, not added
conditions on its metrics: see `research/20260912.tex`,
`BUNTOP:object` and `BUNTOP:group`, and
`research/20260916_global.tex`, `sec:bundle-input`. The fixed point
outside the twist support supplies the section; the original
homomorphism `u` is explicitly primitive and surjective.

## 3. The curve-killing lemma

**Lemma 1.** Let `H` be a group in which the centralizer of every
nonidentity element is abelian. Every homomorphism `phi:G -> H`
sends `a` to the identity.

**Proof.** Use capital letters for the images of the generators. If
`T=1`, the relation `T B T^{-1}=B A` gives `A=1`.
Suppose `T!=1`. Equation (5) places `A,A_i,B_i`, for `i>=2`, in the
abelian group `C_H(T)`. Hence `[A_i,B_i]=1`. The surface relation
then gives `[A,B]=1`. If `A!=1`, both `T` and `B` lie in the abelian
centralizer `C_H(A)`, so they commute. Again the twist relation gives
`B=B A`, a contradiction. Thus `A=1`. QED.

Killing the normal closure of `a` makes the twist trivial and removes
the first commutator from (2). Therefore

\[
 \boxed{\quad
 G/\langle\!\langle a\rangle\!\rangle
 \cong A\times B,\qquad
 A=\Pi_{p-1}*\mathbb Z,\quad B=\Pi_q.
 \quad}                                                     \tag{6}
\]

The extra free generator in `A` is the surviving `b`. It must not be
silently discarded when describing the full representation space.
The factorization (6), rather than a dimension count or a choice of
harmonic map, is the main structural input.

Every nonidentity element of `PSL(2,R)` has an abelian centralizer:
elliptic, hyperbolic and parabolic elements have respectively the
rotation, axial-translation and horocyclic-translation centralizers.
The possible order-two elliptic element causes no exception in this
real orientation-preserving group. Thus Lemma 1 applies to all
`PSL(2,R)` representations, including nondiscrete ones.

**Power-twist distinction.** If the monodromy is `D^k`, with nonzero
integer `k`, the same proof gives `phi(a)^k=1`. It gives `phi(a)=1`
when the target is torsion-free, but not for a general `PSL(2,R)`
target. For example, send `a` to an elliptic element of order `|k|`
and all other fibre and base generators to the identity. This is an
actual representation of the power-twist group. Thus the precise
`PSL(2,R)` factorization here is for the single twist; it must not be
copied to arbitrary finite covers.

## 4. A degree-vanishing theorem with no genus restriction

**Theorem 2.** Suppose `N` is a closed oriented aspherical
four-manifold whose group `Gamma` is torsion-free and every
nonidentity element has cyclic centralizer. Every map
`f:E_D -> N` has degree zero. The same holds for the bundle with
monodromy `D^k`, for every nonzero `k`.

**Proof.** Apply Lemma 1, or its power-twist version, to `f_*`.
The homomorphism factors through (6). The two factor images commute.
If both are nontrivial, choose nontrivial `x` and `y` in the respective
images. Each image centralizes a nontrivial element of the other.
Their two cyclic centralizers coincide: if `y=z^r` belongs to the
cyclic centralizer `<z>` of `x`, the cyclic centralizer of `y`
contains `z`, and every element of it then commutes with `x`.
Consequently the entire image lies in one cyclic subgroup.

If one factor image is trivial, the homomorphism factors through
`A` or `B`. Classifying spaces of these groups can be chosen as
`Sigma_{p-1} vee S1` and `Sigma_q`, both of dimension two. In the
first case above it factors through a circle. Since `E_D` and `N`
are aspherical, these group factorizations give homotopy
factorizations of `f` through the corresponding classifying spaces.
All induce the zero map in degree-four homology. Hence `deg f=0`.
QED.

For a closed negatively curved target, the centralizer hypothesis
also has a direct geometric proof. A nontrivial deck transformation
has a unique invariant geodesic axis. Every commuting transformation
preserves this axis and its orientation. Translation distance on the
axis embeds its centralizer into `R`; the kernel fixes points and is
trivial, while proper discontinuity makes the image discrete. The
centralizer is therefore infinite cyclic. Hadamard's theorem makes
the target aspherical.

The same group hypothesis holds for torsion-free hyperbolic groups.
The relationship between centralizers, product factorizations, and
nonzero-degree maps is classical; see [Kotschick--Löh,
*Fundamental classes not representable by products*, Section 3 and
Proposition 3.6](https://loeh.app.uni-regensburg.de/preprints/products.pdf).
The specific Dehn-twist factorization (6) is the calculation used here.

Thus no ordinary nonzero-degree Besson--Courtois--Gallot argument
from this source to a closed real-hyperbolic four-manifold is available,
regardless of `p,q`. This does not make entropy itself zero and says
nothing about unproved orbifold-degree variants or more general
metric inequalities not obtained from such a map.

## 5. Sharp Euler-product and representation-volume bounds

The quotient map (6) is realized by a map

\[
 r:E_D\longrightarrow
       (\Sigma_{p-1}\vee S^1)\times\Sigma_q.
\]

Let `alpha` be the pullback of the integral generator of
`H^2(Sigma_{p-1} vee S1;Z)` and `beta` the pullback of the oriented
base generator. The first map has degree one on the fibre after
pinching the twisting nonseparating loop, so

\[
 \alpha^2=\beta^2=0,\qquad
                    \langle\alpha\beta,[E_D]\rangle=1.    \tag{7}
\]

These formulas retain the unnormalized integral generators. In
particular `beta` is not itself the Euler class of the base tangent
bundle, which is `(2-2q)beta`.

For a representation `phi:G -> PSL(2,R)`, let `e(phi)` denote the
Euler class of its boundary-circle action, viewed in real cohomology.
After (6), the two factor images commute. If both images are
nontrivial, their union is contained in one of the abelian
centralizers described above. Such an image has zero real Euler
class: the hyperbolic or parabolic case has a common boundary fixed
point, while the elliptic case is a flat rotation bundle and has
zero real Chern class. Otherwise the representation factors through
one of the two factors. It follows that every nonzero real Euler
class has one of the forms

\[
 e(\phi)=k\alpha,\quad |k|\le2p-4,
 \qquad\text{or}\qquad
 e(\phi)=l\beta,\quad |l|\le2q-2.                          \tag{8}
\]

For `p=2` the first bound is zero: a representation of the remaining
torus group has zero Euler number. For higher genus the bounds are
the classical Milnor--Wood inequalities; the fibre-side Euler class
restricts to the genus `p-1` factor of the wedge. The extra circle
adds no second cohomology.

The primary reference [Goldman, *Topological components of spaces
of representations*, Introduction and Sections 2--3](https://www.math.umd.edu/~wmg/TopologicalComponents.pdf) states the
Euler interval and its extremal Fuchsian representations. No new
version of Milnor--Wood is asserted here.

**Theorem 3.** For any two representations `phi_1,phi_2` of `G`
into `PSL(2,R)`,

\[
 \left|\langle e(\phi_1)e(\phi_2),[E_D]\rangle\right|
                      \le(2p-4)(2q-2).                    \tag{9}
\]

The bound is attained. For `p>=3`, compose the quotient with the
map killing the extra free circle, then choose Fuchsian
representations of `Pi_{p-1}` and `Pi_q`. Their Euler classes are
the two extremal multiples in (8), and (7) proves equality. For
`p=2` both sides of (9) are zero.

The cohomology class of the curvature-minus-one area form on each
hyperbolic plane is `-2 pi e`. Hence the invariant product volume
of `rho=(phi_1,phi_2)` is

\[
 \operatorname{Vol}(\rho)
       =4\pi^2\langle e(\phi_1)e(\phi_2),[E_D]\rangle.
                                                               \tag{10}
\]

This can equivalently be defined by any equivariant map of the
universal cover into `H2 times H2`; the target is contractible and
the integral is independent of that map. Equations (9)--(10) prove
(1). This is the connected factor-preserving isometry group, not
an assertion about representations with factor permutations.

The sharpness construction is the representation-theoretic form of
the degree-one map to `Sigma_{p-1} times Sigma_q` already present
in the old manuscript. The new statement here is the upper bound
for **all** representations of the actual group, not rediscovery
of that one map.

## 6. The vertical Euler class is genuinely nonlinear holonomy

The actual vertical tangent Euler class satisfies

\[
 \langle e_V,[\Sigma_p]\rangle=2-2p,
 \qquad
 \langle e_V e_B,[E_D]\rangle
        =\chi(E_D)=4(p-1)(q-1).                            \tag{11}
\]

It cannot be the Euler class of any `PSL(2,R)` representation of
`G`: its fibre restriction exceeds (8) in absolute value by two.
Nor can two such representations jointly reproduce the pairing in
(11); their maximum misses it by exactly `4(q-1)`.

There nevertheless is a natural action of `G` on the circle at
infinity of the fibre group. The fibre acts by its inner
automorphisms and the base acts by the boundary extension of the
Dehn twist. This is an action by orientation-preserving circle
homeomorphisms, not generally by Möbius transformations. The
associated Euler class is the vertical Euler class; this is the
standard flat-circle description used by Morita. An explicit
account is given in [Bucher--Campagnolo, *Surface bundles over
surfaces: new inequalities between signature, simplicial volume
and Euler characteristic*, Section 2.3](https://link.springer.com/article/10.1007/s10711-020-00570-2).

Consequently a bounded Euler class, or extremal Euler number on
each fibre, does not automatically supply a reductive linear
representation to which a target-symmetric-space harmonic-map or
Toledo rigidity theorem can be applied. The boundary-circle action
retains information that every `PSL(2,R)` representation of this
group discards: its twisting loop acts nontrivially in the fibre
Fuchsian subgroup but is killed by every representation in Lemma 1.

This is also consistent with the harmonic-map discussion in the
Skill. Maps to the hyperbolic base use the representation factoring
through `B`, whose Euler class has zero fibre restriction. Neither
harmonicity nor choosing an optimal target recovers the missing
vertical representation or forces a product splitting.

## 7. What remains to prove for Yau26

The established near-Einstein sequence on `E_D` remains unchanged.
These calculations are global statements about that same smooth
object, but they do not exclude negative Einstein metrics with
nonparallel curvature. The known monopole argument already
excludes nonnegative Einstein constants; the remaining negative
case is not settled by (1), (9), or (11).

In particular, an arbitrary Einstein metric does not define a flat
`PSL(2,R)^2` holonomy representation. Its Levi-Civita connection has
curvature, and the Einstein equation is not a flatness equation.
Thus the missing mathematical implication cannot be supplied by
renaming the vertical circle action as a Fuchsian representation.

A successful use of this result would require an additional,
independently proved implication from an Einstein metric to the
specific representation or splitting now excluded. Alternatively,
one must use an invariant or analytic mechanism not limited to
these rank-one representations and degree maps. No such new
implication is established here.

For the non-Abelian-monopole direction, this does give a concrete
obstruction to a proposed locally symmetric conclusion. Complex
hyperbolic geometry is excluded by Theorem 2 applied to a
diffeomorphism to the hypothetical locally symmetric target. A
factor-preserving, orientation-preserving product-hyperbolic
holonomy on this exact group is excluded by Lemma 1: its two
projections both kill the nontrivial fibre loop `a`, so the holonomy
cannot be faithful. If factors or orientations are permuted, one
must pass to a finite cover; Lemma 1 must not then be invoked with
the unchanged primitive single-twist presentation. The established
absence of nonpositive-curvature metrics on `E_D`, already treated
in the Skill, handles that remaining locally symmetric case.
None of these exclusions constructs the rank-two monopole solution
needed to obtain a locally symmetric conclusion from a general
Einstein metric.

Equation (1) is a representation-volume calculation, not a bound
on the volume of every Einstein metric. No general entropy-degree
theorem for `H2 times H2` is assumed: the low-dimensional factors
are excluded in several otherwise applicable degree theorems.

The arguments use classical group and Euler-class facts to derive
specific restrictions for `E_D`; field-wide novelty is not claimed.
The checker verifies presentation identities, the cohomological
arithmetic, sharp constants, and the necessity of two scope
restrictions. It is not a formal proof of the group theorem or a
verification of general Einstein nonexistence.
