#!/usr/bin/env python3
"""Step 68h: homotopy continuation for the order-8 even AKE system at A02's gen5 (lam=-5) E6 solution.

Unknowns v=(H4,H6,H8) with H2 fixed (even germ; odd orders vanish by parity; H10 is then fixed by L8 since the
84 scalar-compatibility rows P(E8) are the only obstruction to solving E8 = L8 H10 + ...).
System: C(v) = (E2,E4,E6) = 0,  R(v) = P(E8)(v) = (1-t) R(v*)   for t: 0 -> 1.
Corrector: min-norm Gauss-Newton on the full stacked system.  Records the smallest singular value of the
restricted Jacobian G = DR|_{ker DC} along the path (a fold/critical value would show sigma_min -> 0), and the
final unreduced residuals, including E8 with H10 = -L8^+ E8.
Output: workspace/data/step68/order8_homotopy_<name>.json (+ .npy of final v)
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / 'S1003A02' / 'workspace' / 'scripts')); sys.path.insert(0, str(HERE))
from step78_real_tower import Tower
from step77_gn_germ import dev, dt
from step68_scalar_compatibility import P_matrix
from step68_cokernel_tower import ell_vector
import step68_flat_cokernel as F
OUT = HERE.parent / 'data' / 'step68'


def main(name, nsteps=40):
    base = HERE.parents[2] / 'S1003A02' / 'workspace' / 'data' / 'step80'
    dd = np.load(base / f'{name}.npz'); lam = float(name.split('lam')[-1])
    T = Tower(8, lam); T.degs = list(range(2, T.N + 1)); T.size = {e: 6 * len(T.mon_d[e]) for e in T.degs}
    tt = lambda a: torch.tensor(np.asarray(a), dtype=dt, device=dev)
    H2 = tt(dd['H2']); sizes = [T.size[4], T.size[6], T.size[8]]; n = sum(sizes)
    v0 = torch.cat([tt(dd['H4']), tt(dd['H6']), tt(dd['H8'])])
    scale = torch.cat([torch.full((s,), float(dd[k].std()), dtype=dt, device=dev) for s, k in zip(sizes, ['H4', 'H6', 'H8'])])
    P8n = P_matrix(8).astype(float); P8n = P8n / np.linalg.norm(P8n, axis=1, keepdims=True)
    P8 = tt(P8n)
    ell = ell_vector(8).astype(float); w = np.linalg.lstsq(P8n.T, ell, rcond=None)[0]; w /= np.linalg.norm(w)
    nC = 10 * (len(T.mon_d[2]) + len(T.mon_d[4]) + len(T.mon_d[6]))
    def jets(v, h10=None):
        J = {2: H2, 4: v[:sizes[0]], 6: v[sizes[0]:sizes[0] + sizes[1]], 8: v[sizes[0] + sizes[1]:]}
        if h10 is not None: J[10] = h10
        return J
    def CR(x):
        E = T.Evec(jets(v0 + scale * x), [2, 4, 6, 8])[0]
        return E[:nC], P8 @ E[nC:]
    eye = torch.eye(n, dtype=dt, device=dev)
    def jac(x):
        f = lambda y: torch.cat(CR(y))
        vj = torch.func.vmap(lambda e: torch.func.jvp(f, (x,), (e,))[1])
        return torch.cat([vj(eye[s:s + 64]).T for s in range(0, n, 64)], dim=1).cpu().numpy()
    x = torch.zeros(n, dtype=dt, device=dev)
    C0, R0 = CR(x); R0 = R0.cpu().numpy()
    rec = {'name': name, 'lam': lam, 'R0_norm': float(np.linalg.norm(R0)), 'R0_radial': float(w @ R0), 'path': []}
    print('R0', rec['R0_norm'], 'radial', rec['R0_radial'], flush=True)
    t0 = time.time()
    ts = np.linspace(0, 1, nsteps + 1)[1:]
    ok = True
    for t in ts:
        target = (1 - t) * R0
        for it in range(8):
            C, R = CR(x); C = C.cpu().numpy(); R = R.cpu().numpy()
            res = np.concatenate([C, R - target]); nr = np.linalg.norm(res)
            if nr < 1e-10 * max(1.0, np.linalg.norm(R0)): break
            Jm = jac(x)
            dx = np.linalg.lstsq(Jm, -res, rcond=1e-13)[0]
            x = x + tt(dx)
        Jm = jac(x); JC = Jm[:nC]; JR = Jm[nC:]
        U, s, Vt = np.linalg.svd(JC, full_matrices=True); rC = int((s > 1e-11 * s[0]).sum()); TV = Vt[rC:].T
        sg = np.linalg.svd(JR @ TV, compute_uv=False)
        C, R = CR(x); C = C.cpu().numpy(); R = R.cpu().numpy()
        step = {'t': float(t), 'C': float(np.linalg.norm(C)), 'R_minus_target': float(np.linalg.norm(R - target)),
                'R': float(np.linalg.norm(R)), 'radial': float(w @ R), 'sigma_min_G': float(sg[-1]), 'sigma_max_G': float(sg[0]),
                'rank_C': rC, 'x_norm': float(x.norm()), 'time': time.time() - t0}
        rec['path'].append(step); print(json.dumps(step), flush=True)
        (OUT / f'order8_homotopy_{name}.json').write_text(json.dumps(rec, indent=1) + '\n')
        if step['R_minus_target'] > 1e-3 * max(1.0, np.linalg.norm(R0)) or step['C'] > 1e-4:
            ok = False; rec['stopped'] = 'corrector failed'; break
    rec['completed'] = ok
    # unreduced check with H10 = -L8^+ E8
    v = v0 + scale * x
    E8 = T.Evec(jets(v), [8])[0].cpu().numpy()
    L8 = F.L_matrix(8).astype(float) / 2.0   # L_matrix stores 2 x (flat linearized Ricci)
    h10 = -np.linalg.lstsq(L8, E8, rcond=1e-12)[0]
    J = jets(v, tt(h10))
    rec['unreduced'] = {f'E{k}': float(T.Evec(J, [k])[0].norm()) for k in range(9)}
    rec['coef_norms'] = {d: float(J[d].norm()) for d in (2, 4, 6, 8, 10)}
    np.save(OUT / f'order8_homotopy_v_{name}.npy', v.cpu().numpy()); np.save(OUT / f'order8_homotopy_h10_{name}.npy', h10)
    (OUT / f'order8_homotopy_{name}.json').write_text(json.dumps(rec, indent=1) + '\n')
    print(json.dumps({k: rec[k] for k in ['completed', 'unreduced', 'coef_norms']}), flush=True)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 40)
