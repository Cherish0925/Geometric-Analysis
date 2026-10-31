"""Exact independent check of the (h,beta,q) Ricci control equations.

Substitute a=e^{h+2 beta/3}, b=e^{h-beta/3+q/2}, c=e^{h-beta/3-q/2}
into the independent Cartan Ricci tensor and compare D,E,H with the formulas
used by saturation_optimal_control.py.  Here H=Ric00-(Ric11+Ric22+Ric33)/3.
"""
import sys
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[2]/'S1003A01'/'workspace'/'scripts'))
import perp_cartan_verify as pc  # noqa
h,be,q=sp.symbols('h be q', real=True)
h1,be1,q1,h2,be2,q2=sp.symbols('h1 be1 q1 h2 be2 q2', real=True)
A=[sp.exp(h+2*be/3),sp.exp(h-be/3+q/2),sp.exp(h-be/3-q/2)]
logjets=[(h1+2*be1/3,h2+2*be2/3),(h1-be1/3+q1/2,h2-be2/3+q2/2),(h1-be1/3-q1/2,h2-be2/3-q2/2)]
sub={pc.a:A[0],pc.b:A[1],pc.c:A[2]}
for x,x1,x2,aa,(l1,l2) in zip([pc.a,pc.b,pc.c],[pc.a1,pc.b1,pc.c1],[pc.a2,pc.b2,pc.c2],A,logjets):
    sub[x1]=aa*l1; sub[x2]=aa*(l2+l1*l1)
R=[sp.factor(v.subs(sub)) for v in pc.Ric]
D=sp.factor(R[2]-R[3])
E=sp.factor(R[1]-(R[2]+R[3])/2)
H=sp.factor(R[0]-(R[1]+R[2]+R[3])/3)
VD=8*(sp.exp(-4*be/3)*sp.sinh(2*q)-sp.exp(2*be/3)*sp.sinh(q))
VE=4*sp.exp(8*be/3)-4*sp.exp(2*be/3)*sp.cosh(q)-8*sp.exp(-4*be/3)*sp.sinh(q)**2
VH=sp.Rational(2,3)*sp.exp(8*be/3)-sp.Rational(8,3)*sp.exp(2*be/3)*sp.cosh(q)+sp.Rational(8,3)*sp.exp(-4*be/3)*sp.sinh(q)**2
Df=-q2-3*h1*q1+sp.exp(-2*h)*VD
Ef=-be2-3*h1*be1+sp.exp(-2*h)*VE
Hf=-2*h2-sp.Rational(2,3)*be1**2-sp.Rational(1,2)*q1**2+sp.exp(-2*h)*VH
checks={'D':sp.simplify(D-Df),'E':sp.simplify(E-Ef),'H':sp.simplify(H-Hf)}
print(checks)
if any(v!=0 for v in checks.values()): raise SystemExit(1)
