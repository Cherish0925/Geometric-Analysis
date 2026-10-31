---
title: Half-Weyl regularity from the curvature equation
date: 23 September 2026
---

# 1. A differential budget supplied by the equation

Let \((M,g)\) be a closed oriented smooth four-manifold. Regard
\(W=W^+\) as a section of the metric bundle
\(E=\operatorname{Sym}_0(\Lambda^+)\), with its induced connection and
Hilbert--Schmidt norm. Define the residual of the half-Weyl equation by
\[
 Z=\nabla^*\nabla W+\frac{s}{2}W-6W^2+2|W|^2I,
 \qquad q=\fint_M|Z|^2.
 \tag{1}
\]
The rough Laplacian is nonnegative. All averages use the original metric.

**Theorem 1 (equation-to-budget estimate).** Suppose
\[
                  |\operatorname{Ric}|\le K,\qquad |W^+|\le\Lambda
                  \quad\hbox{on }M.
 \tag{2}
\]
Then
\[
 \boxed{\fint_M\bigl(|\nabla^2W^+|^2+|\nabla W^+|^4\bigr)
                    \le C_{K,\Lambda}(1+q).}
 \tag{3}
\]
Let the ordered eigenvalues be \(\lambda_1\le\lambda_2\le\lambda_3\).
If also
\[
                         \lambda_2-\lambda_1\ge\rho>0,
 \tag{4}
\]
the smooth orthogonal projector \(P\) onto the lowest eigenline defines
the global endomorphism
\[
 A=\frac{\lambda_1}{2}(3P-I).
 \tag{5}
\]
It satisfies
\[
 \boxed{H_2(A):=\fint_M|\nabla^2A|^2
                     \le C_{K,\Lambda,\rho}(1+q).}
 \tag{6}
\]
The constants are independent of volume, injectivity radius, diameter,
Sobolev constants and \(W^-\). No derivative of the curvature of the
bundle \(E\) is assumed or estimated.

In particular, if \(\operatorname{Ric}=-g\), then \(K=2\), \(s=-4\),
and \(Z=0\). Thus an upper bound on the *one-sided* Weyl tensor and
the displayed eigenline gap supply the Hessian budget automatically:
\[
                  H_2(A)\le C_{\Lambda,\rho}.
 \tag{7}
\]
The same zero-residual conclusion applies to harmonic self-dual Weyl
curvature, \(\delta W^+=0\), under (2). In that case the classical
half-Weyl Weitzenböck equation gives \(Z=0\), even without the Einstein
equation.

The residual version is useful when the equation is not exactly
harmonic. It does not assert that an \(L^\infty\) bound on Ricci alone
controls \(q\); the latter is an explicit differential input.

# 2. The bundle Hessian argument

We give the argument because applying a full-curvature estimate to a
four-tensor would introduce an unnecessary \(W^-\) hypothesis.

Let \(z\) be a section of a metric bundle with connection curvature
\(F_{ij}\), and write
\[
 H_{ij}=\nabla_i\nabla_j z,\qquad L=\operatorname{tr}H.
\]
The Hessian includes the cotangent Levi-Civita correction. Use the full
two-index convention \(|F|^2=\sum_{ij}|F_{ij}|_{\mathrm{HS}}^2\).
First interchange the Hessian slots, using
\(H_{ij}-H_{ji}=F_{ij}z\). Then integrate by parts and commute once
on the bundle-valued one-form \(\nabla z\). One obtains
\[
\begin{split}
 \int|H|^2={}&\int|L|^2
 -\int\operatorname{Ric}_{ij}\langle\nabla_i z,\nabla_j z\rangle\\
 &+\sum_{ij}\int\langle F_{ij}\nabla_j z,\nabla_i z\rangle
 +\frac12\sum_{ij}\int|F_{ij}z|^2.
\end{split}
 \tag{8}
\]
In detail, the difference between the left side and
\(\sum_{ij}\int\langle H_{ij},H_{ji}\rangle\) is exactly the last
term in (8). In the mixed expression, the commutator acts on
\(\nabla z\), not on \(Fz\). Its cotangent contribution contracts
to Ricci curvature; its bundle contribution is the third term in (8).
The remaining trace term integrates to \(\int|L|^2\). This order
avoids differentiating \(F\).

