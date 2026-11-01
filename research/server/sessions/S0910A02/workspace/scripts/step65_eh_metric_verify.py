#!/usr/bin/env python3
"""Step 65 (fix): Verify Eguchi-Hanson metric is Ricci-flat in correct coordinates.

The Gibbons-Hawking form is:
    g = V * (dx^2 + dy^2 + dz^2) + V^{-1} * (dpsi + A)^2
where (x,y,z) are Cartesian coords on R^3, V = 1 - a^4/R^4, R^2 = x^2+y^2+z^2,
and A is the 1-form with dA = *_3 dV.

For V = 1 - a^4/R^4 (Taub-NUT with negative mass -> EH):
    *_3 dV has period 4*pi over S^2 at infinity (after normalization).
    psi has period 2*pi (giving the Z_2 quotient at infinity).

We use Cartesian (x, y, z, psi) to avoid the polar-coordinate subtleties.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step65_eh_metric_verify.json"

print("=== Verifying EH metric in Gibbons-Hawking Cartesian form ===")

# Coordinates: x, y, z, psi
x, y, z, psi = sp.symbols('x y z psi', real=True)
a = sp.symbols('a', positive=True)
coords = [x, y, z, psi]
n = 4

R2 = x**2 + y**2 + z**2
R = sp.sqrt(R2)

# Harmonic function V = 1 - a^4/R^4  (note: for EH, the constant is chosen so V(a)=0)
# Actually the standard EH potential is V = 1/R^2 - a^4/R^6 ... no.
# Let me use the CORRECT form.
#
# The multi-center Gibbons-Hawking: V = sum_i 1/|x - x_i| + c
# For EH (2 centers at origin, or 1 center with negative mass):
# V = 1/R^2 is NOT harmonic on R^3!
#
# The correct harmonic function for EH on R^3 \ {0} is:
# V = 1/R  -- this is harmonic away from origin, dV = -x/R^3 dx - ..., *_3 dV = monopole
# But then g = V*(dx^2+dy^2+dz^2) + V^{-1}*(dpsi+A)^2 with V = 1/R gives the
# Taub-NUT metric, which is NOT asymptotically R^4/Z_2.
#
# For EH, we need V = 1/R with TWO centers identified, i.e., the Z_2 quotient.
# The correct potential is V = 1/(2R) on R^3/Z_2... this is getting complicated.
#
# SIMPLER APPROACH: use the standard Bianchi IX / Brioschi form.
# EH metric in terms of the radial coordinate r >= a:
#   g = (1 - a^4/r^4)^{-1} dr^2 + (r^2/4)[sigma_1^2 + sigma_2^2 + (1-a^4/r^4)*sigma_3^2]
# where sigma_i are the standard left-invariant 1-forms on S^3:
#   sigma_1 = sin(psi)*d(theta) - cos(psi)*sin(theta)*d(phi)
#   sigma_2 = -cos(psi)*d(theta) - sin(psi)*sin(theta)*d(phi)
#   sigma_3 = d(psi) + cos(theta)*d(phi)
# with ranges: theta in [0,pi], phi in [0,2pi], psi in [0,2pi) (the Z_2 quotient gives psi ~ psi+pi).
#
# This is the standard form. Let me use this.

print("Using Brioschi/Bianchi IX form:")
print("  g = dr^2/W + (r^2/4)[sigma_1^2 + sigma_2^2 + W*sigma_3^2], W = 1 - a^4/r^4")

r, theta, phi, psi_var, a_var = sp.symbols('r theta phi psi a', positive=True)
W = 1 - a_var**4/r**4

# Left-invariant 1-forms (as components in dtheta, dphi, dpsi basis)
# sigma_1 = sin(psi) dtheta - cos(psi) sin(theta) dphi
# sigma_2 = -cos(psi) dtheta - sin(psi) sin(theta) dphi
# sigma_3 = dpsi + cos(theta) dphi
s1 = [sp.sin(psi_var), -sp.cos(psi_var)*sp.sin(theta), 0]
s2 = [-sp.cos(psi_var), -sp.sin(psi_var)*sp.sin(theta), 0]
s3 = [0, sp.cos(theta), 1]

# Metric: g = diag(1/W, r^2/4 * (s1^2 + s2^2 + W*s3^2))
# where the spatial part is built from outer products
coords2 = [r, theta, phi, psi_var]
g = sp.zeros(4, 4)
g[0, 0] = 1/W
for i in range(3):
    for j in range(3):
        g[1+i, 1+j] = (r**2/4) * (s1[i]*s1[j] + s2[i]*s2[j] + W*s3[i]*s3[j])

print("Metric constructed. Computing Ricci...")

ginv = g.inv()
n = 4

Gamma = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            s = sp.Integer(0)
            for l in range(n):
                s += ginv[i, l]*(sp.diff(g[l, j], coords2[k]) + sp.diff(g[l, k], coords2[j]) - sp.diff(g[j, k], coords2[l]))
            Gamma[i][j][k] = sp.simplify(s/2)

Ric = [[sp.Integer(0)]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        s = sp.Integer(0)
        for k in range(n):
            s += sp.diff(Gamma[k][i][j], coords2[k]) - sp.diff(Gamma[k][i][k], coords2[j])
            for l in range(n):
                s += Gamma[k][k][l]*Gamma[l][i][j] - Gamma[k][j][l]*Gamma[l][i][k]
        Ric[i][j] = sp.trigsimp(sp.expand(s))

flat = all(Ric[i][j] == 0 for i in range(n) for j in range(n))
print(f"Ricci-flat: {flat}")

if not flat:
    print("Nonzero components:")
    for i in range(n):
        for j in range(n):
            if Ric[i][j] != 0:
                print(f"  Ric[{i}][{j}] = {sp.simplify(Ric[i][j])}")

# Also compute the scalar curvature as a sanity check
Scal = sp.Integer(0)
for i in range(n):
    for j in range(n):
        Scal += ginv[i, j] * Ric[i][j]
Scal = sp.simplify(Scal)
print(f"Scalar curvature: {Scal}")

data = {
    "status": "ok",
    "metric_form": "Brioschi: dr^2/W + (r^2/4)[s1^2+s2^2+W*s3^2], W=1-a^4/r^4",
    "Ricci_flat": bool(flat),
    "scalar_curvature": str(Scal),
    "note": "Standard Eguchi-Hanson on T*S^2, asymptotic to R^4/Z_2"
}
OUT.write_text(json.dumps(data, indent=2))
print(f"Output: {OUT}")
