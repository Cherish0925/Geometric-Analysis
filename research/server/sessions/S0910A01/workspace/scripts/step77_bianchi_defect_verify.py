"""Verify the quadratic Bianchi defect and its coordinate correction for the
S^2 x S^2 product normal-coordinate model used in Step 77.

Convention: B(h)_j = - partial_i h_ij + 1/2 partial_j tr(h), matching
B = delta + (1/2)d tr with delta the negative divergence.
"""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

OUT = Path("Sessions/S0910A01/workspace/data/step77_bianchi_defect_verify.json")
x0,x1,x2,x3 = sp.symbols('x0 x1 x2 x3')
xs=[x0,x1,x2,x3]


def metric_quad_block(indices, K=sp.Integer(1)):
    M=sp.zeros(4,4)
    a,b=indices
    r2=xs[a]**2+xs[b]**2
    for i in indices:
        for j in indices:
            delta=1 if i==j else 0
            M[i,j] = -K*sp.Rational(1,3)*(r2*delta - xs[i]*xs[j])
    return M

def lie_X(A):
    r2=sum(x*x for x in xs)
    dX=sp.zeros(4,4)
    for i in range(4):
        for k in range(4):
            dX[i,k]=sp.simplify(A*(2*xs[i]*xs[k]+r2*(1 if i==k else 0)))
    L=sp.zeros(4,4)
    for i in range(4):
        for j in range(4):
            L[i,j]=sp.simplify(dX[i,j]+dX[j,i])
    return L

def B(h):
    tr=sum(h[i,i] for i in range(4))
    comps=[]
    for j in range(4):
        div=sum(sp.diff(h[i,j], xs[i]) for i in range(4))
        comps.append(sp.simplify(-div + sp.Rational(1,2)*sp.diff(tr,xs[j])))
    return comps

def vec_str(v):
    return [str(sp.factor(e)) for e in v]

def main():
    H2=metric_quad_block([0,1])+metric_quad_block([2,3])
    Xcorr=lie_X(-sp.Rational(1,18))
    bH=B(H2)
    bX=B(Xcorr)
    btot=[sp.simplify(bH[i]+bX[i]) for i in range(4)]
    result={
        "step":77,
        "convention":"B_j=-partial_i h_ij + 1/2 partial_j tr h",
        "H2_product_normal_coordinates":"sum of the two constant-curvature S2 quadratic metric blocks, Lambda=1",
        "B_H2":vec_str(bH),
        "X":"X^a=-(1/18)r^2 x^a",
        "B_LX_e":vec_str(bX),
        "B_total":vec_str(btot),
        "cancels_exactly":all(e==0 for e in btot),
        "interpretation":"This verifies the TTCS correction that the raw product-normal quadratic tensor is not in Bianchi gauge and that the radial quadratic coordinate correction cancels its Bianchi defect."
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
    print(f"Wrote {OUT}")

if __name__=='__main__':
    main()
