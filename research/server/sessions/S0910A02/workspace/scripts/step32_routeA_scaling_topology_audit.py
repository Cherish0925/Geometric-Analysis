#!/usr/bin/env python3
"""Step 32 Route-A audit for Yau Problem 26.

This is an execution/consistency script, not a proof.  It records the
calculational content forced by the Step-32 strategist correction:

1. The Page metric should not be used as a one-parameter Eguchi--Hanson
   flux experiment.  Blowing up a smooth point adds a (-1)-class; resolving
   an A1=C^2/Z2 singularity adds a (-2)-class.  CP^2#CPbar has no integral
   (-2)-class in its intersection lattice, so it cannot be the minimal
   resolution of a single A1 point.
2. The Morteza--Viaclovsky/Calabi first obstruction is scale-critical in the
   *endomorphism* norm used by Yau-26: a (0,2) term t*lambda*o over a core
   metric t*g_cal becomes an O(lambda) Ricci-endomorphism defect, whereas the
   ordinary weighted remainder becomes small.
3. A Taub/Wronskian bilinear flux, not the linear cosmological Einstein tensor
   flux, has the right dimensional scaling for the H2-H4 obstruction.  The
   balance radius is r=t^(2/3), where H_orb~r^2 and H_ALE~t^4/r^4 both have
   size t^(4/3).  On a dyadic balanced shell the delta-driven nonconservation
   scales like delta*t^4, comparable to a signal t^4 with only a delta factor.
   The older linear E_g vector flux has error delta*r^4, which at the balance
   scale gives delta*t^(8/3) and would require an artificial rate
   delta << t^(4/3) if one tried to compare to a t^4 signal.
4. If a separate theorem places branch-(b) limits in the KE/Q-Fano del Pezzo
   classification with Du Val singularities, then the expected smooth minimal
   resolutions have rational-surface intersection forms already known to carry
   some Einstein metric in all del Pezzo smooth types (FS/product, Page, CLW,
   Tian--Yau/KE for k>=3).  The script records this as a conditional topology
   audit, not as a proved implication from det R_+=0 alone.
"""
from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass, asdict
from fractions import Fraction
from typing import Dict, List, Tuple


def has_vector_of_square(form_diag: List[int], target: int, bound: int = 8) -> Dict:
    """Brute-force small search for an integral vector with given square."""
    n = len(form_diag)
    hits: List[List[int]] = []

    def rec(prefix: List[int], idx: int):
        if idx == n:
            q = sum(d * x * x for d, x in zip(form_diag, prefix))
            if q == target and any(prefix):
                hits.append(prefix.copy())
            return
        for x in range(-bound, bound + 1):
            prefix.append(x)
            rec(prefix, idx + 1)
            prefix.pop()

    rec([], 0)
    # Remove sign duplicates for display.
    canonical = []
    seen = set()
    for v in hits:
        tup = tuple(v)
        mtup = tuple(-x for x in v)
        key = min(tup, mtup)
        if key not in seen:
            seen.add(key)
            canonical.append(v)
    return {
        "form_diag": form_diag,
        "target_square": target,
        "search_bound": bound,
        "exists_in_search_box": bool(canonical),
        "examples": canonical[:8],
        "num_examples_mod_sign_displayed_limited": len(canonical),
    }


def page_topology_audit() -> Dict:
    # CP^2 # k CPbar has odd diagonal unimodular form <1> + k<-1>.
    cp2_bar1 = [1, -1]
    cp2_bar2 = [1, -1, -1]
    cp2_bar3 = [1, -1, -1, -1]
    return {
        "correction": "Page metric is on CP^2#CPbar^2 (one smooth blow-up, exceptional square -1), not a degenerating EH/A1 desingularization family.",
        "smooth_blow_up": {
            "operation": "blow up a smooth point on a complex surface",
            "lattice_effect": "orthogonal sum with <-1>",
            "exceptional_curve_square": -1,
        },
        "A1_minimal_resolution": {
            "local_model": "C^2/{±1}",
            "ALE_model": "Eguchi--Hanson on T^*S^2",
            "exceptional_curve_square": -2,
            "lattice_effect": "adds a (-2)-root/chains of ADE roots in the minimal resolution, not a lone (-1)-class",
        },
        "intersection_lattice_checks": {
            "CP2#CPbar_has_minus2_class": has_vector_of_square(cp2_bar1, -2, bound=12),
            "CP2#2CPbar_has_minus2_class": has_vector_of_square(cp2_bar2, -2, bound=4),
            "CP2#3CPbar_has_minus2_class": has_vector_of_square(cp2_bar3, -2, bound=3),
        },
        "conclusion": "The proposed Page annulus-flux test has no bubble scale t and no A1 exceptional (-2)-sphere; a null flux computation on Page would be only a consistency check for an exact rigid Einstein metric, not evidence against Route A.",
    }


