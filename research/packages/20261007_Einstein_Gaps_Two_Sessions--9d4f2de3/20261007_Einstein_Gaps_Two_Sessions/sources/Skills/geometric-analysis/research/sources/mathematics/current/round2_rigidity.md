# Global monopole phase separation without a global Weyl eigenvalue gap

Date: 2026-09-19. The live Skill was reread in full. The mathematical inputs
below are the spinor deficit and Walsh identities in the live
`research/20260916_rigidity.tex`, sections beginning at lines 645 and 836.
This note does not change the Skill or claim an arbitrary-collapse theorem.

The main improvement proved here is global rank-one approximation of all
the relevant harmonic forms, despite a bad set where the Weyl eigenline is
undefined or its spectral gap degenerates. The existing amplitude estimates
control harmonic mass on that bad set. Thus the phase-separation estimates
need no additional global spectral-gap or bounded-weight hypothesis.

## 1. Definitions and the precise input

Work on a closed oriented four-manifold and write

    delta=||g^(-1)Ric+I||_(infinity,op),  E=Ric+g, e=s+4,
    u=|W+|HS, w=lambda_min(W+), t=s+8 sqrt(6)u,
    a=sqrt(2/3)u, q=-s+sqrt(6)u,
    b=2s/3+2w, f_scalar=2s/3-2a,
    G=f_scalar^2-b^2,
    D=|E|^2+e^2+t^2+G,   dcal=integral D.

Here delta<=1/64, so s<0 and b<0; thus this G agrees with the negative-part
definition in the manuscript. It is nonnegative. The symbol dcal denotes
an integral, not the topological ratio defect used elsewhere. The
Hilbert--Schmidt norm is that of the operator on Lambda+; it is not the
largest-eigenvalue norm.

For a monopole class indexed by epsilon, let H_epsilon be its harmonic
self-dual representative, p_epsilon=||H_epsilon||2^2, and put

    Qcal=integral q^2, K=Qcal/(72 pi^2),
    Delta_epsilon=Qcal-72 pi^2 p_epsilon >=0,
    L=q/(6 sqrt(2)pi), c0=3/(4 sqrt(2)pi).

The manuscript's rescaled Seiberg--Witten argument supplies

    || |H_epsilon|-L ||2^2 <= Delta_epsilon/(18 pi^2),       (1)

and, on any measurable region where the lowest eigenline has gap >=gamma
and q<=F^2, it supplies

    integral |Pi_perp H_epsilon|^2
      <= [1/(36 pi^2)+F^2/(216 gamma pi^2)] Delta_epsilon.   (2)

These estimates follow by smooth positive approximation of sqrt(q) if
necessary. H_epsilon is fixed in that approximation, so the limiting
inequalities contain no residual approximation term.

For the spinor statements below the source is the manuscript's equations
`quantSW` and `eigenline-deficit`. In its normalization psi=2sqrt(2)sigma(Phi),
the nonnegative spectral defect is

    D_eig=2 integral [<W+psi,psi>+sqrt(2/3)u|psi|^2]
           <=4Delta/27+eta.

Where the lowest eigenline has gap >=gamma, its integrand is at least
2gamma|(I-Pi)psi|^2. Hence

    integral_U |(I-Pi)psi|^2 <=2Delta/(27gamma)+eta.     (2a)

The arbitrary eta>0 accounts for the smooth weight approximation. This
derivation specifies the spinor normalization behind (18c), independently
of the harmonic-form projection estimate (2).

For the sign-cube application suppose the harmonic forms are actual linear
combinations H_epsilon=sum_r epsilon_r x_r for the specified monopole classes.
Let Delta_bar be the average of Delta_epsilon over this finite cube. The cube
may vary from one manifold to another; none of the constants below depend
on its number of vertices or coordinates.

## 2. A good set produced by the density itself

Define the measurable sets

    U={D<=1/64}, B=M\U.

Then Vol(B)<=64 dcal. On U, |t|<=1/8 and |e|<=4delta<=1/16. Since

    a=(t-s)/24,

we have

    |a-1/6|<=1/128,   61/384<=a<=67/384.                  (3)

