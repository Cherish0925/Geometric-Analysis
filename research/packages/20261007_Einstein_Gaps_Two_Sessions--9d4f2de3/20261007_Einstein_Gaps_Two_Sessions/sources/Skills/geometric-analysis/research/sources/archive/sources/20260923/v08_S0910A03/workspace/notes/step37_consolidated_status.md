# Step 37 consolidated status

## Main advances this step

### 1. Transported-coefficient DeTurck short-time existence (§37a)

Adapted Yang's Theorem 8.2 to the normalized fixed-cutoff flow
$\partial_tg=-2\chi^2(\operatorname{Ric}+g)$. Uses transported hatted
coefficient $\hat a=(\chi\circ\varphi_t^{-1})^2$ with full Lie-derivative
cancellation; the normalization $-2\hat a\hat g$ is a bounded zeroth-order
perturbation of the linearized matrices that does not alter the principal symbol
$2\chi^2\Delta$ or the tame estimate mechanism. This replaces the incorrect
Step 35 existence note.

**Status:** structurally complete; cites Yang's published tame estimates with the
elementary perturbation. Per-datum $T>0$ and constants depending on $(g_0,\chi)$.

### 2. Global unweighted $Q(t)$ persistence (§37b)

$Q(t)=\int_M|E|^2\,d\mu_t$ is proved independently of $J_6$ and $\|aE\|_\infty$.
Uses the homogeneous defect equation (no curvature-only source) and
support-by-support two-factor absorption with the same $\gamma$ product.
Result: $Q(t)\le e^{C\theta}Q(0)$ on the first-exit interval.

**Status:** self-contained conditional lemma under the standard first-exit
hypotheses. Feeds the terminal calibration ($7/24$ inequality).

### 3. Base-pair $(\nabla U,\nabla^2\chi)$ continuation (§37c)

Proved that $\sup|U|<\infty$ on $[0,T)$ implies
$\sup_{t<T}(\|\nabla U\|_p+\|\nabla^2\chi\|_p)<\infty$ for all finite $p$.
TTCS found and we fixed three errors: (a) $I_{1c}/I_3$ have total power $p+1$,
needing a second IBP; (b) $\chi^2/a$ ratio replaced by no-division Young;
(c) Sobolev $L^\infty$ upgrade needs $W^{1,p}$ from higher induction.
After corrections: $Y_1=\|W\|_p^p+\|\Theta\|_p^p$ satisfies Grönwall with known
inhomogeneity $\|T\|_p^p$ from Step 27 §5. No hidden $\|T\|_\infty$ or
$\|a\nabla\operatorname{Rm}\|_\infty$.

**Status:** correct $L^p$ base-pair estimate; starts the Step 27 induction.
Combined with the higher induction (Moves A--C) and terminal restart, gives the
full extension theorem. Constants are per-datum.

## Current dependency graph for the 4D negative Ishida–LeBrun route

```
Existence ──────────────────────────────────────────────────────┐
  (transported-DeTurck, Yang §8 + zeroth-order normalization)   │
                                                                v
First-exit bootstrap on [0, theta*r^2]  <───────────────────── smooth solution
  │
  ├─ K_2 persistence (q=2 curvature seed)           [Step 23, A01 Step 34]
  │    └─ Y=K_3 (q=3 curvature seed)                [Step 23, A01 Step 34]
  │         └─ curvature Moser: ||aF(t)||_inf        [Steps 20-26]
  │
  ├─ J_6 persistence (two-factor, no Y needed)       [Step 35] ✓
  │    └─ defect Moser: ||aE(t)||_inf                [Steps 20-26]
  │         └─ integrable metric drift               [Step 34]
  │              └─ moving Sobolev/support comparison
  │
  ├─ Q persistence (global unweighted)                [Step 37] ✓
  │    └─ terminal calibration (7/24 inequality)
  │
  └─ all three ──> first-exit self-improvement at T*
                                                                │
Continuation/extension                                          │
  (shifted-curvature Wang induction)                            │
  ├─ base pair (∇U, ∇²χ): L^p bound               [Step 37] ✓ │
  ├─ higher induction (Moves A-B-C)                 [Step 27]   │
  └─ smooth terminal metric + restart               [Step 27, 37a]
                                                                │
Terminal geometric passage                                      v
  ├─ plateau curvature control + Shi                 [from Moser endpoint]
  ├─ exponential-pullback averaging + Rauch          [Step 16, 29]
  ├─ monopole/calibration + eigenline density        [Steps 4, 29, 30]
  └─ projector contradiction |∇W+|^2 = 1/16 vs 0   [Step 6] ✓
```

## What is NOT yet proved

1. **K_2 and Y persistence as self-contained theorems**: The curvature energy
   inequalities (A01 Steps 33-35) have correct tensor structure but need final
   assembly into proved lemmas with all hypotheses explicit.

2. **Curvature and defect Moser iteration**: The weighted recurrence
   $p\mapsto 3p/2$ and time-slab estimates exist in schematic form but have not
   been assembled into a proved pointwise endpoint.

3. **Integrable metric drift**: Conditional on the Moser endpoint
   $\|aE(t)\|_\infty\lesssim\delta(r^2/t)^{1/3}$, one gets
   $\int_0^T\|aE\|_\infty\le C\delta\cdot T^{2/3}r^{2/3}$, which is integrable.
   This has not been written as a self-contained lemma.

4. **Higher induction (Moves A-B-C)**: Step 27 describes the structural induction
   clearly but does not write term-level estimates for each move. This is mostly
   a packaging task once the base pair is available.

5. **Terminal geometric passage consolidation**: The exponential-pullback
   selection, monopole reconstruction on the terminal metric, eigenline density
   control, and chart-buffer verification are scattered across Steps 16, 29, 30.
   They need assembly into a single proof.

6. **Positive branch, arbitrary 4D topology, $n\ge5$, Lean formalization**:
   entirely untouched by this step.

## Verification records

- `workspace/notes/step37_transported_deturck_existence.md` (10.9k chars)
- `workspace/notes/step37_global_Q_persistence.md` (7.2k chars)
- `workspace/notes/step37_base_pair_continuation.md` (~10.5k chars, TTCS-corrected)
- `workspace/scripts/verify_step37_interface_algebra.py` (25 checks, all pass)
- `trace/ttcs/results/step37_ttcs01_verifier1_integration.md`
- Peer message: #343
