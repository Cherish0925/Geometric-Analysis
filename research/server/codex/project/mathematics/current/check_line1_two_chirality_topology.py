#!/usr/bin/env python3
"""Exact algebra for the two-chirality application; not a PDE proof checker."""

import json
import sympy as s


checks = []


def equal(name, left, right=0):
    assert s.simplify(left - right) == 0, name
    checks.append(name)


def positive(name, expr):
    assert s.simplify(expr).is_positive is True, (name, expr)
    checks.append(name)


R, P, T, V, I, lam, A = s.symbols("R P T V I lam A", positive=True)
S2 = 4 * (R - P)
W = 2 * s.pi**2 * T - R / 12 + P / 3
equal("Chern-Weil identity in either chirality", S2 / 24 + 2 * W - P / 2, 4 * s.pi**2 * T)
quotient = R / (lam**2 * V) - 2 * I / (lam * V) + 4
equal("Einstein-defect optimization", quotient.subs(lam, R / I), 4 - I**2 / (R * V))
equal("nonnegative scalar-variance remainder", 4 - I**2 / (R * V) - 4 * P / R, (S2 - I**2 / V) / R)
equal("opposite-Weyl energy upper bound", R - 24 * s.pi**2 * T - 4 * P, -12 * W)

chi, tau, k, m = s.symbols("chi tau k m", real=True)
chiM = chi + k - 2 * m
tauM = tau - k
equal("T-plus surgery cost", 2 * chiM + 3 * tauM, 2 * chi + 3 * tau - k - 4 * m)
equal("T-minus surgery cost", 2 * chiM - 3 * tauM, 2 * chi - 3 * tau + 5 * k - 4 * m)
equal("ball-quotient U", (3 * (2 * chiM - 3 * tauM) / A).subs({chi: A / 3, tau: A / 9}), 1 + (15 * k - 12 * m) / A)

h = s.symbols("h", real=True)
F = (4 - s.sqrt(1 - 3 * h))**2 / 9
equal("envelope derivative", s.diff(F, h), (4 - s.sqrt(1 - 3 * h)) / (3 * s.sqrt(1 - 3 * h)))
h0 = s.Rational(19, 300)
x0 = s.Rational(29, 2025)
z0 = s.Rational(397, 32400)
F0 = s.Rational(961, 900)
equal("target h", x0 + 4 * z0, h0)
equal("target F", F.subs(h, h0), F0)
equal("target U meets classical envelope", 1 + 15 * x0 - 12 * z0, F0)
equal("target derivative", s.diff(F, h).subs(h, h0), s.Rational(31, 27))
positive("envelope derivative bounded by two on target interval", 2 - s.Rational(31, 27))
positive("h0 away from old strip", s.Rational(1, 3) - h0 - s.Rational(1, 4))
positive("positive signature", s.Rational(1, 9) - x0)
equal("T-plus limit", 1 - h0, s.Rational(281, 300))
equal("T-minus limit", F0 / 3, s.Rational(961, 2700))
positive("entropy degree test slack", F0 / 6 - s.Rational(32, 243))
equal("Miyaoka-Yau test slack", 4 * x0 - 2 * z0, s.Rational(59, 1800))
positive("Euler characteristic grows", s.Rational(1, 3) + x0 - 2 * z0)

alpha, beta = s.symbols("alpha beta", real=True)
kj = x0 * A - alpha
mj = z0 * A - beta - 2
hj = (kj + 4 * mj) / A
Uj = 1 + (15 * kj - 12 * mj) / A
equal("exact floor h error", hj, h0 - (alpha + 4 * beta + 8) / A)
equal("exact floor U error", Uj, F0 + (-15 * alpha + 12 * beta + 24) / A)
corner_h = [a + 4 * b + 8 for a in (0, 1) for b in (0, 1)]
corner_U = [-15 * a + 12 * b + 24 for a in (0, 1) for b in (0, 1)]
assert (min(corner_h), max(corner_h)) == (8, 13)
assert (min(corner_U), max(corner_U)) == (9, 36)
checks.append("affine floor-error extrema on closed unit square")
equal("safe total excess coefficient", 36 + 2 * 13, 62)

E, U = s.symbols("E U", real=True)
equal("upper bound excess identity", U / (1 - E) - U, U * E / (1 - E))
positive("large-defect branch constant margin", s.Rational(1, 2) - s.Rational(1, 63))
equal("seven-fold transfer coefficient", 1 + 2 * 3, 7)
equal("cover-uniform integral lower bound", s.Rational(1, 2) * (h0 / 2)**2, h0**2 / 8)
equal("cover-uniform pointwise lower bound squared", (h0**2 / 8) / 4, h0**2 / 32)

# Test concrete *integer arithmetic*, not actual covering degrees or metrics.
for n in (1, 2, 5, 100, 10000):
    aj = 32400 * n
    kk = s.floor(x0 * aj)
    mm = s.floor(z0 * aj) - 2
    hh = s.Rational(kk + 4 * mm, aj)
    uu = 1 + s.Rational(15 * kk - 12 * mm, aj)
    excess = s.simplify(uu - F.subs(h, hh))
    assert 0 < hh < h0
    assert excess.is_positive is True
    assert (s.Rational(62, aj) - excess).is_positive is True
checks.append("five integer realizations obey strict two-sided excess bound")

# Deliberate wrong formulas must fail algebraic identity checks.
wrong_handle = 2 * chi - 3 * tau + 5 * k + 4 * m
assert s.simplify((2 * chiM - 3 * tauM) - wrong_handle) != 0
wrong_tracefree = R - 24 * s.pi**2 * T - 2 * P
assert s.simplify(wrong_tracefree + 12 * W) != 0
wrong_m = z0 * A - beta + 2
wrong_U = 1 + (15 * kj - 12 * wrong_m) / A
assert s.simplify((wrong_U - F0) * A).subs({alpha: 0, beta: 0}) < 0

print(json.dumps({
    "status": "passed",
    "exact_check_groups": len(checks),
    "checks": checks,
    "intentional_errors_rejected": [
        "opposite-orientation handle sign",
        "trace-free Ricci coefficient",
        "floor shift with incorrect sign",
    ],
    "scope": "Exact finite algebra only; analytic, gauge, and covering inputs remain in the proof.",
}, indent=2))
