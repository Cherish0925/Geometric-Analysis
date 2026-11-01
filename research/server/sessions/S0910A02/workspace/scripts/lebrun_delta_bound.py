# ERRATUM (Step 3): this script contains the Step 2 factor error and an obsolete scalar-only interpretation. Do not use it as a source for LeBrun constants or delta bounds. Use Sessions/S0910A02/workspace/scripts/step3_corrected_lebrun_bounds.py and Sessions/S0910A02/workspace/notes/step3_corrections_lebrun_and_collapse.md instead.

#!/usr/bin/env python3
"""
Compute the CGB + SW lower bound on delta_- for LeBrun manifolds
M = X # k CPbar^2, where X is a minimal surface of general type with
c1^2(X) = A and Euler number chi(X).

The Bogomolov-Miyaoka-Yau inequality gives A <= 3*chi(X).

For the manifold M:
  chi(M) = chi(X) + k
  tau(M) = tau(X) - k = (A - 2*chi(X))/3 - k
  2*chi + 3*tau = A - k    (denote C)
  2*chi - 3*tau = 4*chi(X) - A + 5*k  (denote B)

Strict HT requires C > 0 and B > 0, i.e., k < A and k > (A - 4*chi(X))/5.

LeBrun nonexistence (lambda < 0):
  From SW: integral s^2 >= 32*pi^2*(A-k)
  From CGB (Einstein, E=0):
    8*pi^2*(A-k) = 4*int|W+|^2 + 16*lambda^2*Vol/3
    so int|W+|^2 = 2*pi^2*(A-k) - 4*lambda^2*Vol/3
  From SW: lambda^2*Vol >= 2*pi^2*(A-k)
    so int|W+|^2 <= 2*pi^2*(A-k) - 8*pi^2*(A-k)/3 = -2*pi^2*(A-k)/3 < 0
  CONTRADICTION: no negative Einstein on M when A > k.

For INPUT metric with delta_-(g) = delta:
  s = -4 + e_s, |e_s| <= 4*delta
  |E|^2 <= 4*delta^2
  
  From CGB (2chi+3tau):
    4*pi^2*(A-k) = 2*int|W+|^2 + int(s^2/24) - int(|E|^2/2)
  
  From SW (applied to input metric!):
    int s^2 >= 32*pi^2*(A-k)
  
  Non-negativity of |W+|^2:
    int(|E|^2/2) >= int(s^2/24) - 4*pi^2*(A-k)

We want to find if this forces delta > 0 for fixed (A, k, chi(X)).

Strategy: parameterize Vol = V, and use:
  (a) CGB (2chi-3tau): V <= 6*pi^2*B / (1 - 3*delta^2)  [for small delta]
  (b) SW lower bound: V >= 2*pi^2*(A-k) / (1+delta)^2
  (c) |E|^2 bound: int|E|^2 <= 4*delta^2*V
  (d) W+ non-negativity: int|E|^2/2 >= int s^2/24 - 4*pi^2*(A-k)

From (d): 2*delta^2*V >= (2/3)*V*(1 - O(delta))^2 - 4*pi^2*(A-k)
But this needs Vol to be large enough relative to A-k.

Let me compute numerically for specific examples.
"""

import numpy as np

def compute_bounds(A, chi_X, k_values=None):
    """Compute bounds for LeBrun manifolds."""
    if k_values is None:
        k_values = range(1, A)
    
    tau_X = (A - 2*chi_X) / 3
    
    print(f"\nX: c1^2 = {A}, chi = {chi_X}, tau = {tau_X:.2f}")
    print(f"BMY check: A <= 3*chi? {A} <= {3*chi_X}: {'YES' if A <= 3*chi_X else 'NO'}")
    print()
    print(f"{'k':>4} {'C=A-k':>6} {'B':>8} {'HT_ok':>6} {'SW_Vlb':>10} {'CGB_Vub':>10} {'S01_delta':>12}")
    print("-" * 70)
    
    for k in k_values:
        C = A - k  # 2chi + 3tau
        B = 4*chi_X - A + 5*k  # 2chi - 3tau
        ht_ok = (C > 0) and (B > 0)
        
        if not ht_ok or C <= 0:
            continue
        
        # SW volume lower bound (delta -> 0 limit)
        sw_vlb = 2 * np.pi**2 * C
        
        # CGB volume upper bound (delta -> 0 limit)
        cgb_vub = 6 * np.pi**2 * B
        
        # S0910A01's formula: delta^2 >= (k - 2A/3) / (3*(A-k))
        if k > 2*A/3:
            s01_delta_sq = (k - 2*A/3) / (3*(A - k))
            s01_delta = np.sqrt(s01_delta_sq)
        else:
            s01_delta = 0.0
        
        print(f"{k:4d} {C:6d} {B:8.1f} {'Y' if ht_ok else 'N':>6} {sw_vlb:10.1f} {cgb_vub:10.1f} {s01_delta:12.6f}")

# Example 1: Horikawa surface X with c1^2 = 2*chi - 6 (on the Noether line)
# For chi = 4: A = 2, not enough blow-ups
# For chi = 10: A = 14
print("=" * 70)
print("Example: Surfaces near Noether line c1^2 = 2*chi - 6")
for chi_X in [10, 20, 50, 100, 300, 1000]:
    A = 2 * chi_X - 6
    compute_bounds(A, chi_X, range(1, A))

# Example 2: Surfaces at BMY bound c1^2 = 3*chi
print("\n" + "=" * 70)
print("Example: Surfaces at BMY bound c1^2 = 3*chi")
for chi_X in [4, 10, 50, 100, 300, 1000]:
    A = 3 * chi_X
    compute_bounds(A, chi_X, range(1, A))

# Key analysis: for k ≈ 2A/3, how does delta bound behave?
print("\n" + "=" * 70)
print("Key: S0910A01 delta bound at k = ceil(2A/3) for growing A")
print(f"{'A':>6} {'chi_X':>6} {'k':>6} {'delta_lb':>12} {'1/sqrt(A)':>12}")
print("-" * 55)
for chi_X in [10, 50, 100, 500, 1000, 5000, 10000]:
    A = 2 * chi_X - 6  # Noether line
    k = int(np.ceil(2*A/3))
    if k >= A:
        k = A - 1
    C = A - k
    if C <= 0:
        continue
    if k > 2*A/3:
        delta_sq = (k - 2*A/3) / (3*C)
        delta = np.sqrt(delta_sq)
    else:
        delta = 0.0
    print(f"{A:6d} {chi_X:6d} {k:6d} {delta:12.6f} {1/np.sqrt(A):12.6f}")

print("\nConclusion: The S0910A01 bound delta >= C/sqrt(A) for k near 2A/3.")
print("For fixed M, delta is bounded away from 0.")
print("For varying M_j with A_j -> infty, the bound -> 0.")
print("This is a NECESSARY condition from CGB+SW, not a constructive bound.")
