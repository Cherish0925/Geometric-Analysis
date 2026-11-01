# TTCS Independent Branch Record

```json
{
  "step_id": 53,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step55_direct_nonlinear_flow_construction.md",
    "Sessions/S0910A03/workspace/scripts/verify_step55_direct_construction.py",
    "Sessions/S0910A03/workspace/data/step55_direct_construction_checks.json",
    "Sessions/S0910A01/workspace/notes/step45_consolidated_IL_negative_gap_proof.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step51.md",
    "Sessions/S0910A01/workspace/notes/step52_lefschetz_product_quotient_obstruction_scan.md"
  ]
}
```

## Task

Independently verify the mathematical substance of A03 Step55's direct nonlinear construction of the normalized cutoff flow and its interface with the restricted Ishida--LeBrun negative-gap architecture. Read the supplied A03 note, structural check script/data, and the A01 consolidated IL proof/route notes. Focus on whether the transported-cutoff DeTurck system, epsilon-regularized parabolic-plus-transport construction, epsilon-uniform H^s and all-order hierarchy, epsilon->0 passage, and pullback identity plausibly give a genuine per-datum smooth solution of ∂_t g = -2 χ^2(Ric+g). Then identify precisely what remains before the restricted IL theorem is an end-to-end proof: first-exit quantities, support/terminal chain, sequence-uniform time, or hidden derivative/epsilon losses. Do not decide the session route; give a direct scientific verification memo with load-bearing errors, corrections, and implications for the Yau 26 research state.

## Output

# Scientific verification memo

## Overall assessment

The transported-cutoff DeTurck formulation is algebraically correct, and its principal derivative structure supports an \(\varepsilon\)-independent \(H^s\) estimate. No unavoidable factor \(\varepsilon^{-1}\) appears in the displayed top-order interactions. Subject to completion of the tame Sobolev estimates and fixed-\(\varepsilon\) mixed parabolic–transport existence theory, Step 55 gives a credible construction of at least one smooth per-datum solution of
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]

Three points are materially incomplete:

1. Proposition 5.1 contains an incorrect derivative-index argument, although standard tame estimates appear capable of repairing it.
2. The uniqueness asserted for the geometric equation does not follow directly from uniqueness of the gauged \((G,\beta)\) system; an inverse gauge construction is absent.
3. The final Appendix sentence asserting a sequence-independent existence time from curvature/volume budgets is unsupported and conflicts with A01 §4.2, which explicitly has no sequence-independent control of higher cutoff jets. The per-datum theorem therefore does not yet supply the fixed terminal time required by the Ishida–LeBrun argument.

The first-exit and terminal-chart chain remains the largest analytic component not demonstrated in the supplied material.

---

## 1. Transported-cutoff DeTurck system

Let
\[
H(G):=-2\operatorname{Ric}(G)+\mathcal L_{W(G)}G.
\]
With the stated DeTurck vector,
\[
H(G)=G^{ab}D_aD_bG+R(G,G)+Q(G,DG)
\]
up to the standard background-curvature and first-derivative terms.

For a scalar \(f\),
\[
\mathcal L_{fW}G
=f\mathcal L_WG+df\otimes W_G^\flat+W_G^\flat\otimes df.
\]
Consequently the metric equation in (1.4) is exactly
\[
\partial_tG
=-2\beta^2(\operatorname{Ric}(G)+G)+\mathcal L_{\beta^2W(G)}G.
\]
Thus the extra \(d(\beta^2)\)-term is necessary; omitting it would produce the wrong fixed-cutoff equation after pullback.

The transport equation
\[
\partial_t\beta=\beta^2W(G)\cdot D\beta
\]
has characteristic velocity \(-\beta^2W(G)\). For
\[
\partial_t\varphi=-\beta^2W(G)\circ\varphi
\]
one obtains
\[
\frac d{dt}\beta(t,\varphi(t,x))=0,
\qquad
\beta(t,\varphi(t,x))=\chi(x).
\]
The signs in (7.1)–(7.5) are therefore consistent.

The regularized equation can be written
\[
\partial_tG_\varepsilon
=(\beta_\varepsilon^2+\varepsilon)H(G_\varepsilon)
-2\beta_\varepsilon^2G_\varepsilon
+d(\beta_\varepsilon^2)\otimes W^\flat
+W^\flat\otimes d(\beta_\varepsilon^2).
\]
Its principal spatial operator is
\[
(\beta_\varepsilon^2+\varepsilon)G_\varepsilon^{ab}D_aD_b.
\]
It is strictly parabolic for each fixed \(\varepsilon>0\). Its ellipticity lower bound is proportional to \(\varepsilon\), so it is not a uniformly elliptic family as \(\varepsilon\to0\); the compactness argument must rely on weighted energies rather than ordinary parabolic estimates with uniform constants. Step 55 uses the correct strategy in this respect.

