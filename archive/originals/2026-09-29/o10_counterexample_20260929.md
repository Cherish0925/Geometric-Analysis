# O10: a concentration restriction on any actual counterexample

This note concerns the O10 assumptions in Section 25 of the attached integrated manuscript. It does not construct a closed counterexample and does not close the full endpoint. Its main new conclusion is a weighted covariant interpolation estimate: the fourth-power energy of the **actual bounded spinor gradient** cannot retain positive normalized mass at arbitrarily large gradient amplitude once the spinor curvature has a bounded model with vanishing normalized square error. The manuscript supplies precisely that curvature fit along a hypothetical endpoint sequence.

## 1. General lemma

Let $(M_j,g_j)$ be closed Riemannian manifolds of one fixed dimension, $E_j$ fixed-rank Hermitian bundles with unitary connections, and $u_j$ smooth sections. All norms and integrals are for $g_j$. Write $V_j=\operatorname{Vol}(M_j)$,

\[
P=\nabla u,\qquad H=\nabla P,\qquad q=|P|^2.
\]

Suppose, with constants independent of $j$,

\[
|u|\le M,\quad \nabla^*\nabla u=f(|u|^2)u,
\quad |f|+|f'|\le C_f
\]

on the relevant bounded interval, and

\[
\operatorname{Ric}=R_0+E_R,\qquad F_E=F_0+E_F,
\quad |R_0|+|F_0|\le K.
\]

Neither $R_0$ nor $F_0$ needs derivative bounds, and neither must arise from an independent background connection. Put

\[
e_j^2=\fint (|E_R|^2+|E_F|^2),
\qquad \sup_j e_j^2<\infty.
\]

There exist universal-for-these-data $\varepsilon\in(0,1)$ and $C$ such that, for $L\ge1$,

\[
\boxed{
\fint \left(\frac{q}{L^2+q}\right)^\varepsilon
       (|H|^2+q^2)
\le C L^{-2\varepsilon}+C e_j^2.}
\tag{1}
\]

In particular, if $e_j\to0$,

\[
\boxed{
\lim_{L\to\infty}\limsup_{j\to\infty}
\fint_{\{q>L^2\}}q^2=0.}
\tag{2}
\]

The same estimate controls the Hessian-square energy **on the sets where $q$ is large**. It does not assert uniform integrability of $|H|^2$ on all small sets.

### 1.1 Exact weighted Hessian interchange

Use a regularization

\[
w=\left(\frac{q+\delta}{L^2+q+\delta}\right)^\varepsilon,
\qquad\delta>0.
\]

It obeys

\[
|dw|\sqrt q\le2\varepsilon w|H|.
\tag{3}
\]

In a local orthonormal frame, $H_{ij}=\nabla_iP_j$ and
$H_{ij}-H_{ji}=F_{ij}u$. With real parts in all Hermitian pairings,

\[
\sum_{i,j}\langle H_{ij},F_{ij}u\rangle
=\frac12\sum_{i,j}|F_{ij}u|^2.
\]

Thus swapping the two Hessian indices and integrating the resulting cross term gives the exact identity

\[
\begin{split}
\int w|H|^2={}&\int w\langle P_i,\nabla_i(fu)\rangle
-\int w\langle P_i,\mathcal C_i\rangle\\
&-\int (\nabla_jw)\langle P_i,H_{ij}\rangle
+\frac12\int w\sum_{i,j}|F_{ij}u|^2,
\end{split}
\tag{4}
\]

where

\[
\mathcal C_i=\sum_j[\nabla_j,\nabla_i]P_j.
\]

The commutator contains only a Ricci contraction of $P$ and a bundle-curvature contraction of $P$. Formula (4) uses $\operatorname{tr}H=-fu$. Signs of the separate Ricci contractions depend on the curvature convention; the invariant commutator expression avoids that ambiguity. The norm estimate is

\[
|\mathcal C|\le C(|\operatorname{Ric}|+|F_E|)|P|.
\]

