#!/usr/bin/env python3
"""Step 48: exact form of the field saving density and Theorem Y constants.

Identity (symbolic): with M = W - (r^2/4)(I/3 - n n^T), W traceless symmetric 3x3, |n|=1,
   r^2 M(n,n) - 4|M|^2 + p(r) = -r^2 W(n,n) - 4|W|^2 + p(r),  p(r)=(2-r)(r-1)(3r+2)/3.
Hence sup_n f = -r^2 mu_min(W) - 4|W|^2 + p(r) and, with x=-mu_min, r in [0,2]:
   phi(x) = sup_r [x r^2 + p(r)] = r*^3/2 - 4/3, r*=(6x+14)/9   (0<=x<=2/3),   = 4x  (x>=2/3).
Psi(W) = 4/3 + 2|W|^2 - phi(-mu_min(W)) >= 0, and c_Psi = inf Psi/dist(W,K)^2.
Output: workspace/data/step48_theoremY.json
"""
import json, os
import numpy as np
import sympy as sp

# 1. symbolic identity
w = sp.symbols('w0:6'); r = sp.symbols('r', positive=True)
th, ph = sp.symbols('theta phi', real=True)
W = sp.Matrix([[w[0], w[1], w[2]], [w[1], w[3], w[4]], [w[2], w[4], -w[0]-w[3]]])
n = sp.Matrix([sp.cos(th), sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph)])
P = sp.eye(3)/3 - n*n.T
M = W - r**2/4*P
nrm = lambda A: sum(A[i, j]**2 for i in range(3) for j in range(3))
p = (2-r)*(r-1)*(3*r+2)/3
lhs = r**2*(n.T*M*n)[0] - 4*nrm(M) + p
rhs = -r**2*(n.T*W*n)[0] - 4*nrm(W) + p
ident = sp.simplify(sp.expand(sp.trigsimp(lhs - rhs)))
x = sp.symbols('x', nonnegative=True)
rs = (6*x+14)/9
phi_low = sp.expand(rs**3/2 - sp.Rational(4, 3))
phi_check = sp.simplify((x*rs**2 + p.subs(r, rs)) - phi_low)
# psi along axial (-x,x/2,x/2): 4/3+3x^2-phi
psi_low = sp.expand(sp.Rational(4, 3) + 3*x**2 - phi_low)
psi_high = sp.factor(sp.Rational(4, 3) + 3*x**2 - 4*x)
psi_low_series = sp.series(psi_low.subs(x, sp.Rational(2, 3) - sp.Symbol('h')), sp.Symbol('h'), 0, 4)

# 2. numeric: inf Psi/dist^2 over spectra
def phi(xv):
    if xv >= 2/3:
        return 4*xv
    rr = (6*xv+14)/9
    return rr**3/2 - 4/3

def Psi(mu):
    mu = np.sort(mu)
    return 4/3 + 2*np.sum(mu**2) - phi(-mu[0])

def dist2(mu):
    m = np.sort(mu)
    return (m[0]+2/3)**2 + (m[1]-1/3)**2 + (m[2]-1/3)**2

# brute-force check of sup f formula on random W
rng = np.random.default_rng(1)
maxerr = 0.0
for _ in range(200):
    A = rng.normal(size=(3, 3)); A = (A+A.T)/2; A -= np.trace(A)/3*np.eye(3)
    best = -1e9
    for rv in np.linspace(0, 2, 201):
        for t in np.linspace(0, np.pi, 61):
            for q in np.linspace(0, 2*np.pi, 61):
                nv = np.array([np.cos(t), np.sin(t)*np.cos(q), np.sin(t)*np.sin(q)])
                Mv = A - rv*rv/4*(np.eye(3)/3 - np.outer(nv, nv))
                val = rv*rv*(nv@Mv@nv) - 4*np.sum(Mv*Mv) + (2-rv)*(rv-1)*(3*rv+2)/3
                best = max(best, val)
    mu = np.linalg.eigvalsh(A)
    exact = phi(-mu[0]) - 4*np.sum(mu**2)
    maxerr = max(maxerr, exact - best)  # grid sup <= exact
    if _ >= 19:
        break
ratios = []
e1 = np.array([2, -1, -1])/np.sqrt(6); e2 = np.array([0, 1, -1])/np.sqrt(2)
for rad in np.concatenate([np.logspace(-5, 1, 61)]):
    for ang in np.linspace(0, 2*np.pi, 721):
        mu = np.array([-2/3, 1/3, 1/3]) + rad*(np.cos(ang)*e1 + np.sin(ang)*e2)
        d2 = dist2(mu)
        if d2 > 0:
            ratios.append((Psi(mu)/d2, rad, ang, Psi(mu)))
ratios.sort()
minPsi = min(t[3] for t in ratios)
out = {'identity_f_simplifies_residual': str(ident),
       'phi_low_formula_check_residual': str(phi_check),
       'phi_low': str(phi_low), 'psi_axial_low': str(psi_low), 'psi_axial_high': str(psi_high),
       'psi_axial_low_series_in_h=2/3-x': str(psi_low_series),
       'grid_vs_exact_supf_max_gap(first 20 random W)': maxerr,
       'inf_Psi_over_dist2_numeric': ratios[0][0], 'argmin_rad_ang': ratios[0][1:3],
       'expected_sharp_c_Psi': 10/9, 'min_Psi_over_scan': minPsi}
pth = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step48_theoremY.json')
with open(pth, 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
