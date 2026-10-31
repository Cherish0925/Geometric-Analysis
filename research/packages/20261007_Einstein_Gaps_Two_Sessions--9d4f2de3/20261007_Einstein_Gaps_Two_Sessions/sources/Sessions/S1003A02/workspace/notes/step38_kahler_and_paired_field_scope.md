# Step 38 — The Kähler blow-up tariff and the corrected paired-field problem

## 1. The closed same-metric form

Let \(M=X\#k\overline{\mathbf {CP}}^{2}\), where \(X\) is a fixed minimal complex surface of general type, \(A=K_X^2>0\), and orient \(M\) by its complex orientation. Put
\[
 C_+(g)=\frac1{2\pi^2}\int_M|W^+_g|^2+\frac1{96\pi^2}\int_Ms_g^2.
\]
The closed Chern--Weil identity is
\[
 \frac{P(g)}{8\pi^2}=C_+(g)-(A-k),\qquad P(g)=\int_M|\operatorname{Ric}^\circ_g|^2.
\]
Thus a universal tariff \(P/(8\pi^2)\ge ck\) is exactly
\[
 C_+(g)\ge A-(1-c)k
\]
for the same metric. The sharpened Arb enclosure for the authoritative perpendicular cell is
\[
 \frac{P_{\rm cell}}{8\pi^2}\in
 [0.995662732753254329\ldots,0.995662732771114200\ldots].
\]
Thus any per-blow-up coefficient compatible with the supplied sparse ramified/ball-quotient constructions must satisfy \(c\le0.995662732771115\).

## 2. Kähler blow-up theorem

Fix the blow-up complex structure \(\pi:M\to X\), write
\[
 K_0=\pi^*K_X,\qquad K_M=K_0+\sum_{i=1}^kE_i,
\]
so that \(K_0^2=A\), \(K_0\cdot E_i=0\), and \(E_i\cdot E_j=-\delta_{ij}\). For any Kähler metric \(g\) on this complex surface, with Kähler class \(\Omega=[\omega]\), put \(e_i=\Omega\cdot E_i>0\).

### Theorem K-blow-up

Every such Kähler metric satisfies
\[
 C_+(g)=\frac1{32\pi^2}\int_Ms_g^2\ge A,
 \qquad P(g)\ge8\pi^2k.
\]
If \(k>0\), both inequalities are strict.

### Proof

On a Kähler surface in the complex orientation the eigenvalues of \(W^+\) are \(s/6,-s/12,-s/12\). Hence \(|W^+|^2=s^2/24\) and
\[
 C_+=\frac1{32\pi^2}\int s^2.
\]
Also
\[
 \int_Ms\,d\mu=4\pi c_1(M)\cdot\Omega=-4\pi K_M\cdot\Omega,
 \qquad \operatorname{Vol}(g)=\frac{\Omega^2}{2}.
\]
Cauchy--Schwarz for the scalar function gives the exact decomposition
\[
 C_+(g)=\frac{(K_M\cdot\Omega)^2}{\Omega^2}
 +\frac1{32\pi^2}\int_M(s-\bar s)^2.
\]
Since \(K_X\) is nef and big, \(K_0\) and \(\Omega\) lie in the same positive cone closure. Hodge index gives
\[
 K_0\cdot\Omega\ge\sqrt{A\Omega^2}.
\]
Because \(K_M\cdot\Omega=K_0\cdot\Omega+\sum_i e_i\),
\[
\begin{aligned}
 C_+-A
 &\ge \frac{2\sqrt A\sum_i e_i}{\sqrt{\Omega^2}}
      +\frac{(\sum_i e_i)^2}{\Omega^2}
      +\frac1{32\pi^2}\int(s-\bar s)^2\ge0.
\end{aligned}
\]
When \(k>0\), every \(e_i>0\), so the result is strict. The closed identity then yields \(P>8\pi^2k\). A slightly stronger Hodge estimate follows from \(\Omega_0=\Omega+\sum_ie_iE_i\):
\[
 K_0\cdot\Omega\ge\sqrt{A(\Omega^2+\sum_ie_i^2)}.
\]

### Exact infimum: proved range and needed input

The theorem proves only \(\inf_{\rm Kahler}P\ge8\pi^2k\). Equality of the infimum requires a Kähler recovery family with exceptional areas tending to zero, Kähler classes tending to the canonical ray, and scalar variance tending to zero. It follows, for example, when \(K_X\) is ample and a standard small-exceptional-size Kähler blow-up construction supplies metrics converging off the exceptional curves to the negative Kähler--Einstein metric. In that setting
\[
 \inf_{\rm Kahler}P=8\pi^2k,
\]
and for \(k>0\) it is not attained. Theorem F's aligned Burns response \(1+6x_0+O(x_0^{6/5})\) is compatible with this upper approach but, by itself, is only a Riemannian local gluing theorem and does not prove that the glued metric is Kähler. The exact-infimum statement therefore must retain the Kähler-recovery hypothesis.

The strict subunit perpendicular cell is consequently genuinely non-Kähler. Its canonical almost-Kähler form has zero period on the exceptional sphere, whereas the Riemannian exceptional area is positive. Thus the cheap cell realizes monopole blindness geometrically: the class is null for the compatible field used by a LeBrun-type estimate, not merely lost by averaging sign classes.

## 3. Paired monopoles: exact line bundles and algebra

Assume the metric-wise simultaneous supply of monopoles for
\[
 a_\epsilon=c+\sum_i\epsilon_iE_i=c_1(L_\epsilon),\qquad \epsilon\in\{\pm1\}^k.
\]
For \(S^+_{\epsilon'}\cong S^+_\epsilon\otimes N_{\epsilon'\epsilon}\), Spin\(^c\) twisting gives
\[
 c_1(N_{\epsilon'\epsilon})=\frac{a_{\epsilon'}-a_\epsilon}{2}.
\]
With the Hermitian convention conjugate-linear in the first entry,
\[
 u_{\epsilon\epsilon'}=\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle
 \in\Gamma(N_{\epsilon'\epsilon}^*),
 \qquad c_1(u)=\frac{a_\epsilon-a_{\epsilon'}}2,
\]
while
\[
 w_{\epsilon\epsilon'}=\Phi_\epsilon\wedge\Phi_{\epsilon'}
 \in\Gamma(\det S^+_\epsilon\otimes N_{\epsilon'\epsilon}),
 \qquad c_1(w)=\frac{a_\epsilon+a_{\epsilon'}}2.
\]
For a single sign flip at \(E_i\), \(c_1(u)=\pm E_i\), not \(\pm2E_i\). If \(A_{\epsilon'}=A_\epsilon+2B\), the relative curvature is
\[
 f_u=\frac{f_\epsilon-f_{\epsilon'}}2.
\]
This factor is essential for Chern--Weil. The nonzero class forces every transverse section \(u\) to have a zero cycle dual to \(\pm E_i\), but it does not force either spinor to vanish: \(u=0\) may instead mean pointwise orthogonality.

Let \(\rho_\epsilon=|\Phi_\epsilon|^2\), and write \(f_\epsilon^+=(\rho_\epsilon/\sqrt2)n_\epsilon\), \(|n_\epsilon|=1\). Fierz gives
\[
 |u|^2=\rho\rho'\frac{1+n\cdot n'}2,
 \qquad |w|^2=\rho\rho'\frac{1-n\cdot n'}2,
\]
so
\[
 |f_\epsilon^+-f_{\epsilon'}^+|^2
 =\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}+2|w_{\epsilon\epsilon'}|^2.
\]
Together with Walsh Parseval,
\[
 2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
 =\mathbb E_{\epsilon,\epsilon'}\int
 \left[\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}+2|w_{\epsilon\epsilon'}|^2\right].
\]
The kinetic split is
\[
 |\nabla_A\Phi|^2=\frac{|\zeta|^2}{\rho}+\frac\rho4|\nabla n|^2,
 \qquad \zeta=\langle\Phi,\nabla_A\Phi\rangle.
\]
Thus a forced zero of \(u\) can be paid either by amplitude depletion or by relative spin-direction rotation. Static topology alone does not price the latter; a useful lower estimate needs a covariant vortex/winding inequality involving the relative connection.

## 4. Correct amplitude theorem at scalar \(-4\)

Suppose \(s_g=-4\), \(b_+\ge2\), and actual monopoles for the entire sign family are available on the same metric in the normalization
\[
 D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),\qquad |\sigma(\Phi)|^2=|\Phi|^4/8.
\]
The integrated Weitzenböck identity gives
\[
 0\le\rho\le2,\qquad
 K_\epsilon=\int|\nabla_{A_\epsilon}\Phi_\epsilon|^2
 =\frac12\int\rho_\epsilon(2-\rho_\epsilon).
\]
Substitution into the simultaneous-field identity yields the exact nonnegative form
\[
\begin{aligned}
&P-8\pi^2Q+4\mathbb E_\epsilon\int(2-\rho_\epsilon)\\
={}&2\|f_\varnothing^-\|_2^2
+\mathbb E_{\epsilon,\epsilon'}\int
\left[\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}+2|w_{\epsilon\epsilon'}|^2\right]\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2+4\|W^+-W_{0,\epsilon}\|_2^2
+\int(b(\rho_\epsilon)+2)(2-\rho_\epsilon)^2\right],
\end{aligned}
\]
where \(b(t)=(-t^2+8t+2)/6\ge1/3\) on \([0,2]\). In particular,
\[
 \boxed{P\ge8\pi^2Q-4\mathbb E_\epsilon\int(2-\rho_\epsilon).}
\]
This is the corrected clean amplitude theorem. An equivalent residual-polynomial form uses
\[
 m(\rho)=\frac{(2-\rho)(-\rho^3+10\rho^2-2\rho-4)}6,
\]
which changes sign; it cannot prove \(P\ge8\pi^2Q\) by itself. The coefficient four in the linear amplitude-deficit bound is sharp at \(\rho=2\).

## 5. The isolated cell monopole problem is different from closed supply

The invariant diagonal Bianchi--IX reduction was checked by Lichnerowicz. With
\[
 v_i=\alpha_i/a_i,\qquad
 c=\frac{\sum a_i^2}{2a_1a_2a_3}-\frac12\sum\dot a_i/a_i,
\]
and \(n=(\rho\cos\theta,0,\rho\sin\theta)\),
\[
\begin{aligned}
\dot{\log\rho}&=2c+v_1\cos\theta+v_3\sin\theta,\\
\dot\theta&=v_3\cos\theta-v_1\sin\theta,\\
\dot\alpha_1&=a_1\rho\cos\theta-2a_1\alpha_1/(a_2a_3),\\
\dot\alpha_3&=a_3\rho\sin\theta-2a_3\alpha_3/(a_1a_2).
\end{aligned}
\]
At a smooth slot-1 bolt, the regular charged family has two parameters \((\rho_0,\beta)\) and
\[
 \theta=\theta_\sigma-\sigma\beta t+O(t^3),\quad
 \alpha_1=\sigma\left[1-(\rho_0/2+b^{-2})t^2\right]+O(t^4),\quad
 \alpha_3=b\rho_0\beta t^2/4+O(t^4).
\]
The exact CH monopole is \(\rho=12\), \(\theta=\pi/2\), \(\alpha_1=0\), \(\alpha_3=3\sinh^2r\). Exact finite-radius matching to all four CH data is impossible for \(\sigma=\pm1\): the plane \(\theta=\pi/2,\alpha_1=0\) is invariant, hence backward uniqueness reaches bolt charge zero. The correct isolated problem is asymptotic convergence to the two-dimensional CH stable manifold, with far conditions
\[
 \mathcal B+6L=0,\qquad
 \mathcal A-(\sqrt{13}-1)\delta=0
\]
to leading order, where \(L=\log(\rho/12)\), \(\delta=\theta-\pi/2\), \(\mathcal A=\alpha_1/\sinh r\), and \(\mathcal B=(\alpha_3-3\sinh^2r)/(\sinh r\cosh r)\).

The Step-37 forward code imposed only \((\rho,\theta)=(12,\pi/2)\) at finite radius and was exponentially ill-conditioned; the first Step-38 collocation imposed limiting bolt values at a positive cutoff, omitted the regularity condition excluding the \(\alpha_3\sim t^{-2}\) mode, and again used the wrong terminal subspace. Its failed output is not monopole data. A corrected multiple-shoot attempt also timed out before any root or profile was produced. More importantly, a monopole on the closed host need not restrict to an invariant isolated-cell monopole with canonical CH asymptotics: its boundary trace is selected by the exterior, and nonlinear equations cannot be averaged to impose symmetry. Therefore cell ODE data, even if obtained, would be a model of one field channel rather than the metric-wise closed theorem required globally.

## 6. Consequence for the global route

The Kähler theorem identifies a complete unit tariff in the class where the canonical field sees every exceptional curve. The cheap cell identifies the opposite mechanism: the field period on \(E\) vanishes and the topology can be carried by relative spin-direction rotation rather than a holomorphic amplitude vortex. The paired formulation restores the class through \(c_1(u)=E_i\), but no current identity proves that its relative rotation has a positive metric-uniform energy. The next global advance must either derive such a covariant vortex bound on closed metrics or produce a family in which the relative rotation spreads with vanishing energy while the singleton curvature charge remains fixed. Isolated exact-end shooting cannot decide that global dichotomy by itself.

## 7. Anti-self-dual retention on a ramification neighbourhood

Let \(N\) be a fixed ramification neighbourhood and suppose \(g\) agrees with the Kähler--Einstein model \(g_0\) to the order needed for the Euler and signature transgressions to agree on \(\partial N\). No surgery topology is placed inside \(N\). Relative signature gives
\[
 \Delta_N\int|W^+|^2=\Delta_N\int|W^-|^2=:\Delta_N B.
\]
The relative closed/APS Chern--Weil identity, using \(\operatorname{Ric}^\circ(g_0)=0\), then gives the exact formula
\[
 \boxed{\Delta_N B=\frac14P_N(g)-\frac1{48}\Delta_N S.}
\]
Thus characteristic flux alone supplies no sign for anti-self-dual retention: it converts it exactly into the scalar-square channel. If both metrics are normalized to \(s=-4\), this becomes
\[
 \boxed{\Delta_N B=\frac14P_N(g)-\frac13\Delta_N V.}
\]
Consequently, a useful local retention estimate is equivalent to an upper relative-volume estimate. Depletion occurs precisely when the normalized relative-volume increase exceeds \(3P_N/4\). This is the same Weyl--volume exchange already exposed by Theorem C for exact-CH cells; the APS/calibration identities do not add an independent positive term. The global monopole scalar budget controls total \(S\), not its allocation among ramification and surgery regions, so it does not presently close this local estimate. A field localized to the ramification neighbourhood, or a construction showing favourable relative-volume increase there, is necessary to decide the true \(r\)-dependence.

## 8. Exact relative-curvature completion and the fate of the paired route

For one sign flip write \(a'=a+2E\), \(E^2=-1\), choose the relative twisting line \(N\) with \(c_1(N)=E\), and set
\[
 h=\frac{f-f'}2,\qquad \bar f=\frac{f+f'}2.
\]
Then \([h/(2\pi)]=-E\), while the SW curvature equations and Fierz identities give
\[
 |h^+|^2=\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2}.
\]
Chern--Weil gives the exact Bogomolny completion
\[
 \boxed{\|h^-\|_2^2-\|h^+\|_2^2=4\pi^2,}
\]
\[
 \boxed{\|h\|_2^2=4\pi^2+\int\left[\frac{(\rho-\rho')^2}{4}+|w|^2\right].}
\]
Thus the fixed negative-square charge is stored in the anti-self-dual relative curvature. Amplitude mismatch and spin-direction disagreement measure only \(h^+\). The paired object does not produce an additional positive sector beyond the singleton Walsh curvature; it explains where that sector's topology lives.

There is also a topological unwinding mechanism. The combined bilinear
\[
 q=(u,w)\in N^*\oplus D,
 \qquad D=\det S_a^+\otimes N,
\]
has \(|q|^2=\rho\rho'\). In the pure one-flip situation \(c_1(N^*)=-E\), \(c_1(D)=c\), and \(c\cdot E=0\), so
\[
 c_2(N^*\oplus D)=0.
\]
Where both spinors are nonzero, \(q/|q|\) lies in \(S^3\). The phase winding of the \(u\)-component, which would be protected inside \(S^1\), can unwind through \(w\) because \(\pi_1(S^3)=0\). This makes the orthogonality zero mechanism precise.

The bilinear fields obey product Bochner equations, for example
\[
 \left(\nabla_{N^*}^*\nabla_{N^*}+\frac s2+\frac{\rho+\rho'}2\right)u
 =-2\sum_\alpha\langle\nabla_{A',e_\alpha}\Phi',\nabla_{A,e_\alpha}\Phi\rangle.
\]
The right side is an unsigned twistor cross term. Hence \(u\) is not a closed scalar vortex field on a general Riemannian four-manifold. The relative curvature enters derivative commutators multiplied by \(u\), precisely degenerating at the forced zero, while \(w\) couples to \(\bar f\), not \(h\).

For one pair, the simultaneous-field cost identity can be written
\[
 P-8\pi^2
 =2\|\bar f^-\|_2^2+2\|h^+\|_2^2
 +\frac{\mathcal R(\Phi)+\mathcal R(\Phi')}{2}-2(K+K'),
\]
where \(\mathcal R\) is the nonnegative alignment/amplitude remainder already recorded above. The topological \(8\pi^2\) has already been extracted from \(\|h^-\|^2-\|h^+\|^2=4\pi^2\). A positive excess would require an additional kinetic compensation estimate; the paired Bochner system does not supply one. Common amplitude depletion is linear in \(2-\rho\) while the displayed amplitude remainders are quadratic, and relative rotation can unwind through \(w\).

Accordingly, the paired construction is scientifically useful as a structural explanation but does not by itself improve the global lower bound. A positive excess can follow under extra projection/noncollapse input, e.g. \((E_g^+)^2\ge\delta>0\) together with a kinetic compensation inequality. Such projection input fails exactly in the perpendicular null-period regime. In a tube of radius \(r\) around an exceptional sphere of area \(A_E\), a relative spin rotation has the scale
\[
 \int|\nabla n|^2=O(A_E),\qquad \int|w|^2=O(A_Er^2),
\]
so both can vanish as \(A_E\to0\) while the fixed \(4\pi^2\) relative charge remains in \(h^-\). This is the field-theoretic countermechanism compatible with subunit perpendicular cells.

Independent derivation: `trace/ttcs/results/step38_ttcs02_generator1_integration.md`.
