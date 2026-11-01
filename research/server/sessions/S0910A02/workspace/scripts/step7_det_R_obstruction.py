#!/usr/bin/env python3
"""Step 7: Curvature operator det R computation for obstruction-amplitude principle.

Verify det R at orbifold singularities for the positive branch of Yau Problem 26.

The Biquard-Ozuch obstruction: for Einstein sequences converging to Einstein
orbifold, desingularization requires det R = 0 at each singular point.
Combined with the session's obstruction-amplitude principle (nonzero det R
forces order-1 C^0 Ricci excess), this determines which orbifold limits
are compatible with tight C^0 Ricci pinching.
"""

import numpy as np
from fractions import Fraction
import json

results = {}

print("=" * 70)
print("CURVATURE OPERATOR det R ON Lambda^2 FOR 4D EINSTEIN METRICS")
print("=" * 70)

# Lambda^2 basis: {e12, e34, e13, e14, e23, e24}
# Hodge star: *e12 = e34, *e13 = -e24, *e14 = e23
# Self-dual basis (eigenvalue +1 of *):
#   phi1 = (e12 + e34)/sqrt(2)
#   phi2 = (e13 - e24)/sqrt(2)
#   phi3 = (e14 + e23)/sqrt(2)

# Curvature operator R: Lambda^2 -> Lambda^2
# R_{(ij),(kl)} = R_{ijkl} as a matrix on Lambda^2

# Change-of-basis matrix from {e12,e34,e13,e14,e23,e24} to SD/ASD
# SD: rows give phi_i as linear combinations of basis
SD = np.array([
    [1, 1, 0, 0, 0, 0],   # phi1 = (e12+e34)/sqrt2
    [0, 0, 1, 0, 0, -1],  # phi2 = (e13-e24)/sqrt2
    [0, 0, 0, 1, 1, 0],   # phi3 = (e14+e23)/sqrt2
]) / np.sqrt(2)

ASD = np.array([
    [1, -1, 0, 0, 0, 0],  # psi1 = (e12-e34)/sqrt2
    [0, 0, 1, 0, 0, 1],   # psi2 = (e13+e24)/sqrt2
    [0, 0, 0, 1, -1, 0],  # psi3 = (e14-e23)/sqrt2
]) / np.sqrt(2)

def build_R_matrix(R_components):
    """Build 6x6 curvature operator from nonzero R_{ijkl}.
    Basis order: e12, e34, e13, e14, e23, e24.
    Input: dict of ((i,j),(k,l)) -> value."""
    
    idx = {(1,2): 0, (3,4): 1, (1,3): 2, (1,4): 3, (2,3): 4, (2,4): 5}
    M = np.zeros((6, 6))
    
    for (pair1, pair2), val in R_components.items():
        if pair1 in idx and pair2 in idx:
            M[idx[pair1], idx[pair2]] = val
            M[idx[pair2], idx[pair1]] = val  # symmetry
    
    return M

# ===== Example 1: Round S^4 with Ric = g =====
print("\n--- Example 1: Round S^4, constant curvature K = 1/3 ---")
print("(Ric = (n-1)K g = 3Kg = g => K = 1/3, s = n(n-1)K = 4)")

K = 1.0/3.0
# R_{ijkl} = K(delta_ik delta_jl - delta_il delta_jk)
# On Lambda^2: R = K * Id
R_S4 = K * np.eye(6)
evals_S4 = np.linalg.eigvalsh(R_S4)
det_S4 = np.linalg.det(R_S4)

R_S4_SD = SD @ R_S4 @ SD.T
det_S4_SD = np.linalg.det(R_S4_SD)

print(f"  R on Lambda^2 = K * Id, eigenvalues = {evals_S4}")
print(f"  det R (full Lambda^2) = K^6 = {det_S4:.10f}")
print(f"  det R|_{{Lambda^2_+}} = K^3 = {det_S4_SD:.10f}")
print(f"  W+ = R|_{{Lambda^2_+}} - (s/12)Id = 0")
print(f"  => det R != 0: S^4/Z_2 CANNOT be Einstein-desingularized")
results["S4"] = {
    "eigenvalues_full": list(np.sort(evals_S4)),
    "det_R_full": float(det_S4),
    "det_R_SD": float(det_S4_SD),
    "det_R_zero": False,
    "desingularizable": False
}

