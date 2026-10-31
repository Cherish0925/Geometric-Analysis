# Step 57: Review and repair of the common-time interface

Session: S0910A01. Agent4 / Preceptor. Phase: Execute.

## 0. Purpose

Step 56 assembled a useful common-time and terminal-compactness route for the
restricted four-dimensional negative Ishida--LeBrun program, but two parts of
that assembly cannot be treated as proved.

1. The overlap uniqueness argument in Step 56 §2.6 compares raw metrics under
   the ungauged fixed-cutoff Ricci flow.  That comparison is not parabolic in
   the metric components because the ungauged Ricci tensor contains second-order
   gauge terms.  Infinitesimal diffeomorphism directions already show that a
   coercive estimate of the displayed form cannot follow for the raw difference.

2. Step 56 §5.4 described the final pinching threshold as depending on varying
   characteristic numbers.  That loses the actual strength of the route.  The
   proportional-volume argument cancels the topology parameter; if the uniform
   support, chart, and flow constants are really established over the stated IL
   class, the negative pinching gap is uniform over that class.  The theorem
   concerns exclusion of tightly pinched input metrics, not a statement that the
   smooth manifold lacks a negative Einstein metric.

This note records the corrected mathematical interface.  It does not turn the
restricted IL theorem into a proof of the full Yau 26 proposition: positive
pinching, arbitrary four-dimensional topology, dimensions n >= 5, and Lean
formalization remain untouched.

---

## 1. Why the raw metric uniqueness estimate is invalid

The fixed-cutoff geometric flow is
\[
 \partial_t g=-2a(\operatorname{Ric}_g+g),\qquad a=\chi^2.
\tag{1.1}
\]
Step 56 §2.6 compared two solutions by setting \(h=g_1-g_2\) and using
\[
 \delta\operatorname{Ric}(h)=-\frac12\Delta_Lh+\hbox{lower order}.
\tag{1.2 bad}
\]
Equation (1.2 bad) is not the linearization of the ungauged Ricci tensor in
fixed coordinates.  The actual linearization contains
\[
 \frac12\bigl(\nabla_i\nabla^k h_{kj}+\nabla_j\nabla^k h_{ki}
              -\nabla_i\nabla_j\operatorname{tr}h\bigr)
\]
in addition to the rough Laplace and curvature terms.  These are precisely the
second-order diffeomorphism directions removed by DeTurck gauge.  If
\(h=\mathcal L_Xg\), the variation of Ricci is \(\mathcal L_X\operatorname{Ric}\),
not a coercive tensor heat operator on \(h\).  Therefore the displayed estimate
\[
 {d\over dt}\int |h|^2\le -\int a|\nabla h|^2+C\int |h|^2
\]
for the raw difference is unsupported.  The preterminal restart remains a good
idea, but overlap agreement must be proved in a gauge-compatible formulation.

---

## 2. Coupled transported-cutoff DeTurck uniqueness: the correct repair

A03 Step 56 constructs the exact flow through the transported-cutoff DeTurck
pair
\[
\begin{split}
 \partial_tG={}&\beta^2\bigl[G^{-1}D^2G+R(G,G)+Q(G,DG)-2G\bigr]
 +2\operatorname{sym}\bigl(d(\beta^2)\otimes W(G)^\flat_G\bigr),\\
 \partial_t\beta={}&\beta^2W(G)\cdot D\beta,
\end{split}
\tag{2.1}
\]
where \(D\) is a fixed background connection and \(W(G)=G^{ab}(\Gamma(G)-\Gamma(\bar g))_{ab}\).  This is the formulation in which uniqueness should be proved.
The scalar \(\beta\) is part of the unknown; a metric-only comparison misses
terms from scalar transport and from \(d(\beta^2)\otimes W\).

### 2.1 Difference variables

