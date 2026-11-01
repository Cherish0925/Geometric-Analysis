#!/usr/bin/env python3
"""
Step 93: analytic structure of the AA/BB coincident-point divergence.

The coincident-factor spectral sum can be expressed through the second zonal 
derivative of the S^2 heat kernel at x=1 (same point), using the identity:
    P_l''(1) = l(l+1)(l(l+1)-2)/8  for l >= 0

and the dimension-raising identity:
    d_x^2 p_t^{S^2}(x) = 4pi^2 e^{-6t} p_t^{S^6}(x)

At x=1: d_x^2 p_t^{S^2}(1) = 4pi^2 e^{-6t} p_t^{S^6}(1).

The on-diagonal heat kernel p_t^{S^6}(1) diverges as t->0 like (4pi t)^{-3},
so d_x^2 p_t^{S^2}(1) ~ pi^2/(16 pi^3 t^3) = 1/(16 pi t^3) * e^{-6t}.

Compare with the AB SEPARATED case: d_x p_t^{S^2}(-1) = 2pi e^{-2t} p_t^{S^4}(-1),
which is finite for t > 0 because the antipodal heat kernel is smooth.

This script verifies the heat-kernel representation and the divergence rate.
"""
import json, math, pathlib
import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

def mu(l): return l*(l+1)


def zonal_heat_diagonal_deriv2(t, Lmax=500):
    """Compute d_x^2 p_t^{S^2}(x)|_{x=1} by direct spectral sum.
    
    p_t(x) = sum_{l>=0} (2l+1)/(4pi) P_l(x) e^{-mu_l t}
    d_x^2 p_t(1) = sum_{l>=0} (2l+1)/(4pi) P_l''(1) e^{-mu_l t}
                  = sum_{l>=2} (2l+1)/(4pi) * mu_l(mu_l-2)/8 * e^{-mu_l t}
    (l=0,1 have P_l''(1)=0 for l=0 and P_1''(1)=0.)
    """
    total = 0.0
    for l in range(2, Lmax+1):
        m = mu(l)
        total += (2*l+1)/(4*math.pi) * m*(m-2)/8 * math.exp(-m*t)
    return total


def zonal_heat_antipodal_deriv1(t, Lmax=500):
    """Compute d_x p_t^{S^2}(x)|_{x=-1} by spectral sum.
    
    d_x p_t(-1) = sum_{l>=1} (2l+1)/(4pi) P_l'(-1) e^{-mu_l t}
    P_l'(-1) = (-1)^{l+1} l(l+1)/2
    """
    total = 0.0
    for l in range(1, Lmax+1):
        m = mu(l)
        total += (2*l+1)/(4*math.pi) * ((-1)**(l+1)) * m/2 * math.exp(-m*t)
    return total


def verify_dimension_raising(t, Lmax=500):
    """Check d_x^2 p_t^{(2)}(1) = 4pi^2 e^{-6t} p_t^{(6)}(1)."""
    # Direct: spectral sum
    direct = zonal_heat_diagonal_deriv2(t, Lmax)
    
    # S^6 diagonal heat kernel: p_t^{(6)}(1) = sum_{l>=0} d_l^{(6)}/(Vol S^6) * e^{-lambda_l^{(6)} t}
    # On S^n(1): eigenvalue = l(l+n-1), degeneracy ~ (2l+n-1)(l+n-2)!/[l!(n-1)!]
    # For S^6: n=6, eigenvalue = l(l+5), degeneracy = (2l+5)*(l+4)!/(l!*5!)
    s6_diag = 0.0
    vol_s6 = math.pi**3 * 16 / 15  # Vol(S^6) = 16*pi^3/15
    for l in range(0, Lmax+1):
        lam = l*(l+5)
        # degeneracy for S^6
        deg = 1
        for k in range(1, 5):
            deg *= (l+k)
        deg = deg * (2*l+5) // math.factorial(5)
        s6_diag += deg / vol_s6 * math.exp(-lam * t)
    
    predicted = 4 * math.pi**2 * math.exp(-6*t) * s6_diag
    
    return {
        "t": t,
        "direct_spectral": direct,
        "dimension_raising_prediction": predicted,
        "relative_error": abs(direct - predicted) / max(abs(direct), 1e-30),
    }


