#!/usr/bin/env python3
"""Step 80: is the surviving order-6 scalar condition a UNIVERSAL linear functional of the degree-6 Ricci
coefficients?  Also: weighted-homogeneity test of Phi6.

For each case (H2 from a prescribed cone jet (c,S,A) at lambda, H3 = 0), run the general order-6 reduction
(step79_general_order6.reduce_general), then form the full functional
      ell = C6 @ Ur @ pi    (a vector on the 840-dim space of degree-6 coefficients of E = Ric - lam e^H)
where pi is the unique (up to scale) row combination annihilating J on the common kernel of the quadratic
forms.  Compare ell across jets (|cos|), and Phi6 computed with ell normalised to unit length.
Weighted homogeneity: x -> mu x sends H_k -> mu^k H_k, lam -> mu^2 lam, so (c,S,A,lam) -> mu^2 (c,S,A,lam)
must give ell unchanged and Phi6 -> mu^8 Phi6 (with ell held fixed).
Output: workspace/data/step80/universal_pi.json, ell vectors in universal_pi.npz
Run: CUDA_VISIBLE_DEVICES=1 python step80_universal_pi.py
"""
import json, sys, time, os
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault('STEP79_OUT', 'step80')
import step79_general_order6 as G
from step77_gn_germ import jet_coords

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step80'
OUT.mkdir(exist_ok=True)


def reduce_full(T, H2, H3, tol=1e-10):
    """like G.reduce_general but returns full-space (c, J, H) = C6^T(...) and C6."""
    U = [4, 5, 6, 7]; orders = [1, 2, 3, 4, 5]
    sizes = [T.size[d] for d in U]; n = sum(sizes)
    base = G.zeros(T, skip=tuple(U) + (2, 3))
    def jets(u):
        out = {2: H2, 3: H3, **base}; o = 0
        for d, s in zip(U, sizes):
            out[d] = u[o:o + s]; o += s
        return out
    F = lambda u: T.Evec(jets(u), orders)[0]
    z = torch.zeros(n, dtype=G.dt, device=G.dev)
    b = F(z); A = G.batched_cols(F, n, b)
    u0 = -torch.linalg.pinv(A, rtol=tol) @ b
    lin_resid = float((A @ u0 + b).norm())
    N = G.null_right(A, tol); ny = N.shape[1]
    E6 = lambda u: T.Evec(jets(u), [6])[0]
    if 'Qc' not in G._CACHE:
        G.reduce_general(T, H2, H3)          # fills the universal cache
    C6 = G._CACHE['C6']; Qc = G._CACHE['Qc']
    c = C6.T @ E6(u0)
    vj = torch.func.vmap(lambda v: torch.func.jvp(E6, (u0,), (v,))[1])
    Jy = C6.T @ torch.cat([vj(N[:, s:s + 64].T).T for s in range(0, ny, 64)], dim=1)
    N4 = N[:sizes[0]]
    Hy = 2 * torch.einsum('ia,rij,jb->rab', N4, Qc, N4)
    Gm = torch.outer(c, c) + Jy @ Jy.T + torch.einsum('rab,sab->rs', Hy, Hy)
    ev, V = torch.linalg.eigh(Gm)
    r = int((ev > 1e-10 * ev[-1]).sum()); Ur = V[:, -r:]
    c = Ur.T @ c; Jy = Ur.T @ Jy; Hy = torch.einsum('rs,rab->sab', Ur, Hy)
    return c, Jy, Hy, C6 @ Ur, {'ny': ny, 'lin_resid': lin_resid, 'rows': r}


def surviving_functional(c, J, H, tol=1e-9):
    """pi in coker-coordinates (259) : pi.H vanishes on common kernel, pi.J vanishes on common kernel."""
    c, J, H = c.cpu().numpy(), J.cpu().numpy(), H.cpu().numpy()
    m, n = J.shape
    Hs = np.concatenate([H[i] for i in range(m)], axis=1)          # n x (m n)
    Uq, s, _ = np.linalg.svd(Hs, full_matrices=False)
    r = int((s > tol * s[0]).sum())
    P, K = Uq[:, :r], Uq[:, r:]
    JK = J @ K                                                     # m x (n-r)
    Ul, sl, _ = np.linalg.svd(JK, full_matrices=True)
    rw = int((sl > tol * sl[0]).sum())
    Pi = Ul[:, rw:]                                                # m x (m-rw): includes trivial (Bianchi) rows
    # remove functionals that vanish identically on (c, J, H)
    M = np.concatenate([Pi.T @ c[:, None], Pi.T @ J, np.einsum('ri,rab->iab', Pi, H).reshape(Pi.shape[1], -1)], axis=1)
    Um, sm, _ = np.linalg.svd(M, full_matrices=False)
    keep = sm > 1e-9 * (sm[0] if sm.size else 1)
    Pin = Pi @ Um[:, keep]                                         # nontrivial surviving functionals
    rec = {'quad_rank': r, 'rank_JK': rw, 'n_surv_raw': int(Pi.shape[1]), 'n_surv': int(Pin.shape[1])}
    return Pin, P, rec, (c, J, H)


