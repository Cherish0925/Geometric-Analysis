# Independent proof audit: the logarithmic line-bundle resolvent lemma

2026-09-29. The construction was proposed by the parallel `topological_escape` branch and audited independently here. Unlike the false inference in `O10_LineBundle_Limitation.md`, this statement uses the Ricci curvature essentially.

## Statement

Let \((M_j,g_j)\) be closed oriented four-manifolds, \(E_j\) Hermitian line bundles with unitary connections, and let every integral below use normalized volume. Assume:

1. \(s_j\) are smooth uniformly bounded sections, \(\fint|\nabla s_j|^2\le E\), and \(|s_j|\to c>0\) in normalized L2;
2. \(\mathrm{Ric}_{g_j}=R_{0,j}+R_{e,j}\), with \(|R_{0,j}|\le C\) and \(\|R_{e,j}\|_{2,\mathrm{avg}}\to0\);
3. \(F_j=F_{0,j}+F_{e,j}\), with \(|F_{0,j}|\le C\) and \(\|F_{e,j}\|_{2,\mathrm{avg}}\to0\).

The bounded model F0 need not be closed. The actual curvature F is closed because the bundle has rank one. Then

\[
 \boxed{\frac{c_1(E_j)^2[M_j]}{V_j}\longrightarrow0.}
\tag{1}
\]

No Sobolev, injectivity-radius, diameter, or noncollapse bound is used.

## 1. An unweighted second-derivative bound

Write \(L=\nabla^*\nabla\). For any uniformly bounded section u with \(\fint|\nabla u|^2\le E\), derivative-free Hessian interchange and integration by parts give

\[
 \fint|\nabla^2u|^2
 \le C\left(1+\|Lu\|_{2,\mathrm{avg}}^2\right)
  +\eta\fint|\nabla u|^4,
\tag{2}
\]

for an arbitrarily small fixed eta, with its corresponding constant C independent of j and u. Here curvature paired with \(|\nabla u|^2\) is split into bounded and error terms; Young's inequality bounds each error term by eta times the fourth-power gradient plus a constant times the squared L2 error. The commutator acting on u contributes \(|F u|^2\), also bounded in average. No curvature derivative is estimated.

For clarity, the derivative-free identity starts with

\[
 \int|\nabla^2u|^2
 =\int\operatorname{Re}\langle\nabla_i\nabla_j u,
                  \nabla_j\nabla_i u\rangle
   +\frac12\int\sum_{i,j}|F_{ij}u|^2.
\]

After integrating and commuting on the covector-valued \(\nabla u\), the remaining curvature terms are bounded by

\[
 C\int(|\mathrm{Ric}|+|F|)|\nabla u|^2;
\]

the potential term is exactly \(\int|Lu|^2\). This establishes (2).

The bounded-section interpolation follows by integrating the divergence of \(|\nabla u|^2\operatorname{Re}\langle u,\nabla u\rangle\). With M a bound for \(|u|\), it yields

\[
 \fint|\nabla u|^4
 \le C_M\left(\fint|\nabla^2u|^2+\|Lu\|_2^2\right).
\tag{3}
\]

Choose eta small relative to \(C_M\) and absorb (3) into (2). Consequently

\[
 \boxed{\fint\bigl(|\nabla^2u|^2+|\nabla u|^4\bigr)
 \le C\bigl(1+\|Lu\|_{2,\mathrm{avg}}^2\bigr).}
\tag{4}
\]

The constant depends on E, M, the bounded curvature models, and an eventual bound for the L2 errors. It is independent of a resolvent parameter.

## 2. Select a parameter by logarithmic averaging

Let

\[
 u_\epsilon=(I+\epsilon L)^{-1}s.
\]

The connection-Laplacian maximum principle gives \(\|u_\epsilon\|_\infty\le\|s\|_\infty\). The spectral theorem gives

\[
 \|\nabla u_\epsilon\|_2^2\le\|\nabla s\|_2^2\le E,
 \qquad \|u_\epsilon-s\|_2^2\le\epsilon E,
\tag{5}
\]