For completeness, integration of
\(\operatorname{div}(|\nabla z|^2\langle z,\nabla z\rangle^\sharp)\)
gives the dimension-four interpolation estimate
\[
 \left(\int|\nabla z|^4\right)^{1/2}
             \le4\|z\|_\infty\left(\int|\nabla^2z|^2\right)^{1/2}.
 \tag{9}
\]
Indeed the differentiated gradient norm contributes at most
\(2\|z\|_\infty|H||\nabla z|^2\), and the trace Hessian contributes
at most \(2\|z\|_\infty|H||\nabla z|^2\). Cauchy--Schwarz proves
(9). This is integration by parts, not a Sobolev inequality.

Assume \(\|z\|_\infty\le B\), \(|\operatorname{Ric}|\le K\), and
\(|F|\le F_0\). Equation (8) and Cauchy--Schwarz imply
\[
 \fint|\nabla^2z|^2\le
 \fint|\nabla^*\nabla z|^2
 +(K+C F_0)\fint|\nabla z|^2+\tfrac12 F_0^2B^2.
 \tag{10}
\]
Also
\[
 \fint|\nabla z|^2
   =\fint\langle z,\nabla^*\nabla z\rangle
   \le B\left(\fint|\nabla^*\nabla z|^2\right)^{1/2}.
 \tag{11}
\]
Consequently, if the rough-Laplacian squared average is at most
\(C_0(1+q)\), then (10), followed by (9), bounds the Hessian squared
average and fourth-power gradient average by
\(C(B,K,F_0,C_0)(1+q)\). Every term before averaging is proportional
to volume. No lower volume bound is introduced.

# 3. Applying the argument to the half-Weyl equation

The curvature operator of an oriented four-manifold has blocks
\[
 \mathcal R=
 \begin{pmatrix}
 W^++sI/12&\operatorname{Ric}^{\circ}\\
 \operatorname{Ric}^{\circ}&W^-+sI/12
 \end{pmatrix},
 \tag{12}
\]
where the off-diagonal entries use the usual identification with
trace-free Ricci curvature. The action of
\(\mathfrak{so}(4)=\mathfrak{su}(2)_+\oplus\mathfrak{su}(2)_-\)
on \(\Lambda^+\) is trivial on the second summand. Therefore
\[
 |F^{\Lambda^+}|\le C(|W^+|+|s|+|\operatorname{Ric}^{\circ}|),
 \qquad |F^E|\le C|F^{\Lambda^+}|.
 \tag{13}
\]
The second estimate is the induced commutator action on endomorphisms.
It is important that \(W\) is treated as an \(E\)-valued section.
The \(W^-\) block does not occur in (13).

Since \(|s|\le2|\operatorname{Ric}|\), (1)--(2) give
\[
 \nabla^*\nabla W
       =Z-\tfrac{s}{2}W+6W^2-2|W|^2I,
 \qquad
 \fint|\nabla^*\nabla W|^2\le C_{K,\Lambda}(1+q).
 \tag{14}
\]
The identity part has Hilbert--Schmidt norm \(\sqrt3\).
Now (13) and (2) bound the bundle curvature; (10)--(11) apply with
\(z=W\) and \(B=\Lambda\). Finally (9) proves (3).

For an Einstein metric, contracted Bianchi gives \(\delta W^+=0\).
The harmonic-Weyl Weitzenböck equation is precisely \(Z=0\).
For \(\operatorname{Ric}=-g\) its sign-normalized form is
\[
       \nabla^*\nabla W=2W+6W^2-2|W|^2I.
 \tag{15}
\]
The negative Kähler--Einstein eigenvalues
\((-2/3,1/3,1/3)\) solve its algebraic right side, as they must.

# 4. Differentiating the spectral model

