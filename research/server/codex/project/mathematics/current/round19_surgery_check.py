#!/usr/bin/env python3
"""Exact algebra supporting round19_surgery.md; no existence certificate."""

import sympy as s


def zero(expr):
    assert s.simplify(expr) == 0, s.factor(expr)


def check_codazzi_and_slice_ricci():
    c = s.symbols("c1:4", positive=True)
    shape_entries = s.symbols("s11 s22 s33 s12 s13 s23")
    p, q, r, u, v, w = shape_entries
    shape = s.Matrix([[p, u, v], [u, q, w], [v, w, r]])

    def bracket(i, j, k):
        return s.LeviCivita(i, j, k) * c[k]

    def gamma(i, j, k):
        return (bracket(i, j, k) - bracket(j, k, i)
                + bracket(k, i, j)) / 2

    divergence = []
    for i in range(3):
        divergence.append(-sum(
            gamma(j, i, k) * shape[k, j]
            + gamma(j, j, k) * shape[i, k]
            for j in range(3) for k in range(3)))
    for i, j, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        zero(divergence[i] - (c[k] - c[j]) * shape[j, k])

    # R(e_i,e_j)e_k = nabla_i nabla_j e_k - nabla_j nabla_i e_k
    #                  - nabla_[e_i,e_j] e_k; spatial coefficients constant.
    def curvature(i, j, k, ell):
        return sum(gamma(j, k, m) * gamma(i, m, ell)
                   - gamma(i, k, m) * gamma(j, m, ell)
                   - bracket(i, j, m) * gamma(m, k, ell)
                   for m in range(3))

    for i, j, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        ric = sum(curvature(m, i, i, m) for m in range(3))
        zero(ric - (c[i]**2 - (c[j] - c[k])**2) / 2)
    print("PASS: Codazzi mixed coefficients and intrinsic SU(2) Ricci")


def check_rotating_eigenframe():
    x, y, off = s.symbols("x y off", positive=True)
    # lambda_i'' includes 2 G'_ij^2/(lambda_i-lambda_j).
    # Subtract the diagonal evolution of S=G^{-1}G'/2.
    correction = off**2 * (1 / (x * (x - y)) + 1 / (2 * x * y))
    physical_shape_sq = off**2 / (4 * x * y)
    zero(correction - 2 * (x + y) / (x - y) * physical_shape_sq)

    d, e, u, v = s.symbols("d e u v", real=True)
    vector = s.Matrix([u, v])
    diagonal = s.diag(d, e)
    rotation = -(vector * (diagonal * vector).T
                 + (diagonal * vector) * vector.T)
    zero(s.trace(rotation) + 2 * (d * u**2 + e * v**2))
    # The matrix need not be negative semidefinite, despite negative trace.
    zero(rotation.det() + u**2 * v**2 * (d - e)**2)
    print("PASS: rotating-frame term, trace sign, and indefinite-matrix warning")


def check_cone_polynomials():
    a, x, y, z = s.symbols("A X Y Z", positive=True)
    q = 4 + a**2
    r2 = 2 * (y**2 - (x - z)**2) / (x * y * z)
    poly = x**2 - q * x * z + z**2 - y**2
    zero((-r2 - (4 + 2 * a**2) / y) * x * y * z / 2 - poly)
    zero(poly.subs({x: q * a**2, y: a**2})
         - (a**2 - z) * (q**2 * a**2 - a**2 - z))
    # Monotonicity of the remaining long-axis polynomial.
    h, j = s.symbols("h j", nonnegative=True)
    derivative = s.diff(poly, x).subs({x: q * a**2 + h, z: a**2 - j})
    zero(derivative - (q * a**2 + 2 * h + q * j))

    # Initial scalar is -2, the zero-shape constraint for Ric=-g in 4D.
    radii_sq = [q * a**2, a**2, a**2]
    ric = []
    for i, j, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        ric.append(2 * (radii_sq[i]**2
                       - (radii_sq[j] - radii_sq[k])**2)
                   / s.prod(radii_sq))
    zero(sum(ric) + 2)
    print("PASS: short-axis intrinsic barrier and initial Hamiltonian constraint")


def check_uniform_constants():
    # q>=4 implies 2(q-1)/sqrt(q)>=3 and (q+1)/(q-1)<=5/3.
    t = s.symbols("t", nonnegative=True)
    q = 4 + t
    zero(4 * (q - 1)**2 - 9 * q - (15 * t + 4 * t**2))
    zero(s.Rational(5, 3) - (q + 1) / (q - 1)
         - 2 * t / (3 * (t + 3)))
    assert 2 * s.Rational(5, 3) / 9 == s.Rational(10, 27)
    assert -4 + s.Rational(10, 27) == -s.Rational(98, 27)
    # 15/(4A)-sqrt(6)/2>5/(2A) for 0<A<=1 follows from 5/4>sqrt(6)/2.
    assert s.Rational(25, 16) > s.Rational(6, 4)
    assert s.Rational(1, 5) + 2 == s.Rational(11, 5)
    print("PASS: mixed norm, matrix cone, and finite-time constants")


def check_arbitrary_radius_extension():
    a = s.symbols("A", positive=True)
    q = 4 + a**2
    zero((q - 1)**2 - a**2 * q - (2 * a**2 + 9))
    assert 2 * s.Rational(5, 3) / 4 == s.Rational(5, 6)
    assert -1 + s.Rational(1, 2) + s.Rational(5, 6) / 4 == -s.Rational(7, 24)
    ca = 4 + a**2 / 2
    zero(ca - (a / 8)**2 - (4 + s.Rational(31, 64) * a**2))
    assert s.Rational(31, 64) - s.Rational(1, 5) == s.Rational(91, 320)
    assert s.Rational(91, 320)**2 - s.Rational(9, 128) == s.Rational(1081, 102400)
    assert (s.Rational(1, 8) / s.Rational(1, 5)) + 8 == s.Rational(69, 8)
    print("PASS: arbitrary-radius rotation bound, cone margin, uniform lifetime")


if __name__ == "__main__":
    check_codazzi_and_slice_ricci()
    check_rotating_eigenframe()
    check_cone_polynomials()
    check_uniform_constants()
    check_arbitrary_radius_extension()
    print("5 exact check groups passed; no closed surgery construction asserted")
