#!/usr/bin/env python3
"""Exact finite-dimensional checks for the mathematical continuation.

The SymPy assertions are rational/polynomial identities.  Optional --jets
computes ranks over two finite fields of the homogeneous highest-order
Darboux Ricci block.  These are finite-dimensional checks, not formal
integrability, convergence, Einstein existence or minimizer attainment.
"""
from __future__ import annotations
import argparse
import json
import math
import time
from pathlib import Path
import sympy as sp


def exact_checks() -> dict:
    a,b,c,d,e,f=sp.symbols('a b c d e f', real=True)
    J=sp.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    H=sp.Matrix([[a,b,c,d],[b,-a,d,-c],[c,d,e,f],[d,-c,f,-e]])
    xi=sp.Matrix([1,0,0,0])
    S=(xi*(H*xi).T+(H*xi)*xi.T-H)/2
    norm2=lambda M: sp.expand(sum(t*t for t in M))
    assert H*J+J*H==sp.zeros(4)
    assert sp.trace(H)==0
    assert S*xi-sp.trace(S)*xi/2==sp.zeros(4,1)
    assert sp.simplify((J*xi).dot(S*(J*xi))-sp.trace(S)/2)==0
    assert sp.simplify(norm2(S)+b*b/4-norm2(H)/8-(a*a+e*e+f*f)/4)==0
    parameters=[a,b,c,d,e,f]
    M=sp.Matrix([S[i,j] for i in range(4) for j in range(i,4)]).jacobian(parameters)
    assert M.rank()==5
    assert M.nullspace()==[sp.Matrix([0,1,0,0,0,0])]
    t,u,v,w,z=sp.symbols('t u v w z', real=True)
    K=sp.Matrix([[t,0,0,0],[0,t,u,v],[0,u,w,z],[0,v,z,-w]])
    substitutions={a:2*t,b:0,c:2*v,d:-2*u,e:-2*w,f:-2*z}
    assert sp.simplify(S.subs(substitutions)-K)==sp.zeros(4)
    A,x=sp.symbols('A x', positive=True)
    ell=A*(1-x*x)/3
    r=(2*A+6*ell-2*A*x)/9
    assert sp.factor(r-ell-ell**2/(A*(1+x)**2))==0
    assert sp.factor(A*A-2*A*r-(A-3*r+2*ell)**2)==0
    SS,Sh,T=sp.symbols('S Sh T')
    lhs=SS/12+Sh/6-8*sp.pi**2*T-8*sp.pi**2*(A-T)
    rhs=(SS-32*sp.pi**2*A)/12+(Sh-32*sp.pi**2*A)/6
    assert sp.simplify(lhs-rhs)==0
    N=sp.symbols('N',integer=True)
    C=lambda q:sp.expand(q*(q-1)*(q-2)/6)
    count=6*C(N+3)-10*C(N+1)+4*C(N)+C(N-1)-C(N+5)
    assert sp.expand(count)==N*N+8*N-5
    return {'exact_identities':'passed','ricci_symbol_rank':5,
            'hamiltonian_kernel_dimension':1,
            'gauge_coercivity_constant':'1/8',
            'squared_singular_values':['0','1/8','1/8','1/4','1/4','1/4'],
            'source_corrected_formal_count':'N^2+8N-5'}


def monomials(n:int):
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                yield (a,b,c,n-a-b-c)


def jet_matrix(n:int):
    """Integer matrix for 2 D Ric on compatible homogeneous degree-n tensors."""
    import numpy as np
    pairs=[(i,j) for i in range(4) for j in range(i,4)]
    source=list(monomials(n)); dest=list(monomials(n-2))
    row={(i,j,alpha):a*len(dest)+b for a,(i,j) in enumerate(pairs) for b,alpha in enumerate(dest)}
    letters=sp.symbols('a b c d e f')
    a,b,c,d,e,f=letters
    H=sp.Matrix([[a,b,c,d],[b,-a,d,-c],[c,d,e,f],[d,-c,f,-e]])
    basis=[H.diff(v) for v in letters]
    mat=np.zeros((10*len(dest),6*len(source)), dtype=np.int64)
    def deriv(alpha,i,j):
        al=list(alpha)
        coeff=al[i]; al[i]-=1
        if coeff==0:return None,0
        coeff*=al[j]; al[j]-=1
        if coeff==0:return None,0
        return tuple(al),coeff
    for r,B in enumerate(basis):
        for q,alpha in enumerate(source):
            col=r*len(source)+q
            for i,j in pairs:
                for z in range(4):
                    for val,k,l in [(int(B[j,z]),i,z),(int(B[i,z]),j,z),(-int(B[i,j]),z,z)]:
                        if val:
                            beta,coef=deriv(alpha,k,l)
                            if coef:mat[row[i,j,beta],col]+=val*coef
    return mat


def rank_mod(mat,p:int)->int:
    import numpy as np
    A=mat.copy()%p
    r=0
    for c in range(A.shape[1]):
        nz=np.flatnonzero(A[r:,c])
        if not len(nz):continue
        pivot=r+int(nz[0]); A[[r,pivot]]=A[[pivot,r]]
        A[r]=A[r]*pow(int(A[r,c]),-1,p)%p
        if r+1<A.shape[0]:
            coeff=A[r+1:,c].copy()
            A[r+1:]=(A[r+1:]-coeff[:,None]*A[r])%p
        r+=1
        if r==A.shape[0]:break
    return r


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--jets',type=int,default=0,help='check homogeneous degrees 2 through this degree')
    parser.add_argument('--out',type=Path,default=Path(__file__).with_name('exact_check_results.json'))
    args=parser.parse_args()
    report=exact_checks()
    if args.jets:
        results=[]
        for n in range(2,args.jets+1):
            start=time.time(); matrix=jet_matrix(n)
            ranks=[rank_mod(matrix,p) for p in [65521,65519]]
            gauge=math.comb(n+5,3)
            expected_free=n*n+8*n-5
            results.append({'degree':n,'shape':list(matrix.shape),'bytes':matrix.nbytes,
                            'primes':[65521,65519], 'ranks_mod_p':ranks,
                            'kernel_minus_hamiltonian_count':[matrix.shape[1]-r-gauge for r in ranks],
                            'source_expected_count':expected_free,
                            'seconds':round(time.time()-start,3)})
        report['homogeneous_jet_checks']=results
        report['rank_scope']='Finite-field ranks; no nonlinear prolongation or convergence assertion.'
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
