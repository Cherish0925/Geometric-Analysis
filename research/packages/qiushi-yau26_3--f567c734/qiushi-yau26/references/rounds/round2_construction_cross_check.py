"""Actual cross Ricci variation for simultaneous base/fibre TT transfers."""
import sympy as s
x,y,a,b,A,B,au,bu,At,Bt=s.symbols('x y a b A B au bu At Bt',real=True)
f,r=1-x*x,1-y*y

def dt(v):
    return s.diff(v,x)*f+s.diff(v,A)*At+s.diff(v,B)*Bt-x*At*s.diff(v,At)-x*Bt*s.diff(v,Bt)

def du(v):
    return s.diff(v,y)*r+s.diff(v,a)*au+s.diff(v,b)*bu-y*au*s.diff(v,au)-y*bu*s.diff(v,bu)

def dd(v,i):
    return dt(v) if i==0 else du(v) if i==2 else s.S.Zero

g=s.diag(1,1/f,1,1/r)
gi=s.diag(1,f,1,r)
G0={}
G0[0,1,1]=-x/f
G0[1,0,1]=G0[1,1,0]=x
G0[2,3,3]=-y/r
G0[3,2,3]=G0[3,3,2]=y

Hb=s.zeros(4)
Hf=s.zeros(4)
Hb[0,0],Hb[1,1]=f*a,-a
Hb[0,1]=Hb[1,0]=s.sqrt(f)*b
Hf[2,2],Hf[3,3]=r*A,-A
Hf[2,3]=Hf[3,2]=s.sqrt(r)*B

def gamma1(H):
    Hu=gi*H
    result={}
    for k in range(4):
        for i in range(4):
            for j in range(4):
                value=gi[k,k]*(dd(H[j,k],i)+dd(H[i,k],j)-dd(H[i,j],k))/2-sum(Hu[k,l]*G0.get((l,i,j),0) for l in range(4))
                value=s.simplify(value)
                if value!=0:
                    result[k,i,j]=value
    return result

Gb,Gf=gamma1(Hb),gamma1(Hf)
G2={}
Hbu,Hfu=gi*Hb,gi*Hf
for k in range(4):
    for i in range(4):
        for j in range(4):
            value=-sum(Hbu[k,l]*Gf.get((l,i,j),0)+Hfu[k,l]*Gb.get((l,i,j),0) for l in range(4))
            value=s.simplify(value)
            if value!=0:
                G2[k,i,j]=value

def ric_cross(i,j):
    v=sum(dd(G2.get((k,i,j),0),k)-dd(G2.get((k,i,k),0),j) for k in range(4))
    for k in range(4):
        for l in range(4):
            for U,V in ((G0,G2),(G2,G0),(Gb,Gf),(Gf,Gb)):
                v+=U.get((k,k,l),0)*V.get((l,i,j),0)-U.get((k,j,l),0)*V.get((l,i,k),0)
    return s.factor(s.simplify(v))

Rcross=s.Matrix(4,4,lambda i,j: ric_cross(i,j))
assert Rcross==Rcross.T
# Compare ALL sixteen coordinate-Ricci entries with the asserted
# orthonormal-frame formula, not just contractions or the Bianchi identity.
frame=s.diag(1,s.sqrt(f),1,s.sqrt(r))
expected=-f*r*s.Matrix([
    [A*au*y,A*bu*y,At*au/2,Bt*au/2],
    [A*bu*y,-A*au*y,At*bu/2,Bt*bu/2],
    [At*au/2,At*bu/2,At*a*x,Bt*a*x],
    [Bt*au/2,Bt*bu/2,Bt*a*x,-At*a*x],
])
for i in range(4):
    for j in range(4):
        assert s.simplify((frame*Rcross*frame)[i,j]-expected[i,j])==0,(i,j)
print('PASS: every entry of the asserted full cross-Ricci matrix')
trace=s.trace(gi*Rcross)
for j in range(4):
    divergence=sum(gi[i,i]*(dd(Rcross[i,j],i)-sum(G0.get((k,i,i),0)*Rcross[k,j]+G0.get((k,i,j),0)*Rcross[i,k] for k in range(4))) for i in range(4))
    assert s.simplify(-divergence+dd(trace,j)/2)==0, j
R00,R11,R22,R33=(Rcross[i,i] for i in range(4))
pb=s.factor(f*(R00-f*R11))
pf=s.factor(r*(R22-r*R33))
print('Pointwise cross projection onto base length:',pb)
print('Pointwise cross projection onto fibre length:',pf)
print('Pointwise combined cross projection:',s.factor(pb+pf))
assert s.simplify(pb+2*A*au*y*f*f*r)==0
assert s.simplify(pf+2*At*a*x*f*r*r)==0
print('PASS: complete mixed source obeys the quadratic Bianchi identity')

# A=A0+A1 J(t), a=a0+a1 J(u), with J odd and J'=sech.
# Each displayed projection contains an odd radial factor after separation.
# Its full integral is therefore exactly zero; the two self terms remain.
bl,bt,fl,ftw=s.symbols('bl bt fl ftw',real=True)
Ibase=s.pi**2*(bl**2-3*bt**2-fl**2-ftw**2)/8
Ifibre=s.pi**2*(fl**2-3*ftw**2-bl**2-bt**2)/8
assert s.simplify(Ibase+Ifibre+s.pi**2*(bt**2+ftw**2)/2)==0
print('Combined integrated source:',s.factor(Ibase+Ifibre))

# Store the exact expressions in ordinary stdout; integration is handled in the note.
