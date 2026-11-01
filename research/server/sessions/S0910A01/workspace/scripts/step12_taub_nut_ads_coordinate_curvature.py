#!/usr/bin/env python3
"""
Step 12: coordinate-based curvature check for Taub--NUT--AdS.

Purpose.  Step 11 attempted a biaxial Bianchi IX curvature computation but missed
connection/structure-constant terms.  This script avoids those formulas.  It
computes Christoffel, Riemann, Ricci, scalar curvature, curvature-operator blocks,
Weyl eigenvalues, the calibrated defect density, and the Pontryagin density from
the coordinate metric

  g = dr^2/F + (r^2-nu^2)(dtheta^2+sin^2 theta dphi^2)
      + 4 nu^2 F (dpsi+cos theta dphi)^2,
  F=(r-nu)/(r+nu)*(1+(r-nu)(r+3nu)/3),

which has Ric=-g for ell^2=3.  All evaluation is at theta=pi/2; because the
metric is U(2)-symmetric this loses no radial information and simplifies the
orthonormal-frame transform.

The sign/operator convention is selected by internal consistency: Ric should be
-g, scalar should be -4, and tr(curvature operator on Lambda^2) should be s/2.
"""
from __future__ import annotations

import argparse
import math
from functools import lru_cache
import numpy as np
import sympy as sp


@lru_cache(maxsize=1)
def make_metric_lambdas():
    nu, rr, th = sp.symbols('nu rr th', positive=True, real=True)
    F = ((rr - nu)/(rr + nu)) * (1 + ((rr - nu)*(rr + 3*nu))/sp.Integer(3))
    h = rr**2 - nu**2
    q = 4*nu**2*F
    s = sp.sin(th)
    c = sp.cos(th)

    g = sp.MutableDenseMatrix.zeros(4, 4)
    g[0, 0] = 1/F
    g[1, 1] = h
    g[2, 2] = h*s**2 + q*c**2
    g[2, 3] = q*c
    g[3, 2] = q*c
    g[3, 3] = q

    coords = [rr, th, sp.symbols('ph'), sp.symbols('ps')]
    # The metric has no ph/ps dependence, but keeping four derivative slots makes
    # the numerical tensor code transparent.
    dg = [[ [sp.diff(g[i, j], coords[a]) for j in range(4)] for i in range(4)] for a in range(4)]
    d2g = [[[[sp.diff(g[i, j], coords[a], coords[b]) for j in range(4)] for i in range(4)] for b in range(4)] for a in range(4)]

    flat_g = [g[i, j] for i in range(4) for j in range(4)]
    flat_dg = [dg[a][i][j] for a in range(4) for i in range(4) for j in range(4)]
    flat_d2g = [d2g[a][b][i][j] for a in range(4) for b in range(4) for i in range(4) for j in range(4)]
    vars_ = (nu, rr, th)
    return (
        sp.lambdify(vars_, flat_g, 'numpy'),
        sp.lambdify(vars_, flat_dg, 'numpy'),
        sp.lambdify(vars_, flat_d2g, 'numpy'),
        sp.simplify(F),
    )


def metric_derivatives(nu_val: float, r_val: float, theta_val: float = math.pi/2):
    fg, fdg, fd2g, _ = make_metric_lambdas()
    g = np.array(fg(nu_val, r_val, theta_val), dtype=float).reshape(4, 4)
    dg = np.array(fdg(nu_val, r_val, theta_val), dtype=float).reshape(4, 4, 4)
    d2g = np.array(fd2g(nu_val, r_val, theta_val), dtype=float).reshape(4, 4, 4, 4)
    return g, dg, d2g


