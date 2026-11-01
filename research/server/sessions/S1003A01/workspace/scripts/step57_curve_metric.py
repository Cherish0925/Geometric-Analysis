"""Step 57i: exact rational-angle parametrization of the invariant curve and
the strict negative AKE metric in closed form (up to the quadrature t(phi)).

Curve (projective, W2=1):  u=W1/W2, v=W3/W2,
   c=cos(phi), s=sin(phi),  z=1/2+c,  r=(c^2-1/4)/3,
   u = [(1-2r) + (2/sqrt3) s]/(2r),   v = z (u-1)^2/(u+1).
Check F(u,1,v)=0 symbolically.  Then, with lam=-3 (scale k: Q(kh,kW)=3),
   W=k(u,1,v), h=k*h(u,1,v),  a1=1/sqrt|W2W3|, a2=1/sqrt|W1W3|, a3=1/sqrt|W1W2|,
   dt/dphi = (du/dphi) / (2u k (h1-h2)/k ...)   [u' = 2u(h1-h2)].
Strict arc: phi in (-2pi/3,-pi/3)  (u<0: Bianchi VIII type n=(-1,1,1)).
Outputs ../data/step57/curve_metric.json and figure ../figures/step57_strict_AKE_profile.png
"""
import sympy as sp, numpy as np, json, os, sys
import mpmath as mp
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import step57_classA_metric_only as M
ph = sp.symbols('phi', real=True)
c, s = sp.cos(ph), sp.sin(ph)
z = sp.Rational(1, 2) + c; r = (c**2 - sp.Rational(1, 4))/3
u = ((1 - 2*r) + 2/sp.sqrt(3)*s)/(2*r); v = z*(u - 1)**2/(u + 1)
W1, W2, W3 = M.W
F = -(W1+W2)**4*W3**2 + (W1+W2)**3*(W1-W2)**2*W3 + 3*W1*W2*(W1-W2)**4
chk = [sp.N(F.subs({W1: u, W2: 1, W3: v}).subs(ph, val), 30) for val in [-1.2, -1.6, -1.9, 0.3, 2.0]]
print('F on parametrization:', chk)
par = json.load(open(os.path.join(here, '../data/step57/component_param.json')))
hW = [sp.sympify(par['h_of_W'][str(x)]) for x in M.h]
hfun = sp.lambdify(M.W, hW, 'mpmath')
Qfun = sp.lambdify(list(M.h) + list(M.W), M.Q, 'mpmath')
mufun = sp.lambdify(list(M.h) + list(M.W), M.mu, 'mpmath')
ufun = sp.lambdify(ph, u, 'mpmath'); vfun = sp.lambdify(ph, v, 'mpmath'); dufun = sp.lambdify(ph, sp.diff(u, ph), 'mpmath')
mp.mp.dps = 40
def state(p):
    p = mp.mpf(p); uu, vv = ufun(p), vfun(p)
    Wv = [uu, mp.mpf(1), vv]; hv = hfun(*Wv)
    Qh = Qfun(*hv, *Wv); k = mp.sqrt(3/Qh)
    W = [k*x for x in Wv]; h = [k*x for x in hv]
    a = [1/mp.sqrt(abs(W[1]*W[2])), 1/mp.sqrt(abs(W[0]*W[2])), 1/mp.sqrt(abs(W[0]*W[1]))]
    mu = mufun(*h, *W)
    dtdphi = dufun(p)/(2*uu*(h[0]-h[1]))
    X1 = -mu[1]/(mu[0]-mu[1])
    return dict(Qh=Qh, W=W, h=h, a=a, mu=mu, dtdphi=dtdphi, X1=X1)
lo, hi = -2*mp.pi/3, -mp.pi/3
grid = [lo + (hi - lo)*mp.mpf(j)/400 for j in range(1, 400)]
rows = []
for p in grid:
    S = state(p)
    rows.append([float(p), float(S['Qh']), *[float(x) for x in S['a']], *[float(x) for x in S['h']],
                 float(S['mu'][0]*S['mu'][1]), float(S['X1']), float(S['dtdphi'])])
R = np.array(rows)
print('Qhat>0 on whole arc:', bool(np.all(R[:, 1] > 0)), ' mu1mu2<0 on whole arc:', bool(np.all(R[:, 8] < 0)))
print('sign dt/dphi:', np.unique(np.sign(R[:, 10])))
# total t-length of arc (quadrature, both ends)
f = lambda p: state(p)['dtdphi']
eps_list = [mp.mpf('1e-3'), mp.mpf('1e-6'), mp.mpf('1e-9')]
for e in eps_list:
    L = mp.quad(f, [lo + e, (lo+hi)/2, hi - e])
    print('arc length in t, cut', e, ':', L)
for e in [mp.mpf('1e-4'), mp.mpf('1e-8'), mp.mpf('1e-12')]:
    Sb = state(hi - e); Sf = state(lo + e)
    print('near bolt end phi=hi-%s: a=' % e, [mp.nstr(x, 12) for x in Sb['a']], ' X1=', mp.nstr(Sb['X1'], 10))
    print('near far end phi=lo+%s: a=' % e, [mp.nstr(x, 12) for x in Sf['a']], ' h=', [mp.nstr(x, 10) for x in Sf['h']], ' X1=', mp.nstr(Sf['X1'], 10))
json.dump(dict(columns=['phi', 'Qhat', 'a1', 'a2', 'a3', 'h1', 'h2', 'h3', 'mu1mu2', 'X1', 'dtdphi'], rows=rows),
          open(os.path.join(here, '../data/step57/curve_metric.json'), 'w'))
