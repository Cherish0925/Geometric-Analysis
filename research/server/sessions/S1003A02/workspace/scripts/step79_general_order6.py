#!/usr/bin/env python3
"""Step 79: order-6 real compatibility of AKE germs at a torsion zero WITHOUT the even ansatz.

Darboux gauge (Omega standard), g = exp(H), H anti-J symmetric, H = H2 + H3 + ... (torsion zero at 0).
Degree count: the x-degree-k part of E = Ric(e^H) - lam e^H collects jet products of total degree k+2
(Ricci) or k (lam).  With H2, H3 FIXED and unknowns u = (H4, H5, H6, H7), the orders 1..5 are AFFINE in u
(no product of two unknowns has total degree <= 7), and order 6 is
     E6 = L6 H8 + affine(u) + Q(H4, H4),       Q universal (flat), independent of H2, H3, lam.
So, with u = u0 + N y the general solution of orders 1..5 and C6 the cokernel of the flat L6,
     Psi(y) = C6^T E6 = c + J y + y^T H y / 2   (exactly quadratic).
The joint quadratic range / linear absorption / scalar reduction is then done as in step78_phi6.scalar_reduce.
For H3 = 0 this reproduces the even-ansatz Phi6 (odd unknowns decouple); H3 != 0 is the genuinely new case.

Modes for H2: d6 (Step-77 jet, lam=-3 only), jet (prescribed (c,S,A) on the cone; torsion-free part min-norm),
kahler (random torsion-free admissible H2), random (random real quadric point).
H3: zero, or t * (random admissible odd jet: orders 1 and 3 solvable).
Output: workspace/data/step79/gen6_<tag>.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
from step77_gn_germ import dev, dt, jet_coords
from step78_real_tower import Tower, load_h2_from_d6
from step78_certificate import random_quadric_H2, null_left, null_right
from step78_phi6 import scalar_reduce
from step78_quad6 import lm

import os
OUT = Path(__file__).resolve().parents[1] / 'data' / os.environ.get('STEP79_OUT', 'step79')
OUT.mkdir(exist_ok=True)


_CACHE = {}


class TowerAll(Tower):
    def __init__(self, K, lam):
        super().__init__(K, lam)
        self.degs = list(range(2, self.N + 1))
        self.size = {d: 6 * len(self.mon_d[d]) for d in self.degs}


def zeros(T, skip=()):
    return {d: torch.zeros(T.size[d], dtype=dt, device=dev) for d in T.degs if d not in skip}


def batched_cols(f, n, b0, chunk=96):
    """columns f(e_j) - b0 for an affine f on R^n."""
    cols = []
    eye = torch.eye(n, dtype=dt, device=dev)
    vf = torch.func.vmap(f)
    for s in range(0, n, chunk):
        cols.append((vf(eye[s:s + chunk]) - b0).T)
    return torch.cat(cols, dim=1)


def h2_tools(T):
    z2 = torch.zeros(T.size[2], dtype=dt, device=dev)
    zz = zeros(T, skip=(2,))
    E0 = lambda h: T.Evec({2: h, **zz}, [0])[0]
    L0 = torch.func.jacfwd(E0)(z2)
    h0 = -torch.linalg.pinv(L0) @ E0(z2)
    N0 = null_right(L0)
    def tor_vec(h):
        D = T.torsion({2: h, **zz})          # 4 x 4 real
        M0 = D[0] + 0j; M = torch.stack([torch.complex(D[0], D[1]), torch.complex(D[2], D[3])])
        C = torch.stack([torch.stack([(M[k, 0] - 1j * M[k, 1]) / 2, (M[k, 2] - 1j * M[k, 3]) / 2]) for k in range(2)])
        B = torch.stack([torch.stack([(M[k, 0] + 1j * M[k, 1]) / 2, (M[k, 2] + 1j * M[k, 3]) / 2]) for k in range(2)])
        v = torch.cat([C.reshape(-1), B.reshape(-1)])
        return torch.cat([v.real, v.imag])
    return h0, N0, tor_vec


def make_H2(T, mode, lam, rng, jet=None, scale=1.0, wscale=0.0):
    h0, N0, tor_vec = h2_tools(T)
    if mode == 'd6':
        return load_h2_from_d6(Path(__file__).resolve().parents[1] / 'data' / 'step77_gn_D6_even_lam-3.0_s0.pt', T)[2]
    if mode == 'random':
        return random_quadric_H2(T, lam, rng, scale)[0]
    Tm = batched_cols(lambda x: tor_vec(h0 + N0 @ x), N0.shape[1], tor_vec(h0), chunk=N0.shape[1])
    if mode == 'kahler':
        K = null_right(Tm)
        x = K @ torch.tensor(rng.standard_normal(K.shape[1]) * scale, dtype=dt, device=dev)
        return h0 + N0 @ x
    if mode == 'jet':
        c, S, A = jet
        C = c * np.eye(2); B = np.array(S) + np.array(A)
        v = np.concatenate([C.reshape(-1), B.reshape(-1)])
        tgt = torch.tensor(np.concatenate([v.real, v.imag]), dtype=dt, device=dev) - tor_vec(h0)
        x = torch.linalg.lstsq(Tm, tgt.unsqueeze(1)).solution[:, 0]
        x = torch.linalg.pinv(Tm) @ tgt
        res = float((Tm @ x - tgt).norm())
        assert res < 1e-9, ('jet not realised', res)
        if wscale:
            K = null_right(Tm)
            w = torch.tensor(rng.standard_normal(K.shape[1]), dtype=dt, device=dev)
            x = x + wscale * K @ (w / w.norm())
        return h0 + N0 @ x
    raise ValueError(mode)


def admissible_H3(T, H2, rng):
    """random H3 such that orders 1 and 3 are solvable (unknowns H3, H5; H2 fixed)."""
    n3, n5 = T.size[3], T.size[5]
    base = zeros(T, skip=(2, 3, 5))
    f = lambda v: T.Evec({2: H2, 3: v[:n3], 5: v[n3:], **base}, [1, 3])[0]
    b0 = f(torch.zeros(n3 + n5, dtype=dt, device=dev))
    A = batched_cols(f, n3 + n5, b0)
    assert float(b0.norm()) < 1e-10
    N = null_right(A, 1e-10)
    # random element, H3 part, normalised to unit Frobenius norm of coefficients
    v = N @ torch.tensor(rng.standard_normal(N.shape[1]), dtype=dt, device=dev)
    h3 = v[:n3]
    # remove the pure-gauge part? (kept; gauge is harmless).  dims for record
    rk3 = int(torch.linalg.matrix_rank(N[:n3]))
    return h3 / h3.norm(), {'dim_adm_(H3,H5)': int(N.shape[1]), 'rank_H3_projection': rk3}


def reduce_general(T, H2, H3, even=False, tol=1e-10):
    t0 = time.time()
    U = [4, 6] if even else [4, 5, 6, 7]
    orders = [2, 4] if even else [1, 2, 3, 4, 5]
    sizes = [T.size[d] for d in U]; n = sum(sizes)
    base = zeros(T, skip=tuple(U) + (2, 3))
    def jets(u, h8=None):
        out = {2: H2, 3: H3, **base}; o = 0
        for d, s in zip(U, sizes):
            out[d] = u[o:o + s]; o += s
        if h8 is not None:
            out[8] = h8
        return out
    F = lambda u: T.Evec(jets(u), orders)[0]
    z = torch.zeros(n, dtype=dt, device=dev)
    b = F(z)
    A = batched_cols(F, n, b)
    ur = torch.randn(n, dtype=dt, device=dev)
    aff_err = float((F(ur) - b - A @ ur).norm() / F(ur).norm())
    Ap = torch.linalg.pinv(A, rtol=tol)
    u0 = -Ap @ b
    lin_resid = float((A @ u0 + b).norm())
    N = null_right(A, tol)
    ny = N.shape[1]
    # order 6
    E6 = lambda u: T.Evec(jets(u), [6])[0]
    n8 = T.size[8]
    zall = zeros(T)
    n4 = T.size[4]
    if 'Qc' not in _CACHE:      # L6 and the H4*H4 form are flat/universal (independent of H2, H3, lambda)
        f8 = lambda h: T.Evec({**zall, 8: h}, [6])[0]
        L6 = batched_cols(f8, n8, f8(torch.zeros(n8, dtype=dt, device=dev)))
        C6 = null_left(L6, tol)
        E6q = lambda h: T.Evec({**zall, 4: h}, [6])[0]
        Bt = []
        for i in range(n4):
            ei = torch.zeros(n4, dtype=dt, device=dev); ei[i] = 1.0
            gi = lambda h, ei=ei: torch.func.jvp(E6q, (h,), (ei,))[1]
            Bt.append(torch.func.jacfwd(gi)(torch.zeros(n4, dtype=dt, device=dev)) / 2)   # B(e_i, e_j), 840 x n4
        Bt = torch.stack(Bt, dim=1)            # 840 x n4 x n4
        _CACHE['C6'] = C6; _CACHE['Qc'] = torch.einsum('ra,aij->rij', C6.T, Bt)
    C6 = _CACHE['C6']; Qc = _CACHE['Qc']
    # pieces in y
    c = C6.T @ E6(u0)
    Jcols = []
    vj = torch.func.vmap(lambda v: torch.func.jvp(E6, (u0,), (v,))[1])
    for s in range(0, ny, 64):
        Jcols.append(vj(N[:, s:s + 64].T).T)
    Jy = C6.T @ torch.cat(Jcols, dim=1)
    N4 = N[:sizes[0]]
    Hy = 2 * torch.einsum('ia,rij,jb->rab', N4, Qc, N4)     # Psi = c + J y + y^T Hy y / 2 (Hy = 2 Q)
    # exactness check
    yr = torch.randn(ny, dtype=dt, device=dev)
    ex = C6.T @ E6(u0 + N @ yr)
    mod = c + Jy @ yr + 0.5 * torch.einsum('rab,a,b->r', Hy, yr, yr)
    quad_err = float((ex - mod).norm() / ex.norm())
    # row reduction (remove identically-zero rows such as Bianchi)
    G = torch.outer(c, c) + Jy @ Jy.T + torch.einsum('rab,sab->rs', Hy, Hy)
    ev, V = torch.linalg.eigh(G)
    r = int((ev > 1e-10 * ev[-1]).sum())
    Ur = V[:, -r:]
    cr = (Ur.T @ c).cpu().numpy(); Jr = (Ur.T @ Jy).cpu().numpy()
    Hr = torch.einsum('rs,rab->sab', Ur, Hy).cpu().numpy()
    rec = {'U': U, 'orders_lin': orders, 'n_unknowns': n, 'rank_A': n - ny, 'ny': ny, 'affine_err': aff_err,
           'lin_resid': lin_resid, 'coker_L6': int(C6.shape[1]), 'n_rows_nontrivial': r,
           'G_eigs_top': [float(x) for x in ev[-(r + 2):].cpu()], 'quad_model_relerr': quad_err, 'time': time.time() - t0}
    return rec, cr, Jr, Hr


def analyse(cr, Jr, Hr, rng, nlm=40):
    sr = scalar_reduce(cr, Jr, Hr)
    # LM fallback on the reduced polynomial system
    best = np.inf
    for s in range(nlm):
        y0 = (10 ** rng.uniform(-2, 1)) * rng.standard_normal(Jr.shape[1])
        _, nf, _ = lm(cr, Jr, Hr, y0, iters=200)
        best = min(best, nf)
    sr['lm_min'] = float(best)
    sr['|c|'] = float(np.linalg.norm(cr))
    return sr


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--lam', type=float, default=-3.0)
    ap.add_argument('--h2', default='d6')
    ap.add_argument('--jet', default=None, help='json [c,[S11,S12,S22],a] complex as [re,im]')
    ap.add_argument('--h3scales', default='0')
    ap.add_argument('--nh3', type=int, default=1)
    ap.add_argument('--even', action='store_true')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--nlm', type=int, default=30)
    ap.add_argument('--tag', default='test')
    ap.add_argument('--save', action='store_true')
    ap.add_argument('--wscale', type=float, default=0.0, help='random torsion-free (W^- / gauge) shift of H2 in jet mode')
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed); torch.manual_seed(a.seed)
    T = TowerAll(6, a.lam)
    jet = None
    if a.jet:
        js = json.loads(a.jet)
        cc = complex(*js[0]); s11, s12, s22 = [complex(*x) for x in js[1]]; aa = complex(*js[2])
        jet = (cc, [[s11, s12], [s12, s22]], [[0, aa], [-aa, 0]])
    H2 = make_H2(T, a.h2, a.lam, rng, jet, a.scale, a.wscale)
    jc = jet_coords(T.torsion({2: H2, **zeros(T, skip=(2,))}))
    tn = float(np.sqrt(4 * jc['c2'] + 2 * jc['S2'] + 2 * jc['A2']))
    out = {'args': vars(a), 'jet': jc, 'torsion_norm': tn, 'lam_over_torsion': a.lam / tn if tn > 1e-12 else None, 'runs': []}
    print('H2', a.h2, {k: round(v, 5) for k, v in jc.items()}, 'tn', tn, flush=True)
    scales = [float(x) for x in a.h3scales.split(',')]
    for ih in range(a.nh3):
        h3u, info3 = admissible_H3(T, H2, rng)
        for t in scales:
            if t == 0 and ih > 0:
                continue
            rec, cr, Jr, Hr = reduce_general(T, H2, t * h3u, even=a.even)
            rec.update(info3); rec['h3_index'] = ih; rec['h3_scale'] = t
            rec['analysis'] = analyse(cr, Jr, Hr, rng, a.nlm)
            out['runs'].append(rec)
            an = rec['analysis']
            print('h3', ih, 't', t, {k: rec[k] for k in ('ny', 'lin_resid', 'coker_L6', 'n_rows_nontrivial', 'quad_model_relerr', 'affine_err')},
                  {k: an.get(k) for k in ('joint_quad_rank', 'rank_J_on_common_kernel', 'n_scalar', 'definite', 'c', 'Phi6', 'Phi6_over_c', 'lm_min')},
                  round(rec['time'], 1), flush=True)
            (OUT / f'gen6_{a.tag}.json').write_text(json.dumps(out, indent=1) + '\n')
            if a.save:
                np.savez(OUT / f'gen6_{a.tag}_h{ih}_t{t}.npz', c=cr, J=Jr, H=Hr)


if __name__ == '__main__':
    main()
