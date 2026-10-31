# Independent review of rigidity.md

Date: 2026-09-19. Read-only review of the other agent's derivation; this
review did not edit rigidity.md or rigidity_check.py.

Verdict: I found no sign, normalization, matrix-positivity, or numerical-radius
failure in the stated spectral exclusion lemma. The stronger global scalar
multiplier obstruction also passes an independent first-jet check. The
conclusions remain restricted exactly as stated: neither is an average
density gap or a solution of the arbitrary-collapse problem.

## Primary formulas and independent reconstruction

I checked the public classical formulas directly against Peng Wu,
*Einstein four-manifolds with self-dual Weyl curvature of nonnegative
determinant*, Section 2:
<https://arxiv.org/html/1903.11818>.
The Laplacian is `tr Hess`, the Weyl norm is the operator Hilbert--Schmidt
norm, and the eigenforms have squared length two. Wu's eigenvalue equations
give exactly the displayed gradient equations and invariant equations for
`Delta x` and `Delta y`, including the cross-term coefficients.

The independent script `rigidity_review_check.py` reconstructs those two
invariant equations from the individual eigenvalue equations. It does not
import the author's checker or its multiplier matrix. The determinant
reaction simplifies to `(3/2)s y-x^2` after imposing trace zero; the norm
reaction is `s x-36y`. At the target these yield the claimed polynomial
reaction `1/16`. This independently excludes the common factor-four and
opposite-Laplacian mistakes.

I also checked the source of the non-harmonic identity, Corollary 2.3 and
equation (2.5) in Catino--Mastrolia--Monticelli--Punzo:
<https://cvgmt.sns.it/media/doc/paper/4075/WHW-metrics.pdf>.
Dividing its four-index identity by four leaves coefficient `-1` on the
ordinary three-index divergence norm, as rigidity.md states; Cotton and
divergence differ by factor `-2` in the cited convention.

## Multiplier, matrix, and radius

Starting from the invariant equations and applying the chain rule to

    f=x+36y+24(x-1/24)^2,

I recovered the center matrix

    [[ 8,-8,-2],[-8,32,-8],[-2,-8,8]].

The leading minors after subtracting the identity are `7,153,243`, hence
the claimed strictly positive margin follows from Sylvester's criterion.

The perturbation bounds can be reconstructed without numerical sampling:

* A gap changes by at most `2 eps`; its center absolute value is at most
  `1/4`. Thus its square changes by at most `eps+4 eps^2`.
* With `|x-x0|<=eps`, a diagonal matrix entry changes by at most
  `(384+144+192)eps+768eps^2`.
* An off-diagonal entry changes by at most
  `(96+72+192)eps+768eps^2`.
* The maximum absolute row sum is therefore at most `1443eps` at
  `eps=1/10000`; it is strictly below `1/2`.
* Writing `U=-4x-36y`, the reaction variation is bounded by
  `2(29/5)eps+6eps+(54/5)eps+3eps+36eps^2`, namely
  `(157/5)eps+36eps^2`.

Consequently the potential remains greater than `1/32` and the derivative
matrix remains greater than `(1/2)I` throughout the asserted box. The use
of a globally smooth polynomial, rather than individual eigenvectors,
justifies continuation of the scalar Laplacian inequality across changing
multiplicity strata. Closedness then gives the contradiction by integration.

## The radial first jet and the stronger multiplier obstruction

I constructed a tensor first jet explicitly using self-dual two-form matrices
in an oriented orthonormal four-frame. Direct contraction of all components
of its covariant derivative gives `div W+=0`. Its norms are exactly

    |nabla A|^2=10,  |grad |A||^2=6,
    |orbit-tangent part|^2=4.

Thus the ratio of the orbit contribution to the radial contribution is
`2/3`. This check avoids assuming that the formal X,Y,Z values happen to
satisfy the first-order Bianchi equation. Interior-product signs depend on
the chosen matrix convention, but simultaneous reversal has no effect on
the invariant quadratic form; the checker fixes signs by direct divergence.

For an invariant function restricted to the negative repeated-eigenvalue
ray, write `psi(u)=f(u diag(-2,1,1)/sqrt(6))`. Its gradient on the ray is
radial by isotropy. The Hessian on the above tangent jet is therefore

    [psi''(u)+(2/(3u))psi'(u)] |grad u|^2.

This confirms the differential inequality used in the new proposition.
Global C2 regularity and invariance at zero give `psi'(u)=O(u)`, so
`(u^(2/3)psi')'>=0` forces `psi'>=0`. The reaction at the target is
`-(3/2)u0 psi'(u0)<=0`. No curvature-growth assumption is needed.

I additionally checked, directly as a matrix function, that the first and
second derivatives of `det(A)/|A|^3` vanish on each of these radial-plus-orbit
tangent directions. This confirms the homogeneous corollary independently.
The assertion concerns algebraically allowed first jets, not their
extension to closed Einstein metrics; that distinction is retained in the
author's statement.

## High-frequency source and remaining scope

For covector `xi=e1` and `q=diag(0,1,-1,0)`, I recomputed the Cotton
principal symbol and its self-dual projection. Their squared norms are
`4` and `2`, respectively. Thus the proposed high-frequency perturbation
does not accidentally cancel the required source. Its metric amplitude
`eps/k^2`, Ricci amplitude `eps`, and Cotton amplitude `eps*k` have the
stated scaling; at `eps=1/j`, `k=j^2` the Cotton energy grows like `j^2`.
The smooth fixed support, noncritical phase, and transverse trace-free
polarization give the required actual local metric construction. This
tests a missing derivative estimate, not the target zero-density regime.

Likewise the concentration example is explicitly an algebraic curvature
field example. It proves failure of a norm-only passage from L2 control to
the cubic potential; it makes no metric-realizability claim. That limitation
is mathematically essential and is stated correctly.

Executed both `rigidity_check.py` and `rigidity_review_check.py` locally;
both passed. The latter's checks are independent reconstruction, direct
four-index divergence, and exact principal-symbol calculations.

No correction to the stated claims is requested. Any later use must still
preserve their boundaries: the pointwise spectral box is not forced by a
small integral density, and the multiplier obstruction excludes only a
globally sign-coercive invariant scalar strategy. Coupled, nonlocal,
singular, and controlled-error strategies remain outside that obstruction.
