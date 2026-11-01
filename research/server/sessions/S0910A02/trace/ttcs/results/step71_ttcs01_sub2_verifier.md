# TTCS Independent Branch Record

```json
{
  "step_id": 71,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step71_collapse_quantum_and_lean_scope.md",
    "Sessions/S0910A02/workspace/scripts/step71_collapse_quantum_diophantine.py",
    "Sessions/S0910A02/workspace/data/step71_collapse_quantum_diophantine.json",
    "Sessions/S0910A02/workspace/notes/step58_biquard_ct_and_collapse_ceiling.md",
    "Sessions/S0910A02/workspace/notes/step64_positive_mirror_homeomorphism_and_allocation.md",
    "Knowledge/objects/papers/Curvature-cones-and-characteristic-numbers--8d08033cf0c7--47e3a363f7a4/object.md",
    "Knowledge/objects/papers/The-collapsing-geometry-of-almost-Ricci-flat-4-manifolds--a6608f08b3f8--f94b3ef0dffe/object.md",
    "Sessions/S0910A02/workspace/proofs/Step71RicciOnlySearch.lean",
    "Sessions/S0910A02/workspace/proofs/Step71Yau26SyntheticStatement.lean"
  ]
}
```

## Task

Verify the Step-71 collapse quantum/chiral-split audit for the positive-collapse front of Yau Problem 26. The target is the spin balanced row homeomorphic to #_3(S^2 x S^2), with chi=8 and tau=0, under a hypothetical positive Ricci-pinched collapse Vol->0. Check: (1) the corrected Chern--Gauss--Bonnet ledger total int|W|^2 -> 64 pi^2 and chiral split int|W+|^2=int|W-|^2 ->32 pi^2; (2) ALE Ricci-flat quantum Q=chi-1/|Gamma| and ALF quantum Q=chi as used; (3) the ADE enumeration result that total Q=8 has only 3*A2 but no ADE multiset has Q=4 in one chiral half; (4) whether the inference to a compatibility gate for half-flat ALE/ALF concentration is valid or needs caveats about orientation, signature boundary terms, ALF/ALG/collapsed bubbles, or non-hyperkaehler Ricci-flat limits; (5) whether the Lean/Mathlib scoping conclusion is accurately separated from mathematical proof. Give a direct mathematical memo: identify errors, overclaims, missing assumptions, and the strongest valid conclusion for the next research step.

## Output

# Verification Memo — Step-71 collapse quantum and chiral-split accounting for the #₃(S²×S²) row

## Bottom line

The arithmetic is correct. The corrected Chern–Gauss–Bonnet ledger (total → 64π², chiral halves → 32π² each), the ALE/ALF quantum formulas, and the ADE enumeration (total Q = 8 realized only by 3·A₂; no ADE multiset gives Q = 4 in one chiral half) all check out, and I confirm them two independent ways below. The separation of the Lean/Mathlib infrastructure statement from mathematical content is accurate. The one place that needs sharper statement is the inference from "no ADE 4+4 split" to a constraint on collapse: as written it covers only Kronheimer SU(2) hyperkähler ALE bubbles with atomic chiral assignment, and several classes of Ricci-flat concentration are not enumerated. The note flags two of these; it is thin on two more.

---

## 1. CGB ledger: total → 64π², chiral 32π² each — correct

