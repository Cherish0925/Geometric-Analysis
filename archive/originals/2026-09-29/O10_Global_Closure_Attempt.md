# Unrestricted O10: exact amplitude-defect law and a test of the proposed shortcut

Date: 2026-09-29 UTC. This is a research audit of the remaining unrestricted problem. It does not establish the unrestricted O10 gap, a new decay-rate improvement, or an actual counterexample to O10. It preserves the finite-density theorem and the already established quantitative continuations.

## 1. What was tested

The attempted route was to remove the dependence on the negative-spinor Hessian by using only the bounded auxiliary section, its bounded rough Laplacian, and the nearly constant amplitude. These hypotheses hold without an opposite-Weyl bound. They give
\[
 |v_j|+|L_jv_j|\le C,\qquad L_jv_j-2v_j\to0\text{ in }L^2_{\rm av},
 \qquad m_j=|v_j|^2\to m_*={128\over81}\text{ in }L^2_{\rm av}.
\]
Set \(q_j=|\nabla v_j|^2\). Then
\[
 \Delta m_j=4m_j-2q_j+r_j,\quad \|r_j\|_{2,\rm av}\to0,
 \quad \fint q_j\to2m_*,\quad |dm_j|^2\le4m_jq_j.
 \tag{1}
\]
The pointwise upper bound \(\Delta m_j\le C\) is also available. Here \(\Delta=d^*d\), so \(\int f\Delta f=\int|df|^2\).

An argument that (1), bounded Ricci curvature in mean, and amplitude convergence automatically imply \(dm_j\to0\) would close an important missing step. Such an argument is not valid. Sections 2–3 identify precisely what those scalar statements still permit, on a fixed flat geometry.

## 2. The exact defect law retains a positive radial measure

The amplitudes lie in a fixed interval \([0,M]\). Define positive measures on that interval by
\[
 \mu_j(B)=\fint_{\{m_j\in B\}}|dm_j|^2,
 \qquad \nu_j(B)=\fint_{\{m_j\in B\}}q_j.
\]
Their total masses are uniformly bounded, by (1). Pass to weakly convergent subsequences \(\mu_j\rightharpoonup\mu\), \(\nu_j\rightharpoonup\nu\). For every \(f\in C^1([0,M])\), the scalar equation tested with \(f(m_j)\) gives
\[
 \int f'(t)\,d\mu(t)
 =4m_*f(m_*)-2\int f(t)\,d\nu(t).
 \tag{2}
\]
Consequently
\[
 \mu'=2\nu-4m_*\delta_{m_*}
 \tag{3}
\]
as distributions after extension by zero outside \([0,M]\). In particular \(\nu([0,M])=2m_*\). The upper-amplitude estimate from the preceding continuation shows that \(\mu\) is supported in \([0,m_*]\); it does not make \(\mu\) vanish there.

These statements are not merely a technical failure of one estimate. The measures
\[
 d\mu(t)=4t\,\mathbf1_{(0,m_*)}(t)\,dt,
 \qquad d\nu(t)=2\,\mathbf1_{(0,m_*)}(t)\,dt
 \tag{4}
\]
satisfy (2)–(3), including the endpoint atom of the distributional derivative, and satisfy the Kato bound \(d\mu\le4t\,d\nu\). They even satisfy the stronger radial coefficient equality \(d\mu=2t\,d\nu\) occurring in the formal exact first-jet model with no surviving \(c\)-component. Thus the entire mean gradient energy can be carried by lower-amplitude radial concentration without contradicting these scalar identities.

Equation (4) is a measure-level consistency test, not an actual field construction. In particular it does not establish the full equations \(N_v\simeq0\), \(D^-v\simeq0\), or the Levi-Civita realization of the connection.

## 3. A fixed flat scalar realization of the amplitude-concentration phenomenon

Here is a more concrete check: all the scalar features of (1) except their realization as the covariant derivatives of an actual O10 spinor can occur on a fixed flat four-torus. This prevents the scalar-amplitude shortcut even under excellent base geometry.

