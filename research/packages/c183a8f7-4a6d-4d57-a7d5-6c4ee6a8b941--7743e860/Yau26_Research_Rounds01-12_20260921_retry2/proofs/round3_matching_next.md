# A two-face matching law with movable cylinder parameters

19 September 2026. This note advances the closed E_D matching question
using the exact complete-model family from `round3_construction.md`.
It proves a conditional finite-dimensional matching law and identifies
an explicit exterior quadratic functional that a possible larger closed
correction must supply. It does not prove global Einstein nonexistence.

## 1. Every bounded second-order model repair, with its end shifts

Retain the eight first-order parameters
`z=(a0,a1,b0,b1,A0,A1,B0,B1)` and let

    g[s z]=g0+s H[z]+s^2 N[z]+O(s^3),
    Ric(g[s z])+g[s z]=s^2 D[z]+O(s^3),
    K[z]=-L^(-1)D[z], beta_0 K[z]=0.

The eight-parameter exact family has correction
`k[s z]=s^2 K[z]+O(s^3)` in the weighted space proved in the preceding
note. Suppose Z is any smooth bounded invariant second-order correction
in the background Bianchi gauge:

    LZ=-D[z], beta_0 Z=0.                                  (1.1)

Then Z-K is a bounded invariant Jacobi field. The complete kernel
classification in round two therefore proves

    Z=K[z]+H[zeta],                                       (1.2)

for some eight constants zeta. This is a classification of all bounded
corrections satisfying (1.1), not just a convenient finite-dimensional
trial space. It is also realized by actual exact metrics: use the
parameter curve `G[s z+s^2 zeta]` and compare with `g[s z]`.

Write the horizontal and vertical length coefficients in H[zeta] as

    c(u)=c0+c1 J(u), C(t)=C0+C1 J(t),
    c_+/-=c0+/-pi c1/2, C_+/-=C0+/-pi C1/2,
    Delta c=c_+-c_-=pi c1, Delta C=C_+-C_-=pi C1.           (1.3)

The other four constants in zeta are the second-order twist shifts. They
are orthogonal to the two length detectors below. A constant length shift
changes the common end value; a difference of length shifts changes the
two opposite derivative fluxes.

## 2. The precise matching matrix

Let Q1=f T1 and Q2=r T2, with the unit-period convention and tensor norms
of the construction note. Set

    I1=(pi^2/8)(a1^2-3b1^2-A1^2-B1^2),
    I2=(pi^2/8)(A1^2-3B1^2-a1^2-b1^2),
    E1=A0 a1, E2=a0 A1.                                  (2.1)

For the decaying correction K, its individual receiver fluxes were
`-Ii/2 +/-pi Ei/4`. Adding H[zeta] changes the Q1 projection by

    integral_R <H[zeta],Q1>cosh(t)dt=pi(c0+c1 J(u)).        (2.2)

Since `cosh(u)J'(u)=1`, the added outward Green fluxes are `-pi c1/2`
on the positive u face and `+pi c1/2` on the negative face. Thus the
complete formula for the bounded repair Z is

    F_(1,+)=-I1/2+pi E1/4-Delta c/2,
    F_(1,-)=-I1/2-pi E1/4+Delta c/2,
    F_(2,+)=-I2/2+pi E2/4-Delta C/2,
    F_(2,-)=-I2/2-pi E2/4+Delta C/2.                       (2.3)

Equivalently, each pair has an even part `-(Ii/2)(1,1)` and an odd part
`(pi Ei/4-Delta c_i/2)(1,-1)`. In particular

    F_(i,+)+F_(i,-)=-Ii.                                  (2.4)

No second-order background-parameter shift changes this sum. The full
bounded homogeneous freedom has already been included in (2.3).

The physical meaning of the endpoint parameters is explicit. If the
background y period is P_y, the limiting base-cylinder waist lengths are

    ell_(B,+/-)(s)=P_y exp[-s a_+/-/2-s^2 c_+/-/2],
    log[ell_(B,+)/ell_(B,-)]
        =-s pi a1/2-s^2 Delta c/2.                        (2.5)

This is exact for the parameter curve `s z+s^2 zeta`. The analogous
formula for fibre waist lengths uses A1 and Delta C. Thus imposing a
condition on physical boundary lengths can constrain the odd part of
(2.3), but cannot erase its even part. Equality of the actual thick-mouth
lengths does **not**, by itself, imply equality of the normalized complete-
model face data: the intervening collapsing region can carry a response,
as the explicit cutoff counterexample in round two shows.

