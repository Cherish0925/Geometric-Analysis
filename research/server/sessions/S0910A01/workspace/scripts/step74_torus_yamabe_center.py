"""Construct analytic scalar -6 T^2-invariant torus center data.

We test the Strategist-suggested construction for the graph-neck route:
  h0 = dtheta^2 + exp(2 f(theta)) dx^2 + exp(-2 f(theta)) dy^2,
  f(theta)=sin(theta).
For theta-invariant conformal factor psi, scalar(h=psi^4 h0)=-6 is
  -8 psi'' - 2 (f')^2 psi = -6 psi^5.
The script solves this periodic ODE numerically and computes the resulting
arclength-gauge Ricci eigenvalues and Koiso center acceleration S'(0)=Ric_h^#+3I.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp

TWOPI = 2.0 * np.pi


def f(theta: np.ndarray) -> np.ndarray:
    return np.sin(theta)


def fp(theta: np.ndarray) -> np.ndarray:
    return np.cos(theta)


def ode(theta: np.ndarray, y: np.ndarray) -> np.ndarray:
    psi = y[0]
    dpsi = y[1]
    ddpsi = 0.75 * psi**5 - 0.25 * fp(theta) ** 2 * psi
    return np.vstack((dpsi, ddpsi))


def bc(ya: np.ndarray, yb: np.ndarray) -> np.ndarray:
    return np.array([ya[0] - yb[0], ya[1] - yb[1]])


def spectral_derivatives_periodic(values: np.ndarray, period: float) -> tuple[np.ndarray, np.ndarray]:
    """Return first and second periodic derivatives by FFT on an endpoint-free grid."""
    n = len(values)
    freqs = np.fft.fftfreq(n, d=period / n) * 2.0 * np.pi
    hat = np.fft.fft(values)
    d1 = np.fft.ifft(1j * freqs * hat).real
    d2 = np.fft.ifft(-(freqs**2) * hat).real
    return d1, d2


def solve_positive_periodic() -> solve_bvp:
    mesh = np.linspace(0.0, TWOPI, 300)
    avg_fp2 = 0.5
    amp = (avg_fp2 / 3.0) ** 0.25
    guesses = []
    for scale in [0.65, 0.8, 1.0, 1.25, 1.6]:
        psi0 = amp * scale * (1.0 + 0.08 * np.cos(2.0 * mesh))
        dpsi0 = amp * scale * (-0.16 * np.sin(2.0 * mesh))
        guesses.append(np.vstack((psi0, dpsi0)))
    last = None
    for guess in guesses:
        sol = solve_bvp(ode, bc, mesh, guess, tol=1e-8, max_nodes=20000, verbose=0)
        last = sol
        if sol.success and np.min(sol.sol(mesh)[0]) > 1e-6:
            return sol
    if last is None:
        raise RuntimeError("no solve attempted")
    return last


def main() -> None:
    sol = solve_positive_periodic()
    n = 2048
    theta = np.linspace(0.0, TWOPI, n, endpoint=False)
    y = sol.sol(theta)
    psi = y[0]
    dpsi = y[1]
    ddpsi_ode = 0.75 * psi**5 - 0.25 * fp(theta) ** 2 * psi
    residual = -8.0 * ddpsi_ode - 2.0 * fp(theta) ** 2 * psi + 6.0 * psi**5

    # Independent spectral check of the scalar equation.
    dpsi_fft, ddpsi_fft = spectral_derivatives_periodic(psi, TWOPI)
    residual_fft = -8.0 * ddpsi_fft - 2.0 * fp(theta) ** 2 * psi + 6.0 * psi**5

    # Arclength-gauge metric h = ds^2 + exp(2b(s))dx^2 + exp(2c(s))dy^2.
    b = 2.0 * np.log(psi) + f(theta)
    c = 2.0 * np.log(psi) - f(theta)
    b_th, b_thth = spectral_derivatives_periodic(b, TWOPI)
    c_th, c_thth = spectral_derivatives_periodic(c, TWOPI)
    # d/ds = psi^{-2} d/dtheta, d_s^2 F = psi^{-4}F_thth - 2 psi^{-5}psi_th F_th.
    b_s = psi ** (-2) * b_th
    c_s = psi ** (-2) * c_th
    b_ss = psi ** (-4) * b_thth - 2.0 * psi ** (-5) * dpsi_fft * b_th
    c_ss = psi ** (-4) * c_thth - 2.0 * psi ** (-5) * dpsi_fft * c_th
    ric_s = -b_ss - c_ss - b_s**2 - c_s**2
    ric_x = -b_ss - b_s * (b_s + c_s)
    ric_y = -c_ss - c_s * (b_s + c_s)
    scalar = ric_s + ric_x + ric_y
    sprime = np.vstack((ric_s + 3.0, ric_x + 3.0, ric_y + 3.0))

    length = float((TWOPI / n) * np.sum(psi**2))
    out = {
        "step": 74,
        "construction": "h0=dtheta^2+exp(2 sin theta) dx^2+exp(-2 sin theta) dy^2; solve -8 psi''-2 cos^2(theta) psi=-6 psi^5",
        "solve_bvp_success": bool(sol.success),
        "solve_bvp_message": str(sol.message),
        "mesh_nodes": int(sol.x.size),
        "psi_min": float(np.min(psi)),
        "psi_max": float(np.max(psi)),
        "circle_arclength_period_after_conformal_change": length,
        "algebraic_residual_sup_using_ode_rhs_not_independent": float(np.max(np.abs(residual))),
        "independent_residual_sup_fft_second_derivative": float(np.max(np.abs(residual_fft))),
        "scalar_min_arclength_formula": float(np.min(scalar)),
        "scalar_max_arclength_formula": float(np.max(scalar)),
        "scalar_mean_arclength_formula": float(np.mean(scalar)),
        "koiso_trace_Sprime_min": float(np.min(np.sum(sprime, axis=0))),
        "koiso_trace_Sprime_max": float(np.max(np.sum(sprime, axis=0))),
        "koiso_Sprime_eigenvalue_ranges": {
            "normal_circle_direction": [float(np.min(sprime[0])), float(np.max(sprime[0]))],
            "x_direction": [float(np.min(sprime[1])), float(np.max(sprime[1]))],
            "y_direction": [float(np.min(sprime[2])), float(np.max(sprime[2]))],
        },
        "anisotropy_sup_Sprime_minus_I": float(np.max(np.abs(sprime - 1.0))),
        "ricci_eigenvalue_ranges": {
            "circle": [float(np.min(ric_s)), float(np.max(ric_s))],
            "x": [float(np.min(ric_x)), float(np.max(ric_x))],
            "y": [float(np.min(ric_y)), float(np.max(ric_y))],
        },
        "notes": [
            "The ODE-right-hand residual is algebraic self-consistency; the FFT second-derivative residual and arclength scalar range are the independent numerical consistency checks.",
            "Trace S'(0)=3 is equivalent to scalar(h)=-6 and is required by the four-dimensional Ric=-3g center equation with S(0)=0.",
            "This constructs admissible diagonal T^2-invariant analytic center data; it does not construct the global Einstein half-core or the cusp match.",
        ],
    }
    path = Path("Sessions/S0910A01/workspace/data/step74_torus_yamabe_center.json")
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({k: out[k] for k in [
        "solve_bvp_success", "psi_min", "psi_max", "circle_arclength_period_after_conformal_change",
        "algebraic_residual_sup_using_ode_rhs_not_independent", "independent_residual_sup_fft_second_derivative",
        "scalar_min_arclength_formula", "scalar_max_arclength_formula", "anisotropy_sup_Sprime_minus_I"
    ]}, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
