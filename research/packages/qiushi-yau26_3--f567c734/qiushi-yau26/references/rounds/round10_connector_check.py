"""Exact coordinate checks for charge transport with full Ricci error.

The examples deliberately have variable shape, lapse, base metric and charge.
This checks the reduced identities, not existence of a complete connector.
"""

import json
import sympy as s


def ricci_at(metric, coords, point):
    n = len(coords)
    g = metric.subs(point)
    inv = g.inv()
    dg = [metric.diff(x).subs(point) for x in coords]
    ddg = [[metric.diff(x, y).subs(point) for y in coords] for x in coords]
    dinv = [-inv * d * inv for d in dg]
    gamma = [[[sum(inv[k, l] * (dg[i][l, j] + dg[j][l, i] - dg[l][i, j])
                      for l in range(n)) / 2
               for j in range(n)] for i in range(n)] for k in range(n)]

    def derivative(a, k, i, j):
        return sum(
            dinv[a][k, l] * (dg[i][l, j] + dg[j][l, i] - dg[l][i, j])
            + inv[k, l] * (ddg[a][i][l, j] + ddg[a][j][l, i] - ddg[a][l][i, j])
            for l in range(n)) / 2

    return s.Matrix(n, n, lambda i, j: s.factor(sum(
        derivative(k, k, i, j) - derivative(j, k, i, k)
        + sum(gamma[k][k][l] * gamma[l][i][j]
              - gamma[k][j][l] * gamma[l][i][k] for l in range(n))
        for k in range(n))))


x, y, u, v = s.symbols("x y u v", real=True)
coords = (x, y, u, v)
b = 1 + x*x + y*y
rho = 2 + x + y*y
shear = x*y
G = rho * s.Matrix([[1 + shear*shear, shear], [shear, 1]])
A = s.Matrix([[0, x + x*x*y], [0, x*x - x*y]])
coframe = s.eye(4)
coframe[2:, :2] = A
block_metric = s.diag(b*b, b*b, 1, 1)
block_metric[2:, 2:] = G
metric = coframe.T * block_metric * coframe
f = s.Matrix([s.diff(A[a, 1], x) / b**2 for a in range(2)])
charge = s.simplify(rho * G * f)
checks = []
for point in ({x: 0, y: 0, u: 0, v: 0},
              {x: s.Rational(1, 3), y: s.Rational(-1, 2), u: 0, v: 0}):
    Ric = ricci_at(metric, coords, point)
    horizontal_frame = coframe.inv().subs(point)
    reduced_Ric = s.simplify(horizontal_frame.T * Ric * horizontal_frame)
    # Orientation dx wedge dy: R(Hx,Ka)=+(2rho)^-1 partial_y q_a,
    # R(Hy,Ka)=-(2rho)^-1 partial_x q_a.
    expected = s.Matrix(2, 2, lambda i, a:
        (s.diff(charge[a], y) if i == 0 else -s.diff(charge[a], x))
        / (2*rho)).subs(point)
    assert s.simplify(reduced_Ric[:2, 2:] - expected) == s.zeros(2), (
        reduced_Ric[:2, 2:], expected)
    assert expected != s.zeros(2), "A constant-charge test would miss leakage."
    checks.append("coordinate_mixed_block_and_nonconstant_charge")
    mixed_norm = s.trace(G.subs(point).inv() * expected.T * expected) / b.subs(point)**2
    dq = s.Matrix(2, 2, lambda i, a: s.diff(charge[a], (x, y)[i])).subs(point)
    expected_norm = s.trace(G.subs(point).inv() * dq.T*dq) / (
        4*rho.subs(point)**2*b.subs(point)**2)
    assert s.factor(mixed_norm - expected_norm) == 0
    checks.append("full_mixed_norm_identity")

g11, g12, g22, f1, f2 = s.symbols("g11 g12 g22 f1 f2", real=True)
r2 = g11*g22-g12*g12
q1 = g11*f1 + g12*f2  # divided by rho
assert s.factor(f1 + g12/g11*f2 - q1/g11) == 0
checks.append("circle_curvature_horizontal_component")

eps, Amax, Dmax, q0 = s.symbols("eps Amax Dmax q0", positive=True)
threshold = q0 / (Amax + s.sqrt(Amax*Amax + 2*Dmax*q0))
assert s.simplify(2*Dmax*threshold**2 + 2*Amax*threshold - q0) == 0
checks.append("conditional_gap_root")

print(json.dumps({"passed": len(checks), "checks": checks}, indent=2))
