"""Test sign dependence of the perpendicular log-neck coefficient.

Use signed complex-space-form outer axes in proper time:
  a1 = S_k(t), a2 = S_k(t) C_k(t), a3 = S_k(t),
where S_k=t-k t^3/6+..., C_k=1-k t^2/2+..., so k=-1 is CH
(S=sinh,C=cosh) and k=+1 is the positive complex-space-form formal collar.
Insert the same perpendicular Burns tail sqrt(S_k^2+eps*x0) in a1,a2 and
constant order-x0 mixed modes C_i. Extract the t^0 coefficient per d log t.
"""
import sympy as sp

t,x0,eps,k=sp.symbols('t x0 eps k', real=True)
C1,C2,C3=sp.symbols('C1 C2 C3', real=True)
# Terms through the order needed for the t^0 coefficient.
S=t-k*t**3/sp.Integer(6)+k**2*t**5/sp.Integer(120)
Co=1-k*t**2/sp.Integer(2)+k**2*t**4/sp.Integer(24)
X=eps*x0
a=[sp.sqrt(S**2+X)*sp.exp(X*C1),sp.sqrt(S**2+X)*Co*sp.exp(X*C2),S*sp.exp(X*C3)]

def ui(i):
 j=(i+1)%3;q=(i+2)%3
 return sp.diff(a[i],t)-(a[j]**2+a[q]**2-a[i]**2)/(a[j]*a[q])
u=[ui(i) for i in range(3)];ud=[sp.diff(q,t) for q in u]
H=[u[0]+u[1]*u[2]/2,u[1]+u[2]*u[0]/2,u[2]+u[0]*u[1]/2]
la=[a[1]*a[2]/a[0],a[2]*a[0]/a[1],a[0]*a[1]/a[2]]
S1=la[0]/4*(ud[0]+2*H[0]/la[0])**2
S2=la[1]/4*(ud[1]-(2*u[1]-u[0]*u[2])/la[1])**2
S3=la[2]/4*(ud[2]+2*H[2]/la[2])**2
cub=2*u[0]*u[1]*u[2]/la[1]
Sig=sum(ud[i]/a[i]+2*H[i]/(a[(i+1)%3]*a[(i+2)%3]) for i in range(3))
# Scalar target is signed Einstein scalar s0=24k in this convention (CH k=-1 -> -24).
scal=a[0]*a[1]*a[2]/4*(Sig+12*k)**2

def coeff(ex):
 q=sp.diff(t*ex,eps,2).subs(eps,0)/2
 return sp.factor(sp.expand(sp.series(q,t,0,2).removeO()).coeff(t,0)/x0**2)
parts=[coeff(q) for q in (S1,S2,S3,cub,scal)]
fP=sp.expand(sum(parts[:4]));fJ=sp.expand(fP+parts[4])
print('parts',*[sp.factor(q) for q in parts],sep='\n')
for name,f in [('P',fP),('J',fJ)]:
 sol=sp.solve([sp.diff(f,q) for q in (C1,C2,C3)],(C1,C2,C3),dict=True)
 print(name,'form=',sp.factor(f))
 for so in sol: print(name,'opt=',so,'value=',sp.factor(f.subs(so)))
 for kv in (-1,1):
  fk=sp.expand(f.subs(k,kv));sk=sp.solve([sp.diff(fk,q) for q in (C1,C2,C3)],(C1,C2,C3),dict=True)[0]
  print(name,'k=',kv,'opt=',sk,'value=',sp.factor(fk.subs(sk)))
