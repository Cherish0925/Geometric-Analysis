# The Ricci direction at a negative P-critical metric: an explicit signed identity

Date: 2026-10-11. Continuation of `q3_new_global_attainment.md` and `q3_variational_structure_current.md`. This note makes the remaining Ricci-direction sign completely explicit; it proves no attainment or universal instability theorem.

Let M be closed and four-dimensional, let

\[
P(g)=\int_M|E|^2\,dV_g,\qquad E=\operatorname{Ric}-\frac{s}{4}g,
\]

and assume g is an unrestricted smooth critical point of P with s<0. The trace equation implies that s is constant, hence E is transverse traceless. Put A=g^{-1}E and q=tr(A²). All integrals, derivatives, contractions and raising of indices below use g.

## 1. The exact remaining signed invariant

Define two (1,2) tensors

\[
C^k{}_{ij}=\frac12\bigl(\nabla_i E_j{}^k+\nabla_jE_i{}^k-\nabla^kE_{ij}\bigr),
\]

\[
D^k{}_{ij}=\frac12\bigl(\nabla_i(E^2)_j{}^k+\nabla_j(E^2)_i{}^k-\nabla^k(E^2)_{ij}\bigr)-2A^k{}_\ell C^\ell{}_{ij}.
\]

Here (E²)_{ij}=E_i{}^a E_{aj}. Write

\[
Q(C,D)=g^{ij}C^k{}_{i\ell}D^\ell{}_{jk},\qquad
Q_E(C,C)=E^{ij}C^k{}_{i\ell}C^\ell{}_{jk}.
\]

These contractions need not be nonnegative. If H is the unrestricted P-Hessian at g, then

\[
\boxed{
H(E,E)=\int_M\left[2\operatorname{tr}(A^4)
 +\frac{s}{2}\operatorname{tr}(A^3)
 -12Q(C,D)+12Q_E(C,C)\right]dV_g.
}\tag{1}
\]

Thus the missing quantity involves only E and its first covariant derivative. It is not necessary to compute fourth metric derivatives or differentiate the Bach tensor to evaluate this particular Hessian direction.

Combined with the previously proved conformal reduction, put L=-div grad and q_0=q-Vol(M)^{-1}\int q. Then the actual direction

\[
h_*=E+2(6L-2s)^{-1}q_0\,g
\]

has second variation

\[
\boxed{
H(h_*,h_*)=\int_M\left[2\operatorname{tr}(A^4)
 +\frac{s}{2}\operatorname{tr}(A^3)-12Q(C,D)+12Q_E(C,C)\right]
-\langle q_0,L(6L-2s)^{-1}q_0\rangle.
}\tag{2}
\]

If the right side is negative, g cannot be a local or global P-minimum. Every putative Q3 minimizer must have the right side nonnegative. This is a test for a smooth critical candidate; its use cannot assume a minimizer exists.

## 2. Derivation without Bach sign conventions

Fix the volume form dV_g and consider the manifold of metrics with this volume form, with its induced Ebin L² metric. Let

\[
F(\gamma)=\int_M s_\gamma\,dV_g.
\]

For trace-free variations, the first variation is

\[
DF_\gamma(h)=-\int_M\langle\operatorname{Ric}^\circ_\gamma,h\rangle_\gamma dV_g,
\]

so grad F=-E and P=|grad F|², as functions on this manifold. Its geodesic with initial velocity E is

\[
g_t=g\exp(tA).
\]

The determinant is fixed because tr A=0. At a P-critical point,

\[
\operatorname{Hess}F(E)=0,
\]

since grad P=2 Hess F(grad F)=0. Differentiating the squared gradient along this geodesic gives

\[
H(E,E)=-2\frac{d^3}{dt^3}F(g_t)\bigg|_{t=0}.
\tag{3}
\]

This does not assign a sign to either side. It uses the restricted Ebin connection, not the ambient metric-space connection without projection.

Now let C(t)=∇^{g_t}-∇^g. Its first two derivatives are exactly C'(0)=C and C''(0)=D from above. Because the volume form is fixed,

\[
C(t)^k{}_{ik}=0.
\]

The Ricci connection-difference formula and integration by parts give the exact identity

\[
F(g_t)=\int_M g_t^{ij}\operatorname{Ric}(g)_{ij}
 +\int_Mg_t^{ij}C(t)^k{}_{i\ell}C(t)^\ell{}_{jk}.
\tag{4}
\]

For clarity, in the Ricci difference the derivative term is ∇_k C(t)^k_{ij}. Upon integration its contraction yields twice the displayed quadratic connection term, while the original Ricci difference contains minus one copy. The trace-connection terms vanish identically.

