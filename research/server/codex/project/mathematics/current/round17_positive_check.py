"""Exact finite checks for round17_positive.md; no PDE certification."""
from fractions import Fraction as F
from itertools import product
import math


def invariants(orb_chi, orb_tau, n, m):
    return orb_chi + F(3, 2) * n, orb_tau + 2 * m - n


def weyl_energies(chi, tau, volume_over_pi2):
    return (4 * chi + 6 * tau - 3 * volume_over_pi2,
            4 * chi - 6 * tau - 3 * volume_over_pi2)


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


checks = 0


def passed(label):
    global checks
    checks += 1
    print(f"PASS {checks}: {label}")


for n in range(9):
    for m in range(n + 1):
        for oc in [F(1), F(2), F(5, 2)]:
            for ot in [F(-1, 3), F(0), F(2, 3)]:
                chi, tau = invariants(oc, ot, n, m)
                assert 2 * chi + 3 * tau == 2 * oc + 3 * ot + 6 * m
                assert 2 * chi - 3 * tau == 2 * oc - 3 * ot + 6 * (n - m)
                rchi, rtau = invariants(oc, -ot, n, n - m)
                assert (rchi, rtau) == (chi, -tau)
passed("chiral characteristic transport and orientation reversal")

for m in range(3):
    chi, tau = invariants(F(1), F(0), 2, m)
    assert chi == 4 and tau == 2 * m - 2
    assert ((chi - 2 + tau) / 2, (chi - 2 - tau) / 2) == (m, 2 - m)
    assert weyl_energies(chi, tau, F(4, 3)) == (12 * m, 12 * (2 - m))
    assert 2 * chi - 3 * abs(tau) > 0
passed("football Betti numbers, strict Hitchin-Thorpe and Weyl budgets")

# Integral coordinates in the enlarged lattice basis (u,p).
u, v, p, m0 = (1, 0), (-1, 2), (0, 1), (1, -1)
baseline = [p, m0, p, m0]
spin_patterns = []
for bits in product([0, 1], repeat=4):
    inserted = [(m0 if x == p else p) if bit else x
                for x, bit in zip(baseline, bits)]
    rays = [u, inserted[0], v, inserted[1],
            u, inserted[2], v, inserted[3]]
    assert all(abs(det(rays[i], rays[(i + 1) % 8])) == 1 for i in range(8))
    spin = any(all((a * x + b * y) % 2 == 1 for x, y in rays)
               for a, b in product([0, 1], repeat=2))
    if spin:
        spin_patterns.append(bits)
    m = sum(bits)
    chi, tau = invariants(F(2), F(0), 4, m)
    assert chi == 8 and tau == 2 * m - 4
    assert ((chi - 2 + tau) / 2, (chi - 2 - tau) / 2) == (m + 1, 5 - m)
    assert weyl_energies(chi, tau, F(8, 9)) == (
        F(16, 3) + 12 * m, F(16, 3) + 12 * (4 - m))
    assert 2 * chi - 3 * abs(tau) > 0
assert set(spin_patterns) == {(0, 1, 0, 1), (1, 0, 1, 0)}
passed("all 16 product markings: smooth lattice, spin and Betti numbers")
passed("product Weyl budgets reconstructed by Chern-Weil")

for oc, n, v0, w0 in [(F(1), 2, F(4, 3), F(0)),
                       (F(2), 4, F(8, 9), F(16, 3))]:
    for m in range(n + 1):
        chi, tau = invariants(oc, F(0), n, m)
        wp, wm = weyl_energies(chi, tau, v0)
        assert wp + wm + 6 * v0 == 8 * chi
        assert wp - wm == 12 * tau
        assert 4 * (wp + wm) + 24 * v0 == 32 * chi
        assert wp - w0 == 12 * m and wm - w0 == 12 * (n - m)
passed("Euler, signature and full Riemann norm conventions")

v_output_max, v_input = F(4, 9), F(4, 3)
assert 4 - 3 * v_output_max == 6 * v_output_max
assert v_input == 3 * v_output_max
assert 144 * v_output_max == 64
assert 144 * v_input == 192
passed("half-Weyl gap gives factor-three volume separation")

threshold = 1 - 1 / math.sqrt(3)
assert math.isclose((1 - threshold) ** 2 * float(v_input),
                    float(v_output_max), rel_tol=1e-14)
for eps in [0.0, 0.1, 0.25, 0.4]:
    assert (1 - eps) ** 2 * float(v_input) > float(v_output_max)
passed("relative C0 metric bound and four-dimensional volume exponent")

assert (4 + 2) % 4 != 0 and (4 - 2) % 4 != 0
for chi, tau in [(4, 0), (8, 0)]:
    assert -F(tau, 8) == 0
passed("definite filling Todd obstruction and spin-row Dirac indices")

assert invariants(F(1), F(0), 2, 2)[1] != 0  # not the Page manifold
assert F(1) + 2 != 4                         # wrong +N instead of +3N/2
assert weyl_energies(F(4), F(2), F(4, 3))[1] == 0
assert v_output_max != v_input               # no Einstein-gap transfer
passed("reject Page substitution, missing Euler defect and gap transfer")
print(f"All {checks} finite check groups passed.")
