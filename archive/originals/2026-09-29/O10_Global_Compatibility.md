# O10: a resolvent, Hopf-form spectral gap, and the threshold 39/4

Date: 2026-09-29. This note continues the same actual O10 system. It uses the strong-current theorem proved in the preceding continuation and independently verified in `o10_counterexample_20260929.md`; it does not assert the unrestricted O10 endpoint theorem.

## 1. New conclusion

Retain the original actual conformal monopole supply, $p\ge A>0$, and $a^2\ge T_+$. Put $r=\fint|\operatorname{Ric}+g|^2$ and $\kappa_\beta=r+D_\beta/V$; in the exact $s=-4$ representative, $r=P/V$. There exist absolute numbers $\eta_*>0$ and $\delta_*>0$ such that these actual scalar-minus-four O10 inputs satisfy, for $\beta\ge4$,

\[
\boxed{\kappa_\beta+\beta^{-2}+
\left(\fint|W^-|^2-\frac{50}{3}\right)_+\ge\eta_*.}
\tag{1}
\]

There is no Euler-density hypothesis in (1). Consequently, after the manuscript's exact Yamabe transfer and combination with its finite-parameter estimate, the requested O10 endpoint inequality holds whenever

\[
\boxed{\chi(M)/A\le39/4+\delta_* .}
\tag{1a}
\]

In particular the density threshold $39/4$, including equality and a fixed positive margin, is excluded for every hypothetical O10 escape sequence. The constants are existential; no optimal margin is claimed. The full problem for arbitrary fixed $B$ remains open.

The mechanism is a global elliptic regularization of the actual opposite spinor. It turns the previously unavailable derivative information into a bounded smooth section to which both a slow-gradient truncation estimate and a rank-two characteristic-class localization apply. It does not assume that the original torsion has a fourth-power derivative bound.

## 2. Starting data and topology

Use the exact Yamabe reduction and the same constant-weight actual solution of the manuscript:

\[
s=-4,\quad D_A\Phi=0,\quad F_A^+=2i\sigma(\Phi),
\quad \rho=|\Phi|^2\le2,
\quad \beta_j\to\infty,\quad \kappa_{\beta_j}\to0.
\]

Set $\tau=t_\Phi\in E_-=S^-\otimes L$, $m=|\tau|^2$, $m_*=128/81$, and $U=\nabla_{3A}\tau$. The previously proved strong-current continuation supplies

\[
\|D^-_{3A}\tau\|_{2,\mathrm{avg}}\to0,
\quad \|m-m_*\|_{2,\mathrm{avg}}\to0,
\quad \fint|U|^2\le C,\qquad
N_\tau\to0\text{ in normalized }L^2,
\tag{2}
\]

and the upper-amplitude test proved in `o10_counterexample_20260929.md`, Section 5, gives

\[
\fint_{\{m>m_*+d\}}|U|^2\to0\qquad(d>0).
\tag{3}
\]

The same actual determinant curvature has a bounded ASD fit $K$:

\[
f=-iF_A^-,\quad Q=-iq_-(\tau),\quad
S=m_*+2\rho^2|\nabla_A\Phi|^2,
\quad K=-\frac98\frac{\rho^3Q}{S},
\quad |K|\le C,\quad\|f-K\|_{2,\mathrm{avg}}\to0.
\tag{4}
\]

The original same-solution formulas imply

\[
\frac pV\to\frac{2}{9\pi^2},\quad
\frac{T_+}{V}\to\frac1{6\pi^2},\quad
\frac{a^2-T_+}{V}\to0,
\quad \fint|W^+|^2\to0,
\quad \fint|\operatorname{Ric}+g|^2\to0.
\tag{5}
\]

Write $b_j=\fint|W^-|^2$. Chern--Gauss--Bonnet gives

\[
\frac{\chi}{V}=\frac1{12\pi^2}+\frac{b_j}{8\pi^2}+o(1).
\tag{6}
\]

