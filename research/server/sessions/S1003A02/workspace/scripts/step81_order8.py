#!/usr/bin/env python3
"""Step 81: is the REAL formal AKE problem at a nondegenerate torsion zero solvable through ORDER 8?

Even germs (H3 = H5 = H7 = H9 = 0; odd orders then vanish by parity), Darboux gauge, g = exp(H), lam fixed.
Degree count (x-degree k of E = Ric(e^H) - lam e^H collects jet products of total degree k+2 / k):
   orders 2, 4 : affine in u = (H4, H6)          ->  u = u0 + N y
   order 6     : E6 = L6 H8 + R6(y)               (R6 quadratic in y through H4*H4)
   order 8     : E8 = L8 H10 + R8(y, H8)          (linear in H8 via H2*H8, quadratic in y)
With H8 = -L6^+ R6(y) + K6 w  (K6 = ker L6) the remaining conditions are
   r6(y)   = C6^T R6(y)            (35 nontrivial rows, the rest vanish by Bianchi)
   r8(y,w) = C8^T R8(y, H8(y,w))   (84 excess rows + Bianchi rows that vanish automatically)
both exactly quadratic in (y, w).  Real solvability is tested by Levenberg-Marquardt on R = (r6, r8) from the
order-6 real solution y* of step80 (Phi6 <= 0 branch), several perturbed starts, and verified by the
UNREDUCED residuals E0..E8 of the assembled jet (H10 = -L8^+ E8).
Controls: Kahler 2-jet (KE germs exist to all orders: must converge), and a Phi6 > 0 jet (must fail at order 6).
Output: workspace/data/step81/order8_<tag>.json
Run: CUDA_VISIBLE_DEVICES=0 python step81_order8.py --njets 6 --lam -1 --seed 81
"""
import json, sys, os, time, argparse
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step81')
import step79_general_order6 as G
from step77_gn_germ import jet_coords
from step80_reconstruct import construct
from step80_F012_scan import random_cone_jet

dev, dt = G.dev, G.dt
OUT = Path(__file__).resolve().parents[1] / 'data' / 'step81'
OUT.mkdir(exist_ok=True)


def svd_null(A, tol=1e-10, side='right'):
    U, s, Vh = torch.linalg.svd(A, full_matrices=True)
    r = int((s > tol * s[0]).sum())
    return (Vh[r:].T if side == 'right' else U[:, r:]), r


class Flat:
    """flat (H2-independent) top maps L6: H8 -> E6 and L8: H10 -> E8 and their cokernels."""
    def __init__(self, T):
        zall = G.zeros(T)
        f8 = lambda h: T.Evec({**zall, 8: h}, [6])[0]
        f10 = lambda h: T.Evec({**zall, 10: h}, [8])[0]
        self.L6 = G.batched_cols(f8, T.size[8], f8(torch.zeros(T.size[8], dtype=dt, device=dev)))
        self.L8 = G.batched_cols(f10, T.size[10], f10(torch.zeros(T.size[10], dtype=dt, device=dev)))
        self.C6, r6 = svd_null(self.L6, side='left'); self.K6, _ = svd_null(self.L6, side='right')
        self.C8, r8 = svd_null(self.L8, side='left')
        self.L6p = torch.linalg.pinv(self.L6, rtol=1e-10); self.L8p = torch.linalg.pinv(self.L8, rtol=1e-10)
        self.info = {'rank_L6': r6, 'coker_L6': int(self.C6.shape[1]), 'ker_L6': int(self.K6.shape[1]),
                     'rank_L8': r8, 'coker_L8': int(self.C8.shape[1])}


_QC = {}


