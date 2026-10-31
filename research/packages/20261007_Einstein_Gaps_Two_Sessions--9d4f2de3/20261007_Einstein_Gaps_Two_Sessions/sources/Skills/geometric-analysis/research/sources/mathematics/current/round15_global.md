# Product-exterior response and the boundary equation for closed shear repair

## 1. The question and the result

The Round-14 pure-shear metrics have a signed throat force of order
\(c^3\), where the waist length is \(2\pi c\). A global correction may
change both adjacent blocks and every tensor mode. This note computes
what the actual hyperbolic product exteriors contribute, rather than
treating them as fixed endpoints or as an unspecified error.

Three exact conclusions are useful.

1. The Einstein--Hilbert action with its full boundary term on any
   hyperbolic product exterior \(B\times F\) is topological:
   \[
   \mathscr A(B\times F)=4\pi\chi(B)\operatorname{Area}(F).
   \tag{1}
   \]
   Base or fiber hyperbolic moduli do not provide an independent
   action gradient capable of absorbing a shear force.
2. For an arbitrary infinitesimal exterior tensor, its projection onto
   the fiber Teichmüller directions satisfies the scalar Laplace equation
   on \(B\). This projection is gauge invariant and does not assume any
   symmetry of the tensor. Exterior response can redistribute a
   Teichmüller traction, but its total charge is zero.
3. The resulting circle-averaged matching operator is a positive
   capacitance operator with a precisely identified constant kernel.
   Its compatibility condition is the sum of the shear stresses.
   Vanishing of that sum solves this averaged linear sector, not the
   remaining boundary functions, constraints, or full nonlinear equation.

These statements explain why the balanced integral examples in
[round15_shear_balance.md](round15_shear_balance.md) remove a real global
projected obstruction. They also identify, without setting it to zero,
the nonlinear exterior response required for a full Einstein repair.

## 2. Boundary action and exact matching

Let \(\Omega\) be a compact four-manifold with smooth boundary. Use the
outward unit normal \(n\), second fundamental form
\(A(X,Y)=g(\nabla_Xn,Y)\), mean curvature \(H=\operatorname{tr}_\gamma A\),
and induced boundary metric \(\gamma\). Define
\[
 \mathscr A_\Omega(g)
 =\int_\Omega(s_g+6)\,d\mu_g+2\int_{\partial\Omega}H_g\,d\mu_\gamma,
 \qquad \Pi=A-H\gamma.
 \tag{2}
\]
For a covariant metric variation \(q\), including arbitrary normal
components, its first variation is
\[
 D\mathscr A_\Omega(q)
 =-\int_\Omega
   \left\langle\operatorname{Ric}
             -\left(\frac{s}{2}+3\right)g,q\right\rangle d\mu
  -\int_{\partial\Omega}\langle\Pi,q^T\rangle d\mu_\gamma.
 \tag{3}
\]
The divergence terms in the scalar-curvature variation cancel the
normal-derivative terms in \(2D\int H\); boundary tangential divergences
integrate to zero. This sign convention is checked by a Euclidean
four-ball: \(2\int H=6|\mathbb S^3|R^2\), while
\(\Pi=-2\gamma/R\), giving the same derivative in (3).

At a normalized Einstein metric \(\operatorname{Ric}=-3g\), the bulk
term vanishes. Along any actual smooth family of such fillings,
\[
 6\,D\operatorname{Vol}
 =2D\!\int_{\partial\Omega}H
   +\int_{\partial\Omega}\langle\Pi,D\gamma\rangle.
 \tag{4}
\]
Thus volume is not locally constant for pieces with boundary. The
closed-manifold volume constancy used in Round 13 cannot be applied to
an exterior block after discarding its boundary terms.

