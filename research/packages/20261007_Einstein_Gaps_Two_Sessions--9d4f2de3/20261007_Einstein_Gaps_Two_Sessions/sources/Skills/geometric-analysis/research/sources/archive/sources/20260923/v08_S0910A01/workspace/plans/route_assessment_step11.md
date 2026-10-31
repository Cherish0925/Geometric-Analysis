> **Step 12 repair note.** This Step 11 plan is superseded on the Taub--NUT and Pontryagin interpretation by `workspace/notes/step12_taub_nut_accessibility_and_diffuse_pontryagin.md`, `workspace/scripts/step12_taub_nut_ads_coordinate_curvature.py`, and `workspace/scripts/step12_taub_nut_ads_multiscale_calibration.py`. The corrected computation verifies Ric=-g, W+=0 in the coordinate orientation, exact defect 16 on annuli, full Weyl norm `32 nu^2(4nu^2-3)^2/(3(r+nu)^6)`, divergent mean energy for fixed-radius domains reaching the NUT, and accessibility of smaller annular covers. Counting NUT residues is not the current main route; near-critical Pontryagin density is diffuse: `fint |P-3/4| -> 0`. The next route should study multiscale rank recovery and mixed non-basic connection curvature, not a single F-per-NUT ratio.

# Step 11: Route assessment — Pontryagin obstruction and the decisive NUT test

## Advances in this step

1. **Noether energy bound (Proposition 1, verified):** For ANY minimal complex surface of general type, χ_top(X) ≤ 5A+36 (classical Noether). This gives the global mean curvature-operator energy ≤ 12 + O(1/A) on all near-critical LeBrun sequences. No family restriction needed. Script: `scripts/step11_noether_energy_bound.py`.

2. **Chart-accessible exclusion theorem (Theorem 1, formalized):** Any positive-volume-proportion set of (h,v)-chart-accessible points (buffered normal cover + noncollapse + harmonic chart) is excluded by the Derdziński/projector contradiction. This is independent of Naber-Zhang: NZ is one source of chart accessibility, not its definition. Full statement in `notes/step11_chart_accessibility_and_energy.md`.

3. **Taub-NUT-AdS countermodel (from S0910A03, incorporated):** Controlled maximal ∫|Rm|² at every scale does NOT imply noncollapse of the local universal cover. The Taub-NUT-AdS metric with ν→0 has exact Ric=-g, bounded curvature in the annular band, but the ψ-circle is contractible through the NUT, so the local universal cover doesn't unwrap it. This kills the general regularity route.

4. **Pontryagin obstruction to basic collapse (NEW, from TTCS):** The calibrated Pontryagin density p₁(Λ²₊) = (1/4π²)(2|W⁺|² + s²/24 - |E|²/2) converges to (1/4π²)·3/4 > 0 on the F-small bulk. Since basic Λ²₊ connection collapse (pulled back from dim ≤ 3 base) has zero Pontryagin density, the bulk CANNOT be basic collapse. A positive volume proportion must carry O(1) non-basic mixed Λ²₊ curvature.

5. **TTCS verifier corrections:**
   - The definite-pair mechanism (A03) does NOT exclude flat rank ≥ 2 in general. A closed definite TRIPLE forces parallel forms; a closed definite PAIR leaves residual torsion. The rank-2 exclusion needs additional structural input.
   - The Weitzenböck eigenvalues (1 and 3/2) are verified: R̃|_{Λ²₊} = W⁺ + (s/12)I.
   - The formula ∫p₁(Λ²₊) = 2χ+3τ = A-k is verified.

## Key new insight: the Pontryagin density argument

On the F-small bulk of a near-critical sequence:
- s → -4, |W⁺|² → 1/24, |E| → 0
- The Pontryagin density: 2·(1/24) + (16/24) - 0 = 1/12 + 2/3 = 3/4

This is strictly positive. But if the Λ²₊ connection is basic (pulled back from a ≤3D base), tr(Ω⁺ ∧ Ω⁺) = 0 (no 4-form on ≤3D base).

**Conclusion:** The calibrated good bulk cannot be basic collapse. If most volume is collapsed, the Λ²₊ connection must carry non-trivial mixed (vertical-horizontal) curvature of O(1) magnitude.

