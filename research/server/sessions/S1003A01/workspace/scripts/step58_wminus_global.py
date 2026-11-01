"""All-p exact curvature-block reduction for the explicit Bianchi-VIII branch.
Imports the rational quadratic-extension state from step58_exact_bianchiVIII_fast
but independently contracts the Step-56 Koszul Riemann tensor, substitutes the
explicit metric, and reduces in Q(p,y)/(y^2-D). Output step58/wminus_global.json.
"""
import sympy as s, os, sys, json
here=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,here)
# Importing runs/checks the fast script; its exact assertions must pass.
import step58_exact_bianchiVIII_fast as E
p,y,D,red=E.p,E.y,E.D,E.red
B=E.B; cv=E.cv; subs=E.subs
# Build unnormalised SD/ASD bases. Overall scale/sign does not affect TF vanishing.
def basis(sign):
 out=[]
 for i,(j,k) in zip([1,2,3],[(2,3),(3,1),(1,2)]):
  F=s.zeros(4);F[0,i]=1;F[i,0]=-1;F[j,k]=sign;F[k,j]=-sign;out.append(F)
 return out
BP,BM=basis(1),basis(-1)
# Substitute explicit a,a',a'' before contraction; simplify each R component once.
# Replace branch-heavy explicit square roots in E.subs by formal radii a_i.
# Curvature entries are homogeneous rational expressions; after substitution, all
# trace-free block entries depend only on A_i=a_i^2, h_i and h_i'+h_i^2.
r1,r2,r3=s.symbols('r1 r2 r3', positive=True)
h=E.h; hp=[E.Dt(z) for z in h]
formal={E.sa:r1,E.sb:r2,E.sc:r3,E.sA:r1*h[0],E.sB:r2*h[1],E.sC:r3*h[2],E.sAp:r1*(hp[0]+h[0]**2),E.sBp:r2*(hp[1]+h[1]**2),E.sCp:r3*(hp[2]+h[2]**2)}
Rm={key:[s.together(cv(z).subs(formal)) for z in vv] for key,vv in B.Rm.items()}
def entry(F,H):
 z=0
 for i in range(4):
  for j in range(4):
   if F[i,j]:
    for k in range(4):
     for l in range(4):
      if H[k,l]:z+=s.Rational(1,4)*Rm[(i,j,k)][l]*F[i,j]*H[k,l]
 return red(z)
def block(bs):return s.Matrix([[entry(F,H) for H in bs] for F in bs])
Mm=block(BM);Mp=block(BP)
Wm=(Mm-s.trace(Mm)/3*s.eye(3))
# Diagonal block entries contain radii only through squares; substitute A_i.
Wm=Wm.applyfunc(lambda z:red(s.cancel(s.powdenest(z.subs({r1**2:E.A[0],r2**2:E.A[1],r3**2:E.A[2]}),force=True))))
print('Wm residual=',Wm,flush=True)
assert Wm==s.zeros(3)
# Non-eigenform: wedge x,M+x. Its square is rational, avoiding roots.
X1,X2=E.X[0],E.X[1]
# Both blocks are diagonal in this diagonal metric.
assert all(Mp[i,j]==0 for i in range(3) for j in range(3) if i!=j)
Mp=Mp.applyfunc(lambda z:red(s.cancel(s.powdenest(z.subs({r1**2:E.A[0],r2**2:E.A[1],r3**2:E.A[2]}),force=True))))
eta_wedge_sq=red(X1*X2*(Mp[1,1]-Mp[0,0])**2)
assert eta_wedge_sq!=0
od=os.path.join(here,'../data/step58');os.makedirs(od,exist_ok=True)
out={'minus_block':[[str(Mm[i,j]) for j in range(3)] for i in range(3)],'minus_tracefree':[[str(Wm[i,j]) for j in range(3)] for i in range(3)],'plus_block':[[str(Mp[i,j]) for j in range(3)] for i in range(3)],'Omega_MOmega_wedge_sq':str(eta_wedge_sq)}
json.dump(out,open(os.path.join(od,'wminus_global.json'),'w'),indent=1)
print('GLOBAL OPPOSITE WEYL BLOCK VANISHES EXACTLY')
print('Mm=',Mm);print('Mp=',Mp);print('non-eigen wedge^2=',eta_wedge_sq)
