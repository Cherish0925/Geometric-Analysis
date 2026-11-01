#!/usr/bin/env python3
"""Step 73: find GENUINE periodic fiber metrics with R = -6 on T^3.

Both u=b_{0,theta} and v=c_{0,theta} must be 2pi-periodic AND have
zero mean (so that b_0 and c_0 are themselves periodic).

Two-parameter shooting: fix v(theta) = B*sin(theta) (zero mean),
then solve for (u_0, B) such that:
  (1) u(2pi) = u(0)   [periodicity]
  (2) int_0^{2pi} u dtheta = 0   [zero mean]

Session: S0910A01.  Agent2 / Constructor.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root
import json
from pathlib import Path

results = {}

def fiber_system(theta, state, B):
    """ODE for [u, integral_of_u]"""
    u, I = state
    v = B * np.sin(theta)
    vp = B * np.cos(theta)
    du = 3 - u**2 - v**2 - u*v - vp
    dI = u  # running integral
    return [du, dI]

def shooting_residual(params):
    """Two residuals: periodicity and zero-mean"""
    u0, B = params
    sol = solve_ivp(fiber_system, [0, 2*np.pi], [u0, 0.0],
                    args=(B,), max_step=0.005, rtol=1e-12, atol=1e-14)
    if not sol.success:
        return [1e10, 1e10]
    u_end = sol.y[0, -1]
    I_end = sol.y[1, -1]
    return [u_end - u0, I_end]

# Scan (u0, B) parameter space
print("=== Scanning for zero-mean periodic fibers ===\n")

# First, check what happens with larger B or negative u0
# The mean of u depends on both u0 and B
# We need mean(u) = 0, so u must oscillate around zero

found_solutions = []

# Grid search
u0_range = np.linspace(-3, 3, 60)
B_range = np.linspace(0.1, 5, 60)

best_residual = 1e10
best_params = None

for u0_try in u0_range:
    for B_try in B_range:
        try:
            res = shooting_residual([u0_try, B_try])
            total_res = abs(res[0]) + abs(res[1])
            if total_res < best_residual:
                best_residual = total_res
                best_params = (u0_try, B_try)
        except:
            continue

print(f"  Best from grid: u0={best_params[0]:.3f}, B={best_params[1]:.3f}, "
      f"residual={best_residual:.4f}")

# Now try to refine with root finding
try:
    sol_opt = root(shooting_residual, best_params, method='hybr',
                   options={'maxfev': 2000, 'xtol': 1e-12})
    if sol_opt.success:
        u0_opt, B_opt = sol_opt.x
        res = shooting_residual([u0_opt, B_opt])
        print(f"  Refined: u0={u0_opt:.8f}, B={B_opt:.8f}")
        print(f"    periodicity: {res[0]:.2e}, zero-mean: {res[1]:.2e}")
        found_solutions.append({"u0": float(u0_opt), "B": float(B_opt),
                                "periodicity": float(res[0]),
                                "zero_mean": float(res[1])})
    else:
        print(f"  Root finding failed: {sol_opt.message}")
except Exception as e:
    print(f"  Root finding error: {e}")

# Also try multiple starting points
print("\n  Trying multiple starts...")
starts = [
    (0, 2.5), (-1, 3), (1, 3), (0, 4), (-0.5, 2),
    (0.5, 3.5), (-1.5, 2), (0, 1.5), (-2, 3), (1, 4),
    (0, 3), (-0.5, 3.5), (0.5, 4.5), (-1, 4), (0, 5),
]
for u0_try, B_try in starts:
    try:
        sol_opt = root(shooting_residual, [u0_try, B_try], method='hybr',
                       options={'maxfev': 2000, 'xtol': 1e-12})
        if sol_opt.success and max(abs(sol_opt.fun)) < 1e-8:
            u0_opt, B_opt = sol_opt.x
            if B_opt > 0:  # physical
                res = shooting_residual([u0_opt, B_opt])
                print(f"    u0={u0_opt:.8f}, B={B_opt:.8f}: "
                      f"per={res[0]:.2e}, mean={res[1]:.2e}")
                found_solutions.append({"u0": float(u0_opt), "B": float(B_opt),
                                        "periodicity": float(res[0]),
                                        "zero_mean": float(res[1])})
    except:
        continue

# Try alternative: v(theta) = B*sin(theta) + D*sin(2*theta) for more freedom
print("\n=== Alternative: v = B*sin + D*sin(2theta) ===\n")

def fiber_system_2mode(theta, state, B, D):
    u, I = state
    v = B * np.sin(theta) + D * np.sin(2*theta)
    vp = B * np.cos(theta) + 2*D * np.cos(2*theta)
    du = 3 - u**2 - v**2 - u*v - vp
    dI = u
    return [du, dI]

def shooting_2mode(params):
    u0, B, D = params
    sol = solve_ivp(fiber_system_2mode, [0, 2*np.pi], [u0, 0.0],
                    args=(B, D), max_step=0.005, rtol=1e-12, atol=1e-14)
    if not sol.success:
        return [1e10, 1e10]
    return [sol.y[0, -1] - u0, sol.y[1, -1]]

# Need 2 equations, 3 unknowns => 1-parameter family
# Fix D and solve for (u0, B)
for D_try in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
    for u0_try in np.linspace(-2, 2, 20):
        for B_try in np.linspace(0.5, 5, 20):
            try:
                sol_opt = root(lambda p: shooting_2mode([p[0], p[1], D_try]),
                               [u0_try, B_try], method='hybr',
                               options={'maxfev': 1000, 'xtol': 1e-10})
                if sol_opt.success and max(abs(sol_opt.fun)) < 1e-7:
                    u0_o, B_o = sol_opt.x
                    if B_o > 0:
                        res = shooting_2mode([u0_o, B_o, D_try])
                        if abs(res[0]) < 1e-7 and abs(res[1]) < 1e-4:
                            print(f"  D={D_try}: u0={u0_o:.6f}, B={B_o:.6f}, "
                                  f"per={res[0]:.2e}, mean={res[1]:.2e}")
                            found_solutions.append({
                                "u0": float(u0_o), "B": float(B_o),
                                "D": float(D_try),
                                "periodicity": float(res[0]),
                                "zero_mean": float(res[1])
                            })
                            break  # found one for this D
            except:
                continue
        else:
            continue
        break

if not found_solutions:
    print("  No zero-mean periodic solutions found!")
    print("  This means the T^2-inv diagonal ansatz with v=B*sin(theta)")
    print("  may not admit genuine periodic R=-6 fiber metrics.")

results["found_solutions"] = found_solutions
results["note"] = ("Fiber periodicity requires both u(2pi)=u(0) AND int(u)=0. "
                   "The single-mode v=B*sin(theta) shooting found u periodic but "
                   "with nonzero mean. Two-parameter search attempted.")

# For any found solutions, compute Koiso data
for sol_data in found_solutions:
    u0 = sol_data["u0"]
    B = sol_data["B"]
    D = sol_data.get("D", 0)

    N = 512
    th = np.linspace(0, 2*np.pi, N, endpoint=False)
    if D == 0:
        sol = solve_ivp(fiber_system, [0, 2*np.pi], [u0, 0],
                        args=(B,), max_step=0.003, t_eval=th, rtol=1e-12, atol=1e-14)
    else:
        sol = solve_ivp(fiber_system_2mode, [0, 2*np.pi], [u0, 0],
                        args=(B, D), max_step=0.003, t_eval=th, rtol=1e-12, atol=1e-14)
    u = sol.y[0]
    v = B * np.sin(th) + D * np.sin(2*th)
    vp = B * np.cos(th) + 2*D * np.cos(2*th)
    up = 3 - u**2 - v**2 - u*v - vp

    R3 = -2*(u**2 + v**2 + u*v + up + vp)
    sol_data["R3_range"] = [float(np.min(R3)), float(np.max(R3))]
    sol_data["R3_error"] = float(np.max(np.abs(R3 + 6)))

    # Koiso accelerations
    a_tt = u * v
    b_tt = v**2 + vp
    c_tt = u**2 + up
    sol_data["koiso_trace_range"] = [float(np.min(a_tt+b_tt+c_tt)),
                                      float(np.max(a_tt+b_tt+c_tt))]

out = Path("Sessions/S0910A01/workspace/data/step73_zero_mean_fiber_search.json")
with open(out, 'w') as fh:
    json.dump(results, fh, indent=2, default=str)
print(f"\nWrote {out}")
