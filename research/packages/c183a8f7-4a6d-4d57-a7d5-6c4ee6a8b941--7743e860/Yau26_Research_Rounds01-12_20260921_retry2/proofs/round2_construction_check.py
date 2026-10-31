"""Full invariant product Jacobi sectors and two-parameter quadratic source.

No imports from prior checks. Exact symbolic identities only.
"""
import sympy as sp

x,y,A,B,At,Bt=sp.symbols('x y A B At Bt', real=True)
ft,ru=1-x*x,1-y*y

def dt(v):
    return sp.diff(v,x)*ft+sp.diff(v,A)*At+sp.diff(v,B)*Bt-sp.diff(v,At)*x*At-sp.diff(v,Bt)*x*Bt

def du(v):
    return sp.diff(v,y)*ru

def d(v,i):
    return dt(v) if i==0 else du(v) if i==2 else 0

g=sp.diag(1,1/ft,1,1/ru)
ginv=sp.diag(1,ft,1,ru)
Gamma={}
Gamma[0,1,1]=-x/ft
Gamma[1,0,1]=Gamma[1,1,0]=x
Gamma[2,3,3]=-y/ru
Gamma[3,2,3]=Gamma[3,3,2]=y

def gamma(i,j,k):
    return Gamma.get((i,j,k),0)

def div(h):
    return [sp.simplify(sum(ginv[i,i]*(d(h[i,j],i)-sum(gamma(k,i,i)*h[k,j]+gamma(k,i,j)*h[i,k] for k in range(4))) for i in range(4))) for j in range(4)]

def bianchi(h):
    trace=sp.trace(ginv*h)
    dh=div(h)
    return [sp.simplify(-dh[j]+d(trace,j)/2) for j in range(4)]

def einstein_operator(h):
    nabla=[sp.Matrix(4,4,lambda i,j: d(h[i,j],m)-sum(gamma(k,m,i)*h[k,j]+gamma(k,m,j)*h[i,k] for k in range(4))) for m in range(4)]
    rough=sp.Matrix(4,4,lambda i,j: -sum(ginv[m,m]*(d(nabla[m][i,j],m)-sum(gamma(k,m,m)*nabla[k][i,j]+gamma(k,m,i)*nabla[m][k,j]+gamma(k,m,j)*nabla[m][i,k] for k in range(4))) for m in range(4)))
    action=sp.zeros(4)
    for inds in ((0,1),(2,3)):
        block_trace=sum(ginv[i,i]*h[i,i] for i in inds)
        for i in inds:
            for j in inds:
                action[i,j]=h[i,j]-block_trace*g[i,j]
    return (rough-2*action).applyfunc(sp.simplify)

# Verify every component sector for an unrestricted jointly t,u-dependent F.
F=sp.Function('F')(x,y)
PF=dt(dt(F))+x*dt(F)+du(du(F))+y*du(F)
bases=[]
for inds,pot in (((0,1),ft),((2,3),ru)):
    tr=sp.zeros(4)
    tt=sp.zeros(4)
    off=sp.zeros(4)
    i,j=inds
    tr[i,i]=tt[i,i]=1
    tr[j,j]=1/pot
    tt[j,j]=-1/pot
    off[i,j]=off[j,i]=1/sp.sqrt(pot)
    bases.extend(((tr,2),(tt,2-4*pot),(off,2-4*pot)))
for i,si in ((0,1),(1,1/sp.sqrt(ft))):
    for j,sj in ((2,1),(3,1/sp.sqrt(ru))):
        mixed=sp.zeros(4)
        mixed[i,j]=mixed[j,i]=si*sj
        bases.append((mixed,2-ft-ru))
for index,(basis,V) in enumerate(bases):
    difference=einstein_operator(F*basis)-(-PF+V*F)*basis
    assert difference.applyfunc(sp.simplify)==sp.zeros(4), index

