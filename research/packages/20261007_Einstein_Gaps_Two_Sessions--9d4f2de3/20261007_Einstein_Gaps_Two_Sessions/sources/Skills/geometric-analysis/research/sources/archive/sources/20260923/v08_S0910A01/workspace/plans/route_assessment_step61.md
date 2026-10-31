# Route assessment: Step 61

Session S0910A01, Agent2, Execute.

> **Step 62 update.** The defect Moser endpoint gate result below is
> superseded. Step 62 (`workspace/notes/step62_defect_moser_general_p_proof.md`)
> closes the blocking gap via the three-factor route. The endpoint
> $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$ is established. See
> `workspace/plans/route_assessment_step62.md` for the updated status.
## What Step 61 established

A **gate audit** (not confirmation) of the three load-bearing analytic modules
for the restricted four-dimensional negative Ishida--LeBrun cutoff-flow theorem,
following the Strategist's correction that prior audit assignments presupposed
the verdict.

## Gate results

### Defect Moser endpoint: FAILED

The $J_6$ persistence via two-factor absorption is sound and $Y$-independent.
The $L^\infty$ endpoint $\|aE\|_\infty \le C\delta(r^2/t)^{1/3}$ is
**unestablished** because:

1. The general-$p$ two-factor defect inequality needed for Moser iteration is
   not proved (only $p=6$ exists).
2. The nested Moser recurrence is cited, not derived; the seed $H_{p_0}$ is
   undefined, and the exponent $1/3$ vs $1/2$ depends on its definition.
3. The index-level defect evolution from Ricci variation is stated as premise.

This is the **single blocking gap**. Without the defect endpoint, the metric
drift $V(T) = \int_0^T\|aE\|_\infty dt$ cannot close, so the $(\Gamma,V)$
bootstrap has no $V$-leg, and the first-exit interval cannot be closed.

### Curvature Moser endpoint: CONDITIONAL

The internal logic is sound and compatible with the Step 55 $(\Gamma,V)$
repair. The missing items are:

1. Index-level tensor identities (pure-scaling checksum needed).
2. Display repair: insert $C_V\|aE\|_\infty H$ into the $H$-inequality.
3. Record $A = e^{8V_*}$ explicitly.

No structural gap in the Moser machinery itself.

### Per-datum existence: CONDITIONAL

The tame hierarchy, maximum principle, smooth limit, pullback, and autonomous
splice are verified. Missing:

1. Fixed-parameter parabolic existence pinned to a named theorem.
2. Time-derivative induction displayed.
3. DeTurck identity conventions fixed.
4. Derivative-reordering lemma at tensor-index level.
5. Upstream first-exit estimates (depends on the failed defect endpoint).

## Theorem status after audits

The restricted IL theorem has **one blocking gap** (defect Moser general-$p$
inequality + nested recurrence) and several conditional premises. The theorem
remains conditional. The audit changes the stated status: the defect endpoint
was previously carried as "established at the same level as the curvature
endpoint" (A03 #420), but the gate shows it has a structural gap that the
curvature endpoint does not share.

## Revised module status

| Module | Previous status | After Step 61 gate |
|--------|----------------|-------------------|
| Coupled $(\Gamma,V)$ bootstrap | Proof level (Step 55) | Proof level |
| Curvature Moser endpoint | Proof level (A03 Step 58) | Conditional (tensor premises) |
| Defect Moser endpoint | "Same level as curvature" (A03 #420) | **FAILED** (general-$p$ + recurrence) |
| Base pair ($m=1$) | Proof level (Step 60) | Proof level |
| All-order continuation | Structurally verified (Steps 59-60) | Structurally verified |
| Terminal compactness | Proof level (Step 56) | Proof level |
| Derdziński forbidden germ | Source-verified | Source-verified |
| Per-datum existence | Credible skeleton (A03 Step 56) | Conditional (cited-standard) |

## What the next step should attack

The blocking gap is the defect Moser endpoint. Specifically:

1. **Prove the general-$p$ two-factor defect inequality** for even $p \ge 6$:
   show the chain rule for $s^{p/2}$ gives principal dissipation $\ge cp^2 D_p^E$,
   the signed Hessian tensor satisfies $|\nabla B| \le Cs^{1/2}|\nabla E|$
   uniformly in $p$, and the reaction absorbs by
   $P_p \le Cp^2\gamma_t(D_p^E + r^{-2}J_p)$.

2. **Derive the nested Moser recurrence explicitly**: define $H_{p_0}$,
   establish the nested time-slab structure, verify product convergence of
   $p$-dependent constants, and determine the correct time exponent ($1/3$ or
   $1/2$).

3. If the exponent turns out to be $1/2$ instead of $1/3$, the metric drift
   becomes $V(T) \lesssim \delta r^2\theta^{1/2}$, which still closes the
   bootstrap but with different scaling. The $V$-leg closes either way for
   small $\delta$; the difference is quantitative, not structural.

## Broader research context

A03's graph-manifold route (Step 63, corrected) is now a gap-theorem candidate
rather than a counterexample route: $T^3$ cannot carry $\operatorname{Ric}=-2g$,
so the exact funnel exists only over hyperbolic 3-manifolds. The flat-slice
barrier $H^2 \ge 9-6\delta$ remains valid. A03's quantifier normalization
(message #440) correctly reduces Yau 26 to two independent single-sign
questions, which aligns with the session's existing sign-branch framework.

The IL theorem and the graph-manifold analysis sharpen each other: a completed
IL gap excludes tightly pinched negative counterexamples on calibrated SW
geographies; any refutation must then live where no such calibration budget
exists (graph manifolds, mixed fillings, the positive-collapse region).
