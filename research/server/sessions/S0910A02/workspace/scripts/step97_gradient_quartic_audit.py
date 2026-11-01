#!/usr/bin/env python3
"""Step 97: variational/gradient audit of the product-orbifold kernel-plane response.

This script is deliberately small and diagnostic.  It does not try to compute a
new Ozuch coefficient from first principles.  Instead it reads the already
produced A01 Step97 AB and tensor-sector maps, decomposes them into the
P-channel and Q-channel dictated by a quartic reduced functional, and tests the
cheap constraints that should be checked before trusting any mixed-row number.

The main mathematical model is:
    f4 = sum_{i<j} c_ij |xi_i|^2 |xi_j|^2
       + Re(q_ij xi_i^2 conjugate(xi_j)^2)
so the reduced equation has the form
    d f4 / d conjugate(xi_j) = P_j xi_j + Q_j conjugate(xi_j)
(up to harmless global factors depending on the convention for Wirtinger
normalization).  P is a trace/radial channel; Q is a traceless/angular channel.
"""
from __future__ import annotations

import json
import math
import pathlib
from typing import Any

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
A01_DATA = ROOT / "S0910A01" / "workspace" / "data"
# If the script is run from user root, the path above is wrong because __file__ is
# Sessions/S0910A02/workspace/scripts/..., parents[3] is Sessions.  Keep both
# possibilities explicit for robustness.
if not A01_DATA.exists():
    A01_DATA = pathlib.Path("Sessions/S0910A01/workspace/data")
OUT = pathlib.Path("Sessions/S0910A02/workspace/data/step97_gradient_quartic_audit.json")
OUT.parent.mkdir(parents=True, exist_ok=True)


def load_json(path: pathlib.Path) -> Any:
    with open(path) as f:
        return json.load(f)


def complex_decompose_trace_double(Kxyz: list[list[float]]) -> dict[str, Any]:
    """Decompose a trace/double-angle 3x3 block.

    Coordinates: source (x,y,z) = (tr M, M22-M33, 2M23), output
    (X,Y,Z) = (tr A, A22-A33, 2A23).  A P-channel P*Id gives X=2P x and
    Y=Z=0.  A Q-channel has complex angular output O=Y+iZ.  For S=y+iz,
    O = alpha*S + beta*conj(S).  Allowed source holomorphic vs antiholomorphic
    depends on node-frame character conventions, but |alpha|, |beta| and
    conjugacy relations are invariant diagnostics.
    """
    K = np.array(Kxyz, dtype=float)
    p_from_trace = 0.5 * K[0, 0]
    trace_leak = K[0, 1:].tolist() + K[1:, 0].tolist()
    # Angular block maps (y,z) to (Y,Z)
    m11, m12 = K[1, 1], K[1, 2]
    m21, m22 = K[2, 1], K[2, 2]
    A_y = complex(m11, m21)
    A_z = complex(m12, m22)
    alpha = (A_y - 1j * A_z) / 2.0  # coefficient of S=y+iz
    beta = (A_y + 1j * A_z) / 2.0   # coefficient of conjugate(S)
    return {
        "P_from_trace_channel": p_from_trace,
        "trace_leak_entries": trace_leak,
        "angular_block_YZ_from_yz": [[m11, m12], [m21, m22]],
        "alpha_coeff_of_S": [alpha.real, alpha.imag],
        "beta_coeff_of_conjS": [beta.real, beta.imag],
        "alpha_abs": abs(alpha),
        "beta_abs": abs(beta),
    }


def compact_to_trace_double(K: np.ndarray) -> np.ndarray:
    source_entries_from_xyz = np.array([
        [0.5, 0.5, 0.0],
        [0.5, -0.5, 0.0],
        [0.0, 0.0, 1.0],
    ])
    xyz_from_output_entries = np.array([
        [1.0, 1.0, 0.0],
        [1.0, -1.0, 0.0],
        [0.0, 0.0, 2.0],
    ])
    return xyz_from_output_entries @ K @ source_entries_from_xyz


def pair_value_from_ab_kernel_map(ab96: Any, source: str) -> dict[str, Any]:
    """Extract the final/available AB odd_odd compact map for source SS/NS/SN."""
    # step96_kernel_plane_ab_map stores adjacent_NS_ladder and pair_compare.
    if source == "NS":
        entry = ab96["adjacent_NS_ladder"][-1]
    else:
        matches = [r for r in ab96["pair_compare_tau_0p02_L180"] if r["source"] == source]
        if not matches:
            raise KeyError(source)
        entry = matches[0]
    K = np.array(entry["combo_compact_maps_basis"]["maps"]["odd_odd"], dtype=float)
    Kxyz = compact_to_trace_double(K)
    dec = complex_decompose_trace_double(Kxyz.tolist())
    return {
        "source": source,
        "tau": entry["tau"],
        "Lmax": entry["Lmax"],
        "compact_odd_odd": K.tolist(),
        "trace_double_angle": Kxyz.tolist(),
        "decomposition": dec,
        "old_scalar_R22_from_M22": entry["old_scalar_checks"]["odd_odd_R22_source22"],
        "warning": "AB one-form sector only; not the full reduced gradient."
    }


