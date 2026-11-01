#!/usr/bin/env python3
"""
Verify the Weitzenböck gradient energy for harmonic self-dual 2-forms
on an Einstein 4-manifold.

KEY FORMULA: For a harmonic self-dual 2-form H on (M^4, g) with Ric = (s/4)g:
    ∫|∇H|² = (2λ_W - s/3) ∫|H|²
where λ_W is the W+ eigenvalue of H.

DERIVATION:
  The Bochner-Weitzenböck formula for 2-forms is:
    Δ_d ω = ∇*∇ω + q(R)(ω)
  
  For Einstein 4-manifolds, the curvature endomorphism q(R) on Λ²₊ is:
    q(R)|_{Λ²₊} = s/3 · Id - 2W⁺
  
  (The s/2 from Ric terms minus s/6 from the curvature operator diagonal gives s/3.)
  
  For harmonic H (Δ_d H = 0):
    ∇*∇H = -(s/3)H + 2W⁺(H) = (2W⁺ - s/3)H
  
  Integrating:
    ∫|∇H|² = ∫⟨∇*∇H, H⟩ = (2λ_W - s/3) ∫|H|²
"""

from sympy import *

print("=" * 70)
print("WEITZENBÖCK GRADIENT ENERGY FOR SELF-DUAL 2-FORMS")
print("=" * 70)

# ============================================================
# 1. Verify the formula at the calibrated spectrum
# ============================================================
print("\n1. CALIBRATED SPECTRUM (s = -4, Spec(W+) = (-1/6, 1/12, 1/12))")
print("-" * 60)

s = Rational(-4, 1)  # scalar curvature for Ric = -g in dim 4

# W+ eigenvalues at the calibrated point
lam_simple = Rational(-1, 6)   # simple eigenvalue
lam_double = Rational(1, 12)   # double eigenvalue

# Check trace-free condition
assert lam_simple + 2 * lam_double == 0, "W+ must be trace-free"

# Check |W+|² = 1/24
W_sq = lam_simple**2 + 2 * lam_double**2
print(f"  |W+|² = {lam_simple}² + 2·{lam_double}² = {W_sq}")
assert W_sq == Rational(1, 24)

# Gradient energy coefficient: c = 2λ_W - s/3
c_simple = 2 * lam_simple - s / 3
c_double = 2 * lam_double - s / 3

print(f"\n  Simple eigenvalue λ = {lam_simple}:")
print(f"    2λ - s/3 = 2·({lam_simple}) - ({s})/3 = {c_simple}")
print(f"    ∫|∇H|² = {c_simple} · ∫|H|²")

print(f"\n  Double eigenvalue λ = {lam_double}:")
print(f"    2λ - s/3 = 2·({lam_double}) - ({s})/3 = {c_double}")
print(f"    ∫|∇H|² = {c_double} · ∫|H|²")

# Both must be positive for the identity to be consistent
assert c_simple > 0, "Gradient energy coefficient must be positive"
assert c_double > 0, "Gradient energy coefficient must be positive"

print(f"\n  Both coefficients positive: forms NOT nearly parallel ✓")
print(f"  Gradient energy ~ amplitude energy: c_simple = {c_simple} = {float(c_simple):.4f}")
print(f"                                       c_double = {c_double} = {float(c_double):.4f}")

# ============================================================
# 2. Verify against known models
# ============================================================
print("\n\n2. KNOWN MODEL VERIFICATION")
print("-" * 60)

# Round S⁴: s = 12, W+ = 0, b₂⁺ = 0
print("\n  Round S⁴ (s = 12, W+ = 0, b₂⁺ = 0):")
s_S4 = 12
c_S4 = 2 * 0 - s_S4 / 3
print(f"    c = 2·0 - 12/3 = {c_S4}")
print(f"    c < 0 → no harmonic SD forms can exist → consistent with b₂⁺ = 0 ✓")

