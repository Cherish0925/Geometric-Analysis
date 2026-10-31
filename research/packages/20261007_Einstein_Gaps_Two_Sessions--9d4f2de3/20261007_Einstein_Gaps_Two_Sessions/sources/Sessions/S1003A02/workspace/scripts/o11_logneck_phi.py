"""Boundary values of the relative calibration Phi = u1^2+u3^2+u1u2u3 and C = sum u^2 + u1u2u3
for a saved o11_perp_logneck record, at t -> 0 and t -> TC, plus the uncal-vs-calib split.
Usage: python o11_logneck_phi.py record.json
"""
import sys, json
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from o11_perp_logneck import Cell, TC

r = json.load(open(sys.argv[1]))
c = Cell(r['x0'], r['deg'], 2400, s_hi=r.get('s_hi', np.log(0.6)), smooth=r.get('smooth', False), ncore=r.get('ncore', 0), nout=r.get('nout', 0))
z = jnp.array(r['z'])
x0 = r['x0']
for t in [1e-6*np.sqrt(x0), 1e-4*np.sqrt(x0), 1e-2*np.sqrt(x0), TC*(1-1e-6), TC*(1-1e-3), TC*0.99]:
    u, a = c.u_of_t(z, jnp.array(t))
    u = np.array(u); a = np.array(a)
    Phi = u[0]**2 + u[2]**2 + u[0]*u[1]*u[2]
    print('t=%.3e  u=%s  a=%s  Phi=%.12e' % (t, u, a, Phi))
I, D = c.terms(z); I = np.array(I)
print('calib int', I[:4].sum(), ' uncal-1', I[4] - 1)
