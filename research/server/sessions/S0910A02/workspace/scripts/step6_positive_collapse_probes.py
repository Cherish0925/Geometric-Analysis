#!/usr/bin/env python3
"""
Step 6 probes for Yau Problem 26 positive-branch collapse.

This script is NOT a proof of Yau26. It records small algebraic and numerical
checks used in Explore:

1. Four-dimensional principal-circle Kaluza--Klein collapse with metric
   g = g_B + t^2 alpha^2 and phi=tF=O(1).  Under standard O'Neill constants
   (with |2-form|^2=sum_{i<j} F_ij^2), Ric_M≈g implies on the 3D base:
       |b|^2≈2,  Ric_B≈2 g_B - (1/2)b⊗b,
   for phi=*b, while the mixed Ricci component forces db≈0 and d* b=0.
   The Bochner identity for 1-forms on the closed base then gives a quantitative
   contradiction for small pinching in a smooth free circle collapse model.

2. Normalization constants: round S^4 with Ric=g has radius sqrt(3), volume
   24π^2, and saturates the 4D CGB beta(0) volume inequality; ALE Ricci-flat
   energy quantum is 8π^2(χ-1/|Γ|), so Eguchi--Hanson contributes 12π^2.

3. A cheap rotationally symmetric S^4 ansatz search for metrics
       dr^2 + f(r)^2 g_{S^3}
   with Ricci eigenvalues in [0.9,1.1].  It tries to minimize volume.  Failure
   to find volume << 24π^2 is only heuristic/falsification evidence for this
   ansatz class, not a theorem.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

try:
    from scipy.optimize import differential_evolution, minimize
    SCIPY_AVAILABLE = True
except Exception as exc:  # pragma: no cover
    SCIPY_AVAILABLE = False
    SCIPY_IMPORT_ERROR = repr(exc)

ROOT = Path("Sessions/S0910A02/workspace")
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)


def kk_obstruction_constants(delta_grid=None) -> Dict:
    """Return convention-dependent quantitative threshold for free S^1 collapse.

    In an orthonormal frame for the base, let phi=*b. With the convention
    Ric(U,U)=|phi|^2/2 and Ric(X,U)=-(1/2)(delta phi)(X), the total-space
    pinching |Ric_M-g_M|_op<=delta gives
        |b|^2 in [2(1-delta),2(1+delta)], |db|<=2delta,
        Ric_B(b,b)>=(1-delta)|b|^2.
    Since d phi=0 gives delta b=0 and delta phi=±*db, Bochner yields
        ∫ Ric_B(b,b) <= ∫(|db|^2+|delta b|^2) <= 4 delta^2 Vol_B.
    Combining with |b|^2>=2(1-delta) gives
        2(1-delta)^2 <= 4 delta^2,
    hence delta >= 1/(1+sqrt(2)).
    """
    threshold = 1.0 / (1.0 + math.sqrt(2.0))
    samples = []
    if delta_grid is None:
        delta_grid = [0.01, 0.05, 0.1, 0.2, threshold, 0.45]
    for d in delta_grid:
        lower = 2.0 * (1.0 - d) ** 2
        upper = 4.0 * d**2
        samples.append(
            {
                "delta": d,
                "bochner_lower_per_base_volume": lower,
                "mixed_error_upper_per_base_volume": upper,
                "contradiction_if_lower_exceeds_upper": lower > upper,
            }
        )
    return {
        "model": "principal S^1 connection metric over closed smooth 3D base",
        "convention": "|2-form|^2=sum_{i<j} F_ij^2; Ric(U,U)=|phi|^2/2; Ric(X,U)=-(delta phi)(X)/2",
        "exact_limit_equations": {
            "vertical": "|b|^2=2",
            "mixed": "db=0 and delta b=0 (since dphi=0 and Ric(X,U)=0)",
            "horizontal": "Ric_B=2 g_B - (1/2)b⊗b",
            "bochner_consequence": "nonzero harmonic b on closed base with Ric_B(b,b)=|b|^2>0 is impossible",
        },
        "quantitative_delta_threshold_under_recorded_constants": threshold,
        "samples": samples,
        "interpretation": "Smooth free circle collapse in dimension 4 cannot have delta_+ -> 0. Positive-pinched collapse must be quotient/orbifold/singular/fixed-stratum compatible, not a regular free S^1 bundle with bounded geometry.",
    }


def normalization_constants() -> Dict:
    vol_s4_unit = 8.0 * math.pi**2 / 3.0
    radius_ric_eq_g = math.sqrt(3.0)
    vol_s4_ric_eq_g = vol_s4_unit * radius_ric_eq_g**4
    beta0 = 2.0 / 3.0
    chi_s4 = 2
    cgb_rhs = 8.0 * math.pi**2 * chi_s4
    return {
        "round_S4_unit_radius": {
            "Ric_constant": 3.0,
            "volume": vol_s4_unit,
        },
        "round_S4_normalized_Ric_equals_g": {
            "radius": radius_ric_eq_g,
            "volume": vol_s4_ric_eq_g,
            "volume_as_multiple_pi2": vol_s4_ric_eq_g / math.pi**2,
            "beta0_times_volume": beta0 * vol_s4_ric_eq_g,
            "8pi2_chi": cgb_rhs,
            "cgb_sharp": abs(beta0 * vol_s4_ric_eq_g - cgb_rhs) < 1e-10,
        },
        "ALE_Ricci_flat_energy_quantum": {
            "formula": "(1/8π²)∫|Rm|² = χ(X) - 1/|Γ|",
            "Eguchi_Hanson": {
                "chi": 2,
                "Gamma_order": 2,
                "energy": 8.0 * math.pi**2 * (2.0 - 0.5),
                "energy_as_multiple_pi2": 12.0,
            },
        },
    }


def rotational_s4_profile(params: np.ndarray, ngrid: int = 800):
    """Return r, f, f', f'' for f=(L/pi) sin(pi r/L) exp(u), u=sum a_k sin^2(k pi r/L)."""
    L = params[0]
    coeffs = params[1:]
    # avoid endpoints where formula divides by f; smooth endpoints are encoded analytically
    eps = 1e-4
    r = np.linspace(eps * L, (1.0 - eps) * L, ngrid)
    x = math.pi * r / L
    s = np.sin(x)
    c = np.cos(x)
    u = np.zeros_like(r)
    ux = np.zeros_like(r)
    uxx = np.zeros_like(r)
    for k, a in enumerate(coeffs, start=1):
        kx = k * x
        # sin^2(kx): first derivative k sin(2kx), second derivative 2 k^2 cos(2kx)
        u += a * np.sin(kx) ** 2
        ux += a * k * np.sin(2.0 * kx)
        uxx += a * 2.0 * k * k * np.cos(2.0 * kx)
    A = L / math.pi
    expu = np.exp(u)
    f = A * s * expu
    # derivatives w.r.t x, then r: d/dr=(pi/L)d/dx
    gx = c + s * ux
    gxx = -s + 2.0 * c * ux + s * (ux * ux + uxx)
    fp = A * expu * gx * (math.pi / L)
    fpp = A * expu * gxx * (math.pi / L) ** 2
    return r, f, fp, fpp


