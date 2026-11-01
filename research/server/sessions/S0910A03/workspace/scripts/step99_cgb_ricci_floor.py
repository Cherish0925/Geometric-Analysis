"""Step 99: Verify the closed-chi=0 Chern-Gauss-Bonnet Ricci pinching bound.

STEP 100 CORRECTION: this is the older Step 2/64 closed-manifold bound. It does
not apply to a connector with boundary or to a pure-hyperbolic-piece graph
completion with positive Euler characteristic. It does not change the Yau-26
counterexample target: the normalized defect must still tend to zero. The
former connector-absorption and sharpness interpretations below are retained
only as superseded provenance; use step100_relative_cgb_scaling.py and
notes/step100_relative_cgb_graph_budget.md for the correct relative identity.


On a closed oriented 4-manifold M with χ(M)=0:
  ∫|Ric°|² = 2∫|W|² + (1/12)∫s²

Since |W|² ≥ 0, ∫|Ric°|² ≥ (1/12)∫s².

If all Ricci eigenvalues are in [Λ-δ, Λ+δ]:
  |Ric°|² ≤ 4δ²  (optimal for k=2 split)
  |s| ≥ 4(|Λ|-δ)  when δ < |Λ|

So: 4δ² Vol ≥ (4/3)(|Λ|-δ)² Vol
    δ ≥ |Λ|/(1+√3)

For Λ = -3: δ ≥ 3/(1+√3) ≈ 1.098.

This applies to any closed 4-manifold with χ=0, including free-T² manifolds
(graph manifolds, surface bundles with χ=0, etc.).

IMPORTANT: This bounds the defect on the CLOSED manifold, not on an open
connector. We must verify how this constrains the actual construction.
"""
import json, math
from pathlib import Path
import numpy as np

SESSION = Path(__file__).resolve().parents[2]


def cgb_floor(Lambda, n_dim=4):
    """CGB-based Ricci pinching floor on χ=0 manifolds in dimension 4."""
    # δ ≥ |Λ|/(1+√3) from |Ric°|² ≤ 4δ², ∫s² ≥ 16(|Λ|-δ)² Vol
    return abs(Lambda) / (1.0 + math.sqrt(3.0))


def verify_eigenvalue_bounds():
    """Verify the optimal |Ric°|² bound for eigenvalues in [Λ-δ, Λ+δ]."""
    Lambda, delta = -3.0, 1.5
    
    results = []
    for k in range(5):  # k eigenvalues at Λ+δ, rest at Λ-δ
        eigs = np.array([Lambda + delta] * k + [Lambda - delta] * (4-k))
        s = np.sum(eigs)
        ric_tracefree = eigs - s/4
        ric0_sq = np.sum(ric_tracefree**2)
        results.append({
            "k": k,
            "eigenvalues": eigs.tolist(),
            "s": float(s),
            "|Ric°|²": float(ric0_sq),
            "4δ²": 4*delta**2,
        })
    return results


def cgb_identity_check():
    """Check equality of two separate algebraic estimates (not geometric attainability)."""
    Lambda = -3.0
    delta_floor = cgb_floor(Lambda)
    
    # At the critical delta, check the identity
    delta = delta_floor
    Ric0_sq = 4 * delta**2
    s_sq = (4 * (abs(Lambda) - delta))**2
    lhs = Ric0_sq
    rhs = s_sq / 12  # from |W|²=0 case
    
    return {
        "Lambda": Lambda,
        "delta_floor": delta_floor,
        "delta_floor_exact": f"3/(1+sqrt(3)) = {3/(1+math.sqrt(3)):.10f}",
        "delta_floor_rationalized": f"3(sqrt(3)-1)/2 = {3*(math.sqrt(3)-1)/2:.10f}",
        "|Ric°|²_at_floor": lhs,
        "s²/12_at_floor": rhs,
        "identity_ratio": lhs/rhs if rhs > 0 else None,
        "algebraic_bound_equality": abs(lhs - rhs) < 1e-10,
        "geometric_sharpness_not_established": True,
    }


