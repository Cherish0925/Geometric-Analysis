# Integral selection of a spatially varying negative-Einstein calibration

23 September 2026.

## 1. Statement

Let \((M,g)\) be a closed oriented smooth four-manifold. Let \(\omega\)
be a smooth self-dual two-form with \(|\omega|^2=2\), and let \(t\) be
a smooth positive function satisfying \(0<m\le t\le M_0<\infty\).
Use exterior norms for forms and Hilbert--Schmidt norms for Weyl
endomorphisms. Set
\[
 A=t\left(\frac23 I-\omega\otimes\omega\right),\qquad
 R=W^+-A,\qquad E=\operatorname{Ric}+g,
\]
\[
 d=\fint(|E|^2+|R|^2),\qquad
 H_2=\fint|\nabla^2 A|^2.
\tag{1}
\]

**Theorem 1.** There is a constant depending only on \(m,M_0\) such that
\[
 \boxed{\quad
 \fint\left[|dt|^2+(t-\tfrac12)^2+|\nabla\omega|^2\right]
 \le C_{m,M_0}\left(d+\sqrt{dH_2}\right).
 \quad}                                                     \tag{2}
\]
The conclusion does not assume small amplitude variation. No Sobolev
constant, injectivity radius, volume lower bound, scalar spectral gap or
bound on \(W^-\) appears. The second-order budget in (1) is explicit.

The statement also holds when only the unoriented real line spanned by
\(\omega\) is globally defined. Pass to its orientation double cover;
\(A,t,d,H_2\) and all energy densities descend, and normalized integrals
are unchanged. Thus the assertion does not assume that a global Kähler
orientation of this line has already been chosen.

The theorem extends constant-amplitude compatibility in a specific
direction: the amplitude is a function, and its variation is part of
the conclusion. It does not classify general Weyl tensors. A global
nonvanishing rank-one model and the displayed spectral bounds are genuine
inputs. It supplies neither global integrability nor an exact Einstein
repair when \(d>0\).

## 2. The sourced conformal identity

Put
\[
 u=t^{1/3},\quad v=\log u,\quad
 \widehat g=u^2g,\quad \Omega=u^2\omega,
\]
\[
 Q_X=\nabla_X\omega-dv\wedge\iota_X\omega
                     +X^\flat\wedge\iota_{\nabla v}\omega,
 \qquad P=d\omega+2dv\wedge\omega.
\tag{3}
\]
The conformal connection formula gives
\(\widehat\nabla_X\Omega=u^2Q_X\) and \(d\Omega=u^2P\).
In particular \(|\Omega|_{\widehat g}^2=2\).

Let \(J=\operatorname{div}W(A)\), where \(W(A)\) is the Weyl
four-tensor associated with \(A\). The first-jet identity proved in the
companion variable-calibration calculation is
\[
 |J|^2=2t^2|Q|^2+4t^2|P|^2.
\tag{4}
\]
Its conformal kernel is essential: estimating \(\nabla\omega\) from
\(J\) before including \(dt\) would miss this kernel.

The weak contracted Bianchi identity gives, for any smooth test tensor
\(Z\),
\[
 \left|\int\langle J,Z\rangle\right|
 \le C(\|E\|_2+\|R\|_2)\|\nabla Z\|_2.
\tag{5}
\]
This is integration by parts; it requires no bound on \(\nabla E\).
Taking \(Z=J\), and using the parallel algebraic map \(A\mapsto W(A)\),
\[
 \fint|J|^2\le C\sqrt{dH_2},\qquad
 \fint|Q|^2\le C_m\sqrt{dH_2}.
\tag{6}
\]
All objects are smooth on the fixed closed manifold, so the test is
legitimate without a limiting regularity argument.

## 3. A coercive scalar equation without assuming Kähler geometry

We now turn (6) into control of \(du\). This step uses compactness of
the manifold only for integration by parts, not a compactness theorem
for a family of metrics.