Since $A\le p$ and $\chi>0$ eventually, the assumption $\chi/A\le B$ implies

\[
\limsup_j b_j\le\frac{16}{9}B-\frac23.
\tag{7}
\]

The primary proof of (1) needs no such assumption: failure of (1) would itself give an escape with $b_j\le50/3+o(1)$.

For the actual opposite-spinor bundle,

\[
c_2(E_-)[M]=5\chi+6\tau+\frac94(a^2-T_+)
=\chi+2T_++\frac94(a^2-T_+).
\]

Thus

\[
\boxed{\frac{c_2(E_-)[M]}V
=\frac5{12\pi^2}+\frac{b_j}{8\pi^2}+o(1).}
\tag{8}
\]

This is the positive characteristic density to be contradicted.

## 3. Bounded truncation of the actual torsion

Choose a fixed $R>m_*$ and a smooth function $\vartheta(m)$ equal to one for $m\le R$, with $\vartheta(m)\sqrt m$ bounded and
$|\vartheta|+m|\vartheta'|\le C$. Arrange that all changes occur in $m>R$. Define

\[
u=\vartheta(m)\tau.
\]

Then $u$ is uniformly bounded. By (2)--(3), the chain rule, and
$|dm|\le2\sqrt m|U|$,

\[
\|u-\tau\|_{H^1_{\mathrm{avg}}}\to0,
\quad\|D^-_{3A}u\|_{2,\mathrm{avg}}\to0,
\quad |u|^2\to m_*\text{ in normalized }L^2.
\tag{9}
\]

The torsion Dirac square is

\[
D^2=\nabla^*\nabla+\mathcal V,
\qquad \mathcal V=-I+\frac32c(F_A^-).
\]

The bounded fit (4), the strong mass limits, and the Clifford identity for the quadratic map show that

\[
\boxed{\|(\mathcal V+2I)u\|_{2,\mathrm{avg}}\to0.}
\tag{10}
\]

Here the determinant-curvature error acts on the **bounded** section $u$. For its bounded model the coefficient acting on the line of $\tau$ tends to $-2$; the orthogonal component of the fit error is already small. This step must not be applied directly to unbounded $\tau$ using only two independent $L^2$ bounds.

## 4. Resolvent regularization

Let $\mathcal L=\nabla^*\nabla$ on $E_-$. Define the smooth section

\[
v=3(1+\mathcal L)^{-1}u.
\tag{11}
\]

The inverse exists on every closed manifold, without a spectral-gap assumption beyond the added identity. The scalar maximum principle applied to $|v|^2$ at its maximum gives

\[
\|v\|_\infty\le3\|u\|_\infty,
\qquad \mathcal Lv=3u-v=:f_v,
\qquad \|f_v\|_\infty\le C.
\tag{12}
\]

Moreover

\[
(\mathcal L-2)u=D^*(Du)-(\mathcal V+2)u\to0
\quad\hbox{in normalized }H^{-1}.
\]

Testing
$(1+\mathcal L)(v-u)=-(\mathcal L-2)u$
against $v-u$ yields, by Cauchy--Schwarz and the pointwise Clifford estimate $|Dw|\le2|\nabla w|$,

\[
\boxed{\|v-u\|_{H^1_{\mathrm{avg}}}\to0.}
\tag{13}
\]

Consequently $|v|^2\to m_*$ in normalized measure and in every finite normalized $L^p$, since $u,v$ are uniformly bounded. Moreover

\[
\|v-\tau\|_{H^1_{\rm avg}}\to0,\qquad
\|Dv\|_{2,\rm avg}\to0,\qquad
\|(\mathcal L-2)v\|_{2,\rm avg}=3\|u-v\|_{2,\rm avg}\to0.
\tag{13a}
\]

This construction is global; it introduces neither charts nor a noncollapse hypothesis.

## 5. Unweighted second-derivative budget: bounded opposite Weyl is enough

