#!/usr/bin/env python3
"""
Step 91: exact scalar-excess accounting for hyperbolic connected sums
and the BBCG multiplicative-gap dependence.

This is not a proof assistant artifact.  It is a reproducible algebra/ledger
script to prevent normalization drift in the Yau-26 negative-branch analysis.
"""
import json
import math
from pathlib import Path

PI = math.pi


def eps_threshold_bcg_cgb(chi):
    """Previous BCG+CGB contradiction threshold for relative epsilon in Ric≈-3(1±eps)."""
    r = math.sqrt(1.0 - 1.0 / chi)
    return (1.0 - r) / (1.0 + r)


def eps_threshold_scalar_excess_positive(chi):
    """Threshold making 6 V_BCG_lower - 8π² χ(M) positive (ignoring E/W)."""
    return math.sqrt(chi / (chi - 1.0)) - 1.0


def scalar_base_lower(chi, delta):
    """Lower bound for 6Vol - 8π²χ(M) from BCG after scaling.

    Here N is hyperbolic with Euler chi, M=N#N, and |Ric+3g|_op<=delta.
    eps=delta/3; Vol_g >= 2Vol(N)/(1+eps)^2.
    chi(M)=2chi-2, Vol(N)=4π² chi/3.
    """
    eps = delta / 3.0
    return 16 * PI**2 * (1.0 - chi * (2 * eps + eps**2) / (1 + eps) ** 2)


def scalar_base_lower_with_uniform_gap(chi, delta, eps0):
    """If a uniform BBCG-type gap Vol_hat >= 2(1+eps0) Vol(N) existed."""
    eps = delta / 3.0
    return 16 * PI**2 * ((1 + eps0) * chi / (1 + eps) ** 2 - chi + 1)


def plus_volume_lower_from_integral(integral_u_lower, delta):
    """Since u<=4δ pointwise, positive integral forces positive-u volume."""
    if integral_u_lower <= 0:
        return 0.0
    return integral_u_lower / (4.0 * delta)


def main():
    out = {
        "normalization": {
            "metric_condition": "||Ric_g + 3 g||_op,g <= delta",
            "eigenvalues": "Ric eigenvalues = -3 + eta_i with |eta_i| <= delta",
            "scalar_excess": "s = -12 + u, u=sum eta_i, so |u| <= 4 delta",
            "cgb_identity": (
                "8*pi^2*chi(M) = int |W|^2 + 6 Vol - int u "
                "+ int u^2/24 - (1/2) int |E|^2"
            ),
            "rearranged": (
                "int u = 6 Vol - 8*pi^2*chi(M) + int |W|^2 "
                "+ int u^2/24 - (1/2) int |E|^2"
            ),
            "bcg_scaling": (
                "Ric_g >= -(3+delta)g.  Set eps=delta/3 and ghat=(1+eps)g; "
                "then Ric_ghat=Ric_g >= -3 ghat and Vol(ghat)=(1+eps)^2 Vol(g)."
            )
        },
        "M_equals_N_connected_sum_N": {
            "chi_M": "2*chi_N - 2",
            "vol_N_hyp": "(4*pi^2/3)*chi_N",
            "BCG_lower_after_rescaling": "Vol_g(M) >= 2 Vol(N)/(1+delta/3)^2",
            "base_scalar_lower": (
                "6 Vol_g - 8*pi^2 chi(M) >= "
                "16*pi^2 * [1 - chi_N*(2eps+eps^2)/(1+eps)^2], eps=delta/3"
            ),
            "full_integral_lower": (
                "int u >= base_scalar_lower + int|W|^2 - (1/2)int|E|^2 + int u^2/24"
            ),
            "diffuseness_fixed_N": (
                "For fixed N and delta->0, Vol({s>-12}) >= "
                "(16*pi^2 + int|W|^2 - o(1))/(4 delta); in particular topology change cannot be localized."
            ),
            "nonuniform_slack": (
                "For varying N, the base term contains -O(delta*chi_N).  If delta*chi_N is not small, "
                "this accounting alone may give no positive scalar-excess lower bound; a refuting sequence only needs delta_i->0."
            )
        },
        "thresholds": [],
        "uniform_multiplicative_gap_if_available": {
            "hypothesis": "For all closed hyperbolic N, every Ric>=-3 metric on N#N has Vol >= 2(1+eps0)Vol(N) with eps0 independent of N.",
            "base_scalar_lower": "16*pi^2 * [ (1+eps0)*chi_N/(1+delta/3)^2 - chi_N + 1 ]",
            "large_chi_positive_when": "delta < 3*(sqrt(1+eps0)-1) = (3/2)eps0 + O(eps0^2)",
            "research_status": "BBCG Cor. 1.7 supplies eps for fixed X; Theorem 1.3/1.6 constants depend on diam(X), and the introduction says size/diameter dependence is necessary in related finite-cover examples."
        },
        "sample_values": []
    }

    for chi in [2, 10, 100, 1000, 10000]:
        eps1 = eps_threshold_bcg_cgb(chi)
        eps2 = eps_threshold_scalar_excess_positive(chi)
        out["thresholds"].append({
            "chi_N": chi,
            "eps_BCG_CGB_contradiction": eps1,
            "delta_BCG_CGB_contradiction": 3 * eps1,
            "asymptotic_eps_BCG_CGB_times_chi": eps1 * chi,
            "eps_scalar_base_positive": eps2,
            "delta_scalar_base_positive": 3 * eps2,
            "asymptotic_eps_scalar_times_chi": eps2 * chi,
        })

    for chi, delta in [(10, 0.01), (10, 0.1), (100, 0.001), (100, 0.01), (1000, 0.001), (1000, 0.01)]:
        base = scalar_base_lower(chi, delta)
        out["sample_values"].append({
            "chi_N": chi,
            "delta": delta,
            "delta_times_chi": delta * chi,
            "base_scalar_lower_over_pi2": base / PI**2,
            "plus_volume_lower_if_EW_terms_ignored": plus_volume_lower_from_integral(base, delta),
            "plus_volume_lower_over_1_delta": plus_volume_lower_from_integral(base, delta) * delta,
        })

    out_path = Path("Sessions/S0910A02/workspace/data/step91_scalar_excess_bbcg_gap.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Saved {out_path}")
    print("Correct BCG scale: ghat=(1+delta/3) g, not its inverse.")
    print("Fixed N: int u has 16π² leading scalar-excess budget; positive-u volume is Ω(1/delta).")
    print("Varying N: base budget loses O(delta*chi_N); no uniform obstruction without a uniform multiplicative BBCG gap.")
    for row in out["thresholds"][:4]:
        print(f"chi={row['chi_N']:5d}: delta_BCG_CGB≈{row['delta_BCG_CGB_contradiction']:.6g}, delta_scalar_positive≈{row['delta_scalar_base_positive']:.6g}")


if __name__ == "__main__":
    main()
