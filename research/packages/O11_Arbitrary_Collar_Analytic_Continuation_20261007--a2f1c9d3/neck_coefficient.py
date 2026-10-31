import sympy as sp
# First variation in epsilon, with exact hyperbolic functions.
t=sp.symbols('t',positive=True)
c1,c2,c3=sp.symbols('c1 c2 c3',real=True)
S=sp.sinh(t); C=sp.cosh(t)
a=[S,S*C,S]
f=[1/(2*S*S)+c1,1/(2*S*S)+c2,c3]
u0=[sp.S(0),3*S*S,sp.S(0)]
U=[]
for i in range(3):
 j,k=(i+1)%3,(i+2)%3
 ga=(a[j]**2+a[k]**2-a[i]**2)/(a[j]*a[k])
 dg=(2*a[j]**2*f[j]+2*a[k]**2*f[k]-2*a[i]**2*f[i])/(a[j]*a[k])-ga*(f[j]+f[k])
 ui=sp.simplify(sp.diff(a[i],t)*f[i]+a[i]*sp.diff(f[i],t)-dg)
 U.append(ui)
 print('U',i,ui)
lam=[a[1]*a[2]/a[0],a[2]*a[0]/a[1],a[0]*a[1]/a[2]]
H1=[U[0]+u0[1]*U[2]/2,U[1],U[2]+u0[1]*U[0]/2]
A=[sp.diff(U[0],t)+2*H1[0]/lam[0],
   sp.diff(U[1],t)-2*U[1]/lam[1]+2*u0[1]/lam[1]*(f[2]+f[0]-f[1]),
   sp.diff(U[2],t)+2*H1[2]/lam[2]]
# Only leading Laurent coefficients required: Ai = ai/t + O(t).
AL=[sp.simplify(sp.limit(t*z,t,0)) for z in A]
U1zero=sp.simplify(sp.limit(U[0],t,0))
U3pole=sp.simplify(sp.limit(t*t*U[2],t,0))
F_P=sp.factor(sum(z*z/4 for z in AL)+6*U1zero*U3pole)
Sig1=sp.S(0)
for i in range(3):
 j,k=(i+1)%3,(i+2)%3
 Sig1+=(sp.diff(U[i],t)-sp.diff(u0[i],t)*f[i])/a[i]+2*(H1[i]-u0[i]*(f[j]+f[k]))/(a[j]*a[k])
spole=sp.simplify(sp.limit(t*t*Sig1,t,0))
F_J=sp.factor(F_P+spole**2/4)
print('A coefficients',AL)
print('u1zero',U1zero,'u3pole',U3pole)
print('scalar pole',spole)
print('F_P',sp.expand(F_P))
print('F_J',sp.expand(F_J))
star={c1:sp.Rational(9,4),c2:sp.Rational(3,4),c3:sp.Rational(1,2)}
print('Pstar',F_P.subs(star),'Jstar',F_J.subs(star))
print('Psol',sp.solve([sp.diff(F_P,c) for c in (c1,c2,c3)],(c1,c2,c3),dict=True))
print('Jsol',sp.solve([sp.diff(F_J,c) for c in (c1,c2,c3)],(c1,c2,c3),dict=True))
