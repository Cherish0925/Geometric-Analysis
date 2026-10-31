# Linear Einstein separation at the small-surgery boundary

27 September 2026. Continues [the actual-cost proof](20260926_actual_topological_cost.md),
commit `168bea5`. The [new web contribution](../guidance/source/20260927_web_critical_mixed_term.zh.md)
is preserved verbatim. **The main result is proved in Sections 4--5:** a
refined same-spinor Hessian estimate closes the beta=2 weak-Bianchi
bootstrap, gives linear topological cost, and determines the order of the
relative Einstein defect on the previously constructed small-h family.
Sections 1--3 below incorporate the web note's mixed-current
estimate, model cancellation and curvature identity, with explicit attribution;
they are not claimed as newly discovered here. Subsequent sections record
further proof work. All actual-solvability hypotheses remain those of the
inherited functional pencil. No conjectured linear gap is a premise. The
zero-Weyl endpoint and general Einstein realization remain separate problems.

For precision, the actual input on a closed connected oriented smooth
four-manifold (M,g) is a Spin^c structure whose unperturbed Seiberg--Witten
equations are solvable for every metric conformal to g. Its real Chern
class a is fixed throughout the auxiliary weights; it may be selected
anew when the original metric changes. Put

\[
 p=(a_g^+)^2>0,\quad r=V^{-1}\int|\operatorname{Ric}+g|^2,\quad
 D_2=\frac32\int(s^2+12|W^+|^2)-72\pi^2p\ge0.
\]

Norms and the rescaled equations are those of the
[functional pencil](../mathematics/current/line1_functional_pencil.md),
Sections 1--3. There is no diameter, noncollapse, Sobolev, injectivity-radius
or full-curvature assumption. The new beta=2 proof uses the supplied
actual-field estimates, not an arbitrary approximately closed form.

Write rho=|Phi|^2, zeta=<Phi,nabla_A Phi>, with the Hermitian pairing linear
in its second entry, P=nabla_A Phi, and Theta=(kappa+epsilon)V. Curvature
two-form norms use sum_{i<j}|F_ij|_HS^2. The selectable smoothing error epsilon
belongs to one actual weighted solution, not a comparison of two solutions.

## 1. The full rank-two transgression and the mixed bound

On {rho>0}, use u=Phi/sqrt(rho) and a local unitary complement v. In this
frame let the connection matrix and the connection fixing u be

\[
 \mathcal A=\begin{pmatrix}a&-\bar b\\b&d\end{pmatrix},
 \qquad \mathcal A^0=\begin{pmatrix}0&0\\0&d\end{pmatrix}.
\]

Here a is an imaginary one-form, not the topological class. Set
B_c=mathcal A-mathcal A^0 and F^t the curvature of mathcal A^0+tB_c.
The global transgression on the nonzero set is

\[
 T_u=\frac1{4\pi^2}\int_0^1
 [\operatorname{tr}(B_c\wedge F^t)
       -\operatorname{tr}B_c\wedge\operatorname{tr}F^t]dt,
 \qquad dT_u=c_2(F).
\]

The web note's exact expansion is

\[
 4\pi^2T_u=-a\wedge F_{22}
 +\tfrac12(b\wedge F_{12}-\bar b\wedge F_{21})
 +a\wedge\bar b\wedge b.                         \tag{1.1}
\]

Indeed F^0_22=F_22-bar b wedge b, and
F^t=(1-t)F^0+tF-t(1-t)B_c wedge B_c; substitution and integration in t
give (1.1). This calculation retains the matrix order and wedge signs.
The expression is invariant under changing v by a unit complex scalar.

For beta=2 put T={1/2<rho<1}. On T,

\[
 \zeta=\tfrac12d\rho+\rho a,\quad
 |d\rho|\le2|\zeta|,\quad |a|\le2|\zeta|,
 \quad |b|\le\sqrt2|P|.                             \tag{1.2}
\]

Choose chi=(1-eta)^2 with eta=0 below 1/2, eta=1 above 1 and |eta'|<=4.
The inherited signed identity and the zero-set extension give

\[
 c_2(S^+)[M]=\int\chi c_2(F)+\int d\chi\wedge T_u,
 \quad
 16\pi^2c_2(F)=
 (|F_A^+|^2-|F_A^-|^2-2|\Omega^+|^2+2|\Omega^-|^2)d\mu.
                                                               \tag{1.3}
\]

Let G^2=|Omega|^2+|F_A^+|^2. The actual estimates already give
int_{rho<=1}G^2<=CTheta and the same bound for the positive part in (1.3).
Since off-diagonal curvature has no central part, (1.1) yields

\[
 |d\chi\wedge T_u|\le C|\chi'|
 (G|\zeta||P|+|F_A^-||\zeta|^2+|\zeta|^2|P|^2).
\]

