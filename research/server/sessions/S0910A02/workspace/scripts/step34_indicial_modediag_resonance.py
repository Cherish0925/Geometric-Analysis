#!/usr/bin/env python3
"""
Step 34: Mode-diagonal indicial structure, pairing table, and resonance analysis
for the flat A₁ cone C(S³/Z₂) = R⁴/{±1}.

Mathematical content:
1. On the flat cone, the Lichnerowicz/linearized Einstein operator is the
   componentwise rough Laplacian, which preserves angular harmonics.
2. For each angular degree l (even, by Z₂ parity), homogeneous solutions
   of the radial ODE have rates α = l and α = -(l+2).
3. The Taub/Wronskian boundary integral is mode-diagonal: it pairs only
   within the same angular mode l.
4. For l=2: the (2, -4) pair IS Ozuch's obstruction (Corollary 4.10).
5. The l=0 pair is gauge-removable on the growing side and mass/volume on
   the decaying side; it is Wronskian-invisible to l≥2 test fields.
6. Resonance analysis: a δ-size source at rate r⁰ in the l=2 radial ODE
   produces a particular solution with a logarithmic resonance δ r² log r.
   The key question is whether the Bianchi constraint removes this resonance.

Convention: we use the research's t⁴ coefficient (t⁴ H⁴ for ALE), so
balance radius is r = t^{2/3}. Ozuch uses t² H⁴, balance at t^{1/3}.
These are consistent with t_ours² = t_Ozuch.
"""

import json
import numpy as np
from fractions import Fraction
import sympy as sp

# ============================================================
# 1. Radial ODE for each angular degree l on the flat 4-cone
# ============================================================
# For a mode f(r) × T_l(σ) with angular degree l on S³,
# the radial equation in dimension d=4 is:
#
#   f''(r) + (d-1)/r f'(r) - μ_l/r² f(r) = 0
#
# where μ_l is the effective angular eigenvalue.
# Homogeneous solutions f = r^α give:
#   α(α-1) + 3α - μ_l = α² + 2α - μ_l = 0
# For roots α = l and α = -(l+2): μ_l = l(l+2) - 0 ... check:
#   l² + 2l - μ = 0  and  (l+2)² - 2(l+2) - μ = l² + 4l + 4 - 2l - 4 - μ = l² + 2l - μ = 0  ✓
# So μ_l = l² + 2l = l(l+2).
#
# For type-III TT tensor harmonics of degree l on S³:
#   Δ_{S³} TT_l = (l(l+2) - 2) TT_l  (Berger–Ebin formula for S³)
# But on the flat cone, the effective equation uses μ_l = l(l+2) directly
# because the cone Lichnerowicz operator = rough Laplacian on flat space.

results = {
    "title": "Step 34: Mode-diagonal indicial structure and resonance on flat A₁ cone",
    "scope": "Route A noncollapsed positive subroute; not a proof of Yau-26.",
}

# ============================================================
# 2. Indicial roots and Z₂ parity
# ============================================================
indicial = []
for l in range(6):
    alpha_reg = l
    alpha_sing = -(l + 2)
    kept = (l % 2 == 0)
    mu = l * (l + 2)
    indicial.append({
        "l": l,
        "mu_l": mu,
        "alpha_regular": alpha_reg,
        "alpha_singular": alpha_sing,
        "Z2_parity_even": kept,
        "kept_on_A1_cone": kept,
        "wronskian_sum": alpha_reg + alpha_sing,  # always -2
    })
results["indicial_roots"] = indicial

