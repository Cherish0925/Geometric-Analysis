#!/usr/bin/env python3
"""Finite combinatorial checks for the Step 56 tame derivative allocation.

This does not prove the PDE estimates.  It exhaustively checks the derivative
budgets used after the two exceptional (m+1)-derivative allocations are
removed, and checks the Gagliardo--Nirenberg exponent-sum inequality for all
integer partitions up to a configurable order.
"""
from __future__ import annotations

import json
from itertools import product
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "step56_tame_allocation_checks.json"
MAX_M = 40
MIN_M = 7


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for tail in compositions(total - x, parts - 1):
            yield (x,) + tail


def gn_exponent_sum(qs, m):
    return sum((q - 4) / (m - 4) for q in qs if q > 4)

checks = []
failures = []

for m in range(MIN_M, MAX_M + 1):
    # Principal commutators after j=1 is treated by weighted Young.
    for j in range(2, m + 1):
        orders = (j, m - j + 2)
        ok = max(orders) <= m and sum(orders) == m + 2
        checks.append(("principal", m, orders, ok))

    # Q: D^j(weight) D^(q+1)G D^(r+1)G, j+q+r=m.
    for j, q, r in compositions(m, 3):
        orders = (j, q + 1, r + 1)
        is_top = (j == 0 and (q == m or r == m))
        if not is_top:
            ok = max(orders) <= m and sum(orders) == m + 2
            checks.append(("Q_remainder", m, orders, ok))

    # Lie: D^(j+1)(beta^2) D^(m-j+1)G. Endpoints are treated separately.
    for j in range(1, m):
        orders = (j + 1, m - j + 1)
        ok = max(orders) <= m and sum(orders) == m + 2
        checks.append(("Lie_remainder", m, orders, ok))

    # Transport: D^j(beta^2) D^(k+1)G D^(l+1)beta, j+k+l=m.
    for j, k, ell in compositions(m, 3):
        orders = (j, k + 1, ell + 1)
        is_top_metric = (j == 0 and k == m and ell == 0)
        is_top_advective = (j == 0 and k == 0 and ell == m)
        if not (is_top_metric or is_top_advective):
            ok = max(orders) <= m and sum(orders) == m + 2
            checks.append(("transport_remainder", m, orders, ok))

    # Exhaustively check GN exponent budget for 1--5 factors with sum <= m+2,
    # each factor order <=m. Factors of order <=4 use L-infinity and add zero.
    for parts in range(1, 6):
        for total in range(m + 3):
            for qs in compositions(total, parts):
                if max(qs) > m:
                    continue
                a = gn_exponent_sum(qs, m)
                ok = a <= 1 + 1e-12
                checks.append(("GN", m, qs, ok, a))

for item in checks:
    if not item[3]:
        failures.append(item)

summary = {
    "min_m": MIN_M,
    "max_m": MAX_M,
    "checks": len(checks),
    "failures": len(failures),
    "sample_failures": failures[:20],
    "interpretation": (
        "Combinatorial support only: after the explicit top allocations are removed, "
        "principal/Q/Lie/transport products have factor orders <=m and total order <=m+2; "
        "their GN interpolation exponents sum to <=1. Tensor identities and PDE existence "
        "remain mathematical arguments, not established by this script."
    ),
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps(summary, indent=2))
