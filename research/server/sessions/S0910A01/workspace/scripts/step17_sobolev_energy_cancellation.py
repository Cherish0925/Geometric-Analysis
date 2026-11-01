#!/usr/bin/env python3
"""
Step 17/18 corrected scale check for the 4D Sobolev-energy cancellation.

This script verifies only the collapse-compatible scaling

    A_U * ||Rm||_{L^2(U)} = O(sqrt(K0) r^2)

for a four-dimensional support U with average_U |Rm|^2 <= K0.  It does NOT
prove the full-support cutoff-flow continuation theorem, an unweighted
transition curvature bound, or terminal Q(t)/A -> 0.  Those require the coupled
weighted curvature/defect estimates recorded in the Step 18 note.
"""
import math
from scipy.integrate import quad


def V_neg1(r, n=4):
    integrand = lambda t: math.sinh(t)**(n-1) if t > 0 else t**(n-1)
    val, _ = quad(integrand, 0, r)
    return val


def BG(s, r_star, n=4):
    return V_neg1(s * r_star, n) / V_neg1(r_star, n)


print("=" * 70)
print("4D SOBOLEV-ENERGY CANCELLATION SCALE CHECK (CORRECTED)")
print("=" * 70)

K0 = 15100.0
eps_Li = 1e-3
BG5_approx = 625.0
r_star = (eps_Li / (BG5_approx * K0))**0.25
omega_4 = math.pi**2 / 2

print(f"Li scale used for illustration: r_* = {r_star:.6f}")
print("This scale comes from eps_Li >= BG(5) K0 r_*^4.")

# Euclidean-volume illustration only; collapse-cancellation is checked below by
# varying V directly.
Vol_eucl = omega_4 * (5*r_star)**4
Rm_L2_eucl = math.sqrt(K0 * Vol_eucl)
print(f"Euclidean reference volume of B_{{5r_*}}: {Vol_eucl:.3e}")
print(f"Euclidean-reference ||Rm||_2 <= {Rm_L2_eucl:.6f}")

print("\nCollapse cancellation with arbitrary support volumes:")
C_rel = 1.0
products = []
for V in [10.0**(-k) for k in range(0, 25, 4)]:
    # Relative Sobolev coefficient in dimension 4:
    # ||u||_4^2 <= A_U int |grad u|^2, with A_U <= C r^2 / sqrt(V).
    A_U = C_rel * r_star**2 / math.sqrt(V)
    Rm_L2 = math.sqrt(K0 * V)
    product = A_U * Rm_L2
    products.append(product)
    print(f"  V={V:>9.1e}: A_U={A_U:.3e}, ||Rm||_2={Rm_L2:.3e}, product={product:.6e}")

spread = max(products) / min(products)
print(f"Product spread over collapsed volumes: {spread:.6f}")
assert abs(spread - 1.0) < 1e-10
expected = math.sqrt(K0) * r_star**2
print(f"Expected sqrt(K0) r_*^2 = {expected:.6e}")

print("\nInterpretation:")
print("  * The product can absorb a reaction term such as")
print("      int a |Rm| |E|^2 = int |Rm| |chi E|^2")
print("    after testing through chi E, provided the fixed scale is small enough.")
print("  * This is a scaling input for the coupled energy system, not a proof of")
print("    weighted curvature control, metric comparability, or unweighted Q(t)/A -> 0.")
print("PASS")
