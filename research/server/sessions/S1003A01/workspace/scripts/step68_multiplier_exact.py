#!/usr/bin/env python3
"""Step 68b: identify A02's universal order-six multiplier ell exactly.

Ann = left null space of the flat anti-J linearized Ricci operator L6 (dim 259),
T   = contracted-Bianchi rows (dim 224, contained in Ann),
Q   = Ann / T  (dim 35 = quartic scalar compatibility coefficients).
We compute the U(2)-invariant classes in Q (dual action of u(2) on degree-6 symmetric-tensor polynomials),
compare with ell (A02 stores the representative in Ann orthogonal to T), and test natural formulas:
   c1(E) = Delta^2 [ (J d)_i (J d)_j E_ij ](0),  c2(E) = Delta^3 tr E (0),  c3(E) = Delta^2 [d_i d_j E_ij](0).
Output: workspace/data/step68/multiplier_exact.json
"""
import json, itertools
from pathlib import Path
import numpy as np
import sympy as sp
import step68_flat_cokernel as F

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / 'data' / 'step68'
J0 = F.J0; TRI = F.TRI


def orth(A, tol=1e-10):
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    r = int((s > tol * s[0]).sum()); return U[:, :r]


def left_null(A, tol=1e-10):
    U, s, Vt = np.linalg.svd(A, full_matrices=True)
    r = int((s > tol * s[0]).sum()); return U[:, r:]


def action_matrix(X, d):
    """M_X on degree-d symmetric-tensor polynomials E (TRI storage): (X.E) = X^T E + E X + (dE/dx) X x."""
    mons = F.mons_deg(d); mi = {m: q for q, m in enumerate(mons)}; n = len(mons)
    tix = {p: t for t, p in enumerate(TRI)}
    comp = lambda i, j: tix[(min(i, j), max(i, j))]
    M = np.zeros((10 * n, 10 * n))
    for t, (i, j) in enumerate(TRI):
        for q, m in enumerate(mons):
            col = t * n + q
            # E = e_ij-sym * x^m ; full symmetric matrix S with S_ij=S_ji=1
            S = np.zeros((4, 4)); S[i, j] = 1; S[j, i] = 1
            R = X.T @ S + S @ X
            for a in range(4):
                for b in range(a, 4):
                    if R[a, b]:
                        M[comp(a, b) * n + q, col] += R[a, b]
            # transport term: sum_k d_k(x^m) (X x)_k = sum_{k,l} X_kl x_l d_k x^m
            for k in range(4):
                c, mm = F.dmon(m, k)
                if not c: continue
                for l in range(4):
                    if X[k, l]:
                        m2 = list(mm); m2[l] += 1
                        M[t * n + mi[tuple(m2)], col] += X[k, l] * c
    return M


def u2_basis():
    out = []
    for a in range(4):
        for b in range(a + 1, 4):
            X = np.zeros((4, 4)); X[a, b] = 1; X[b, a] = -1; out.append(X)
    A = np.array([(X @ J0 - J0 @ X).ravel() for X in out]).T
    N = sp.Matrix(A).nullspace()
    return [sum(float(v[t]) * out[t] for t in range(6)) for v in N]


def deriv_functional(d, ops):
    """functional on degree-d E: sum over terms (coef, comp(i,j), multiset of derivative indices) at 0.
    ops: list of (coef, i, j, tuple_of_derivative_indices) with full symmetric E_ij (off-diagonal summed both ways)."""
    mons = F.mons_deg(d); mi = {m: q for q, m in enumerate(mons)}; n = len(mons)
    tix = {p: t for t, p in enumerate(TRI)}
    v = np.zeros(10 * n)
    for coef, i, j, der in ops:
        cnt = [0] * 4
        for k in der: cnt[k] += 1
        m = tuple(cnt)
        fac = np.prod([float(sp.factorial(x)) for x in m])
        v[tix[(min(i, j), max(i, j))] * n + mi[m]] += coef * fac
    return v


def natural_functionals():
    # c1 = Delta^2 (J d)_i (J d)_j E_ij ;  (J d)_i = J_ia d_a
    ops1, ops2, ops3 = [], [], []
    for i in range(4):
        for j in range(4):
            for a in range(4):
                for b in range(4):
                    cJ = J0[i, a] * J0[j, b]
                    for c in range(4):
                        for e in range(4):
                            if cJ: ops1.append((cJ, i, j, (a, b, c, c, e, e)))
                            if a == i and b == j: ops3.append((1, i, j, (a, b, c, c, e, e)))
    for i in range(4):
        for a in range(4):
            for c in range(4):
                for e in range(4):
                    ops2.append((1, i, i, (a, a, c, c, e, e)))
    return [deriv_functional(6, o) for o in (ops1, ops2, ops3)]


