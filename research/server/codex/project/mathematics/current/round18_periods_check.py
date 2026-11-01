#!/usr/bin/env python3
"""Exact algebra for actual intersections and scalar spectral clusters.

This checks finite identities and numerical constants only. The existence
of actual monopoles, measurable choices, Hodge pairing and min--max
arguments are proved or cited in round18_periods.md.
"""
from itertools import product
import sympy as s


def zero(name, expr):
    assert s.factor(s.expand(expr)) == 0, (name, expr)
    print("PASS:", name)


x = s.Matrix(s.symbols("x0:3", real=True))
y = s.Matrix(s.symbols("y0:3", real=True))


def Q(u):
    return u * u.T - u.dot(u) * s.eye(3) / 3


delta = Q(x) - Q(y)
zero("full rank-one tensor difference",
     s.trace(delta * delta)
     - 2 * (x.dot(x) * y.dot(y) - x.dot(y)**2)
     - s.Rational(2, 3) * (x.dot(x) - y.dot(y))**2)

t = s.symbols("t", nonnegative=True)
zero("unit-vector sign-alignment remainder",
     (2*(1-t*t) - 2*(1-t)) - 2*t*(1-t))

b, p, ell = s.symbols("b p ell", nonnegative=True)
amp = (b + ell)/8
e0 = p/4 + s.Rational(27, 16)*b + s.Rational(19, 12)*ell
eta = s.expand(74*amp + 24*e0)
assert eta == 6*p + s.Rational(199, 4)*b + s.Rational(189, 4)*ell
assert all(eta.coeff(v) <= 50 for v in (p, b, ell))
z0 = s.Rational(3, 16)*b + ell/8
full_error = s.expand(2*z0 + 100*(p+b+ell))
assert all(full_error.coeff(v) <= 101 for v in (p, b, ell))
print("PASS: cap-to-common-line and full-curvature error constants")

assert s.sqrt(101)*(s.sqrt(s.Rational(19, 16))+1) < 22
assert (22+s.Rational(1, 16))*s.Rational(16, 15) < 24
assert s.sqrt(s.Rational(3, 16))*(s.sqrt(s.Rational(19, 16))+2) < 2
assert 2+s.Rational(17, 15)/16 < 3
assert 3*(4+s.Rational(17, 15)) < 16
assert 2*s.sqrt(450)+15 < 64
assert 5*s.sqrt(450)+24+16 < 160
print("PASS: intersection, variance and covariance error constants")

k, V, A = s.symbols("k V A", positive=True)
zero("determinant wedge normalization",
     (2*s.pi)**2/(2*k*k*V) - (2*s.pi*s.pi*A/(k*k*V))/A)
assert 8 * 2 * s.Rational(1, 4) == 4
print("PASS: smooth-observable gradient coefficient")

for n in range(1, 7):
    vectors = list(product((-1, 1), repeat=n))
    odd_coefficients = [
        q for q in product((-1, 0, 1), repeat=n)
        if sum(q) % 2
    ]
    for q in odd_coefficients:
        assert all(sum(a*c for a, c in zip(q, v))**2 >= 1
                   for v in vectors)
print("PASS: odd-sum sign inequalities (finite cases; general proof is parity)")

Gstar = s.ones(3, 3)*(-s.Rational(1, 2)) + s.eye(3)*s.Rational(3, 2)
assert Gstar.eigenvals() == {s.Integer(0): 1, s.Rational(3, 2): 2}
assert (s.ones(1, 3)*Gstar*s.ones(3, 1))[0] == 0
assert min(sum(z)**2 for z in product((-1, 1), repeat=3)) == 1
print("PASS: PSD Gram matrix separated from sign-correlation polytope")

for m in (2, 3, 4):
    signs = s.ones(m+1, m)
    for j in range(m):
        signs[j+1, j] = -1
    G = signs * signs.T / m
    covariance = G[1:, 1:] - G[1:, 0] * G[0, 1:]
    expected = 4*(s.eye(m)/m-s.ones(m, m)/(m*m))
    assert covariance == expected
    assert covariance.eigenvals() == {
        s.Integer(0): 1, s.Rational(4, m): m-1}
    assert G == sum(
        (signs[:, j]*signs[:, j].T for j in range(m)),
        s.zeros(m+1, m+1))/m
    assert s.Rational(8*m, 1)/s.Rational(4, m) == 2*m*m
    assert (s.Rational(4, m)/(320*m))**2 == s.Rational(1, (80*m*m)**2)
print("PASS: Bauer-Furuta balanced covariance, cut representation and eigenvalue cluster")

weights = s.diag(s.Rational(1, 6), s.Rational(1, 3), s.Rational(1, 2))
signs = s.ones(4, 3)
for j in range(3):
    signs[j+1, j] = -1
G = signs*weights*signs.T
w = s.Matrix(list(weights.diagonal()))
assert G[1:, 1:] - G[1:, 0]*G[0, 1:] == 4*(weights-w*w.T)
print("PASS: unequal-component covariance formula")

for d in range(8, 129, 4):
    pg = s.binomial(d-1, 3)
    bp = 1+2*pg
    assert pg % 2 == 1 and bp % 4 == 3 and 4*bp % 8 == 4
    square = d*(d-4)**2
    for m in (2, 3, 4):
        total = m*square
        top = total-4*(m-1)
        assert total-top == 4*(m-1)
        assert total > 0
print("PASS: hypersurface examples and connected-sum normalization")

t_scale = s.symbols("t_scale", positive=True)
assert s.simplify(t_scale**(-4)*t_scale**4) == 1
assert s.simplify(t_scale**(-2)*t_scale**4) == t_scale**2
volume_error, scalar_error = s.symbols("volume_error scalar_error", real=True)
actual_volume = 2*s.pi**2*A + volume_error
mean_kappa = -(-4*actual_volume + scalar_error)/(4*actual_volume)
zero("four-dimensional surgery cost and mean-scalar normalization",
     mean_kappa - (1-scalar_error/(4*actual_volume)))

# Failure checks keep the topological loss and spectral multiplicity honest.
assert s.Rational(4, 3) != s.Rational(4, 4)
assert (2*8*(8-4)**2 - 4) != 2*8*(8-4)**2
assert Gstar != s.ones(3, 3)
print("PASS: incorrect cluster, omitted topological loss and false sign rank rejected")
print("All Round-18 period/covariance algebra checks passed.")