def flat_Q4(T, C6, chunk=24):
    """E6 restricted to H = H4 is exactly quadratic (Ricci H4*H4 at degree 6; no lam term at degree 6):
    Q(a,b) = (E6q(a+b) - E6q(a-b))/4.  Universal (H2-, lam-independent); cached in memory and on disk."""
    if 'Qc' in _QC:
        return _QC['Qc']
    f = OUT / 'flat_Q4_C6.pt'
    if f.exists():
        _QC['Qc'] = torch.load(f).to(dev); return _QC['Qc']
    n4 = T.size[4]; zall = G.zeros(T)
    E6q = lambda h: T.Evec({**zall, 4: h}, [6])[0]
    vE = torch.func.vmap(E6q)
    I = torch.eye(n4, dtype=dt, device=dev)
    Q = torch.zeros(C6.shape[1], n4, n4, dtype=dt, device=dev)
    for i in range(n4):
        for s in range(i, n4, chunk):
            B = I[s:s + chunk]
            v = (vE(I[i] + B) - vE(I[i] - B)) / 4            # (m, 840)
            q = C6.T @ v.T                                    # 259 x m
            Q[:, i, s:s + chunk] = q; Q[:, s:s + chunk, i] = q
    _QC['Qc'] = Q; torch.save(Q.cpu(), f)
    return Q


def even_pieces(T, Fl, H2, tol=1e-10):
    U = [4, 6]; sizes = [T.size[4], T.size[6]]; n = sum(sizes)
    base = G.zeros(T, skip=(2, 4, 6))
    def jets(u, h8=None, h10=None):
        out = {**base, 2: H2, 4: u[:sizes[0]], 6: u[sizes[0]:]}
        if h8 is not None: out[8] = h8
        if h10 is not None: out[10] = h10
        return out
    F = lambda u: T.Evec(jets(u), [2, 4])[0]
    z = torch.zeros(n, dtype=dt, device=dev)
    b = F(z); A = G.batched_cols(F, n, b)
    u0 = -torch.linalg.pinv(A, rtol=tol) @ b
    N, rA = svd_null(A, tol); ny = N.shape[1]
    E6 = lambda u: T.Evec(jets(u), [6])[0]
    # quadratic model of r6 in y (exact: quadratic), reduced to nontrivial rows
    C6 = Fl.C6
    c = C6.T @ E6(u0)
    vj = torch.func.vmap(lambda v: torch.func.jvp(E6, (u0,), (v,))[1])
    Jy = C6.T @ torch.cat([vj(N[:, s:s + 64].T).T for s in range(0, ny, 64)], dim=1)
    # Hessian: E6 quadratic part only through H4*H4 -> polarise on N4 columns
    n4 = sizes[0]; N4 = N[:n4]
    Qc = flat_Q4(T, C6)                                            # 259 x n4 x n4, E6q(h) = h^T Q h (exactly quadratic)
    Hy = 2 * torch.einsum('ia,rij,jb->rab', N4, Qc, N4)            # full second derivative in y
    Gm = torch.outer(c, c) + Jy @ Jy.T + torch.einsum('rab,sab->rs', Hy, Hy)
    ev, V = torch.linalg.eigh(Gm)
    rr = int((ev > 1e-10 * ev[-1]).sum()); Ur = V[:, -rr:]
    pc = dict(c=Ur.T @ c, J=Ur.T @ Jy, H=torch.einsum('rs,rab->sab', Ur, Hy))
    # exactness check of the quadratic model
    yr = torch.randn(ny, dtype=dt, device=dev) * 0.1
    ex = C6.T @ E6(u0 + N @ yr); mod = c + Jy @ yr + 0.5 * torch.einsum('rab,a,b->r', Hy, yr, yr)
    info = {'ny': ny, 'rank_A': rA, 'rows6_nontrivial': rr, 'quad_model_relerr': float((ex - mod).norm() / ex.norm())}
    return pc, dict(u0=u0, N=N, jets=jets, E6=E6), info


def residual_fn(T, Fl, base):
    u0, N, jets, E6 = base['u0'], base['N'], base['jets'], base['E6']
    ny = N.shape[1]
    def R(x):
        y, w = x[:ny], x[ny:]
        u = u0 + N @ y
        e6 = E6(u)
        h8 = -Fl.L6p @ e6 + Fl.K6 @ w
        r6 = Fl.C6.T @ e6
        e8 = T.Evec(jets(u, h8), [8])[0]
        r8 = Fl.C8.T @ e8
        return torch.cat([r6, r8])
    return R


