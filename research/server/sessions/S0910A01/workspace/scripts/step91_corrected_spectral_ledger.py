#!/usr/bin/env python3
"""
Step 91: corrected product spectral ledger for the K-odd calculation.

This replaces the flawed enumeration in step90_K_odd_spectral_analysis.py while
preserving the useful conclusion P>=1 on the K-odd quotient-descending tensor
sector.  The corrections are:
  * quotient descent for the generator r_pi is by azimuthal m parity, not ell;
  * AA/BB factor trace-free tensors have P=(lambda_factor+lambda_other)/2-1,
    so the minimum factor-TF value is 2 at (ell,m)=(2,2), not 4;
  * ell_A and ell_B remain independent; factor interchange is a symmetry, not
    a summation restriction.
"""
from __future__ import annotations

import json
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def lam(l: int) -> int:
    return l * (l + 1)


def p_scalar(lA: int, lB: int) -> float:
    return 0.5 * (lam(lA) + lam(lB)) - 1


def p_ab(lA: int, lB: int) -> float:
    return 0.5 * (lam(lA) + lam(lB)) - 1


def p_factor_tf(l_tf: int, l_other: int) -> float:
    return 0.5 * (lam(l_tf) + lam(l_other)) - 1


rows = []
# Scalar/trace blocks: record only low K-odd quotient possibilities.
for lA in range(0, 6):
    for mA in range(0, lA + 1):
        for lB in range(0, 6):
            for mB in range(0, lB + 1):
                desc = ((mA + mB) % 2 == 0)
                if not desc:
                    continue
                # K acts on first factor by reflection.  For mA=0 there is only cos/even.
                # For mA>0 the sin real harmonic is K-odd and cos is K-even.
                has_kodd_scalar = mA > 0
                if has_kodd_scalar:
                    rows.append({
                        "sector": "scalar_trace_block_candidate",
                        "lA": lA,
                        "mA": mA,
                        "lB": lB,
                        "mB": mB,
                        "P_formula": "0.5*(lambda_A+lambda_B)-1",
                        "P": p_scalar(lA, lB),
                        "descends_by_m_parity": True,
                        "K_odd_real_component": "sin(m_A phi_A) component",
                    })

# Factor trace-free tensors: the K-odd quotient minimum occurs already at ell=2, m=2.
for l in range(2, 7):
    for m in range(0, l + 1):
        if m % 2 != 0:
            continue
        # Tensor harmonics have both reflection parities when m>0; m=0 has even pieces.
        has_kodd = m > 0
        if has_kodd:
            rows.append({
                "sector": "AA_or_BB_factor_tracefree",
                "l_factor": l,
                "m_factor": m,
                "l_other": 0,
                "m_other": 0,
                "P_formula": "0.5*(lambda_factor+lambda_other)-1",
                "P": p_factor_tf(l, 0),
                "descends_by_m_parity": True,
                "rough_eigenvalue_factor": lam(l) - 4,
                "Rcirc_on_TF": -1,
            })

# Mixed one-form sector minima with independent degrees.
for lA in range(1, 6):
    for mA in range(0, lA + 1):
        for lB in range(1, 6):
            for mB in range(0, lB + 1):
                if (mA + mB) % 2 != 0:
                    continue
                # K-odd components exist either from coexact cos/even A modes or exact sin/odd A modes.
                kodd_options = []
                if mA == 0:
                    kodd_options.append("A coexact m=0")
                else:
                    kodd_options.extend(["A coexact cos", "A exact sin"])
                rows.append({
                    "sector": "AB_oneform_product",
                    "lA": lA,
                    "mA": mA,
                    "lB": lB,
                    "mB": mB,
                    "P_formula": "0.5*(lambda_A+lambda_B)-1",
                    "P": p_ab(lA, lB),
                    "descends_by_m_parity": True,
                    "K_odd_options_on_A": kodd_options,
                })

# Extract low minima.
low_by_sector = {}
for r in rows:
    sec = r["sector"]
    if sec not in low_by_sector or r["P"] < low_by_sector[sec]["P"]:
        low_by_sector[sec] = r

results = {
    "step": 91,
    "scope": "corrected spectral ledger for K-odd quotient-descending product tensors",
    "corrected_rules": {
        "quotient_generator": "r_pi rotates each sphere by phi -> phi+pi; scalar and derived tensor modes transform by (-1)^m, so descent uses m_A+m_B parity, not ell_A+ell_B.",
        "factor_tracefree_formula": "rough eigenvalue ell(ell+1)-4 and Rcirc=-1 give P=(ell_factor(ell_factor+1)+ell_other(ell_other+1))/2 - 1; minimum K-odd quotient value is 2 at ell=2,m=2,l_other=0.",
        "independent_degrees": "ell_A and ell_B are independent; factor interchange only relates coefficients after summing or comparing symmetry-related node pairs.",
        "mixed_oneform_formula": "P=(ell_A(ell_A+1)+ell_B(ell_B+1))/2 - 1 with ell_A,ell_B>=1; minimum is 1 at (1,1).",
        "scalar_nonpositive_modes": "constant negative trace/shape directions and l=1 scalar zero modes are K-even or do not descend in their K-odd real components; they do not enter the K-odd quotient source sector.",
    },
    "low_minima_by_sector": low_by_sector,
    "lowest_rows_overall": sorted(rows, key=lambda r: (r["P"], r["sector"]))[:20],
    "conclusion": "The Step90 lower bound P>=1 on the K-odd quotient tensor sector survives, but the enumeration and factor-TF minimum in step90_K_odd_spectral_analysis.py were incorrect. The actual low K-odd sector starts with AB one-form products at P=1 and factor trace-free products at P=2.",
}

outpath = DATA_DIR / "step91_corrected_spectral_ledger.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps(results, indent=2))
print(f"Wrote {outpath}")
