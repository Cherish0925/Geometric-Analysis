# A finite-parameter charge and scattering law for the exact model

20 September 2026. The qiushi-yau26 Skill was reread in full, together
with the round-three exact-family and matching proofs. All work is in
this isolated local worktree. No live asset is modified.

This note constructs an actual nonlinear boundary charge for the exact
eight-parameter complete Einstein family. The marked twist transfers
determine a nonzero conserved torus charge through a finite positive
matrix. The resulting boundary energy has the previously calculated
total length-flux coefficient at second order. Its boundary limit and
parameter derivatives do commute, with a proof using the existing decay
estimates. A full nonlinear length Dirichlet-to-Neumann map is not claimed.

## 1. The exact family and its torus reduction

Let `G[z]=g[z]+k[z]`, `Ric(G[z])=-G[z]`, be the exact complete family of
`round3_construction.md`. Its parameters are

    z=(a0,a1,b0,b1,A0,A1,B0,B1),
    a(u)=a0+a1 J(u), b(u)=b0+b1 J(u),
    A(t)=A0+A1 J(t), B(t)=B0+B1 J(t),
    J(v)=arctan(sinh(v)), W=cosh(t)cosh(u).

Use the base orientation `dt wedge du` and the angular order `(y,x)`.
The background is

    g0=dt^2+cosh(t)^2 dy^2+du^2+cosh(u)^2 dx^2.

The correction is analytic in a weighted Sobolev space and obeys, with
every fixed number of derivatives,

    |nabla_0^j k[z]| <= C_j |z|^2 W^(-3/4).                (1.1)

The corresponding estimates for each parameter derivative are uniform
on a smaller fixed parameter ball. Write the exact metric uniquely as

    G=h_ij dx^i dx^j
         +H_ab(dtheta^a+mathcal A^a)(dtheta^b+mathcal A^b),
    (x^1,x^2)=(t,u), (theta^1,theta^2)=(y,x),
    v=sqrt(det H), F^a=d mathcal A^a=f^a dA_h.             (1.2)

Here H is the Gram matrix of the specified Killing generators, h is the
quotient metric, and the connection is globally defined because the
bundle over R2 is trivial. Explicitly, H is the angular block, the
connection is obtained by multiplying the base-angular block by H^-1,
and h is the Schur complement. Neither H nor h is assumed diagonal in
the exact metric.

Define the coordinate charge covector

    q=v H f.                                             (1.3)

The exact mixed Ricci identity is

    Ric_G(X_i,K_a)=-(1/(2v))(*_h d q_a)_i,                 (1.4)

where `X_i=partial_i-mathcal A_i^a K_a` is the horizontal lift and
`K_a=partial_(theta^a)`. This follows from the horizontal/vertical Koszul
formula. Equivalently, varying the connection in the reduced Einstein
action gives `d(vH *_h F)=0`; its connection-dependent scalar-curvature
term is `-H_ab F^a_ij F^{b,ij}/4`. Formula (1.4) agrees with the charge
normalization in `round2_global.md` and is independent of the Einstein
constant. For this exact Einstein family it yields

    d q=0.                                               (1.5)

Thus q is a constant vector on the connected quotient, and is an analytic
function of z: evaluate (1.3) at the fixed point (t,u)=(0,0).

## 2. The nonlinear scattering theorem

Set `c=pi^2/2` and define

    S[z]=c(-b1,B1)^T,
    M[z]=integral_R2 v^(-1)H^(-1) dA_h.                   (2.1)

**Theorem.** For every sufficiently small parameter z, M[z] is a finite,
positive definite, real-analytic matrix, and

    integral_R2 F = S[z] = M[z] q[z],
    q[z]=M[z]^(-1)c(-b1,B1)^T.                            (2.2)

In particular

    q[z]=0  if and only if  b1=B1=0.                       (2.3)

With the other six parameters fixed sufficiently close to zero, the two
twist-transfer parameters can be replaced locally by the two components
of q as analytic coordinates. This is a two-channel finite-parameter
charge map, not the full metric boundary scattering operator.

### Integrability and positivity of M

Let `p=sech(t)`, `r=sech(u)` in this note. Uniform equivalence to g0 gives

    h comparable to I,
    H comparable to diag(p^(-2),r^(-2)), v comparable to W.

Consequently the positive matrix density in (2.1) is bounded above by
a constant times

    diag(p^3 r, p r^3) dtdu.                              (2.4)

Both entries are integrable. Positivity is strict because for every
nonzero vector w the integrand `v^-1 w^T H^-1 w` is positive everywhere.
At zero,

    M[0]=diag[(integral sech^3 t dt)(integral sech u du),
              (integral sech t dt)(integral sech^3 u du)]
         =c I.                                           (2.5)

The same integrable domination holds for all fixed parameter derivatives
of the normalized metric coefficients on a smaller parameter ball.
The analytic inverse-matrix formulas and a common small complex parameter
neighborhood give analytic dependence of the integral. This also follows
by differentiating the convergent Banach-valued local power series.

### Stokes at the actual ends