Let z=w+a>=0. Because w<=0, z<=a, and

    G=2z(-4s/3+4a-2z)>=8z.

Consequently z<=1/512 on U. Trace-freeness gives the other two eigenvalues as

    lambda_(2,3)=-w/2 +/- (1/2)sqrt(2u^2-3w^2).

Since 2u^2-3w^2=6az-3z^2, the gap satisfies

    lambda2-lambda1
      >=(3/2)(61/384-1/512)
         -(1/2)sqrt(6(67/384)/512) >1/8.                 (4)

Also q=-s+3a<=587/128<5. Thus (2) applies on U with gamma=1/8 and F^2=5:

    integral_U |Pi_perp H_epsilon|^2
      <=23 Delta_epsilon/(108 pi^2).                    (5)

Let P=Pi on U and P=0 on B. It is a measurable orthogonal projection of
rank one on U and rank zero on B. Its derivative is neither taken nor
assumed controlled. In particular, no choice of a global eigenvector or
orientation of its line bundle is needed.

## 3. Bad-set mass is controlled by amplitude, not pointwise bounds on H

The exact identity

    q-9/2=(t-9e)/8

gives

    integral (q-9/2)^2 <=(41/32)dcal.                    (6)

Combining (1) and (6),

    || |H_epsilon|-c0 ||2^2
      <=Delta_epsilon/(9 pi^2)+41 dcal/(1152 pi^2).      (7)

It follows that

    integral_B |H_epsilon|^2
      <=2 || |H_epsilon|-c0 ||2^2+2c0^2 Vol(B)
      <=[2 Delta_epsilon/9+(36+41/576)dcal]/pi^2.        (8)

This is the key concentration estimate. A small-volume set cannot carry an
uncontrolled fraction of harmonic mass because the norm of that harmonic
form is already close to a nonzero constant in L2. It is unnecessary to
assume a harmonic-form L-infinity bound, a Sobolev constant, or noncollapse.

**Global projection theorem.** Under the preceding hypotheses,

    ||(I-P)H_epsilon||2^2
      <=[47 Delta_epsilon/108+(36+41/576)dcal]/pi^2
      <=(Delta_epsilon+37dcal)/pi^2.                    (9)

Indeed, add (5) and (8). This theorem removes the extra global gap and weight
bounds from the manuscript's conditional eigenline-alignment step.

There is also a useful global algebraic identity, whether or not the lowest
eigenvalue is simple. Choose any rank-one projection Pi onto a lowest
eigenvector and set A0(Pi)=I/12-Pi/4. Direct expansion gives

    |W+-A0(Pi)|HS^2=u^2+1/24+w/2
      =(3/2)(a-1/6)^2+z/2
      <=(t^2+e^2)/192+G/16 <=D/16.                     (9a)

This uses a-1/6=(t-e)/24 and G>=8z. Thus D controls squared distance to
the complete forbidden-spectrum orbit pointwise, even at eigenvalue
degeneracies. The projection need only be measurable for this identity.

## 4. Global Walsh phase separation

Write y_r=(I-P)x_r. Sign averaging (9) and using Walsh orthogonality yields

    sum_r ||y_r||2^2 <= B0,
    B0=(Delta_bar+37dcal)/pi^2.                         (10)

On U write Px_r=alpha_r v for a locally chosen unit vector in the lowest
eigenline, and set alpha_r=0 on B. Changing v to -v changes all alpha_r by
the same sign, so alpha_r^2 and alpha_p alpha_q are globally defined.

The zeroth and pairwise Walsh coefficients, together with (1), give

    ||sum_r |x_r|^2-L^2||1 <=2sqrt(K Delta_bar/(18 pi^2)),
    ||<x_p,x_q>||1 <=sqrt(K Delta_bar/(18 pi^2)), p!=q.

Since the P and I-P pieces are orthogonal pointwise, we obtain globally

    ||sum_r alpha_r^2-L^2||1
      <=2sqrt(K Delta_bar/(18 pi^2))+B0,                 (11)

    ||alpha_p alpha_q||1
      <=sqrt(K Delta_bar/(18 pi^2))+B0/2, p!=q.         (12)

