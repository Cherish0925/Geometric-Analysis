"""Sampled Hamilton--Jacobi subsolution program for diagonal perpendicular CH cells (Step 17).

Goal: find a state function S(a,u) (scale invariant) with
    H_S = D0 S + W^{-1} sum_i a_i^2 S_{u_i}^2 <= 0     on sampled states,
    S = 0 on the exact CH curve (u1=u3=0, a1=a3, u2=3x, a2/a1=sqrt(1+x)),
maximizing -S(bolt), bolt state (a3/a1=0, a2/a1=1, u=(0,0,-1)).
If H_S<=0 held on ALL states visited by a competitor, P/(8pi^2) >= -S(bolt) (Step-17 note).
Here the inequality is imposed only on sampled states (the witness trajectories and a random
tube of radius sigma around them, plus transverse CH/N perturbations), so the optimum is an
UPPER bound on what this basis can certify on that tube -- exploratory, not a theorem.

The constraint is convex (second-order cone) in the linear coefficients theta of S.
Basis:  S = -c Phi + sum_k theta_k b_k(q,w,y) m_k(u1,u3),
   q=a3/a1, w=tanh(log(a2/a1)), y=u2/sqrt(4+u2^2), m in {1,u1,u3,u1^2,u1u3,u3^2}.
Usage: python hj_socp.py --sigma 0.05 --deg 4 --out OUT.json RECORD.json ...
"""
import argparse, json, sys, itertools, glob
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
import cvxpy as cp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from joint_dual_calibration import load_profile

MONOS = ['1', 'u1', 'u3', 'u1^2', 'u1u3', 'u3^2']


def make_basis(deg):
    exps = [e for e in itertools.product(range(deg+1), repeat=3) if sum(e) <= deg]
    def feats(a, u):
        q = a[2]/a[0]; w = jnp.tanh(jnp.log(a[1]/a[0])); y = u[1]/jnp.sqrt(4+u[1]**2)
        mono = jnp.array([1., u[0], u[2], u[0]**2, u[0]*u[2], u[2]**2])
        b = jnp.array([q**i*w**j*y**k for (i, j, k) in exps])
        Phi = u[0]**2+u[2]**2+u[0]*u[1]*u[2]
        return jnp.concatenate([jnp.array([-Phi]), jnp.outer(mono, b).ravel()])
    names = ['-Phi']+[f'{m}*q^{i}w^{j}y^{k}' for m in MONOS for (i, j, k) in exps]
    return feats, names


def drift(a, u):
    a1, a2, a3 = a
    gam = jnp.array([(a2**2+a3**2-a1**2)/(a2*a3), (a3**2+a1**2-a2**2)/(a3*a1), (a1**2+a2**2-a3**2)/(a1*a2)])
    H = jnp.array([u[0]+u[1]*u[2]/2, u[1]+u[2]*u[0]/2, u[2]+u[0]*u[1]/2])
    lam = jnp.array([a2*a3/a1, a3*a1/a2, a1*a2/a3])
    return u+gam, 2*H/lam


def sample_states(records, sigma, K, seed, tcut, n):
    rng = np.random.default_rng(seed)
    A, U, tags = [], [], []
    for p in records:
        rec, v, t, dtdv, W, z, e, ec, u, H, bs, a = load_profile(p, n)
        m = (t > 1e-4) & (t <= tcut)
        a_, u_ = a[m], u[m]
        A.append(a_); U.append(u_); tags += ['traj']*len(a_)
        if sigma > 0:
            q = a_[:, 2]/a_[:, 0]; damp = np.minimum(1., q/0.3)[:, None]
            for _ in range(K):
                du = sigma*rng.standard_normal(u_.shape)*damp*np.maximum(1., np.abs(u_))
                da = np.exp(sigma*rng.standard_normal(a_.shape)*damp*0.5)
                A.append(a_*da); U.append(u_+du); tags += ['tube']*len(a_)
    # exact CH curve and transverse perturbations (Kahler manifold N neighbourhood)
    x = np.geomspace(1e-3, 30., 300)
    ach = np.column_stack([np.sqrt(x), np.sqrt(x*(1+x)), np.sqrt(x)])
    uch = np.column_stack([0*x, 3*x, 0*x])
    A.append(ach); U.append(uch); tags += ['CH']*len(x)
    if sigma > 0:
        for _ in range(K):
            du = np.zeros_like(uch); du[:, [0, 2]] = sigma*rng.standard_normal((len(x), 2))
            du[:, 1] = sigma*rng.standard_normal(len(x))*np.maximum(1, uch[:, 1])
            A.append(ach*np.exp(0.5*sigma*rng.standard_normal(ach.shape))); U.append(uch+du); tags += ['CHtube']*len(x)
    return np.vstack(A), np.vstack(U), np.array(tags), ach, uch


