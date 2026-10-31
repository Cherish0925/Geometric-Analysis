# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Skills/geometric-analysis/research/paper/sections/single_solution_coercivity.tex",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Sessions/S1003A02/workspace/scripts/paired_cross_field_algebra.py",
    "Sessions/S1003A02/workspace/data/paired_cross_field_algebra.json"
  ]
}
```

## Task

Verify the simultaneous signed-cost/amplitude identity as a proof-level mathematical statement. Check every coefficient and normalization from the single-solution identities through Walsh Parseval, the Weitzenböck formula at s=-4, the clean amplitude completion, and the necessary condition for a sequence with P/(8π^2 k)->c<1. Determine the exact band interpretation using m(rho), including the root near 0.77579, and state which nonnegative terms measure the realized fraction of the deficit bound. Identify any unsupported equation or quantifier. The active goal is a same-metric lower theory for M=X#k CPbar^2 that must permit the certified subunit cell. Read the actual files, not merely this task prose.

## Output

# Verification memo: the simultaneous signed-cost and amplitude identity for M = X # k CP̄²

## Summary

- **Every coefficient checks.** I checked the chain from the single-solution decomposition through Walsh–Parseval, the Weitzenböck substitution at s = −4, and the clean amplitude completion.
  - The one imported identity, the β = 2 decomposition (eq. `ssc-exact-decomposition`), is cited from a proof file that was not supplied.
  - I re-derived it below from first principles.
- **The amplitude bound is LeBrun-strength, not stronger.** P ≥ 8π²Q − 4𝔼∫(2−ρ) is an exact rearrangement of the averaged LeBrun Weyl–scalar estimate. It contains no information beyond that estimate.
- **The identity permits the certified subunit cell.** A deficit exists only if three things happen together:
  - the field amplitude ρ is shallowly depleted, sitting in the band ρ ∈ (ρ*, 2) with ρ* ≈ 0.775789;
  - the spin direction rotates with energy bounded below;
  - each exceptional class E_i is nearly anti-self-dual for g.
- **One statement in the Step-38 note conflicts with the identity.** In note §8, rotation energy that vanishes as A_E → 0 is offered as the field countermechanism behind subunit perpendicular cells. Vanishing rotation energy gives no deficit; the identity requires rotation energy of at least 8π²(1−c) per blow-up.

## 1. Normalizations, fixed by the Kähler–Einstein point

The normalization is F⁺ = 2iσ(Φ) with |σ(Φ)|² = ρ²/8. This gives |f⁺|² = ρ²/2 and |ψ| = ρ for ψ = 2√2 σ(Φ) = √2 f⁺.

**Kähler–Einstein check (s = −4).**
- The Ricci form has |ω|² = 2, which forces ρ ≡ 2.
- W⁺ has eigenvalues −2/3, 1/3, 1/3.
- The model W₀ = ¼(ρ²/3·I − ψ⊗ψ) has the same eigenvalues: −ρ²/6 on ψ and ρ²/12 on its orthogonal complement.
- |W₀|² = ρ⁴/24 = 2/3 = s²/24.

**Spinor Weitzenböck coefficient.** Write ∇*∇Φ = (−s/4 − κρ)Φ. Parallel Φ at ρ = 2 forces κ = 1/2, so ∇*∇Φ = (1 − ρ/2)Φ. This gives:
- 0 ≤ ρ ≤ 2 by the maximum principle;
- K_ε = ½∫ρ_ε(2 − ρ_ε).

The script's `K_from_slack = I1 − I2/2` derives K from the slack formula, which was itself derived from this Weitzenböck formula. It is a consistency check, not an independent confirmation. The Kähler–Einstein pin above supplies the independent part.

**Other single-solution identities.**
- Harmonic projection: ∫ρ² = 8π²p + 2J, since ∫|f⁺|² = 4π²p + J.
- Rescaling: K_rescaled = (2/√6)K and U = 2(ρ₂ − 2). These convert Σ = 8√6 K_r + ∫U² + 8J into Σ = 16K + 4∫(ρ−2)² + 8J.

## 2. Independent derivation of the single-solution decomposition

Write W₊ = ∫|W⁺|². Using ⟨W⁺, W₀⟩ = −¼ W⁺(ψ,ψ) and |W₀|² = ρ⁴/24:

D/18 − ‖W⁺ − W₀‖² = 4V/3 − 4π²p − ½∫W⁺(ψ,ψ) − ∫ρ⁴/24.

**Step 1 (self-dual Weitzenböck).** On Λ⁺, Δ = ∇*∇ − 2W⁺ + s/3. For self-dual ψ, ∫⟨Δψ, ψ⟩ = 2‖dψ‖². This gives

−½∫W⁺(ψ,ψ) = ½‖dψ‖² − ¼‖∇ψ‖² + ⅓∫ρ².

**Step 2 (target identity).** Substitute 4π²p = ½∫ρ² − J. The decomposition with C(t) = t + 1 − (t+2)²/12 then holds if and only if

½‖dψ‖² − ¼‖∇ψ‖² = 2‖ζ‖² + ∫(ρ³/2 − ρ²).

Here I used ½C(t)(t−2)² = −t⁴/24 + t³/2 − 7t²/6 + 4/3.

**Step 3 (Bloch split and spinor Weitzenböck).**
- The Bloch split ψ = ρn gives |∇ψ|² = |dρ|² + ρ²|∇n|² = 4ρ|∇Φ|² − 4(Im ζ)².
- The spinor Weitzenböck formula gives ∫ρ|∇Φ|² = ∫(ρ² − ρ³/2) − ½‖dρ‖².
- With dρ = 2Re ζ, the target reduces exactly to ‖dψ‖² = 2‖Im ζ‖².

**Step 4 (Dirac step).** Use the quaternionic model:
- S^± = ℍ, Clifford multiplication is left multiplication, and DΦ = Σ e_j ∇_jΦ.
- ψ ↔ u = Φ i Φ̄, an isometric identification of Λ⁺ with Im ℍ.
- d*ψ ↔ (1/√2) Σ_j e_j ∂_j u.

Write ∇_jΦ = Φ m_j with m_j = α_j + β_j i + γ_j, where γ_j ∈ span{j, k}. Then Φ i m̄_j Φ̄ = Φ m_j i Φ̄ + 2β_j ρ, and the Dirac equation removes the first term:

Σ_j e_j ∂_j u = 2ρ Σ_j β_j e_j, with |Im ζ_j| = ρ|β_j|.

Hence |dψ|² = |d*ψ|² = 2|Im ζ|² pointwise. This is first order and gauge invariant, so it holds on any curved metric with a twisted connection.

**Consequence.** The decomposition, and with it everything downstream, holds for every actual solution at s = −4.

## 3. Signed remainder, Chern–Weil, and Walsh–Parseval

**Signed remainder.** Substituting D/18 and Σ/4 into 4W₊ + 4V/3 − ∫ρ² = 2D/9 − Σ/4 − 2J:
- the J terms cancel (4 − 2 − 2 = 0);
- the amplitude coefficient is 2C − 1 = b(ρ) = (−ρ² + 8ρ + 2)/6, with min_{[0,2]} b = b(0) = 1/3.

**Topological input.** P = 4W₊ + 4V/3 − 8π²(A − Q) uses only T₊ = 2χ + 3τ = A − Q.

In the paper's eq. (`webvar:joint-energies`), the formulas χ = A/3 + k − 2ℓ and the reference value 4π²A/3 + 12π²k carry an unstated hypothesis χ(X) = A/3, i.e. X a ball quotient. For the Step-38 manifold with general X, only the T₊ form is valid. The invariant statement is

P − 8π²Q = 4(W₊ + V/3 − 2π²A).

**Chern–Weil.**
- a_ε² = A − k gives P = 32π²ℓ + 2‖f_ε⁻‖² + 4W₊ + 4V/3 − ∫ρ_ε².
- c₂(S⁺) = ℓ.

**Walsh–Parseval.**
- The classes of the Walsh averages are [f_∅/2π] = c, [f_{i}/2π] = E_i, and [f_I] = 0 for |I| ≥ 2.
- Hence 𝔼‖f⁻‖² = 4π²k + ‖f_∅⁻‖² + Σ_{I≠∅}‖f_I⁺‖².
- The pair form 2Σ_{I≠∅}‖f_I⁺‖² = 𝔼_{ε,ε'}∫[(ρ−ρ')²/2 + 2|w|²] is valid. It needs the canonical identification su(S⁺⊗N) = Λ⁺, which holds.

**Script data.** The symbolic Fierz residuals are all 0, and the Walsh variance identity agrees to 2×10⁻¹⁶.

**Result.** P − 8π²Q = 𝒜 − 4𝔼K is exact for every choice of solutions.

## 4. Clean amplitude completion and the band structure

**Completion.** Write 4K = 4∫(2−ρ) − 2∫(2−ρ)². Then

P − 8π²Q + 4𝔼∫(2−ρ) = R,

where R is the sum of the following nonnegative terms:
- 2‖f_∅⁻‖²;
- the pair term 𝔼_{ε,ε'}∫[(ρ−ρ')²/2 + 2|w|²];
- 𝔼[8‖ζ‖² + 4‖W⁺ − W₀‖² + ∫(b+2)(2−ρ)²].

Here b + 2 ∈ [7/3, 13/3] on [0, 2].

**Equivalent m-form.** With m(ρ) = 4(2−ρ) − (b+2)(2−ρ)² = (2−ρ)q(ρ)/6 and q = −ρ³ + 10ρ² − 2ρ − 4:

8π²Q − P = 𝔼∫m(ρ_ε) − R₀,

where R₀ ≥ 0 is the sum of R's terms other than the amplitude term ∫(b+2)(2−ρ)².

**Properties of m.**
- **Sign change.** q has a single root in [0, 2], at ρ* ≈ 0.775789 (q′(ρ*) ≈ 11.71). The other two roots lie near −0.53 and 9.75.
- **Deep depletion is a cost.** m < 0 on [0, ρ*), with m(0) = −4/3; m′(0) = 0, so ρ = 0 is a local minimum of m.
- **Shallow depletion pays.** m > 0 on (ρ*, 2).
- **Maximum.** Setting m′ = 0 gives ρ(ρ² − 9ρ + 11) = 0. The maximum is at ρ = (9 − √37)/2 ≈ 1.45862, with m_max ≈ 1.01556. This is in s = −4 normalization, per unit volume.
- **Endpoint.** m(2) = 0 and m′(2) = −4.

**Local efficiency.** The fraction of the linear allowance 4(2−ρ) that is realized pointwise is m/(4(2−ρ)) = q(ρ)/24.
- It increases from −1/6 at ρ = 0 to 1 at ρ = 2.
- Near the top, q(2−η)/24 = 1 − 13η/12 + O(η²).
- The coefficient 4 is therefore sharp only pointwise, as ρ → 2. Global sharpness would additionally need R₀ = o(allowance), and this is not shown in the note.

**Realized fraction.** Let Λ = 4𝔼∫(2−ρ). Then

θ = (8π²Q − P)/Λ = 1 − R/Λ.

- The term ∫(b+2)(2−ρ)² converts 4(2−ρ) into m.
- R₀ is the field-geometric cost.
- Inside R₀, the determinant part splits as 2‖f_∅⁻‖² + 2Σ‖f_I⁺‖² = 8π²[(c⁺)² − A + Σ_i(E_i⁺)²] + 2𝔼J.

**Spin rotation is not a cost in R.** It enters only through K. By the Weitzenböck formula, K = ½∫ρ(2−ρ), so rotation enlarges the allowance Λ instead of being charged.

## 5. Relation to the classical LeBrun bound

Averaging 4∫(2−ρ_ε) = 4V − 8π²p_ε − 2J_ε + ∫(2−ρ_ε)² and using the Walsh comparison gives:

4𝔼∫(2−ρ) = 4(V − 2π²A) − (2‖f_∅⁻‖² + 2Σ‖f_I⁺‖²) + 𝔼∫(2−ρ)²,

P − 8π²Q + 4(V − 2π²A) = 4‖f_∅⁻‖² + 4Σ‖f_I⁺‖² + 𝔼[8‖ζ‖² + 4‖W⁺ − W₀‖² + ∫(b+1)(2−ρ)²].

The second line is the convex-hull LeBrun estimate W₊ + 4V/3 ≥ 4π²A. In the paper's variables, for ball-quotient X, it reads Δ_W ≥ −Δ_S/6.

Consequences:
- The amplitude bound and the volume bound differ by 2(det) − 𝔼∫(2−ρ)², which can have either sign.
- Both are the averaged single-solution identity. Neither reaches P ≥ 8π²Q − o(Q), which is the inequality Δ_W ≥ −Δ_S/24.
- This matches the paper's remark that simultaneous organization leaves the averaged classical budget unchanged.

## 6. Necessary structure for P/(8π²k) → c < 1

Take ℓ = 0, so Q = k, and work on Yamabe representatives. The transfer to arbitrary metrics uses P(g) ≥ P(ĝ), with ρ evaluated on ĝ.

| | Condition |
|---|---|
| N1 | 𝔼∫m(ρ_ε) ≥ 8π²(1−c)k + R₀, which implies 𝔼∫_{ρ>ρ*}(2−ρ) ≥ 2π²(1−c)k. |
| N2 | 𝔼K ≥ 2π²(1−c)k + 𝒜/4. |
| N3 | V − 2π²A ≥ 2π²(1−c)k + ‖f_∅⁻‖² + Σ‖f_I⁺‖² + …, i.e. S − 32π²A ≥ 4(8π²Q − P). |
| N4 | 2𝔼‖dρ‖² ≤ 8𝔼‖ζ‖² ≤ 𝔼∫m − 8π²(1−c)k. Transition layers are expensive, so depletion must be diffuse. |
| N5 | 8π²[(c_g⁺)² − A + Σ_i(E_{i,g}⁺)²] ≤ Λ − 8π²(1−c)k. The exceptional classes must be nearly g-anti-self-dual, i.e. the null-period regime. This is consistent with Theorem K-blow-up, where e_i > 0 forbids it. |
| N6 | All 2^k sign fields must nearly agree in amplitude and spin direction, since the terms in (ρ−ρ')² and \|w\|² are part of R. |

**N7, rotation energy.** Use the kinetic split 4K = 4∫|ζ|²/ρ + ∫ρ|∇n|² instead of the Weitzenböck substitution. This gives

8π²Q − P = 𝔼∫ρ|∇n|² − 𝔼∫(8 − 4/ρ)|ζ|² − 𝒜′,

where 𝒜′ is 𝒜 with 8𝔼‖ζ‖² removed. The script's `zeta_weight` entry comes from this substitution. It is an exact alternative to the m-form, not an addition to it; using both would count K twice.

If ρ_ε ≥ ½ everywhere, then 𝔼∫ρ|∇n|² ≥ 8π²(1−c)k + 𝒜′.

**Per-cell values.** With 1 − c ≈ 4.33727×10⁻³ from the Arb enclosure, in s = −4 units:
- deficit per cell ≈ 0.34246;
- 𝔼K ≥ 0.08561 per cell;
- V − 2π²A ≥ 0.08561 per cell;
- 𝔼∫ρ|∇n|² ≳ 0.34246 per cell.

None of these conditions contradicts the existence of a subunit cell. In particular, c₂(S⁺) = ℓ = 0, so nonvanishing spinors are topologically allowed and spinor zeros, which are costly, are not forced. The identity therefore permits the cell, and it fixes what the fields must look like on it.

**Conflict with Step-38 §8.** The note's tube scaling ∫|∇n|² = O(A_E) → 0 is presented as the field countermechanism compatible with subunit perpendicular cells. Rotation energy that vanishes yields a per-cell deficit that vanishes. A fixed subunit cell requires rotation energy bounded below by 8π²(1−c), and this rotation is coupled to depletion through ¼∫ρ|∇n|² ≤ K ≤ ∫(2−ρ).

## 7. Unsupported equations and quantifiers

1. **Same-metric supply needs b₊(X) ≥ 2, i.e. p_g(X) ≥ 1.** Under this condition the blow-up formula gives SW(c + Σε_iE_i) = ±SW_X(K_X) ≠ 0 for every metric. Step-38 §1 states only "minimal general type". If the ramified or ball-quotient hosts of the certified cell have p_g = 0, the sign family depends on the chamber and Sections 3–6 do not apply as written.
2. **The ball-quotient relation χ(X) = A/3 is silent in eq. (`webvar:joint-energies`).** See §3.
3. **The clean bound and its consequences are stated at s = −4.** ρ is not conformally invariant, so the statement for a general metric is P(g) ≥ P(ĝ) ≥ 8π²Q − 4𝔼∫(2 − ρ̂).
4. **"Sharp coefficient four" in note §4 is a pointwise statement.**
5. **Note §8's "both can vanish as A_E → 0".** This is a scaling heuristic with no construction behind it, and N7 contradicts it as a mechanism for a deficit.
6. **The paper's remark that a smooth field branch "would merely recover DP, D²P" is informal.** It is not proved in the section.
7. **Result-level statements of the note.** The paper's simultaneous-field results are explicitly conditioned on b₊(M) ≥ 2, which ensures all ordinary sign classes are supplied without a chamber choice. The paired-field and amplitude results in Step-38 §§3, 4 and 8 are correct for any fixed choice of actual solutions under that same-metric supply hypothesis. Their content equals the averaged single-solution identity. What is missing is the signed kinetic compensation (the paper's eq. `missing-field-inequality`), now sharpened by N7 into a lower bound on rotation energy.