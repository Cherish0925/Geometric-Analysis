#!/usr/bin/env python3
"""Step 77: fast truncated power-series Ricci of g = exp(H) in Darboux gauge, modulo a prime.

All arithmetic is exact in F_p (p = 33554393 < 2^25, so that int64 matrix products of length <= 4096 cannot overflow).  Ranks computed mod p equal the
rational ranks with overwhelming probability for random data; every structural rank used later is
re-checked with a second prime.

Polynomials in x1..x4 truncated at total degree NMAX are dense int64 vectors indexed by
`MON` (all exponents of degree <= NMAX).  Poly matrices are arrays of shape (4,4,nm).
"""
import itertools
import numpy as np

P = 33554393


def set_prime(p):
    global P
    P = p


class Ring:
    def __init__(self, nmax, p=None):
        self.p = p or P
        self.N = nmax
        mons = [e for d in range(nmax + 1) for e in itertools.product(range(d + 1), repeat=4) if sum(e) == d]
        self.mons = mons
        self.idx = {m: i for i, m in enumerate(mons)}
        self.deg = np.array([sum(m) for m in mons])
        self.nm = len(mons)
        # multiplication table sorted by target
        I, J, K = [], [], []
        for i, a in enumerate(mons):
            for j, b in enumerate(mons):
                if sum(a) + sum(b) <= nmax:
                    I.append(i); J.append(j); K.append(self.idx[tuple(x + y for x, y in zip(a, b))])
        I, J, K = map(np.array, (I, J, K))
        o = np.argsort(K, kind='stable')
        self.I, self.J, self.K = I[o], J[o], K[o]
        self.starts = np.flatnonzero(np.r_[True, self.K[1:] != self.K[:-1]])
        self.tk = self.K[self.starts]
        # derivative tables
        self.dsrc, self.dcoef = [], []
        for k in range(4):
            src = np.full(self.nm, -1); cf = np.zeros(self.nm, dtype=np.int64)
            for i, m in enumerate(mons):
                mm = list(m); mm[k] += 1
                if sum(mm) <= nmax:
                    src[i] = self.idx[tuple(mm)]; cf[i] = mm[k]
            self.dsrc.append(src); self.dcoef.append(cf)

    def inv(self, a):
        return pow(int(a) % self.p, self.p - 2, self.p)

    def mul(self, a, b, trunc=None):
        p = self.p
        prod = (a[self.I] * b[self.J]) % p
        s = np.add.reduceat(prod, self.starts) % p
        out = np.zeros(self.nm, dtype=np.int64)
        out[self.tk] = s
        if trunc is not None:
            out[self.deg > trunc] = 0
        return out

    def diff(self, a, k):
        src = self.dsrc[k]
        out = np.zeros(self.nm, dtype=np.int64)
        ok = src >= 0
        out[ok] = (a[src[ok]] * self.dcoef[k][ok]) % self.p
        return out

    def hom(self, a, d):
        out = a.copy(); out[self.deg != d] = 0
        return out

    # ---- matrices -------------------------------------------------
    def eye(self):
        E = np.zeros((4, 4, self.nm), dtype=np.int64)
        for i in range(4):
            E[i, i, 0] = 1
        return E

    def mmul(self, A, B, trunc=None):
        C = np.zeros_like(A)
        for i in range(4):
            for j in range(4):
                acc = np.zeros(self.nm, dtype=np.int64)
                for k in range(4):
                    if A[i, k].any() and B[k, j].any():
                        acc += self.mul(A[i, k], B[k, j], trunc)
                C[i, j] = acc % self.p
        return C

    def exp_series(self, H, lowdeg=2):
        p = self.p
        g = (self.eye() + H) % p
        gi = (self.eye() - H) % p
        Pw = H.copy(); fact = 1; sign = -1
        for k in range(2, self.N // lowdeg + 1):
            Pw = self.mmul(Pw, H); fact *= k; sign = -sign
            fi = self.inv(fact)
            g = (g + Pw * fi) % p
            gi = (gi + Pw * ((sign * fi) % p)) % p
        return g, gi

    def christoffel(self, g, gi):
        p = self.p; N = self.N
        dg = np.zeros((4, 4, 4, self.nm), dtype=np.int64)
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    dg[i, j, k] = self.diff(g[i, j], k)
        half = self.inv(2)
        G = np.zeros((4, 4, 4, self.nm), dtype=np.int64)
        for k in range(4):
            for i in range(4):
                for j in range(i, 4):
                    acc = np.zeros(self.nm, dtype=np.int64)
                    for l in range(4):
                        if gi[k, l].any():
                            t = (dg[l, i, j] + dg[l, j, i] - dg[i, j, l]) % p
                            if t.any():
                                acc += self.mul(gi[k, l], t, N - 1)
                    acc = (acc % p) * half % p
                    G[k, i, j] = acc; G[k, j, i] = acc
        return G

    def ricci(self, H, lowdeg=2):
        """Ricci of exp(H) valid up to degree N-2 (entries of higher degree zeroed)."""
        p = self.p; N = self.N
        g, gi = self.exp_series(H, lowdeg)
        G = self.christoffel(g, gi)
        R = np.zeros((4, 4, self.nm), dtype=np.int64)
        nz = [[[G[k, i, j].any() for j in range(4)] for i in range(4)] for k in range(4)]
        for i in range(4):
            for j in range(i, 4):
                acc = np.zeros(self.nm, dtype=np.int64)
                for k in range(4):
                    acc += self.diff(G[k, i, j], k)
                    acc -= self.diff(G[k, i, k], j)
                    for l in range(4):
                        if nz[k][k][l] and nz[l][i][j]:
                            acc += self.mul(G[k, k, l], G[l, i, j], N - 2)
                        if nz[k][j][l] and nz[l][i][k]:
                            acc -= self.mul(G[k, j, l], G[l, i, k], N - 2)
                acc %= p
                acc[self.deg > N - 2] = 0
                R[i, j] = acc; R[j, i] = acc
        return R, g, G

    # ---- vectorization -------------------------------------------
    def monos(self, d):
        return [i for i, m in enumerate(self.mons) if sum(m) == d]

    def symvec(self, M, d):
        ii = self.monos(d)
        return np.concatenate([M[i, j, ii] for i in range(4) for j in range(i, 4)]) % self.p


# ---------------- linear algebra mod p ------------------------------
def rref(M, p):
    A = np.array(M, dtype=np.int64) % p
    r = 0; piv = []
    rows, cols = A.shape
    for c in range(cols):
        if r >= rows:
            break
        nzr = np.flatnonzero(A[r:, c])
        if nzr.size == 0:
            continue
        k = r + nzr[0]
        if k != r:
            A[[r, k]] = A[[k, r]]
        A[r] = A[r] * pow(int(A[r, c]), p - 2, p) % p
        col = A[:, c].copy(); col[r] = 0
        nz = np.flatnonzero(col)
        if nz.size:
            A[nz] = (A[nz] - np.outer(col[nz], A[r]) % p) % p
        piv.append(c); r += 1
    return A[:r], piv


def rank(M, p):
    return len(rref(M, p)[1])


def nullspace(M, p):
    """right nullspace basis (as columns of returned array, shape (ncols, k))"""
    M = np.array(M, dtype=np.int64)
    R, piv = rref(M, p)
    n = M.shape[1]
    free = [c for c in range(n) if c not in set(piv)]
    out = np.zeros((n, len(free)), dtype=np.int64)
    for t, f in enumerate(free):
        out[f, t] = 1
        for r, c in enumerate(piv):
            out[c, t] = (-R[r, f]) % p
    return out


def solve(M, b, p):
    """one solution x of M x = b, or None"""
    M = np.array(M, dtype=np.int64) % p; b = np.array(b, dtype=np.int64) % p
    Aug = np.hstack([M, b.reshape(-1, 1)])
    R, piv = rref(Aug, p)
    if M.shape[1] in piv:
        return None
    x = np.zeros(M.shape[1], dtype=np.int64)
    for r, c in enumerate(piv):
        x[c] = R[r, -1]
    return x


def sqrt_mod(a, p):
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        return None
    # Tonelli-Shanks
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, tt = 0, t
        while tt != 1:
            tt = tt * tt % p; i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r
