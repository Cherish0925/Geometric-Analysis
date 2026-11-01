# TTCS Independent Branch Record

```json
{
  "step_id": 19,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step19_whitney_tensor_estimate.md",
    "Sessions/S0910A01/workspace/scripts/step19_whitney_energy_transfer.py",
    "Sessions/S0910A01/workspace/scripts/step19_tensor_whitney_absorption.py",
    "Sessions/S0910A01/workspace/notes/step18_weighted_cutoff_system.md",
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md"
  ]
}
```

## Task

Verify the mathematical correctness of the Whitney-ball reduction for the degenerate cutoff-flow curvature estimate. The construction claims: (1) On Whitney balls B_{crχ₀}(y) in the support of a cutoff flow ∂_tg = -2χ²(Ric+g), Bishop-Gromov comparison transfers total support energy ∫_Ω|Rm|² ≤ CK₀Vol(Ω) to Whitney-ball Li smallness ℓ⁴ fint|Rm|² ≤ CK₀r⁴ with the χ₀ canceling. (2) The Sobolev product A_ℓ||Rm||₂ ≤ C√K₀ r² is independent of χ₀ and collapsed volume. (3) On each Whitney ball, a≈a₀=χ₀², so the operator is non-degenerate; time θr² provides smoothing at ALL Whitney levels simultaneously because the diffusion-to-ball ratio √θ/c is χ₀-independent. (4) The Moser iteration gives |aRm|≤C/t with C independent of χ₀. (5) For U=aE and p>2, ||U||_∞ ≤ Ca₀^{1-2/p}t^{-2/p}||E(0)||_p, so the weighted defect improves as a₀→0. Check: (a) Is the BG comparison in Section 3 correct — does ℓ⁴/Vol(B_ℓ) exactly cancel the χ₀⁴ in ℓ⁴? (b) Does the Sobolev product really cancel the cutoff level algebraically? (c) Is the time matching correct — does physical time θr² suffice for all Whitney levels? (d) Are there hidden obstacles: does the cutoff perturbation (a-a₀)E on the Whitney ball remain absorbable through the Moser iteration? (e) Does the finite-overlap Whitney cover create cumulative constants that could depend on χ₀? (f) Is the claim that ∇²a can be fully removed by integration by parts in the tensor energy correct?

## Output

## Verifier Memo: Whitney-ball reduction for the degenerate cutoff-flow curvature estimate

I reworked the geometry, the Bishop–Gromov transfer, the Sobolev product, the diffusion-time matching, the cover multiplicity, the perturbation size, and the integration-by-parts structure. The three cancellations that carry the reduction — (a), (b), (c) — are mathematically correct, and the cover argument (e) is sound. Two places contain a genuine mis-statement of order (the size of the cutoff perturbation, and the size of the localization coefficient), which do not break the argument but change *why* it works. The heaviest unverified content sits in (f): the full tensor derivation for curvature is asserted by analogy and produces a defect-gradient coupling that the isolated Section 6 inequality omits.

---

### (a) Bishop–Gromov transfer: the χ₀⁴ cancellation is correct

The comparison is set up in the right direction. With `y ∈ Ω = B_{5r}(p_j)`, one has `Ω ⊂ B_{10r}(y)`, and volume-ratio monotonicity under `Ric ≥ -(n-1)` gives
`Vol(Ω)/Vol(B_ℓ(y)) ≤ Vol(B_{10r}(y))/Vol(B_ℓ(y)) ≤ V_{-1}(10r)/V_{-1}(ℓ)`.
Then `ℓ⁴ fint_{B_ℓ}|Rm|² ≤ ℓ⁴ K₀ V_{-1}(10r)/V_{-1}(ℓ)`. For `ℓ = crχ₀ ≤ r` small, `V_{-1}(ρ) = ω₃∫₀^ρ sinh³ ≈ ω₃ρ⁴/4`, so the ratio `≈ (10r/ℓ)⁴` and the `ℓ⁴` (hence `χ₀⁴`) cancels, leaving `~10⁴ K₀ r⁴`, independent of χ₀. The lower bound `V_{-1}(ℓ) ≥ ω₃ℓ⁴/4` (from `sinh³ t ≥ t³`) and `V_{-1}(10r) ≤ ω₃(10r)⁴/4·(1+O(r²))` make the constant uniform, not merely asymptotic. **This is correct.** The transfer is conditional on (H2) energy persistence and on transferring `Ric ≥ -(n-1)` from `g₀` to `g(t)` through (H1); both are legitimately treated as bootstrap inputs.

