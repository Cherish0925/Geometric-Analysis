"""Step 62: finite-order compatibility of Einstein almost-Kahler jets at a torsion (Nijenhuis) zero.

Representation (independent of A02's Darboux gauge): unknown Taylor jets of (g, omega) in coordinates with
  g = delta + O(|x|^2)  (first-order normal coordinates; achievable by a diffeomorphism),
  omega = omega0 + O(|x|^2)  (omega0 = e01+e23; the vanishing 1-jet is exactly the torsion zero nabla omega(0)=0,
                              because Gamma(0)=0 in this gauge).
Equations (degree-D truncation, all equations of these orders and every unknown they contain):
  E1: omega^T g^{-1} omega = g   to degree D;  E2: d omega = 0 to degree D-1;  E3: Ric = lam g to degree D-2.
First torsion jet: N[k,l,.] = <nabla_k nabla_l omega(0), (phi, psi)>,  phi=e02-e13, psi=e03+e12.
With nabla_l omega = a_l phi - (Ja)_l psi and |phi|^2=2, the array called Mmat below is the form inner product
N^phi[k,l] = <nabla_k nabla_l omega, phi> = 2 nabla_k a_l (the einsum 0.5*NN:PHI is already the 2-form inner product).
The local index of a nondegenerate zero is sign det(Mmat) (orientations from omega0^2).

Modes:
  lin D              : linear analysis of the order-0 system; dimension of the admissible first torsion jets L,
                       complex-linear / antilinear split, eta and W3 maps, sector bases -> data/step62/linear.npz
  gh D eps           : exact Ricci-flat Gibbons-Hawking AK zero control (w+iv = 1+eps(x+iy)^2): residual + its jet
  solve D lam SECTOR seed nst [scale] : solve the truncated system with prescribed first torsion jet
                       SECTOR in {kahler, c, A, S, mixed, generic, gh}
Outputs JSON in workspace/data/step62/.
"""
import os, sys, json, time, itertools
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from step53_ak_einstein_jets import Poly

LINDIR = os.path.join(HERE, "..", "data", "step62")
OUT = os.environ.get("STEP62_OUT", LINDIR); os.makedirs(OUT, exist_ok=True)
TRI = [(i, j) for i in range(4) for j in range(i, 4)]
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
def two_form(entries):
    m = np.zeros((4, 4))
    for (i, j), v in entries.items(): m[i, j] = v; m[j, i] = -v
    return m
W0 = two_form({(0, 1): 1, (2, 3): 1})
PHI = two_form({(0, 2): 1, (1, 3): -1})
PSI = two_form({(0, 3): 1, (1, 2): 1})
r2 = 1/np.sqrt(2)
SD = np.array([[r2, 0, 0, 0, 0, r2], [0, r2, 0, 0, -r2, 0], [0, 0, r2, r2, 0, 0]])
ASD = np.array([[r2, 0, 0, 0, 0, -r2], [0, r2, 0, 0, r2, 0], [0, 0, r2, -r2, 0, 0]])
JM = W0.T  # J e_a = sum_b Omega_ab e_b  -> column-vector matrix J[b,a]=Omega[a,b]

