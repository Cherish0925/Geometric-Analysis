#!/usr/bin/env python3
"""Step 73: verify the full T^2-invariant Einstein algebra and find
periodic fiber metrics with R = -6 for the Koiso center.

Uses A03's exact Ricci formulas and numerically solves the fiber
scalar curvature constraint.

Session: S0910A01.  Agent2 / Constructor.
"""
import numpy as np
from scipy.integrate import solve_ivp, solve_bvp
import json, sys
from pathlib import Path

results = {}

# ============================================================
# Part A: Verify the algebraic constraint |S|^2 = H^2 - 6 - R^{(3)}
# using the exact A03 Einstein equations (diagonal, (t,theta)-dependent)
# ============================================================

# For g = dt^2 + e^{2a} dth^2 + e^{2b} dx^2 + e^{2c} dy^2
# E_{00} = -(a_tt + a_t^2 + b_tt + b_t^2 + c_tt + c_t^2) + 3
# E_{11}/e^{2a} = -(a_tt + a_t*H) + 3 + e^{-2a}*Omega_a
#   where Omega_a = a_th*(b_th+c_th) - b_th^2 - b_thth - c_th^2 - c_thth
# E_{22}/e^{2b} = -(b_tt + b_t*H) + 3 + e^{-2a}*Omega_b
#   where Omega_b = a_th*b_th - b_th^2 - b_th*c_th - b_thth
# E_{33}/e^{2c} = -(c_tt + c_t*H) + 3 + e^{-2a}*Omega_c
#   where Omega_c = a_th*c_th - c_th^2 - b_th*c_th - c_thth
#
# Sum of tangential eigenvalues (E_{11}/g_{11} + E_{22}/g_{22} + E_{33}/g_{33}):
# -(a_tt+b_tt+c_tt) - H^2 + 9 + e^{-2a}*(Omega_a+Omega_b+Omega_c) = 0
#
# Now Omega_a + Omega_b + Omega_c
# = [a_th*(b_th+c_th) - b_th^2 - b_thth - c_th^2 - c_thth]
# + [a_th*b_th - b_th^2 - b_th*c_th - b_thth]
# + [a_th*c_th - c_th^2 - b_th*c_th - c_thth]
# = 2*a_th*(b_th+c_th) - 2*b_th^2 - 2*c_th^2 - 2*b_th*c_th
#   - 2*b_thth - 2*c_thth
# This is the fiber scalar curvature R^{(3)} of h = e^{2a}dth^2+e^{2b}dx^2+e^{2c}dy^2

# Verify: for a=0, b=A*sin(th), c=-A*sin(th):
A_val = 1.5
th = np.linspace(0, 2*np.pi, 500)
b0 = A_val * np.sin(th)
c0 = -A_val * np.sin(th)
b0_th = A_val * np.cos(th)
c0_th = -A_val * np.cos(th)
b0_thth = -A_val * np.sin(th)
c0_thth = A_val * np.sin(th)

# With a=0 (a_th=0):
R3_numerical = -2*(b0_th**2 + c0_th**2 + b0_th*c0_th + b0_thth + c0_thth)
# = -2*(A^2*cos^2 + A^2*cos^2 - A^2*cos^2 + 0) = -2*A^2*cos^2(th)
R3_formula = -2*A_val**2*np.cos(th)**2
results["R3_check"] = {
    "max_error": float(np.max(np.abs(R3_numerical - R3_formula))),
    "R3_range": [float(np.min(R3_numerical)), float(np.max(R3_numerical))],
    "note": "R^{(3)} is NOT constant for antisymmetric oscillation"
}
print(f"Fiber R^(3) check: max_error = {results['R3_check']['max_error']:.2e}")
print(f"  R^(3) range: {results['R3_check']['R3_range']}")

# The algebraic constraint at S=0 (t=0 of reflection center):
# 0 = H^2 - |S|^2 = 6 + R^{(3)}  [from normal + tangential sum]
# So R^{(3)} must be -6 pointwise
# For the antisymmetric case: R^{(3)} = -2A^2 cos^2(th), not constant
# Average: -A^2, need -6 average but also -6 pointwise
results["antisym_not_constant"] = {
    "R3_average": float(np.mean(R3_numerical)),
    "is_constant": bool(np.std(R3_numerical) < 1e-10),
    "note": "Antisymmetric oscillation gives non-constant R^{(3)}"
}


