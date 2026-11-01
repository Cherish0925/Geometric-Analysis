#!/usr/bin/env python3
"""Step 86: exact algebra checks for the forced OT Bochner superlevel estimate.

This script verifies:
  * the natural reaction root k_*;
  * the factorization at k_*;
  * the Kato-enhanced gradient coefficient;
  * the operator-norm conversion |F| <= 2 delta from the traceless 2x2
    orbit Ricci defect in the normalization |X|_{H^2}^2 = tr(X^2)/2;
  * a scalar constant-energy ball model showing why a local ceiling must
    retain the ball-radius / boundary-data scale.

It is algebraic verification, not a proof of the geometric Sobolev theory.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

# Symbols
b, f, u = sp.symbols("b f u", nonnegative=True)
e = sp.symbols("e", positive=True)

# Psi(e) = 1/2 e(e-6) - b e - f^2.
S = sp.sqrt((3 + b) ** 2 + 2 * f**2)
k_star = 3 + b + S
k_minus = 3 + b - S
Psi = sp.Rational(1, 2) * e * (e - 6) - b * e - f**2
factor_residual = sp.simplify(Psi - sp.Rational(1, 2) * (e-k_star) * (e-k_minus))
at_root_residual = sp.simplify(Psi.subs(e, k_star))
reaction_at_root = sp.expand(u * Psi.subs(e, k_star + u))
reaction_target = S*u**2 + sp.Rational(1, 2)*u**3
reaction_residual = sp.simplify(reaction_at_root - reaction_target)

# Kato-enhanced coefficient for grad u when u=e-k.
k = sp.symbols("k", nonnegative=True)
a_k = sp.simplify(sp.Rational(1, 2) + (e-k)/(4*e))
a_k_target = (3*e-k)/(4*e)

# Orbit forcing conversion. E0 has eigenvalues (+a,-a), |a|<=delta.
a, delta = sp.symbols("a delta", nonnegative=True)
tr_E0_sq = 2*a**2
F_sq = sp.simplify(2*tr_E0_sq)  # |-2E0|_H^2 = 1/2 tr(4E0^2)
F_norm = 2*a

# Scalar local model on a Euclidean two-ball:
# e=H, W=1/2 H(H-6), V=-c x, div V=-2c.
H, f0, R = sp.symbols("H f0 R", positive=True)
W = sp.Rational(1, 2)*H*(H-6)
c = (W-f0**2)/2
scalar_pde_residual = sp.simplify(-2*c - f0**2 + W)
R_bound = sp.simplify(f0*sp.sqrt(H)/c)
# This equals 2 f sqrt(H)/(W-f^2).

# Small-delta expansion of k_* with b=B delta and f=F delta.
B, C, d = sp.symbols("B C d", nonnegative=True)
k_delta = 3+B*d+sp.sqrt((3+B*d)**2+2*C**2*d**2)
k_series = sp.series(k_delta, d, 0, 3).removeO()

checks = {
    "psi_factorization_residual": str(factor_residual),
    "psi_at_k_star": str(at_root_residual),
    "root_factorization": "Psi(e)=1/2(e-k_*)(e-k_-)",
    "k_star": str(k_star),
    "reaction_at_root": str(reaction_at_root),
    "reaction_target": str(reaction_target),
    "reaction_residual": str(reaction_residual),
    "kato_gradient_coefficient": str(a_k),
    "kato_coefficient_residual": str(sp.simplify(a_k-a_k_target)),
    "kato_range_for_e_ge_k": "1/2 <= (3e-k)/(4e) < 3/4",
    "orbit_forcing": {
        "E0_eigenvalues": ["a", "-a"],
        "tr_E0_squared": str(tr_E0_sq),
        "F_squared_H2": str(F_sq),
        "F_norm_H2": str(F_norm),
        "operator_bound": "a<=delta implies |F|<=2 delta",
    },
    "small_delta_root_series": str(k_series),
    "scalar_ball_model": {
        "energy": "e=H>6",
        "reaction_W": str(W),
        "vector_field": "V(x)=-c x on a Euclidean 2-ball",
        "c": str(c),
        "pde_residual_divV_minus_f2_plus_W": str(scalar_pde_residual),
        "radius_condition_from_|V|<=f*sqrt(H)": "R <= " + str(R_bound),
        "meaning": "arbitrarily high constant H is compatible on a sufficiently small ball; a local estimate must retain radius or boundary information",
    },
    "all_symbolic_zero_checks": bool(
        factor_residual == 0
        and at_root_residual == 0
        and reaction_residual == 0
        and sp.simplify(a_k-a_k_target) == 0
        and scalar_pde_residual == 0
    ),
}

out = Path(__file__).resolve().parents[1] / "data" / "step86_forced_caccioppoli_verify.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(checks, indent=2), encoding="utf-8")
print(json.dumps(checks, indent=2))
print(f"wrote {out}")
