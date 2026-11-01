"""
Step 28 Part 3: Bochner also bounds horizontal twist

Key observation: the same Bochner identity ∫|∇Z|² = ∫Ric(Z,Z) simultaneously
bounds BOTH the fiber bracket (b²/2) AND the horizontal twist (|A|²), since
both appear as non-negative terms in the decomposition of |∇Z|².

For a circle bundle: A_X(fU) = -f/2 · φ(X,·)♯, so
  |A_X Z|² = |Z|²/4 · |φ(X,·)|²

Summing over a horizontal ONB:
  Σ_i |A_{X_i} Z|² = (|Z|²/4) · |φ|²

Since each term in |∇Z|² is non-negative, Bochner gives:
  ⟨|φ|²⟩_{|Z|²} ≤ 4(Λ+δ)

This means the horizontal twist IS bounded in the |Z|²-weighted L² average.
"""
import json, pathlib

out = {
    "title": "Step 28 Bochner bounds horizontal twist",
    "scope": "Observation that Bochner also constrains the horizontal A-tensor"
}

# Decomposition of |∇Z|² for a circle bundle
# For unit vertical U, central Killing Z = fU with |Z|² = f²:
# ∇_{U_a}Z = f·∇^F_{U_a}U + f·T_{U_a}U + (U_a f)U  (for vertical U_a)
# ∇_{X_i}Z = f·A_{X_i}U + f·V(∇_{X_i}U) + (X_i f)U  (for horizontal X_i)

# For a circle fiber (1-dimensional), there's only one vertical direction.
# In the H3 model: U_1=e_1, U_2=e_2 are generating (not central), U_3=e_3 is central.
# The central Killing field is Z = c·e_3 where c=|Z|.
# Then: A_{X_i}(ce_3) = c A_{X_i} e_3 (for horizontal X_i)

# In the H3 model there are NO horizontal directions (the orbit is all of space);
# the "base" is 1-dimensional (the dt direction), and e_0=∂_t is the base.
# So A is trivial (no 2-form on a 1D base), and all twist comes from T.

# For a TRUE circle bundle (fiber = S^1, base = B of dim n-1):
# |A_{X_i}U|² = (1/4)|φ(X_i,·)|²  where φ = connection curvature
# Σ_i |A_{X_i}U|² = (1/4)|φ|²
# Σ_i |A_{X_i}Z|² = f²·(1/4)|φ|² = (|Z|²/4)|φ|²

out["circle_bundle_decomposition"] = {
    "formula": "|∇Z|² = (b²/2)|Z|² + (base+radial terms) + (|φ|²/4)|Z|²",
    "where": "b = fiber bracket, φ = connection curvature (horizontal twist)",
    "bochner_gives": "∫(b²/2)|Z|² + ∫(|φ|²/4)|Z|² ≤ ∫|∇Z|² = ∫Ric(Z,Z) ≤ (Λ+δ)∫|Z|²",
    "fiber_bracket_bound": "⟨b²⟩_{|Z|²} ≤ 2(Λ+δ)",
    "horizontal_twist_bound": "⟨|φ|²⟩_{|Z|²} ≤ 4(Λ+δ)",
    "combined": "Both bounds from the SAME Bochner identity"
}

out["induction_consequence"] = {
    "quotient_Ricci_upper": (
        "Ric_B(X,X) = Ric_M(X,X) + 2|A_X U|² + T-terms. "
        "From two-sided pinching and ⟨|φ|²⟩ ≤ 4(Λ+δ): "
        "⟨Ric_B(X,X)⟩_{|Z|²} ≤ (Λ+δ) + 2(Λ+δ) = 3(Λ+δ)."
    ),
    "remaining_gap": (
        "This is a WEIGHTED AVERAGE bound, not a POINTWISE bound. "
        "The induction needs pointwise Ricci control on the quotient. "
        "Averaging only gives quotient Ricci ≤ 3(Λ+δ) in the weighted L² sense. "
        "Passing to pointwise requires either Moser iteration on the quotient, "
        "or a different mechanism."
    ),
    "partial_progress": (
        "The observation is that the horizontal twist IS controlled by Bochner "
        "(not a separate ingredient), just at the L² level. The gap is average-to-pointwise, "
        "not a missing bound entirely."
    )
}

out["H3_model_check"] = {
    "note": (
        "In the H3 cohomogeneity-one model, the base is 1-dimensional, "
        "so there are no horizontal 2-forms and |A|=0. The entire |∇Z|² "
        "comes from fiber bracket (b²/2) and base variation (2k₃²). "
        "The horizontal twist bound is relevant for circle bundles over "
        "higher-dimensional bases, not for the codimension-one model."
    )
}

path = pathlib.Path('Sessions/S0910A02/workspace/data/step28_bochner_horizontal_twist.json')
path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
print(f"\nSaved to {path}")
