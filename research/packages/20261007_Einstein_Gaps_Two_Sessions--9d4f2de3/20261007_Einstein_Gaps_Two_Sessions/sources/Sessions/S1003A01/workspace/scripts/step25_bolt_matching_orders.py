"""Independent asymptotic calculation for a smooth O(-1) Einstein bolt.

The collapsing slot is h=3.  The bolt series is
 a_f=b+c2*t^2+p4*t^4+..., a_g=b+c2*t^2+q4*t^4+...,
 a_h=t+r3*t^3+..., with d=p4-q4.
Set z=(a_h/a_g)^(1/3), r=(a_f*a_g*a_h)^(1/3),
 x=log(a_f/a_g), p=r*(log r)', chi=r*x', eta=r*q', q=log(a_g/a_h).
The output records the leading powers at fixed b and the exact controlled-charge
limit separately.  It is meant to distinguish local bolt regularity from a
scale-one global matching hypothesis.
"""
import json
from pathlib import Path
import sympy as sp

t,b,d=sp.symbols('t b d', positive=True)
c2=(3*b**2+2)/(2*b)
r3=-sp.Rational(2,3)/b**2
# Keep only terms needed for leading orders; p4-q4=d.
ag=b+c2*t**2
# Symmetric common fourth-order terms cancel from x to leading order; choose
# a_f-a_g=d*t^4 because only this difference enters the leading terms below.
af=ag+d*t**4
ah=t+r3*t**3
z3=sp.series(ah/ag,t,0,5).removeO()
# r is expanded through the orders needed for p and eta
r=(af*ag*ah)**sp.Rational(1,3)
x=sp.log(af/ag)
q=sp.log(ag/ah)
p=sp.simplify(r*sp.diff(sp.log(r),t))
chi=sp.simplify(r*sp.diff(x,t))
eta=sp.simplify(r*sp.diff(q,t))
# substitute t=b*z^3 and expand in z
z=sp.symbols('z', positive=True)
def zseries(expr,n=15):
    return sp.series(expr.subs(t,b*z**3),z,0,n).removeO().expand()
out={
 'z3_t_series':str(sp.series(z3.subs(t,b*z**3),z,0,10).removeO()),
 'x':str(zseries(x,16)),
 'chi':str(zseries(chi,14)),
 'p':str(zseries(p,5)),
 'eta':str(zseries(eta,5)),
 'interpretation':'fixed-b smooth bolt expansion; the coefficients are not uniform as b->0',
 'controlled_entry_not_implied':True,
}
# Controlled charge algebra using limiting u variables from the exact spin formula.
X,P,C,N=sp.symbols('X P C N', real=True)
u_f=P+sp.Rational(2,3)*C+sp.Rational(1,3)*N+2*X
u_g=P-sp.Rational(1,3)*C+sp.Rational(1,3)*N-2*X
u_h=-2
bp=sp.factor(2-(u_f**2+u_g**2+u_h**2)-u_f*u_g*u_h)
out['controlled_charge']={'u_limit':[str(u_f),str(u_g),'-2'],
                          'bplus':str(bp),'bplus_plus_2':str(sp.factor(bp+2))}
path=Path(__file__).resolve().parents[1]/'data'/'step25_bolt_matching_orders.json'
path.write_text(json.dumps(out,indent=1)+'\n')
print(json.dumps(out,indent=1))