Let \((G_1,\beta_1)\) and \((G_2,\beta_2)\) be two smooth solutions of (2.1) on
\([\tau,\tau+L]\) with the same initial data at \(\tau\).  Assume, as is allowed
in the per-datum restart argument, that on this slab
\[
 \lambda\bar g\le G_i\le \lambda^{-1}\bar g,
 \qquad
 \|G_i\|_{C^3}+\|\beta_i\|_{C^2}\le R,
 \qquad 0\le\beta_i\le1.
\tag{2.2}
\]
Put
\[
 H=G_1-G_2,
 \qquad b=\beta_1-\beta_2.
\tag{2.3}
\]
All constants below are per-datum constants depending on \(R,\lambda,L\) and the
background.  They are not used in the sequence-uniform first-exit estimates.

### 2.2 Metric difference energy

Subtracting the metric equations and writing the second-order block with
an averaged positive coefficient gives the leading structure
\[
 \partial_tH=\bar A^{ab}D_aD_bH+
   \mathcal A_1(D\beta_i,DG_i)*DH
  +\mathcal A_0*H+\mathcal B_0*b+
  \mathcal B_1*Db,
\tag{2.4}
\]
where one may take
\[
 \bar A^{ab}=\tfrac12(\beta_1^2G_1^{ab}+\beta_2^2G_2^{ab}).
\]
Here \(\mathcal A_1*DH\) contains first derivatives of the averaged coefficient
and of the lower-order DeTurck coefficients, while
\(\mathcal A_0*H\) includes the differences of \(G^{-1},R,Q,-2\beta^2G\) with all
available coefficients bounded, \(\mathcal B_0*b\) includes the coefficient
difference \((\beta_1^2-\beta_2^2)G_2^{-1}D^2G_2\), and \(\mathcal B_1*Db\) comes
from the difference of the Lie cross term
\(2\operatorname{sym}(d(\beta^2)\otimes W(G)^\flat_G)\).  The important point is
that no ungauged Ricci second-order gauge expression remains; the only second
metric derivative of the difference is the averaged DeTurck block
\(\bar A^{ab}D_aD_bH\).  This choice is important because the scalar equation
can contain \(\beta_2^2(W(G_1)-W(G_2))\), so the metric energy must provide
\((\beta_1^2+\beta_2^2)|DH|^2\) dissipation, not only \(\beta_1^2|DH|^2\).

Testing (2.4) against \(H\) and integrating by parts gives
\[
 {1\over2}{d\over dt}\|H\|_2^2
 +c\int(\beta_1^2+\beta_2^2)|DH|^2
 \le
 C\|H\|_2^2+C\|b\|_2^2
 +\varepsilon\int(\beta_1^2+\beta_2^2)|DH|^2
 +I_{Db}.
\tag{2.5}
\]
The first-derivative coefficient term is harmless because
\(|D\bar A|\le C(\beta_1+\beta_2+\beta_1^2+\beta_2^2)\), so weighted Young gives
\(\varepsilon(\beta_1^2+\beta_2^2)|DH|^2+C|H|^2\).  The scalar-derivative term is handled by
one integration by parts:
\[
 \int H*\mathcal B_1*Db
 =-\int b*D(H*\mathcal B_1),
\tag{2.6}
\]
so it contributes at most
\[
 \varepsilon\int(\beta_1^2+\beta_2^2)|DH|^2+C\|H\|_2^2+C\|b\|_2^2,
\tag{2.7}
\]
because the occurrences of \(DH\) are multiplied by bounded multiples of
\(\beta_1\) or \(\beta_2\).  After choosing \(\varepsilon\) small,
\[
 {d\over dt}\|H\|_2^2
 +c\int(\beta_1^2+\beta_2^2)|DH|^2
 \le C(\|H\|_2^2+\|b\|_2^2).
\tag{2.8}
\]

### 2.3 Scalar transport energy

