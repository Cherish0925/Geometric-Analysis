#!/usr/bin/env python3
"""Step 76: Chern-Weil density of c2(E), E = Lambda^{0,1} (x) Lambda^{0,2},
for the canonical Hermitian connection of an almost-Kaehler Einstein 4-manifold,
evaluated on A01's complete strict Bianchi-VIII AKE pair (Ric=-3g, s=-12, W^-=0).

Derivation (note step76): with p1(L^+) = (1/4pi^2) db^db, p1(L^-) unchanged from
Levi-Civita (the torsion correction of the curvature lies in [m,m] = R Omega),
  c2(E) = (9/4) p1(L^+) - (1/4) p1(L^-),
  db = R(Omega) - a^Ja,  q = |nabla Omega|^2 = 4|a|^2,
so for s=-12:
  4 pi^2 c2(E)_b / vol = 42 - 27 q/8 + 9|eta|^2/4 + |W^-|^2/2.
Consistency check used below: |W^+|^2 = kappa^2/24 + |eta|^2 + |W3|^2 with
kappa = s + 3q/2, and w_Omega = X1 w1 + X2 w2 = kappa/6.
Output: workspace/data/step76_cw_density_on_pair.json
"""
import json
from pathlib import Path
import sympy as s

p = s.symbols('p', positive=True)
w = [-4*(9*p**6-18*p**5-9*p**4-6*p**3+9*p**2-1)/(3*p**2+1)**3,
     -4*(9*p**6+18*p**5-9*p**4+6*p**3+9*p**2-1)/(3*p**2+1)**3,
     8*(9*p**6-9*p**4+9*p**2-1)/(3*p**2+1)**3]
X1 = (1-p)**3*(3*p+1)/(16*p**3)
X2 = (1+p)**3*(3*p-1)/(16*p**3)
q = 36*(1-p**2)**3/(1+3*p**2)**3
eta2 = -18*(p-1)**3*(p+1)**3*(3*p-1)*(3*p+1)/(3*p**2+1)**4
W32 = 81*(p-1)**4*(p+1)**4*(3*p-1)**2*(3*p+1)**2/(2*(3*p**2+1)**6)
kappa = -12 + s.Rational(3, 2)*q
res = {}
res['X1+X2-1'] = str(s.simplify(X1+X2-1))
res['wOmega-kappa/6'] = str(s.simplify(X1*w[0]+X2*w[1]-kappa/6))
res['|W+|^2-(k^2/24+eta2+W32)'] = str(s.simplify(sum(z**2 for z in w)-(kappa**2/24+eta2+W32)))
D = s.factor(s.simplify(42 - s.Rational(27, 8)*q + s.Rational(9, 4)*eta2))
res['density_4pi2_c2E'] = str(D)
LC = s.factor(s.simplify(15 + s.Rational(9, 2)*sum(z**2 for z in w)))
res['LC_density_4pi2_(5chi+6tau)'] = str(LC)
res['difference_LC_minus_b_equals_half_AAD_balance'] = str(s.simplify(
    LC - D - (eta2 + 2*W32 + s.Rational(3, 16)*q**2 - s.Rational(3, 2)*q)*s.Rational(9, 4)))
import numpy as np
ps = np.linspace(1/3, 1, 2001)
f = s.lambdify(p, D, 'numpy')
vals = f(ps)
res['density_min'] = float(vals.min()); res['density_argmin_p'] = float(ps[vals.argmin()])
res['density_at_bolt'] = str(s.nsimplify(D.subs(p, s.Rational(1, 3))))
res['density_at_infinity'] = str(s.limit(D, p, 1))
res['q_at_bolt'] = str(q.subs(p, s.Rational(1, 3)))
out = Path(__file__).resolve().parents[1]/'data'/'step76_cw_density_on_pair.json'
out.write_text(json.dumps(res, indent=1)+'\n')
print(json.dumps(res, indent=1))