χ(#₃(S²×S²)) = 2k+2 = 8 and τ = 0 are correct (these are homeomorphism invariants, so the uncertain diffeotype recorded in Step 64 does not affect them). The smooth-metric case of the paper's Theorem 2.1 gives

χ = (1/8π²)∫(s²/24 + |W|² − |Ric°|²/2).

Under Ric ≈ g the scalar is s ≈ n = 4 and the trace-free Ricci Ric° → 0 pointwise; since Vol → 0,

∫(s²/24 − |Ric°|²/2) dμ ≈ (16/24)·Vol → 0,

so ∫|W|² → 8π²·8 = 64π². The signature formula ∫|W⁺|² − ∫|W⁻|² = 12π²τ = 0 then forces ∫|W⁺|² = ∫|W⁻|² → 32π² = 4·(8π²) each. All internally consistent with Step 58's identity A± = 2π²(2χ ± 3τ) − (1/2)∫(…), which gives A± → 4π²χ = 32π².

One point worth stating more forcefully than the note does: the "regions of bounded curvature contribute o(1)" step is not merely plausible, it is forced. On a region with |Rm| ≤ Λ the CGB integrand is O(Λ²) and the region's volume is ≤ Vol(M) → 0, so its contribution vanishes. More strongly, a Vol→0 collapse with *globally* bounded curvature is impossible here: Cheeger–Fukaya–Gromov collapse with bounded curvature forces χ = 0, and χ = 8 ≠ 0. Hence curvature concentration is unavoidable, and the concentration regions must carry the full 8 units. This is a rigorous ingredient, independent of any regularity transfer (and therefore not touched by the Step-11 obstruction to pointwise ε-regularity from C⁰ Ricci pinching).

Also correct: rescaling by the concentration curvature scale sends Ric = g to Ric = λ⁻²g → 0, so the blow-up limits are Ricci-flat. On a Ricci-flat 4-manifold Rm = W, so ∫|Rm|² = ∫|W|²; the quantum accounting is legitimate.

## 2. ALE quantum Q = χ − 1/|Γ| and ALF quantum Q = χ — correct

Both are source-matched to the Atiyah–LeBrun paper. From Gauss–Bonnet with an end term (eq. 5.16), the det(II) contribution at the asymptotic end gives 1/|Γ| times the S³ integral for ALE (∫|Rm|² = 8π²(χ − 1/|Γ|), eq. 5.17), and vanishes under ALF volume/curvature decay (∫|Rm|² = 8π²χ, eq. 5.18). Table 1 confirms the ADE values used by the script. The convention |W|² = ¼W_{jklm}W^{jklm} is the paper's, and the Eguchi–Hanson check (χ=2, |Γ|=2 → 12π² → Q = 3/2 = A₁) closes. The script's data (A₁: 3/2, A₂: 8/3, A₃: 15/4, D₄: 39/8, E₆: 167/24, E₇: 383/48, E₈ = 9−1/120 > 8 excluded) all reproduce Table 1.

The ALF-uses-integer-quantum step is sound for the multi-Taub–NUT (A_k) and D_k ALF families used, and it depends on the finite-topological-type / decay hypothesis being met — which is exactly the regime Lott describes for the collapsed K3.

## 3. ADE enumeration: total 3·A₂ unique, no chiral Q = 4 — correct, and confirmable analytically

I verify the brute-force result with an independent invariant. For any ADE multiset, ΣQ = Σχ − Σ(1/|Γ|). If ΣQ is an integer T, then Σ(1/|Γ|) = Σχ − T must be a positive integer with each summand < 1.

- **Total T = 8.** Partitions of a positive integer into the available unit fractions {1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/12, 1/16, 1/20, 1/24, 1/48}: the reciprocal sum must be 1 (sum ≥ 2 needs too many pieces, overshooting Q). Reciprocal partitions of 1 that could give Q = 8: {A₁,A₁} → Q=3; adding any further piece changes the reciprocal sum away from an integer, so the multiset is forced to be exactly {A₁,A₁}, Q=3 ≠ 8. {A₂,A₂,A₂} → reciprocal 1, Q = 3·(8/3) = 8 ✓. Any other reciprocal-1 partition ({A₃⁴}, {A₁,A₃,A₃}, {A₁,A₂,A₅}, …) overshoots Q. So 3·A₂ is the unique solution — matching the script.
- **Chiral half T = 4.** The reciprocal sum must again be a positive integer, minimally 1. Reciprocal-1 partitions give Q ∈ {3 (two A₁), 8 (three A₂), 15 (four A₃), …} — 4 is not attained; no other partition reaches Q = 4. Hence no ADE multiset has Q = 4, confirming zero chiral solutions.

The 3·A₂ configuration (subset sums 0, 8/3, 16/3, 8) cannot split 4+4, so it is arithmetically incompatible with the τ = 0 requirement of equal chiral halves. Correct.

- **ALF completion.** Integer-Q ADE contributions ≤ 4 are 0 and {A₁,A₁}=3; completing to 4 by ALF integer units gives exactly (0 ALE + 4 ALF) or (2·A₁ + 1 ALF), as the script reports. Note a full configuration must realize 4 in *both* halves simultaneously; e.g. {+ half: 2A₁+1 ALF} and {− half: 2A₁+1 ALF}, with the two A₁/ALF groups carrying opposite hyperkähler orientation.

## 4. Reach of the "arithmetic constraint" — valid but narrower than a collapse exclusion

The chiral atomicity used here is correct where it is invoked: a hyperkähler 4-manifold has holonomy ⊂ Sp(1) = SU(2), hence is self-dual (W⁻ = 0 pointwise) for one of its two orientations, so its entire quantum sits in a single Weyl half, and no end/eta correction is needed for that assignment. Bubbles of opposite hyperkähler orientation populate the two halves, and the 4+4 requirement is the right necessary condition. So *within the enumerated class* the exclusion is a genuine necessary arithmetic condition.

What the exclusion does **not** yet reach:

- **Non-SU(2) Ricci-flat ALE.** Kronheimer's ADE list is exhaustive only for ends R⁴/Γ with Γ ⊂ SU(2). Ricci-flat ALE spaces with Γ ⊂ U(2) (Suvaina/Wright-type quotients) exist, have different (χ, |Γ|) and hence different quanta, and can be half-flat. Enumerating only ADE therefore does not close the half-flat case. This is the largest missing piece and the note does not mention it.
- **Non-half-flat Ricci-flat bubbles.** A Ricci-flat 4-manifold with both W⁺ ≠ 0 and W⁻ ≠ 0 contributes to both halves, so the split ceases to be atomic; the multiset arithmetic no longer applies. The note flags this ("non-half-flat/non-ADE Ricci-flat concentration").
- **ALF/ALG/ALH and Ooguri–Vafa transition regions.** The Lott reference is decisive here: genuinely collapsed 4-dimensional Ricci-flat sequences bubble ALF (dihedral, Taub–NUT) pieces and carry curvature in incomplete Ooguri–Vafa/ALG transition regions that cobound the ALF ends and the collapsed base. That curvature is not captured by discrete complete-ALE quanta, and its chiral assignment and topological attachment are exactly what remain unknown. The note flags this correctly and it is the main reason the arithmetic is not a collapse exclusion.
- **Existence of the concentration decomposition itself.** The clean bubble-tree picture with well-defined ALE/ALF quanta rests on Anderson/BKN/Tian-type L²-curvature and non-collapsing-at-bubble-scale inputs proven for almost-Ricci-flat/Einstein settings. Under mere C⁰ two-sided Ricci pinching with Vol→0, that the concentration is a finite union of complete instantons with the tabulated quanta is not established. The χ≠0 forcing (item 1) gives concentration but not this structure. The note acknowledges "determine which concentration geometries occur," which is the honest statement of what is unresolved.

There is no arithmetic error to correct; the corrections are additive assumptions: "Kronheimer SU(2) ADE," "half-flat," "atomic (transition-region-free)," and "complete-instanton concentration."

## 5. Lean/Mathlib infrastructure statement vs mathematical content — accurately separated

The environment probe (`Step71RicciOnlySearch.lean`) greps `env.constants` under `import Mathlib` for Ricci/Riemann/sectional/scalar-curvature/Levi-Civita/Christoffel substrings and reports none, while `IsRiemannianManifold`, `Bundle.ContMDiffRiemannianMetric`, `ModelWithCorners` exist. Because `import Mathlib` pulls the whole library, the substring search over `env.constants` is comprehensive for the imported environment, so the conclusion "the two-sided Ricci-pinching hypothesis cannot presently be stated with native curvature objects" is well-founded (the only gap is curvature registered under an unrelated name, which the substring set makes unlikely). This is an infrastructure statement, not a mathematical one, and it is labeled as such.

The synthetic `GeometryInterface`/`Yau26Statement` file is correctly presented as an uninterpreted logical shell: `RicciPinched`, `EinsteinMetric`, `IsClosedConnectedSmoothRealManifold` are abstract fields, and `dimensionStatement_of_normalizedSignBranch` and `yau26Statement_unfold` are trivial logical/`rfl` facts. The quantifier structure matches the target (∀ n ≥ 2, ∃ c < C dimension-only, ∀ closed connected smooth Mⁿ, ∀ g with c g ≤ Ric ≤ C g, ∃ Einstein h; no closeness, no sign restriction). Nothing here asserts geometric truth, and the note says so. Accurate.

---

## Strongest valid conclusion and the productive next object

What is rigorously in hand for this row:
1. Any Vol→0 collapse of a metric with Ric ≈ g on #₃(S²×S²) must concentrate curvature (χ = 8 ≠ 0 rules out bounded-curvature collapse), with ∫|W±|² → 32π² in each Weyl half.
2. If that concentration is a disjoint family of Kronheimer SU(2) hyperkähler ALE bubbles of definite chirality, the required 4+4 unit split has no solution; adding ALF integer units, a single chiral half of value 4 is realizable only as 4 pure ALF units or as 2·A₁ + 1 ALF.

Statement 2 is a correct necessary arithmetic condition on that specific model, not an exclusion of collapse.

The object that would convert this arithmetic into a genuine constraint on the collapse is a structural theorem about which Ricci-flat concentration geometries a C⁰ positively-Ricci-pinched Vol→0 sequence on this row can carry — specifically: whether Γ ⊂ U(2) (non-SU(2)) ALE, non-half-flat Ricci-flat bubbles, and ALF/ALG/Ooguri–Vafa transition regions can appear, and how each is assigned to W⁺ vs W⁻ together with its topological attachment to the collapsed base. The most cost-effective sub-target is to redo the enumeration with (i) the U(2)-quotient ALE quanta added and (ii) ALF A_k/D_k units placed with explicit chirality, and then ask whether *any* 4+4 realization is topologically consistent with #₃(S²×S²) — which would tell you whether the arithmetic can ever bite or whether transition-region curvature must always absorb the mismatch. Independently, it is worth recording whether uniformly-positive two-sided Ricci pinning with Vol→0 is even geometrically possible on a fixed diffeotype; the Lott/Cheeger–Tian collapse literature cited is almost-Ricci-*flat* (Ric→0), and the positive-pinched Vol→0 regime is not obviously populated. Establishing impossibility there would resolve the collapse half directly, without the quantum arithmetic.