#!/usr/bin/env python3
"""
Step 89: exact normalization, algebraic source--receiver identity, and
principal spectral support checks for the product-orbifold chirality calculation.

This script repairs the Step 88 normalization/positivity drift.  It uses the
Ozuch/Step87 convention in which C_ab = omega_a^+ o omega_b^- is a trace-free
involution (tr C_ab C_cd = 4 delta_ac delta_bd) and the boundary source is
computed from the homogeneous quadratic polynomial V_2, not from the Hessian
without the required factor 1/2.

Objects checked:
  1. Exact identity between the chirality-odd H^4 boundary source and the
     chirality-odd receiver curvature functional at the flat V_2 principal
     level:
         S_odd(V_2) = (pi^2/2) R_odd(V_2)
     for arbitrary symmetric Hessian H_{ij,pq}=d_p d_q h_ij(0), where
     V_2(x)=1/2 H_{ij,pq} x_p x_q.
  2. The parallel shape tensor q=g_A-g_B is TT and has Pq=-q, so P is not
     positive on all TT tensors.  Its principal odd source is zero.
  3. The four scalar Ozuch zero modes u_A g_A, u_A g_B, u_B g_A, u_B g_B have
     zero principal odd source at the same level.
  4. A finite relative comparison formula cancels all diagonal coefficients
     algebraically because epsilon_i^2-1=0; positivity of the full relative
     off-diagonal limit is not inferred.
"""
from __future__ import annotations

import json
import math
import pathlib
from fractions import Fraction
from itertools import product

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# Exact C_ab matrices in the Ozuch trace-free involution convention.
# -----------------------------------------------------------------------------
def wedge(i: int, j: int, n: int = 4) -> np.ndarray:
    A = np.zeros((n, n), dtype=int)
    A[i, j] = 1
    A[j, i] = -1
    return A


def build_C_int() -> tuple[np.ndarray, list[np.ndarray], list[np.ndarray]]:
    e01 = wedge(0, 1); e02 = wedge(0, 2); e03 = wedge(0, 3)
    e12 = wedge(1, 2); e13 = wedge(1, 3); e23 = wedge(2, 3)
    rt2 = math.sqrt(2.0)
    wp = [(e01 + e23)/rt2, (e02 - e13)/rt2, (e03 + e12)/rt2]
    wm = [(e01 - e23)/rt2, (e02 + e13)/rt2, (e03 - e12)/rt2]
    C = np.zeros((3, 3, 4, 4), dtype=float)
    for a in range(3):
        for b in range(3):
            prod_ab = wp[a] @ wm[b]
            C[a, b] = prod_ab + prod_ab.T
    C_int = np.rint(C).astype(int)
    if np.max(np.abs(C - C_int)) > 1e-12:
        raise RuntimeError("C matrices were not integral")
    return C_int, wp, wm


C, wp_float, wm_float = build_C_int()

orth_err = 0
for a, b, c, d in product(range(3), repeat=4):
    val = int(np.sum(C[a, b] * C[c, d]))
    expected = 4 if (a == c and b == d) else 0
    orth_err = max(orth_err, abs(val - expected))

# D = sum_k C_{2k}\otimes C_{2k} - C_{k2}\otimes C_{k2}, with index 2 = 0-based 1.
D = np.zeros((4, 4, 4, 4), dtype=int)
for k in range(3):
    D += np.einsum('ij,pq->ijpq', C[1, k], C[1, k]).astype(int)
    D -= np.einsum('ij,pq->ijpq', C[k, 1], C[k, 1]).astype(int)

# -----------------------------------------------------------------------------
# Boundary and receiver functionals.
# -----------------------------------------------------------------------------
def source_odd_over_pi2_from_H(H: np.ndarray) -> Fraction:
    """S_odd/pi^2 from a symmetric Hessian H=d_p d_q h_ij(0).

    The homogeneous quadratic term is V_2 = (1/2) H_{ijpq} x_p x_q.
    For polynomial coefficients V, S_odd/pi^2 = -(1/16) D:V.
    Hence in Hessian variables S_odd/pi^2 = -(1/32) D:H.
    """
    val = int(np.einsum('ijpq,ijpq->', D, H))
    return Fraction(-val, 32)


