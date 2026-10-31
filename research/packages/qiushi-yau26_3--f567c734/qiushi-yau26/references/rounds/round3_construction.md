# Exact Einstein completion of the invariant double-cylinder family

Date: 2026-09-19. Scope: the complete model `(R x S1) x (R x S1)` with
fixed positive angular periods. No live Skill or running Session is changed.
The qiushi-yau26 Skill was read in full, followed by its relevant construction
manuscript and the round-two proof and independent review.

The second-order repair extends to an actual small family of complete
Einstein metrics. The missing analytic ingredient is that the **entire
nonlinear defect**, not merely its quadratic coefficient, belongs to the
space where the model inverse acts. A moving reference metric in the Bianchi
gauge avoids a nonintegrable boundary gauge error.

## 1. Precise theorem

Use unit angular periods in integral formulas. Put

    g0=dt^2+cosh(t)^2 dy^2+du^2+cosh(u)^2 dx^2,
    J(v)=arctan(sinh(v)), f(t)=sech(t)^2, r(u)=sech(u)^2,
    W(t,u)=cosh(t)cosh(u).

For constants alpha,gamma define

    h_(alpha,gamma)(v,theta)
      = cosh(v)^2/[sinh(v)^2+exp(-alpha)] dv^2
        +[sinh(v)^2+exp(-alpha)]
             (dtheta+gamma sech(v)^3 dv)^2.                  (1.1)

It is complete, has curvature -1, and has area form `cosh(v)dv dtheta`.
Let

    z=(a0,a1,b0,b1,A0,A1,B0,B1),
    a(u)=a0+a1 J(u), b(u)=b0+b1 J(u),
    A(t)=A0+A1 J(t), B(t)=B0+B1 J(t),
    g[z]=h_(a(u),b(u))(t,y)+h_(A(t),B(t))(u,x).               (1.2)

Define H^m_delta for invariant tensors by the norm

    sum_(|I|<=m) integral_R2 W^(1+2delta)|partial^I h|^2 dtdu, (1.3)

where partial derivatives are radial derivatives of the background
orthonormal-frame coefficients. Covariant-derivative norms are equivalent:
the frame connection matrices and all their derivatives are bounded.
Fix `delta=1/4`, and for example `m=4`.

**Theorem.** In a neighborhood U of zero in R8 there is a real-analytic map
`k:U -> H^(m+2)_delta`, with `k(0)=dk(0)=0`, such that

    G[z]=g[z]+k[z],   Ric(G[z])=-G[z],
    beta_(g[z]) k[z]=0,
    ||k[z]||_(H^(m+2)_delta)<=C|z|^2.                       (1.4)

The metrics are smooth, complete, invariant under both angular rotations,
and uniformly equivalent to g0. Their first derivatives at zero are the
eight bounded invariant Jacobi fields of round two. The correction is
unique in a sufficiently small H^(m+2)_delta ball among solutions of the
specified gauged equation. This is uniqueness in this gauge and correction
space, not a classification modulo arbitrary diffeomorphisms.

For every fixed derivative order j, elliptic regularity gives

    |nabla_0^j k[z]|<=C_j |z|^2 W^(-3/4).                   (1.5)

U may be shrunk for any finite list of estimates. These are asymptotic
estimates for the **exact** metrics. No assertion that the eight parameters
remain distinct modulo unrestricted diffeomorphisms is needed.

## 2. The exact nonlinear source lies in the required space

Compactify the radial variables by

    xi=J(t), eta=J(u), p=cos(xi)=sech(t), q=cos(eta)=sech(u),
    partial_t=p partial_xi, partial_u=q partial_eta.

The closed parameter square is `[-pi/2,pi/2]^2`. In the background
orthonormal frame, a cylinder block is

    d=1+(exp(-alpha)-1)p^2,
    H(alpha,gamma;p)
      = [[d^(-1)+gamma^2 d p^4, gamma d p^2],
         [gamma d p^2,                 d]].                 (2.1)

Its determinant is exactly 1. The blocks, their inverses, and their
parameter derivatives extend smoothly to the closed square, uniformly
for small z. Their positive definiteness is uniform there. The only
nonzero background frame brackets are

    [e0,e1]=-sin(xi)e1, [e2,e3]=-sin(eta)e3.

Thus every component of `E[z]=Ric(g[z])+g[z]` is smooth on that square:
the curvature formula only involves these smooth coefficients, their
`p partial_xi,q partial_eta` derivatives, the smooth brackets, and the
uniformly invertible matrix (2.1).

On `eta=+/-pi/2`, the second block is the identity and its derivatives
vanish. Every transverse derivative of a,b vanishes there as well, because
of the factor q. The face curvature is precisely that of the product of
`h_(a_+,b_+)` or `h_(a_-,b_-)` with a hyperbolic radial-end model; hence
its Ricci tensor is minus its metric. The same holds on both xi faces.
This is an identity for the exact defect, including every mixed component
and every corner, at each small z.

