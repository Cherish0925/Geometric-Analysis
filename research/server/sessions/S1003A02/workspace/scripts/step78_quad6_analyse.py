#!/usr/bin/env python3
"""Step 78: analyse an extracted order-6 quadratic system (npz from step78_quad6.py).
At LM local minima y*: stationarity, Jacobian rank drop, candidate multiplier l = Psi/|Psi|,
inertia of l.H, and the value inf_y l.Psi(y) (computed exactly for a quadratic form).
Usage: python step78_quad6_analyse.py <npz> [nstarts]
"""
import sys, json
import numpy as np
from step78_quad6 import model, lm

f = sys.argv[1]; ns = int(sys.argv[2]) if len(sys.argv) > 2 else 40
d = np.load(f); c, J, H = d['c'], d['J'], d['H']
rng = np.random.default_rng(1)
m, n = J.shape
res = []
for s in range(ns):
    y, nf, it = lm(c, J, H, 10 ** rng.uniform(-1, 1) * rng.standard_normal(n), iters=2000)
    r = model(c, J, H, y); Jy = J + np.einsum('iab,b->ia', H, y)
    U, sv, Vh = np.linalg.svd(Jy)
    l = r / np.linalg.norm(r)
    Ql = np.tensordot(l, H, 1) / 2
    ev = np.linalg.eigvalsh(Ql)
    # inf of f_l(y) = l.c + (l.J) y + y^T Ql y
    g = J.T @ l
    if ev[0] > -1e-10 * abs(ev[-1]):
        # PSD: min = l.c - g^T Ql^+ g /4 if g in range
        Qp = np.linalg.pinv(Ql, rcond=1e-10)
        ystar = -Qp @ g / 2
        inrange = np.linalg.norm(Ql @ ystar * 2 + g) / max(np.linalg.norm(g), 1e-30)
        fmin = l @ c + g @ ystar + ystar @ Ql @ ystar
    else:
        inrange, fmin = None, -np.inf
    res.append({'final': float(nf), 'y_norm': float(np.linalg.norm(y)), 'stationarity': float(np.linalg.norm(Jy.T @ r) / max(nf, 1e-30)),
                'sv_min': float(sv[-1]), 'sv_2ndmin': float(sv[-2]), 'align_l_leftsv': float(abs(U[:, -1] @ l)),
                'lQ_eig_min': float(ev[0]), 'lQ_eig_max': float(ev[-1]), 'lQ_n_neg': int((ev < -1e-9 * abs(ev).max()).sum()),
                'lQ_n_zero': int((abs(ev) <= 1e-9 * abs(ev).max()).sum()), 'f_l_min': float(fmin), 'range_err': inrange})
    print(json.dumps(res[-1]), flush=True)
json.dump(res, open(f.replace('.npz', '_analysis.json'), 'w'), indent=1)
