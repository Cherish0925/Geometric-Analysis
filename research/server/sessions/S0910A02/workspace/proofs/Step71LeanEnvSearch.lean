import Mathlib
import Lean

open Lean

#eval show CoreM Unit from do
  let env ← getEnv
  let names := env.constants.toList.map (fun kv => kv.fst)
  let needles := ["Ricci", "ricci", "Riemann", "riemann", "Curvature", "curvature", "Manifold", "Riemannian", "Metric"]
  for needle in needles do
    let hits := names.filter (fun n => n.toString.contains needle) |>.take 40
    IO.println s!"NEEDLE {needle}: {hits.length} shown"
    for h in hits do IO.println s!"  {h}"

