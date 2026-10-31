"""Re-evaluate a saved o11_perp_logneck record with independent quadratures.
Usage: python o11_logneck_requad.py record.json
"""
import sys, json
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from o11_perp_logneck import Cell

r = json.load(open(sys.argv[1]))
z = jnp.array(r['z']); out = dict(record=sys.argv[1], x0=r['x0'])
for nq, ni in ((1200, 40), (2400, 80), (4800, 160), (8000, 300)):
    c = Cell(r['x0'], r['deg'], nq, s_hi=r.get('s_hi', np.log(0.6)), ninner=ni, smooth=r.get('smooth', False), ncore=r.get('ncore', 0), nout=r.get('nout', 0))
    I, D = c.terms(z); I = np.array(I)
    out['nq%d_ni%d' % (nq, ni)] = dict(Pm1_calib=float(I[:4].sum()), P_uncal_minus1=float(I[4] - 1),
                                      Jm1=float(I[:4].sum() + I[5]), S=[float(v) for v in I[:4]], scal=float(I[5]))
print(json.dumps(out, indent=1))
