# Actual spinor energy and the location of a possible topological cost

26--27 September 2026, Beijing time. Continuation of
[the boundary proof](20260926_boundary_compatibility.md), based at local
commit `f48f385`. The owner's
[parallel execution brief](../guidance/source/20260926_web_parallel_execution.zh.md)
proposes zero-Weyl rigidity and a linear small-h lower bound. Neither is
assumed proved here. The inherited actual weighted-field construction is an
explicit premise, with its original fixed-structure/conformal-solvability
quantifiers. No inherited proof or eight-volume source is replaced.

Two connections are proved below using the **same bounded weighted
solution**. First, an exact remainder identity, the localized spinor equation
and signed Chern transgression force any sublinear small-h sequence to carry
both projective first-order energy and critical transition-layer concentration.
This avoids comparing unidentified ordinary and weighted solutions. Second,
a smooth cubic torsion field satisfies an additional Dirac identity, giving
a vanishing weak residual at the hypothetical zero-Weyl endpoint. These are
necessary-structure and weak-equation results; neither the linear small-h
gap nor the zero-end exclusion is assumed or claimed.

## 1. An exact identity without differentiating the weight

Let M be a closed oriented Riemannian four-manifold. Use the spinor and
curvature conventions of [the functional pencil](../mathematics/current/line1_functional_pencil.md).
Fix an actual Spin^c structure and a smooth positive weight f, and a solution
of the corresponding rescaled Seiberg--Witten equations. Write

\[
 \rho=|\Phi|^2,\quad K_A=\int|\nabla_A\Phi|^2,\quad
 p=(a_g^+)^2,\quad \Sigma=\int s^2-32\pi^2p,
 \quad J_+=\|iF_A^+-2\pi H\|_2^2,
\]

where H is the self-dual harmonic representative of a_g^+. The sign of
the quadratic map is chosen so that the determinant curvature has harmonic
projection 2pi H. The two identities needed are

\[
 4K_A+\int s\rho+\int f\rho^2=0,\qquad
 \int f^2\rho^2=32\pi^2p+8J_+.                 \tag{1.1}
\]

**Proposition 1.** For every constant c>0, the same solution satisfies

\[
 \boxed{\Sigma+\int(f-c)^2\rho^2
 =\|s+c\rho\|_2^2+8cK_A+8J_+.}              \tag{1.2}
\]

**Proof.** Expand the square on the right and substitute (1.1). The
coefficient of rho^2 after cancelling the scalar-spinor term is
c^2-2cf+f^2=(f-c)^2. No derivative of f is taken. QED.

For f=c=1 this recovers the ordinary-solution remainder in the supplied
brief. For a variable f, it is not legitimate to omit the additional
nonnegative term on the left. In particular, replacing Phi by sqrt(f)Phi
would introduce derivatives of f; (1.2) does not make that replacement.
The equations and Weitzenboeck input are classical; retaining and using the
same weighted solution is the point of the present composition.

## 2. Uniform amplitude and potential estimates for the supplied solution

Retain the actual conformal-solvability hypotheses of the inherited pencil,
with the same structure throughout all auxiliary weights. Put

\[
 r=\fint|\operatorname{Ric}+g|^2,\quad
 \kappa=r+D_\beta/V,\quad 2\le\beta<\infty,
 \quad q_\beta=4(1+1/\beta),
 \quad c_\beta=\sqrt{q_\beta},\quad \rho_\beta=2c_\beta/3.
\]

Here c_beta denotes the reference **weight**, not the form rescaling
constant denoted similarly in some earlier manuscripts. Set
U=s+f rho and U_beta=-4+c_beta rho_beta=(4/3)(2/beta-1).
The selected smooth majorants may have an arbitrarily small total allowance
epsilon V in the following estimates. Every estimate concerns the same
actual solution; one can choose epsilon after fixing each metric and class.

**Lemma 2.** The inherited construction gives, uniformly in beta,