For instance, for any fixed h>0,

    Vol{|alpha_p|>=h and |alpha_q|>=h}
      <=h^(-2)[sqrt(K Delta_bar/(18 pi^2))+B0/2].        (13)

The constant target can replace L^2, with the explicit additional error

    ||L^2-c0^2||1
      <=(sqrt(K)+c0 sqrt(Vol M))sqrt(41 dcal/(2304 pi^2)). (14)

On the critical connected-sum locus the manuscript gives

    Delta_bar=O(A delta^2), dcal=O(A delta^2),
    K asymptotic to A, Vol M asymptotic to A.

Thus alignment (10) has normalized error O(delta^2), while phase products
and phase mass (11)--(14) have normalized error O(delta). These conclusions
now require no global spectral gap and no global bound on q. The only
global class assumption is the actual monopole sign-cube hypothesis.

**Remaining limitation.** P is measurable, not a controlled frame. The
estimates do not prevent phases from occupying different large regions
joined through small transition sets; they do not provide equicontinuity,
a common geometric limit, or a fixed harmonic patch. No topological
contradiction follows from (11)--(14) alone.

## 5. The spinor input supplies a bounded approximate almost-Kahler form

There is also usable first-derivative information, but it has a specific
strength. For smooth positive f approximating sqrt(q), let psi be the
quadratic self-dual form in the manuscript, rho=|psi|=|Phi|^2, and
varphi=(3/2)psi. The spinor maximum principle gives

    sup rho <=sup(-s)/inf f <=5/sqrt(3)+o(1).           (15)

Indeed, at a maximum of rho the spinor Weitzenbock equation gives
f rho<=-s there; globally -s<=5 and q>=-s>=3. The optimal amplitude estimate
integral f^2(|varphi|-f)^2<=Delta+o(1) then gives

    ||rho-(2/3)sqrt(q)||2^2 <=4Delta/27+o(1).

The square-root map is Lipschitz on q>=3, so (6) yields

    ||rho-sqrt(2)||2^2 <=C(Delta+dcal)+o(1).             (16)

The Hodge defect is at most 4Delta/27+o(1). For this self-dual form,

    ||dpsi||2^2+||d*psi||2^2 <=4Delta/27+o(1).          (17)

Finally the two-form Weitzenbock identity and (15) imply

    integral |nabla psi|^2
      <=4Delta/27+(sup rho)^2[(5/3)Vol M+2 integral u]+o(1).

Since t and e are included in D, integral u^2<=C(Vol M+dcal). Therefore

    integral |nabla psi|^2 <=C(Vol M+dcal+Delta)+o(1).  (18)

For a critical near-equality sequence, these are a uniform normalized W1,2
bound, amplitude approaching sqrt(2), and Hodge defect tending to zero.
They do not say that the full covariant derivative tends to zero. Nor does
(16) give pointwise nonvanishing. These distinctions matter when replacing
psi by a unit form or using it to define a differentiable frame.

## 5a. A smooth bounded W1,2 model for the Weyl tensor itself

The spinor form yields a more constructive output than a measurable
projection, and it requires no normalization or division at its zero set.
For each eta>0, choose the smooth positive approximation to sqrt(q) and a
rescaled monopole solution so accurately that every approximation error
below is absorbed into eta. Define the smooth trace-free symmetric operator

    A_psi=(|psi|^2/24)I-(1/8)psi tensor psi.             (18a)

It has eigenvalues -rho^2/12,rho^2/24,rho^2/24. At rho^2=2 these are exactly
the target eigenvalues. The maximum principle permits rho<=3 throughout.

**Coupled approximation theorem.** For this choice of psi,

    ||A_psi||infinity,HS <=9/(4 sqrt(6)),
    ||W+-A_psi||2^2 <=Delta+649dcal+eta,
    integral |nabla A_psi|^2 <=10 Vol M+Delta+dcal+eta.   (18b)

Here Delta is the defect of the chosen actual monopole class. The estimates
apply to each chosen class separately and are not statements about a fixed
spinor limit as the approximating weight varies.