---

## 2. The \(\varepsilon\)-independent \(H^s\) mechanism

The central weight is
\[
a_\varepsilon=\beta^2+\varepsilon.
\]
The most important coefficient identity is
\[
\frac{|Da_\varepsilon|^2}{a_\varepsilon}
=\frac{4\beta^2|D\beta|^2}{\beta^2+\varepsilon}
\le 4|D\beta|^2.
\]
This removes the apparent singularity near \(\{\beta=0\}\).

### Principal metric commutator

After differentiating \(k\) times and integrating the principal term by parts, the leading contribution is, with the \(G^{-1}\) contraction retained,
\[
-\int a_\varepsilon\,G^{-1}*D^{k+1}G*D^{k+1}G.
\]
The term involving \(Da_\varepsilon\) satisfies
\[
\left|\int Da_\varepsilon*D^{k+1}G*D^kG\right|
\le
\eta\int a_\varepsilon|D^{k+1}G|^2
+C_\eta\int |D\beta|^2|D^kG|^2.
\]
Derivatives of \(G^{-1}\) carry the full factor \(a_\varepsilon\) and obey the analogous weighted estimate. This is the core reason no \(\varepsilon^{-1}\) is forced.

### Transport coupling

The highest metric derivative in the \(H^s\) transport energy is
\[
\int D^s\beta\,
\beta^2D^sW(G)\,D\beta
\sim
\int \beta^2D^s\beta\,D^{s+1}G\,D\beta.
\]
Since
\[
\frac{\beta^4}{\beta^2+\varepsilon}\le\beta^2\le1,
\]
weighted Young gives
\[
\left|\int \beta^2D^s\beta\,D^{s+1}G\,D\beta\right|
\le
\eta\int a_\varepsilon|D^{s+1}G|^2
+C_{\eta}\|D\beta\|_\infty^2\|D^s\beta\|_2^2.
\]
This absorption is valid.

### Lie cross-term

The highest \(\beta\)-derivative has the form
\[
\int D^sG*\beta W(G)*D^{s+1}\beta.
\]
One integration by parts yields
\[
-\int \beta W(G)*D^{s+1}G*D^s\beta
\]
plus lower-order terms. Again,
\[
\frac{\beta^2}{\beta^2+\varepsilon}\le1,
\]
so the metric dissipation absorbs the first term. When all derivatives instead hit \(W(G)\), the factor \(d(\beta^2)=2\beta\,d\beta\) supplies the needed \(\beta\).

These computations substantiate the principal structural assertion of Proposition 3.1.

### Corrections needed in the written estimate

- In (1.6), the \(Q\)-term has coefficient \(\beta^2+\varepsilon\), whereas §3 discusses \(\beta^2Q\). The proper estimate is
  \[
  \left|\int D^kG*a_\varepsilon A(G,DG)D^{k+1}G\right|
  \le \eta\int a_\varepsilon|D^{k+1}G|^2
  +C_{\eta,R}\|D^kG\|_2^2.
  \]
  This is still favorable, but the displayed coefficient must match the equation.

- Taking the coupling constant \(A\) “large enough” is not the operative mechanism. Multiplying the transport energy by \(A\) also multiplies its cross-term. A fixed \(A>0\), followed by a sufficiently small Young parameter, closes the estimate; the resulting Grönwall constant depends on \(A\).

- The stated bound including \(\int\mathcal D_s\) needs one additional short-time estimate after Grönwall. The bound on \(\mathcal E_s\) alone does not directly yield the exact right side in (3.2), though a smaller \(T_0\) repairs this.

- A complete proof needs a stopping-time bootstrap controlling \(G^{-1}\), \(\|G\|_{H^s}\), and \(\|\beta\|_{H^s}\). The note sketches this but does not write the closed bootstrap inequalities.

For fixed \(\varepsilon\), standard mixed quasilinear theory is applicable. A Galerkin presentation needs care because spectral projection does not automatically preserve every integration-by-parts identity or metric positivity. A citation to a suitable parabolic–transport theorem, or a Friedrichs scheme with explicit commutators, would be cleaner.

