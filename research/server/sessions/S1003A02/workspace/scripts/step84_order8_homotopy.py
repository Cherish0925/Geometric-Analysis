#!/usr/bin/env python3
"""Step 84: order-8 real solvability at a nondegenerate AKE torsion zero by homotopy continuation.

Reduced system (step81_order8, variable projection over w in ker L6):
   R(y) = ( r6(y) ; Qp^T r8(y) ),   y in R^361,  91 nontrivial rows, Jacobian full rank (Step 84).
Homotopy from the order-6 root y* (Step 80 construction):
   F(y,t) = R(y) - (1-t) * (0 ; Qp^T r8(y*)),   t: 0 -> 1.
Corrector: minimum-norm Gauss-Newton (pseudo-inverse with relative cutoff), adaptive step in t.
At t = 1 the full unreduced residuals E0..E8 are evaluated with H8 = -L6^+ E6 + K6 w(y) and H10 = -L8^+ E8.

Output: workspace/data/step84/order8_homotopy_<tag>.json
Run:    python step84_order8_homotopy.py --gen 5 --lam -5
"""
import json, sys, os, time, argparse
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step84')
import step79_general_order6 as G
import step81_order8 as O
from step80_reconstruct import construct
from step80_F012_scan import random_cone_jet

dev, dt = G.dev, G.dt
OUT = Path(__file__).resolve().parents[1] / 'data' / 'step84'
OUT.mkdir(exist_ok=True, parents=True)


def mn_step(J, r, rcut=1e-9):
    U, s, Vh = torch.linalg.svd(J, full_matrices=False)
    keep = s > rcut * s[0]
    return -(Vh[keep].T @ ((U[:, keep].T @ r) / s[keep])), int(keep.sum()), float(s[keep][-1] / s[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gen', type=int, default=5)
    ap.add_argument('--lam', type=float, default=-5.0)
    ap.add_argument('--dt0', type=float, default=0.05)
    ap.add_argument('--tol', type=float, default=5e-8)
    a = ap.parse_args()
    t0 = time.time()
    T = G.TowerAll(8, a.lam); Fl = O.Flat(T)
    rng = np.random.default_rng(81)
    r42 = np.random.default_rng(42); gens = [random_cone_jet(r42, 'generic') for _ in range(8)]
    c, S, A = gens[a.gen]
    jet = (complex(c), [[complex(S[i, j]) for j in range(2)] for i in range(2)], [[complex(A[i, j]) for j in range(2)] for i in range(2)])
    H2 = G.make_H2(T, 'jet', a.lam, rng, jet, 1.0, 0.0)
    pc, base, info = O.even_pieces(T, Fl, H2)
    sol, cinfo = construct({k: v for k, v in pc.items()})
    rec = {'tag': f'gen{a.gen}_lam{a.lam:g}', 'info': info, 'order6': cinfo}
    print('order6', json.dumps(cinfo, default=float), flush=True)
    ny = base['N'].shape[1]; nw = Fl.K6.shape[1]; n6 = Fl.C6.shape[1]
    Rfull = O.residual_fn(T, Fl, base)
    Mw = O.jac(lambda w: Rfull(torch.cat([torch.zeros(ny, dtype=dt, device=dev), w]))[n6:], torch.zeros(nw, dtype=dt, device=dev))
    Um, sm, _ = torch.linalg.svd(Mw, full_matrices=True)
    Mrank = int((sm > 1e-10 * sm[0]).sum()); Qp = Um[:, Mrank:]; Mp = torch.linalg.pinv(Mw, rtol=1e-10)
    zw = torch.zeros(nw, dtype=dt, device=dev)
    def R(y):
        r = Rfull(torch.cat([y, zw])); return torch.cat([r[:n6], Qp.T @ r[n6:]])
    y = torch.tensor(sol['y'], dtype=dt, device=dev)
    r0 = R(y); tgt = r0.clone(); tgt[:n6] = 0
    print('start |r6|=%.2e |r8p|=%.3e' % (float(r0[:n6].norm()), float(r0[n6:].norm())), flush=True)
    t, h = 0.0, a.dt0; path = []
    while t < 1.0 and time.time() - t0 < 5000:
        tn = min(1.0, t + h)
        F = lambda yy: R(yy) - (1 - tn) * tgt
        yn = y.clone(); ok = False; hist = []
        for it in range(8):
            r = F(yn); nr = float(r.norm()); hist.append(nr)
            if nr < (a.tol if tn == 1.0 else 5e-8): ok = True; break
            Jm = O.jac(R, yn)
            st, rk, cond = mn_step(Jm, r)
            yn = yn + st
            if it >= 2 and hist[-1] > 0.5 * hist[-2]:
                break
        if ok:
            y, t = yn, tn; path.append({'t': t, 'res': nr, 'newton': len(hist), 'rank': rk if 'rk' in dir() else None,
                                        'smin_rel': cond if 'cond' in dir() else None, 'ynorm': float(y.norm())})
            print('t=%.4f res=%.2e it=%d |y|=%.1f' % (t, nr, len(hist), float(y.norm())), flush=True)
            h = min(0.25, h * 1.5)
        else:
            h /= 2
            print('  reject tn=%.4f hist=%s -> h=%.3g' % (tn, ['%.1e' % x for x in hist], h), flush=True)
            if h < 1e-5: break
    rec['path'] = path; rec['t_reached'] = t; rec['M_rank_w_to_r8'] = Mrank
    if t == 1.0:
        Jm = O.jac(R, y); sv = torch.linalg.svdvals(Jm)
        rec['jac_rank_end'] = int((sv > 1e-9 * sv[0]).sum()); rec['smin_rel_end'] = float(sv[rec['jac_rank_end'] - 1] / sv[0])
        r = Rfull(torch.cat([y, zw])); w = -Mp @ r[n6:]
        x = torch.cat([y, w])
        rec['reduced_residual_full_w'] = float(Rfull(x).norm())
        rec['unreduced'] = O.unreduced(T, Fl, base, x)
        torch.save({'y': y.cpu(), 'w': w.cpu()}, OUT / f'order8_homotopy_{rec["tag"]}.pt')
        print('unreduced', json.dumps(rec['unreduced']), flush=True)
    rec['time'] = time.time() - t0
    (OUT / f'order8_homotopy_{rec["tag"]}.json').write_text(json.dumps(rec, indent=1, default=float) + '\n')


if __name__ == '__main__':
    main()
