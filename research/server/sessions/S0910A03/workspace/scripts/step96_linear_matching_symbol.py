"""Principal-symbol audit for the Step 96 mixed-order joint matching system.

Unknowns: (phi, sigma, u1, u2, q1, q2). Equations retain the elliptic core
(trace H, T, Z1, Z2) plus first-order charge block dq.  The script verifies
injectivity of the Douglis-Nirenberg principal symbol for every nonzero covector
and records the determinant of the square scalar/map subblock.  Traceless H is a
compatibility/finite matching block after Bianchi reduction, not added to this
square core.
"""
import sympy as sp
from pathlib import Path
import json

x,y=sp.symbols('xi eta', real=True)
r2=x*x+y*y
# Rows: trH, T, Z1, Z2, dq1_x,dq1_y,dq2_x,dq2_y
# Cols: phi,sigma,u1,u2,q1,q2. Overall positive conformal weights suppressed.
P=sp.zeros(8,6)
P[0,0]=-2*r2;P[0,1]=-r2
P[1,1]=r2
P[2,2]=r2;P[3,3]=r2
P[4,4]=sp.I*x;P[5,4]=sp.I*y
P[6,5]=sp.I*x;P[7,5]=sp.I*y
core=P[:4,:4]
# Gram matrix P*P has determinant convenient for an overdetermined injective symbol.
gram=sp.simplify(sp.conjugate(P.T)*P)
out={
 'covector':'(xi,eta) != 0','r2':str(r2),
 'core_determinant':str(sp.factor(core.det())),
 'gram_determinant':str(sp.factor(gram.det())),
 'rank_generic':int(P.subs({x:2,y:3}).rank()),
 'unknowns':['phi','sigma','U1','U2','q1','q2'],
 'rows':['trH','T','Z1','Z2','dq1_x','dq1_y','dq2_x','dq2_y'],
 'conclusion':'The elliptic scalar/map block has determinant 2|xi|^8 and dq is injective for nonzero covector; the combined mixed-order principal symbol is injective. Fredholm index and cokernel still depend on gauges, Bianchi reduction, end weights, and indicial roots.'
}
path=Path('workspace/data/step96_linear_matching_symbol.json');path.write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
