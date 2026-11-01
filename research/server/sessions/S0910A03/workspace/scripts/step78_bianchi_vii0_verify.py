#!/usr/bin/env python3
"""Exact symbolic verification for the rotating-eigenframe Bianchi VII_0 ansatz.

Metric (coordinates r,z,x,y, with k an integer for global 2*pi-periodicity):
    g = dr^2 + a(r)^2 dz^2 + b(r)^2 omega1^2 + c(r)^2 omega2^2,
    omega1 = cos(k z) dx + sin(k z) dy,
    omega2 = -sin(k z) dx + cos(k z) dy.

The script computes the coordinate Ricci tensor from Christoffel symbols, evaluates
at z=0 (permitted by slice homogeneity), and checks the intrinsic and
cohomogeneity-one formulas used in the Step 78 invariant-region argument.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

r, z, x, y = sp.symbols("r z x y", real=True)
k = sp.symbols("k", real=True, nonzero=True)
coords = (r, z, x, y)
a = sp.Function("a")(r)
b = sp.Function("b")(r)
c = sp.Function("c")(r)
C = sp.cos(k*z)
S = sp.sin(k*z)

# Coordinate metric.  At z=0, dx and dy are respectively omega1 and omega2.
g = sp.zeros(4)
g[0, 0] = 1
g[1, 1] = a**2
g[2, 2] = b**2*C**2 + c**2*S**2
g[3, 3] = b**2*S**2 + c**2*C**2
g[2, 3] = g[3, 2] = (b**2-c**2)*C*S

ginv = sp.zeros(4)
ginv[0, 0] = 1
ginv[1, 1] = a**-2
ginv[2, 2] = b**-2*C**2 + c**-2*S**2
ginv[3, 3] = b**-2*S**2 + c**-2*C**2
ginv[2, 3] = ginv[3, 2] = (b**-2-c**-2)*C*S
assert sp.simplify(g*ginv-sp.eye(4)) == sp.zeros(4)

n = 4
Gamma = [[[sp.S.Zero for _ in range(n)] for _ in range(n)] for _ in range(n)]
for ell in range(n):
    for i in range(n):
        for j in range(n):
            Gamma[ell][i][j] = sp.simplify(sp.Rational(1, 2)*sum(
                ginv[ell, m]*(sp.diff(g[m, j], coords[i])
                               + sp.diff(g[m, i], coords[j])
                               - sp.diff(g[i, j], coords[m]))
                for m in range(n)
            ))

Ric = sp.zeros(n)
for i in range(n):
    for j in range(n):
        expr = sp.S.Zero
        for ell in range(n):
            expr += sp.diff(Gamma[ell][i][j], coords[ell])
            expr -= sp.diff(Gamma[ell][i][ell], coords[j])
            for m in range(n):
                expr += Gamma[ell][i][j]*Gamma[m][ell][m]
                expr -= Gamma[m][i][ell]*Gamma[ell][j][m]
        Ric[i, j] = sp.trigsimp(sp.simplify(expr))

# Evaluate after differentiating. Homogeneity makes normalized diagonal entries
# independent of z; z=0 exposes the invariant orthonormal frame directly.
def at0(expr):
    return sp.factor(sp.trigsimp(sp.simplify(expr.subs(z, 0))))

Rrr = at0(Ric[0, 0])
Rz = at0(Ric[1, 1]/a**2)
Rb = at0(Ric[2, 2]/b**2)
Rc = at0(Ric[3, 3]/c**2)

offdiag = {}
for i in range(n):
    for j in range(i+1, n):
        offdiag[f"Ric_{i}{j}_at_z0"] = str(at0(Ric[i, j]))

a1, b1, c1 = sp.diff(a, r), sp.diff(b, r), sp.diff(c, r)
a2, b2, c2 = sp.diff(a, r, 2), sp.diff(b, r, 2), sp.diff(c, r, 2)
u, v, w = a1/a, b1/b, c1/c
H = u+v+w

K_alg = sp.factor(k**2*(b**2-c**2)**2/(2*a**2*b**2*c**2))
L_alg = sp.factor(k**2*(b**4-c**4)/(2*a**2*b**2*c**2))

expected = {
    "Rrr": -(a2/a+b2/b+c2/c),
    "Rz_unit": -K_alg-a2/a-u*(v+w),
    "Rb_unit": L_alg-b2/b-v*(u+w),
    "Rc_unit": -L_alg-c2/c-w*(u+v),
}
computed = {"Rrr": Rrr, "Rz_unit": Rz, "Rb_unit": Rb, "Rc_unit": Rc}
checks = {name: str(sp.factor(computed[name]-expr)) for name, expr in expected.items()}

# Intrinsic Ricci is obtained by suppressing all radial derivatives.
radial_zero = {
    a1: 0, b1: 0, c1: 0,
    a2: 0, b2: 0, c2: 0,
}
intrinsic = {
    "Ric_z_unit": sp.factor(Rz.subs(radial_zero)),
    "Ric_omega1_unit": sp.factor(Rb.subs(radial_zero)),
    "Ric_omega2_unit": sp.factor(Rc.subs(radial_zero)),
}
intrinsic_scalar = sp.factor(sum(intrinsic.values()))
intrinsic_checks = {
    "Ric_z_plus_K": str(sp.factor(intrinsic["Ric_z_unit"]+K_alg)),
    "Ric_omega1_minus_L": str(sp.factor(intrinsic["Ric_omega1_unit"]-L_alg)),
    "Ric_omega2_plus_L": str(sp.factor(intrinsic["Ric_omega2_unit"]+L_alg)),
    "scalar_plus_K": str(sp.factor(intrinsic_scalar+K_alg)),
}

# Algebraic conversion to d=log(b/c).  With t=b/c=e^d:
# K=(k^2/(2a^2))(t-t^{-1})^2=2k^2 a^{-2}sinh(d)^2,
# L=(k^2/(2a^2))(t^2-t^{-2})=K*coth(d).
d, aa, kk = sp.symbols("d aa kk", real=True, positive=True)
t = sp.exp(d)
K_d = 2*kk**2/aa**2*sp.sinh(d)**2
L_d = kk**2/aa**2*sp.sinh(2*d)
hyperbolic_check = sp.simplify(sp.trigsimp(L_d-K_d*sp.coth(d)))

# Einstein ODE residuals, using Ric=-3g.  These are identities after replacing
# each normalized Ricci entry by -3.
up = a2/a-u**2
dp = (b2/b-v**2)-(c2/c-w**2)
einstein_ode_checks = {
    "u_equation_from_Rz": str(sp.factor((up+H*u)-(3-K_alg) + (Rz+3))),
    "d_equation_from_Rb_minus_Rc": str(sp.factor(
        (dp+H*(v-w)-2*L_alg) + (Rb-Rc)
    )),
    "K_log_derivative": str(sp.factor(
        sp.diff(K_alg, r)/K_alg - (-2*u+2*(b**2+c**2)/(b**2-c**2)*(v-w))
    )),
}

out = {
    "ansatz": "dr^2+a(r)^2 dz^2+b(r)^2 omega1^2+c(r)^2 omega2^2",
    "forms": {
        "omega1": "cos(kz) dx + sin(kz) dy",
        "omega2": "-sin(kz) dx + cos(kz) dy",
        "globality": "k integer when z has period 2*pi",
        "structure": "d omega1=k dz wedge omega2; d omega2=-k dz wedge omega1",
    },
    "computed_normalized_Ricci_at_z0": {key: str(value) for key, value in computed.items()},
    "full_ricci_formula_checks_zero": checks,
    "offdiagonal_ricci_at_z0": offdiag,
    "intrinsic_slice_ricci": {key: str(value) for key, value in intrinsic.items()},
    "intrinsic_formula_checks_zero": intrinsic_checks,
    "definitions": {
        "K_algebraic": str(K_alg),
        "L_algebraic": str(L_alg),
        "K_hyperbolic": "2*k^2*a^(-2)*sinh(d)^2",
        "L_hyperbolic": "k^2*a^(-2)*sinh(2d)=K*coth(d)",
        "L_minus_K_coth_d": str(hyperbolic_check),
    },
    "einstein_ode_checks_zero": einstein_ode_checks,
    "resulting_exact_odes": {
        "u": "u' + H u = 3-K",
        "d": "d'' + H d' = 2 K coth(d)",
        "K": "(log K)' = -2u + 2 coth(d)d'",
    },
    "perturbed_odes_for_E_Ric_plus_3g": {
        "u": "u' + H u = 3-K-E_z",
        "d": "d'' + H d' = 2 K coth(d)-(E_omega1-E_omega2)",
    },
}

path = Path(__file__).resolve().parents[1]/"data"/"step78_bianchi_vii0_symbolic.json"
path.write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out, indent=2))
print("wrote", path)