Hadamard division by the simple endpoint zeros of cos(xi), then cos(eta),
therefore gives

    E[z](xi,eta)=p q R[z](xi,eta),                           (2.2)

with R smooth on the closed square. The eight first variations of g[z]
are actual TT Jacobi fields, so `E[0]=0` and `dE[0]=0`. Division commutes
with parameter differentiation, giving `R[z]=O(|z|^2)` with every fixed
derivative. Radial derivatives preserve the factor pq; angular covariant
derivatives are bounded frame-matrix operations. Consequently

    |nabla_0^j E[z]|<=C_j |z|^2 W^(-1),
    ||E[z]||_(H^m_delta)<=C_(m,delta)|z|^2  (delta<1/2).      (2.3)

The squared integral is bounded by
`C|z|^4 integral W^(-1+2delta)dtdu`, which is finite. All parameter
derivatives satisfy the same domination. The formulas are analytic in z
with denominators uniformly bounded away from zero, so E is analytic as a
map into H^m_delta. This checks the whole nonlinear source; a cubic or
higher term cannot silently leave the target space.

## 3. Weighted invertibility, including an explicit weight

Let `L=(nabla* nabla-2 R-circle)/2`, and
`P_t=partial_t^2+tanh(t)partial_t`, similarly P_u. Round two proved that
`2L=-P_t-P_u+V` on ten constant frame components, with potentials

    2; 2-4f; 2-4r; 2-f-r

for the trace, first TT, second TT, and mixed blocks. It proved the full
invariant Friedrichs estimate

    <Lv,v>_(L2(W)) >= (1/8)||v||_(L2(W))^2.                 (3.1)

All components may depend jointly on t,u. Set `rho=log W`. Conjugation gives

    L_delta=W^delta L W^(-delta)
      =L+delta grad(rho).grad+(delta/2)(P_t+P_u)rho
             -(delta^2/2)|grad rho|^2.                     (3.2)

The first-order term and the linear zeroth-order term are skew-adjoint
together in L2(Wdtdu). Hence

    Re <L_delta v,v>
      =<Lv,v>-(delta^2/2) integral |grad rho|^2 |v|^2 W
      >=(1/8-delta^2)||v||_2^2,                            (3.3)

since `|grad rho|^2=tanh(t)^2+tanh(u)^2<=2`. For delta=1/4 this bound is
1/16. At that weight the first line is at least half of `<Lv,v>`.
Moreover `V>=-2` gives
`<Lv,v> >= ||grad v||_2^2/2-||v||_2^2`.
A fixed positive convex combination with (3.1) controls the full H1 norm.
The continuous form of L_delta is therefore coercive on H1.

Lax--Milgram supplies a weak inverse. Uniform interior elliptic estimates,
summed over unit radial boxes where W has uniformly bounded ratios, give

    ||v||_(H^(m+2))<=C_m(||L_delta v||_(H^m)+||v||_2).

Regularity of the weak inverse yields an isomorphism

    L:H^(m+2)_(1/4) -> H^m_(1/4)                          (3.4)

for every nonnegative integer m. Multiplication by W^delta identifies the
weighted and unweighted versions with equivalent Sobolev norms, since all
positive derivatives of rho are bounded. This proves the weighted inverse
directly; it does not assume a weighted Fredholm theorem or a closed-model
maximum-norm inverse bound.

## 4. Nonlinear contraction and removal of gauge

Use `beta_g h=-div_g h+(1/2)d tr_g h` and
`delta_g^* omega=(nabla_i omega_j+nabla_j omega_i)/2`. Set

    F(z,k)=Ric(g[z]+k)+(g[z]+k)
             +delta^*_(g[z]+k) beta_(g[z]) k.               (4.1)

Then `F(z,0)=E[z]` and `D_k F(0,0)=L`. The moving reference is useful:
for a constant length deformation with gamma=0 one computes exactly

    beta_g0(h_(alpha,0))
      =tanh(t)((d-1)/d)^2 dt,
    d=1+(exp(-alpha)-1)sech(t)^2.                           (4.2)

This is generally nonzero and independent of u, so it is not L2 on the
product. Being of order alpha^2 does not cure its nonintegrability. In
(4.1) the inverse instead receives the integrable exact source (2.2).

For m=4, weighted radial Sobolev multiplication and embedding make H^m_delta
an algebra. To verify this, cover R2 by unit boxes; their weights have
uniformly bounded ratios, and W>=1 makes the global weighted norm control
all local unweighted norms. Apply two-dimensional Sobolev multiplication
in each box and sum. Smooth coefficients with bounded derivatives act as
bounded multipliers. The coefficients of g[z]-g0 and all fixed derivatives
have uniform maximum norm O(|z|).