# ============================================================
# 3. Mode-diagonal Wronskian pairing at radius R
# ============================================================
# The bilinear Taub/Wronskian boundary integral at S³(R)/Z₂:
#
#   W_l(R) = ∫_{S³/Z₂} Ric_e^{(2)}(h_l, k_l)(X, ∂_r) dv
#
# For h_l = A r^l T_l(σ) and k_l = B r^{-(l+2)} T_l(σ):
# The integrand has radial part ~ R^{l + (-(l+2)) + 3 - 1} = R^0
# (boundary area R³ × radial scaling R^{l-(l+2)-1}).
# So the Wronskian is R-independent for each self-paired mode. ✓
#
# Cross-mode vanishing: ∫_{S³/Z₂} T_l · T_{l'} dv = 0 for l ≠ l'
# by orthogonality of spherical tensor harmonics.
#
# The Ric_e^{(2)} is bilinear and preserves the angular type:
# Ozuch line 626: Ric_e^{(2)}(H⁴, H₂) = Σ_j R^+_{kj} θ_l⁻ ∘ ω_j⁺/r⁴
# This lives in the SAME angular space as H⁴ = θ_l⁻ ∘ ω_k⁺/r⁴.
# Therefore mode-diagonality is confirmed at the source level.

results["mode_diagonality"] = {
    "statement": (
        "On flat R⁴/{±1}, the bilinear form Ric_e^{(2)}(h,k)(X,∂_r) "
        "preserves angular degree l. Cross-mode pairs l ≠ l' integrate to zero "
        "by orthogonality of tensor harmonics on S³/Z₂."
    ),
    "source": "Ozuch 2021 line 626: Ric_e^{(2)} maps l=2 to l=2",
    "consequence": (
        "The Wronskian/Taub obstruction integral pairs only within the same "
        "angular mode. This is WHY α + β = -2 (same l on both sides)."
    ),
}

# ============================================================
# 4. Pairing table at the balance radius r = t^{2/3}
# ============================================================
# Convention: t⁴ coefficient for ALE insertion.
# Orbifold coefficients: A_l = O(1) for each even l ≥ 0.
# ALE coefficients at angular degree l: the dominant EH term is l=2
# with coefficient t⁴ · A_{-4} where A_{-4} = O(1).
# Higher ALE modes (l=4 etc.) enter at higher t powers.
#
# For the l=0 mass mode: coefficient t² (in our convention, from
# Ozuch's H₂⁴ ~ r⁻² with coefficient t²).
#
# For the l=2 mode: coefficient t⁴ (the EH r⁻⁴ asymptotics).
#
# At r = t^{2/3}:
#   |r^l| = t^{2l/3}
#   |t⁴ r^{-(l+2)}| = t⁴ · t^{-2(l+2)/3} = t^{(12 - 2l - 4)/3} = t^{(8-2l)/3}

pairing_table = []
t = sp.Symbol('t', positive=True)

# l=0: mass/volume pair
l_val = 0
reg_size_0 = t**(sp.Rational(2*l_val, 3))  # = 1
sing_size_0 = t**2 * t**(sp.Rational(-2*(l_val+2), 3))  # mass ~ t²/r² at balance
# At r=t^{2/3}: t²·t^{-4/3} = t^{2/3}
pairing_table.append({
    "label": "l=0 (mass/volume)",
    "regular_rate": 0,
    "singular_rate": -2,
    "regular_size_at_balance": str(reg_size_0),  # 1
    "singular_size_at_balance": "t^(2/3)",
    "wronskian_signal": "not flux-visible (angular-orthogonal to l>=2 tests)",
    "gauge_status": "pure gauge on growing side; mass/volume on decaying side",
    "note": "Larger than l=2 modes in absolute size, but invisible by mode-diagonality",
})

# l=2: main obstruction pair
l_val = 2
reg_size_2 = t**(sp.Rational(2*l_val, 3))  # t^{4/3}
sing_size_2 = t**4 * t**(sp.Rational(-2*(l_val+2), 3))  # t^{4/3}
pairing_table.append({
    "label": "l=2 (H₂/H⁴ Ozuch obstruction)",
    "regular_rate": 2,
    "singular_rate": -4,
    "regular_size_at_balance": "t^(4/3)",
    "singular_size_at_balance": "t^(4/3)",
    "wronskian_signal": "t⁴ (radius-independent, R⁰)",
    "gauge_status": "first non-gauge mode; signal = R⁺·v (Ozuch Cor 4.10)",
    "note": "This IS the obstruction. Nonzero iff det R_+ ≠ 0.",
})

