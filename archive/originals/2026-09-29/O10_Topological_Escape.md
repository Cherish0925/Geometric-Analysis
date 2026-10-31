# O10: a rank-one Chern obstruction by logarithmic resolvent selection

> Application update: the section hypotheses in Section 7 are now proved in `O10_Weak_Bianchi.md` and combined with this lemma in `O10_All_Finite_Density.md`. No first Nijenhuis-bracket prolongation is required. The general no-density-bound constant remains unproved.

2026-09-29. This note proves an analytic lemma, then gives its exact conditional application to the proposed third-torsion line section. The lemma does not assume noncollapse, a Sobolev inequality, an injectivity-radius bound, a Riemann-curvature bound, or convergence of the manifolds. The application requires the separately derived third-section amplitude and derivative estimates; those estimates are not silently assumed to have been proved here.

## 1. The lemma

Let \((M_j,g_j)\) be closed oriented Riemannian four-manifolds, with \(V_j=\operatorname{Vol}(M_j,g_j)\). All norms and integrals in the proof below are normalized by \(V_j\). Let \(L_j\) be Hermitian line bundles with unitary connections, and write their real curvature as \(F_j=-iF_{\nabla_j}\). Assume

\[
\sup_j\left(\fint|\operatorname{Ric}_{g_j}|^2+\fint|F_j|^2\right)<\infty.
\tag{1.1}
\]

Suppose smooth sections \(\sigma_j\) satisfy

\[
|\sigma_j|\longrightarrow c>0\quad\text{in normalized measure},
\qquad \sup_j\fint|\nabla_j\sigma_j|^2<\infty.
\tag{1.2}
\]

Let \(\omega_j\) be closed real two-forms with a decomposition

\[
\omega_j=\omega_{0,j}+e_j,
\qquad \|\omega_{0,j}\|_\infty\le C,
\qquad \fint|e_j|^2\longrightarrow0.
\tag{1.3}
\]

Then

\[
\boxed{\fint F_j\wedge\omega_j\longrightarrow0.}
\tag{1.4}
\]

The notation in (1.4) means \(V_j^{-1}\int F_j\wedge\omega_j\); it is not a pointwise inner-product convention. In particular, if \(F_j\) itself admits (1.3), then

\[
\boxed{\frac{c_1(L_j)^2[M_j]}{V_j}\longrightarrow0.}
\tag{1.5}
\]

The uniform Ricci-energy assumption is essential to the argument. There is no assertion here that a nearly unit section with bounded Dirichlet energy alone rules out line-bundle topology on arbitrarily degenerating metrics.

## 2. Uniformly bounded truncation

Choose a smooth fiberwise radial map \(T\), equal to the identity on a fixed neighborhood of the circle \(|z|=c\), uniformly bounded, and globally Lipschitz. Put

\[
s_j=T(\sigma_j).
\]

This definition is invariant under unitary changes of frame. There are constants \(K,E\), independent of \(j\), such that

\[
\|s_j\|_\infty\le K,\qquad
\fint|\nabla_j s_j|^2\le E,
\qquad d_j:=\fint (|s_j|-c)^2\longrightarrow0.
\tag{2.1}
\]

The last convergence follows from boundedness and convergence in measure. No bound on the untruncated section's fourth power is needed.

## 3. A resolvent parameter selected over logarithmic scales

Write \(\mathcal L_j=\nabla_j^*\nabla_j\). For \(\varepsilon>0\), solve exactly

\[
u_{j,\varepsilon}=(I+\varepsilon\mathcal L_j)^{-1}s_j.
\tag{3.1}
\]

Each inverse exists on the individual compact manifold. The unitary maximum principle gives \(\|u_{j,\varepsilon}\|_\infty\le K\). Spectral calculus for the nonnegative self-adjoint operator \(\mathcal L_j\) gives

\[
\|u_{j,\varepsilon}-s_j\|_2^2
\le\varepsilon\|\nabla_j s_j\|_2^2\le E\varepsilon,
\qquad
\|\nabla_j u_{j,\varepsilon}\|_2^2\le E,
\tag{3.2}
\]

and the exact integrated estimate

\[
\int_0^\infty\|\mathcal L_j u_{j,\varepsilon}\|_2^2\,d\varepsilon
=\|\nabla_j s_j\|_2^2\le E.
\tag{3.3}
\]

