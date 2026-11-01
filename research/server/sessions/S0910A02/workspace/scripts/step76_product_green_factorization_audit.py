#!/usr/bin/env python3
"""
Step 76: audit the proposed product-Green finiteness shortcut for the
(S^2 x S^2)/Z2 mixed-row second-obstruction computation.

This script is deliberately NOT a computation of Ozuch's second-obstruction
coefficients.  It records exact algebraic facts that decide whether the next
coefficient computation may replace the product Einstein-operator Green kernel
by a product of two ordinary S^2 Green functions.

Main conclusions checked here:
  * Inter-node evaluation is regular: the singular part of \bar h^4 belongs
    only to the source node.  If a source and receiver share one S^2 factor
    (adjacent nodes), the full 4D product point is still separated; any
    one-factor singularity is an artifact of an illegal factorwise inverse.
  * The inverse of a separated product operator A⊗1 + 1⊗B + C has eigenbasis
    denominators lambda_A + lambda_B + algebraic_shift.  This is not the
    product of two one-factor Green denominators.  A one-factor massive Green
    reduction is valid only after one factor has been fixed to a single
    eigenmode/eigenspace.
  * A second jet at a pole has nonzero spherical-harmonic coefficients for
    every l>=2 in the corresponding |m|=2 channel.  The T^2 selection rule
    restricts the character m but does not by itself truncate l.
  * At antipodal source/receiver positions the relevant Legendre factors have
    alternating signs (-1)^l (up to frame conventions), so closed forms or
    certified alternating-tail bounds are plausible, but they remain part of
    the coefficient computation rather than a pre-existing finite reduction.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step76_product_green_factorization_audit.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Product inverse algebra.
# ---------------------------------------------------------------------------
x, y, kappa, a, b, C = sp.symbols("x y kappa a b C")
# A product inverse coefficient of A⊗1 + 1⊗B + kappa is 1/(x+y+kappa).
# A literal product of one-factor Green functions would have coefficients
# C/((x+a)(y+b)).  Cross multiplication exposes an xy term that cannot be
# matched by a linear denominator for all x,y.
product_factorization_difference = sp.expand((x + a) * (y + b) - C * (x + y + kappa))
xy_coefficient = sp.Poly(product_factorization_difference, x, y).coeff_monomial(x * y)

# concrete coefficients for the scalar analogue on S^2 x S^2 with shift kappa=1
# and Laplacian eigenvalues l(l+1).  This is only a unit test for denominator
# structure; tensor blocks add finite algebraic curvature shifts but keep the
# additive spectral form.
def lam(l: int) -> int:
    return l * (l + 1)

sample_pairs = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 3), (5, 7)]
scalar_coeff_samples = []
for l1, l2 in sample_pairs:
    true_coeff = Fraction(1, lam(l1) + lam(l2) + 1)
    naive_product_coeff = Fraction(1, (lam(l1) + 1) * (lam(l2) + 1))
    scalar_coeff_samples.append({
        "l1": l1,
        "l2": l2,
        "additive_product_resolvent_coeff_kappa1": f"{true_coeff.numerator}/{true_coeff.denominator}",
        "naive_product_of_factor_resolvents_coeff_shift1": f"{naive_product_coeff.numerator}/{naive_product_coeff.denominator}",
        "equal": true_coeff == naive_product_coeff,
    })

# ---------------------------------------------------------------------------
# 2. Pole second-jet coefficients in one S^2 factor.
# ---------------------------------------------------------------------------
# For m=2 scalar harmonics, P_l^2(cos theta) = (1-x^2) P_l''(x) with x=cos theta.
# Near the north pole theta=0, 1-x^2 ~ theta^2 and
# P_l''(1)=(l+2)(l+1)l(l-1)/8, nonzero for every l>=2.  Thus a pole second
# jet in a |m|=2 channel has infinitely many l modes.
def Pdd_at_1(l: int) -> Fraction:
    if l < 2:
        return Fraction(0, 1)
    return Fraction((l + 2) * (l + 1) * l * (l - 1), 8)

pole_second_jet_coeffs = []
for l in range(0, 13):
    coeff = Pdd_at_1(l)
    pole_second_jet_coeffs.append({
        "l": l,
        "P_l_second_derivative_at_1": f"{coeff.numerator}/{coeff.denominator}",
        "nonzero_for_m2_second_jet": coeff != 0,
        "antipodal_second_derivative_sign_relative_to_north": (-1) ** l if coeff != 0 else 0,
    })

# The endpoint relation P_l''(-1)=(-1)^l P_l''(1) follows by differentiating
# P_l(-x)=(-1)^l P_l(x) twice.  For associated/spin-weight normalizations there
# may be additional basis signs, but the l-parity alternation is unavoidable.

# ---------------------------------------------------------------------------
# 3. Pattern/geometry implications for the node pairs.
# ---------------------------------------------------------------------------
node_pairs = {
    "adjacent_example_pNN_to_pNS": {
        "factor_1_position": "coincident (N -> N)",
        "factor_2_position": "antipodal (N -> S)",
        "full_product_distance": "pi (for unit-curvature factors)",
        "regularity": "regular as a 4D inter-node Green evaluation; no receiver singular subtraction",
        "mode_sign_schematic": "(-1)^{l2} from the antipodal factor; no alternation from the coincident factor",
        "warning": "Do not multiply a singular one-factor Green at N=N by an antipodal factor Green; the inverse denominator is additive and the full 4D kernel is smooth off the product diagonal.",
    },
    "diagonal_example_pNN_to_pSS": {
        "factor_1_position": "antipodal (N -> S)",
        "factor_2_position": "antipodal (N -> S)",
        "full_product_distance": "sqrt(2)*pi (for unit-curvature factors)",
        "regularity": "regular in both factors and in the full 4D product",
        "mode_sign_schematic": "(-1)^{l1+l2}",
        "use_as_calibration": "cleanest first case; diagonal r=2 also has the larger D8 stabilizer and the working spin-row identification",
    },
}

# ---------------------------------------------------------------------------
# 4. Safe completion criterion for the next coefficient computation.
# ---------------------------------------------------------------------------
completion_criterion = {
    "object": "Ozuch mixed-row second-obstruction coefficients on O=(S2xS2)/Z2",
    "must_output": [
        "For each independent pattern class r=1~r=3, adjacent r=2, diagonal r=2: coefficient maps for every node and every zeta in ker(R_±) in a fixed basis, including D8 transport conventions.",
        "Inter-node contribution computed from the full product P-Green/resolvent or an equivalent heat-kernel/massive-resolvent formula, not from a naive product of two massless S2 Green functions.",
        "No singular subtraction at receiver nodes j != i; singular asymptotic and source renormalization handled only at the source/self node, plus global kernel projection.",
        "The four non-TT scalar full-gauged kernel directions are explicitly sliced by L2 orthogonality or included as Ozuch v_l variables/projections.",
        "r=1 and r=3 complement/reflection systems agree; both balanced classes obey their self-conjugacy constraints; diagonal r=2 satisfies its larger stabilizer checks.",
        "If closed forms are not obtained, a certified tail bound for the remaining alternating/resolvent series is part of the output; a raw truncated spectral sum is not enough.",
    ],
    "scientific_role": "diagnostic for local nearby-orbifold desingularization/tower-rigidity on the product geometry, not a proof/refutation of P4+ or Yau-26",
}

result = {
    "scope": "factorization/regularity audit only; no Ozuch coefficient values are computed",
    "product_resolvent_algebra": {
        "true_eigenbasis_denominator": "1/(lambda_1 + lambda_2 + algebraic_curvature_shift)",
        "naive_factor_product_denominator": "C/((lambda_1+a)(lambda_2+b))",
        "symbolic_cross_multiplication_difference": str(product_factorization_difference),
        "xy_coefficient_obstruction_to_product_factorization": str(xy_coefficient),
        "conclusion": "A literal product of two one-factor Green functions is not the inverse of a sum-type product Einstein operator. Factor geometry separates variables, but inversion gives additive denominators.",
        "legitimate_one_factor_reduction": "If one factor is first projected to a single eigenvalue lambda_fixed, the remaining factor solves a massive S2 Green problem with shift lambda_fixed+algebraic_shift.",
        "scalar_unit_test_coefficients": scalar_coeff_samples,
    },
    "pole_second_jet_infinite_l_check": {
        "formula": "P_l''(1)=(l+2)(l+1)l(l-1)/8 for l>=2",
        "endpoint_parity": "P_l''(-1)=(-1)^l P_l''(1); associated/spin bases may add fixed frame signs",
        "coefficients_l_0_to_12": pole_second_jet_coeffs,
        "conclusion": "The T2 character selection |m|<=2 does not truncate l; a |m|=2 pole second-jet channel contains every l>=2.",
    },
    "node_pair_implications": node_pairs,
    "ozuch_source_anchors": {
        "source_singularity": "Ozuch Prop. 2.10 lines 608-612: bar h^4 is asymptotic to H^4+H_2^4 at the specified singular point and is solved with kernel/obstruction projections.",
        "multi_node_regular_expansion": "Ozuch lines 903-905: the sum over i' != i has expansion H_0(i)+H_2(i)+O(d(i,.)^4) at another singular point, confirming regular inter-node second-jet extraction.",
        "obstruction_equations": "Ozuch lines 770-807: exact nearby Einstein metrics force t_j lambda_k^j + t_j^2 mu_k^j = O(t_max^(5/2)).",
    },
    "completion_criterion": completion_criterion,
}

OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps({
    "output": str(OUT),
    "xy_coefficient_obstruction_to_naive_product_factorization": str(xy_coefficient),
    "m2_second_jet_nonzero_l_range_checked": "all l=2..12 nonzero; formula gives all l>=2",
    "adjacent_regular_but_not_factor_product": node_pairs["adjacent_example_pNN_to_pNS"]["warning"],
    "diagonal_first_calibration": node_pairs["diagonal_example_pNN_to_pSS"]["use_as_calibration"],
}, indent=2, ensure_ascii=False))
