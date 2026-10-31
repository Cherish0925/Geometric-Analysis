# Referee check of the orthogonally-transitive T^2 reduction identities used in lem:critical (sec5)
import sympy as sp
t,z,x,y=sp.symbols('t z x y',real=True)
co=[t,z,x,y]
phi=sp.Function('phi')(t,z); sig=sp.Function('sigma')(t,z); a=sp.Function('a')(t,z); b=sp.Function('b')(t,z)
# general unimodular M via upper-half-plane coordinates (a,b), b>0:  M = (1/b) [[1,a],[a,a^2+b^2]]
b=sp.exp(sp.Function('beta')(t,z))
M=sp.Matrix([[1,a],[a,a**2+b**2]])/b
assert sp.simplify(M.det())==1
g=sp.zeros(4); g[0,0]=g[1,1]=sp.exp(2*phi); G=sp.exp(sig)*M
g[2:,2:]=G
def ricci(g):
    gi=g.inv(); n=4
    Gam=[[[sum(gi[A,d]*(sp.diff(g[d,B],co[c])+sp.diff(g[d,c],co[B])-sp.diff(g[B,c],co[d])) for d in range(n))/2 for c in range(n)] for B in range(n)] for A in range(n)]
    Ric=sp.zeros(n)
    for B in range(n):
        for c in range(n):
            Ric[B,c]=sum(sp.diff(Gam[A][B][c],co[A]) for A in range(n))-sum(sp.diff(Gam[A][B][A],co[c]) for A in range(n))\
              +sum(Gam[A][A][d]*Gam[d][B][c] for A in range(n) for d in range(n))-sum(Gam[A][c][d]*Gam[d][B][A] for A in range(n) for d in range(n))
    return Ric
Ric=ricci(g)
# base geometry gamma=e^{2phi}(dt^2+dz^2)
gam=sp.eye(2)*sp.exp(2*phi); bc=[t,z]
KB=-sp.exp(-2*phi)*(sp.diff(phi,t,2)+sp.diff(phi,z,2))
gami=gam.inv()
Gam2=[[[sum(gami[A,d]*(sp.diff(gam[d,B],bc[c])+sp.diff(gam[d,c],bc[B])-sp.diff(gam[B,c],bc[d])) for d in range(2))/2 for c in range(2)] for B in range(2)] for A in range(2)]
hess=lambda f: sp.Matrix(2,2,lambda i,j: sp.diff(f,bc[i],bc[j])-sum(Gam2[k][i][j]*sp.diff(f,bc[k]) for k in range(2)))
lap=lambda f: sum(gami[i,j]*hess(f)[i,j] for i in range(2) for j in range(2))
ds=sp.Matrix([sp.diff(sig,t),sp.diff(sig,z)])
Mi=M.inv()
Uh=sp.Matrix(2,2,lambda i,j: sp.Rational(1,2)*(Mi*sp.diff(M,bc[i])*Mi*sp.diff(M,bc[j])).trace())
print("U^*h == (da^2+db^2)/b^2 :",sp.simplify(Uh-sp.Matrix(2,2,lambda i,j:(sp.diff(a,bc[i])*sp.diff(a,bc[j])+sp.diff(b,bc[i])*sp.diff(b,bc[j]))/b**2))==sp.zeros(2))
claim_base=KB*gam-hess(sig)-ds*ds.T/2-Uh/2
print("base block residual:",sp.simplify(Ric[:2,:2]-claim_base).tolist())
print("mixed block:",sp.simplify(Ric[:2,2:]).tolist())
trF=(G.inv()*Ric[2:,2:]).trace()
gradsq=(ds.T*gami*ds)[0]
print("fibre trace residual:",sp.simplify(trF+lap(sig)+gradsq))
# tension field: trace-free part of G^{-1}Ric_F = -(1/2) M^{-1} tau_sigma(M)
dM=[sp.diff(M,c) for c in bc]
lapM=sp.Matrix(2,2,lambda i,j: lap(M[i,j]))
tau=lapM-sum((gami[i,i]*dM[i]*Mi*dM[i] for i in range(2)),sp.zeros(2))+sum((gami[i,i]*ds[i]*dM[i] for i in range(2)),sp.zeros(2))
EF0=G.inv()*Ric[2:,2:]-sp.eye(2)*trF/2
print("trace-free fibre block + (1/2)M^{-1}tau_sigma(M):",sp.simplify(EF0+Mi*tau/2).tolist())
# mu=e^{sigma/2}
mu=sp.exp(sig/2)
print("Hess mu identity:",sp.simplify(hess(mu)-mu/2*hess(sig)-mu/4*ds*ds.T)==sp.zeros(2))
