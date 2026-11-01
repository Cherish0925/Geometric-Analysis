#!/usr/bin/env python3
"""
Step 22: Collapse Sobolev and downstream-scope audit for the negative cutoff-flow route.

This script records simple scale checks used by the Preceptor audit.
It is not a proof of any geometric PDE theorem.  It verifies two model facts:

1. On a one-dimensionally collapsed 4D product S^1_ell x B^3, a downstairs
   L^4 Sobolev constant for fiber-independent test functions degenerates at
   least like ell^{-1/4}.  Thus dimension-only downstairs Sobolev constants are
   false in collapsed regions.

2. For a constant-curvature/constant-|Rm| collapsed model with volume proportional
   to ell, the unweighted local L^2 curvature energy tends to zero, but the
   critical Sobolev product A^2 ||Rm||_2 stays O(1).  Collapse-neutral estimates
   must carry this product or an equivalent lifted noncollapsing hypothesis.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

SESSION = Path("Sessions/S0910A02")
OUT = SESSION / "workspace/data/step22_collapse_sobolev_and_scope_audit.json"

# Model: M_ell = S^1_ell x B^3(1), u(theta,x)=f(x).
# Norms scale by the fiber length ell:
#   ||u||_4 = ell^{1/4} ||f||_{L4(B3)}
#   ||grad u||_2 = ell^{1/2} ||grad f||_{L2(B3)}
# Hence Sobolev ratio ||u||_4/||grad u||_2 scales as ell^{-1/4}.
# If a lower-order r^{-1}||u||_2 term is included, it scales as ell^{1/2};
# for nonconstant f with a fixed ratio on B3 the same ell^{-1/4} lower bound
# remains for the gradient-dominated quotient after subtracting/normalizing constants.

def sobolev_ratio_scaling(ell: float) -> float:
    return ell ** (-0.25)

# Constant curvature normalized Ric=-g in dimension 4 has sectional curvature k=-1/3.
# |Rm|^2 = 2 n(n-1) k^2 = 24/9 = 8/3 under the common convention.
n = 4
k = -1 / 3
rm_sq = 2 * n * (n - 1) * k * k
rm_norm = math.sqrt(rm_sq)

# Let a local collapsed ball have volume C_vol * ell at fixed base radius.
C_vol = 1.0

rows = []
for ell in [1.0, 1e-1, 1e-2, 1e-4, 1e-6, 1e-8]:
    V = C_vol * ell
    L2_energy = rm_sq * V
    L2_norm = rm_norm * math.sqrt(V)
    A_lower = sobolev_ratio_scaling(ell)
    critical_product = A_lower**2 * L2_norm
    rows.append({
        "ell": ell,
        "sobolev_A_lower_relative_to_ell1": A_lower,
        "unweighted_L2_energy_Rm2": L2_energy,
        "L2_norm_Rm": L2_norm,
        "A_lower_squared_times_L2_norm": critical_product,
    })

# Hyperbolic cusp/Margulis-tube moral: exact E=0 and bounded |Rm| with V->0.
hyperbolic_model = {
    "dimension": n,
    "sectional_curvature_for_Ric_minus_g": k,
    "Rm_norm_squared": rm_sq,
    "Einstein_defect_E": 0,
    "downstairs_energy_as_volume_collapses": "int |Rm|^2 = (8/3) Vol -> 0",
    "audit_consequence": (
        "Any claim using only small unweighted downstairs L2 curvature energy to get "
        "dimension-only pointwise curvature control is false in collapsed regions. "
        "A scale-adapted claim may survive only if it keeps the Sobolev factor A^2 "
        "or works on an accessible noncollapsed cover with controlled mean transport."
    ),
}

# Downstream scope logic if the A01/A03 zero-order lemma were proved.
downstream_scope = {
    "granting_zero_order_weighted_moser": [
        "On plateau regions one obtains bounded curvature at positive time and small Ric+g.",
        "For critical Ishida-LeBrun 4-manifolds, Chern-Weil + monopole estimates give a 7/24 L2 Weyl-calibration inequality from small global L2 defect.",
        "A contradiction requires transporting that calibration to a noncollapsed local limit; in collapsed charts this needs a local mean-transfer/noncollapsing-cover hypothesis, not just global L2 smallness.",
        "The conclusion, if all transport and localization issues are solved, is a fixed-topology or standard-subclass uniform negative pinching gap for those Ishida-LeBrun 4-manifolds only.",
    ],
    "does_not_follow": [
        "No proof of the unrestricted four-dimensional negative branch P_4^-.",
        "No proof of the positive branch P_4^+.",
        "No mechanism for n>=5, because the L2-critical Sobolev exponent and Chern-Weil/Seiberg-Witten calibration are four-dimensional.",
        "No Min-Oo endpoint: exact large-diameter hyperbolic manifolds have Ric=-g and unbounded diameter*curvature scale while already Einstein.",
    ],
}

result = {
    "title": "Step 22 collapse Sobolev and downstream-scope audit",
    "thin_product_model": "S^1_ell x B^3 with fiber-independent test functions",
    "norm_scaling": {
        "L4_norm": "||u||_4 = ell^(1/4)||f||_4",
        "gradient_L2_norm": "||grad u||_2 = ell^(1/2)||grad f||_2",
        "sobolev_constant_lower_bound": "A_ell >= c ell^(-1/4)",
    },
    "hyperbolic_constant_curvature_model": hyperbolic_model,
    "scale_table": rows,
    "downstream_scope_if_lemma_granted": downstream_scope,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
print(f"Saved {OUT}")
