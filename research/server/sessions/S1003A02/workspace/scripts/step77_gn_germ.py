#!/usr/bin/env python3
"""Step 77: real Gauss-Newton search for formal AKE germs with a torsion zero (torch, float64, GPU).

Darboux gauge: Omega standard, g = exp(H), H anti-J symmetric, H = O(|x|^2) (torsion zero at 0).
Unknowns: coefficients of H in degrees 2..D (even ansatz: even degrees only, or all degrees).
Equations: all components of E = Ric(g) - lam g of degree <= K = D-2, plus the normalisation
|first jet of nabla Omega|^2 = tau2 (keeps the torsion zero nondegenerate-sized).
Gauss-Newton with minimum-norm steps (pseudo-inverse via SVD); Hamiltonian gauge is left free.
Reports the residual history, torsion jet coordinates (c,S,A) in the Step-76 normalisation,
the order-2 quadric value ||A||^2-||S||^2-8|c|^2, and the zero index det_R Df.
Output: workspace/data/step77_gn_<tag>.json
"""
import json, sys, time, itertools, math
from pathlib import Path
import numpy as np
import torch

DATA = Path(__file__).resolve().parents[1] / 'data'
dt = torch.float64
dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
J0 = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
OM = J0.T
PHI0 = np.zeros((4, 4)); PHI0[0, 2] = 1; PHI0[2, 0] = -1; PHI0[1, 3] = -1; PHI0[3, 1] = 1


def anti_basis():
    import sympy as sp
    syms = []
    for i in range(4):
        for j in range(i, 4):
            E = np.zeros((4, 4), dtype=int); E[i, j] = 1; E[j, i] = 1; syms.append(E)
    A = np.array([(S @ J0 + J0 @ S).ravel() for S in syms]).T
    out = []
    for v in sp.Matrix(A).nullspace():
        v = v * sp.ilcm(*[x.q for x in v])
        out.append(sum(int(v[t]) * syms[t] for t in range(10)))
    return np.array(out, dtype=float)


class TRing:
    def __init__(self, N):
        self.N = N
        mons = [e for d in range(N + 1) for e in itertools.product(range(d + 1), repeat=4) if sum(e) == d]
        self.mons = mons; self.idx = {m: i for i, m in enumerate(mons)}
        self.nm = len(mons); self.deg = torch.tensor([sum(m) for m in mons], device=dev)
        I, Jj, K = [], [], []
        for i, a in enumerate(mons):
            for j, b in enumerate(mons):
                if sum(a) + sum(b) <= N:
                    I.append(i); Jj.append(j); K.append(self.idx[tuple(x + y for x, y in zip(a, b))])
        self.I = torch.tensor(I, device=dev); self.J = torch.tensor(Jj, device=dev); self.K = torch.tensor(K, device=dev)
        Ds = []
        for k in range(4):
            Dm = torch.zeros(self.nm, self.nm, dtype=dt, device=dev)
            for i, m in enumerate(mons):
                mm = list(m); mm[k] += 1
                if sum(mm) <= N:
                    Dm[self.idx[tuple(mm)], i] = mm[k]     # coefficient of m in d/dx_k of x^mm
            Ds.append(Dm)
        self.D = torch.stack(Ds)      # (4, nm, nm): out[m] = sum_src D[k][src, m]*a[src]

    def diff(self, a, k):
        return a @ self.D[k]

    def mm(self, A, B, eq):
        """batched poly-matrix product with einsum spec eq on the pair axis"""
        prod = torch.einsum(eq, A[..., self.I], B[..., self.J])
        out = torch.zeros(prod.shape[:-1] + (self.nm,), dtype=dt, device=dev)
        return out.index_add(-1, self.K, prod)

    def trunc(self, a, d):
        return a * (self.deg <= d).to(dt)


