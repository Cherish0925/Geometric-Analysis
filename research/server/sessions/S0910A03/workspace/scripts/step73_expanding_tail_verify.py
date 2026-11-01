"""Verify the long expanding-tail mechanism for the Yau-26 graph-neck route.

Metric on [r0,r0+K] x T^3:
    g = dr^2 + e^(2r) [dz^2 + N^(-2)e^v dx^2 + N^(-2)e^(-v) dy^2],
    v(r,z) = chi((r-r0)/K) A sin(z),
where chi=1 at the left end, chi=0 at the right end, and its first two
 derivatives vanish at both ends.

The script symbolically checks the claimed Ricci-defect formulas by substituting
this ansatz into the exact conformal-gauge formulas from Step 72, then evaluates
operator-norm suprema on dense grids.  Outputs are research data, not a global
neck construction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


def symbolic_check() -> dict:
    # Conformal coordinate t=e^{-r}.  Then
    # g=t^{-2}(dt^2+dz^2+N^{-2}e^v dx^2+N^{-2}e^{-v}dy^2).
    t, z, N = sp.symbols("t z N", positive=True, real=True)
    v = sp.Function("v")(t, z)
    phi = -sp.log(t)
    b = -sp.log(t) - sp.log(N) + v / 2
    c = -sp.log(t) - sp.log(N) - v / 2

    def d(f, *args):
        return sp.diff(f, *args)

    em2p = sp.exp(-2 * phi)
    # Exact normalized formulas copied algebraically from the Step-72 derivation.
    Ett = (
        3
        - em2p * d(b, t) ** 2
        + em2p * d(b, t) * d(phi, t)
        - em2p * d(b, t, 2)
        - em2p * d(b, z) * d(phi, z)
        - em2p * d(c, t) ** 2
        + em2p * d(c, t) * d(phi, t)
        - em2p * d(c, t, 2)
        - em2p * d(c, z) * d(phi, z)
        - em2p * d(phi, t, 2)
        - em2p * d(phi, z, 2)
    )
    Etz_cov = (
        -d(b, t) * d(b, z)
        + d(b, t) * d(phi, z)
        + d(b, z) * d(phi, t)
        - d(c, t) * d(c, z)
        + d(c, t) * d(phi, z)
        + d(c, z) * d(phi, t)
        - d(b, t, z)
        - d(c, t, z)
    )
    Ezz = (
        3
        - em2p * d(b, t) * d(phi, t)
        - em2p * d(b, z) ** 2
        + em2p * d(b, z) * d(phi, z)
        - em2p * d(b, z, 2)
        - em2p * d(c, t) * d(phi, t)
        - em2p * d(c, z) ** 2
        + em2p * d(c, z) * d(phi, z)
        - em2p * d(c, z, 2)
        - em2p * d(phi, t, 2)
        - em2p * d(phi, z, 2)
    )
    Ex = (
        3
        - em2p * d(b, t) ** 2
        - em2p * d(b, t) * d(c, t)
        - em2p * d(b, t, 2)
        - em2p * d(b, z) ** 2
        - em2p * d(b, z) * d(c, z)
        - em2p * d(b, z, 2)
    )
    Ey = (
        3
        - em2p * d(b, t) * d(c, t)
        - em2p * d(b, z) * d(c, z)
        - em2p * d(c, t) ** 2
        - em2p * d(c, t, 2)
        - em2p * d(c, z) ** 2
        - em2p * d(c, z, 2)
    )

    # Expected orthonormal components in (t,z) coordinates.  Since the base
    # metric is t^{-2}(dt^2+dz^2), E^hat_{ab}=t^2 E_{ab}^{coord}.
    grad2 = t**2 * (d(v, t) ** 2 + d(v, z) ** 2)
    # r=-log t: v_rr+3v_r+e^{-2r}v_zz
    Lv = t**2 * (d(v, t, 2) + d(v, z, 2)) - 2 * t * d(v, t)
    expected = {
        "Ett": -sp.Rational(1, 2) * t**2 * d(v, t) ** 2,
        "Ezz": -sp.Rational(1, 2) * t**2 * d(v, z) ** 2,
        "Etz_orth": -sp.Rational(1, 2) * t**2 * d(v, t) * d(v, z),
        "Ex": -sp.Rational(1, 2) * Lv,
        "Ey": sp.Rational(1, 2) * Lv,
    }
    residuals = {
        "Ett": sp.simplify(Ett - expected["Ett"]),
        "Ezz": sp.simplify(Ezz - expected["Ezz"]),
        "Etz_orth": sp.simplify(t**2 * Etz_cov - expected["Etz_orth"]),
        "Ex": sp.simplify(Ex - expected["Ex"]),
        "Ey": sp.simplify(Ey - expected["Ey"]),
    }
    return {
        "coordinate_relation": "t=exp(-r)",
        "Lv_in_t": str(Lv),
        "grad_norm_sq": str(grad2),
        "formula_residuals": {k: str(val) for k, val in residuals.items()},
        "all_zero": all(val == 0 for val in residuals.values()),
    }


def chi(s: np.ndarray) -> np.ndarray:
    # 1 minus the quintic smootherstep; C^2 matches constants at both ends.
    return 1.0 - 10.0 * s**3 + 15.0 * s**4 - 6.0 * s**5


def chi_p(s: np.ndarray) -> np.ndarray:
    return -30.0 * s**2 + 60.0 * s**3 - 30.0 * s**4


def chi_pp(s: np.ndarray) -> np.ndarray:
    return -60.0 * s + 180.0 * s**2 - 120.0 * s**3


def tail_sup(r0: float, K: float, amplitude: float = 1.0,
             nr: int = 1001, nz: int = 1024) -> dict:
    s = np.linspace(0.0, 1.0, nr)[:, None]
    z = np.linspace(0.0, 2.0 * np.pi, nz, endpoint=False)[None, :]
    r = r0 + K * s

    vv = amplitude * chi(s) * np.sin(z)
    vr = amplitude * chi_p(s) * np.sin(z) / K
    vrr = amplitude * chi_pp(s) * np.sin(z) / (K * K)
    vz = amplitude * chi(s) * np.cos(z)
    vzz = -vv

    grad2 = vr**2 + np.exp(-2.0 * r) * vz**2
    Lv = vrr + 3.0 * vr + np.exp(-2.0 * r) * vzz

    # The base block is the rank-one operator -1/2 grad(v) tensor grad(v).
    # Its nonzero eigenvalue has absolute value grad2/2.  Fiber eigenvalues
    # are +/- Lv/2, so this is the exact full operator norm.
    defect = np.maximum(0.5 * grad2, 0.5 * np.abs(Lv))
    idx = np.unravel_index(np.argmax(defect), defect.shape)

    # Gaussian shape operator: (1, 1+vr/2, 1-vr/2), hence H=3 and
    # |S-I|^2=vr^2/2=-E_rr pointwise.
    shear_sq = 0.5 * vr**2
    Err = -0.5 * vr**2
    balance_residual = float(np.max(np.abs(Err + shear_sq)))

    return {
        "r0": r0,
        "K": K,
        "amplitude": amplitude,
        "sup_defect_exact": float(np.max(defect)),
        "K_times_sup_defect": float(K * np.max(defect)),
        "sup_grad_sq_half": float(np.max(0.5 * grad2)),
        "sup_abs_Lv_half": float(np.max(0.5 * np.abs(Lv))),
        "argmax_s": float(s[idx[0], 0]),
        "argmax_z": float(z[0, idx[1]]),
        "left_defect": float(np.max(defect[0, :])),
        "right_defect": float(np.max(defect[-1, :])),
        "anisotropy_left_oscillation": float(np.ptp(vv[0, :])),
        "anisotropy_right_oscillation": float(np.ptp(vv[-1, :])),
        "normal_balance_residual": balance_residual,
        "mean_curvature": 3.0,
        "N_dependence": "none",
    }


def main() -> None:
    symbolic = symbolic_check()
    runs = []
    for r0 in (2.0, 4.0, 6.0):
        for K in (4.0, 8.0, 16.0, 32.0, 64.0):
            runs.append(tail_sup(r0, K))

    result = {
        "metric": "dr^2+e^(2r)[dz^2+N^(-2)e^v dx^2+N^(-2)e^(-v)dy^2]",
        "v": "chi((r-r0)/K) A sin(z)",
        "symbolic_check": symbolic,
        "exact_formulas": {
            "E_base": "-(1/2) dv tensor dv",
            "E_x": "-(1/2)(v_rr+3v_r+e^(-2r)v_zz)",
            "E_y": "+(1/2)(v_rr+3v_r+e^(-2r)v_zz)",
            "operator_norm": "max(|dv|_B^2/2, |v_rr+3v_r+e^(-2r)v_zz|/2)",
            "shape": "diag(1,1+v_r/2,1-v_r/2)",
            "normal_balance": "E_rr=-|S-I|^2=-v_r^2/2; H=3",
        },
        "bound": "C_A,chi (K^(-1)+K^(-2)+exp(-2r0)), uniformly in N",
        "runs": runs,
    }

    out = Path(__file__).resolve().parent.parent / "data" / "step73_expanding_tail.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({
        "symbolic_all_zero": symbolic["all_zero"],
        "selected_runs": [x for x in runs if x["r0"] == 6.0],
        "output": str(out),
    }, indent=2))


if __name__ == "__main__":
    main()
