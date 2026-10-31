# Round 2: all invariant Jacobi modes and their coupled transfer source

Date: 2026-09-19. All work and checks are local. The qiushi-yau26 Skill was
read in full for this round. No live Skill, service, or Session was changed.

There are three substantive results here: a complete bounded-kernel
classification in the angularly invariant double-cylinder model; the
quadratic source and its two coupled length projections for every mode in
that kernel; and a second-order correction solving every tensor block in
the complete model. They do not identify the full global E_D kernel or
produce a closed exact Einstein metric.

## 1. Model and all ten tensor components

Use unit angular periods; angular invariance makes their sizes irrelevant.
Put

    g0=dt^2+cosh(t)^2 dy^2+du^2+cosh(u)^2 dx^2,
    f(t)=sech(t)^2, r(u)=sech(u)^2,
    J(v)=arctan(sinh(v)), J'=sech(v), J(+infinity)-J(-infinity)=pi,
    P_t=partial_t^2+tanh(t)partial_t,
    P_u=partial_u^2+tanh(u)partial_u.

The orthonormal coframe is `(dt,cosh(t)dy,du,cosh(u)dx)`. Write g1,g2 for
the two factor metrics and

    T1=(e0)^2-(e1)^2,  S1=e0 tensor e1+e1 tensor e0,
    T2=(e2)^2-(e3)^2,  S2=e2 tensor e3+e3 tensor e2.

The Bianchi-gauged linearization of `Phi=Ric+g` is

    L=1/2 Delta_E,  Delta_E=nabla* nabla-2 R-circle.

For coefficient functions with arbitrary JOINT dependence on (t,u), the
operator is diagonal on the following ten tensor components:

| Components | Scalar operator for Delta_E |
| --- | --- |
| g1, g2 | `-P_t-P_u+2` |
| T1, S1 | `-P_t-P_u+2-4f` |
| T2, S2 | `-P_t-P_u+2-4r` |
| the four mixed `e_i symmetric-tensor e_alpha` | `-P_t-P_u+2-f-r` |

These formulas are obtained from the product connection. The independent
checker computes the full covariant rough Laplacian and curvature action on
each of the ten components with an unrestricted function F(t,u). No
separation-of-variables assumption enters this verification.

## 2. Complete bounded angularly invariant kernel

**Proposition.** Every smooth angularly invariant tensor H with bounded
g0-relative norm and `L H=0` has the form

    H=f(t)[(a0+a1 J(u))T1+(b0+b1 J(u))S1]
      +r(u)[(A0+A1 J(t))T2+(B0+B1 J(t))S2].            (2.1)

All eight constants are independent. Every displayed field is TT. There
are no bounded trace or mixed modes in this class.

**Proof, including nonseparable solutions.** All scalar operators have
principal part `-partial_t^2-partial_u^2` and bounded drift. The standard
bounded maximum principle follows directly by subtracting a small multiple
of `sqrt(1+t^2+u^2)`, taking its attained maximum, and letting that multiple
decrease to zero. This supplies approximate maximum points with
`(P_t+P_u)z<=o(1)`.

The trace potential is 2. The mixed potential is `2-f-r`, nonnegative,
zero only at (0,0), and bounded below away from zero outside every fixed
neighbourhood of that point. If a mixed coefficient had positive supremum,
approximate maximum points would have to converge to (0,0); the supremum
would be attained. The strong maximum principle then forces a constant,
which the nonzero potential excludes. Apply the same argument to the
negative of the coefficient. Thus both trace and mixed coefficients vanish.

Consider an arbitrary bounded horizontal TT coefficient z(t,u):

    (-P_t-P_u+2-4f)z=0.

Since `(-P_t+2-4f)f=0`, bounded comparison on each half-plane `|t|>=T`,
where `2-4f>=1`, gives `|z(t,u)|<=C f(t)`. On the boundary t=+/-T choose
C to dominate z; the exterior potential is uniformly positive, so the
bounded maximum principle applies also to `z-Cf` and `-z-Cf`. The same
bound holds on the remaining compact t-interval after enlarging C.

Write z=f a. The function a is bounded and satisfies

    T a-P_u a=0,
    T=-partial_t^2+3 tanh(t)partial_t
      =-m^(-1)partial_t(m partial_t), m=sech(t)^3.      (2.2)