The scalar difference satisfies
\[
 \partial_tb=\beta_1^2W(G_1)\cdot Db
 +\bigl(\beta_1^2W(G_1)-\beta_2^2W(G_2)\bigr)\cdot D\beta_2.
\tag{2.9}
\]
Since
\[
 W(G_1)-W(G_2)=A_1*DH+A_0*H
\tag{2.10}
\]
with bounded coefficients, the second term in (2.9) has the form
\[
 \beta_1^2DH*b + H*b+b^2.
\]
Testing with \(b\) and integrating the transport term gives
\[
 {1\over2}{d\over dt}\|b\|_2^2
 \le C\|b\|_2^2+C\|H\|_2^2
 +\varepsilon\int\beta_1^2|DH|^2.
\tag{2.11}
\]
Here the term \((\beta_1^2+\beta_2^2)|DH||b|\) is absorbed by the averaged
metric dissipation and weighted Young, while
\(\operatorname{div}(\beta_1^2W(G_1))\) is bounded by the smooth per-datum norms.

### 2.4 Coupled uniqueness for pair variables

Adding a large multiple of (2.11) to (2.8) gives
\[
 {d\over dt}\bigl(\|H\|_2^2+A\|b\|_2^2\bigr)
 +c\int(\beta_1^2+\beta_2^2)|DH|^2
 \le C\bigl(\|H\|_2^2+A\|b\|_2^2\bigr).
\tag{2.12}
\]
If \(H(\tau)=0\) and \(b(\tau)=0\), Gronwall gives \(H\equiv0\) and \(b\equiv0\)
on the overlap.  This is the needed smooth uniqueness statement for the exact
DeTurck pair.

This pair uniqueness is a valid analytic module, but it is not by itself a
complete proof of uniqueness for arbitrary geometric solutions of (1.1).  To
turn it into branch-preserving geometric uniqueness one must also prove the
reverse DeTurck gauge lemma: starting from a smooth geometric solution \(g\),
construct a diffeomorphism \(\varphi\) such that
\(G=(\varphi^{-1})^*g\), \(\beta=\chi\circ\varphi^{-1}\) solve (2.1), including
where \(\chi=0\).  This is a real but per-datum gauge statement.

For the common-time existence theorem, however, branch-preserving uniqueness is
not strictly necessary.  Define the existence time as the supremum of times for
which there exists some smooth fixed-cutoff solution from \(g_0\) satisfying the
first-exit bounds.  If a solution exists on \([0,T_*)\) with \(T_*<\theta r^2\),
choose \(t_j<T_*\) close to \(T_*\).  The preterminal \(H^{s_0}\) bounds give a
uniform local-existence window from the smooth datum \(g(t_j)\).  A newly
constructed geometric solution from \(g(t_j)\) can be pasted to the old solution
restricted to \([0,t_j]\).  The pasted solution is smooth at \(t_j\) because the
flow is autonomous and both one-sided time jets are recursively determined by
the same smooth spatial metric and the same fixed \(\chi\).  The first-exit
energy estimates apply to any smooth branch, so the extended solution retains
the bootstrap on a short extra interval and contradicts the supremum.  This
existence-style restart avoids importing geometric uniqueness into the
sequence-uniform argument.  If later agents prefer branch-maximal language, they
should prove the reverse gauge lemma and use the pair uniqueness above.

All constants here are per-datum and positive-time.  They do not add any
sequence-uniform terminal regularity requirement.

---

## 3. Finite current-pair induction remains a real proof dependency

Step 55 worked out the first nontrivial \((U_2,C_3)\) exchange.  A03 Step 59
states the general pattern, but the proof-level tensor enumeration is still not
written.  The needed lemma is the following.

