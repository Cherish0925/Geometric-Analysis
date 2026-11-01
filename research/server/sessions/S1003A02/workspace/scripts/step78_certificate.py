#!/usr/bin/env python3
"""Step 78: real-obstruction certificate for the order-<=6 AKE germ system at a fixed torsion jet H2.

System (even ansatz, Darboux gauge, H2 fixed with E0 = 0 and the order-2 quadric satisfied):
    F(H4,H6,H8) = (E2, E4, E6) = c + J4 H4 + Jtop (H6,H8) + Q(H4,H4)       (exact: Q only in E6 rows)
A real solution fails to exist if some multiplier l (with l^T Jtop = 0) makes
    f_l(H4) = l.c + (l.J4) H4 + H4^T (l.Q) H4  >= eps (1+|H4|^2)  for all H4,
i.e. the (1+210)x(1+210) matrix M(l) = [[l.c, (l.J4)/2],[(l.J4)^T/2, l.Q]] is positive definite.
We maximise t = lambda_min(M(l)) over l = Lambda beta, ||beta||_2 <= 1 (SDP via cvxpy/Clarabel).
t > 0 (robustly)  => no real formal solution through order 6 with this H2.
t = 0             => no certificate of this (degree-2 multiplier) type.
Also: H2 sampler on the real quadric (E0 = 0 affine + one scalar quadratic), multi-start GN at fixed H2.
Output: workspace/data/step78/cert_<tag>.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from step77_gn_germ import dev, dt, jet_coords
from step78_real_tower import Tower, load_h2_from_d6, gn_solve, per_order

DATA = Path(__file__).resolve().parents[1] / 'data'
OUT = DATA / 'step78'


def null_left(A, tol=1e-10):
    U, s, Vh = torch.linalg.svd(A, full_matrices=True)
    r = int((s > tol * s[0]).sum())
    return U[:, r:]


def null_right(A, tol=1e-10):
    U, s, Vh = torch.linalg.svd(A, full_matrices=True)
    r = int((s > tol * s[0]).sum())
    return Vh[r:].T


def random_quadric_H2(T, lam, rng, scale=1.0, tries=200):
    """real H2 with E0 = 0 and the single order-2 excess condition satisfied."""
    n2 = T.size[2]
    z = lambda: torch.zeros(n2, dtype=dt, device=dev)
    zeros = {d: torch.zeros(T.size[d], dtype=dt, device=dev) for d in T.degs if d != 2}
    E0 = lambda h: T.Evec({2: h, **zeros}, [0])[0]
    L0 = torch.func.jacfwd(E0)(z())
    b0 = E0(z())                               # = -lam delta
    h0 = -torch.linalg.pinv(L0) @ b0
    N0 = null_right(L0)
    # order-2 coker of L2 (wrt H4)
    E2of = lambda h4, h2: T.Evec({2: h2, 4: h4, **{d: zeros[d] for d in zeros if d != 4}}, [2])[0]
    L2 = torch.func.jacfwd(lambda h4: E2of(h4, h0))(torch.zeros(T.size[4], dtype=dt, device=dev))
    C2 = null_left(L2)                         # 100 x 17
    # find the single non-Bianchi functional by sampling
    samp = []
    for _ in range(30):
        h = h0 + N0 @ torch.tensor(rng.standard_normal(N0.shape[1]) * scale, dtype=dt, device=dev)
        samp.append(C2.T @ E2of(torch.zeros(T.size[4], dtype=dt, device=dev), h))
    S = torch.stack(samp)
    U, s, Vh = torch.linalg.svd(S)
    ell = C2 @ Vh[0]
    sv_ratio = float(s[1] / s[0])
    f = lambda h: float(ell @ E2of(torch.zeros(T.size[4], dtype=dt, device=dev), h))
    for _ in range(tries):
        a = h0 + N0 @ torch.tensor(rng.standard_normal(N0.shape[1]) * scale, dtype=dt, device=dev)
        b = N0 @ torch.tensor(rng.standard_normal(N0.shape[1]) * scale, dtype=dt, device=dev)
        f0, f1, fm = f(a), f(a + b), f(a - b)
        A2 = (f1 + fm - 2 * f0) / 2; B1 = (f1 - fm) / 2
        disc = B1 * B1 - 4 * A2 * f0
        if disc < 0 or abs(A2) < 1e-12:
            continue
        t = (-B1 + np.sqrt(disc)) / (2 * A2)
        h = a + t * b
        return h, {'bianchi_sv_ratio': sv_ratio, 'excess_value': f(h)}
    raise RuntimeError('no real quadric point found')


def build_system(T, H2):
    zero = {d: torch.zeros(T.size[d], dtype=dt, device=dev) for d in T.degs}
    orders = [2, 4, 6]
    n4, n6, n8 = T.size[4], T.size[6], T.size[8]

    def F(h4, top):
        return T.Evec({2: H2, 4: h4, 6: top[:n6], 8: top[n6:]}, orders)[0]

    z4 = zero[4]; ztop = torch.zeros(n6 + n8, dtype=dt, device=dev)
    c = F(z4, ztop)
    J4 = torch.func.jacfwd(lambda h: F(h, ztop))(z4)
    Jt = torch.func.jacfwd(lambda t: F(z4, t))(ztop)
    Lam = null_left(Jt)
    return F, c, J4, Jt, Lam


def certificate(T, H2, solver='CLARABEL'):
    import cvxpy as cp
    t0 = time.time()
    F, c, J4, Jt, Lam = build_system(T, H2)
    n4 = T.size[4]
    ztop = torch.zeros(Jt.shape[1], dtype=dt, device=dev)
    z4 = torch.zeros(n4, dtype=dt, device=dev)
    # check exact structure: F(h4,top) - c - J4 h4 - Jt top is quadratic in h4 only
    h = torch.randn(n4, dtype=dt, device=dev); tp = torch.randn(Jt.shape[1], dtype=dt, device=dev)
    q1 = F(h, tp) - c - J4 @ h - Jt @ tp; q2 = F(2 * h, tp) - c - 2 * J4 @ h - Jt @ tp
    struct_err = float((q2 - 4 * q1).norm() / max(q1.norm(), 1e-30))
    top_indep = float(((F(h, tp) - F(h, 2 * tp)) - (Jt @ (-tp))).norm())
    m = Lam.shape[1]
    # Hessians of beta-basis functionals l_a = Lam[:,a]
    Hs = []
    for a in range(m):
        la = Lam[:, a]
        Ha = torch.func.hessian(lambda x: la @ F(x, ztop))(z4)
        Hs.append(Ha / 2)
    Hs = torch.stack(Hs).cpu().numpy()            # quadratic form coefficients (x^T H x)
    lc = (Lam.T @ c).cpu().numpy(); lJ = (Lam.T @ J4).cpu().numpy()
    beta = cp.Variable(m); t = cp.Variable()
    def Mexpr():
        top = cp.reshape(lc @ beta, (1, 1), order='C')
        lin = cp.reshape(lJ.T @ beta / 2, (n4, 1), order='C')
        Q = sum(beta[a] * Hs[a] for a in range(m))
        return cp.bmat([[top, lin.T], [lin, Q]])
    M = Mexpr()
    Ms = (M + M.T) / 2
    prob = cp.Problem(cp.Maximize(t), [Ms - t * np.eye(n4 + 1) >> 0, cp.norm(beta, 2) <= 1])
    prob.solve(solver=solver)
    b = beta.value
    Mv = np.block([[np.array([[lc @ b]]), (lJ.T @ b / 2)[None]], [(lJ.T @ b / 2)[:, None], np.tensordot(b, Hs, 1)]])
    Mv = (Mv + Mv.T) / 2
    ev = np.linalg.eigvalsh(Mv)
    # also: best PSD-ness of pure quadratic part alone
    return {'m_multipliers': int(m), 'struct_err_quadratic_check': struct_err, 'top_linear_check': top_indep,
            'sdp_status': prob.status, 'sdp_t': float(t.value) if t.value is not None else None,
            'M_eig_min': float(ev[0]), 'M_eig_max': float(ev[-1]), 'M_eig_low': [float(x) for x in ev[:8]],
            'time': time.time() - t0}, b, Lam


def main(lam=-3.0, h2='d6', seed=0, scale=1.0, gn_starts=0, tag=None):
    rng = np.random.default_rng(seed); torch.manual_seed(seed)
    T = Tower(6, lam)
    info = {}
    if h2 == 'd6':
        jets = load_h2_from_d6(DATA / 'step77_gn_D6_even_lam-3.0_s0.pt', T); H2 = jets[2]
    else:
        H2, info = random_quadric_H2(T, lam, rng, scale)
    zero = {d: torch.zeros(T.size[d], dtype=dt, device=dev) for d in T.degs if d != 2}
    jc = jet_coords(T.torsion({2: H2, **zero}))
    print('H2 jet', jc, info, flush=True)
    res, b, Lam = certificate(T, H2)
    print(json.dumps(res, indent=1), flush=True)
    out = {'lam': lam, 'h2': h2, 'seed': seed, 'scale': scale, 'jet': jc, 'h2_info': info, 'cert': res}
    if gn_starts:
        gns = []
        for s in range(gn_starts):
            jets = {2: H2}
            for d in T.degs:
                if d != 2:
                    jets[d] = 0.1 * torch.randn(T.size[d], dtype=dt, device=dev)
            jets, hist, sv = gn_solve(T, jets, [4, 6, 8], [2, 4, 6], iters=40, log=False)
            gns.append({'final': hist[-1], 'per_order': per_order(T, jets), 'n_it': len(hist)})
            print('GN start', s, hist[-1], flush=True)
        out['gn'] = gns
    tag = tag or f'lam{lam}_{h2}_s{seed}'
    OUT.mkdir(exist_ok=True)
    (OUT / f'cert_{tag}.json').write_text(json.dumps(out, indent=1) + '\n')
    np.save(OUT / f'cert_{tag}_beta.npy', b)
    torch.save(H2.cpu(), OUT / f'cert_{tag}_H2.pt')


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--lam', type=float, default=-3.0)
    ap.add_argument('--h2', default='d6')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--gn', type=int, default=0)
    a = ap.parse_args()
    main(a.lam, a.h2, a.seed, a.scale, a.gn)