def riemann_from_H(H: np.ndarray) -> np.ndarray:
    R = np.zeros((4, 4, 4, 4), dtype=Fraction)
    for a, b, c, d in product(range(4), repeat=4):
        R[a, b, c, d] = Fraction(
            H[a, d, b, c] + H[b, c, a, d] - H[a, c, b, d] - H[b, d, a, c],
            2,
        )
    return R

# Exact normalized SD/ASD forms as coefficient dictionaries with 1/sqrt(2)
# avoided.  If Omega = raw/sqrt(2), then <Omega, R Omega> has contraction
# (1/4)*(1/2)*raw R raw = raw R raw / 8.  This matches Step87's normalized
# 2-form convention.
wp_raw = [wedge(0,1)+wedge(2,3), wedge(0,2)-wedge(1,3), wedge(0,3)+wedge(1,2)]
wm_raw = [wedge(0,1)-wedge(2,3), wedge(0,2)+wedge(1,3), wedge(0,3)-wedge(1,2)]


def block_entry_raw(R: np.ndarray, rawA: np.ndarray, rawB: np.ndarray) -> Fraction:
    total = Fraction(0, 1)
    for i, j, k, l in product(range(4), repeat=4):
        if rawA[i, j] and rawB[k, l]:
            total += Fraction(int(rawA[i, j]) * int(rawB[k, l]), 1) * R[i, j, k, l]
    return total / 8


def receiver_odd_from_H(H: np.ndarray) -> Fraction:
    """R_odd=(delta R^+_{22}-delta R^-_{22})/2 for zeta=omega_2."""
    R = riemann_from_H(H)
    Rp22 = block_entry_raw(R, wp_raw[1], wp_raw[1])
    Rm22 = block_entry_raw(R, wm_raw[1], wm_raw[1])
    return (Rp22 - Rm22) / 2


def receiver_even_from_H(H: np.ndarray) -> Fraction:
    R = riemann_from_H(H)
    Rp22 = block_entry_raw(R, wp_raw[1], wp_raw[1])
    Rm22 = block_entry_raw(R, wm_raw[1], wm_raw[1])
    return (Rp22 + Rm22) / 2

# -----------------------------------------------------------------------------
# Exact identity on a basis of all symmetric Hessians.
# -----------------------------------------------------------------------------
def sym_hessian_basis_element(ij: tuple[int, int], pq: tuple[int, int]) -> np.ndarray:
    """Basis tensor H symmetric in ij and pq with unit independent component."""
    i, j = ij; p, q = pq
    H = np.zeros((4, 4, 4, 4), dtype=int)
    tensor_pairs = [(i, j)] if i == j else [(i, j), (j, i)]
    deriv_pairs = [(p, q)] if p == q else [(p, q), (q, p)]
    for a, b in tensor_pairs:
        for c, d in deriv_pairs:
            H[a, b, c, d] = 1
    return H

pairs = [(i, j) for i in range(4) for j in range(i, 4)]
identity_failures = []
identity_max_abs_num = Fraction(0, 1)
nonzero_identity_tests = 0
for ij in pairs:
    for pq in pairs:
        H = sym_hessian_basis_element(ij, pq)
        S = source_odd_over_pi2_from_H(H)     # S_odd/pi^2
        Rodd = receiver_odd_from_H(H)         # R_odd
        diff = S - Rodd / 2                   # expected 0
        if diff != 0:
            identity_failures.append({"ij": ij, "pq": pq, "S_over_pi2": str(S), "Rodd": str(Rodd), "diff": str(diff)})
        if S != 0 or Rodd != 0:
            nonzero_identity_tests += 1
        identity_max_abs_num = max(identity_max_abs_num, abs(diff))