**Proof.** Let Pi be a measurable lowest-eigenline projection everywhere,
agreeing with the simple projection on U, and put y=(I-Pi)psi. The spectral
defect gives, on U,

    integral_U |y|^2 <=2Delta/(27 gamma)+eta
                       =16Delta/27+eta.

On B use |psi|<=3 and Vol(B)<=64dcal. Consequently

    integral |y|^2 <=16Delta/27+576dcal+eta.             (18c)

The amplitude estimate can be made explicit. The lower bound f^2>=3 gives
||rho-(2/3)sqrt(q)||2^2<=4Delta/27+eta. Since q and 9/2 are at least 3,

    |sqrt(q)-sqrt(9/2)|^2 <=(q-9/2)^2/12.

Using (6),

    ||rho-sqrt(2)||2^2 <=8Delta/27+41dcal/432+eta.        (18d)

The elementary rank-one identity

    |psi tensor psi-rho^2 Pi|HS^2=2rho^2 |y|^2

and |A0(Pi)|HS^2=1/24 imply

    |A_psi-A0(Pi)|^2
       <=rho^2 |y|^2/16+(rho^2-2)^2/48.

Combine this with (9a), rho<=3, and (3+sqrt(2))^2<20:

    ||W+-A_psi||2^2
       <=dcal/8+(9/8)integral |y|^2
                      +(20/24)||rho-sqrt(2)||2^2
       <=(74/81)Delta+(1/8+648+205/2592)dcal+eta
       <=Delta+649dcal+eta.

For the derivative bound, differentiate (18a). For any vector derivative
v=nabla psi the exact algebraic identity is

    |dA_psi(v)|^2=rho^2 |v|^2/32+<psi,v>^2/96
                 <=rho^2 |v|^2/24.

Hence integral |nabla A_psi|^2 <=(3/8)integral |nabla psi|^2. In the proof
of (18), a fully explicit bound follows from

    integral u^2 <=(dcal+25 Vol M)/192,
    integral u <=(1/2)(Vol M+integral u^2).

These give integral |nabla psi|^2<=26 Vol M+Delta+dcal+eta, which proves
the last inequality of (18b). Finally |A_psi|^2=rho^4/96 proves the
pointwise bound. This completes the proof.

The residual R=W+-A_psi is therefore small in normalized L2 in the critical
regime. The intrinsic weak Bianchi estimate also gives

    ||div A_psi||_(H^-1,av)
      <=C[delta+sqrt((Delta+649dcal+eta)/Vol M)].        (18e)

Indeed div A_psi=div W+-div R, Cotton is a covariant first derivative of
E, and integration by parts bounds both terms in the intrinsic negative
norm. The operator and test norms in (18e) use the same metric; this does
not identify those normed spaces across a varying sequence.

The coupled theorem supplies a bounded W1,2 tensor model for W+, weakly
harmonic and close to the forbidden orbit. It still does not supply a
coordinate frame, a uniform Sobolev inequality, or compactness of the
varying metric connections. Those are distinct issues, not a zero-set
problem for (18a).

## 6. A useful weak-source estimate that preserves the L-infinity Ricci information

A generic H-minus-one norm discards some information. Throughout this note,
H^-1,av is the dual, under normalized integration, of the same metric's
inhomogeneous covariant H1 norm

    ||phi||_(H1,av)^2=average (|phi|^2+|nabla phi|^2).

It is an intrinsic norm for each individual metric, not a shared coordinate
norm across a varying family. Let C be the Cotton
tensor, written as a fixed linear combination of covariant derivatives of
E and tr E. For a bounded tensor a with nabla a in L2, integration by parts
against a smooth test tensor phi gives

    |average <a C,phi>|
      <=C ||E||infinity [||a||infinity ||nabla phi||_(2,av)
                         +||nabla a||_(2,av)||phi||_(2,av)]. (19)

The contraction pattern only changes the dimensional constant. Here all
averages use the same metric, so no coordinate comparison or Sobolev
embedding is involved. In particular,

    ||a C||_(H^-1,av)
      <=C ||E||infinity (||a||infinity+||nabla a||_(2,av)). (20)