# K3 surface: s = 0, W+ = 0, b₂⁺ = 3
print("\n  K3 surface (s = 0, W+ = 0, b₂⁺ = 3):")
s_K3 = 0
c_K3 = 2 * 0 - s_K3 / 3
print(f"    c = 2·0 - 0/3 = {c_K3}")
print(f"    c = 0 → harmonic SD forms are parallel ✓ (Calabi-Yau holonomy)")

# Negative KE surface: s = -4, W+ spectrum = (-1/3, 1/6, 1/6)
print("\n  Negative KE surface (s = -4, Spec(W+) = (-1/3, 1/6, 1/6)):")
s_KE = Rational(-4, 1)
lam_KE_simple = Rational(-1, 3)
lam_KE_double = Rational(1, 6)
assert lam_KE_simple + 2 * lam_KE_double == 0

c_KE_simple = 2 * lam_KE_simple - s_KE / 3
c_KE_double = 2 * lam_KE_double - s_KE / 3
W_sq_KE = lam_KE_simple**2 + 2 * lam_KE_double**2
print(f"    |W+|² = {W_sq_KE} (= s²/24 = 16/24 = 2/3)")
print(f"    c_simple = {c_KE_simple} = {float(c_KE_simple):.4f}")
print(f"    c_double = {c_KE_double} = {float(c_KE_double):.4f}")
print(f"    KE Kähler form ω is in the simple eigenspace:")
print(f"    ∫|∇ω|² = {c_KE_simple} · ∫|ω|²")
print(f"    But ∇ω = 0 for Kähler form → consistent only if")
print(f"    the Kähler form is harmonic AND parallel")
print(f"    Actually: the Kähler form IS parallel on KE,")
print(f"    so ∫|∇ω|² = 0 and the Weitzenböck identity")
print(f"    becomes 0 = {c_KE_simple} · ∫|ω|² which requires ω = 0.")
print(f"    RESOLUTION: ω is NOT harmonic on a non-Ricci-flat KE surface!")
print(f"    For Kähler, ω is parallel hence harmonic (Δ_d ω = 0);")
print(f"    but KE with s ≠ 0: ω is parallel → harmonic →")
print(f"    Weitzenböck gives c > 0 only if ω = 0... contradiction?")
print(f"    No: for negative KE, b₂⁺ = 1 (only ω/|ω| × volume)")
print(f"    and d*ω = 0, dω = 0, so ω IS harmonic.")
print(f"    Then ∫|∇ω|² = {c_KE_simple}∫|ω|² AND ∇ω = 0")
print(f"    → This means {c_KE_simple} must be 0. But it's {c_KE_simple} ≠ 0!")

# This reveals a subtlety!
print(f"\n  RESOLUTION OF APPARENT PARADOX:")
print(f"  The formula q(R)|_{{Λ²₊}} = s/3·Id - 2W⁺ is for GENERAL 2-forms.")
print(f"  For EINSTEIN metrics, Ric = (s/n)g = (s/4)g in dim 4.")
print(f"  The actual endomorphism is:")
print(f"    q(R)(ω)_ab = R_a^c ω_cb + R_b^c ω_ac - 2R_acbd ω^cd")
print(f"  For Einstein: first two terms give (s/4)(ω+ω) = (s/2)ω")
print(f"  The curvature operator on Λ²₊: R̂|_{{Λ²₊}} = W⁺ + s/12·Id")
print(f"  So -2R̂(ω) = -2(W⁺ + s/12)ω")
print(f"  Total: q(R)(ω) = (s/2)ω - 2W⁺(ω) - (s/6)ω = (s/3)ω - 2W⁺(ω)")

