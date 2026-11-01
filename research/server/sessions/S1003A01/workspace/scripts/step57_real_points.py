"""Step 57e: real points of the invariant component, signs, and direct verification.
W-curve:  F = -(W1+W2)^4 W3^2 + (W1+W2)^3 (W1-W2)^2 W3 + 3 W1 W2 (W1-W2)^4 = 0,
h = h(W) from component_param.json.  For each real point report
type (signs of W), mu1, mu2, X1=-mu2/(mu1-mu2), lam=-Q, q.
Then integrate the full Einstein + closure ODE in (a,b,c,A,B,C,x1,x2) from a point
of Bianchi-IX type (if any) or any type, and check Ric=lam g, |Omega|=1, dOmega=0
directly along the flow, plus that the state stays on V(P).
"""
import sympy as sp, numpy as np, json, os, sys
from scipy.integrate import solve_ivp
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import step57_classA_metric_only as M
h, W = M.h, M.W
par = json.load(open(os.path.join(here, '../data/step57/component_param.json')))
hW = [sp.sympify(par['h_of_W'][str(v)]) for v in h]
sub = dict(zip(h, hW))
muW = [sp.simplify(m.subs(sub)) for m in M.mu]
QW = sp.factor(sp.simplify(M.Q.subs(sub)))
print('mu1(W)=', sp.factor(muW[0])); print('mu2(W)=', sp.factor(muW[1])); print('mu3(W)=', sp.factor(muW[2]))
print('Q(W)=', QW)
f_mu = sp.lambdify(W, muW); f_Q = sp.lambdify(W, QW); f_h = sp.lambdify(W, hW)
rows = []
for th in np.linspace(0.01, 2*np.pi - 0.01, 2000):
    w1, w2 = np.cos(th), np.sin(th)
    s, d = w1 + w2, w1 - w2
    if abs(s) < 1e-6 or abs(d) < 1e-6: continue
    r = w1*w2/s**2
    disc = 1 + 12*r
    if disc < 0: continue
    for sg in (+1, -1):
        z = (1 + sg*np.sqrt(disc))/2
        w3 = z*d**2/s
        m = f_mu(w1, w2, w3); Qv = f_Q(w1, w2, w3)
        rows.append([th, sg, w1, w2, w3, m[0], m[1], m[2], Qv])
rows = np.array(rows)
good = rows[(rows[:, 5]*rows[:, 6] < 0)]
print('real samples', len(rows), ' with mu1 mu2<0:', len(good))
def typ(w):
    return ''.join('+' if x > 1e-9 else ('-' if x < -1e-9 else '0') for x in w)
from collections import Counter
cnt = Counter((typ(g[2:5]), np.sign(-g[8])) for g in good)
print('type, sign(lam) counts among strict points:', cnt)
cntall = Counter((typ(g[2:5]), np.sign(-g[8])) for g in rows)
print('all real points:', cntall)
json.dump({'counts_strict': {f'{k[0]} lam{int(k[1])}': v for k, v in cnt.items()},
           'samples': good[::max(1, len(good)//40)].tolist()},
          open(os.path.join(here, '../data/step57/real_points.json'), 'w'), indent=1)
