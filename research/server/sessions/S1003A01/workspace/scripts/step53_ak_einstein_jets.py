"""Step 53b: formal-jet feasibility of the almost-Kahler Einstein system in dimension 4.

Question (Problem 4 entrance): at a point where the Nijenhuis tensor is nonzero (q(0)=|nabla omega|^2(0)>0), do
truncated Taylor jets of (g, omega) exist solving
    E1:  omega^T g^{-1} omega = g          (omega is a g-orthogonal almost-complex 2-form, |omega|^2 = 2)
    E2:  d omega = 0                        (almost Kahler)
    E3:  Ric(g) = lam g                     (Einstein)
to the orders forced by a degree-D truncation (E1 to degree D, E2 to D-1, E3 to D-2)?
If, for lam<0, the truncated system becomes infeasible with q(0)>0 at some D while the controls stay feasible,
there is a finite-order local obstruction (local Goldberg); if it stays feasible, the obstruction (if any) is
global or of higher order.  Numerical evidence only; any obstruction must then be extracted exactly.

Controls:  lam<0, q0=0 (Kahler-Einstein jets exist);  lam=0, q0>0 (Nurowski-Przanowski-Tod Ricci-flat strictly
almost-Kahler local metrics exist).
Gauge: g = delta + O(|x|^2) (normal coordinates to first order), omega(0) = e01+e23.  Remaining gauge freedom is
left in the (minimum-norm Gauss-Newton) solve.

Usage: python step53_ak_einstein_jets.py D lam q0 nstarts seed [tag]
Output: workspace/data/step53_jets/akjets_<tag>.json
"""
import os, sys, json, time, itertools
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step53_jets"); os.makedirs(OUT, exist_ok=True)

def monos(D):
    L = []
    for d in range(D+1):
        for a in itertools.product(range(d+1), repeat=4):
            if sum(a) == d: L.append(a)
    return L

class Poly:
    def __init__(self, D):
        self.D = D; self.L = monos(D); self.M = len(self.L)
        self.idx = {a: i for i, a in enumerate(self.L)}
        self.deg = np.array([sum(a) for a in self.L])
        I, J, K = [], [], []
        for i, a in enumerate(self.L):
            for j, b in enumerate(self.L):
                if self.deg[i] + self.deg[j] <= D:
                    I.append(i); J.append(j); K.append(self.idx[tuple(x+y for x, y in zip(a, b))])
        self.I, self.J, self.K = map(jnp.array, (I, J, K))
        self.dm = []
        for k in range(4):
            Dm = np.zeros((self.M, self.M))
            for i, a in enumerate(self.L):
                if a[k] > 0:
                    b = list(a); b[k] -= 1; Dm[self.idx[tuple(b)], i] = a[k]
            self.dm.append(jnp.array(Dm))
    def mul(self, a, b, spec):  # spec like 'ijp,jkp->ikp' on coefficient-pair axis p
        pa = a[..., self.I]; pb = b[..., self.J]
        c = jnp.einsum(spec, pa, pb)
        return jax.ops.segment_sum(jnp.moveaxis(c, -1, 0), self.K, self.M).transpose(
            tuple(range(1, c.ndim)) + (0,))
    def d(self, a, k):
        return a @ self.dm[k].T

