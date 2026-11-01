#!/usr/bin/env python3
"""Step 71b: which lower-order metric freedoms feed the next scalar compatibility?

Setting as step71_fibre_test.py (A02 Darboux tower, polished gen5 lambda=-5 witness, H2 fixed).
Tan = ker dC, C=(E2..E_{K-2}); R = P_K(E_K).  For each lower degree d<K the variation dH_d of a
tangent vector lies in the flat Einstein kernel (mod lower data) and is split into
   principal torsion part  (detected by dN_{d-1}, the degree-(d-1) Nijenhuis coefficient, which is
                            linear in H_d with only lower jets fixed),
   Hamiltonian gauge       (flat sym dX, X = Omega grad f, f homogeneous of degree d+2),
   physical curvature      (the rest of ker T).
We compute ranks of dR on nested subspaces of Tan:
   S_top   : dH_d = 0 for all d<K                   (newest channel)
   S_gauge : dH_d in gauge span, d<K
   S_curv  : dN_{d-1}(dH) = 0 for d<K  (torsion part of every lower jet fixed; includes gauge+curvature)
   S_all   : Tan
plus the same with only the highest lower degree released.  If rank(S_curv) > rank(S_gauge),
physical torsion-free curvature data feed the scalar obstruction (coupled tower);
if equal, the obstruction factors through torsion data at this order.
Absolute thresholds are used and the singular spectra are recorded.
Out: workspace/data/step71/fibre_split_K{K}.json
"""
from pathlib import Path
import json, sys, time, itertools
import numpy as np
import torch
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[2] / 'S1003A02' / 'workspace' / 'scripts'))
from step78_real_tower import Tower
from step77_gn_germ import dev, dt, J0, OM, anti_basis
from step68_scalar_compatibility import P_matrix
from step71_fibre_test import expH, nijenhuis
OUT = HERE.parent / 'data' / 'step71'; OUT.mkdir(parents=True, exist_ok=True)


def gauge_basis(T, d):
    """Flat Hamiltonian gauge on degree-d jets in Tower layout: columns of (6*n_d, m)."""
    mons_d = [T.R.mons[i] for i in T.mon_d[d]]; pos = {m: q for q, m in enumerate(mons_d)}
    B = anti_basis().reshape(6, 16)                       # (6,16)
    Bpinv = np.linalg.pinv(B.T)                            # 16 -> 6 coefficients
    fmons = [m for m in itertools.product(range(d + 3), repeat=4) if sum(m) == d + 2]
    best = None
    for Om in (OM, OM.T):
        cols = []; resid = 0.0
        for fm in fmons:
            # grad f components (degree d+1): dict mon->coef
            grad = []
            for k in range(4):
                if fm[k] == 0: grad.append({}); continue
                mm = list(fm); mm[k] -= 1; grad.append({tuple(mm): fm[k]})
            X = [dict() for _ in range(4)]
            for i in range(4):
                for k in range(4):
                    if Om[i, k]:
                        for m, c in grad[k].items(): X[i][m] = X[i].get(m, 0) + Om[i, k] * c
            # dg_ij = d_i X_j + d_j X_i at degree d
            G = np.zeros((4, 4, len(mons_d)))
            for i in range(4):
                for j in range(4):
                    for (a, b) in ((i, j), (j, i)):
                        for m, c in X[b].items():
                            if m[a] == 0: continue
                            mm = list(m); mm[a] -= 1
                            G[i, j, pos[tuple(mm)]] += c * m[a]
            Gf = G.reshape(16, -1)
            U = Bpinv @ Gf                                  # (6, n_d)
            resid += float(np.linalg.norm(B.T @ U - Gf))
            cols.append(U.reshape(-1))
        M = np.array(cols).T
        if best is None or resid < best[1]: best = (M, resid)
    M, resid = best
    u, s, vh = np.linalg.svd(M, full_matrices=False)
    r = int((s > 1e-9 * s[0]).sum())
    return u[:, :r], resid, r