\[
 \rho\le4,\qquad
 \fint(\rho-\rho_\beta)^2\le40\kappa+o(1),\qquad
 \fint(f-c_\beta)^2\le\tfrac{33}{2}\kappa+o(1),
                                                        \tag{2.1}
\]
\[
 \fint|U-U_\beta|^2\le1504\kappa+o(1),\quad
 \fint|d\rho|^2\le\tfrac{26}{3}\kappa+o(1),\quad
 8J_+/V\le52\kappa+o(1).                              \tag{2.2}
\]

**Proof.** With the original notation w=sqrt(6)|W+|, q=-s+w,
Q=max(q,3), e=s+4, u=3rho/2 and f_0=max(sqrt(Q),(-s)_+/4), the exact
square completion gives

\[
 \int(q-q_\beta)^2\le18\kappa V,\quad
 \int e^2\le4\kappa V,\quad
 \int Q(u-\sqrt Q)^2\le117\kappa V+o(V).
\]

Clipping at three does not increase distance to q_beta in [4,6]. Thus
int(sqrt(Q)-c_beta)^2<=6kappa V and
int(u-sqrt(Q))^2<=39kappa V. Combining gives the first amplitude
estimate. Also (f_0-sqrt(Q))^2<=f_0^2-Q<=9e^2/16, which gives the
weight estimate. The potential difference is
e+c_beta(rho-rho_beta)+(f-c_beta)rho. First bound the first two terms
together by 488kappa V and the last by 264kappa V, and then their sum
by 1504kappa V. Finally D_0<=52kappa V/3 controls 2int|drho|^2.
The actual curvature moment C_act satisfies
C_act-72pi^2p<=117kappa V+o(V); since
8J_+=(4/9)(C_act-72pi^2p), this proves the final estimate. QED.

**Corollary 3 (same-solution scalar-slack comparison at beta=2).** Take
c=sqrt(6). Then

\[
 -540\kappa V-o(V)\le8\sqrt6 K_A-\Sigma
 \le264\kappa V+o(V).                                 \tag{2.3}
\]

Indeed rho_2=4/sqrt(6), so int(s+c rho)^2<=488kappa V+o(V),
int(f-c)^2rho^2<=264kappa V+o(V), and 8J_+<=52kappa V+o(V).
Substitute in (1.2). The little-o allowance here is freely selectable
smoothing error, not an assumed limiting solution or a rate in kappa.

## 3. Actual first-order energy cannot be hidden at spinor zeros

Use a fixed pair 0<a<b<4/3. A Lipschitz nonincreasing cutoff chi(rho)
equals one below a and zero above b, with |chi'|<=1/(b-a). Smooth
approximations give the same inequalities. Testing

\[
             4\nabla_A^*\nabla_A\Phi+U\Phi=0
\]

against chi(rho)Phi gives the exact real identity

\[
 4\int\chi|\nabla_A\Phi|^2+
 2\int\chi'|d\rho|^2+\int\chi U\rho=0.
\]

If mu_b=Vol{rho<b}/V, Cauchy--Schwarz gives

\[
 \fint_{\{\rho\le a\}}|\nabla_A\Phi|^2
 \le\frac{\fint|d\rho|^2}{2(b-a)}
 +\frac b4\left(|U_\beta|\mu_b+
      \|U-U_\beta\|_{L^2_{\rm avg}}\sqrt{\mu_b}\right). \tag{3.1}
\]

The symbol fint over a subset here and below means integral over the
subset divided by **total** V. By (2.1),
mu_b<= (40kappa+o(1))/(rho_beta-b)^2; rho_beta>=4/3 and |U_beta|<=4/3.
Consequently

\[
 \boxed{\int_{\{\rho\le a\}}|\nabla_A\Phi|^2
             \le C_{a,b}\kappa V+o(V).}                \tag{3.2}
\]

This is uniform over all finite beta>=2, and uses the actual spinor equation
and moment remainders. It is stronger than applying a generic Hessian/L4
estimate, which would give only an O(sqrt(kappa)) bound. It does not estimate
the fourth-power gradient or squared Hessian energy on the same set.

There is a further phase/radial decomposition. On {rho>0}, let Pi_Phi be
Hermitian projection onto the complex line spanned by Phi, and write
gamma=Im< Phi,nabla_A Phi >, with the pairing linear in its second entry.
For the normalized quadratic map psi used
in the original proof, direct differentiation gives

