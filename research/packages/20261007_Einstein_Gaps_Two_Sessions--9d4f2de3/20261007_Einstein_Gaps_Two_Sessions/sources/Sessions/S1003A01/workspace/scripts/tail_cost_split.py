"""Cumulative J6/P cost of stored perpendicular cells beyond a radius x_p (8 pi^2 units).
Used to separate the core cost from the cost paid in the far collar/truncation region.
Usage: python tail_cost_split.py REC... --xp 5 10 20
"""
import argparse, json
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from perp_dual_cost import DualCell, load_record, seed_vector, PI

ap = argparse.ArgumentParser(); ap.add_argument('records', nargs='+')
ap.add_argument('--xp', type=float, nargs='+', default=[2, 5, 10, 20, 40]); ap.add_argument('--nq', type=int, default=1400)
a = ap.parse_args()
out = []
for p in a.records:
    rec = load_record(p); deg = int(rec['deg'])
    c = DualCell(float(rec['x0']), float(rec['X']), deg, deg, a.nq); c.aligned = False; c.wpow = 2
    z = jnp.asarray(seed_vector(c, rec))
    s, r0, wa, wb, dv = c.fields(z)
    W = np.asarray(c.wx*dv); xx = np.asarray(c.xx)
    pd = np.asarray(r0)*W/(8*PI**2); sd = np.asarray((s+24)**2)*W/(32*PI**2)
    row = dict(record=p, X=float(rec['X']), P=float(pd.sum()), J=float(pd.sum()+sd.sum()))
    for xp in a.xp:
        m = xx > xp
        row['P_beyond_%g' % xp] = float(pd[m].sum()); row['J_beyond_%g' % xp] = float(pd[m].sum()+sd[m].sum())
        row['J_core_%g' % xp] = row['J'] - row['J_beyond_%g' % xp]
    out.append(row); print(json.dumps(row))
