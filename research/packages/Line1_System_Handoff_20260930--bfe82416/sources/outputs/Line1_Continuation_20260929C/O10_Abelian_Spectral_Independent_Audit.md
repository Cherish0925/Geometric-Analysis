# Independent audit: the Abelian spectral-selection lemma

2026-09-29. This is an independent check of the spectral-pigeonhole construction proposed in the present continuation. It explains why the construction resolves the previous lack of uniform integrability of a nearly nonzero line section's gradient. The lemma is special to the Abelian characteristic form: its transgression is linear in the phase connection and has no cubic phase term.

## 1. Precise geometric lemma

Let `(M_j,g_j)` be closed oriented four-manifolds, `L_j` Hermitian line bundles with unitary connections, and use normalized volume in every norm. Assume

\[
 \operatorname{Ric}_{g_j}=R_{0,j}+r_j,\quad
 F_j=F_{0,j}+e_j,\quad
 |R_{0,j}|+|F_{0,j}|\le C,
 \qquad \|r_j\|_2+\|e_j\|_2\to0.
\tag{1.1}
\]

Suppose smooth sections `sigma_j` satisfy, for a fixed `a_*>0`,

\[
 |\sigma_j|\to a_*\text{ in normalized measure},
 \qquad \fint|\nabla\sigma_j|^2\le E<\infty.
\tag{1.2}
\]

No pointwise bound on `sigma_j` is needed. Then

\[
 \boxed{\frac{c_1(L_j)^2[M_j]}{V_j}\longrightarrow0.}
\tag{1.3}
\]

The constants can depend on `E`, the fixed amplitude, and the bounded models, but do not require a Sobolev constant, noncollapse, diameter, injectivity radius, or curvature derivatives.

## 2. Bounded radial cap and error parameter

Choose a fixed smooth radial map `T` equal to the identity near `a_*` and uniformly bounded in norm and derivative. Put `s_j=T(sigma_j)`. Then

\[
 |s_j|\le C,
 \quad |s_j|\to a_*\text{ in measure},
 \quad \fint|\nabla s_j|^2\le C E.
\]

Boundedness gives `avg (|s_j|-a_*)² -> 0`. Choose any positive sequence `delta_j -> 0` satisfying

\[
 \delta_j\ge\fint(|s_j|-a_*)^2+
 \|e_j\|_2^2+\|r_j\|_2^2.
\tag{2.1}
\]

One may add `1/j` to the right side to ensure strict positivity.

## 3. Spectral selection

Write `L=nabla* nabla` and, for epsilon positive, define

\[
 u_\epsilon=(I+\epsilon L)^{-1}s.
\tag{3.1}
\]

The maximum principle gives `||u_epsilon||infinity <= ||s||infinity`. Spectral calculus for the nonnegative self-adjoint connection Laplacian yields the exact estimates

\[
 \|u_\epsilon-s\|_2^2\le\epsilon\|\nabla s\|_2^2,
 \qquad \|\nabla u_\epsilon\|_2^2\le\|\nabla s\|_2^2,
\tag{3.2}
\]

\[
 \int_0^1\|Lu_\epsilon\|_2^2\,d\epsilon
 \le\|\nabla s\|_2^2.
\tag{3.3}
\]

For an eigenvalue `lambda`, the last assertion is the elementary identity

\[
 \int_0^1\frac{\lambda^2}{(1+\epsilon\lambda)^2}\,d\epsilon
 =\frac{\lambda^2}{1+\lambda}\le\lambda.
\]

Apply (3.3) on the interval `[delta_j^(1/2), delta_j^(1/4)]`, with measure `d epsilon/epsilon`. There exists a choice `epsilon_j` in that interval for which

\[
 \epsilon_j\|Lu_{\epsilon_j}\|_2^2
 \le\frac{4CE}{|\log\delta_j|}\to0.
\tag{3.4}
\]

In particular, `epsilon_j -> 0`, `delta_j/epsilon_j -> 0`, and

\[
 \epsilon_j\bigl(1+\|Lu_{\epsilon_j}\|_2^2\bigr)\to0.
\tag{3.5}
\]

All these statements hold for the normalized Hilbert-space inner product. The spectrum need not have a uniform positive lower bound.

## 4. Hessian and fourth-gradient bound with only L2 forcing

