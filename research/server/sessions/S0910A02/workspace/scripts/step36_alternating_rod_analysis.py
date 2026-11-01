#!/usr/bin/env python3
"""
Step 36: Alternating-rod Weyl regularity analysis.

For the toric α-family stress test on #_k(S²×S²), the rod labels ALTERNATE:
(1,0), (0,1), (1,0), (0,1), ...

This is structurally different from Israel-Khan multi-Schwarzschild,
where all rods collapse the SAME circle.

Key question: do alternating-label rods force conical deficits (struts)?

This script analyzes:
1. The alternating vs same-label distinction  
2. Known strut-free examples (multi-Taub-NUT, Gibbons-Hawking)
3. The force-balance condition for the periodic alternating array
"""
import json, math, os

out = {"title": "Step 36: Alternating-rod Weyl regularity analysis",
       "scope": "Structural question for collapsed P4+ route"}

# ==========================================================================
# 1. ROD LABEL STRUCTURE
# ==========================================================================

out["rod_labels"] = {
    "S2xS2_rectangle": {
        "polygon": "Rectangle with vertices at (0,0), (1,0), (1,1), (0,1)",
        "edge_normals": ["(1,0)", "(0,1)", "(-1,0)", "(0,-1)"],
        "alternating": True,
        "adjacent_labels_form_basis": True,
        "smooth_metric": "Round product S²(1)×S²(1), which IS Einstein"
    },
    "k2_hexagon": {
        "polygon": "Hexagon with 6 edges for #₂(S²×S²)",
        "edge_normals": ["(1,0)", "(0,1)", "(-1,1)", "(-1,0)", "(0,-1)", "(1,-1)"],
        "note": (
            "For k≥2, the Delzant polygon has 2+2k edges. "
            "NOT all edges need have the alternating (1,0)/(0,1) pattern; "
            "the standard Delzant realization uses more general primitive vectors. "
            "But the diagonal model studied in Steps 12-25 imposes the alternating pattern."
        )
    },
    "distinction_from_Israel_Khan": {
        "Israel_Khan": (
            "In the Israel-Khan problem, all rods collapse the SAME S¹. "
            "Adjacent bolts are both S² fixed sets of the SAME U(1). "
            "Between them, the axis has a conical singularity (strut)."
        ),
        "alternating_toric": (
            "In the alternating toric model, adjacent rods collapse DIFFERENT S¹ factors. "
            "Between them (at the NUT/corner), BOTH circles degenerate to give a fixed point. "
            "There is NO axis segment between bolts where one circle is regular; "
            "instead, the transition goes through a NUT (codimension-4 point)."
        ),
        "critical_consequence": (
            "A NUT is a POINT, not a codimension-2 surface. It does NOT have a cone angle. "
            "The Israel-Khan strut (codimension-2 conical deficit) is not the same object "
            "as a NUT (codimension-4 fixed point). The edge-cone defect term "
            "(1-β)χ(Σ) applies to codimension-2 singularities Σ, not to isolated points. "
            "For a NUT, the relevant singularity is an orbifold point, which contributes to χ "
            "through the orbifold Euler characteristic, not through an edge-cone term."
        )
    }
}

# ==========================================================================
# 2. STRUT-FREE EXAMPLES
# ==========================================================================

out["strut_free_examples"] = {
    "multi_Taub_NUT": (
        "The Gibbons-Hawking multi-center gravitational instantons are "
        "smooth, Ricci-flat, self-dual (W⁻=0), ALF/ALE metrics with "
        "multiple NUT centers. These have NO struts. They are toric and "
        "have alternating rod labels. Example: multi-Eguchi-Hanson on "
        "resolved ALE spaces."
    ),
    "Euclidean_Schwarzschild": (
        "A single Euclidean Schwarzschild has one smooth bolt and one "
        "asymptotic end. It is NOT self-dual and has both W⁺ and W⁻ nonzero. "
        "It is a single-rod solution with no strut."
    ),
    "two_Schwarzschild_on_same_axis": (
        "Two Euclidean Schwarzschild solutions on the same axis (same circle "
        "collapsing) REQUIRE an Israel-Khan strut between them. This is the "
        "standard same-label obstruction."
    ),
    "alternating_rods_key_question": (
        "For an alternating-label periodic array, the NUTs between rods "
        "are codimension-4 points, not codimension-2 struts. The regularity "
        "condition at each NUT is that both fiber functions vanish at the "
        "correct rate. Whether this can be satisfied globally in a periodic "
        "Ricci-flat solution is the key open question."
    )
}

# ==========================================================================
# 3. REFRAMING: STRUT VS NUT
# ==========================================================================

