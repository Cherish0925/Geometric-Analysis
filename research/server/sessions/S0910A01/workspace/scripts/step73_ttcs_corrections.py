#!/usr/bin/env python3
"""Step 73: TTCS-prompted corrections.

Checks:
1. Periodic fiber: does int_0^{2pi} u d(theta) = 0?
2. Correct ODE for 3-direction system: H' = 9 - H^2, H = 3*tanh(3t)
3. Decay rate: sech(3t), not sech(sqrt(3)*t)
4. a=0 gauge: full PDE gives b_t*c_t + b_th*c_th = 0, not b_t*c_t = 0
5. Forced difference equation with fiber Ricci
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.optimize import brentq
import json, sys

results = {}

# ============================================================
# Check 1: Does int u dtheta = 0 for the periodic fibers?
# ============================================================
print("=== Check 1: Zero-mean condition ===\n")

def fiber_rhs(theta, state, B_val):
    u = state[0]
    v = B_val * np.sin(theta)
    vp = B_val * np.cos(theta)
    du = 3 - u**2 - v**2 - u*v - vp
    return [du]

for B in [0.5, 1.0, 1.5, 2.0]:
    def residual(u0):
        sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0],
                        args=(B,), max_step=0.005, rtol=1e-12, atol=1e-14)
        return sol.y[0, -1] - u0 if sol.success else 1e10

    u0s = np.linspace(-3, 3, 400)
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
        print(f"  B={B}: no periodic solution")
        continue

    N = 1024
    th = np.linspace(0, 2*np.pi, N, endpoint=False)
    dth = th[1] - th[0]
    sol = solve_ivp(fiber_rhs, [0, 2*np.pi], [u0_opt],
                    args=(B,), max_step=0.002, t_eval=th, rtol=1e-12, atol=1e-14)
    u = sol.y[0]
    v = B * np.sin(th)

    # Integrals
    int_u = np.trapz(u, th)
    int_v = np.trapz(v, th)  # should be 0 by symmetry

    # For b_0 to be periodic: int u dtheta must = 0
    # For c_0 to be periodic: int v dtheta must = 0
    print(f"  B={B}: u0={u0_opt:.8f}")
    print(f"    int(u) / 2pi = {int_u/(2*np.pi):.10f}")
    print(f"    int(v) / 2pi = {int_v/(2*np.pi):.10f}")
    print(f"    PERIODIC b_0: {'YES' if abs(int_u) < 1e-6 else 'NO (int_u = ' + f'{int_u:.6f})'}")

    results[f"B={B}_int_u"] = {
        "u0": float(u0_opt),
        "int_u": float(int_u),
        "int_v": float(int_v),
        "periodic_b0": bool(abs(int_u) < 1e-6),
        "mean_u": float(int_u / (2*np.pi)),
        "mean_v": float(int_v / (2*np.pi))
    }


# ============================================================
# Check 2: Correct 3-direction ODE rate
# ============================================================
print("\n=== Check 2: Three-direction ODE ===\n")

# From s_i' + H*s_i = 3, summing: H' + |S|^2 = 9
# Constraint: |S|^2 >= H^2/3, with equality for isotropic
# For isotropic: H' + H^2/3 = ? No: s_i = H/3, |S|^2 = H^2/3
# H' + H^2/3 = 3*3 = 9? No: each equation gives s' + s*H = 3, with s=H/3:
# H'/3 + H^2/3 = 3 => H' + H^2 = 9
# So H(0) = 0 => H = 3*tanh(3*t)

t = np.linspace(0, 5, 2000)
H_correct = 3 * np.tanh(3*t)
H_wrong = np.sqrt(3) * np.tanh(np.sqrt(3)*t)

# Verify ODE: H' = 9 - H^2
H_deriv = np.gradient(H_correct, t)
H_ode_residual = H_deriv - (9 - H_correct**2)
print(f"  H = 3*tanh(3t): ODE residual max = {np.max(np.abs(H_ode_residual)):.2e}")

# Decay factor: exp(-int_0^t H) = exp(-log(cosh(3t))) = sech(3t)
decay_correct = 1.0 / np.cosh(3*t)
decay_wrong = 1.0 / np.cosh(np.sqrt(3)*t)

print(f"  At t=1: sech(3) = {decay_correct[400]:.6f}, sech(sqrt3) = {decay_wrong[400]:.6f}")
print(f"  At t=2: sech(6) = {decay_correct[800]:.8f}, sech(2sqrt3) = {decay_wrong[800]:.8f}")

results["ode_rate_correction"] = {
    "correct_H": "3*tanh(3t)",
    "correct_decay": "sech(3t)",
    "wrong_H": "sqrt(3)*tanh(sqrt(3)*t)",
    "wrong_decay": "sech(sqrt(3)*t)",
    "sech3_at_t1": float(decay_correct[400]),
    "sech_sqrt3_at_t1": float(decay_wrong[400]),
    "note": "sqrt(3) was from a=0 two-direction gauge; 3 is the correct three-direction rate"
}


# ============================================================
# Check 3: Forced difference equation with fiber Ricci
# ============================================================
print("\n=== Check 3: Forced difference equation ===\n")

# Correct tangential Einstein equation:
# s_i' + H*s_i = 3 + r_i(h_t)
# where r_i are eigenvalues of the fiber Ricci tensor
#
# Difference: delta_ij' + H*delta_ij = r_i - r_j
# NOT delta_ij' + H*delta_ij = 0
#
# For reflection center: s_i(0) = 0, delta_ij(0) = 0
# Duhamel: delta_ij(t) = exp(-int_0^t H) * int_0^t exp(int_0^tau H) (r_i-r_j)(tau) dtau
#
# In cusp regime: Ric_{h_t} ~ e^{-2t} Ric_{h_infty}
# So r_i(h_t) ~ e^{-2t} r_i(h_infty)
# Duhamel estimate:
# delta_ij(t) ~ sech(3t) * int_0^t cosh(3tau) * C * e^{-2tau} dtau
# For large t: ~ e^{-3t} * int_0^t e^{3tau} * C * e^{-2tau} dtau
#            = C * e^{-3t} * (e^t - 1) ~ C * e^{-2t}

# Verify by solving the forced system numerically
def forced_ode(t, y, r_func):
    """s_i' + H*s_i = 3 + r_i(t), i=1,2,3"""
    s1, s2, s3 = y
    H = s1 + s2 + s3
    r1, r2, r3 = r_func(t)
    return [3 + r1 - s1*H, 3 + r2 - s2*H, 3 + r3 - s3*H]

