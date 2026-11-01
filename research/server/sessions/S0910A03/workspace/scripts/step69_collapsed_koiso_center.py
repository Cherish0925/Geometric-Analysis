"""Construct a rank-two collapsed analytic T^3 family with scalar curvature -6.

Start from h = dtheta^2 + exp(2 f(theta)) dX^2 + exp(-2 f(theta)) dY^2,
f(theta)=A sin(theta).  Its scalar curvature is -2(f')^2.  Solve the
3-dimensional Yamabe ODE for q=u^4 h with R_q=-6, then report the Ricci
endomorphism and Koiso initial acceleration S'(0)=Ric_q^#+3I.

For q_N on unit-period x,y coordinates replace dX,dY by dx/N,dy/N.
All q_N are locally isometric, R=-6, and Vol(q_N)=Vol(q_1)/N^2.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp

A = 1.0
TWOPI = 2.0 * np.pi


def f(theta):
    return A * np.sin(theta)


def fp(theta):
    return A * np.cos(theta)


def fpp(theta):
    return -A * np.sin(theta)


def ode(theta, y):
    u, up = y
    # -8 u'' - 2 (f')^2 u = -6 u^5.
    upp = 0.75 * u**5 - 0.25 * fp(theta) ** 2 * u
    return np.vstack((up, upp))


def bc(ya, yb):
    return np.array([ya[0] - yb[0], ya[1] - yb[1]])


def main():
    theta = np.linspace(0.0, TWOPI, 801)
    u0 = (np.mean(fp(theta) ** 2) / 3.0) ** 0.25
    guess = np.vstack((u0 * (1.0 + 0.02 * np.cos(2 * theta)),
                       -0.04 * u0 * np.sin(2 * theta)))
    sol = solve_bvp(ode, bc, theta, guess, tol=1e-10, max_nodes=30000)
    if not sol.success:
        raise RuntimeError(sol.message)

    th = np.linspace(0.0, TWOPI, 4001)
    u, up = sol.sol(th)
    upp = ode(th, np.vstack((u, up)))[1]
    phi_p = 2.0 * up / u
    phi_pp = 2.0 * (upp / u - (up / u) ** 2)

    # Ric(q) as an endomorphism, in the h-orthonormal frame. Since q=u^4 h,
    # multiply the (0,2) conformal Ricci components by u^{-4}.
    ric0_cov_h = -2.0 * fp(th) ** 2 - 2.0 * phi_pp
    ricx_cov_h = -fpp(th) - fp(th) * phi_p - phi_pp - phi_p**2
    ricy_cov_h = fpp(th) + fp(th) * phi_p - phi_pp - phi_p**2
    ric = np.vstack((ric0_cov_h, ricx_cov_h, ricy_cov_h)) / u**4
    scalar = np.sum(ric, axis=0)
    sprime = ric + 3.0

    # dV_q = u^6 dtheta dX dY, with unit X,Y periods.
    vol1 = np.trapz(u**6, th)
    yamabe_res = -8.0 * upp - 2.0 * fp(th) ** 2 * u + 6.0 * u**5
    trace_sprime = np.sum(sprime, axis=0)

    samples = {}
    for N in [1, 10, 100, 1000]:
        samples[str(N)] = {
            "volume": float(vol1 / N**2),
            "lattice_lengths_relative": [1.0, 1.0 / N, 1.0 / N],
            "matching_cover_lattice_before_cusp_scaling": [float(N), 1.0, 1.0],
            "matching_uniform_cusp_scale": float(1.0 / N),
        }

    result = {
        "A": A,
        "solver_success": bool(sol.success),
        "solver_nodes": int(sol.x.size),
        "u_min": float(np.min(u)),
        "u_max": float(np.max(u)),
        "yamabe_equation_sup_residual": float(np.max(np.abs(yamabe_res))),
        "scalar_min": float(np.min(scalar)),
        "scalar_max": float(np.max(scalar)),
        "scalar_minus_target_sup": float(np.max(np.abs(scalar + 6.0))),
        "ricci_endomorphism_min": [float(np.min(ric[i])) for i in range(3)],
        "ricci_endomorphism_max": [float(np.max(ric[i])) for i in range(3)],
        "koiso_Sprime_min": [float(np.min(sprime[i])) for i in range(3)],
        "koiso_Sprime_max": [float(np.max(sprime[i])) for i in range(3)],
        "koiso_Sprime_trace_sup": float(np.max(np.abs(trace_sprime))),
        "volume_N1": float(vol1),
        "quotient_samples": samples,
        "interpretation": {
            "local_geometry": "independent of N after X=x/N,Y=y/N",
            "scalar": "exactly -6 up to numerical ODE residual",
            "volume_scaling": "N^-2",
            "cusp_match": "degree-N cover in theta has lattice (N,1,1); truncation scale 1/N gives (1,1/N,1/N)",
        },
    }
    out = Path(__file__).resolve().parents[1] / "data" / "step69_collapsed_koiso_center.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
