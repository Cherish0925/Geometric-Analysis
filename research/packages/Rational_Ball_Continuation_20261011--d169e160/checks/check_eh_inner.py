import sympy as s
x,t,nu,mu=s.symbols('x t nu mu', positive=True)
G=1-x**-2
u1=(nu-mu)*x/6+(nu+mu)/(2*x)-(2*nu+mu)/(3*x*x)
v1=u1-nu*(x-1/x)
F=G+t*u1; H=G+t*v1
Dx=lambda a:s.diff(a,x)
k01=-Dx(H)
k12=(4-3*F-H)/x
k13=(F-H)/x-H*Dx(F)/F
k03=-H*(3*Dx(F)/F+2*x*Dx(Dx(F))/F-x*Dx(F)**2/F**2)-Dx(H)*(1+x*Dx(F)/F)
R=[2*k01+k03,k01+k12+k13,k01+k12+k13,k03+2*k13]
R1=[s.factor(s.diff(a,t).subs(t,0)) for a in R]
S1=s.factor(sum(R1)); E1=[s.factor(a-S1/4) for a in R1]
print('Ricci linear:',R1)
print('Scalar linear:',S1)
print('Einstein defect linear:',E1)
assert R1==[2*nu+mu+mu/x**2,2*nu+mu-mu/x**2,2*nu+mu-mu/x**2,2*nu+mu+mu/x**2] or all(s.simplify(a-b)==0 for a,b in zip(R1,[2*nu+mu+mu/x**2,2*nu+mu-mu/x**2,2*nu+mu-mu/x**2,2*nu+mu+mu/x**2]))
assert s.simplify(u1.subs(x,1))==0 and s.simplify(v1.subs(x,1))==0
assert s.simplify((Dx(u1)+Dx(v1)).subs(x,1))==0
print('Core Ricci coefficient / link volume:',s.integrate(sum(a*a for a in E1)*x/2,(x,1,s.oo)))
r=s.symbols('r', positive=True)
Gr=1-r**-4; A=s.sqrt(r**4-1)
rad=s.diff(r**3*Gr*s.diff(A,r),r)/r**3
angular=-(8+4*(1/Gr-1))*A/r**2
assert s.simplify(rad+angular)==0
av=Gr*s.diff(A,r)**2/3+8*A*A/(3*r*r)+4*(1/Gr-1)*A*A/(3*r*r)
av=s.factor(av)
flux=s.factor(r**3*Gr*s.diff(av,r)/2)
print('Mean gradient square:',av)
print('Hessian Bochner flux / link volume:',s.expand(flux))
assert s.limit(flux-4*r**4,r,s.oo)==-s.Rational(8,3)
print('All identities verified.')
