"""
Step 46: Annulus window and selection analysis for the mode-projection bridge.

In manifold coordinates r near a singularity at p, with bubble scale t:
- Growing mode: f₁(r) = r²  (carries orbifold curvature ∝ R(p))
- Decaying mode: f₂(r) = r⁻⁴ (carries ALE coefficient ∝ t⁴)
- Signal for the ALE coefficient: the Wronskian value 6|α₋| = 6t⁴ (constant)

Sources of error in the Wronskian integral on annulus [R, 2R]:
1. C⁰ Ricci defect: |Ric - Λg| ≤ δ → source |S| ≤ Cδ
   Using test f₁ = r²: ∫_R^{2R} |S| r² r³ dr ≤ Cδ R⁶
   
2. Quadratic remainder from linearization: |h|² r⁴ where
   h = g - g_cone, |h| ~ max(α₊r², α₋t⁴r⁻⁴)
   In the overlap regime t ≪ r ≪ 1:
   - Orbifold part: |h|_orb ~ r² (from curvature of limit)
   - ALE part: |h|_ALE ~ t⁴r⁻⁴
   Combined: |h|² ~ max(r⁴, t⁸r⁻⁸)
   Quadratic source ~ |h|²r⁴ ~ max(r⁸, t⁸r⁻⁴)

3. Λ-source (from cosmological constant in bubble frame):
   |Λt²| per unit volume → source ~ Λt² in the ODE, contributing ∫ Λt² r⁵ dr ~ Λt²R⁶
   
The Wronskian pairing with f₁ = r² extracts the r⁻⁴ coefficient.
Signal: 6t⁴
Errors: (a) Cδ R⁶, (b) max(R⁸, t⁸R⁻⁴)·R, (c) CΛt²R⁶

For the errors to be ≪ signal:
(a) δ R⁶ ≪ t⁴ → R ≪ (t⁴/δ)^{1/6} = t^{2/3} δ^{-1/6}
(b.i) R⁹ ≪ t⁴ → R ≪ t^{4/9}    [orbifold quadratic]
(b.ii) t⁸R⁻³ ≪ t⁴ → R ≫ t^{4/3}  [ALE quadratic, always satisfied for R ≫ t]
(c) t²R⁶ ≪ t⁴ → R ≪ t^{1/3}     [Λ-source]

Wait, let me be more careful. The Wronskian integral for extracting α₋ uses test f₁ = r²:

∫_R^{2R} S_total(r) · r² · r³ dr

where S_total includes Ricci defect, quadratic, and Λ-source.

But actually, the correct signal/noise is:
- The Wronskian boundary evaluation gives -6α₋ + error
- The error is ∫ S_total · r⁵ dr

Hmm, re-reading the strategist more carefully:
"With a test field growing like r², the C⁰ Ricci defect contributes about δr⁶ 
 against a signal t⁴"

This means: the integral ∫ δ·r⁵ dr ~ δR⁶/6 on [R,2R], compared to signal 6t⁴.
So for relative error < 1: R < (36t⁴/δ)^{1/6} ~ t^{2/3}δ^{-1/6}.

"the quadratic remainder about |h|²r⁴ with |h| ~ max(r², t⁴r⁻⁴)"
Integral: ∫ max(r⁴, t⁸r⁻⁸)·r⁴·r⁻¹ dr... 

Actually I think the source in the ODE is not ∫... the source S(r) in
a'' + 3/r a' - 8/r² a = S(r)
has contributions from:
- Ricci defect: |S_Ric| ≤ Cδ
- Quadratic: |S_quad| ≤ C|h|²/r² (from the nonlinearity of Ricci)
- Λ-source: |S_Λ| ≤ CΛt² (in bubble frame, becomes CΛ after transform)

The Wronskian integral uses Green's function. For extracting α₋ (r⁻⁴ coeff),
we pair with f₁ = r², giving:

error ~ (1/6) ∫_R^{2R} S(s) · s⁵ ds

Let me compute all three bounds.
"""

import numpy as np
import json

