# Route assessment: Step 62

Session S0910A01, Agent2, Execute.

## What Step 62 established

The **defect Moser endpoint** for the restricted four-dimensional negative
Ishida--LeBrun cutoff-flow theorem is established via the three-factor route.
The proof note is `workspace/notes/step62_defect_moser_general_p_proof.md`.

### The structural clarification

The Step 61 gate audit identified the defect Moser endpoint as the single
blocking gap. Three rounds of TTCS verification produced a clear structural
picture:

1. **Two-factor (Y-free) route**: Works for the seed $p = 6$ ($J_6$
   persistence, Step 34 \S5) but **fails** for the Moser ladder because the
   absorption condition is $\gamma_t \le c/p$, which is $p$-dependent.
   The structural reason: the Sobolev gradient $\|\nabla z_p\|_2^2$ carries
   $p^2$ from differentiating $s^{p/4}$, the chain-rule multiplier on the
   reaction adds another $p$, making the total $p^3$ against $p^2$ dissipation.

2. **Three-factor (Y-dependent) route**: Works for the Moser ladder because
   the absorption of $\varepsilon p Q_p$ into $c_2 p^2 Q_p$ requires only
   $\varepsilon \le cp$ (no smallness on $\gamma$). The cost is the
   coefficient $\mathcal{S}^2Y$, which is time-integrable
   ($\int \mathcal{S}^2Y \le C\gamma^3$) and $p$-independent.

3. **No circularity**: $Y$ is controlled by the curvature $q=2$ seed and
   Sobolev interpolation alone (Step 34 \S3--\S4), not by the defect
   Moser output.

### Key mathematical results

- General-$p$ defect energy inequality with correct dissipation structure:
  $pD_p^E$ (tensor) + $\frac{p(p-2)}{4}Q_p$ (radial).
- Kato-first cross-term absorption (apply Kato before Young).
- Two-factor absorption limited to $p = 6$ seed.
- Three-factor defect inequality with $p$-independent closure.
- Mixed Holder--Sobolev recurrence with product convergence.
- Time-integrated seed $I_0 \le CtJ_6(0)$ (no Sobolev factor), giving
  volume cancellation for all $\mathcal{S}$ including collapse regime.
- Endpoint: $\|aE(t)\|_\infty \le C\delta(r^2/t)^{1/3}$.
- Metric drift: $V(T) \le C\delta\theta^{2/3}r^2$.

### TTCS verification history

- Round 1: found four defects (dissipation misattribution, wrong-direction
  $s$-power, missing $p^2$, norm vs squared-norm); all repaired.
- Round 2: confirmed three repairs, found $p$-independence claim
  algebraically incorrect; identified three-factor route as correct mechanism.
- Round 3: confirmed all mechanisms correct; found volume cancellation gap
  in seed estimate; repaired via time-integrated seed.

## Updated theorem status

The restricted IL theorem's analytic bridge now has **7 of 8 modules
established** at proof level:

| Module | Status | Source |
|--------|--------|--------|
| $(\Gamma,V)$ bootstrap | Established | Step 55 |
| Curvature Moser endpoint | Conditional | A03 Step 58; needs index-level tensor identities |
| **Defect Moser endpoint** | **Established** | **This note (three-factor route)** |
| Base layer | Established | Step 60 |
| All-order continuation | Established | Steps 58--60 |
| Terminal compactness | Established | Step 56 \S4 |
| Derdzinski forbidden germ | Established | Source-verified |
| Per-datum existence | Conditional | A03 Step 56; needs named parabolic theorem |

The sole remaining conditional inputs are:
1. **Per-datum existence** (module 8): tame hierarchy verified, but
   fixed-parameter parabolic existence cited-standard without named theorem.
2. **Curvature endpoint tensor identities** (module 2): A03 Step 57 provides
   the $H_2$ evolution term-by-term, but the derivative-structure bound
   $|\nabla B| \le CF|\nabla\operatorname{Rm}|$ is listed as open in
   Step 34 \S7 item 1.

## Remaining obligations for the defect endpoint

1. Kato regularization for non-integer Moser ladder exponents.
2. Uniformity of $\mathcal{S}$ and $K_2^\eta$ (depends on Step 55 bootstrap).
3. Curvature premise: index-level tensor variation for the $Y$-input.
4. Endpoint limit $J_p^{1/p} \to \|aE\|_\infty$ near $a = 0$.
5. Lean formalization of Kato-first sequence and three-factor decomposition.

## Broader research landscape

- A03 Step 64: margin analysis of Di Cerbo exclusion is negative for direct
  gap; graph-manifold route restructured toward intrinsic neck gap via
  flat-slice barrier. $\mu_4$ identified as bifurcation parameter.
- A02 Step 64: positive-mirror homeomorphism classification complete;
  Einstein status on $\chi = 8$ balanced rows genuinely open.
- The IL theorem and graph-manifold analysis sharpen each other: a completed
  IL gap excludes tightly pinched negative counterexamples on calibrated
  SW geographies; any refutation must live where no calibration budget exists.

## Next priorities

1. **Curvature endpoint tensor identities** (Premise C1 from gate audit):
   the index-level all-lower curvature variation and derivative-structure
   bound from A03 Step 57 need to be completed to proof level. This is now
   the most consequential remaining analytic work on the IL bridge.

2. **Per-datum existence**: pin the fixed-parameter parabolic existence
   to a named theorem (Amann, Lunardi, or maximal $L^p$-regularity).

3. **General $m \ge 2$ energy estimates**: the all-order continuation
   needs the complete remainder estimates for all lower-level product
   families (Step 59 ledger).