# l=4: next even mode
l_val = 4
# ALE coefficient at l=4: higher order, ~ t⁸ (two orders above t⁴)
pairing_table.append({
    "label": "l=4 (higher curvature)",
    "regular_rate": 4,
    "singular_rate": -6,
    "regular_size_at_balance": "t^(8/3)",
    "singular_size_at_balance": "t^(8/3) [coefficient t⁸]",
    "wronskian_signal": "t^(16/3) [subleading, ≪ t⁴]",
    "gauge_status": "non-gauge; decoupled from l=2",
    "note": "Angular-orthogonal to l=2 test; contributes at higher order",
})

# Cross-mode entries (all zero)
cross_modes = []
for l1, l2 in [(2, 0), (2, 4), (0, 2), (4, 2)]:
    cross_modes.append({
        "l1": l1, "l2": l2,
        "integral": 0,
        "reason": f"angular orthogonality: ∫ T_{l1} · T_{l2} = 0 on S³/Z₂",
    })

# Same-direction (α, α) entries
same_dir = [
    {
        "pair": "(2, 2) same-direction",
        "size_at_balance": "t^(8/3) ≪ t⁴",
        "note": "Wronskian of a mode with itself vanishes: W[f,f]=0",
    },
    {
        "pair": "(-4, -4) same-direction",
        "size_at_balance": "would give t⁴ × t⁴ / t^(16/3) = t^(8/3)",
        "note": "Antisymmetry: W[f,f]=0; also angular: Ric^{(2)}(H⁴,H⁴) is O(r⁻⁸), subleading",
    },
]

results["pairing_table"] = {
    "balance_radius": "r = t^(2/3) (our convention: t⁴ ALE coefficient)",
    "entries": pairing_table,
    "cross_modes_all_zero": cross_modes,
    "same_direction_all_zero": same_dir,
    "conclusion": (
        "At the balance radius, the ONLY flux-visible contribution at O(t⁴) "
        "is the l=2 dual pair (H₂, t⁴H⁴). The l=0 mass mode is larger "
        "in absolute size (O(t^{2/3}) > O(t^{4/3})) but angular-orthogonal. "
        "Higher modes are subleading. Same-direction pairings vanish."
    ),
}

# ============================================================
# 5. Resonance analysis for the l=2 radial ODE
# ============================================================
# ODE: f'' + 3f'/r - 8f/r² = S(r)  [l=2 sector]
# Homogeneous: r², r⁻⁴.  Wronskian W = -6r⁻³.
#
# For constant source S = δ:
# Variation of parameters from r₀ to r₁:

r, delta_sym, r0, r1 = sp.symbols('r delta r_0 r_1', positive=True)

# General homogeneous solutions
y1 = r**2
y2 = r**(-4)
W = y1.diff(r) * y2 - y2.diff(r) * y1  # Should be -6r^{-3}
W_simplified = sp.simplify(W)

# Particular solution for source S = δ (constant):
# u_p = -y1(r) ∫[r₀..r] y2(s) δ / W(s) ds + y2(r) ∫[r₀..r] y1(s) δ / W(s) ds
#
# ∫ y2 δ / W ds = ∫ s⁻⁴ δ / (-6s⁻³) ds = ∫ -δ/(6s) ds = -(δ/6) log(s)
# ∫ y1 δ / W ds = ∫ s² δ / (-6s⁻³) ds = ∫ -δ s⁵/6 ds = -δ s⁶/36

# So u_p(r) = -r² × [-(δ/6)(log r - log r₀)] + r⁻⁴ × [-δ(r⁶ - r₀⁶)/36]
#           = (δ/6) r² (log r - log r₀) - (δ/36) r⁻⁴ (r⁶ - r₀⁶)
#           = (δ/6) r² log(r/r₀) - (δ/36)(r² - r₀⁶ r⁻⁴)

