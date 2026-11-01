# Plan (Step 61): the open-range lower bound — candidate global mechanisms to attack before Step 70

Source: TTCS generator `trace/ttcs/results/step61_ttcs01_generator1_integration.md` (branches sub1, sub2). Ledger: `notes/step58_consolidated_hypothesis_ledger.md`.

Notation: p = P/8π², d = A − C₊ = k − p (Chern–Weil), A = c₁²(X), on M = X#kCP̄², with 0 < k < A/3.

**Unifying target (G): d₊² ≤ B·A·p.**
- (G) is equivalent to p ≥ (√(BA/4 + k) − √(BA/4))² = k²/(BA) + O(k³/A²).
- B = 4 matches the formal common mode P ≈ 2π²k²/A.
- (G) is compatible with the certified cell, which has d/k ≈ 0.0043.
- It is a collective response law, not a tariff.

Three routes:

1. **Hypercube response identity.**
   - The full sign family a_ε = K + Σε_jE_j satisfies 𝔇 = 2^{−k}Σ_ε((a_ε⁺)² − a_ε²) = |K⁻|² + Σ|E_j⁺|² + k ≥ k. This is exact cohomology; the usual convex hull discards it.
   - Needed: an on-shell variation of the SW Weitzenböck completion that produces a trace-free tensor 𝕋_g with 4π²d ≤ |⟨Ric°, 𝕋_g⟩| and ‖𝕋_g‖² ≤ 8π²A (or C π²A).
   - Decisive first test: does a nonzero response term survive the on-shell cancellations? Normalise it against the Burns flux −8π²εR⁺(ζ,ζ) and the kernel log coefficient −4π²|T|². In the Kähler degeneration limit, d → 0 must be respected.
   - Caveat: hypercube SW validity (chambers, b⁺) must be checked.

2. **Yamabe susceptibility.**
   - On unit-volume Yamabe representatives, set x² = ∫s²/(32π²A) and y² = ∫|W⁺|²/((4/3)π²A). Then x ≥ 1 by LeBrun, C₊/A = (x² + 2y²)/3, and d = R_W − E_Y.
   - Target 1: p ≥ γA(x − 1)² when C₊ < A.
   - Target 2, the envelope: 2x + y ≥ 3 (equivalently ∫(s − √6|W⁺|)² ≥ 72π²A; source and hypotheses to be checked, e.g. LeBrun's Weyl estimates with the Gursky-type mixed functional).
   - Together they give d ≤ 2A(x − 1) and d² ≤ (4/γ)Ap, so γ = 1 gives B = 4.
   - Decisive computation: a KE bulk with N kernel-direction Burns cells, followed by Yamabe normalisation (using Ric°_{u²g} = (Ric − 2∇²log u + 2 dlog u ⊗ dlog u)°). Read off the collective rank-one scalar channel and check whether p ≳ A(x − 1)² holds to leading order. The two-cell cross term on a CH quotient is the first case.
   - Caution: Yamabe normalisation lowers P; it adds no "hidden" cost.

3. **Interface/characteristic ledger.** This route prices orbifold absorption and collapse via linking forms, spin^c restrictions and APS corrections on RP³, spherical and Wahl links L(n², nm − 1), including the finite-index lattice enlargement. Exactly one of two outcomes must hold:
   - a residual q_i ≥ θd_i with q_i² ≤ CAp_i; or
   - an actual non-Kähler Einstein core (orbifold, or cusp domain with collapsing complement) realising X#kCP̄² with A > 3k, which would give α = 0.
   EH/Wahl obstruction sizes change only rates; they cannot by themselves give a gap.

Choice for the next serious attempt: Route 2's decisive computation. It is concrete, uses the verified local laws (59.R, cell machinery), and either confirms the 1/(4A) collective coefficient or produces construction data. Route 1's on-shell variation is a short derivation worth attempting in parallel.
