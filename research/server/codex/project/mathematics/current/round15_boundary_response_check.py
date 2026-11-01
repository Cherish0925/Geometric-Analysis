#!/usr/bin/env python3
"""Independent Sturm--Liouville, boundary, and gauge calculations.

These tests do not substitute an arbitrary Robin matrix for an actual
Einstein exterior. Numerical integration checks explicit constants only.
"""
import sympy as s
import mpmath as mp

t,k,c,A,B = s.symbols('t k c A B', positive=True)
a=c*s.cosh(k*t)
kap=k*s.tanh(k*t)
f=s.sech(k*t)**2
p=a*f*f
St=(s.sinh(k*t)+s.sinh(k*t)**3/3)/(k*c)
lw=lambda v: -(s.diff(v,t,2)+kap*s.diff(v,t))/2+(2*kap**2-k*k)*v
ls=lambda v: -(s.diff(v,t,2)+kap*s.diff(v,t))/2
clean=lambda expr:s.simplify(s.trigsimp(expr.rewrite(s.exp)))
assert clean(s.diff(St,t)-1/p)==0
assert clean(lw(f))==0
assert clean(lw(f*St))==0
assert clean(s.diff(f*(A+B*St),t)+2*kap*f*(A+B*St)-B/(a*f))==0
print('PASS: radial fundamental system and exact Bianchi current')

u=s.Function('u')(t)
assert clean(lw(f*u)+s.diff(p*s.diff(u,t),t)/(2*a*f))==0
v=s.Function('v')(t)
qcur=s.diff(v,t)+2*kap*v
# For a twist vO, Bianchi dual vector is -qcur/a*d_phi.
# Its symmetrized gradient has coefficient a/2*(-qcur/a)'.
assert clean(lw(v)-a*s.diff(-qcur/a,t)/2)==0
print('PASS: ground-state transform and twist pure-gauge identity')

ar,fr,kr,Lam,ym,yp=s.symbols('ar fr kr Lam ym yp', positive=True)
boundary_mean=(ym+yp)/(2*fr)
boundary_slope=(yp-ym)/(fr*Lam)
# v'=f'u+f B/p, with f'(-R)=+2kr fr, f'(+R)=-2kr fr.
vmprime=2*kr*ym+boundary_slope/(ar*fr)
vpprime=-2*kr*yp+boundary_slope/(ar*fr)
flux=s.Matrix([-ar*vmprime/2,ar*vpprime/2])
J=s.Matrix([[1,-1],[-1,1]])
Dw=-ar*kr*s.eye(2)+J/(2*Lam*fr**2)
assert s.simplify(flux-Dw*s.Matrix([ym,yp]))==s.zeros(2,1)
energy=(s.Matrix([ym,yp]).T*Dw*s.Matrix([ym,yp]))[0]
assert s.simplify(energy+ar*kr*(ym*ym+yp*yp)-(yp-ym)**2/(2*Lam*fr**2))==0
print('PASS: both radial DtN blocks and exact boundary quadratic form')

mp.mp.dps=60
kk=mp.sqrt(3)
def data(cc,RR):
    aa=lambda q:cc*mp.cosh(kk*q)
    ff=lambda q:mp.sech(kk*q)**2
    jj=lambda n:mp.quad(lambda q:mp.sech(kk*q)**n,[-RR,0,RR])
    j1,j3,j5=(jj(n) for n in (1,3,5))
    zz=lambda q:mp.mpf('.5')+(mp.sech(kk*q)*mp.tanh(kk*q)
                    +mp.atan(mp.sinh(kk*q)))/(2*kk*j3)
    zp=lambda q:mp.sech(kk*q)**3/j3
    SS=lambda q:(mp.sinh(kk*q)+mp.sinh(kk*q)**3/3)/(kk*cc)
    LL=2*SS(RR)
    return aa,ff,j1,j3,j5,zz,zp,SS,LL

