#!/usr/bin/env python3
"""Step 66: clean decoupling of Step-65 EH linearized Ricci ODE and bolt regularity analysis.

Uses Step-65 full-4D dRic formulas. Solves frame equations dRic_i = Lambda for
unknowns f1' (constraint), f2'', f3''. Then computes Laurent leading terms at the bolt r=1
under generic finite Taylor data to identify regularity constraints.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step66_ode_decouple_and_regular.json"
D = json.loads((ROOT/"data"/"step65_full4d_lichnerowicz.json").read_text())
r, Lam = sp.symbols('r Lambda')
f1 = sp.Function('f1'); f2=sp.Function('f2'); f3=sp.Function('f3')
loc={'r':r,'Lambda':Lam,'Derivative':sp.Derivative,'f1':f1,'f2':f2,'f3':f3}
coord={k:sp.sympify(v, locals=loc) for k,v in D['dRic_at_point'].items()}
W = 1-r**-4
frame={
 '00': sp.simplify(W*coord['00']),
 '11': sp.simplify(4*coord['11']/r**2),
 '33': sp.simplify(4*coord['33']/(r**2*W)),
}
# equations frame = Lam
F00=sp.simplify(frame['00']-Lam)
F11=sp.simplify(frame['11']-Lam)
F33=sp.simplify(frame['33']-Lam)
f1p=sp.Derivative(f1(r),r); f2pp=sp.Derivative(f2(r),(r,2)); f3pp=sp.Derivative(f3(r),(r,2))
sol=sp.solve([F00,F11,F33],[f1p,f2pp,f3pp],dict=True,simplify=True)
print("number of decoupled solutions", len(sol))
if not sol:
    raise SystemExit(1)
sol=sol[0]
for var in [f1p,f2pp,f3pp]:
    print(var, "=")
    print(sp.factor(sol[var]))

# Bolt Laurent: set r=1+s and finite Taylor data up to needed order.
s=sp.symbols('s')
# Taylor data at bolt (finite in r variable)
a0,a1,a2 = sp.symbols('a0 a1 a2')  # f1
b0,b1,b2 = sp.symbols('b0 b1 b2')  # f2
c0,c1,c2 = sp.symbols('c0 c1 c2')  # f3
subs_taylor={
 f1(r): a0+a1*s+a2*s**2,
 f2(r): b0+b1*s+b2*s**2,
 f3(r): c0+c1*s+c2*s**2,
 sp.Derivative(f1(r),r): a1+2*a2*s,
 sp.Derivative(f2(r),r): b1+2*b2*s,
 sp.Derivative(f3(r),r): c1+2*c2*s,
 sp.Derivative(f1(r),(r,2)): 2*a2,
 sp.Derivative(f2(r),(r,2)): 2*b2,
 sp.Derivative(f3(r),(r,2)): 2*c2,
}
def laurent(expr, order=1):
    e=sp.simplify(expr.subs(r,1+s).subs(subs_taylor))
    return sp.series(e, s, 0, order).removeO()

# Instead of solved RHS (which includes denominators), examine original equations F00,F11,F33 Laurent.
laur={k: sp.factor(laurent(F,0)) for k,F in [('F00',F00),('F11',F11),('F33',F33)]}
print("\nOriginal equation Laurent leading terms:")
for k,v in laur.items():
    print(k, v)
# Compute more detailed expansion to constant term.
laur2={k: sp.factor(laurent(F,2)) for k,F in [('F00',F00),('F11',F11),('F33',F33)]}
print("\nOriginal equation expansion to s^1:")
for k,v in laur2.items():
    print(k, v)

# Solve leading 1/s singular coefficient conditions. Extract coeff of s^-1 when present by multiplying by s and limit.
sing={}
for k,F in [('F00',F00),('F11',F11),('F33',F33)]:
    e=sp.simplify(F.subs(r,1+s).subs(subs_taylor))
    sing[k]=sp.factor(sp.limit(s*e,s,0))
print("\nSingular coeffs s^-1:")
for k,v in sing.items(): print(k,v)
cond_sing=[sp.Eq(v,0) for v in sing.values() if v!=0]
print("singular conditions solve:", sp.solve(cond_sing,[a0,b0,c0,a1,b1,c1,b2,c2],dict=True))

OUT.write_text(json.dumps({
 "status":"ok",
 "frame_equations":{"F00":str(F00),"F11":str(F11),"F33":str(F33)},
 "decoupled":{"f1p":str(sp.factor(sol[f1p])),"f2pp":str(sp.factor(sol[f2pp])),"f3pp":str(sp.factor(sol[f3pp]))},
 "singular_coeffs":{k:str(v) for k,v in sing.items()},
 "laurent_to_s1":{k:str(v) for k,v in laur2.items()},
}, indent=2))
print("Output:", OUT)
