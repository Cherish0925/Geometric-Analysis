#!/usr/bin/env python3
"""Step 78: the scalar order-6 reality obstruction Phi6 for AKE germs with a torsion zero.

Finding (d6 jet): the 15 order-6 residual conditions Psi(y) (y = admissible H4 after orders 2,4) have
quadratic parts depending only on a 12-dim projection z = P y; 14 of the 15 are absorbed linearly by the
complementary H4 directions; the single remaining scalar condition is
    phi(z) = c + j.z + z^T H z / 2 = 0 ,  H definite (normalised positive).
It has a real solution iff  Phi6 := c - j H^{-1} j / 2 <= 0 .
This script computes Phi6 for torsion jets k (kernel part of H2, on the lambda-independent quadric) along a
lambda grid, H2(lambda) = lambda * h_unit + k.
Output: workspace/data/step78/phi6_<tag>.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
from step77_gn_germ import dev, dt, jet_coords
from step78_real_tower import Tower, load_h2_from_d6
from step78_certificate import random_quadric_H2
from step78_reduced_order6 import Reduced
from step78_quad6 import extract

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step78'


def scalar_reduce(c, J, H, tol=1e-9):
    m, n = J.shape
    Hs = np.concatenate([H[i] for i in range(m)], axis=1)
    U, s, _ = np.linalg.svd(Hs)
    r = int((s > tol * s[0]).sum())
    P, Kc = U[:, :r], U[:, r:]
    Jw = J @ Kc
    Uw, sw, _ = np.linalg.svd(Jw)
    rw = int((sw > tol * sw[0]).sum()) if sw.size else 0
    Pi = Uw[:, rw:]
    rec = {'joint_quad_rank': r, 'rank_J_on_common_kernel': rw, 'n_scalar': int(Pi.shape[1]),
           'sv_gap_quad': [float(x) for x in (s[r - 1] / s[0], s[r] / s[0] if r < len(s) else 0.0)],
           'sv_gap_lin': [float(x) for x in (sw[rw - 1] / sw[0], sw[rw] / sw[0] if rw < len(sw) else 0.0)]}
    if Pi.shape[1] != 1:
        return rec
    pi = Pi[:, 0]
    cr = float(pi @ c); jr = (pi @ J) @ P; Hr = np.einsum('i,iab->ab', pi, np.einsum('ab,ibc,cd->iad', P.T, H, P))
    ev = np.linalg.eigvalsh(Hr)
    if ev[-1] < 0:
        cr, jr, Hr, ev = -cr, -jr, -Hr, -ev[::-1]
    rec.update({'H_eig': [float(x) for x in ev], 'definite': bool(ev[0] > 0), 'c': cr, '|j|': float(np.linalg.norm(jr))})
    if ev[0] > 0:
        rec['Phi6'] = float(cr - 0.5 * jr @ np.linalg.solve(Hr, jr))
        rec['Phi6_over_c'] = rec['Phi6'] / abs(cr) if cr else None
    return rec


def main(lams, seed=0, nk=2, scale=1.0, from_d6=False, tag=None):
    rng = np.random.default_rng(seed); torch.manual_seed(seed)
    out = {'seed': seed, 'scale': scale, 'lams': lams, 'jets': []}
    T0 = Tower(6, -3.0)
    ks = []
    for a in range(nk):
        if from_d6 and a == 0:
            H2 = load_h2_from_d6(OUT.parent / 'step77_gn_D6_even_lam-3.0_s0.pt', T0)[2]
        else:
            H2, _ = random_quadric_H2(T0, -3.0, rng, scale)
        ks.append(H2)
    # unit lambda part: solve E0 at lambda=-3 with zero kernel part = h0(-3); h_unit = h0/(-3)
    zero = {d: torch.zeros(T0.size[d], dtype=dt, device=dev) for d in T0.degs if d != 2}
    E0 = lambda h: T0.Evec({2: h, **zero}, [0])[0]
    L0 = torch.func.jacfwd(E0)(torch.zeros(T0.size[2], dtype=dt, device=dev))
    h0 = -torch.linalg.pinv(L0) @ E0(torch.zeros(T0.size[2], dtype=dt, device=dev))
    hunit = h0 / (-3.0)
    for a, H2 in enumerate(ks):
        k = H2 - h0
        jc = jet_coords(T0.torsion({2: H2, **zero}))
        tn = float(np.sqrt(4 * jc['c2'] + 2 * jc['S2'] + 2 * jc['A2']))
        jrec = {'k_index': a, 'jet': jc, 'torsion_norm': tn, 'by_lambda': []}
        for lam in lams:
            t0 = time.time()
            T = Tower(6, lam)
            H2l = lam * hunit + k
            e0 = float(T.Evec({2: H2l, **zero}, [0])[0].norm())
            R = Reduced(T, H2l)
            c, J, H, r, P = extract(R)
            rec = scalar_reduce(c, J, H)
            rec.update({'lam': lam, 'lam_over_torsion': lam / tn, 'E0_resid': e0, 'n_cond': r, 'dims': R.dims, 'time': time.time() - t0})
            jrec['by_lambda'].append(rec)
            print('k', a, 'lam', lam, 'lam/tors %.3f' % (lam / tn), {kk: rec.get(kk) for kk in ('joint_quad_rank', 'rank_J_on_common_kernel', 'n_scalar', 'definite', 'c', 'Phi6', 'Phi6_over_c')}, 'Heig', rec.get('H_eig', [None])[:2], round(rec['time'], 1), flush=True)
        out['jets'].append(jrec)
        tag2 = tag or f's{seed}_sc{scale}'
        (OUT / f'phi6_{tag2}.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--lams', default='-3,0,3')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--nk', type=int, default=2)
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--d6', action='store_true')
    ap.add_argument('--tag', default=None)
    a = ap.parse_args()
    main([float(x) for x in a.lams.split(',')], a.seed, a.nk, a.scale, a.d6, a.tag)
