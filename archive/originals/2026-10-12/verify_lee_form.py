"""Exact algebra for the Lee form of the supplied transverse Weyl form.
The source Einstein metric and the published geometric theorems are inputs;
this script checks only the displayed rational exterior-calculus identities.
Requires Python 3 and sympy.
"""
from pathlib import Path
import json
import sympy as s

x=s.symbols("x", positive=True)
D=1+3*x**2
a=(x+1)*(3*x-1)
b=(x-1)*(3*x+1)
c=4*x*(x+1)**2*(9*x**2-1)/D
d=-4*x*(x-1)**2*(9*x**2-1)/D
ell=-s.Rational(3,2)/x-6*x/D
u=-3*(x**2-1)/(x*D)
v=12*(x**2-1)/D
residuals={
    "d_eta_dx_sigma23":s.factor(s.diff(c,x)+ell*c+2*a-u*c-v*b),
    "d_eta_dx_sigma31":s.factor(s.diff(d,x)+ell*d-2*b-u*d+v*a),
    "d_theta_radial":s.factor(s.diff(v,x)-96*x/D**2),
    "d_theta_angular":s.factor(2*v-24*(x**2-1)/D),
}
volume_density=64*x*D/(3*(1-x*x)**3)
norm=18*(1-x*x)**3*(9*x*x-1)/D**4
residuals["eta_norm"]=s.factor(
    2*(3/(x**3*D**2))*(a*c+b*d)/volume_density-norm)
X1=(1-x)**3*(3*x+1)/(16*x**3)
X2=(1+x)**3*(3*x-1)/(16*x**3)
residuals["weyl_norm"]=s.factor(2*(48*x**3/D**2)**2*X1*X2-norm)
r1=-3*(x-1)**2*(21*x**4+18*x**3+12*x*x-2*x-1)/D**3
r2=-3*(x+1)**2*(21*x**4-18*x**3+12*x*x+2*x-1)/D**3
residuals["source_eigenvalue_difference"]=s.factor(r1-r2-48*x**3/D**2)
if any(value!=0 for value in residuals.values()):
    raise AssertionError(residuals)
report={
    "checks":{key:str(value) for key,value in residuals.items()},
    "all_residuals_zero":True,
    "nonclosure":"96*x/(1+3*x**2)**2 > 0 on 1/3 < x < 1",
    "scope":"Exact rational identities only; not a proof of general Q4."
}
Path(__file__).with_name("verification.json").write_text(
    json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps(report,indent=2))
