# Step 24: Corrected curvature evolution, conditional downstream chain, and precise gap status

> **STEP 25 SUPERSESSION.** The tensor term \(-2a\operatorname{Rm}\) in the fully covariant evolution is correct, but Section 1.4 below incorrectly treated it as net damping for the evolving curvature energy. The four inverse metrics contribute \(+8a|\operatorname{Rm}|^2\), so together with the tensor contribution \(-4a|\operatorname{Rm}|^2\) and the four-dimensional measure variation \(-4a\,d\mu\), the pure constant-homothety contribution to \(|\operatorname{Rm}|^2d\mu\) is exactly zero. For \(F^2=1+|\operatorname{Rm}|^2\), it is only \(-4a\,d\mu\). The useful weak inequality retains harmless lower-order reactions but no normalization coercivity. Sections 2.3--2.5 also incorrectly let plateau regularity replace whole-support transition control. The first-exit requires positive-time bounds for \(a\operatorname{Rm}\) and \(aE\) on all of \(\operatorname{supp}\chi\); Step 25 restores them through the Wang/Yang weighted iteration. The terminal obstruction remains the Step 6 Einstein--Weyl identity contradiction, not a classification of locally symmetric Einstein spaces.

## 1. Critical correction to the normalization reaction

### 1.1 The error

Steps 22–23 claimed that the normalization piece $h = -2ag$ of the flow
velocity produces NO linear curvature reaction.  This is **false** for the
fully-lowered tensor $R_{ijkl}$.  The Chow–Lu–Ni formula governs the mixed
tensor $R^l{}_{ijk}$, whose conformal lower-order terms do cancel.  But the
physical curvature is $R_{ijkl} = g_{lm}R^m{}_{ijk}$, and index-lowering adds

$$
 h_{lm}R^m{}_{ijk} = (-2a)\,g_{lm}R^m{}_{ijk} = -2a\,R_{ijkl}.
\tag{1.1}
$$

**Decisive test (TTCS):** for $a\equiv1$, $\partial_tg=-2g$ gives
$g(t)=e^{-2t}g_0$.  The Christoffel symbols and $R^l{}_{ijk}$ are unchanged,
but $R_{ijkl}(t)=e^{-2t}R_{ijkl}(0)$, hence
$\partial_tR_{ijkl}=-2R_{ijkl}$.

### 1.2 The corrected evolution

The full flow $\partial_tg=-2a(\operatorname{Ric}+g)$ gives

$$
\boxed{
 \partial_t\operatorname{Rm}
 =a\Delta\operatorname{Rm}+aQ(\operatorname{Rm})-2a\operatorname{Rm}
 +\mathcal C(\nabla a,\nabla E)-(\nabla^2a\owedge E).
}
\tag{1.2}
$$

Term-by-term:
- $a\Delta\operatorname{Rm}$: leading degenerate Laplacian.
- $aQ(\operatorname{Rm})$: Wang's standard quadratic reaction (cubic in Rm).
- $-2a\operatorname{Rm}$: **normalization damping** (linear, beneficial).
- $\mathcal C(\nabla a,\nabla E)$: first-order cross terms.
- $-(\nabla^2a\owedge E)$: Kulkarni–Nomizu Hessian source (homogeneous in $E$).

### 1.3 Stationarity under the Einstein–Lichnerowicz identity

For $\operatorname{Ric}=-g$ (negative Einstein), $E=0$, $h=0$, and
$\partial_t\operatorname{Rm}=0$ trivially.  But the mechanism is worth recording:
the Lichnerowicz identity for Einstein four-manifolds gives

$$
 \Delta\operatorname{Rm}+Q(\operatorname{Rm})=2\operatorname{Rm},
$$

so $a(\Delta\operatorname{Rm}+Q-2\operatorname{Rm})=0$ even before $E=0$ is used
for the cross terms.

### 1.4 Effect on the energy framework

For $F^2=1+|\operatorname{Rm}|^2$, the linear damping contributes

$$
 2R^{ijkl}(-2aR_{ijkl})=-4a|\operatorname{Rm}|^2=-4a(F^2-1).
\tag{1.3}
$$

In the integrated $H_2$ inequality this adds
$+4\int\eta^2aF^2$ on the left (beneficial damping) and $-4\int\eta^2a$
on the right (bounded source $\le 4\operatorname{Vol}$).  The cubic reaction
constant in Step 23's estimate (2.7) is unchanged; the damping is an
additional term that improves energy persistence.  Therefore the energy
framework **survives** with a better coefficient, not a worse one.