---

## 3. Difference estimate, all-order hierarchy, and compactness

### Difference estimate

The orientation of the principal difference is well chosen:
\[
A_1D^2G_1-A_2D^2G_2
=A_2D^2Z+(A_1-A_2)D^2G_1.
\]
At \(r=s-2\),
\[
\|(A_1-A_2)D^2G_1\|_{H^r}
\le C_R\bigl(\|\omega\|_{H^r}+\|Z\|_{H^r}\bigr),
\]
because \(H^r\) is an algebra and \(D^2G_1\in H^r\).

The branch-oriented splittings for the \(Q\)-term, Lie term, and transport velocity are essential. They arrange every occurrence of \(D^{r+1}Z\) with either \(\beta_2\) or \(\beta_2^2+\varepsilon\), allowing absorption by the branch-2 metric dissipation. At the principal level this is sound.

A full proof still requires all intermediate Moser terms to be written with the same orientation. Proposition 4.1 is plausible, but the supplied derivation is not yet a term-complete estimate.

### Concrete error in Proposition 5.1

The derivative partition in §5 is incorrect as written. It says that for
\[
j\le m-s,
\]
the factor \(D^j[(\beta^2+\varepsilon)G^{-1}]\) is controlled by \(E_s\). For example, if \(m=3s\) and \(j=2s\), an \(H^s\) bound cannot control \(2s\) derivatives of that coefficient.

The repair is a tame Moser estimate, not that partition. After isolating the two top structures
\[
a_\varepsilon D^{m+2}G,
\qquad
\beta W\,D^{m+1}\beta,
\]
the remaining products admit bounds of the form
\[
C\bigl(\|(G,\beta)\|_{H^s},\|G^{-1}\|_{L^\infty}\bigr)
\bigl(1+E_m\bigr),
\]
possibly with already established \(E_{m-1}\) entering the coefficient. The products in
\[
D^{m+1}(\beta^2)-2\beta D^{m+1}\beta
\]
are controlled by the standard tame estimate
\[
\|D\beta\,D\beta\|_{H^{m-1}}
\le C\|D\beta\|_{L^\infty}\|\beta\|_{H^m}.
\]
Thus the all-order result appears repairable, but its current proof is not valid.

### Passage \(\varepsilon\to0\)

If the repaired all-order bounds hold on one common interval, the diagonal compactness argument works. Uniform \(E_{m+1}\) bounds give spatial compactness in \(H^m\); the equations give time equicontinuity after choosing \(m\) sufficiently large. Then
\[
\varepsilon G_\varepsilon^{-1}D^2G_\varepsilon\to0
\]
in every prescribed \(C^k\) norm by using a correspondingly higher spatial bound.

The zero set is fixed: at each spatial point,
\[
\partial_t\beta=\bigl(W(G)\cdot D\beta\bigr)\beta^2
\]
is an ordinary differential equation in \(\beta(t,x)\) with continuous coefficient, so \(\beta(0,x)=0\) implies \(\beta(t,x)=0\). At such points \(d(\beta^2)=0\), and the exact \(G\)-equation is stationary.

### Geometric uniqueness

Propositions 6.1 and 7.1 establish one geometric solution. The uniqueness sentence in Theorem 9.1 needs more work. Uniqueness of the gauged system only compares pairs already satisfying (1.4). To compare arbitrary solutions of the fixed-\(\chi\) geometric equation, each one must be transformed into the same gauged system through an inverse DeTurck construction. Because the coefficient degenerates and the transformed cutoff must be transported, this is not merely the ODE used in §7. The Ishida–LeBrun argument only needs existence, so this gap does not obstruct that application.

---

## 4. Interface with the Ishida–LeBrun architecture

Step 55 supplies the correct exact flow for the later geometry:

- \(g(t)=g_0\) on \(\{\chi=0\}\);
- ordinary normalized Ricci flow occurs where \(\chi=1\);
- disjoint supports give
  \[
  \left(\sum_\alpha\chi_\alpha\right)^2
  =\sum_\alpha\chi_\alpha^2.
  \]

This removes the earlier transported-versus-fixed cutoff mismatch.

The terminal contradiction in A01 is logically coherent once its analytic inputs hold: fixed chart parameters produce a local lower mean for \(\Phi\), proportional plateau volume produces a lower bound of order \(A_i\), and
\[
\int\Phi_i\le119Q_i(T),\qquad Q_i(T)=o(A_i)
\]
produces the contradiction. The Derdziński germ argument and the elliptic \(W^{2,p}\) upgrade are also mathematically plausible.

