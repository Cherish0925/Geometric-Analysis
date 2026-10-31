# O10 closes at every fixed finite Euler density

Date: 2026-09-29. This continuation uses the already established strong-current result, a direct mass--phase--Dirac reduction, the new constant-length derivative lemma, and a logarithmic resolvent argument for a line bundle. The conclusion removes the previous numerical Euler-density threshold. It does not assert a constant independent of the Euler-density bound.

## 1. Precise conclusion

Retain the original O10 actual conformal monopole input, the positive projection budget \(p\ge A>0\), and \(a^2\ge T_+\). For every fixed finite \(B\), there exists \(c(B)>0\) such that

\[
 \boxed{\frac{\chi(M)}A\le B
 \quad\Longrightarrow\quad
 \fint_M|\operatorname{Ric}+g|^2+\frac{D_\beta(g)}{V(g)}
 \ge c(B)\frac{(\beta-2)^2}{\beta^2},\qquad\beta\ge2.}
\tag{1}
\]

The class of admissible metrics and the actual supplier are exactly those of the original O10 problem. There is no added pointwise Ricci bound, diameter bound, noncollapse hypothesis or Sobolev inequality. The dependence on the fixed number \(B\) is retained.

Here \(a=c_1(L)\), \(p=(a_g^+)^2\), \(T_+=2\chi(M)+3\operatorname{sign}(M)\), and

\[
 D_\beta=(1+\beta^{-1})\int s_g^2
 +6(\beta+1)\int|W_g^+|^2-72\pi^2p.
\]

Weyl norms are Hilbert--Schmidt norms on two-forms; Ricci norms are tensor norms. The actual single solution is taken on the negative Yamabe representative normalized by \(s=-4\). An application to every original metric uses the original conformal-class supplier and the stated conformal comparison. Throughout a sequence, all analytic norms are taken with respect to \(dV_j/V_j\).

Equivalently, an unrestricted hypothetical O10 zero-end sequence must have

\[
 \boxed{\chi(M_j)/A_j\longrightarrow+\infty}
\tag{2}
\]

along the endpoint subsequence. The statement does not yet rule out this final escape regime.

## 2. The new analytic lemma: a line cannot keep characteristic square through this bounded-energy limit

Consider closed oriented Riemannian four-manifolds \((M_j,g_j)\), Hermitian line bundles \(K_j\) and unitary connections. Write the real curvature as \(F_j=-iF^{K_j}\). Suppose:

1. \(\fint|\operatorname{Ric}_{g_j}|^2\le C_R\).
2. \(F_j=F_{0,j}+e_j\), with \(|F_{0,j}|\le C_F\) and \(\|e_j\|_{2,\mathrm{avg}}\to0\). The bounded model need not be closed.
3. Smooth sections \(\sigma_j\) satisfy \(\fint|\nabla\sigma_j|^2\le E\), and \(|\sigma_j|\to\ell>0\) strongly in normalized \(L^2\).

Then

\[
 \boxed{\frac{c_1(K_j)^2[M_j]}{V_j}
 =\frac1{4\pi^2}\fint F_j\wedge F_j\longrightarrow0.}
\tag{3}
\]

The notation on the right means the coefficient of the four-form relative to the volume form. The conclusion is signed convergence; no sign of the characteristic number is assumed.

### 2.1 A bounded cap and its spectral regularization

Apply a fixed smooth radial cap which is the identity near radius \(\ell\), has uniformly bounded derivative, and has bounded image. The resulting sections \(s_j\) satisfy

\[
 |s_j|\le M,\qquad \fint|\nabla s_j|^2\le E',
 \qquad d_j:=\fint(|s_j|-\ell)^2\to0.
\tag{4}
\]

Let \(L_j=\nabla^*\nabla\) and, for \(\varepsilon>0\), put

\[
 u_{j,\varepsilon}=(I+\varepsilon L_j)^{-1}s_j.
\]

The connection-Laplacian maximum principle and the spectral theorem give

\[
 |u_{j,\varepsilon}|\le M,\qquad
 \fint|u_{j,\varepsilon}-s_j|^2\le\varepsilon E',
 \qquad \fint|\nabla u_{j,\varepsilon}|^2\le E'.
\tag{5}
\]

