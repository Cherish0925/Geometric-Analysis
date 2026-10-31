# 允许 Weyl 模式、方程提供的估计与无泡核心

来源提交：`ff3c3a828b56c0a9824d8fe2fd412b210a229120`。

本卷为原文阅读汇编，不是新论文或独立证明认证。先读第1卷的状态与第8卷的修订。源路径用于定位；原文相对链接仍相对于原文件。TeX原文使用源码块保留。



---

## 原稿 1: line1_variable_calibration.md

来源：`mathematics/current/line1_variable_calibration.md`；范围：`full`。

原文件 SHA-256：`a9f4737ecf8c56f9c0a0225b4e2e79ba43209ee51ed6734f6ac704264c374734`。

---
title: Variable-amplitude Weyl calibration with a divergence source
date: 2026-09-23
geometry: margin=1in
header-includes:
  - \usepackage{esint}
---

# Statement and conventions

Let $(M,g)$ be a smooth closed oriented four-manifold, and let $\omega$ be
a smooth self-dual two-form with $|\omega|_g^2=2$. Let $t$ be smooth with
$0<\tau\le |t|\le T$. Set

\[
 A=t\left(\frac23 I-\omega\otimes\omega\right),\qquad
 R=W_g^+-A,\qquad E=\operatorname{Ric}_g-\sigma g,
 \qquad \sigma\in\{-1,1\}.
 \tag{1}
\]

Two-forms have the exterior-algebra norm, and $A,R$ have the
Hilbert--Schmidt endomorphism norm. The algebraic Weyl tensor associated
with $A$ is

\[
 \mathcal W(A)_{ijkl}=\sum_{a,b}A_{ab}(\epsilon_a)_{ij}(\epsilon_b)_{kl},
 \quad J_{jkl}=\nabla^i\mathcal W(A)_{ijkl},
 \quad |J|^2=\sum_{j,k,l}J_{jkl}^2,
 \tag{2}
\]

where $(\epsilon_a)$ is an orthonormal basis of $\Lambda_g^+$. In
particular $|\mathcal W(A)|^2=4|A|^2$. Put

\[
 v=\tfrac13\log|t|,\quad \widehat g=e^{2v}g,
 \quad \widehat\omega=e^{2v}\omega,\quad
 Q_X=\nabla_X\omega-dv\wedge\iota_X\omega
                   +X^\flat\wedge\iota_{\nabla v}\omega.
 \tag{3}
\]

Here $|Q|^2$ uses the exterior norm in the two-form slots. The connection
transformation formula gives
$Q=e^{-2v}\widehat\nabla\widehat\omega$. Define

\[
 d=\fint_M(|E|^2+|R|^2),\qquad
 H=\fint_M|\nabla^2 A|^2,\qquad
 \phi=\sqrt{|t|}\,\omega,\qquad
 B_\phi=\fint_M|\Delta_H\phi|^2.
 \tag{4}
\]

All unmarked averages and norms refer to $g$. The Hodge Laplacian is
nonnegative. The derivatives in $H$ are covariant derivatives on
$\operatorname{End}(\Lambda_g^+)$.

**Theorem 1 (exact identity and weak estimate).** The following pointwise
and integral identities hold:

\[
 \boxed{|J|^2=2t^2|Q|^2
       +4t^2|d\omega+\tfrac23d\log|t|\wedge\omega|^2,}
 \tag{5}
\]

\[
 \boxed{\int_M\left(|\widehat\nabla\widehat\omega|_{\widehat g}^2
                   +2|d\widehat\omega|_{\widehat g}^2\right)dV_{\widehat g}
       =\frac12\int_M|t|^{-4/3}|J|^2dV_g.}
 \tag{6}
\]

There are constants depending only on the displayed parameters such that

\[
 \fint_M|J|^2\le C\sqrt{dH},\qquad
 H\le C_T(1+B_\phi+d),
 \tag{7}
\]

and consequently

\[
 \boxed{\fint_M\left(|Q|^2
      +2|d\omega+\tfrac23d\log|t|\wedge\omega|^2\right)
 \le C_{\tau,T}\sqrt{d(1+B_\phi+d)}.}
 \tag{8}
\]

Equivalently, the conformal energy in (6), divided by
$\operatorname{Vol}_{\widehat g}(M)$, is bounded by the right-hand side
of (8), with another $C_{\tau,T}$. No derivative of Ricci curvature,
bound on $W^-$, Sobolev constant, injectivity radius, diameter, or lower
volume bound is assumed. Neither $dt$ nor $d\omega$ is assumed small.

The source $\Delta_H(\sqrt{|t|}\omega)$ includes amplitude derivatives.
They have been included in an explicit budget, not discarded. Another
sufficient budget is

\[
 B_\omega+D_t=\fint_M\left(|\Delta_H\omega|^2
                        +|\nabla^2t|^2+|dt|^4\right):
 \qquad H\le C_T(1+B_\omega+D_t+d).
 \tag{9}
\]

The exact zero-source implication, $J=0\Rightarrow
\widehat\nabla\widehat\omega=0$, is the classical conformal Kähler
mechanism. The quantitative result here is the explicit sourced identity
and the weak near-Einstein estimate with its stated differential budget.
An $L^2$ bound on a connection defect does not provide coordinates, a
nearby Kähler metric, or geometric compactness.

# Proof of the exact identity

The Levi-Civita transformation formula on a two-form is

\[
 e^{-2v}\widehat\nabla_X(e^{2v}\omega)
 =\nabla_X\omega-dv\wedge\iota_X\omega
                         +X^\flat\wedge\iota_{\nabla v}\omega.
 \tag{10}
\]

Thus $Q_X\in\Lambda_g^+$ and $\langle Q_X,\omega\rangle=0$.
Alternating (10) gives

\[
 \operatorname{Alt}Q=d\omega+2dv\wedge\omega
                         =e^{-2v}d\widehat\omega.
 \tag{11}
\]

We calculate at a point in an oriented orthonormal coframe indexed
$0,1,2,3$. Let

\[
 \Omega_1=e^{01}+e^{23},\quad
 \Omega_2=e^{02}+e^{31},\quad
 \Omega_3=e^{03}+e^{12},\quad \omega=\Omega_1.
\]

The frame of $\Lambda^+$ used for components is $\Omega_a/\sqrt2$.
Write $\nabla_i\omega=a_i\Omega_2+b_i\Omega_3$ and $h_i=\nabla_it$.
At the chosen point,

\[
 \nabla_iA=h_i\operatorname{diag}(-4/3,2/3,2/3)
       -2t\begin{pmatrix}0&a_i&b_i\\a_i&0&0\\b_i&0&0\end{pmatrix}.
 \tag{12}
\]

The coefficients $\widetilde a_i,\widetilde b_i$ of $Q_i$ are the rows of

\[
 \begin{pmatrix}
 a_0-h_3/(3t)&b_0+h_2/(3t)\\
 a_1-h_2/(3t)&b_1-h_3/(3t)\\
 a_2+h_1/(3t)&b_2-h_0/(3t)\\
 a_3+h_0/(3t)&b_3+h_1/(3t)
 \end{pmatrix}.
 \tag{13}
\]

Substitute (12) in (2). Direct contraction of the three displayed
$\Omega_a$ shows that the resulting $J$ equals the divergence obtained
from the purely angular array

\[
 -2t\begin{pmatrix}0&\widetilde a_i&\widetilde b_i\\
 \widetilde a_i&0&0\\\widetilde b_i&0&0\end{pmatrix}.
 \tag{14}
\]

This is an equality of tensors, not only their norms. In particular, for
arbitrary column vectors $a,b$, let
$V_1=-2t(\Omega_2^Ta+\Omega_3^Tb)$,
$V_2=-2t\Omega_1^Ta$, and $V_3=-2t\Omega_1^Tb$.
The tensor represented by (14) is
$J_{jkl}=\frac12\sum_c(V_c)_j(\Omega_c)_{kl}$ with
$a=\widetilde a,b=\widetilde b$. Since the $\Omega_c$ are orthogonal
and have full component norm squared four,

\[
 |J|^2=4t^2\left(|a|^2+|b|^2
                   +|\Omega_2^Ta+\Omega_3^Tb|^2\right).
 \tag{15}
\]

Here $|Q|^2=2(|a|^2+|b|^2)$ and
$|\operatorname{Alt}Q|^2=|\Omega_2^Ta+\Omega_3^Tb|^2$, proving (5).
All twelve first-jet entries in (12) are arbitrary; no differential
equation was used.

The conformal norm and volume rules give

\[
 |\widehat\nabla\widehat\omega|_{\widehat g}^2=e^{-2v}|Q|_g^2,
 \quad |d\widehat\omega|_{\widehat g}^2=e^{-2v}|\operatorname{Alt}Q|_g^2,
 \quad dV_{\widehat g}=e^{4v}dV_g.
\]

