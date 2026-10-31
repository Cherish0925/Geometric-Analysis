# Route assessment after Step 45


> **Step 47 superseding notice.** The strategic extension in lines 64--91 below is withdrawn. In Step 46--47 source reading showed that the `Vol/A -> 32π²/9` calibration and the associated mean critical-curvature budget are specific to the Ishida--LeBrun near-critical sequence, not universal for arbitrary almost-negative-Einstein 4-manifolds. Chern--Gauss--Bonnet controls curvature integrals relative to topological numbers but does not bound `χ/Vol` in the needed direction; exact normalized negative Einstein examples already have different volume ratios. The statement that all known strict-Hitchin--Thorpe no-Einstein examples are exactly the Ishida--LeBrun geography is also withdrawn: LeBrun, Sambusetti/BCG, Kotschick, and extended-graph/simplicial-volume mechanisms form separate obstruction families. Use `workspace/plans/route_assessment_step47_entropy_degree_theorem.md` for the corrected entropy/global-volume route and keep the regularized IL theorem as an intermediate result with its analytic module still to be written self-containedly.
## Restricted negative IL gap: consolidated

Both A01 and A03 have independently consolidated the restricted
four-dimensional negative Ishida–LeBrun defect gap theorem.

- **A01** (`step45_consolidated_IL_negative_gap_proof.md`): organizes the
  proof around Proposition 3.2, a quantitative local Φ lower bound from
  compactness.  Terminal contradiction via Liouville–Rauch averaging
  against the positive lower bound.  Derdziński mechanism: Kähler–Einstein
  Weyl norm |W⁺|² = 2/3 ≠ 1/24.  54/54 structural checks; TTCS verified
  with three corrections incorporated (elliptic upgrade for Prop 3.2,
  Liouville constant renaming, coefficient-regularization completeness
  caveat).

- **A03** (`step47_consolidated_negative_IL_gap_theorem.md`): organizes
  as Module S (topology-independent smoothing) + Module O (IL spectral
  obstruction).  Terminal contradiction via min-point selection on plateau
  with Shi-estimate smooth convergence.  Derdziński mechanism:
  projector–Bochner 0 = −1/8.  157/157 algebraic checks.

The two consolidations reach the same mathematical conclusion through
slightly different proof presentations.  The key structural contribution
of A03 is identifying Module S as a reusable topology-independent
extraction tool: any 4D no-Einstein mechanism supplying a Q-controlled
nonneg density whose vanishing is locally impossible gets the same
chart-level contradiction.

### Remaining analytic caveat

TTCS identified that the ε-uniform fixed-coordinate short-time existence
and all-order compactness for the regularized flows (b_ε = χ² + ε²) is
stated but not yet independently proved as a self-contained analytic
module.  The algebraic bounds in (5.2) and the staggered weight structure
are necessary inputs, but the complete fixed-coordinate estimate package
(metric equivalence, unweighted T chain, connection-difference bounds,
time-derivative bounds) must be assembled without using frozen-complement
identities that only hold for the exact degenerate flow.  This is an
important but bounded analytic obligation, not a structural gap.

---

## Structural lessons for Yau Problem 26

### What the restricted theorem actually uses

The negative IL gap proof depends on three ingredients:

1. **Curvature-energy budget.** The Ishida–LeBrun geography gives
   ∫|Rm|²/Vol = O(1), with explicit constants from Chern–Weil and the
   calibrated volume ratio Vol/A → 32π²/9.

2. **Module S (smoothing).** From (1) and Ric ≈ −g, a degenerate cutoff
   flow produces bounded-curvature noncollapsed terminal charts on a
   positive fraction of volume, with pointwise |E| → 0 and global
   Q(T)/Vol → 0.  This module is topology-independent in dimension 4.

3. **Locally impossible Einstein profile.** The SW mixed estimate +
   Chern–Weil force a specific calibrated Weyl spectrum at any terminal
   point where Φ = 0.  Derdziński's theorem shows this spectrum is
   impossible for a smooth Einstein germ.

### What is needed beyond this family

For the full 4D negative statement, the question is: does every closed
4-manifold M without a negative Einstein metric resist tight negative
Ricci pinching?  This requires extending (1) and (3) beyond IL geography:

