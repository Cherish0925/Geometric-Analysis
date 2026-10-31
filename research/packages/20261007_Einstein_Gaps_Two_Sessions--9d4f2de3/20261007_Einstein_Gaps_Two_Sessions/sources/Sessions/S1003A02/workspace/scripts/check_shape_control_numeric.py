"""High-precision randomized check of the exact shape-control formulas."""
import sys, random
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[2]/'S1003A01'/'workspace'/'scripts'))
import perp_cartan_verify as pc  # noqa
h,be,q,h1,be1,q1,h2,be2,q2=sp.symbols('h be q h1 be1 q1 h2 be2 q2')
A=[sp.exp(h+2*be/3),sp.exp(h-be/3+q/2),sp.exp(h-be/3-q/2)]
lj=[(h1+2*be1/3,h2+2*be2/3),(h1-be1/3+q1/2,h2-be2/3+q2/2),(h1-be1/3-q1/2,h2-be2/3-q2/2)]
vars=[h,be,q,h1,be1,q1,h2,be2,q2]
VD=8*(sp.exp(-4*be/3)*sp.sinh(2*q)-sp.exp(2*be/3)*sp.sinh(q))
VE=4*sp.exp(8*be/3)-4*sp.exp(2*be/3)*sp.cosh(q)-8*sp.exp(-4*be/3)*sp.sinh(q)**2
VH=sp.Rational(2,3)*sp.exp(8*be/3)-sp.Rational(8,3)*sp.exp(2*be/3)*sp.cosh(q)+sp.Rational(8,3)*sp.exp(-4*be/3)*sp.sinh(q)**2
F=[-q2-3*h1*q1+sp.exp(-2*h)*VD,-be2-3*h1*be1+sp.exp(-2*h)*VE,
   -2*h2-sp.Rational(2,3)*be1**2-sp.Rational(1,2)*q1**2+sp.exp(-2*h)*VH]
mx=0
for seed in range(12):
    random.seed(seed); vv=[random.uniform(-.5,.5) for _ in vars]
    base=dict(zip(vars,vv)); av=[sp.N(x.subs(base),40) for x in A]
    sub={pc.a:av[0],pc.b:av[1],pc.c:av[2]}
    for x,x1,x2,aa,(l1,l2) in zip([pc.a,pc.b,pc.c],[pc.a1,pc.b1,pc.c1],[pc.a2,pc.b2,pc.c2],av,lj):
        l1v=sp.N(l1.subs(base),40); l2v=sp.N(l2.subs(base),40)
        sub[x1]=aa*l1v; sub[x2]=aa*(l2v+l1v*l1v)
    R=[sp.N(z.subs(sub),35) for z in pc.Ric]
    lhs=[R[2]-R[3],R[1]-(R[2]+R[3])/2,R[0]-(R[1]+R[2]+R[3])/3]
    rhs=[sp.N(z.subs(base),35) for z in F]
    err=max(abs(float(lhs[i]-rhs[i])) for i in range(3)); mx=max(mx,err)
    print(seed,err)
print('max_abs_error',mx)
if mx>1e-25: raise SystemExit(1)