---

## 2. Precise conditional status of the downstream chain

The TTCS verification identified that "conditional on $q=2,3$ energy
inequalities" is **not sufficient** for the full downstream chain.  The
precise dependencies are:

### 2.1 What the $q=2$ inequality gives (conditionally)

Assume the integrated tensor inequality

$$
 H_2'+cD_2\le C\int\eta^2aF^3+Cr^{-2}H_2+C_0
\tag{2.1}
$$

with $C_0=O(\operatorname{Vol})$.  The matched Sobolev absorption with
$\gamma=A^2\|F\|_2$ then gives:

- $H_2(t)\le e^{C\theta}H_2(0)$ (energy persistence).
- $\int_0^TD_2\le CH_2(0)$ (integrated dissipation).
- $\int_0^TH_3\le C\gamma_*H_2(0)$ (spacetime cubic).

These are **unconditional** consequences of (2.1) on the provisional bilipschitz
interval.

### 2.2 What the $q=3$ inequality adds

Assume the separate tensor inequality

$$
 Y'+cD_3\le Cr^{-2}Y+CI_4,\qquad I_4=\int\eta^2a^2F^4,
\tag{2.2}
$$

with the correct absorption $I_4\le C\gamma(D_3+r^{-2}Y)$.  Then:

- Time-average + forward propagation → $A^4Y(t)\le C\gamma^3/t$.

### 2.3 What is NOT automatic from $q=2,3$ alone

To go from $H_3(t)\le C\gamma^3/(A^4t)$ to $|aF|\le C\gamma/(A^2t)$
(the weighted $L^\infty$ bound), one needs **one of**:

(A) **All-$q$ energy inequalities** with per-step constants growing at most
    polynomially in $q$; or

(B) **A scalar Moser theorem** for the degenerate operator
    $\partial_t-a\Delta$ with an $L^3$ potential on the buffered support.

Standard option (B) is available **on the plateau** $\{a=1\}$, where the
equation is uniformly parabolic.  There:

- Interior parabolic regularity (normalized Ricci flow estimates) gives
  $|\operatorname{Rm}|\le C/t$ on $B_{3r}\subset\{a=1\}$ from
  $\int_{B_{4r}}F^3\le C/t$.

Option (A) is needed only if one wants $|aF|\le C/t$ on the **whole support**
including the transition annulus.  For the gap theorem, the projector
contradiction lives on the plateau, so (B) suffices.

### 2.4 Defect propagation: independent chain

The defect iteration uses:

- $J_6(t)\le e^{C\theta}J_6(0)\le C\delta^6\operatorname{Vol}$ (from the
  independent homogeneous defect inequality, NOT from the curvature chain).
- Bounded curvature on the plateau at positive time (from §2.3).
- Standard subcritical Moser for $|E|$ on the plateau, using the $L^3$
  curvature potential.

The resulting bound $|E|(t)\le C\delta(r^2/t)^{1/3}$ on the plateau is
conditional on both the $q=2,3$ curvature and the $J_6$ defect inequalities.

### 2.5 Metric drift and first-exit

Given $|aE|\le C\delta(r^2/t)^{1/3}$:

$$
 \int_0^{\theta r^2}|aE|\,dt\le\tfrac32C\delta\theta^{2/3}r^2.
\tag{2.3}
$$

For $\delta<\delta_0(\theta)$ this is $<1/10$, giving bilipschitz with
factor $<e^{1/5}<2$.  The first-exit bootstrap is:

- **Sobolev**: stable under bilipschitz.
- **Energy**: from absorbed $q=2$ (§2.1).
- **Curvature**: from interior regularity on plateau (§2.3(B)).
- **Defect**: from $J_6$ + subcritical Moser on plateau (§2.4).
- **Metric**: self-improves from integrable velocity (§2.5).

---

## 3. Remaining load-bearing work

The precise PDE obligations are:

**T1.** The exact $(0,4)$-tensor evolution inequality for $F^2$ under
$\partial_tg=-2a(\operatorname{Ric}+g)$, including the $-4aF^2$ damping,
the inverse-metric cubic, and the volume-form terms.  Integration against
$\eta^2$ with the buffered support geometry and integration by parts of the
$\nabla^2a\owedge E$ term.

