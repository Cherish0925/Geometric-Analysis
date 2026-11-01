#!/usr/bin/env python3
"""Step 67 Part 2: Inter-node coupling and orbifold deformation space.

For the product orbifold (S²×S²)/Z₂ with Λ>0 Einstein metric:
(a) Compute dim O(g_∞) — the infinitesimal Einstein deformation space
(b) Determine the structure of the Green's operator coupling between nodes
(c) Identify the leading inter-node coupling coefficient

The 4 A₁ points are at the Z₂ fixed points of S²×S²:
  p₁=(N,N), p₂=(N,S), p₃=(S,N), p₄=(S,S)
"""
import numpy as np
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "step67_internode_coupling.json"

# =====================================================================
# Part A: Infinitesimal Einstein deformations O(g_∞)
# =====================================================================
# The product metric g = g_{S²(Λ)} ⊕ g_{S²(Λ)} on S²×S² is KE (Λ>0).
# P_g = (1/2)∇*∇ - R̊ on TT symmetric 2-tensors.
#
# The infinitesimal Einstein deformations of product metrics on S²×S²:
# By Koiso's decomposition, on a product of Einstein manifolds (M₁×M₂, g₁⊕g₂):
#   O(g) = O(g₁) ⊕ O(g₂) ⊕ {f(g₁-g₂) : f harmonic on M₁×M₂} 
#          ⊕ {cross terms from mixed harmonic maps}
#
# For S²(Λ): simply connected, positive curvature
#   O(g_{S²}) = 0 (round S² is rigid among Einstein surfaces)
#
# The cross-product deformations come from:
#   h = f · (g₁ - g₂) where Δf = -2Λf on S²×S²
# But we need h to be TT: tr_g h = 0 and δ_g h = 0.
# tr_g(f(g₁-g₂)) = f(2-2) = 0 ✓
# δ_g(f(g₁-g₂)) = df(g₁-g₂) + f·δ_g(g₁-g₂) = df♯ - df♯ = 0 
# Wait, need to be careful: δ_g(fg₁) = (df)♯ + f·δg₁ = df♯ (since δg₁=0 on M₁×M₂)
# Actually δ_{g₁⊕g₂}(fg₁) has components mixing, needs full computation.
#
# For the product of round S²s, the relevant eigenvalue is the first nonzero
# eigenvalue of the Laplacian on S²: λ₁ = 2/R² where R is the radius.
# For S²(Λ) with Ric=Λg, the Gaussian curvature is Λ, radius R = 1/√Λ,
# so λ₁ = 2Λ.
#
# The TT condition on f(g₁-g₂) for the Lichnerowicz operator P:
# P(f(g₁-g₂)) = (1/2)∇*∇(f(g₁-g₂)) - R̊(f(g₁-g₂))
# = (1/2)(Δf)(g₁-g₂) + ... curvature terms
#
# For the round S²×S², the product is actually KE with c₁² = 8.
# Wait: the product S²×S² has χ=4, τ=0, so 2χ+3τ=8 and c₁²=8.
# But our orbifold (S²×S²)/Z₂ has c₁²= 8/|Z₂| = 4.
# This matches the LeBrun-Ozuch dP4 case!

# The KEY fact from LeBrun-Ozuch: for c₁²(X)=4 orbifolds, singularities
# are all A₁ (Z₂) and no bubble trees form. Corollary 9.2 applies.

# For the smooth S²×S², Koiso-Cao computed:
#   O(g_{S²×S²}) is spanned by the KE deformations.
#   S²×S² is NOT rigid: it deforms to CP²#CP̄² with the Page metric family.
#   Actually, S²×S² and CP²#CP̄² are in the same smooth family of KE metrics
#   (the toric dP family with c₁²=8).

# BUT our orbifold is (S²×S²)/Z₂, not S²×S² itself.
# O(g_∞) for the orbifold includes ONLY Z₂-invariant deformations.
# The Z₂ action is the simultaneous antipodal map on both factors.

# For the toric KE metrics on dP surfaces with c₁²=4:
# The moduli space is 2-dimensional (Odaka-Spotti-Sun).
# The toric moduli give deformations of the orbifold complex structure.
# For our product orbifold, dim O(g_∞) includes these moduli.

# Rather than compute dim O(g_∞) exactly (which requires knowing the full
# Lichnerowicz spectrum on the orbifold), note that for the PURPOSE of the
# obstruction computation, we need:
#   - The obstruction space at each bubble (3D per bubble)
#   - The inter-node coupling through G

