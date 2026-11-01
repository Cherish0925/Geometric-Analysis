"""
Step 79: reconstruct Ozuch's angular rho_x and the EH quadrupole H^4.

Purpose:
  Step 78 froze rho(zeta) in a fixed product Lambda^- frame.  Ozuch
  Definition 1.14 defines rho_x(zeta)_j = x^T(zeta^+ circ omega_j^-)x/|x|^2;
  varying x rotates rho_x(zeta).  This script verifies what survives for
  zeta in ker R^+ = span{omega_2^+, omega_3^+} and what must be withdrawn.

Conventions:
  We use 2-form matrices normalized by 1/sqrt(2) and the symmetrized product
  A circ B = AB+BA.  This equals the product of Ozuch's unnormalised commuting
  matrices, so the matrices agree with earlier Step 77/78 scripts.
"""

import json
import math
from fractions import Fraction

import numpy as np
import sympy as sp


def make_2form_np(entries):
    A = np.zeros((4, 4), dtype=float)
    for i, j, v in entries:
        A[i, j] = v
        A[j, i] = -v
    return A


def make_2form_sp(entries):
    A = sp.zeros(4, 4)
    for i, j, v in entries:
        A[i, j] = v
        A[j, i] = -v
    return A


SQ2 = math.sqrt(2.0)
omega_p = [
    make_2form_np([(0, 1, 1 / SQ2), (2, 3, 1 / SQ2)]),
    make_2form_np([(0, 2, 1 / SQ2), (1, 3, -1 / SQ2)]),
    make_2form_np([(0, 3, 1 / SQ2), (1, 2, 1 / SQ2)]),
]
omega_m = [
    make_2form_np([(0, 1, 1 / SQ2), (2, 3, -1 / SQ2)]),
    make_2form_np([(0, 2, 1 / SQ2), (1, 3, 1 / SQ2)]),
    make_2form_np([(0, 3, 1 / SQ2), (1, 2, -1 / SQ2)]),
]

sqrt2 = sp.sqrt(2)
omega_p_sp = [
    make_2form_sp([(0, 1, 1 / sqrt2), (2, 3, 1 / sqrt2)]),
    make_2form_sp([(0, 2, 1 / sqrt2), (1, 3, -1 / sqrt2)]),
    make_2form_sp([(0, 3, 1 / sqrt2), (1, 2, 1 / sqrt2)]),
]
omega_m_sp = [
    make_2form_sp([(0, 1, 1 / sqrt2), (2, 3, -1 / sqrt2)]),
    make_2form_sp([(0, 2, 1 / sqrt2), (1, 3, 1 / sqrt2)]),
    make_2form_sp([(0, 3, 1 / sqrt2), (1, 2, -1 / sqrt2)]),
]


def circ_np(A, B):
    return A @ B + B @ A


def circ_sp(A, B):
    return A * B + B * A


g1 = np.diag([1.0, 1.0, 0.0, 0.0])
g2 = np.diag([0.0, 0.0, 1.0, 1.0])
R_minus = np.diag([1.0, 0.0, 0.0])


def rho_x(zeta_vec, x):
    """Ozuch rho_x(zeta), in the fixed omega^- basis, for |x| arbitrary."""
    zeta_plus = sum(zeta_vec[i] * omega_p[i] for i in range(3))
    r2 = float(np.dot(x, x))
    comps = []
    for j in range(3):
        C = circ_np(zeta_plus, omega_m[j])
        comps.append(float(x @ C @ x) / r2)
    return np.array(comps)


def H4_angular(zeta_vec, x):
    """Angular part of H^4 at r=1: -1/2 rho_x(zeta)^- circ zeta^+."""
    zeta_plus = sum(zeta_vec[i] * omega_p[i] for i in range(3))
    rho = rho_x(zeta_vec, x)
    rho_minus = sum(rho[j] * omega_m[j] for j in range(3))
    return -0.5 * circ_np(rho_minus, zeta_plus)


