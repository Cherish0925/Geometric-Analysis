# Step 67: Obstruction Framework and Ambient Jet Analysis

## Target
Determine whether the Ozuch finite-dimensional obstruction vanishes for mixed EH bubble patterns on the positive-Einstein product orbifold (S²×S²)/Z₂ with 4 A₁ points.

## Verified Results

### R± at each A₁ point (verified symbolically)
The product S²(Λ)×S²(Λ) with Ric = Λg has:
- R⁺ = W⁺ + (Λ/3)I = diag(Λ, 0, 0) in the basis (ω₁⁺, ω₂⁺, ω₃⁺)
- R⁻ = W⁻ + (Λ/3)I = diag(Λ, 0, 0) in the basis (ω₁⁻, ω₂⁻, ω₃⁻)
- W± = diag(2Λ/3, -Λ/3, -Λ/3)
- ker(R⁺) = span{ω₂⁺, ω₃⁺}, dim = 2
- ker(R⁻) = span{ω₂⁻, ω₃⁻}, dim = 2

The curvature has EXACTLY the Kähler-Einstein form (4) of Ozuch Theorem 0.2.

### First obstruction (Biquard/Ozuch)
For compatible EH (W⁺≡0): ζ⁺ ∈ ker(R⁺) ⟹ λₖ = c⟨R⁺ζ, ζ₍ₖ₎⟩ = 0 for all k.
For reversed EH (W⁻≡0): ζ⁻ ∈ ker(R⁻) ⟹ λₖ = 0 similarly.
**FIRST OBSTRUCTION AUTOMATICALLY ZERO at every A₁ point, for both orientations.**

### Ambient quadratic jet H₂
In normal Bianchi-gauge coordinates at an A₁ point:
- H₂ is block-diagonal: nonzero only in (x₁,x₂)-block and (x₃,x₄)-block
- tr(H₂) = -(Λ/3)r²
- The trace-free part H₂° has 5 active components in the ω_i⁺∘ω_j⁻ basis:
  - ω₁⁺∘ω₁⁻ (U(2)-invariant, separates the two S² factors)
  - ω₂⁺∘ω₂⁻, ω₃⁺∘ω₃⁻, ω₂⁺∘ω₃⁻, ω₃⁺∘ω₂⁻ (NOT U(2)-invariant)
- Zero components: ω₁⁺∘ω₂⁻, ω₁⁺∘ω₃⁻, ω₂⁺∘ω₁⁻, ω₃⁺∘ω₁⁻

### U(2) representation content
Under the Hopf U(1) ⊂ U(2) (diagonal phase rotation):
- ω₁⁺ has charge 0; ω₂⁺±iω₃⁺ have charge ±2
- ALL ω_j⁻ have charge 0
- U(2)-invariant Sym₀²: span{ω₁⁺∘ω₁⁻, ω₁⁺∘ω₂⁻, ω₁⁺∘ω₃⁻} (3-dimensional)
- But ω₁⁺∘ω₂⁻ and ω₁⁺∘ω₃⁻ are ABSENT from H₂.
- The active non-U(2) content is in the {ω₂,ω₃}⁺ × {ω₂,ω₃}⁻ block (4D, charge ±2)

**Consequence: The Step 65-66 U(2)-radial ansatz captures only 1 of 5 angular sectors of H₂.**
This explains the BVP convergence failure: the radial system solves the wrong projection.

### Isotropy structure
- Product curvature: O(2)×O(2) = T² ⊂ U(2) (independent rotations of each S²)
- EH symmetry: U(2) (via the standard complex structure on C²/Z₂)
- Intersection: T² (common maximal torus)
- The ambient jet at ANY gluing rotation has the same T²-invariant structure
- No choice of EH rotation makes the full H₂ U(2)-invariant

## Implications for the Obstruction Computation

### Framework (Ozuch arXiv:2012.13316, Sections 1-2)
For the compact orbifold (S²×S²)/Z₂ with 4 A₁ nodes:

1. **Degrees of freedom per node**: ζ ∈ ker(R±) is 2-dimensional, plus 1 scale = 3 real per node
   Total from bubbles: 4 × 3 = 12
   Plus: dim O(g_∞) from orbifold deformations

2. **Obstructions per node**: 3 second-order λ-type, but first two vanish automatically.
   The third λ₁ is nonzero (since R±ζ has a component along the Λ-eigenspace).
   Wait — λ₁ = c⟨R±ζ, ζ₍₁₎⟩ where ζ₍₁₎ = ζ/|ζ|. For ζ ∈ ker(R±), R±ζ = 0, so ALL λ_k = 0.
   
   The μ-type (second order) obstructions are the main object. Per node: 3 real.
   Total from local second order: 4 × 3 = 12
   Plus: inter-node coupling obstructions

3. **Inter-node coupling**: Through the orbifold Green's operator G of P_{g_∞} on (S²×S²)/Z₂.
   The h^4 term in Ozuch's construction (equation 21 in LeBrun-Ozuch) requires solving
   P_{g_∞} h^4 = source (from bubble corrections) with w^4 ∈ O(g_∞).
   The source at each node is a TT tensor on the orbifold, and G couples different nodes.

### Product structure of Green's operator
On S²(Λ)×S²(Λ), the Lichnerowicz Laplacian P_g decomposes by eigenvalues of each factor:
- Scalar harmonics Y_{l₁}(S²₁) × Y_{l₂}(S²₂), l₁,l₂ ≥ 0
- Tensor harmonics similarly factorize
- The Green function G(x,y) = Σ ψ_λ(x)ψ_λ(y)/λ
- For TT tensors, relevant eigenvalues involve both curvature and Laplacian

The 4 A₁ points are the Z₂ fixed points of (S²×S²):
- p₁ = (N,N), p₂ = (N,S), p₃ = (S,N), p₄ = (S,S)
where N,S are north/south poles of each S².

The distances on the orbifold: d(pᵢ,pⱼ) = π/√Λ for adjacent pairs (sharing one pole),
d(p₁,p₄) = d(p₂,p₃) = π√2/√Λ for diagonal pairs.

### Key symmetry of the obstruction
By the bi-Kähler mirror (chirality exchange ω⁺ ↔ ω⁻):
- A compatible EH at node j with ζⱼ⁺ ∈ ker(R⁺)
- A reversed EH at node j with ζⱼ⁻ ∈ ker(R⁻)
have IDENTICAL local obstruction equations (identical source terms, identical kernels).

Therefore: **the local second obstruction μ_k is the same function of (|ζ|, direction in ker) whether the bubble is compatible or reversed.**

Any difference between compatible and mixed patterns must come from:
(a) The asymptotic term H^4(ζ±) of the EH metric, which has OPPOSITE chirality:
    compatible: H^4 ~ ω_k⁺∘ρ(ζ)⁻/r⁴ (ASD content)
    reversed:   H^4 ~ ζ⁻∘ρ(ζ)⁺/r⁴ (SD content)
(b) The inter-node coupling through the orbifold Green operator, which sees the CHIRALITY of each node's correction

This is the decisive mechanism: compatible nodes contribute ASD source terms to the orbifold correction, reversed nodes contribute SD terms. The coupling through G mixes these differently than an all-compatible or all-reversed pattern.

## Next Steps
1. Compute the Green's operator kernel on (S²×S²)/Z₂ for TT tensors — at least the leading spherical-harmonic terms
2. Evaluate the inter-node coupling matrix for the 4 nodes
3. Write the full finite-dimensional obstruction system for a mixed pattern
4. Determine whether it has a solution (Einstein desingularization exists) or not
