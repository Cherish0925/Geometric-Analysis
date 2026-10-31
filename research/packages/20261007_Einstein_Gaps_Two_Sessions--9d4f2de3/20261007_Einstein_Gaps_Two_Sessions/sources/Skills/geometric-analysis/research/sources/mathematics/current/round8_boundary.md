# Boundary holonomy and orbit shape in a two-ended Einstein connector

21 September 2026.

Consider a complete Einstein four-metric with Ric = -3g on a principal
T2 bundle over a cylinder, with two smooth conformally compact AH ends.
The action is free, isometric, preserves the ends, and extends freely
to the smooth conformal compactification. Fix the torus lattice and one
global bundle trivialization. This note gives restrictions
on the actual marked end data; it does not identify expanding sections
with shrinking cusp sections by a coordinate change.

## 1. A positive definite boundary pairing

In the notation used in the preceding rounds,

\[
 g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\quad
 \rho=\sqrt{\det G},\quad dA=f\,d\mu_\gamma,
 \quad q=\rho Gf,\quad Q=\tfrac12f^{\mathsf T}Gf.
 \tag{1}
\]

The mixed Einstein equation is dq=0. Thus q is one constant covector
on the marked torus Lie algebra, not a freely adjustable parameter at
each end. Orient the base by dt wedge dtheta, where t increases from
the negative end to the positive end. With the same circle orientation
on both ends, define the real holonomy lifts

\[
 H_\pm=\lim_{t\to\pm\infty}\int_{\{t\}\times S^1} A.
 \tag{2}
\]

These are integrals of a connection form in one global trivialization,
not just the corresponding elements of R2/Lambda.

**Proposition 1.** The matrix

\[
 C(g)=\int_B \rho^{-1}G^{-1}\,d\mu_\gamma
 \tag{3}
\]

is finite and positive definite, and the lifted end data satisfy

\[
 \boxed{\quad H_+-H_-=C(g)q,\qquad
 q\cdot(H_+-H_-)=2\int_B\rho Q\,d\mu_\gamma.\quad}
 \tag{4}
\]

Proof. On an AH end in outward geodesic coordinate r,
G=e^(2r)(G0+O(e^(-2r))) and the base area density is
e^r(b0+O(e^(-2r))). Hence the integrand in (3) is O(e^(-3r))
in a fixed marking. It is smooth on the compact middle. Its quadratic
form on every nonzero covector is everywhere positive, so its integral
is positive definite. The same decay proves convergence in (2).
Since f=rho^(-1)G^(-1)q, Stokes' theorem on successively longer cylinders
gives the first equality. Pairing with q gives the second. No inverse
injectivity-radius estimate is involved.

In particular a charged filling requires a nonzero lifted holonomy
difference, and the charge is uniquely determined by that difference
once the full interior G and gamma are fixed. This last statement is
not uniqueness of the coupled Einstein boundary problem.

If the torus coordinate cell has area C_Lambda, then the physical
energy is

\[
 2\int_M Q\,dV_g=C_\Lambda q\cdot(H_+-H_-).
 \tag{5}
\]

Finite fibre quotients multiply C_Lambda and physical energy by the
same factor. The marked base identity (4) survives unchanged in the
local torus coordinates. Consequently collapsing physical energy does
not remove the end-data restriction.

## 2. What equal boundary holonomy does and does not mean

A global gauge transformation on the cylinder has the same winding
number on its two boundary circles. It shifts H+ and H- by the same
lattice element; their real difference in (4) is gauge invariant.
If the boundary holonomies agree only as torus elements, however, then

\[
                 H_+-H_-\in\Lambda
 \tag{6}
\]

need not be zero. Independent boundary trivializations can hide this
relative winding. One must therefore specify real lifted matching, or
an equivalent relative boundary marking, to infer q=0.

For the actual Einstein cylinder, q=0 makes the action orthogonally
transitive. The complete OT cylinder is impossible even with arbitrary
smooth AH conformal infinities: its orbit-shape energy tends to zero
at both ends; the exact Bochner inequality gives sup e <= 6, whereas
a shortest invariant separator forces sup e >= 12. The full proof and
hypotheses are in [round8_global.md](round8_global.md).

**Corollary 2.** A complete free-T2 Einstein cylinder as above cannot
have equal real holonomy lifts at its two ends in a common marking.
It must have q != 0 and q dot (H+ - H-) > 0. Equality of the
torus-valued boundary holonomies alone does not yield this obstruction.

This concerns an exact Einstein filling. A small mixed Ricci residual
allows q to vary; (4) then has an interior error term. In a gauge on
a truncated cylinder D the exact identity is

