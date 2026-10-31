# Route Assessment: Step 78

Session `S0910A01`. Step 78.

## What was accomplished

Three structural theorems for the A-equivariant diagonal Einstein desingularization of `(S²×S²)/Z₂`:

1. **Scalar kernel elimination by symmetry** (Theorem 2.1): The simultaneous antipodal map A makes all four Ozuch kernel modes A-odd, so an A-invariant construction is automatically orthogonal to them. This replaces the withdrawn "O(g_o)=0" claim with a proved symmetry restriction.

2. **Scalar decoupling theorem** (Theorem 3.1): For in-kernel EH directions, H⁴(ζ) has zero trace on each S² factor, hence zero coupling to ALL scalar eigenmodes. The inter-node Green response lives entirely in the vector+TT sectors where P is positive definite.

3. **Order analysis** (Theorem 4.1): At comparable scales, the inter-node interaction O(t³) is below the Ozuch remainder O(t^{5/2}). The leading reduced equation is simply μ_k(α) = 0 at each orbit, decoupled from other orbits.

Additional findings:
- **SO(2) covariance**: μ₂ and μ₃ are independent of the in-kernel angle α. The angle is pure gauge at the obstruction level. Sufficient to check at one convenient angle.
- **Rank-one orthogonality**: R⁻·ρ(ζ)⁻ = 0 (verified). But dR⁻·v = 8v/r⁶ ≠ 0 (TTCS correction). NOT sufficient for μ₂ = μ₃ = 0.
- **Spectral gap correction**: Full non-scalar gap is Λ, not 3Λ/2 (mixed 1-form sector has eigenvalue Λ).

## What it establishes

The problem is now precisely framed: the equivariant diagonal construction reduces to a SINGLE binary question:
- **Do μ₂(ω₂) and μ₃(ω₂) vanish for the rank-1 product curvature block?**
  - If YES: all Ozuch necessary conditions are satisfied at O(t^{5/2}), and the path to Einstein metrics on #3(S²×S²) requires only inverse/nonlinear estimates on a positive-definite operator.
  - If NO: the obstruction is a nonzero constant, and no in-kernel EH direction works on the product orbifold.

## What it does NOT establish

- The values of μ₂ and μ₃ (the Biq16 computation is still needed)
- An inverse estimate on the non-scalar sector
- Nonlinear contraction for the full Einstein equation
- The full Yau-26 resolution (this is only a positive-branch test family)

## Immediate next work (in priority order)

1. **Compute μ₂ and μ₃** from the Biq16/Ozuch formulas at α=0 (ζ = ω₂) on the product curvature block. This is the decisive calculation. Use Ozuch Lemma 2.14 and [Biq16, Lemme 15]. The rank-1 block R = diag(Λ,0,0) and the factor-traceless H^4 provide specific input.

2. **If μ = 0**: Construct the A-equivariant weighted Schauder inverse on the non-scalar sector. The positive spectral gap Λ and the absence of kernel in the A-invariant sector should give standard estimates.

3. **Cross-orbit interaction analysis**: When scales differ (t₁ ≫ t₂), the inter-node term can compete with the self-obstruction. Compute I_{12} in the positive-definite non-scalar resolvent.

4. **Keep all three Yau-26 fronts active**:
   - Negative IL branch: mature, proof-level assembly
   - Graph-neck: A03's full-constraint continuation from center data
   - Positive mixed-row: this step's equivariant reduction
   None resolves the full proposition alone.

## Files

- Note: `workspace/notes/step78_equivariant_diagonal_reduction.md`
- Data: `workspace/data/step78_equivariant_construction.json`, `step78_spectral_structure.json`, `step78_rank_one_orthogonality.json`
- Scripts: `workspace/scripts/step78_equivariant_construction.py`, `step78_spectral_structure.py`, `step78_rank_one_orthogonality.py`
- TTCS: `trace/ttcs/results/step78_ttcs01_verifier1_integration.md`