Initially assume only $b_j\le B_0$ for one fixed finite number. The full curvature of $E_-$ is the sum of the opposite Levi-Civita block and determinant curvature $3F_A/2$. Therefore

\[
\fint\bigl(|F^{E_-}|^2+|\operatorname{Ric}|^2\bigr)\le C(B_0).
\tag{14}
\]

For a bounded section with bounded rough Laplacian, the derivative-free Hessian interchange and bounded-section interpolation imply

\[
\boxed{\fint\bigl(|\nabla^2v|^2+|\nabla v|^4\bigr)\le C(B_0).}
\tag{15}
\]

Here is the relevant proof structure, which makes clear that no Sobolev constant occurs. Write $P_i=\nabla_i v$ and $H_{ij}=\nabla_iP_j$. Since $H_{ij}-H_{ji}=F_{ij}v$,

\[
\int|H|^2=\int\langle H_{ij},H_{ji}\rangle
 +\frac12\int\sum_{i,j}|F_{ij}v|^2.
\]

Integrating the cross term by parts and commuting derivatives on $P$ introduces only $\operatorname{Ric}*P$ and $F*P$. The forcing term becomes $\int|\mathcal Lv|^2$. Thus

\[
\int|H|^2\le C V+C\int(|\operatorname{Ric}|+|F|)|P|^2.
\]

Integration of $\operatorname{div}(|P|^2\operatorname{Re}\langle v,P\rangle)$, using bounded $v$ and $\mathcal Lv$, gives

\[
\int|P|^4\le C\int|H|^2+CV.
\]

Cauchy--Schwarz and Young absorb the resulting term of size
$C\bigl(\int(|\operatorname{Ric}|^2+|F|^2)\bigr)^{1/2}
\bigl(\int|P|^4\bigr)^{1/2}$ and prove (15). This is an ordinary bound, not uniform integrability of $|\nabla v|^4$.

## 6. Resolvent mass, phase, and Hopf-form identities

Use different symbols from the topological class $a$:

\[
 a_v=|v|^2,\qquad q_v=|\nabla v|^2,\qquad
 j_v=\operatorname{Im}\langle v,\nabla v\rangle,
 \qquad Q_v=-iq_-(v).
\]

Choose the nonnegative scalar Laplacian. Then

\[
 \Delta a_v=2\operatorname{Re}\langle\mathcal Lv,v\rangle-2q_v.
\]

Its normalized $L^2$ norm is bounded by (12), (15). Since
$a_v-m_*\to0$ in normalized $L^2$, integration against $a_v-m_*$ gives

\[
 \boxed{\fint|da_v|^2
 =\fint(a_v-m_*)\Delta a_v\longrightarrow0.}
\tag{16}
\]

On the set where the positive spinor defines its almost-complex structure $J_+$, let $N_v$ denote the same complete first projection of $\nabla v$ as in the actual torsion identity. The projection has bounded operator norm, so strong $H^1$ closeness in (13a) and $N_\tau\to0$ imply $N_v\to0$ in normalized $L^2$. One may first restrict to $\rho\ge c>0$; its omitted set has vanishing relative volume and (15) makes its $\nabla v$ square integral vanish. No derivative of $J_+$ is used here.

The exact frame identity is

\[
 \left|j_v+\frac12J_+da_v\right|^2\le2a_v|N_v|^2.
\tag{17}
\]

As $v$ is bounded, (16)--(17) yield $j_v\to0$ in normalized $L^2$. The contribution on the omitted low-$\rho$ set also vanishes by (15). Furthermore (13a), integration by parts, and (15) give

\[
 \fint q_v\longrightarrow2m_*,\qquad
 \fint a_vq_v\longrightarrow2m_*^2.
\tag{18}
\]

The second assertion uses
$\bigl|\fint(a_v-m_*)q_v\bigr|
\le\|a_v-m_*\|_{2,\rm avg}\|q_v\|_{2,\rm avg}\to0$.