The unresolved connection is the fixed terminal time.

### Sequence-independent time is not supplied by Step 55

Theorem 9.1 gives
\[
T=T\bigl(\|g_0\|_{H^s(\bar g)},\|\chi\|_{C^s(\bar g)}\bigr).
\]
The IL family assumptions provide pointwise control of \(\operatorname{Ric}+g\), an \(L^2\) curvature budget, volume information, and first-derivative cutoff control. They do not provide comparable \(H^s\) metric bounds on varying manifolds. A01 §4.2 explicitly states that cutoff jets of order at least two are only finite per datum.

Therefore the Appendix assertion
\[
T_i\ge T_0(H^s,C^s)>0
\]
from “curvature-to-volume budgets” does not follow from the supplied estimates. Curvature \(L^2\) and volume information do not control high fixed-coordinate Sobolev norms.

A fixed time \(T=\theta r^2\) could instead arise from a maximal-time continuation argument on the exact flow. Such an argument requires the weighted geometric hierarchy to show that no smooth quantity becomes infinite before \(\theta r^2\), even though its bound may depend on the individual initial high derivatives. That continuation theorem is not present in Step 55.

### Analytic objects still requiring full derivations

The supplied A01 note states, but does not derive in the provided material, the following load-bearing estimates:

1. The local curvature energy \(K_2^\eta\) and collapse-independent Sobolev absorption.
2. The integrated cubic quantity \(Y\) and the endpoint
   \[
   \|a\,\operatorname{Rm}(t)\|_\infty\le C/t.
   \]
3. The sixth-power defect energy \(J_6\), including the signed integration of every \(\nabla^2a\) term.
4. The all-\(p\) defect ladder leading to
   \[
   \|aE(t)\|_\infty
   \le C\delta(r^2/t)^{1/3}.
   \]
5. The homogeneous global estimate
   \[
   Q(T)\le e^{C(1+r^{-2})T}Q(0)
   \]
   with no additive curvature term.
6. Metric drift and preservation of the proportional inner volume.
7. The all-order weighted/unweighted continuation needed to extend the per-datum solution to \(\theta r^2\).

The dangerous coefficient is
\[
\nabla^2a=2\,d\chi\otimes d\chi+2\chi\nabla^2\chi.
\]
Since \(\nabla^2\chi\) is not controlled uniformly in the support construction, each low-order estimate must explicitly integrate the \(\chi\nabla^2\chi\) term by parts until only uniformly controlled first derivatives remain. A summary reference to a signed Hessian contraction is not enough to establish family-independent constants.

The terminal exponential-pullback chart also needs
\[
\rho<\min\{r/2,cK^{-1/2}\}
\]
so that the pullback metric is nonsingular before the first conjugate time. With this choice, Rauch comparison gives the required tangent-space volume lower bound despite collapse on the base manifold.

The radii in A03’s Appendix and A01 §4 differ (\(B_4,B_5\) versus \(B_5,B_6,B_7\)). This is repairable, but the final presentation must use one set of radii ensuring both disjoint \(\chi_\alpha\)-supports and disjoint buffered \(\eta_\alpha\)-supports.

---

## 5. Evidentiary value of the script and implications

`verify_step55_direct_construction.py` does not verify the PDE estimates computationally. Most entries pass because their Boolean value is literally `True`; the Sobolev entries use only one sample \((n,s,r)=(4,10,8)\). It also retains the obsolete “Q-type antisymmetric IBP identity,” while the note correctly replaced that step by weighted Young inequalities. The JSON output therefore records a structural ledger, not mathematical validation of Propositions 2.1–6.1.

Scientifically, Step 55 is still a substantial repair: it gives the right transported scalar, the right product Lie derivative, the right regularization, and a convincing mechanism preventing \(\varepsilon^{-1}\) losses. With a corrected tame hierarchy, it plausibly establishes per-datum existence of the exact cutoff flow.

It does not yet complete the restricted Ishida–LeBrun theorem. The family-independent first-exit/continuation chain, terminal chart construction, and propagation of \(Q=o(A)\) remain unproved in the supplied files. The full Yau 26 proposition is much farther away: the present construction addresses an analytic flow module in dimension four and does not settle arbitrary topology, the \(\operatorname{Ric}\approx +g\) regime, dimensions \(n\ge5\), or the requested Lean formalization.