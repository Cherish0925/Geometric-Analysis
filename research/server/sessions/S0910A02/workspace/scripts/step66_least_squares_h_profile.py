#!/usr/bin/env python3
"""Step 66: finite-difference least-squares approximate EH correction profile.

Goal: test the Strategist's certificate-decoupling idea by fitting a non-Kaehler radial
U(2)-invariant tensor profile h=f1 e0^2+f2(e1^2+e2^2)+f3 e3^2 so that
    dRic_EH(h) ~= Lambda*g_EH
on r in [1+eps_bolt, R].  We use Step-65's full-4D linearized Ricci formulas (frame
components), finite-difference derivatives, and solve a linear least-squares problem.

Boundary penalties are intentionally modest and explicit:
  inner r=1+eps: f1=f3 and f1',f2',f3' small (smooth polar heuristic, not proof)
  outer r=R: quadratic growth f_i' ~ 2 f_i/R and relation c1-2c2-c3=Lambda/3.

This is NOT a Biquard/Fredholm proof and NOT ambient-H matched.  If it reduces the direct
operator defect, it gives a candidate profile to pass through the nonlinear audit and a concrete
next object for a proper Frobenius/ambient-matching solve.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix, vstack
from scipy.sparse.linalg import lsqr

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'step66_least_squares_h_profile.json'
PROFILE=ROOT/'data'/'step66_ls_h_profile.npz'
D=json.loads((ROOT/'data'/'step65_full4d_lichnerowicz.json').read_text())
Lam=1.0

# Parse frame expressions and extract algebraic coefficients.
r=sp.symbols('r')
f1=sp.Function('f1'); f2=sp.Function('f2'); f3=sp.Function('f3')
loc={'r':r,'Derivative':sp.Derivative,'f1':f1,'f2':f2,'f3':f3}
coord={k:sp.sympify(v,locals=loc) for k,v in D['dRic_at_point'].items()}
W=1-r**-4
frame_exprs={
 '00':sp.simplify(W*coord['00']),
 '11':sp.simplify(4*coord['11']/r**2),
 '33':sp.simplify(4*coord['33']/(r**2*W)),
}
a0,b0,c0,a1,b1,c1,a2,b2,c2=sp.symbols('a0 b0 c0 a1 b1 c1 a2 b2 c2')
vars_sym=[a0,b0,c0,a1,b1,c1,a2,b2,c2]
repl={f1(r):a0,f2(r):b0,f3(r):c0,sp.Derivative(f1(r),r):a1,sp.Derivative(f2(r),r):b1,sp.Derivative(f3(r),r):c1,sp.Derivative(f1(r),(r,2)):a2,sp.Derivative(f2(r),(r,2)):b2,sp.Derivative(f3(r),(r,2)):c2}
coeff_lams={}
const_lams={}
for key,expr in frame_exprs.items():
    e=sp.expand(expr.subs(repl))
    coeff_lams[key]=[sp.lambdify(r, sp.simplify(sp.diff(e,v)), 'numpy') for v in vars_sym]
    const_lams[key]=sp.lambdify(r, sp.simplify(e.subs({v:0 for v in vars_sym})), 'numpy')

# Grid and finite difference matrices.
N=180
r0=1.015
R=8.0
x=np.linspace(r0,R,N)
h=x[1]-x[0]
D1=np.zeros((N,N)); D2=np.zeros((N,N))
for i in range(1,N-1):
    D1[i,i-1]=-0.5/h; D1[i,i+1]=0.5/h
    D2[i,i-1]=1/h**2; D2[i,i]=-2/h**2; D2[i,i+1]=1/h**2
# one-sided boundaries
D1[0,0]=-3/(2*h); D1[0,1]=4/(2*h); D1[0,2]=-1/(2*h)
D1[-1,-1]=3/(2*h); D1[-1,-2]=-4/(2*h); D1[-1,-3]=1/(2*h)
D2[0,0]=1/h**2; D2[0,1]=-2/h**2; D2[0,2]=1/h**2
D2[-1,-1]=1/h**2; D2[-1,-2]=-2/h**2; D2[-1,-3]=1/h**2

def idx(comp,i): return comp*N+i  # comp 0=f1,1=f2,2=f3
rows=[]; rhs=[]; weights=[]
# Interior equations (avoid first/last few points for FD reliability)
for i in range(2,N-2):
    rv=x[i]
    for key in ['00','11','33']:
        row={}
        coeffs=[float(fn(rv)) for fn in coeff_lams[key]]
        # values f1,f2,f3
        for comp,coef in zip([0,1,2],coeffs[0:3]):
            row[idx(comp,i)]=row.get(idx(comp,i),0)+coef
        # first derivatives
        for comp,coef in zip([0,1,2],coeffs[3:6]):
            for j,c in enumerate(D1[i]):
                if c!=0: row[idx(comp,j)]=row.get(idx(comp,j),0)+coef*c
        # second derivatives
        for comp,coef in zip([0,1,2],coeffs[6:9]):
            for j,c in enumerate(D2[i]):
                if c!=0: row[idx(comp,j)]=row.get(idx(comp,j),0)+coef*c
        rows.append(row); rhs.append(Lam-float(const_lams[key](rv))); weights.append(1.0)

# Boundary penalties
def add_bc(entries, target, weight):
    rows.append(entries.copy()); rhs.append(target); weights.append(weight)
# inner smooth heuristic
wbc=20.0
add_bc({idx(0,0):1,idx(2,0):-1},0,wbc)              # f1=f3 at bolt edge
# derivatives small at inner edge
for comp in [0,1,2]:
    add_bc({idx(comp,j):D1[0,j] for j in range(3) if D1[0,j]!=0},0,5.0)
# outer quadratic growth f' - 2f/R =0
for comp in [0,1,2]:
    add_bc({idx(comp,j):D1[-1,j] for j in range(N-3,N) if D1[-1,j]!=0} | {idx(comp,N-1):-2/R},0,10.0)
# outer relation f1/R^2 -2 f2/R^2 - f3/R^2 = Lambda/3 (from Step65 asymptotic relation)
add_bc({idx(0,N-1):1/R**2, idx(1,N-1):-2/R**2, idx(2,N-1):-1/R**2}, Lam/3, 30.0)

M=lil_matrix((len(rows),3*N)); b=np.array(rhs,float); w=np.array(weights,float)
for ii,row in enumerate(rows):
    for j,c in row.items(): M[ii,j]=w[ii]*c
b=b*w
print('LS system',M.shape,'nnz',M.nnz)
sol=lsqr(M.tocsr(),b,atol=1e-10,btol=1e-10,iter_lim=20000)
y=sol[0]
print('lsqr istop',sol[1],'iters',sol[2],'resid',sol[3])
F1=y[0*N:1*N]; F2=y[1*N:2*N]; F3=y[2*N:3*N]
# Evaluate linear residual using formulas with FD derivatives.
def eval_linear(F1,F2,F3):
    F=[F1,F2,F3]; P=[D1@F1,D1@F2,D1@F3]; PP=[D2@F1,D2@F2,D2@F3]
    Rv=[]
    for i,rv in enumerate(x):
        vals=[F1[i],F2[i],F3[i],P[0][i],P[1][i],P[2][i],PP[0][i],PP[1][i],PP[2][i]]
        comps=[]
        for key in ['00','11','33']:
            comps.append(float(const_lams[key](rv))+sum(float(fn(rv))*val for fn,val in zip(coeff_lams[key],vals)))
        Rv.append(comps)
    return np.array(Rv)
Rlin=eval_linear(F1,F2,F3)
defect=np.max(np.abs(Rlin-Lam),axis=1)
interior=slice(4,N-4)
print('linear defect all/max/med',float(defect.max()),float(np.median(defect)))
print('linear defect interior max/med',float(defect[interior].max()),float(np.median(defect[interior])))
print('boundary f values',F1[0],F2[0],F3[0],F1[-1],F2[-1],F3[-1])

# Save profile and summary. Nonlinear audit in this script too (reuse Bianchi formulas by finite derivatives only approx).
np.savez(PROFILE,r=x,f1=F1,f2=F2,f3=F3,dRic_frame=Rlin,defect=defect)
OUT.write_text(json.dumps({
 'status':'ok',
 'profile_npz':str(PROFILE),
 'N':N,'r0':r0,'R':R,
 'lsqr':{'istop':int(sol[1]),'iters':int(sol[2]),'resid_norm':float(sol[3]),'cond_est':float(sol[6])},
 'linear_defect':{'max_all':float(defect.max()),'median_all':float(np.median(defect)),'max_interior':float(defect[interior].max()),'median_interior':float(np.median(defect[interior]))},
 'boundary_values':{'inner':[float(F1[0]),float(F2[0]),float(F3[0])],'outer':[float(F1[-1]),float(F2[-1]),float(F3[-1])]},
 'warning':'Finite-difference LS with heuristic boundary penalties; not a proof, not ambient-H matched, not a full nonlinear certificate.'
},indent=2))
print('Output',OUT)
