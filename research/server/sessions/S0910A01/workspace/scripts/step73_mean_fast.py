#!/usr/bin/env python3
"""Step 73: fast mean(u) tracking using continuation."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import json
from pathlib import Path

def shoot(u0, B):
    sol = solve_ivp(lambda th, y: [3 - y[0]**2 - (B*np.sin(th))**2 - y[0]*B*np.sin(th) - B*np.cos(th), y[0]],
                    [0, 2*np.pi], [u0, 0.0], max_step=0.02, rtol=1e-10, atol=1e-12)
    return sol.y[0, -1] - u0, sol.y[1, -1] / (2*np.pi)

def find_u0(B, u0_guess):
    """Find periodic u0 near guess"""
    def per(u0): return shoot(u0, B)[0]
    # Try small bracket
    for dw in [0.1, 0.3, 0.5, 1.0, 2.0]:
        lo, hi = u0_guess - dw, u0_guess + dw
        try:
            if per(lo)*per(hi) < 0:
                return brentq(per, lo, hi, xtol=1e-10)
        except: pass
    return None

print("B       u0          mean(u)")
print("-" * 40)

u0_prev = 1.73  # start near sqrt(3)
track = []
for B in np.arange(0.5, 10.1, 0.25):
    u0 = find_u0(B, u0_prev)
    if u0 is None:
        print(f"{B:6.2f}  FAILED")
        continue
    _, mu = shoot(u0, B)
    print(f"{B:6.2f}  {u0:10.6f}  {mu:10.6f}")
    track.append({"B": float(B), "u0": float(u0), "mean": float(mu)})
    u0_prev = u0
    if mu < -1:  # diverging negative, stop
        break

# Check for sign change
means = [t["mean"] for t in track]
for i in range(len(means)-1):
    if means[i]*means[i+1] < 0:
        B_lo, B_hi = track[i]["B"], track[i+1]["B"]
        print(f"\nSign change: B in [{B_lo}, {B_hi}]")
        # Bisect
        def mean_at_B(B):
            u0 = find_u0(B, track[i]["u0"])
            return shoot(u0, B)[1] if u0 else 1e10
        B_star = brentq(mean_at_B, B_lo, B_hi, xtol=1e-6)
        u0_star = find_u0(B_star, track[i]["u0"])
        _, mu_star = shoot(u0_star, B_star)
        print(f"B* = {B_star:.8f}, u0* = {u0_star:.8f}, mean = {mu_star:.2e}")
        track.append({"B_star": float(B_star), "u0_star": float(u0_star),
                       "mean_star": float(mu_star)})
        break

out = Path("Sessions/S0910A01/workspace/data/step73_mean_u_track.json")
with open(out, 'w') as fh:
    json.dump({"track": track}, fh, indent=2)
print(f"\nWrote {out}")