Let
\[
 T=\operatorname{Rm}+{g\owedge g\over6},\qquad U=aT,\qquad C_j=\nabla^j\chi,
\tag{3.1}
\]
on a positive-time slab with \(|T|+|U|\le K\) and the base pair
\(T_1,U_1,C_2\in L^q\) for all finite \(q\).  For each \(m\ge2\), after all
covariant commutators and time-connection terms are expanded, the equations must
have the structure
\[
\begin{split}
 \partial_tU_m={}&\operatorname{div}(a\nabla U_m)
 +\chi C_{m+2}*U+C_1*C_{m+1}*U+\chi C_{m+1}*U_1
 +\chi C_2*U_m+C_1*C_1*U_m+\mathcal P_m,\\
 \partial_tC_{m+1}={}&C_1*U_m+
 \sum_{1\le j<m}C_{m+1-j}*U_j+\mathcal R_m,
\end{split}
\tag{3.2}
\]
where \(\mathcal P_m,\mathcal R_m\) contain only previous-level quantities,
bounded zero-order coefficients, and factors already known in finite exponents;
current-pair linear factors such as \(C_1*C_{m+1}*U\) are displayed rather than
hidden in the remainder.
For the unweighted curvature level,
\[
 \partial_tT_m=a\Delta T_m+
 \chi C_{m+2}*T+C_1*C_{m+1}*T+\chi C_{m+1}*T_1+
 \chi C_2*T_m+C_1*C_1*T_m+\mathcal S_m.
\tag{3.3}
\]
The proof must explicitly show:

- no term \(C_{m+2}*U\) or \(C_{m+2}*T\) appears without the leading \(\chi\);
- no residual after integrating \(\chi C_{m+2}\) contains a current unknown at an enlarged exponent;
- current signed-Hessian terms \(\chi C_2*U_m\) and \(\chi C_2*T_m\) are exactly of the Step 55 signed-integration form;
- time-connection commutators produce at most \(C_1*U_m\) in the cutoff-jet equation and do not require \(U_{m+1}\) before the current pair is controlled;
- every lower monomial contains only previous levels, bounded coefficients, or the explicitly allowed bounded-coefficient current-pair factors such as \(C_1*C_{m+1}*U\) and \(C_1*C_{m+1}*T\).

Until this lemma is written with an actual commutator expansion, the common-time
continuation theorem remains dependent on more than the per-datum existence
module.  The existing scripts preserve the order counting and exponent
arithmetic; they do not establish the tensor identities.

### 3.1 A03 Step 60 assimilation

After the first version of this review was written, A03 Step 60 supplied a much
stronger candidate for this missing lemma:
`Sessions/S0910A03/workspace/notes/step60_all_order_continuation_and_terminal_chart.md`.
It gives exact coordinate-time families T1--T6 and U1--U7, uses
\((B_1*B_1)T=4(C_1*C_1)U\) to remove the deceptive unweighted term in the
\(U\)-equation, converts \(aT_m\) by
\[
 aT_m=U_m-\sum_{q=1}^m B_q*T_{m-q},
\]
and records that time-commutator reordering only introduces prior
\(T_{\le m-2}\).  Its final finite enumeration checks 252,256 allocations through
order 64 with no failures after adding coefficient-before-commutator and
time-reordering subfamilies.  This is real progress beyond the schematic Step 55
ledger and may close dependency D after a proof-level audit of the base tensor
identities and exact contraction families.

A03 Step 60 also gives a cleaner uniqueness-free continuation: the all-order
current-pair tower yields \(g(t)\to g_*\) in \(C^\infty\) as \(t\uparrow T_*\);
a local solution starting at \(g_*\) is spliced at \(T_*\), and autonomous-PDE
time jets match.  This avoids both the invalid raw metric uniqueness estimate
and the reverse geometric-to-pair gauge lemma.  It is stronger than the
preterminal existence-style splice in §2.4, but it rests on the all-order tower,
not merely the finite \(H^7\) restart package.  The tower should start from the
already established base layer \(T_1,U_1,C_2\in L^q\) and then run from
\(m=2\); applying the same residual estimate at \(m=1\) would be circular.

For terminal selection, A03 Step 60 correctly uses Liouville averaging over the
buffered set and obtains the same \(A\)-cancellation.  Its local contradiction
should be kept aligned with the A01 Step 45/56 formulation: strong
\(W^{2,q}_{\rm loc}\) convergence gives an Einstein limit with vanishing
nonnegative density, and Derdziński's harmonic-\(W^+\), two-eigenvalue theorem
(or the equivalent constant-norm consequence already verified from that source)
excludes the calibrated germ.  Do not replace this source-grounded endpoint by
an unverified spectral slogan.  Also keep notation distinct: the terminal gap
term is \(\mathcal G\), while \(G=g\owedge g/(2(n-1))\) is the shifted-curvature
background tensor.

