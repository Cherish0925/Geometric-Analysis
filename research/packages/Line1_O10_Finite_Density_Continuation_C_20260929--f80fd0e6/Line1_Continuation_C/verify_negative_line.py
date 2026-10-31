"""Exact finite algebra check. This does NOT certify the analytic estimates."""
import sympy as s
from itertools import combinations
from collections import defaultdict
I=s.I
pairs=list(combinations(range(4),2))
C=[s.eye(2),s.diag(I,-I),s.Matrix([[0,1],[-1,0]]),s.Matrix([[0,-I],[-I,0]])]
a=s.symbols('a1:5',real=True)
p=s.symbols('p1:5',real=True)
q=s.symbols('q1:5',real=True)
k,x,y=s.symbols('k x y',real=True)
c=x+I*y
eta=[k,-I*k,0,0]; b=[0,0,c,-I*c]
Gamma=[[[0]*4 for j in range(4)] for i in range(4)]
for l in range(4):
 Op=s.Matrix([[I*(p[l]-a[l]/2),-s.conjugate(eta[l])],[eta[l],-I*(p[l]-a[l]/2)]])
 Om=s.Matrix([[I*(q[l]-3*a[l]/2),-s.conjugate(b[l])],[b[l],-I*(q[l]-3*a[l]/2)]])
 for j in range(4):
  val=Om*C[j]-C[j]*Op
  for i in range(4): Gamma[i][j][l]=s.simplify(s.re(s.trace(C[i].H*val))/2)
  assert s.simplify(val-sum((Gamma[i][j][l]*C[i] for i in range(4)),s.zeros(2)))==s.zeros(2)
def wedge(u,v):return s.Matrix([s.expand(u[i]*v[j]-u[j]*v[i]) for i,j in pairs])
e=[s.eye(4)[:,i] for i in range(4)]
de=[s.simplify(-sum((wedge(s.Matrix(Gamma[i][j]),e[j]) for j in range(4)),s.zeros(6,1))) for i in range(4)]
theta=e[2]-I*e[3]
psi=wedge(e[0],e[2])+wedge(e[1],e[3])+I*(wedge(e[0],e[3])-wedge(e[1],e[2]))
expr=s.simplify(de[2]-I*de[3]-I*wedge(s.Matrix([2*a[i]-p[i]-q[i] for i in range(4)]),theta)+s.conjugate(c)*psi)
assert expr==s.zeros(6,1),expr
# ASD convention: psi has zero SD projection.
SD=lambda v:s.Matrix([v[0]+v[5],v[1]-v[4],v[2]+v[3]])
assert SD(psi)==s.zeros(3,1)
# derivative symbol for c: SD(alpha ^ theta)
al=s.symbols('u1:5'); aa=s.Matrix(al)
assert s.simplify(SD(wedge(aa,theta))-s.Matrix([-I*al[2]-al[3],al[0]+I*al[1],-I*al[0]+al[1]]))==s.zeros(3,1)
# second cubic, target determinant power: 3 -> 9, wedge original det1 -> line L5.
rho,m=s.symbols('rho m',positive=True)
z=s.Matrix([1,0]); tv=sum((-C[i].H*z*m**s.Rational(3,2)*b[i] for i in range(4)),s.zeros(2,1))
assert s.simplify(tv[1]+2*m**s.Rational(3,2)*c)==0
assert s.simplify(tv[0])==0
# constants
ms=s.Rational(128,81); rs=s.Rational(4,3)
assert ms/(4*rs**3)==s.Rational(1,6)
assert s.Rational(135,64)*ms==s.Rational(10,3)
print('PASS: Clifford/SO(4) compatibility; dtheta structure with both phase currents; ASD quadratic cancellation; CR symbol; L5 cubic normalization; positive 10/3 potential.')
# Weighted symbol pairing L^* diag(2,1,1) L = I-iJ on one-forms.
L=s.Matrix([[0,0,-I/s.sqrt(2),-1/s.sqrt(2)],
            [1/s.sqrt(2),I/s.sqrt(2),0,0],
            [-I/s.sqrt(2),1/s.sqrt(2),0,0]])
J=s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,1],[0,0,-1,0]])
assert s.simplify(L.H*s.diag(2,1,1)*L-(s.eye(4)-I*J))==s.zeros(4)
# Negative-spinor Clifford action and the sign of the line potential.
clminus=lambda p,q: -C[p]*C[q].H
Omminus=clminus(0,1)-clminus(2,3)
assert Omminus==s.diag(2*I,-2*I)
# q_-(sqrt(m)e1)=-i m Omega_-/4, so f=-(27/32)(-m Omega_-/4).
# The line L^5 has -i<F^{L5},Omega_->=5<f,Omega_->=135m/64.
assert s.simplify(5*s.Rational(27,128)*ms*2-s.Rational(10,3))==0
print('PASS: weighted self-dual symbol = I-iJ_-; negative Clifford sign; L5 curvature contraction = +10/3.')
