# E_D: the first admissible correction scale and the base Teichmuller modes

Date: 2026-09-19. Local research calculation; no live Skill or Session changes.

This note derives a restricted obstruction beyond the generic
`a >= c epsilon^(3/2)` lower bound. It does not prove that E_D has no Einstein
metric, and it does not identify the full small spectrum of its Jacobian.
The geometric input estimates listed below are taken from the manuscripts;
the new projection calculation is proved here and checked independently in
`construction_checks.py`.

## 1. Inputs and notation

Write `eps` for epsilon, `beta=eps^2`, `G=G_eps` for the original balanced
double-collar metric, and `Phi(g)=Ric(g)+g`. The background has block form

    G = b + h_x,       b hyperbolic on B,

where the fibre metrics have a common pointwise area form. The fibre genus is
`p>=2`. Let `Q=pi^*q_beta` be the globally defined concentrated base TT tensor.
The following input estimates are in the long manuscript `20260912.tex`,
lines 3666-3737, and in `20260916_construction.tex`, lines 873-943:

    I_eps := integral <Phi(G),Q>_G dV_G
           = -eps^3 beta/(2 pi^2) (1+o(1)),

    integral |Q|_* dV_G = 8 pi^2 (p-1) beta + O(beta^2),
    ||J_G Q||_L1 <= C eps^2 beta.

Here `J_G` is the actual self-adjoint Jacobian part on this non-Einstein
background; the Ricci-error zeroth-order term is retained. Q is TT for G,
so for every global symmetric tensor r,

    integral <D Phi_G(r),Q>_G dV_G = integral <r,J_G Q>_G dV_G.

Every norm on a metric perturbation below is the original G-relative C^2
norm, including derivatives of orders zero through two. Constants are uniform
for the stated family. The Ricci Taylor estimates are pointwise tensor
estimates in this geometric norm: use the connection difference
`C=(1/2)(G+h)^(-1)*(nabla^G h)` and the exact curvature difference
`nabla^G C+C*C`. Uniform positive definiteness controls the inverse metric.
These estimates require no positive injectivity-radius bound or choice of
uniform coordinate charts.

## 2. Exact cancellation of every base-TT quadratic projection

Let k be ANY global TT symmetric 2-tensor for the hyperbolic base b, and
let B=pi^*k. It need not be proportional to the concentrated q_beta. Thus
the calculation includes the entire real `(6q-6)`-dimensional base
Teichmuller tangent space, with bounds imposed on the actual tensor B.

For any nearby base metric b', hold the fibre path h_x fixed and set
`G'=b'+h_x`. The horizontal Ricci block is exactly

    Ric(G')_ij = Ric(b')_ij - T_ij,
    T_ij = tr(S_i S_j),    S_i=(1/2) h_x^(-1) partial_i h_x.

Indeed, in the usual block-metric Ricci formula the terms involving the
base covariant derivative of `tr(S)` vanish because the common fibre area
form gives `tr(S_i)=0`. T is a covariant base tensor determined by h_x,
independent of b'. Therefore, in dimension two,

    Phi(G')_HH = (K(b')+1)b' - T.                         (2.1)

All pairings in this section use the FIXED metric G and fixed test Q.
In particular, the measure and tensor contractions do not move with b'.
Since `K(b)=-1` and k is TT, the scalar-curvature variation formula gives
`DK_b(k)=0`. For the straight path `b_s=b+s k`,

    K(b_s)+1 = O(s^2),
    <b_s,q_beta>_b = s <k,q_beta>_b.

Consequently the change of the Q projection is cubic:

    integral <Phi(G+sB)-Phi(G),Q>_G dV_G = O(s^3 beta).

More invariantly, for any two base TT tensors B_1,B_2,

    <D^2 Phi_G(B_1,B_2),Q>_G = 0                       (2.2)

pointwise. Its horizontal block is `D^2 K_b(k_1,k_2) b`, hence pure trace;
the other blocks do not pair with Q. The first projected variation is
also exactly zero. This is a trace identity, NOT a parity argument.

