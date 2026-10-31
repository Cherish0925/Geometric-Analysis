# A mapping-class obstruction to invariant Einstein repair

21 September 2026.

The closed metrics in round11_closed_gluing.md have Ricci defect tending
to zero on a fixed smooth manifold. This note tests exact repair, not
another reduction of that residual. It proves a uniform repair
obstruction in a specified invariant sector, using the actual marked
Teichmüller displacement and an exact nonlinear Einstein constraint.
It does not exclude arbitrary nonsymmetric Einstein metrics.

## 1. The full scalar constraint on a circle-invariant collar

Let \(F\) be a closed oriented surface of genus at least two, and let
\(I=[-L,L]\). On a principal circle bundle over \(I\times F\), consider

\[
g=b+a^2\theta^2,\qquad b=dt^2+h_t,\qquad
S=\tfrac12 h_t^{-1}\partial_t h_t,\qquad H=\operatorname{tr}S .
\tag{1}
\]

Here \(\theta\) is a connection, all data are circle invariant, and the
positive orbit radius \(a=a(t,x)\) is initially unrestricted. The
horizontal lift of \(\partial_t\) is denoted \(T\), and the unit circle
vector is \(U\). Decompose its curvature as

\[
\mathcal F=d\theta=dt\wedge\beta+B,\qquad
Q=|\beta|_{h_t}^2+\tfrac14|B|_{h_t,\mathrm{tensor}}^2\ge0.
\tag{2}
\]

The tensor convention for a two-form is
\(|B|_{\mathrm{tensor}}^2=\sum_{i,j}B_{ij}^2\); it is twice the
usual exterior-form norm squared. Define
\(D=\operatorname{Ric}(U,U)-\operatorname{Ric}(T,T)\).
The circle submersion and hypersurface formulas give the exact identity

\[
\boxed{
D=\partial_tH-\frac{\partial_ta}{a}H
       +|S|^2-\frac{\Delta_{h_t}a}{a}+a^2Q.}
\tag{3}
\]

Indeed,

\[
\begin{aligned}
\operatorname{Ric}(U,U)
 &=-\frac{a_{tt}+Ha_t+\Delta_{h_t}a}{a}
       +\frac{a^2}{4}
           (2|\beta|^2+|B|_{\mathrm{tensor}}^2),\\
\operatorname{Ric}(T,T)
 &=-H'-|S|^2-\frac{a_{tt}}a-\frac{a^2}{2}|\beta|^2 .
\end{aligned}
\tag{4}
\]

Their difference proves (3). No hyperbolicity assumption on \(h_t\),
linearization, connection flatness, or fixed fibre area is used.
If \(g\) is Einstein with any constant, then \(D=0\): the Einstein
constant cancels. The mixed Einstein equations impose additional
conditions; satisfying (3) alone is not sufficient.

## 2. A nonlinear positive receiver and its boundary flux

First impose only the additional assumption \(a=a(t)\). Then (3) becomes

\[
\left(\frac Ha\right)'
   =\frac Da-\frac{|S|^2}{a}-aQ .
\tag{5}
\]

For every \(x\in F\) separately, integration yields

\[
\boxed{
\int_{-L}^{L}
 \left(\frac{|S|^2}{a}+aQ\right)\,dt
 =\frac{H(-L,x)}{a(-L)}-\frac{H(L,x)}{a(L)}
  +\int_{-L}^{L}\frac{D(t,x)}{a(t)}\,dt .}
\tag{6}
\]

This is an exact equation, not the leading coefficient of an expansion.
For an Einstein metric the last integral is zero. In particular, if
both fibre mean curvatures vanish at the collar faces, then \(S=0\) and
\(\mathcal F=0\) throughout the collar. Arbitrary changes in the
intrinsic fibre metric or connection cannot cancel one another:
their contributions have the same sign.

