# O10: a strong-current upgrade from the actual constant-weight equation

Date: 2026-09-29. Source: `upload/27b3cef6-aeed-442c-9e66-fef1a757828e.tex`, especially `sec:single-parameter`, `sec:endpoint-covariance`, `sec:phase-curvature`, `sec:torsion-prolongation`, and `sec:quartic-flux`.

## Result and scope

There is a new global estimate available before attempting any further manipulation of the final quartic flux identity. The actual constant-weight positive spinor has uniformly integrable fourth-power first derivative along every hypothetical O10 endpoint sequence. This upgrades the cubic torsion Dirac equation, its length, the original current derivative, and the full first torsion projection to strong critical statements. It uses no diameter, Sobolev, noncollapse, pointwise Ricci bound, or Euler-density upper bound.

It does **not** complete O10: it does not estimate the fourth-power derivative of the cubic torsion, its relative-index flux, or the remaining curvature-weighted radial-horizontal interaction. In particular it does not contradict the shrinking actual local torsion cores already constructed in the manuscript.

All averages below use the actual total volume, even when the manifold varies. Thus every vanishing squared norm is an `o(V)` statement, not an unnormalized smallness assumption.

## 1. A slow gradient truncation lemma

Let \((M_j,g_j)\) be closed Riemannian manifolds of fixed dimension and \(E_j\) Hermitian bundles of fixed rank, with unitary connections. Let \(u_j\) satisfy

\[
 |u_j|\le C_0,\qquad \nabla^*\nabla u_j=f_j(|u_j|^2)u_j,
 \qquad |f_j|+|f'_j|\le C_0.
\]

Suppose

\[
 \operatorname{Ric}_{g_j}=R_{0,j}+e_j,
 \quad F_j=F_{0,j}+E_j,
 \quad |R_{0,j}|+|F_{0,j}|\le C_0,
\]

where the symbol \(E_j\) on the right denotes a curvature error, and assume

\[
 \mu_j:=\fint(|e_j|^2+|E_j|^2)\longrightarrow0,
 \qquad \sup_j\mu_j\le C_0.
\]

No independent Hessian or fourth-power gradient budget is needed: these follow from the displayed hypotheses by the unweighted version of the argument below.

There is \(\epsilon>0\), depending only on the displayed constants, dimension, and rank, such that, with

\[
 q=|\nabla u|^2,\quad H=\nabla^2u,\quad
 w_L=\left(\frac q{L^2+q}\right)^\epsilon,
 \qquad L\ge1,
\]

one has

\[
 \boxed{\fint w_L(|H|^2+q^2)
              \le C L^{-2\epsilon}+C\mu_j.}\tag{1}
\]

Consequently

\[
 \boxed{\lim_{L\to\infty}\limsup_j
       \fint_{\{|\nabla u_j|\ge L\}}|\nabla u_j|^4=0.}\tag{2}
\]

This establishes uniform integrability of \(|\nabla u_j|^4\) relative to normalized volume. Formula (1) also controls \(|H|^2\) on the large-gradient set. It does **not**, by itself, prove uniform integrability of \(|H|^2\) on arbitrary small-volume sets.

### Proof

Use the smooth regularization

\[
 w_{L,\delta}=\left(\frac{q+\delta}{L^2+q+\delta}\right)^\epsilon,
 \quad \delta>0.
\]

It obeys

\[
 |dw_{L,\delta}|\,|\nabla u|\le2\epsilon w_{L,\delta}|H|.
\tag{3}
\]

Put \(P_i=\nabla_i u\), \(H_{ij}=\nabla_iP_j\), and
\(I=\int w|H|^2\), \(J=\int wq^2\), \(A_w=\int w(1+q)\).
Antisymmetry gives the exact algebraic identity

\[
 I=\int w\operatorname{Re}\langle H_{ij},H_{ji}\rangle
       +\frac12\int w\sum_{i,j}|F_{ij}u|^2.
\tag{4}
\]

In the first term integrate the derivative indexed by \(j\) in \(H_{ji}\). Then commute the two derivatives in
\(\nabla_jH_{ij}=\nabla_j\nabla_iP_j\). The commutator on the covector-valued section \(P\) contains only \(\operatorname{Ric}*P+F*P\), and
\(\sum_j\nabla_jP_j=-f(|u|^2)u\). In particular **no derivative of either curvature occurs**. The derivative of \(f(|u|^2)u\) is bounded by \(C|P|\). The derivative of the scalar weight contributes at most \(2\epsilon I\), by (3). Thus, after taking \(\epsilon\) sufficiently small,