def main(K=6, name='recon_F012_gen5_lam-5'):
    t0 = time.time()
    lam = float(name.split('lam')[-1])
    base = HERE.parents[2] / 'S1003A02' / 'workspace' / 'data' / 'step80'
    dd = np.load(base / f'{name}.npz')
    T = Tower(K, lam); T.degs = list(range(2, T.N + 1)); T.size = {e: 6 * len(T.mon_d[e]) for e in T.degs}
    tt = lambda a: torch.tensor(np.asarray(a), dtype=dt, device=dev)
    H2 = tt(dd['H2'])
    pv = HERE.parent / 'data' / 'step69' / f'order8_polished_v_{name}.npy'
    if pv.exists():
        v8 = np.load(pv); s8 = [6 * 35, 6 * 84, 6 * 165]
        parts = {4: v8[:s8[0]], 6: v8[s8[0]:s8[0] + s8[1]], 8: v8[s8[0] + s8[1]:]}
    else:
        parts = {d: dd[f'H{d}'] for d in (4, 6, 8) if f'H{d}' in dd.files}
    unk = list(range(4, K + 1, 2)); sizes = [T.size[d] for d in unk]
    offs = dict(zip(unk, np.cumsum([0] + sizes[:-1]).tolist()))
    x0 = torch.cat([tt(parts[d]) for d in unk]); n = x0.numel()
    cons = list(range(2, K - 1, 2))
    PK = tt(P_matrix(K).astype(float) / 2.0)
    iu = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    J0t = tt(J0)

    def jets(x):
        J = {2: H2}
        for d, s in zip(unk, sizes): J[d] = x[offs[d]:offs[d] + s]
        return J
    funC = lambda x: T.Evec(jets(x), cons)[0]
    funR = lambda x: PK @ T.Evec(jets(x), [K])[0]
    def funNd(deg):
        idx = torch.tensor(T.mon_d[deg], device=dev)
        def f(x):
            g = expH(T.R, T.H(jets(x))); Jm = torch.einsum('ab,bjp->ajp', J0t, g)
            N = nijenhuis(T.R, Jm)
            return torch.stack([N[k, i, j][idx] for k in range(4) for (i, j) in iu]).reshape(-1)
        return f
    eye = torch.eye(n, dtype=dt, device=dev)
    def jac(f):
        vj = torch.func.vmap(lambda e: torch.func.jvp(f, (x0,), (e,))[1])
        return torch.cat([vj(eye[s:s + 64]).T for s in range(0, n, 64)], dim=1)
    JC, JR = jac(funC), jac(funR)
    JN = {d: jac(funNd(d - 1)) for d in unk[:-1]}
    sC = torch.linalg.svdvals(JC); tolC = 1e-9 * float(sC[0])
    U_, s_, Vh_ = torch.linalg.svd(JC, full_matrices=True); r = int((s_ > tolC).sum()); Tan = Vh_[r:].T
    sR = torch.linalg.svdvals(JR @ Tan); refR = float(sR[0]); tolR = 1e-8 * refR
    out = {'K': K, 'name': name, 'dim_Tan': int(Tan.shape[1]), 'rank_R_on_Tan': int((sR > tolR).sum()),
           'sv_R_Tan_top': refR, 'sv_R_Tan_tail': [float(a) for a in sR[-4:]], 'gauge': {}}
    import step68_flat_cokernel as F
    from math import factorial
    tg = F.mons_deg(K - 2); m_ = (K - 2) // 2
    ell = np.array([factorial(m_) * np.prod([factorial(a) for a in mm]) / np.prod([factorial(a // 2) for a in mm]) if all(a % 2 == 0 for a in mm) else 0.0 for mm in tg])
    ell = tt(ell / np.linalg.norm(ell))
    G = {}
    for d in unk[:-1]:
        Gb, resid, rg = gauge_basis(T, d); G[d] = tt(Gb)
        out['gauge'][str(d)] = {'rank': rg, 'antiJ_projection_residual': resid}
        # check gauge lies in flat kernel direction of dN_{d-1}? (gauge changes N coords: record)
    def block(d):  # selector rows for dH_d
        Sel = torch.zeros(T.size[d], n, dtype=dt, device=dev); Sel[:, offs[d]:offs[d] + T.size[d]] = torch.eye(T.size[d], dtype=dt, device=dev)
        return Sel
    def rank_on(constraints, label):
        A = torch.cat([c @ Tan for c in constraints], 0) if constraints else torch.zeros(0, Tan.shape[1], dtype=dt, device=dev)
        if A.shape[0]:
            u, s, vh = torch.linalg.svd(A, full_matrices=True)
            rr = int((s > 1e-9 * max(float(s[0]), 1e-300)).sum()); Z = vh[rr:].T
        else:
            Z = torch.eye(Tan.shape[1], dtype=dt, device=dev)
        sub = Tan @ Z
        if sub.shape[1] == 0:
            out[label] = {'dim': 0, 'rank_R': 0}; return None
        s = torch.linalg.svdvals(JR @ sub)
        rk = int((s > tolR).sum())
        rad = float((ell @ (JR @ sub)).norm()); radT = float((ell @ (JR @ Tan)).norm())
        out[label] = {'dim': int(sub.shape[1]), 'rank_R': rk, 'radial_norm': rad, 'radial_norm_Tan': radT, 'sv_head': [float(a) for a in s[:3]],
                      'sv_around_rank': [float(a) for a in s[max(rk - 2, 0):rk + 3]]}
        print(label, out[label], flush=True)
        return sub
    lower = unk[:-1]
    proj_out = lambda d: (torch.eye(T.size[d], dtype=dt, device=dev) - G[d] @ G[d].T) @ block(d)
    rank_on([block(d) for d in lower], 'S_top')
    rank_on([proj_out(d) for d in lower], 'S_gauge')
    rank_on([JN[d] for d in lower], 'S_Nfixed_principal')
    # curvature+gauge: principal torsion fixed AND (for comparison) gauge removed? use S_Nfixed
    # releasing only the highest lower degree
    if len(lower) > 1:
        hi = lower[-1]; lo = lower[:-1]
        rank_on([block(d) for d in lo], 'S_release_hi_only')
        rank_on([block(d) for d in lo] + [proj_out(hi)], 'S_release_hi_gauge')
        rank_on([block(d) for d in lo] + [JN[hi]], 'S_release_hi_Nfixed')
        rank_on([JN[d] for d in lo] + [block(hi)], 'S_release_lo_Nfixed_only')
        rank_on([proj_out(d) for d in lo] + [block(hi)], 'S_release_lo_gauge_only')
    # does the principal torsion constraint cut the gauge? (gauge moves N coords => S_gauge not inside S_N)
    for d in lower:
        out['gauge'][str(d)]['dN_on_gauge_norm'] = float((JN[d][:, offs[d]:offs[d] + T.size[d]] @ G[d]).norm())
        out['gauge'][str(d)]['dN_block_norm'] = float(JN[d][:, offs[d]:offs[d] + T.size[d]].norm())
        # dN_{d-1} must not depend on higher jets
        out['gauge'][str(d)]['dN_dependence_on_higher'] = float(JN[d][:, offs[d] + T.size[d]:].norm())
    out['time'] = time.time() - t0
    (OUT / f'fibre_split_K{K}_{name}.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out['gauge']), out['time'], flush=True)


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6, sys.argv[2] if len(sys.argv) > 2 else 'recon_F012_gen5_lam-5')