Crucially, **no derivative of $F_E$, $F_0$, or $R_0$ occurs**. Also $|\nabla(fu)|\le C|P|$. Let $I=\int w|H|^2$ and $J=\int wq^2$. Equations (3)--(4), followed by Young's inequality, yield for every small fixed $a>0$,

\[
(1-2\varepsilon)I
\le C\int w(1+q)+aJ+C_a\int(|E_R|^2+|E_F|^2).
\tag{5}
\]

Here $\int w |E|q\le aJ+C_a\int |E|^2$; the term involving $F_Eu$ is bounded by a constant times $\int w+\int|E_F|^2$.

### 1.2 Bounded-section interpolation

Set $B_i=\operatorname{Re}\langle u,P_i\rangle$. Since

\[
\operatorname{div}B=q-f|u|^2,
\]

integration of $\operatorname{div}(wqB)$ gives

\[
J=\int wqf|u|^2-\int w\langle dq,B\rangle
                   -\int q\langle dw,B\rangle.
\]

Use $|B|\le M\sqrt q$, $|dq|\le2\sqrt q|H|$, and (3). Then

\[
J\le C\int wq+2M(1+\varepsilon)\sqrt{IJ}
\le\tfrac12J+C I+C\int wq.
\tag{6}
\]

First take $w\equiv1$ in (4)--(6). Testing the section equation by $u$ gives $\int q=\int f|u|^2\le CV$. Absorbing the $aJ$ term proves $\fint(|H|^2+q^2)\le C(1+e_j^2)$. Thus the fourth-power gradient budget required below follows from the lemma's hypotheses, rather than being an extra assumption.

Now use the displayed regularized weight. Choose first $\varepsilon$ small, then $a$ in (5) small enough relative to the fixed constant in (6). Absorbing yields

\[
I+J\le C\int w(1+q)+C\int(|E_R|^2+|E_F|^2).
\]

Let $\delta\downarrow0$. For $0<\varepsilon<1$,

\[
w(1+q)\le L^{-2\varepsilon}(q^\varepsilon+q^{1+\varepsilon}),
\]

whose volume average is bounded by $C L^{-2\varepsilon}$ using the just-proved normalized $q^2$ bound. This proves (1). On $q>L^2$, $w\ge2^{-\varepsilon}$, proving (2).

## 2. Application to the manuscript's same actual solution

On the scalar-minus-four representative, the manuscript takes

\[
D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),\qquad
0\le\rho=|\Phi|^2\le2.
\]

Its Weitzenböck equation is

\[
\nabla_A^*\nabla_A\Phi=(1-\rho/2)\Phi.
\]

The connection here is the full positive-spinor connection. Its curvature involves $W^+$, scalar curvature, the off-diagonal traceless Ricci block, and determinant curvature $F_A$. The opposite Weyl tensor does not occur in that representation. The manuscript's equation `proof:single-parameter:e2.14a` provides a bounded model $K$ for $-iF_A^-$ with

\[
\fint|F_A^- - iK|^2=O(\sqrt\eta),\qquad
\eta=r+D_\beta/V+\beta^{-2}\to0.
\]

The other curvature pieces are bounded or have vanishing normalized square error: scalar curvature is exactly $-4$, $F_A^+$ is bounded by the spinor, $W^+\to0$ in normalized $L^2$, and $\operatorname{Ric}^{\circ}\to0$ in normalized $L^2$. Consequently the lemma applies with

\[
e_j^2\le C\sqrt{\eta_j}.
\]

The normalized fourth-power gradient budget is both one of the manuscript's established Hessian consequences and, as shown above, a consequence of the lemma's other hypotheses. Therefore the actual $|\nabla_A\Phi|^4$ is uniformly integrable in the normalized sense (2). This argument uses neither a Sobolev inequality nor noncollapse nor a pointwise Ricci bound.

### 2.1 A mixed critical term is forced to vanish

