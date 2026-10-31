"""Finite coefficient checks only; no PDE convergence is certified."""
from pathlib import Path
source=Path('outputs/Line1_Continuation_20260929D/verify_fifth_line_symbols.py').read_text()
exec(source.split('# The Cartan identity')[0])
def hodge(x):return [x[5],-x[4],x[3],x[2],-x[1],x[0]]
def sd(x):return scale(.5,plus(x,hodge(x)))
barXi=list(map(lambda z:complex(z).conjugate(),Xi_plus))
for u,c in [([1,2,3,4],2+3j),([-2,1,0,3],-1+2j),([0,0,1,-2],1)]:
 q=[u[1],-u[0],u[3],-u[2]]
 d=-u[2]-I*u[3];z=u[0]-I*u[1]
 b=plus(scale(d,theta1),scale(c,theta))
 assert sd(wedge(plus(u,scale(I,q)),b))==scale(d*d+c*z.conjugate(),barXi)
 # Common m^{-3/2} weighting leaves only the displayed Psi1 drift.
 psi1=plus(wedge(e[0],e[1]),wedge(e[2],e[3]))
 correction=plus(plus(scale(d,sd(wedge(plus(scale(3,u),scale(-I,q)),theta1))),scale(c,sd(wedge(scale(3,plus(u,scale(-I,q))),theta)))),plus(scale(-d*d,barXi),scale(-I*c*d.conjugate(),psi1)))
 assert correction==scale(2*I*(c*d.conjugate()-d*z),psi1)
print('PASS: complete polynomial ASD source and common-weight radial transport')
# Matrix action for real Omega_minus: e12-e34.
Om=[[0,1,0,0],[-1,0,0,0],[0,0,0,-1],[0,0,1,0]]
for th,pot in [(theta1,-3),(theta,1)]:
 mat=[sum(Om[i][j]*th[j] for j in range(4)) for i in range(4)]
 assert plus(scale(-1,th),scale(-2*I,mat))==scale(pot,th)
print('PASS: ASD deformation potentials -3 and +1')
# Opposite-type covariant derivative determined by eta=kappa theta1.
G={}
for i,j in product(range(4),repeat=2):
 G[i,j]=[]
 for h in range(4):
  Op=[[0,-complex(theta1[h]).conjugate()],[theta1[h],0]];On=[[0,0],[0,0]]
  G[i,j].append(tr(mul(star(C[i]),sub(mul(On,C[j]),mul(C[j],Op)))).real/2)
for ind,k in [(0,1),(2,3)]:
 for h in range(4):
  ww=[-G[ind,j][h]+I*G[k,j][h] for j in range(4)]
  cc=[(ww[0]-I*ww[1])/2,(ww[2]-I*ww[3])/2]
  expected=([0,complex(theta1[h]).conjugate()] if ind==0 else [-complex(theta1[h]).conjugate(),0])
  assert cc==expected
print('PASS: forced normal energy = 4 m^2 kappa^2 (|d|^2+|c|^2)')
