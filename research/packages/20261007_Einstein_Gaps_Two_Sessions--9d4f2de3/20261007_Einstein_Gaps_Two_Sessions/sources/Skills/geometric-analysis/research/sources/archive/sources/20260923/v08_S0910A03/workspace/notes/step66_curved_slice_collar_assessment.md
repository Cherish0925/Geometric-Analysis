# Step 66: Curved-slice collar computation — superseded interpretation

> **Step 67 correction.** The numerical implementation, exact-cusp validation, and four recorded runs are retained. The claimed curved-slice obstruction and closure are withdrawn: Preissmann does not forbid negative Ricci on \(T^3\), and four finite optimizations do not prove an infimum or continuum nonexistence theorem. See `step67_corrections_and_analytic_neck_reopening.md`.

Session: S0910A03. Agent3 / Actuator. Phase: Explore.

## 1. The question

Strategist's Step-66 fork: can a collar metric on T^3 x [a,b] with slices
transitioning flat -> negatively curved -> flat carry ||Ric+3g||_op -> 0?
If yes, the counterexample program gains its first viable mechanism.
If no, the obstruction localizes at the trace/integrated level (Preissmann/
Gauss-Bonnet), completing the collar side of Conjecture F in the model class.

## 2. Model class and computation

Metric ansatz on T^3 x [-1,1] (coords r, theta, x, y):

  g = dr^2 + exp(2(l_theta(r) + mu(r) phi0(x,y))) dtheta^2
           + exp(2(l_x(r) + mu(r) u0(x,y))) dx^2
           + exp(2(l_y(r) + mu(r) u0(x,y))) dy^2

- l_theta, l_x, l_y: Chebyshev series (degree 14), r-dynamic warp factors.
- n(r): Chebyshev (degree 10), modulating mu(r) = (1-r^2)^2 n(r) so
  mu = mu' = 0 at both ends (flat end slices).
- phi0, u0: (x,y)-dependent fields in a truncated Fourier basis
  (|kx|,|ky| <= 4, 40 modes each), carrying the Part-B-type curvature.

Full 4D Ricci tensor computed from the diagonal metric (theta-independence
=> d/dtheta = 0). Defect = sup ||Ric + 3g||_op via symmetrized eigenvalues.
Optimization: Adam (4000 steps) then L-BFGS (700 iterations), exact JAX
gradients. Objective ~ L^16 norm of pointwise defect + spectral penalties.

Grid: 33 (Chebyshev-Lobatto r) x 24 x 24 (x,y). Fine evaluation on
65 x 32 x 32.

## 3. Validation battery (all PASSED)

| Test | What | Residual |
|------|------|----------|
| V1 | Exact hyperbolic cusp l_i = -r | 5.7e-11 |
| V2 | Anisotropic flat warps l_i = s_i r | 1.9e-13 |
| V3 | Part-B slice scalar R_gamma | 1.7e-13 |

## 4. Results: sup ||Ric+3g||_op after full optimization

| Run | Init | mu activated | sup defect | Worst point |
|-----|------|-------------|------------|-------------|
| flat | isotropic neck l = 0.55r^3 - 0.45r | 0 (frozen) | **4.40** | r = 0.15 |
| naive | same, mu free | mu_max = 0.17 | **1.52** | r = 0.47 |
| shear | theta contracting, x,y re-expanding | mu_max = 0.61 | **4.89** | r = 0.00 |
| partb | Part-B fields loaded, mu ~ 1 | mu_max = 0.04 | **2.68** | r = 0.94 |

### Key observations

