"""Dump neck profile of an o11_perp_logneck record: per-ds densities / x0^2 and u_i / x0.
Usage: python o11_logneck_profile.py record.json [out.csv]
"""
import sys, json
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from o11_perp_logneck import Cell

r = json.load(open(sys.argv[1]))
x0 = r['x0']; c = Cell(x0, r['deg'], 400, s_hi=r.get('s_hi', np.log(0.6)), smooth=r.get('smooth', False), ncore=r.get('ncore', 0), nout=r.get('nout', 0))
z = jnp.array(r['z'])
s = np.linspace(0.5*np.log(x0) - 2, np.log(0.85), 61)
t = jnp.array(np.exp(s))
D = np.array(jax.vmap(lambda tt: c.dens(z, tt))(t))
tn = np.exp(s)
rows = []
print(' s      t/sqrt(x0)   S1     S2     S3    cub   (sum)   scal  per ds /x0^2 | u1/x0  u2/t^2  u3*t^2/x0  u2u3/x0')
for i in range(len(s)):
    d = D[i]*tn[i]/x0**2
    rows.append([s[i], *d[:6], D[i, 6]/x0, D[i, 7]/tn[i]**2, D[i, 8]*tn[i]**2/x0, D[i, 7]*D[i, 8]/x0])
    if i % 3 == 0:
        print('%6.2f %9.3g %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f | %7.3f %7.3f %7.3f %7.3f' % (s[i], tn[i]/np.sqrt(x0), d[0], d[1], d[2], d[3], d[0]+d[1]+d[2]+d[3], d[5], D[i,6]/x0, D[i,7]/tn[i]**2, D[i,8]*tn[i]**2/x0, D[i,7]*D[i,8]/x0))
if len(sys.argv) > 2:
    np.savetxt(sys.argv[2], np.array(rows), delimiter=',', header='s,S1,S2,S3,cubic,Puncal,scal (per ds over x0^2),u1/x0,u2/t^2,u3 t^2/x0,u2u3/x0')
