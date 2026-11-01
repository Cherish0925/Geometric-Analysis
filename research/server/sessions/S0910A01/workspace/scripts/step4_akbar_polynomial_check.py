"""
Direct check of Akbar gr-qc/0301007 displayed seventh-degree polynomial
for Taub--Bolt--AdS boundary data.

This probes an apparent convention/formula tension: the direct parametric sampler
using the regular bolt formulas and boundary radii suggests only b/a<~0.397 for
p=1, Lambda=-1, while the paper states that even round S^3 boundaries have bolt
fillings.  Here we solve the displayed polynomial g(p)=0 for selected dimensionless
A=a^2 lambda, B=b^2 lambda and test the unsquared equations for both M branches.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)
P_MAX = (2.0 - math.sqrt(3.0)) / 4.0


def coeffs(A: float, B: float):
    a7 = 8192*A*(-6*A*B+4*A**3+6*A**2-1)*(2*A**2+3*A-3*B)
    a6 = -128*(216*A**3-3456*B*A**3+2304*A**5-27+128*A**7-288*B*A**2-1152*B*A**4+36*A**2-36*B*A-1152*A**3*B**2+1840*A**4+576*B*A**5+1728*A**2*B**2+960*A**6)
    a5 = 4*(13824*A**6+20736*A**2*B**2+1728*A**3-4320*B*A+4320*A**2+27648*B*A**4+81+3072*A**7+1728*A+256*A**8+41472*B*A**5+1728*B*A**2+28160*A**5+9216*B*A**6+20448*A**4-55296*A**3*B**2-39168*B*A**3)
    a4 = -8*A*(3240*A*B+10368*A**4*B-1440*A**3-81+5184*A**3*B**2+10752*A**3*B+72*A**2*B-2176*A**2-240*A**4-144*A*B**2-10368*A**2*B**2+3456*A**4*B**2+3456*A**5*B+24*B-1728*A**2*B**3-456*A+384*A**6*B)
    a3 = 4*A*(-72*A*B+1728*A**3*B**3+24*A**2-720*A**3*B+864*A**5*B**2+288*A**2*B**2-2160*A**2*B+5184*A**4*B**2+7776*A**3*B**2+270*A*B**2+36*B-2592*A**2*B**3+45*A+28*A**3)
    a2 = -8*A**2*(-27*B+648*A**2*B**3+9*A*B-135*A*B**2+216*A**3*B**3+2*A**3+18*A+12*A**2)
    a1 = 3*A**2*B*(108*A**2*B**3+24*A+8*A**2-3*B)
    a0 = -9*A**3*B**2
    return [a7,a6,a5,a4,a3,a2,a1,a0]


def rb_roots(L):
    disc = 1+16*L**4-16*L**2
    sd = math.sqrt(max(0,disc))
    return [(1-sd)/(4*L), (1+sd)/(4*L)]


def M_from_rb(L,rb):
    return (3*rb**2 + rb**4 + 3*L**2 - 3*L**4 - 6*L**2*rb**2)/(6*rb)


def delta_boundary(rho,L,M):
    return rho**2 - 2*M*rho + L**2 - (L**4 + 2*L**2*rho**2 - rho**4/3)


def test_case(A,B):
    roots = np.roots(coeffs(A,B))
    good=[]
    for z in roots:
        if abs(z.imag)<1e-8 and 0<z.real<=P_MAX*(1+1e-8):
            p=float(z.real); L=math.sqrt(p); rho=math.sqrt(A + L*L)
            branch_info=[]
            for rb in rb_roots(L):
                M=M_from_rb(L,rb)
                D=delta_boundary(rho,L,M)
                residual = B*(rho**2-L**2) - 4*L**2*D
                branch_info.append({"rb":rb,"M":M,"Delta_boundary":D,"eq35_residual":residual,"positive_metric":D>0,"rho_gt_rb":rho>rb})
            good.append({"p":p,"L":L,"rho_from_A":rho,"branches":branch_info})
    return good


def main():
    cases=[(1,1),(0.1,0.1),(10,10),(1,0.01),(1,0.1),(1,0.5),(1,2),(1,10)]
    out={"P_MAX":P_MAX,"cases":{}}
    for A,B in cases:
        good=test_case(A,B)
        out[repr((A,B))]=good
        out["cases"][f"A={A},B={B}"]=good
        print(f"A={A}, B={B}: {len(good)} roots in allowed interval")
        for item in good:
            print(f"  p={item['p']:.12g}, L={item['L']:.6g}, rho={item['rho_from_A']:.6g}")
            for j,b in enumerate(item['branches']):
                print(f"    branch{j}: rb={b['rb']:.6g}, D={b['Delta_boundary']:.6g}, residual={b['eq35_residual']:.3g}, D>0={b['positive_metric']}, rho>rb={b['rho_gt_rb']}")
    path=DATA/"step4_akbar_polynomial_check.json"
    path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(f"wrote {path}")

if __name__=='__main__':
    main()
