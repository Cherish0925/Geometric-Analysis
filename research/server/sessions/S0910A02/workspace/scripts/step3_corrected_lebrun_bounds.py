#!/usr/bin/env python3
"""
Step 3 correction for the dimension-four LeBrun/Ishida-LeBrun curvature
estimates used in the Yau Problem 26 negative-branch analysis.

This script is not a proof of Yau26. It is a reproducible algebra/numerical
check of the constants after the Step 2 factor error was found.

Notation:
  M = X # k CPbar^2, A = c1^2(X), p = k/A, C = 2χ+3τ = A-k.
  A δ_- pinched metric satisfies |Ric + g|_op <= δ (after normalization).
  E = trace-free Ricci r̊, W2 = ∫|W+|^2.

Main checks:
  1. Correct Einstein CGB factor gives LeBrun 1996 threshold k > 2A/3
     from the scalar estimate, not k < A.
  2. The mixed LeBrun Proposition 4 estimate plus pinching gives
        δ/(1-δ) >= sqrt((p - 1/3)/2) for p > 1/3.
  3. The direct upper-bound optimization for
        ∫(s - sqrt(6)|W+|)^2
     under δ=0 CGB constraints saturates exactly at p=1/3.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def delta_mixed_lower_bound(p: float) -> float:
    """δ lower bound from mixed SW + CGB for p=k/A."""
    if p <= 1.0 / 3.0:
        return 0.0
    t = math.sqrt((p - 1.0 / 3.0) / 2.0)
    return t / (1.0 + t)


def beta(delta: float) -> float:
    """Bδ = lower bound for s^2/24 - |E|^2/2 per unit volume."""
    return (2.0 / 3.0) * (1.0 - delta) ** 2 - 2.0 * delta**2


def refined_F_over_pi2C(x: float, delta: float) -> float:
    """
    Upper-bound objective F/(π² C) for L = ∫(s-sqrt(6)|W+|)^2.

    x = V/(π² C), W2/(π²C)=2 - beta*x/2.
    Valid for 0 <= x <= 4/beta(delta), beta>0.
    """
    b = beta(delta)
    y = 2.0 - 0.5 * b * x
    if x < 0 or y < -1e-12 or b <= 0:
        return float("-inf")
    y = max(0.0, y)
    r = 1.0 + delta
    return 16.0 * r * r * x + 8.0 * math.sqrt(6.0) * r * math.sqrt(max(0.0, x * y)) + 6.0 * y


def maximize_refined_F(delta: float) -> tuple[float, float]:
    """Golden-section maximize refined_F over x in [0, 4/beta]."""
    b = beta(delta)
    if b <= 0:
        return float("inf"), float("nan")
    lo, hi = 0.0, 4.0 / b
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c = hi - gr * (hi - lo)
    d = lo + gr * (hi - lo)
    fc = refined_F_over_pi2C(c, delta)
    fd = refined_F_over_pi2C(d, delta)
    for _ in range(200):
        if fc < fd:
            lo = c
            c = d
            fc = fd
            d = lo + gr * (hi - lo)
            fd = refined_F_over_pi2C(d, delta)
        else:
            hi = d
            d = c
            fd = fc
            c = hi - gr * (hi - lo)
            fc = refined_F_over_pi2C(c, delta)
    x = 0.5 * (lo + hi)
    return refined_F_over_pi2C(x, delta), x


def pcrit_from_refined(delta: float) -> float:
    """
    If p > pcrit(delta), then even the refined upper bound is below the
    LeBrun lower bound 72π²A, so δ-pinching is impossible.
    Necessary condition for existence: (1-p)Fmax(delta) >= 72.
    """
    Fmax, _ = maximize_refined_F(delta)
    if not math.isfinite(Fmax) or Fmax <= 0:
        return float("nan")
    return 1.0 - 72.0 / Fmax


def invert_refined_for_p(p: float) -> float:
    """Smallest δ (by refined upper-bound test) not immediately excluded."""
    if p <= 1.0 / 3.0:
        return 0.0
    # beta positive only for δ < 1/(1+sqrt(3)). This is the CGB pinching window.
    hi = 1.0 / (1.0 + math.sqrt(3.0)) - 1e-12
    lo = 0.0
    # pcrit increases with delta in the tested range; bisection is adequate.
    if pcrit_from_refined(hi) < p:
        return float("nan")
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if pcrit_from_refined(mid) >= p:
            hi = mid
        else:
            lo = mid
    return hi


def corrected_einstein_threshold_examples() -> list[dict]:
    """Compute W2 upper coefficient under the corrected Einstein formula."""
    rows = []
    for p in [0.25, 1/3, 0.5, 2/3, 0.7, 0.9]:
        # For Einstein and scalar SW λ²V > 2π²A when k>0,
        # W2 < π² A * (4/3 - 2p). The formal coefficient is negative
        # for p>2/3, and endpoint p=2/3 is still contradictory because
        # the source inequality is strict, giving W2<0 rather than W2<=0.
        coeff = 4.0 / 3.0 - 2.0 * p
        tol = 1e-12
        contradiction = p >= 2.0 / 3.0 - tol
        rows.append({
            "p": p,
            "Wplus2_strict_upper_coeff_pi2A": coeff,
            "contradiction_by_scalar_estimate": contradiction,
            "endpoint_uses_strictness": abs(p - 2.0 / 3.0) <= tol,
        })
    return rows


def main() -> None:
    out_dir = Path("Sessions/S0910A02/workspace/data")
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Corrected Step 3 LeBrun/Ishida-LeBrun algebra checks")
    print("=" * 72)
    print("Einstein CGB: 8π²C = 4∫|W+|² + (4/3)λ²V")
    print("Thus ∫|W+|² = 2π²C - (1/3)λ²V, not 2π²C - (4/3)λ²V.")
    print()

    print("Corrected scalar-only Einstein threshold:")
    for row in corrected_einstein_threshold_examples():
        print(
            f"  p={row['p']:.6f}: W2 < π²A*{row['Wplus2_strict_upper_coeff_pi2A']:.6f}; "
            f"contradiction={row['contradiction_by_scalar_estimate']}"
            f" endpoint_strict={row['endpoint_uses_strictness']}"
        )
    print("  Contradiction holds for p=k/A>=2/3; the endpoint uses LeBrun strictness.")
    print()

    print("Mixed SW pinching lower bound δ/(1-δ) >= sqrt((p-1/3)/2):")
    for p in [1/3, 0.34, 0.40, 0.50, 0.60, 2/3, 0.70, 0.80, 0.90]:
        print(f"  p={p:.6f}: δ >= {delta_mixed_lower_bound(p):.9f}")
    print()

    print("Refined upper-bound optimization for ∫(s-√6|W+|)^2:")
    rows = []
    for d in [0.0, 0.01, 0.02, 0.05, 0.10, 0.20, 0.28, 0.34]:
        Fmax, xstar = maximize_refined_F(d)
        pc = pcrit_from_refined(d)
        rows.append({"delta": d, "Fmax_over_pi2C": Fmax, "xstar_V_over_pi2C": xstar, "pcrit": pc})
        print(f"  δ={d:.3f}: Fmax/(π²C)={Fmax:.9f}, x*={xstar:.9f}, pcrit={pc:.9f}")
    print("  At δ=0, Fmax=108 and pcrit=1/3 exactly (numerically).")
    print()

    print("Compare mixed-simple and refined-optimization δ thresholds:")
    compare = []
    for p in [0.34, 0.36, 0.40, 0.50, 0.60, 2/3, 0.80]:
        dm = delta_mixed_lower_bound(p)
        dr = invert_refined_for_p(p)
        compare.append({"p": p, "delta_mixed_simple": dm, "delta_refined_opt": dr})
        print(f"  p={p:.6f}: mixed δ>={dm:.9f}; refined-opt δ>={dr:.9f}")

    result = {
        "corrected_einstein_threshold": corrected_einstein_threshold_examples(),
        "mixed_bound_samples": [{"p": p, "delta_lb": delta_mixed_lower_bound(p)} for p in [0.34, 0.4, 0.5, 0.6, 2/3, 0.8]],
        "refined_optimization_samples": rows,
        "comparison": compare,
        "conclusion": (
            "Step 2's all-k<A negative-Einstein exclusion and 1/sqrt(A) route were artefacts. "
            "Scalar-only LeBrun gives the literature k/A>2/3 threshold; mixed Prop4 gives a "
            "pinching lower bound depending only on p=k/A and rules out δ->0 for fixed p>1/3. "
            "Only p->1/3+ remains visible to these integral inequalities."
        ),
    }
    path = out_dir / "step3_corrected_lebrun_bounds.json"
    path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print()
    print(f"Saved JSON summary to {path}")


if __name__ == "__main__":
    main()
