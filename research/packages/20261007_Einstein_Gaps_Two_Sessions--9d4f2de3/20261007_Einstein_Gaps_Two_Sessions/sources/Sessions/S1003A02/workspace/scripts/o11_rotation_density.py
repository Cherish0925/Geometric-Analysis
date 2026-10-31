"""Local quadratic density of the O11 rotation sector at an aligned optimized cell.

At an aligned (theta=0) SU(2)_L cell the integrand r0*dvol of P is pointwise
invariant under a constant (1,3)-rotation (right translation).  Hence to second
order in the rotation profile phi(x) the local density is

    L = A(x) phi'^2 + 2 B(x) phi' phi'' + C(x) phi''^2 ,

and  P(phi) - P0 = (1/8pi^2) int (A phi'^2 + 2B phi'phi'' + C phi''^2) dx .
A,B,C are computed by a pointwise JAX Hessian with the local test profile
phi(t) = p1 (t-x) + p2 (t-x)^2/2.  We then (i) check that this quadratic form
reproduces the Schur complement of o11_rotation_hessian.py on its optimal
Chebyshev profile, and (ii) minimise it over a much richer space of profiles
psi = phi' (polynomial in u = log(x/x0)/ell vanishing to 2nd order at both ends,
so phi is locally constant at the bolt and C^2-flat at X), subject to
int psi dx = -theta.  The minimum is theta^2 * x0 * coef, coef = relaxed
small-angle coefficient in the full radial rotation sector.

Usage: python o11_rotation_density.py x0 [x0 ...]   -> data/o11rot/rotation_density_x0<x0>.json
"""
import json, os, sys
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from o11_rotated_cell import Cell, cheb, rot2, metric_from, curvature_scalars, ANG, PI


