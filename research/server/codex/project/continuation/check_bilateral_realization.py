#!/usr/bin/env python3
"""Exact algebra only; does not certify the PDE or geometric compactness."""

import sympy as s


def main():
    S, P, T, p, V = s.symbols("S P T p V", real=True, nonzero=True)
    W = (4 * s.pi**2 * T - S / 24 + P / 2) / 2
    R = P + S / 4
    deficit = s.Rational(3, 2) * (S + 12 * W) - 72 * s.pi**2 * p
    assert s.simplify(deficit - s.Rational(9, 2) * (R - 8 * s.pi**2 * (2 * p - T))) == 0

    chi, tau, pp, pm, ap, am = s.symbols("chi tau pp pm ap am", real=True)
    qp = s.Rational(9, 2) * (R - 8 * s.pi**2 * (2 * pp - 2 * chi - 3 * tau)) / V
    qm = s.Rational(9, 2) * (R - 8 * s.pi**2 * (2 * pm - 2 * chi + 3 * tau)) / V
    e = (R - 8 * s.pi**2 * (ap + am - 2 * chi)) / V
    assert s.simplify(e - (qp + qm) / 9 - 8 * s.pi**2 * (pp - ap + pm - am) / V) == 0

    A = s.symbols("A", positive=True)
    product_deficit = deficit.subs({S: 16 * 2 * s.pi**2 * A, P: 0, T: A, p: A})
    assert s.simplify(product_deficit) == 0
    assert s.simplify(e.subs({S: 16 * 2 * s.pi**2 * A, P: 0, V: 2 * s.pi**2 * A,
                            ap: A, am: A, chi: A / 2})) == 0
    delta = s.symbols("delta", nonnegative=True)
    shear_bound = s.Rational(9, 2) * (4 * (1 + delta)**2 - 8 * s.pi**2 * A / (2 * s.pi**2 * A))
    assert s.expand(shear_bound) == 36 * delta + 18 * delta**2

    J = s.Matrix([[0, -1], [1, 0]])
    jp = s.diag(J, J)
    jm = s.diag(J, -J)
    identity = s.eye(4)
    zero = s.zeros(4)
    assert jp**2 == jm**2 == -identity
    assert jp * jm - jm * jp == zero
    k = -jp * jm
    assert k.T == k and k**2 == identity and s.trace(k) == 0
    assert (k - identity).rank() == (k + identity).rank() == 2

    # Rotating either chirality preserves commutation; sample full bases of so(4).
    def skew(entries):
        result = s.zeros(4)
        for i, j, value in entries:
            result[i, j], result[j, i] = value, -value
        return result

    plus = [skew([(0, 1, 1), (2, 3, 1)]),
            skew([(0, 2, 1), (1, 3, -1)]),
            skew([(0, 3, 1), (1, 2, 1)])]
    minus = [skew([(0, 1, 1), (2, 3, -1)]),
             skew([(0, 2, 1), (1, 3, 1)]),
             skew([(0, 3, 1), (1, 2, -1)])]
    for left in plus:
        for right in minus:
            assert left * right == right * left
            assert s.trace(left * right) == 0

    print("PASS: Chern-Weil deficit identity, bilateral excess decomposition,")
    print("      product normalization, bilateral shear saturation,")
    print("      opposite-chirality commutation,")
    print("      symmetric trace-zero involution and rank-two splitting.")
    print("Scope: finite exact algebra only; no PDE/topology certification.")


if __name__ == "__main__":
    main()