# At r = t^{2/3} (balance), with r₀ in the ALE region:
# The RESONANT term: (δ/6) r² log(r/r₀)
# The REGULAR term: -(δ/36)(r² - r₀⁶ r⁻⁴)

# The resonant piece at the balance radius:
# (δ/6) t^{4/3} log(t^{2/3}/r₀)
# If r₀ ~ t^{1/2} (ALE scale): log ratio ~ (2/3 - 1/2) log(1/t) = (1/6) log(1/t)

resonance = {
    "radial_ODE": "f'' + 3f'/r - 8f/r² = δ  (l=2 sector, constant source)",
    "wronskian_check": f"W(y₁=r², y₂=r⁻⁴) = {W_simplified}",
    "particular_solution": "(δ/6) r² log(r/r₀) - (δ/36)(r² - r₀⁶ r⁻⁴)",
    "resonant_term": "(δ/6) r² log(r/r₀)",
    "resonance_type": "logarithmic (rate r⁰ source resonates with r² homogeneous mode)",
}

# Wronskian contamination from resonance:
# The correction to the r² coefficient is ~ (δ/6) log(r/r₀).
# This enters the Wronskian integral as:
#   ∫ Ric_e^{(2)}(correction, t⁴ H⁴)(X, ∂_r) dv
#   ~ (δ/6) log(r/r₀) × t⁴ × (angular integral) × R⁰
# Relative to signal t⁴:
#   relative_error ~ (C δ) log(r/r₀)

# For r = t^{2/3}, r₀ = t^{1/2}:
# log(r/r₀) = log(t^{1/6}) = (1/6) log(1/t)  [diverges as t→0]

# For r = t^{2/3}, r₀ = 0 (full integration):
# The integral ∫₀^{t^{2/3}} δ/(6s) ds diverges! So the log is necessary.

resonance["balance_evaluation"] = {
    "balance_radius": "r = t^{2/3}",
    "ALE_scale": "r₀ ~ t^{1/2} (Ozuch: √t ≪ r ≪ 1)",
    "log_ratio": "(1/6) log(1/t)",
    "resonant_piece_size": "(δ/36) t^{4/3} log(1/t)",
    "signal_size": "t⁴",
    "relative_error": "(C·δ) log(1/t) [DIVERGES if δ fixed, t→0]",
    "consequence": (
        "If δ and t go to zero independently, the resonance gives relative "
        "error δ log(1/t), which is NOT automatically small. The A2 bridge "
        "carries the hypothesis δ log(1/t) → 0 UNLESS the Bianchi constraint "
        "removes the resonant l=2 source component."
    ),
}

# ============================================================
# 6. Bianchi constraint analysis
# ============================================================
# The source is E = Ric_g - Λg, satisfying div_g E = 0 (contracted Bianchi).
# In the linearized regime: div_e E ≈ 0.
#
# A divergence-free symmetric 2-tensor on R⁴ of size δ in the l=2 sector:
# must have radial dependence S₂(r) satisfying the constraint
#   (S₂' + connection terms) × (angular constraint) = 0
#
# For a TT tensor harmonic T₂ of degree 2 on S³:
# div_e(S₂(r) T₂(σ))_r = S₂'(r) · (something) = 0 ??
#
# Actually, for a pure TT tensor: div_{S³} T₂ = 0 and tr T₂ = 0.
# On the cone dr² + r²g_{S³}, the divergence of h = S(r) T(σ) has
# radial component involving S' and angular component involving S/r.
# The exact formula for TT tensor h of degree l is:
#   div h = [S' + (d-1)S/r - (l+2)(l-1)S/(r·l)] (something)
# This does NOT force S(r) = 0 or have a special rate.
#
# More specifically: for a general divergence-free h = S(r) T(σ) on R⁴
# with T being l=2 TT on S³:
# The divergence constraint gives a FIRST-ORDER ODE for S(r), whose
# general solution is S(r) ~ r^{-p} for some specific p.
# If p > 0, the source S₂(r) decays as r→∞ and the constant (r⁰)
# component is killed.
# If p = 0, the constant source survives and the resonance is real.