Thus multiplying Cotton by the bounded W1,2 spinor form is harmless for this
weak estimate. A W1,4 bound is NOT needed for this particular multiplication.

The different product arising from W+=A(psi)+R is R nabla psi, where only
R in L2 is small. It tends to zero in L1 if nabla psi is bounded in L2,
but need not tend to zero in H^-1. That is the actual endpoint distinction.
The same issue arises for an uncontrolled connection coefficient Gamma in
L2 multiplied by Weyl curvature in L2.

## 7. An explicit endpoint counterexample for the error commutator

This is a functional example on a fixed Euclidean four-ball, not a metric
counterexample. Let chi be a fixed smooth bump, choose zeta smooth and
positive on its support, and for r decreasing to zero set

    a_r(x)=chi(x/r) sin(x1/r^(3/2)),
    R_r(x)=r^(-3/2)chi(x/r) cos(x1/r^(3/2)),
    phi_r(x)=r^(-1)zeta(x/r).

All functions are supported in a ball of radius O(r). Scaling gives

    ||a_r||infinity<=C, ||nabla a_r||2=O(r^(1/2)),
    ||R_r||2=O(r^(1/2)), ||phi_r||H1<=C,
    ||R_r partial1 a_r||1=O(r).

Nevertheless, after x=ry, oscillatory averaging gives

    integral R_r (partial1 a_r) phi_r
      ->(1/2)integral chi(y)^2 zeta(y)dy >0.

The cutoff-derivative term is O(r^(1/2)); the main term contains
cos^2(y1/sqrt(r)). Hence

    liminf ||R_r partial1 a_r||H^-1 >0.                 (21)

This remains an obstruction even when both L2 factors tend to zero.
One may use a_r as the angle of a bounded unit-vector or unit-self-dual-form
rotation; its amplitude is then exactly constant and its first derivative
and Hodge defect are small in L2. The construction does not impose the
metric curvature equation or the exact Seiberg--Witten equations, and so
does not disprove a compensated estimate exploiting those additional
equations. It does disprove an estimate based only on the displayed norms.

Small L1 error suffices for distributional convergence against fixed smooth
tests. On an already controlled coordinate domain it also gives convergence
in W^(-1,p) for p<4/3. Combining such bounds with ellipticity and bounded
amplitudes is potentially useful. Uniform domain and coefficient control,
or an intrinsic substitute, is still required to use those embeddings
and inverse estimates across collapsing metrics.

## 8. The intrinsic energy test has an exact Hodge cancellation

The bounded model removes the cubic concentration problem, so it is useful
to test directly whether its Weitzenbock energy supplies a contradiction.
Here the precise obstruction is stronger than a generic negative-norm
warning: the resulting identity is already contained in the two-form
Hodge identity.

Let J_psi be the divergence of the four-index tensor corresponding to
A_psi, with its ordinary three-index tensor norm. Use the operator
Hilbert--Schmidt norm for nabla A_psi. A covariant first-jet computation gives

    |nabla A_psi|^2-|J_psi|^2
      =rho^2(|nabla psi|^2-2|dpsi|^2)/64
        +rho^2|drho|^2/32
        -(rho/16)<i_(grad rho)psi,*dpsi>.               (22)

For example, when rho^2=2, write psi=omega1 in a self-dual frame with
|omega_j|^2=2, and nabla psi=a tensor omega2+b tensor omega3. Put
S=|a|^2+|b|^2 and c=<i_a omega2,i_b omega3>. Then

    |nabla A_psi|^2=S/8,
    |J_psi|^2=(S+c)/8,
    |dpsi|^2=S+2c, |nabla psi|^2=2S,

which proves the constant-amplitude case. The exact checker verifies (22)
for all twelve components of the covariant first jet, including amplitude
derivatives, using the oriented self-dual frame. Although rho itself can
fail to be smooth at zeros, every weighted expression in (22) extends:
rho drho=(1/2)d(rho^2) and rho^2|drho|^2=|d(rho^2)|^2/4.

Write the curvature term in the self-dual two-form Hodge formula as

    B_psi=(s/3)rho^2-2<W+psi,psi>.

