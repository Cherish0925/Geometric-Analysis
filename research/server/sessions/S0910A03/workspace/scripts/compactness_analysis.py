"""
Analyze the compactness chain for near-Einstein sequences.

The question: does two-sided Ricci pinching on a FIXED manifold
give subsequential smooth convergence to an Einstein metric?

Positive branch: YES (Myers + Bishop-Gromov give non-collapsing)
Negative branch: conditional on non-collapsing
"""
import sympy as sp
from sympy import sqrt, pi, Rational, simplify

print("=" * 70)
print("COMPACTNESS ANALYSIS FOR NEAR-EINSTEIN SEQUENCES")
print("=" * 70)

# Positive branch: Ric ≈ +g, normalization Ric ∈ [(1-δ)g, (1+δ)g]
print("\n--- POSITIVE BRANCH ---")
d = sp.Symbol('delta', positive=True)
# Myers diameter bound
diam_bound = pi / sqrt((1-d)/3)
print(f"Myers: diam ≤ π/√((1-δ)/3)")
print(f"  At δ=0.1: diam ≤ {float(diam_bound.subs(d, 0.1)):.3f}")
print(f"  At δ=0:   diam ≤ π√3 = {float(pi*sqrt(3)):.3f}")

# Bishop-Gromov volume comparison (model: round sphere of appropriate radius)
# Vol(S⁴(r)) = 8π²r⁴/3
r_sphere = 1/sqrt((1-d)/3)
vol_upper = 8*pi**2 * r_sphere**4 / 3
print(f"\nBishop-Gromov: Vol ≤ Vol(S⁴(1/√((1-δ)/3))) = 8π²·9/(3(1-δ)²)")
print(f"  = 24π²/(1-δ)²")
print(f"  At δ=0: Vol ≤ 24π² = {float(24*pi**2):.1f}")

# Volume lower bound for unit balls from diameter bound
print(f"\nNon-collapsing: diam ≤ D implies")
print(f"  Vol(B(p,1)) ≥ c(D) · Vol(M)")
print(f"  which is ≥ c(D) · v₀ > 0")
print(f"  Anderson's harmonic radius bound then applies")

# Conclusion for positive branch
print(f"\nPOSITIVE BRANCH CONCLUSION:")
print(f"  δ_i → 0 ⟹ subsequence → C^{{1,α}} limit g∞")
print(f"  Ric∞ = +g∞ (distributional)")
print(f"  DeTurck-Kazdan: g∞ is smooth")
print(f"  ⟹ g∞ is a SMOOTH POSITIVE EINSTEIN METRIC on M")
print(f"  ⟹ Every manifold admitting δ_+ → 0 carries a positive Einstein metric")

# Negative branch: Ric ≈ -g
print("\n\n--- NEGATIVE BRANCH ---")
print("Ric ∈ [-(1+δ)g, -(1-δ)g]")
print("NO Myers theorem (negative Ricci)")
print("Diameter not automatically bounded")
print("")
print("Available controls:")
print("  1. |Ric| ≤ 1+δ ≤ 2 (uniform Ricci bound)")
print("  2. Vol(M) → 32π²A/9 > 0 (from CGB + Weyl profile)")
print("  3. |Φ|² ≤ |s| ≤ 4+4δ (SW maximum principle)")
print("  4. ∫|Φ|⁴ ≥ 32π²A (integral lower bound)")
print("  5. ∫(|W+|-1/(2√6))² = O(Aδ²) (Weyl profile)")

# Anderson compactness requirement
print("\nAnderson compactness requires:")
print("  |Ric| ≤ Λ + Vol(B(p,1)) ≥ v > 0 for ALL p")
print("  The second condition IS non-collapsing")

# The SW-based argument
print("\n--- SW MAXIMUM PRINCIPLE ARGUMENT ---")
print("If non-collapsing holds:")
print("  (a) Anderson ⟹ g_i → g∞ in C^{1,α} on M")
print("  (b) Ric_i → -g∞ in L^∞ ⟹ Ric∞ = -g∞ distributional")
print("  (c) DeTurck-Kazdan ⟹ g∞ smooth")
print("  (d) SW equations with C^{1,α} metric: Φ_i → Φ∞ in C^{2,α}")
print("  (e) Weitzenböck: |Φ∞|² satisfies (-Δ + c(x))u = f ≥ 0")
print("     with c(x) = 2 - u/2 ≥ 0 (since u ≤ 4)")
print("  (f) Strong maximum principle: u > 0 everywhere (since ∫u² > 0)")
print("  (g) ω∞ = √2 σ(Φ∞)/|σ(Φ∞)| is a smooth symplectic form")
print("  BUT: g∞ is Einstein on M, contradicting Theorem 7!")

# The non-collapsing question
print("\n--- THE KEY OPEN QUESTION ---")
print("Does |Ric| ≤ Λ + Vol(M) ≥ V₀ on a FIXED closed manifold")
print("imply non-collapsing Vol(B(p,1)) ≥ v₀ for all p?")
print("")
print("KNOWN:")
print("  - If diam ≤ D (bounded): YES (covering argument)")
print("  - For positive Ricci: diam bounded by Myers, so YES")
print("  - For negative Ricci: diam not bounded in general")
print("  - On a FIXED manifold: topology constrains diameter growth")
print("  - Under bounded |Rm|: Cheeger-Fukaya-Gromov applies")
print("  - Under bounded |Ric| only: Cheeger-Colding-Naber theory")

# Conditional theorem
print("\n--- CONDITIONAL THEOREM ---")
print("Theorem (conditional on non-collapsing):")
print("  For M in the Ishida-LeBrun family with D ≥ A/3,")
print("  inf_g ||g^{-1}(Ric_g + g)||_∞ > 0.")
print("  That is: M does not admit arbitrarily tight negative Ricci pinching.")
print("")
print("Proof: By contradiction, assume δ_i → 0.")
print("  Under non-collapsing: Anderson + DeTurck-Kazdan give")
print("  smooth limit g∞ with Ric = -g, i.e., Einstein.")
print("  But Theorem 7 says no Einstein metric exists. □")

# What non-collapsing would prove
print("\n--- IMPLICATIONS ---")
print("If non-collapsing is established:")
print("  1. Fixed Ishida-LeBrun families have δ_- > 0")
print("  2. Combined with D > A/3 families: δ_- ≥ δ₀(D/A - 1/3)")
print("  3. ALL Ishida-LeBrun no-Einstein 4-manifolds: δ_- > 0")
print("  4. Positive branch: δ_+ > 0 (from compactness + existence)")
print("  5. Together: consistent with Q₄ TRUE")

print("\n\nANALYSIS COMPLETE")
