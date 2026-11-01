"""Exact small polynomial test of a proposed top-kernel explanation.

This checks the polarization of the Step-65 homogeneous torsion identity.
It does NOT establish its identification with the full Darboux metric jet map.
All algebra is over Q(i), with z and w=bar(z) treated independently.
"""
from pathlib import Path
import json
import sympy as sp

WS = Path(__file__).resolve().parents[1]
z1, z2, w1, w2 = variables = sp.symbols('z1 z2 w1 w2', real=True)
z = sp.Matrix([z1, z2])
w = (w1, w2)
I = sp.I


def involution(p):
    return sp.conjugate(p).xreplace({z1:w1, z2:w2, w1:z1, w2:z2})


def mons(n, length=4):
    if length == 1:
        return [(n,)]
    return [(a,) + tail for a in range(n+1) for tail in mons(n-a, length-1)]


def polarized(c, B, h, g, n):
    """Derivative is -2 Re[ tr(bar B Dg)+(3n+8)bar c h+4 Dh.bar B.z ]."""
    Dh = sp.Matrix([sp.diff(h, t) for t in w])
    Dg = g.jacobian(w)
    q = sp.trace(sp.conjugate(B)*Dg) + (3*n+8)*sp.conjugate(c)*h
    q += 4*(Dh.T*sp.conjugate(B)*z)[0]
    return sp.expand(-q-involution(q))


def matrix(c, B, n):
    columns = []
    labels = []
    zero = sp.zeros(2,1)
    for j in range(n+1):
        h0 = w1**j*w2**(n-j)
        for p, name in ((1,'re'),(I,'im')):
            columns.append(polarized(c, B, p*h0, zero, n))
            labels.append(f'h{j}_{name}')
    for k in range(2):
        for j in range(n+2):
            for p, name in ((1,'re'),(I,'im')):
                g = sp.zeros(2,1)
                g[k] = p*w1**j*w2**(n+1-j)
                columns.append(polarized(c, B, 0, g, n))
                labels.append(f'g{k}_{j}_{name}')
    monomials = mons(n)
    rows = []
    pd = [sp.Poly(p, *variables).as_dict() for p in columns]
    for exponent in monomials:
        v = [p.get(exponent, sp.S.Zero) for p in pd]
        rows.append([sp.re(q) for q in v])
        rows.append([sp.im(q) for q in v])
    A = sp.Matrix(rows)
    radial = []
    if n % 2 == 0:
        for p in columns:
            for _ in range(n//2):
                p = 4*(sp.diff(p,z1,w1)+sp.diff(p,z2,w2))
            radial.append(sp.expand(p))
    return A, radial, columns


S = sp.Matrix([[2,1],[1,1+I]])
B = S + sp.Matrix([[0,2+2*I],[-2-2*I,0]])
cases = [('strict_cone', sp.S.One, B),
         ('rank_one_GH', sp.S.Zero, sp.Matrix([[0,1],[0,0]])),
         ('kahler', sp.S.Zero, sp.zeros(2))]
records = []
for name, c, Bb in cases:
    for n in (2,4,6,8):
        A, radial, columns = matrix(c, Bb, n)
        rank = A.rank()
        support = sorted({(sum(e[:2]),sum(e[2:]))
                          for p in columns for e in sp.Poly(p,*variables).as_dict()})
        rec = {'case':name, 'metric_jet_degree_d':n+2,
               'scalar_degree_n':n, 'exact_rank':int(rank),
               'radial_row_zero':all(r==0 for r in radial),
               'holomorphic_antiholomorphic_bidegrees':support}
        print(json.dumps(rec),flush=True)
        records.append(rec)
        if name == 'strict_cone':
            assert rank == (10 if n==2 else 4*(n+1))
        elif name == 'rank_one_GH':
            assert rank == (9 if n==2 else 4*n+2)
        else:
            assert rank==0
        if n>=4:
            assert all(r==0 for r in radial)

out = WS/'data/spirit_step68'
out.mkdir(exist_ok=True)
(out/'top_channel_polarization.json').write_text(json.dumps({
    'status':'Exact polarization algebra only; full metric-channel correspondence remains to be checked',
    'records':records
},indent=2)+'\n')