## 3. Conditional gluing lemma and its finite-dimensional consequence

Use the outward normal of the exterior to define its limiting fluxes
`r_(i,+),r_(i,-)`. For a finite collar the exterior and interior normals
are opposite. Assume that a proposed second-order gluing has all of the
following properties:

- its rescaled invariant interior coefficient converges to a bounded
  Bianchi-gauge Z satisfying (1.1);
- the boundary metric, correction, and detector jets match so that the
  Green pairings cancel across each interface;
- after division by the physical angular-period product and the squared
  amplitude, the four interface pairings converge to those in (2.3) and
  to the displayed exterior fluxes; discarded corner, noninvariant, and
  gauge terms are o(1) in this same normalization.

These are precise interface hypotheses, not conclusions of local smooth
convergence. Under them, `r_(i,+)+F_(i,+)=0` and
`r_(i,-)+F_(i,-)=0`. Therefore

    r_(1,+)+r_(1,-)=I1,
    r_(2,+)+r_(2,-)=I2,
    Delta c=r_(1,+)-r_(1,-)+pi A0 a1/2,
    Delta C=r_(2,+)-r_(2,-)+pi a0 A1/2.                     (3.1)

Conversely, for prescribed four exterior numbers, the scalar Q1,Q2
interface equations admit second-order end differences exactly when
their two sums equal I1,I2; the last two equations then give the required
differences. The means c0,C0 remain free. This is sufficient only for
these four projected equations, not for full tensor gluing.

**Finite-dimensional consequence.** If the two net exterior receiver
responses vanish, then I1=I2=0, which is equivalent to

    b1=B1=0, a1^2=A1^2.                                  (3.2)

Indeed their sum is `-pi^2(b1^2+B1^2)/2`. With both twists zero, either
equation reduces to `a1^2=A1^2`. First-order length transfers can cancel
one detector, but never both when a first-order twist transfer remains.
Second-order endpoint shifts cannot change this conclusion. If all four
exterior face responses vanish separately, the additional requirements
are `Delta c=pi A0 a1/2` and `Delta C=pi a0 A1/2`.

The operative conditional assumption is **zero net exterior response**.
It has not been proved for E_D. There is no global contradiction merely
because the interior source has nonzero total flux.

## 4. Where an exterior response enters the actual equation

Let Omega_ext be an exterior reference region, J_ext its self-adjoint
Bianchi linearization, and U its second-order coefficient in that gauge.
Suppose `J_ext U=-D_ext`. Let Q_ext extend the relevant detector with
the matching boundary jets. Green's identity gives

    r_i=-integral_(Omega_ext) <D_ext,Q_ext>
          -integral_(Omega_ext) <U,J_ext Q_ext>,             (4.1)

with additional external boundary terms included if the region has more
boundary components. Combining this with (3.1) yields the projected
solvability equation

    Ii+integral <D_ext,Q_ext>
         +integral <U,J_ext Q_ext>=0.                      (4.2)

Thus a nonzero source or an adjoint defect can receive the interior flux.
Calling Q_ext an approximate kernel does not permit the last integral to
be dropped without an estimate at the physical flux scale. If the Bianchi
condition on U is not imposed, one must additionally retain the gauge
boundary term `integral_boundary Q(nu,beta U)` and the interior pairing
with the detector's divergence. The present lemma states the gauge in
which (4.1) has the displayed form.

For E_D the horizontal global TT detector is already constructed in the
manuscript. A vertical global detector with the same useful properties
is not supplied by the complete-model calculation. An arbitrary smooth
extension can be made, but its adjoint and gauge defects then belong in
(4.1). This is a second independent reason why the local two-detector sum
cannot be declared a closed obstruction.

## 5. Physical periods and a fixed Dehn-twist marking

If the unfolded angular periods are P_y=beta and P_x=epsilon, all
quadratic fluxes in (2.3) acquire the factor `s^2 epsilon beta`. Changing
periods does not change the reduced operator, but it does change the
integrated source and flux. All matching limits must use this factor.

The two t-face cylinder models have an end-to-end marked x-shear
`(pi/2) B_+` and `(pi/2) B_-`. Their difference along the parameter curve
is therefore

    (pi^2/2)(s B1+s^2 zeta_B1).                            (5.1)

If the entire marked m-fold Dehn twist is assigned to these two model
faces in the retained trivializations, this equals `m P_x(s)`. More
generally an exterior marked shear tau_ext must be retained:

    (pi^2/2)(s B1+s^2 zeta_B1)+tau_ext(s)=m P_x(s).         (5.2a)

