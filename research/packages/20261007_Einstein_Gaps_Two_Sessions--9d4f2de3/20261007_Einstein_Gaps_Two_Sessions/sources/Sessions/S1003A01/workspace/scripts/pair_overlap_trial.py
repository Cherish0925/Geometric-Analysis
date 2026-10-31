"""Overlapping-tail two-cell trial metric on complex hyperbolic space (S1003A01 Step 13).

Two copies of the frozen perpendicular cell (x0 = 1/100, record z) are placed in CH^2
(ball model, holomorphic sectional curvature -4, Ric = -6 g):
    cell 1 centred at 0 in its standard U(2)-frame,
    cell 2 = phi_a o L_theta (cell),  phi_a the ball involution 0 <-> a, a = (tanh d, 0),
             L_theta(z) = e^{i theta} z  (rotates the cell's contact frame by 2 theta).
Each cell is written over its tail as g_CH + h_i with h_i diagonal in the CH orthonormal
coframe of cell i:  lambda = (G_CH/G, F/x, 1, e^w/(1+x)),  x = sinh^2 r_i.
Trial metric: g = g_CH + h_1 + h_2.  It equals cell 1 / cell 2 / CH outside the lens
L = B_rho(0) cap B_rho(a), rho = asinh(sqrt X); hence
    J(trial) - J(cell1) - J(cell2) = int_L [ |E(g)|^2 dV_g - |E(g1)|^2 dV_g1 - |E(g2)|^2 dV_g2 ],
with E = Ric + 6 g.  We also record the quadratic proxy 2 int_L <E(g1),E(g2)>_{g_CH} dV_CH.
Ricci tensors are computed by forward-mode autodiff of the explicit coordinate metric (no
symmetry assumption), so the single-cell densities serve as a check against the Bianchi formula.

Overlap depth w = 2 rho - d.  Outputs normalised by 8 pi^2.
Usage: python pair_overlap_trial.py RECORD.json --w 0.05,0.1 --theta 0,0.785 --n 18 --out OUT.json
"""
import argparse, json, math, time, os
from pathlib import Path
os.environ.setdefault('XLA_FLAGS', '--xla_cpu_multi_thread_eigen=true')
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.stats import qmc


def make_profile(rec):
    d = int(rec['deg']); z = np.array(rec['z'], float)
    cF, cG, cW = z[:d].copy(), z[d:2*d].copy(), z[2*d:3*d].copy()
    cG[0] += -sum(((-1)**k)*(cF[k]+cG[k]) for k in range(d))
    x0 = 0.01; X = float(rec['X']); ell = math.log(X/x0)

    def cheb(c, s):
        T0, T1 = 1.0, s; acc = c[0]*T0 + c[1]*T1
        for k in range(2, len(c)):
            T0, T1 = T1, 2*s*T1 - T0; acc = acc + c[k]*T1
        return acc

    def lam(r):
        """CH-orthonormal diagonal ratios (radial, bolt slot, contact slot, fibre) for r<rho."""
        x = jnp.sinh(r)**2
        u = jnp.log(x/x0)/ell
        s = 2*u - 1; om3 = (1-u)**3
        S = u**3*(10 - 15*u + 6*u*u)
        F = (x - x0)*jnp.exp(om3*cheb(cF, s)) + x0*S
        G = ((x - x0) + (x*x + x0)*S)*jnp.exp(om3*cheb(cG, s))
        w = jnp.log1p(x)*S + u*u*om3*cheb(cW, s)
        return jnp.stack([(x + x*x)/G, F/x, jnp.ones_like(x), jnp.exp(w)/(1 + x)])
    return lam, X, math.asinh(math.sqrt(X))


def cplx(q):            # R^4 -> C^2
    return jnp.array([q[0] + 1j*q[1], q[2] + 1j*q[3]])


def real(z):
    return jnp.array([z[0].real, z[0].imag, z[1].real, z[1].imag])


def bergman(q):
    z = cplx(q); r2 = jnp.real(jnp.vdot(z, z)); A = 1/(1 - r2); B = A*A
    E = jnp.eye(4)
    V = jax.vmap(cplx)(E)                         # basis vectors as complex 2-vectors
    H = A*(V @ jnp.conj(V).T) + B*jnp.outer(V @ jnp.conj(z), jnp.conj(V @ jnp.conj(z)))
    return jnp.real(H)