For the manuscript's quadratic-map normalization the exact identities are

\[
 |Q_v|^2=\frac{a_v^2}{8},\qquad
 |\nabla Q_v|^2=\frac{a_v}{2}|\nabla v|^2-\frac12|j_v|^2,
\tag{19}
\]

\[
 \delta Q_v=-\frac12j_v+E_v,
 \qquad |E_v|^2\le\frac14a_v|Dv|^2.
\tag{20}
\]

For example, the gradient identity follows at $v=\sqrt{a_v}(1,0)$ by splitting each derivative into the radial, phase, and orthogonal complex components; the phase component contributes zero to the Hopf derivative. Consequently

\[
 \fint|Q_v|^2\to\frac{m_*^2}{8},\quad
 \fint|\nabla Q_v|^2\to m_*^2,\quad
 \|\delta Q_v\|_{2,\rm avg}+\|dQ_v\|_{2,\rm avg}\to0.
\tag{21}
\]

The last equality for $dQ_v$ uses anti-self-duality, not an additional field equation.

## 7. The sharp opposite-Weyl threshold is 50/3

The two-form Weitzenböck identity, with $s=-4$ and anti-self-dual $Q_v$, reads

\[
 \int\bigl(|dQ_v|^2+|\delta Q_v|^2\bigr)
 =\int|\nabla Q_v|^2-\frac43\int|Q_v|^2
          -2\int\langle W^-Q_v,Q_v\rangle.
\]

Substitution of (21) gives the exact asymptotic pairing

\[
 \boxed{\fint\langle W^-Q_v,Q_v\rangle
          \longrightarrow\frac{5m_*^2}{12}.}
\tag{22}
\]

For any tracefree symmetric endomorphism $W$ of a three-dimensional Euclidean space,

\[
 \langle WQ,Q\rangle\le\sqrt{\frac23}|W|\,|Q|^2.
\]

Since $v$ is bounded and $a_v\to m_*$ in every finite normalized $L^p$,
$\fint|Q_v|^4\to m_*^4/64$. Cauchy--Schwarz in (22) gives

\[
 \left(\frac{5m_*^2}{12}\right)^2
 \le\frac23\liminf_j b_j\,\frac{m_*^4}{64},
 \qquad
 \boxed{\liminf_j b_j\ge\frac{50}{3}.}
\tag{23}
\]

Using (5)--(6), this also says

\[
 \frac\chi p=\frac38+\frac9{16}b_j+o(1),\qquad
 \boxed{\liminf_j\frac\chi A\ge\frac{39}{4}.}
\tag{24}
\]

The constants are exact in the manuscript's operator norm on $W^-$. This step only uses the unweighted estimate (15). It does **not** use a prior assumption that the full curvature of $E_-$ has a bounded model with a vanishing error.

## 8. Equality produces a bounded curvature model, hence is impossible

Put $q_0^2=m_*^2/8$. Define a globally smooth tracefree symmetric endomorphism of $\Lambda^-$ by the polynomial formula

\[
 \boxed{W_0=\frac5{q_0^2}
 \left(Q_v\otimes Q_v-\frac{|Q_v|^2}{3}I\right).}
\tag{25}
\]

Unlike the expression using $Q_v/|Q_v|$, this has no singularity at zeros. It is uniformly bounded because $v$ is uniformly bounded. The elementary identities

\[
 \left|Q\otimes Q-\frac{|Q|^2}{3}I\right|^2
       =\frac23|Q|^4,
 \quad
 \langle W,Q\otimes Q-\frac{|Q|^2}{3}I\rangle
       =\langle WQ,Q\rangle
\]

and (22) imply

\[
 \fint|W_0|^2\longrightarrow\frac{50}{3},\qquad
 \fint\langle W^-,W_0\rangle\longrightarrow\frac{50}{3}.
\tag{26}
\]