def implication_for_yau26():
    """Compute what the CGB floor means for Yau 26 intervals."""
    Lambda = -3.0
    delta_floor = cgb_floor(Lambda)
    
    # If Ric has eigenvalues in [c, C] with c < C < 0:
    # Λ = (c+C)/2, δ = (C-c)/2
    # δ ≥ |Λ|/(1+√3)
    # (C-c)/2 ≥ -(c+C)/(2(1+√3))
    # (C-c)(1+√3) ≥ -(c+C) = |c|-|C|
    # C(1+√3) - c(1+√3) ≥ -c - C
    # C(2+√3) ≥ c√3
    # C/c ≤ √3/(2+√3)
    
    ratio = math.sqrt(3) / (2 + math.sqrt(3))
    
    # Check with specific values
    examples = []
    for c in [-4, -3, -2, -1]:
        C_min = c * ratio
        delta_min_direct = cgb_floor((c + C_min)/2)
        examples.append({
            "c": c,
            "C_min": C_min,
            "ratio_C_c": ratio,
            "Lambda": (c + C_min)/2,
            "delta": (C_min - c)/2,
            "CGB_floor_check": delta_min_direct,
        })
    
    # Positive Ricci case: 0 < c < C
    # δ ≥ Λ/(1+√3), Λ = (c+C)/2
    # (C-c)/2 ≥ (c+C)/(2(1+√3))
    # (C-c)(1+√3) ≥ c+C
    # C(√3) - c(√3) ≥ c+C ... wait:
    # C + C√3 - c - c√3 ≥ c + C
    # C√3 - c - c√3 ≥ c
    # C√3 ≥ 2c + c√3 = c(2+√3)
    # C/c ≥ (2+√3)/√3 = 1/ratio
    
    pos_ratio = (2 + math.sqrt(3)) / math.sqrt(3)
    
    return {
        "negative_branch": {
            "min_ratio_C_over_c": ratio,
            "explanation": "On χ=0 closed 4-manifold with c < C < 0: C/c ≤ √3/(2+√3)",
            "normalized_Λ_minus3": {
                "delta_floor": delta_floor,
                "c_n": -3 - delta_floor,
                "C_n": -3 + delta_floor,
            },
        },
        "positive_branch": {
            "min_ratio_C_over_c": pos_ratio,
            "explanation": "On χ=0 closed 4-manifold with 0 < c < C: C/c ≥ (2+√3)/√3",
        },
        "interval_crossing_zero": {
            "explanation": "If c < 0 < C, the bound δ ≥ |Λ|/(1+√3) with Λ=(c+C)/2 near 0 "
                          "gives a weak constraint. But constant rescaling of metrics does not "
                          "change Ric, so any manifold admits metrics with arbitrarily narrow "
                          "positive-to-negative intervals centered at 0.",
        },
        "examples": examples,
    }


def assess_connector_vs_closed():
    """Determine whether the CGB floor applies to the connector or whole manifold."""
    # The connector is an open cylinder, not a closed manifold.
    # The CGB identity is for closed manifolds.
    # On the closed manifold, the integral averages over:
    #   - connector region (volume ~ L × cross-section)
    #   - cusp regions (volume ~ e^{3R} × cross-section)
    
    # For a two-ended connector of length 2R with cusps:
    # ∫_M s² = ∫_connector s² + ∫_cusps s²
    # On cusps: s ≈ -12, so s² ≈ 144
    # ∫_cusps s² ≈ 144 Vol(cusps)
    
    # ∫_M |Ric°|² = ∫_connector |Ric°|² + ∫_cusps |Ric°|²
    # On cusps: |Ric°| ≈ 0, so ∫_cusps |Ric°|² ≈ 0
    
    # CGB: ∫_connector |Ric°|² ≈ 2∫_M |W|² + (1/12)(144 Vol(cusps) + ∫_conn s²)
    # ≥ 12 Vol(cusps) + (1/12)∫_conn s²
    
    # If connector has δ_sup = max operator norm:
    # ∫_connector |Ric°|² ≤ 4δ² Vol(connector)
    # ∫_connector s² ≥ (12-4δ)² Vol(connector) for s in [-12-4δ,-12+4δ]
    
    # So: 4δ² Vol(conn) ≥ 12 Vol(cusps) + (4/3)(3-δ)² Vol(conn)
    # 4δ² - (4/3)(3-δ)² ≥ 12 Vol(cusps)/Vol(conn)
    
    # The LHS is (4/3)(3δ²-(3-δ)²) = (4/3)(3δ²-9+6δ-δ²) = (4/3)(2δ²+6δ-9)
    # This is positive iff 2δ²+6δ-9>0, i.e., δ > (-6+√(36+72))/4 = (-6+√108)/4 ≈ 1.098/√(3/4)
    # Actually: 2δ²+6δ-9=0 gives δ = (-6+√(36+72))/4 = (-6+6√3)/4 = 3(√3-1)/2 ≈ 1.098
    # This is EXACTLY the CGB floor!
    
    delta_floor = 3*(math.sqrt(3)-1)/2
    lhs_at_floor = 4/3 * (2*delta_floor**2 + 6*delta_floor - 9)
    
    return {
        "key_identity": "4δ² - (4/3)(3-δ)² = (4/3)(2δ²+6δ-9)",
        "delta_floor_for_connector_to_absorb_cusps": delta_floor,
        "lhs_at_floor": lhs_at_floor,  # should be ≈ 0
        "interpretation_SUPERSEDED_STEP100": (
            "Invalid for the intended graph gluing: it assumes the completed closed manifold has chi=0 "
            "and deletes the positive Euler contribution of its real-hyperbolic pieces. A connector has "
            "boundary and local free-T2 symmetry does not force global chi=0. Equality of the separate "
            "eigenvalue estimates also does not establish geometric sharpness. Use the relative identity "
            "in step100_relative_cgb_scaling.py instead."
        ),
    }


