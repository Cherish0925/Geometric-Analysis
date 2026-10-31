# Route assessment after Step 13

## What Step 13 established

1. **Normalization-invariant rank-one reduction verified.**  The cover metric
   g = g_B + v²(dz+B)² with v(p) = 1 has all local coefficients independent
   of ℓ(p).  The reduced Einstein equations for (g_B, v, F_B) are a
   period-independent system.  Script `step13_rank1_reduction.py` produces the
   full symbolic curvature dictionary and passes all structural checks.

2. **A03's static formula confirmed.**  Spec(W+) = {1/3 - η_i} where η_i
   are eigenvalues of Hess(ℓ)/ℓ, verified against the reduction for the
   diagonal case and two specific profiles (calibrated and isotropic).

3. **Twist correction computed.**  W+ receives nonzero corrections from the
   scaled twist C_ab, the fiber gradient u_a, and their derivatives.  The
   correction involves both algebraic (C²) and differential (∇C) terms.

4. **H²×H² counterexample accepted.**  The product of two hyperbolic planes
   has static Spec(W+) = (-2/3, 1/3, 1/3), disproving the general static
   rigidity claim.  Only cohomogeneity-one static rigidity survives.

5. **Bootstrap gap identified.**  The accessibility bootstrap requires
   ordinary (not weighted) base Ricci control to obtain the 3D harmonic
   radius.  The weighted RCD(-1,4) structure does not automatically supply
   this.

6. **Conditional algebraic implication only.**  If Hess(ℓ)/ℓ ≥ 0 on a region, then Ric_B ≥ -I after adding the nonnegative twist term.  This does not supply an absolute volume anchor or a uniform cover chart.  Staticity C=0 gives tr H=1, not H ≥ 0; the earlier static rank-one closure statement is withdrawn.

7. **Step 12 curvature-operator sign correction.**  The exponential-twist
   W+ computation had R_{abdc} instead of R_{abcd} (negating the operator).
   Documented in the note.

## Current research position

The four-dimensional negative-branch obstruction architecture has three
layers:

### Layer 1: Noncollapsed (original Step 8)
Fixed-scale noncollapsed good points have vanishing volume proportion
(Derdziński forbidden germ + harmonic chart passage).  **VALID**.

### Layer 2: Rank-one collapsing, static fiber (new in Step 13)
If the circle fiber survives at fixed buffer scale AND the region is static
(no twist), the normalization removes ℓ(p), base Ricci is controlled
(H ≥ 0), the cover is noncollapsed, and the forbidden germ applies.
**VALID but restricted to the static case.**

### Layer 3: Rank-one collapsing, twisted fiber (open)
The chiral factorization (A03) gives the correct reduced structure:
a± = u ∓ z/2, with W± = -[sym∇a± + a±⊗a±]₀.  The calibrated condition
constrains a₊ but allows large cancellations between u and z.  Derivative
twisting can maintain |W+|² ≈ 1/24 while the quotient geometry degenerates.
The accessibility bootstrap has a gap at the base regularity step.
**OPEN: requires either weighted compactness/reconstruction or a
derivative-twist countermodel.**

### Layer 4: Rank-two and non-circle collapse (open)
Degeneration to fixed-point (NUT) neighborhoods, non-abelian collapse,
curvature concentration, and singular fibers remain open.

## What remains open in the negative branch

The active interface is broader than Layers 2 and 3: can one recover controlled geometry on a positive-volume portion of the calibrated bulk, either by localized smoothing under bounded local curvature mean or by coercive estimates in the reduced system, without assuming an exact circle action or semipositivity of H?

Three approaches remain live:

1. **Weighted Bochner identity for a±.**  Derive a coercive identity using
   the ℓ-weighted Laplacian, bounding |∇a±|² + |a₊∧a₋|² by the chiral
   Weyl energies plus boundary terms.  The obstruction is the trace mode.

2. **Localized Li smoothing at a fixed small radius.**  Ye Li's dimension-four input is r^4·(average of |Rm|²), so a bounded local curvature mean becomes small after choosing a sufficiently small but fixed physical radius.  The real analytic questions are localizing the all-centers theorem to a buffered good region and transferring or preserving the near-Einstein/calibrated data, not subtracting the calibrated block as the first move.

3. **Derivative-twist countermodel.**  Search for a near-Einstein metric
   with calibrated W+, bounded curvature means, but vanishing reconstruction
   radius through derivative twisting.  This would decisively redirect the
   program.

## Consequences for the full Yau 26 proposition

- The proposition remains unresolved in all dimensions n ≥ 4.  The Step 14 note `workspace/notes/step14_smoothing_vs_reduction_route.md` is the current route comparison for smoothing versus reduced-system reconstruction.
- The positive branch lacks a noncollapse theorem (A02's Proposition A
  is conditional on volume gap).
- The Lean formalization cannot begin because the mathematical theorem
  is not complete.
- Dimension 3 is classical.

## Key files

- `workspace/notes/step13_normalized_accessibility_theorem.md` — main note.
- `workspace/scripts/step13_rank1_reduction.py` — verified reduction script.
- `workspace/scripts/step13_chiral_and_base_ricci.py` — supplementary checks.
- A03 `workspace/notes/step12_reduced_equations_accessibility.md` — chiral
  factorization and corrections.
- A02 `workspace/notes/step13_preceptor_toric_spectral_review.md` — toric
  spectral anchors.
