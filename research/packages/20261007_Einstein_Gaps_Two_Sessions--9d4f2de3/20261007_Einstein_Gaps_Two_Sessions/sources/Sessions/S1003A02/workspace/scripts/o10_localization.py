"""O10 localization: elementary (Chern-Weil + LeBrun) lower bounds for
kappa_beta = fint|Ric+g|^2 + D_beta/V that need no density hypothesis.

Conventions (Skills/geometric-analysis/references/conventions-and-literature.md):
  S=int s^2, P=int|Ric0|^2, W=int|W+|^2 (operator HS norm),
  4 pi^2 T+ = S/24 + 2W - P/2,   |Ric+g|^2 = |Ric0|^2 + (s+4)^2/4,
  D_beta = (1+1/beta) S + 6(beta+1) W - 72 pi^2 p,
  LeBrun: int (s - sqrt6 |W+|)^2 >= 72 pi^2 p  =>  for every gamma>0
          72 pi^2 p <= (1+1/gamma) S + 6(1+gamma) W.
Hypothesis used: T+ <= theta * p   (e.g. T+ <= theta*A since p >= A).

Output: Sessions/S1003A02/workspace/data/o10_localization.json
"""
import json, os
import sympy as sp

b, th, g = sp.symbols('beta theta gamma', positive=True)
S, W, P, Tp, p, V, s = sp.symbols('S W P T_p p V s', real=True)

# 1. exact rewriting of kappa*V
P_expr = S/12 + 4*W - 8*sp.pi**2*Tp
kV = P_expr + sp.Symbol('Q4') + (1+1/b)*S + 6*(b+1)*W - 72*sp.pi**2*p  # Q4 = int (s+4)^2/4
kV = sp.expand(kV)
coefS = sp.simplify(kV.coeff(S)); coefW = sp.simplify(kV.coeff(W))

# 2. use T+ <= theta p, then LeBrun with gamma, choose gamma so W-coefficient = 0
lam = 1 + th/9                    # (72+8theta)pi^2 p = 72 pi^2 lam p
gmax = sp.simplify(coefW/(6*lam) - 1)
a = sp.simplify(coefS - lam*(1 + 1/gmax))
a_inf = sp.limit(a, b, sp.oo)
# pointwise min of a s^2 + (s+4)^2/4
smin = sp.solve(sp.diff(a*s**2 + (s+4)**2/4, s), s)[0]
cbound = sp.simplify((a*s**2 + (s+4)**2/4).subs(s, smin))

# 3. Kahler-Einstein values (s=-4): |W+|^2=2/3, p=V/(2 pi^2)
kKE = sp.simplify(((1+1/b)*16 + 6*(b+1)*sp.Rational(2, 3) - 72*sp.pi**2/(2*sp.pi**2)))
# 4. beta=infinity critical numerology: P=0, W=0, s=-4, D_inf -> S-72pi^2 p = 0
pV = sp.Rational(16, 72)/sp.pi**2
TV = sp.Rational(4, 3)/(8*sp.pi**2)  # from P/V = 4/3 + 4w - 8pi^2 T/V = 0, w=0
ratio = sp.simplify(TV/pV)
chi_hyp = sp.Rational(2, 3)/(8*sp.pi**2)   # chi/V for W=0 Einstein, s=-4

rows = []
for thv in [-1, 0, sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(7, 10), sp.Rational(74, 100)]:
    av = sp.lambdify(b, a.subs(th, thv))
    # smallest beta>=2 with a>0 (scan)
    beta0 = None
    for k in range(0, 200001):
        bv = 2 + k*0.01
        if bv > 2 and av(bv) > 0 and (gmax.subs(th, thv).subs(b, bv) > 0):
            beta0 = bv; break
    rows.append({'theta': str(thv), 'a_inf': str(sp.nsimplify(a_inf.subs(th, thv))),
                 'beta0_first_positive': beta0,
                 'c_inf': (lambda A: float(16*A/(4*A+1)) if A > 0 else None)(a_inf.subs(th, thv))})

out = {
    'kappaV_coefficients': {'S': str(coefS), 'W': str(coefW), 'Tp': '-8 pi^2', 'p': '-72 pi^2'},
    'gamma_max': str(gmax), 'a(theta,beta)': str(a), 'a_inf(theta)': str(sp.simplify(a_inf)),
    'pointwise_min_bound(a)': str(cbound),
    'a(theta=0,beta)': str(sp.simplify(a.subs(th, 0))),
    'kappa_KE': str(sp.factor(kKE)),
    'beta_infinity_critical': {'p/V': str(pV), 'T+/V': str(TV), 'T+/p': str(ratio),
                               'chi/V for W=0 Einstein bulk (W- term excluded)': str(chi_hyp)},
    'table': rows,
}
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '..', 'data', 'o10_localization.json')
with open(path, 'w') as fh:
    json.dump(out, fh, indent=2)
print(json.dumps(out, indent=2))