The algebraic identities |A_psi|^2=rho^4/96 and
tr(W+ A_psi^2)=rho^2<W+psi,psi>/192 give

    (s/2)|A_psi|^2-6tr(W+ A_psi^2)=rho^2 B_psi/64.     (23)

Test the two-form Hodge identity against rho^2 psi. Since psi is self-dual,
|d*psi|^2=|dpsi|^2, and integration by parts yields

    integral rho^2[|nabla psi|^2+B_psi-2|dpsi|^2]
      =4 integral rho<i_(grad rho)psi,*dpsi>
        -2 integral rho^2|drho|^2.                    (24)

For clarity, the Hodge side produces the cross term
2<*dpsi,i_(grad rho^2)psi>, and the rough-Laplacian side produces
(1/2)<d(rho^2),d(rho^2)>. Thus all signs in (24) are fixed directly by
integration by parts.

Combining (22)--(24) proves the intrinsic model identity

    integral [|nabla A_psi|^2-|J_psi|^2
               +(s/2)|A_psi|^2-6tr(W+ A_psi^2)]=0.     (25)

This derivation requires no Weyl-derivative bound. But (25) provides no
additional constraint beyond the weighted Hodge formula: its terms cancel
exactly for every smooth self-dual psi. In particular, the negative
potential at the target is not a contradiction.

### A compulsory derivative-energy defect in a hypothetical critical sequence

The cancellation gives a concrete additional necessary degeneration.
Suppose a sequence has delta_j->0 and

    (Delta_j+dcal_j)/Vol(M_j)->0,

and choose approximation errors eta_j=o(Vol(M_j)). Take the spinor forms
constructed above. Besides the preceding estimates, the amplitude defect
in the manuscript supplies integral |drho_j|^2<=2Delta_j/27+eta_j.
Thus rho_j is uniformly bounded, rho_j->sqrt(2) in normalized L2, and
both dpsi_j and drho_j tend to zero in normalized L2. Put
R_j=W+_j-A_(psi_j); its normalized L2 norm tends to zero.

Because A_psi psi=-(rho^2/12)psi, one has

    B_psi=(s/3)rho^2+rho^4/6-2<R psi,psi>.

All moments of the bounded rho converge to their constant-amplitude values,
and the R term tends to zero in normalized L1. The unweighted Hodge formula
therefore gives

    average |nabla psi_j|^2 ->2.                       (26)

The cross terms on the right of (24) tend to zero by Cauchy--Schwarz.
Its curvature term has limit

    average rho_j^2 B_(psi_j) ->(-4/3)*4+8/6=-4.

Consequently

    average rho_j^2 |nabla psi_j|^2 ->4.               (27)

Using the differentiated quadratic-map identity from Section 5a and (22),

    average |nabla A_(psi_j)|^2 ->1/8,
    average |J_(psi_j)|^2 ->1/16.                     (28)

At the same time (18e) gives J_(psi_j)->0 in the intrinsic H^-1,av norm.
Thus the divergence has a definite surviving L2 energy despite its vanishing
weak norm. No assumed uniform integrability of derivative energy is used:
(27) follows from the weighted Hodge identity itself.

This is a necessary condition, not a construction of such a sequence. It
shows exactly why the bounded W1,2 model does not close the gap by simply
squaring its weak Bianchi source. Replacing J_psi=div W+-div R by a small
L2 term would incorrectly discard the nonzero limit in (28). Either an
additional mechanism must exclude this derivative-energy defect, or a
successful proof must avoid that replacement. A Cotton L2 divergence is
not itself the obstruction to using (25); the genuine issue is the
uncontrolled strong norm of this particular weakly small source.

## 9. A uniform gap under bounded full curvature, including collapsed metrics

Let O0 be the orthogonal orbit of diag(-1/6,1/12,1/12) in the
trace-free self-adjoint endomorphisms of Lambda+, and put

    F(g)=dist_HS(W+(g),O0)^2.

The distance uses the operator Hilbert--Schmidt norm. The following
consequence of controlled-patch compactness does not require monopoles.

