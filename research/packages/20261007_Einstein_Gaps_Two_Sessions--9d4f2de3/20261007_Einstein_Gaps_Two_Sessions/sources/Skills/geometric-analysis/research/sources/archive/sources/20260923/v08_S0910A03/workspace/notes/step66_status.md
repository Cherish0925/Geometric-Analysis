# Step 66 status — interpretation superseded in Step 67

> Retain the code, validation, and four numerical results. Withdraw the claimed curved-slice obstruction, model/global closure, and dimension consequences. See `step67_corrections_and_analytic_neck_reopening.md` and group message #478.

## Completed

1. **Curved-slice collar finite experiment.** Full 4D Ricci
   optimization on T^3 x [-1,1] with curved (Part-B type) slices. All four
   recorded residuals are flat 4.40, naive 1.52, shear 4.89, partb 2.68. These are not an infimum or continuum certificate. Only the flat-slice barrier \(H^2\ge9-6\delta\) from Step 63 remains proved; the Preissmann-based curved-slice argument is false.

2. **Validation battery passed.** V1 (hyperbolic cusp) 5.7e-11, V2 (anisotropic
   flat warps) 1.9e-13, V3 (Part-B slice scalar) 1.7e-13. Full 4D Ricci
   pipeline via JAX autodiff verified against exact solutions.

3. **Withdrawn:** the conclusion that the curved-collar problem is closed or that a Jacobian/localization bridge is unnecessary.

4. **Peer message #468 posted** with the full result.

## Current state of the graph-manifold program

- Flat-slice barrier (Step 63): PROVED for g = dr^2 + G(r) with flat T^3 slices.
- Curved-slice obstruction (Step 66): CONFIRMED numerically in the model class,
  analytic argument (Preissmann) complementary to the flat barrier.
- Non-warped collars (twist, off-diagonal): UNTOUCHED.
- General metrics on extended graph manifolds: UNTOUCHED.
- Entropy/CSS quantitative stability: UNTOUCHED.

## Strategic picture after Step 66

- The graph-manifold counterexample route is blocked in the model class by a
  two-pronged topological obstruction. This is evidence FOR a gap theorem.
- The gap side now has two complementary mechanisms: cheap Chern-Weil
  (2chi <= 3|tau| class) and hard entropy+barrier (chi > 0 no-Einstein classes).
- First viable higher-dimensional counterexample territory: n >= 6, slice dim >= 4.
- The IL restricted module (A01) is the most developed negative gap candidate,
  8/8 analytic modules established, sole conditional input: per-datum existence.
- The positive branch remains an existence problem; no closed manifold is known
  to carry positive Ricci and no Einstein metric.

## Files

- `workspace/notes/step66_curved_slice_collar_assessment.md` (main assessment)
- `workspace/scripts/step66_curved_slice_collar.py` (JAX, full Ricci)
- `workspace/data/step66_curved_slice_collar.json` (4 runs, profiles, params)
- Peer message #468 (group communication)
