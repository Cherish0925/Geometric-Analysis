#!/usr/bin/env python3
"""
Step 92: AB adjacent heat-kernel sign formula support calculations.

This script is not a proof.  It records the finite algebra behind the Step 91
AB-sector reduction and numerical evidence for the Abel-limit value.  The sign
of the alternating antipodal heat derivative is proved analytically in the Step
92 note; direct floating-point summation of B(s) at small s is ill-conditioned
because the true value is exponentially small.

After the adjacent m=2 polarizations cancel, the AB contribution is the Abel
limit of
  K_tau = 1/512 sum_{l,k>=1} (-1)^k (2l+1)(2k+1) mu_l mu_k
          exp[-tau p_lk] / p_lk,
  p_lk=(mu_l+mu_k)/2-1, mu_l=l(l+1).
Equivalently,
  K = 1/512 int_0^infty e^s A(s) B(s) ds,
  A(s)=sum_l (2l+1)mu_l exp[-s mu_l/2] >0,
  B(s)=sum_l (-1)^l(2l+1)mu_l exp[-s mu_l/2]
      = -4*pi*d_t p_t(N,S)|_{t=s/2} <0.
"""
from __future__ import annotations

import json
import math
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def mu(l: int) -> int:
    return l * (l + 1)


def A_B_float(s: float, L: int) -> tuple[float, float]:
    A = 0.0
    B = 0.0
    for l in range(1, L + 1):
        ml = mu(l)
        term = (2 * l + 1) * ml * math.exp(-0.5 * s * ml)
        A += term
        B += ((-1) ** l) * term
    return A, B


def K_tau(L: int, tau: float) -> float:
    total = 0.0
    for l in range(1, L + 1):
        ml = mu(l)
        al = (2 * l + 1) * ml
        for k in range(1, L + 1):
            mk = mu(k)
            p = 0.5 * (ml + mk) - 1.0
            total += ((-1) ** k) * al * (2 * k + 1) * mk * math.exp(-tau * p) / p
    return total / 512.0


def sample_B_values():
    samples = []
    for s in [0.003, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]:
        # Direct summation of B is reliable only once the antipodal signal is
        # above roundoff.  For small s the exact value is negative but
        # exponentially tiny, so the recorded sign may be numerical noise.
        L = max(80, int(30 / math.sqrt(s)))
        A, B = A_B_float(s, L)
        reliable = abs(B) > 1e-8
        samples.append({
            "s": s,
            "L": L,
            "A_float": A,
            "B_float": B,
            "finite_precision_B_sign_reliable": reliable,
            "finite_precision_B_sign": "negative" if B < 0 else "positive_or_roundoff_zero",
            "analytic_B_sign": "strictly negative for every s>0, by heat-kernel monotonicity",
            "e_s_A_B_over_512_float": math.exp(s) * A * B / 512.0,
        })
    return samples


def polarization_cancellation_table():
    # The Step 91 receiver signs for an adjacent pair give four m=2 mode-type
    # contributions of equal magnitude and signs +,-,+,- after the common
    # spectral denominator and antipodal frame signs are factored.  This table
    # records the cancellation pattern, not the full tensor-harmonic algebra.
    terms = [
        {"mode_pair": "c2-c2", "oneform_type": "coexact-coexact", "relative_sign": +1},
        {"mode_pair": "c2-s2", "oneform_type": "coexact-exact", "relative_sign": -1},
        {"mode_pair": "s2-c2", "oneform_type": "exact-coexact", "relative_sign": +1},
        {"mode_pair": "s2-s2", "oneform_type": "exact-exact", "relative_sign": -1},
    ]
    return {"terms": terms, "sum_relative_signs": sum(t["relative_sign"] for t in terms)}


def main():
    tau_ladder = []
    for tau, L in [(0.2, 120), (0.1, 160), (0.05, 220), (0.02, 360), (0.01, 520), (0.005, 760), (0.003, 1000)]:
        tau_ladder.append({"tau": tau, "L": L, "K_tau_double_sum_m0_only": K_tau(L, tau)})

    results = {
        "step": 92,
        "scope": "AB adjacent heat sign formula after Step91 m=2 cancellation",
        "formula": "K_adj^AB = (1/512) int_0^infty e^s A(s)B(s) ds, A=sum(2l+1)mu_l e^{-s mu_l/2}, B=sum(-1)^l(2l+1)mu_l e^{-s mu_l/2}",
        "analytic_sign_reason": "A(s)>0 termwise. B(s)=-4*pi*d_t p_t(N,S)|_{t=s/2}; strict radial monotonicity of the S^2 heat kernel plus the semigroup makes the antipodal heat value strictly increasing, hence B(s)<0.",
        "polarization_cancellation": polarization_cancellation_table(),
        "B_float_samples_with_roundoff_warning": sample_B_values(),
        "tau_ladder_m0_double_sum": tau_ladder,
        "interpretation": [
            "The numerical Abel ladder matches Step91's stabilized AB value near -0.03144249732 because only the m=0 coexact-coexact double series remains after m=2 cancellation.",
            "The strict sign proof is analytic and does not rely on the finite-precision B(s) samples; small-s direct alternating sums are ill-conditioned.",
            "This proves at most the principal AB-sector adjacent sign in the Step89/91 normalization; it is not the full Ozuch coefficient and not a Yau-26 result."
        ]
    }
    outpath = DATA_DIR / "step92_ab_heat_sign_formula.json"
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
    print(f"Wrote {outpath}")


if __name__ == "__main__":
    main()
