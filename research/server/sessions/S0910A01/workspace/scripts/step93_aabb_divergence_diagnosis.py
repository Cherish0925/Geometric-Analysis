#!/usr/bin/env python3
"""
Step 93: diagnose the AA/BB coincident-point divergence structure.

STEP 94 CORRECTION: this diagnostic is superseded as a statement about the
principal product-background AA/BB response. It forms the electric+magnetic
tensor numerator using full-Lie magnetic amplitude 4b but normalizes magnetic
with the electric norm. With the correct magnetic norm, the separated-pole
electric and magnetic tensor contributions cancel exactly. Use
step94_corrected_aabb_principal_response.py.

The key finding: for the NS adjacent pair, the BB sector evaluates the scalar 
harmonic on factor A at the SAME pole (N) in both source and receiver, creating
a coincident-point singularity. The AB sector avoids this because both factors 
are evaluated at separated (antipodal) points.

This script:
1. Isolates the divergence rate (power law in 1/tau).
2. Verifies that the finite sector (AA for NS) has a true limit.
3. Checks whether electric + magnetic cancel or reinforce.
4. Computes the coincident-factor spectral weight to identify the divergence.
"""
import json, math, pathlib
import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def mu(l): return l*(l+1)

def b_squared(l):
    """b^2 for the m=2 pole amplitude: (2b)^2 = (2l+1)/(32pi) * mu*(mu-2)."""
    if l < 2: return 0.0
    m = mu(l)
    return (2*l+1)/(128*math.pi) * m * (m-2)


def coincident_factor_weight(l_same, P_val, tf_norm_other, s_or_t="scalar"):
    """Weight from the factor where source and receiver share the same pole.
    
    For BB-NS: scalar on A at same pole. 
    d01 phi_A(N)^2 = (2b_A)^2 for s2 mode = (2l+1)/(32pi) * mu_A*(mu_A-2).
    
    Divided by P * (tf_norm_other/2):
    weight_per_lA = (2l_A+1)/(32pi) * mu_A(mu_A-2) / [P * tf_norm_other/2]
    """
    lam = mu(l_same)
    d01_sq = (2*l_same+1)/(32*math.pi) * lam * (lam - 2) * 4  # (2b)^2
    return d01_sq / (P_val * tf_norm_other / 2.0)


def diagnose_divergence():
    """Track the l_A partial sums for BB sector in NS pair at fixed l_B."""
    results = []
    for l_B in [2, 3, 4]:
        lam_B = mu(l_B)
        tf_norm_B = 0.5 * lam_B * (lam_B - 2)
        
        # Tensor B at different poles: T23(N) * T23(S)
        # Electric s2: sign = -((-1)^l_B) for even->even
        # Magnetic c2: sign = (-1)^l_B
        
        partial_sums = []
        running = 0.0
        for l_A in range(2, 201):
            lam_A = mu(l_A)
            P_val = 0.5 * (lam_A + lam_B) - 1.0
            
            # Scalar A at same pole: (2b_A)^2 for s2 = (2l_A+1)mu_A(mu_A-2)/(32pi)
            d01_sq = (2*l_A+1) * lam_A * (lam_A - 2) / (32 * math.pi)
            
            # Contribution per l_A (summed over electric+magnetic for tensor B)
            # For electric s2 on B: T23 = 2b_B at N, sign_S = -((-1)^l_B) * 2b_B
            # T23(N)*T23(S) = -((-1)^l_B) * 4*b_squared(l_B)
            elec_B = -((-1)**l_B) * 4 * b_squared(l_B)
            # For magnetic c2 on B: T23 = 4b_B at N, sign_S = (-1)^l_B * 4b_B.
            # STEP 94 CORRECTION: this numerator must be divided by the magnetic
            # norm, which is four times the electric norm. Combining `elec_B +
            # mag_B` before the norm division creates the false residual.
            mag_B = ((-1)**l_B) * 16 * b_squared(l_B)
            
            # Superseded net tensor B contribution (fixed l_B).
            tensor_B_product = elec_B + mag_B
            
            # Source normalization factor (pi^2/2 from S_odd = (pi^2/2)R_odd)
            # Receiver factor: (1/2)^2 from both R_odd applications
            # Total per mode: (pi^2/2) * (1/4) * d01_sq * tensor_B / (P * quotient_norm)
            # quotient_norm = tf_norm_B / 2 for BB
            
            val = (math.pi**2 / 2) * 0.25 * d01_sq * tensor_B_product / (P_val * tf_norm_B / 2)
            running += val
            
            if l_A <= 10 or l_A % 20 == 0:
                partial_sums.append({
                    "l_A": l_A, "running_sum": running,
                    "this_term": val,
                    "d01_sq": d01_sq,
                })
        
        results.append({
            "l_B": l_B,
            "tensor_B_sign": "negative" if (elec_B + mag_B) < 0 else "positive",
            "partial_sums": partial_sums,
            "total_l200": running,
        })
    return results


def compute_asymptotic_rate():
    """For large l_A, the partial sum growth rate.
    
    The weight per l_A ~ (2l+1) l^4 / (32pi) / (l^2/2 * norm_B/2) 
    = (2l+1) l^4 * 4 / (32pi * l^2 * norm_B) ~ l^3 / (8pi * norm_B)
    
    Sum_{l=2}^L ~ L^4 / (32pi * norm_B)
    """
    return {
        "asymptotic_term": "~(2l+1) * mu_A * (mu_A-2) / (32pi * P * norm_B_quotient)",
        "P_for_large_lA": "~ mu_A/2",
        "growth_per_term": "~ l_A^3 / (8pi * norm_B_quotient)", 
        "partial_sum_to_L": "~ L^4 / (32pi * norm_B_quotient)",
        "power_law": 4,
        "interpretation": "quartic divergence from coincident-point scalar evaluation in factor A",
    }