# ===== Example 2: S^2 x S^2, product metric =====
print("\n--- Example 2: S^2(1) x S^2(1), product Einstein metric ---")
print("(K1 = K2 = 1, Ric = g, s = 4)")

# R_{1212} = 1, R_{3434} = 1, rest = 0
R_comp_prod = {
    ((1,2), (1,2)): 1.0,
    ((3,4), (3,4)): 1.0,
}
R_prod = build_R_matrix(R_comp_prod)
evals_prod = np.linalg.eigvalsh(R_prod)
det_prod = np.linalg.det(R_prod)

R_prod_SD = SD @ R_prod @ SD.T
det_prod_SD = np.linalg.det(R_prod_SD)
evals_prod_SD = np.linalg.eigvalsh(R_prod_SD)

s = 4.0
W_plus_prod = R_prod_SD - (s/12.0) * np.eye(3)
evals_Wplus_prod = np.linalg.eigvalsh(W_plus_prod)

print(f"  R on Lambda^2 eigenvalues: {np.sort(evals_prod)}")
print(f"  det R (full Lambda^2) = {det_prod:.10f}")
print(f"  R|_{{Lambda^2_+}} eigenvalues: {np.sort(evals_prod_SD)}")
print(f"  det R|_{{Lambda^2_+}} = {det_prod_SD:.10f}")
print(f"  W+ eigenvalues: {np.sort(evals_Wplus_prod)}")
print(f"  det W+ = {np.linalg.det(W_plus_prod):.10f}")
print(f"  => det R = 0: (S^2xS^2)/Z_2 MAY be desingularizable")
results["S2xS2"] = {
    "eigenvalues_full": list(np.sort(evals_prod)),
    "det_R_full": float(det_prod),
    "eigenvalues_SD": list(np.sort(evals_prod_SD)),
    "det_R_SD": float(det_prod_SD),
    "Wplus_eigenvalues": list(np.sort(evals_Wplus_prod)),
    "det_Wplus": float(np.linalg.det(W_plus_prod)),
    "det_R_zero": True,
    "desingularizable": True
}

# ===== Example 3: CP^2, Fubini-Study with Ric = g =====
print("\n--- Example 3: CP^2, Fubini-Study with Ric = g ---")
print("(s = 4, W+ eigenvalues (2/3, -1/3, -1/3))")

# For CP^2 (Kahler-Einstein), W+ has eigenvalues s/6, -s/12, -s/12
# on the basis {omega, Re Omega, Im Omega} where omega is Kahler form
Wplus_CP2 = np.diag([2.0/3, -1.0/3, -1.0/3])
R_CP2_SD = Wplus_CP2 + (s/12.0) * np.eye(3)
det_CP2_SD = np.linalg.det(R_CP2_SD)
evals_CP2_SD = np.linalg.eigvalsh(R_CP2_SD)

print(f"  W+ eigenvalues: {np.sort(np.linalg.eigvalsh(Wplus_CP2))}")
print(f"  R|_{{Lambda^2_+}} = W+ + (s/12)Id eigenvalues: {np.sort(evals_CP2_SD)}")
print(f"  det R|_{{Lambda^2_+}} = {det_CP2_SD:.10f}")
print(f"  => det R = 0: CP^2 orbifolds MAY be desingularizable")
print(f"  Note: SAME det R as S^2 x S^2 — generic for KE 4-manifolds!")
results["CP2"] = {
    "Wplus_eigenvalues": [2./3, -1./3, -1./3],
    "eigenvalues_SD": list(np.sort(evals_CP2_SD)),
    "det_R_SD": float(det_CP2_SD),
    "det_R_zero": True,
    "desingularizable": True
}

