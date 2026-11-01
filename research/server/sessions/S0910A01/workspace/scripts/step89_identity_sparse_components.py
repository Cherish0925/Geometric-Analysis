#!/usr/bin/env python3
"""Step 89: sparse coefficient form of the flat chirality-odd identity."""
from fractions import Fraction
from itertools import product
import json, math, pathlib
import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)

def wedge(i,j,n=4):
    A=np.zeros((n,n),dtype=int); A[i,j]=1; A[j,i]=-1; return A

def build_C():
    e01=wedge(0,1); e02=wedge(0,2); e03=wedge(0,3); e12=wedge(1,2); e13=wedge(1,3); e23=wedge(2,3)
    rt2=math.sqrt(2.0)
    wp=[(e01+e23)/rt2,(e02-e13)/rt2,(e03+e12)/rt2]
    wm=[(e01-e23)/rt2,(e02+e13)/rt2,(e03-e12)/rt2]
    C=np.zeros((3,3,4,4))
    for a,b in product(range(3),repeat=2):
        P=wp[a]@wm[b]; C[a,b]=P+P.T
    return np.rint(C).astype(int)

C=build_C()
D=np.zeros((4,4,4,4),dtype=int)
for k in range(3):
    D += np.einsum('ij,pq->ijpq', C[1,k], C[1,k]).astype(int)
    D -= np.einsum('ij,pq->ijpq', C[k,1], C[k,1]).astype(int)

wp_raw=[wedge(0,1)+wedge(2,3), wedge(0,2)-wedge(1,3), wedge(0,3)+wedge(1,2)]
wm_raw=[wedge(0,1)-wedge(2,3), wedge(0,2)+wedge(1,3), wedge(0,3)-wedge(1,2)]

def basis(ij,pq):
    i,j=ij; p,q=pq
    H=np.zeros((4,4,4,4),dtype=int)
    tps=[(i,j)] if i==j else [(i,j),(j,i)]
    dps=[(p,q)] if p==q else [(p,q),(q,p)]
    for a,b in tps:
        for c,d in dps:
            H[a,b,c,d]=1
    return H

def riemann(H):
    R=np.empty((4,4,4,4),dtype=object)
    for a,b,c,d in product(range(4),repeat=4):
        R[a,b,c,d]=Fraction(H[a,d,b,c]+H[b,c,a,d]-H[a,c,b,d]-H[b,d,a,c],2)
    return R

def block(R,A,B):
    s=Fraction(0,1)
    for i,j,k,l in product(range(4),repeat=4):
        if A[i,j] and B[k,l]:
            s += Fraction(int(A[i,j])*int(B[k,l]),1)*R[i,j,k,l]
    return s/Fraction(8,1)

def Rodd(H):
    R=riemann(H)
    return (block(R,wp_raw[1],wp_raw[1])-block(R,wm_raw[1],wm_raw[1]))/2

pairs=[(i,j) for i in range(4) for j in range(i,4)]
rows=[]
for ij in pairs:
    for pq in pairs:
        H=basis(ij,pq)
        DH=int(np.einsum('ijpq,ijpq->',D,H))
        R=Rodd(H)
        if DH or R:
            rows.append({'tensor_pair': ij, 'derivative_pair': pq, 'D_H_coeff': DH, 'R_odd_coeff': str(R), 'S_odd_over_pi2_coeff': str(Fraction(-DH,32))})

# Nonzero raw D entries too, useful for understanding orientation subspace.
D_entries=[]
for i,j,p,q in product(range(4),repeat=4):
    if D[i,j,p,q]:
        D_entries.append({'i':i,'j':j,'p':p,'q':q,'D':int(D[i,j,p,q])})

out={'independent_nonzero_coefficients':rows,'number_independent_nonzero':len(rows),'raw_D_nonzero_entries':D_entries,'number_raw_D_nonzero':len(D_entries)}
outpath=DATA_DIR/'step89_identity_sparse_components.json'
with open(outpath,'w') as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
print(f'Wrote {outpath}')
