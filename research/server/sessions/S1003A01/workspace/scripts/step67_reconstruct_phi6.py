#!/usr/bin/env python3
"""Reconstruct and verify an order-6 Darboux jet from A02's reduced Phi6 system.

This is an independent execution of the saved A02 equations, not a proof of a
convergent Einstein almost-Kahler germ.  For a selected unit cone jet and lambda:
  * solve E_1,...,E_5 affinely for H4,...,H7;
  * reduce the degree-6 residual modulo the H8 image;
  * find a real zero of the complete reduced polynomial system;
  * reconstruct the minimum-norm H8 and evaluate unreduced E_0,...,E_6.
The positive comparison reports the scalar minimum but is not reconstructed.
"""
import argparse, json, os, sys, time
from pathlib import Path
import numpy as np
import torch

HERE = Path(__file__).resolve().parent
A02 = HERE.parents[2] / "S1003A02" / "workspace" / "scripts"
sys.path.insert(0, str(A02))
os.environ.setdefault("STEP79_OUT", "step80")
import step79_general_order6 as G
from step80_lambda_scan import unit_jet
from step80_universal_pi import reduce_full, surviving_functional, phi6_of
from step77_gn_germ import jet_coords

OUT = HERE.parent / "data" / "step67"
OUT.mkdir(parents=True, exist_ok=True)


def make_case(lam, jet_index=0, seed=21):
    rng = np.random.default_rng(seed)
    jets = [unit_jet(rng) for _ in range(jet_index + 1)]
    jet = jets[jet_index]
    T = G.TowerAll(6, lam)
    H2 = G.make_H2(T, "jet", lam, np.random.default_rng(1000 + jet_index), jet, 1.0, 0.0)
    H3 = torch.zeros(T.size[3], dtype=G.dt, device=G.dev)
    return T, H2, H3, jet


def build_reduction(T, H2, H3, tol=1e-10):
    Udegs = [4, 5, 6, 7]
    orders = [1, 2, 3, 4, 5]
    sizes = [T.size[d] for d in Udegs]
    n = sum(sizes)
    base = G.zeros(T, skip=tuple(Udegs) + (2, 3))

    def jets_u(u, h8=None):
        out = {2: H2, 3: H3, **base}
        o = 0
        for d, s in zip(Udegs, sizes):
            out[d] = u[o:o+s]
            o += s
        if h8 is not None:
            out[8] = h8
        return out

    F = lambda u: T.Evec(jets_u(u), orders)[0]
    z = torch.zeros(n, dtype=G.dt, device=G.dev)
    b = F(z)
    A = G.batched_cols(F, n, b)
    u0 = -torch.linalg.pinv(A, rtol=tol) @ b
    N = G.null_right(A, tol)
    lin_resid = float((A @ u0 + b).norm())

    zall = G.zeros(T)
    n8 = T.size[8]
    f8 = lambda h: T.Evec({**zall, 8: h}, [6])[0]
    z8 = torch.zeros(n8, dtype=G.dt, device=G.dev)
    b8 = f8(z8)
    L6 = G.batched_cols(f8, n8, b8)
    C6 = G.null_left(L6, tol)

    E6 = lambda u: T.Evec(jets_u(u), [6])[0]
    cfull = C6.T @ E6(u0)
    vj = torch.func.vmap(lambda v: torch.func.jvp(E6, (u0,), (v,))[1])
    Jfull = C6.T @ torch.cat([vj(N[:, s:s+64].T).T for s in range(0, N.shape[1], 64)], dim=1)

    # Reuse independently regenerated universal quadratic cache.
    if "Qc" not in G._CACHE:
        G.reduce_general(T, H2, H3)
    Qc = G._CACHE["Qc"]
    N4 = N[:sizes[0]]
    Hfull = 2 * torch.einsum("ia,rij,jb->rab", N4, Qc, N4)

    # Remove rows that are identically zero on the quadratic model.
    Gram = torch.outer(cfull, cfull) + Jfull @ Jfull.T + torch.einsum("rab,sab->rs", Hfull, Hfull)
    ev, V = torch.linalg.eigh(Gram)
    rr = int((ev > tol * ev[-1]).sum())
    Ur = V[:, -rr:]
    cr = (Ur.T @ cfull).cpu().numpy()
    Jr = (Ur.T @ Jfull).cpu().numpy()
    Hr = torch.einsum("rs,rab->sab", Ur, Hfull).cpu().numpy()

    return {
        "T": T, "H2": H2, "H3": H3, "Udegs": Udegs, "sizes": sizes,
        "jets_u": jets_u, "u0": u0, "N": N, "L6": L6, "C6": C6,
        "cfull": cfull, "Jfull": Jfull, "Hfull": Hfull,
        "Ur": Ur, "cr": cr, "Jr": Jr, "Hr": Hr,
        "lin_resid": lin_resid, "rows": rr,
    }


def reduced_value(R, y):
    return R["cr"] + R["Jr"] @ y + 0.5*np.einsum("rab,a,b->r", R["Hr"], y, y)