def setup(D):
    P = Poly(D)
    mask = P.deg >= 2; idx = np.where(mask)[0]; n = len(idx)
    nvar = 16*n
    d2 = [c for c, a in enumerate(P.L) if sum(a) == 2]
    T2 = np.zeros((P.M, 4, 4))
    for c in d2:
        a = P.L[c]; ks = [k for k in range(4) for _ in range(a[k])]; k, l = ks
        fac = 2.0 if k == l else 1.0
        T2[c, k, l] = fac; T2[c, l, k] = fac
    T2 = jnp.array(T2)
    def unpack(z):
        gz = z[:10*n].reshape(10, n); wz = z[10*n:].reshape(6, n)
        g = jnp.zeros((4, 4, P.M)); g = g.at[jnp.arange(4), jnp.arange(4), 0].set(1.0)
        for c, (i, j) in enumerate(TRI):
            g = g.at[i, j, idx].add(gz[c])
            if i != j: g = g.at[j, i, idx].add(gz[c])
        w = jnp.zeros((4, 4, P.M)); w = w.at[:, :, 0].set(jnp.array(W0))
        for c, (i, j) in enumerate(PAIRS):
            w = w.at[i, j, idx].add(wz[c]); w = w.at[j, i, idx].add(-wz[c])
        return g, w
    degm = lambda dmax: jnp.array(P.deg <= dmax)
    def system(z, lam):
        g, w = unpack(z)
        h = g - jnp.eye(4)[:, :, None]*(jnp.arange(P.M) == 0)[None, None, :]
        gi = jnp.eye(4)[:, :, None]*(jnp.arange(P.M) == 0)[None, None, :]
        term = gi
        for _ in range(1, D//2 + 1):
            term = -P.mul(term, h, 'ijp,jkp->ikp'); gi = gi + term
        dg = jnp.stack([P.d(g, k) for k in range(4)], 0)
        Gl = 0.5*(jnp.einsum('jlkp->ljkp', dg) + jnp.einsum('kljp->ljkp', dg) - dg)
        Gam = P.mul(gi, Gl, 'ilp,ljkp->ijkp')
        dGam = jnp.stack([P.d(Gam, k) for k in range(4)], 0)
        Ric = (jnp.einsum('iijkp->jkp', dGam) - jnp.einsum('kiijp->jkp', dGam)
               + P.mul(jnp.einsum('iipq->pq', Gam), Gam, 'pq,pjkq->jkq')
               - P.mul(Gam, Gam, 'ikpq,pijq->jkq'))
        E3 = (Ric - lam*g)*degm(D-2)[None, None, :]
        E1 = P.mul(P.mul(jnp.transpose(w, (1, 0, 2)), gi, 'ijp,jkp->ikp'), w, 'ijp,jkp->ikp') - g
        dw = jnp.stack([P.d(w, k) for k in range(4)], 0)
        E2 = jnp.stack([dw[i, j, k] + dw[j, k, i] + dw[k, i, j]
                        for (i, j, k) in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]])*degm(D-1)[None, :]
        tri = np.array(TRI)
        return jnp.concatenate([E1[tri[:, 0], tri[:, 1]].ravel(), E2.ravel(), E3[tri[:, 0], tri[:, 1]].ravel()])
    # row bookkeeping: degree of each equation coefficient
    rowdeg = np.concatenate([np.tile(P.deg, 10), np.tile(P.deg, 4), np.tile(P.deg, 10)])
    rowtype = np.concatenate([np.full(10*P.M, 1), np.full(4*P.M, 2), np.full(10*P.M, 3)])
    keep = np.where(((rowtype == 1) & (rowdeg <= D)) | ((rowtype == 2) & (rowdeg <= D-1)) | ((rowtype == 3) & (rowdeg <= D-2)))[0]
    def jets2(z):
        g, w = unpack(z)
        Hg = jnp.einsum('ijc,ckl->ijkl', g, T2)   # Hg[i,j,k,l] = d_k d_l g_ij(0)
        Hw = jnp.einsum('ijc,ckl->ijkl', w, T2)
        return Hg, Hw
    def torsion_jet(z):
        Hg, Hw = jets2(z)
        dGam = 0.5*(jnp.einsum('mikl->kmli', Hg) + jnp.einsum('mlki->kmli', Hg) - jnp.einsum('likm->kmli', Hg))
        w0 = jnp.array(W0)
        NN = (jnp.einsum('ijkl->klij', Hw) - jnp.einsum('kmli,mj->klij', dGam, w0)
              - jnp.einsum('kmlj,im->klij', dGam, w0))
        Nphi = 0.5*jnp.einsum('klij,ij->kl', NN, jnp.array(PHI))
        Npsi = 0.5*jnp.einsum('klij,ij->kl', NN, jnp.array(PSI))
        Nom = 0.5*jnp.einsum('klij,ij->kl', NN, w0)
        return Nphi, Npsi, Nom, NN
    def curvature(z):
        Hg, _ = jets2(z)
        H = Hg
        R = 0.5*(jnp.einsum('adbc->abcd', H) + jnp.einsum('bcad->abcd', H) - jnp.einsum('acbd->abcd', H) - jnp.einsum('bdac->abcd', H))
        Ric = jnp.einsum('abad->bd', R); s = jnp.trace(Ric); dl = jnp.eye(4)
        W = (R - 0.5*(jnp.einsum('ac,bd->abcd', dl, Ric) - jnp.einsum('ad,bc->abcd', dl, Ric)
                      - jnp.einsum('bc,ad->abcd', dl, Ric) + jnp.einsum('bd,ac->abcd', dl, Ric))
             + s/6*(jnp.einsum('ac,bd->abcd', dl, dl) - jnp.einsum('ad,bc->abcd', dl, dl)))
        Mw = jnp.stack([jnp.stack([W[i, j, k, l] for (k, l) in PAIRS]) for (i, j) in PAIRS])
        Wp = jnp.array(SD) @ Mw @ jnp.array(SD).T; Wm = jnp.array(ASD) @ Mw @ jnp.array(ASD).T
        eta = Wp[0, 1:]; V = Wp[1:, 1:]; W3 = jnp.array([(V[0, 0] - V[1, 1])/2, V[0, 1]])
        return {"s": s, "Wp": Wp, "Wm": Wm, "eta": eta, "W3": W3}
    return dict(P=P, n=n, nvar=nvar, unpack=unpack, system=system, keep=keep, rowdeg=rowdeg, rowtype=rowtype,
                torsion_jet=torsion_jet, curvature=curvature)

