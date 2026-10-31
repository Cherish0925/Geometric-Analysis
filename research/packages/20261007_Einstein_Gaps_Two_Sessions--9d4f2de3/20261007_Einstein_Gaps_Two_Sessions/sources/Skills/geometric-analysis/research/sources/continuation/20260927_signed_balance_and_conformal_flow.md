# Signed spinor energy, conformal Ricci flow, and extremal degeneration

27 September 2026. Continuation from `754bc3a`, on the local branch
`local/yau26-signed-balance-20260927`. The preceding proof is
[Full-core cost and extremal metrics](20260927_full_core_cost_and_extremal_metrics.md).
This is a mathematical continuation, not a web-export packet. The inherited
linear small-h theorem is used, not rediscovered. All statements below retain
their own hypotheses; no general zero-end gap or balanced coefficient-four
theorem is asserted.

The main connection is now dynamic: the all-metric gap and the two energy
walls bound the lifetime of an actual geometric flow, even when the gap
itself tends to zero. A genuine ordinary-SW deformation also determines
which term cannot be removed from the signed sharpness argument. The last
sections identify the additional information supplied by stationarity and
by noncollapsed curvature blow-up.

## 1. Three static budgets force finite conformal-flow time

Let \(M\) be closed, connected and oriented. Write

\[
 V=\operatorname{Vol}(g),\quad P=\int|\operatorname{Ric}^{\circ}|^2,
 \quad R=\int|\operatorname{Ric}|^2,
 \quad S_2=\int s^2.
\]

Suppose constants \(A>0\), \(h>0\), and \(0<\mu<1\) give, for every
smooth metric on \(M\),

\[
 S_2\ge32\pi^2A,\qquad R\ge8\pi^2A(1+h),
 \qquad \mathcal E(g)\ge\mu.                         \tag{1.1}
\]

Only the corresponding bounds on scalar-minus-four metrics are needed.
In the realized balanced surgery family, the actual gauge input supplies
the first two inequalities and I40 supplies \(\mu=c_1h\), after decreasing
a fixed \(c_1\) if necessary. Put

\[
 U=\frac{3(2\chi-3\tau)}A.
\]

This uses the specified opposite orientation, not an unlabelled minimum
over orientations. It agrees with the earlier \(U\) on the balanced family
for sufficiently small \(h\).

### 1.1. The actual evolution and the basic lifetime bound

Start at any smooth metric with \(s=-4\). Use positive scalar Laplacian
\(\Delta=d^*d\) and conformal pressure \(\varpi\). Conformal Ricci flow is

\[
 \partial_tg=-2Z-2\varpi g,\qquad
 Z=\operatorname{Ric}+g=\operatorname{Ric}^{\circ},\qquad
 (3\Delta+4)\varpi=|Z|^2.                            \tag{1.2}
\]