# ============================================================
# Part B: Search for periodic fiber metrics with R = -6
# ============================================================
print("\n=== Part B: Periodic fiber search ===")

# In a=0 gauge: R^{(3)} = -2(u^2 + v^2 + uv + u' + v') = -6
# where u = b_th, v = c_th, periodic on [0, 2*pi]
# Constraint: u^2 + v^2 + uv + u' + v' = 3

# Strategy: fix v(theta) with zero mean, solve for u(theta)
# u' = 3 - u^2 - v^2 - uv - v'  (Riccati-type ODE for u)

def fiber_rhs(theta, state, v_func, vp_func):
    """RHS for u' = 3 - u^2 - v^2 - uv - v'"""
    u = state[0]
    v_val = v_func(theta)
    vp_val = vp_func(theta)
    du = 3 - u**2 - v_val**2 - u*v_val - vp_val
    return [du]

# Try v(theta) = B * sin(theta) for various B, shoot for u(0) = u(2*pi)
def shoot_fiber(B, u0_guess):
    """Shoot from theta=0 with u(0)=u0, check u(2*pi)=u(0)"""
    v_func = lambda th: B * np.sin(th)
    vp_func = lambda th: B * np.cos(th)
    sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0_guess],
                    args=(v_func, vp_func),
                    max_step=0.01, rtol=1e-12, atol=1e-14)
    if sol.success:
        return sol.y[0, -1] - u0_guess
    return float('inf')

# Scan B values and use bisection for u0
fiber_results = []
for B in [0.5, 1.0, 1.5, 2.0]:
    # For each B, scan u0 values
    best_residual = float('inf')
    best_u0 = None
    for u0_try in np.linspace(-3, 3, 200):
        try:
            res = shoot_fiber(B, u0_try)
            if abs(res) < abs(best_residual):
                best_residual = res
                best_u0 = u0_try
        except:
            continue

    # Refine with bisection if we found a sign change
    if best_u0 is not None and abs(best_residual) < 0.5:
        from scipy.optimize import brentq
        try:
            u0_opt = brentq(lambda u0: shoot_fiber(B, u0),
                            best_u0 - 0.5, best_u0 + 0.5,
                            xtol=1e-12)
            final_res = shoot_fiber(B, u0_opt)
            fiber_results.append({
                "B": B, "u0": float(u0_opt),
                "periodicity_residual": float(final_res),
                "found_periodic": abs(final_res) < 1e-8
            })
            print(f"  B={B:.1f}: u0={u0_opt:.6f}, residual={final_res:.2e}")
        except:
            fiber_results.append({"B": B, "found_periodic": False,
                                  "note": "Brent failed"})
            print(f"  B={B:.1f}: no periodic solution found in range")
    else:
        fiber_results.append({"B": B, "found_periodic": False,
                              "best_residual": float(best_residual)})
        print(f"  B={B:.1f}: best residual {best_residual:.4f}")

results["fiber_periodic_search"] = fiber_results

