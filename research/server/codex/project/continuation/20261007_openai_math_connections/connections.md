# Actual fields, concentration, and global variational bounds

## 1. Scope and common normalization

This note combines the owner's supplied web discussion with parallel readings of the primary manuscripts in the [OpenAI mathematics release](https://github.com/openai/math). The public source collection was retrieved on 7 October 2026 from revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The [release announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/) is dated 6 October. Its README describes 722 manuscripts in 372 result families and explicitly distinguishes levels of verification. We use individual statements with their hypotheses, not the number of released papers as evidence of validity.

Throughout the Einstein-gap discussion, \(M\) is a closed oriented smooth four-manifold, and

\[
P=\int|\operatorname{Ric}^{\circ}|^2,
\quad S=\int s^2,
\quad R=P+\frac S4,
\quad W_\pm=\int|W^\pm|^2,
\quad T_\pm=2\chi\pm3\tau.
\]

The Weyl norm is the curvature-operator norm on two-forms. Thus

\[
4\pi^2T_\pm=\frac S{24}+2W_\pm-\frac P2,
\qquad
8\pi^2\chi=W_++W_-+\frac S{24}-\frac P2.
\tag{1.1}
\]

For \(R>0\),

\[
\mathcal J=\frac{4P}{R},\qquad
\mathcal E=4-\frac{(\int s)^2}{VR}
=\mathcal J+\frac{S-(\int s)^2/V}{R}.
\tag{1.2}
\]

For an actual monopole class selected in a conformal class, put

\[
p=(a_g^+)^2,\quad
D_\beta=(1+\beta^{-1})S+6(\beta+1)W_+-72\pi^2p,
\quad
r=\frac1V\int|\operatorname{Ric}+g|^2,
\quad
\kappa_\beta=r+\frac{D_\beta}{V}.
\tag{1.3}
\]

The \(D_\beta/V\) normalization here differs from \(D_\beta/(\beta V)\) used in some finite-parameter lemmas. No inference below interchanges them.

The N1/I40/I41 backbone, finite-density endpoint theorem, and L′/K extensions are inherited from the project. For O11, the selected covering-family construction already gives a first coefficient strictly below four. Its strongest current proof and the precise family quantifiers must be retained. The sources below do not supersede that construction or establish a matching optimal lower bound.

## 2. The remaining endpoint has unbounded actual density

Here we use the project's finite-density theorem with its stated full conformal-class actual supply, positive budget, and class-square hypothesis. Its constant is uniform when \(\chi(M)/A\) is bounded. Suppose an admissible sequence satisfies

\[
\beta_j\longrightarrow\infty,\qquad \kappa_{\beta_j}\longrightarrow0.
\tag{2.1}
\]

In four dimensions the Hodge star on two-forms, and hence the harmonic self-dual projection of a fixed class, is conformally invariant. Consequently the same conformal-class supply permits choosing the theorem's budget to be \(A_j'=p_j\). If \(\chi(M_j)/p_j\) had a bounded subsequence, the finite-density theorem would contradict (2.1). Therefore

\[
\frac{\chi(M_j)}{p_j}\longrightarrow\infty.
\tag{2.2}
\]

This step uses the theorem's quantifiers; it is not justified by the mere existence of a solution at one metric if the applicable theorem requires more.

The classical joint inequality gives

\[
D_\beta\ge
\left(\sqrt{S/\beta}-\sqrt{6\beta W_+}\right)^2.
\tag{2.3}
\]

Indeed, subtracting the square from \(D_\beta\) leaves
\((\sqrt S+\sqrt{6W_+})^2-72\pi^2p\ge0\).
Also

\[
r=\frac PV+\frac1{4V}\int(s+4)^2.
\]

It follows that \(P/V\to0\), \(S/V\to16\), and then (2.3) gives
\(\beta W_+/V\to0\). Substitution into (1.3) and (1.1) yields

\[
\frac pV\to\frac{2}{9\pi^2},\qquad
\frac{T_+}{p}\to\frac34,\qquad
\frac\chi V\to\infty,
\qquad
\frac{W_-}{V}=8\pi^2\frac\chi V-\frac23+o(1)\to\infty.
\tag{2.4}
\]

Thus a remaining escape sequence has genuinely unbounded *actual* topology density and negative-chirality Weyl energy. A fixed-energy bubble theorem cannot alone exclude it. The implication would be invalid if one merely used \(\chi/A\to\infty\) together with \(p\ge A\); resetting the budget in (2.2) supplies the missing step.

This is a necessary-condition deduction from existing project results, not a new resolution of O10.

## 3. Joint concentration: positive currents and transverse moments

