#!/usr/bin/env python3
"""Step 72 graph-neck weighted shear budget tests.

The point is to turn A03's reflection-core identity into a reusable numerical
necessary test for proposed T^3-neck constructions.

For a Gaussian metric g = dt^2 + h_t with shape operator S and H=tr S, put
B=S-I and b=H-3.  With E = Ric + 3g, the normal equation gives

    b' + 2 b + |B|^2 = - E_00.

Therefore along each normal trajectory

    e^{2R} b(R) - b(0) + int_0^R e^{2t}|B|^2 dt
       = - int_0^R e^{2t} E_00 dt.

If a proposed reflection-to-cusp core has S(0)=0 and H(R)=3, then b(0)=-3,
b(R)=0, and any pointwise bound |E_00| <= delta must satisfy

    delta >= 2(3 + int e^{2t}|B|^2 dt)/(e^{2R}-1).

This file evaluates that weighted shear quantity together with the full Ricci
residual for several toy profiles and low-resolution T^2-invariant BVP runs.
It is a necessary test only; small value here is not a construction.
"""
from __future__ import annotations

import json
import math
import traceback
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from scipy.integrate import solve_bvp

TWOPI = 2 * np.pi


def spec_deriv(v: np.ndarray, order: int = 1) -> np.ndarray:
    """Spectral d^order/dtheta^order for 2pi-periodic samples."""
    n = len(v)
    m = np.arange(n // 2 + 1)
    vc = np.fft.rfft(v)
    return np.fft.irfft((1j * m) ** order * vc, n=n)


def spec_project(v: np.ndarray, M: int) -> np.ndarray:
    n = len(v)
    vc = np.fft.rfft(v)
    vc[M + 1 :] = 0
    return np.fft.irfft(vc, n=n)


def build_koiso_center(A: float = 1.0, npts: int = 512) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """A03's scalar-minus-six T^2-invariant conformal center model."""
    th = np.linspace(0, TWOPI, npts, endpoint=False)
    f_val = A * np.sin(th)

    def ode(x, y):
        u, up = y
        return np.vstack((up, 0.75 * u**5 - 0.25 * (A * np.cos(x)) ** 2 * u))

    def bc(ya, yb):
        return np.array([ya[0] - yb[0], ya[1] - yb[1]])

    x = np.linspace(0, TWOPI, 801)
    u0 = (np.mean((A * np.cos(x)) ** 2) / 3) ** 0.25
    guess = np.vstack((u0 * (1 + 0.02 * np.cos(2 * x)), -0.04 * u0 * np.sin(2 * x)))
    sol = solve_bvp(ode, bc, x, guess, tol=1e-11, max_nodes=40000)
    if not sol.success:
        raise RuntimeError(sol.message)
    u = sol.sol(th)[0]
    a0 = 2 * np.log(u)
    b0 = 2 * np.log(u) + f_val
    c0 = 2 * np.log(u) - f_val
    return th, a0, b0, c0


def spatial_accel(a: np.ndarray, b: np.ndarray, c: np.ndarray,
                  da: np.ndarray, db: np.ndarray, dc: np.ndarray, M: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Accelerations from E_11=E_22=E_33=0 in A03's diagonal T^2-invariant gauge."""
    H = da + db + dc
    alpha = np.exp(-2 * a)
    ap = spec_deriv(a); bp = spec_deriv(b); cp = spec_deriv(c)
    bpp = spec_deriv(b, 2); cpp = spec_deriv(c, 2)
    rhs_a = 3 - da * H + alpha * (ap * bp + ap * cp - bp**2 - bpp - cp**2 - cpp)
    rhs_b = 3 - db * H + alpha * (ap * bp - bp**2 - bp * cp - bpp)
    rhs_c = 3 - dc * H + alpha * (ap * cp - bp * cp - cp**2 - cpp)
    return spec_project(rhs_a, M), spec_project(rhs_b, M), spec_project(rhs_c, M)


def ehat_components(a: np.ndarray, b: np.ndarray, c: np.ndarray,
                    da: np.ndarray, db: np.ndarray, dc: np.ndarray,
                    dda: np.ndarray, ddb: np.ndarray, ddc: np.ndarray) -> Dict[str, np.ndarray]:
    """Orthonormal components for E=Ric+3g for the diagonal T^2-invariant metric."""
    ap = spec_deriv(a); bp = spec_deriv(b); cp = spec_deriv(c)
    bpp = spec_deriv(b, 2); cpp = spec_deriv(c, 2)
    dbp = spec_deriv(db); dcp = spec_deriv(dc)
    alpha = np.exp(-2 * a)
    E00 = -(dda + ddb + ddc) - (da**2 + db**2 + dc**2) + 3
    E01_hat = np.exp(-a) * (da * bp + da * cp - db * bp - dc * cp - dbp - dcp)
    E11_hat = (-(da**2 + da * db + da * dc + dda) + 3
               + alpha * (ap * bp + ap * cp - bp**2 - bpp - cp**2 - cpp))
    E22_hat = (-(da * db + db**2 + db * dc + ddb) + 3
               + alpha * (ap * bp - bp**2 - bp * cp - bpp))
    E33_hat = (-(da * dc + db * dc + dc**2 + ddc) + 3
               + alpha * (ap * cp - bp * cp - cp**2 - cpp))
    return {
        "E00": E00,
        "E01_hat": E01_hat,
        "E11_hat": E11_hat,
        "E22_hat": E22_hat,
        "E33_hat": E33_hat,
    }


def shape_budget(t: np.ndarray, da: np.ndarray, db: np.ndarray, dc: np.ndarray,
                 E00: np.ndarray | None = None) -> Dict[str, object]:
    """Weighted normal identity quantities. Arrays have shape (nt, nth)."""
    R = float(t[-1])
    expw = np.exp(2 * t)[:, None]
    S = np.stack([da, db, dc], axis=2)
    H = da + db + dc
    b = H - 3
    B = S - 1.0
    shear_sq = np.sum(B * B, axis=2)
    shear_int = np.trapz(expw * shear_sq, t, axis=0)
    denom = math.exp(2 * R) - 1.0
    target_reflection_cusp_lb = 2 * (3.0 + shear_int) / denom
    actual_normal_lhs = math.exp(2 * R) * b[-1] - b[0] + shear_int
    actual_normal_lb = 2 * np.abs(actual_normal_lhs) / denom
    out: Dict[str, object] = {
        "R": R,
        "H_start_range": [float(np.min(H[0])), float(np.max(H[0]))],
        "H_end_range": [float(np.min(H[-1])), float(np.max(H[-1]))],
        "S_start_sup": float(np.max(np.abs(S[0]))),
        "S_end_minus_I_sup": float(np.max(np.abs(S[-1] - 1.0))),
        "shear_sq_sup": float(np.max(shear_sq)),
        "weighted_shear_integral_range": [float(np.min(shear_int)), float(np.max(shear_int))],
        "reflection_to_cusp_delta_lb_range": [float(np.min(target_reflection_cusp_lb)), float(np.max(target_reflection_cusp_lb))],
        "actual_boundary_normal_delta_lb_range": [float(np.min(actual_normal_lb)), float(np.max(actual_normal_lb))],
    }
    if E00 is not None:
        Eint = np.trapz(expw * E00, t, axis=0)
        identity_error = actual_normal_lhs + Eint
        out.update({
            "E00_sup": float(np.max(np.abs(E00))),
            "E00_weighted_average_range": [float(np.min(2 * Eint / denom)), float(np.max(2 * Eint / denom))],
            "normal_identity_trapz_error_sup": float(np.max(np.abs(identity_error))),
        })
    return out


def normal_only_profiles() -> List[Dict[str, object]]:
    """Profiles for the normal equation only; not claimed as full Einstein metrics."""
    rows: List[Dict[str, object]] = []
    for R in [1.0, 2.0, 4.0, 6.0, 8.0]:
        t = np.linspace(0, R, 2001)
        u = np.tanh(t)[:, None]
        zeros = np.zeros_like(u)
        bgt = shape_budget(t, u, u, u, E00=zeros)
        bgt["profile"] = "normal_equation_u=tanh(t); E00=0 but H(R)<3"
        rows.append(bgt)

    # A more relevant normal-only control: follow tanh(t) and patch the final
    # exponentially small deficit to hit S(R)=I exactly.  This tests whether the
    # shear term itself forces an order-one residual.  It does not: when B has
    # already decayed exponentially, the patch has exponentially small pointwise
    # E00, so the remaining obstruction must come from the tangential equations,
    # constraints, topology, and boundary-value solvability, not from the scalar
    # weighted normal identity alone.
    for R in [2.0, 4.0, 6.0, 8.0]:
        for L in [0.5, 1.0, min(2.0, R/2)]:
            t = np.linspace(0, R, 4001)
            d = 1.0 - math.tanh(R)
            x = np.clip((t - (R - L)) / L, 0, 1)
            phi = x * x * (3 - 2 * x)
            phip = np.where((0 < x) & (x < 1), 6 * x * (1 - x) / L, 0.0)
            u1 = np.tanh(t) + d * phi
            u1p = 1.0 / np.cosh(t)**2 + d * phip
            E00 = (3 * (1 - u1**2) - 3 * u1p)[:, None]
            bgt = shape_budget(t, u1[:, None], u1[:, None], u1[:, None], E00=E00)
            bgt["profile"] = f"tanh_plus_endpoint_patch_L={L:.3g}; H(R)=3"
            rows.append(bgt)

    # A false friend: if one spreads a generic interpolation over the whole neck
    # without solving the normal equation, the weighted normalized cost can look
    # small but the pointwise normal residual stays O(1), so it cannot satisfy
    # operator-norm Ricci pinching.
    for R in [4.0, 8.0, 12.0]:
        t = np.linspace(0, R, 4001)
        x = t / R
        u2 = x * x * (3 - 2 * x)
        u2p = 6 * x * (1 - x) / R
        E00 = (3 * (1 - u2**2) - 3 * u2p)[:, None]
        bgt = shape_budget(t, u2[:, None], u2[:, None], u2[:, None], E00=E00)
        bgt["profile"] = "whole_neck_smoothstep; H(R)=3 but E00_sup stays O(1)"
        rows.append(bgt)
    for R in [4.0, 8.0, 12.0]:
        for L in [0.5, 1.0, 2.0, max(2.0, R / 4)]:
            t = np.linspace(0, R, 2001)
            x = np.clip((t - (R - L)) / L, 0, 1)
            smooth = x * x * (3 - 2 * x)
            u = smooth[:, None]
            bgt = shape_budget(t, u, u, u, E00=None)
            bgt["profile"] = f"late_tail_transition_L={L:.3g}"
            rows.append(bgt)
    return rows


def run_bvp_case(A_koiso: float, M: int, n_phys: int, R: float,
                 target_type: str, nt_mesh: int = 25, nt_eval: int = 161) -> Dict[str, object]:
    _, a0_raw, b0_raw, c0_raw = build_koiso_center(A_koiso, n_phys)
    a0 = spec_project(a0_raw, M); b0 = spec_project(b0_raw, M); c0 = spec_project(c0_raw, M)
    if target_type == "round_cusp":
        aR = np.full(n_phys, R); bR = np.full(n_phys, R); cR = np.full(n_phys, R)
    elif target_type == "aniso_expand":
        aR = np.full(n_phys, np.mean(a0))
        bR = np.full(n_phys, np.mean(b0) + R)
        cR = np.full(n_phys, np.mean(c0) + R)
    else:
        raise ValueError(target_type)

    N = 6 * n_phys

    def fun(x_arr, y_arr):
        if y_arr.ndim == 1:
            y_arr = y_arr[:, None]
        out = np.zeros_like(y_arr)
        for j in range(y_arr.shape[1]):
            yj = y_arr[:, j]
            a = spec_project(yj[0*n_phys:1*n_phys], M)
            b = spec_project(yj[1*n_phys:2*n_phys], M)
            c = spec_project(yj[2*n_phys:3*n_phys], M)
            da = spec_project(yj[3*n_phys:4*n_phys], M)
            db = spec_project(yj[4*n_phys:5*n_phys], M)
            dc = spec_project(yj[5*n_phys:6*n_phys], M)
            dda, ddb, ddc = spatial_accel(a, b, c, da, db, dc, M)
            out[0*n_phys:1*n_phys, j] = da
            out[1*n_phys:2*n_phys, j] = db
            out[2*n_phys:3*n_phys, j] = dc
            out[3*n_phys:4*n_phys, j] = dda
            out[4*n_phys:5*n_phys, j] = ddb
            out[5*n_phys:6*n_phys, j] = ddc
        return out

    def bc(ya, yb):
        res = np.empty(N)
        res[0*n_phys:1*n_phys] = ya[0*n_phys:1*n_phys] - a0
        res[1*n_phys:2*n_phys] = ya[1*n_phys:2*n_phys] - b0
        res[2*n_phys:3*n_phys] = ya[2*n_phys:3*n_phys] - c0
        res[3*n_phys:4*n_phys] = yb[0*n_phys:1*n_phys] - aR
        res[4*n_phys:5*n_phys] = yb[1*n_phys:2*n_phys] - bR
        res[5*n_phys:6*n_phys] = yb[2*n_phys:3*n_phys] - cR
        return res

    t_mesh = np.linspace(0, R, nt_mesh)
    y_guess = np.zeros((N, nt_mesh))
    for j, tj in enumerate(t_mesh):
        s = tj / R
        y_guess[0*n_phys:1*n_phys, j] = (1 - s) * a0 + s * aR
        y_guess[1*n_phys:2*n_phys, j] = (1 - s) * b0 + s * bR
        y_guess[2*n_phys:3*n_phys, j] = (1 - s) * c0 + s * cR
        y_guess[3*n_phys:4*n_phys, j] = (aR - a0) / R
        y_guess[4*n_phys:5*n_phys, j] = (bR - b0) / R
        y_guess[5*n_phys:6*n_phys, j] = (cR - c0) / R

    sol = solve_bvp(fun, bc, t_mesh, y_guess, tol=1e-4, max_nodes=500, verbose=0)
    t = np.linspace(0, R, nt_eval)
    y = sol.sol(t)
    yp = fun(t, y)

    da_raw = y[3*n_phys:4*n_phys, :].T
    db_raw = y[4*n_phys:5*n_phys, :].T
    dc_raw = y[5*n_phys:6*n_phys, :].T
    # The Galerkin right-hand side projects all fields to M modes.  Project the
    # shape variables before measuring the residual/budget; otherwise unconstrained
    # high Fourier modes in the collocation state produce a misleadingly enormous
    # "residual" although they are outside the truncated system.
    da = np.vstack([spec_project(row, M) for row in da_raw])
    db = np.vstack([spec_project(row, M) for row in db_raw])
    dc = np.vstack([spec_project(row, M) for row in dc_raw])
    dda = yp[3*n_phys:4*n_phys, :].T
    ddb = yp[4*n_phys:5*n_phys, :].T
    ddc = yp[5*n_phys:6*n_phys, :].T
    raw_shape_highmode_sup = float(max(np.max(np.abs(da_raw-da)), np.max(np.abs(db_raw-db)), np.max(np.abs(dc_raw-dc))))

    component_sups = {"E00": [], "E01_hat": [], "E11_hat": [], "E22_hat": [], "E33_hat": []}
    E00_grid = np.zeros((nt_eval, n_phys))
    full_component_sup = 0.0
    for k in range(nt_eval):
        a = spec_project(y[0*n_phys:1*n_phys, k], M)
        b = spec_project(y[1*n_phys:2*n_phys, k], M)
        c = spec_project(y[2*n_phys:3*n_phys, k], M)
        comps = ehat_components(a, b, c, da[k], db[k], dc[k], dda[k], ddb[k], ddc[k])
        E00_grid[k] = comps["E00"]
        for key, arr in comps.items():
            m = float(np.max(np.abs(arr)))
            component_sups[key].append(m)
            full_component_sup = max(full_component_sup, m)

    bgt = shape_budget(t, da, db, dc, E00=E00_grid)
    return {
        "kind": "A03_style_spatial_Einstein_Dirichlet_BVP",
        "params": {"A": A_koiso, "M": M, "n_phys": n_phys, "R": R, "target": target_type},
        "success": bool(sol.success),
        "message": str(sol.message),
        "nodes": int(len(sol.x)),
        "rms_res_max": float(np.max(sol.rms_residuals)) if hasattr(sol, "rms_residuals") else None,
        "full_component_residual_sup": full_component_sup,
        "component_residual_sups": {k: float(max(v)) for k, v in component_sups.items()},
        "raw_shape_highmode_sup": raw_shape_highmode_sup,
        "budget": bgt,
        "interpretation": (
            "This solves only the spatial Dirichlet ODE/PDE block.  Large E00 or E01_hat means "
            "it is not an approximate Einstein neck even if solve_bvp converges."
        ),
    }


def main() -> None:
    out: Dict[str, object] = {
        "step": 72,
        "purpose": "weighted shear budget and full Ricci residual tests for graph-neck candidates",
        "normal_identity": "e^{2R}b(R)-b(0)+int e^{2t}|S-I|^2 dt = -int e^{2t}E00 dt",
        "reflection_to_cusp_lower_bound": "delta >= 2(3+int e^{2t}|S-I|^2 dt)/(e^{2R}-1)",
        "normal_only_profiles": normal_only_profiles(),
        "bvp_runs": [],
    }
    configs = [
        (1.0, 2, 16, 0.5, "aniso_expand"),
        (1.0, 2, 16, 1.0, "aniso_expand"),
        (1.0, 2, 16, 1.0, "round_cusp"),
    ]
    for cfg in configs:
        print("BVP", cfg, flush=True)
        try:
            out["bvp_runs"].append(run_bvp_case(*cfg))
        except Exception as exc:
            traceback.print_exc()
            out["bvp_runs"].append({"params": cfg, "error": repr(exc)})

    path = Path(__file__).resolve().parents[1] / "data" / "step72_graph_neck_shear_budget.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
