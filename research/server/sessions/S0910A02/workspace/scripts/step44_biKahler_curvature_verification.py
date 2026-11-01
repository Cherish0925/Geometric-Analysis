"""
Step 44: Symbolic verification of S^2 x S^2 bi-Kahler curvature structure

Verify that the product Einstein metric on S^2(1) x S^2(1) has
R+ and R- with identical eigenvalue structure (Lambda, 0, 0),
hence det R+ = det R- = 0 at every point.
"""

import sympy as sp
from sympy import Matrix, Rational, sqrt, zeros, eye

print("="*60)
print("CURVATURE OPERATOR ON S^2(1) x S^2(1)")
print("="*60)

# Riemann tensor components in orthonormal frame {e1,e2,e3,e4}
# e1,e2 tangent to first S^2; e3,e4 tangent to second S^2
# R_{ijkl} with pair (ij) and pair (kl) as antisymmetric pairs

# Nonzero: R_1212 = R_3434 = K = 1 (Gaussian curvature of unit S^2)
K1, K2 = 1, 1  # Both S^2 factors have K = 1

# For Einstein 4-manifold with Ric = Lambda*g:
# Ric_{11} = R_{1212} + R_{1313} + R_{1414} = K1 + 0 + 0 = 1
# So Lambda = 1 consistent
Lambda = 1

# 6-dimensional basis of 2-forms (ordered as pairs):
# (12), (13), (14), (23), (24), (34)

# Curvature operator R: Sym map on Lambda^2
# (R*alpha)_{kl} = (1/2) R_{klij} alpha^{ij}
# In the basis above, R is a 6x6 symmetric matrix

# Matrix elements: R_{pair_a, pair_b} = R_{i_a j_a i_b j_b}
# where pair_a = (i_a, j_a), pair_b = (i_b, j_b)

pairs = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

# Define Riemann tensor as a function
def Rm(i,j,k,l):
    """Riemann tensor R_{ijkl} for S^2(1) x S^2(1) product metric.
    Nonzero only for R_1212 = R_3434 = 1 and permutations."""
    # Antisymmetry: R_{ijkl} = -R_{jikl} = -R_{ijlk} = R_{klij}
    # Pair symmetry: R_{ijkl} = R_{klij}
    # First Bianchi: R_{ijkl} + R_{iklj} + R_{iljk} = 0
    
    # Only nonzero independent: R_1212 = K1, R_3434 = K2
    # All cross-components = 0 for product metric
    
    # Sort into canonical form using symmetries
    if i == j or k == l:
        return 0
    
    # Make first pair have i < j
    sign = 1
    if i > j:
        i, j = j, i
        sign *= -1
    if k > l:
        k, l = l, k
        sign *= -1
    
    if (i,j,k,l) == (1,2,1,2):
        return sign * K1
    elif (i,j,k,l) == (3,4,3,4):
        return sign * K2
    elif (i,j,k,l) == (1,2,3,4):
        return 0
    elif (i,j,k,l) == (3,4,1,2):
        return 0
    else:
        return 0

# Build 6x6 curvature operator matrix
R_op = zeros(6)
for a, (i1,j1) in enumerate(pairs):
    for b, (i2,j2) in enumerate(pairs):
        R_op[a,b] = Rm(i1,j1,i2,j2)

print("\nCurvature operator in basis (12,13,14,23,24,34):")
sp.pprint(R_op)

# Self-dual basis (with respect to orientation e1,e2,e3,e4):
# omega1+ = (e12 + e34)/sqrt(2)  -> coefficients in our basis
# omega2+ = (e13 - e24)/sqrt(2)  -> (13) - (24) with signs
# omega3+ = (e14 + e23)/sqrt(2)

# Anti-self-dual basis:
# omega1- = (e12 - e34)/sqrt(2)
# omega2- = (e13 + e24)/sqrt(2)
# omega3- = (e14 - e23)/sqrt(2)

s2 = sqrt(2)

# Change of basis matrix P: columns are the self-dual/anti-self-dual basis
# in terms of (12,13,14,23,24,34)
#                    omega1+ omega2+ omega3+ omega1- omega2- omega3-
P = Matrix([
    [1/s2,  0,     0,      1/s2,   0,      0     ],  # e12
    [0,     1/s2,  0,      0,      1/s2,   0     ],  # e13
    [0,     0,     1/s2,   0,      0,      1/s2  ],  # e14
    [0,     0,     1/s2,   0,      0,      -1/s2 ],  # e23
    [0,     -1/s2, 0,      0,      1/s2,   0     ],  # e24
    [1/s2,  0,     0,      -1/s2,  0,      0     ],  # e34
])

# Transform: R_sd = P^T * R_op * P
R_sd = P.T * R_op * P
R_sd = sp.simplify(R_sd)

print("\nCurvature operator in self-dual/anti-self-dual basis:")
print("(omega1+, omega2+, omega3+, omega1-, omega2-, omega3-)")
sp.pprint(R_sd)

# Extract R+ and R- blocks
R_plus = R_sd[:3, :3]
R_minus = R_sd[3:, 3:]
R_cross = R_sd[:3, 3:]

print("\nR+ (self-dual block):")
sp.pprint(R_plus)

print("\nR- (anti-self-dual block):")
sp.pprint(R_minus)

print("\nCross term (should be 0 for Einstein):")
sp.pprint(R_cross)

# Eigenvalues
eig_plus = R_plus.eigenvals()
eig_minus = R_minus.eigenvals()

print(f"\nR+ eigenvalues: {eig_plus}")
print(f"R- eigenvalues: {eig_minus}")

det_plus = R_plus.det()
det_minus = R_minus.det()

print(f"\ndet R+ = {det_plus}")
print(f"det R- = {det_minus}")

# W+ and W- (subtract Lambda/3 * I)
W_plus = R_plus - Rational(Lambda, 3) * eye(3)
W_minus = R_minus - Rational(Lambda, 3) * eye(3)

print(f"\nW+ = R+ - (Lambda/3)I:")
sp.pprint(W_plus)

print(f"\nW- = R- - (Lambda/3)I:")
sp.pprint(W_minus)

eig_Wplus = sorted(W_plus.eigenvals().keys(), reverse=True)
eig_Wminus = sorted(W_minus.eigenvals().keys(), reverse=True)
print(f"\nW+ eigenvalues: {eig_Wplus}")
print(f"W- eigenvalues: {eig_Wminus}")

# Key verification
print("\n" + "="*60)
print("VERIFICATION")
print("="*60)
print(f"R+ = R- (identical blocks): {R_plus == R_minus}")
print(f"det R+ = 0: {det_plus == 0}")
print(f"det R- = 0: {det_minus == 0}")
print(f"Cross term vanishes: {R_cross == zeros(3)}")
print(f"W+ eigenvalues = (2/3, -1/3, -1/3): {eig_Wplus}")
print(f"W- eigenvalues = (2/3, -1/3, -1/3): {eig_Wminus}")
print(f"W+ traceless: {sp.simplify(W_plus.trace()) == 0}")
print(f"W- traceless: {sp.simplify(W_minus.trace()) == 0}")

print("\nBI-KAHLER CONFIRMATION:")
print("S^2 x S^2 product metric has R+ = R- = diag(1, 0, 0)")
print("=> det R+ = det R- = 0 at EVERY point")
print("=> Both orientation-compatible and reversed EH bubbles")
print("   satisfy the first-order Ozuch obstruction trivially")
