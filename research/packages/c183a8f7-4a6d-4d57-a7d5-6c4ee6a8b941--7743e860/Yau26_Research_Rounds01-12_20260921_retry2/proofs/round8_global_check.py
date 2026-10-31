"""Exact local identities used in round8_global.md; not a global proof checker."""

import json
import sympy as sp


def ricci_tensor(metric, coordinates):
    n = len(coordinates)
    inverse = metric.inv()
    gamma = [
        [
            [
                sp.cancel(
                    sum(
                        inverse[k, l]
                        * (
                            sp.diff(metric[l, j], coordinates[i])
                            + sp.diff(metric[l, i], coordinates[j])
                            - sp.diff(metric[i, j], coordinates[l])
                        )
                        for l in range(n)
                    )
                    / 2
                )
                for j in range(n)
            ]
            for i in range(n)
        ]
        for k in range(n)
    ]
    ricci = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            ricci[i, j] = sp.cancel(
                sum(
                    sp.diff(gamma[k][i][j], coordinates[k])
                    - sp.diff(gamma[k][i][k], coordinates[j])
                    + sum(
                        gamma[k][k][l] * gamma[l][i][j]
                        - gamma[k][j][l] * gamma[l][i][k]
                        for l in range(n)
                    )
                    for k in range(n)
                )
            )
    return ricci


def scalar_curvature(metric, coordinates):
    inverse = metric.inv()
    ricci = ricci_tensor(metric, coordinates)
    n = len(coordinates)
    return sp.cancel(sum(inverse[i, j] * ricci[i, j] for i in range(n) for j in range(n)))


checks = {}
s, x, y = sp.symbols("s x y", real=True)
a, b, c = [sp.Function(name)(s) for name in ("a", "b", "c")]
G = sp.Matrix([[a, b], [b, c]])
metric = sp.diag(1, 1, 1)
metric[1:3, 1:3] = G
curvature = scalar_curvature(metric, (s, x, y))
T = G.inv() * G.diff(s)
sigma_prime = sp.trace(T) / 2
shape = T - sigma_prime * sp.eye(2)
e_tan = sp.trace(shape * shape) / 2
expected = -2 * sp.diff(sigma_prime, s) - sp.Rational(3, 2) * sigma_prime**2 - e_tan / 2
assert sp.cancel(curvature - expected) == 0
checks["arbitrary_symmetric_fibre_scalar_identity"] = True
assert sp.cancel(curvature - (expected + sp.diff(sigma_prime, s))) != 0
checks["missing_area_hessian_detected"] = True

u, v = sp.symbols("u v", real=True)
M = sp.Matrix([[sp.exp(u), sp.exp(u) * v], [sp.exp(u) * v, sp.exp(-u) + sp.exp(u) * v**2]])
target = sp.Matrix(
    2, 2,
    lambda i, j: sp.simplify(sp.trace(M.inv() * M.diff((u, v)[i]) * M.inv() * M.diff((u, v)[j])) / 2),
)
assert target == sp.diag(1, sp.exp(2 * u))
assert sp.simplify(scalar_curvature(target, (u, v))) == -2
checks["shape_target_curvature_minus_one"] = True

lam1, lam2 = sp.symbols("lam1 lam2", nonnegative=True)
e = lam1 + lam2
quartic = e**2 - (lam1**2 + lam2**2) / 2
assert sp.expand(quartic - e**2 / 2) == lam1 * lam2
assert sp.factor(-3 * e + e**2 / 2) == e * (e - 6) / 2
checks["bochner_ceiling_six_algebra"] = True

area_second, ii_squared, tangential = sp.symbols("area_second ii_squared tangential", real=True)
floor = sp.solve(sp.Eq(-2 * area_second - tangential / 2, -6 - ii_squared), tangential)[0]
assert floor == 12 + 2 * ii_squared - 4 * area_second
checks["minimal_separator_floor_twelve"] = True

t, z, xi, eta = sp.symbols("t z xi eta", real=True)
aa, bb = sp.symbols("aa bb", positive=True)
f1, f2 = sp.symbols("f1 f2", real=True)
coframe = sp.eye(4)
coframe[2, 1] = f1 * t
coframe[3, 1] = f2 * t
charged_metric = coframe.T * sp.diag(1, 1, aa, bb) * coframe
charged_ricci = ricci_tensor(charged_metric, (t, z, xi, eta))
assert sp.cancel(charged_ricci[2, 3] - aa * bb * f1 * f2 / 2) == 0
checks["offdiagonal_vertical_twist_coefficient"] = True

shear, rho, charge = sp.symbols("shear rho charge", real=True, nonzero=True)
M_charge = sp.Matrix([
    [sp.exp(-u) + sp.exp(u) * shear**2, sp.exp(u) * shear],
    [sp.exp(u) * shear, sp.exp(u)],
])
charge_vector = sp.Matrix([charge, 0])
Q = sp.simplify((charge_vector.T * M_charge.inv() * charge_vector)[0] / (2 * rho**3))
assert Q == charge**2 * sp.exp(u) / (2 * rho**3)
assert sp.diff(Q, shear) == 0
target_charge = sp.Matrix(
    2, 2,
    lambda i, j: sp.simplify(sp.trace(M_charge.inv() * M_charge.diff((u, shear)[i]) * M_charge.inv() * M_charge.diff((u, shear)[j])) / 2),
)
assert target_charge == sp.diag(1, sp.exp(2 * u))
assert sp.simplify(sp.diff(target_charge[1, 1], u) / (2 * target_charge[1, 1])) == 1
checks["charge_adapted_shear_potential_and_current"] = True
print(json.dumps({"passed": len(checks), "checks": checks}, indent=2))
