"""Step 57h: behaviour at the bolt end and at the conformal infinity end.
Bolt: backward integration in (h,W,x) up to a1 ~ 1e-4; fit
   a1' - 1,  a2 - a3,  a2' (=a2'), X2=1-X1  against a1  (log-log slopes).
Smooth bolt (SL(2,R)/Gamma circle of sigma1-length 2pi) requires
   a1' -> 1 with a1' - 1 = O(a1^2),  a2 - a3 = O(a1^2) even, a2', a3' = O(a1).
Infinity: a_i e^{-t} limits (conformal boundary metric ratios).
"""
import numpy as np, json, os, sys, sympy as sp
from scipy.integrate import solve_ivp
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import step57_classA_metric_only as M
d = json.load(open(os.path.join(here, '../data/step57/verify_p1.json')))
w = np.array(d['start']['W']); hv = np.array(d['start']['h']); lamv = -3.0
Vf = sp.lambdify(list(M.h) + list(M.W), [M.V[v].subs(M.lam, lamv) for v in list(M.h) + list(M.W)])
mu_f = sp.lambdify(list(M.h) + list(M.W), M.mu)
def rhs(t, y):
    m = mu_f(*y[:6]); return list(Vf(*y[:6])) + [m[0]*y[6], m[1]*y[7]]
m0 = mu_f(*hv, *w); X1 = -m0[1]/(m0[0]-m0[1])
y0 = list(hv) + list(w) + [np.sqrt(X1), np.sqrt(1-X1)]
def amin(t, y): return 1/np.sqrt(abs(y[4]*y[5])) - 2e-5
amin.terminal = True
sol = solve_ivp(rhs, [0, -2], y0, method='DOP853', rtol=1e-13, atol=1e-14, events=amin, dense_output=True)
t0 = sol.t[-1]
rows = []
for tt in np.linspace(t0, t0 + 0.3, 3000)[1:]:
    y = sol.sol(tt); hh, ww = y[:3], y[3:6]
    aa = np.array([1/np.sqrt(abs(ww[1]*ww[2])), 1/np.sqrt(abs(ww[0]*ww[2])), 1/np.sqrt(abs(ww[0]*ww[1]))])
    ad = aa*hh
    rows.append([aa[0], ad[0]-1, aa[1]-aa[2], ad[1], ad[2], y[7]**2, aa[1], aa[2]])
R = np.array(rows)
def slope(col, lo=3e-3, hi=3e-2):
    m = (R[:, 0] > lo) & (R[:, 0] < hi)
    x = np.log(R[m, 0]); yv = np.log(np.abs(R[m, col]))
    return np.polyfit(x, yv, 1).tolist()
res = dict(t_bolt_approx=float(t0), a1_min=float(R[0, 0]), a2_at=float(R[0, 6]), a3_at=float(R[0, 7]),
           slope_a1p_minus1=slope(1), slope_a2_minus_a3=slope(2), slope_a2p=slope(3), slope_a3p=slope(4), slope_X2=slope(5))
# coefficients: (a1'-1)/a1^2, (a2-a3)/a1^2, a2'/a1
m = (R[:, 0] > 1e-3) & (R[:, 0] < 1e-2)
res['coef_a1p'] = float(np.median(R[m, 1]/R[m, 0]**2)); res['coef_a2ma3'] = float(np.median(R[m, 2]/R[m, 0]**2))
res['coef_a2p'] = float(np.median(R[m, 3]/R[m, 0])); res['coef_a3p'] = float(np.median(R[m, 4]/R[m, 0]))
res['coef_X2'] = float(np.median(R[m, 5]/R[m, 0]**2))
# infinity
sol2 = solve_ivp(rhs, [0, 30], y0, method='DOP853', rtol=1e-12, atol=1e-13)
y = sol2.y[:, -1]; ww = y[3:6]
aa = np.array([1/np.sqrt(abs(ww[1]*ww[2])), 1/np.sqrt(abs(ww[0]*ww[2])), 1/np.sqrt(abs(ww[0]*ww[1]))])
res['infinity_a_times_e^-t'] = (aa*np.exp(-sol2.t[-1])).tolist()
res['infinity_ratios'] = (aa/aa[0]).tolist()
res['infinity_h'] = y[:3].tolist()
print(json.dumps(res, indent=1))
json.dump(res, open(os.path.join(here, '../data/step57/ends_p1.json'), 'w'), indent=1)
