#!/usr/bin/env python3
"""Step 84: Session-side derivation of the scalar compatibility operator of the flat anti-J Ricci tower.

Statement checked (A01 #860, re-derived here independently in our own E-vector conventions):
  For d = 4, 6, 8 the left cokernel of the flat top map L_d : H_{d+2} (anti-J tracefree, 6 components)
  -> E_d (10 components x degree-d monomials) is spanned by
     (B) the linearized Bianchi rows   E -> coefficients of  d_i E_ij - (1/2) d_j tr E   (degree d-1, 4 comps)
     (P) the coefficients of the scalar  P(E) = J_ia J_jb d_a d_b E_ij - (1/2) Lap tr E   (degree d-2)
  and these are independent:  dim coker = 4*C(d+2,3) + C(d+1,3)  (224+35=259 at d=6, 480+84=564 at d=8).
  Moreover the universal order-6 multiplier ell (Step 80, data/step80/universal_pi.npz) is, modulo (B),
  a multiple of the radial row  E -> Lap^2 P(E_6)(0).

Proof content: (B) annihilates im L_d by the linearized Bianchi identity; (P) annihilates im L_d because
for anti-J tracefree h the anti-J part of dRic(h) is div-div exact (checked in Fourier in part (a)).
The exact rank count then shows nothing else is in the cokernel.

Output: workspace/data/step84/scalar_compat.json
Run:    python step84_scalar_compat.py   (CPU or GPU; ~1 min)
"""
import json, sys, os
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step84')
import step79_general_order6 as G
from step77_gn_germ import J0

dev, dt = G.dev, G.dt
OUT = Path(__file__).resolve().parents[1] / 'data' / 'step84'
OUT.mkdir(exist_ok=True, parents=True)
J = torch.tensor(J0, dtype=dt, device=dev)          # J[i,a]: J(e_a) = sum_i J[i,a] e_i


def fourier_check(ntrial=500, seed=84):
    """(a) P(dRic(h)) = 0 symbolically in Fourier, for every anti-J (automatically tracefree) h."""
    rng = np.random.default_rng(seed)
    Jn = np.array(J0, float)
    # anti-J symmetric: S J + J S = 0
    syms = []
    for i in range(4):
        for j in range(i, 4):
            E = np.zeros((4, 4)); E[i, j] = E[j, i] = 1; syms.append(E)
    A = np.array([(S @ Jn + Jn @ S).ravel() for S in syms]).T
    _, s, Vh = np.linalg.svd(A); ns = Vh[(s > 1e-12).sum():]
    basis = [sum(c * S for c, S in zip(v, syms)) for v in ns]
    err = 0.0; err_full = 0.0
    for _ in range(ntrial):
        k = rng.standard_normal(4); k2 = k @ k
        for h in basis + [rng.standard_normal((4, 4)) + 0 * np.eye(4)]:
            h = (h + h.T) / 2
            # dRic(h) symbol (up to overall -1 from i^2): R = 1/2(k k.h + h.k k) - 1/2 k2 h - 1/2 tr h k k
            kh = h @ k
            R = 0.5 * (np.outer(k, kh) + np.outer(kh, k)) - 0.5 * k2 * h - 0.5 * np.trace(h) * np.outer(k, k)
            Jk = Jn @ k
            PE = Jk @ R @ Jk - 0.5 * k2 * np.trace(R)
            if h is basis[0] or any(h is b for b in basis):
                err = max(err, abs(PE))
            else:
                err_full = max(err_full, abs(PE))
    return {'dim_antiJ': len(basis), 'max_P_dRic_antiJ': err, 'max_P_dRic_generic_h': err_full}


