#!/usr/bin/env python3
"""
Step 36: Edge-cone CGB accounting and strut smoothing scaling for the collapsed front.

KEY CORRECTION (from strategist): The previous "no-slack" argument conflated
bulk ∫|W|² with the edge-cone defect term. Atiyah-LeBrun's Theorem A shows
that struts enter through a SEPARATE defect correction in the CGB/signature
identity, not through the bulk Weyl integral.

This script:
1. Records the exact Atiyah-LeBrun edge-cone CGB identities
2. Computes strut smoothing energy scaling as function of cone defect, length, transverse scale
3. Settles rod-count = χ for toric 4-manifolds
4. Identifies the honest scaling dichotomy for the α-family

References:
- Atiyah-LeBrun, arXiv:1203.6389, Theorems 2.1, 2.2, Theorem A
- Step 17: μ(A) = (2a_+ + 1)/(a_+(a_+ + 2)), a_+ = (-1+√(9+24A))/2
"""
import json, math, os

out = {"title": "Step 36: Edge-cone accounting and strut smoothing scaling",
       "scope": "Collapsed positive P4+ subroute correction; not a proof of Yau-26."}

# ==========================================================================
# 1. EXACT EDGE-CONE FORMULAS (Atiyah-LeBrun Theorems 2.1, 2.2)
# ==========================================================================

edge_cone_formulas = {
    "source": "Atiyah-LeBrun, arXiv:1203.6389, Theorems 2.1 and 2.2",
    "Theorem_2_1_GB": (
        "chi(M) = (1/8pi^2) int_{M-Sigma} (|W|^2 - 2|Ric^0|^2 + s^2/24) dV "
        "+ (1-beta)*chi(Sigma)"
    ),
    "Theorem_2_2_sig": (
        "tau(M) = (1/12pi^2) int_{M-Sigma} (|W+|^2 - |W-|^2) dV "
        "- (1-beta^2)/3 * [Sigma]^2"
    ),
    "Theorem_A_Einstein": (
        "(2 chi +/- 3 tau)(M) >= (1-beta)(2 chi(Sigma) +/- (1+beta)[Sigma]^2)"
    ),
    "note_smooth": (
        "For smooth metrics (beta=1), defect terms vanish and we recover "
        "the standard Chern-Gauss-Bonnet and Hirzebruch signature theorems."
    ),
    "note_defect_vs_bulk": (
        "CRITICAL: The defect terms (1-beta)*chi(Sigma) and (1-beta^2)/3*[Sigma]^2 "
        "are SEPARATE from the bulk integrals ∫|W|^2 etc. A strut (codim-2 edge-cone "
        "singularity) enters through these defect terms, NOT as additional bulk Weyl energy. "
        "Therefore 'bulk energy saturated => no room for struts' is INCORRECT."
    )
}
out["edge_cone_formulas"] = edge_cone_formulas

# ==========================================================================
# 2. SMOOTH VS LIMIT IDENTITY
# ==========================================================================

# For SMOOTH g_i with Ric = (1+O(δ))g, Vol → 0:
# Standard CGB: 8π²χ = ∫|W|² + ∫(s²/24 - 2|Ric°|²) Vol_g
# Since Ric° = O(δ), s = 4(1+O(δ)):
# ∫|W|² → 8π²χ as Vol → 0 and δ → 0.
# This is bulk curvature of the SMOOTH metric, with no defect terms.

# For a LIMIT metric with edge-cone singularities:
# 8π²χ(M) = ∫_{M-Σ}(|W|² + s²/24) dV_limit + 8π²(1-β)χ(Σ)
# (using Einstein limit with Ric°=0)
# If limit is Ricci-flat (Λ=0) with Vol_limit = 0 (after rescaling → noncompact):
# The identity becomes distributional; formal rod-by-rod.

