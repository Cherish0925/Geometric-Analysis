#!/usr/bin/env python3
"""Step 77: higher-order formal prolongation of AKE germs at a torsion zero (Darboux gauge, mod p).

Formulation (as Step 76): Omega standard, g = exp(H), H symmetric with H J0 = -J0 H (6 functions);
AKE <=> E := Ric(g) - lam g = 0 modulo Hamiltonian diffeomorphisms.  At a torsion zero, after
the cubic-Hamiltonian gauge, H = O(|x|^2).  E_k (degree-k part) = L_k H_{k+2} + N_k(H_2..H_{k+1}).

Parts
 A. linear Hilbert data of L_k (k=0..KMAX): rank, coker, flat-Bianchi rank, excess coker,
    Hamiltonian gauge rank, dim ker L_k / gauge.
 B. order 3: for H2 on the order-2 quadric, rank of H3 in ker L1 -> excess-coker(L3) . E3.
 C. order 4 (even ansatz H3=0): for H2 on the quadric, H4 = H4p + K, K in ker L2;
    is there K with excess-coker(L4) . E4 = 0 ?  (rank of the K-linear map, solvability)
 D. order 4 with odd jets: add H3 in the order-3 solution space (enters E4 quadratically).
Output: workspace/data/step77_prolong_higher.json
"""
import json, sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import step77_modp_series as ms
from step77_modp_series import Ring, rref, rank, nullspace, solve, sqrt_mod

DATA = Path(__file__).resolve().parents[1] / 'data'
J0 = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])


def anti_basis():
    # symmetric S with S J0 + J0 S = 0
    syms = []
    for i in range(4):
        for j in range(i, 4):
            E = np.zeros((4, 4), dtype=int); E[i, j] = 1; E[j, i] = 1; syms.append(E)
    A = np.array([(S @ J0 + J0 @ S).ravel() for S in syms]).T
    # integer nullspace via sympy
    import sympy as sp
    ns = sp.Matrix(A).nullspace()
    out = []
    for v in ns:
        v = v * sp.ilcm(*[x.q for x in v])
        out.append(sum(int(v[t]) * syms[t] for t in range(10)))
    return out


