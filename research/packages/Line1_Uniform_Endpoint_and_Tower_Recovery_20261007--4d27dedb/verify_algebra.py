"""Finite algebra checks only; does not certify inherited PDE or interval analysis."""
from fractions import Fraction
from decimal import Decimal, localcontext
from pathlib import Path
import json
import sympy as sp

A, chi0, k, ell, r, C = sp.symbols('A chi0 k ell r C', real=True)
Q = k + 4*ell + 4*(r-1)
chi = chi0 + k - 2*ell - 2*(r-1)
T = A - Q
assert sp.simplify((A-k)-T - 4*(ell+r-1)) == 0
assert sp.simplify(C*A + Q - chi - (C*A-chi0+6*ell+6*(r-1))) == 0

V,D,t = sp.symbols('V D t', positive=True)
R = 4*V + D - 2*t
Stot = t - 4*V
assert sp.simplify(4 - Stot**2/(R*V) - (4*D-t**2/V)/R) == 0

# Positive integer canonical square: classical Noether upper bound on p_g.
for ai in range(1, 1001):
    pg_max = (ai + 4)//2
    chi_max = 12*(1+pg_max)-ai
    assert chi_max <= 35*ai

root=Path('/mnt/data/research_oct7_inputs/20261007_Einstein_Gaps_Two_Sessions')
src=root/'sources/Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json'
cert=json.loads(src.read_text())
num,den=map(int, cert['P']['upper_dyadic'])
p=Fraction(num,den)
assert p < 1
bound=Fraction(28,9)+Fraction(8,9)*p
assert bound < Fraction(3996144652,10**9)
with localcontext() as ctx:
    ctx.prec=65
    p_dec=str(Decimal(p.numerator)/Decimal(p.denominator))
    bound_dec=str(Decimal(bound.numerator)/Decimal(bound.denominator))
report={
  'status':'finite algebra checks passed; inherited geometric/PDE premises not re-certified',
  'geography_threshold':str(Fraction(35)+Fraction(1,3)),
  'P_certificate_upper_exact':[str(p.numerator),str(p.denominator)],
  'P_certificate_upper_decimal':p_dec,
  'balanced_upper_exact':[str(bound.numerator),str(bound.denominator)],
  'balanced_upper_decimal':bound_dec,
  'outward_decimal_upper':'3.996144652',
  'interval_certificate_recomputed':False,
  'assertions':[
    'connected-sum characteristic identities',
    'geography splitting residual',
    'Einstein residual quotient identity',
    'Noether integer bound checked for A=1,...,1000; general proof in note',
    'exact rational transfer of supplied P certificate'
  ]
}
Path(__file__).with_name('algebra_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
