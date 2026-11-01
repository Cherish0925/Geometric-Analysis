#!/usr/bin/env python3
"""
Step 87: receiver-side linearized curvature for the missed Killing-one-form
product eigentensor.

For a smooth perturbation h_ij(x)=M_ijpq x_p x_q with h(0)=dh(0)=0,
the first variation of the curvature operator at the receiver node is determined
by the second jet.  This script computes the flat linearized curvature blocks
on self-dual and anti-self-dual 2-forms for the four linear-linear AB modes
(grad/kill on the two S^2 factors).  It is the local receiver part that Step 86
had not computed.

Sign conventions are reported explicitly.  Overall sign may differ from Ozuch's
Riemann convention; nonzero channels and chirality contrasts are convention-
invariant up to the common convention sign.
"""
import json, math, os
import numpy as np


def wedge(i, j, n=4):
    A = np.zeros((n, n))
    A[i, j] = 1.0
    A[j, i] = -1.0
    return A


def build_sd_asd_bases():
    e01 = wedge(0, 1); e02 = wedge(0, 2); e03 = wedge(0, 3)
    e12 = wedge(1, 2); e13 = wedge(1, 3); e23 = wedge(2, 3)
    rt2 = math.sqrt(2.0)
    wp = [(e01 + e23)/rt2, (e02 - e13)/rt2, (e03 + e12)/rt2]
    wm = [(e01 - e23)/rt2, (e02 + e13)/rt2, (e03 - e12)/rt2]
    return wp, wm


def oneform_linear(kind, factor):
    A = np.zeros((4, 4))
    if factor == 'A':
        i0, i1 = 0, 1
    else:
        i0, i1 = 2, 3
    if kind == 'grad':
        A[i0, i0] = -1
        A[i1, i1] = -1
    elif kind == 'kill':
        A[i0, i1] = 1
        A[i1, i0] = -1
    else:
        raise ValueError(kind)
    return A


def sym_product_quadratic(A, B):
    M = np.zeros((4, 4, 4, 4))
    for i in range(4):
        for j in range(4):
            for p in range(4):
                for q in range(4):
                    M[i, j, p, q] += A[i, p] * B[j, q] + B[i, p] * A[j, q]
    return M


def second_derivatives(M):
    """H[i,j,a,b]=∂_a∂_b h_ij(0)."""
    return M + M.transpose(0, 1, 3, 2)


def linearized_riemann(H):
    """Return dR[i,j,k,l] = δR_{ij k l} in convention
    δR_{ij k l}=1/2(h_{i l,j k}+h_{j k,i l}-h_{i k,j l}-h_{j l,i k}).
    """
    R = np.zeros((4, 4, 4, 4))
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    R[i, j, k, l] = 0.5 * (H[i, l, j, k] + H[j, k, i, l]
                                           - H[i, k, j, l] - H[j, l, i, k])
    return R


def curvature_block(R, basis_left, basis_right):
    """Operator block entries <basis_a, R basis_b> using 2-form inner product.
    With basis matrices normalized by (1/2)sum A_ij^2=1, the coefficient is
    (1/4) sum A_ij R_ij kl B_kl.
    """
    B = np.zeros((len(basis_left), len(basis_right)))
    for a, A in enumerate(basis_left):
        for b, C in enumerate(basis_right):
            B[a, b] = 0.25 * np.einsum('ij,ijkl,kl->', A, R, C)
    return B


def mode_curvature(Akind, Bkind):
    A = oneform_linear(Akind, 'A')
    B = oneform_linear(Bkind, 'B')
    M = sym_product_quadratic(A, B)
    H = second_derivatives(M)
    R = linearized_riemann(H)
    wp, wm = build_sd_asd_bases()
    Rpp = curvature_block(R, wp, wp)
    Rmm = curvature_block(R, wm, wm)
    Rpm = curvature_block(R, wp, wm)
    Ric = np.zeros((4, 4))
    # Ric_{jl}=R_{i j i l}; sign convention follows the above R formula.
    for j in range(4):
        for l in range(4):
            Ric[j, l] = sum(R[i, j, i, l] for i in range(4))
    Scal = np.trace(Ric)
    return M, Rpp, Rmm, Rpm, Ric, Scal


def mat_to_list(A):
    return [[float(x) for x in row] for row in A]


def main():
    reports = []
    for Ak in ['grad', 'kill']:
        for Bk in ['grad', 'kill']:
            M, Rpp, Rmm, Rpm, Ric, Scal = mode_curvature(Ak, Bk)
            reports.append({
                'name': f'{Ak}A_{Bk}B',
                'delta_R_plus_block': mat_to_list(Rpp),
                'delta_R_minus_block': mat_to_list(Rmm),
                'delta_R_plus_zeta2_column_index1': [float(x) for x in Rpp[:, 1]],
                'delta_R_minus_zeta2_column_index1': [float(x) for x in Rmm[:, 1]],
                'radial_component_delta_Rpp_22_index1_1': float(Rpp[1, 1]),
                'radial_component_delta_Rmm_22_index1_1': float(Rmm[1, 1]),
                'mixed_plus_minus_block': mat_to_list(Rpm),
                'linearized_Ricci': mat_to_list(Ric),
                'linearized_scalar': float(Scal),
            })
    kk = [r for r in reports if r['name'] == 'killA_killB'][0]
    results = {
        'scope': 'linearized receiver curvature from full quadratic jet of linear-linear AB eigentensors',
        'riemann_convention': 'δR_ijkl=1/2(h_il,jk+h_jk,il-h_ik,jl-h_jl,ik); 2-form block=<ω_a,Rω_b> with 1/4 contraction',
        'receiver_zeta': 'zeta=omega_2 (0-based index 1); lambda variation components are entries of delta_R^± column 1 up to Ozuch normalization and possible sign convention',
        'reports': reports,
        'missed_mode_summary': {
            'name': 'killA_killB',
            'P_eigenvalue': 1.0,
            'delta_R_plus_column_for_zeta2': kk['delta_R_plus_zeta2_column_index1'],
            'delta_R_minus_column_for_zeta2': kk['delta_R_minus_zeta2_column_index1'],
            'radial_plus': kk['radial_component_delta_Rpp_22_index1_1'],
            'radial_minus': kk['radial_component_delta_Rmm_22_index1_1'],
            'interpretation': 'The missed mode has nonzero receiver curvature in the zeta=omega_2 channel. For a plus receiver its radial component is nonzero in this convention, so together with the nonzero source projection it gives a nonzero single-eigenmode contribution to the provisional source-to-receiver spectral response.'
        },
        'caution': 'This still lacks L2 normalization, node transport signs, and the constant-jet/frame terms for modes with V0 != 0. It is an exact local jet calculation for the V0=0 missed mode, not the full Ozuch radial coefficient.'
    }
    outpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'step87_missed_killing_mode_receiver.json')
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, 'w') as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
    print(f'Wrote {outpath}')


if __name__ == '__main__':
    main()
