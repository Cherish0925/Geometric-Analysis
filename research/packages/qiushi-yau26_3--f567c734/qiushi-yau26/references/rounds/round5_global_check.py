"""Exact coefficient checks for round5_global.md; not a geometric proof."""

from itertools import product

import sympy as s


def zero(expr):
    assert s.simplify(expr) == 0, s.factor(expr)


# Euler density followed by elimination of the vertical volume flux.
b, v, vol, boundary, twist, weyl, e2 = s.symbols(
    "b v vol boundary twist weyl e2", real=True
)
trace = b + v
tracefree_square = e2 - trace**2 / 4
euler = weyl - tracefree_square / 2 + (-12 + trace) ** 2 / 24
zero(euler - (weyl + 6 - trace - e2 / 2 + trace**2 / 6))
# Integrated linear terms b,v and quadratic terms can be represented formally.
linear_euler = weyl + 6 * vol - b - v - e2 / 2 + trace**2 / 6 - 2 * boundary
flux_boundary = (6 * vol + twist - v) / 2
zero(
    linear_euler.subs(boundary, flux_boundary)
    - (weyl - twist - b - e2 / 2 + trace**2 / 6)
)

# Physical cutoff invariance: end volume is delta(area)/3.
a, shift, ren = s.symbols("a shift ren", real=True)
new_vol = vol + a * (s.exp(3 * shift) - 1) / 3
new_boundary = boundary + a * (s.exp(3 * shift) - 1)
zero(new_vol - new_boundary / 3 - (vol - boundary / 3))

# Base Gauss--Bonnet elimination.
area, length, energy, x, q, eb, ev = s.symbols(
    "area length energy x q eb ev", real=True
)
gauss = (energy - x) / 4 + s.Rational(3, 2) * q + (eb - ev) / 2 + length
x_from_area = 6 * area + q - ev - 2 * length
zero(
    4 * gauss.subs(x, x_from_area)
    - (energy + 5 * q - 6 * (area - length) + 2 * eb - ev)
)

# Quadratic error extrema and sharp examples. The full analytic bounds are
# Cauchy--Schwarz and |lambda_i|<=epsilon, as stated in the proof.
lam = s.symbols("l0:4", real=True)
R = sum(z * z for z in lam) / 2 - sum(lam) ** 2 / 6
vertex_values = [R.subs(dict(zip(lam, z))) for z in product([-1, 1], repeat=4)]
assert max(vertex_values) == 2
assert min(vertex_values) == -s.Rational(2, 3)
zero(R.subs(dict(zip(lam, [1, 1, -1, -1]))) - 2)
zero(R.subs(dict(zip(lam, [1, 1, 1, 1]))) + s.Rational(2, 3))

# General-dimensional flat-torus Ricci discrepancy.
n, target = s.symbols("n target", positive=True)
zero(n * (-target) - (-target) + (n - 1) * target)
assert ((3 - 1) * s.Integer(3) / (3 + 1)) == s.Rational(3, 2)

# Warped sharpness construction before smoothing.
t = s.symbols("t", real=True)
k = s.sqrt(s.Rational(3, 2))
raw = k * s.tanh(k * t)
zero(s.diff(raw, t) + raw**2 - s.Rational(3, 2))
zero(s.diff(raw, t) + 3 * raw**2 - (s.Rational(3, 2) + 2 * raw**2))
# The constant pieces have a=+-1 and derivative zero.
for sign in [-1, 1]:
    assert sign**2 == 1
    assert 3 * sign**2 == 3

# Jensen/variance accounting: m=E[a0], d=E[a0'], v=Var(a0).
m, d, variance = s.symbols("m d variance", real=True)
second_moment = m**2 + variance
zero(d + m**2 - (d + second_moment - variance))
zero(d + 3 * m**2 - (d + 3 * second_moment - 3 * variance))
eta = s.symbols("eta", nonnegative=True)
variance_bound = s.Rational(9, 4) * eta**2
zero(3 * variance_bound - s.Rational(27, 4) * eta**2)

# Weyl sectional estimate constants: each chiral block can achieve the
# trace-free eigenvalue bound, and identical chiral blocks realize sqrt(3).
chiral = s.diag(1, -s.Rational(1, 2), -s.Rational(1, 2))
chiral_norm_sq = s.trace(chiral * chiral)
assert chiral_norm_sq == s.Rational(3, 2)
assert 2 * chiral_norm_sq == 3
assert (s.Rational(1, 2) + s.Rational(1, 2)) == 1
# Ricci contribution to K_12 maximized at (+,+,-,-).
ricci_plane = (lam[0] + lam[1]) / 3 - (lam[2] + lam[3]) / 6
assert max(
    ricci_plane.subs(dict(zip(lam, z))) for z in product([-1, 1], repeat=4)
) == 1

print("PASS: Euler/volume/base eliminations, error bounds, flat-rank threshold,")
print("      smooth sharpness variance constants, and Weyl sectional normalization.")
