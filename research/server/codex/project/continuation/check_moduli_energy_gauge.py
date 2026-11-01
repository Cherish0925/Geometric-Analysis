"""Exact algebra for the actual-gauge/slow-energy composition, not a PDE proof."""
import json
import sympy as s


def main():
    V, alpha, r, lam, af = s.symbols("V alpha r lam af", positive=True)
    R = V * (4 + 2 * alpha + r)
    scalar_integral = -V * (4 + alpha)
    checks = {
        "relative_defect": s.simplify(
            4 - scalar_integral**2 / (R * V)
            - (4 * r - alpha**2) / (4 + 2 * alpha + r)
        ) == 0,
        "classical_deficit_to_slow_energy": s.simplify(
            s.Rational(9, 2) * (R - 4 * V) / V
            - (9 * alpha + s.Rational(9, 2) * r)
        ) == 0,
        "small_relative_to_functional_constant": s.simplify(
            (s.Rational(9, 2) + 9 / lam) * s.Rational(7, 3)
            - (s.Rational(21, 2) + 21 / lam)
        ) == 0,
        "variance_constant": s.simplify(
            4 * af / lam**2 * s.Rational(7, 3)
            - 28 * af / (3 * lam**2)
        ) == 0,
    }
    x = s.symbols("x", nonnegative=True)
    f = 3 * x**2 / (4 + 2 * x + x**2)
    checks["relative_lower_bound_monotonic"] = s.simplify(
        s.diff(f, x) - 6 * x * (x + 4) / (x**2 + 2*x + 4)**2
    ) == 0
    checks["threshold"] = f.subs(x, 1) == s.Rational(3, 7)
    delta = s.symbols("delta", nonnegative=True)
    checks["variable_base_pointwise_bound"] = s.expand(
        s.Rational(9, 2) * (4*(1+delta)**2 - 2*(1+(1-delta)**2))
        - (54*delta + 9*delta**2)
    ) == 0
    b = s.symbols("b", positive=True)
    p = (b+1)**2*V/(8*s.pi**2)
    T = b*V/(2*s.pi**2)
    checks["variable_base_gauge_bound"] = s.simplify(
        8*s.pi**2*(2*p-T) - 2*(1+b**2)*V
    ) == 0
    checks["negative_projection_kept"] = s.simplify(
        p-T - (b-1)**2*V/(8*s.pi**2)
    ) == 0
    aa, bb, vx, vy = s.symbols("aa bb vx vy", real=True)
    S = s.Matrix([[aa, bb], [bb, -aa]])
    J = s.Matrix([[0, -1], [1, 0]])
    Si = [vx*S, vy*S]
    def norm2(mat):
        return s.trace(mat.T*mat)
    for chirality in (-1, 1):
        mixed = [Si[1] + chirality*Si[0]*J,
                 -Si[0] + chirality*Si[1]*J]
        checks[f"actual_form_derivative_{chirality}"] = s.simplify(
            sum(norm2(t) for t in mixed)
            - 2*sum(norm2(t) for t in Si)
        ) == 0
    # Root-of-unity sums prove the deck identities for every m >= 3.
    # The displayed finite values independently check the implementation.
    for m in (3, 4, 5, 6, 8, 12):
        values = [2 * s.pi * j / m for j in range(m)]
        checks[f"deck_mean_{m}"] = s.simplify(sum(s.cos(t) for t in values)) == 0
        checks[f"deck_variance_{m}"] = s.simplify(
            sum(s.cos(t)**2 for t in values) - s.Rational(m, 2)
        ) == 0
    a, m, V0, I2, I4 = s.symbols("a m V0 I2 I4", positive=True)
    D = 2 * s.pi**2 * a**2 * I2 / m
    checks["cyclic_q_leading_term"] = s.simplify(
        9 * D / (4 * m * V0)
        - 9 * s.pi**2 * a**2 * I2 / (2 * V0 * m**2)
    ) == 0
    lap_energy = 8 * s.pi**4 * a**2 * I4 / m**3
    checks["cyclic_r_lower_term"] = s.simplify(
        lap_energy / (4 * m * V0)
        - 2 * s.pi**4 * a**2 * I4 / (V0 * m**4)
    ) == 0
    assert all(checks.values()), checks
    print(json.dumps({"passed": len(checks), "checks": checks}, indent=2))


if __name__ == "__main__":
    main()
