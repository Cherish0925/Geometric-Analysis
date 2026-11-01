# Session S1003A02 — Einstein Gaps on Four-Manifolds (Discovery loop 1; resumed after Step 34; owner-authorized continuation at Step 101)

## Governing goal
The aligned goal is the human's original goal verbatim (human-confirmed, unchanged). This loop is Discovery: success is new, fully proved mathematics about α(M)=inf_g 𝒟(g) — positivity conditions, matching bounds with correct scale/constants, realizing constructions, rigidity and near-extremal structure, degeneration, and the relation between positive gap, approximation, attained infimum and exact Einstein existence. Papers belong to a later Writing loop; keep proofs in the workspace in exposable form. Cumulative Step cap 108 (owner-authorized extension from 100; no further increase assumed). No human reply means neither mathematical endorsement nor completion.

## Inheritance
Read `Skills/geometric-analysis/SKILL.md` and its references, then `workspace/notes/state_of_problems_1_4.md` (§6 = state at the close of Steps 1–100, with reading provenance), `workspace/notes/theorem_package_v1.md` (dependence-ordered, status-tagged package; §22.6(7) for Steps 93–99), `workspace/notes/step58_consolidated_hypothesis_ledger.md`, and `workspace/notes/step99_independent_verification_and_repairs.md`. The human functional is 𝒟=(4P+L_s)/R (R>0), 𝒟=4 at Ricci-flat metrics; every statement is tagged P or α; covers scale P but not 𝒟. Keep all inherited theorems with their exact scopes: N1 (actual supply only), Theorems L′, Z, Z′, ASD, F, 59.R, 61.EH, 66.R, 69.KE, 71.B–D′, 74.W, Lemma 86.S, 87.O, 93.A, 95.S/F, 96.Ş/K, 98.W/98.V as repaired at Step 99.

## Steps 101–108 (owner-authorized continuation)
0. First, read A01's latest substantive progress (A01 is at Step 87 and continues to 95; its notes are under `Sessions/S1003A01/workspace/notes/`, latest peer message #881 on regularized torsion transport is unread). Exchange through `qiushi-session-group` the most important current understanding, unresolved problems and complementary work; avoid duplicating A01's lines (A01: constructions, saving mechanisms, regularized Q4 identities; A02: constraints over all competing geometries, verification, lattice/orbifold classification).
1. Give an independent Agent reading to the two items checked only by TTCS in the Step that wrote them: the Step-99 strengthenings of 98.W/98.V (torsion-block elimination, L=Q_X⊕L₀, k≥4t, chain primitivity) and the nonattainment of P_{*,orb} in 93.A. Repair in place if needed.
2. Attack the fixed-topology centre X#kCP̄², 0<k<A/3, where any obstruction must now live: (a) geometric realization — embedded Wahl balls or D_{≥6} prism complements with the prescribed complement and degree-one map, or exclusion via w₂/spin^c or Dedekind/APS data; (b) singular analysis — existence or exclusion of a negative Einstein orbifold via orbifold SW / type-T information; (c) smooth side — a metric-wise class-sensitive relation valid through aligned AK and cscK degeneracies and compatible with the certified cells, or the density-free O10 endpoint. Choose by whether a Step can change one of the three global alternatives (α>0 / α=0 nonattained / smooth negative Einstein).
3. Problem 4: test A01's regularized q+ε torsion budget and the identification T_AK=T on the complete noncompact strict AKE pair before using either; T_AK≥2π²k adds nothing once T_AK=T.
4. Do not extend finite lattice tables without a geometric candidate. Do not treat local models, conditional results or package organization as completion of the goal. At Step 108 leave nothing half-edited; keep `state_of_problems_1_4.md` synchronized with the package and send A01 the updated state.

## Problem-specific discipline
- Integral approximation, pointwise approximation, local repair and Einstein existence are different conclusions; P-zero and α-zero are different.
- Fixed topology needs same-metric scalar+Weyl comparison; separate infima cannot be subtracted; signed errors must be o(Q); every lower bound needs a competitor at the same scale.
- Aggregate smooth transfer through resolution is class-blind once its budget passes (retained ranks are paid by the bulk as in the smooth problem); do not repeat it expecting class-sensitive information.
- Aligned AK, J-invariant-Ricci/Einstein–Maxwell and cscK loci are where coercivity degenerates, not escape routes; only the Einstein end carries p→0.
- Survivors of charge/lattice screens are necessary data, never constructions.
- Each freshly written result needs an independent reading before it enters the package; the last writer must not be the last reader. Grep the corpus before any [N] tag; one knowledge request per theorem.
- Exchange with A01 testable inequalities and their quantifiers, not task lists.

## Tools
`qiushi-geometry env {core,sage,tensor,topology,pde}`, `qiushi-wolfram-run` (license was expired at Step 95 — use exact SymPy/Fraction if still so), `qiushi-lean-proof` where formalization removes real doubt, bg_task after a pilot. Knowledge requests before novelty claims. Scripts in `workspace/scripts`, data in `workspace/data`, proofs/notes in `workspace/notes`.

## Completion
End only when the central propositions are closed by complete proofs, optimal constructions or decisive counterexamples with the common mechanism explained and each statement's scope exact. Stating limits honestly is required but does not replace attacking attackable gaps now.
