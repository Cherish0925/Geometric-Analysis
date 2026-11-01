#!/usr/bin/env python3
"""Focused regression tests for the V4 Ricci-flow prototype."""
from __future__ import annotations

import numpy as np

from naive_start_v4_ricci_flow import (
    FOUR_PI,
    Thresholds,
    classifier,
    make_icosphere,
    reference_operators,
    regge_curvature,
    v4_orbits,
)


def _fixture(**updates):
    n = 10
    metrics = {
        "triangle_margin_relative": [0.2] * n,
        "seam_area_ratio_min": [1.0] * n,
        "interior_abs_curvature_max": [1.0] * n,
        "model_defect_sup": [0.01] * n,
        "direct_target_relative_sup": [0.01] * n,
        "flow_speed_sup": [0.01] * n,
    }
    metrics.update(updates)
    return metrics


def test_mesh_and_exact_v4_reduction():
    vertices, faces = make_icosphere(2)
    mass, laplacian = reference_operators(vertices, faces)
    orbit_index, orbits, maps = v4_orbits(vertices)
    assert len(vertices) - 3 * len(faces) // 2 + len(faces) == 2
    assert abs(np.sum(mass) - FOUR_PI) < 1e-12
    assert np.max(np.abs(laplacian @ np.ones(len(vertices)))) < 1e-12
    reduced = np.arange(len(orbits), dtype=float)[orbit_index]
    assert max(np.max(np.abs(reduced - reduced[m])) for m in maps) == 0.0


def test_round_direct_audit_has_zero_mesh_calibrated_defect():
    vertices, faces = make_icosphere(2)
    audit = regge_curvature(vertices, faces, np.zeros(len(vertices)))
    assert audit["valid"]
    assert audit["gauss_bonnet_error"] < 1e-10
    target = np.asarray(audit["curvature"])
    assert np.max(np.abs(np.asarray(audit["curvature"]) - target)) == 0.0


def test_failure_taxonomy_and_control_primitive():
    thresholds = Thresholds()
    assert classifier(_fixture(), True, thresholds) == "converged"
    assert classifier(_fixture(), False, thresholds) == "numerical_failure"
    assert classifier(_fixture(triangle_margin_relative=[-0.1] * 10), True, thresholds) == "discrete_metric_breakdown"
    seam = [1.0, 0.95, 0.8, 0.6, 0.4, 0.3, 0.2, 0.12, 0.07, 0.03]
    assert classifier(_fixture(seam_area_ratio_min=seam), True, thresholds) == "seam_recollapse"
    interior = [1.0] * 5 + [2.0, 4.0, 8.0, 20.0, 40.0]
    assert classifier(_fixture(interior_abs_curvature_max=interior), True, thresholds) == "interior_concentration_or_divergence"
    assert classifier(_fixture(model_defect_sup=[0.2] * 10), True, thresholds) == "stalled_or_unresolved"
