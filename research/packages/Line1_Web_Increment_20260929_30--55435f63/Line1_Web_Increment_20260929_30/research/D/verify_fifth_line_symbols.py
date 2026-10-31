#!/usr/bin/env python3
"""Exact finite algebra for O10 Fifth Line attachment. Values are dyadic Gaussians.
No PDE, cutoff convergence, or analytical hypotheses are verified by this file.
"""
from itertools import product
I=1j
C=[[[1,0],[0,1]],[[I,0],[0,-I]],[[0,1],[-1,0]],[[0,-I],[-I,0]]]
def star(A):return [[complex(A[j][i]).conjugate() for j in range(len(A))] for i in range(len(A[0]))]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sub(A,B):return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def tr(A):return sum(A[i][i] for i in range(len(A)))
def scale(a,x):return [a*t for t in x]
def plus(x,y):return [a+b for a,b in zip(x,y)]
pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
e=[[int(i==j) for i in range(4)] for j in range(4)]
def wedge(u,v):return [u[i]*v[j]-u[j]*v[i] for i,j in pairs]
theta=plus(e[2],scale(-I,e[3]))
Xi=plus(plus(wedge(e[0],e[2]),wedge(e[1],e[3])),scale(I,plus(wedge(e[0],e[3]),scale(-1,wedge(e[1],e[2])))))
theta1=plus(e[0],scale(-I,e[1]))
Xi_plus=plus(plus(wedge(e[0],e[2]),scale(-1,wedge(e[1],e[3]))),scale(I,plus(wedge(e[0],e[3]),wedge(e[1],e[2]))))
# The Cartan identity is linear in 15 real connection components.
for index in range(15):
 a=[int(index==h) for h in range(4)]
 p=[int(index==4+h) for h in range(4)]
 q=[int(index==8+h) for h in range(4)]
 k=int(index==12); c=int(index==13)+I*int(index==14)
 eta=[k,-I*k,0,0];b=[0,0,c,-I*c]
 G={}
 for i,j in product(range(4),repeat=2):
  G[i,j]=[]
  for h in range(4):
   Op=[[I*(p[h]-a[h]/2),-complex(eta[h]).conjugate()],[eta[h],I*(a[h]/2-p[h])]]
   Om=[[I*(q[h]-3*a[h]/2),-complex(b[h]).conjugate()],[b[h],I*(3*a[h]/2-q[h])]]
   G[i,j].append(tr(mul(star(C[i]),sub(mul(Om,C[j]),mul(C[j],Op)))).real/2)
 de=[]
 for i in range(4):
  value=[0]*6
  for j in range(4):value=plus(value,scale(-1,wedge(G[i,j],e[j])))
  de.append(value)
 actual=plus(de[2],scale(-I,de[3]))
 expected=plus(scale(I,wedge([2*a[h]-p[h]-q[h] for h in range(4)],theta)),scale(-c.conjugate(),Xi))
 assert actual==expected,(index,actual,expected)
 actual1=plus(de[0],scale(-I,de[1]))
 expected1=plus(scale(-I,wedge([a[h]+p[h]-q[h] for h in range(4)],theta1)),scale(k,Xi_plus))
 assert actual1==expected1,(index,actual1,expected1)
print('PASS: both Cartan identities on all 15 real basis directions; c cancels from dtheta1')
# SD target basis has squared norm 2, so the adjoint includes a factor 2.
L=[[0,0,-I/2,-1/2],[1/2,I/2,0,0],[-I/2,1/2,0,0]]
D=[[2,0,0],[0,1,0],[0,0,1]]
J=[[0,-1,0,0],[1,0,0,0],[0,0,0,1],[0,0,-1,0]]
M=mul(mul(star(L),D),L)
expected=[[int(i==j)-I*J[i][j] for j in range(4)] for i in range(4)]
assert [[2*t for t in row] for row in M]==expected
print('PASS: L* D L = I - i J with the correct target metric')
# Hodge star with orientation e1234: star(12)=34, star(13)=-24, star(14)=23.
def hodge(x):return [x[5],-x[4],x[3],x[2],-x[1],x[0]]
assert hodge(Xi)==scale(-1,Xi)
print('PASS: Xi is anti-self-dual')
# Cubic spinor coefficients for v=(1,0), multiplying b_i.
coeff=[]
for Ci in C:
 coeff.append([-star(Ci)[0][0],-star(Ci)[1][0]])
assert coeff==[[-1,0],[I,0],[0,-1],[0,-I]]
print('PASS: t(v)=m^(3/2)(-b1+i b2,-b3-i b4)')
from fractions import Fraction as F
m=F(128,81)
assert 5*F(27,32)*4/m*(m*m/8)==F(10,3)
print('PASS: fifth-line curvature contraction is +10/3')
print('LIMIT: this script certifies finite algebra only, not weak CR test convergence.')
# Radial mass retained: u=dm/(2m), q=-J_plus u, b=d theta1+c theta2.
# Nv=Dv=0 forces d=-(u3+i u4). This term must NOT be discarded.
radial_cases=[]
for index in range(11):
 radial_cases.append(([int(index==h) for h in range(4)],
                      [int(index==4+h) for h in range(4)],
                      int(index==8), int(index==9)+I*int(index==10)))
# Also evaluate the bilinear kappa*u curvature cancellation with kappa=1.
for h in range(4):radial_cases.append(([0]*4,e[h],1,0))
for a,u,k,c in radial_cases:
 p=[0]*4; q=[u[1],-u[0],u[3],-u[2]]; d=-u[2]-I*u[3]
 eta=scale(k,theta1); b=plus(scale(d,theta1),scale(c,theta))
 G={}
 for i,j in product(range(4),repeat=2):
  G[i,j]=[]
  for h in range(4):
   Op=[[I*(-a[h]/2),-complex(eta[h]).conjugate()],[eta[h],I*a[h]/2]]
   Om=[[I*(q[h]-3*a[h]/2),-complex(b[h]).conjugate()],[b[h],I*(3*a[h]/2-q[h])]]
   G[i,j].append(tr(mul(star(C[i]),sub(mul(Om,C[j]),mul(C[j],Op)))).real/2)
 de=[]
 for i in range(4):
  value=[0]*6
  for j in range(4):value=plus(value,scale(-1,wedge(G[i,j],e[j])))
  de.append(value)
 actual1=plus(de[0],scale(-I,de[1]));actual2=plus(de[2],scale(-I,de[3]))
 expected1=plus(plus(scale(-I,wedge([a[h]-q[h] for h in range(4)],theta1)),scale(k,Xi_plus)),scale(-d,wedge(theta1,theta)))
 expected2=plus(plus(scale(I,wedge([2*a[h]-q[h] for h in range(4)],theta)),scale(-complex(c).conjugate(),Xi)),scale(-2*I*complex(d).conjugate(),wedge(e[0],e[1])))
 assert actual1==expected1
 assert actual2==expected2
 # rho constant gives d(kappa)=kappa*u; p=0.
 Fplus21=plus(plus(scale(k,wedge(u,theta1)),scale(k,actual1)),scale(I*k,wedge(a,theta1)))
 assert Fplus21==scale(k*k,Xi_plus),(a,u,k,c,Fplus21)
print('PASS: radial Cartan terms and exact positive-curvature cancellation with dm retained')