Source: [Taming implies compatibility on four-manifolds](https://github.com/openai/math/blob/main/preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/paper.pdf), family 342. Local original: [taming.pdf](../../archive/sources/20261007-openai-math/taming.pdf).

Theorem 1.1 concerns a **fixed smooth almost-complex structure on a closed four-manifold**, tamed by a symplectic form. The conclusion is existence of a compatible symplectic form; it does not assert integrability, compatibility with the original Riemannian metric, or preservation of the original class. Corollary 1.2 relates the tamed and compatible cones using the anti-invariant cohomology subspace.

For O10, the pertinent result is Theorem 5.1 and the concentration arguments in Lemma 4.4 and §6. The original works with a positive complex-line current \(\mathsf P\), a trace measure \(\mu\), an associated directional measure, and an anti-invariant \(L^2\) correction \(\mathsf Q\), satisfying

\[
d(\mathsf P+\mathsf Q)=0.
\]

In the notation of the source, the mass and directional hypotheses include

\[
\mu(B_r)\le Cr^2,\qquad I_r=O(r^4).
\]

The transverse-displacement argument supplies \(N_r=o(r^2)\). Their product, rather than either factor in isolation, controls the critical error:

\[
r^{-3}\sqrt{I_r}\sqrt{N_r}=o(1).
\tag{3.1}
\]

The conclusion identifies the density and proves closedness of the positive-density part. The useful information is that closure couples directional variation and displacement; separate absolute-value derivative estimates would lose that coupling.

An O10 application needs an actual construction of \(\mathsf P,\mathsf Q\) from the field equations, the correct positivity and closure, and uniform versions of the mass and directional bounds on the degenerating metrics. A scalar amplitude moment does not supply a complex-line directional moment. Nor do estimates for a fixed smooth background automatically provide uniform constants for varying backgrounds.

Another reusable component is Lemma 2.1's zero-order closed lift: using the Green operator and harmonic projection, it builds a right inverse to anti-invariant projection on closed forms. A sufficiently small correction preserves taming positivity. This is a fixed-background statement; the operator's higher Sobolev norms and the topology of its harmonic term must be tracked in a family.

If an actual closed self-dual two-form is already nowhere zero, the metric is already conformally almost-Kähler. In that branch, the final existence statement is not itself the missing new input. The concentration mechanism is the relevant part.

## 4. Same-test stability and the defect mass

Source: [A positive resolution of De Giorgi's conjecture in dimension eight](https://github.com/openai/math/blob/main/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/article.pdf), family 375. Local original: [degiorgi8.pdf](../../archive/sources/20261007-openai-math/degiorgi8.pdf).

The equation is the scalar quartic Allen–Cahn equation

\[
\Delta v=v^3-v,
\qquad
Q_v(\phi)=\int\bigl(|\nabla\phi|^2+(3v^2-1)\phi^2\bigr)\ge0
\quad(\phi\in C_c^1(\mathbb R^n)).
\tag{4.1}
\]

The stability tests are unrestricted compactly supported scalar tests, not volume-preserving, zero-mean, or merely radial tests. The manuscript first treats finite-density stable solutions and then excludes unbounded density in dimension seven, leading to its monotone dimension-eight conclusion.

### 4.1 The localization that carries geometric content

Equations (5.6)–(5.8), p.16, set \(q=1-v^2>0\), \(U=g^{-1}(v)\), and \(D=1-|\nabla U|^2\ge0\), where \(g\) is the one-dimensional profile. They give

\[
(-\Delta+3v^2-1)q=-q^2D,
\qquad
0\le Q_v(q\eta)
=\int\bigl(q^2|\nabla\eta|^2-q^3D\eta^2\bigr).
\tag{4.2}
\]

This is stronger than abstract nonnegativity of a Hessian: the same actual function supplies a weight and a *negative geometric-defect term*. It controls defect mass before a regular interface is assumed.

### 4.2 Combining tests without losing the common positive term

For \(F=(\sum_j\xi_j^2)^{1/2}>0\), direct differentiation gives

\[
\sum_j|\nabla\xi_j|^2-|\nabla F|^2
=\min_b\sum_j|\nabla\xi_j-\xi_jb|^2\ge0.
\tag{4.3}
\]

Here \(b\) is a cotangent vector; its minimizer is
\(b=\sum_j\xi_j\nabla\xi_j/F^2\). For a common scalar potential \(V\),

\[
Q(F)=\sum_j Q(\xi_j)
-\int\min_b\sum_j|\nabla\xi_j-\xi_jb|^2,
\tag{4.4}
\]

since \(VF^2=\sum_jV\xi_j^2\), regardless of the sign of \(V\). For
\(\xi_0=h\cos\theta,\xi_1=h\sin\theta\), the variance is exactly
\(h^2|d\theta|^2\). This cancels the corresponding switching cost.

Lemma 8.3 and Lemma 9.3, equation (9.10), implement this for local branches and bulk amplitudes in one physical test, including local finiteness, admissibility and exhaustion. They do not postulate a bounded total number of branches.

Proposition 9.1 controls bad-region terms at the same density scale. In §10 the geometric reach estimate and stability use the same amplitude
\(\psi=m_c\rho^{-2}\sqrt{W_*(\log\rho,d)}\). The numerical coefficients in the two inequalities cannot simply be subtracted: expanding the *same* gradient preserves the radial and transverse terms needed in the final comparison. Lemma 10.6 then combines the resulting radial integral with a same-region area lower bound and disjoint normal tubes. The argument does not prescribe a rate of divergence of the density.

### 4.3 What this asks of the actual SW system

An exact monopole already has a nonnegative residual-square Hessian. Under
\(D_{A+a}=D_A+\tfrac12c(a)\), its quadratic form is

\[
Q^{\rm SW}(a,\varphi)
=\|D_A\varphi+\tfrac12c(a)\Phi\|_2^2
+\|d^+a-dq_\Phi(\varphi)\|_2^2\ge0.
\tag{4.5}
\]

What is missing is a useful localization of this form. One possible precise target is to construct an actual admissible variation \(\mathscr L\eta\) such that

\[
0\le Q^{\rm SW}(\mathscr L\eta)
\le C\int w|d\eta|^2-c\int w\,\mathcal I_{\rm SW}\eta^2
+\operatorname{Err},
\tag{4.6}
\]

where \(\mathcal I_{\rm SW}\) controls the actual endpoint alignment defect and the errors satisfy the original budgets. Formula (4.6) is a proposed interface, not a proved SW estimate.

Simply taking \(a=0,\varphi=\eta\Phi\) does not achieve it. From the actual equations and the homogeneity of \(q\), one obtains

\[
Q^{\rm SW}(0,\eta\Phi)
=\int\bigl(|\Phi|^2|d\eta|^2+4\eta^2|q(\Phi)|^2\bigr).
\tag{4.7}
\]

There is no negative geometric-defect term here. A useful SW analogue of (4.2) therefore needs a different coupled variation or a different exact identity. If such a localization exists, the common-potential combination (4.4) explains how one might retain strength through the regular/transition decomposition. It does not itself construct that localization.

## 5. Curvature action: exploit Bianchi before estimating

Sources: [Zero-Plane Rigidity for Einstein Four-Manifolds](https://github.com/openai/math/blob/main/preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf) and [An L2 Einstein Gap for Nonnegatively Curved Four-Manifolds](https://github.com/openai/math/blob/main/preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf), family 348. Local originals: [boundary](../../archive/sources/20261007-openai-math/einstein-boundary.pdf), [gap](../../archive/sources/20261007-openai-math/einstein-gap.pdf).

### 5.1 The cancellation actually established in the source

The zero-plane paper uses \(\operatorname{Ric}=3g\). Write \(T=W^+\), \(U=W^-\). Proposition 2.4, pp.8–9, restricts \(Z=\nabla T\) to representation type \((5/2,1/2)\) and gives, in its conventions,

\[
\Delta T=6\bigl(T-(T^2)_0\bigr),\qquad
\Delta Z=\bigl(13-20Q_{5/2}(T)\bigr)Z.
\tag{5.1}
\]

The second equation has no \(W^-\) term. Lemma 5.1 then restricts the *actual curvature Hessian*

\[
\nabla^2T=Y+D_0,\qquad
Y\in(3,1),\quad D_0=\tfrac5{12}\operatorname{Tr}^*\Delta T\in(2,0).
\]

The tensor in the commutator must be the curvature block itself. This identity is not an identity for an arbitrary self-dual form or spinor.

### 5.2 The final positive square still contains negative chirality

Lemma 5.2 uses

\[
\mathsf P=4-\frac56\bigl(T_D+2B_F(T)\bigr)-U_D.
\]

On the free Hessian component,

\[
\mathsf P\ge(4-2x-2y)I\ge0,
\quad x=-\lambda_{\min}(W^+),\quad y=-\lambda_{\min}(W^-).
\tag{5.2}
\]

The last step is the sectional-curvature condition \(x+y\le2\). Proposition 5.3's final weighted expression still has \(-3b^2e\), with
\(b=|W^-|/\sqrt6\) and \(e=|\nabla W^+|^2/6\). Thus the paper does **not** prove a general elimination of \(W^-\).

For a near-Einstein application, Cotton sources must also be retained. The Einstein identity \(\operatorname{div}W=0\) is replaced by a first derivative of Ricci and scalar curvature. The integration by parts used in §5.2 acquires terms of the form

\[
-\int m\,(\nabla^k A_{ikjl})
\langle\nabla_i Z_j,Z_l\rangle,
\tag{5.3}
\]

for the relevant curvature-action tensor \(A\). The Ricci off-diagonal curvature block also changes the Hessian representation decomposition. An \(L^2\) Ricci residual alone does not control the displayed derivative products.

The transferable design is therefore: identify the actual constrained representation, calculate the compressed curvature action, and retain all weight derivatives and Cotton sources before estimating. A preliminary algebraic test is useful: if a self-adjoint candidate satisfies \(\mathsf P_0+t\mathsf Q(U)\ge0\) for all real \(t\), then \(\mathsf Q(U)=0\). This follows by testing every vector and letting \(t\) have either sign. This test applies only when the family really permits both signs of that unbounded direction.

### 5.3 Why the similarly named gap theorem is not the missing endpoint

The L2-gap theorem assumes a closed simply connected four-manifold with
\(\sec\ge0\), and absolute smallness \(P<\varepsilon_0\). Its classification conclusion uses the stated classification assumption; its smoothing argument is a separate component. Nonnegative sectional curvature controls the full curvature by scalar curvature, and the proof obtains diameter, Sobolev and smoothing bounds in that setting.

O10 concerns negative Einstein normalization, only small \(P/V\), and in the remaining branch (2.4) unbounded \(W_-/V\). In dimension four constant rescaling does not reduce \(P\). The source theorem therefore does not apply. Its Ricci-flow argument also leaves the original conformal class; one cannot silently assume that a merely conformal-class actual supply persists along that flow.

## 6. A global lower bound before local optimality

Source: [Triangular minimality for planar Coulomb renormalized energy](https://github.com/openai/math/blob/main/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf), family 090. Local original: [coulomb.pdf](../../archive/sources/20261007-openai-math/coulomb.pdf).

The source treats a linear Poisson constraint on a fixed flat background and a quadratic renormalized Dirichlet energy. Its proof is useful because it separates a competitor-entry theorem from a local comparison.

1. **Existence and entry, Lemmas 3.1–3.2.** A finite square torus of area \(N\), with \(N\) sites, has an energy minimizer. Collisions have diverging energy, and only the minimizer needs the separation estimate \(r_*=1/\sqrt\pi\).
2. **Admissible cells, Lemma 4.1.** The minimizer's periodic Voronoi data give the required distances and a sector count at most \(6N\).
3. **A single global comparison, Proposition 4.3, p.18.** A piecewise potential \(H\) has matching value traces across sectors and the prescribed singularities with zero constant term. For those compatible periodic data,

\[
W_T(h)=\sum_S J(S)+\frac12\int_T|\nabla(h-H)|^2,
\quad
J(S)=-2\pi\int_S H-\frac12\int_S^{\rm ren}|\nabla H|^2.
\tag{6.1}
\]

Normal derivatives need not match. If the singular expansion instead contains constants \(c_i\), the identity has the additional \(2\pi\sum_i c_i\) contribution. These constants cannot be dropped.

4. **Summation, Proposition 4.5.** A common affine sector bound
\(J(S)\ge K+\lambda\operatorname{Area}(S)+\mu\operatorname{Angle}(S)\), with \(K\le0\), combines with total area \(N\), total angle \(2\pi N\) and the sector count to bound the minimizer. Minimality then gives the bound for every finite-torus competitor. The proof includes the negative endpoint sectors, not just cells resembling the candidate optimum.
5. **Transfer to the plane, Proposition 2.4.** Periodic approximation and boundary cutoff estimates are separate ingredients. The identity is not directly applied to arbitrary nonperiodic planar configurations. The scalar inequalities completing the comparison use the paper's interval certificate and analytic tails; that certificate was not rerun in this reading.

For O11, the relevant chain is

\[
\text{infimum-preserving approximation}
\longrightarrow\text{entry for minimizing objects}
\longrightarrow\text{global comparison identity}
\longrightarrow\text{lower bound for all competitors}.
\tag{6.2}
\]

A collar or marked-core assumption cannot be supplied by naming a local model. It must follow from the chosen minimizing problem, or failure of entry must itself carry a sufficient global cost. Conversely, a direct global estimate may avoid decomposition entirely.

The nonnegative square in (6.1) uses linearity and a fixed background. It does not make \(P(g)\) convex as a functional of metrics, supply a geometric dual potential, or prove compactness of its minimizing sequences. Any proposed Einstein-gap comparison must also reproduce the real savings of the known sub-four constructions rather than silently normalizing every surgery to its old cost.

## 7. Collar extension and exact-form correction

### 7.1 Preserve Ricci structure when extending a controlled collar

Source: [Bounded scalar curvature and smooth extension of four-dimensional Ricci flow](https://github.com/openai/math/blob/main/preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf), family 351. Local original: [ricci-extension.pdf](../../archive/sources/20261007-openai-math/ricci-extension.pdf).

The main theorem concerns an actual Ricci flow on a fixed closed four-manifold. Its proof uses the scalar evolution equation, spacetime Ricci energy, and fixed-flow geometric controls. It is not a compactness theorem for arbitrary static metrics with small normalized Ricci residual.

Theorem 5.1, however, has a useful extension interface. From its high-order controlled near-flat quotient collar, with the stated nontrivial end group and weighted data, it constructs an ALE extension retaining the near-Ricci-flat modes. In its notation,

\[
\|\operatorname{Ric}(\widehat h)\|_{H^{k-2}_{q+2}}\le C m_1,
\qquad 1<q<2.
\tag{7.1}
\]

The weighted decay controls the ordinary exterior integral. For example the pointwise decay \(|\operatorname{Ric}|\le Cm_1r^{-q-2}\) gives

\[
\int_E|\operatorname{Ric}^{\circ}(\widehat h)|^2
\le C m_1^2\int_1^\infty r^{-2q-1}\,dr
\le C' m_1^2.
\tag{7.2}
\]

This cost is scale invariant in dimension four. Therefore collars satisfying the original theorem and
\(\sum_i C_i m_{1,i}^2=o(Q)\) would have total additional \(P\)-cost \(o(Q)\). This is a **conditional implication**, not a proof that general near-minimizers provide those collars or that their constants are uniform.

Lemma 4.3 also illustrates a local Bianchi cancellation. A putative Euclidean annular Ricci mode \(T=r^{-2}A\), with constant symmetric \(A\), has

\[
\operatorname{div}(T-\tfrac12\operatorname{tr}T\,I)
=-2r^{-3}(A-\tfrac12\operatorname{tr}A\,I)n.
\]

Vanishing for all radial directions forces \(A=0\) in dimension four. This computation excludes that mode, but needs the annular representation in an application and does not charge Ricci-flat Weyl bubbles.

### 7.2 Finite-dimensional projection must preserve the relevant order

Companion source: [Path selection and an elliptic inequality on degenerating Ricci-flat trees](https://github.com/openai/math/blob/main/preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf). Local original: [ricci-tree.pdf](../../archive/sources/20261007-openai-math/ricci-tree.pdf).

Theorem 2.2 fixes a finite Ricci-flat tree, with nontrivial joined end groups, decay and high-order weighted controls. Its functional is a renormalized scalar integral with a boundary mass term, homogeneous of length squared. It is not \(P\), \(\mathcal E\), or \(\mathcal J\).

Lemma 4.6 retains the finite-dimensional kernels and gives a projected approximation with metric/Ricci errors of order \(M\), and a renormalized-functional error of order \(M^2\). This is informative for reduction, but an \(O(M^2)\) error does not preserve the leading coefficient of a target energy that is itself \(O(M^2)\). One must calculate that term or make it \(o(M^2)\).

The path-selection step uses an all-order analytic/exponential admissibility class, not merely a finite gluing expansion. Fixed-tree estimates also give no automatic uniformity as the tree size grows with \(Q\). Ordinary Burns surgery has additional mismatches: its model is not Ricci flat and its standard spherical end has trivial group.

### 7.3 Estimate the exact two-form, not an arbitrary primitive

Source: [Deforming hypersymplectic four-manifolds to hyperkähler triples](https://github.com/openai/math/blob/main/preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026/paper.pdf), family 341, Lemma 10.4, pp.65–66. Local original: [hypersymplectic.pdf](../../archive/sources/20261007-openai-math/hypersymplectic.pdf).

The global theorem concerns a closed positive triple, and is not a new negative-Einstein supplier. The following Hodge-theoretic component is separately useful. For an exact real two-form \(h\) on a closed oriented four-manifold,

\[
0=\int h\wedge h=\|h^+\|_2^2-\|h^-\|_2^2,
\qquad
\boxed{\|h\|_2^2=2\|h^+\|_2^2.}
\tag{7.3}
\]

For a smooth self-dual form \(\varphi\) orthogonal to the self-dual harmonic forms, let \(G\) be the Green operator of the Hodge Laplacian. Then

\[
h=2dd^*G\varphi,\qquad h^+=\varphi,\qquad
\|h\|_2=\sqrt2\|\varphi\|_2.
\tag{7.4}
\]

Indeed on self-dual two-forms \(2d^+d^*=\Delta\), so \(h^+=\Delta G\varphi=\varphi\); exactness and (7.3) prove the norm identity. An exact anti-self-dual form has zero norm, giving uniqueness. This argument concerns \(h\) itself, not a bound for its primitive. It thus avoids a separate uniform one-form spectral gap at this level. Higher derivatives, positivity requirements and the coupled Dirac equation remain additional matters.

## 8. A different topological input: simplicial volume

Source: [An integral scalar curvature bound for real simplicial volume](https://github.com/openai/math/blob/main/preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/v126-proof.pdf), family 335. Local original: [scalar-simplicial.pdf](../../archive/sources/20261007-openai-math/scalar-simplicial.pdf).

Theorem 1.1 asserts, for every closed connected oriented smooth \(n\)-manifold, \(n\ge3\),

\[
\int(s_g^-)^{n/2}\,dV_g\ge a_n\|M\|,\qquad a_n>0.
\tag{8.1}
\]

Its proof depends on the companion manuscript [Positive scalar curvature forces rational inessentiality](https://github.com/openai/math/blob/main/preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/paper.pdf). The integral theorem's statements, conformal reduction and proof architecture were read here; the long proof and companion have not been independently re-established. All deductions in this section explicitly import (8.1).

### 8.1 A normalized gap with no gauge-field hypothesis

Put

\[
H=a_4\|M\|>0,\qquad T=(2\chi-3|\tau|)_+,
\qquad b=\frac{96\pi^2T}{H}<1.
\]

For either orientation (1.1) gives
\(P\ge S/12-8\pi^2T_\pm\). Choosing the smaller \(T_\pm\) and weakening it to its positive part gives

\[
P\ge\frac S{12}-8\pi^2T,
\qquad S\ge H,
\qquad\frac PS\ge\frac{1-b}{12}.
\]

The map \(x\mapsto4x/(x+1/4)\) is increasing, so

\[
\boxed{\mathcal E(g)\ge\mathcal J(g)\ge\frac{4(1-b)}{4-b}.}
\tag{8.2}
\]

Here \(S\ge H>0\) ensures \(R>0\). At \(b=1\) this becomes the zero bound; the positive-gap formula is not an argument for \(b>1\). If \(2\chi-3|\tau|\le0\), it gives \(\mathcal J\ge1\).

This is an elementary Chern–Weil consequence of the imported scalar theorem. It supplies an alternate input to normalized Einstein-gap estimates, not a new independent proof of (8.1).

### 8.2 A natural family and a limitation

Take finite covers \(N_j\) of unbounded degree of a closed oriented real-hyperbolic four-manifold \(N\). Then \(\tau(N_j)=0\), \(\chi(N_j)\) is positive and even, and \(\|N_j\|\to\infty\). Form

\[
M_j=N_j\#\left(\frac{\chi(N_j)}2-1\right)(S^1\times S^3).
\]

Connected-sum formulas give \(\chi(M_j)=2\), \(\tau(M_j)=0\), and additivity of simplicial volume gives \(\|M_j\|=\|N_j\|\). Thus \(T=4\), \(b_j\to0\), and

\[
\liminf_j\inf_g\mathcal E(g)\ge1
\quad\text{and}\quad
\liminf_j\inf_g\mathcal J(g)\ge1.
\tag{8.3}
\]

This family requires no monopole hypothesis in the displayed argument. It is not presented as previously unknown Einstein nonexistence: entropy and simplicial-volume obstructions already have a substantial literature.

For the original surgery family, \(\|X\#k\overline{\mathbb{CP}}^{,2}\#\ell(S^1\times S^3)\|=\|X\|\). If the base has a scalar recovery sequence with \(S\to32\pi^2A\), then (8.1) forces \(H\le32\pi^2A\). In the balanced window

\[
T_+=A(1-h),\qquad T_-=\frac A3(1+h),\qquad 0<h<\frac12,
\]

the smaller topological combination is \(T_-\), and

\[
b\ge1+h>1.
\tag{8.4}
\]

Thus this criterion does not determine that window's small-\(h\) lower bound or optimal first coefficient. It should be pursued, if useful, as a genuinely different topological input rather than advertised as an O11 solution.

Classical references for these deductions are [Gromov, Volume and bounded cohomology](https://www.ihes.fr/~gromov/wp-content/uploads/2018/08/435.pdf), §0.2 and §3.5 (mapping degree and connected sums); [Davis, A hyperbolic 4-manifold](https://people.math.osu.edu/davis.12/old_papers/4-mfld.pdf); and [Kotschick, Entropies, volumes, and Einstein metrics](https://arxiv.org/abs/math/0410215). The latter is a comparison reference, not a claim of novelty for (8.3).

## 9. Additional resources and the next mathematical use

The source collection also contains [Spectral scalar curvature and uniform Urysohn width](https://github.com/openai/math/blob/main/preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/main.pdf), family 336, as an adjacent spectral/geometric input. Its positivity input is for the scalar operator \(-4\Delta+s\). In a closed \(s=-4\) representative, the constant function disproves \(-4\Delta+s\ge1\). A positive potential on a twisted fifth line bundle is not this scalar operator. No implication for O10 or O11 is asserted here.

The [sharp Fourier certificate for planar circle packing](https://github.com/openai/math/blob/main/preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/paper.pdf), family 090, separates exact algebra, interval bounds, and analytic tails. Its named component order and independently reconstructed inequalities are useful for certified computations. It does not supply an Einstein filling theorem or repair the existing Fuchsian initial-value certificate merely by analogy. The coordinate-order and remainder-bound issue reported for `ach_bolt_fuchs.py` remains separate from the valid sub-four construction.

The six principal readings above identify three genuinely different kinds of missing information:

- **An equation-level pairing:** an actual-field localization that retains the defect term and permits the same test in two independent identities.
- **A uniform concentration constraint:** a closedness or curvature-action relation surviving the unbounded actual density in (2.4).
- **A variational entry and global lower bound:** an infimum-preserving passage that constrains all competing metrics, while retaining the background interaction responsible for sub-four savings.

None requires first proving every possible bubble-tree or limiting classification. A direct global argument is equally useful. Equally, a local identity is only an O10/O11 advance when its hypotheses can be obtained at the necessary scale: total-volume scale for the endpoint, and \(o(Q)\) error for first-order optimality.

The source texts are preserved so later work can return to the full proof rather than repeatedly deriving consequences from a compressed analogy. Subsequent Session proofs, corrections and constructions should be linked to the applicable source proposition and then back to the precise global conclusion they change.

## 10. Further inputs: backgrounds, exact rigidity, and limit spaces

These sources enlarge the available mathematics beyond the two remaining extremal questions. They are alternatives and additional inputs, not a requirement to open six new projects.

### 10.1 Negative Kähler–Einstein backgrounds from complex hyperbolicity

Source: [Canonical ampleness of compact hyperbolic Kähler manifolds](https://github.com/openai/math/blob/main/preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/canonical-ampleness.pdf), family 051. Local original: [canonical-ampleness.pdf](../../archive/sources/20261007-openai-math/canonical-ampleness.pdf).

Theorem 1.1 assumes that \(X\) is compact, connected and Kähler, of complex dimension at least one, and every holomorphic map \(\mathbb C\to X\) is constant. It concludes that \(K_X\) is ample and \(X\) is projective. Here hyperbolicity means Brody/Kobayashi hyperbolicity, not a negative-sectional-curvature metric.

The proof uses a holomorphic-disc derivative bound, canonical nefness and a quantitative volume estimate. For a fixed Kähler metric \(k\) and the source's disc bound \(D\), Proposition 7.1 gives

\[
\operatorname{Ric}(h)\ge-h
\quad\Longrightarrow\quad
h^n\ge e^{-D}\left(\frac n{2n+D}\right)^n k^n.
\]

The regularized metrics satisfy
\([h_t]=2\pi c_1(K_X)+t[k]\) and \(\operatorname{Ric}(h_t)=-h_t+tk\). The argument takes a limit of cohomological volumes; it does not assert smooth convergence of these metrics.

Combining the ampleness conclusion with the classical Aubin–Yau theorem gives a genuine negative Kähler–Einstein background

\[
[\omega_{\rm KE}]=2\pi c_1(K_X),\qquad
\operatorname{Ric}(\omega_{\rm KE})=-\omega_{\rm KE}.
\]

This may broaden the sources for background-interaction constructions. It does not ensure negative sectional curvature, local symmetry, prescribed ends, or actual monopoles on arbitrary surgeries. The relevant Spin\(^c\) structure, chamber and global actual supply must still be specified. If ampleness was already known for the chosen base, this source adds no new background-existence conclusion there.

### 10.2 Entropy equality as an exact geometric identifier

Source: [Entropy equality and local symmetry in negative curvature](https://github.com/openai/math/blob/main/preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/paper.pdf), family 339. Local original: [entropy-rigidity.pdf](../../archive/sources/20261007-openai-math/entropy-rigidity.pdf).

Theorem 1.1 assumes a closed connected smooth Riemannian manifold of dimension \(n\ge3\) with strictly negative sectional curvature. For its unit-speed geodesic flow,

\[
h_{m_L}(\varphi_1)=h_{\rm top}(\varphi_1)
\quad\Longleftrightarrow\quad\nabla\operatorname{Rm}=0,
\]

where \(m_L\) is normalized Liouville measure. It identifies the given metric, up to overall scale, with a rank-one locally symmetric geometry. In real dimension four the universal-cover models are real hyperbolic four-space and complex hyperbolic two-space.

The mechanism goes from entropy equality and Livšic cohomology to transported conormal volume data, then constructs smooth nondegenerate leaf markings and applies rigidity. It is an exact recognition principle, not existence on an unknown topology and not a quantitative near-equality theorem. Small \(L^2\) traceless Ricci curvature does not supply either strict negative sectional curvature or entropy equality.

### 10.3 Sharp isoperimetry when a sectional upper bound is available

Source: [Generalized Cartan–Hadamard isoperimetry and Euclidean equality rigidity](https://github.com/openai/math/blob/main/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf), family 337. Local original: [cartan-hadamard.pdf](../../archive/sources/20261007-openai-math/cartan-hadamard.pdf).

Theorem 1.1 assumes completeness, simple connectivity and \(\sec\le\kappa\le0\), and compares the ambient perimeter of any finite-volume finite-perimeter set with that of an equal-volume model ball. The Euclidean equality statement additionally treats bounded positive-volume sets. Corollary 1.3 supplies Faber–Krahn and Saint–Venant comparisons.

The proof proceeds from radial Hessian comparison to a sharp hypersurface Sobolev inequality and a differential inequality for the isoperimetric profile. This can provide spectral and cutoff estimates on domains or covers where the sectional hypothesis is already proved.

It does not additionally require a Ricci lower bound or noncollapse, but its sectional *upper* bound is substantive. In fact a whole four-dimensional sequence with \(\sec\le0\) has \(|\operatorname{Rm}|\le C_4|s|\), so \(S/V\to16\) would bound \(W_-/V\), contrary to (2.4). The remaining O10 escape cannot simply be placed in this subclass. Isoperimetry on a universal cover also need not descend to a uniform Sobolev inequality on the compact quotient.

### 10.4 Tangent uniqueness through summable motion

Source: [Uniqueness of tangent flows at the first singular time of embedded surface mean-curvature flow](https://github.com/openai/math/blob/main/preprints/Tangent-flow-uniqueness-2026-09-24/paper.pdf), family 355. Local original: [tangent-355.pdf](../../archive/sources/20261007-openai-math/tangent-355.pdf).

Theorem 1.1 concerns a smooth compact connected embedded surface without boundary in \(\mathbb R^3\), at its first singular time. At a fixed singular spacetime point and in fixed ambient coordinates, all parabolic blow-ups converge to the same multiplicity-one self-shrinking tangent. Mean convexity, a Type-I bound and a preselected spherical/cylindrical model are not assumed. Moving centers and continuation beyond the singular time are different questions.

The decisive input is actual dissipation. For the rescaled Gaussian area,

\[
\frac{d}{d\tau}\mathcal F=-d(\tau)^2,
\qquad
d(\tau)^2=\int|H+X^\perp/2|^2e^{-|X|^2/4}.
\]

Proposition 8.1 provides a local gradient inequality with a Gaussian tail, under the relevant graphical and area-ratio conditions. Section 9 chooses the spatial cutoff using the preceding energy decrease, obtains summable tails and \(\int d(\tau)\,d\tau<\infty\), and converts subsequential convergence to all-scale convergence.

The useful pattern is *summable geometric motion*, not merely a subsequence with small energy. A static O11 application would need its own dissipation or parameter-variation identity, entry to an appropriate neighborhood, and summable interscale errors. Near-minimality of \(P\) alone supplies none of these. The source does not prove uniqueness of a static Einstein bubble tree.

### 10.5 Weak Hessians and regular coordinates on singular limits

Source: [Weak Hessian bounds along every geodesic in RCD spaces](https://github.com/openai/math/blob/main/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/weak-hessian-geodesics.pdf), family 356. Local original: [weak-hessian.pdf](../../archive/sources/20261007-openai-math/weak-hessian.pdf).

Theorem 1.1 assumes a full-support unreduced \(\mathrm{RCD}(K,N)\) space, \(1<N<\infty\), a bounded globally Lipschitz function \(F\), and a bounded continuous \(G\) bounding its distributional Hessian from above in the stated quadratic-form sense. Then every constant-speed minimizing geodesic \(\sigma:[0,1]\to X\) of length \(\ell\) satisfies

\[
(F\circ\sigma)''\le\ell^2G\circ\sigma
\]

distributionally. Noncollapse is not an assumption of this theorem. The proof changes the reference measure to \(e^{\lambda F}m\), derives the relevant curvature-dimension bound, and concentrates endpoint measures while controlling the entropy. It carefully addresses the generator domain for the Lipschitz drift.

An \(L^2\) Hessian norm is not the required distributional quadratic-form bound. Nor does a small ordinary integral Ricci residual establish an RCD lower bound. The companion [Gigli characterization](https://github.com/openai/math/blob/main/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf) additionally uses a distributional *sectional* lower bound and Hausdorff reference measure.

Source: [Bi-Lipschitz Coordinates at Regular Points of Noncollapsed RCD Spaces](https://github.com/openai/math/blob/main/preprints/Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026/paper.pdf), family 357. Local original: [rcd-coordinates.pdf](../../archive/sources/20261007-openai-math/rcd-coordinates.pdf).

Theorem 1.1 requires noncollapsed \(\mathrm{RCD}(K,n)\), reference measure exactly \(\mathcal H^n\), and a point whose every tangent is Euclidean. The PDF states a dimensional distortion constant; the neighborhood radius depends on the point and space. The catalogue's family summary uses a weaker description of the constant, so the PDF statement is the relevant one.

The proof retains summable directional square-errors even when accumulated normalization matrices become unbounded. This is an instructive organization of degenerating coordinates. The conclusion is a local bi-Lipschitz chart in ambient distance, not a uniform chart radius or second-order regularity sufficient to pass the SW and curvature equations to a limit.

## 11. A direct Ricci-flow consequence of a positive traceless-Ricci gap

This is a derived application, conditional only on the explicitly imported finite-time extension theorem in family 351 and the stated geometric hypotheses. It is not an O10 or O11 solution.

**Proposition.** Let \(M\) be a closed smooth four-manifold with negative Yamabe invariant and

\[
\mathcal Y(M)<0,\qquad
p_0:=\inf_{g\in\operatorname{Met}(M)}\int_M|\operatorname{Ric}^{\circ}_g|^2\,dV_g>0.
\tag{11.1}
\]

Assume the finite-time scalar-curvature extension theorem of [family 351](https://github.com/openai/math/blob/main/preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf), Theorem 1.1. Then every maximal volume-normalized Ricci flow from a smooth initial metric satisfies

\[
\boxed{\sup_{0\le t<T_{\max}}\|s_{g(t)}\|_\infty=\infty.}
\tag{11.2}
\]

**Proof.** Use the four-dimensional normalization

\[
\partial_tg=-2\operatorname{Ric}+\tfrac12\bar s\,g,
\qquad
\bar s=V^{-1}\int s,
\]

for which \(V\) is constant. Suppose instead that \(|s|\le C\) throughout the maximal interval.

If \(T_{\max}<\infty\), put

\[
a(t)=\exp\left(-\frac12\int_0^t\bar s(u)\,du\right),\qquad
\tau(t)=\int_0^t a(u)\,du,\qquad
\widetilde g(\tau(t))=a(t)g(t).
\]

Then \(\partial_\tau\widetilde g=-2\operatorname{Ric}_{\widetilde g}\). The factor \(a\) has positive upper and lower bounds on the finite interval, \(\tau(T_{\max})<\infty\), and \(s_{\widetilde g}=a^{-1}s_g\) remains bounded. The imported extension theorem continues \(\widetilde g\) smoothly. Returning to fixed volume continues \(g\), contradicting maximality.

Now suppose \(T_{\max}=\infty\). Set \(m(t)=\min_Ms_{g(t)}\). The Yamabe inequality gives

\[
m(t)\le\mathcal Y(M)V^{-1/2}=-c<0.
\tag{11.3}
\]

One way to see this is that the Yamabe constant of the current conformal class is at least \(m(t)V^{1/2}\), while it is at most \(\mathcal Y(M)\). The negative sign and Hölder's inequality give this first comparison directly from the Yamabe quotient.

The minimum principle for scalar evolution gives, almost everywhere (or in the usual barrier sense),

\[
m'\ge\tfrac12m(m-\bar s)
\ge\tfrac c2(\bar s-m).
\tag{11.4}
\]

Thus \(m\) is nondecreasing and bounded, and
\(\int_0^\infty(\bar s-m)\,dt<\infty\). Since \(0\le s-m\le2C\),

\[
\operatorname{Var}_g(s):=\fint(s-\bar s)^2
\le\fint(s-m)^2
\le2C(\bar s-m).
\]

Hence the scalar variance is integrable in time. The exact mean-scalar identity is

\[
\bar s'=\frac{2P(g(t))}{V}-\frac12\operatorname{Var}_{g(t)}(s).
\tag{11.5}
\]

Integrating (11.5), using bounded \(\bar s\) and integrable variance, proves
\(\int_0^\infty P(g(t))\,dt<\infty\). This contradicts \(P(g(t))\ge p_0>0\). Both possible maximal intervals are excluded under the bounded-scalar assumption. \(\square\)

The immortal-flow argument is classical: see [Ishida, The normalized Ricci flow on four-manifolds and exotic smooth structures](https://arxiv.org/abs/0807.2169), Propositions 3 and 5. Its PDF and searchable text are in the source collection. We included the short computation to make the dependency and normalization explicit.

A genuinely uniform \(\mathcal J\)-gap together with a uniform positive scalar budget can provide (11.1): if every metric satisfies \(\mathcal J\ge c_0\), \(0<c_0<4\), and \(S\ge S_0>0\), then

\[
P\ge\frac{c_0S}{4(4-c_0)}\ge\frac{c_0S_0}{4(4-c_0)}>0.
\tag{11.6}
\]

A lower bound for \(P+D_2\) alone cannot replace this step. The proposition does not assert finite-time blow-up, a blow-up rate, or a classification of singularities.

## 12. Two further proof mechanisms retained from the web discussion

### 12.1 Concentration can carry a closed object rather than vanish

In §3, let \(E\) denote the positive two-dimensional density set. The source's decisive conclusion is
\(d(\mathbf1_E\mathsf P)=0\). Consequently, a suitable application need not first prove that all concentrated energy tends to zero. It may identify the concentrated part as a genuine closed geometric current, then constrain it through periods and global pairings. The source's directional and transverse moment estimates are exactly what prevent the density restriction from introducing a boundary.

For O10 this poses a concrete alternative question: can the actual curvature/type/radial system produce such a current with a useful pairing? A scalar measure such as \(|\nabla v|^2dV\) is not automatically an oriented positive two-current. The object and uniform estimates must be constructed from the equations; naming the measure a current supplies neither.

### 12.2 Finite weighted variation can close a multiscale contradiction

The tree paper in §7.2 proves a path-selection implication for its admissible reduced quantities. Schematically, if

\[
|dF|\le C\sqrt J\left(\sum_\alpha|dz_\alpha|
+\sum_e e^{-cL_e}|dL_e|\right),
\]

and a putative failure branch has \(F\ne0\), \(F\to0\), \(F^2\ge c_0J\), the selected path has finite total weighted variation. Therefore \(|d\log|F||\) is integrable, contradicting \(\log|F|\to-\infty\). The source retains kernels, cokernels and critical neck modes to obtain its actual finite-dimensional family. It does not assume an invertible linearization or an unobstructed moduli space.

The Ricci-flow companion also keeps a bad scale quantity on both sides of its closing inequality, of the form

\[
cK^2\le\varepsilon_j(K+1)^2,\qquad\varepsilon_j\to0,
\]

which forces \(K\to0\) without first assuming that \(K\) is bounded. Its \(K\) comes from actual spacetime Ricci energy and its outermost-scale selection. An O10 counterpart would have to be derived from the static actual-field equations; replacing \(K\) by a Weyl-density symbol is not a derivation.

These are useful ways to organize a proof around an uncontrolled quantity without burying it in a constant. They supplement the shared-test and global-comparison approaches above; none is prescribed as the only route.
