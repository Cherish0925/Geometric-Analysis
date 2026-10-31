# Harmonic separation, twist, and the spectrum of a complete connector

20 September 2026.

The local charged Einstein neck does not determine whether its two halves
can reach conformal infinity. This note gives a necessary condition on the
complete object. It retains the nonnegative defect in the classical
harmonic-function proof of the Li--Wang end theorem and identifies the
physical twist as part of that defect. It does not construct a connector
or exclude every possible connector. The classical spectral threshold is
not claimed as a new discovery.

## 1. Setting and conclusion

Let a complete smooth four-manifold have two smooth conformally compact
asymptotically hyperbolic ends, of sectional-curvature limit -1, and a
compact interior. Let

\[
 E=\operatorname{Ric}+3g,\qquad \|E\|_{\infty,\mathrm{op}}\le\epsilon.
\]

Assume enough conformal boundary regularity for the Dirichlet harmonic
function with locally constant boundary values to have its usual indicial
decay, with two differentiated orders. Smooth conformal compactness is
sufficient. Denote by u the bounded harmonic function with value 0 at one
boundary component and 1 at the other. It can equivalently be obtained by
Dirichlet exhaustion. Put

\[
 h=|du|,\qquad v=h^{2/3},\qquad
 d\nu=\frac{v^2\,dV}{\int v^2\,dV}.
 \tag{1.1}
\]

The measure is defined on the whole connector, not a chosen central slice.
On its regular set let n=grad(u)/h, let II be the second fundamental form
of a level hypersurface, and define

\[
 \mathcal D=|\mathrm{II}^{\circ}|^2
       +\frac23|\nabla_{\{u=\mathrm{const}\}}\log h|^2\ge0.
 \tag{1.2}
\]

Its value on h=0 is immaterial to integrals against nu. With lambda_0
denoting the bottom of the spectrum of -Delta on the complete manifold,

\[
 \boxed{\quad
 \lambda_0+\frac23\int\mathcal D\,d\nu
 \le 2-\frac23\int E(n,n)\,d\nu
 \le2+\frac23\epsilon .\quad}
 \tag{1.3}
\]

Suppose in addition there is a free isometric T2 action preserving the
ends, with two-dimensional quotient. Use the fixed principal-bundle
notation

\[
 g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\quad
 G=\rho M,\quad\det M=1,\quad dA=f\,d\mu_\gamma,
 \qquad Q=\frac12f^{\mathsf T}Gf.
 \tag{1.4}
\]

Then u is invariant, and (1.3) implies the useful weaker statement

\[
 \boxed{\quad\lambda_0+\frac23\int Q\,d\nu
                  \le2+\frac23\epsilon .\quad}
 \tag{1.5}
\]

In particular, a two-ended Einstein continuation carrying nonzero twist
must have lambda_0<2: Q is positive on an open set, and unique continuation
prevents the nonconstant harmonic u from having du=0 on that entire set.
If a candidate has Q>=q0 on a region of nu-mass at
least theta, then it requires

\[
 \lambda_0\le2+\frac23\epsilon-\frac23q_0\theta.
 \tag{1.6}
\]

Neither a fixed pointwise twist peak nor a fixed physical support volume
supplies theta. It is a new quantity to calculate on the complete geometry.

## 2. The retained Kato defect

At a regular point choose an orthonormal frame with first vector n. The
harmonic equation and the Hessian of a level function give

\[
 \nabla^2u(n,n)=-hH,\quad
 \nabla^2u(n,e_A)=e_Ah,\quad
 \nabla^2u(e_A,e_B)=h\mathrm{II}_{AB}.
\]

Consequently the improved Kato defect has the exact expression

\[
 D:=|\nabla^2u|^2-\frac43|\nabla h|^2
   =h^2|\mathrm{II}^{\circ}|^2
       +\frac23|\nabla_{\{u=\mathrm{const}\}}h|^2
   =h^2\mathcal D.
 \tag{2.1}
\]

Bochner's formula, with Delta=div grad, reads

\[
 h\Delta h=\frac13|\nabla h|^2+D-3h^2+E(n,n)h^2.
\]

The exponent 2/3 cancels the gradient-square term. Thus on the regular set

\[
 \Delta v=-2v+\frac23E(n,n)v+\frac23\mathcal Dv.
 \tag{2.2}
\]

At the critical set one uses the weak inequality with the same right-hand
side. For eta>0 set w_eta=(h^2+eta)^(1/3). Direct differentiation gives

\[
 \Delta w_\eta=
 \frac89\eta(h^2+\eta)^{-5/3}|\nabla h|^2
 +\frac23(h^2+\eta)^{-2/3}D
 +\frac23(-3+E(n,n))h^2(h^2+\eta)^{-2/3}.
\]

The first term is nonnegative. Pass to the limit against nonnegative
compact tests and use Fatou for the second term; one must not divide by h
on its zero set. Testing first with a compact cutoff times
w_eta-eta^(1/3) bounds its local Dirichlet integral and proves v in
H1_loc and local integrability of D h^(-2/3).
This is the regularization in the harmonic-function proof of the classical
end theorem, retaining rather than discarding its nonnegative remainder.

On an end with defining function x, locally constant boundary data have
u-u_boundary=O(x^3), h=O(x^3), and v=O(x^2). The indicial roots for
functions in dimension four are 0 and 3; the coefficients below order 3
vanish for constant boundary data. Since dV is O(x^-4 dx dV_boundary),
v is in L2 and end cutoff errors tend to zero. The integrated inequality
also bounds its full Dirichlet integral. Testing (2.2) by cutoff times v
and passing to the limit therefore gives