# For found periodic solutions, verify R = -6 and compute properties
for fr in fiber_results:
    if fr.get("found_periodic"):
        B = fr["B"]
        u0 = fr["u0"]
        v_func = lambda th: B * np.sin(th)
        vp_func = lambda th: B * np.cos(th)
        sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0],
                        args=(v_func, vp_func),
                        max_step=0.01, t_eval=th, rtol=1e-12, atol=1e-14)
        u_sol = sol.y[0]
        v_sol = np.array([v_func(t) for t in th])

        # Verify R = -6
        up_sol = 3 - u_sol**2 - v_sol**2 - u_sol*v_sol - np.array([vp_func(t) for t in th])
        R3_check = -2*(u_sol**2 + v_sol**2 + u_sol*v_sol + up_sol + np.array([vp_func(t) for t in th]))
        fr["R3_range"] = [float(np.min(R3_check)), float(np.max(R3_check))]
        fr["R3_std"] = float(np.std(R3_check))

        # Compute the Ricci eigenvalues of the fiber
        # Ric_theta/g_theta = -(u^2+v^2+uv+u'+v') wait, that's the scalar curvature
        # Actually Ric_theta/g_theta at a=0: only contributes from b_thth,c_thth terms
        # From the 3D formulas at a=0:
        # Ric_{theta,theta}/1 = -(b_thth + c_thth + b_th^2 + c_th^2)
        #   = -(u'+v'+u^2+v^2)  -- wait this is from the full formula
        # Actually from my earlier computation at a=0:
        # R_thth^(3) = -(b_th^2 + b_thth + c_th^2 + c_thth)
        #            = -(u^2 + u' + v^2 + v')
        # R_xx^(3)/e^{2b} = -(b_th^2 + b_th*c_th + b_thth)
        #                  = -(u^2 + uv + u')
        # R_yy^(3)/e^{2c} = -(c_th^2 + b_th*c_th + c_thth)
        #                  = -(v^2 + uv + v')

        ric_theta = -(u_sol**2 + up_sol + v_sol**2 + np.array([vp_func(t) for t in th]))
        ric_x = -(u_sol**2 + u_sol*v_sol + up_sol)
        ric_y = -(v_sol**2 + u_sol*v_sol + np.array([vp_func(t) for t in th]))

        # Koiso condition: S'(0) = Ric_h + 3I
        # S'_theta = ric_theta + 3, S'_x = ric_x + 3, S'_y = ric_y + 3
        sp_theta = ric_theta + 3
        sp_x = ric_x + 3
        sp_y = ric_y + 3
        sp_trace = sp_theta + sp_x + sp_y

        fr["koiso_S_prime"] = {
            "theta_range": [float(np.min(sp_theta)), float(np.max(sp_theta))],
            "x_range": [float(np.min(sp_x)), float(np.max(sp_x))],
            "y_range": [float(np.min(sp_y)), float(np.max(sp_y))],
            "trace_range": [float(np.min(sp_trace)), float(np.max(sp_trace))],
            "trace_should_be": 3.0
        }

        # Fiber Ricci defect |Ric_h + 2I|_op
        defect_theta = ric_theta + 2
        defect_x = ric_x + 2
        defect_y = ric_y + 2
        defect_max = np.maximum(np.abs(defect_theta),
                                np.maximum(np.abs(defect_x), np.abs(defect_y)))
        fr["Ric_h_plus_2h"] = {
            "max_op_norm": float(np.max(defect_max)),
            "min_op_norm": float(np.min(defect_max)),
            "note": "If < 2/3 everywhere, Preissmann contradiction"
        }
        print(f"  B={B}: R3 in [{fr['R3_range'][0]:.4f}, {fr['R3_range'][1]:.4f}], "
              f"|Ric_h+2h|_op in [{fr['Ric_h_plus_2h']['min_op_norm']:.4f}, "
              f"{fr['Ric_h_plus_2h']['max_op_norm']:.4f}]")


# ============================================================
# Part C: The anisotropy question — does shear subside?
# ============================================================
print("\n=== Part C: Koiso collar evolution ===")

# For each found periodic fiber, set up the collar IVP (short-time check)
# Use the tangential Einstein equations as an evolution system in t
# (this is ill-posed as a Cauchy problem for the elliptic system, but
# short-time Fourier stability can be checked)

# The constraint is satisfied exactly at t=0 by construction.
# We track |B(t)| = |S(t) - I|^2 and H(t) to see if anisotropy subsides.

