# Step 22 consolidated mathematical status

## Summary of advances

This step made three structural contributions:

1. **Refuted the abstract Nash shortcut** using the 4D Hardy potential V = κ/|x|² as a counterexample. The form bound ∫Vφ² ≤ κ∫|∇φ|² (small perturbation) does NOT imply L²→L∞ ultracontractivity; the heat kernel has singular spatial weights r^{-σ} with σ = 1-√(1-κ) > 0. TTCS independently confirmed via the Milman–Semenov heat kernel estimate.

2. **Identified the two-stage architecture:**
   - **Stage 1 (Critical, hard):** H₂ → H₃ via the single Wang-type Moser step. This uses critical Sobolev absorption with the volume-independent β = C√ε_Li. It is a SINGLE step, not an infinite iteration.
   - **Stage 2 (Subcritical, standard):** H₃ → L∞ via standard Moser with convergent constants. The potential K = aF is in L³(ν) at positive time, which is subcritical (3 > 2 = n/2 in 4D). Form-relative bound zero allows all-exponent iteration.

3. **Formulated the precise critical energy lemma** that reduces the entire remaining PDE problem to a single tensor computation: the evolution inequality for F² under ∂_tg = -2χ²(Ric+g). The absorption mechanism (Cauchy-Schwarz + outer cutoff + Sobolev) is algebraically verified.

## Corrections incorporated

- **Transcription:** a⁻¹/² not a⁻¹ in the quadratic form (from Strategist)
- **Hardy solution:** L²_loc, not global L² (from TTCS)
- **Normalized bound:** A₀⁴H₃ ≤ Cγ³/t, not just H₃ (from TTCS)
- **Conformal-Hardy term:** a⁻²|∇χ|²φ² genuine singularity, screened by natural test function (TTCS)
- **Positive branch (A02):** Codim-1 positive collapse Einstein-compatible in n≥5 via KK; only n=4 obstructed by Bochner

## Remaining task

The entire 4D negative-branch critical Ishida–LeBrun gap theorem reduces to proving the **critical energy lemma** (see `step22_critical_energy_lemma_formulation.md`). This requires:
- The exact Lichnerowicz evolution of |Rm|² under ∂_tg = -2a(Ric+g)
- Identifying the cubic reaction constant
- Controlling the ∇²a ⊗ (Ric+g) normalization source
- The ∇a ⊗ ∇Rm cross terms

Everything downstream (subcritical Moser, defect propagation, metric comparability, Q preservation, exponential chart, projector contradiction) is either standard or already proved.

## Files

- `workspace/notes/step22_inverse_square_correction_and_two_stage_architecture.md` — main note
- `workspace/notes/step22_critical_energy_lemma_formulation.md` — precise lemma statement
- `workspace/scripts/verify_step22_inverse_square_and_subcritical.py` — Hardy exponents
- `workspace/scripts/verify_step22_critical_sobolev_absorption.py` — absorption structure
- `workspace/scripts/verify_step22_absorption_mechanism.py` — complete mechanism check
- `trace/ttcs/results/step22_ttcs01_*` — TTCS verification records
