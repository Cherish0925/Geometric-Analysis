"""Coordinate verification of the twisted surface-cusp doubling core.

g = dt^2 + a(t)^2 (dphi + k exp(z) dw)^2
    + (dz^2 + exp(2z) dw^2)/3,  a'' = 3a.
Uses only the coordinate Christoffel and Ricci definitions.
Run: qiushi-yau26 env numeric python round10_cusp_doubling_check.py
"""

import sympy as s

a, d = s.symbols("a d", positive=True)
p, k, z = s.symbols("p k z", real=True)
g = s.diag(1, a*a, s.Rational(1, 3),
           s.exp(2*z)*(s.Rational(1, 3) + a*a*k*k))
g[1, 3] = g[3, 1] = a*a*k*s.exp(z)
inverse = s.simplify(g.inv())


def clean(expr):
    num, den = s.fraction(s.cancel(expr))
    return s.factor(s.rem(num, p*p - 3*(a*a - d*d), p) /
                    s.rem(den, p*p - 3*(a*a - d*d), p))


def D(expr, i):
    if i == 0:
        return p*s.diff(expr, a) + 3*a*s.diff(expr, p)
    if i == 2:
        return s.diff(expr, z)
    return s.S.Zero


C = {}
for out in range(4):
    for i in range(4):
        for j in range(4):
            value = sum(inverse[out, ell] *
                        (D(g[ell, j], i) + D(g[ell, i], j) -
                         D(g[i, j], ell)) / 2 for ell in range(4))
            value = clean(value)
            if value != 0:
                C[out, i, j] = value


def Gamma(out, i, j):
    return C.get((out, i, j), s.S.Zero)


Ric = s.zeros(4)
for i in range(4):
    for j in range(4):
        value = 0
        for out in range(4):
            value += D(Gamma(out, i, j), out) - D(Gamma(out, i, out), j)
            for ell in range(4):
                value += Gamma(out, i, j)*Gamma(ell, out, ell)
                value -= Gamma(ell, i, out)*Gamma(out, j, ell)
        Ric[i, j] = clean(value)

theta = s.Matrix([0, 1, 0, k*s.exp(z)])
base = s.diag(0, 0, s.Rational(1, 3), s.exp(2*z)/3)
ev = 9*k*k*a*a/2
want = ev*(a*a*theta*theta.T - base)
E = Ric + 3*g
for i in range(4):
    for j in range(4):
        assert clean(E[i, j] - want[i, j]) == 0, (i, j)
print("PASS all 16 twisted-core coordinate Ricci components")

# Orthonormal frame (radial, vertical, horizontal base 1, base 2).
B = s.Matrix([[1, 0, 0, 0],
              [0, 1/a, 0, -s.sqrt(3)*k],
              [0, 0, s.sqrt(3), 0],
              [0, 0, 0, s.sqrt(3)*s.exp(-z)]])
assert s.simplify(B.T*g*B - s.eye(4)) == s.zeros(4)
assert s.simplify(B.T*E*B - s.diag(0, ev, -ev, -ev)) == s.zeros(4)
print("PASS exact four error eigenvalues and zero mixed blocks")

area, ell = s.symbols("area ell", positive=True)
f = 2*s.pi*ell/area
central_error = d*d*f*f/2
chern_lower = s.pi**2*ell**2*d*d/area**2
assert s.simplify(central_error - 2*chern_lower) == 0
assert s.simplify((area*d*d)*(area*d**-4) - area**2/d**2) == 0
print("PASS nonzero-Chern lapse-escape identities")
print("The global source and collar estimate are proved in the accompanying note.")
