# Step 67 — Complete Findings and Handoff

## What was established

### 1. Curvature at A₁ points (VERIFIED SYMBOLICALLY)
On the product orbifold (S²(Λ)×S²(Λ))/Z₂ with 4 A₁ points:
- R⁺ = R⁻ = diag(Λ, 0, 0): both have 2-dimensional kernel
- W⁺ = W⁻ = diag(2Λ/3, −Λ/3, −Λ/3): exactly KE form
- ker(R⁺) = span{ω₂⁺, ω₃⁺}, ker(R⁻) = span{ω₂⁻, ω₃⁻}

Consequence: The first Biquard obstruction λ_k = c⟨R±ζ, ζ₍ₖ₎⟩ = 0 
for ALL ζ in the 2D kernel, for BOTH orientations.

### 2. Ambient quadratic jet H₂ (VERIFIED SYMBOLICALLY)
H₂ has 5 active angular components in the ω_i⁺∘ω_j⁻ basis:
- 1 U(2)-invariant: ω₁⁺∘ω₁⁻
- 4 non-U(2)-invariant: {ω₂,ω₃}⁺ × {ω₂,ω₃}⁻ block

The Step 65-66 U(2)-radial 3-function ansatz captures only the ω₁⁺∘ω₁⁻ sector.
This EXPLAINS the BVP convergence failure: the ansatz omits the dominant content.

### 3. Local orientation independence (PROVED BY STRUCTURE)
The local correction h₂ solving P_eh h₂ = Λ·eh + Σλ_k o_k has:
- λ_k = 0 (from 2D kernel): so P_eh h₂ = Λ·eh
- h₂ ~ H₂ at infinity (same for both orientations)
- Q²(h₂,h₂) depends only on h₂ and the EH metric (orientation-independent)

Therefore: LOCAL second obstruction μ_k is IDENTICAL for compatible and reversed.

### 4. Decisive mechanism identified (FROM SOURCE ANALYSIS)
The ONLY source of obstruction for mixed patterns is inter-node coupling:
- Compatible node: H⁴(ζ⁺) = −(ρ(ζ)⁻∘ζ⁺)/(2r⁴) → ASD source  
- Reversed node: H⁴(ζ⁻) = −(ζ⁻∘ρ(ζ)⁺)/(2r⁴) → SD source
- Green's operator G of P_{g_∞} couples different nodes
- The CHIRALITY of the source distinguishes compatible from reversed

### 5. LeBrun-Ozuch framework applied
From arXiv:2601.19215, §9 and Corollary 9.2:
- Admissible sequences (all W⁺≡0 bubbles) → metrics are KE on CP²#5CP̄²
- Mixed sequences are NON-admissible → outside the scope of their theorem
- But Ozuch's Einstein-modulo-obstructions construction applies to ALL patterns
  (Theorem 4.10, Propositions 5.11/5.13 of Ozuch II)

### 6. Codex loop result (COLLECTED AND ASSESSED)
The 2D toy model validated the numerical pipeline (control+mixed+symmetry+audit),
but has no 4D implications. The four-dimensional prototype requires dolfinx/PETSc
and a conforming tagged mesh, which are not currently available.

## What remains open

### The decisive finite computation
For each mixed pattern (r=1,2,3), determine whether the finite-dimensional
Ozuch obstruction equations have a solution:
1. Compute H_{j,2}: the quadratic correction at remaining nodes from partial
   desingularization, using the Green operator G of P_{g_∞} on (S²×S²)/Z₂
2. Evaluate the modified R±(p) at remaining nodes after inter-node correction
3. Write the obstruction equations (polynomial in direction + scale parameters)
4. Determine solvability

Key technical ingredients:
- Product Lichnerowicz spectrum on TT tensors of S²×S²
- Green's function evaluated at pairs of A₁ points
- Angular harmonic decomposition of the sources

### Framework for the computation
From Ozuch arXiv:2012.13316, §3.2-3.3:
- The partial desingularization g± (same-orientation nodes) is KE
- At remaining nodes j ∈ S∓: g± = e + H_{j,2} + O(r⁴)
- H_{j,2} = Σ_{i∈S±} [Green coupling from node i to j] × H⁴(ζ_i±)
- This is formula (67) with the product Green operator replacing the flat one
- The λ-type obstruction at j involves ⟨R±_modified · ζ_j, ζ_{j,(k)}⟩
- The μ-type involves h₂ solving P_eh h₂ = Λ eh with h₂ ~ H_{j,2} at infinity

## Files produced
- `workspace/scripts/step67_ambient_jet_and_obstruction.py` → verified R±, H₂, angular decomposition
- `workspace/scripts/step67_internode_coupling.py` → node distances, coupling structure
- `workspace/data/step67_ambient_jet_and_obstruction.json` → complete numerical data
- `workspace/data/step67_internode_coupling.json` → coupling matrix and pattern analysis
- `workspace/notes/step67_obstruction_framework_and_ambient_jet.md` → detailed analysis

## Sources used
- LeBrun-Ozuch arXiv:2601.19215 (Definition 1, Theorem A, §8-9, Corollary 9.2)
- Ozuch arXiv:2012.13316 (Theorem 0.2, §1-3, equation 25 for λ_k formula)
- Ozuch arXiv:1909.12960 (Theorem 4.10, Propositions 5.11/5.13)
- Biquard arXiv:1105.4904 (Section 4, Lemmas 4.1-4.2)