Put \(\lambda=\lambda_1\). On the finite-dimensional space of real
symmetric matrices, a simple eigenvalue and its rank-one projector
depend smoothly on the matrix. This requires no separation between
\(\lambda_2\) and \(\lambda_3\).

For clarity, let
\[
 S=(W-\lambda I)^{-1}(I-P),
\]
where the inverse is taken on the orthogonal complement of \(P\).
For a symmetric variation \(K_1\), differentiation of
\(WP=\lambda P\) and \(P^2=P\) gives
\[
 D\lambda[K_1]=\operatorname{tr}(PK_1),\qquad
 DP[K_1]=-SK_1P-PK_1S.
 \tag{16}
\]
Since \(\|S\|_{\mathrm{op}}\le\rho^{-1}\), a further differentiation
gives the uniform bounds
\[
\begin{aligned}
 |D\lambda[K_1]|&\le |K_1|,&
 |D^2\lambda[K_1,K_2]|&\le C\rho^{-1}|K_1||K_2|,\\
 |DP[K_1]|&\le C\rho^{-1}|K_1|,&
 |D^2P[K_1,K_2]|&\le C\rho^{-2}|K_1||K_2|.
\end{aligned}
 \tag{17}
\]
One may obtain the last estimate without differentiating an inverse on
a moving subspace: use the Riesz formula for \(P\) on a circle of
radius \(\rho/2\) around the eigenvalue at the base matrix. Resolvents
on this fixed circle have norm at most \(2/\rho\). Each derivative
inserts one additional resolvent, yielding (17). This is a local
derivative formula; a single spectral contour for every point of
\(M\) is not required.

The map in (5) is orthogonally equivariant, so its Euclidean derivatives
give covariant chain rules in a normal orthonormal frame. In particular
\[
\begin{split}
 |\nabla A|&\le C(1+\Lambda/\rho)|\nabla W|,\\
 |\nabla^2 A|&\le C(1+\Lambda/\rho)|\nabla^2W|
              +C(\rho^{-1}+\Lambda\rho^{-2})|\nabla W|^2.
\end{split}
 \tag{18}
\]
Squaring, averaging, and applying (3) proves (6). The same reasoning
also proves
\[
 \fint\bigl(|\nabla^2P|^2+|\nabla P|^4
                  +|\nabla^2\lambda|^2+|d\lambda|^4\bigr)
              \le C_{K,\Lambda,\rho}(1+q).
 \tag{19}
\]
This is a regularity statement for the entire isolated eigenline, not
an estimate depending on a choice of local eigensection.

# 5. Composition with negative-amplitude selection

Suppose (2) and (4) hold, and set
\[
 r=\fint|\operatorname{Ric}+g|^2,\qquad
 e=\frac12\fint(\lambda_3-\lambda_2)^2,\qquad d=r+e.
 \tag{20}
\]
Trace-freeness and (4) imply
\[
 0=\lambda_1+\lambda_2+\lambda_3
       \ge3\lambda_1+2\rho,
 \qquad -\lambda_1\ge2\rho/3.
 \tag{21}
\]
On the orientation cover of the lowest real eigenline, choose the
smooth normalized form \(\omega\) with \(|\omega|^2=2\).
Set \(t=-3\lambda_1/4\). Then
\[
 \rho/2\le t\le3\Lambda/4,\quad
 P=\tfrac12\omega\otimes\omega,\quad
 A=t(2I/3-\omega\otimes\omega),\quad
 |W-A|^2=\tfrac12(\lambda_3-\lambda_2)^2.
 \tag{22}
\]
All squared densities below descend to \(M\), and averages on the
cover equal averages on the base.

**Corollary 2 (sourced curvature-spectral application).** Under (2)
and (4), the variable-amplitude selection theorem gives
\[
 \boxed{\fint\bigl[|dt|^2+(t-\tfrac12)^2+|\nabla\omega|^2\bigr]
    \le C_{K,\Lambda,\rho}\bigl(d+\sqrt{d(1+q)}\bigr).}
 \tag{23}
\]
The right side now uses the residual of an equation for actual
curvature. There is no separately prescribed \(H_2(A)\) hypothesis.
This is a direct composition of (6) with Theorem 1 of
`line1_variable_negative_selection.md`; no new monopole assumption
is used.