print(f"\n  For KE Kähler form ω with W⁺(ω) = (-1/3)ω:")
print(f"    q(R)(ω) = ({s_KE}/3 - 2·({lam_KE_simple}))ω")
print(f"            = ({s_KE/3} + {-2*lam_KE_simple})ω = {s_KE/3 - 2*lam_KE_simple}ω")
qR_KE = s_KE/3 - 2*lam_KE_simple
print(f"    = {qR_KE}ω")
print(f"  So ∇*∇ω = -q(R)(ω) = {-qR_KE}ω")
print(f"  ∫|∇ω|² = {-qR_KE}∫|ω|² > 0!")
print(f"  But ω is parallel (∇ω = 0), so ∫|∇ω|² = 0.")
print(f"  CONTRADICTION → our formula derivation has an error!")

# ============================================================
# 3. Careful re-derivation
# ============================================================
print("\n\n3. CAREFUL RE-DERIVATION FROM FIRST PRINCIPLES")
print("-" * 60)

print("""
  The issue is in q(R). For a 2-form on a 4-manifold, the
  Bochner-Weitzenböck formula involves the FULL curvature action,
  not just Λ²₊ → Λ²₊. The curvature endomorphism on ALL 2-forms is:

    q(R)(ω)_ij = R_i^c ω_cj + R_j^c ω_ic - 2 R_{icjd} ω^{cd}

  For an Einstein metric with Ric = (s/4)g (n=4):
    R_i^c ω_cj + R_j^c ω_ic = (s/4)(ω_ij + ω_ij) = (s/2)ω_ij

  The last term -2R_{icjd}ω^{cd}: we need the FULL curvature operator,
  NOT just the Λ²₊ block. In 4D, the curvature operator on Λ² is:

    R̂ = ( W⁺ + s/12    B  )
         ( B^T      W⁻ + s/12 )

  where B involves traceless Ricci. For Einstein, B = 0 and:

    -2R̂(ω) for ω ∈ Λ²₊: -2(W⁺ + s/12)(ω)

  So q(R)(ω) = (s/2)ω - 2(W⁺ + s/12)(ω) = (s/2 - s/6)ω - 2W⁺(ω)
             = (s/3)ω - 2W⁺(ω)

  For KE with ω parallel: ∇*∇ω = 0, and Δ_d ω = 0, so:
    0 = 0 + q(R)(ω) = (s/3 - 2λ_W)ω
  → s/3 = 2λ_W
  → λ_W = s/6

  For s = -4: λ_W = -2/3.
  But for negative KE, W⁺(ω) = (-1/3)ω, so λ_W = -1/3 ≠ -2/3.

  THERE IS STILL AN INCONSISTENCY. The Kähler form of a negative KE
  surface IS parallel AND harmonic. The Weitzenböck identity should
  give 0 = 0 + q(R)(ω), so we need q(R)(ω) = 0.
""")

# Let me check the correct curvature action more carefully
print("  CHECKING: What is W⁺(ω) for a Kähler-Einstein surface?")
print("  For a Kähler surface with Kähler form ω:")
print("    W⁺ has simple eigenvalue on ω and double on ω⊥ ∩ Λ²₊")
print("    The eigenvalue of ω is: (s/12) (for n=4)")
print("    NOT -s/6 or -1/3!")
print()
print("  CORRECTION: There are different normalizations of 'W⁺ eigenvalue'")
print("  in the literature. The curvature operator eigenvalue on Λ²₊ is:")
print("    W⁺ + s/12")
print("  For a Kähler surface, the eigenvalue of the CURVATURE OPERATOR")
print("  on ω is s/6 (for the round CP²). The W⁺ eigenvalue is s/6 - s/12 = s/12.")
print()

# For Kähler-Einstein with Ric = λg:
# s = 4λ in dim 4
# The curvature operator on the Kähler form ω:
# Rm(ω, ·, ω, ·) = λ in the relevant directions
# The eigenvalue of R̂ on ω is: s/6 (this is a known result)
# So W⁺ eigenvalue on ω is: s/6 - s/12 = s/12

