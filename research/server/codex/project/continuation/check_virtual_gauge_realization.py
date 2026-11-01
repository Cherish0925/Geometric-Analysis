"""Exact finite checks only; not a PDE or compactness certification."""
from fractions import Fraction as F


def run():
    target = [F(-2, 3), F(1, 3), F(1, 3)]
    assert sum(target) == 0
    norm2 = sum(x * x for x in target)
    determinant = target[0] * target[1] * target[2]
    assert norm2 == F(2, 3)
    assert determinant == F(-2, 27)
    assert F(-4, 2) * norm2 - 18 * determinant == 0
    for u in [F(0), F(1, 7), F(2), F(12)]:
        model = [-u / 3, u / 6, u / 6]
        assert sum((x-y)**2 for x, y in zip(model, target)) == (u-2)**2 / 6
    for degree in [2, 4, 18, 1000]:
        volume = F(11, 3)
        lifted_volume = degree * volume
        budget = degree * F(5, 2)
        assert budget / lifted_volume == F(5, 2) / volume
        # A one-chirality invariant upstairs equals d/2 times the
        # unordered two-chirality invariant on a nonorientable base.
        base_error = F(7, 9)
        lifted_error = F(degree, 2) * base_error
        assert 2 * lifted_error / lifted_volume == base_error / volume
    for g in [2, 4, 6]:
        for h in [2, 4, 8]:
            chi_cover = 4 * (g-1) * (h-1)
            chi_base = chi_cover // 2
            p = 2 * chi_cover
            assert chi_base % 4 == 2  # no almost-complex structure
            assert p / 2 == 2 * chi_base
    print("PASS: orbit, Weyl cancellation, cover normalization, quotient parity")


if __name__ == "__main__":
    run()
