#!/usr/bin/env python3
"""Step 68f: can the top kernel freedom absorb the order-d scalar compatibility linearly?

At a torsion zero (Darboux gauge, g=exp H, H=H2+H3+...), the kernel part k of H_d in ker L_{d-2} (flat) leaves
E_0..E_{d-1} unchanged and enters E_d only through   D_d(k) = B(H2,k) - lam k   (exact: no other product has
low enough degree).  The coker conditions on E_d (modulo automatic Bianchi rows) are the C(d+1,3) coefficients
of the scalar compatibility P(E_d).  Hence if  M_d = P_d o D_d |_{ker L_{d-2}}  has full row rank, every lower
solution extends through E_d (no sign condition at this order); if the radial row Delta^{(d-2)/2}P is missed,
order d carries a genuine scalar condition that must be met by lower-order (quadratic) freedom.
We compute rank M_d and the radial-row residual for d=4,6,8 at A02's saved first jets H2 (gen5, gen2, lsA)
and at random / Kahler H2.  Output: workspace/data/step68/kernel_absorption.json
"""
import json, sys, os
from pathlib import Path
import numpy as np
import torch
HERE = Path(__file__).resolve().parent
A02S = HERE.parents[2] / 'S1003A02' / 'workspace' / 'scripts'
sys.path.insert(0, str(A02S)); sys.path.insert(0, str(HERE))
from step78_real_tower import Tower
from step77_gn_germ import dev, dt
import step68_flat_cokernel as F
from step68_scalar_compatibility import P_matrix
from step68_cokernel_tower import ell_vector

OUT = HERE.parent / 'data' / 'step68'


def null_right(A, tol=1e-10):
    U, s, Vt = np.linalg.svd(A, full_matrices=True)
    r = int((s > tol * s[0]).sum()); return Vt[r:].T


def absorption(d, H2, lam, Kd, Pd, elld, Tcache):
    K = d - 2 + 0
    if (d, lam) not in Tcache:
        Tcache[(d, lam)] = Tower(d, lam)       # Evec orders up to d, jets to d+2
    T = Tcache[(d, lam)]
    T.degs = list(range(2, T.N + 1)); T.size = {e: 6 * len(T.mon_d[e]) for e in T.degs}
    H2t = torch.tensor(H2, dtype=dt, device=dev)
    nd = T.size[d]
    f = lambda k: T.Evec({2: H2t, d: k}, [d])[0]
    z = torch.zeros(nd, dtype=dt, device=dev)
    Kt = torch.tensor(Kd, dtype=dt, device=dev)
    vj = torch.func.vmap(lambda v: torch.func.jvp(f, (z,), (v,))[1])
    cols = [vj(Kt[:, s:s + 128].T).T for s in range(0, Kt.shape[1], 128)]
    DK = torch.cat(cols, dim=1).cpu().numpy()            # E_d x dimker
    M = Pd.astype(float) @ DK
    s = np.linalg.svd(M, compute_uv=False)
    rank = int((s > 1e-9 * s[0]).sum())
    # radial row: is elld (as a P-row combination) in the left null space of M?
    # elld = w^T Pd for the unique w (rows of Pd independent mod Bianchi); solve w
    w = np.linalg.lstsq(Pd.T.astype(float), elld.astype(float), rcond=None)[0]
    wres = float(np.linalg.norm(Pd.T.astype(float) @ w - elld) / np.linalg.norm(elld.astype(float)))
    rad = w @ M
    # left null space of M
    U, sv, Vt = np.linalg.svd(M)
    nl = U[:, rank:]
    rad_in_null = float(np.linalg.norm(rad) / (np.linalg.norm(w) * np.linalg.norm(M))) if True else None
    rec = {'d': d, 'lam': lam, 'n_rows': int(Pd.shape[0]), 'dim_ker': int(Kd.shape[1]), 'rank_M': rank,
           'sv_tail': [float(x) for x in s[-4:]], 'sv_top': float(s[0]),
           'radial_row_w_fit': wres, 'radial_row_image_rel': rad_in_null}
    if nl.shape[1]:
        wn = w / np.linalg.norm(w)
        rec['cos_radial_with_leftnull'] = float(np.linalg.norm(nl.T @ wn))
    return rec


def main():
    base = HERE.parents[2] / 'S1003A02' / 'workspace' / 'data' / 'step80'
    cases = []
    for name in ['recon_F012_gen5_lam-5', 'recon_F012_gen2_lam0', 'recon_lsA_jet0_lam-1']:
        dd = np.load(base / f'{name}.npz')
        lam = float(name.split('lam')[-1])
        cases.append((name, dd['H2'], lam))
    rng = np.random.default_rng(0)
    cases.append(('random_H2_lam-1', rng.standard_normal(60) * 0.3, -1.0))
    ds = [int(x) for x in os.environ.get('DS', '4,6,8').split(',')]
    pre = {}
    for d in ds:
        L = F.L_matrix(d - 2).astype(float)
        pre[d] = (null_right(L), P_matrix(d), ell_vector(d))
        print('d', d, 'dim ker L_{d-2} =', pre[d][0].shape[1], flush=True)
    out = []; Tc = {}
    for name, H2, lam in cases:
        for d in ds:
            r = absorption(d, H2, lam, *pre[d], Tc); r['case'] = name
            print(json.dumps(r), flush=True); out.append(r)
            (OUT / 'kernel_absorption.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    main()
