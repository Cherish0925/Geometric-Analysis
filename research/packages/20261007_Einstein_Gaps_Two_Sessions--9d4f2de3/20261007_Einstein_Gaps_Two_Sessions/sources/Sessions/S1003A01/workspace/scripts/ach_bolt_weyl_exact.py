"""Exact Weyl halves at an O(-1) Einstein bolt from the regular 2-jet (Step 16).

Peer convention: g=dt^2+A(t)^2 sigma1^2+B(t)^2 sigma2^2+C(t)^2 sigma3^2,
C collapses, A(0)=B(0)=b, C=t+..., Ric=-6g.  The validated family has
A-B=d t^4+..., while the Weyl tensor at the bolt depends only on the 2-jet.
This script derives the finite t->0 curvature operator from the Cartan formulas and
projects it to the two Lambda^2 chiral blocks using the convention in
o11_rotated_cell.py.  It then evaluates b=4/5 exactly.
"""
import sympy as sp
from perp_cartan_verify import Om,R

t=sp.symbols('t',positive=True)
br=sp.Dummy('br',positive=True)
# From the validated Fuchsian series: sigma=(A+B)/2-b=(49/20)t^2+O(t^4),
# gamma=C/t-1=-(25/24)t^2+O(t^4) at b=4/5.  Keep general 2-jet symbols first.
A2,B2,C3=sp.symbols('A2 B2 C3',real=True)
AA=br+A2*t**2; BB=br+B2*t**2; CC=t+C3*t**3
subs={sp.symbols('a'):AA,sp.symbols('b'):BB,sp.symbols('c'):CC,
      sp.symbols('a1'):sp.diff(AA,t),sp.symbols('b1'):sp.diff(BB,t),sp.symbols('c1'):sp.diff(CC,t),
      sp.symbols('a2'):sp.diff(AA,t,2),sp.symbols('b2'):sp.diff(BB,t,2),sp.symbols('c2'):sp.diff(CC,t,2)}
# Use the actual symbols exported by the module (same names, but make substitution explicit by name).
import perp_cartan_verify as pc
subs={pc.a:AA,pc.b:BB,pc.c:CC,pc.a1:sp.diff(AA,t),pc.b1:sp.diff(BB,t),pc.c1:sp.diff(CC,t),
      pc.a2:sp.diff(AA,t,2),pc.b2:sp.diff(BB,t,2),pc.c2:sp.diff(CC,t,2)}
pairs=[(0,1),(0,2),(0,3),(2,3),(3,1),(1,2)]
Rop=sp.Matrix([[sp.limit(pc.R(i,j,k,l).subs(subs),t,0) for k,l in pairs] for i,j in pairs])
sq=sp.sqrt(2)/2
LA=sp.zeros(3,6);LB=sp.zeros(3,6)
for k in range(3): LA[k,k]=sq;LA[k,3+k]=sq;LB[k,k]=sq;LB[k,3+k]=-sq
# Scalar at bolt from curvature operator / Cartan Ricci; Weyl projection is R_chiral-s/12 I.
Riclim=[sp.limit(q.subs(subs),t,0) for q in pc.Ric]; scal=sp.simplify(sum(Riclim))
WA=sp.simplify(LA*Rop*LA.T-scal*sp.eye(3)/12)
WB=sp.simplify(LB*Rop*LB.T-scal*sp.eye(3)/12)
nA=sp.simplify(sp.trace(WA.T*WA));nB=sp.simplify(sp.trace(WB.T*WB))
vals={br:sp.Rational(4,5),A2:sp.Rational(49,20),B2:sp.Rational(49,20),C3:-sp.Rational(25,24)}
print('Rop_bolt =');print(Rop)
print('scalar_bolt =',scal)
print('WA =');print(WA);print('WB =');print(WB)
print('norms general:',sp.factor(nA),sp.factor(nB))
print('b=4/5 Einstein 2-jet: scalar=',sp.simplify(scal.subs(vals)))
print('WA=',sp.simplify(WA.subs(vals)))
print('WB=',sp.simplify(WB.subs(vals)))
print('norms=',sp.factor(nA.subs(vals)),sp.factor(nB.subs(vals)))
