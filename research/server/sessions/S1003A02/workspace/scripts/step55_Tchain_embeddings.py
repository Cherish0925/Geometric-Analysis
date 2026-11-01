#!/usr/bin/env python3
"""Step 55b: lattice gate for zero-charge T-type orbifold channels at k=1.

A T-singularity 1/n^2(1, n a - 1) (gcd(n,a)=1) has resolution chain [b_1..b_r] (HJ continued fraction of n^2/(na-1)),
Milnor fibre a rational ball B_{n,a} carrying a Ricci-flat Kahler ALE metric (charge c_+=0 in its complex orientation).
Proved in the Step-55 note: on M = X # CP2bar (X aspherical, pi_1 torsion-free), a zero-charge B_{n,a} bubble requires
Y = (M - B) u C with pi_1(Y)=pi_1(X), a degree-one map Y->X, all chain spheres in K = ker(c_*) which is NEGATIVE-DEFINITE
UNIMODULAR of rank r+1, and the chain lattice must embed PRIMITIVELY in K (torsion of H_1 forces o = |coker(K->C^*)| = 1).
For r+1 <= 7, K = -I_{r+1}.  We search embeddings v_i in Z^{r+1} (positive form) with v_i.v_i=b_i, v_i.v_{i+1}=-1,
v_i.v_j=0 (|i-j|>1), and test primitivity (gcd of maximal minors = 1).
Output: workspace/data/step55_Tchain_embeddings.json
"""
import json, os, itertools
from math import gcd
from functools import reduce
import sympy as sp


def hj(p, q):
    out = []
    while q:
        b = -(-p // q)
        out.append(b)
        p, q = q, b * q - p
    return out


def vecs_of_norm(N, dim):
    res = []
    rng = range(-int(N**0.5), int(N**0.5) + 1)
    for v in itertools.product(rng, repeat=dim):
        if sum(x * x for x in v) == N:
            res.append(v)
    return res


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def primitive(vs):
    Mx = sp.Matrix(vs)
    r = Mx.rows
    minors = [Mx[:, list(c)].det() for c in itertools.combinations(range(Mx.cols), r)]
    g = reduce(gcd, [int(abs(x)) for x in minors])
    return g == 1, g


def embeddings(chain, dim, limit=4000):
    pools = [vecs_of_norm(b, dim) for b in chain]
    found = []
    # fix first vector up to signed permutations: choose canonical sorted-nonneg representative
    firsts = {tuple(sorted((abs(x) for x in v), reverse=True)) for v in pools[0]}
    def rec(i, acc):
        if len(found) >= limit:
            return
        if i == len(chain):
            found.append(list(acc)); return
        for v in pools[i]:
            if dot(v, acc[-1]) != -1:
                continue
            if any(dot(v, acc[j]) != 0 for j in range(i - 1)):
                continue
            rec(i + 1, acc + [v])
    for f in firsts:
        rec(1, [f])
    return found


out = []
import sys
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
for n in range(2, NMAX + 1):
    for a in range(1, n):
        if gcd(n, a) != 1:
            continue
        p, q = n * n, n * a - 1
        chain = hj(p, q)
        r = len(chain)
        dim = r + 1
        if dim > 7 or max(chain) > 12:
            out.append({'n': n, 'a': a, 'chain': chain, 'skipped': True}); continue
        embs = embeddings(chain, dim)
        prim = [e for e in embs if primitive(e)[0]]
        nonprim_g = sorted({primitive(e)[1] for e in embs if not primitive(e)[0]})
        out.append({'n': n, 'a': a, 'q': q % p, 'chain': chain, 'rank_K': dim, 'n_embeddings_found': len(embs),
                    'n_primitive': len(prim), 'nonprimitive_minor_gcds': nonprim_g,
                    'example_primitive': prim[0] if prim else None,
                    'zero_charge_channel_lattice_allowed': bool(prim)})
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step55_Tchain_embeddings.json')
with open(p, 'w') as fh:
    json.dump(out, fh, indent=1)
for d in out:
    print(d)