lam_true = s_KE / 12
print(f"  For negative KE (s = -4):")
print(f"    W⁺ eigenvalue on ω = s/12 = {lam_true}")
print(f"    q(R)(ω) = (s/3 - 2·s/12)ω = (s/3 - s/6)ω = (s/6)ω")
qR_check = s_KE / 6
print(f"    q(R)(ω) = ({qR_check})ω")
print(f"    For harmonic parallel ω: 0 = q(R)(ω) requires q(R)(ω) = 0")
print(f"    But q(R)(ω) = ({qR_check})ω ≠ 0!")
print(f"\n  THE KÄHLER FORM IS NOT IN THE STANDARD W⁺ EIGENSPACE!")
print(f"  The issue: my normalization of W⁺ eigenvalues is inconsistent")
print(f"  with the Weitzenböck formula. Let me use the self-consistent version.")

# ============================================================
# 4. Self-consistent computation using the curvature operator
# ============================================================
print("\n\n4. SELF-CONSISTENT COMPUTATION")
print("-" * 60)

print("""
  On a 4D Einstein manifold (Ric = λg, s = 4λ):
  The curvature operator R̂ on Λ²₊ has eigenvalues μ₁, μ₂, μ₃
  (the W⁺ eigenvalues PLUS s/12).

  The Weitzenböck formula for self-dual 2-forms is:
    Δ_d H = ∇*∇H + q(R)(H)
  where (for Einstein):
    q(R)(H) = (s/2)H - 2R̂(H) = s/2 H - 2μ_H H
            = (s/2 - 2μ_H) H

  For harmonic H: ∇*∇H = (2μ_H - s/2) H
  ∫|∇H|² = (2μ_H - s/2) ∫|H|²

  For this to be ≥ 0 (existence condition): μ_H ≥ s/4 = λ.

  CHECK: Kähler form on KE:
    R̂(ω) = (s/6)ω, so μ_ω = s/6
    ∫|∇ω|² = (2·s/6 - s/2) ∫|ω|² = (s/3 - s/2) ∫|ω|² = (-s/6) ∫|ω|²
    For s = -4: ∫|∇ω|² = (4/6)∫|ω|² = (2/3)∫|ω|² > 0
    
  But ω is parallel! So ∫|∇ω|² = 0. STILL CONTRADICTS.
  
  The resolution must be that the Kähler form is NOT a standard
  harmonic 2-form in the Hodge sense when the metric is Einstein
  with s ≠ 0...
  
  Actually wait: on a compact Kähler manifold, the Kähler form IS
  always harmonic (dω = 0, d*ω = 0). And on an Einstein manifold
  with Ric = λg, the Kähler form IS parallel (∇ω = 0).
  
  So we need 0 = ∫|∇ω|² = (2μ - s/2)∫|ω|², hence μ = s/4 = λ.
  
  Check: μ_ω = s/6 for KE. We need μ = s/4.
  s/6 ≠ s/4 for s ≠ 0. Contradiction!
  
  The error MUST be in the formula for q(R).
""")

# ============================================================
# 5. Correct derivation using index computation
# ============================================================
print("\n5. DIRECT INDEX COMPUTATION")
print("-" * 60)

