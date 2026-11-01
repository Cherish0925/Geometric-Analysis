#!/usr/bin/env python3
"""Step 66: compatibility/constraint equation for the U(2)-invariant EH linearized Ricci system.

The algebraic matrix extraction showed rank(M)=2, rank_aug=3 for unknowns (f1',f2'',f3''):
there is a lower-order compatibility constraint, not simply a decoupled 2+1 ODE.
Compute the left null vector v of M and constraint v^T rhs=0. Then solve two independent
equations for f2'', f3'' in terms of f1' and lower-order data.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'step66_ode_compatibility.json'
D=json.loads((ROOT/'data'/'step66_ode_matrix_extract.json').read_text())
r,L=sp.symbols('r L')
a0,b0,c0,a1,b1,c1,a2,b2,c2=sp.symbols('a0 b0 c0 a1 b1 c1 a2 b2 c2')
# reconstruct equations from strings using symbols
loc=locals()
F=[sp.sympify(s,locals=loc) for s in D['algebraic_equations']]
unknowns=[a1,b2,c2]
M,rhs=sp.linear_eq_to_matrix(F,unknowns)
left_null=M.T.nullspace()
print('left null dimension',len(left_null))
constraint=None
if left_null:
    v=left_null[0]
    print('left null v=', [sp.factor(x) for x in v])
    constraint=sp.factor((v.T*rhs)[0])
    print('compatibility v^T rhs =')
    print(constraint)
    # simplify clearing denominators
    constraint_poly=sp.factor(sp.together(constraint).as_numer_denom()[0])
    print('constraint numerator=')
    print(constraint_poly)
else:
    v=None; constraint_poly=None
# Solve equations F11,F33 for b2,c2 in terms of a1
sol23=sp.solve([F[1],F[2]],[b2,c2],dict=True,simplify=True)[0]
print('\nF11,F33 solve:')
for k,val in sol23.items(): print(k,'=',sp.factor(val))
# Solve compatibility for a1, if possible
sola=sp.solve(constraint_poly,a1,dict=True,simplify=True) if constraint_poly is not None else []
print('\nconstraint solve for a1:', sola[:1])
# With a1 constraint, b2,c2 become determined.
if sola:
    a1_expr=sp.factor(sola[0][a1])
    b2_expr=sp.factor(sol23[b2].subs(a1,a1_expr))
    c2_expr=sp.factor(sol23[c2].subs(a1,a1_expr))
    print('a1=',a1_expr)
    print('b2=',b2_expr)
    print('c2=',c2_expr)
else:
    a1_expr=b2_expr=c2_expr=None
OUT.write_text(json.dumps({
 'status':'ok',
 'left_null':[str(sp.factor(x)) for x in v] if v is not None else None,
 'constraint':str(constraint),
 'constraint_numerator':str(constraint_poly),
 'solve_F11_F33':{str(k):str(sp.factor(val)) for k,val in sol23.items()},
 'constraint_solve_a1':str(a1_expr),
 'determined_b2':str(b2_expr),
 'determined_c2':str(c2_expr),
},indent=2,default=str))
print('Output:',OUT)