The measure m dt is finite. T has kernel the constants and a spectral gap
at least 2 on their orthogonal complement. Here is an explicit proof.
Conjugation by sqrt(m) gives

    T_tilde=-partial_t^2+9/4-(15/4)sech(t)^2=D*D,
    D=partial_t+(3/2)tanh(t).

The partner factorization is

    DD*=2+E*E, E=partial_t+(1/2)tanh(t).

Thus the nonzero spectrum of D*D is at least 2; its kernel is sqrt(m).
This proves the claimed mean-zero gap without a spectral table.

Let abar(u) be the weighted t-average of a. Uniform elliptic estimates for
(2.2), whose coefficients and all their derivatives are bounded, give
bounded derivatives of a. Integration in t is therefore justified, since
m and m times the first derivatives vanish at infinity. It gives
`P_u abar=0`. Let zeta=a-abar and

    w(u)=integral |zeta(t,u)|^2 m(t)dt.

The function w is bounded, smooth, and nonnegative, and

    P_u w=2||partial_u zeta||_m^2+2<T zeta,zeta>_m
          >=4w.

The one-dimensional bounded maximum principle for `-P_u+4` gives w=0.
Thus a is independent of t, and its bounded solutions are exactly
`a0+a1 J(u)`. This argument excludes ALL jointly dependent bounded
solutions, not only separated ones. The vertical TT coefficients are
handled by interchanging t and u. Direct divergence shows that the eight
remaining tensors are TT. This proves the proposition.

In particular, a bounded invariant Jacobi field that tends to zero in
relative norm at all four radial ends is zero. If equal, rather than zero,
normalized end data are imposed on each transfer channel, the four
transfer coefficients a1,b1,A1,B1 vanish, leaving the four constant factor
TT modes. These statements describe specified end data; they do not prove
those end conditions for an arbitrary global E_D perturbation.

## 3. A full invariant L2 gap

The preceding bounded modes are not L2 on the double cylinder. On the
invariant L2 space with measure `cosh(t)cosh(u)dtdu`, the full operator has

    Delta_E >=1/4,       L>=1/8.                        (3.1)

For the horizontal TT block, `-P_t+2-4f` is nonnegative by the ground-state
identity with positive solution f. The remaining scalar factor satisfies
`-P_u>=1/4`, since conjugation by sqrt(cosh(u)) gives
`-partial_u^2+1/4+(1/4)sech(u)^2`. This yields the bound 1/4. Interchange
the variables for the vertical TT block. The trace blocks have a larger
gap. For mixed blocks, each `-P_t-f` and `-P_u-r` is nonnegative by its
positive ground state sech; the additional constant is 2. Taking the
Friedrichs realizations proves (3.1) for all ten invariant components.

