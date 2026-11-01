"""Exact verification of the explicit Bianchi-VIII almost-Kahler Einstein pair.

Conventions:
  d sigma_1 = -2 sigma_2^sigma_3,
  d sigma_2 =  2 sigma_3^sigma_1,
  d sigma_3 =  2 sigma_1^sigma_2,
  g = G dp^2 + sum A_i sigma_i^2,  1/3 < p < 1.
Let e0=sqrt(G)dp, ei=sqrt(A_i)sigma_i and
  omega_i=e0^ei+e_j^e_k.
The form is Omega=sqrt(X1) omega_1+sqrt(X2) omega_2.

The script checks over Q(p), up to explicitly displayed positive square roots:
  * the class-A Einstein equations and Hamiltonian constraint (lambda=-3),
  * dOmega=0 directly in the sigma coframe and |Omega|^2=2,
  * the exact torsion formula and strict positivity,
  * exact Ric=-3g at several rational points using the independent Koszul engine,
  * vanishing of the trace-free opposite-chirality curvature block globally,
  * nonzero transverse W^+ action at p=1/2.
Output: ../data/step58/exact_verification.json.
"""
import sympy as sp, os, sys, json
here=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,here)
p=sp.symbols('p', positive=True)
G=4*(3*p**2+1)/((1-p)**2*(1+p)**2*(3*p-1)*(3*p+1))
A=[
  4*(3*p-1)*(3*p**2+1)/(3*(1-p)*(1+p)**2),
  4*(3*p+1)*(3*p**2+1)/(3*(1-p)**2*(1+p)),
  64*p**2/((1-p)*(1+p)*(3*p**2+1))]
X=[(1-p)**3*(3*p+1)/(16*p**3),
   (1+p)**3*(3*p-1)/(16*p**3), sp.Integer(0)]
n=[-1,1,1]
# Positive square roots on 1/3<p<1.  Supplying them explicitly avoids
# SymPy's branch-generated Abs/sign expressions.
rho=2*sp.sqrt(3*p**2+1)/((1-p)*(1+p)*sp.sqrt((3*p-1)*(3*p+1)))
a=[
  2*sp.sqrt((3*p-1)*(3*p**2+1)/3)/((1+p)*sp.sqrt(1-p)),
  2*sp.sqrt((3*p+1)*(3*p**2+1)/3)/((1-p)*sp.sqrt(1+p)),
  8*p/sp.sqrt((1-p)*(1+p)*(3*p**2+1))]
def simp(z):
    z=sp.powdenest(z,force=True)
    return sp.factor(sp.cancel(sp.powsimp(sp.trigsimp(z),force=True)))
def Dt(z): return sp.diff(z,p)/rho
# Log derivatives and W_i^2 are rational; these explicit positive/negative
# branches are the interval-valid square roots.
h=[simp(sp.diff(A[i],p)/(2*A[i]*rho)) for i in range(3)]
W=[
  -sp.sqrt((1-p)**2*(3*p-1)*(3*p**2+1)/(64*p**2*(3*p+1))),
  sp.sqrt((1+p)**2*(3*p+1)*(3*p**2+1)/(64*p**2*(3*p-1))),
  sp.sqrt(36*p**2*(1-p)**2*(1+p)**2/((3*p-1)*(3*p+1)*(3*p**2+1)**3))]
W=[simp(z) for z in W]
S=sum(h)
Q=h[0]*h[1]+h[0]*h[2]+h[1]*h[2]+sum(z*z for z in W)-2*(W[0]*W[1]+W[0]*W[2]+W[1]*W[2])
resQ=simp(Q-3)
resh=[]; resW=[]
for i in range(3):
    j,k=(i+1)%3,(i+2)%3
    # h_i'=-h_i S+2(W_i^2-(W_j-W_k)^2)-lambda, lambda=-3
    resh.append(simp(Dt(h[i])-(-h[i]*S+2*(W[i]**2-(W[j]-W[k])**2)+3)))
    resW.append(simp(Dt(W[i])-W[i]*(h[i]-h[j]-h[k])))
mu=[simp(2*W[i]-h[(i+1)%3]-h[(i+2)%3]) for i in range(3)]
resX=[simp(Dt(X[i])-2*mu[i]*X[i]) for i in range(2)]
resunit=simp(X[0]+X[1]-1)
# Direct closure in sigma coordinates: V_i=x_i sqrt(A_j A_k), U_i=x_i sqrt(G A_i), V_i'=2n_i U_i.
x=[sp.sqrt((1-p)**3*(3*p+1))/(4*p**sp.Rational(3,2)),
   sp.sqrt((1+p)**3*(3*p-1))/(4*p**sp.Rational(3,2)),sp.Integer(0)]
U=[]; Vcoef=[]; resclose=[]
for i in range(2):
    j,k=(i+1)%3,(i+2)%3
    U.append(simp(x[i]*sp.sqrt(G*A[i])))
    Vcoef.append(simp(x[i]*sp.sqrt(A[j]*A[k])))
    resclose.append(simp(sp.diff(Vcoef[-1],p)-2*n[i]*U[-1]))
# q from the independently derived connection formula.
b=[h[0]+W[0]-W[1]-W[2],h[1]-W[0]+W[1]-W[2],h[2]-W[0]-W[1]+W[2]]
q=simp(2*(sum(X[i]*mu[i]**2 for i in range(3))+(X[0]+X[1])*b[2]**2+(X[0]+X[2])*b[1]**2+(X[1]+X[2])*b[0]**2))
qtarget=36*(1-p**2)**3/(1+3*p**2)**3
resq=simp(q-qtarget)

