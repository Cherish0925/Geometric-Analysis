"""
Step 26: nilpotent submersion balance tests for the Yau-26 positive branch.

Purpose
-------
Agent3 execution for the abelian-forcing route.  This script does not attempt a
full global collapse theorem.  It checks the finite-dimensional algebra that any
such theorem must survive:

1. Intrinsic Ricci of the 3D Heisenberg fibre [e1,e2]=b e3.
2. The totally-geodesic submersion/twist-only vertical equation
       Ric^V_M = Ric^F + Q,
   where Q is positive semidefinite and rank(Q) <= binom(d,2) for base dimension d.
   This tests anisotropy and trace, not just scalar sign.
3. A cohomogeneity-one diagonal Heisenberg fibration
       g = dt^2 + a(t)^2(theta1^2+theta2^2)+c(t)^2 theta3^2,
   [E1,E2]=E3, b=c/a^2,
   where the second fundamental form T is the active mechanism.  The vertical
   Einstein equations Ric=+1 and the dt dt equation reduce to an explicit ODE
   plus Hamiltonian constraint.  This tests whether T can reverse Milnor's
   anisotropy locally.

The output is evidence for theorem formulation: twist-only/T=0 admits a clean
bounded-bracket statement; with T allowed, large Heisenberg bracket is not
pointwise impossible but forces second fundamental form of order b and rapid
relative scaling, so any abelian-forcing theorem must be integrated/graded and
cannot be a local algebraic tautology.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp


def heisenberg_intrinsic_ricci(b: float) -> np.ndarray:
    """Ricci eigenvalues in an orthonormal H3 frame with [e1,e2]=b e3."""
    return np.array([-0.5 * b * b, -0.5 * b * b, 0.5 * b * b], dtype=float)


def twist_target_Q_for_exact_positive(b: float, lam: float = 1.0) -> np.ndarray:
    """Q required in Ric_F + Q = lam I for a totally geodesic submersion."""
    return lam * np.ones(3) - heisenberg_intrinsic_ricci(b)


def twist_only_bounds(delta: float) -> dict:
    """Necessary bound from the centre direction when Q is positive semidefinite.

    Since Ric_F(e3)=+b^2/2 and Q(e3,e3)>=0, the upper pinching
    Ric_M(e3,e3) <= 1+delta implies b^2/2 <= 1+delta.
    """
    return {
        "delta": delta,
        "necessary_b_squared_upper_from_center": 2.0 * (1.0 + delta),
        "necessary_abs_b_upper": math.sqrt(2.0 * (1.0 + delta)),
    }


def rank_needed_for_Q(q_diag: np.ndarray, tol: float = 1e-12) -> int:
    return int(np.sum(q_diag > tol))


def binom2(d: int) -> int:
    return d * (d - 1) // 2


def twist_only_rank_table(b_values=(0.1, 0.7, 1.0, math.sqrt(2.0), 2.0), max_base_dim=7):
    rows = []
    for b in b_values:
        q = twist_target_Q_for_exact_positive(b)
        psd = bool(np.all(q >= -1e-12))
        rank_need = rank_needed_for_Q(q)
        feasible_base_dims = [d for d in range(1, max_base_dim + 1) if binom2(d) >= rank_need]
        rows.append({
            "b": b,
            "RicF_diag": heisenberg_intrinsic_ricci(b).tolist(),
            "Q_needed_diag_for_Ric_equals_1": q.tolist(),
            "Q_needed_psd": psd,
            "rank_needed_if_psd": rank_need if psd else None,
            "minimal_base_dimension_by_rank_only": feasible_base_dims[0] if (psd and feasible_base_dims) else None,
            "interpretation": (
                "twist-only exact Ric=1 algebraically possible by PSD/rank only"
                if psd and feasible_base_dims else
                "twist-only exact Ric=1 impossible by center upper bound or rank"
            ),
        })
    return rows


# Cohomogeneity-one H3 fibration formulas.
# k1 = a'/a for the two generating directions, k3 = c'/c for the center, H=2 k1+k3.
# b=c/a^2 so b'/b = k3 - 2 k1.
# Intrinsic fibre Ricci: (-b^2/2, -b^2/2, +b^2/2).
# Hypersurface evolution vertical Ricci components in orthonormal directions:
# r_i = Ric_F,i - k_i' - H k_i.
# dt dt component: r0 = -[2(k1' + k1^2) + (k3' + k3^2)].
# Exact Ric=+1 vertical equations define k1', k3'.  The dt dt equation is the constraint
#     4 k1^2 + 8 k1 k3 + b^2 + 4 = 0.


def hamiltonian_constraint(b: float, k1: float, k3: float) -> float:
    return 4.0 * k1 * k1 + 8.0 * k1 * k3 + b * b + 4.0


def k3_from_constraint(b: float, k1: float) -> float:
    if abs(k1) < 1e-14:
        raise ValueError("k1 must be nonzero to solve the constraint for k3")
    return -(4.0 * k1 * k1 + b * b + 4.0) / (8.0 * k1)


def cohom1_rhs(t: float, y: np.ndarray, lam: float = 1.0) -> np.ndarray:
    b, k1, k3 = y
    H = 2.0 * k1 + k3
    # vertical equations Ric_gen=lam, Ric_center=lam
    k1_prime = -lam - 0.5 * b * b - H * k1
    k3_prime = -lam + 0.5 * b * b - H * k3
    b_prime = b * (k3 - 2.0 * k1)
    return np.array([b_prime, k1_prime, k3_prime])


def cohom1_ricci_components(b: float, k1: float, k3: float, k1_prime: float, k3_prime: float) -> dict:
    H = 2.0 * k1 + k3
    r_gen = -0.5 * b * b - k1_prime - H * k1
    r_center = 0.5 * b * b - k3_prime - H * k3
    r_00 = -(2.0 * (k1_prime + k1 * k1) + (k3_prime + k3 * k3))
    return {"r_00": r_00, "r_gen_1": r_gen, "r_gen_2": r_gen, "r_center": r_center}


def integrate_cohom1_sample(b0: float = 20.0, x: float = 0.5, t_end: float = 0.01) -> dict:
    """Integrate a local exact-Einstein ODE sample.

    k1 is chosen as x*b0; k3 is solved from the Hamiltonian constraint.  This is
    not a compact metric; it is a local model demonstrating that T can carry the
    required anisotropy at a point, but at cost |T|~b and rapid b evolution.
    """
    k10 = x * b0
    k30 = k3_from_constraint(b0, k10)
    y0 = np.array([b0, k10, k30], dtype=float)
    sol = solve_ivp(lambda t, y: cohom1_rhs(t, y), (0.0, t_end), y0, rtol=1e-10, atol=1e-12, max_step=t_end / 200)
    samples = []
    max_constraint = 0.0
    max_ricci_error = 0.0
    for idx in np.linspace(0, sol.y.shape[1] - 1, 6, dtype=int):
        t = float(sol.t[idx])
        b, k1, k3 = map(float, sol.y[:, idx])
        rhs = cohom1_rhs(t, np.array([b, k1, k3]))
        ric = cohom1_ricci_components(b, k1, k3, rhs[1], rhs[2])
        constraint = hamiltonian_constraint(b, k1, k3)
        max_constraint = max(max_constraint, abs(constraint))
        max_ricci_error = max(max_ricci_error, max(abs(v - 1.0) for v in ric.values()))
        samples.append({
            "t": t,
            "b": b,
            "k1=a_prime_over_a": k1,
            "k3=c_prime_over_c": k3,
            "mean_curvature_H": 2.0 * k1 + k3,
            "b_prime": float(rhs[0]),
            "T_norm_squared_diagonal_proxy_2k1sq_plus_k3sq": 2.0 * k1 * k1 + k3 * k3,
            "constraint_4k1sq_8k1k3_bsq_4": constraint,
            "ricci_components_from_equations": ric,
        })
    return {
        "initial_choice": {"b0": b0, "x=k1/b0": x, "k1_0": k10, "k3_0": k30, "t_end": t_end},
        "success": bool(sol.success),
        "message": sol.message,
        "max_abs_constraint_on_samples": max_constraint,
        "max_abs_ricci_minus_1_on_samples": max_ricci_error,
        "samples": samples,
        "interpretation": (
            "The diagonal H3 cohomogeneity-one equations admit local exact Ric=+1 data with large b, "
            "but only with |T|~|k|~b and b changing on length scale 1/b. This defeats a pointwise "
            "Milnor-only abelian-forcing proof once T is allowed; a valid theorem must be graded/integrated/global."
        ),
    }


def scaling_examples():
    """Relative collapse rates for Heisenberg nilmanifold metrics.

    Original bracket [E1,E2]=E3.  If generating scale is a=eps^alpha and center
    scale c=eps^gamma, orthonormal bracket b=c/a^2=eps^(gamma-2alpha).
    Homothetic collapse has gamma=alpha, so b=eps^(-alpha) -> infinity.
    Graded collapse with gamma=2alpha keeps b=1; faster center collapse gamma>2alpha
    makes b->0.  At the visible fibre-diameter scale, bounded b becomes abelian.
    """
    eps_values = [1e-1, 1e-2, 1e-3, 1e-4]
    regimes = [
        ("homothetic", 1.0, 1.0),
        ("graded_keeps_b_constant", 1.0, 2.0),
        ("supergraded_b_to_0", 1.0, 2.5),
    ]
    rows = []
    for name, alpha, gamma in regimes:
        vals = []
        for eps in eps_values:
            a = eps ** alpha
            c = eps ** gamma
            b = c / (a * a)
            diameter_proxy = max(a, c)
            rescaled_bracket_at_diam1 = b * diameter_proxy
            vals.append({"eps": eps, "a": a, "c": c, "b=c/a^2": b, "diameter_proxy": diameter_proxy,
                         "b_times_diameter_proxy": rescaled_bracket_at_diam1})
        rows.append({"regime": name, "alpha": alpha, "gamma": gamma, "values": vals})
    return rows


def main():
    out = {
        "title": "Step 26 nilpotent submersion balance audit",
        "scope": "Local/algebraic tests for positive Ricci collapse; not a global Yau-26 proof/refutation.",
        "heisenberg_intrinsic_Ricci_formula": {
            "bracket": "[e1,e2]=b e3 in an orthonormal fibre frame",
            "Ric_diag": "(-b^2/2, -b^2/2, +b^2/2)",
            "scalar": "-b^2/2",
            "anisotropy_center_minus_generator": "b^2",
        },
        "twist_only_T_equals_0_analysis": {
            "vertical_equation_model": "Ric_M^V = Ric_F + Q, Q>=0, rank(Q)<=binom(base_dim,2)",
            "necessary_upper_pinching_bound": twist_only_bounds(delta=0.1),
            "exact_Ric_equals_1_rank_table": twist_only_rank_table(),
            "main_conclusion": (
                "With T=0, two-sided positive pinching controls the Heisenberg bracket by the centre direction: "
                "b^2/2 <= 1+delta. Exact Ric=1 additionally requires Q=I-Ric_F, so Q must be PSD and high rank; "
                "H3 over a 2-dimensional base is impossible by rank, but this is a T=0 theorem, not the desired general collapse theorem."
            ),
        },
        "cohomogeneity_one_T_active_model": {
            "metric": "dt^2 + a(t)^2(theta1^2+theta2^2)+c(t)^2 theta3^2 on H3, [E1,E2]=E3",
            "variables": "k1=a'/a, k3=c'/c, H=2k1+k3, b=c/a^2",
            "vertical_Ricci_equations_Ric_equals_1": {
                "generator": "-b^2/2 - k1' - H k1 = 1",
                "center": "+b^2/2 - k3' - H k3 = 1",
                "b_evolution": "b'/b = k3 - 2 k1",
                "dt_dt_constraint": "4 k1^2 + 8 k1 k3 + b^2 + 4 = 0",
            },
            "sample_large_b_local_solution": integrate_cohom1_sample(b0=20.0, x=0.5, t_end=0.01),
            "scaling_regimes": scaling_examples(),
            "main_conclusion": (
                "T can reproduce the opposite anisotropy locally: large b is compatible with the pointwise Ric=1 equations "
                "only if the fibre second fundamental form is also large and anisotropic. Thus abelian forcing must be a "
                "relative-rate/global statement: homothetic nonabelian collapse is ruled out, but graded nilpotent collapse can hide "
                "the bracket at the first collapse scale and should be treated by iterated abelian stages."
            ),
        },
        "source_status": {
            "Kapovitch_Wilking_checked_via_Naber_Zhang_lines": ["NZ object lines 373-389 quote KW Theorem 2.26 and refined Theorem 2.27"],
            "ONeill_formula_source_status": (
                "Direct O'Neill/Besse formulas not fully ingested; accessible submersion source lines 179-183 state A/T roles and cite Besse/O'Neill. "
                "The cohomogeneity-one equations use standard hypersurface evolution and should receive independent verification before theorem use."
            ),
        },
        "Yau26_implication": (
            "This step strengthens the positive-branch architecture but does not solve Yau-26. It converts abelian forcing from an overstrong pointwise claim "
            "into a sharper conjectural theorem: under C^0 positive pinching, local lower-Ricci collapse groups are almost nilpotent; upper pinching plus "
            "O'Neill equations should forbid ungraded nonabelian bracket-scale collapse, while graded collapse factors through torus/circle stages."
        ),
    }
    out_path = Path(__file__).resolve().parents[1] / "data" / "step26_nilpotent_submersion_balance.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
