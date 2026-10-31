"""Exact check of the proposed Bianchi-IX Euler flux identity.

With the session convention int(S3) sigma123=2*pi^2 and
4*pi^2 chi = int (|W|^2-|Ric0|^2/2+s^2/24), the normalized boundary flux bE
should satisfy on an annulus
  P/(8*pi^2) = bE(t1)-bE(t0) + int|W|^2/(4*pi^2)+int s^2/(96*pi^2).
Differentiating gives the pointwise radial density relation
  W |Ric0|^2/4 = bE' + W |W|^2/2 + W s^2/48,
since dV=2*pi^2 W dt and |W|^2 is the full operator norm |W+|^2+|W-|^2.
This script derives every term from the independent Cartan source
S1003A01/workspace/scripts/perp_cartan_verify.py and checks the identity exactly.
"""
from pathlib import Path
import sys
import sympy as sp

HERE=Path(__file__).resolve().parent
PEER=HERE.parents[2]/'S1003A01'/'workspace'/'scripts'
sys.path.insert(0,str(PEER))
import perp_cartan_verify as pc  # noqa: E402

a,b,c,a1,b1,c1,a2,b2,c2=pc.a,pc.b,pc.c,pc.a1,pc.b1,pc.c1,pc.a2,pc.b2,pc.c2
A=[a,b,c]; y=[a1/a,b1/b,c1/c]; W=a*b*c
# intrinsic orbit sectional curvatures, complementary-index form
def K3(i,j,k):
    return sp.factor(((A[j]**2-A[k]**2)**2+2*A[i]**2*(A[j]**2+A[k]**2)-3*A[i]**4)/(A[i]**2*A[j]**2*A[k]**2))
bE=sp.factor(W*(y[0]*K3(0,1,2)+y[1]*K3(1,2,0)+y[2]*K3(2,0,1)-y[0]*y[1]*y[2]))
db=sp.factor(pc.Dt(bE))
# Curvature-operator convention: sum of squares of chiral 3x3 blocks is
# half the 6x6 curvature-operator sum because paired 2-forms have norm sqrt(2).
pairs=[(0,1),(0,2),(0,3),(2,3),(3,1),(1,2)]
Rop=sp.Matrix([[pc.R(i,j,k,l) for k,l in pairs] for i,j in pairs])
sq=sp.sqrt(2)/2
LA=sp.zeros(3,6); LB=sp.zeros(3,6)
for k in range(3):
    LA[k,k]=sq; LA[k,3+k]=sq; LB[k,k]=sq; LB[k,3+k]=-sq
WA=sp.simplify(LA*Rop*LA.T-pc.s*sp.eye(3)/12)
WB=sp.simplify(LB*Rop*LB.T-pc.s*sp.eye(3)/12)
Weyl=sp.factor(sp.trace(WA.T*WA)+sp.trace(WB.T*WB))
rhs=sp.factor(db+W*Weyl/2+W*pc.s**2/48)
lhs=sp.factor(W*pc.ric0sq/4)
res=sp.factor(lhs-rhs)
print('bE =',bE)
print('identity residual =',res)
if sp.simplify(res)!=0:
    raise SystemExit(1)
