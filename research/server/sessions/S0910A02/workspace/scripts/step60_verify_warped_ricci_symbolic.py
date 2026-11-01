#!/usr/bin/env python3
"""Symbolically verify exact Ricci formula for the local Step-60 opposite-warped metric.

Coordinates (r,theta,phi,psi), metric
  diag(1, r^2, exp(2u(r,theta)), exp(-2u(r,theta))).

Expected covariant Ricci components:
  Ric_rr = -2 u_r^2
  Ric_rtheta = -2 u_r u_theta
  Ric_thetatheta = -2 u_theta^2
  Ric_phiphi / g_phiphi = -Delta_B u
  Ric_psipsi / g_psipsi = +Delta_B u
  other components zero
where Delta_B u = u_rr + r^{-1}u_r + r^{-2}u_thetatheta.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step60_verify_warped_ricci_symbolic.json"

r, th, ph, ps = sp.symbols('r th ph ps', positive=True)
coords = [r, th, ph, ps]
u = sp.Function('u')(r, th)
metric = sp.diag(1, r**2, sp.exp(2*u), sp.exp(-2*u))
ginv = metric.inv()
n = 4
Gamma = [[ [sp.Integer(0) for k in range(n)] for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            s = sp.Integer(0)
            for l in range(n):
                s += ginv[i,l]*(sp.diff(metric[l,k], coords[j]) + sp.diff(metric[l,j], coords[k]) - sp.diff(metric[j,k], coords[l]))
            Gamma[i][j][k] = sp.simplify(s/2)

Ric = [[sp.Integer(0) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        s = sp.Integer(0)
        for k in range(n):
            s += sp.diff(Gamma[k][i][j], coords[k]) - sp.diff(Gamma[k][i][k], coords[j])
            for l in range(n):
                s += Gamma[k][i][j]*Gamma[l][k][l] - Gamma[l][i][k]*Gamma[k][j][l]
        Ric[i][j] = sp.simplify(sp.trigsimp(s))

ur = sp.diff(u,r)
ut = sp.diff(u,th)
Delta = sp.diff(u,r,2) + sp.diff(u,r)/r + sp.diff(u,th,2)/r**2
expected = [[sp.Integer(0) for j in range(n)] for i in range(n)]
expected[0][0] = -2*ur**2
expected[0][1] = expected[1][0] = -2*ur*ut
expected[1][1] = -2*ut**2
expected[2][2] = -metric[2,2]*Delta
expected[3][3] = metric[3,3]*Delta

checks = []
all_ok = True
for i in range(n):
    for j in range(n):
        diff = sp.simplify(sp.factor(Ric[i][j] - expected[i][j]))
        ok = (diff == 0)
        all_ok = all_ok and ok
        checks.append({
            "component": [i,j],
            "ricci": str(Ric[i][j]),
            "expected": str(expected[i][j]),
            "difference": str(diff),
            "ok": ok,
        })

data = {
    "status": "ok" if all_ok else "failed",
    "metric": "diag(1, r^2, exp(2u(r,theta)), exp(-2u(r,theta)))",
    "Delta_base": str(Delta),
    "all_components_match": all_ok,
    "checks": checks,
    "orthonormal_interpretation": "In the orthonormal fiber frame, Ric_phi_phi/g_phi_phi = -Delta_B u and Ric_psi_psi/g_psi_psi = +Delta_B u; the base covariant block is -2 du⊗du.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, indent=2), encoding='utf-8')
print(json.dumps({"status": data["status"], "output": str(OUT), "all_components_match": all_ok, "Delta_base": str(Delta)}, indent=2))
