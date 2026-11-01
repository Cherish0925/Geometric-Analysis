#!/usr/bin/env python3
"""Step 68 supplemental kernel ledger for the product orbifold.

The Ozuch/LeBrun-Ozuch operator in Bianchi gauge is
    P = 1/2 nabla^* nabla - R^circ
on all symmetric two-tensors, while the usual infinitesimal Einstein deformation
(IED) space is the TT kernel.  On a positive product with sphere factors these
two ledgers differ: scalar eigenfunctions with Delta f=2 Lambda give P-kernel
tensors, but the TT kernel on CP^1 x CP^1 is zero.  This distinction matters for
which finite-dimensional variables enter the obstruction problem and which ones
are only gauge/automorphism/normalization directions.
"""
from __future__ import annotations

import json
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step68_orbifold_kernel_full_vs_tt.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

# Quotient action rho(z,w)=(-z,-w): on l=1 real harmonics of each factor
# (x,y,z), the pi-rotation acts diag(-1,-1,+1).  For product scalar eigenvalue
# 2 Lambda, only one factor has l=1 and the other is constant.  Hence invariant
# multiplicity is 1+1=2.
scalar_l1_cover_per_factor = 3
scalar_l1_invariant_per_factor = 1
scalar_lambda_2Lambda_invariant_total = 2

# For each invariant f with Delta f = 2 Lambda, the full gauged operator P kills
# f*g1 and f*g2.  Direct check:
# P(f*g_a) = 1/2(2 Lambda) f*g_a - Rcirc(f*g_a) = Lambda f*g_a - Lambda f*g_a.
# Thus full P-kernel scalar sector has 2 tensors per invariant f.
full_scalar_kernel_dim = 2 * scalar_lambda_2Lambda_invariant_total

# TT check for the same scalar sector.  If f is on factor 1, the most general
# scalar-sector tensor after including Hess f is A f g1 + B f g2 because on S^2
# Hess f=-Lambda f g1 for first harmonics.  Trace-free gives A+B=0, while
# divergence-free gives A=0, hence B=0.  Same for factor 2.
TT_scalar_kernel_dim = 0
TT_factor_kernel_dim = 0  # CP^1 has no holomorphic quadratic differentials / TT IEDs.
TT_mixed_kernel_dim = 0   # mixed one-form sector is strictly positive.
TT_total_kernel_dim = 0

# Relative factor scaling h=g1-g2 is TT and invariant but not kernel.  In Ozuch P
# convention P h = -Lambda h; in Kroencke Delta_E=2P convention, Delta_E h=-2Lambda h.
# This is the bounded-away-from-zero unstable mode.
relative_mode = {
    "tensor": "h_rel=g1-g2",
    "TT": True,
    "rho_invariant": True,
    "P_eigenvalue_over_Lambda_Ozuch": -1,
    "Delta_E_eigenvalue_over_Lambda_Kroencke": -2,
    "not_kernel": True,
}

result = {
    "operator_conventions": {
        "Ozuch_P": "1/2*nabla^*nabla - R^circ (linearization of Ric-Lambda g plus Bianchi gauge)",
        "Kroencke_Delta_E": "nabla^*nabla - 2 R^circ = 2*Ozuch_P on Einstein backgrounds",
        "important_factor_warning": "A claimed P(h_rel)=-4Lambda h_rel is not the Ozuch or Kroencke convention used in the cited sources; with Ric=Lambda g it is P=-Lambda and Delta_E=-2Lambda.",
    },
    "quotient_action": {
        "rho": "(z,w)->(-z,-w), a pi-rotation in each CP^1 coordinate, with four fixed nodes (0/∞,0/∞)",
        "l1_harmonic_action_each_factor": "diag(-1,-1,+1)",
        "lambda_2Lambda_scalar_invariant_multiplicity": scalar_lambda_2Lambda_invariant_total,
    },
    "full_P_kernel_scalar_sector": {
        "dimension": full_scalar_kernel_dim,
        "basis_schematic": ["z1*g1", "z1*g2", "z2*g1", "z2*g2"],
        "meaning": "kernel of the gauged operator on all symmetric 2-tensors; these are scalar/conformal/gauge/automorphism-type directions, not TT Einstein deformations",
    },
    "TT_kernel": {
        "scalar_sector_dimension": TT_scalar_kernel_dim,
        "factor_TT_dimension": TT_factor_kernel_dim,
        "mixed_sector_dimension": TT_mixed_kernel_dim,
        "total_dimension": TT_total_kernel_dim,
        "direct_l1_check": "for f on one factor, Hess f=-Lambda f g_factor; trace-free gives A+B=0 and divergence-free gives A=0, so the scalar l=1 kernel contributes no TT tensor",
        "quotient_argument": "any quotient TT kernel lifts to a rho-invariant TT kernel on the cover; cover TT kernel is zero",
    },
    "relative_mode": relative_mode,
    "consequence_for_obstruction_program": "The TT infinitesimal Einstein deformation space is zero, so there is no small TT kernel amplification.  However the full gauged P-kernel has a 4-dimensional scalar sector on the orbifold quotient; a faithful Ozuch implementation must either quotient/fix these automorphism-normalization directions or include the corresponding v_l variables/projections.  Bubble parameters are not literally the only variables until this gauge issue is fixed.",
}

OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps({
    "output": str(OUT),
    "full_P_kernel_scalar_dim": full_scalar_kernel_dim,
    "TT_kernel_dim": TT_total_kernel_dim,
    "h_rel_P_eigen_over_Lambda": -1,
}, indent=2))