# Also record the tensor relation D:H = -16 R_odd in Hessian variables.
D_relation_failures = []
for ij in pairs:
    for pq in pairs:
        H = sym_hessian_basis_element(ij, pq)
        DH = int(np.einsum('ijpq,ijpq->', D, H))
        Rodd = receiver_odd_from_H(H)
        if Fraction(DH, 1) + 16 * Rodd != 0:
            D_relation_failures.append({"ij": ij, "pq": pq, "D_H": DH, "Rodd": str(Rodd)})

# -----------------------------------------------------------------------------
# Test named modes with the corrected normalization.
# -----------------------------------------------------------------------------
def oneform_linear(kind: str, factor: str) -> np.ndarray:
    A = np.zeros((4, 4), dtype=int)
    if factor == 'A':
        i0, i1 = 0, 1
    elif factor == 'B':
        i0, i1 = 2, 3
    else:
        raise ValueError(factor)
    if kind == 'grad':
        A[i0, i0] = -1
        A[i1, i1] = -1
    elif kind == 'kill':
        A[i0, i1] = 1
        A[i1, i0] = -1
    else:
        raise ValueError(kind)
    return A


def sym_product_hessian(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """H=d^2(alpha\otimes beta+beta\otimes alpha) for linear one-forms."""
    M = np.zeros((4, 4, 4, 4), dtype=int)  # polynomial coefficient, not sym in derivatives
    for i, j, p, q in product(range(4), repeat=4):
        M[i, j, p, q] = A[i, p] * B[j, q] + B[i, p] * A[j, q]
    return M + M.transpose(0, 1, 3, 2)

named_modes = {}
for Ak, Bk in [('grad','grad'), ('grad','kill'), ('kill','grad'), ('kill','kill')]:
    H = sym_product_hessian(oneform_linear(Ak, 'A'), oneform_linear(Bk, 'B'))
    named_modes[f'{Ak}A_{Bk}B'] = {
        'S_odd_over_pi2': str(source_odd_over_pi2_from_H(H)),
        'R_odd': str(receiver_odd_from_H(H)),
        'S_even_over_pi2_not_computed_here': 'see Step87/88 if needed',
        'identity_S_over_pi2_minus_Rodd_over_2': str(source_odd_over_pi2_from_H(H) - receiver_odd_from_H(H)/2),
    }

# -----------------------------------------------------------------------------
# Principal source support for the negative shape mode and scalar zero modes.
# -----------------------------------------------------------------------------
def add_s2_metric_hessian(H: np.ndarray, factor: str, tensor_factor: str, scalar_factor: str | None, scalar_kind: str | None, sign: int) -> None:
    """Add a local Hessian contribution for sign * scalar * g_tensor_factor.

    factor labels: A directions 0,1; B directions 2,3.
    scalar_kind can be None (constant 1), 'uA' or 'uB' with u=height at north.
    The metric Hessian in geodesic normal coordinates on S^2(1) is
        g_ab = delta_ab - (1/3)(delta_ab |x|^2 - x_a x_b)+O(r^3)
    within its own factor.
    Height at a north pole is u=1 - |x|^2/2 + O(r^4) in its factor.
    """
    dirs = {'A': (0, 1), 'B': (2, 3)}
    a0, a1 = dirs[tensor_factor]
    # Hessian of the metric tensor components.
    Hg = np.zeros((4,4,4,4), dtype=Fraction)
    for a in [a0, a1]:
        for b in [a0, a1]:
            for p in [a0, a1]:
                for q in [a0, a1]:
                    # d_p d_q[-1/3(delta_ab (x_a0^2+x_a1^2) - x_a x_b)]
                    delta_ab = 1 if a == b else 0
                    delta_pq_in = 1 if p == q else 0
                    # d_p d_q (x_a x_b) = delta_pa delta_qb + delta_pb delta_qa
                    d2_xaxb = (1 if (p == a and q == b) else 0) + (1 if (p == b and q == a) else 0)
                    Hg[a,b,p,q] = Fraction(-1,3) * (delta_ab * 2 * delta_pq_in - d2_xaxb)
    # Constant metric value delta_ab.
    g0 = np.zeros((4,4), dtype=int)
    g0[a0,a0] = 1; g0[a1,a1] = 1
    # Hessian of scalar.
    Hu = np.zeros((4,4), dtype=Fraction)
    u0 = Fraction(1,1)
    if scalar_kind is None:
        u0 = Fraction(1,1)
    else:
        sf = 'A' if scalar_kind == 'uA' else 'B'
        s0, s1 = dirs[sf]
        for p in [s0, s1]:
            Hu[p,p] = Fraction(-1,1)  # d^2[-|x|^2/2]
    # H(scalar*g)=u0 Hg + Hu*g0 (first derivative terms vanish at north).
    for i,j,p,q in product(range(4), repeat=4):
        val = u0 * Hg[i,j,p,q] + Hu[p,q] * g0[i,j]
        if val:
            H[i,j,p,q] = Fraction(H[i,j,p,q]) + sign * val


def fraction_tensor_to_int_scaled(H_frac: np.ndarray, scale: int = 6) -> np.ndarray:
    out = np.zeros(H_frac.shape, dtype=int)
    for idx in product(*[range(s) for s in H_frac.shape]):
        out[idx] = int(Fraction(H_frac[idx]) * scale)
    return out

# Shape q = g_A - g_B.  Use Fraction tensor then scale by 6 for exact integer functions.
Hq_frac = np.empty((4,4,4,4), dtype=object); Hq_frac.fill(Fraction(0,1))
add_s2_metric_hessian(Hq_frac, 'A', 'A', None, None, +1)
add_s2_metric_hessian(Hq_frac, 'B', 'B', None, None, -1)
Hq = fraction_tensor_to_int_scaled(Hq_frac, 6)
# Scaling by 6 means source/R scale by 6; zero remains zero.

scalar_modes = {}
for scalar_kind in ['uA', 'uB']:
    for tensor_factor in ['A', 'B']:
        Hf = np.empty((4,4,4,4), dtype=object); Hf.fill(Fraction(0,1))
        add_s2_metric_hessian(Hf, tensor_factor, tensor_factor, scalar_kind, scalar_kind, +1)
        H_int = fraction_tensor_to_int_scaled(Hf, 6)
        key = f'{scalar_kind}_g{tensor_factor}'
        scalar_modes[key] = {
            'scaled_by': 6,
            'S_odd_over_pi2_scaled': str(source_odd_over_pi2_from_H(H_int)),
            'R_odd_scaled': str(receiver_odd_from_H(H_int)),
            'principal_odd_source_zero': source_odd_over_pi2_from_H(H_int) == 0,
        }

shape_mode = {
    'mode': 'q=g_A-g_B',
    'TT': True,
    'P_eigenvalue_unit_sphere_normalization': -1,
    'scaled_by': 6,
    'S_odd_over_pi2_scaled': str(source_odd_over_pi2_from_H(Hq)),
    'R_odd_scaled': str(receiver_odd_from_H(Hq)),
    'principal_odd_source_zero': source_odd_over_pi2_from_H(Hq) == 0,
    'reason_for_zero': 'its quadratic metric expansion has tensor and derivative support inside one S^2 factor, so the fully mixed non-diagonal D contraction vanishes',
}

# -----------------------------------------------------------------------------
# Relative comparison algebra.
# -----------------------------------------------------------------------------
NODES = ['NN','NS','SN','SS']
s = {'NN': 1, 'NS': -1, 'SN': -1, 'SS': 1}
eps_same = {n: 1 for n in NODES}
eps_mixed = dict(s)
relative_coeff_factor = {}
for i in NODES:
    for j in NODES:
        relative_coeff_factor[f'{i},{j}'] = eps_mixed[i]*eps_mixed[j] - eps_same[i]*eps_same[j]

diagonal_relative_factors = {n: relative_coeff_factor[f'{n},{n}'] for n in NODES}
nonzero_relative_pairs = {k: v for k, v in relative_coeff_factor.items() if v != 0}

# Axial off-diagonal relative sign under a provisional odd kernel K_ij^ax = kappa*s_i*s_j.
axial_relative_factors = {}
for i in NODES:
    for j in NODES:
        factor = (eps_mixed[i]*eps_mixed[j] - 1) * s[i] * s[j]
        axial_relative_factors[f'{i},{j}'] = factor

results = {
    'scope': 'Step89 corrected principal algebra and spectral-support checks',
    'normalization': {
        'C_convention': 'C_ab=omega_a^+ o omega_b^- as trace-free involutions, tr(C_ab C_cd)=4 delta_ac delta_bd',
        'V2_convention': 'smooth tensor expansion h=V0 + V2 + O(r^4), V2=(1/2) H_ijpq x_p x_q with H=d_p d_q h_ij(0)',
        'source_formula': 'S_odd/pi^2 = -(1/32) D_ijpq H_ijpq = -(1/16) D_ijpq V_ijpq',
        'receiver_formula': 'R_odd=(delta R^+_22 - delta R^-_22)/2, where delta R^pm_22 is the curvature-operator matrix entry in the normalized SD/ASD basis (omega/sqrt(2)); delta R_ijkl=1/2(h_il,jk+h_jk,il-h_ik,jl-h_jl,ik)',
        'correct_identity': 'S_odd(V2) = (pi^2/2) R_odd(H), where V2=(1/2)H_ijpq x_p x_q',
        'equivalent_tensor_relation': 'D:H = -16 R_odd (Hessian variables); D:V = -8 R_odd (polynomial coefficient variables)',
        'step88_factor_issue': 'step88_source_receiver_proportionality used Hessian variables in the source contraction without the 1/2 converting H to V2, giving pi^2 instead of pi^2/2',
    },
    'C_orthogonality_max_integer_error': orth_err,
    'identity_basis_test': {
        'basis_dimension_symmetric_H': len(pairs)*len(pairs),
        'nonzero_tests': nonzero_identity_tests,
        'failures_count': len(identity_failures),
        'failures': identity_failures[:10],
        'D_relation_failures_count': len(D_relation_failures),
    },
    'named_modes_corrected': named_modes,
    'shape_negative_mode_support': shape_mode,
    'scalar_zero_mode_support': scalar_modes,
    'relative_interaction_algebra': {
        'nodes': NODES,
        'mixed_epsilon': [eps_mixed[n] for n in NODES],
        'all_same_epsilon': [eps_same[n] for n in NODES],
        'formula': 'Radial Delta_tau = sum_ij a_i b_j (epsilon_i epsilon_j - 1) K_ij^odd(tau) with a_i=t_i receiver weight and b_j=t_j^2 source weight. A purely energy-like comparison may use w_i w_j, but it is not Ozuch radial order. Diagonal odd-odd factors vanish before tau->0.',
        'diagonal_relative_factors': diagonal_relative_factors,
        'nonzero_relative_pairs': nonzero_relative_pairs,
        'axial_if_Kij_equals_kappa_sisj': axial_relative_factors,
        'interpretation': 'relative comparison cancels common odd-odd self singularities algebraically; sign of the finite off-diagonal limit is not implied by positivity of a regularized full matrix. Even-odd and odd-even diagonal terms require separate symmetry or renormalization.',
    },
    'order_bookkeeping': {
        'inter_node_term': 't_i t_j^2 = O(t^3) for comparable scales',
        'Ozuch_Prop_2_19_remainder': 'O(t_max^(5/2)) in the necessary estimate',
        'comparison': 't^3 is smaller than t^(5/2) as t->0, so Proposition 2.19 cannot decide this layer without a sharper projected expansion',
    },
}

outpath = DATA_DIR / 'step89_identity_and_spectral_support.json'
with open(outpath, 'w') as f:
    json.dump(results, f, indent=2, default=str)

print(json.dumps(results, indent=2, default=str))
print(f'Wrote {outpath}')
