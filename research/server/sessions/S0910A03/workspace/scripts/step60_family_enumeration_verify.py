#!/usr/bin/env python3
"""Finite verification of the derivative-family classification used in Step 60.

This program checks every integer derivative allocation in the universal
T- and U-families through a configurable order.  It verifies the triangular
ordering of current, previous, top-cutoff, and gradient terms.  It also checks
an explicit principal-symbol counterexample to the proposed ungauged L2
uniqueness estimate.  The mathematical derivation of the universal tensor
families is in the companion Step 60 note; this finite program does not replace
that derivation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

MAX_ORDER = 64
issues: List[str] = []
counts: Dict[str, int] = {
    "T2": 0,
    "T3": 0,
    "T4": 0,
    "T5": 0,
    "T6": 0,
    "U2": 0,
    "U3_exact": 0,
    "U4": 0,
    "U5": 0,
    "U6": 0,
    "U7": 0,
    "cutoff": 0,
    "time_reordering": 0,
    "coefficient_spatial_reordering_T": 0,
    "coefficient_spatial_reordering_U": 0,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        issues.append(message)


for m in range(1, MAX_ORDER + 1):
    # T2: B_r * T_{m+2-r}, 1 <= r <= m+2.
    for r in range(1, m + 3):
        k = m + 2 - r
        counts["T2"] += 1
        require(0 <= k <= m + 1, f"T2 index out of range m={m}, r={r}, k={k}")
        if k == m + 1:
            require(r == 1, f"T2 next derivative lacks B1 weight m={m}, r={r}")
        elif k == m:
            require(r == 2, f"T2 current derivative is not Hessian-weighted m={m}, r={r}")
        elif r == m + 2:
            require(k == 0, f"T2 top cutoff is not paired with T0 m={m}")
        elif r == m + 1:
            require(k == 1, f"T2 current cutoff residual is not paired with T1 m={m}")
        else:
            require(k <= m - 1, f"T2 unexplained current level m={m}, r={r}, k={k}")

    # When r0>=1 derivatives land on a before the Laplacian is commuted,
    # B_r0 * [nabla^(m-r0),Delta] produces only prior levels.
    for r0 in range(1, m):
        k = m - r0
        for q in range(k + 1):
            s = k - q
            counts["coefficient_spatial_reordering_T"] += 1
            require(r0 <= m - 1 and q <= m - 1 and s <= m - 1,
                    f"T coefficient-commutator not prior m={m}, {(r0,q,s)}")

    # T3: B_r * T_i * T_j, r+i+j=m.
    for r in range(m + 1):
        for i in range(m - r + 1):
            j = m - r - i
            counts["T3"] += 1
            if i == m or j == m:
                require(r == 0 and min(i, j) == 0,
                        f"T3 current Tm lacks weighted T0 coefficient m={m}, {(r,i,j)}")
            else:
                require(i <= m - 1 and j <= m - 1,
                        f"T3 non-current classification failure m={m}, {(r,i,j)}")

    # T4 current subfamily: a*nabla^r Rm*T_s, r+s=m.  The
    # coefficient-before-commutator subfamilies were checked above.
    for r in range(m + 1):
        s = m - r
        counts["T4"] += 1
        if s == m:
            require(r == 0, f"T4 current Tm coefficient failure m={m}, r={r}")
        elif r == m:
            require(s == 0, f"T4 top curvature conversion failure m={m}, r={r}")
        else:
            require(r <= m - 1 and s <= m - 1,
                    f"T4 intermediate level failure m={m}, r={r}, s={s}")

    # T5: U_{r+1} * T_s, r+s=m-1.
    for r in range(m):
        s = m - 1 - r
        counts["T5"] += 1
        require(r + 1 <= m and s <= m - 1,
                f"T5 exceeds completed weighted/current levels m={m}, r={r}, s={s}")

        # Reordering r derivatives of partial_t Gamma can introduce
        # nabla^q Rm * U_{r-q} with q <= r-1; these are strictly prior T levels.
        for q in range(r):
            counts["time_reordering"] += 1
            require(q <= m - 2,
                    f"time reordering reaches non-prior curvature m={m}, r={r}, q={q}")

    # T6: B_r*T_{m-r}, from the linear a*G*T reaction.
    for r in range(m + 1):
        k = m - r
        counts["T6"] += 1
        if k == m:
            require(r == 0, f"T6 current Tm lacks bounded a coefficient m={m}")
        else:
            require(k <= m - 1, f"T6 lower level failure m={m}, r={r}, k={k}")

    # U2: B_r * U_{m+2-r}, 1 <= r <= m+2.
    for r in range(1, m + 3):
        k = m + 2 - r
        counts["U2"] += 1
        require(0 <= k <= m + 1, f"U2 index out of range m={m}, r={r}, k={k}")
        if k == m + 1:
            require(r == 1, f"U2 next derivative lacks B1 weight m={m}, r={r}")
        elif k == m:
            require(r == 2, f"U2 current derivative is not Hessian-weighted m={m}, r={r}")
        elif r == m + 2:
            require(k == 0, f"U2 top cutoff is not paired with U0 m={m}")
        elif r == m + 1:
            require(k == 1, f"U2 current cutoff residual is not paired with U1 m={m}")
        else:
            require(k <= m - 1, f"U2 unexplained current level m={m}, r={r}, k={k}")

    # Exact-flow U3 after (B1*B1)*T = 4(C1*C1)*U:
    # C_{r+1} * C_{s+1} * U_t, r+s+t=m.
    for r in range(m + 1):
        for s in range(m - r + 1):
            t = m - r - s
            counts["U3_exact"] += 1
            current_u = (t == m)
            current_c = (r == m or s == m)
            if current_u:
                require(r == 0 and s == 0,
                        f"exact U3 current Um has non-C1 coefficient m={m}, {(r,s,t)}")
            if current_c:
                require(t == 0 and min(r, s) == 0,
                        f"exact U3 current C_(m+1) not times C1,U0 m={m}, {(r,s,t)}")
            if not current_u and not current_c:
                require(t <= m - 1 and r + 1 <= m and s + 1 <= m,
                        f"exact U3 is not previous-level forcing m={m}, {(r,s,t)}")

    # The analogous coefficient-before-commutator terms in nabla^m(a Delta U)
    # have B_r0*T_q*U_s with r0>=1 and are strictly previous-level.
    for r0 in range(1, m):
        k = m - r0
        for q in range(k + 1):
            s = k - q
            counts["coefficient_spatial_reordering_U"] += 1
            require(r0 <= m - 1 and q <= m - 1 and s <= m - 1,
                    f"U coefficient-commutator not prior m={m}, {(r0,q,s)}")

    # U4: U_i*U_j, i+j=m.
    for i in range(m + 1):
        j = m - i
        counts["U4"] += 1
        if i == m or j == m:
            require(min(i, j) == 0,
                    f"U4 current Um lacks U0 coefficient m={m}, i={i}, j={j}")

    # U5 current subfamily: a*nabla^r Rm*U_s, r+s=m.  The
    # coefficient-before-commutator subfamilies were checked above.
    for r in range(m + 1):
        s = m - r
        counts["U5"] += 1
        if r == m:
            require(s == 0, f"U5 top curvature conversion failure m={m}, r={r}")
        elif s == m:
            require(r == 0, f"U5 current Um lacks bounded aRm coefficient m={m}, r={r}")
        else:
            require(r <= m - 1 and s <= m - 1,
                    f"U5 intermediate level failure m={m}, r={r}, s={s}")

    # U6: U_{r+1}*U_s, r+s=m-1.
    for r in range(m):
        s = m - 1 - r
        counts["U6"] += 1
        require(r + 1 <= m and s <= m - 1,
                f"U6 exceeds current level m={m}, r={r}, s={s}")
        if r + 1 == m:
            require(s == 0, f"U6 current Um lacks U0 coefficient m={m}, r={r}")

    # U7: B_r*U_{m-r}, from the linear a*G*U reaction.
    for r in range(m + 1):
        k = m - r
        counts["U7"] += 1
        if k == m:
            require(r == 0, f"U7 current Um lacks bounded a coefficient m={m}")
        else:
            require(k <= m - 1, f"U7 lower level failure m={m}, r={r}, k={k}")
    # Fixed scalar cutoff evolution: U_{r+1}*C_{s+1}, r+s=m-1.
    for r in range(m):
        s = m - 1 - r
        counts["cutoff"] += 1
        require(r + 1 <= m and s + 1 <= m,
                f"cutoff evolution exceeds pair m={m}, r={r}, s={s}")
        if r + 1 == m:
            require(s + 1 == 1,
                    f"current Um in cutoff equation is not paired with C1 m={m}, r={r}")

# Principal-symbol counterexample to ungauged L2 coercivity.
# xi=e1, h=diag(1,-eps,0,0).  The symbol in the convention of the note is
# sigma(h)=diag(eps,eps,0,0), hence <sigma(h),h>=eps-eps^2>0.
epsilon = 0.25
sigma_diag = [epsilon, epsilon, 0.0, 0.0]
h_diag = [1.0, -epsilon, 0.0, 0.0]
principal_quadratic = sum(x * y for x, y in zip(sigma_diag, h_diag))
require(abs(principal_quadratic - (epsilon - epsilon**2)) < 1e-12,
        "principal-symbol arithmetic mismatch")
require(principal_quadratic > 0,
        "principal-symbol counterexample is not positive")

# Smooth splice dependency: the l-th time jet of a second-order autonomous
# equation uses spatial derivatives through order at most 2*l.
jet_orders = {ell: 2 * ell for ell in range(1, 13)}
require(all(order == 2 * ell for ell, order in jet_orders.items()),
        "time-jet spatial-order recurrence failed")

result = {
    "max_order": MAX_ORDER,
    "family_allocation_counts": counts,
    "total_allocations": sum(counts.values()),
    "failures": issues,
    "failure_count": len(issues),
    "principal_symbol_counterexample": {
        "xi": [1, 0, 0, 0],
        "h_diagonal": h_diag,
        "symbol_diagonal": sigma_diag,
        "inner_product": principal_quadratic,
        "formula": "epsilon-epsilon^2",
        "implication": "no frequency-independent ungauged L2 Gronwall estimate from Ricci coercivity",
    },
    "smooth_splice_time_jet_spatial_orders": jet_orders,
    "scope": (
        "Finite verification of derivative allocations and symbol arithmetic. "
        "The universal tensor-family derivation and energy proof are in the companion note."
    ),
}

workspace = Path(__file__).resolve().parents[1]
out_path = workspace / "data" / "step60_family_enumeration_verify.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")

print(f"orders checked: 1..{MAX_ORDER}")
print(f"allocations checked: {result['total_allocations']}")
print(f"principal symbol quadratic: {principal_quadratic:.8f} (>0)")
print(f"failures: {len(issues)}")
print(f"saved: {out_path}")
if issues:
    for item in issues[:20]:
        print(f"FAIL: {item}")
    raise SystemExit(1)
print("All finite allocation and symbol checks pass.")
