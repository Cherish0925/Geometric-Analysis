"""Step 100: exact relative Chern--Gauss--Bonnet bookkeeping for a graph gluing.

This script does not model an unknown connector.  It records the exact algebra and
the scaling forced by one explicit hyperbolic-piece/lattice family, so local
matching experiments can be compared in the same normalization.

Laboratory piece: an orientable double cover 24cdc1.* of a one-cusped 24-cell
hyperbolic four-manifold.  Source data give chi=2, total hyperbolic volume
8*pi^2/3, torus cusp, and maximum-cusp volume 16.  A degree-N cyclic cover with
one cusp has total volume and cusp covolume multiplied by N.  Truncating an
oriented cusp at depth T multiplies the boundary 3-volume by exp(-3T), and the
removed tail volume is boundary_volume/3.

For a replacement N with E=Ric+3g and exactly hyperbolic complement:
  B := 2 int_N |W|^2 + 12(Vol(N)-V_removed)
     = int_N (|E0|^2 + 2 tr E - (tr E)^2/12).
If ||E||_op <= delta then |B| <= (8 delta+4 delta^2) Vol(N).
"""
from __future__ import annotations

import json
import math
from pathlib import Path

SESSION = Path(__file__).resolve().parents[2]


def row(N: int, depth_shift: float, connector_density: float,
        weyl_density: float, delta: float) -> dict:
    """Return bookkeeping at T=log N+depth_shift.

    connector_density means Vol(connector)/boundary_volume at the attachment.
    weyl_density means (int |W|^2)/Vol(connector).  They are placeholders to be
    replaced by integrals from a faithful full-matrix field, not fit parameters.
    """
    chi_piece = 2 * N
    total_hyp_volume = (8.0 * math.pi**2 / 3.0) * N
    max_cusp_volume = 16.0 * N
    max_boundary_volume = 3.0 * max_cusp_volume
    T = math.log(N) + depth_shift
    boundary_volume = max_boundary_volume * math.exp(-3.0 * T)
    removed_volume = boundary_volume / 3.0
    connector_volume = connector_density * boundary_volume
    weyl_energy = weyl_density * connector_volume
    cgb_lhs = 2.0 * weyl_energy + 12.0 * (connector_volume - removed_volume)
    defect_bound = (8.0 * delta + 4.0 * delta**2) * connector_volume
    return {
        "N": N,
        "depth_T": T,
        "chi_piece_cover": chi_piece,
        "total_hyperbolic_volume": total_hyp_volume,
        "maximum_cusp_volume_before_depth": max_cusp_volume,
        "boundary_volume_at_depth": boundary_volume,
        "removed_tail_volume": removed_volume,
        "connector_volume_placeholder": connector_volume,
        "weyl_energy_placeholder": weyl_energy,
        "relative_cgb_lhs_placeholder": cgb_lhs,
        "pointwise_defect_rhs_bound": defect_bound,
        "normalized_balance_by_connector_volume": cgb_lhs / connector_volume,
        "removed_to_connector_ratio": removed_volume / connector_volume,
        "boundary_times_N_squared": boundary_volume * N * N,
        "removed_times_N_squared": removed_volume * N * N,
        "connector_times_N_squared": connector_volume * N * N,
    }


def main() -> None:
    # Dimensionless placeholder choices only demonstrate scaling.  The actual
    # values must come from integrating the full metric.
    depth_shift = 0.0
    connector_density = 1.0
    weyl_density = 0.0
    delta = 0.05
    rows = [row(N, depth_shift, connector_density, weyl_density, delta)
            for N in (1, 2, 4, 8, 16, 32, 64, 128)]

    # Exact algebra checks for a generic trace t and tracefree norm z2 are
    # represented symbolically in the metadata; numerical checks concern the
    # N-scaling only.
    scaled_boundary = [r["boundary_times_N_squared"] for r in rows]
    scaled_removed = [r["removed_times_N_squared"] for r in rows]
    scaled_connector = [r["connector_times_N_squared"] for r in rows]
    checks = {
        "boundary_Nminus2_relative_spread": (
            max(scaled_boundary) - min(scaled_boundary)
        ) / scaled_boundary[0],
        "removed_Nminus2_relative_spread": (
            max(scaled_removed) - min(scaled_removed)
        ) / scaled_removed[0],
        "connector_Nminus2_relative_spread": (
            max(scaled_connector) - min(scaled_connector)
        ) / scaled_connector[0],
        "removed_equals_boundary_over_3_max_abs": max(
            abs(r["removed_tail_volume"] - r["boundary_volume_at_depth"] / 3.0)
            for r in rows
        ),
        "hyperbolic_GB_max_abs": max(
            abs(r["total_hyperbolic_volume"] - 4.0 * math.pi**2 * r["chi_piece_cover"] / 3.0)
            for r in rows
        ),
    }
    out = {
        "explicit_family": {
            "piece": "orientable double cover 24cdc1.* of a one-cusped hyperbolic 24-cell manifold",
            "base_chi": 2,
            "base_hyperbolic_volume": 8.0 * math.pi**2 / 3.0,
            "base_maximum_cusp_volume": 16.0,
            "base_cusp_link": "T^3",
            "base_homology_fact": "b1=1, b3=0 for the listed orientable double covers",
            "cyclic_cover_assumption": "use a primitive character nonzero on the peripheral image and N coprime to its peripheral multiplicity",
        },
        "relative_identity": (
            "2*int_N|W|^2 + 12*(Vol_N-V_removed) = "
            "int_N(|E0|^2 + 2*trE - (trE)^2/12)"
        ),
        "pointwise_bound": "absolute RHS <= (8*delta+4*delta^2)*Vol_N",
        "parameters_for_scaling_demonstration": {
            "depth": "T=log(N)+depth_shift",
            "depth_shift": depth_shift,
            "connector_density_Vol_over_boundary3volume": connector_density,
            "weyl_density_energy_over_connector_volume": weyl_density,
            "delta": delta,
            "warning": "connector and Weyl densities are placeholders, not computed geometry",
        },
        "rows": rows,
        "checks": checks,
        "interpretation": (
            "Degree-N cusp area followed by depth log N scales as N^-2. "
            "A rank-two lattice quotient of a locally fixed connector also scales as N^-2. "
            "Therefore volume, Weyl energy, and defect integrals share the same leading factor; "
            "only a nonzero mismatch after normalization by connector volume could obstruct the family."
        ),
    }
    path = SESSION / "workspace/data/step100_relative_cgb_scaling.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(path), "checks": checks, "first": rows[0], "last": rows[-1]}, indent=2))


if __name__ == "__main__":
    main()