**T2.** The separate $q=3$ tensor inequality with dissipation weight
$a^2F|\nabla\operatorname{Rm}|^2$ and reaction $a^2F^4$, absorbed by the
correct Sobolev variable $u=aF^{3/2}$.

**T3.** The homogeneous defect inequality for $Q=\int|E|^2$ and
$J_6=\int a^4|E|^6$, confirming no curvature-only source.

**T4.** Interior parabolic regularity on the plateau $\{a=1\}$ at positive
time, adapted to the normalized flow.  Standard Shi estimates for
$\partial_tg=-2(\operatorname{Ric}+g)$ should suffice here.

**T5.** Yang–Wang smooth continuation adapted to the normalized lower-order
term, giving existence on $[0,\theta r^2]$ with the required qualitative
regularity.

**T6.** From bounded-curvature plateau to exponential chart, joint monopole
density averaging, calibrated germ, and Derdziński projector contradiction
(the topology/geometry chain from Steps 5–6 and 16, which is conditional
on the analytic input from T1–T5).

---

## 4. Conditional gap theorem: precise statement

**Theorem (conditional).** Let $M^4$ be a fixed critical Ishida–LeBrun manifold
with $D=A/3$.  Assume:

(i) the integrated tensor inequalities T1–T2 hold for the normalized cutoff
    flow with volume-independent constants;

(ii) the homogeneous defect inequalities T3 hold;

(iii) the normalized flow has smooth existence on $[0,\theta r^2]$ (T5).

Then there exists $\varepsilon_0=\varepsilon_0(M)>0$ such that

$$
 \inf_g\|\operatorname{Ric}_g+g\|_\infty\ge\varepsilon_0.
$$

**Proof chain (conditional on (i)–(iii)):**

1. **Support geometry**: Vitali thinning from the maximal-function good set
   gives disjoint buffered supports with positive total volume proportion.
2. **$H_2$ persistence**: from T1 + critical absorption with small $\gamma$.
3. **Spacetime $H_3$**: from integrated $H_2$ dissipation.
4. **Terminal $H_3(t)\le C\gamma^3/t$**: from T2 + time average + forward propagation.
5. **Interior regularity**: standard Shi on the plateau at positive time.
6. **$J_6$ persistence**: from T3 with initial $\delta^6$ factor.
7. **Plateau defect**: subcritical Moser for $|E|$ on the plateau.
8. **Metric comparability**: self-improving from integrable velocity.
9. **First-exit closure**: all five conditions bootstrap simultaneously.
10. **Exponential chart**: Rauch + joint density averaging on the positive-volume
    set of plateau centers.
11. **Smooth local limit**: Cheeger–Naber compactness with calibrated topology.
12. **Forbidden germ**: $W^+$ spectrum $(-1/6,1/12,1/12)$ + Derdziński projector
    → $\nabla W^+=0$ contradicts $|\nabla W^+|^2=1/16$.
13. **Contradiction**: no near-saturating sequence exists.

---

## 5. Scope and open directions

Even a successful resolution of T1–T5 would address only the **critical
four-dimensional negative Ishida–LeBrun subclass**.  Open:

- **Arbitrary negative 4D topology**: requires extending beyond the critical
  boundary $D=A/3$.
- **Positive branch $P_4^+$**: A02's toric analysis (Step 25) shows integral
  identities alone cannot obstruct the $\alpha$-family on $\#_k(S^2\times S^2)$.
  A BUILD theorem needs a global PDE solvability obstruction.
- **Dimensions $n\ge5$**: neither the Ishida–LeBrun obstruction nor the critical
  curvature energy control (which uses $n/2=2$) extends.  A02's KK construction
  shows codim-1 positive collapse is Einstein-compatible in $n\ge5$.
- **Lean formalization**: no work begun.
- **Full Yau 26**: the dimension-only quantifiers remain far from any current result.

## 6. Files and scripts

- `workspace/scripts/verify_step24_exact_curvature_variation.py` — structural checks (PARTIALLY INCORRECT on lower-order; see §1)
- `workspace/scripts/verify_step24_normalization_correction.py` — corrected reaction verification
- `workspace/scripts/verify_step24_downstream_chain.py` — scaling and exponent checks (logic gaps identified in §2)
- `trace/ttcs/results/step24_ttcs01_verifier1_integration.md` — TTCS verification with correction
- A01 `workspace/notes/step24_buffered_support_energy_test.md` — convergent buffered-support construction
- A02 `workspace/notes/step25_build_break_analytic_verdict.md` — positive-branch toric verdict
