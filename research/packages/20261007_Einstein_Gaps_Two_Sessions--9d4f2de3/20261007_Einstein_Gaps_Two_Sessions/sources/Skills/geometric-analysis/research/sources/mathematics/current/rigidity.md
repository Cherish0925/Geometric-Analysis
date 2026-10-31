# A direct Weitzenbock attack on the forbidden Weyl spectrum

Date: 2026-09-19. This is a bounded mathematical investigation, not a proof of
the arbitrary-collapse density gap or of Yau's problem. The substantive outputs
are an explicit spectral exclusion lemma, a multiplier obstruction, and two
precise failures of estimates one might otherwise use to close the gap.

## Conventions and classical input

Let A=W+ be the self-dual Weyl operator on an oriented Riemannian four-manifold.
Use the Hilbert--Schmidt operator norm, x=|A|^2, y=det A, scalar curvature s,
and Delta=tr Hess. The four-index Weyl tensor has squared norm 4x. The target is

    A0 = diag(-1/6, 1/12, 1/12),  x0=1/24,  y0=-1/864,  s=-4.

For div W+=0, the classical equations are

    Delta A = (s/2) A - 6 A^2 + 2 |A|^2 I,
    (1/2) Delta |A|^2 = |nabla A|^2 + (s/2)|A|^2 - 18 det A.

The first equation is understood with the induced connection on Lambda+;
the displayed invariant formulas below fix all signs and normalizations.
For the eigenframe differential identities used here, see Peng Wu,
*Einstein four-manifolds with self-dual Weyl curvature of nonnegative
determinant*, Section 2, pp. 2--4:
<https://arxiv.org/pdf/1903.11818>.
For the general, non-harmonic integral identity and Cotton conventions see
Catino--Mastrolia--Monticelli--Punzo, *Four dimensional closed manifolds admit
a weak harmonic Weyl metric*, Corollary 2.3 and equations (2.2), (2.5):
<https://cvgmt.sns.it/media/doc/paper/4075/WHW-metrics.pdf>.
Only these public classical formulas were searched externally; private
manuscript statements were not included in searches.

## 1. The ordinary norm potential has the wrong sign

At A0 the algebraic term in the norm identity is exactly

    (s/2)x0 - 18 y0 = -1/12 + 1/48 = -1/16.

In fact A0^2=-(1/12)A0+(1/72)I, so the operator reaction at A0 is

    -2 A0 - 6 A0^2 + 2 x0 I = -(3/2) A0.

Consequently, even if cubic curvature could be passed to the limit, integration
of the ordinary norm identity would prescribe an average gradient energy
1/16, not yield a contradiction. At exact constant spectrum the first-order
Bianchi equations rule out that gradient; approximate spectral constancy in
L2 does not by itself rule out high-frequency gradients.

## 2. An explicit pointwise spectral exclusion without compactness

**Lemma.** On every closed oriented four-manifold with s=-4 and div W+=0,
there is a point where at least one ordered eigenvalue of W+ differs from
(-1/6,1/12,1/12) by more than 10^(-4). In particular this holds for every
closed Einstein four-manifold normalized by Ric=-g. No volume, diameter,
injectivity-radius, or topological assumption is needed.