def scalar_geometry(R, tol=1e-9):
    c, J, H = R["cr"], R["Jr"], R["Hr"]
    m, n = J.shape
    Hs = np.concatenate([H[i] for i in range(m)], axis=1)
    Uq, sv, _ = np.linalg.svd(Hs, full_matrices=False)
    rq = int((sv > tol*sv[0]).sum())
    P, K = Uq[:, :rq], Uq[:, rq:]
    JK = J @ K
    Ul, sl, _ = np.linalg.svd(JK, full_matrices=True)
    rw = int((sl > tol*sl[0]).sum())
    Pi = Ul[:, rw:]
    # remove rows vanishing identically
    M = np.concatenate([Pi.T @ c[:,None], Pi.T @ J,
                        np.einsum("ri,rab->iab", Pi, H).reshape(Pi.shape[1], -1)], axis=1)
    Um, sm, _ = np.linalg.svd(M, full_matrices=False)
    keep = sm > tol*(sm[0] if sm.size else 1)
    Pin = Pi @ Um[:, keep]
    if Pin.shape[1] != 1:
        raise RuntimeError(f"expected one scalar, got {Pin.shape[1]}")
    pi = Pin[:,0]
    # normalize by the actual full degree-6 functional, matching A02 convention
    ell = R["C6"].cpu().numpy() @ (R["Ur"].cpu().numpy() @ pi)
    pi = pi / np.linalg.norm(ell)
    ell = R["C6"].cpu().numpy() @ (R["Ur"].cpu().numpy() @ pi)
    j = (pi @ J) @ P
    Hred = P.T @ np.einsum("i,iab->ab", pi, H) @ P
    cc = float(pi @ c)
    ee = np.linalg.eigvalsh(Hred)
    if ee[-1] < 0:
        pi, ell, j, Hred, cc, ee = -pi, -ell, -j, -Hred, -cc, -ee[::-1]
    phi = cc - 0.5*j @ np.linalg.solve(Hred, j) if ee[0] > 0 else None
    return {"P": P, "K": K, "pi": pi, "ell": ell, "j": j, "Hred": Hred,
            "c": cc, "Phi6": float(phi) if phi is not None else None,
            "eig_min": float(ee[0]), "eig_max": float(ee[-1]),
            "quad_rank": rq, "absorbed_rank": rw}


def lm_full(R, y0, iters=300, tol=1e-13):
    """A02/Step78 damped LM on the complete 35-row quadratic system."""
    c, J, H = R["cr"], R["Jr"], R["Hr"]
    y = np.asarray(y0, dtype=float).copy()
    mu = 1e-3
    f = reduced_value(R, y); nf = float(np.linalg.norm(f)); hist=[nf]
    for it in range(iters):
        Jy = J + np.einsum("rab,b->ra", H, y)
        g = Jy.T @ f
        A = Jy.T @ Jy
        while True:
            step = -np.linalg.solve(A + mu*np.eye(len(y)), g)
            fn = reduced_value(R, y + step); nn = float(np.linalg.norm(fn))
            if nn < nf:
                y, f, nf = y + step, fn, nn
                mu = max(mu/3, 1e-15)
                hist.append(nf)
                break
            mu *= 4
            if mu > 1e12:
                return y, hist
        if nf < tol:
            break
    return y, hist


def reconstruct(lam, jet_index, seed=21):
    t0=time.time()
    T,H2,H3,jet = make_case(lam,jet_index,seed)
    R=build_reduction(T,H2,H3)
    SG=scalar_geometry(R)
    rec={"lam":lam,"jet_index":jet_index,"lin_resid":R["lin_resid"],"rows":R["rows"],
         "ny":int(R["N"].shape[1]),"quad_rank":SG["quad_rank"],"absorbed_rank":SG["absorbed_rank"],
         "Phi6":SG["Phi6"],"Hred_eig_min":SG["eig_min"],"Hred_eig_max":SG["eig_max"],
         "scalar_c":SG["c"],"jet":jet_coords(T.torsion({2:H2,**G.zeros(T,skip=(2,))}))}
    if SG["Phi6"] is None or SG["Phi6"] > 0:
        rec["reconstructed"] = False
        rec["time"] = time.time()-t0
        return rec, None

    # Start at scalar minimizer in the active range; LM enforces every nontrivial row.
    zstar = -np.linalg.solve(SG["Hred"], SG["j"])
    y0 = SG["P"] @ zstar
    y,hist=lm_full(R,y0,iters=160)
    rr=reduced_value(R,y)
    u=(R["u0"] + R["N"] @ torch.tensor(y,dtype=G.dt,device=G.dev))
    jets=R["jets_u"](u)
    E6=T.Evec(jets,[6])[0]
    # minimum-norm H8 correction to kill E6
    h8=torch.linalg.lstsq(R["L6"],-E6).solution
    jets8=R["jets_u"](u,h8)
    per={k:float(T.Evec(jets8,[k])[0].norm()) for k in range(7)}
    allres=float(T.Evec(jets8,list(range(7)))[0].norm())
    rec.update({"reconstructed":True,"reduced_res_norm":float(np.linalg.norm(rr)),
                "reduced_res_history_tail":[float(x) for x in hist[-10:]],
                "full_res_norm_E0_to_E6":allres,"per_order_res_norm":per,
                "H_norms":{str(k):float(v.norm()) for k,v in jets8.items()},
                "time":time.time()-t0})
    payload={"jets":{k:v.detach().cpu() for k,v in jets8.items()},"y":torch.tensor(y),
             "ell":torch.tensor(SG["ell"]),"pi":torch.tensor(SG["pi"]),
             "active_P":torch.tensor(SG["P"]),"Hred":torch.tensor(SG["Hred"]),
             "jred":torch.tensor(SG["j"]),"u0":R["u0"].detach().cpu(),"N":R["N"].detach().cpu()}
    return rec,payload


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lam",type=float,default=-40.0); ap.add_argument("--jet",type=int,default=0); ap.add_argument("--tag",default="neg")
    a=ap.parse_args()
    rec,payload=reconstruct(a.lam,a.jet)
    (OUT/f"reconstruct_{a.tag}.json").write_text(json.dumps(rec,indent=1,default=float)+"\n")
    if payload is not None: torch.save(payload,OUT/f"reconstruct_{a.tag}.pt")
    print(json.dumps(rec,indent=1,default=float),flush=True)

if __name__=="__main__": main()
