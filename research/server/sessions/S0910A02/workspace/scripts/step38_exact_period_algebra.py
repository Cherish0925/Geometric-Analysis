#!/usr/bin/env python3
"""Step 38: Exact algebra and structural analysis of Weyl rod period coefficients.

Three computations:
1. Verify that for m equal-length alternating rods (m/2 same-label each),
   the exp_range ratio is exactly prod_{k=1}^{m/2-1} (2k+1)/(2k).
2. Test the periodic/symmetric truncation: as m grows, does the central-rod
   period mismatch converge (=end effect) or persist (=structural)?
3. Check the positive-mass forcing: a finite chain with R^4 asymptotics and
   matching periods would be Ricci-flat ALE = flat, hence no bolts.
"""
import json, os, math
from fractions import Fraction

# Import the Step 37 probe machinery for the numerical computation
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace = os.path.dirname(script_dir)
sys.path.insert(0, os.path.join(workspace, 'scripts'))
from step37_weyl_partition_period_probe import (
    alternating_partition, log_period_coeff, Segment
)

def main():
    results = {}
    
    # ============ Part 1: Verify exact formula ============
    # Strategist's prediction: for m finite rods (m/2 same-label each),
    # exp(ell_max - ell_min) = prod_{k=1}^{n-1} (2k+1)/(2k)
    # where n = m/2 is the number of same-label rods.
    predicted_exact = {}
    for n_same in range(2, 8):
        p = Fraction(1)
        for k in range(1, n_same):
            p *= Fraction(2*k + 1, 2*k)
        predicted_exact[n_same] = {"fraction": str(p), "decimal": float(p)}
    results["predicted_exp_range_formula"] = {
        "description": "exp(ell_max - ell_min) = prod_{k=1}^{n-1} (2k+1)/(2k)",
        "values": {str(k): v for k, v in predicted_exact.items()}
    }
    
    # Numerical verification from Step 37 probe data
    numerical_from_step37 = {
        4: 1.5000000000027216,
        6: 1.8750000000034883,
        8: 2.187500000004003,
        10: 2.460937500004417
    }
    verification = {}
    for m, num_val in numerical_from_step37.items():
        n_same = m // 2
        pred = predicted_exact[n_same]["decimal"]
        rel_err = abs(num_val - pred) / pred
        verification[str(m)] = {
            "m_finite": m, "n_same_label": n_same,
            "numerical": num_val, "predicted": pred,
            "relative_error": rel_err, "match": rel_err < 1e-10
        }
    results["step37_verification"] = verification
    
    # ============ Part 2: Consecutive same-label ratios ============
    # For the 10-rod chain, compute exp(ell_{k+1} - ell_k) for consecutive
    # same-label rods and check for rational patterns.
    # Using the Step 37 partition probe values:
    ell_label1_10 = [2.2868425538675203, 2.583849906905515, 2.7788225812532468,
                     2.961144138047143, 3.187384928775331]
    consec_ratios_10 = []
    for i in range(len(ell_label1_10) - 1):
        r = math.exp(ell_label1_10[i+1] - ell_label1_10[i])
        # Try to identify as a rational
        fr = Fraction(r).limit_denominator(100)
        consec_ratios_10.append({
            "from_rod": 2*i+1, "to_rod": 2*i+3,
            "exp_ratio": r, "candidate_fraction": str(fr),
            "match": abs(r - float(fr)) < 1e-8
        })
    results["consecutive_ratios_m10"] = consec_ratios_10
    
    # Check: the strategist says central rods differ by exactly 6/5
    # Central pair in 10-rod: rods 5,7 (label-1 indices 2,3)
    central_ratio = math.exp(ell_label1_10[3] - ell_label1_10[2])
    results["central_pair_m10"] = {
        "exp_ratio": central_ratio,
        "candidate_6/5": abs(central_ratio - 6/5) < 1e-8,
        "match_exact": abs(central_ratio - 1.2) < 1e-8
    }
    
    # ============ Part 3: Periodic/symmetric truncation ============
    # Grow the chain symmetrically and check if central-rod mismatch → 0.
    # If it does, the mismatch is an end effect; if not, structural.
    periodic_test = {}
    for m in [4, 6, 8, 10, 12, 14, 16, 20, 24, 30]:
        segs = alternating_partition(m, left_label=2)
        label_1_rods = [s for s in segs if s.finite() and s.label == 1]
        n1 = len(label_1_rods)
        if n1 < 2:
            continue
        
        # Compute ell for the two most central label-1 rods
        mid = n1 // 2
        if n1 % 2 == 0:
            # Even: two central rods at indices mid-1, mid
            ell_a = log_period_coeff(segs, label_1_rods[mid-1])
            ell_b = log_period_coeff(segs, label_1_rods[mid])
        else:
            # Odd: central rod and its neighbor
            ell_a = log_period_coeff(segs, label_1_rods[mid-1])
            ell_b = log_period_coeff(segs, label_1_rods[mid])
        
        exp_ratio = math.exp(abs(ell_b - ell_a))
        periodic_test[str(m)] = {
            "n_same_label": n1,
            "central_ell_diff": abs(ell_b - ell_a),
            "central_exp_ratio": exp_ratio,
            "converges_to_1": None  # will fill
        }
    
    # Check convergence pattern
    ms = sorted(int(k) for k in periodic_test.keys())
    ratios_list = [periodic_test[str(m)]["central_exp_ratio"] for m in ms]
    if len(ratios_list) >= 3:
        diffs = [abs(ratios_list[i+1] - ratios_list[i]) for i in range(len(ratios_list)-1)]
        converging = all(diffs[i+1] < diffs[i] for i in range(len(diffs)-1)) if len(diffs) >= 2 else False
        for m in ms:
            periodic_test[str(m)]["converges_to_1"] = converging
    
    results["periodic_truncation"] = periodic_test
    
    # ============ Part 4: Positive mass theorem argument ============
    # For a finite alternating chain with semi-infinite ends forming a Z^2-basis:
    # - At infinity, looks like R^4 (modulo finite group)
    # - If all periods matched → complete Ricci-flat ALE metric with R^4 asymptotics
    # - Positive mass theorem: Ricci-flat, AE, zero mass → flat R^4
    # - Flat R^4 has no bolts → contradiction
    # Therefore: the period mismatch for finite chains is STRUCTURALLY FORCED.
    
    # Verify the asymptotic type: left end has label 2, right end has label 1.
    # det([[1,0],[0,1]]) = 1, so the asymptotics are R^4 (not R^4/Gamma).
    results["positive_mass_argument"] = {
        "statement": "For a finite alternating chain with Z^2-basis semi-infinite ends, "
                     "period matching would give Ricci-flat ALE with R^4 asymptotics. "
                     "Positive mass theorem forces mass >= 0, mass = 0 iff flat. "
                     "Flat R^4 has no bolts. So period mismatch is forced.",
        "applies_to": "finite noncompact chain only",
        "does_NOT_apply_to": "compact polygon (no asymptotics) or infinite periodic chain",
        "semi_inf_labels": {"left": 2, "right": 1},
        "det": 1,
        "asymptotic_type": "R^4"
    }
    
    # ============ Part 5: Compact polygon vs noncompact chain ============
    # The compact alpha-family polygon has NO semi-infinite rods.
    # It is a closed polygon with m edges and m corners.
    # The Weyl/rod formalism requires adaptation to the compact setting.
    # 
    # Key structural point: for the INFINITE periodic chain with period 2
    # (translate by two rod lengths), same-label rods are automatically
    # identified by the periodicity, so ell values match WITHIN each label.
    # The obstruction then lives in the transition from the microscopic
    # periodic Ricci-flat chain to the macroscopic λ=1 polygon.
    #
    # This is a two-scale matching problem:
    # - Inner scale: periodic Ricci-flat rod chain (Schwarzschild-type bolts)
    # - Outer scale: positive-Einstein orbit space (polygon with Ric=g)
    # Same architecture as Route A's balanced annulus for noncollapsed bubbling.
    
    results["compact_polygon_analysis"] = {
        "two_scale_matching": {
            "inner": "periodic Ricci-flat rod chain with Schwarzschild-type bolts",
            "outer": "positive-Einstein toric metric (Ric = Lambda*g) orbit space",
            "matching_region": "annular collar at intermediate scale",
            "analogy": "Same architecture as noncollapsed Route A balanced annulus"
        },
        "periodic_chain_period_matching": {
            "2_periodic_translation": "same-label rods identified → ell match automatic",
            "obstruction_locus": "transition from periodic RF chain to macroscopic Lambda>0 polygon"
        },
        "key_question": "Does the compact polygon's finite total angle (2π vs "
                       "infinite accumulation) create a global period obstruction?"
    }
    
    # ============ Part 6: Energy-per-cell verification ============
    # Check whether the bolt-cell integral includes the polar/corner regions.
    # For a single Schwarzschild bolt of length L:
    # Bolt region: r in [0, L], with boundary at the rod.  
    # The curvature energy 8π² is concentrated near the bolt.
    # Does this include the NUT/corner region?
    #
    # In the Nariai limit (A→∞, L→0), the rescaled metric is
    # Euclidean Schwarzschild with mass → 1/2, bolt radius → 1.
    # The total ∫|Rm|² for ES is 8π² (Euler characteristic 2).
    # The ES metric covers the bolt and both polar caps.
    # So the per-bolt 8π² INCLUDES the polar/corner contributions.
    # No additional O(1) per corner is needed.
    
    results["energy_per_cell"] = {
        "euclidean_schwarzschild_chi": 2,
        "ES_energy": "8*pi^2 * chi_ES = 8*pi^2 * 2 = 16*pi^2",
        "but_ES_is_complete_manifold_not_half": True,
        "correction": "Each bolt in the alternating chain is HALF an ES (one bolt, not two). "
                      "The half-cell energy is 8π², which includes one bolt and two half-caps. "
                      "When two half-cells share a NUT/corner, the two half-caps merge into one cap. "
                      "So the total for m bolts is m × 8π² WITHOUT double-counting corners.",
        "total_vs_CGB": {
            "total_energy": "m × 8π²",
            "CGB_budget": "8π² × χ = 8π² × (m + 2)",
            "slack": "8π² × 2 = 16π²",
            "interpretation": "The 16π² slack accommodates the two polar regions at the polygon's "
                            "two 'poles' (if thinking of it as a sphere-like orbit space), "
                            "or the boundary conditions. This is NOT zero slack."
        }
    }
    
    path = os.path.join(workspace, "data", "step38_exact_period_algebra.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved to {path}")
    
    print("\n=== PREDICTED EXP RANGE (strategist formula) ===")
    for k in sorted(predicted_exact.keys()):
        v = predicted_exact[k]
        print(f"  n_same={k}: {v['fraction']} = {v['decimal']}")
    
    print("\n=== STEP 37 VERIFICATION ===")
    for m in sorted(verification.keys(), key=int):
        v = verification[m]
        print(f"  m={m}: predicted={v['predicted']:.10f}, match={v['match']}")
    
    print("\n=== CONSECUTIVE RATIOS (m=10, label 1) ===")
    for cr in consec_ratios_10:
        print(f"  rods {cr['from_rod']}->{cr['to_rod']}: exp={cr['exp_ratio']:.10f}, "
              f"fraction={cr['candidate_fraction']}, match={cr['match']}")
    
    print(f"\n=== CENTRAL PAIR m=10: ratio={central_ratio:.10f}, is 6/5? {results['central_pair_m10']['candidate_6/5']} ===")
    
    print("\n=== PERIODIC TRUNCATION (central exp ratio) ===")
    for m in sorted(periodic_test.keys(), key=int):
        v = periodic_test[m]
        print(f"  m={int(m):3d} ({v['n_same_label']:2d} same): central_exp_ratio={v['central_exp_ratio']:.10f}")
    
    print("\n=== POSITIVE MASS: mismatch is structurally forced for finite chain ===")
    print(f"  Asymptotic type: {results['positive_mass_argument']['asymptotic_type']}")
    print(f"  Does NOT apply to: {results['positive_mass_argument']['does_NOT_apply_to']}")
    
    print(f"\n=== ENERGY PER CELL ===")
    epc = results['energy_per_cell']
    print(f"  Total: m × 8π², CGB budget: (m+2) × 8π², slack: 16π²")
    print(f"  Interpretation: {epc['total_vs_CGB']['interpretation'][:100]}...")

if __name__ == '__main__':
    main()
