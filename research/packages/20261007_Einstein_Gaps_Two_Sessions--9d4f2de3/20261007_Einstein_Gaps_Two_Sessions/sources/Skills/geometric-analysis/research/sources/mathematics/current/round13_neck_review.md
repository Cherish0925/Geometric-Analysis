# Independent checks of the collapsing collar kernel

## 1. Exact product calculation

On
\[
 g_0=dt^2+a(t)^2d\phi^2+h_F,\qquad
 a(t)=a_0\cosh(\sqrt3t),\qquad K(h_F)=-3,
\]
set \(k=a'/a\), \(f=\operatorname{sech}^2(\sqrt3t)\), and
\[
 H=f(dt^2-a^2d\phi^2).
\]
The trace vanishes. The only potentially nonzero divergence component
is the radial one, \(f'+2kf\), which vanishes because \(f'=-2kf\).
Thus \(H\) is an exact TT tensor on the product cylinder.

For a direct check independent of a Lichnerowicz sign convention, use
\[
 g_\tau=(1+\tau f)dt^2+a^2(1-\tau f)d\phi^2+h_F.
\]
Writing \(v_\tau=\sqrt{1+\tau f}\) and
\(b_\tau=a\sqrt{1-\tau f}\), the first surface's Gauss curvature is
\[
 K_\tau=-\frac{1}{v_\tau b_\tau}
                  \partial_t(b_\tau'/v_\tau).
\]
Differentiating at zero gives
\[
 \dot K=3f+\frac32kf'+\frac12f''
       =(3-k'-k^2)f=0.
\]
Since the two-dimensional Ricci tensor is \(K_\tau g_\tau\), the
derivative of \(\operatorname{Ric}+3g\) vanishes. The fibre remains
unchanged. Any usual Bianchi gauge term also vanishes on this TT
tensor. This establishes the local kernel without relying on a
remembered curvature-operator sign.

## 2. It is not a global infinitesimal diffeomorphism

In the Round 11 geometry the shear cutoff is identically zero near
\(t=0\), the fibre metric is constant there, and \(a'(0)=0\).
For each fibre point the waist circle \(\gamma\), of length \(\ell\),
is consequently a closed geodesic of \(G_\ell\).

Let \(U\) be its unit tangent and define
\[
 \mathscr L(T)=\ell^{-1}\int_\gamma T(U,U)\,ds.
\]
For every smooth vector field \(Z\) on the closed manifold,
\[
 \mathscr L(\mathcal L_ZG_\ell)
 =2\ell^{-1}\int_\gamma
     \frac{d}{ds}\langle Z,U\rangle\,ds=0.
\]
The tensor \(H_\ell\), cut off to agree with \(H\) near the waist,
satisfies \(\mathscr L(H_\ell)=-1\). Therefore
\[
 \inf_Z\|H_\ell-\mathcal L_ZG_\ell\|_{C^0(G_\ell),\mathrm{op}}
 \ge1.
\]
This is stronger than saying that a convenient coordinate expression
does not look like a gauge term: the length-variation functional
detects a genuine marked deformation. Local pure-gauge expressions
for constant-curvature deformations do not invalidate this closed-orbit
test.

## 3. Support and operator-error bookkeeping

The step function \(\zeta\) in Round 11 is identically one on a fixed
neighborhood of the upper endpoint of its parameter interval. Hence
there is a fixed \(c>0\) such that, for all sufficiently small \(\ell\),
the marked fibre metric is exactly constant on \(|t|\le cL_\ell\).
Choose the tensor cutoff inside this region, equal to one on a smaller
fixed-fraction collar and zero before its outer boundary.

Outside the fixed shear transition \(0<t<1\), the connection one-form
is constant in \(t\) and closed on the fibre. It is locally gauge
equivalent to the product, even when its cohomology class is nonzero.
Thus the uncut tensor is exactly in the local linearized kernel there.
The cutoff errors occur where
\(f+|f'|+|f''|\le Ce^{-c'L_\ell}\), so they are of that order.

Inside the fixed shear transition the circle radius is \(O(\ell)\).
In geometric orthonormal frames the metric and the relevant finite
derivative coefficients differ from the product by \(O(\ell)\).
The linearized Einstein and Bianchi operators are second order.
Their action on the uniformly \(C^2\)-bounded tensor therefore costs
\(O(\ell)\) in this region.

Since \(L_\ell\) is a positive constant multiple of
\(|\log\ell|\) up to bounded error, the resulting full gauge-fixed
operator \(P_\ell\) has
\[
 \|H_\ell\|_{C^2}\ge c_0>0,\qquad
 \|P_\ell H_\ell\|_{C^0}\le C(\ell+\ell^\nu)
\]
for some fixed \(\nu>0\). The exponent depends on the plateau and
cutoff placement, not on a universal sharp spectral claim.

The same bookkeeping applies after any fixed number of covariant
derivatives: all fixed data are smooth, the transition width is fixed,
and derivatives of the cutoff add powers of \(L_\ell^{-1}\).
In particular the error is \(O(\ell+\ell^\nu)\) in \(C^1\), and hence
in geometric \(C^{0,\alpha}\) norms, while \(H_\ell\) is uniformly
bounded in \(C^{2,\alpha}\).

If \(P_\ell:X_\ell\to Y_\ell\) is invertible, \(X_\ell\) controls
the displayed \(C^0\) norm and the same error estimate holds in the
chosen \(Y_\ell\), then
\[
 \|P_\ell^{-1}\|\ge
 \frac{\|H_\ell\|_{X_\ell}}{\|P_\ell H_\ell\|_{Y_\ell}}.
\]
In particular, the full elliptic inverse
\(C^{0,\alpha}\to C^{2,\alpha}\), with these specified geometric
norms, has lower bound \(c(\ell+\ell^\nu)^{-1}\).
The raw \(C^2\to C^0\) test alone should not be presented as a
standard bounded-inverse theorem: a general \(C^0\) source does not
control second derivatives in supremum norm.

This does not establish a bound for an inverse after removing the neck
mode, nor a spectral eigenvalue in an unspecified self-adjoint space.
The cut-off tensor need not be exactly TT globally; that is immaterial
for the full gauge-fixed operator, but matters if one instead states a
TT-slice theorem. A separate projection estimate would be needed for
the latter.

The geometric content beyond the abstract volume/continuation
obstruction is explicit: changing the waist length supplies a genuine
approximate kernel whose leakage is concentrated in a collapsed shear
region and exponentially small cut-off tails.