Let $\zeta=\langle\Phi,\nabla_A\Phi\rangle$. The same-solution identity gives $\fint|\zeta|^2\le C\eta$, while $|\zeta|^2\le2q$. Splitting at $q=L^2$ and applying (1) gives

\[
\boxed{
\fint |\zeta|^2|\nabla_A\Phi|^2
\le C\bigl(L^2\eta+L^{-2\varepsilon}+\sqrt\eta\bigr).}
\tag{7}
\]

In particular this tends to zero, first letting $j\to\infty$ and then $L\to\infty$. Taking $L^2=\eta^{-1/(1+\varepsilon)}$ gives the explicit rate

\[
\fint |\zeta|^2|\nabla_A\Phi|^2
\le C\bigl(\eta^{\varepsilon/(1+\varepsilon)}+\sqrt\eta\bigr).
\tag{8}
\]

This is a real restriction on a putative endpoint counterexample. It rules out any proposed global gluing mechanism requiring positive normalized mass in this particular mixed term. It also makes products of bounded, amplitude-small errors with $|\nabla_A\Phi|^4$ small. It does not automatically control arbitrary quartic energies of the *torsion derivative*, since the torsion already contains a spinor derivative.

## 3. What remains open after this estimate

The bound is obtained for the same actual solution and its fitted positive-spinor curvature, so it is not a formal curvature-budget model. Nevertheless, to conclude O10 one must insert (7) into the exact torsion equation and then prove that its remaining critical terms yield an actual incompatible identity. The error-free leading signed Maxwell pairing in the manuscript already balances to zero; making its error smaller does not create a contradiction. Nor does (1) alone give full uniform integrability of $|\nabla_A^2\Phi|^2$ or of the normalized torsion direction's fourth derivatives.

No closed O10 counterexample has been constructed here. The positive result is the vanishing of a previously only bounded spinor-current/gradient critical coupling and a sharp statement of what concentration a true counterexample may still exploit.

## 4. Elementary construction checks (secondary)

For completeness, neither pulling back a fixed metric and class through finite covers nor multiplying the metric by a constant supplies a counterexample by itself. Under a degree-$m$ cover all relevant integrals, $p,A,a^2,T$, and $V$ multiply by $m$, so normalized defects are unchanged. For constant rescaling $g\mapsto cg$,

\[
\kappa_\beta(cg)=4+\frac{2\int s_g}{cV_g}
                 +\frac{R_g+D_\beta(g,a)}{c^2V_g}.
\]

When $\int s_g<0$, minimizing over $c>0$ gives

\[
\inf_c\kappa_\beta(cg)
=4-\frac{(\int s_g)^2}{V_g(R_g+D_\beta)}.
\]

For a Kähler metric in the same orientation as the supplier, $\int w^2=\frac14\int s^2$ and the actual scalar budget $32\pi^2p\le\int s^2$ give

\[
D_\beta\ge\frac{(\beta-2)^2}{4\beta}\int s^2.
\]

Combining with $r\ge\fint(s+4)^2/4$ and minimizing the resulting quadratic function of scalar curvature pointwise yields

\[
\boxed{\kappa_\beta\ge
\frac{4(\beta-2)^2}{\beta+(\beta-2)^2}.}
\]

This excludes the usual Kähler--Einstein and product-of-curves metrics, including their constant rescalings and pulled-back coverings, from a $\beta\to\infty$, $\kappa_\beta\to0$ construction. It does not exclude non-pulled-back classes on covers, changed geometry, or the opposite orientation without separately verifying its actual supply.

## 5. A one-sided strong estimate for the torsion-length derivative

Use now the strong conclusions established in `o10_global_identity_20260929.md`: $\mathcal R=D^-_{3A}\tau\to0$ in normalized $L^2$, $m=|\tau|^2\to m_*=128/81$ in normalized $L^2$, and $\fint|\nabla\tau|^2\le C$. The torsion Weitzenböck formula is

