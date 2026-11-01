#!/usr/bin/env python3
"""Step 66: robust matrix extraction of the EH linearized Ricci ODE system.

Use Step-65 full-4D coordinate-component dRic formulas, convert to frame components,
replace f_i and their derivatives by algebraic symbols, and solve the 3x3 linear
system for X=(f1', f2'', f3'').  This avoids SymPy Function solve fragility.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'data'/'step65_full4d_lichnerowicz.json').read_text())
OUT=ROOT/'data'/'step66_ode_matrix_extract.json'
r,L=sp.symbols('r L')
f1=sp.Function('f1'); f2=sp.Function('f2'); f3=sp.Function('f3')
loc={'r':r,'Derivative':sp.Derivative,'f1':f1,'f2':f2,'f3':f3}
coord={k:sp.sympify(v,locals=loc) for k,v in D['dRic_at_point'].items()}
W=1-r**-4
# frame equations dRic_frame - L =0. The coordinate formulas in D are coordinate components.
frame={
 '00':sp.factor(W*coord['00']),
 '11':sp.factor(4*coord['11']/r**2),
 '33':sp.factor(4*coord['33']/(r**2*W)),
}
# Algebraic symbols for functions/derivatives.
a0,b0,c0,a1,b1,c1,a2,b2,c2=sp.symbols('a0 b0 c0 a1 b1 c1 a2 b2 c2')
repl={
 f1(r):a0, f2(r):b0, f3(r):c0,
 sp.Derivative(f1(r),r):a1, sp.Derivative(f2(r),r):b1, sp.Derivative(f3(r),r):c1,
 sp.Derivative(f1(r),(r,2)):a2, sp.Derivative(f2(r),(r,2)):b2, sp.Derivative(f3(r),(r,2)):c2,
}
F=[sp.factor((frame[k]-L).subs(repl)) for k in ['00','11','33']]
# Check which unknowns occur.
unknowns=[a1,b2,c2]
print('unknown occurrence:')
for i,Fi in enumerate(F):
    print(i,[u for u in unknowns if Fi.has(u)])
M,vec=sp.linear_eq_to_matrix(F, unknowns)
print('M=')
print(sp.factor(M))
print('rhs=')
print(sp.factor(vec))
rankM=M.rank(); rankAug=M.row_join(vec).rank()
print('rank',rankM,'aug',rankAug)
sol=None
if rankM==len(unknowns):
    solvec=sp.simplify(M.LUsolve(vec))
    sol={str(u):sp.factor(solvec[i]) for i,u in enumerate(unknowns)}
    print('solution:')
    for k,v in sol.items(): print(k,'=',v)
else:
    # Try sequential solve for b2,c2,a1 or alternative unknowns.
    sol_list=sp.solve(F, unknowns, dict=True, simplify=False)
    print('solve list len',len(sol_list))
    if sol_list:
        sol={str(k):sp.factor(v) for k,v in sol_list[0].items()}
        for k,v in sol.items(): print(k,'=',v)
# Bolt singular coefficients using algebraic Taylor finite data.
s=sp.symbols('s')
# finite Taylor replacement in algebraic symbols as r=1+s: approximate f values/derivatives by finite constants (a0 etc).
# To get singular coefficient, substitute r=1+s in F and take lim s*F. Here a_i... are values at bolt.
sing={}
for name,Fi in zip(['F00','F11','F33'],F):
    e=sp.factor(Fi.subs(r,1+s))
    sing[name]=sp.factor(sp.limit(s*e,s,0))
print('sing coeffs:')
for k,v in sing.items(): print(k,v)
OUT.write_text(json.dumps({
 'status':'ok' if sol else 'underdetermined_or_failed',
 'frame_equations':{k:str(frame[k]) for k in frame},
 'algebraic_equations':[str(x) for x in F],
 'unknowns':[str(u) for u in unknowns],
 'matrix':str(M),
 'rhs':str(vec),
 'rank':int(rankM),'rank_aug':int(rankAug),
 'solution':{k:str(v) for k,v in sol.items()} if sol else None,
 'singular_coeffs':{k:str(v) for k,v in sing.items()},
},indent=2,default=str))
print('Output:',OUT)
