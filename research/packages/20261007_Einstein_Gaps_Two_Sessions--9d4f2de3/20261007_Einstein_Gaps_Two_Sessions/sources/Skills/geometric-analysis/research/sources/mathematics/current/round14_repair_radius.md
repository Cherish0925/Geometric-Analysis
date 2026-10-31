# An all-mode no-repair radius for optimized closed shear metrics

## 1. Statement

Let \(G_c\) be the optimized pure-shear closed family in
`round14_global.md`, with all smooth gluing data fixed, and assume that
at least one edge has nonzero harmonic shear form \(\beta\). The common
waist length is \(\ell=2\pi c\). On the selected edge,
\[
 G_c=dt^2+a_c(t)^2\theta_c^2+h_F,
 \quad a_c=c\cosh(kt),\quad k=\sqrt3,
 \quad \theta_c=d\phi+z_c(t)\beta,
\]
where \(K(h_F)=-3\) and
\[
 z_c'=I_c^{-1}\eta_{R_c}(t)\operatorname{sech}^3(kt),
 \quad I_c=\int\eta_{R_c}\operatorname{sech}^3(kt)dt,
 \quad R_c=w_c-C_0,\quad C_0>4.
                                                               \tag{1}
\]
Here \(w_c\) is the full hyperbolic half-collar width. Thus
\(e^{-kR_c}\asymp c\) and \(a_c\asymp1\) on a fixed-width
neighborhood of the two ends \(\pm R_c\). The even cutoff \(\eta_R\)
is one on \(|t|\le R-1\), zero near and beyond \(|t|=R\), and has
uniformly bounded derivatives. This family has
\[
 \|G_c^{-1}\operatorname{Ric}_{G_c}+3I\|_\infty\le Cc^2,
 \qquad \|\operatorname{Rm}_{G_c}\|_\infty\le C.              \tag{2}
\]

**Theorem.** There are constants \(\varepsilon,b,c_0>0\), depending
only on the fixed gluing and fiber data, such that for \(0<c<c_0\)
and every smooth symmetric tensor \(h\) satisfying
\[
 \|h\|_{C^2(G_c)}
 :=\sum_{j=0}^2\|\nabla_{G_c}^j h\|_{L^\infty(G_c)}
 \le\varepsilon c,
\]
the positive metric \(g=G_c+h\) satisfies
\[
 \boxed{\|g^{-1}\operatorname{Ric}_g+3I\|_\infty\ge bc^2.}   \tag{3}
\]
After possibly reducing \(\varepsilon\), no such \(g\) is Einstein
with **any** Einstein constant.

There is no symmetry, gauge, foliation, or support condition on \(h\).
The perturbation may have all circle Fourier modes, all fiber modes, and
arbitrary global support. Constants are not asserted uniform over changing
shear classes or degenerating fiber metrics. This is a neighborhood theorem
for an explicit fixed smooth family, not global Einstein nonexistence.

## 2. A closed test tensor with small adjoint error

Choose an even cutoff \(\chi_c\) equal to one on \(|t|\le R_c\),
zero on \(|t|\ge R_c+1\), with uniformly bounded derivatives. These
outer bands lie inside the actual collar and have zero connection
curvature. Extend by zero to the entire closed manifold:
\[
 H_c=\chi_c f\bigl(dt^2-a_c^2\theta_c^2\bigr),
 \qquad f=\operatorname{sech}^2(kt).                          \tag{4}
\]
This is globally smooth and trace-free for \(G_c\).

The key bounds are
\[
 \boxed{\|H_c\|_{L^1}\le Cc,\qquad
        \|P_{G_c}H_c\|_{L^1}
          +\|\delta_{G_c}H_c\|_{L^1}\le Cc^2,}              \tag{5}
\]
where
\[
 \mathcal B_Gh=\delta_Gh+\tfrac12d\operatorname{tr}_Gh,
 \qquad P_Gh=D(\operatorname{Ric}+3g)_G[h]+\delta_G^*\mathcal B_Gh
            =\tfrac12\Delta_{L,G}h+3h.                     \tag{6}
\]
The operator \(P_G\) is formally self-adjoint on the closed manifold.
The sign convention is \((\delta h)_j=-\nabla^ih_{ij}\).