def Mvec(S, z):
    Nphi, Npsi, _, _ = S["torsion_jet"](z)
    return jnp.concatenate([Nphi.ravel(), Npsi.ravel()])

def linear_analysis(D=4):
    S = setup(D); nvar = S["nvar"]; n = S["n"]; P = S["P"]
    z0 = jnp.zeros(nvar)
    Jsys = np.asarray(jax.jacfwd(lambda z: S["system"](z, 0.0))(z0))[S["keep"]]
    rows0 = np.where(np.isin(S["keep"], np.where(((S["rowtype"] == 1) & (S["rowdeg"] == 2)) | ((S["rowtype"] == 2) & (S["rowdeg"] == 1))
                                                 | ((S["rowtype"] == 3) & (S["rowdeg"] == 0)))[0]))[0]
    deg2 = np.array([P.deg[c] == 2 for c in np.where(P.deg >= 2)[0]])
    cols = np.where(np.tile(deg2, 16))[0]
    A0 = Jsys[rows0][:, cols]
    # rows of order-0 equations should involve only degree-2 unknowns
    other = np.setdiff1d(np.arange(nvar), cols)
    leak = float(np.abs(Jsys[rows0][:, other]).max())
    U, sv, Vt = np.linalg.svd(A0); rk = int((sv > 1e-10*sv[0]).sum()); K = Vt[rk:].T
    Mlin = np.asarray(jax.jacfwd(lambda z: Mvec(S, z))(z0))[:, cols]
    curvlin = np.asarray(jax.jacfwd(lambda z: jnp.concatenate([S["curvature"](z)["eta"], S["curvature"](z)["W3"]]))(z0))[:, cols]
    MK = Mlin @ K; CK = curvlin @ K
    rM = np.linalg.matrix_rank(MK, 1e-9); rMC = np.linalg.matrix_rank(np.vstack([MK, CK]), 1e-9)
    Um, sm, Vm = np.linalg.svd(MK); Lb = Um[:, :rM]          # orthonormal basis of L in R^32
    # eta,W3 as function of M on L: C = G M
    pre = np.linalg.pinv(MK)
    G = CK @ pre
    # complex structure split of Mmat (F = Mmat^T as map v -> nabla_v a)
    def split(m32):
        Mm = m32[:16].reshape(4, 4); F = Mm.T
        Fp = (F - JM @ F @ JM)/2; Fm = (F + JM @ F @ JM)/2
        return Fp, Fm
    Pp = np.array([split(Lb[:, i])[0].ravel() for i in range(rM)]).T
    Pm = np.array([split(Lb[:, i])[1].ravel() for i in range(rM)]).T
    dlin = np.linalg.matrix_rank(Pp, 1e-9); danti = np.linalg.matrix_rank(Pm, 1e-9)
    # subspace of L with antilinear-only F: kernel of Pp
    _, sp_, Vp = np.linalg.svd(Pp); kP = Vp[int((sp_ > 1e-9).sum()):].T; Lanti = Lb @ kP
    _, sm_, Vm_ = np.linalg.svd(Pm); kM = Vm_[int((sm_ > 1e-9).sum()):].T; Llin = Lb @ kM
    # within Lanti: kernel of eta,W3
    Ca = G @ Lanti; _, sc, Vc = np.linalg.svd(Ca); rc = int((sc > 1e-9).sum())
    Ssec = Lanti @ Vc[rc:].T; Asec = Lanti @ Vc[:rc].T
    out = {"D": D, "order0_rows": int(len(rows0)), "deg2_unknowns": int(len(cols)), "leak": leak, "rank_A0": rk,
           "dim_kernel": int(K.shape[1]), "dim_L": int(rM), "rank_M_plus_curv": int(rMC),
           "dim_Llin": int(Llin.shape[1]), "dim_Lanti": int(Lanti.shape[1]), "rank_lin_proj": int(dlin), "rank_anti_proj": int(danti),
           "dim_S": int(Ssec.shape[1]), "dim_A": int(Asec.shape[1]),
           "eta_W3_on_Llin_rank": int(np.linalg.matrix_rank(G @ Llin, 1e-9)) if Llin.shape[1] else 0,
           "Nomega_max_on_K": float(np.abs(np.asarray(jax.jacfwd(lambda z: S['torsion_jet'](z)[2].ravel())(z0))[:, cols] @ K).max())}
    print(json.dumps(out, indent=1), flush=True)
    np.savez(os.path.join(OUT, "linear.npz"), Lb=Lb, Llin=Llin, Lanti=Lanti, S=Ssec, A=Asec, G=G)
    json.dump(out, open(os.path.join(OUT, "linear.json"), "w"), indent=1)
    return out

