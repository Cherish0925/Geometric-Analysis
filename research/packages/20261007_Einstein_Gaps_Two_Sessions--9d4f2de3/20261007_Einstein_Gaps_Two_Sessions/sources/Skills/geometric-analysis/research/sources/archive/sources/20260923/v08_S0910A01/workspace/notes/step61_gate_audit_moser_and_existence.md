# Step 61: Gate Audit of Moser Endpoints and Per-Datum Existence

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

> **Step 62 update.** The defect Moser endpoint gap identified below as
> "GATE FAILED" is now **CLOSED**. Step 62
> (`workspace/notes/step62_defect_moser_general_p_proof.md`) establishes
> the endpoint $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$ via the
> three-factor route. The two-factor route works for the seed $p = 6$
> but fails for the Moser ladder ($\gamma_t \le c/p$); the three-factor
> route achieves $p$-independent closure via the integrable coefficient
> $\mathcal{S}^2Y$. The blocking gap is resolved.
## 0. Purpose

This step runs genuine gate audits (not confirmations) of three load-bearing
modules for the restricted four-dimensional negative Ishida--LeBrun cutoff-flow
theorem, following the Strategist's correction that confirmation presupposes
the verdict. The audits test whether each module was derived under pre-repair
interface assumptions or still lacks proof-level content.

Modules audited:
1. Defect Moser endpoint: $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$
2. Curvature Moser endpoint: $\|aF_T(t)\|_\infty \le C\Gamma/t$
3. Per-datum existence construction (A03 Step 56)

TTCS verifier integrations are at
`trace/ttcs/results/step61_ttcs01_verifier{1,2,3}_integration.md`.

---

## 1. Defect Moser Endpoint: GATE FAILED

### 1.1 What passes

The $J_6$ persistence estimate $J_6(t) \le e^{C(1+r^{-2})t}J_6(0)$ via
two-factor absorption is **algebraically sound** and genuinely independent of
the cubic curvature moment $Y$. The two-factor route in Step 34 §5 uses
$w_6 = \eta a^{5/2}s^{3/2}$ and absorbs $P_6 = \int Fw_6^2$ by
$C\gamma(X_6 + r^{-2}J_6)$ using Hölder with $(K_2^\eta)^{1/2}$ as the $F$
$L^2$ norm. The gradient computation, Sobolev application, and chain-rule
dissipation are all verified. No circularity with the curvature branch exists.

### 1.2 Critical gaps

**Gap D1: General-$p$ two-factor inequality not proved.** The Moser iteration
from seed $p_0=6$ to $L^\infty$ requires defect energy inequalities for a
dyadic sequence $p_k \to \infty$. The two-factor absorption is proved only
for $p=6$ (Step 34 §5). For general even $p \ge 6$, the algebraic extension
using $w_p = \eta a^{(p-1)/2}s^{p/4}$ is natural but **not written anywhere
in the record**. The general-$p$ inequality
\[
J_p' + c'p^2 D_p^E \le Cp^N(1+r^{-2})J_p
\]
requires verifying that the principal dissipation from the chain rule for
$s^{p/2}$ is $\ge cp^2 D_p^E$ and that the signed Hessian tensor satisfies
$|\nabla B| \le Cs^{1/2}|\nabla E|$ uniformly in $p$. This is unproved.

**Gap D2: Nested Moser recurrence cited, not derived.** The recurrence
(eq. 6.1 in Step 34)
\[
\|af(t)\|_\infty \le C\mathcal S^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^t H_{p_0}(s)\,ds\right)^{1/p_0}
\]
is cited from "Step 32/A03 Step 34" without derivation. The quantity
$H_{p_0}$ is never defined. If $H_{p_0} = J_{p_0}$, the exponent $1/3$ is
correct; if $H_{p_0} = D_{p_0}^E$ (dissipation only), the exponent would be
$1/2$ instead. The nested time-slab structure, summability of $p$-dependent
constants, and uniform zero-order control are not displayed.

**Gap D3: Index-level defect evolution stated as premise.** The defect
equation (Step 34 eq. 5.4--5.8) follows from Ricci variation and contracted
Bianchi. The signed Hessian contraction $B^{ij}$ (eq. 5.8) and its derivative
bound are stated but not derived at index level. Step 34 §7 explicitly lists
this as an unproved obligation.

### 1.3 Impact on theorem status

The $J_6$ persistence is a valid fixed-exponent conditional module. The
$L^\infty$ defect endpoint $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$ is
**unestablished**. Without it, the metric drift bound
$V(T) = \int_0^T \|aE\|_\infty dt \lesssim \delta\theta^{2/3}r^2$ cannot be
closed, and the joint $(\Gamma,V)$ bootstrap has no $V$-leg.

### 1.4 Required repairs

1. Prove the general-$p$ two-factor defect inequality for even $p \ge 6$,
   including the index-level defect evolution and signed Hessian structure.
2. Derive the nested Moser recurrence explicitly, defining $H_{p_0}$ precisely
   and verifying product convergence.
