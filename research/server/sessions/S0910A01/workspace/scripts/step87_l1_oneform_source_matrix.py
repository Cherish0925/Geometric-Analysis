#!/usr/bin/env python3
"""
Step 87: exact NN source boundary projections for the full l=1 one-form
product P-eigenspace before gauge reduction.

Each factor S^2 has six l=1 one-forms: exact dX,dY,dZ and coexact *dX,*dY,*dZ.
For any pair eta_A, theta_B with rough eigenvalue 1, the mixed tensor
eta_A ⊙ theta_B has product-operator eigenvalue P=1 because the product
curvature has no mixed AB action.  The simultaneous pi-rotation quotient keeps
pairs with equal vertical-axis parity: X/Y are odd, Z is even.

This script computes only the source boundary coefficient
B_eps(V2)=3∫_{S^3/Z2}<H^4_eps,V2>dσ at the NN node.  Modes with nonzero V0
still require receiver constant-frame/background-curvature corrections.
"""
import json, math, os
from fractions import Fraction
import sympy as sp
import numpy as np


def trunc(poly, vars, maxdeg=2):
    poly = sp.Poly(sp.expand(poly), *vars)
    out = 0
    for mon, coeff in poly.terms():
        if sum(mon) <= maxdeg:
            term = coeff
            for v, e in zip(vars, mon):
                term *= v**e
            out += term
    return sp.expand(out)


def coeff_degree2_matrix(poly, vars4):
    poly = sp.Poly(sp.expand(poly), *vars4)
    M = [[Fraction(0) for _ in range(4)] for __ in range(4)]
    for mon, coeff in poly.terms():
        if sum(mon) != 2:
            continue
        inds=[]
        for k,e in enumerate(mon):
            inds += [k]*e
        p,q = inds[0], inds[1]
        if isinstance(coeff, sp.Rational):
            cf=Fraction(int(coeff.p), int(coeff.q))
        else:
            cf=Fraction(coeff)
        M[p][q] += cf
    return M


def sphere_forms(prefix):
    x,y=sp.symbols(f'{prefix}0 {prefix}1')
    vars2=(x,y); r2=x*x+y*y
    X=x-x*r2/6
    Y=y-y*r2/6
    Z=1-r2/2
    # metric inverse and sqrt(det) in geodesic normal coordinates to O(r^2)
    ginv=sp.Matrix([[1+r2/3-x*x/3, -x*y/3],[-x*y/3,1+r2/3-y*y/3]])
    sqrtg=1-r2/6
    star_mat=sqrtg*sp.Matrix([[-ginv[0,1],-ginv[1,1]],[ginv[0,0],ginv[0,1]]])
    forms={}
    for name,u,parity in [('X',X,-1),('Y',Y,-1),('Z',Z,+1)]:
        du=sp.Matrix([sp.diff(u,x), sp.diff(u,y)])
        sd=star_mat*du
        forms[f'd{name}']={'components':[trunc(du[0],vars2,2),trunc(du[1],vars2,2)],'axis':name,'parity':parity,'coexact':False}
        forms[f's{name}']={'components':[trunc(sd[0],vars2,2),trunc(sd[1],vars2,2)],'axis':name,'parity':parity,'coexact':True}
    return vars2,forms


def wedge(i,j):
    A=np.zeros((4,4),dtype=int); A[i,j]=1; A[j,i]=-1; return A

def build_C():
    e01=wedge(0,1); e02=wedge(0,2); e03=wedge(0,3); e12=wedge(1,2); e13=wedge(1,3); e23=wedge(2,3)
    rt2=math.sqrt(2.0)
    wp=[(e01+e23)/rt2,(e02-e13)/rt2,(e03+e12)/rt2]
    wm=[(e01-e23)/rt2,(e02+e13)/rt2,(e03-e12)/rt2]
    C=np.zeros((3,3,4,4),dtype=int)
    for a in range(3):
        for b in range(3):
            C[a,b]=np.rint(wp[a]@wm[b]+(wp[a]@wm[b]).T).astype(int)
    return C


