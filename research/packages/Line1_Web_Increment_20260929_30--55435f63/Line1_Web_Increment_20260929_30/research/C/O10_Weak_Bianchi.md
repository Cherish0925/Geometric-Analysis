# O10: the regularized derivative has asymptotically constant length

Date: 2026-09-29. This note continues the existing actual O10 endpoint argument for a sequence with a fixed finite bound on the normalized opposite Weyl energy. It proves a further consequence of the bounded resolvent construction and identifies a genuine next coefficient bundle. It does **not** prove unrestricted O10.

## 1. Inputs already proved in continuation B

All norms and integrals below are normalized by volume. Let

\[
 v\in\Gamma(E_-),\qquad E_-=S^-\otimes L,\qquad
 a=|v|^2,\quad q=|\nabla v|^2,\quad m_*=128/81.
\]

For each fixed bound on \(\fint |W^-|^2\), the preceding resolvent argument gives

\[
 \|v\|_\infty\le C,\qquad
 \|\nabla v\|_4+\|\nabla^2v\|_2\le C_B,
 \qquad a\to m_*\text{ in }L^p\ (p<\infty),
\]

\[
 e=\nabla^*\nabla v-2v\to0\text{ in }L^2,
 \qquad da\to0\text{ in }L^2.
\tag{1}
\]

The last assertion was obtained from the scalar identity for \(a\), its strong amplitude convergence, and the uniform \(L^2\) bound on \(q\). The strong-current prerequisite gives \(N_v=(\nabla v)^{1,0}_{J_+}\to0\) in normalized \(L^2\). Together with (1) and \(D^-_{3A}v\to0\), this gives, in compatible frames adapted to the actual positive spinor and to \(v\),

\[
 \nabla_{Z_1}v\to0,\quad \nabla_{Z_2}v\to0,
 \quad \nabla_{\bar Z_1}v\to0,
 \quad (\nabla_{\bar Z_2}v)_1\to0
 \qquad\text{in }L^2.
\tag{2}
\]

Statements in adapted frames are understood invariantly on fixed positive-amplitude sets, with the exceptional sets removed using the established \(L^4\) derivative bound. No smooth limiting manifold or noncollapse is assumed.

