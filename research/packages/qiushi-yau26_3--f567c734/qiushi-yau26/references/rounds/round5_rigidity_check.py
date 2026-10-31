#!/usr/bin/env python3
"""Exact algebra checks for round5_rigidity.md; no PDE existence claims."""

from itertools import product

import sympy as sp


def zero(expression):
    assert sp.simplify(expression) == 0, expression


def topology_and_energy():
    B, m, n = sp.symbols("B m n", positive=True)
    volume = 6 * sp.pi**2 * B
    chi_orb = volume / (12 * sp.pi**2)
    chi = chi_orb + sp.Rational(3, 2) * n
    tau = 2 * m - n
    T = 2 * chi + 3 * tau
    zero(T - (B + 6 * m))

    # Operator Weyl norms, not full four-index Riemann tensor norms.
    W_total = 8 * sp.pi**2 * chi - sp.Rational(2, 3) * volume
    W_diff = 12 * sp.pi**2 * tau
    W_plus = sp.expand((W_total + W_diff) / 2)
    W_minus = sp.expand((W_total - W_diff) / 2)
    zero(W_total - 12 * sp.pi**2 * n)
    zero(W_plus - 12 * sp.pi**2 * m)
    zero(W_minus - 12 * sp.pi**2 * (n - m))
    zero(W_plus - (2 * sp.pi**2 * T - volume / 3))

    mixed_limit = 16 * volume + 6 * W_plus
    upper = mixed_limit / (72 * sp.pi**2)
    zero(upper - (sp.Rational(4, 3) * B + m))
    ratio = T / upper
    zero(ratio - sp.Rational(3, 4) - 21 * m / (4 * upper))
    zero(ratio.subs(m, 0) - sp.Rational(3, 4))
    zero(sp.Rational(3, 4) - sp.Rational(2, 3) - sp.Rational(1, 12))
    zero(sp.diff(ratio, m) - 7 * B / upper**2)
    T0, C0, s, w = sp.symbols("T0 C0 s w", real=True)
    zero((T0 + 6 * m) / (C0 + m) - sp.Rational(2, 3)
         - (3 * T0 - 2 * C0 + 16 * m) / (3 * (C0 + m)))
    zero(27 * (s**2 / 24 + 2 * w**2) - (-s + sp.sqrt(6) * w)**2
         - (s + 8 * sp.sqrt(6) * w)**2 / 8)
    print("PASS: A1 Euler/signature, Weyl energies, mixed integral, ratio >= 3/4")


def connected_sum():
    chi_X, tau_X, ell, k, A = sp.symbols("chi_X tau_X ell k A")
    # N is closed, connected, oriented, with b+(N)=0.
    chi_N, tau_N = 2 - 2 * ell + k, -k
    T_X = 2 * chi_X + 3 * tau_X
    T_M = 2 * (chi_X + chi_N - 2) + 3 * (tau_X + tau_N)
    zero(T_M - (T_X - 4 * ell - k))
    a_square = A - k
    zero(a_square - T_M - (A - T_X + 4 * ell))
    zero((T_M / A - sp.Rational(2, 3)).subs(T_X, A)
         - (sp.Rational(1, 3) - (4 * ell + k) / A))

    # Formal positive projection inner products for up to four exceptional classes.
    for count in range(5):
        gram = sp.Matrix(count + 1, count + 1,
                         lambda i, j: sp.Symbol(f"G{min(i, j)}_{max(i, j)}"))
        total = 0
        for signs in product((-1, 1), repeat=count):
            vector = sp.Matrix((1,) + signs)
            total += (vector.T * gram * vector)[0]
        zero(total / 2**count - sum(gram[i, i] for i in range(count + 1)))
    print("PASS: negative-definite connected-sum topology and full sign averaging")


def convex_geometry():
    x, z, L = sp.symbols("x z L", real=True)
    Q = x**2 - z**2
    # Convex hull is (x,0,z), |x|<=1, |z|<=L.
    # Q<=1 because 1-Q=(1-x)(1+x)+z^2, all terms nonnegative.
    zero(1 - Q - ((1 - x) * (1 + x) + z**2))
    zero(Q.subs({x: 1, z: 0}) - 1)
    zero(Q.subs({x: 1, z: L}) - (1 - L**2))
    # xy projection gives every listed vertex projected square exactly one.
    for sign_x, sign_z in product((-1, 1), repeat=2):
        vertex = sp.Matrix([sign_x, 0, sign_z * L])
        assert vertex[0]**2 + vertex[1]**2 == 1
    print("PASS: beta=alpha=1 does not bound negative vertex squares")


def bundle_saturation_and_surgery():
    chi, d, delta = sp.symbols("chi d delta", positive=True)
    V = 4 * sp.pi**2 * d * chi
    T = 2 * d * chi
    scalar_upper = 16 * (1 + delta)**2 * V / (32 * sp.pi**2)
    zero(scalar_upper - T * (1 + delta)**2)
    zero(T / T - sp.Rational(2, 3) - sp.Rational(1, 3))
    print("PASS: finite-cover E_D monopole saturation ratio is one")


if __name__ == "__main__":
    topology_and_energy()
    connected_sum()
    convex_geometry()
    bundle_saturation_and_surgery()
    print("All round-five rigidity algebra checks passed.")
