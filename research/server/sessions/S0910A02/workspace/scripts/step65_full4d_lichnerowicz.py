#!/usr/bin/env python3
"""Step 65: Full 4D symbolic linearized Ricci on EH with diagonal ansatz.

The diagonal-only-r approximation is INVALID (angular Christoffels at theta=pi/2
are nonzero and contribute). We must do the full 4D Ricci computation.

Strategy to keep it tractable:
  - Build the full EH metric in (r, theta, phi, psi) with the Bianchi-IX 1-forms.
  - Perturb: g_s = g_EH + s*h, h built from the diagonal ansatz extended to 4D.
    The U(2)-invariant diagonal ansatz in the Bianchi-IX coframe:
      h = f1(r)*(dr^2/W) + f2(r)*(r^2/4)(s1^2+s2^2) + f3(r)*(r^2 W/4) s3^2
    This is already the full 4D tensor (no angular approximation).
  - Compute Ric(g_s) symbolically, extract coefficient of s^1.
  - The U(2) symmetry means the linearized Ricci is also diagonal in this coframe,
    so we can evaluate at theta=pi/2, phi=0, psi=0 AFTER computing the full tensor.
  - Extract 3 ODEs and solve.

This is heavy but correct. We substitute a=1 early to reduce expression size.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step65_full4d_lichnerowicz.json"

print("=== Full 4D linearized Ricci on EH ===")

r, theta, phi, psi, a, s, Lam = sp.symbols('r theta phi psi a s Lambda', positive=True)
W = 1 - a**4/r**4

# Bianchi-IX left-invariant 1-forms (dtheta, dphi, dpsi components)
s1 = [sp.sin(psi), -sp.cos(psi)*sp.sin(theta), 0]
s2 = [-sp.cos(psi), -sp.sin(psi)*sp.sin(theta), 0]
s3 = [0, sp.cos(theta), 1]

f1, f2, f3 = sp.symbols('f1 f2 f3', cls=sp.Function)

# EH metric
g = sp.zeros(4, 4)
g[0, 0] = 1/W
for i in range(3):
    for j in range(3):
        g[1+i, 1+j] = (r**2/4)*(s1[i]*s1[j] + s2[i]*s2[j] + W*s3[i]*s3[j])

# Perturbation h (U(2)-invariant diagonal in the Bianchi-IX coframe)
h = sp.zeros(4, 4)
h[0, 0] = f1(r)*(1/W)
for i in range(3):
    for j in range(3):
        h[1+i, 1+j] = f2(r)*(r**2/4)*(s1[i]*s1[j] + s2[i]*s2[j]) + f3(r)*(r**2*W/4)*s3[i]*s3[j]

# Perturbed metric
gs = g + s*h

coords = [r, theta, phi, psi]
n = 4

# Substitute a=1 to reduce size
a_val = sp.Rational(1, 1)
gs = gs.subs(a, 1)

print("Computing inverse metric (4x4 symbolic, this may take a moment)...")
gs_inv = gs.inv()

print("Computing Christoffels...")
Gamma = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(j, n):
            s_expr = sp.Integer(0)
            for l in range(n):
                s_expr += gs_inv[i, l]*(sp.diff(gs[l, j], coords[k]) + sp.diff(gs[l, k], coords[j]) - sp.diff(gs[j, k], coords[l]))
            Gamma[i][j][k] = sp.simplify(s_expr/2)
            Gamma[i][k][j] = Gamma[i][j][k]

print("Computing Ricci tensor...")
Ric = [[sp.Integer(0)]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        s_expr = sp.Integer(0)
        for k in range(n):
            s_expr += sp.diff(Gamma[k][i][j], coords[k]) - sp.diff(Gamma[k][i][k], coords[j])
            for l in range(n):
                s_expr += Gamma[k][k][l]*Gamma[l][i][j] - Gamma[k][j][l]*Gamma[l][i][k]
        Ric[i][j] = s_expr  # don't simplify yet (too slow)

# Extract first-order in s
print("Extracting linearized Ricci (coefficient of s^1)...")
dRic = [[sp.Integer(0)]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dRic[i][j] = sp.simplify(sp.diff(Ric[i][j], s).subs(s, 0))

# Evaluate at theta=pi/2, phi=0, psi=0
subs_pt = {theta: sp.pi/2, phi: 0, psi: 0}
print("\nLinearized Ricci at evaluation point:")
dRic00 = sp.simplify(dRic[0][0].subs(subs_pt))
dRic11 = sp.simplify(dRic[1][1].subs(subs_pt))
dRic22 = sp.simplify(dRic[2][2].subs(subs_pt))
dRic33 = sp.simplify(dRic[3][3].subs(subs_pt))

print(f"  dRic00 = {dRic00}")
print(f"  dRic11 = {dRic11}")
print(f"  dRic22 = {dRic22}")
print(f"  dRic33 = {dRic33}")

# Target: Lambda*g_ii at the point
g00_pt = sp.simplify(g[0,0].subs({a:1}).subs(subs_pt))
g11_pt = sp.simplify(g[1,1].subs({a:1}).subs(subs_pt))
g22_pt = sp.simplify(g[2,2].subs({a:1}).subs(subs_pt))
g33_pt = sp.simplify(g[3,3].subs({a:1}).subs(subs_pt))

# ODEs: dRic_ii = Lambda*g_ii
eq00 = sp.Eq(dRic00, Lam*g00_pt)
eq11 = sp.Eq(dRic11, Lam*g11_pt)
eq33 = sp.Eq(dRic33, Lam*g33_pt)

# Decouple
f1pp = sp.Derivative(f1(r), (r,2))
f2pp = sp.Derivative(f2(r), (r,2))
f3pp = sp.Derivative(f3(r), (r,2))

print("\nDecoupling...")
try:
    sols = sp.solve([eq00, eq11, eq33], [f1pp, f2pp, f3pp], dict=True)
    decoupled = bool(sols)
    if sols:
        sol = sols[0]
        e1 = sp.simplify(sol[f1pp])
        e2 = sp.simplify(sol[f2pp])
        e3 = sp.simplify(sol[f3pp])
        print("Decoupled.")
        print(f"  f1'' = {e1}")
        print(f"  f2'' = {e2}")
        print(f"  f3'' = {e3}")
except Exception as ex:
    print(f"Failed: {ex}")
    decoupled = False
    e1=e2=e3=None

data = {
    "status": "ok" if decoupled else "decouple_failed",
    "dRic_at_point": {
        "00": str(dRic00), "11": str(dRic11), "22": str(dRic22), "33": str(dRic33),
    },
    "ode_decoupled": decoupled,
}
if decoupled:
    data["odes"] = {"f1pp": str(e1), "f2pp": str(e2), "f3pp": str(e3)}
OUT.write_text(json.dumps(data, indent=2))
print(f"\nOutput: {OUT}")