def factor_traces(H):
    return float(H[0, 0] + H[1, 1]), float(H[2, 2] + H[3, 3]), float(np.trace(H))


# Exact rho formulas for zeta=e2 and zeta=e3.
x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4", real=True)
xx = sp.Matrix([x1, x2, x3, x4])
r2_sp = x1**2 + x2**2 + x3**2 + x4**2
exact_rho = {}
for label, zeta_idx in [("omega2", 1), ("omega3", 2)]:
    zeta_plus = omega_p_sp[zeta_idx]
    comps = []
    mats = []
    for j in range(3):
        C = sp.simplify(circ_sp(zeta_plus, omega_m_sp[j]))
        mats.append([[sp.simplify(C[a, b]) for b in range(4)] for a in range(4)])
        comps.append(sp.factor((xx.T * C * xx)[0] / r2_sp))
    exact_rho[label] = {
        "rho_components": [str(c) for c in comps],
        "composition_matrices": [[[str(entry) for entry in row] for row in mat] for mat in mats],
    }

# Linear algebra: eta^- circ zeta^+ is factor-traceless for zeta in kernel plane and arbitrary eta.
# We verify on the six basis pairs zeta in {omega2,omega3}, eta in {omega1,omega2,omega3}.
factor_traceless_basis_checks = []
max_basis_factor_trace = 0.0
for zeta_idx in [1, 2]:
    for eta_idx in [0, 1, 2]:
        C = circ_np(omega_m[eta_idx], omega_p[zeta_idx])
        tr1, tr2, tr = factor_traces(C)
        max_basis_factor_trace = max(max_basis_factor_trace, abs(tr1), abs(tr2), abs(tr))
        factor_traceless_basis_checks.append({
            "zeta_plus": f"omega{zeta_idx+1}+",
            "eta_minus": f"omega{eta_idx+1}-",
            "diag": np.round(np.diag(C), 12).tolist(),
            "trace_factor1": round(tr1, 12),
            "trace_factor2": round(tr2, 12),
            "trace_full": round(tr, 12),
            "factor_traceless": abs(tr1) < 1e-12 and abs(tr2) < 1e-12,
        })

# Monte Carlo / deterministic sample on S^3.
rng = np.random.default_rng(7901)
zeta = np.array([0.0, 1.0, 0.0])  # alpha=0, product-kernel direction omega_2^+
N = 20000
rho_samples = []
Rrho_norms = []
first_row_offdiag = []
H4_factor_trace_max = 0.0
for _ in range(N):
    x = rng.normal(size=4)
    x /= np.linalg.norm(x)
    rho = rho_x(zeta, x)
    rho_samples.append(rho)
    Rrho_norms.append(np.linalg.norm(R_minus @ rho))
    dR = 12 * (np.outer(rho, rho) - np.eye(3) * (np.dot(rho, rho) / 3.0))
    first_row_offdiag.append([dR[0, 1], dR[0, 2]])
    H = H4_angular(zeta, x)
    tr1, tr2, tr = factor_traces(H)
    H4_factor_trace_max = max(H4_factor_trace_max, abs(tr1), abs(tr2), abs(tr))

rho_samples = np.array(rho_samples)
Rrho_norms = np.array(Rrho_norms)
first_row_offdiag = np.array(first_row_offdiag)

