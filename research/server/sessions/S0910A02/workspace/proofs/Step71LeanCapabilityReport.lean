import Mathlib
import Lean

/-!
Step 71 Lean capability report for statement fidelity.
This file does not attempt to prove geometry. It inspects imported Mathlib
constant names to see whether the current environment exposes mature Ricci / Riemann
curvature objects sufficient to state Yau--26 literally.
-/

open Lean

#eval show CoreM Unit from do
  let env ← getEnv
  let names := env.constants.toList.map (fun kv => kv.fst.toString)
  let needles := [
    "Ricci", "ricci", "RiemannCurvature", "riemannCurvature",
    "sectionalCurvature", "scalarCurvature", "LeviCivita", "Christoffel",
    "Connection", "connection", "IsRiemannianManifold", "RiemannianMetric",
    "ContMDiffRiemannianMetric", "SmoothManifoldWithCorners", "ModelWithCorners"
  ]
  let mut lines : Array String := #[]
  lines := lines.push "# Step 71 Lean capability report"
  lines := lines.push s!"total_constants={names.length}"
  for needle in needles do
    let hits := names.filter (fun n => n.contains needle)
    lines := lines.push s!"\n## {needle}: count={hits.length}"
    for h in hits.take 60 do
      lines := lines.push h
  IO.FS.writeFile "Sessions/S0910A02/workspace/data/step71_lean_capability_report.txt" (String.intercalate "\n" lines.toList)