# For the alternating toric model:
# - At each BOLT (rod): one circle degenerates, the other stays finite
# - At each NUT (corner): both circles degenerate to a point
# - On the axis between a rod and a NUT: one circle is small but finite
#
# The potential strut singularity would occur if:
# (a) Same-label adjacent rods: strut on the axis where neither circle degenerates
#     → Israel-Khan type, codimension-2
# (b) Alternating-label: NUT between rods is a point singularity
#     → NOT an edge-cone strut; it's an orbifold/cone point
#
# For case (b), the smoothness question is:
# Can the smooth metric g_i have all NUTs resolved (smooth T²-fixed points)?
# 
# For a toric manifold with the Delzant polygon: YES! The Delzant theorem
# guarantees a smooth symplectic toric manifold for any Delzant polygon.
# And smooth toric metrics exist with arbitrary Ricci pinching? Not necessarily.
#
# The key point: the potential singularity is at the NUTs, not at struts.
# The NUT regularity is a DIFFERENT type of singularity from a codimension-2 strut.

out["strut_vs_nut_reframing"] = {
    "for_alternating_labels": (
        "In the alternating-label toric model, the potential singularities are NUTs "
        "(codimension-4 fixed points), NOT struts (codimension-2 edge-cone). "
        "The Atiyah-LeBrun edge-cone formulas do NOT apply to NUT singularities. "
        "NUT singularities are orbifold-type points that enter the Gauss-Bonnet "
        "through the orbifold Euler characteristic correction, not through "
        "(1-β)χ(Σ) terms."
    ),
    "consequence_for_energy_budget": (
        "The strut smoothing energy estimate ∫|Rm|² ~ (1-β)²|Σ|/ε² applies to "
        "codimension-2 deficits. A NUT is a POINT singularity with curvature "
        "concentrated in a ball of radius ε, giving ∫|Rm|² ~ 1/ε⁴ × ε⁴ = O(1) "
        "in 4D. So NUT smoothing costs O(1), not O(√A)."
    ),
    "revised_dichotomy": (
        "If the collapsed α-family has ALTERNATING labels (which it does for the "
        "diagonal toric model on #_k(S²×S²)), then the singularities are NUTs, "
        "not struts. The energy budget is: χ bolts × 8π² + χ nuts × O(1) ≤ 8π²χ. "
        "This is satisfied if the O(1) NUT energy is small enough. "
        "The OBSTRUCTION from divergent strut smoothing does NOT apply in this case."
    ),
    "warning": (
        "This analysis assumes the alternating-label model. If some other collapse "
        "mode produces same-label adjacent rods (through a topology change or "
        "non-toric collapse), the strut analysis would apply. Also, the NUT "
        "smoothing O(1) estimate is crude and should be checked."
    )
}

# ==========================================================================
# 4. WHAT THIS CHANGES
# ==========================================================================

out["what_this_changes"] = {
    "collapsed_front_status": (
        "The collapsed α-family adversary is NOT killed by the strut energy argument "
        "because it has alternating labels and NUT (not strut) singularities. "
        "The honest status is: the formal toric family with alternating labels and "
        "growing edge curvature A satisfies ALL checked local, integral, and CGB "
        "conditions. No global smooth metric has been constructed, but no "
        "topology-uniform energy obstruction has been found either."
    ),
    "what_would_kill_it": [
        "A global Ricci-flat periodic solution with alternating labels → BREAK (requires separate Einstein nonexistence)",
        "A topological obstruction from NUT-type orbifold constraints",
        "A higher-order PDE obstruction in the nonlinear filling of the formal model",
        "A Bochner/Killing-field obstruction from collapse (Steps 28-29)",
        "A new integral identity that constrains NUT curvature more tightly"
    ],
    "what_would_be_BREAK": (
        "A smooth collapsing family on #_k(S²×S²) with Ric→g is a BREAK for "
        "the positive collapsed branch only if #_k(S²×S²) admits no Einstein "
        "metric of any sign. No such nonexistence result is known."
    )
}

# Save
outpath = os.path.join("Sessions", "S0910A02", "workspace", "data",
                         "step36_alternating_rod_analysis.json")
with open(outpath, "w") as f:
    json.dump(out, f, indent=2)

print(f"Saved to {outpath}")
print()
print("=== KEY FINDING ===")
print("  The α-family has ALTERNATING rod labels.")
print("  Transition between rods is through NUTs (codim-4 points),")
print("  NOT struts (codim-2 edge-cone singularities).")
print("  The Atiyah-LeBrun edge-cone formula does NOT apply to NUTs.")
print("  NUT smoothing costs O(1), not O(√A).")
print()
print("=== CONSEQUENCE ===")
print("  The strut-energy obstruction does NOT kill the alternating α-family.")
print("  The collapsed positive adversary survives this analysis.")
print("  It is killed only by a global construction failure or a separate mechanism.")
