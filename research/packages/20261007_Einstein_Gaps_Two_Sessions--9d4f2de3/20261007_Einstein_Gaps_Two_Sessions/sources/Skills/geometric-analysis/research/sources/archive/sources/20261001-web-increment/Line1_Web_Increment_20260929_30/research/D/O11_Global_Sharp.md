# O11: an exact simultaneous-field decomposition, and why the O10 positive-potential argument does not transfer

2026-09-29, continuation D. This note pursues the all-metric lower bound on the original balanced family. It does **not** determine the optimal coefficient. The result below is an exact differential-field decomposition of the missing sharp cost, with no exponential loss from the number of supplied classes. It is a research reduction, not a new range of the main theorem.

## 1. Input and normalization

Let
\[
M=X\#k\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3),
\qquad A=c_1^2(X),\qquad Q=k+4\ell.
\]
Use a constant-scalar representative with \(s=-4\), and the manuscript's curvature norms. Set \(P=\int|\operatorname{Ric}^\circ|^2\). For the present family all the classes
\[
a_\epsilon=c_0+\sum_{i=1}^k\epsilon_iE_i,
\quad \epsilon\in\{-1,1\}^k,
\quad c_0^2=A,\quad E_iE_j=-\delta_{ij}
\]
have actual ordinary solutions. This statement uses the chamber-independent supply on the original family; it is not asserted for arbitrary \(b_+=1\) data. Select one solution for each class, all on this same metric:
\[
D_{A_\epsilon}\Phi_\epsilon=0,
\qquad F_{A_\epsilon}^+=2i\sigma(\Phi_\epsilon),
\qquad 0\le\rho_\epsilon=|\Phi_\epsilon|^2\le2.
\]
Write
\[
f_\epsilon=-iF_{A_\epsilon},\quad
K_\epsilon=\int|\nabla_{A_\epsilon}\Phi_\epsilon|^2,
\quad\zeta_\epsilon=\langle\Phi_\epsilon,\nabla_{A_\epsilon}\Phi_\epsilon\rangle.
\]
The convention is \([f_\epsilon/(2\pi)]=a_\epsilon\). Reversing every Chern representative sign changes none of the identities involving squares below. The spinor Hessian equation is
\[
\nabla_{A_\epsilon}^*\nabla_{A_\epsilon}\Phi_\epsilon
=\left(1-\frac{\rho_\epsilon}{2}\right)\Phi_\epsilon.
\tag{1}
\]

All formulas through (10) are exact for each fixed manifold and metric. No limiting compactness or identification of surgery regions is used.

## 2. The supplied curvature cube carries the exceptional cost without an exponential factor

For a subset \(I\subset\{1,\ldots,k\}\), define the real closed two-form
\[
f_I=2^{-k}\sum_\epsilon\left(\prod_{i\in I}\epsilon_i\right)f_\epsilon.
\]
These are averages of curvature forms, not averages of connections on distinct line bundles. Their cohomology classes are
\[
[f_\varnothing/(2\pi)]=c_0,\qquad
[f_{\{i\}}/(2\pi)]=E_i,\qquad
[f_I]=0\quad(|I|\ge2).
\tag{2}
\]
The last equality is over real de Rham cohomology, which is all that Chern–Weil uses here. Parseval's identity on the finite sign cube gives
\[
\mathbb E_\epsilon\|f_\epsilon^\pm\|_2^2
=\sum_I\|f_I^\pm\|_2^2.
\]
For every singleton, (2) implies
\(\|f_{\{i\}}^-\|_2^2-\|f_{\{i\}}^+\|_2^2=4\pi^2\);
for \(|I|\ge2\), the two norms are equal. Consequently
\[
\boxed{
\mathbb E_\epsilon\|f_\epsilon^-\|_2^2
=4\pi^2k+\|f_\varnothing^-\|_2^2
 +\sum_{I\ne\varnothing}\|f_I^+\|_2^2.}
\tag{3}
\]
Thus the full exceptional contribution is already visible in one simultaneous system. Merely writing (3), however, does not pay this contribution with traceless Ricci curvature. The next identity identifies the term that prevents such a conclusion.

## 3. Exact sharp-cost identity: every remaining adverse term is spinor kinetic energy

