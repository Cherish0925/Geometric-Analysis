#!/usr/bin/env python3
"""Exact local identities for the collar-complement proof (SymPy only).

The operator check starts from coordinate Christoffel symbols and the full
covariant Hessian of a symmetric tensor. It does not implement the scalar
radial formula as the definition of the tensor operator.
"""

import json
import sympy as s

t, phi = s.symbols("t phi", real=True)
k, c = s.symbols("k c", positive=True)
a = s.Function("a")(t)
v, w, u = (s.Function(name)(t) for name in ("v", "w", "u"))
coords = [t, phi]
g = s.diag(1, a**2)
gi = g.inv()
Gamma = [
    [
        [
            s.simplify(sum(gi[r, z] * (
                s.diff(g[z, j], coords[i]) + s.diff(g[z, i], coords[j])
                - s.diff(g[i, j], coords[z])) / 2 for z in range(2)))
            for j in range(2)
        ] for i in range(2)
    ] for r in range(2)
]
q = s.Matrix([[v, a*w], [a*w, -a**2*v]])
dq = [[[s.simplify(s.diff(q[i, j], coords[p]) - sum(
    Gamma[r][p][i]*q[r, j] + Gamma[r][p][j]*q[i, r]
    for r in range(2))) for j in range(2)] for i in range(2)] for p in range(2)]


def d2(p, r, i, j):
    return s.diff(dq[r][i][j], coords[p]) - sum(
        Gamma[z][p][r]*dq[z][i][j]
        + Gamma[z][p][i]*dq[r][z][j]
        + Gamma[z][p][j]*dq[r][i][z]
        for z in range(2))


rough = s.Matrix(2, 2, lambda i, j: s.simplify(-sum(
    gi[p, r]*d2(p, r, i, j) for p in range(2) for r in range(2))))
P = rough/2 - k**2*q  # Trace-free curvature action at K=-k^2.
kappa = s.diff(a, t)/a


def L(z):
    return -(s.diff(z, t, 2) + kappa*s.diff(z, t))/2 + (2*kappa**2-k**2)*z


expected = s.Matrix([[L(v), a*L(w)], [a*L(w), -a**2*L(v)]])
assert all(s.simplify(x) == 0 for x in P-expected)
div = [s.simplify(-sum(gi[p, r]*dq[p][r][j]
                      for p in range(2) for r in range(2))) for j in range(2)]
assert s.simplify(div[0] + s.diff(v, t) + 2*kappa*v) == 0
assert s.simplify(div[1]/a + s.diff(w, t) + 2*kappa*w) == 0

a0 = c*s.cosh(k*t)
kap0 = k*s.tanh(k*t)
f = s.sech(k*t)**2


def simplify_hyperbolic(z):
    return s.factor(s.simplify(s.expand_trig(z.rewrite(s.exp))))


def L0(z):
    return -(s.diff(z, t, 2)+kap0*s.diff(z, t))/2 + (2*kap0**2-k**2)*z


assert simplify_hyperbolic(L0(f)) == 0
assert simplify_hyperbolic(s.diff(f, t)+2*kap0*f) == 0
# Conjugation potential obtained by applying to a^{-1/2}; the leading
# coefficient and cancellation of the first derivative are checked below.
pot = s.Rational(9, 4)*k**2-s.Rational(15, 4)*k**2*s.sech(k*t)**2
asqrt = s.sqrt(a0)
conjugated = s.expand(2*asqrt*L0(u/asqrt))
assert simplify_hyperbolic(s.diff(conjugated, s.diff(u, t, 2)) + 1) == 0
assert simplify_hyperbolic(s.diff(conjugated, s.diff(u, t))) == 0
assert simplify_hyperbolic(conjugated + s.diff(u, t, 2)-pot*u) == 0


def A(z, b):
    return s.diff(z, t)+b*k*s.tanh(k*t)*z


def At(z, b):
    return -s.diff(z, t)+b*k*s.tanh(k*t)*z


assert simplify_hyperbolic(At(A(u, s.Rational(3, 2)), s.Rational(3, 2))
                           + s.diff(u, t, 2)-pot*u) == 0
assert simplify_hyperbolic(
    A(At(u, s.Rational(3, 2)), s.Rational(3, 2))
    - At(A(u, s.Rational(1, 2)), s.Rational(1, 2))-2*k**2*u) == 0
scalar_conj = s.expand(asqrt*(-s.diff(u/asqrt, t, 2)-kap0*s.diff(u/asqrt, t)))
assert simplify_hyperbolic(scalar_conj+s.diff(u, t, 2)
        -k**2*(1+s.sech(k*t)**2)*u/4) == 0
assert simplify_hyperbolic(a0*f**2-c*s.sech(k*t)**3) == 0

# Deliberately wrong profiles/potentials must fail.
assert simplify_hyperbolic(L0(s.sech(k*t))) != 0
assert simplify_hyperbolic(pot-(9*k**2/4-3*k**2*s.sech(k*t)**2/4)) != 0
assert s.simplify(expected[0, 1]) != 0  # The second polarization is real.
print(json.dumps({
    "coordinate_tensor_operator": "both trace-free polarizations passed",
    "coordinate_divergence": "both polarizations passed",
    "radial_kernel_and_conjugation": "passed",
    "factorization_and_partner_gap": "passed",
    "scalar_sector_and_cutoff_weight": "passed",
    "wrong_profile_and_wrong_potential_rejected": True,
    "scope": "exact local algebra; analytic complement proof is in round14_collar_complement.md"
}, indent=2))