- **(1) is universal in dimension 4:** for any closed (M, g) with
  Ric ≈ −g, Chern–Gauss–Bonnet gives ∫|Rm|² ≈ 8π²χ(M) + 2Vol/3,
  and Vol ≈ (32π²/9)χ(M) when τ(M) ≈ 0.  The budget ∫|Rm|²/Vol
  depends on the topology only through (2χ + 3τ)/χ, which is bounded
  for Hitchin–Thorpe-compatible manifolds.

- **(3) is the hard part.** The SW obstruction is specific to the IL
  connected-sum structure.  For other no-Einstein topologies (if they
  exist with strict HT), a different mechanism would be needed to force
  a locally impossible profile.

**Important observation:** all currently known closed 4-manifolds without
Einstein metrics fall into two categories:
- HT violators (2χ ≤ 3|τ|): these already resist tight pinching by the
  universal topological obstruction.
- SW-obstructed manifolds with strict HT: these are exactly the
  Ishida–LeBrun geography.

If no other no-negative-Einstein 4-manifolds with strict HT exist, then
the restricted theorem plus the universal HT obstruction would settle
the full 4D negative statement.  The existence of such "hidden"
no-Einstein manifolds is itself an open problem in 4-manifold topology.

### Positive branch (A02)

A02 Steps 46–47 developed a conditional mode-projection vector
obstruction for noncollapsed positive 4D sequences with Kleinian/ADE
bubbles.  Key findings:

- The Γ-invariant l = 2 TT harmonic computation gives finite
  representation theory for the degeneracy locus.
- A₁ (Z₂ quotient) is the main large double-degeneracy case.
- A_k≥2 and D_k reduce to explicit scalar equations.
- E₆/E₇/E₈: the nontrivial block has W = 0, so R = (Λ/3)I is
  invertible for Λ > 0; E-type is NOT a KE double-degeneracy loophole.
- The analytic bridge H4 must be stated in dual/weak form (TT test-field
  pairing), not as a pointwise radial ODE.

This is complementary to the negative route but still conditional on
proving H4_dual.  It also does not address positive collapse (where
Myers gives diameter bounds but not noncollapse).

### Dimensions n ≥ 5

No mechanism analogous to SW, self-dual Weyl, or Derdziński exists in
higher dimensions.  The 4D proof uses:
- Self-dual/anti-self-dual Weyl decomposition (specific to n = 4)
- Seiberg–Witten invariants (specific to n = 4)
- Derdziński's conformal-Kähler theorem (specific to n = 4)
- Critical Sobolev cancellation in the Whitney product (specific to n = 4)

A higher-dimensional approach would need fundamentally different tools.

---

## Current relation to the full Yau 26 goal

| Dimension | Sign | Status |
|---|---|---|
| n = 3 | Both | Solved by Hamilton/geometrization |
| n = 4, negative | IL geography q ≥ 0 | Restricted gap theorem (A01 + A03) |
| n = 4, negative | HT violators | Universal topological obstruction |
| n = 4, negative | Other no-Einstein | Open (existence unknown) |
| n = 4, positive | Noncollapsed + Kleinian | Conditional on H4_dual (A02) |
| n = 4, positive | Collapse | Open |
| n ≥ 5 | Both | Open (no mechanism) |

The restricted negative theorem is a genuine scientific result that
rules out one important counterexample family.  Combined with the
universal HT obstruction and the observation that all known no-Einstein
4-manifolds are covered by these two results, the negative branch in
dimension 4 is close to resolution—modulo the open 4-manifold topology
question of whether other no-negative-Einstein strict-HT manifolds exist.

## Next work

The most valuable continued work, in approximate order of expected
return for the full Yau 26 goal:

1. **Close the ε-uniform compactness module** for the restricted theorem
   (the only remaining analytic caveat identified by TTCS).

2. **Investigate the 4D negative completeness question:** are there closed
   smooth 4-manifolds satisfying strict Hitchin–Thorpe, admitting no
   negative Einstein metric, but not in the IL geography?  If not, the
   restricted theorem resolves the full 4D negative branch.

3. **Build A02's H4_dual** for the positive noncollapsed route.

4. **Explore higher-dimensional mechanisms** or obstructions.

5. **Begin Lean formalization** of the restricted theorem's key modules.