def verify_finite_sector():
    """Verify that AA for NS (tensor A same pole, scalar B different poles) converges."""
    partial_sums = []
    running = 0.0
    for l_A in range(2, 201):
        lam_A = mu(l_A)
        for l_B in range(2, 201):
            lam_B = mu(l_B)
            P_val = 0.5 * (lam_A + lam_B) - 1.0
            
            # Tensor A at same pole: T01 products
            # Electric s2: T01(N)^2 = 4*b_squared(l_A) > 0 (no alternation)
            # Magnetic c2: T01(N)^2 = 16*b_squared(l_A) > 0
            tensor_A_same = (4 + 16) * b_squared(l_A)
            
            # Scalar B at different poles: d23(N)*d23(S) 
            # s2 mode: sign = -((-1)^l_B) * 4*b_squared(l_B)
            scalar_B_diff = -((-1)**l_B) * 4 * b_squared(l_B)
            
            val = (math.pi**2 / 2) * 0.25 * tensor_A_same * scalar_B_diff / (P_val * 0.5 * lam_A * (lam_A - 2) / 2)
            running += val
    
    return {"AA_NS_total_L200_no_heat": running, "note": "no heat regularization; convergence from B-factor alternation"}


def check_electric_magnetic_signs():
    """Check whether electric and magnetic TF contributions reinforce or cancel."""
    results = []
    for l_B in [2, 3, 4, 5]:
        lam_B = mu(l_B)
        # At north pole, south pole evaluations for tensor:
        # Electric s2: T(N) = 2b, T(S) = -((-1)^l)*2b => product = -((-1)^l)*4b^2
        # Magnetic c2: T(N) = 4b, T(S) = (-1)^l*4b   => product = (-1)^l*16b^2
        # Sum: -((-1)^l)*4b^2 + (-1)^l*16b^2 = (-1)^l * 12b^2 (if l even: +12b^2; odd: -12b^2)
        
        elec_sign = -((-1)**l_B)
        mag_sign = (-1)**l_B
        
        # STEP 94 CORRECTION: mag has 4x the product amplitude but also 4x the
        # norm, so the normalized separated-pole contributions cancel rather than
        # leaving magnetic dominance.
        net_sign = "positive" if (-1)**l_B > 0 else "negative"
        
        results.append({
            "l_B": l_B,
            "electric_product_sign": elec_sign,
            "magnetic_product_sign": mag_sign,
            "magnetic_to_electric_ratio": -4,
            "net_sign": net_sign,
            "alternates_with_l_parity": True,
        })
    return results


def main():
    diag = diagnose_divergence()
    asymp = compute_asymptotic_rate()
    em_signs = check_electric_magnetic_signs()
    
    results = {
        "step": 93,
        "scope": "AA/BB coincident-point divergence diagnosis",
        "key_finding": (
            "The AA/BB trace-free tensor sectors have a same-factor coincident-point "
            "divergence when one scalar factor is evaluated at the same pole in both "
            "source and receiver. For the NS adjacent pair, BB diverges (scalar A at "
            "same N pole) while AA is finite (scalar B at separated N/S poles, giving "
            "convergent alternating sum). The divergence is quartic in the cutoff L."
        ),
        "asymptotic_rate": asymp,
        "electric_magnetic_signs": em_signs,
        "divergence_diagnosis_by_lB": [
            {"l_B": d["l_B"], "tensor_sign": d["tensor_B_sign"], 
             "running_at_l200": d["total_l200"],
             "first_5_terms": d["partial_sums"][:5]}
            for d in diag
        ],
        "physical_meaning": (
            "The full product Green function G_P(x_i, x_j) between separated nodes "
            "is smooth. The divergence is an artifact of the sector decomposition: "
            "individual AA or BB sectors can diverge even though the total over all "
            "sectors (including AB) converges. This means the AA/BB contribution to "
            "the inter-node interaction CANNOT be computed as an independent sector sum. "
            "It must be combined with source normalization, gauge projection, or a "
            "reorganized partial summation that keeps one full factor's Green function "
            "unsplit."
        ),
        "consequence_for_coefficient": (
            "The AB sector result (K_adj^AB ≈ -0.031) is well-defined because both "
            "factors involve separated-point evaluation. The AA/BB sector requires a "
            "different computational strategy: either (a) keep the scalar factor's "
            "coincident sum as a delta-function and extract the regular part after "
            "singular subtraction, or (b) reorganize the spectral sum by first summing "
            "over the coincident factor analytically (using the factor heat kernel or "
            "Green function at the diagonal), then summing over the separated factor. "
            "Strategy (b) is the Strategist's suggestion: the coincident scalar sum "
            "produces a scalar heat kernel at the diagonal point, which can be handled "
            "with zonal derivative identities."
        ),
    }
    
    outpath = DATA_DIR / "step93_aabb_divergence_diagnosis.json"
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(json.dumps(results, indent=2, default=str))
    print(f"Wrote {outpath}")


if __name__ == "__main__":
    main()