**Proof.** Work first on the open dense set on which eigenvalue multiplicities
are locally constant. Let lambda1<=lambda2<=lambda3, and use the classical
eigenframe one-forms a,b,c to set

    X=(lambda1-lambda2) i_(a#) omega3,
    Y=(lambda2-lambda3) i_(b#) omega1,
    Z=(lambda3-lambda1) i_(c#) omega2.

The eigenforms have squared length two; raising a final index identifies these
one-forms with vectors. The harmonic-Weyl equations give

    grad lambda1=-X+Z, grad lambda2=X-Y, grad lambda3=Y-Z,

    Delta x=8(|X|^2+|Y|^2+|Z|^2)
            -4(<X,Y>+<X,Z>+<Y,Z>) + sx-36y,

    Delta y=-4 lambda3 |X|^2-4 lambda1 |Y|^2-4 lambda2 |Z|^2
            -4 lambda2 <X,Y>-4 lambda1 <X,Z>-4 lambda3 <Y,Z>
            +(3/2)sy-x^2.

Choose the globally smooth spectral polynomial

    f(x,y)=x+36y+24(x-1/24)^2,   a0(x)=f_x=1+48(x-1/24).

Set p=lambda1-lambda2, q=lambda2-lambda3, r=lambda3-lambda1. Then

    Delta f = sum_ij M_ij <V_i,V_j> + P(x,y),  (V1,V2,V3)=(X,Y,Z),

where

    M11=8a0-144 lambda3+192p^2,
    M22=8a0-144 lambda1+192q^2,
    M33=8a0-144 lambda2+192r^2,
    M12=-2a0-72 lambda2+192pq,
    M13=-2a0-72 lambda1+192pr,
    M23=-2a0-72 lambda3+192qr,

    P=(-4x-36y)a0-216y-36x^2.

At the target,

    M0 = [[ 8, -8, -2],
          [-8, 32, -8],
          [-2, -8,  8]],             P0=1/16.

The leading principal minors of M0-I are 7,153,243. Thus M0>I. Suppose now
that every eigenvalue differs from its target by at most epsilon=10^(-4).
Expansion of x and y gives

    |x-x0| <= (2/3)epsilon+3epsilon^2 <= epsilon,
    |y-y0| <= (5/144)epsilon+(1/3)epsilon^2+epsilon^3 <= epsilon/20.

It follows that |a0-1|<=48epsilon. Each diagonal entry of M-M0 has magnitude
at most 720epsilon+768epsilon^2 <=721epsilon; each off-diagonal entry has
magnitude at most 360epsilon+768epsilon^2 <=361epsilon. Therefore

    ||M-M0||op <=1443epsilon <1/2,   so M >=(1/2)I.

Also |-4x-36y+1/8| <=(29/5)epsilon, |a0|<2, and

    |P-P0| <=(157/5)epsilon+36epsilon^2 <32epsilon.

Hence P>1/32 throughout this spectral box, and

    Delta f >= (1/2)(|X|^2+|Y|^2+|Z|^2)+1/32 >=1/32.

Although the eigenframes need not extend over multiplicity changes, f is a
smooth polynomial in W+. The inequality for Delta f extends by continuity
from the open dense multiplicity strata. Integration on the closed manifold
contradicts integral Delta f=0. This proves the lemma.

The script rigidity_check.py verifies the exact center calculation, the
principal minors, and every numerical inequality in these box estimates.
It does not certify geometric realizability or the classical PDE formulas.

**Scope.** This is a quantitative pointwise exclusion, not an average-density
gap. Small average density does not force the entire manifold into the
spectral box. Outside it, the derivative quadratic form of this multiplier
need not have a useful sign. Moreover f contains fourth-order curvature
growth. The lemma therefore cannot be substituted for the missing
arbitrary-collapse argument without additional work. No literature novelty
claim is made.

## 3. An obstruction to global invariant scalar multipliers

There is a stronger obstruction than a restriction on curvature growth.

**Proposition.** Let f be a C2, orthogonally invariant real function on the
entire vector space of trace-free symmetric 3-by-3 matrices. Suppose its
derivative quadratic form in the harmonic-Weyl equation is nonnegative on
every algebraically admissible harmonic-Weyl first jet. Then its algebraic
reaction at A0, with s=-4, cannot be positive.

**Proof.** Restrict to the negative repeated-eigenvalue ray

    A(u)=(u/sqrt(6))diag(-2,1,1),  u>0,  psi(u)=f(A(u)).

On this ray, take the first jet Y=0,Z=-X, so that

    grad lambda1=-2X, grad lambda2=X, grad lambda3=X,
    |grad u|^2=6|X|^2,   |nabla A|^2=10|X|^2.

The derivative of A consists of radial and orbit-tangent pieces. Isotropy
of the repeated eigenvalue implies that df on the ray is radial. Consequently
its Hessian on this jet is the same as that of the radial function psi(|A|).
Equivalently, f-psi(|A|) and its first derivative vanish on the ray's
orthogonal-conjugation orbit, so its Hessian vanishes on the tangent jet.
The derivative quadratic form is therefore

    Q_f=[psi''(u)+(2/(3u))psi'(u)] |grad u|^2.

Its assumed nonnegativity implies

    (u^(2/3)psi'(u))' >=0.

Smooth invariance at the zero matrix forces df(0)=0: the only invariant
linear functional on trace-free symmetric matrices is zero. Thus psi'(u)=O(u)
as u decreases to zero. Integrating the last monotonicity inequality from
zero yields psi'(u)>=0 for every u>0. At the target u0=1/sqrt(24), the
operator reaction is -(3/2)A0, and hence

    P_f(A0)=-(3/2)u0 psi'(u0)<=0.

This proves the proposition. The assertion concerns the sign on all
algebraically allowed first jets; it does not assume that every such jet
extends to a global Einstein metric.

Thus a globally smooth invariant scalar multiplier cannot simultaneously
have a globally nonnegative derivative term and a positive reaction at A0.
This includes nonhomogeneous multipliers of arbitrary growth. Any extension
of the successful local polynomial must accept a negative derivative term
somewhere, or change the method, or be singular. For the polynomial in
Section 2, the radial derivative coefficient tends to -10/3 as u tends to
zero, displaying the necessary loss directly. Cutting the multiplier off
does not remove the need to estimate this derivative cost.

### A local homogeneous corollary

Consider any C2, orthogonally invariant, degree-two homogeneous function near
the nonzero target orbit. Write

    f(A)=x phi(z),  z=y/x^(3/2),  z0=-1/(3 sqrt(6)).

Since the algebraic operator reaction at A0 is -(3/2)A0, Euler's homogeneity
identity gives its contribution to Delta f as

    P_f(A0)=-3 f(A0)=-(1/8)phi(z0).

There is a permissible harmonic-Weyl first jet at the repeated eigenvalue
with Y=0 and Z=-X. The first-order identities then read

    grad lambda1=-2X, grad lambda2=X, grad lambda3=X.

These are radial changes of the eigenvalues; the eigenframe connections
account for the additional orbit-tangent part of nabla A. Directly from the
formulas above,

    |grad |A||^2=6|X|^2,   |nabla A|^2=10|X|^2.

At z0 the first derivative of z as a matrix function vanishes; its Hessian
annihilates this radial-plus-orbit tangent jet. Thus the derivative part of
Delta f for this jet is

    Q_f=(10/3)phi(z0)|grad |A||^2=20 phi(z0)|X|^2.

For Q_f to be nonnegative on every first jet allowed by the harmonic-Weyl
equation, phi(z0)>=0 is necessary. For P_f(A0)>0, phi(z0)<0 is necessary.
These conditions are incompatible. Unlike the proposition, this corollary
needs the multiplier only near the target orbit; it uses degree-two
homogeneity instead of regularity down to the zero matrix.

This rules out a precise class of direct sign-coercive arguments: a C2
invariant homogeneous degree-two multiplier cannot simultaneously have a
nonnegative full derivative quadratic form and a positive potential at A0.
It does not rule out nonhomogeneous, singular, nonlocal, or coupled multipliers.
For example, inverse powers of |A| change the radial sign analysis, but
introduce uncontrolled zero sets; the polynomial in Section 2 uses radial
convexity at the expense of higher curvature growth.

## 4. The Ricci-derivative term survives integration

For an arbitrary smooth closed oriented four-metric, let J=div W+ with the
ordinary three-index tensor norm, while retaining the operator norm for A.
The exact integrated identity, with this mixed but explicit convention, is

    0 = integral [ |nabla A|op^2 - |J|tensor^2
                    +(s/2)|A|op^2 -18 det A ].

Indeed, divide the four-index formula of Corollary 2.3 in the cited paper by
four; W+_ijkl W+_ijpq W+_klpq=24 det A. Equivalently, if the divergence norm
is rescaled by a factor 1/2, its coefficient is -4.

Put E=Ric+g and e=tr E=s+4. With the source's Cotton convention,

    C_ijk=nabla_k E_ij-nabla_j E_ik
          -(1/6)[(nabla_k e)g_ij-(nabla_j e)g_ik],
    J=-(1/2) C+.

Thus integration does not remove derivatives of E: it creates their squared
Cotton projection. Moving derivatives onto a test tensor would require
control of derivatives of that tensor. No estimate of this source by
||E||infinity alone is legitimate.

Here is an actual geometric high-frequency obstruction to such an estimate.
Fix any closed negative Einstein four-metric g0, for example the product of
two closed surfaces of curvature -1. In a fixed coordinate patch choose a
smooth phase theta with dtheta nonzero, a cutoff chi, and a nonzero symmetric
tensor q with tr_(g0)q=0 and q(grad theta,.)=0. Arrange that the Cotton
principal symbol of q is nonzero on a smaller patch. At one orthonormal
frame this is simply dtheta=e1 and q=diag(0,1,-1,0). For epsilon small and
integer k large set

    g_(epsilon,k)=g0+(epsilon/k^2) chi sin(k theta) q.

This is positive definite and equals g0 outside the patch. The principal
symbol of linearized Ricci, on this transverse trace-free q, gives

    Ric(g_(epsilon,k))+g_(epsilon,k)
       =(epsilon/2)|dtheta|^2 chi sin(k theta)q
         +O(epsilon/k+epsilon^2/k^2)

uniformly, where harmless smooth zeroth-order terms are included in the
remainder. Its scalar leading symbol vanishes. Differentiating the Ricci
principal term yields a nonzero Cotton principal symbol of size epsilon*k;
the next derivative errors are O(epsilon+epsilon^2/k). On the region where
chi is fixed and nonzero, oscillatory averaging therefore gives

    ||Ric(g_(epsilon,k))+g_(epsilon,k)||infinity <=C epsilon,
    ||Rm(g_(epsilon,k))||infinity <=C,
    integral |C(g_(epsilon,k))|^2 >= c epsilon^2 k^2

for sufficiently large k. The same conclusion holds for the self-dual
Cotton projection in the indicated polarization: its principal symbol is
nonzero. Taking epsilon=1/j and k=j^2 makes the residual tend to zero and
the Cotton L2 energy grow at least as j^2, on a fixed compact manifold with
uniform curvature bounds.

This family is not a zero-density sequence: the background Einstein metric
does not have the forbidden spectrum. It disproves the intermediate bound
of Cotton energy by small Ricci residual and curvature energy, even under
much stronger noncollapse and curvature assumptions. It is not a
counterexample to the targeted geometric density-gap conjecture.

## 5. Quadratic density does not control cubic concentration

There is also a sharp functional, rather than geometric, obstruction to
passing the norm-identity potential to the limit using only the manuscript's
quadratic budget. On a fixed unit-volume domain consider smooth trace-free
symmetric matrix fields

    A_j=A0+t_j b_j B,  B=diag(2,-1,-1),  t_j ->infinity,

where b_j is a fixed smooth nonnegative bump rescaled to a ball of volume
comparable to t_j^(-5/2). Formally fix Ric=-g and s=-4 at the algebraic
curvature-tensor level. Every term of the calibration density is zero at
A0 and grows at most quadratically in A_j. Thus

    integral D_j = O(t_j^2 t_j^(-5/2)) = O(t_j^(-1/2)) ->0,
    integral |A_j-A0|^2 ->0,
    integral det A_j - det A0
       = c t_j^3 t_j^(-5/2)+lower-order terms ->+infinity.

Here c>0 because det B=2 and the cubic bump integral is positive. The
four-dimensional support radius is of order t_j^(-5/8). This is the
standard L2-versus-L3 concentration threshold, now expressed for the exact
Weyl invariants in the proposed proof. Smoothing the bump does not change
the powers.

These are algebraic curvature fields, not asserted to be the curvature of
an actual Einstein or near-Einstein metric. They rigorously invalidate a
purely norm-based inference from vanishing quadratic density plus bounded
L2 curvature to convergence of the cubic potential. Differential
regularity could exclude them, but that is additional mathematics rather
than a consequence of the displayed integral budgets.

## Conclusion of this attack

The direct differential route yields the explicit pointwise exclusion in
Section 2. It does not close the minimal density-aware harmonic-patch
implication. A successful integral replacement must both retain/control the
Cotton source and overcome concentration or avoid cubic terms altogether.
The ordinary norm identity and globally smooth invariant scalar multipliers
with everywhere nonnegative derivative term fail for the precise reasons
proved above. Even locally, degree-two homogeneous invariant multipliers
cannot supply the two desired signs. This
locates the missing estimate more narrowly than an unspecified appeal to
collapse regularity, without asserting that all direct methods are impossible.
