"""Step 30: exact structure of the AK interface B relative to the chiral charge b_+.

B = b_+ - 3F - 9 Pm^2 - 6 W u u'   (Step 29),  F = 4 Pm cosh q - Pm Pm_TT - Pm_T^2/2,
with hatted arclength dT = u dt, Pm = u^2 a_g a_h (= the canonical moment phi of
omega_f = d(phi sigma_f)), phi' = 2 a_f phi/(a_g a_h), q = log(a_g/a_h), W = a_f a_g a_h.

Claim checked here: B-b_+ = 6*phi*u_f-9*phi^2, where u_f=a_f'-gamma_f.
The moment's multiplicative normalization is fixed at the outer marked collar.  Thus on a
complete marked collapsed trajectory, bounded u_f and collar-normalized phi->0 imply
B-b_+->0; scale-free entry data alone do not determine phi or this limit.
Output: workspace/data/step30/B_minus_bplus.json
"""
import json
from pathlib import Path
import sympy as sp

t = sp.symbols('t')
af, ag, ah = [sp.Function(n)(t) for n in ('a_f', 'a_g', 'a_h')]
phi = sp.Function('phi')(t)
u = sp.sqrt(phi / (ag * ah))
W = af * ag * ah
dphi = 2 * af * phi / (ag * ah)


def D(expr):
    """t-derivative using phi' = 2 a_f phi/(a_g a_h)."""
    return sp.diff(expr, t).subs(sp.Derivative(phi, t), dphi)


Pm = u**2 * ag * ah                       # = phi
up = D(u)
PmT = D(Pm) / u
PmTT = D(PmT) / u
coshq = (ag / ah + ah / ag) / 2
F = 4 * Pm * coshq - Pm * PmTT - PmT**2 / 2
diff = sp.simplify(-3 * F - 9 * Pm**2 - 6 * W * u * up)
p = sp.symbols('p', positive=True)
expr = sp.expand(sp.simplify(diff.subs(phi, p)))
poly = sp.Poly(expr, p)
coeffs = {int(m[0]): sp.simplify(c) for m, c in zip(poly.monoms(), poly.coeffs())}
out = {k: str(v) for k, v in coeffs.items()}
print(json.dumps(out, indent=1))
# CH check: a_f = sinh cosh, a_g = a_h = sinh (Ric=-6 normalization, slot f Hopf) ; phi = sinh^2
r = sp.symbols('r', positive=True)
ch = {af: sp.sinh(r) * sp.cosh(r), ag: sp.sinh(r), ah: sp.sinh(r)}
def on_ch(e):
    e = e.subs({sp.Derivative(af, (t, 2)): sp.diff(ch[af], r, 2), sp.Derivative(ag, (t, 2)): sp.diff(ch[ag], r, 2),
                sp.Derivative(ah, (t, 2)): sp.diff(ch[ah], r, 2)})
    e = e.subs({sp.Derivative(af, t): sp.diff(ch[af], r), sp.Derivative(ag, t): sp.diff(ch[ag], r),
                sp.Derivative(ah, t): sp.diff(ch[ah], r)})
    return sp.simplify(e.subs(ch))
chval = sp.simplify(on_ch(expr.subs(p, sp.sinh(r)**2)))
print('CH value of B-b_+ with phi=sinh^2:', chval)
Path(__file__).resolve().parents[1].joinpath('data/step30').mkdir(parents=True, exist_ok=True)
Path(__file__).resolve().parents[1].joinpath('data/step30/B_minus_bplus.json').write_text(
    json.dumps({'coefficients_in_phi': out, 'CH_value_phi_sinh2': str(chval),
                'note': "B-b_+=6 phi u_f-9 phi^2, u_f=a_f'-gamma_f; phi is normalized from the marked outer collar"}, indent=1) + '\n')