Here is the direct proof of (2), avoiding a Nijenhuis bracket or a second-derivative adjoint test. Write
\[
 A_i=\nabla_{Z_i}v,\quad B=\nabla_{\bar Z_1}v,
 \quad C=\nabla_{\bar Z_2}v,\quad
 j_v=\operatorname{Im}\langle v,\nabla v\rangle.
\]
The exact elementary phase identity
\[
 |j_v+\tfrac12J_+da|^2\le2a|N_v|^2
\]
shows that \(j_v\to0\) in \(L^2\), since \(v\) is bounded and \(da\to0\). In a compatible frame with \(v=\sqrt a\,e_1\), every first spinor component obeys
\[
 (\nabla_Xv)_1=\frac{da(X)/2+i j_v(X)}{\sqrt a}
\]
for real \(X\), extended complex linearly. On a fixed set \(a\ge c>0\), all these components therefore tend to zero in \(L^2\). The sets where \(a<c<m_*\), or where the actual positive amplitude \(\rho<c'<\rho_*\), have relative volume tending to zero; there
\[
 \fint_E|\nabla v|^2
 \le \mu(E)^{1/2}\bigl(\fint|\nabla v|^4\bigr)^{1/2}\to0.
\]
Hence \(B_1,C_1\to0\) globally in the invariant cutoff sense. The actual Clifford formula is
\[
 D^-v=((A_1)_1-(A_2)_2,\ B_2+C_1),
\]
up to an overall sign. It follows that \(B_2\to0\). Finally \(A_1,A_2\to0\) are exactly the small \((1,0)\) projection supplied by \(N_v\). This proves (2) using only mass, phase, and Dirac information.


## 2. A scalar covariance argument gives more than the averaged energy limit

Use the nonnegative scalar Laplacian. Equation (1) gives

\[
 \Delta a=4a-2q+2\operatorname{Re}\langle e,v\rangle.
\tag{3}
\]

Set \(q_*=2m_*\) and

\[
 T(x)=\frac{x}{1+x},\qquad x\ge0.
\]

The chain rule and the covariant Kato estimate imply

\[
 |dT(q)|\le \frac{2\sqrt q}{(1+q)^2}|\nabla^2v|
 \le C|\nabla^2v|.
\tag{4}
\]

Thus \(T(q)-T(q_*)\) is a bounded test function with a uniformly bounded normalized \(H^1\) seminorm, even though \(q\) itself need not have an \(L^2\) gradient. Testing (3) with this function gives

\[
\begin{aligned}
 2\fint(q-q_*)[T(q)-T(q_*)]
 ={}&4\fint(a-m_*)[T(q)-T(q_*)]\\
 &+2\fint\operatorname{Re}\langle e,v\rangle[T(q)-T(q_*)]\\
 &-\fint\langle da,dT(q)\rangle\longrightarrow0.
\end{aligned}
\tag{5}
\]

Every term on the right tends to zero by (1) and (4). The integrand on the left is nonnegative and is bounded below by a positive number on every set \(|q-q_*|\ge\epsilon\). Consequently

\[
 \boxed{|\nabla v|^2\longrightarrow2m_*\quad\text{in normalized measure}.}
\tag{6}
\]

Since \(q\) is uniformly bounded in normalized \(L^2\), it follows that

\[
 \boxed{|\nabla v|^2\longrightarrow2m_*
       \quad\text{strongly in normalized }L^p\text{ for every }1\le p<2.}
\tag{7}
\]

This strengthens the preceding result \(\fint|\nabla v|^2\to2m_*\). It does **not** establish strong \(L^2\) convergence of \(q\), equivalently uniform integrability of \(|\nabla v|^4\). Critical concentration remains possible under these estimates.

## 3. The remaining first-derivative coefficient has nonzero constant modulus

Let \(C=(\nabla_{\bar Z_2}v)_2\). Because \(Z_i=e_{2i-1}-ie_{2i}\), the full derivative norm is

\[
 |\nabla v|^2=\tfrac12\bigl(
 |\nabla_{Z_1}v|^2+|\nabla_{\bar Z_1}v|^2+
 |\nabla_{Z_2}v|^2+|\nabla_{\bar Z_2}v|^2\bigr).
\]

Equations (2) and (7) therefore imply

\[
 \boxed{|C|^2\longrightarrow4m_*\quad\text{in measure and in }L^1.}
\tag{8}
\]

Write the surviving negative-spinor off-diagonal connection as

\[
 b=(0,0,c,-ic),\qquad c=C/(2\sqrt a),
\]

on fixed positive-amplitude sets. Then

\[
 \boxed{|c|^2\longrightarrow1\quad\text{in measure}.}
\tag{9}
\]

The conclusion concerns the invariant modulus. It does not provide a global choice of the phase of \(c\).

## 4. A genuine line-bundle coefficient for the next prolongation

The cubic construction is an algebraic first-order operation on any spinor; it does not require that the spinor solve a monopole equation. Since \(v\) is a negative spinor with determinant line \(L^3\), its cubic torsion is a smooth positive spinor

\[
 t(v)\in\Gamma(S^+\otimes L^4).
\tag{10}
\]

Use the actual positive spinor \(\Phi\in\Gamma(S^+)\) to form the determinant pairing

\[
 \boxed{\sigma=\Phi\wedge t(v)\in\Gamma(L^5).}
\tag{11}
\]

This is a globally defined section. The exponent is checked directly:
\(\det S^+=L\), and the second factor is twisted by \(L^4\).

In compatible frames \(\Phi=\sqrt\rho\,e_1\), \(v=\sqrt a\,e_1\), the ideal remaining first jet gives

\[
 t(v)=(0,2a^{3/2}c),\qquad
 |\sigma|^2=4\rho a^3|c|^2.
\tag{12}
\]

The omitted components are bounded linear multiples of the projections in (2); hence they tend to zero in \(L^2\). With \(\rho\to\rho_*=4/3\), (9) gives

\[
 \boxed{|\sigma|^2\longrightarrow
 a_{\sigma,*}=4\rho_*m_*^3>0\quad\text{in measure}.}
\tag{13}
\]

The exact polynomial definition and boundedness of \(\Phi,v\) also give

\[
 |\sigma|\le C|\nabla v|,
\]

\[
 |\nabla\sigma|\le C\bigl(
 |\nabla\Phi|\,|\nabla v|+|\nabla v|^2+|\nabla^2v|\bigr).
\]

Therefore

\[
 \boxed{\|\sigma\|_4+\|\nabla\sigma\|_2\le C_B,
 \qquad |\sigma|^2\to a_{\sigma,*}\text{ strongly in }L^p\ (1\le p<2).}
\tag{14}
\]

Unlike the connection on \(E_-\), this line has curvature \(5F_A\), already a bounded actual model plus an error tending to zero in normalized \(L^2\). Its characteristic square has positive endpoint density:

\[
 \frac{c_1(L^5)^2[M]}V=25\frac{a^2}{V}
 \longrightarrow\frac{25}{6\pi^2}.
\tag{15}
\]

These facts identify a concrete next coefficient, rather than an abstract proposal to add a new field.

## 5. What has not yet been inferred

A nearly constant nonzero modulus in measure and a bounded \(H^1\) energy do not supply a nowhere-zero smooth section. In particular, (13)--(15) alone are not a contradiction on varying geometries. A separate geometry-free line-bundle compactness or actual differential constraint would be required.

Nor has this note proved

\[
 D^+_{9A}t(v)\to0\quad\text{in }L^2.
\]

The Lichnerowicz potential along the surviving positive-spinor line is negative, tending to \(-7\). That sign prevents a positive-potential vanishing argument, but it does not itself prevent a resolvent-and-characteristic-class argument if a sufficiently small Dirac residual can be established. The latter remains unproved.

The exact anti-self-dual Einstein almost-Kähler calculation in Armstrong's thesis, Section 3.3.3, constrains derivatives of the analogous complex coefficient and then uses differential Bianchi identities. Its smooth exact argument does not justify discarding products of an \(L^2\)-small first projection, an \(L^4\)-bounded derivative, and an \(L^2\)-bounded curvature in the present weak setting. The covariance argument above closes a genuine amplitude step. The rank-one argument in Section 6 bypasses this further weak curvature/prolongation step for fixed finite density; it does not establish the latter separately.

Primary reference checked: John Armstrong, thesis, Section 3.3.3, PDF pp. 82--84, https://johnarmstrongmaths.com/publications/resources/thesis.pdf . The screenshot of PDF p. 83 is needed to distinguish the two different spinor directions in the derivative constraints; plain-text extraction loses one conjugation.

## 6. Integration with the new rank-one lemma

The covariance identity used above has the explicit form

\[
 (q-q_*)[T(q)-T(q_*)]
 =\frac{(q-q_*)^2}{(1+q)(1+q_*)},
\]

so the proof also gives \(\fint (q-q_*)^2/(1+q)\to0\).

The additional line-bundle argument referred to in Section 5 has now been supplied in `O10_Topological_Escape.md`. It uses the actual normalized Ricci-energy bound, logarithmic selection of a rough-Laplacian resolvent parameter, and rank-one Chern transgression. Combining it with (13)--(15) produces the contradiction. The complete combined proof is `O10_All_Finite_Density.md`: O10 holds for every fixed finite bound \(\chi/A\le B\), with a constant \(c(B)>0\). The unrestricted uniform-density statement remains outside that proof.
