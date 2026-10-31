# A fixed-topology two-ended near-Einstein family with collapsing circles

21 September 2026.

## 1. An explicit global construction

Let \((\Sigma,h_\Sigma)\) be any fixed closed hyperbolic surface of
genus at least two, with Gaussian curvature \(-1\). Fix the period
\(2\pi\) of \(\phi\). For \(0<d<1/2\), put
\[
y=d\cosh u,\qquad r=\frac{1+y}{\sqrt3},\qquad
F(y)=\frac{y^2(y+3)}{3(y+1)}.
\tag{1.1}
\]
On the fixed manifold \(\mathbb R_u\times S^1_\phi\times\Sigma\), define
\[
\boxed{
g_d=\frac{1+y}{3+y}\,du^2
 +\frac{y^2(y+3)}{3(y+1)}\,d\phi^2
 +\frac{(1+y)^2}{3}\,h_\Sigma.}
\tag{1.2}
\]

**Theorem 1.** These metrics are smooth, complete, and smoothly AH at
both ends. Their free isometric circle action, marked circle period,
underlying smooth manifold, and two conformal boundary metrics
\(d\phi^2+h_\Sigma\) are independent of \(d\). Nevertheless
\[
\boxed{
\|g_d^{-1}(\operatorname{Ric}_{g_d}+3g_d)\|_{\infty,\mathrm{op}}
=\frac{d(2d+3)}{(1+d)^2}<3d\longrightarrow0.}
\tag{1.3}
\]
Their minimum circle radius is
\[
\sqrt{F(d)}=d\sqrt{\frac{d+3}{3(d+1)}}\sim d.
\tag{1.4}
\]
All fixed covariant derivative orders of curvature stay uniformly bounded
as \(d\to0\). Thus the degeneration is not forced curvature blow-up:
the separating circle collapses.

There is also a version \(\widetilde g_d\) on the same manifold and with
the same conformal boundaries which equals the exact extremal Kottler
Einstein metric outside a compact core on each side, and satisfies
\(\|\operatorname{Ric}_{\widetilde g_d}+3\widetilde g_d\|_{\mathrm{op}}
\le C d\). The physical length of that error core is \(O(\log(1/d))\).

By `round9_connector.md`, no exact conformally compact Einstein metric
in this free-circle class can have two ends. Therefore no positive
uniform Ricci-defect gap holds on this noncompact class, even with fixed
smooth topology, fixed conformal infinities, fixed circle period, and
bounded curvature and its fixed-order derivatives.

This is not a closed Yau26 counterexample. The cross-section is
\(S^1\times\Sigma\), not \(T^3\), and there is no free residual
isometric \(T^2\) action. The construction does not contradict the
earlier OT torus gap or establish nonexistence of nonsymmetric Einstein
fillings on the same manifold.

