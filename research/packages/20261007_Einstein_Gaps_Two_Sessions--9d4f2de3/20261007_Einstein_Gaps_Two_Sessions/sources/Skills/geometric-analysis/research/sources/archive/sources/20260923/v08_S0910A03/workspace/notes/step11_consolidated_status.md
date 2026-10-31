# Step 11 consolidated status

> **Step 12 repair.** The static formula and spherical cohomogeneity-one calculation remain valid. The general static-rigidity wording and the fiber-survival/high-twist dichotomy below are superseded: `H^2 x H^2` is a static constant-spectrum counterexample to the former, while small scaled twist does not control derivative twisting or quotient geometry. Toric orthogonal transitivity also does not make a chosen Hopf circle static. See `step12_reduced_equations_accessibility.md`.

## Corrections applied this step

### Static circle reduction formula
The initial formula W+ = 2J(h - I/3) was WRONG by a factor/sign.

CORRECTED (verified by TTCS and computation):
- R_hat_+ on Lambda^2_+ has Spec = -Spec(h), where h = Hess(ell)/ell
- W+ = R_hat_+ + (1/3)I, so **Spec(W+) = {1/3 - eta_i}**
- Calibrated: h = (1/2, 1/4, 1/4), NOT (3/8, 3/8, 1/4)
- Script: `workspace/scripts/corrected_circle_reduction.py`

### Twist sign
tr(h) = 1 + ell^2|F|^2/4 > 1 under nonzero twist (corrected from < 1).

### Near-NUT behavior
Both h and twist corrections diverge near a smooth NUT. They cancel in the 
total smooth curvature. The static formula does NOT dominate near the NUT.
This invalidates the claim that "NUTs force isotropic W+."

## New results

### Static cohomogeneity-one incompatibility (verified)
For a static Einstein circle metric with constant calibrated spectrum:
- Einstein E1 gives a'' = a/4
- Einstein E2 + differentiation gives a'' = a/2
- CONTRADICTION with gap a/4 (relative error 1/2)

Within the displayed spherical cohomogeneity-one ansatz, the only compatible constant-eigenvalue solution is u = v = 1/3 (W+ = 0). This is not a general static classification.

### Superseded TTCS proposal
Buffered fiber survival plus a controlled cover chart still leads to the forbidden Einstein germ. It has **not** been shown that failure of accessibility forces `ell^2|F|^2 >= c`: `ell nabla F`, `(nabla ell)F`, and quotient degeneration remain possible, so there is no established case (D).

### Pontryagin non-discrimination (Strategist correction)
The Ξ lower bound from the Pontryagin density is automatic for ALL Ric=-g 
(by self-duality of the connection curvature on Lambda^2_+). The isotropic 
scalar part provides 88.9% of the calibrated density. The distinguishing 
feature is the W+ ANISOTROPY (eigenvalue structure), not the density.

## Integration with peers

- A01 (Step 12): Confirms Taub-NUT-AdS multiscale computation. Developing 
  rank-one Cartan structure equations for the Lambda^2_+ connection algebra.
  One-jet computations support diffuse mixed-curvature picture.

- A02 (Step 12): Toric determinant calculation with 
  tr_h Ric^V = -Delta_B w/w + |F|^2_h/2. Its toric orthogonal-transitivity result concerns integrability of the 2-plane perpendicular to full torus orbits; it does not remove the connection curvature of an individual circle reduction.

## Research position

The four-dimensional negative-branch collapse analysis has three remaining 
mechanisms:

1. **Case (S) with noncollapse + maximal rank**: EXCLUDED by the forbidden 
   calibrated Einstein germ (Steps 5-6), assuming buffer-scale covering 
   charts exist.

2. **Case (D) with high twist**: NOT YET EXCLUDED. Requires diffuse 
   ell^2|F|^2 >= c > 0, which means persistent scaled holonomy/O'Neill 
   curvature. Global constraints (topology, energy budget) may exclude 
   this but the argument is not constructed.

3. **NUT-type with contractible fibers**: NOT YET EXCLUDED in general.
   Taub-NUT-AdS shows standard NUTs have diverging curvature near the 
   core and calibrated deficit 16 on the unwrapped annulus. But the 
   corrected near-NUT analysis shows that general smooth NUTs could 
   potentially maintain any W+ structure through cancellation of 
   divergent h and twist terms.

The positive branch, higher dimensions, and Lean formalization remain open.

## Key files
- `workspace/notes/step11_circle_reduction_anisotropy_and_fiber_survival.tex`
- `workspace/scripts/corrected_circle_reduction.py`
- `trace/ttcs/results/step11_ttcs01_generator1_integration.md`
- `trace/ttcs/results/step11_ttcs01_verifier1_integration.md`
