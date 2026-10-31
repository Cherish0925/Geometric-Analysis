"""Independent check of o11_perp_logneck cost formulas against direct JAX curvature
(o11_rotated_cell.metric_from / curvature_scalars, Euler-angle coordinates).
Coordinate x := t, G = 1/4 so dx^2/(4G) = dt^2; h = diag(a3^2, a1^2, a2^2) (s1 = bolt slot).
Usage: python o11_logneck_check.py x0 [zfile.json]
"""
import sys, json
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from o11_rotated_cell import metric_from, curvature_scalars, ANG, PI
from o11_perp_logneck import Cell

x0 = float(sys.argv[1])
deg = 24
z = jnp.zeros(3*deg)
if len(sys.argv) > 2:
    r = json.load(open(sys.argv[2])); deg = r['deg']; z = jnp.array(r['z'])
c = Cell(x0, deg, 1600, s_hi=r.get('s_hi', np.log(0.6)) if len(sys.argv) > 2 else np.log(0.6),
         smooth=r.get('smooth', False) if len(sys.argv) > 2 else False,
         ncore=r.get('ncore', 0) if len(sys.argv) > 2 else 0, nout=r.get('nout', 0) if len(sys.argv) > 2 else 0)

def prof(t):
    a = c.a_of_t(z, t)
    return jnp.array(0.25), jnp.diag(jnp.array([a[2]**2, a[0]**2, a[1]**2]))

g = metric_from(prof)

def at(t):
    y = jnp.concatenate([jnp.array([t]), ANG])
    s, r0, wa, wb = curvature_scalars(g, y)
    G, h = prof(t)
    return jnp.array([s, r0, PI**2*jnp.sqrt(jnp.linalg.det(h)/G)])

V = jax.vmap(at)(c.tt)
P_direct = float(jnp.sum(V[:, 1]*V[:, 2]*c.wt))/(8*PI**2)
J_direct = float(jnp.sum((V[:, 1] + (V[:, 0] + 24)**2/4)*V[:, 2]*c.wt))/(8*PI**2)
dens = np.array(V[:, 1]*V[:, 2]*c.wt)/(8*PI**2)
Dc = jax.vmap(lambda t: c.dens(z, t))(c.tt)
pu = np.array(Dc[:, 4]*c.wt)
bad = np.argsort(-np.abs(dens - pu))[:5]
print('worst nodes t, direct, uncal:', [(float(c.tt[i]), float(dens[i]), float(pu[i])) for i in bad])
print('P_direct over t>1.5*t1 :', float(dens[80:].sum()), ' uncal:', float(pu[80:].sum()))
I, D = c.terms(z)
I = np.array(I)
print(json.dumps(dict(x0=x0, P_direct=P_direct, P_calib=1 + float(I[:4].sum()), P_uncal=float(I[4]),
                      J_direct=J_direct, J_calib=1 + float(I[:4].sum() + I[5]),
                      s_end=float(V[-1, 0]), ric0_end=float(V[-1, 1]))))
