"""Step 47: split of the TN-core torsion Hessian by I3-type directions (numerical quadrature).

tau_TN = sqrt(2) rho* a d fbar is the exact cubic torsion of Phi_TN = sqrt(rho*) e1 + a fbar e2
(S^- = Lambda^{0,1}_{I3} on Kaehler TN), so |nabla_Z tau|^2 = (m*/2)|Hess fbar(Z,.)|^2.
Frame: e_xk = V^{-1/2} horizontal lift of d/dx_k, e_4 = V^{1/2} d/dpsi.  We find which of
Z = e_x1 -+ i e_x2, e_x3 -+ i e_4 annihilate Hess fbar (T^{1,0}_{I3}) and integrate the rest over a
core (ell = 1; all integrals scale like ell^2).  Output workspace/data/step47/tn_core_split.json
"""
import json, os
import numpy as np, sympy as sp
from scipy import integrate
r, th, ph, ps, ell = sp.symbols('r theta phi psi ell', positive=True)
X = [r, th, ph, ps]
V = 1 + ell/r
eta = [0, 0, ell*sp.cos(th), 1]
gb = sp.diag(1, r**2, r**2*sp.sin(th)**2, 0)
g = sp.Matrix(4, 4, lambda i, j: V*gb[i, j] + eta[i]*eta[j]/V)
gi = sp.simplify(g.inv())
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(4))/2)
         for c in range(4)] for b in range(4)] for a in range(4)]
x1 = r*sp.sin(th)*sp.cos(ph); x2 = r*sp.sin(th)*sp.sin(ph); x3 = r*sp.cos(th)
fb = x1 - sp.I*x2
df = [sp.diff(fb, x) for x in X]
H = sp.Matrix(4, 4, lambda b, c: sp.diff(df[c], X[b]) - sum(Gam[a][b][c]*df[a] for a in range(4)))
J = sp.Matrix([x1, x2, x3]).jacobian(sp.Matrix([r, th, ph]))
Ji = J.inv()
fH = sp.lambdify((r, th, ph, ell), H, 'numpy')
fgi = sp.lambdify((r, th, ph, ell), gi, 'numpy')
fJi = sp.lambdify((r, th, ph), Ji, 'numpy')
def frame(rv, tv, pv, lv):
    Vv = 1 + lv/rv
    Jn = np.array(fJi(rv, tv, pv), dtype=float)
    es = []
    for k in range(3):
        vec = np.array([Jn[0, k], Jn[1, k], Jn[2, k], 0.0])
        vec[3] = -lv*np.cos(tv)*vec[2]
        es.append(vec/np.sqrt(Vv))
    es.append(np.array([0, 0, 0, np.sqrt(Vv)]))
    return es
labels = ['e1-ie2', 'e1+ie2', 'e3-ie4', 'e3+ie4']
def dens(rv, tv, pv=0.37, lv=1.0):
    Hn = np.array(fH(rv, tv, pv, lv), dtype=complex)
    G = np.array(fgi(rv, tv, pv, lv), dtype=float)
    e = frame(rv, tv, pv, lv)
    Zs = [e[0]-1j*e[1], e[0]+1j*e[1], e[2]-1j*e[3], e[2]+1j*e[3]]
    out = []
    for Z in Zs:
        al = Z @ Hn
        out.append(np.real(al @ G @ np.conj(al)))
    tot = np.real(np.einsum('ab,cd,ac,bd->', G, G, Hn, np.conj(Hn)))
    return np.array(out), tot
# pointwise checks against |Hess fbar|^2 = 2/(1+r)^4 (ell=1) and phi-independence
chk = []
for (rv, tv) in [(0.3, 0.7), (2.0, 1.3), (7.0, 2.5)]:
    d1, t1 = dens(rv, tv, 0.37); d2, _ = dens(rv, tv, 1.9)
    chk.append(dict(r=rv, th=tv, split=d1.tolist(), split_other_phi=d2.tolist(), total=t1, exact_total=2/(1+rv)**4,
                    frame_sum_over_2=float(d1.sum()/2)))
mstar = 128/81
def radial(k):
    f = lambda tv, rv: dens(rv, tv)[0][k]*(1+1/rv)*rv**2*np.sin(tv)
    val, err = integrate.dblquad(f, 0, np.inf, 0, np.pi, epsabs=1e-11, epsrel=1e-9)
    return val*2*np.pi*4*np.pi*(mstar/2), err
res = dict(pointwise_checks=chk)
E = 8*np.pi**2*mstar
for k, lab in enumerate(labels):
    val, err = radial(k)
    res[lab] = dict(core_integral=val, over_core_energy=val/E, quad_err=err)
    print(lab, val, val/E)
res['core_energy_8pi2mstar'] = E
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step47'); os.makedirs(od, exist_ok=True)
with open(os.path.join(od, 'tn_core_split.json'), 'w') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(chk, indent=1))
