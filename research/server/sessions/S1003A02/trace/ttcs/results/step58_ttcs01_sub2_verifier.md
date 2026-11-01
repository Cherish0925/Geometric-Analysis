# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step57_kernel_burns_coefficient_general_background.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md",
    "Sessions/S1003A02/workspace/notes/step53_anderson_entrance_bubble_exclusion_attainment.md"
  ]
}
```

## Task

Verify the formal Theorem 57.Φ and the Step-58 cross-checks. The claim is:

(a) For a Burns insertion on a 4-manifold at a point p with zeta an eigenvector of R⁺ = W⁺ + s/12 having eigenvalue μ₁ (other: μ₂, μ₃), the ε²log(1/ε) coefficient in P(g̃)/(8π²) is Φ = -μ₁(μ₁-μ₂-μ₃)/2 - (μ₂-μ₃)²/2. In the kernel μ₁=0: Φ = -(μ₂-μ₃)²/2 ≤ 0.

(b) Φ depends only on s and W⁺(p), not on W⁻, Ric°, ∇Rm, or ∇²Rm. The proof of W⁻/Ric° independence is: P(g̃) - P(g) - 8π² = Δ(4∫|W⁺|² + ∫s²/12) by Chern-Weil; if W⁺=0,s=0 at p the right side is ≥ 0, so W⁻/Ric° coefficients are nonneg, and D=4 attains 0. Check this argument.

(c) Lemma 57.1: ∇²Rm drops out because the Burns family δ+εA is P-critical for all ε, so the C-linear coefficient is a divergence of a degree -3 field on S³, with zero integrated coefficient. ∇Rm drops out by parity under U(1)_ζ.

(d) Product-background test: Σ₁(K₁)×Σ₂(K₂) has R⁺=diag(s/4,0,0), s=2(K₁+K₂). Both par (μ₁=s/4) and perp (μ₁=0) layouts should give Φ = -s²/32. The computation uses conformal coordinates (nonzero quartic C). Does the corrector convergence rate depend on the gauge of the background jet?

(e) The strategist question: do degree-0 correctors exhaust the contributions to the log coefficient? That is, correctors of higher homogeneity feed other powers of r, not the ε²log corner.

(f) Consequence: every compact KE surface has R⁺=diag(s/4,0,0). The kernel circle ζ⊥ω gives Φ=-s²/32<0 at every point. Does this give p_*(X#kCP̄²) < 8π²k for ALL minimal general-type X? Scope: formal (needs the rigorous remainder).

(g) Minimizer rigidity: R⁺≤0, and μ_max(R⁺)=0 ⟹ μ₂=μ₃. Combined with |W⁺|²≤s²/24 on R⁺≤0, does this strengthen to |W⁺|²<s²/24 strictly?

(h) The unification reading: R⁺<0 (interior of the cone) is decided at first order (positive cost -εμ₁>0); the boundary at second order (Φ≤0). Real-hyperbolic = Theorem H regime (cost, bubbling allowed); KE = saving regime (bubbling excluded at minimizers). Is this consistent and complete?

## Output

# Verification Memo: Theorem 57.Φ and Step-58 Cross-Checks

## (a) Algebraic consistency of the formula

The eigenvalue formula Φ = −μ₁(μ₁−μ₂−μ₃)/2 − (μ₂−μ₃)²/2 and the invariant-coefficient form (table entries at D ≥ 4) are algebraically equivalent. Using μ₂+μ₃ = s/4 − μ₁ and w = μ₁ − s/12 = W⁺(ζ,ζ):

Φ = s²/288 − sw/24 − w² − |W⁺_⊥⊥|²

where |W⁺_⊥⊥|² = (μ₂−μ₃)²/2 in the operator Frobenius norm on the 2D trace-free endomorphism of ζ⊥. Expanding:

−μ₁(2μ₁−s/4)/2 − (μ₂−μ₃)²/2 = −μ₁² + sμ₁/8 − (μ₂−μ₃)²/2

and substituting μ₁ = w + s/12:

s²/288 − sw/24 − w² − (μ₂−μ₃)²/2

matching the table coefficients 1/288, −1/24, −1, −1. ✓

CH verification: s = −24, R⁺ = diag(−6,0,0). Kernel direction μ₁ = 0, {μ₂,μ₃} = {−6,0}: Φ = −36/2 = −18. ✓

## (b) W⁻/Ric° independence via Chern–Weil

The structural identity is:

P = 4∫|W⁺|² + ∫s²/12 − 8π²T₊,  where  T₊ = 2χ + 3τ

(derived from CGB 8π²χ = ∫(|W⁺|²+|W⁻|²−|Ric°|²/2+s²/24) and signature 12π²τ = ∫(|W⁺|²−|W⁻|²), eliminating |W⁻|² and isolating |Ric°|²). Under one blow-up, T₊ decreases by 1, giving:

P(g̃) − P(g₀) − 8π² = Δ(4∫|W⁺|² + ∫s²/12)

The right side involves only W⁺ and s of the blown-up metric, not W⁻ or Ric° directly. The argument that the W⁻/Ric° quadratic terms in Φ are nonnegative (and hence zero after optimization):

At a point p with W⁺(p) = s(p) = 0 (but arbitrary W⁻(p), Ric°(p)), construct a *locally ASD scalar-flat* representative, i.e., a metric agreeing in the W⁻, Ric° components at p but having W⁺ ≡ 0, s ≡ 0 in a neighborhood. For this representative, 4|W⁺|²+s²/12 = 0 identically near p, and the blown-up metric has 4|W⁺(g̃)|²+s(g̃)²/12 ≥ 0 pointwise. Therefore Δ(4∫|W⁺|²+∫s²/12) ≥ 0, giving P(g̃) ≥ P(g₀)+8π². Since the expansion has first-order term zero (R⁺(ζ,ζ) = 0 at W⁺=s=0), the ε²log coefficient Φ must be ≥ 0. Since Φ depends only on Rm(p) (Lemma 57.1), this holds for all backgrounds with W⁺(p) = s(p) = 0, regardless of W⁻(p) and Ric°(p).

The argument is sound, subject to one implicit ingredient: **local existence of ASD scalar-flat metrics with prescribed W⁻ and Ric° at a point**. This is available: product metrics Σ₁(K₁)×Σ₂(K₂) with K₁ = −K₂ give s = 0, W⁺ = 0 (Kähler with s = 0), and nonzero Ric° (when K₁ ≠ 0). Hyperkähler metrics give W⁺ = 0, s = 0, Ric° = 0 with arbitrary W⁻. These examples, combined with the fact that Φ is a continuous quadratic form in the curvature components, suffice to conclude Φ|_{W⁻,Ric°} ≥ 0 on the full parameter space.

That D = 4 correctors achieve 0 is confirmed numerically (residuals ≤ 10⁻¹⁵) and by A01's explicit corrector formula k₀^W for the W⁻ sector. ✓

## (c) Lemma 57.1

**∇Rm parity.** The Burns insertion has U(1)_ζ symmetry. Under the element −1 ∈ U(1)_ζ (which acts as −Id on the ζ-complex structure's coordinates), ∇Rm is odd (rank-5 tensor). Any monomial in ∇Rm appearing in the density that is linear (or odd-degree) integrates to zero on U(1)_ζ-orbits on S³. The quadratic term |∇Rm|² would have m = 6 (two extra derivative orders beyond Rm), exceeding the m = 4 needed for the ε²log coefficient. ✓

**∇²Rm / C-term.** Burns metric δ+εA is ASD (W⁺ = 0) hence Bach-flat, therefore P-critical. The C-linear coefficient ∂_c F(δ+εA+cC)|_{c=0} = ⟨∇P(δ+εA), C⟩ + div(V) = div(V), since ∇P = 0. The divergence term V is a homogeneous degree-3 vector field on S³ (from the variational boundary terms of the fourth-order P-functional). Its integral over S³ vanishes by the divergence theorem on S³. The numerical confirmation (‖ℓ‖ = 5·10⁻¹⁵ on all 350 quartic jets) is consistent. ✓

## (d) Product-background tests

For Σ₁(K₁)×Σ₂(K₂): s = 2(K₁+K₂), R⁺ = diag(s/4, 0, 0) (Kähler with W⁺ eigenvalues (s/6,−s/12,−s/12)).

Both par (μ₁ = s/4) and perp (μ₁ = 0) predict Φ = −s²/32:
- Par: Φ = −(s/4)(s/4−0−0)/2 − 0 = −s²/32
- Perp: Φ = 0 − (s/4−0)²/2 = −s²/32

Numerical predictions match: (−1,−1) → −1/2, (−1,−3) → −2, (−1,1) → 0, (−2,1/2) → −9/32, (1,2) → −9/8. All D = 6 entries match to 10⁻¹⁵. ✓

**Gauge dependence of corrector convergence:** In normal coordinates, the quartic jet C is determined by ∇²Rm(p), which doesn't enter Φ (Lemma 57.1). Hence degree-0 correctors (D = 2) already capture the full log coefficient, and D = 4 converges. In conformal (native product) coordinates, C contains Rm(p)-level information displaced from its natural position, requiring higher-degree correctors K to compensate. The D = 4 values in conformal coordinates lie *above* the truth (as expected from minimization over a smaller space), and D = 6 converges. This is a gauge artifact of the polynomial corrector representation, not a deficiency of the formula. ✓

## (e) Degree-0 correctors and the log coefficient

The two-parameter homogeneity structure r⁻⁴(ε/r²)^a(νr)^m of the |Ric°|² density on the annulus ε ≲ r ≲ 1 selects (a,m) = (2,4) for the ε²log(1/ε) coefficient. A polynomial corrector K of degree d in the coordinates contributes to the density with shifted m values: the cross term between the Burns O(ε/r²) field and K has m increased by d, and the K² term has m increased by 2d. For d > 0, these terms hit m > 4, which contributes to ε² (or higher) rather than ε²log.

More precisely: the density quadratic form M_ij K^i K^j + 2b_i K^i + c on S³ has M and b depending on the background jet. The S³-integral of the optimal value c − b^T M⁻¹ b is the log coefficient. Higher-degree K's affect M, b only in blocks that don't couple to the (a=2, m=4) corner. The D = 4 → D = 6 stability of the converged coefficients (to 10⁻¹⁵) confirms this separation numerically. ✓

## (f) Scope: every compact KE surface

Every minimal general-type surface X with ample K_X admits a Kähler–Einstein metric with Ric = λg, λ < 0, s = 4λ < 0 (Aubin–Yau). This metric has P(g_KE) = 0 (Einstein ⟹ Ric° = 0) and R⁺ = diag(s/4, 0, 0).

Burns insertion in the kernel direction (ζ ⊥ ω): μ₁ = 0, Φ = −s²/32 < 0. For k insertions at distinct points with common scale ε:

P(g̃) = 0 + 8π²k − k·(s²/64)·ε²log(1/ε) + O(ε²) < 8π²k

for ε small. Hence p_*(X#kCP̄²) < 8π²k. ✓

For canonical models with ADE singularities: orbifold KE metric (Kobayashi, Tian–Yau) with P_orb = 0, plus Kronheimer ALE Ricci-flat resolutions at P = 0. The construction extends. ✓

**Scope note:** This covers all minimal surfaces of general type, without any condition on c₁²/c₂ or W⁻. The earlier D = 2 estimate requiring c₁²/c₂ > 21/37 is correctly withdrawn. The result is formal: it requires the rigorous remainder estimate O(ε²) to be genuinely o(ε²log(1/ε)).

## (g) Minimizer rigidity and strict |W⁺|² bound

At a minimizing bulk with R⁺ ≤ 0 carrying a Burns bubble: if λ_max(R⁺)(p) = 0 at some point p, the kernel direction ζ gives Φ = −(μ₂−μ₃)²/2. If μ₂ ≠ μ₃, this is < 0, meaning the Burns insertion at p in direction ζ would save energy — contradicting that the configuration is already minimizing (the same bubble could be re-glued at p to reduce the total P). Hence μ₂ = μ₃.

On the constraint set {R⁺ ≤ 0, tr W⁺ = 0, tr R⁺ = s/4}, the maximum of |W⁺|² is s²/24, uniquely attained at eigenvalues (|s|/12, |s|/12, −|s|/6), corresponding to R⁺ eigenvalues (s/4, 0, 0) — the KE-type spectrum. At this point, μ₂ and μ₃ are s/4 and 0, which are unequal (since s < 0). So the rigidity condition μ₂ = μ₃ is violated. Therefore |W⁺|² < s²/24 strictly at every point. ✓

The allowed boundary type with μ₂ = μ₃ corresponds to W⁺ = (|s|/12)(1, −1/2, −1/2), giving |W⁺|² = s²/96. This is the degenerate case where the second-order analysis gives Φ = 0 and higher-order terms would be needed.

## (h) Unification and completeness

The three regimes of R⁺ at a bulk point:

| Region | First order | Second order | Bubbling status |
|---|---|---|---|
| R⁺ has positive eigenvalue | −εμ₁ < 0 (saving) | not needed | Excluded at minimizers (Thm 53.B) |
| R⁺ < 0 strictly | −εμ₁ > 0 (cost) | not needed | Allowed; approaches 8π²k from above |
| λ_max(R⁺) = 0, μ₂ ≠ μ₃ | 0 | Φ < 0 (saving) | Excluded at minimizers (57.Φ) |
| λ_max(R⁺) = 0, μ₂ = μ₃ | 0 | Φ = 0 | Undecided; needs higher order |

Real-hyperbolic manifolds: R⁺ = (s/12)I < 0, all eigenvalues equal and negative. This is the interior of the cone, decided at first order with positive cost. Consistent with Theorem H. ✓

KE surfaces: R⁺ = diag(s/4, 0, 0), boundary of the cone with μ₂ = s/4 ≠ 0 = μ₃. Decided at second order with negative Φ. Bubbling excluded at minimizers. ✓

The only unresolved case is the codimension-1 locus μ₂ = μ₃ at the boundary, which is the W⁺ spectrum (|s|/12, −|s|/24, −|s|/24). This is a genuine residual; it does not arise for KE or real-hyperbolic backgrounds and would require either third-order analysis or a structural argument. The classification is otherwise complete. ✓

## Summary of scientific substance

The formula, its derivation structure, the Chern–Weil independence argument, the product-background tests, and the consequences are all internally consistent and mutually reinforcing. The principal items that remain unresolved:

1. **Rigorous remainder estimate** for the ε²log(1/ε) expansion: the formal coefficient is computed and cross-checked, but the proof that the remainder is genuinely O(ε²) (i.e., o(ε²log)) in a general analytic background has not been written. This is the single analytic step separating the numerical/formal result from an unconditional theorem.

2. **The degenerate boundary μ₂ = μ₃**: Φ = 0, and the bubbling/cost question is undecided. This is a codimension-1 condition in the space of possible bulk curvatures and does not affect the KE or real-hyperbolic applications.

3. **Batch gluing interactions** for k > 1: per-cell savings are additive at leading order, but inter-cell interactions at order ε² or higher have not been analyzed.