"""Volume profile and Rossi readout along large-bolt Einstein separatrices.

Purpose: test whether the Einstein orbit from a large O(-1) bolt keeps a large orbit volume
W=a1 a2 a3 all the way to the ACH block (no base-shrinking excursion).  If so, a shadowing
argument plus Lemma P/Lemma N would price standard-CR large-bolt cells by W times the Rossi
mismatch.  Reads the ACH1 separatrices from data/ach_fate/fate_b<b>.json.
Output: workspace/data/ach_fate/large_bolt_volume_profile.json
"""
import json, math, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ach_fate_enum import run  # noqa: E402
from ach_projected import md_to_Ly, to_compact  # noqa: E402

DATA = HERE.parent/'data'/'ach_fate'
rows = []
for b in [0.8, 2, 20]:
    rec = json.loads((DATA/f'fate_b{b:g}.json').read_text())
    for sp in rec['separatrices']:
        r1 = sp['read']['ACH1']
        if r1['min_dev'] > 1e-3:
            continue
        d = 0.5*(sp['d_lo']+sp['d_hi'])
        fate, s = run(b, d, dense=True)
        tt = np.linspace(s.t[0], min(s.t[-1], r1['t']), 4000)
        Z = np.array([md_to_Ly(x) for x in s.sol(tt).T])
        L = Z[:, :3]
        W = np.exp(L.sum(axis=1))
        C = np.array([to_compact(z, 0) for z in Z])
        phi = C[:, 4]+(C[:, 1]-C[:, 2])/4-C[:, 5]*np.sinh(C[:, 4])
        base = np.exp(L[:, 1]+L[:, 2])  # a_g a_h for fibre slot 1
        sel = tt > 0.05
        rows.append({'b': b, 'd': d, 't_ACH': r1['t'], 'rho_readout': r1['rho'],
                     'W_bolt_scale_b2': b*b, 'min_W_after_t0.05': float(W[sel].min()),
                     't_minW': float(tt[sel][np.argmin(W[sel])]),
                     'min_base_area_ag_ah': float(base.min()), 't_min_base': float(tt[np.argmin(base)]),
                     'base_at_start': float(base[0]),
                     'profile': [[float(t), float(w), float(k), float(z), float(p)] for t, w, k, z, p in
                                 zip(tt[::200], W[::200], C[::200, 3], C[::200, 5], phi[::200])]})
        print({k: v for k, v in rows[-1].items() if k != 'profile'})
(DATA/'large_bolt_volume_profile.json').write_text(json.dumps(rows, indent=1)+'\n')
