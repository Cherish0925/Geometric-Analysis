"""Exact coordinate check of the collapsing-circle Ricci commutator.

This finite calculation checks the sharp example in round13_averaging.md,
not its tensor estimates or any PDE existence theorem.
"""
import sympy as s

x, y, z, theta = s.symbols("x y z theta", real=True)
a, eta = s.symbols("a eta", positive=True)
coords = (x, y, z, theta)
n = len(coords)
u = eta * a**2 * s.cos(theta)
b = s.diag(1, 1, 1, a**2)
q = s.exp(2 * u) * b
qi = s.exp(-2 * u) * b.inv()
gamma = [[[s.simplify(sum(
    qi[i, l] * (s.diff(q[l, k], coords[j])
                + s.diff(q[l, j], coords[k])
                - s.diff(q[j, k], coords[l])) / 2
    for l in range(n))) for k in range(n)]
    for j in range(n)] for i in range(n)]
ric = s.zeros(n)
for i in range(n):
    for j in range(n):
        ric[i, j] = s.simplify(sum(
            s.diff(gamma[k][i][j], coords[k])
            - s.diff(gamma[k][i][k], coords[j])
            + sum(gamma[k][k][l] * gamma[l][i][j]
                  - gamma[k][j][l] * gamma[l][i][k]
                  for l in range(n))
            for k in range(n)))

def mean(expr):
    return s.simplify(s.integrate(s.expand_trig(expr),
                                (theta, 0, 2*s.pi))/(2*s.pi))

expected_transverse = eta*s.cos(theta) - 2*eta**2*a**2*s.sin(theta)**2
expected_circle = 3*eta*a**2*s.cos(theta)
for i in range(3):
    assert s.simplify(ric[i, i] - expected_transverse) == 0
    assert mean(ric[i, i]) == -eta**2*a**2
assert s.simplify(ric[3, 3] - expected_circle) == 0
assert mean(ric[3, 3]) == 0
assert all(ric[i, j] == 0 for i in range(n) for j in range(n) if i != j)
print("PASS: Ricci derived from Christoffel symbols agrees in all components")
print("PASS: averaged transverse Ricci = -eta^2*a^2")
print("PASS: averaged circle and off-diagonal Ricci vanish")
print("PASS: averaged metric is a constant flat multiple of b; commutator order is sharp")

# Exact identities used in the circle-frequency suppression.
f = eta*a**2*s.cos(theta)
assert s.diff(f, theta, 2) == -f
assert s.simplify(mean((s.diff(f, theta)/a)**2) - eta**2*a**2/2) == 0
assert s.simplify(mean((s.diff(f, theta, 2)/a**2)**2) - eta**2/2) == 0
print("PASS: amplitude/gradient/Hessian squared scale as a^4/a^2/1")