\[
 4\rho|\nabla_A\Phi|^2-|\nabla\psi|^2=4|\gamma|^2,
 \qquad
 |\Pi_\Phi\nabla_A\Phi|^2
       =\frac{|d\rho|^2}{4\rho}+\frac{|\gamma|^2}{\rho}.
                                                        \tag{3.3}
\]

These identities can be checked in a unitary frame Phi=(sqrt(rho),0),
with an arbitrary complex two-component derivative; they are gauge
invariant. Since both remainders are summands of D_0,

\[
 \int_{\{\rho>a\}}|\Pi_\Phi\nabla_A\Phi|^2
       \le\frac{13}{2a}\kappa V+o(V).                 \tag{3.4}
\]

Thus all but O(kappa V) of K_A lies in
int_{rho>a}|(1-Pi_Phi)nabla_A Phi|^2. This is a change of direction of
the spinor line, not a gauge phase change or a change of amplitude.

For completeness, testing the spinor equation against Phi and using (2.1)
--(2.2) gives

\[
 K_A/V=-\tfrac14 U_\beta\rho_\beta+O(\sqrt\kappa)+o(1)
       =\tfrac29\sqrt{q_\beta}(1-2/\beta)
          +O(\sqrt\kappa)+o(1).                       \tag{3.5}
\]

In a putative actual zero-end sequence beta->infinity, kappa->0,
the projective-direction energy outside {rho<=a} therefore tends to 4/9.
The previously proved two-form energy limit 8/3 is consistent with this.
Neither limit is zero-Weyl rigidity: it identifies which nonparallel
energy that rigidity would have to detect.

## 4. A necessary structure theorem for any sublinear small-h sequence

Fix precisely the varying-topology family in Theorem 5 of
[the preceding continuation](20260926_boundary_compatibility.md), with
T_+=A(1-h), p>=A and U_top=F(h)+o(h^2). Its selected actual class has
a^2=A-k and c_2(S^+)[M]=ell, with ell/(Ah)->7/36. The positive budget,
actual conformal-solvability and chiral identities are unchanged.

**Theorem 4 (where a hypothetical sublinear cost must go).** Suppose
metrics g_j on this same family satisfy E(g_j)=o(h_j). After the optimal
negative rescaling, there exist the bounded beta=2 actual weighted
solutions above, with freely chosen allowances o(h_j), such that

\[
 \frac{V_j}{A_j}\to2\pi^2,\qquad
 \kappa_j=o(h_j),\qquad
 \frac{\Sigma_j}{A_jh_j}\to32\pi^2,
                                                        \tag{4.1}
\]
\[
 \boxed{\frac1{A_jh_j}
   \int_{\{\rho_j>a\}}|(1-\Pi_{\Phi_j})\nabla_{A_j}\Phi_j|^2
       \longrightarrow\frac{4\pi^2}{\sqrt6}.}           \tag{4.2}
\]

The integral on {rho_j<=a} and the line/radial/phase derivative on
{rho_j>a}, divided by A_j h_j, both tend to zero.

**Proof, including the normalization and sign.** Put R=int|Ric|^2,
I=int s, L_s=int(s-I/V)^2 and e=R/(8pi^2 A). For R>0,

\[
 E=4-I^2/(VR)=(4P+L_s)/R.
\]

If I>=0, the actual scalar estimate gives
32pi^2 A<=int s_-^2<=L_s<=RE, hence 4<=eE. On the other hand,
e(1-E)<=U_top and U_top<=2 eventually, so for E<1/2 we have e<=4
and eE<2, a contradiction. Thus I<0 for all late j.
The minimizing constant is lambda_*=R/I<0. Set g'=(-lambda_*)g.
Then r(g')=E(g), V(g')=R/(4-E), and R,P,D_2,p are invariant under
this constant rescaling. Relabel g' as g.

The exact identities are

\[
 D_2=36\pi^2A\{e-(1+h)-2(p/A-1)\},\qquad
 36\pi^2(p-T_+)=\tfrac92P+\tfrac98\Sigma-D_2.
\]