### Exact divergence, including electric shear

For the uncut tensor \(H_0=f(dt^2-a^2\theta^2)\), direct covariant
differentiation gives
\[
 \delta H_0=-(f'+2a'/a\,f)dt=0.                             \tag{7}
\]
This identity remains exact when \(\theta=d\phi+z(t)\beta\)
has nonzero curvature. Consequently
\(\delta H_c=-\chi_c'f\,dt\); only the two outer cutoff bands
contribute. There \(f=O(c^2)\) and the volume density \(a\) is
bounded above and below. Their total contribution is \(O(c^2)\).
Also
\[
 \|H_c\|_1\le Cc\int_{\mathbb R}\operatorname{sech}(kt)dt
 \le Cc.
\]

### The actual gauged linearization on the core

On the central region where \(\eta_{R_c}=1\), the Maxwell equation
\((a^3z')'=0\) holds. For \(B(x)=|\beta(x)|_{h_F}^2\), the
nonzero orthonormal blocks of \(P_GH_0\) are exactly
\[
 \begin{split}
 (P_GH_0)_{tt}&=\tfrac12a^2fz'^2B,\\
 (P_GH_0)_{UU}&=-\tfrac32a^2fz'^2B,\\
 (P_GH_0)_{XY}&=a^2fz'^2\beta(X)\beta(Y),\\
 (P_GH_0)_{XU}&=a f'z'\beta(X).
 \end{split}                                                  \tag{8}
\]
One way to derive (8) is to differentiate the Kaluza--Klein Ricci
formula along
\[
 G_\tau=(1+\tau f)dt^2+a^2(1-\tau f)\theta^2+h_F.
\]
The unsheared part has zero first Einstein variation. For the mixed
component, the varying Maxwell density is
\(a^3(1-2\tau f)z'+O(\tau^2)\), giving \(af'z'\beta\).
Equation (7) eliminates the gauge term on this core. The accompanying
program also derives all ten first-variation blocks directly from
coordinate Christoffel symbols, without importing the variation formula.

Since \(z'=O(\operatorname{sech}^3(kt))\), (8) implies
\[
 |P_GH_0|\le C\bigl(c^2\operatorname{sech}^6(kt)
                  +c\operatorname{sech}^4(kt)\bigr).
\]
Integrating against \(a\,dt\,d\phi\,d\mu_F\) gives \(O(c^2)\).

In the two Maxwell cutoff bands, \(a\asymp1\),
\(z'=O(c^3)\), and each of its fixed derivatives is \(O(c^3)\).
The tensor and its derivatives are \(O(c^2)\). The metric is uniformly
smooth there in local gauges, so the direct second-order operator bound
is \(O(c^2)\) on a bounded-volume region. In the two farther tensor
cutoff bands the connection is closed, the uncut tensor is an exact
product Einstein kernel, and only the cutoff commutator remains; it is
again \(O(c^2)\). This proves (5) without a noncollapse assumption.

## 3. The signed source survives arbitrary small corrections

Put \(E_c=\operatorname{Ric}_{G_c}+3G_c\) and
\(B_0=\|\beta\|_{L^2(F)}^2>0\). The tensor cutoff is identically
one wherever the selected shear residual is supported. The exact pairing
from `round14_shear.md` is
\[
 \begin{split}
 \int_M\langle E_c,H_c\rangle d\mu_{G_c}
 &=-2\pi c^3B_0
   \frac{\int\eta_{R_c}^2\operatorname{sech}^5(kt)dt}{I_c^2}\\
 &=-3kB_0c^3+O(c^6).
 \end{split}                                                  \tag{9}
\]
Other edges contribute nothing, since \(H_c\) has support only on
the selected edge. In particular the absolute value in (9) is at least
\(A c^3\) for a fixed \(A>0\) and all sufficiently small \(c\).

Let \(\eta=\|h\|_{C^2(G_c)}\). Formal self-adjointness of (6)
and integration by parts on the closed manifold give
\[
 \begin{split}
 \int_M\langle D E_{G_c}[h],H_c\rangle
 &=\int_M\langle h,P_{G_c}H_c\rangle
   -\int_M\langle\mathcal B_{G_c}h,\delta_{G_c}H_c\rangle,\\
 \left|\int_M\langle D E_{G_c}[h],H_c\rangle\right|
 &\le Cc^2\eta.
 \end{split}                                                  \tag{10}
\]
No Bianchi gauge is imposed on \(h\). Its complete gauge contribution
is the second integral and is controlled by (5).

For \(\eta\le1/2\), the exact difference-of-connections formula
gives the pointwise Taylor bound
\[
 E(G_c+h)=E_c+D E_{G_c}[h]+Q_c(h),\qquad
 |Q_c(h)|_{G_c}\le C\eta^2.                                 \tag{11}
\]
For example the nonlinear Ricci terms are bounded by a fixed constant
times \(|h||\nabla^2h|+|\nabla h|^2+|\operatorname{Rm}||h|^2\).
All norms and derivatives in this estimate use \(G_c\). Uniform
curvature bounds and \((G_c+h)^{-1}\le2G_c^{-1}\) make its constant
independent of the shrinking injectivity radius. It is a pointwise tensor
estimate, not an elliptic estimate relying on a uniform Sobolev constant.
Combining (5) and (11) yields
\[
 \left|\int_M\langle Q_c(h),H_c\rangle\right|
 \le Cc\eta^2.                                               \tag{12}
\]
It follows from (9)--(12) that
\[
 \left|\int_M\langle E(G_c+h),H_c\rangle\right|
 \ge A c^3-Cc^2\eta-Cc\eta^2.                               \tag{13}
\]
Choose \(\varepsilon>0\) such that
\(C(\varepsilon+\varepsilon^2)\le A/2\). For
\(\eta\le\varepsilon c\), the right side is at least
\(Ac^3/2\). On the other hand, metric comparability and (5) bound
the left side above by
\[
 Cc\,\|(G_c+h)^{-1}\operatorname{Ric}_{G_c+h}+3I\|_\infty.
\]
This proves the all-mode lower bound (3).

## 4. Allowing the Einstein constant to change

Suppose, contrary to the final assertion, that
\(\operatorname{Ric}_{G_c+h}=\lambda(G_c+h)\) in the same ball.
Equations (2) and (11), with the elementary pointwise bound
\(|D E[h]|\le C\eta\), imply
\[
 |\lambda+3|\le C(c^2+\eta).                                \tag{14}
\]
The receiver is trace-free for \(G_c\), so its pairing with this
putative Einstein output is
\[
 \int\langle E(G_c+h),H_c\rangle
 = (\lambda+3)\int\langle h,H_c\rangle.
\]
Consequently its absolute value is at most
\[
 Cc\eta(c^2+\eta)
 \le C(\varepsilon c+\varepsilon^2)c^3.                    \tag{15}
\]
Reducing \(\varepsilon\), then \(c_0\), makes (15) strictly less
than the lower bound \(Ac^3/2\) in (13), a contradiction. In
particular any putative Einstein constant in this neighborhood would
already be negative by (14); the proof does not silently impose its
normalization.

The same conclusion holds after any diffeomorphism pullback: if an
Einstein metric had a representative in this \(C^2(G_c)\) ball, that
representative itself would contradict the theorem. This does not control
weaker metric distances such as Gromov--Hausdorff distance.

## 5. Consequence and remaining equation

The construction has defect \(O(c^2)\), yet no Einstein metric lies
within an all-tensor geometric \(C^2\) distance \(\varepsilon c\).
The proof uses a localized approximate adjoint kernel to control **every**
linear and nonlinear correction in that ball. It does not omit the
complementary modes or require them to preserve a circle action.

This is stronger than knowing that the uncorrected residual has a signed
projection, and stronger than excluding only invariant corrections. It
still permits corrections of larger order, other degenerating branches,
and Einstein metrics elsewhere on the same smooth manifold. The global
Einstein existence question and the original Yau26 problem remain open.

`round14_repair_radius_check.py` verifies exact divergence and the full
coordinate first variation used in (8); estimates (5), (10)--(15) are
proved analytically above.
