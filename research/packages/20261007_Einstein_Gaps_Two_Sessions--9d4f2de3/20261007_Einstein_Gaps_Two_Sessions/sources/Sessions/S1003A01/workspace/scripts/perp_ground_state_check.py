"""Symbolic and numerical check of the exact-CH transverse Sturm factorization.

For Q[v]=int_A^B (p v'^2+V v^2) dx, where
 p=x(1+x)/4 and V=(4-18x+3x^2)/(16x(1+x)), the positive function
 f=x/(1+x)^(5/2) solves -(p f')'+V f=0.  Hence

 Q[v] = int_A^B p f^2 ((v/f)')^2 dx + [p f'/f v^2]_A^B,
 p f'/f=(2-3x)/8.

The script also compares both sides for nonzero-endpoint polynomial tests.
"""
import sympy as s
x=s.symbols('x',positive=True)
p=x*(1+x)/4
V=(4-18*x+3*x**2)/(16*x*(1+x))
f=x/(1+x)**s.Rational(5,2)
L=s.factor(-s.diff(p*s.diff(f,x),x)+V*f)
beta=s.factor(p*s.diff(f,x)/f)
print('L[f] =',L)
print('p fprime/f =',beta)

# Pointwise divergence identity. With w=v/f:
# p v'^2+Vv^2-p f^2 w'^2 = d/dx(beta v^2).
v=s.Function('v')(x)
w=v/f
res=s.factor(p*s.diff(v,x)**2+V*v**2-p*f**2*s.diff(w,x)**2-s.diff(beta*v**2,x))
print('ground-state identity residual =',res)

# Verify the full transverse quadratic action from (4.8), including the first
# endpoint term produced when mixed derivatives are integrated by parts.
vp=s.Function('vp')(x); vm=s.Function('vm')(x)
xi=(vp+vm)/2; zeta=(vp-vm)/2; L2=x*(1+x)
raw=s.Rational(1,2)*(s.sqrt(L2)*s.diff(xi,x)+(xi+s.Rational(3,2)*x*zeta)/s.sqrt(L2))**2
raw+=s.Rational(1,2)*(s.sqrt(L2)*s.diff(zeta,x)+(zeta+s.Rational(3,2)*x*xi)/s.sqrt(L2))**2+3*xi*zeta
Vp=(4+18*x+15*x**2)/(16*x*(1+x))
bp=(2+3*x)/8; bm=(2-3*x)/8
sturm=p*s.diff(vp,x)**2+Vp*vp**2+p*s.diff(vm,x)**2+V*vm**2
full_res=s.factor(raw-sturm-s.diff(bp*vp**2+bm*vm**2,x))
print('full CH quadratic-to-Sturm residual =',full_res)

# Exact polynomial tests on rational intervals.
for A,B,poly in [(s.Rational(1,100),s.Rational(1,2),1+x+x**2),
                 (s.Rational(1,20),s.Rational(1),x*(1-x)+s.Rational(1,3))]:
    q=s.integrate(p*s.diff(poly,x)**2+V*poly**2,(x,A,B))
    bulk=s.integrate(p*f**2*s.diff(poly/f,x)**2,(x,A,B))
    bd=s.simplify((beta*poly**2).subs(x,B)-(beta*poly**2).subs(x,A))
    rr=s.simplify(q-bulk-bd)
    print('test',A,B,'symbolic residual =',rr,' numeric =',s.N(rr,30))

# Search power-product zero modes x^m(1+x)^n for both channels.
m,n=s.symbols('m n',real=True)
fpow=x**m*(1+x)**n
rho=s.symbols('rho',positive=True)
for name,Vc in [('plus',(4+18*x+15*x**2)/(16*x*(1+x))),('minus',V)]:
    num=s.Poly(s.together((-s.diff(p*s.diff(fpow,x),x)+Vc*fpow)/fpow).as_numer_denom()[0],x)
    sols=s.solve(num.all_coeffs(),(m,n),dict=True)
    print(name,'power zero modes:',sols)
    sol=sols[0]; ff=s.factor(fpow.subs(sol)); bb=s.factor(p*s.diff(ff,x)/ff)
    I=s.integrate(1/(p*ff**2),(x,rho,1))
    dtn=s.factor(1/(ff.subs(x,rho)**2*I)-bb.subs(x,rho))
    print(name,'f =',ff,' beta =',bb)
    print(name,'Dirichlet-to-Neumann coefficient at rho =',dtn)
    for rv in [s.Rational(1,100),s.Rational(1,20),s.Rational(1,10),s.Rational(1,5),s.Rational(1,2)]:
        print('  rho',rv,'coefficient',s.N(dtn.subs(rho,rv),16))

if any(s.simplify(z)!=0 for z in [L,res,full_res]):
    raise SystemExit('symbolic factorization failed')