In fact, for an arbitrary hyperbolic path b(s) while h_x is held fixed,
equation (2.1) makes the entire fixed-Q projection equal to I_eps for all s.
The nonlinear acceleration of the hyperbolic moduli path matters: the
cubic coefficient of a straight tensor path is not a moduli obstruction.

## 3. A stronger necessary estimate and its consequence at eps^(3/2)

Decompose a perturbation as

    h = B+r,     B=pi^*k with k TT on b,
    a=||B||_C2,  z=||r||_C2,

with a+z in a fixed sufficiently small positive-definite neighbourhood.
The preceding exact cancellation and the ordinary Ricci Taylor formula give

    | integral <Phi(G+h),Q> dV_G - I_eps |
       <= C beta [eps^2 z + a^3 + a z + z^2].            (3.1)

Proof: the linear r term is bounded using `||J_GQ||_1`; the pure B term
starts at cubic order by (2.2); the mixed Taylor remainder is bounded by
`C(a z+z^2)` pointwise and then integrated against `|Q|_*`. These estimates
allow arbitrary tensor components, support, and angular dependence in r.
No full inverse or hypothetical exact solution is used.

This proves the following restricted extension of the manuscript's
third-order lower bound. Its coefficient is explicit; optimal attainable
equality in that coefficient is not established here.

**Proposition, conditional only on the stated E_D input estimates.**
If

    a=O(eps^(3/2)),     z=o(eps^(3/2)),

then

    liminf delta_-(G+B+r)/eps^3 >= 1/[16 pi^4(p-1)].     (3.2)

To see this, every term in brackets in (3.1) is o(eps^3). Thus the projected
residual retains `-eps^3 beta/(2 pi^2)(1+o(1))`. Metric comparison and
operator/nuclear-norm duality bound its absolute value by
`(1+o(1)) delta_-(G+h) integral |Q|_* dV_G`, giving (3.2).

The same conclusion follows under the alternative, larger-range bounds

    a=o(eps),          z=O(eps^2).                     (3.3)

In particular the known tensor correction `eps^2 Psi K` fits into r.
At the nominal first permissible eps^(3/2) scale, a correction led by any
combination of the global base TT modes still cannot cancel the source.
The generic `a^2` in the manuscript's unrestricted estimate is not the
actual leading nonlinearity in these directions.

This does NOT exhaust all leading tensor directions. If r is itself of
order eps^(3/2), the term a z+z^2 can contribute at order eps^3, and the
argument does not assign it a sign. The long manuscript, lines 3742-3759,
already gives an exact conformal example that cancels this one projection
while worsening the full Ricci residual to order eps^(3/2). Thus no
sign-definiteness statement for arbitrary perturbations is possible from
this projection alone.

## 4. Independent exact cylinder calculation

Use the infinite cylinder metric

    b_0 = dt^2 + cosh(t)^2 dy^2,
    f=sech(t)^2,
    Q_0=f dt^2-dy^2,
    b_s=b_0+s Q_0.

For `|s|<1`, direct evaluation of Gaussian curvature gives

    D=1-s^2 f^2,
    K(b_s)=[-1+s^2 f^2(1+2 tanh(t)^2)]/D^2,

    K(b_s)+1=s^2 f^2(1-2f)+O(s^4),
    <(K(b_s)+1)b_s,Q_0>_b0
        =2s^3 f^4(1-2f)+O(s^5).

The exact quadratic projected coefficient is zero. After integration
against `cosh(t)dt`, the cubic coefficient per unit angular length and
fibre area is

    2 integral [sech(t)^7-2 sech(t)^9] dt = -15 pi/32.

