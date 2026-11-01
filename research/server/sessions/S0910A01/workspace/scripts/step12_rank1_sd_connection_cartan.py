#!/usr/bin/env python3
"""Cartan-solved rank-one KK toy for the Lambda^2_+ connection.

Coframe: e0,e1,e2 flat horizontal, e3 vertical, with
  de3 = C01 e01 + C02 e02 + C12 e12,
  de0=de1=de2=0.
The C_ab are allowed to vary along horizontal directions.  First solve the
Levi-Civita connection forms from Cartan's first equations rather than guessing.
Then compute the induced SO(3) connection on Lambda^2_+ and sum F_i wedge F_i.
"""
from __future__ import annotations
import sympy as sp

# exterior algebra
def inv_count(t):
    return sum(1 for i in range(len(t)) for j in range(i+1,len(t)) if t[i]>t[j])
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
C01,C02,C12=sp.symbols('C01 C02 C12', real=True)
# Here C_ab is literally the coefficient of e^a wedge e^b in de3.
de=[zero,zero,zero,add(add(scale(C01,wedge(e[0],e[1])),scale(C02,wedge(e[0],e[2]))),scale(C12,wedge(e[1],e[2])))]

# Unknown connection gamma_{ij,k} for i<j.
gam={}
unknowns=[]
for i in range(4):
    for j in range(i+1,4):
        for k in range(4):
            u=sp.symbols(f'g{i}{j}_{k}')
            gam[(i,j,k)]=u; unknowns.append(u)

def omega(i,j):
    if i==j: return zero
    sign=1
    if i>j: i,j=j,i; sign=-1
    return clean({(k,):sign*gam[(i,j,k)] for k in range(4)})

# Build linear equations de_i + sum_j omega_ij wedge e_j = 0.
eqs=[]
for i in range(4):
    form=de[i]
    for j in range(4):
        form=add(form,wedge(omega(i,j),e[j]))
    for pair in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]:
        eqs.append(sp.Eq(form.get(pair,0),0))
sol=sp.solve(eqs,unknowns, dict=True, simplify=True)
assert len(sol)==1
sol=sol[0]

def subform(A): return clean({k:sp.simplify(v.subs(sol)) for k,v in A.items()})
print('Levi-Civita connection forms omega_ij:')
for i in range(4):
    for j in range(i+1,4):
        print(f'omega{i}{j} = {subform(omega(i,j))}')

# horizontal derivatives of C symbols
derivs={}
for C in [C01,C02,C12]:
    for a in [0,1,2]: derivs[(C,a)]=sp.symbols(f'{C}_{a}', real=True)

def d_coeff(c):
    out={}
    for C in [C01,C02,C12]:
        dc=sp.diff(c,C)
        if dc!=0:
            for a in [0,1,2]: out[(a,)]=sp.simplify(out.get((a,),0)+dc*derivs[(C,a)])
    return clean(out)

def d_form(A):
    out={}
    for (i,),coef in A.items():
        out=add(out,wedge(d_coeff(coef), e[i]))
        out=add(out,scale(coef,de[i]))
    return clean(out)

# Induced connection on Lambda^2_+ in basis (01+23),(02+31),(03+12).
om={}
for i in range(4):
    for j in range(4): om[(i,j)]=subform(omega(i,j))
A=[add(om[(0,1)],om[(2,3)]), add(om[(0,2)],om[(3,1)]), add(om[(0,3)],om[(1,2)])]
print('\nA+ connection forms:')
for i,Ai in enumerate(A,1): print(f'A{i} = {Ai}')
# Try both signs for SO(3) curvature; wedge-square sum differs by exact? record plus sign.
for sign in [1,-1]:
    Fcurv=[]
    for i,(j,k) in enumerate([(1,2),(2,0),(0,1)]):
        Fcurv.append(add(d_form(A[i]), scale(sign,wedge(A[j],A[k]))))
    P={}
    for Fi in Fcurv: P=add(P,wedge(Fi,Fi))
    Pcoef=sp.factor(P.get((0,1,2,3),0))
    closure=derivs[(C12,0)] - derivs[(C02,1)] + derivs[(C01,2)]
    Pclosed=sp.factor(Pcoef.subs(derivs[(C12,0)], derivs[(C02,1)]-derivs[(C01,2)]))
    print(f'\nSO(3) curvature sign {sign}:')
    for i,Fi in enumerate(Fcurv,1): print(f'F{i} = {Fi}')
    print('Pcoef =', Pcoef)
    print('closure d(de3)=0 coeff =', closure)
    print('Pclosed =', Pclosed)
    print('P constant C =', sp.simplify(Pcoef.subs({v:0 for v in derivs.values()})))
    # Test rotating closed C: take C12=cos Y, C01=sin Y, C02=0, d/d e1 only.
    Y=sp.symbols('Y', real=True)
    subs={C12:sp.cos(Y),C01:sp.sin(Y),C02:0}
    for key in derivs: subs[derivs[key]]=0
    subs[derivs[(C12,1)]]=-sp.sin(Y)
    subs[derivs[(C01,1)]]=sp.cos(Y)
    print('Pclosed rotating C12/C01 along e1 =', sp.simplify(Pclosed.subs(subs)))
