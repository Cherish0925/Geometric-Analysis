"""Local exact checks for round9_global.md; no global Einstein certificate."""

import json
import sympy as sp


def ricci_tensor(g, coords):
    n = len(coords)
    gi = g.inv()
    connection = [[[
        sp.simplify(sum(gi[k, l] * (
            sp.diff(g[l, j], coords[i]) + sp.diff(g[l, i], coords[j])
            - sp.diff(g[i, j], coords[l])) for l in range(n)) / 2)
        for j in range(n)] for i in range(n)] for k in range(n)]
    return sp.Matrix(n, n, lambda i, j: sp.simplify(sum(
        sp.diff(connection[k][i][j], coords[k])
        - sp.diff(connection[k][i][k], coords[j])
        + sum(connection[k][k][l] * connection[l][i][j]
              - connection[k][j][l] * connection[l][i][k]
              for l in range(n)) for k in range(n))))


passed = {}
t, theta, x, y = sp.symbols("t theta x y", real=True)
h = sp.diag(1, sp.exp(sp.sin(theta)), sp.exp(-sp.sin(theta)))
rh = ricci_tensor(h, (theta, x, y))
expected_h = sp.diag(-sp.cos(theta)**2 / 2, sp.sin(theta) / 2, -sp.sin(theta) / 2)
assert sp.simplify(h.inv() * rh - expected_h) == sp.zeros(3)
passed["torus_curvature_and_negative_scalar"] = True

g = sp.diag(1, sp.cosh(t)**2, sp.cosh(t)**2 * h[1, 1], sp.cosh(t)**2 * h[2, 2])
rg = ricci_tensor(g, (t, theta, x, y))
expected_g = sp.diag(-3, *[-3 + (expected_h[i, i] + 2) / sp.cosh(t)**2 for i in range(3)])
ricci_residual = sp.simplify(g.inv() * rg - expected_g).applyfunc(
    lambda expression: sp.cancel(expression.rewrite(sp.exp)))
assert ricci_residual == sp.zeros(4), ricci_residual
passed["complete_warped_ricci_blocks"] = True

v = 1 / sp.cosh(t)**2
assert sp.simplify(-sp.diff(v, t, 2) - 3 * sp.tanh(t) * sp.diff(v, t) - 2 * v) == 0
passed["positive_L2_eigenfunction_equation"] = True

s = sp.symbols("s", real=True)
sigma, psi = sp.Function("sigma")(s), sp.Function("psi")(s)
V = sp.Function("V")(s)
phi = sp.exp(-sigma / 2) * psi
conjugated = sp.simplify(sp.exp(sigma / 2) * (
    -sp.diff(phi, s, 2) - sp.diff(sigma, s) * sp.diff(phi, s) + V * phi))
expected = -sp.diff(psi, s, 2) + (V + sp.diff(sigma, s, 2) / 2 + sp.diff(sigma, s)**2 / 4) * psi
assert sp.simplify(conjugated - expected) == 0
passed["weighted_jacobi_unitary_conjugation"] = True

Q, sn, ss, en, es, sss = sp.symbols("Q sn ss en es sss", real=True)
gauss_second = 3 + sp.Rational(3, 4) * sn**2 + en / 4 + Q / 2 - sp.Rational(3, 4) * ss**2 - es / 4
potential = 3 - Q - sp.Rational(3, 2) * sn**2 - en / 2 + gauss_second / 2 + ss**2 / 4
assert sp.expand(potential - (36 - 6*Q - 9*sn**2 - 3*en - ss**2 - es) / 8) == 0
assert sp.simplify(potential.subs({sn: 0, ss: 0, en: 0, es: 12 + 2*Q}) - (3 - Q)) == 0
passed["charged_separator_potential_and_germ"] = True

p, r, w1, w2 = sp.symbols("p r w1 w2", real=True)
II = sp.Matrix([[-sn, w1/2, w2/2], [w1/2, (sn+p)/2, r/2], [w2/2, r/2, (sn-p)/2]])
expected_norm = sp.Rational(3, 2)*sn**2 + (p**2 + r**2)/2 + (w1**2 + w2**2)/2
assert sp.expand(sp.trace(II.T * II) - expected_norm) == 0
assert sp.trace(II) == 0
passed["full_second_fundamental_form_charge_norm"] = True
print(json.dumps({"passed": len(passed), "checks": passed}, indent=2))
