# Weak Cotton sources and local Weyl compactness

This note identifies a way to pass the self-dual curvature to a local limit
without an L2 bound on the Cotton tensor. It does not construct the controlled
coordinate patches needed in a collapsed near-Einstein sequence.

## 1. An exact elliptic symbol

Use oriented Euclidean coordinates in dimension four and self-dual two-forms
\(\omega_1=dx^{01}+dx^{23}\),
\(\omega_2=dx^{02}+dx^{31}\),
\(\omega_3=dx^{03}+dx^{12}\), each of two-form norm squared two.
For a symmetric trace-free matrix \(A\), define
\[
W(A)_{ijkl}=\frac12\sum_{a,b}A_{ab}(\omega_a)_{ij}(\omega_b)_{kl}.
\]
Then the ordinary four-index norm is \(|W(A)|^2=4|A|_{\rm HS}^2\).
Let \(D A=\partial^i W(A)_{ijkl}\), with the ordinary three-index norm
on its range. For every real covector \(\xi\),
\[
|\sigma_D(\xi)A|^2=|\xi|^2|A|_{\rm HS}^2.                 \tag{1}
\]
One proof sets \(\xi=dx^0\). The three vectors
\(((\omega_a)_{0j})_j\) are orthonormal and
\(\sum_{kl}(\omega_b)_{kl}(\omega_d)_{kl}=4\delta_{bd}\).
Contraction gives (1); orthogonal covariance proves the general case.
The script also checks the identity polynomially for all five entries of
\(A\) and all four entries of \(\xi\).

On a flat four-torus the Fourier identity is consequently
\[
\|A-\overline A\|_{L^2}^2=\|DA\|_{\dot H^{-1}}^2,        \tag{2}
\]
where the zero mode is omitted from the homogeneous negative norm.
This is not a divergence operator with an uncontrolled oscillatory kernel:
its restriction to a single Weyl half is overdetermined elliptic.

### Full-jet coercivity on the constant-spectrum orbit

There is a stronger pointwise fact on the orbit of
\(A_0=\operatorname{diag}(-1/6,1/12,1/12)\). In a frame diagonalizing
\(A\) at a point, an arbitrary covariant first derivative tangent to this
orbit has four matrices
\[
H_m=\begin{pmatrix}0&u_m&v_m\\u_m&0&0\\v_m&0&0\end{pmatrix}.
\]
For the eight real variables \((u_m,v_m)\), the divergence quadratic form
has eigenvalues 1 and 3, each with multiplicity four; meanwhile
\(\sum_m|H_m|^2=2\sum_m(u_m^2+v_m^2)\). Hence every smooth field taking
values in this orbit satisfies
\[
\tfrac12|\nabla A|^2\le|\operatorname{div}W(A)|^2
                       \le\tfrac32|\nabla A|^2.        \tag{2a}
\]
This is a bound for the complete first jet, not just a single-frequency
symbol. If \(A=I/12-(n\otimes n)/4\) for a local unit eigenvector \(n\),
it implies \(|\nabla n|^2\le16|\operatorname{div}W(A)|^2\).
It explains the local constant-spectrum rigidity directly.

For an actual Weyl operator \(W^+=A+R\), however,
\(\operatorname{div}W(A)=\operatorname{div}W^+-\operatorname{div}W(R)\).
Small L2 size of \(R\) does not bound its derivative in L2. Multiplying
its weak divergence by an eigenframe depending on position also produces
\(R\nabla n\). Thus (2a) alone does not turn small calibration density
into a small gradient-energy estimate.

## 2. The residual is small in the correct weak source space

For a smooth metric let \(E=\operatorname{Ric}+g\),
\(e=\operatorname{tr}E\), and use the Cotton convention
\[
C_{ijk}=\nabla_kE_{ij}-\nabla_jE_{ik}
-\frac16\bigl((\nabla_ke)g_{ij}-(\nabla_je)g_{ik}\bigr).
\]
The contracted Bianchi identity gives \(\operatorname{div}W^+=-C^+/2\)
up to the choice of divergence sign, which has no effect on the following
norm estimate. On a fixed uniformly elliptic C1-controlled coordinate
domain, integration by parts against an H1 test tensor gives
\[
\|\operatorname{div}W^+\|_{H^{-1}}\le C\|E\|_{L^2}.       \tag{3}
\]
The derivative is transferred to the test tensor, volume density, and
bounded metric coefficients. The constant uses first derivatives of the
metric, not derivatives of E.

Thus the previous high-frequency counterexample to a Cotton L2 estimate
does not refute (3). For a Fourier mode of amplitude epsilon and frequency
k, its first derivative has L2 size proportional to epsilon*k but H-1
size proportional to epsilon. A divergent Cotton energy is compatible with
a vanishing weak source.

