"""Step 64b: the first NONLINEAR compatibility at a second-order torsion zero (level 6) and the exceptional winding.

At a point p with T(p)=DT(p)=0 (normal-coordinate gauge of step62, D=6):
  level 3:  A3 z3 = 0;     level 5:  A5 z5 + B(z2) z3 = 0  (no extra condition found in step64a)
  level 6:  A6 z6 + B6(z2) z4 + C(z3,z3) + T(z2) = 0
Solvability at level 6 for fixed 2-jet z2: there exist dz4 in ker A4 and z6 with
  A6 z6 + B6(z2) dz4 + C(z3,z3) = 0,
i.e. Pi' C(z3,z3) = 0 with Pi' the projector onto coker[A6 | B6 K4].  These are quadratic forms on the
admissible 3-jets (f2 = second torsion jet, and nabla W^- which f2 does not see).

Exceptional-point question: impose the zero-surface conditions (Z1) a2|_P = 0, (Z2) d_N a2(x) in TC for x in P,
and ask whether the level-6 quadric admits w=W3+|_C linear part of negative (and of positive) winding.
Feasibility by LM on y in the linear space, residuals = [Q_k(y), det W(y) - sigma], sigma = +-1.

Usage: python step64_level6.py lam seed ; output data/step64/level6_lam{lam}_s{seed}.json (+ .npz)
"""
import os, sys, json, time
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import step62_zero_prolong as Z
OUT = os.path.join(HERE, "..", "data", "step64"); os.makedirs(OUT, exist_ok=True)

def nullspace(A, tol=1e-9):
    if A.shape[0] == 0: return np.eye(A.shape[1])
    U, s, Vt = np.linalg.svd(A)
    r = int((s > tol*max(s[0], 1e-300)).sum()) if len(s) else 0
    return Vt[r:].T

def colspace(A, tol=1e-9):
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    r = int((s > tol*s[0]).sum()); return U[:, :r]