Let \(\varphi\ge0\) be smooth, supported in a small Euclidean ball, with integral one. On the unit flat torus let
\[
 \rho_\delta(y)=\delta^{-4}\varphi(y/\delta),\qquad
 \Delta U_\delta=\rho_\delta-1,\qquad\int U_\delta=0.
\]
Write \(G\) for the mean-zero torus Green function. Locally \(G(y)=c_4|y|^{-2}+O(1)\), and away from its pole \(G\) is smooth. Hence, directly from convolution with \(\rho_\delta\),
\[
 -C_0\le U_\delta\le C_1\delta^{-2},\qquad
 \int U_\delta^2\le C_2(1+|\log\delta|),
 \tag{5}
\]
and
\[
 \int|dU_\delta|^2=\int U_\delta\rho_\delta
 =c_\varphi\delta^{-2}+O(1),\qquad c_\varphi>0.
 \tag{6}
\]
The last coefficient is the positive Euclidean Newtonian self-energy of \(\varphi\); the mean-zero condition removes the constant term in the source.

Take \(\varepsilon=1/n\), put \(\delta=\varepsilon\), and define an \(\varepsilon\)-periodic function on the unit torus by
\[
 u_\varepsilon(x)=a\varepsilon^2\bigl(U_\varepsilon(x/\varepsilon)+C_0\bigr).
 \tag{7}
\]
Choose the fixed \(a>0\) small enough that \(0\le u_\varepsilon\le1/4\) for all sufficiently small \(\varepsilon\), and also \(a\le1\). The scaling and (5)–(6) give
\[
 u_\varepsilon\to0\text{ in }L^2,\quad
 \int|du_\varepsilon|^2\to a^2c_\varphi>0,\quad
 \Delta u_\varepsilon=a\bigl(\rho_\varepsilon(x/\varepsilon)-1\bigr)\ge-a.
 \tag{8}
\]
Define
\[
 m_\varepsilon=m_*(1-u_\varepsilon)^2,\qquad
 q_\varepsilon=2m_\varepsilon-\frac12\Delta m_\varepsilon.
 \tag{9}
\]
For the positive Laplacian,
\[
 \Delta m_\varepsilon
 =-2m_*(1-u_\varepsilon)\Delta u_\varepsilon
   -2m_*|du_\varepsilon|^2\le2am_*.
\]
Moreover
\[
 q_\varepsilon
 =2m_*(1-u_\varepsilon)^2
 +m_*(1-u_\varepsilon)\Delta u_\varepsilon
 +m_*|du_\varepsilon|^2
 \ge m_*|du_\varepsilon|^2
 =\frac{|dm_\varepsilon|^2}{4m_\varepsilon},
 \tag{10}
\]
because \(2(1-u_\varepsilon)-a\ge1/2\). Thus
\[
 m_\varepsilon\to m_*\text{ in }L^2,\quad
 \fint q_\varepsilon=2\fint m_\varepsilon\to2m_*,\quad
 \liminf\int|dm_\varepsilon|^2>0,
 \tag{11}
\]
while \(m_\varepsilon\) is bounded above and uniformly bounded away from zero, and \(\Delta m_\varepsilon\le C\). The base is one fixed flat torus: no collapsing coordinates or unbounded Ricci curvature are used.

Each cell has diameter \(\varepsilon\), and the source core has physical radius \(\varepsilon^2\). There are \(\varepsilon^{-4}\) cells. The four-dimensional capacities of the cores therefore have order
\[
 \varepsilon^{-4}(\varepsilon^2)^2\asymp1,
\]
whereas their total volume has order \(\varepsilon^{-4}(\varepsilon^2)^4=\varepsilon^4\to0\). This accounts for the coexistence of nearly constant amplitude and nonvanishing radial energy.

**Scope:** \(q_\varepsilon\) is a nonnegative scalar energy density satisfying the amplitude equation and Kato constraint. This construction does not claim \(q_\varepsilon=|\nabla v_\varepsilon|^2\) for the required spinor and spin connection. It is not an O10 counterexample. Its purpose is to rule out deducing the missing radial estimate from scalar amplitude/Laplacian information alone.

## 4. What the full actual equations would have to add

The inherited first projection and Dirac equation yield, on a positive-amplitude adapted frame and with their small errors retained,
\[
 q_{\rm ph}=-\frac{J_+dm}{2m},\qquad
 b=d\theta_1+c\theta_2,\qquad
 d=-\frac{m_3+im_4}{2m}.
\]
The exact positive-curvature Cartan equation cancels the displayed radial term; it does not imply \(d\to0\). This cancellation was verified in the preceding continuation and is not re-counted as a new result here.

