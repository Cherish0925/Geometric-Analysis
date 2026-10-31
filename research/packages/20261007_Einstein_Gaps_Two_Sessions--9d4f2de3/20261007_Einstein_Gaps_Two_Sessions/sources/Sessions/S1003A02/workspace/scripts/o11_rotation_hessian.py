"""Quadratic rotation sector at an aligned optimized O11 cell.

The finite-angle code parametrizes phi=theta*(fixed profile + theta-independent
shape parameters), which is singular at theta=0 for computing the relaxed
second variation.  Here we instead use

    phi = theta*(1-smoothstep(v)) + v^3(1-v)^3 sum_j a_j T_j(2v-1),

where theta fixes the bolt/end relative angle and the a_j are unconstrained
linear rotation-profile modes.  At an aligned cell, parity under phi -> -phi
decouples this sector to second order from the diagonal F,G,w modes.  The
Schur complement of the Hessian in (theta,a) is therefore the relaxed
small-angle coefficient within the chosen Chebyshev rotation space.

Usage: python o11_rotation_hessian.py [x0 ...]
Reads data/o11rot/grid_x0<X>_th0.0.json and writes
 data/o11rot/rotation_hessian.json.
"""
import json, os, sys
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64', True)

from o11_rotated_cell import (Cell, cheb, rot2, metric_from,
                               curvature_scalars, ANG, PI)


class LinearRotationCell(Cell):
    def prof_factory_q(self, z, q):
        x0, ell, u1 = self.x0, self.ell, self.u1
        dU, dw = self.degU, self.degw
        cF = z[:dU]
        cG = z[dU:2*dU]
        cw = z[2*dU:2*dU+dw]
        shift = -(jnp.sum(cF*cheb(dU, jnp.array(-1.0)))
                  + jnp.sum(cG*cheb(dU, jnp.array(-1.0))))
        cG = cG.at[0].add(shift)
        theta, aa = q[0], q[1:]
        da = aa.shape[0]
        K = self.K

        def prof(x):
            u = jnp.log(x/x0)/ell
            zc = 2*u - 1
            Bu = cheb(max(dU, dw, 1), zc)
            qF = (1-u)**3*jnp.sum(cF*Bu[:dU])
            qG = (1-u)**3*jnp.sum(cG*Bu[:dU])
            Kx = K(x)
            F = Kx*jnp.exp(qF)
            G = Kx*jnp.exp(qG)
            w = u*(1-u)**3*jnp.sum(cw*Bu[:dw]) if dw > 0 else 0.0*u
            v = jnp.clip((u-u1)/(1-u1), 0.0, 1.0)
            step = 10*v**3 - 15*v**4 + 6*v**5
            shape = (v**3*(1-v)**3*jnp.sum(aa*cheb(da, 2*v-1))
                     if da > 0 else 0.0*v)
            phi = theta*(1-step) + shape
            Rm = rot2(phi)
            h = Rm @ jnp.diag(jnp.array([x*jnp.exp(w),
                                          x*jnp.exp(-w), F])) @ Rm.T
            return G, h
        return prof

    def P_q(self, z, q):
        g = metric_from(self.prof_factory_q(z, q))
        prof = self.prof_factory_q(z, q)

        def at(x):
            y = jnp.concatenate([jnp.array([x]), ANG])
            _, r0, _, _ = curvature_scalars(g, y)
            G, h = prof(x)
            dv = PI**2*jnp.sqrt(jnp.linalg.det(h)/G)
            return r0, dv

        r0, dv = jax.vmap(at)(self.xx)
        return jnp.sum(r0*dv*self.wx)/(8*PI**2)


def load_aligned(path):
    with open(path) as f:
        d = json.load(f)
    return np.asarray(d['z'], dtype=float), d


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    datadir = os.path.join(here, '..', 'data', 'o11rot')
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    opts = dict(a[2:].split('=') for a in sys.argv[1:] if a.startswith('--'))
    degr = int(opts.get('degr', 6)); nq = int(opts.get('nq', 300))
    xvals = args if args else ['0.03', '0.01', '0.003', '0.001']
    out = []
    for xs in xvals:
        x0 = float(xs)
        # Step-6 grid files are named grid_x0<x0 as passed on the command line>_th0.json
        p = os.path.join(datadir, f'grid_x0{xs}_th0.json')
        z, raw = load_aligned(p)
        # Step-6 grid: 6 U modes, 4 triaxial modes; degr free linear rotation modes.
        c = LinearRotationCell(x0, 1.0, 6, 4, degr, 0.05, nq)
        q0 = jnp.zeros(1+c.degr)
        H = np.asarray(jax.jit(jax.hessian(lambda q: c.P_q(jnp.array(z), q)))(q0))
        Haa = H[1:, 1:]
        Hta = H[0, 1:]
        evals = np.linalg.eigvalsh(Haa)
        sol = np.linalg.lstsq(Haa, Hta, rcond=1e-11)[0]
        schur = float(H[0, 0] - Hta @ sol)
        # P is already divided by 8 pi^2. Expansion is P=P0+(schur/2) theta^2.
        coeff = 0.5*schur/x0
        out.append(dict(x0=x0, degr=degr, nq=nq, P0=float(c.P_q(jnp.array(z), q0)),
                        Htt=float(H[0,0]), schur=schur,
                        relaxed_theta2_over_x0=coeff,
                        min_Haa=float(evals[0]), max_Haa=float(evals[-1]),
                        cond_Haa=float(evals[-1]/evals[0]),
                        optimal_a_per_theta=[float(v) for v in -sol],
                        source=os.path.relpath(p, os.path.join(here, '..', '..', '..', '..')),
                        aligned_optimizer_message=raw.get('msg'),
                        aligned_optimizer_iterations=raw.get('nit')))
        print(json.dumps(out[-1]))
    outpath = os.path.join(datadir, opts.get('out', 'rotation_hessian.json'))
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2)
    print('wrote', outpath)


if __name__ == '__main__':
    main()
