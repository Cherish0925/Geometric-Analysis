# An explicit Clifford-block system: central correction, graded energy and equality

21 September 2026. All bundles, signs and equations below are defined here.

The main result is a first-principles replacement for an ambiguous connection
bridge, not a claim that ordinary Seiberg--Witten theory proves uniformization.
For the stated Clifford-block ansatz we derive the exact equations equivalent
to projective graded anti-self-duality. Their trace has a cohomological
constraint which an ordinary positive-square monopole cannot satisfy. We also
prove the equality classification for this explicitly defined system. In
particular, it is **not identified with the intended system in Leung's
published product-of-disks converse**.

## 1. Determinants, arrows and the source of the central term

Let \(X\) be a closed oriented Riemannian four-manifold, with a spin-c
structure whose genuine determinant line is \(L\). Write

\[
 W^\pm=S_L^\pm,\qquad \det W^\pm=L,\qquad a=c_1(L).
 \tag{1}
\]

Fix a unitary connection \(C\) on \(L\). The induced spin connections
\(\nabla_C^\pm\) have trace \(F_C\), and hence central curvature
\(F_C I/2\). Let \(E\) be a Hermitian rank-two bundle, \(A\) a unitary
connection on it, and

\[
 \phi\in\Gamma\operatorname{Hom}(W^+,E).
 \tag{2}
\]

The Dirac operator uses \(A\) on \(E\) and the **dual** of the source
connection on \((W^+)^*\). No target-determinant connection is identified
with \(C\) unless expressly stated.

On an oriented orthonormal frame numbered \(0,1,2,3\), choose right Clifford
matrices \(c_j:W^-\to W^+\):

\[
 c_0=I,\quad c_1=-i\sigma_3,\quad c_2=i\sigma_1,\quad c_3=i\sigma_2,
 \qquad
 \rho_+(e^{ij})=-c_i c_j^*\quad(i\ne j).
 \tag{3}
\]

Here \(\sigma_j\) are the Pauli matrices. Set

\[
 \Theta_j=\phi c_j\in\operatorname{Hom}(W^-,E),\qquad
 Q(\phi)=-\tfrac12(\Theta\wedge\Theta^*)^+.
 \tag{4}
\]

This defines the sign and scale of \(Q\) without an implicit identification
between a dual representation and its source. The wedge uses matrix
composition in the displayed order. Direct Clifford algebra gives

\[
 (\Theta^*\wedge\Theta)^+=(\operatorname{tr}_E Q)I_{W^-},
 \qquad
 (\Theta\wedge\Theta^*)^+=-2Q.
 \tag{5}
\]

For example, in source and target unitary frames with
\(\phi=\operatorname{diag}(x,y)\), the coefficients of \(Q\) in the
self-dual basis
\(e^{01}+e^{23},e^{02}-e^{13},e^{03}+e^{12}\) are

\[
 -i\operatorname{diag}(x^2,-y^2),\qquad
 ixy\sigma_1,\qquad ixy\sigma_2.
 \tag{6}
\]

Each basis form has norm squared two. In particular, the trace-free target
part \(Q_0:\Lambda^+\to\mathfrak{su}(E)\) is invertible whenever
\(xy\ne0\). Its two off-diagonal coefficients do not disappear when
\(x\ne y\).

