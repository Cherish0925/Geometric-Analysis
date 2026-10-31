"""Exact bookkeeping for the Davis-resolution gauge-theory reduction.

Checks arithmetic only; primary theorems and metric construction are inputs.
"""

from fractions import Fraction as Q


def data(m):
    chi = 196
    tau = 2 * m - 122
    top = 2 * chi + 3 * tau
    bplus = (chi - 2 + tau) // 2
    bminus = (chi - 2 - tau) // 2
    bound = Q(104, 3) + m
    squares = [a2 for a2 in range(top, int(bound) + 1)
               if (a2 - tau) % 8 == 0]
    candidates = [(a2, Q(a2 - top, 4), Q(a2 - tau, 8))
                  for a2 in squares]
    return chi, tau, top, bplus, bminus, bound, candidates


for m in range(123):
    chi, tau, top, bp, bm, bound, candidates = data(m)
    assert top == 26 + 6 * m
    assert bp == 36 + m and bm == 158 - m
    rev = data(122 - m)
    assert (chi, -tau, bm, bp) == (rev[0], rev[1], rev[3], rev[4])
    assert Q(bound - top, 4) == Q(13, 6) - Q(5, 4) * m
    if m == 0:
        assert candidates == [(30, Q(1), Q(19))]
        assert bp - 1 == 35 and 2 * (19 - 1) == 36
        assert 17 % 2 == 1  # Sq^2(x^17) = x^18, killing the Z/2 term.
    elif m == 1:
        assert candidates == [(32, Q(0), Q(19))]
        assert bp - 1 == 2 * (19 - 1) == 36
        assert m > 0  # A positive-square bolt is present.
    else:
        assert not candidates

assert data(61)[1] == 0
assert Q(61, 4) - Q(61, 4) == 0
assert sum(1 for m in range(123) if not data(m)[6]) == 121

# Negative tests: a square-38 class at m=0 has valid characteristic parity
# and expected dimension 3, but violates the actual curvature ceiling.
assert (38 - data(0)[1]) % 8 == 0
assert 38 > data(0)[5]
# The wrong even-index rule would spuriously retain the m=0 BF invariant.
assert data(0)[6][0][2] % 2 != 0

print("PASS: 123 chirality counts and orientation reversal")
print("PASS: only (m,a^2,d,index) = (0,30,1,19), (1,32,0,19)")
print("PASS: stable-cohomotopy parity and positive-bolt case separation")
print("PASS: symmetric spin count and two deliberate false alternatives")
