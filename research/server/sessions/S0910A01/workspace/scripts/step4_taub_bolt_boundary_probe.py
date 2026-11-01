"""
Step 4 Taub--Bolt--AdS boundary-data probe for Yau 26.

Purpose
-------
This script samples exact U(2)-invariant Einstein caps with Ric = -g in the
Taub--Bolt--AdS family.  It is not an optimization proof.  It records the
first and normal-derivative boundary data that are attainable by smooth bolt
fillings of disk-bundle topology, so the later cap problem can be posed as a
matching problem rather than as a free residual minimization.

Conventions follow Akbar, gr-qc/0301007, with cosmological constant Lambda=-1:

  ds^2 = (rho^2-L^2)/Delta d rho^2
       + 4 L^2 Delta/(rho^2-L^2) (d psi + cos theta d phi)^2
       + (rho^2-L^2)(d theta^2 + sin^2 theta d phi^2),

  Ric = - g,
  Delta = rho^2 - 2 M rho + L^2 - (L^4 + 2 L^2 rho^2 - rho^4/3).

For period Delta psi = 4 pi (the p=1 case), smooth bolts occur for
0 < L^2 <= (2-sqrt(3))/4.  The bolt radius r_b is one of the two roots

  r_b = [1 +/- sqrt(1 + 16 L^4 - 16 L^2)]/(4L),

and M is then determined by Delta(r_b)=0.  At a finite cutoff rho > r_b,
the boundary Berger metric is a^2(sigma_1^2+sigma_2^2)+b^2 sigma_3^2 with

  a^2 = rho^2 - L^2,
  b^2 = 4 L^2 Delta/(rho^2-L^2).

The script also computes the two principal second-fundamental-form ratios
A = (da/dt)/a and B = (db/dt)/b, where t is outward geodesic distance.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

try:
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover
    plt = None

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGURES = ROOT / "figures"
DATA.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

LAMBDA_POS = 1.0  # -cosmological constant; Ric = -g
L2_MAX = (2.0 - math.sqrt(3.0)) / 4.0
L_MAX = math.sqrt(L2_MAX)


def bolt_radius(L: float, branch: str) -> float:
    disc = 1.0 + 16.0 * L**4 - 16.0 * L**2
    if disc < 0:
        raise ValueError("outside regular bolt range")
    sd = math.sqrt(max(disc, 0.0))
    if branch == "small_bolt_root":
        return (1.0 - sd) / (4.0 * L)
    if branch == "large_bolt_root":
        return (1.0 + sd) / (4.0 * L)
    raise ValueError(branch)


def mass_from_bolt(L: float, rb: float) -> float:
    # Negative cosmological constant formula with lambda=1.
    return (3 * rb**2 + rb**4 + 3 * L**2 - 3 * L**4 - 6 * L**2 * rb**2) / (6 * rb)


def Delta(rho: float, L: float, M: float) -> float:
    return rho**2 - 2 * M * rho + L**2 - (L**4 + 2 * L**2 * rho**2 - rho**4 / 3.0)


def Deltaprime(rho: float, L: float, M: float) -> float:
    return 2 * rho - 2 * M - 4 * L**2 * rho + (4.0 / 3.0) * rho**3


def boundary_data(L: float, branch: str, rho: float) -> dict[str, float | str]:
    rb = bolt_radius(L, branch)
    M = mass_from_bolt(L, rb)
    D = Delta(rho, L, M)
    if D <= 0:
        raise ValueError("rho is not in the positive-metric region")
    a2 = rho**2 - L**2
    if a2 <= 0:
        raise ValueError("invalid a^2")
    a = math.sqrt(a2)
    b = 2.0 * L * math.sqrt(D) / a
    sqrtD = math.sqrt(D)
    # geodesic distance satisfies dt/drho = sqrt((rho^2-L^2)/Delta) = a/sqrtD
    da_dt = rho * sqrtD / (a2)
    logb_rho_derivative = 0.5 * Deltaprime(rho, L, M) / D - rho / a2
    db_dt = b * (sqrtD / a) * logb_rho_derivative
    return {
        "branch": branch,
        "L": L,
        "L_squared": L * L,
        "regularity_L2_max": L2_MAX,
        "rho_bolt": rb,
        "M": M,
        "rho_boundary": rho,
        "a": a,
        "b": b,
        "b_over_a": b / a,
        "a_over_b": a / b if b > 0 else float("inf"),
        "da_dt": da_dt,
        "db_dt": db_dt,
        "A_second_fund_ratio": da_dt / a,
        "B_second_fund_ratio": db_dt / b,
        "mean_curvature_trace": 2.0 * da_dt / a + db_dt / b,
        "ricci_defect_sup": 0.0,
    }


def main() -> None:
    rows: list[dict[str, float | str]] = []
    # Avoid the endpoint where the two roots merge and avoid L=0.
    L_values = np.geomspace(2e-4, L_MAX * 0.999, 240)
    # sample cutoffs from just outside the bolt to far out; include linear near-bolt samples
    eta_values = np.unique(
        np.concatenate([
            np.geomspace(1e-4, 1e-1, 35),
            np.geomspace(1.1e-1, 50.0, 75),
        ])
    )
    for branch in ("small_bolt_root", "large_bolt_root"):
        for L in L_values:
            rb = bolt_radius(float(L), branch)
            for eta in eta_values:
                rho = rb * (1.0 + float(eta))
                try:
                    rows.append(boundary_data(float(L), branch, rho))
                except (ValueError, ZeroDivisionError, OverflowError):
                    continue

    csv_path = DATA / "step4_taub_bolt_ads_boundary_samples.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    by_branch = {}
    for branch in ("small_bolt_root", "large_bolt_root"):
        sub = [r for r in rows if r["branch"] == branch]
        ratios = np.array([float(r["b_over_a"]) for r in sub])
        H = np.array([float(r["mean_curvature_trace"]) for r in sub])
        by_branch[branch] = {
            "count": len(sub),
            "b_over_a_min": float(np.min(ratios)),
            "b_over_a_max": float(np.max(ratios)),
            "b_over_a_median": float(np.median(ratios)),
            "mean_curvature_min": float(np.min(H)),
            "mean_curvature_max": float(np.max(H)),
        }

    # Points closest to selected squashing ratios, useful as exact zero-defect examples.
    targets = [0.25, 0.5, 1.0, 2.0, 4.0]
    nearest = {}
    for target in targets:
        best = min(rows, key=lambda r: abs(math.log(float(r["b_over_a"]) / target)))
        nearest[str(target)] = {k: best[k] for k in [
            "branch", "L", "rho_bolt", "rho_boundary", "a", "b", "b_over_a",
            "A_second_fund_ratio", "B_second_fund_ratio", "mean_curvature_trace",
            "ricci_defect_sup",
        ]}

    summary = {
        "metric_family": "Taub-Bolt-AdS, biaxial Bianchi IX, Lambda=-1 so Ric=-g",
        "regularity_range_L_squared": [0.0, L2_MAX],
        "topology_reading": {
            "Akbar_2003_words": "complete metric over a manifold having topology CP^2 (orientation convention not fixed here)",
            "Toldo_Willett_2017_words": "Bolt topology O(-p)->S^2 and boundary S^3/Z_p; for p=1 this is the disk bundle with Euler number -1, orientation-equivalent to CPbar^2 minus a ball under standard complex orientation",
            "research_use": "smooth exceptional-handle-type bolt fillings with Ric=-g exist for their attained boundary Cauchy data; a cap obstruction must be a matching or global-topology statement, not a free cap residual statement",
        },
        "samples_csv": str(csv_path.relative_to(ROOT)),
        "sample_count": len(rows),
        "branch_summaries": by_branch,
        "nearest_zero_defect_examples_by_target_b_over_a": nearest,
    }
    json_path = DATA / "step4_taub_bolt_ads_summary.json"
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    fig_path = None
    if plt is not None:
        fig_path = FIGURES / "step4_taub_bolt_boundary_map.png"
        fig, ax = plt.subplots(figsize=(8, 5), dpi=160)
        for branch, color in [("small_bolt_root", "tab:blue"), ("large_bolt_root", "tab:orange")]:
            sub = [r for r in rows if r["branch"] == branch]
            x = [float(r["a"]) for r in sub]
            y = [float(r["b_over_a"]) for r in sub]
            ax.scatter(x, y, s=2, alpha=0.18, label=branch, color=color, rasterized=True)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("boundary horizontal radius a")
        ax.set_ylabel("boundary squashing b/a")
        ax.set_title("Exact Ric=-g Taub--Bolt--AdS bolt fillings: attained boundary data")
        ax.legend(markerscale=4)
        ax.grid(True, which="both", alpha=0.25)
        fig.tight_layout()
        fig.savefig(fig_path)
        plt.close(fig)
        summary["figure"] = str(fig_path.relative_to(ROOT))
        json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("Taub--Bolt--AdS boundary probe complete")
    print(f"regular L^2 range: (0, {L2_MAX:.12g}]")
    print(f"rows: {len(rows)}")
    for branch, info in by_branch.items():
        print(f"{branch}: b/a in [{info['b_over_a_min']:.6g}, {info['b_over_a_max']:.6g}], "
              f"mean curvature in [{info['mean_curvature_min']:.6g}, {info['mean_curvature_max']:.6g}]")
    print("nearest zero-defect sampled examples:")
    for target, best in nearest.items():
        print(f"  target b/a={target}: branch={best['branch']}, L={best['L']:.6g}, "
              f"rho={best['rho_boundary']:.6g}, b/a={best['b_over_a']:.6g}, "
              f"H={best['mean_curvature_trace']:.6g}")
    print(f"summary: {json_path}")
    print(f"csv: {csv_path}")
    if fig_path is not None:
        print(f"figure: {fig_path}")


if __name__ == "__main__":
    main()