In the exact negative-Einstein case, put
\(\epsilon=(\fint(\lambda_3-\lambda_2)^2)^{1/2}\).
Then \(q=r=0\), \(e=\epsilon^2/2\), and \(\epsilon\le2\Lambda\),
so (23) implies
\[
 \fint\left[|d\lambda_1|^2+(\lambda_1+\tfrac23)^2
                                  +|\nabla\omega|^2\right]
                         \le C_{\Lambda,\rho}\epsilon.
 \tag{24}
\]
It also follows that
\[
 \fint\left[|\nabla W^+|^2+
       \operatorname{dist}\bigl(W^+,\mathcal K_-\bigr)^2\right]
                         \le C_{\Lambda,\rho}\epsilon,
 \tag{25}
\]
where \(\mathcal K_-\) is the orthogonal orbit in
\(\operatorname{Sym}_0(\mathbb R^3)\) of
\(\operatorname{diag}(-2/3,1/3,1/3)\).
To prove the derivative part, write \(R=W-A\).
Equations (3), (6) bound the averaged squared rough Laplacian of
\(R\). Integration by parts yields
\[
 \fint|\nabla R|^2
       \le\left(\fint|R|^2\right)^{1/2}
          \left(\fint|\nabla^*\nabla R|^2\right)^{1/2}
       \le C_{\Lambda,\rho}\epsilon.
\]
The derivative of \(A\) is controlled by \(dt\) and
\(\nabla\omega\), hence by (24). For the zeroth-order part, with
\(h=\lambda_3-\lambda_2\), diagonalization gives the exact formula
\[
 \operatorname{dist}(W,\mathcal K_-)^2
        =\tfrac83(t-\tfrac12)^2+\tfrac12h^2.
 \tag{26}
\]

The regularity theorem is useful beyond this particular composition.
In the exactly harmonic regime, a separate weighted first-order
identity can improve (24) for the lowest-eigenline branch. Equations
(3), (6), and (19) still supply second-order control and apply to a
nonzero equation residual; no claim of optimality is made for (24).

# 6. Mathematical scope and sources

The new step here is the removal of an auxiliary spectral-model
derivative budget by the actual half-Weyl equation, with constants
uniform under collapse and without controlling the opposite Weyl
tensor. Its proof combines standard bundle calculus and spectral
functional calculus with the previously established variable-amplitude
selection estimate. It is not a new classification of exact Einstein
metrics, nor a claim that pointwise Ricci pinching supplies bounded
\(W^+\), the eigenline gap, or the source in (1).

The classical half-Weyl equation is stated in LeBrun,
*Einstein Metrics, Harmonic Forms, and Conformally Kähler Geometry*,
arXiv:1903.00956v2, Section 2, equation (9). Its weighted version reduces
to (1) with \(Z=0\) when the weight is one. The curvature block
decomposition and its endomorphism conventions appear in Section 1,
equation (3). [Primary source](https://arxiv.org/html/1903.00956).

The classical zero-splitting conformal-Kähler mechanism is Derdziński,
*Self-dual Kähler manifolds and Einstein manifolds of dimension four*,
Compositio Math. 49 (1983), 405--433, Proposition 5(i).
[Primary source](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf).

The local proof inputs are the [bounded-form criterion](round21_analytic.md),
Section 2; the [variable calibration](line1_variable_calibration.md); and
the [negative-amplitude selection theorem](line1_variable_negative_selection.md).
The argument above reproduces
the bundle estimate to make its curvature dependence explicit. The
accompanying [finite checker](check_line1_half_weyl_regularity.py) checks the algebraic
equation, spectral projection derivatives, residual norm, and target
distance. It does not replace the integration-by-parts proof or verify
publication priority.
