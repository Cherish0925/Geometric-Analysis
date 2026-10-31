# Route allocation after Step 64 (A02 / Agent1 judgment)

Session `S0910A02`. Basis: Steps 45–64 record, Strategist Step-64 note, peer
messages #445–#452. Full argument: `workspace/notes/step64_positive_mirror_homeomorphism_and_allocation.md`.

## Fixed points of the landscape

- Refutation of any branch needs BOTH (i) arbitrarily pinched metrics and
  (ii) non-existence of an Einstein metric on the underlying smooth manifold.
  The construction half is done to current-tool level on the noncollapsed
  positive arc (Steps 49–50, operator-norm principle).  The open half is
  always (ii).
- Step 63: the obstruction/necessity framework is sharp at δ·log(1/t) and is
  blind beyond it; it cannot decide (ii).  The jet-drift channel is therefore
  NOT a counterexample route (answer to A03 #450).
- Four-dimensional Yau-26 is exactly as hard as Einstein existence on
  SW-void, simply connected, b_+ ≥ 2 manifolds.  The χ = 8 positive-mirror
  rows are where that hardness is cheapest, and they now have names.

## The named decision point (Step-64 classification)

| row | homeotype | Einstein |
|:--|:--|:--|
| r=0 | #CP^2#5CP̄^2 | del Pezzo, known (anchor) |
| r=1 | #_2CP^2#_4CP̄^2 | OPEN |
| r=2 spin | #_3(S^2×S^2) | OPEN; = k=3 stress family (homeo) |
| r=2 non-spin | #_3CP^2#_3CP̄^2 | OPEN; unconditionally realizable |
| r=3 | #_4CP^2#_2CP̄^2 | OPEN |
| r=4 | reverse of r=0 | known |

## Active queue for A02 (priority order)

1. **Balanced-row Einstein experiment (main line, next arc).**
   Export the explicit near-pinched glued metric on one balanced row —
   prefer the non-spin #_3CP^2#_3CP̄^2 pattern (no spin gluing needed), with
   #_3(S^2×S^2) as the second target — as a concrete initial tensor field;
   run Einstein–DeTurck (or variational Ricci-functional) search.
   - Convergence ⇒ positive-Einstein existence on an SW-void non-Kähler s.c.
     manifold: new existence machinery, and a verified consequence of P_4^+.
   - Robust divergence with identifiable mechanism ⇒ candidate refutation of
     P_4^+ (then escalate: independent verification, group cross-check).
   - Failure criteria pre-registered: distinguish "no convergence because far
     Einstein exists" from "no Einstein at all" — a divergence mechanism must
     be named (e.g. curvature concentration with a limiting soliton/ALE
     profile, L² curvature blowup rates, obstruction residue growth).
2. **H_flux: one final focused attack, then standing hypothesis.**
   Work items: TT/Bianchi gauge on neck annuli; ambient H_2/H_4 tower
   subtraction at signal order t_i; nonlinear/gauge/bad-set errors;
   inner/outer ALE flux normalization; target estimate
   |B_k(r2)−B_k(r1)| ≤ C t_i δ_i log(r2/r1) + o(t_i).
   Deliverable: either a proof under δ_i·log(1/t_i)→0, or a precise standing
   hypothesis statement archived and not re-opened without new input.
3. **p = 1/3 sharpness experiment (bounded, negative side).**
   Near-pinched constructions on IL-type manifolds just above p = 1/3 vs the
   stable gap δ/(1−δ) ≥ √((p−1/3)/2): is the zero-margin endpoint a real
   risk locus or an estimate artifact?  Small, self-contained, complementary
   to A01/A03 flow work.

## Explicitly defunded / not A02's

- Global drift-neck realization on mixed-wall rows (invests in solved half).
- Fourth wall variant / new product-quotient family.
- IL defect-Moser plumbing: A01 owns the blocking gap; A03 Codex derivation
  is under peer audit (#445, #447).  A03's μ_4 / graph-gap and Di Cerbo
  margin routes stay with A03 (#446, #449–450).
- Positive collapse on M_k as a standalone arc: superseded into the merge —
  the balanced spin row IS the k=3 member; collapse questions now enter
  through the same named-manifold experiment and through H_flux.

## Long-range reminders (unchanged)

n ≥ 5: no known closed manifold without any Einstein metric; proof-side or
new-obstruction-side only.  Lean formalization: nothing yet formalizable
beyond Step 27–29 local algebra; the Step-64 classification is a future
formalization candidate (finite topological ledger).  Full proposition still
requires both sign branches per dimension; no branch is decided.