TTCS review of A03 Step 60 found one concrete correction still needed in the
base equations as read: independent constant forcing terms such as
\(a\cdot1\) in \(\partial_tT\) or \(a^2\) in \(\partial_tU\) should not be quoted
as actual nonzero terms, because \(T=U=0\) is stationary.  They may only appear
as harmless over-envelopes in a structural script; the proof text should use
\(a(T*T+T)\) and \(U*U+aU\) plus the displayed cutoff-gradient terms.

---

## 4. Correct scope of the restricted IL gap

The intended restricted theorem is a contradiction to sequences in the IL class
with
\[
 \delta_i=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{\infty,\operatorname{op}}
 \longrightarrow0.
\tag{4.1}
\]
In the assembled terminal argument,
\[
 \int\Phi_i\le C\delta_i^2 A_i,
 \qquad
 \operatorname{Vol}(P_i^{\rm in})\ge c_0 A_i,
\tag{4.2}
\]
so the average over selected inner centers satisfies
\[
 \mathcal A_\rho\Phi_i(p_i)
 \le Cc_0^{-1}\delta_i^2.
\tag{4.3}
\]
The factor \(A_i\) cancels.  Therefore, if the constants \(C,c_0,K,\rho,\eta\)
are uniform over the stated IL class, the contradiction for
\(C c_0^{-1}\delta_i^2<\eta\) gives a gap
\[
 \varepsilon_{\rm IL}>0
\tag{4.4}
\]
that is uniform over that class.  It should not be described as depending on
\(A_i,D_i\), nor should the old shrinking-with-topology loss be revived.

The theorem being pursued is also not "if a tightly pinched input exists then
\(M\) has no negative Einstein metric".  The IL gauge-theoretic topology often
already obstructs exact Einstein metrics by separate arguments.  The new result
would exclude the existence of arbitrarily tight negative Ricci-pinched input
metrics on those topologies.  This distinction matters for Yau 26, whose input
hypothesis is a two-sided Ricci interval and whose output Einstein metric may
have any sign.

The corrected status is:

- restricted four-dimensional negative IL class: plausible route to a uniform
  negative pinching gap, pending the analytic dependencies above;
- full dimension-four Yau proposition: not settled, because a positive branch or
  other topology might still supply dimension-only forcing, while a refutation
  must defeat both signs;
- dimensions \(n\ge5\): no analogous mechanism established.

---

## 5. Revised dependency map for the restricted theorem

The restricted IL theorem should now be carried with the following dependencies.

A. Per-datum transported-cutoff DeTurck existence and gauge reconstruction
(A03 Step 56).  For continuation, either use the existence-style preterminal
restart/pasting in §2.4, which avoids branch-preserving uniqueness, or prove the
reverse geometric-to-pair gauge lemma and then use the coupled pair uniqueness
above for overlap pasting.

B. Curvature first-exit branch: unweighted shifted \(H_2\), critical-to-
subcritical bridge, and positive-time Moser endpoint
\(\|aF_T(t)\|_\infty\le C\Gamma/t\) (A03 Step 58), including the full tensor
identity for the exact flow.

C. Defect branch: homogeneous \(Q,J_6\) propagation and
\(\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}\), with only first-cutoff-derivative
constants after signed Hessian integration.

D. Finite positive-time continuation: proof-level commutator expansion for the
staggered current-pair induction through
\((U_7,C_8)\) and \(T_0,\ldots,T_6\), followed by fixed-background connection
conversion.

E. Terminal mechanism: terminal monopole recalibration on \(g(T)\), global
\(Q\)-to-\(\Phi\) bound, unit-tangent Liouville averaging, pullback-ball
\(W^{2,q}_{\rm loc}\) compactness, and Derdziński forbidden germ.

This is a strong restricted research program, not final resolution of Yau 26.
The next mathematical construction should either make A+D proof-level, or use
this restricted theorem as a tested component while searching for a route that
reaches the full all-dimensional proposition.
