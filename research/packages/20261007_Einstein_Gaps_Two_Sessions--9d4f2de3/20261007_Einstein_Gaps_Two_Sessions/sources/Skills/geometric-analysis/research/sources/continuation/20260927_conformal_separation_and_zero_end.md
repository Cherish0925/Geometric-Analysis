# Conformal separation, realized linear windows, and the zero-end system

27 September 2026. This is a mathematical continuation of
[the linear-cost proof](20260927_mixed_current_and_signed_cores.md),
not a new export or a replacement for the inherited manuscripts.
The beta=2 refined Hessian theorem is the analytic premise of Part I.
Part II continues the actual zero-Weyl equations and proves geometric
endpoint exclusions under their stated hypotheses. The unrestricted
integral-error endpoint gap remains open.

Throughout, manifolds are closed, connected, oriented, smooth and
four-dimensional unless a local limit is explicitly specified. Curvature
norms and actual conformal monopole solvability have exactly the conventions
of the [functional pencil](../mathematics/current/line1_functional_pencil.md).
In particular, one genuine Spin^c structure is fixed while the metric varies
within its conformal class. A different original metric may select a different
structure. Constants are universal unless a dependence is displayed.

## Part I. Removing scalar variance and enlarging the actual energy window

### 1. A scale-invariant scalar-slack theorem

For one such actual structure, put

\[
\begin{gathered}
 p=(a_g^+)^2>0,\quad T=2\chi+3\tau,\quad
 P=\int|\operatorname{Ric}^{\circ}|^2,\quad S_2=\int s^2,\\
 D=\frac32S_2+18\int|W^+|^2-72\pi^2p,\quad
 \Sigma=S_2-32\pi^2p,\quad Y=(T-a^2)_+,\quad \Pi=P+D.
\end{gathered}                                                     \tag{1.1}
\]

The actual scalar and functional inequalities give Sigma,D>=0.

**Theorem 1.** For every such metric, with no small-error condition,

\[
 \boxed{\Sigma\le C\bigl(\Pi+\sqrt{\Pi Y}\bigr),\qquad
 (p-T)_+\le C_T\bigl(\Pi+\sqrt{\Pi Y}\bigr).}             \tag{1.2}
\]

In particular, when a^2>=T,

\[
 \boxed{\Sigma\le C(P+D),\qquad (p-T)_+\le C_T(P+D).}     \tag{1.3}
\]

There is no scalar-variance term, normalized target Ricci error, diameter,
Sobolev constant or noncollapse assumption in (1.2).

**Proof.** The positive actual projection excludes a nonnegative constant
scalar-curvature representative: the unperturbed spinor Weitzenboeck formula
would force the spinor and the self-dual determinant curvature to vanish,
contradicting p>0. The Yamabe representative in [g] therefore has negative
constant scalar curvature. Rescale it to obtain s_hat=-4, and denote it by
g_hat. The same actual structure remains available throughout this conformal
class. Hodge star on two-forms is conformally invariant, so p is unchanged.
Class squares and Y are unchanged as well.

For clarity, the conformal energy comparison is exact, not a claim that the
conformal factor is small. Write g=u^2 g_hat and use Delta=d*d. The scalar
transformation law gives s_g u^3=6 Delta_hat u-4u. Squaring and integrating,
then using int u^{-1}Delta u=-int u^{-2}|du|^2, gives

\[
 \delta:=S_2-\widehat S_2
 =48\int_{\widehat g}u^{-2}|du|^2
       +36\int_{\widehat g}(u^{-1}\Delta u)^2\ge0.        \tag{1.4}
\]

Conformal invariance of the Weyl energy and Chern--Weil give

\[
 P-\widehat P=\delta/12,\quad
 D-\widehat D=3\delta/2,\quad
 \Sigma-\widehat\Sigma=\delta.                          \tag{1.5}
\]

Both hatted energies P_hat,D_hat are nonnegative. On g_hat the normalized
Einstein residual satisfies r_hat V_hat=P_hat. If
(P_hat+D_hat)/V_hat<=1, the refined actual theorem and its square-shortfall
version in Sections 4--5 of the preceding proof give

\[
 \widehat\Sigma\le C_0\left(\widehat\Pi+
                             \sqrt{\widehat\Pi Y}\right).
\]

The selectable smoothing allowance is sent to zero for this fixed metric
and actual structure. If instead Pi_hat>V_hat, the elementary inequality
0<=Sigma_hat=16V_hat-32pi^2p<=16V_hat gives the same estimate with constant
16. Thus it holds in both cases, with C>=max(C_0,16).
Now Pi=Pi_hat+(19/12)delta, and (1.5) immediately transfers the bound to g.
Finally use the exact identity

\[
 36\pi^2(p-T)=\frac92P+\frac98\Sigma-D.                 \tag{1.6}
\]

This proves (1.2). QED.

The conformal identities were already available in
[energy selection, Section 4](../mathematics/current/line1_energy_selection.md)
and [Yamabe normalization, Section 1](../mathematics/current/line1_yamabe_endpoint.md).
The new inference is their combination with the refined beta=2 theorem.
No pointwise Ricci preservation under a conformal change is used or claimed.
Nor does (1.2) transfer the hatted spinor's estimates to a particular weighted
spinor on the original metric: its conclusions are curvature energies.

### 2. An unconditional lower Ricci-energy wall

Assume, for the metric under consideration,

\[
 p\ge A>0,\qquad T=A(1-h),\qquad h>0.
\]

Write

\[
 R=\int|\operatorname{Ric}|^2,\quad
 e=\frac{R}{8\pi^2A},\quad
 \mathcal J=\frac{4P}{R},\quad z=p/A-1\ge0,\quad y=Y/A.
\]

The scalar budget makes R positive. Always 0<=J<=4 and J<=E, where E is
the project's relative Einstein defect. The two exact reductions are

\[
 \frac DA=36\pi^2[e-1-h-2z],\qquad
 \frac PA=2\pi^2e\mathcal J.                           \tag{2.1}
\]

In particular e>=1+h+2z. Theorem 1 now has the following consequence.

**Theorem 2.** If a^2>=T, there is c_0>0, independent of h and e, such that

\[
 \boxed{e(1+\mathcal J/18)
       \ge1+(1+c_0)h+(2+c_0)z.}                       \tag{2.2}
\]

In general there is c_s>0 such that

\[
 \boxed{e(1+\mathcal J/18)
       \ge1+h+2z+c_s\frac{(h+z)^2}{h+z+y}.}            \tag{2.3}
\]

The estimates require no upper energy budget from the other chirality.
In particular every non-Ricci-flat Einstein candidate in the square-controlled
case satisfies e>=1+(1+c_0)h.

**Proof.** In the square-controlled case, (1.3) gives
A(h+z)<=C_T(P+D). Substitute (2.1), and take
c_0=(36pi^2 C_T)^{-1}. For the general case put x=Pi/A and v=h+z.
The inequality v<=C_T(x+sqrt(xy)) implies
x>=c v^2/(v+y): if x>=v this is immediate; otherwise square and use x<v.
Substitution proves (2.3). QED.

For 0<h<=1/3, (2.2) also gives J+(e-1-h)>=c h. Indeed if
e-1-h>=h/2 there is nothing to prove; otherwise e<=3/2 and
e-1-h+J/12>=c_0h. This is a global energy-versus-anisotropy statement,
not merely an exact Einstein inequality.

### 3. A stronger chiral window and the small-h variational problem

Put U=3 min(T_+,T_-)/A. Chern--Weil yields directly

\[
 e(1-\mathcal J)\le U.                                 \tag{3.1}
\]

Unlike the older formula with E, no scalar variance has been discarded here.
Let L_h=1+(1+c_0)h. If U>0, combining (2.2) and (3.1) gives

\[
 \boxed{\mathcal J\ge
       \frac{(L_h-U)_+}{L_h+U/18}.}                    \tag{3.2}
\]

For J<1 this follows by eliminating e. For J>=1 the right side is at most
one, so it remains true. If U<=0, (3.1) itself gives J>=1.
Thus for 0<h<=1/3,

\[
 \mathcal J+(U-1-h)_+\ge c h.                          \tag{3.3}
\]

The analogous square-shortfall result has right side c h^2/(h+y), or
c h/(1+L) when y<=Lh. All statements also hold with E in place of J.

On the already constructed actual small-h family in
[Section 3 of the boundary continuation](20260926_boundary_compatibility.md),
U_j=1+h_j+O(h_j^2), y_j=0. Consequently

\[
 \boxed{c_1h_j\le\inf_g\mathcal J(g)
                  \le\frac{4h_j}{1+h_j}.}              \tag{3.4}
\]

The upper bound uses the previously justified classical shrinking-core
metrics and J<=E. The lower bound applies to every smooth metric.
The linear order is therefore forced by traceless Ricci itself; scalar
variance cannot be the sole payment of the topological cost.

Here is a useful exact variational comparison. From (1.5),

\[
 R-\widehat R=\delta/3,\qquad
 \mathcal J(g)=
 \frac{\mathcal J(\widehat g)\widehat R+\delta/3}
      {\widehat R+\delta/3}.                           \tag{3.5}
\]

Thus J(g) lies between J(g_hat) and 1. Since the normalized negative Yamabe
metric has constant scalar curvature, E(g_hat)=J(g_hat). Whenever J(g)<1,

\[
 \mathcal E(\widehat g)=\mathcal J(\widehat g)
                 \le\mathcal J(g)\le\mathcal E(g).      \tag{3.6}
\]

If the manifold has the stipulated actual supply for every metric and
inf_g J(g)<1, it follows that

\[
                    \inf_g\mathcal E(g)=\inf_g\mathcal J(g).
                                                               \tag{3.7}
\]

This applies to the small-h family for all sufficiently large j. It concerns
infima, not attainment, pointwise closeness, or uniqueness of Einstein metrics.

#### 3.1 Conformal minimization and minimizing sequences