For an eigenvalue \(\lambda\ge0\), the identity behind (3.3) is
\(\int_0^\infty \lambda^2(1+\varepsilon\lambda)^{-2}\,d\varepsilon=\lambda\).

Set

\[
\delta_j=d_j+\|e_j\|_2^2+j^{-1}\longrightarrow0.
\]

For sufficiently large \(j\), choose \(\varepsilon_j\) in the interval

\[
\delta_j^{1/2}\le\varepsilon_j\le\delta_j^{1/4}
\tag{3.4}
\]

so that

\[
\varepsilon_j\|\mathcal L_j u_{j,\varepsilon_j}\|_2^2
\le\frac{4E}{|\log\delta_j|}\longrightarrow0.
\tag{3.5}
\]

Such a parameter exists by averaging (3.3) with respect to \(d\varepsilon/\varepsilon\) on (3.4). Abbreviate \(u_j=u_{j,\varepsilon_j}\) and \(K_j=\|\mathcal L_j u_j\|_2^2\). Thus

\[
\varepsilon_j\to0,\quad
\varepsilon_jK_j\to0,\quad
\frac{\|e_j\|_2^2}{\varepsilon_j}\le\sqrt{\delta_j}\to0.
\tag{3.6}
\]

This logarithmic selection is the decisive step. Choosing an arbitrary smoothing parameter only gives \(K_j=O(\varepsilon_j^{-1})\), which leaves a nonvanishing critical error in the argument below.

## 4. Derivative-free Hessian estimate

For any bounded smooth section \(u\) of a unitary bundle on a closed four-manifold, put

\[
I=\fint|\nabla^2u|^2,\qquad J=\fint|\nabla u|^4.
\]

Integrating the divergence of
\(|\nabla u|^2\operatorname{Re}\langle u,\nabla u\rangle\) gives

\[
J\le C\|u\|_\infty I^{1/2}J^{1/2},
\qquad J\le C\|u\|_\infty^2 I.
\tag{4.1}
\]

This is an integrated interpolation identity, not a Sobolev inequality. Interchanging the two covariant derivative slots and integrating by parts gives

\[
I\le \|\nabla^*\nabla u\|_2^2
+C\fint (|\operatorname{Ric}|+|F_{\nabla}|)|\nabla u|^2
+C\|u\|_\infty^2\|F_{\nabla}\|_2^2.
\tag{4.2}
\]

There is no derivative of \(F_{\nabla}\) in (4.2). One direct verification is to apply the integrated covariant Hodge--Weitzenböck identity to the bundle-valued one-form \(\nabla u\): its exterior covariant derivative is \(F_{\nabla}u\), and its covariant codifferential is \(\nabla^*\nabla u\). The curvature term on its one-form index contains only Ricci, and the bundle term is algebraic in \(F_{\nabla}\). Equivalently, use \(\nabla_i\nabla_j u-\nabla_j\nabla_i u=F_{ij}u\), symmetrize the Hessian square, and commute the remaining derivatives on the one-form index. Cauchy--Schwarz, (4.1), and Young's inequality give, under (1.1),

\[
\boxed{\fint|\nabla u_j|^4+\fint|\nabla^2u_j|^2
\le C(1+K_j).}
\tag{4.3}
\]

Here \(C\) depends on the uniform bounds in (1.1), (2.1), and dimension, and not on \(\varepsilon_j\), charts, or a Sobolev constant.

## 5. Small quadratic energy on the amplitude-transition region

Fix \(0<a<b<c\), and let

\[
B_j=\{|u_j|\le b\}.
\]

By (2.1), (3.2), and (3.4),

\[
\mu_j(B_j)\le C(d_j+E\varepsilon_j)\le C\varepsilon_j,
\qquad \mu_j=dV_j/V_j.
\tag{5.1}
\]

Consequently (4.3) and (3.6) imply

\[
\fint_{B_j}|\nabla u_j|^2
\le \mu_j(B_j)^{1/2}
 \left(\fint|\nabla u_j|^4\right)^{1/2}
\le C\sqrt{\varepsilon_j(1+K_j)}\longrightarrow0.
\tag{5.2}
\]

At the same time,

\[
\|e_j\|_2
\left(\fint|\nabla u_j|^4\right)^{1/2}
\le C\sqrt{\|e_j\|_2^2(1+K_j)}\longrightarrow0,
\tag{5.3}
\]