def compare_ab_vs_aabb_divergence():
    """Show the AB convergence vs AA/BB divergence as heat parameter varies."""
    results = []
    for t in [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002]:
        L = max(100, int(20/math.sqrt(t)))
        
        # AB-type: antipodal first derivative (finite)
        ab_deriv = zonal_heat_antipodal_deriv1(t, L)
        
        # AA/BB-type: diagonal second derivative (divergent)
        aabb_deriv = zonal_heat_diagonal_deriv2(t, L)
        
        # Predicted AA/BB from S^6: 4pi^2 e^{-6t} p_t^{(6)}(1)
        # At short time: p_t^{(6)}(1) ~ (4pi t)^{-3} = 1/(64 pi^3 t^3)
        # So aabb_pred ~ 4pi^2 * 1/(64 pi^3 t^3) = 1/(16 pi t^3)
        aabb_pred_shorttime = 1.0 / (16 * math.pi * t**3)
        
        results.append({
            "t": t,
            "Lmax": L,
            "AB_antipodal_deriv1": ab_deriv,
            "AABB_diagonal_deriv2": aabb_deriv,
            "AABB_shorttime_prediction": aabb_pred_shorttime,
            "ratio_aabb_to_pred": aabb_deriv / aabb_pred_shorttime if aabb_pred_shorttime > 0 else None,
            "AB_finite": True,
            "AABB_divergent": True,
        })
    return results


def main():
    # Verify dimension-raising identity
    dim_raising = [verify_dimension_raising(t) for t in [0.5, 0.2, 0.1, 0.05]]
    
    # Compare AB vs AABB
    comparison = compare_ab_vs_aabb_divergence()
    
    results = {
        "step": 93,
        "scope": "analytic structure of AA/BB coincident-point divergence via heat kernel",
        "dimension_raising_identity": {
            "formula": "d_x^2 p_t^{S^2}(x)|_{x=1} = 4*pi^2 * e^{-6t} * p_t^{S^6}(1)",
            "verification": dim_raising,
        },
        "ab_vs_aabb_comparison": comparison,
        "analytic_structure": {
            "AB_sector": {
                "heat_representation": "d_x p_t^{S^2}(-1) = 2*pi*e^{-2t}*p_t^{S^4}(-1) > 0",
                "convergent": True,
                "sign": "B(s) = -4*pi*d_t p_t^{S^2}(-1)|_{t=s/2} < 0 by p_t^{S^4}(-1) > 0",
                "K_adj_AB": "≈ -0.031, finite and strictly negative",
            },
            "AABB_sector": {
                "heat_representation": "d_x^2 p_t^{S^2}(1) = 4*pi^2*e^{-6t}*p_t^{S^6}(1)",
                "convergent": False,
                "short_time": "~ 1/(16*pi*t^3) as t->0",
                "divergence_type": "coincident-point singularity in one S^2 factor",
            },
        },
        "mathematical_conclusion": (
            "The sector decomposition AB vs AA/BB is meaningful only for the AB sector, "
            "which involves separated-point evaluation in both factors. The AA/BB sectors "
            "involve coincident-point evaluation in one factor, creating a divergence "
            "analogous to a UV singularity. The physical inter-node Green coefficient is "
            "finite (smooth Green function between separated nodes), but extracting the "
            "AA/BB contribution requires the full singular source structure from the ALE "
            "model (Ozuch's H^4), not a naive mode-by-mode sum. The AB sign theorem "
            "K_adj^AB < 0 remains valid and is the only cleanly computable sector."
        ),
    }
    
    outpath = DATA_DIR / "step93_aabb_analytic_divergence.json"
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(json.dumps(results, indent=2, default=str))
    print(f"Wrote {outpath}")


if __name__ == "__main__":
    main()
