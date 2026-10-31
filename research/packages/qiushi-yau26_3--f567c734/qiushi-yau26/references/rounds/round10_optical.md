# A quantitative boundary-to-boundary Ricci anisotropy identity

21 September 2026.

The exact free-circle obstruction has a quantitative form. The quantity
that must accumulate is not the scalar curvature error, but a signed
vertical-minus-horizontal Ricci error, reduced further by a nonnegative
twist term. A one-dimensional ground state identifies its unavoidable
boundary cost. This gives a test for approximate connectors without
assuming a lower bound for an orbit length or conserving an approximate
charge.

## 1. Geometric assumptions

Let a compact connected smooth manifold with boundary carry a free circle
action, free also on its boundary. On its interior let an invariant metric
in dimension `n+1 >= 3` be written intrinsically as

\[
g=V^2\eta^2+h,\qquad d\eta=\pi^*F,
\]

on its principal circle quotient `N`. No global connection potential is
required. Assume the optical metric and defining function

\[
k=V^{-2}h,\qquad \Omega=V^{-1}
\tag{1}
\]

extend smoothly to the compact quotient, with `k` positive definite,
`Omega>0` inside and `Omega=0`, `dOmega!=0` on its boundary. Assume:

* the boundary of `(N,k)` is totally geodesic;
* `|dOmega|_k=1` on that boundary;
* `E=Ric_g+ng` vanishes outside a compact subset of the interior.

These assumptions hold for a smooth conformally compact connector that
is exactly normalized Einstein near each conformal end. In an invariant
geodesic compactification, the boundary first normal derivative of the
compactified metric is zero; the same is true after taking the quotient
and dividing by the squared compactified circle length. The normalization
gives the second condition. The conditions are stated explicitly rather
than inferred from a small unweighted Ricci error alone.

Suppose there are at least two conformal boundary components. Choose a pair
at minimal optical distance and a shortest unit-speed geodesic

\[
\gamma:[0,\ell]\longrightarrow\overline N.
\]

Its open segment is interior and its endpoint velocities are normal to
the boundary. To justify the interior assertion, an earlier contact with
a third component would shorten the least distance between components;
contact with an endpoint component would shorten this pair. With totally
geodesic boundary, a minimizing arc cannot leave a boundary tangentially:
the geodesic initial-value problem would keep it in that boundary.
Put `T=gamma'`, `m=n-1`, and write `Omega(s)=Omega(gamma(s))`. Then

\[
\Omega(0)=\Omega(\ell)=0,
\qquad \Omega'(0)=1,\quad\Omega'(\ell)=-1.
\tag{2}
\]

## 2. A nonnegative Neumann index operator

Parallel-transport an orthonormal basis of `T^perp` along `gamma`.
At either end it is tangent to the boundary. The sum of the `m`
second-variation inequalities for fields `f E_a`, whose endpoints may
move in the boundary, is

