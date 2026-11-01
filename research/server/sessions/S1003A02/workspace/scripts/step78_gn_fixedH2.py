#!/usr/bin/env python3
"""Step 78: fixed-H2 Gauss-Newton tests of real solvability through order K (even ansatz).
H2: random real point on the order-2 quadric (E0=0 affine + scalar excess), or the Step-77 D6 jet.
For each H2 run GN on (H4,...,H_{K+2}) with equations E_2..E_K from several random starts.
Output: workspace/data/step78/gnfix_<tag>.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
from step77_gn_germ import dev, dt, jet_coords
from step78_real_tower import Tower, load_h2_from_d6, gn_solve, per_order
from step78_certificate import random_quadric_H2

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step78'


def main(K=6, lam=-3.0, seed=0, nh2=3, starts=2, init=0.1, iters=40, scale=1.0, h2src='random'):
    rng = np.random.default_rng(seed); torch.manual_seed(seed)
    T = Tower(K, lam)
    out = {'K': K, 'lam': lam, 'seed': seed, 'runs': []}
    for a in range(nh2):
        if h2src == 'd6':
            H2 = load_h2_from_d6(OUT.parent / 'step77_gn_D6_even_lam-3.0_s0.pt', T)[2]; info = {}
        else:
            H2, info = random_quadric_H2(T, lam, rng, scale)
        zero = {d: torch.zeros(T.size[d], dtype=dt, device=dev) for d in T.degs if d != 2}
        jc = jet_coords(T.torsion({2: H2, **zero}))
        tnorm = float(np.sqrt(4 * jc['c2'] + 2 * jc['S2'] + 2 * jc['A2']))
        rec = {'h2_index': a, 'jet': jc, 'info': info, 'H2_norm': float(H2.norm()), 'lam_over_torsion': lam / max(tnorm, 1e-30), 'starts': []}
        for s in range(starts):
            jets = {2: H2}
            for d in T.degs:
                if d != 2:
                    jets[d] = init * torch.randn(T.size[d], dtype=dt, device=dev)
            t0 = time.time()
            jets, hist, sv = gn_solve(T, jets, [d for d in T.degs if d >= 4], list(range(2, K + 1, 2)), iters=iters, log=False)
            po = per_order(T, jets)
            rec['starts'].append({'final': hist[-1], 'hist': hist, 'per_order': po, 'time': time.time() - t0,
                                  'jet_norms': {d: float(v.norm()) for d, v in jets.items()}})
            print('H2', a, 'c2 %.3g S2 %.3g A2 %.3g' % (jc['c2'], jc['S2'], jc['A2']), 'start', s, 'final %.3e' % hist[-1], 'its', len(hist), flush=True)
            torch.save({d: v.cpu() for d, v in jets.items()}, OUT / f'gnfix_K{K}_lam{lam}_s{seed}_h{a}_st{s}.pt')
        out['runs'].append(rec)
    (OUT / f'gnfix_K{K}_lam{lam}_{h2src}_s{seed}.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--K', type=int, default=6)
    ap.add_argument('--lam', type=float, default=-3.0)
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--nh2', type=int, default=3)
    ap.add_argument('--starts', type=int, default=2)
    ap.add_argument('--init', type=float, default=0.1)
    ap.add_argument('--iters', type=int, default=40)
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--h2src', default='random')
    a = ap.parse_args()
    main(a.K, a.lam, a.seed, a.nh2, a.starts, a.init, a.iters, a.scale, a.h2src)
