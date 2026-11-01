#!/usr/bin/env python3
"""Step 78: structured real tower for formal AKE germs with a torsion zero (Darboux gauge, even ansatz).

Purpose: decide whether the order-6 (and higher) compatibility conditions admit REAL solutions once the
torsion jet H2 is fixed on the order-2 quadric.  Unlike the Step-77 LM search, H2 is held fixed and the
remaining unknowns H4, H6, ..., H_{K+2} are solved by undamped Gauss-Newton with minimum-norm steps
(the system is underdetermined; equations E_2..E_K, all components).

Structure (x-degree k of E = Ric(e^H) - lam e^H involves products of jets with sum of degrees k+2 for the
Ricci part, k for the lam part):  E_k = L_k H_{k+2} + N_k(H_2..H_k).  For even H, E_6 is QUADRATIC in H4
(H4*H4 terms), E_8 is linear in H6 given H4, E_10 quadratic in H6, etc.

Input : H2 either from a Step-77 D=6 solution (.pt) or a fresh random real quadric point (--h2 random).
Output: workspace/data/step78_real_tower_<tag>.json  (residual history per order, jet invariants, ranks).
Run   : CUDA_VISIBLE_DEVICES=1 python scripts/step78_real_tower.py --K 6 --lam -3 --h2 d6
"""
import json, sys, time, math
from pathlib import Path
import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from step77_gn_germ import TRing, ricci_E, anti_basis, dev, dt, OM, PHI0, jet_coords

DATA = Path(__file__).resolve().parents[1] / 'data'


class Tower:
    def __init__(self, K, lam):
        self.K = K; self.N = K + 2; self.lam = lam
        self.R = TRing(self.N)
        self.Bs = torch.tensor(anti_basis(), dtype=dt, device=dev)
        self.mon_d = {d: [i for i, m in enumerate(self.R.mons) if sum(m) == d] for d in range(self.N + 1)}
        self.degs = list(range(2, self.N + 1, 2))
        self.size = {d: 6 * len(self.mon_d[d]) for d in self.degs}
        self.d1 = [self.R.idx[tuple(1 if t == m else 0 for t in range(4))] for m in range(4)]
        iu = [(i, j) for i in range(4) for j in range(i, 4)]
        self.iu = iu

    def H(self, jets):
        """jets: dict degree -> tensor (6*n_d)"""
        H = torch.zeros(4, 4, self.R.nm, dtype=dt, device=dev)
        for d, v in jets.items():
            U = v.reshape(6, -1)
            Hc = torch.einsum('aij,am->ijm', self.Bs, U)
            idx = torch.tensor(self.mon_d[d], device=dev)
            H = H.index_copy(2, idx, Hc)
        return H

    def Evec(self, jets, orders):
        E, G = ricci_E(self.R, self.H(jets), self.lam)
        out = []
        for k in orders:
            idx = torch.tensor(self.mon_d[k], device=dev)
            out.append(torch.stack([E[i, j][idx] for (i, j) in self.iu]).reshape(-1))
        return torch.cat(out), G

    def torsion(self, jets):
        _, G = self.Evec(jets, [0])
        Om = torch.tensor(OM, dtype=dt, device=dev); Ph = torch.tensor(PHI0, dtype=dt, device=dev)
        G1 = G[..., self.d1]
        T = -torch.einsum('lkim,lj->kijm', G1, Om) - torch.einsum('lkjm,il->kijm', G1, Om)
        Dm = torch.einsum('kijm,ij->km', T, Ph) / 4
        return Dm


def load_h2_from_d6(path, T):
    u = torch.load(path).to(dev)
    R6 = TRing(6)
    cols = [i for i, m in enumerate(R6.mons) if sum(m) in (2, 4, 6)]
    U = u.reshape(6, len(cols))
    jets = {}
    for d in (2, 4, 6):
        sel = [n for n, i in enumerate(cols) if sum(R6.mons[i]) == d]
        mons = [R6.mons[cols[n]] for n in sel]
        order = [T.R.idx[m] for m in mons]
        # reorder to T.mon_d[d]
        pos = {T.R.idx[m]: n for n, m in zip(sel, mons)}
        jets[d] = torch.stack([U[:, pos[i]] for i in T.mon_d[d]], dim=1).reshape(-1)
    return jets