This sign does not determine the Einstein reduction: the straight path has
an order-s^2 curvature residual. A genuine hyperbolic path with the same
tangent is obtained by

    T_s(t)=t+(s/2)tanh(t),
    b_hyp(s)=(T_s')^2 dt^2+exp(-s)cosh(T_s)^2 dy^2.

It has curvature exactly -1, tangent Q_0, and acceleration

    b_hyp''(0)=(f^2/2)dt^2+((1+f)/2)dy^2.

Thus its second-order correction cancels the scalar residual responsible
for the apparent cubic term. The calculation also gives the polarized
quadratic cancellation without invoking an external moduli theorem.

The exact same trace argument applies globally, so no unsupported cutoff
of Q_0 is being used in Proposition (3.2). The cylinder calculation tests
the algebra; the proposition uses the existing GLOBAL base TT tensors and
the actual closed-manifold adjoint estimate.

## 5. Vertical response: a bounded check, not the complete complement

The long manuscript, lines 3930-3942, improves the two-vector Ritz
compression by allowing the angularly invariant vertical response

    W=-c0 r(u)tanh(t)sech(t)^3 M,
    Y=-(c0/2)r(u)tanh(t)sech(t) M,

where `c0=2/pi^2`, `r(u)=sech(u)^2`, and M is the symmetric off-diagonal
fibre tensor. The independent script checks exactly

    J_0Y=W,
    <W,Y>_L2=1/(4pi^2),
    3/(8pi^2)-<W,Y>=1/(8pi^2)>0.

The last number is the optimized coefficient in this specified response
class on the corrected background. It is not the full Schur complement.
W and Y are odd in t, so their mutual pairing is even and nonzero; parity
does not eliminate this coupling. The base TT quadratic cancellation in
Section 2 has a different, algebraic reason.

At base-mode amplitude s=eps^(3/2), the formal leading vertical response
has size `eps s=eps^(5/2)`, consistent with the remainder range in (3.2).
This observation does not assert that the complete global complement can
be solved with this bound.

## 6. The first correct full reduced equation

For a specified gauge-fixed map F on the corrected background, let P be a
bounded projection onto ALL low modes that must be retained, Qc=I-P,
and write `F(v)=r0+Lv+N(v)`. Define

    A=Qc L Qc,  Bop=P L Qc,  C=Qc L P,  D=P L P.

If, and only if, an inverse A^-1 and the complement equation are controlled,
write v=k+w with k=Pv, w=Qc v. Then the exact complement equation and
remaining finite-dimensional equation are

    w=-A^-1[Qc r0+Ck+Qc N(k+w)],

    O(k)=rho+S k+(P-Bop A^-1 Qc)N(k+w)=0,
    rho=P r0-Bop A^-1 Qc r0,
    S=D-Bop A^-1 C.                                   (6.1)

In a quadratic expansion the Hessian is evaluated on
`k-A^-1(Qc r0+Ck)` and projected by `P-Bop A^-1 Qc`;
using just `P D^2F(k,k)/2` can therefore omit contributions of the same order.
The norms of A^-1 and both projections, the full low-mode list, changes
with eps, gauge removal, and the nonlinear remainder remain necessary
inputs. An order-eps^3 eigenvalue of a trial compression does not establish
any of them.

On an exact closed product, the complete kernel consists of the two factors'
Teichmuller tensors. Its ordinary projected quadratic term vanishes:
same-factor variations have pure-trace second variation and mixed-factor
variations split. On degenerating E_D, fibre monodromy, neck modes, and
complement amplification prevent transferring this fact to all of (6.1)
without further analysis. Proposition (3.2) is the part that transfers
directly and rigorously through the actual global base TT subspace.

## 7. Verification and remaining target

Executed locally:

    qiushi-yau26 env numeric python construction_checks.py

Result: PASS, thirteen exact symbolic/integral checks. These verify the
cylinder curvature, vanishing quadratic projection, cubic coefficient,
exact hyperbolic tangent/acceleration, and stated restricted vertical
response. They are not a numerical PDE existence calculation.

The next mathematical target is now more specific: classify possible
leading eps^(3/2) corrections outside the base TT subspace after imposing
the FULL leading Einstein/gauge equations, and compute their coupled
projection through (6.1). Base Teichmuller drift alone cannot close the
third-order source. A proof that every admissible leading correction falls
in the integrable product directions would extend the exclusion, but that
statement is not established here and is precisely where collapse and end
conditions must be controlled.
