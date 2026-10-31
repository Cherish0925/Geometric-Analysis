"""Symbolic checks for the perpendicular relative calibration.

Verifies purely algebraic steps used in Step 6:
  C = sum u_i^2 + u1*u2*u3,
  H_i = (1/2) dC/du_i,
  relative-calibration square completion with Phi=C-u2^2,
and derives the residual for the candidate Hamilton-Jacobi correction
  psi = -(a2^2/(a1*a3))*u1*u3.

This does not verify the curvature-to-u identities, which are checked numerically by
perp_spin_diagnostics.py against the independent JAX coordinate curvature.
"""
import sympy as s
u1,u2,u3=s.symbols('u1 u2 u3',real=True)
l1,l2,l3=s.symbols('l1 l2 l3',positive=True)
v1,v2,v3=s.symbols('v1 v2 v3',real=True) # udot
C=u1**2+u2**2+u3**2+u1*u2*u3
H=[s.diff(C,u)/2 for u in (u1,u2,u3)]
P=sum([l/4*(v-2*h/l)**2 for l,v,h in zip((l1,l2,l3),(v1,v2,v3),H)])
Phi=C-u2**2
# completion: for Phi drop of 1, use plus flow in 1,3 and selected CH flow in 2
R=(l1/4*(v1+2*H[0]/l1)**2+l3/4*(v3+2*H[2]/l3)**2
   +l2/4*(v2-(2*u2-u1*u3)/l2)**2+2*u1*u2*u3/l2)
# Difference P - R equals -dPhi/dt, so integrating P gives Phi_b-Phi_e + int R.
dPhi=sum(s.diff(Phi,u)*v for u,v in zip((u1,u2,u3),(v1,v2,v3)))
print('H:',H)
print('P - R + dPhi =',s.factor(s.expand(P-R+dPhi)))

# General Hamilton-Jacobi residual R_B = grad_a B.(u+gamma)+ sum Bu(2H-Bu)/lambda.
a1,a2,a3=s.symbols('a1 a2 a3',positive=True)
g1=(a2**2+a3**2-a1**2)/(a2*a3)
g2=(a3**2+a1**2-a2**2)/(a3*a1)
g3=(a1**2+a2**2-a3**2)/(a1*a2)
ls=[a2*a3/a1,a3*a1/a2,a1*a2/a3]
psi=-a2**2/(a1*a3)*u1*u3
B=Phi+psi
avec=(a1,a2,a3); uvec=(u1,u2,u3); gam=(g1,g2,g3)
RB=sum(s.diff(B,a)*(u+g) for a,u,g in zip(avec,uvec,gam))
RB+=sum(s.diff(B,u)*(2*h-s.diff(B,u))/l for u,h,l in zip(uvec,H,ls))
print('RB(B0)=',s.factor(sum(s.diff(Phi,u)*(2*h-s.diff(Phi,u))/l for u,h,l in zip(uvec,H,ls))))
print('RB(B0+psi)=')
print(s.factor(RB))