def rotational_s4_metrics(params: np.ndarray, ngrid: int = 800) -> Dict:
    r, f, fp, fpp = rotational_s4_profile(params, ngrid=ngrid)
    ric_rad = -3.0 * fpp / f
    ric_tan = (2.0 * (1.0 - fp**2) - f * fpp) / (f**2)
    vol = 2.0 * math.pi**2 * float(np.trapz(f**3, r))
    return {
        "volume": vol,
        "volume_over_round": vol / (24.0 * math.pi**2),
        "ric_rad_min": float(np.min(ric_rad)),
        "ric_rad_max": float(np.max(ric_rad)),
        "ric_tan_min": float(np.min(ric_tan)),
        "ric_tan_max": float(np.max(ric_tan)),
        "delta_plus_sup": float(max(np.max(np.abs(ric_rad - 1.0)), np.max(np.abs(ric_tan - 1.0)))),
        "L": float(params[0]),
        "coeffs": [float(x) for x in params[1:]],
    }


def run_rotational_search(delta_target: float = 0.1, modes: int = 3) -> Dict:
    if not SCIPY_AVAILABLE:
        return {"available": False, "error": SCIPY_IMPORT_ERROR}

    round_params = np.zeros(modes + 1)
    round_params[0] = math.pi * math.sqrt(3.0)
    round_metrics = rotational_s4_metrics(round_params)

    # Penalty objective. We use coarse grid during global search, then refine best.
    def objective(x):
        # Softly reject pathological profiles by coefficient bounds are already finite; f>0 interior.
        m = rotational_s4_metrics(np.array(x), ngrid=260)
        violations = [
            max(0.0, 0.9 - m["ric_rad_min"]),
            max(0.0, m["ric_rad_max"] - 1.1),
            max(0.0, 0.9 - m["ric_tan_min"]),
            max(0.0, m["ric_tan_max"] - 1.1),
        ]
        penalty = 1e6 * sum(v * v for v in violations)
        # small roughness penalty prevents hiding huge oscillations between grid points
        rough = 10.0 * sum(float(a * a) for a in x[1:])
        return m["volume"] + penalty + rough

    L0 = math.pi * math.sqrt(3.0)
    bounds = [(0.90 * L0, 1.10 * L0)] + [(-0.35, 0.35)] * modes
    result = differential_evolution(
        objective,
        bounds=bounds,
        tol=1e-7,
        maxiter=50,
        popsize=10,
        seed=2606,
        polish=False,
        updating="immediate",
        workers=1,
    )
    local = minimize(objective, result.x, method="Nelder-Mead", options={"maxiter": 2000, "xatol": 1e-10, "fatol": 1e-8})
    best = local.x if local.fun <= result.fun else result.x
    best_metrics = rotational_s4_metrics(best, ngrid=2400)
    feasible = best_metrics["delta_plus_sup"] <= delta_target + 5e-3
    return {
        "available": True,
        "ansatz": "SO(4)-invariant warped product dr^2 + f(r)^2 g_{S^3}, f=(L/pi)sin(pi r/L)exp(sum a_k sin^2(k pi r/L))",
        "delta_target": delta_target,
        "modes": modes,
        "round_metrics": round_metrics,
        "best_metrics_refined_grid": best_metrics,
        "feasible_with_tolerance": bool(feasible),
        "optimizer": {
            "differential_evolution_fun": float(result.fun),
            "local_fun": float(local.fun),
            "success": bool(result.success or local.success),
            "message_de": str(result.message),
            "message_local": str(local.message),
        },
        "interpretation": "Within this small smooth rotational ansatz and search budget, no low-volume metric with Ricci eigenvalues in [0.9,1.1] was found if best volume stays near the round 24π² value. This is heuristic only.",
    }