The unweighted Hessian interchange and bounded-section interpolation apply to `u=u_epsilon`, with `h=Lu` merely in `L2`. They give

\[
 I=\fint|\nabla^2u|^2
 \le C\|h\|_2^2+C\fint(|\operatorname{Ric}|+|F|)|\nabla u|^2
 +C\fint|F|^2,
\]

\[
 J=\fint|\nabla u|^4
 \le C\bigl(I+\|h\|_2^2\bigr).
\]

The second inequality follows by integrating `div(|nabla u|² Re<u,nabla u>)`. Its forcing term is at most `C||h||2 sqrt(J)`, and its Hessian term at most `C sqrt(IJ)`.

Split Ricci and bundle curvature as in (1.1). The bounded portions multiply `avg |nabla u|² <= CE`. Apply Young's inequality to the error portions times `|nabla u|²`, choosing a small multiple of `J` and absorbing after the interpolation estimate. This proves

\[
 \boxed{\fint|\nabla^2u|^2+\fint|\nabla u|^4
 \le C_E\bigl(1+\|Lu\|_2^2\bigr).}
\tag{4.1}
\]

It uses no derivative of the curvature: after Hessian interchange, the only derivative of `h` is integrated back to `||h||2²`. This estimate remains valid even though `||Lu_epsilon||infinity` need not be uniformly bounded as epsilon tends to zero.

## 5. The low-amplitude gradient energy disappears

Fix `0<c_0<c_1<a_*` and let `Z_j={|u_epsilon_j|<=c_1}`. Equations (2.1) and (3.2) imply

\[
 \frac{\operatorname{Vol}(Z_j)}{V_j}
 \le C(\delta_j+\epsilon_j).
\tag{5.1}
\]

By Cauchy–Schwarz and (4.1),

\[
 \fint_{Z_j}|\nabla u_{\epsilon_j}|^2
 \le C_E\sqrt{(\delta_j+\epsilon_j)
          (1+\|Lu_{\epsilon_j}\|_2^2)}\to0.
\tag{5.2}
\]

The convergence follows from `delta_j/epsilon_j -> 0` and (3.5). In addition,

\[
 \fint |e_j|\,|\nabla u_{\epsilon_j}|^2
 \le C_E\sqrt{\delta_j}
          \sqrt{1+\|Lu_{\epsilon_j}\|_2^2}\to0.
\tag{5.3}
\]

This second estimate is essential. It cannot be replaced by an unsupported claim that a product of an `L2`-small curvature error and an `L2`-bounded gradient square is automatically small uniformly in epsilon.

## 6. Rank-one transgression closes the proof

On the nonzero set of `u`, put `n=u/|u|`, let `alpha=-i<n,nabla n>`, and write `f=-iF`. Then `d alpha=f`. Consequently

\[
 d(\alpha\wedge f)=f\wedge f.
\]

Choose a smooth cutoff `chi(|u|²)` equal to one below `c_0²` and zero above `c_1²`. The form `(1-chi) alpha wedge f` vanishes near every zero and extends smoothly. Stokes gives

\[
 \int f\wedge f
 =\int\chi f\wedge f+
   \int d\chi\wedge\alpha\wedge f.
\tag{6.1}
\]

The first term divided by volume tends to zero by (1.1) and (5.1). On the transition set all amplitude denominators are bounded, and

\[
 |d\chi\wedge\alpha\wedge f|
 \le C|F|\,|\nabla u|^2.
\]

Split `F=F0+e`. The bounded part tends to zero by (5.2), and the error by (5.3). Thus `avg f wedge f -> 0`, proving (1.3), including its fixed `1/(4 pi²)` normalization.

There is no omitted cubic term. In a line bundle the phase connection is Abelian, `alpha wedge alpha=0`, and the exact transgression for `f wedge f` is `alpha wedge f`. This is why the spectral choice only has to control the second-power gradient on the low-amplitude set.

## 7. Check of the proposed O10 line section

For the O10 application, let `v` be the bounded resolvent negative spinor with `a=|v|² -> m_*`, and retain the original strong-current input `N_v=(nabla v)^(1,0) -> 0` and `Dv -> 0` in normalized `L2`. Set `q=|nabla v|²`. The later first-prolongation/bracket theorem is unnecessary, as checked below.

The bounded-b Hessian estimate, `da -> 0` in `L2`, and `(L-2)v -> 0` in `L2` give