def build(feats, A, U):
    def one(a, u):
        Fa = jax.jacfwd(feats, argnums=0)(a, u); Fu = jax.jacfwd(feats, argnums=1)(a, u)
        ad, ud = drift(a, u)
        g = Fa@ad+Fu@ud           # D0 of each basis function
        Wv = a[0]*a[1]*a[2]
        M = (a[:, None]*Fu.T)/jnp.sqrt(Wv)   # 3 x nb
        return g, M
    g, M = jax.vmap(one)(jnp.asarray(A), jnp.asarray(U))
    return np.asarray(g), np.asarray(M)


def solve(g, M, Fch, Fbolt, bound=1e3):
    nb = g.shape[1]
    # row scaling (positive per-state factor; feasibility unchanged)
    s = 1/np.maximum(1e-12, np.abs(g).max(1)+np.abs(M).reshape(len(M), -1).max(1)**2)
    G = g*s[:, None]; Ms = M*np.sqrt(s)[:, None, None]
    # column scaling theta = D phi
    colnorm = np.sqrt((G**2).sum(0)+(Ms**2).sum((0, 1))+(Fch**2).sum(0))+1e-12
    D = 1/colnorm
    G = G*D; Ms = Ms*D; Fc = Fch*D; Fb = Fbolt*D
    # drop numerically null CH rows via SVD of Fc
    Uc, sc, Vc = np.linalg.svd(Fc, full_matrices=False)
    Fc = (Vc[sc > 1e-10*sc.max()])
    ph = cp.Variable(nb)
    lhs = cp.sum(cp.square(cp.hstack([(Ms[:, i, :]@ph)[:, None] for i in range(3)])), axis=1)
    cons = [lhs+G@ph <= 0, Fc@ph == 0, cp.norm(ph, 'inf') <= bound]
    prob = cp.Problem(cp.Maximize(-Fb@ph), cons)
    for solver in ('CLARABEL', 'SCS'):
        try:
            if solver == 'SCS': prob.solve(solver='SCS', max_iters=400000, eps=1e-8)
            else: prob.solve(solver='CLARABEL', max_iter=500)
            break
        except Exception as ex:
            print('solver', solver, 'failed', ex)
    th = None if ph.value is None else D*ph.value
    return prob.value, th, prob.status


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('records', nargs='+')
    ap.add_argument('--sigma', type=float, default=0.); ap.add_argument('--K', type=int, default=4)
    ap.add_argument('--deg', type=int, default=3); ap.add_argument('--tcut', type=float, default=3.0)
    ap.add_argument('--n', type=int, default=1201); ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--out')
    a = ap.parse_args()
    feats, names = make_basis(a.deg)
    A, U, tags, ach, uch = sample_states(a.records, a.sigma, a.K, a.seed, a.tcut, a.n)
    g, M = build(feats, A, U)
    Fch = np.asarray(jax.vmap(feats)(jnp.asarray(ach), jnp.asarray(uch)))
    eps = 1e-9
    Fbolt = np.asarray(feats(jnp.array([1., 1., eps]), jnp.array([0., 0., -1.])))
    val, th, status = solve(g, M, Fch, Fbolt)
    out = dict(sigma=a.sigma, K=a.K, deg=a.deg, tcut=a.tcut, nsamples=int(len(A)), nbasis=len(names),
               status=status, certified_on_samples=val, records=a.records)
    if th is not None:
        out['c_Phi'] = float(th[0])
        Hs = g@th+np.sum((M@th)**2, axis=1)
        out['max_H_on_samples'] = float(Hs.max())
        big = np.argsort(-np.abs(th))[:12]
        out['largest_coeffs'] = {names[i]: float(th[i]) for i in big}
        out['theta'] = th.tolist(); out['names'] = names
    print(json.dumps({k: v for k, v in out.items() if k not in ('theta', 'names')}, indent=1))
    if a.out: Path(a.out).write_text(json.dumps(out)+'\n')

if __name__ == '__main__': main()
