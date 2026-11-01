#!/usr/bin/env python3
"""Step 73: track mean(u) vs B to find zero-mean periodic fiber.

The mean of the periodic u(theta) solving u'=3-u^2-v^2-uv-v' with v=B*sin(theta)
decreases as B increases. Find B* where mean(u)=0.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, root
import json
from pathlib import Path

def fiber_rhs(theta, state, B):
    u, I = state
    v = B * np.sin(theta)
    vp = B * np.cos(theta)
    du = 3 - u**2 - v**2 - u*v - vp
    return [du, u]

def find_periodic_u0(B):
    """Find u0 such that u(2pi;u0,B) = u0"""
    def per_res(u0):
        sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0, 0.0],
                        args=(B,), max_step=0.01, rtol=1e-11, atol=1e-13)
        return sol.y[0, -1] - u0 if sol.success else 1e10

    # Scan for sign change
    u0s = np.linspace(-4, 4, 100)
    ress = [per_res(u0) for u0 in u0s]
    for i in range(len(ress)-1):
        if ress[i]*ress[i+1] < 0:
            try:
                return brentq(per_res, u0s[i], u0s[i+1], xtol=1e-12)
            except:
                continue
    return None

def compute_mean(B, u0):
    """Compute mean of u for given (B, u0)"""
    sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0, 0.0],
                    args=(B,), max_step=0.01, rtol=1e-11, atol=1e-13)
    return sol.y[1, -1] / (2*np.pi)  # integral / period

print("=== Tracking mean(u) vs B ===\n")
print(f"  {'B':>6s} | {'u0':>10s} | {'mean(u)':>10s}")
print("  " + "-"*36)

B_vals = []
mean_vals = []
u0_vals = []

for B in np.arange(0.5, 8.1, 0.5):
    u0 = find_periodic_u0(B)
    if u0 is not None:
        mu = compute_mean(B, u0)
        B_vals.append(B)
        mean_vals.append(mu)
        u0_vals.append(u0)
        print(f"  {B:6.1f} | {u0:10.6f} | {mu:10.6f}")

# Find B* where mean crosses zero
if len(mean_vals) > 1:
    B_arr = np.array(B_vals)
    mu_arr = np.array(mean_vals)

    # Check for sign change
    sign_changes = []
    for i in range(len(mu_arr)-1):
        if mu_arr[i]*mu_arr[i+1] < 0:
            sign_changes.append(i)

    if sign_changes:
        i = sign_changes[0]
        print(f"\n  Sign change between B={B_arr[i]:.1f} (mean={mu_arr[i]:.6f}) "
              f"and B={B_arr[i+1]:.1f} (mean={mu_arr[i+1]:.6f})")

        # Bisect for precise B*
        def mean_at_B(B):
            u0 = find_periodic_u0(B)
            if u0 is None:
                return 1e10
            return compute_mean(B, u0)

        try:
            B_star = brentq(mean_at_B, B_arr[i], B_arr[i+1], xtol=1e-8)
            u0_star = find_periodic_u0(B_star)
            mu_star = compute_mean(B_star, u0_star)
            print(f"  B* = {B_star:.8f}, u0* = {u0_star:.8f}, mean = {mu_star:.2e}")

            # Verify: compute full solution
            N = 512
            th = np.linspace(0, 2*np.pi, N, endpoint=False)
            sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0_star, 0],
                            args=(B_star,), max_step=0.003, t_eval=th,
                            rtol=1e-12, atol=1e-14)
            u = sol.y[0]
            v = B_star * np.sin(th)
            vp = B_star * np.cos(th)
            up = 3 - u**2 - v**2 - u*v - vp

            # R^{(3)} check
            R3 = -2*(u**2 + v**2 + u*v + up + vp)
            print(f"  R3 range: [{np.min(R3):.6f}, {np.max(R3):.6f}]")

            # Koiso data
            a_tt = u*v
            b_tt = v**2 + vp
            c_tt = u**2 + up
            print(f"  S' at theta=0: ({a_tt[0]:.4f}, {b_tt[0]:.4f}, {c_tt[0]:.4f})")
            print(f"  S' at theta=pi/2: ({a_tt[N//4]:.4f}, {b_tt[N//4]:.4f}, {c_tt[N//4]:.4f})")
            print(f"  trace range: [{np.min(a_tt+b_tt+c_tt):.6f}, {np.max(a_tt+b_tt+c_tt):.6f}]")

            result = {
                "B_star": float(B_star),
                "u0_star": float(u0_star),
                "mean_residual": float(mu_star),
                "R3_range": [float(np.min(R3)), float(np.max(R3))],
                "R3_error": float(np.max(np.abs(R3+6))),
                "S_prime_at_0": [float(a_tt[0]), float(b_tt[0]), float(c_tt[0])],
                "trace_range": [float(np.min(a_tt+b_tt+c_tt)), float(np.max(a_tt+b_tt+c_tt))],
                "u_range": [float(np.min(u)), float(np.max(u))],
                "u_mean": float(np.mean(u))
            }
        except Exception as e:
            result = {"error": str(e)}
            print(f"  Bisection failed: {e}")
    else:
        print("\n  No sign change found — mean stays positive")
        result = {"no_sign_change": True,
                  "B_range": [float(B_arr[0]), float(B_arr[-1])],
                  "mean_range": [float(mu_arr[0]), float(mu_arr[-1])]}
else:
    result = {"insufficient_data": True}

# Also record the track
result["track"] = [{"B": float(b), "u0": float(u), "mean_u": float(m)}
                   for b, u, m in zip(B_vals, u0_vals, mean_vals)]

out = Path("Sessions/S0910A01/workspace/data/step73_mean_u_track.json")
with open(out, 'w') as fh:
    json.dump(result, fh, indent=2)
print(f"\nWrote {out}")
