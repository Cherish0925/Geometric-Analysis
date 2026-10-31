"""Low-cost symbolic sign test for the perpendicular log-neck coefficient.

It recomputes the Step-10 CH result after t -> i t analytic continuation at the
level of the exact family. For real positive-curvature axes use
S_+(t)=sin t, C_+(t)=cos t. This is obtained from the CH axes sinh,cosh by
T=i t and simultaneously x0_CH=-x0_FS (so sqrt(sinh(T)^2+x0_CH)=i
sqrt(sin(t)^2+x0_FS)). The order-x0^2 density and dT both acquire signs whose
product is checked explicitly by substituting into the already exact CH form.
This is an algebraic continuation check, not an independent geometric derivation.
"""
import sympy as s
C1,C2,C3,k=s.symbols('C1 C2 C3 k',real=True)
# Step-10 exact CH forms, generalized by the continuation sign k where k=+1
# denotes CH and k=-1 denotes the analytically continued positive collar.
# x0 -> k*x0 changes all first-order u channels by k, so every quadratic square
# and the cubic u1*(bulk u2)*(tail u3) is even in k at order x0^2.
S1=(6*C1-2*C2-2*C3-5*k)**2/4
S2=(2*C1-6*C2+2*C3-1*k)**2/4
S3=(2*C1+2*C2-6*C3-3*k)**2/4
cub=-6*k*(3*C1-C2-C3-k)
scal=(2*C1+2*C2+2*C3-7*k)**2/4
for name,f in [('P',s.expand(S1+S2+S3+cub)),('J',s.expand(S1+S2+S3+cub+scal))]:
 print(name,s.factor(f))
 for sign in [1,-1]:
  q=s.expand(f.subs(k,sign)); sol=s.solve([s.diff(q,z) for z in (C1,C2,C3)],(C1,C2,C3),dict=True)[0]
  print(' sign',sign,'opt',sol,'value',s.factor(q.subs(sol)))