class Setup:
    def __init__(self, NMAX, p):
        self.p = p
        self.R = Ring(NMAX, p)
        self.Bs = anti_basis()
        assert len(self.Bs) == 6

    def Hbasis(self, d):
        R = self.R; out = []
        for B in self.Bs:
            for m in R.monos(d):
                Z = np.zeros((4, 4, R.nm), dtype=np.int64)
                Z[:, :, m] = B % self.p
                out.append(Z)
        return out

    def comb(self, basis, coeffs):
        Z = np.zeros_like(basis[0])
        for b, c in zip(basis, coeffs):
            if c % self.p:
                Z = (Z + b * (int(c) % self.p)) % self.p
        return Z

    def lin_ricci(self, h, d_out):
        """flat linearized Ricci, degree d_out part, as symvec"""
        R = self.R; p = self.p
        D = lambda a, k: R.diff(a, k)
        tr = sum(h[k, k] for k in range(4)) % p
        out = np.zeros((4, 4, R.nm), dtype=np.int64)
        half = R.inv(2)
        for i in range(4):
            for j in range(i, 4):
                acc = np.zeros(R.nm, dtype=np.int64)
                for k in range(4):
                    acc += D(D(h[k, j], k), i) + D(D(h[k, i], k), j) - D(D(h[i, j], k), k)
                acc -= D(D(tr, i), j)
                acc = (acc % p) * half % p
                out[i, j] = acc; out[j, i] = acc
        return R.symvec(out, d_out)

    def Lmat(self, k):
        return np.array([self.lin_ricci(e, k) for e in self.Hbasis(k + 2)]).T % self.p

    def bianchi_rows(self, k):
        """rows (functionals on symvec degree k) of flat contracted Bianchi div E - 1/2 d tr E (degree k-1)"""
        R = self.R; p = self.p
        mk = R.monos(k); mk1 = R.monos(k - 1) if k >= 1 else []
        if not mk1:
            return np.zeros((0, 10 * len(mk)), dtype=np.int64)
        cols = []
        half = R.inv(2)
        for i in range(4):
            for j in range(i, 4):
                for m in mk:
                    E = np.zeros((4, 4, R.nm), dtype=np.int64); E[i, j, m] = 1; E[j, i, m] = 1
                    tr = sum(E[a, a] for a in range(4)) % p
                    b = []
                    for l in range(4):
                        acc = np.zeros(R.nm, dtype=np.int64)
                        for a in range(4):
                            acc += R.diff(E[a, l], a)
                        acc = (acc - R.diff(tr, l) * half) % p
                        b.append(acc[mk1])
                    cols.append(np.concatenate(b))
        return np.array(cols).T % p

    def gauge(self, k):
        """images L_X delta for Hamiltonians f of degree k+4, as coefficient vectors in Hbasis(k+2)"""
        R = self.R; p = self.p
        cols = []
        for f in R.monos(k + 4):
            a = np.zeros(R.nm, dtype=np.int64); a[f] = 1
            grad = [R.diff(a, j) for j in range(4)]
            X = [sum((-J0[i, j]) * grad[j] for j in range(4)) % p for i in range(4)]
            h = np.zeros((4, 4, R.nm), dtype=np.int64)
            for i in range(4):
                for j in range(4):
                    h[i, j] = (R.diff(X[j], i) + R.diff(X[i], j)) % p
            cols.append(self.coords(h, k + 2))
        return np.array(cols).T % p

    def coords(self, h, d):
        """coefficients of anti-J degree-d field h in Hbasis(d)"""
        R = self.R; mons = R.monos(d)
        # basis element (B,m): entries B; solve per monomial using 6 anti-J matrices
        if not hasattr(self, '_Binv'):
            A = np.array([B.ravel() for B in self.Bs]).T.astype(float)   # 16 x 6
            self._A = A
        out = np.zeros((6, len(mons)), dtype=np.int64)
        for t, m in enumerate(mons):
            v = h[:, :, m].ravel() % self.p
            # exact: pick 6 independent rows of A (entries are 0,+-1) and solve mod p
            if not hasattr(self, '_rows'):
                import itertools
                for rows in itertools.combinations(range(16), 6):
                    sub = self._A[list(rows)]
                    if abs(np.linalg.det(sub)) > 0.5:
                        self._rows = list(rows); break
                import sympy as sp
                S = sp.Matrix(self._A[self._rows].astype(int))
                Si = S.inv()
                self._Si = np.array([[int(x.p) * pow(int(x.q), self.p - 2, self.p) % self.p for x in Si.row(r)] for r in range(6)], dtype=np.int64)
                Afull = self._A.astype(np.int64)
                self._Afull = Afull
            c = self._Si @ v[self._rows] % self.p
            assert ((self._Afull @ c - v) % self.p == 0).all(), 'not anti-J'
            out[:, t] = c
        return out.ravel()

    def E(self, H, lam, k, ring=None):
        """symvec of degree-k part of Ric(exp H) - lam exp H, using a ring with N=k+2"""
        R = ring
        Ric, g, G = R.ricci(H)
        Em = (Ric - (lam % self.p) * g) % self.p
        return R.symvec(Em, k)


def restrict(S, H, ring):
    """re-embed a field from S.R (NMAX) into a smaller ring"""
    out = np.zeros((4, 4, ring.nm), dtype=np.int64)
    for i, m in enumerate(S.R.mons):
        if sum(m) <= ring.N:
            out[:, :, ring.idx[m]] = H[:, :, i]
    return out


