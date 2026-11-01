#!/usr/bin/env python3
"""Step 48, Lemma P: projected Weyl saving.

Saving density (Theorem W/K, scalar -4, amplitude r in [0,2], unit direction n):
  f(W,r,n) = r^2 M(n,n) - 4|M|^2 + (2-r)(r-1)(3r+2)/3,   M = W - (r^2/4)(I/3 - n n^T).
Claim: there is a finite C2 with, for every traceless symmetric W on Lambda^+,
  sup_{r,n} f(W,r,n) <= 2(2/3 - |W|^2) + C2 dist(W,K)^2,
K = orbit of spectrum (-2/3,1/3,1/3).  Combined with the exact closed identity
  8pi^2 k - P = 4 D_W - 4(V - 2pi^2 A),  D_W = int (2/3 - |W+|^2),
this gives 8pi^2 k - P <= 4(V - 2pi^2 A) + 2 C2 int dist(W+,K)^2.
We compute the ratio R(W) = [sup f - 2(2/3-|W|^2)]/dist^2 over the 2-parameter family of
spectra (by SO(3) invariance W may be taken diagonal) and report its sup, the small-E limit
and the large-E limit.  Output: workspace/data/step48_lemmaP.json
"""
import json, os
import numpy as np
from scipy.optimize import minimize

I3 = np.eye(3)

def f(W, r, n):
    M = W - (r*r/4.0)*(I3/3.0 - np.outer(n, n))
    return r*r*(n @ M @ n) - 4.0*np.sum(M*M) + (2-r)*(r-1)*(3*r+2)/3.0

def supf(W, ngrid=24):
    best = -1e9; arg = None
    for r in np.linspace(0, 2, 41):
        for th in np.linspace(0, np.pi, ngrid):
            for ph in np.linspace(0, np.pi, ngrid):
                n = np.array([np.cos(th), np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph)])
                v = f(W, r, n)
                if v > best:
                    best, arg = v, (r, th, ph)
    def neg(x):
        r = np.clip(x[0], 0, 2)
        n = np.array([np.cos(x[1]), np.sin(x[1])*np.cos(x[2]), np.sin(x[1])*np.sin(x[2])])
        return -f(W, r, n)
    res = minimize(neg, np.array(arg), method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 4000})
    return max(best, -res.fun), res.x

def dist2(mu):
    m = np.sort(mu)
    return (m[0]+2/3)**2 + (m[1]-1/3)**2 + (m[2]-1/3)**2

def ratio(mu):
    W = np.diag(mu)
    s, _ = supf(W)
    d2 = dist2(mu)
    return (s - 2*(2/3 - np.sum(mu**2)))/d2, s, d2

out = {}
# scan spectra mu = (x, y, -x-y) around the orbit point (-2/3,1/3,1/3)
rows = []
best = (-1e9, None)
for rad in [1e-3, 1e-2, 0.03, 0.1, 0.2, 0.4, 0.7, 1.0, 2.0, 5.0]:
    for ang in np.linspace(0, 2*np.pi, 25, endpoint=False):
        e1 = np.array([2, -1, -1])/np.sqrt(6); e2 = np.array([0, 1, -1])/np.sqrt(2)
        mu = np.array([-2/3, 1/3, 1/3]) + rad*(np.cos(ang)*e1 + np.sin(ang)*e2)
        R, s, d2 = ratio(mu)
        rows.append([rad, ang, R, s, d2])
        if R > best[0]:
            best = (R, mu.tolist(), rad, ang)
rows = np.array(rows)
out['sup_ratio_scan'] = best[0]
out['argmax_spectrum'] = best[1]
out['argmax_radius_angle'] = [best[2], best[3]]
out['ratio_by_radius_max'] = {str(rad): float(rows[rows[:, 0] == rad][:, 2].max()) for rad in np.unique(rows[:, 0])}
out['ratio_by_radius_min'] = {str(rad): float(rows[rows[:, 0] == rad][:, 2].min()) for rad in np.unique(rows[:, 0])}
# also: check the first-order identity at canonical state: sup f ~ 4E(w,w) for small E
mu = np.array([-2/3, 1/3, 1/3]) + 1e-3*np.array([2, -1, -1])/np.sqrt(6)
s, x = supf(np.diag(mu))
out['small_magnitude_mode'] = {'supf': s, 'two_deficit': 2*(2/3-np.sum(mu**2)), 'argmax_r_th_ph': x.tolist()}
mu = np.array([-2/3, 1/3, 1/3]) + 1e-3*np.array([0, 1, -1])/np.sqrt(2)
s, x = supf(np.diag(mu))
out['small_split_mode'] = {'supf': s, 'two_deficit': 2*(2/3-np.sum(mu**2)), 'argmax_r_th_ph': x.tolist()}
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step48_lemmaP.json')
with open(p, 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
