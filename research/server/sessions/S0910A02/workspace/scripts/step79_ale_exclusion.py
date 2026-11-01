#!/usr/bin/env python3
"""
Step 79: ALE exclusion from CGB energy budget.

For chi=8 mixed rows under collapse, the outermost ALE bubble 
must fit within the CGB energy budget 64 pi^2. 
The CGB-ALE formula (Hitchin, Nakajima):
  int|W|^2 = 8 pi^2 (chi_top - 1/|Gamma|)
where chi_top = 1 + rank for the crepant resolution.

Combined with the transition-scale theorem (AVR <= eps, |Gamma| >= 1/eps),
this EXCLUDES ALE outermost models for sufficiently small eps.

We compute the exact threshold.
"""
import json, os, math
from fractions import Fraction

pi2 = math.pi**2
chi_total = 8
energy_budget = 8 * chi_total  # in units of pi^2

# ADE classification with group orders
# A_k: rank k, |Gamma| = k+1, chi = k+1
# D_k (k>=4): rank k, |Gamma| = 4(k-2), chi = k+1
# E_6: rank 6, |Gamma| = 24, chi = 7
# E_7: rank 7, |Gamma| = 48, chi = 8
# E_8: rank 8, |Gamma| = 120, chi = 9

ade_data = []

# A-series
for k in range(1, 20):
    rank = k
    gamma_order = k + 1
    chi = k + 1
    energy = Fraction(chi * gamma_order - 1, gamma_order) * 8
    ade_data.append({
        "type": f"A_{k}",
        "rank": rank,
        "gamma_order": gamma_order,
        "chi_top": chi,
        "energy_pi2": float(energy),
        "energy_exact": str(energy),
        "fits_budget": float(energy) <= energy_budget,
        "avr": 1.0/gamma_order,
    })

# D-series (k >= 4)
for k in range(4, 15):
    rank = k
    gamma_order = 4*(k - 2)
    chi = k + 1
    energy = Fraction(chi * gamma_order - 1, gamma_order) * 8
    ade_data.append({
        "type": f"D_{k}",
        "rank": rank,
        "gamma_order": gamma_order,
        "chi_top": chi,
        "energy_pi2": float(energy),
        "energy_exact": str(energy),
        "fits_budget": float(energy) <= energy_budget,
        "avr": 1.0/gamma_order,
    })

# E-series
for name, rank, gamma_order in [("E_6", 6, 24), ("E_7", 7, 48), ("E_8", 8, 120)]:
    chi = rank + 1
    energy = Fraction(chi * gamma_order - 1, gamma_order) * 8
    ade_data.append({
        "type": name,
        "rank": rank,
        "gamma_order": gamma_order,
        "chi_top": chi,
        "energy_pi2": float(energy),
        "energy_exact": str(energy),
        "fits_budget": float(energy) <= energy_budget,
        "avr": 1.0/gamma_order,
    })

# Find all ADE types that fit the budget AND have chi_top <= chi_total
feasible = [d for d in ade_data if d["fits_budget"] and d["chi_top"] <= chi_total]
infeasible_energy = [d for d in ade_data if not d["fits_budget"]]
infeasible_chi = [d for d in ade_data if d["fits_budget"] and d["chi_top"] > chi_total]

max_gamma_feasible = max(d["gamma_order"] for d in feasible) if feasible else 0
min_avr_feasible = min(d["avr"] for d in feasible) if feasible else 1.0

# The exact threshold: eps < 1/max_gamma => no ALE fits
eps_threshold = 1.0 / max_gamma_feasible if max_gamma_feasible > 0 else 0

# Report the maximizers
maximizers = [d for d in feasible if d["gamma_order"] == max_gamma_feasible]

# Energy remaining after each feasible type
for d in feasible:
    d["energy_remaining_pi2"] = energy_budget - d["energy_pi2"]
    d["max_inner_rank"] = int(d["energy_remaining_pi2"] / 8)  # rough bound

results = {
    "chi_total": chi_total,
    "energy_budget_pi2": energy_budget,
    "feasible_count": len(feasible),
    "max_gamma_feasible": max_gamma_feasible,
    "min_avr_feasible": round(min_avr_feasible, 6),
    "eps_threshold": round(eps_threshold, 6),
    "maximizer_type": maximizers[0]["type"] if maximizers else None,
    "maximizer_details": maximizers[0] if maximizers else None,
    "theorem": (
        f"For eps < 1/{max_gamma_feasible} = {round(eps_threshold,6)}, "
        f"no hyper-Kahler ALE 4-manifold can serve as the outermost "
        f"model in a collapsing near-positive-Einstein sequence on a "
        f"chi={chi_total} mixed row."
    ),
    "feasible_types": [
        {"type": d["type"], "rank": d["rank"], "|Gamma|": d["gamma_order"],
         "chi": d["chi_top"], "energy_pi2": round(d["energy_pi2"], 4),
         "avr": round(d["avr"], 6), "remaining_pi2": round(d["energy_remaining_pi2"], 4)}
        for d in sorted(feasible, key=lambda x: -x["gamma_order"])[:10]
    ],
    "first_excluded": [
        {"type": d["type"], "rank": d["rank"], "|Gamma|": d["gamma_order"],
         "chi": d["chi_top"], "energy_pi2": round(d["energy_pi2"], 4),
         "reason": "energy exceeds budget" if not d["fits_budget"] else "chi exceeds total"}
        for d in sorted(infeasible_energy + infeasible_chi, 
                       key=lambda x: x["gamma_order"])[:5]
    ],
}

outpath = "Sessions/S0910A02/workspace/data/step79_ale_exclusion.json"
os.makedirs(os.path.dirname(outpath), exist_ok=True)
with open(outpath, "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps({
    "output": outpath,
    "max_Gamma_feasible": max_gamma_feasible,
    "eps_threshold": round(eps_threshold, 6),
    "maximizer": maximizers[0]["type"] if maximizers else None,
    "maximizer_energy_pi2": round(maximizers[0]["energy_pi2"], 4) if maximizers else None,
    "E8_energy_pi2": round(next(d["energy_pi2"] for d in ade_data if d["type"]=="E_8"), 4),
    "E8_fits": next(d["fits_budget"] for d in ade_data if d["type"]=="E_8"),
}, indent=2))
