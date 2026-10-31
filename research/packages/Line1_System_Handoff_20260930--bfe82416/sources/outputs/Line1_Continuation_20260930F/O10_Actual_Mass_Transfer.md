# O10: transferring the radial defect to the original actual field

2026-09-30. This note proves two density-independent statements and records the precise unresolved differential term. It does not prove unrestricted O10.

## 1. A strong radial transfer for bounded resolvent approximations

Suppose \(u,v\) are sections of the same Hermitian bundle on a closed manifold, with
\[
\|u\|_\infty+\|v\|_\infty+\|\nabla^*\nabla v\|_\infty\le C,
\qquad h:=v-u.
\]
Then, with normalized norms,
\[
\boxed{
\big\||v|^2-|u|^2\big\|_{H^1}\le C'\|h\|_{H^1}.
}
\tag{1}
\]
The zero-order term is immediate. For the derivative write
\[
d(|v|^2-|u|^2)
=2\operatorname{Re}\langle v,\nabla h\rangle
 +2\operatorname{Re}\langle h,\nabla v\rangle
 -2\operatorname{Re}\langle h,\nabla h\rangle.
\]
The first and third terms are bounded by \(C\|\nabla h\|_2\). The middle term is controlled by the weighted Caccioppoli estimate from E:
\[
\||h|\nabla v\|_2\le C\|h\|_{H^1}.
\]
This proves (1), without a negative-spinor Hessian estimate or an opposite Weyl-energy budget.

Apply this to the bounded actual torsion cap \(u=b(|\tau|^2)\tau\) and its bounded-forcing resolvent \(v\). Since the existing construction gives \(u-v\to0\) in normalized \(H^1\),
\[
d|v|^2-d|u|^2\to0\quad\text{in normalized }L^2.
\tag{2}
\]
Thus the unresolved radial derivative is already a derivative of a bounded smooth function of the **actual** torsion magnitude; it is not created by the resolvent approximation.

## 2. The original actual mass identifies the differential order exactly

Put \(\rho=|\Phi|^2\), \(q_\Phi=|\nabla_A\Phi|^2\), and
\[
\nu=2\rho^2q_\Phi-|\tau|^2.
\]
The exact scalar equation gives
\[
\Delta\rho=-2q_\Phi+2\rho-\rho^2.
\]
Therefore
\[
\boxed{|\tau|^2=2\rho^3-\rho^4-\rho^2\Delta\rho-\nu.}
\tag{3}
\]
Differentiating,
\[
d|\tau|^2
=(6\rho^2-4\rho^3-2\rho\Delta\rho)d\rho
 -\rho^2d\Delta\rho-d\nu.
\tag{4}
\]
The strong-current estimates control \(\Delta\rho\) in \(L^2\), equivalently the trace of \(\nabla\zeta\); they do not yet control \(d\Delta\rho\) in \(L^2\). Substituting (4) into a radial term and integrating by parts moves **two derivatives of the current** onto the rest of the test, unless the complete combination has an additional cancellation. This issue must be handled in the combined actual equation, not by treating \(d|\tau|^2\) as an already small first-order error.

Equation (2) means that such a successful combined cancellation may be proved using the actual identity (3), then transferred to the resolvent field. It avoids losing a factor of the negative-curvature budget merely in that transfer.

## 3. A one-sided radial localization that follows without density control

Let \(a=|v|^2\), with \(a\to m_*>0\) in normalized \(L^2\), \(v\) uniformly bounded, and
\[
\nabla^*\nabla v=2v+r_v,\qquad \|r_v\|_2\to0.
\]
Then
\[
\Delta a=4a-2|\nabla v|^2+e_a,
\qquad\|e_a\|_2\to0.
\]
Testing with \((a-m_*)_+\) yields
\[
\int_{a>m_*}|da|^2
\le 4\int(a-m_*)_+a+\int(a-m_*)_+e_a\to0.
\tag{5}
\]
For \(0<\delta<m_*\), test instead with \((a-m_*+\delta)_+\). Dropping the nonpositive gradient-energy term gives
\[
\limsup_j\fint_{a_j>m_*-\delta}|da_j|^2
\le 4m_*\delta.
\tag{6}
\]
Thus any persistent radial energy must be supported increasingly on genuinely lower-amplitude regions. It cannot be placed exclusively in small fluctuations above the limiting amplitude.

This does not remove the defect: those lower-amplitude regions may have vanishing volume and nonvanishing radial energy. It also does not supply uniform integrability of \(|\nabla v|^2\) or nonzero mass of the fifth-line horizontal component. The scalar amplitude equation permits precisely the concentration alternative that the unrestricted proof must decide.

## 4. Current boundary of the combined-equation attempt

The double-weighted lemma in E controls \(\zeta\nabla^2v\nabla w\), and a small \(L^2\) first-order coefficient paired with \(\nabla v\nabla w\), uniformly in the opposite curvature. It does not alone control a term with \(d\Delta\rho\) paired with a tensor containing \(\nabla^2w\): direct integration by parts differentiates the test a third time. A proof that the full radial CR combination cancels that derivative has not been obtained in this note.

No new uncontrolled quantity has been hidden in the notation: (3) gives the exact actual-field source of the radial defect, (1) removes the resolvent-transfer loss, and (5)–(6) locate where any remaining concentration can occur. The final density-free implication remains open.
