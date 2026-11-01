#!/usr/bin/env python3
"""Step 55c: discriminant forms of T-chain lattices C_{n,a} (negative definite, det n^2).
Gluing C (+) <-n^2> to a unimodular lattice requires disc(C) = <beta/n^2> to be isometric to <+1/n^2>, i.e. beta a unit
square mod n^2.  We verify beta == 1 - n a (mod n^2) and tabulate the unit-square test (predicted: n odd or 8 | n).
Output: workspace/data/step55_Tchain_discriminants.json
"""
import json, os
from math import gcd
import sympy as sp


def hj(p, q):
    out = []
    while q:
        b = -(-p // q); out.append(b); p, q = q, b * q - p
    return out


rows = []
for n in range(2, 17):
    sq = {(u * u) % (n * n) for u in range(1, n * n) if gcd(u, n) == 1}
    for a in range(1, n):
        if gcd(n, a) != 1:
            continue
        ch = hj(n * n, n * a - 1); r = len(ch)
        G = sp.zeros(r)
        for i, b in enumerate(ch):
            G[i, i] = -b
            if i + 1 < r:
                G[i, i + 1] = G[i + 1, i] = 1
        beta = int((G.inv()[0, 0] * n * n) % (n * n))
        rows.append({'n': n, 'a': a, 'chain': ch, 'det': int(G.det()), 'beta': beta,
                     'beta==1-na': beta == (1 - n * a) % (n * n), 'unit_square': beta in sq,
                     'predicted(n odd or 8|n)': (n % 2 == 1) or (n % 8 == 0)})
ok = all(d['beta==1-na'] and d['unit_square'] == d['predicted(n odd or 8|n)'] for d in rows)
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step55_Tchain_discriminants.json')
json.dump({'all_consistent': ok, 'rows': rows}, open(p, 'w'), indent=1)
print('all_consistent', ok, 'cases', len(rows))