One notational item to unify: the scripts use `K₀ = 15100` as a *density* `fint_Ω|Rm|²` (units `L⁻⁴`), while the Section 11 theorem writes the input as the *dimensionless* `r⁴ fint_{B_{6r}}|Rm|² ≤ K₀`. These are two different objects (`K₀^dens · r⁴ = K₀^dimless ≈ 1.22e-6`). The arithmetic is consistent once dimensions are tracked, but the two symbols should be one. The real smallness driving everything is the scale-invariant local energy `r⁴ fint_{B_{6r}}|Rm|² ≈ 10⁻⁶`; the `10⁴` is a fixed geometric amplification, and the good-point/maximal-function selection must genuinely deliver such points from the Chern–Weil/Noether budget.

### (b) Sobolev product: cancellation is correct

`A_ℓ‖Rm‖₂ ≤ (ℓ²/Vol(B_ℓ)^{1/2})(K₀Vol(Ω))^{1/2} = ℓ²√K₀ (Vol(Ω)/Vol(B_ℓ))^{1/2} ≤ ℓ²√K₀(10r/ℓ)² = 100√K₀ r²`. The `ℓ²` cancels the volume ratio, χ₀ disappears, and this is algebraically the square-root of (a). Numerics check: `100·√15100·0.003² = 0.111`. **Correct.**

Notation to reconcile across notes: Step 19 uses `A_ℓ` for the *squared* Sobolev constant (`‖·‖₄² ≤ A_ℓ(…)`, so `A_ℓ ~ ℓ²/Vol^{1/2}`), whereas Step 18 Eq. (9) uses `A_α` for the *non-squared* constant (`‖·‖₄ ≤ A_α(…)`, `A_α ~ r/Vol^{1/4}`). They are self-consistent within each note (`A_ℓ = A_α²`) but a reader crossing between them will double-count powers of the volume unless this is stated.

### (c) Diffusion-time matching: correct, and the apparent tension is not real

The effective operator on `B_ℓ(y)` is `≈ a₀Δ = χ₀²Δ`. The diffusion-length-to-radius ratio at physical time `t = θr²` is `√(a₀t)/ℓ = χ₀√θ r/(crχ₀) = √θ/c`, independent of χ₀. Containment `√θ/c ≤ 1/2` gives `θ ≤ c²/4`. **Correct, and simultaneous over all levels.**

I checked the one point that could have bitten: the Li mean-value estimate on `B_ℓ` with operator `a₀Δ` is valid for `0 < t ≤ τ := ℓ²/a₀ = c²r²`, and we evaluate at `t = θr² ≤ (c²/4)r² = τ/4 < τ`. So the smoothing estimate `|Rm(x,t)| ≤ C(a₀t)⁻¹(ℓ⁴fint|Rm|²)^{1/2}` holds at the terminal time; one needs `t ≤ τ` (validity), not `t ≥ τ` (completion). Multiplying by `a ≈ a₀` gives `|aRm| ≤ C/t` with `C ≈ 0.11`, χ₀-independent. **Correct.**

Downstream magnitude worth recording: at the terminal time on the plateau (`χ=1`, `a=1`), `|Rm| ≤ 0.11/(θr²) ≈ 5·10⁶`. The scale-invariant content `t|Rm| ≤ 0.11 < 1` is what matters, giving harmonic charts at scale `√t = √θ·r ≈ 1.5·10⁻⁴`. This is a legitimate but very small controlled scale; the Cheeger–Naber harmonic-radius step in the Section 13 chain must be stated at that scale, not at scale `r`.

### (d) The `(a−a₀)E` perturbation: the order is mis-stated, but the operator is uniformly elliptic

