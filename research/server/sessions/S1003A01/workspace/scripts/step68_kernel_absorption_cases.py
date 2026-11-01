#!/usr/bin/env python3
"""Step 68i: which property of H2 causes the top-kernel rank deficiency of P(E_d) at d=6,8?
Cases: (a) H2 solving E0 only (random, off the cone), (b) Kahler H2 (torsion-free E0 solution),
(c) cone H2 from A02 (control).  Uses step68_kernel_absorption.absorption.
Output: workspace/data/step68/kernel_absorption_cases.json
"""
import json, sys
from pathlib import Path
import numpy as np
import torch
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / 'S1003A02' / 'workspace' / 'scripts')); sys.path.insert(0, str(HERE))
import step79_general_order6 as G
from step78_real_tower import Tower
import step68_kernel_absorption as KA
import step68_flat_cokernel as F
from step68_scalar_compatibility import P_matrix
from step68_cokernel_tower import ell_vector


def main():
    rng = np.random.default_rng(3)
    out = []
    pre = {}
    for d in (6, 8):
        pre[d] = (KA.null_right(F.L_matrix(d - 2).astype(float)), P_matrix(d), ell_vector(d))
    for lam in (-1.0, 0.0):
        T = Tower(6, lam); T.degs = list(range(2, T.N + 1)); T.size = {e: 6 * len(T.mon_d[e]) for e in T.degs}
        h0, N0, tor_vec = G.h2_tools(T)
        E0 = lambda h: T.Evec({2: h, **G.zeros(T, skip=(2,))}, [0])[0]
        cases = []
        x = torch.tensor(rng.standard_normal(N0.shape[1]) * 0.5, dtype=G.dt, device=G.dev)
        cases.append(('E0_only_random', h0 + N0 @ x))
        cases.append(('kahler', G.make_H2(T, 'kahler', lam, rng)))
        cases.append(('E0_only_random_small', h0 + N0 @ (0.05 * x)))
        for nm, H2 in cases:
            e0 = float(E0(H2).norm())
            tv = tor_vec(H2).cpu().numpy()
            for d in (6, 8):
                r = KA.absorption(d, H2.cpu().numpy(), lam, *pre[d], {})
                r.update({'case': nm, 'E0_norm': e0, 'torsion_vec_norm': float(np.linalg.norm(tv))})
                print(json.dumps(r), flush=True); out.append(r)
                OUT2 = HERE.parent / 'data' / 'step68b'; OUT2.mkdir(exist_ok=True)
                (OUT2 / 'kernel_absorption_cases.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    main()
