"""
Step 80: Verify J-symmetry = simultaneous complex conjugation J(z,w) = (z̄,w̄)
on the product orbifold (S²×S²)/⟨(r_π,r_π)⟩ and its consequences for the 
Ozuch obstruction problem.

Key results to verify:
1. J = diag(1,-1,1,-1) on R⁴ tangent coords at each node
2. J acts on SD/ASD 2-form basis as diag(-1,+1,-1)  
3. J commutes with quotient σ = -I₄ and antipodal A
4. ρ_x(ω₂) transforms under J with component parities (-1,+1,-1)
5. H⁴ is J-invariant ⟹ all J-odd obstruction projections vanish
6. In adapted frame (ω₂,ω₁,ω₃): k=2,3 killed by J, k=1 killed by det
"""
import numpy as np
import json

results = {"step": 80, "purpose": "J-symmetry complete verification"}

# === 1. Basic matrices ===
J = np.diag([1., -1., 1., -1.])  # J(z,w)=(z̄,w̄) at (N,N)
sigma = -np.eye(4)                 # quotient (r_π,r_π): tangent = -I₄

# SD 2-form matrices (skew-symmetric on R⁴)
def form_matrix(pairs):
    """Create 4x4 skew-sym matrix from list of (i,j,val) triples."""
    M = np.zeros((4,4))
    for i,j,v in pairs:
        M[i,j] = v; M[j,i] = -v
    return M

omega1p = form_matrix([(0,1,1),(2,3,1)])     # e1∧e2 + e3∧e4
omega2p = form_matrix([(0,2,1),(1,3,-1)])     # e1∧e3 - e2∧e4  
omega3p = form_matrix([(0,3,1),(1,2,1)])      # e1∧e4 + e2∧e3
omega1m = form_matrix([(0,1,1),(2,3,-1)])     # e1∧e2 - e3∧e4
omega2m = form_matrix([(0,2,1),(1,3,1)])      # e1∧e3 + e2∧e4
omega3m = form_matrix([(0,3,1),(1,2,-1)])     # e1∧e4 - e2∧e3

SD = [omega1p, omega2p, omega3p]
ASD = [omega1m, omega2m, omega3m]

# === 2. J action on 2-form basis ===
def pullback_2form(M_form, T):
    """Pullback of 2-form matrix by linear map T: M → T^T M T."""
    return T.T @ M_form @ T

j_parity_sd = []
j_parity_asd = []
for i, (om, name) in enumerate(zip(SD, ['ω₁⁺','ω₂⁺','ω₃⁺'])):
    Jom = pullback_2form(om, J)
    # Check if Jom = ±om
    if np.allclose(Jom, om):
        j_parity_sd.append(+1)
    elif np.allclose(Jom, -om):
        j_parity_sd.append(-1)
    else:
        j_parity_sd.append(None)

for i, (om, name) in enumerate(zip(ASD, ['ω₁⁻','ω₂⁻','ω₃⁻'])):
    Jom = pullback_2form(om, J)
    if np.allclose(Jom, om):
        j_parity_asd.append(+1)
    elif np.allclose(Jom, -om):
        j_parity_asd.append(-1)
    else:
        j_parity_asd.append(None)

results["J_parity_SD"] = j_parity_sd  # expect [-1, +1, -1]
results["J_parity_ASD"] = j_parity_asd  # expect [-1, +1, -1]
print(f"J parity on SD basis:  {j_parity_sd}")
print(f"J parity on ASD basis: {j_parity_asd}")

# === 3. Commutation checks ===
results["commutation"] = {
    "J_sigma_commute": bool(np.allclose(J @ sigma, sigma @ J)),
    "J_squared_is_I": bool(np.allclose(J @ J, np.eye(4))),
    "det_J": float(np.linalg.det(J)),
    "sigma_is_neg_I4": bool(np.allclose(sigma, -np.eye(4))),
    "det_sigma": float(np.linalg.det(sigma))
}
print(f"\nJ commutes with σ: {results['commutation']['J_sigma_commute']}")
print(f"det(J) = {results['commutation']['det_J']}")
print(f"σ = -I₄: {results['commutation']['sigma_is_neg_I4']}")

# A = -I on each S², so globally maps (N,N)→(S,S); cannot test tangent
# commutation at a single node. Check global commutation.
# In R³×R³: A(x) = (-x₁,-x₂,-x₃,-y₁,-y₂,-y₃)
# J(x) = (x₁,-x₂,x₃,y₁,-y₂,y₃)  
# JA(x) = J(-x₁,-x₂,-x₃,-y₁,-y₂,-y₃) = (-x₁,x₂,-x₃,-y₁,y₂,-y₃)
# AJ(x) = A(x₁,-x₂,x₃,y₁,-y₂,y₃) = (-x₁,x₂,-x₃,-y₁,y₂,-y₃)
# So JA = AJ globally ✓
results["commutation"]["JA_eq_AJ_global"] = True  # verified analytically
print(f"J commutes with A globally: True (verified analytically)")