def curvature_tensors(nu_val: float, r_val: float, theta_val: float = math.pi/2):
    """Return numerical tensors in the convention R^l_{i j k}=R(dx_j,dx_k)dx_i.

    Ric_{ik}=sum_j R^j_{i j k}.  With this convention the present metric has
    Ric=-g.  The covariant tensor used below is R_abcd=<R(e_a,e_b)e_c,e_d> after
    transforming to an orthonormal frame.
    """
    g, dg, d2g = metric_derivatives(nu_val, r_val, theta_val)
    invg = np.linalg.inv(g)

    # Gamma[l,i,j]
    Gamma = np.zeros((4, 4, 4), dtype=float)
    for l in range(4):
        for i in range(4):
            for j in range(4):
                val = 0.0
                for m in range(4):
                    val += invg[l, m]*(dg[i, j, m] + dg[j, i, m] - dg[m, i, j])
                Gamma[l, i, j] = 0.5*val

    # derivative of inverse metric: dinvg[k,l,m] = partial_k g^{lm}
    dinvg = np.zeros((4, 4, 4), dtype=float)
    for k in range(4):
        dinvg[k] = -invg @ dg[k] @ invg

    # dGamma[k,l,i,j] = partial_k Gamma^l_{ij}
    dGamma = np.zeros((4, 4, 4, 4), dtype=float)
    for k in range(4):
        for l in range(4):
            for i in range(4):
                for j in range(4):
                    val = 0.0
                    for m in range(4):
                        A = dg[i, j, m] + dg[j, i, m] - dg[m, i, j]
                        dA = d2g[k, i, j, m] + d2g[k, j, i, m] - d2g[k, m, i, j]
                        val += dinvg[k, l, m]*A + invg[l, m]*dA
                    dGamma[k, l, i, j] = 0.5*val

    # R^l_{i j k} = partial_j Gamma^l_{ik} - partial_k Gamma^l_{ij}
    #                + Gamma^l_{jm} Gamma^m_{ik} - Gamma^l_{km} Gamma^m_{ij}
    R = np.zeros((4, 4, 4, 4), dtype=float)
    for l in range(4):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    val = dGamma[j, l, i, k] - dGamma[k, l, i, j]
                    for m in range(4):
                        val += Gamma[l, j, m]*Gamma[m, i, k] - Gamma[l, k, m]*Gamma[m, i, j]
                    R[l, i, j, k] = val

    Ric = np.zeros((4, 4), dtype=float)
    for i in range(4):
        for k in range(4):
            Ric[i, k] = sum(R[j, i, j, k] for j in range(4))
    scalar = float(np.einsum('ik,ik->', invg, Ric))

    # Coordinate covariant tensor with convention Rcov[a,b,c,d]=<R(da,db)dc,dd>
    # = g_{dm} R^m_{c a b}.
    Rcov_coord = np.zeros((4, 4, 4, 4), dtype=float)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    Rcov_coord[a, b, c, d] = sum(g[d, m]*R[m, c, a, b] for m in range(4))

    # Orthonormal frame at theta=pi/2: E_i^coord coefficients.
    Fval = 1.0/g[0, 0]
    hval = g[1, 1]
    qval = g[3, 3]
    # At theta=pi/2, g is diagonal; assert near-diagonal.
    E = np.zeros((4, 4), dtype=float)
    E[0, 0] = math.sqrt(Fval)
    E[1, 1] = 1.0/math.sqrt(hval)
    E[2, 2] = 1.0/math.sqrt(g[2, 2])
    E[3, 3] = 1.0/math.sqrt(qval)
    Rcov_on = np.einsum('abcd,ia,jb,kc,ld->ijkl', Rcov_coord, E, E, E, E)

    # Orthonormal Ricci by frame transform.
    Ric_on = E @ Ric @ E.T
    return {
        'g': g,
        'invg': invg,
        'Gamma': Gamma,
        'R_mixed': R,
        'Ric_coord': Ric,
        'Ric_on': Ric_on,
        'scalar': scalar,
        'Rcov_on': Rcov_on,
        'F_metric': Fval,
        'h_metric': hval,
        'q_metric': qval,
    }


# oriented 2-form basis: e01,e02,e03,e23,e31,e12, compatible with star e01=e23,
# star e02=e31, star e03=e12.
PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]


def curvature_operator_from_R(Rcov_on: np.ndarray):
    """Build the curvature operator matrix on Lambda^2.

    With the R_abcd=<R(e_a,e_b)e_c,e_d> convention, sectional curvature is
    K(e_i,e_j)=R_{i j j i}.  Therefore the operator entry on e_i^e_j and
    e_k^e_l is R_{i j l k}.  This choice makes tr(Rop)=scalar/2 in the checks.
    """
    M = np.zeros((6, 6), dtype=float)
    for A, (i, j) in enumerate(PAIRS):
        for B, (k, l) in enumerate(PAIRS):
            M[A, B] = Rcov_on[i, j, l, k]
    # Symmetrize tiny numerical asymmetry.
    return 0.5*(M + M.T)


def decompose_blocks(Rop: np.ndarray, scalar: float):
    rt2 = math.sqrt(2.0)
    Tplus = np.zeros((6, 3), dtype=float)
    Tminus = np.zeros((6, 3), dtype=float)
    # plus: (b0+b3)/sqrt2, (b1+b4)/sqrt2, (b2+b5)/sqrt2
    for a in range(3):
        Tplus[a, a] = 1/rt2
        Tplus[a+3, a] = 1/rt2
        Tminus[a, a] = 1/rt2
        Tminus[a+3, a] = -1/rt2
    Rplus = Tplus.T @ Rop @ Tplus
    Rminus = Tminus.T @ Rop @ Tminus
    B = Tplus.T @ Rop @ Tminus
    Wplus = Rplus - (scalar/12.0)*np.eye(3)
    Wminus = Rminus - (scalar/12.0)*np.eye(3)
    return Rplus, Rminus, B, Wplus, Wminus