smooth_vs_limit = {
    "smooth_g_i": {
        "identity": "8π²χ = ∫|W|² + (2/3)(1+O(δ))²Vol",
        "as_Vol_to_0": "∫|W|²_{g_i} → 8π²χ exactly",
        "no_defect_terms": True,
        "explanation": "The smooth g_i have β=1 everywhere, so no edge-cone corrections."
    },
    "limit_with_struts": {
        "identity": "8π²χ = ∫_{M-Σ}|W|²_limit + 8π²(1-β)χ(Σ)",
        "explanation": (
            "If the limit develops struts with cone angle 2πβ along surfaces Σ, "
            "the defect term absorbs some of the topology. The bulk Weyl integral "
            "is REDUCED by the defect contribution, not supplemented."
        ),
        "consequence": (
            "A limit with (1-β)>0 struts has LESS bulk Weyl energy than 8π²χ, "
            "because (1-β)χ(Σ) > 0 moves part of χ into the defect term."
        )
    },
    "strut_smoothing_in_g_i": {
        "mechanism": (
            "The smooth g_i approximate the strut by smoothing the cone deficit "
            "over a transverse scale ε. This smoothing generates curvature "
            "concentrated near the would-be strut."
        ),
        "energy_estimate": "∫|Rm|² ~ (1-β)² × |Σ| / ε²",
        "explanation": (
            "A 2D cone of angle 2πβ smoothed at radius ε has curvature ~ (1-β)/ε "
            "over area ~ ε|Σ|, giving ∫|Rm|² ~ (1-β)²|Σ|/ε²."
        )
    }
}
out["smooth_vs_limit_identity"] = smooth_vs_limit

# ==========================================================================
# 3. STRUT SMOOTHING ENERGY SCALING
# ==========================================================================

def mu(A):
    """Cone-angle ratio from Step 17."""
    if A < 1e-10:
        return 1.0
    a_plus = (-1 + math.sqrt(9 + 24*A)) / 2
    return (2*a_plus + 1) / (a_plus * (a_plus + 2))

def rod_length(A):
    return math.pi / math.sqrt(1 + 2*A)

# For the α-family with edge curvature A:
# Rod length: L = π/√(1+2A) ~ π/√(2A) for large A
# Cone defect: 1-μ(A) ≈ 1 - O(A^{-1/2}) for large A
# Transverse scale of the orbit fiber at a NUT (corner):
#   The fiber is T² with area w² (determinant). Near a corner (nut),
#   both p and q vanish like r (smooth corner condition).
#   So fiber area ~ r², transverse fiber radius ~ r.
#   At the NUT point itself, both circles collapse → a point.
#
# In the RESCALED frame (by √(2A)):
#   Rod length L_scaled → π
#   NUT is at finite distance (corner of polygon)
#   The smoothing scale ε for a would-be strut:
#     - In the original frame: ε ~ collapse fiber size ~ √(pq) ~ w
#     - At a nut: w = 0 (both fibers degenerate)
#     - Away from nut/bolt: w is determined by the PDE
#
# The key question: what is ε/|Σ| at the would-be strut?

strut_scaling_table = []
for A in [1, 5, 10, 50, 100, 500, 1000, 10000]:
    L = rod_length(A)
    mu_A = mu(A)
    cone_defect = 1 - mu_A
    
    # Rescaled quantities
    scale = math.sqrt(2*A)
    L_scaled = scale * L
    
    # Strut length ~ gap between rods = L (same as rod length in periodic model)
    strut_length_original = L
    strut_length_scaled = L_scaled  # ~ π
    
    # Transverse smoothing scale for the strut in the smooth g_i:
    # At the strut (axis between bolts), one circle degenerates (it's a rod end)
    # while the other has size ~ L. The cone deficit is (1-μ).
    # The smoothing must happen over the fiber degeneration scale.
    # 
    # In the original frame: the collapsing T² fiber has sizes ~ L and ~ L
    # at the midpoint of a strut/collar. So ε ~ L.
    # In the rescaled frame: ε_scaled ~ L_scaled ~ π.
    
    eps_original = L  # fiber scale at strut midpoint
    eps_scaled = L_scaled
    
    # Smoothing energy cost in the rescaled frame (per strut):
    # ∫|Rm|² ~ (1-β)² × strut_length / ε² 
    # where β = μ(A) (the cone-angle ratio at the second bolt)
    # In the rescaled frame: (1-μ)² × π / π² = (1-μ)²/π
    
    energy_per_strut_rescaled = cone_defect**2 * strut_length_scaled / eps_scaled**2
    
    # In original frame this would be:
    energy_per_strut_original = cone_defect**2 * strut_length_original / eps_original**2
    # = (1-μ)²/L = (1-μ)² √(1+2A)/π ~ (1-μ)² √(2A)/π
    
    # Compare to bolt energy 8π² (in original frame or rescaled: same)
    ratio_to_bolt = energy_per_strut_original / (8 * math.pi**2) if energy_per_strut_original > 0 else 0
    
    strut_scaling_table.append({
        "A": A,
        "mu": round(mu_A, 8),
        "cone_defect_1_minus_mu": round(cone_defect, 8),
        "rod_length_L": round(L, 8),
        "rescaled_rod_length": round(L_scaled, 8),
        "strut_smoothing_energy_per_strut": round(energy_per_strut_original, 8),
        "ratio_to_bolt_8pi2": round(ratio_to_bolt, 8),
        "explanation": (
            f"Cone defect (1-μ)={cone_defect:.4f}, "
            f"smoothing energy ~ (1-μ)²/L = {energy_per_strut_original:.4f}, "
            f"ratio to 8π² = {ratio_to_bolt:.4f}"
        )
    })