The quasilinear Ricci and gauge expressions contain inverse metrics,
second derivatives, and products of first derivatives. Thus F is analytic
near `(0,0)` from `R8 x X` into Y, with
`X=H^(m+2)_delta`, `Y=H^m_delta`. Use
`F(z,k)=E[z]+F(z,k)-F(z,0)` in checking this statement; it does not require
g[z]-g0 itself to be L2. Put `A_z=D_kF(z,0)` and
`N_z(k)=F(z,k)-E[z]-A_z k`. The product estimates give

    ||(A_z-L)h||_Y<=C|z| ||h||_X,
    ||N_z(k)-N_z(l)||_Y
      <=C(||k||_X+||l||_X)||k-l||_X.                        (4.3)

The map `k -> -L^(-1)[E[z]+(A_z-L)k+N_z(k)]` preserves a ball of radius
`C0|z|^2` and is a contraction for small z. The analytic implicit function
theorem also gives analytic parameter dependence. Smallness preserves
positive definiteness and uniform equivalence to the complete g0, hence
completeness. Elliptic bootstrapping supplies smoothness and the higher
weighted derivative estimates.

For the actual Einstein assertion put `omega=beta_(g[z]) k[z]`. This is
H1 and L2 with respect to G. Applying beta_G to F=0 and using contracted
Bianchi gives

    (nabla_G* nabla_G-Ric_G)omega=0.                        (4.4)

The factor 1/2 in beta_G delta_G^* has been canceled. Before appealing to
Einstein, C2 closeness already gives `Ric_G<=-cG` for some c>0. Test (4.4)
against chi_R^2 omega on this complete metric, with `|d chi_R|<=C/R`.
Integration by parts and absorption yield

    integral chi_R^2(|nabla omega|^2+c|omega|^2)
      <=C integral |d chi_R|^2 |omega|^2 ->0.

Thus omega=0 and (4.1) is the actual Einstein equation. This completes the
theorem, including the gauge-removal step.

## 5. Genuine end models of the exact metrics

Put `a_+/-=a0+/-pi a1/2`, `b_+/-=b0+/-pi b1/2`, and define A_+/-,B_+/-
likewise. On the positive and negative u radial faces G[z] approaches

    g_(u,+/-)=h_(a_+/-,b_+/-)(t,y)+du^2+cosh(u)^2 dx^2.     (5.1)

On the t faces it approaches

    g_(t,+/-)=dt^2+cosh(t)^2 dy^2+h_(A_+/-,B_+/-)(u,x).     (5.2)

For example, uniformly in t and with every fixed number of background
covariant derivatives,

    |G[z]-g_(u,+/-)|
      <=C|z|[f(t)e^(-|u|)+e^(-2|u|)]+C|z|^2 W^(-3/4).     (5.3)

For (1.5), restrict the weighted Sobolev estimate to a unit radial box,
divide its local norm by W^(1/2+delta), and apply the two-dimensional local
embedding. Formula (5.3) then follows from
`J(u)=+/-pi/2+O(e^(-|u|))` and from the f,r factors in the metric blocks.
The analogous bound holds for the t faces. At a corner where both radial
variables escape, G[z] approaches g0 in relative norm. The four faces are
asymptotic regions, not four different topological ends of R2 x T2. These
metrics need not be exact products outside a compact set.

For angular period 1, the waist geodesic of h_(alpha,gamma) has length
`exp(-alpha/2)`, and its marked angular shear between radial ends is

    gamma integral_R sech(v)^3 dv=(pi/2)gamma.              (5.4)

The latter depends on retained end coordinates. Accordingly the two u
faces have different waist lengths when a1 is nonzero, and different
marked shears when b1 is nonzero. The same statement applies to t faces.

## 6. Individual receiver fluxes of the actual second variation

Fix z and take the ray G[s z]. The analytic family satisfies

    k[s z]=s^2 K[z]+O_(H^(m+2)_delta)(s^3),
    K[z]=-L^(-1)D[z], beta_g0 K[z]=0,                       (6.1)

where D is the complete quadratic source in round two. K is now the
second Taylor coefficient of an **existing exact Einstein family**.
Let `Q1=f T1`, `Q2=r T2`, with `|T1|^2=|T2|^2=2`. Recall

    I1=integral <D,Q1>=(pi^2/8)(a1^2-3b1^2-A1^2-B1^2),
    I2=integral <D,Q2>=(pi^2/8)(A1^2-3B1^2-a1^2-b1^2).     (6.2)

