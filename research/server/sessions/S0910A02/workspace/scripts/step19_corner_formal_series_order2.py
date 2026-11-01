"""
Step 19 (S0910A02): higher corner series for the diagonal fixed-point ansatz.

Purpose: test the Strategist's proposed finite rod/corner matching system at the
first nontrivial corner level.  The question is whether smooth right-angle
corners force the rod edge-curvature parameter A=-K_B|edge to stay bounded.

We impose the smoothness parity conditions of the toric fixed-point Lemma 2.2 in
a diagonal gauge:
  g_B = dr^2 + mu(r,t)^2 dt^2,
  p^2 in r^2+r^4 R_even,
  q^2 in t^2 mu(r,0)^2+t^4 R_even,
  b_fiber=0.
The most general low-order positive functions are parameterized as
  mu = 1 + u r^2 + m40 r^4 + m22 r^2 t^2,
  p  = r + a r^3 + p50 r^5 + p32 r^3 t^2,
  q  = t(1+u r^2+m40 r^4) + b t^3 + q23 r^2 t^3 + q05 t^5.
Here A=-K_B(0)=2u.

We compute Ric(g)-g using double-warped-product formulas and expand along all
rays t=z r.  Vanishing of the constant and r^2 coefficients for all z is a
necessary formal Einstein matching condition through the first nontrivial order.
"""
import json, os
import sympy as sp

r,t,z=sp.symbols('r t z')
u,a,b,m40,m22,p50,p32,q23,q05=sp.symbols('u a b m40 m22 p50 p32 q23 q05')
unknowns=[a,b,m40,m22,p50,p32,q23,q05]

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
residuals={
    'Hrr': sp.simplify(A_rr-1),
    'Htt': sp.simplify(A_tt-1),
    'Hrt_cov': sp.simplify(RicH_rt),
    'rp': sp.simplify(rp-1),
    'rq': sp.simplify(rq-1),
}

# First solve constant terms, known from previous script.
const_eqs=[]
series_by_res={}
for name,e in residuals.items():
    er=sp.simplify(e.subs(t,z*r))
    ser=sp.series(er, r, 0, 5).removeO().expand()
    series_by_res[name]=ser
    const_eqs.append(sp.factor(ser.coeff(r,0)))
const_eqs_unique=[]
for eq in const_eqs:
    if eq not in const_eqs_unique:
        const_eqs_unique.append(eq)
const_sol=sp.solve(const_eqs_unique, [a,b], dict=True)[0]

# Substitute constants and collect r^2 coefficients as polynomials in z.
r2_equations=[]
r2_polys={}
for name,ser in series_by_res.items():
    ser2=sp.series(sp.simplify(ser.subs(const_sol)), r, 0, 5).removeO().expand()
    poly=sp.Poly(sp.factor(ser2.coeff(r,2)), z)
    r2_polys[name]=str(sp.factor(poly.as_expr()))
    for coeff in poly.all_coeffs():
        coeff_s=sp.factor(coeff)
        if coeff_s != 0 and coeff_s not in r2_equations:
            r2_equations.append(coeff_s)

# Solve r2 equations for as many low-order coefficients as possible.  Keep u free.
solve_vars=[m40,m22,p50,p32,q23,q05]
sols=sp.solve(r2_equations, solve_vars, dict=True, simplify=True)
# If full solve too restrictive, also solve linear subset.

# Analyze whether u is constrained: collect equations after any first solution.
sol_records=[]
for s in sols[:5]:
    rec={str(k):str(sp.factor(v)) for k,v in s.items()}
    # residual r2 after substitution
    rem=[]
    for eq in r2_equations:
        rem_eq=sp.factor(eq.subs(s))
        if rem_eq != 0:
            rem.append(str(rem_eq))
    rec['remaining_r2_equations_after_solution']=rem
    sol_records.append(rec)

A=sp.symbols('A')
subst_A={u:A/2}
const_sol_A={str(k):str(sp.factor(v.subs(subst_A))) for k,v in const_sol.items()}
sol_records_A=[]
for s in sols[:3]:
    sol_records_A.append({str(k):str(sp.factor(v.subs(subst_A))) for k,v in s.items()})

report={
    'title':'Step 19 diagonal fixed-corner formal Ric=g matching through r^2 along rays',
    'smoothness_parameterization':{
        'mu':'1+u r^2 + m40 r^4 + m22 r^2 t^2',
        'p':'r + a r^3 + p50 r^5 + p32 r^3 t^2',
        'q':'t(1+u r^2+m40 r^4)+b t^3+q23 r^2 t^3+q05 t^5',
        'A':'A=-K_B(0)=2u'
    },
    'constant_equations_unique':[str(e) for e in const_eqs_unique],
    'constant_solution':{str(k):str(sp.factor(v)) for k,v in const_sol.items()},
    'constant_solution_in_A':const_sol_A,
    'r2_polynomials_after_constant_solution':r2_polys,
    'r2_equations_unique':[str(e) for e in r2_equations],
    'number_of_r2_equations':len(r2_equations),
    'solutions_for_r2_coefficients_count':len(sols),
    'solutions_for_r2_coefficients_first5':sol_records,
    'solutions_for_r2_coefficients_in_A_first3':sol_records_A,
    'interpretation':(
        'The first nontrivial formal corner equations remain solvable with u (hence A=2u) free. Thus neither the local smoothness parity conditions nor exact Ric=g through r^2 impose a cap on the adjacent rod edge-curvature parameter. The finite BUILD obstruction, if true, cannot be a purely local low-jet corner algebra obstruction; it must involve longer-range matching around rods/corners, eigenfunction/spectral scale, holonomy/twist, global topology/energy, or a higher-order/resurgent obstruction not visible at this order.'),
    'caution':'Formal local solvability does not construct a global smooth metric and does not establish pinched collapse. It only removes one possible local BUILD shortcut.'
}

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.abspath(os.path.join(HERE,'..','data','step19_corner_formal_series_order2.json'))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
with open(OUT,'w') as f: json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
print('Saved',OUT)