out["strut_smoothing_scaling"] = {
    "formula": "∫|Rm|² ~ (1-β)² × |Σ| / ε², with β=μ(A), |Σ|~L, ε~L",
    "simplified": "(1-μ(A))² / L(A) = (1-μ)² √(1+2A) / π",
    "table": strut_scaling_table,
    "crucial_observation": (
        "For large A: (1-μ)→1, L→0, so (1-μ)²/L → √(2A)/π → ∞. "
        "The strut smoothing energy DIVERGES as A→∞ if ε~L. "
        "But this assumes the transverse smoothing scale ε equals the rod length L. "
        "If instead ε is the COLLAPSE SCALE of the full manifold (fiber volume), "
        "then ε ~ L as well, and the divergence is genuine."
    )
}

# ==========================================================================
# 4. ROD COUNT = χ FOR TORIC 4-MANIFOLDS
# ==========================================================================

# For a closed toric 4-manifold (T² action with isolated fixed points):
# - Fixed points = vertices of Delzant polygon = χ(M) (Poincaré-Hopf for T²)
# - Invariant 2-spheres = edges of polygon = #edges = #vertices = χ(M)
# So #rods = χ = 2 + b₂

rod_count_check = []
for k in [1, 2, 3, 5, 10]:
    chi = 2 + 2*k
    b2 = 2*k
    tau = 0
    rod_count_check.append({
        "family": f"#_{k}(S²×S²)",
        "chi": chi,
        "b2": b2,
        "tau": tau,
        "rod_count_equals_chi": True,
        "edges_of_polygon": chi,
        "vertices_of_polygon": chi,
        "rods_times_8pi2": round(chi * 8 * math.pi**2, 4),
        "CGB_total": round(chi * 8 * math.pi**2, 4),
        "slack": 0.0
    })

out["rod_count_topology"] = {
    "theorem": "For a closed toric T²-manifold M⁴, #(invariant 2-spheres) = #(fixed points) = χ(M)",
    "proof_sketch": (
        "Delzant polygon has #edges = #vertices. Each vertex is a T²-fixed point, "
        "each edge is an invariant S². By Poincaré-Hopf for the T²-action, "
        "#(fixed points) = χ(M)."
    ),
    "examples": rod_count_check,
    "consequence": (
        "If each rod consumes EXACTLY 8π² of bulk Weyl energy, then the total "
        "8π²χ is saturated by bolts alone. However, this bulk saturation says "
        "NOTHING about the edge-cone defect term, which is additive in the "
        "edge-cone CGB formula. See edge_cone_formulas."
    )
}

# ==========================================================================
# 5. THE HONEST DICHOTOMY
# ==========================================================================

# The smooth g_i satisfy: 8π²χ = ∫|W|² + (2/3)(1+O(δ))²Vol_i
# As Vol→0: ∫|W|² → 8π²χ
# 
# Question: where does this curvature sit in the manifold?
# 
# Each bolt region contributes ~8π² (Step 34 computation).
# If #bolts = χ, the bolt contributions saturate the budget.
# But if there are struts between bolts, the smooth metric must also
# allocate curvature for strut smoothing.
# 
# RESOLUTION OF THE APPARENT CONTRADICTION:
# The bolt energy 8π² was computed INCLUDING the collar/transition region
# around the bolt. The strut, if present, is in the COLLAR between bolts.
# So the bolt energy 8π² already INCLUDES whatever strut smoothing energy
# the collar carries. The question is whether the collar can simultaneously
# carry the bolt curvature AND smooth the strut within 8π².
#
# If the strut smoothing energy (1-μ)²/L diverges as A→∞, while the bolt
# energy stays at 8π², then for large enough A the strut smoothing must
# OVERFLOW the bolt's collar budget. This would give a topology-uniform
# energy contradiction.
#
# HOWEVER: the 8π² bolt energy was computed by integrating |Rm|² over the
# bolt region with crude bounds. The actual Weyl energy ∫|W|² per bolt
# might differ from 8π² by an amount that covers or fails to cover the strut.