Let \(\Delta=d^*d\) be nonnegative and write \(s=-4+e\), where
\(|e|\le2|E|\). Set
\[
 \zeta=\langle R\omega,\omega\rangle,\qquad |\zeta|\le2|R|.
\]
Scalar curvature and Weyl curvature transform as
\[
 \widehat s=u^{-3}(6\Delta u+su),\qquad
 \langle\widehat W^+\Omega,\Omega\rangle_{\widehat g}
       =-\frac83u+u^{-2}\zeta.
\tag{7}
\]
No complex-analytic identity has been used here.

Test the self-dual Weitzenböck equation against \(f\Omega\), for a
smooth real function \(f\). Because \(|\Omega|^2_{\widehat g}=2\),
the norm derivative term vanishes. Since \(\Omega\) is self-dual,
the exterior and codifferential cross terms coincide. Thus
\[
\begin{split}
 \int_{\widehat g} f(\widehat s+8u)
  ={}&\int_{\widehat g} f
       \left(3|d\Omega|^2-\tfrac32|\widehat\nabla\Omega|^2\right)\\
    &+3\int_{\widehat g}\langle df\wedge\Omega,d\Omega\rangle
      +3\int_{\widehat g}fu^{-2}\zeta.
\end{split}                                                   \tag{8}
\]
Equation (8) holds for an arbitrary almost-Hermitian form of constant
norm; closedness and integrability are not assumed.

Let \(u_0=2^{-1/3}\), and choose
\[
                     f=\frac{u-u_0}{u}.
\tag{9}
\]
Using \(d\mu_{\widehat g}=u^4d\mu_g\), the left side of (8) is
\[
 6\int|du|^2
 +8\int u(u^3-u_0^3)(u-u_0)
 +\int e\,u(u-u_0).
\tag{10}
\]
The potential in this expression is coercive:
\[
 u(u^3-u_0^3)(u-u_0)
 =u(u^2+uu_0+u_0^2)(u-u_0)^2
 \ge m^{1/3}u_0^2(u-u_0)^2.
\tag{11}
\]

Here are bounds for every term on the right of (8). The first is at
most \(C_{m,M_0}\int|Q|^2\) in absolute value, because
\[
 |\widehat\nabla\Omega|_{\widehat g}^2=u^{-2}|Q|^2,
 \quad |d\Omega|_{\widehat g}^2=u^{-2}|P|^2,
 \quad |P|^2\le3|Q|^2.
\]
For a unit normalized self-dual form,
\(|\xi\wedge\Omega|_{\widehat g}=|\xi|_{\widehat g}\).
Since \(df=u_0u^{-2}du\), the cross term in (8) is bounded by
\[
 3u_0\int|du||P|
 \le 3\int|du|^2+C\int|Q|^2.
\tag{12}
\]
Finally, combine the Weyl-error term and the last term in (10):
\[
 \left|\int u(u-u_0)(3\zeta-e)\right|
 \le 4m^{1/3}u_0^2\int(u-u_0)^2
       +C_{m,M_0}\int(|R|^2+|E|^2).
\tag{13}
\]
Equations (8)--(13) therefore yield
\[
 \fint\left[|du|^2+(u-u_0)^2\right]
 \le C_{m,M_0}\left(\fint|Q|^2+d\right).
\tag{14}
\]
No Poincaré inequality is used. The restoring term is the nonlinear
scalar-curvature potential, not a scalar spectral gap.

Since \(t=u^3\) and \(u\) stays in a fixed positive compact interval,
\(|dt|\le C|du|\) and \(|t-1/2|\le C|u-u_0|\).
Equation (3) also gives
\(|\nabla\omega|^2\le C(|Q|^2+|du|^2)\).
Insert (6) into (14) to prove (2).

## 4. The opposite sign of the variable amplitude

