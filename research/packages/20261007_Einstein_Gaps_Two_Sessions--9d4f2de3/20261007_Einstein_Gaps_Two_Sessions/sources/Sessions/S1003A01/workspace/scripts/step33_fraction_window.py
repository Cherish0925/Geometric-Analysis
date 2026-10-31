"""Step 33: general blow-up-fraction window for ramified Kahler-Einstein surgery families.

M = Xbar # k CP2bar # l (S^1 x S^3), Xbar smooth compact KE (Ric=-g), A=c_1^2(Xbar),
Delta = 3 chi(Xbar) - A >= 0.  Q = k + 4 l, h = Q/A, theta = k/Q, r = Delta/Q.

Inherited inputs (linear_coercivity.tex, eq. lc-all-metric-input and thm:linear-window):
  p >= A, T_+ = A(1-h), a^2 >= T_+, 0<h<=1/3,  L_h = 1+(1+c0)h,
  J >= (L_h - U)_+/(L_h + U/18),  U = 3 min(T_+,T_-)/A,  and E >= J.
Upper construction (Step 31/32): D = k J_1 + 32 pi^2 l + o(Q), V = 2 pi^2 A + O(Q),
  E = (4D - T^2/V)/(4V + D - 2T), T = O(Q)  =>  E = 4h(1 - eta theta) + o(h).

Output: exact symbolic identities and the (r,theta) region, plus the improved
certified eta read from the Step-33 Arb record (outward rounded, exact dyadic).
Usage: python step33_fraction_window.py [--out PATH]
"""
import argparse, json
from fractions import Fraction
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
A, Q, th, r, c0, eta = sp.symbols('A Q theta r c0 eta', positive=True)
k = th*Q; l = (1-th)*Q/4; Dl = r*Q
chi = (A+Dl)/3                      # 3 chi = A + Delta for the background
# background: c1^2 = 2chi+3tau = A  =>  tau = (A - 2chi)/3
tau = (A - 2*chi)/3
chiM = chi + k - 2*l; tauM = tau - k
Tp = sp.simplify(2*chiM + 3*tauM)                       # T_+ = 2chi+3tau of M
Tm = sp.expand(2*chiM - 3*tauM)                         # T_- = 2chi-3tau of M
assert sp.simplify(Tm - (A/3 + 4*Dl/3 + 5*k - 4*l)) == 0  # Step-31 formula
h = Q/A
U_minus = sp.expand(3*Tm/A)
res = {}
res['T_plus'] = str(sp.factor(Tp))
res['T_plus_equals_A(1-h)'] = bool(sp.simplify(Tp - A*(1-h)) == 0)
res['3T_minus_over_A'] = str(sp.collect(sp.expand(U_minus), Q))
res['3T_minus_over_A_is_1+(4r+18theta-3)h'] = bool(sp.simplify(U_minus - (1 + (4*r + 18*th - 3)*h)) == 0)
Lh = 1 + (1 + c0)*h
num = sp.simplify(Lh - U_minus)
res['L_h-U'] = str(sp.factor(num))
# leading coefficient of the J-window lower bound as h->0
hh = sp.symbols('hh', positive=True)
lower = (num/(Lh + U_minus/18)).subs(Q, hh*A)
lead = sp.limit(sp.simplify(lower/hh), hh, 0)
res['liminf_alpha_over_h_lower(if positive)'] = str(sp.factor(lead))
res['upper_coefficient'] = '4*(1-eta*theta)'
res['balanced_theta'] = str(sp.solve(sp.Eq(U_minus, 1 + h), th)[0])
res['lower_at_balanced'] = str(sp.simplify(lead.subs(th, sp.solve(sp.Eq(U_minus, 1 + h), th)[0])))
res['positive_gap_region'] = '4r+18theta < 4+c0  (theta in [0,1]); hence r < 1 + c0/4'
res['consistency_with_pure_handles'] = 'theta=r=0: (18/19)(4+c0) <= 4 forces c0 <= 2/9'

# Delta-corrected scalar-Weyl (handle) identity: with B=int|W^-|^2, S=int s^2,
# W_+ = B + 12 pi^2 tau_M,  P = 4 W_+ + S/12 - 8 pi^2 T_+   (eq. vg-chiral-identities)
B, S = sp.symbols('B S')
pi2 = sp.pi**2
P_expr = 4*(B + 12*pi2*tauM) + S/12 - 8*pi2*Tp
theta0 = (4*l - 5*k)/A
B_Delta = 8*pi2*Dl/3          # = int|W^-|^2 of the KE background (exact)
S0 = 32*pi2*A
res['P_identity_Delta'] = bool(sp.simplify(P_expr - ((S - S0)/12 + 4*(B - B_Delta) + 8*pi2*A*theta0)) == 0)
thD = sp.simplify(theta0 - 4*Dl/(3*A))
res['theta_Delta_over_h'] = str(sp.factor(sp.simplify(thD/h)))
res['handle_identity_lower_coefficient'] = '4*(1-6*theta-4*r/3)_+  (from E>=4 thD/(1+thD), 0<=thD<=1/3)'
# KE background check: B_Delta from signature with |W+|^2 = s^2/24 = 2/3, V = 2 pi^2 A
tau_bg = (A - 2*Dl)/9
res['KE_background_int_Wminus_equals_B_Delta'] = bool(sp.simplify((sp.Rational(2, 3)*2*pi2*A - 12*pi2*tau_bg) - B_Delta) == 0)

# improved certified eta from the Step-33 exact-dyadic Arb record
rec = json.loads((HERE/'../data/step33/rigorous_x00.03_X128_d20_J_exact.json').read_text())
up = Fraction(int(rec['J']['upper_dyadic'][0]), int(rec['J']['upper_dyadic'][1]))
eta_c = 1 - up
res['certified_J_upper_dyadic_float'] = float(up)
res['eta_certified_lower'] = rec['eta_certified_dec_outward_down']
tab = []
for rr in (Fraction(0), Fraction(1, 2), Fraction(1)):
    for tt in (Fraction(0), Fraction(1, 100), Fraction(2, 9)*(1-rr), Fraction(1, 2), Fraction(1)):
        tab.append(dict(r=str(rr), theta=str(tt), upper=float(4*(1-eta_c*tt)),
                        lower_lead_c0_0=float(Fraction(18, 19)*max(Fraction(0), 4-4*rr-18*tt)),
                        lower_positive_iff=f'c0 > {float(4*rr+18*tt-4):.6g}'))
res['table'] = tab
ap = argparse.ArgumentParser(); ap.add_argument('--out')
a = ap.parse_args()
txt = json.dumps(res, indent=1); print(txt)
if a.out:
    Path(a.out).write_text(txt + '\n')
