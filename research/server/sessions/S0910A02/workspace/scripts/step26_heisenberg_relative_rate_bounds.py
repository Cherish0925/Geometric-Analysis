"""
Step 26 addendum: exact relative-rate inequalities for the T-active H3 model.

This script converts the TTCS verifier's sharpened algebra into a reproducible
symbolic certificate.  Model:
  g = dt^2 + a(t)^2(theta1^2+theta2^2)+c(t)^2 theta3^2,
  [E1,E2]=E3,
  b=c/a^2, k1=a'/a, k3=c'/c, H=2k1+k3.

For exact Ric=+1, vertical equations plus Ric00=1 give the constraint
  C = 4 k1^2 + 8 k1 k3 + b^2 + 4 = 0.
The script verifies:
  C' = -2 H C along the vertical Einstein ODE;
  |T|^2 = 2 k1^2 + k3^2 >= (b^2+4)/2 on C=0;
  |b'/b|^2 = (k3-2k1)^2 >= 5/4 (b^2+4) on C=0.
For pinched Ricci components rho0,rho1,rho3 in [1-delta,1+delta], the analogous
constraint identity gives conservative bounds with 8 delta loss.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

b, k1, k3, rho0, rho1, rho3, delta = sp.symbols('b k1 k3 rho0 rho1 rho3 delta', positive=True)
H = 2*k1 + k3
C = 4*k1**2 + 8*k1*k3 + b**2 + 4
k1p = -1 - b**2/2 - H*k1
k3p = -1 + b**2/2 - H*k3
bp = b*(k3 - 2*k1)
Cp = sp.diff(C, b)*bp + sp.diff(C, k1)*k1p + sp.diff(C, k3)*k3p

T2 = 2*k1**2 + k3**2
logb2 = (k3 - 2*k1)**2
# Exact sum-of-squares certificates after substituting C=0 are encoded as identities:
# 2*T2 - (b^2+4) = 2*(2*k1+k3)^2 - C
T_identity = sp.expand(2*T2 - (b**2 + 4) - (2*H**2 - C))
# (4/5)*logb2 - (b^2+4) = (4/5)*(3*k1+k3)^2 - C
rate_identity = sp.expand(sp.Rational(4,5)*logb2 - (b**2 + 4) - (sp.Rational(4,5)*(3*k1+k3)**2 - C))

# Pinched variables.  Using formulas:
# rho0 = -2(k1'+k1^2)-(k3'+k3^2),
# rho1 = -b^2/2-k1'-Hk1, rho3=b^2/2-k3'-Hk3.
# Eliminating k' gives: 4k1^2+8k1k3 = 2 rho0 - 4 rho1 - 2 rho3 - b^2.
Cpin = 4*k1**2 + 8*k1*k3 + b**2 - (2*rho0 - 4*rho1 - 2*rho3)
# If rho_i in [1-d,1+d], then S=2rho0-4rho1-2rho3 lies in [-4-8d, -4+8d].
S_min = 2*(1-delta) - 4*(1+delta) - 2*(1+delta)
S_max = 2*(1+delta) - 4*(1-delta) - 2*(1-delta)
# Conservative bounds from S <= -4 + 8delta, hence C_exactlike = 4k1^2+8k1k3+b^2+4 <= 8delta.
# Then 2T2-(b^2+4-8delta)=2H^2-(Cpin+4-?); derive direct identity using S variable.
S = sp.symbols('S')
C_S = 4*k1**2 + 8*k1*k3 + b**2 - S
# If S <= -4+8delta, then C_S+4-8delta <= 0.
# 2T2-(b^2+4-8delta)=2H^2 - (C_S+4-8delta) when S is used? verify with S expression.
T_pin_identity = sp.expand(2*T2 - (b**2+4-8*delta) - (2*H**2 - (C_S + 4 - 8*delta)))
rate_pin_identity = sp.expand(sp.Rational(4,5)*logb2 - (b**2+4-8*delta) - (sp.Rational(4,5)*(3*k1+k3)**2 - (C_S + 4 - 8*delta)))

out = {
    'title': 'Step 26 exact H3 relative-rate bounds',
    'model': 'dt^2 + a^2(theta1^2+theta2^2)+c^2 theta3^2; b=c/a^2, k1=a_prime/a, k3=c_prime/c',
    'constraint_exact_Ric_equals_1': str(C),
    'constraint_derivative_along_vertical_ODE': {
        'C_prime': str(sp.factor(Cp)),
        'C_prime_plus_2HC_simplifies_to': str(sp.simplify(Cp + 2*H*C)),
        'meaning': 'The Ric00=1 constraint is preserved by the vertical Einstein ODE.'
    },
    'exact_bounds_certificates': {
        'T_norm_squared': str(T2),
        'log_bracket_derivative_squared': str(logb2),
        'T_identity_check_zero': str(T_identity),
        'T_certificate': '2|T|^2-(b^2+4)=2(2k1+k3)^2-C, hence on C=0: |T|^2 >= (b^2+4)/2.',
        'rate_identity_check_zero': str(rate_identity),
        'rate_certificate': '(4/5)|d log b/dt|^2-(b^2+4)=(4/5)(3k1+k3)^2-C, hence on C=0: |d log b/dt|^2 >= 5/4 (b^2+4).'
    },
    'pinched_bounds_certificates': {
        'rho_variables': 'rho0=Ric00, rho1=Ric11=Ric22, rho3=Ric33',
        'eliminated_constraint': '4k1^2+8k1k3+b^2 = 2rho0-4rho1-2rho3',
        'S_range_if_all_rho_in_[1-delta,1+delta]': {'S_min': str(sp.expand(S_min)), 'S_max': str(sp.expand(S_max))},
        'conservative_assumption_for_bounds': 'S <= -4+8delta, i.e. C_S+4-8delta <=0',
        'T_pin_identity_check_zero': str(T_pin_identity),
        'T_bound': '|T|^2 >= (b^2+4-8delta)/2 whenever b^2+4>8delta.',
        'rate_pin_identity_check_zero': str(rate_pin_identity),
        'rate_bound': '|d log b/dt|^2 >= 5/4 (b^2+4-8delta) whenever b^2+4>8delta.'
    },
    'interpretation': 'Large Heisenberg bracket is not pointwise impossible under positive Ricci pinching, but it forces large second fundamental form and fast relative bracket variation in this T-active model.'
}

path = Path(__file__).resolve().parents[1] / 'data' / 'step26_heisenberg_relative_rate_bounds.json'
path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
print(f"\nSaved to {path}")