# A few explicit points showing rho leaves ker R^-.
explicit_points = {
    "north_quat_1": np.array([1.0, 0.0, 0.0, 0.0]),
    "i_axis": np.array([0.0, 1.0, 0.0, 0.0]),
    "mix_13": np.array([1.0, 0.0, 1.0, 0.0]) / math.sqrt(2.0),
    "mix_12": np.array([1.0, 1.0, 0.0, 0.0]) / math.sqrt(2.0),
    "generic": np.array([1.0, 2.0, -1.0, 0.5]) / np.linalg.norm([1.0, 2.0, -1.0, 0.5]),
}
explicit = {}
for name, x in explicit_points.items():
    rho = rho_x(zeta, x)
    H = H4_angular(zeta, x)
    dR = 12 * (np.outer(rho, rho) - np.eye(3) * (np.dot(rho, rho) / 3.0))
    tr1, tr2, tr = factor_traces(H)
    explicit[name] = {
        "x": np.round(x, 8).tolist(),
        "rho_x_omega2": np.round(rho, 12).tolist(),
        "rho_norm": round(float(np.linalg.norm(rho)), 12),
        "R_minus_times_rho": np.round(R_minus @ rho, 12).tolist(),
        "dR_first_row": np.round(dR[0, :], 12).tolist(),
        "H4_diag": np.round(np.diag(H), 12).tolist(),
        "H4_trace_factor1": round(tr1, 12),
        "H4_trace_factor2": round(tr2, 12),
    }

# S^3 distribution moment checks.  For a quaternionic rotation of a fixed unit vector,
# rho is uniformly distributed on S^2; moments should be E rho = 0, E rho rho^T = I/3.
moment_mean = rho_samples.mean(axis=0)
moment_second = rho_samples.T @ rho_samples / N
mean_dR = 12 * (moment_second - np.eye(3) * np.trace(moment_second) / 3.0)

results = {
    "step": 79,
    "purpose": "correct Step78 fixed-rho substitution by reconstructing Ozuch rho_x and H^4 angular tensor",
    "source_definition": {
        "Ozuch_Definition_1_14_lines": "Knowledge object lines 301-302: rho_x(zeta)_j = x^T(zeta^+ circ omega_j^-)x/|x|^2",
        "Ozuch_Remark_1_15_lines": "lines 304-305: rho_x is quaternionic conjugation on pure quaternions",
        "Ozuch_H4_lines": "lines 320-332: H^4(zeta^+) = -rho_x(zeta)^- circ zeta^+/(2 r^4)",
    },
    "exact_rho_formulas": exact_rho,
    "factor_traceless_survives": {
        "statement": "For zeta^+ in span{omega2^+,omega3^+}, eta^- circ zeta^+ is factor-traceless for arbitrary eta^-.",
        "max_basis_factor_trace": max_basis_factor_trace,
        "basis_checks": factor_traceless_basis_checks,
        "consequence": "The bare angular H^4 direct pairing with scalar tensors f*g1 and f*g2 vanishes pointwise, without freezing rho_x.",
    },
    "fixed_rho_claims_withdrawn": {
        "rho1_range_for_zeta_omega2": [float(rho_samples[:, 0].min()), float(rho_samples[:, 0].max())],
        "rho_norm_max_error": float(np.max(np.abs(np.linalg.norm(rho_samples, axis=1) - 1.0))),
        "fraction_samples_with_abs_rho1_gt_0_1": float(np.mean(np.abs(rho_samples[:, 0]) > 0.1)),
        "R_minus_rho_norm_max": float(Rrho_norms.max()),
        "R_minus_rho_norm_mean": float(Rrho_norms.mean()),
        "dR_first_row_offdiag_abs_max": float(np.max(np.abs(first_row_offdiag))),
        "mean_rho": np.round(moment_mean, 8).tolist(),
        "second_moment_rho": np.round(moment_second, 8).tolist(),
        "mean_dR_over_S3_approx": np.round(mean_dR, 8).tolist(),
        "interpretation": "rho_x(omega2) rotates through S^2; it is not confined to ker R^-=(omega2^-,omega3^-). Pointwise R^- rho_x and off-block dR entries are generally nonzero.",
    },
    "H4_angular_checks": {
        "samples": N,
        "max_factor_trace_abs_for_H4": H4_factor_trace_max,
        "explicit_points": explicit,
    },
}

print(json.dumps(results, indent=2))
out = "Sessions/S0910A01/workspace/data/step79_angular_rho_verify.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print(f"Wrote {out}")
