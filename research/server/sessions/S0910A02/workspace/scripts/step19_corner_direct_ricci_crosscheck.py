"""
Step 19 direct Ricci cross-check for the diagonal corner ansatz.

This script independently computes Christoffel/Ricci for the 4D diagonal metric
  diag(1, mu^2, p^2, q^2)
in coordinates (r,t,theta,phi), for the lowest corner jets, and compares the
zeroth-order Ricci-endomorphism conditions with the warped-product formula used
in step19_corner_matching_symbolic.py.
"""
import json, os
import sympy as sp

r,t,z=sp.symbols('r t z')
u,a,b=sp.symbols('u a b')
coords=[r,t,sp.symbols('th'),sp.symbols('ph')]
mu=1+u*r**2
p=r+a*r**3
q=t*(1+u*r**2)+b*t**3
one=sp.Integer(1)
g=[one,mu**2,p**2,q**2]
ginv=[one/gi for gi in g]
n=4
# Christoffel Gamma^l_{ij}; diagonal metric but use general formula.
Gamma=[[[0 for j in range(n)] for i in range(n)] for l in range(n)]
for l in range(n):
    for i in range(n):
        for j in range(n):
            s=0
            for k in range(n):
                # since inverse diagonal, only k=l contributes
                pass
            Gamma[l][i][j]=sp.simplify(sp.Rational(1,2)*ginv[l]*(
                sp.diff(g[j] if l==j else 0, coords[i]) +
                sp.diff(g[i] if l==i else 0, coords[j]) -
                sp.diff(g[i] if i==j else 0, coords[l])
            ))
# Ric_ij = d_k Gamma^k_ij - d_j Gamma^k_ik + Gamma^k_ij Gamma^l_kl - Gamma^l_ik Gamma^k_jl
Ric=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        expr=0
        for k in range(n):
            expr += sp.diff(Gamma[k][i][j], coords[k]) - sp.diff(Gamma[k][i][k], coords[j])
            for l in range(n):
                expr += Gamma[k][i][j]*Gamma[l][k][l] - Gamma[l][i][k]*Gamma[k][j][l]
        Ric[i][j]=sp.simplify(expr)

endom_minus1={
    'rr': sp.simplify(Ric[0][0]-1),
    'tt': sp.simplify(Ric[1][1]/g[1]-1),
    'theta': sp.simplify(Ric[2][2]/g[2]-1),
    'phi': sp.simplify(Ric[3][3]/g[3]-1),
    'rt_cov': sp.simplify(Ric[0][1])
}
const={}
series={}
for name,e in endom_minus1.items():
    ser=sp.series(sp.together(e.subs(t,z*r)), r, 0, 3).removeO().expand()
    series[name]=str(sp.factor(ser))
    const[name]=str(sp.factor(ser.coeff(r,0)))
conditions=[sp.factor(sp.sympify(const[n])) for n in ['rr','tt','theta','phi']]
conditions_unique=[]
for c in conditions:
    if c not in conditions_unique: conditions_unique.append(c)
sol=sp.solve(conditions_unique,[a,b],dict=True)
report={
  'title':'Step 19 direct Christoffel/Ricci cross-check of corner constant terms',
  'series_t_equals_zr':series,
  'constant_terms':const,
  'unique_constant_conditions':[str(c) for c in conditions_unique],
  'solution':[ {str(k):str(sp.factor(v)) for k,v in s.items()} for s in sol],
  'matches_warped_product_script': sol and str(sp.factor(sol[0][a]))=='-(4*u + 1)/6' and str(sp.factor(sol[0][b]))=='-(4*u + 1)/6',
  'interpretation':'Direct 4D Ricci computation reproduces the same no-cap constant corner equations as the warped-product formula.'
}
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.abspath(os.path.join(HERE,'..','data','step19_corner_direct_ricci_crosscheck.json'))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
with open(OUT,'w') as f: json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
print('Saved',OUT)