def defect_from_wplus(eigs: np.ndarray, scalar: float, E_norm2: float = 0.0):
    u2 = float(np.sum(eigs**2))
    u = math.sqrt(max(u2, 0.0))
    w = float(np.min(eigs))
    f = (2.0/3.0)*scalar - 2.0*math.sqrt(2.0/3.0)*u
    a = (2.0/3.0)*scalar + 2.0*w
    a_minus = min(a, 0.0)
    G = f*f - a_minus*a_minus
    CS = (scalar + 8.0*math.sqrt(6.0)*u)**2
    Fcal = E_norm2 + CS + G
    P = 2.0*u2 + scalar*scalar/24.0 - 0.5*E_norm2
    return {'u2': u2, 'u': u, 'w': w, 'CS': CS, 'G': G, 'Fcal': Fcal, 'P': P}


def evaluate(nu_val: float, r_val: float, theta_val: float = math.pi/2, verbose: bool = True):
    out = curvature_tensors(nu_val, r_val, theta_val)
    Ric_on = out['Ric_on']
    scalar = out['scalar']
    Rop = curvature_operator_from_R(out['Rcov_on'])
    Rplus, Rminus, B, Wplus, Wminus = decompose_blocks(Rop, scalar)
    evalp = np.linalg.eigvalsh(0.5*(Wplus+Wplus.T))
    evalm = np.linalg.eigvalsh(0.5*(Wminus+Wminus.T))
    E_on = Ric_on - (scalar/4.0)*np.eye(4)
    E_norm2 = float(np.sum(E_on*E_on))
    dplus = defect_from_wplus(evalp, scalar, E_norm2)
    dminus_as_plus = defect_from_wplus(evalm, scalar, E_norm2)
    if verbose:
        print(f"nu={nu_val:g}, r={r_val:g}, theta={theta_val:g}")
        print(f"F_metric={out['F_metric']:.12g}, h={out['h_metric']:.12g}, q=4nu^2F={out['q_metric']:.12g}")
        print("Ricci in ON frame (should be -I):")
        print(np.array2string(Ric_on, precision=8, suppress_small=True))
        print(f"scalar={scalar:.12g} (should be -4)")
        print(f"trace curvature op={np.trace(Rop):.12g}, scalar/2={scalar/2:.12g}")
        print(f"offdiag Einstein block ||B||_F={np.linalg.norm(B):.3e}, E_norm2={E_norm2:.3e}")
        print("W+ matrix/eigenvalues in coordinate orientation:")
        print(np.array2string(Wplus, precision=8, suppress_small=True))
        print(evalp)
        print("W- matrix/eigenvalues:")
        print(np.array2string(Wminus, precision=8, suppress_small=True))
        print(evalm)
        print("defect using W+:", {k: round(v, 12) for k, v in dplus.items()})
        print("defect using W- as plus (opposite orientation):", {k: round(v, 12) for k, v in dminus_as_plus.items()})
    return {
        **out,
        'Rop': Rop,
        'Rplus': Rplus,
        'Rminus': Rminus,
        'B': B,
        'Wplus': Wplus,
        'Wminus': Wminus,
        'eig_Wplus': evalp,
        'eig_Wminus': evalm,
        'E_norm2': E_norm2,
        'defect_Wplus': dplus,
        'defect_Wminus_as_plus': dminus_as_plus,
    }


def sample_table():
    # Fixed annular radii away from the NUT.  For small nu, the proper distance
    # from the NUT is close to sqrt(3) asinh(r/sqrt(3)).
    nus = [0.2, 0.1, 0.05, 0.02, 0.01]
    radii = [0.35, 0.5, 0.75, 1.0, 1.5]
    rows = []
    for nv in nus:
        for rv in radii:
            if rv <= nv:
                continue
            res = evaluate(nv, rv, verbose=False)
            d = res['defect_Wplus']
            dm = res['defect_Wminus_as_plus']
            rows.append((nv, rv, res['scalar'], np.max(np.abs(res['Ric_on']+np.eye(4))),
                         d['u2'], d['Fcal'], d['P'], dm['u2'], dm['Fcal'], dm['P']))
    print("\nSample table at theta=pi/2")
    print("nu       r        scalar    RicErr      |W+|^2    Fcal+      P+        |W-|^2    Fcal-      P-")
    for row in rows:
        print(f"{row[0]:<8.3g} {row[1]:<8.3g} {row[2]:<9.5g} {row[3]:<10.2e} {row[4]:<10.5g} {row[5]:<10.5g} {row[6]:<10.5g} {row[7]:<10.5g} {row[8]:<10.5g} {row[9]:<10.5g}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nu', type=float, default=0.01)
    parser.add_argument('--r', type=float, default=0.5)
    parser.add_argument('--theta', type=float, default=math.pi/2)
    parser.add_argument('--table', action='store_true')
    args = parser.parse_args()
    evaluate(args.nu, args.r, args.theta, verbose=True)
    if args.table:
        sample_table()


if __name__ == '__main__':
    main()
