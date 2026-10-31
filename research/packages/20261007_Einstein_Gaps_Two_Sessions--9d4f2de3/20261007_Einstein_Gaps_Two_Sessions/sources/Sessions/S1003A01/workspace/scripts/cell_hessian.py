"""Exact (autodiff) Hessian of J6/(8pi^2) in the spectral cell parameters at an LM-stationary record,
plus the gradient; reports eigenvalues (local minimality inside the ansatz) and the softest directions.
Usage: python cell_hessian.py RECORD [--nq 1400] --out OUT.json
"""
import argparse, json
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from perp_dual_cost import DualCell, load_record, seed_vector

ap = argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--nq', type=int, default=1400); ap.add_argument('--out')
ap.add_argument('--newton', action='store_true')
a = ap.parse_args()
rec = load_record(a.record); deg = int(rec['deg'])
c = DualCell(float(rec['x0']), float(rec['X']), deg, deg, a.nq); c.aligned = False; c.wpow = 2
z = jnp.asarray(seed_vector(c, rec))
f = lambda zz: c.target(zz, 'J')
g = np.asarray(jax.grad(f)(z)); H = np.asarray(jax.hessian(f)(z)); H = (H+H.T)/2
ev, V = np.linalg.eigh(H)
# Newton step prediction (how far from the stationary point inside the ansatz)
keep = ev > 1e-10*ev[-1]
gp = V.T @ g
step = -(V[:, keep] @ (gp[keep]/ev[keep]))
gain = float(0.5*g @ step)   # predicted decrease (negative) over the non-null eigenspace
proj = [dict(eig=float(ev[i]), g_proj=float(gp[i]), newton_gain=float(-0.5*gp[i]**2/ev[i]) if keep[i] else None)
        for i in range(min(8, len(ev)))]
out = dict(record=a.record, X=float(rec['X']), x0=float(rec['x0']), J=float(f(z)), grad_inf=float(np.abs(g).max()),
           eig_min=float(ev[0]), eig_max=float(ev[-1]), eig_lowest=[float(e) for e in ev[:8]], n=int(len(ev)),
           newton_predicted_gain=gain, n_negative=int((ev < 0).sum()), n_null=int((~keep).sum()), lowest_modes=proj,
           newton_step_inf=float(np.abs(step).max()))
if '--newton' in __import__('sys').argv:
    z1 = np.asarray(z) + step
    out['J_after_newton'] = float(f(jnp.asarray(z1)))
    rec2 = dict(rec); rec2['z'] = [float(v) for v in z1]; rec2['J'] = out['J_after_newton']; rec2['method'] = 'newton_from_' + a.record
    Path(a.out.replace('.json', '_newton_record.json')).write_text(json.dumps(rec2)+'\n')
print(json.dumps(out))
if a.out: Path(a.out).write_text(json.dumps(out)+'\n')
