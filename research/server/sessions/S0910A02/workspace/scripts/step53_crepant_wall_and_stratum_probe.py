#!/usr/bin/env python3
"""
Step 53 probe for the Yau-26 Ricci-pinching project.

This script records two arithmetic/scaling tests:

1. Four-dimensional negative ADE wall: crepant ADE/Kronheimer bubbles preserve
   c1^2 and therefore do not create the LeBrun/Ishida-LeBrun nonexistence
   deficit, while non-crepant (-1)-blowup/Burns pieces create the deficit but
   are not Ricci-flat, so they are not admissible first-order Ricci-pinched
   bubbles.
2. A bounded n>=5 codimension-four stratum scaling probe: a naive integral
   obstruction along a singular stratum is too weak for C^0 operator pinching;
   a nonzero first-obstruction coefficient or O(1) variation of ALE parameters
   along the stratum is visible pointwise in the core.

The script is not a theorem prover. It produces a JSON ledger of exact algebraic
formulas and finite sample values used in the Step 53 research note.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[2]  # Sessions/S0910A02
DATA = ROOT / "workspace" / "data"
DATA.mkdir(parents=True, exist_ok=True)


def lebrun_gap(p: Fraction) -> dict:
    """Return the Step-3 stable Ricci-pinching lower bound for p=k/A.

    The bound applies in the single blow-up LeBrun setup for p>1/3:
        delta/(1-delta) >= sqrt((p-1/3)/2).
    """
    threshold = Fraction(1, 3)
    if p <= threshold:
        return {
            "p": str(p),
            "applies": False,
            "reason": "p <= 1/3, no strict mixed LeBrun margin",
        }
    q = (p - threshold) / 2
    root = math.sqrt(float(q))
    delta = root / (1.0 + root)
    return {
        "p": str(p),
        "applies": True,
        "sqrt_term": f"sqrt(({p}-1/3)/2)",
        "delta_lower_bound_numeric": delta,
    }


def burns_metric_check() -> dict:
    """Symbolic check for the standard Burns Kähler potential on C^2\{0}.

    With potential phi(s)=s+log(s), s=|z|^2, the complex Hessian has determinant
    det(g)=phi'(s)^(m-1)(phi'(s)+s phi''(s)); for m=2 this is 1+1/s.  The Ricci
    form is -i partial partialbar log det(g), so it is nonzero because det(g) is
    not constant.  The metric is scalar-flat in complex dimension 2 but not
    Ricci-flat.
    """
    # Evaluate a radial derivative of log(1+1/s) at a sample point to show nonzero.
    s = 2.0
    # f(s)=log(1+1/s); f'(s)= -1/(s(s+1))
    fp = -1.0 / (s * (s + 1.0))
    return {
        "potential": "phi(s)=s+log(s), s=|z|^2, complex dimension 2",
        "det_formula": "det(g_{i\u0304j})=(1+1/s)",
        "ricci_form": "rho=-i partial partialbar log(1+1/s)",
        "sample_f_prime_at_s=2": fp,
        "ricci_flat": False,
        "scalar_flat_kahler": True,
        "pinching_scaling_consequence": (
            "If a scaled Burns core is t*g_Burns, its nonzero Ricci endomorphism "
            "scales like t^{-1}; hence a Burns (-1)-bubble cannot be hidden in "
            "a sequence with ||Ric+g||_op -> 0 by the same Ricci-flat ALE mechanism."
        ),
    }


def four_dimensional_wall_table() -> list[dict]:
    samples = []
    # Crepant ADE resolution: no non-crepant blowup count k.
    for A in [3, 12, 24, 96]:
        samples.append({
            "model": "crepant ADE/Kronheimer resolution of a negative KE canonical orbifold",
            "A=c1^2_canonical": A,
            "noncrepant_blowups_k": 0,
            "p=k/A": "0",
            "c1_square_after_resolution": A,
            "first_obstruction": "Kähler chirality has rank-one curvature block, so kernel directions can kill R_± zeta locally",
            "known_LeBrun_nonexistence_margin": lebrun_gap(Fraction(0, 1)),
            "interpretation": "compatible with Ricci-flat ALE pinching but not reached by LeBrun blow-up nonexistence theorem",
        })
    # Blowup/noncrepant samples at and above threshold.
    for p in [Fraction(1, 3), Fraction(2, 5), Fraction(2, 3), Fraction(1, 1)]:
        A = 120
        k = int(p * A)
        samples.append({
            "model": "noncrepant (-1)-blowup/Burns topology over a smooth point",
            "A=c1^2_minimal": A,
            "noncrepant_blowups_k": k,
            "p=k/A": str(p),
            "c1_square_after_blowup": A - k,
            "known_LeBrun_nonexistence_margin": lebrun_gap(p),
            "local_pinching_bubble": "Burns is scalar-flat Kähler but not Ricci-flat; local Ricci operator is order t^{-1} after scaling",
            "interpretation": "creates known Einstein nonexistence margin when p>=1/3, but is not an admissible Ricci-flat ALE bubble for ||Ric+g||_op -> 0",
        })
    return samples


def stratum_probe() -> dict:
    """Return a bounded structural n>=5 codim-4 stratum probe."""
    return {
        "local_model": "codimension-four orbifold stratum S^m with normal cone R^4/Gamma and ALE replacement X_Gamma",
        "operator_norm_locality": (
            "Yau-26 pinching is a C^0 pointwise operator norm; a first obstruction "
            "coefficient that is nonzero at any stratum point gives an O(1) Ricci "
            "endomorphism defect on the corresponding core, so integration over S cannot cancel it."
        ),
        "expected_first_obstruction_form": (
            "bundle-valued pointwise/elliptic condition along S: R_normal,±(y) zeta(y) plus "
            "possible normal-connection/tangential derivative terms must vanish, rather than only an integral condition"
        ),
        "variation_warning_model": {
            "warped_product_metric": "dy^2 + a(y)^2 dx^2",
            "sectional_curvature": "K=-a''(y)/a(y)",
            "scaling_message": (
                "multiplying the fiber metric by a small constant does not suppress curvature produced by O(1) variation of the fiber parameter along y; "
                "analogously, ALE parameters over a stratum must be parallel/slow in a scale-correct gauge or create visible mixed curvature"
            ),
        },
        "bounded_verdict": (
            "The n>=5 stratum idea has content, but the naive stratum-integral obstruction is too weak. "
            "The correct probe is existence/classification of nonzero parallel or elliptic kernel sections in the ALE obstruction bundle over each codim-4 stratum, with pointwise normal curvature block constraints."
        ),
        "does_not_solve": "no all-dimensional Yau-26 branch follows from this bounded probe",
    }


result = {
    "four_dimensional_negative_ADE_wall": {
        "principle": (
            "Known LeBrun/Ishida-LeBrun nonexistence is generated by non-crepant topology "
            "(blowups or connected-sum deficit). Ricci-pinched ALE gluing naturally uses Ricci-flat "
            "Kronheimer/ADE crepant bubbles, which preserve c1^2. The two mechanisms therefore miss each other."
        ),
        "table": four_dimensional_wall_table(),
        "burns_check": burns_metric_check(),
    },
    "n_ge_5_codim4_stratum_probe": stratum_probe(),
}

out = DATA / "step53_crepant_wall_and_stratum_probe.json"
out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({
    "status": "ok",
    "output": str(out.relative_to(ROOT)),
    "num_table_rows": len(result["four_dimensional_negative_ADE_wall"]["table"]),
    "burns_ricci_flat": result["four_dimensional_negative_ADE_wall"]["burns_check"]["ricci_flat"],
    "stratum_verdict": result["n_ge_5_codim4_stratum_probe"]["bounded_verdict"],
}, indent=2))