\[
 \Delta a=4a-2q+o_{L^2}(1).
\]

Test this identity against `T(q)=clamp(q-2m_*,-1,1)`, with a smooth monotone approximation if desired. Its derivative is supported in a fixed bounded-q interval, where `|nabla q| <= 2 sqrt(q)|nabla²v|`. Hence `avg da dot nabla T(q) -> 0`. It follows that

\[
 \fint(q-2m_*)T(q)\to0,
\]

so `q -> 2m_*` in measure and `L1`, and in `Lp` for every `p<2`. This does not assert strong `L2` convergence of q.

Here is a direct check of the surviving derivative component without a bracket argument. Put `j_v=Im<v,nabla v>`. The algebraic decomposition `<v,nabla v>=da/2+i j_v`, evaluated on `Z_1=e_1-i e_2` and `Z_2=e_3-i e_4`, gives

\[
 |j_v|\le C\bigl(|v|\,|N_v|+|da|\bigr).
\]

Hence `j_v -> 0` in `L2`. This argument uses no Dirac equation or Nijenhuis identity. On `a>=a_0>0`, adapt the negative frame to `v=sqrt(a)e_1`; the entire first component of `nabla v` is then `(da/2+i j_v)/sqrt(a)` and tends to zero in `L2`. Regions where a or the original rho is small have vanishing relative volume, and the bounded fourth-gradient norm makes their gradient-square contributions vanish.

Write `A_i=nabla_(Z_i)v`, `B=nabla_(bar Z_1)v`, `C=nabla_(bar Z_2)v`. The manuscript's Clifford matrices give exactly

\[
 D^-v=(-(A_1)_1+(A_2)_2,-B_2-C_1).
\]

Since `A_1,A_2 -> 0` from N, and all first components tend to zero from the preceding phase/amplitude argument, `Dv -> 0` forces `B_2 -> 0`. Thus only `C_2` can survive. This proves the component statement previously obtained using the longer bracket argument, but does not use that argument.

The determinant bookkeeping is:

\[
 v\in S^-\otimes L,\qquad
 t(v)\in S^+\otimes L^4,\qquad
 \sigma:=\Phi\wedge t(v)\in L^5.
\tag{7.1}
\]

Indeed, v has spin-c determinant `L³`; its cubic opposite-spinor has an additional `L³` twist, making the total twist `L⁴` relative to the original positive bundle. Wedge with the original Phi adds `det S+=L`.

The ideal surviving component has `t(v)` orthogonal to Phi and

\[
 |t(v)|^2=2a^2q.
\]

The component errors just controlled tend to zero in measure, which is enough here. Therefore

\[
 |\sigma|^2\to
 4\rho_*m_*^3
 =\frac{33554432}{1594323}>0
 \quad\text{in normalized measure}.
\tag{7.2}
\]

Differentiating the globally defined polynomial expression for sigma gives the bound

\[
 |\nabla\sigma|
 \le C\bigl(|\nabla^2v|+|\nabla v|^2
                   +|\nabla\Phi||\nabla v|\bigr),
\]

using bounded Phi and v. The finite-b Hessian and fourth-gradient budgets for v, and the inherited fourth-gradient budget for Phi, thus give a uniform normalized `H1` energy for sigma. No derivative of a normalized local frame is used.

Finally the connection of `L⁵` has curvature `5F_A`, already a bounded tensor plus an `L2`-small error. Thus (1.1)–(1.2) hold. The Abelian lemma gives

\[
 \frac{c_1(L^5)^2[M]}{V}=25\frac{a^2}{V}\to0.
\tag{7.3}
\]

But the actual endpoint curvature limits give

\[
 \frac{a^2}{V}
 =\frac1{4\pi^2}\fint
          (|F_A^+|^2-|F_A^-|^2)
 \to\frac1{6\pi^2},
\tag{7.4}
\]

contradicting (7.3).

Accordingly, using the old strong-current projection, the resolvent estimates, and the checked cubic component computation, the new Abelian argument excludes every O10 zero sequence with a fixed finite opposite-Weyl energy-density bound. The separate bracket/first-prolongation theorem is not in this proof's dependency chain. This is stronger than any single numerical Euler-density cutoff. It still does not supply that bound for a sequence whose Euler or opposite-Weyl density diverges.
