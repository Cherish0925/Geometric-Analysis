# Step 68 route map (supersedes step67_route_map.md)

Session: S0910A03. Phase: Explore.

## Organizing principle (from 20260912.tex, line 6436)

Two complementary difficulties:
1. Surface bundle E_D: has δ→0, lacks Einstein nonexistence
2. Extended graph manifold: has Einstein nonexistence, lacks δ→0

A complete n=4 negative-branch answer requires ONE manifold with both.
A complete Yau 26 disproof requires both signs to fail in one dimension.

## Negative branch routes

### Route A: Surface bundle E_D
- **Status**: δ = Θ(ε³) achieved (manuscript Ch. 6)
- **Blocking question**: Does E_D carry an Einstein metric?
- **Known exclusions**: no complex structure (any cover), not virtually
  Kähler, no sec≤0, fibered rigidity for adapted metrics only
- **Candidate mechanisms**: harmonic-map critical-set analysis, or
  energy-functional compactness failure. See step68_einstein_nonexistence_analysis.md.
- **Assessment**: hardest open question; no known tool is close

### Route B: Extended graph manifold
- **Status**: Di Cerbo Einstein nonexistence; Koiso local reversal confirmed.
  The earlier favorable-volume inference is withdrawn: the radius bound was
  for deleted hyperbolic balls, whereas flat cusp interfaces give a bridge
  length bound only.
- **Blocking question**: Can δ→0 be achieved globally?
- **Ingredients**: Koiso germ, anisotropic curvature transfer, cusp matching.
- **Assessment**: slow variation conflicts with thin scale because
  \(f^{-2}\operatorname{Ric}_{\gamma}\) grows as slices shrink. Chapter 6
  succeeds by retaining curved directions at Einstein scale while a separate
  circle degenerates. A graph construction must reproduce such compensation,
  not merely insert a long interpolation.

### Route C: Varying-entropy M_d = X_d # Q
- **Status**: Kotschick Einstein nonexistence; entropy lower bound δ ≥ t_Q/(4c_d)
- **Blocking question**: Can δ→0 on a single M_d?
- **Interface cost**: surgery at radius R gives δ ≥ csch²(R/√3), volume
  c_d δ^{3/2} ≥ 1 requires c_d → ∞ for δ→0.
- **Assessment**: same structural difficulty as graph manifolds but
  with explicit topology.

## Positive branch

- No closed 4-manifold is known with positive Ricci and no Einstein metric
- A02 pursuing mixed A1 obstruction on (S²×S²)/Z₂
- Positive branch is an existence problem, not obstruction

## IL restricted theorem

- A01: per-datum existence complete; terminal IL interface recovered (msg #486)
- Remaining: canonical-convention assembly of flow modules
- This gives a geography-dependent gap, not dimension-only constants

## Research priorities (for A03)

1. **Develop Route B's compensation equation**: compare the exact Chapter 6
   Ricci matrix with a thin torus layer and determine whether intrinsic
   curvature can be transferred into normal shear while all three cusp
   directions become small. Do not assume favorable volume scaling.

2. **Restrict Route A to monodromy-specific information**: exact Einstein
   products already admit harmonic submersions to a differently marked target
   that are not horizontally conformal, and target minimization imposes only
   fiber-averaged TT stationarity. Any advance must use the infinite Dehn-twist
   outer action or an additional variational identity.

3. **Support IL assembly**: verify key interfaces on request from A01.

## Files
- workspace/notes/step68_manuscript_absorption.md
- workspace/notes/step68_einstein_nonexistence_analysis.md
- workspace/notes/step67_corrections_and_analytic_neck_reopening.md (updated)
