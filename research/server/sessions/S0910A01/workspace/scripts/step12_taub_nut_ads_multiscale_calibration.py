#!/usr/bin/env python3
"""
Step 12 multiscale calibration for Taub--NUT--AdS.

This script uses the exact invariant formulas independently computed by S0910A03
and checked by the coordinate tensor computation in
step12_taub_nut_ads_coordinate_curvature.py:

  Ric = -g, s=-4,
  |W|^2_(0,4) = 32 nu^2 (4 nu^2 - 3)^2 / (3 (r+nu)^6),
  dVol/dr (complete Hopf orbit) = 32 pi^2 nu (r^2-nu^2).

The LeBrun/Chern--Weil norm |W^+|^2 is the Hilbert--Schmidt norm of the
curvature-operator block, i.e. one quarter of the corresponding four-index
Weyl norm.  In the coordinate orientation used by the tensor script W^+=0;
reversing orientation puts the nonzero half-flat block into W^+ with eigenvalues
(a,a,-2a), a=2 nu(4nu^2-3)/(3(r+nu)^3).

The computation distinguishes three mechanisms:
  1. A large ball containing the NUT has collapsed cover because the Hopf fiber
     contracts, but its mean curvature energy diverges as nu^{-1}; it is not a
     maximal-function good ball controlling all radii.
  2. A smaller annular buffered domain avoiding the NUT unwraps the Hopf fiber;
     after z=2nu psi it converges to H^4_{sec=-1/3}, with W^+=0 and calibrated
     defect 16 in the coordinate orientation.
  3. The shell where the nonzero half has calibrated magnitude occurs at
     r ~ 576^{1/6} nu^{1/3}; this scale tends to zero and does not provide a
     fixed-scale calibrated region.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGS = ROOT / "figures"
DATA.mkdir(exist_ok=True)
FIGS.mkdir(exist_ok=True)


def w_full_04_sq(nu: float, r: float) -> float:
    return 32.0 * nu**2 * (4.0*nu**2 - 3.0)**2 / (3.0 * (r + nu)**6)


def w_block_hs_sq(nu: float, r: float) -> float:
    return w_full_04_sq(nu, r) / 4.0


def half_flat_eigs(nu: float, r: float):
    a = 2.0 * nu * (4.0*nu**2 - 3.0) / (3.0 * (r + nu)**3)
    return np.array([a, a, -2*a], dtype=float)


def volume_nut_to_R(nu: float, R: float) -> float:
    # Complete orbit volume from r=nu to r=R.
    return 32.0 * math.pi**2 * nu * (((R**3 - nu**3)/3.0) - nu**2*(R-nu))


def full_weyl_energy_nut_to_R(nu: float, R: float) -> float:
    return (32.0 * math.pi**2 * (4.0*nu**2 - 3.0)**2 / 9.0) * (
        ((R-nu)**2 * (R**2 + 6.0*R*nu + 17.0*nu**2)) / ((R+nu)**4)
    )


def proper_radial_distance(nu: float, R: float, N: int = 20000) -> float:
    # Numerical integral int_nu^R dr/sqrt(F).  Used only for calibration of
    # fixed annular distances; exact closed form is unnecessary here.
    if R <= nu:
        return 0.0
    # Avoid the endpoint integrable singular by starting at t^2 substitution.
    xs = np.linspace(0.0, math.sqrt(R-nu), N+1)
    rs = nu + xs**2
    F = ((rs-nu)/(rs+nu)) * (1.0 + ((rs-nu)*(rs+3*nu))/3.0)
    integrand = np.empty_like(xs)
    integrand[0] = math.sqrt(8.0*nu)  # endpoint limit after r=nu+x^2
    integrand[1:] = 2.0*xs[1:]/np.sqrt(F[1:])
    return float(np.trapezoid(integrand, xs))


def defect_from_eigs(eigs, scalar: float = -4.0):
    eigs = np.array(eigs, dtype=float)
    u2 = float(np.sum(eigs*eigs))
    u = math.sqrt(max(u2, 0.0))
    w = float(np.min(eigs))
    f = (2.0/3.0)*scalar - 2.0*math.sqrt(2.0/3.0)*u
    a = (2.0/3.0)*scalar + 2.0*w
    amin = min(a, 0.0)
    G = f*f - amin*amin
    CS = (scalar + 8.0*math.sqrt(6.0)*u)**2
    P = 2.0*u2 + scalar*scalar/24.0
    return {"u2": u2, "u": u, "w_min": w, "CS": CS, "G": G, "Fcal": CS + G, "P": P}


def coordinate_orientation_defect():
    # W^+=0, E=0, s=-4.
    return defect_from_eigs([0.0, 0.0, 0.0])


def reversed_orientation_defect(nu: float, r: float):
    return defect_from_eigs(half_flat_eigs(nu, r))


def calibrated_magnitude_radius(nu: float) -> float:
    # Solve w_block_hs_sq(nu,r)=1/24 exactly by monotonicity in r.
    lo = nu
    hi = 10.0
    while w_block_hs_sq(nu, hi) > 1.0/24.0:
        hi *= 2.0
    for _ in range(100):
        mid = 0.5*(lo+hi)
        if w_block_hs_sq(nu, mid) > 1.0/24.0:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo+hi)


def build_rows():
    rows = []
    fixed_rs = [0.35, 0.5, 0.75, 1.0]
    for nu in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
        for r in fixed_rs:
            if r <= nu:
                continue
            d0 = coordinate_orientation_defect()
            d1 = reversed_orientation_defect(nu, r)
            rows.append({
                "type": "fixed_annulus",
                "nu": nu,
                "r": r,
                "proper_dist_nut_to_r": proper_radial_distance(nu, r, N=4000),
                "W_full_04_sq": w_full_04_sq(nu, r),
                "W_block_hs_sq_nonzero_half": w_block_hs_sq(nu, r),
                "F_coordinate_orientation_Wplus_zero": d0["Fcal"],
                "P_coordinate_orientation": d0["P"],
                "F_reversed_orientation_nonzero_Wplus": d1["Fcal"],
                "P_reversed_orientation": d1["P"],
            })
        rc = calibrated_magnitude_radius(nu)
        dc = reversed_orientation_defect(nu, rc)
        rows.append({
            "type": "calibrated_magnitude_shell_reversed_orientation",
            "nu": nu,
            "r": rc,
            "r_over_nu_one_third": rc/(nu**(1.0/3.0)),
            "proper_dist_nut_to_r": proper_radial_distance(nu, rc, N=8000),
            "W_full_04_sq": w_full_04_sq(nu, rc),
            "W_block_hs_sq_nonzero_half": w_block_hs_sq(nu, rc),
            "F_reversed_orientation_nonzero_Wplus": dc["Fcal"],
            "P_reversed_orientation": dc["P"],
            "cumulative_full_W_energy_to_shell": full_weyl_energy_nut_to_R(nu, rc),
            "cumulative_volume_to_shell": volume_nut_to_R(nu, rc),
            "mean_full_W_to_shell": full_weyl_energy_nut_to_R(nu, rc)/volume_nut_to_R(nu, rc),
        })
        for R in [0.35, 0.5, 0.75, 1.0]:
            if R <= nu:
                continue
            V = volume_nut_to_R(nu, R)
            E = full_weyl_energy_nut_to_R(nu, R)
            rows.append({
                "type": "nut_to_fixed_R_cumulative",
                "nu": nu,
                "R": R,
                "proper_dist_nut_to_R": proper_radial_distance(nu, R, N=4000),
                "volume": V,
                "full_W_energy": E,
                "mean_full_W": E/V,
                "nu_times_mean_full_W": nu*E/V,
                "asymptotic_nu_mean_coefficient_3_over_R3": 3.0/(R**3),
            })
    return rows


def save_outputs(rows):
    csv_path = DATA / "step12_taub_nut_ads_multiscale.csv"
    keys = sorted({k for row in rows for k in row.keys()})
    with csv_path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for row in rows:
            w.writerow(row)

    summary = {
        "formula_W_full_04_sq": "32 nu^2 (4 nu^2 - 3)^2 / (3 (r+nu)^6)",
        "formula_W_block_hs_sq": "one quarter of full four-index Weyl norm",
        "formula_dVol_dr_complete_orbit": "32 pi^2 nu (r^2-nu^2)",
        "coordinate_orientation": "W^+=0, Ric=-g, s=-4, Fcal=16, P=2/3",
        "reversed_orientation": "W^+ eigenvalues (a,a,-2a), a=2 nu(4nu^2-3)/(3(r+nu)^3)",
        "calibrated_magnitude_asymptotic": "r ~ 576^(1/6) nu^(1/3) = 2*3^(1/3) nu^(1/3)",
        "fixed_R_cumulative_mean_asymptotic": "mean full four-index Weyl from NUT to fixed R ~ 3/(nu R^3)",
        "interpretation": [
            "A large buffered domain containing the NUT can keep the Hopf fiber contractible, but it has divergent centered mean curvature energy once the NUT core is included.",
            "A smaller annular buffered domain avoiding the NUT unwraps the Hopf circle; after z=2nu psi it converges to real hyperbolic 4-space with W=0 and coordinate-orientation Fcal=16.",
            "The radius where the nonzero half has calibrated norm tends to zero like nu^(1/3); it is not a fixed physical scale and its cumulative mean energy from the NUT diverges like nu^{-2}."
        ],
        "selected_rows": rows[:12],
        "output_csv": str(csv_path),
    }
    json_path = DATA / "step12_taub_nut_ads_multiscale_summary.json"
    json_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')

    # Optional figure for visual inspection.
    fig_path = FIGS / "step12_taub_nut_ads_multiscale.png"
    try:
        import matplotlib.pyplot as plt
        nus = [0.1, 0.03, 0.01, 0.003]
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
        for nu in nus:
            rs = np.geomspace(nu*1.02, 2.0, 500)
            ax[0].loglog(rs, [w_block_hs_sq(nu, r) for r in rs], label=f"nu={nu:g}")
            means = []
            for r in rs:
                means.append(full_weyl_energy_nut_to_R(nu, r)/volume_nut_to_R(nu, r))
            ax[1].loglog(rs, means, label=f"nu={nu:g}")
        ax[0].axhline(1/24, color='k', ls='--', lw=1, label='calibrated |W+|^2')
        ax[0].set_xlabel('outer radius r')
        ax[0].set_ylabel('nonzero half |W|^2 (HS/operator)')
        ax[0].set_title('Pointwise half-flat Weyl magnitude')
        ax[0].legend(fontsize=8)
        ax[1].set_xlabel('outer radius R from NUT')
        ax[1].set_ylabel('mean full four-index |W|^2 on [nu,R]')
        ax[1].set_title('Cumulative mean including NUT core')
        ax[1].legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(fig_path, dpi=180)
        plt.close(fig)
        summary["output_figure"] = str(fig_path)
        json_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    except Exception as exc:  # matplotlib may not be present; data is enough.
        summary["figure_error"] = repr(exc)
        json_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    return csv_path, json_path, fig_path if fig_path.exists() else None


def main():
    rows = build_rows()
    csv_path, json_path, fig_path = save_outputs(rows)
    print("Step 12 Taub--NUT--AdS multiscale calibration")
    print("Coordinate orientation W+=0 defect:", coordinate_orientation_defect())
    print("Asymptotic calibrated radius constant 576^(1/6)=", 576.0**(1.0/6.0))
    print("Saved CSV:", csv_path)
    print("Saved JSON:", json_path)
    if fig_path:
        print("Saved figure:", fig_path)
    print("\nSelected rows:")
    for row in rows[:10]:
        print(row)
    print("\nCalibrated shell rows:")
    for row in rows:
        if row.get('type') == 'calibrated_magnitude_shell_reversed_orientation':
            print(row)


if __name__ == '__main__':
    main()
