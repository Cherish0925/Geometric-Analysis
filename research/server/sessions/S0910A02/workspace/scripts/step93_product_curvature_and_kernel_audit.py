"""
Step 93 curvature correction audit for the positive/negative product mirrors.

Purpose: independently check the load-bearing curvature value in the Step 92
Ozuch-spectral note.  The product Einstein metric on S^2 x S^2 is NOT
conformally flat.  In the standard self-dual/anti-self-dual bases its chiral
curvature blocks are R^+ = R^- = diag(Lambda,0,0), not (Lambda/3) I.

The script also records the immediate consequence for the obstruction problem:
the Kähler axis e1 is the rank-one image direction, while the allowed EH
parameter directions are the kernel plane span{e2,e3}.  A small toy computation
of Ozuch's single-image b_x restricted to this kernel plane is included only to
show the corrected algebraic target; it is not the full physical coefficient on
(S^2 x S^2)/Z2.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "step93_product_curvature_and_kernel_audit.json"


def chiral_blocks(lambda_einstein: float):
    """Return R^+, R^-, W^+, W^- for product of two surfaces with K=lambda.

    Orthonormal basis: e1,e2 tangent to first factor; e3,e4 tangent to second.
    Curvature operator on Λ^2 has eigenvalue λ on e12,e34 and zero on mixed
    planes.  Since Ric=λ g in four dimensions, scalar/12 = λ/3.
    """
    lam = float(lambda_einstein)
    # two-form basis [12,13,14,23,24,34]
    R2 = np.diag([lam, 0.0, 0.0, 0.0, 0.0, lam])
    rt2 = math.sqrt(2.0)
    # columns are SD basis ω1+=(12+34)/sqrt2,
    # ω2+=(13-24)/sqrt2, ω3+=(14+23)/sqrt2
    Pp = np.zeros((6, 3))
    Pp[0, 0] = 1 / rt2
    Pp[5, 0] = 1 / rt2
    Pp[1, 1] = 1 / rt2
    Pp[4, 1] = -1 / rt2
    Pp[2, 2] = 1 / rt2
    Pp[3, 2] = 1 / rt2
    # ASD basis ω1-=(12-34)/sqrt2,
    # ω2-=(13+24)/sqrt2, ω3-=(14-23)/sqrt2
    Pm = np.zeros((6, 3))
    Pm[0, 0] = 1 / rt2
    Pm[5, 0] = -1 / rt2
    Pm[1, 1] = 1 / rt2
    Pm[4, 1] = 1 / rt2
    Pm[2, 2] = 1 / rt2
    Pm[3, 2] = -1 / rt2
    Rp = Pp.T @ R2 @ Pp
    Rm = Pm.T @ R2 @ Pm
    Wp = Rp - (lam / 3.0) * np.eye(3)
    Wm = Rm - (lam / 3.0) * np.eye(3)
    return R2, Rp, Rm, Wp, Wm


def qmul(q, p):
    a, b, c, d = q
    e, f, g, h = p
    return np.array([
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    ], dtype=float)


def rho_x(x, zeta):
    x = np.asarray(x, dtype=float)
    zeta = np.asarray(zeta, dtype=float)
    r2 = float(np.dot(x, x))
    q = x
    p = np.array([0.0, zeta[0], zeta[1], zeta[2]])
    qc = np.array([q[0], -q[1], -q[2], -q[3]])
    res = qmul(qmul(q, p), qc) / r2
    return res[1:]


def b_matrix(x, zeta):
    """3x3 matrix 12 rho_x(zeta) rho_x(zeta)^T/|x|^6 - 4|zeta|^2 I/|x|^6."""
    x = np.asarray(x, dtype=float)
    zeta = np.asarray(zeta, dtype=float)
    r2 = float(np.dot(x, x))
    rho = rho_x(x, zeta)
    return (12.0 * np.outer(rho, rho) - 4.0 * float(np.dot(zeta, zeta)) * np.eye(3)) / (r2 ** 3)


def mat_to_list(a):
    return [[float(x) for x in row] for row in np.asarray(a)]


def eigvals(a):
    return [float(x) for x in np.linalg.eigvalsh(np.asarray(a, dtype=float))]


results = {
    "purpose": "Correct Step92 false claim R^±=(Λ/3)I for the product mirror; identify the allowed EH kernel plane.",
    "curvature_blocks": {},
    "consequences": {},
    "toy_kernel_restricted_ozuch_single_image": {},
}

for name, lam in [("positive_S2xS2", 1.0), ("negative_surface_product", -1.0)]:
    R2, Rp, Rm, Wp, Wm = chiral_blocks(lam)
    results["curvature_blocks"][name] = {
        "einstein_constant_Lambda": lam,
        "R2_operator_basis_12_13_14_23_24_34": mat_to_list(R2),
        "R_plus": mat_to_list(Rp),
        "R_minus": mat_to_list(Rm),
        "W_plus": mat_to_list(Wp),
        "W_minus": mat_to_list(Wm),
        "R_plus_eigenvalues": eigvals(Rp),
        "R_minus_eigenvalues": eigvals(Rm),
        "W_plus_eigenvalues": eigvals(Wp),
        "W_minus_eigenvalues": eigvals(Wm),
        "R_is_Lambda_over_3_identity": bool(np.allclose(Rp, (lam / 3.0) * np.eye(3))),
        "R_is_rank_one_diag_Lambda_0_0": bool(np.allclose(Rp, np.diag([lam, 0.0, 0.0])) and np.allclose(Rm, np.diag([lam, 0.0, 0.0]))),
        "W_nonzero": bool(not np.allclose(Wp, 0.0) and not np.allclose(Wm, 0.0)),
    }

R2p, Rp, Rm, Wp, Wm = chiral_blocks(1.0)
K = np.diag([0.0, 1.0, 1.0])
results["consequences"] = {
    "positive_product_correct_R_pm": "diag(1,0,0), not (1/3)I",
    "negative_product_correct_R_pm": "diag(-1,0,0), not (-1/3)I",
    "allowed_EH_directions": "ker R^± = span{e2,e3} = ω^⊥; e1 is the Kähler/image direction and is excluded by the zeroth-order obstruction.",
    "no_critical_scale_equation": "For ζ=t ξ with ξ in ker R, the projected leading equation is Π_K Q Π_K ξ=0; t cancels. There is no 1/3 + t^2 K critical scale in the product mirror.",
    "sanity_checks": [
        "If W vanished, the Einstein product would have constant sectional curvature, but S^2xS^2 has zero mixed sectional curvatures.",
        "The all-compatible r=0 row admits the known KE desingularization, forcing a nontrivial kernel direction at each product node; an invertible (1/3)I obstruction would forbid it."
    ],
}

# Toy single-image kernel restriction.  This is not the curved product physical coefficient.
e1 = np.array([1.0, 0.0, 0.0])
e2 = np.array([0.0, 1.0, 0.0])
e3 = np.array([0.0, 0.0, 1.0])
x_id = np.array([1.0, 0.0, 0.0, 0.0])
x_i = np.array([0.0, 1.0, 0.0, 0.0])
for source_name, zeta in [("excluded_e1_Kahler_axis", e1), ("kernel_e2", e2), ("kernel_e3", e3)]:
    for sep_name, x in [("sep_1_identity_rotation", x_id), ("sep_i_rotation", x_i)]:
        B = b_matrix(x, zeta)
        Bker = K @ B @ K
        Bker2 = B[1:3, 1:3]
        results["toy_kernel_restricted_ozuch_single_image"][f"{source_name}__{sep_name}"] = {
            "rho_x_zeta": [float(v) for v in rho_x(x, zeta)],
            "full_B_matrix": mat_to_list(B),
            "kernel_2x2_block_e2e3": mat_to_list(Bker2),
            "kernel_2x2_eigenvalues": eigvals(Bker2),
            "physical_status": "toy flat single-image algebra only; full product coefficient needs projected P^{-1}, gauge/Bianchi, isotropy, and r=0 KE calibration",
        }

DATA.parent.mkdir(parents=True, exist_ok=True)
DATA.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Saved {DATA.relative_to(ROOT.parents[1]) if False else DATA}")
print("Positive product R^+=R^-=diag(1,0,0); W^±=diag(2/3,-1/3,-1/3).")
print("The old Step92 I/3/critical-scale framing is invalid; allowed EH directions lie in span{e2,e3}.")
