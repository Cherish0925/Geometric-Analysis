"""Exact finite checks for round14_rigidity.md; not a gauge/PDE proof."""

import json
import sympy as s


def main():
    d, volume, numerator, lam = s.symbols("d V N lam", positive=True)
    normalized_cover = d * numerator / (lam**2 * d * volume)
    assert s.simplify(normalized_cover - numerator / (lam**2 * volume)) == 0

    scalar_integral, ricci_energy = s.symbols("S R", real=True, nonzero=True)
    cover_defect = 4 - (d * scalar_integral) ** 2 / (
        d * volume * d * ricci_energy
    )
    base_defect = 4 - scalar_integral**2 / (volume * ricci_energy)
    assert s.simplify(cover_defect - base_defect) == 0

    p, q, k = s.symbols("p q k", integer=True, positive=True)
    D = (p - 1) * (q - 1)
    chi = 2 * D
    b1 = p + q
    b2 = 2 * p * q
    assert s.expand(2 - 2 * b1 + b2 - chi) == 0
    assert s.expand(2 * p * q - b2) == 0
    assert s.simplify(16 * (8 * s.pi**2 * D) / (32 * s.pi**2) - 4 * D) == 0

    # The two involutions have +/- eigenspaces of dimensions p,p and q,q.
    # Neither surface area class survives; ++ and -- tensors do survive.
    for pg in range(2, 6):
        for qg in range(2, 6):
            P = s.diag(*([1] * pg + [-1] * pg))
            Q = s.diag(*([1] * qg + [-1] * qg))
            tensor = s.kronecker_product(P, Q)
            total_h2_action = s.diag(-1, -1, tensor)
            invariants = (total_h2_action.rows + s.trace(total_h2_action)) / 2
            assert invariants == 2 * pg * qg

    A_cover = 8 * D
    T_cover = A_cover - 2 * k
    T_base = 4 * D - k
    assert s.expand(T_cover - 2 * T_base) == 0
    assert s.simplify(
        T_cover / A_cover - s.Rational(2, 3)
        - (s.Rational(1, 3) - k / (4 * D))
    ) == 0

    chi_shear = s.symbols("chi_shear", positive=True)
    budget = 2 * d * chi_shear
    assert s.simplify(budget / d - 2 * chi_shear) == 0
    assert s.simplify((2 * d * chi_shear) / budget - 1) == 0

    A, ell, n, m, genus_sum = s.symbols("A ell n m genus_sum", real=True)
    T_N = 4 - 4 * ell - k
    # n surface-product summands contribute 8n-8sum(r_j), and m circle
    # products contribute zero; there are 1+n+m connected-sum operations.
    T_X = A + T_N + 8 * n - 8 * genus_sum - 4 * (1 + n + m)
    loss = k + 4 * ell + 8 * genus_sum - 4 * n + 4 * m
    assert s.expand(T_X - (A - loss)) == 0
    assert s.expand((A - k) - T_X - (loss - k)) == 0
    assert s.simplify(T_X / A - s.Rational(2, 3)
                      - (s.Rational(1, 3) - loss / A)) == 0
    assert loss.subs({k: 0, ell: 0, n: 1, m: 0, genus_sum: 1}) == 4
    assert T_X.subs({A: 8, k: 0, ell: 0, n: 1, m: 0, genus_sum: 1}) == 4
    j = s.symbols("j", integer=True, positive=True)
    critical_subs = {A: 24*j, k: 0, ell: 0, n: 2*j, m: 0, genus_sum: 2*j}
    assert s.simplify(T_X.subs(critical_subs) / (24*j) - s.Rational(2, 3)) == 0
    assert s.simplify(loss.subs(critical_subs) / (24*j) - s.Rational(1, 3)) == 0
    c2 = s.symbols("c2", positive=True)
    assert s.simplify(2 * c2 / (2 * volume) - c2 / volume) == 0

    psi = s.Matrix(s.symbols("psi1 psi2 psi3", real=True))
    model = (psi.dot(psi) * s.eye(3) / 24 - psi * psi.T / 8)
    flipped = ((-psi).dot(-psi) * s.eye(3) / 24 - (-psi) * (-psi).T / 8)
    assert s.simplify(model - flipped) == s.zeros(3)
    assert s.simplify(s.trace(model)) == 0

    # Detect the two tempting normalization errors explicitly.
    assert s.simplify(numerator / (lam**2 * d * volume)
                      - numerator / (lam**2 * volume)) != 0
    assert s.simplify(s.Rational(1, 3) - k / A_cover
                      - (s.Rational(1, 3) - k / (4 * D))) != 0

    print(json.dumps({
        "cover_energy_normalization": "passed",
        "quotient_euler_and_betti": "passed",
        "quotient_cohomology_characters": "16 exact cases passed",
        "scalar_energy_saturation": "passed",
        "equivariant_blowup_ratio": "passed",
        "shear_cover_budget_ratio": "passed",
        "twisted_cover_factors_and_connected_sum_loss": "passed",
        "smallest_shear_positive_bplus_surgery": "passed",
        "twisted_infinite_critical_family": "passed",
        "sign_twisted_weyl_model_is_untwisted_and_tracefree": "passed",
        "wrong_normalizations_detected": 2,
        "scope": "finite algebra only; geometry and gauge inputs are in the proof"
    }, indent=2))


if __name__ == "__main__":
    main()