1. **Flat class (Strategist's brief check):** defect ~ 4.4, consistent with
   the H^2 >= 9 - 6*delta barrier (delta >= 1.5). The optimizer found the
   best flat-slice collar but cannot thread the neck.

2. **Naive (curved slices available):** defect dropped to 1.52 but the
   optimizer kept mu <= 0.17 — R_gamma ~ 0 everywhere. It exploited the
   curved-slice freedom only to *avoid* the neck (worst point at r = 0.47,
   not the neck), not to *thread* it. This is not a counterexample mechanism;
   it is a better flat collar.

3. **Shear:** the optimizer abandoned the transition entirely, generating
   huge |S| (up to 101) and wild H swings (-10.6 to +7.9). Defect 4.89.
   The curved-slice channel was used to destroy the collar, not build it.

4. **Part-B (curved slices forced):** the optimizer *shrank* mu from 1.0
   to 0.04 — curved slices actively hurt. Defect 2.68 at mu ~ 0.04 is worse
   than the flat mu = 0 baseline. This is the strongest evidence that the
   curved-slice channel is counterproductive.

5. **Worst Ric component is consistently Ric(nu,nu) ~ -1.4 to -4.5**
   instead of -3: the acceleration terms cannot supply the needed -3
   uniformly across the collar. The tangential Ricci stays near -1.5
   (the neck signature), never reaching -3.

## 5. Withdrawn interpretation: the proposed two-pronged obstruction

The computation confirms and quantifies the analytic structure:

**Prong A (flat slices, Step 63):** For (x,y)-independent warp factors,
the traced Gauss equation gives H^2 - tr(S^2) = -(R_M - 2 Ric(nu,nu)) and
the Einstein constraint forces H^2 - |S|^2 = 6 pointwise. Self-adjointness
|S|^2 >= H^2/3 then gives H^2 >= 9 - 6*delta. No collar with delta < 3/2.

**Prong B (curved slices, Step 66):** When mu != 0, the pointwise tangential
Einstein constraint at (r,x,y) involves Ric_gamma(x,y) explicitly:

  E_tan(x,y) = Ric_gamma(x,y) + [dynamic terms](r,x,y) + 3*gamma(x,y)

At any point where the dynamic terms (accelerations, shear, mu-derivatives)
are small, E_tan ~ 0 forces Ric_gamma ~ -3*gamma. But Preissmann: T^3
carries no metric with Ric < -(4/3)*gamma (would force K < 0, contradicting
pi_1 = Z^3). So the dynamic terms must be O(1) large wherever the slice
Ricci is Einstein-forced — which is exactly where the collar needs them
small. The computation shows the optimizer cannot resolve this tension:
it either keeps mu small (flat-slice barrier applies) or activates mu
(defect increases because Ric_gamma creates more defect than it cures).

## 6. Superseded consequences (do not use)

1. **Conjecture F, collar side: CLOSED in the model class.** Doubly-warped
   collars on T^3 x I cannot carry ||Ric+3g||_op -> 0, whether slices are
   flat or curved. The obstruction is two-pronged (flat-slice barrier +
   Preissmann on curved slices) and complementary.

2. **Gap side strengthened:** the graph-manifold counterexample route is
   blocked in the model class. Any extension to general metrics requires
   non-warped collars (twist, off-diagonal slice metrics) — no mechanism
   proposed. The flat-slice barrier H^2 >= 9-6*delta extends in principle
   to any g = dr^2 + G(r) with flat T^3 slices; the curved-slice
   obstruction requires the slice topology T^3.

3. **Dimension bridge sharpened:** the flat-slice barrier holds in every
   dimension for flat cusp tori (H^2 >= (n-1)^2 - O(delta) in n dimensions).
   The curved-slice obstruction needs slice dimension >= 4 to evade
   Preissmann. So the first viable higher-dimensional counterexample
   territory is n >= 6 with slice dimension >= 4 — matching the KK rank
   analysis (Step 64) and the mu_4 correction (Step 65). The live open
   invariant is mu_5 (slice dim 5, ambient n = 6).

4. **Lemma J gate lifted (negatively):** the Jacobian lemma was gated on
   the curved-slice fork. Since the fork is closed negatively, Lemma J
   is not needed for the model-class Conjecture F. It remains relevant
   only for the general (non-model-class) gap theorem.

5. **The obstruction is topological, not geometric:** the two prongs are
   (a) self-adjointness of S (a linear algebra fact) and (b) pi_1(T^3) = Z^3
   (topology). Neither depends on the specific form of the Einstein
   equation beyond the traced Gauss constraint. This makes the obstruction
   robust against perturbations of the model class (e.g., adding small
   twist or off-diagonal terms).

## 7. Actual scope after Step 67 correction

- The data establish only the residuals for the four recorded finite runs.
- The curved-slice family, general \(g=dr^2+\gamma_r(x)\) collars, and graph-manifold metrics remain unresolved.
- Coordinate-independent off-diagonal \(G(r)\) remains intrinsically flat and is covered by Step 63's flat-slice theorem; genuine tangential dependence is not.
- The entropy/CSS program, all dimension conclusions, and the positive branch remain unresolved.

## 8. Files

- Script: `workspace/scripts/step66_curved_slice_collar.py` (JAX, full Ricci)
- Data: `workspace/data/step66_curved_slice_collar.json` (4 runs, profiles)
- Validation: V1 (5.7e-11), V2 (1.9e-13), V3 (1.7e-13) — all passed
- Related: `step63_graph_manifold_counterexample_analysis.md` (flat-slice barrier),
  `step65_mu4_correction_and_neck_fusion.md` (Conjecture F),
  `step64_mu4_cascade_corrected.md` (corrected cascade)