def operators(T, d):
    """Rows (as matrices acting on E_d vectors of T) of Bianchi B_d and of P_d (all coefficients) and radial row."""
    R = T.R; nm = R.nm
    iu = T.iu; nd = len(T.mon_d[d])
    ne = 10 * nd
    # unpack E vector -> full 4x4xnm polynomial tensor (linear map, build by columns)
    idx = torch.tensor(T.mon_d[d], device=dev)
    def unpack(v):
        V = v.reshape(10, nd)
        E = torch.zeros(4, 4, nm, dtype=dt, device=dev)
        for c, (i, j) in enumerate(iu):
            row = torch.zeros(nm, dtype=dt, device=dev).index_copy(0, idx, V[c])
            E[i, j] = row; E[j, i] = row
        return E
    Dk = lambda a, k: a @ R.D[k]
    def bianchi(v):
        E = unpack(v); tr = sum(E[i, i] for i in range(4))
        out = []
        for j in range(4):
            out.append(sum(Dk(E[i, j], i) for i in range(4)) - 0.5 * Dk(tr, j))
        o = torch.stack(out)
        sel = torch.tensor(T.mon_d[d - 1], device=dev)
        return o[:, sel].reshape(-1)
    def Pop(v):
        E = unpack(v); tr = sum(E[i, i] for i in range(4))
        p = torch.zeros(nm, dtype=dt, device=dev)
        for i in range(4):
            for jj in range(4):
                for a in range(4):
                    for b in range(4):
                        c = J[i, a] * J[jj, b]
                        if c != 0:
                            p = p + c * Dk(Dk(E[i, jj], a), b)
        lap = lambda f: sum(Dk(Dk(f, a), a) for a in range(4))
        p = p - 0.5 * lap(tr)
        return p
    def Pcoef(v):
        sel = torch.tensor(T.mon_d[d - 2], device=dev)
        return Pop(v)[sel]
    def radial(v):
        p = Pop(v)
        lap = lambda f: sum(Dk(Dk(f, a), a) for a in range(4))
        for _ in range((d - 2) // 2):
            p = lap(p)
        return p[R.idx[(0, 0, 0, 0)]].reshape(1)
    I = torch.eye(ne, dtype=dt, device=dev)
    B = torch.stack([bianchi(I[c]) for c in range(ne)], 1)
    P = torch.stack([Pcoef(I[c]) for c in range(ne)], 1)
    rad = torch.stack([radial(I[c]) for c in range(ne)], 1)
    return B, P, rad


def rank(M, tol=1e-9):
    s = torch.linalg.svdvals(M)
    return int((s > tol * s[0]).sum()) if s.numel() else 0


def main():
    rec = {'fourier': fourier_check()}
    print('fourier', rec['fourier'], flush=True)
    T = G.TowerAll(8, -1.0)
    zall = G.zeros(T)
    for d in (4, 6, 8):
        f = lambda h: T.Evec({**zall, d + 2: h}, [d])[0]
        L = G.batched_cols(f, T.size[d + 2], f(torch.zeros(T.size[d + 2], dtype=dt, device=dev)))
        rL = rank(L); coker = L.shape[0] - rL
        B, P, rad = operators(T, d)
        nB = float((B @ L).abs().max()); nP = float((P @ L).abs().max())
        rB = rank(B); rP = rank(P); rBP = rank(torch.cat([B, P])); rBr = rank(torch.cat([B, rad]))
        out = {'rows_E': L.shape[0], 'rank_L': rL, 'coker': coker,
               'max|B L|': nB, 'max|P L|': nP, 'rank_B': rB, 'rank_P': rP, 'rank_B+P': rBP,
               'radial_independent_of_B': rBr == rB + 1,
               'coker_equals_B_plus_P': (rBP == coker) and nB < 1e-9 and nP < 1e-9}
        if d == 6:
            npz = np.load(Path(__file__).resolve().parents[1] / 'data' / 'step80' / 'universal_pi.npz')
            # residual of ell after removing the Bianchi span, compared with the radial row (same projection)
            Q, _ = torch.linalg.qr(B.T)          # orthonormal basis of Bianchi row span (rank-revealing enough here)
            Ub, sb, _ = torch.linalg.svd(B.T, full_matrices=False); Ub = Ub[:, :rB]
            proj = lambda x: x - Ub @ (Ub.T @ x)
            r = proj(rad[0]); r = r / r.norm()
            cos = {}
            for key in npz.files:
                e = torch.tensor(npz[key], dtype=dt, device=dev)
                e_in_coker = float((e @ L).abs().max() / e.norm())
                pe = proj(e)
                cos[key] = {'|cos(ell mod B, radial mod B)|': float((pe @ r).abs() / pe.norm()),
                            'ell_in_coker_L6': e_in_coker, 'frac_ell_outside_B': float(pe.norm() / e.norm())}
            out['ell_match'] = cos
        rec[f'd{d}'] = out
        print(d, json.dumps(out), flush=True)
    (OUT / 'scalar_compat.json').write_text(json.dumps(rec, indent=1) + '\n')


if __name__ == '__main__':
    main()