For every \(\epsilon\),
\[
c_2(S^+_{a_\epsilon})[M]
=\frac{a_\epsilon^2-(2\chi+3\tau)}4=\ell.
\]
The manuscript's exact spinor Chern density yields
\[
P=32\pi^2\ell+2\|f_\epsilon^-\|_2^2
 +4\|W^+\|_2^2+\frac{4V}{3}-\int\rho_\epsilon^2.
\tag{4}
\]
Let
\[
C(t)=t+1-\frac{(t+2)^2}{12},\qquad
b(t)=2C(t)-1=\frac{-t^2+8t+2}{6}.
\]
In particular \(b(t)\ge1/3\) on \([0,2]\). Let \(W_{0,\epsilon}\) be the same bounded spinor curvature model used in the single-solution \(\beta=2\) decomposition. The two already established exact identities are
\[
\frac{D_\epsilon}{18}=J_\epsilon+2\|\zeta_\epsilon\|_2^2
 +\|W^+-W_{0,\epsilon}\|_2^2
 +\frac12\int C(\rho_\epsilon)(\rho_\epsilon-2)^2,
\]
\[
\Sigma_\epsilon=16K_\epsilon
 +4\int(\rho_\epsilon-2)^2+8J_\epsilon.
\tag{5}
\]
The identity
\[
4\|W^+\|_2^2+\frac{4V}{3}-\int\rho_\epsilon^2
=\frac29D_\epsilon-\frac14\Sigma_\epsilon-2J_\epsilon
\]
therefore becomes
\[
4\|W^+\|_2^2+\frac{4V}{3}-\int\rho_\epsilon^2
=8\|\zeta_\epsilon\|_2^2
 +4\|W^+-W_{0,\epsilon}\|_2^2
 +\int b(\rho_\epsilon)(\rho_\epsilon-2)^2-4K_\epsilon.
\tag{6}
\]
Average (4), use (3), and substitute (6). This proves
\[
\boxed{P-8\pi^2Q=\mathcal A(g,\{\Phi_\epsilon\})
 -4\mathbb E_\epsilon K_\epsilon,}
\tag{7}
\]
where every term of
\[
\begin{aligned}
\mathcal A={}&2\|f_\varnothing^-\|_2^2
 +2\sum_{I\ne\varnothing}\|f_I^+\|_2^2\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2
 +4\|W^+-W_{0,\epsilon}\|_2^2
 +\int b(\rho_\epsilon)(\rho_\epsilon-2)^2\right]
\end{aligned}
\tag{8}
\]
is nonnegative.

The coefficients in (7) can be checked independently by substituting (5) and \(D_\epsilon=24V+18\|W^+\|_2^2-72\pi^2p_\epsilon\), \(\Sigma_\epsilon=16V-32\pi^2p_\epsilon\). No estimate is used in this cancellation.

For precision about what the simultaneous organization adds, its first line also equals
\[
2\|f_\varnothing^-\|_2^2+2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
=8\pi^2(\mathbb E_\epsilon p_\epsilon-A)+2\mathbb E_\epsilon J_\epsilon.
\]
Thus Walsh decomposition does not itself improve the averaged classical projection budget. Its role is to identify the exceptional charge and every nonnegative curvature remainder in the same actual family.

In particular, a putative sequence with
\(P\le8\pi^2(1-\delta)Q\), \(\delta>0\), must satisfy
\[
\boxed{\mathbb E_\epsilon K_\epsilon
\ge2\pi^2\delta Q+\frac14\mathcal A.}
\tag{9}
\]
Thus amplitude errors, phase errors, the scalar–Weyl model error, or additional determinant curvature alone cannot create a cheaper competitor: they occur with positive signs. A cheaper competitor must support enough genuine covariant first-derivative energy to overpay all those terms. This is a stronger description of the required mechanism than an unsigned scalar-slack variable, although it is **not** a sharp lower bound.

Conversely, the exact all-metric missing estimate can now be written
\[
4\mathbb E_\epsilon K_\epsilon\le\mathcal A+o(Q)
\tag{10}
\]
on a selected true near-minimizing sequence. The existing I40/I41 estimates give bounds with unspecified universal constants and \(O(Q)\) errors. They do not give (10), and (7) cannot itself be cited as a proof of (10).

## 4. The genuine comparison line and its second-order equation

Let \(a,b\) be two supplied structures. If \(S_b^+=S_a^+\otimes K_{ab}\), then
\[
c_1(K_{ab})=\frac{b-a}{2},\qquad
2B_{ab}=A_b-A_a
\]
in the usual local connection description. The fiberwise Hermitian pairing defines a genuine section
\[
u_{ab}=\langle\Phi_a,\Phi_b\rangle\in\Gamma(K_{ab}).
\]
For a sign edge, \(c_1(K_{ab})=\pm E_i\). Product differentiation of (1) gives the exact equation
\[
\boxed{
\nabla_{B_{ab}}^*\nabla_{B_{ab}}u_{ab}
=\left(2-\frac{\rho_a+\rho_b}{2}\right)u_{ab}
 -2\sum_j\langle\nabla_{A_a,j}\Phi_a,
                         \nabla_{A_b,j}\Phi_b\rangle.}
\tag{11}
\]
All pairings on the right are sections of the same comparison line. At the KE calibration \(\rho_a,\rho_b\to2\), its displayed scalar potential tends to **zero**, not a strictly positive number. Moving it to the left gives a nonpositive potential. Therefore this natural pairwise line does not reproduce the positive \(10/3\) coercive operator of the O10 zero endpoint.

