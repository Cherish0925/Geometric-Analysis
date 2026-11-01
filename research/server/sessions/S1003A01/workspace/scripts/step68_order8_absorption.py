#!/usr/bin/env python3
"""Step 68g: linear absorbability of the order-8 scalar compatibility at A02's reconstructed even germ.

Base: A02 recon (H2..H8, H odd = 0, lam), even germ so odd orders vanish by parity.
Variables v = (H4, H6, H8) (H2 fixed).  Constraint map C(v) = (E2, E4, E6).  Tangent space TV = ker DC(v*).
Order-8 conditions: the 84 coefficients of the scalar compatibility P(E8) (Bianchi rows automatic; L8 H10 is
killed by P).  We compute G = D[P(E8)] restricted to TV, its rank, and the component of the radial row
ell8 = Delta^3 P(E8)(0).  Full rank 84 (radial included) => the order-8 system is a submersion on the order-6
solution variety at this point (no new sign condition at the linear level); radial row missed => order 8 adds a
genuine scalar condition carried only by quadratic terms.  Also performs damped Gauss-Newton on (E2,E4,E6,P E8)
from the base to test actual real solvability through order 8.
Output: workspace/data/step68/order8_absorption_<name>.json
"""
import json, sys, os, time
from pathlib import Path
import numpy as np
import torch
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / 'S1003A02' / 'workspace' / 'scripts')); sys.path.insert(0, str(HERE))
from step78_real_tower import Tower
from step77_gn_germ import dev, dt
from step68_scalar_compatibility import P_matrix
from step68_cokernel_tower import ell_vector
OUT = HERE.parent / 'data' / 'step68'


def main(name):
    base = HERE.parents[2] / 'S1003A02' / 'workspace' / 'data' / 'step80'
    dd = np.load(base / f'{name}.npz'); lam = float(name.split('lam')[-1])
    T = Tower(8, lam); T.degs = list(range(2, T.N + 1)); T.size = {e: 6 * len(T.mon_d[e]) for e in T.degs}
    tt = lambda a: torch.tensor(a, dtype=dt, device=dev)
    H2 = tt(dd['H2']); sizes = [T.size[4], T.size[6], T.size[8]]; n = sum(sizes)
    v0 = torch.cat([tt(dd['H4']), tt(dd['H6']), tt(dd['H8'])])
    scale = torch.cat([torch.full((s,), float(dd[k].std()) + 1e-30, dtype=dt, device=dev) for s, k in zip(sizes, ['H4', 'H6', 'H8'])])
    P8 = tt(P_matrix(8).astype(float)); ell = ell_vector(8).astype(float)
    w = np.linalg.lstsq(P_matrix(8).T.astype(float), ell, rcond=None)[0]; w = tt(w / np.linalg.norm(w))
    def jets(v):
        return {2: H2, 4: v[:sizes[0]], 6: v[sizes[0]:sizes[0] + sizes[1]], 8: v[sizes[0] + sizes[1]:]}
    def F(v):
        E = T.Evec(jets(v), [2, 4, 6, 8])[0]
        nC = 10 * (len(T.mon_d[2]) + len(T.mon_d[4]) + len(T.mon_d[6]))
        return E[:nC], P8 @ E[nC:]
    t0 = time.time()
    C0, R0 = F(v0)
    rec = {'name': name, 'lam': lam, 'n_vars': n, 'base_C_norm': float(C0.norm()), 'base_PE8_norm': float(R0.norm()),
           'base_radial': float(w @ R0)}
    # Jacobians in scaled variables v = v0 + scale*x
    f = lambda x: torch.cat(F(v0 + scale * x))
    vj = torch.func.vmap(lambda e: torch.func.jvp(f, (torch.zeros(n, dtype=dt, device=dev),), (e,))[1])
    eye = torch.eye(n, dtype=dt, device=dev)
    Jm = torch.cat([vj(eye[s:s + 64]).T for s in range(0, n, 64)], dim=1).cpu().numpy()
    nC = C0.shape[0]; JC = Jm[:nC]; JR = Jm[nC:]
    rec['jac_time'] = time.time() - t0
    U, s, Vt = np.linalg.svd(JC, full_matrices=True)
    rC = int((s > 1e-11 * s[0]).sum()); TV = Vt[rC:].T
    rec['rank_JC'] = rC; rec['dim_TV'] = int(TV.shape[1]); rec['JC_sv_gap'] = [float(s[rC - 1]), float(s[rC]) if rC < len(s) else 0.0]
    G = JR @ TV
    sg = np.linalg.svd(G, compute_uv=False)
    rec['rank_G'] = int((sg > 1e-9 * sg[0]).sum()); rec['G_sv_tail'] = [float(x) for x in sg[-6:]]; rec['G_sv_top'] = float(sg[0])
    wn = w.cpu().numpy()
    rec['radial_row_on_TV_rel'] = float(np.linalg.norm(wn @ G) / np.linalg.norm(G, 2))
    # radial row modulo the span of the other 83 P-row directions on TV
    Q, _ = np.linalg.qr(np.linalg.svd(P_matrix(8).astype(float).T, full_matrices=False)[0])
    # simple: rank of G with the radial row projected out
    Pperp = np.eye(84) - np.outer(wn, wn)
    sg2 = np.linalg.svd(Pperp @ G, compute_uv=False)
    rec['rank_G_without_radial'] = int((sg2 > 1e-9 * sg[0]).sum())
    print(json.dumps(rec, indent=1), flush=True)
    # damped Gauss-Newton on full system (C, R) in scaled variables
    x = np.zeros(n); hist = []
    for it in range(12):
        Cx, Rx = F(v0 + scale * tt(x)); res = np.concatenate([Cx.cpu().numpy(), Rx.cpu().numpy()])
        hist.append([float(np.linalg.norm(Cx.cpu().numpy())), float(np.linalg.norm(Rx.cpu().numpy())), float(wn @ Rx.cpu().numpy())])
        print('GN', it, hist[-1], flush=True)
        if np.linalg.norm(res) < 1e-10: break
        fx = lambda y: torch.cat(F(v0 + scale * y))
        vjx = torch.func.vmap(lambda e: torch.func.jvp(fx, (tt(x),), (e,))[1])
        Jx = torch.cat([vjx(eye[s:s + 64]).T for s in range(0, n, 64)], dim=1).cpu().numpy()
        dx = np.linalg.lstsq(Jx, -res, rcond=1e-12)[0]
        # backtracking
        t = 1.0; base_n = np.linalg.norm(res)
        for _ in range(20):
            C1, R1 = F(v0 + scale * tt(x + t * dx))
            if np.sqrt(float(C1.norm()) ** 2 + float(R1.norm()) ** 2) < base_n: break
            t /= 2
        x = x + t * dx
    rec['GN_hist'] = hist; rec['dx_scaled_norm'] = float(np.linalg.norm(x))
    np.save(OUT / f'order8_x_{name}.npy', x)
    (OUT / f'order8_absorption_{name}.json').write_text(json.dumps(rec, indent=1) + '\n')
    print(json.dumps({k: rec[k] for k in ['GN_hist', 'dx_scaled_norm']}), flush=True)


if __name__ == '__main__':
    main(sys.argv[1])