The source convention in [Leung, *Non-Abelian Seiberg--Witten equations on
Einstein manifolds*, pp. 18, 21--24](https://archive.ymsc.tsinghua.edu.cn/pacm_download/60/582-2000_Leung_NonAbelian_SW_eqt_on_Einstein_mfd_Crelle_Journal.pdf)
uses \(L\) for the spin-c determinant, defines the spinor as a homomorphism,
and constructs an indefinite-Hermitian block connection. The displayed
central curvature on p. 24 is not obtained simply by declaring \(L\) to be
a twisting line: that would change (1). The
[1997 preprint, Sections 3--4](https://arxiv.org/pdf/dg-ga/9705001)
has the same determinant-versus-twist issue in this step. We therefore compute
the connection anew instead of importing its displayed central coefficient.

## 2. The exact corrected equation

On \(V=W^-\oplus E\), define

\[
 \mathbb D=
 \begin{pmatrix}
  \nabla_C^-&\Theta^*/\sqrt2\\
  \Theta/\sqrt2&A
 \end{pmatrix},
 \qquad
 \Gamma=\operatorname{diag}(I_{W^-},-I_E).
 \tag{7}
\]

This preserves the form \(h_{W^-}-h_E\), not a positive Hermitian form. It is
a \(U(2,2)\) connection. Its graded Hodge operator is

\[
 *_\Gamma B=\Gamma(*B)\Gamma.
 \tag{8}
\]

Thus the graded self-dual projection is the ordinary self-dual projection on
diagonal blocks, and the ordinary anti-self-dual projection on off-diagonal
blocks. The grading is part of the data; it is not assumed parallel under
\(\mathbb D\).

The curvature is exactly

\[
 F_{\mathbb D}=
 \begin{pmatrix}
 F_{\nabla_C^-}+\tfrac12\Theta^*\wedge\Theta&
       (d_{A,C}\Theta)^*/\sqrt2\\
 d_{A,C}\Theta/\sqrt2&F_A+\tfrac12\Theta\wedge\Theta^*
 \end{pmatrix}.
 \tag{9}
\]

At a normal frame, put \(X_j=\nabla_j\phi\). Then
\(D_{A,C}\phi=\sum_jX_jc_j\), and the three anti-self-dual coefficients
of \(d_{A,C}\Theta\) are respectively
\((D_{A,C}\phi)c_1/2,(D_{A,C}\phi)c_2/2,(D_{A,C}\phi)c_3/2\).
Consequently

\[
 (d_{A,C}\Theta)^-=0\quad\Longleftrightarrow\quad D_{A,C}\phi=0.
 \tag{10}
\]

If \(g\) is Einstein, the ordinary self-dual source spin curvature is
\((F_{\nabla_C^-})^+=(F_C^+/2)I\). From (5), the diagonal graded
self-dual curvature blocks in (9) are therefore

\[
 \left(\tfrac12F_C^++\tfrac12\operatorname{tr}Q\right)I_{W^-},
 \qquad F_A^+-Q.
 \tag{11}
\]

**Proposition 1 (exact Clifford-block criterion).** On an Einstein
four-manifold, (7) is projectively graded anti-self-dual if and only if

\[
 \boxed{\quad D_{A,C}\phi=0,\qquad
 F_A^+=Q(\phi)+\tfrac12\operatorname{tr}Q(\phi)I_E
                   +\tfrac12F_C^+I_E.\quad}
 \tag{12}
\]

Indeed, (10) kills the off-diagonal graded self-dual block, and (12) says that
the two diagonal blocks in (11) are the same scalar. That scalar is

\[
 c^+=\tfrac12(F_C^++\operatorname{tr}Q)
     =\tfrac14(F_C^++\operatorname{tr}F_A^+).
 \tag{13}
\]

The additional central terms in (12) are essential. They cannot be absorbed
by changing the overall normalization of \(Q\).

More generally, off-diagonal coefficient \(\lambda\) and target rank \(r\)
give the exact equation

\[
 F_A^+=2\lambda^2Q+
       (\tfrac12F_C^++\lambda^2\operatorname{tr}Q)I_E,
 \quad
 \operatorname{tr}F_A^+=\tfrac r2F_C^++(r+2)\lambda^2\operatorname{tr}Q.
 \tag{14}
\]

This is a useful rank check on any proposed transfer from an abelian block
connection: the coefficient in its scalar equation changes with target rank.

## 3. What twisting can and cannot change

If a spin structure exists and \(L=B^2\), then
\(W^\pm=S^\pm\otimes B\). For compatible connections,
\(F_C=2F_B\), so the central curvature of \(W^\pm\) is \(F_B=F_C/2\).
Writing it as \(F_B\) is correct only if \(B\), rather than the genuine
determinant \(L\), is being named.

A common tensor twist of both summands of \(V\) by a line \(T\) shifts
\(F_{\mathbb D}\) by \(F_T I_V\), while replacing the spin-c determinant by
\(L\otimes T^2\). A twist of only one summand also changes the homomorphism
bundle containing \(\Theta\). Neither operation leaves all of (1), (2) and
(7) unchanged.

When \(E\cong W^+\), the true determinant of \(V\) is \(L^2\). Therefore
its curvature trace has cohomology class \(2a\), in the normalization
\(c_1=[i\operatorname{tr}F/(2\pi)]\). A proposed scalar curvature
\(-F_C I_4\) would instead have trace class \(-4a\). A change of sign in
the Chern--Weil convention changes both sides and does not remove this
discrepancy. Formula (13) has the required harmonic central class \(a/2\).
This argument resolves the central coefficient for the literal bundle (7);
it does not assign an unprinted twist to the published theorem.

## 4. A cohomological obstruction to direct ordinary-monopole transfer

Assume \(E\cong W^+\) topologically. Taking the trace of (12) gives

\[
 \operatorname{tr}F_A^+-F_C^+=2\operatorname{tr}Q(\phi).
 \tag{15}
\]

The two determinant curvatures on the left represent the same cohomology
class, whether or not their connections agree. Hence

\[
 \boxed{\quad\mathcal H_g^+(\operatorname{tr}Q(\phi))=0.\quad}
 \tag{16}
\]

If their determinant connections actually coincide, the stronger pointwise
condition \(\operatorname{tr}Q=0\) follows. For rank two this says
\(\phi^*\phi\) is scalar at each point. In particular, a nonzero rank-one
field cannot satisfy that fixed-determinant version.

Here is a convention-fixed comparison with an ordinary spinor. Suppose a
rank-one field takes values in a target line \(R\subset E\). It is a section

\[
 \psi\in (W^+)^*\otimes R,
 \qquad B=L^{-1}\otimes R^2
 \tag{17}
\]

of a positive spin-c bundle with determinant \(B\). Its dual Clifford action
on two-forms is \(\rho_{\rm dual}(\eta)=-\rho_+(\eta)^T\).
Define the ordinary quadratic map by
\(\rho_{\rm dual}(q_{\rm std}(\psi))=(\psi\psi^*)_0\).
Then the **actual** source-to-dual conversion gives

\[
 \operatorname{tr}Q(\phi)=4q_{\rm std}(\psi).
 \tag{18}
\]

For verification, place \(\phi=(x,0)\) in its active target row and let
\(\omega=e^{01}+e^{23}\). Equations (3)--(6) give
\(\operatorname{tr}Q=-ix^2\omega\),
\(\rho_{\rm dual}(\omega)=2i\sigma_3\), and
\(\rho_{\rm dual}(\operatorname{tr}Q)=2x^2\sigma_3
=4(\psi\psi^*)_0\). Unitary equivariance proves (18) generally.

If \(\psi\) solves the ordinary equation
\(F_B^+=q_{\rm std}(\psi)\), (16) and (18) would force
\(c_1(B)_g^+=0\). A different nonzero normalization of the ordinary quadratic
map changes the numerical factor, not this implication. Thus:

**Proposition 2 (no direct positive-square transfer).** An ordinary
Seiberg--Witten solution of determinant class \(b\), with \(b_g^+\ne0\),
cannot be inserted unchanged as a rank-one field into (12), even allowing
an arbitrary coupled target connection with determinant line \(L\).
In particular, \(b^2>0\) prevents this transfer for every metric.

This is not a nonexistence theorem for differently oriented rank-one fields
or genuinely rank-two solutions. The obstruction is the harmonic trace of
the particular quadratic field, not an assumed parallelism of that field.

For an almost-Kähler metric with the canonical smooth splitting
\(W^+=\mathbb C\oplus L\) and Kähler form \(\omega\), (16) also implies
the balanced column identity

\[
 \int_X\|\phi|_{\mathbb C}\|^2\,d\mu
 =\int_X\|\phi|_L\|^2\,d\mu.
 \tag{19}
\]

Indeed, the coefficient of \(\operatorname{tr}Q\) along \(\omega\) is
\(-i(\|\phi|_{\mathbb C}\|^2-\|\phi|_L\|^2)\), and a closed self-dual form
is harmonic. Here the notation means the squared norm of the indicated
column, not the rank of its image. A field supported in just one canonical
source column is therefore excluded unless it vanishes identically.

## 5. The indefinite connection has a positive *graded* energy identity

No positive-unitary instanton inequality is being imported. Put
\(F_0=F_{\mathbb D}-\tfrac14\operatorname{tr}(F_{\mathbb D})I\).
It remains \(\mathfrak u(2,2)\)-valued. In blocks it has the form

\[
 F_0=\begin{pmatrix}P&B^*\\B&S\end{pmatrix},
 \qquad P^*=-P,\quad S^*=-S.
 \tag{20}
\]

If \(*_\Gamma F_0=-F_0\), then \(*P=-P,*S=-S,*B=B\).
With the positive Hilbert--Schmidt norm from the direct-sum metric,

\[
 \begin{aligned}
 \operatorname{tr}(P\wedge P)&=|P|^2d\mu,\\
 \operatorname{tr}(S\wedge S)&=|S|^2d\mu,\\
 2\operatorname{tr}(B^*\wedge B)&=2|B|^2d\mu.
 \end{aligned}
\]

Thus

\[
 \boxed{\quad
 \operatorname{tr}(F_0\wedge F_0)=|F_0|^2d\mu\ge0.
 \quad}
 \tag{21}
\]

The reversed Hodge sign on the off-diagonal block is exactly what makes
its contribution positive. For an ordinary ASD \(U(2,2)\) connection the
off-diagonal contribution has the opposite sign, so (21) would be false.

For \(E\cong W^+\), the standard spin-c characteristic-class identities are

\[
 c_2(W^\pm)=\tfrac14(a^2\mp2\chi-3\tau),\qquad
 c_1(V)=2a,\qquad c_2(V)=\tfrac32(a^2-\tau).
 \tag{22}
\]

Chern--Weil theory applies to this complex connection without requiring
positive-unitary holonomy. Equations (21)--(22) give the exact identity

\[
 \boxed{\quad
 \int_X|F_0|^2\,d\mu
 =8\pi^2c_2(V)-3\pi^2c_1(V)^2
 =-12\pi^2\tau(X).
 \quad}
 \tag{23}
\]

In particular, a solution of (12) on an Einstein manifold has \(\tau\le0\),
and if \(\tau=0\), its block connection is projectively flat. This proves
the relevant equality implication directly, using the *graded* equation.

## 6. Exact zero-signature equality classification for this system

**Theorem 3.** Let \(g\) be an Einstein metric on a connected closed oriented
four-manifold with \(\chi>0\) and \(\tau=0\). Let \(L\) be any spin-c
determinant and \(C\) any unitary connection on it. With \(E=W^+\), the
explicit system (12) has a solution if and only if \(g\) has constant
negative sectional curvature.

**Proof.** By (23), \(F_0=0\). In particular,
\(d_{A,C}\Theta=0\), not just its anti-self-dual projection. This forces
\(\nabla_{A,C}\phi=0\). To see it pointwise, write
\(X_ic_j-X_jc_i=0\). Since \(c_0=I\),
\(X_j=X_0c_j\). For two distinct nonzero indices,
\(X_0(c_ic_j-c_jc_i)=0\); the quaternionic commutator is invertible, so
\(X_0=0\), and then every \(X_j=0\).

The rank and singular values of \(\phi\) are constant.

If its rank is zero, projective flatness of the source spin connection
forces \(W^-=0\) and \(s=0\). The signature formula and \(\tau=0\) give
\(W^+=0\). Since \(g\) is Einstein, it is flat, contradicting \(\chi>0\).

If the rank is one, its image \(R\subset E\) and orthogonal complement
\(K\subset E\) are parallel. Since the off-diagonal field vanishes on \(K\),
this line is also parallel for \(\mathbb D\). Projective flatness forces

\[
 c_1(K)=\tfrac14c_1(V)=a/2
 \quad\hbox{in }H^2(X;\mathbb R).
\]

But \(E=R\oplus K\) then has
\(a^2-4c_2(E)=(c_1(R)-c_1(K))^2=0\), whereas (22) gives
\(a^2-4c_2(W^+)=2\chi+3\tau=2\chi>0\). This is impossible.

If the rank is two, polar decomposition gives a parallel unitary
isomorphism \(U:W^+\to E\) and a parallel positive endomorphism
\(H=(\phi^*\phi)^{1/2}\). Gauge by \(U\), so \(A=\nabla_C^+\) and
\(\phi=H\). If \(H\) has distinct eigenvalues \(x,y>0\), its eigenlines
are parallel, so the target curvature commutes with \(H\). Equation (12)
would make \(Q(H)\) commute with \(H\) as well. This contradicts the two
nonzero off-diagonal matrices in (6). Therefore \(H=fI\), where \(f>0\)
is constant, and \(\operatorname{tr}Q=0\).

For completeness fix the curvature convention
\(R(X,Y)Z=k(\langle Y,Z\rangle X-\langle X,Z\rangle Y)\) for sectional
curvature \(k\). The spin curvature on a constant-curvature metric is
\(-k\rho_+(e^{ij})/2\), whereas \(Q(fI)_{ij}=f^2\rho_+(e^{ij})\).
More generally, its trace-free self-dual coefficient matrix is the same
faithful Clifford image of \(-\tfrac12(W^++sI/12)\). Thus (12) forces
\(W^+=0\) and \(s/12=-2f^2\). The signature formula again gives
\(W^-=0\). Since \(g\) is Einstein, its sectional curvature is the
constant \(k=-2f^2<0\).

Conversely, for constant curvature \(k<0\), take
\(A=\nabla_C^+\) and \(\phi=\sqrt{-k/2}\,I\). The field is parallel;
its trace quadratic term is zero; the displayed spin-curvature identity
verifies (12). Its block connection has curvature \((F_C/2)I_V\).
This establishes both directions. \(\square\)

The exclusion of the bidisk in Theorem 3 is a scope distinction, not a claim
that a product metric lacks all nonabelian monopoles in every definition.
It shows that the literal pure-Clifford ansatz with the corrected central
equation cannot be substituted for a system whose converse is asserted to
include the bidisk. Producing that converse requires a different, explicitly
specified bundle or field equation; it does not follow by relabelling \(L\).

## 7. Consequence for the actual closed sheared gluings

For the closed manifolds \(M(h,g;u,f)\) of
[round11_closed_gluing.md](round11_closed_gluing.md), the established inputs
are \(\chi>0\), \(\tau=0\), \(b^+>1\), symplectic structures and
\(\mathbb Z^2\subset\pi_1(M)\); see
[round11_graph_topology.md](round11_graph_topology.md) and
[round11_variational.md](round11_variational.md). Their canonical classes
have square \(2\chi>0\).

[Taubes's Main Theorem](https://doi.org/10.4310/MRL.1994.v1.n6.a15) gives
ordinary canonical monopoles. These persist for every metric through the
standard small-perturbation limiting argument, with reducibility excluded
by positive class square. Proposition 2 proves that these solutions do not
give (12) by rank-one insertion, even on an arbitrary hypothetical Einstein
metric, and not merely on the constructed almost-Einstein family.

More strongly, Theorem 3 says that any hypothetical Einstein metric on this
\(M\) has **no solution of (12)**: a closed real-hyperbolic manifold has no
\(\mathbb Z^2\) subgroup (its nontrivial abelian subgroups are cyclic),
contrary to the displayed group inclusion. This is a conditional emptiness
statement for the explicitly defined auxiliary system. It is not an
Einstein obstruction, since no invariant has been shown to force this
auxiliary system to have a solution.

The remaining global Einstein question therefore cannot be closed by the
implication “ordinary canonical monopoles imply the needed Clifford-block
solution.” This implication is contradicted here by an exact trace equation,
and its stronger existence version would contradict Theorem 3. A successful
nonabelian route must supply a genuinely different existence mechanism and
state its bundle, central equation and quadratic map before invoking a
uniformization argument.

## 8. Executable scope

Run

```bash
qiushi-yau26 env numeric python round12_uniformization_check.py
```

The checker verifies the oriented Clifford identities, both wedge terms,
the Dirac/graded projection equivalence, injectivity of the covariant-closed
Clifford map, the rank-dependent central coefficient, the full positive
graded Chern pairing, the characteristic-class substitutions, the dual
ordinary-spinor factor, and the constant-negative-curvature model. These
are exact algebraic checks. The global Hodge, characteristic-class and
parallel-subbundle arguments are the proofs above, not numerical output.
