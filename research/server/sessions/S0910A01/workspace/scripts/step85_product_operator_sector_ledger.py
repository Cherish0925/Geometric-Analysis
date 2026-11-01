#!/usr/bin/env python3
"""
Step 85: product Lichnerowicz sector ledger for S^2 x S^2.

This turns the Strategist warning into an explicit operator block model.  The
full symmetric 2-tensor space is not a nine-dimensional TT sector.  On a product
of unit 2-spheres, decompose tensors into:
  AA block: symmetric 2-tensors along factor A times scalar harmonics on B;
  BB block: scalar harmonics on A times symmetric 2-tensors along factor B;
  AB block: one-form harmonics on A tensor one-form harmonics on B.
On each S^2, symmetric 2-tensors further split into trace, scalar trace-free
Hessian, and vector trace-free sectors.  This script records rough Laplacian
and curvature-action eigenvalues and hence P = 1/2 ∇*∇ - R° denominators.
"""
import json
from pathlib import Path

OUT = Path("Sessions/S0910A01/workspace/data/step85_product_operator_sector_ledger.json")

def lam(l): return l*(l+1)

def P_AA(lA, lB, one_factor_sector):
    # h_AA sector on factor A, scalar lB on factor B.
    # R° eigen on AA: +1 for trace, -1 for trace-free.
    if one_factor_sector == "trace":
        roughA = lam(lA)
        Rcirc = 1
        valid = lA >= 0
    elif one_factor_sector in ("scalar_TF_Hessian", "vector_TF"):
        roughA = lam(lA) - 4
        Rcirc = -1
        valid = lA >= 2
    else:
        raise ValueError(one_factor_sector)
    return {"valid": valid, "rough": roughA + lam(lB), "Rcirc": Rcirc, "P": 0.5*(roughA + lam(lB)) - Rcirc}

def P_BB(lA, lB, one_factor_sector):
    # scalar lA on A, tensor sector on B.
    if one_factor_sector == "trace":
        roughB = lam(lB)
        Rcirc = 1
        valid = lB >= 0
    elif one_factor_sector in ("scalar_TF_Hessian", "vector_TF"):
        roughB = lam(lB) - 4
        Rcirc = -1
        valid = lB >= 2
    else:
        raise ValueError(one_factor_sector)
    return {"valid": valid, "rough": lam(lA) + roughB, "Rcirc": Rcirc, "P": 0.5*(lam(lA) + roughB) - Rcirc}

def P_AB(lA, lB, A_oneform="exact", B_oneform="exact"):
    # one-form rough eigenvalue on unit S2: λ_l - 1 for l>=1, exact or coexact.
    valid = lA >= 1 and lB >= 1
    rough = (lam(lA) - 1) + (lam(lB) - 1)
    return {"valid": valid, "rough": rough, "Rcirc": 0, "P": 0.5*rough}

rows = []
for lA in range(0, 6):
    for lB in range(0, 6):
        for sec in ["trace", "scalar_TF_Hessian", "vector_TF"]:
            r = P_AA(lA, lB, sec)
            if r["valid"]:
                rows.append({"block": "AA", "sector": sec, "lA": lA, "lB": lB, **r})
            r = P_BB(lA, lB, sec)
            if r["valid"]:
                rows.append({"block": "BB", "sector": sec, "lA": lA, "lB": lB, **r})
        r = P_AB(lA, lB)
        if r["valid"]:
            rows.append({"block": "AB", "sector": "oneform_x_oneform (exact/coexact variants)", "lA": lA, "lB": lB, **r})

zero_modes = [r for r in rows if abs(r["P"]) < 1e-12]
negative_modes = [r for r in rows if r["P"] < -1e-12]
lowest_positive = sorted([r for r in rows if r["P"] > 1e-12], key=lambda r: r["P"])[:20]

result = {
    "scope": "sector denominator ledger for P=1/2 rough - Rcirc on product S^2(unit)xS^2(unit)",
    "formulas": {
        "scalar_eigenvalue": "lambda_l=l(l+1)",
        "oneform_rough": "lambda_l-1 for l>=1 (exact or coexact)",
        "S2_symmetric_trace_rough_Rcirc": "rough=lambda_l, Rcirc=+1 on f*g_factor",
        "S2_symmetric_TF_rough_Rcirc": "rough=lambda_l-4 for l>=2 on scalar-TF-Hessian and vector-TF sectors, Rcirc=-1",
        "AA_or_BB_P_eigenvalue": "0.5*(lambda_A+lambda_B)-1 for trace and TF tensor sectors after valid l restrictions",
        "AB_P_eigenvalue": "0.5*(lambda_A+lambda_B-2) for oneform x oneform, lA,lB>=1",
    },
    "zero_modes_l_le_5": zero_modes,
    "negative_modes_l_le_5": negative_modes,
    "lowest_positive_l_le_5": lowest_positive,
    "interpretation": {
        "four_scalar_kernel_modes": "AA/BB trace sectors with (lA,lB)=(1,0) or (0,1): u_A g_A, u_B g_A, u_A g_B, u_B g_B all have P=0.",
        "negative_shape_and_scale_modes": "constant trace blocks have P=-1; linear combinations include g_A-g_B and g_A+g_B in the fixed-Einstein-constant operator.",
        "mixed_oneform_gap": "AB lA=lB=1 has P=1, matching the corrected mixed 1-form spectral gap Λ for unit spheres.",
        "why_Cab_not_enough": "The pointwise C_ab matrices split into AA, BB, and AB pieces; global propagation uses these sector denominators and derived-harmonic source factors, not one common 9D TT eigenvalue."
    },
    "rows_l_le_5": rows,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2))
print(json.dumps({
    "output": str(OUT),
    "zero_modes": zero_modes,
    "negative_modes": negative_modes[:8],
    "lowest_positive": lowest_positive[:8],
    "formulas": result["formulas"],
}, indent=2))
print(f"Wrote {OUT}")
