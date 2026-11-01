"""Step 57f: independent verification of a strict negative AKE candidate on the
exact invariant component, using the step56 coordinate Koszul curvature engine.

1. Pick a real point of V(P) with mu1*mu2<0 and Q>0, rescale so lam=-Q=-3.
2. Convert to (a,b,c,A,B,C), structure constants n_i = sign(W_i).
3. Integrate the full Einstein ODE + closure x_i'=mu_i x_i (x3=0) numerically in
   the (h,W,x) variables; independently evaluate along the flow:
     - Ricci from step56_bianchiA_ake (Koszul, NB=n) -> must equal lam*delta,
     - x1^2+x2^2 (must stay 1; nontrivial AK constraint),
     - distance of the state to V(P) (generators evaluated),
     - q=|nabla Omega|^2, curvature operator blocks: W+ spectrum, |W-|^2, eta.
Output ../data/step57/verify_<tag>.json
"""
import sympy as sp, numpy as np, json, os, sys
from scipy.integrate import solve_ivp
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
tag = os.environ.get('TAG', 'p1')
th0 = float(os.environ.get('TH', 'nan'))
import step57_classA_metric_only as M
h, W = M.h, M.W
par = json.load(open(os.path.join(here, '../data/step57/component_param.json')))
hW = [sp.sympify(par['h_of_W'][str(v)]) for v in h]
subs = dict(zip(h, hW))
f_h = sp.lambdify(W, hW); f_mu = sp.lambdify(W, [m.subs(subs) for m in M.mu]); f_Q = sp.lambdify(W, M.Q.subs(subs))
txt = open(os.path.join(here, '../data/step57/two_lift_P1.txt')).read().replace('^', '**')
gens = [sp.sympify(g) for g in txt.replace('\n', '').split(',') if g.strip()]
f_gens = sp.lambdify(list(h) + list(W), gens)
pts = json.load(open(os.path.join(here, '../data/step57/real_points.json')))['samples']
if np.isnan(th0):
    p = [r for r in pts if r[8] > 0][len(pts)//4]
else:
    p = min(pts, key=lambda r: abs(r[0]-th0))
w = np.array(p[2:5]); hv = np.array(f_h(*w)); Qv = f_Q(*w)
k = np.sqrt(3.0/Qv); w = w*k; hv = hv*k
print('start point W=', w, 'h=', hv, 'Q=', f_Q(*w), 'mu=', f_mu(*w))
n = [int(np.sign(x)) for x in w]
lamv = -3.0
# vector field in (h,W)
Vf = sp.lambdify(list(h) + list(W), [M.V[v].subs(M.lam, lamv) for v in list(h) + list(W)])
mu_f = sp.lambdify(list(h) + list(W), M.mu)
def rhs(t, y):
    hw = y[:6]; x = y[6:8]
    m = mu_f(*hw)
    return list(Vf(*hw)) + [m[0]*x[0], m[1]*x[1]]
m0 = f_mu(*w)
X1 = -m0[1]/(m0[0]-m0[1]); X2 = m0[0]/(m0[0]-m0[1])
y0 = list(hv) + list(w) + [np.sqrt(X1), np.sqrt(X2)]
T = float(os.environ.get('T', '0.6'))
sol = solve_ivp(rhs, [0, T], y0, rtol=1e-12, atol=1e-13, dense_output=True)
sol2 = solve_ivp(rhs, [0, -T], y0, method='DOP853', rtol=1e-13, atol=1e-14, dense_output=True)
print('integration', sol.status, sol2.status, sol.t[-1], sol2.t[-1])
# coordinate curvature engine
os.environ['NB'] = ','.join(str(v) for v in n)
import step56_bianchiA_ake as B
t = B.t; a, b, c = B.a, B.b, B.c
sa, sb, sc, sA, sB, sC, sAp, sBp, sCp = sp.symbols('sa sb sc sA sB sC sAp sBp sCp')
def tosym(e):
    e = e.subs({sp.diff(a, t, 2): sAp, sp.diff(b, t, 2): sBp, sp.diff(c, t, 2): sCp})
    e = e.subs({sp.diff(a, t): sA, sp.diff(b, t): sB, sp.diff(c, t): sC})
    return e.subs({a: sa, b: sb, c: sc})
args = [sa, sb, sc, sA, sB, sC, sAp, sBp, sCp]
Ricf = sp.lambdify(args, B.Ric.applyfunc(tosym))
Rmf = {key: sp.lambdify(args, [tosym(x) for x in val]) for key, val in B.Rm.items()}
def state(tt):
    y = sol.sol(tt) if tt >= 0 else sol2.sol(tt)
    hh, ww, x = y[:3], y[3:6], y[6:8]
    # a_i from W: W_j W_k = n_j n_k / a_i^2
    aa = [1/np.sqrt(abs(ww[1]*ww[2])), 1/np.sqrt(abs(ww[0]*ww[2])), 1/np.sqrt(abs(ww[0]*ww[1]))]
    dh = rhs(tt, y)[:3]
    Ad = [aa[i]*hh[i] for i in range(3)]
    Add = [aa[i]*(dh[i] + hh[i]**2) for i in range(3)]
    return y, aa, Ad, Add
SDb = []
for i, (j, kk) in zip([1, 2, 3], [(2, 3), (3, 1), (1, 2)]):
    F = np.zeros((4, 4)); F[0, i] = 1; F[i, 0] = -1; F[j, kk] = 1; F[kk, j] = -1; SDb.append(F/np.sqrt(2))
ASDb = []
for i, (j, kk) in zip([1, 2, 3], [(2, 3), (3, 1), (1, 2)]):
    F = np.zeros((4, 4)); F[0, i] = 1; F[i, 0] = -1; F[j, kk] = -1; F[kk, j] = 1; ASDb.append(F/np.sqrt(2))
rec = []
TL = os.environ.get('TLIST')
for tt in ([float(v) for v in TL.split(',')] if TL else np.linspace(-0.9*T, 0.9*T, 13)):
    y, aa, Ad, Add = state(tt)
    ar = aa + Ad + Add
    Ric = np.array(Ricf(*ar), float)
    R = np.zeros((4, 4, 4, 4))
    for (i, j, kk), v in Rmf.items():
        R[i, j, kk, :] = np.array(v(*ar), float)
    # curvature operator on 2-forms: <Rop(F),G> = -1/2 sum R(e_i,e_j,e_k,e_l) F_ij G_lk  (sign fixed below)
    def Rop(F, G): return 0.25*np.einsum('ijkl,ij,kl->', R, F, G)
    Mpp = np.array([[Rop(F, G) for G in SDb] for F in SDb]); Mmm = np.array([[Rop(F, G) for G in ASDb] for F in ASDb])
    s = np.trace(Ric)
    sgn = s/(2*(np.trace(Mpp)+np.trace(Mmm)))
    Mpp *= sgn; Mmm *= sgn
    Wp = Mpp - s/12*np.eye(3); Wm = Mmm - s/12*np.eye(3)
    x = y[6:8]; Om = np.array([x[0], x[1], 0.0])
    WO = Wp @ Om; etav = WO - (Om @ WO)*Om
    hw = y[:6]; m = mu_f(*hw)
    X = [x[0]**2, x[1]**2, 0]
    b1 = hw[0]+hw[3]-hw[4]-hw[5]; b2 = hw[1]-hw[3]+hw[4]-hw[5]; b3 = hw[2]-hw[3]-hw[4]+hw[5]
    q = 2*(sum(X[i]*m[i]**2 for i in range(3)) + (X[0]+X[1])*b3**2 + (X[0]+X[2])*b2**2 + (X[1]+X[2])*b1**2)
    rec.append(dict(t=float(tt), ric_err=float(np.max(np.abs(Ric - lamv*np.eye(4)))), unit=float(x[0]**2+x[1]**2-1),
                    VP=float(np.max(np.abs(f_gens(*hw)))), q=float(q), s=float(s), Wp_spec=sorted(np.linalg.eigvalsh((Wp+Wp.T)/2).tolist()),
                    Wm_norm2=float(np.sum(Wm**2)), Wp_on_Omega=float(Om @ Wp @ Om), eta=float(np.linalg.norm(etav)),
                    a=[float(v) for v in aa], X1=float(X[0])))
for r in rec: print('t=%.5f ric=%.1e unit=%.1e |W-|^2=%.1e q=%.4g eta=%.4g X1=%.5f a=' % (r['t'], r['ric_err'], r['unit'], r['Wm_norm2'], r['q'], r['eta'], r['X1']), ['%.5g' % v for v in r['a']], 'W+spec', ['%.5g' % v for v in r['Wp_spec']])
json.dump(dict(start=dict(W=w.tolist(), h=hv.tolist(), n=n), records=rec),
          open(os.path.join(here, f'../data/step57/verify_{tag}.json'), 'w'), indent=1)
