#!/usr/bin/env python3
"""Independent consumer-side checks for the Step-95 JSON certificate."""
from fractions import Fraction
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "data" / "step95" / "filler_lattice_screen_certificate.json"
d = json.loads(p.read_text())
assert all(d["symbolic_transfer"]["checks"].values())
r = d["root_lattice_screen"]["irreducible_tests"]
for e in ("E6", "E7", "E8"):
    assert r[e]["search"]["found"] is False
for a in range(2, 13):
    row = r[f"A{a}"]
    assert row["in_I_rank_plus_1"]["found"] is True
    assert row["in_I_rank"]["found"] is (a == 3)

rows = d["D_block_thresholds"]["single_block_D6_through_D12"]
expected = {
    "D6": (Fraction(15,16), Fraction(3675,64), 63),
    "D7": (Fraction(19,20), Fraction(32041,1040), 36),
    "D8": (Fraction(23,24), Fraction(8281,288), 36),
    "D9": (Fraction(27,28), Fraction(16641,560), 36),
    "D10": (Fraction(31,32), Fraction(271441,8576), 36),
}
for key, (cost, ac, a9) in expected.items():
    z = rows[key]
    assert Fraction(z["cost"]["numerator"], z["cost"]["denominator"]) == cost
    w = z["threshold"]["Acrit"]
    assert Fraction(w["numerator"], w["denominator"]) == ac
    assert z["threshold"]["smallest_A_multiple_of_9"] == a9

mixed = {tuple(z["blocks"]): z for z in d["D_block_thresholds"]["first_mixed_rows"]}
assert set(mixed) == {(3,8),(4,7)}
assert d["D_block_thresholds"]["first_viable_k"] == 6
assert d["D_block_thresholds"]["first_mixed_k"] == 11
assert sum(v["finite_A_viable"] for v in d["D_block_thresholds"]["exhaustive_counts"].values()) == 16049
print(json.dumps({
    "certificate": str(p),
    "symbolic_checks": "pass",
    "root_checks": "pass",
    "threshold_checks": "pass",
    "finite_A_viable_partition_count": 16049
}, indent=2))