def gn_solve(T, jets, free, orders, iters=40, tol=1e-13, log=True, rcond=1e-11):
    """Gauss-Newton (min-norm, backtracking) on unknown jets `free` (list of degrees)."""
    sizes = [T.size[d] for d in free]
    x = torch.cat([jets[d] for d in free])
    fixed = {d: v for d, v in jets.items() if d not in free}

    def unpack(x):
        out = dict(fixed); o = 0
        for d, s in zip(free, sizes):
            out[d] = x[o:o + s]; o += s
        return out

    F = lambda x: T.Evec(unpack(x), orders)[0]
    hist = []
    for it in range(iters):
        r = F(x); nr = float(r.norm()); hist.append(nr)
        if log:
            print('  it', it, 'res %.3e' % nr, flush=True)
        if nr < tol:
            break
        Jm = torch.func.jacfwd(F)(x)
        U_, s_, Vh_ = torch.linalg.svd(Jm, full_matrices=False)
        keep = s_ > rcond * s_[0]
        step = -(Vh_[keep].T @ ((U_[:, keep].T @ r) / s_[keep]))
        t = 1.0
        while t > 1e-4:
            nn = float(F(x + t * step).norm())
            if nn < nr:
                break
            t /= 2
        x = x + t * step
    Jm = torch.func.jacfwd(F)(x)
    sv = torch.linalg.svdvals(Jm).cpu().numpy()
    return unpack(x), hist, sv


def per_order(T, jets):
    res = {}
    for k in range(0, T.K + 1, 2):
        res[k] = float(T.Evec(jets, [k])[0].norm())
    return res


def main(K=6, lam=-3.0, h2='d6', seed=0, iters=40, tag=None, extra_scale=0.0):
    t0 = time.time(); torch.manual_seed(seed)
    T = Tower(K, lam)
    if h2 == 'd6':
        jets = load_h2_from_d6(DATA / 'step77_gn_D6_even_lam-3.0_s0.pt', T)
        assert abs(lam + 3.0) < 1e-12
    else:
        raise SystemExit('only d6 start implemented here; see step78_quadric_points.py')
    for d in T.degs:
        if d not in jets:
            jets[d] = torch.zeros(T.size[d], dtype=dt, device=dev)
        elif d > 2 and extra_scale:
            jets[d] = jets[d] + extra_scale * torch.randn(T.size[d], dtype=dt, device=dev)
    print('start per-order residuals', per_order(T, jets), flush=True)
    free = [d for d in T.degs if d >= 4]
    orders = list(range(2, K + 1, 2))
    jets, hist, sv = gn_solve(T, jets, free, orders, iters=iters)
    po = per_order(T, jets)
    jc = jet_coords(T.torsion(jets))
    out = {'K': K, 'lam': lam, 'h2': h2, 'seed': seed, 'hist': hist, 'per_order': po, 'jet': jc,
           'sv_tail': [float(s) for s in sv[-40:]], 'sv_max': float(sv[0]), 'n_eq': int(sum(10 * len(T.mon_d[k]) for k in orders)),
           'n_unknowns': int(sum(T.size[d] for d in free)), 'time': time.time() - t0}
    tag = tag or f'K{K}_lam{lam}_{h2}_s{seed}'
    (DATA / 'step78' / f'real_tower_{tag}.json').write_text(json.dumps(out, indent=1) + '\n')
    torch.save({d: v.cpu() for d, v in jets.items()}, DATA / 'step78' / f'real_tower_{tag}.pt')
    print(json.dumps({k: v for k, v in out.items() if k not in ('hist',)}, indent=1))


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--K', type=int, default=6)
    ap.add_argument('--lam', type=float, default=-3.0)
    ap.add_argument('--h2', default='d6')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--iters', type=int, default=40)
    ap.add_argument('--extra_scale', type=float, default=0.0)
    a = ap.parse_args()
    main(a.K, a.lam, a.h2, a.seed, a.iters, extra_scale=a.extra_scale)