print("="*60)
print("Part A: Orbifold structure and deformation")
print("="*60)
print(f"Orbifold: (S²×S²)/Z₂, c₁² = 4, 4 A₁ points")
print(f"Einstein constant: Λ > 0 (normalized to Λ=3 for LeBrun-Ozuch)")
print(f"Singularity type: all C²/Z₂ (no bubble trees)")
print(f"Applicable theorems: LeBrun-Ozuch §9, Ozuch higher-order §2")

# =====================================================================
# Part B: Node positions and distances
# =====================================================================
# On S²(1/√Λ) × S²(1/√Λ), the Z₂ fixed points are:
# p₁ = (N₁,N₂), p₂ = (N₁,S₂), p₃ = (S₁,N₂), p₄ = (S₁,S₂)
# where N,S are the poles of each round S².
#
# Geodesic distances on the orbifold:
# d(pᵢ,pⱼ) on (S²×S²)/Z₂ with the product metric

Lam = 1  # normalize
R = 1/np.sqrt(Lam)  # radius of each S²

# On S²(R): d(N,S) = πR = π/√Λ
d_NS = np.pi * R

# Product distances:
# d(p₁,p₂) = d((N,N),(N,S)) = d_S²(N,N) + d_S²(N,S) = 0 + πR (NOT Euclidean sum)
# Actually on product: d²((a₁,a₂),(b₁,b₂)) = d²(a₁,b₁) + d²(a₂,b₂) (Pythagorean)
d = {}
d[(1,2)] = d_NS  # same first factor, opposite second
d[(1,3)] = d_NS  # opposite first, same second
d[(1,4)] = np.sqrt(2)*d_NS  # opposite on both
d[(2,3)] = np.sqrt(2)*d_NS  # mixed: both differ
d[(2,4)] = d_NS  # same first, opposite second
d[(3,4)] = d_NS  # opposite first, same second

print(f"\n{'='*60}")
print(f"Part B: Node distances on S²×S² (Λ=1)")
print(f"{'='*60}")
for (i,j), dij in d.items():
    print(f"  d(p{i},p{j}) = {dij:.4f} = {dij/np.pi:.4f}π")

# Node adjacency structure:
# Adjacent (distance πR): (1,2), (1,3), (2,4), (3,4)
# Diagonal (distance π√2 R): (1,4), (2,3)
# This is the edge/diagonal structure of a square.

print(f"\n  Adjacency: square graph with diagonals")
print(f"  4 adjacent pairs (distance πR)")  
print(f"  2 diagonal pairs (distance π√2·R)")

# =====================================================================
# Part C: Symmetry of the mixed pattern
# =====================================================================
# Compatible pattern (r=0): all 4 nodes use ζ⁺ ∈ ker(R⁺)
# Mixed r=1: 1 reversed, 3 compatible (4 ways)
# Balanced r=2: 2 reversed, 2 compatible (6 ways, but symmetry reduces)
#   - Adjacent pair reversed: (p₁,p₂) or (p₁,p₃) etc.
#   - Diagonal pair reversed: (p₁,p₄) or (p₂,p₃)
# Mixed r=3: 3 reversed, 1 compatible (4 ways)
# All reversed r=4: orientation-reversal of r=0

# For the balanced r=2 patterns:
# The orbifold Z₂×Z₂ symmetry (permuting the 4 nodes) distinguishes:
# - Adjacent reversed: inequivalent classes by node position
# - Diagonal reversed: two inequivalent classes

print(f"\n{'='*60}")
print(f"Part C: Mixed patterns and symmetry")
print(f"{'='*60}")
print(f"  r=0: all compatible → dP4 KE (known Einstein by LeBrun-Ozuch)")
print(f"  r=1: 1 reversed → 4 patterns (mod Z₂×Z₂: up to 2 classes)")
print(f"  r=2: 2 reversed → 6 patterns")  
print(f"    Adjacent: e.g., (p1,p2) reversed — 4 patterns")
print(f"    Diagonal: e.g., (p1,p4) reversed — 2 patterns")
print(f"  r=3: 3 reversed → mirror of r=1")
print(f"  r=4: all reversed → orientation-reversal of r=0 (known Einstein)")

# =====================================================================  
# Part D: Leading coupling coefficient structure
# =====================================================================
# In Ozuch's framework (arXiv:2012.13316, §2.1):
# The correction h₂ on each EH bubble satisfies:
#   P_eh h₂ = Λ·eh + Σ λ_k o_k
# with h₂ ~ H₂ at infinity.
#
# The asymptotic term of h₂ at infinity (beyond H₂) contains an O(r⁻²) piece
# that is determined by the EH Green's function.
# 
# On the orbifold side, the fourth-order jet h⁴ satisfies:
#   P_{g_∞} h⁴ = Σ_j [source from node j] + w⁴ (∈ O(g_∞))
#
# The source at node j contains the r⁻⁴ falloff of the EH correction,
# which depends on the orientation (compatible vs reversed) through
# the chirality of H⁴(ζ±).
#
# The Green's operator G couples node j to node k:
#   h⁴(near node k) = G * (source at node j) + ...
# This coupling is the leading inter-node term.
#
# For the product orbifold, the Green's function of P_{g_∞} on TT tensors
# can be expanded in product spherical harmonics.

