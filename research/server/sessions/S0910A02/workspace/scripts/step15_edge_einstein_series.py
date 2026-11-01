"""
Step 15: formal Einstein edge series for a large negative-curvature rod.

We study a local twist-free separated model near a p=0 rod:
    g = dr^2 + a(r)^2 ds^2 + P(r)^2 dtheta^2 + (R(r)Q(s))^2 dphi^2,
    a(r)=cosh(sqrt(A) r),   K_B=-A,
    Q'' + omega^2 Q=0,      omega^2=1+2A,
with Ric(g)=g.  The Step-12/14 edge equations give
    P=r+(-A/3-1/6)r^3+..., R=1+(A/2)r^2+...
This script recursively solves the Einstein ODE residuals for higher formal
coefficients.  It tests whether large negative edge curvature is locally
incompatible with Ric=g (it is not, at least formally to the checked order).
"""
import json, math, os
import sympy as sp
import numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.abspath(os.path.join(HERE,"..","data"))
os.makedirs(DATA,exist_ok=True)

r,A=sp.symbols('r A', positive=True)
max_order=12
# unknown coefficients: P=r+p3 r^3+...+p11 r^11, R=1+r2 r^2+...+r10 r^10
p_syms={k: sp.symbols(f'p{k}') for k in range(3,max_order,2)}
r_syms={k: sp.symbols(f'R{k}') for k in range(2,max_order,2)}
P=r+sum(p_syms[k]*r**k for k in p_syms)
R=1+sum(r_syms[k]*r**k for k in r_syms)
# series for H=a'/a=sqrtA tanh(sqrtA r), avoid sqrt by series in A
H=sp.series(sp.sqrt(A)*sp.tanh(sp.sqrt(A)*r), r, 0, max_order).removeO()
omega2=1+2*A
u=sp.diff(P,r)/P
v=sp.diff(R,r)/R
# residuals Ric-g=0
E_rr = -A - sp.diff(P,r,2)/P - sp.diff(R,r,2)/R - 1
E_ss = -A - H*(u+v) + omega2*(1 - sp.tanh(sp.sqrt(A)*r)**2).series(r,0,max_order).removeO() - 1  # omega2/a^2
E_th = -(sp.diff(P,r,2)+H*sp.diff(P,r))/P - u*v - 1
E_ph = -(sp.diff(R,r,2)/R + H*v - omega2*(1 - sp.tanh(sp.sqrt(A)*r)**2).series(r,0,max_order).removeO()) - u*v - 1
residuals=[sp.series(expr, r, 0, max_order-1).removeO().expand() for expr in [E_rr,E_ss,E_th,E_ph]]

# Sequentially solve coefficients by increasing even residual order.  Because P has a zero,
# residuals may contain r^-? terms; the chosen p3/R2 should remove constants.
unknowns=[]
solutions={}
records=[]
for target_even in range(0, max_order-3, 2):
    # Add next pair of unknowns p_{target+3}, R_{target+2} when available.
    pk=target_even+3
    rk=target_even+2
    new=[]
    if pk in p_syms and p_syms[pk] not in solutions: new.append(p_syms[pk])
    if rk in r_syms and r_syms[rk] not in solutions: new.append(r_syms[rk])
    unknowns.extend(new)
    eqs=[]
    for expr in residuals:
        ex=sp.series(expr.subs(solutions), r, 0, target_even+1).removeO().expand()
        coeff=sp.expand(ex).coeff(r,target_even)
        if coeff!=0:
            eqs.append(coeff)
    # Use only equations involving current unknowns; solve all if possible.
    if unknowns and eqs:
        sol=sp.solve(eqs, unknowns, dict=True, simplify=True)
        if sol:
            # choose first, update all solved among unknowns
            s0=sol[0]
            for var,val in s0.items():
                solutions[var]=sp.simplify(val)
            unknowns=[v for v in unknowns if v not in solutions]
            records.append({'order':target_even,'solved':{str(k):str(v) for k,v in s0.items()},'num_equations':len(eqs)})
        else:
            records.append({'order':target_even,'failed_eqs':[str(e) for e in eqs],'unknowns':[str(u) for u in unknowns]})
            break

# Substitute solutions and inspect leading residual orders.
solved_res=[sp.series(expr.subs(solutions), r, 0, max_order-1).removeO().expand() for expr in residuals]
lead_terms=[]
for name,expr in zip(['rr','ss','theta','phi'], solved_res):
    coeffs=[]
    for k in range(0,max_order-1):
        c=sp.simplify(expr.coeff(r,k))
        if c!=0:
            coeffs.append((k,str(c)))
    lead_terms.append({'equation':name,'nonzero_coefficients_up_to_checked_order':coeffs[:5]})

