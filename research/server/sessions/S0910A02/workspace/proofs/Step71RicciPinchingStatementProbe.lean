import Mathlib

/-!
Step 71 cheap probe: can the current Mathlib environment state Yau--26's
Ricci pinching hypothesis directly?

This file intentionally starts with only the minimal structures one would need
for statement fidelity. It uses #check/#guard_msgs rather than proving geometry.
If names such as Ricci curvature are absent or too weakly developed, compilation
will show the scoping boundary.
-/

#check SmoothManifoldWithCorners
#check RiemannianMetric
#check Metric.closedBall
#check CompactSpace
#check ConnectedSpace

-- Differential-geometric curvature names expected in a mature Riemannian library.
-- These checks are allowed to fail in the first probe; their diagnostics are the result.
#check ricci
#check Ricci
#check riemannCurvature
#check RiemannCurvature
#check sectionalCurvature
#check scalarCurvature

