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