def main():
    out = {
        "kk_obstruction": kk_obstruction_constants(),
        "normalizations": normalization_constants(),
        "rotational_S4_search": run_rotational_search(delta_target=0.1, modes=3),
    }
    path = DATA / "step6_positive_collapse_probes.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("Step 6 positive-branch collapse probes")
    print("=" * 72)
    kk = out["kk_obstruction"]
    print(f"Free S^1 Kaluza-Klein Bochner threshold δ >= {kk['quantitative_delta_threshold_under_recorded_constants']:.9f}")
    for s in kk["samples"]:
        print(
            f"  δ={s['delta']:.6f}: lower={s['bochner_lower_per_base_volume']:.6f}, "
            f"upper={s['mixed_error_upper_per_base_volume']:.6f}, "
            f"contradiction={s['contradiction_if_lower_exceeds_upper']}"
        )
    norm = out["normalizations"]["round_S4_normalized_Ric_equals_g"]
    print(f"Round S^4 Ric=g radius={norm['radius']:.9f}, Vol={norm['volume']:.9f} = {norm['volume_as_multiple_pi2']:.6f}π²")
    print(f"CGB sharp: beta(0)*Vol={norm['beta0_times_volume']:.9f}, 8π²χ={norm['8pi2_chi']:.9f}")
    eh = out["normalizations"]["ALE_Ricci_flat_energy_quantum"]["Eguchi_Hanson"]
    print(f"Eguchi-Hanson ALE energy={eh['energy']:.9f} = {eh['energy_as_multiple_pi2']:.6f}π²")
    rs = out["rotational_S4_search"]
    if rs.get("available"):
        bm = rs["best_metrics_refined_grid"]
        rm = rs["round_metrics"]
        print("Rotational S^4 ansatz search (heuristic):")
        print(f"  round δ={rm['delta_plus_sup']:.6e}, Vol={rm['volume']:.9f}")
        print(f"  best δ={bm['delta_plus_sup']:.6f}, Vol={bm['volume']:.9f}, Vol/round={bm['volume_over_round']:.6f}")
        print(f"  best Ric_rad=[{bm['ric_rad_min']:.6f},{bm['ric_rad_max']:.6f}], Ric_tan=[{bm['ric_tan_min']:.6f},{bm['ric_tan_max']:.6f}]")
        print(f"  best L={bm['L']:.9f}, coeffs={bm['coeffs']}")
    else:
        print(f"Rotational search skipped: {rs.get('error')}")
    print(f"Saved JSON to {path}")


if __name__ == "__main__":
    main()