# Let's compute more carefully:
# In the formal SdS model with edge curvature A:
# - Bolt S² has K_Σ = 1+2A, area ≈ 4π/(1+2A)
# - Collar has transverse width ~ L/2π ~ 1/(2√A)
# - At the bolt: |Rm| ~ 2A, Rm is ~ Weyl + Ricci/scalar
# - For Einstein (Ric=g): |Ric| ~ 1, |W| ~ |Rm| - Ricci_part
# - Schematically: |Rm|² = |W|² + (1/2)|Ric°|² + (1/24)s² in 4D
# - For Ric=g: |Ric°|=0, s=4, so |Rm|² = |W|² + 2/3
# - ∫(|W|² + 2/3)dV = 8π²χ ... this is just CGB again
#
# The bolt |Rm| ~ 2A includes BOTH Weyl and scalar curvature.
# Since s=4(1+O(δ)), the scalar part contributes 2/3 per volume,
# and Vol→0. So asymptotically ∫|Rm|² ≈ ∫|W|² + (2/3)Vol ≈ 8π²χ.
# And per bolt: ∫|Rm|²_bolt ≈ ∫|W|²_bolt ≈ 8π².

# The strut smoothing cost (1-μ)²/L grows like √A.
# The bolt Weyl energy is 8π² (approximately constant).
# So for A >> 1: strut smoothing >> bolt Weyl.
#
# But wait: the strut smoothing cost (1-μ)²/L is ∫|Rm|² from the smoothing,
# which goes into the SAME bulk integral ∫|Rm|² that is bounded by 8π²χ.
# So if each strut costs >> 8π², and there are χ struts, the total would be
# >> 8π²χ, contradicting the smooth CGB bound.
#
# The catch: is the strut energy ADDITIONAL to the bolt energy, or is it
# the SAME curvature? In the smooth metric, a "bolt + its collar" region
# contains the curvature that becomes both the bolt (in the limit) and the
# strut smoothing. So the 8π² per bolt must COVER the strut smoothing.
# If strut smoothing costs >> 8π², the construction is impossible.

# For large A: strut cost ~ (1-μ)²√(2A)/π ~ √(2A)/π (since μ→0)
# This exceeds 8π² when √(2A)/π > 8π², i.e., A > 32π⁶/2 ≈ 15,000
# (crude; the constant in the ∫|Rm|² estimate matters)

A_threshold_crude = (8 * math.pi**2 * math.pi)**2 / 2  # ~ (8π³)²/2
# Actually: strut cost = (1-μ)²/L. For A>>1: (1-μ)≈1, L≈π/√(2A).
# So strut cost ≈ √(2A)/π. This exceeds 8π² when A > 32π⁶ ≈ 30,500.

threshold_values = []
for A in [100, 1000, 5000, 10000, 20000, 50000, 100000]:
    mu_A = mu(A)
    L_A = rod_length(A)
    strut_cost = (1 - mu_A)**2 / L_A
    bolt_energy = 8 * math.pi**2
    threshold_values.append({
        "A": A,
        "strut_cost_per_strut": round(strut_cost, 4),
        "bolt_energy_8pi2": round(bolt_energy, 4),
        "ratio_strut_to_bolt": round(strut_cost / bolt_energy, 4),
        "strut_exceeds_bolt": strut_cost > bolt_energy
    })

out["honest_dichotomy"] = {
    "reframing": (
        "Struts are limit objects; the smooth g_i have none. A strut lives on the axis "
        "between bolts, i.e. in the collar. So the strut question and the 'no neck energy "
        "loss' hypothesis are THE SAME OBJECT. The smooth g_i must smooth any would-be "
        "strut within the same 8π²χ bulk budget that the bolts consume."
    ),
    "strut_smoothing_formula": (
        "Smoothing a codim-2 deficit 2π(1-β) at transverse scale ε costs "
        "∫|Rm|² ~ (1-β)² |Σ| / ε². If ε is comparable to |Σ|: O(1). "
        "If ε << |Σ|: divergent."
    ),
    "alpha_family_scaling": (
        "In the α-family: both ε and |Σ| scale as L = π/√(1+2A). "
        "So the RATIO ε/|Σ| stays O(1), but the strut cost is (1-μ)²/L ~ √(2A)/π, "
        "which GROWS without bound. This is because the cone defect (1-μ) approaches 1 "
        "while the strut length L shrinks."
    ),
    "threshold_table": threshold_values,
    "conditional_conclusion_obstruction": (
        "IF the smooth g_i must allocate curvature to smooth a would-be strut in the collar, "
        "AND if the strut smoothing cost grows like √A while the bolt energy is bounded, "
        "THEN for A large enough the total curvature budget 8π²χ is exceeded, giving a "
        "topology-uniform energy contradiction (obstruction to the collapse)."
    ),
    "conditional_conclusion_BREAK": (
        "IF a strut-free periodic Ricci-flat toric Weyl solution exists "
        "(no Israel-Khan conical deficit between bolts), then the smooth g_i can approach "
        "this limit without any strut smoothing cost, and the bolt energy 8π² suffices. "
        "This would be a genuine BREAK candidate for the positive collapsed branch."
    ),
    "what_decides": (
        "The Israel-Khan strut force balance: in the 4D static vacuum (Weyl) problem with "
        "periodic alternating rod labels, is a conical deficit on the axis between bolts "
        "FORCED by the field equations, or can the regularity conditions at adjacent bolts "
        "be simultaneously satisfied? This is a concrete PDE/ODE question in the Weyl "
        "formalism, not a topological statement."
    ),
    "strategist_correction": (
        "The Step-35 'no-slack' argument incorrectly concluded that bulk energy saturation "
        "leaves no room for struts. In fact, struts enter the edge-cone CGB through a "
        "SEPARATE defect term (Atiyah-LeBrun), not through the bulk ∫|W|². The correct "
        "lever is the SMOOTHING COST of the strut within the smooth g_i, which competes "
        "with the bolt energy for the same total bulk budget."
    )
}