def compute_window(delta, t, Lambda=1.0):
    """Compute the usable annulus window for mode projection."""
    
    # Lower bound: must be above bubble scale
    r_low = t
    
    # Upper bounds from each error source:
    # (a) Ricci defect: δ R⁶ ≪ t⁴ → R ≪ (t⁴/δ)^{1/6}
    r_ricci = (t**4 / max(delta, 1e-30))**(1./6)
    
    # (b) Quadratic orbifold: |h|~r², source ~ r⁴/r² = r², integral ~ r⁸
    # ∫ r² · r⁵ dr / r⁶ ~ R⁸ ≪ t⁴ → R ≪ t^{1/2}
    r_quad_orb = t**0.5
    
    # (c) Quadratic ALE: |h|~t⁴r⁻⁴, source ~ t⁸r⁻⁸/r² = t⁸r⁻¹⁰
    # ∫ t⁸r⁻¹⁰ r⁵ dr ~ t⁸ R⁻⁴ / t⁴ → need R ≫ t (always sat)
    r_quad_ALE_lower = t  # always above bubble scale
    
    # (d) Λ-source: Λt² in the ODE source
    # integral: Λt² ∫ r⁵ dr ~ Λt² R⁶ ≪ t⁴ → R ≪ t^{1/3}/Λ^{1/6}
    r_lambda = (t**2 / Lambda)**(1./6) * t**(1./3) if Lambda > 0 else np.inf
    # Actually: Λt²R⁶ ≪ t⁴ → R⁶ ≪ t²/Λ → R ≪ (t²/Λ)^{1/6} = t^{1/3}/Λ^{1/6}
    r_lambda = (t**2 / max(Lambda, 1e-30))**(1./6)
    
    r_upper = min(r_ricci, r_quad_orb, r_lambda)
    
    # Number of dyadic scales
    if r_upper > r_low:
        n_dyadic = np.log2(r_upper / r_low)
    else:
        n_dyadic = 0
    
    # Binding constraint
    if r_upper == r_ricci:
        binding = "Ricci defect"
    elif r_upper == r_quad_orb:
        binding = "quadratic orbifold"
    else:
        binding = "Lambda source"
    
    return {
        "t": t, "delta": delta, "Lambda": Lambda,
        "r_low": r_low,
        "r_ricci": r_ricci,
        "r_quad_orb": r_quad_orb,
        "r_lambda": r_lambda,
        "r_upper": r_upper,
        "binding_constraint": binding,
        "n_dyadic_scales": round(n_dyadic, 2),
        "half_log2_1_over_t": round(0.5 * np.log2(1/t), 2)
    }

# Test cases
results = {"purpose": "Annulus window analysis for mode-projection bridge",
           "mechanism": "The Wronskian is radius-independent; the window gives the range "
                        "where errors are subleading to the t⁴ signal.",
           "cases": []}

# Typical scenarios
for t in [1e-2, 1e-3, 1e-5, 1e-10]:
    for delta in [1e-1, 1e-2, 1e-3, 1e-5]:
        w = compute_window(delta, t)
        results["cases"].append(w)

# Print summary
print("=" * 90)
print("ANNULUS WINDOW ANALYSIS")
print("=" * 90)
print(f"{'t':<12} {'δ':<12} {'r_low':<12} {'r_upper':<14} {'N_dyadic':<12} {'½log₂(1/t)':<12} Binding")
print("-" * 90)

for c in results["cases"]:
    print(f"{c['t']:<12.1e} {c['delta']:<12.1e} {c['r_low']:<12.1e} "
          f"{c['r_upper']:<14.4e} {c['n_dyadic_scales']:<12} "
          f"{c['half_log2_1_over_t']:<12} {c['binding_constraint']}")

# The key insight: for δ = t^a with a > 0, the window has ~½log₂(1/t) scales
# when the quadratic orbifold bound is tighter than the Ricci bound
print("\n" + "=" * 90)
print("KEY: Window has ~½log₂(1/t) dyadic scales when quadratic is binding.")
print("Bridge 1 (Cheeger-Naber weak-type) bounds bad set to Vol ≤ C(εR)⁴,")
print("so fraction ε⁴ of each annulus is controlled. With N ≫ 1 scales,")
print("a selection argument finds good annuli where harmonic gauge exists.")
print("=" * 90)

# Also compute the Cheeger-Naber selection estimate
print("\n--- Cheeger-Naber annulus selection ---")
print("On annulus [R, 2R], weak-type L² estimate gives:")
print("  Vol({r_h ≤ εR} ∩ B_R) ≤ C(v)(εR)⁴")
print("  → fraction of bad set: C(v)ε⁴")
print("  → for ε = 0.01: fraction ≤ C·10⁻⁸")
print("  → for ε = 0.1:  fraction ≤ C·10⁻⁴")
print("With N ~ ½log₂(1/t) available scales, select the one with smallest")
print("bad-set fraction. The harmonic coordinates exist on the good subset.")

output = "Sessions/S0910A02/workspace/data/step46_annulus_window_analysis.json"
with open(output, 'w') as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nSaved to {output}")
