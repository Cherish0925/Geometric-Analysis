import Mathlib
import Lean

/-!
Environment-level complement to the source scan.  This inspects every constant
loaded by `import Mathlib`, so it can catch declarations re-exported under
unexpected source paths.  Substring search cannot rule out an entirely
unrelated name; the source scan and inspected geometry modules are the other
two parts of the audit.
-/

open Lean

private def reportNeedle (names : List String) (needle : String) : CoreM Unit := do
  let hits := names.filter (fun name ↦ name.contains needle)
  IO.println s!"{needle}: count={hits.length}"
  for hit in hits.take 40 do
    IO.println s!"  {hit}"

#eval show CoreM Unit from do
  let env ← getEnv
  let names := env.constants.toList.map (fun entry ↦ entry.fst.toString)
  for needle in [
      "LeviCivita", "Levi_Civita", "leviCivita", "Christoffel",
      "RiemannCurvature", "riemannCurvature", "RiemannTensor", "riemannTensor",
      "Ricci", "ricci", "ScalarCurvature", "scalarCurvature",
      "SectionalCurvature", "sectionalCurvature",
      "CovariantDerivative", "RiemannianMetric"] do
    reportNeedle names needle
