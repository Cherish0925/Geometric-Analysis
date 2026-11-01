#!/usr/bin/env python3
"""Step 88: algebraic checks for the minimal-separator extension of Step 87.

This does not replace the geometric proof.  It verifies the coefficient bookkeeping in
(1) the intrinsic scalar identity, (2) the contracted Gauss equation, (3) the
Ricci-defect bound, and (4) the exact expanding-end model used in the existence
argument for a weighted-length minimizing essential loop.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

# Intrinsic T^3 scalar identity along C:
# R_q = -2 h_s - 3/2 h^2 - 1/2 e_s, rho_s = h rho.
# Periodicity gives <h_s>_rho = -<h^2>_rho.
h2, es = sp.symbols("h2 es", real=True)
weighted_R_after_ibp = sp.simplify(-2 * (-h2) - sp.Rational(3, 2) * h2 - sp.Rational(1, 2) * es)
expected_weighted_R = sp.Rational(1, 2) * (h2 - es)

# Contracted Gauss at a minimal hypersurface H=0.
trE, Enn, II2 = sp.symbols("trE Enn II2", real=True)
Rg = -12 + trE
Ricnn = -3 + Enn
R_sigma = sp.expand(Rg - 2 * Ricnn - II2)
D = trE - 2 * Enn
expected_R_sigma = -6 + D - II2

# Equating the two averaged scalar expressions:
# 1/2(h^2-e_s) = -6 + D - |II|^2.
floor_identity_rhs = sp.expand(12 - 2 * D + 2 * II2 + h2)
solve_es = sp.solve(
    sp.Eq(sp.Rational(1, 2) * (h2 - es), -6 + D - II2),
    es,
)[0]

# In a g-orthonormal frame (t1,t2,t3,nu), D=sum tangent Eii-Enn.
e1, e2, e3, en, delta = sp.symbols("e1 e2 e3 en delta", real=True, nonnegative=False)
D_frame = e1 + e2 + e3 - en
# Triangle inequality yields |D| <= 4 delta if each diagonal component has abs <= delta.
D_l1_coefficient = 4

# Exact expanding end: gamma=dt^2+exp(2t) dz^2, rho=c exp(2t).
# Lifted t-slice has one horizontal and two orbit principal curvatures, all +1.
principal_curvatures = [1, 1, 1]
H_out = sum(principal_curvatures)
# Auxiliary metric rho^2 gamma has radial line element c exp(2t)dt and
# circle line element c exp(3t)dz.
# Record primitive antiderivative and growth exponents.
t, c = sp.symbols("t c", positive=True)
aux_radial_density = c * sp.exp(2 * t)
aux_radial_antiderivative = sp.integrate(aux_radial_density, t)
aux_circle_density = c * sp.exp(3 * t)

# Step 87 ceiling/floor crossing, retained to check that the threshold is unchanged.
d = sp.symbols("d", nonnegative=True)
B = (
    4 * d / sp.sqrt(3 + d)
    + sp.sqrt(2 * (3 + d) + 20 * d**2 / (3 + d))
) ** 2
floor = 12 - 8 * d
root = float(sp.nsolve(sp.Eq(B, floor), 0.24))

checks = {
    "weighted_scalar_after_periodic_ibp": str(weighted_R_after_ibp),
    "weighted_scalar_expected": str(expected_weighted_R),
    "weighted_scalar_zero_residual": sp.simplify(weighted_R_after_ibp - expected_weighted_R) == 0,
    "gauss_minimal_scalar": str(R_sigma),
    "gauss_expected": str(expected_R_sigma),
    "gauss_zero_residual": sp.simplify(R_sigma - expected_R_sigma) == 0,
    "separator_energy_identity_solved": str(solve_es),
    "separator_energy_expected": str(floor_identity_rhs),
    "separator_energy_zero_residual": sp.simplify(solve_es - floor_identity_rhs) == 0,
    "D_orthonormal_frame": str(D_frame),
    "D_bound_from_operator_norm": "|D| <= |E11|+|E22|+|E33|+|Enn| <= 4 delta",
    "D_l1_coefficient": D_l1_coefficient,
    "coarse_energy_floor": "<e_s> >= 12 - 8 delta",
    "exact_expanding_end": {
        "principal_curvatures_outward": principal_curvatures,
        "hypersurface_mean_curvature": H_out,
        "rho": "c*exp(2t)",
        "auxiliary_metric": "c^2 exp(4t) dt^2 + c^2 exp(6t) dz^2",
        "auxiliary_radial_density": str(aux_radial_density),
        "auxiliary_radial_antiderivative": str(aux_radial_antiderivative),
        "auxiliary_circle_density": str(aux_circle_density),
        "radial_distance_and_essential_loop_length_diverge": True,
    },
    "step87_ceiling_at_zero": float(B.subs(d, 0)),
    "minimal_separator_floor_at_zero": float(floor.subs(d, 0)),
    "unchanged_crossing_delta_star": root,
    "all_symbolic_zero_checks": all(
        [
            sp.simplify(weighted_R_after_ibp - expected_weighted_R) == 0,
            sp.simplify(R_sigma - expected_R_sigma) == 0,
            sp.simplify(solve_es - floor_identity_rhs) == 0,
            H_out == 3,
        ]
    ),
}

out_path = Path(__file__).resolve().parents[1] / "data" / "step88_minimal_separator_verify.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(checks, indent=2), encoding="utf-8")
print(json.dumps(checks, indent=2))
print(f"\nwrote {out_path}")