bianchi = {
    "constraint": "div_g(Ric_g - Λg) = 0, linearized: div_e E ≈ 0",
    "question": (
        "Does the divergence-free constraint on the l=2 projection of E "
        "remove the constant (r⁰) radial component, thereby killing the "
        "logarithmic resonance?"
    ),
    "preliminary_analysis": (
        "For a TT tensor T₂ of degree 2 on S³, div_e(S(r)T₂) = 0 on R⁴ "
        "imposes S' + (3/r)S - c/r S = 0 for some constant c depending on "
        "the tensor type. If c = 3, solution is S = const (resonance survives). "
        "If c ≠ 3, S ~ r^{c-3} and the constant source is killed."
    ),
    "load_bearing_status": (
        "If Bianchi removes the resonance: A2 bridge is rate-free (relative "
        "error O(δ), no log correction). If not: A2 carries the additional "
        "hypothesis δ_i log(1/t_i) → 0, which is a rate condition on the "
        "pinching-to-bubble-scale coupling."
    ),
    "next_computation": (
        "Explicit divergence of S(r) × (θ_l⁻ ∘ ω_k⁺) on R⁴ in polar "
        "coordinates, to determine the exact constraint on S(r)."
    ),
}
results["resonance"] = resonance
results["bianchi_constraint"] = bianchi

# ============================================================
# 7. Explicit divergence calculation for θ₁⁻ ∘ ω₁⁺ / r⁴
# ============================================================
# The tensor θ₁⁻ ∘ ω₁⁺ is a specific l=2 tensor harmonic on S³.
# It has the form (in Cartesian coordinates x₁,...,x₄):
#
#   T_{ij} = (symmetric traceless part of)
#     (dx¹∧dx² - dx³∧dx⁴)(r dr∧α₁ + r²α₂∧α₃)
#
# where α_i are left-invariant 1-forms on S³.
#
# In Cartesian: θ₁⁻ involves x^T(ω₁⁺∘ω_j⁻)x/|x|² types.
# From Ozuch eq (3.1.): θ₁⁻(x) = Σ_j x^T(ω₁⁺ ∘ ω_j⁻)x/|x|² · ω_j⁻
# And θ₁⁻ ∘ ω₁⁺ is the symmetric product.
#
# The key check: does div_e(f(r) θ₁⁻ ∘ ω₁⁺ / r⁴) vanish for
# f(r) ~ r^α for specific α?
#
# Since H⁴ = θ₁⁻ ∘ ω₁⁺ / (2r⁴) satisfies Ric_e^{(1)}(H⁴) ≈ 0
# at leading order (it's the linearized EH mode), and the
# Bianchi gauge condition B_e(H₂) = δ_e H₂ + (1/2)d(tr H₂) = 0
# is a separate condition, the source E has:
#   div_e E = 0
# which constrains the l=2 component.
#
# For the specific Ozuch basis, the divergence of r^α T₂ on R⁴
# involves only the radial equation since the angular part is TT.
# The cone Laplacian decomposes, and the Bianchi identity becomes
# a first-order radial constraint.
#
# Result: for a GENERAL approximately divergence-free source with
# |E| ≤ δ, the l=2 projection need not be exactly divergence-free
# — it can have a divergence of size O(δ/r). The constraint only
# says that the TOTAL divergence (summed over all l) vanishes.
# Each individual l-component can have nonzero divergence, with
# cancellation between components.

