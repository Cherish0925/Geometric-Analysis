# Route Assessment — Step 84

Session `S0910A01`. Updated after T-symmetry, chirality H^4 angular
difference, and TTCS verification.

## Positive mixed-row branch: current exact structural state

### Established (exact algebra)
1. **Ozuch obstruction vanishing through O(t^{5/2})**: λ_k=0 (rank-one),
   μ₁=0 (rank-one determinant), μ₂,μ₃ eliminated by J-parity,
   ν_l eliminated by A-parity. All within A+J equivariant family.

2. **L-exchange symmetry**: F₁(t₁,t₂) = F₂(t₂,t₁) after consistent
   normalization. Equal-scale branch t₁=t₂=t reduces to one equation.

3. **T-symmetry (NEW)**: For the pencil c=1/2, κ=-1, the group
   G=⟨T,S₀,S₂⟩ acts transitively on all 4 nodes and kills all
   continuous automorphisms of X₀. This removes the infinite-Aut
   obstacle for G-equivariant Spotti-type arguments.

4. **Chirality angular difference (NEW)**: The orthogonality identity
   tr(C_{ab}C_{cd})=4δ_{ac}δ_{bd} gives:
   - Same-chirality obstruction Gram: 4I₃
   - Cross-chirality obstruction Gram: diag(0,4,0)
   - Pointwise difference: 4(1-p₂²) ≥ 0, mean 8/3 on S³

### NOT established
1. **c_opp - c_same**: The 8/3 is a local angular Gram numerator, not
   the Green-projected inter-node coefficient. The full product
   Lichnerowicz pseudo-inverse transfer could cancel or preserve it.

2. **Matched KE control**: The G-equivariant KE degeneration should give
   s+d+2c_same=0, but this requires identifying the KE path in the
   Biquard-Ozuch chart (insertion directions, scales, gauge).

3. **Nonlinear closure**: Even with the leading coefficient computed,
   a nonlinear inverse/remainder estimate is needed for the full
   desingularization theorem.

## Decisive computation

The SINGLE number c_opp - c_same determines the mixed-chirality route:
- If nonzero: nearby-orbifold construction is obstructed for #₃(S²×S²)
- If zero: next-order analysis needed (t³ log t terms, etc.)

Computing it requires:
- Product S²×S² Lichnerowicz eigentensors (separated spectrum)
- H^4 angular overlap with eigentensors at source node
- Green kernel propagation (spectral sum)
- Obstruction projection at receiver node
- All in the C_{ab} basis with proper Bianchi/gauge corrections

This is a definite spectral computation on the round product.

## Broader Yau-26 state

| Branch | Status | Scope |
|--------|--------|-------|
| IL negative theorem | Research-level assembly | Restricted 4D geography |
| Mixed-row positive | Angular Gram computed | One orbifold family |
| Graph-manifold | Rotating eigenframe blocked | Need matrix connectors |
| Higher dimensions | No mechanism | n≥5 open |

The restricted IL negative theorem remains the strongest scope-relevant
result directly aligned with Yau-26. The mixed-row computation is a
demanding positive stress test that could produce either a new Einstein
construction or a local obstruction.

## Files

- Notes: `workspace/notes/step84_corrections_and_matched_control.md`
- T-symmetry: `workspace/data/step84_T_symmetry_automorphism.json`
- Chirality: `workspace/data/step84_chirality_corrected.json`
- Obstruction: `workspace/data/step84_chirality_obstruction_projection.json`
- TTCS: `trace/ttcs/results/step84_ttcs01_verifier1_integration.md`
