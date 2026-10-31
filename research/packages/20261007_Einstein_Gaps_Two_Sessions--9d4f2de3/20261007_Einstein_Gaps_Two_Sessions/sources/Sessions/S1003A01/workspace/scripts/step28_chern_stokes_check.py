"""Step 28d: symbolic check of the diagonal AK Chern identity as an exact Stokes formula.
  shat* w = d/dT [4 Pm cosh q - Pm Pm'' - Pm'^2/2],  shat* = shat + 2 nu^2,  w = A_f A_g A_h,
and pinning  w = d/dT[Pm^2/4]; CH check (Pm = sinh^2 T, q = 0): bracket = -6 sinh^4 T.
"""
import json
from pathlib import Path
import sympy as sp
T = sp.symbols('T', real=True)
Pm = sp.Function('P')(T); q = sp.Function('q')(T)
d = lambda e: sp.diff(e, T)
Ag = sp.sqrt(Pm)*sp.exp(q/2); Ah = sp.sqrt(Pm)*sp.exp(-q/2); Af = d(Pm)/2
A = [Af, Ag, Ah]
y = [d(a)/a for a in A]; S = sum(y); W = A[0]*A[1]*A[2]
def Porb(i):
    j, k = (i+1) % 3, (i+2) % 3
    return 2*(A[i]**4 - (A[j]**2 - A[k]**2)**2)/W**2
R00 = -sum(d(yi) + yi**2 for yi in y)
Rii = [-d(y[i]) - S*y[i] + Porb(i) for i in range(3)]
s = R00 + sum(Rii)
nu = -(d(q) + 4*sp.sinh(q)/Af)/2
bracket = 4*Pm*sp.cosh(q) - Pm*d(d(Pm)) - d(Pm)**2/2
res = sp.simplify(sp.expand((s + 2*nu**2)*W - d(bracket)))
pin = sp.simplify(W - d(Pm**2/4))
ch = sp.simplify(bracket.subs({Pm: sp.sinh(T)**2, q: 0}).doit())
out = dict(chern_stokes_residual=str(res), pinning_residual=str(pin), CH_bracket=str(sp.simplify(ch)))
print(out)
Path(__file__).resolve().parents[1].joinpath('data', 'step28', 'chern_stokes_check.json').write_text(json.dumps(out, indent=1) + '\n')