def detF(m32):
    return float(np.linalg.det(m32[:16].reshape(4, 4)))

def gh_jets(D, eps):
    import sympy as sp
    X = sp.symbols('x0:4'); t = sp.symbols('t')
    x, y = X[0], X[1]
    w = 1 + eps*(x**2 - y**2); v = 2*eps*x*y
    # coordinates (x, y, tau, z) = (x0, x1, x2, x3);  g = w(dx^2+dy^2+dz^2) + w^-1 (dtau + v dz)^2
    G = sp.zeros(4, 4)
    G[0, 0] = w; G[1, 1] = w; G[3, 3] = w + v**2/w; G[2, 2] = 1/w; G[2, 3] = G[3, 2] = v/w
    Wf = sp.zeros(4, 4); Wf[0, 1] = w; Wf[1, 0] = -w; Wf[2, 3] = 1; Wf[3, 2] = -1
    S = setup(D); P = S["P"]; idx = np.where(P.deg >= 2)[0]
    def coeffs(expr):
        ser = sp.expand(sp.series(expr.subs({X[i]: t*X[i] for i in range(4)}), t, 0, D+1).removeO().subs(t, 1))
        c = np.zeros(P.M)
        if ser == 0: return c
        pol = sp.Poly(ser, *X)
        for mon, val in pol.terms():
            if sum(mon) <= D: c[P.idx[tuple(mon)]] = float(val)
        return c
    gz = np.zeros((10, len(idx))); wz = np.zeros((6, len(idx)))
    for c, (i, j) in enumerate(TRI):
        cc = coeffs(G[i, j] - (1 if i == j else 0)); gz[c] = cc[idx]
    for c, (i, j) in enumerate(PAIRS):
        cc = coeffs(Wf[i, j] - W0[i, j]); wz[c] = cc[idx]
    return S, np.concatenate([gz.ravel(), wz.ravel()])

def lm(R, Jf, z, iters, tol=1e-27):
    mu = 1e-3; r = np.asarray(R(z)); f = float(r @ r); hist = [f]
    for it in range(iters):
        Jm = np.asarray(Jf(z))
        U, s, Vt = np.linalg.svd(Jm, full_matrices=False)
        step = -Vt.T @ ((s/(s**2 + mu))*(U.T @ r))
        zn = z + step; rn = np.asarray(R(zn)); fn = float(rn @ rn)
        if fn < f: z, r, f = zn, rn, fn; mu = max(mu/5, 1e-15)
        else: mu *= 10
        hist.append(f)
        if f < tol or mu > 1e12: break
    Jm = np.asarray(Jf(z)); grad = Jm.T @ r
    return z, f, hist, float(np.linalg.norm(grad)), Jm, r