def jac(R, x, chunk=64):
    n = x.shape[0]; I = torch.eye(n, dtype=dt, device=dev)
    vj = torch.func.vmap(lambda v: torch.func.jvp(R, (x,), (v,))[1])
    return torch.cat([vj(I[s:s + chunk]).T for s in range(0, n, chunk)], dim=1)


def lm(R, x0, iters=150, tol=1e-13, chunk=64, log=None):
    x = x0.clone(); r = R(x); nr = float(r.norm()); mu = None; hist = [nr]
    for it in range(iters):
        if nr < tol: break
        Jm = jac(R, x, chunk)
        U_, s, Vh = torch.linalg.svd(Jm, full_matrices=False)
        if mu is None: mu = float(s[0]) * 1e-3
        Ur = U_.T @ r
        while True:
            step = -(Vh.T @ (s * Ur / (s ** 2 + mu ** 2)))
            xn = x + step; rn = R(xn); nn = float(rn.norm())
            if nn < nr:
                x, r, nr = xn, rn, nn; mu = max(mu / 3, 1e-14 * float(s[0])); break
            mu *= 4
            if mu > 1e12 * float(s[0]): break
        hist.append(nr)
        if log and it % 10 == 0: print('   lm', it, '%.3e' % nr, 'mu %.1e' % mu, flush=True)
        if mu > 1e12 * float(s[0]): break
    Jm = jac(R, x, chunk)
    sv = torch.linalg.svdvals(Jm)
    rk = int((sv > 1e-9 * sv[0]).sum())
    return x, hist, {'jac_rank_at_end': rk, 'n_rows': int(Jm.shape[0]), 'n_cols': int(Jm.shape[1])}


def unreduced(T, Fl, base, x):
    u0, N, jets, E6 = base['u0'], base['N'], base['jets'], base['E6']
    ny = N.shape[1]; y, w = x[:ny], x[ny:]
    u = u0 + N @ y; e6 = E6(u); h8 = -Fl.L6p @ e6 + Fl.K6 @ w
    e8 = T.Evec(jets(u, h8), [8])[0]; h10 = -Fl.L8p @ e8
    J = jets(u, h8, h10)
    out = {f'E{k}': float(T.Evec(J, [k])[0].norm()) for k in range(9)}
    out['coef_norm'] = float(torch.cat([J[d] for d in (2, 4, 6, 8, 10)]).norm())
    return out


