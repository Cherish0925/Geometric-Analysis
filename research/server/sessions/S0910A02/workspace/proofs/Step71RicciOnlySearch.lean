import Mathlib
import Lean

open Lean

#eval show CoreM Unit from do
  let env ← getEnv
  let names := env.constants.toList.map (fun kv => kv.fst.toString)
  let needles := ["Ricci", "ricci", "RiemannCurvature", "riemannCurvature", "sectionalCurvature", "scalarCurvature", "LeviCivita", "Christoffel", "PseudoRiemannian"]
  for needle in needles do
    let hits := names.filter (fun n => n.contains needle)
    IO.println s!"{needle}: count={hits.length}"
    for h in hits.take 25 do
      IO.println s!"  {h}"

#check IsRiemannianManifold
#check Bundle.ContMDiffRiemannianMetric
#check ModelWithCorners

