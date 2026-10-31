# Route assessment after Step 29

**STEP 30 SUPERSEDING NOTICE.** The Step 29 route assessment contains three corrected errors. First, the ordinary unweighted-\(U\) Moser replacement is not justified; the active repair is the mixed Hölder--Sobolev weighted recurrence in `notes/step30_weighted_moser_and_family_repair.md`. Second, Noether does not give \(\chi(M)=A+O(1)\) or \(K_0\to9\); the route needs and has only an \(O(A)\) Euler bound plus positive \(\operatorname{Vol}/A\) in the near-critical regime. Third, the analytic regime is \(\sigma_i/A_i\to0\), including sequences with all \(\sigma_i>0\), not only exact \(\sigma=0\). Read this assessment with those replacements.


## Key advances

1. **Simultaneous support theorem assembled** (A01 Step 29): the complete
   bootstrap chain — H₂ → β → Y → curvature pointwise → J₆ → defect
   pointwise → velocity → metric comparison — is organized with non-circular
   dependency graph (verified by topological sort).  All volume cancellations
   pass independently of collapse.

2. **Family extension** (A03 Step 29, Step 30 corrected): the calibration algebra extends to the
   entire Ishida–LeBrun no-Einstein family (σ = D − A/3 ≥ 0).  A purely
   topological gap gives a uniform margin only when σ/A is bounded below.
   Any near-pinched sequence has σ/A → 0, even if every σ_i>0, so the flow
   must treat the full near-critical regime rather than only exact σ=0.

3. **Uniform K₀ and β** (A03 Step 29, A01 verification): K₀ = Vol⁻¹∫|Rm|²
   is uniformly bounded by CGB (≤ C + O(δ²)), making β = S·H₂^{1/2} =
   Cr²√(1+K₀) a universal constant.  Volume cancels exactly.

## Corrected Moser interpretation (Step 30)

The direct comparison of ‖z_p‖₃³ with H_{3p/2} has a half-power gap: with
H_p = ∫a^{p-2}f^p and z_p = a^{(p-1)/2}f^{p/2}, ‖z_p‖₃³ carries one extra
factor a^{1/2} relative to H_{3p/2}.  This only invalidates that particular
comparison.

The active fix is the weighted mixed Hölder--Sobolev recurrence:

H_{3p/2}=∫(a^{p-2}f^p)^{1/2}z_p² ≤ H_p^{1/2}‖z_p‖₄²,

and Sobolev controls ‖z_p‖₄² by the same weighted dissipation plus r^{-2}H_p.
This yields the desired p→3p/2 recurrence with polynomial p-losses and no
ordinary unweighted gradient.  A03 Step 31 independently verified the same
structure.

The unweighted U-based Moser is withdrawn as a first-bound mechanism: the
operator is still aΔ, testing U controls only ∫a|∇|U|^{p/2}|², and the shifted
quadratic reaction is U*U rather than aU*U.  U remains valuable for
velocity/connection and shifted-curvature continuation after the weighted
curvature bound is obtained.

## Additional TTCS corrections

1. **First-exit set:** Must explicitly include H₂(t) ≤ 4H₂(0) and
   S(t) ≤ 4S(0) in the bootstrap hypotheses, not just (B1)–(B4).

2. **CGB/Euler coefficient:** Use a fixed curvature-norm convention.  Step 30 replaces the unsupported
   χ(M)=A+O(1) / K₀→9 claim with the valid Noether and connected-sum bound
   χ(M) ≤ (16/3)A + σ + 30m + 6 under minimal general-type summands and
   b_+(N)=0.  Together with two-sided Vol/A bounds and σ/A→0, this gives
   the qualitative uniform mean-energy bound K₀≤C needed by the route.

3. **Vitali thinning:** A maximal r/5-separated net does not give disjoint
   B_{2r/3} supports; bounded-degree coloring (already in Step 24) is needed.

4. **Derdziński contradiction:** Confirmed valid through the locally
   conformally Kähler + modulus conflict (|W⁺|² = 1/24 ≠ 2/3), not through
   ∇W⁺ = 0 (eigenframe could rotate).

## Remaining mathematical obligations

| Obligation | Status | Priority |
|---|---|---|
| Weighted all-p Moser/power inequality | Needed for rigorous proof; active route uses H_{3p/2}≤H_p^{1/2}||z_p||_4² | HIGH |
| CGB/Noether O(A) topology and Vol/A bounds | Qualitative K₀≤C, not K₀→9 | MEDIUM |
| Shifted-curvature Wang 4.14: expand IBP | Schematic only | HIGH |
| Support coloring: explicit degree bound | Done in Step 24 but needs check | LOW |
| Terminal pullback: Rauch constant audit | Step 28, constants verified | LOW |
| J₆ → |aE|⁶ Kato regularization | A03 described, not formalized | MEDIUM |

## Scope

The conditional theorem would cover the standard four-dimensional Ishida–LeBrun
near-critical regime (σ/A→0, m = 2 or 3, with the topology hypotheses used for
χ(M)=O(A)) if the corrected analytic bridge and support selection are proved.
A fixed positive σ/A margin is already excluded by the topological bound.

Still outside scope:
- Arbitrary 4D non-Einstein topologies
- Positive branch
- Dimensions n ≥ 5
- Full Yau-26 interval proposition
- Lean formalization

## Files

- Bootstrap theorem: `workspace/notes/step29_simultaneous_support_theorem.md`
- Weight gap fix: `workspace/scripts/step29_weight_gap_fix.py`
- Bootstrap chain verify: `workspace/scripts/step29_bootstrap_chain_verify.py`
- Family extension verify: `workspace/scripts/step29_family_extension_verify.py`
- A03 consolidated theorem:
  `Sessions/S0910A03/workspace/notes/step29_consolidated_conditional_theorem.md`
- TTCS: `trace/ttcs/results/step29_ttcs01_verifier1_integration.md`
