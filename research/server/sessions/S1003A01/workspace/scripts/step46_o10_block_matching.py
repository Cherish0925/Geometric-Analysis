"""Step 46: exact scaling checks for the O10 TN/TNAdS block matching problem.

This script records two computations used in the accompanying note.

1.  For the Taub--NUT torsion parent
        Phi = sqrt(rho_*) e1 + a conjugate(f) e2,
    t_Phi = sqrt(m_*/2) d conjugate(f),
    the coefficient a and the exact integrated parent-Hessian energy are
    reconstructed from the known Taub--NUT energy.

2.  The exact one-dimensional minimum of integral |u''|^2 between endpoint
    first jets is evaluated.  It quantifies why independently resetting the
    affine torsion parent in cells of width L violates the inherited extensive
    Hessian bound, while jets sampled from a coherent macroscopic field have
    finite energy density.

The one-dimensional calculation is the normal-direction factor of an
anisotropic Wigner--Seitz cell.  Transverse measure cancels when converting to
energy per four-volume, so the reset density is 12 |p|^2/L^2.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


RHO_STAR = 4.0 / 3.0
M_STAR = 128.0 / 81.0
A_PARENT = math.sqrt(M_STAR) / (2.0 * RHO_STAR)  # sqrt(2)/3


def hermite_bending(L: float, u0: float, p0: float, u1: float, p1: float) -> dict:
    """Exact min integral_0^L |u''|^2 for fixed (u,u') at both ends."""
    delta = u1 - u0
    affine_defect = delta - 0.5 * L * (p0 + p1)
    slope_defect = p1 - p0
    term_value = 12.0 * affine_defect**2 / L**3
    term_slope = slope_defect**2 / L
    return {
        "affine_defect": affine_defect,
        "slope_defect": slope_defect,
        "value_term": term_value,
        "slope_term": term_slope,
        "energy": term_value + term_slope,
    }


def chain_energy(n: int, mode: str) -> float:
    """Bending energy on [0,1], using exact Hermite minimizers per cell."""
    L = 1.0 / n
    x = np.linspace(0.0, 1.0, n + 1)
    if mode == "reset":
        # Every local cell uses u=p(x-x_i), then resets u to zero at x_{i+1}.
        # Endpoint values are both zero and endpoint slopes are both p=1.
        return sum(hermite_bending(L, 0.0, 1.0, 0.0, 1.0)["energy"] for _ in range(n))
    if mode == "coherent_affine":
        u = x
        p = np.ones_like(x)
    elif mode == "smooth_sine":
        u = np.sin(2.0 * math.pi * x)
        p = 2.0 * math.pi * np.cos(2.0 * math.pi * x)
    else:
        raise ValueError(mode)
    return sum(
        hermite_bending(L, float(u[i]), float(p[i]), float(u[i + 1]), float(p[i + 1]))[
            "energy"
        ]
        for i in range(n)
    )


def main() -> None:
    # Known exact truncated TN rough-harmonic energy:
    # E_v(R)=8 pi^2 m_* ell^2 [R/(R+ell)]^2.
    # Since v=sqrt(m_*/2) d conjugate(f) and chi=a conjugate(f)e2,
    # int |nabla^2 chi|^2=(2a^2/m_*) E_v.
    parent_ratio_to_Ev = 2.0 * A_PARENT**2 / M_STAR
    parent_hessian_coeff = parent_ratio_to_Ev * 8.0 * math.pi**2 * M_STAR
    normalization_volume_coeff = 4.0 * math.pi**2
    parent_hessian_density = parent_hessian_coeff / normalization_volume_coeff

    rows = []
    sine_limit = (2.0 * math.pi) ** 4 / 2.0
    for n in [4, 8, 16, 32, 64, 128, 256]:
        L = 1.0 / n
        reset = chain_energy(n, "reset")
        coherent = chain_energy(n, "coherent_affine")
        sine = chain_energy(n, "smooth_sine")
        rows.append(
            {
                "n": n,
                "L": L,
                "reset_energy_density": reset,
                "reset_times_L2": reset * L**2,
                "coherent_affine_energy": coherent,
                "smooth_sine_energy": sine,
                "smooth_sine_limit": sine_limit,
                "smooth_sine_relative_error": (sine - sine_limit) / sine_limit,
            }
        )

    # Outer boundary of a marked TNAdS block.  Put ell=L^3 and R=cL.
    # These dimensionless ratios expose the admissible interface scaling.
    c = (3.0 / 4.0) ** (1.0 / 3.0)
    boundary_rows = []
    for L in [0.2, 0.1, 0.05, 0.025, 0.0125]:
        ell = L**3
        R = c * L
        H = 1.0 + ell / R
        F = 1.0 + R * (R + 2.0 * ell) / 3.0
        m_ratio = R / (R + ell)
        # The next quantity uses only the scalar profile m(R), measured with
        # the TNAdS radial unit normal. It is not yet the norm of an actual
        # TNAdS negative spinor.
        tnads_scalar_profile_dm_dproper = math.sqrt(F / H) * M_STAR * ell / (R + ell) ** 2
        # The following energy and flux are exact for the Ricci-flat TN
        # harmonic section.  The TNAdS flux of the same scalar profile is F
        # times the TN flux, but no actual TNAdS spinor with exactly this norm
        # has been constructed.
        raw_tn_grad_v_sq = M_STAR * ell**2 / (R + ell) ** 4
        raw_tn_flux = 16.0 * math.pi**2 * M_STAR * ell**2 * m_ratio**2
        tnads_scalar_profile_flux = F * raw_tn_flux
        raw_tn_energy = 8.0 * math.pi**2 * M_STAR * ell**2 * m_ratio**2
        raw_tn_mass = (16.0 * math.pi**2 / 3.0) * M_STAR * ell * R**3
        # For Delta m=2|nabla v|^2-4m-2 Re<q,v>, q_TN=-2v_TN.
        raw_tn_q_pairing = 0.5 * (2.0 * raw_tn_energy - 4.0 * raw_tn_mass - raw_tn_flux)
        raw_tn_q_l2_lower = raw_tn_q_pairing**2 / raw_tn_mass
        boundary_rows.append(
            {
                "L": L,
                "ell": ell,
                "R": R,
                "H_minus_1_over_L2": (H - 1.0) / L**2,
                "F_minus_1_over_L2": (F - 1.0) / L**2,
                "one_minus_m_over_mstar_over_L2": (1.0 - m_ratio) / L**2,
                "tnads_scalar_profile_proper_dm_over_L": tnads_scalar_profile_dm_dproper / L,
                "raw_tn_grad_v_sq_over_L2": raw_tn_grad_v_sq / L**2,
                "raw_tn_flux_over_ell2": raw_tn_flux / ell**2,
                "tnads_scalar_profile_flux_over_ell2": tnads_scalar_profile_flux / ell**2,
                "raw_tn_energy_over_ell2": raw_tn_energy / ell**2,
                "raw_tn_mass_over_ell2": raw_tn_mass / ell**2,
                "raw_tn_q_pairing_over_ell2": raw_tn_q_pairing / ell**2,
                "raw_tn_q_l2_lower_over_L6": raw_tn_q_l2_lower / L**6,
                "fiber_length_over_ell": 4.0 * math.pi * math.sqrt(F / H),
            }
        )

    out = {
        "constants": {
            "rho_star": RHO_STAR,
            "m_star": M_STAR,
            "a_parent": A_PARENT,
            "a_parent_exact": "sqrt(2)/3",
            "parent_ratio_to_Ev": parent_ratio_to_Ev,
            "parent_ratio_to_Ev_exact": "9/32",
            "truncated_parent_hessian":
                "(32*pi^2/9)*ell^2*(R/(R+ell))^2",
            "asymptotic_parent_hessian_coeff_over_ell2": parent_hessian_coeff,
            "normalization_cell_volume_coeff_over_ell2": normalization_volume_coeff,
            "parent_hessian_density_per_normalization_volume": parent_hessian_density,
            "parent_hessian_density_exact": "8/9",
        },
        "hermite_identity": {
            "formula":
                "12/L^3*(u1-u0-L*(p0+p1)/2)^2 + (p1-p0)^2/L",
            "reset_density_formula": "12*p^2/L^2",
            "bounded_density_jet_scaling":
                "p1-p0=O(L), u1-u0-L*(p0+p1)/2=O(L^2)",
        },
        "finite_marked_block_boundary": {
            "definition": "ell=L^3, R=(3/4)^(1/3)*L on exact TNAdS",
            "expected_orders": {
                "metric_departure": "O(L^2)",
                "amplitude_departure": "O(L^2)",
                "tnads_scalar_profile_proper_normal_derivative_of_m": "O(L)",
                "raw_tn_rough_harmonic_gradient_square": "O(L^2)",
                "transmitted_geometric_circle_degree_under_circle_compatible_extension": 1,
                "raw_tn_mass_flux": "O(ell^2)=O(L^6), not zero",
                "q_small_flux_requirement":
                    "Phi_mass=2E-4M+o(ell^2); at the balance radius its leading mean is zero",
                "raw_tn_q_pairing":
                    "-2M=-8*pi^2*m_star*ell^2 at R=(3/4)^(1/3)L; the Ricci-flat TN field is inadmissible at the desired residual scale",
                "tnads_warning":
                    "TNAdS scalar-profile flux equals F times raw TN flux; a TNAdS spinor/resolvent has not been constructed",
            },
            "rows": boundary_rows,
        },
        "chains": rows,
    }

    out_path = Path(__file__).resolve().parents[1] / "data" / "step46" / "o10_block_matching.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