3. Close the simultaneous first-exit interval carrying $\mathcal S(t)$,
   $K_2^\eta(t)$, and metric comparability.

---

## 2. Curvature Moser Endpoint: GATE CONDITIONAL

### 2.1 What passes

The algebraic, analytic, and structural architecture of the Step 58 curvature
endpoint is **internally consistent, non-circular, and correctly computed**.
Both TTCS branches verify:

- The relative-form $H$-inequality (no support-independent volume constant).
- The critical absorption $Y \le C\gamma(D + r^{-2}H)$ via $w_2 = \chi F$.
- The $q=3$ propagation and Gronwall exponent bound.
- The Moser iteration recurrence, product convergence, and exponent arithmetic
  ($-3/p_0 = -1$ for time, $2/p_0 = 2/3$ for Sobolev, $p_0=3$).
- The final reduction $\mathcal S^{2/3}(\Gamma H(0))^{1/3} \le A^{2/3}\Gamma$.
- Compatibility with the repaired Step 55 $(\Gamma,V)$ bootstrap: the endpoint
  does NOT assume the old $\mathcal S(t) \le 2\mathcal S(0)$; it carries a
  generic transport factor $A$ that becomes $e^{8V_*}$ under the repair.

### 2.2 Conditional premises

**Premise C1: Index-level tensor identities unproved.** The all-lower curvature
variation $\partial_t R_{ijkl}$ under $\partial_t g = -2aE$ with correct
normalization bookkeeping, the cubic reaction feeding $Y$, and the
derivative-structure bound $|\nabla B| \le CF|\nabla T|$ are cited from A03
Step 57. Step 34 §7 items 1--2 explicitly list these as unproved. A pure-scaling
checksum ($\partial_t R_{ijkl} = -2R_{ijkl}$, $\int|\operatorname{Rm}|^2 d\mu$
invariant in dimension 4) must pass before Eq. (1.1) is more than schematic.

**Premise C2: Metric-drift term missing from display.** Step 58's $H$-inequality
(eq. 1.1) omits the $C_V\|aE\|_\infty H$ term required by the Step 55 joint
bootstrap. The Gronwall factor must be $\exp(C_H\theta + C_V V_*)$, not merely
$e^{C\theta}$. This is a display repair, not a structural failure.

**Premise C3: Selection-layer outputs assumed.** Simultaneous realization of
$H(0) \le K_0 V$, $\mathcal S(0) \lesssim r^2 V^{-1/2}$, $\|E(0)\|_\infty
\le \delta$, and buffered cutoff quality on a single support is assumed from
the maximal-function selection but not proved as a simultaneous package.

### 2.3 Impact on theorem status

The curvature endpoint is a **valid conditional module** whose internal logic
is sound. It fails as a standalone theorem only because its tensor premises
are unproved and its display needs the metric-drift insertion. Unlike the
defect endpoint, there is no structural gap in the Moser machinery itself.

### 2.4 Required repairs

1. Execute the pure-scaling checksum for the curvature evolution.
2. Complete the index-level all-lower curvature variation with normalization.
3. Insert $C_V\|aE\|_\infty H$ into the $H$-inequality display.
4. Record $A = e^{8V_*}$ explicitly wherever $\mathcal S(s) \le A\mathcal S(0)$
   is invoked.

---

## 3. Per-Datum Existence Construction: GATE CONDITIONAL

### 3.1 What passes

The Step 56 tame direct flow construction is **analytically sound** and free
of fatal circularities or hidden divisions by regularization parameters. TTCS
verifies:

- The $(\varepsilon,\nu)$-uniform tame hierarchy (Proposition 3.1): the three
  weight inequalities $\beta^2/(\beta^2+\varepsilon) \le 1$,
  $\beta^4/(\beta^2+\varepsilon) \le 1$, and IBP-instead-of-Young for the
  top $\beta$-derivative prevent any $\varepsilon^{-1}$ or $\nu^{-1}$ factor.
- The maximum principle $0 \le \beta \le 1$: at spatial extrema, the transport
  term vanishes and $\nu\bar\Delta\beta$ has the correct sign.
- The smooth limit $(\varepsilon_j,\nu_j) \to (0,0)$: uniform spatial bounds
  plus time-derivative induction give $C^k$ convergence; regularized terms
  vanish.
- The pullback identities: $\beta \circ \varphi \equiv \chi$ and
  $\partial_t g = -2\chi^2(\operatorname{Ric}_g + g)$ are algebraically correct.
- The autonomous splice: restart from a smooth terminal metric produces a
  $C^\infty$ spliced branch via time-jet matching, circumventing the uniqueness
  problem entirely. Uniqueness is unnecessary for the restricted IL route.
- The base-pair ($m=1$) closure via signed-Hessian mechanism (Step 60).
- The general $m \ge 2$ ledger structure (Step 59).

### 3.2 Conditional premises