\[
D^2\tau=\nabla^*\nabla\tau+\mathcal V\tau,
\qquad \mathcal V=-I+\tfrac32c(F_A^-).
\]

The previously established bounded determinant-curvature fit gives
$\mathcal V=\mathcal V_0+E$, $|\mathcal V_0|\le C$ and
$\fint|E|^2\to0$.

Let $h$ be bounded and Lipschitz, with $h\ge0$, $h'\ge0$, $h(m_*)=0$, and $\sup_{m\ge0}mh'(m)<\infty$. Testing the weak equation against $h(m)\tau$ is legitimate because $|D(h\tau)|\le C(|\nabla\tau|+|\mathcal R|)$. The exact identity is

\[
\begin{split}
\int h|\nabla\tau|^2+\frac12\int h'|dm|^2
+\int h\langle\mathcal V\tau,\tau\rangle
={}&\int h|\mathcal R|^2\\
&+\int\operatorname{Re}\langle\mathcal R,c(dh)\tau\rangle.
\end{split}
\tag{9}
\]

The last term is bounded by

\[
\frac14\int h'|dm|^2+C\int mh'|\mathcal R|^2=o(V)+\frac14\int h'|dm|^2.
\]

The bounded-model part of the potential term tends to zero after division by $V$, since $h(m)m\to0$ in normalized $L^1$. Its error part is bounded by

\[
\|E\|_{L^2_{\rm avg}}\,\|h(m)m\|_{L^2_{\rm avg}}\to0.
\]

Therefore

