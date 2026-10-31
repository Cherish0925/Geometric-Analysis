"""Independent tensor/form check of the Gibbons--Hawking O10 tangent.

Conventions
-----------
g = V (dr^2+r^2 dtheta^2+r^2 sin(theta)^2 dphi^2)
    + V^{-1}(dpsi+ell cos(theta)dphi)^2,
V=1+ell/r, psi-period 4*pi*ell.  The hyperkahler orientation is the one
for which Omega_i = eta wedge dx_i + V dx_j wedge dx_k are self-dual.
The complex structure I_3 makes f=x_1+i x_2 holomorphic.  We check the
metric Ricci tensor, the quaternionic complex structure, the (0,1)-form
v=sqrt(m0/2)d(conj f), its type equation, co-closedness and norm.  We
also check dOmega_i=0.  Ricci-flatness plus a parallel self-dual triple
implies W^+=0 and that both matrix entries of the S^- spin-connection
curvature are anti-self-dual.

The last block verifies the general k-centre scalar/energy identities
symbolically from Delta_R3 V=0; no spherical symmetry is used there.
"""
import json
import os
import sympy as sp

r, th, ph, ps, ell, m0 = sp.symbols('r theta phi psi ell m0', positive=True, real=True)
coords = (r, th, ph, ps)
n = 4
V = 1 + ell/r
eta = sp.Matrix([0, 0, ell*sp.cos(th), 1])
# coordinate metric
g = sp.diag(V, V*r**2, V*r**2*sp.sin(th)**2, 0)
g += (eta*eta.T)/V
ginv = sp.simplify(g.inv())

Gamma = [[[
    sp.simplify(sum(ginv[a,d]*(sp.diff(g[d,c],coords[b]) + sp.diff(g[d,b],coords[c])
                              - sp.diff(g[b,c],coords[d])) for d in range(n))/2)
    for c in range(n)] for b in range(n)] for a in range(n)]
Ric = sp.zeros(n)
for a in range(n):
    for b in range(n):
        Ric[a,b] = sp.simplify(sum(
            sp.diff(Gamma[c][a][b],coords[c]) - sp.diff(Gamma[c][a][c],coords[b])
            + sum(Gamma[c][c][d]*Gamma[d][a][b] - Gamma[c][b][d]*Gamma[d][a][c]
                  for d in range(n)) for c in range(n)))

# Exterior-form helpers: dict sorted-index-tuple -> coefficient.
def wedge(A,B):
    C={}
    for I,a in A.items():
        for J,b in B.items():
            if set(I)&set(J):
                continue
            inv=sum(i>j for i in I for j in J)
            K=tuple(sorted(I+J))
            C[K]=sp.simplify(C.get(K,0)+(-1)**inv*a*b)
    return {K:sp.simplify(v) for K,v in C.items() if sp.simplify(v)!=0}

def dform(A):
    C={}
    for I,a in A.items():
        for q,x in enumerate(coords):
            da=sp.diff(a,x)
            if da==0 or q in I:
                continue
            inv=sum(q>i for i in I)
            K=tuple(sorted((q,)+I))
            C[K]=sp.simplify(C.get(K,0)+(-1)**inv*da)
    return {K:sp.simplify(v) for K,v in C.items() if sp.simplify(v)!=0}

def one(v):
    return {(i,):sp.simplify(v[i]) for i in range(n) if v[i]!=0}

# Cartesian differentials on R^3 in spherical coordinates.
x1 = r*sp.sin(th)*sp.cos(ph)
x2 = r*sp.sin(th)*sp.sin(ph)
x3 = r*sp.cos(th)
dx=[]
for x in (x1,x2,x3):
    dx.append(one(sp.Matrix([sp.diff(x,q) for q in coords])))