\[
 I\le C A_w+C\int w(|e|+|E|)q+C\int (|e|^2+|E|^2).
\tag{5}
\]

The term involving \(F^2\) in (4) was bounded using \(F=F_0+E\) and bounded \(F_0\). No derivative of the bounded model is required.

For completeness, a weighted bounded-section interpolation follows by integrating the divergence of
\(wq\operatorname{Re}\langle u,P\rangle\). The derivative of \(q\) contributes at most \(C\int wq|H|\); the derivative of \(w\) has the same bound by (3); the trace Hessian term is bounded by \(C\int wq\). Therefore

\[
 J\le C\int wq+C\sqrt{IJ},\qquad
 J\le C_1(I+A_w).\tag{6}
\]

Since \(0\le w\le1\), for any fixed \(a>0\),

\[
 \int w(|e|+|E|)q
 \le aJ+C_a\int(|e|^2+|E|^2).
\tag{7}
\]

Choose \(a\) after \(C_1\) so that (5)--(7) absorb the resulting multiple of \(I\). It follows that

\[
 I+J\le C A_w+C\mu_jV_j.
\tag{8}
\]

Before estimating the weighted right side, take \(w\equiv1\) in (4)--(8). Testing the section equation by \(u\) gives
\[
\int q=\int f(|u|^2)|u|^2\le CV.
\]
The same absorption then proves
\[
\fint(|H|^2+q^2)\le C(1+\mu_j)\le C.
\]
Thus the energy budget used in the following step is a consequence, not an extra hypothesis.

For \(0<\epsilon\le1\),

\[
 w_{L,\delta}\le L^{-2\epsilon}(q+\delta)^\epsilon.
\]

The just-proved normalized \(q^2\) bound controls the average of
\((q+\delta)^\epsilon(1+q)\), uniformly for \(0<\delta\le1\). Divide (8) by \(V_j\), then let \(\delta\downarrow0\), obtaining (1). On \(q\ge L^2\), \(w_L\ge2^{-\epsilon}\), so (2) follows. Every calculation is on a closed manifold with a globally smooth regularized scalar weight.

## 2. Apply the lemma to the hypothetical O10 endpoint

Use the manuscript's exact Yamabe reduction and a single ordinary solution rescaled to

\[
 s=-4,\quad D_A\Phi=0,\quad F_A^+=2i\sigma(\Phi),
 \quad \rho=|\Phi|^2\le2.
\]

Set \(P=\nabla_A\Phi\), \(H=\nabla_AP\),
\(\zeta=\langle\Phi,P\rangle\), \(\tau=t_\Phi\),
\(m=|\tau|^2\), \(\rho_*=4/3\), \(m_*=128/81\), and
\(\eta=r+D_\beta/V+\beta^{-2}\to0\).

The actual semilinear equation is

\[
 \nabla_A^*\nabla_A\Phi=(1-\rho/2)\Phi.\tag{9}
\]

The latest bounded ASD fit supplies the lemma's full connection-curvature hypothesis. The old Hessian budget is consistent with, and can also be recovered from, the unweighted part of the lemma. With

\[
 f=-iF_A^-,\quad Q=-iq_-(\tau),\quad
 S=m_*+2\rho^2|P|^2,\quad
 K=-\frac98\frac{\rho^3Q}{S},
\]

the manuscript proves

\[
 |K|\le C,\qquad \fint|f-K|^2\le C\sqrt\eta.
\tag{10}
\]

The traceless curvature of \(S^+\) contains \(W^++s/12\) and the off-diagonal Ricci block; it contains **no \(W^-\)**. Its central part is \(F_A/2\). Retain the scalar block, the bounded actual self-dual determinant curvature, and the bounded ASD model \(iK\) as \(F_0\). The remaining curvature has

\[
 \fint|F^{S^+}-F_0|^2\le C\sqrt\eta,
 \quad |F_0|\le C,
 \quad \fint|\operatorname{Ric}+g|^2\le\eta.
\tag{11}
\]

Here \(W^+\to0\) follows from the same-solution parameter estimate, including its bounded axial model of size \(O(\beta^{-1})\). Applying (1) gives

\[
 \boxed{\fint w_L(|H|^2+|P|^4)
         \le C L^{-2\epsilon}+C\sqrt\eta.}\tag{12}
\]

There is no hypothesis on the opposite Weyl curvature and hence no use of \(\chi/A\le B\) in this result.

## 3. Strong critical consequences