def main():
    print("=" * 70)
    print("CHERN-GAUSS-BONNET RICCI PINCHING OBSTRUCTION")
    print("=" * 70)
    
    # Eigenvalue bounds
    print("\n=== Eigenvalue bounds verification ===")
    ev = verify_eigenvalue_bounds()
    for r in ev:
        print(f"  k={r['k']}: |Ric°|²={r['|Ric°|²']:.4f}, 4δ²={r['4δ²']:.4f}")
    
    # CGB identity check
    print("\n=== CGB floor at Λ=-3 ===")
    check = cgb_identity_check()
    print(f"  δ_floor = {check['delta_floor']:.10f}")
    print(f"  Exact: {check['delta_floor_exact']}")
    print(f"  Separate algebraic bounds meet: {check['algebraic_bound_equality']} (no realizing metric or sharpness proved)")
    
    # Yau 26 implications
    print("\n=== Implications for Yau 26 ===")
    impl = implication_for_yau26()
    print(f"  Negative branch ratio C/c: ≤ {impl['negative_branch']['min_ratio_C_over_c']:.6f}")
    print(f"  Positive branch ratio C/c: ≥ {impl['positive_branch']['min_ratio_C_over_c']:.6f}")
    nb = impl['negative_branch']['normalized_Λ_minus3']
    print(f"  At Λ=-3: c₄ ≤ {nb['c_n']:.4f}, C₄ ≥ {nb['C_n']:.4f}")
    
    # Connector vs closed analysis
    print("\n=== Connector absorption analysis ===")
    ca = assess_connector_vs_closed()
    print(f"  Floor for connector to absorb cusp s²: {ca['delta_floor_for_connector_to_absorb_cusps']:.6f}")
    print(f"  LHS at floor (should be ≈ 0): {ca['lhs_at_floor']:.2e}")
    
    # The Weyl-inclusive bound
    print("\n=== Weyl-inclusive bound ===")
    # ∫|Ric°|² = 2∫|W|² + (1/12)∫s²
    # If we can bound ∫|W|² from below, the bound improves.
    # For near-hyperbolic: W ≈ (W_hyp), |W|² = 2 (since scalar flat conformal)
    # Actually, for Ric = -3g: s = -12, Rm = -g∧g/2, W = Rm - Ric∧g/(n-2) + R∧g∧g/...
    # In 4D for Einstein: |W|² = |Rm|² - 2|Ric°|² + s²/24 = 2|Rm| for Ric=-3g
    # Wait: for Ric=-3g (Einstein), |Ric°|=0 and |W|² = |Rm|² - s²/24
    # With Rm = (s/12)(g∧g) + W for Einstein, |Rm|² = s²/24 + |W|²
    # So |W|² = |Rm|² - s²/24. For constant sectional curvature -1:
    # |Rm|² = 4·6/4 = ... actually this needs careful computation.
    
    print("  (Weyl contribution is nonneg but volume-dependent; not a universal improvement)")
    
    out = {
        "eigenvalue_bounds": ev,
        "cgb_floor_check": check,
        "yau26_implications": impl,
        "connector_analysis": ca,
    }
    path = SESSION / "workspace/data/step99_cgb_obstruction.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
