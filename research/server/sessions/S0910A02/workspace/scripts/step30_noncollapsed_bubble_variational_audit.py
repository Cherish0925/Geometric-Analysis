#!/usr/bin/env python3
"""
Step 30: noncollapsed positive-branch bubble/variational audit.

This script records algebraic/scaling checks for returning to the
four-dimensional noncollapsed P_4^+ route in Yau Problem 26.  It is not a
proof.  It verifies:
  * Eguchi-Hanson's leading asymptotic in Ozuch's volume gauge is trace-free
    (ordinary mass/volume flux is blind at leading order).
  * The first Biquard-Ozuch Eguchi-Hanson obstruction is algebraically R_+ v,
    so an orientation v can kill it iff det(R_+)=0.
  * A cone-closeness based approximate Killing/Komar test would need quadratic
    accuracy eta << t^2/r^2 if the bubble coefficient is t^4; this motivates
    variational minimizers with prescribed asymptotics instead of transplanted
    cone fields.
  * The variational almost-Killing functional has Euler-Lagrange operator
    delta delta^* Z = 0 (up to convention), not a curvature smoothing theorem.
"""

import json
import math
from pathlib import Path

import sympy as sp
import numpy as np


def eh_volume_gauge_expansion(order=10):
    """Expansion of Ozuch's EH metric form at infinity.

    eh = A (dr^2 + r^2 a1^2) + B (a2^2 + a3^2)
    cone = dr^2 + r^2(a1^2+a2^2+a3^2)
    A = sqrt(r^4/(1+r^4)), B=sqrt(1+r^4).
    Leading relative coefficients are read against the cone orthonormal basis.
    """
    x = sp.symbols("x")  # x = r^{-4}
    # A = (1+x)^(-1/2), B/r^2=(1+x)^(1/2)
    Arel = sp.series((1 + x) ** sp.Rational(-1, 2), x, 0, 4).removeO()
    Brel = sp.series((1 + x) ** sp.Rational(1, 2), x, 0, 4).removeO()
    dr_rel = sp.expand(Arel - 1)
    a1_rel = sp.expand(Arel - 1)
    a23_rel = sp.expand(Brel - 1)
    trace_rel = sp.expand(dr_rel + a1_rel + 2 * a23_rel)
    # determinant coefficient through trace check: if relative eigenvalues 1+e_i,
    # log sqrt(det) has first variation 1/2 sum e_i; leading term zero.
    leading = {
        "dr2_relative_x_coeff": sp.Rational(-1, 2),
        "alpha1_relative_x_coeff": sp.Rational(-1, 2),
        "alpha2_relative_x_coeff": sp.Rational(1, 2),
        "alpha3_relative_x_coeff": sp.Rational(1, 2),
        "relative_trace_x_coeff": sp.Rational(0),
    }
    return {
        "A_relative_series_in_x_rminus4": str(Arel),
        "B_over_r2_relative_series_in_x_rminus4": str(Brel),
        "relative_difference_series": {
            "dr2": str(dr_rel),
            "alpha1": str(a1_rel),
            "alpha2_alpha3_each": str(a23_rel),
            "trace": str(trace_rel),
        },
        "leading_coefficients": {k: str(v) for k, v in leading.items()},
        "interpretation": (
            "The r^{-4} relative trace vanishes: Eguchi-Hanson is in volume "
            "gauge and ordinary ADM/mass/volume flux is blind at leading order. "
            "The anisotropic coefficient H^4 is nonzero and is detected only "
            "after pairing with the orbifold H_2 curvature term in the "
            "Biquard-Ozuch/Ozuch Pohozaev obstruction."
        ),
    }


def obstruction_algebra():
    """Linear algebra for the EH first obstruction.

    In the Ozuch/Biquard normalization for an EH orientation v in Lambda^2_+,
    the local first obstruction is R_+ v (three scalar conditions).  Some EH
    orientation kills it iff R_+ has a nonzero kernel iff det R_+=0.
    """
    examples = {}
    matrices = {
        "S4_Ric_eq_g": np.diag([1 / 3, 1 / 3, 1 / 3]),
        "CP2_or_S2xS2_Ric_eq_g_relevant_orientation": np.diag([1.0, 0.0, 0.0]),
        "generic_det_zero_not_KE": np.diag([2 / 3, 1 / 3, 0.0]),
        "indefinite_singular": np.diag([1.0, -0.2, 0.0]),
    }
    for name, R in matrices.items():
        evals = np.linalg.eigvalsh(R)
        det = float(np.linalg.det(R))
        min_abs = float(np.min(np.abs(evals)))
        kernel_dim = int(np.sum(np.abs(evals) < 1e-12))
        # obstruction for canonical EH orientation e1, and if possible kernel orientation
        e1 = np.array([1.0, 0.0, 0.0])
        obs_e1_norm = float(np.linalg.norm(R @ e1))
        examples[name] = {
            "eigenvalues_R_plus": [float(x) for x in evals],
            "det_R_plus": det,
            "kernel_dim_numeric": kernel_dim,
            "min_possible_obstruction_norm_over_unit_v": min_abs,
            "canonical_orientation_e1_obstruction_norm": obs_e1_norm,
            "some_orientation_kills_obstruction": bool(kernel_dim > 0),
        }
    return {
        "statement": "For an Eguchi-Hanson bubble with orientation v in Lambda^2_+, first obstruction = R_+ v; an orientation can kill it iff det(R_+)=0.",
        "examples": examples,
        "source_formula": (
            "Ozuch 2021 Theorem 4.6 and Corollary 4.10: for EH H^4=-theta_1^- o omega_1^+/(2 r^4), "
            "the radial and rotation Pohozaev obstructions are equivalent to R_e^{+,(1)}(H_2) omega_1^+ = 0."
        ),
    }


