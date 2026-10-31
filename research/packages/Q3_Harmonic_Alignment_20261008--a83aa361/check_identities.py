"""Exact algebra for the harmonic-alignment variation; not a PDE proof."""
import sympy as s
from itertools import product
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def skew(v):
    A=s.zeros(4)
    for val,(i,j) in zip(v,pairs): A[i,j],A[j,i]=val,-val
    return A
root=s.sqrt(2)
Sp=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,1],[0,-1,0],[1,0,0]])/root
Sm=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,-1],[0,1,0],[-1,0,0]])/root
assert Sp.T*Sp==s.eye(3) and Sm.T*Sm==s.eye(3) and Sp.T*Sm==s.zeros(3)
# The composition map Lambda+ tensor Lambda- -> Sym^2_0 is isometric.
M=[skew(Sp[:,i])*skew(Sm[:,j]) for i,j in product(range(3),repeat=2)]
G=s.Matrix(9,9,lambda i,j:s.trace(M[i].T*M[j]))
assert G==s.eye(9)
p1,p2,p3,p4,p5,m1,m2,m3,m4,m5,sc,a,b=s.symbols('p1 p2 p3 p4 p5 m1 m2 m3 m4 m5 sc a b',real=True)
Wp=s.Matrix([[p1,p3,p4],[p3,p2,p5],[p4,p5,-p1-p2]])
Wm=s.Matrix([[m1,m3,m4],[m3,m2,m5],[m4,m5,-m1-m2]])
B=s.Matrix(3,3,s.symbols('b0:9'))
Rop=Sp*(Wp+sc*s.eye(3)/12)*Sp.T+Sm*(Wm+sc*s.eye(3)/12)*Sm.T+Sp*B.T*Sm.T+Sm*B*Sp.T

def getR(i,k,j,l):
    if i==k or j==l:return 0
    ik=tuple(sorted([i,k]));jl=tuple(sorted([j,l]))
    sign=(1 if i<k else -1)*(1 if j<l else -1)
    return sign*Rop[pairs.index(ik),pairs.index(jl)]
phi=root*a*Sp[:,0];psi=root*b*Sm[:,0]
Z=skew(phi)*skew(psi)
Znorm=s.trace(Z.T*Z)
assert s.expand(Znorm-4*a*a*b*b)==0
rz=sum(getR(i,k,j,l)*Z[i,j]*Z[k,l] for i,k,j,l in product(range(4),repeat=4))
f=2*a*a;h=2*b*b
expected=h*(Sp.T*phi).dot(Wp*(Sp.T*phi))+f*(Sm.T*psi).dot(Wm*(Sm.T*psi))-sc*f*h/12
assert s.simplify(rz-expected)==0
# Gradient convention checked on unequal-curvature surface products.
k1,k2,t=s.symbols('k1 k2 t',real=True)
x=(k1-k2)/2
P=((k1/(1+t*x)-k2/(1-t*x))**2)*(1+t*x)*(1-t*x)
assert s.simplify(s.diff(P,t).subs(t,0)+(k1+k2)*(k1-k2)**2)==0
print('Composition isometry: exact PASS')
print('Curvature contraction: exact PASS')
print('Product first variation DP[Z] = -s P / 2: exact PASS')
# Generic SD/ASD first jets check the gradient norm and cross term.
u=s.Matrix(s.symbols('u0:3'));v=s.Matrix(s.symbols('v0:3'))
du=s.Matrix(s.symbols('du0:3'));dv=s.Matrix(s.symbols('dv0:3'))
U=skew(Sp*u);V=skew(Sm*v);dU=skew(Sp*du);dV=skew(Sm*dv)
dZ=dU*V+U*dV
lhs=s.expand(s.trace(dZ.T*dZ))
rhs=(v.dot(v))*du.dot(du)+(u.dot(u))*dv.dot(dv)+2*u.dot(du)*v.dot(dv)
assert s.simplify(lhs-rhs)==0
print('First-jet product rule and amplitude cross term: exact PASS')