def main(p=ms.P, seed=1, KMAX=5, lam=-3, ntrials=3):
    t0 = time.time(); rng = np.random.default_rng(seed)
    NMAX = max(KMAX + 4, 6)
    S = Setup(NMAX, p)
    res = {'p': p, 'seed': seed, 'lam': lam}
    # ---------- A. linear data
    lin = {}
    Lm, cok_ex = {}, {}
    for k in range(0, KMAX + 1):
        L = S.Lmat(k); Lm[k] = L
        rk = rank(L, p)
        cok = nullspace(L.T, p)   # columns: functionals
        Bi = S.bianchi_rows(k)
        brk = rank(Bi, p) if Bi.size else 0
        joint = rank(np.vstack([cok.T, Bi]) if Bi.size else cok.T, p) if cok.size else brk
        G = S.gauge(k); grk = rank(G, p)
        ker = L.shape[1] - rk
        lin[k] = dict(rows=int(L.shape[0]), cols=int(L.shape[1]), rank=int(rk), coker=int(cok.shape[1]),
                      bianchi_rank=int(brk), coker_plus_bianchi=int(joint), excess=int(cok.shape[1] - brk),
                      gauge_rank=int(grk), ker=int(ker), ker_mod_gauge=int(ker - grk),
                      LG_zero=bool(((L @ G) % p == 0).all()))
        # excess functionals: complete Bianchi span inside coker
        if cok.size:
            base = Bi.copy() if Bi.size else np.zeros((0, L.shape[0]), dtype=np.int64)
            ex = []
            r0 = rank(base, p) if base.size else 0
            for c in range(cok.shape[1]):
                trial = np.vstack([base, cok[:, c]]) if base.size else cok[:, c][None]
                r1 = rank(trial, p)
                if r1 > r0:
                    base, r0 = trial, r1; ex.append(cok[:, c])
            cok_ex[k] = np.array(ex) if ex else np.zeros((0, L.shape[0]), dtype=np.int64)
            cok_ex[(k, 'all')] = cok.T
        print('lin', k, lin[k], round(time.time() - t0, 1), flush=True)
    res['linear'] = lin
    # ---------- order-2 quadric points
    R4 = Ring(4, p); R5 = Ring(5, p); R6 = Ring(6, p)
    B2 = S.Hbasis(2); B3 = S.Hbasis(3); B4 = S.Hbasis(4)
    delta = np.array([1 if i == j else 0 for i in range(4) for j in range(i, 4)])
    L0 = Lm[0]
    haff = solve(L0, (lam * delta) % p, p); assert haff is not None
    N0 = nullspace(L0, p)          # 60 x 50
    def H2of(v):
        return restrict(S, S.comb(B2, v), R4)
    ell2 = cok_ex[2]; assert ell2.shape[0] == 1
    ell2all = cok_ex[(2, 'all')]
    def c2(v):
        return int(ell2[0] @ S.E(H2of(v), lam, 2, R4) % p)
    def quad_point():
        while True:
            v0 = (haff + N0 @ rng.integers(0, p, N0.shape[1])) % p
            w = (N0 @ rng.integers(0, p, N0.shape[1])) % p
            f0, f1, fm = c2(v0), c2((v0 + w) % p), c2((v0 - w) % p)
            inv2 = pow(2, p - 2, p)
            a = f0; cq = (f1 + fm - 2 * f0) * inv2 % p; b = (f1 - fm) * inv2 % p
            if cq == 0:
                continue
            disc = (b * b - 4 * a * cq) % p
            r = sqrt_mod(disc, p)
            if r is None:
                continue
            s = (-b + r) * pow(2 * cq, p - 2, p) % p
            v = (v0 + s * w) % p
            E2 = S.E(H2of(v), lam, 2, R4)
            assert ((ell2all @ E2) % p == 0).all()
            return v, E2
    L1, L2, L3, L4 = Lm[1], Lm[2], Lm[3], Lm[4]
    N1 = nullspace(L1, p); N2 = nullspace(L2, p)
    G1 = S.gauge(1); G2 = S.gauge(2)
    ell3 = cok_ex.get(3, np.zeros((0, L3.shape[0]), dtype=np.int64))
    ell3all = cok_ex.get((3, 'all'))
    ell4 = cok_ex.get(4, np.zeros((0, L4.shape[0]), dtype=np.int64))
    ell4all = cok_ex.get((4, 'all'))
    res['excess'] = {'k3': int(ell3.shape[0]), 'k4': int(ell4.shape[0])}
    trials = []
    for tr in range(ntrials):
        v2, E2 = quad_point()
        H2 = S.comb(B2, v2)
        H4p = solve(L2, (-E2) % p, p); assert H4p is not None
        rec = {}
        # ---- B. order 3: H3 in ker L1, map to ell3 . E3 (linear in H3)
        def E3of(c3):
            H = (H2 + S.comb(B3, c3)) % p
            return S.E(restrict(S, H, R5), lam, 3, R5)
        e30 = E3of(np.zeros(len(B3), dtype=np.int64))
        assert (e30 % p == 0).all()          # parity: odd part vanishes for even H
        cols = []
        for j in range(N1.shape[1]):
            cols.append(E3of(N1[:, j]))
        M3 = np.array(cols).T % p           # E3 values (degree-3 symvec) for basis of ker L1
        # only the projection onto coker(L3) matters; image(L3) part is absorbed by H5
        M3c = (ell3all @ M3) % p if ell3all is not None else np.zeros((0, M3.shape[1]))
        # gauge directions of ker L1: G1 columns (are in ker L1)
        rec['dim_kerL1'] = int(N1.shape[1]); rec['gauge1_rank'] = int(rank(G1, p))
        rec['order3_map_rank'] = int(rank(M3c, p)) if M3c.size else 0
        rec['bianchi_auto_order3'] = bool(((S.bianchi_rows(3) @ M3) % p == 0).all())
        # gauge columns must map to 0: check
        gcheck = []
        for j in range(G1.shape[1]):
            gcheck.append(E3of(G1[:, j]))
        gM = (ell3all @ np.array(gcheck).T) % p if ell3all is not None else None
        rec['gauge_maps_to_zero_order3'] = bool((gM == 0).all()) if gM is not None else True
        # order-3 solution space of H3 (mod nothing): kernel of M3c in ker L1 coordinates
        K3 = nullspace(M3c, p) if M3c.size else np.eye(N1.shape[1], dtype=np.int64)
        rec['order3_solution_dim'] = int(K3.shape[1])
        rec['order3_solution_mod_gauge'] = int(K3.shape[1] - rank(G1, p))
        # ---- C. order 4 even ansatz
        def E4of(c4, c3=None):
            H = (H2 + S.comb(B4, c4)) % p
            if c3 is not None:
                H = (H + S.comb(B3, c3)) % p
            return S.E(restrict(S, H, R6), lam, 4, R6)
        e40 = E4of(H4p)
        rec['bianchi_auto_order4'] = bool(((S.bianchi_rows(4) @ e40) % p == 0).all())
        rhs = (-(ell4all @ e40)) % p
        cols = []
        for j in range(N2.shape[1]):
            cols.append((E4of((H4p + N2[:, j]) % p) - e40) % p)
        M4 = (ell4all @ np.array(cols).T) % p
        rec['order4_K_rank'] = int(rank(M4, p)); rec['order4_rows'] = int(M4.shape[0])
        rec['order4_excess'] = int(ell4.shape[0])
        x = solve(M4, rhs, p)
        rec['order4_even_solvable'] = x is not None
        rec['order4_sol_dim'] = int(N2.shape[1] - rank(M4, p)) if x is not None else -1
        rec['dim_kerL2'] = int(N2.shape[1]); rec['gauge2_rank'] = int(rank(G2, p))
        print('trial', tr, rec, round(time.time() - t0, 1), flush=True)
        trials.append(rec)
    res['trials'] = trials
    res['time'] = time.time() - t0
    out = DATA / f'step77_prolong_higher_p{p}_s{seed}_lam{lam}.json'
    out.write_text(json.dumps(res, indent=1) + '\n')
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--p', type=int, default=ms.P)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--kmax', type=int, default=4)
    ap.add_argument('--lam', type=int, default=-3)
    ap.add_argument('--trials', type=int, default=2)
    a = ap.parse_args()
    main(a.p, a.seed, a.kmax, a.lam, a.trials)
