"""
Fast version of Step 19 corner formal series.

This avoids full rational simplification. It substitutes t=z*r after taking the
needed partial derivatives and extracts Laurent coefficients in r.  It then
solves the constant and r^2 coefficient equations by linear algebra.
"""
import json, os
import sympy as sp

r,t,z=sp.symbols('r t z')
u,a,b,m40,m22,p50,p32,q23,q05=sp.symbols('u a b m40 m22 p50 p32 q23 q05')

mu=1+u*r**2+m40*r**4+m22*r**2*t**2
p=r+a*r**3+p50*r**5+p32*r**3*t**2
q=t*(1+u*r**2+m40*r**4)+b*t**3+q23*r**2*t**3+q05*t**5

mur=sp.diff(mu,r); mut=sp.diff(mu,t)
K=-sp.diff(mu,r,2)/mu

def hess(f):
    fr,ft=sp.diff(f,r),sp.diff(f,t)
    frr,frt,ftt=sp.diff(f,r,2),sp.diff(f,r,t),sp.diff(f,t,2)
    Hrr=frr
    Hrt=frt - (mur/mu)*ft
    Htt=ftt + mu*mur*fr - (mut/mu)*ft
    return Hrr,Hrt,Htt

def lap(f):
    Hrr,Hrt,Htt=hess(f)
    return Hrr + Htt/mu**2

def inner(f,g):
    return sp.diff(f,r)*sp.diff(g,r) + sp.diff(f,t)*sp.diff(g,t)/mu**2

Hp=hess(p); Hq=hess(q)
RicH_rr=K - Hp[0]/p - Hq[0]/q
RicH_rt= - Hp[1]/p - Hq[1]/q
RicH_tt=K*mu**2 - Hp[2]/p - Hq[2]/q
A_rr=RicH_rr
A_tt=RicH_tt/mu**2
rp= -lap(p)/p - inner(p,q)/(p*q)
rq= -lap(q)/q - inner(p,q)/(p*q)
residuals={'Hrr':A_rr-1,'Htt':A_tt-1,'Hrt_cov':RicH_rt,'rp':rp-1,'rq':rq-1}

def coeffs_along(expr, max_order=5):
    e=expr.subs(t,z*r)
    # together before series is much faster/safer for Laurent cancellation than simplify.
    ser=sp.series(sp.together(e), r, 0, max_order).removeO().expand()
    return ser

series0={name: coeffs_along(e,5) for name,e in residuals.items()}
const_eqs=[]
for name,ser in series0.items():
    c=sp.factor(ser.coeff(r,0))
    if c!=0 and c not in const_eqs:
        const_eqs.append(c)
const_sol=sp.solve(const_eqs,[a,b], dict=True)[0]

r2_polys={}
r2_eqs=[]
for name,ser in series0.items():
    ser2=sp.series(sp.together(ser.subs(const_sol)), r, 0, 5).removeO().expand()
    c2=sp.factor(ser2.coeff(r,2))
    # Treat as rational in z; numerator coefficients must vanish for all z.
    num,den=sp.fraction(sp.together(c2))
    poly=sp.Poly(sp.expand(num), z)
    r2_polys[name]=str(sp.factor(c2))
    for coeff in poly.coeffs():
        coeff=sp.factor(coeff)
        if coeff!=0 and coeff not in r2_eqs:
            r2_eqs.append(coeff)

# The system is linear in the higher coefficients; solve manually by linsolve.
vars2=[m40,m22,p50,p32,q23,q05]
A_mat,b_vec=sp.linear_eq_to_matrix(r2_eqs, vars2)
solset=sp.linsolve((A_mat,b_vec), vars2)
sol_tuple=list(solset)[0]
sol_map={v:sp.factor(sol_tuple[i]) for i,v in enumerate(vars2)}
# Remaining symbolic parameters are free if they appear on RHS.
free_symbols=sorted([str(s) for expr in sol_tuple for s in expr.free_symbols if s not in {u}], key=str)

Apar=sp.symbols('A')
subA={u:Apar/2}
report={
 'title':'Step 19 fast corner formal series through r^2',
 'constant_eqs':[str(e) for e in const_eqs],
 'constant_solution':{str(k):str(sp.factor(v)) for k,v in const_sol.items()},
 'constant_solution_in_A':{str(k):str(sp.factor(v.subs(subA))) for k,v in const_sol.items()},
 'r2_polynomials_after_constant_solution':r2_polys,
 'r2_equations_count':len(r2_eqs),
 'r2_equations':[str(e) for e in r2_eqs],
 'linear_system_rank':int(A_mat.rank()),
 'unknown_count':len(vars2),
 'solution_one_affine_family':{str(k):str(v) for k,v in sol_map.items()},
 'solution_one_affine_family_in_A':{str(k):str(sp.factor(v.subs(subA))) for k,v in sol_map.items()},
 'free_parameters_besides_u':free_symbols,
 'interpretation':('Exact Ric=g formal corner matching through the r^2 coefficient along all rays is solvable with u, hence A=-K_B(0)=2u, free. Therefore the periodic standard-basis diagonal ansatz is locally smooth at corners and no low-order algebraic corner condition caps the large negative edge curvature used in the boundary-bubble collapse seed.'),
 'caution':'Necessary local formal matching only; no global polygon metric or Yau-26 conclusion.'
}

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.abspath(os.path.join(HERE,'..','data','step19_corner_formal_series_order2_fast.json'))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
with open(OUT,'w') as f: json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
print('Saved',OUT)
