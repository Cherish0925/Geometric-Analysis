#!/usr/bin/env python3
"""
Step 12: local rank-one circle-collapse toy computation for the Lambda^2_+
connection.

Metric model: flat 3D base, constant fiber length, invariant circle connection

    g = (e0)^2+(e1)^2+(e2)^2+(e3)^2,
    e3 = ell(dtheta+A),       de3 = ell dA

Write C_ab=(ell/2)F_ab, so de3=2(C01 e01 + C02 e02 + C12 e12).
The Levi-Civita connection forms are

    omega_ab = - C_ab e3,
    omega_a3 = - C_ab e_b,

at this flat-base constant-length level.  The induced SO(3) connection on
Lambda^2_+ is taken as

    A1 = omega01 + omega23,
    A2 = omega02 - omega13,
    A3 = omega03 + omega12.

The script computes F_i=dA_i+epsilon_ijk A_j^A_k and the coefficient of
sum_i F_i^F_i for an initial guessed connection.  It was superseded in the
same Step by `step12_rank1_sd_connection_cartan.py`, which solves Cartan's
first structural equations before computing A_+.  Keep this file only as a
record of the false vector-form guess; do not use it as evidence.
"""
from __future__ import annotations
import sympy as sp

# Simple exterior algebra on basis e0,e1,e2,e3.
def inv_count(t):
    c=0
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if t[i]>t[j]: c+=1
    return c

def wedge_monom(a,b):
    if set(a) & set(b):
        return None, 0
    t=a+b
    s=-1 if inv_count(t)%2 else 1
    return tuple(sorted(t)), s

def add(A,B):
    C=dict(A)
    for k,v in B.items():
        C[k]=sp.simplify(C.get(k,0)+v)
        if C[k]==0: C.pop(k)
    return C

def scale(c,A):
    return {k:sp.simplify(c*v) for k,v in A.items() if sp.simplify(c*v)!=0}

def wedge(A,B):
    C={}
    for ka,va in A.items():
        for kb,vb in B.items():
            k,s=wedge_monom(ka,kb)
            if k is not None:
                C[k]=sp.simplify(C.get(k,0)+s*va*vb)
    return {k:sp.simplify(v) for k,v in C.items() if sp.simplify(v)!=0}

basis=[{(i,):sp.Integer(1)} for i in range(4)]
e0,e1,e2,e3=basis

C01,C02,C12=sp.symbols('C01 C02 C12', real=True)
# Derivative symbols d(Cab)=Cab_0 e0+Cab_1 e1+Cab_2 e2. Invariant in fiber.
derivs={}
for C in [C01,C02,C12]:
    for a in [0,1,2]:
        derivs[(C,a)] = sp.symbols(f'{C}_{a}', real=True)

def one(coeffs):
    out={}
    for idx,coef in coeffs.items():
        if coef!=0:
            out[(idx,)]=sp.simplify(coef)
    return out

def d_coeff(c):
    return one({0:derivs[(c,0)],1:derivs[(c,1)],2:derivs[(c,2)]})

# de basis. de3=2(C01 e01+C02 e02+C12 e12)
de=[{}, {}, {}, add(add(scale(2*C01,wedge(e0,e1)), scale(2*C02,wedge(e0,e2))), scale(2*C12,wedge(e1,e2)))]

def d_form(A):
    # A is a 1-form with symbolic coefficients in C variables only.
    out={}
    for (i,),coef in A.items():
        # d(coef) wedge e_i + coef de_i
        dc={}
        for C in [C01,C02,C12]:
            dc=add(dc, scale(sp.diff(coef,C), d_coeff(C)))
        out=add(out, wedge(dc, basis[i]))
        out=add(out, scale(coef, de[i]))
    return out

# Connection forms omega_ij, encoded only as needed.
omega={}
def setomega(i,j,A):
    omega[(i,j)]=A
    omega[(j,i)]=scale(-1,A)

setomega(0,1,scale(-C01,e3))
setomega(0,2,scale(-C02,e3))
setomega(1,2,scale(-C12,e3))
# omega_a3=-C_ab e_b, summing over b.
setomega(0,3,add(scale(-C01,e1),scale(-C02,e2)))
setomega(1,3,add(scale(C01,e0),scale(-C12,e2)))
setomega(2,3,add(scale(C02,e0),scale(C12,e1)))

A1=add(omega[(0,1)], omega[(2,3)])
A2=add(omega[(0,2)], scale(-1, omega[(1,3)]))
A3=add(omega[(0,3)], omega[(1,2)])
A=[A1,A2,A3]

# SO(3) curvature with cyclic convention F1=dA1+A2^A3, etc.
Fcurv=[]
for i,(j,k) in enumerate([(1,2),(2,0),(0,1)]):
    Fcurv.append(add(d_form(A[i]), wedge(A[j], A[k])))

P={}
for Fi in Fcurv:
    P=add(P,wedge(Fi,Fi))
Pcoef=sp.factor(P.get((0,1,2,3),0))
# Bianchi closure for dF=0: d(C01 e01+C02 e02+C12 e12)=0 coefficient.
bianchi=sp.symbols('Bianchi')
closure=derivs[(C12,0)] - derivs[(C02,1)] + derivs[(C01,2)]
P_closed=sp.factor(Pcoef.subs(derivs[(C12,0)], derivs[(C02,1)]-derivs[(C01,2)]))

print('A+ connection forms:')
for i,Ai in enumerate(A,1): print(f'A{i} = {Ai}')
print('\nCurvature F_i:')
for i,Fi in enumerate(Fcurv,1): print(f'F{i} = {Fi}')
print('\nPontryagin raw coefficient for sum_i F_i wedge F_i:')
print(Pcoef)
print('Closure dF=0 coefficient C12_0 - C02_1 + C01_2 =')
print(closure)
print('Pontryagin coefficient after imposing closure:')
print(P_closed)
print('\nVector form: with scaled magnetic vector H=(C12,-C02,C01),')
print('the closed-form expression is proportional to H dot (curl H), up to the SO(3) normalization/sign convention.')

# Verify the H dot curl H interpretation.
H0,H1,H2=C12,-C02,C01
# curl H=(d1 H2-d2 H1, d2 H0-d0 H2, d0 H1-d1 H0)
curl0=derivs[(C01,1)] - (-derivs[(C02,2)])
curl1=derivs[(C12,2)] - derivs[(C01,0)]
curl2=(-derivs[(C02,0)]) - derivs[(C12,1)]
Hdotcurl=sp.factor(H0*curl0 + H1*curl1 + H2*curl2)
print('H dot curl H =')
print(Hdotcurl)
print('P_closed / (H dot curl H) =')
print(sp.simplify(P_closed/Hdotcurl))

# Two sanity substitutions.
subs_constant={v:0 for v in derivs.values()}
print('\nconstant twist P =', sp.simplify(Pcoef.subs(subs_constant)))
# A rotating divergence-free example H=(cos(k y),0,sin(k y)); y=e1.
k=sp.symbols('k', real=True)
subs_rot={C12:sp.cos(sp.symbols('Y')), C02:0, C01:sp.sin(sp.symbols('Y'))}
# Derivatives: only d/d e1 nonzero.
for key in derivs: subs_rot[derivs[key]]=0
Y=sp.symbols('Y', real=True)
subs_rot[derivs[(C12,1)]]=-sp.sin(Y)
subs_rot[derivs[(C01,1)]]=sp.cos(Y)
print('rotating unit H example P_closed =', sp.simplify(P_closed.subs(subs_rot)))
print('rotating unit H has H dot curl H =', sp.simplify(Hdotcurl.subs(subs_rot)))