### 3.1 The mixed spinor product and torsion Dirac residual

The old identity gives \(\fint|\zeta|^2\le C\eta\), while
\(|\zeta|\le\sqrt2|P|\). Splitting into \(|P|\le L\) and its complement in (12) yields

\[
 \fint|\zeta|^2|P|^2
 \le C\{L^2\eta+L^{-2\epsilon}+\sqrt\eta\}\to0.
\tag{13}
\]

For example choosing \(L=\eta^{-1/(2+2\epsilon)}\) gives a bound by
\(C\eta^{\epsilon/(1+\epsilon)}+C\sqrt\eta\).
Also \(\fint|\zeta|^4\to0\). The exact cubic equation, with axial cancellation retained, now implies

\[
 \boxed{\|D^-_{3A}\tau\|_{L^2_{\rm avg}}\to0.}\tag{14}
\]

This is stronger than the previous \(L^q\), \(q<2\), conclusion.

### 3.2 Torsion length and positive-spinor energy density

The existing torsion-length concentration gives \(m\to m_*\) in normalized measure. Since
\(m\le2\rho^2|P|^2\le8|P|^2\), (12) makes \(m^2\) uniformly integrable. Vitali on the probability spaces \((M_j,dV_j/V_j)\) gives

\[
 \boxed{\|m-m_*\|_{L^2_{\rm avg}}\to0.}\tag{15}
\]

The exact algebraic defect satisfies

\[
 \nu=2\rho^2|P|^2-m,\quad
 0\le\nu\le4\rho|\zeta|^2,
\]

so \(\nu\to0\) in normalized \(L^2\). On \(\rho\ge c>0\), use (15) and \(\rho\to\rho_*\) in measure; on \(\rho<c<\rho_*\), its relative volume tends to zero and (12) controls \(|P|^4\). Consequently

\[
 \boxed{\big\||P|^2-4/9\big\|_{L^2_{\rm avg}}\to0.}\tag{16}
\]

The scalar equation
\(\Delta\rho=-2|P|^2+2\rho-\rho^2\) therefore gives

\[
 \|\Delta\rho\|_{L^2_{\rm avg}}\to0.\tag{17}
\]

### 3.3 The full current derivative

The actual polynomial curvature equation is

\[
 \rho^3 f+2Q=2\rho^2(d\gamma)^-+\mathcal R,
 \quad \gamma=\operatorname{Im}\zeta,
 \quad |\mathcal R|\le
 C(\rho^3|\operatorname{Ric}^{\circ}|+
              \rho^{3/2}|\zeta||P|).
\tag{18}
\]

Real/imaginary conventions may reverse both signs of the derivative term; only its norm is used here. By (13), \(\mathcal R\to0\) in normalized \(L^2\). Furthermore

\[
 \rho^3 f+2Q
 =\rho^3(f-K)+\left(2-\frac98\frac{\rho^6}{S}\right)Q.
\tag{19}
\]

The first term is small by (10). The coefficient in the second is uniformly bounded, converges to zero in measure, and \(|Q|^2=m^2/8\) is uniformly integrable by (15). Thus the second term is small in normalized \(L^2\). Equation (18) proves \(\rho^2(d\gamma)^-\to0\) in that norm.

This weighted assertion becomes unweighted without assuming a pointwise lower bound for \(\rho\). Indeed

\[
 |d\zeta|\le C(|P|^2+\rho|F^{S^+}|).
\tag{20}
\]

The squares on the right are uniformly integrable, respectively by (12) and the bounded-model fit (11). The set \(\{\rho<c\}\), for any fixed \(0<c<\rho_*\), has vanishing relative volume. On its complement divide by \(\rho^2\); on that set use (20). Hence

\[
 \|(d\gamma)^-\|_{L^2_{\rm avg}}\to0.
\tag{21}
\]

The real part \(\operatorname{Re}\zeta=d\rho/2\) is exact, and \(\gamma\) is a globally smooth one-form with \(\delta\gamma=0\). Stokes gives exactly

\[
 \int|d\gamma^+|^2=\int|d\gamma^-|^2,
\]

so \(d\gamma\to0\) in normalized \(L^2\). The one-form and scalar Bochner formulas yield

\[
 \int|\nabla\gamma|^2
 =\int|d\gamma|^2-\int\operatorname{Ric}(\gamma,\gamma),
\]

\[
 \int|\nabla^2\rho|^2
 =\int(\Delta\rho)^2-\int\operatorname{Ric}(d\rho,d\rho).
\]