\[
\boxed{\fint h(m)|\nabla\tau|^2+
          \frac14\fint h'(m)|dm|^2\longrightarrow0.}
\tag{10}
\]

In particular take

\[
h(m)=\frac{(m-m_*)_+}{1+m},\qquad
h'(m)=\frac{1+m_*}{(1+m)^2}\mathbf1_{\{m>m_*\}}.
\]

Smooth approximations or the Sobolev chain rule justify the corner at $m_*$. Then

\[
\boxed{\fint_{\{m>m_*\}}\frac{|dm|^2}{(1+m)^2}\to0,
\qquad
\fint_{\{m>m_*+\delta\}}|\nabla\tau|^2\to0
\quad(\delta>0).}
\tag{11}
\]

Thus super-calibrated amplitude regions cannot carry a positive normalized part of the torsion derivative energy. The unresolved radial energy is on the lower-amplitude side or in an arbitrarily thin band around the calibrated mass.

The same argument cannot simply be reflected to the lower side. A nonnegative decreasing $h$ produces a **negative** $h'|dm|^2$ term. An increasing $h$ with $h(m_*)=0$ is negative below $m_*$, making $h|\nabla\tau|^2$ lose its sign. Retaining these terms is essential. The full first torsion projection $N\to0$ does not remove this problem algebraically: the manuscript's equations `proof:phase-curvature:e3.6`--`e3.8` retain a radial derivative permitted by the first projection and a commutator with derivatives of $N$. Its weak pairing still requires control of $N\nabla B$, beyond the currently proved strong $L^2$ norm of $N$.

Consequently (11) is a genuine new necessary condition for an endpoint sequence, but it is not the two-sided $dm/m\to0$ estimate requested for an Armstrong continuation.

## 6. Full first projection improves the low-amplitude Kato threshold

The full first torsion projection gives more than the Dirac trace. In a frame adapted to the positive spinor, its rows have the form

\[
N_1=(U_1-iU_2)/\sqrt2,\qquad
N_2=(-U_3+iU_4)/\sqrt2,
\quad U=\nabla\tau.
\]

Let $j=\operatorname{Im}\langle\tau,U\rangle$. Directly from these two rows, with the manuscript's convention for $J_+$,

\[
|j+\tfrac12J_+dm|^2\le2m|N|^2.
\tag{12}
\]

Moreover $|dm|^2/4+|j|^2\le m|U|^2$. Combining the two statements by Young's inequality proves, for every fixed $\delta>0$,

\[
\boxed{|dm|^2\le(2+\delta)m|U|^2+C_\delta m|N|^2.}
\tag{13}
\]

The coefficient approaches $2$, improving the Dirac-only refined Kato coefficient $3$ in dimension four. At $\Phi=0$, the cubic formula for $\tau$ gives both $\tau=0$ and $U=0$, so the estimate extends despite the absence of a preferred $J_+$ there. On $\Phi\ne0$ the displayed adapted projection is precisely the manuscript's $N$.

For $0<a<1$ and $\epsilon>0$ put

\[
h_\epsilon(m)=\left(\frac\epsilon{\epsilon+m}\right)^a.
\]

Choose $\delta>0$ so that $a(2+\delta)/2<1$. In the exact test identity (9), its decreasing derivative is compensated by (13):

\[
\int h_\epsilon|U|^2+\frac12\int h_\epsilon'|dm|^2
\ge c_a\int h_\epsilon|U|^2-C_a\int|N|^2.
\]

The Dirac test error has no adverse power of $\epsilon$:

\[
|h_\epsilon'|\sqrt m|dm||\mathcal R|
\le2a h_\epsilon |U||\mathcal R|
\le\tfrac12c_a h_\epsilon|U|^2+C_a|\mathcal R|^2.
\]

The bounded potential contributes at most $C\int h_\epsilon m$, and its $L^2$-small error tends to zero for fixed $\epsilon$, uniformly bounded by its norm times $\|m\|_{2,\mathrm{avg}}$. Since $m\to m_*$ strongly and $N,\mathcal R\to0$ strongly in normalized $L^2$, it follows that

\[
\boxed{
\limsup_j\fint h_\epsilon(m)|U|^2
\le C_a m_*\left(\frac\epsilon{\epsilon+m_*}\right)^a.}
\tag{14}
\]

On $m\le\epsilon$ the weight is at least $2^{-a}$. Therefore

\[
\boxed{
\limsup_j\fint_{\{m\le\epsilon\}}|\nabla\tau|^2
\le C_a\epsilon^a,
\qquad
\limsup_j\fint_{\{0<m\le\epsilon\}}\frac{|dm|^2}{m}
\le C_a\epsilon^a,
\quad 0<a<1.}
\tag{15}
\]

Only squared first derivatives of the torsion are controlled here. The quantity $|\nabla(\tau/\sqrt m)|^4$, or the phase-curvature squared integral at a shrinking zero, has different scaling and is not bounded by (15).

### 6.1 Why these scalar tests do not yet force two-sided length rigidity

There is an exact nonimplication check for the remaining scalar test system. It is **not** a constructed actual sequence or a counterexample to O10.

In the ideal limiting scalar tests, let $\mu$ be the amplitude-pushforward of $|U|^2dV/V$ and $\nu$ that of $|dm|^2dV/V$. The strong limits above and the calibrated potential give

\[
\int h\,d\mu+\tfrac12\int h'\,d\nu
=2m_*h(m_*),\qquad
d\nu\le2m\,d\mu.
\tag{16}
\]

For any $0<c\le4$ the nonnegative measures

\[
d\nu=c m\mathbf1_{(0,m_*)}\,dm,
\qquad
d\mu=\frac c2\mathbf1_{(0,m_*)}\,dm
+m_*(2-c/2)\delta_{m_*}
\tag{17}
\]

satisfy every identity and inequality in (16), with $\mu([0,\infty))=2m_*$. Indeed integrating $m h'$ over $(0,m_*)$ cancels the absolutely continuous $\mu$ term, leaving $2m_*h(m_*)$. The Kato inequality is equality on the lower band. Yet $\nu\ne0$.

Thus all scalar Lichnerowicz tests, the strong amplitude convergence, the correct total derivative energy, and the improved first-projection Kato inequality still permit a lower-amplitude concentration profile at the level of these necessary identities. Eliminating it requires additional differential information from the full torsion system or its global matching. Iterating only these same scalar tests cannot supply the missing conclusion.
