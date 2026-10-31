#!/usr/bin/env python3
"""Exact algebra behind the convention-independent connection obstruction."""

import sympy as s


def main():
    r = s.symbols("r", integer=True, positive=True)
    assert s.simplify((r - 1) / r**2 + (1 - 1 / r) ** 2 - (r - 1) / r) == 0
    print("PASS: norm squared of the trace-free line projection is (r-1)/r")

    z0, z1, z2 = s.symbols("z0 z1 z2", real=True)
    z3 = -z0 - z1 - z2
    norm = z0**2 + z1**2 + z2**2 + z3**2
    remainder = (z1 + z0 / 3) ** 2 + (z2 + z0 / 3) ** 2 + (z3 + z0 / 3) ** 2
    assert s.expand(norm - s.Rational(4, 3) * z0**2 - remainder) == 0
    print("PASS: sharp rank-four complementary-block Cauchy--Schwarz coefficient")

    a2, t, k2 = s.symbols("a2 T k2", real=True)
    ak = k2 + (a2 - t) / 4
    b2 = 4 * k2 - 4 * ak + a2
    assert s.expand(b2 - t) == 0
    print("PASS: (2k-a)^2 = T from the spinor Chern identity and line splitting")

    gamma = s.diag(1, 1, -1, -1)
    fp = s.Matrix(4, 4, lambda i, j: s.Symbol(f"p{i}{j}"))
    fm = s.Matrix(4, 4, lambda i, j: s.Symbol(f"m{i}{j}"))
    y = (fp + fm + gamma * (fp - fm) * gamma) / 2
    assert s.simplify(s.trace(y) - s.trace(fp)) == 0
    p = s.diag(0, 0, 0, 1)
    assert s.simplify(s.trace(p * y) - s.trace(p * fp)) == 0
    print("PASS: graded projection commutes with the needed trace and line compression")

    commutator = fp * p - p * fp
    selected = {(i, j) for i in range(4) for j in range(4) if (i == 3) != (j == 3)}
    for i in range(4):
        for j in range(4):
            assert s.simplify(commutator[i, j] ** 2 - (fp[i, j] ** 2 if (i, j) in selected else 0)) == 0
    print("PASS: projection commutator retains only selected entries, giving the L4 separation")

    curvature = s.diag(s.Rational(2, 3), s.Rational(2, 3), s.Rational(2, 3), 0)
    z = curvature - s.trace(curvature) * s.eye(4) / 4
    assert z == s.diag(s.Rational(1, 6), s.Rational(1, 6), s.Rational(1, 6), -s.Rational(1, 2))
    assert s.trace(z.T * z) == s.Rational(1, 3)
    assert -s.Rational(1, 3) + 1 == s.Rational(2, 3)
    print("PASS: dual-twist rank-three curvature and sharp rank-four residual")

    # From pi sqrt(T) <= sqrt(3)/2 ||Z||2 + 2 ||DP||4^2.
    assert s.simplify((2 * s.pi / s.sqrt(3)) ** 2 - 4 * s.pi**2 / 3) == 0
    assert s.simplify((s.pi / 2) ** 2 - s.pi**2 / 4) == 0
    assert s.simplify((4 * s.pi**2 / 3) / (2 * s.pi**2) - s.Rational(2, 3)) == 0
    print("PASS: split-defect, exact-ASD mixing, and E_D normalized constants")

    # The matrix wedge bound has room: 4 sum_{i<j} a_i^2 a_j^2 <= 2 (sum a_i^2)^2.
    u = s.symbols("u0:4", real=True)
    lhs = 4 * sum(u[i] ** 2 * u[j] ** 2 for i in range(4) for j in range(i + 1, 4))
    rhs = 2 * sum(x**2 for x in u) ** 2
    assert s.expand(rhs - lhs - 2 * sum(x**4 for x in u)) == 0
    print("PASS: coefficient bound for tr(P DP wedge DP), hence the stated factor 2")
    print("Scope: algebra only; no claim to resolve the published quadratic-map sign")


if __name__ == "__main__":
    main()