**Proposition.** For every finite K there is c0(K)>0 such that every
closed oriented smooth Riemannian four-manifold with |Rm_full|<=K satisfies

    average [|Ric+g|^2+F(g)] >=c0(K).                 (29)

Consequently delta^2+average F>=c0(K)/4. No volume, diameter,
base-injectivity, Ricci-derivative, or Cotton bound is assumed. Constants
are existential; the proof does not compute c0(K).

Here are the details, including the local development and average transfer.
They also explain why collapse does not invalidate this corollary.

### Fixed-scale source geometry

Set rho=1/(100sqrt(1+K)). Since |sec|<=K, for each p the exponential map
on the Euclidean tangent ball B_rho(0) has no conjugate points and is a
local diffeomorphism. Equip this source with h=exp_p^*g. Rauch comparison
gives, after identifying T_pM with Euclidean space,

    Q0^(-1)I<=h<=Q0 I

with, for example, a fixed Q0=2. The source need not map injectively into
M. Its center nevertheless has source distance d_h(0,v)=|v|: Gauss's
lemma gives the lower bound for every path and the radial path attains it.
Thus the center has a fixed cut-free radius in the source itself.

There is a fixed interior harmonic radius on this source, depending only
on K and the chosen buffer. One way to check applicability of the usual
local bounded-geometry theorem is to take a source point x well inside
B_rho and a sufficiently small t depending only on rho. The Euclidean
ball B_(t/sqrt(Q0))(x) is contained in the source metric ball B_t^h(x),
and hence

    Vol_h B_t^h(x)>=Q0^(-4) omega_4 t^4.