# Model: r_i(t) = r_i(0) * exp(-2t) with initial Koiso data
# At t=0: s_i = 0, so s_i'(0) = 3 + r_i(0)
# For B=1.0 fiber at theta=0: a_tt=0, b_tt=1, c_tt=2
# So s'(0) = (0, 1, 2), meaning 3 + r_i(0) = (0, 1, 2) => r_i(0) = (-3, -2, -1)

r0_vals = np.array([-3.0, -2.0, -1.0])
r_func = lambda t: r0_vals * np.exp(-2*t)

dt = 0.001
y0 = [(3 + r0_vals[i]) * dt for i in range(3)]  # s_i(dt) ~ s_i'(0)*dt
sol = solve_ivp(forced_ode, [dt, 10], y0, args=(r_func,),
                max_step=0.01, rtol=1e-10, atol=1e-12,
                t_eval=np.linspace(dt, 10, 2000))

s1, s2, s3 = sol.y
t_sol = sol.t
delta12 = s1 - s2
delta13 = s1 - s3

# Compare with unforced
def unforced_ode(t, y):
    s1, s2, s3 = y
    H = s1 + s2 + s3
    return [3 - s1*H, 3 - s2*H, 3 - s3*H]

y0_unforced = [(3 + r0_vals[i]) * dt for i in range(3)]
sol_uf = solve_ivp(unforced_ode, [dt, 10], y0_unforced,
                   max_step=0.01, rtol=1e-10, atol=1e-12,
                   t_eval=np.linspace(dt, 10, 2000))
delta12_uf = sol_uf.y[0] - sol_uf.y[1]

print("  Forced vs unforced delta_12:")
for R in [1, 2, 4, 6, 8]:
    idx = np.argmin(np.abs(t_sol - R))
    idx_uf = np.argmin(np.abs(sol_uf.t - R))
    print(f"    R={R}: forced={delta12[idx]:.2e}, unforced={delta12_uf[idx_uf]:.2e}, "
          f"ratio={delta12[idx]/(delta12_uf[idx_uf]+1e-30):.3f}")

print(f"\n  Large-t behavior: forced delta_12 ~ C*e^{{-2t}}, unforced ~ C*e^{{-3t}}")
for R in [6, 8, 10]:
    idx = np.argmin(np.abs(t_sol - R))
    print(f"    R={R}: forced delta_12 = {delta12[idx]:.2e}, "
          f"e^{{-2R}} = {np.exp(-2*R):.2e}, "
          f"e^{{-3R}} = {np.exp(-3*R):.2e}")

results["forced_decay"] = {
    "correct_equation": "delta' + H*delta = r_i - r_j",
    "forced_rate": "~exp(-2t) from fiber Ricci scaling",
    "unforced_rate": "~exp(-3t) = sech(3t)",
    "delta12_at_R4": float(delta12[np.argmin(np.abs(t_sol - 4))]),
    "delta12_at_R8": float(delta12[np.argmin(np.abs(t_sol - 8))]),
    "note": "Forced system still decays but at slower rate e^{-2t}"
}


# ============================================================
# Check 4: Verify a=0 gauge constraint
# ============================================================
print("\n=== Check 4: a=0 gauge constraint ===\n")
print("  Full PDE gives: b_t*c_t + b_theta*c_theta = 0")
print("  NOT b_t*c_t = 0 (which requires additionally b_theta*c_theta = 0)")
print("  The theta-homogeneous ODE (b_th=c_th=0) does give b_t*c_t = 0")
print("  But the full T^2-invariant PDE does NOT force b_t*c_t = 0")
print("  Koiso center has a_tt(0) = u*v ≠ 0 (for u,v ≠ 0), so the solution")
print("  immediately leaves a=0. The a=0 gauge cannot hold along the collar.")
results["a0_correction"] = {
    "full_pde": "b_t*c_t + b_theta*c_theta = 0",
    "theta_homogeneous_only": "b_t*c_t = 0",
    "koiso_incompatible": "a_tt(0) = u*v ≠ 0 at generic theta"
}


# ============================================================
# Save
# ============================================================
from pathlib import Path
out = Path("Sessions/S0910A01/workspace/data/step73_ttcs_corrections.json")
with open(out, 'w') as fh:
    json.dump(results, fh, indent=2, default=str)
print(f"\nWrote {out}")