def scaling_audit():
    rows = []
    for t in [1e-1, 1e-2, 1e-3, 1e-4]:
        for alpha in [0.25, 0.5, 0.75]:
            # annulus radius r=t^alpha, bubble coefficient q=t^4
            r = t ** alpha
            q = t ** 4
            # model obstruction flux scale ~ q; cone-field C1 error eta gives quadratic flux error eta^2 r^4.
            eta_detect = math.sqrt(q) / (r ** 2)  # eta^2 r^4 ~ q
            rows.append({
                "t": t,
                "radius_r=t^alpha": r,
                "alpha": alpha,
                "bubble_flux_scale_t4": q,
                "eta_threshold_sqrt(t4)/r2": eta_detect,
            })
    return {
        "model": "If EH bubble coefficient is t^4 and cone-field non-Killing error contributes ~ eta^2 r^4, detection requires eta^2 r^4 << t^4, i.e. eta << t^2/r^2.",
        "samples": rows,
        "interpretation": (
            "At natural intermediate annuli r=t^alpha, alpha<1, the needed cone closeness is much stronger than naive GH/C1 neck closeness. "
            "This supports replacing transplanted cone rotation fields by variational minimizers with prescribed asymptotics/boundary data, whose error is controlled by an energy minimum rather than by raw annular C1 closeness."
        ),
    }


def variational_operator_summary():
    return {
        "functional": "J(Z)=int_Omega |L_Z g|^2 dmu = 4 int |delta^* Z|^2 dmu",
        "euler_lagrange_interior": "delta_g delta_g^* Z = 0 for fixed boundary/asymptotic data (sign conventions may change); on a closed manifold the kernel consists Killing fields.",
        "komar_pohozaev_pairing": "For divergence-free symmetric T, int_boundary T(Z,n)=1/2 int_Omega <T,L_Z g>; if Z is Killing, the bulk term vanishes. For approximate/variational Z, the error is the minimized L_Z energy paired with the tensor being tested, not a derivative of Ricci.",
        "relevance_to_Yau26": (
            "This object can be used in two distinct places: (i) collapse, where central almost-Killing fields should be obtained by minimizing on covers/scale windows; "
            "(ii) noncollapsed bubbles, where rotation/conformal asymptotics can be imposed and the resulting minimizer may define the Pohozaev projection without needing full Biquard-Ozuch normal form for the original C0-pinched metric."
        ),
    }


def main():
    out = {
        "title": "Step 30 noncollapsed bubble / variational-field route audit",
        "scope": "Explore-level algebraic and scaling checks; not a proof or refutation of Yau 26.",
        "eh_volume_gauge_expansion": eh_volume_gauge_expansion(),
        "eguchi_hanson_first_obstruction_algebra": obstruction_algebra(),
        "annular_detection_scaling": scaling_audit(),
        "variational_almost_killing_operator": variational_operator_summary(),
        "route_decision": [
            "For noncollapsed P4+, if the Cheeger-Naber singular set is empty, the limit is a smooth weak Einstein metric and M is eventually diffeomorphic to it; this half is conceptually closed modulo standard convergence/diffeomorphism details.",
            "If singularities occur, finite CGB energy bounds the number of bubbles. The decisive bridge is a Pohozaev/Komar projection that works for C0 Ricci-pinched metrics and forces the Ozuch/Biquard first obstruction R_+ v to vanish.",
            "The EH ordinary mass/volume flux is zero at leading order; the useful flux is the Taub/Pohozaev obstruction paired with the orbifold H2 curvature term and cone rotations/conformal radial field.",
            "Cone-field transplantation requires unrealistically strong annular closeness; variational minimizers with prescribed asymptotics are a more faithful next execution target."
        ],
    }
    path = Path("Sessions/S0910A02/workspace/data/step30_noncollapsed_bubble_variational_audit.json")
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    print(f"\nSaved to {path}")


if __name__ == "__main__":
    main()
