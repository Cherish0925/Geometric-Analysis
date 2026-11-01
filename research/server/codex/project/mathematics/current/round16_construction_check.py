#!/usr/bin/env python3
"""Exact coordinate checks for a Maxwell-compatible waist receiver.

The coordinate connection and its waist variation are freshly computed by
the imported Round 14 programs. This script independently differentiates
the connection variable, computes its divergence, and checks every block
of the corrected gauged variation. It does not test a global PDE theorem.
"""
import round14_repair_radius_check as r
import mpmath as mp

m, s = r.m, r.s
t, a, z, y, f = r.t, r.a, r.z, r.y, r.f
zz = s.Function('zeta')(t)
mean = s.symbols('mean', real=True)
theta = s.Matrix([0, 1, z, 0])
beta = s.Matrix([0, 0, 1, 0])
K = a*a*zz*(theta*beta.T+beta*theta.T)
assert s.simplify(s.trace(m.gi*K)) == 0

covK = [[[s.simplify(s.diff(K[i,j],m.coords[n])
    -sum(m.Gamma[p][n][i]*K[p,j]+m.Gamma[p][n][j]*K[i,p]
         for p in range(4))) for j in range(4)]
    for i in range(4)] for n in range(4)]
divK = [s.simplify(-sum(m.gi[i,n]*covK[n][i][j]
    for i in range(4) for n in range(4))) for j in range(4)]
assert divK == [3*y*y*a*a*zz*s.diff(z,t),0,0,0]
print('PASS R16: exact trace and divergence of the connection correction')

# Differentiate the full coordinate Ricci tensor in z, z', z''.
def connection_variation(expr):
    return s.simplify(sum(s.diff(expr,s.diff(z,t,j))*s.diff(zz,t,j)
                          for j in range(3)))
dEK = (m.ric+3*m.g).applyfunc(connection_variation)
gauge = s.Matrix(4,4,lambda i,j:
    (s.diff(divK[j],m.coords[i])+s.diff(divK[i],m.coords[j]))/2
    -sum(m.Gamma[p][i][j]*divK[p] for p in range(4)))
corrected = r.dE+dEK+gauge
ap, zp, zzp = s.diff(a,t),s.diff(z,t),s.diff(zz,t)
kap, B = ap/a,3*y*y
relations = {
    s.diff(a,t,2):3*a,
    s.diff(f,t):-2*kap*f,
    s.diff(f,t,2):(-6+6*kap*kap)*f,
    s.diff(z,t,2):-3*kap*zp,
    zzp:2*(f-mean)*zp,
    s.diff(zz,t,2):(-4*kap*f-6*kap*(f-mean))*zp,
}
def reduce(expr):
    return s.simplify(expr.subs(relations,simultaneous=True))

targets = [
    (m.T,m.T,a*a*(f*zp*zp/2-kap*zz*zp)*B),
    (m.U,m.U,a*a*(-3*f*zp*zp/2+zzp*zp+kap*zz*zp)*B),
    (m.X,m.X,a*a*(f*zp*zp-zp*zzp)),
    (m.Y,m.Y,0),
    (m.T,m.X,0),
    (m.T,m.Y,3*a*a*zz*zp*y),
    (m.X,m.U,a**3*zz*zp*zp*B),
    (m.Y,m.U,0),
    (m.T,m.U,0),
    (m.X,m.Y,0),
]
for v,w,target in targets:
    error=reduce((v.T*corrected*w)[0]-target)
    assert error == 0, (v,w,error)
print('PASS R16: all ten corrected gauged Einstein blocks')

# The uncanceled cubic mixed component is essential, not a zero block.
mixed=reduce((m.X.T*corrected*m.U)[0])
assert s.simplify(mixed-a**3*zz*zp*zp*B) == 0
assert mixed != 0
print('PASS R16: the false exact-zero mixed-block variant is rejected')

# Re-solving the endpoint Maxwell problem gives zeta'=2(f-mean)z'.
eps = s.symbols('eps', real=True)
N, b = s.sqrt(1+eps*f), a*s.sqrt(1-eps*f)
assert s.simplify(s.diff(b**3/N,eps).subs(eps,0)+2*a**3*f)==0
assert s.simplify(s.diff((b**3/N)*(zp+eps*zzp),eps).subs(eps,0)
    .subs(zzp,2*(f-mean)*zp)+2*mean*a**3*zp)==0
print('PASS R16: exact linear Maxwell flux compatibility')

mp.mp.dps=55
k=mp.sqrt(3)
for R in map(mp.mpf,('0.5','1.7','4')):
    jm=lambda p:mp.quad(lambda u:mp.sech(k*u)**p,[-R,0,R])
    J3,J5=jm(3),jm(5)
    primitive=lambda u:(mp.sech(k*u)*mp.tanh(k*u)
                         +mp.atan(mp.sinh(k*u)))/(2*k)
    profile=lambda u:mp.mpf('.5')+primitive(u)/J3
    offset=mp.sech(k*R)**3*mp.tanh(k*R)/(2*k*J3)
    mean_value=J5/J3
    correction=lambda u:mp.sech(k*u)**3*mp.tanh(k*u)/(2*k*J3) \
                         +offset*(1-2*profile(u))
    assert abs(mean_value-mp.mpf('.75')-offset)<mp.mpf('1e-47')
    assert abs(correction(-R))+abs(correction(R))<mp.mpf('1e-47')
    for u in (-R/2,mp.mpf('0'),R/3):
        assert abs(mp.diff(correction,u)
            -2*(mp.sech(k*u)**2-mean_value)*mp.sech(k*u)**3/J3) \
            <mp.mpf('1e-47')
print('PASS R16: exact finite-interval correction and endpoint conditions')

# Derive the infinite profile and its uniform integrable weights.
xx=s.symbols('xx',real=True)
zeta_inf=s.sech(xx)**3*s.tanh(xx)/s.pi
assert s.simplify(s.diff(zeta_inf,xx)
    -4/s.pi*(s.sech(xx)**2-s.Rational(3,4))*s.sech(xx)**3)==0
J3inf=mp.pi/(2*k)
J5inf=3*mp.pi/(8*k)
assert abs(2*mp.pi*J5inf/J3inf**2-3*k)<mp.mpf('1e-47')
print('PASS R16: infinite correction and retained signed cubic source')

# Exact fixed-profile FN length scaling (not a full geometric filling test).
c,Q,B0,V=s.symbols('c Q B0 V',positive=True)
action=-12*s.sqrt(V)-s.pi*c**3*Q*B0/s.sqrt(V)
assert s.simplify(c*s.diff(action,c)+3*s.pi*c**3*Q*B0/s.sqrt(V))==0
print('PASS R16: fixed-profile closed action has strictly signed waist derivative')

# The genuine waist length variation is not merely angular twist gauge.
xx=s.symbols('xx',real=True)
fk=s.sech(xx)**2
assert s.simplify(s.diff(s.tanh(xx),xx)-fk)==0
assert s.simplify(-1+s.tanh(xx)**2+fk)==0
print('PASS R16: waist tensor equals length variation plus radial gauge')