print("""
  Let me compute q(R)(ω)_{ij} directly for an Einstein 4-manifold.
  
  q(R)(ω)_{ij} = R_i^c ω_{cj} + R_j^c ω_{ic} - 2 R_{icjd} ω^{cd}
  
  Term 1+2: R_i^c ω_{cj} + R_j^c ω_{ic}
    For Einstein: R_i^c = λ δ_i^c
    So this = λ(ω_{ij} + ω_{ij}) = 2λ ω_{ij}
    
  Term 3: -2 R_{icjd} ω^{cd}
    This is -2 (R̂·ω)_{ij} where R̂ is the curvature operator on Λ².
    BUT: R̂ acts on Λ² and its matrix representation depends on
    the chosen basis and identification of Λ² with a vector space.
    
  The standard identification: ω_{ij} ↔ (ω_{12}, ω_{13}, ω_{14}, ω_{34}, ω_{42}, ω_{23})
  But the curvature operator acts as:
    (R̂·ω)_{ij} = R_{ijkl} ω^{kl} = R_{ijkl} g^{kp} g^{lq} ω_{pq}
    
  Note: (R̂·ω)_{ij} is antisymmetric. And the factor issue:
    R_{icjd} ω^{cd} = (1/2)(R̂·ω)_{ij} or (R̂·ω)_{ij}?
    
  Actually: (R̂·ω)_{ij} = R_{ijcd} ω^{cd} (summing over c,d independently)
  Since R_{ijcd} is antisymmetric in cd: = 2 R_{ij[cd]} ω^{cd} / not quite...
  
  Let me be very explicit. R_{ijkl} ω^{kl} = Σ_{k<l} R_{ijkl} (ω^{kl} - ω^{lk})
  = 2 Σ_{k<l} R_{ijkl} ω^{kl}
  
  But in the Weitzenböck formula the term is:
  -2 R_{icjd} ω^{cd} = -2 Σ_{c,d} R_{icjd} g^{ce} g^{df} ω_{ef}
  = -2 Σ_{c,d} R_{icjd} ω^{cd}
  
  With antisymmetry of ω: = -2 Σ_{c<d} R_{icjd} (ω^{cd} - ω^{dc}) 
  = -4 Σ_{c<d} R_{icjd} ω^{cd}
  
  Hmm, this depends on whether we use the convention R_{icjd} ω^{cd}
  with free sum or restricted sum.
  
  CLEANER APPROACH: use the known result for specific models.
""")

# For a direct check, use the Kähler-Einstein model
# On a KE surface (Ric = λg), the Kähler form ω is parallel.
# The Weitzenböck identity Δ_d ω = ∇*∇ω + q(R)(ω) gives:
# 0 = 0 + q(R)(ω), so q(R)(ω) = 0.

# The Ricci term: 2λω
# The curvature term: must be -2λω to cancel.
# So the curvature operator eigenvalue μ on ω satisfies -2μω = -2λω → μ = λ.

# For Kähler-Einstein: μ_ω = λ = s/4.
# But the USUAL statement says the curvature operator eigenvalue on ω is s/6.
# These can't both be right. The issue is in how -2R_{icjd}ω^{cd} relates to R̂.

# The resolution: -2R_{icjd}ω^{cd} ≠ -2(R̂ω)_{ij} in general.
# Rather: R_{icjd}ω^{cd} = (R̂ω)_{ij} where (R̂ω)_{ij} = R_{ijcd}ω^{cd}
# But R_{icjd} ≠ R_{ijcd} in general! (first Bianchi gives R_{icjd} = R_{ijcd} + R_{idjc})
# No: by symmetries of Rm: R_{icjd} = R_{jdic} = R_{ijcd} only with specific symmetries.

# Actually R_{abcd} = R_{cdab} (pair symmetry), so R_{icjd} = R_{jdic} always.
# And R_{icjd} = -R_{cijd} = -R_{cijt} by antisymmetry in first pair.
# R_{icjd} has no simple relation to R_{ijcd} in general.

# Let me use R_{icjd} ω^{cd} directly:
# = g^{ce} g^{df} R_{iejf} ω_{ef} ... this is getting complicated.
# Let me just use a symbolic computation.

print("\n  SYMBOLIC COMPUTATION of q(R)(ω) for KE 4-manifolds")
print("  Using an explicit orthonormal frame and Kähler-Einstein curvature")

# On a Kähler surface with Kähler form ω = e¹∧e² + e³∧e⁴
# (standard orientation making ω self-dual)
# For Kähler-Einstein with Ric = λg:
# R_{1212} = R_{3434} = λ/2 (the holomorphic sectional curvature times corrections)
# Actually, for a constant-holomorphic-sectional-curvature Kähler surface:
# R_{ijkl} = (λ/2)(g_{ik}g_{jl} - g_{il}g_{jk} + ω_{ik}ω_{jl} - ω_{il}ω_{jk} + 2ω_{ij}ω_{kl})

