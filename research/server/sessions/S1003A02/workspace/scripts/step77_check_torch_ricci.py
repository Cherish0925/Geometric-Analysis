#!/usr/bin/env python3
"""Step 77 check: torch float Ricci (step77_gn_germ) vs exact Fraction Ricci (step76_polyseries)."""
import sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np, torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
import step77_gn_germ as gg
import step76_polyseries as ps

rng = np.random.default_rng(3)
D = 5
R = gg.TRing(D)
Bs = gg.anti_basis()
H = np.zeros((4, 4, R.nm))
for i, m in enumerate(R.mons):
    if sum(m) >= 2:
        c = rng.integers(-3, 4, 6)
        H[:, :, i] = np.einsum('a,aij->ij', c, Bs)
Ht = torch.tensor(H, dtype=gg.dt, device=gg.dev)
E, G = gg.ricci_E(R, Ht, 0.0)
Hf = [[{m: F(int(H[i, j, k])) for k, m in enumerate(R.mons) if H[i, j, k] != 0} for j in range(4)] for i in range(4)]
Rx, g, Gx = ps.ricci_exp(Hf, D)
err = 0; mx = 0
for i in range(4):
    for j in range(4):
        for k, m in enumerate(R.mons):
            if sum(m) <= D - 2:
                v = float(Rx[i][j].get(m, 0)); w = float(E[i, j, k])
                err = max(err, abs(v - w)); mx = max(mx, abs(v))
print('max abs diff', err, 'max |Ric|', mx)
errG = 0
for k in range(4):
    for i in range(4):
        for j in range(4):
            for n, m in enumerate(R.mons):
                if sum(m) <= D - 1:
                    errG = max(errG, abs(float(Gx[k][i][j].get(m, 0)) - float(G[k, i, j, n])))
print('max Gamma diff', errG)
