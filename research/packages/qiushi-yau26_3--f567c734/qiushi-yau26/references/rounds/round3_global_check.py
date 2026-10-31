"""Exact symbolic checks for round3_global.md; no geometric existence inference."""

import math
import sympy as sp

t = sp.symbols("t", real=True)
x, y, z = sp.symbols("x y z", real=True)
coords = (t, x, y, z)
F = sp.Function("F")(t)
g = sp.diag(1, F**2, F**2, F**2)
gi = g.inv()
dim = 4
Gamma = [
    [
        [
            sp.simplify(sum(
                gi[a, d] * (sp.diff(g[d, b], coords[c])
                            + sp.diff(g[d, c], coords[b])
                            - sp.diff(g[b, c], coords[d])) / 2
                for d in range(dim)))
            for c in range(dim)
        ]
        for b in range(dim)
    ]
    for a in range(dim)
]
Ric = sp.zeros(dim)
for i in range(dim):
    for j in range(dim):
        Ric[i, j] = sp.simplify(sum(
            sp.diff(Gamma[a][i][j], coords[a])
            - sp.diff(Gamma[a][i][a], coords[j])
            + sum(Gamma[a][a][b] * Gamma[b][i][j]
                  - Gamma[a][j][b] * Gamma[b][i][a]
                  for b in range(dim))
            for a in range(dim)))
expected = sp.diag(
    -3 * sp.diff(F, t, 2) / F,
    -F * sp.diff(F, t, 2) - 2 * sp.diff(F, t)**2,
    -F * sp.diff(F, t, 2) - 2 * sp.diff(F, t)**2,
    -F * sp.diff(F, t, 2) - 2 * sp.diff(F, t)**2,
)
assert all(sp.simplify(v) == 0 for v in Ric - expected)
print("PASS: all 16 four-dimensional coordinate Ricci components")

n, k, L = sp.symbols("n k L", positive=True)
s = sp.symbols("s", real=True)
test = sp.cosh(k * (s - L / 2)) / sp.cosh(k * L / 2)
assert sp.simplify(sp.diff(test, s, 2) - k**2 * test) == 0
flux = (test * sp.diff(test, s)).subs(s, L) - (test * sp.diff(test, s)).subs(s, 0)
assert sp.simplify(flux - 2 * k * sp.tanh(k * L / 2)) == 0
print("PASS: optimized index-form boundary flux")

D = sp.symbols("D", positive=True)
f1 = sp.cosh(s - D / 2)
I1 = sp.integrate(f1**2, (s, 0, D))
assert sp.simplify(I1 - (D + sp.sinh(D)) / 2) == 0
source_rhs = 2 * n * (1 - sp.tanh(D / 2)) * sp.cosh(D / 2)**2
assert sp.simplify(sp.expand(source_rhs.rewrite(sp.exp)) - n * (1 + sp.exp(-D))) == 0
print("PASS: signed cosh-weighted source and explicit epsilon bound")

A, B = sp.symbols("A B", real=True)
fab = A * sp.exp(s) + B * sp.exp(-s)
baseline = n * (
    sp.integrate(sp.diff(fab, s)**2 + fab**2, (s, -L / 2, L / 2))
    - fab.subs(s, -L / 2)**2 - fab.subs(s, L / 2)**2
)
assert sp.simplify(baseline + 2 * n * sp.exp(-L) * (A**2 + B**2) + 4 * n * A * B) == 0
print("PASS: exact two-moment matrix boundary contribution")

eps = sp.symbols("eps", positive=True)
kk = sp.sqrt(1 + eps / n)
threshold = sp.log((kk + 1) / (kk - 1)) / kk
assert sp.simplify(kk * sp.tanh(kk * threshold / 2).rewrite(sp.exp)) == 1
assert sp.limit(threshold - sp.log(4 * n / eps), eps, 0, dir="+") == 0
print("PASS: sharp inversion and log(4n/epsilon) asymptotic")

aa = k * sp.tanh(k * t)
assert sp.simplify(sp.diff(aa, t) + aa**2 - k**2) == 0
assert sp.simplify(3 - k**2 - (2 - eps / 3)).subs(k**2, 1 + eps / 3) == 0
print("PASS: unsmoothed Riccati equality and central full-defect lower bound")

for error in (0.1, 0.01, 0.001, 1e-6):
    kval = math.sqrt(1 + error / 3)
    width = math.log((kval + 1) / (kval - 1)) / kval
    print(f"n=3 epsilon={error:g}: L_min={width:.12f}")
print("All symbolic checks passed.")
