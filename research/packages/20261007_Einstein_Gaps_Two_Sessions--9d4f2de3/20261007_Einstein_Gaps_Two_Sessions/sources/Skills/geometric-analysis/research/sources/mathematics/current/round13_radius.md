# Optical receivers for spatially varying circle radius

21 September 2026.

## 1. The geometric change

Round 12 used unit-normal quotient coordinates and obtained a positive
receiver only when the circle radius was constant on each fibre. There
is a different choice of normal parameter that removes this restriction:
move the quotient surfaces with speed equal to the circle radius. The
spatial Laplacian then cancels against the lapse term in mean-curvature
variation. This gives an exact nonlinear receiver, including twist and
Ricci error, rather than a linearized identity.

Let a four-dimensional metric with a free isometric circle action be

\[
 g=b+a^2\theta^2,\qquad a>0,
\]

on a circle bundle over a three-manifold. Let \(\Sigma_s\) be closed
oriented quotient surfaces moving with normal velocity \(a\nu\), where
\(\nu\) is their unit normal for \(b\). In the resulting normal marking,

\[
 b=a(s,x)^2ds^2+h_s,\qquad
 S=\frac1{2a}h_s^{-1}\partial_s h_s,\quad H=\operatorname{tr}S.
 \tag{1}
\]

Write \(\mathcal F=d\theta=\nu^\flat\wedge\beta+B\), with \(B\)
tangential, and put

\[
 Q=|\beta|^2+\tfrac14|B|_{\rm tensor}^2\ge0,
 \qquad
 D=\operatorname{Ric}_g(U,U)-\operatorname{Ric}_g(\nu,\nu),
 \tag{2}
\]

where \(U\) is the unit circle vector and horizontal lift is understood
for \(\nu\). The squared tensor norm of a two-form is twice its squared
exterior-form norm. Neither \(a\), \(h_s\), nor \(\theta\) is required to be
constant on a surface.

## 2. Exact defect identity

**Proposition 1.** Under (1),

\[
 \boxed{\partial_s(H/a)=D-|S|^2-a^2Q.} \tag{3}
\]

To prove this, the circle-submersion formulas first give

\[
 D=-\frac{\Delta_{\Sigma}a+H\nu(a)}a
       -\operatorname{Ric}_b(\nu,\nu)+a^2Q. \tag{4}
\]

Mean curvature under normal velocity \(a\nu\), with the convention
\(\partial_sh=2a hS\), satisfies

\[
 \partial_sH=-\Delta_{\Sigma}a
       -a\bigl(\operatorname{Ric}_b(\nu,\nu)+|S|^2\bigr).
\]

Substitute (4), then use \(\partial_sa=a\nu(a)\). Both spatial
second derivatives and the term \(H\nu(a)\) cancel, proving (3).
No Einstein assumption was needed. In particular, if
\(\|\operatorname{Ric}_g-\lambda g\|_{\rm op}\le\delta\), then
\(|D|\le2\delta\), independently of the value or sign of \(\lambda\).

For each fixed point in the normal marking, (3) integrates to

\[
 \int_{s_-}^{s_+}(|S|^2+a^2Q)\,ds
  =\frac{H_-}{a_-}-\frac{H_+}{a_+}+\int_{s_-}^{s_+}D\,ds. \tag{5}
\]

This is the round-12 receiver in optical parametrization. When
\(a=a(t)\), \(dt=a\,ds\) recovers exactly the earlier formula;
when \(a\) varies spatially, it is a different foliation, not a
coordinate relabeling of the old unit-normal slices.

## 3. Marked boundary estimate, including nonuniform error

Assume that the optical normal foliation is smooth and covers the
entire collar between its two specified faces. Define

\[
 A_{\rm opt}=\sup_x\int_{s_-}^{s_+}a(s,x)^2\,ds,
\quad C_\partial=\sup_x\left(\frac{H_-}{a_-}-\frac{H_+}{a_+}\right),
\quad R_D=\sup_x\int_{s_-}^{s_+}|D(s,x)|\,ds.
\]

If the surfaces have genus at least two, their endpoint conformal
structures, with this marking, satisfy

\[
 \boxed{d_{\mathcal T}([h_-],[h_+])^2
             \le A_{\rm opt}(C_\partial+R_D).} \tag{6}
\]

Indeed, for a fixed marked tangent vector,

\[
 \left|\tfrac12\log\frac{h_+(v,v)}{h_-(v,v)}\right|
 \le\int a|S|\,ds
 \le\left(\int a^2ds\right)^{1/2}
       \left(\int|S|^2ds\right)^{1/2}.
\]

Equation (5) bounds the last factor. The endpoint metric comparison
then gives quasiconformal dilatation at most \(e^{2R}\), where
\(R^2=A_{\rm opt}(C_\partial+R_D)\), and hence (6).
If a variable domain is used, the same argument requires a common
product parameterization of the faces; stopping different normal rays
at unrelated times is not silently included.

The useful error scale is more precise than \(\delta\) times optical
length. If

\[
 |D(s,x)|\le C a(s,x)^2\eta^2,
\]

then \(R_D\le C A_{\rm opt}\eta^2\) and

\[
 d_{\mathcal T}([h_-],[h_+])^2
       \le A_{\rm opt}C_\partial+C A_{\rm opt}^2\eta^2. \tag{7}
\]

Thus an error suppressed by the square of the circle radius survives
optical integration without a factor proportional to the very long
optical length. This is the relevant interface for averaging small
nonsymmetric repairs; such an averaging estimate is a separate input,
not proved by this receiver.

