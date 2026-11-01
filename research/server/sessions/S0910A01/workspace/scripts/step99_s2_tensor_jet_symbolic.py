#!/usr/bin/env python3
"""
Step 99: symbolic local S^2 jet check for the tensor-scalar product modes.

The Step 98 AA/BB tensor calculation used only the product Hessian component
    H_{ab,mn}=T_{ab}(pole) (nabla^2 f)_{mn}(pole)
for h=T_A f_B.  A complete product eigentensor also has, when f is zonal
(m=0) at the other factor pole,
    H_{ab,pq}=(nabla^2 T)_{ab,pq}(pole) f(pole)
with p,q on the tensor factor.  Mixed first-derivative terms are possible for
m=1 scalar factors, but the sparse receiver/source functionals annihilate that
support; this script focuses on the same-factor second derivative contribution.

It derives the local normal-coordinate quartic expansion on the unit S^2 for
m=2 scalar harmonics and the associated electric TF tensor and full magnetic
Lie-derivative tensor, then contracts their same-factor Hessian jets with the
Step 96 Ozuch source functional.  The output is formula-level evidence about
whether Step 98's restricted H_ab,mn model omitted a surviving source term.
"""
from __future__ import annotations

import importlib.util
import json
import math
import pathlib
import sys

import numpy as np
import sympy as sp

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

_spec = importlib.util.spec_from_file_location("step96_ab", SCRIPT_DIR / "step96_kernel_plane_ab_map.py")
step96 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = step96
_spec.loader.exec_module(step96)

x, y, mu_sym, b_sym = sp.symbols("x y mu b")
coords = [x, y]
r2 = x*x + y*y
alpha = (sp.Integer(2) - mu_sym) / sp.Integer(12)

# Unit S^2 metric in geodesic normal coordinates to quadratic order.
# g_ij = delta_ij - (1/3)(|x|^2 delta_ij - x_i x_j) + O(|x|^3)
g = sp.Matrix([[1 - y*y/3, x*y/3], [x*y/3, 1 - x*x/3]])
# Inverse to the order needed for linear Christoffels.
ginv = sp.Matrix([[1 + y*y/3, -x*y/3], [-x*y/3, 1 + x*x/3]])

Gamma = [[ [sp.Integer(0) for _ in range(2)] for _ in range(2)] for _ in range(2)]
for k in range(2):
    for i in range(2):
        for j in range(2):
            expr = sp.Integer(0)
            for l in range(2):
                expr += ginv[k, l] * (sp.diff(g[l, j], coords[i]) + sp.diff(g[l, i], coords[j]) - sp.diff(g[i, j], coords[l])) / 2
            poly = sp.Poly(sp.expand(expr), x, y)
            lin = sp.Integer(0)
            for monom, coeff in poly.terms():
                ax, ay = monom
                if ax + ay <= 1:
                    lin += coeff * x**ax * y**ay
            Gamma[k][i][j] = sp.expand(lin)

J = sp.Matrix([[0, -1], [1, 0]])