def frames0(z):
    """Unnormalised cell frame at z (cell centred at 0): radial, j z, k z, i z."""
    z1, z2 = z[0], z[1]
    return [z, jnp.array([-jnp.conj(z2), jnp.conj(z1)]),
            jnp.array([-1j*jnp.conj(z2), 1j*jnp.conj(z1)]), 1j*z]


def phi(a, z):
    """Ball involution swapping 0 and a (a = (alpha,0), alpha real)."""
    al = a[0].real; s = jnp.sqrt(1 - al*al)
    den = 1 - z[0]*al
    return jnp.array([(al - z[0])/den, -s*z[1]/den])


def build(lam, rho):
    def h_cell0(q, gB):
        """h of a cell centred at 0, evaluated at real point q, returned in ball coords."""
        z = cplx(q); r = jnp.arctanh(jnp.sqrt(jnp.real(jnp.vdot(z, z))))
        L = jnp.where(r < rho, lam(jnp.minimum(r, rho)) - 1.0, 0.0)
        H = jnp.zeros((4, 4))
        for s, v in enumerate(frames0(z)):
            vr = real(v); vr = vr/jnp.sqrt(vr @ gB @ vr)
            co = gB @ vr
            H = H + L[s]*jnp.outer(co, co)
        return H

    def h1(q):
        return h_cell0(q, bergman(q))

    def h2(q, a, th):
        # pull back: p = phi_a(q) ; cell coordinates p' = e^{-i th} p ; h2 = (phi_a o L_th)^* h_cell0
        f = lambda qq: real(jnp.exp(-1j*th)*phi(a, cplx(qq)))
        p = f(q); Jm = jax.jacfwd(f)(q)
        return Jm.T @ h_cell0(p, bergman(p)) @ Jm
    return h1, h2


def ricci(metric):
    def Gam_lower(q):
        dg = jax.jacfwd(metric)(q)                 # dg[a,b,c] = d_c g_ab
        # Gamma_{l,ij} = 1/2 (d_i g_jl + d_j g_il - d_l g_ij)
        return 0.5*(jnp.einsum('jli->lij', dg) + jnp.einsum('ilj->lij', dg) - jnp.einsum('ijl->lij', dg))

    def Gam(q):
        return jnp.einsum('kl,lij->kij', jnp.linalg.inv(metric(q)), Gam_lower(q))

    def Ric(q):
        G = Gam(q); dG = jax.jacfwd(Gam)(q)        # dG[k,i,j,m] = d_m Gamma^k_ij
        return (jnp.einsum('kijk->ij', dG) - jnp.einsum('kikj->ij', dG)
                + jnp.einsum('kkl,lij->ij', G, G) - jnp.einsum('kjl,lik->ij', G, G))
    return Ric


def density(metric):
    Ric = ricci(metric)
    def f(q):
        g = metric(q); gi = jnp.linalg.inv(g); E = Ric(q) + 6*g
        return jnp.trace(gi @ E @ gi @ E)*jnp.sqrt(jnp.linalg.det(g)), E, jnp.linalg.eigvalsh(g)
    return f


def lens_r2(q, d):
    zq = q[:, 0] + 1j*q[:, 1]; z2q = q[:, 2] + 1j*q[:, 3]
    al = math.tanh(d); s = math.sqrt(1 - al*al); den = 1 - zq*al
    p1 = (al - zq)/den; p2 = -s*z2q/den
    return np.arctanh(np.sqrt(np.abs(p1)**2 + np.abs(p2)**2))


def cap_angle(rho, d, w, n=400000):
    """Max polar angle (about the axis to the second centre) of lens points; CH is not
    constant curvature, so this is found numerically and enlarged by 10 percent."""
    rng = np.random.default_rng(1)
    r = rho - w + w*rng.random(n); psi = np.pi*rng.random(n)
    v = rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    u = np.concatenate([np.cos(psi)[:, None], np.sin(psi)[:, None]*v], 1)
    q = np.tanh(r)[:, None]*u
    ind = lens_r2(q, d) < rho
    return float(min(np.pi, 1.1*psi[ind].max()))


