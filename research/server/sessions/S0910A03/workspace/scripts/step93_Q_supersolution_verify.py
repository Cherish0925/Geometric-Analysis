"""
Step 93c: algebraic verification of the diagonal fixed-charge identity
L(log Q) = -18 - 4Q.

STEP 94 CORRECTION: the identity is correct but the maximum-principle inference
formerly printed below was false. For L=Delta+grad(sigma).grad, an interior
maximum has LQ<=0, fully compatible with LQ=-18Q-4Q^2<0. Retain this file only
for the diagonal algebra; use step94_invariant_charge_identity.py for the full
fixed-charge formula and step94_scalar_superharmonic_countermodel.py for the
sign countermodel.
"""
import sympy as sp
from sympy import symbols, Function, exp, diff, simplify, expand, collect, sqrt
import json
from pathlib import Path

r, z = symbols('r z', real=True)

# Functions on the 2D base
sigma = Function('sigma')(r, z)
alpha = Function('alpha')(r, z)   # orbit anisotropy
q0 = symbols('q0', positive=True, real=True)  # CONSTANT charge (exact Einstein)

# Abbreviations
sr, sz = diff(sigma, r), diff(sigma, z)
ar, az = diff(alpha, r), diff(alpha, z)
srr, szz = diff(sigma, r, 2), diff(sigma, z, 2)
arr, azz = diff(alpha, r, 2), diff(alpha, z, 2)
srz = diff(sigma, r, z)
arz = diff(alpha, r, z)

# Q = (1/2) q0^2 exp(-(3σ + α)) for diagonal M, constant q=(q0,0)
h = -3*sigma - alpha
Q_expr = sp.Rational(1,2) * q0**2 * exp(h)

# Compute drift Laplacian: L = Δ + ∇σ · ∇
def L(f):
    """Drift Laplacian on flat base metric dr² + dz²."""
    return diff(f, r, 2) + diff(f, z, 2) + sr*diff(f, r) + sz*diff(f, z)

# Step 1: Raw computation
LQ_raw = L(Q_expr)
LQ_expanded = expand(LQ_raw)

# Factor out Q_expr
# Q = (1/2)q0² exp(h), h = -3σ-α
# ∇Q = Q·∇h = Q(-3∇σ - ∇α)
# |∇Q|² = Q²·|∇h|² = Q²(9|∇σ|² + 6⟨∇σ,∇α⟩ + |∇α|²)

hr, hz = -3*sr - ar, -3*sz - az
grad_h_sq = hr**2 + hz**2  # = |3∇σ + ∇α|²

# L(exp(h)) = exp(h)·(Lh + |∇h|²)
Lh = L(h)
Lh_explicit = expand(Lh)  # = -3Lσ - Lα = -3(σ_rr+σ_zz+σ_r²+σ_z²) - (α_rr+α_zz+σ_r·α_r+σ_z·α_z)

# Step 2: Substitute Einstein equations
# Lσ = 6 + Q  →  srr + szz + sr² + sz² = 6 + Q_sym (symbolic)
# Lα = Q       →  arr + azz + sr·ar + sz·az = Q_sym

Q_sym = symbols('Q', positive=True)
grad_sig_sq = sr**2 + sz**2
cross_sig_alp = sr*ar + sz*az
grad_alp_sq = ar**2 + az**2

# From Lσ = 6+Q:  Δσ = 6+Q - |∇σ|²
Delta_sigma = srr + szz  # = 6 + Q - grad_sig_sq  (after using Lσ=6+Q)

# From Lα = Q:  Δα = Q - ⟨∇σ,∇α⟩
Delta_alpha = arr + azz   # = Q - cross_sig_alp  (after using Lα=Q)

# The coefficient of Q in LQ = Q × (|∇h|² - 3Δσ - Δα)
# Note: Lh = -3Lσ - Lα = -3Δσ - Δα - 3|∇σ|² - ⟨∇σ,∇α⟩
# And Lh + |∇h|² = what appears in L(Q) = Q(Lh + |∇h|²)

# Compute the bracket:
bracket = sp.Symbol('B')  # placeholder

# Manual computation:
# bracket = |∇h|² + Lh
#         = (9|∇σ|² + 6⟨∇σ,∇α⟩ + |∇α|²) + (-3Δσ - Δα - 3|∇σ|² - ⟨∇σ,∇α⟩)
#         = 6|∇σ|² + 5⟨∇σ,∇α⟩ + |∇α|² - 3Δσ - Δα

# Substitute Δσ = 6+Q-|∇σ|², Δα = Q-⟨∇σ,∇α⟩:
# bracket = 6|∇σ|² + 5⟨∇σ,∇α⟩ + |∇α|² - 3(6+Q-|∇σ|²) - (Q-⟨∇σ,∇α⟩)
#         = 6|∇σ|² + 5⟨∇σ,∇α⟩ + |∇α|² - 18 - 3Q + 3|∇σ|² - Q + ⟨∇σ,∇α⟩
#         = 9|∇σ|² + 6⟨∇σ,∇α⟩ + |∇α|² - 18 - 4Q
#         = |3∇σ + ∇α|² - 18 - 4Q

# But |3∇σ + ∇α|² = |∇h|² = |∇Q/Q|² (since ∇Q = -Q·∇h, so |∇Q|² = Q²|∇h|²)
# Therefore: bracket = |∇Q|²/Q² - 18 - 4Q

# And: LQ = Q·bracket = |∇Q|²/Q - 18Q - 4Q²