def hessian_scalar(f: sp.Expr) -> list[list[sp.Expr]]:
    H = [[sp.Integer(0) for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for c in range(2):
            expr = sp.diff(f, coords[a], coords[c])
            for r in range(2):
                expr -= Gamma[r][a][c] * sp.diff(f, coords[r])
            # keep to quadratic order, sufficient for second derivatives at 0
            poly = sp.Poly(sp.expand(expr), x, y)
            out = sp.Integer(0)
            for monom, coeff in poly.terms():
                ax, ay = monom
                if ax + ay <= 2:
                    out += coeff * x**ax * y**ay
            H[a][c] = sp.expand(out)
    return H


def cov_hess_tensor_at_origin(T: list[list[sp.Expr]]) -> np.ndarray:
    """Return array K[a,c,p,q]=(nabla_p nabla_q T)_{ac}(0)."""
    T0 = [[sp.simplify(T[a][c].subs({x: 0, y: 0})) for c in range(2)] for a in range(2)]
    K = np.empty((2, 2, 2, 2), dtype=object)
    for a in range(2):
        for c in range(2):
            for p in range(2):
                for q in range(2):
                    expr = sp.diff(T[a][c], coords[p], coords[q]).subs({x: 0, y: 0})
                    # Because Gamma(0)=0, only derivatives of the first covariant derivative's connection terms survive.
                    for r in range(2):
                        expr -= sp.diff(Gamma[r][p][a], coords[q]).subs({x: 0, y: 0}) * T0[r][c]
                        expr -= sp.diff(Gamma[r][p][c], coords[q]).subs({x: 0, y: 0}) * T0[a][r]
                    K[a, c, p, q] = sp.factor(sp.simplify(expr))
    return K


def electric_tensor_from_scalar(f: sp.Expr) -> list[list[sp.Expr]]:
    H = hessian_scalar(f)
    E = [[sp.Integer(0) for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for c in range(2):
            E[a][c] = sp.expand(H[a][c] + (mu_sym / 2) * f * g[a, c])
    return E


def magnetic_tensor_from_scalar(f: sp.Expr) -> list[list[sp.Expr]]:
    # Full Lie derivative L_{J grad f} g. Since J is parallel on an oriented surface,
    # covariantly this is J_c^r Hess_{ar} f + J_a^r Hess_{cr} f.
    H = hessian_scalar(f)
    M = [[sp.Integer(0) for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for c in range(2):
            expr = sp.Integer(0)
            for r in range(2):
                expr += J[c, r] * H[a][r] + J[a, r] * H[c][r]
            M[a][c] = sp.expand(expr)
    return M


def embed_same_factor(K2: np.ndarray, sector: str) -> np.ndarray:
    H4 = np.zeros((4, 4, 4, 4), dtype=float)
    for a in range(2):
        for c in range(2):
            for p in range(2):
                for q in range(2):
                    val = float(K2[a, c, p, q])
                    if sector == "AA":
                        H4[a, c, p, q] += val
                    elif sector == "BB":
                        H4[2+a, 2+c, 2+p, 2+q] += val
                    else:
                        raise ValueError(sector)
    return H4


def source_receiver_contractions(K2: np.ndarray, sector: str) -> dict:
    H4 = embed_same_factor(K2, sector)
    out = {}
    for chir in ["plus", "minus"]:
        out[f"receiver_{chir}"] = step96.receiver_matrix(H4, chir).tolist()
        out[f"source_{chir}_over_pi2"] = step96.source_matrix_over_pi2(H4, chir).tolist()
    return out


def formula_array_to_str(A: np.ndarray) -> list:
    return [[[[str(A[a, c, p, q]) for q in range(2)] for p in range(2)] for c in range(2)] for a in range(2)]


def eval_K(K: np.ndarray, ell: int, bval: float) -> np.ndarray:
    out = np.zeros((2, 2, 2, 2), dtype=float)
    for idx in np.ndindex(2, 2, 2, 2):
        out[idx] = float(K[idx].subs({mu_sym: ell*(ell+1), b_sym: bval}))
    return out


def b2(ell: int) -> float:
    m = ell * (ell + 1)
    return (2 * ell + 1) * m * (m - 2) / (128.0 * math.pi)


def numerical_examples() -> dict:
    examples = {}
    for ell in [2, 3, 4, 5]:
        bval = math.sqrt(b2(ell))
        row = {"ell": ell, "mu": ell*(ell+1), "b": bval}
        for seed, Kform in FORMULAS.items():
            Knum = eval_K(Kform, ell, bval)
            row[seed] = {}
            for sector in ["AA", "BB"]:
                row[seed][sector] = source_receiver_contractions(Knum, sector)
        examples[f"ell_{ell}"] = row
    return examples

# Local m=2 scalar harmonics through quartic order.
psi_c = b_sym * (x*x - y*y) * (1 + alpha*r2)
psi_s = b_sym * (2*x*y) * (1 + alpha*r2)

TENSORS = {
    "electric_c2": electric_tensor_from_scalar(psi_c),
    "electric_s2": electric_tensor_from_scalar(psi_s),
    "magnetic_c2": magnetic_tensor_from_scalar(psi_c),
    "magnetic_s2": magnetic_tensor_from_scalar(psi_s),
}
FORMULAS = {name: cov_hess_tensor_at_origin(T) for name, T in TENSORS.items()}

# Summarize whether same-factor jets are annihilated by the two functionals.
formula_summary = {}
for name, K in FORMULAS.items():
    formula_summary[name] = {
        "K_ac_pq": formula_array_to_str(K),
        "symbolic_nonzero_entries": [
            {"a": a, "c": c, "p": p, "q": q, "value": str(K[a, c, p, q])}
            for a, c, p, q in np.ndindex(2, 2, 2, 2) if K[a, c, p, q] != 0
        ],
    }

results = {
    "step": 99,
    "purpose": "check omitted same-factor second-derivative jets for product tensor-scalar eigentensors",
    "normal_coordinates": {
        "metric_O2": "g_ij=delta_ij-(|x|^2 delta_ij-x_i x_j)/3+O(|x|^3) on unit S^2",
        "m2_scalar_expansion": "psi=b*(quadratic m=2)*(1+(2-mu)r^2/12)+O(r^6)",
        "electric_tensor": "E=Hess(psi)+(mu/2)psi*g",
        "magnetic_tensor": "M=L_{J grad psi}g=J_c^r Hess_{ar}psi+J_a^r Hess_{cr}psi",
    },
    "functional_support_test_from_step96": {
        "same_factor_receiver": "Step96 R_plus/R_minus annihilate arbitrary H_ab,pq supported wholly in the tensor factor for AA/BB.",
        "same_factor_source": "Step96 source functional does NOT annihilate such jets; hence same-factor tensor Hessians can alter the Green pairing if the other scalar factor has nonzero value.",
        "mixed_first_derivative_support": "Step96 R and S annihilate arbitrary mixed derivative support for AA/BB components, so m=1 scalar-gradient terms are invisible to these functionals.",
    },
    "same_factor_tensor_hessian_formulas": formula_summary,
    "numerical_examples": numerical_examples(),
    "interpretation": [
        "For m=2 scalar factors on the other S^2, f(pole)=0, so the same-factor tensor Hessian term is absent and Step98's H_ab,mn component is complete for that mode family.",
        "For zonal m=0 scalar factors, f(pole) is nonzero while Hess(f) is isotropic, so one must check the omitted same-factor tensor Hessian term directly; receiver sparsity alone is not enough because arbitrary same-factor jets can be seen by the source functional.",
        "The later authoritative partial-jet check in step99_tensor_partial_jets.json shows that for the actual electric/full-Lie magnetic m=2 tensor families, the omitted same-factor partial jets have zero Step96 source and receiver contraction. Thus this file is only a preliminary covariant-jet support warning, not evidence of a surviving missing contribution.",
    ],
}

out = DATA_DIR / "step99_s2_tensor_samefactor_jets.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)

# Print a compact human-readable summary.
print(json.dumps({
    "purpose": results["purpose"],
    "nonzero_formula_counts": {k: len(v["symbolic_nonzero_entries"]) for k, v in formula_summary.items()},
    "ell2_electric_c2_AA_source_plus": results["numerical_examples"]["ell_2"]["electric_c2"]["AA"]["source_plus_over_pi2"],
    "ell2_electric_c2_AA_receiver_plus": results["numerical_examples"]["ell_2"]["electric_c2"]["AA"]["receiver_plus"],
    "main_interpretation": results["interpretation"],
    "superseding_check": "See Sessions/S0910A01/workspace/data/step99_tensor_partial_jets.json for the authoritative partial-normal-coordinate same-factor jet contraction.",
    "output": str(out),
}, indent=2))
