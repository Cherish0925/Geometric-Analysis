#!/usr/bin/env python3
"""Step 68d: flat cokernel structure of the Darboux-gauge Einstein system at every degree d<=8, and the exact
U(2)-invariant multiplier ell_d(E) = Delta^{(d-2)/2} [ (J d)_i (J d)_j E_ij - 1/2 Delta tr E ](0)  (d even).

For each d: rank of the anti-J flat linearized Ricci L_d : H_{d+2} -> E_d, dim Ann = coker, dim T (contracted
Bianchi rows), dim Q = Ann/T, number of U(2)-invariant classes in Q, exact (integer) check ell_d L_d = 0, and the
class of ell_d modulo T.  Saves ell_d in A02's layout (component-major over i<=j, monomials in TRing order).
Output: workspace/data/step68/cokernel_tower.json, ell_tower.npz
"""
import json
import numpy as np
import sympy as sp
import step68_flat_cokernel as F
import step68_multiplier_exact as M


def ell_vector(d):
    """integer vector of Delta^k [(Jd)(Jd)E - 1/2 Delta trE](0), k=(d-2)/2, times 2 to keep integrality."""
    k = (d - 2) // 2
    mons = F.mons_deg(d); mi = {m: q for q, m in enumerate(mons)}; n = len(mons)
    tix = {p: t for t, p in enumerate(TRI)}
    v = np.zeros(10 * n, dtype=object)
    import itertools
    def add(coef, i, j, der):
        cnt = [0] * 4
        for x in der: cnt[x] += 1
        m = tuple(cnt); fac = 1
        for x in m: fac *= sp.factorial(x)
        v[tix[(min(i, j), max(i, j))] * n + mi[m]] += coef * int(fac)
    for pairs in itertools.product(range(4), repeat=k):
        lap = tuple(x for p in pairs for x in (p, p))
        for i in range(4):
            for j in range(4):
                for a in range(4):
                    for b in range(4):
                        cJ = int(F.J0[i, a] * F.J0[j, b])
                        if cJ:
                            add(2 * cJ, i, j, (a, b) + lap)
        for i in range(4):
            for a in range(4):
                add(-1, i, i, (a, a) + lap)
    return np.array(v, dtype=np.int64)

TRI = F.TRI


def main():
    import flint
    rec = {}
    store = {}
    for d in range(0, 9):
        L = F.L_matrix(d)
        nE = L.shape[0]
        rk = flint.fmpz_mat(L.tolist()).rank()
        r = {'n_E': nE, 'n_H': L.shape[1], 'rank_L': int(rk), 'dim_Ann': int(nE - rk)}
        if d >= 1:
            B = F.bianchi_rows(d)
            rB = flint.fmpz_mat(B.tolist()).rank()
            r['dim_T'] = int(rB); r['dim_Q'] = int(nE - rk - rB)
            r['bianchi_in_Ann'] = bool(not np.any(B @ L))
        else:
            B = None; r['dim_T'] = 0; r['dim_Q'] = int(nE - rk)
        # invariant classes (float)
        Lf = L.astype(float)
        Ann = M.left_null(Lf) if r['dim_Ann'] else np.zeros((nE, 0))
        if B is not None and r['dim_T']:
            T = M.orth(B.T.astype(float)); PT = np.eye(nE) - T @ T.T
        else:
            T = np.zeros((nE, 0)); PT = np.eye(nE)
        if r['dim_Q']:
            Qb = M.orth(PT @ Ann)
            Ms = [M.action_matrix(X, d) for X in M.u2_basis()]
            Sys = np.vstack([PT @ Mx.T @ Qb for Mx in Ms])
            s = np.linalg.svd(Sys, compute_uv=False) if Sys.shape[1] else np.zeros(0)
            ninv = int(Qb.shape[1] - (s > 1e-9 * max(s.max(), 1)).sum())
            r['n_invariant_classes'] = ninv
        if d % 2 == 0 and d >= 2:
            ell = ell_vector(d)
            r['ell_exact_annihilates_L'] = bool(not np.any(ell @ L))
            cls = PT @ ell.astype(float)
            r['ell_class_norm_rel'] = float(np.linalg.norm(cls) / np.linalg.norm(ell.astype(float)))
            store[f'ell{d}'] = ell; store[f'ell{d}_class'] = cls
        rec[d] = r
        print(d, json.dumps(r), flush=True)
    (F.OUT / 'cokernel_tower.json').write_text(json.dumps(rec, indent=1) + '\n')
    np.savez(F.OUT / 'ell_tower.npz', **store)
    # compare degree-6 with A02's ell
    dd = np.load(F.A02 / 'data' / 'step80' / 'recon_F012_gen5_lam-5.npz')['ell']
    c = store['ell6_class']; print('cos(ell6 class, A02 ell) =', float(c @ dd / (np.linalg.norm(c) * np.linalg.norm(dd))))


if __name__ == '__main__':
    main()
