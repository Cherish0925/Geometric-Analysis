"""Exact algebra supporting the nonlinear invariant-model charge theorem."""
import sympy as s

# A genuine varying metric checks the v H normalization in mixed Ricci.
# Coordinates are (t,u,y,x), h=E dt^2+F du^2, H=diag(U,V), A^y=w du.
t=s.symbols('t',real=True)
E,F,U,V=[s.Function(name,positive=True)(t) for name in ('E','F','U','V')]
w=s.Function('w')(t)
g=s.Matrix([[E,0,0,0],[0,F+U*w*w,U*w,0],
            [0,U*w,U,0],[0,0,0,V]])
gi=s.Matrix([[1/E,0,0,0],[0,1/F,-w/F,0],
             [0,-w/F,1/U+w*w/F,0],[0,0,0,1/V]])
assert (g*gi-s.eye(4)).applyfunc(s.simplify)==s.zeros(4)

def d(value,i):
    return s.diff(value,t) if i==0 else s.S.Zero

Gamma={}
for k in range(4):
    for i in range(4):
        for j in range(4):
            Gamma[k,i,j]=s.simplify(sum(
                gi[k,ell]*(d(g[j,ell],i)+d(g[i,ell],j)-d(g[i,j],ell))/2
                for ell in range(4)))

def ric(i,j):
    return s.simplify(sum(d(Gamma[k,i,j],k)-d(Gamma[k,i,k],j)
        +sum(Gamma[k,k,ell]*Gamma[ell,i,j]
             -Gamma[k,j,ell]*Gamma[ell,i,k] for ell in range(4))
        for k in range(4)))

q=U*s.sqrt(U*V)*s.diff(w,t)/s.sqrt(E*F)
mixed=s.factor(ric(1,2)-w*ric(2,2))
claimed=-s.sqrt(F)/(2*s.sqrt(U*V)*s.sqrt(E))*s.diff(q,t)
assert s.simplify(mixed-claimed)==0
print('PASS: exact mixed Ricci = -(*dq)/(2v), with five arbitrary functions')

# The first-order transfer connection gives constant charges directly.
p,r,b1,B1=s.symbols('p r b1 B1',positive=True)
v0=1/(p*r)
H0=s.diag(1/p**2,1/r**2)
f1=s.Matrix([-b1*r*p**3,B1*p*r**3])
assert s.simplify(v0*H0*f1)==s.Matrix([-b1,B1])

# Exact reference density, including both determinant factors.
dt,du=s.symbols('dt du',positive=True)
h=s.diag(1/dt,1/du)
H=s.diag(dt/p**2,du/r**2)
density=s.sqrt(h.det())/s.sqrt(H.det())*H.inv()
expected=s.diag(p**3*r/(dt**2*du),p*r**3/(dt*du**2))
assert (density-expected).applyfunc(s.simplify)==s.zeros(2)
print('PASS: first Jacobi charge and exact two-block reference integral density')

primitive=(s.sech(t)*s.tanh(t)+s.atan(s.sinh(t)))/2
assert s.simplify(s.diff(primitive,t)-s.sech(t)**3)==0
print('PASS: global angular gauge primitive removing the two constant twists')

def sech_integral(k):
    return s.sqrt(s.pi)*s.gamma(s.Rational(k,2))/s.gamma(s.Rational(k+1,2))

a0,A0=s.symbols('a0 A0',real=True)
cc=s.pi**2/2
M11first=2*a0*sech_integral(5)*sech_integral(1)
M11first+=A0*sech_integral(3)**2
M22first=a0*sech_integral(3)**2+2*A0*sech_integral(1)*sech_integral(5)
assert s.simplify(M11first-cc*(3*a0+A0)/2)==0
assert s.simplify(M22first-cc*(a0+3*A0)/2)==0
v_tw=s.Matrix([-b1,B1])
D=s.diag((3*a0+A0)/2,(a0+3*A0)/2)
q_through_second=(s.eye(2)-D)*v_tw
energy_through_third=s.expand((cc*v_tw).dot(q_through_second))
assert s.simplify(energy_through_third-cc*(
    b1**2+B1**2-(3*a0+A0)*b1**2/2-(a0+3*A0)*B1**2/2))==0
print('PASS: integrated matrix derivative, quadratic charge and cubic boundary energy')

# Nontrivial integral basis change checks covector/vector transformation.
h11,h12,h22,qq1,qq2=s.symbols('h11 h12 h22 qq1 qq2',real=True)
mat=s.Matrix([[h11,h12],[h12,h22]])
qq=s.Matrix([qq1,qq2])
ss=mat*qq
P=s.Matrix([[2,1],[1,1]])
mat_new=P*mat*P.T
qq_new=P.T.inv()*qq
ss_new=P*ss
assert s.simplify(mat_new*qq_new-ss_new)==s.zeros(2,1)
assert s.simplify(qq_new.dot(ss_new)-qq.dot(ss))==0
print('PASS: nontrivial GL(2,Z) charge/scattering covariance and energy invariance')

# All four oriented edge terms sum to q dot S, including constant twists.
b0,B0=s.symbols('b0 B0',real=True)
edge_sum=s.pi*(-qq1*(b0+s.pi*b1/2)+qq1*(b0-s.pi*b1/2)
              +qq2*(B0+s.pi*B1/2)-qq2*(B0-s.pi*B1/2))/2
assert s.simplify(edge_sum-cc*(-qq1*b1+qq2*B1))==0
print('PASS: exact oriented boundary sum and cancellation of constant end shears')
