"""
Step 15: flexible formal Einstein edge series with free base normal jets.

The previous rigid test fixed a(r)=cosh(sqrt(A)r), i.e. constant base curvature
-A off the rod, and failed at order r^2.  That failure is not a local obstruction
from the toric edge equations; Step 12 only fixes a_2=A at the rod.  Here we
allow
    a(r)=1 + A/2 r^2 + a4 r^4 + a6 r^6 + ...,
    P(r)=r+p3 r^3+p5 r^5+...,
    R(r)=1+R2 r^2+R4 r^4+...,
    Q''+(1+2A)Q=0.
We solve Ric(g)=g formally for the separated twist-free ansatz
    g=dr^2+a(r)^2 ds^2+P(r)^2 dtheta^2+(R(r)Q(s))^2 dphi^2.
"""
import json, os
import sympy as sp

HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.abspath(os.path.join(HERE,'..','data'))
os.makedirs(DATA,exist_ok=True)

r,A=sp.symbols('r A')
order=14
# coefficients
a_syms={k:sp.symbols(f'a{k}') for k in range(4,order,2)}
p_syms={k:sp.symbols(f'p{k}') for k in range(3,order,2)}
R_syms={k:sp.symbols(f'R{k}') for k in range(2,order,2)}
a=1 + A*r**2/2 + sum(a_syms[k]*r**k for k in a_syms)
P=r + sum(p_syms[k]*r**k for k in p_syms)
R=1 + sum(R_syms[k]*r**k for k in R_syms)
H=sp.series(sp.diff(a,r)/a,r,0,order).removeO()
K=sp.series(-sp.diff(a,r,2)/a,r,0,order).removeO()
omega2=1+2*A
u=sp.series(sp.diff(P,r)/P,r,0,order).removeO()
v=sp.series(sp.diff(R,r)/R,r,0,order).removeO()
inva2=sp.series(1/a**2,r,0,order).removeO()

E_rr=sp.series(K - sp.diff(P,r,2)/P - sp.diff(R,r,2)/R - 1,r,0,order-2).removeO().expand()
E_ss=sp.series(K - H*(u+v) + omega2*inva2 - 1,r,0,order-2).removeO().expand()
E_th=sp.series(-(sp.diff(P,r,2)+H*sp.diff(P,r))/P - u*v - 1,r,0,order-2).removeO().expand()
E_ph=sp.series(-(sp.diff(R,r,2)/R + H*v - omega2*inva2) - u*v - 1,r,0,order-2).removeO().expand()
res=[E_rr,E_ss,E_th,E_ph]

solutions={}
records=[]
# Solve by increasing even powers. At even power 0 unknowns p3,R2; a4 enters at power2.
for powr in range(0,order-4,2):
    unk=[]
    # coefficient at r^powr involves new P coeff p_{powr+3}, R_{powr+2}, a_{powr+2? maybe a4 at powr2}
    for d in [p_syms.get(powr+3), R_syms.get(powr+2), a_syms.get(powr+2), a_syms.get(powr+4)]:
        if d is not None and d not in solutions and d not in unk:
            # include a4 already when solving powr=2 via powr+2; a_{powr+4} can appear in K coefficient powr
            unk.append(d)
    eqs=[]
    for expr in res:
        coeff=sp.simplify(expr.subs(solutions).coeff(r,powr))
        if coeff!=0:
            eqs.append(coeff)
    # Filter equations to those depending on current/free unknowns; solve for all unsolved variables appearing up to this order.
    vars_in_eq=[]
    all_vars=list(p_syms.values())+list(R_syms.values())+list(a_syms.values())
    for e in eqs:
        for var in all_vars:
            if var not in solutions and var in e.free_symbols and var not in vars_in_eq:
                vars_in_eq.append(var)
    if vars_in_eq:
        sol=sp.solve(eqs, vars_in_eq, dict=True, simplify=True)
        if sol:
            s0=sol[0]
            for var,val in s0.items():
                solutions[var]=sp.simplify(val)
            records.append({'power':powr,'variables':[str(v) for v in vars_in_eq],
                            'solved':{str(k):str(v) for k,v in s0.items()},
                            'num_equations':len(eqs)})
        else:
            records.append({'power':powr,'failed':True,'variables':[str(v) for v in vars_in_eq],
                            'equations':[str(e) for e in eqs]})
            break
    else:
        # coefficients should vanish after substitutions
        records.append({'power':powr,'variables':[],'remaining_equations':[str(e) for e in eqs]})

res_solved=[sp.series(expr.subs(solutions),r,0,order-4).removeO().expand() for expr in res]
lead=[]
for name,expr in zip(['rr','ss','theta','phi'],res_solved):
    coeffs=[]
    for k in range(0,order-4):
        c=sp.simplify(expr.coeff(r,k))
        if c!=0:
            coeffs.append([k,str(c)])
    lead.append({'equation':name,'nonzero_coefficients':coeffs[:10]})

# Try to choose free coefficients zero and report first coefficients numeric/ symbolic.
solved_coeff={str(k):str(sp.factor(v)) for k,v in solutions.items()}
free_unsolved=[]
for var in list(p_syms.values())+list(R_syms.values())+list(a_syms.values()):
    if var not in solutions:
        free_unsolved.append(str(var))

report={
 'title':'Step 15 flexible formal Einstein edge series',
 'edge_parameter':'A=a2=-K_B(edge), omega^2=1+2A',
 'ansatz':'dr^2+a(r)^2ds^2+P(r)^2dtheta^2+(R(r)Q(s))^2dphi^2',
 'solved_coefficients':solved_coeff,
 'free_unsolved_coefficients':free_unsolved,
 'records':records,
 'residual_after_substitution':lead,
 'finding':('Allowing the base normal jets to vary removes the artificial obstruction of the rigid cosh-base test. The formal separated Einstein equations solve recursively through the checked order, with a4,a6,... determined along with P and R coefficients from A. Thus arbitrarily large negative edge curvature is not locally excluded by the Einstein equations; a BUILD proof must use global rod/polygon compatibility or Biquard/Ozuch-type boundary-bubble obstruction.' if all(len(x['nonzero_coefficients'])==0 for x in lead) else 'The flexible formal solve still leaves residual coefficients; inspect records.')
}
OUT=os.path.join(DATA,'step15_edge_einstein_series_flexible.json')
with open(OUT,'w') as f: json.dump(report,f,indent=2)
print(json.dumps({
 'solved_coefficients':solved_coeff,
 'free_unsolved_coefficients':free_unsolved[:10],
 'records':records,
 'residual_after_substitution':lead,
 'finding':report['finding'],
 'saved':OUT},indent=2))
