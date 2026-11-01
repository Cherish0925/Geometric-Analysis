#!/usr/bin/env python3
"""
Step 5: Verify positive-branch geometric constants for the all-dimensional
Yau Problem 26 program.

Checks:
1. Myers diameter bound D(n,delta) = pi*sqrt(n-1)/sqrt(1-delta)
2. Bishop volume bound V_n(delta) = Vol(S^n(R)) with R=sqrt((n-1)/(1-delta))
3. Optimal beta(delta) from TTCS verifier for 4D CGB accounting
4. The noncollapse threshold: bounded Rm + tight pinching => vol > 0

Not a proof of Yau26.
"""
import numpy as np
from scipy.special import gamma as Gamma

def vol_sphere(n, R):
    """Volume of S^n(R) = omega_n * R^n."""
    omega_n = 2 * np.pi**((n+1)/2) / Gamma((n+1)/2)
    return omega_n * R**n

def myers_diam(n, delta):
    """Myers diameter bound for Ric >= (1-delta)g on n-manifold."""
    return np.pi * np.sqrt(n - 1) / np.sqrt(1 - delta)

def bishop_vol(n, delta):
    """Bishop-Gromov volume upper bound."""
    R = np.sqrt((n - 1) / (1 - delta))
    return vol_sphere(n, R)

def beta_optimal(delta):
    """Optimal 4D pointwise CGB lower bound (TTCS-verified)."""
    if delta <= 1/3:
        return 2/3 * (1 - delta)**2
    elif delta < 1/2:
        return 2/3 * (1 + delta) * (1 - 2*delta)
    else:
        return 0.0

def alpha_upper(delta):
    """4D pointwise CGB upper bound."""
    return 2/3 * (1 + delta)**2

def noncollapse_vol_4d(K, delta):
    """Lower volume bound in 4D under |Rm| <= K and tight pinching."""
    b = beta_optimal(delta)
    if b <= 0:
        return 0.0
    a = alpha_upper(delta)
    return 8 * np.pi**2 / (K**2 + a)

print("=" * 72)
print("Step 5: Positive-branch constants for Yau Problem 26")
print("=" * 72)

print("\n--- Myers diameter bound D(n, delta) ---")
for n in [2, 3, 4, 5, 10, 20]:
    for delta in [0.0, 0.01, 0.1, 0.3]:
        D = myers_diam(n, delta)
        print(f"  n={n:2d}, delta={delta:.2f}: D = {D:.4f}")

print("\n--- Bishop volume upper bound V_n(delta) ---")
for n in [2, 3, 4, 5]:
    for delta in [0.0, 0.01, 0.1]:
        V = bishop_vol(n, delta)
        print(f"  n={n}, delta={delta:.2f}: Vol <= {V:.4f}")

print("\n--- Optimal beta(delta) for 4D CGB ---")
for delta in np.arange(0, 0.51, 0.05):
    b = beta_optimal(delta)
    a = alpha_upper(delta)
    print(f"  delta={delta:.2f}: beta={b:.6f}, alpha={a:.6f}, "
          f"beta>0={b>0}")

print("\n--- 4D noncollapse under |Rm| <= K ---")
for K in [1, 10, 100, 1000]:
    for delta in [0.01, 0.1, 0.3]:
        v = noncollapse_vol_4d(K, delta)
        print(f"  K={K:4d}, delta={delta:.2f}: Vol >= {v:.6e}")

print("\n--- Topological filter: 2*chi > 3*|tau| constraint ---")
print("  Simply connected 4-manifolds #k CP^2 # l CPbar^2:")
print("  Constraint: 2(2+k+l) > 3|k-l|")
for k in range(8):
    for l in range(k + 1):
        chi = 2 + k + l
        tau = k - l
        ht = 2 * chi - 3 * abs(tau)
        # Reversed orientation
        ht2 = 2 * chi + 3 * abs(tau)  # Always >0 for chi>0
        status = "HT_OK" if ht > 0 else "HT_FAIL"
        ein = "?"
        if (k, l) == (0, 0):
            ein = "Einstein (S^4)"
        elif (k, l) == (1, 0):
            ein = "Einstein (CP^2)"
        elif (k, l) == (1, 1):
            ein = "Einstein (Page)"
        elif (k, l) == (2, 1):
            ein = "Einstein? (CLW-type)"
        elif (k, l) == (2, 0):
            ein = "Unknown"
        elif (k, l) == (3, 0):
            ein = "Unknown"
        print(f"  ({k},{l}): chi={chi}, tau={tau}, "
              f"2chi-3|tau|={ht}, {status}, {ein}")

print("\n--- Positive branch asymmetry summary ---")
print("  Positive: diam bounded, vol bounded, b1=0, pi1 finite, PSC")
print("  Negative: NO diam bound, NO vol bound, b1 unrestricted")
print("  Gap for P_n+: collapse only")
print("  Gap for P_n-: diameter + collapse")
