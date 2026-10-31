"""Independent checks from eigenvalue equations and tensor first jets.

This does not import rigidity_check.py or its multiplier matrix.
"""
import sympy as s

l1, l2, l3, X, Y, Z, scalar = s.symbols("l1 l2 l3 X Y Z scalar", real=True)
ls = (l1, l2, l3)
gs = (-X + Z, X - Y, Y - Z)
p, q, r = l1-l2, l2-l3, l3-l1
dl = (2*X**2/p-2*Z**2/r, -2*X**2/p+2*Y**2/q, 2*Z**2/r-2*Y**2/q)
tracefree = {l3: -l1-l2}

dx = 2*sum(g*g for g in gs)+2*sum(v*d for v,d in zip(ls,dl))
dx_expected = 8*(X*X+Y*Y+Z*Z)-4*(X*Y+X*Z+Y*Z)
assert s.simplify(dx-dx_expected) == 0
dy = sum(ls[(i+1)%3]*ls[(i+2)%3]*dl[i] for i in range(3))
dy += 2*(l3*gs[0]*gs[1]+l2*gs[0]*gs[2]+l1*gs[1]*gs[2])
dy_expected = -4*l3*X*X-4*l1*Y*Y-4*l2*Z*Z-4*l2*X*Y-4*l1*X*Z-4*l3*Y*Z
assert s.simplify((dy-dy_expected).subs(tracefree)) == 0
x = sum(v*v for v in ls)
y = s.prod(ls)
reaction_eigen = tuple(scalar*v/2-6*v*v+2*x for v in ls)
rx = 2*sum(v*d for v,d in zip(ls,reaction_eigen))
ry = sum(ls[(i+1)%3]*ls[(i+2)%3]*reaction_eigen[i] for i in range(3))
assert s.simplify((rx-(scalar*x-36*y)).subs(tracefree)) == 0
assert s.simplify((ry-(3*scalar*y/2-x*x)).subs(tracefree)) == 0

center = {l1:-s.Rational(1,6), l2:s.Rational(1,12), l3:s.Rational(1,12)}
a0=1+48*(x-s.Rational(1,24))
gradx=2*sum(v*g for v,g in zip(ls,gs))
quadratic=s.expand(a0*dx_expected+36*dy_expected+48*gradx**2)
M=s.hessian(quadratic,(X,Y,Z))/2
M0=M.subs(center)
assert M0 == s.Matrix([[8,-8,-2],[-8,32,-8],[-2,-8,8]])
assert [((M0-s.eye(3))[:j,:j]).det() for j in (1,2,3)] == [7,153,243]
reaction=s.expand(a0*rx+36*ry)
assert reaction.subs(center).subs(scalar,-4)==s.Rational(1,16)

# Construct the negative-double-eigenvalue harmonic-Weyl first jet directly.
def twoform(*pairs):
    om=s.zeros(4)
    for i,j in pairs:
        om[i,j]=1
        om[j,i]=-1
    return om

omegas=(twoform((0,1),(2,3)),twoform((0,2),(3,1)),twoform((0,3),(1,2)))
xx=s.Matrix([1,0,0,0])
zz=-xx
# Choose the connection signs by the four-index divergence convention below.
# Simultaneously reversing the contraction-defined X,Y,Z changes none of the
# invariant quadratic identities or norm values used in the argument.
aa=-omegas[2]*xx/(-s.Rational(1,4))
cc=-omegas[1]*zz/s.Rational(1,4)
A=s.diag(-s.Rational(1,6),s.Rational(1,12),s.Rational(1,12))
H=[]
for m in range(4):
    hm=s.diag(-2*xx[m],xx[m],xx[m])
    hm[0,1]=hm[1,0]=-aa[m]/4
    hm[0,2]=hm[2,0]=cc[m]/4
    H.append(hm)

# The four-index derivative is 1/2 sum H_ab omega_a tensor omega_b.
for j in range(4):
    for k in range(4):
        for ell in range(4):
            divergence=sum(H[m][a,b]*omegas[a][m,j]*omegas[b][k,ell]/2
                           for m in range(4) for a in range(3) for b in range(3))
            assert s.simplify(divergence)==0, (j,k,ell,divergence)
u0=s.sqrt(s.trace(A*A))
du=[s.trace(A*hm)/u0 for hm in H]
norm_DA=sum(s.trace(hm*hm) for hm in H)
norm_du=sum(v*v for v in du)
orbit_norm=sum(s.trace((hm-d/u0*A)**2) for hm,d in zip(H,du))
assert (norm_DA,norm_du,orbit_norm)==(10,6,4)

# z=det A/|A|^3 has zero Hessian on each of these radial-plus-orbit tangents.
t=s.symbols("t",real=True)
for hm in H:
    At=A+t*hm
    zt=At.det()/s.trace(At*At)**s.Rational(3,2)
    assert s.simplify(s.diff(zt,t).subs(t,0))==0
    assert s.simplify(s.diff(zt,t,2).subs(t,0))==0

# Nonzero self-dual Cotton principal symbol for xi=e_1, q=diag(0,1,-1,0).
qq=s.diag(0,1,-1,0)
C=s.MutableDenseNDimArray.zeros(4,4,4)
Cp=s.MutableDenseNDimArray.zeros(4,4,4)
for i in range(4):
    for j in range(4):
        for k in range(4):
            C[i,j,k]=int(k==0)*qq[i,j]-int(j==0)*qq[i,k]
for i in range(4):
    for j in range(4):
        for k in range(4):
            star=sum(s.LeviCivita(j,k,a,b)*C[i,a,b]/2 for a in range(4) for b in range(4))
            Cp[i,j,k]=(C[i,j,k]+star)/2
cotton_norm=sum(C[i,j,k]**2 for i in range(4) for j in range(4) for k in range(4))
cotton_plus_norm=sum(Cp[i,j,k]**2 for i in range(4) for j in range(4) for k in range(4))
assert (cotton_norm,cotton_plus_norm)==(4,2)

print("PASS: independent eigenvalue-to-invariant equations and multiplier matrix")
print("PASS: divergence-free tensor first jet; (|DA|^2,|du|^2,orbit norm^2) =",norm_DA,norm_du,orbit_norm)
print("PASS: normalized determinant Hessian vanishes on the radial-plus-orbit jet")
print("PASS: Cotton principal symbol squared norms =",cotton_norm,cotton_plus_norm)
