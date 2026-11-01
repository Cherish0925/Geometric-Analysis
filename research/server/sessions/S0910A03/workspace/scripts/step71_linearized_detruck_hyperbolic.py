"""Symbolic linearization of Ric+3g + (1/2)L_V g at the rank-3 hyperbolic model.

Coordinates (t,theta,x,y).  The background is
    g0 = dt^2 + exp(2t)(dtheta^2+dx^2+dy^2).
The T^2-invariant perturbation has five components
    h_tt=p, h_ttheta=q, h_thetatheta=e^{2t}r,
    h_xx=e^{2t}s, h_yy=e^{2t}u,
all depending on (t,theta).  V^k=g^{ij}(Gamma(g)^k_ij-Gamma(g0)^k_ij).
We compute the coefficient linear in eps of
    Phi = Ric(g)+3g - 1/2 L_V g,
for V^k=g^{ij}(Gamma(g)^k_ij-Gamma(g0)^k_ij).  This sign cancels the
diffeomorphism part of the Ricci principal symbol.
"""
import sympy as sp
from pathlib import Path
import json

t,z,x,y,eps=sp.symbols('t z x y eps', real=True)
coords=(t,z,x,y); n=4
p=sp.Function('p')(t,z)
q=sp.Function('q')(t,z)
r=sp.Function('r')(t,z)
s=sp.Function('s')(t,z)
u=sp.Function('u')(t,z)
e2=sp.exp(2*t)

g0=sp.diag(1,e2,e2,e2)
h=sp.zeros(4)
h[0,0]=p
h[0,1]=h[1,0]=q
h[1,1]=e2*r
h[2,2]=e2*s
h[3,3]=e2*u

g=g0+eps*h
g0inv=sp.diag(1,sp.exp(-2*t),sp.exp(-2*t),sp.exp(-2*t))
ginv=g0inv-eps*(g0inv*h*g0inv)  # sufficient to first order

def trunc(expr):
    return sp.simplify(sp.diff(expr,eps).subs(eps,0))*eps + sp.simplify(expr.subs(eps,0))

def christoffel(metric, inv):
    G=[[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    for k in range(n):
      for i in range(n):
       for j in range(n):
        val=0
        for l in range(n):
         val += inv[k,l]*(sp.diff(metric[l,j],coords[i])+sp.diff(metric[l,i],coords[j])-sp.diff(metric[i,j],coords[l]))/2
        G[k][i][j]=trunc(val)
    return G

G0=christoffel(g0,g0inv)
G=christoffel(g,ginv)

Ric=sp.MutableDenseMatrix(n,n,[0]*(n*n))
for i in range(n):
 for j in range(n):
  val=0
  for k in range(n):
   val += sp.diff(G[k][i][j],coords[k])-sp.diff(G[k][i][k],coords[j])
   for l in range(n):
    val += G[k][k][l]*G[l][i][j]-G[k][j][l]*G[l][i][k]
  Ric[i,j]=trunc(val)

# Linear DeTurck vector: background inverse contracted with delta Gamma.
V=[]
for k in range(n):
 val=0
 for i in range(n):
  for j in range(n):
   val += g0inv[i,j]*sp.diff(G[k][i][j],eps).subs(eps,0)
 V.append(sp.simplify(val))

# (L_V g0)_ij = V^k d_k g0_ij + g0_kj d_i V^k + g0_ik d_j V^k
LV=sp.MutableDenseMatrix(n,n,[0]*(n*n))
for i in range(n):
 for j in range(n):
  val=0
  for k in range(n):
   val += V[k]*sp.diff(g0[i,j],coords[k])+g0[k,j]*sp.diff(V[k],coords[i])+g0[i,k]*sp.diff(V[k],coords[j])
  LV[i,j]=sp.simplify(val)

PhiLin=sp.MutableDenseMatrix(n,n,[0]*(n*n))
for i in range(n):
 for j in range(n):
  riclin=sp.diff(Ric[i,j],eps).subs(eps,0)
  PhiLin[i,j]=sp.simplify(riclin+3*h[i,j]-sp.Rational(1,2)*LV[i,j])

# Linear Bianchi one-form beta_i = -nabla^j h_ij + 1/2 d_i tr(h).
trh=sp.simplify(sum(g0inv[i,j]*h[i,j] for i in range(n) for j in range(n)))
beta=[]
for i in range(n):
 div=0
 for j in range(n):
  for k in range(n):
   # nabla_k h_{ij}
   nab=sp.diff(h[i,j],coords[k])
   for l in range(n):
    nab -= G0[l][k][i]*h[l,j]+G0[l][k][j]*h[i,l]
   div += g0inv[j,k]*nab
 beta.append(sp.simplify(-div+sp.diff(trh,coords[i])/2))

names=['tt','tz','zz','xx','yy']
inds=[(0,0),(0,1),(1,1),(2,2),(3,3)]
print('DeTurck vector V:')
for i,vv in enumerate(V): print(i, sp.simplify(vv))
print('\nLinear Bianchi beta:')
for i,bb in enumerate(beta): print(i,bb)
print('\nPhi linear components (-1/2 L_V convention):')
out={'V':{},'beta':{},'Phi_minus':{}}
for i,vv in enumerate(V): out['V'][str(i)]=str(vv)
for i,bb in enumerate(beta): out['beta'][str(i)]=str(bb)
for nm,(i,j) in zip(names,inds):
 val=sp.simplify(PhiLin[i,j])
 print(nm,val)
 out['Phi_minus'][nm]=str(val)

path=Path(__file__).resolve().parents[1]/'data'/'step71_linearized_detruck_hyperbolic.json'
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print('\nwrote',path)