In the original balanced assignment, `tau_ext=0`, `s=epsilon`, and
`P_x(s)=s`, so the relation forces

    B1=2m/pi^2, zeta_B1=0.                                (5.2)

If the coordinate period itself has a second-order change, or the
exterior carries marked shear, (5.2a) fixes the corresponding relation.
Topology alone does not prove tau_ext=0 in a new proposed construction.
When the marked twist remains assigned to the model as in (5.2), the
total exterior response required by both detectors, for nonzero m, is

    r_(1,+)+r_(1,-)+r_(2,+)+r_(2,-)
      =-pi^2(b1^2+B1^2)/2 <=-2m^2/pi^2.                   (5.3)

This is conditional on the compatible two-detector interface assumptions
in Section 3; it is not a newly established global topological identity.
For the original single-twist profile, `b1=a1=A1=0`, `B1=2/pi^2`, and
`B0=1/pi`. Then `I1=-1/(2pi^2)`, `I2=-3/(2pi^2)`. Restoring s=epsilon
gives physical receiver totals `-epsilon^3 beta/(2pi^2)` and
`-3epsilon^3 beta/(2pi^2)`.

## 6. A concrete missing quadratic functional at the allowed larger scale

There is an unconditional necessary equation for any small exact closed
repair of the particular original balanced metric G_epsilon on E_D. Use
the genuine global horizontal TT tensor Q_epsilon from the manuscript.
Its verified estimates, with the original rather than corrected background,
are

    integral <E(G_epsilon),Q_epsilon>
      =-epsilon^3 beta/(2pi^2)(1+o(1)),
    ||J_(G_epsilon) Q_epsilon||_1<=C epsilon^2 beta,
    ||Q_epsilon||_1<=C beta.                              (6.1)

For an exact metric `G_epsilon+h_epsilon`, the actual Ricci Taylor formula
and global TT integration by parts give

    0=integral <E(G_epsilon),Q_epsilon>
       +integral <h_epsilon,J_(G_epsilon)Q_epsilon>
       +integral <N_(G_epsilon)(h_epsilon),Q_epsilon>.      (6.2)

Consequently a global correction with C2 size O(epsilon^2), including
global parameter shifts at that size, cannot suffice: the last two terms
are O(epsilon^4 beta). This is consistent with the known lower bound.
The leading potentially admissible size is epsilon^(3/2).

More precisely, suppose

    h_epsilon=epsilon^(3/2) U_epsilon,
    ||U_epsilon||_(C2(G_epsilon))<=C,
    E(G_epsilon+h_epsilon)=0.                              (6.3)

The linear adjoint term in (6.2), divided by epsilon^3 beta, is
O(epsilon^(1/2)). Uniform bounded geometry on the local covers of the
original balanced construction gives the quasilinear Taylor estimate

    N_G(h)=(1/2)D^2E_G[h,h]+O_(C0)(||h||_(C2)^3).

Therefore the **explicit necessary receiver equation** is

    Qcal_epsilon(U_epsilon)
      :=(1/(2beta)) integral_E_D
           <D^2E_(G_epsilon)[U_epsilon,U_epsilon],Q_epsilon>
       ->1/(2pi^2).                                      (6.4)

This limit follows directly from (6.1)--(6.3); no inferred model boundary
condition is used. It is not enough to know that U_epsilon has a bounded
Jacobi limit on the thin core: the integral is over the entire closed
manifold with the genuine global TT test. A deformation can disappear
in the core normalization while contributing on a thick region.

Equation (6.4) identifies a concrete next calculation. One needs the
quadratic form of the actual Ricci operator on globally admissible leading
responses U_epsilon, with their marking, gauge and projected linearized
equation retained. Neither its vanishing nor its sign follows from the
complete-model classification. The first-order exterior receiver problem,
its adjoint defect, and this quadratic functional are computable objects;
they have not been replaced here by an unsupported global no-go statement.

## 7. Verification and scope

`round3_matching_check.py` checks the endpoint-shift Green pairings,
matching equations, source sums, marked-twist scaling, and the coefficient
of (6.4). The classification (1.2) uses the proved round-two bounded kernel;
the exact realization uses the round-three exact family. The closed
identity uses the live manuscript's `ED-global-pairings` and
`ED-nonlinear-obstruction` derivations, read with their original-background
and TT qualifications. No live asset is changed.