def main():
    L = F.L_matrix(6).astype(float); B = F.bianchi_rows(6).astype(float)
    Ann = left_null(L)                       # 840 x 259 orthonormal
    T = orth(B.T)                            # 840 x 224 orthonormal (rows of B as functionals)
    rec = {'dim_Ann': Ann.shape[1], 'dim_T': T.shape[1],
           'T_in_Ann': float(np.linalg.norm(T - Ann @ (Ann.T @ T)))}
    PT = np.eye(840) - T @ T.T
    Qb = orth(PT @ Ann)                      # Ann ∩ T^perp, 35-dim
    rec['dim_Q'] = Qb.shape[1]
    # invariant classes: x in R^35 with PT M_X^T (Qb x) = 0 for X in u(2)
    Ms = [action_matrix(X, 6) for X in u2_basis()]
    rec['T_invariant'] = max(float(np.linalg.norm(PT @ M.T @ T)) for M in Ms)
    rec['Ann_invariant'] = max(float(np.linalg.norm((np.eye(840) - Ann @ Ann.T) @ M.T @ Ann)) for M in Ms)
    Sys = np.vstack([PT @ M.T @ Qb for M in Ms])
    U, s, Vt = np.linalg.svd(Sys)
    rec['inv_system_smallest_sv'] = [float(x) for x in s[-4:]]
    ninv = int((s < 1e-9 * s[0]).sum()); rec['n_invariant_classes'] = ninv
    inv = Qb @ Vt[-ninv:].T if ninv else None
    d = np.load(F.A02 / 'data' / 'step80' / 'recon_F012_gen5_lam-5.npz'); ell = d['ell']
    rec['ell_in_Ann'] = float(np.linalg.norm(ell - Ann @ (Ann.T @ ell)) / np.linalg.norm(ell))
    rec['ell_perp_T'] = float(np.linalg.norm(T.T @ ell) / np.linalg.norm(ell))
    if ninv:
        e = inv[:, 0] / np.linalg.norm(inv[:, 0]); en = ell / np.linalg.norm(ell)
        rec['cos_ell_invariant_class'] = float(abs(e @ en))
    c1, c2, c3 = natural_functionals()
    for name, c in (('JJdd', c1), ('LapTr', c2), ('divdiv', c3)):
        rec[f'{name}_annihilates_L6'] = float(np.linalg.norm(c @ L) / (np.linalg.norm(c) * np.linalg.norm(L)))
        cp = PT @ c
        rec[f'{name}_classnorm_rel'] = float(np.linalg.norm(cp) / np.linalg.norm(c))
        if np.linalg.norm(cp) > 1e-12:
            rec[f'{name}_class_cos_with_ell'] = float(abs(cp @ ell) / (np.linalg.norm(cp) * np.linalg.norm(ell)))
    # best combination of natural functionals that annihilates L6, compared modulo T
    Cmat = np.stack([c1, c2, c3], 1)
    K = Cmat.T @ L
    _, sk, vk = np.linalg.svd(K.T @ np.eye(1) if False else (L.T @ Cmat))
    rec['natural_combo_sv'] = [float(x) for x in sk]
    w = vk[-1]; comb = Cmat @ w
    rec['natural_combo_coeffs'] = (w / w[np.argmax(np.abs(w))]).tolist()
    rec['natural_combo_annihilates_L6'] = float(np.linalg.norm(comb @ L) / (np.linalg.norm(comb) * np.linalg.norm(L)))
    cp = PT @ comb
    rec['natural_combo_class_cos_with_ell'] = float(abs(cp @ ell) / (np.linalg.norm(cp) * np.linalg.norm(ell)))
    print(json.dumps(rec, indent=1))
    (OUT / 'multiplier_exact.json').write_text(json.dumps(rec, indent=1) + '\n')
    np.savez(OUT / 'multiplier_exact.npz', Ann=Ann, T=T, Qb=Qb, inv=inv if ninv else np.zeros(0), c1=c1, c2=c2, c3=c3)


if __name__ == '__main__':
    main()