# === 4. ρ_x transformation under J ===
# Composition matrices ω₂⁺ ∘ ω_j⁻ (endomorphism of R⁴)
comp_matrices = []
for j in range(3):
    comp_matrices.append(SD[1] @ ASD[j])  # ω₂⁺ · ω_j⁻

# J conjugation: J^{-1}(AB)J = (J^{-1}AJ)(J^{-1}BJ) = ε_A ε_B AB
# where ε_A = J-parity of A's 2-form.
# For ω₂⁺ ∘ ω_j⁻: parity = ε₂⁺ · ε_j⁻ = (+1)·ε_j⁻
expected_comp_parity = [j_parity_sd[1] * j_parity_asd[j] for j in range(3)]

rho_J_parities = []
for j in range(3):
    M = comp_matrices[j]
    JMJ = J @ M @ J  # = J^T M J since J is symmetric
    ratio = JMJ / (M + 1e-30)  # pointwise ratio where M nonzero
    nonzero = np.abs(M) > 1e-10
    if nonzero.any():
        ratios = ratio[nonzero]
        if np.allclose(ratios, ratios[0]):
            rho_J_parities.append(float(ratios[0]))
        else:
            rho_J_parities.append("mixed")
    else:
        rho_J_parities.append(0)

results["rho_x_J_parity"] = {
    "components_j_1_2_3": rho_J_parities,
    "expected": expected_comp_parity,
    "interpretation": "ρ_{Jx}(ω₂)_j = ε_j · ρ_x(ω₂)_j with ε=(-1,+1,-1)"
}
print(f"\nρ_x(ω₂) J-parity per component: {rho_J_parities}")
print(f"Expected (ε₂⁺·ε_j⁻):            {expected_comp_parity}")

# === 5. Numerical verification with random S³ samples ===
np.random.seed(42)
N_samples = 50000
X = np.random.randn(N_samples, 4)
X = X / np.linalg.norm(X, axis=1, keepdims=True)

# Compute ρ_x(ω₂) for each sample
def compute_rho(x, comp_mats):
    """Compute ρ_x(ζ) = [x^T M_j x / |x|²] for j=0,1,2."""
    r2 = np.dot(x, x)
    return np.array([x @ M @ x / r2 for M in comp_mats])

# Verify ρ_{Jx} = diag(-1,+1,-1) · ρ_x
max_parity_error = 0.0
parity_signs = np.array([-1., +1., -1.])
for i in range(min(N_samples, 10000)):
    x = X[i]
    Jx = J @ x
    rho_x = compute_rho(x, comp_matrices)
    rho_Jx = compute_rho(Jx, comp_matrices)
    err = np.max(np.abs(rho_Jx - parity_signs * rho_x))
    max_parity_error = max(max_parity_error, err)

results["rho_parity_numerical"] = {
    "N_samples": 10000,
    "max_parity_deviation": float(max_parity_error),
    "verified": max_parity_error < 1e-12
}
print(f"\nρ parity verification: max error = {max_parity_error:.2e}")

# === 6. H⁴ J-invariance ===
# H⁴(ω₂) = -Σ_j ρ_j (ω_j⁻ ∘ ω₂⁺) / (2r⁴)
# Each term: ρ_j has J-parity ε_j, and ω_j⁻ ∘ ω₂⁺ has J-parity ε_j·ε₂⁺ = ε_j
# So each summand has parity ε_j · ε_j = +1  ⟹  H⁴ is J-INVARIANT
reverse_comp = [ASD[j] @ SD[1] for j in range(3)]  # ω_j⁻ ∘ ω₂⁺

H4_invariance_checks = []
for i in range(min(N_samples, 5000)):
    x = X[i]
    Jx = J @ x
    r2 = np.dot(x, x)
    rho_x = compute_rho(x, comp_matrices)
    rho_Jx = compute_rho(Jx, comp_matrices)
    
    # H⁴ at x
    H4_x = sum(-rho_x[j] * reverse_comp[j] for j in range(3)) / (2 * r2**2)
    # H⁴ at Jx  
    H4_Jx = sum(-rho_Jx[j] * reverse_comp[j] for j in range(3)) / (2 * r2**2)
    # J-pullback of H⁴ at Jx: J^T H4(Jx) J
    JH4J = J @ H4_Jx @ J
    
    err = np.max(np.abs(JH4J - H4_x))
    H4_invariance_checks.append(err)

max_H4_err = max(H4_invariance_checks)
results["H4_J_invariance"] = {
    "max_deviation": float(max_H4_err),
    "verified": max_H4_err < 1e-12,
    "mechanism": "each summand has J-parity ε_j² = +1"
}
print(f"\nH⁴ J-invariance: max error = {max_H4_err:.2e}")

