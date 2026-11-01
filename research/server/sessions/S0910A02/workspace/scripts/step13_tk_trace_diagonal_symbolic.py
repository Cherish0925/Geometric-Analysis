"""
Step 13 (S0910A02): symbolic check of the determinant trace for diagonal
T^k-invariant metrics without twist.

Metric: g = dx^2 + dy^2 + sum_i p_i(x,y)^2 dtheta_i^2.
Let w=prod_i p_i.  For k=1,2,3 this script verifies at a generic point:
    tr_h Ric^V = - Delta(log w) - sum_i |grad log p_i|^2
               = - Delta w / w
(the cancellation uses Delta w / w = Delta log w + |grad log w|^2 and the
vertical trace includes the pairwise gradient terms).  In Einstein scale
Ric=lambda g this gives (-Delta)w = k*lambda*w.

This does not include twist or non-diagonal h; Step 12 verified those in k=2.
"""
import json, os
import sympy as sp

x, y = sp.symbols('x y')


def ricci_tensor(coords, g):
    n = len(coords)
    ginv = sp.simplify(g.inv())
    Gamma = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                Gamma[a][b][c] = sp.simplify(sp.Rational(1,2)*sum(
                    ginv[a,d]*(sp.diff(g[d,c], coords[b]) + sp.diff(g[d,b], coords[c]) - sp.diff(g[b,c], coords[d]))
                    for d in range(n)))
    Ric = [[0 for _ in range(n)] for _ in range(n)]
    for b in range(n):
        for d in range(n):
            expr = 0
            for a in range(n):
                expr += sp.diff(Gamma[a][b][d], coords[a]) - sp.diff(Gamma[a][b][a], coords[d])
                for e in range(n):
                    expr += Gamma[a][a][e]*Gamma[e][b][d] - Gamma[a][d][e]*Gamma[e][b][a]
            Ric[b][d] = sp.simplify(expr)
    return Ric, ginv

reports = {}
for k in [1,2,3]:
    ps = [sp.Function(f'p{i+1}')(x,y) for i in range(k)]
    coords = [x,y] + [sp.symbols(f't{i+1}') for i in range(k)]
    diag = [1,1] + [p**2 for p in ps]
    g = sp.diag(*diag)
    Ric, ginv = ricci_tensor(coords, g)
    tr_vert = sp.simplify(sum(ginv[2+i,2+i]*Ric[2+i][2+i] for i in range(k)))
    w = sp.prod(ps)
    minus_Delta_w_over_w = sp.simplify(-(sp.diff(w,x,2)+sp.diff(w,y,2))/w)
    diff = sp.simplify(tr_vert - minus_Delta_w_over_w)
    reports[f'k={k}'] = {
        'tr_h_RicV': str(tr_vert),
        'minus_Delta_w_over_w': str(minus_Delta_w_over_w),
        'difference_simplified': str(diff),
        'Einstein_implication': f'If Ric=lambda*g then -Delta w = {k}*lambda*w'
    }

OUT = 'Sessions/S0910A02/workspace/data/step13_tk_trace_diagonal_symbolic.json'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(reports, f, indent=2)
print(json.dumps(reports, indent=2))
print(f'Saved {OUT}')
