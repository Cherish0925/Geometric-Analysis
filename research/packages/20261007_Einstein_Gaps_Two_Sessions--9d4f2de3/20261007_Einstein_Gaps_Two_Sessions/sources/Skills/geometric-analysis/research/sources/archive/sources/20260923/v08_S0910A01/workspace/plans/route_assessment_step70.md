# Route assessment: Step 70

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 1. What Step 70 produced

Two self-contained proof notes expanding the most load-bearing
interfaces in the restricted IL assembly:

### a. Selected-support lemma (`step70_selected_support_lemma.md`, 824 lines)

Expands assembly §4 into a complete proof module.  TTCS verification
found four genuine errors, all repaired:

1. **Curvature decomposition coefficient**: Corrected to
   $|\operatorname{Rm}|^2=|W|^2+\frac12|\mathring{\operatorname{Ric}}|^2+\frac{s^2}{24}$
   (operator-normalized), giving $\int|\operatorname{Rm}|^2=8\pi^2\chi+\int|\mathring{\operatorname{Ric}}|^2$.

2. **Euler characteristic bound**: Replaced false $8\pi^2\chi=I+J$
   with a correct derivation through Noether/BMY surface inequalities
   ($c_2\le Cc_1^2$) and bounded topology ($D_i=O(A_i)$).

3. **Volume lower bound mean**: Corrected from $2/9$ to $3/4$.
   (At calibrated values $s\to-4$, $|W^+|^2\to1/24$:
   $16/24+2/24=3/4$.)  Final constant $32\pi^2/9$ unchanged.

4. **Packing/coloring**: Replaced absolute volume lower bound
   $v_-(r/2)>0$ (false under collapse) with relative Bishop–Gromov
   comparison $D_0\le V_{-1}(29r)/V_{-1}(r/2)$.

5. **Cutoff smoothing**: Pre-reserved $\varepsilon$-buffers to maintain
   strict support nesting after mollification.

Structural script: 33/33 (`step70_support_lemma_verify.json`).

### b. Defect Moser real-exponent proof (`step70_defect_moser_real_exponent.md`)

Expands assembly §6.5 with:
- Real-exponent regularization $s_\varepsilon=|E|^2+\varepsilon$.
- Explicit time cutoffs and nested slab structure.
- Three-factor absorption with $p$-independent coefficient.
- Endpoint identification via $a=1$ on the plateau $B_{5r}$.
- Volume cancellation in all collapse regimes.
- Reconciliation of two exponent conventions: sup-time recurrence
  gives $\|aE\|_\infty\le C\delta(r^2/t)^{1/3}$ (sharp); time-integrated
  recurrence gives the weaker $t^{-1/6}$ from the extra seed factor.

## 2. Impact on the restricted IL assembly

The assembly's §4 and §6.5 now have self-contained proof modules
behind them.  Of the nine modules in the assembly:

| Module | Standalone note | Status |
|--------|----------------|--------|
| Terminal calibration §3 | step67 | Proved |
| Selected support §4 | **step70 (this step)** | **Proved** |
| Per-datum existence §5 | step65 | Proved |
| Bootstrap §6.1-6.2 | step55 | Proved |
| Curvature branch §6.3-6.4 | step63 | Proved |
| Defect Moser §6.5 | **step70 (this step)** | **Proved** |
| Global Q §7 | step45 | Proved |
| Continuation §8 | steps 58-60 | Proved |
| Terminal contradiction §9 | step45/28 | Proved |

## 3. Remaining IL work

The restricted IL theorem is now at proof level across all nine modules.
The remaining presentation work is:
- A complete convention-clean writeup (each module uses consistent notation).
- Formal peer review of each module's interface.
- Lean formalization (blocked by theorem stability, not yet started).

## 4. Distance from the full Yau-26 goal

The restricted IL theorem covers:
- Dimension 4 only.
- Negative normalization only.
- Ishida–LeBrun geography with $q\ge0$ only.
- Family-uniform gap, not dimension-only.

For the full Yau-26 proposition:
- **Positive branch**: No calibration budget or forbidden germ exists.
  Manuscript gives positive results for complex/symplectic types only.
- **Arbitrary 4-manifold topology**: The IL geography is specific.
- **$n\ge5$**: No replacement for SW/self-dual-Weyl mechanism.
- **Refutation route**: Needs both signs defeated on the same manifold
  (or different manifolds in the same dimension).
  Surface-bundle $\delta\to0$ with all-sign Einstein nonexistence would
  defeat the negative branch; positive branch must also be defeated.
- **Lean formalization**: Requires a stable mathematical theorem first.

## 5. Next valuable work

Within the IL line:
- Interface convention verification across all nine module notes.
- Formal writeup of the complete restricted theorem.

For the full Yau-26:
- A03's anisotropic compensation equations on surface bundles.
- A02's flux/kernel formalization and transfer to bubbling sequences.
- Positive-branch mechanism search.
- Higher-dimensional structure exploration.