# Independent Koszul curvature engine.
os.environ['NB']='-1,1,1'
import step56_bianchiA_ake as B
t=B.t; af=[B.a,B.b,B.c]
sa,sb,sc,sA,sB,sC,sAp,sBp,sCp=sp.symbols('sa sb sc sA sB sC sAp sBp sCp')
def tosym(e):
    e=e.subs({sp.diff(af[0],t,2):sAp,sp.diff(af[1],t,2):sBp,sp.diff(af[2],t,2):sCp})
    e=e.subs({sp.diff(af[0],t):sA,sp.diff(af[1],t):sB,sp.diff(af[2],t):sC})
    return e.subs({af[0]:sa,af[1]:sb,af[2]:sc})
args=[sa,sb,sc,sA,sB,sC,sAp,sBp,sCp]
ad=[simp(Dt(z)) for z in a]; add=[simp(Dt(z)) for z in ad]
submetric=dict(zip(args,a+ad+add))
# Exact rational-point direct Ricci checks, deliberately independent of simplification along the flow.
RicS=B.Ric.applyfunc(tosym)
point_checks={}
for pv in [sp.Rational(2,5),sp.Rational(1,2),sp.Rational(3,4)]:
    subp={p:pv}
    vals={v:sp.simplify(z.subs(subp)) for v,z in submetric.items()}
    RR=RicS.applyfunc(lambda z:sp.simplify(z.subs(vals)))
    point_checks[str(pv)]=[[str(sp.simplify(RR[i,j]+(3 if i==j else 0))) for j in range(4)] for i in range(4)]
# Curvature operator blocks.  Trace-free vanishing is independent of the overall Riemann sign.
def form_basis(sign):
    out=[]
    for i,(j,k) in zip([1,2,3],[(2,3),(3,1),(1,2)]):
        F=sp.zeros(4); F[0,i]=1; F[i,0]=-1; F[j,k]=sign; F[k,j]=-sign; out.append(F)
    return out
Bp=form_basis(1); Bm=form_basis(-1)
# Build only the contractions needed, first in generic a,a',a'' symbols.
RmS={(i,j,k):[tosym(z) for z in val] for (i,j,k),val in B.Rm.items()}
def rop(F,H):
    z=0
    for i in range(4):
      for j in range(4):
       if F[i,j]!=0:
        for k in range(4):
         for l in range(4):
          if H[k,l]!=0: z += sp.Rational(1,4)*RmS[(i,j,k)][l]*F[i,j]*H[k,l]
    return sp.factor(z)
def block(basis): return sp.Matrix([[rop(F,H) for H in basis] for F in basis])
Mminus_generic=block(Bm); Mplus_generic=block(Bp)
Mminus=Mminus_generic.applyfunc(lambda z:simp(z.subs(submetric)))
trm=simp(sp.trace(Mminus)/3)
Wminus_tf=(Mminus-trm*sp.eye(3)).applyfunc(simp)
# At p=1/2 show the plus block does not preserve Omega: for a diagonal block this is
# x1*x2*(M22-M11), and in general use the 2x2 determinant of (x,Mx).
Mplus_half=Mplus_generic.applyfunc(lambda z:sp.simplify(z.subs(submetric).subs(p,sp.Rational(1,2))))
xh=sp.Matrix([sp.sqrt(sp.Rational(5,32)),sp.sqrt(sp.Rational(27,32)),0])
yh=Mplus_half*xh
eta_wedge=sp.simplify(xh[0]*yh[1]-xh[1]*yh[0])

checks={'constraint':str(resQ),'h_flow':[str(z) for z in resh],'W_flow':[str(z) for z in resW],
        'unit':str(resunit),'X_flow':[str(z) for z in resX],'closure':[str(z) for z in resclose],
        'q_residual':str(resq),'direct_Ricci_residuals':point_checks,
        'Wminus_tracefree':[[str(Wminus_tf[i,j]) for j in range(3)] for i in range(3)],
        'Mplus_at_half':[[str(Mplus_half[i,j]) for j in range(3)] for i in range(3)],
        'Omega_MOmega_wedge_at_half':str(eta_wedge),
        'h':[str(z) for z in h],'W':[str(z) for z in W],'mu':[str(z) for z in mu],
        'U':[str(z) for z in U],'V':[str(z) for z in Vcoef],'q':str(q)}
# Fail loudly if any central exact identity is nonzero.
outdir=os.path.join(here,'../data/step58'); os.makedirs(outdir,exist_ok=True)
json.dump(checks,open(os.path.join(outdir,'exact_verification.json'),'w'),indent=1)
print('resQ',resQ); print('resh',resh); print('resW',resW); print('resX',resX); print('resclose',resclose); print('resunit',resunit); print('resq',resq)
assert resQ==0 and all(z==0 for z in resh+resW+resX+resclose) and resunit==0 and resq==0
assert all(Wminus_tf[i,j]==0 for i in range(3) for j in range(3))
assert eta_wedge!=0
assert all(v=='0' for R in point_checks.values() for row in R for v in row)
print('ALL EXACT CHECKS PASSED')
print('h=',h); print('W=',W); print('mu=',mu)
print('q=',q)
print('Mminus=',Mminus)
print('Mplus(p=1/2)=',Mplus_half)
print('Omega wedge M Omega at p=1/2=',eta_wedge)