For \(K_j(\varepsilon)=\fint|L_j u_{j,\varepsilon}|^2\), the exact spectral calculation is

\[
 \int_0^1K_j(\varepsilon)\,d\varepsilon
 =\frac1{V_j}\sum_\nu
 \frac{\lambda_\nu^2}{1+\lambda_\nu}|(s_j)_\nu|^2
 \le\fint|\nabla s_j|^2\le E'.
\tag{6}
\]

No uniform spectral gap is required.

Choose numbers \(\delta_j\downarrow0\) with

\[
 d_j+\|e_j\|_{2,\mathrm{avg}}^2\le\delta_j<1.
\]

Since

\[
 \int_{\delta_j^{1/2}}^{\delta_j^{1/4}}
 K_j(\varepsilon)\,d\varepsilon
 =\int_{\delta_j^{1/2}}^{\delta_j^{1/4}}
 [\varepsilon K_j(\varepsilon)]\frac{d\varepsilon}{\varepsilon}
 \le E',
\]

there exists \(\varepsilon_j\) in this interval such that

\[
 \boxed{\varepsilon_jK_j(\varepsilon_j)
 \le\frac{4E'}{|\log\delta_j|}\longrightarrow0.}
\tag{7}
\]

Write \(u_j=u_{j,\varepsilon_j}\), \(K_j=K_j(\varepsilon_j)\). In particular \(\varepsilon_j\to0\), while (7) is stronger than the elementary bound \(K_j\le E'/\varepsilon_j\).

### 2.2 The geometry-free fourth-power estimate

For a bounded section \(u\) of a line bundle over a closed four-manifold, derivative interchange and integration by parts give

\[
 \fint\bigl(|\nabla^2u|^2+|\nabla u|^4\bigr)
 \le C_M\left\{\fint|Lu|^2+
 \fint\bigl(|\operatorname{Ric}|^2+|F|^2\bigr)\right\}.
\tag{8}
\]

A harmless additive constant can be included. Only the Ricci contraction occurs when commuting derivatives on the covector slot. Bundle curvature enters without derivatives. To see the absorption, set \(I=\int|\nabla^2u|^2\), \(J=\int|\nabla u|^4\) and \(K=\int|Lu|^2\). Interchanging the two covariant derivatives first gives

\[
 I\le C K+C M^2\int|F|^2+
 C\int(|\operatorname{Ric}|+|F|)|\nabla u|^2.
\]

Integration of \(\operatorname{div}(|\nabla u|^2\operatorname{Re}\langle u,\nabla u\rangle)\) gives \(J\le C_M(I+K)\). Cauchy--Schwarz and Young then absorb \(I\) and yield (8). No Sobolev estimate or derivative of curvature is used.

Thus in our sequence

\[
 \fint|\nabla u_j|^4\le C(1+K_j).
\tag{9}
\]

Let \(Z_j=\{|u_j|\le3\ell/4\}\). From (4)--(5),

\[
 \frac{\operatorname{Vol}(Z_j)}{V_j}
 \le C(d_j+\varepsilon_j E')\le C\varepsilon_j.
\]

Consequently

\[
 \boxed{\fint_{Z_j}|\nabla u_j|^2
 \le C\sqrt{\varepsilon_j(1+K_j)}\longrightarrow0.}
\tag{10}
\]

This is the estimate unavailable for the unregularized \(H^1\) section.

### 2.3 Rank-one transgression and its error bounds

Put \(a_j=|u_j|^2\), \(j_j=\operatorname{Im}\langle u_j,\nabla u_j\rangle\). Choose a fixed smooth cutoff \(\chi(a)\), zero for \(a\le(\ell/2)^2\) and one for \(a\ge(3\ell/4)^2\). The real one-form

\[
 \theta_j=\chi(a_j)j_j/a_j
\]

is globally smooth, extended by zero at zeros of \(u_j\). For a line bundle the exact local identity is

\[
 d\theta_j=\chi(a_j)F_j+
 \chi'(a_j)\,da_j\wedge j_j/a_j.
\tag{11}
\]

Its second term has norm at most \(C_\ell|\nabla u_j|^2\) and is supported in \(Z_j\). Since \(dF_j=0\), Stokes gives

\[
 \left|\fint F_j\wedge F_j\right|
 \le C\fint_{Z_j}|F_j|^2+
 C\fint_{Z_j}|F_j|\,|\nabla u_j|^2.
\tag{12}
\]

The first term tends to zero because \(F_j\) has a uniformly bounded model and an \(L^2\)-small error. For the second term, split \(F_j=F_{0,j}+e_j\). Its bounded-model part tends to zero by (10). Its error part satisfies

\[
 \fint|e_j|\,|\nabla u_j|^2
 \le C\sqrt{\delta_j(1+K_j)}\longrightarrow0,
\tag{13}
\]

since \(\delta_j/\varepsilon_j\le\delta_j^{1/2}\) and \(\varepsilon_jK_j\to0\). This proves (3).

## 3. Applying the lemma to the actual O10 system

Suppose that a scalar-minus-four actual endpoint sequence has

\[
 \beta_j\to\infty,\qquad
 \kappa_j=P_j/V_j+D_{\beta_j}/V_j\to0,
 \qquad \chi(M_j)/A_j\le B<\infty.
\tag{14}
\]

The existing curvature/topological budgets imply \(\fint|W^-|^2\le C_B\). The preceding strong-current and resolvent arguments produce \(v\in S^-\otimes L\) with

\[
 v\text{ bounded},\quad |v|^2\to m_*,\quad
 \nabla^*\nabla v-2v\to0\text{ in }L^2,
 \quad \|\nabla v\|_4+\|\nabla^2v\|_2\le C_B.
\]

The direct mass--phase--Dirac reduction leaves only \(C=(\nabla_{\bar Z_2}v)_2\). Indeed, the inherited \(N_v=(\nabla v)^{1,0}_{J_+}\to0\) gives \(A_i=\nabla_{Z_i}v\to0\). The scalar identity and bounded second-derivative budget give \(da\to0\), where \(a=|v|^2\). The exact phase identity \(|j_v+J_+da/2|^2\le2a|N_v|^2\) gives \(j_v\to0\). In a frame with \(v=\sqrt a\,e_1\),
\[
 (\nabla v)_1=(da/2+i j_v)/\sqrt a,
\]
so every first spinor component tends to zero on fixed positive-amplitude sets. Low-amplitude sets contribute \(o(1)\) to \(\fint|\nabla v|^2\) by the \(L^4\) bound. Thus \(B_1,C_1\to0\), and the Clifford identity \(D^-v=((A_1)_1-(A_2)_2,B_2+C_1)\) gives \(B_2\to0\) as well. No bracket prolongation estimate is required.

The new covariance argument in `O10_Weak_Bianchi.md` proves

\[
 |\nabla v|^2\to2m_*,\quad |C|^2\to4m_*,\quad
 |c|^2\to1\quad\text{in measure},
 \qquad c=C/(2|v|).
\tag{15}
\]

For completeness, the new covariance test is
\(T(q)=q/(1+q)\), \(q=|\nabla v|^2\). Since
\(\Delta|v|^2=4|v|^2-2q+o_{L^2}(1)\),
\(d|v|^2\to0\) in \(L^2\), and
\(|dT(q)|\le C|\nabla^2v|\), testing yields

\[
 \fint\frac{(q-2m_*)^2}{1+q}\longrightarrow0.
\]

Define the actual polynomial section

\[
 \sigma=\Phi\wedge t(v)\in\Gamma(L^5).
\]

The bundle power follows from \(t(v)\in S^+\otimes L^4\) and \(\det S^+=L\). In the surviving first-jet configuration,

\[
 t(v)=(0,2|v|^3c),\qquad
 |\sigma|^2\to4\rho_*m_*^3>0.
\]

Moreover

\[
 |\sigma|\le C|\nabla v|,
\quad
 |\nabla\sigma|\le C\bigl(
 |\nabla\Phi||\nabla v|+|\nabla v|^2+|\nabla^2v|\bigr),
\]

so \(\|\sigma\|_4+\|\nabla\sigma\|_2\le C_B\). In particular \(|\sigma|\) tends to its positive constant strongly in \(L^2\).

The three hypotheses of the line lemma now hold:

- \(\operatorname{Ric}=-g+o_{L^2}(1)\), so its normalized square is uniformly bounded.
- The curvature of \(L^5\) is \(5F_A\). Its self-dual part is bounded pointwise by the actual spinor equation; its anti-self-dual part has the previously proved bounded same-field fit plus an \(L^2\)-small error.
- The section \(\sigma\) has the amplitude and first-derivative bounds just proved.

The lemma forces

\[
 \frac{c_1(L^5)^2[M_j]}{V_j}\to0.
\]

But the actual endpoint characteristic budgets give

\[
 \frac{c_1(L^5)^2[M_j]}{V_j}
 =25\frac{a^2[M_j]}{V_j}
 \longrightarrow\frac{25}{6\pi^2}>0.
\tag{16}
\]

This is a contradiction. Every fixed finite-density zero-end sequence is therefore excluded.

## 4. Returning to all parameters and the original metric

The existing finite-parameter estimate excludes a sequence with vanishing ratio in (1) and bounded \(\beta\); hence failure of (1) at a fixed \(B\) would force \(\beta\to\infty\) and \(\kappa_\beta\to0\). The exact Yamabe transfer of the manuscript gives

\[
 \widehat\kappa_\beta\le
 \frac{\kappa_\beta}{1-\sqrt{\kappa_\beta}-\kappa_\beta/16}
\]

on its small-defect branch. Thus such a failure on the original metrics supplies precisely a scalar-minus-four sequence of the form (14), which has just been excluded. This proves (1).

## 5. Exact remaining boundary of this result

The theorem now applies to every prescribed finite \(B\), rather than only \(B<39/4+\delta_*\). It completes the topology-density-controlled version of O10 stated in the original research directive.

The proof uses \(B\) to bound \(\nabla^2v\), \(\nabla v\) in \(L^4\), and ultimately \(\nabla\sigma\) in \(L^2\). It does not provide these bounds uniformly if \(\chi/A\to\infty\). Consequently it does not prove an absolute \(c>0\) for the full unrestricted O10 class. Such a statement requires a further argument excluding simultaneous unbounded opposite-Weyl energy and derivative energy, or a genuine counterexample satisfying the original actual hypotheses.

### 5.1 Where an unbounded opposite-Weyl budget would enter

Write \(b_j=\fint|W^-|^2\). The present proof has three specific uses of a uniform bound on \(b_j\):

1. The derivative-interchange estimate on \(E_-=S^-\otimes L\) gives \(\fint(|\nabla^2v|^2+|\nabla v|^4)\le C(1+b_j)\). The negative-spin connection contains \(W^-\); the estimate does not discard that block.
2. The scalar mass-gradient and covariance tests use \(\|\Delta|v|^2\|_2\) and \(\|\nabla^2v\|_2\). They therefore also need the same bound before the positive constant modulus of \(\sigma\) is obtained. For example, \(\|da\|_2^2\le\|a-m_*\|_2\|\Delta a\|_2\) pairs a small amplitude error with a quantity growing with \(b_j\).
3. The first-derivative estimate for \(\sigma\) uses \(\nabla^2v\), \(\nabla v\otimes\nabla v\), and \(\nabla\Phi\otimes\nabla v\). Their \(L^2\) bounds again depend on \(b_j\). The rank-one lemma requires a uniform bound along the sequence.

The direct mass--phase--Dirac reduction avoids the earlier Nijenhuis-bracket adjoint estimate entirely, but it still uses the mass-gradient conclusion in item 2. A future estimate only bounding a selected component of \(\nabla\sigma\) would not by itself justify the unrestricted conclusion; it must also preserve the constant-modulus conclusion, or replace that step. No rate comparison between the original endpoint error and \(b_j\) is imposed in unrestricted O10, so none may be inserted when passing to a subsequence.

## 6. Proof provenance within this continuation

The rank-one logarithmic-resolvent lemma was developed in parallel in `O10_Topological_Escape.md` and independently checked in deriving Section 2 here. That note proves the more general pairing conclusion \(V^{-1}\int F_j\wedge\omega_j\to0\) for a closed two-form \(\omega_j\) with a bounded model and an \(L^2\)-small remainder. Only the special case \(\omega_j=F_j\) is needed above.

The constant-length derivative and \(L^5\)-section calculations are detailed in `O10_Weak_Bianchi.md`; their scalar test, complex-frame norm factors, bundle exponent and derivative bound received a separate algebraic check. The inherited strong-current result remains a prerequisite, rather than a conclusion silently reproved by the rank-one lemma.
