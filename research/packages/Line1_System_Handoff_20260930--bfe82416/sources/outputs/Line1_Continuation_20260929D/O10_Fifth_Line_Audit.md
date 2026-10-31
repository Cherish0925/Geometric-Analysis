# Independent audit of the fifth-line weak CR proof

Date: 2026-09-29. Scope: sections 3–6 of the supplied `O10_Finite_Density_Fifth_Line(1).md`, including the global line-bundle types and the estimates needed from sections 1–2. Comparison: `Line1_Continuation_20260929C/O10_All_Finite_Density.md`.

## Finding

Under the direct analytic inputs explicitly listed in the supplied note, the fifth-line argument closes at every **fixed finite** average anti-self-dual Weyl budget. I found no sign error in the Cartan identity, CR symbol, or positive curvature potential. The cutoff and weak-testing arguments can be written with the estimates below; they do not require uniform Sobolev constants.

This is an alternative proof of a finite-density conclusion already obtained in continuation C. It is a useful analytic simplification: it needs only nonzero average mass of the fifth-line section, rather than constant-length convergence and the logarithmic Chern-pairing lemma. It does **not** presently remove the finite Weyl budget. The main unresolved dependence occurs before, and during, the weak CR passage, even though the final line-bundle resolvent itself is independent of the anti-self-dual Weyl block.

This audit accepts the stated strong-current and resolvent inputs. It does not independently reprove every upstream estimate of the integrated manuscript.

## 1. Bundle bookkeeping

Let \(L=\det S^+\), \(E=S^-\otimes L\), and \(v\in E\). Then
\[
\det E=L^3,\qquad
t(v)\in S^+\otimes L^4,\qquad
\Phi\wedge t(v)\in L^5.
\]
The fourth power in the middle formula comes from one copy of \(L\) in the Clifford image of \(v\), and three copies in \(v\wedge\nabla v\). The final wedge contributes \(\det S^+=L\).

In an adapted frame, the remaining frame freedom changes the local determinant frame by \(e^{it}\). The coefficients have weights
\[
c_0\mapsto e^{-5it}c_0,\quad
\theta_2\mapsto e^{2it}\theta_2,\quad
b\mapsto e^{-3it}b.
\]
Thus \(D_5c_0\wedge\theta_2\) and \(d_{3A}\epsilon_b\) have exactly the same type as \((F^E)_{21}\). The adjoint test map has the corresponding inverse weight. No estimate on a naked local connection potential is needed.

The global definition
\[
c=\chi_\rho(\rho)\chi_m(m)
\frac{-\Phi\wedge t(v)}{2\sqrt\rho\,m^{3/2}}
\]
is legitimate when the fixed cutoffs vanish on neighborhoods of zero. The quotient is only used where its denominators have fixed positive lower bounds.

## 2. Independent finite algebra

I recomputed the Levi-Civita connection from the supplied Clifford matrices, rather than assuming the displayed Cartan equation. For each covector component, put
\[
X_j=\Omega_{-,\mathrm{LC}}C_j-C_j\Omega_{+,\mathrm{LC}},
\qquad
\Gamma^i{}_j=\tfrac12\operatorname{tr}(C_i^*X_j).
\]
Substitution into \(d\theta_2=-\Gamma^3{}_j\wedge e^j+i\Gamma^4{}_j\wedge e^j\) gives
\[
d\theta_2=i(2\mathfrak a-p-q)\wedge\theta_2
-\bar c\,[e^{13}+e^{24}+i(e^{14}-e^{23})].
\]
The computation was checked on all 15 independent real variables \(\kappa,\Re c,\Im c,p_i,q_i,\mathfrak a_i\), hence on all 90 real-linear two-form coefficients. Every residual was exactly zero. The arithmetic uses only Gaussian integers and dyadic rationals; no numerical tolerance is involved. In particular the \(\kappa\) terms cancel.

With the three SD basis forms each of squared norm 2, the matrix of \(\mathcal L\) is
\[
L=\frac12\begin{pmatrix}
0&0&-i&-1\\
1&i&0&0\\
-i&1&0&0
\end{pmatrix}.
\]
For \(D=\operatorname{diag}(2,1,1)\), the correct adjoint includes the target metric \(2I\). Direct multiplication gives
\[
L^*(2D)L=I-iJ_-,\qquad
J_-=\begin{pmatrix}
0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0
\end{pmatrix}.
\]
This is exactly the note's intrinsic identity \(\mathcal L^*\mathcal D\mathcal L=I-iJ_-\). Omitting the factor 2 from the two-form metric would introduce a false factor-of-two discrepancy.

