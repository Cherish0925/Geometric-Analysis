> **Step 40 Preceptor update.** This route assessment is superseded at the interfaces reviewed in `workspace/notes/step40_preceptor_review_step39_interfaces.md`.  The Step 39 synthesis remains useful, but Step 40 found additional analytic and geometric interfaces that still require proof beyond the DeTurck start/restart.  The full Yau proposition is equivalent in each dimension to one forcing sign branch `P_n^+ or P_n^-`; proving both signs is stronger than necessary, while refuting the proposition in one fixed dimension requires defeating both branches.\n\n
# Route assessment after Step 39

## Main construction

Step 39 assembled the complete conditional defect gap theorem for the
four-dimensional negative Ishida–LeBrun branch in one self-contained document:
`workspace/notes/step39_complete_conditional_defect_gap_theorem.md`.

This is the first time the end-to-end argument from Ishida–LeBrun hypothesis to
Derdziński contradiction has been written in a single location.  It collects
conditional pieces from A01 Steps 2–38 and A03 Steps 39–40.

## What the theorem establishes (conditional on (H1))

There exists ε₄ > 0 such that every near-critical Ishida–LeBrun four-manifold
M = X # k C̄P² with A = c₁²(X) → ∞, k/A → 1/3 has no metric with
||g⁻¹Ric + I||_{∞,op} < ε₄.  In other words, these manifolds have a uniform
negative Ricci defect gap.

The argument has seven modules:
1. Near-critical calibration (§2): mixed SW → calibrated s, |W⁺|, spectral gap
2. Support construction (§3): maximal-function good centers, BG coloring, macro-disjoint buffers
3. First-exit bootstrap (§4): K₂→B→Y→J₆ chain, Moser endpoints, continuation
4. Global Q propagation (§5): unweighted defect preserved through disjoint supports
5. Terminal recalibration (§6): int 𝔇 ≤ 119Q(T)
6. Exponential pullback (§7.1-7.2): tangent-space ball with vanishing calibration density
7. Derdziński contradiction (§7.3): calibrated Einstein germ is locally Kähler with wrong |W⁺|²

TTCS verified: (a) velocity singularity t⁻¹/³ integrable, (b) no circular
dependency, (c) no timing issue, (d) Q summation works for disjoint buffers,
(e) DeTurck +g modification is plausible but requires explicit tame verification.
Script: 41/41 pass.

## Former H1 framing, superseded by Step 40 review

The per-datum transported-coefficient DeTurck existence/restart for
∂_t g = -2χ²(Ric+g) is hypothesis (H1).  This is Yang's Theorem 4.1 with the
normalization +g as a zeroth-order perturbation.  It does not change the
degenerate parabolic principal symbol, the DeTurck strict parabolicity where
χ > 0, or the regularization argument a → a+ε.

TTCS described (H1) as plausible but not yet proved from the available text. Step 40 preserves the correct gauge architecture while requiring the normalized Yang adaptation to include the actual ε-independent tame estimates, regularization limit, local uniqueness, and restart proof written with the transported coefficient.

## Earlier H2 framing, superseded by Step 40 review

The zero-order unweighted T ∈ L^q propagation was recorded in Step 39 as discharged by Step 35. Step 40 found that Step 35 supplies the key signed Hessian-a tensor mechanism but not yet the full unweighted T lemma with G, normalization, stationary-region terms, and the |U| bounded reaction written out. Equation (4.12) remains a plausible target lemma, not an established theorem.

## A02 update (message #353)

A02 Step 41 is a Preceptor review of the positive toric diagonal route.  Key
finding: the Step 40 product linearization needs correction (alpha equation
derivation missing; sin x boundary data wrong at fixed Lambda=1).  Corrected
FEM gives m=6 regular polygon eigenvalue probe at only 1.84% defect, not 68.7%.
A02 recommends downweighting constant-K toric refinement and pivoting to Route A
(cone indicial/Wronskian on C(S³/Z₂)) or variable-curvature m=6 compatibility.
The positive toric work is independent of the negative flow route.

## Complete dependency table

| Module | Status | Reference | Hypothesis |
|:---|:---:|:---|:---:|
| Near-critical calibration | established | §2 | — |
| Calibrated profiles | established | §2.4–2.5 | — |
| Derdziński forbidden germ | established | §7.3 | — |
| Support construction | needs repair | §3, Lemma 3.1 + Step 40 review | remove Hessian bound, add 7r≤R, global cutoff, inner centers |
| Curvature power inequality | conditional | §4.4 Step A | (H1) |
| Fixed-exponent K₂→B→Y→J₆ | conditional | §4.4 Steps B–D | (H1) |
| General-p defect inequality | conditional | §4.4 Step E | (H1) |
| Weighted Moser endpoints | conditional | §4.4 Step F | (H1) |
| Zero-order T ∈ L^q | needs written proof | §4.5 (4.12) + Step 40 review | full unweighted T lemma |
| All-order continuation | conditional on structural equations | §4.5 Step H + A03 Step 40 | derive U/T/cutoff equations and DeTurck |
| First-exit closure | conditional | §4.7 | (H1) |
| Global Q propagation | conditional | §5 | (H1) |
| Terminal recalibration | conditional with topology assumptions | §6 + Step 40 review | require q≥0 or q_- error and terminal monopole choice |
| Exponential pullback | needs Step 28 strong version | §7.1–7.2 + Step 28 | inner centers, Liouville averaging, strong W^{2,p} |
| Defect gap theorem | **conditional on (H1)** | **Thm 1.1** | **(H1)** |

Step 40 found that this dependency table understates the remaining mathematical interfaces: support cutoff regularity, homogeneous K₂ propagation, zero-order unweighted T propagation, full normalized shifted evolution formulae, transported-DeTurck tame estimates, terminal topology/sign assumptions, and strong terminal pullback convergence still need to be written before the restricted theorem is established.

## What is NOT addressed

1. **Positive branch**: open (A02's toric work is exploratory)
2. **Arbitrary 4-manifold topology**: the monopole structure is Ishida–LeBrun specific
3. **Dimensions n ≥ 5**: no SW/W⁺/Derdziński analog exists
4. **Dimension-only constants**: ε₄ depends on K̄₀ and r, not just n=4
5. **Lean formalization**: no formalizable theorem yet
6. **Full Yau Problem 26**: for each n it suffices to prove one forcing sign branch P_n^+ or P_n^-; refutation in one fixed n must defeat both branches; all n ≥ 2 and Lean formalization remain open.

## Next work priorities

1. **Repair the interfaces identified in Step 40**: write the normalized Yang adaptation with tame estimates, derive the shifted U/T/cutoff-jet structural equations and the zero-order unweighted T lemma, replace the support and K₂ sections by their collapse-sensitive forms, and restore the Step 28 terminal passage.
2. **Extend topology**: determine whether the SW inequality can be replaced by
   a more general 4D obstruction covering non-Ishida–LeBrun manifolds.
3. **Positive branch**: A02's indicial/Wronskian route on C(S³/Z₂) may provide
   complementary evidence.
4. **Lean formalization**: wait until the restricted theorem has a complete mathematical proof; current materials are not ready for formalization.

## Files produced

- `workspace/notes/step39_complete_conditional_defect_gap_theorem.md` (main theorem)
- `workspace/scripts/step39_defect_gap_assembly_verify.py` (41/41 pass)
- `trace/ttcs/results/step39_ttcs01_verifier1_integration.md` (TTCS verification)
- This file: `workspace/plans/route_assessment_step39.md`
