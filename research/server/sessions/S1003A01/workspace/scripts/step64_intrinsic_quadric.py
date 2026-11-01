"""Step 64c: express the level-6 quadrics at a second-order torsion zero in the intrinsic second-jet coordinates.

Structure (derived by hand, checked here): the admissible second torsion jets are exactly
    f2(z) = delta(zbar) z + Q(zbar, zbar),   delta in (C^2)^* antilinear functional (4 real), Q in S^2 (C^2)^* (x) C^2 (12 real)
(16 real dims).  For a J-complex zero surface tangent to {z2=0}:
    delta_1 = 0, Q_11 = 0  (T vanishes on C to 2nd order),   (Q_12)_2 = 0  (cone along C),
and the restricted W3+ has linear part  b12(z1) = delta_2 z1 + 2 (Q_12)_1 zbar1:
winding = sign(|delta_2|^2 - 4|(Q_12)_1|^2).

Input: data/step64/level6_lam{lam}_s{seed}.npz.  Output: data/step64/intrinsic_lam{lam}_s{seed}.json
"""
import os, sys, json, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "..", "data", "step64")

def monos2():
    L = []
    for a in itertools.product(range(3), repeat=4):
        if sum(a) == 2: L.append(a)
    return L

def main(lam, seed):
    d = np.load(os.path.join(OUT, f"level6_lam{lam}_s{seed}.npz"))
    Fz, Qind, K3 = d["Fz"], d["Qind"], d["K3"]
    # monomial order used by Poly for degree 2 (same generator as step53.monos restricted to degree 2)
    mon2 = monos2()
    k = Fz.shape[1]
    # complex sample points: evaluate f2 at random x, fit complex coefficients
    # real quadratic a(x) = sum_c coef[l,c] x^mon_c ; complexify target (a0+i a1, a2+i a3), source z1=x0+i x1, z2=x2+i x3
    rng = np.random.default_rng(0)
    # basis of complex monomials in z, zbar (degree 2): 10 monomials
    def cmonos(z):
        z1, z2 = z; b1, b2 = np.conj(z1), np.conj(z2)
        return np.array([z1*z1, z1*z2, z2*z2, z1*b1, z1*b2, z2*b1, z2*b2, b1*b1, b1*b2, b2*b2])
    names = ["z1z1", "z1z2", "z2z2", "z1b1", "z1b2", "z2b1", "z2b2", "b1b1", "b1b2", "b2b2"]
    pts = rng.standard_normal((40, 4))
    Mc = np.array([cmonos((p[0]+1j*p[1], p[2]+1j*p[3])) for p in pts])   # (40,10)
    Mr = np.array([[np.prod(p**np.array(m)) for m in mon2] for p in pts])  # (40,10)
    coefs = np.zeros((k, 2, 10), complex); fit_err = 0.0
    for j in range(k):
        cf = Fz[:, j].reshape(4, 10)
        vals = Mr @ cf.T                     # (40,4) real values a_l
        cv = vals[:, 0] + 1j*vals[:, 1], vals[:, 2] + 1j*vals[:, 3]
        for t in range(2):
            sol, *_ = np.linalg.lstsq(Mc, cv[t], rcond=None); coefs[j, t] = sol
            fit_err = max(fit_err, float(np.abs(Mc @ sol - cv[t]).max()))
    # check structure: holomorphic-holomorphic part zero; z_a zbar_b part = delta_b z_a
    hol = np.abs(coefs[:, :, 0:3]).max()
    # delta_b: coefficient of z_a zbar_b in component a
    d1 = coefs[:, 0, 3]; d2 = coefs[:, 0, 4]
    struct_err = max(np.abs(coefs[:, 1, 5] - d1).max(), np.abs(coefs[:, 1, 6] - d2).max(),
                     np.abs(coefs[:, 0, 5]).max(), np.abs(coefs[:, 0, 6]).max(), np.abs(coefs[:, 1, 3]).max(), np.abs(coefs[:, 1, 4]).max())
    # Q: f2 antiholomorphic part sum Q_ab^t zbar_a zbar_b : b1b1 -> Q11, b1b2 -> 2 Q12, b2b2 -> Q22
    Q11 = coefs[:, :, 7]; Q12 = coefs[:, :, 8]/2; Q22 = coefs[:, :, 9]
    # real coordinate matrix: y -> (delta1, delta2, Q11^1,Q11^2, Q12^1,Q12^2, Q22^1,Q22^2) complex (8) -> 16 real
    Cmat = np.stack([d1, d2, Q11[:, 0], Q11[:, 1], Q12[:, 0], Q12[:, 1], Q22[:, 0], Q22[:, 1]], 1)  # (k,8)
    Rmat = np.concatenate([Cmat.real, Cmat.imag], 1).T    # (16,k)  w = Rmat y
    rk = np.linalg.matrix_rank(Rmat, 1e-9)
    # quadrics as functions of w: need Q(y)=w^T G w + (terms in ker Rmat).  Restrict y = pinv(Rmat) w + n, n in ker
    U, s, Vt = np.linalg.svd(Rmat); r = int((s > 1e-9*s[0]).sum()); Kn = Vt[r:].T
    Pinv = np.linalg.pinv(Rmat)
    G = np.einsum('qab,ai,bj->qij', Qind, Pinv, Pinv)
    cross = np.einsum('qab,ai,bj->qij', Qind, Pinv, Kn); nn = np.einsum('qab,ai,bj->qij', Qind, Kn, Kn)
    # independent quadrics on w
    Gs = 0.5*(G + G.transpose(0, 2, 1)); Gf = Gs.reshape(Gs.shape[0], -1)
    Ug, sg, Vg = np.linalg.svd(Gf, full_matrices=False); rg = int((sg > 1e-7*sg[0]).sum())
    Gind = Vg[:rg].reshape(rg, 16, 16)
    out = {"lam": lam, "seed": seed, "fit_err": fit_err, "holomorphic_part_max": float(hol), "structure_err": float(struct_err),
           "rank_w_map": int(rk), "dim_ker_w": int(Kn.shape[1]),
           "quadric_cross_w_ker_max": float(np.abs(cross).max()), "quadric_ker_ker_max": float(np.abs(nn).max()),
           "n_quadrics_in_w": rg, "sv_quadrics_w": sg[:10].tolist()}
    labels = ["d1", "d2", "Q11_1", "Q11_2", "Q12_1", "Q12_2", "Q22_1", "Q22_2"]
    labels = [l+"_re" for l in labels] + [l+"_im" for l in labels]
    out["labels"] = labels
    out["quadrics_w"] = [np.round(Gi/np.abs(Gi).max(), 8).tolist() for Gi in Gind]
    # Test the U(2)-invariant candidate: a|delta|^2 + b|Q|^2_F (+ irreducible pieces).  Fit G-span membership.
    def herm(wvec):  # helpers
        return wvec
    def quad_from(fun):
        M = np.zeros((16, 16))
        E = np.eye(16)
        for i in range(16):
            for j in range(16):
                M[i, j] = 0.25*(fun(E[i]+E[j]) - fun(E[i]-E[j]))
        return M
    def unpack(w):
        c = w[:8] + 1j*w[8:]
        dl = c[0:2]; Q = np.zeros((2, 2, 2), complex)
        Q[0, 0] = c[2:4]; Q[0, 1] = Q[1, 0] = c[4:6]; Q[1, 1] = c[6:8]
        return dl, Q
    def nd(w): dl, Q = unpack(w); return float(np.vdot(dl, dl).real)
    def nQ(w): dl, Q = unpack(w); return float(np.vdot(Q, Q).real)          # sum_{ab t} |Q_ab^t|^2
    def Pv(Q):   # equivariant epsilon contraction P_a = Q^1_{a2} - Q^2_{a1}  (Q[a,b,t] = Q^t_ab)
        return np.array([Q[0, 1, 0] - Q[0, 0, 1], Q[1, 1, 0] - Q[1, 0, 1]])
    def nTr(w):
        dl, Q = unpack(w); tr = Pv(Q); return float(np.vdot(tr, tr).real)
    def mix(w):
        dl, Q = unpack(w); tr = Pv(Q); return float(np.real(np.dot(tr, dl)))
    def mix2(w):
        dl, Q = unpack(w); tr = Pv(Q); return float(np.real(np.vdot(tr, dl)))
    def mix3(w):
        dl, Q = unpack(w); tr = Pv(Q); return float(np.imag(np.dot(tr, dl)))
    def mix4(w):
        dl, Q = unpack(w); tr = Pv(Q); return float(np.imag(np.vdot(tr, dl)))
    basis = {"|delta|^2": quad_from(nd), "|Q|^2": quad_from(nQ), "|P|^2": quad_from(nTr),
             "Re tr.delta": quad_from(mix), "Re <tr,delta>": quad_from(mix2), "Im tr.delta": quad_from(mix3), "Im <tr,delta>": quad_from(mix4)}
    Bm = np.array([v.ravel() for v in basis.values()]).T          # (256, nb)
    fits = []
    for Gi in Gind:
        Gi = 0.5*(Gi + Gi.T)
        cfit, *_ = np.linalg.lstsq(Bm, Gi.ravel(), rcond=None)
        resid = float(np.linalg.norm(Bm @ cfit - Gi.ravel())/np.linalg.norm(Gi))
        sc = cfit[0] if abs(cfit[0]) > 1e-12 else 1.0
        fits.append({"coeffs_over_delta": dict(zip(basis.keys(), (cfit/sc).round(10).tolist())), "rel_resid": resid})
    out["invariant_fits"] = fits
    print(json.dumps({k_: v for k_, v in out.items() if k_ != "quadrics_w"}, indent=1))
    json.dump(out, open(os.path.join(OUT, f"intrinsic_lam{lam}_s{seed}.json"), "w"), indent=1)

if __name__ == "__main__":
    main(float(sys.argv[1]), int(sys.argv[2]))
