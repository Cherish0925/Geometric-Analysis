#!/usr/bin/env python3
"""Step 68: exact flat structure of the order-six Einstein cokernel in A02's Darboux convention.

Convention (A02 step78_real_tower): g = exp(H), H = sum_a B_a U_a(x), B_a = anti_basis() (anti-J symmetric),
E vector of degree d = stack over (i<=j) of the coefficients E_ij[m], m in degree-d monomials ordered as in TRing.
L_d : H_{d+2} -> E_d is the flat linearized Ricci operator
   dRic_ij = 1/2 (d_k d_i h_kj + d_k d_j h_ki - Lap h_ij - d_i d_j tr h).
We compute L6 in exact integers, its left null space (rank over Q via flint), the contracted-Bianchi rows
   B(E)_j = d_i E_ij - 1/2 d_j trE,
and compare with A02's saved C6 and ell.  Output: workspace/data/step68/flat_cokernel.json
"""
import itertools, json, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
A02 = HERE.parents[2] / 'S1003A02' / 'workspace'
OUT = HERE.parent / 'data' / 'step68'; OUT.mkdir(parents=True, exist_ok=True)
J0 = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
TRI = [(i, j) for i in range(4) for j in range(i, 4)]


def mons_deg(d):
    return [e for e in itertools.product(range(d + 1), repeat=4) if sum(e) == d]


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
    return np.array(out, dtype=int)


def dmon(m, k):
    """d/dx_k x^m = c x^m'"""
    if m[k] == 0:
        return 0, None
    mm = list(m); c = mm[k]; mm[k] -= 1
    return c, tuple(mm)


def ddmon(m, k, l):
    c1, m1 = dmon(m, k)
    if not c1:
        return 0, None
    c2, m2 = dmon(m1, l)
    if not c2:
        return 0, None
    return c1 * c2, m2


def L_matrix(d, sym_full=False):
    """integer matrix (2*) L_d : coefficients of H_{d+2} -> E_d (factor 2 kept to stay integral)."""
    src = mons_deg(d + 2); tgt = mons_deg(d); ti = {m: q for q, m in enumerate(tgt)}
    if sym_full:
        basis = []
        for (i, j) in TRI:
            E = np.zeros((4, 4), dtype=int); E[i, j] = 1; E[j, i] = 1; basis.append(E)
        basis = np.array(basis)
    else:
        basis = anti_basis()
    nb = len(basis)
    M = np.zeros((10 * len(tgt), nb * len(src)), dtype=np.int64)
    for a in range(nb):
        h = basis[a]
        trh = int(np.trace(h))
        for q, m in enumerate(src):
            col = a * len(src) + q
            for t, (i, j) in enumerate(TRI):
                # 2 dRic_ij = d_k d_i h_kj + d_k d_j h_ki - d_k d_k h_ij - d_i d_j tr h, h = basis * x^m
                for k in range(4):
                    for (coef, (p, r)) in ((h[k, j], (k, i)), (h[k, i], (k, j)), (-h[i, j], (k, k))):
                        if coef:
                            c, mm = ddmon(m, p, r)
                            if c:
                                M[t * len(tgt) + ti[mm], col] += coef * c
                if trh:
                    c, mm = ddmon(m, i, j)
                    if c:
                        M[t * len(tgt) + ti[mm], col] -= trh * c
    return M


def bianchi_rows(d):
    """integer matrix Bmat (4*n_{d-1} x 10*n_d): (2*) [d_i E_ij - 1/2 d_j trE]."""
    src = mons_deg(d); tgt = mons_deg(d - 1); ti = {m: q for q, m in enumerate(tgt)}
    tix = {p: t for t, p in enumerate(TRI)}
    def comp(i, j):
        return tix[(min(i, j), max(i, j))]
    B = np.zeros((4 * len(tgt), 10 * len(src)), dtype=np.int64)
    for j in range(4):
        for q, m in enumerate(src):
            for i in range(4):
                c, mm = dmon(m, i)
                if c:
                    B[j * len(tgt) + ti[mm], comp(i, j) * len(src) + q] += 2 * c
            for i in range(4):
                c, mm = dmon(m, j)
                if c:
                    B[j * len(tgt) + ti[mm], comp(i, i) * len(src) + q] -= c
    return B


def qrank(M):
    import flint
    return flint.fmpz_mat(M.tolist()).rank()


def main():
    d = np.load(A02 / 'data' / 'step80' / 'recon_F012_gen5_lam-5.npz')
    mons = d['mons']
    assert [tuple(int(x) for x in mons[i]) for i in d['mon_d6']] == mons_deg(6), 'monomial order mismatch'
    ell = d['ell']; C6 = d['C6']
    out = {}
    for full in (False, True):
        L = L_matrix(6, sym_full=full)
        out[f'rank_L6_{"sym" if full else "antiJ"}'] = int(qrank(L))
    L = L_matrix(6)
    B = bianchi_rows(6)
    out['rank_bianchi_rows'] = int(qrank(B))
    out['bianchi_kills_full_sym_image'] = bool(not np.any(B @ L_matrix(6, True)))
    out['bianchi_kills_antiJ_image'] = bool(not np.any(B @ L))
    Lf = L.astype(float)
    out['ell_annihilates_my_L6_rel'] = float(np.linalg.norm(ell @ Lf) / (np.linalg.norm(ell) * np.linalg.norm(Lf)))
    out['C6_annihilates_my_L6_rel'] = float(np.linalg.norm(C6.T @ Lf) / np.linalg.norm(Lf))
    print(json.dumps(out, indent=1))
    (OUT / 'flat_cokernel.json').write_text(json.dumps(out, indent=1) + '\n')
    np.savez(OUT / 'flat_mats.npz', L6=L, B6=B)


if __name__ == '__main__':
    main()