Together with p>=A, D_2>=0 and e(1-E)<=U_top=1+h+O(h^2), these
give e=1+h+o(h), p-A=o(Ah), D_2=o(Ah), P<=RE/4=o(Ah), and
Sigma/(Ah)->32pi^2. Also V/A=8pi^2e/(4-E)->2pi^2, proving (4.1).
Equation (2.3) then gives K_A/(Ah)->4pi^2/sqrt(6). Choose all
smoothing allowances o(h). Equations (3.2) and (3.4), with kappa=o(h),
leave exactly (4.2). QED.

This theorem goes beyond a formal moment model: it concerns the same
actual bounded solution used in the curvature-deficit proof. It does not
assert that (4.2) is impossible. The still-open estimate P+D_2>=c ell
would exclude the entire sequence and imply a linear lower bound; no such
estimate is assumed in Theorem 4.

### 4.1 Positive Chern charge forces critical transition concentration

The necessary condition can be strengthened using the **sign** of the
determinant curvature, not an absolute bound on all its components.
Write Theta=(kappa+epsilon)V, where epsilon is the selectable allowance.
For bundle curvature in this subsection use the two-form Hilbert--Schmidt
norm sum_{i<j}|F_ij|^2, half the double-sum convention of the inherited
Hessian lemma. Let F be the curvature of the positive spinor connection,
F=Omega+(F_A/2)I, where Omega is traceless.

**Theorem 5 (localized positive-charge bound).** For the same beta=2
supplied solutions there is a universal C such that

\[
 \boxed{c_2(S^+)[M]\le C\Theta+
               C\int_{\{1/2<\rho<1\}}|\nabla_A\Phi|^4.} \tag{4.3}
\]

No bound for W-, F_A- in L-infinity, derivatives of f, a uniform Sobolev
constant or transverse zeros is required. The inequality holds also when
c_2 is negative; its useful application here is c_2=ell>0.

**Proof.** For a unitary rank-two connection,
c_2(F)=(tr(F wedge F)-trF wedge trF)/(8pi^2). In our conventions,

\[
 16\pi^2 c_2(F)=\left(|F_A^+|^2-|F_A^-|^2
                 -2|\Omega^+|^2+2|\Omega^-|^2\right)d\mu,
 \quad |\Omega^+|^2=|W^+|^2+s^2/48,\quad
 |\Omega^-|^2=|\operatorname{Ric}^\circ|^2/4.            \tag{4.4}
\]

In particular its positive part is bounded by
(|F_A+|^2+|Ric^circ|^2/2)/(16pi^2), while the term
-|F_A-|^2/(16pi^2) must be retained for the argument below.

Let B={rho<=1} and T={1/2<rho<1}. Since (4/sqrt(6)-1)^2>2/5,
(2.1) gives Vol(B)<=100Theta. The actual equation and weight estimate give

\[
 \int_B|F_A^+|^2=\tfrac18\int_B f^2\rho^2
       \le\tfrac18(12\operatorname{Vol}(B)+33\Theta)
       \le155\Theta.                                  \tag{4.5}
\]

On B the bounded model A_{omega,1/2}, with omega=sqrt(3)psi/2, has
|A_{omega,1/2}|^2=3rho^4/32<=3/32. The inherited squared model error
is at most CTheta. Thus int_B|W+|^2<=CTheta; also int_B s^2<=CTheta
and int|Ric^circ|^2<=Theta. Consequently

\[
 \int_B G^2\le C\Theta,\qquad G^2=|\Omega|^2+|F_A^+|^2. \tag{4.6}
\]

On {rho>0}, set u=Phi/sqrt(rho), Pi=uu*, Q=1-Pi. Define a unitary
connection nabla^0 by
nabla^0(zu+w)=dz tensor u+Q nabla_A w for w perpendicular to u.
It fixes u, so c_2(F^0)=0. In a local unitary frame (u,v), write
nabla_A u=i alpha u+b v; the difference B_c=nabla_A-nabla^0 is
the matrix [[i alpha,-b*],[b,0]], with |B_c|<=sqrt(2)|nabla_A u|.
The projected-connection curvature formula gives
|F^0|<=C(|F|+|nabla_A u|^2). For nabla^t=nabla^0+tB_c,
F^t=(1-t)F^0+tF-t(1-t)B_c wedge B_c, hence the same bound holds.
The Chern--Weil transgression form

