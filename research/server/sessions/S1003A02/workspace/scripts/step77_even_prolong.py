#!/usr/bin/env python3
"""Step 77: even-ansatz formal prolongation of AKE germs at a torsion zero, to order K (even).

Even ansatz H(-x) = H(x): consistent at all orders (x -> -x is a symplectic linear isometry of the
flat model, so E_odd = 0 identically when H is even).  Any even germ has grad(Omega) odd, hence a
torsion zero at 0.  Algorithm (mod p, see step77_modp_series):
  order 0 : H2 in affine space L0 H2 = lam*delta
  order 2 : the single excess functional gives the quadric; pick a random F_p point
  order k (k = 4, 6, ...): H_{k} = Hp_k + K, K in ker L_{k-2}; the excess functionals of L_k
            applied to E_k must vanish; the K-dependence is affine (coupling with H2).
            Record rank of the K-map, the number of excess conditions, solvability,
            then pick a random solution K and continue.
Options: --mode generic | kahler (H2 torsion-free: tests whether the K-map surjectivity needs torsion)
Output: workspace/data/step77_even_prolong_<mode>_K<K>_p<p>_s<seed>.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import step77_modp_series as ms
from step77_modp_series import Ring, rank, nullspace, solve, sqrt_mod
import step77_prolong_higher as ph

DATA = Path(__file__).resolve().parents[1] / 'data'


def excess_functionals(S, L, k):
    p = S.p
    cok = nullspace(L.T, p).T
    Bi = S.bianchi_rows(k)
    base = Bi.copy(); r0 = rank(base, p); ex = []
    for c in cok:
        t = np.vstack([base, c]); r1 = rank(t, p)
        if r1 > r0:
            base, r0 = t, r1; ex.append(c)
    return np.array(ex), cok, Bi


def torsion_jet_map(S, B2, p):
    """linear torsion (first jet of nabla Omega) of degree-2 fields, as rows over Hbasis(2) coords.
    Uses Christoffel symbols: (nabla_k Omega)_ij = -Gamma^l_ki Omega_lj - Gamma^l_kj Omega_il at degree 1."""
    R4 = Ring(4, p)
    OM = ph.J0.T
    cols = []
    for e in B2:
        H = ph.restrict(S, e, R4)
        g, gi = R4.exp_series(H)
        G = R4.christoffel(g, gi)
        v = []
        d1 = R4.monos(1)
        for k in range(4):
            for i in range(4):
                for j in range(i + 1, 4):
                    acc = np.zeros(R4.nm, dtype=np.int64)
                    for l in range(4):
                        acc -= G[l, k, i] * int(OM[l, j]) + G[l, k, j] * int(OM[i, l])
                    v += list(acc[d1] % p)
        cols.append(v)
    return np.array(cols).T % p


def main(K=6, p=ms.P, seed=1, lam=-3, mode='generic'):
    t0 = time.time(); rng = np.random.default_rng(seed)
    S = ph.Setup(K + 2, p)
    rings = {k: Ring(k + 2, p) for k in range(2, K + 1, 2)}
    delta = np.array([1 if i == j else 0 for i in range(4) for j in range(i, 4)])
    L = {k: S.Lmat(k) for k in range(0, K + 1, 2)}
    print('L built', round(time.time() - t0, 1), flush=True)
    B = {d: S.Hbasis(d) for d in range(2, K + 1, 2)}
    haff = solve(L[0], (lam * delta) % p, p)
    N0 = nullspace(L[0], p)
    if mode == 'kahler':
        T = torsion_jet_map(S, B[2], p)
        # restrict to torsion-free part of ker L0 and torsion-free particular solution
        N0 = N0 @ nullspace((T @ N0) % p, p) % p
        A = np.vstack([L[0], T]); rhs = np.concatenate([(lam * delta) % p, np.zeros(T.shape[0], dtype=np.int64)])
        haff = solve(A, rhs, p)
    exs = {}
    for k in range(2, K + 1, 2):
        exs[k] = excess_functionals(S, L[k], k)
        print('order', k, 'excess', exs[k][0].shape[0], round(time.time() - t0, 1), flush=True)

    def Ek(H, k):
        return S.E(ph.restrict(S, H, rings[k]), lam, k, rings[k])

    ell2 = exs[2][0]
    # ---- quadric point
    def c2(v):
        return int(ell2[0] @ Ek(S.comb(B[2], v), 2) % p)
    inv2 = pow(2, p - 2, p)
    while True:
        v0 = (haff + N0 @ rng.integers(0, p, N0.shape[1])) % p
        w = (N0 @ rng.integers(0, p, N0.shape[1])) % p
        f0, f1, fm = c2(v0), c2((v0 + w) % p), c2((v0 - w) % p)
        a = f0; cq = (f1 + fm - 2 * f0) * inv2 % p; b = (f1 - fm) * inv2 % p
        if mode == 'kahler' and cq == 0 and b == 0:
            v = v0; break      # compat automatically satisfied on torsion-free jets
        if cq == 0:
            continue
        r = sqrt_mod((b * b - 4 * a * cq) % p, p)
        if r is None:
            continue
        v = (v0 + ((-b + r) * pow(2 * cq, p - 2, p) % p) * w) % p
        break
    H = S.comb(B[2], v)
    E2 = Ek(H, 2)
    log = {'mode': mode, 'p': p, 'seed': seed, 'lam': lam, 'K': K,
           'order2_all_coker_zero': bool(((exs[2][1] @ E2) % p == 0).all()), 'orders': []}
    for k in range(4, K + 1, 2):
        # particular H_k from order k-2
        Ekm2 = Ek(H, k - 2)
        Hp = solve(L[k - 2], (-Ekm2) % p, p)
        assert Hp is not None, 'order %d not solvable' % (k - 2)
        H = (H + S.comb(B[k], Hp)) % p
        assert (Ek(H, k - 2) % p == 0).all()
        Nk = nullspace(L[k - 2], p)
        ex, cok, Bi = exs[k]
        e0 = Ek(H, k)
        rec = {'order': k, 'excess': int(ex.shape[0]), 'kerL_dim': int(Nk.shape[1]),
               'bianchi_auto': bool(((Bi @ e0) % p == 0).all())}
        cols = []
        for j in range(Nk.shape[1]):
            cols.append((Ek((H + S.comb(B[k], Nk[:, j])) % p, k) - e0) % p)
        M = (ex @ np.array(cols).T) % p
        rhs = (-(ex @ e0)) % p
        rec['K_map_rank'] = int(rank(M, p))
        rec['rhs_zero'] = bool((rhs == 0).all())
        x = solve(M, rhs, p)
        rec['solvable'] = x is not None
        print(rec, round(time.time() - t0, 1), flush=True)
        log['orders'].append(rec)
        if x is None:
            break
        z = nullspace(M, p)
        x = (x + z @ rng.integers(0, p, z.shape[1])) % p if z.size else x
        Kfield = (Nk @ x) % p
        H = (H + S.comb(B[k], Kfield)) % p
        ek = Ek(H, k)
        assert ((cok @ ek) % p == 0).all()
    log['time'] = time.time() - t0
    out = DATA / f'step77_even_prolong_{mode}_K{K}_p{p}_s{seed}_lam{lam}.json'
    out.write_text(json.dumps(log, indent=1) + '\n')
    print(json.dumps(log, indent=1))


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--K', type=int, default=6)
    ap.add_argument('--p', type=int, default=ms.P)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--lam', type=int, default=-3)
    ap.add_argument('--mode', default='generic')
    a = ap.parse_args()
    main(a.K, a.p, a.seed, a.lam, a.mode)