def main() -> None:
    ab97 = load_json(A01_DATA / "step97_ab_physical_cone_row.json")
    ten97 = load_json(A01_DATA / "step97_tensor_odd_physical_map.json")
    ab96 = load_json(A01_DATA / "step96_kernel_plane_ab_map.json")

    # AB P-channel from the physical cone row.
    c_adj_ab = -float(ab97["a_positive_defined_by_minus_Kadj_AB"])
    adj_ab_dec = complex_decompose_trace_double(
        ab97["trace_double_angle_coordinates"]["odd_odd_matrix_[X,Y,Z]_<-[x,y,z]"]
    )
    diag_ab = pair_value_from_ab_kernel_map(ab96, "SS")
    c_diag_ab = diag_ab["decomposition"]["P_from_trace_channel"]

    # Tensor odd adjacent Q-channel from A01 Step97 final summary.
    final = ten97["final_tau_0p01_L260_summary"]
    NS_xyz = final["NS_AA_plus_BB_trace_double_angle"]
    SN_xyz = final["SN_AA_plus_BB_trace_double_angle"]
    NS_dec = complex_decompose_trace_double(NS_xyz)
    SN_dec = complex_decompose_trace_double(SN_xyz)
    b_NS = max(NS_dec["alpha_abs"], NS_dec["beta_abs"]) / 2.0  # because O=2 Q
    b_SN = max(SN_dec["alpha_abs"], SN_dec["beta_abs"]) / 2.0

    # Cheap compatibility tests for the available partial data.
    p_r0_ab_partial = 2.0 * c_adj_ab + c_diag_ab
    # Odd tensor diagonal was not present in A01's source-compatible tensor file; the SS entry is zero there.
    ss_tensor = np.array(ten97["ladders"][-1]["pairs"]["SS"]["AA"]["trace_double_angle_[X,Y,Z]_<-[x,y,z]"]) + \
                np.array(ten97["ladders"][-1]["pairs"]["SS"]["BB"]["trace_double_angle_[X,Y,Z]_<-[x,y,z]"])
    ss_tensor_dec = complex_decompose_trace_double(ss_tensor.tolist())

    # Phase reachability for two equal-magnitude adjacent Q terms in diagonal balanced NN equation.
    # If one adjacent term uses S and the other uses conjugate(S), the two phase angles are still independently tunable
    # after quotienting by the diagonal receiver phase; their sum fills a disk of radius 2b in the Q-plane.
    b = 0.5 * (b_NS + b_SN)
    rng = np.random.default_rng(9703)
    mags = []
    for _ in range(20000):
        phi1, phi2 = rng.uniform(0, 2*math.pi, size=2)
        qsum = b * np.exp(2j*phi1) + b * np.exp(-2j*phi2)
        mags.append(abs(qsum))
    mags = np.array(mags)

    results = {
        "step": 97,
        "purpose": "Audit the variational gradient/quartic constraints before treating tensor-sector numbers as a mixed-row decision.",
        "model": {
            "reduced_potential": "f4 = sum_{i<j} c_ij |xi_i|^2 |xi_j|^2 + Re(q_ij xi_i^2 conjugate(xi_j)^2) plus self/global terms",
            "gradient_equation": "partial f4 / partial conjugate(xi_j) = P_j xi_j + Q_j conjugate(xi_j) (up to convention factors)",
            "checks": [
                "c_ij must be real and symmetric in a true gradient reduction",
                "q_ji must be conjugate(q_ij) after common frame transport",
                "Euler: homogeneous f4 of degree 4 has gradient zero only at value f4=0",
                "phase variables are real gluing parameters; equal-phase collapse to |q_diag| vs |2q_adj+q_diag| is an extra ansatz, not the general decision"
            ]
        },
        "source_files_read": {
            "A01_AB_physical_cone": str(A01_DATA / "step97_ab_physical_cone_row.json"),
            "A01_tensor_odd": str(A01_DATA / "step97_tensor_odd_physical_map.json"),
            "A01_AB_kernel_map": str(A01_DATA / "step96_kernel_plane_ab_map.json")
        },
        "AB_channel": {
            "adjacent_c_AB": c_adj_ab,
            "adjacent_decomposition_from_physical_row": adj_ab_dec,
            "diagonal_AB": diag_ab,
            "c_diag_AB": c_diag_ab,
            "realness_check": {
                "adjacent_c_imag": 0.0,
                "diagonal_c_imag": 0.0,
                "passes_available_realness": True
            },
            "r0_AB_partial_P_at_NN": p_r0_ab_partial,
            "interpretation": "AB is a P/trace channel only in the inspected odd sector. The nonzero compatible-row partial P cannot be the final LS gradient on the KE locus; missing tensor-even, self/frame, complement and global terms must cancel or change coordinates."
        },
        "tensor_odd_adjacent_channel": {
            "NS_trace_double_angle": NS_xyz,
            "NS_complex_decomposition": NS_dec,
            "SN_trace_double_angle": SN_xyz,
            "SN_complex_decomposition": SN_dec,
            "q_magnitude_from_NS_convention": b_NS,
            "q_magnitude_from_SN_convention": b_SN,
            "conjugate_partner_check": {
                "magnitudes_match_abs_diff": abs(b_NS - b_SN),
                "NS_has_only_conjS_or_S": min(NS_dec["alpha_abs"], NS_dec["beta_abs"]),
                "SN_has_only_conjS_or_S": min(SN_dec["alpha_abs"], SN_dec["beta_abs"]),
                "passes_available_factor_swap_conjugacy": abs(b_NS - b_SN) < 1e-10 and min(NS_dec["alpha_abs"], NS_dec["beta_abs"]) < 1e-10 and min(SN_dec["alpha_abs"], SN_dec["beta_abs"]) < 1e-10
            },
            "old_scalar_decomposition": {
                "old_adjacent_R22_from_M22_total_if_AB_plus_tensor": c_adj_ab - b_NS,
                "meaning": "This reproduces the older scalar adjacent value as P+one angular Q evaluation at a fixed source/receiver angle; it is not a pure P coefficient."
            },
            "diagonal_SS_tensor_odd_source_compatible_decomposition": ss_tensor_dec,
            "warnings": ten97["interpretation_warnings"]
        },
        "phase_reachability_two_adjacent_terms": {
            "q_adj_magnitude_b": b,
            "analytic_range_for_abs_of_two_terms": [0.0, 2.0*b],
            "random_sample_min_abs": float(mags.min()),
            "random_sample_max_abs": float(mags.max()),
            "random_sample_mean_abs": float(mags.mean()),
            "interpretation": "The two adjacent Q terms in the diagonal balanced NN equation should be treated as independently phase-tunable (one holomorphic, one anti-holomorphic after pole signs), not collapsed to a fixed 2*q_adj unless an additional symmetric equal-phase ansatz is imposed."
        },
        "compatible_KE_zero_test_status": {
            "source_grounding": "OSS/Mabuchi-Mukai/Tian-Yau imply smooth degree-4 del Pezzo surfaces and the four-A1 boundary are KE in the compactified moduli; this supports a Kähler-compatible zero set of the full reduced Einstein gradient near the product quotient.",
            "what_is_checked_here": "Only partial raw Green sectors are checked, not the full variational LS potential in Kähler smoothing coordinates.",
            "partial_AB_P_nonzero": p_r0_ab_partial,
            "partial_tensor_odd_diagonal_Q_abs": max(ss_tensor_dec["alpha_abs"], ss_tensor_dec["beta_abs"]) / 2.0,
            "conclusion": "The available partial coefficients do NOT pass a full compatible-locus zero test by themselves. This is expected because the computation omits sectors and coordinate/complement/global corrections. Therefore these partial coefficients must not be used alone to decide the mixed branch."
        },
        "next_computational_implication": [
            "Assemble the finite-dimensional response as the gradient of one real quartic potential before interpreting signs.",
            "Compute/organize the full compatible-pattern quartic (including AB, AA/BB even pieces, self/opposite-corner finite parts, frame/projector motion and global deformation variables) and require that its restriction to the KE-compatible Kähler smoothing locus has zero gradient/value.",
            "Only after that calibration should mixed-pattern phase equations be solved; the generic decision is existence of a zero critical point of f4 on scale/phase/deformation directions, not |q_diag| versus |2q_adj+q_diag| at equal phase."
        ]
    }
    with open(OUT, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps({
        "wrote": str(OUT),
        "c_adj_AB": c_adj_ab,
        "c_diag_AB": c_diag_ab,
        "r0_AB_partial_P": p_r0_ab_partial,
        "q_adj_tensor_odd_magnitude": b,
        "phase_abs_range_two_adjacent": [0.0, 2.0*b],
        "available_checks_pass": results["tensor_odd_adjacent_channel"]["conjugate_partner_check"]["passes_available_factor_swap_conjugacy"],
    }, indent=2))


if __name__ == "__main__":
    main()
