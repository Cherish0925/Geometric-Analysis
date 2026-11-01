#!/usr/bin/env python3
"""
Step 60 executable ledger for Yau-26.

Purpose:
1. Correct the Step-59 H4-dual matching analysis using the l=2 Wronskian
   propagator and the resonant beta=2 weight.
2. Quantify the actual rate-limited necessity theorem: delta log(1/t) -> 0.
3. Exhibit the named failure/counterexample channel: exponentially small bubble
   scale relative to the C^0 Ricci defect, t ~ exp(-const/delta).
4. Compute the first scalar ALF indicial/flux model (Taub-NUT/Schwarzschild
   mass term) and compare its source accumulation with the ALE l=2 logarithmic
   resonance.

This is a scaling/ODE/flux ledger, not a complete geometric construction.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import sympy as sp
except Exception as e:  # pragma: no cover
    sp = None

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step60_resonant_flux_neck_alf.json"


def verify_l2_particular() -> Dict[str, str]:
    """Verify the resonant particular solution for L f = S.

    L = d^2 + 3/r d - 8/r^2, homogeneous roots 2 and -4.
    The solution with f(r0)=f'(r0)=0 for constant source S is
        S/6 r^2 log(r/r0) - S/36 (r^2 - r0^6 r^-4).
    """
    if sp is None:
        return {"status": "sympy_unavailable"}
    r, r0, S = sp.symbols("r r0 S", positive=True)
    f = S / 6 * r**2 * sp.log(r / r0) - S / 36 * (r**2 - r0**6 * r**-4)
    Lf = sp.simplify(sp.diff(f, r, 2) + 3 / r * sp.diff(f, r) - 8 / r**2 * f)
    f_r0 = sp.simplify(f.subs(r, r0))
    fp_r0 = sp.simplify(sp.diff(f, r).subs(r, r0))
    # Extract coefficient of r^2 at large r after dividing by r^2.
    alpha_asymptotic = sp.simplify(f / r**2)
    return {
        "status": "ok",
        "operator": "L f = f'' + (3/r) f' - (8/r^2) f",
        "particular_solution": str(f),
        "Lf_simplifies_to": str(Lf),
        "f_at_r0": str(f_r0),
        "fprime_at_r0": str(fp_r0),
        "asymptotic_growing_coefficient_f_over_r2": str(alpha_asymptotic),
        "interpretation": "The source S produces growing coefficient (S/6) log(r/r0) - S/36 + o(1). For a neck from r0=O(1) to R=t^{-1/2}, relative drift is O(delta log(1/t)).",
    }


def h4_rate_tables() -> Dict[str, object]:
    rows = []
    # Use convention: t is the metric bubble scale in the ALE frame; outer ALE radius R=t^{-1/2}.
    # l=2 coefficient drift from constant source S=t*delta is approx (t*delta/6) log R = (t*delta/12) log(1/t).
    # Signal is t*kappa.  Relative error = (delta/12) log(1/t), constants suppressed in theorem statements.
    for log10_t in [4, 8, 12, 16, 20, 40, 80]:
        t = 10.0 ** (-log10_t)
        L = math.log(1.0 / t)
        schedules = {
            "delta=1/log^2": 1.0 / (L * L),
            "delta=1/log": 1.0 / L,
            "delta=0.05": 0.05,
            "delta=sqrt(t)": math.sqrt(t),
        }
        for name, delta in schedules.items():
            rel_no_constants = delta * L
            rel_with_ode_constant = delta * L / 12.0
            abs_flux_error = t * rel_with_ode_constant
            rows.append(
                {
                    "t": t,
                    "log10_1_over_t": log10_t,
                    "schedule": name,
                    "delta": delta,
                    "delta_log_1_over_t": rel_no_constants,
                    "relative_flux_error_with_constant_1_over_12": rel_with_ode_constant,
                    "absolute_flux_error_for_signal_t": abs_flux_error,
                    "necessity_regime_delta_log_to_zero": rel_no_constants < 0.1,
                }
            )
    exponential = []
    # Solve rel error C*delta*log(1/t) ~= kappa.  Constants depend on normalization;
    # record both the scale-free relation and the ODE constant 1/12 relation.
    for delta in [0.2, 0.1, 0.05, 0.02, 0.01]:
        kappa = 1.0
        log_no_constants = kappa / delta
        log_with_ode_constant = 12.0 * kappa / delta
        # Use log10 to avoid underflow.
        exponential.append(
            {
                "delta": delta,
                "log_1_over_t_for_CdeltaLog_equals_1": log_no_constants,
                "log10_1_over_t_for_CdeltaLog_equals_1": log_no_constants / math.log(10),
                "log_1_over_t_for_ODE_constant_1_over_12_equals_1": log_with_ode_constant,
                "log10_1_over_t_for_ODE_constant_1_over_12_equals_1": log_with_ode_constant / math.log(10),
                "named_channel": "bubble metric scale exponentially small relative to pinching defect",
            }
        )
    return {
        "convention": "t is metric bubble scale; outer ALE radius R ~ t^{-1/2}; signal flux from ambient H2 is size t*kappa; pointwise Ricci defect in ALE frame has size <= t*delta.",
        "relative_error_formula": "|Delta B|/|B_signal| <= C delta log(1/t). In the scalar l=2 ODE model with constant source and R=t^{-1/2}, C=1/12.",
        "rate_rows": rows,
        "exponential_failure_scales": exponential,
    }


def weighted_beta_check() -> Dict[str, object]:
    betas = [0.0, 0.5, 1.0, 1.5, 1.9, 2.0]
    rows = []
    # Source weighted norm for pointwise Ricci defect: ||E||_{C^0_{beta-2}} ~ t delta R^{2-beta}
    # with R=t^-1/2 gives delta t^{beta/2}; target for matching is t.
    for log10_t in [8, 16, 32]:
        t = 10.0 ** (-log10_t)
        L = math.log(1.0 / t)
        delta = 1.0 / (L * L)  # a schedule with delta log -> 0
        for beta in betas:
            weighted_source = delta * (t ** (beta / 2.0))
            factor_over_target = weighted_source / t
            rows.append(
                {
                    "t": t,
                    "log10_1_over_t": log10_t,
                    "delta_schedule": "1/log^2(1/t)",
                    "delta": delta,
                    "beta": beta,
                    "weighted_source_delta_t_beta_over_2": weighted_source,
                    "factor_over_target_t": factor_over_target,
                    "beta_less_2_worse_than_target": beta < 2.0 and factor_over_target > 1.0,
                    "beta_equals_2_resonant": beta == 2.0,
                }
            )
    return {
        "formula": "For beta in [0,2], ||E||_{C^0_{beta-2}} ~ t*delta*R^{2-beta} at R=t^{-1/2}, hence ~ delta*t^{beta/2}; target O(t). For beta<2 this exceeds t by delta*t^{beta/2-1}; beta=2 is the resonant endpoint and must be handled by flux/log rather than nonresonant Fredholm inversion.",
        "rows": rows,
    }


def alf_roots_and_flux() -> Dict[str, object]:
    roots = []
    for ell in range(0, 6):
        alpha_plus = float(ell)
        alpha_minus = float(-ell - 1)
        # radial Wronskian constant for f=r^ell, g=r^{-ell-1} in 3D scalar Laplacian:
        # r^2(f*g' - g*f') = -(2ell+1).
        wr = -(2 * ell + 1)
        roots.append(
            {
                "ell": ell,
                "alpha_plus": alpha_plus,
                "alpha_minus": alpha_minus,
                "growth": f"r^{ell}",
                "decay": f"r^{-ell-1}",
                "radial_wronskian_r2_constant": wr,
            }
        )
    accum = []
    # Scalar ALF/Gibbons-Hawking mass model: Delta_{R3} V = S.
    # Flux m(R)=R^2 V'(R); m(R2)-m(R1)=int S r^2 dr.
    # Compare coherent source S=t*delta*r^{-q} over [1,R=t^-1/2].
    for log10_t in [4, 8, 12, 16]:
        t = 10.0 ** (-log10_t)
        R = t ** (-0.5)
        delta = 1.0 / (math.log(1.0 / t) ** 2)
        for q in [0, 1, 2, 3, 4]:
            if abs(q - 3) < 1e-12:
                integral = t * delta * math.log(R)
                growth_type = "log"
            else:
                power = 3.0 - q
                integral = t * delta * (R ** power - 1.0) / power
                growth_type = f"R^{3-q}" if q < 3 else "bounded_tail"
            accum.append(
                {
                    "t": t,
                    "outer_R": R,
                    "delta": delta,
                    "source_model": f"S=t*delta*r^(-{q}) in Delta_R3 V",
                    "mass_flux_drift": integral,
                    "drift_divided_by_t": integral / t,
                    "growth_type": growth_type,
                }
            )
    return {
        "model": "ALF scalar mass model (Gibbons-Hawking/Taub-NUT asymptotic): V=1+m/r+..., Delta_{R^3}V=0 in the Ricci-flat case; mass flux is R^2 d_R V.",
        "interpretation": "The leading ALF mass deviation is ell=0 decay r^{-1}, paired with the constant mode by a nonzero Wronskian. This is not the ALE l=2 (r^2,r^-4) curvature-block degeneracy condition. Source accumulation is polynomial for weight q<3 and logarithmic only at q=3, so the ALF collapse obstruction has a different scale law and must be analyzed in the correct fibration variables.",
        "roots": roots,
        "source_accumulation_rows": accum,
    }


def collapse_blowup_accounting() -> Dict[str, object]:
    rows = []
    for k in [1, 2, 10, 100]:
        chi = 2 * k + 2
        tau = 0
        total_weyl_energy_limit = 8 * math.pi**2 * chi
        chiral = 2 * math.pi**2 * (2 * chi)  # tau=0, for each chirality
        rows.append(
            {
                "M": f"#_{k}(S^2 x S^2)",
                "chi": chi,
                "tau": tau,
                "lim_int_absW_squared_total_if_Vol_to_0_and_Ric_to_g": total_weyl_energy_limit,
                "lim_int_absW_plus_squared": chiral,
                "lim_int_absW_minus_squared": chiral,
                "rod_count_m=2k+2": 2 * k + 2,
                "rod_energy_8pi2_times_m": 8 * math.pi**2 * (2 * k + 2),
            }
        )
    return {
        "statement": "If ||Ric-g||_op -> 0 in dimension four and Vol -> 0, then the scalar/E terms vanish in Chern-Weil and int|W|^2 -> 8*pi^2*chi. If chi>0, bounded curvature collapse is impossible because int|W|^2 <= sup|W|^2 Vol would tend to 0. Thus positive pinched collapse on chi>0 manifolds must have curvature blow-up/bubbles.",
        "principal_circle_warning": "A closed principal S^1-bundle over a closed 3-manifold has chi=0. Since chi(S^2 x S^2)=4, S^2 x S^2 cannot be used as a principal S^1 collapse background; localized spikes in a fixed background do not themselves test collapse.",
        "rows": rows,
    }


def main() -> None:
    data = {
        "status": "ok",
        "h4_l2_particular_verification": verify_l2_particular(),
        "h4_rate_limited_flux_theorem_ledger": h4_rate_tables(),
        "weighted_beta_correction": weighted_beta_check(),
        "neck_drift_linear_counterexample_channel": {
            "mechanism": "A coherent l=2 TT Ricci-defect source of size delta across the whole ALE neck changes the normalized curvature-block/Wronskian coefficient by O(delta log(1/t)). Thus if delta log(1/t)->0 the Ozuch vector condition is necessary; if t is exponentially small in 1/delta, C^0 Ricci pinching alone does not prevent O(1) drift of the effective curvature block between the orbifold and bubble scales.",
            "realization_status": "This ledger verifies the ODE/flux scale. It does not realize the TT source as a closed smooth metric. Step 11's opposite-warping Hessian channel is the candidate realization mechanism because it changes Weyl/trace-free Hessian data while keeping Ricci small.",
            "constructive_test": "Build a neck annulus with trace-free divergence-free Ricci defect size delta on ~1/delta dyadic scales, subtract the known H2/H4 ambient tower, and check whether the l=2 block can be rotated from nondegenerate at r~1 to degenerate at r~sqrt(t).",
        },
        "alf_flux_model": alf_roots_and_flux(),
        "positive_collapse_blowup_accounting": collapse_blowup_accounting(),
        "research_consequence": {
            "proved_conditionally_on_standard_gauge_flux_setup": "For A1/EH noncollapsed bubbling, after subtracting the ambient H2/H4 tower, the Wronskian identity gives R_pm(p) zeta = 0 whenever delta_i log(1/t_i)->0. This is a rate-limited necessity theorem, not full Yau-26.",
            "open_failure_channel": "The only named escape in this model is exponentially small bubble scale t_i <= exp(-c/delta_i), where C^0 pinching permits order-one l=2 drift through the free derivative-of-Ricci/Cotton channel.",
            "next_decisive_computation": "Try to realize the coherent TT neck source by an explicit opposite-warping/KK neck metric, or compute the full tensor ALF flux for Taub-NUT/Euclidean Schwarzschild bubbles to test forced energy defect in positive collapse.",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps({
        "status": "ok",
        "output": str(OUT),
        "l2_verification": data["h4_l2_particular_verification"]["Lf_simplifies_to"],
        "beta_correction": data["weighted_beta_correction"]["formula"],
        "alf_mass_root": data["alf_flux_model"]["roots"][0],
        "collapse_warning": data["positive_collapse_blowup_accounting"]["principal_circle_warning"],
    }, indent=2))


if __name__ == "__main__":
    main()
