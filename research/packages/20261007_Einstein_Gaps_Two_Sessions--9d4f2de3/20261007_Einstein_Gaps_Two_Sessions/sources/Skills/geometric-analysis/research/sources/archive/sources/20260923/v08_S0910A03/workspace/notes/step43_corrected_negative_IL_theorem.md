# Step 43: Corrected near-critical Ishida–LeBrun negative defect gap theorem

> **Step 45 analytic update.** The Step 44 zero-order seed and the repaired coordinate-time ledger in `step45_coordinate_tensor_ledger_and_regularized_closure.md` now give a coherent coefficient-regularization route to per-datum start/restart and arbitrary-order propagation, without importing a self-contained reconstruction of Yang's smooth-tame inverse. This does not by itself certify the entire theorem below: the simultaneous first-exit, support-volume, global-Q, terminal-chart, and topological-density assembly still needs an independent connected review on one realized flow.

## 0. Statement

**Theorem (conditional).** *Let $m \in \{2,3\}$ and
$M_i = (\#_{j=1}^m X_j^{(i)})\#N_i$ be a sequence of closed oriented smooth
$4$-manifolds with*
\[
  A_i = \sum_j c_1^2(X_j^{(i)}),\qquad
  D_i = 4m - (2\chi+3\tau)(N_i),\qquad
  q_i = D_i - A_i/3,
\]
*such that $q_i/A_i \to 0$ and $A_i \to \infty$.  Suppose each $M_i$
carries the Ishida–LeBrun monopole family.  Then there exists
$\varepsilon_4 > 0$ (universal) such that for all sufficiently large $i$,
no smooth Riemannian metric $g_i$ on $M_i$ satisfies*
\[
  \|g_i^{-1}(\operatorname{Ric}_{g_i} + g_i)\|_\infty < \varepsilon_4.
\]

*Proof by contradiction: assuming $\delta_i := \|g_i^{-1}(\operatorname{Ric}_{g_i}
+ g_i)\|_\infty \to 0$, the following chain leads to a contradiction.*

**Step 45 analytic replacement.**  The earlier H-DT/H-AO formulation is
superseded by `step45_coordinate_tensor_ledger_and_regularized_closure.md`.
That note combines the Step 44 zero-order $T_0$ seed with a coordinate-time
all-order ledger and Yang's coefficient-regularization route
$b_\varepsilon=\chi^2+\varepsilon^2$.  It preserves the exact
$B_{r+1}B_{s+1}T_t$ weights, proves regularization-uniform finite-exponent
propagation on a per-datum bootstrap interval, obtains fixed-coordinate smooth
compactness, and supplies existence plus restart by autonomous time-jet
matching.  It does not prove uniqueness of the degenerate flow, which is not
needed to exhibit a continuation.  Independent TTCS reconstruction found no
hidden current derivative, pointwise-$T$ premise, exponent escalation, or
$\varepsilon^{-1}$ after its listed corrections were inserted.

**Current remaining task.**  The theorem in this file is still not promoted to
an established result until the support construction, simultaneous homogeneous
first-exit estimates, global $Q$, terminal buffered chart, and spectral-density
passage have been reread as one argument on the actual regularization-limit
flow.  This is now an assembly verification, not the former standalone
start/restart gap.

## 1. Near-critical calibration

The Chern–Weil identity $(2\chi+3\tau)(M_i) = A_i - D_i = 2A_i/3 - q_i$
and the sign-averaged monopole inequality give:
\[
  \operatorname{Vol}_i/A_i \to 32\pi^2/9,\quad
  R_i/A_i \to 0,\quad
  \int|W_i^+|^2/(\pi^2 A_i) \to 4/27.
\]

The completed-square identity yields:
\[
  \int\left(|W_i^+| - \frac{1}{2\sqrt{6}}\right)^2 \le
  \frac{7}{24}\int|E_i|^2 = \frac{7}{24}Q_i,
\]
where $Q_i = \int|E_i|^2$, $E_i = \operatorname{Ric}_{g_i} + g_i$.

*Source: Codex quantitative_deficit_analysis.md §§2--4; LeBrun Prop.~3.8.*

## 2. Support construction

**Volume-average maximal function.** Choose $R = 7r$, $r > 0$ universal.
Define the maximal-function good set $G_R = \{x : \text{maximal avg of
$1 + |\operatorname{Rm}|^2$ on $B_{R}(x)$} \le \Lambda\}$.  By
CGB, $\int(1+|\operatorname{Rm}|^2) \le C(1+A_i)$, so
$\operatorname{Vol}(G_R^c) \le CA_i/\Lambda$.

**BG coloring and macro-disjoint supports.**  Take a maximal $2r$-separated
net $\{x_\alpha\}$ in $G_R$; Bishop–Gromov doubling gives a chromatic number
$D_7$ (depending on $n=4$ and the Ricci lower bound); select the largest
color class.  The resulting index set $\mathcal A$ satisfies:
\[
  \{B_{6r}(x_\alpha)\}_{\alpha\in\mathcal A}\ \text{pairwise disjoint},\qquad
  \sum_{\alpha\in\mathcal A}\operatorname{Vol}(B_{2r}(x_\alpha))
  \ge \alpha_0\operatorname{Vol}(G_R) \ge \alpha_0'A_i.
\]

**Cutoffs.** Smooth $\chi_\alpha$ with $\chi_\alpha = 1$ on $B_{4r}(x_\alpha)$,
$\operatorname{supp}\chi_\alpha \subset B_{5r}(x_\alpha)$,
$|d\chi_\alpha| \le C/r$.  Auxiliary $\eta_\alpha$ with $\eta_\alpha = 1$ on
$B_{6r}(x_\alpha)$, $\operatorname{supp}\eta_\alpha \subset B_{7r}(x_\alpha)$.
Higher cutoff derivatives may depend on the individual metric.

**Global coefficient:** $a_i = \sum_{\alpha\in\mathcal A}\chi_\alpha^2$.
Satisfies $|da_i|^2/a_i = 4|d\chi_\alpha|^2 \le C/r^2$ on each support.

*Correction from Step 42: no uniform sequence Hessian bound $\|\nabla^2\chi\|_\infty$
is assumed.  The signed IBP mechanism handles all Hessian-$a$ terms using only
$|d\chi| \le C/r$.*

## 3. Normalized cutoff flow and first-exit bootstrap

**Flow equation:**
\[
  \partial_tg_i = -2a_i(\operatorname{Ric}_{g_i(t)} + g_i(t)),
  \qquad g_i(0) = g_i.
\]

**Shifted curvature:**
$G = g\wedge g/(2\cdot3)$, $T = \operatorname{Rm} + G$, $U = aT$.
Then $\operatorname{Ric}(T) = E$, $\operatorname{Ric}(U) = aE$.

**First-exit parameters:** Choose $\theta > 0$ small and set $T_* = \theta r^2$.
The bootstrap controls the following quantities on each support component
$\alpha$ on $[0,T_*]$:

**(a) Curvature energy (homogeneous).**
\[
  K_{2,\alpha}' + cD_{2,\alpha} \le CY_\alpha + C(1+r^{-2})K_{2,\alpha},
\]
with no additive $C_0$ or $C_0T$ term (Step 42 correction).  The critical
absorption coefficient $\gamma_\alpha = \mathcal S_\alpha K_{2,\alpha}^{1/2}
\lesssim r^2\sqrt{K_0}$ is collapse-independent.

Self-improvement: $K_{2,\alpha}(T_*)/K_{2,\alpha}(0) \le e^{C\theta(1+r_0^2)}$.

**(b) Curvature Moser:** $q = 2 \to 3$ propagation, then $p \mapsto 3p/2$
recurrence with dyadic time slabs, giving
$\|aF(t)\|_\infty \le C\gamma/t$.

**(c) Defect persistence ($J_6$ and general $p$).**
$J_6 = \int\eta^2 a^4|E|^6$ obeys a homogeneous Grönwall with
two-factor absorption and coefficient $C(1+r^{-2})$.
General $p \ge 6$:
\[
  (H_p^E)' + c\|\nabla z_p\|_2^2
  \le Cp^4(1+r^{-2}+\mathcal S^2 Y)H_p^E,
\]
using three-factor Hölder (not two-factor, which requires $\gamma \lesssim 1/p$).

**(d) Defect Moser:** $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$.
Metric drift $\int_0^T\|aE\|_\infty\,dt \le C\delta r^{4/3}T^{2/3}$ integrable.

**(e) Global $Q$ propagation:**
\[
  Q_i(T) = \int|E_i(T)|^2 \le e^{C\theta}Q_i(0).
\]
Independent of $J_6$ and $\|aE\|_\infty$; uses support-by-support two-factor
absorption and summation over disjoint $\eta$-supports.

**(f) Continuation (Step 45 coefficient-regularization construction):**
If $\sup|U|\le K$ on $[0,T_*)$ with $T_*<\infty$, the Step 44 zero-order
energy inequality first gives $T_0\in L^p$ for every finite $p$.  The staggered
induction
\[
  T_0 \to (U_1,C_2) \to T_1 \to (U_2,C_3) \to T_2 \to \cdots
\]
is designed to give all finite-exponent bounds for $\nabla^mU$,
$\nabla^{m+1}\chi$, and $\nabla^mT$.  At $m=1$,
$\chi\operatorname{Hess}\chi*|\nabla T|^p$ is handled by signed integration
by parts; at higher order, derivatives of $\partial_t\Gamma$ are estimated
through derivatives of $\operatorname{Ric}(U)$ rather than an assumed
pointwise bound for $T$.  The corrected exhaustive tensor ledger is now supplied by Step 45.  Sobolev
embedding and a fixed-background connection-difference induction give a smooth
endpoint metric; repeating coefficient regularization from that datum and
matching autonomous time jets gives a restart.  This is an existence extension,
not a uniqueness theorem.

**Self-improving first-exit chain:**
Drift $\to$ metric $\to$ Sobolev $\to$ curvature/defect $\to$ drift.
No circularity because drift depends only on $\|aE\|_\infty$ (not on
Sobolev constants), and the Sobolev constants are compared to initial
ones through the bilipschitz comparison.

## 4. Terminal geometric passage (repaired)

**Inner centers.** Let $P_\alpha = B_{g_0}(x_\alpha, r)$.  Under
bilipschitz $e^{-\Lambda}g_0 \le g(t) \le e^{\Lambda}g_0$,
for $p \in P_\alpha$ and $R = e^{-\Lambda/2}r/2$:
\[
  B_{g(t)}(p, 2R) \subset B_{g_0}(x_\alpha, 2r) \subset \{\chi_\alpha = 1\}
  \qquad \forall\, t \in [0,T_*].
\]

**Sequence-uniform curvature on $[T_*/2, T_*]$.**
On the $\chi = 1$ plateau, the flow is
$\partial_t g = -2(\operatorname{Ric} + g)$.
The Moser endpoint gives $|\operatorname{Rm}|(t) \le K_*$ for
$t \in [T_*/2, T_*]$, with $K_*$ depending only on
$r, \theta, \gamma_*$.

**Conversion to ordinary Ricci flow.**
Rescale $\bar g(t) = e^{2(t-T_*/2)}g(t)$ and reparametrize
$ds/dt = e^{2(t-T_*/2)}$; then $\partial_s\bar g = -2\operatorname{Ric}_{\bar g}$.
Local Shi estimates on $B_{g(t)}(p, 2R) \times [T_*/2, T_*]$ give
\[
  |\nabla^m\operatorname{Rm}|(T_*) \le C_m(K_*, R, T_*)
\]
on $B_{g(T_*)}(p, R)$, sequence-uniform.

**Exponential pullback and Liouville–Rauch averaging.**
Choose $\rho < \min(R/8, \pi/(4\sqrt{K_*}))$.  On the pullback chart
$h_i = (\exp_{p_i}^{g_i(T_*)})^*g_i(T_*)$, the derivative bounds
give sequence-uniform $C^\infty_{\rm loc}$ convergence on $B_\rho(0)$.

Select $p_i \in \bigcup_\alpha P_\alpha$ minimizing the Riemannian
pullback mean of the terminal density $\mathfrak D$:
\[
  \fint_{B_\rho(0),h_i}\mathfrak D_i(\exp_{p_i}v)\,d\mu_{h_i}(v) \to 0.
\]

## 5. Terminal spectral density and contradiction

**Simplified terminal density (Step 43 derivation):**
\[
  \mathfrak D = |E|^2 + (s+4)^2 + (s + 8\sqrt{6}|W^+|)^2 + G,
\]
where $G = f^2 - (b_-)^2$ with $f = 2s/3 - 2\sqrt{2/3}|W^+|$,
$b = 2s/3 + 2w_{\min}$.

**Integral bound (Theorem 4.1 of step43_terminal_density_G_lemma.md):**
\[
  \int\mathfrak D \le 119Q(T_*) + 912\pi^2(-q_i)_+.
\]
Since $Q(T_*) \le e^{C\theta}Q_i(0) = e^{C\theta}\delta_i^2\operatorname{Vol}_i
\lesssim A_i\delta_i^2$ and $(-q_i)_+/A_i \to 0$:
$\int\mathfrak D_i/A_i \to 0$.

**Smooth convergence and vanishing density.**
The strong $C^\infty$ convergence on the pullback chart gives:
\[
  h_i \to h_\infty \quad C^\infty_{\rm loc},\qquad
  \operatorname{Ric}_{h_\infty} = -h_\infty.
\]
Each component of $\mathfrak D$ is a continuous function of the
curvature.  Lipschitz continuity of eigenvalues and $x \mapsto x_-$ give
$G_i \to G_\infty$ uniformly.  Combined with $\mathfrak D \ge 0$
and vanishing mean:
\[
  E_\infty = 0,\quad s_\infty = -4,\quad
  |W_\infty^+|^2 = 1/24,\quad G_\infty = 0.
\]

**Spectral determination (Lemma 1.2):**
$G = 0$ at $s = -4$, $|W^+|^2 = 1/24$ forces
\[
  \operatorname{Spec}(W_\infty^+) = (-1/6, 1/12, 1/12).
\]

**Derdziński contradiction.**
$\delta W^+ = 0$ (Einstein) and constant simple/double eigenvalue structure
$\Rightarrow$ $\nabla W^+ = 0$ (projector argument from Step 6).
But Einstein–Weyl with $s = -4$, $|W^+|^2 = 1/24$,
$\det W^+ = -1/864$:
\[
  0 = 2|\nabla W^+|^2 - 1/6 + 1/24 = 2|\nabla W^+|^2 - 1/8,
\]
giving $|\nabla W^+|^2 = 1/16 \ne 0$.  **Contradiction.**

Alternatively: Derdziński Prop.~5 makes the limit locally Kähler–Einstein
with $|W^+|^2 = s^2/24 = 2/3 \ne 1/24$.

## 6. What is proved and what remains

### Modules assembled (the connected theorem still awaits the review stated above):
- Near-critical calibrated profiles and topological excess control
- Volume-average support with gradient cutoffs (no Hessian input)
- Homogeneous $K_2$ with componentwise relative self-improvement
- $J_6$ persistence and general-$p$ defect inequality ($p \ge 6$)
- Curvature and defect Moser endpoints with integrable drift
- Global $Q$ propagation via disjoint-support summation
- $m = 1$ unweighted $\nabla T$ estimate
- $m = 2$ coupled $(U_2, C_3)$ continuation mechanism
- Signed Hessian IBP removing uniform $\nabla^2\chi$ requirement
- Terminal density $\int G \le 6Q + 48\pi^2(-q)_+$
  (focused gauge-theoretic derivation)
- Buffered terminal centers with local Shi estimates
- Strong curvature convergence on exponential pullback charts
- Spectral determination via $G = 0$ and Derdziński contradiction

### Updated analytic interface

Step 45 replaces the former H-DT/H-AO/H-UT list by one coefficient-regularized
construction.  Its coordinate-time ledger supplies the staggered
$(U_m,C_{m+1})\to T_m$ estimates, and the smooth $\varepsilon\downarrow0$
limit supplies per-datum start and restart.  Degenerate-flow uniqueness remains
open but is not needed for existence of a continuation.  The unresolved work
for this restricted theorem is now an independent connected verification of
the simultaneous first-exit and terminal geometric assembly on that flow.

### Scope limitations (even after H-DT, H-AO, H-UT):
- Covers only near-critical Ishida–LeBrun families in dimension $4$
- Does not cover arbitrary $4$-manifold topology
- Does not address the positive normalized branch
- Does not cover dimensions $n \ge 5$
- Does not provide dimension-only constants
- No Lean 4 formalization

## 7. File cross-references

| Component | File |
|---|---|
| General-$m$ $\nabla T$ | `workspace/notes/step43_general_order_unweighted_T_estimate.md` |
| Terminal $G$ lemma | `workspace/notes/step43_terminal_density_G_lemma.md` |
| Codex deficit analysis | `workspace/codex_loop/work/quantitative_deficit_analysis.md` |
| Projector obstruction | `workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex` |
| Homogeneous $K_2$ | `workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md` |
| $J_6$ lemma | `workspace/notes/step35_unregularized_J6_persistence_lemma.md` |
| General-$p$ defect | `workspace/notes/step39_general_p_defect_power_inequality.md` |
| Signed Hessian IBP | `workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md` |
| $m=2$ continuation | `workspace/notes/step40_m2_coupled_continuation_mechanism.md` |
| Staggered schedule | `workspace/notes/step40_staggered_all_order_continuation_candidate.md` |
| DeTurck existence | `workspace/notes/step37_transported_deturck_existence.md` |
| Global $Q$ | `workspace/notes/step37_global_Q_persistence.md` |
| A01 synthesis | `Sessions/S0910A01/workspace/notes/step39_complete_conditional_defect_gap_theorem.md` |
| Step 42 TTCS repairs | `trace/ttcs/results/step42_ttcs01_verifier1_integration.md` |
| Step 42 TTCS terminal | `trace/ttcs/results/step42_ttcs01_verifier2_integration.md` |
| Verification | `workspace/scripts/verify_step43_terminal_density.py` (26/26) |