# ===== General analysis: when does det R|_{Lambda^2_+} = 0? =====
print("\n--- General positive Einstein with Ric = g ---")
print("W+ eigenvalues (w1, w2, w3) with w1+w2+w3=0 (traceless)")
print("R|_{Lambda^2_+} eigenvalues: (w_i + 1/3)")
print("det R|_{Lambda^2_+} = (w1+1/3)(w2+1/3)(w3+1/3)")
print("")
print("This vanishes iff some w_i = -1/3, i.e., R has a zero")
print("eigenvalue on Lambda^2_+.")
print("")

# Symbolic: det = (w1+1/3)(w2+1/3)(-w1-w2+1/3)
# Let's sample the (w1, w2) space
print("Sampling the (w1, w2) space (w3 = -w1-w2, traceless):")
print("  S^4 (w1=0, w2=0):          det = ", f"{(1/3)**3:.6f}")
print("  S^2xS^2 (w1=2/3, w2=-1/3): det = ", 
      f"{(2/3+1/3)*(-1/3+1/3)*(-1/3+1/3):.6f}")
print("  CP^2 (w1=2/3, w2=-1/3):    det = ", 
      f"{(2/3+1/3)*(-1/3+1/3)*(-1/3+1/3):.6f}")

# Generic non-KE positive Einstein: typical W+ eigenvalues
# E.g., Page metric on CP^2 # overline{CP^2} — not relevant (tau != 0)
# For S^4 deformation: w1 ~ epsilon, det ~ 1/27 - O(epsilon)
print("")
print("For small perturbation from S^4: w_i = epsilon_i (small)")
print("  det ~ (1/3)^3 + O(epsilon) = 1/27 + O(epsilon) > 0")
print("  So S^4-like orbifolds have det R > 0: not desingularizable")
print("")

# ===== KEY THEOREM =====
print("=" * 70)
print("KEY RESULT FOR OBSTRUCTION-AMPLITUDE PRINCIPLE")
print("=" * 70)
print("")
print("det R|_{Lambda^2_+} = 0 at an Einstein (Ric=g) orbifold point iff")
print("one W+ eigenvalue equals -1/3.")
print("")
print("This condition is equivalent to the curvature operator having a")
print("KERNEL on Lambda^2_+, which for Kahler-Einstein 4-manifolds is")
print("automatic (the anti-holomorphic self-dual 2-forms are in the kernel).")
print("")
print("POSITIVE-BRANCH ARGUMENT SHAPE:")
print("1. delta_i -> 0 noncollapsed sequence -> Einstein orbifold limit")
print("2. Obstruction-amplitude: nonzero det R forces C^0 Ricci excess ~ O(1)")
print("   (the non-scalar obstruction endomorphism survives in operator norm)")
print("3. Therefore delta_i -> 0 forces det R = 0 at each singularity")
print("4. By Ozuch Thm 0.3: this is the necessary condition for desingularization")
print("5. By Biquard: with det R = 0, desingularization IS possible")
print("   (under nondegeneracy + appropriate ALE model conditions)")
print("6. By LeBrun-Ozuch Thm B: positive Einstein orbifold limits with")
print("   ASD ALE bubbles have Kahler-Einstein rigidity")
print("")
print("CONCLUSION: Regime (II) of P_4^+ (noncollapsed curvature concentration)")
print("is solvable IF the approximate-to-exact bridge and higher-order")
print("obstruction vanishing can be established.")
print("")
print("EVIDENCE FROM LITERATURE:")
print("- Ozuch Example 1: S^4/Z_2 has det R = 1 != 0, and L^p-close")
print("  approximate Einstein metrics exist but C^0-close ones do NOT")
print("  (confirming the obstruction-amplitude mechanism)")
print("- Biquard 2013: desingularization succeeds for R^4/Z_2 with det R = 0")
print("- All known positive KE orbifolds (CP^2/Gamma, (S^2xS^2)/Gamma)")
print("  have det R = 0: obstruction-compatible")

# Save results
output_path = "Sessions/S0910A02/workspace/data/step7_det_R_obstruction.json"
with open(output_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {output_path}")
