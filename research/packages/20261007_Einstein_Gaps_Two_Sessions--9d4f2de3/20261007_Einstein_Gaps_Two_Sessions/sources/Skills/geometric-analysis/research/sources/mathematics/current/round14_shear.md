# Eliminating the connection equation: shear capacity and its two geometric forces

## 1. The fixed product throat

Let \((F,h)\) be a closed oriented surface with curvature \(-3\), let
\(k=\sqrt3\), and put
\[
 I_R=[-R,R],\qquad a(t)=c\cosh(kt),\qquad c>0.
\]
The circle coordinate has period \(2\pi\). A nonzero integral shear class
has harmonic representative \(\beta\in\Omega^1(F)\); write
\(B=\|\beta\|_{L^2(h)}^2>0\). Consider
\[
 g=dt^2+a^2(d\phi+z(t)\beta)^2+h,\qquad z(-R)=0,
 \quad z(R)=1.                                                   \tag{1}
\]
Replacing a circle-valued gluing map by the map having its harmonic
differential changes it by an isotopy, not its integral shear or the
diffeomorphism type of the closed gluing. Alternatively one keeps the
original representative and removes its exact component by a gauge change.

Set
\[
 J_m(R)=\int_{-R}^R\operatorname{sech}^m(kt)\,dt,
 \qquad I_3=\int_{-R}^R a^{-3}dt=c^{-3}J_3.
\]
All finite-interval assertions below concern the displayed boundary data.
Matching every derivative to flat exterior connections is treated in §6.