for RR in map(mp.mpf,('0.5','1.4','3.1')):
    cc=mp.mpf('.17')
    aa,ff,j1,j3,j5,zz,zp,SS,LL=data(cc,RR)
    yyminus,yyplus=mp.mpf('.23'),mp.mpf('-.31')
    AA=(yyminus+yyplus)/(2*ff(RR))
    BB=(yyplus-yyminus)/(ff(RR)*LL)
    vv=lambda q:ff(q)*(AA+BB*SS(q))
    assert abs(vv(-RR)-yyminus)<mp.mpf('1e-50')
    assert abs(vv(RR)-yyplus)<mp.mpf('1e-50')
    angle=mp.quad(lambda q:vv(q)/aa(q),[-RR,0,RR])
    assert abs(angle-AA*j3/cc)<mp.mpf('1e-50')
    # Fiber Dirichlet response and its exact outward source traction.
    fiberprime=lambda q:cc**3*(mp.mpf('.5')-zz(q))/(j3*aa(q))
    left=-aa(-RR)*fiberprime(-RR)/2
    right=aa(RR)*fiberprime(RR)/2
    assert abs(left+cc**3/(4*j3))<mp.mpf('1e-50')
    assert abs(right-left)<mp.mpf('1e-50')
    # Radial source (rho=1): its transformed current is -2 integral_0^t a f F.
    Gamma=cc**3*j5/(2*j3*j3)
    weighted_source=lambda q:aa(q)*ff(q)*aa(q)**2*zp(q)**2/2
    assert abs(mp.quad(weighted_source,[-RR,0,RR])-Gamma)<mp.mpf('1e-50')
    currentplus=-2*mp.quad(weighted_source,[0,RR])
    assert abs(currentplus+Gamma)<mp.mpf('1e-50')
    assert abs(currentplus/(2*ff(RR))+Gamma/(2*ff(RR)))<mp.mpf('1e-50')
print('PASS: finite endpoint data, marked twist angle, and both source tractions')

# Full-width response: fix a(R)=A0=1 exactly.
A0=mp.mpf(1)
limits=[]
for cc in map(mp.mpf,('0.05','0.01','0.002')):
    RR=mp.acosh(A0/cc)/kk
    aa,ff,j1,j3,j5,zz,zp,SS,LL=data(cc,RR)
    Gamma=cc**3*j5/(2*j3*j3)
    weighted_source=lambda q:aa(q)*ff(q)*aa(q)**2*zp(q)**2/2
    center=Gamma*LL/2-2*mp.quad(lambda q:SS(q)*weighted_source(q),[0,RR])
    limits.append(cc*center)
    odd=-A0*kk*mp.tanh(kk*RR)+1/(LL*ff(RR)**2)
    if cc==mp.mpf('.002'):
        assert abs(cc*center-A0**3/(4*mp.pi))<mp.mpf('2e-6')
        assert abs(odd-kk*A0/2)<mp.mpf('2e-5')
assert abs(limits[-1]-A0**3/(4*mp.pi)) < abs(limits[0]-A0**3/(4*mp.pi))
print('PASS: full-width waist amplification c*v_D(0) -> A0^3/(4*pi)')

# Explicit boundary Schur algebra, including source feedback.
d,ss,rr=s.symbols('d ss rr', positive=True)
Ds=d*J
ycommon=s.Matrix([rr/ss,rr/ss])
assert s.simplify((Ds+ss*s.eye(2))*ycommon-s.Matrix([rr,rr]))==s.zeros(2,1)
assert (s.Matrix([[1,1]])*Ds)==s.zeros(1,2)
assert (s.Matrix([[1,1]])*s.Matrix([rr,rr]))[0]==2*rr
print('PASS: zero product traction fails; nonzero exterior response can balance algebraically')

# Scalar Robin exterior: combine boundary and zero-Dirichlet interior terms.
rho,AA,kkk,ss=s.symbols('rho AA kkk ss', positive=True)
leading= rho*AA**3/(4*s.pi) + 3*kkk*rho*AA**4/(8*s.pi*(ss-kkk*AA))
assert s.simplify(leading-rho*AA**3*(2*ss+kkk*AA)/(8*s.pi*(ss-kkk*AA)))==0
assert s.simplify(leading.subs(ss,-kkk*AA/2))==0
print('PASS: Robin model cancels the leading waist amplification only at s=-k*A0/2')
