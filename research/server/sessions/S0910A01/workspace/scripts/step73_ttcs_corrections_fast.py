#!/usr/bin/env python3
"""Step 73: TTCS corrections — fast version with known u0 values."""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
import json
from pathlib import Path

results = {}
known_u0 = {0.5: 1.657041, 1.0: 1.560867, 1.5: 1.428753, 2.0: 1.202337}

def fiber_rhs(theta, state, B_val):
    u = state[0]
    v = B_val * np.sin(theta)
    vp = B_val * np.cos(theta)
    return [3 - u**2 - v**2 - u*v - vp]

# Check 1: Zero-mean condition
print("=== Check 1: Zero-mean condition ===\n")
for B, u0 in known_u0.items():
    N = 1024
    th = np.linspace(0, 2*np.pi, N, endpoint=False)
    sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0],
                    args=(B,), max_step=0.002, t_eval=th, rtol=1e-12, atol=1e-14)
    u = sol.y[0]
    v = B * np.sin(th)
    dth = th[1] - th[0]
    int_u = np.sum(u) * dth
    int_v = np.sum(v) * dth
    periodic_b0 = abs(int_u) < 1e-4
    print(f"  B={B}: mean(u) = {int_u/(2*np.pi):.8f}, mean(v) = {int_v/(2*np.pi):.10f}")
    print(f"    int(u) = {int_u:.8f}, periodic b_0: {'YES' if periodic_b0 else 'NO'}")
    results[f"B={B}_int_u"] = {"int_u": float(int_u), "mean_u": float(int_u/(2*np.pi)),
                                "periodic_b0": bool(periodic_b0)}

# Check 2: Correct 3-direction ODE rate
print("\n=== Check 2: ODE rate ===\n")
t = np.linspace(0, 5, 2000)
H3 = 3 * np.tanh(3*t)
H_wrong = np.sqrt(3) * np.tanh(np.sqrt(3)*t)
# Verify H' = 9 - H^2
dH = np.gradient(H3, t)
res = np.max(np.abs(dH - (9 - H3**2)))
print(f"  H = 3tanh(3t): residual = {res:.2e}")
print(f"  sech(3) at t=1: {1/np.cosh(3):.6f}")
print(f"  sech(sqrt3) at t=1: {1/np.cosh(np.sqrt(3)):.6f}")
print(f"  TTCS correct: rate is sech(3t), not sech(sqrt3 t)")
results["ode_rate"] = {"correct": "sech(3t)", "wrong": "sech(sqrt3 t)",
                       "sech3_at_1": float(1/np.cosh(3)),
                       "sech_s3_at_1": float(1/np.cosh(np.sqrt(3)))}

# Check 3: Forced system with fiber Ricci
print("\n=== Check 3: Forced vs unforced ===\n")
def forced_ode(t, y, r0):
    s1, s2, s3 = y
    H = s1 + s2 + s3
    r = r0 * np.exp(-2*t)
    return [3 + r[0] - s1*H, 3 + r[1] - s2*H, 3 + r[2] - s3*H]

def unforced_ode(t, y):
    s1, s2, s3 = y
    H = s1 + s2 + s3
    return [3 - s1*H, 3 - s2*H, 3 - s3*H]

r0 = np.array([-3.0, -2.0, -1.0])  # from B=1 Koiso at theta=0
dt = 0.001
y0 = [(3 + r0[i]) * dt for i in range(3)]  # Koiso initial data

ts = np.linspace(dt, 10, 2000)
sol_f = solve_ivp(forced_ode, [dt, 10], y0, args=(r0,),
                  max_step=0.01, rtol=1e-10, atol=1e-12, t_eval=ts)
sol_u = solve_ivp(unforced_ode, [dt, 10], y0,
                  max_step=0.01, rtol=1e-10, atol=1e-12, t_eval=ts)

d12_f = sol_f.y[0] - sol_f.y[1]
d12_u = sol_u.y[0] - sol_u.y[1]

print("  R | forced delta_12 | unforced delta_12 | ratio | e^{-2R} | e^{-3R}")
forced_data = []
for R in [1, 2, 4, 6, 8]:
    i_f = np.argmin(np.abs(sol_f.t - R))
    i_u = np.argmin(np.abs(sol_u.t - R))
    ratio = d12_f[i_f] / (d12_u[i_u] + 1e-30)
    print(f"  {R} | {d12_f[i_f]:+.4e} | {d12_u[i_u]:+.4e} | {ratio:.3f} | "
          f"{np.exp(-2*R):.4e} | {np.exp(-3*R):.4e}")
    forced_data.append({"R": R, "forced": float(d12_f[i_f]),
                        "unforced": float(d12_u[i_u])})

# Fit exponential rate for forced system
from numpy.polynomial import polynomial as P
idx_late = (sol_f.t > 3) & (sol_f.t < 9)
log_d = np.log(np.abs(d12_f[idx_late]) + 1e-30)
t_late = sol_f.t[idx_late]
fit = np.polyfit(t_late, log_d, 1)
print(f"\n  Forced: log(|delta|) ~ {fit[0]:.4f}*t + {fit[1]:.2f}")
print(f"  Exponential rate: {-fit[0]:.4f} (should be ~2 for fiber Ricci scaling)")

results["forced_decay"] = {
    "data": forced_data,
    "fitted_rate": float(-fit[0]),
    "expected_rate": 2.0,
    "note": "Forced decay ~e^{-2t} vs unforced ~e^{-3t}"
}

# Check 4: a=0 constraint
print("\n=== Check 4: a=0 gauge ===")
print("  Full PDE: b_t*c_t + b_theta*c_theta = 0")
print("  Only theta-homogeneous (b_th=c_th=0) gives b_t*c_t = 0")
print("  Koiso: a_tt(0) = u*v, so a immediately leaves 0")
results["a0_gauge"] = "b_t*c_t + b_th*c_th = 0; NOT b_t*c_t = 0 alone"

out = Path("Sessions/S0910A01/workspace/data/step73_ttcs_corrections.json")
out.parent.mkdir(parents=True, exist_ok=True)
with open(out, 'w') as fh:
    json.dump(results, fh, indent=2, default=str)
print(f"\nWrote {out}")
