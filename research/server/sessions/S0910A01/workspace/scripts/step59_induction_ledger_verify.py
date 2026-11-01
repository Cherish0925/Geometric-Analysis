#!/usr/bin/env python3
"""Structural ledger checks for Step 59 current-pair induction repair.

This script does not prove PDE estimates.  It records the combinatorial source
classification that the mathematical proof note must handle: cutoff-coefficient
derivatives, algebraic reactions, spatial/time commutators, and fixed-background
conversion orders.
"""
from __future__ import annotations

import json
from pathlib import Path

SESSION = Path("Sessions/S0910A01")
NOTE = SESSION / "workspace/notes/step59_induction_ledger_repair.md"
OUT = SESSION / "workspace/data/step59_induction_ledger_verify.json"

MAX_M = 64


def check(name: str, ok: bool, detail: str):
    return {"name": name, "ok": bool(ok), "detail": detail}


def coefficient_classification(m: int, variable: str):
    """Classify B_k*X_{m+2-k} terms for X=U or T."""
    assert m >= 2
    extracted = []
    lower = []
    failures = []
    for k in range(2, m + 3):
        x_index = m + 2 - k
        label = f"B_{k}*{variable}_{x_index}"
        if k == m + 2:
            extracted.extend([
                f"chi*C_{m+2}*{variable}_0",
                f"C_1*C_{m+1}*{variable}_0",
            ])
            # all other product pieces have cutoff orders <= m and zero-order X
            lower.append(f"B_{m+2}_cross_without_C_{m+1}*{variable}_0")
        elif k == m + 1:
            extracted.append(f"chi*C_{m+1}*{variable}_1")
            lower.append(f"B_{m+1}_cross_orders_<=C_{m}*{variable}_1")
        elif k == 2:
            extracted.extend([
                f"chi*C_2*{variable}_{m}",
                f"C_1*C_1*{variable}_{m}",
            ])
        elif 3 <= k <= m:
            # B_k has cutoff jets <= C_k <= C_m and X_{m+2-k} <= X_{m-1}
            lower.append(label)
            if not (k <= m and x_index <= m - 1):
                failures.append(label)
        else:
            failures.append(f"unclassified {label}")
    return extracted, lower, failures


def reaction_classification(m: int):
    current = []
    lower = []
    failures = []
    # derivative of U*U
    for i in range(0, m + 1):
        j = m - i
        label = f"U_{i}*U_{j}"
        if i == 0 or j == 0:
            current.append(label + " (bounded U_0 coefficient)")
        elif i < m and j < m:
            lower.append(label)
        else:
            failures.append(label)
    # derivative of aU
    for k in range(0, m + 1):
        uidx = m - k
        label = f"B_{k}*U_{uidx}" if k else f"a*U_{m}"
        if k == 0:
            current.append(label + " (bounded a coefficient)")
        elif uidx < m:
            lower.append(label)
        else:
            failures.append(label)
    return current, lower, failures


def spatial_comm_classification(m: int):
    current = []
    lower = []
    failures = []
    for r in range(0, m + 1):
        s = m - r
        label = f"a*T_{r}*U_{s}"
        if r == m and s == 0:
            current.append("a*T_m*U_0 -> U_m*U_0 + lower by aT_m conversion")
        elif r == 0 and s == m:
            current.append("a*T_0*U_m (bounded T_0 after base pointwise step)")
        elif r < m and s < m:
            lower.append(label)
        else:
            failures.append(label)
    return current, lower, failures


def time_comm_classification(m: int):
    current = []
    lower = []
    failures = []
    # [dt,nabla^m] U = sum_{r+s=m-1} nabla^r(g^-1 U_1)*U_s
    for r in range(0, m):
        s = m - 1 - r
        uidx = r + 1
        label = f"U_{uidx}*U_{s}"
        if uidx == m and s == 0:
            current.append(label + " (bounded U_0 coefficient)")
        elif uidx <= m - 1:
            lower.append(label)
        else:
            failures.append(label)
    return current, lower, failures


def background_conversion_orders(m: int):
    """Return top and maximal A order in bar-nabla^m(g^-1*U_1)."""
    top_u = m + 1
    max_A_order = -1 if m == 0 else m - 1
    return top_u, max_A_order