Boundary circle symmetry does not by itself remove that last qualification.
Anderson's conformally compact isometry-extension theorem requires
\(\pi_1(\overline M,\partial\overline M)=0\)
([Theorem 5.4](https://arxiv.org/pdf/0704.3373)). This relative condition
fails here because the boundary is disconnected, even though each boundary
component separately surjects onto the interior fundamental group.

## 2. Extremal Kottler geometry and smooth doubling

The hyperbolic-horizon Kottler metric has
\[
g_K=\frac{dr^2}{F}+F\,d\phi^2+r^2h_\Sigma,\qquad
F=r^2-1+\frac{2}{3\sqrt3r},\qquad r_0=\frac1{\sqrt3}.
\tag{2.1}
\]
It satisfies \(\operatorname{Ric}=-3g_K\). The root \(r_0\) is double,
and \(F=(r-r_0)^2(r+2r_0)/r\). The classical Kottler expression and its
normalizations appear in Chruściel--Simon, equation (1.1)
([primary text](https://arxiv.org/pdf/gr-qc/0004032)); here
\(k=-1\), \(\Lambda=-3\), and mass \(-1/(3\sqrt3)\).

Rather than matching asymptotic expansions, change only the radial factor:
\[
q_d=F\left(1-\frac{d^2}{y^2}\right)
=\frac{(y^2-d^2)(y+3)}{3(y+1)},\qquad
g_d=\frac{dr^2}{q_d}+F\,d\phi^2+r^2h_\Sigma,
\quad y\ge d.
\tag{2.2}
\]
The apparent degeneracy at \(y=d\) is a doubling surface, not a bolt.
The substitution \(y=d\cosh u\) gives precisely (1.2), smooth and
positive for every real \(u\). In particular the circle does not vanish
at \(u=0\). Reflection \(u\mapsto-u\) glues two identical ends smoothly
without a seam or a nonlinear correction problem.

As \(|u|\to\infty\), the radial proper length diverges. Each end can
be compactified by \(x=1/r\):
\[
x^2g_d=\frac{dx^2}{x^2q_d(1/x)}+x^2F(1/x)d\phi^2+h_\Sigma,
\]
\[
x^2F(1/x)=1-x^2+\frac{2x^3}{3\sqrt3},\qquad
\frac{q_d}{F}=1-\frac{d^2x^2}{(\sqrt3-x)^2}.
\tag{2.3}
\]
Both expressions are smooth, their boundary values are one, and their
first derivatives at zero vanish. This proves smooth AH compactness and
the stated fixed conformal boundaries. Those boundary metrics have
negative scalar curvature; no nonnegative-Yamabe connectedness theorem
has been applied to them.

## 3. Complete Ricci calculation

For a general metric \(dr^2/q+F\,d\phi^2+r^2h_\Sigma\), let \(t\)
be proper radial distance, so \(r_t=\sqrt q\), \(a=\sqrt F\), \(b=r\).
Its Ricci endomorphism is diagonal with eigenvalues
\[
\begin{split}
\lambda_t&=-a_{tt}/a-2b_{tt}/b,\\
\lambda_\phi&=-a_{tt}/a-2a_tb_t/(ab),\\
\lambda_\Sigma&=-b^{-2}-b_{tt}/b-b_t^2/b^2-a_tb_t/(ab),
\end{split}
\tag{3.1}
\]
the last of multiplicity two. In terms of derivatives with respect to
\(r\),
\[
\frac{a_{tt}}a=\frac{qF''}{2F}+\frac{q'F'}{4F}
                         -\frac{q(F')^2}{4F^2},\quad
b_{tt}=q'/2,\quad
\frac{a_tb_t}{ab}=\frac{qF'}{2rF}.
\tag{3.2}
\]
Substitution of (2.2) yields exact identities
\[
\boxed{
\lambda_t+3=-\frac{3d^2}{y(1+y)^2},\qquad
\lambda_\phi+3=\lambda_\Sigma+3
=\frac{d^2(2y+3)}{y(1+y)^2}.}
\tag{3.3}
\]
The positive tangential value dominates the radial absolute value and
strictly decreases with \(y>0\). Since \(y\ge d\), its maximum is the
value in (1.3). This proves a continuous global operator-norm bound, not
a sampled maximum.

Uniform curvature bounds can also be read directly from the warped form.
On \(y\le2\), all fixed derivatives of \(y=d\cosh u\) are \(O(y)\),
the radial coefficient \((1+y)/(3+y)\) is bounded away from zero, and
all fixed derivatives of \(\log a\) are bounded. The quantities
\(a^{(j)}/a\) and \(b^{(j)}/b\) in proper radial coordinate are therefore
uniformly bounded, while \(b\ge1/\sqrt3\). The sectional curvature
blocks are \(-a_{tt}/a\), \(-b_{tt}/b\), \(-a_tb_t/(ab)\), and
\((-1-b_t^2)/b^2\); their covariant derivatives have the same control.
For \(y\ge1\), the explicit rational expressions or (2.3) give uniform
bounds through infinity. The same reasoning applies to the fixed smooth
cutoff below. The circle at \(u=0\) is a closed geodesic of length
\(2\pi\sqrt{F(d)}\); hence injectivity radius is not uniformly positive.

## 4. An exact-end version with controlled nonlinear error

Fix a smooth \(\chi:[0,\infty)\to[0,1]\) with \(\chi=1\) for
\(y\le1\) and \(\chi=0\) for \(y\ge2\). Define
\[
\widetilde q_d=F\left(1-\frac{d^2\chi(y)}{y^2}\right),
\qquad
\widetilde g_d=\frac{dr^2}{\widetilde q_d}
                    +F d\phi^2+r^2h_\Sigma,
\tag{4.1}
\]
again doubled at \(y=d\). The central metric is unchanged and the ends
are exactly Kottler for \(y\ge2\). Positivity holds for \(y>d\), and
the same coordinate \(y=d\cosh u\) gives a smooth central doubling.

No unspecified matching error remains. Equations (3.1)--(3.2) give,
with primes here denoting \(d/dy\),
\[
\begin{split}
\widetilde\lambda_t+3
 &=\frac{3d^2\bigl((y^2+3y+1)\chi'-2\chi\bigr)}
         {2y(1+y)^2},\\
\widetilde\lambda_\phi+3
 &=\frac{d^2\bigl((y^2+3y+3)\chi'+(4y+6)\chi\bigr)}
         {2y(1+y)^2},\\
\widetilde\lambda_\Sigma+3
 &=\frac{d^2\bigl((y^2+3y)\chi'+(4y+6)\chi\bigr)}
         {2y(1+y)^2}.
\end{split}
\tag{4.2}
\]
The transition lies in a fixed interval \(1\le y\le2\); its error is
bounded by \(C_\chi d^2\). In the central region the exact bound (1.3)
is \(O(d)\). Thus the full global defect is \(O(d)\), with exact
Einstein collars at both conformal infinities.

The error support lies between the two levels \(y=2\). Its radial
physical length is \(L_d=O(\log(1/d))\): in the central region this is
the integral of \(\sqrt{(1+y)/(3+y)}\,du\) up to
\(u=\operatorname{arcosh}(1/d)\), and the transition adds bounded length.
Therefore
\[
\epsilon_dL_d\longrightarrow0.
\tag{4.3}
\]

## 5. The optical ground state identifies the actual escape

For the free circle, \(V=a=\sqrt F\), \(\Omega=1/a\), and the optical
metric is a warped product
\[
k=ds^2+w(s)^2h_\Sigma,\qquad
ds=dt/a,\qquad
w=\frac ba=\frac{(1+y)^{3/2}}{y\sqrt{y+3}}.
\tag{5.1}
\]
The radial curve between boundaries is a shortest optical curve, since
any transverse motion increases length. At either boundary
\(w\to1\) and \(w_s\to0\). These statements hold for both the explicit
metric and its exact-end variant.

Since \(\operatorname{Ric}_k(\partial_s,\partial_s)=-2w_{ss}/w\), the
Neumann index operator of `round10_optical.md` obeys
\[
\mathcal A w=\left(-2\partial_s^2
        -\operatorname{Ric}_k(\partial_s,\partial_s)\right)w=0.
\tag{5.2}
\]
The positive function \(w\) is its ground state and the lowest eigenvalue
is exactly zero. Moreover
\[
\frac{d}{dy}\log w=-\frac3{y(1+y)(y+3)}<0.
\]
Thus \(\max w=w(d)\). Normalizing \(f=w/w(d)\), the boundary-to-maximum
ratio in the optical error-length inequality is exactly
\[
\boxed{
f(0)+f(\ell)
=\frac{2}{w(d)}
=\frac{2d\sqrt{d+3}}{(1+d)^{3/2}}
\sim2\sqrt3\,d\longrightarrow0.}
\tag{5.3}
\]
Equations (4.3) and (5.3) exhibit the ground-state-localization alternative
of that inequality in an actual complete small-Ricci-error family. The
mechanism is not merely a scalar model: all Ricci blocks and the smooth
global metric have been controlled.

## 6. Exact contribution and limits

The construction shows why the exact free-circle nonexistence theorem
cannot be upgraded to a uniform near-Einstein theorem in the same
noncompact topological and boundary class without another hypothesis.
Even bounded full curvature and its fixed-order derivatives do not
prevent the collapse. The circle must remain free for every parameter,
but its length is allowed to vanish in the limit.

The classical exact Kottler geometry is the starting input; no claim that
it is new is made. The modified radial coefficient, global Ricci bounds,
fixed exact-end cutoff and optical ground-state calculation are the
explicit construction established here. Priority relative to other
approximate cusp-doubling constructions is not asserted.

Kottler metrics already serve as local models in approximate-Einstein
constructions: Fine--Premoselli use them in their compact branched-cover
construction and subsequently solve the exact equation
([primary paper](https://arxiv.org/pdf/1802.00608)). That precedent is
different from the two-conformal-end, collapsing-circle family above;
neither the use of Kottler geometry nor the general idea of approximate
Einstein gluing is a new ingredient here.

A useful comparison is Cotler--Jensen's two-ended constrained-instanton
metric ([equation (11)](https://arxiv.org/pdf/2010.02241)). Its
four-dimensional isotropic torus case has
\(a(\rho)=b(2\cosh(3\rho/2))^{2/3}\) in
\(d\rho^2+a^2g_{T^3}\). Direct calculation gives
\[
\lambda_\rho+3=-\tfrac32\operatorname{sech}^2(3\rho/2),\qquad
\lambda_T+3=\tfrac32\operatorname{sech}^2(3\rho/2).
\]
Its uniform Ricci defect is \(3/2\), independent of the bottleneck
size \(b\). Thus shrinking a two-ended off-shell geometry does not
itself produce the vanishing pointwise error proved here. The negative
surface curvature in (1.2), rather than only a shrinking bottleneck,
is essential. This comparison and the preceding Kottler references
do not constitute an exhaustive priority search.

The metrics are noncompact. No gluing to a closed manifold, no global
Einstein nonexistence for that closed smooth type, and no Yau26 branch
counterexample are supplied. In particular, the genus-at-least-two
factor cannot be replaced by a torus while keeping these curvature
equations: its curvature \(-1\) is essential to the extremal model.

## 7. A non-gauge approximate infinitesimal deformation

Let \(\mathcal F(g)=\operatorname{Ric}_g+3g\) and differentiate the
explicit family in its fixed \(u,\phi,\Sigma\) coordinates:
\[
h_d=d\,\partial_d g_d.
\]
The eigenvalues of \(g_d^{-1}h_d\), in radial, circle and surface
directions respectively, are
\[
\frac{2y}{(1+y)(3+y)},\qquad
2+\frac{y}{y+3}-\frac{y}{y+1},\qquad
\frac{2y}{1+y}\quad\text{(twice)}.
\tag{7.1}
\]
They are positive and at most two; the surface eigenvalue tends to two
at infinity. Thus \(\|h_d\|_{\infty,\mathrm{op}}=2\).

Write \(E_r,E_T\) for the error eigenvalues in (3.3). Differentiation
at fixed \(u\) acts on their expressions by
\(d\partial_d+y\partial_y\). Directly,
\[
d\partial_d E_r=\frac{1-y}{1+y}E_r,\qquad
d\partial_d E_T=\frac{y+3}{(2y+3)(y+1)}E_T.
\tag{7.2}
\]
Both multipliers have absolute value at most one. Differentiating the
covariant tensor \(\mathcal F(g_d)\) also differentiates its metric
factor; the additional term is the product of its error eigenvalue and
the corresponding eigenvalue in (7.1). Hence
\[
\boxed{\quad
\|D\mathcal F_{g_d}(h_d)\|_{\infty,\mathrm{op}}
\le 3\epsilon_d<9d,\qquad
\epsilon_d=\frac{d(2d+3)}{(1+d)^2}.
\quad}
\tag{7.3}
\]

This deformation does not approach a pure infinitesimal
diffeomorphism in the uniform norm. A circle at \(u=0\) with its base
point fixed is a closed geodesic. For its unit tangent \(U\), every
smooth globally single-valued vector field \(X\) satisfies
\[
\oint (\mathcal L_Xg_d)(U,U)\,dt
=2\oint \frac{d}{dt}\langle X,U\rangle\,dt=0.
\]
But \(h_d(U,U)\) is constant on that circle, equal to
\[
c_d=2+\frac{d}{d+3}-\frac{d}{d+1}\longrightarrow2.
\]
Consequently
\[
\inf_X\|h_d-\mathcal L_Xg_d\|_{\infty,\mathrm{op}}
\ge c_d.
\tag{7.4}
\]
The family therefore supplies an actual non-gauge approximate
infinitesimal deformation, not merely small errors at isolated metrics.
The perturbation has not been put in Bianchi gauge and does not decay
in the fixed-\(u\) identification. Equations (7.3)--(7.4) establish no
weighted, boundary-fixed, gauge-fixed or \(L^2\) inverse estimate.

## 8. Exact checks

`round10_kottler_check.py` checks all three Ricci eigenvalues, the global
maximum, smooth doubling, optical monotonicity, and the full cutoff
formulas with symbolic \(\chi\), the parameter-variation identities,
and the nonvanishing defect of the torus comparison. Nine exact checks pass.
`round10_kottler_coordinate_check.py` independently reconstructs the
Christoffel symbols and all Ricci entries from the four-dimensional
coordinate metric with \(h_\Sigma=dz^2+e^{2z}dw^2\). It does not use
the warped-product Ricci formulas. Neither calculation relies on a
finite numerical grid for the global bound.