# Let me just verify the Weitzenböck with the formula:
# ∇*∇H = -q(R)(H) for harmonic H
# and for KE Kähler form: ∇ω = 0 (parallel), so ∇*∇ω = 0, Δ_d ω = 0.
# Therefore q(R)(ω) = 0.
# This DETERMINES: (Ric terms + curvature terms)(ω) = 0.

# For a DIFFERENT self-dual form H ⊥ ω in Λ²₊:
# On a KE surface, H is harmonic iff H is in H²₊ (which has dim = b₂⁺ - 1)
# For a general-type surface, b₂⁺ can be > 1.

# The key result we need: for the CALIBRATED SPECTRUM, NOT the KE spectrum.
# Calibrated: W⁺ eigenvalues are (-1/6, 1/12, 1/12) in the trace-free convention.
# Curvature operator eigenvalues: (-1/6 + s/12, 1/12 + s/12, 1/12 + s/12)
# = (-1/6 - 1/3, 1/12 - 1/3, 1/12 - 1/3) = (-1/2, -1/4, -1/4)

# For KE: W⁺ eigenvalues are (-1/3, 1/6, 1/6) (trace-free convention)
# Curvature operator eigenvalues: (-1/3 - 1/3, 1/6 - 1/3, 1/6 - 1/3)
# = (-2/3, -1/6, -1/6)

# For KE Kähler form ω (the simple eigenform with W⁺ eigenvalue -1/3):
# q(R)(ω) = 2λω - 2μω where μ is the curvature op eigenvalue = -2/3
# = 2(-1)ω - 2(-2/3)ω = -2ω + 4/3 ω = -2/3 ω
# This should be 0 for parallel ω. It's NOT!

# So the formula q(R)(H) = 2λH - 2μH is WRONG.
# The correct formula must be different.

print("\n  The formula q(R)(H) = 2λH - 2R̂(H) gives a nonzero result")
print("  for the parallel Kähler form. This means the Weitzenböck")
print("  formula has a different form than I assumed.")
print()
print("  CORRECT WEITZENBÖCK FOR 2-FORMS (Besse, Thm 1.155):")
print("    q(R)(ω)_{ij} = Σ_{k,l} R_{ikjl} ω_{kl}")
print("  (NO separate Ricci terms; they are absorbed into R.)")
print()
print("  For Einstein: R_{ikjl} = W_{ikjl} + (s/12)(g_{ij}g_{kl} - g_{il}g_{kj})")
print("                          + (traceless Ricci terms) = 0 for Einstein")
print("  Wait, this doesn't have the Kulkarni-Nomizu term right...")

# ============================================================
# 6. USE BESSE'S EXACT FORMULA
# ============================================================
print("\n\n6. BESSE'S EXACT FORMULA (Theorem 1.155)")
print("-" * 60)

# Besse (Einstein Manifolds, 2008), Theorem 1.155:
# For a p-form ω, the Weitzenböck formula is:
# Δ_d ω = ∇*∇ω + F(R)(ω)
# where F(R) is the curvature endomorphism.
#
# For 2-forms specifically:
# F(R)(ω)_{ij} = Σ_k [R_{ik} ω_{kj} - R_{jk} ω_{ki}] + Σ_{k,l} R_{ikjl} ω_{kl}
#
# Wait, there's no factor of 2 here? Let me check.
# Actually from Besse p.53:
# F(R)(ω)_{i₁i₂} = Σ_k [R_{i₁k} ω_{ki₂} + R_{i₂k} ω_{i₁k}] 
#                   + Σ_{k,l} R_{i₁ki₂l} ω_{kl}
#
# For Einstein R_{ij} = λg_{ij}:
# Ricci terms: λ(ω_{i₁i₂} + ω_{i₁i₂}) = 2λω
# Curvature operator term: (R̃ω)_{i₁i₂} = R_{i₁ki₂l}ω^{kl}
#   where ω^{kl} = g^{ka}g^{lb}ω_{ab}