\[
 2\int_D\rho Q\,d\mu_\gamma
   =\int_{\partial D}q\cdot A-\int_D dq\wedge A.
 \tag{7}
\]

Its right side is gauge invariant as a whole. A pointwise small
mixed Ricci error does not bound the second term uniformly on all
degenerating cylinders: the conversion from dq to the physical error
contains rho and G. Thus Corollary 2 is not a uniform near-Einstein
gap theorem in disguise.

## 3. The conformal-boundary sign has an elementary exact description

A free T2-invariant metric on a boundary T3 can be written

\[
 h=b(\theta)^2d\theta^2+
   G(\theta)_{ab}(d\xi^a+A^a(\theta)d\theta)
                       (d\xi^b+A^b(\theta)d\theta).
\]

Put rho=sqrt(det G), M=G/rho, and ds=b rho^(-1/2)dtheta.
The conformal representative

\[
 \widehat h=\rho^{-1}h
    =ds^2+M(s)_{ab}(d\xi^a+\widehat A^a ds)
                      (d\xi^b+\widehat A^b ds),\quad\det M=1
 \tag{8}
\]

has scalar curvature

\[
 R_{\widehat h}=-\tfrac14\operatorname{tr}
                  [(M^{-1}M_s)^2]= -\tfrac12 e(s),
 \qquad e=\tfrac12\operatorname{tr}[(M^{-1}M_s)^2].
 \tag{9}
\]

Indeed the one-dimensional connection is locally pure gauge. The
flat torus slices have second fundamental form S=(1/2)M^(-1)M_s,
mean curvature zero, and |S|^2=e/2. Their scalar Gauss identity
gives (9). It is a calculation of the full boundary metric, not an
assumption that its global holonomy vanishes.

**Proposition 3.** Its conformal Yamabe constant is zero exactly when
M is constant, and is strictly negative otherwise. If the s-circle
has length ell, then

\[
 Y([h])\le -\frac{C_\Lambda^{2/3}}{2\ell^{1/3}}
                         \int_0^\ell e(s)\,ds.
 \tag{10}
\]

For nonconstant M this is the constant test function in the
three-dimensional Yamabe functional. For constant M, (8) is flat,
possibly with helical holonomy; its Yamabe functional is nonnegative
and constants attain zero. This proves both directions.

By the known connected-boundary theorem for conformally compact
Einstein metrics with a nonnegative-Yamabe boundary component, both
shape loops M+ and M- of a hypothetical two-ended Einstein cylinder
must therefore be nonconstant. Negative boundary Yamabe sign is a
necessary end-shape condition, not evidence that the filling exists.

The external theorem used here is Cai--Galloway, *Boundaries of zero
scalar curvature in the AdS/CFT correspondence*, Theorem 1:
<https://www.math.miami.edu/~galloway/papers/zero2.pdf>.

## 4. A complete test metric that detects the relative-winding error

The lifted distinction can be tested on real metrics, not just formal
connection data. Let theta,x,y have period one and put

\[
 g=dt^2+\cosh^2t\,[d\theta^2+(dx+a(t)d\theta)^2+dy^2],
 \qquad a'(t)=c\,\operatorname{sech}^3t.
 \tag{11}
\]

This is smooth and complete on R x T3 and is AH at both ends. For
the free translations in x,y,

\[
 q=(c,0),\quad Q=\tfrac12c^2\operatorname{sech}^6t,
 \quad C(g)=\tfrac\pi2 I,\quad H_+-H_-=(\tfrac\pi2c,0).
 \tag{12}
\]

Thus choosing c=2n/pi, n a nonzero integer, gives identical
torus-valued holonomies at the two ends but nonzero charge and energy.
The mixed Einstein equation is satisfied exactly. The other Einstein
equations are not: Ric_tt+3=-Q. No Einstein filling is claimed for
this test. It refutes the inference from unlifted holonomy equality
and the Maxwell equation to q=0, which would otherwise invalidate a
global matching argument.

The test also shows why this boundary computation and the previous
spectral calculation have to retain the complete Ricci system.
Solving its mixed block is not solving the Einstein equation.

## 5. What this adds to the continuation problem

A complete Einstein extension of the charged neck must simultaneously
have nonconstant shape at both conformal boundaries, a compatible
nonzero real holonomy difference, and the low spectral mode required
by the harmonic-separator inequality. None is determined by the local
Cauchy data alone. Changing finite fibre lattices cannot eliminate
these normalized restrictions. These conditions do not yet exclude
all admissible boundary data or produce a complete filling.