def build(x0, z):
    c = Cell(x0, 1.0, 6, 4, 0, 0.05, 300)
    dU, dw = 6, 4
    cF = jnp.array(z[:dU]); cG = jnp.array(z[dU:2*dU]); cw = jnp.array(z[2*dU:2*dU+dw])
    shift = -(jnp.sum(cF*cheb(dU, jnp.array(-1.0))) + jnp.sum(cG*cheb(dU, jnp.array(-1.0))))
    cG = cG.at[0].add(shift)
    ell, K = c.ell, c.K

    def diag(x):
        u = jnp.log(x/x0)/ell
        Bu = cheb(dU, 2*u-1)
        F = K(x)*jnp.exp((1-u)**3*jnp.sum(cF*Bu[:dU]))
        G = K(x)*jnp.exp((1-u)**3*jnp.sum(cG*Bu[:dU]))
        w = u*(1-u)**3*jnp.sum(cw*Bu[:dw])
        return F, G, w

    def L_at(x, p):
        def prof(t):
            F, G, w = diag(t)
            phi = p[0]*(t-x) + 0.5*p[1]*(t-x)**2
            Rm = rot2(phi)
            return G, Rm @ jnp.diag(jnp.array([t*jnp.exp(w), t*jnp.exp(-w), F])) @ Rm.T
        g = metric_from(prof)
        y = jnp.concatenate([jnp.array([x]), ANG])
        _, r0, _, _ = curvature_scalars(g, y)
        G, h = prof(x)
        return r0*PI**2*jnp.sqrt(jnp.linalg.det(h)/G)

    H = jax.jit(jax.vmap(lambda x: jax.hessian(lambda p: L_at(x, p))(jnp.zeros(2))))
    return c, H


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    dd = os.path.join(here, '..', 'data', 'o11rot')
    for xs in sys.argv[1:]:
        x0 = float(xs)
        raw = json.load(open(os.path.join(dd, f'grid_x0{xs}_th0.json')))
        z = np.asarray(raw['z'])
        c, Hf = build(x0, z)
        xx = np.asarray(c.xx); wx = np.asarray(c.wx)
        Hs = np.asarray(Hf(c.xx))
        A = 0.5*Hs[:, 0, 0]; B = 0.5*Hs[:, 0, 1]; C = 0.5*Hs[:, 1, 1]
        ell = c.ell
        u = np.log(xx/x0)/ell
        res = {}
        # (i) reproduce the Chebyshev-sector Schur value using the Step-8 optimal profile
        rh = os.path.join(dd, f'rh_x{xs}_d8_n300.json')
        if os.path.exists(rh):
            r = json.load(open(rh))[0]
            a = np.asarray(r['optimal_a_per_theta'])
            uj = jnp.array(u)
            def phi_fun(uu):
                v = jnp.clip((uu-0.05)/0.95, 0.0, 1.0)
                step = 10*v**3 - 15*v**4 + 6*v**5
                return (1-step) + v**3*(1-v)**3*jnp.sum(jnp.array(a)*cheb(len(a), 2*v-1))
            dphi_du = jax.vmap(jax.grad(phi_fun)); d2phi_du2 = jax.vmap(jax.grad(jax.grad(phi_fun)))
            pu = np.asarray(dphi_du(uj)); puu = np.asarray(d2phi_du2(uj))
            p1 = pu/(ell*xx); p2 = (puu - ell*pu)/(ell*xx)**2
            Q = np.sum((A*p1**2 + 2*B*p1*p2 + C*p2**2)*wx)/(8*PI**2)
            res['check_cheb_d8'] = dict(Q_density=float(Q), half_schur_from_hessian=0.5*r['schur'],
                                        coef_density=float(Q/x0), coef_hessian=r['relaxed_theta2_over_x0'])
        # (ii) minimise over psi(u) = u^2(1-u)^2 sum b_j T_j(2u-1)
        out = []
        for N in [8, 16, 32, 48, 64]:
            zc = 2*u - 1
            T = np.polynomial.chebyshev.chebvander(zc, N-1).T          # N x nq
            dT = np.array([np.polynomial.chebyshev.chebval(zc, np.polynomial.chebyshev.chebder(np.eye(N)[j]))*2 for j in range(N)])
            bump = u**2*(1-u)**2; dbump = 2*u*(1-u)**2 - 2*u**2*(1-u)
            Psi_u = bump*T                                             # dphi/du basis
            dPsi_u = dbump*T + bump*dT
            p1 = Psi_u/(ell*xx); p2 = (dPsi_u - ell*Psi_u)/(ell*xx)**2
            M = ((A*wx)*p1) @ p1.T + ((B*wx)*p1) @ p2.T + ((B*wx)*p2) @ p1.T + ((C*wx)*p2) @ p2.T
            M = M/(8*PI**2)
            cvec = Psi_u @ (np.full_like(u, 1.0)*(1.0/len(u))*0)  # placeholder
            # constraint: phi(X)-phi(x0) = int dphi/du du = -1  (theta=1)
            du_w = wx/(ell*xx)
            cvec = Psi_u @ du_w
            ev = np.linalg.eigvalsh(0.5*(M+M.T))
            sol = np.linalg.lstsq(M, cvec, rcond=1e-14)[0]
            Qmin = 1.0/float(cvec @ sol)
            out.append(dict(N=N, coef=Qmin/x0, min_eig=float(ev[0]), cond=float(ev[-1]/abs(ev[0]))))
        # local profile of the optimal psi at the largest N, and where it concentrates
        b = sol/(cvec @ sol)
        psi = b @ Psi_u
        res.update(x0=x0, minimisation=out, aligned_P0=raw['opt']['P'],
                   aligned_slope=(raw['opt']['P']-1)/x0,
                   A_min=float(A.min()), C_min=float(C.min()),
                   ACmB2_min=float((A*C-B**2).min()),
                   u_peak_psi=float(u[np.argmax(np.abs(psi))]),
                   x_peak_psi=float(xx[np.argmax(np.abs(psi))]),
                   sqrt_x0=float(np.sqrt(x0)))
        np.savez(os.path.join(dd, f'rotation_density_x0{xs}.npz'), x=xx, u=u, A=A, B=B, C=C, w=wx, psi=psi)
        json.dump(res, open(os.path.join(dd, f'rotation_density_x0{xs}.json'), 'w'), indent=1)
        print(json.dumps(res))


if __name__ == '__main__':
    main()
