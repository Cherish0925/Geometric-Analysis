#!/usr/bin/env python3
"""Exact local model for the Bloch field of a transverse C^2 spinor zero.

For z=(x1+i x2,x3+i x4), the unit Bloch field is the radial Hopf map
n = (2 Re(z1 conjugate(z2)), 2 Im(z1 conjugate(z2)), |z1|^2-|z2|^2)/r^2.
The script verifies |dn|^2=8/r^2 and |n^* omega_S2|^2=16/r^4.
It also records the induced frame-twist density |t^-|^2=8/r^4 and
annular logarithmic coefficients.
"""
import json
from pathlib import Path
import sympy as sp

x = sp.symbols('x1:5', real=True)
r2 = sum(v*v for v in x)
x1,x2,x3,x4 = x
N = sp.Matrix([
    2*(x1*x3+x2*x4),
    2*(x2*x3-x1*x4),
    x1*x1+x2*x2-x3*x3-x4*x4,
])
n = sp.simplify(N/r2)
Dn = n.jacobian(x)
grad_sq = sp.factor(sum(Dn[a,i]**2 for a in range(3) for i in range(4)))

# Pullback of the unit-area form on S^2: F_ij=n dot (partial_i n cross partial_j n).
F = {}
F_sq = 0
for i in range(4):
    for j in range(i+1,4):
        fij = sp.factor(n.dot(Dn[:,i].cross(Dn[:,j])))
        F[(i+1,j+1)] = fij
        F_sq += fij*fij
F_sq = sp.factor(F_sq)

# If Omega=sqrt(2)n and dn=alpha phi + beta Jphi with |phi|^2=2,
# the Hopf model has |alpha|^2=|beta|^2=4/r^2 and alpha perpendicular beta.
# Hence |(alpha wedge beta)^-|^2=(1/2)|alpha wedge beta|^2=8/r^4.
twist_minus_sq = sp.factor(8/r2**2)

out = {
    "n_norm_sq": str(sp.factor(n.dot(n))),
    "grad_n_sq": str(grad_sq),
    "hopf_curvature_components": {f"{i}{j}": str(v) for (i,j),v in F.items()},
    "hopf_curvature_sq": str(F_sq),
    "twist_minus_sq": str(twist_minus_sq),
    "sphere_area_S3": "2*pi^2",
    "annulus_int_grad_n_4": "128*pi^2*log(R/epsilon)",
    "annulus_int_twist_minus_sq": "16*pi^2*log(R/epsilon)",
    "weighted_rho2_grad_n2_if_rho_r2": "(8*pi^2/3)*R^6 up to the leading amplitude constant squared",
}
assert sp.simplify(n.dot(n)-1) == 0
assert sp.simplify(grad_sq-8/r2) == 0
assert sp.simplify(F_sq-16/r2**2) == 0

root = Path(__file__).resolve().parents[1]
out_path = root/'data'/'step64_hopf_spinor_twist.json'
out_path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