and, exactly,

\[
 \int_0^1\|Lu_\epsilon\|_2^2\,d\epsilon
 =\sum_\lambda\frac{\lambda^2}{1+\lambda}|s_\lambda|^2
 \le\sum_\lambda\lambda|s_\lambda|^2\le E.
\tag{6}
\]

All squared coefficient norms here are normalized by V. Choose positive \(\delta_j\downarrow0\) dominating

\[
 \big\||s_j|-c\big\|_2^2+\|F_{e,j}\|_2^2.
\]

Equation (6), viewed with logarithmic measure \(d\epsilon/\epsilon\), supplies a parameter

\[
 \delta_j^{1/2}\le\epsilon_j\le\delta_j^{1/4},
 \qquad
 \epsilon_j\|Lu_{\epsilon_j}\|_2^2
 \le\frac{4E}{\log(1/\delta_j)}\longrightarrow0.
\tag{7}
\]

Fix a low-amplitude set \(Z_j=\{|u_{\epsilon_j}|<3c/4\}\). Chebyshev and (5) show

\[
 \frac{\operatorname{Vol}Z_j}{V_j}\le C(\delta_j+\epsilon_j)
 \le C\epsilon_j.
\tag{8}
\]

By (4), (7), and Hölder,

\[
 \fint_{Z_j}|\nabla u_{\epsilon_j}|^2
 \le C\sqrt{\epsilon_j}
       \sqrt{1+\|Lu_{\epsilon_j}\|_2^2}
 \longrightarrow0.
\tag{9}
\]

Moreover,

\[
 \|F_{e,j}\|_2
 \left(\fint|\nabla u_{\epsilon_j}|^4\right)^{1/2}
 \le C\sqrt{\delta_j}
       \sqrt{1+\|Lu_{\epsilon_j}\|_2^2}
 \longrightarrow0,
\tag{10}
\]

because \(\delta_j/\epsilon_j\le\sqrt{\delta_j}\).

## 3. Rank-one transgression needs only curvature times gradient squared

Write the actual curvature as \(F=i f\) for a real closed two-form f. On \(u\ne0\), the unit section \(u/|u|\) defines a real connection one-form

\[
 \alpha=\frac{\operatorname{Im}\langle u,\nabla u\rangle}{|u|^2},
 \qquad d\alpha=f,
\]

up to an immaterial simultaneous sign convention. Let \(\chi(|u|^2)\) vanish for \(|u|\le c/4\) and equal one for \(|u|\ge c/2\). Then \(B=\chi\alpha\) extends to a smooth global one-form. Since f is closed,

\[
 \int f\wedge f
 =\int(1-\chi)f\wedge f
  -\int d\chi\wedge\alpha\wedge f.
\tag{11}
\]

The first integrand is supported in Z. On the cutoff shell, \(|d\chi\wedge\alpha|\le C_c|\nabla u|^2\). Hence

\[
 \left|\fint f\wedge f\right|
 \le C_c\left[
  \fint_Z|F|^2+
  \fint_Z|F_0||\nabla u|^2+
  \fint|F_e||\nabla u|^2\right].
\tag{12}
\]

The first term tends to zero by (8) and \(F_e\to0\) in L2. The second tends to zero by (9) and boundedness of F0. The third tends to zero by (10). Chern–Weil now proves (1).

## Audit conclusion

The logarithmic choice is essential: a generic small resolvent parameter would give only \(\epsilon\|Lu_\epsilon\|_2^2\le E\), and (9) would not tend to zero. Integrating over a growing logarithmic interval improves this to a vanishing quantity without a uniform spectral gap. Rank one is also essential in (11): the actual curvature is closed, and the transgression couples it to a quadratic gradient term.

This proof validates the proposed lemma. Applying it to the actual derived section still requires the separately proved positive amplitude limit and H1 bound for that section, and the actual positive value of its normalized Chern square.
