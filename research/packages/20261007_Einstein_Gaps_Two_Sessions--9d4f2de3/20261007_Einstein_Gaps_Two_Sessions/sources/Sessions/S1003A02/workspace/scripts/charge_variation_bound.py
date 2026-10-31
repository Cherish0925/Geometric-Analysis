"""Charge-variation lower bound along trajectories.

Because the chiral identities hold on every annulus, they hold pointwise in t:
   dP_hat/dt = d b_pm/dt + (nonnegative Weyl and scalar densities).
Hence  P_hat >= int max(0, b_+', b_-') dt,  the 'charge-variation functional'.
This script evaluates its discrete version sum_k max(0, Db_+, Db_-) on node data
(and the positive variations of each charge separately) and compares with the cost.
Usage: python charge_variation_bound.py files...
Output: workspace/data/saturation_control/charge_variation.json
"""
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
from chiral_two_sided_bound import charges  # noqa: E402

OUT = Path(__file__).resolve().parents[1]/'data'/'saturation_control'/'charge_variation.json'
rows = []
for f in sys.argv[1:]:
    r = json.loads(Path(f).read_text())
    bb = np.array([charges(x) for x in r['X']])
    d = np.diff(bb, axis=0)
    rows.append({'file': Path(f).name, 'cost': r['cost'],
                 'Vplus_bplus': float(np.clip(d[:, 0], 0, None).sum()),
                 'Vplus_bminus': float(np.clip(d[:, 1], 0, None).sum()),
                 'int_max': float(np.clip(d.max(axis=1), 0, None).sum())})
    print(rows[-1])
OUT.write_text(json.dumps(rows, indent=1)+'\n')
