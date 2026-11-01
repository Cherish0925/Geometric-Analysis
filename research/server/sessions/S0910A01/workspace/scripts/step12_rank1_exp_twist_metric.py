#!/usr/bin/env python3
"""Concrete rank-one variable-length/twist metric test.

Metric on R^4:
  g = dx^2+dy^2+dz^2 + exp(2 u x) (dt + C y dz)^2.
At (x,y)=(0,0) the coordinate basis is orthonormal and
  de3 = u e03 + C e12
with the closure-compatible one-jet C12_0=u C in the Cartan toy.

This script computes Ricci, scalar, W+ eigenvalues, calibrated defect, and
Pontryagin density at the origin as functions of u,C.  It is a low-dimensional
model check, not a global collapse theorem.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp

x,y,z,t,u,C=sp.symbols('x y z t u C', real=True)
coords=[x,y,z,t]
n=4
ell2=sp.exp(2*u*x)
g=sp.zeros(n)
g[0,0]=1; g[1,1]=1; g[2,2]=1+ell2*C**2*y**2; g[2,3]=g[3,2]=ell2*C*y; g[3,3]=ell2
ginv=sp.simplify(g.inv())
pt={x:0,y:0}
print('building Christoffel/Riemann for exp-twist metric...')
Gamma=[[[sp.S(0) for k in range(n)] for j in range(n)] for i in range(n)]
for a in range(n):
  for b in range(n):
    for cc in range(n):
      Gamma[a][b][cc]=sp.simplify(sum(ginv[a,d]*(sp.diff(g[d,cc],coords[b])+sp.diff(g[d,b],coords[cc])-sp.diff(g[b,cc],coords[d])) for d in range(n))/2)
Rmix=[[[[sp.S(0) for d in range(n)] for cc in range(n)] for b in range(n)] for a in range(n)]
for a in range(n):
  for b in range(n):
    for cc in range(n):
      for d in range(n):
        val=sp.diff(Gamma[a][d][b],coords[cc])-sp.diff(Gamma[a][cc][b],coords[d])
        val+=sum(Gamma[a][cc][e]*Gamma[e][d][b]-Gamma[a][d][e]*Gamma[e][cc][b] for e in range(n))
        Rmix[a][b][cc][d]=sp.factor(sp.simplify(val.subs(pt)))
geq=sp.eye(n)  # at origin
Ric=sp.zeros(n)
for b in range(n):
  for d in range(n): Ric[b,d]=sp.factor(sum(Rmix[a][b][a][d] for a in range(n)))
scalar=sp.factor(sum(Ric[i,i] for i in range(n)))
print('Ric at origin =')
print(Ric)
print('scalar =', scalar)
print('Einstein offdiag/diagonal deviations Ric+I =')
print(sp.simplify(Ric+sp.eye(n)))

# Lower first index; at origin g=I.
Rlow=Rmix
pairs=[(0,1),(0,2),(0,3),(2,3),(3,1),(1,2)]
R6=sp.zeros(6)
for I,(a,b) in enumerate(pairs):
  for J,(cc,d) in enumerate(pairs):
    # same convention as Taub-NUT coordinate script: operator entry R_{a b d c}
    R6[I,J]=sp.factor(Rlow[a][b][d][cc])
Splus=sp.zeros(6,3); Sminus=sp.zeros(6,3)
for j in range(3):
  Splus[j,j]=1/sp.sqrt(2); Splus[j+3,j]=1/sp.sqrt(2)
  Sminus[j,j]=1/sp.sqrt(2); Sminus[j+3,j]=-1/sp.sqrt(2)
Rp=sp.simplify(Splus.T*R6*Splus); Rm=sp.simplify(Sminus.T*R6*Sminus)
Wplus=sp.simplify(Rp - scalar*sp.eye(3)/12)
Wminus=sp.simplify(Rm - scalar*sp.eye(3)/12)
print('W+ ='); print(Wplus)
print('W- ='); print(Wminus)
print('W+ eigenvals =', Wplus.eigenvals())
print('W- eigenvals =', Wminus.eigenvals())
# Pontryagin block density Pplus=2|W+|^2+s^2/24-|E|^2/2 in HS convention.
E=sp.simplify(Ric - scalar*sp.eye(n)/4)
Enorm2=sp.factor(sum(E[i,j]**2 for i in range(n) for j in range(n)))
Wpnorm2=sp.factor(sp.trace(Wplus.T*Wplus))
Wmnorm2=sp.factor(sp.trace(Wminus.T*Wminus))
Pplus=sp.factor(2*Wpnorm2 + scalar**2/sp.Integer(24) - Enorm2/sp.Integer(2))
print('|E|^2 =', Enorm2)
print('|W+|^2 =', Wpnorm2)
print('|W-|^2 =', Wmnorm2)
print('Pplus =', Pplus)

# Numerical scan for simple compatibility with Ric=-I and calibrated P.
Ric_func=sp.lambdify((u,C), Ric, 'numpy')
Wp_func=sp.lambdify((u,C), Wplus, 'numpy')
sc_func=sp.lambdify((u,C), scalar, 'numpy')
E_func=sp.lambdify((u,C), Enorm2, 'numpy')
P_func=sp.lambdify((u,C), Pplus, 'numpy')

def defect(eigs, scalar_val, En2):
    eigs=np.array(eigs,dtype=float)
    u2=float(np.sum(eigs*eigs)); un=math.sqrt(max(u2,0.0)); w=float(np.min(eigs))
    CS=(scalar_val+8*math.sqrt(6)*un)**2
    f=(2/3)*scalar_val-2*math.sqrt(2/3)*un
    a=(2/3)*scalar_val+2*w
    G=f*f-min(a,0)**2
    return CS+G+En2

best=[]
for uv in np.linspace(-3,3,121):
  for Cv in np.linspace(-4,4,161):
    R=np.array(Ric_func(uv,Cv),dtype=float)
    ricerr=float(np.linalg.norm(R+np.eye(4)))
    Wp=np.array(Wp_func(uv,Cv),dtype=float)
    eig=np.linalg.eigvalsh((Wp+Wp.T)/2)
    sc=float(sc_func(uv,Cv)); En2=float(E_func(uv,Cv)); P=float(P_func(uv,Cv))
    Fcal=defect(eig,sc,En2)
    score=ricerr+abs(P-0.75)+0.05*Fcal
    best.append((score,uv,Cv,ricerr,sc,En2,float(np.sum(eig*eig)),P,Fcal,eig))
best=sorted(best,key=lambda x:x[0])[:12]
print('\nBest coarse grid rows score,u,C,RicErr,scalar,|E|2,|W+|2,Pplus,Fcal,eigs:')
for row in best:
  print(row[:-1], row[-1])
