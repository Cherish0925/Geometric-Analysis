# General critical-background Burns insertion: a missing synthesis and its consequences

This note uses the two supplied manuscripts, especially A01.52, A01.53R and the binding correction A02.59D. It closes one connection between their proved ingredients. It does not claim a solution of the four global questions.

## 1. Precise result

Let \(g\) be a smooth oriented four-dimensional metric, critical for
\[
P(g)=\int |\operatorname{Ric}^{\circ}_g|^2\,dV_g
\]
on a neighbourhood containing the full support of a Burns insertion at \(p\). Set \(R^+=W^++sI/12\). Suppose \(\zeta\in\Lambda_p^+\) is a unit eigenvector of \(R^+\), with eigenvalue \(\mu\), and set
\[
T=(R^+|_{\zeta^\perp})^\circ.
\]
Combining the corrected remainder theorem A02.59D with the two explicit curvature-sector correctors gives an actual smooth competitor on \(X\#\overline{\mathbb {CP}}^2\), equal to \(g\) outside the chosen ball, such that
\[
\boxed{P(g_\varepsilon)=P(g)+8\pi^2-8\pi^2\mu\varepsilon
+4\pi^2\bigl[-\mu(\mu-s/8)-|T|^2\bigr]\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2).}
\]
Here the remainder depends on the fixed smooth background and fixed insertion data. No Einstein assumption, and no smallness of \(\operatorname{Ric}^{\circ}_p\), is required for this competitor statement.

Consequently, at a kernel direction,
\[
P(g_\varepsilon)=P(g)+8\pi^2-4\pi^2|T|^2\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]
The residual condition \(|T|^2>C|\operatorname{Ric}^{\circ}_p|^2\) retained in A02.59D.4 is unnecessary after incorporating A01.53R. The latter supplies the precise corrector that was absent when that condition was written.

This is a synthesis of existing ingredients, with the integrated cross-term argument below made explicit. The manuscript already asserts the corresponding *formal* cancellation in A01.53R; the new connection is that A02.59D supplies the needed critical-background remainder, so the assertion becomes a genuine competitor theorem.

## 2. Fixing the Burns-tail convention

In Euclidean blowdown coordinates, with \(J=J_\zeta\), \(u=|x|^2\), the correct tail is
\[
B(x)=\frac{uI-xx^T-(Jx)(Jx)^T}{u^2}.
\]
Thus \(g_{B,\varepsilon}=\delta+\varepsilon B\) is the scalar-flat ASD Burns metric in the normalization used by A01.52 and A02.59D.

A01.53R prints \((v_0v_0^T+v_1v_1^T)/u^2\) while also declaring \(v_0=x\) and \(J=J_3\). Taken literally, these conventions do not describe this Burns tail. With the quaternionic frame of A01.52 it is \((v_1v_1^T+v_2v_2^T)/u^2\). The following calculation uses the invariant displayed formula, so it does not depend on this indexing typo.

For \(E\in\operatorname{Sym}^2_0\), define
\[
q=x^TEx,\qquad E_H=(E+J^TEJ)/2,\qquad q_H=x^TE_Hx,
\]
\[
f=-q/4,\qquad V=-uEx/12+qx/6,
\]
\[
h_E=-\tfrac16\{uE+qI-(Ex)x^T-x(Ex)^T\}.
\]
Direct differentiation gives
\[
h_E=\mathcal L_V\delta+2f\delta.
\]
For the actual Burns tail,
\[
\operatorname{tr}B=2/u,\qquad \operatorname{div}B=-2x/u^2,
\qquad \operatorname{div}B-\tfrac12d\operatorname{tr}B=0.
\]
Using the positive-coordinate Laplacian \(\Delta=\sum_i\partial_i^2\),
\[
\Delta'_B f=-B^{ij}\partial_{ij}f=-q_H/u^2,
\qquad
\Delta\left(-\frac{q_H}{8u}\right)=q_H/u^2.
\]
The last identity uses \(\operatorname{tr}E_H=0\), so \(q_H\) is a harmonic quadratic and \(\Delta(q_H/u)=-8q_H/u^2\). Therefore
\[
f_\varepsilon=f-\varepsilon q_H/(8u),\qquad
\Delta_{g_{B,\varepsilon}}f_\varepsilon=O(\varepsilon^2)
\]
on every fixed annulus.

The degree-zero corrector is
\[
K_E=\mathcal L_VB-\frac q2 B-\frac{q_H}{4u}\delta.
\]
The infinitesimal conformal/diffeomorphism variation
\(\mathcal L_Vg_{B,\varepsilon}+2f_\varepsilon g_{B,\varepsilon}\)
equals \(h_E+\varepsilon K_E+O(\varepsilon^2)\). Conformal covariance and naturality give zero variation of \(W^+\); the scalar-curvature variation is \(-6\Delta_{g_B}f_\varepsilon\), hence is \(O(\varepsilon^2)\). This proves the A01.53R cancellation with the corrected coordinate convention.

## 3. Why the entire integrated coefficient has no Ricci contribution

Write
\[
\mathscr C=(2W^+,s/\sqrt{12}),\quad
\Phi(h,K)=\frac1{8\pi^2}\int_{S^3}[z^2]
\left|D\mathscr C_{\delta+zB}[h+zK]\right|^2_{\delta+zB}
\,dV_{\delta+zB}.
\]
This is the corner functional in corrected A02.59D. It is quadratic in the pair \((h,K)\), including all metric-dependent norm and volume factors. The formula is invariant under the subgroup \(SU(2)_-\) commuting with all self-dual quaternionic structures; this subgroup fixes \(B\) and \(\zeta\).