The sign of the amplitude is not silently discarded. Suppose instead
\(-M_0\le t\le-m<0\), retaining (1). Set \(u=|t|^{1/3}\), so that
the Weyl term in (7) is now \(+8u/3+u^{-2}\zeta\). The left side
of (8) becomes \(\int_{\widehat g}f(\widehat s-8u)\).
Choose \(f=u^{-2}\). Its expression in the original metric is
\[
 -6\int|d\log u|^2-4V-8\int u^3+\int e.
\]
The right side is
\[
 3\int|P|^2-\tfrac32\int|Q|^2
 -6\int\langle d\log u\wedge\omega,P\rangle+3\int\zeta.
\]
Use \(6ab\le3a^2+3b^2\), and cancel the resulting exterior
energy term. This gives the explicit sign obstruction
\[
 3\fint|d\log u|^2+4+8\fint|t|
 \le\tfrac32\fint|Q|^2+\sqrt{40d}.
\]
Together with (6), it proves
\[
 \boxed{(1+H_2)d\ge c_m>0.}                    \tag{14a}
\]
The upper amplitude bound is only needed when replacing \(H_2\) by
the alternative budget below. Thus a uniformly nonzero negative
amplitude is incompatible with negative-Einstein approximation at
vanishing joint error, even when the amplitude varies spatially.

## 5. Input alternatives and exact limit

Set \(\varphi=\sqrt t\,\omega\), so that
\[
 A=\frac{|\varphi|^2}{3}I-\varphi\otimes\varphi.
\]
The bounded-section Hessian estimate and its fourth-power-gradient
consequence give
\[
 H_2\le C_{M_0}(1+B_\varphi+d),\qquad
 B_\varphi=\fint|\Delta_H\varphi|^2.
\tag{15}
\]
The self-dual connection sees \(W^+,s,\operatorname{Ric}^{\circ}\),
not \(W^-\). Consequently an alternative statement of (2) is
\[
 \fint\left[|dt|^2+(t-\tfrac12)^2+|\nabla\omega|^2\right]
 \le C_{m,M_0}\left(d+\sqrt{d(1+B_\varphi+d)}\right).
\tag{16}
\]
Amplitude derivatives are included in \(\Delta_H(\sqrt t\,\omega)\);
they are not assumed small or suppressed by notation.

For a sequence, the sufficient condition is \(d\to0\) and
\(dH_2\to0\), not necessarily bounded \(H_2\). Equation (2)
then forces integral stabilization of both the amplitude and the line
direction. If \(d=0\) for a fixed smooth metric, (2) gives
\(t=1/2\) and \(\nabla\omega=0\); the orientation cover is negative
Kähler--Einstein. This exact conclusion is classical, not a new
classification theorem.

When \(W^+\) has simple lowest eigenvalue \(\lambda<0\), take its
unoriented eigenline and \(t=-3\lambda/4\). If the other two
eigenvalues are \(\lambda_2,\lambda_3\), then
\[
 |W^+-A|^2=\frac12(\lambda_2-\lambda_3)^2.
\tag{17}
\]
Thus (2) has a curvature-spectral interpretation on the actual line
cover. A uniform gap from zero and a genuine simple eigenline are still
required. The joint derivative budget is not supplied by Ricci pinching
alone.

## 6. Relation to the research program and classical theory

The constant-parameter criterion is in `round21_analytic.md`. The new
conformal first-jet identity is proved in the companion
`line1_variable_calibration.md`. The present argument adds the weighted
scalar test (9): on the negative branch it removes the need to prescribe
constant amplitude before applying differential compatibility.

Derdziński's exact conformal-Kähler theorem is the relevant classical
comparison: *Self-dual Kähler manifolds and Einstein manifolds of
dimension four*, Compositio Math. 49 (1983), 405--433,
[original article](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf).
The zero-source conformal kernel and the exact negative-Einstein
conclusion belong to that tradition. The present statement is an
integral stability estimate with explicit residual and derivative
budgets; exhaustive publication-priority verification is not asserted.

For Yau26 input, \(\fint|\operatorname{Ric}+g|^2\le4\delta_-^2\).
One must additionally establish the half-Weyl spectral conditions and
the joint budget. The theorem does not claim they follow for every
near-Einstein metric, and does not infer an exact metric from integral
parallelness alone.