Multiplying (5) by $|t|^{-4/3}/2=e^{-4v}/2$ proves (6).

For a prescribed divergence source $S=\operatorname{div}\mathcal W(W^+)$,
the exact tensor relation is $J=S-\operatorname{div}\mathcal W(R)$.
Equation (5) therefore gives a direct strong-source estimate whenever
this difference is controlled in $L^2$. The next argument obtains that
control weakly from zeroth-order Ricci and Weyl errors and a second-order
budget for $A$.

# Weak Bianchi and the second-order budget

The contracted Bianchi identity and the parallel self-dual projection
express $\operatorname{div}\mathcal W(W^+)$ as a fixed algebraic
contraction of $\nabla E$ and $\nabla\operatorname{tr}E$. Since
$\mathcal W(A)=\mathcal W(W^+)-\mathcal W(R)$, integration by parts
gives, for every smooth three-tensor $Z$,

\[
 \left|\int_M\langle J,Z\rangle\right|
       \le C(\|E\|_2+\|R\|_2)\|\nabla Z\|_2.
 \tag{16}
\]

With $Z=J$, the parallel nature of (2) gives
$|\nabla J|\le C|\nabla^2 A|$, proving the first inequality of (7).
It does not assert an estimate for $\nabla E$.

For completeness, the bounded-section estimates used below are

\[
 \int|\nabla z|^4\le16\|z\|_\infty^2\int|\nabla^2z|^2,
 \tag{17}
\]

\[
 \int|\nabla^2z|^2
 \le2\int|\nabla^*\nabla z|^2
       +32\|z\|_\infty^2\int|\operatorname{Ric}|^2
       +33\|z\|_\infty^2\int|F|^2.
 \tag{18}
\]

Here $F$ is the curvature of the metric bundle of $z$, with full two-index
component norm. These estimates follow from integrating
$\operatorname{div}(|\nabla z|^2\langle z,\nabla z\rangle)$ and the
bundle Hessian identity. In the latter identity one first swaps the two
Hessian slots and then commutes derivatives on $\nabla z$; this produces
Ricci curvature, $F\nabla z$, and $|Fz|^2/2$, with no derivative of $F$.
Cauchy--Schwarz and Young's inequality, using (17), give (18). The full
derivation appears in `round21_analytic.md`, Section 2; these inequalities
are homogeneous in the volume and have no geometric compactness constant.

Apply them to $z=\phi=\sqrt{|t|}\omega$, whose pointwise norm is at most
$\sqrt{2T}$. Since $t$ has constant sign on each connected component,

\[
 A=\operatorname{sgn}(t)\left(\frac{|\phi|^2}{3}I
                                      -\phi\otimes\phi\right),
 \quad |A|^2=\frac83t^2.
 \tag{19}
\]

The curvature of $\Lambda^+$ satisfies

\[
 |F^{\Lambda^+}|^2\le C\left(|W^+|^2+s^2+|\operatorname{Ric}^{\circ}|^2\right).
 \tag{20}
\]

Its $W^-$ contribution vanishes, because the anti-self-dual Lie algebra
factor acts trivially on $\Lambda^+$. Equations (1), (4), and (19) imply

\[
 \fint\left(|\operatorname{Ric}|^2+|F^{\Lambda^+}|^2\right)
 \le C_T(1+d).
\]

The Weitzenböck equation, for arbitrary $\phi$, reads

\[
 \nabla^*\nabla\phi
       =\Delta_H\phi+2W^+\phi-\frac{s}{3}\phi.
\]

It supplies
$\fint|\nabla^*\nabla\phi|^2\le C_T(1+B_\phi+d)$.
Using (17)--(18) therefore gives

\[
 \fint\left(|\nabla^2\phi|^2+|\nabla\phi|^4\right)
                    \le C_T(1+B_\phi+d).
 \tag{21}
\]

Differentiate the quadratic expression (19) twice:
$|\nabla^2A|\le C(|\phi||\nabla^2\phi|+|\nabla\phi|^2)$.
This proves the second inequality of (7). Equations (5) and
$|t|\ge\tau$ now prove (8). For the conformal average, use (6),
$|t|^{-4/3}\le\tau^{-4/3}$, and
$\operatorname{Vol}_{\widehat g}(M)\ge\tau^{4/3}\operatorname{Vol}_g(M)$.

Alternatively apply (17)--(18) to $\omega$, whose norm is fixed, and
differentiate $A=t(2I/3-\omega\otimes\omega)$. This gives

\[
 |\nabla^2A|^2\le C_T\left(|\nabla^2\omega|^2+|\nabla\omega|^4
                       +|\nabla^2t|^2+|dt|^2|\nabla\omega|^2\right).
\]

Young's inequality bounds the final term by
$(|dt|^4+|\nabla\omega|^4)/2$, proving (9).

# Endpoint, zeros, and relation to the earlier calibration

If $J=0$, (5) forces $Q=0$, so $\widehat\omega$ is parallel for
$\widehat g$. Its norm is $\sqrt2$, and its associated orthogonal almost
complex structure is parallel, hence integrable. Thus
$(M,\widehat g,\widehat\omega)$ is Kähler. When $R=0$ and
$\operatorname{Ric}=\sigma g$, contracted Bianchi gives $J=0$ automatically.
The simple Weyl eigenvalue is $-4t/3$. At the exact endpoint the Kähler
scalar curvature is consequently

\[
 \widehat s=-8\operatorname{sgn}(t)|t|^{1/3}.
 \tag{22}
\]

Without an Einstein or scalar-curvature equation, (5) cannot bound $dt$
by $J$. The linear map from the twelve variables $(dt,a,b)$ in (12) to
$J$ has rank eight. Its four-dimensional kernel is obtained by setting
the eight entries of (13) to zero, leaving all four components of $dt$
free. Thus an estimate $|dt|\le C|J|$ is already false at the first-jet
level. A further equation is necessary to select a constant amplitude.

This theorem deliberately assumes both a globally supplied normalized
form and a nonzero lower amplitude bound. If only the simple eigenline
is supplied, local choices of $\omega$ differ by sign; the formula for
$A$ and all the energies descend. A global form can be chosen on the
orientation double cover of that real line bundle. This cover addresses
the sign of the eigensection, not zeros of $t$.

On an open nonzero-amplitude locus, (5) is valid locally, but no extension
of $\widehat g=|t|^{2/3}g$ across $t=0$ is asserted. The constants in
(8) deteriorate as $\tau\downarrow0$. No measure estimate for the zero
set is hidden in the proof.

For the earlier model
$A_{\psi,t}=t(|\psi|^2I/3-\psi\otimes\psi)$, normalization on a locus
where $q=|\psi|^2>0$ gives
$\omega=\sqrt{2/q}\,\psi$ and effective amplitude $\widetilde t=tq/2$.
The theorem applies if that normalized data satisfies its hypotheses;
the corresponding budget is the budget for
$\sqrt{|\widetilde t|}\omega=\sqrt{|t|}\psi$. If $\psi$ has zeros,
this normalization does not produce a global application. The polynomial
zero-set argument in the earlier fixed-parameter gap and the nonvanishing
conformal theorem here address different regimes.

# Primary-source comparison and verification

Derdziński, *Self-dual Kähler manifolds and Einstein manifolds of dimension
four*, Compositio Mathematica 49 (1983), Proposition 5(i), pp. 420--421,
proves the local conformal Kähler conclusion for harmonic $W^+$ with at
most two eigenvalues, on $\{W^+\ne0\}$. His conformal metric is
$|W^+|^{2/3}g$ up to a constant. Since $|A|^2=8t^2/3$, this is exactly
the conformal factor in (3), up to a constant. Thus the zero-source
conclusion is classical. [Primary article](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf).

