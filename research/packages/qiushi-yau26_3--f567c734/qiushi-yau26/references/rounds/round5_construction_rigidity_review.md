# Independent review of the whole-fibre receiver argument

Reviewed `round5_construction.md`, the independent classification in
`round5_receiver_independent.md`, and the closed detector in
`round3_matching_next.md`, Section 6. The relevant fixed-fibre,
balanced-collar, and TT-detector passages of the construction source
were also checked. No blocking mathematical error was found.

## 1. The limit retains the right mass

The receiver is normalized by the base period beta, not by epsilon beta.
After this normalization its fibre factor has the full limiting area
4 pi(p-1). The limiting nuclear mass is therefore

\[
   2\int_{\mathbb R}\operatorname{sech}t\,dt
       \operatorname{Area}(F_\infty)=8\pi^2(p-1).
\]

For a cusp truncation at depth R, the omitted central collar area is
bounded by integrating epsilon cosh(u) on |u|<=w(epsilon)-R. This is
O(exp(-R)), uniformly as epsilon tends to zero; an O(epsilon) endpoint
error is harmless. The fibre area form is unchanged by the shear.
The t-tail has mass O(exp(-T)), and the off-collar global quadratic
differential contributes O(beta) after normalization. These estimates
give actual tightness on the entire punctured fibre. They do not assign
zero response to the exterior of a thin-cylinder model.

## 2. C1 convergence is sufficient for the quadratic expression

On a fixed compact local cover, the covariant C2 bound is a coordinate
C2 bound. Periodicity of period beta implies that the y derivative has
mean zero and oscillation O(beta), hence is uniformly O(beta).
Mixed second-derivative bounds imply that each other first derivative
differs from its angular average by O(beta). Arzela--Ascoli on the
averages therefore gives strong local C1 convergence, with bounded weak
second derivatives.

This is enough for the term U times Hess(U): move one derivative onto
the smooth compactly supported test and the first U. Periodic boundary
terms cancel over the actual beta-period. The remaining terms depend
continuously on U and its first derivatives. Uniform pointwise bounds
for the second variation, together with the tight receiver mass, then
control the tails. No unproved strong C2 convergence or interchange of
a quadratic expression with mere weak convergence is required.

## 3. Gauge fixing and its receiver effect

The sign in the gauge equation is correct:

\[
 b(\mathcal L_Xg_*)=(\nabla^*\nabla+1)X^\flat
 \quad\text{when }\operatorname{Ric}(g_*)=-g_*.
\]

Dirichlet exhaustion and the Kato maximum principle bound X in L-infinity.
Uniform local-cover estimates give a bounded first derivative, so the
gauge-fixed V is bounded. Its Bianchi equation and linearized Einstein
equation make LV=0 elliptic, hence V is smooth with bounded derivatives
on fixed-radius local covers. The Killing-operator identity then recovers
bounded weak derivatives of X through order three from
Lie_X g=U-V. This avoids assuming C3 bounds at the initial C1,1 limit.

Naturality gives the correct second-order identity

\[
 D^2E[U,U]-D^2E[V,V]=-DE[W],
 \qquad W=2\mathcal L_XV+\mathcal L_X^2g_*
                         =\mathcal L_X(U+V).
\]

W is bounded. The identity (DE)*Q=0 follows from the Einstein background,
the TT property and LQ=0. The cutoff argument needs only bounded W and
integrability of Q and its first two derivatives. All hold on the
unit-y quotient of the whole-fibre limit. It is not necessary for an
individual pointwise cusp flux to vanish.

## 4. The classification and receiver sign

The four block potentials agree with the product connection: trace
potential 2, horizontal trace-free potential 2-4 sech(t)^2, mixed
potential 2-sech(t)^2, and the fibre Einstein operator. The mixed
potential retains both the horizontal frame-connection term and the
Ricci term in the one-form Weitzenbock identity.

For the fibre operator, delta P=(Delta_H+2)/2 gives a closed range
for P and a gap at least 2 on the orthogonal complement of the TT kernel.
The bounded-derivative, finite-area cutoffs justify the Hilbert-space
pairings. The horizontal ground-state transform has finite measure
sech(t)^3 dt dA_F, so its bounded solutions are constants. These arguments
do not discard the continuous spectrum of the punctured fibre.

The resulting kernel is precisely

\[
             V=f(aT+bS)+A+J(t)B.
\]

The determinant-preserving fibre path makes the horizontal second Ricci
variation equal to -(J')^2 |B|^2 dt^2/2. The exact horizontal cylinder
path has no receiver and no quadratic cross term with this shape stress.
The path acceleration is removed by the same integrable-adjoint test.
Consequently the affine quadratic receiver is

\[
                         -\frac\pi8\|B\|_{L^2(F)}^2\le0.
\]

This sign is applied only after the limiting Jacobi equation is proved.
It is not a sign assertion for arbitrary bounded tensor perturbations.

## 5. Quantitative conclusion and all signs

The normalized closed source is -1/(2 pi^2), while the limiting nuclear
mass is 8 pi^2(p-1). Their quotient is the stated lower bound
1/[16 pi^4(p-1)]. For a sequence with residual O(epsilon^3), division of
the pointwise Taylor equation by epsilon^(3/2) still gives the Jacobi
limit; exactness is not used prematurely in the quantitative proof.

If a nearby metric is Einstein with constant lambda, the C2 Taylor bound
gives lambda=-1+O(epsilon^(3/2)). Scaling it by -lambda preserves the
O(epsilon^(3/2)) neighbourhood, because the scaling coefficient is
constant and all derivatives are measured against the fixed background.
This establishes the any-sign statement within these neighbourhoods.

The conclusion does not exclude larger corrections tending to zero,
different degenerations, or distant Einstein metrics. In particular
the kernel directions with B=0 survive this receiver. The note preserves
that limitation explicitly. The only textual issue observed is the
missing backslash in `qquad` in equation (3.2); it does not affect the
mathematical argument.