def target(sector, rng, lin, scale):
    Lb, Llin, Lanti, Ss, As = lin["Lb"], lin["Llin"], lin["Lanti"], lin["S"], lin["A"]
    rv = lambda B: B @ rng.standard_normal(B.shape[1])
    if sector == "kahler": m = np.zeros(32)
    elif sector == "c": m = rv(Llin)
    elif sector == "A": m = rv(As)
    elif sector == "S": m = rv(Ss)
    elif sector == "generic": m = rv(Lb)
    elif sector == "mixed":   # c + t S with det < 0
        for _ in range(2000):
            c = rv(Llin); c /= np.linalg.norm(c); s_ = rv(Ss); s_ /= np.linalg.norm(s_)
            ts = np.linspace(0.05, 6, 400); ds = [detF(c + tt*s_) for tt in ts]
            neg = [tt for tt, d in zip(ts, ds) if d < 0]
            if neg:
                tt = neg[len(neg)//2]; m = c + tt*s_; break
    elif sector in ("AS", "cA", "cone"):  # points on the predicted cone |m_A|^2 = 4|m_c|^2 + |m_S|^2
        xc = rng.standard_normal(2) if sector != "AS" else np.zeros(2)
        xs = rng.standard_normal(6) if sector != "cA" else np.zeros(6)
        xa = rng.standard_normal(2); xa = xa/np.linalg.norm(xa)*np.sqrt(4*xc @ xc + xs @ xs)
        m = Llin @ xc + As @ xa + Ss @ xs
    else: raise ValueError(sector)
    nrm = np.linalg.norm(m)
    return m/nrm*scale if nrm > 0 else m

def solve(D, lam, sector, seed, nst, scale=1.0, iters=120):
    S = setup(D); nvar = S["nvar"]; keep = jnp.array(S["keep"])
    rng = np.random.default_rng(seed)
    if sector == "gh":
        _, zgh = gh_jets(D, 0.5); mt = np.asarray(Mvec(S, jnp.array(zgh)))
    else:
        lin = dict(np.load(os.path.join(OUT, "linear.npz"))); mt = target(sector, rng, lin, scale)
    mtj = jnp.array(mt)
    Rf = jax.jit(lambda z: jnp.concatenate([S["system"](z, lam)[keep], Mvec(S, z) - mtj]))
    Jf = jax.jit(jax.jacfwd(lambda z: jnp.concatenate([S["system"](z, lam)[keep], Mvec(S, z) - mtj])))
    res = {"D": D, "lam": lam, "sector": sector, "seed": seed, "scale": scale, "nvar": nvar,
           "neq": int(len(S["keep"]) + 32), "target_det": detF(mt), "target_norm": float(np.linalg.norm(mt)), "runs": []}
    t0 = time.time()
    for st in range(nst):
        z = rng.standard_normal(nvar)*0.3
        z, f, hist, gn, Jm, r = lm(Rf, Jf, z, iters)
        sv = np.linalg.svd(Jm, compute_uv=False); rank = int((sv > 1e-9*sv[0]).sum())
        cv = S["curvature"](jnp.array(z)); mz = np.asarray(Mvec(S, jnp.array(z)))
        sysr = np.asarray(S["system"](jnp.array(z), lam))[S["keep"]]
        # residual by equation type/degree
        bydeg = {}
        for k_, ri in zip(S["keep"], sysr):
            key = f"E{S['rowtype'][k_]}_d{S['rowdeg'][k_]}"; bydeg[key] = bydeg.get(key, 0.0) + float(ri**2)
        run = {"res2": f, "iters": len(hist)-1, "grad_norm": gn, "rank": rank, "Merr": float(np.linalg.norm(mz - mt)),
               "det": detF(mz), "s": float(cv["s"]), "eta": np.asarray(cv["eta"]).tolist(), "W3": np.asarray(cv["W3"]).tolist(),
               "|W-|": float(np.linalg.norm(np.asarray(cv["Wm"]))), "Wp_spec": np.linalg.eigvalsh(np.asarray(cv["Wp"])).tolist(),
               "res_by_block": {k: v for k, v in bydeg.items() if v > 1e-30}, "hist_tail": hist[-4:], "time": time.time()-t0}
        res["runs"].append(run); print(json.dumps(run), flush=True)
    fn = os.path.join(OUT, f"solve_D{D}_l{lam}_{sector}_s{seed}.json")
    json.dump(res, open(fn, "w"), indent=1)
    return res

def solve_cont(D, lam, sector, seed, nsteps=10, scale=1.0, iters=60):
    """Homotopy continuation in the first torsion jet: target t*M, t from 0 (Kahler germ) to 1, warm starts.
    A genuine obstruction quadratic in M would give a minimal residual growing like t^4 (res^2)."""
    S = setup(D); nvar = S["nvar"]; keep = jnp.array(S["keep"])
    rng = np.random.default_rng(seed)
    if sector == "gh":
        _, zgh = gh_jets(D, 0.5); mt = np.asarray(Mvec(S, jnp.array(zgh)))*scale
    else:
        lin = dict(np.load(os.path.join(LINDIR, "linear.npz"))); mt = target(sector, rng, lin, scale)
    tpar = jnp.zeros(())
    def F(z, t): return jnp.concatenate([S["system"](z, lam)[keep], Mvec(S, z) - t*jnp.array(mt)])
    Fj = jax.jit(F); Jj = jax.jit(jax.jacfwd(F))
    res = {"D": D, "lam": lam, "sector": sector, "seed": seed, "scale": scale, "nvar": nvar,
           "neq": int(len(S["keep"]) + 32), "target_det": detF(mt), "target_norm": float(np.linalg.norm(mt)),
           "target": mt.tolist(), "path": []}
    z = rng.standard_normal(nvar)*0.1; t0 = time.time()
    for t in np.concatenate([[0.0], np.linspace(1.0/nsteps, 1.0, nsteps)]):
        z, f, hist, gn, Jm, r = lm(lambda zz: Fj(zz, t), lambda zz: Jj(zz, t), z, iters)
        sysr = np.asarray(S["system"](jnp.array(z), lam))[S["keep"]]
        bydeg = {}
        for k_, ri in zip(S["keep"], sysr):
            key = f"E{S['rowtype'][k_]}_d{S['rowdeg'][k_]}"; bydeg[key] = bydeg.get(key, 0.0) + float(ri**2)
        cv = S["curvature"](jnp.array(z)); mz = np.asarray(Mvec(S, jnp.array(z)))
        rec = {"t": float(t), "res2": f, "iters": len(hist)-1, "grad_norm": gn, "det": detF(mz),
               "Merr": float(np.linalg.norm(mz - t*mt)), "eta": np.asarray(cv["eta"]).tolist(), "W3": np.asarray(cv["W3"]).tolist(),
               "|W-|": float(np.linalg.norm(np.asarray(cv["Wm"]))), "Wp_spec": np.linalg.eigvalsh(np.asarray(cv["Wp"])).tolist(),
               "worst_blocks": dict(sorted(bydeg.items(), key=lambda kv: -kv[1])[:3]), "time": time.time()-t0}
        res["path"].append(rec); print(json.dumps(rec), flush=True)
    np.save(os.path.join(OUT, f"cont_D{D}_l{lam}_{sector}_s{seed}_z.npy"), np.asarray(z))
    json.dump(res, open(os.path.join(OUT, f"cont_D{D}_l{lam}_{sector}_s{seed}.json"), "w"), indent=1)
    return res

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "lin": linear_analysis(int(sys.argv[2]))
    elif mode == "gh":
        D = int(sys.argv[2]); eps = float(sys.argv[3])
        S, z = gh_jets(D, eps)
        r = np.asarray(S["system"](jnp.array(z), 0.0))[S["keep"]]
        m = np.asarray(Mvec(S, jnp.array(z))); _, _, Nom, NN = S["torsion_jet"](jnp.array(z))
        out = {"D": D, "eps": eps, "res_norm": float(np.linalg.norm(r)), "res_max": float(np.abs(r).max()),
               "Mmat": m[:16].reshape(4, 4).tolist(), "Npsi": m[16:].reshape(4, 4).tolist(), "det": detF(m),
               "Nomega_max": float(np.abs(np.asarray(Nom)).max())}
        lin = np.load(os.path.join(OUT, "linear.npz")) if os.path.exists(os.path.join(OUT, "linear.npz")) else None
        if lin is not None:
            Lb = lin["Lb"]; out["dist_to_L"] = float(np.linalg.norm(m - Lb @ (Lb.T @ m)))
        print(json.dumps(out, indent=1)); json.dump(out, open(os.path.join(OUT, f"gh_D{D}.json"), "w"), indent=1)
    elif mode == "solve":
        D, lam, sector, seed, nst = int(sys.argv[2]), float(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
        scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
        solve(D, lam, sector, seed, nst, scale)
    elif mode == "cont":
        D, lam, sector, seed = int(sys.argv[2]), float(sys.argv[3]), sys.argv[4], int(sys.argv[5])
        nsteps = int(sys.argv[6]) if len(sys.argv) > 6 else 10
        scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
        solve_cont(D, lam, sector, seed, nsteps, scale)