Taking the SD part of the off-diagonal curvature indeed deletes \(|c_0|^2\Xi_-\). The SD-to-negative-spin curvature block is the traceless-Ricci block; the central determinant curvature is diagonal. Thus the remaining curvature term is controlled by \(|\operatorname{Ric}^\circ|\), without a hidden \(W^-\) term.

## 3. Weak CR passage: precise estimates

All norms in this section use the probability measure \(dV/V\). Fix a finite \(K\) for which
\[
\|\nabla v\|_4+\|\nabla^2v\|_2+\|c\|_4+\|D_5c\|_2\le C_K.
\]
The fixed lower-amplitude regions also have \(\nabla\Phi\) bounded in \(L^4\), and all frame-free structure errors below tend to zero in \(L^2\).

The curvature equation gives
\[
\mathcal L(D_5c_0)=-(d_{3A}\epsilon_b)^++G,\qquad
\|G\|_{4/3}\to0.
\]
For example
\[
\|pc_0\|_{4/3}\le\|p\|_2\|c_0\|_4,\qquad
\|c_0\mathcal R\|_{4/3}
\le\|c_0\|_4\|\mathcal R\|_2.
\]
These estimates require bounded critical factors, not their strong convergence.

For a test with
\[
\|w\|_\infty+\|D_5w\|_4+\|D_5^2w\|_2\le C_w,
\]
use the covariant test \(\chi\mathcal D\mathcal L(D_5w)\). Integration by parts bounds the differentiated error by
\[
\|\epsilon_b\|_2
\left[ C\|D_5^2w\|_2+
C(\|\nabla\Phi\|_4+\|\nabla v\|_4+\|d\chi\|_4)
\|D_5w\|_4\right]=o(1).
\]
This verifies the derivative transfer. It is not an assertion that \(d\epsilon_b\to0\) strongly.

Let \(Z_j\) be the support of cutoff derivatives; its relative measure \(\mu_j\) tends to zero. Since \(c_0\) and \(d\chi\) are bounded in \(L^4\),
\[
\|c_0d\chi\|_{4/3}
\le\mu_j^{1/4}\|c_0d\chi\|_2
\le C_K\mu_j^{1/4}\to0.
\]
This is sufficient to pair the cutoff error with \(D_5w\in L^4\). Nested fixed cutoffs keep all frame formulas away from zero amplitude. Covariant patching involves no partition-of-unity derivative uncontrolled by the actual fields: the maps are global bundle maps defined by the normalized fields on their domains.

On this support \(\bar J=(m/m_*)J_-\), and \(m\) is uniformly bounded. Hence
\[
\|\bar J-J_-\|_4\to0,\qquad
\left|\fint\langle(\bar J-J_-)D_5c,D_5w\rangle\right|
\le\|\bar J-J_-\|_4\|D_5c\|_2\|D_5w\|_4=o(1).
\]
The resulting global weak relation is therefore valid for this test class.

## 4. Bochner sign and the positive potential

Use a Hermitian product conjugate-linear in its first entry and \(\Omega(X,Y)=g(J_\Omega X,Y)\). Then the skew part of the weak pairing is
\[
i\Omega_{ij}\overline{D_i c}\,D_jw.
\]
After integration by parts, the antisymmetric second-derivative contraction is
\[
-\frac{i}{2}\Omega_{ij}[D_i,D_j]w
=-i\langle F,\Omega\rangle w.
\]
The derivative of \(\Omega\) contributes \(i\delta\Omega\cdot Dw\). This establishes the note's sign in (5.3).

Here \(f=-iF_A^-\), \(\bar\Omega=-4Q_v/m_*\), and \(f=-(27/32)Q_v+o_{L^2}(1)\). Consequently
\[
-i\langle 5F_A,\bar\Omega\rangle
\longrightarrow
5\frac{27}{32}\frac4{m_*}\frac{m_*^2}{8}
=\frac{10}{3}>0.
\]
The positive sign is consistent with the CR orientation and the line-bundle connection. It does not contradict the negative potential of the different rank-two cubic-spinor operator.

