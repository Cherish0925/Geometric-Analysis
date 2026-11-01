"""Symbolic verification of the projected Taub--NUT charge-five formula.

The computation uses the same canonical Kahler-spinor realization as
step90_tn_sigma_projection.py, but keeps r, theta and ell symbolic (setting
phi=0 only after differentiating). Axial equivariance then restores the
factor exp(-i phi). Output is a compact JSON certificate.
"""
import sympy as sp, json, os
r,t,p,u,L=sp.symbols('r t p u L', positive=True, real=True)
X=[r,t,p,u]
V=1+L/r
eta=[0,0,L*sp.cos(t),1]
gb=sp.diag(1,r**2,r**2*sp.sin(t)**2,0)
g=sp.Matrix(4,4,lambda i,j: sp.simplify(V*gb[i,j]+eta[i]*eta[j]/V))
gi=sp.simplify(g.inv())
Gam=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(4))/2)
       for c in range(4)] for b in range(4)] for a in range(4)]
x1=r*sp.sin(t)*sp.cos(p); x2=r*sp.sin(t)*sp.sin(p); x3=r*sp.cos(t)
fb=x1-sp.I*x2
df=sp.Matrix([sp.diff(fb,x) for x in X])
H=sp.Matrix(4,4,lambda b,c: sp.simplify(sp.diff(df[c],X[b])-sum(Gam[a][b][c]*df[a] for a in range(4))))
# Cartesian horizontal orthonormal frame, then specialize phi=0.
Jac=sp.Matrix([x1,x2,x3]).jacobian(sp.Matrix([r,t,p])); Ji=sp.simplify(Jac.inv())
subs0={p:0}
Ji0=sp.simplify(Ji.subs(subs0)); H0=sp.simplify(H.subs(subs0)); df0=sp.simplify(df.subs(subs0)); fb0=sp.simplify(fb.subs(subs0))
frames=[]
for k in range(3):
    q=sp.Matrix([Ji0[0,k],Ji0[1,k],Ji0[2,k],0])
    q[3]=sp.simplify(-L*sp.cos(t)*q[2])
    frames.append(sp.simplify(q/sp.sqrt(V)))
frames.append(sp.Matrix([0,0,0,sp.sqrt(V)]))
# Exterior algebra matrices [1,e1,e2,e12].
def wedge(a):
    M=sp.zeros(4)
    if a==0: M[1,0]=1; M[3,2]=1
    else: M[2,0]=1; M[3,1]=-1
    return M
def contr(a):
    M=sp.zeros(4)
    if a==0: M[0,1]=1; M[2,3]=1
    else: M[0,2]=1; M[1,3]=-1
    return M
W1,W2=wedge(0),wedge(1); C1,C2=contr(0),contr(1)
cl=[W1-C1,sp.I*(W1+C1),W2-C2,sp.I*(W2+C2)]
even=[0,3]; odd=[1,2]
Gmp=[M.extract(even,odd) for M in cl]
def det2(x,y): return sp.expand(x[0]*y[1]-x[1]*y[0])
def cov01(vals): return sp.Matrix([(vals[0]+sp.I*vals[1])/sp.sqrt(2),(vals[2]+sp.I*vals[3])/sp.sqrt(2)])
rho=sp.Rational(4,3); aa=sp.sqrt(2)/3; m=sp.Rational(128,81); Cv=sp.sqrt(m/2)
dvals=sp.Matrix([sp.simplify((df0.T*E)[0]) for E in frames])
v=sp.simplify(Cv*cov01(dvals))
Q=[]
for Ei in frames:
    vals=sp.Matrix([sp.simplify((Ei.T*H0*Ej)[0]) for Ej in frames])
    Q.append(sp.simplify(Cv*cov01(vals)))
tv=sp.zeros(2,1)
for i in range(4):
    tv += Gmp[i]*v*det2(v,Q[i])
tv=sp.simplify(tv)
phi=sp.Matrix([sp.sqrt(rho),aa*fb0])
sigma=sp.factor(det2(phi,tv))
expected=sp.Rational(2048,2187)*sp.sqrt(6)*L*fb0/(r+L)**3
residual=sp.simplify(sp.trigsimp(sigma-expected))
ratio=sp.simplify(sp.trigsimp(sigma/expected))
out={'phi_specialization':'phi=0 after tensor differentiation','sigma_phi0':str(sigma),'expected_phi0':str(expected),'ratio':str(ratio),'residual':str(residual),'axial_completion':'multiply the phi=0 expression by exp(-I phi), equivalently replace r sin(theta) by fbar'}
print(json.dumps(out,indent=1))
here=os.path.dirname(os.path.abspath(__file__)); od=os.path.join(here,'..','data','step90'); os.makedirs(od,exist_ok=True); json.dump(out,open(os.path.join(od,'tn_sigma_symbolic.json'),'w'),indent=1)
assert residual==0