Full curvature is bounded on a larger buffered source ball. The local
bounded-curvature volume-to-injectivity estimate, followed by the
bounded-Ricci harmonic-radius estimate, therefore gives uniform
ellipticity and C^(1,alpha) harmonic coordinates on a smaller fixed
domain. This is an interior application: it requires neither source
completeness nor an injectivity-radius lower bound on the base. The
classical harmonic-radius/compactness input is Anderson's
[1990 theorem](https://doi.org/10.1007/BF01233434); its local,
away-from-boundary formulation and the stronger bounded-curvature case
are made explicit in [his survey, Section 2, Remark 2.4(i),(iii)](https://arxiv.org/pdf/gr-qc/0208079).

Fix s>0 sufficiently smaller than rho, depending only on K, so the closed
source 3s-ball is compactly contained in the domain. Subsequent harmonic
charts can be restricted to a fixed domain whose image lies inside the
source s-ball. In particular no sequence-dependent rescaling is used.

### The transfer lemma does not require a covering map

Suppose pi:(U_tilde,h)->(M,g) is a local isometry taking p_tilde to p,
and the closed source 3s-ball is compactly contained in U_tilde. For any
nonnegative measurable H,

    average_(B_s^h(p_tilde)) pi^*H
      <=[Vol_h B_(3s)^h(p_tilde)/Vol_h B_s^h(p_tilde)]
            average_(B_s^g(p)) H.                    (30)

To prove this, write m_a(q) for the number of preimages of q in the
source a-ball. For q,y in the base s-ball, concatenate minimizing
geodesics q->p->y, of total length less than 2s. Lift this path from
each preimage of q in the source s-ball. Each lift remains in the
source 3s-ball. Compact containment ensures continuation for the whole
path, and reverse-path uniqueness shows that its endpoints are distinct.
Thus m_s(q)<=m_(3s)(y). The fibers in the compact buffer are finite:
they are closed and a local diffeomorphism makes them discrete. Integrate
the inequality over y in the base s-ball to obtain

    m_s(q) Vol_g B_s(p)<=Vol_h B_(3s)(p_tilde).

The area formula now gives (30). This proof does not suppose the map is
a global cover, a regular cover, or has uniformly bounded multiplicity.
On the exponential development the ratio in (30) is at most 3^4 Q0^8
by the preceding metric bounds.

### Proof of the gap

If (29) failed, there would be a sequence with |Rm_full|<=K and
average H_j->0, where H_j=|Ric+g|^2+F. Global Ricci is bounded below by
-3K g. With v_(-K) denoting the four-dimensional model-ball volume,
Bishop--Gromov comparison and Fubini give

    integral_M average_(B_s(p)) H_j dmu(p)
      <=D_K(s) integral_M H_j,
    D_K(s)=v_(-K)(2s)/v_(-K)(s).

Indeed q in B_s(p) implies B_s(q) subset B_(2s)(p), so
Vol B_s(q)<=D_K(s) Vol B_s(p). There is therefore a center p_j with
average_(B_s(p_j)) H_j<=D_K(s) average_M H_j->0.

Pull back at p_j as above. Equation (30) transfers this vanishing
average to the noncollapsed source s-ball. Source volumes are bounded
above and below, so the integral tends to zero on every smaller fixed
harmonic chart. After a subsequence, the metrics converge in C1 there,
with uniform ellipticity and C^(1,alpha) bounds. The Ricci residual
tends to zero in L2. Section 3 of `round2_weak_curvature.md` gives strong
L2 convergence of W+ and a smooth Einstein limit satisfying Ric=-g.
This step uses the Cotton source only in H^-1, not in L2. The local
integral of F tends to zero, so the limit has precisely the spectrum
(-1/6,1/12,1/12). Section 4 of that note excludes this Einstein germ.
The contradiction proves (29). Since |Ric+g|^2<=4delta^2, its stated
delta consequence follows as well.

### Monopole consequence and what the added hypothesis costs

In the manuscript's pinched regime delta<=1/4, s>=-5 and s<=-3. The
exact algebraic estimate from Section 5a, which only needs s<=-3, is

    F<=(t^2+e^2)/192+G/16.

Consequently |E|^2+F<=D pointwise. The manuscript's monopole density
budget, equation `436675`, therefore gives under |Rm_full|<=K

    c0(K)<=average D<=436delta^2+675d,
    delta^2+d>=c0(K)/675,                            (31)

where d=(1/3-k/A)_+ for the indicated general-type blow-up family.
The same statement holds with d=(T/A-2/3)_+ under the corresponding
monopole input. Thus a dimension-four family-uniform pinching/topology
gap does follow from the additional full-curvature bound, even with
collapse and unbounded Cotton. This is a conditional corollary, not the
unrestricted Yau26 statement: an average L2 curvature budget does not
imply the required fixed-scale pointwise curvature bound.

There is also a localized necessary degeneration. Suppose delta_j->0
and average_M F_j->0. For fixed K,R>0 define

    Omega_(K,R)(g)={p: sup_(B_R(p)) |Rm_full|<=K}.

Then

    Vol Omega_(K,R)(g_j)/Vol M_j ->0.                 (32)

Otherwise that proportion is at least some alpha>0 along a subsequence.
Choose the preceding fixed exponential radius additionally below R/4,
and the averaging radius s still smaller. Global Ricci lower bounds from
delta_j->0 give the same uniform Fubini estimate. Averaging over Omega
selects p_j in Omega with

    average_(B_s(p_j)) F_j
      <=[D_1(s)/alpha] average_M F_j ->0.

The full-curvature bound is available throughout each needed exponential
development, and E_j tends to zero uniformly. The same source compactness,
transfer, and forbidden-germ argument is a contradiction. Statement (32)
says that a fixed-radius neighborhood of curvature concentration must
meet almost every center. It does not assert pointwise curvature
divergence or that the high-curvature set itself has positive volume.

## Status

The proven global projection theorem (9), phase estimates (11)--(14), and
smooth coupled Weyl approximation (18b) are the main round-two advances.
They remove a real extra geometric assumption from the manuscript's phase
argument and supply a bounded W1,2 model without normalizing at spinor
zeros. The exact cancellation and compulsory derivative-energy limits
(26)--(28) identify what remains after the direct intrinsic test. The
bounded-full-curvature corollary (29)--(31) proves a conditional uniform
gap without a base noncollapse or Cotton bound; (32) specifies necessary
fixed-scale curvature degeneration in any counterexample sequence.
The weak-source estimate
(19) retains the useful L-infinity strength of Ricci pinching, while (21)
identifies a separate endpoint obstruction. None supplies the missing
geometric compactness or resolves the unrestricted Ricci-pinching problem.