Thus the exact defect relation is

\[
 \boxed{\fint|W^--W_0|^2=b_j-\frac{50}{3}+o(1).}
\tag{27}
\]

Suppose now $b_j\le50/3+o(1)$, as would follow from failure of (1). The full curvature of $E_-$ has a bounded model: include $W_0$, the scalar block, and the bounded determinant fit (4). All remaining terms converge to zero in normalized $L^2$, by (5), (27). Therefore

\[
 F^{E_-}=F_0+\mathcal E_F,\qquad
 |F_0|\le C,\qquad\|\mathcal E_F\|_{2,\rm avg}\to0.
\tag{28}
\]

This is the point at which the full bounded curvature model becomes available. Its derivatives are never used.

For completeness, apply the slow-gradient estimate to the bounded section $v$ with bounded forcing $\mathcal Lv=f_v$. For

\[
 w=\left(\frac{q_v+\epsilon_0}{L^2+q_v+\epsilon_0}\right)^\varepsilon,
 \qquad0<\varepsilon\ll1,
\]

one has $|dw|\sqrt{q_v}\le2\varepsilon w|\nabla^2v|$. The derivative-free Hessian interchange used in Section 5 now gives weighted estimates. The only forcing term to check is

\[
 \int w\langle\nabla v,\nabla f_v\rangle
 =\int w|f_v|^2-\int\langle dw\otimes\nabla v,f_v\rangle.
\]

The last term is absorbed by Young's inequality and small fixed $\varepsilon$. Weighted bounded-section interpolation follows by integrating
$\operatorname{div}(wq_v\operatorname{Re}\langle v,\nabla v\rangle)$.
After the error terms from (28) are absorbed using Cauchy--Schwarz and Young, and $\epsilon_0\downarrow0$, one obtains

\[
 \fint w\bigl(|\nabla^2v|^2+|\nabla v|^4\bigr)
 \le C L^{-2\varepsilon}+C\|\mathcal E_F\|_{2,\rm avg}^2
       +C\|\operatorname{Ric}+g\|_{2,\rm avg}^2.
\tag{29}
\]

Here $\fint w\le L^{-2\varepsilon}\fint q_v^\varepsilon
\le CL^{-2\varepsilon}$, by the bounded first-gradient energy. Neither derivatives of $f_v$ nor derivatives of $F_0$ occur in the resulting inequality.

Splitting at $|\nabla v|=L$ shows that $|\nabla v|^4$ is uniformly integrable with respect to normalized volume. Equation (28) likewise makes $|F^{E_-}|^2$ uniformly integrable. In particular, for every sequence $Z_j$ with $\operatorname{Vol}(Z_j)/V_j\to0$,

\[
 \fint_{Z_j}|\nabla v|^4\to0,\qquad
 \fint_{Z_j}|F^{E_-}|^2\to0.
\tag{30}
\]

## 9. Characteristic localization gives the contradiction

Fix $0<a_0<b_0<m_*$. On the complement of the zero set of $v$, the unit section $\widehat v=v/|v|$ splits the rank-two complex bundle into a trivial line and its orthogonal line. The connection making $\widehat v$ parallel has zero second Chern form. Its transgression to the given connection can be chosen with

\[
 dT_v=c_2(F^{E_-}),\qquad
 |T_v|\le C\bigl(|F^{E_-}|\,|\nabla\widehat v|
                              +|\nabla\widehat v|^3\bigr).
\]

Take $\chi(a_v)=1$ for $a_v\le a_0$ and $\chi(a_v)=0$ for $a_v\ge b_0$. Stokes, with the transgression supported away from zeros, gives

\[
 c_2(E_-)[M]=\int\chi\,c_2(F^{E_-})+
                          \int d\chi\wedge T_v.
\]

All inverse powers of $|v|$ in the transition term are bounded by the fixed lower threshold $a_0$. Young's inequality on its mixed term yields