Define `M1(u)=integral_R <K(t,u),Q1(t)>cosh(t)dt`. The weighted estimates
justify this integral and the transverse integration by parts. Projection
of LK=-D onto the first cylinder's ground state yields

    P_u M1=2d1(u),
    d1(u)=integral_R <D(t,u),Q1(t)>cosh(t)dt
      =(pi/8)(a1^2-3b1^2)r-(pi/4)(A1^2+B1^2)r^2
         -pi A0 a1 tanh(u)sech(u)^3.                       (6.3)

M1 is in L2(cosh(u)du). In eta=J(u), `P_u=r partial_eta^2`. Write
`C1=a1^2-3b1^2`, `F1=A1^2+B1^2`, `E1=A0 a1`. The unique L2 solution is

    M1(eta)=(pi/8)(C1-F1)(eta^2-pi^2/4)
              +(pi/16)F1[cos(2eta)+1]+(pi/4)E1 sin(2eta).   (6.4)

It tends to zero at both endpoints; uniqueness also follows from the
positive scalar L2 gap. Its true tails and derivative fluxes are

    M1(u)=(-2I1+pi E1)e^(-u)+O(e^(-2u))       (u ->+infinity),
    M1(u)=(-2I1-pi E1)e^( u)+O(e^( 2u))       (u ->-infinity),
    lim_(u->+infinity)cosh(u)M1'(u)= I1-pi E1/2,
    lim_(u->-infinity)cosh(u)M1'(u)=-I1-pi E1/2.             (6.5)

For the background Green pairing

    Flux(K,Q;Omega)=(1/2) integral_boundary(Omega)
                [<K,nabla_nu Q>-<nabla_nu K,Q>],            (6.6)

the positive and negative u-face contributions for Q1 are respectively

    F_(1,+)=-I1/2+pi A0 a1/4,
    F_(1,-)=-I1/2-pi A0 a1/4.                              (6.7)

Here the full transverse t line is integrated first; the same values arise
on expanding squares. The other face terms vanish there using the
W^(-3/4) bound on K and its derivatives and the e^(-2|t|) decay of Q1.
Interchanging the factors gives the t-face receiver coefficients for Q2:

    F_(2,+)=-I2/2+pi a0 A1/4,
    F_(2,-)=-I2/2-pi a0 A1/4.                              (6.8)

In particular their sum is

    -(I1+I2)=(pi^2/2)(b1^2+B1^2).                          (6.9)

Constant length offsets redistribute the paired face fluxes without
changing their total. Nonzero twist transfer has compulsory nonzero
quadratic end flux even in an actual complete Einstein family.

The order of limits matters. Equation (6.9) concerns the flux of
`(1/2)d^2 k[s z]/ds^2 at s=0`. We have **not** proved that the unrenormalized
g0 Green pairing of k[s z] has a finite limit at every nonzero s, or that
its limit can be interchanged with parameter differentiation. The
W^(-3/4) remainder estimate alone permits neither inference against
non-L2 test tensors. A fixed-s nonlinear charge or full polyhomogeneous
expansion requires further end-operator analysis. The exact existence
theorem, its genuine end limits (5.1)--(5.3), and the explicit second-
variation flux above do not require that stronger assertion.

## 7. Closed E_D and the relation to prior work

This proves that all eight invariant bounded model directions integrate
on R2 x T2: there is no nonlinear local obstruction to these transfers
in this particular complete problem. The correction can change all ten
tensor components. It need not preserve block diagonality, exact product
volume, or the original Riemannian-submersion structure.

It does not construct a metric on the closed marked surface bundle E_D.
The asymptotic cylinder data and nonzero receiver coefficients must be
matched to that manifold's exterior, with physical angular periods,
topology, global gauge, and the actual closed kernel retained. Cutting off
an exact noncompact solution introduces error; this inverse remains an
invariant complete-model inverse, not a uniform closed-manifold inverse.

Biquard and Mazzeo develop Einstein deformations near products using an
asymptotic approximate metric, a moving Bianchi gauge, an inverse, and
nonlinear contraction. Their main theorem requires nondegeneracy of both
factors and their product. Here each individual hyperbolic cylinder has
invariant L2 TT zero modes, although the invariant product has the positive
gap (3.1), so that theorem is not directly applicable to the specified end
data. The present argument checks this smaller model directly; the general
method is established prior work. See their main theorem, Proposition 19,
and proof of Proposition 22 in
[A nonlinear Poisson transform for Einstein metrics on product spaces,
JEMS 13 (2011), 1423--1475](https://ems.press/content/serial-article-files/31796).
No publication-priority claim is made here.

## 8. Checks and proof boundary

`round3_construction_check.py` checks the exact block determinant, cylinder
curvature, exact formal face Ricci tensor in the noncoordinate frame,
fixed-reference gauge defect (4.2), weight conjugation (3.2), projected
ODE, end derivatives, and summed flux formulas. These are algebraic
checks, not a computer proof of elliptic regularity or contraction.
The analytic proof, spaces, and hypotheses are in sections 2--4.