# But R_{i₁ki₂l} ≠ R_{i₁i₂kl} due to pair index ordering!
# R_{abcd} has symmetry R_{abcd} = R_{cdab} and R_{abcd} = -R_{bacd} = -R_{abdc}
# R_{i₁ki₂l} = R_{(i₁k)(i₂l)} with pair symmetry
# but (i₁k) means antisymmetric pair, so R_{i₁ki₂l} = -R_{ki₁i₂l}

# The map ω → (R̃ω)_{ij} = R_{ikjl}ω_{kl} is NOT the same as
# ω → (R̂ω)_{ij} = R_{ijkl}ω_{kl}

# R_{ikjl} = R_{jlik} (pair symmetry) = -R_{jilk} (antisym in second pair)
# = R_{jilk} with a sign...

# Let me just compute this for the Kähler-Einstein case numerically.
# Use the Fubini-Study metric on CP² (s > 0) or a hyperbolic KE surface (s < 0).

print("  Using explicit KE curvature tensor on a complex surface.")
print("  For a constant-holomorphic-sectional-curvature KE surface (s = -4, λ = -1):")
print("  R_{ijkl} = (λ/2)(g_{ik}g_{jl} - g_{il}g_{jk} + ω_{ik}ω_{jl} - ω_{il}ω_{jk} + 2ω_{ij}ω_{kl})")
print()

import numpy as np

lam_val = -1.0  # Ric = -g, s = -4

# Orthonormal frame, ω = e1∧e2 + e3∧e4
g = np.eye(4)  # orthonormal
omega = np.zeros((4,4))
omega[0,1] = 1; omega[1,0] = -1
omega[2,3] = 1; omega[3,2] = -1

# Curvature tensor for constant-holo-sec-curv Kähler surface
def R_tensor(i,j,k,l, lam, g, omega):
    return (lam/2)*(g[i,k]*g[j,l] - g[i,l]*g[j,k]
                   + omega[i,k]*omega[j,l] - omega[i,l]*omega[j,k]
                   + 2*omega[i,j]*omega[k,l])

R = np.zeros((4,4,4,4))
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                R[i,j,k,l] = R_tensor(i,j,k,l, lam_val, g, omega)

# Verify: Ric_{ij} = Σ_k R_{ikjk} = should be λ g_{ij}
Ric = np.einsum('ikjk->ij', R)
print(f"  Ric = λg check: Ric[0,0] = {Ric[0,0]:.4f}, λ = {lam_val}")
assert np.allclose(Ric, lam_val * g), "Ric ≠ λg!"
print(f"  Ric = λg ✓")

# Scalar curvature
s_val = np.trace(Ric)
print(f"  s = {s_val:.4f} (should be {4*lam_val})")

# Now compute F(R)(ω) using Besse's formula:
# F(R)(ω)_{ij} = Σ_k [R_{ik} ω_{kj} + R_{jk} ω_{ik}] + Σ_{k,l} R_{ikjl} ω_{kl}
# Wait, the exact formula from Besse for 2-forms:
# I need to be more careful about which version of the Weitzenböck formula.

# Let me use the version: Δ_d = ∇*∇ + q
# where for ω ∈ Λ², q(ω)_{ij} = Σ_k (Ric_{ik} ω_{kj} - Ric_{jk} ω_{ki}) + 2 Σ_{k,l} R_{ikjl} ω_{kl}

# This is from Petersen "Riemannian Geometry" (3rd ed), Chapter 9.
# Note the factor of 2 in front of the curvature term.

FR_omega = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        # Ricci terms
        ric_term = sum(Ric[i,k]*omega[k,j] - Ric[j,k]*omega[k,i] for k in range(4))
        # Curvature term (with factor 2)
        curv_term = 2*sum(R[i,k,j,l]*omega[k,l] for k in range(4) for l in range(4))
        FR_omega[i,j] = ric_term + curv_term

