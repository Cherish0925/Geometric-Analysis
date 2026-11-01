"""Step 64: second torsion jets at an exceptional point of a torsion-zero surface, and the winding of W3+|C.

Setting. (M,g,Omega) Einstein almost-Kahler, Ric=lam g, T=nabla Omega.  p is a point with T(p)=0 and DT(p)=0
(second-order torsion zero).  In first-order normal coordinates with g=delta+O(x^2), Omega=Omega0+O(x^2),
Omega0=e01+e23 (J e0=e1, J e2=e3), the first torsion jet vanishes iff Mvec(z2)=0, and the torsion
    a_l(x) = (1/4) <T_l(x), phi>   (nabla_l Omega = a_l phi - (Ja)_l psi)
has quadratic Taylor part a2(x) that is LINEAR in the 3-jets z3 of (g,Omega).

Truncation D=5.  Row levels: E1 deg d, E2 deg d-1, E3 deg d-2 are 'level d'.  At a base point
(z2,z4) solving levels 2,4 with Mvec=0 and z3=z5=0:
  level 3:  A3 z3 = 0                    (linear, lam-independent)
  level 5:  A5 z5 + B(z2) z3 = 0          (bilinear in z2,z3; solvable iff Pi_coker(A5) B z3 = 0)
So the admissible z3 for this 2-jet form an exact linear space; f2 = F z3 is gauge invariant.

Zero-surface conditions at p for a surface C tangent to P=span(e0,e1) (J-complex) with T|C=0:
  (Z1) a2(x)=0 for x in P                                    (T vanishes on C to second order)
  (Z2) cone theorem at every point x of C:  b22(x)=0, i.e. D a(x)(N) lies in the line TC   (Step 62/63)
Then the restricted W3+ (proportional to b12) has linear part  w(x) = d_{e2} a2(x) projected to TC, a real 2x2
map P->TC; winding = sign det in the J-orientations (e0, J e0) of both.

Outputs data/step64/winding_lam{lam}_s{seed}.json
Usage: python step64_exceptional_winding.py lam seed
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

def main(lam, seed, D=5):
    S = Z.setup(D); P = S["P"]; n = S["n"]; nvar = S["nvar"]
    idx = np.where(P.deg >= 2)[0]
    coldeg = np.tile(P.deg[idx], 16)
    keep = S["keep"]; rt = S["rowtype"][keep]; rd = S["rowdeg"][keep]
    level = np.where(rt == 1, rd, np.where(rt == 2, rd + 1, rd + 2))
    sysf = jax.jit(lambda z: S["system"](z, lam)[jnp.array(keep)])
    # torsion polynomial a_l(x), (Ja)_l(x)
    def torsion_poly(z):
        g, w = S["unpack"](z)
        h = g - jnp.eye(4)[:, :, None]*(jnp.arange(P.M) == 0)[None, None, :]
        gi = jnp.eye(4)[:, :, None]*(jnp.arange(P.M) == 0)[None, None, :]; term = gi
        for _ in range(1, D//2 + 1):
            term = -P.mul(term, h, 'ijp,jkp->ikp'); gi = gi + term
        dg = jnp.stack([P.d(g, k) for k in range(4)], 0)
        Gl = 0.5*(jnp.einsum('jlkp->ljkp', dg) + jnp.einsum('kljp->ljkp', dg) - dg)
        Gam = P.mul(gi, Gl, 'ilp,ljkp->ijkp')          # Gam[i,j,k] = Gamma^i_{jk}
        dw = jnp.stack([P.d(w, k) for k in range(4)], 0)  # dw[k,i,j] = d_k w_ij
        T = (dw - P.mul(Gam, w, 'mkip,mjp->kijp') - P.mul(Gam, w, 'mkjp,imp->kijp'))
        a = 0.25*jnp.einsum('kijp,ij->kp', T, jnp.array(Z.PHI))
        Ja = -0.25*jnp.einsum('kijp,ij->kp', T, jnp.array(Z.PSI))
        aom = 0.25*jnp.einsum('kijp,ij->kp', T, jnp.array(Z.W0))
        return a, Ja, aom
    d2 = [c for c in range(P.M) if P.deg[c] == 2]
    mon2 = [P.L[c] for c in d2]
    def a2vec(z):
        a, Ja, aom = torsion_poly(z)
        return jnp.concatenate([a[:, jnp.array(d2)].ravel(), Ja[:, jnp.array(d2)].ravel(), aom[:, jnp.array(d2)].ravel()])
    # ---- base point: levels 2 and 4 with Mvec = 0, z3 = z5 = 0
    rng = np.random.default_rng(seed)
    free = np.where((coldeg == 2) | (coldeg == 4))[0]
    rows24 = np.where((level == 2) | (level == 4))[0]
    def R24(y):
        z = jnp.zeros(nvar).at[jnp.array(free)].set(y)
        return jnp.concatenate([sysf(z)[jnp.array(rows24)], Z.Mvec(S, z)])
    R24j = jax.jit(R24); J24j = jax.jit(jax.jacfwd(R24))
    y = rng.standard_normal(len(free))*0.3
    y, f, hist, gn, _, _ = Z.lm(R24j, J24j, y, 200, tol=1e-28)
    z0 = np.zeros(nvar); z0[free] = np.asarray(y)
    full_res = float(np.linalg.norm(np.asarray(sysf(jnp.array(z0)))))
    cv = S["curvature"](jnp.array(z0))
    # ---- linearization
    J = np.asarray(jax.jacfwd(sysf)(jnp.array(z0)))
    c3 = np.where(coldeg == 3)[0]; c5 = np.where(coldeg == 5)[0]
    r3 = np.where(level == 3)[0]; r5 = np.where(level == 5)[0]
    leak3 = float(np.abs(J[np.ix_(r3, np.setdiff1d(np.arange(nvar), c3))]).max())
    leak5 = float(np.abs(J[np.ix_(r5, np.setdiff1d(np.arange(nvar), np.concatenate([c3, c5])))]).max())
    A3 = J[np.ix_(r3, c3)]; A5 = J[np.ix_(r5, c5)]; B5 = J[np.ix_(r5, c3)]
    U, s5, _ = np.linalg.svd(A5); rk5 = int((s5 > 1e-9*s5[0]).sum()); Ucok = U[:, rk5:]
    C5 = Ucok.T @ B5
    K3 = nullspace(A3); K35 = nullspace(np.vstack([A3, C5]))
    Fz = np.asarray(jax.jacfwd(a2vec)(jnp.array(z0)))
    leakF = float(np.abs(Fz[:, np.setdiff1d(np.arange(nvar), c3)]).max())
    F3 = Fz[:, c3]
    na = 4*len(d2)
    def image(Kb):
        M = F3 @ Kb
        U_, s_, _ = np.linalg.svd(M, full_matrices=False); r = int((s_ > 1e-9*s_[0]).sum()) if len(s_) else 0
        return U_[:, :r]
    L3 = image(K3); L35 = image(K35)
    res = {"lam": lam, "seed": seed, "base_res2": f, "base_full_res": full_res, "s": float(cv["s"]),
           "Wp_spec": np.linalg.eigvalsh(np.asarray(cv["Wp"])).tolist(), "|W-|": float(np.linalg.norm(np.asarray(cv["Wm"]))),
           "leak3": leak3, "leak5": leak5, "leakF": leakF, "dim_z3": len(c3), "rank_A3": int(len(c3) - K3.shape[1]),
           "coker5": int(Ucok.shape[1]), "rank_C5_on_K3": int(np.linalg.matrix_rank(C5 @ K3, 1e-8)),
           "dim_f2_level3": int(L3.shape[1]), "dim_f2_level5": int(L35.shape[1])}
    # sanity: Omega-component of torsion vanishes; Ja = Mj a
    Om = L35[2*na:]; res["omega_comp_max"] = float(np.abs(Om).max()) if Om.size else 0.0
    Av = L35[:na].reshape(4, len(d2), -1); JAv = L35[na:2*na].reshape(4, len(d2), -1)
    Xa = Av.reshape(4, -1); Xj = JAv.reshape(4, -1)
    Mj = Xj @ np.linalg.pinv(Xa); res["Ja_equals_Mj_a_err"] = float(np.abs(Mj @ Xa - Xj).max())
    res["Mj"] = np.round(Mj, 10).tolist(); res["JM"] = Z.JM.tolist()
    # coefficient access: a2 coefficient of monomial x_i x_j in component l, as function of basis vector
    def coef(Lb, l, i, j):
        e = [0, 0, 0, 0]; e[i] += 1; e[j] += 1; c = mon2.index(tuple(e))
        return Lb[l*len(d2) + c]
    # Df(x)(e_k) at x in P: d_k a2(x) = sum_i coef(x_i x_k)*(1+delta_ik) x_i ; for k normal only i in {0,1}
    def dA(Lb, l, k, i):   # coefficient of x_i in d_k a_l restricted to P (i in 0,1; k in 2,3)
        return coef(Lb, l, i, k)
    Lb = L35
    rowsZ1 = [coef(Lb, l, i, j) for l in range(4) for (i, j) in [(0, 0), (0, 1), (1, 1)]]
    KZ1 = nullspace(np.array(rowsZ1)); LZ1 = Lb @ KZ1
    # complex-linear part along P must be zero (automatic?)  and image in TC (cone): components l=2,3 of d_k a(x)
    rowsZ2 = [dA(LZ1, l, k, i) for l in (2, 3) for k in (2, 3) for i in (0, 1)]
    KZ2 = nullspace(np.array(rowsZ2)); LZ = LZ1 @ KZ2
    res["dim_after_Z1"] = int(LZ1.shape[1]); res["rank_Z2_on_Z1"] = int(np.linalg.matrix_rank(np.array(rowsZ2), 1e-9))
    res["dim_after_Z2"] = int(LZ.shape[1])
    # check antilinearity of D a(x)|N on LZ1: d_{e3} a = -Mj d_{e2} a
    if LZ1.shape[1]:
        anti = []
        for i in (0, 1):
            d2v = np.array([dA(LZ1, l, 2, i) for l in range(4)]); d3v = np.array([dA(LZ1, l, 3, i) for l in range(4)])
            anti.append(float(np.abs(d3v + Mj @ d2v).max())); anti.append(float(np.abs(d3v - Mj @ d2v).max()))
        res["antilinear_check(+,-)"] = anti
    # winding: W[m,i] = coefficient of x_i in d_{e2} a_m(x), m in {0,1} (TC components)
    if LZ.shape[1]:
        Wb = np.array([[dA(LZ, m, 2, i) for i in (0, 1)] for m in (0, 1)])  # (2,2,dim)
        # target orientation (e0, Mj e0) restricted to TC
        tor = np.sign(Mj[1, 0]) if abs(Mj[1, 0]) > 0.5 else 0.0
        res["target_orientation_sign"] = float(tor)
        dets = []
        for _ in range(20000):
            cvec = rng.standard_normal(LZ.shape[1]); W = np.einsum('mic,c->mi', Wb, cvec)
            nr = np.linalg.norm(W)
            if nr > 0: dets.append(tor*np.linalg.det(W)/nr**2)
        dets = np.array(dets)
        res["det_min"] = float(dets.min()); res["det_max"] = float(dets.max())
        res["frac_neg"] = float((dets < 0).mean())
        # quadratic form of det on the space
        dimz = LZ.shape[1]; Q = np.zeros((dimz, dimz))
        for a_ in range(dimz):
            for b_ in range(dimz):
                Wa = Wb[:, :, a_]; Wbb = Wb[:, :, b_]
                Q[a_, b_] = 0.5*(Wa[0, 0]*Wbb[1, 1] + Wbb[0, 0]*Wa[1, 1] - Wa[0, 1]*Wbb[1, 0] - Wbb[0, 1]*Wa[1, 0])
        res["det_form_eigs"] = np.linalg.eigvalsh(tor*Q).tolist()
        # complex decomposition of the 2x2 real map: alpha (complex-linear) and beta (antilinear) parts
        Jt = np.array([[0, -1], [1, 0]])*tor if tor != 0 else np.array([[0, -1], [1, 0]])
        Js = np.array([[0, -1], [1, 0]])
        al = [np.linalg.norm((Wb[:, :, c] - Jt @ Wb[:, :, c] @ Js)/2) for c in range(dimz)]
        be = [np.linalg.norm((Wb[:, :, c] + Jt @ Wb[:, :, c] @ Js)/2) for c in range(dimz)]
        res["basis_alpha_norms"] = al; res["basis_beta_norms"] = be
        # rank of alpha-map and beta-map from the admissible space
        Amap = np.array([((Wb[:, :, c] - Jt @ Wb[:, :, c] @ Js)/2).ravel() for c in range(dimz)]).T
        Bmap = np.array([((Wb[:, :, c] + Jt @ Wb[:, :, c] @ Js)/2).ravel() for c in range(dimz)]).T
        res["rank_alpha_map"] = int(np.linalg.matrix_rank(Amap, 1e-9)); res["rank_beta_map"] = int(np.linalg.matrix_rank(Bmap, 1e-9))
        res["rank_alpha_beta_joint"] = int(np.linalg.matrix_rank(np.vstack([Amap, Bmap]), 1e-9))
    # same analysis without the level-5 condition (level-3 only), for comparison
    rowsZ1b = [coef(L3, l, i, j) for l in range(4) for (i, j) in [(0, 0), (0, 1), (1, 1)]]
    LZ1b = L3 @ nullspace(np.array(rowsZ1b))
    rowsZ2b = [dA(LZ1b, l, k, i) for l in (2, 3) for k in (2, 3) for i in (0, 1)]
    LZb = LZ1b @ nullspace(np.array(rowsZ2b))
    res["level3_only_dims"] = [int(LZ1b.shape[1]), int(LZb.shape[1])]
    if LZb.shape[1]:
        Wb3 = np.array([[dA(LZb, m, 2, i) for i in (0, 1)] for m in (0, 1)])
        tor = res.get("target_orientation_sign", 1.0) or 1.0
        dd = []
        for _ in range(5000):
            cvec = rng.standard_normal(LZb.shape[1]); W = np.einsum('mic,c->mi', Wb3, cvec); nr = np.linalg.norm(W)
            if nr > 0: dd.append(tor*np.linalg.det(W)/nr**2)
        dd = np.array(dd); res["level3_only_det_range"] = [float(dd.min()), float(dd.max())]
    np.savez(os.path.join(OUT, f"spaces_lam{lam}_s{seed}.npz"), L3=L3, L35=L35, LZ1=LZ1, LZ=LZ, mon2=np.array(mon2), z0=z0)
    print(json.dumps(res, indent=1))
    json.dump(res, open(os.path.join(OUT, f"winding_lam{lam}_s{seed}.json"), "w"), indent=1)

if __name__ == "__main__":
    main(float(sys.argv[1]), int(sys.argv[2]))