Using

\[
g_t^{-1}=g^{-1}-tE^{\sharp\sharp}+\frac{t^2}{2}(A^2)^{\sharp}
 -\frac{t^3}{6}(A^3)^{\sharp}+O(t^4),
\qquad C(t)=tC+\frac{t^2}{2}D+O(t^3),
\]

one obtains

\[
F'''(0)=-\int_M\operatorname{tr}(\operatorname{Ric}^{\sharp}A^3)
 +6\int_M Q(C,D)-6\int_MQ_E(C,C).
\]

Substitute Ric^sharp=A+(s/4)I and (3) to prove (1).

For (2), the conformal identities at constant scalar curvature are

\[
H(2fg,2fg)=6\|Lf\|_2^2-2s\langle f,Lf\rangle,
\qquad H(E,2fg)=-\langle q,Lf\rangle.
\]

Completing the square on mean-zero functions yields (2). The operator 6L-2s is strictly positive. This is exactly the conformal adjustment tangent to the constant-scalar slice, apart from its immaterial scalar scaling direction.

## 3. What the formula decides, and what it does not

The quartic term is positive, the cubic term has no fixed sign even when s<0, and the connection contractions are indefinite. Neither the Euler-Lagrange equation nor scalar negativity by itself has supplied an inequality giving the sign of their sum. A statement that the Ricci or Bach direction necessarily decreases P would therefore require an additional theorem.

There is a direct exact check of the quartic coefficient. On the scalar-flat product of constant-curvature surfaces c and -c, E is parallel with eigenvalues (c,c,-c,-c), so C=D=0. The unrestricted P-critical metric satisfies

\[
H(E,E)=8c^4\operatorname{Vol}(M)>0.
\]

Indeed the determinant-preserving path rescales the two factors by e^{ct} and e^{-ct}, and

\[
P(g_t)=4c^2\operatorname{Vol}(M)\cosh^2(ct).
\]

This example is not in the negative-scalar target; it verifies the coefficient and shows why discarding the quartic contribution would produce a false universal instability argument.

A second check uses a flat background and g_t=diag(e^{ta_0f(x_0)},...,e^{ta_3f(x_0)}) with sum a_i=0 on a torus. Formula (4) gives exactly

\[
F(g_t)=\frac{t^2}{4}\left(a_0^2-\sum_{i=1}^3a_i^2\right)
\int e^{-ta_0f}(f')^2.
\]

The cubic coefficient agrees with (4) and the C,D formula. `critical_hessian_check.py` checks the tensor contractions with exact rational arithmetic at 125 integer eigenvalue triples. The displayed analytic calculation, not those finite checks, establishes the identity.

## 4. Consequence for the current Q3 route

This completes the calculation previously left as an unspecified Einstein-Hilbert third variation. It provides an explicit candidate test using E, ∇E and one scalar resolvent. It does not yield a global sign on all critical metrics and does not control a singular minimizing sequence. No non-Bach-flat stable example or unrestricted global P-minimum has been produced here.

Thus the exact unresolved implication is whether the complete actual-field system, or the unrestricted minimizing property, forces a sign incompatible with (2) for every non-Einstein candidate. The present Euler-Lagrange and stability identities alone have not done so.

## Primary references and scope

- M. T. Anderson, *Extrema of curvature functionals on the space of metrics on 3-manifolds, I*, Section 7, formulas (7.3)-(7.4), for the fixed-volume Ebin exponential geodesics (the metric-space statement is dimension independent): https://www.math.stonybrook.edu/~anderson/existI.pdf . The derivation above only needs that explicit geodesic formula and its pointwise symmetric-space connection; it does not import a compactness result.
- M. Gursky and J. Viaclovsky, *Rigidity and stability of Einstein metrics for quadratic curvature functionals*, arXiv:1105.4648: https://arxiv.org/pdf/1105.4648 . Its established stability theorems concern the Einstein backgrounds specified there, not all negative P-critical metrics.
- Y. Euh and J. H. Park, *Critical metrics for the quadratic curvature functional on complete four-dimensional manifolds*, arXiv:2512.18758v1, Theorem 1.1 and equations (2.1): https://arxiv.org/html/2512.18758v1 . Its classification has an additional curvature-operator hypothesis; global P-minimality has not been shown to imply that hypothesis.
- C. LeBrun, *Curvature Functionals, Optimal Metrics, and the Differential Topology of 4-Manifolds*, arXiv:math/0404251, Section 11: https://arxiv.org/pdf/math/0404251 . The original global smooth-minimizer question remains the target.
