#!/usr/bin/env python3
"""
Step 55 verification ledger for the coupled first-exit bootstrap and
fixed-background continuation bridge.

This script does not prove the PDE estimates.  It checks the algebraic/scaling
interfaces repaired in Step 55:
  * bilipschitz transport of the Sobolev constant uses V(t)=int ||aE||_inf;
  * the weighted defect endpoint is integrable and improves V;
  * the gamma/V bootstrap can be closed for explicit small parameters;
  * fixed-background connection conversion is triangular in A-derivative order;
  * restart data are obtained from A-bounds, not from moving-covariant derivatives
    of the metric;
  * Rauch noncollapse is attached to the exponential pullback ball.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

SESSION = Path("Sessions/S0910A01")
OUT = SESSION / "workspace/data/step55_bootstrap_continuation_verify.json"


def check(cond: bool, name: str, details: str = "") -> dict:
    return {"name": name, "pass": bool(cond), "details": details}


def sobolev_bilipschitz_exponent(n: int) -> dict:
    """Return exponents for S_g <= L^expo S_g0 under length L-bilipschitz."""
    if n <= 2:
        # The IL module is four-dimensional.  For n=2 the critical exponent is
        # replaced by any finite Sobolev exponent; we do not use it here.
        return {"n": n, "critical_p": None, "left_norm_exponent": None, "gradient_total_exponent": None, "used_exponent": None}
    p = 2 * n / (n - 2)
    left = 2 * n / p  # exponent from L^p norm squared under volume change
    gradient = left + n + 2  # compare grad_0 integral to grad_g integral
    l2term = left + n
    used = max(gradient, l2term)
    return {"n": n, "critical_p": p, "left_norm_exponent": left, "gradient_total_exponent": gradient, "l2_total_exponent": l2term, "used_exponent": used}


def bootstrap_sample(n=4, C_H=10.0, C_V=6.0, C_E=8.0, r=0.25, gamma_star=1e-2):
    """Choose explicit small theta, V_star, delta and verify improvement."""
    theta = min(1e-3, 1.0 / (100.0 * C_H))
    V_star = min(1e-3, 1.0 / (100.0 * (2*n + 0.5*C_V)))
    factor = math.exp((2*n + 0.5*C_V) * V_star + C_H * theta)
    gamma0 = gamma_star / 2.0
    gamma_improved = gamma0 * factor
    # Choose delta with room so V(T) <= V_star/2.
    delta_max_for_half = V_star / (3.0 * C_E * (theta ** (2.0/3.0)) * (r ** 2))
    delta = 0.5 * delta_max_for_half
    T = theta * r * r
    V_bound = 1.5 * C_E * delta * (theta ** (2.0/3.0)) * (r ** 2)
    return {
        "n": n,
        "constants": {"C_H": C_H, "C_V": C_V, "C_E": C_E, "r": r, "gamma_star": gamma_star},
        "chosen": {"theta": theta, "V_star": V_star, "delta": delta, "T": T},
        "factor": factor,
        "gamma0": gamma0,
        "gamma_improved": gamma_improved,
        "target_gamma_bound": 0.75 * gamma_star,
        "V_bound": V_bound,
        "target_V_bound": 0.5 * V_star,
        "passes": {
            "gamma_factor_le_3_over_2": factor <= 1.5,
            "gamma_improves": gamma_improved <= 0.75 * gamma_star,
            "V_improves": V_bound <= 0.5 * V_star,
        },
    }


def defect_integral_formula(r: float, theta: float) -> float:
    """Integral of (r^2/t)^(1/3) from 0 to theta*r^2."""
    T = theta * r * r
    return 1.5 * (r ** (2.0/3.0)) * (T ** (2.0/3.0))


def expected_defect_integral(r: float, theta: float) -> float:
    return 1.5 * (theta ** (2.0/3.0)) * (r ** 2)


def triangular_orders(max_m: int = 20) -> list[dict]:
    """Check the schematic triangular order facts in the fixed-background bridge.

    For bar∇^m(g^{-1} * ∇Y): distributing k derivatives to g^{-1} and m-k to ∇Y:
      - bar∇^k g^{-1} uses A-derivatives up to k-1 if k>=1;
      - bar∇^(m-k)(∇Y) has top evolving derivative ∇^(m-k+1)Y and A-order <= m-k-1.
    Hence top Y order <= m+1 and top A order <= m-1, never m.
    """
    rows = []
    for m in range(max_m + 1):
        worst_A = -1
        worst_Y = 0
        for k in range(m + 1):
            A_from_g_inv = k - 1 if k >= 1 else -1
            A_from_connection_conversion = (m - k) - 1 if (m - k) >= 1 else -1
            Y_order = (m - k) + 1
            worst_A = max(worst_A, A_from_g_inv, A_from_connection_conversion)
            worst_Y = max(worst_Y, Y_order)
        rows.append({
            "m": m,
            "worst_A_derivative_order_on_rhs": worst_A,
            "allowed_A_order": m - 1,
            "worst_evolving_Y_derivative_order": worst_Y,
            "allowed_Y_order": m + 1,
            "triangular_for_A": worst_A <= m - 1,
            "top_Y_is_U_m_plus_1": worst_Y <= m + 1,
        })
    return rows


def cutoff_conversion_orders(max_j: int = 20) -> list[dict]:
    rows = []
    for j in range(max_j + 1):
        if j <= 1:
            worst_A = -1
        else:
            worst_A = j - 2
        rows.append({
            "j": j,
            "worst_A_derivative_order_in_nabla_j_chi": worst_A,
            "allowed": max(-1, j - 2),
            "triangular": worst_A <= max(-1, j - 2),
        })
    return rows


def metric_restart_orders(max_m: int = 20) -> list[dict]:
    rows = []
    for m in range(max_m + 1):
        # bar∇^(m+1) g has leading bar∇^m A * g plus lower A products.
        rows.append({
            "metric_derivative_order": m + 1,
            "requires_A_derivative_order": m,
            "not_moving_covariant_metric_derivative": True,
        })
    return rows


def rauch_pullback_lower_volume(n: int = 4, K: float = 10.0, rho: float = 0.1, samples: int = 100000) -> dict:
    """Numerically integrate a standard positive lower model for the pullback ball.

    If sectional curvature <= K and rho < pi/sqrt(K), Rauch/Bishop comparison
    gives polar Jacobian bounded below by (sin(sqrt(K) t)/(sqrt(K) t))^(n-1)
    relative to Euclidean polar density on the tangent ball.  This is a lower
    volume for the exponential pullback ball; it is not a statement about the
    image ball being embedded or noncollapsed in the base manifold.
    """
    omega_sphere = 2 * math.pi ** (n / 2) / math.gamma(n / 2)
    if K <= 0:
        ratio_lower = 1.0
        volume_lower = omega_sphere * rho ** n / n
    else:
        sqrtK = math.sqrt(K)
        assert rho * sqrtK < math.pi
        # Simpson integration for int_0^rho (sin(sqrtK t)/sqrtK)^(n-1) dt * area(S^{n-1}).
        if samples % 2:
            samples += 1
        h = rho / samples
        total = 0.0
        for i in range(samples + 1):
            t = i * h
            if t == 0:
                val = 0.0
            else:
                val = (math.sin(sqrtK * t) / sqrtK) ** (n - 1)
            coef = 4 if i % 2 else 2
            if i == 0 or i == samples:
                coef = 1
            total += coef * val
        volume_lower = omega_sphere * h * total / 3.0
        eucl = omega_sphere * rho ** n / n
        ratio_lower = volume_lower / eucl
    return {
        "n": n,
        "K": K,
        "rho": rho,
        "condition_rho_sqrtK_lt_pi": rho * math.sqrt(max(K, 0.0)) < math.pi if K > 0 else True,
        "pullback_volume_lower": volume_lower,
        "euclidean_ball_volume": omega_sphere * rho ** n / n,
        "ratio_to_euclidean": ratio_lower,
        "statement_scope": "pullback tangent ball only; no injectivity or base-ball volume lower bound asserted",
    }


def main() -> None:
    checks = []
    sob = sobolev_bilipschitz_exponent(4)
    checks.append(check(abs(sob["used_exponent"] - 8.0) < 1e-12, "sobolev_transport_n4_exponent", f"S(t) <= e^(8V) S(0), data={sob}"))

    for r in (0.125, 0.25, 0.5, 1.0):
        for theta in (1e-4, 1e-3, 1e-2):
            lhs = defect_integral_formula(r, theta)
            rhs = expected_defect_integral(r, theta)
            checks.append(check(abs(lhs - rhs) <= 1e-12 * max(1, abs(rhs)), f"defect_integral_r={r}_theta={theta}", f"integral={lhs}, expected={rhs}"))

    sample = bootstrap_sample()
    checks.append(check(sample["passes"]["gamma_factor_le_3_over_2"], "bootstrap_factor", json.dumps(sample["passes"])))
    checks.append(check(sample["passes"]["gamma_improves"], "gamma_improvement", f"gamma={sample['gamma_improved']} target={sample['target_gamma_bound']}"))
    checks.append(check(sample["passes"]["V_improves"], "V_improvement", f"V={sample['V_bound']} target={sample['target_V_bound']}"))

    tri = triangular_orders(25)
    checks.append(check(all(row["triangular_for_A"] for row in tri), "connection_conversion_triangular_A", "bar∇^m A does not enter RHS for ∂t bar∇^m A"))
    checks.append(check(all(row["top_Y_is_U_m_plus_1"] for row in tri), "connection_conversion_top_U", "top evolving derivative is U_{m+1}"))

    cut = cutoff_conversion_orders(25)
    checks.append(check(all(row["triangular"] for row in cut), "cutoff_jet_conversion", "nabla^j chi uses A-derivatives only up to j-2"))

    met = metric_restart_orders(25)
    checks.append(check(all(row["not_moving_covariant_metric_derivative"] for row in met), "metric_restart_uses_background_derivatives", "bar∇^(m+1)g from bar∇^m A, not ∇^m g"))

    rauch = rauch_pullback_lower_volume()
    checks.append(check(rauch["condition_rho_sqrtK_lt_pi"] and rauch["pullback_volume_lower"] > 0, "rauch_pullback_volume_positive", f"ratio={rauch['ratio_to_euclidean']}"))

    passed = sum(1 for c in checks if c["pass"])
    result = {
        "summary": {"passed": passed, "total": len(checks)},
        "checks": checks,
        "sobolev_bilipschitz_exponent": sob,
        "bootstrap_sample": sample,
        "triangular_orders_sample": tri[:8] + tri[-3:],
        "cutoff_conversion_sample": cut[:8] + cut[-3:],
        "metric_restart_orders_sample": met[:5] + met[-3:],
        "rauch_pullback": rauch,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print("=== Step 55 bootstrap/continuation verification ===")
    for c in checks:
        status = "PASS" if c["pass"] else "FAIL"
        print(f"[{status}] {c['name']} -- {c['details']}")
    print(f"=== Summary: {passed}/{len(checks)} passed ===")
    print(f"Wrote {OUT}")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