The background curvature-jet decomposition under this subgroup is:

* \((s,W^+)\): trivial representation;
* \(W^-\): spin 2;
* \(\operatorname{Ric}^{\circ}\cong\Lambda^+\otimes\Lambda^-\): three copies of spin 1.

The corrector maps \(W^-\mapsto K_W\) and \(E\mapsto K_E\) are equivariant: they are constructed tensorially from \(x,\delta,J,B\) and the relevant curvature jet. Consequently the polarized integrated quadratic form has no cross terms between any of these three sectors. This is Schur orthogonality for real inequivalent compact-group representations; it concerns the complete coefficient, rather than only the first curvature derivative.

In the Ricci sector,
\[
D\mathscr C_{\delta+zB}[h_E+zK_E]=O(z^2),
\]
by the preceding explicit calculation. Its squared norm has zero \(z^2\) coefficient. The same vanishing in the \(W^-\) sector is exactly the A01.50 identity inherited by A01.52 and independently checked in A02.59D.3.

Choose
\[
K=K_{s,W^+}+K_W+K_E,
\]
where \(K_{s,W^+}\) is the exact eigenvector-sector corrector already computed in A01.52/A02.59D.2. Orthogonality and the two zero squares imply
\[
\Phi(h,K)=\Phi(h_{s,W^+},K_{s,W^+})
=-\mu(\mu-s/8)-|T|^2.
\]
The claim needed here is that this coefficient is attained by an explicit corrector. No claim about an unrestricted global minimum over arbitrary neck ansatz is required.

Finally A02.59D.1 gives the full expansion for *every fixed* degree-zero corrector on any background critical throughout the support. It already proves that higher jets contribute only to \(O(\varepsilon^2)\), and that the linear flux is \(-8\pi^2\mu\varepsilon\). Applying that theorem to the displayed sum proves Section 1.

## 4. Consequence for minimizing degeneration

Assume an ideal minimizing configuration has an exact energy identity and contains a Burns bubble that can be relocated, with compatible topology, to any regular point of a critical bulk component. These are the reconstruction hypotheses of A02.53.B; they are not consequences of the local expansion.

At every such point:

1. \(\lambda_{\max}(R^+)>0\) would produce a first-order saving, contradicting minimality.
2. Once \(R^+\le0\), a kernel direction is an eigenvector. If the restriction to its perpendicular plane is not scalar, the negative logarithmic coefficient produces a saving, again contradicting minimality.

Hence every surviving bulk, **including a non-Einstein critical bulk**, satisfies
\[
R^+\le0,
\qquad
\ker R^+\ne0\Longrightarrow
\operatorname{spec}(R^+)=(0,s/8,s/8)
\]
at each accessible regular point, apart from the zero-curvature case \(R^+=0\). For a smooth closed critical bulk, scalar curvature is constant; if it is negative, this conclusion excludes all Kähler-type kernel spectra \((s/4,0,0)\).

This removes the Ricci-residual exception in the current minimizer-selection route. It does not remove the strictly negative cone \(R^+<0\), and it does not give the Einstein-only claim that the degenerate-kernel contact set has empty interior. The latter proof uses \(\delta W^+=0\), unavailable on a general critical bulk.

## 5. What many small independent insertions can and cannot accomplish

Suppose the background balls and correctors belong to a fixed bounded-geometry family (in particular, lifted balls on covers of a fixed smooth compact background), and all insertions are disjoint. Then the local differences add exactly, because the metric agrees with the background outside these balls. For kernel insertions on an Einstein background,
\[
P(g_{\boldsymbol\varepsilon})=P(g)+8\pi^2k
-4\pi^2\sum_{i=1}^k |T_i|^2\varepsilon_i^2\log(1/\varepsilon_i)
+O\left(\sum_{i=1}^k\varepsilon_i^2\right),
\]
with a common remainder constant.

If \(\max_i\varepsilon_i\to0\), and \(|T_i|\) remains uniformly bounded, then
\[
\frac{P(g_{\boldsymbol\varepsilon})-P(g)}{8\pi^2k}\longrightarrow1.
\]
Indeed, divide by \(k\) and bound the average correction by the maximum of \(\varepsilon^2\log(1/\varepsilon)\), which tends to zero. Thus an arbitrarily large number of individually shrinking standard cells does not yield an \(o(k)\) law, let alone \(k^2/A\) in a regime \(k/A\to0\).

Conversely, fixing one sufficiently small scale first gives a definite saving per cell on fixed-base covers. That construction establishes a strictly improved linear upper bound. To reach a different asymptotic order, one must leave this uniformly controlled independent-cell regime: a collective background change, an unbounded-geometry rescaling, or another geometric channel is needed. No purely algebraic rearrangement of the same expansion changes this conclusion.

## 6. Why zero-cost ALE channels are not removed

The proof uses the nonzero Burns tail and its precise topological insertion. Ricci-flat ALE pieces can have zero \(P\), different end groups, and different relative characteristic corrections. They do not acquire the Burns charge merely because they carry two-cycles. The preceding relocation restriction applies to an actual relocatable Burns component. It is not a statement that all resolution components cost \(8\pi^2\), nor an exclusion of orbifold or partial-collapse minimizers.

## Outcome

The completed connection is a genuine extension of the local competitor theorem and its conditional variational consequence from Einstein points to arbitrary smooth critical backgrounds. It removes one previously retained Ricci-sector restriction. The four public questions still require their global missing information: this local theorem neither proves unrestricted attainment nor excludes the negative-curvature cone, orbifold absorption, or collapse.
