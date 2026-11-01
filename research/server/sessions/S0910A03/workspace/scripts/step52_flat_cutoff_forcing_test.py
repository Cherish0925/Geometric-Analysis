#!/usr/bin/env python3
"""Exact leading-order flat-torus test for normalized cutoff flow.

On T^4 with the flat metric and chi(x1)=(1+cos x1)/2, let a=chi^2.
At t=0, the normalized cutoff flow has metric variation -2 a g, since Ric=0.
The fully lowered curvature variation is g \owedge Hess(a).  This script
enumerates its Euclidean tensor norm and integrates the exact leading
coefficient of int |Rm(g(t))|^2 dmu.

It checks only this explicit infinitesimal calculation, not PDE existence.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

n = 4
x = sp.symbols("x", real=True)
chi = (1 + sp.cos(x)) / 2
a = sp.expand_trig(chi**2)
h = sp.simplify(sp.diff(a, x, 2))

# H = Hess(a) has only H_00=h.  Enumerate (delta \owedge H)_{ijkl}.
def delta(i: int, j: int) -> int:
    return int(i == j)

def H(i: int, j: int):
    return h if (i == 0 and j == 0) else sp.Integer(0)

def KN(i: int, j: int, k: int, l: int):
    return (
        delta(i, k) * H(j, l)
        - delta(i, l) * H(j, k)
        - delta(j, k) * H(i, l)
        + delta(j, l) * H(i, k)
    )

norm_sq = sp.simplify(sum(KN(i, j, k, l) ** 2
                          for i in range(n) for j in range(n)
                          for k in range(n) for l in range(n)))
ratio = sp.simplify(norm_sq / h**2)
int_x = sp.integrate(sp.expand_trig(h**2), (x, 0, 2 * sp.pi))
leading_energy = sp.simplify(ratio * int_x * (2 * sp.pi) ** 3)

expected_h = -(sp.cos(x) + sp.cos(2*x)) / 2
assert sp.simplify(h - expected_h) == 0
assert ratio == 12
assert sp.simplify(int_x - sp.pi / 2) == 0
assert sp.simplify(leading_energy - 48 * sp.pi**4) == 0

# If E(t)=C t^2+O(t^3), then E'(t)/E(t)=2/t+O(1), so no finite
# homogeneous Gronwall coefficient E' <= C0 E can hold near t=0.
t = sp.symbols("t", positive=True)
model_E = leading_energy * t**2
model_ratio = sp.simplify(sp.diff(model_E, t) / model_E)
assert model_ratio == 2/t

result = {
    "manifold": "flat T^4 with periods 2*pi",
    "chi": str(chi),
    "a": str(sp.expand_trig(a)),
    "a_second_derivative": str(h),
    "kn_norm_squared_over_hessian_component_squared": int(ratio),
    "integral_a_second_derivative_squared": str(int_x),
    "critical_energy_leading_term": "48*pi^4*t^2 + O(t^3)",
    "critical_energy_log_derivative_leading_term": "2/t + O(1)",
    "conclusion": (
        "Spatial normalization creates curvature from flat data.  The critical "
        "homothety reaction cancels, but the Hessian(a) forcing remains; a "
        "homogeneous inequality E'(t)<=C E(t) is impossible near t=0."
    ),
    "not_checked": [
        "nonlinear PDE existence",
        "higher-order t expansion",
        "the coupled Yang inverse",
        "Yau Problem 26"
    ]
}

out = Path(__file__).resolve().parents[1] / "data" / "step52_flat_cutoff_forcing_test.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
print(f"wrote {out}")
