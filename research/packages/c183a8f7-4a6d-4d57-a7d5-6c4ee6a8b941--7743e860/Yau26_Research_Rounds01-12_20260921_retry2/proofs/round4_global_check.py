"""Exact curvature and full-matrix checks for the round-four Nil obstruction."""

import sympy as s

# Derive slice Ricci from the Koszul formula in an orthonormal Nil frame.
beta = s.symbols("beta", positive=True)
C = [[[s.Integer(0) for k in range(3)] for j in range(3)] for i in range(3)]
C[0][1][2] = beta
C[1][0][2] = -beta
Gamma = [[[s.simplify((C[i][j][k] - C[j][k][i] + C[k][i][j]) / 2)
           for k in range(3)] for j in range(3)] for i in range(3)]


def curvature(i, j, k, ell):
    return s.simplify(sum(
        Gamma[j][k][a] * Gamma[i][a][ell]
        - Gamma[i][k][a] * Gamma[j][a][ell]
        - C[i][j][a] * Gamma[a][k][ell]
        for a in range(3)))


Ric = s.Matrix(3, 3, lambda j, k: sum(curvature(i, j, k, i) for i in range(3)))
mu = beta**2 / 2
assert Ric == s.diag(-mu, -mu, mu)
assert curvature(0, 1, 1, 0) == -3 * beta**2 / 4
assert curvature(0, 2, 2, 0) == beta**2 / 4
assert curvature(1, 2, 2, 1) == beta**2 / 4
print("PASS: Koszul derivation of all nine slice Ricci components")

# At an arbitrary time use a metric-orthonormal fixed frame with e3 central.
# S and S' are fully arbitrary symmetric matrices at this time.  The raw
# metric jets G'=2S, G''=2S'+4S^2 retain all changing-eigenframe terms.
u = s.symbols("u0:6", real=True)
d = s.symbols("d0:6", real=True)


def symm(v):
    return s.Matrix([[v[0], v[1], v[2]],
                     [v[1], v[3], v[4]],
                     [v[2], v[4], v[5]]])


S, Sp = symm(u), symm(d)
G1, G2 = 2 * S, 2 * Sp + 4 * S * S
lam = s.symbols("lambda", positive=True)
H, Hp = s.trace(S), s.trace(Sp)
ET = Ric + lam * s.eye(3) - Sp - H * S
E00 = lam - Hp - s.trace(S * S)
chi1 = G1[2, 2] - s.trace(G1) / 2
chi2 = (G2[2, 2] - G1[2, 2]**2
        - s.trace(G2) / 2 + s.trace(G1 * G1) / 2)
mix2 = S[0, 2]**2 + S[1, 2]**2
rhs = -lam + 3 * mu + s.trace(ET) - 2 * ET[2, 2] + 4 * mix2
assert s.expand(chi2 + H * chi1 - rhs) == 0
assert s.expand(chi1 - (2 * S[2, 2] - H)) == 0
assert s.expand(chi2 - (2 * Sp[2, 2] - Hp) - 4 * mix2) == 0
print("PASS: moving central vector and positive +4 mixing term for full matrices")

gauss = -2 * lam + H**2 - s.trace(S * S) + s.trace(ET) - E00
assert s.expand(gauss - s.trace(Ric)) == 0
print("PASS: full scalar constraint including residual signs")

eps = s.symbols("epsilon", nonnegative=True)
assert s.solve(s.Eq(2 * lam - 4 * eps, lam / 3 + eps), eps) == [lam / 3]
assert s.solve(s.Eq(2 * lam, 4 * eps), eps) == [lam / 2]
print("PASS: Nil epsilon >= lambda/3 and radial torus epsilon >= lambda/2")

# Exact Einstein cusp retained in the Skill, normalized Ric=-g.
rates = s.diag(1 / s.sqrt(6), 1 / s.sqrt(6), 2 / s.sqrt(6))
cusp_mu = s.Rational(1, 3)
cusp_Ric_slice = s.diag(-cusp_mu, -cusp_mu, cusp_mu)
assert s.simplify(-s.trace(rates * rates)) == -1
assert s.simplify(cusp_Ric_slice - s.trace(rates) * rates) == -s.eye(3)
print("PASS: all normal/tangential components of the allowed exact Nil cusp")

# Invariant bracket normalization under an arbitrary metric at a sample time:
# beta^2=G(Z,Z)^2/det(G), independent of the chosen horizontal lift.
G = s.Matrix([[4, 1, 2], [1, 3, 1], [2, 1, 5]])
Z = s.Matrix([0, 0, 1])
horizontal1 = s.Matrix([1, 0, -s.Rational(2, 5)])
horizontal2 = s.Matrix([0, 1, -s.Rational(1, 5)])
assert (horizontal1.T * G * Z)[0] == 0
assert (horizontal2.T * G * Z)[0] == 0
horizontal_G = s.Matrix([[ (v.T * G * w)[0]
                         for w in (horizontal1, horizontal2)]
                        for v in (horizontal1, horizontal2)])
assert s.simplify(G[2, 2] / horizontal_G.det() - G[2, 2]**2 / G.det()) == 0
print("PASS: physical bracket normalization with nonzero central cross terms")
print("All exact round-four global checks passed.")
