"""
Step 9: Compute explicit constants for the noncollapsed finiteness theorem.
Session: S0910A02. Agent2/Constructor.

Verifies the chain: |Ric-g|_op ≤ δ → Myers diameter → Bishop-Gromov volume ratio
→ Cheeger-Naber Theorem 1.12 hypotheses satisfied.

Also computes the Sha-Yang dichotomy stress test numbers.
"""
import numpy as np
from scipy import integrate
import json

# ============================================================
# 1. Myers diameter bound
# ============================================================
# Ric ≥ (1-δ)g on M^4.  Comparison curvature K = (1-δ)/3.
# Myers: diam ≤ π/√K = π√(3/(1-δ)).

def myers_diam(delta, n=4):
    """Myers diameter bound for Ric ≥ (1-δ)g on n-manifold."""
    K = (1 - delta) / (n - 1)
    return np.pi / np.sqrt(K)

# ============================================================
# 2. Bishop-Gromov volume ratio
# ============================================================
# In n=4, space form of curvature K: V_K(r) = 2π² ∫₀ʳ (sin(√K t)/√K)³ dt
# (for K > 0, using the formula for S⁴ with curvature K)

def volume_ball_space_form(r, K, n=4):
    """Volume of ball of radius r in n-dim space form of curvature K > 0."""
    if r <= 0:
        return 0.0
    max_r = np.pi / np.sqrt(K) if K > 0 else 1e10
    r_eff = min(r, max_r)
    
    # In n-dim space form with sectional curvature K:
    # Vol(B_r) = ω_{n-1} ∫₀ʳ sn_K(t)^{n-1} dt
    # where sn_K(t) = sin(√K t)/√K
    # ω_{n-1} = n-sphere surface area = 2π^{n/2}/Γ(n/2)
    
    sqrtK = np.sqrt(K)
    
    # For n=4: ω_3 = 2π²
    omega_3 = 2 * np.pi**2
    
    def integrand(t):
        if K > 0:
            return (np.sin(sqrtK * t) / sqrtK)**(n-1)
        else:
            return t**(n-1)
    
    result, _ = integrate.quad(integrand, 0, r_eff)
    return omega_3 * result

def bishop_gromov_ratio(delta, n=4):
    """
    Bishop-Gromov ratio V_K(1)/V_K(D) where K = (1-δ)/(n-1), D = Myers diam.
    This gives: Vol(B_1(p)) ≥ Vol(M) × ratio for all p.
    """
    K = (1 - delta) / (n - 1)
    D = myers_diam(delta, n)
    V1 = volume_ball_space_form(1.0, K, n)
    VD = volume_ball_space_form(D, K, n)
    return V1 / VD

# ============================================================
# 3. Compute for various δ
# ============================================================
results = {
    "theorem_A_constants": [],
    "sha_yang_dichotomy": [],
    "upper_ricci_role": {}
}

print("=" * 70)
print("THEOREM A: Noncollapsed Positive Finiteness Constants (dim 4)")
print("=" * 70)
print(f"{'δ':>8} {'diam':>10} {'|Ric|':>8} {'BG ratio':>12} {'v_min(B1)':>12}")
print("-" * 60)

for delta in [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.49]:
    D = myers_diam(delta)
    ric_bound = 1 + delta
    bg = bishop_gromov_ratio(delta)
    
    print(f"{delta:8.2f} {D:10.4f} {ric_bound:8.3f} {bg:12.8f} {bg:12.8f}*v")
    
    results["theorem_A_constants"].append({
        "delta": delta,
        "myers_diam": float(D),
        "ric_upper": float(ric_bound),
        "ric_satisfies_CN": ric_bound <= 3.0,
        "bishop_gromov_ratio": float(bg),
        "vol_B1_lower": f"{bg:.8f} * Vol(M)",
        "CN_1_12_hypotheses": {
            "|Ric| ≤ 3": ric_bound <= 3.0,
            "Vol(B1) > v'": True,
            "diam ≤ D": True
        }
    })

# ============================================================
# 4. Sha-Yang dichotomy stress test
# ============================================================
print("\n" + "=" * 70)
print("SHA-YANG DICHOTOMY: #_k(S²×S²) stress test")
print("=" * 70)
print("For each k, if δ_+(M_k) ≤ δ and Vol ≥ v, then b₂ = 2k ≤ B(δ,v)")
print(f"{'k':>6} {'χ':>6} {'Weyl_lower/π²':>16} {'Vol_upper/π²':>14} {'mean_W²':>12}")
print("-" * 60)