A proposed nonintegrability route uses \([\nabla_{Z_1},\nabla_{Z_2}]v\), whose relevant curvature component contains Ricci rather than uncontrolled \(W^-\). The small first projection yields a weak differentiated constraint. Turning it into an \(L^2\) estimate for the missing derivative requires pairing a small first-order quantity with a derivative of the test. The currently available test involves \(\nabla^2v\) or products with \(\nabla v\); their control is precisely what grows with opposite-Weyl energy. Merely invoking the bracket identity or local exact almost-Kähler rigidity does not bound that pairing on the degenerating sequence.

No new estimate obtained in this attempt eliminates the measure \(\mu\), controls the required bracket test without the missing integrability, or constructs a closed actual escape. The precise remaining question is whether the full positive-spinor/Levi-Civita equations force this capacity defect to vanish or force it to pay a nonzero amount of the original O10 residual. A proof from the scalar consequences alone is excluded by Section 3.

## 5. A genuine estimate from the full section equation: small coefficients multiply the gradient in L2

There is additional uniform information, beyond the scalar defect law. Let \(e\) be any smooth section of any metric bundle (a scalar or a one-form is allowed), and let \(v\) be the actual bounded auxiliary section with \(|v|+|Lv|\le C\). Then
\[
 \boxed{\fint |e|^2|\nabla v|^2
 \le C\fint\bigl(|e|^2+|\nabla e|^2\bigr).}
 \tag{12}
\]
The constant depends only on the bounds for \(v,Lv\). It contains no opposite-Weyl bound and no Sobolev constant. Indeed test \(Lv\) by \(|e|^2v\):
\[
 \int |e|^2|\nabla v|^2
 =\operatorname{Re}\int |e|^2\langle Lv,v\rangle
 -\operatorname{Re}\int \langle d|e|^2\otimes v,\nabla v\rangle.
\]
Use \(|d|e|^2|\le2|e||\nabla e|\) and absorb half of the left side by Young. The argument is valid without an a priori pointwise bound on \(e\).

The inherited strong-current estimate has \(\zeta\to0\) in normalized \(H^1\). Thus the actual system gives
\[
 \boxed{\|\zeta\,\nabla v\|_{2,\mathrm{av}}\to0.}
 \tag{13}
\]
This is stronger than the naive product estimate \(L^4\cdot L^2\subset L^{4/3}\). Similarly, whenever an actual resolvent/cap error \(e\to0\) in \(H^1\), one obtains \(e\nabla v\to0\) in \(L^2\).

Consequently, for a line-bundle test section \(w\) with \(\|\nabla^2w\|_2\le C\), terms of the form
\[
 \fint C_0*(\zeta\nabla v)*\nabla^2w
\]
tend to zero whenever the tensor coefficient \(C_0\) is uniformly bounded. This removes one genuine weak-test product obstruction without controlling \(\nabla^2v\).

### A second use of Caccioppoli removes the previously problematic differentiated-current tests

Suppose the line-bundle test satisfies
\[
 |w|+|\nabla^*\nabla w|\le C,
 \qquad \|\nabla w\|_2+\|\nabla^2w\|_2\le C.
\]
These are the existing bounded-forcing positive line-resolvent bounds, independent of opposite-Weyl energy. Apply (12) with \(e=\nabla w\), using Kato for the scalar norm. This gives the genuinely uniform product estimate
\[
 \boxed{\|\,|\nabla v|\,|\nabla w|\,\|_2\le C.}
 \tag{14}
\]
Although neither factor has a uniform pointwise bound, their product is controlled in \(L^2\). Similarly apply Caccioppoli to the bounded line section \(w\) with \(e=\nabla\Phi\). The inherited positive-spinor Hessian bound yields
\[
 \boxed{\|\,|\nabla\Phi|\,|\nabla w|\,\|_2\le C.}
 \tag{15}
\]

For a bounded tensor coefficient \(C^{iajk}\) satisfying
\[
 |\nabla C|\le C_0(1+|\nabla\Phi|+|\nabla v|),
\]
integrating the representative differentiated-current pairing by parts gives
\[
 \begin{split}
 \int C^{iajk}(\nabla_i\zeta_a)
                  \langle\nabla_jv,\nabla_kw\rangle
 ={}&-\int\zeta_a C^{iajk}
               \langle\nabla_i\nabla_jv,\nabla_kw\rangle\\
 &-\int\zeta_a C^{iajk}
               \langle\nabla_jv,\nabla_i\nabla_kw\rangle\\
 &-\int\zeta_a(\nabla_iC^{iajk})
               \langle\nabla_jv,\nabla_kw\rangle.
 \end{split}
 \tag{16}
\]
The left side tends to zero by \(\|\nabla\zeta\|_2\to0\) and (14). The second line tends to zero by (13) and the test Hessian bound. The third line tends to zero by (13) paired with (14)–(15). Thus **the first line, including its symmetric Hessian component, tends to zero as well**. No alternating-index assertion or negative-spinor Hessian estimate is needed. All integrations are divided by the actual volume.