The orthogonal wedge \(\Phi_a\wedge\Phi_b\), in the line of class \((a+b)/2\), satisfies the analogous product equation. It is the wrong replacement for a mass argument: when the two positive spinor lines align, this wedge vanishes.

There is also an exact pointwise alignment formula. With the normalized Hopf map of the manuscript,
\[
\boxed{|u_{ab}|^2=\frac{(\rho_a+\rho_b)^2}{4}
-\frac12|f_a^+-f_b^+|^2.}
\tag{12}
\]
It follows from \(\langle\psi_a,\psi_b\rangle=2|u_{ab}|^2-\rho_a\rho_b\) and \(f^+=\psi/\sqrt2\). On a near-minimizer the supplied estimates and the Hodge parallelogram bound give \(\int|f_a^+-f_b^+|^2=O(Q)\), uniformly in the two choices. Here is the complete Hodge step. Write \(f_a^+=2\pi H_a+r_a\), where \(H_a\) is harmonic and \(r_a\) is orthogonal to all harmonic self-dual forms, so \(\|r_a\|_2^2=J_a\). Then exactly
\[
\|f_a^+-f_b^+\|_2^2
=4\pi^2\|(a-b)^+\|^2+\|r_a-r_b\|_2^2
\le4\pi^2\|(a-b)^+\|^2+2J_a+2J_b.
\]
The single-solution decomposition gives \(J_a,J_b=O(Q)\). To bound the harmonic part, use
\[
\frac14\|(a-b)^+\|^2
=\frac{p_a+p_b}{2}-\|((a+b)/2)^+\|^2
\le A+O(Q)-(A-k)=O(Q).
\]
Together with (1) and (5), this shows that the comparison sections have nearly full volume-normalized mass. Their allowed derivative and curvature cost is nevertheless of order \(Q\), precisely the unresolved order. The large-volume rank-one Chern-vanishing argument from O10 cannot erase their \(Q\)-scale exceptional classes.

## 5. A needed topological distinction

Although \(f_\varnothing\) is a closed form in the integral class \(2\pi c_0\), its connection must **not** be declared a new ordinary Seiberg–Witten supplier on this blow-up. For \(k>0\), \(c_0\) is not characteristic:
\[
c_0\cdot E_i=0,
\qquad E_i^2=-1\pmod2.
\]
Hence \(c_0\bmod2\ne w_2(M)\). Averaging actual connections cannot remove this obstruction or manufacture a positive spinor bundle with determinant \(c_0\). This is why the curvature cube can be averaged exactly, whereas the actual spinor equations cannot simply be replaced by an equation for their average.

## 6. Outcome

The simultaneous-field calculation yields the exact identity (7), the necessary \(Q\)-scale kinetic cost (9), and the actual comparison-line equation (11). It identifies a specific sharp inequality (10) whose proof would settle the lower-bound side of O11. It does not prove that inequality, produce a lower-cost closed metric, or justify promoting the coefficient 4 from a recovery value to the global optimum.

The algebraic coefficients in (6) were independently checked with exact rational arithmetic: the coefficients of \((V,\|W^+\|_2^2,\pi^2p,J)\) on both sides of its first equality are \((4/3,4,-8,-2)\); after substitution of the field decompositions the coefficients of \((J,\|\zeta\|_2^2,\|W^+-W_0\|_2^2,\int C(\rho)(\rho-2)^2,K,\int(\rho-2)^2)\) are \((0,8,4,2,-4,-1)\).

The exact manuscript source labels are `eq:ssc-exact-decomposition`, `eq:ssc-spinor-rescaling`, `eq:ssc-low-slack`, and `proof:actual-topological:e4.4`. In particular, the source's rescaled kinetic term is \(K_{\rm rescaled}=(2/\sqrt6)K_\epsilon\), so \(8\sqrt6K_{\rm rescaled}=16K_\epsilon\); its amplitude potential is \(-4+2\rho_\epsilon\). This is the ordinary constant-weight-2 convention throughout the present note.

Source scope: the manuscript's single-solution decomposition and calibrated coercivity sections (local source `upload/27b3cef6-aeed-442c-9e66-fef1a757828e.tex`, around lines 4020–4180), its actual Chern-density section (around lines 28140–28180), and the original family's actual sign supply. The new work here is the simultaneous curvature organization and pairwise differential test; no independent certification of all manuscript inputs is claimed.