because \(\|e_j\|_2^2 K_j=(\|e_j\|_2^2/\varepsilon_j)(\varepsilon_jK_j)\to0\).

## 6. Rank-one transgression

On \(\{u_j\ne0\}\), the unit section \(u_j/|u_j|\) trivializes the line bundle. Its real connection form \(\alpha_j\) satisfies

\[
d\alpha_j=F_j,\qquad
|\alpha_j|\le C|\nabla u_j|/|u_j|.
\]

Choose a fixed smooth cutoff \(\chi\), zero on \([0,a]\), one on \([b,\infty)\), and put \(\chi_j=\chi(|u_j|)\). Then \(\chi_j\alpha_j\) is a globally smooth real one-form. Since \(d\omega_j=0\),

\[
\int F_j\wedge\omega_j
=\int(1-\chi_j)F_j\wedge\omega_j
-\int d\chi_j\wedge\alpha_j\wedge\omega_j.
\tag{6.1}
\]

The first term tends to zero after division by \(V_j\): by (1.1),

\[
\left|\fint(1-\chi_j)F_j\wedge\omega_j\right|
\le C\|F_j\|_2\mu_j(B_j)^{1/2}
+\|F_j\|_2\|e_j\|_2\to0.
\tag{6.2}
\]

The second term is supported where \(a\le|u_j|\le b\), and there
\(|d\chi_j\wedge\alpha_j|\le C|\nabla u_j|^2\). Decomposing \(\omega_j\) as in (1.3) gives

\[
\left|\fint d\chi_j\wedge\alpha_j\wedge\omega_j\right|
\le C\fint_{B_j}|\nabla u_j|^2
+C\|e_j\|_2\left(\fint|\nabla u_j|^4\right)^{1/2}\to0
\tag{6.3}
\]

by (5.2)--(5.3). Equations (6.1)--(6.3) prove the lemma. Taking \(\omega_j=F_j\) and using \(c_1(L_j)=[F_j/(2\pi)]\) proves (1.5).

## 7. Conditional application to the third torsion line

Suppose the weak third-torsion analysis produces, from a hypothetical O10 zero sequence, a section

\[
\sigma_j\in\Gamma(L_j^{\otimes5})
\]

with

\[
|\sigma_j|\to c_\sigma>0\text{ in normalized measure},
\qquad \sup_j\fint|\nabla_{5A_j}\sigma_j|^2<\infty.
\tag{7.1}
\]

The original zero-endpoint assumptions give bounded normalized Ricci energy, and the actual determinant-curvature fit gives

\[
-iF_{5A_j}=5(-iF_{A_j})=F_{0,j}+e_j,
\qquad |F_{0,j}|\le C,\quad\|e_j\|_{2,\mathrm{avg}}\to0.
\tag{7.2}
\]

Hence the lemma forces

\[
25\,a_j^2/V_j\longrightarrow0.
\tag{7.3}
\]

But the already established actual zero-endpoint identities give

\[
a_j^2/V_j\longrightarrow\frac1{6\pi^2}>0.
\tag{7.4}
\]

Thus (7.1) excludes the zero endpoint. In particular, if (7.1) is established with constants depending on a fixed finite bound \(\chi/A\le B\), this proves O10 for **every fixed finite \(B\)** after the existing finite-parameter estimate and exact Yamabe transfer. It would replace the earlier finite threshold \(39/4+\delta\) by arbitrary fixed density bounds.

This note does **not** claim (7.1) without a bound on the negative Weyl budget. An estimate whose right side grows with \(\fint|W^-|^2\) is not the uniform bound required by the lemma along an unrestricted sequence.

## 8. What the older rank-two argument could not see

For a rank-two section, Chern localization involves a fourth-power derivative term. Fixed-parameter smoothing and an amplitude-exceptional set of measure \(O(\varepsilon)\) do not make its fourth-power energy vanish. For a line section, the topological pairing in (6.1) involves only the **quadratic** derivative expression \(d\chi\wedge\alpha\), paired with a bounded curvature model. The logarithmic resolvent choice upgrades its estimate from \(O(1)\) to \(o(1)\).

This distinction is the mathematical reason to pass from the opposite rank-two torsion bundle to the third-torsion line. It is not an assertion that rank-two characteristic energy or the existing Weyl tail disappears automatically.