For the old radius \(a_0(t)=c\cosh(kt)\), \(-L\le t\le L\),
the exact conversion gives

\[
 A_{\rm opt}=\int_{-L}^L a_0(t)\,dt
       =\frac{2a_0(L)}k\tanh(kL).
\]

The boundary-radius cancellation in the round-12 repair estimate is
therefore preserved whenever the new foliation has comparable optical
area integral and comparable endpoint radii. Establishing those
comparisons for a specific candidate is a geometric task.

## 4. Zero-flux rigidity

**Corollary 2.** Suppose the metric is Einstein, the optical foliation
spans the collar, and both face mean curvatures vanish. Then \(S=0\)
and \(\mathcal F=0\) throughout. If the fibres have genus at least two,
the metric is locally a product of two surfaces of the same negative
constant curvature.

The first claim follows pointwise from (5). It gives \(h_s=h\), while
the flat connection is locally removable. The metric becomes

\[
 h+a(s,x)^2(ds^2+d\phi^2).
\]

Its horizontal Einstein equation is

\[
 \operatorname{Ric}_h-2a^{-1}\operatorname{Hess}_h a=\lambda h.
\]

In dimension two this says that \(\operatorname{Hess}_h a\) has
zero trace-free part. Thus \(\nabla_h a\) is a conformal vector
field. A closed surface of genus at least two has no nonzero conformal
vector field: in its Riemann-surface structure such a field gives a
holomorphic section of the tangent line bundle, whose degree
\(2-2g\) is negative. Hence \(a\) is spatially constant.
The remaining Einstein equations give the stated equal-curvature
product, and Gauss--Bonnet forces \(\lambda<0\).
Flat connection holonomy is not ruled out globally.

## 5. A foliation-free stability test on one surface

One can extract a useful statement without a global optical foliation.
Let \(\Sigma\) be any closed two-sided stable minimal surface in the
quotient \((N,b)\). Its Jacobi operator is

\[
 J=\Delta_\Sigma+\operatorname{Ric}_b(\nu,\nu)+|S|^2.
\]

At \(H=0\), (4) implies

\[
 Ja=-aD+a|S|^2+a^3Q.
\]

Test stability with the actual positive function \(a|_\Sigma\), using
\(-\int aJa\ge0\). The result is

\[
 \boxed{\int_\Sigma a^2(|S|^2+a^2Q)\,d\mu
                 \le\int_\Sigma a^2D\,d\mu.} \tag{8}
\]

For an Einstein metric this forces \(S=0\) and \(\mathcal F=0\)
on the surface. This alone does not yet prove a neighborhood splits.

**Proposition 3.** If such a minimal surface is locally area minimizing,
the Einstein metric splits as the equal-negative-curvature product on
an open neighborhood, provided the surface has genus at least two.

Only a short optical normal flow is needed, which exists around any
smooth embedded two-sided surface. Starting from \(H=0\), (3) gives
\(H\le0\) for positive flow time and \(H\ge0\) for negative time.
Since \(\partial_s\operatorname{Area}(\Sigma_s)=\int aH\), the area
on either side cannot exceed the initial area. Local minimization gives
the opposite inequality. Equality forces \(H=S=Q=0\) on both sides,
and the argument of Corollary 2 completes the splitting.

These are not existence theorems for stable or minimizing surfaces.
In particular, a chosen product foliation is not automatically a
family of minimizers. The distinction between stability and local area
minimization is essential in the neighborhood claim.

The static-potential/minimal-surface method has classical antecedents;
see Huang--Martin--Miao, *Static potentials and area minimizing
hypersurfaces*, [arXiv:1706.03734](https://arxiv.org/abs/1706.03734),
Lemma 4, Proposition 5, and Lemma B.6. Their Lemma 4 uses the static
potential in the stability inequality, and the proof of Proposition 5
uses its inverse-square conformal metric for the normal flow. That
proposition has an additional scalar-flat hypothesis and a different
Ricci-flat conclusion. The present direct calculation retains the
circle-connection energy and the Ricci-error term, while the
genus-at-least-two Einstein conclusion is the negative product.
No priority claim for the underlying static-flow method is made.

## 6. What this changes in the repair problem

The pointwise spatial-radius Laplacian in the old unit-normal receiver
is not an invariant obstruction to a signed formula. The correct
radius-speed normal flow cancels it exactly. This genuinely enlarges
the receiver to spatially varying radius and arbitrary connection.

The replacement hypothesis is geometric: a prescribed collar must
admit the required optical normal foliation between its actual marked
faces. The optical metric is \(a^{-2}b\); the normal exponential map
can develop focal or cut points. Local existence does not prove global
coverage, and smallness in a long, collapsing collar does not by itself
supply a uniform no-focal estimate. A graph with different arrival
times also requires a new boundary comparison.

Accordingly, (6)--(7) give a precise interface for full-mode repair
analysis, not an unconditional exclusion of every small Einstein
repair. The surface test (8) and local minimizing-surface splitting
provide another route that does not require a long optical foliation.
All statements still require a free isometric circle action on the
metric to which the formulas are applied; they do not infer one for an
arbitrary Einstein metric on the closed shear manifold.

`round13_radius_check.py` independently computes the Ricci tensor from
coordinate metric jets, with nonconstant spatial radius, varying fibre
area, and electric and magnetic connection curvature. It checks (3)
for five exact rational test jets. The geometric foliation and
Teichmüller arguments above are separate proofs, not consequences of
the finite checks.