eta_form=one(eta)
# Cyclic convention.  The sign is fixed by d eta = *_3 dV for A=ell cos(theta)dphi.
# With the Euclidean orientation dx1 dx2 dx3, this gives Omega_i=eta^dx_i-V dx_j^dx_k.
Omegas=[]
for i,(j,k) in enumerate(((1,2),(2,0),(0,1))):
    Om=wedge(eta_form,dx[i])
    base=wedge(dx[j],dx[k])
    for K,val in base.items():
        Om[K]=sp.simplify(Om.get(K,0)-V*val)
    Omegas.append(Om)
closed=[dform(Om) for Om in Omegas]

# Matrix of Omega_3 and the induced J, Omega(X,Y)=g(JX,Y).
def form_matrix(A):
    M=sp.zeros(n)
    for (i,j),v in A.items():
        M[i,j]=v; M[j,i]=-v
    return M
Om3=form_matrix(Omegas[2])
# J^c_a = g^{cb} Omega_{ab} = -(g^{-1}Omega)^c_a
J=sp.simplify(-ginv*Om3)
J2=sp.simplify(J*J)

# v = sqrt(m0/2) d(conjugate f), f=x1+i*x2.
I=sp.I
fbar=x1-I*x2
v=sp.Matrix([sp.sqrt(m0/2)*sp.diff(fbar,q) for q in coords])
T=sp.MutableDenseMatrix(n,n,[0]*(n*n)) # T[a,b]=nabla_a v_b
for a in range(n):
    for b in range(n):
        T[a,b]=sp.simplify(sp.diff(v[b],coords[a])-sum(Gamma[c][a][b]*v[c] for c in range(n)))
# For the chosen orientation f is anti-holomorphic and d(conj f) has type
# (1,0).  The inherited equation is the vanishing of the (0,1) derivative:
# P^{0,1}=(Id+iJ)/2 on the derivative vector index.
P01=sp.simplify((sp.eye(n)+I*J)/2)
type_tensor=sp.simplify(P01.T*T)  # (P01)^a_c T[a,b]
trace=sp.simplify(sum(ginv[a,b]*T[a,b] for a in range(n) for b in range(n)))
vnorm=sp.simplify(sum(ginv[a,b]*sp.conjugate(v[a])*v[b] for a in range(n) for b in range(n)))
# closedness of v
dv=sp.MutableDenseMatrix(n,n,[0]*(n*n))
for a in range(n):
    for b in range(n):
        dv[a,b]=sp.simplify(sp.diff(v[b],coords[a])-sp.diff(v[a],coords[b]))

# Full curvature and Hodge-star check for both spin-connection blocks.
# R^a_{ b i j}; lower the first index.  We do not infer the anti-self-duality
# equation merely from Ricci-flatness: compute *R_{ab}= -R_{ab} on form indices.
Riem={}
for a in range(n):
    for b in range(n):
        for i in range(n):
            for j in range(n):
                Rup=sp.diff(Gamma[a][j][b],coords[i])-sp.diff(Gamma[a][i][b],coords[j])
                Rup+=sum(Gamma[a][i][c]*Gamma[c][j][b]-Gamma[a][j][c]*Gamma[c][i][b] for c in range(n))
                Riem[(a,b,i,j)]=sp.simplify(sum(g[a,d]*Rup.subs({}, {}) if d==a else 0 for d in range(n)))
# Correct lowering without recomputing connection curvature.
for a in range(n):
    for b in range(n):
        for i in range(n):
            for j in range(n):
                Riem[(a,b,i,j)]=sp.simplify(sum(g[a,d]*(
                    sp.diff(Gamma[d][j][b],coords[i])-sp.diff(Gamma[d][i][b],coords[j])
                    +sum(Gamma[d][i][c]*Gamma[c][j][b]-Gamma[d][j][c]*Gamma[c][i][b] for c in range(n))) for d in range(n)))