The Round-11 Ricci formulas give, in the orthonormal splitting
\((T=\partial_t,U=a^{-1}\partial_\phi,TF)\),
\[
 \begin{split}
 E_{tt}&=-\tfrac12a^2z'^2|\beta|^2,&
 E_{UU}&=\tfrac12a^2z'^2|\beta|^2,\\
 E_{XY}&=-\tfrac12a^2z'^2\beta(X)\beta(Y),&
 E_{XU}&=-\tfrac a2(z''+3a'/a\,z')\beta(X),
 \end{split}                                                     \tag{2}
\]
where \(E=\operatorname{Ric}+3g\); the other mixed entries vanish because
\(\beta\) is closed and coclosed. Thus eliminating the actual mixed
Einstein equation means solving \((a^3z')'=0\), not minimizing the
waist projection in isolation.

## 2. Exact connection capacity

The unique solution of that mixed equation with the prescribed endpoints is
\[
 \boxed{z'(t)=\frac{a(t)^{-3}}{I_3}
       =\frac{\operatorname{sech}^3(kt)}{J_3(R)}.}                \tag{3}
\]
It is also the unique minimizer of the connection quadratic form
\[
 \mathscr C_c(z,h)=B\int_{-R}^R a^3z'^2dt,
 \qquad \min_z\mathscr C_c=\boxed{\frac{c^3}{J_3(R)}B}.         \tag{4}
\]
The quadratic form is written without the circle factor \(2\pi\). In the
Einstein--Hilbert scalar integral its curvature contribution is
\(-\pi\mathscr C_c\); that fixed factor does not change the Euler equation.
Cauchy--Schwarz applied to \(1=\int z'\) proves (4), including its equality
condition. No asymptotic approximation is involved.

This capacity remains sharp among arbitrary invariant connections on the
same quotient \(I_R\times F\), not only the scalar ansatz. Write
\[
 \mathcal F=dt\wedge\alpha_t+\mathcal B_t,
 \qquad \mathscr C(A)=\int_{I_R}a^3
   \bigl(\|\alpha_t\|_2^2+\|\mathcal B_t\|_2^2\bigr)dt.        \tag{5}
\]
Two-form norms here are exterior-power norms. In temporal gauge
\(\alpha_t=\partial_t A_t\) and \(\mathcal B_t=d_FA_t\). Suppose the
end connections are closed and their cohomological difference is
\([\beta]\). Harmonic projection gives
\(\int P_{\mathcal H}\alpha_tdt=\beta\), so Hilbert-space
Cauchy--Schwarz yields
\[
 \mathscr C(A)\ge\frac{\|\beta\|_2^2}{I_3}.                   \tag{6}
\]
Equality forces zero magnetic curvature and harmonic electric curvature
\(\alpha_t=a^{-3}\beta/I_3\); (3) realizes it. Exact endpoint components
are removable by gauge, and a common flat harmonic component is immaterial.
Thus neither nonharmonic electric modes nor magnetic curvature lowers this
fixed-background capacity.

## 3. The surviving waist force and the distinction between its weight and capacity

Use the Round-13 waist tensor
\[
 H_0=f(t)\bigl(dt^2-a^2(d\phi+z\beta)^2\bigr),\qquad
 f=\operatorname{sech}^2(kt)=c^2/a^2.
\]
It is the exact transverse-traceless Einstein kernel at the unsheared
product metric. Pairing with the **actual** residual (2) gives
\[
 \int_{I_R\times S^1\times F}\langle E,H_0\rangle d\mu
 =-2\pi c^2B\int_{I_R}a z'^2dt.                              \tag{7}
\]
At the Maxwell solution (3), therefore,
\[
 \boxed{\mathscr F_{\mathrm{waist}}
       =-2\pi c^3B\frac{J_5(R)}{J_3(R)^2}<0.}                \tag{8}
\]
In the complete-throat limit,
\[
 J_1\to\frac\pi k,\quad J_3\to\frac\pi{2k},\quad
 J_5\to\frac{3\pi}{8k},\qquad
 \mathscr F_{\mathrm{waist}}\to-3kc^3B.                       \tag{9}
\]
This is a reduced force after the connection equation has been solved.
It is not the initial cut-off profile's coefficient.

The best lower bound on the negative projection over all scalar profiles is
instead
\[
 -\mathscr F_{\mathrm{waist}}
 \ge\boxed{\frac{2\pi c^3}{J_1(R)}B};                       \tag{10}
\]
its equality profile has \(z'\propto a^{-1}\), not \(a^{-3}\).
On the complete throat this lower bound is \(2kc^3B\), whereas the
Maxwell projection is \(3kc^3B\). Confusing these variational problems
would give the wrong leading coefficient.

For a general connection (5), Kaluza--Klein contraction gives the exact
identity
\[
 \int\langle E,H_0\rangle d\mu
 =-2\pi c^2\int_{I_R}a
  \bigl(\|\alpha_t\|_2^2+\tfrac12\|\mathcal B_t\|_2^2\bigr)dt.
                                                                    \tag{11}
\]
Indeed \(\operatorname{Ric}_{tt}-\operatorname{Ric}_{UU}
=-a^2(|\alpha|^2+|\mathcal B|^2/2)\). Harmonic projection and
Cauchy--Schwarz prove (10) in this larger invariant connection class as
well. Equation (11) concerns the fixed quotient metric and radius; it
does not hold unchanged after arbitrary metric correction.

## 4. A second surviving force: the fiber's Teichmüller directions

Define
\[
 T_\beta=\beta\otimes\beta-\tfrac12|\beta|^2h.                \tag{12}
\]
It is a nonzero transverse-traceless tensor. To check the divergence,
use \(\nabla^i\beta_i=0\) and \(\nabla_i\beta_j=\nabla_j\beta_i\):
\[
 \nabla^i(T_\beta)_{ij}
 =\beta^i\nabla_i\beta_j-\beta^i\nabla_j\beta_i=0,
 \qquad |T_\beta|^2=\tfrac12|\beta|^4.                       \tag{13}
\]
For a hyperbolic surface, scalar-curvature variation of a TT tensor is
zero; since \(\operatorname{Ric}_h=K_hh\),
\(D(\operatorname{Ric}+3h)[T_\beta]=0\). This is a genuine hyperbolic
shape direction, not a massive fiber mode. It integrates to curvature
\(-3\) metrics: start with \(h+sT_\beta\) and uniformize conformally;
the conformal correction has zero first derivative because its scalar
linearization is invertible and the original curvature derivative vanishes.

For any fiber TT tensor \(Q\) constant in \(t,\phi\), equation (2) gives
at the Maxwell solution
\[
 \boxed{\int\langle E,Q\rangle d\mu
 =-\frac{\pi c^3}{J_3(R)}\langle T_\beta,Q\rangle_{L^2(F)}.} \tag{14}
\]
In particular, the pairing with \(T_\beta\) is strictly negative.

This force is precisely the variation of the reduced Hodge energy.
For a fixed cohomology class, let
\(\mathcal H(h)=\|\beta_h\|_2^2\). Differentiating the harmonic
minimization problem gives
\[
 D\mathcal H_h[Q]=-\int_F\langle T_\beta,Q\rangle d\mu_h.     \tag{15}
\]
The derivative of the minimizing representative contributes zero because
it is exact and \(\beta_h\) is coclosed. Therefore
\[
 D\mathcal H_h[T_\beta]
 =-\tfrac12\int_F|\beta|^4d\mu_h<0.                          \tag{16}
\]
Consequently the single-shear reduced potential
\(c^3\mathcal H(h)/J_3\) has no stationary point in hyperbolic fiber
moduli. The mixed equation does not remove its shape force.

This last statement is about this potential, not the complete closed
Einstein problem. Several shears, mapping-class energy and exterior
responses contribute additional terms. For example
\(T_{*\beta}=-T_\beta\), so two equally weighted star-related harmonic
forms can cancel their shape stresses. No integrality of \(*\beta\)
is asserted by this algebraic example.

## 5. Linear backreaction: what it must transmit to the ends

The shape force can be solved locally but cannot be erased without
boundary response. A first-order correction \(q=v(t)T_\beta\) about
the unsheared product has
\[
 D(\operatorname{Ric}+3g)[q]_{FF}^{TT}
 =-\tfrac12\bigl(v''+(a'/a)v'\bigr)T_\beta.                  \tag{17}
\]
Its divergence and trace are zero; hence the Bianchi-gauged and ungauged
linearizations agree on this tensor. Cancelling the fiber TT source
requires
\[
 (a v')'=-a^3z'^2,
 \qquad [a v']_{-R}^R=-\frac1{I_3}=-\frac{c^3}{J_3}.         \tag{18}
\]
Thus a correction which has zero first normal derivative at both ends
cannot solve this equation. Under the Dirichlet conditions
\(v(-R)=v(R)=0\), symmetry gives the explicit solution
\[
 v'(t)=\frac{1/2-z(t)}{I_3a(t)},\qquad
 v(t)=\frac{c^2}{J_3}\int_{-R}^t
                (1/2-z(s))\operatorname{sech}(ks)ds.         \tag{19}
\]
It is positive in the interior and has size \(O(c^2)\), while it exports
the nonzero flux (18). In the complete-throat limit,
\[
 \boxed{v(0)=c^2\left(\frac14+\frac1{\pi^2}\right).}        \tag{20}
\]
The scalar trace has a different response. Let a first correction be
\(h_t=h+c^2q_t\), \(a_{\mathrm{new}}=a(1+c^2p)\), keep Gaussian
normal gauge, and put
\(m(t)=(2\operatorname{Area}F)^{-1}\int_F\operatorname{tr}_h(q_t')\).
The averaged \(UU-tt\) equation at order \(c^2\) is
\[
 m'-(a'/a)m
 =-\frac{B}{\operatorname{Area}F}\cosh^2(kt)z'^2.             \tag{21}
\]
The radius's spatial Laplacian integrates to zero. At (3),
\[
 \left[\frac m{\cosh(kt)}\right]_{-R}^R
 =-\frac{B}{\operatorname{Area}F}\frac{J_5}{J_3^2}<0.         \tag{22}
\]
Hence the scalar/fiber-trace correction also needs nonzero end response.
For symmetric data, \(m\) is odd and grows like \(\cosh(kt)\) toward
the ends. A compactly supported first correction cannot cancel this
receiver. A global correction can transmit the flux into adjacent blocks;
establishing that it cannot do so is a further global problem.

Equations (18) and (22) are different flux balances. They identify actual
low-mode terms that must remain in the Schur complement. They do not prove
that the complementary solution or nonlinear terms are \(o(c^3)\).

## 6. Smooth use in the existing closed construction

Choose an even cut-off \(\eta_R\), equal to one on \(|t|\le R-1\),
zero near \(|t|=R\), with uniformly bounded fixed derivatives. Set
\[
 \widetilde z'_R
 =\frac{\eta_R\operatorname{sech}^3(kt)}
        {\int_{-R}^R\eta_R\operatorname{sech}^3(kt)dt}.
                                                                    \tag{23}
\]
Integrate from the left endpoint. This preserves the exact shear jump and
matches to flat endpoint connections to every order. The mixed equation
fails only in the outer unit bands, where (2) gives
\[
 \|E_{UF}\|_\infty=O(ce^{-2kR}),\qquad
 \|E_{tt}\|_\infty+\|E_{UU}\|_\infty+\|E_{FF}\|_\infty=O(c^2).
                                                                    \tag{24}
\]
The same orders hold in every fixed invariant covariant derivative norm.
In the Round-11 fixed-fiber plateau one may take
\(R=\vartheta(L_\ell-1)\), \(0<\vartheta<1\), with
\(e^{-2kL_\ell}\asymp\ell\) and \(c=\ell/(2\pi)\). Thus the shear
part improves from \(O(\ell)\) to
\[
 \boxed{O(\ell^2+\ell^{1+\vartheta})}.                     \tag{25}
\]
The disjoint mapping-class part still has error \(O(1/|\log\ell|)\).
When there is no mapping-class transition, a longer constant-fiber collar
can make the mixed tail still smaller. None of these rate improvements
supplies a global Einstein existence or nonexistence theorem.

The capacity and waist force of (23) have relative error
\(O(e^{-3kR})\) from their complete-throat limits. The neck tensor can
be cut off outside the support of \(\widetilde z'_R\), so its exact
residual projection retains (8) up to that tail error. This is compatible
with the actual closed gluing rather than a noncompact profile inserted
without end matching.

## 7. What the reduction establishes

After solving the complete invariant connection equation on the fixed
product quotient, the nonzero cohomological shear still produces a
strictly negative waist force and a nonzero hyperbolic-shape force. Their
coefficients, sharp connection capacity, and first boundary responses are
explicit. Arbitrary invariant connection modes cannot reduce the capacity
below (6). Small scalar and fiber corrections can carry these forces to
the boundary rather than cancelling them internally.

The remaining finite-dimensional equation must include waist parameters,
fiber moduli, end response and all complementary-mode feedback. No claim
that the signed leading force survives that entire equation is made here.
The exact calculations are checked in `round14_shear_check.py`; the Hodge
projection, end matching and variation arguments are the analytic proofs
given above.