LeBrun, *Einstein Metrics, Harmonic Forms, and Conformally Kähler Geometry*,
arXiv:1903.00956v2, uses the conformal covariance of the harmonic-Weyl
equation in Section 2 and obtains global alternatives in Theorem 2 under
a near-symplectic harmonic-form hypothesis and a sign condition. Those
hypotheses differ from the rank-one calibration and nonvanishing
assumptions here. His treatment of zeros is not supplied by (5)--(8).
[Primary article](https://arxiv.org/html/1903.00956).

The accompanying `line1_variable_calibration_check.py` checks the
connection correction, all 64 components of (12)--(14), the norm identity
on all twelve independent first-jet variables, the rank-eight symbol and
its conformal kernel, and the conformal energy exponent. The integration
by parts, curvature representation, and global consequences are proved
above; symbolic checks do not establish these analytic assertions.

Local development baseline: commit `8113dd1`. The relevant user-supplied
literature discussion is Section 6 of the theoretical-structure and
literature-integration note in `line1_sources_20260923/`.



---

## 原稿 2: line1_variable_negative_selection.md

来源：`mathematics/current/line1_variable_negative_selection.md`；范围：`full`。

原文件 SHA-256：`44acfcf90e039f48d8c8becd056ae020689273e680f1bf3ee9801fc48ff42f03`。

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



---

## 原稿 3: line1_half_weyl_regularity.md

来源：`mathematics/current/line1_half_weyl_regularity.md`；范围：`full`。

原文件 SHA-256：`8a4906f27a470e41f4ab9f676523e06cc8e0b8d2c4ce6fb76751ad028bc6faa0`。

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



---

## 原稿 4: line1_signed_harmonic_weyl.md

来源：`mathematics/current/line1_signed_harmonic_weyl.md`；范围：`full`。

原文件 SHA-256：`7a334cce5373ad0b483458ec27ce57554b272e2033a487bef88d2c25380d0faf`。

# A negative-eigenvalue balance for harmonic self-dual Weyl curvature

23 September 2026.

## 1. Result

Let \((M,g)\) be a closed connected oriented smooth four-manifold with
\(\delta W^+=0\). Order the eigenvalues of the self-dual Weyl endomorphism as
\(\lambda_1<\lambda_2\le\lambda_3\). The lowest eigenvalue is assumed
simple everywhere. Set
\[
 t=-\frac34\lambda_1>0,\qquad h=\lambda_3-\lambda_2\ge0,
 \qquad z=\frac{h}{4t}<1.                                      \tag{1}
\]
The symbol \(h\) denotes a scalar splitting, not a metric. Work on the
orientation double cover of the lowest eigenline if necessary, and choose
its smooth self-dual eigenform \(\omega\) with \(|\omega|^2=2\). All
energies below descend to \(M\); using normalized integrals does not change
them under this cover.

Put
\[
 u=t^{1/3},\quad u_0=2^{-1/3},\quad \widehat g=u^2g,
 \quad\Omega=u^2\omega,
\]
\[
 Q_X=\nabla_X\omega-d\log u\wedge\iota_X\omega
                      +X^\flat\wedge\iota_{\nabla\log u}\omega,
 \qquad P=d\omega+2d\log u\wedge\omega.                       \tag{2}
\]
Thus \(\widehat\nabla\Omega=u^2Q\) and \(d\Omega=u^2P\).

**Theorem 1 (exact balance).** The following identities hold:
\[
 \boxed{\int_M\frac32\frac{1-z^2}{1+z^2}\,t^{2/3}|Q|^2
       =\frac32\int_Mt^{-1/3}h^2,}                            \tag{3}
\]
\[
 \boxed{|P|^2=\frac{z^2}{1+z^2}|Q|^2.}                       \tag{4}
\]
No derivative budget or bound on \(W^-\) is assumed.

**Theorem 2 (scalar restoring estimate).** Suppose, for fixed constants,
\[
                   t\ge m>0,\qquad z\le\theta<1.
\tag{5}
\]
Then
\[
\boxed{\begin{split}
 \fint_M\big[&|du|^2+|\nabla\omega|^2
               +u(u^3-u_0^3)(u-u_0)\big]\\
 &\le C_{m,\theta}\fint_M\big[h^2+(s+4)^2\big].
\end{split}}                                                 \tag{6}
\]
In particular, the left side controls \(\fint(u-u_0)^2\).
If additionally \(t\le M_0\), then
\[
 \boxed{\fint_M\big[|dt|^2+(t-\tfrac12)^2+|\nabla\omega|^2\big]
 \le C_{m,M_0,\theta}\fint_M\big[h^2+(s+4)^2\big].}            \tag{7}
\]
These are estimates for an eigenform supplied by the actual curvature,
not a hypothetical auxiliary form. There is no Sobolev constant,
injectivity-radius bound, scalar spectral gap, second-order input,
or full-curvature bound. Formula (6) also requires no upper bound on
\(t\). The harmonic-Weyl condition is a genuine equation hypothesis;
small Ricci error alone does not imply it.

For \(\operatorname{Ric}=-g\), the scalar term vanishes. Compared with the
previous variable-amplitude estimate
\(C(d+\sqrt{dH_2})\), (7) removes \(H_2\) and gives a linear bound in
\(d=\fint h^2/2\), in this exact harmonic-Weyl setting.

## 2. Signed conformal normalization

The derivation uses the weighted harmonic-Weyl identities underlying
Catino--Dameno, equations (2.8), (2.9), and (3.1)--(3.9), but with the
lowest negative eigenvalue rather than the largest positive one. The sign
changes the rigidity identity into an energy balance. We give the algebra
and the sign step explicitly.

In \(\widehat g\), the chosen eigenvalue is
\(\alpha=-4u/3\). Define the signed weight
\[
                 F=-\frac3{4u},\qquad F\alpha=1.
\]
Conformal covariance gives \(\delta_{\widehat g}(u^{-1}
W^+_{\widehat g})=0\). Multiplication by the constant \(-3/4\) gives
\(\delta_{\widehat g}(FW^+_{\widehat g})=0\).
Although a conformal factor must be positive, \(F\) here is a signed
tensor weight, not the conformal factor. Every equation in the next
display is linear in that weight, so its negative sign is legitimate:
\[
 0=\widehat\nabla^*\widehat\nabla(FW)
       +\frac{\widehat s}{2}FW-6FW^2+2F|W|^2I.               \tag{8}
\]
This is the standard bundle-valued Weitzenböck identity for the
divergence-free self-dual tensor \(FW\); here and in this section
\(W=W^+_{\widehat g}\).

Let
\[
 \rho=\lambda_2/\lambda_1=-\tfrac12+\tfrac32z,
 \qquad k=\frac{1-\rho}{2+\rho}=\frac{1-z}{1+z}.
\tag{9}
\]
On the open dense set where the other two eigenvalues have locally
constant multiplicities, extend \(\Omega=\Omega_1\) to an oriented
orthogonal eigenframe of \(\Lambda^+\), each of norm \(\sqrt2\), and write
\[
 \widehat\nabla\Omega_1=a\otimes\Omega_2-c\otimes\Omega_3,
 \quad\widehat\nabla\Omega_2=-a\otimes\Omega_1+b\otimes\Omega_3.
\]
The eigenvalues of \(FW\) are \(1,\rho,-1-\rho\). The first row of
its divergence equation, since the first eigenvalue is constant, gives
\[
 (1-\rho)\iota_{a^\sharp}\Omega_3
       +(2+\rho)\iota_{c^\sharp}\Omega_2=0.                  \tag{10}
\]
In a compatible orthonormal coframe this says
\(c=k(-a_2,a_1,-a_4,a_3)\). Consequently,
\[
\begin{split}
 |d\Omega|^2&=(1-k)^2|a|^2,\\
 |\widehat\nabla\Omega|^2&=2(1+k^2)|a|^2,\\
 W(\widehat\nabla_e\Omega,\widehat\nabla^e\Omega)
       &=2\alpha[\rho-(1+\rho)k^2]|a|^2.
\end{split}                                                   \tag{11}
\]
These formulas only use the signed normalized eigenvalues and (10).
In particular they do not require \(\alpha>0\).

Contract (8) with \(\Omega\otimes\Omega\), use
\(FW(\Omega)=\Omega\), \(|\Omega|^2=2\), and
\(\Delta_H\Omega=\widehat\nabla^*\widehat\nabla\Omega
-2W\Omega+\widehat s\Omega/3\). This gives
\[
\begin{split}
0={}&\tfrac12|\widehat\nabla\Omega|^2
-\tfrac2\alpha W(\widehat\nabla_e\Omega,
                         \widehat\nabla^e\Omega)\\
&+\tfrac32\langle\Omega,\Delta_H\Omega\rangle
+2\left(\frac{2|W|^2}{\alpha}-3\alpha\right).
\end{split}                                                   \tag{12}
\]
On a closed four-manifold, self-duality gives
\(\int\langle\Omega,\Delta_H\Omega\rangle=2\int|d\Omega|^2\).
Also \(|W|^2=2\alpha^2(1+\rho+\rho^2)\). Equations (11)--(12)
therefore give
\[
 \int_{\widehat g}\left[
 \frac{3(1-\rho)(2+\rho)}{2\rho^2+2\rho+5}
           |\widehat\nabla\Omega|^2
       +8\alpha(\rho+\tfrac12)^2\right]=0.                 \tag{13}
\]
The first coefficient equals \(\tfrac32(1-z^2)/(1+z^2)\).
The second term is negative, since \(\alpha=-4u/3\).
Using \(d\mu_{\widehat g}=u^4d\mu_g\), (13) is exactly (3).
Taking the ratio of the first two identities in (11) gives (4).

The calculations extend across the collision set \(\lambda_2=\lambda_3\)
by continuity: the lowest eigenline is smooth, and \(z^2\), all
coefficients in (3)--(4), and both energy densities are smooth there.
No differentiation of the possibly nonsmooth ordered splitting \(h\)
is used.

## 3. Scalar restoration with no upper amplitude bound

Write \(e=s+4\). Since the model
\[
 A=t(2I/3-\omega\otimes\omega)
\]
has the exact lowest eigenvalue and eigenline of \(W^+\), the residual
\(R=W^+-A\) satisfies \(R\omega=0\) and \(|R|^2=h^2/2\).
The conformal scalar and Weyl formulas are
\[
 \widehat s=u^{-3}(6\Delta u+su),\qquad
 \langle\widehat W^+\Omega,\Omega\rangle=-\tfrac83u,
\]
where \(\Delta=d^*d\ge0\). Testing the self-dual form Weitzenböck
formula against \(f\Omega\), with \(f=(u-u_0)/u\), gives
\[
\begin{split}
6\int|du|^2+8\int V(u)+\int e\,u(u-u_0)
={}&\int f u^2(3|P|^2-\tfrac32|Q|^2)\\
&+3u_0\int\langle du\wedge\omega,P\rangle,\qquad
 V(u)=u(u^3-u_0^3)(u-u_0).
\end{split}                                                   \tag{14}
\]
This is the arbitrary constant-norm form identity used in the previous
variable-amplitude proof; closedness or integrability is not imposed.

Here \(V(u)\ge m^{1/3}u_0^2(u-u_0)^2\). By (3) and (5),
\[
 \int u^2|Q|^2\le
       \frac{1+\theta^2}{1-\theta^2}\,m^{-1/3}\int h^2,
 \qquad
 \int |Q|^2\le
       \frac{1+\theta^2}{1-\theta^2}\,m^{-1}\int h^2.
\tag{15}
\]
Since \(|f|\le 1+u_0m^{-1/3}\) and \(|P|^2\le|Q|^2\), the first
term on the right of (14) is bounded by \(C_m\int u^2|Q|^2\).
The second is at most \(3\int|du|^2+C\int|Q|^2\).
For the scalar error observe the uniform identity and bound
\[
 \frac{u^2(u-u_0)^2}{V(u)}
 =\frac{u}{u^2+uu_0+u_0^2}\le\frac1{3u_0},
\]
with its continuous interpretation at \(u=u_0\). Young's inequality
then bounds its absolute value by \(4\int V(u)+C\int e^2\).
Absorption in (14) proves the \(du\) and \(V(u)\) parts of (6).
The conformal connection formula gives
\(|\nabla\omega|^2\le C(|Q|^2+m^{-2/3}|du|^2)\), completing (6).
If \(t\le M_0\), then
\(|dt|^2=9u^4|du|^2\) and
\((t-1/2)^2\le C_{m,M_0}V(u)\), proving (7).

## 4. What this proves about negative Einstein geometry

If \(\operatorname{Ric}=-g\), \(t\) is bounded between two positive
constants, and the upper eigenvalues approach one another in normalized
\(L^2\), (7) controls both the amplitude and the derivative of the
actual eigenform. No separate derivative estimate is needed. For example,
uniform spectral closeness to \((-2/3,1/3,1/3)\) of size \(\epsilon\)
implies all three normalized integral quantities in (7) are
\(O(\epsilon^2)\), with uniform constants for sufficiently small
\(\epsilon\).

At zero splitting and \(s=-4\), the theorem gives
\(t=1/2\) and \(\nabla\omega=0\), hence a constant-negative-scalar
Kähler metric on the double cover. It is Kähler--Einstein when
\(\operatorname{Ric}=-g\). This exact degenerate-spectrum conclusion
belongs to classical Derdziński theory; it is not claimed as a new
classification.

Small positive splitting is **not** proved to vanish. The signed balance
has two nonnegative energies on opposite sides, rather than two on the
same side of a zero identity. In particular, reversing the eigenvalue
ordering in a positive-branch rigidity theorem is not valid.
The formal reaction in the Einstein Weyl equation reinforces this
distinction. At \(W_0=\operatorname{diag}(-2/3,1/3,1/3)\),
the splitting direction \(B=\operatorname{diag}(0,b,-b)\) has
\[
 D\left[-2W-6W^2+2|W|^2I\right]_{W_0}(B)=-6B.
\]
Thus the zero-order linearization does not give a positive-mass
absorption argument for the splitting. This is a check on that proposed
proof, not a counterexample to a possible uniform exact rigidity theorem.
Neither this note nor the inspected sources decide whether every
sufficiently small two-sided spectral neighborhood is exactly Kähler.

## 5. Sources, scope, and verification

The signed algebra adapts Catino--Dameno's first-order method; the scalar
restoring test is the prior variable-amplitude argument. Their positive
largest-eigenvalue theorem does not cover this negative-lowest branch.
Kim's condition \(\lambda_2\le\lambda_3/4\) also excludes the negative
Kähler--Einstein model, whose upper eigenvalues coincide and are positive.
These distinctions are mathematical hypotheses, not novelty claims.

- A. Derdziński, *Self-dual Kähler manifolds and Einstein manifolds of
  dimension four*, Compositio Math. 49 (1983), 405--433, Proposition 5.
  [Primary paper](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf).
- G. Catino and D. Dameno, *Conformal Kähler Rigidity of Einstein
  Four-Manifolds*, arXiv:2607.21538v1, Sections 2--3.
  [Primary manuscript](https://arxiv.org/html/2607.21538v1).
- I. Kim, *Pinched self-dual Weyl curvature on Einstein four-manifolds*,
  arXiv:2512.00825v1, Theorem 7.
  [Primary manuscript](https://arxiv.org/html/2512.00825v1).
- [Prior variable-amplitude scalar test](line1_variable_negative_selection.md),
  Sections 2--3; its \(H_2\)-dependent weak-Bianchi estimate is replaced
  here by (3), not silently assumed.

`check_line1_signed_harmonic_weyl.py` checks the signed normalization,
spectral coefficients, conformal powers, scalar restoring algebra, and
reaction linearization by exact symbolic arithmetic. It also rejects
three deliberate sign or normalization errors. These finite checks
support the displayed identities; the global theorem relies on the
written differential and integration argument above.



---

## 原稿 5: line1_einstein_spectral_application.md

来源：`mathematics/current/line1_einstein_spectral_application.md`；范围：`full`。

原文件 SHA-256：`b721c3d42690215ca512954fbec57cc14d4d9b503053c1e1bb67222f4953199c`。

# Einstein spectral pinching: automatic amplitude and a monopole consequence

23 September 2026. Conventions: nonnegative scalar Laplacian,
Hilbert--Schmidt norm on the Weyl endomorphism, and exterior norm on forms.
This note supplies two applications of the harmonic-Weyl selection theorem.
The maximum-principle calculation is elementary; no independent priority is
claimed for that calculation. The quantitative topological consequence uses
the accompanying selection estimate, with its complete hypotheses.

## 1. An upper amplitude supplied by the equation

Let \((M,g)\) be a closed oriented Einstein four-manifold with
\(\operatorname{Ric}=-g\). Write the ordered eigenvalues of \(W^+\) as
\(\lambda_1<\lambda_2\le\lambda_3\), and put
\[
 t=-\frac34\lambda_1>0,\qquad b=\lambda_3-\lambda_2,\qquad
 \theta=\frac{b}{4t}.
\tag{1}
\]
The lowest eigenvalue is assumed simple everywhere. The function \(t\)
is smooth, while \(b\) need only be continuous at an upper-eigenvalue
collision. Its square is smooth. Trace-freeness gives
\[
 (\lambda_1,\lambda_2,\lambda_3)
 =\left(-\frac{4t}{3},\frac{2t}{3}-\frac b2,
                         \frac{2t}{3}+\frac b2\right),
 \quad |W^+|^2=\frac83t^2+\frac12b^2.
\tag{2}
\]
In particular, simplicity of the lowest eigenvalue is equivalent to
\(\theta<1\).

**Lemma 1.** If \(\theta\le\theta_0<1/\sqrt3\), then
\[
 \boxed{t\le M_{\theta_0}:=\frac{1}{2(1-3\theta_0^2)}.}
\tag{3}
\]
There is no separate upper Weyl-curvature hypothesis.

To prove this, use the Einstein Weyl equation
\[
 \nabla^*\nabla W^+=2W^++6(W^+)^2-2|W^+|^2I.
\tag{4}
\]
For a smooth simple eigenvalue of a self-adjoint bundle section, the
second derivative formula, with the nonnegative Laplacian convention, is
\[
 \Delta\lambda_1
 =\langle(\nabla^*\nabla W^+)e_1,e_1\rangle
 -2\sum_{j=2}^3\frac{|\langle\nabla W^+e_1,e_j\rangle|^2}
                          {\lambda_1-\lambda_j}.
\tag{5}
\]
An orthonormal eigenbasis at the point suffices; the two upper eigenvalues
need not be locally simple. Since each denominator is negative, (2)--(5)
imply
\[
 \Delta t\le 2t-4t^2+\frac34b^2
            \le2t-4(1-3\theta_0^2)t^2.
\tag{6}
\]
At a maximum of \(t\), one has \(\Delta t\ge0\). Equation (3) follows.
The conclusion is only an upper bound: this argument does not provide a
uniform positive lower bound for \(t\) over a family of manifolds.

## 2. A derivative-free structure estimate

Assume in addition \(t\ge m>0\), with a prescribed lower bound.
Let \(\omega\) be the normalized lowest eigenform, \(|\omega|^2=2\),
on the orientation cover of its real eigenline. The cover has degree at
most two. Normalized integrals are unchanged under this cover. The
[harmonic-Weyl selection theorem](line1_signed_harmonic_weyl.md),
applied using (3), gives
\[
 \boxed{\fint\left(|dt|^2+(t-\tfrac12)^2+|\nabla\omega|^2\right)
       \le C_{m,\theta_0}\fint b^2.}
\tag{7}
\]
Here the Einstein equation supplies harmonicity of \(W^+\) and \(s=-4\).
No assumed Hessian budget, Ricci derivative estimate, Sobolev constant,
injectivity radius, scalar spectral gap, diameter, or \(W^-\) bound is
present. The lower amplitude and relative spectral pinching are genuine
assumptions. This is an integral structure estimate, not a theorem
constructing a nearby Kähler metric.

## 3. Topology forces a definite upper-eigenvalue splitting

Suppose that the given metric admits an actual polarized monopole class
with \(p=(a_g^+)^2\ge A>0\). This can be the metricwise class on the
blow-up/handle families of the main integral theorem; no globally fixed
class working for all polarizations is being presumed. Put
\[
 T=2\chi(M)+3\tau(M),\qquad h=1-T/A,
 \quad 0<h<1.
\tag{8}
\]

**Corollary 2.** Under the hypotheses of Section 2 and (8),
\[
 \boxed{\fint_M(\lambda_3-\lambda_2)^2\ge c_{m,\theta_0}h^2.}
\tag{9}
\]
It applies to every normalized negative Einstein metric meeting these
spectral assumptions, not merely to a selected construction.

Indeed, the scalar monopole estimate and \(s=-4\) give
\[
 16V\ge32\pi^2p\ge32\pi^2A.
\tag{10}
\]
For an Einstein metric, Chern--Weil gives
\[
 2\pi^2T/V=\frac13+\fint|W^+|^2.
\tag{11}
\]
Since \(T=A(1-h)>0\), (10)--(11) imply
\[
 \fint|W^+|^2\le\frac23-h.
\tag{12}
\]
Combining (2) and (12), and discarding only nonpositive terms, yields
\[
 h\le\frac83\left(\frac14-\fint t^2\right)-\frac12\fint b^2
   \le\frac83(M_{\theta_0}+\tfrac12)
                  \left(\fint(t-\tfrac12)^2\right)^{1/2}.
\tag{13}
\]
Use (7) and square this inequality. This proves (9), with, for example,
\(c_{m,\theta_0}=[\frac83(M_{\theta_0}+\frac12)]^{-2}
C_{m,\theta_0}^{-1}\), where the latter constant is the one in (7).

On
\(M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)\),
\(A=c_1^2(X)>0\), the parameter is \(h=(k+4\ell)/A\).
Thus the inequality detects a required spectral departure from the
negative Kähler--Einstein curvature pattern on this actual family.
It does not exclude metrics with a lowest-eigenvalue collision, very
small lower amplitude, or failure of the displayed pinching. Consequently
this corollary alone is not an unconditional Einstein nonexistence result.
The separate two-chirality theorem supplies the new unconditional
topological application in this research package.

## 4. Sources and what is being added

The Einstein Weyl equation is classical; see Derdziński,
[Self-dual Kähler manifolds and Einstein manifolds of dimension four](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf),
and the formulas recalled in Catino--Dameno,
[Conformal Kähler rigidity of Einstein four-manifolds](https://arxiv.org/abs/2607.21538).
The latter paper's largest-simple-eigenvalue classification must not be
replaced by a lowest-simple-eigenvalue classification: the negative
Kähler--Einstein model has a simple lowest eigenvalue and a double largest
one. The accompanying harmonic-Weyl proof derives the signed balance for
this different branch.

The scalar monopole estimate is the classical input of
[LeBrun, Ricci curvature, minimal volumes, and Seiberg--Witten theory](https://arxiv.org/abs/math/0003068).
Equations (10)--(12) are classical consequences. The present quantitative
application is their composition with (7); it is not a new proof of the
classical inequalities or a complete spectral classification of Einstein
four-manifolds.



---

## 原稿 6: line1_aspherical_no_bubbles.md

来源：`mathematics/current/line1_aspherical_no_bubbles.md`；范围：`full`。

原文件 SHA-256：`f22817a8bac196b7fb95245406716b59849b7657850b6eaa65590781e3975615`。

# Asphericity excludes half-flat ALE bubbles

23 September 2026. This note strengthens the
[bounded-geometry result](line1_allowed_branch_escape.md): for the actual aspherical shear
manifolds, the assumed bound on the opposite Weyl curvature can be
removed. Spin is not required. The key point is a compact-core embedding
obstruction which treats both negative-definite ALE cores and the
non-simply-connected rational-ball cores.

## 1. A topological obstruction to ALE cores

**Lemma 1.** Let \(M\) be a closed aspherical smooth oriented
four-manifold. No sufficiently large compact core of a nonflat smooth
Ricci-flat anti-self-dual ALE four-manifold \(X\) embeds smoothly in
\(M\).

The orientation on an ALE core is the one for which \(W^+=0\).
Reversing the orientation of an embedding does not change the
non-embedding conclusion.

**Proof.** Take a large compact core \(B\subset X\) with connected
boundary \(Y=S^3/\Gamma\) and cylindrical complement. Thus \(B\) has
the homotopy type of \(X\). Its fundamental group is finite. Since
\(M\) is a closed aspherical manifold, \(\pi_1(M)\) is torsion-free
and its universal cover \(\widetilde M\) is contractible. If
\(i:B\hookrightarrow M\) were an embedding, then \(i_*\pi_1(B)\)
would be trivial. The covering-space lifting criterion therefore lifts
\(i\) to an embedding \(\widetilde i:B\hookrightarrow\widetilde M\).
It is the core itself that lifts: no injectivity assertion about the
fundamental group of a geometrical limit is being made. The lift is
injective because its composition with the covering projection is the
original embedding.

Wright's classification gives a negative-definite rational intersection
form on \(H_2(B;\mathbb Q)\). If \(b_2(B)>0\), choose a nonzero
rational class with negative square. Represent an integral multiple by
a compact cycle and a transverse push-off in the interior of \(B\).
Their intersection number is unchanged by the embedding. In the
contractible ambient manifold both classes are zero, so their
intersection is zero. This is a contradiction.

It remains to treat \(b_2(B)=0\). Wright's theorem, combined with
Suvaina's classification of Ricci-flat Kähler ALE surfaces, gives
\[
 \pi_1(B)\cong\mathbb Z_n,\qquad
 Y\cong L(n^2,nr-1),\qquad n\ge2,\quad (n,r)=1.            \tag{1}
\]
In particular, \(H_1(B;\mathbb Z)=\mathbb Z_n\) and
\(H_1(Y;\mathbb Z)=\mathbb Z_{n^2}\). The nonflat assumption
excludes the trivial Euclidean case \(n=1\).

Put \(C=\widetilde M\setminus\operatorname{int}B\). Use small
collar enlargements to apply ordinary Mayer--Vietoris to
\(\widetilde M=B\cup_Y C\); compactness of the ambient manifold is
not required. Since its first and second homology vanish, the exact
sequence gives an isomorphism
\[
 \mathbb Z_{n^2}=H_1(Y;\mathbb Z)
       \cong H_1(B;\mathbb Z)\oplus H_1(C;\mathbb Z)
       =\mathbb Z_n\oplus H_1(C;\mathbb Z).                 \tag{2}
\]
The second factor must have order \(n\). Therefore every element on
the right is annihilated by \(n\), while the left has an element of
order \(n^2\). This is impossible for every \(n\ge2\), composite
or prime. The two cases exhaust the smooth nonflat ASD Ricci-flat ALE
classification. This proves the lemma.

### Why a spin-only argument would fail

There are spin rational-ball ALE spaces in (1). For example, take the
three-centre Gibbons--Hawking space with centres in a regular triangle
and its free cyclic quotient of order three supplied by Wright's
construction. The covering space is hyperkähler and spin. Pull-back
on mod-two cohomology is injective for an odd-degree cover (transfer
composed with pull-back is multiplication by three), so the quotient
is also spin. It has \(b_2=0\), fundamental group \(\mathbb Z_3\)
and a lens end of order nine. Lemma 1 excludes its embedding by (2),
not by a false assertion that rational-ball bubbles are non-spin.

## 2. Half-Weyl bounds give full curvature control on aspherical types

**Theorem 2.** Fix \(v>0,D>0,\Lambda>0\) and \(\chi_0<\infty\).
There is a constant \(C(v,D,\Lambda,\chi_0)\) such that every closed
aspherical oriented Einstein four-manifold satisfying
\[
 \operatorname{Ric}=-g,\quad V\ge v,\quad
 \operatorname{diam}(g)\le D,\quad \|W^+\|_\infty\le\Lambda,
 \quad \chi(M)\le\chi_0                                    \tag{3}
\]
has \(\|\operatorname{Rm}\|_\infty\le C\).

**Proof.** Suppose a sequence violates the conclusion and set
\(Q_j=\max|\operatorname{Rm}_{g_j}|\to\infty\), attained at \(p_j\).
Rescale by \(\widehat g_j=Q_jg_j\). Then
\[
 |\operatorname{Rm}_{\widehat g_j}|\le1,\quad
 |\operatorname{Rm}_{\widehat g_j}|(p_j)=1,\quad
 \operatorname{Ric}_{\widehat g_j}=-Q_j^{-1}\widehat g_j,
 \quad |W^+_{\widehat g_j}|\le\Lambda/Q_j.                  \tag{4}
\]
Relative Bishop comparison, using \(V\ge v\) and diameter \(D\),
gives \(\operatorname{Vol}_{g_j}B_r(x)\ge c(v,D)r^4\) for
\(0<r\le D\). After rescaling this holds on every fixed finite
radius for all sufficiently large \(j\). The curvature bound in (4)
and this noncollapse give injectivity-radius control and smooth pointed
Einstein compactness. The limit \((X,g_\infty,p)\) is complete,
Ricci-flat, anti-self-dual, has Euclidean lower volume growth, and is
nonflat because \(|\operatorname{Rm}|(p)=1\).

Einstein Chern--Gauss--Bonnet and \(\chi\le\chi_0\) give a uniform
full \(L^2\) curvature bound, unchanged by rescaling. The limit
therefore has finite curvature energy. The classical
Bando--Kasue--Nakajima asymptotic theorem makes it an ALE space.
Equivalently this is the smooth deepest-bubble case of Einstein
compactness. Choosing a global curvature maximum ensured a smooth
limit; an unproved classification of intermediate orbifold bubbles is
not needed.

Smooth pointed convergence embeds every fixed compact subset of \(X\)
into \(M_j\) for sufficiently large \(j\). Choose a large ALE core.
Lemma 1 forbids precisely this embedding. This contradiction proves
the theorem. No spin, simply-connected-bubble or global complex-gluing
assumption has entered the proof.

## 3. A diameter-only spectral gap on the actual shear family

Let \(M=M(q,g;u,f)\) be the self-gluing of
\(F_{q,2}\times\Sigma_g\), with \(q\ge1\), \(g\ge2\), under
\[
 (\phi,x)\longmapsto(-\phi+u(x),f(x)),
 \qquad f\in\operatorname{Diff}^+(\Sigma_g),\qquad
 0\ne[u]\in H^1(\Sigma_g;\mathbb Z).
\]
These are the explicit self-gluings covered by the complete virtual
Kähler and actual monopole arguments of Rounds 11--12; no arbitrary
multi-block assembly is included by implication. No order condition on
the mapping class of \(f\) is imposed. The inherited results give:

- \(M\) is aspherical and \(\tau(M)=0\);
- no finite cover is Kähler;
- \(\pi_1(M)\) contains \(\mathbb Z^2\);
- \(\chi(M)=4q(g-1)\), and an actual monopole class has square
  \(A=2\chi(M)>0\).

As before, write
\[
 t=-3\lambda_1(W^+)/4,\quad b=\lambda_3(W^+)-\lambda_2(W^+),
 \quad\mathscr S(g)=\fint b^2.
\]

**Theorem 3.** For every \(D>0\) and \(0\le\theta<1/\sqrt3\)
there is \(\varepsilon(D,\theta)>0\) such that every normalized
negative Einstein metric on any member of this actual shear family
with
\[
                  b\le4\theta t,
                  \qquad\operatorname{diam}(g)\le D         \tag{5}
\]
satisfies \(\mathscr S(g)\ge\varepsilon(D,\theta)\).
Zeros of \(W^+\) are allowed. There is no lower amplitude, opposite
Weyl, full-curvature, injectivity-radius or separately assumed
noncollapse bound.

**Proof.** The previously established maximum principle, applied at a
positive maximum of \(t\), gives
\(t\le[2(1-3\theta^2)]^{-1}\) and hence a uniform bound on
\(W^+\). At such a maximum the lowest eigenvalue is simple since
\(\lambda_2-\lambda_1\ge2(1-\theta)t>0\). The case \(t\equiv0\)
needs no maximum argument.

The actual monopole scalar inequality gives
\[
                       V\ge4\pi^2\chi(M).                  \tag{6}
\]
In this family \(\chi(M)\ge4\), so \(V\ge16\pi^2\).
Bishop comparison gives a diameter-dependent upper volume bound.
Consequently (6) also bounds \(\chi(M)\) in terms of \(D\).
All constants in Theorem 2 are thus controlled by \(D,\theta\),
uniformly across the family. Full curvature is bounded, and the
geometric compactness used in the preceding note follows.

If splitting energies tended to zero, the smooth limit would be exact
negative Einstein with at most two self-dual Weyl eigenvalues.
Derdziński's classification gives a KE metric on a cover of degree
at most two, or an ASD metric. The first contradicts the inherited
virtual Kähler obstruction. The second, together with the preserved
signature zero, has \(W^-=0\), so is real hyperbolic; Preissmann's
theorem excludes its \(\mathbb Z^2\) subgroup. This proves the
uniform gap.

**Corollary 4.** Every exact Einstein sequence on these manifolds with
fixed \(\theta<1/\sqrt3\) and \(\mathscr S(g_j)\to0\) satisfies
\[
                          \operatorname{diam}(g_j)\to\infty.
\]
This replaces the former alternative "diameter escape or opposite-Weyl
blow-up" by diameter escape alone, in this actual aspherical family.
It still permits arbitrary exact Einstein metrics outside the relative
pinching class, or with a splitting bounded away from zero, and it does
not establish their nonexistence.

## 4. Sources and precise status

1. Wright, *Quotients of gravitational instantons*, Theorem A,
   Remark 3 and Corollary C:
   <https://arxiv.org/pdf/1102.2442>.
2. Suvaina, *ALE Ricci-flat Kähler metrics and deformations of quotient
   surface singularities*, Theorem B, Theorem 2.2, Proposition 3.3 and
   its classification proof: <https://arxiv.org/pdf/1102.2672>.
   These give the cyclic fundamental group and the lens boundary in
   (1), not merely the existence of one chosen rational ball.
3. Bando--Kasue--Nakajima, *On a construction of coordinates at
   infinity on manifolds with fast curvature decay and maximal volume
   growth*, Invent. Math. 97 (1989), 313--349:
   <https://doi.org/10.1007/BF01389045>.
4. Derdziński, Proposition 5 and Theorem 2:
   <https://www.numdam.org/article/CM_1983__49_3_405_0.pdf>.
5. Actual objects: `round11_graph_topology.md`, `round11_kahler.md`,
   `round12_global.md`; spectral calculation and initial escape proof:
   `line1_einstein_spectral_application.md`,
   `line1_allowed_branch_escape.md`.

The classification and compactness inputs are classical. The compact-core
exclusion is proved explicitly above, including the rational-ball case
that a sphere-only or spin-only argument misses. No exhaustive
publication-priority assertion is made. The result removes an actual
curvature assumption from the preceding all-output spectral application;
it does not claim to solve the unrestricted negative Einstein problem.



---

## 原稿 7: line1_allowed_branch_escape.md

来源：`mathematics/current/line1_allowed_branch_escape.md`；范围：`full`。

原文件 SHA-256：`d239581d278a9cce6d668fa3f7ecd0dab9fd004ad0a0825572bbeedbc3850107`。

# Exact negative-Einstein spectral degeneration on non-virtually-Kähler manifolds

23 September 2026. This note proves a global escape alternative for the
allowed branch. It does not assert that small Weyl splitting always vanishes.
The main argument combines the previously proved signed harmonic-Weyl estimate
with classical smooth Einstein compactness and an actual smooth-topological
obstruction. Its scope is all exact outputs satisfying the stated geometric
bounds, not a neighbourhood of a selected approximate construction.

**Strengthening for the actual aspherical family.** The subsequent
[aspherical no-bubble theorem](line1_aspherical_no_bubbles.md) removes
the opposite-Weyl bound from the self-gluing application below. In that
family, vanishing splitting forces diameter escape alone. Theorem 1
and the general degeneration discussion remain useful for other
non-virtually-Kähler types where asphericity is not available.

## 1. Hypotheses and the new conclusion

Let \(M\) be a closed connected oriented smooth four-manifold for which no
connected cover of degree at most two admits a Kähler structure compatible
with the lifted orientation. Suppose there is \(A>0\) such that each metric
under consideration has an actual polarized monopole class \(a_g\) with
\((a_g^+)^2\ge A\). The class may depend on the metric. The scalar monopole
estimate, not an assumption about a formal cohomology vector, is required.

Consider exact metrics \(\operatorname{Ric}_g=-g\). Order the eigenvalues of
\(W_g^+\) and set
\[
 \lambda_1<\lambda_2\le\lambda_3,\qquad
 t=-\frac34\lambda_1,\quad b=\lambda_3-\lambda_2,\quad
 z=\frac b{4t}.
\]
Fix \(m>0\) and \(0\le\theta<1/\sqrt3\), and impose
\[
                 t\ge m,\qquad z\le\theta.                 \tag{1}
\]
Define the normalized splitting energy
\[
                      \mathscr S(g)=\fint_M b^2.
\]

**Theorem 1 (global bounded-geometry splitting gap).** For every \(D,K>0\)
there is \(\varepsilon=\varepsilon(A,m,\theta,D,K)>0\) such that every metric
above satisfying
\[
              \operatorname{diam}(M,g)\le D,
              \qquad \|W_g^-\|_\infty\le K                 \tag{2}
\]
satisfies
\[
                         \mathscr S(g)\ge\varepsilon.       \tag{3}
\]
The constant can be chosen uniformly over all smooth types satisfying the
same hypotheses and the same positive budget \(A\). No independent volume,
injectivity-radius, full-curvature or Sobolev hypothesis is needed.

**Corollary 2 (escape alternative).** On a fixed such \(M\), if exact
negative-Einstein metrics satisfy (1) and \(\mathscr S(g_j)\to0\), then
\[
       \operatorname{diam}(M,g_j)+\|W^-_{g_j}\|_\infty
                         \longrightarrow\infty.            \tag{4}
\]
More precisely, every fixed bounded rectangle in these two quantities
contains only metrics with a positive lower splitting energy. It is not
claimed that each summand in (4) tends to infinity separately.

This conclusion changes a global decision at the canonical shear ratio
\(T/A=1\): the earlier monopole splitting bound proportional to
\((1-T/A)^2\) vanishes there, while (3) is strictly positive under (2).
It does not exclude arbitrary outputs escaping (2).

## 2. Derivation of the geometric compactness, with no redundant inputs

Since \(s=-4\), the actual scalar monopole inequality gives
\[
 16\operatorname{Vol}(g)=\int_M s^2
       \ge32\pi^2(a_g^+)^2\ge32\pi^2A,
 \qquad \operatorname{Vol}(g)\ge2\pi^2A.                    \tag{5}
\]
The maximum-principle result in
[the Einstein spectral application](line1_einstein_spectral_application.md)
gives
\[
        t\le M_\theta=\frac1{2(1-3\theta^2)}.              \tag{6}
\]
Moreover,
\[
 |W^+|^2=\frac83t^2+\frac12b^2
       \le\left(\frac83+8\theta^2\right)M_\theta^2.        \tag{7}
\]
Consequently the bound on \(W^-\), together with the Einstein equation,
gives a full sectional-curvature bound depending only on \(\theta,K\).

With \(\operatorname{Ric}=-g\), Bishop comparison and the diameter bound
also give an upper volume bound depending only on \(D\). In addition,
relative Bishop comparison and (5) give a uniform lower bound for the
volume of every ball of any fixed positive radius at most \(D\).
The sectional bound and these bounds imply the standard uniform
injectivity-radius estimate. Thus every sequence satisfying (1)--(2)
has, after a subsequence and pull-back by orientation-preserving
diffeomorphisms, a smooth Einstein limit on a closed smooth manifold.
Here smoothness follows by elliptic bootstrapping of the exact Einstein
equation after Cheeger--Gromov compactness. This is classical compactness,
not a new regularity theorem.

## 3. Proof of the splitting gap

If (3) failed, take a sequence with \(\mathscr S(g_j)\to0\) and use the
preceding smooth compactness. The ordered Weyl eigenvalues converge
uniformly. In the limit, \(b_\infty=0\) everywhere and
\(t_\infty\ge m\). Thus the lowest Weyl eigenline remains smooth and
separated from its two-dimensional complement.

One can already finish with the exact Derdziński theorem. Equivalently,
the proved [signed harmonic-Weyl estimate](line1_signed_harmonic_weyl.md)
gives, for the normalized lowest eigenform on its orientation cover,
\[
 \fint\left(|dt_j|^2+(t_j-\tfrac12)^2+|\nabla\omega_j|^2\right)
                        \le C_{m,\theta}\mathscr S(g_j).    \tag{8}
\]
The line bundles converge under the diffeomorphisms: the uniform spectral
gap makes their spectral projections smoothly convergent, and sufficiently
close real line bundles are isomorphic. Their orientation covers are
therefore identified with the limit orientation cover. This is a cover of
degree at most two, not an assumed global choice of eigenform on \(M\).

Passing to the smooth limit in (8) gives
\(t_\infty=1/2\) and a parallel self-dual form
\(|\omega_\infty|^2=2\). The corresponding orthogonal almost complex
structure is parallel, hence integrable and Kähler. The lifted metric is
negative Kähler--Einstein. Since smooth convergence preserves the
diffeomorphism type, this contradicts the topological hypothesis for
every sufficiently late manifold of the sequence. This also proves the
claimed uniformity across smooth types. Corollary 2 is its contrapositive.

## 4. Actual application and removal of the lower amplitude assumption

For the self-gluings
\[
 M=M(q,g;u,f),\qquad
 (\phi,x)\longmapsto(-\phi+u(x),f(x)),\quad [u]\ne0,
 \quad q\ge1,\quad g\ge2,\quad f\in\operatorname{Diff}^+(\Sigma_g),
\]
the inherited [virtual Kähler theorem](round11_kahler.md) excludes all
finite Kähler covers. The [canonical-class calculation](round12_global.md)
supplies an actual canonical monopole class \(a\) with
\[
 a^2=2\chi(M)>0,\qquad (a_g^+)^2\ge a^2.
\]
Thus Theorem 1 applies with \(A=2\chi(M)\), to every negative Einstein
metric in its stated spectral class, independently of the original gluing
coordinates or of its position in the Einstein moduli space.

For these objects \(\tau=0\) and \(T=A\). Hence the previously proved
topological splitting estimate involving \((1-T/A)^2\) is zero. The
present positive bound instead uses the obstruction to a degree-two
Kähler cover. It is therefore not an algebraic restatement of that earlier
estimate. No assertion is made that this compactness corollary is new in
the published literature.

The known almost-Einstein sequences on these manifolds do not contradict
the theorem: they are not exact Einstein and their long thin geometry
leaves the compact regime. The result still permits a non-Kähler exact
Einstein metric of appreciable Weyl splitting.

In fact this actual family allows removal of the lower amplitude bound.
This strengthening uses both its signature and its fundamental group,
not an assumption that the selected eigenline cannot disappear.

**Theorem 3 (shear-family gap without lower Weyl amplitude).** Fix
\(A_0>0\), \(D,K>0\), and \(0\le\theta<1/\sqrt3\). For every member of
the shear family with \(2\chi(M)\ge A_0\), every exact
\(\operatorname{Ric}_g=-g\) metric satisfying
\[
 b\le4\theta t,\qquad \operatorname{diam}(g)\le D,
 \qquad\|W^-\|_\infty\le K
\]
has \(\mathscr S(g)\ge\varepsilon(A_0,\theta,D,K)>0\).
Here ordered eigenvalues define \(t,b\) everywhere, and \(W^+=0\)
is allowed. There is no prescribed \(m>0\). In particular, any exact
sequence in this relative pinching class with vanishing splitting energy
must satisfy the diameter/opposite-Weyl escape conclusion (4).
The later [Theorem 3](line1_aspherical_no_bubbles.md) strengthens this
to \(\operatorname{diam}(g_j)\to\infty\), with a uniform splitting
gap depending only on \(D,\theta\), and without assuming \(K\).

**Proof.** At any positive maximum of \(t\), the lowest eigenvalue is
simple because \(\lambda_2-\lambda_1=2t-b/2\ge2(1-\theta)t>0\).
The previous maximum-principle calculation therefore proves (6) even
when \(W^+\) has zeros. If \(t\equiv0\), (6) is immediate. Thus all
the compactness conclusions of Section 2 remain available, uniformly
using \(A_0\) in (5).

If a gap failed, the smooth limit would be a compact negative Einstein
metric with \(\lambda_2=\lambda_3\) everywhere. Derdziński's Proposition
5(iv) and Theorem 2 give two relevant alternatives: \(W^+\equiv0\), or
a Kähler--Einstein metric on a cover of degree at most two. The possible
non-Kähler conformally Kähler case of that classical classification has
a nonzero Killing field; a compact negative Einstein metric has none by
the integrated Bochner formula. Thus it does not provide another case
here. The KE alternative contradicts the virtual Kähler obstruction.

In the ASD alternative, the inherited signature \(\tau(M)=0\) and the
signature formula give \(\int|W^-|^2=0\). Both Weyl halves vanish,
so the limit has constant sectional curvature \(-1/3\). But the
injected vertex group \(\pi_1(F_{q,2})\times\pi_1(\Sigma_g)\)
contains \(\mathbb Z^2\). This contradicts Preissmann's theorem for
closed strictly negatively curved manifolds. Both alternatives are
excluded on every smooth type in the limiting subsequence. This proves
the theorem. In particular the argument controls the possible vanishing
of the lowest Weyl amplitude instead of hiding it in a nondegeneracy
hypothesis.

Under the original lower-amplitude hypothesis, the spectral assumptions
themselves also force the endpoint
volume if the splitting tends to zero; endpoint volume is not a premise
of Theorem 1. Einstein Chern--Weil gives
\[
 \frac{2\pi^2T}{V}=\frac13+\fint|W^+|^2
     =1+\frac83\fint(t^2-\tfrac14)+\frac12\mathscr S.
                                                               \tag{10}
\]
By (6) and (8), the last two terms are bounded in absolute value by
\(C\sqrt{\mathscr S}+\mathscr S/2\). When \(T=A\), (5) also gives
\(V\ge2\pi^2T\). Consequently, for sufficiently small splitting,
\[
 0\le\frac{V}{2\pi^2T}-1\le C_{m,\theta}\sqrt{\mathscr S}.
                                                               \tag{11}
\]
Thus the hypotheses cover the full volume window before showing that a
vanishing-splitting sequence must approach its lower end. They do not
exclude candidates whose splitting is bounded away from zero.

## 5. Opposite-Weyl degeneration without the aspherical input

There is a more precise necessary degeneration picture in the general
fixed-topology, bounded-diameter case. This is no longer a remaining
possibility for the aspherical self-gluings: the
[compact-core obstruction](line1_aspherical_no_bubbles.md) excludes
their bubbles directly, without proving compatibility of complex
fillings. Suppose \(g_j\) are exact Einstein,
satisfy (1), \(\mathscr S(g_j)\to0\), and have bounded diameter, but no
uniform \(W^-\) bound.

The volume lower bound is still (5). The four-dimensional Einstein
Chern--Gauss--Bonnet identity gives
\[
 8\pi^2\chi(M)=\int_M\left(|W^+|^2+|W^-|^2+\frac23\right),
 \qquad \operatorname{Vol}(g_j)\le12\pi^2\chi(M).           \tag{9}
\]
Thus the full curvature energy is bounded and relative Bishop comparison
gives noncollapse. Classical Einstein orbifold compactness supplies an
Einstein orbifold limit with smooth convergence off finitely many points,
together with the usual ALE rescaling analysis at concentrations.

Because (9) bounds total volume, the unnormalized splitting integral also
tends to zero. On the regular part of the limit, (8) gives
\[
 t_\infty=\tfrac12,\qquad \nabla\omega_\infty=0.
\]
The lowest eigenline extends as an orbifold eigenline since its eigenvalue
stays simple and nonzero. Its orientation orbifold cover therefore carries
the induced negative Kähler--Einstein orbifold metric.

At a curvature blow-up scale \(\rho_j\to0\), the rescaled metrics are
\(\rho_j^{-2}g_j\). Their Ricci constant tends to zero, while (7) gives
\[
       \|W^+_{\rho_j^{-2}g_j}\|_\infty
                     \le C_\theta\rho_j^2\longrightarrow0.
\]
Consequently any smooth nonflat ALE bubble obtained in this process is
Ricci-flat and anti-self-dual in the original orientation. Wright's
classification shows that such smooth bubbles are hyperkähler or suitable
cyclic quotients of Gibbons--Hawking spaces, and are Kähler.

This is **not** a proof that the original \(M\) is Kähler. A Kähler
orbifold and Kähler ALE pieces do not by themselves provide compatible
complex structures across the actual marked necks, a global complex
smoothing, or the original smooth type. Intermediate bubble-tree objects
can themselves be orbifolds. No assertion that all bubbles are simply
connected, nor that a global complex smoothing is unobstructed, is used.
Thus, in the absence of an additional topological argument,
opposite-chirality concentration remains a genuine mechanism; it is not
silently removed by the word "resolution". On the actual aspherical
self-gluings, the later compact-core argument supplies precisely such
an additional argument and rules it out.

The lower amplitude hypothesis is used in this specific KE-orbifold
description. Without that hypothesis, an orbifold limit in a general
family can instead have \(W^+\equiv0\).
One may not transfer \(\tau(M)=0\) directly to its orbifold signature
and repeat the smooth-limit hyperbolicity argument: bubble and boundary
correction terms intervene. The smooth gap of Theorem 3 is unaffected.

## 6. Why the universal small-splitting vanishing theorem remains open here

The signed identity in the preceding work equates positive connection
energy to positive splitting energy. It does not force either to vanish.
At the negative KE curvature model the splitting reaction has coefficient
\(-6\), so there is no immediate positive-mass absorption proof.

Near a fixed negative KE metric, Dai--Wang--Wei, Theorem 3.6, prove that
nearby Einstein metrics remain KE when all infinitesimal complex
deformations are integrable. This is a genuine sufficient geometric
condition, not an invertibility assumption. It does not give a uniform
statement over degenerating moduli or over obstructed complex structures.
Nagy's 2026 second- and third-order deformation results are finite-order
results; they cannot be substituted for all-order local integrability.

The present theorem avoids that unresolved local issue by using actual
non-virtual-Kähler topology. It excludes smooth compact limits on those
objects regardless of the deformation theory of any hypothetical KE
limit. Diameter escape is not removed by either this note or its
aspherical strengthening. The marked ALE compatibility problem is not
solved here in general; the later aspherical result bypasses it for the
actual self-gluings by proving that an ALE core cannot embed at all.

## 7. Primary sources and provenance

- A. Derdziński, *Self-dual Kähler manifolds and Einstein manifolds of
  dimension four*, Compositio Math. 49 (1983), Proposition 5 and Theorem 2:
  <https://www.numdam.org/article/CM_1983__49_3_405_0.pdf>.
- M. T. Anderson, *Orbifold compactness for spaces of Riemannian metrics
  and applications*, including the recalled Einstein compactness case:
  <https://arxiv.org/abs/math/0312111>.
- E. P. Wright, *Quotients of gravitational instantons*, Theorem A:
  <https://arxiv.org/abs/1102.2442>.
- A. Preissmann, *Quelques propriétés globales des espaces de Riemann*,
  Comment. Math. Helv. 15, 175--216, original scan:
  <https://www.e-periodica.ch/cntmng?pid=com-001%3A1942%3A15%3A%3A15>.
- X. Dai, X. Wang, G. Wei, *On the Variational Stability of Kähler-Einstein
  Metrics*, Theorem 3.6 in the inspected author manuscript:
  <https://web.math.ucsb.edu/~dai/paper/dww3.pdf>.
- P.-A. Nagy, second-order and third-order negative KE deformation results:
  <https://arxiv.org/abs/2603.09028> and
  <https://arxiv.org/abs/2606.04501>.

The application uses the complete hypotheses of the inherited shear
topology and actual monopole results. The new content of this note is
their composition with the spectral structure estimate to obtain the
global escape alternative, including the explicit zero-budget-ratio
application. It introduces neither a new compactness theorem nor a
general Einstein nonexistence result.



---

本卷结束：04_允许Weyl结构与核心控制.md
