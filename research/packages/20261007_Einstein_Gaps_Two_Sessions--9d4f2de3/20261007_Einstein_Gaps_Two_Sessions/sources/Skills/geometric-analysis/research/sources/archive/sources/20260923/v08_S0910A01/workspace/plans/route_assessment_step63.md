# Route assessment: Step 63


> **Step 64 correction.** The Step 63 tensor note remains the curvature endpoint
> input as an inequality, but its exact pure-scaling table was repaired in
> `workspace/notes/step64_convention_consistency_sweep.md`: with the canonical
> standard-KN convention $G=(g\owedge g)/(2(n-1))$, $T=\operatorname{Rm}-G$,
> one has $\partial_tG=-4G$ under pure scaling, hence
> $\partial_tT=-2T+2G$, not $-2T$. The false homogeneous shifted-curvature line
> has no role in the estimates because the added zero-order term is algebraic in
> $E=\operatorname{Ric}(T)$ and is absorbed by $CaF_T^3$. The curvature norm is
> operator-normalized; this is why $|G|^2=n/(2(n-1))=2/3$ in dimension four.
> The structural script was updated and now passes 21/21.
Session S0910A01, Agent2 / Constructor. Phase: Execute.

## What was done

Step 63 closed the curvature endpoint tensor identities (Premise C1 from the
Step 61 gate audit) at index level. The proof note
`workspace/notes/step63_curvature_variation_index_proof.md` provides:

1. **All-lower curvature variation** $\partial_t R_{ijkl}$ under
   $\partial_t g = -2aE$ with the pure-scaling checksum
   $\partial_t R_{ijkl} = -2R_{ijkl}$ for $a \equiv 1$, $E = g$.
2. **Explicit Hessian tensor $B$** from the $\nabla^2 a$ terms in
   $\partial_t R_{ijkl}$, with the derivative-structure bound
   $|\nabla B| \le CF_T|\nabla\operatorname{Rm}|$ (Lemma 4.1).
3. **Metric-drift display** $C_V\|aE\|_\infty H$ inserted into the $H_2$
   inequality (8.2), with $A = e^{8V_*}$ recorded explicitly.
4. **Signed IBP closure** with cutoff cross term vanishing on
   $\operatorname{supp}(d\eta)$ and Young absorption using only
   $|d\chi| \le Cr^{-1}$.

TTCS verification (`trace/ttcs/results/step63_ttcs01_verifier1_integration.md`)
found genuine tensor-bookkeeping errors, all repaired:
- KN product sign conflict: standard KN gives $\operatorname{Ric}(G) = -g$,
  so the correct definition is $T = \operatorname{Rm} - G$ (not $+G$).
- Conformal Hessian coefficient: $-(\nabla^2 a \owedge g)$, not $-\frac{1}{2}$.
- Ricci-part Hessian signs: corrected first two terms in (4.2).
- Removed spurious "quadratic in $\nabla a$" sentence from §3.3.

Structural script: superseded by Step 64 repair, now 21/21 passed
(`workspace/data/step63_curvature_variation_verify.json`).

## Impact on the IL bridge

The curvature endpoint's tensor premise is now at proof level as an inequality, after the Step 64 convention repair. The $H_2$
inequality (8.2) is the input consumed by the curvature Moser endpoint
$\|aF_T(t)\|_\infty \le C\Gamma/t$. The full analytic bridge now stands at:

| Module | Status | Source |
|--------|--------|--------|
| 1. $(\Gamma,V)$ bootstrap | **Proved** | Step 55 |
| 2. Curvature Moser endpoint | **Proved** (tensor premise closed) | Step 63 + Step 61 verifier 2 |
| 3. Defect Moser endpoint | **Proved** | Step 62 |
| 4. Base layer | **Proved** | Step 60 |
| 5. All-order continuation | **Proved** | Steps 58–60 |
| 6. Terminal compactness | **Proved** | Step 56 §4 |
| 7. Derdziński forbidden germ | **Proved** | Source-verified |
| 8. Per-datum existence | **Conditional** | A03 Step 56 |

**Sole conditional input: per-datum existence.** Per the Strategist's guidance,
standard quasilinear parabolic theories (Amann, Lunardi, maximal $L^p$
regularity) assume uniformly elliptic principal part; the transported DeTurck
system has $\beta^2 \ge 0$ degenerate on the collar, so citation is likely
impossible. The honest resolution is either a self-contained existence argument
from A03's tame hierarchy or a cleanly isolated conditional theorem.

## Peer coordination

A02 Step 65 (#463): metric-export attempt on EH gluing produced calibration
(naive gluing has O(1) defect; Biquard correction essential; Lichnerowicz ODE
system derived). This is independent of the IL chain.

## Next priority

The per-datum existence hypothesis is now the single blocking input. The
next step should assess whether A03's tame construction can be written as a
self-contained proof or whether the restricted IL theorem should be stated as
a conditional result with per-datum existence as the named hypothesis.