print(f"\n  F(R)(ω) (Petersen convention with factor 2):")
# Check if it's a scalar multiple of ω
if np.allclose(omega, 0):
    print("  omega is zero???")
else:
    ratio = FR_omega[0,1] / omega[0,1] if omega[0,1] != 0 else 0
    print(f"  F(R)(ω) / ω = {ratio:.6f}")
    print(f"  Is F(R)(ω) proportional to ω? {np.allclose(FR_omega, ratio * omega)}")
    if np.allclose(FR_omega, ratio * omega):
        print(f"  F(R)(ω) = {ratio:.6f} · ω")
        print(f"  For parallel ω: ∇*∇ω = 0, Δ_d ω = 0")
        print(f"  → 0 = 0 + {ratio:.6f} · ω")
        if abs(ratio) < 1e-10:
            print(f"  → {ratio:.6f} ≈ 0 ✓ CONSISTENT!")
        else:
            print(f"  → INCONSISTENT unless ratio = 0")

print(f"\n  Try without factor of 2:")
FR_omega_v2 = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        ric_term = sum(Ric[i,k]*omega[k,j] - Ric[j,k]*omega[k,i] for k in range(4))
        curv_term = sum(R[i,k,j,l]*omega[k,l] for k in range(4) for l in range(4))
        FR_omega_v2[i,j] = ric_term + curv_term

ratio_v2 = FR_omega_v2[0,1] / omega[0,1] if omega[0,1] != 0 else 0
print(f"  F(R)(ω) / ω = {ratio_v2:.6f}")
print(f"  Is proportional? {np.allclose(FR_omega_v2, ratio_v2 * omega)}")

# Also try the OTHER convention: q(ω)_{ij} = Σ_k (R_{ik}ω_{kj} + R_{jk}ω_{ik}) + 2R_{ikjl}ω_{kl}
print(f"\n  Try with PLUS in Ricci terms:")
FR_omega_v3 = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        ric_term = sum(Ric[i,k]*omega[k,j] + Ric[j,k]*omega[i,k] for k in range(4))
        curv_term = 2*sum(R[i,k,j,l]*omega[k,l] for k in range(4) for l in range(4))
        FR_omega_v3[i,j] = ric_term + curv_term

ratio_v3 = FR_omega_v3[0,1] / omega[0,1] if omega[0,1] != 0 else 0
print(f"  F(R)(ω) / ω = {ratio_v3:.6f}")
print(f"  Is proportional? {np.allclose(FR_omega_v3, ratio_v3 * omega)}")

# Let me try ALL reasonable conventions systematically
print(f"\n  SYSTEMATIC: q(ω)_ij = a·(RicTerms) + b·Σ R_ikjl ω_kl")
for a_coeff in [1, 2]:
    for b_coeff in [1, 2, -1, -2]:
        for ric_sign in [1, -1]:  # ω_{ki} vs -ω_{ki}
            FR_test = np.zeros((4,4))
            for i in range(4):
                for j in range(4):
                    ric_t = a_coeff * sum(Ric[i,k]*omega[k,j] + ric_sign*Ric[j,k]*omega[k,i] for k in range(4))
                    curv_t = b_coeff * sum(R[i,k,j,l]*omega[k,l] for k in range(4) for l in range(4))
                    FR_test[i,j] = ric_t + curv_t
            if np.allclose(FR_test, 0):
                print(f"  FOUND ZERO: a={a_coeff}, b={b_coeff}, ric_sign={ric_sign}")
            r = FR_test[0,1] / omega[0,1] if abs(omega[0,1]) > 1e-10 else None
            if r is not None and abs(r) < 1e-10 and np.allclose(FR_test, r*omega):
                print(f"  FOUND ~ZERO: a={a_coeff}, b={b_coeff}, ric_sign={ric_sign}, ratio={r:.8f}")

print("\n" + "=" * 70)
print("CONCLUSION from numerical computation")
print("=" * 70)