def phi6_of(pi, P, c, J, H):
    cr = float(pi @ c); jr = (pi @ J) @ P
    Hr = P.T @ np.einsum('i,iab->ab', pi, H) @ P
    ev = np.linalg.eigvalsh(Hr)
    if ev[-1] < 0:
        cr, jr, Hr, ev, pi = -cr, -jr, -Hr, -ev[::-1], -pi
    out = {'Hr_eig_min': float(ev[0]), 'Hr_eig_max': float(ev[-1]), 'definite': bool(ev[0] > 0), 'c': cr}
    if ev[0] > 0:
        out['Phi6'] = float(cr - 0.5 * jr @ np.linalg.solve(Hr, jr))
    # residual of pi.J on common kernel (should be ~0)
    return out, pi


def cone_jet(c, S, a):
    S = np.array(S, dtype=complex); A = np.array([[0, a], [-a, 0]], dtype=complex)
    return complex(c), S, A


def main():
    cases = []
    rng = np.random.default_rng(80)
    # generic cone jets
    for k in range(2):
        cz = lambda: complex(*rng.standard_normal(2))
        c = cz(); S = np.array([[cz(), cz()], [0, cz()]]); S[1, 0] = S[0, 1]
        amod = np.sqrt((np.sum(abs(S) ** 2) + 8 * abs(c) ** 2) / 2); a = amod * np.exp(1j * rng.uniform(0, 6.3))
        cases.append((f'gen{k}', (c, S, a), -1.0))
    cases.append(('a01pt', (1, [[2, 1], [1, 1 + 1j]], 2 + 2j), -1.0))
    mu2 = 0.5
    c0, S0, a0 = cases[0][1]
    cases.append(('gen0_scaled', (mu2 * c0, mu2 * np.array(S0), mu2 * a0), -1.0 * mu2))
    res = {'cases': []}; ells = {}
    Ts = {}
    for tag, (c, S, a), lam in cases:
        t0 = time.time()
        if lam not in Ts:
            Ts[lam] = G.TowerAll(6, lam)
        T = Ts[lam]
        cc, SS, AA = cone_jet(c, S, a)
        H2 = G.make_H2(T, 'jet', lam, np.random.default_rng(0), (cc, SS, AA), 1.0, 0.0)
        H3 = torch.zeros(T.size[3], dtype=G.dt, device=G.dev)
        jc = jet_coords(T.torsion({2: H2, **G.zeros(T, skip=(2,))}))
        cF, JF, HF, C6, info = reduce_full(T, H2, H3)
        Pin, P, rec, (cn, Jn, Hn) = surviving_functional(cF, JF, HF)
        rec.update(info); rec['jet'] = jc; rec['lam'] = lam; rec['tag'] = tag
        if Pin.shape[1] == 1:
            pi = Pin[:, 0]
            ell = C6.cpu().numpy() @ pi
            nrm = np.linalg.norm(ell); pi = pi / nrm; ell = ell / nrm
            ph, pi = phi6_of(pi, P, cn, Jn, Hn)
            ell = C6.cpu().numpy() @ pi
            rec.update(ph); ells[tag] = ell
        res['cases'].append(rec); rec['time'] = time.time() - t0
        print(tag, {k: rec.get(k) for k in ('quad_rank', 'rank_JK', 'n_surv_raw', 'n_surv', 'definite', 'c', 'Phi6', 'Hr_eig_min')}, round(rec['time'], 1), flush=True)
        tags = list(ells)
        res['cos'] = {f'{x}|{y}': float(abs(ells[x] @ ells[y])) for i, x in enumerate(tags) for y in tags[i + 1:]}
        print('cos', res['cos'], flush=True)
        (OUT / 'universal_pi.json').write_text(json.dumps(res, indent=1, default=str) + '\n')
        np.savez(OUT / 'universal_pi.npz', **ells)
    if 'gen0' in ells and 'gen0_scaled' in ells:
        p0 = [r for r in res['cases'] if r['tag'] == 'gen0'][0].get('Phi6'); p1 = [r for r in res['cases'] if r['tag'] == 'gen0_scaled'][0].get('Phi6')
        res['homogeneity_ratio_Phi6_scaled_over_mu8'] = p1 / (mu2 ** 4 * p0) if (p0 and p1) else None
        print('homogeneity ratio (should be 1):', res['homogeneity_ratio_Phi6_scaled_over_mu8'])
        (OUT / 'universal_pi.json').write_text(json.dumps(res, indent=1, default=str) + '\n')


if __name__ == '__main__':
    main()