This is the classical scalar-preserving flow, not ordinary normalized
Ricci flow. Short-time smooth existence follows from
[Lu--Qing--Zheng, Theorem 1.1](https://arxiv.org/pdf/1109.5377): the required
elliptic operator is invertible at negative scalar curvature. Their
nonpositive-Laplacian convention is converted in (1.2). The scalar
variation verifies preservation of \(s=-4\), and integration of the
pressure equation gives

\[
 \varpi\ge0,\qquad 4\int\varpi=P,
 \qquad \boxed{V'=-P.}                              \tag{1.3}
\]

The volume identity is also equation (2.3) of that paper. It is a
classical input; the following use of the project budgets is the new
connection here.

At scalar \(-4\),

\[
 R=P+4V,\qquad \mathcal E=\frac{4P}{P+4V},\qquad
 V\ge V_*:=2\pi^2A.
\]

Consequently every smooth interval of (1.2) satisfies

\[
 V'\le-\frac{4\mu}{4-\mu}V,
 \qquad
 \boxed{T_{\max}\le\frac{4-\mu}{4\mu}
                      \log\frac{V(0)}{V_*}.}        \tag{1.4}
\]

Indeed integrate the differential inequality and then use the fixed
positive lower volume bound. Here \(T_{\max}\) is the maximal classical
smooth continuation time in normalization (1.2). The conclusion neither
identifies the singularity nor assumes a curvature-only extension
criterion. In particular it does not prove nonexistence by assuming a flow
must converge: its input is an already established all-metric gap.

### 1.2. Both energy walls improve the time bound

Normalize by

\[
 y=V/V_*,\quad p=P/V_*,\quad
 \kappa=\frac{4\mu}{4-\mu},\quad b=P/(4V).
\]

Chern--Weil in the opposite orientation gives

\[
 P=\frac43V+4\int|W^-|^2-8\pi^2(2\chi-3\tau).
\]

Together with (1.1)--(1.3), this proves at every smooth time

\[
 \boxed{y\ge1,\quad y'=-p,\quad
 p\ge\Psi(y):=\max\left\{\kappa y,
                   4(1+h-y),\frac43(y-U)\right\}.}   \tag{1.5}
\]

No pointwise Ricci bound, stationarity, continuously selected monopole,
or preservation of the initial energy level is used in (1.5). The
all-metric budgets are applied afresh to each metric of the flow.

Suppose initially \(b(0)\le\bar b<1/3\). The third wall and
\(p(0)\le4\bar b\,y(0)\) imply

\[
 y(0)\le Y:=\frac U{1-3\bar b}.
\]

Thus, without any ordering assumption,

\[
                 T_{\max}\le\int_1^Y\frac{dy}{\Psi(y)}.       \tag{1.6}
\]

To see the inequality rigorously, differentiate
\(\int_1^{y(t)}\Psi(v)^{-1}dv\); its derivative is at most \(-1\).
The integral is nonnegative until the flow ceases to be smooth.

When

\[
 1\le y_L:=(1+h)(1-\mu/4)
 \le y_H:=\frac{U(4-\mu)}{4(1-\mu)}\le Y,            \tag{1.7}
\]

the maximum in (1.5) is respectively its second, first and third entry
on the three consecutive intervals. Integrating explicitly gives

\[
\boxed{\begin{split}
 T_{\max}\le{}&\frac14\log\frac{4h}{(1+h)\mu}\\
 &+\frac{4-\mu}{4\mu}
             \log\frac U{(1-\mu)(1+h)}\\
 &+\frac34\log\frac{4\bar b(1-\mu)}
                              {\mu(1-3\bar b)}.
\end{split}}                                                   \tag{1.8}
\]

These are upper bounds, not sharp lifetime claims. If (1.7) fails, use
(1.6), not the three-piece expression.

### 1.3. A uniform time bound on genuine near-minimizing metrics

On the realized balanced family,

\[
 h_j\to0,\qquad U_j=1+h_j+O(h_j^2),\qquad
 \mathcal E(g)\ge c_1h_j\quad\hbox{for every }g,       \tag{1.9}
\]

where we may choose \(0<c_1<4\). Let scalar-minus-four initial metrics
satisfy \(b_j(0)\le\bar b_j=h_j+o(h_j)\), with
\(\bar b_j\ge h_j\). Conditions (1.7) hold for large \(j\), since

\[
 y_L=1+(1-c_1/4)h+O(h^2),\quad
 y_H=1+(1+3c_1/4)h+O(h^2),\quad
 Y=1+4h+o(h).
\]

The three terms in (1.8) tend respectively to
\(\frac14\log(4/c_1)\), \(1\), and
\(\frac34\log(4/c_1)\). Therefore

\[
              \boxed{\limsup_j T_{\max,j}
                          \le1+\log\frac4{c_1}.}               \tag{1.10}
\]

The initial window is not assumed attained at the infimum. For example,

\[
 \mathcal E(g_j(0))\le\frac{4h_j}{1+h_j}+h_j^2
\]

gives \(\bar b_j=h_j+O(h_j^2)\). Such smooth scalar-minus-four metrics
exist by the inherited construction upper bound and I41's negative
Yamabe reduction. Requiring the exact upper infimum instead could give
an empty starting set when that infimum is not attained; this slack
avoids that error.

The time bound remains uniform although the all-metric defect gap tends
to zero. There is a specific reason: the two energy walls constrain the
volume to a width of order \(h\), while the linear gap forces a volume
loss rate of order \(h\). Replacing (1.9) by only a quadratic gap in the
same comparison generally gives a logarithmically divergent bound,
not (1.10).

## 2. The inherited variational obstruction gives actual flow descent

This section additionally uses an actual ordinary SW solution with
projection \(p_a\ge A\) at each metric under consideration. Retain the
preceding proof's quantities

\[
 \alpha=\mathcal E=\frac{4P}{R},\quad b=\frac P{4V},\quad
 q=\frac13-2b,\quad \theta_*=-\frac1{4-\alpha}.
\]

Hold \(\theta_*\) fixed when differentiating
\(Q_{\theta_*}=R+\theta_*S_2\). For the nonpositive tensor Laplacian,
its gradient at the scalar-minus-four metric is

\[
 \mathcal G=-\Delta Z-2\operatorname{Rm}(Z)-2bZ
                                      +\tfrac12|Z|^2g,
 \qquad \operatorname{tr}\mathcal G=0.               \tag{2.1}
\]

The trace identity makes the nonlocal conformal pressure drop out of
the first variation of \(Q_{\theta_*}\). Since
\(4+16\theta_*=-4b\), (1.3) gives the exact evolution

\[
 \boxed{P'=-2\langle\mathcal G,Z\rangle_{L^2}-\frac{P^2}V
          =-2\int|\nabla Z|^2+4\int\operatorname{Rm}(Z,Z).}     \tag{2.2}
\]

Let \(C_{ijk}=\nabla_kZ_{ij}-\nabla_jZ_{ik}\), with the full ordered
tensor norm, and
\(\xi=(w_3^++w_3^--1/3)_+\). The previously proved Cotton inequality is

\[
 qP+\tfrac12\int|C|^2
              \le\langle\mathcal G,Z\rangle+\int\xi|Z|^2.
\]

Define \(D=D_2\), \(B=\int|W^-|^2\), and
\(\mathcal H=D/18+3B\). The actual same-solution estimates give
\(\int\xi^2\le8\mathcal H/9\). Inserting them into (2.2), the
terms involving \(bP\) cancel exactly:

\[
 \boxed{P'\le
    \left[-\frac23+2\sqrt{\frac{8\mathcal H}{9P}}\|Z\|_\infty\right]P
                      -\int|C|^2.}                            \tag{2.3}
\]

Here and below \(\|Z\|_\infty\) is Hilbert--Schmidt, not operator norm.
Likewise direct differentiation of \(\alpha=4P/R\) gives

\[
 \boxed{-\frac{d}{dt}\log\alpha\ge\frac{4-\alpha}{2}
 \left[q-\sqrt{\frac{8\mathcal H}{9P}}\|Z\|_\infty
                                  +\frac{\int|C|^2}{2P}\right].} \tag{2.4}
\]

In the balanced family, at every smooth time,

\[
 \mathcal H=P+2\pi^2A(U-1-h-2(p_a/A-1)),
 \qquad \mathcal H/P\le1+O(h).                      \tag{2.5}
\]

The lower bound \(P\ge cAh\) follows from (1.1) and \(V\ge V_*\).
Together with \(p_a\ge A\) and \(U-1-h=O(h^2)\), it proves the
ratio bound in (2.5) without preserving an initial energy window or
choosing monopoles continuously in time.
Consequently an initial sequence with \(\|Z\|_\infty\to0\) has an
actual decreasing direction along (1.2), with initial relative rate
at least \(2/3-o(1)\) in (2.4). This is stronger than merely exhibiting
a nonzero abstract gradient, but does not assume the pinching persists.

For a finite-time formulation, consider a portion of the smooth flow
on which the following bounds hold:

\[
 b\le1/24,\quad \alpha\le1,\quad \mathcal H/P\le2,
 \quad\|Z\|_\infty\le1/32.
\]

While this tube and smoothness persist, (2.4) implies
\(-d\log\alpha/dt\ge1/4\). Starting in Section 1.3's window, the
energy level remains in that window while the estimate applies. Since
\(\alpha\ge c_1h\), the tube cannot persist beyond

\[
                     4\log\frac{\alpha(0)}{c_1h}.              \tag{2.6}
\]

Thus there is actual energy improvement until pointwise escape or loss
of smooth continuation: for sufficiently small \(h\), (2.5) prevents
exit through the \(\mathcal H/P\) face, while decreasing \(\alpha\)
also decreases \(b=\alpha/(4-\alpha)\). The unconditional bound (1.10) remains valid
after that escape. Neither conclusion presupposes a smooth minimizer.

## 3. An actual deformation makes the Weyl payment indispensable

Use the ordinary-SW quantities from the preceding proof, Section 4.1:
the scalar is \(-4\), so the spinor maximum principle gives
\(0\le\rho\le4\), hence \(0\le x\le1\).

\[
 \rho=|\Phi|^2,\quad x=\rho/4,\quad \omega=\sigma(\Phi),\quad
 K=\int|\nabla_{\mathcal A}\Phi|^2,\quad
 \gamma=\operatorname{Im}\langle\Phi,\nabla_{\mathcal A}\Phi\rangle,
\]
\[
 \Gamma=\int(|d\rho|^2/4+|\gamma|^2),\quad
 J=\|F_{\mathcal A}^+-(F_{\mathcal A}^+)_H\|_2^2,
 \quad F=\int|W^+-W_0|^2,
\]
\[
 W_0=\tfrac12(|\omega|^2I/3-\omega\otimes\omega),\qquad
 L_0=\tfrac23\int(1-x)^2(1+8x-2x^2).
\]

Set

\[
 \mathscr S=K-\Gamma-J-L_0-4\pi^2(p_a-A).
\]

The inherited exact signed identity is

\[
              P-8\pi^2Ah=2(2F-\mathscr S).                    \tag{3.1}
\]

One sufficient target for coefficient four had been to show
\(\mathscr S_+=o(Ah)\), discarding \(2F\). This section proves that
ordinary SW and smooth closeness to a KE metric alone cannot justify
that stronger omission. The balanced target itself is not refuted.

### 3.1. The closed metric and its actual solution

Let \(M=\Sigma_1\times\Sigma_2\), each factor a closed hyperbolic
surface of curvature \(-1\). Its product metric \(g_0\) is negative KE,
with \(s=-4\), Kähler form \(\Omega=\Omega_1+\Omega_2\), and

\[
 A=c_1(K_M^{-1})^2=T_+=8(g_1-1)(g_2-1),\qquad h=0,\quad U=3.
\]

Its canonical ordinary SW solution has parallel spinor of squared norm
four and determinant curvature \(\pm i\Omega\). Choose a nonzero real
holomorphic quadratic differential \(h_1\) on \(\Sigma_1\), viewed as a
TT symmetric tensor, and a nonconstant real eigenfunction on \(\Sigma_2\),
\(\Delta f=\lambda f\), \(\lambda>0\). Put \(H=f h_1\), extended
by zero on other components, and \(B_0=g_0^{-1}H\). Then \(H\) is TT
on the product and \(B_0J=-JB_0\).

The smooth metrics

\[
 g_\varepsilon^{AK}(u,v)=g_0(e^{\varepsilon B_0}u,v)
\]

remain compatible with the fixed closed form \(\Omega\). Let
\(\widehat g_\varepsilon=u_\varepsilon^2g_\varepsilon^{AK}\) be
their scalar-minus-four Yamabe representatives. Negative scalar
normalization is smooth near \(g_0\). Since the scalar derivative in
the TT Einstein direction is zero,
\((6\Delta+8)\dot u=0\), so

\[
 \dot u=0,\qquad \dot{\widehat g}=H.                \tag{3.2}
\]

The fixed form \(\Omega\) is harmonic and self-dual for the entire path;
self-duality of two-forms is conformally invariant in dimension four.
Thus the same canonical class has \(p_a=A\) exactly.

The canonical Kähler monopole is a regular isolated solution modulo
gauge. In the divisor description its divisor is empty; tangent and
obstruction spaces vanish. The exact classical input is
[Okonek--Teleman, Theorem 3.1.2, pp. 413--414](https://library.slmath.org/books/Book37/files/okonek.pdf),
with trivial auxiliary line and perturbation zero. Its expected dimension
is also zero. The gauge-fixed linearization is therefore invertible.
The implicit function theorem supplies a smooth branch of genuine,
unperturbed ordinary SW solutions for \(\widehat g_\varepsilon\).

Under the natural metric identification of spinors, the metric derivative
of the Dirac equation vanishes: its three terms involve respectively
\(H\nabla_{\mathcal A_0}\Phi_0\), divergence and trace of \(H\).
The curvature equation's metric derivative also vanishes: the trace is
zero and \(F_{\mathcal A_0}^-=0\). These formulas are in
[Scala, Theorem 3.3 and Section 4, pp. 1274--1276](https://www.numdam.org/item/10.5802/aif.2640.pdf).
In a fixed gauge slice, invertibility now gives

\[
                    \dot{\mathcal A}=0,\qquad\dot\Phi=0.      \tag{3.3}
\]

There is no invocation of formal cohomological solvability or of a
perturbed monopole equation.

Regularity can also be checked directly in the project's normalization.
On the fixed KE background, write \(b_0=\mathcal A-\mathcal A_0\).
Lichnerowicz and completion of the curvature square give

\[
 \|D_{\mathcal A}\Phi\|_2^2+
 \|-iF_{\mathcal A}^+-\sigma(\Phi)\|_2^2
 =\|\nabla_{\mathcal A}\Phi\|_2^2
   +\tfrac18\||\Phi|^2-4\|_2^2+\tfrac12\|db_0\|_2^2.        \tag{3.3a}
\]

Indeed the cross terms cancel, while harmonic self-duality and exactness
give \(\|F_{\mathcal A}^+\|_2^2=2V+\frac12\|db_0\|_2^2\).
A linearized kernel element \((b_0,\phi)\) therefore satisfies

\[
 \nabla\phi+\tfrac12b_0\Phi_0=0,\quad db_0=0,\quad
 \operatorname{Re}\langle\Phi_0,\phi\rangle=0.
\]

Its component perpendicular to \(\Phi_0\) would be parallel in the
complementary line, which has nonzero curvature, and must vanish. The
remaining solution is \(\phi=it\Phi_0, b_0=-2i\,dt\), a gauge
direction. The gauge-fixed index is \((a^2-T_+)/4=0\), so the operator
is invertible. Thus the use of the implicit function theorem does not
rely on uniqueness of the nonlinear solution alone.

### 3.2. The losses and the directional term have different orders

Because \(B_0\) is anti-Hermitian, its derivation action on \(\Omega\)
vanishes. Thus the derivative of the actual two-form
\(\sigma(\Phi_\varepsilon)\), as an ordinary differential form, is
zero. It follows that \(\rho-4=O(\varepsilon^2)\) and

\[
                 \Gamma,J,L_0=O(\varepsilon^4).                \tag{3.4}
\]

For \(\Gamma\), use the exact identity
\(|\gamma|^2=4|d\omega|^2\); for \(J\), use the unchanged harmonic
curvature representative \(\pm i\Omega\). All orders here hold in
fixed smooth norms on this fixed background.

The covariant derivative of \(\omega\), however, has a nonzero first
variation. At a product orthonormal frame, with \(a,b\) indices on the
first factor and \(\mu,\nu\) on the second, the mixed connection
variations are

\[
 \dot\Gamma^b_{a\mu}=\tfrac12 f_\mu(h_1)_{ab},\qquad
 \dot\Gamma^\mu_{ab}=-\tfrac12 f_\mu(h_1)_{ab}.
\]

The pure first-factor contribution to \(\dot\nabla\Omega\) vanishes:
every area-compatible two-dimensional metric preserves its area form.
The displayed mixed terms give, with the usual two-form norm,

\[
 |\dot\nabla\Omega|^2=\tfrac12|h_1|^2|df|^2.
\]

The Hopf identity
\(|\nabla\omega|^2=(\rho/2)|\nabla_{\mathcal A}\Phi|^2-|\gamma|^2/2\)
therefore proves

\[
 K=c\varepsilon^2+O(\varepsilon^3),\qquad
 c=\tfrac14\|h_1\|_2^2\|df\|_2^2>0.              \tag{3.5}
\]

Since \(h_1\) is a hyperbolic infinitesimal Einstein deformation,
the product TT variation satisfies \(\dot Z=(\lambda/2)H\). Equivalently
apply the Einstein deformation operator to \(f h_1\); only the scalar
Laplacian of \(f\) remains. Hence

\[
 \frac PK\longrightarrow\lambda,\qquad
 \frac{\mathscr S}K\longrightarrow1,\qquad
 \frac FK\longrightarrow\frac{\lambda+2}{4}.        \tag{3.6}
\]

The last limit follows as well from (3.1). The exact nonnegative
decomposition \(D/18=F+\Gamma/2+J+H_{\rm amp}\) gives

\[
             \boxed{\frac{\mathscr S_+}{P+D}
                          \longrightarrow\frac2{11\lambda+18}>0.} \tag{3.7}
\]

Thus the omission fails on genuine smooth solutions, with no zeros or
concentration needed. The missing positive contribution is nonintegrable
directional variation, paid for by \(2F\). This example has \(h=0,U=3\),
not the balanced small-h topology or its minimizing window.

An exact simplification helps isolate this distinction. With
\(T_\omega=\int(|\nabla\omega|^2-2|d\omega|^2)\), the scalar and
weighted scalar identities give

\[
 \boxed{\mathscr S=T_\omega-
       \tfrac23\int(1-x^2)(1+2x^2)-J-4\pi^2(p_a-A).}          \tag{3.8}
\]

For Kähler-aligned solutions \(T_\omega=0\), all terms on the right
are nonpositive. The actual deformation (3.5) is precisely a case where
that favorable alignment is lost.

### 3.3. The coefficient of the Weyl payment is genuinely sharp

The preceding construction continues to a sharp universal statement on
one fixed smooth manifold. Fix the first surface and let the second have
genus two. Double a one-holed hyperbolic torus with geodesic boundary
length \(\ell\) along its boundary. Each half has area \(2\pi\); the
separating geodesic has the standard collar

\[
 dr^2+\ell^2\cosh^2r\,d\vartheta^2,\qquad
 \vartheta\in\mathbb R/\mathbb Z,\qquad
 |r|<\operatorname{arsinh}(1/\sinh(\ell/2)).
\]

For sufficiently small \(\ell\), this width exceeds one. The odd Lipschitz
function equal to \(r\) on \([-1,1]\) and to \(\pm1\) on the two remaining
pieces has mean zero. Direct integration gives

\[
 \int|dv|^2=2\ell\sinh1,\qquad
 \int v^2=4\pi-\ell\int_{-1}^1(1-r^2)\cosh r\,dr
          =4\pi-4\ell/e.
\]

The Rayleigh principle, valid for this \(H^1\) test, supplies actual
first eigenfunctions with

\[
 0<\lambda_1\le\frac{2\ell\sinh1}{4\pi-4\ell/e}\longrightarrow0. \tag{3.9}
\]

This uses the classical hyperbolic pants/collar construction, not a new
spectral existence theorem. The collar metric follows from Fermi
coordinates around a geodesic in curvature \(-1\).

Take \(\ell_j\to0\), normalize \(\|df_j\|_2^2=1\) and
\(\|h_1\|_2^2=4\). At every fixed \(j\), the preceding actual construction
has

\[
 K_j(\varepsilon)=\varepsilon^2+O_j(\varepsilon^3),\quad
 P_j(\varepsilon)=\lambda_j\varepsilon^2+O_j(\varepsilon^3),\quad
 \Gamma_j+J_j+L_{0,j}=O_j(\varepsilon^4).
\]

Choose \(\eta_j\to0\) and then choose \(\varepsilon_j>0\) inside the
individual SW/Yamabe existence interval, with \(\varepsilon_j<1/j\), so
that all three normalized errors are at most \(\eta_j\lambda_j\):

\[
 |K_j/\varepsilon_j^2-1|,\quad
 |P_j/\varepsilon_j^2-\lambda_j|,\quad
 (\Gamma_j+J_j+L_{0,j})/\varepsilon_j^2
                                      \le\eta_j\lambda_j.
\]

No uniform inverse radius is assumed. A further decrease of
\(\varepsilon_j\) may impose arbitrarily small relative \(C^2\) distance
to that background. Since \(p_a=A\) exactly, (3.1) now proves

\[
 \frac{P_j}{\lambda_jK_j}\to1,\quad
 \frac{\mathscr S_j}{K_j}\to1,\quad
 \frac{F_j}{K_j}\to\frac12,\qquad
 \boxed{\frac{\mathscr S_j}{F_j}\to2,\quad\frac{P_j}{F_j}\to0.} \tag{3.10}
\]

At \(h=0\), (3.1) universally gives \(\mathscr S=2F-P/2\le2F\).
The sequence proves that its coefficient two cannot be reduced, even
with an arbitrary fixed finite Ricci allowance: for every \(c<2\) and
finite \(C\),

\[
                         \mathscr S\le cF+CP                   \tag{3.11}
\]

fails on sufficiently late examples. This is a sharp actual-field
statement, not a formal matrix or moment construction. It remains on
\(h=0,U=3\); the balanced coefficient-four question needs its additional
topology or minimizing geometry and remains open.

## 4. The missing minimizing direction is not conformal

There is also an exact second-variation reduction, useful for continuing
the coefficient problem without guessing a negative conformal mode.
Let \(g\) be an actual smooth critical point of \(\mathcal E\), with

\[
 s=-4,\quad0<\alpha=\mathcal E(g)<1,\quad
 a=4-\alpha,\quad\theta=-1/a,\quad
 c=\theta+1/3=(1-\alpha)/(3a)>0.
\]

Here \(a\) is a scalar parameter, not a gauge class. In this section
\(\Delta=d^*d\) again denotes the positive scalar Laplacian. Put

\[
 L=3\Delta+4,\quad M=a\Delta+4,
 \quad\phi_0=\langle Z,k\rangle-\fint\langle Z,k\rangle
\]

for a TT tensor \(k\). For mean-zero \(f\),

\[
\boxed{\begin{split}
 \operatorname{Hess}\mathcal E(k+2fg,k+2fg)
 ={}&\frac aR\left[\operatorname{Hess}Q_\theta(k,k)
                   -6c\langle\phi_0,\Delta L^{-1}\phi_0\rangle\right]\\
 &+\frac8R\left\langle f-\tfrac12L^{-1}\phi_0,
                  LM(f-\tfrac12L^{-1}\phi_0)\right\rangle.
\end{split}}                                                   \tag{4.1}
\]

All brackets use the same metric's real \(L^2\) inner product; \(\theta\)
is held fixed in the Hessian of \(Q_\theta\).

Here is a derivation. Weyl conformal invariance gives
\(Q_\theta=2\int|W|^2+cS_2-16\pi^2\chi\). At a csc critical metric,

\[
 \operatorname{Hess}Q_\theta(2fg,2fg)=24c\langle f,\Delta Lf\rangle,
 \quad
 \operatorname{Hess}Q_\theta(k,2fg)=-12c\langle\phi_0,\Delta f\rangle.
\]

Also \(\mathcal E-J=(S_2-S_1^2/V)/R\) and
\(J-\alpha=aQ_\theta/R\), where \(J=4P/R\). Both first variations
vanish at this metric. The mean-zero scalar derivative is
\((s'[k+2fg])_0=-\phi_0+2Lf\), so

\[
 \operatorname{Hess}\mathcal E(h,h)
  =\frac aR\operatorname{Hess}Q_\theta(h,h)
                  +\frac2R\|(s'[h])_0\|_2^2.
\]

Expanding and completing the square proves (4.1). In particular,

\[
 \operatorname{Hess}\mathcal E(2fg,2fg)
      =\frac8R\langle f,(3\Delta+4)(a\Delta+4)f\rangle>0       \tag{4.2}
\]

for nonzero mean-zero \(f\). Constants are the separate scaling kernel.
The minimizing conformal correction in (4.1) is exactly the one making
the first scalar variation spatially constant. Modulo diffeomorphisms
and scaling, stability therefore reduces to the actual TT form

\[
 \operatorname{Hess}Q_\theta(k,k)
            -6c\langle\phi_0,\Delta(3\Delta+4)^{-1}\phi_0\rangle. \tag{4.3}
\]

The correction is bounded and nonnegative before its minus sign:
\(0\le\Delta(3\Delta+4)^{-1}<1/3\). This identifies the remaining
nonlinear variational question; it does not prove (4.3) is negative.
No Hessian formula valid only at an Einstein background is substituted
at the non-Einstein candidates.

## 5. A stationary zero-end sequence must lose Sobolev control

This is an alternative elliptic endpoint result, not a deduction of I48's
small local lower-Ricci budget. Fix \(S,L_0,\Theta,T_0,\chi_0\). Let

\[
 s=-4,\quad \nabla Q_\theta=0,\quad |\theta|\le\Theta,
 \quad 0<T_+=2\chi+3\tau\le T_0,\quad\chi\le\chi_0,          \tag{5.1}
\]

on closed connected oriented four-manifolds, and assume the genuine global
Sobolev inequality

\[
 \left(\int|u|^4\right)^{1/2}
       \le S\int|du|^2+V^{-1/2}\int|u|^2.                     \tag{5.2}
\]

For a smooth self-dual form with \(|\omega|\le L_0\), define

\[
 Z_t=|\operatorname{Ric}+g|^2+|W^+-A_{\omega,t}|^2
                    +(|\omega|^2-2)^2+|d\omega|^2,
 \quad A_{\omega,t}=t(|\omega|^2I/3-\omega\otimes\omega).
\]

There is \(c=c(S,L_0,\Theta,T_0,\chi_0)>0\) such that

\[
                    \fint Z_t\ge c,\qquad0\le t\le1/4.       \tag{5.3}
\]

**Proof.** Put \(z=\fint Z_t\). If \(z\le1/3\), then
\(P\le zV\), \(W_+\le2zV+L_0^4V/12\), and Chern--Weil gives

\[
 4\pi^2T_+=2W_++\tfrac23V-\tfrac12P,
 \qquad
 \frac{4\pi^2}{2+L_0^4/6}\le V\le8\pi^2T_0.                  \tag{5.4}
\]

The lower bound uses the positive integer \(T_+\ge1\). In the full
four-index norm,

\[
 \int|\operatorname{Rm}|^2=32\pi^2\chi+4P
                       \le32\pi^2\chi_0+\tfrac43(8\pi^2T_0). \tag{5.5}
\]

Thus normalized vanishing error implies absolute vanishing error, but
only after (5.4). At constant scalar curvature the critical equation is

\[
 \Delta\operatorname{Ric}=-2\operatorname{Rm}(\operatorname{Ric})
 -2\theta s\operatorname{Ric}
            +\tfrac12(|\operatorname{Ric}|^2+\theta s^2)g,     \tag{5.6}
\]

with nonpositive tensor Laplacian. Every right-hand term is an algebraic
\(\operatorname{Rm}*\operatorname{Ric}\) term, uniformly for bounded
\(\theta\). This is [Catino, equation (2.1)](https://arxiv.org/pdf/1404.0569),
not an Einstein equation assigned to the original metrics.

Normalize volume to one. Equations (5.2), (5.4), (5.5) and (5.6) give
orbifold compactness and smooth convergence on regular charts by
[Anderson, Theorem 1.1 and Proposition 3.5](https://arxiv.org/pdf/math/0312111).
The Sobolev inequality supplies the lower ball-volume bound; the elliptic
equation supplies the small-energy estimate. There is no division by
\(\theta+1/3\), and csc is retained even at that parameter. Pass to a
subsequence with \(V_j\to V_\infty\in(0,\infty)\), justified by (5.4).
Returning from \(\widehat g_j=V_j^{-1/2}g_j\) to physical scale, a
sequence violating (5.3) has a nonempty smooth regular chart with
\(\operatorname{Ric}=-g\) in the limit.

The local first-order elliptic estimate for self-dual forms bounds
\(\omega_j\) in \(H^1\), since \(d^*\omega_j=-*d\omega_j\). Rellich
compactness and the uniform amplitude bound give strong \(L^2\)
convergence of their quadratic models. The limiting form is harmonic,
smooth, and satisfies

\[
 d\omega=0,\quad |\omega|^2=2,\quad
 W^+=t_\infty(2I/3-\omega\otimes\omega),
 \quad t_\infty\in[0,1/4].
\]

The local incompatibility already proved in I42/I45 excludes this:
at \(t=0\) use the local ASD negative-Einstein almost-Kähler obstruction;
at \(t>0\), Einstein Bianchi and the constant two-eigenvalue model force
the parallel Kähler branch \(t=1/2\). This proves (5.3). QED.

On a fixed topology, an actual csc quadratic-critical zero-end sequence
must therefore lose (5.2). This does not say that an arbitrary minimizing
sequence is critical, does not remove all compactness hypotheses, and
does not address the \(\beta=2\) coefficient problem. The topology bound
is on \(T_+\) and \(\chi\) themselves, not merely their ratio.

## 6. What curvature-maximal extraction supplies, and what it loses

A separate bounded statement advances the core question without assuming
the desired core in advance. Let \(g_j\) be exact scalar-minus-four
critical metrics of \(Q_{\theta_j}\), with bounded \(\theta_j\),

\[
 \operatorname{Vol}B_s(x)\ge v s^4\ (0<s\le r_0),\qquad
 \int|\operatorname{Rm}|^2\le E_0,                            \tag{6.1}
\]

and bounded forms \(|\omega_j|\le L_0\), \(t_j\in[0,1/4]\), such that

\[
 \int\bigl(|\operatorname{Ric}+g|^2+
                      |W^+-A_{\omega_j,t_j}|^2\bigr)\to0.     \tag{6.2}
\]

The errors in (6.2) are absolute, not volume averages. If
\(Q_j=\max|\operatorname{Rm}_{g_j}|\to\infty\), choose maximum
points and rescale \(h_j=r_j^{-2}g_j\), \(r_j=Q_j^{-1/2}\).
Then \(|\operatorname{Rm}_{h_j}|\le1\), with equality at the base
point. The rescaled balls are noncollapsed at every fixed radius.
Bounded curvature and noncollapse give injectivity control. Harmonic
coordinates and (5.6) then bootstrap to smooth pointed convergence on
compact sets to a complete nonflat manifold \(X\).

On fixed rescaled balls, the original volume is \(O(r_j^4)\). Curvature
square energy is scale invariant; the bounded backgrounds in (6.2)
disappear. Therefore \(X\) is Ricci-flat and \(W_X^+=0\). It has finite
curvature energy and Euclidean lower volume growth. The classical
[Bando--Kasue--Nakajima ALE theorem](https://doi.org/10.1007/BF01389045)
now applies to this exact Ricci-flat limit, not to \(g_j\).
The limit has one end: multiple ends would force an isometric splitting
with a compact transverse factor and hence linear volume growth,
contrary to its Euclidean lower growth. Thus the truncations below have
one outer boundary, as required by the entire-core theorem.

Large compact ALE truncations embed into \(M_j\). A diagonal choice of
truncation radius gives actual entire smooth cores whose original volumes
tend to zero and whose lifted outer collars converge to a flat cone.
Their total

\[
 \int\bigl(|\operatorname{Ric}^{\circ}|^2+4|W^+|^2+s^2/12\bigr)
                                                               \tag{6.3}
\]

tends to zero by (6.2). Explicitly its integral over a core
\(\Omega_j\) is at most
\(8\,\mathrm{error}_j+C(L_0)\operatorname{Vol}_{g_j}(\Omega_j)\).
No bubble-tree energy identity is being assumed. I47's entire-core theorem therefore excludes
the physical quotients \(1/n(1,-2)\), odd \(n\ge3\), as their infinity
groups. The group cannot be trivial either: a complete Ricci-flat ALE
space with Euclidean asymptotic volume ratio is Euclidean by volume
rigidity. Its order is bounded by \(\omega_4/v\).

The metric core has genuinely been extracted. The nonzero actual
opposite-spinor field has not. Its amplitude and Dirac errors have
different rescaling weights: absolute errors tending to zero need not
tend to zero after division by powers of \(r_j\). For instance,
the mean amplitude error on a fixed rescaled ball contains

\[
                      r_j^{-4}\int_{\Omega_j}(\rho-\rho_*)^2.
\]

Consequently it is not legitimate to combine the extracted core with
I46's simultaneous nonzero-spinor holonomy conclusion without a new
same-scale field estimate. These are terminal cores, not an identified
entire exceptional/handle surgery region or a proved bubble tree.

## 7. The next exact questions left by these arguments

For the balanced coefficient, retain the full signed target
\((\mathscr S-2F)_+=o(Ah)\) in (3.1), or find a variational/core
argument producing the same conclusion. The stronger omission of \(2F\)
requires topology-specific information: it is false as a universal
ordinary-SW principle. A negative direction for a hypothetical minimizer
must be found in the reduced TT form (4.3), not in conformal directions.

For the general integral zero endpoint, a metric core and a calibrated
field on that core are distinct outputs. Section 6 makes their scaling
gap explicit. Section 5 excludes uniformly Sobolev-controlled stationary
escape, while I48 treats a different integral-Ricci class. Neither turns
raw weak input into a complete core decomposition.

For the dynamic connection, (1.10) already applies to actual smooth
near-minimizing initial metrics without a minimizer. Determining the
forced loss of smooth continuation, or proving persistence estimates
strong enough to contradict it in a broader input class, requires new
analysis. It is not inferred from the monotonic volume formula alone.
