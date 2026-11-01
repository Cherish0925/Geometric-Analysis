#!/usr/bin/env python3
"""Variable-fiber rank-one KK Cartan calibration.

Coframe at a base-geodesic point:
  de0=de1=de2=0,
  de3 = u0 e03+u1 e13+u2 e23 + C01 e01+C02 e02+C12 e12.
Here u=d log ell and C=ell F_A are scaled variables.  Horizontal base
connection is suppressed in this local toy, so base curvature terms are not yet
included.  The script solves Cartan's first equation, forms the Lambda^2_+
SO(3) connection, and extracts the 4-form coefficient of sum_i F_i wedge F_i.

Scientific use: identify whether diffuse p1 density can arise from variable
fiber length/scaled twist before adding base curvature and non-invariant errors.
"""
from __future__ import annotations
import sympy as sp

# exterior algebra
def inv_count(t): return sum(1 for i in range(len(t)) for j in range(i+1,len(t)) if t[i]>t[j])
def wedge_monom(a,b):
    if set(a)&set(b): return None,0
    t=a+b; return tuple(sorted(t)), -1 if inv_count(t)%2 else 1
def clean(A): return {k:sp.factor(v) for k,v in A.items() if sp.simplify(v)!=0}
def add(A,B):
    C=dict(A)
    for k,v in B.items(): C[k]=sp.simplify(C.get(k,0)+v)
    return clean(C)
def scale(c,A): return clean({k:sp.simplify(c*v) for k,v in A.items()})
def wedge(A,B):
    C={}
    for ka,va in A.items():
        for kb,vb in B.items():
            k,s=wedge_monom(ka,kb)
            if k is not None: C[k]=sp.simplify(C.get(k,0)+s*va*vb)
    return clean(C)

e=[{(i,):sp.Integer(1)} for i in range(4)]
zero={}
u0,u1,u2,C01,C02,C12=sp.symbols('u0 u1 u2 C01 C02 C12', real=True)
vars6=[u0,u1,u2,C01,C02,C12]
# de3 components
de3=zero
for coef,pair in [(u0,(0,3)),(u1,(1,3)),(u2,(2,3)),(C01,(0,1)),(C02,(0,2)),(C12,(1,2))]:
    de3=add(de3, scale(coef, wedge(e[pair[0]],e[pair[1]])))
de=[zero,zero,zero,de3]

# Solve Cartan for omega_ij.
gam={}; unknowns=[]
for i in range(4):
    for j in range(i+1,4):
        for k in range(4):
            s=sp.symbols(f'g{i}{j}_{k}')
            gam[(i,j,k)]=s; unknowns.append(s)
def omega_raw(i,j):
    if i==j: return zero
    sign=1
    if i>j: i,j=j,i; sign=-1
    return clean({(k,):sign*gam[(i,j,k)] for k in range(4)})
eqs=[]
for i in range(4):
    form=de[i]
    for j in range(4): form=add(form,wedge(omega_raw(i,j),e[j]))
    for pair in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]: eqs.append(sp.Eq(form.get(pair,0),0))
sol=sp.solve(eqs,unknowns, dict=True, simplify=True)[0]
def sub(A): return clean({k:sp.simplify(v.subs(sol)) for k,v in A.items()})
omega={(i,j):sub(omega_raw(i,j)) for i in range(4) for j in range(4)}
print('Levi-Civita connection with variable length:')
for i in range(4):
    for j in range(i+1,4): print(f'omega{i}{j} = {omega[(i,j)]}')

# Derivatives of variables along horizontal directions only (circle-invariant).
derivs={}
for V in vars6:
    for a in [0,1,2]: derivs[(V,a)]=sp.symbols(f'{V}_{a}', real=True)

def d_coeff(expr):
    out={}
    for V in vars6:
        dV=sp.diff(expr,V)
        if dV!=0:
            for a in [0,1,2]: out[(a,)]=sp.simplify(out.get((a,),0)+dV*derivs[(V,a)])
    return clean(out)
def d_form(A):
    """Exterior derivative for a form with coefficients depending on vars6.

    A maps ordered basis tuples I to coefficients.  Uses
    d(c e^{i1}...e^{ik}) = dc wedge e^I + c sum_m (-1)^m e^{i1}...de^{im}...e^{ik}.
    """
    out={}
    for inds,coef in A.items():
        base={inds:sp.Integer(1)}
        out=add(out,wedge(d_coeff(coef), base))
        for m,idx in enumerate(inds):
            if de[idx]:
                left={inds[:m]:sp.Integer(1)} if m>0 else {():sp.Integer(1)}
                right={inds[m+1:]:sp.Integer(1)} if m+1<len(inds) else {():sp.Integer(1)}
                term=wedge(wedge(left,de[idx]),right)
                out=add(out,scale(coef*((-1)**m),term))
    return clean(out)

# Closure d(de3)=0.
closure=d_form(de3)
print('\nclosure d(de3) components:')
for k in sorted(closure): print(k, '=', sp.factor(closure[k]))

# Induced A+ connection. We use the same basis as before.
A=[add(omega[(0,1)],omega[(2,3)]), add(omega[(0,2)],omega[(3,1)]), add(omega[(0,3)],omega[(1,2)])]
print('\nA+ connection forms:')
for i,Ai in enumerate(A,1): print(f'A{i} = {Ai}')

for sign in [1,-1]:
    Fcurv=[]
    for i,(j,k) in enumerate([(1,2),(2,0),(0,1)]): Fcurv.append(add(d_form(A[i]),scale(sign,wedge(A[j],A[k]))))
    P={}
    for Fi in Fcurv: P=add(P,wedge(Fi,Fi))
    Pcoef=sp.factor(P.get((0,1,2,3),0))
    constsubs={v:0 for v in derivs.values()}
    Pconst=sp.factor(Pcoef.subs(constsubs))
    print(f'\nSO(3) sign {sign}: P coefficient (full, may include derivative terms) =')
    print(Pcoef)
    print('Derivative-free P coefficient =')
    print(Pconst)
    # impose derivative-free closure u wedge C = 0 components by testing aligned examples.
    # Example 1: u=(u,0,0), C dual also along u => C12=c, C01=C02=0.
    u,c=sp.symbols('u c', real=True)
    aligned={u0:u,u1:0,u2:0,C12:c,C01:0,C02:0,**constsubs}
    print('aligned constant u=(u,0,0), C12=c P =', sp.factor(Pcoef.subs(aligned)))
    # Example 2: nonclosed constant u=(u,0,0), C01=c.
    nonclosed={u0:u,u1:0,u2:0,C01:c,C02:0,C12:0,**constsubs}
    print('nonclosed constant u=(u,0,0), C01=c P =', sp.factor(Pcoef.subs(nonclosed)))
    # Closure-satisfying one-jet example: u=(u,0,0), C12=C, and C12_0=u*C
    # makes d(de3)=0 at the point (other first derivatives zero).
    C=sp.symbols('C', real=True)
    closed_jet={u0:u,u1:0,u2:0,C12:C,C01:0,C02:0,**constsubs}
    closed_jet[derivs[(C12,0)]]=u*C
    print('closed one-jet u=(u,0,0), C12=C, C12_0=uC P =', sp.factor(Pcoef.subs(closed_jet)))
