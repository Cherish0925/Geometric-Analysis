"""Fast exact signed-collar log-neck coefficient from truncated bivariate series."""
import sympy as s

t,e,x,k=s.symbols('t e x k', real=True); C=s.symbols('C1:4',real=True)
# Keep exact expressions in e, truncate to e^2 after each operation; use enough t order.
def E(q): return s.series(q,e,0,3).removeO()
S=t-k*t**3/s.Integer(6)+k**2*t**5/s.Integer(120)
Co=1-k*t**2/s.Integer(2)+k**2*t**4/s.Integer(24)
# sqrt(S^2+e*x)=S*(1+q/2-q^2/8)
q=e*x/S**2; R=E(S*(1+q/2-q**2/8))
a=[E(R*(1+e*x*C[0]+e**2*x**2*C[0]**2/2)),
   E(R*Co*(1+e*x*C[1]+e**2*x**2*C[1]**2/2)),
   E(S*(1+e*x*C[2]+e**2*x**2*C[2]**2/2))]
def inv(z):
 z0=z.subs(e,0);q=E((z-z0)/z0);return E((1-q+q*q)/z0)
def div(a,b):return E(a*inv(b))
def U(i):
 j=(i+1)%3;l=(i+2)%3
 return E(s.diff(a[i],t)-div(E(a[j]**2+a[l]**2-a[i]**2),E(a[j]*a[l])))
u=[U(i) for i in range(3)];ud=[E(s.diff(z,t)) for z in u]
H=[E(u[0]+u[1]*u[2]/2),E(u[1]+u[2]*u[0]/2),E(u[2]+u[0]*u[1]/2)]
la=[div(E(a[1]*a[2]),a[0]),div(E(a[2]*a[0]),a[1]),div(E(a[0]*a[1]),a[2])]
S1=E(la[0]/4*E(ud[0]+2*div(H[0],la[0]))**2)
S2=E(la[1]/4*E(ud[1]-div(E(2*u[1]-u[0]*u[2]),la[1]))**2)
S3=E(la[2]/4*E(ud[2]+2*div(H[2],la[2]))**2)
cub=E(2*u[0]*u[1]*u[2]*inv(la[1]))
Sig=0
for i in range(3):Sig=E(Sig+div(ud[i],a[i])+2*div(H[i],E(a[(i+1)%3]*a[(i+2)%3])))
scal=E(a[0]*a[1]*a[2]/4*E(Sig+12*k)**2)
def coef(z):
 z2=s.expand(z).coeff(e,2);ser=s.series(t*z2,t,0,2).removeO();return s.factor(s.expand(ser).coeff(t,0)/x**2)
parts=[coef(z) for z in (S1,S2,S3,cub,scal)]
print('parts');[print(s.factor(z)) for z in parts]
for name,f in [('P',s.expand(sum(parts[:4]))),('J',s.expand(sum(parts)))]:
 print(name,'=',s.factor(f))
 for kv in [-1,1]:
  fk=s.expand(f.subs(k,kv));sol=s.solve([s.diff(fk,q) for q in C],C,dict=True)[0]
  print(name,kv,sol,s.factor(fk.subs(sol)))