for k in [1, 2, 5, 10, 50, 100, 500]:
    chi = 2 + 2*k
    delta = 0.1  # representative tight pinching
    
    # Weyl lower bound: ∫|W|² ≥ 8π²[χ - 2((1+δ)/(1-δ))²]
    ratio_sq = ((1 + delta)/(1 - delta))**2
    weyl_lower = 8 * (chi - 2 * ratio_sq)  # in units of π²
    
    # Vol upper bound: Vol ≤ 24π²/(1-δ)² (Bishop, n=4, Ric ≥ (1-δ)g for round sphere scaling)
    # More precisely, Vol ≤ V_K(D) where K = (1-δ)/3
    K = (1 - delta)/3
    vol_upper = volume_ball_space_form(myers_diam(delta), K) / np.pi**2
    
    # Mean |W|² if Vol = vol_upper (upper bound on vol gives lower bound on mean)
    mean_W2 = weyl_lower / vol_upper if vol_upper > 0 else float('inf')
    
    print(f"{k:6d} {chi:6d} {weyl_lower:16.2f} {vol_upper:14.2f} {mean_W2:12.4f}")
    
    results["sha_yang_dichotomy"].append({
        "k": k,
        "chi": chi,
        "b2": 2*k,
        "delta": delta,
        "weyl_lower_over_pi2": float(weyl_lower),
        "vol_upper_over_pi2": float(vol_upper),
        "mean_W2": float(mean_W2),
        "ALE_bubbles_needed_lower": max(1, int(weyl_lower * np.pi**2 / (12 * np.pi**2))),
        "note": "ALE bubble energy ≥ 8π²/|Γ|; EH gives 12π²"
    })

# ============================================================
# 5. Role of upper Ricci bound
# ============================================================
print("\n" + "=" * 70)
print("UPPER RICCI BOUND: WHY IT'S LOAD-BEARING")
print("=" * 70)
print("Sha-Yang: Ric > 0 on #_k(S²×S²) for ALL k ≥ 1")
print("  → One-sided Ric ≥ c > 0 allows b₂ → ∞")
print("Cheeger-Naber Thm 1.12: |Ric| ≤ 3 + noncollapse + diam ≤ D")  
print("  → At most C(v,D) diffeomorphism types → b₂ bounded")
print("Key: the UPPER bound is what upgrades codim-2 regularity (Cheeger-Colding)")
print("     to codim-4 regularity (Cheeger-Naber Theorem 1.4)")
print("     and enables the bubble-tree decomposition (Theorem 8.64).")

results["upper_ricci_role"] = {
    "one_sided_lower": {
        "Sha_Yang_family": "#_k(S²×S²), all k ≥ 1",
        "admits_Ric_positive": True,
        "b2_unbounded": True,
        "finiteness": False,
        "reason": "Cheeger-Colding gives only codim-2 regularity with lower Ricci"
    },
    "two_sided_CN": {
        "hypothesis": "|Ric| ≤ 3, Vol(B₁) > v, diam ≤ D",
        "conclusion": "finite diffeomorphism types",
        "key_upgrade": "codim-4 regularity (Theorem 1.4) → bubble tree → finiteness",
        "Einstein_required": False
    }
}

# ============================================================
# 6. Blow-up Ricci scaling
# ============================================================
print("\n" + "=" * 70)
print("BLOW-UP RICCI SCALING")
print("=" * 70)
print("At bubble scale t: ĝ = t⁻²g, Ric_ĝ = t² Ric_g")
print("So |Ric_ĝ|_ĝ = t²|Ric_g|_g ≤ t²(1+δ)")
print("As t → 0: blow-up is Ricci-flat with defect O(t²), INDEPENDENT of δ")
print("The Einstein constant scales away at bubble scale.")
print("This is why the obstruction-amplitude principle can work:")
print("  at bubble scale, the equation is as clean as exact-Einstein theory.")

for t in [0.1, 0.01, 0.001]:
    for delta in [0.01, 0.1, 0.3]:
        ric_defect = t**2 * (1 + delta)
        print(f"  t={t:.3f}, δ={delta:.2f}: |Ric_ĝ| ≤ {ric_defect:.6f}")

# ============================================================
# 7. Annular convergence parameters from §8.2
# ============================================================
print("\n" + "=" * 70)
print("§8.2 ANNULAR CONVERGENCE: BRIDGE INPUTS")
print("=" * 70)
print("Theorem 8.6: for |Ric| ≤ 3δ, Vol(B₁) > v, almost-constant volume ratio:")
print("  (1) r_h(x) > r₀(v)·ε for x ∈ A_{ε,2}(p)")  
print("  (2) Annular diffeomorphism Φ: A_{ε,2}(0) → U with")
print("      ||g_ij - δ_ij||_C⁰ + ||∂_k g_ij||_C⁰ < ε")
print("  where 0 ∈ R⁴/Γ, |Γ| ≤ N(v)")
print("\nFor projection bridge: test field φ₀ on R⁴/Γ, cutoff to M")
print("  ||φ_j||_{L¹(g_i)} = O(t_j)")
print("  C⁰ Ricci pinching gives: |∫⟨Ric-g, φ_j⟩| ≤ δ_i · O(t_j)")
print("  Bridge identity: ∫ = t_j · Obstruction + o(t_j)")
print("  → Obstruction = O(δ_i) + o(1) → 0")

# Save results
output_path = "Sessions/S0910A02/workspace/data/step9_finiteness_constants.json"
with open(output_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {output_path}")
