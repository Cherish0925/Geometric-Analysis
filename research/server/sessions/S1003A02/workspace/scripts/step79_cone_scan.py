#!/usr/bin/env python3
"""Step 79: map the order-6 scalar obstruction Phi6 over the real torsion cone, lambda, and the torsion-free
(W^-) part of the 2-jet.  Even branch H3 = 0 (odd jets only add conditions, see step77_79 note), plus an
optional H3 probe.

Jets: f = c z + (S + A) zbar, c in C, S complex symmetric, A = [[0,a],[-a,0]] with |a|^2 = (||S||^2+8|c|^2)/2
(cone), random phases; torsion norm tn = sqrt(4|c|^2+2||S||^2+2||A||^2) normalised to 1, so lam = lam/tn.
Output: workspace/data/<STEP79_OUT>/cone_<tag>.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
import step79_general_order6 as G
from step77_gn_germ import jet_coords


def random_cone_jet(rng, mode='generic'):
    cz = lambda: complex(*rng.standard_normal(2))
    c = cz()
    S = np.array([[cz(), cz()], [0, cz()]]); S[1, 0] = S[0, 1]
    if mode == 'smallc':
        c *= 0.05
    if mode == 'bigc':
        c *= 3
    s2 = np.sum(abs(S) ** 2)
    amod = np.sqrt((s2 + 8 * abs(c) ** 2) / 2)
    a = amod * np.exp(1j * rng.uniform(0, 2 * np.pi))
    A = np.array([[0, a], [-a, 0]])
    tn = np.sqrt(4 * abs(c) ** 2 + 2 * s2 + 2 * 2 * abs(a) ** 2)
    return c / tn, S / tn, A / tn


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--njets', type=int, default=4)
    ap.add_argument('--lams', default='-3,-1,0,1')
    ap.add_argument('--wscales', default='0')
    ap.add_argument('--mode', default='generic')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--h3', type=float, default=0.0)
    ap.add_argument('--tag', default='scan')
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed); torch.manual_seed(a.seed)
    lams = [float(x) for x in a.lams.split(',')]; ws = [float(x) for x in a.wscales.split(',')]
    jets = [random_cone_jet(rng, a.mode) for _ in range(a.njets)]
    out = {'args': vars(a), 'records': []}
    Ts = {lam: G.TowerAll(6, lam) for lam in lams}
    for ij, (c, S, A) in enumerate(jets):
        for lam in lams:
            T = Ts[lam]
            for w in ws:
                t0 = time.time()
                rs = np.random.default_rng(1000 * a.seed + ij)       # same W^- direction for all lam
                H2 = G.make_H2(T, 'jet', lam, rs, (c, S, A), 1.0, w)
                jc = jet_coords(T.torsion({2: H2, **G.zeros(T, skip=(2,))}))
                H3 = torch.zeros(T.size[3], dtype=G.dt, device=G.dev)
                if a.h3:
                    h3u, _ = G.admissible_H3(T, H2, rs)
                    H3 = a.h3 * h3u
                rec, cr, Jr, Hr = G.reduce_general(T, H2, H3)
                an = G.analyse(cr, Jr, Hr, rng, nlm=10)
                r = {'jet_index': ij, 'c': [c.real, c.imag], 'S': [[x.real, x.imag] for x in S.ravel()],
                     'a': [A[0, 1].real, A[0, 1].imag], 'lam': lam, 'wscale': w, 'h3': a.h3, 'jet': jc,
                     'reduce': rec, 'analysis': an, 'time': time.time() - t0}
                out['records'].append(r)
                print('jet', ij, 'lam', lam, 'w', w, 'c2 %.3g S2 %.3g A2 %.3g det %.3g' % (jc['c2'], jc['S2'], jc['A2'], jc['detD']),
                      'rows', rec['n_rows_nontrivial'], 'lin', '%.1e' % rec['lin_resid'],
                      {k: an.get(k) for k in ('joint_quad_rank', 'rank_J_on_common_kernel', 'n_scalar', 'definite', 'Phi6', 'lm_min')},
                      round(r['time'], 1), flush=True)
                (G.OUT / f'cone_{a.tag}.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    main()