Two Einstein pieces glue smoothly when their marked induced metrics
agree and their outward momenta satisfy
\[
 \gamma_+=\gamma_-,\qquad \Pi_++\Pi_-=0.
 \tag{5}
\]
Indeed the boundary dimension is three, so
\(H=-\tfrac12\operatorname{tr}_\gamma\Pi\) and
\(A=\Pi-\tfrac12(\operatorname{tr}_\gamma\Pi)\gamma\).
Equation (5) is exactly equality of the induced metrics and opposition
of second fundamental forms. Gaussian normal coordinates then match
the first metric derivatives. The tangential Einstein equation
recursively determines the higher normal derivatives from these data,
so smooth Einstein pieces have matching jets of every order.

Each piece must also satisfy the constraints
\[
 s_\gamma+6-H^2+|A|^2=0,\qquad
 \operatorname{div}_\gamma(A-H\gamma)=0.
 \tag{6}
\]
There is no assumption that arbitrary nearby \(\gamma\) admits an
Einstein filling or a single-valued nonlinear Dirichlet-to-Neumann map.
The ordinary Einstein Dirichlet problem is not elliptic; suitable mixed
boundary conditions are needed. This is established in
[Anderson, Section 3 and Proposition 3.1](https://arxiv.org/pdf/math/0612647).
Equations (3)--(6) apply to actual fillings and their variations, without
postulating such a map.

## 3. The product action is exactly topological

Let \(B\) be a compact oriented surface with smooth boundary and
curvature \(-3\), and let \(F\) be a closed oriented curvature-\(-3\)
surface. Their product \(G=g_B+h_F\) is Einstein with constant \(-3\).
At the boundary, \(A=\kappa\,ds_{\partial B}^2\) in the base direction,
and \(A=0\) in the fiber directions. Here \(\kappa\) is geodesic
curvature relative to the outward-normal second-fundamental-form
convention. Consequently
\[
 \begin{split}
 \mathscr A_\Omega(G)
 &=-6\,\operatorname{Area}(B)\operatorname{Area}(F)
     +2\operatorname{Area}(F)\int_{\partial B}\kappa\,ds\\
 &=4\pi\chi(B)\operatorname{Area}(F).
 \end{split}                                                    \tag{7}
\]
The last step is Gauss--Bonnet,
\(-3\operatorname{Area}(B)+\int_{\partial B}\kappa=2\pi\chi(B)\).
Since \(\operatorname{Area}(F)=4\pi(g(F)-1)/3\), (7) is constant
under all hyperbolic product deformations of the fixed topological
surfaces, including changes of the base boundary lengths and shapes.

Pointwise, \(\Pi\) has zero circle component and fiber component
\(-\kappa h_F\). Thus
\[
 \langle\Pi,Q\rangle=0
 \quad\text{for every fiber tracefree tensor }Q.
 \tag{8}
\]
In particular an exact hyperbolic product exterior has no fiber
Teichmüller traction, regardless of its base or fiber moduli.

Volume nevertheless varies. For example, let \(B_R\) be a hyperbolic
disk of radius \(R\), put \(k=\sqrt3\), and write \(A_F=\operatorname{Area}(F)\).
Then
\[
 \operatorname{Vol}(B_R\times F)
   =\frac{2\pi A_F}{k^2}(\cosh(kR)-1),\qquad
 \int_{\partial(B_R\times F)}H=2\pi A_F\cosh(kR).
 \tag{9}
\]
Their combination (2) is the constant \(4\pi A_F\).
This elementary exact family shows why exterior volume is not a
free scalar parameter which can be inserted into the matching equation
independently of the mean-curvature term.

## 4. Projection of every exterior deformation onto fiber moduli

Let \(\mathcal T(F)\) denote the finite-dimensional space of
tracefree, divergence-free symmetric two-tensors on \(F\), with its
\(L^2(F)\) inner product. On a hyperbolic surface these are precisely
the infinitesimal hyperbolic metric deformations in transverse gauge.
Each satisfies
\[
 P_FQ=0,\qquad
 P_F=\frac12\nabla_F^*\nabla_F-\mathring R_F.
 \tag{10}
\]
For example, the scalar-curvature variation of a TT tensor is zero,
and \(\operatorname{Ric}_{h_F}=K_{h_F}h_F\) in dimension two;
therefore \(D(\operatorname{Ric}+3h_F)[Q]=0\). Since its Bianchi
gauge term vanishes, (10) follows.

For any smooth symmetric tensor \(q\) on \(B\times F\), without support,
symmetry, or gauge restrictions, define \(U:B\to\mathcal T(F)\) by
fiberwise orthogonal projection of its \(FF\)-block:
\[
 \langle U(b),Q\rangle_{L^2(F)}
 =\int_F\langle q_{FF}(b,\cdot),Q\rangle\,d\mu_F.
 \tag{11}
\]
For the ungauged Einstein linearization,
\[
 \boxed{
 \operatorname{pr}_{\mathcal T}
       D(\operatorname{Ric}+3g)_G[q]
       =-\frac12\Delta_BU.}
 \tag{12}
\]
Here \(\Delta_B=\operatorname{div}\nabla\).

To prove (12), add the Bianchi gauge term so that the operator is
\(\frac12\nabla^*\nabla-\mathring R\). The product splitting is parallel,
and the \(FF\)-block separates into \(-\frac12\Delta_B+P_F\).
Pairing with (10) eliminates \(P_F\). The added gauge term has
fiber projection zero: its pairing is a fiber integration by parts
against \(\delta_FQ=0\). The same argument proves
\(\operatorname{pr}_{\mathcal T}(\mathcal L_XG)=0\) for every vector
field \(X\). Thus (12) is a gauge-invariant projection of the full
operator, not a restriction to a symmetric ansatz.

In particular any infinitesimal Einstein exterior obeys
\[
 \Delta_BU=0,\qquad
 \boxed{\frac12\int_{\partial B}\partial_nU\,ds=0.}
 \tag{13}
\]
Arbitrary angular dependence of \(q\) is included. The second identity
is a total conormal charge, not the assertion that the traction vanishes
at each boundary point.

### Conormal charge versus the physical boundary momentum

The link to (5) includes a Robin term which must not be omitted on
an individual piece. Pair covariant boundary tensors with the fixed
background fiber metric and a fixed \(Q\in\mathcal T(F)\).
Since \(A_{FF}=0\) on a product boundary, variation of the normal and
second fundamental form gives
\[
 (DA[q])_{FF}
 =\frac12\partial_nq_{FF}
   -\frac12\{\nabla_F(q(n,\cdot))+
                         \nabla_F(q(n,\cdot))^{T}\}.
 \tag{13a}
\]
The fiber projection of the second term is zero by
\(\delta_FQ=0\). Normal-normal metric variation multiplies the
vanishing background \(A_{FF}\), and the term \((DH)\gamma_{FF}\)
is fiber pure trace. Consequently
\[
 \boxed{\operatorname{pr}_{\mathcal T}D\Pi[q]
            =\frac12\partial_nU-HU.}
 \tag{13b}
\]
At a matched product interface, the outward background means satisfy
\(H_++H_-=0\), and the induced boundary variation is common to both
sides. Thus their two Robin terms cancel. The linearized physical
momentum equation is exactly equality of the opposing TT conormals
used below. If instead one differentiates the metric-dependent boundary
pairing or its measure, the additional terms multiply
\(\Pi_++\Pi_-=0\) and likewise cancel after the two sides are combined.
They need not vanish on a single side.

For an actual normalized Einstein exterior \(G+q\), write exactly
\[
 \mathcal N_G(q)
 =(\operatorname{Ric}_{G+q}+3(G+q))
       -D(\operatorname{Ric}+3g)_G[q].
 \tag{14}
\]
Then (12) gives the nonlinear charge law
\[
 \boxed{
 \frac12\int_{\partial B}\partial_nU\,ds
       =\int_B\operatorname{pr}_{\mathcal T}\mathcal N_G(q)\,d\mu_B.}
 \tag{15}
\]
For \(|q|_G\leq1/2\), the ordinary difference-of-connections formula
implies
\[
 \left|\int_B\operatorname{pr}_{\mathcal T}\mathcal N_G(q)\right|
 \leq C_F\int_{B\times F}
   \bigl(|q||\nabla^2q|+|\nabla q|^2+|q|^2\bigr)\,d\mu_G .
 \tag{16}
\]
The constant depends on the fixed fiber TT basis and curvature, not
on the base injectivity radius. Formula (15) identifies the response
which an arbitrary nonproduct filling can supply; it is not set to zero.
It is an identity for the background projected conormal. Beyond first
order, the induced metric, unit normal, and momentum also have nonlinear
conversion terms; a full match must use (5), not only (15).

## 5. The actual exterior capacitance matrix

Suppose \(B\) is connected and has boundary circles
\(\Gamma_1,\ldots,\Gamma_m\). Let \(\omega_j\) be the unique harmonic
function on \(B\) equal to one on \(\Gamma_j\) and zero on the other
boundary components. Define
\[
 C_{ij}=\frac12\int_B
                  \langle d\omega_i,d\omega_j\rangle\,d\mu_B.
 \tag{17}
\]
This matrix contains the response of the entire exterior, not only a
collar. Green's identity gives
\[
 C_{ij}=\frac12\int_{\Gamma_i}\partial_n\omega_j\,ds.
 \tag{18}
\]
For constant boundary TT data \(y_i\in\mathcal T(F)\), the harmonic
extension \(U=\sum_j\omega_jy_j\) therefore has integrated conormals
\[
 p_i=\frac12\int_{\Gamma_i}\partial_nU\,ds
        =\sum_jC_{ij}y_j.
 \tag{19}
\]
The matrix is symmetric and nonnegative:
\[
 \sum_{ij}\langle y_i,C_{ij}y_j\rangle
       =\frac12\int_B|dU|^2,\qquad
 \ker(C\otimes I_{\mathcal T})
       =\{(Q,\ldots,Q):Q\in\mathcal T(F)\}.
 \tag{20}
\]
Connectedness proves the last statement. In particular
\(C\mathbf1=0\). Base moduli change the nonzero entries and eigenvalues
of \(C\), but do not create a nonzero total charge.

There is no claim of a uniform inverse while \(B\) degenerates.
Also, \(\partial_n\omega_j\) need not be constant along \(\Gamma_i\).
Equations (17)--(20) are an exact relation for integrated traction;
the nonconstant boundary response must still be matched.

## 6. Combining the exterior with the shear throats

For a throat with \(a=c\cosh(kt)\), the fiber-TT linearized operator
is
\[
 L_s=-\frac1{2a}(a\,\partial_t)'.
 \tag{21}
\]
The homogeneous constant-angular Dirichlet response is the positive
matrix
\[
 D_s=\frac1{2\int_{-R}^R a^{-1}dt}
          \begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
 \tag{22}
\]
Its entries use conormal values \((-aU'(-R)/2,aU'(R)/2)\);
integrated circle traction multiplies (22) by \(2\pi\).
Unlike radial waist and twist tensors, these fiber TT tensors are
genuine ungauged infinitesimal Einstein variables. No Bianchi constraint
has been silently dropped.

Let \(\beta\) be the harmonic integral shear form and
\(T_\beta=\beta\otimes\beta-\tfrac12|\beta|^2h_F\in\mathcal T(F)\).
The shear's TT residual is
\(-\tfrac12a^2z'^2T_\beta\).
The zero-Dirichlet particular repair obeys
\[
 (aU')'=-a^3z'^2T_\beta.
 \tag{23}
\]
Hence its total integrated outgoing traction is
\[
 \boxed{
 p_-^{\rm src}+p_+^{\rm src}
       =-\pi\left(\int_{-R}^Ra^3z'^2dt\right)T_\beta.}
 \tag{24}
\]
For an even throat and the symmetric profiles used here the two terms
are equal. With the exact finite-interval Maxwell profile,
the integral in (24) is \(c^3/J_3(R)\); with the smooth Round-14
cutoff it is \(c^3I_\ell^{-2}\int\eta_\ell^2\operatorname{sech}^3\).
This agrees with the independently computed throat response in
[round15_boundary_response.md](round15_boundary_response.md).

Assemble the exterior matrices (17) and throat matrices \(2\pi D_s\)
using one variable for each marked interface. The sum \(K\) is symmetric
nonnegative. For a connected network with the same fixed marked fiber,
\[
 \ker K=\{\text{one common }Q\in\mathcal T(F)
                         \text{ at every interface}\}.
 \tag{25}
\]
Indeed zero quadratic form makes the boundary values equal on every
connected exterior and across every throat; connectedness propagates
that equality to the whole network.

The finite, circle-averaged fiber-TT matching equation
\[
 Ky+p^{\rm src}=0                                           \tag{26}
\]
is therefore solvable if and only if
\[
 \boxed{\sum_e q_eT_{\beta_e}=0,\qquad
                 q_e=\int_{\text{throat }e}a_e^3z_e'^2dt>0.}
 \tag{27}
\]
When compatible, its solution is unique modulo the common fiber
Teichmüller direction. A single nonzero shear fails (27);
balanced multiple shears can satisfy it.

This is a theorem about the specified projected product-background
boundary system. Integer shear markings preserve the common TT receiver
and the integrated circle charge, since they act by a circle translation
over the identity of \(F\). They need not preserve a nonconstant angular
boundary tensor mode. Thus solving (26) does not match all pointwise
boundary functions, nor does it solve the nonlinear Einstein equation.
Those outputs are retained in the full momentum equation (5), not
discarded as zero.

## 7. The next condition is an exterior response, not a volume adjustment

Equations (15), (24), and (27) distinguish three mechanisms.

- Hyperbolic product moduli alter \(\beta\), \(T_\beta\), and the
  capacitance matrix, but their exterior action remains (7).
- Linear nonproduct exterior response redistributes TT traction through
  (17); it cannot absorb a nonzero aggregate source.
- Nonlinear nonproduct response can contribute the explicit right side
  of (15), and higher boundary modes contribute to (5). Neither term
  has been proved to have a favorable sign or to be negligible.

Thus a candidate full reduction must solve the complement with actual
boundary data and evaluate these contributions in the same scale as
\(c^3T_\beta\). A uniform Dirichlet collar complement alone does not
calculate the exterior response. Conversely the existence of the
capacitance matrix does not remove the finite TT compatibility condition.

This corrects a possible misuse of normalized Einstein volume: a closed
Einstein branch has constant volume, but each truncated block has the
boundary identity (4). At matching interfaces the momenta and mean
curvature terms cancel. There is no extra free volume parameter that
can be adjusted independently to cancel a remaining shear equation.

The work does not improve the Round-14 \(O(c)\) no-repair radius by
itself. It replaces an unspecified global term by an exact product
response, proves the associated projected solvability criterion, and
isolates the genuinely nonproduct nonlinear term needed for a stronger
global conclusion.

## 8. Inputs and verification

- [round14_global.md](round14_global.md): the precise smooth closed
  profile, scalar calibration, integral scales, and local exclusion.
- [round14_shear.md](round14_shear.md): full Ricci blocks and shear stress.
- [round14_collar_complement.md](round14_collar_complement.md): the
  full product linearization and its Dirichlet complement.
- [round13_global.md](round13_global.md): the closed normalized
  Einstein-volume result, used here only with its original hypotheses.
- [Anderson, On boundary value problems for Einstein metrics,
  Section 3](https://arxiv.org/pdf/math/0612647): the non-ellipticity
  of ordinary Einstein Dirichlet data and the role of mixed data.

[round15_global_check.py](round15_global_check.py) verifies the
normalization, action identity, flux factors, and an explicit assembled
capacitance model. The general identities (12), (15), and (20) are proved
by integration by parts; the finite check does not substitute for them.