# Actual h_(a,b) family has fixed fibre area, not just its first variation.
# In the fibre background orthonormal frame, h_s=I+sH+s^2N+O(s^3).
H=ru*sp.Matrix([[A,B],[B,-A]])
N=sp.Matrix([[A*A*(ru*ru-ru/2)+B*B*ru*ru,-A*B*ru*ru],[-A*B*ru*ru,A*A*ru/2]])
assert sp.simplify(sp.trace(N)-sp.trace(H*H)/2)==0
# Horizontal harmonic coefficients: A''+tanh(t) A'=B''+tanh(t) B'=0.
Hprime=H.applyfunc(dt)
vertical=sp.simplify(-(N.applyfunc(dt).applyfunc(dt)+x*N.applyfunc(dt))/2+Hprime*Hprime/2)
D22=At*At*ru/2-(At*At+Bt*Bt)*ru*ru/2
expected_vertical=sp.Matrix([[D22,At*Bt*ru*ru],[At*Bt*ru*ru,-D22]])
assert (vertical-expected_vertical).applyfunc(sp.simplify)==sp.zeros(2)

# Mixed block independently from fibre shape divergence before expanding.
q,bvel=sp.symbols('q bvel', real=True)
Dfib=1/ru+q-1
mixed_coord=bvel*sp.sqrt(ru)/2*du(Dfib**2*ru**2)
# q=exp(-sA), b'=s B'; coefficient at s^2 converted from dx to orthonormal e^3.
s=sp.symbols('s',real=True)
mixed2=sp.diff(mixed_coord.subs({q:sp.exp(-s*A),bvel:s*Bt}),s,2).subs(s,0)/2*sp.sqrt(ru)
assert sp.simplify(mixed2-2*A*Bt*y*ru**2)==0

Don=sp.zeros(4)
Don[0,0]=-(At*At+Bt*Bt)*ru**2/2
Don[2,2],Don[3,3]=D22,-D22
Don[2,3]=Don[3,2]=At*Bt*ru**2
Don[0,3]=Don[3,0]=mixed2
scale=sp.diag(1,1/sp.sqrt(ft),1,1/sp.sqrt(ru))
Dcoord=scale*Don*scale
assert bianchi(Dcoord)==[0,0,0,0], bianchi(Dcoord)

# Both TT fibre polarizations with A,B harmonic in t are trace-free/divergence-free.
H4=sp.zeros(4)
H4[2:4,2:4]=H
assert bianchi(scale*H4*scale)==[0,0,0,0]
assert div(scale*H4*scale)==[0,0,0,0]

def sech_integral(n):
    return sp.sqrt(sp.pi)*sp.gamma(sp.Rational(n,2))/sp.gamma(sp.Rational(n+1,2))

ba,bb=sp.symbols('ba bb',real=True)
base_pair=sp.simplify(-(ba*ba+bb*bb)*sech_integral(3)**2/2)
fibre_length_pair=sp.simplify(sech_integral(1)*(ba*ba*(sech_integral(3)-sech_integral(5))-bb*bb*sech_integral(5)))
fibre_twist_pair=sp.simplify(2*ba*bb*sech_integral(1)*sech_integral(5))
assert sp.simplify(base_pair+sp.pi**2*(ba*ba+bb*bb)/8)==0
assert sp.simplify(fibre_length_pair-sp.pi**2*(ba*ba-3*bb*bb)/8)==0
assert sp.simplify(fibre_twist_pair-3*sp.pi**2*ba*bb/4)==0

# Exact factorization potentials for the normalized horizontal TT channel.
t=sp.symbols('t',real=True)
w=sp.Rational(3,2)*sp.tanh(t)
v=sp.Rational(1,2)*sp.tanh(t)
assert sp.simplify(w*w-sp.diff(w,t)-(sp.Rational(9,4)-sp.Rational(15,4)*sp.sech(t)**2))==0
assert sp.simplify(w*w+sp.diff(w,t)-(2+v*v-sp.diff(v,t)))==0
# Finite-energy scalar conjugation: -P becomes -d^2 + 1/4 + sech^2/4.
scalar_drift=sp.tanh(t)
scalar_potential=scalar_drift**2/4+sp.diff(scalar_drift,t)/2
assert sp.simplify(scalar_potential-(sp.Rational(1,4)+sp.sech(t)**2/4))==0

print('PASS: fixed-area second variation and all vertical second-order components')
print('PASS: all ten product Jacobi sectors, with arbitrary joint radial dependence')
print('PASS: independent mixed shape-divergence term and full quadratic Bianchi identity')
print('PASS: two TT fibre polarizations have zero trace and divergence')
print('Base length projection:',base_pair)
print('Fibre length projection:',fibre_length_pair)
print('Fibre twist projection:',fibre_twist_pair)
print('PASS: factorization giving the exact normalized-channel spectral gap 2')
print('PASS: finite-energy scalar conjugation lower bound 1/4')