For clarity, the scalar lower bound is a finite-energy statement, not a
claim that every bounded scalar is in its domain. For compactly supported
smooth v and w=sqrt(cosh(u))v, integration by parts gives exactly

    integral cosh(u)|v'|^2 du
      =integral [|w'|^2+(1/4+sech(u)^2/4)|w|^2]du
      >=(1/4)integral cosh(u)|v|^2 du.

Density extends this to the Friedrichs form domain. Applying this identity
to almost every t-slice and integrating gives the two-variable lower
bound; no unproved finite-volume or compactness premise is involved.

This is a full model-operator statement. It is not a lower spectral bound
for the closed E_D operator, nor a bound for its maximum-norm inverse.

## 4. An exact nonlinear family realizing all eight tangents

For constants alpha,gamma define a metric on one hyperbolic cylinder by

    D_alpha(v)=sinh(v)^2+exp(-alpha),
    h_(alpha,gamma)=cosh(v)^2/D_alpha(v) dv^2
             +D_alpha(v)(dtheta+gamma sech(v)^3 dv)^2. (4.1)

Its curvature is exactly -1 and its area form is exactly
`cosh(v)dv dtheta`. Indeed use
`U=arsinh(exp(alpha/2)sinh(v))` and then the angular coordinate change with
derivative `gamma sech(v)^3`. The two tangents at zero are respectively
`sech(v)^2 T` and `sech(v)^2 S`.

Set

    a(u)=a0+a1 J(u), b(u)=b0+b1 J(u),
    A(t)=A0+A1 J(t), B(t)=B0+B1 J(t).

Use (4.1) in both blocks:

    g_s=h_(s a(u),s b(u)) on (t,y)
         +h_(s A(t),s B(t)) on (u,x).                 (4.2)

This is an actual smooth positive metric for small s, has exactly the
product volume form, and has first variation (2.1). Each block is
hyperbolic when its other coordinate is held fixed. Both blocks depend on
both radial variables, so the cross Ricci terms must be retained.

## 5. Every second-order block and the coupled projection

Write `Phi(g_s)=s^2 D+O_Ck(s^3)` for every fixed k. First take just the
fibre path, setting a=b=0. Dots denote t derivatives; write j=tanh(u).
The complete source in the background orthonormal frame is

    D00=-(Adot^2+Bdot^2)r^2/2, D11=0,
    D22=Adot^2 r/2-(Adot^2+Bdot^2)r^2/2, D33=-D22,
    D23=Adot Bdot r^2,
    D03=2 A Bdot j r^2,                               (5.1)

with symmetric entries and all others zero. In particular the mixed block
does not vanish for a general simultaneous length/twist transfer. The
base-only source is obtained by interchanging the factor labels.

For reproducibility, the fibre metric's second Taylor coefficient in its
background orthonormal frame is

    N22=A^2(r^2-r/2)+B^2 r^2,
    N23=-AB r^2, N33=A^2 r/2.

The vertical equation gives
`D_FF=-(Nddot+tanh(t)Ndot)/2+(Hdot)^2/2`.
The mixed equation follows from the actual fibre shape divergence; it
cannot be recovered from just the diagonal Ricci blocks.

For the simultaneous two-block family (4.2), the cross source is as follows.
Put k=tanh(t), j=tanh(u), and use subscripts u or t for derivatives:

    D_cross=-f r times

    [[ A a_u j,  A b_u j,  A_t a_u/2, B_t a_u/2],
     [ A b_u j, -A a_u j,  A_t b_u/2, B_t b_u/2],
     [ A_t a_u/2,A_t b_u/2,A_t a k,   B_t a k  ],
     [ B_t a_u/2,B_t b_u/2,B_t a k,  -A_t a k  ]].      (5.2)

The checker obtains this by expanding the coordinate Christoffel and Ricci
formulas, including all inverse-metric and connection cross terms. Both
(5.1) and (5.2) independently satisfy the full quadratic Bianchi identity
`-div D+(1/2)d tr D=0`.

Now let `Q1=f T1`, `Q2=r T2`. Both are actual bounded TT model Jacobi
fields, but neither is L2. All the following pairings converge absolutely.
With the product measure and unit angular periods, direct integration gives

    I1=integral <D,Q1>
      =(pi^2/8)(a1^2-3b1^2-A1^2-B1^2),

    I2=integral <D,Q2>
      =(pi^2/8)(A1^2-3B1^2-a1^2-b1^2).               (5.3)

The cross integrands are exactly

    <D_cross,Q1>=-2 A a_u tanh(u) f^2 r,
    <D_cross,Q2>=-2 A_t a tanh(t) f r^2.

Their integrals vanish by parity, since J is odd and each of a_u,A_t is a
constant times sech of its variable. Thus (5.3) includes, rather than
ignores, the complete cross contribution.

The sum is particularly informative:

    integral <D,Q1+Q2>=-(pi^2/2)(b1^2+B1^2)
       =-1/2[(Delta b)^2+(Delta B)^2],                (5.4)

where each Delta is the end-to-end change along the corresponding radial
coordinate. A base length transfer can cancel the fibre contribution to
I1 alone; it cannot cancel both detectors if either twist transfer is
nonzero. This is a coupled statement covering all eight bounded invariant
modes in this explicit nonlinear completion.

For comparison, the single-fibre source has

    integral <D,Q1>=-pi^2(A1^2+B1^2)/8,
    integral <D,Q2>= pi^2(A1^2-3B1^2)/8,
    integral <D,r S2>=3pi^2 A1 B1/4.

Thus the fibre length detector by itself is not sign-definite. Retaining
both factors is essential.

## 6. All-block second-order repair exists, with compulsory end flux

Every coefficient of D and every fixed derivative is bounded by a constant
times `sech(t)sech(u)`. This follows from (5.1), its swapped copy, and
(5.2); the amplitudes a,b,A,B are bounded and their derivatives are
constant multiples of sech. Thus D is smooth, belongs to L2 with all fixed
derivatives, and is Bianchi closed.

The full gap (3.1) supplies a unique invariant L2 correction

    K=-L^(-1)D=-integral_0^infinity exp(-vL)D dv,
    ||K||_2<=8||D||_2.                               (6.1)

This is a convergent definition using the full ten-component operator, not
a trial compression or an assumed Schur inverse. Elliptic estimates on
uniform local covers give smoothness and boundedness of all fixed
derivatives. To remove the gauge, use the exact Einstein-background identity

    beta L=(1/2)(Delta_H+2) beta.

Since beta D=0 and beta K is L2, positivity of `Delta_H+2` gives beta K=0.
Therefore K solves the actual equation `D Phi_g0 K=-D`. Consequently

    g_s+s^2 K is positive definite for small s,
    Phi(g_s+s^2 K)=O_Ck(s^3).                         (6.2)

Equation (6.2) is an actual formal correction satisfying ALL leading
Ricci blocks on the complete model. It generalizes the three-scalar
single-twist correction in the manuscript to arbitrary combinations of
the eight bounded invariant first modes. It does not assert a closed
gluing theorem or convergence of a full nonlinear series.

There is no contradiction with (5.4). On an exhausting rectangle define
the Green boundary pairing

    Flux(K,Q)=1/2 integral_boundary
                   [<K,nabla_nu Q>-<nabla_nu K,Q>].

Since LQ=0 and LK=-D, its limit for Q=Q1+Q2 is

    Flux(K,Q1+Q2)=-integral <D,Q1+Q2>
                 =(pi^2/2)(b1^2+B1^2).              (6.3)

Thus a nonzero twist forces a nonzero second-order end flux. Decay in L2
does not remove it because the test fields are not L2.

**Conditional obstruction.** No Bianchi-gauge second-order repair of
(4.2) with nonzero twist transfer can have vanishing Green pairings at all
ends. For an arbitrary actual repair, `D Phi K=L K-delta* beta K=-D`,
pairing the additional gauge term against TT Q contributes the boundary
integral

    GaugeFlux(K,Q)=integral_boundary Q(nu,beta K).

The general identity is therefore
`lim[Flux(K,Q)-GaugeFlux(K,Q)]=-integral <D,Q>`. Outside Bianchi gauge,
both the Green and gauge boundary contributions must vanish for the
conditional contradiction. No arbitrary-gauge assertion follows from
vanishing Green flux alone.

In particular there is no such compactly supported repair, or one with K
and its first derivatives decaying like
`exp(-(1+eta)(|t|+|u|))` for any eta>0. Those explicit decay bounds force
both types of boundary pairing to vanish. The actual Bianchi-gauge L2
repair (6.1) necessarily falls outside that faster-decay class.

This identifies the remaining global task as the reception and matching
of the compulsory end flux. It does not label that flux an obstruction
without proving the global matching conditions.

## 7. Relation to the epsilon scales and fixed E_D

In the manuscript's balanced construction the local unfolded fibre shear is

    H_twist=(2/pi) tau(t) r(u) S2,
    tau(t)=[J(t)+pi/2]/pi.

It is precisely one of the transfer fields in (2.1), at amplitude epsilon.
Here B1=2/pi^2 and all other transfer coefficients vanish. Equations (5.3)
give `I1=-1/(2pi^2)` and `I2=-3/(2pi^2)`, agreeing with the two source/flux
coefficients in the long manuscript. Their sum is `-2/pi^2`.

An epsilon^(3/2) correction is smaller than this existing order-epsilon
transfer. If its leading profile is bounded and angularly invariant, and
the gauge-fixed leading equation converges on the double-cylinder model,
the classification (2.1) applies. There are no additional bounded mixed or
trace channels hidden in that model. This does not prove that every actual
global correction has such a leading limit, is angularly invariant, or
satisfies any proposed end condition.

At amplitude epsilon, changing transfer coefficients can change the
leading twist itself. Keeping the same marked Dehn twist imposes a global
matching problem; setting its model transfer to zero is not an admissible
topology-preserving step without a separate matching argument.

## 8. Collapsing normalization: a counterexample and a sufficient interface

There is a useful closed-product test for the possible positive base-length
transfer. Let F_epsilon be a closed hyperbolic fibre pinching one
nonseparating curve, with all other moduli controlled, and assume
`lambda1(F_epsilon)>=c>0`. The manuscript gives the corresponding
nonseparating Poincare argument in `20260912.tex:4010`; the conditional
argument below retains the spectral assumption explicitly.

On the exact closed product, normalize a base TT Jacobi tensor q_B by
`||q_B||_2=1`. For a tensor `h=v q_B`, with v a scalar on the fibre,

    L h=(1/2)(Delta_F v)q_B,
    ||v-average(v)||_L2(F)<= (2/c)||Lh||_L2(product).  (8.1)

An o(1) residual in (8.1), even with identical thick-mouth values, does
NOT exclude the local transfer a1. Here is a concrete counterexample.
Write the collapsing collar metric as
`du^2+ell^2 cosh(u)^2 dx^2`, with width R satisfying
`ell exp(R)` bounded above and below. Choose a smooth even cutoff chi
equal to 1 on [-1/2,1/2] and supported in (-3/4,3/4). Define

    v_ell(u)=J(u) chi(u/R),

and extend it by zero beyond the collar. It is zero near both thick
mouths, has mean zero by parity, and has uniform local smooth control.
On each fixed core interval it tends to J(u), so its pointed transfer
coefficient is 1. Yet P_u J=0 and the product rule gives

    P_u v_ell
      =J[chi''(u/R)/R^2+tanh(u)chi'(u/R)/R]
         +2 sech(u)chi'(u/R)/R.

This vanishes off the transition bands and has magnitude at most C/R.
Their collar volume is at most `C ell exp(3R/4)<=C ell^(1/4)`. Hence

    ||Delta_F v_ell||_2<=C ell^(1/8)/R ->0,
    ||v_ell||_2<=C ell^(1/8) ->0.                     (8.2)

There is no conflict with a uniform scalar spectral gap. Collapsing-core
normalization, not just the equality of thick end values, is essential.

A sufficient, strictly stronger hypothesis is

    ||L(v q_B)||_L2(product)=o(sqrt(ell)),
    ||q_B||_L2(base)=1.                              (8.3)

By (8.1), `||v-average(v)||_2=o(sqrt(ell))`. Dividing the squared L2
integral on any fixed inner collar interval by ell shows convergence to
the same constant there. Thus if v has a bounded smooth pointed limit
`a0+a1 J(u)`, condition (8.3) forces a1=0. The interval's normalized
measure is the fixed positive density cosh(u)du dx, so this step does not
mistake a collapsing L2 estimate for pointwise control.

For an unnormalized base TT field with L2 mass m_B, the corresponding
required residual is `o(m_B sqrt(ell))`. To apply this interface to E_D
one must derive its actual projected-Jacobi residual, control the
connection and gauge couplings, and prove the stated normalized smallness.
None follows from fixed topology or the local kernel classification.
Separating degeneration also need not have the assumed scalar gap.

## 9. Verification and source boundary

Executed locally, both passing:

    python round2_construction_check.py
    python round2_construction_cross_check.py

The first verifies all ten Jacobi sectors with unrestricted joint radial
dependence, the entire fibre source including its mixed block, its Bianchi
identity, the projection integrals, and the factorization for the
nonseparable-kernel proof. The second independently expands the actual
two-block Christoffel/Ricci cross variation, checks its full Bianchi
identity, and verifies the coupled projection formula.

The source interfaces extended here can be located in
`20260916_construction.tex:472-623` (all Ricci blocks), `:625-699` (balanced
double collar), `:701-845` (three-scalar correction), `:849-871` (end flux),
`:873-943` (global TT projection), and `:1130-1215` (product kernel and
maximum-norm inverse); and `20260912.tex:3930-3942` (restricted response
space), `:4004-4012` (product gap and nonseparating scalar estimate).
These are manuscript source locations, not independent certification of
all their global claims. The present independently checked calculation
does not transfer the model L2 gap to the global collapsing E_D
maximum-norm problem.