The Cotton convention and divergence relation are classical; see
[Catino--Mastrolia--Monticelli--Punzo, equations (2.2), (2.5)](https://cvgmt.sns.it/media/doc/paper/4075/WHW-metrics.pdf).

## 3. Conditional strong convergence on controlled patches

Let \(U\) be a fixed coordinate ball. Suppose smooth metrics \(g_j\) are
uniformly elliptic, bounded in C1,alpha for a fixed alpha>0, and converge
in C1 to \(g_\infty\). Suppose also
\[
\|\operatorname{Ric}(g_j)+g_j\|_{L^2(U)}\longrightarrow0. \tag{4}
\]
Then, after identifying self-dual bundles by frames depending algebraically
on the metric, the entire sequence of Weyl operators converges strongly in
L2 on every relatively compact subdomain. Its limit is the self-dual Weyl
curvature of the weak Einstein limit. A separate L2 curvature bound is not
needed: it follows locally from the other hypotheses.

Here are the analytic steps, including the needed negative-norm estimate.
The divergence operator in these frames has the form
\(D_j=P_j^a\partial_a+Q_j\), with \(P_j\to P_\infty\) in C1 and
\(Q_j\to Q_\infty\) uniformly. Integration by parts therefore gives
\[
\|(D_j-D_\infty)u\|_{H^{-1}}
\le o(1)\|u\|_{L^2}
\]
for fields with fixed interior support. By (3), \(D_j A_j\to0\)
in H-1. Before obtaining a curvature bound, the difference term is retained
on the right and will be absorbed, not assumed small independently.

For a first-order operator with injective symbol (1), a localized negative
order elliptic estimate is
\[
\|u\|_{L^2}\le C\bigl(\|D_\infty u\|_{H^{-1}}
                         +\|u\|_{H^{-1}}\bigr).       \tag{5}
\]
For constant coefficients it follows directly from Fourier transform and
(1), with the low frequencies accounted for by the second term. For C1
coefficients, localize on small balls, freeze the principal coefficients,
and absorb their oscillation. Integrating the coefficient difference by
parts produces a zeroth-order term; multiplication by its continuous
coefficient followed by the compact inclusion L2 into H-1 is compact.
For each such compact lower-order map \(K:L^2\to H^{-1}\),
\(\|Ku\|_{H^{-1}}\le\eta\|u\|_2+C_\eta\|u\|_{H^{-1}}\).
Indeed, failure after normalization would give a bounded L2 sequence
converging to zero in H-1, hence weakly to zero in L2, while its compact
image did not converge to zero. Absorption gives (5) on each fixed interior
support. Constants depend on that coordinate geometry.

The curvature formula \(\partial\Gamma+\Gamma\Gamma\) and C1 metric
convergence first give \(A_j\to A_\infty\) strongly in H-1 locally.
Here \(A_\infty\) is initially a distribution. Index contractions and
algebraic frame changes are legitimate because their coefficients converge
in C1, which acts continuously by multiplication on H-1.

For an interior cutoff chi, use
\[
D_\infty(\chi A_j)=(D_\infty-D_j)(\chi A_j)
                    +\chi D_j A_j+[D_j,\chi]A_j.       \tag{6}
\]
Apply (5). The first term is \(o(1)\|\chi A_j\|_2\) and is absorbed.
The second tends to zero by (3). The commutator is multiplication by
\(P_j^a\partial_a\chi\), uniformly bounded in C1, so its H-1 norm
is bounded by the curvature H-1 convergence on a slightly larger chart.
The remaining \(\|\chi A_j\|_{H^{-1}}\) is bounded as well. Thus
\(\sup_j\|\chi A_j\|_2<\infty\).

Subtract (6) for j and k and apply (5) to \(\chi(A_j-A_k)\).
The operator differences tend to zero using this new L2 bound, the
Ricci-source terms tend to zero, and the commutator terms tend to zero
by C1 coefficient and H-1 curvature convergence. The full sequence is
therefore Cauchy in L2 where chi=1. The argument applies separately to
either Weyl half.

Since \(g_j\to g_\infty\) in C1, the curvature expressions
\(\partial\Gamma+\Gamma\Gamma\) converge distributionally. They identify
the preceding limit with \(W^+(g_\infty)\), and (4) gives
\(\operatorname{Ric}(g_\infty)=-g_\infty\) distributionally. The uniform
C1,alpha bound passes to this limit. Construct harmonic coordinates for
the limit metric alone; no common harmonic gauge for the sequence was
assumed. In these coordinates rewrite the weak Ricci system in divergence
form, whose coefficients are Lipschitz and whose lower-order terms are
C0,alpha. Interior W2,p regularity first justifies its nondivergence form;
Schauder bootstrapping then makes the limit smooth. This is the
classical harmonic-coordinate regularity mechanism, not a new smoothness
theorem; see [DeTurck--Kazdan, Sections 1, 4, 5](https://www.numdam.org/article/ASENS_1981_4_14_3_249_0.pdf).

## 4. Consequence for the calibrated limit

Assume in addition that the integral of the squared ordered spectral
distance from \((-1/6,1/12,1/12)\) tends to zero on a fixed inner ball.
Strong L2 convergence transfers this condition to the limit, whose spectrum
is exactly that constant triple there. The spectrum is incompatible with
a smooth Einstein germ of scalar curvature -4.

The local contradiction does not use integration over a closed manifold.
The harmonic-Weyl eigenframe equations give
\(\nabla\lambda_1=-X+Z\),
\(\nabla\lambda_2=X-Y\),
\(\nabla\lambda_3=Y-Z\).
Since the eigenvalues are constant and \(\lambda_2=\lambda_3\), one has
\(Y=0\), then \(X=Z=0\); the Weyl operator is parallel. Its algebraic
Weitzenbock reaction, however, is \(-3A_0/2\ne0\). This contradicts the
parallel equation. The identities use the conventions in
[Wu, Section 2](https://arxiv.org/pdf/1903.11818).

The exact requirement is now clearer: controlled coordinate geometry,
small weak source, and transfer of calibration density suffice. A bound
on Cotton L2 is not required. Producing such patches from the unrestricted
collapsed hypotheses remains unproved. The gauge/Sobolev constants and
buffered covering multiplicities cannot be omitted or inferred from a
small Ricci residual. This note supplies a conditional transfer argument,
not a new assumption-free pinching gap.