\[
 \boxed{|c_2(E_-)[M]|
 \le C\int_{\{a_v<b_0\}}|F^{E_-}|^2
       +C\int_{\{a_0<a_v<b_0\}}|\nabla v|^4.}
\tag{31}
\]

Both supports have vanishing relative volume because $a_v\to m_*$ in measure. By (30), $c_2(E_-)[M]/V\to0$. But (8), (23), and $b_j\le50/3+o(1)$ give

\[
 \boxed{\frac{c_2(E_-)[M]}V\longrightarrow
 \frac5{12\pi^2}+\frac{50/3}{8\pi^2}
 =\frac5{2\pi^2}>0.}
\tag{32}
\]

This contradiction excludes the critical opposite-Weyl endpoint sequence.

If the universal inequality (1) were false, choosing its left side tending to zero would give exactly the excluded sequence. Therefore an absolute $\eta_*>0$ exists. This compactness-of-numbers argument proves a positive margin without claiming a numerical value.

For the Euler-density corollary, an escape with $\chi/A\le39/4+\delta$ would satisfy, by (7),

\[
 \limsup b_j\le\frac{50}{3}+\frac{16}{9}\delta.
\]

Choosing $\delta_*>0$ with $(16/9)\delta_*<\eta_*$ contradicts (1) along such an escape. The manuscript's already proved finite-parameter estimate covers bounded $\beta$ and the vanishing factor at $\beta=2$. Its exact Yamabe comparison then returns the O10 inequality for the original admissible metrics. No unproved general compactness theorem is inserted in this last step.

## 10. Source dependencies and exact scope

The logical dependencies, kept separate from the new calculations, are:

| Input | Source and role |
|---|---|
| O10 system, exact Yamabe comparison, finite-parameter gap | Integrated manuscript, Section 25 and its cited single-parameter analysis. These supply the normalized escape reduction and the transfer back. |
| Same-solution bounded ASD fit | Integrated manuscript, formula labelled `proof:single-parameter:e2.14a` (around lines 2390–2415 in the uploaded source). No independent determinant connection is chosen. |
| Torsion Dirac and Lichnerowicz formulas | Integrated manuscript, around lines 28273–28583. The potential has the opposite-monopole sign; it is not positive. |
| Complete first projection and phase identity | Integrated manuscript, around lines 29358 and 32611. Both components of the first projection are needed in (17). |
| Hopf codifferential identity | Integrated manuscript, around line 32482. Section 6 additionally writes out the full gradient identity with the same normalization. |
| Strong current, mass, and first-projection convergence | `o10_global_identity_20260929.md`, its strong-current continuation, and independent checks in `o10_counterexample_20260929.md`. This is the new September 29 prerequisite, not an assumption from the original manuscript. |
| Upper-amplitude torsion-gradient vanishing | `o10_counterexample_20260929.md`, Section 5; its complete monotone-test proof is also incorporated in `O10_Strengthened_Endpoint.md`, Section 3. |
| Slow-gradient lemma | `o10_counterexample_20260929.md`, Sections 1–3; Sections 5 and 8 above supply its bounded-forcing adaptation. |
| New part of this note | Resolvent regularization, mass/phase reduction, the sharp $50/3$ pairing, polynomial model at equality, and the characteristic contradiction at $39/4$. |

All statements use the curvature norms and Clifford normalization of the integrated manuscript. The completed result is a density range reaching strictly beyond $39/4$. It is not a proof for arbitrary fixed $B$, not a closed-manifold escape construction, and not an unconditional solution of O10. The resolvent is an auxiliary section of the actual bundle, not a replacement for the original actual-field supply.

For unrestricted $B$, a hypothetical escape must now have a definite excess above $50/3$ in opposite-Weyl energy. Its curvature need not be a bounded model plus a vanishing $L^2$ error, so (30) is no longer available from this proof. That is a precise remaining obstruction, rather than a missing fourth-power estimate for the original torsion alone.
