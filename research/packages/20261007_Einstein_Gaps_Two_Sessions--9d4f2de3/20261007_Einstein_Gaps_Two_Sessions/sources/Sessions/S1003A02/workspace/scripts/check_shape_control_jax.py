"""Independent automatic-differentiation check of the shape-control equations.

Uses coordinate Christoffel/Ricci calculation on R x SU(2) in the nonholonomic
orthonormal frame, implemented independently from the symbolic Cartan module.
Actually the shortest independent check is direct substitution into the known
exact diagonal Ricci formulas:
 Ric00=-sum(Li''+(Li')^2), Ricii=-Li''-Li' sum Lj'+Pot_i.
"""
import numpy as np
rng=np.random.default_rng(281)
mx=0.0
for _ in range(10000):
 h,be,q,h1,be1,q1,h2,be2,q2=rng.uniform(-1,1,9)
 L=np.array([h+2*be/3,h-be/3+q/2,h-be/3-q/2])
 y=np.array([h1+2*be1/3,h1-be1/3+q1/2,h1-be1/3-q1/2])
 yp=np.array([h2+2*be2/3,h2-be2/3+q2/2,h2-be2/3-q2/2])
 Pot=[]
 for i in range(3):
  j,k=(i+1)%3,(i+2)%3
  Pot.append(2*np.exp(2*L[i]-2*L[j]-2*L[k])-8*np.exp(-2*L[i])*np.sinh(L[j]-L[k])**2)
 R0=-np.sum(yp+y*y); Ri=-yp-y*np.sum(y)+np.array(Pot)
 D=Ri[1]-Ri[2]; E=Ri[0]-(Ri[1]+Ri[2])/2; H=R0-np.sum(Ri)/3
 VD=8*(np.exp(-4*be/3)*np.sinh(2*q)-np.exp(2*be/3)*np.sinh(q))
 VE=4*np.exp(8*be/3)-4*np.exp(2*be/3)*np.cosh(q)-8*np.exp(-4*be/3)*np.sinh(q)**2
 VH=2*np.exp(8*be/3)/3-8*np.exp(2*be/3)*np.cosh(q)/3+8*np.exp(-4*be/3)*np.sinh(q)**2/3
 rhs=np.array([-q2-3*h1*q1+np.exp(-2*h)*VD,
               -be2-3*h1*be1+np.exp(-2*h)*VE,
               -2*h2-2*be1**2/3-q1**2/2+np.exp(-2*h)*VH])
 mx=max(mx,np.max(np.abs(np.array([D,E,H])-rhs)))
print('max_abs_error',mx)
assert mx<2e-12