The comparison can be sharpened without further analytic input. Fix a negative
conformal class, and put J_Y=J(g_hat), R_Y=R(g_hat). Formula (3.5) shows

\[
             \inf_{g\in[g_0]}\mathcal J(g)=\min\{J_Y,1\}.
                                                               \tag{3.8}
\]

To justify the possibly unattained endpoint 1, choose a coordinate ball and
a compactly supported smooth cutoff chi which is one on a smaller ball.
For fixed sufficiently small epsilon>0 let
u_n=1+epsilon chi sin(nx^1). These are uniformly positive, bounded conformal
factors. The n^2 term in Delta_hat u_n has nonzero squared integral of order
n^4 on the smaller ball, while the lower-order terms are O(n); hence the
nonnegative expression (1.4) tends to infinity. Formula (3.5) tends to 1.
If J_Y<1, (3.8) is attained exactly by constant conformal rescalings of the
Yamabe metric. If J_Y=1, every metric in the class has J=1. If J_Y>1,
the infimum 1 is not attained.

If every conformal class on M is negative (as follows from the all-metric
actual positive supply), write alpha=inf_g E(g). Since J<=E, while (3.6)
would produce an E-value below alpha from any J-value below min(alpha,1),

\[
                 \boxed{\inf_g\mathcal J(g)=\min\{1,\alpha\}.}
                                                               \tag{3.9}
\]

When alpha<1 there is an exact useful excess decomposition. Define
L_s=int(s-s_bar)^2 and delta=S_2-S_Y. Since E=(4P+L_s)/R and
E(g_hat)=J_Y>=alpha, (3.5) gives

\[
 \boxed{\mathcal E(g)-\alpha=
   \frac{R_Y}{R}(J_Y-\alpha)
   +(1-\alpha)\frac{\delta}{3R}+\frac{L_s}{R}.}          \tag{3.10}
\]

Every summand is nonnegative. In particular
delta/R<=3(E-alpha)/(1-alpha) and L_s/R<=E-alpha.
Every E-minimizing sequence therefore has delta/R->0, R_Y/R->1, and
J_Y->alpha. Its late terms may be replaced by their scalar-normalized Yamabe
metrics with no larger E. This reduces the low-defect variational problem
to constant-scalar metrics and controls the conformal energy discarded in
the reduction. It does not supply convergence of conformal factors, geometric
compactness, or attainment of the infimum.

#### 3.2 The remaining sharp coefficient is a specific remainder problem

For the realized family with U=1+h+O(h^2), h->0, the upper bound tends
to zero. The preceding reduction therefore permits restricting the
variational infimum to the actual scalar -4 Yamabe representatives. Put

\[
 x=\frac{P}{8\pi^2A},\quad d=\frac{D}{36\pi^2A},\quad
 \sigma=\frac{\Sigma}{32\pi^2A},\quad z=p/A-1.
\]

All are nonnegative, and exact identities give

\[
\begin{gathered}
 e=1+h+2z+d,\qquad V/(2\pi^2 A)=1+z+\sigma,\\
 x=h+z+d-\sigma,\qquad
 \mathcal E=\mathcal J=\frac{4(h+z+d-\sigma)}{1+h+2z+d},\\
                 d+2z\le4x+(U-1-h).
\end{gathered}                                                     \tag{3.11}
\]

The minimization is over triples realized by these actual metrics and
classes, not arbitrary nonnegative numbers satisfying (3.11).

For the same class take an actual ordinary solution with weight one.
This is available for the present actual family. It is a separately
supplied solution, not the variable-weight spinor silently rescaled.
Write rho=|Phi|^2, K=int|nabla_A Phi|^2,
Q=int(4-rho)^2, and J_+=||F_A^+-(F_A^+)_H||_2^2.
The maximum principle gives rho<=4, and the same-solution identities give

\[
 4K=\int(4-\rho)\rho,\quad
 \int\rho^2=32\pi^2p+8J_+,\quad
 \boxed{\Sigma=8K+Q+8J_+.}                             \tag{3.12}
\]

The last formula is the ordinary-weight specialization of the
[actual remainder identity](20260926_actual_topological_cost.md), not a
new gauge estimate. It holds for every such solution, so changing the
solution does not alter the sum of these three losses.

Along any actual candidate sequence with E=O(h), (3.1) and
e>=1+h+2z+d imply e=1+O(h). Thus x,z,d,sigma=O(h), and (3.11) gives
E/h=4-4(sigma-z-d)/h+O(h). Consequently

\[
 \boxed{\liminf\frac{\mathcal E}{h}\ge4
 \quad\Longleftrightarrow\quad
 \frac{[K+Q/8+J_+-D/9-4\pi^2(p-A)]_+}{Ah}\longrightarrow0.}
                                                               \tag{3.13}
\]

Equivalently, the still-unproved first-order estimate is

\[
                 \Sigma\le\frac89D+32\pi^2(p-A)+o(Ah)
                                                               \tag{3.14}
\]

on these candidate sequences. Obtaining it for all such sequences would
determine coefficient4, in view of the known upper construction. It is
not asserted for arbitrary manifolds or as a consequence of Theorem 1.
On a sharp minimizing sequence it asks for sigma=z+d+o(h), not for
each slack separately to vanish. Controlling K alone loses the other
two nonnegative terms in (3.12).

There is an actual obstruction to reaching this coefficient merely by
optimizing C_T in (1.3). Take a product of closed surfaces of genera
g_1,g_2>=2, with Gaussian curvatures -(1+t), -(1-t), 0<t<1. Set
A_0=T=8(g_1-1)(g_2-1). The product is a negative Yamabe cscK metric
with s=-4 and actual canonical input. Direct product calculations give

\[
 p=\frac{A_0}{1-t^2},\quad
 P=\frac{8\pi^2 A_0t^2}{1-t^2},\qquad D=\Sigma=0.
                                                               \tag{3.15}
\]

The canonical ordinary solution is parallel with rho=4, so K=Q=J_+=0.
Thus p-T=P/(8pi^2), forcing C_T>=1/(8pi^2) and c_0<=2/9.
The slope certified by (3.2) when U=1+h+O(h^2) is 18c_0/19,
at most 4/19. Improving that isotropic constant alone cannot yield 4.
This product test has h=0 for the common budget A=A_0; it is not a
counterexample in the tight small-h window or to (3.14).

Finally Yamabe replacement does not improve the known classical upper
coefficient. For each fixed surgery manifold it decreases Ricci energy,
while LeBrun's absolute lower bound prevents it falling below the same
infimum. Hence e->1+h, and (2.1) forces z,d->0. The classical completed
square bound Sigma<=4D/9+(4sqrt(2)/3)sqrt(RD) then gives Sigma->0.
A sufficiently accurate diagonal sequence has z,d,sigma=o(h), still
yielding E/h->4. The unresolved improvement must therefore control the
actual combined remainder in (3.13), not merely discard scalar variance.

### 4. A realized BF family outside the old quadratic strip