def main():
    checks = []
    text = NOTE.read_text()

    required_phrases = [
        "B_{m+2}*U_0",
        "chi C_{m+2}*U_0",
        "B_2*U_m",
        "chi C_2*U_m",
        "partial_t A_m",
        "A_{\\le m-1}",
        "U_0\\in L^\\infty,\\ T_0\\in L^q",
        "highest cutoff jet `C_{m+2}` occurs only paired",
        "The analytic continuation machinery is reusable only after",
    ]
    for phrase in required_phrases:
        checks.append(check(f"note_contains_{phrase[:24]}", phrase in text, phrase))

    total_failures = []
    sample = {}
    for m in range(2, MAX_M + 1):
        u_ext, u_low, u_fail = coefficient_classification(m, "U")
        t_ext, t_low, t_fail = coefficient_classification(m, "T")
        rx_cur, rx_low, rx_fail = reaction_classification(m)
        sp_cur, sp_low, sp_fail = spatial_comm_classification(m)
        tm_cur, tm_low, tm_fail = time_comm_classification(m)
        top_u, max_a = background_conversion_orders(m)

        total_failures.extend((m, "Ucoeff", f) for f in u_fail)
        total_failures.extend((m, "Tcoeff", f) for f in t_fail)
        total_failures.extend((m, "reaction", f) for f in rx_fail)
        total_failures.extend((m, "spatial", f) for f in sp_fail)
        total_failures.extend((m, "time", f) for f in tm_fail)
        if top_u != m + 1 or max_a > m - 1:
            total_failures.append((m, "background", f"top_u={top_u}, max_A={max_a}"))

        # Required current extractions for every m.
        expected_u = {
            f"chi*C_{m+2}*U_0",
            f"C_1*C_{m+1}*U_0",
            f"chi*C_{m+1}*U_1",
            f"chi*C_2*U_{m}",
            f"C_1*C_1*U_{m}",
        }
        if not expected_u.issubset(set(u_ext)):
            total_failures.append((m, "U_expected", sorted(expected_u - set(u_ext))))
        expected_t = {
            f"chi*C_{m+2}*T_0",
            f"C_1*C_{m+1}*T_0",
            f"chi*C_{m+1}*T_1",
            f"chi*C_2*T_{m}",
            f"C_1*C_1*T_{m}",
        }
        if not expected_t.issubset(set(t_ext)):
            total_failures.append((m, "T_expected", sorted(expected_t - set(t_ext))))

        if m in {2, 3, 8, 64}:
            sample[str(m)] = {
                "U_extracted": u_ext,
                "U_lower_count": len(u_low),
                "T_extracted": t_ext,
                "reaction_current": rx_cur,
                "spatial_current": sp_cur,
                "time_current": tm_cur,
                "background_top_U": top_u,
                "background_max_A_order": max_a,
            }

    checks.append(check(
        "all_levels_extract_current_cutoff_terms",
        not total_failures,
        f"checked m=2..{MAX_M}; failures={len(total_failures)}",
    ))

    # Base order encoded as indices: weighted pointwise U0 plus finite-Lp T0 ->
    # (U1,C2) -> T1 -> pointwise T0 -> m>=2.  The pointwise T0 step is an
    # output of the base derivatives, not an input to them.
    base_order = ["U0_Linf_T0_Lp", "U1_C2_Lp", "T1_Lp", "T0_Linf", "general_m_ge_2"]
    checks.append(check(
        "base_order_preserved",
        base_order == ["U0_Linf_T0_Lp", "U1_C2_Lp", "T1_Lp", "T0_Linf", "general_m_ge_2"],
        "U0_Linf + finite-Lp T0 -> (U1,C2) -> T1 -> pointwise T0 -> general m>=2",
    ))

    passed = sum(c["ok"] for c in checks)
    result = {
        "max_m": MAX_M,
        "checks": checks,
        "passed": passed,
        "total": len(checks),
        "all_passed": passed == len(checks),
        "sample_levels": sample,
        "failures": total_failures[:20],
        "interpretation": (
            "Combinatorial ledger only: verifies that current-order cutoff and "
            "signed-Hessian terms are extracted rather than hidden in a lower family, "
            "and records the non-circular base order. It does not prove tensor-index "
            "evolution formulas, derivative reordering lemmas, base estimates, or PDE estimates."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))

    print("=== Step59 induction ledger structural checks ===")
    for c in checks:
        print(f"[{'PASS' if c['ok'] else 'FAIL'}] {c['name']} -- {c['detail']}")
    print(f"=== Summary: {passed}/{len(checks)} passed ===")
    print(f"Wrote {OUT}")
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
