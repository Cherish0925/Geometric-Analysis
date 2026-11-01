"""Step 57g: global behaviour of the strict negative AKE trajectory (lam=-3).
Integrates the (h,W,x) system forward/backward until blow-up or a_i -> 0 and
records a_i, a_i', X1, q, mu along the way.  Output ../data/step57/global_<tag>.json
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
def big(t, y): return 1e6 - np.max(np.abs(y[:6]))
big.terminal = True
out = {}
for sgn in (+1, -1):
    sol = solve_ivp(rhs, [0, sgn*40], y0, rtol=1e-11, atol=1e-12, events=big, dense_output=True)
    ts = np.linspace(0, sol.t[-1], 400)
    rec = []
    for tt in ts:
        y = sol.sol(tt); hh, ww = y[:3], y[3:6]
        aa = [1/np.sqrt(abs(ww[1]*ww[2])), 1/np.sqrt(abs(ww[0]*ww[2])), 1/np.sqrt(abs(ww[0]*ww[1]))]
        m = mu_f(*y[:6])
        rec.append([float(tt)] + aa + [aa[i]*hh[i] for i in range(3)] + [float(y[6]**2), *map(float, m)])
    out['fwd' if sgn > 0 else 'bwd'] = dict(t_end=float(sol.t[-1]), status=int(sol.status), rec=rec)
    print('dir', sgn, 'end t', sol.t[-1], 'status', sol.status)
    for r in rec[::40] + [rec[-1]]:
        print(' t=%.4f a=(%.4g %.4g %.4g) a\'=(%.4g %.4g %.4g) X1=%.4g mu=(%.3g %.3g %.3g)' % tuple(r))
json.dump(out, open(os.path.join(here, '../data/step57/global_p1.json'), 'w'))