This application changes the region actually excluded by the project. It is
not a claim that these smooth manifolds have never been obstructed elsewhere.
The actual class supply and symplectic geography are classical; their precise
versions are recorded in
[the existing BF geography proof](../mathematics/current/line1_bauer_furuta_geography.md).
See also [Ishida--LeBrun](https://arxiv.org/html/math/0111228) and
[Braungardt--Kotschick, Theorem 4](https://arxiv.org/pdf/math/0306021).

Fix theta=min(c_0/2,1/2)>0 and eta_j=1/j. For sufficiently large j choose an
even integer N_j, increasing as fast as necessary, with N_j>=j^6 and
N_j>=2c(eta_j^2/2)/eta_j^2, where c(epsilon) is the geography constant.
Set

\[
 d_j=\lceil\eta_j^2N_j\rceil,\quad a_j=9N_j-d_j,
 \quad A_j=2a_j.
\]

The geography theorem supplies a simply connected minimal symplectic X_j
with chi_h(X_j)=N_j and c_1^2(X_j)=a_j: indeed
a_j<=(9-eta_j^2/2)N_j-c(eta_j^2/2). Choose N_j additionally large enough
for the theorem's lattice-range condition. Its invariants are

\[
 \chi(X_j)=3N_j+d_j,\quad \tau(X_j)=N_j-d_j,\quad
 b_+(X_j)=2N_j-1\equiv3\pmod4,\quad b_-(X_j)=N_j+d_j-1.
\]

For the pair of building blocks define

\[
 u_j=3-18\frac{2\tau(X_j)}{A_j}
     =1+\frac{16d_j}{a_j}=1+O(\eta_j^2),\qquad
 U_j^*=1+(1+\theta)\eta_j,
\]
\[
 x_j=\frac{U_j^*-u_j+3\eta_j}{18},\qquad
 y_j=\frac{\eta_j-x_j}{4}.
\]

They are positive for large j, with
x_j/eta_j->(4+theta)/18 and y_j/eta_j->(14-theta)/72.
Take even surgery counts

\[
 k_j=2\lfloor A_jx_j/2\rfloor,\qquad
 m_j=2\lfloor A_jy_j/2\rfloor-4,
\]

and form the actual smooth manifold

\[
 M_j=X_j\#X_j\#k_j\overline{\mathbb {CP}}^{\,2}
                         \#m_j(S^1\times S^3).         \tag{4.1}
\]

**Theorem 3.** On this family, for all sufficiently large j,

\[
 \inf_g\mathcal J(g)\ge c_2h_j>0,\qquad
 U_j-F(h_j)\sim\theta h_j,
 \qquad h_j\longrightarrow0,                           \tag{4.2}
\]

where h_j=(4+k_j+4m_j)/A_j and
F(h)=(4-sqrt(1-3h))^2/9. The manifolds have no Einstein metric of any sign,
ordinary SW invariants vanish, and neither orientation admits an almost-complex
structure. Both strict Hitchin--Thorpe inequalities hold.

**Proof.** Write k_j=A_jx_j-alpha_j and
m_j=A_jy_j-beta_j-4 with alpha_j,beta_j in [0,2). The exact topology gives

\[
 h_j=\eta_j-\frac{12+\alpha_j+4\beta_j}{A_j},\qquad
 U_j=U_j^*+\frac{36-15\alpha_j+12\beta_j}{A_j}.          \tag{4.3}
\]

Here the signature is positive for large j, so the smaller chirality really
is T_-. In particular T_+>0 and T_->0. The correction in U is positive and
O(A_j^{-1}); the correction in h is negative and O(A_j^{-1}). Since
A_j^{-1}=o(eta_j^2), and F(h)=1+h+h^2+O(h^3),

\[
 U_j-F(h_j)=\theta\eta_j+O(\eta_j^2),\qquad
 L_{h_j}-U_j=(c_0-\theta)\eta_j+o(\eta_j).              \tag{4.4}
\]

BF nonvanishing supplies the actual canonical-sum and exceptional-sign
structures. For the four-input formulation of Ishida--LeBrun's theorem,
one may add auxiliary X_3=X_4=K3: the total b_+ is 4N_j+4, congruent to
4 modulo 8, and the theorem's m=2 conclusion concerns just the two target
summands. The auxiliary K3 surfaces are not included in M_j.
As in the existing proof, averaging the independent exceptional
signs selects, for every metric, an actual class with p>=A_j and
a^2=A_j-k_j>=T_+=A_j-4-k_j-4m_j. Thus (3.2) applies and proves the first
claim in (4.2). Nonzero Einstein constants have J=0; Ricci-flatness is also
excluded directly by the positive actual scalar budget.

Finally,
b_1(M_j)=m_j,
b_+(M_j)=4N_j-2, and b_-(M_j)=2N_j+2d_j-2+k_j are all even.
An almost-complex four-manifold has (chi+tau)/4=(1-b_1+b_+)/2 integral,
which is impossible here, in either orientation. Ordinary SW vanishing
follows from the positive-b_+ connected-sum decomposition. Increasing N_j
ensures distinct b_+ and hence pairwise nonhomeomorphism.
QED.

This is outside the old *quantitative* strip: (U_j-F(h_j))/h_j^2->infinity,
so the old inequality E+(U-F(h))_+>=c_old h^2 does not by itself give a
positive E on this family. The classical optimized energy interval also
allows e between F(h_j) and U_j. The new linear wall excludes it. The old
near-1/3 estimate does not apply effectively as h_j->0, and the old upper
wall concerned h>1/4. No assertion of an upper near-Einstein construction
on these symplectic BF manifolds is made.

### 5. Cover-compatible inputs are retained, not strengthened

The preceding arguments extend to the invariant-weight version of the actual
input in [the Pin-minus proof](../mathematics/current/round14_twisted_rigidity.md).
Suppose pi:M_tilde->M is a finite regular oriented cover, g_tilde=pi^*g,
and one ordinary structure upstairs supplies every positive deck-invariant
weight required by the proof. The beta=2 refined argument only uses these
weights and therefore holds upstairs without requiring all other weights.

The normalized negative Yamabe representative upstairs is deck-invariant
by uniqueness of the scalar -4 representative in a negative conformal class.
It descends to M. Every further auxiliary weight used on that representative
is still deck-invariant, so the same actual supply remains valid. Apply
Theorems 1--2 upstairs, divide the extensive energies and topology by the
covering degree, and keep the normalized quantities e,J,E unchanged.
The square-shortfall term divides correctly:
sqrt(Pi_tilde Y_tilde)/degree=sqrt(Pi_per_sheet Y_per_sheet).
There is no degree-dependent loss.

For a genuine Pin-minus double-cover input, the inherited lifting theorem
gives p_tilde=2p, a_tilde^2=2a^2 and T_tilde=2T, so all statements above
apply to the twisted budgets downstairs. This is the actual lifting input of
[Ishida--Matsuo--Nakamura](https://arxiv.org/pdf/1505.05948), not a claim
that an arbitrary formal local-system class has solutions. The conclusion
does not require the covering manifold to solve arbitrary non-invariant
weights or metrics.

## Part II. The remaining zero-Weyl endpoint

The following continuation uses the actual torsion system and length estimates
in Section 8 of the preceding proof. Unlike Part I, it has not yet produced
a universal zero-end gap. Further results are recorded below as their proofs
close, without turning them into an export or a completion claim.

### 6. Saturation of determinant curvature, not just torsion length

Use the actual fields and notation of the preceding proof, Section 8:
P_spin=nabla_A Phi, rho=|Phi|^2, zeta=<Phi,P_spin>, t=t_Phi,
m=|t|^2, eta=kappa+epsilon, beta>=4, and a^2>=T_+.
Set rho_beta=2sqrt(4(1+1/beta))/3,
U_beta=(4/3)(2/beta-1), m_beta=-U_beta rho_beta^3/2, and
S=m_beta+2rho^2|P_spin|^2. All norms in this section are normalized by V.
The quadratic map q_- obeys |q_-(t)|^2=m^2/8. Define bounded smooth fields

\[
 Q=\frac{\rho^3q_-(t)}S,\qquad
 A_\beta=\frac{4m_\beta}{\rho_\beta^6}Q.                \tag{6.1}
\]

There is no division by rho or m. S has a universal positive lower bound.

**Theorem 4.** Under these actual hypotheses,

\[
 \boxed{\|F_A^-+A_\beta\|_{2,\mathrm{avg}}^2
       +\frac{4\pi^2(a^2-T_+)}V
       \le\frac8{3\beta}(1-2/\beta)+C\sqrt\eta.}       \tag{6.2}
\]

Consequently, along beta->infinity and eta->0,

\[
 \fint|F_A^-|^2\longrightarrow\frac29,
 \qquad (a^2-T_+)/V\longrightarrow0.                   \tag{6.3}
\]

More quantitatively, for any measurable B subset M,

\[
 \fint_B|F_A^-|^2\le
 C\left(\frac{\operatorname{Vol}(B)}V+\beta^{-1}
                                      +\sqrt\eta\right),        \tag{6.4}
\]

where fint_B in (6.4) means V^{-1}int_B, not normalization by Vol(B).
Thus determinant ASD energy cannot concentrate at the normalized volume
scale in the hypothetical endpoint sequence.

**Proof.** Pair the actual curvature equation

\[
 \rho^3F_A^-+2q_-(t)=2\rho^2(d\zeta)^-+\mathcal R
\]

with q_-(t)/S. The derivative test rho^2 q_-(t)/S has bounded normalized
L2 derivative by (8.10) of the preceding proof. Integration by parts against
zeta therefore costs O(sqrt eta), and the remainder costs the same. Hence

\[
 \fint\langle F_A^-,Q\rangle
     =-\fint\frac{m^2}{4S}+O(\sqrt\eta)
     =-m_\beta/8+O(\sqrt\eta).                         \tag{6.5}
\]

The reciprocal scalar test also implies

\[
 \fint |Q|^2=\rho_\beta^6/32+O(\sqrt\eta).             \tag{6.6}
\]

For the error rate, write S=m_beta+m+d, avg d=O(eta). The Jensen defect
avg[(S-2m_beta)^2/S]=O(sqrt eta), together with S>=m_beta, controls
avg(1/S-1/(2m_beta))^2 by O(sqrt eta). It follows that
avg(m/S)^2=1/4+O(sqrt eta): here one also uses the independently proved
mean identity avg(1/S)=1/(2m_beta)+O(sqrt eta), and avg(d/S)=O(eta).
The squared fluctuation alone would not give this error rate.
Replacing rho^6 by rho_beta^6 is legitimate
because m/S<=1 and rho is bounded with small L2 amplitude error. This proves
(6.6), not merely convergence without a rate.

The actual positive-curvature fit and Chern--Weil give

\[
 \fint|F_A^+|^2=\frac89(1+1/\beta)^2+O(\sqrt\eta),
\]
\[
 \frac{4\pi^2T_+}V=\frac23+\frac{16}{3\beta^2}
                                         +O(\sqrt\eta).
\]

Using int(|F_A^+|^2-|F_A^-|^2)=4pi^2a^2 yields the exact upper-budget
expansion

\[
 \fint|F_A^-|^2+\frac{4\pi^2(a^2-T_+)}V
 =\frac{2+16/\beta-40/\beta^2}{9}+O(\sqrt\eta).          \tag{6.7}
\]

Completing the square with (6.5)--(6.6) subtracts
m_beta^2/(2rho_beta^6)=2(1-2/beta)^2/9. The difference is exactly
8(1-2/beta)/(3beta), proving (6.2). The square term and the class-square
term are both nonnegative. Since A_beta is uniformly bounded, (6.4) follows
by the elementary squared triangle inequality. Its total norm and (6.2)
give (6.3). QED.

For a sequence with bounded total volume, the nonnegative integer
(a^2-T_+)/4=c_2(S^+)[M] must eventually be zero. This does not make the
particular spinor section zero-free. With unbounded volume, (6.2) gives
a density conclusion only; individual bubbles can still carry finite energy.

### 7. Opposite-Weyl bulk cancels, leaving compulsory signed transition flux

Let E_-=S^- tensor L, whose determinant connection is 3A. Its signed density is

\[
 16\pi^2c_2(E_-)=\bigl(2|W^-|^2+k\bigr)d\mu,
\quad k=9(|F_A^+|^2-|F_A^-|^2)+s^2/24
                                      -|\operatorname{Ric}^{\circ}|^2/2.
                                                               \tag{7.1}
\]

Choose a smooth theta(m) equal to zero for m<=m_beta/16 and one for
m>=m_beta/8, with uniformly bounded derivative, and put chi=1-theta^2.
Let T_beta={m_beta/16<m<m_beta/8}. The actual torsion-length theorem gives
Vol{chi!=0}/V<=C sqrt eta. By Theorem 4 and the other bounded-model fits,

\[
 \fint k=20/3+O(\beta^{-1}+\sqrt\eta),\qquad
 V^{-1}\int\chi|k|\le C(\beta^{-1}+\sqrt\eta).          \tag{7.2}
\]

On {t!=0}, let T_t be the rank-two Chern transgression for t/|t|, using the
same normalization as Section 1 of the preceding proof. Since chi=1 near
every zero, its localization is globally legitimate:

\[
 \boxed{2\int\theta^2|W^-|^2+\int\theta^2 k
                  =16\pi^2\int d\chi\wedge T_t.}       \tag{7.3}
\]

In particular, even an arbitrarily large positive W^- bulk charge in the
small-torsion region is not an independent payment of the obstruction:
the identical term occurs in the global characteristic number and cancels
from (7.3). The right side must supply a positive signed flux of order V.

**Theorem 5.** With xi=<t,nabla t>, the actual endpoint fields satisfy

\[
 \boxed{C V^{-1}\int_{T_\beta}|\xi|^2|\nabla t|^2
    \ge\frac{20}{3}-C(\beta^{-1}+\sqrt\eta)
                          +V^{-1}\int\theta^2|W^-|^2.}          \tag{7.4}
\]

Thus a hypothetical zero-end sequence necessarily has
V^{-1}int_{T_beta}|<t,nabla t>|^2|nabla t|^2>=c>0 on regions of vanishing
relative volume. No upper bound for W^- is required for this statement.

**Proof.** In the unit t-frame write the connection as
[[alpha,-bar b],[b,d]]. On T_beta its amplitude is bounded above and away
from zero, so |alpha|<=C|xi|, |b|<=C|nabla t|, and |dm|<=2|xi|.
The transgression is

\[
 4\pi^2T_t=-\alpha\wedge F_{22}
   +\tfrac12(b\wedge F_{12}-\bar b\wedge F_{21})
   +\alpha\wedge\bar b\wedge b.
\]

Moreover |chi'|<=C theta. The curvature of E_- is bounded algebraically
by C(|W^-|+|s|+|Ric^circ|+|F_A|). Young's inequality therefore gives,
for any fixed epsilon_1>0,

\[
\begin{split}
16\pi^2\left|\int d\chi\wedge T_t\right|
 \le{}&\epsilon_1\int\theta^2|W^-|^2
       +C_{\epsilon_1}\int_{T_\beta}|\xi|^2|\nabla t|^2\\
      &+C_{\epsilon_1}\int_{T_\beta}
              (s^2+|\operatorname{Ric}^{\circ}|^2+|F_A|^2).
\end{split}                                                     \tag{7.5}
\]

For example the W^- term is bounded by C theta |W^-||xi||nabla t|;
the cubic connection term by C theta |xi|^2|nabla t|^2. All other curvature
terms use the same Young inequality without needing an absorption sign.
The last line is O((beta^{-1}+sqrt eta)V), by (6.4), the positive-curvature
and scalar fits, and the small volume of T_beta. Take epsilon_1=1 in (7.5),
use (7.2)--(7.3), and rearrange. QED.

This also forces int_{T_beta}|nabla t|^4>=cV and
sup_{T_beta}|nabla t|>=c eta^{-1/8} along a zero-end sequence.
It does not prove the needed mixed energy is uniformly integrable.
Uniform integrability of this particular transition density would suffice
to exclude the endpoint; it is not an added premise in any earlier theorem.

### 8. A local compatibility gap and collapse in measure

This section gives an independent geometric consequence with a bounded-Ricci
hypothesis. It does not replace the no-compactness, integral-Ricci endpoint
question. The two classical inputs are the local harmonic-radius estimate
of [Cheeger--Naber, Theorem 1.13 and Definition 2.9](https://arxiv.org/pdf/1406.6534),
and the local nonexistence of negative Einstein ASD almost-Kaehler metrics
in [Armstrong, Theorem 3.3.5](https://johnarmstrongmaths.com/publications/resources/thesis.pdf).
The proof below connects them to the actual approximate-form supply.

Fix K,L,v>0. Let g be a complete oriented four-metric with |Ric|<=K,
let omega be a smooth self-dual two-form with |omega|<=L, and let the
constant parameter t belong to [0,1/4]. Define

\[
 Z_t=|\operatorname{Ric}+g|^2+
 |W^+-t(|\omega|^2I/3-\omega\otimes\omega)|^2
                  +( |\omega|^2-2)^2+|d\omega|^2.       \tag{8.1}
\]

**Theorem 6 (local coercivity).** There is epsilon(K,L,v)>0 such that

\[
       \operatorname{Vol}B_1(x)\ge v
            \quad\Longrightarrow\quad
       \int_{B_2(x)}Z_t\ge\epsilon(K,L,v).             \tag{8.2}
\]

**Proof.** Otherwise take a sequence whose local integral tends to zero.
Volume comparison gives a fixed lower volume for B_{1/2}(x). The local
harmonic-radius estimate supplies a point in B_{1/2}(x) with harmonic radius
at least r_0(K,v)>0. In a fixed-size chart compactly contained in B_1(x),
the metrics have uniform C^{1,alpha} and W^{2,p} bounds for each finite p.
Pass on smaller charts to C^{1,alpha'} and weak W^{2,p} convergence.

The local L2 Ricci residual tends to zero. Its pointwise norm is bounded by
K+2, so interpolation gives convergence to zero in every finite Lp. The
harmonic-coordinate metric equation shows the limit is a weak Einstein
metric with Ric=-g, hence smooth. Subtracting that equation from the
sequence and using interior elliptic estimates improves the metric
convergence to strong W^{2,p} on smaller charts. In particular the Weyl
operators converge strongly in L2. No Ricci derivative bound is assumed.

Self-duality gives |delta_g omega|=|d omega|. Interior estimates for d+delta
in the uniformly C1-controlled charts give a uniform H1 bound for omega;
Rellich compactness gives strong L2 convergence on a smaller ball. The
limit is weakly closed and coclosed, hence smooth, self-dual, and of squared
length two. Bounded amplitude also makes its polynomial model converge
strongly in L2. Passing to a subsequence t->t_infinity yields

\[
 \operatorname{Ric}=-g,\quad d\omega=0,\quad |\omega|^2=2,
 \quad W^+=t_\infty(2I/3-\omega\otimes\omega).          \tag{8.3}
\]

If t_infinity=0 this is the locally forbidden ASD Einstein almost-Kaehler
system. If t_infinity>0, the Einstein Bianchi identity gives div W^+=0.
Differentiating (8.3), using constant length and delta omega=0, gives
omega_{ij}nabla^i omega_{kl}=0. The two-form is nondegenerate, so
nabla omega=0. The two-form Weitzenboeck equation now implies
W^+omega=(s/6)omega=-(2/3)omega. But (8.3) gives
W^+omega=-(4t_infinity/3)omega, forcing t_infinity=1/2,
outside [0,1/4]. Both cases contradict existence of the limit. QED.

**Corollary 7 (collapse in measure).** On a closed manifold put
S_v={x:Vol B_1(x)>=v}. Then

\[
 \boxed{\frac{\operatorname{Vol}(S_v)}V
       \le C(K,L,v)\fint Z_t.}                        \tag{8.4}
\]

Indeed integrate (8.2) over S_v. Fubini and the Bishop upper bound b_K(2)
for a radius-two ball give

\[
 \epsilon\operatorname{Vol}(S_v)
 \le\int_M Z_t(y)\operatorname{Vol}(S_v\cap B_2(y))d\mu(y)
 \le b_K(2)\int_M Z_t.
\]

There is no packing multiplicity, total-volume upper bound or diameter
assumption. In particular, for the actual supplier, beta>=4, p>0, and
|Ric|<=K, its SAME bounded near-closed form has L=3sqrt2,
t=1/beta and avg Z_t<=C(r+D_beta/V)+o(1). Sending the selectable allowance
to zero yields

\[
 \boxed{\frac{\operatorname{Vol}\{x:\operatorname{Vol}B_1(x)\ge v\}}V
       \le C(K,v)(r+D_\beta/V).}                      \tag{8.5}
\]

No class-square or Hessian budget is needed for (8.5). Hence any bounded-Ricci
sequence with actual compactified-pencil defect tending to zero must collapse
in measure at unit scale, for every fixed v>0. A single noncollapsed point
is not excluded when total volume tends to infinity; the assertion concerns
its volume fraction. Uniform unit-ball noncollapse, or a fixed positive
fraction of noncollapsed points, gives a uniform defect gap.

### 9. A diameter consequence for the original pointwise Ricci input

Let delta=||Ric^sharp+I||_{infinity,op}, diam(g)<=D, and suppose the actual
class has p>0 and a^2>=T_+. There is epsilon(D)>0 such that

\[
                  \boxed{\delta^2+D_\beta/V\ge\epsilon(D),
                              \qquad\beta\ge4.}       \tag{9.1}
\]

To prove this it suffices to consider delta<=1/4. Then
|Ric|<=5/2, r<=4delta^2, and Chern--Weil gives

\[
 T_+\ge\frac{V}{4\pi^2}
       \left[\frac23(1-\delta)^2-2\delta^2\right]
       \ge V/(16\pi^2)>0.
\]

Integrality gives T_+>=1, hence a^2>=1 and p>=1. The actual scalar bound
and |s|<=4(1+delta) give V>=2pi^2/(1+delta)^2. Ricci lower bound and bounded
diameter then imply Vol B_1(x)>=v(D)>0 at every x. Apply (8.5), and absorb
the remaining delta>=1/4 case by decreasing epsilon(D) below 1/16.

Alternatively, replace the square condition by an explicit p>=A_0>0;
the same proof gives epsilon(D,A_0). It is the noncollapse produced by these
inputs that matters. The result excludes actual near-saturation in this
range; it neither constructs Einstein metrics nor proves the unrestricted
integral endpoint gap. It does not assume asphericity, vanishing pi_2,
bilateral saturation, or an opposite-Weyl energy bound.

### 10. A nonvanishing upper-energy margin at the zero-Weyl corner

Consider an exact metric Ric=-g satisfying the actual hypotheses of Section 9,
with diam(g)<=D. Put T_+=A(1-h), p>=A>0 and e=R/(8pi^2 A).
Then V=2pi^2 A e. Write z=p/A>=1 and d=3(1-h)-e>=0; the last inequality
is the positive-chirality Chern--Weil identity. Direct substitution gives

\[
 \frac{D_\beta}{V}=16+\frac{16}{\beta}-\frac{36z}{e}
                         +\frac{2(\beta+1)d}{e}.       \tag{10.1}
\]

Let epsilon=epsilon(D) in (9.1), decreased to at most one. Set

\[
 \beta_0=32/\epsilon,\quad a_0=\epsilon-16/\beta_0=\epsilon/2,
 \quad H=2(\beta_0-7)+a_0,\quad
 \gamma=\frac{9a_0}{4H}>0.
\]

**Corollary 8.** All these exact candidates obey

\[
 \boxed{e\le U_D(h):=
       \frac{6(\beta_0+1)(1-h)-36}{H}
       =\frac94-\gamma-
          \frac{6(\beta_0+1)}H(h-\tfrac14).}           \tag{10.2}
\]

Indeed D_beta0/V>=epsilon by (9.1); use z>=1 in (10.1), multiply by e,
substitute d, and rearrange. H is positive. In particular h>=1/4 forces
e<=9/4-gamma. Let

\[
 G(h)=\frac{(4+\sqrt{1-3h})^2}{9},\qquad
 \eta_D=\min\{1/24,\gamma/10\}.
\]

Since G(1/4)=9/4 and |G'|<=5 on [1/4,7/24], (10.2) gives

\[
 \boxed{e\le G(h)-\gamma/2,
              \qquad 1/4\le h\le1/4+\eta_D.}          \tag{10.3}
\]

The positive margin does not vanish as h approaches 1/4. It depends on D;
it is not an all-diameter improvement of the earlier upper envelope.
The alternative p>=A_0 hypothesis gives the corresponding D,A_0 dependence.

There is also a diameter-free conclusion about any hypothetical sequence
at this corner. Suppose exact negative Einstein metrics with actual p_j>=A_j
satisfy h_j->1/4 and e_j->9/4. Then d_j->0. Choose beta_j->infinity so
slowly that beta_j d_j->0. Equation (10.1), z_j>=1, and D_beta>=0 imply
D_beta_j/V_j->0. Applying (8.5) proves, for every fixed v>0,

\[
 \frac{\operatorname{Vol}\{x:\operatorname{Vol}B_1(x)\ge v\}}{V_j}
                        \longrightarrow0.            \tag{10.4}
\]

Thus approaching this energy corner would force collapse in measure, not
merely unbounded diameter. This is a necessary degeneration statement,
not the construction of a sequence realizing the corner.

### 11. Local exponential averaging: excluding bounded-curvature collapse

The collapse conclusion in Section 8 need not be the endpoint. A second
averaging argument removes the noncollapse condition when sectional
curvature is bounded. Crucially, it does not assume that an exponential
chart is a regular covering or has uniformly bounded multiplicity.

Fix K,L>0 and a radius r_0>0 with
4r_0<pi/(2sqrt(max(K,1))). On a closed oriented four-manifold let omega
and t satisfy the field conditions of (8.1). Define the curvature-regular
set

\[
 G_{K,r_0}=\{x: |\sec_g|\le K\text{ on }B_{4r_0}(x)\}.
\]

**Theorem 9.** Without any curvature assumption outside these balls,

\[
 \boxed{\frac{\operatorname{Vol}(G_{K,r_0})}{V}
                   \le C(K,L,r_0)\fint Z_t.}           \tag{11.1}
\]

In particular, if |sec|<=K globally then avg Z_t>=c(K,L)>0. For the
actual conformal monopole supplier with p>0, this yields

\[
 \boxed{r_{\rm Ric}+D_\beta/V\ge c(K)>0,
                 \qquad |\sec|\le K,\quad\beta\ge4.}  \tag{11.2}
\]

There is no diameter, injectivity-radius, volume or class-square condition
in (11.2). The extra curvature hypothesis is explicit; (11.2) does not
replace the unrestricted integral-Ricci problem.

**Proof.** For x in G, pull back the metric and form by exp_x to the tangent
ball of radius 4r_0. The map is nonsingular by the conjugate-radius estimate.
The pullback metric has controlled sectional curvature and interior
injectivity, hence a fixed-size harmonic chart on a smaller ball. These
normal-cover facts require no curvature derivatives or injectivity on M;
one precise formulation is
[Deleporte--Lagace--Rouveyrol, Proposition 2.6](https://arxiv.org/html/2601.16176v1#S2.SS3).
Its proof is local, so bounds on B_{4r_0}(x) suffice.

The contradiction proof of Theorem 6 on such a chart, with fixed r_0,
gives epsilon_loc(K,L,r_0)>0 such that

\[
 E_{r_0}(x):=\int_{|v|<r_0\subset T_xM}
                Z_t(\exp_xv)\,d\mu_{\exp_x^*g}(v)
                              \ge\epsilon_{\rm loc}. \tag{11.3}
\]

This uses the exact same lifted self-dual form. If (11.3) failed, the
interior harmonic chart would give the forbidden smooth system (8.3).
The local cover is used only for that compactness argument, not to impose
any new gauge solvability assumption.

Let J_x(s,theta) be its polar volume density. Rauch comparison gives
J_x(s,theta)<=C(K,r_0)s^3 for 0<s<r_0. Therefore

\[
\begin{split}
 \epsilon_{\rm loc}\operatorname{Vol}(G)
 &\le C(K,r_0)\int_0^{r_0}s^3
          \int_G\int_{S_xM}Z_t(\exp_x(s\theta))d\theta d\mu(x)ds\\
 &\le C(K,r_0)|S^3|\frac{r_0^4}{4}\int_M Z_t.
\end{split}                                                     \tag{11.4}
\]

For the second line first drop the nonnegative center restriction G.
The geodesic flow preserves Liouville measure on the unit tangent bundle,
so for each s the integral over all (x,theta) is |S^3|int_M Z_t.
This identity is valid even when geodesics close or exp_x has many sheets.
It avoids both a false uniform multiplicity bound and any deck-normality
requirement. Equations (11.1)--(11.2) follow, sending the actual supplier's
selectable allowance to zero. QED.

Define the sectional-curvature radius

\[
 r_{\sec}(x)=\sup\{0<r\le1:\sup_{B_r(x)}|\sec|\le r^{-2}\}.
\]

For any fixed a>0 the set {r_sec>=a} is contained in one G_{K,r_0},
with K,r_0 depending only on a; choose a smaller radius if the supremum
is not attained. Consequently an actual sequence with
r_Ric+D_beta/V->0 and beta>=4 satisfies

\[
       \frac{\operatorname{Vol}\{r_{\sec}\ge a\}}V\to0
                                  \quad\text{for every }a>0.    \tag{11.5}
\]

This forces curvature scale to vanish in measure, not merely injectivity
scale. It does not say pointwise curvature tends to infinity everywhere:
a high-curvature set can have large metric neighborhoods. In particular,
the exact energy-corner sequence in (10.4), if it existed, would also
obey (11.5). Section 10's nonvanishing energy-wall margin holds with a
K-dependent constant under |sec|<=K, without its diameter or square
hypothesis, by substituting (11.2) for (9.1).

### 12. Exact Einstein metrics: replacing curvature bounds by Euler density

The preceding argument can be continued once more. For exact Einstein
metrics, the curvature-regular fraction follows from an integral curvature
budget, even when balls collapse. This uses the unnormalized small-energy
theorem of Cheeger--Tian, not a regularity assertion for arbitrary small
Ricci residuals. The theorem is stated explicitly in
[Cheeger's author presentation, pages 2--3](https://sites.duke.edu/scshgap/files/2016/08/dim4dukebeamer.pdf)
of the [2006 paper](https://doi.org/10.1090/S0894-0347-05-00511-4).

Use the Hilbert--Schmidt norm of the full curvature operator R_op on
Lambda^2; fixed norm factors can be absorbed into the classical constants.
For Ric=-g, Chern--Gauss--Bonnet gives

\[
          \int|R_{\rm op}|^2=8\pi^2\chi(M),\qquad
          \Lambda=8\pi^2\chi(M)/V.                    \tag{12.1}
\]

**Theorem 10.** Given Lambda_0,L>0, every closed Ric=-g four-manifold with
Lambda<=Lambda_0, and every bounded self-dual form and t in [0,1/4] as
in (8.1), satisfies

\[
                         \fint Z_t\ge c(\Lambda_0,L)>0.
                                                               \tag{12.2}
\]

For actual conformal monopole input with p>0 this gives

\[
       \boxed{D_\beta/V\ge c(\Lambda_0)>0,
                       \qquad \beta\ge4.}            \tag{12.3}
\]

No diameter, total-volume, noncollapse, derivative, or class-square bound
is imposed. Here the Einstein equation is exact.

**Proof.** Cheeger--Tian supply constants epsilon_CT,C_CT such that for
0<R<=1,

\[
 \int_{B_R(x)}|R_{\rm op}|^2\le\epsilon_{\rm CT}
        \quad\Longrightarrow\quad
 \sup_{B_{R/2}(x)}|R_{\rm op}|\le C_{\rm CT}R^{-2}.    \tag{12.4}
\]

This implication has no lower ball-volume premise. Put
F_R(x)=int_{B_R(x)}|R_op|^2. Bishop comparison for Ric=-g and Fubini give,
with a dimensional B and R<=1,

\[
 \int_M F_R(x)d\mu(x)
 =\int_M|R_{\rm op}(y)|^2\operatorname{Vol}B_R(y)d\mu(y)
                         \le B R^4\Lambda V.          \tag{12.5}
\]

Choose R=min{1,[epsilon_CT/(2B Lambda_0)]^{1/4}}. At least half the volume
then consists of centers with F_R<=epsilon_CT. On each corresponding
B_{R/2} the sectional curvature is bounded by C_CT R^{-2}.
Choose a fixed small theta_0>0, depending only on C_CT, and put
r_0=theta_0 R, K=max(C_CT,1)R^{-2}. Choose theta_0 so that
4r_0<R/2 and 4r_0<pi/(2sqrt(K)). All these centers belong to G_{K,r_0}.
Theorem 9 therefore yields 1/2<=C(K,L,r_0)avg Z_t, proving (12.2).
Apply the same actual form and send its selectable allowance to zero
to obtain (12.3). QED.

The proof also gives, for each fixed 0<R<=1, a useful tradeoff

\[
           1\le C_0\Lambda R^4+C_1(R,L)\fint Z_t.      \tag{12.6}
\]

Indeed the high-energy centers have fraction at most C_0 Lambda R^4,
and all remaining centers are in the curvature-regular set controlled
by Theorem 9. Thus any exact Einstein actual zero-end sequence must have
chi(M_j)/V_j->infinity. Curvature scale tending to zero is not a free
escape at bounded Euler density.

For the topological energy variables, e=V/(2pi^2 A)>=p/A>=1 by the
scalar monopole inequality. Therefore

\[
                   \Lambda=4\frac{\chi/A}{e}.
\]

An independently checkable budget chi/A<=B_0 supplies Lambda<=4B_0.
The energy-wall proof of Section 10 consequently holds with an epsilon
depending only on B_0, and with no diameter assumption. In particular
the corner h->1/4, e->9/4 cannot be approached by these exact candidates.

This budget is automatic in the complex-hyperbolic surgery family:
if X is a closed complex-hyperbolic surface, A=c_1^2(X)=3chi(X), and
M=X#k CPbar^2#ell(S^1 x S^3), then

\[
 \chi(M)/A=1/3+k/A-2\ell/A\le1/3+h,
                    \qquad h=(k+4\ell)/A.             \tag{12.7}
\]

Thus for 1/4<=h<=1/3 the density threshold is uniform over all such actual
inputs, their covers and all normalized exact Einstein candidates.
This excludes an energy region for arbitrary exact outputs on the smooth
types, not just for a chosen gluing family. It does not claim that the
entire remaining energy interval is realizable or that these topologies
are all non-Einstein solely from the upper wall.

### 13. A uniform forbidden band for approximate pointwise inputs

The energy-wall conclusion can be made robust without discarding scalar
variance. In this section retain the bounded-diameter hypotheses of
Section 9, with p>=A>0, T_+=A(1-h), and 1/4<=h<=1/3. Either a^2>=T_+
or the alternative p>=A_0 is required. Let epsilon_* denote the resulting
constant in (9.1), decreased to at most 1/16.

**Theorem 11.** There is c(D)>0 (or c(D,A_0)>0 for the alternative input)
such that

\[
 \boxed{\delta_-^2+(G(h)-e)_+\ge c(D),
                       \qquad 1/4\le h\le1/3.}        \tag{13.1}
\]

One may take c=min{1/64,epsilon_*^2/80000}. In particular this is a
uniform forbidden neighborhood of the zero-Weyl upper-energy corner for
approximately Einstein input metrics, not just for exact outputs.

**Proof.** Put J=4P/R, ell=R/(4V), z=p/A-1>=0, B=3(1-h), and
b=B/e-1+J=12 int|W^+|^2/R>=0. Exact Chern--Weil gives

\[
 \frac{D_\beta}{V}
  =\ell\left[16-4J-\frac{36(1+z)}e+2b+2\beta b
                                      +\frac{16-4J}{\beta}\right].
                                                               \tag{13.2}
\]

The scalar mean and variance are retained through

\[
 \ell=\frac{\bar s^2+L_s/V}{16(1-J/4)}
      =1-\tfrac12\fint(s+4)+\tfrac14r_{\rm Ric}.
\]

Let s_0=(G(h)-e)_+. If delta_->1/8 or s_0>1/16, (13.1) follows
immediately with the stated smaller c. Otherwise

\[
 J\le4\delta_-^2/(1-\delta_-)^2\le4/49,\quad
 247/144\le e\le49/20,\quad
 3/2\le e_0:=e(1-J)\le9/4.
\]

Here the upper bound on e follows from positive-chirality Chern--Weil,
e(1-J)<=B, and G>=16/9 gives its lower bound. Set b_0=B/e_0-1.
Then 0<=b_0<=1/2 and b=(1-J)b_0<=(4-J)/8. Minimizing (13.2) over
beta>=4 is therefore permitted at beta=sqrt(2(4-J)/b); for b=0 take
the limit beta->infinity. The result is ell F_{J,z}, where

\[
 F_{J,z}=16-4J-36(1+z)/e+2b+4\sqrt{2(4-J)b}.
\]

Define, for 3/2<=v<=B,

\[
 F_0(h,v)=16-36/v+2(B/v-1)+8\sqrt{2(B/v-1)}.
\]

Direct expansion yields

\[
 F_{J,0}-F_0(h,e_0)
 =J(-4+36/e_0-2b_0)
       +4\sqrt{2b_0}\,[\sqrt{(4-J)(1-J)}-2]\le20J.    \tag{13.3}
\]

Also vF_0=[4sqrt(v)+sqrt(2(B-v))]^2-36. Its upper zero is G(h),
F_0<=0 for v>=G(h), and elementary square-root comparison gives
F_0(h,v)<=30sqrt((G(h)-v)_+) on the displayed compact v-range.
Since (G-e_0)_+<=s_0+(49/20)J, ell<=81/64, ell/e>=5/16,
and J<=256delta_-^2/49, (13.3) gives the convenient uniform bound

\[
 \delta_-^2+\inf_{\beta\ge4}D_\beta/V
        \le200(\delta_-+\sqrt{s_0})-45z/4.
\]

The lower bound (9.1) holds for every beta, so
epsilon_*+45z/4<=200(delta_-+sqrt(s_0)). Squaring and using
(delta_-+sqrt(s_0))^2<=2(delta_-^2+s_0) proves the claim. QED.

For exact Einstein metrics this proof also applies with epsilon_* from
Theorem 10 instead of (9.1). Thus chi/A<=B_0, actual p>=A, and
1/4<=h<=1/3 imply

\[
                      e\le G(h)-c(B_0),                \tag{13.4}
\]

without a diameter or class-square bound. In the complex-hyperbolic surgery
family (12.7), B_0=2/3 suffices. The approximate-input version of (13.4)
does not follow from Cheeger--Tian: exact Einstein regularity was essential
in Theorem 10. These are distinct quantified extensions, not a single
unconditional estimate.

For exact metrics a shorter optimization gives the better explicit margin
c(B_0)=epsilon^2/288, where epsilon=min{1,c(4B_0)} from (12.3).
Put a=3(1-h), d=a-e, and Delta=G(h)-e. If beta_*=sqrt(8e/d)>=4,
minimizing (10.1), using p/A>=1, gives

\[
 \epsilon e\le 14e+2a-36+8\sqrt{2e(a-e)}=:P_a(e).
\]

The upper zero of P_a is G. Thus e<=G, and
e(a-e)<=G(a-G)+G Delta implies P_a(e)<=8sqrt(2G Delta)
<=12sqrt(2Delta). Since e>=1, Delta>=epsilon^2/288.
If beta_*<4 then e<2a/3 and G-2a/3>=4/9, which is stronger.
The d=0 case follows by taking beta->infinity. Therefore

\[
                 e\le G(h)-\epsilon^2/288.             \tag{13.5}
\]

The main improvement over the inherited upper wall is uniformity at h=1/4,
not the first appearance of a strict upper wall for fixed h>1/4.
As a secondary recovery of the previously studied near-1/3 obstruction,
choose beta_c=(14-epsilon+sqrt((14-epsilon)^2+128))/4 in [7,8]. Its
e-independent term in (10.1) equals epsilon, so the remaining numerator
must be nonnegative. This gives h<=1-6/(beta_c+1)<=1/3-8epsilon/243.
It is not counted as a separate new obstruction mechanism.

#### 13.1 What the upper wall does and does not decide topologically

The new fixed margin excludes candidate energy levels, not automatically
new smooth topologies. The recorded Chern--Weil budgets give upper bounds
e<=U, not a lower pinning of e near G. This matters for the realized families.
For instance take complex-hyperbolic covers with A_j->infinity, let
k_j=ceil(A_j/4), and make no S1xS3 surgery. The actual exceptional-sign
classes give p>=A_j and a^2=T_+=A_j-k_j, while

\[
 h_j\ge1/4,\quad h_j\to1/4,\qquad
 \chi(M_j)/A_j\to7/12,\qquad U_j=3(1-h_j)\to9/4.
\]

At the limiting topological data, the formal candidate e=7/4, p/A=1
has W^+/(2pi^2 A)=1/6 and W^-/(2pi^2 A)=1, where W^pm here denote
their integrated squared energies. The scalar budget and every classical
pencil inequality are positive at this value; it stays distance 1/2
below G(1/4). Thus these known inequalities do not force candidates into
the new forbidden upper strip. This is a witness about implication between
inequalities, NOT an Einstein metric or a counterexample to a theorem.

More generally the known lower roots and the I41 wall remain separated
from G near h=1/4. After the harmless caps on the recorded constants,
on [1/4,7/24] their maximum is at most 19/12, whereas G-1/288>7/4.
Replacing the old upper root by (13.5) therefore need not make the numeric
feasible interval empty. An additional genuine lower-volume/energy input
would be needed for that use. In contrast, the BF family in Section 4
already has an actual all-metric exclusion from the LOWER linear wall;
that application does not depend on such an unproved upper-corner pinning.

### 14. The torsion transition cannot be closed by a Dirac null-form shortcut

This section records a targeted construction, not an actual gauge counterexample.
It explains why the signed transition flux in Theorem 5 still needs the
full curvature equation or a global argument. The simple pointwise Dirac
constraints do not force its positive quartic component to cancel.

Use Clifford matrices mapping S^+ to S^-:

\[
 C_1=I,\quad C_2=\operatorname{diag}(i,-i),\quad
 C_3=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 C_4=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}.
\]

Reverse Clifford action is -C_j^*. At a point Phi=sqrt(rho)e_1, write
H_{ji}=(h_{ji},k_{ji}) and K_{ij}=k_{ij}-k_{ji}. Differentiated D Phi=0
has components

\[
 d_{1j}=h_{j1}+ih_{j2}+k_{j3}-ik_{j4}=0,\quad
 d_{2j}=-h_{j3}-ih_{j4}+k_{j1}-ik_{j2}=0.              \tag{14.1}
\]

The linear Hessian contribution to nabla_j t is
rho(k_{j1}+ik_{j2},-k_{j3}-ik_{j4}). The projected derivative
N_{bc}=sum_j(C_j^*)_{1b}(nabla_j t)_c/sqrt(2) can be written as

\[
 N=\sqrt{\rho/2}\,\mathcal L(\nabla\zeta)+\mathcal R_N,
 \quad |\mathcal R_N|\le C[\rho^{3/2}(|\operatorname{Ric}^{\circ}|
                        +|W^+-W_0|)+|\zeta||P_{\rm spin}|],      \tag{14.2}
\]

where

\[
\mathcal L(Z)=\begin{pmatrix}
 Z_{13}-Z_{24}+i(Z_{14}+Z_{23})&-Z_{33}+Z_{44}-i(Z_{34}+Z_{43})\\
 Z_{11}-Z_{22}+i(Z_{12}+Z_{21})&-Z_{31}+Z_{42}-i(Z_{32}+Z_{41})
\end{pmatrix}.
\]

For verification the Hessian expression is rho(L(h)+C(K))/sqrt(2),
modulo (14.1), with

\[
\mathcal C(K)=\begin{pmatrix}
2iK_{12}&-K_{13}-iK_{14}+iK_{23}-K_{24}\\
K_{13}+iK_{23}-iK_{14}+K_{24}&2iK_{34}
\end{pmatrix}.
\]

Central curvature, scalar curvature and the axial W_0 model cancel in this
projection. Substitute sqrt(rho)h_ji=nabla_j zeta_i-<P_j,P_i>;
the remaining quadratic expression vanishes for the pure kernel component
(iz,z,iw,w), while the other terms are bounded by C|zeta||P_spin|.
This proves (14.2) directly from the actual prolonged equations, not by
discarding all components except the Dirac trace.

In a compatible frame with t=sqrt(m)e_1, writing x_j=(nabla_j t)_1
gives the first column of N as
(x_1-ix_2,-x_3+ix_4)/sqrt(2), while dm=2sqrt(m) Re x. Hence

\[
                 |\langle t,\nabla t\rangle|^2
                      \le\tfrac34|dm|^2+4m|N|^2.      \tag{14.3}
\]

Determinant-curvature saturation does not directly control N, since that
curvature has canceled from (14.2). More decisively, even N=0 does not
remove the radial derivative in (14.3). Take h=0 and the symmetric
trace-free Hessian increment

\[
k=\frac12\begin{pmatrix}
1&-i&0&0\\-i&-1&0&0\\0&0&-1&i\\0&0&i&1
\end{pmatrix}.
\]

It satisfies (14.1), preserves curvature commutators and trace, and gives
nabla t/rho=[(1,0),(-i,0),(0,1),(0,-i)]. Its real Jacobian determinant
is positive one while N=0. These are exact Clifford-algebra checks.

There is an actual local Dirac field realizing this increment. On flat C^2
with A=0, put z_1=x_1+ix_2, z_2=x_3+ix_4,
g_0=(bar z_1^2-bar z_2^2)/4, and

\[
 \Phi_\epsilon(x)=(1,\epsilon g_0(x/\epsilon)),\qquad
 t_\epsilon(x)=(\bar z_1/\epsilon,\bar z_2/\epsilon).
                                                               \tag{14.4}
\]

Direct differentiation gives D^+Phi_epsilon=0 and D^-t_epsilon=0,
and t_epsilon is exactly the cubic torsion of Phi_epsilon, not an
independently chosen field. On |x|<=R_0 epsilon, for fixed R_0,
rho=1+O(epsilon^2), |zeta|=O(epsilon), |d zeta|=O(1), and
int|nabla t|^2=O(epsilon^2). Yet its isolated torsion zero has positive
index and can carry unit signed transition flux.

Indeed at t=(r,0), write nabla t=(x+iy,z+iw) as real one-forms. In the
flat rank-two connection the transgression in Section 7 gives

\[
        d\chi(m)\wedge T_t
             =-\frac{\chi'(m)}{\pi^2m}
                       x\wedge y\wedge z\wedge w.      \tag{14.5}
\]

For (14.4) the real Jacobian is epsilon^{-4} and m=|x|^2/epsilon^2.
If chi equals one near zero and vanishes before m=R_0^2, polar integration
gives int dchi wedge T_t=-int_0^{R_0^2}chi'(m)dm=1.
Thus small current, the two exact Dirac equations, and a small integrated
first-derivative budget cannot alone cancel the signed flux.

This field is NOT an actual positive-weight monopole: F_A^+=0 while
f sigma(Phi_epsilon) is nonzero for f>0. Nor does flat curvature satisfy
the normalized negative Einstein target on a global fixed-volume manifold.
It rules out precisely the proposed Dirac-only/null-form deduction, not
the zero-end gap and not the full actual equations. It leaves the new
geometric exclusions in Sections 8--13 intact.

### 15. The positive transition core persists for the actual local gauge equation

The preceding construction can be continued to solve the positive-weight
Seiberg--Witten equations themselves. This strengthens the local test:
the missing global estimate cannot be obtained merely by declaring that
the critical transition scaling violates the local gauge PDE.

**Theorem 12 (local actual core).** Fix f_*>0 and a>0. For every sufficiently
small epsilon>0 there is a smooth unitary determinant connection A_epsilon
and positive spinor Phi_epsilon on the Euclidean ball B_{2epsilon} such that

\[
 D_{A_\epsilon}\Phi_\epsilon=0,\qquad
       -iF_{A_\epsilon}^+=f_*\sigma(\Phi_\epsilon).
                                                               \tag{15.1}
\]

On smaller fixed-proportion balls their cubic torsion t_epsilon has exactly
one positive-index zero, at the center. There
is a cutoff chi(|t_epsilon|^2), one near its zero and zero near the boundary,
for which

\[
 \int d\chi\wedge T_{t_\epsilon}=1+O(\epsilon^4).      \tag{15.2}
\]

The physical-coordinate estimates are

\[
\begin{gathered}
 |\Phi_\epsilon|^2=a^2+O(\epsilon^2),\quad
 |\langle\Phi_\epsilon,\nabla_A\Phi_\epsilon\rangle|=O(\epsilon),
 \quad |\nabla_A\Phi_\epsilon|=O(1),\quad |F_A|=O(1),\\
 \int|\nabla_A^2\Phi_\epsilon|^2+
       \int|\nabla_{3A}t_\epsilon|^2=O(\epsilon^2),\quad
 \int|F_A|^2=O(\epsilon^4).
\end{gathered}                                                     \tag{15.3}
\]

The signed transition flux nevertheless has order one, as does its
corresponding quartic transition energy. All these are unnormalized local
integrals. The flat core also has int|Ric+g|^2=O(epsilon^4).

**Proof of existence.** Work first on the fixed Euclidean ball B_2 in
y-coordinates. Let lambda=epsilon^2 and
Phi_0=a e_1+epsilon g_0(y)e_2, with g_0 from (14.4). Thus D^+Phi_0=0.
On imaginary-valued forms put T=(d^*,sqrt(2)d^+). In flat space
TT^*=Delta on Omega^0 direct-sum Omega^2_+, with Delta nonnegative.
Let G_D be the componentwise Dirichlet inverse of Delta on this smooth
ball, and define

\[
 R_A=T^*G_D,\qquad R_D=D^-G_D.
\]

Then TR_A=Id and D^+R_D=Id. On C^{k,alpha} for fixed k>=3, 0<alpha<1,
both are bounded operators gaining one derivative, by the classical
[Dirichlet Schauder estimates, lectures 11--17](https://ocw.mit.edu/courses/18-156-differential-analysis-spring-2004/pages/lecture-notes/).
Their boundary traces
are not prescribed independently; only their right-inverse property is used.
For a spinor Phi in a fixed bounded C^{k,alpha} neighborhood of Phi_0 set

\[
 A(\Phi)=R_A(0,\sqrt2\lambda i f_*\sigma(\Phi)),\qquad
 \mathcal T(\Phi)=\Phi_0-\tfrac12R_D[c(A(\Phi))\Phi]. \tag{15.4}
\]

Products and the quadratic spinor map are locally Lipschitz in this Banach
space. A(Phi)=O(lambda) and the Lipschitz constant of T is O(lambda),
uniformly for small epsilon. A ball of radius C lambda about Phi_0 is
mapped to itself for fixed sufficiently large C; for sufficiently small
epsilon, T is a contraction. Its fixed point and the associated A satisfy

\[
 d^*A=0,\quad F_A^+=\lambda i f_*\sigma(\Phi),\quad D_A\Phi=0,
 \quad \|A\|_{C^{k+1,\alpha}}+
        \|\Phi-\Phi_0\|_{C^{k,\alpha}}\le C\epsilon^2.
\]

The fixed-point identities and elliptic regularity bootstrap to smoothness.
Rescale x=epsilon y, setting Phi_x(x)=Phi_y(x/epsilon) and
A_x(x)=epsilon^{-1}A_y(x/epsilon) in components. The Dirac equation scales
by epsilon^{-1}, the curvature by epsilon^{-2}; lambda=epsilon^2 cancels
the latter factor. This proves (15.1) with the fixed positive f_*.

**Torsion and charge.** In y-coordinates the physical torsion obeys

\[
        t_\epsilon(\epsilon y)
           =a^2(\bar z_1,\bar z_2)+O(\epsilon)
                                      \quad\text{in }C^1(B_1).
                                                               \tag{15.5}
\]

This follows directly from the cubic formula: its leading derivative of
epsilon g_0 cancels the physical epsilon^{-1}, and all fixed-point and
connection corrections are O(epsilon). The leading real linear map is
invertible with positive determinant a^8. Small C1 perturbation makes
the map injective on a smaller convex ball. The degree on its boundary
is positive one, so it has exactly one zero. In fact Phi_0 is even under
y->-y. The Dirichlet inverse preserves parity, whereas T^* and D^- reverse
it. Thus the contraction preserves even Phi and produces odd A; the fixed
point has these parities. Its torsion is odd, placing its unique zero
exactly at the center. The bounds (15.3) follow by differentiating (15.4)
and rescaling. In particular the squared Hessian L2 integral is
O(epsilon^2); its L2 norm is O(epsilon), not O(epsilon^2).

In the extending flat spin frame, E_-=S^- tensor L has curvature
(3/2)F_A I and
c_2(E_-)=-9F_A wedge F_A/(16pi^2). Removing a small sphere about the
torsion zero, the transgression convention of Section 7 gives

\[
 \int_B c_2(E_-)-\int_{\partial B}T_t=1,
 \qquad
 \int_B d\chi\wedge T_t=1-\int_B\chi c_2(E_-).
\]

Since F_A=O(1) and Vol(B)=O(epsilon^4), (15.2) follows. On a fixed
torsion-amplitude transition annulus, (15.5) also gives the order-one
quartic cost directly. QED.

The costs can be identified more precisely. The constant-source part of
the Dirichlet calculation gives, in y-components,

\[
 A_y=\epsilon^2 A_0+O(\epsilon^3),\qquad
 A_0=\frac{if_*}{2}\iota_y\sigma(ae_1).
\]

Consequently the physical curvature is if_*sigma(ae_1)+O(epsilon), its
ASD part is O(epsilon), and

\[
 \int_{B_{2\epsilon}}|F_A|^2
    =\pi^2f_*^2a^4\epsilon^4+O(\epsilon^5).
                                                               \tag{15.6}
\]

For fixed 0<m_1<m_2<4a^4 let T_epsilon={m_1<|t_epsilon|^2<m_2}.
The C1 convergence in (15.5), valid on B_2, and rescaling imply

\[
\begin{aligned}
 \int_{T_\epsilon}|\nabla t|^4
       &\longrightarrow8\pi^2(m_2^2-m_1^2),\\
 \int_{T_\epsilon}|\langle t,\nabla t\rangle|^2|\nabla t|^2
       &\longrightarrow\frac{8\pi^2}{3}(m_2^3-m_1^3),\\
 \int_{T_\epsilon}|dm|^2|\nabla t|^2
       &\longrightarrow\frac{16\pi^2}{3}(m_2^3-m_1^3).
\end{aligned}                                                   \tag{15.7}
\]

Indeed the limiting y-field has m=a^4|y|^2, |dt|^2=4a^4,
|<t,dt>|^2=2a^8|y|^2 and |dm|^2=4a^8|y|^2; integrate with
the four-dimensional polar factor 2pi^2 r^3 dr. The limiting level
spheres are regular, so replacing the exact transition region by its
limiting annulus is justified by this C1 convergence.

The leading anti-complex-linear derivative has N=0 in Section 14's
projection. The actual Phi-adapted frame differs by O(epsilon), while
the physical derivative is O(epsilon^{-1}); hence N=O(1) and

\[
       \int_{T_\epsilon}m|N|^2|\nabla t|^2=O(\epsilon^2).
                                                               \tag{15.8}
\]

Thus the positive charge survives while this projected contribution tends
to zero. The critical radial mass term, not an uncontrolled N term, can
carry the transition cost. Even int|dm|^2=O(epsilon^2) does not remove it.

For the flat metric the inherited majorant weight is exactly sqrt(3), so
f_*=sqrt(3) is an allowed concrete choice; there is no zero-weight limit.
Choosing a^2=4/3 and radius R_0 epsilon with R_0=2sqrt(2)/3 makes the
leading boundary torsion mass a^4 R_0^2=128/81 equal to the zero-end
mass. This is amplitude matching only. Its outgoing normal mass derivative
is 2a^4 R_0/epsilon+O(1), and its unit torsion boundary map has degree +1
in the extending trivialization. It cannot be joined through a zero-free
collar to a regular nonzero torsion field extending over a ball, whose
boundary degree is zero. Compensating zeros or a nontrivial marked bundle
identification would be necessary.

No such exterior, clutching, fixed closed manifold, or conformally solvable
global class system is produced here. The flat scalar curvature and weight
also differ from the negative Einstein exterior model. Consequently this
is an exact local concentration mechanism with its relative charge, not
a counterexample to O10, not a closed near-Einstein construction, and not
a reversal of the geometric exclusions above. It does establish that the
remaining work must use global matching or information beyond the local
weighted gauge equations and the displayed integral budgets alone.

#### 15.1 Removing the local metric and weight mismatch

The local core also exists on a FIXED hyperbolic background with sectional
curvature -1/3. It then satisfies Ric=-g, W^pm=0 and the canonical weight
f_0=2 exactly; the two mismatches just noted are not local obstructions.
Here is the perturbation argument, including its boundary convention.

Fix a point p. In geodesic coordinates x=epsilon y set
g_epsilon=epsilon^{-2}(exp_p(epsilon dot))^*g on B_2. In polar and
Cartesian coordinates, respectively,

\[
\begin{split}
 g_\epsilon&=dr^2+\frac3{\epsilon^2}
                    \sinh^2(\epsilon r/\sqrt3)g_{S^3},\\
 (g_\epsilon)_{ij}
  &=\delta_{ij}+\frac{\epsilon^2}{9}
             (|y|^2\delta_{ij}-y_i y_j)+O(\epsilon^4).
\end{split}                                                     \tag{15.9}
\]

In every fixed C^{k,alpha} norm this is an O(epsilon^2) perturbation of
the Euclidean metric. Use the positive-square-root orthonormal coframe
and its spin lift. The spin connections and coefficients of
D_epsilon-D_0 are O(epsilon^2), the latter as a first-order operator.
For T_epsilon=(d*_epsilon,sqrt(2)d+_epsilon) the exact identity
T_epsilon T_epsilon^*=Delta_H remains valid on Omega^0 direct-sum
Lambda+_epsilon. Identify that target with a fixed trivial bundle.
Both this second-order operator and D+_epsilon D-_epsilon have the form

\[
          L_\epsilon=\Delta_0+O(\epsilon^2)\partial^2
                             +O(\epsilon^2)\partial+O(\epsilon^2).
\]

Their auxiliary Dirichlet inverses exist by the convergent Neumann series

\[
 G_\epsilon=G_0[I+(L_\epsilon-\Delta_0)G_0]^{-1}.
\]

The norm here is C^{k,alpha}->C^{k,alpha} for the bracketed operator;
G_0 maps into C^{k+2,alpha} with zero boundary trace. Thus the new
right inverses R_A=T_epsilon^*G_A and R_D=D-_epsilon G_D gain one
derivative uniformly. No boundary condition on A or Phi is asserted.

The flat seed Phi_0=a e_1+epsilon g_0 e_2 is no longer exactly harmonic,
but the corrected seed

\[
       \widehat\Phi_0=\Phi_0-R_D D_\epsilon^+\Phi_0
\]

is: D+_epsilon Phi_hat_0=0, and Phi_hat_0-Phi_0=O(epsilon^2).
Apply the same contraction (15.4) with this seed, the curved right inverses,
lambda=epsilon^2 and f_*=2. The result obeys the exact physical equations

\[
            D_{A,g}\Phi=0,\qquad F_A^+=2i\sigma_g(\Phi).
                                                               \tag{15.10}
\]

The physical metric is the original fixed g, not g_epsilon. It has
s=-4, W^pm=0 and q=4, so the inherited majorant is indeed f_0=2.
All fields differ from the flat seed in rescaled coordinates by
O(epsilon^2). The physical cubic torsion therefore still has the C1
expansion (15.5), giving one positive simple zero and the same limiting
transition costs (15.7)--(15.8). Only its O(epsilon^2) displacement in
physical coordinates is needed here; no parity assertion is necessary.

Take a^2=4/3. The physical determinant curvature has F_A^-=O(epsilon)
and |F_A^+|^2=8/9+O(epsilon^2). The full bundle E_-=S^- tensor L
now includes the nonflat spin connection. Its characteristic density is

\[
 16\pi^2c_2(E_-)
   =\left[9(|F_A^+|^2-|F_A^-|^2)+\frac23\right]d\mu_g
   =\left[\frac{26}{3}+O(\epsilon^2)\right]d\mu_g.
\]

It is bounded; the relative formula still gives
int dchi wedge T_t=1+O(epsilon^4). The Ricci and Weyl error terms vanish
identically on the core. The form-closure term does NOT vanish identically,
and no normalized full defect on these shrinking balls is claimed to
tend to zero. Quadratic derivative costs remain O(epsilon^2), whereas
the critical radial transition cost has a positive limit.

This removes the metric and canonical-weight mismatches, but not the
boundary winding, O(epsilon^{-1}) outgoing torsion derivative, determinant
ASD matching, or global conformally solvable class. In particular, the
core's F_A^- is small while the globally calibrated endpoint exterior
requires its squared mean to approach 2/9. Exact local Einstein and gauge
equations admit the core; producing a closed endpoint degeneration still
requires the entire exterior and its matching. Theorem 10 excludes that
global construction at bounded Euler density, so it is not contradicted.
