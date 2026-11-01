"""Step 53c: pointwise curvature data at the origin of numerically solved AK-Einstein jets.

For each saved solution z (step53_ak_einstein_jets.py), compute from the 2-jet of g and 1-jet of omega:
  s(0), W+(0) in the SD basis (e01+e23, e02-e13, e03+e12)/sqrt2 with omega/sqrt2 first, |W-(0)|,
  nu = W+_00 (check nu = s/6 + q/4), eta = W+_{0,perp}, V = traceless perp block, q(0).
Usage: python step53_jet_curvature.py TAG D [TAG D ...]   (reads data/step53_jets/akjets_<TAG>_z*.npy)
"""
import os, sys, glob, json
import numpy as np
import jax.numpy as jnp
from step53_ak_einstein_jets import setup

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "step53_jets")
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
r2 = 1/np.sqrt(2)
SD = np.array([[r2, 0, 0, 0, 0, r2], [0, r2, 0, 0, -r2, 0], [0, 0, r2, r2, 0, 0]])
ASD = np.array([[r2, 0, 0, 0, 0, -r2], [0, r2, 0, 0, r2, 0], [0, 0, r2, -r2, 0, 0]])

def analyze(tag, D):
    P, unpack, residual, nvar, ng, nw = setup(D)
    out = []
    for f in sorted(glob.glob(os.path.join(DATA, f"akjets_{tag}_z*.npy"))):
        z = np.load(f); g, w = unpack(jnp.array(z)); g = np.asarray(g); w = np.asarray(w)
        H = np.zeros((4, 4, 4, 4))   # H[i,j,k,l] = d_k d_l g_ij (0)
        for c, a in enumerate(P.L):
            if sum(a) == 2:
                ks = [k for k in range(4) for _ in range(a[k])]
                k, l = ks; fac = 2.0 if k == l else 1.0
                H[:, :, k, l] = g[:, :, c]*fac; H[:, :, l, k] = g[:, :, c]*fac
        R = np.zeros((4, 4, 4, 4))
        for a_, b, c_, d in np.ndindex(4, 4, 4, 4):
            R[a_, b, c_, d] = 0.5*(H[a_, d, b, c_] + H[b, c_, a_, d] - H[a_, c_, b, d] - H[b, d, a_, c_])
        Ric = np.einsum('abad->bd', R); s = np.trace(Ric)
        dl = np.eye(4)
        W = (R - 0.5*(np.einsum('ac,bd->abcd', dl, Ric) - np.einsum('ad,bc->abcd', dl, Ric)
                      - np.einsum('bc,ad->abcd', dl, Ric) + np.einsum('bd,ac->abcd', dl, Ric))
             + s/6*(np.einsum('ac,bd->abcd', dl, dl) - np.einsum('ad,bc->abcd', dl, dl)))
        M = np.array([[W[i, j, k, l] for (k, l) in PAIRS] for (i, j) in PAIRS])
        Wp = SD @ M @ SD.T; Wm = ASD @ M @ ASD.T
        lin = P.deg == 1
        q = float(sum((w[i, j][lin]**2).sum() for (i, j) in PAIRS))
        nu = Wp[0, 0]; eta = Wp[0, 1:]; Vb = Wp[1:, 1:] - np.trace(Wp[1:, 1:])/2*np.eye(2)
        out.append({"file": os.path.basename(f), "s": float(s), "q": q, "nu": float(nu), "nu_pred": float(s/6 + q/4),
                    "eta": eta.tolist(), "|eta|": float(np.linalg.norm(eta)), "|V|": float(np.linalg.norm(Vb)/np.sqrt(2)),
                    "|W-|": float(np.linalg.norm(Wm)), "trW+": float(np.trace(Wp)), "|Ric0|": float(np.linalg.norm(Ric - s/4*dl)),
                    "spec_W+": np.linalg.eigvalsh(Wp).tolist()})
        print(tag, json.dumps(out[-1]), flush=True)
    json.dump(out, open(os.path.join(DATA, f"curv_{tag}.json"), "w"), indent=1)

if __name__ == "__main__":
    a = sys.argv[1:]
    for i in range(0, len(a), 2):
        analyze(a[i], int(a[i+1]))
