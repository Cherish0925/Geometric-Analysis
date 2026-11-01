#!/usr/bin/env python3
"""Step 77: rank of the top-jet absorption map at a nondegenerate torsion zero, orders k = 4,6,8,...

For H2 on the order-2 quadric (random F_p point), the order-k excess conditions (coker L_k modulo flat
Bianchi, dimension C(k+1,3)) depend on the new free jet K in ker L_{k-2} only through
    A_k(H2) K = ex_k . [ B(H2,K) - lam K ]_k ,
independently of the lower jets.  r_k = rank A_k is the number of order-k conditions absorbed by K;
the remaining C(k+1,3) - r_k must be imposed on lower jets.  Also computed for torsion-free H2.
Output: workspace/data/step77_topmap_rank_p<p>_s<seed>.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import step77_modp_series as ms
from step77_modp_series import Ring, rank, nullspace, solve, sqrt_mod
import step77_prolong_higher as ph
from step77_even_prolong import excess_functionals, torsion_jet_map

DATA = Path(__file__).resolve().parents[1] / 'data'


def main(KMAX=8, p=ms.P, seed=1, lam=-3):
    t0 = time.time(); rng = np.random.default_rng(seed)
    S = ph.Setup(KMAX + 2, p)
    delta = np.array([1 if i == j else 0 for i in range(4) for j in range(i, 4)])
    L0 = S.Lmat(0); L2 = S.Lmat(2)
    B2 = S.Hbasis(2)
    R4 = Ring(4, p)
    haff = solve(L0, (lam * delta) % p, p); N0 = nullspace(L0, p)
    ell2 = excess_functionals(S, L2, 2)[0][0]
    c2 = lambda v: int(ell2 @ S.E(ph.restrict(S, S.comb(B2, v), R4), lam, 2, R4) % p)
    inv2 = pow(2, p - 2, p)
    while True:
        v0 = (haff + N0 @ rng.integers(0, p, N0.shape[1])) % p
        w = (N0 @ rng.integers(0, p, N0.shape[1])) % p
        f0, f1, fm = c2(v0), c2((v0 + w) % p), c2((v0 - w) % p)
        a = f0; cq = (f1 + fm - 2 * f0) * inv2 % p; b = (f1 - fm) * inv2 % p
        r = sqrt_mod((b * b - 4 * a * cq) % p, p) if cq else None
        if r is None:
            continue
        v2 = (v0 + ((-b + r) * pow(2 * cq, p - 2, p) % p) * w) % p
        break
    # torsion-free comparison point
    T = torsion_jet_map(S, B2, p)
    N0k = N0 @ nullspace((T @ N0) % p, p) % p
    hk = solve(np.vstack([L0, T]), np.concatenate([(lam * delta) % p, np.zeros(T.shape[0], dtype=np.int64)]), p)
    vK = (hk + N0k @ rng.integers(0, p, N0k.shape[1])) % p
    out = {'p': p, 'seed': seed, 'lam': lam, 'orders': {}}
    for k in range(4, KMAX + 1, 2):
        Rk = Ring(k + 2, p)
        Lk = S.Lmat(k); Lkm2 = S.Lmat(k - 2)
        ex = excess_functionals(S, Lk, k)[0]
        Nk = nullspace(Lkm2, p)
        Bk = S.Hbasis(k)
        rec = {'excess': int(ex.shape[0]), 'kerL_{k-2}': int(Nk.shape[1])}
        for name, v in (('generic', v2), ('torsion_free', vK)):
            H2 = S.comb(B2, v)
            e0 = S.E(ph.restrict(S, H2, Rk), lam, k, Rk)
            cols = []
            for j in range(Nk.shape[1]):
                Hj = (H2 + S.comb(Bk, Nk[:, j])) % p
                cols.append((S.E(ph.restrict(S, Hj, Rk), lam, k, Rk) - e0) % p)
            A = (ex @ np.array(cols).T) % p
            rec['rank_' + name] = int(rank(A, p))
        out['orders'][k] = rec
        print(k, rec, round(time.time() - t0, 1), flush=True)
    out['time'] = time.time() - t0
    (DATA / f'step77_topmap_rank_p{p}_s{seed}.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--kmax', type=int, default=8)
    ap.add_argument('--p', type=int, default=ms.P)
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    main(a.kmax, a.p, a.seed)