# ==========================================================================
# 6. CORRECTED NONCOLLAPSED ROUTE A SUMMARY
# ==========================================================================

out["noncollapsed_route_A_correction"] = {
    "Step_34_error": (
        "Step 34 introduced δ log(1/t) → 0 as a theorem hypothesis. "
        "This is an artifact of reading the growing H₂ coefficient by pairing "
        "against the r^{-4} test field through a long neck."
    ),
    "Step_35_correction": (
        "In the rescaled bubble frame ĝ = t^{-2}g, the Ricci defect has size "
        "t²δ relative to the fixed EH scale. Over a fixed annulus ρ ∈ [1,R], "
        "the relative Wronskian nonconservation is O(δ log R) + O(1/R). "
        "Fix R large, let δ_i → 0, then R → ∞. No coupling between δ and t survives."
    ),
    "real_missing_input": (
        "Existence of the second-order blow-up k = lim(ĝ_i - g_EH)/t_i² with "
        "quadratic growth, solving DRic_EH(k) = Λ g_EH + O(δ_i), and matching "
        "of k's quadratic part to the orbifold 2-jet. "
        "C^{1,α} ∩ W^{2,q} convergence does not transmit a 2-jet for non-Einstein g_i."
    ),
    "CZ_spike_compatibility": (
        "The CZ opposite-warp spike (Step 11) does NOT refute this: "
        "the spike has unbounded pointwise curvature but good harmonic-coordinate "
        "C^{1,α} control. Harmonic-radius epsilon regularity is about coordinate "
        "regularity, not pointwise curvature."
    )
}

# Save
outpath = os.path.join("Sessions", "S0910A02", "workspace", "data",
                         "step36_edge_cone_strut_scaling.json")
os.makedirs(os.path.dirname(outpath), exist_ok=True)
with open(outpath, "w") as f:
    json.dump(out, f, indent=2)

print(f"Saved to {outpath}")
print()
print("=== EDGE-CONE DEFECT VS BULK ===")
print(f"  Atiyah-LeBrun Theorem A: struts enter as SEPARATE defect terms")
print(f"  NOT through bulk ∫|W|²")
print()
print("=== STRUT SMOOTHING SCALING ===")
for row in strut_scaling_table[-4:]:
    print(f"  A={row['A']:>6}: (1-μ)={row['cone_defect_1_minus_mu']:.4f}, "
          f"strut cost={(1-row['mu'])**2/rod_length(row['A']):.2f}, "
          f"ratio to 8π²={row['ratio_to_bolt_8pi2']:.4f}")
print()
print("=== THRESHOLD TABLE ===")
for row in threshold_values:
    flag = "EXCEEDS" if row["strut_exceeds_bolt"] else "within"
    print(f"  A={row['A']:>6}: strut_cost={row['strut_cost_per_strut']:.1f}, "
          f"bolt=8π²≈{row['bolt_energy_8pi2']:.1f}, {flag}")
print()
print("=== ROD COUNT ===")
print(f"  For toric M⁴: #rods = χ(M) = 2 + b₂")
print()
print("=== DICHOTOMY ===")
print("  OBSTRUCTION if: Israel-Khan struts are forced and smoothing diverges")
print("  BREAK if: strut-free periodic Weyl solution exists")
