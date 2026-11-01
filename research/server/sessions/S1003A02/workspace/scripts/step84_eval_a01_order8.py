#!/usr/bin/env python3
"""Step 84: evaluate A01's polished order-8 jet (gen5, lam=-5) in our own unreduced AKE tower.

Input:  A01 S1003A01/workspace/data/step69/order8_polished_{v,h10}_recon_F012_gen5_lam-5.npy
        v = (H4, H6, H8) in our TowerAll(8) layout; H10 separate; H2 from our data/step80/recon_F012_gen5_lam-5.npz.
Output: workspace/data/step84/eval_a01_order8_gen5_lam-5.json
Checks: E0..E8 norms (our Ricci of exp(H) minus lam exp(H)), torsion jet coordinates (cone, det, index),
        coefficient norms, and a scale-relative residual; also E0..E8 with H8,H10 zeroed as a control.
"""
import json, sys, os
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step84')
import step79_general_order6 as G
from step77_gn_germ import jet_coords

dev, dt = G.dev, G.dt
ROOT = Path(__file__).resolve().parents[3]
A01 = ROOT / 'S1003A01' / 'workspace' / 'data' / 'step69'
OUT = Path(__file__).resolve().parents[1] / 'data' / 'step84'


def main():
    T = G.TowerAll(8, -5.0)
    rec = np.load(Path(__file__).resolve().parents[1] / 'data' / 'step80' / 'recon_F012_gen5_lam-5.npz')
    v = np.load(A01 / 'order8_polished_v_recon_F012_gen5_lam-5.npy')
    h10 = np.load(A01 / 'order8_polished_h10_recon_F012_gen5_lam-5.npy')
    s4, s6, s8, s10 = T.size[4], T.size[6], T.size[8], T.size[10]
    assert v.shape[0] == s4 + s6 + s8 and h10.shape[0] == s10, (v.shape, h10.shape, T.size)
    tt = lambda x: torch.tensor(x, dtype=dt, device=dev)
    jets = G.zeros(T)
    jets[2] = tt(rec['H2']); jets[4] = tt(v[:s4]); jets[6] = tt(v[s4:s4 + s6]); jets[8] = tt(v[s4 + s6:]); jets[10] = tt(h10)
    out = {'sizes': {d: T.size[d] for d in (2, 4, 6, 8, 10)},
           'coef_norm': {f'H{d}': float(jets[d].norm()) for d in (2, 4, 6, 8, 10)}}
    E = {f'E{k}': float(T.Evec(jets, [k])[0].norm()) for k in range(9)}
    out['E_unreduced'] = E
    # odd orders vanish by parity; scale-relative: compare E8 with the size of its individual Ricci terms
    j0 = dict(jets); j0[10] = torch.zeros_like(jets[10])
    out['E8_without_H10'] = float(T.Evec(j0, [8])[0].norm())
    j1 = dict(jets); j1[8] = torch.zeros_like(jets[8]); j1[10] = torch.zeros_like(jets[10])
    out['E6_without_H8'] = float(T.Evec(j1, [6])[0].norm())
    out['jet'] = jet_coords(T.torsion({2: jets[2], **G.zeros(T, skip=(2,))}))
    # compare with our own order-6 reconstruction H4,H6 (same lower data?)
    out['dist_H4_to_our_recon'] = float(np.linalg.norm(v[:s4] - rec['H4']) / np.linalg.norm(rec['H4']))
    out['dist_H6_to_our_recon'] = float(np.linalg.norm(v[s4:s4 + s6] - rec['H6']) / np.linalg.norm(rec['H6']))
    print(json.dumps(out, indent=1, default=float))
    (OUT / 'eval_a01_order8_gen5_lam-5.json').write_text(json.dumps(out, indent=1, default=float) + '\n')


if __name__ == '__main__':
    main()