def moment(a,b,p,q):
    return Fraction((a==b and p==q)+(a==p and b==q)+(a==q and b==p),12)


def boundary(C,M,chir):
    total=Fraction(0)
    for k in range(3):
        A=C[1,k] if chir=='+' else C[k,1]
        for a in range(4):
            for b in range(4):
                Aab=int(A[a,b])
                if not Aab: continue
                for i in range(4):
                    for j in range(4):
                        Aij=int(A[i,j])
                        if not Aij: continue
                        for p in range(4):
                            for q in range(4):
                                coeff=M[i][j][p][q]
                                if coeff:
                                    total += coeff*Aab*Aij*moment(a,b,p,q)
    return Fraction(-3,4)*total


def build_M(formA,formB,varsA,varsB):
    a0,a1=varsA; b0,b1=varsB; vars4=(a0,a1,b0,b1)
    alpha=[formA['components'][0],formA['components'][1],0,0]
    beta=[0,0,formB['components'][0],formB['components'][1]]
    M=[[[[Fraction(0) for _ in range(4)] for __ in range(4)] for ___ in range(4)] for ____ in range(4)]
    V0=False
    V1=False
    for i in range(4):
        for j in range(4):
            poly=sp.expand(alpha[i]*beta[j]+beta[i]*alpha[j])
            P=sp.Poly(poly,*vars4)
            for mon,coeff in P.terms():
                if sum(mon)==0 and coeff!=0: V0=True
                if sum(mon)==1 and coeff!=0: V1=True
            mat=coeff_degree2_matrix(poly,vars4)
            for p in range(4):
                for q in range(4): M[i][j][p][q]+=mat[p][q]
    return M,V0,V1


def main():
    varsA,FA=sphere_forms('x'); varsB,FB=sphere_forms('y'); C=build_C()
    all_reports=[]; allowed=[]
    for nameA,formA in FA.items():
        for nameB,formB in FB.items():
            M,V0,V1=build_M(formA,formB,varsA,varsB)
            bp=boundary(C,M,'+'); bm=boundary(C,M,'-'); diff=bp-bm
            descends=(formA['parity']*formB['parity']==1)
            TT=(formA['coexact'] and formB['coexact'])
            rec={
                'mode':f'{nameA}_A_sym_{nameB}_B',
                'descends_under_simultaneous_pi_rotation':descends,
                'TT_if_both_coexact':TT,
                'V0_nonzero':V0,
                'V1_nonzero':V1,
                'Bplus_over_pi2':f'{bp.numerator}/{bp.denominator}',
                'Bminus_over_pi2':f'{bm.numerator}/{bm.denominator}',
                'difference_over_pi2':f'{diff.numerator}/{diff.denominator}',
                'float_difference':float(diff)
            }
            all_reports.append(rec)
            if descends and (bp or bm): allowed.append(rec)
    results={
        'scope':'full l=1 one-form product NN source projections, before gauge reduction',
        'P_eigenvalue':'1 for every listed mixed one-form product in the product operator convention',
        'source_projection':'B_eps(V2)=3 int_{S3/Z2}<H4_eps,V2>; rational multiples of pi^2',
        'quotient_rule':'global simultaneous pi-rotation keeps pairs with equal axis parity: X/Y odd, Z even',
        'reports':all_reports,
        'nonzero_quotient_descending_source_modes':allowed,
        'interpretation':'Within the quotient-descending l=1 mixed one-form products, nonzero source projections occur in several modes, but among the TT/coexact and V0=0 modes the axial sZ_A_sym_sZ_B channel is the clean chirality-sensitive unit test. V0-nonzero modes require receiver frame/background corrections before spectral summation.'
    }
    outpath=os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','step87_l1_oneform_source_matrix.json')
    os.makedirs(os.path.dirname(outpath),exist_ok=True)
    with open(outpath,'w') as f: json.dump(results,f,indent=2)
    print(json.dumps(results,indent=2))
    print(f'Wrote {outpath}')

if __name__=='__main__': main()