Section 5 states the perturbation is `O(c²)a₀|E|`. This is **incorrect by one order**. Directly, `a/a₀ = (χ/χ₀)² = (1 + O(Lc))² = 1 + 2Lc + O(c²)`, so `|a−a₀| ≤ Lc(2+Lc)a₀`, which for `L=2, c=0.1` is `≤ 0.44 a₀` — an `O(Lc)=O(c)` variation, not `O(c²)`. The stated `[0.64,1.44]` band in Section 2 already contradicts the `O(c²)` phrasing (a 44% swing).

This does not damage the reduction, but it changes the mechanism. A 44% swing is **not** a small perturbation to be absorbed; it is a bounded-ratio ellipticity. The correct statement is that `aΔ` restricted to `B_ℓ(y)` is uniformly elliptic with ratio `(1+Lc)²/(1−Lc)² = 2.25`, χ₀-independent, so Moser/De Giorgi constants depend only on this fixed ratio, not on χ₀. The "effective time rescaling `t̃ = a₀t` reducing to Δ" should be presented as *uniform ellipticity with a fixed ratio*, not as a `c²`-small correction to the constant-coefficient heat equation. I recommend replacing the `O(c²)` sentence with the ellipticity-ratio statement; otherwise a later reader will try to make `c²` small and shrink `ℓ` unnecessarily.

### (e) Finite-overlap cover: no χ₀-dependent accumulation

The overlap multiplicity `N(c,L,n)` is the doubling/Besicovitch constant of the cover; under `Ric ≥ -(n-1)` it is dimensional and χ₀-independent. Across dyadic levels `{χ ~ 2⁻ᵏ}`, `|∇χ| ≤ L/r` forces `χ` to vary by only `Lc·2⁻ᵏ` across a level-`k` ball, so only adjacent levels can overlap — bounded multiplicity survives. **Correct.**

The structural point I verified: near the zero set of χ there are infinitely many Whitney balls (χ₀→0), so one must confirm the coupled energy system closes over an infinite, locally finite graph. Summing `Ḣ_α + c'(…) ≤ Cr⁻²Σ_{β~α}H_β` gives `d/dt ΣH_α ≤ CN r⁻² Σ H_α`, and with the localization coefficient (see next paragraph) this is `exp(CNθ/c²)`; with `θ ≤ c²/4`, the growth is `exp(CN/4)`, a fixed dimensional constant. Because total initial energy `ΣH_α(0) ≤ K₀Vol(Ω) < ∞`, the sum closes despite infinitely many nodes. **No cumulative χ₀-dependence.** The unweighted `|Rm| = |aRm|/a ≤ C/(χ₀²t)` does blow up as χ₀→0, consistent with the design (only weighted curvature is controlled near the zero set; the plateau `χ=1` is where genuine curvature bounds live).

Localization bookkeeping to fix in Section 6: the term written as `C₁r⁻²∫η²|Rm|²` actually has two contributions — the cutoff gradient `η²|∇χ|²|Rm|² ~ r⁻²` and the Whitney localization `a|∇η|²|Rm|² ~ a₀/ℓ² = 1/(c²r²)`. The dominant one is `c⁻²r⁻²`, not `r⁻²`. This is exactly compensated by `θ ≤ c²/4` (Gronwall factor `exp(Cθ/c²) = O(1)`), so the closure is intact, but Section 6 as written understates the coefficient by `c⁻²` and hides the reason the time budget must be `c²`-small. The `θ ≤ c²/4` condition is thus doing double duty (containment *and* Gronwall control); this should be said.

### (f) Removal of ∇²a by integration by parts: asserted, not derived, and it induces a defect-gradient coupling

For the **defect** equation this is genuinely established: A03 Eqs. (2)–(4) show `a(Δa)E + 2a∇a·∇E` cancels against the commutator in `aΔ(aE)`, and Eq. (8) integrates the residual `∇²a` once into first-derivative terms plus `da*dη*wᵖ`. That derivation is explicit and I have no objection to it.

For the **curvature** equation, Section 6 asserts the same by analogy, and Section 12(i) itself records that the full derivation "must be written out" — so this is the acknowledged unverified core, not a completed step. Working the integration by parts of the load-bearing term `∫⟨∇²a·E, Rm⟩η²`:
`= −∫⟨∇a·∇E, Rm⟩η² − ∫⟨∇a·E, ∇Rm⟩η² − ∫⟨∇a·E, Rm⟩·2η∇η`.