\[
 \int|\nabla v|^2+\frac23\int\mathcal Dv^2
       \le 2\int v^2-\frac23\int E(n,n)v^2.
 \tag{2.3}
\]

Rayleigh's variational principle proves (1.3). The epsilon inequality
requires only the displayed Ricci lower bound in the n direction; the
two-sided norm is used to match the Yau26 normalization.

## 3. Twist is an unavoidable part of the level-set defect

Uniqueness of the Dirichlet problem makes u invariant under the torus.
Take z to be the horizontal unit vector perpendicular to n, tangent to
the level set, and V_a an orthonormal vertical frame. The submersion
connection formula gives, up to an immaterial common sign,

\[
 \mathrm{II}(z,V_a)=\frac12\langle F(z,n),V_a\rangle_G.
\]

Both symmetric off-diagonal entries occur in the tensor norm, hence

\[
 2\sum_a|\mathrm{II}(z,V_a)|^2
       =\frac12 f^{\mathsf T}Gf=Q.
 \tag{3.1}
\]

This coefficient is Q, not Q/2. Trace subtraction does not change these
entries. More explicitly, write a=II(z,z) and b=n(log rho), and normalize
the orbit-shape target by |dU|^2=(1/2)tr(M^-1 dM M^-1 dM). Then

\[
 \boxed{\quad
 \mathcal D=Q+\frac12|dU(n)|^2
       +\frac16(2a-b)^2+\frac23|z(\log h)|^2.\quad}
 \tag{3.2}
\]

The three additional terms respectively measure normal shape change,
failure of umbilicity between the quotient-circle and orbit directions,
and variation of harmonic speed along a level set. The estimate is not a
Maxwell-only assertion: its test function uses the complete metric and
both ends, and Bochner uses the full Ricci tensor.

## 4. Collapse does not erase this test

Quotient by a finite subgroup of the acting torus. The local metric,
harmonic function u, Q and D are unchanged, while all integrals in nu
are divided by the subgroup order. The normalized quantities in (1.3)
and (1.5) are unchanged.

In fact lambda_0 is also unchanged. For a compactly supported function w
on any such metric set

\[
 W(p)=\left(\int_{T^2}|w(a\cdot p)|^2\,da\right)^{1/2}.
\]

Normalized Haar measure and Cauchy--Schwarz give ||W||2=||w||2 and
||dW||2<=||dw||2. W is invariant and compactly supported; its possible
zeros are handled by smooth approximation. Thus the bottom of the full
spectrum equals the bottom on invariant functions. The latter is the
Rayleigh quotient on the base with measure rho dmu_gamma; changing only
the orbit lattice multiplies numerator and denominator by the same factor.

This is precisely different from an absolute physical energy bound that
can disappear under the finite quotients of the local neck.

The same calculation has a dimension-independent interpretation. In
dimension n>=4 replace v by h^((n-2)/(n-1)) and define
\(\mathcal D_n=|\mathrm{II}^\circ|^2+
\frac{n-2}{n-1}|\nabla_\Sigma\log h|^2\). Then
\[
 \lambda_0+\frac{n-2}{n-1}\int\mathcal D_n\,d\nu
 \le n-2+\frac{n-2}{n-1}\epsilon,
 \qquad E=\operatorname{Ric}+(n-1)g.
\]
Here h=O(x^(n-1)); hence v^2 dV is O(x^(n-4)dx), integrable for
n>=4. The dimension-three endpoint needs the classical cutoff argument
instead of this L2 test. This extension is a retained-defect version of
the same classical Bochner argument, not a general closed-manifold result.

## 5. Consequences, checks, and the remaining global issue

For Einstein metrics with epsilon=0, lambda_0<=2 is already the classical
two-end spectral restriction. If the manifold is R x T3, equality is also
impossible without assuming torus symmetry: the equality case in the
Li--Wang theorem is dt^2+cosh^2(t)h_N. The Einstein equation forces the
closed three-metric h_N to have Ric=-2h_N, hence constant sectional
curvature -1. Its fundamental group cannot be Z^3. Thus lambda_0<2.
This is a classical consequence, not a claimed new topological theorem.

For smooth AH ends the essential spectrum begins at 9/4. Formula (1.3)
therefore forces a discrete L2 mode below 9/4 whenever epsilon<3/8.
For an exact Einstein continuation with nonnegative-Yamabe conformal
infinity, the known spectral lower bound would be 9/4 and is incompatible
with this requirement. Negative boundary conformal classes are not ruled
out by that argument.

The retained twist term identifies which spectral deficit a charged
continuation must create. It supplies no independent lower bound on
lambda_0 or on the mass fraction theta. Therefore it does not by itself
rule out the charged AH continuation, arbitrary small-defect cylinders,
or any closed Yau26 input. Producing such a lower bound from the prescribed
marked ends and complete equations is a genuine next question; assuming
it would merely move the missing global argument into a hypothesis.

The exact checks in `round7_spectral_check.py` verify the tensor
decomposition, mixed twist coefficient, exponent cancellation, and an
actual complete twisted test metric. They do not prove harmonic existence,
the boundary expansion, or the spectral equality classification.

### Primary literature

P. Li and J. Wang, *Complete manifolds with positive spectrum*, J.
Differential Geometry 58 (2001), 501--534: the harmonic separator construction
and Theorem 2.1, including its equality case.
<https://www2.math.ethz.ch/EMIS/journals/NYJM/jdg/p/2001/58-3-5.pdf>

J. M. Lee, *The spectrum of an asymptotically hyperbolic Einstein manifold*,
Communications in Analysis and Geometry 3 (1995), 253--271: essential
spectrum background and the nonnegative-Yamabe spectral conclusion for
Einstein metrics. <https://arxiv.org/abs/dg-ga/9409003>