# The KEY coupling coefficient is:
#   c_{jk} = ∫_{∂B_ε(p_k)} ⟨G(·,p_j)·[source_j], n⟩ dσ
# where [source_j] is the δ-function-like r⁻⁴ source from node j.

# For the flat case (T⁴/Z₂, Ozuch), the Green function is explicit:
# G(x,y) ~ 1/|x-y|² (in 4D, for the Laplacian)
# The coupling between nodes j,k goes as 1/d(p_j,p_k)²

# For our product (S²×S²), the Green function has a different structure
# but the leading behavior near each node is still ~ 1/ρ² 
# (where ρ = geodesic distance).

# The coupling matrix (leading order) is:
n_nodes = 4
C = np.zeros((n_nodes, n_nodes))
for i in range(n_nodes):
    for j in range(n_nodes):
        if i != j:
            key = (min(i+1,j+1), max(i+1,j+1))
            C[i,j] = 1/d[key]**2  # leading Green's function coupling

print(f"\n{'='*60}")
print(f"Part D: Leading coupling matrix (proportional to 1/d²)")
print(f"{'='*60}")
print(f"C_ij (relative to 1/π²):")
C_norm = C * np.pi**2
for i in range(4):
    row = "  "
    for j in range(4):
        row += f"{C_norm[i,j]:8.4f}"
    print(row)

# Structure: the coupling is a graph Laplacian on the square with diagonals
# Adjacent nodes: coupling 1/π²
# Diagonal nodes: coupling 1/(2π²) = 0.5/π²

print(f"\n  Adjacent coupling: {1/d_NS**2:.6f} (= 1/π²)")
print(f"  Diagonal coupling: {1/(np.sqrt(2)*d_NS)**2:.6f} (= 1/(2π²))")

# =====================================================================
# Part E: Chirality content of the source terms
# =====================================================================
# Compatible bubble (W⁺≡0): 
#   H⁴(ζ⁺) = -ρ(ζ)⁻∘ζ⁺/(2r⁴)  — this has SD×ASD structure
#   The correction h₂ contributes a source with ASD curvature content
#
# Reversed bubble (W⁻≡0):
#   H⁴(ζ⁻) = -ζ⁻∘ρ(ζ)⁺/(2r⁴)  — this has ASD×SD structure
#   The correction h₂ contributes a source with SD curvature content
#
# On the product orbifold, the TT tensor source at node j decomposes:
#   source_j ∈ Sym₀²(T*p_j) ≅ Ω⁺(p_j) ⊗ Ω⁻(p_j)
#
# For compatible: source has dominant content in specific Ω⁺⊗Ω⁻ channels
# For reversed: source has content in the OPPOSITE Ω⁺⊗Ω⁻ channels
# (because H⁴ swaps the chirality)

print(f"\n{'='*60}")
print(f"Part E: Chirality and the decisive mechanism")
print(f"{'='*60}")
print(f"""
For compatible EH at node j with ζ_j⁺ = a ω₂⁺ + b ω₃⁺:
  H⁴ = -(ρ(ζ)⁻ ∘ ζ⁺)/(2r⁴)
  → source contributes to SPECIFIC tensor spherical harmonics

For reversed EH at node j with ζ_j⁻ = a ω₂⁻ + b ω₃⁻:
  H⁴ = -(ζ⁻ ∘ ρ(ζ)⁺)/(2r⁴)
  → source contributes to DIFFERENT tensor spherical harmonics
  (chirality-swapped relative to compatible)

The inter-node coupling through G mixes these:
  μ_k(mixed) = Σ_j G_kj × [chirality_j-dependent source]
  
For all-compatible: all sources have same chirality structure.
  The obstruction VANISHES (by LeBrun-Ozuch Corollary 9.2).

For mixed: sources at compatible and reversed nodes have DIFFERENT chirality.
  The coupling mixes opposite-chirality sources.
  WHETHER THE OBSTRUCTION VANISHES IS A FINITE COMPUTATION
  on the product S²×S² Green's operator.
""")