The two remaining errors are controlled as follows:
\[
\left|\fint(\mathfrak q-10/3)\langle c,w\rangle\right|
\le\|\mathfrak q-10/3\|_2\|c\|_2\|w\|_\infty=o(1),
\]
\[
\left|\fint\langle c,i\delta\bar\Omega\cdot Dw\rangle\right|
\le\|\delta\bar\Omega\|_2\|c\|_4\|Dw\|_4=o(1).
\]
Thus the weak positive-operator conclusion follows at fixed \(K\).

## 5. The resolvent test is legal

For fixed \(M\), solve
\[
(D_5^*D_5+10/3)w=T_M(c).
\]
Positive zeroth order gives invertibility and the bundle maximum principle gives \(\|w\|_\infty\le 3\|T_M(c)\|_\infty/10\). The equation bounds \(D_5^*D_5w\) pointwise.

The derivative-interchange estimate for a bounded section requires only Ricci curvature on the covector slot and the curvature \(5F_A\) on the line slot. Writing \(I=\fint|D^2w|^2\), \(J=\fint|Dw|^4\), it gives
\[
I\le C\fint|D^*Dw|^2+C\|w\|_\infty^2\fint|5F_A|^2
+C\fint(|\operatorname{Ric}|+|5F_A|)|Dw|^2,
\]
while bounded-section interpolation gives \(J\le C\|w\|_\infty^2 I\), with a harmless Laplacian term if a different interchange arrangement is used. Cauchy–Schwarz and Young close the estimate. The uniform \(L^2\) curvature budgets of this line connection and Ricci suffice; no \(W^-\) budget is needed at this final stage.

The contradiction then uses
\[
\fint|c|^2\to1,\qquad
\fint_{|c|>M}|c|^2\le M^{-2}\|c\|_4^4.
\]
First fix \(M\) sufficiently large relative to the finite \(C_K\), and only then send \(j\to\infty\). Reversing these quantifiers would be invalid for unbounded \(K_j\).

## 6. What can actually be simplified

The separate first bracket/prolongation theorem can be removed from the dependency chain. Continuation C supplies the shorter mass–phase–Dirac reduction:

1. \(N_v\to0\) kills the two \((1,0)\) derivatives.
2. The bounded Hessian budget and amplitude convergence imply \(dm\to0\).
3. The exact phase identity implies \(j_v\to0\).
4. Thus every first spinor component of \(\nabla v\) is small on fixed positive-amplitude sets.
5. The Dirac trace kills the remaining \(\bar Z_1\) second component.

Only the same \(\bar Z_2\) horizontal component survives. This does not remove the finite \(K\) dependence of the amplitude and derivative estimates, but avoids the extra bracket-testing machinery.

The new proof also avoids continuation C's constant-length covariance test for \(|c|\) and its logarithmic line-bundle regularization. The weaker average-mass statement suffices because the CR operator itself supplies a positive potential.

## 7. Boundary of the supplied fixed-budget proof

There are five explicit uses that the final line resolvent does not erase:

| Passage | Required estimate |
|---|---|
| Defining a useful global remaining component | \(\nabla v\in L^4\), \(\nabla^2v\in L^2\), and small mass on bad-amplitude sets |
| Integrating the CR structure error | \(\|\epsilon_b\|_2\,\|\nabla v\|_4\,\|Dw\|_4\to0\) |
| Cutoff terms | \(\mu_j^{1/4}\|c_0\|_4\|d\chi\|_4\to0\) |
| Replacing \(J_-\) by \(\bar J\) and treating drift | \(\|\bar J-J_-\|_4\|D_5c\|_2\to0\), \(\|\delta\bar\Omega\|_2\|c\|_4\to0\) |
| Nonzero mass in a fixed truncation | Uniform integrability of \(|c|^2\), obtained here from bounded \(\|c\|_4\) |

When \(K_j\to\infty\), none of these products is forced to tend to zero merely because its first factor does. A subsequence cannot generally repair that mismatch. Moreover \(\fint|c_j|^2\to1\) alone allows its entire mass to escape beyond every fixed truncation.

Accordingly, the supplied fixed-budget proof alone does not control unrestricted sequences. A quantitative continuation can nevertheless control the displayed joint products under a growth relation between the primitive endpoint errors and the Weyl budget. Such a growth result is a separate deduction, not a correction to the sign or validity of the supplied argument; the quantitative audit below records that distinction.


## 8. Independent audit of the quantitative unbounded-budget continuation

