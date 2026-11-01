#!/usr/bin/env python3
"""Step 102: check the inherited mixed Einstein edge in the Step-93 normalization.

For an Einstein (orbifold or smooth) metric with s<0 on a space with 2chi+3tau = A-k and
transferred LeBrun inputs  int s^2 >= 32 pi^2 A,  int (s - sqrt6 |W+|)^2 >= 72 pi^2 A,
put u = int s^2/(32 pi^2), D = int(s^2/24 - |W+|^2) = 2 pi^2 (u - A + k),
w = int|W+|^2 = 2pi^2(A-k) - (2/3) pi^2 u.  Cauchy-Schwarz on the constant-s Einstein metric gives
   sqrt(8u) + sqrt(3(A-k) - u) >= 3 sqrt(2A).
Claim (A01 / Spirit #113): D_min = 4 pi^2 k + (8 pi^2 A/9)(1 - sqrt(1-3k/A))^2.
"""
import sympy as sp, json, os

A, k, u = sp.symbols('A k u', positive=True)
h = sp.symbols('h', positive=True)  # h = k/A
# substitute u = A*y, k = A*h
y = sp.symbols('y', positive=True)
eq = sp.sqrt(8*y) + sp.sqrt(3*(1-h) - y) - 3*sp.sqrt(2)
rows = []
ok = True
for hv in [sp.Rational(1,100), sp.Rational(1,20), sp.Rational(1,10), sp.Rational(1,5), sp.Rational(3,10), sp.Rational(33,100)]:
    f = eq.subs(h, hv)
    # roots in (0, 3(1-h))
    sols = [s for s in sp.solve(sp.Eq(sp.sqrt(8*y), 3*sp.sqrt(2) - sp.sqrt(3*(1-hv) - y)), y)]
    sols = [sp.nsimplify(s) for s in sols if abs(sp.N(f.subs(y, s))) < 1e-12]
    ymin = min(sols, key=lambda s: sp.N(s))
    yfeas = sp.Max(ymin, 1)  # also need u >= A
    D_over = 2*(sp.N(yfeas) - 1 + hv)          # D/(pi^2 A)
    claim = 4*hv + sp.Rational(8,9)*(1 - sp.sqrt(1-3*hv))**2
    good = abs(sp.N(D_over - claim)) < 1e-12
    ok &= bool(good)
    rows.append({"h": str(hv), "y_min_root": str(sp.N(ymin, 20)), "D_over_pi2A": str(sp.N(D_over, 20)),
                 "claim": str(sp.N(claim, 20)), "match": bool(good)})
    print(hv, sp.N(ymin, 15), sp.N(D_over, 15), sp.N(claim, 15), good)
# closed form of the smaller root: y = (1+... ) check symbolic
ysym = sp.symbols('ys')
cand = 1 + 2*h - sp.Rational(4,9)*(1 - sp.sqrt(1-3*h))**2 * 0  # placeholder not used
os.makedirs('data/step102', exist_ok=True)
json.dump({"rows": rows, "all_ok": bool(ok)}, open('data/step102/mixed_edge_check.json', 'w'), indent=1)
print("all_ok", ok)
assert ok
