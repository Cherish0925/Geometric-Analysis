"""Dynamics of the conformal-infinity face zeta=0 of the compact ACH system (Step 25).

On zeta=0 the compact system reduces to
    y_f' = 6 - y_f S + 2k^2,  y_g' = 6 - y_g S - 2k^2,  y_h' = 6 - y_h S - 2k^2,
    k' = k (y_f - y_g - y_h),  q' = y_g - y_h,
with constraint C0 = y_f y_g + y_g y_h + y_h y_f - 6 + k^2 = 0 (from C with Pot at zeta=0:
-(1/2) sum Pot = -(1/2)(2k^2-2k^2-2k^2) = k^2).  Equilibria: the ACH curve E(q) (k=1, y=(2,1,1)),
and the AH point k=0, y_i = sqrt2.  We integrate both branches of the unstable manifold of E(q)
(eigenvalue 2, eigenvector restricted to the face) and record their fates.  This decides whether a
large-orbit-volume excursion off the ACH curve can return to the standard point E(0).
Writes workspace/data/face_unstable_fates.json.
"""
import json, pathlib, math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

ROOT = pathlib.Path(__file__).resolve().parents[1]
yf, yg, yh, k, q = sp.symbols('y_f y_g y_h k q')
S = yf + yg + yh
F = sp.Matrix([6 - yf*S + 2*k**2, 6 - yg*S - 2*k**2, 6 - yh*S - 2*k**2, k*(yf - yg - yh), yg - yh])
X = sp.Matrix([yf, yg, yh, k, q])
J = F.jacobian(X).subs({yf: 2, yg: 1, yh: 1, k: 1})
ev = J.eigenvects()
vu = [v for (lam, m, vs) in ev if lam == 2 for v in vs][0]
vu = np.array([float(c) for c in vu]); vu /= np.abs(vu).max()
f = sp.lambdify([X], F, 'numpy')
C0 = sp.lambdify([X], yf*yg + yg*yh + yh*yf - 6 + k**2, 'numpy')
out = dict(eigen=[(str(l), int(m)) for (l, m, v) in ev], v_unstable=vu.tolist(), runs=[])

def blow(t, Y):
    return 50 - np.abs(Y).max()
blow.terminal = True
for sgn in (+1, -1):
    for eps in (1e-3, 1e-5):
        Y0 = np.array([2, 1, 1, 1, 0.3]) + sgn*eps*vu
        sol = solve_ivp(lambda t, Y: np.array(f(Y), float).ravel(), (0, 40), Y0, rtol=1e-11, atol=1e-13,
                        events=blow)
        Yt = sol.y[:, -1]
        out['runs'].append(dict(sign=sgn, eps=eps, t_end=float(sol.t[-1]), final=Yt.tolist(),
                                blew_up=bool(sol.status == 1), C0_start=float(C0(Y0)),
                                C0_end=float(C0(Yt)), kmin=float(sol.y[3].min()), kmax=float(sol.y[3].max())))
        print(out['runs'][-1])
(ROOT/'data'/'face_unstable_fates.json').write_text(json.dumps(out, indent=1) + '\n')