def mv_obstruction_scaling(lambda_abs: float = 1.0, spread_o: float = 2.0) -> Dict:
    # In core metric g_t=t*g_cal: |t lambda o|_op,g_t = |lambda| |g_cal^{-1}o|.
    # Distance to any scalar multiple is half spectral spread.
    scalar_distance_constant = lambda_abs * spread_o / 2.0
    samples = []
    for t in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
        rho_core = 1.0
        rho_transition = t ** (-Fraction(1, 4))
        rem_core = t * rho_core**2
        rem_transition = t * float(rho_transition) ** 2  # = t^(1/2)
        defect_lower = max(0.0, scalar_distance_constant - rem_core)
        samples.append({
            "t": t,
            "rho_transition=t^{-1/4}": float(rho_transition),
            "remainder_core_op_scale=t": rem_core,
            "remainder_transition_op_scale=t*rho^2=t^{1/2}": rem_transition,
            "first_obstruction_op_distance_from_scalars": scalar_distance_constant,
            "core_lower_bound_after_remainder_model": defect_lower,
        })
    return {
        "model_estimate": "Ric(g_t)-Lambda g_t-t*lambda*chi_t*o = O_{g_cal}(t^2 rho^2), g_t~t g_cal on the Calabi/EH core.",
        "operator_norm_conversion": "A (0,2)-tensor norm/endomorphism size scales by t^{-1}; hence t*lambda*o becomes lambda*(g_cal^{-1}o), while O(t^2 rho^2) becomes O(t rho^2).",
        "non_scalar_distance": "inf_a ||lambda*g_cal^{-1}o - a Id||_op = |lambda|*(spectral spread of g_cal^{-1}o)/2.",
        "assumed_spread_for_display": spread_o,
        "samples": samples,
        "conclusion": "Within a gluing normal form with nonzero first obstruction coefficient, Yau26's pointwise Ricci-endomorphism pinching cannot tend to zero. Weighted or L^p smallness misses this scale-critical core defect.",
    }


def flux_dimensional_scaling() -> Dict:
    rows = []
    for t in [1e-1, 1e-2, 1e-3, 1e-4, 1e-6]:
        r_balance = t ** (2.0 / 3.0)
        H2 = r_balance**2
        H4 = t**4 / r_balance**4
        signal = t**4
        vol_shell = r_balance**4
        # Dyadic shell estimates with unit constants.
        residual_pair_H2 = H2 * vol_shell      # delta multiplier omitted
        residual_pair_H4 = H4 * vol_shell      # delta multiplier omitted = t^4
        linear_Eg_error = r_balance**4         # delta multiplier omitted
        rows.append({
            "t": t,
            "r_balance=t^(2/3)": r_balance,
            "H2_size=r^2": H2,
            "t4H4_size=t^4/r^4": H4,
            "Wronskian_signal_scale": signal,
            "delta_bulk_pair_with_H2_no_delta": residual_pair_H2,
            "delta_bulk_pair_with_t4H4_no_delta": residual_pair_H4,
            "ratio_pair_H2_to_signal": residual_pair_H2 / signal,
            "ratio_pair_H4_to_signal": residual_pair_H4 / signal,
            "linear_Eg_vector_flux_error_no_delta=r^4": linear_Eg_error,
            "linear_Eg_error_to_signal_ratio_no_delta": linear_Eg_error / signal,
            "rate_needed_for_linear_Eg_delta_less_signal": f"delta << {linear_Eg_error / signal:.3g}^(-1) i.e. delta << t^(4/3)",
        })
    return {
        "local_expansions": {
            "orbifold_2jet_size": "|H_2| ~ r^2, |∂H_2| ~ r",
            "ALE_rminus4_size": "|t^4 H^4| ~ t^4 r^{-4}, |∂(t^4 H^4)| ~ t^4 r^{-5}",
            "boundary_area": "~ r^3",
        },
        "Wronskian_boundary_signal": "area*(H2*∂H4 - H4*∂H2) ~ r^3*(r^2*t^4*r^{-5}) ~ t^4 (and similarly for the other term), independent of r.",
        "balance_radius": "r^2 = t^4/r^4 => r=t^(2/3); at this radius |H2|=|t^4H4|=t^(4/3).",
        "delta_nonconservation_on_dyadic_balanced_shell": "If the residual is only ||Ric-g||_op<=delta, pairing with the natural linearized modes gives delta*∫|H2| or delta*∫|t^4H4| ~ delta*t^4. Thus exponent a=6 in delta*r^a, since r^6=t^4 at balance.",
        "computed_exponent_a": 6,
        "caution": "Across a long neck, pairing with t^4 r^{-4} over all dyadic shells can introduce logarithmic/summability issues; the rate-free statement is safest for a localized balanced-shell or genuinely conserved bilinear Wronskian identity.",
        "why_linear_Eg_is_wrong_object": "The vector-field cosmological Einstein tensor flux has bulk scale delta*r^4 for Z~r, L_Z g~1. At r=t^(2/3) this is delta*t^(8/3), larger than t^4 unless delta<<t^(4/3), and in any case it is linear and blind to the H2-H4 Taub cross term.",
        "samples": rows,
    }