def run_case(T, Fl, tag, H2, rng, nstarts=4, log=True):
    t0 = time.time()
    rec = {'tag': tag, 'lam': T.lam}
    rec['jet'] = jet_coords(T.torsion({2: H2, **G.zeros(T, skip=(2,))}))
    pc, base, info = even_pieces(T, Fl, H2); rec.update(info)
    try:
        sol, cinfo = construct({k: v for k, v in pc.items()})
    except ValueError:
        sol, cinfo = None, {'n_surv': 0, 'note': 'no surviving scalar row (all rows absorbed linearly)'}
    rec['order6'] = cinfo
    ny = base['N'].shape[1]; nw = Fl.K6.shape[1]
    Rfull = residual_fn(T, Fl, base)
    # variable projection: r8 is affine in w with a CONSTANT matrix M (H8 couples only to H2 and lam at order 8)
    n6 = Fl.C6.shape[1]
    xz = torch.zeros(ny + nw, dtype=dt, device=dev)
    Mw = jac(lambda w: Rfull(torch.cat([xz[:ny], w]))[n6:], torch.zeros(nw, dtype=dt, device=dev))
    Um, sm, _ = torch.linalg.svd(Mw, full_matrices=True)
    Mrank = int((sm > 1e-10 * sm[0]).sum()); Qp = Um[:, Mrank:]
    Mp = torch.linalg.pinv(Mw, rtol=1e-10)
    def R(y):
        r = Rfull(torch.cat([y, torch.zeros(nw, dtype=dt, device=dev)]))
        return torch.cat([r[:n6], Qp.T @ r[n6:]])
    def full_x(y):
        r = Rfull(torch.cat([y, torch.zeros(nw, dtype=dt, device=dev)]))
        return torch.cat([y, -Mp @ r[n6:]])
    y_star = torch.tensor(sol['y'], dtype=dt, device=dev) if sol is not None else torch.zeros(ny, dtype=dt, device=dev)
    runs = []
    for s in range(nstarts):
        pert = 0.0 if s == 0 else 0.3 * float(y_star.norm() + 1) * 10 ** rng.uniform(-2, 0)
        y0 = y_star + pert * torch.tensor(rng.standard_normal(ny), dtype=dt, device=dev) / np.sqrt(ny)
        r0 = R(y0)
        yv, hist, li = lm(R, y0, log=log)
        r = R(yv); x = full_x(yv)
        rr = {'start': s, 'pert': pert, 'res0': float(r0.norm()), 'res0_r6': float(r0[:Fl.C6.shape[1]].norm()),
              'res_end': hist[-1], 'r6_end': float(r[:Fl.C6.shape[1]].norm()), 'r8_end': float(r[Fl.C6.shape[1]:].norm()),
              'iters': len(hist) - 1, **li}
        if hist[-1] < 1e-8:
            rr['unreduced'] = unreduced(T, Fl, base, x)
        runs.append(rr)
        print(tag, json.dumps(rr), flush=True)
        if hist[-1] < 1e-10 and s >= 1: break
    rec['runs'] = runs; rec['time'] = time.time() - t0
    rec['M_rank_w_to_r8'] = Mrank
    (OUT / f'order8_{tag}.json').write_text(json.dumps(rec, indent=1, default=float) + '\n')
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--njets', type=int, default=6)
    ap.add_argument('--lam', type=float, default=-1.0)
    ap.add_argument('--seed', type=int, default=81)
    ap.add_argument('--controls', type=int, default=1)
    ap.add_argument('--nstarts', type=int, default=4)
    ap.add_argument('--f012', type=str, default='')
    a = ap.parse_args()
    T = G.TowerAll(8, a.lam); Fl = Flat(T)
    print('flat', Fl.info, flush=True)
    rng = np.random.default_rng(a.seed)
    if a.controls:
        H2k = G.make_H2(T, 'kahler', a.lam, rng, None, 1.0)
        run_case(T, Fl, f'kahler_lam{a.lam:g}_s{a.seed}', H2k, rng, nstarts=2)
    if a.f012:
        r42 = np.random.default_rng(42); gens = [random_cone_jet(r42, 'generic') for _ in range(8)]
        for gi in [int(t) for t in a.f012.split(',')]:
            c, S, A = gens[gi]
            jet = (complex(c), [[complex(S[i, j]) for j in range(2)] for i in range(2)], [[complex(A[i, j]) for j in range(2)] for i in range(2)])
            H2 = G.make_H2(T, 'jet', a.lam, rng, jet, 1.0, 0.0)
            run_case(T, Fl, f'F012gen{gi}_lam{a.lam:g}', H2, rng, nstarts=a.nstarts)
        return
    done = 0; tried = 0
    while done < a.njets and tried < 6 * a.njets:
        tried += 1
        c, S, A = random_cone_jet(rng, 'generic')
        jet = (complex(c), [[complex(S[i, j]) for j in range(2)] for i in range(2)], [[complex(A[i, j]) for j in range(2)] for i in range(2)])
        H2 = G.make_H2(T, 'jet', a.lam, rng, jet, 1.0, 0.0)
        tag = f'gen_lam{a.lam:g}_s{a.seed}_{tried}'
        rec = run_case(T, Fl, tag, H2, rng, nstarts=a.nstarts)
        if rec['order6'].get('Phi6', 1) <= 0:
            done += 1


if __name__ == '__main__':
    main()