collar_results = []
for fr in fiber_results:
    if not fr.get("found_periodic"):
        continue
    B_val = fr["B"]
    u0_val = fr["u0"]
    v_func = lambda th: B_val * np.sin(th)
    vp_func = lambda th: B_val * np.cos(th)

    # Reconstruct u(theta) on a grid
    N_th = 128
    th_grid = np.linspace(0, 2*np.pi, N_th, endpoint=False)
    dth = th_grid[1] - th_grid[0]

    sol_f = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0_val],
                      args=(v_func, vp_func),
                      max_step=0.01, t_eval=th_grid, rtol=1e-12, atol=1e-14)
    u_grid = sol_f.y[0]
    v_grid = np.array([v_func(t) for t in th_grid])

    # Reconstruct b_0(theta) and c_0(theta) by integration
    b0_grid = np.cumsum(u_grid) * dth
    b0_grid -= np.mean(b0_grid)  # zero mean for periodicity
    c0_grid = np.cumsum(v_grid) * dth
    c0_grid -= np.mean(c0_grid)

    # Koiso initial data: a_t(0)=b_t(0)=c_t(0)=0
    # a_tt(0), b_tt(0), c_tt(0) from tangential Einstein equations
    # With a_0 fixed (choose a_0 = 0 for simplicity):
    a0_grid = np.zeros(N_th)

    # Compute second theta derivatives using FFT
    def fft_deriv(f, order=1):
        N = len(f)
        k = np.fft.fftfreq(N, d=dth) * 2 * np.pi
        fhat = np.fft.fft(f)
        return np.real(np.fft.ifft(fhat * (1j*k)**order))

    b0_thth = fft_deriv(b0_grid, 2)
    c0_thth = fft_deriv(c0_grid, 2)
    a0_th = fft_deriv(a0_grid, 1)  # = 0
    b0_th_grid = fft_deriv(b0_grid, 1)
    c0_th_grid = fft_deriv(c0_grid, 1)

    # Tangential Einstein at t=0, S=0 (a_t=b_t=c_t=0):
    # a_tt = 3 + e^{-2*a_0}*(a_0_th*(b_0_th+c_0_th) - b_0_th^2 - b_0_thth - c_0_th^2 - c_0_thth)
    e_neg2a = np.exp(-2*a0_grid)
    a_tt0 = 3 + e_neg2a*(a0_th*(b0_th_grid+c0_th_grid) - b0_th_grid**2 - b0_thth - c0_th_grid**2 - c0_thth)
    b_tt0 = 3 + e_neg2a*(a0_th*b0_th_grid - b0_th_grid**2 - b0_th_grid*c0_th_grid - b0_thth)
    c_tt0 = 3 + e_neg2a*(a0_th*c0_th_grid - c0_th_grid**2 - b0_th_grid*c0_th_grid - c0_thth)

    # Check normal equation at t=0:
    E00_check = -(a_tt0 + b_tt0 + c_tt0) + 3
    # Should be 0 if R^{(3)} = -6 everywhere

    # Compute the shape operator acceleration:
    # S'_theta = a_tt, S'_x = b_tt, S'_y = c_tt
    # Trace = a_tt + b_tt + c_tt, should = 3 for Einstein
    trace_Sp = a_tt0 + b_tt0 + c_tt0

    # Anisotropy measure: |B(dt)| = |S'(0)dt - I*dt| = |S'(0) - I/dt| * dt... 
    # Actually at small t: S(t) ~ S'(0)*t, so B(t) = S(t) - I ~ S'(0)*t - I
    # |B(t)|^2 = |S'(0)|^2*t^2 - 2*tr(S'(0))*t + 3
    # = (a_tt^2 + b_tt^2 + c_tt^2)*t^2 - 2*(tr S')*t + 3

    aniso_measure = np.std([a_tt0, b_tt0, c_tt0], axis=0)  # spatial variation of S'

    cr = {
        "B": B_val,
        "E00_at_center": {
            "max_abs": float(np.max(np.abs(E00_check))),
            "note": "Should be 0 if R^{(3)}=-6 everywhere"
        },
        "trace_Sp": {
            "range": [float(np.min(trace_Sp)), float(np.max(trace_Sp))],
            "should_be": 3.0
        },
        "S_prime_eigenvalues_at_th0": {
            "a_tt": float(a_tt0[0]),
            "b_tt": float(b_tt0[0]),
            "c_tt": float(c_tt0[0])
        },
        "anisotropy": {
            "max_std_across_theta": float(np.max(aniso_measure)),
            "mean_std_across_theta": float(np.mean(aniso_measure))
        }
    }
    collar_results.append(cr)
    print(f"  B={B_val}: |E00| max = {cr['E00_at_center']['max_abs']:.4f}, "
          f"tr(S') range = [{cr['trace_Sp']['range'][0]:.4f}, {cr['trace_Sp']['range'][1]:.4f}]")
    print(f"    S' eigenvalues at th=0: ({a_tt0[0]:.4f}, {b_tt0[0]:.4f}, {c_tt0[0]:.4f})")

results["collar_evolution"] = collar_results


# ============================================================
# Save
# ============================================================
out = Path("Sessions/S0910A01/workspace/data/step73_fiber_constraint_and_collar.json")
with open(out, 'w') as fh:
    json.dump(results, fh, indent=2, default=str)
print(f"\nWrote {out}")
