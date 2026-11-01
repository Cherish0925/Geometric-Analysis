#!/usr/bin/env python3
"""Fast exact power-series Ricci in Darboux gauge (step 76), pure-Python Fractions.

Polynomials: dict {exponent 4-tuple: Fraction}.  Matrices: 4x4 lists of polys.
Provides ricci_exp(H, N): Ricci of g = exp(H) truncated at total degree N-2, where
H is O(|x|^2) and g is needed up to degree N.  Also Christoffels for torsion.
"""
from fractions import Fraction as F
import itertools

def padd(a, b, s=1):
    r = dict(a)
    for m, c in b.items():
        v = r.get(m, 0) + s*c
        if v == 0:
            r.pop(m, None)
        else:
            r[m] = v
    return r

def pscale(a, s):
    if s == 0:
        return {}
    return {m: c*s for m, c in a.items()}

def pmul(a, b, N):
    r = {}
    for m1, c1 in a.items():
        d1 = sum(m1)
        for m2, c2 in b.items():
            if d1 + sum(m2) > N:
                continue
            m = (m1[0]+m2[0], m1[1]+m2[1], m1[2]+m2[2], m1[3]+m2[3])
            v = r.get(m, 0) + c1*c2
            if v == 0:
                r.pop(m, None)
            else:
                r[m] = v
    return r

def pdiff(a, k):
    r = {}
    for m, c in a.items():
        if m[k] > 0:
            mm = list(m); mm[k] -= 1
            r[tuple(mm)] = c*m[k]
    return r

def phom(a, d):
    return {m: c for m, c in a.items() if sum(m) == d}

def ptrunc(a, N):
    return {m: c for m, c in a.items() if sum(m) <= N}

def zero():
    return [[{} for _ in range(4)] for _ in range(4)]

def eye():
    Z = zero()
    for i in range(4):
        Z[i][i] = {(0, 0, 0, 0): F(1)}
    return Z

def madd(A, B, s=1):
    return [[padd(A[i][j], B[i][j], s) for j in range(4)] for i in range(4)]

def mscale(A, s):
    return [[pscale(A[i][j], s) for j in range(4)] for i in range(4)]

def mmul(A, B, N):
    C = zero()
    for i in range(4):
        for j in range(4):
            acc = {}
            for k in range(4):
                if A[i][k] and B[k][j]:
                    acc = padd(acc, pmul(A[i][k], B[k][j], N))
            C[i][j] = acc
    return C

def const_matrix(M):
    """numeric 4x4 -> poly matrix"""
    Z = zero()
    for i in range(4):
        for j in range(4):
            if M[i][j] != 0:
                Z[i][j] = {(0, 0, 0, 0): F(M[i][j])}
    return Z

def mono(e):
    return {tuple(e): F(1)}

def exp_series(H, N, lowdeg=2):
    g = madd(eye(), H); gi = madd(eye(), H, -1)
    P = H; fact = 1; sign = -1
    for k in range(2, N//lowdeg + 1):
        P = mmul(P, H, N); fact *= k; sign = -sign
        g = madd(g, mscale(P, F(1, fact)))
        gi = madd(gi, mscale(P, F(sign, fact)))
    return g, gi

def christoffel(g, gi, N):
    dg = [[[ptrunc(pdiff(g[i][j], k), N-1) for k in range(4)] for j in range(4)] for i in range(4)]
    G = [[[None]*4 for _ in range(4)] for _ in range(4)]
    for k in range(4):
        for i in range(4):
            for j in range(i, 4):
                acc = {}
                for l in range(4):
                    if gi[k][l]:
                        t = padd(padd(dg[l][i][j], dg[l][j][i]), dg[i][j][l], -1)
                        if t:
                            acc = padd(acc, pmul(gi[k][l], t, N-1))
                acc = pscale(acc, F(1, 2))
                G[k][i][j] = acc; G[k][j][i] = acc
    return G

def ricci_from_gamma(G, N):
    R = zero()
    for i in range(4):
        for j in range(i, 4):
            acc = {}
            for k in range(4):
                acc = padd(acc, pdiff(G[k][i][j], k))
                acc = padd(acc, pdiff(G[k][i][k], j), -1)
                for l in range(4):
                    if G[k][k][l] and G[l][i][j]:
                        acc = padd(acc, pmul(G[k][k][l], G[l][i][j], N-2))
                    if G[k][j][l] and G[l][i][k]:
                        acc = padd(acc, pmul(G[k][j][l], G[l][i][k], N-2), -1)
            acc = ptrunc(acc, N-2)
            R[i][j] = acc; R[j][i] = acc
    return R

def ricci_exp(H, N, lowdeg=2):
    g, gi = exp_series(H, N, lowdeg)
    G = christoffel(g, gi, N)
    return ricci_from_gamma(G, N), g, G

def monos(d):
    return [e for e in itertools.product(range(d+1), repeat=4) if sum(e) == d]

def sym_vec(M, d):
    ms = monos(d); v = []
    for i in range(4):
        for j in range(i, 4):
            v += [M[i][j].get(m, F(0)) for m in ms]
    return v
