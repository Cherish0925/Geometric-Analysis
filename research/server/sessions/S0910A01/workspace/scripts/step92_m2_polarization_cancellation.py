#!/usr/bin/env python3
"""
Step 92: exact 2x2 Hessian/star matrix proof for adjacent m=2 AB cancellation.

The calculation is finite and integral.  It supports the written proof in
step92_route_comparison_and_ab_heat_sign.md.  It does not include the actual ALE
source normalization or the AA/BB tensor sectors.
"""
from __future__ import annotations

import json
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# matrices as tuples for exact integer arithmetic
C = ((1, 0), (0, -1))
S = ((0, 1), (1, 0))
J = ((0, -1), (1, 0))


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def scale(a, A):
    return tuple(tuple(a * A[i][j] for j in range(2)) for i in range(2))


def receiver(A, B):
    # omit the common factor -1/2; record numerator - (A01 B10 + A10 B01)
    return -(A[0][1] * B[1][0] + A[1][0] * B[0][1])


def deriv(kind, H):
    return H if kind == "exact" else matmul(J, H)

# At a south-pole adjacent source in the B factor, c2 gets (-1)^k and s2 gets -(-1)^k.
# We factor out the common (-1)^k, so source_sign(c)=+1, source_sign(s)=-1.
source_mode_sign = {"c": 1, "s": -1}
H = {"c": C, "s": S}

terms = []
for mode_A, kind_A, mode_B, kind_B in [
    ("c", "coexact", "c", "coexact"),
    ("c", "coexact", "s", "exact"),
    ("s", "exact", "c", "coexact"),
    ("s", "exact", "s", "exact"),
]:
    A_rec = deriv(kind_A, H[mode_A])
    B_rec = deriv(kind_B, H[mode_B])
    R_rec_num = receiver(A_rec, B_rec)
    # A source is at the same pole, B source at the adjacent antipodal pole.
    A_src = A_rec
    B_src = scale(source_mode_sign[mode_B], B_rec)
    R_src_num_without_common_l_parity = receiver(A_src, B_src)
    terms.append({
        "mode_A": mode_A,
        "kind_A": kind_A,
        "mode_B": mode_B,
        "kind_B": kind_B,
        "A_derivative": A_rec,
        "B_derivative": B_rec,
        "R_receiver_numerator_without_half": R_rec_num,
        "R_source_numerator_without_half_and_without_common_(-1)^k": R_src_num_without_common_l_parity,
        "relative_product_sign": (1 if R_rec_num * R_src_num_without_common_l_parity > 0 else -1 if R_rec_num * R_src_num_without_common_l_parity < 0 else 0),
    })

results = {
    "step": 92,
    "scope": "finite exact m=2 adjacent AB polarization cancellation",
    "matrices": {
        "C": C,
        "S": S,
        "J": J,
        "J*C": matmul(J, C),
        "J*S": matmul(J, S),
    },
    "receiver_numerator": "-(A_01 B_10 + A_10 B_01), common factor 1/2 omitted",
    "terms": terms,
    "sum_relative_product_signs": sum(t["relative_product_sign"] for t in terms),
    "cancellation_verified": sum(t["relative_product_sign"] for t in terms) == 0,
    "interpretation": "After common degree-dependent amplitudes, denominator, heat factor, norm, and common (-1)^k antipodal parity are factored, the four m=2 adjacent polarizations have signs +,-,+,- and cancel mode by mode.",
}

outpath = DATA_DIR / "step92_m2_polarization_cancellation.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
print(f"Wrote {outpath}")
