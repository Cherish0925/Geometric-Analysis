"""Exact algebra for round19_global_gap.md; no metric existence claims."""

import sympy as sp

d, z, h, k, c = sp.symbols("d z h k c", real=True)
x = sp.symbols("x0:4", real=True)
Q = sp.Rational(3, 2) * (sum(x) ** 2 - 3 * sum(t**2 for t in x))
vertices = []
for m in range(5):
    values = [1 + d] * m + [1 - d] * (4 - m)
    q = sp.expand(Q.subs(dict(zip(x, values))))
    assert sp.expand(q - 6 * (1 + (m - 2) * d + ((m - 2) ** 2 - 3) * d**2)) == 0
    vertices.append(q)
assert all(sp.diff(Q, t, 2) == -6 for t in x)
assert vertices[0] == 6 * d**2 - 12 * d + 6
assert sp.factor(vertices[1] - vertices[0]) == -6 * d * (3 * d - 1)
# Every competing vertex is >= Q_0 on [0,1/3].
assert sp.factor(vertices[2] - vertices[0]) == -12 * d * (2 * d - 1)
assert sp.factor(vertices[3] - vertices[0]) == -18 * d * (d - 1)
assert sp.factor(vertices[4] - vertices[0]) == 24 * d
# Every competing vertex is >= Q_1 on [1/3,1].
assert sp.factor(vertices[2] - vertices[1]) == -6 * d * (d - 1)
assert sp.factor(vertices[3] - vertices[1]) == 12 * d
assert sp.factor(vertices[4] - vertices[1]) == 18 * d * (d + 1)
g_large_z = (1 - sp.sqrt(z)) / (1 + sp.sqrt(z))
g_small_z = (1 - z) / (2 + z)
assert sp.simplify((((1 - d) / (1 + d)) ** 2).subs(d, g_large_z) - z) == 0
assert sp.simplify(((1 - 2 * d) / (1 + d)).subs(d, g_small_z) - z) == 0
assert g_large_z.subs(z, sp.Rational(1, 4)) == sp.Rational(1, 3)
assert g_small_z.subs(z, sp.Rational(1, 4)) == sp.Rational(1, 3)
assert g_small_z.subs(z, 0) == sp.Rational(1, 2)
band_numerator = sp.expand((2 * h - 4 * k) - sp.Rational(17, 24) * (sp.Rational(8, 3) * h + c))
assert band_numerator == h / 9 - 4 * k - sp.Rational(17, 24) * c
assert band_numerator.subs(h, 36 * k + sp.Rational(51, 8) * c) == 0
assert sp.limit((2 * h - 4 * k) / (sp.Rational(8, 3) * h + c), h, sp.oo) == sp.Rational(3, 4)
print("PASS: five Ricci-box vertices and separate concavity")
print("PASS: exact box minimum branches and inverse thresholds")
print("PASS: all-monopole 3/4 limit and explicit 17/24 threshold")