def main(lam, seed, D=6):
    t0 = time.time()
    S = Z.setup(D); P = S["P"]; nvar = S["nvar"]
    idx = np.where(P.deg >= 2)[0]; coldeg = np.tile(P.deg[idx], 16)
    keep = S["keep"]; rt = S["rowtype"][keep]; rd = S["rowdeg"][keep]
    level = np.where(rt == 1, rd, np.where(rt == 2, rd + 1, rd + 2))
    sysf = jax.jit(lambda z: S["system"](z, lam)[jnp.array(keep)])
    d2 = [c for c in range(P.M) if P.deg[c] == 2]; mon2 = [P.L[c] for c in d2]
    rng = np.random.default_rng(seed)
    # ---- base: levels 2,4,6 with Mvec=0, z3=z5=0
    # stage 1: (z2,z4) on levels 2,4 + Mvec (nonlinear, small);  stage 2: (z4,z6) affine solve on levels 4,6
    free = np.where((coldeg == 2) | (coldeg == 4))[0]
    rows = np.where((level == 2) | (level == 4))[0]
    def Rb(y):
        z = jnp.zeros(nvar).at[jnp.array(free)].set(y)
        return jnp.concatenate([sysf(z)[jnp.array(rows)], Z.Mvec(S, z)])
    Rbj = jax.jit(Rb); Jbj = jax.jit(jax.jacfwd(Rb))
    y = rng.standard_normal(len(free))*0.3
    y, f, hist, gn, _, _ = Z.lm(Rbj, Jbj, y, 80, tol=1e-28)
    z0 = np.zeros(nvar); z0[free] = np.asarray(y)
    print("stage1", f, len(hist), time.time()-t0, flush=True)
    free2 = np.where((coldeg == 4) | (coldeg == 6))[0]
    rows2 = np.where((level == 4) | (level == 6))[0]
    def R2(y2):
        z = jnp.array(z0).at[jnp.array(free2)].set(y2)
        return sysf(z)[jnp.array(rows2)]
    for _ in range(2):
        y2 = jnp.array(z0[free2]); r2 = np.asarray(R2(y2)); J2 = np.asarray(jax.jacfwd(R2)(y2))
        dy, *_ = np.linalg.lstsq(J2, -r2, rcond=None); z0[free2] = z0[free2] + dy
    f = float(np.sum(np.asarray(sysf(jnp.array(z0)))**2) + np.sum(np.asarray(Z.Mvec(S, jnp.array(z0)))**2))
    base_full = float(np.linalg.norm(np.asarray(sysf(jnp.array(z0)))))
    cv = S["curvature"](jnp.array(z0))
    print("base", f, base_full, time.time()-t0, flush=True)
    J = np.asarray(jax.jacfwd(sysf)(jnp.array(z0)))
    cs = {d: np.where(coldeg == d)[0] for d in range(2, D+1)}
    rl = {d: np.where(level == d)[0] for d in range(2, D+1)}
    A3 = J[np.ix_(rl[3], cs[3])]; A5 = J[np.ix_(rl[5], cs[5])]; B5 = J[np.ix_(rl[5], cs[3])]
    U5, s5, _ = np.linalg.svd(A5); r5 = int((s5 > 1e-9*s5[0]).sum()); C5 = U5[:, r5:].T @ B5
    K3 = nullspace(np.vstack([A3, C5]))            # admissible z3 (incl. gauge)
    A4 = J[np.ix_(rl[4], cs[4])]; K4 = nullspace(A4)
    Y = np.hstack([J[np.ix_(rl[6], cs[6])], J[np.ix_(rl[6], cs[4])] @ K4])
    Yc = colspace(Y); 
    U6, s6, _ = np.linalg.svd(Y, full_matrices=True); r6 = int((s6 > 1e-9*s6[0]).sum()); Pi = U6[:, r6:]
    print("dims K3", K3.shape[1], "coker6", Pi.shape[1], time.time()-t0, flush=True)
    c3 = cs[3]; r6rows = rl[6]
    def lev6(yv):
        z = jnp.array(z0).at[jnp.array(c3)].add(jnp.array(K3) @ yv)
        return jnp.array(Pi).T @ sysf(z)[jnp.array(r6rows)]
    # quadratic forms: lev6(y) = const + Q(y,y)  (const ~ base residual)
    jl = jax.jit(lev6); kk0 = K3.shape[1]
    jlg = jax.jit(jax.jacfwd(lev6))
    lin = np.asarray(jlg(jnp.zeros(kk0)))
    # compute Hessian column by column (k x k might be 168x168)
    print("computing Hessian", kk0, "x", kk0, flush=True)
    Hq = np.zeros((Pi.shape[1], kk0, kk0))
    batch = 20
    for i0 in range(0, kk0, batch):
        e = np.zeros((min(batch, kk0-i0), kk0))
        for jj in range(e.shape[0]): e[jj, i0+jj] = 1.0
        cols = np.asarray(jax.vmap(jlg)(jnp.array(e)))     # (batch, m, k)
        for jj in range(cols.shape[0]):
            Hq[:, i0+jj, :] = (cols[jj] - lin)/2.0
        if i0 % 100 == 0: print("  col", i0, time.time()-t0, flush=True)
    Hq = 0.5*(Hq + Hq.transpose(0, 2, 1))
    print("quad forms", Hq.shape, "linear part max", np.abs(lin).max(), time.time()-t0, flush=True)
    # torsion map f2 = F y
    def tors(z):
        g, w = S["unpack"](z)
        dg = jnp.stack([P.d(g, k) for k in range(4)], 0)
        Gl = 0.5*(jnp.einsum('jlkp->ljkp', dg) + jnp.einsum('kljp->ljkp', dg) - dg)
        dw = jnp.stack([P.d(w, k) for k in range(4)], 0)
        T = dw - jnp.einsum('mkip,mj->kijp', Gl, jnp.array(Z.W0)) - jnp.einsum('mkjp,im->kijp', Gl, jnp.array(Z.W0))
        T = T[..., jnp.array(d2)]
        return 0.25*jnp.einsum('kijp,ij->kp', T, jnp.array(Z.PHI))     # a_l, deg-2 coefficients
    Fz = np.asarray(jax.jacfwd(lambda z: tors(z).ravel())(jnp.zeros(nvar)))[:, c3] @ K3   # (40, k)
    # reduce quadratic forms to an independent set (flatten, rank)
    m, k, _ = Hq.shape
    Qflat = Hq.reshape(m, -1); Uq, sq, Vq = np.linalg.svd(Qflat, full_matrices=False)
    rq = int((sq > 1e-8*sq[0]).sum()); Qind = (Vq[:rq]*1.0).reshape(rq, k, k)
    # quadric restricted to f2: does Q vanish on ker F (pure nabla W^- / gauge) ?
    KF = nullspace(Fz); ImF = colspace(Fz.T)  # ImF: complement directions in y
    res = {"lam": lam, "seed": seed, "base_res2": f, "base_full_res": base_full, "s": float(cv["s"]),
           "|W-|": float(np.linalg.norm(np.asarray(cv["Wm"]))), "Wp_spec": np.linalg.eigvalsh(np.asarray(cv["Wp"])).tolist(),
           "dim_K3": int(k), "rank_F": int(np.linalg.matrix_rank(Fz, 1e-9)), "coker6": int(m), "n_indep_quadrics": rq,
           "quadric_sv_top": sq[:min(12, len(sq))].tolist(), "const_part": float(np.linalg.norm(np.asarray(lev6(jnp.zeros(k))))),
           "linear_part_max": float(np.abs(lin).max())}
    # gauge-null check: Q(u, v) for u in KF (W^- and gauge)
    if KF.shape[1]:
        res["Q_on_kerF_kerF_max"] = float(np.abs(np.einsum('qab,ai,bj->qij', Qind, KF, KF)).max())
        res["Q_on_kerF_ImF_max"] = float(np.abs(np.einsum('qab,ai,bj->qij', Qind, KF, ImF)).max())
    # ---- zero-surface conditions
    def coef(Fm, l, i, j):
        e = [0, 0, 0, 0]; e[i] += 1; e[j] += 1; return Fm[l*len(d2) + mon2.index(tuple(e))]
    Z1 = np.array([coef(Fz, l, i, j) for l in range(4) for (i, j) in [(0, 0), (0, 1), (1, 1)]])
    Z2 = np.array([coef(Fz, l, i, kk) for l in (2, 3) for kk in (2, 3) for i in (0, 1)])
    Ksurf = nullspace(np.vstack([Z1, Z2]))
    res["dim_surface_space"] = int(Ksurf.shape[1])
    Wmap = np.array([[coef(Fz, mm, i, 2) for i in (0, 1)] for mm in (0, 1)])  # (2,2,k): W[m,i]
    Ws = np.einsum('mik,kj->mij', Wmap, Ksurf)
    Qs = np.einsum('qab,ai,bj->qij', Qind, Ksurf, Ksurf)
    # rank of the quadrics on the surface space
    res["n_quadrics_on_surface"] = int(np.linalg.matrix_rank(Qs.reshape(rq, -1), 1e-8))
    np.savez(os.path.join(OUT, f"level6_lam{lam}_s{seed}.npz"), Hq=Hq, Qind=Qind, Fz=Fz, K3=K3, Ksurf=Ksurf, Ws=Ws, Qs=Qs, z0=z0)
    # ---- feasibility for both winding signs
    ks = Ksurf.shape[1]
    Qsj = jnp.array(Qs); Wsj = jnp.array(Ws)
    def Rf(yv, sig):
        Wv = jnp.einsum('mij,j->mi', Wsj, yv)
        return jnp.concatenate([jnp.einsum('qij,i,j->q', Qsj, yv, yv), jnp.array([Wv[0, 0]*Wv[1, 1]-Wv[0, 1]*Wv[1, 0]-sig])])
    feas = {}
    for sig in (-1.0, 1.0):
        Rj = jax.jit(lambda yv: Rf(yv, sig)); Jj = jax.jit(jax.jacfwd(lambda yv: Rf(yv, sig)))
        best = []
        for st in range(12):
            yv = rng.standard_normal(ks)
            yv, fv, h_, g_, _, _ = Z.lm(Rj, Jj, yv, 400, tol=1e-28)
            best.append(fv)
        feas[str(sig)] = sorted(best)[:6]
        print("sigma", sig, sorted(best)[:6], flush=True)
    res["feasibility_res2(sigma)"] = feas
    res["time"] = time.time()-t0
    print(json.dumps(res, indent=1))
    json.dump(res, open(os.path.join(OUT, f"level6_lam{lam}_s{seed}.json"), "w"), indent=1)

if __name__ == "__main__":
    main(float(sys.argv[1]), int(sys.argv[2]))