results["bianchi_refinement"] = {
    "critical_point": (
        "The Bianchi constraint div_g E = 0 applies to the TOTAL error, "
        "not to each l-component separately. The l=2 projection of E "
        "need not itself be divergence-free. Therefore the resonance "
        "CANNOT be removed by the Bianchi identity alone."
    ),
    "rate_hypothesis": (
        "Route A therefore carries the hypothesis δ_i log(1/t_i) → 0. "
        "In many geometric sequences, t ~ δ^{α} for some α > 0, so "
        "log(1/t) ~ α log(1/δ) and δ log(1/t) ~ αδ log(1/δ) → 0. "
        "But an a priori statement needs either a rate relation or "
        "a structural improvement (e.g., L²-projection killing the "
        "resonant source)."
    ),
    "alternative_escape": (
        "If the noncollapsed sequence has a uniform harmonic-radius lower "
        "bound at scale r, then the metric in harmonic coordinates has "
        "C^{1,α} control, and the l=2 source projection has improved "
        "regularity that may kill the resonance. This connects the "
        "resonance question to the harmonic-radius epsilon lemma."
    ),
}

# ============================================================
# 8. Summary of Route A status after mode-diagonal analysis
# ============================================================
results["route_A_update"] = {
    "mode_diagonality": "CONFIRMED: Wronskian is l-diagonal, l=0 invisible, l=2 IS obstruction",
    "gauge_triviality_l0": "CONFIRMED: l=0 growing mode is pure gauge, l=0 decaying is mass",
    "resonance_found": True,
    "resonance_severity": "MODERATE: δ log(1/t) rate condition, not δ × (power of t)",
    "resolution_paths": [
        "1. Accept δ log(1/t) → 0 as a mild additional hypothesis (covers most geometric sequences)",
        "2. Prove harmonic-radius epsilon lemma → improved l=2 source regularity → resonance killed",
        "3. Show that in the specific EH/orbifold geometry, the l=2 Bianchi constraint IS exact",
    ],
    "A2_bridge_precise_statement": (
        "At r ≈ t^{2/3}, the metric equals e + A₂ r² T₂ + t⁴ B₋₄ r⁻⁴ T₂ + "
        "(l=0 mass/gauge) + (l≥4 subleading) + corrections. The l=2 Wronskian "
        "signal is t⁴ R⁺·v. The relative error is O(δ) + O(δ log(1/t)). "
        "If δ log(1/t) → 0, nonzero R⁺·v forces δ bounded away from zero."
    ),
}

# ============================================================
# 9. A03 retraction correction
# ============================================================
results["A03_correction"] = {
    "message_330_status": "RETRACTED by A03 in messages #332 and #333",
    "reason": (
        "A03 mixed Sobolev embedding conventions: S^2 vs S_cal. The correct "
        "embedding coefficient S_cal = Cr²/√V gives S_cal√(H₂) that is "
        "collapse-independent. The per-manifold conclusion was also false "
        "because Ricci lower bound + total volume does not bound diameter "
        "or fixed-radius ball volume."
    ),
    "corrected_status": (
        "The negative cutoff-flow route remains UNRESOLVED (neither "
        "dimension-uniform nor per-manifold). The genuine open work is "
        "spacetime recurrence with all time factors, defect-drift "
        "summability, and evolving cutoff-jet estimates."
    ),
    "impact_on_A02": (
        "Step 33 §9 assimilation of #330 must be corrected. The per-manifold "
        "conclusion recorded there is invalid."
    ),
}

# Save
import pathlib
out_dir = pathlib.Path("Sessions/S0910A02/workspace/data")
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "step34_indicial_modediag_resonance.json"
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2, default=str)
print(f"Saved to {out_path}")

# Print key results
print("\n=== MODE-DIAGONAL PAIRING TABLE ===")
for entry in pairing_table:
    print(f"  {entry['label']}: signal = {entry['wronskian_signal']}")
print(f"\n=== RESONANCE ===")
print(f"  Type: logarithmic (δ r² log r)")
print(f"  Relative error at balance: O(δ log(1/t))")
print(f"  Bianchi removes it? NO (applies to total, not per-mode)")
print(f"  Rate condition: δ_i log(1/t_i) → 0")
print(f"\n=== A03 RETRACTION ===")
print(f"  #330 retracted in #332/#333. Negative route: UNRESOLVED, not per-manifold.")
