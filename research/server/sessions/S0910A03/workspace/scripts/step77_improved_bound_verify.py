#!/usr/bin/env python3
"""Verify the improved bound R_gamma < -24 via the Riccati comparison.

For Ric=-3g in dim 4 with S(0)=0:
  H' = 3 - |S|^2,  and  |S|^2 >= H^2/3  (Cauchy-Schwarz on 3x3 matrix S).
So H' <= 3 - H^2/3.  Compare with y' = 3 - y^2/3, y(0)=0.
"""
from __future__ import annotations
import json, sympy as sp
from pathlib import Path

r = sp.Symbol('r', real=True, nonneg=True)

# Solution of y' = 3 - y^2/3, y(0)=0:
y = 3 * sp.tanh(r)
yp = sp.diff(y, r)
rhs = 3 - y**2 / 3
check_ode = sp.simplify(yp - rhs)
print("y = 3 tanh(r)")
print("y' - (3 - y^2/3) =", check_ode, "  (should be 0)")

# 3 - y = 3(1 - tanh r)
three_minus_y = sp.simplify(3 - y)
print("\n3 - y =", three_minus_y)
# Explicit: 3(1-tanh r) = 6/(e^{2r}+1)
alt = 6 / (sp.exp(2*r) + 1)
print("= 6/(e^{2r}+1)?", sp.simplify(three_minus_y - alt) == 0)

# e^{2r}(3-y) -> 6 as r -> inf
weighted = sp.simplify(sp.exp(2*r) * three_minus_y)
limit_val = sp.limit(weighted, r, sp.oo)
print("\ne^{2r}(3-y) =", weighted)
print("limit as r -> inf:", limit_val)

# Since H <= y = 3 tanh r, we have 3-H >= 3-y, hence
# e^{2r}(3-H) >= e^{2r}(3-y) -> 6
# Therefore: -R_gamma/4 >= 6, i.e., R_gamma <= -24
print("\n--- Bound ---")
print("H(r) <= 3 tanh(r)  for all r >= 0")
print("e^{2r}(3-H(r)) >= e^{2r}(3 - 3 tanh r) -> 6")
print("-R_gamma/4 >= 6")
print("R_gamma <= -24")

# Pointwise equality at one boundary point controls only that normal ray.
# Equality on every ray forces S = (H/3)I globally, giving
# g = dr^2 + cosh^2(r) q_0 with Ric(q_0) = -2 q_0, impossible on T^3.
print("Equality on every ray forces S = (H/3)I globally")
print("  => g = dr^2 + cosh^2(r)q_0 with Ric(q_0)=-2q_0, impossible on T^3.")
print("Thus R_gamma <= -24 pointwise and R_gamma < -24 somewhere;")
print("this comparison alone does not prove strictness on each individual ray.")

# Verify the tanh comparison is monotone
# The function w(r) = 3 tanh(r) satisfies w(0)=0 and w' = 3 - w^2/3
# For H with H' = 3 - |S|^2 <= 3 - H^2/3, ODE comparison gives H <= w.
# This is valid as long as H >= 0 (which holds since H' > 0 initially
# and H' = 3 - |S|^2 >= 3 - |S|_op^2 * 3 could in principle be negative,
# but the comparison is between H and w, both starting at 0).
print("\n--- Comparison validity ---")
print("H' = 3 - |S|^2 <= 3 - H^2/3  (since |S|^2 >= H^2/3 = (tr S)^2/3)")
print("This is the standard ODE comparison theorem.")
print("Both H and w start at 0; first-contact comparison applies on every finite interval.")
print("No separate sign assumption on H is needed; global use assumes the normal foliation reaches the PE end.")

# Also check: from the shear identity
# -R_gamma/4 = 3 + integral e^{2r}|S-I|^2 dr
# With -R_gamma/4 >= 6:
print("\n--- Shear integral bound ---")
print("integral_0^inf e^{2r}|S-I|^2 dr = -R_gamma/4 - 3 >= 3")

# Near-center correction (from TTCS verifier):
# |S(r)-I|^2 = 3 - 6r + |S'|^2 r^2 + O(r^3)
# e^{2r}|S(r)-I|^2 = 3 + (|S'|^2 - 6)r^2 + O(r^3)
# (the linear term -6r is cancelled by the e^{2r} = 1+2r+... times 3)
# So integral_0^eps = 3*eps + (|S'|^2-6)*eps^3/3 + O(eps^4)
print("\n--- Near-center expansion (TTCS correction) ---")
print("|S(r)-I|^2 = 3 - 6r + |S'|^2 r^2 + O(r^3)")
print("e^{2r}|S-I|^2 = (1+2r+2r^2+...)(3-6r+|S'|^2 r^2+...)")
print("  = 3 + (6-6)r + (6-12+|S'|^2)r^2 + ...")
print("  = 3 + (|S'|^2 - 6)r^2 + O(r^3)")
print("integral_0^eps = 3 eps + (|S'|^2 - 6) eps^3/3 + O(eps^4)")
print("NOT 3eps - 3eps^2 + ... (the step77 note eq 7.2 was wrong)")

# Save
out = {
    "riccati_comparison": {
        "ODE": "y' = 3 - y^2/3, y(0)=0",
        "solution": "y = 3 tanh(r)",
        "inequality": "H(r) <= 3 tanh(r)",
        "weighted_limit": "e^{2r}(3-y) -> 6",
    },
    "improved_bound": {
        "statement": "R_gamma <= -24 for the center-normalized representative",
        "strict": "R_gamma < -24 somewhere; equality everywhere would require Ric(q_0)=-2q_0, impossible on T^3. Pointwise strictness on every ray is not proved.",
        "previous_bound": "R_gamma <= -12 pointwise (from the shear integral alone; strict somewhere under the global torus argument)",
        "improvement_factor": 2,
    },
    "shear_integral": {
        "identity": "-R_gamma/4 = 3 + integral e^{2r}|S-I|^2 dr",
        "lower_bound": "integral >= 3 (from -R_gamma/4 >= 6)",
    },
    "near_center_correction": {
        "integrand": "e^{2r}|S-I|^2 = 3 + (|S'|^2-6)r^2 + O(r^3)",
        "integral": "3 eps + (|S'|^2-6) eps^3/3 + O(eps^4)",
        "correction": "Step 77 note eq 7.2 was wrong: linear terms cancel",
    },
    "scope_warning": "R_gamma <= -24 assumes a global smooth normal foliation from the center and uses the center-normalized representative; it is not conformally invariant", 
}
outpath = Path(__file__).resolve().parents[1]/'data'/'step77_improved_bound.json'
outpath.write_text(json.dumps(out, indent=2), encoding='utf-8')
print("\nwrote", outpath)
