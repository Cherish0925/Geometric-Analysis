"""Exact algebra only. This script does not verify PDE or compactness arguments."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s

rho = s.Rational(4, 3)
m = s.Rational(128, 81)
q = s.Rational(4, 9)
S = m + 2 * rho**2 * q
gamma = s.Rational(27, 32) * rho**3 * m / S
assert S == 2 * m
assert gamma == 1
K_coefficient = -s.Rational(9, 8) * rho**3 / S
assert K_coefficient == -s.Rational(27, 32)
assert s.Rational(3, 2) * K_coefficient * m / 2 == -1

chi, sig, aa = s.symbols('chi sig aa')
Tp, Tm = 2 * chi + 3 * sig, 2 * chi - 3 * sig
c2 = (9 * aa + Tm) / 4
assert s.expand(c2 - (5 * chi + 6 * sig + s.Rational(9, 4) * (aa - Tp))) == 0

Wp, Wm, P, S2 = s.symbols('Wp Wm P S2')
# chi and signature in operator-norm convention; this is polynomial bookkeeping.
pi = s.pi
chi_form = (Wp + Wm + S2 / 24 - P / 2) / (8 * pi**2)
sig_form = (Wp - Wm) / (12 * pi**2)
expr = s.expand(8 * pi**2 * (5 * chi_form + 6 * sig_form))
target = 9 * Wp + Wm + s.Rational(5, 24) * S2 - s.Rational(5, 2) * P
assert s.simplify(expr - target) == 0
assert s.Rational(5, 24) * 16 == s.Rational(10, 3)

eta = s.symbols('epsilon_W', positive=True)
delta = s.Rational(9, 32) * eta
assert s.simplify(s.Rational(16, 9) * (s.Rational(3, 8) + delta) - s.Rational(2, 3) - eta / 2) == 0

result = {
    'rho_star': str(rho), 'm_star': str(m), 'q_star': str(q),
    'S_star': str(S), 'gamma_star': str(gamma),
    'K_endpoint_coefficient': str(K_coefficient),
    'positive_c2_density_lower_bound': '5/(12*pi**2)',
    'threshold_increment': '9*epsilon_W/32',
    'checks_passed': 9,
    'scope': 'Finite exact algebra only; not a verification of the analytic lemmas.'
}
output = Path(__file__).with_name('constant_checks.json')
output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
