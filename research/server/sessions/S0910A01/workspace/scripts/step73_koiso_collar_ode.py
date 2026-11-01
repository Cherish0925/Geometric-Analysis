#!/usr/bin/env python3
"""Step 73: correct Koiso center analysis using exact algebraic formulas.

At t=0 with a_0=0, the Koiso initial data satisfy:
  a_tt(0) = u*v                   (where u=b_{0,theta}, v=c_{0,theta})
  b_tt(0) = v^2 + v'
  c_tt(0) = u^2 + u'
  trace = u^2 + v^2 + uv + u' + v' = 3  (constraint = R_h = -6)

The anisotropy decay for the ODE approximation (theta-independent):
  (f_i' - f_j')' + H*(f_i' - f_j') = 0
  => f_i'(t) - f_j'(t) = Delta_{ij}(0) * exp(-int_0^t H(s) ds)

Session: S0910A01.  Agent2 / Constructor.
"""
import numpy as np
from scipy.integrate import solve_ivp
import json, sys
from pathlib import Path

results = {}

# ============================================================
# Part A: Periodic fiber metrics with R = -6
# ============================================================
print("=== Part A: Fiber metrics with R=-6 ===\n")

def fiber_rhs(theta, state, B_val):
    u = state[0]
    v = B_val * np.sin(theta)
    vp = B_val * np.cos(theta)
    du = 3 - u**2 - v**2 - u*v - vp
    return [du]

from scipy.optimize import brentq

