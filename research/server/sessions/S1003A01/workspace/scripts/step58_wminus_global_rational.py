"""Global half-conformal-flatness check using rational radii symbols.
The diagonal Bianchi curvature block entries are invariant under replacing radii
by symbols with pairwise ratio products W_i. We rewrite every occurrence of
r_i/r_j in terms of W and eliminate radii before substituting the explicit branch.
"""
import sympy as s, os, sys, json
here=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,here)
import step58_exact_bianchiVIII_fast as E
B=E.B; cv=E.cv; red=E.red; p,y=E.p,E.y
r1,r2,r3=s.symbols('r1 r2 r3', positive=True)
h=E.h; hp=[E.Dt(z) for z in h]
formal={E.sa:r1,E.sb:r2,E.sc:r3,E.sA:r1*h[0],E.sB:r2*h[1],E.sC:r3*h[2],E.sAp:r1*(hp[0]+h[0]**2),E.sBp:r2*(hp[1]+h[1]**2),E.sCp:r3*(hp[2]+h[2]**2)}
# Substitute explicit rational representatives for the radii in the quadratic field.
# From W1=-r1/(r2 r3), W2=r2/(r1 r3), W3=r3/(r1 r2):
# r1^2=-1/(W2 W3), r2^2=-1/(W1 W3), r3^2=-1/(W1 W2).
# Curvature entries involve only even total powers; use squared-radius variables via
# a scaling parameter R and rational ratios. Set r1=1, r2^2=W2/(-W1), r3^2=W3/(-W1).
# Branch radicals cancel from tracefree combinations; square-root substitution is delayed.
W1,W2,W3=E.W
u=s.symbols('u', positive=True);v=s.symbols('v', positive=True)
# relation u^2=-W2/W1, v^2=-W3/W1; r=(1,u,v), common scale fixed by r1^2=-1/(W2W3)
R2=red(-1/(W2*W3))
# Homothetic scale matters for curvature; use r1=sqrt(R2), r2=u*r1, r3=v*r1.
R=s.symbols('R', positive=True)
radsub={r1:R,r2:u*R,r3:v*R}
Rm={key:[s.factor(cv(z).subs(formal).subs(radsub)) for z in vv] for key,vv in B.Rm.items()}
def basis(sign):
 out=[]
 for i,(j,k) in zip([1,2,3],[(2,3),(3,1),(1,2)]):
  F=s.zeros(4);F[0,i]=1;F[i,0]=-1;F[j,k]=sign;F[k,j]=-sign;out.append(F)
 return out
def ent(F,H):return s.factor(sum(s.Rational(1,4)*Rm[(i,j,k)][l]*F[i,j]*H[k,l] for i in range(4) for j in range(4) for k in range(4) for l in range(4)))
def block(bs):return s.Matrix([[ent(F,H) for H in bs] for F in bs])
Mm=block(basis(-1));Mp=block(basis(1));Wm=Mm-s.trace(Mm)/3*s.eye(3)
# Entries are rational in u^2,v^2,R^2. Substitute these directly by simultaneous xreplace
# after collecting even powers; no branch square roots remain in diagonal tracefree entries.
subs_even={u**2:red(-W2/W1),v**2:red(-W3/W1),R**2:R2}
def ev(z):
 z=s.cancel(z)
 z=z.xreplace(subs_even)
 # repeat because powers can emerge after cancellation
 z=s.cancel(z).subs(subs_even, simultaneous=True)
 return red(z)
Wm2=Wm.applyfunc(ev)
print('Wm=',Wm2,flush=True)
assert Wm2==s.zeros(3)
Mp2=Mp.applyfunc(ev)
X1,X2=E.X[0],E.X[1]
wedge2=red(X1*X2*(Mp2[1,1]-Mp2[0,0])**2)
assert wedge2!=0
od=os.path.join(here,'../data/step58');os.makedirs(od,exist_ok=True);json.dump({'minus_tracefree':[[str(Wm2[i,j]) for j in range(3)] for i in range(3)],'plus':[[str(Mp2[i,j]) for j in range(3)] for i in range(3)],'wedge2':str(wedge2)},open(os.path.join(od,'wminus_global.json'),'w'),indent=1)
print('GLOBAL HALF-CONFORMAL FLATNESS EXACT; wedge2=',wedge2)
