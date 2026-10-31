# Exact positive-spinor Hessian budget: no independent radial coercivity

2026-09-30. Source: integrated manuscript `proof:bounded-forms:e3` / `eq:lc-exact-hessian`, together with the actual strong-current limits. All displayed energy limits are normalized by volume.

The exact identity is
\[
\int|H|^2=\int|L\Phi|^2
-\int\operatorname{Ric}_{ij}\operatorname{Re}\langle P_i,P_j\rangle
+\sum_{ij}\int\operatorname{Re}\langle F_{ij}P_j,P_i\rangle
+\tfrac12\sum_{ij}\int|F_{ij}\Phi|^2.
\tag{1}
\]

At the calibrated endpoint choose the compatible frame
\[
\Phi=\sqrt{4/3}\,e_1,\qquad
P_1=t e_2,\quad P_2=-it e_2,\quad P_3=P_4=0,
\qquad t^2=2/9.
\]
The real determinant curvature is
\[
-iF_A=(2/3)(e^{12}+e^{34})+(1/3)(e^{12}-e^{34})
=e^{12}+(1/3)e^{34}.
\]
With the project's Clifford signs, the positive-spinor curvature is
\[
F_{ij}=\tfrac16c^+(e^{ij})+\tfrac12(F_A)_{ij}I.
\]
In particular \(F_{12}=\operatorname{diag}(i/3,2i/3)\) and
\(F_{34}=\operatorname{diag}(0,i/3)\); each of the four mixed pairs contributes \(\rho/36\) to \(|F_{ij}\Phi|^2\).

The four terms in (1) consequently have the following limits, in their displayed order:
\[
\frac4{27},\qquad\frac{12}{27},\qquad
\frac8{27},\qquad\frac8{27}.
\]
Thus
\[
\boxed{\fint|\nabla_A^2\Phi|^2\longrightarrow\frac{32}{27}.}
\tag{2}
\]
The passage to the limit in (1) uses the bounded-model-plus-small-\(L^2\) curvature fit and strong \(L^2\) convergence of \(|P|^2\); no differentiated curvature or \(W^-\) budget is used.

To see what this pays, write \(H_{ji}=(h_{ji},k_{ji})\). In the calibrated first jet, \(\nabla\zeta=0\) fixes
\[
h_{ji}=-\overline{\alpha_j}\alpha_i/\sqrt\rho,
\qquad (\alpha_1,\alpha_2,\alpha_3,\alpha_4)=(t,-it,0,0),
\]
so \(|h|^2=4/27\). Differentiated Dirac gives
\[
k_{j1}-ik_{j2}=h_{j3}+ih_{j4},\qquad
k_{j3}-ik_{j4}=-h_{j1}-ih_{j2}.
\]
The complementary squared sum on the right is \(8/27\). The pure-kernel quadratic contribution to \(\nabla\tau\) vanishes, leaving
\[
\nabla_j\tau=\rho(k_{j1}+ik_{j2},-k_{j3}-ik_{j4}).
\]
Hence the same total Hessian budget yields
\[
\begin{aligned}
\fint|\nabla\tau|^2
&=\rho_*^2\left[2\left(\frac{32}{27}-\frac4{27}\right)-\frac8{27}\right]+o(1)\\
&=\frac{256}{81}+o(1)=2m_*+o(1).
\end{aligned}
\tag{3}
\]
This is exactly the total torsion-gradient budget already obtained from its Lichnerowicz formula. At the calibrated algebraic level it does not assign a separate positive excess to the radial part of \(\nabla\tau\).

Coefficient replacement in the limiting decomposition must not be justified merely by bounded Hessian energy. It can instead be localized with a weight \((\rho-\rho_*)^2\) in the positive-spinor Hessian interchange; the weight-derivative cost is bounded by \(C\int|d\rho|^2|P|^2=o(V)\), already available from the strong-current estimate. This removes an amplitude-coefficient concentration ambiguity; it does not create a new radial term in (3).

**Conclusion:** the exact positive-spinor Hessian identity does sharpen the known coarse budget to \(32/27\), but its calibrated torsion content is the existing \(2m_*\) total-gradient identity. It has not supplied a new inequality forcing \(d|\tau|^2\) or \(d|v|^2\) to vanish. Counting (2) and (3) as two independent coercive budgets would double-count the same information.