The \(-g\) terms are small by the original current bound. The Ricci-error pairings are bounded by its \(L^2_{\rm avg}\) norm times the squared \(L^4_{\rm avg}\) norm of \(\gamma\) or \(d\rho\), which tend to zero by (13). Therefore

\[
 \boxed{\|\nabla\zeta\|_{L^2_{\rm avg}}\to0.}\tag{22}
\]

This proves the conclusion sought from the manuscript's current--Hessian correlation \(\mathcal B\) **without adding \(\mathcal B\to0\) as a hypothesis** and without claiming that \(\mathcal B\) itself has been estimated.

### 3.4 The full first torsion projection

Use the already proved actual identity

\[
 N=\sqrt{\rho/2}\,\mathcal L(\nabla\zeta)+\mathcal R_N,
\quad
 |\mathcal R_N|\le C\{\rho^{3/2}(
 |\operatorname{Ric}^{\circ}|+|W^+-W_0|)+|\zeta||P|\}.
\]

Equations (13), (22), and the curvature errors give

\[
 \boxed{\|N\|_{L^2_{\rm avg}}\to0.}\tag{23}
\]

This is the complete displayed first torsion projection, not merely its Dirac trace.

### 3.5 The remaining torsion gradient has a fixed nonzero mean

The unweighted twisted Lichnerowicz identity is now legitimate at the limiting strength:

\[
 \fint|\nabla_{3A}\tau|^2
 =\fint|D^-_{3A}\tau|^2+\fint m
       -\frac32\fint\langle c(F_A^-)\tau,\tau\rangle.
\]

Replace \(f=-iF_A^-\) by its bounded fit \(K\) using Cauchy--Schwarz with the uniformly bounded \(L^2\) norm of \(m\). The Clifford identity and (15) then give

\[
 \frac32\fint\langle c(F_A^-)\tau,\tau\rangle
 =-\frac{27}{32}\fint\frac{\rho^3m^2}{S}
 \longrightarrow-m_*.
\]

The bounded coefficient \(\rho^3/S\), convergence in measure, and uniform integrability of \(m^2\) justify this replacement. Consequently

\[
 \boxed{\fint|\nabla_{3A}\tau|^2\longrightarrow
              2m_* =256/81.}\tag{25}
\]

Thus the strengthened first projection does not imply that the torsion is parallel: its surviving derivative energy is nonzero and sits in the complementary type component.

## 4. What has actually been removed, and what remains

The previous chain had only subcritical torsion-length convergence and weak Dirac control, and had left \(\nabla\zeta\) behind an unresolved current--Hessian covariance. Equations (14)--(16), (22), and (23) genuinely strengthen that chain.

The critical quantity needed for the final signed characteristic flux is still of higher differential order. Neither

\[
 \fint|D\tau|^2\to0,\quad
 \fint|N|^2\to0,\quad
 \fint(m-m_*)^2\to0
\]

controls

\[
 \fint_{\{a<m<b\}}
      |\langle\tau,\nabla\tau\rangle|^2|\nabla\tau|^2,
\tag{24}
\]

or the curvature-weighted radial--horizontal product in `proof:phase-curvature:e3.6`. The first quantity involves fourth powers of **\(\nabla\tau\)**, which contains the original Hessian. Formula (12) controls fourth powers of **\(\nabla\Phi\)**; these must not be conflated.

The local actual simple torsion-zero cores remain compatible with (14)--(23): their contributions to the strong quadratic norms vanish under shrinking, while their transition flux stays of order one. Thus one cannot append an unsupported topological vanishing conclusion to the new strong-current theorem.

The shortest remaining global step is to control the signed interaction in the final identity

\[
 \|\vartheta W^--\widetilde H\|_2^2-
 \|\widetilde H\|_2^2
 =\|\vartheta\mathsf R\|_2^2-
 2\int\vartheta\langle\mathsf R,H^+\rangle
\]

using (14)--(23), the full actual commutator/bracket, and the exterior matching. The old positive \(20V/3\) has already canceled in this identity and cannot be reinserted. A proof of a uniform signed separation, or a complete calibrated closed escape construction, is still required for O10.

## Independent verification within this turn

The slow-truncation lemma was independently checked by the root agent and `o10_counterexample`. The latter supplied the derivative-free weighted Hessian interchange (4), which is stronger and cleaner than commuting the rough Laplacian and integrating a derivative-of-curvature term. Both checks explicitly preserve the distinction between gradient fourth-power uniform integrability and full Hessian-square uniform integrability.
