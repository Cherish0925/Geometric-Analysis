#!/usr/bin/env python3
"""Direct local tensor check for the Step-67 product-saddle claim.

Use H^2_{K1=-A^2} x H^2_{K2=-B^2} and a holomorphic quadratic
differential q(z) dz^2.  The code permits q=z^n (n=0,1,2), expands the
fixed-area compatible exponential family g_t=g_1 exp(t f g_1^{-1}Re q)+g_2,
and evaluates the normalized t^2 coefficient of |Ric^0|^2 dvol at z=i.
The three choices have different jets but all satisfy the holomorphic/Codazzi
equations. Agreement would establish jet independence; disagreement exposes
which derivatives still have to be integrated using the global Bochner law.
"""
from pathlib import Path
import argparse,json,sympy as sp
ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=1);args=ap.parse_args();n=args.n
N=3
def add(a,b):return [a[i]+b[i] for i in range(N)]
def sub(a,b):return [a[i]-b[i] for i in range(N)]
def mul(a,b):return [sum((a[j]*b[i-j] for j in range(i+1)),sp.S.Zero) for i in range(N)]
def scale(a,s):return [s*z for z in a]
def der(a,z):return [sp.diff(w,z) for w in a]
def C(z):return [z,0,0]
def S(z):return sp.factor(sp.cancel(sp.together(z)))
x,u,y,v=sp.symbols('x u y v',positive=True,real=True);A,B,mu=sp.symbols('A B mu',positive=True,real=True);f=sp.Function('f')(v);co=[x,u,y,v];c=1/(A**2*u**2);d=1/(B**2*v**2)
z=(x+sp.I*u)**n;qr=sp.re(sp.expand_complex(z));qi=sp.im(sp.expand_complex(z));Q=sp.Matrix([[qr,-qi],[-qi,-qr]]);M=A**2*u**2*f*Q;M2=S((M*M)[0,0])
g=[[[0,0,0]for _ in range(4)]for _ in range(4)];gi=[[[0,0,0]for _ in range(4)]for _ in range(4)]
for i in range(2):
 for j in range(2):
  e=1 if i==j else 0;g[i][j]=[c*e,c*M[i,j],c*M2*e/2];gi[i][j]=[(1/c)*e,-M[i,j]/c,M2*e/(2*c)]
for i in (2,3):g[i][i]=C(d);gi[i][i]=C(1/d)
G=[[[C(0)for _ in range(4)]for _ in range(4)]for _ in range(4)]
for i in range(4):
 for j in range(4):
  for k in range(4):
   r=C(0)
   for l in range(4):r=add(r,scale(mul(gi[i][l],sub(add(der(g[l][j],co[k]),der(g[l][k],co[j])),der(g[j][k],co[l]))),sp.Rational(1,2)))
   G[i][j][k]=r
Ric=[[C(0)for _ in range(4)]for _ in range(4)]
for j in range(4):
 for k in range(4):
  r=C(0)
  for i in range(4):
   r=add(r,der(G[i][j][k],co[i]));r=sub(r,der(G[i][j][i],co[k]))
   for l in range(4):r=add(r,mul(G[i][i][l],G[l][j][k]));r=sub(r,mul(G[i][k][l],G[l][j][i]))
  Ric[j][k]=r
sc=C(0)
for i in range(4):
 for j in range(4):sc=add(sc,mul(gi[i][j],Ric[i][j]))
Z=[[sub(Ric[i][j],scale(mul(sc,g[i][j]),sp.Rational(1,4)))for j in range(4)]for i in range(4)]
norm=C(0)
for i in range(4):
 for j in range(4):
  for k in range(4):
   for l in range(4):norm=add(norm,mul(mul(gi[i][k],gi[j][l]),mul(Z[i][j],Z[k][l])))
dens=scale(norm,c*d);ev={x:0,u:1,sp.diff(f,v,2):-mu*f/(B**2*v**2)};P2=S(dens[2].subs(ev));qnorm=S((2*A**4*u**4*f**2*(qr**2+qi**2)*c*d).subs({x:0,u:1}));ratio=S(P2/qnorm)
F,FP=sp.symbols('F FP',nonzero=True,real=True);rr=sp.expand(ratio.xreplace({f:F,sp.diff(f,v):FP}));cf=sp.diff(rr,FP,2)/2;c0=S(rr-cf*FP**2);integ=S(c0+cf*mu*F**2/(B**2*v**2));K1,K2=sp.symbols('K1 K2',real=True);integK=S(integ.subs({A**2:-K1,B**2:-K2}));gen=mu*(mu+2*(K1-K2))/4
out={'n':n,'q_at_i':str(sp.simplify(z.subs({x:0,u:1}))),'scalar1':str(S(sc[1].subs({x:0,u:1}))),'ratio_K':str(integK),'generator':str(gen),'difference':str(S(integK-gen)),'example':str(S(integK.subs({K1:-2,K2:-1,mu:1})))}
p=Path(__file__).resolve().parents[1]/'data'/f'step68_product_saddle_direct_n{n}.json';p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
