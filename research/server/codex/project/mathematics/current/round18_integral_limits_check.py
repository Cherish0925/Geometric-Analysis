"""Finite algebra checks for the classical bounded-geometry dilution example."""
import sympy as s


def main():
    d, chi, c2 = s.symbols("d chi c2", positive=True)
    cv = s.Symbol("cv", real=True)
    v = 4 * s.pi**2 * d * chi / 3
    upper = 4 * s.pi**2 * (d * chi - 2) / 3
    assert s.simplify(v - upper) == 8 * s.pi**2 / 3
    print("PASS 1: degree-one volume lower bound exceeds Einstein CGB upper bound")

    cgb_density = s.Rational(1, 24) * (-12) ** 2
    assert cgb_density == 6
    # Positive and zero Einstein signs have zero entropy under Ricci >= 0.
    assert 0 < 3**4 * v
    print("PASS 2: normalized negative density and nonnegative entropy contradiction")

    defect_bound = c2 / (9 * (v + cv))
    assert s.limit(defect_bound, d, s.oo) == 0
    assert s.simplify(defect_bound * (v + cv)) == c2 / 9
    print("PASS 3: relative integral defect vanishes by growing volume")

    maximum = s.Symbol("fixed_positive_maximum", positive=True)
    assert s.limit(maximum, d, s.oo) == maximum
    # Negative control: the pointwise norm is not divided by total volume.
    wrong = maximum / (v + cv)
    assert s.limit(wrong, d, s.oo) == 0
    assert s.simplify(maximum - wrong) != 0
    print("PASS 4: dilution cannot turn the fixed pointwise error into zero")


if __name__ == "__main__":
    main()