def run(rec, ws, ths, nlog2, seed=0):
    lam, X, rho = make_profile(rec)
    h1, h2 = build(lam, rho)
    out = []
    for w in ws:
        d = 2*rho - w; a = jnp.array([math.tanh(d) + 0j, 0j])
        for th in ths:
            m1 = lambda q: bergman(q) + h1(q)
            m2 = lambda q: bergman(q) + h2(q, a, th)
            mt = lambda q: bergman(q) + h1(q) + h2(q, a, th)
            f1, f2, ft = density(m1), density(m2), density(mt)

            def pt(q):
                d1, E1, _ = f1(q); d2, E2, _ = f2(q); dt, Et, ev = ft(q)
                gB = bergman(q); gi = jnp.linalg.inv(gB)
                quad = 2*jnp.trace(gi @ E1 @ gi @ E2)*jnp.sqrt(jnp.linalg.det(gB))
                return jnp.array([dt - d1 - d2, quad, d1, d2, jnp.min(ev)])
            ptv = jax.jit(jax.vmap(pt))
            # sample cell-1 polar coords: r in [rho-w, rho], cap angle psi around axis e1
            # cap bound from hyperbolic law of cosines with r1 >= rho - w, r2 <= rho
            r_lo = rho - w
            psimax = cap_angle(rho, d, w)
            sob = qmc.Sobol(d=4, scramble=True, seed=seed)
            U = sob.random_base2(nlog2)
            r = r_lo + w*U[:, 0]; psi = psimax*U[:, 1]
            cz = 2*U[:, 2] - 1; az = 2*np.pi*U[:, 3]; sz = np.sqrt(1 - cz*cz)
            v = np.stack([sz*np.cos(az), sz*np.sin(az), cz], 1)          # S^2 in (Im z1, Re z2, Im z2)
            u = np.stack([np.cos(psi), np.sin(psi)*v[:, 0], np.sin(psi)*v[:, 1], np.sin(psi)*v[:, 2]], 1)
            # ball point and Lebesgue jacobian of (r, psi, S^2) -> R^4
            t = np.tanh(r); q = t[:, None]*u
            jac = t**3*(1 - t*t)*np.sin(psi)**2          # d|q| = sech^2 dr ; dOmega3 = sin^2 psi dpsi dOmega2
            vol = w*psimax*4*np.pi
            # lens indicator: r2 < rho
            zq = q[:, 0] + 1j*q[:, 1]; z2q = q[:, 2] + 1j*q[:, 3]
            al = math.tanh(d); s = math.sqrt(1 - al*al); den = 1 - zq*al
            p1 = (al - zq)/den; p2 = -s*z2q/den
            r2 = np.arctanh(np.sqrt(np.abs(p1)**2 + np.abs(p2)**2))
            ind = (r2 < rho)
            t0 = time.time(); res = []
            Q = jnp.array(q[ind]); B = 4096
            for i in range(0, Q.shape[0], B):
                res.append(np.asarray(ptv(Q[i:i+B])))
            res = np.concatenate(res) if res else np.zeros((0, 5))
            wt = (jac[ind]*vol/len(q))[:, None]
            tot = (res[:, :4]*wt).sum(0)/(8*np.pi**2)
            se = (res[:, :4]*wt).std(0)*math.sqrt(len(q))/(8*np.pi**2)/math.sqrt(len(q))
            rec_out = dict(w=w, theta=th, d=d, rho=rho, n=int(len(q)), n_lens=int(ind.sum()),
                           psimax=psimax, max_psi_used=float(psi[ind].max()) if ind.any() else 0.0,
                           dJ=float(tot[0]), quad=float(tot[1]), J1_lens=float(tot[2]), J2_lens=float(tot[3]),
                           mc_se_naive=[float(x) for x in se[:2]],
                           min_eig=float(res[:, 4].min()) if len(res) else None, sec=time.time()-t0)
            print(json.dumps(rec_out), flush=True); out.append(rec_out)
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('record')
    ap.add_argument('--w', default='0.1'); ap.add_argument('--theta', default='0')
    ap.add_argument('--n', type=int, default=16); ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--out')
    a = ap.parse_args()
    rec = json.loads(Path(a.record).read_text())
    ws = [float(s) for s in a.w.split(',')]; ths = [float(s) for s in a.theta.split(',')]
    out = run(rec, ws, ths, a.n, a.seed)
    if a.out: Path(a.out).write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    main()