def setup(D):
    P = Poly(D)
    # unknown layout: g upper-triangular comps, degrees >= 2 ; omega 6 comps, degrees >= 1
    gmask = P.deg >= 2; wmask = P.deg >= 1
    ng = int(gmask.sum()); nw = int(wmask.sum())
    TRI = [(i, j) for i in range(4) for j in range(i, 4)]
    PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    w0 = np.zeros((4, 4)); w0[0, 1] = 1; w0[1, 0] = -1; w0[2, 3] = 1; w0[3, 2] = -1
    gidx = np.where(gmask)[0]; widx = np.where(wmask)[0]
    nvar = 10*ng + 6*nw
    def unpack(z):
        gz = z[:10*ng].reshape(10, ng); wz = z[10*ng:].reshape(6, nw)
        g = jnp.zeros((4, 4, P.M)); g = g.at[jnp.arange(4), jnp.arange(4), 0].set(1.0)
        for c, (i, j) in enumerate(TRI):
            g = g.at[i, j, gidx].add(gz[c])
            if i != j: g = g.at[j, i, gidx].add(gz[c])
        w = jnp.zeros((4, 4, P.M)); w = w.at[:, :, 0].set(jnp.array(w0))
        for c, (i, j) in enumerate(PAIRS):
            w = w.at[i, j, widx].add(wz[c]); w = w.at[j, i, widx].add(-wz[c])
        return g, w
    degm = lambda dmax: jnp.array(P.deg <= dmax)
    def residual(z, lam, q0, wq):
        g, w = unpack(z)
        h = g - jnp.eye(4)[:, :, None]*(jnp.arange(P.M) == 0)[None, None, :]
        gi = jnp.eye(4)[:, :, None]*(jnp.arange(P.M) == 0)[None, None, :]
        term = gi
        for n in range(1, D//2 + 1):
            term = -P.mul(term, h, 'ijp,jkp->ikp'); gi = gi + term
        dg = jnp.stack([P.d(g, k) for k in range(4)], 0)        # dg[k,i,j]
        # lowered Christoffel G_{l jk} = 1/2(d_j g_lk + d_k g_lj - d_l g_jk)
        Gl = 0.5*(jnp.einsum('jlkp->ljkp', dg) + jnp.einsum('kljp->ljkp', dg) - dg)
        Gam = P.mul(gi, Gl, 'ilp,ljkp->ijkp')                   # Gamma^i_{jk}
        dGam = jnp.stack([P.d(Gam, k) for k in range(4)], 0)    # dGam[m,i,j,k]
        Ric = (jnp.einsum('iijkp->jkp', dGam) - jnp.einsum('kiijp->jkp', dGam)
               + P.mul(jnp.einsum('iipq->pq', Gam), Gam, 'pq,pjkq->jkq')
               - P.mul(Gam, Gam, 'ikpq,pijq->jkq'))
        E3 = (Ric - lam*g)*degm(D-2)[None, None, :]
        E1 = (P.mul(P.mul(jnp.transpose(w, (1, 0, 2)), gi, 'ijp,jkp->ikp'), w, 'ijp,jkp->ikp') - g)
        dw = jnp.stack([P.d(w, k) for k in range(4)], 0)        # dw[k,i,j] = d_k w_ij
        E2 = []
        for (i, j, k) in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
            E2.append(dw[i, j, k] + dw[j, k, i] + dw[k, i, j])
        E2 = jnp.stack(E2)*degm(D-1)[None, :]
        lin = jnp.array(P.deg == 1)
        q = jnp.sum(jnp.stack([w[i, j]*lin for (i, j) in PAIRS])**2)
        tri = jnp.array([[i, j] for (i, j) in TRI])
        r = jnp.concatenate([E1[tri[:, 0], tri[:, 1]].ravel(), E2.ravel(), E3[tri[:, 0], tri[:, 1]].ravel(),
                             jnp.array([wq*(q - q0)])])
        return r
    return P, unpack, residual, nvar, ng, nw

def solve(residual, nvar, lam, q0, rng, iters=60, wq=1.0, init_scale=0.5):
    z = rng.standard_normal(nvar)*init_scale
    R = jax.jit(lambda z: residual(z, lam, q0, wq))
    Jf = jax.jit(jax.jacfwd(lambda z: residual(z, lam, q0, wq)))
    mu = 1e-3; r = R(z); f = float(r @ r); hist = [f]
    for it in range(iters):
        Jm = np.asarray(Jf(z)); rr = np.asarray(r)
        # Levenberg-Marquardt minimum-norm step
        U, S, Vt = np.linalg.svd(Jm, full_matrices=False)
        step = -Vt.T @ ((S/(S**2 + mu)) * (U.T @ rr))
        zn = z + step; rn = R(zn); fn = float(rn @ rn)
        if fn < f:
            z, r, f = zn, rn, fn; mu = max(mu/5, 1e-15)
        else:
            mu *= 10
        hist.append(f)
        if f < 1e-26: break
    Jm = np.asarray(Jf(z)); S = np.linalg.svd(Jm, compute_uv=False)
    return z, f, hist, S

def exact_test(D):
    """Residual of the exact Kahler-Einstein jet of H^2(-1) x H^2(-1) (lam=-1, q0=0): must vanish."""
    import sympy as sp
    P, unpack, residual, nvar, ng, nw = setup(D)
    X = sp.symbols('x0:4'); t = sp.symbols('t')
    f1 = (1 - (X[0]**2 + X[1]**2)/4)**-2; f2 = (1 - (X[2]**2 + X[3]**2)/4)**-2
    def coeffs(expr):
        ser = sp.expand(sp.series(expr.subs({X[i]: t*X[i] for i in range(4)}), t, 0, D+1).removeO().subs(t, 1))
        pol = sp.Poly(ser, *X); c = np.zeros(P.M)
        for mon, val in pol.terms():
            if sum(mon) <= D: c[P.idx[tuple(mon)]] = float(val)
        return c
    c1, c2 = coeffs(f1), coeffs(f2)
    gmask = P.deg >= 2; wmask = P.deg >= 1
    TRI = [(i, j) for i in range(4) for j in range(i, 4)]
    gz = np.zeros((10, ng)); wz = np.zeros((6, nw))
    gz[TRI.index((0, 0))] = c1[gmask]; gz[TRI.index((1, 1))] = c1[gmask]
    gz[TRI.index((2, 2))] = c2[gmask]; gz[TRI.index((3, 3))] = c2[gmask]
    wz[0] = c1[wmask]; wz[5] = c2[wmask]
    z = np.concatenate([gz.ravel(), wz.ravel()])
    r = np.asarray(residual(jnp.array(z), -1.0, 0.0, 1.0))
    print("exact H2xH2 KE residual norm", np.linalg.norm(r), "max", np.abs(r).max(), flush=True)
    r2 = np.asarray(residual(jnp.array(z), -1.1, 0.0, 1.0))
    print("control wrong lam residual norm", np.linalg.norm(r2), flush=True)

def main():
    if sys.argv[1] == "test":
        exact_test(int(sys.argv[2])); return
    D = int(sys.argv[1]); lam = float(sys.argv[2]); q0 = float(sys.argv[3])
    nst = int(sys.argv[4]); seed = int(sys.argv[5]); tag = sys.argv[6] if len(sys.argv) > 6 else f"D{D}_l{lam}_q{q0}"
    t0 = time.time()
    P, unpack, residual, nvar, ng, nw = setup(D)
    rng = np.random.default_rng(seed)
    out = {"D": D, "lam": lam, "q0": q0, "nvar": nvar, "neq": int(residual(jnp.zeros(nvar), lam, q0, 1.0).shape[0]), "runs": []}
    print("setup", time.time()-t0, out["nvar"], out["neq"], flush=True)
    for s in range(nst):
        z, f, hist, S = solve(residual, nvar, lam, q0, rng)
        rank = int((S > 1e-8*S[0]).sum())
        g, w = unpack(jnp.array(z))
        lin = P.deg == 1
        dw0 = np.asarray(w)[:, :, lin]  # d_k omega_ij(0) (k ordering = monomial order of degree-1 monomials)
        run = {"final_res2": f, "iters": len(hist)-1, "rank": rank, "nvar": nvar, "hist_tail": hist[-5:],
               "smin_nonzero": float(S[rank-1]) if rank > 0 else None, "time": time.time()-t0}
        out["runs"].append(run)
        np.save(os.path.join(OUT, f"akjets_{tag}_z{s}.npy"), np.asarray(z))
        print(s, json.dumps(run), flush=True)
    json.dump(out, open(os.path.join(OUT, f"akjets_{tag}.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
