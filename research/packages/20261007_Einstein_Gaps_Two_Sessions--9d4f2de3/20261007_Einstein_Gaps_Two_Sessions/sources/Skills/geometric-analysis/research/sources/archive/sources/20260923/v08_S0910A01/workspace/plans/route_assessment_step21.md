# Step 22 superseding note

The Step 21 route assessment is superseded by `workspace/plans/route_assessment_step22.md` and `workspace/notes/step22_current_energy_formulation.md`.  The Step 21 text treats the time-uniform `H_3` input as if it follows from a Whitney-volume-normal `L^2` estimate; the available component budget gives only the scale-invariant mean and critical Sobolev product.  Current energy persistence must be proved as a finite-neighbor first-exit estimate.  Also remove the transition inference that small metric displacement keeps curvature close to its initial value.

# Route assessment after Step 21

## What changed

Step 21 developed the conditional finite-exponent smoothing lemma: the
two-step (q=2, q=3) energy argument produces a time-controlled weighted
cubic potential H_3(t) ≤ Cγ H_2(0)/t, after which A03's q→3q/2 Moser
iteration gives the pointwise weighted bounds |aRm| ≤ Cγ/t and
|aE| ≤ Cδ(r²/t)^{1/3}.

TTCS found a critical scaling correction: curvature has dimension length⁻²,
so the metric-rescaling approach to local boundedness gives ℓ²F ≤ C (i.e.,
|aRm| ≤ Cr⁻²), not F ≤ C with constant independent of χ₀.  The correct
mechanism avoiding this overestimate is A03's weighted-moment Moser iteration,
which works entirely in the original metric.

A03 (messages #294–295) further clarified that quantitative pointwise
derivative control is NOT needed for the zero-order first-exit closure.
All Hessian-a terms integrate by parts; cutoff gradients transfer under
bilipschitz comparability.  The derivative/Bernstein estimate is no longer
load-bearing for the zero-order argument.

## Established

1. BG energy transfer: ℓ⁴ fint |Rm|² ≤ CK₀r⁴ (χ₀ cancels exactly).
2. Critical a₀-cancellation in the Sobolev absorption at q=2 and q=3.
3. Parabolic Sobolev exponent 2(n+2)/n = 3 for n=4.
4. Time-cutoff mechanism: spacetime L³ controls the q=3 time-derivative source.
5. A03 q→3q/2 infinite product converges; endpoint gives |aF| ≤ Cγ/t.
6. No derivative estimate needed for zero-order first-exit.

## Corrected (from TTCS)

- Curvature rescaling: under g̃ = ℓ⁻²g, |Rm(g̃)| = ℓ²|Rm(g)|.
  F is NOT invariant under metric rescaling.
- Volume power in parabolic Sobolev: Vol^{3/2}, not Vol².
- Current-time γ(t) must be maintained by the first-exit system, not
  assumed from γ(0) alone.
- Bootstrap closure (Section 13) requires the first-exit structure
  explicitly, not just a verbal assertion.

## Current mathematical state

The analytic bridge now has a clean structure:

1. Fixed q=2,3 energy → cubic potential H₃ (Steps A–C, valid)
2. q→3q/2 Moser iteration → pointwise |aRm| ≤ Cγ/t (A03 Sections 10–11)
3. Triangular defect → Q/A → 0 (Step 20 Section 7)
4. Metric comparability from integrable |aE| (A03 Section 9)

The remaining derivation is the weak nested time-space estimate (A03 eq. 11.1)
uniformly with finite-neighbor outer terms.  Once this is proved, the first-exit
system closes without derivative estimates and without metric rescaling.

## What this does NOT settle

- Only the critical four-dimensional negative LeBrun/Ishida-LeBrun laboratory
- Positive branch, higher dimensions n≥5, and Lean formalization remain open
- The full interval statement of Yau Problem 26 is not resolved
