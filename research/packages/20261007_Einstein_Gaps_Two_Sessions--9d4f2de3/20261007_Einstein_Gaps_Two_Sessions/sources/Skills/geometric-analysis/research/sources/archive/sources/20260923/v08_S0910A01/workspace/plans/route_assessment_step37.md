# Step 38 superseding correction

Step 37's route assessment is superseded.  The shifted continuation theorem and first-exit platform were not proved: the cutoff-degenerate derivative recovery in Lemma 1.2a fails, and the TTCS result for Step 37 explicitly left the higher continuation argument unproved.  The correct next work is the weighted shifted equation and Wang-style unweighted-curvature module developed in `workspace/notes/step38_continuation_repair_and_support_normalization.md`, together with the corrected support-selection normalization.

---

# Route assessment after Step 37

**Step 37 continuation/first-exit claims are superseded by Step 38.** The material below is historical and contains withdrawn conclusions.
## Main construction

Step 37 built the shifted continuation theorem (Theorem 1.1) and first-exit
closure (Section 3), closing the degenerate-flow platform by adapting Wang's
staggered induction to the normalized fixed-cutoff equation.

### Core mechanism

The continuation theorem separates cleanly from the sequence-uniform smoothing
estimates:

| Layer | Work | Uniformity |
|:---:|:---|:---|
| A. Existence | transported DeTurck (A03 Step 37) | per-datum |
| B. Continuation | Theorem 1.1 (this step) | per-datum |
| C. Terminal | K₂, Y, J₆, Q, Moser endpoints | sequence-uniform |

The critical insight is that the degenerate diffusion \(\int a|\nabla\operatorname{Rm}|^2|\operatorname{Rm}|^{p-2}\) is exactly what absorbs both
the Hessian-cutoff and gradient-cutoff terms, because the signed IBP (0.4) and
Young inequality both produce the matching factor \(a=\chi^2\).  The reaction
\(a|\operatorname{Rm}|^{p+1}\le(K+C)|\operatorname{Rm}|^p\) uses only
\(\sup|U|\), not unweighted \(\sup|\operatorname{Rm}|\).

### TTCS corrections incorporated

1. **Metric equivalence**: logarithmic estimate
   \(|d/dt\log g(v,v)|\le CK\), not \(|g(t)-g(\tau)|\le 2K\Delta t\).
2. **Hessian-a splitting**: \(E=\operatorname{Ric}+g\) gives two IBP terms:
   \(B_{\mathrm{Ric}}\) (order \(p\)) and \(B_g\) (order \(p-1\)); the latter
   uses Young at \(\operatorname{Rm}=0\).
3. **Unweighted derivative recovery** (Lemma 1.2a): the split
   \(\{\chi\ge\delta\}\cup\{\chi<\delta\}\) gives per-datum
   \(\|\nabla^k\operatorname{Rm}\|_p\) from \(\|\nabla^kU\|_p\) by Leibniz
   inversion on the interior and frozen-exterior control on the boundary.
4. **First-exit \(\sup|U|\)**: bounded directly by
   \(\|aF\|_\infty+C\le C\gamma/\tau+C\), not \(\sup|a|\cdot\sup|T|\).

### TTCS residual gap: high-order Hölder exponents

TTCS noted that the explicit Hölder exponent arrangement for \(m\ge2\) top-jet
terms (coupling \(\nabla^{m+1}\chi\) to differentiated lower curvature factors)
is stated but not displayed.  The note claims these are paid by the signed IBP
(for single-Hessian type) and Hölder with the induction hypothesis (for
top-jet/lower-curvature couplings), but does not give the explicit
\(L^{q_1}\times L^{q_2}\times\cdots\) decomposition for every product.

This is a legitimate expositional gap, not a structural error: Wang's original
Lemmas 4.4–4.6 also state the grouping schematically and prove each level by
the same mechanism.  Nevertheless, a future revision should display the explicit
\(p'\), \(p''\), \(p'''\) for the \(m=1\) and \(m=2\) base cases.

## Conditional chain status after Step 37

| Module | Status | Reference |
|:---|:---:|:---|
| Curvature power inequality | proved at index level | Step 35 |
| Defect power inequality | proved (A03 Step 39, Thm 7.1) | A03 Step 39 |
| K₂ persistence + q=3 propagation | conditional (Step 34) | Step 34 |
| J₆ persistence | conditional (A03 Step 35) | A03 Step 35 |
| Global Q persistence | conditional (Step 36) | Step 36 |
| Weighted Moser endpoints | conditional (A03 Step 38) | A03 Step 38 |
| DeTurck short-time existence | formulated (A03 Step 37) | A03 Step 37 |
| **Shifted continuation** | **withdrawn as proved; repair active** | **Step 38 + A03 Step 40** |
| **First-exit closure** | **conditional only; depends on unresolved continuation** | **Step 38** |
| Plateau/support construction | open | — |
| Exponential pullback selection | conditional (Step 28) | Step 28 |
| Derdziński forbidden germ | conditional (Step 8) | Step 8 |

The first-exit closure paragraph from Step 37 is withdrawn.  It remains only a conditional assembly: without the repaired continuation theorem and short-time platform, it does not prove existence on \([0,\theta r^2]\).

## Remaining work for the restricted negative route

1. **Macro-disjoint support construction**: maximal-function good centers,
   volume-proportional assignment, coloring, \(a=1\) plateau containment.
2. **Plateau volume bound**: \(\operatorname{Vol}(P_i)\ge\alpha A_i\).
3. **Positive-branch counterpart** (A02, separate mechanism).
4. **Arbitrary 4-manifold topology**: current route uses Ishida–LeBrun inputs.
5. **Dimensions \(n\ge5\)**: no analogue of SW/W⁺/Derdziński.
6. **Lean formalization**: premature.

## Peer context

A03 Step 39 (#346) proved the general-p homogeneous defect power inequality and
identified a key structural finding: two-factor absorption fails on the Moser
ladder (requires \(\gamma\sim1/p\to0\)), while three-factor Hölder succeeds
with polynomial \(p\)-growth.  This completes the defect Moser ladder.

A02 Step 38 (#345) confirmed exact period-transport algebra for toric
alternating-rod families and identified compact-polygon monodromy for \(m=6,8\)
as the open positive-branch question.

## Files produced

- `workspace/notes/step37_continuation_theorem_and_first_exit.md` (main note)
- `workspace/scripts/step37_continuation_verify.py` (42/42 pass)
- `trace/ttcs/results/step37_ttcs01_verifier1_integration.md` (TTCS)
- This file: `workspace/plans/route_assessment_step37.md`