# VERIFICATION: check with the substitution rules
s2, cs, a2 = symbols('s2 cs a2', real=True)  # |∇σ|², ⟨∇σ,∇α⟩, |∇α|²

bracket_expr = 6*s2 + 5*cs + a2 - 3*(6 + Q_sym - s2) - (Q_sym - cs)
bracket_simplified = expand(bracket_expr)
# Expected: 9*s2 + 6*cs + a2 - 18 - 4*Q_sym
print("Bracket after Einstein substitution:")
print(f"  = {bracket_simplified}")
print(f"  = {collect(bracket_simplified, [s2, cs, a2, Q_sym])}")

# Check: should be 9s2 + 6cs + a2 - 18 - 4Q = |3∇σ+∇α|² - 18 - 4Q
grad_h_sq_check = 9*s2 + 6*cs + a2
print(f"\n|3∇σ+∇α|² = {grad_h_sq_check}")
print(f"bracket - (|3∇σ+∇α|² - 18 - 4Q) = {expand(bracket_simplified - grad_h_sq_check + 18 + 4*Q_sym)}")

# Step 3: L(log Q) = LQ/Q - |∇Q|²/Q²
# = (|∇Q|²/Q² - 18 - 4Q) - |∇Q|²/Q² = -18 - 4Q
print("\n=== KEY IDENTITY (exact Einstein, diagonal one-charge) ===")
print("L(log Q) = -18 - 4Q")
print("\nAt any interior max of Q (where ∇Q=0, LQ≤0):")
print("  LQ = -18Q - 4Q² < 0, which is COMPATIBLE with an interior maximum.")
print("  There is no boundary-maximum conclusion. L(log Q)<0 is superharmonicity.")

# Step 4: General (non-diagonal) case
print("\n=== General free-T² case ===")
print("Q = (1/2)ρ^{-3} q^T M^{-1} q, with Hess_{H²}Q = Qh")
print("For σ-harmonic U with τ_σ=0:")
print("  L(Q_target ∘ U) = Q_target · |dU|² = Q_target · e")
print("where Q_target = (1/2)q^T M^{-1} q (the target function)")
print("")
print("L(ρ^{-3}) = ρ^{-3}[-3Lσ + 9|∇σ|²]")
print("         = ρ^{-3}[-18-3Q + 9|∇σ|²]")
print("")
print("The product rule gives:")
print("  LQ = L(ρ^{-3} · Q_tgt∘U)")
print("     = ρ^{-3}L(Q_tgt∘U) + Q_tgt∘U·L(ρ^{-3}) + 2∇(ρ^{-3})·∇(Q_tgt∘U)")
print("")
print("First term: Qe (from target harmonic map)")
print("Second term: Q(-18-3Q+9|∇σ|²)")
print("Third term: -6Q⟨∇σ, (∇_H Q_tgt)(dU)⟩/Q_tgt = -6Q⟨∇σ, direction⟩")
print("")
print("The direction is the pullback of the unit gradient of Q_tgt on H².")
print("Since |∇_H Q_tgt| = Q_tgt, this term has magnitude ≤ 6Q|∇σ|·√e.")

# Step 5: Forced case structure
print("\n=== Forced case structure ===")
print("L(log Q) = -18 - 4Q + 2L(log q₀) - 3D_σ - D_α")
print("where |D_σ| ≤ Cδ, |D_α| ≤ Cδ (Ricci defect)")
print("and L(log q₀) involves Δq₀/q₀ = d*S/q₀ ← DERIVATIVES OF E")
print("")
print("This is the identified gap: controlling L(log q₀) requires")
print("either C¹ regularity of E or a weak (integrated) formulation.")
print("")
print("STEP 94: the negative reaction is not an upper-bound mechanism.")
print("A weak formulation may move derivatives off E, but cannot create a")
print("maximum estimate or imply Q=O(δ²).")

# Step 6: Forced reaction from area and orbit defects alone
print("\n=== Partial forced bound (area+orbit only, no charge derivative) ===")
print("If we IGNORE the L(log q₀) term:")
print("  L(log Q) ≤ -18 + 4δ  (at the max, where the defect terms are ≤ 4δ)")
print("  Even if L(log Q)<0 at a maximum, this gives no contradiction.")
print("  The earlier proposed closure was wrong independently of charge derivatives.")
print("  Variable-charge logarithms are additionally singular at charge zeros.")

# Save results
result = {
    "exact_LQ_formula": "LQ = |∇Q|²/Q - 18Q - 4Q²",
    "exact_L_logQ": "L(log Q) = -18 - 4Q",
    "mechanism": "Area equation (Lσ=6+Q) contributes -18-3Q; orbit equation (Lα=Q) contributes -Q; total reaction -18-4Q",
    "step94_correction": "The identity has no maximum-principle corollary: negative LQ is compatible with an interior maximum.",
    "forced_L_logQ_formal_diagonal": "L(log Q) = -18 - 4Q + 2L(log q₀) - 3D_σ - D_α",
    "forced_status": "Derivative placement is secondary; the reaction sign itself gives no upper bound. Use a global vector-charge flux formulation.",
    "hopf_quadratic_coefficient": 4,
    "hopf_linear_coefficient": 18,
    "bracket_residual": 0  # verified symbolically
}
out = Path("workspace/data/step93_Q_maximum_principle.json")
out.write_text(json.dumps(result, indent=2))
print(f"\nwrote {out}")
