"""
Step 21 (S0910A02): rod-flux identity and alpha-family audit for the toric
#_k(S^2 x S^2) positive-branch crux.

This script does not construct a Ricci-pinched metric.  It checks what follows
from the 1D rod equation
    Q'' + (1 - 2 K_edge) Q = 0, Q(0)=Q(L)=0, Q'(0)=1, Q'(L)=-1,
and records the consequences for the previously proposed chi-uniform flux/volume
route.
"""
import json, math, os
from typing import Dict, List

OUT = "Sessions/S0910A02/workspace/data/step21_toric_rod_identity_alpha_audit.json"


def rod_constant_A(A: float) -> Dict[str, float]:
    omega = math.sqrt(1 + 2*A)
    L = math.pi/omega
    flux = 2/(1 + 2*A)
    vol_per_rod = 2*math.pi**2*flux
    vol_per_rod_from_length = 4*L*L
    return {
        "A": A,
        "omega": omega,
        "L": L,
        "L_sqrt_A": L*math.sqrt(A) if A > 0 else 0.0,
        "flux": flux,
        "vol_per_rod": vol_per_rod,
        "vol_per_rod_from_4L2": vol_per_rod_from_length,
        "relative_vol_formula_error": abs(vol_per_rod - vol_per_rod_from_length)/max(1.0, abs(vol_per_rod)),
    }


def anchor_checks() -> Dict[str, Dict[str, float]]:
    # Anchors use Vol = 4 sum_i L_i^2 in the constant-edge-curvature exact cases.
    anchors = {
        "S4_m2": {"m": 2, "L": math.pi*math.sqrt(3), "known_vol": 24*math.pi**2},
        "CP2_m3": {"m": 3, "L": math.pi*math.sqrt(1.5), "known_vol": 18*math.pi**2},
        "S2xS2_m4": {"m": 4, "L": math.pi, "known_vol": 16*math.pi**2},
    }
    out = {}
    for name, a in anchors.items():
        vol = 4*a["m"]*a["L"]**2
        out[name] = {
            **a,
            "rod_identity_vol": vol,
            "relative_error": abs(vol-a["known_vol"])/a["known_vol"],
        }
    return out


def alpha_family(alpha: float, ms: List[int]) -> List[Dict[str, float]]:
    rows = []
    for m in ms:
        A = m**alpha
        rd = rod_constant_A(A)
        total_flux = m*rd["flux"]
        vol4 = 2*math.pi**2*total_flux
        perimeter = m*rd["L"]
        # For a disk-like m-gon with geodesic sides and right-angle corners,
        # int K = 2*pi - m*pi/2.  A constant -A collar carrying this total
        # curvature would need total area about (m*pi/2 - 2*pi)/A.
        gb_negative_curv = math.pi*(m/2 - 2)
        collar_area_total = gb_negative_curv/A if A > 0 else float("inf")
        collar_area_per_rod = collar_area_total/m
        collar_width_per_rod = collar_area_per_rod/rd["L"]
        rows.append({
            "m": m,
            "alpha": alpha,
            "A=m^alpha": A,
            "L": rd["L"],
            "L_sqrt_A": rd["L_sqrt_A"],
            "flux_per_rod": rd["flux"],
            "total_flux": total_flux,
            "vol4=2pi2_total_flux": vol4,
            "perimeter=mL": perimeter,
            "GB_negative_curvature_magnitude": gb_negative_curv,
            "constant_minus_A_collar_area_total": collar_area_total,
            "collar_area_per_rod": collar_area_per_rod,
            "collar_width_per_rod": collar_width_per_rod,
            "width_over_L": collar_width_per_rod/rd["L"],
            "bishop_upper_vol_delta0": 24*math.pi**2,
            "bishop_margin_delta0": 24*math.pi**2 - vol4,
        })
    return rows


def regular_right_angle_mgon(m: int, A: float) -> Dict[str, float]:
    # Regular right-angled hyperbolic m-gon in curvature -A.
    # For curvature -1: cosh(s/2)=cos(pi/m)/sin(pi/4).
    ratio = math.cos(math.pi/m)/math.sin(math.pi/4)
    if ratio <= 1:
        side_unit = 0.0
    else:
        side_unit = 2*math.acosh(ratio)
    side = side_unit/math.sqrt(A) if A > 0 else float("inf")
    L_ode = math.pi/math.sqrt(1 + 2*A)
    return {
        "m": m,
        "A": A,
        "side_unit_curv_minus1": side_unit,
        "regular_side_length": side,
        "rod_ODE_length": L_ode,
        "ratio_rodODE_over_regular": L_ode/side if side > 0 else float("inf"),
        "asymptotic_side_unit_m_infty": 2*math.acosh(math.sqrt(2)),
        "asymptotic_rod_unit_A_infty": math.pi/math.sqrt(2),
        "asymptotic_ratio": (math.pi/math.sqrt(2))/(2*math.acosh(math.sqrt(2))),
    }


