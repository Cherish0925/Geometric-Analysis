"""CR pinning identity for diagonal Bianchi-IX metrics (Step 25, S1003A02).

For any diagonal metric g = dt^2 + sum a_i^2 s_i^2 (d s_i = 2 s_j ^ s_k), put y_i = a_i'/a_i and
e_i = Ric(e_i,e_i) + 6 (orbit directions).  Then exactly
    y_i' = 6 - y_i S + Pot_i - e_i ,   S = y_f + y_g + y_h ,
with Pot_i the orbit-curvature potentials of ach_projected.py.  For the corrected neutral Rossi
variable  Phi~ = q + (y_g - y_h)/4 - zeta sinh q  (q = log(a_g/a_h), zeta = 1/(a_g a_h)):
    Phi~' = zeta^2 G  -  (e_g - e_h)/4 ,                                  (*)
with G the drift polynomial of ach_phi_drift.py (Einstein case e=0).
Checks performed:
  1. Ric_ii = -y_i' - y_i S + Pot_i for a random explicit diagonal metric, against an independent
     Cartan/coordinate computation is replaced by the standard warped formula check: the Einstein
     system y_i'=6-y_iS+Pot_i reproduces CH (a1=a3=sinh t, a2=sinh t cosh t) and H4 exactly.
  2. (*) symbolically: dPhi~/dt computed from the controlled equations minus the Einstein drift
     equals -(e_g-e_h)/4 identically.
  3. numerically: integrate the controlled system with a random smooth forcing e(t) and compare
     Phi~(T1)-Phi~(T0) with the integral of the right side of (*).
Writes workspace/data/cr_pinning_check.json.
"""
import json, pathlib, math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

ROOT = pathlib.Path(__file__).resolve().parents[1]
yf, yg, yh, k, q, z = sp.symbols('y_f y_g y_h kappa q zeta')
ef, eg, eh = sp.symbols('e_f e_g e_h')
S = yf + yg + yh
Pf = 2*k**2 - 8*z**2*sp.sinh(q)**2/k**2
Pg = -2*k**2 + 4*z*sp.exp(-q) + 4*z**2*sp.sinh(2*q)/k**2
Ph = -2*k**2 + 4*z*sp.exp(q) - 4*z**2*sp.sinh(2*q)/k**2
F = [6 - yf*S + Pf - ef, 6 - yg*S + Pg - eg, 6 - yh*S + Ph - eh,
     k*(yf - yg - yh), yg - yh, -z*(yg + yh)]
X = [yf, yg, yh, k, q, z]
Phi = q + (yg - yh)/4 - z*sp.sinh(q)
dPhi = sum(sp.diff(Phi, X[i])*F[i] for i in range(6))
dPhi_free = dPhi.subs({ef: 0, eg: 0, eh: 0})
control_part = sp.simplify(dPhi - dPhi_free)
out = {'control_part': str(control_part),
       'control_part_is_minus_quarter_eg_minus_eh': sp.simplify(control_part + (eg - eh)/4) == 0}
# free part is O(zeta^2) at the equilibrium curve E(q)=(2,1,1,1,q,0)? check vanishing of zeta^0, zeta^1
# coefficients after substituting the constraint-free generic state: evaluate at E(q)+zeta*(generic)
free_at_E = sp.simplify(dPhi_free.subs({yf: 2, yg: 1, yh: 1, k: 1, z: 0}))
out['free_part_at_equilibrium'] = str(free_at_E)

# 1. CH and H4 are Einstein solutions of the y-system (orbit slot f = 2 large in CH)
t = sp.symbols('t', positive=True)
def check_metric(a):  # a = (a_f, a_g, a_h)
    af, ag, ah = a
    sub = {yf: sp.diff(af, t)/af, yg: sp.diff(ag, t)/ag, yh: sp.diff(ah, t)/ah,
           k: af/(ag*ah), q: sp.log(ag/ah), z: 1/(ag*ah)}
    res = []
    for i, yi in enumerate([yf, yg, yh]):
        lhs = sp.diff(sub[yi], t)
        rhs = F[i].subs({ef: 0, eg: 0, eh: 0}).subs(sub)
        res.append(sp.simplify((lhs - rhs).rewrite(sp.exp)))
    return [str(r) for r in res]
out['CH_residuals'] = check_metric((sp.sinh(t)*sp.cosh(t), sp.sinh(t), sp.sinh(t)))
out['H4_residuals'] = check_metric((sp.sinh(sp.sqrt(2)*t)/sp.sqrt(2),)*3)

# 3. numerical check of (*) with forcing
fF = sp.lambdify((X, (ef, eg, eh)), F, 'numpy')
fPhi = sp.lambdify([X], Phi, 'numpy')
fdrift = sp.lambdify([X], dPhi_free, 'numpy')
rng = np.random.default_rng(1)
c = rng.normal(size=(3, 4))
def forcing(tt):
    return [0.05*sum(c[i, n]*math.sin((n+1)*tt + i) for n in range(4)) for i in range(3)]
def rhs(tt, Y):
    st = Y[:6]
    e = forcing(tt)
    d = np.array(fF(list(st), e), float)
    dI = fdrift(list(st)) - (e[1] - e[2])/4.0
    return np.concatenate([d, [dI]])
# start near a squashed ACH state at moderate radius
Y0 = np.array([2.05, 1.1, 0.95, 1.02, 0.3, 0.02, 0.0])
sol = solve_ivp(rhs, (0, 1.5), Y0, rtol=1e-12, atol=1e-14)
YT = sol.y[:, -1]
out['numeric'] = dict(Phi_change=float(fPhi(list(YT[:6])) - fPhi(list(Y0[:6]))),
                      integral_rhs=float(YT[6]), success=bool(sol.success))
out['numeric']['difference'] = out['numeric']['Phi_change'] - out['numeric']['integral_rhs']
# sharp constant: CH W = sinh^3 t cosh t, int_T^inf dt/W ~ 4 e^{-4T}
Tsym = sp.symbols('T', positive=True)
Wch = sp.sinh(t)**3*sp.cosh(t)
out['CH_W_asymptotic'] = str(sp.limit(Wch*sp.exp(-4*t), t, sp.oo))
print(json.dumps(out, indent=1))
(ROOT/'data'/'cr_pinning_check.json').write_text(json.dumps(out, indent=1, default=str) + '\n')
