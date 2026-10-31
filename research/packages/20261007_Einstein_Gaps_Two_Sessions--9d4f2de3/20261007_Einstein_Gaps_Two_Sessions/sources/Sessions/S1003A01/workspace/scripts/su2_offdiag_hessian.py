"""Second variation of J6 in non-diagonal SU(2)-invariant directions at a diagonal cell.

Question: is the converged diagonal (triaxial Bianchi IX) perpendicular CH cell a local
minimum of J6 among *all* SU(2)-invariant metrics dt^2 + h_ij(t) s_i s_j, or does breaking
the diagonal ansatz lower the cost?

Background: DualCell profile (stable cG[0] interpretation), h=diag(F, x, x e^w) in the
peer slot order (s1 = bolt slot, s3 = CH-fibre slot).  Perturbation
    h_ij -> h_ij + k_ij(x),  i<j,
    k_ij = N_ij(x) u^2 (1-u)^3 sum_m c^{ij}_m T_m(2u-1),   u = log(x/x0)/log(X/x0),
with CH reference norms N_12 = x, N_13 = N_23 = x sqrt(1+x).  The factor u^2 ~ r^4 at the bolt
(x-x0 ~ r^2) gives a smooth tensor for every circle weight <= 4; (1-u)^3 gives C^2 contact
with the exact CH collar at X.  Constant rotations (diffeomorphisms) are excluded.

The sign flips s_i -> -s_i, s_j -> -s_j (conjugations in SU(2)) preserve diagonal metrics and
act on the three off-diagonal channels by distinct characters, so the first variation vanishes
and the Hessian is block diagonal; both facts are checked numerically.

Curvature: full coordinate Ricci by autodiff in Euler-angle coordinates (peer
`curvature_scalars`), valid for arbitrary symmetric h.  Output: J6/(8 pi^2) at c=0, the gradient,
the Hessian blocks and their spectra.  Numerical (float64) evidence, not a proof.

Usage: python su2_offdiag_hessian.py RECORD --n 8 --nq 600 --out OUT.json
"""
import argparse, json, math, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from perp_dual_cost import DualCell, load_record, seed_vector
from o11_perp_cell import metric_from, curvature_scalars, ANG, PI, cheb

PAIRS = [(0, 1), (0, 2), (1, 2)]


def build(rec, n, nq, boltrot=False):
    """If boltrot, channels 12 and 13 get one extra coefficient psi: an infinitesimal
    rotation [Psi,h]_ij = psi (h_jj-h_ii) chi(u), chi=(1-u)^3(1+3u+6u^2)=1+O(u^3).  This
    rotates the collapsing bolt direction (smooth: it is a constant rotation to O(r^6)) and is
    cut off to C^2 contact at the collar.  Channel 23 needs none: the bolt is round."""
    m = n+1 if boltrot else n
    deg = int(rec['deg']); x0 = float(rec['x0']); X = float(rec['X'])
    c = DualCell(x0, X, deg, deg, nq); c.aligned = False; c.wpow = 2
    z = jnp.asarray(np.asarray(seed_vector(c, rec), float))
    base = c.prof_factory(z)

    def J(cc):
        cc = cc.reshape(3, m)

        def prof(x):
            G, h = base(x)
            u = jnp.log(x/x0)/c.ell
            B = cheb(n, 2*u-1)
            env = u**2*(1-u)**3
            N = jnp.array([x, x*jnp.sqrt(1+x), x*jnp.sqrt(1+x)])
            chi = (1-u)**3*(1+3*u+6*u*u)
            if boltrot:
                # exact rotation by angle psi*chi in the (1,2) and (1,3) planes (admissible curve)
                # A global constant rotation is a diffeomorphism (right translation), so the
                # bolt rotation by psi*chi is isometric to the rotation by psi*(chi-1), which
                # vanishes to O(u^3) at the bolt and is the constant -psi on the collar (a
                # rotated, isometric CH).  This form avoids float cancellation at the bolt.
                for p, (i, j) in enumerate(PAIRS[:2]):
                    b = cc[p, n]*(chi-1); R = jnp.eye(3)
                    R = R.at[i, i].set(jnp.cos(b)).at[j, j].set(jnp.cos(b)).at[i, j].set(-jnp.sin(b)).at[j, i].set(jnp.sin(b))
                    h = R @ h @ R.T
            for p, (i, j) in enumerate(PAIRS):
                kij = N[p]*env*jnp.sum(cc[p, :n]*B)
                h = h.at[i, j].add(kij).at[j, i].add(kij)
            return G, h
        g = metric_from(prof)

        def at(x):
            y = jnp.concatenate([jnp.array([x]), ANG])
            s, r0, wa, wb = curvature_scalars(g, y)
            G, h = prof(x)
            return r0 + (s+24.0)**2/4, PI**2*jnp.sqrt(jnp.linalg.det(h)/G)
        dens, dv = jax.vmap(at)(c.xx)
        return jnp.sum(dens*dv*c.wx)/(8*PI**2)
    return J, c, m


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--n', type=int, default=8)
    ap.add_argument('--nq', type=int, default=600); ap.add_argument('--out'); ap.add_argument('--boltrot', action='store_true')
    a = ap.parse_args(); rec = load_record(a.record)
    J, c, m = build(rec, a.n, a.nq, a.boltrot); t = time.time()
    c0 = jnp.zeros(3*m)
    J0 = float(jax.jit(J)(c0)); g0 = np.asarray(jax.jit(jax.grad(J))(c0))
    H = np.asarray(jax.jit(jax.jacfwd(jax.grad(J)))(c0)); H = 0.5*(H+H.T)
    out = dict(record=a.record, x0=c.x0, X=c.X, n=a.n, m=m, boltrot=a.boltrot, nq=a.nq, J0=J0, grad_inf=float(np.max(np.abs(g0))))
    blocks = {}
    for p, (i, j) in enumerate(PAIRS):
        Hb = H[p*m:(p+1)*m, p*m:(p+1)*m]
        ev, V = np.linalg.eigh(Hb)
        blocks[f'h{i+1}{j+1}'] = dict(eig=[float(v) for v in ev], min_vec=[float(v) for v in V[:, 0]],
                                     grad_inf=float(np.max(np.abs(g0[p*m:(p+1)*m]))))
    off = H.copy()
    for p in range(3):
        off[p*m:(p+1)*m, p*m:(p+1)*m] = 0
    out['H_blocks'] = {f'h{i+1}{j+1}': H[p*m:(p+1)*m, p*m:(p+1)*m].tolist()
                       for p, (i, j) in enumerate(PAIRS)}
    out.update(blocks=blocks, offblock_max=float(np.max(np.abs(off))), H_max=float(np.max(np.abs(H))),
               sec=time.time()-t)
    print(json.dumps(out, indent=1))
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1)+'\n')


if __name__ == '__main__':
    main()
