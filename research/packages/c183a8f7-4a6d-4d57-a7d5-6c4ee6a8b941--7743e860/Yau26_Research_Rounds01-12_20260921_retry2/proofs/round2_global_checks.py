"""Exact full-Ricci, charge, and threshold checks for round2_global.md."""
import sympy as s

r,m=s.symbols("r m",positive=True)
c=s.symbols("c",real=True)
V=r*r-m/r
D=r*r+c*c*V

def ricci_radial_metric(g):
    """All coordinate components; coefficients depend only on coordinate 0=r."""
    n=4
    gi=s.simplify(g.inv())
    def der(expr,i):
        return s.diff(expr,r) if i==0 else s.S.Zero
    Gamma=[[[s.S.Zero for j in range(n)] for i in range(n)] for k in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                Gamma[k][i][j]=s.factor(sum(gi[k,l]*(der(g[l,j],i)+der(g[l,i],j)-der(g[i,j],l)) for l in range(n))/2)
    Ric=s.zeros(n)
    for i in range(n):
        for j in range(n):
            terms=sum(der(Gamma[k][i][j],k)-der(Gamma[k][i][k],j) for k in range(n))
            terms+=sum(Gamma[k][i][j]*Gamma[l][k][l]-Gamma[l][i][k]*Gamma[k][j][l] for k in range(n) for l in range(n))
            Ric[i,j]=s.factor(terms)
    return Ric

original=s.diag(1/V,V,r*r,r*r)
ric_original=ricci_radial_metric(original)
assert all(s.simplify(z)==0 for z in ric_original+3*original)
print("PASS: all 16 Ricci components of the original soliton.")
sheared=s.Matrix([[1/V,0,0,0],[0,V,c*V,0],[0,c*V,D,0],[0,0,0,r*r]])
ric_sheared=ricci_radial_metric(sheared)
assert all(s.simplify(z)==0 for z in ric_sheared+3*sheared)
print("PASS: all 16 Ricci components after the integral torus shear.")
As=c*V/D
assert s.simplify(s.diff(As,r)-3*c*m/D**2)==0
# rho=r sqrt(D), sqrt(det gamma)=r/sqrt(D); q=rho*G11*f.
charge=s.factor(D**2*s.diff(As,r))
assert charge==3*c*m
twist=s.factor(D**2*s.diff(As,r)**2/(2*r*r))
assert s.simplify(twist-9*c*c*m*m/(2*r*r*D*D))==0
a=s.symbols("a",positive=True)
assert s.simplify(twist.subs(m,a**3).subs(r,a)-s.Rational(9,2)*c*c)==0
z=s.symbols("z",positive=True)
series=s.series(As.subs(r,1/z),z,0,6).removeO()
assert s.simplify(series-(c/(1+c*c)-c*m*z**3/(1+c*c)**2))==0
print("PASS: constant q=(3cm,0), twist energy, bolt value, cubic AH coefficient.")
eps=s.symbols("eps",nonnegative=True)
K=3+eps
L0=12-8*eps
f=s.symbols("f",nonnegative=True)
B=(2*f/s.sqrt(K)+s.sqrt(2*K+5*f*f/K))**2
y=s.sqrt(B)
# Use the explicit nonnegative root rather than simplifying sqrt(square).
y=2*f/s.sqrt(K)+s.sqrt(2*K+5*f*f/K)
assert s.simplify(y*y-4*f*y/s.sqrt(K)-2*K-f*f/K)==0
fcrit=s.sqrt(K)*(s.sqrt(5*L0-2*K)-2*s.sqrt(L0))
assert s.expand(fcrit**2+4*s.sqrt(K*L0)*fcrit+K*(2*K-L0)).simplify()==0
qcrit=fcrit-2*eps
assert s.simplify(qcrit.subs(eps,0)-(9*s.sqrt(2)-12))==0
ot=(4*eps/s.sqrt(K)+s.sqrt(2*K+20*eps*eps/K))**2
assert s.simplify(B.subs(f,2*eps)-ot)==0
print("PASS: charged threshold inversion and exact recovery of OT expression.")
print("liminf Q_* threshold:",s.N(qcrit.subs(eps,0),15))
for ee in [s.S.Zero,s.Rational(1,20),s.Rational(1,10),s.Rational(1,5)]:
    print("epsilon=",ee,"necessary Q_* >=",s.N(qcrit.subs(eps,ee),12))
rr,RR=s.symbols("rr RR",real=True)
assert s.simplify(s.integrate(s.exp(3*rr),(rr,0,RR))-(s.exp(3*RR)-1)/3)==0
print("PASS: weighted transport integral on an expanding model.")