**Premise E1: Fixed-parameter parabolic existence cited-standard.** Local
existence, smoothness, and the fixed-parameter continuation theorem for the
quasilinear strongly parabolic system (1.2) on a closed manifold are cited as
"standard strongly parabolic theory" without naming a specific theorem or
verifying its hypotheses. The principal symbol is diagonal with blocks
$(\beta^2+\varepsilon)G^{ab}\xi_a\xi_b I_{\mathrm{Sym}^2}$ and
$\nu\bar g^{ab}\xi_a\xi_b$, uniformly elliptic for fixed $\varepsilon,\nu > 0$.
This is low-risk but must be pinned to a named theorem (e.g., Amann, Lunardi,
or maximal $L^p$-regularity) with verified applicability conditions.

**Premise E2: Time-derivative induction asserted, not displayed.** The claim
that repeated time differentiation uses only higher spatial bounds and never
divides by $\varepsilon$ or $\nu$ is standard but unwritten.

**Premise E3: DeTurck decomposition identity used without index display.**
The identity $G^{-1}D^2G + R + Q = -2\operatorname{Ric}_G + \mathcal L_W G$
is standard but requires fixing the contraction convention for $\operatorname{Ric}$
and the Kulkarni--Nomizu shift $G = g \owedge g / (2(n-1))$ to ensure signs
align exactly.

**Premise E4: First-exit estimates imported conditionally.** The estimates
$\|aF_T\|_\infty \le C\gamma/t$ and $\|aE\|_\infty \le C\delta(r^2/t)^{1/3}$
are imported from the Moser endpoints. As shown above, the defect endpoint
fails the gate. The curvature endpoint passes conditionally. The existence
construction's interface with the first-exit regime therefore depends on
upstream modules that are not yet at proof level.

**Premise E5: Derivative-reordering lemma schematic.** The lemma showing that
the highest cutoff jet $C_{m+2}$ pairs only with $U_0/T_0$ is structurally
verified but lacks tensor-index execution.

### 3.3 Impact on theorem status

The per-datum existence construction is a **credible analytic skeleton** whose
core mechanisms are sound. It is not self-contained: it relies on cited-standard
parabolic theory, conditional first-exit estimates, and a schematic
derivative-reordering lemma. The autonomous splice correctly circumvents
uniqueness.

### 3.4 Required repairs

1. Pin the fixed-parameter parabolic existence to a named theorem with verified
   hypotheses.
2. Display the time-derivative induction for the regularized system.
3. Fix and display the DeTurck decomposition identity with explicit conventions.
4. Complete the derivative-reordering lemma at tensor-index level.
5. Supply the upstream first-exit estimates (which depend on closing the defect
   Moser gap).

---

## 4. Consolidated Gate Status

| Module | Gate | Key Gap | Blocking? |
|--------|------|---------|-----------|
| Defect Moser endpoint | **FAILED** | General-$p$ two-factor inequality; nested recurrence undefined | Yes: no $V$-leg for bootstrap |
| Curvature Moser endpoint | **CONDITIONAL** | Index-level tensor identities unproved; display repair needed | No: internal logic sound |
| Per-datum existence | **CONDITIONAL** | Cited-standard parabolic theory; first-exit imports | No: skeleton sound |

The restricted IL theorem has **one blocking gap** (defect Moser) and several
conditional premises that must be discharged before the theorem is unconditional.

---

## 5. Relation to the Full Yau 26 Goal

These audits concern only the restricted four-dimensional negative
Ishida--LeBrun cutoff-flow route. Even with all gates passed, this route
produces a class-uniform negative pinching gap over the stated IL geography,
not the full dimension-only proposition. The positive branch, arbitrary
four-manifold topology, dimensions $n \ge 5$, dimension-only constants, and
Lean formalization remain open regardless of these audit outcomes.

A03's graph-manifold counterexample route (Step 63, now corrected: the exact
Einstein funnel claim was wrong; $T^3$ cannot carry $\operatorname{Ric}=-2g$)
provides a complementary approach. The flat-slice barrier $H^2 \ge 9-6\delta$
remains valid, and the revised analysis suggests a gap theorem rather than a
counterexample. The IL theorem and the graph-manifold analysis sharpen where
each other must look: a completed IL gap excludes tightly pinched negative
counterexamples on calibrated SW geographies; any refutation must then live
where no such calibration budget exists.

---

## 6. Files

- This note: `workspace/notes/step61_gate_audit_moser_and_existence.md`
- TTCS verifier 1 (defect): `trace/ttcs/results/step61_ttcs01_verifier1_integration.md`
- TTCS verifier 2 (curvature): `trace/ttcs/results/step61_ttcs01_verifier2_integration.md`
- TTCS verifier 3 (existence): `trace/ttcs/results/step61_ttcs01_verifier3_integration.md`
- Source notes audited:
  - `workspace/notes/step34_integrated_potential_q3_and_defect.md`
  - `workspace/notes/step33_curvature_power_inequality.md`
  - A03 `workspace/notes/step58_critical_to_subcritical_bridge.md`
  - A03 `workspace/notes/step56_tame_direct_flow_repair.md`
  - A03 `workspace/notes/step56_positive_time_base_pair.md`