There is also a precise linear interpretation. At a product solution,
the linear part of this scalar equation is \(H'-a'H/a\).
Pairing with \(a^{-1}dt\) annihilates that linear expression for
variations with vanishing face mean curvatures. The retained nonlinear
term is the nonnegative left side of (6). This identifies an actual
annihilator of the scalar constraint with those boundary conditions.
It is not asserted to be an element of the cokernel of the complete
closed, gauge-fixed Einstein operator.

## 3. Marked Teichmüller distance from the same receiver

Let

\[
I_a=\int_{-L}^{L}a(t)\,dt,\qquad
C_{\partial}=
 \left\|\frac{H(-L,\cdot)}{a(-L)}
       -\frac{H(L,\cdot)}{a(L)}\right\|_\infty .
\]

For an Einstein metric in this sector, (6) implies
\(\int |S(t,x)|^2/a(t)\,dt\le C_{\partial}\) for each \(x\).
If \(v\in T_xF\) is fixed under the product marking, then

\[
\left|\frac12\log
       \frac{h_L(v,v)}{h_{-L}(v,v)}\right|
\le \int_{-L}^{L}|S(t,x)|\,dt
\le\sqrt{I_a C_{\partial}} .
\tag{7}
\]

The first inequality follows by differentiating the logarithm of the
length of \(v\); the second is weighted Cauchy--Schwarz. Consequently

\[
e^{-2R}h_{-L}\le h_L\le e^{2R}h_{-L},
\qquad R=\sqrt{I_aC_{\partial}} .
\]

At every point the quasiconformal dilatation of the marked identity
between these two metrics is at most \(e^{2R}\): the ratio of the two
metric eigenvalues is at most \(e^{4R}\), and dilatation is its square
root. From the definition \(d_{\mathcal T}=\frac12\inf\log K\),

\[
\boxed{
d_{\mathcal T}([h_{-L}],[h_L])^2
       \le I_a C_{\partial}.}
\tag{8}
\]

The endpoint metrics need not have constant curvature; their oriented
conformal structures define their Teichmüller points. This step avoids
mistaking a removable coordinate deformation for a mapping-class
obstruction. Endpoint pullbacks by diffeomorphisms isotopic to the
identity do not change (8).

The normal product marking used here is part of the hypotheses.
A time-dependent fibre diffeomorphism introduces a shift into \(b\).
If it is subsequently removed by transporting along the same unit
normal foliation, the endpoint markings change only by isotopy.
Thus the conclusion is independent of those gauges. Arbitrary changes
of foliation, or a quotient with a spatially dependent normal lapse,
are not silently included in (1).

## 4. A uniform collar repair gap for the actual closed inputs

Use the round11 collar radius

\[
a_0(t)=c_\ell\cosh(\sqrt3\,t),\qquad
c_\ell=\frac{\ell}{2\pi},\qquad A_\ell=a_0(L_\ell).
\tag{9}
\]

Although \(L_\ell\to\infty\), the exact integral is

\[
\int_{-L_\ell}^{L_\ell}a_0\,dt
  =\frac{2A_\ell}{\sqrt3}\tanh(\sqrt3L_\ell)
  \le\frac{2A_\ell}{\sqrt3}.
\tag{10}
\]

Suppose an exact Einstein candidate of the form (1) satisfies
\(a=a(t)\) and

\[
\Lambda^{-1}a_0\le a\le\Lambda a_0,\qquad
\|H(-L_\ell,\cdot)\|_\infty,\quad
\|H(L_\ell,\cdot)\|_\infty\le\eta ,
\quad \Lambda\ge1 .
\tag{11}
\]

There is no smallness assumption on the interior \(S\), its trace,
or the connection. Equations (8)--(11) give

\[
\boxed{
\eta\ge\frac{\sqrt3}{4\Lambda^2}
          d_{\mathcal T}([h_-],[h_+])^2.}
\tag{12}
\]

The radius \(A_\ell\) cancels. This is a positive lower bound
independent of the collapsing parameter, rather than a repair radius
which shrinks with \(\ell\).