I independently checked `O10_Alternative_Global.md`, including its primitive error aggregate. The proposed extension is valid with the covariance step retained:
\[
 H=(1+\fint|W^-|^2)^{1/2},\qquad
 \eta H^3\to0
 \quad\Longrightarrow\quad\text{no actual endpoint sequence}.
\]
Here \(\eta\to0\) dominates the specified amplitude, bounded-resolvent, actual first-order, curvature-fit, and positive-spinor errors. It must not hide any conclusion about \(dm\), \(j_v\), the remaining connection error, or \(c\). The companion note's definition meets that condition. It makes no unproved identification of \(\eta\) with a power of the original scalar defect.

The powers are as follows, with fixed normalization of all cutoff levels:

| Quantity | Independently checked bound |
|---|---|
| \(\|\nabla^2v\|_2\) | \(CH\) |
| \(\|\nabla v\|_4\) | \(CH^{1/2}\) |
| \(\|dm\|_2,\|j_v\|_2,\|\epsilon_b\|_2\) | \(C\eta^{1/2}H^{1/2}\) |
| Measure of fixed bad-amplitude sets | \(C\eta^2\) |
| Gradient square on bad-amplitude sets | \(C\eta H\) |
| \(\|c\|_2,\|c\|_4,\|D_5c\|_2\) | \(C, CH^{1/2}, CH\) |
| Weak CR error against a unit test | \(C\eta^{1/2}H\) |

The last line includes the structure remainder \(G\), derivative transfer, cutoff, normalized-to-polynomial complex-structure replacement, and Bochner drift. For example, the potentially largest derivative-transfer term is
\[
 \|\epsilon_b\|_2\|\nabla v\|_4\|Dw\|_4
 \le C\eta^{1/2}H.
\]
The cutoff contribution is bounded by
\[
 \mu(\mathrm{bad})^{1/4}\|c_0\|_4\|d\chi\|_4
 \le C\eta^{1/2}H.
\]
The replacement \(J_-\to\bar J\) costs the same amount, since bounded \(m\) gives \(\|m-m_*\|_4\le C\eta^{1/2}\), while \(\|D_5c\|_2\le CH\). Thus no larger unrecorded power of \(H\) appears in the weak CR step.

The decisive extra argument concerns mass. Merely using \(\|c\|_4^4\le CH^2\) would require a truncation level \(M\) of order \(H\); because the test bounds then grow like \(M\), that route only yields the stronger sufficient condition \(\eta H^4\to0\). It does **not** justify the claimed cubic power.

The covariance test repairs this issue. Put \(q=|\nabla v|^2\), \(q_*=2m_*\), and \(T(q)=q/(1+q)\). The scalar identity gives
\[
 I:=\fint\frac{(q-q_*)^2}{1+q}
 \le C\bigl(\eta+\|dm\|_2\|\nabla^2v\|_2\bigr)
 \le C(\eta+\eta^{1/2}H^{3/2}).
\]
Since \(\fint q\le C\),
\[
 \|q-q_*\|_1\le C I^{1/2}.
\]
In addition, the definition of \(c_0\) is exactly the Hermitian orthogonal projection of \(b\) onto the complex line generated by \(\theta_2\). Therefore
\[
 |b|^2=2|c_0|^2+|\epsilon_b|^2
\]
is an exact identity. On a fixed positive-amplitude region,
\[
 q-2m|c_0|^2
 =\frac{|dm|^2}{4m}+m|q_{\mathrm{phase}}|^2
 +m|\epsilon_b|^2\ge0.
\]
Adding the bad-region and cutoff contributions, and replacing \(m\) by \(m_*\), gives
\[
 \|q-2m_*|c|^2\|_1\le C\eta H.
\]
Consequently
\[
 \boxed{\||c|^2-1\|_1
 \le C\left[(\eta+\eta^{1/2}H^{3/2})^{1/2}+\eta H\right]\to0.}
\]
This validates a **fixed** \(M>2\), whose line-resolvent test norms are independent of \(H\). The weak error \(C\eta^{1/2}H\) tends to zero under \(\eta H^3\to0\), while the test pairing tends to 1. The contradiction follows.

Accordingly, the companion note proves a genuine conditional extension to sequences with unbounded Weyl budget. An unrestricted escape must satisfy
\[
 \liminf_j\eta_j(1+b_j)^{3/2}>0
\]
for the specified primitive error aggregate, or it has a subsequence covered by the argument. This is not the density-free O10 gap: the actual equations have not yet been shown to force the excluded growth relation. The finite-budget audit in sections 1–7 and this quantitative extension are compatible.