\[
 T_u=\frac1{4\pi^2}\int_0^1
       \{\operatorname{tr}(B_c\wedge F^t)
             -\operatorname{tr}B_c\wedge\operatorname{tr}F^t\}\,dt
\]

satisfies dT_u=c_2(F), and

\[
 |T_u|\le C\left(|F||\nabla_Au|+|\nabla_Au|^3\right).  \tag{4.7}
\]

Choose a smooth eta equal to zero below 1/2 and one above 1, with
|eta'|<=4, and put chi=(1-eta)^2. Then |chi'|<=8 and
(chi')^2/chi<=64 on {chi>0}. The form (1-chi(rho))T_u extends by
zero smoothly across Phi=0. Stokes' theorem therefore yields exactly

\[
 c_2(S^+)[M]=\int\chi(\rho)c_2(F)+\int d\chi(\rho)\wedge T_u.
                                                        \tag{4.8}
\]

On T, |nabla_Au|<=|nabla_A Phi|/sqrt(rho) and
|drho|<=2sqrt(rho)|nabla_A Phi|. The second integral is bounded by
C|chi'|[(G+|F_A-|)|nabla_A Phi|^2+|nabla_A Phi|^4] integrated over T.
Young's inequality bounds its F_A- part by

\[
 \frac{\chi|F_A^-|^2}{32\pi^2}
       +C\frac{(\chi')^2}{\chi}|\nabla_A\Phi|^4.
\]

The first term is absorbed by half the **negative** central contribution
in (4.4). The G term costs CG^2+C|nabla_A Phi|^4. Apply (4.5)--(4.6)
to all remaining curvature terms. This proves (4.3). QED.

**Corollary 6 (two distinct energy locations are compulsory).** Under
the hypothesis of Theorem 4, take epsilon_j=o(h_j). Then

\[
 \operatorname{Vol}(T_j)=o(A_jh_j),\qquad
 \int_{T_j}|\nabla_{A_j}\Phi_j|^2=o(A_jh_j),\qquad
 \int_{T_j}|\nabla_{A_j}\Phi_j|^4\ge cA_jh_j.            \tag{4.9}
\]

Indeed the first two statements follow from (2.1), (3.2), choosing
a=1<b<4/3. Since ell_j/(A_jh_j)->7/36, (4.3) gives the third. In
particular, with kappa including an arbitrarily small allowance,

\[
 \sup_{T_j}|\nabla_{A_j}\Phi_j|^2
       \ge\frac{c h_j}{\kappa_j+\epsilon_j}\longrightarrow\infty.
                                                        \tag{4.10}
\]

Thus a sublinear defect requires both the diffuse leading L2 projective
energy from (4.2) on normal-amplitude points and critical L4 concentration
in a small-amplitude transition layer. Neither a purely slow diffuse field
nor the negative determinant-curvature bulk term alone can account for it.
Here "diffuse leading L2" means the leading term is outside the declared
small-amplitude set; it does not assert uniform spatial equiintegrability
over every other set.

This is not yet a contradiction: the inherited global L4 budget permits
(4.9). Even ordinary equiintegrability with respect to dmu/V would give
only o(V), insufficient when the required charge is hV->0 relative to V.
Closing the linear bound needs control at the **hV scale**, or a direct
actual-equation exclusion of (4.9). No such control is silently added.

## 5. The topological quantities and the critical energy not yet controlled

For a Spin^c structure with determinant L and a=c_1(L), the splitting
principle gives

\[
 c_2(S^+)[M]=(a^2-T_+)/4,\quad
 c_2(S^-)[M]=(a^2+2\chi-3\tau)/4,
\]
\[
 c_2(S^-\otimes L)[M]
   =5\chi+6\tau+\tfrac94(a^2-T_+).                    \tag{5.1}
\]

Indeed twisting a rank-two bundle of first Chern class a by L increases
its second Chern class by 2a^2. These are identities, not energy-gap
theorems. With the manuscript curvature norms, Chern--Weil also gives

\[
 \frac{8\pi^2(5\chi+6\tau)}V
 =\fint(9|W^+|^2+|W^-|^2+5s^2/24-5|\operatorname{Ric}^\circ|^2/2)
 \ge10/3-(10/3)\sqrt r-(5/2)r.                         \tag{5.2}
\]

Armstrong's compact exact argument uses a nowhere-zero torsion section
to force the corresponding characteristic number to vanish. Equations
(5.1)--(5.2) provide the desired opposite inequality for actual inputs,
but the existence of an approximate torsion section alone does not force
vanishing. Its zeros and concentrated critical energy must be retained.
See [Armstrong, section 2.2.2](https://johnarmstrongmaths.com/publications/resources/thesis.pdf).

The actual estimates (3.2)--(3.4) remove concentration of the **first**
spinor derivative energy as an explanation for Theorem 4's leading term.
They do not prove uniform integrability of |nabla Phi|^4 or |nabla^2 Phi|^2,
nor any L4 bound for the derivative of a torsion section containing
nabla Phi. Those are different orders of information. The zero-end weak
gap and the linear small-h lower bound therefore remain open.

### 5.1 A polynomial opposite-spinor field and its weak Dirac equation

Let B=S^- tensor L, with the tensor-product connection; its determinant
connection is 3A. Define, without division by the spinor length,

\[
 t_\Phi=\sum_i c(e^i)\Phi\otimes(\Phi\wedge\nabla^A_i\Phi)
              \in\Gamma(B).                           \tag{5.3}
\]

The contraction is invariant under orthonormal-frame and unitary Spin^c
changes. It is smooth across the zero set of Phi. It is the candidate
suggested in the owner's execution brief; the following equation is a
further calculation, not an assertion supplied by the exact rigidity theorem.

**Proposition 7 (actual weak Dirac bridge at the zero endpoint).** For the
same weighted solution, put P_i=nabla_i Phi, w_i=Phi wedge P_i. In the
Clifford convention described below,

\[
 D^-_{3A}t_\Phi=-4\sum_i P_i\otimes w_i+\mathcal K,\qquad
 |\mathcal K|\le2|W^+||\Phi|^3.                       \tag{5.4}
\]

In particular, if beta_j->infinity, kappa_j->0 and a_j^2>=T_{+,j}, the
actual supplied solutions, with sufficiently small allowances, satisfy

\[
 \|t_{\Phi_j}\|_{L^4_{\rm avg}}+
 \|\nabla t_{\Phi_j}\|_{L^2_{\rm avg}}\le C,
 \quad \fint|t_{\Phi_j}|^2\longrightarrow128/81,
                                                        \tag{5.5}
\]
\[
 \boxed{\|D^-_{3A_j}t_{\Phi_j}\|_{L^q_{\rm avg}}
          \longrightarrow0\quad(1\le q<2).}            \tag{5.6}
\]

This produces an actual opposite-chirality twisted spinor with nonvanishing
mean mass and a vanishing weak Dirac residual. It is not a new monopole
solution: no curvature equation for its quadratic map has been established.

**Proof of the differential identity.** At a normal orthonormal frame,
the product rule for (5.3) splits into

\[
 Q=\sum_{ji}c_jc_i\{P_j\otimes w_i+
                       \Phi\otimes(P_j\wedge P_i)\},
 \quad H=\sum_{ji}c_jc_i\Phi\otimes(\Phi\wedge\nabla_jP_i).
\]

The two-dimensional determinant identity
Phi(P_j wedge P_i)=P_j w_i-P_i w_j and D_A Phi=0 give
Q=-4 sum_i P_i tensor w_i, using c_jc_i+c_ic_j=-2delta_ij.
The symmetric part of H is
Phi tensor(Phi wedge nabla^*nabla Phi), which vanishes because the
same weighted spinor equation makes nabla^*nabla Phi a scalar multiple
of Phi. The remaining part is exactly

\[
 \mathcal K=\tfrac12\sum_{ji}c_jc_i\Phi\otimes
                   (\Phi\wedge R^{S^+}_{ji}\Phi).       \tag{5.7}
\]

The central determinant-curvature term vanishes in the wedge. Clifford
action on S^+ annihilates the anti-self-dual first-pair component, so the
Ricci-off-diagonal block also disappears. For a real orthonormal basis
sigma_alpha of Lambda+, set J_alpha=c(sigma_alpha)/sqrt(2). The scalar
curvature term disappears by
sum_alpha J_alpha Phi tensor(Phi wedge J_alpha Phi)=0. With the convention
D_A^2=nabla^*nabla+s/4+c(F_A)/2, the remaining expression is

\[
 \mathcal K=-\sum_{\alpha\beta}W^+_{\alpha\beta}
                  J_\alpha\Phi\otimes(\Phi\wedge J_\beta\Phi).
\]

The matrix with columns J_alpha Phi has operator norm sqrt(2)|Phi|,
and the vector of wedges has norm sqrt(2)|Phi|^2. This proves (5.4).
Equivalently (5.7), whose sign does not depend on identifying a curvature
operator convention, can be used throughout.

Here are explicit pointwise checks of the remaining representation facts.
On S+->S-, take Clifford matrices

\[
 C_1=I,\quad C_2=\operatorname{diag}(i,-i),\quad
 C_3=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 C_4=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}.
\]

On S-->S+ use -C_i^*. Thus c(e12+e34)=-2i diag(1,-1) on S+.
At a nonzero spinor use a unitary frame Phi=sqrt(rho)u and write
nabla Phi=alpha u+beta v, nabla u=i gamma u+b v. In the notation
Omega=sqrt(2)psi/rho, differentiation gives

\[
 |\nabla\Omega|^2=8|b|^2,\quad |d\Omega|^2=8|b_L|^2,
 \quad |t_\Phi|^2=2\rho^3|b_N|^2
    =\frac{\rho^3}{4}(|\nabla\Omega|^2-|d\Omega|^2).
                                                        \tag{5.8}
\]

Here b_N is the component in ker[c(.)v] and b_L its Hermitian-orthogonal
complement. For closed Omega this is precisely the non-Kaehler intrinsic
torsion component, with the appropriate conjugate-bundle convention.
Thus (5.3) is not merely an arbitrary cubic field with the same Chern class.

Let zeta=<Phi,nabla Phi>, with the Hermitian pairing linear in its second
entry. The Dirac equation implies |beta_L|<=|alpha|. Each complex
isotropic subspace has beta_N dot beta_N=beta_L dot beta_L=0. Therefore

\[
 \left|\sum_iP_i\otimes w_i\right|^2
   =\rho(|\alpha\mathbin\cdot\beta|^2+|\beta\mathbin\cdot\beta|^2)
   \le5|\zeta|^2|\nabla\Phi|^2,\qquad
 \fint|\zeta|^2\le D_0/(4V).                          \tag{5.9}
\]

The last inequality follows from (3.3) and
|zeta|^2=|drho|^2/4+|gamma_original|^2. This notation distinguishes
gamma_original=Im<Phi,nabla Phi> from the normalized-frame gamma above.
The inherited bounded-spinor Hessian and fourth-power gradient estimates
are uniform when a^2>=T+ and kappa<=1. Directly differentiating (5.3)
then gives the bounds in (5.5). Holder and (5.4), (5.9) yield

\[
 \|D^-_{3A}t_\Phi\|_{L^{4/3}_{\rm avg}}
 \le2\|\Phi\|_\infty^3\|W^+\|_{L^2_{\rm avg}}
   +4\sqrt5\|\zeta\|_{L^2_{\rm avg}}
                     \|\nabla\Phi\|_{L^4_{\rm avg}}
 \le C(\sqrt\kappa+\beta^{-1})+o(1).                  \tag{5.10}
\]

The same expression is bounded in L2, since
|zeta|<=|Phi||nabla Phi|. Interpolation proves (5.6).
For the mass limit, (5.8) also gives

\[
 |t_\Phi|^2=\frac\rho2\left(|\nabla\psi|^2-|d\rho|^2
                -|d\psi-\rho^{-1}d\rho\wedge\psi|^2\right).
\]

Its difference from (rho/2)|nabla psi|^2 has absolute value bounded
by C(|drho|^2+|dpsi|^2), also through spinor zeros by the polynomial
identity and continuity. Its average is O(kappa). Now rho->4/3 in L2,
nabla psi is bounded in L4, and the previous Hodge computation gives
avg|nabla psi|^2->64/27. The mass limit is consequently 128/81. QED.

The remaining critical quantity is particularly explicit:

\[
 \|D^-_{3A}t_\Phi\|_{L^2_{\rm avg}}^2
 \le C\left(\fint|W^+|^2+
               \fint|\zeta|^2|\nabla_A\Phi|^2\right).   \tag{5.11}
\]

Existing L2 smallness of zeta and L4 boundedness of nabla Phi do not
make the product in (5.11) small. Nor does the mean mass limit make
t_Phi nowhere zero. Thus (5.6) is a weak Dirac bridge, not the claimed
zero-end exclusion or a characteristic-number vanishing theorem.

### 5.2 What the opposite-spinor topological argument must additionally pay

Writing the curvature of B=S^- tensor L as
F_B=Omega_-spin+(3/2)F_A I, the same conventions give

\[
 16\pi^2c_2(F_B)=\bigl(2|W^-|^2+s^2/24-|\operatorname{Ric}^\circ|^2/2
                     +9|F_A^+|^2-9|F_A^-|^2\bigr)d\mu,
\]
\[
 \|F_B\|_2^2=8\pi^2c_2(B)[M]+\tfrac12P+9\|F_A^-\|_2^2. \tag{5.12}
\]

At the zero endpoint, a^2>=T+ bounds avg|F_A-|^2 above by 2/9+o(1).
It does **not** bound avg|F_B|^2 universally, because c_2(B)/V,
equivalently the opposite Weyl energy, need not be bounded above.
The uniform bound in (5.5) concerns the derivative of a particular
section, not the curvature of its whole bundle.

For any smooth section t of a Hermitian rank-two bundle, the construction
of (4.7) applied to t/|t| and a cutoff in |t|/delta gives

\[
 |c_2(B)[M]|\le C\left(
    \int_{\{|t|<2\delta\}}|F_B|^2+
    \delta^{-4}\int_{\{\delta<|t|<2\delta\}}|\nabla t|^4\right).
                                                        \tag{5.13}
\]

For clarity, |dchi|<=C|nabla t|/delta and
|nabla(t/|t|)|<=C|nabla t|/delta on the transition layer; (4.7) and
Young's inequality give exactly (5.13). The cutoff is constant near
zeros, so no zero-set transversality is assumed. Formula (5.13) isolates
the missing terms rather than discarding boundary flux.

Under a^2>=T+ and r->0, (5.1)--(5.2) give
c_2(B)/V>=5/(12pi^2)+o(1). Hence decay of both terms in (5.13), divided
by V, would close the topological contradiction. Proposition 7 by itself
supplies neither: nabla t is bounded in L2, not L4, and W- may concentrate
where t is small. These facts distinguish the actual weak Dirac bridge
from an already completed weak-error rigidity theorem.

## 6. Scope correction for the inherited harmonic-zero example

The owner's new report correctly narrows its previous interpretation of
I37. In [the original proof](20260924_harmonic_zero_scale.md), lines
422--432, the scaled zero-circle construction explicitly has divergent
pointwise Ricci error and does not establish r+q->0. It cannot refute
automatic whole-core matching from the full near-Einstein PDE input.

In fact the particular nonzero-Ricci model fixed in that construction
gives a little more. On a fixed interior open set U of the model with
int_U|Ric(g_tilde)|^2>0, its exact rescaling g_rho=rho^2 g_tilde satisfies

\[
 \int_{\rho U}|\operatorname{Ric}(g_\rho)+g_\rho|^2
 =\int_U|\operatorname{Ric}(\widetilde g)+\rho^2\widetilde g|^2
 \longrightarrow\int_U|\operatorname{Ric}(\widetilde g)|^2>0.
\]

Since total volume tends to the fixed exterior volume, liminf r_rho>0.
This calculation concerns that chosen model, not every possible harmonic
zero construction. The original sufficient scale criterion remains valid;
its automatic derivation under complete PDE input remains an open problem.
