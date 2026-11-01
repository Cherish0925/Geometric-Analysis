#!/usr/bin/env python3
"""Step 61: Exact Ricci for the TORIC-CONE opposite-warped background.

The Strategist's correction: the earlier Step-60 local model used T^2 fibers of
size O(1) over a flat R^2 base -- an ALG/collapsed neck, NOT the cone over
S^3/Z_2 that the Eguchi-Hanson (EH) obstruction actually lives on.

The flat cone R^4/Z_2 in TORIC (polar-symplectic) coordinates is
    g0 = dr1^2 + r1^2 dphi^2 + dr2^2 + r2^2 dpsi^2,
with (r1,r2) in the quarter-plane {r1,r2>=0}, and Z_2 acting by
    (phi,psi) -> (phi+pi, psi+pi).
Set r1 = r cos(alpha), r2 = r sin(alpha), alpha in [0,pi/2].  Then r is the ALE
radial distance and alpha the polar angle on the base quarter-sphere.

The opposite-warping deformation (Step-11 mechanism on the right geometry):
    g = dr1^2 + r1^2 e^{2v} dphi^2 + dr2^2 + r2^2 e^{-2v} dpsi^2,
where v = v(r1,r2) is a function on the orbit space.  We verify EXACTLY:
  (1) g0 (v=0) is flat (Ricci = 0);
  (2) for general v, how the Ricci tensor depends on v -- in particular whether
      the base blocks depend only on nabla v (opposite-warping cancellation)
      and the fiber blocks on a Laplace-type operator of v.

This is the correct frame for the reachability question: does a T^2-invariant
degree-2 harmonic drift move exactly one eigenvalue of W_pm?

We use sympy to compute the full Ricci tensor of g in coordinates
(r1, r2, phi, psi) with v a general function of (r1, r2).
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step61_toric_cone_warp_ricci.json"

r1, r2, phi, psi = sp.symbols('r1 r2 phi psi', positive=True)
coords = [r1, r2, phi, psi]
v = sp.Function('v')(r1, r2)

# Metric g = dr1^2 + r1^2 e^{2v} dphi^2 + dr2^2 + r2^2 e^{-2v} dpsi^2
g = sp.diag(1, 1, r1**2 * sp.exp(2*v), r2**2 * sp.exp(-2*v))
ginv = g.inv()
n = 4

# Christoffel symbols
Gamma = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            s = sp.Integer(0)
            for l in range(n):
                s += ginv[i, l]*(sp.diff(g[l, j], coords[k]) + sp.diff(g[l, k], coords[j]) - sp.diff(g[j, k], coords[l]))
            Gamma[i][j][k] = sp.simplify(s/2)

# Ricci tensor
Ric = [[sp.Integer(0)]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        s = sp.Integer(0)
        for k in range(n):
            s += sp.diff(Gamma[k][i][j], coords[k]) - sp.diff(Gamma[k][i][k], coords[j])
            for l in range(n):
                s += Gamma[k][k][l]*Gamma[l][i][j] - Gamma[k][j][l]*Gamma[l][i][k]
        Ric[i][j] = sp.simplify(sp.expand(s))

# --- Check 1: flat background v = 0 ---
Ric_flat = [[sp.simplify(Ric[i][j].subs({v: 0}).doit()) for j in range(n)] for i in range(n)]
# substitute the function v -> 0 requires replacing derivatives too; do via a zero function
v0 = sp.Function('v')(r1, r2)
subs0 = {sp.Derivative(v0, r1): 0, sp.Derivative(v0, r2): 0,
         sp.Derivative(v0, r1, r1): 0, sp.Derivative(v0, r2, r2): 0,
         sp.Derivative(v0, r1, r2): 0, v0: 0}
Ric_flat = [[sp.simplify(Ric[i][j].subs(subs0)) for j in range(n)] for i in range(n)]
flat_ok = all(Ric_flat[i][j] == 0 for i in range(n) for j in range(n))

# --- Express the general Ricci components in readable form ---
vr1 = sp.diff(v, r1)
vr2 = sp.diff(v, r2)
components = {}
for i in range(n):
    for j in range(n):
        rij = sp.simplify(Ric[i][j])
        if rij != 0:
            components[f"Ric[{i}][{j}]"] = str(rij)

# --- Orthonormal fiber-block Ricci (divide by metric) ---
Ric_phi_norm = sp.simplify(Ric[2][2] / g[2, 2])
Ric_psi_norm = sp.simplify(Ric[3][3] / g[3, 3])

# base-block Ricci in the (r1,r2) plane
Ric_base = sp.Matrix([[sp.simplify(Ric[0][0]), sp.simplify(Ric[0][1])],
                      [sp.simplify(Ric[1][0]), sp.simplify(Ric[1][1])]])

# --- Does the base block depend only on first derivatives of v? ---
# Check by looking for second-derivative symbols in the base entries.
def has_second_deriv(expr):
    return any(d.derivative_count >= 2 for d in expr.atoms(sp.Derivative))
base_only_first = not any(has_second_deriv(Ric_base[a, b]) for a in range(2) for b in range(2))

# --- The fiber Laplace-type operator ---
# expect Ric_phi_norm ~ - (some 2nd-order op of v), Ric_psi_norm ~ + (same op) + curvature terms
data = {
    "status": "ok",
    "metric": "diag(1, 1, r1^2 e^{2v}, r2^2 e^{-2v}), v=v(r1,r2)",
    "coords": ["r1", "r2", "phi", "psi"],
    "flat_background_v0_Ricci_zero": bool(flat_ok),
    "nonzero_Ricci_components_general_v": components,
    "Ric_base_block": [[str(Ric_base[a, b]) for b in range(2)] for a in range(2)],
    "Ric_base_depends_only_on_first_derivatives_of_v": bool(base_only_first),
    "Ric_phi_normalized": str(Ric_phi_norm),
    "Ric_psi_normalized": str(Ric_psi_norm),
    "interpretation": {
        "flat_check": "v=0 gives Ricci=0, confirming toric cone form is flat R^4/Z_2 quotient background.",
        "opposite_warping": "The base (r1,r2) Ricci block should contain only first derivatives of v (opposite-warping Hessian cancellation), while fiber blocks carry the 2nd-order operator.",
    },
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, indent=2), encoding='utf-8')
print(json.dumps({
    "status": "ok",
    "output": str(OUT),
    "flat_background_Ricci_zero": bool(flat_ok),
    "base_only_first_derivs": bool(base_only_first),
    "Ric_phi_normalized": str(Ric_phi_norm),
    "Ric_psi_normalized": str(Ric_psi_norm),
    "nonzero_components": list(components.keys()),
}, indent=2))