\[
\int_0^\ell\left[m(f')^2-R_k f^2\right]ds\ge0,
\qquad R_k=\operatorname{Ric}_k(T,T).
\tag{3}
\]

There are no second-fundamental-form endpoint terms because the boundaries
are totally geodesic. Consequently the scalar Neumann operator

\[
\mathcal A=-m\frac{d^2}{ds^2}-R_k
\tag{4}
\]

has lowest eigenvalue `lambda>=0` and a smooth strictly positive
ground state `f`, with `f'(0)=f'(ell)=0`. Its normalization is immaterial.
This is the Neumann index operator, not a Dirichlet operator: allowing
endpoint motion supplies the eventual strictly positive boundary cost.

## 3. The exact signed identity

Use the auxiliary static metric

\[
g_L=-V^2dt^2+h=\Omega^{-2}(-dt^2+k).
\]

The conformal Ricci formula evaluated on `Z=partial_t+T` gives

\[
\operatorname{Ric}_{g_L}(Z,Z)
=R_k+m\frac{\Omega''}{\Omega},
\qquad
\mathcal A\Omega=-\Omega\operatorname{Ric}_{g_L}(Z,Z).
\tag{5}
\]

Let `U` be the vertical `g`-unit circle generator and let
`X=Omega T` be the horizontal `h`-unit vector along the path. Circle
reduction, without imposing the mixed Einstein equation, gives

\[
\Omega^2\operatorname{Ric}_{g_L}(Z,Z)
= E(X,X)-E(U,U)+Q,
\tag{6}
\]
\[
Q=V^2\left(\frac14|F|_{\rm tens}^2
                  +\frac12|\iota_XF|_h^2\right)\ge0.
\tag{7}
\]

Thus for `D=E(U,U)-E(X,X)-Q`, one has `A Omega=D/Omega`.
Green's identity with the positive Neumann ground state yields

\[
\boxed{
\int_0^\ell \frac{fD}{\Omega}\,ds
=\lambda\int_0^\ell f\Omega\,ds
  +m\bigl(f(0)+f(\ell)\bigr).}
\tag{8}
\]

Indeed
`int(f A Omega-Omega A f)=-m[f Omega'-f' Omega]_0^ell`,
and (2) gives the last term. Formula (5) also shows that the integrand
is locally integrable at the boundary. Smooth exact-Einstein ends have
the usual even first-order compactification; their twist term has the
corresponding vanishing order. The compact support of `E` makes the
error estimates below immediate without assumptions about a decay rate
for an arbitrary approximate end.

In particular, somewhere along this geodesic,

\[
E(U,U)>E(X,X)+Q.
\tag{9}
\]

The exact theorem is recovered by setting `E=0`, which makes the
left side of (8) nonpositive and its right side strictly positive.
This is an entirely Riemannian index proof in the stated end-regularity
class. The more general exact proof without these extra optical
boundary assumptions is in [round9_connector.md](round9_connector.md),
using [Galloway--Schleich--Witt--Woolgar](https://arxiv.org/pdf/hep-th/9912119).

More generally (8) excludes any metric in this class for which the circle
direction is everywhere no larger in Ricci curvature than every horizontal
unit direction. This is a directional condition, not a scalar curvature
bound and not an assumption that the entire metric is Einstein.

## 4. A quantitative error-length tradeoff

Suppose `|g^{-1}E|_op<=epsilon`. Let `K` be any compact region containing
the support of `E`, and denote its trace on `gamma` by the same letter.
From (8), retaining all nonnegative terms,

\[
\boxed{
2\epsilon\int_K\frac{f}{\Omega}\,ds
\ge m(f(0)+f(\ell))
 +\lambda\int_0^\ell f\Omega\,ds
 +\int_0^\ell\frac{fQ}{\Omega}\,ds.}
\tag{10}
\]

The `h`-length spent inside the error region is
`L_K=int_K ds/Omega`. Normalize `max f=1` and define

\[
a_\gamma=f(0)+f(\ell)>0.
\]

Then every such connector satisfies

\[
\boxed{\epsilon L_K\ge\frac{n-1}{2}a_\gamma.}
\tag{11}
\]

Consequently a sequence with `epsilon->0` must have either unbounded
physical length in its error region, or a ground state whose boundary
values vanish relative to its interior maximum, or both. Twist only
increases the required cost. Formula (10) is stronger than (11), since
it also measures the positive index eigenvalue and twist along the path.

This is not a dimension-only Ricci gap: `a_gamma` has not been bounded
below uniformly over degenerating optical geometries. Nor is the compact
support assumption silently dropped. The theorem gives a precise escape
condition that a proposed small-error connector can be checked against.

In particular, suppose `|R_k|<=C` along this geodesic. The constant trial
function gives `0<=lambda<=C`; hence `f''<=a^2 f`, where
`a=sqrt(2C/m)`. From `f'(0)=0`, the scalar comparison inequality gives
`f(s)<=f(0)cosh(as)`. Apply it also from the other end. With `max f=1`,

\[
a_\gamma\ge2\operatorname{sech}\!\left(\ell\sqrt{2C/(n-1)}\right),
\]
\[
\boxed{\epsilon L_K\ge(n-1)
\operatorname{sech}\!\left(\ell\sqrt{2C/(n-1)}\right).}
\tag{12}
\]

The formula is interpreted with `sech(0)=1` when `C=0`. Thus uniformly
bounded optical length and optical Ricci curvature give an explicit
inverse-error lower bound on physical core length. If that physical
length is also bounded, there is a positive family-dependent gap. The
quantitative identity (10) does not require these auxiliary bounds.

## 5. An explicit consistency test and a limitation

On `R x T^n`, take

\[
g=dr^2+\cosh^2r\,(d\phi^2+g_{T^{n-1}}),
\]

with a flat torus metric. Put `s=arcsin(tanh r)+pi/2`. Its circle
optical metric is the flat product on `[0,pi] x T^{n-1}` and
`Omega=sin s`. Thus `R_k=0`, `lambda=0`, `f=1`, `F=0`.
The actual Ricci errors are

\[
E(\partial_r,\partial_r)=0,
\qquad E(U,U)=(n-1)\sin^2s.
\]

Accordingly `D=(n-1)sin^2s` and (8) reads
`(n-1) int_0^pi sin s ds=2(n-1)`, exactly. Its errors decay at infinity
rather than having compact support; (8) remains valid directly, and the
test checks the endpoint signs and normalizations independently of the
compact-support corollary. It is not an almost-Einstein example.

Conversely, engineering a scalar function `Omega` so that only
`-m Omega Omega''` is small does not construct a near-Einstein metric.
For a flat optical product the full conformal metric has Ricci errors

\[
E_{rr}=n\{1-(\Omega')^2+\Omega\Omega''\},
\qquad
E_{\rm tan}=n\{1-(\Omega')^2\}+\Omega\Omega''.
\tag{13}
\]

At a maximum of `Omega`, small anisotropy is compatible with a tangential
error close to `n`, not close to zero. Both error blocks must be controlled.
This explicitly prevents interpreting a long solution of the scalar
necessary condition as a solution of the complete Einstein problem.

## 6. Place in the research program

The useful outcome is a signed, quantitatively normalized diagnostic for
the remaining approximate-connector route. It distinguishes two possible
escape mechanisms, controls the effect of twist with the correct sign,
and requires no approximate conservation law. The identity alone does not
rule out these escapes. The explicit family in
[round10_kottler.md](round10_kottler.md) realizes ground-state localization:
its normalized endpoint sum is asymptotic to \(2\sqrt3d\), while its
error times physical core length tends to zero. This is a full metric
construction, not the scalar test in Section 5. A closed Yau26 counterexample
still requires a small-error global metric on an independently excluded
Einstein smooth type; neither that global construction nor the unrestricted
Yau26 conclusion follows from the identity.