def A_match_regular(m: int) -> Dict[str, float]:
    # Solve pi/sqrt(1+2A) = s_unit/sqrt(A).
    s = 2*math.acosh(math.cos(math.pi/m)/math.sin(math.pi/4))
    denom = math.pi**2 - 2*s*s
    if s <= 0 or denom <= 0:
        A = None
    else:
        A = s*s/denom
    return {"m": m, "A_match": A, "side_unit": s, "denominator": denom}


def main():
    ms = [6, 8, 10, 20, 50, 100, 200]
    alphas = [1.1, 1.25, 1.5, 1.75, 1.9, 2.0]
    report = {
        "title": "Step 21 toric rod identity and alpha-family necessary-condition audit",
        "scope": "Diagonal/twist-free toric rod data only; not a global pinched metric and not a Yau-26 proof/refutation.",
        "rod_identity": {
            "equation": "Q''+(1-2K_edge)Q=0, Q'(0)=1, Q'(L)=-1",
            "integrated": "int_rod (1-2K_edge) Q ds = 2",
            "flux": "Phi_i=int Q ds = 2 + 2 int K_edge Q ds",
            "volume_normalization": "Vol_4 = 2*pi^2*sum_i Phi_i",
            "constant_K=-A": "Phi_i=2/(1+2A)=2 L_i^2/pi^2, hence Vol_4=4*sum_i L_i^2",
        },
        "anchors": anchor_checks(),
        "cauchy_consequence": {
            "statement": "For constant-edge-curvature rods, Vol_4=4 sum L_i^2 >= 4 L_tot^2/m. Any O(1) lower control of total length/perimeter gives at most a C/m lower bound, not a chi-uniform gap.",
            "propA_implication": "A lower bound v0(chi)->0 is insufficient for the finite-cover amplifier; the previous modulus/perimeter route cannot by itself supply the topology-uniform volume gap needed by Proposition A unless it forces a rod length/flux scale independent of m.",
        },
        "alpha_family": {f"alpha_{alpha}": alpha_family(alpha, ms) for alpha in alphas},
        "regular_polygon_mismatch": {
            "description": "Compare the large-A rod ODE length L~pi/sqrt(2A) with a regular right-angled m-gon in constant curvature -A, whose side is 2 arcosh(cos(pi/m)/sin(pi/4))/sqrt(A).",
            "samples_A=m^alpha_alpha1p5": [regular_right_angle_mgon(m, m**1.5) for m in ms],
            "A_match_if_constant_curvature_regular": [A_match_regular(m) for m in ms],
        },
        "scientific_conclusion": [
            "The exact rod identity is a stronger and cleaner bookkeeping handle than the Step-20 modulus note.",
            "The constant-edge alpha family with 1<alpha<2 satisfies the rod ODE, unit endpoint slopes, GB-scale collar area, Bishop volume upper bound, and has total flux/volume tending to zero; these necessary conditions therefore do not imply a chi-uniform toric volume gap.",
            "The regular constant-curvature right-angled m-gon comparison gives a real but narrow obstruction: a globally regular constant-curvature polygon cannot simultaneously have large A and the rod ODE length.  This does not defeat strip-like or nonconstant-curvature collar geometries, where the negative curvature can be boundary-localized and the interior nearly flat.",
            "The remaining inexpensive BUILD obstruction is the full horizontal/traceless transition equation in the collar-to-interior region; the finite rod/corner and scalar/global bookkeeping conditions have not capped A."
        ]
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(report, f, indent=2)
    print(json.dumps({
        "title": report["title"],
        "anchors_ok": {k: v["relative_error"] for k,v in report["anchors"].items()},
        "alpha_samples": {
            "alpha_1.5_m100": report["alpha_family"]["alpha_1.5"][5],
            "alpha_1.9_m100": report["alpha_family"]["alpha_1.9"][5],
        },
        "regular_polygon_asymptotic_ratio": report["regular_polygon_mismatch"]["samples_A=m^alpha_alpha1p5"][-1]["asymptotic_ratio"],
        "A_match_m200": report["regular_polygon_mismatch"]["A_match_if_constant_curvature_regular"][-1],
        "saved": OUT,
    }, indent=2))

if __name__ == "__main__":
    main()
