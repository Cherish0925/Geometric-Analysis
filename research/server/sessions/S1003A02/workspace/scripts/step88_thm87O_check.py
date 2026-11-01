"""Step 88: exact arithmetic check of Theorem 87.O (S^4/Z_2 orbifold deficit over ball quotients).

Conventions (package Sec. 22.6): I_pm = int |W^pm|^2_op, d = 8 pi^2 chi - I_+ - I_-,
I_+ - I_- = 12 pi^2 tau (A_1 links: zero eta correction), Gauss-Bonnet on Ricci-flat ALE:
int |W|^2 = 8 pi^2 (chi(N) - 1/|Gamma|).  Einstein: D = 0, L_s = 0 in
D - 1 = [6(W - 8 pi^2 chi) + L_s]/R  =>  R = 6 d.
Output: Sessions/S1003A02/workspace/data/step88/thm87O_check.json
"""
import json, pathlib
import sympy as sp

A, m = sp.symbols('A m', positive=True)
pi2 = sp.pi**2
chiX, tauX = A/3, A/9                      # ball quotient: c1^2 = 3 c2, tau = (c1^2 - 2 c2)/3
chi_O, tau_O = sp.Integer(1), sp.Integer(0)  # S^4/Z_2 (Satake), two A_1 points
chi_V = chiX + m*chi_O - 2*m               # m smooth-point connected sums
tau_V = tauX + m*tau_O
Imin = 12*pi2*tau_V                        # I_+ + I_- >= |I_+ - I_-| = 12 pi^2 tau
d_upper = sp.simplify(8*pi2*chi_V - Imin)
d_claim = 4*pi2*(A/3 - 2*m)
# lower side: CH metric (I_-=0, I_+ = 12 pi^2 tau_X) + conformally flat round summands
d_lower = sp.simplify(8*pi2*chi_V - 12*pi2*tauX)
# EH resolution of all 2m points
chiN, G = 2, 2
dchi = 2*m*(chiN - sp.Rational(1, G))
dW = 2*m*8*pi2*(chiN - sp.Rational(1, G))
res = dict(
    chi_V=str(sp.simplify(chi_V)), tau_V=str(tau_V),
    d_upper_minus_claim=str(sp.simplify(d_upper - d_claim)),
    d_lower_minus_claim=str(sp.simplify(d_lower - d_claim)),
    EH_dchi=str(sp.simplify(dchi)), EH_dW_minus_8pi2dchi=str(sp.simplify(dW - 8*pi2*dchi)),
    resolved_manifold_chi_minus_chi_of_X_sharp_2m_CPbar2=str(sp.simplify(chi_V + dchi - (chiX + 2*m))),
    einstein_requires=str(sp.solve(sp.Gt(6*d_claim, 0), m)),
)
out = pathlib.Path(__file__).resolve().parents[1] / 'data' / 'step88'
out.mkdir(parents=True, exist_ok=True)
(out / 'thm87O_check.json').write_text(json.dumps(res, indent=1))
print(json.dumps(res, indent=1))