# =====================================================================
# Part F: Obstruction equation count for (S²×S²)/Z₂
# =====================================================================
# Ozuch's framework (T⁴/Z₂ case: 16 nodes):
#   57 degrees of freedom, 84 equations → overdetermined
#   But 14D solution family found (chessboard pattern)
#
# Our case ((S²×S²)/Z₂: 4 nodes):
#   At each node: ζ ∈ ker(R±) = R² (direction in 2D kernel)
#                 |ζ| ∈ R⁺ (scale)
#   Total bubble parameters: 4 × 3 = 12
#   Orbifold deformations: dim O(g_∞) (to be determined)
#
#   First obstructions: 4 × 3 = 12, ALL ZERO (2D kernel)
#   Second obstructions: 4 × 3 = 12 equations
#   Inter-node coupling: additional constraints from h⁴ matching
#
#   The DECISIVE question: do the 12 second-obstruction equations
#   (which include inter-node coupling) have a solution?

# For the IDENTICAL pattern (r=0 or r=4): solution exists (KE metrics).
# For the MIXED pattern: open question.

# The key constraint from the curvature content:
# Compatible bubble at node j: the linearized curvature change on EH is 
#   ASD: d_e R⁻(H⁴(ζ⁺)) = 12 π_tr(ρ(ζ)⁻ ⊗ ρ(ζ)⁻)/r⁶
# Reversed bubble at node j: the linearized curvature change is
#   SD: d_e R⁺(H⁴(ζ⁻)) = 12 π_tr(ρ(ζ)⁺ ⊗ ρ(ζ)⁺)/r⁶
#
# The Wu criterion det(W⁺) > 0:
# Compatible bubbles REDUCE |W⁺| (they add ASD curvature only)
# Reversed bubbles ADD to |W⁺| (they add SD curvature)
# This is exactly LeBrun-Ozuch's argument for why mixed patterns break Wu.

# CRITICAL DISTINCTION:
# LeBrun-Ozuch prove: IF the sequence is admissible (all W⁺≡0 bubbles),
#   THEN Wu criterion holds → metrics are KE.
# For NON-admissible (mixed) sequences: Wu criterion MAY FAIL.
# If Wu fails, the metrics need not be KE.
# But this does NOT mean the metrics don't EXIST.
# It only means they're not conformally Kähler.

# The EXISTENCE question is decided by the obstruction equations.
# If the finite-dimensional obstruction VANISHES: Einstein metrics EXIST
#   (by Ozuch's existence theorem, under transversality)
# If the obstruction is NONZERO: no Einstein metric NEAR the orbifold.

print(f"\n{'='*60}")
print(f"Part F: Summary and next computation")
print(f"{'='*60}")
print(f"""
PARAMETER COUNT:
  Bubble parameters: 4 × 3 = 12 (direction + scale at each node)
  Orbifold deformations: dim O(g_∞) (TBD, likely 2+ from KE moduli)
  Total DOF: 12 + dim O(g_∞)

OBSTRUCTION COUNT:
  First obstruction: 12 equations, ALL AUTOMATICALLY ZERO
  Second obstruction: 12 equations (including inter-node coupling)
  Higher: additional constraints if second-order transversality fails

KNOWN SOLUTIONS:
  r=0 (all compatible): solution exists (dP4 KE family)
  r=4 (all reversed): solution exists (orientation reversal)
  
OPEN QUESTIONS (decidable by finite computation):
  r=1,2,3 (mixed): do the second obstruction equations have a solution?

NEXT COMPUTATION NEEDED:
  1. Compute the product spherical harmonic expansion of the Green
     operator G of P_g on (S²×S²)/Z₂ 
  2. Evaluate the inter-node coupling coefficients
  3. Write the explicit obstruction system for r=2 balanced pattern
  4. Check for solutions (polynomial system, small dimension)
""")

# Save
data = {
    "orbifold": "(S2xS2)/Z2",
    "c1_squared": 4,
    "n_nodes": 4,
    "node_positions": ["(N,N)", "(N,S)", "(S,N)", "(S,S)"],
    "distances_over_pi": {
        "adjacent": 1.0,
        "diagonal": float(np.sqrt(2))
    },
    "coupling_matrix_relative": C_norm.tolist(),
    "bubble_DOF": 12,
    "first_obstruction": "all_zero_2D_kernel",
    "second_obstruction_count": 12,
    "known_solutions": ["r=0 (compatible, KE)", "r=4 (reversed, orientation flip)"],
    "open_patterns": ["r=1", "r=2 (adjacent)", "r=2 (diagonal)", "r=3"],
    "decisive_computation": "second obstruction with inter-node coupling",
    "chirality_mechanism": "compatible: ASD source; reversed: SD source; coupling through Green operator",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, indent=2))
print(f"\nOutput: {OUT}")
