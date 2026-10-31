"""Levenberg-Marquardt (Gauss-Newton) minimization of J6/(8 pi^2) for perpendicular CH cells.

J6/(8pi^2) = sum_q r_q^2 with residuals built from the exact Cartan spin formulas (Step 7):
  z_i = r_i - v_i (|Ric0|^2 = sum z_i^2),  s = -2 sum (r_i+v_i),
  P/(8pi^2) = (1/4) int a1a2a3 |z|^2 dt,  (J-P)/(8pi^2) = (1/16) int a1a2a3 (s+24)^2 dt,
  dt = dx/(2 sqrt G).
Residual vector  r = sqrt(wx * a1a2a3/(2 sqrt G)) * [z1/2, z2/2, z3/2, (s+24)/4]  on the cell quadrature.
L-BFGS on these ill-conditioned spectral parametrizations stalls with large gradients; a least-squares
Jacobian method addresses the conditioning directly.  Works for plain DualCell records and TailCell.
Usage: python perp_lm.py SEED OUT [--tail --xa 4 --xb 16 --c0 -0.9] [--X 256 --deg 24] [--nq 1400]
"""
import argparse, json, math, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.optimize import least_squares
from perp_dual_cost import DualCell, load_record, seed_vector
from perp_tail_cell import TailCell, stripped_seed
from perp_collar_continue import physical_extension_seed


def residual_fn(cell):
    def res(z):
        prof = cell.prof_factory(z)
        def radii(x):
            G, h = prof(x)
            return jnp.sqrt(jnp.array([h[1, 1], h[2, 2], h[0, 0]])), G
        def state(x):
            a, G = radii(x)
            da = jax.jacfwd(lambda xx: radii(xx)[0])(x)*2*jnp.sqrt(G)
            a1, a2, a3 = a
            u = jnp.array([da[0] - (a2**2 + a3**2 - a1**2)/(a2*a3),
                           da[1] - (a3**2 + a1**2 - a2**2)/(a3*a1),
                           da[2] - (a1**2 + a2**2 - a3**2)/(a1*a2)])
            return u, a, G
        def at(x, wx):
            u, a, G = state(x)
            du = jax.jacfwd(lambda xx: state(xx)[0])(x)*2*jnp.sqrt(G)
            a1, a2, a3 = a; u1, u2, u3 = u
            H = jnp.array([u1 + u2*u3/2, u2 + u3*u1/2, u3 + u1*u2/2])
            r = du/a
            v = 2*H/jnp.array([a2*a3, a3*a1, a1*a2])
            z = r - v; s = -2*jnp.sum(r + v)
            wt = jnp.sqrt(wx*a1*a2*a3/(2*jnp.sqrt(G)))
            return wt*jnp.concatenate([z/2, jnp.array([(s+24)/4])])
        return jax.vmap(at)(cell.xx, cell.wx).reshape(-1)
    return res


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('seed'); ap.add_argument('out')
    ap.add_argument('--X', type=float); ap.add_argument('--deg', type=int); ap.add_argument('--nq', type=int, default=1400)
    ap.add_argument('--tail', action='store_true'); ap.add_argument('--xa', type=float, default=4.0)
    ap.add_argument('--xb', type=float, default=16.0); ap.add_argument('--c0', type=float, default=0.0)
    ap.add_argument('--strip', action='store_true'); ap.add_argument('--max_nfev', type=int, default=200)
    ap.add_argument('--x0', type=float, help='override bolt area; seed coefficients reused as shape seed')
    a = ap.parse_args()
    old = load_record(a.seed); x0 = float(old['x0'])
    if a.x0 is not None:
        x0 = a.x0
    X = a.X or float(old['X']); deg = a.deg or int(old['deg'])
    if a.tail:
        c = TailCell(x0, X, deg, deg, a.nq); c.aligned = False; c.wpow = 2; c.setup_tail(a.xa, a.xb)
        if 'c_tail' in old and float(old['X']) == X and int(old['deg']) == deg:
            z0 = np.asarray(old['z'], float)
        elif a.strip:
            z0 = stripped_seed(old, c, a.c0, deg)
        elif float(old['X']) == X and int(old['deg']) == deg:
            z0 = np.r_[np.asarray(old['z'], float), a.c0]
        else:
            z0 = np.r_[physical_extension_seed(old, X, deg)[0], a.c0]
    else:
        c = DualCell(x0, X, deg, deg, a.nq); c.aligned = False; c.wpow = 2
        if float(old['X']) == X and int(old['deg']) == deg:
            z0 = np.asarray(seed_vector(c, old), float)
        else:
            z0 = physical_extension_seed(old, X, deg)[0]
    # PerpCell.prof_factory replaces cG[0] by a bolt-condition shift in which the
    # raw cG[0] cancels identically.  Remove this exact null coordinate before
    # optimization; otherwise huge stored values cause floating cancellation and
    # a singular Jacobian.  TailCell has the same first 3*deg layout.
    redundant = deg
    active = np.array([i for i in range(len(z0)) if i != redundant], dtype=int)
    z0[redundant] = 0.0
    def pack(y):
        zz = np.zeros(len(z0)); zz[active] = y
        return zz
    y0 = z0[active]
    R = jax.jit(residual_fn(c)); Jac = jax.jit(jax.jacfwd(residual_fn(c)))
    r0 = np.asarray(R(jnp.asarray(z0)))
    p0, j0, q0 = [float(v) for v in c.costs(jnp.asarray(z0))]
    print('seed: sum r^2 =', float(r0 @ r0), ' DualCell costs P,J =', p0, j0, flush=True)
    t = time.time()
    sol = least_squares(lambda y: np.asarray(R(jnp.asarray(pack(y)))), y0,
                        jac=lambda y: np.asarray(Jac(jnp.asarray(pack(y))))[:, active],
                        method='trf', x_scale='jac', ftol=1e-15, xtol=1e-15, gtol=1e-15, max_nfev=a.max_nfev)
    z = pack(sol.x); rr = sol.fun
    p, j, q = [float(v) for v in c.costs(jnp.asarray(z))]
    g_active = 2*sol.jac.T @ rr
    g_full = 2*np.asarray(Jac(jnp.asarray(z))).T @ rr
    out = dict(x0=x0, X=X, deg=deg, nq=a.nq, target='J', method='least_squares_trf', P=p, J=j, scalar=q,
               J_resid=float(rr @ rr), grad_inf=float(np.max(np.abs(g_active))),
               grad_inf_full=float(np.max(np.abs(g_full))), redundant_index=int(redundant), nfev=int(sol.nfev),
               status=int(sol.status), message=str(sol.message), source=a.seed, seed_costs=dict(P=p0, J=j0),
               sec=time.time()-t, z=[float(v) for v in z])
    if a.tail:
        out.update(c_tail=float(z[-1]), xa=a.xa, xb=a.xb)
    print(json.dumps({k: v for k, v in out.items() if k != 'z'})); Path(a.out).write_text(json.dumps(out)+'\n')

if __name__ == '__main__': main()