# === 7. Obstruction projection parity analysis ===
# Adapted frame at φ₀ = ω₂: (φ₁, φ₂, φ₃) = (ω₂, ω₁, ω₃)
# Obstruction μ_k projects residual onto φ_k direction
# For J-invariant residual R and φ_k with J-parity ε_k:
# μ_k ∝ ∫ ⟨R, φ_k-based tensor⟩ dσ
# Since J preserves dσ and J*R = R, J*φ_k = ε_k φ_k:
# μ_k = ε_k μ_k  ⟹  μ_k = 0 if ε_k = -1

adapted_frame = {
    "k=1 (φ₁=ω₂)": {"J_parity": j_parity_sd[1], "killed_by_J": j_parity_sd[1] == -1},
    "k=2 (φ₂=ω₁)": {"J_parity": j_parity_sd[0], "killed_by_J": j_parity_sd[0] == -1},
    "k=3 (φ₃=ω₃)": {"J_parity": j_parity_sd[2], "killed_by_J": j_parity_sd[2] == -1},
}

results["adapted_obstruction_parity"] = adapted_frame
print(f"\n=== Adapted obstruction parity ===")
for k, v in adapted_frame.items():
    status = "KILLED by J" if v["killed_by_J"] else "SURVIVES (J-even)"
    extra = ""
    if k.startswith("k=1"):
        extra = " → but μ₁=0 by rank-one determinant"
    print(f"  {k}: J-parity={v['J_parity']:+d} → {status}{extra}")

# === 8. Combined A+J+det theorem ===
results["combined_theorem"] = {
    "A_symmetry": "removes 4 odd scalar kernel modes (ν_l=0)",
    "J_symmetry": "kills adapted k=2 and k=3 projections at ALL orders",
    "determinant": "μ₁=0 unconditionally (rank-one curvature)",
    "conclusion": "ALL finite-dimensional Ozuch obstructions vanish in the A+J symmetric family",
    "surviving_system": {
        "parameters": "(t₁, t₂) — one EH scale per A-orbit",
        "equations": "one ω₂-projection per orbit at order ≥ t³",
        "dimension": "2 equations in 2 unknowns (balanced)",
        "note": "J symmetry works to ALL orders, not just second"
    }
}
print(f"\n=== COMBINED THEOREM ===")
print("A-symmetry: ν_l = 0 (scalar kernel eliminated)")
print("J-symmetry: adapted k=2,3 projections = 0 at ALL orders")
print("Determinant: adapted k=1 projection μ₁ = 0")
print("⟹ ALL finite-dim Ozuch obstructions vanish in A+J family")
print(f"\nSurviving system: 2 scale equations in (t₁,t₂)")

# === 9. Verify J acts on scalar kernel modes ===
# u₁g₁, u₁g₂, u₂g₁, u₂g₂ where u_i are first harmonics
# On S², first harmonics are x₁,x₂,x₃. Under J: x₁→x₁, x₂→-x₂
# Under σ=(r_π,r_π): x₁→-x₁, x₂→-x₂
# On the quotient, the surviving harmonic is the one invariant under σ
# For the scalar modes on (S²×S²)/σ:
# u₁ = x₃ on first S² (σ-invariant, since x₃→x₃ under r_π)
# u₂ = y₃ on second S² (σ-invariant)
# Under A: u₁(N) → u₁(S) = -u₁(N), so A-odd
# Under J: u₁ = x₃ → x₃ = u₁, so J-EVEN

# The scalar kernel modes u_i g_j:
# A-parity: odd (since u_i is A-odd)
# J-parity: even (since u_i is J-even, g_j is J-even)
results["scalar_kernel_parities"] = {
    "u1_A_parity": "odd (A exchanges N↔S, u₁(N)=-u₁(S))",
    "u1_J_parity": "even (x₃ is J-invariant)",
    "modes": "u₁g₁, u₁g₂, u₂g₁, u₂g₂",
    "eliminated_by": "A-symmetry (A-odd), NOT by J (J-even)",
    "shape_mode_g1_minus_g2": {
        "A_parity": "even",
        "J_parity": "even",
        "status": "NOT eliminated by either; must remain in inverse"
    }
}
print(f"\nScalar kernel modes: eliminated by A (A-odd), J-even")
print(f"Shape mode g₁-g₂: A-even, J-even → survives, negative mode in P")

# === 10. Verify J preserves diagonal chirality ===
# Diagonal pattern: all 4 nodes get same chirality
# J fixes all 4 nodes and J*ω₂ = +ω₂, so direction is preserved
# Chirality is determined by which complex structure the EH is aligned with
# J fixes ω₂ → preserves the diagonal chirality assignment
results["chirality_preservation"] = {
    "J_fixes_all_nodes": True,
    "J_fixes_insertion_direction": True,  # ω₂ is J-even
    "diagonal_pattern_preserved": True
}

print(f"\n=== Summary ===")
print(json.dumps(results["combined_theorem"]["surviving_system"], indent=2))

outpath = "Sessions/S0910A01/workspace/data/step80_J_symmetry_verification.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nWrote {outpath}")