More explicitly, each such pairing is bounded by a fixed constant times
\[
 \|\nabla\zeta\|_2+\|\zeta\|_{H^1},
\]
with the displayed test/coefficient budgets fixed. If the inherited current estimate is \(\|\zeta\|_{H^1}=O(x^\gamma)\), this argument keeps the same exponent; no factor involving \(b\) is introduced.

This repairs a real testing obstruction. It must not be overstated: the estimate for \(C\) is to be checked for the full tensor and every cutoff. A coefficient involving a fixed smooth amplitude cutoff has such a derivative bound on its support. It does not justify dividing by an uncontrolled amplitude without that cutoff.

### Linear weak radial tests also vanish, without strong radial convergence

Let \(C=C(v,\Phi)\) be a uniformly bounded contraction tensor, with
\[
 |\nabla C|\le C_0(1+|\nabla v|+|\nabla\Phi|).
\]
Then, for every line-resolvent test \(w\) obeying the bounds above,
\[
 \boxed{\left|\fint dm*C*\nabla w\right|
 \le C\|m-m_*\|_2\to0.}
 \tag{17}
\]
Indeed integration by parts rewrites the integral as
\[
 -\fint(m-m_*)\bigl(C*\nabla^2w+(\nabla C)*\nabla w\bigr).
\]
The bracket is uniformly \(L^2\) by the test Hessian bound and (14)–(15). The same conclusion permits smooth fixed lower-amplitude cutoffs in \(C\): derivatives of such cutoffs are bounded by fixed multiples of \(|\nabla v|+|\nabla\Phi|\), so their transition errors are already included in this calculation.

This is a useful weak radial cancellation, but the order of the test is essential. It does **not** justify discarding
\[
 \fint dm*(\nabla v)*\nabla w
 \quad\hbox{or}\quad
 \fint dm*C*\nabla^2w.
 \tag{18}
\]
Moving the derivative in the first expression introduces \((m-m_*)\nabla^2v\nabla w\); moving it in the second introduces third derivatives of \(w\). Neither has been controlled here. In particular (17) is not strong \(L^2\) convergence of \(dm\), and it does not yet remove the radial-square mass in the full Cartan system.

### What remains after this repair

The unrestricted first-jet reduction still has the radial coefficient
\[
 d=-\frac{m_3+i m_4}{2m}
\]
and the phase current \(-J_+dm/(2m)\). Neither is known to be \(L^2\)-small. Formula (12) cannot be invoked with \(e=m-m_*\) as a small coefficient: that would require the unknown smallness of \(dm\). The surviving first-jet norm is
\[
 |\nabla v|^2=\frac{E_1+2E_2}{2m}+2m|c|^2,
 \qquad E_1=m_1^2+m_2^2,\quad E_2=m_3^2+m_4^2.
\]
Thus the fixed total gradient mass does not yet produce a fixed nonzero mass for the fifth-line coefficient \(c\). If this radial concentration is not first eliminated, the nonnegative contribution \((E_1+2E_2)/(2m)\) may consume the mass used by the finite-density contradiction.

Nor does the bounded-test estimate alone prevent \(|c|^2\) from concentrating above every fixed amplitude truncation. The general scalar constructions in Section 3 are not solutions of the full field system; they show why these two remaining steps require that full system, instead of another scalar manipulation of (1).

The actual new input is therefore (13)–(16), which removes differentiated-current/negative-frame test products from the list of obstructions under the stated tensor bounds. The amplitude-capacity defect and its interaction with the complete radial Cartan system remain unresolved.

## 6. Mathematical status and research consequence

The unrestricted O10 question remains open in this continuation. The new content here is an exact scalar defect law, an explicit fixed-geometry check of a tempting Hessian-free shortcut, and the actual-equation product estimate (12)–(13). They should be recorded as a route audit, not advertised as improved coverage of O10. The controlled-growth theorem and the finite-density theorem are unchanged.

The analysis also explains why repeatedly strengthening decay rates has not closed the full target: those rates penalize the size of the unresolved concentration but do not supply a new compatibility relation that forbids its capacity from remaining nonzero. The actual-field constraints, not an additional optimization of the existing scalar inequality, have to settle that issue.