# Levi-Civita epsilon with hyperkahler orientation (r,theta,phi,psi).
eps=sp.LeviCivita
curv_asd_bad=[]
curv_sd_bad=[]
for a in range(n):
    for b in range(a+1,n):
        for i in range(n):
            for j in range(i+1,n):
                star=sp.simplify(sum(sqrtg*eps(i,j,k,l)*ginv[k,p]*ginv[l,q]*Riem[(a,b,p,q)]
                                     for k in range(n) for l in range(n) for p in range(n) for q in range(n))/2)
                rasd=cs(star+Riem[(a,b,i,j)])
                rsd=cs(star-Riem[(a,b,i,j)])
                if rasd!=0: curv_asd_bad.append((a,b,i,j,str(rasd)))
                if rsd!=0: curv_sd_bad.append((a,b,i,j,str(rsd)))

# Scalar amplitude/energies.
m=sp.simplify(vnorm)
dm=sp.Matrix([sp.diff(m,q) for q in coords])
dm2=sp.simplify(sum(ginv[a,b]*dm[a]*dm[b] for a in range(n) for b in range(n)))
# usual (div grad) scalar Laplacian
detg=sp.simplify(g.det())
sqrtg=sp.sqrt(detg)
lapm=sp.simplify(sum(sp.diff(sqrtg*sum(ginv[a,b]*dm[b] for b in range(n)),coords[a])
                         for a in range(n))/sqrtg)
gradv2=sp.simplify(lapm/2) # since v is rough harmonic and usual Delta |v|^2=2|nabla v|^2
Ev_radial=sp.simplify(16*sp.pi**2*ell*sp.integrate(V*r**2*gradv2,(r,0,sp.oo)))
Em_radial=sp.simplify(16*sp.pi**2*ell*sp.integrate(V*r**2*dm2,(r,0,sp.oo)))

# General multi-centre calculus: write p=|grad V|^2 and impose Delta V=0.
Vs,p=sp.symbols('V p', positive=True, real=True)
# chain rule: Delta F(V)=F''(V)|grad V|^2 when Delta V=0
F1=1/Vs
F2=1/Vs**2
delta_inv=sp.simplify(sp.diff(F1,Vs,2)*p)
delta_inv2=sp.simplify(sp.diff(F2,Vs,2)*p)

def cs(z):
    return sp.simplify(sp.trigsimp(z.rewrite(sp.exp)))

checks={
    'Ricci_nonzero': [(i,j,str(sp.simplify(Ric[i,j]))) for i in range(n) for j in range(n) if sp.simplify(Ric[i,j])!=0],
    'dOmega_nonzero': [[(str(K),str(val)) for K,val in C.items()] for C in closed],
    'J2_plus_I_nonzero': [(i,j,str(cs(J2[i,j]+sp.eye(n)[i,j]))) for i in range(n) for j in range(n) if cs(J2[i,j]+sp.eye(n)[i,j])!=0],
    'Jstar_v_minus_i_v_nonzero': [(i,str(cs((J.T*v-I*v)[i]))) for i in range(n) if cs((J.T*v-I*v)[i])!=0],
    'type_projection_nonzero': [(i,j,str(cs(type_tensor[i,j]))) for i in range(n) for j in range(n) if cs(type_tensor[i,j])!=0],
    'codifferential_trace': str(cs(trace)),
    'dv_nonzero': [(i,j,str(sp.simplify(dv[i,j]))) for i in range(n) for j in range(n) if sp.simplify(dv[i,j])!=0],
    'curvature_ASD_residual_nonzero': curv_asd_bad,
    'curvature_SD_residual_count': len(curv_sd_bad),
    'vnorm': str(vnorm),
    'amplitude': str(m),
    'laplacian_amplitude_usual': str(lapm),
    'grad_v_sq': str(gradv2),
    'dm_sq': str(dm2),
    'Ev': str(Ev_radial),
    'Em': str(Em_radial),
    'multicentre_Delta_1_over_V': str(delta_inv),
    'multicentre_Delta_1_over_V2': str(delta_inv2),
}

here=os.path.dirname(os.path.abspath(__file__))
out=os.path.join(here,'..','data','gh_tangent_symbolic.json')
if __name__ == '__main__':
    with open(out,'w') as fh:
        json.dump(checks,fh,indent=2)
    print(json.dumps(checks,indent=2))