For rank-1 circle collapse: fiber integration turns the Pontryagin form into a Chern-Simons-type 3-form on the base. On a CLOSED 3D base, this integrates to zero. Therefore the nonzero total charge ∫p₁ = 2A/3 must come from:

1. NUT/bolt-type rank-drop residues
2. Transition walls between collapse models
3. Significant vertical non-invariance
4. Strong nil/solvable twist

## The decisive test

For any exact Einstein metric with Ric=-g that is NOT locally Kähler with |W⁺|² = 2/3, the calibrated defect F > 0. Since F = 0 requires the calibrated spectrum (-1/6, 1/12, 1/12), and Derdziński forbids this on any Einstein metric with Ric=-g (it would force local Kähler with |W⁺|² = 2/3 ≠ 1/24), EVERY exact Ric=-g Einstein metric has F > 0 at every point.

In particular: the Taub-NUT-AdS metric has F > 0 everywhere. The question is the QUANTITATIVE F-cost of a NUT region and whether O(A) NUT residues can carry the Pontryagin charge 2A/3 while keeping ∫F = o(A).

If each NUT annular region (of volume O(ν)) has F ≥ c₀ > 0 (pointwise, independent of ν), then:
- Total F per NUT: ∫_{NUT} F ≥ c₀ · O(ν)
- To carry charge 2A/3: need O(A/p₁_per_NUT) NUTs
- Total F: ≥ (A/p₁_per_NUT) · c₀ · ν
- This must be o(A), requiring ν → 0 and p₁_per_NUT → ∞ ... 

The computation of the exact F and p₁ density on Taub-NUT-AdS is the most concrete next test. My initial script had incorrect curvature formulas (missing Bianchi IX structure terms), but the qualitative conclusion (F > 0) follows from Derdziński alone.

## What remains open

| Question | Status |
|----------|--------|
| Noether energy bound | **Established** |
| Chart-accessible exclusion | **Established** |
| Pontryagin obstruction to basic collapse | **Established** (TTCS verified) |
| General regularity → noncollapse | **Disproved** (Taub-NUT-AdS) |
| Flat rank ≥ 2 exclusion | **Weakened** (pair ≠ triple) |
| NUT residue F-cost quantification | **Open** (decisive) |
| Circle Chern-Simons residue accounting | **Open** (next key computation) |
| Positive branch noncollapse | **Open** |
| All-dimensional argument | **Not started** |

## Next work (priority order)

1. **Correct Taub-NUT-AdS curvature computation.** Use Wolfram or careful symbolic computation with the full Bianchi IX connection forms to compute |W⁺|², spec(W⁺), and F on the Taub-NUT-AdS annular band. This is the lowest-cost decisive test.

2. **Pontryagin residue at a NUT.** Compute ∫_{NUT neighborhood} p₁(Λ²₊) for the Taub-NUT-AdS model. Is it a fixed topological quantity (like 1) or does it depend on ν?

3. **Chern-Simons accounting on the closed manifold.** For a circle-collapsed region, derive the Chern-Simons residue formula that relates NUT/transition residues to the total charge. This would turn the F-cost calculation into a proof or refutation.

4. **Correct the rank-2 exclusion.** The definite-pair argument needs a third closed form or an additional structural equation. Check whether near-Einstein + biaxial symmetry supplies the needed torsion cancellation.

5. **Positive branch.** The Cheeger-Naber finite-type dichotomy is complementary but doesn't produce Einstein metrics. The noncollapse question remains.

## Files

- `notes/step11_chart_accessibility_and_energy.md` — main note with Theorem 1 and Propositions 1-2
- `scripts/step11_noether_energy_bound.py` — verified Noether bound
- `scripts/step11_bochner_gradient_bound.py` — Bochner analysis (coefficient needs correction)
- `scripts/step11_taub_nut_ads_defect.py` — NUT computation (formulas need correction)
- `trace/ttcs/results/step11_ttcs01_generator1_integration.md` — Pontryagin localization
- `trace/ttcs/results/step11_ttcs01_verifier1_integration.md` — verification of all claims