def ricci_E(R, H, lam):
    N = R.N
    eye = torch.zeros(4, 4, R.nm, dtype=dt, device=dev)
    for i in range(4):
        eye[i, i, 0] = 1
    g = eye + H; gi = eye - H; Pw = H; fact = 1.0; sign = -1.0
    for n in range(2, N // 2 + 1):
        Pw = R.mm(Pw, H, 'ikp,kjp->ijp'); fact *= n; sign = -sign
        g = g + Pw / fact; gi = gi + sign * Pw / fact
    dg = torch.stack([R.diff(g, k) for k in range(4)], dim=2)          # dg[i,j,k] = d_k g_ij
    T = dg.permute(2, 0, 1, 3) + dg.permute(2, 1, 0, 3) - dg            # T[l,i,j] = d_i g_lj + d_j g_li - d_l g_ij
    # careful: dg[i,j,k]=d_k g_ij ; want t_lij = d_i g_lj + d_j g_li - d_l g_ij
    t = dg.permute(0, 2, 1, 3)  # t1[l,i,j] = d_i g_lj -> dg[l,j,i] ; build explicitly below
    t1 = dg.permute(0, 2, 1, 3)      # [l,i,j] <- dg[l,j,i]? dg[l,j,i] = d_i g_lj ; permute(0,2,1): new[l,a,b]=dg[l,b,a]
    t2 = dg.permute(0, 1, 2, 3)      # [l,i,j] = dg[l,i,j] = d_j g_li
    t3 = dg.permute(2, 0, 1, 3)      # [l,i,j] = dg[i,j,l] = d_l g_ij
    Tl = t1 + t2 - t3
    G = 0.5 * R.mm(gi, Tl, 'klp,lijp->kijp')
    G = R.trunc(G, N - 1)
    dG = torch.stack([R.diff(G, k) for k in range(4)], dim=0)         # dG[m,k,i,j] = d_m G^k_ij
    Ric = torch.einsum('kkij...->ij...', dG.permute(0, 1, 2, 3, 4)) if False else None
    # d_k G^k_ij
    t_a = sum(dG[k, k] for k in range(4))
    # d_j G^k_ik  -> [i,j]
    Gtr = sum(G[k, :, k] for k in range(4))        # G^k_ik as [i]
    t_b = torch.stack([torch.stack([R.diff(Gtr[i], j) for j in range(4)]) for i in range(4)])
    Gk = sum(G[k, k] for k in range(4))            # G^k_kl as [l]
    t_c = R.mm(Gk, G, 'lp,lijp->ijp')
    t_d = R.mm(G, G, 'kjlp,likp->ijp')
    Ric = R.trunc(t_a - t_b + t_c - t_d, N - 2)
    E = Ric - lam * g
    return R.trunc(E, N - 2), G


class Problem:
    def __init__(self, D, lam, parity='even', tau2=1.0):
        self.R = TRing(D); self.D = D; self.K = D - 2; self.lam = lam; self.tau2 = tau2
        self.Bs = torch.tensor(anti_basis(), dtype=dt, device=dev)     # (6,4,4)
        degs = [d for d in range(2, D + 1) if parity == 'all' or d % 2 == 0]
        self.cols = [i for i, m in enumerate(self.R.mons) if sum(m) in degs]
        self.ncols = len(self.cols)
        self.nu = 6 * self.ncols
        okdeg = lambda d: d <= self.K and (parity == 'all' or d % 2 == 0)   # odd E vanish identically for even H
        self.eqmask = [(i, j, m) for i in range(4) for j in range(i, 4) for m in range(self.R.nm) if okdeg(sum(self.R.mons[m]))]
        self.ei = torch.tensor([e[0] for e in self.eqmask], device=dev)
        self.ej = torch.tensor([e[1] for e in self.eqmask], device=dev)
        self.em = torch.tensor([e[2] for e in self.eqmask], device=dev)
        self.d1 = [self.R.idx[tuple(1 if t == m else 0 for t in range(4))] for m in range(4)]   # x1..x4 order
        self.colt = torch.tensor(self.cols, device=dev)

    def H(self, u):
        U = u.reshape(6, self.ncols)
        Hc = torch.einsum('aij,am->ijm', self.Bs, U)
        H = torch.zeros(4, 4, self.R.nm, dtype=dt, device=dev)
        return H.index_copy(2, self.colt, Hc)

    def torsion_D(self, G):
        # (nabla_k Omega)_ij = -G^l_ki OM_lj - G^l_kj OM_il  (degree-1 coefficients); a_k = <nabla_k Om, phi>/4
        Om = torch.tensor(OM, dtype=dt, device=dev); Ph = torch.tensor(PHI0, dtype=dt, device=dev)
        G1 = G[..., self.d1]                                    # (l,k,i,m)
        T = -torch.einsum('lkim,lj->kijm', G1, Om) - torch.einsum('lkjm,il->kijm', G1, Om)
        Dm = torch.einsum('kijm,ij->km', T, Ph) / 4
        return Dm, T

    def residual(self, u):
        E, G = ricci_E(self.R, self.H(u), self.lam)
        r = E[self.ei, self.ej, self.em]
        Dm, T = self.torsion_D(G)
        nrm = (T ** 2).sum() - self.tau2
        return torch.cat([r, nrm.reshape(1)])


def jet_coords(Dm):
    D = Dm.detach().cpu().numpy()
    M = np.vstack([D[0] + 1j * D[1], D[2] + 1j * D[3]])
    C = np.array([[(M[k, 0] - 1j * M[k, 1]) / 2, (M[k, 2] - 1j * M[k, 3]) / 2] for k in range(2)])
    B = np.array([[(M[k, 0] + 1j * M[k, 1]) / 2, (M[k, 2] + 1j * M[k, 3]) / 2] for k in range(2)])
    S = (B + B.T) / 2; A = (B - B.T) / 2
    c = C[0, 0]
    out = {'C_offdiag': float(abs(C[0, 1]) + abs(C[1, 0]) + abs(C[0, 0] - C[1, 1])),
           'c2': float(abs(c) ** 2), 'S2': float(np.sum(abs(S) ** 2)), 'A2': float(np.sum(abs(A) ** 2)),
           'detD': float(np.linalg.det(D))}
    out['quadric_A2-S2-8c2'] = out['A2'] - out['S2'] - 8 * out['c2']
    out['det_formula_9c4+|detB|^2'] = float(9 * abs(c) ** 4 + abs(np.linalg.det(B)) ** 2)
    return out


def gauss_newton(P, u0, iters=30, tol=1e-12, chunk=256, log=None):
    u = u0.clone()
    hist = []
    for it in range(iters):
        r = P.residual(u)
        nr = float(r.norm()); hist.append(nr)
        if log: print('it', it, 'res', nr, flush=True)
        if nr < tol:
            break
        Jm = torch.func.jacrev(P.residual, chunk_size=chunk)(u)
        # Levenberg-Marquardt in the SVD basis (min-norm in the null directions)
        U_, s, Vh = torch.linalg.svd(Jm, full_matrices=False)
        Ur = U_.T @ r
        if it == 0:
            mu = float(s[0]) * 1e-3
        while True:
            step = -(Vh.T * (s / (s ** 2 + mu ** 2))) @ Ur
            un = u + step
            nn = float(P.residual(un).norm())
            if nn < nr:
                mu = max(mu / 3, 1e-14 * float(s[0])); u = un; break
            mu *= 4
            if mu > 1e8 * float(s[0]):
                break
    sv = s.detach().cpu().numpy() if it > 0 else None
    return u, hist, sv


def main(D=8, lam=-3.0, parity='even', seed=0, iters=40, scale=0.05, tau2=1.0, tag=None, chunk=64):
    torch.manual_seed(seed)
    t0 = time.time()
    P = Problem(D, lam, parity, tau2)
    print('unknowns', P.nu, 'equations', len(P.eqmask) + 1, 'nm', P.R.nm, round(time.time() - t0, 1), flush=True)
    u0 = scale * torch.randn(P.nu, dtype=dt, device=dev)
    u, hist, sv = gauss_newton(P, u0, iters=iters, log=True, chunk=chunk)
    E, G = ricci_E(P.R, P.H(u), lam)
    Dm, T = P.torsion_D(G)
    jc = jet_coords(Dm)
    # residual by order
    r_by_order = {}
    rfull = P.residual(u)
    for k in range(0, P.K + 1):
        sel = [n for n, e in enumerate(P.eqmask) if sum(P.R.mons[e[2]]) == k]
        r_by_order[k] = float(rfull[sel].norm()) if sel else 0.0
    res = {'D': D, 'K': P.K, 'lam': lam, 'parity': parity, 'seed': seed, 'tau2': tau2,
           'unknowns': P.nu, 'equations': len(P.eqmask) + 1, 'hist': hist, 'residual_by_order': r_by_order,
           'jet': jc, 'u_norm': float(u.norm()), 'time': time.time() - t0,
           'jac_rank_1e-9': int((sv > sv[0] * 1e-9).sum()) if sv is not None else None}
    tag = tag or f'D{D}_{parity}_lam{lam}_s{seed}'
    (DATA / f'step77_gn_{tag}.json').write_text(json.dumps(res, indent=1) + '\n')
    torch.save(u.cpu(), DATA / f'step77_gn_{tag}.pt')
    print(json.dumps({k: v for k, v in res.items() if k != 'hist'}, indent=1))


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--D', type=int, default=8)
    ap.add_argument('--lam', type=float, default=-3.0)
    ap.add_argument('--parity', default='even')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--iters', type=int, default=40)
    ap.add_argument('--scale', type=float, default=0.05)
    ap.add_argument('--chunk', type=int, default=64)
    ap.add_argument('--tau2', type=float, default=1.0)
    a = ap.parse_args()
    main(a.D, a.lam, a.parity, a.seed, a.iters, a.scale, a.tau2, chunk=a.chunk)
