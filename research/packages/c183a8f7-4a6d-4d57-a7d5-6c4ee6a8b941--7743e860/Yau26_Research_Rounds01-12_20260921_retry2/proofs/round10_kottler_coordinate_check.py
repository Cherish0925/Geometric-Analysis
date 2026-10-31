"""Direct coordinate Ricci calculation for the explicit doubled Kottler family.

Coordinates (u, phi, z, w), y=d*cosh(u), p=d*sinh(u).
The surface metric dz^2+exp(2z)dw^2 has curvature -1.
No warped-product Ricci formulas are used in this checker.
Run: qiushi-yau26 env numeric python round10_kottler_coordinate_check.py
"""

import sympy as s

y, d = s.symbols("y d", positive=True)
p, z = s.symbols("p z", real=True)
F = y**2 * (y + 3) / (3 * (y + 1))
diag = [(y + 1) / (y + 3), F, (y + 1)**2 / 3,
        (y + 1)**2 * s.exp(2*z) / 3]


def reduce(expr):
    """Use p^2=y^2-d^2 after rational simplification."""
    expr = s.cancel(expr)
    num, den = s.fraction(expr)
    num = s.rem(num, p*p - y*y + d*d, p)
    den = s.rem(den, p*p - y*y + d*d, p)
    return s.factor(num / den)


def D(expr, i):
    if i == 0:
        return s.diff(expr, y)*p + s.diff(expr, p)*y
    if i == 2:
        return s.diff(expr, z)
    return s.S.Zero


def metric(i, j):
    return diag[i] if i == j else s.S.Zero


Gamma = {}
for k in range(4):
    for i in range(4):
        for j in range(4):
            value = reduce((D(metric(k, j), i) + D(metric(k, i), j)
                            - D(metric(i, j), k)) / (2*diag[k]))
            if value != 0:
                Gamma[k, i, j] = value


def C(k, i, j):
    return Gamma.get((k, i, j), s.S.Zero)


Ric = s.zeros(4)
for i in range(4):
    for j in range(4):
        value = 0
        for k in range(4):
            value += D(C(k, i, j), k) - D(C(k, i, k), j)
            for ell in range(4):
                value += C(k, i, j)*C(ell, k, ell)
                value -= C(ell, i, k)*C(k, j, ell)
        Ric[i, j] = reduce(value)

radial = -3*d*d/(y*(y + 1)**2)
tangent = d*d*(2*y + 3)/(y*(y + 1)**2)
expected = [radial, tangent, tangent, tangent]
count = 0
for i in range(4):
    for j in range(4):
        actual = Ric[i, j] / diag[i] + (3 if i == j else 0)
        want = expected[i] if i == j else 0
        assert reduce(actual - want) == 0, (i, j, actual, want)
        count += 1
print(f"PASS all {count} coordinate Ricci-endomorphism entries")

assert s.factor(tangent + radial) == 2*d*d/(y + 1)**2
assert s.factor(s.diff(tangent, y)) == -d*d*(4*y*y + 9*y + 3)/(y*y*(y + 1)**3)
maximum = d*(2*d + 3)/(d + 1)**2
assert s.simplify(tangent.subs(y, d) - maximum) == 0
assert s.simplify(3*d - maximum - d*d*(3*d + 4)/(d + 1)**2) == 0
print("PASS exact global defect = d(2d+3)/(1+d)^2 < 3d")

# With y=d*cosh(u), every diagonal entry is a positive smooth even
# function near u=0; the minimum circle radius is not zero for d>0.
throat = [s.factor(value.subs(y, d)) for value in diag]
assert s.simplify(throat[0] - (d + 1)/(d + 3)) == 0
assert s.simplify(throat[1] - d*d*(d + 3)/(3*(d + 1))) == 0
print("PASS smooth positive throat coefficient identities")
print("These are exact local tensor/algebra checks, not a closed-manifold construction.")