For the explicit approximate metric g[z], its connection is exactly

    mathcal A_0^y=b(u)p^3 dt,
    mathcal A_0^x=B(t)r^3 du.                             (2.6)

The length parameters cancel from this expression. Set
`alpha=mathcal A-mathcal A_0`. Taking the angular block inverse in (1.2)
and using (1.1) gives

    |partial^j alpha^y|<=C_j |z|^2 p W^(-3/4),
    |partial^j alpha^x|<=C_j |z|^2 r W^(-3/4).             (2.7)

These are bounds on coordinate coefficients for radial derivatives.
For example a base-angular correction has coordinate size
`cosh(t) k_on` in the y column, and multiplication by the angular inverse
contributes `cosh(t)^(-2)`, leaving the extra p factor. The inverse-block
variation times the old connection satisfies the same bound. Radial
differentiation preserves it because the scaling matrices have bounded
logarithmic derivatives. The same reasoning applies to parameter
derivatives, with constants uniform on a small parameter ball.

Both components of d alpha are absolutely integrable in dtdu, since
`p W^(-3/4)=p^(7/4)r^(3/4)` and its swapped counterpart are integrable.
For the positively oriented square boundary C_R, the two horizontal-edge
integrals of alpha^y are bounded by `C|z|^2 exp(-3R/4)`; its vertical-edge
integrals have the stronger `C|z|^2 exp(-7R/4)` bound. The x-component
has the interchanged bounds. Therefore

    lim_(R->infinity) integral_(C_R) alpha=0.              (2.8)

The same limits hold uniformly after any fixed number of parameter
derivatives. Applying ordinary Stokes on each square to (2.6) now gives

    integral F^y
      =-[b(+infinity)-b(-infinity)] integral p^3 dt
      =-pi^2 b1/2,
    integral F^x
      =[B(+infinity)-B(-infinity)] integral r^3 du
      = pi^2 B1/2.                                       (2.9)

Finally (1.3) and constancy of q give pointwise
`F=v^-1 H^-1 q dA_h`. Its integral is Mq, proving (2.2).
At zero the differential in `(b1,B1)` is diag(-1,1); continuity and the
finite-dimensional inverse theorem give the final coordinate assertion.

### Constant twists are exact angular gauge in this family

There is a useful all-order simplification. Set

    V(v)=integral_0^v sech(w)^3 dw
        =(sech(v)tanh(v)+J(v))/2,
    Phi(t,u,y,x)=(t,u,y+b0 V(t),x+B0 V(u)).

Let z_bar have the same parameters as z except `b0=B0=0`. Directly from
the reference formula, `g[z]=Phi^*g[z_bar]`. The moving-reference Bianchi
equation is natural under diffeomorphisms, and pullback by Phi preserves
the correction's weighted space with bounded operator norm for small
parameters. Local uniqueness of the exact solution therefore gives

    G[z]=Phi^*G[z_bar].                                   (2.10)

H and the quotient metric h are unchanged by this angular gauge, while
the connection changes by `(b0 dV(t),B0 dV(u))`. Consequently M and q
are **exactly independent of b0,B0**, not merely independent to the
orders computed below. These diffeomorphisms preserve each angular
period but change the retained end markings. This does not classify
all remaining parameters modulo unrestricted diffeomorphisms.

## 3. A genuine nonlinear boundary energy

Define

    mathcal E_tw[z]
      =integral_R2 v f^T H f dA_h
      =q^T M q=q dot S=S^T M^(-1)S.                      (3.1)

This is finite, analytic, and strictly positive exactly when at least one
twist-transfer parameter is nonzero. It also has the genuine boundary
formula

    mathcal E_tw[z]
      =lim_(R->infinity) integral_(C_R) q[z] dot mathcal A[z]. (3.2)

Constancy of q and (2.8) justify this formula. The boundary limit can be
interchanged with every fixed parameter derivative, by the uniform bounds
after (2.7). This establishes the operation that was unavailable for the
old non-L2 length detectors.

For comparison with the global notes, their physical twist energy density
is `Q=(1/2)f^T H f`. If the coordinate angular periods are P_y,P_x,
then the four-dimensional integral is

    integral_(R2 x T2) Q dV_G=(P_y P_x/2) mathcal E_tw.    (3.3)

The factor of two is explicit: mathcal E_tw is twice the reduced Q-energy.
It is this normalization whose quadratic coefficient equals the previous
sum of length-detector receiver fluxes.

Individual oriented edge contributions in the fixed trivialization are

    u+: -(pi/2)q_y b_+,   u-: +(pi/2)q_y b_-,
    t+: +(pi/2)q_x B_+,   t-: -(pi/2)q_x B_-,              (3.4)

where `b_+/-=b0+/-pi b1/2` and `B_+/-=B0+/-pi B1/2`.
Only their sum is invariant under a change of angular gauge. Gauge changes
add exact forms to the connection; they redistribute edge integrals by
corner values and leave (2.2), (3.1), and (3.2) unchanged.