# numerical functions for truncated series at chosen A
solP=sp.simplify(P.subs(solutions))
solR=sp.simplify(R.subs(solutions))
# lambdify residuals using solved series with H exact numeric (use formulas directly in Python)
coeff_P=[(k, sp.simplify(p_syms[k].subs(solutions))) for k in p_syms if p_syms[k] in solutions]
coeff_R=[(k, sp.simplify(r_syms[k].subs(solutions))) for k in r_syms if r_syms[k] in solutions]

def eval_coeff(expr,Aval): return float(sp.N(expr.subs(A,Aval)))

def ricci_eigs_series(Aval,c):
    sqrtA=math.sqrt(Aval); omega2v=1+2*Aval; r0=c/sqrtA
    # polynomial and derivatives
    pc=[(1,1.0)]+[(k,eval_coeff(v,Aval)) for k,v in coeff_P]
    rc=[(0,1.0)]+[(k,eval_coeff(v,Aval)) for k,v in coeff_R]
    def poly(coefs,der=0):
        s=0.0
        for k,a in coefs:
            if k>=der:
                fac=1
                for j in range(der): fac*=k-j
                s += a*fac*r0**(k-der)
        return s
    P0,P1,P2=poly(pc,0),poly(pc,1),poly(pc,2)
    R0,R1,R2=poly(rc,0),poly(rc,1),poly(rc,2)
    H0=sqrtA*math.tanh(sqrtA*r0)
    inva2=1/(math.cosh(sqrtA*r0)**2)
    u0=P1/P0; v0=R1/R0
    eig_rr=-Aval-P2/P0-R2/R0
    eig_ss=-Aval-H0*(u0+v0)+omega2v*inva2
    eig_th=-(P2+H0*P1)/P0-u0*v0
    eig_ph=-(R2/R0+H0*v0-omega2v*inva2)-u0*v0
    eigs=[eig_rr,eig_ss,eig_th,eig_ph]
    return {'A':Aval,'c':c,'r':r0,'eigs':eigs,'delta':max(abs(x-1) for x in eigs),'P':P0,'R':R0}

samples=[]
for Aval in [36,64,100,400,1600,10000]:
    for c in [0.01,0.02,0.05,0.1,0.2,0.4]:
        samples.append(ricci_eigs_series(Aval,c))
# best c threshold with delta<0.05 per A
thresholds=[]
for Aval in [36,64,100,400,1600,10000]:
    good=[s for s in samples if s['A']==Aval and s['delta']<0.05]
    thresholds.append({'A':Aval,'max_sampled_c_with_delta_lt_0.05':max([g['c'] for g in good], default=None),
                       'min_delta_sample':min([s['delta'] for s in samples if s['A']==Aval])})

report={
 'title':'Step 15 formal Einstein edge series for arbitrary negative K_B=-A',
 'ansatz':'dr^2+cosh(sqrt(A)r)^2 ds^2+P(r)^2 dtheta^2+(R(r) sin(omega s)/omega)^2 dphi^2, omega^2=1+2A',
 'solved_coefficients':{str(k):str(sp.simplify(v)) for k,v in solutions.items()},
 'solution_records':records,
 'residual_leading_terms':lead_terms,
 'numeric_samples':samples,
 'delta_thresholds':thresholds,
 'finding':('Rigid test with a(r)=cosh(sqrt(A)r) solves only the leading Step-12 coefficients R2=A/2 and p3=-A/3-1/6, then fails at order r^2. This failure is an artifact of freezing the off-rod base curvature to be constant: Step 12 fixed only the rod value a2=A, not all base normal jets. Do not use this file as evidence of a local Einstein obstruction; use step15_edge_einstein_series_flexible.json and step15_edge_germ_first_integral.json for the repaired local analysis.'),
 'limitations':['separated twist-free local ansatz only','formal/truncated series, not a closed metric','does not prove convergence or gluing compatibility']
}
OUT=os.path.join(DATA,'step15_edge_einstein_series.json')
with open(OUT,'w') as f: json.dump(report,f,indent=2)
print(json.dumps({
 'solved_coefficients':report['solved_coefficients'],
 'residual_leading_terms':lead_terms,
 'thresholds':thresholds,
 'selected_samples':[{'A':s['A'],'c':s['c'],'delta':s['delta'],'eigs':s['eigs']} for s in samples if s['A'] in [100,1600,10000] and s['c'] in [0.05,0.1,0.2]],
 'saved':OUT},indent=2))