For a self-glued block, let the reference endpoint conformal structures
be \(q\) and \(f^*q\). Put
\(d_0=d_{\mathcal T}(q,f^*q)\).
If the candidate's two endpoint conformal structures are each within
\(\kappa\) of the corresponding reference point, then

\[
\eta\ge
 \frac{\sqrt3}{4\Lambda^2}(d_0-2\kappa)_+^2 .
\tag{13}
\]

In particular no sequence of such exact repairs can have
\(\kappa\to0\), \(\eta\to0\), and bounded \(\Lambda\), when \(d_0>0\).
Geometric \(C^1\) convergence to the original collars, in the stated
circle/normal-foliation gauge, has precisely these consequences:
the reference \(H\)'s vanish near both faces, the quotient metrics
converge there, and the radii remain relatively comparable.

For an infinite-order \(f\), \(d_0>0\) for each fixed \(q\):
a fixed Teichmüller point would realize \(f\) as an isometry of a
closed hyperbolic surface, whose isometry group is finite.
For a pseudo-Anosov one has the stronger uniform lower bound

\[
d_{\mathcal T}(q,f^*q)\ge\tau_{\mathcal T}(f)
 =\log\lambda(f)>0 ,
\tag{14}
\]

where \(\lambda(f)\) is its stretch factor, not the square of that
factor. This is the classical translation-length identity; see
[Aougab--Taylor, Section 2.4](https://arxiv.org/pdf/1510.00995),
which recalls the identity and its Thurston/Teichmüller background.
Equation (12) can therefore detect the fixed mapping class even if
the common endpoint conformal structure \(q\) is allowed to vary.

This is a class-restricted result. The earlier round5/6 repair theorem
on \(E_D\) allowed arbitrary tensor perturbations but controlled a
shrinking \(C^2\) ball. Here the neighbourhood obstruction has fixed
size and is expressed through a marked mapping class, but candidates
must retain the circle-invariant, orbit-radius-only normal form.
Neither theorem implies the other or excludes distant general
Einstein metrics on the closed manifold.

## 5. Exact connection transport does not remove its backreaction

The mixed Einstein equation for a free circle action is

\[
\delta_b(a^3\mathcal F)=0.
\tag{15}
\]

In the sector \(a=a(t)\), \(B=0\), a temporal connection gauge gives
\(\mathcal F=dt\wedge\beta_t\). Bianchi and (15) imply

\[
d_F\beta_t=0,\qquad d_F(*_{h_t}\beta_t)=0,\qquad
\partial_t\!\left(a^3*_{h_t}\beta_t\right)=0 .
\tag{16}
\]

Thus the closed one-form
\(\eta_{\mathrm{flux}}=a^3*_{h_t}\beta_t\) is conserved, with its
cohomology defined on the marked fibre. The total shear class is
\(\int_I[\beta_t]\,dt\); it is fixed by the actual circle-valued
gluing. This is not a freely adjustable numerical boundary condition.

For fixed \(h\) and prescribed harmonic shear \(b\), these equations
have the explicit solution

\[
\beta_t=\frac{a(t)^{-3}}{I_3}\,b,\qquad
I_3=\int_I a(t)^{-3}\,dt .
\tag{17}
\]

It solves the connection equation, not the Einstein equation. Its
positive contribution to (6), at each point of the fibre, is

\[
\int_Ia|\beta_t|^2\,dt
=|b|^2\,\frac{I_5}{I_3^2},
\qquad I_5=\int_Ia^{-5}\,dt .
\tag{18}
\]

For \(a=c\cosh(kt)\) and intervals exhausting the two ends,

\[
I_3\sim\frac{\pi}{2kc^3},\qquad
I_5\sim\frac{3\pi}{8kc^5},\qquad
\frac{I_5}{I_3^2}\sim\frac{3k}{2\pi}c .
\tag{19}
\]

The integer shear does not disappear, but its contribution is
suppressed by the small circle. It still forbids exact matching to
two zero-mean-curvature product faces by (6). It does not by itself
produce the uniform bound (12): that bound uses the nonzero
Teichmüller displacement. Maxwell transport therefore identifies
which part of the error can be solved, and which signed constraint
remains afterwards.

## 6. What changes when the orbit radius depends on the fibre

The term \(-\Delta_{h_t}a/a\) in (3) is genuinely present.
For \(a=a(t,x)\), the pointwise receiver instead reads

\[
(H/a)'=\frac Da-\frac{|S|^2}{a}-aQ
                     +\frac{\Delta_{h_t}a}{a^2}.
\tag{20}
\]

One cannot omit the last term or claim it has a favourable pointwise
sign. Nor does its integral with the displayed weight vanish:
\(\int_F(\Delta a)/a^2\,d\mu_h
=2\int_F|\nabla a|^2/a^3\,d\mu_h\).
This is the specific escape from the preceding monotonicity, not an
unspecified analytic technicality.

There is nevertheless a useful exact rigidity statement in the
common-area sector used by the round11 symplectic construction.

**Common-area rigidity.** In (1), allow arbitrary \(a(t,x)>0\) and
arbitrary connection. If \(H\equiv0\) and \(g\) is Einstein, then
\(S=0\), \(\mathcal F=0\), and \(a\) depends only on \(t\).
Consequently the metric is locally a product of two constant-curvature
surfaces with the same curvature.

To prove this, with \(D=H=0\), multiply (3) by \(a\) and integrate
over the closed fibre at each \(t\):

\[
0=\int_F \bigl(a|S|^2+a^3Q-\Delta_{h_t}a\bigr)\,d\mu_{h_t}
 =\int_F\bigl(a|S|^2+a^3Q\bigr)\,d\mu_{h_t}.
\tag{21}
\]

Every term is nonnegative, so \(S=\mathcal F=0\).
Equation (3) then gives \(\Delta_h a=0\); closedness and connectedness
of \(F\) make \(a\) spatially constant. The remaining Einstein
equations are
\(\operatorname{Ric}_h=\lambda h\) and \(a''=-\lambda a\).
Genus at least two gives \(\lambda<0\).
A flat connection may have global holonomy; the conclusion is local
product structure, not a globally trivial bundle.

For an almost-Einstein metric in the same common-area sector, (21)
becomes the exact quantitative identity

\[
\int_F(a|S|^2+a^3Q)\,d\mu_h
       =\int_F aD\,d\mu_h
       \le 2\|\operatorname{Ric}-\lambda g\|_{\mathrm{op},\infty}
                         \int_F a\,d\mu_h .
\tag{22}
\]

This is compatible with the constructed sequence. It says that the
shape and connection energies must vanish with its defect; it does
not force their integrated marked transport to disappear on a growing
collar.

## 7. Scope and computation

The new conclusion is a definite, parameter-independent obstruction
to small invariant Einstein repairs whenever the collar transports
a nonzero marked Teichmüller displacement. It is nonlinear, includes
the full connection curvature, and does not depend on the Einstein
constant. It identifies necessary boundary backreaction instead of
assuming that a small Ricci residual automatically has a small inverse.

The unresolved alternatives are concrete: an exact repair could leave
this invariant/foliated sector, permit spatial orbit-radius variation
together with fibre area change, alter its boundary geometry by the
amount forced by (12), or lie far from this degenerating family.
No argument here rules out those possibilities on the closed manifold.

The accompanying round12_repair_check.py computes the relevant Ricci
components directly from a coordinate metric with evolving fibre
area, nonzero electric and magnetic connection curvature, and a
spatially varying orbit radius. It tests (3), the factor \(1/4\)
under the stated tensor norm, and the otherwise missing Laplacian
term. The geometric distance, gauge and boundary arguments above
remain mathematical proofs rather than consequences of a symbolic
calculation.