fiber_data = {}
for B in [0.5, 1.0, 1.5, 2.0]:
    # Find periodic u(theta) via shooting
    def residual(u0):
        sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0],
                        args=(B,), max_step=0.01, rtol=1e-12, atol=1e-14)
        return sol.y[0, -1] - u0 if sol.success else 1e10

    # Scan for sign change
    u0s = np.linspace(-3, 3, 300)
    ress = [residual(u0) for u0 in u0s]
    u0_opt = None
    for i in range(len(ress)-1):
        if ress[i]*ress[i+1] < 0:
            try:
                u0_opt = brentq(residual, u0s[i], u0s[i+1], xtol=1e-13)
                break
            except:
                continue

    if u0_opt is None:
        print(f"  B={B}: no periodic solution found")
        continue

    # Compute on grid
    N = 256
    th = np.linspace(0, 2*np.pi, N, endpoint=False)
    sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0_opt],
                    args=(B,), max_step=0.005, t_eval=th,
                    rtol=1e-12, atol=1e-14)
    u = sol.y[0]
    v = B * np.sin(th)
    vp = B * np.cos(th)
    up = 3 - u**2 - v**2 - u*v - vp

    # Verify R = -6
    R3 = -2*(u**2 + v**2 + u*v + up + vp)
    R3_err = np.max(np.abs(R3 + 6))

    # Koiso initial accelerations
    a_tt = u * v
    b_tt = v**2 + vp
    c_tt = u**2 + up
    trace_check = a_tt + b_tt + c_tt
    trace_err = np.max(np.abs(trace_check - 3))

    # Anisotropy measure: standard deviation of S' eigenvalues
    aniso = np.std(np.array([a_tt, b_tt, c_tt]), axis=0)

    # Fiber Ricci eigenvalues
    r_th = -(u**2 + v**2 + up + vp)
    r_x = -(u**2 + u*v + up)
    r_y = -(v**2 + u*v + vp)

    # Fiber defect |Ric_h + 2h|_op
    d_th = np.abs(r_th + 2)
    d_x = np.abs(r_x + 2)
    d_y = np.abs(r_y + 2)
    defect_op = np.maximum(d_th, np.maximum(d_x, d_y))

    fd = {
        "u0": float(u0_opt),
        "R3_max_error": float(R3_err),
        "trace_max_error": float(trace_err),
        "S_prime_at_theta0": [float(a_tt[0]), float(b_tt[0]), float(c_tt[0])],
        "S_prime_at_theta_pi2": [float(a_tt[N//4]), float(b_tt[N//4]), float(c_tt[N//4])],
        "anisotropy_max": float(np.max(aniso)),
        "anisotropy_mean": float(np.mean(aniso)),
        "fiber_defect_max": float(np.max(defect_op)),
        "fiber_defect_min": float(np.min(defect_op)),
        "Ric_h_eigenvalue_ranges": {
            "theta": [float(np.min(r_th)), float(np.max(r_th))],
            "x": [float(np.min(r_x)), float(np.max(r_x))],
            "y": [float(np.min(r_y)), float(np.max(r_y))]
        }
    }
    fiber_data[f"B={B}"] = fd
    print(f"  B={B}: u0={u0_opt:.6f}")
    print(f"    R3 error: {R3_err:.2e}, trace error: {trace_err:.2e}")
    print(f"    S'(theta=0): ({a_tt[0]:.4f}, {b_tt[0]:.4f}, {c_tt[0]:.4f})")
    print(f"    S'(theta=pi/2): ({a_tt[N//4]:.4f}, {b_tt[N//4]:.4f}, {c_tt[N//4]:.4f})")
    print(f"    |Ric_h+2h|_op: [{np.min(defect_op):.4f}, {np.max(defect_op):.4f}]")
    print(f"    Anisotropy: max={np.max(aniso):.4f}, mean={np.mean(aniso):.4f}")

results["fiber_metrics"] = fiber_data


# ============================================================
# Part B: ODE anisotropy decay estimate
# ============================================================
print("\n=== Part B: ODE anisotropy decay ===\n")

# For the ODE approximation (ignore theta-dependence):
# f_i'' + f_i' * H = 3  for i = 1,2,3
# Normal: sum(f_i'') + sum(f_i'^2) = 3
# Mean: H' + |S|^2 = 3

# Difference: delta_ij = f_i' - f_j' satisfies delta_ij' + H*delta_ij = 0
# So delta_ij(t) = delta_ij(0) * exp(-int_0^t H(s) ds)

# For reflection center: H(0) = 0
# Isotropic part: H' + H^2/3 + |shear|^2 = 3
# In isotropic limit: H'' = 3 - H^2, H = sqrt(3)*tanh(sqrt(3)*t)

# Anisotropy decay rate:
# int_0^t H(s) ds = int_0^t sqrt(3)*tanh(sqrt(3)*s) ds
#                 = log(cosh(sqrt(3)*t))
# So delta(t) = delta(0) * sech(sqrt(3)*t) -> 0 as t -> infinity

# Rate: exponential, ~ exp(-sqrt(3)*t) for large t

t_vals = np.linspace(0, 10, 1000)
H_iso = np.sqrt(3) * np.tanh(np.sqrt(3)*t_vals)
int_H = np.log(np.cosh(np.sqrt(3)*t_vals))
decay_factor = np.exp(-int_H)

# For different initial anisotropies, compute the decay
for B in [0.5, 1.0]:
    if f"B={B}" not in fiber_data:
        continue
    fd = fiber_data[f"B={B}"]
    sp = fd["S_prime_at_theta0"]
    # S'(0) eigenvalues at theta=0
    deltas_0 = [sp[i] - sp[j] for i in range(3) for j in range(i+1, 3)]
    max_delta_0 = max(abs(d) for d in deltas_0)

    # At time t: delta(t) ~ max_delta_0 * decay_factor(t)
    # Time for delta < 0.01:
    idx = np.argmax(max_delta_0 * decay_factor < 0.01)
    t_small = t_vals[idx] if idx > 0 else float('inf')

    print(f"  B={B}: max |delta_ij(0)| = {max_delta_0:.4f}")
    print(f"    Decay factor at t=1: {decay_factor[100]:.4f}")
    print(f"    Decay factor at t=3: {decay_factor[300]:.6f}")
    print(f"    Time for delta < 0.01: {t_small:.2f}")


# ============================================================
# Part C: Weighted shear budget for ODE approximation
# ============================================================
print("\n=== Part C: Weighted shear budget (ODE) ===\n")

# In the ODE approx:
# S_i(t) = S'_i(0)*t * (integral correction) -> not quite right
# Better: solve the full ODE system

def collar_ode(t, y, S_prime_0):
    """ODE for diagonal Einstein collar: f_i'' + f_i'*H = 3"""
    # y = [f1, f1', f2, f2', f3, f3']
    f1, f1p, f2, f2p, f3, f3p = y
    H = f1p + f2p + f3p
    f1pp = 3 - f1p * H
    f2pp = 3 - f2p * H
    f3pp = 3 - f3p * H
    return [f1p, f1pp, f2p, f2pp, f3p, f3pp]

for B in [0.5, 1.0]:
    if f"B={B}" not in fiber_data:
        continue
    fd = fiber_data[f"B={B}"]
    sp = fd["S_prime_at_theta0"]  # S'(0) eigenvalues at one theta

    # Initial conditions: f_i(0) = 0, f_i'(0) = 0 (reflection center)
    # But f_i''(0) = sp[i], so use small-time Taylor:
    # We need to track the shape operator s_i(t) = f_i'(t)
    # s_i' + s_i*H = 3, with s_i(0) = 0
    # s_i(dt) ~ sp[i]*dt, f_i(dt) ~ sp[i]*dt^2/2

    dt = 0.001
    y0 = [sp[0]*dt**2/2, sp[0]*dt,
          sp[1]*dt**2/2, sp[1]*dt,
          sp[2]*dt**2/2, sp[2]*dt]

    sol = solve_ivp(collar_ode, [dt, 15], y0, args=(sp,),
                    max_step=0.01, rtol=1e-10, atol=1e-12,
                    t_eval=np.linspace(dt, 15, 3000))

    t_col = sol.t
    s1 = sol.y[1]
    s2 = sol.y[3]
    s3 = sol.y[5]
    H_col = s1 + s2 + s3
    B2_col = (s1-1)**2 + (s2-1)**2 + (s3-1)**2  # |S-I|^2

    # Weighted shear: int_0^R e^{2t} |S-I|^2 dt
    e2t = np.exp(2*t_col)
    integrand = e2t * B2_col
    from scipy.integrate import cumulative_trapezoid
    ws_budget = cumulative_trapezoid(integrand, t_col, initial=0)

    # Normalized budget: 2*(3 + ws)/( e^{2R} - 1)
    norm_budget = 2*(3 + ws_budget) / (np.exp(2*t_col) - 1 + 1e-30)

    # H approach to 3
    H_deficit = 3 - H_col

    print(f"  B={B} (theta=0 slice):")
    for R_target in [2, 4, 6, 8, 10]:
        idx = np.argmin(np.abs(t_col - R_target))
        print(f"    R={R_target}: H={H_col[idx]:.6f}, 3-H={H_deficit[idx]:.2e}, "
              f"|S-I|^2={B2_col[idx]:.2e}, norm_budget={norm_budget[idx]:.2e}")

    results[f"collar_B={B}"] = {
        "R_values": [2, 4, 6, 8, 10],
        "H_values": [float(H_col[np.argmin(np.abs(t_col-R))]) for R in [2,4,6,8,10]],
        "B2_values": [float(B2_col[np.argmin(np.abs(t_col-R))]) for R in [2,4,6,8,10]],
        "norm_budget": [float(norm_budget[np.argmin(np.abs(t_col-R))]) for R in [2,4,6,8,10]]
    }


# ============================================================
# Part D: Comparison with isotropic tanh
# ============================================================
print("\n=== Part D: Comparison with isotropic tanh ===\n")

# Isotropic: all s_i = tanh(sqrt(3)*t)/sqrt(3) * sqrt(3) = tanh(sqrt(3)*t)
# Wait: for isotropic s1=s2=s3=s, normal eqn: 3s' + 3s^2 = 3 => s' = 1-s^2
# Solution: s = tanh(t) (with unit Einstein constant)
# But our normalization is Ric = -3g, so the ODE is f'' + f'*H = 3
# For isotropic f=f=f: 3f'' + 3(f')^2 = 3 => f'' + (f')^2 = 1
# And f'' + f'*3f' = 3 => f'' + 3(f')^2 = 3
# So f'' = 3 - 3(f')^2, f'(0)=0 => f' = tanh(sqrt(3)*t)

s_iso = np.tanh(np.sqrt(3)*t_vals)
B2_iso = 3*(s_iso - 1)**2
ws_iso = cumulative_trapezoid(np.exp(2*t_vals)*B2_iso, t_vals, initial=0)
norm_iso = 2*(3 + ws_iso) / (np.exp(2*t_vals) - 1 + 1e-30)

print("  Isotropic tanh (S=tanh(sqrt(3)*t)*I):")
for R_target in [2, 4, 6, 8, 10]:
    idx = np.argmin(np.abs(t_vals - R_target))
    print(f"    R={R_target}: s={s_iso[idx]:.6f}, |S-I|^2={B2_iso[idx]:.2e}, "
          f"norm_budget={norm_iso[idx]:.2e}")

# Key difference: isotropic has s_i = tanh(sqrt(3)*t) -> 1 uniformly
# Anisotropic has s_i converging to 1 at DIFFERENT rates but all -> 1
# The norm budget converges to 0 in BOTH cases
results["isotropic_comparison"] = {
    "R_values": [2, 4, 6, 8, 10],
    "s_iso": [float(s_iso[np.argmin(np.abs(t_vals-R))]) for R in [2,4,6,8,10]],
    "B2_iso": [float(B2_iso[np.argmin(np.abs(t_vals-R))]) for R in [2,4,6,8,10]],
    "norm_budget_iso": [float(norm_iso[np.argmin(np.abs(t_vals-R))]) for R in [2,4,6,8,10]]
}


# ============================================================
# Save
# ============================================================
out = Path("Sessions/S0910A01/workspace/data/step73_koiso_center_analysis.json")
with open(out, 'w') as fh:
    json.dump(results, fh, indent=2, default=str)
print(f"\nWrote {out}")
