#!/usr/bin/env python3
"""
Step 8: four-dimensional positive-branch Weyl budget checks.

This script records the Chern--Gauss--Bonnet upper/lower curvature-energy
inequalities used in the Preceptor review of Step 7.  It is not a numerical
search for metrics; it only evaluates sharp algebraic/Bishop constants under
|Ric-g|_op <= delta on closed oriented 4-manifolds.
"""
import json, math
from pathlib import Path

PI = math.pi

def beta_opt(delta: float) -> float:
    # Pointwise optimal lower bound for B=s^2/24-|Ric0|^2/2 from Step 4 TTCS.
    if delta <= 1.0/3.0:
        return (2.0/3.0)*(1.0-delta)**2
    return (2.0/3.0)*(1.0+delta)*(1.0-2.0*delta)

def bishop_vol(delta: float) -> float:
    # Ric >= (1-delta)g = 3H g in dimension 4, H=(1-delta)/3.
    return 24.0*PI**2/(1.0-delta)**2

def weyl_lower(delta: float, chi: float) -> float:
    # ∫|W|^2 >= 8π²χ - (2/3)(1+δ)^2 Vol, with Bishop volume ceiling.
    return 8.0*PI**2*(chi - 2.0*((1.0+delta)/(1.0-delta))**2)

def weyl_lower_s2xs2(delta: float, k: int) -> float:
    return weyl_lower(delta, 2.0+2.0*k)

def weyl_mean_lower(delta: float, chi: float) -> float:
    # Since Vol <= BishopVol, mean |W|² >= lower integral / BishopVol.
    return max(0.0, weyl_lower(delta, chi)/bishop_vol(delta))

def rm_upper_safe(delta: float, chi: float) -> float:
    # Standard 4D norm decomposition |Rm|²=|W|²+2|Ric0|²+s²/6.
    # Using GB to eliminate W: ∫|Rm|²=8π²χ+(5/2)∫|Ric0|²+(1/8)∫s².
    # Bounds |Ric0|² <= 4δ² and s² <= 16(1+δ)² pointwise, then Bishop.
    return 8.0*PI**2*chi + (10.0*delta**2 + 2.0*(1.0+delta)**2)*bishop_vol(delta)

def rm_upper_cgb_volume(delta: float, chi: float) -> float:
    # Same identity but using Vol <= 8π²χ/beta(delta). Useful for sign-blind branch.
    b = beta_opt(delta)
    return 8.0*PI**2*chi*(1.0 + (10.0*delta**2 + 2.0*(1.0+delta)**2)/b)

out = {
    "assumptions": {
        "dimension": 4,
        "branch": "positive normalized: |Ric_g - g|_op <= delta < 1/2",
        "orientation": "closed oriented for chi=2+b2; CGB itself works after orientable double cover",
        "bishop_volume_ceiling": "Vol <= 24*pi^2/(1-delta)^2",
        "weyl_lower_formula": "int |W|^2 >= 8*pi^2*(chi - 2*((1+delta)/(1-delta))^2)",
        "rm_upper_safe_formula": "int |Rm|^2 <= 8*pi^2*chi + (10 delta^2 + 2(1+delta)^2)*24*pi^2/(1-delta)^2",
        "rm_norm_convention": "standard tensor norm: |Rm|^2=|W|^2+2|Ric0|^2+s^2/6 in dimension 4"
    },
    "sharpness_check_round_S4_delta0": {
        "chi": 2,
        "bishop_vol": bishop_vol(0.0),
        "weyl_lower": weyl_lower(0.0, 2),
        "round_S4_weyl_integral": 0.0,
        "round_S4_rm_integral": (8.0/3.0)*24.0*PI**2,
        "rm_upper_safe": rm_upper_safe(0.0, 2)
    },
    "samples_S2xS2_connected_sums": []
}
for delta in [0.0, 0.01, 0.05, 0.1, 0.2]:
    for k in [1, 2, 5, 10, 50, 100]:
        chi = 2 + 2*k
        lower = weyl_lower_s2xs2(delta, k)
        out["samples_S2xS2_connected_sums"].append({
            "delta": delta,
            "k": k,
            "chi": chi,
            "bishop_vol_ceiling": bishop_vol(delta),
            "int_W2_lower": lower,
            "int_W2_lower_over_pi2": lower/PI**2,
            "mean_W2_lower_using_bishop": weyl_mean_lower(delta, chi),
            "curvature_length_scale_from_mean": (weyl_mean_lower(delta, chi)**(-0.25) if weyl_mean_lower(delta, chi) > 0 else None),
            "rm_upper_safe_over_pi2": rm_upper_safe(delta, chi)/PI**2,
            "rm_upper_cgb_volume_over_pi2": rm_upper_cgb_volume(delta, chi)/PI**2,
        })

path = Path("Sessions/S0910A02/workspace/data/step8_weyl_budget_positive4.json")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2), encoding="utf-8")
print("Step 8 Weyl budget checks")
print("round S4 Vol ceiling δ=0:", out["sharpness_check_round_S4_delta0"]["bishop_vol"])
print("round S4 Weyl lower δ=0:", out["sharpness_check_round_S4_delta0"]["weyl_lower"])
for row in out["samples_S2xS2_connected_sums"]:
    if row["delta"] in (0.0, 0.1) and row["k"] in (2, 10, 100):
        print(f"δ={row['delta']:.2f}, k={row['k']:3d}: intW2 >= {row['int_W2_lower_over_pi2']:.6g} π², meanW2 >= {row['mean_W2_lower_using_bishop']:.6g}, scale <= {row['curvature_length_scale_from_mean']}")
print("saved", path)
