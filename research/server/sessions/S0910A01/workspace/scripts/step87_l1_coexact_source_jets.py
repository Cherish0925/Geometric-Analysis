#!/usr/bin/env python3
"""
Step 87: local source boundary projections for the complete l=1 coexact
one-form product family (*dX_a) ⊙ (*dX_b) at the NN node.

This extends the missed axial Killing-Killing mode to all three rotation-axis
Killing one-forms on each S^2 factor.  For X/Y axes the one-forms have nonzero
constant jets at NN, so their receiver contribution needs constant-frame and
background-curvature corrections; nevertheless their source boundary projection
against H^4 is computed from the exact V2 jet.
"""
import json, math, os
from fractions import Fraction
import sympy as sp
import numpy as np

# ---------------------------------------------------------------------------
# Polynomial utilities
# ---------------------------------------------------------------------------

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
    """Return M[p,q] with poly = sum M[p,q] vars[p]*vars[q] + lower/other.
    Uses p<=q storage; this is sufficient for the moment formula because it
    sums over all p,q as represented.
    """
    poly = sp.Poly(sp.expand(poly), *vars4)
    M = [[Fraction(0) for _ in range(4)] for __ in range(4)]
    for mon, coeff in poly.terms():
        if sum(mon) != 2:
            continue
        idx = []
        for k, e in enumerate(mon):
            idx += [k] * e
        if len(idx) == 1:  # x_i^2, exponent list produced length 2 actually
            idx = [idx[0], idx[0]]
        p, q = idx[0], idx[1]
        M[p][q] += Fraction(int(coeff.p), int(coeff.q)) if isinstance(coeff, sp.Rational) else Fraction(coeff)
    return M

# ---------------------------------------------------------------------------
# S^2 normal-coordinate Killing one-forms to degree 2
# ---------------------------------------------------------------------------

def sphere_killing_forms(prefix='A'):
    x, y = sp.symbols(f'{prefix}0 {prefix}1')
    vars2 = (x, y)
    r2 = x*x + y*y
    # metric inverse and sqrt(det g) to order 2 in geodesic normal coords
    ginv = sp.Matrix([[1 + r2/3 - x*x/3, -x*y/3],
                      [-x*y/3, 1 + r2/3 - y*y/3]])
    sqrtg = 1 - r2/6
    # Hodge star on covectors: *dx=dy, *dy=-dx for Euclidean leading term.
    star_mat = sqrtg * sp.Matrix([[-ginv[0,1], -ginv[1,1]],
                                  [ ginv[0,0],  ginv[0,1]]])
    # Height function expansions
    X = x - x*r2/6
    Y = y - y*r2/6
    Z = 1 - r2/2
    forms = {}
    for name, u in [('X', X), ('Y', Y), ('Z', Z)]:
        du = sp.Matrix([sp.diff(u, x), sp.diff(u, y)])
        alpha = star_mat * du
        alpha = [trunc(a, vars2, 2) for a in alpha]
        forms[name] = alpha
    return vars2, forms

# ---------------------------------------------------------------------------
# C matrices and boundary pairing from Step 87
# ---------------------------------------------------------------------------

def wedge(i, j):
    A = np.zeros((4,4), dtype=int)
    A[i,j] = 1; A[j,i] = -1
    return A


def build_C():
    e01 = wedge(0,1); e02 = wedge(0,2); e03 = wedge(0,3)
    e12 = wedge(1,2); e13 = wedge(1,3); e23 = wedge(2,3)
    rt2 = math.sqrt(2.0)
    wp = [(e01+e23)/rt2, (e02-e13)/rt2, (e03+e12)/rt2]
    wm = [(e01-e23)/rt2, (e02+e13)/rt2, (e03-e12)/rt2]
    C = np.zeros((3,3,4,4), dtype=int)
    for a in range(3):
        for b in range(3):
            prod = wp[a] @ wm[b]
            C[a,b] = np.rint(prod+prod.T).astype(int)
    return C


def moment_coeff(a,b,p,q):
    return Fraction((1 if a==b and p==q else 0) + (1 if a==p and b==q else 0) + (1 if a==q and b==p else 0), 12)


def boundary_coeff(C, M, chir):
    total = Fraction(0)
    for k in range(3):
        A = C[1,k] if chir == '+' else C[k,1]
        for a in range(4):
            for b in range(4):
                Aab = int(A[a,b])
                if not Aab: continue
                for i in range(4):
                    for j in range(4):
                        Aij = int(A[i,j])
                        if not Aij: continue
                        for p in range(4):
                            for q in range(4):
                                coeff = M[i][j][p][q]
                                if coeff:
                                    total += coeff * Aab * Aij * moment_coeff(a,b,p,q)
    return Fraction(-3,4)*total


def build_product_V2(formA, formB, varsA, varsB):
    a0,a1 = varsA; b0,b1 = varsB
    vars4 = (a0,a1,b0,b1)
    # components 0,1 from A one-form; components 2,3 from B one-form.
    alpha = [formA[0], formA[1], 0, 0]
    beta = [0, 0, formB[0], formB[1]]
    M = [[[[Fraction(0) for _ in range(4)] for __ in range(4)] for ___ in range(4)] for ____ in range(4)]
    V0_nonzero = False
    for i in range(4):
        for j in range(4):
            poly = sp.expand(alpha[i]*beta[j] + beta[i]*alpha[j])
            if sp.Poly(poly, *vars4).coeff_monomial(1) != 0:
                V0_nonzero = True
            mat = coeff_degree2_matrix(poly, vars4)
            for p in range(4):
                for q in range(4):
                    M[i][j][p][q] += mat[p][q]
    return M, V0_nonzero


def M_nonzero(M):
    out=[]
    for i in range(4):
        for j in range(4):
            for p in range(4):
                for q in range(4):
                    if M[i][j][p][q]:
                        out.append([i,j,p,q,str(M[i][j][p][q])])
    return out


def main():
    varsA, formsA = sphere_killing_forms('x')
    varsB, formsB = sphere_killing_forms('y')
    C = build_C()
    reports=[]
    for a_name in ['X','Y','Z']:
        for b_name in ['X','Y','Z']:
            M, V0_nonzero = build_product_V2(formsA[a_name], formsB[b_name], varsA, varsB)
            bp = boundary_coeff(C,M,'+')
            bm = boundary_coeff(C,M,'-')
            reports.append({
                'mode': f'star_d{a_name}_A_sym_star_d{b_name}_B',
                'V0_nonzero': V0_nonzero,
                'Bplus_over_pi2': f'{bp.numerator}/{bp.denominator}',
                'Bminus_over_pi2': f'{bm.numerator}/{bm.denominator}',
                'difference_over_pi2': f'{(bp-bm).numerator}/{(bp-bm).denominator}',
                'float_difference': float(bp-bm),
                'V2_nonzero_terms': M_nonzero(M),
            })
    results={
        'scope':'NN source boundary projections for complete l=1 coexact one-form product family',
        'method':'normal-coordinate S^2 expansions to degree 2 + exact S^3 quartic moment',
        'star_convention':'*dx=dy, *dy=-dx at Euclidean leading order, matching *dZ=x1 dx0-x0 dx1',
        'reports':reports,
        'caveat':'Modes with V0_nonzero need receiver constant-frame/background-curvature corrections before entering L_iG_P^perpS_j; source projections are still exact for their V2 jets in this convention.'
    }
    outpath=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'step87_l1_coexact_source_jets.json')
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath,'w') as f: json.dump(results,f,indent=2)
    print(json.dumps(results,indent=2))
    print(f'Wrote {outpath}')

if __name__=='__main__':
    main()
