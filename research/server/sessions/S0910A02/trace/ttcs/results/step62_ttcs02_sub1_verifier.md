# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step62_ttcs_assimilation_and_negative_branch_triage.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step60_all_order_continuation_and_terminal_chart.md",
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A01/workspace/notes/step58_all_order_continuation_proof.md"
  ]
}
```

## Task

Independently verify the current peer restricted negative Ishida--LeBrun/cutoff-flow chain for Yau Problem 26, using the supplied A01/A03 notes plus A02's Step-62 triage. Do not decide the full Yau-26 problem. Assess whether the chain, as written, plausibly proves a restricted four-dimensional negative-sign gap, and identify exact load-bearing gaps or scope limitations. Focus on: per-datum transported-cutoff DeTurck existence; low-order first-exit/Moser modules imported into common time; all-order continuation without ungauged uniqueness; terminal Liouville-pullback compactness and Derdzinski forbidden-germ contradiction; whether any conclusion gives dimension-only constants or a counterexample. Return a mathematical verification memo with concrete items A02 should audit next.

## Output

# Mathematical verification memo

## 1. Overall assessment

The visible A01/A03 equations support a coherent conditional theorem of the following form:

\[
\inf_{g\text{ on }M\in\mathcal F}
\left\|g^{-1}(\operatorname{Ric}_g+g)\right\|_{L^\infty,\mathrm{op}}
\ge \varepsilon_{\mathcal F}>0
\]

for a precisely specified four-dimensional Ishida–LeBrun family \(\mathcal F\), provided that the support-selection constants, low-order cutoff-flow estimates, Seiberg–Witten/Chern–Weil calibration, and terminal geometric constants are uniform over \(\mathcal F\).

The transported-cutoff construction and the uniqueness-free continuation mechanism are mathematically plausible from the displayed derivations. The largest unresolved parts in the supplied packet are instead:

1. the sequence-uniform low-order \(H_2,Y,J_6,Q_\alpha,(\Gamma,V)\) estimates;
2. the uniform unweighted base layer \(T_0,U_1,T_1,C_2\) near the transition region where \(a=\chi^2\) becomes small;
3. the exact calibration density \(\mathfrak D\), especially \(\mathcal G\), and the derivation of  
   \(\int\mathfrak D\le C\delta^2A\);
4. uniformity of the Ishida–LeBrun geography and support constants.

Thus the architecture plausibly proves the stated restricted pinching gap after those modules are supplied, but the visible notes alone are not yet a self-contained proof.

---

## 2. Per-datum transported-cutoff DeTurck existence

### 2.1 Pullback algebra is correct

Let
\[
X=-\beta^2W(G),\qquad \partial_t\varphi=X\circ\varphi,\qquad g=\varphi^*G.
\]
Then
\[
\partial_tg=\varphi^*(\partial_tG+\mathcal L_XG).
\]
Using
\[
\mathcal L_{\beta^2W}G
=\beta^2\mathcal L_WG
+2\operatorname{sym}\!\left(d(\beta^2)\otimes W^\flat_G\right),
\]
the cross term in A03 Step 56, equation (1.1), cancels the derivative of
\(\beta^2\) produced by \(\mathcal L_XG\). Provided the bracket
\[
G^{-1}D^2G+R(G,G)+Q(G,DG)
\]
is the standard coordinate expression for
\[
-2\operatorname{Ric}_G+\mathcal L_{W(G)}G,
\]
one obtains
\[
\partial_tg=-2(\beta\circ\varphi)^2(\operatorname{Ric}_g+g).
\]
The scalar equation gives
\[
\frac d{dt}\beta(t,\varphi(t,x))
=\partial_t\beta-\beta^2W\cdot D\beta=0,
\]
so \(\beta\circ\varphi=\chi\). This verifies equation (5.4), including its sign.

### 2.2 Regularized system and maximum principle

For fixed \(\varepsilon,\nu>0\), the principal blocks in (1.2) are
\[
(\beta^2+\varepsilon)G^{ab}\xi_a\xi_bI_{\mathrm{Sym}^2},
\qquad
\nu\bar g^{ab}\xi_a\xi_b.
\]
The metric–scalar coupling contains only first derivatives, so the system is strongly parabolic while \(G\) remains positive definite.

At an extremum of \(\beta\), \(D\beta=0\), so the transport term vanishes. The scalar heat term has the required sign. Hence
\[
0\le\beta\le1
\]
is correctly preserved.

### 2.3 Tame allocation

The interpolation count behind (2.6) is valid. For every factor with \(q_i>4\),
\[
\theta_i=\frac{q_i-4}{m-4},\qquad
\|D^{q_i}u_i\|_{L^{2/\theta_i}}
\lesssim \|u_i\|_{H^m}^{\theta_i},
\]
using the \(W^{4,\infty}\) norm furnished by
\(s_0>n/2+4\). If at least two factors are above order four, then
\[
\sum\theta_i
\le\frac{m+2-4k}{m-4}
\le\frac{m-6}{m-4}<1.
\]
This gives linear dependence on the current high norm, rather than a product of several current \(H^m\) norms.

The displayed treatments of the four top-order interactions are also consistent:

- \(DA\) in the metric principal term uses
  \(\beta^2/(\beta^2+\varepsilon)\le1\);
- the \(Q(G,DG)\) top derivative is absorbed by metric dissipation;
- the \(D^{m+1}\beta\) term from the Lie cross term is integrated once;
- the top metric derivative in the scalar transport equation uses
  \(\beta^4/(\beta^2+\varepsilon)\le1\).

No inverse power of \(\varepsilon\) or \(\nu\) appears in these displayed estimates.

### 2.4 Remaining proof interfaces in this module

The following details are asserted rather than fully expanded in the visible note:

- the exact coordinate identity relating \(R+Q\) to
  \(-2\operatorname{Ric}+\mathcal L_WG\);
- the full \(m=s_0\) polynomial estimate (4.1), including all background-curvature commutators;
- the fixed-parameter continuation theorem in the precise Sobolev spaces used;
- the diagonal compactness argument yielding convergence in every space-time \(C^k\) norm;
- uniform bounds for repeated time derivatives without hidden dependence on \(\varepsilon^{-1}\) or \(\nu^{-1}\).

Nothing in the displayed formulas indicates an inherent obstruction to these steps, but the finite allocation script verifies derivative arithmetic only, not the tensor identities or the parabolic theorem interface.

---

## 3. Low-order first-exit and Moser modules

This is the least documented part of the supplied chain. A03 Step 56 explicitly says that (6.8) is not reproved, while A01 Step 56 imports the same material from earlier records. Consequently, the common-time theorem depends on equations not visible here.

### 3.1 Exact estimates needed

The sequence-uniform argument requires, with constants independent of the individual high Sobolev norms:

1. the unweighted critical energy
   \[
   H_2^\alpha=\int\eta_\alpha^2F_T^2\,d\mu;
   \]
2. the curvature smoothing estimate leading to
   \[
   \|aF_T(t)\|_\infty\le C\Gamma/t;
   \]
3. the homogeneous defect energy \(J_6\) and the endpoint
   \[
   \|aE(t)\|_\infty
   \le C\delta(r^2/t)^{1/3};
   \]
4. local defect evolution
   \[
   Q_\alpha(t)\le e^{Ct/r^2}Q_\alpha(0);
   \]
5. the coupled \((\Gamma,V)\) self-improvement with strict support and Sobolev estimates.

The insistence that \(H_2\) be unweighted is mathematically essential. A factor of \(a\) would lose curvature information in the collar where \(a\) is small, precisely where the later unweighted continuation needs control.

### 3.2 Cutoff Hessian issue

The signed integration-by-parts mechanism is valid in its model form:
\[
\int (\nabla^2a)_{ij}\mathcal B^{ij}
=-\int \nabla a*\nabla\mathcal B,
\]
and
\[
|\nabla a|^2/a=4|\nabla\chi|^2
\]
where \(a>0\), with smooth extension through \(a=0\). This can replace an \(L^\infty\) estimate for \(\nabla^2\chi\).

What remains to be seen is that every occurrence of \(\nabla^2a\) in the actual curvature and defect tensor equations retains a signed contraction suitable for this integration. Once absolute values or scalar envelopes have already been applied, that structure can be lost. The exact \(H_2,Y,J_6,Q_\alpha\) evolution formulas are therefore indispensable.

### 3.3 Unweighted base seed

A serious textual weakness appears around the base layer. A01 Step 58 §3 and A03 Step 60 §3 require
\[
T_0,\ T_1,\ U_1,\ C_2\in L^\infty_tL^q_x
\quad\text{for every finite }q.
\]
The weighted estimate \(\|aT\|_\infty<\infty\) does not itself control \(T\) where \(a\to0\). Smoothness at each individual time also does not give a uniform bound as \(t\uparrow T_*\).

The notes refer to an “independent zero-order seed” and a \(W^{1,p}\to L^\infty\) bridge, but that derivation is not supplied. This base seed must explicitly cover:

- the transition collar \(0<a<1\);
- the stationary region \(a=0\);
- uniformity on the whole slab \([\tau,T_*)\);
- \(T_1\) and \(U_1\), not only \(T_0\).

This point is central because the all-order induction begins only after this base layer is available.

### 3.4 Stationary remainder

The corrected identity
\[
Q_{\mathrm{global}}(t)
=Q_{\mathrm{rest}}(0)+\sum_\alpha Q_\alpha(t)
\]
is sound if \(1-\rho\) is supported in an open set on which \(a\equiv0\). There the metric and all its spatial jets remain fixed. Strict support buffers are therefore part of the mathematical argument, not merely support notation.

---

## 4. All-order continuation without ungauged uniqueness

### 4.1 Ungauged metric-difference estimate is correctly discarded

The principal symbol in A03 Step 60, equations (4.1)–(4.4), has the standard Ricci gauge kernel. The Fourier-mode example gives a quadratic form of size
\[
(\varepsilon-\varepsilon^2)k^2>0.
\]
Thus no coercive inequality of the form
\[
\frac d{dt}\|g_1-g_2\|_2^2\le C\|g_1-g_2\|_2^2
\]
can follow from raw Ricci coercivity. The terminal-limit and autonomous-splice construction is the appropriate replacement.

### 4.2 Current-pair energy closes for \(m\ge2\)

The critical residual is
\[
I_m=\int\chi|C_{m+1}|\,|U_1|\,|U_m|^{p-1}.
\]
With \(f=\chi|U_m|^{p/2}\), the Hölder exponents used in A01 Step 58 are correct:
\[
\frac14+\frac1p+\frac14+\frac{p-2}{2p}=1.
\]
Hence
\[
I_m
\le \|f\|_4\|C_{m+1}\|_p
   \|U_1\|_4\|U_m\|_p^{p/2-1}.
\]
Sobolev and Young give
\[
I_m\le\varepsilon D^U_{m,p}
+C\bigl(1+\|C_{m+1}\|_p^p+\|U_m\|_p^p\bigr)
\]
provided \(U_1\in L^4\) is already known. This explains correctly why the induction begins at \(m=2\); at \(m=1\), \(U_1\) is the current unknown.

The algebraic replacement
\[
(B_1*B_1)*T=4(C_1*C_1)*U
\]
is also exact and removes an apparent unweighted \(T\) coefficient.

### 4.3 Signed Hessian

For
\[
J_m=\int\chi(\nabla^2\chi)_{ij}\mathcal B^{ij}(U_m),
\]
one integration by parts gives terms bounded by
\[
\varepsilon D^U_{m,p}
+C\|\nabla\chi\|_\infty^2\|U_m\|_p^p.
\]
This derivation is valid and uses no uniform \(L^\infty\) estimate for \(C_2\).

### 4.4 Tensor-family completeness remains partly implicit

The families (T1)–(T6) and (U1)–(U7) have the expected derivative allocations, and the two potentially dangerous terms are handled correctly:
\[
aT_m*U_0
=\left(U_m-\sum_{q=1}^mB_q*T_{m-q}\right)*U_0,
\]
and
\[
C_{m+1}*C_1*U_0.
\]

The scripts cited in Step 60 verify integer allocations but not:

- the all-covariant Riemann variation;
- metric contractions in the time commutator;
- curvature terms created while reordering derivatives;
- time variation of the tensor norm and volume form.

A full indexed derivation is still needed to establish that no current \(T_m\) appears without \(a\), and that every omitted term is either a bounded coefficient times the current variable or prior-level forcing.

### 4.5 Fixed-background conversion

The triangular idea is sound. Since
\[
\partial_tA=g^{-1}*\nabla(aE)=g^{-1}*U_1,
\]
up to lower contractions, \(\bar\nabla^m\partial_tA\) has top forcing \(U_{m+1}\) and no \(A_{m+1}\).

The visible proof compresses product estimates involving \(A_j\) and \(U_k\). These can plausibly be closed because the full evolving-derivative tower and scalar Sobolev estimates give \(L^\infty\) bounds for lower tensors from one additional covariant derivative. That intermediate argument should be written explicitly; otherwise the designation of every current \(A_m\) coefficient as bounded is not immediate.

### 4.6 Terminal splice

If
\[
g(t)\to g_*\quad\text{in }C^\infty
\]
and \(g_*\) remains positive definite, then the autonomous recursion
\[
\mathcal F_{\ell+1}(g)
=D\mathcal F_\ell(g)[\mathcal F(g)]
\]
correctly identifies all one-sided time jets. Any local solution beginning at \(g_*\) has the same jets, so the piecewise solution is smooth across \(T_*\). No overlap uniqueness is required.

This continuation mechanism is internally convincing once the unweighted base layer and all-order tensor equations are established.

---

## 5. Terminal Liouville selection and pullback compactness

### 5.1 Liouville averaging

The averaging argument in A03 Step 60 §6 is valid. On each pullback tangent ball,
\[
\int_{\mathcal B_\rho(p)}(\exp_p)^*\mathfrak D
\asymp
\int_0^\rho t^3\int_{S_pM}
\mathfrak D(\pi\varphi_t(p,u))\,du\,dt,
\]
using the Jacobi estimate \(j(p,u,t)\asymp t^3\). Integrating over \(p\in P\), invariance of Liouville measure gives
\[
\int_P\mathcal A_\rho\mathfrak D(p)\,d\mu(p)
\le C\int_M\mathfrak D\,d\mu.
\]
Thus
\[
\operatorname{Vol}(P)\ge c_0A,\qquad
\int_M\mathfrak D\le C_0\delta^2A
\]
selects \(p\in P\) satisfying
\[
\mathcal A_\rho\mathfrak D(p)
\le Cc_0^{-1}\delta^2.
\]
The topological scale \(A\) cancels exactly.

Folding of the image exponential ball is irrelevant because integration occurs over initial tangent vectors.

### 5.2 Pullback geometry

A uniform curvature bound along all radial geodesics and
\(\rho\) below a uniform conjugate radius make
\((\exp_p)^*g\) a smooth positive metric on the tangent ball. The precise center-injectivity argument is
\[
\exp^{(\exp_p)^*g}_0(v)=v
\]
for \(|v|<\rho\), rather than merely saying that radial rays do not intersect. This gives a uniform harmonic radius on a smaller central ball.

The required geodesic buffer is assumed in A03 Step 60 equation (6.3). Its derivation from the original support buffers and terminal bilipschitz estimate is not displayed and is another concrete geometric input.

### 5.3 Strong \(W^{2,q}\) convergence

The compactness argument is sound:

- curvature and center injectivity give harmonic \(C^{1,\alpha}\) and \(W^{2,q}\) bounds;
- \(\mathfrak D_i\ge|E_i|^2\) and mean convergence to zero yield \(E_i\to0\) in \(L^2_{\mathrm{loc}}\);
- bounded curvature upgrades this to every finite \(L^q\);
- the harmonic-coordinate Ricci equation yields a smooth Einstein limit and strong \(W^{2,q}_{\mathrm{loc}}\) convergence.

Strong \(W^{2,q}\) gives strong \(L^q\) convergence of curvature. This is sufficient for continuous algebraic functions of \(W^+\), including its eigenvalues.

It is not sufficient for a density involving \(\nabla W^+\). Therefore the exact definition of \(\mathcal G\) matters: the statement that it is an “algebraic spectral density” must be verified from its formula.

---

## 6. Derdziński forbidden-germ computation

Assume the limit satisfies
\[
\operatorname{Ric}=-g,\qquad s=-4,
\]
and
\[
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Then
\[
|W^+|^2=\frac1{36}+\frac2{144}=\frac1{24}.
\]

Because an Einstein four-metric has \(\delta W^+=0\), Derdziński’s theorem for \(W^+\) with two eigenvalues makes a conformal multiple of \(g\) locally Kähler. Here \(|W^+|\) is constant and nonzero, so the conformal factor is constant; consequently \(g\) itself is locally Kähler.

For a Kähler surface with its complex orientation,
\[
\operatorname{Spec}(W^+)
=\left(\frac s6,-\frac s{12},-\frac s{12}\right).
\]
At \(s=-4\), this is
\[
\left(-\frac23,\frac13,\frac13\right),
\qquad
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
which is incompatible with \(1/24\). This verifies the forbidden-germ contradiction, provided the \(W^+\) orientation in the Seiberg–Witten calibration is the same orientation used here.

The alternative Einstein–Weyl computation is consistent as well. With
\[
\det W^+=-\frac1{864},
\]
the standard formula
\[
\frac12\Delta|W^+|^2
=|\nabla W^+|^2+\frac s2|W^+|^2-18\det W^+
\]
gives, when the norm is constant,
\[
|\nabla W^+|^2
=\frac1{12}-\frac1{48}
=\frac1{16}.
\]
Derdziński’s Kähler conclusion would give \(\nabla W^+=0\), again producing the contradiction. The separate “constant-spectrum projector lemma” mentioned in A03 Step 60 is therefore unnecessary unless it serves some earlier calibration purpose.

The source passage and orientation convention for Derdziński’s theorem are not included in the supplied files and remain to be matched directly.

---

## 7. Calibration and geography inputs

The terminal analytic argument begins from
\[
\int_M\mathfrak D\,d\mu\le C\delta^2A,
\]
where
\[
\mathfrak D
=|E|^2+(s+4)^2
 +(s+8\sqrt6|W^+|)^2+\mathcal G.
\]
The packet does not include:

- the explicit formula for \(\mathcal G\);
- the proof that \(\mathcal G\ge0\);
- the algebra showing \(\mathcal G=0\) forces the stated Weyl spectrum;
- the derivation of the constant \(119\);
- the exact role and sign convention of \(q_{\rm top}\);
- the Seiberg–Witten source yielding the calibrated inequality;
- the definition of \(A\) and the proof of
  \(\operatorname{Vol}(P)\ge c_0A\);
- the theorem identifying which Ishida–LeBrun manifolds carry no Einstein metric for any Einstein constant.

These are essential to the restricted theorem. In particular, the assertion in A01 Step 58 that per-datum existence is the sole conditional input is not supported by the visible packet: A03 Step 56 itself leaves the first-exit estimates conditional, and the terminal calibration source is not present.

---

## 8. Consequence for pinching intervals

The operator estimate
\[
\left\|g^{-1}(\operatorname{Ric}_g+g)\right\|_{\mathrm{op}}\le\delta
\]
is equivalent to
\[
-(1+\delta)g\le\operatorname{Ric}_g\le-(1-\delta)g.
\]

More generally, if \(c<C<0\) and
\[
cg\le\operatorname{Ric}_g\le Cg,
\]
set
\[
\widetilde g=\alpha g,\qquad
\alpha=-\frac{c+C}{2}>0.
\]
Then
\[
-(1+\varepsilon)\widetilde g
\le\operatorname{Ric}_{\widetilde g}
\le-(1-\varepsilon)\widetilde g,
\qquad
\varepsilon=\frac{C-c}{-(c+C)}.
\]
Thus a verified \(\varepsilon_{\mathcal F}\) would exclude sufficiently narrow relative Ricci intervals of this sign on the chosen Ishida–LeBrun family.

It would not provide constants depending only on dimension. The constants visible in the construction depend on
\[
r,\theta,\gamma_*,V_*,c_0,K,\rho,
\]
the support construction, Sobolev constants, calibration constants, and geography data.

It also does not furnish a counterexample to Yau Problem 26. Such a counterexample would require a no-Einstein manifold together with an input metric satisfying whichever universal interval is proposed. This route instead rules out tightly normalized \(\operatorname{Ric}\approx-g\) metrics on certain no-Einstein manifolds. Positive Ricci intervals, arbitrary four-manifolds, and dimensions \(n\ge5\) are untouched.

---

## 9. Highest-value concrete A02 verification objects

1. **Exact low-order evolution ledger:** the full \(H_2,Y,J_6,Q_\alpha\) differential inequalities, including every Hessian-of-cutoff term and all Sobolev absorptions.

2. **Transition-collar base estimate:** a direct proof of
   \[
   T_0,T_1,U_1,C_2\in L^\infty([\tau,T_*);L^q)
   \]
   for every finite \(q\), without deriving unweighted \(T\) control solely from \(aT\).

3. **Indexed shifted-curvature variation:** a tensor derivation of the families (T1)–(T6), (U1)–(U7), including time variation of norms and volume.

4. **DeTurck parabolic interface:** the precise identity for \(R+Q\), the \(m=s_0\) estimate, fixed-parameter continuation, and smooth \((\varepsilon,\nu)\to0\) compactness.

5. **Terminal density formula:** the explicit \(\mathcal G\), its nonnegativity, its zero set, and the derivation of
   \(\int\mathfrak D\le119Q\).

6. **Derdziński source passage:** hypotheses, conformal exponent, orientation, and the Kähler \(W^+\) eigenvalue convention.

7. **Uniform geography data:** exact definition of \(\mathcal F\), \(A\), \(q_{\rm top}\), support buffers, proportional-volume constant \(c_0\), and the theorem excluding every Einstein metric on each member.

The high-order continuation is currently the most internally developed component. The low-order sequence-uniform estimates and terminal calibration are the decisive missing scientific records for converting the architecture into a complete restricted four-dimensional theorem.