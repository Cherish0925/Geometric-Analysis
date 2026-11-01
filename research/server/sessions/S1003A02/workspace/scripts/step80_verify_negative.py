#!/usr/bin/env python3
"""Step 80: independent check of Phi6 < 0 cases.  If Phi6 <= 0 the reduced order-6 polynomial system
Psi(y) = c + J y + y^T H y / 2 (all 35 nontrivial rows, not only the scalar) must have a REAL zero;
LM from many starts should drive |Psi| to ~0.  Conversely Phi6 > 0 should leave LM min > 0.
Jets regenerated with the same RNG as step80_F012_scan (seed 42, same order of draws).
Output: workspace/data/step80/verify_negative.json
"""
import json, sys, os, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step80')
import step79_general_order6 as G
from step80_F012_scan import random_cone_jet

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step80'


def main():
    rng = np.random.default_rng(42)
    jets = {}
    for i in range(8):
        jets[f'gen{i}'] = random_cone_jet(rng, 'generic')
    which = [('gen2', 0.0), ('gen2', -5.0), ('gen0', 5.0), ('gen0', 0.0), ('gen1', -10.0), ('gen5', -5.0)]
    out = []
    Ts = {}
    for tag, lam in which:
        t0 = time.time()
        if lam not in Ts:
            Ts[lam] = G.TowerAll(6, lam)
        T = Ts[lam]
        c, S, A = jets[tag]
        jt = (complex(c), [[complex(S[i, j]) for j in range(2)] for i in range(2)],
              [[complex(A[i, j]) for j in range(2)] for i in range(2)])
        H2 = G.make_H2(T, 'jet', lam, np.random.default_rng(0), jt, 1.0, 0.0)
        H3 = torch.zeros(T.size[3], dtype=G.dt, device=G.dev)
        rec, cr, Jr, Hr = G.reduce_general(T, H2, H3)
        an = G.analyse(cr, Jr, Hr, np.random.default_rng(1), nlm=60)
        r = {'tag': tag, 'lam': lam, 'rows': rec['n_rows_nontrivial'], 'lin_resid': rec['lin_resid'],
             **{k: an.get(k) for k in ('joint_quad_rank', 'rank_J_on_common_kernel', 'n_scalar', 'definite', 'H_eig', 'c', 'Phi6', 'lm_min', '|c|')},
             'time': time.time() - t0}
        out.append(r)
        print(tag, lam, {k: r[k] for k in ('rows', 'n_scalar', 'definite', 'Phi6', 'lm_min', '|c|')}, 'Hmin', (r['H_eig'] or [None])[0], round(r['time'], 1), flush=True)
        (OUT / 'verify_negative.json').write_text(json.dumps(out, indent=1, default=float) + '\n')


if __name__ == '__main__':
    main()
