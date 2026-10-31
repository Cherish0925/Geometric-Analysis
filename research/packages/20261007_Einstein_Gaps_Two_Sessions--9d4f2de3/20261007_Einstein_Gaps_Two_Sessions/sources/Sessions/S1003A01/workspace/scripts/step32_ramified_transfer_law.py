"""Exact algebra and normalization checks for the ramified KE transfer law.

Inputs:
  A = K^2 of the compact negative KE background,
  Delta = 3 chi - A,
  Q = k + 4 l, h=Q/A.
The equal-chirality balance is 16 l - 14 k = 4 Delta.
If Delta/Q -> r in [0,1), then
  k/Q -> 2(1-r)/9, l/Q -> (7+2r)/36,
and a single-blowup cell with J/(8 pi^2)<=1-eta plus separated shrinking
handles gives coefficient <= 4-(8 eta/9)(1-r).

The radius for a cell whose outer coordinate is X, after scaling from
Ric=-6g to Ric=-g, is sqrt(6)*asinh(sqrt(X)).
"""
import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

A, Delta, Q, k, ell, eta, r = sp.symbols(
    "A Delta Q k ell eta r", positive=True, real=True
)
Tplus = A - k - 4 * ell
Tminus = A / 3 + 4 * Delta / 3 + 5 * k - 4 * ell
sol = sp.solve(
    [sp.Eq(k + 4 * ell, Q), sp.Eq(16 * ell - 14 * k, 4 * Delta)],
    [k, ell],
    dict=True,
)[0]
k_sol = sp.factor(sol[k])
ell_sol = sp.factor(sol[ell])
assert sp.simplify(Tplus.subs(sol) - (A - Q)) == 0
assert sp.simplify(Tminus.subs(sol) - (A + Q) / 3) == 0

k_ratio = sp.factor((k_sol / Q).subs(Delta, r * Q))
ell_ratio = sp.factor((ell_sol / Q).subs(Delta, r * Q))
coefficient = sp.factor(4 * (1 - eta) * k_ratio + 16 * ell_ratio)
assert sp.simplify(coefficient - (4 - sp.Rational(8, 9) * eta * (1 - r))) == 0

ap = argparse.ArgumentParser()
ap.add_argument("--X", type=float, default=128.0)
ap.add_argument("--J-upper", type=float, default=0.9956710815089548)
ap.add_argument("--A", type=int, default=10**12)
ap.add_argument("--Q", type=int, default=10**8)
ap.add_argument("--r", type=float, default=0.5)
ap.add_argument("--out")
args = ap.parse_args()

eta_num = 1.0 - args.J_upper
radius = math.sqrt(6.0) * math.asinh(math.sqrt(args.X))
# Rounded integer realization near the balanced real solution.
Delta_num = int(round(args.r * args.Q))
k_star = 2.0 * (args.Q - Delta_num) / 9.0
ell_star = 7.0 * args.Q / 36.0 + Delta_num / 18.0
best = None
for ki in range(max(0, int(round(k_star)) - 12), int(round(k_star)) + 13):
    for li in range(max(0, int(round(ell_star)) - 12), int(round(ell_star)) + 13):
        Qi = ki + 4 * li
        bal = 16 * li - 14 * ki - 4 * Delta_num
        key = (abs(bal), abs(Qi - args.Q))
        if best is None or key < best[0]:
            tp = args.A - Qi
            tm = args.A / 3 + 4 * Delta_num / 3 + 5 * ki - 4 * li
            U = 3 * min(tp, tm) / args.A
            coeff_actual = (
                4 * (1 - eta_num) * ki / Qi + 16 * li / Qi
            )
            best = (
                key,
                {
                    "k": ki,
                    "ell": li,
                    "Q_actual": Qi,
                    "Delta": Delta_num,
                    "Delta_over_Q": Delta_num / Qi,
                    "k_over_Q": ki / Qi,
                    "ell_over_Q": li / Qi,
                    "balance_residual": bal,
                    "U_top": U,
                    "U_minus_1_minus_h": U - 1 - Qi / args.A,
                    "construction_coefficient": coeff_actual,
                },
            )

out = {
    "symbolic": {
        "k": str(k_sol),
        "ell": str(ell_sol),
        "Tplus_balanced": str(sp.factor(Tplus.subs(sol))),
        "Tminus_balanced": str(sp.factor(Tminus.subs(sol))),
        "k_over_Q_limit": str(k_ratio),
        "ell_over_Q_limit": str(ell_ratio),
        "upper_coefficient": str(coefficient),
    },
    "certified_input": {
        "X": args.X,
        "radius_Ric_minus_1": radius,
        "J_over_8pi2_upper": args.J_upper,
        "eta": eta_num,
        "r0_coefficient": 4 - 8 * eta_num / 9,
    },
    "example": best[1],
    "interpretation": (
        "For Delta/Q->r<1, Q->infinity and Q=o(A), rounding contributes O(1/A)=o(h); "
        "the replicated-cell plus separated-handle upper coefficient is "
        "4-(8 eta/9)(1-r)."
    ),
}
text = json.dumps(out, indent=1)
print(text)
if args.out:
    Path(args.out).write_text(text + "\n")