There is also a quantitative bound requiring only relative metric
closeness. If `(1-eta)g0<=G<=(1+eta)g0`, with 0<eta<1, then restriction
to vertical vectors and minimization over vertical lifts give the same
bounds for H and h. Determinants and inverse matrices imply

    c(1-eta)/(1+eta)^2 I <= M
       <= c(1+eta)/(1-eta)^2 I.

Hence, writing `v_tw=(-b1,B1)`,

    c(1-eta)^2/(1+eta) |v_tw|^2
       <=mathcal E_tw
       <=c(1+eta)^2/(1-eta) |v_tw|^2.                    (3.5)

## 4. Explicit nonlinear coefficients through cubic energy order

The first derivative of M is computable without solving a new PDE because
`dk[0]=0`. For g[z], put

    d_t=1+(exp(-a(u))-1)p^2,
    d_u=1+(exp(-A(t))-1)r^2.

Its quotient and orbit matrices give the exact diagonal density

    v_0^(-1)H_0^(-1) dA_(h_0)
      =diag(p^3 r d_t^(-2)d_u^(-1),
             p r^3 d_t^(-1)d_u^(-2))dtdu.               (4.1)

The subscripts here mean the explicit reference g[z], not the undeformed
metric. Expanding to first order and using the oddness of J yields

    M[z]=c[I+(1/2)diag(3a0+A0,a0+3A0)+O(|z|^2)].         (4.2)

Neither length-transfer coefficient enters this derivative, and constant
twists have no effect at any order by (2.10). The integral facts are
`integral sech=pi`, `integral sech^3=pi/2`, and
`integral sech^5=3pi/8`; terms containing the odd J integrate to zero.
Inserting (4.2) into the exact scattering law gives

    q_y=-b1+(3a0+A0)b1/2+O(|z|^2 |v_tw|),
    q_x= B1-(a0+3A0)B1/2+O(|z|^2 |v_tw|),                (4.3)

and

    mathcal E_tw
      =c[b1^2+B1^2
          -(3a0+A0)b1^2/2-(a0+3A0)B1^2/2]
          +O(|z|^2 |v_tw|^2).                           (4.4)

For a fixed ray z=s z0, its quadratic coefficient is
`(pi^2/2)(b1^2+B1^2)`, exactly the sum `-(I1+I2)` from round three.
The next displayed term is the actual cubic coefficient of a finite-
parameter boundary quantity. Second-order parameter shifts can be inserted
directly in (4.4); they cannot make this energy zero while twist transfer
remains nonzero.

This is a nonlinear completion of the **total quadratic twist response**.
It does not identify (3.2) with the unrenormalized g0 Green pairing of the
finite-parameter correction k[z], nor identify individual edges in (3.4)
with the earlier length-detector faces. The latter depended on different
test tensors. A complete nonlinear length scattering map remains open.

## 5. Exact matching consequences and their scope

On every connected exact Einstein region carrying the same free torus
action, (1.5) requires one common charge q. Thus pieces that are to match
smoothly in an invariant exact Einstein gluing must match this charge,
as well as their metric and connection boundary data. In particular an
exact invariant continuation of a model with `(b1,B1) != (0,0)` cannot
contain any open orthogonally transitive region: F vanishes there only if
q=0, contradicting (2.3). In fact F is a nonzero vector-valued two-form
at every base point whenever q is nonzero.

For an integral change of unit-period angular basis `theta'=P theta`,
`P in GL(2,Z)`, with a common base orientation, the transformation laws are

    A'=P A, H'=P^(-T) H P^(-1),
    q'=P^(-T)q, S'=P S, M'=P M P^T.                      (5.1)

They preserve q dot S and make the matching condition coordinate
independent. Reversing the chosen base orientation changes both q and S
by a further sign. For unequal physical angular periods one first uses
the corresponding normalized lattice basis; arbitrary linear rescaling
also changes v and the coordinate angular-volume factor in (3.3).

The asymptotic product faces of the exact family do not force zero q:
they are limits, not open orthogonally transitive subsets. Formula (2.2)
exhibits exactly how a decaying connection curvature can retain a
nonzero constant weighted charge. This distinction is required for any
application to the finite E_D collars.

The original marked Dehn-twist assignment has `B1=2/pi^2` at first order
when the amplitude is the physical fibre period. Its nonlinear matching
must carry the resulting nonzero charge into every connected invariant
Einstein continuation. This statement does not prove that the entire
closed surface bundle carries such a global free torus action, nor that
an asymptotically modified construction agrees with an exact model on an
open set. Those are separate geometric assertions.

## 6. Checks

`round4_construction_check.py` independently computes the actual mixed
Ricci component for a nontrivial class with arbitrary varying base metric,
two varying orbit lengths, and connection, verifying the normalization
in (1.4). It also checks the first Jacobi charge, the exact reference
density (4.1), all integrated Taylor coefficients (4.2)--(4.4), and the
lattice covariance and positive-matrix identities. The Stokes limits,
analyticity, positivity, and matching statements are proved above;
symbolic checks are not substituted for those analytic arguments.