- The middle term `∇a·E·∇Rm` absorbs into the **curvature** dissipation `ε∫a|∇Rm|²` plus `C(|∇a|²/a)|E|² = 4|∇χ|²|E|²`, a source `≲ r⁻²P` (defect energy). Coupled, fine.
- The first term `∇a·∇E·Rm` contains `∇E`, which the curvature dissipation does **not** control. Young sends it to `ε∫a|∇E|² + C(|∇a|²/a)|Rm|²`, i.e., it must be absorbed by the **defect** gradient dissipation `∫a|∇E|²` and leaves `r⁻²|Rm|²`.

Consequence: the honest curvature energy inequality is **not** the isolated form in Section 6 (which lists only `C₃δ∫η²a|Rm|²` as E-coupling). It necessarily contains the defect gradient dissipation and must be run as the coupled quantity `H_α = R_α + κP_α` from Step 18 §5 / A03 §5. The claim in Section 6 that "the reaction term (C₂) is the only term requiring Sobolev absorption" understates the situation: the `∇²a` term forces the curvature–defect coupling before any Sobolev step. This is the single most important thing to write out explicitly; the reduction's assertion "None of (i)–(iv) involves the degeneracy" is defensible (once on a Whitney ball the operator is uniformly elliptic), but the coupled tensor inequality is where the residual analytic content actually lives, and it is heavier than "standard."

### Cross-note consistency on the Moser iteration to L∞ (Section 7)

Section 7 states the curvature iteration converges to `L∞` "in the standard fashion," while A03 §4 warns the defect iteration cannot be pushed to `p=∞` at fixed threshold ("coefficient `~ p√ε`"). These are **not** in conflict, and it is worth recording why: for `|Rm|` the reaction at exponent `p` is `∫f^{2p+1} = ∫f·(fᵖ)²`, whose Sobolev absorption coefficient is `A_ℓ‖f‖_{L^{n/2}} = A_ℓ‖Rm‖_{L²}` in `n=4` — **`p`-independent**, because `n/2 = 2` is exactly the critical exponent. This is Li's Theorem 3.4 setting and it does close with the single smallness `0.111 < c`. A03's `p`-growth obstruction is specific to the *defect* `U = aE`, which is not curvature and does not sit at the critical exponent, hence the two-stage (fixed-`p` + curvature-as-potential) route in A03 §5, correctly reused in Step 19 §8. Section 7 should note that the free iteration to `L∞` is special to dimension 4 / the critical exponent, matching Step 18 §9's remark that other dimensions need an independent `L^{n/2}` input.

### What remains unresolved, stated as substance

1. **Full tensor curvature energy inequality with all `∇²a` contractions integrated by parts**, exhibited as the coupled `H_α = R_α + κP_α` system including the `∫a|∇E|²` absorption forced by the `∇a·∇E·Rm` term. This is the actual analytic object; the notes treat it as bookkeeping but the curvature–defect coupling is intrinsic, not optional.
2. **Energy persistence `R_W(t) ≤ 2R_W(0)`** (Section 7 input, items ii–iv): the Moser output presupposes it, and it must come out of the same first-exit continuation, over the infinite Whitney graph, with the `exp(CN/4)` total-energy bound made rigorous.
3. **Unweighted `Q(t) = ∫|E|²`** (Step 18 §9): correctly identified as not derivable from any weighted pointwise bound where `a→0`; it needs its own summed energy inequality. This is the quantity the λ<0 LeBrun/Ishida–LeBrun recalibration actually consumes, so its independent control is not decorative.
4. **The `O(c)` vs `O(c²)` correction** and the `c⁻²` localization coefficient should be propagated into the constants so the `θ ≤ c²/4` condition is seen to control both containment and Gronwall growth.

Net: the Whitney reduction correctly removes the *conceptual* degeneracy — on adapted balls the operator is uniformly elliptic with χ₀-independent ratio, and all three cancellations (BG, Sobolev, diffusion-time) are exact. What is asserted rather than derived is the coupled tensor energy inequality for curvature (f) and the persistence/closure that feed the Moser step; these are non-degenerate but genuinely coupled and are the content on which the Section 13 chain rests.