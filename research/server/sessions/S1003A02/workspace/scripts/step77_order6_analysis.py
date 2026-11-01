#!/usr/bin/env python3
"""Step 77: order-6 analysis of the even-ansatz AKE prolongation at a torsion zero.

After a random F_p point (H2 on the order-2 quadric, H4 solving orders 2 and 4) we have
  F6(H2,H4,K6) = A(H2) K6 + G(H2,H4)      (35 excess conditions, K6 in ker L4)
with rank A = r6.  Left null vectors mu of A (35 - r6 of them) give conditions mu.G = 0 that
K6 cannot absorb.  We compute the Jacobian of mu.G with respect to
  (i)  admissible H4 variations delta (ker L2 and order-4 linearised conditions), and
  (ii) H2 variations tangent to the quadric (carrying H4 along), [optional]
to decide whether the residual conditions fall on H4 (formal variety cut but nonempty generically)
or on the torsion jet H2 itself.
Output: workspace/data/step77_order6_analysis_p<p>_s<seed>_lam<lam>.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import step77_modp_series as ms
from step77_modp_series import Ring, rank, nullspace, solve, sqrt_mod, rref
import step77_prolong_higher as ph
from step77_even_prolong import excess_functionals

DATA = Path(__file__).resolve().parents[1] / 'data'


def solve_multi(M, Bm, p):
    """X with M X = Bm (columns), assuming solvable"""
    M = np.array(M, dtype=np.int64) % p
    Aug = np.hstack([M, Bm % p])
    R, piv = rref(Aug, p)
    n = M.shape[1]
    assert all(c < n for c in piv), 'not solvable'
    X = np.zeros((n, Bm.shape[1]), dtype=np.int64)
    for r, c in enumerate(piv):
        X[c] = R[r, n:]
    return X


def main(p=ms.P, seed=1, lam=-3):
    t0 = time.time(); rng = np.random.default_rng(seed)
    K = 6
    S = ph.Setup(K + 2, p)
    rings = {k: Ring(k + 2, p) for k in (2, 4, 6)}
    delta = np.array([1 if i == j else 0 for i in range(4) for j in range(i, 4)])
    L = {k: S.Lmat(k) for k in (0, 2, 4, 6)}
    B = {d: S.Hbasis(d) for d in (2, 4, 6)}
    exs = {k: excess_functionals(S, L[k], k) for k in (2, 4, 6)}
    Ek = lambda H, k: S.E(ph.restrict(S, H, rings[k]), lam, k, rings[k])
    vec = lambda d, c: S.comb(B[d], c)
    haff = solve(L[0], (lam * delta) % p, p); N0 = nullspace(L[0], p)
    ell2 = exs[2][0][0]
    c2 = lambda v: int(ell2 @ Ek(vec(2, v), 2) % p)
    inv2 = pow(2, p - 2, p)
    while True:
        v0 = (haff + N0 @ rng.integers(0, p, N0.shape[1])) % p
        w = (N0 @ rng.integers(0, p, N0.shape[1])) % p
        f0, f1, fm = c2(v0), c2((v0 + w) % p), c2((v0 - w) % p)
        a = f0; cq = (f1 + fm - 2 * f0) * inv2 % p; b = (f1 - fm) * inv2 % p
        if cq == 0:
            continue
        r = sqrt_mod((b * b - 4 * a * cq) % p, p)
        if r is None:
            continue
        v2 = (v0 + ((-b + r) * pow(2 * cq, p - 2, p) % p) * w) % p
        break
    H2 = vec(2, v2)
    # order 2 -> particular H4 ; order 4 -> admissible K4
    h4p = solve(L[2], (-Ek(H2, 2)) % p, p)
    N2 = nullspace(L[2], p)
    ex4 = exs[4][0]
    H = (H2 + vec(4, h4p)) % p
    e40 = Ek(H, 4)
    e4cols = np.array([(Ek((H + vec(4, N2[:, j])) % p, 4) - e40) % p for j in range(N2.shape[1])]).T
    M4 = (ex4 @ e4cols) % p
    x = solve(M4, (-(ex4 @ e40)) % p, p); assert x is not None
    Z4 = nullspace(M4, p)
    x = (x + Z4 @ rng.integers(0, p, Z4.shape[1])) % p
    h4 = (h4p + N2 @ x) % p
    H = (H2 + vec(4, h4)) % p
    e4 = Ek(H, 4)
    assert ((exs[4][1] @ e4) % p == 0).all()
    D4 = (N2 @ Z4) % p           # admissible H4 variations (coords in B[4])
    print('order4 done: admissible H4 variations', D4.shape[1], 'rank', rank(D4, p), round(time.time() - t0, 1), flush=True)
    # linear response of E4 to admissible variations, and right inverse of L4 on it
    e4lin = np.array([(Ek((H + vec(4, D4[:, j])) % p, 4) - e4) % p for j in range(D4.shape[1])]).T
    h6p = solve(L[4], (-e4) % p, p); assert h6p is not None
    X6 = solve_multi(L[4], (-e4lin) % p, p)        # H6 response columns
    N4 = nullspace(L[4], p)
    ex6 = exs[6][0]
    Hfull = (H + vec(6, h6p)) % p
    e60 = Ek(Hfull, 6)
    bianchi_ok = bool(((exs[6][2] @ e60) % p == 0).all())
    A = (ex6 @ np.array([(Ek((Hfull + vec(6, N4[:, j])) % p, 6) - e60) % p for j in range(N4.shape[1])]).T) % p
    rA = rank(A, p)
    mu = nullspace(A.T, p).T            # left null vectors
    print('order6: excess', ex6.shape[0], 'rank A', rA, 'left null', mu.shape[0], 'bianchi', bianchi_ok, round(time.time() - t0, 1), flush=True)
    G0 = (mu @ ex6 @ e60) % p
    # Jacobian w.r.t. admissible H4 variations (Psi quadratic in delta -> central difference exact)
    jac = []
    for j in range(D4.shape[1]):
        vals = []
        for s in (1, -1):
            Hs = (H + s * vec(4, D4[:, j]) + vec(6, (h6p + s * X6[:, j]) % p)) % p
            vals.append((mu @ ex6 @ Ek(Hs, 6)) % p)
        jac.append((vals[0] - vals[1]) * inv2 % p)
    J4 = np.array(jac).T % p
    rJ4 = rank(J4, p)
    print('Jacobian wrt H4 rank', rJ4, 'of', mu.shape[0], round(time.time() - t0, 1), flush=True)
    res = {'p': p, 'seed': seed, 'lam': lam, 'order4_admissible_dim': int(D4.shape[1]),
           'order6_excess': int(ex6.shape[0]), 'rank_K6_map': int(rA), 'residual_conditions': int(mu.shape[0]),
           'residual_values_nonzero': int((G0 != 0).sum()), 'bianchi_auto_order6': bianchi_ok,
           'jacobian_H4_rank': int(rJ4), 'time': time.time() - t0}
    out = DATA / f'step77_order6_analysis_p{p}_s{seed}_lam{lam}.json'
    out.write_text(json.dumps(res, indent=1) + '\n')
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--p', type=int, default=ms.P)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--lam', type=int, default=-3)
    a = ap.parse_args()
    main(a.p, a.seed, a.lam)