Young's inequality controls the central term by
chi|F_A^-|^2/(32pi^2)+C(chi')^2|zeta|^4/chi. The first summand is
absorbed by the negative term in (1.3). The ratio (chi')^2/chi<=64 and
|zeta|^2<=rho|P|^2<=|P|^2 on T control the second. Consequently:

**Proposition 1 (web mixed-current refinement).**

\[
 \boxed{c_2(S^+)[M]\le C\Theta+C\int_T|\zeta|^2|P|^2.} \tag{1.4}
\]

In the exact small-h family of the preceding continuation, any E=o(h)
therefore requires int_T|zeta|^2|P|^2>=cAh. This is stronger than the
coarser quartic concentration criterion, but does not exclude that concentration.

There is a further exact simplification useful for retaining the sign.
Since F_11=da-bar b wedge b and tr F=F_A,

\[
 \boxed{4\pi^2T_u=a\wedge da-a\wedge F_A
 +\tfrac12(b\wedge F_{12}-\bar b\wedge F_{21}).}       \tag{1.5}
\]

In particular the two diagonal terms in the cutoff flux are exactly

\[
 \frac{\chi'(\rho)}{\rho^2}d\rho\wedge\zeta\wedge d\zeta
 -\frac{\chi'(\rho)}\rho d\rho\wedge\zeta\wedge F_A.  \tag{1.6}
\]

The real exact part of zeta drops out after wedging with d rho. Formula
(1.6) is signed; its first term is not asserted nonpositive. Replacing it
by its absolute value loses the current's phase/radial correlation.

## 2. Axial model cancellation in the actual torsion equation

Keep the globally smooth cubic field

\[
 t_\Phi=\sum_i c(e^i)\Phi\otimes(\Phi\wedge P_i)\in S^-\otimes L.
\]

The preceding exact calculation gives
D^-_{3A}t_Phi=-4 sum_i P_i tensor(Phi wedge P_i)+mathcal K(W^+,Phi).
For the actual axial model W_0=A_{omega,1/beta}, the web note observes

\[
 \mathcal K(W_0,\Phi)=0.                              \tag{2.1}
\]

To verify this, at Phi!=0 choose J_1 Phi=iPhi. Its wedge factor is zero.
The other model eigenvalues coincide and J_3 Phi=+/-iJ_2 Phi, so the
other tensor factors cancel by 1+i^2=0. At Phi=0 the polynomial vanishes.
Thus throughout the actual finite-parameter range

\[
 D^-_{3A}t_\Phi=-4\sum_i P_i\otimes(\Phi\wedge P_i)
       +\mathcal K(W^+-W_0,\Phi).                     \tag{2.2}
\]

With the inherited uniform Hessian budget (in particular a^2>=T_+),
and kappa<=1 with a sufficiently small chosen epsilon,

\[
 \|D^-_{3A}t_\Phi\|_{4/3,\mathrm{avg}}
       \le C\sqrt{\kappa+\varepsilon},\qquad
 \|D^-_{3A}t_\Phi\|_{2,\mathrm{avg}}^2
       \le C\left(\kappa+\varepsilon+\fint|\zeta|^2|P|^2\right).
                                                               \tag{2.3}
\]

Unlike the previous coarse estimate, (2.3) has no beta^{-1} term.
It does not assert nonzero torsion at the KE endpoint.

The mass calculation also has an all-parameter form. Write
q_beta=4(1+1/beta), rho_beta=2sqrt(q_beta)/3 and
U_beta=(4/3)(2/beta-1). The previous identities give, uniformly,

\[
 \boxed{\fint|t_\Phi|^2
 =\frac{16q_\beta^{3/2}}{81}(1-2/\beta)
       +O(\sqrt{\kappa+\varepsilon}).}                \tag{2.4}
\]

Indeed |t|^2 differs from (rho/2)|nabla psi|^2 by an integrable error
O(Theta); replacing rho by rho_beta costs O(sqrt(kappa+epsilon)) in
the average, using the L4 gradient budget. Also
avg|nabla psi|^2=4rho_beta K_A/V+O(sqrt(kappa+epsilon)), and
K_A/V=-U_beta rho_beta/4+O(sqrt(kappa+epsilon)). Their product is
-U_beta rho_beta^3/2, which is (2.4). The zero-end value is 128/81,
whereas the exact beta=2 leading term is zero.

## 3. The additional actual curvature equation and its sign

The web note supplies a further equation, not an ordinary new monopole.
Use the imaginary-valued quadratic map q_- such that
c(q_-(t))t=(|t|^2/2)t. Then

\[
 \rho^3F_A^-+2q_-(t_\Phi)=2\rho^2(d\zeta)^-+\mathcal R,
 \quad
 |\mathcal R|\le C\left(\rho^3|\operatorname{Ric}^\circ|
                  +\rho^{3/2}|\zeta||P|\right).       \tag{3.1}
\]

Here is a pointwise normalization check and derivation. On rho>0 write
Phi=sqrt(rho)u, P=alpha u+beta v, alpha=zeta/sqrt(rho).
Decompose beta=beta_N+beta_L using the kernel of c(.)v. The Dirac
equation gives |beta_L|<=|alpha|. In the Clifford matrices of the previous
proof this kernel consists of beta_N=(iz,z,iw,w), with
t=2i rho(z,-w) on the kernel part. Directly,
q_-(t)=rho^2(bar beta_N wedge beta_N)^-.

Now use
(d zeta)_ij=<P_i,P_j>-<P_j,P_i>+<Phi,F^S+_ij Phi>.
The anti-self-dual central curvature contributes rho F_A^-/2 and the
traceless contribution is bounded by C rho|Ric^circ|. All terms in
bar beta wedge beta-bar beta_N wedge beta_N, and in bar alpha wedge alpha,
are bounded by C|alpha||P|. Multiplication by 2rho^2 gives (3.1).
Both sides extend polynomially through zeros; the bound extends by continuity.

For completeness the same scalar-potential spinor equation also gives

\[
 \delta\zeta=-|P|^2-U\rho/4,\qquad
 \delta\operatorname{Im}\zeta=0,\qquad
 \Delta\rho=-2|P|^2-U\rho/2.                         \tag{3.2}
\]

The Laplacian convention is Delta=d*d>=0. The first equation follows by
differentiating <Phi,P> and using nabla* nabla Phi=-U Phi/4.
These are additional actual equations, not independent free fields.

The derivative term in (3.1) can be written
rho^2 d zeta=d(rho^2 zeta)-2rho d rho wedge zeta. Its first part is the
derivative of a small L2 field, the second is small in L1. This does not
justify testing by an uncontrolled derivative of q_-(t).

Even a vanishing L2 Dirac residual would not finish the argument:

\[
 \int|D^-_{3A}t|^2=\int|\nabla t|^2+\int(s/4)|t|^2
       +\tfrac32\int\langle c(F_A^-)t,t\rangle.       \tag{3.3}
\]

The scalar term is negative here. The sign in (3.1) is opposite the
ordinary monopole sign. In particular no positive vanishing theorem is
being invoked. Actual U(1)-twisted Dirac modes on Eguchi--Hanson space are
also known; see [Franchetti--Krasnov](https://arxiv.org/abs/2309.08453).

## 4. Removing the background volume from the second-order budget

This is the decisive new step. The previous coarse Hessian estimate paid
O(V) for all background curvature. At beta=2 the bounded KE curvature
model annihilates the distinguished spinor at its calibrated amplitude.
Keeping this fact in the exact Hessian identity, and then using the
existing weak-Bianchi self-test again, closes the remaining estimate.

We distinguish the spinor gradient P_i from the scalar Ricci energy
P_Ric=int|Ric^circ|^2. Set

\[
 T_+=2\chi+3\tau,\quad p=(a_g^+)^2,\quad
 K=\int|\nabla_A\Phi|^2,\quad B=\int|F_A^-|^2,
 \quad \Xi=rV+D_2,\quad\Theta=\Xi+\varepsilon V.
\]

The actual beta=2 supplied solution satisfies, with universal constants,

\[
 |\Phi|\le2,\quad \rho_0=4/\sqrt6,\quad c=\sqrt6,
\]
\[
 \int\bigl((\rho-\rho_0)^2+(f-c)^2+U^2+|d\rho|^2
       +|\operatorname{Im}\zeta|^2+|W^+-W_0|^2
       +|\operatorname{Ric}+g|^2\bigr)\le C\Theta,
 \quad J_+\le C\Theta.                              \tag{4.1}
\]

Here U=s+f rho, W_0=A_{omega,1/2}, omega=sqrt(3)psi/2. These are
the inherited estimates, with their exact same-solution quantifiers,
collected in Sections 1--3 of the preceding actual-cost proof. Its
localized equation and remainder identity also give

\[
 \int_{\{\rho\le1\}}|\nabla_A\Phi|^2\le C\Theta,
 \qquad |8\sqrt6 K-\Sigma|\le C\Theta.               \tag{4.2}
\]

### 4.1 A refined Hessian lemma

**Lemma 2.** The same solution obeys

\[
 \boxed{\int\bigl(|\nabla_A^2\Phi|^2+|\nabla_A\Phi|^4\bigr)
               \le C(K+\Theta+B).}                  \tag{4.3}
\]

**Proof.** Form an algebraic positive-spinor curvature F_b using
s_b=-4, Ric_b^circ=0, W_b^+=W_0, F_{A,b}^+=i c sigma(Phi),
and F_{A,b}^-=0. It need not itself be the curvature of a connection;
it is used only algebraically inside the actual Hessian identity.
Since Phi is bounded, |F_b|<=C, and (4.1) gives

\[
 \|F^{S^+}-F_b\|_2^2\le C(\Theta+B).                \tag{4.4}
\]

The more important bound is

\[
                  |F_b\Phi|^2\le C(\rho-\rho_0)^2.  \tag{4.5}
\]

For an explicit check choose the self-dual basis along psi. W_0 has
eigenvalues -rho^2/4,rho^2/8,rho^2/8. With the Clifford/curvature
conventions of the supplied equations, the axis and transverse
coefficients of F_b Phi, up to their common fixed normalizations, are

\[
 \rho^2/4+1/3-c\rho/4
     =\tfrac14(\rho-4/\sqrt6)(\rho-2/\sqrt6),
 \qquad
 \rho^2/8-1/3
     =\tfrac18(\rho-4/\sqrt6)(\rho+4/\sqrt6).
\]

They vanish at rho_0; bounded rho proves (4.5), including zeros.
Equivalently one can split off the unit-amplitude KE model on the nonzero
set, which annihilates Phi exactly. No derivative of either model is
used in this step.

Put H=nabla_A^2 Phi and L=tr H. The exact covariant identity is

\[
 \|H\|_2^2=\|L\|_2^2
 -\int\operatorname{Ric}_{ij}\operatorname{Re}\langle P_i,P_j\rangle
 +\sum_{ij}\int\operatorname{Re}\langle F_{ij}^{S^+}P_j,P_i\rangle
 +\tfrac12\sum_{ij}\|F_{ij}^{S^+}\Phi\|_2^2.         \tag{4.6}
\]

The sums in (4.6) are double sums; their norms differ by a fixed factor
from the exterior-curvature norm used elsewhere. The identity follows
by interchanging Hessian slots before commuting on P. It differentiates
neither curvature nor f. Bounded-section integration by parts also gives
||P||_4^2<=8||H||_2. Now ||L||_2^2<=CTheta by the actual spinor
equation. Split Ric=-g+(Ric+g), and F=F_b+(F-F_b). The bounded
background terms cost CK, the error terms cost
C sqrt(Theta+B)||H||_2, and (4.4)--(4.5) give
||F Phi||_2^2<=C(Theta+B). Thus

\[
 \|H\|_2^2\le C(K+\Theta+B)
                 +C\sqrt{\Theta+B}\,\|H\|_2.
\]

Young's inequality and the bounded-section interpolation prove (4.3).
There is no additive V term. QED.

### 4.2 The square condition absorbs the remaining determinant energy

Assume a^2>=T_+. The determinant and Chern--Weil identities, with all
constants retained, are

\[
 B=4\pi^2(p-a^2)+J_+,
 \qquad
 36\pi^2(p-T_+)=\tfrac92P_{\rm Ric}+\tfrac98\Sigma-D_2.
                                                               \tag{4.7}
\]

Consequently

\[
 B\le\tfrac12P_{\rm Ric}+\tfrac18\Sigma-D_2/9+J_+
       \le\sqrt6 K+C\Theta.                          \tag{4.8}
\]

This is not a smallness assumption on B: it bounds B by the unknown
spinor energy that the next self-test will absorb. We used
P_Ric<=rV, D_2>=0 and (4.1)--(4.2). Thus (4.3) improves to

\[
             \|H\|_2^2+\|P\|_4^4\le C(K+\Theta).   \tag{4.9}
\]

### 4.3 Closing the weak-Bianchi bootstrap

Let J=div W(W_0), where W(W_0) is the Weyl four-tensor corresponding
to the smooth polynomial W_0. The inherited weak contracted Bianchi
identity gives

\[
 \|J\|_2^2\le C\sqrt\Theta\,\|\nabla J\|_2.
\]

W_0 is a parallel polynomial of degree four in bounded Phi. Consequently
|nabla J|<=C|nabla^2 W_0| and (4.9) give

\[
                    \|J\|_2^2\le C\sqrt{\Theta(K+\Theta)}.
                                                               \tag{4.10}
\]

No commutation of these derivatives, and hence no new full-curvature
term, is needed. The same actual J is the test field.

The pointwise polynomial divergence identity from the existing
[bounded-form criterion](../mathematics/current/round21_analytic.md),
Section 6, with t=1/2 and v=|omega|^2=3rho^2/4, gives

\[
 \tfrac14 v(|\nabla\omega|^2+|d\omega|^2)
       \le |J|^2+\tfrac13|dv|^2.                     \tag{4.11}
\]

On {rho>1}, use
|nabla omega|^2=3rho|P|^2-3|Im zeta|^2 and
dv=(3/2)rho d rho. Equations (4.1), (4.2), (4.11) yield

\[
                       K\le C(\Theta+\|J\|_2^2).    \tag{4.12}
\]

The low-amplitude integral in (4.2) is essential: we did not divide by
rho at its zeros. Combining (4.10)--(4.12) and applying Young once more,

\[
 K\le C\Theta+C\sqrt{\Theta K}\quad\Longrightarrow\quad
                         \boxed{K\le C\Theta.}       \tag{4.13}
\]

This proves the mixed-term smallness sought in the web brief as a
consequence of the original self-test with a sharper budget, rather than
an assumed regularity theorem for the mixed term itself.

**Theorem 3 (linear beta=2 cost).** Under the inherited actual conformal
monopole hypotheses, p>0 and a^2>=T_+, every normalized metric with
kappa=r+D_2/V<=1 has supplied smooth solutions with any sufficiently
small chosen allowance epsilon, for which

\[
 K+B+\int(|\nabla_A^2\Phi|^2+|\nabla_A\Phi|^4)
             +\int|\zeta|^2|\nabla_A\Phi|^2\le C\Theta. 
                                                               \tag{4.14}
\]

Moreover, the solution-independent quantities satisfy

\[
 \boxed{0\le\Sigma\le C(rV+D_2),\qquad
         0\le p-T_+\le C_T(rV+D_2).}                 \tag{4.15}
\]

The nonnegative scalar slack follows from the classical scalar estimate;
p>=a^2>=T_+. Bounds (4.8), (4.9), (4.13) and |zeta|<=2|P| prove
(4.14). Equations (4.2), (4.7) prove (4.15) after letting epsilon tend
to zero on the fixed metric and class. No convergence of the actual
solutions is asserted or needed. In particular,

\[
                     c_2(S^+)[M]\le C(rV+D_2).       \tag{4.16}
\]

For the transition set, (4.14) gives int_T|zeta|^2|P|^2<=CTheta.
Choosing epsilon=o(h) proves the web brief's required o(hV) bound when
kappa=o(h). This now contradicts the positive-charge necessity (1.4).

The theorem controls rV, including scalar variance and normalization
error; it does **not** assert the stronger unproved inequality
Sigma<=C(P_Ric+D_2).

A square-cost variant also follows from the same proof. Retain Theorem 3's
hypotheses except a^2>=T_+. If
Y=(T_+-a^2)_+, replace (4.8) by B<=sqrt6 K+CTheta+4pi^2Y. Then

\[
 K+\Sigma+(p-T_+)_+\le C(\Theta+\sqrt{\Theta Y}),
 \quad
 B+\|\nabla_A^2\Phi\|_2^2+\|\nabla_A\Phi\|_4^4
                   \le C(\Theta+Y).                 \tag{4.17}
\]

The mixed term is controlled by the second, not the first, bound in
(4.17). Thus a square shortfall remains a genuine cost. No such cost
appears in (4.14)--(4.16).

### 4.4 Transfer to parameters near the KE endpoint

This transfer uses no new field or gauge hypothesis. For 2<=beta<=3 let
delta=beta-2 and Xi_beta=rV+D_beta. The exact deficit decomposition
D_beta=A_0+beta^(-1)int z^2, where z=s+beta w and
A_0=Delta_++int q_-^2>=0, gives

\[
 D_2=A_0+\tfrac12\int(z-\delta w)^2
       \le\beta D_\beta+\delta^2\int w^2.
\]

Since w=(z-(s+4)+4)/beta, two applications of the squared triangle
inequality give

\[
 \int w^2\le\frac4\beta D_\beta+
                \frac{16}{\beta^2}rV+\frac{32}{\beta^2}V
             \le2D_\beta+4rV+8V.
\]

Consequently

\[
                    \Xi_2\le5\Xi_\beta+8(\beta-2)^2V. \tag{4.18}
\]

Whenever kappa_2<=1, Theorem 3 controls all its spinor quantities by
C[Xi_beta+(beta-2)^2V+epsilon V]. The majorant
f_0=max(sqrt(max(-s+w,3)),(-s)_+/4) does not depend on beta, so the
same smooth majorants and actual solutions serve this comparison.
This is a nearby-parameter corollary, not an estimate at beta->infinity.

## 5. A linear two-chirality gap and the optimal small-h order

Assume that for every smooth metric on M one can choose a single actual
conformally solvable Spin^c structure with

\[
 p\ge A>0,\quad a^2\ge T_+=A(1-h),\quad 0<h\le1/3.
\]

As before put

\[
 U=\frac{3\min(T_+,T_-)}A,\quad
 e=\frac{R}{8\pi^2A},\quad R=\int|\operatorname{Ric}|^2,
 \quad\mathcal E=\inf_{\lambda\ne0}
       \frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V}.
\]

**Theorem 4 (linear topological window).** There is a universal c>0
such that every smooth metric under these hypotheses satisfies

\[
              \boxed{\mathcal E+(U-1-h)_+\ge c h.}    \tag{5.1}
\]

**Proof.** R>0 by the positive actual scalar budget. If U<=0,
e(1-E)<=U gives E>=1 and the conclusion is immediate. Otherwise U<=3.
Set Delta=(U-1-h)_+. If E+Delta>=1/49, then E+Delta>=(3/49)h.
It remains to consider the smaller branch, in particular E<1/2.

Let I=int s. If I>=0, the negative scalar estimate gives
32pi^2A<=int s_-^2<=L_s<=RE, so 4<=eE. Combining with
e(1-E)<=U gives E>=4/(U+4)>=4/7, a contradiction. Thus I<0.
Rescale by -R/I so that r=E and V=R/(4-E); p,D_2,R,P_Ric
are unchanged. Write z=p/A-1>=0. The exact identity is

\[
          D_2/A=36\pi^2[e-(1+h)-2z].                 \tag{5.2}
\]

Hence e>=1+h, e<=U/(1-E)<=6, and

\[
 D_2/A\le72\pi^2\Delta+96\pi^2E,\quad
 rV/A=\frac{8\pi^2eE}{4-E}\le\frac{96}{7}\pi^2E.
\]

Also A/V=(4-E)/(8pi^2e)<=1/(2pi^2). Thus

\[
 \Xi/A\le112\pi^2(E+\Delta),\qquad
 \kappa\le49(E+\Delta)<1.                            \tag{5.3}
\]

The second bound in (5.3) follows directly from r=E and
D_2/V<=36Delta+48E, not from the coarser first bound alone.
Now p-T_+>=Ah and Theorem 3 give
h<=C_T Xi/A<=112pi^2 C_T(E+Delta). Take
c=min(3/49,1/(112pi^2 C_T)). This is independent of topology, volume,
class choice and metric. QED.

This uses the same chiral upper budget as the preceding h^2 theorem.
Its new content comes from (4.15), not from a new Chern--Weil identity.
The old optimized F(h) inequality remains valid; (5.1) supplies a
linear-width exclusion near the classical Ricci-energy boundary 1+h.
It is not a claim that (5.1) dominates every previous inequality at
every parameter value.

**Corollary 5 (sharp order on the realized family).** On the exact
complex-hyperbolic-cover blowup/handle family constructed in Section 3,
Theorem 5 of
[the boundary continuation](20260926_boundary_compatibility.md),

\[
 \boxed{c_1h_j\le\inf_g\mathcal E(g)
                   \le\frac{4h_j}{1+h_j}\le4h_j}
                  \qquad\text{for all sufficiently large }j. \tag{5.4}
\]

Indeed U_j-F(h_j)=o(h_j^2), and
F(h)-1-h=4h^2/(1+sqrt(1-3h))^2. Therefore
(U_j-1-h_j)_+=O(h_j^2); absorb it into ch_j/2 in (5.1).
The upper bound is the previously established consequence of LeBrun's
actual shrinking-core construction, not a new gluing theorem. Thus the
optimal **order** on this family is linear. The optimal leading constant
over all metrics has not been determined.

Combining E<=4delta_sigma^2 with (5.4) yields delta_sigma>=c sqrt(h)
on this family for either sign. This is a pointwise-input obstruction,
not a pointwise near-Einstein construction or a full solution of Yau26.

There is also a more informative feasible-frontier consequence. On the
optimally negative-normalized branch with kappa<=1, set
alpha=(36pi^2 C_T)^(-1). From p-T_+=A(h+z) and (4.15),

\[
 e\left(1+\frac{2\mathcal E}{9(4-\mathcal E)}\right)
 \ge 1+(1+\alpha)h+(2+\alpha)z,\qquad z=p/A-1\ge0.
                                                               \tag{5.5}
\]

For E<1, combining with e(1-E)<=U gives

\[
 U\ge\frac{(1-\mathcal E)[1+(1+\alpha)h]}
                 {1+2\mathcal E/[9(4-\mathcal E)]}.  \tag{5.6}
\]

These formulas use precisely the same hypotheses as the small-kappa
branch, not arbitrary metrics with uncontrolled D_2/V. In particular,
at an exact negative Einstein metric in that branch they force
U>=1+(1+alpha)h. The all-metric statement remains (5.1), whose separate
large-defect branch supplies the needed global quantifier.

### 5.1 Relaxing the class-square hypothesis without losing the order

The square-cost estimate (4.17) gives a genuine scope extension. Retain
the hypotheses of Theorem 4 except a^2>=T_+, and, for the actual class
selected at g, put y=(T_+-a^2)_+/A. Then

\[
 \boxed{\mathcal E(g)+(U-1-h)_+\ge c\frac{h^2}{h+y}.} \tag{5.7}
\]

To prove it, the negative-average and rescaling arguments of Theorem 4
use p>=A, not the class-square condition. In the small branch let
x=Xi/A. Since p-T_+>=Ah, (4.17), with epsilon sent to zero, gives
h<=C(x+sqrt(xy)). If x<=h, squaring gives
h^2<=2C^2 x(x+y)<=2C^2 x(h+y). If x>h, then
x>h>=h^2/(h+y). Combine with x<=112pi^2(E+Delta).
In the large branch use h^2/(h+y)<=h<=1/3. This proves (5.7)
with a universal positive constant.

In particular a metricwise actual supply with
(T_+-a^2)_+<=L A h, for a fixed L>=0, still gives

\[
               \mathcal E(g)+(U-1-h)_+\ge c h/(1+L). \tag{5.8}
\]

This replaces the exact square inequality by a controlled shortfall at
the surgery scale. It does not assert the existence of any additional
gauge supplier. The realized family of Corollary 5 has y=0.

## 6. Construction-side scope: inverse-surgery curvature costs

The parallel construction analysis gives a separate geometric explanation
of why local insertion alone cannot beat the linear order. It is not used
to prove Theorem 3.

Let N be a common oriented exterior in M and X, where T_+(X)=A and
T_+(M)=A(1-h). Suppose a smooth metric ghat on X agrees with g on N.
Write C_X=X\\N, C_M=M\\N and H_g=s_g^2/24+2|W_g^+|^2. Global
Chern--Weil on the two closed manifolds gives the exact identity

\[
 P_M=P_X+2\int_{C_M}H_g-2\int_{C_X}H_{\widehat g}
                              +8\pi^2Ah.             \tag{6.1}
\]

Every term other than the cap energy has the displayed favorable sign.
Let gamma=(4pi^2A)^{-1}int_{C_X}H_ghat and b=4(h-gamma)_+.
For U>0 the chiral upper bound consequently gives

\[
                         \mathcal E(g)\ge\frac b{U+b}.
                                                               \tag{6.2}
\]

For E<1 this follows from E>=4P_M/R>=b/e and e(1-E)<=U;
E>=1 is immediate. No closeness to a complex-hyperbolic exterior is
assumed. Thus low-energy inverse-surgery caps with energy o(Ah) would
force liminf E/h>=4 when h->0 and U->1. Conversely every such replacement of
a hypothetical sublinear metric would have to cost at least
4pi^2Ah-o(Ah). The main theorem now excludes that sublinear case in
the stated gauge/window family independently of the existence of caps.

Here is an explicit sufficient geometric criterion for cheap caps.
On disjoint spherical collars suppose, in coordinates at arbitrary
scales ell_i, g=ell_i^2(delta+q_i), with ||q_i||_{C^2(1<|x|<2)}
<=epsilon_i<=epsilon_0. A fixed radial cutoff which is zero for
r<=5/4 and one for r>=7/4 extends the metric to a Euclidean inner
ball, unchanged at the exterior. The scaled curvature is O(epsilon_i),
volume is bounded, and dimension-four scaling cancels; hence

\[
                         \int_{\mathrm{cap}_i}H\le C\epsilon_i^2.
                                                               \tag{6.3}
\]

Thus sum epsilon_i^2=o(Ah) suffices, even with unbounded numbers of
collars and arbitrarily small individual scales. An exactly unchanged
normalized complex-hyperbolic exterior outside removed volume v has
cap energy 2v, since H_CH=2. The classical shrinking-core upper sequence
lies in this class: choose its gluing scales diagonally so that the
defect approximation error is o(h_j) and cap energy is o(A_jh_j).
It then matches coefficient 4 asymptotically as h_j->0. This proves
coefficient sharpness **within that replacement class**, not among all
metrics on M.

Actual spinor budgets alone were not shown to produce these C2 collars:
they do not control the full opposite Weyl curvature or injectivity radius.
No such geometric conclusion is needed for the weak-Bianchi proof above.

## 7. Retaining the signed current: an independent exact identity

This records the parallel flux route without presenting it as a second
proof of Theorem 3. Let Gamma=Im zeta and F_A=iF, with F real and closed.
Use the cutoff chi of Section 1, and define, for rho<1,

\[
 B_\chi(\rho)=-\int_\rho^1\frac{\chi'(t)}{t^2}dt,
 \qquad C_\chi(\rho)=-\int_\rho^1\frac{\chi'(t)}t dt.
\]

Both functions are constant below 1/2 and zero above 1. Cauchy--Schwarz
against the positive measure -chi'(t)dt proves C_chi^2<=chi B_chi.
Their derivatives are chi'/rho^2 and chi'/rho, respectively. On the
closed manifold, (1.6) integrates to
int[B_chi dGamma wedge dGamma-C_chi dGamma wedge F]. Combining with
the central curvature in (1.3) and completing a square gives

\[
\begin{split}
16\pi^2c_2(S^+)[M]=\int\bigl[&4B_\chi(|Z^+|^2-|Z^-|^2)
 +\lambda(|F^+|^2-|F^-|^2)\\
 &+2\chi(|\Omega^-|^2-|\Omega^+|^2)\bigr]d\mu+R_{\rm off},
\end{split}                                                     \tag{7.1}
\]

where Z=dGamma-C_chi F/(2B_chi), lambda=chi-C_chi^2/B_chi>=0 and
R_off=2int chi' d rho wedge(b wedge F12-bar b wedge F21).
Where B_chi=0 all weighted terms are defined by their continuous limit;
C_chi=chi=0 there. The identity extends through spinor zeros because
Gamma is globally smooth and the weights are constant near rho=0;
the off-diagonal expression is supported away from those zeros.

The central anti-self-dual terms in (7.1) have nonpositive sign. This
does not make the full topological flux nonpositive: its self-dual
current energy remains. The new estimate (4.14), however, now bounds
that current on the beta=2 square-controlled branch. Indeed
dGamma is the sum of a quadratic spinor-gradient term and
Im<Phi,F^{S+}Phi>; (4.4)--(4.5), (4.8) and (4.14) bound its L2
energy by CTheta. Thus the signed identity is consistent with the
linear positive-charge bound; it supplies no independent zero-end
vanishing theorem.

## 8. Continuing the zero-end system: torsion length and a coupled balance

This section continues the zero-end problem after the linear theorem.
All norms here are normalized by V. Assume the inherited actual supply
with a^2>=T_+, beta>=4, and eta=kappa+epsilon<=1. Write
P=nabla_A Phi, H=nabla_A P, t=t_Phi and m=|t|^2. Its uniform budget gives

\[
 \|P\|_4+\|H\|_2+\|t\|_4+\|\nabla t\|_2\le C,\quad
 \|\zeta\|_2+\|d\rho\|_2\le C\sqrt\eta,
\]
\[
 \|\rho-\rho_\beta\|_2+\|U-U_\beta\|_2
 +\|s+4\|_2+\|\operatorname{Ric}^{\circ}\|_2\le C\sqrt\eta,
\]

where rho_beta and U_beta are as in Section2. Set

\[
 m_\beta=-U_\beta\rho_\beta^3/2
 =\frac{16[4(1+1/\beta)]^{3/2}}{81}(1-2/\beta),\quad
 S=m_\beta+2\rho^2|P|^2,\qquad u=t/\sqrt S.            \tag{8.1}
\]

For beta>=4, m_beta has uniform positive lower and upper bounds.
All these fields are globally smooth, including at spinor zeros.
The pointwise Dirac-compatible decomposition used in Section3 gives

\[
       0\le d:=2\rho^2|P|^2-m\le4\rho|\zeta|^2.      \tag{8.2}
\]

Indeed write P=alpha v_1+gamma_N v_2+gamma_L v_2 using the orthogonal
kernel decomposition there. Then m=2rho^2|gamma_N|^2,
|gamma_L|<=|alpha| and |alpha|^2=|zeta|^2/rho. The inequality extends
through zeros. Thus S=m_beta+m+d, |u|<=1, and avg d<=C eta.
The inherited fourth-order and same-solution mass estimates imply

\[
 \fint S=2m_\beta+O(\sqrt\eta),\qquad \fint S^2\le C. \tag{8.3}
\]

**Proposition 6 (actual torsion-length concentration).** Uniformly under
these assumptions,

\[
 \fint\frac{(S-2m_\beta)^2}{S}\le C\sqrt\eta,\qquad
 \|m-m_\beta\|_{3/2,\mathrm{avg}}\le C\eta^{1/4},
                                                               \tag{8.4}
\]
\[
 \frac{\operatorname{Vol}\{m\le m_\beta/4\}}V
                                      \le C\sqrt\eta. \tag{8.5}
\]

In particular, along beta->infinity, eta->0, |t|^2 tends to 128/81
strongly in every normalized Lq, 1<=q<2, not merely in mean.

**Proof.** Test the actual equation Delta rho=-2|P|^2-U rho/2
against a=2rho^2/S. Direct differentiation cancels its leading terms:

\[
 da=\frac{4m_\beta\rho}{S^2}d\rho
       -\frac{8\rho^4}{S^2}\operatorname{Re}\langle P,H\rangle.
\]

The coefficients of d rho and H are uniformly bounded. For the latter,
put z=rho|P|, so rho^4|P|/S^2=rho^3 z/(m_beta+2z^2)^2<=C.
Hence ||da||_2<=C and |avg<da,d rho>|<=C sqrt eta. The equation gives

\[
 \fint(2-2m_\beta/S+U\rho^3/S)=O(\sqrt\eta).
\]

Replace U rho^3 by U_beta rho_beta^3=-2m_beta, at cost O(sqrt eta).
It follows that avg(1/S)=1/(2m_beta)+O(sqrt eta). The exact nonnegative
Jensen defect
avg[(S-2m_beta)^2/S]=avg S-4m_beta+4m_beta^2 avg(1/S)
and (8.3) prove the first part of (8.4).

For its stronger norm assertion, test instead with b=rho^2 sqrt S.
Direct differentiation gives
|db|<=C[(1+|P|)|d rho|+|H|]. Since |d rho|<=4|P|,
the inherited L4/Hessian budget still gives ||db||_2<=C. Therefore

\[
 \fint(S-2m_\beta)\sqrt S=O(\sqrt\eta).
\]

The replacement error is at most
||U rho^3+2m_beta||_2 ||sqrt S||_2<=C sqrt eta. Subtract
sqrt(2m_beta) times the first identity of (8.3). With
G=(S-2m_beta)(sqrt S-sqrt(2m_beta))>=0, obtain avg G<=C sqrt eta.
Holder yields

\[
 \fint|S-2m_\beta|^{3/2}
 \le(\fint G)^{3/4}
       [\fint(\sqrt S+\sqrt{2m_\beta})^3]^{1/4}
 \le C\eta^{3/8}.
\]

The last factor is bounded by (8.3). From (8.2), interpolation of the
small L2 and bounded L4 norms of zeta gives ||d||_{3/2}<=C eta^{1/3}.
Since m-m_beta=S-2m_beta-d, (8.4) follows. Interpolate with the bounded
L2 norms to obtain every q<2, not q=2.

Finally, split {m<=m_beta/4} into {d>m_beta/4}, of volume O(eta)V,
and its complement. On the complement S<=3m_beta/2 and
(S-2m_beta)^2/S>=m_beta/6; (8.5) follows. QED.

### 8.1 Using both the Dirac and actual curvature equations

The equations of Sections2--3 imply an additional quantitative identity:

\[
 \boxed{\fint\left(\rho^3|\nabla u|^2-
            \frac{\rho^3m|dS|^2}{4S^3}\right)
       =\rho_\beta^3(1-1/\beta)+O(\sqrt\eta).}         \tag{8.6}
\]

In particular, the left side tends to 64/27 at the zero endpoint.
Here is the proof, including the critical tests.

Write Dt=R_D+E, with |R_D|<=C|zeta||P| and ||E||_2<=C sqrt eta.
Let w=1/S and W=rho^3/S. Testing the twisted Lichnerowicz identity
against Wt gives, with real Hermitian pairings,

\[
\begin{split}
 \int W|Dt|^2+\int\langle Dt,c(dW)t\rangle
  ={}&\int W|\nabla t|^2+\tfrac12\int\langle dW,dm\rangle\\
    &+\tfrac14\int sWm
      +\tfrac32\int W\langle c(F_A^-)t,t\rangle.       \tag{8.7}
\end{split}
\]

The two left integrals are O(sqrt eta V): use rho^3|P|^2/S<=C,
and the bounds
|t||dW|+|P||t||dW|<=C(|d rho|+|H|).
Their coefficients reduce to bounded functions of z=rho|P| and
S=m_beta+2z^2, so no division by rho occurs.

The gradient term containing d(rho^3) is also O(sqrt eta V), since
rho^2|t|/S is bounded. The rest completes exactly as

\[
 w|\nabla t|^2+\tfrac12\langle dw,dm\rangle
   =|\nabla(t/\sqrt S)|^2-\frac{m|dS|^2}{4S^3}.       \tag{8.8}
\]

The scalar term is -int rho^3 m/S+O(sqrt eta V).
Substitute the actual curvature equation (3.1) in the last term of (8.7).
The identity c(q_-(t))t=(m/2)t gives

\[
 -\tfrac32\int m^2/S
 +3\int\frac{\rho^2}{S}\langle c((d\zeta)^-)t,t\rangle
 +\tfrac32\int\frac{\langle c(\mathcal R)t,t\rangle}{S}. \tag{8.9}
\]

The quartic term is negative in the original Lichnerowicz equation.
The last integrand is bounded by
C(|Ric^circ|+|zeta||P|), so its normalized integral is O(sqrt eta).
For the middle term, Clifford duality gives
<c(xi)t,t>=4<xi,q_-(t)> for imaginary anti-self-dual xi. Integrating
by parts turns it into

\[
       12\int\left\langle\zeta,
              \delta\left(\frac{\rho^2q_-(t)}S\right)\right\rangle.
\]

The test is smooth globally. Its derivative satisfies

\[
 \left|\nabla\left(\frac{\rho^2q_-(t)}S\right)\right|
       \le C(|\nabla t|+|H|+|d\rho|).                \tag{8.10}
\]

Indeed |q(t)|<=Cm, |nabla q(t)|<=C|t||nabla t|, and differentiating
S reduces the needed coefficients to rho^2|t|/S, rho m/S,
rho^3m|P|^2/S^2, and rho^4m|P|/S^2. All are bounded by m<=2rho^2|P|^2
and bounded rho. Thus this current term is O(sqrt eta V), without
assuming the unweighted critical Dirac residual small.

Combining (8.7)--(8.10) proves

\[
 \fint\left(\rho^3|\nabla u|^2-\frac{\rho^3m|dS|^2}{4S^3}\right)
  =\fint\left(\frac{\rho^3m}{S}+\frac{3m^2}{2S}\right)
      +O(\sqrt\eta).
\]

From S=m_beta+m+d, avg d=O(eta), and the reciprocal test,
avg(m/S)=1/2+O(sqrt eta) and avg(m^2/S)=m_beta/2+O(sqrt eta).
For the latter replace m by S-m_beta at cost at most 2 avg d and use
(S-m_beta)^2/S=S-2m_beta+m_beta^2/S.
Replace rho^3 by rho_beta^3 in the first potential term, whose multiplier
m/S is bounded. The result is
rho_beta^3/2+3m_beta/4=rho_beta^3(1-1/beta), proving (8.6).

Both derivative integrals have uniform budgets; in particular
rho^3 m|dS|^2/S^3<=C(|d rho|^2+|H|^2). Since the subtracted term
is nonnegative, the zero-end consequence is

\[
             \liminf\fint|\nabla u|^2\ge1/27.        \tag{8.11}
\]

We used rho^3<=64, not an unjustified replacement of rho by its limiting
constant inside a derivative integral. The more precise weighted lower
bound is liminf avg rho^3|nabla u|^2>=64/27.

This is a full coupled identity at the available norms and a strong
subcritical length statement. It is not zero-freeness, critical L2
convergence of m, or a zero-end gap. The derivative defect in (8.6)
need not vanish; curvature/topological charge may still concentrate on
the shrinking low-torsion region. That localized charge, rather than
mean mass alone, remains to be controlled.

There is a concrete chirality distinction at this remaining step.
For B=S^- tensor L the signed density is

\[
 16\pi^2c_2(B)=
 \left(9|F_A^+|^2-9|F_A^-|^2
       +2|W^-|^2+s^2/24-\tfrac12|\operatorname{Ric}^{\circ}|^2\right)d\mu.
                                                               \tag{8.12}
\]

Thus an ideal Ricci-flat core with W^+=F_A=0 has *positive* bulk
density |W^-|^2/(8pi^2) for this bundle. The positive-spinor
negative-charge argument does not transfer to it. This is a bulk sign
calculation, not a complete marked filling or an actual counterexample.
The next sufficient exclusion would have to control this positive
curvature contribution together with the boundary flux on the
low-torsion region in (8.5), or a construction would have to realize
that entire coupled region and its exterior. Small volume by itself
settles neither alternative.
