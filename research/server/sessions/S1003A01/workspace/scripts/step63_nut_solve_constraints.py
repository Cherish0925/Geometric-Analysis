"""Solve the Bianchi-IX nut constant-length constraints from Step 63.

Unknowns are trace-free cubic metric anisotropy (d1,d2,d3=-d1-d2)
and leading squared form weights R_i>=0, sum R_i=1.  The exact series script
produces L_n = [u^n](sum X_i).  We eliminate R3 and study L1,L2,... .
"""
import sympy as sp, json, os
here=os.path.dirname(__file__)
D=json.load(open(os.path.join(here,'../data/step63/bix_nut_series_order5.json')))
d1,d2,R1,R2,R3=sp.symbols('d1 d2 R1 R2 R3', real=True)
loc={'d1':d1,'d2':d2,'R1':R1,'R2':R2,'R3':R3}
L=[sp.sympify(x,locals=loc) for x in D['length_conditions']]
Ls=[sp.factor(x.subs(R3,1-R1-R2)) for x in L]
print('L1=',Ls[0]); print('L2=',Ls[1])
# Groebner dimensions and factorizations as more conditions are imposed.
vars=[R1,R2,d1,d2]
out={'L_sub':[str(x) for x in Ls]}
for n in range(1,6):
    G=sp.groebner([sp.together(x).as_numer_denom()[0] for x in Ls[:n]],*vars,order='grevlex')
    print('n',n,'zero_dim',G.is_zero_dimensional,'basis',len(G.polys))
    out['G%d'%n]=[str(sp.factor(p.as_expr())) for p in G.polys]
# Numerically solve L1..L4 from many starts and check L5, positivity.
import numpy as np
from scipy.optimize import least_squares
f=sp.lambdify(vars,Ls[:4],'numpy'); f5=sp.lambdify(vars,Ls[4],'numpy')
rng=np.random.default_rng(63); sols=[]
for trial in range(300):
    z0=np.r_[rng.random(2),rng.normal(scale=.4,size=2)]
    z0[:2] /= max(1.05,z0[:2].sum()+.05)
    r=least_squares(lambda z: np.asarray(f(*z),float),z0,max_nfev=3000,xtol=1e-13,ftol=1e-13,gtol=1e-13)
    z=r.x; r3=1-z[0]-z[1]
    if np.linalg.norm(r.fun)<1e-9 and min(z[0],z[1],r3)>-1e-8:
        if not any(np.linalg.norm(z-w)<1e-5 for w in sols): sols.append(z)
print('solutions L1-L4 with Ri>=0:',len(sols))
rows=[]
for z in sols:
    row={'R':[float(z[0]),float(z[1]),float(1-z[0]-z[1])],
         'd':[float(z[2]),float(z[3]),float(-z[2]-z[3])],
         'L5':float(f5(*z))}
    rows.append(row); print(row)
out['numeric_L1_L4']=rows
od=os.path.join(here,'../data/step63');
json.dump(out,open(os.path.join(od,'bix_nut_constraints.json'),'w'),indent=1)
