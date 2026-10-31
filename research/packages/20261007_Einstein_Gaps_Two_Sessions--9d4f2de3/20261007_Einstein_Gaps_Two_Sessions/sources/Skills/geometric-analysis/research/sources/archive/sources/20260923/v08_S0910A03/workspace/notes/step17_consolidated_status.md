# Step 17 Consolidated Status

> **Step 18 correction.** This status is superseded by `step18_simultaneous_bootstrap_and_fixed_p_defect.md`. The coupled L² estimate is conditional inside a first-exit bootstrap; `|aRm|<=C/t` is nonintegrable at the initial slice and does not preserve `E`; metric equivalence must be improved through an integrable `p>2` weighted-defect estimate. The BMY topology-uniformity justification was reversed; the corrected minimal-general-type bound uses Noether and `b_+(N)=0`.

## Major advances this step

### 1. Coupled L² energy system CLOSES (unconditional)
The normalized local energies R_α (curvature) and P_α (defect) satisfy:
- dR/dt + cX ≤ Cr^{-2}Σ(R+P) + ε₁Y  
- dP/dt + cY ≤ Cr^{-2}ΣP

The combined energy H = R + κP satisfies dH/dt ≤ Cr^{-2}ΣH, giving
H_*(t) ≤ e^{CNθ} H_*(0). Critical curvature energy persistence follows.

Key mechanism: 4D Sobolev-energy cancellation C_S·||Rm||_{L²} = O(√ε*)
absorbs all dangerous reaction terms (confirmed by A01, TTCS).

### 2. Defect evolution corrected
The cubic term tr(E³) FULLY cancels due to inverse-metric variation.
Correct identity: (∂_t - aΔ)|E|² = -2a|∇E|² + 4aRm(E,E) + 2⟨E,C_a(E)⟩
This is Step 14's identity — consistency verified.

### 3. Maximum principle scope clarified
The defect maximum principle requires ||aRm(g(t))||_∞ as INPUT (not derivable
from initial K₀ alone). But given curvature input (e.g., Li's C/t on plateau
or degenerate ε-regularity on transition), defect preservation and metric
equivalence follow unconditionally — breaking that direction of the circle.

### 4. Volume-independent constants
Under bounded χ/A (automatic for critical Ishida-LeBrun families built from
BMY-bounded surfaces of general type):
- K̄ = Vol⁻¹∫|Rm|² ≤ C(1 + χ/A) is UNIFORMLY bounded
- r_* = (ε/(2K̄))^{1/4} is UNIFORM across the family
- All Li/Moser/Gronwall constants depend only on dimension and K̄

### 5. Precise remaining gap identified
The SINGLE open analytical problem: degenerate ε-regularity under ∂_t - aΔ.
Going from L² energy smallness (R_α ≤ 2ε*) to weighted pointwise curvature
(||aRm|| ≤ C/t). This is Li's Theorem 3.4 on the plateau (a = 1) but
requires a new argument on the transition (0 < a < 1).

## Comparison with peers

### A01 (Step 17)
- Vitali/thinning at Li scale for disjoint supports: CONFIRMED and adopted
- 4r_* plateau (corrected from 3r_*): CONFIRMED
- Sobolev-energy cancellation mechanism: INDEPENDENTLY VERIFIED by our TTCS
- Section 9 continuation theorem: the SAME remaining object

### A02 (Step 17)
- Hitchin-Thorpe kills Bridge 3 for positive branch
- T^k identity gives orbit-space spectral scale
- Toric gap is T²-dependent, not topology-only
- Independent positive-branch work, not directly coupled to our negative-branch

## Evidence files
- Main note: `workspace/notes/step17_normalized_cutoff_flow_theorem.md`
- Verification: `workspace/scripts/verify_normalized_cutoff_maximum_principle.py`
- L² chain: `workspace/scripts/verify_improved_constant.py`
- TTCS: `trace/ttcs/results/step17_ttcs01_*`

## Current chain status (4D negative branch, bounded χ/A)

PROVED: Good-set → Vitali supports → Cutoff flow → L² energy persistence
        → Li on plateau → Defect decay on plateau → L² calibration (7/24)
        → Exponential chart → q⁺ monopole → Joint density → Forbidden germ

CONDITIONAL: Degenerate ε-regularity on transition
             (L² smallness → weighted pointwise ||aRm|| ≤ C/t)

OPEN: Positive branch, n ≥ 5, Lean formalization