@dataclass
class DelPezzoTopology:
    name: str
    intersection_form: str
    smooth_type: str
    known_einstein_status: str
    route_relevance: str


def del_pezzo_topology_audit() -> Dict:
    # Smooth del Pezzo topological menu over C: CP2, CP1xCP1, CP2#k CPbar for 1<=k<=8.
    entries = [
        DelPezzoTopology("degree 9", "<1>", "CP^2", "Fubini--Study Kähler--Einstein", "already Einstein"),
        DelPezzoTopology("degree 8 split", "H", "CP^1 x CP^1", "product Kähler--Einstein", "already Einstein"),
        DelPezzoTopology("degree 8 blow-up", "<1>⊕<-1>", "CP^2#CPbar", "Page positive Einstein, non-Kähler but conformally Kähler", "fills the no-KE-but-Einstein gap"),
        DelPezzoTopology("degree 7", "<1>⊕2<-1>", "CP^2#2CPbar", "Chen--LeBrun--Weber positive Einstein, non-Kähler but conformally Kähler", "fills the second no-KE-but-Einstein gap"),
        DelPezzoTopology("degrees 1--6", "<1>⊕k<-1>, 3<=k<=8", "CP^2#kCPbar in general-position del Pezzo smooth types", "Tian--Yau / del Pezzo Kähler--Einstein existence for the stable cases; source-grade details still to be read for every singular smoothing case", "suggests all smooth del Pezzo minimal resolutions carry some Einstein metric"),
    ]
    return {
        "conditional_if_branch_b_is_KE_Q_Fano_DuVal": [asdict(e) for e in entries],
        "important_limits": [
            "det R_+=0 alone is only an algebraic first-obstruction condition and does not imply Hermitian or Kähler geometry.",
            "LeBrun--Ozuch Theorem B, per the dossier, assumes an exact positive Einstein sequence, Hermitian Einstein orbifold limit, a genuine singularity, and ASD Ricci-flat ALE bubbles. It cannot yet be applied to arbitrary C^0-pinched branch-(b) sequences.",
            "Minimal resolutions of Du Val points are crepant; -K becomes nef rather than ample, so the natural KE metric on the singular Q-Fano does not automatically lift to a KE metric on the smooth resolution. Yau26 only needs some Einstein metric, and Page/CLW show non-KE Einstein metrics can fill low-degree gaps.",
            "The Ozuch 2020 T^4/Z2 chessboard family is Lambda=0/K3-compatible evidence; it should not be carried as a positive Lambda counterexample locus without sign-specific checking.",
        ],
        "route_value": "The classification bypass is potentially cheaper than A2: list KE orbifold limits with A1/Du Val singularities, compute their smooth minimal-resolution topologies, and check whether each topology already has a known Riemannian Einstein metric. If yes, noncollapsed branch-(b) closes within that classified subcase without proving ansatz-independent A2.",
    }


def main() -> None:
    result = {
        "title": "Step 32 Route-A scaling/topology audit",
        "scope": "Execution-level consistency checks and dimensional scaling; not a proof or refutation of Yau-26.",
        "page_model_correction": page_topology_audit(),
        "obstruction_amplitude_scaling": mv_obstruction_scaling(),
        "bilinear_flux_dimensional_scaling": flux_dimensional_scaling(),
        "classification_topology_audit": del_pezzo_topology_audit(),
        "route_decision": [
            "Do not perform the Page annular E_g-flux experiment as a test of A2: Page is rigid and not an A1/EH degeneration family.",
            "A2/amplitude should be reconnected to the Step-1/Step-7 core-defect scaling. The missing theorem is ansatz-independence/normal-form entry for arbitrary C^0 Ricci-pinched degenerations, not a numerical detection test on exact Einstein examples.",
            "If a flux bridge is pursued, use a bilinear Taub/Wronskian identity at or localized near the balance radius r=t^(2/3); the old linear cosmological E_g flux has the wrong order for the H2-H4 obstruction.",
            "In parallel, pursue the classification bypass for the branch-(b) KE/Hermitian exact-Einstein subcase, but keep its hypotheses explicit and do not infer Kähler from det R_+=0 alone.",
        ],
    }
    out = "Sessions/S0910A02/workspace/data/step32_routeA_scaling_topology_audit.json"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nSaved to {out}")


if __name__ == "__main__":
    main()
