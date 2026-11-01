#!/usr/bin/env python3
"""Step 78: exact elimination of the linear part of the order<=6 AKE germ system at a fixed torsion jet H2,
and real Newton on the residual quadratic conditions.

For fixed H2 (E0 = 0 and on the order-2 quadric):
  E2 = L2 H4 + n2                         -> H4 = H4p + N2 x
  E4 = L4 H6 + M4 H4 + n4                 -> coker(L4) conditions linear in x -> x = x0 + Z y ;  H6p(y) = -L4^+ (...)
  E6 = L6 H8 + A6 H6 + G(H2,H4)           (G quadratic in H4)
       coker(L6) conditions: C6^T A6 N4 w + C6^T[A6-part of H6p(y) + G(H4(y))] = 0 , w = ker L4 part of H6
  left null mu of C6^T E6(.,w-direction)  -> Psi(y) = mu^T C6^T E6(H2, H4(y), H6p(y), 0)  = 0
Psi is quadratic in y.  We report dim y, #Psi, rank DPsi, and run real Newton (min-norm) from many starts.
Output: workspace/data/step78/red6_<tag>.json and .pt (Psi data)
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
from step77_gn_germ import dev, dt, jet_coords
from step78_real_tower import Tower, load_h2_from_d6
from step78_certificate import random_quadric_H2, null_left, null_right

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step78'


class Reduced:
    def __init__(self, T, H2, tol=1e-10):
        self.T = T; self.H2 = H2
        n4, n6, n8 = T.size[4], T.size[6], T.size[8]
        z = lambda n: torch.zeros(n, dtype=dt, device=dev)
        self.z = z
        E = lambda h4, h6, h8, k: T.Evec({2: H2, 4: h4, 6: h6, 8: h8}, [k])[0]
        self.E = E
        # order 2
        n2v = E(z(n4), z(n6), z(n8), 2)
        L2 = torch.func.jacfwd(lambda h: E(h, z(n6), z(n8), 2))(z(n4))
        L2p = torch.linalg.pinv(L2, rtol=tol)
        H4p = -L2p @ n2v
        assert float((L2 @ H4p + n2v).norm()) < 1e-8 * max(1, float(n2v.norm())), 'order 2 not solvable'
        N2 = null_right(L2, tol)
        # order 4
        L4 = torch.func.jacfwd(lambda h: E(z(n4), h, z(n8), 4))(z(n6))
        e4 = lambda h4: E(h4, z(n6), z(n8), 4)        # = M4 h4 + n4 (linear)
        C4 = null_left(L4, tol)
        M = torch.func.jacfwd(lambda x: C4.T @ e4(H4p + N2 @ x))(z(N2.shape[1]))
        b = C4.T @ e4(H4p)
        Mp = torch.linalg.pinv(M, rtol=tol)
        x0 = -Mp @ b
        self.order4_resid = float((M @ x0 + b).norm())
        Z = null_right(M, tol)
        self.H4of = lambda y: H4p + N2 @ (x0 + Z @ y)
        L4p = torch.linalg.pinv(L4, rtol=tol)
        self.H6of = lambda y: -L4p @ e4(self.H4of(y))
        N4 = null_right(L4, tol)
        # order 6
        L6 = torch.func.jacfwd(lambda h: E(z(n4), z(n6), h, 6))(z(n8))
        C6 = null_left(L6, tol)
        e6 = lambda y, w: C6.T @ E(self.H4of(y), self.H6of(y) + N4 @ w, z(n8), 6)
        Aw = torch.func.jacfwd(lambda w: e6(z(Z.shape[1]), w))(z(N4.shape[1]))
        mu = null_left(Aw, tol)
        self.Psi = lambda y: mu.T @ e6(y, z(N4.shape[1]))
        self.dims = {'ker_L2': int(N2.shape[1]), 'order4_conditions': int(C4.shape[1]), 'rank_M4': int(N2.shape[1] - Z.shape[1]),
                     'dim_y': int(Z.shape[1]), 'coker_L6': int(C6.shape[1]), 'rank_w_map': int(C6.shape[1] - mu.shape[1]),
                     'n_Psi': int(mu.shape[1]), 'order4_resid': self.order4_resid}
        self.ny = Z.shape[1]
        self.full = lambda y: T.Evec({2: H2, 4: self.H4of(y), 6: self.H6of(y), 8: z(n8)}, [2, 4])[0]


def newton(R, y, iters=60, tol=1e-12, rcond=1e-10):
    hist = []
    for it in range(iters):
        r = R.Psi(y); nr = float(r.norm()); hist.append(nr)
        if nr < tol:
            break
        J = torch.func.jacfwd(R.Psi)(y)
        U, s, Vh = torch.linalg.svd(J, full_matrices=False)
        k = s > rcond * s[0]
        step = -(Vh[k].T @ ((U[:, k].T @ r) / s[k]))
        t = 1.0
        while t > 1e-6 and float(R.Psi(y + t * step).norm()) >= nr:
            t /= 2
        y = y + t * step
    J = torch.func.jacfwd(R.Psi)(y)
    s = torch.linalg.svdvals(J)
    r = R.Psi(y)
    grad = float((J.T @ r).norm())
    return y, hist, s.cpu().numpy(), grad


def main(lam=-3.0, h2='random', seed=0, nh2=3, starts=6, scale=1.0, yscale=1.0, tag=None):
    rng = np.random.default_rng(seed); torch.manual_seed(seed)
    T = Tower(6, lam)
    out = {'lam': lam, 'seed': seed, 'scale': scale, 'runs': []}
    for a in range(nh2):
        if h2 == 'd6':
            H2 = load_h2_from_d6(OUT.parent / 'step77_gn_D6_even_lam-3.0_s0.pt', T)[2]; info = {}
        else:
            H2, info = random_quadric_H2(T, lam, rng, scale)
        zero = {d: torch.zeros(T.size[d], dtype=dt, device=dev) for d in T.degs if d != 2}
        jc = jet_coords(T.torsion({2: H2, **zero}))
        t0 = time.time()
        R = Reduced(T, H2)
        rec = {'h2_index': a, 'jet': jc, 'dims': R.dims, 'setup_time': time.time() - t0, 'starts': []}
        print('H2', a, {k: round(v, 4) for k, v in jc.items()}, R.dims, flush=True)
        y0 = torch.zeros(R.ny, dtype=dt, device=dev)
        J0 = torch.func.jacfwd(R.Psi)(y0)
        rec['rank_DPsi_at_0'] = int((torch.linalg.svdvals(J0) > 1e-9 * torch.linalg.svdvals(J0)[0]).sum())
        for s in range(starts):
            y = y0 if s == 0 else yscale * (2 ** (s % 3)) * torch.randn(R.ny, dtype=dt, device=dev)
            y, hist, sv, grad = newton(R, y)
            lin = float(R.full(y).norm())
            rec['starts'].append({'final': hist[-1], 'n_it': len(hist), 'hist_tail': hist[-5:], 'grad_JtPsi': grad,
                                  'sv_min': float(sv[-1]), 'sv_max': float(sv[0]), 'lin_orders_resid': lin, 'y_norm': float(y.norm())})
            print('   start', s, 'final %.3e its %d grad %.2e svmin %.2e |y| %.2e lin %.1e' % (hist[-1], len(hist), grad, sv[-1], float(y.norm()), lin), flush=True)
            if hist[-1] < 1e-10:
                Hj = {2: H2, 4: R.H4of(y), 6: R.H6of(y)}
                torch.save({d: v.cpu() for d, v in Hj.items()}, OUT / f'red6_sol_lam{lam}_s{seed}_h{a}_st{s}.pt')
        out['runs'].append(rec)
    tag = tag or f'lam{lam}_{h2}_s{seed}_sc{scale}'
    (OUT / f'red6_{tag}.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--lam', type=float, default=-3.0)
    ap.add_argument('--h2', default='random')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--nh2', type=int, default=3)
    ap.add_argument('--starts', type=int, default=6)
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--yscale', type=float, default=1.0)
    a = ap.parse_args()
    main(a.lam, a.h2, a.seed, a.nh2, a.starts, a.scale, a.yscale)
