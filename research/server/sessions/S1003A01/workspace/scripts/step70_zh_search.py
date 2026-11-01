#!/usr/bin/env python3
"""Step 70b: explicit flat kernel elements with principal torsion v = z h(zbar).

Search, in the complex flat model of step70_complex_model_check.py, for
anti-J variations nu whose z-degree is restricted to a given set, satisfying
E1=E2=0 and v = (z1 h, z2 h) with h = w1^j w2^(n-j).  Prints the solution with
free parameters set to zero, to guess an all-degree closed form.
"""
import sys, json, itertools
import sympy as sp
sys.path.insert(0, __import__('os').path.dirname(__file__))
from step70_complex_model_check import z, w, ALL, conj, operators, mons, monexpr, realcoeffs

def search(n, j, zdegs):
    d = n + 2
    keys = [(0, 0), (0, 1), (1, 1)]
    ms = [m for m in mons(d) if m[0] + m[1] in zdegs]
    unknowns = []; nu = {k: 0 for k in keys}
    for k in keys:
        for m in ms:
            a, b = sp.symbols(f'a_{k[0]}{k[1]}_{"".join(map(str,m))} b_{k[0]}{k[1]}_{"".join(map(str,m))}', real=True)
            unknowns += [a, b]; nu[k] += (a + sp.I * b) * monexpr(m)
    E1, E2, v = operators(nu)
    h = w[0]**j * w[1]**(n - j)
    tgt = [sp.expand(v[0] - z[0] * h), sp.expand(v[1] - z[1] * h)]
    eqs = []
    for p in E1 + E2 + tgt:
        pd = sp.Poly(p, *ALL).as_dict() if p != 0 else {}
        for c in pd.values():
            c = sp.expand(c); eqs += [sp.re(c), sp.im(c)]
    eqs = [e for e in eqs if e != 0]
    sol = sp.linsolve(eqs, unknowns)
    if not sol:
        return None
    s = list(sol)[0]
    free = set().union(*[x.free_symbols for x in s])
    sub = dict(zip(unknowns, s)); sub = {k: v.subs({f: 0 for f in free}) for k, v in sub.items()}
    out = {str(k): sp.factor(sp.expand(nu[k].subs(sub))) for k in keys}
    return out

if __name__ == '__main__':
    n = int(sys.argv[1]); j = int(sys.argv[2]); zd = [int(x) for x in sys.argv[3].split(',')]
    r = search(n, j, zd)
    print(json.dumps({'n': n, 'j': j, 'zdegs': zd, 'nu': None if r is None else {k: str(v) for k, v in r.items()}}, indent=1))
