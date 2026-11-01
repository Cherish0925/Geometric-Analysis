# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step39_complete_conditional_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step39.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A03/workspace/notes/step37_transported_deturck_existence.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step41_continuation_criterion_and_first_exit_assembly.md",
    "Sessions/S0910A01/trace/ttcs/results/step39_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Critically verify the assembled four-dimensional negative Ishida--LeBrun defect-gap theorem and A03's claimed discharge of H1, focusing only on mathematical interfaces that could invalidate the proof. User goal is the full Yau Problem 26, but the artifact under review is the restricted negative-family theorem. Read the supplied files and give a direct scientific memo addressing: (1) whether Step39's support Lemma 3.1 proves all cutoff regularity it uses, especially Hessian/higher jets under only Ricci lower bound and mean curvature energy; (2) whether the K2 self-improvement with any additive C0*T is homogeneous enough in collapsed or tiny-support regimes; (3) whether A03 Step40/Step41 sufficiently verify the normalized weighted-U and unweighted-T evolution interfaces, including G, normalization, connection variation, and zero-order T propagation, or still leave structural equations to derive; (4) whether the transported DeTurck existence/restart proof is a complete theorem or a plausible adaptation needing detailed tame estimates; (5) whether terminal recalibration requires q>=0 and selected monopole class with (a^+)^2>=A, and whether Step39's theorem statement says this clearly; (6) whether the exponential-pullback/terminal compactness passage must use inner plateau centers, Liouville averaging on a center set, and strong finite-W^{2,p} convergence rather than weak convergence or Lipschitz-in-metric claims. Conclude what should be repaired next to turn the restricted theorem into a rigorous mathematical result, without treating it as completion of Yau 26.

## Output

# Verification Memo: Four-Dimensional Ishida–LeBrun Defect-Gap Theorem (Ric ≈ −g branch) and the Step 37/40/41 Discharge of (H1)

I read Step 39 (assembled theorem), Step 28 (terminal recalibration/pullback), Step 34–35 (fixed-exponent energy and index-level Hessian-χ tensors), A03 Step 37 (transported DeTurck existence), Step 40 (all-order continuation), Step 41 (extension theorem + first-exit + (H1) discharge), and the Step 39 integration memo. Below I address the six interfaces, each with the concrete mathematical object at stake and whether it invalidates or merely must be repaired. I treat the artifact as the restricted family theorem, not Yau 26.

---

## 1. Support Lemma 3.1: which cutoff regularity is actually constructed

**What the lemma asserts vs. what its hypotheses give.** Lemma 3.1(a) states two derivative bounds: `‖dχ_α‖_∞ ≤ C/r` **and** `‖∇²χ_α‖_∞ ≤ C/r²`. The construction supplied is a maximal `14r`-separated net in the maximal-function good set `G_R`, under only `Ric ≥ −2g` (Bishop–Gromov doubling) plus the center energy `r⁴⨏_{B_r}|Rm|² ≤ ε₀`.

- The gradient bound is legitimate: `χ = φ(d(x_α,·)/r)` with `d` 1-Lipschitz gives `|dχ| ≤ C/r` unconditionally.
- The Hessian bound `‖∇²χ‖_∞ ≤ C/r²` is **not** constructible from these hypotheses. A cutoff of the distance function has `∇²χ = φ''|∇d|²/r² + φ'∇²d/r`, and `∇²d` (operator norm) is controlled only from a two-sided sectional bound or a `C^{1,α}` harmonic-radius lower bound. A Ricci lower bound gives only the one-sided Laplacian comparison `Δd ≤ (n−1)cot`-type bound (hence one-sided `Δχ`), and the `ε₀`-smallness of `∫_{B_r}|Rm|²` is an **integral** curvature smallness at the center, not a pointwise `|Rm|` bound on the initial metric that would yield a harmonic radius. So the initial cutoff cannot be given `‖∇²χ‖ ≤ C/r²` at time zero.

**Why this does not invalidate the analytic estimates.** Step 34 and Step 35 were deliberately built to avoid a pointwise `∇²χ` bound. The Hessian-χ contractions enter as *signed* tensors `A_{pq}=∇_p∇_q a` that are integrated by parts once (Step 35 eqs. 3.8, 6.6): after IBP only one factor `∇a = 2χ∇χ` survives, so only `|∇a| ≤ C/r` is used (Step 35 §3.3(ii)–(iv), §6.4(ii)–(iv)). Step 34 states this explicitly: "use the signed Hessian route rather than assuming an evolving pointwise Hessian bound … `|∇²_{g(t)}a| ≤ Cr^{-2}` is a stronger later continuation input, not an interchangeable premise." So the energy machinery needs only `|dχ| ≤ C/r`.

**Consequence.** Lemma 3.1(a) *asserts* more than it constructs and more than the proof consumes. The clean repair is to delete the `‖∇²χ‖ ≤ C/r²` clause, replace it by `|dχ| ≤ C/r` plus (if wanted) a one-sided `Δχ ≥ −C/r²` from Laplacian comparison, and add one sentence confirming that every downstream use of a second cutoff derivative is via the signed IBP (Step 35), never a pointwise `∇²χ` bound.

**Higher jets for Step 40.** Step 40's staggered induction requires `C_{m+1}=∇^{m+1}χ ∈ L^q` for all finite `m`. Two things must be stated that currently are not: (i) `χ` must actually be `C^∞` — a raw distance cutoff `φ(d/r)` is only Lipschitz at the cut locus, so a mollified/smoothed radial function must be used; (ii) the resulting `‖∇^{m+1}χ‖` are finite **per datum** (each `g_i` is smooth), which is all the per-datum first-exit closure needs, but they are **not** `r`- or `i`-uniform because that would require control of higher curvature derivatives of `g_i` near the support. This is consistent with Step 40/41 being per-datum, but the smoothness of `χ` and the per-datum finiteness of its jets should be established rather than left implicit.

---

## 2. K₂ self-improvement with the additive `C₀·T` term — homogeneity in collapse / tiny support

The concern is whether (4.13), `K₂^η(T_*) ≤ e^{Cθ(1+1)+Cγ_*³}K₂^η(0) + C₀θr²`, can yield `K₂^η(T_*) < 2K₂^η(0)` uniformly when the support volume is tiny.

- **The absorption parameter is genuinely collapse-independent.** With `S ≃ r²/Vol(B_{5r})^{1/2}` and the good-support bound `K₂^η(0) ≤ K̄₀·Vol`, one has `γ = S·(K₂^η(0))^{1/2} ≤ C r²√K̄₀`. The support volume cancels, so `γ ≤ γ_*` is a volume-free smallness — this is exactly the point that makes the whole absorption structure survive collapse.
- **The additive constant is homogeneous with the seed, but the note does not display why.** `C₀` originates from the constant floor of `F² = 1+|Rm|²` in the reaction, so `C₀ ~ C·Vol(supp η)`. The seed obeys a **lower** bound `K₂^η(0) = ∫η²F² ≥ ∫η²·1 ~ Vol(supp η)`. Hence `C₀θr²/K₂^η(0) ~ Cθr²`, which is small for the fixed universal `r` (chosen in (3.3)) and small `θ`, **independently of collapse**: collapse only shrinks `Vol`, cancelling in numerator and denominator, and `r` does not shrink with collapse.

**Consequence.** The self-improvement is homogeneous, but (4.13) as written ("for `θ ≤ θ₁` small enough") hides a dependence on `K₂^η(0)/(C₀r²)`. The repair is to display the two facts `C₀ ≤ C·Vol(supp η)` and `K₂^η(0) ≥ c·Vol(supp η)`, so the improvement ratio is `Cθr²` with `θ`-uniform, collapse-uniform, tiny-support-uniform constant. This is a presentational hole with a one-line fix, not a defect in the mechanism. (One should also confirm the local `L⁴` Sobolev inequality `S ≃ r²Vol^{-1/2}` is invoked in the Saloff-Coste/Bishop–Gromov form valid under `Ric ≥ −2g` without noncollapse; this is standard but is used implicitly.)

---

## 3. A03 Step 40/41 evolution interfaces: what is derived vs. asserted

**The `G` term is genuinely harmless.** `G = (g⊛g)/(2(n−1))` is parallel, `∇G = 0`, so it introduces no derivative branch in (1.4)–(1.5). This is correctly used and requires no further work.

**The general-order structural equations are asserted, not derived.** Step 40 writes the two families
`∂_tU_m = a∆U_m + Σ C_α*C_β*U_γ + Σ ∇^i a*U_j*T_k + U*U_m + 𝒢_m` (1.4) and the analogous `∂_tT_m` (1.5), with the statement that `𝒢_m, 𝒩_m` (normalization, `G`, Laplacian commutators, connection variation) have "the same ordering as the displayed terms." This highest-derivative bookkeeping is the load-bearing structural input, and it is **verified only in low orders** (the `m=0` curvature/defect power inequalities are proved at index level in Step 35; `m=2` is claimed in the unsupplied companion `step40_m2_coupled_continuation_mechanism.md`). Step 41 §8 itself records the all-order induction as "TTCS-verified but schematic at high orders." So the normalized weighted-`U` and unweighted-`T` evolution equations remain **structural assertions at general `m`**, anchored — solidly — at `m=0` by Step 35 and (per the note) at `m=2`.

**The discharged (H2) — zero-order unweighted `T ∈ L^q` — rests on a citation, not a supplied derivation.** Step 39 eq. (4.12), `d/dt‖T‖_p^p + c∫a|∇T|²|T|^{p-2} ≤ C(K+1+r^{-2})‖T‖_p^p + C_p`, is a *distinct* estimate from Step 35's *weighted* `K_p` inequality (weight `a^{p-2}F^{p-2}`). Step 41 Step B stage 0 supplies it as "adapting Wang Lemma 4.10 with the normalization term, which is zeroth-order." Two points:
- The mechanism is correct in principle: the quadratic curvature reaction in `∂_tT` carries a factor `a` (the flow is `∂_tg=-2aE`), so it is `a·T*T`, bounded by `|aT||T| = |U||T| ≤ K|T|`, giving linear Gronwall growth. On `{a=0}` the metric is frozen, `T` is time-constant, and the unweighted `‖T‖_p^p` over that region contributes nothing — the RHS reaction over that region is a harmless over-estimate.
- But this Wang-Lemma-4.10 adaptation with the `+g` normalization is not reproduced at the index level; it is the analogue of Step 35 for the *unweighted* whole-manifold norm and is cited, not derived. Since it is the input that "discharges" (H2), its status is: mechanism sound, full derivation with normalization outstanding.

**Consequence.** The `m=0` layer (Step 35) is rigorous. The all-order layer (1.4)–(1.5), and the unweighted `T∈L^q` propagation, are structurally correct but still schematic at general order and should be written out — at minimum the highest-derivative ordering of `𝒢_m,𝒩_m` from connection variation must be verified for general `m`, not asserted.

---

## 4. Transported DeTurck existence/restart (Step 37): theorem or well-founded adaptation?

Step 37 correctly identifies the right object — the transported-coefficient DeTurck system (2.2)–(2.3) with hatted coefficient `\hat a = (χ∘φ_t^{-1})²` and gauge `\hatδ^*(\hat a S^{-1}δG(S))`, repairing the earlier fixed-coefficient error via the product rule `𝓛_{\hat aW}\hat g = \hat a 𝓛_W\hat g + d\hat a⊗W^♭ + W^♭⊗d\hat a` — and proves the pullback identity `g = φ_t^*\hat g` solves `∂_tg = -2a(Ric_g+g)` (§2). This part is verified algebra (the referenced `verify_step36_interface_algebra.py` confirms the product rule and the necessity of the gauged term).

The remaining content is **not** yet a self-contained theorem:

- Yang's construction is a **degenerate** parabolic existence (the coefficient `a=χ²` vanishes), not ordinary uniformly-parabolic Schauder. Existence goes through an `ε`-regularization (`ε²∆h` in the linearized problem, Approach 1, or `ε²+χ²` coefficient, Approach 2) followed by **`ε`-independent tame energy estimates** to pass `ε→0`.
- Step 37 §3 argues the `+g` normalization contributes only two bounded lower-order matrices (`-2\hat a h` into `D`, `-2(δ\hat a)\hat g` into `E`/`C`), leaving the principal symbol `2χ²∆` and the transport structure untouched. This is the right observation. But it does **not** reproduce Yang's specific `ε`-independent tame energy inequalities *with* the two new matrices included; it argues by the general principle that bounded lower-order perturbations are "absorbed by interpolation and Grönwall." The genuinely new mathematical step — that the `ε`-uniform energy/interpolation estimates persist verbatim under the added matrices, so the `ε→0` limit is still smooth with the same short time — is asserted, not carried out.
- **Restart** is clean *given* existence: the theorem is stated for arbitrary smooth `(M,g_*,χ)`, so it applies to the terminal metric with no extra work. This is the one part of the (H1) discharge that is genuinely immediate.

**A source-grounding inconsistency to reconcile.** Step 39 attributes the existence to "Yang, Theorem 4.1 in the Wang–Yang pseudolocality paper," while Step 37 attributes it to "Theorem 8.2, eqs. 8.5–8.6 at lines 804–807" of a specific integral-bounds convergence `object.md`. These are different theorem numbers (and possibly different papers). The degenerate-DeTurck existence must be tied to one verified published statement, and the two notes must cite the same one.

**Consequence.** Step 37 is a correctly-structured, well-founded adaptation that pins down the right system and the right perturbation, but the `ε`-uniform tame estimate for the *normalized degenerate* linearized system (1.4)–(1.5)+(3.1) is what turns it into a theorem, and that is exactly what is not written. Script pass counts ("41/41", "70/70") certify the algebraic/bookkeeping layer, not this analytic existence.

---

## 5. Terminal recalibration hypotheses: `q ≥ 0` and the selected monopole class `(a⁺)² ≥ A`

Step 28 is explicit and correct here. Eq. (1.3), `D_{a_i} = J_i − q_i − (2/3)((a_i⁺)² − A_i)` with `0 ≤ D_{a_i} ≤ J_i − q_i ≤ J_i`, is derived "using `q_i ≥ 0` and `(a_i⁺)² ≥ A_i` for the selected sign." Both facts are load-bearing:

- `D ≥ 0` is the Seiberg–Witten inequality itself (`I ≥ (2/3)(a⁺)²`), valid for **any** metric, hence for `g_i(T)`.
- To conclude `D` is **small** (which forces the calibrated profile `s→−4`, `|W⁺|²→1/24` via completion of squares), one needs the **upper** bound `D ≤ J`, and that needs `q ≥ 0` and `(a⁺)² ≥ A`. For the asymptotic contradiction the sharp form is slightly weaker: with the selected class satisfying `(a⁺)² ≥ A` and `|q_i| = o(A_i)` (which follows from `k_i/A_i → 1/3`), one gets `D ≤ J + |q| = o(A)` regardless of the sign of `q`; but `D ≥ 0` from SW is still required for the completion-of-squares to bite.
- The sign-class selection with `(a⁺)² ≥ A` is metric-independent and therefore transports to the terminal metric: `(a_ε⁺)² ≥ a_ε²` (since `(a_ε⁻)² ≤ 0`) with `a_ε²` topological, and the averaging `2^{-k}Σ(a_ε⁺)² = A + Σ(E_j⁺)² ≥ A` shows *some* class has `(a_ε⁺(T))² ≥ A` for the terminal Hodge star. This is precisely why §6's "depends on topology and orientation, not the specific metric" is substantively right.

**Where Step 39 is unclear.** Theorem 1.1's hypotheses list only `A_i = c₁²(X_i) → ∞`, `k_i/A_i → 1/3`, and "carrying the monopole class structure." It does **not** state (i) `k_i ≥ A_i/3` (i.e. `q_i ≥ 0`, or at least `q_i = o(A_i)` which does follow from `k/A→1/3`), nor (ii) that a monopole sign class with `(a_ε⁺)² ≥ A_i` is selected. Section 6's one line ("the mixed SW inequality still holds … through the a priori monopole estimate") is correct in substance but does not re-invoke the class selection at `g_i(T)` or state `(a⁺)²(T) ≥ a² = A` (metric-independent). The repair is purely to move Step 28's explicit hypotheses into the theorem statement and to have §6 name the selected class and its metric-independent lower bound.

---

## 6. Exponential-pullback / terminal compactness: which convergence is actually needed

**Step 28 does this correctly; Step 39 §7.2 states a weaker convergence that does not close.**

Step 28 §2–3 uses exactly the right ingredients: inner plateau centers `P_i` with `Vol(P_i) ≥ αA_i` (2.1); the Liouville/Rauch exponential-pullback averaging over the **center set** (2.3), whose constant `C(4,K,ρ) = ∫₀^ρ s_{-K}³/∫₀^ρ s_K³` comes from Rauch comparison and whose validity needs `Kρ² < π²/4` (no radial conjugate points); multiplicity/base-collapse harmlessness because the density is nonnegative; and — crucially — noncollapse **manufactured in the tangent space** by the Rauch lower Jacobian `J_i ≥ s_K³` (§3 point 1), which supplies the harmonic-radius lower bound even when the base collapses. It then explicitly invokes **strong finite-`W^{2,p}`** convergence with a single radius shrink, and reads off `E_∞=0`, `s_∞=−4`, `|W⁺_∞|²=1/24`, `G_∞=0`.

Step 39 §7.2 instead writes: "a subsequence converges in `C^{1,α}` and **weakly** in `W^{2,p}`," and "the curvature eigenvalues, scalar curvature, `|W⁺|`, and spectral gap `G` are **Lipschitz in the metric coefficients**." This is insufficient for the conclusion (7.5):

- `|E|²` and `(s+4)²` are convex/quadratic in curvature (curvature is affine in `∂²g` given strong-convergent `∂g`), so weak `W^{2,p}` + strong `C^{1,α}` gives `∫|E_∞|² ≤ liminf = 0`, hence `E_∞=0` a.e. That part survives weak convergence.
- But `|W⁺_∞|² = 1/24` does **not** follow. `|W⁺|²` is quadratic in the curvature, and `s_i + 8√6|W⁺_i| → 0` in `L²` passes to `s_∞ + 8√6|W⁺_∞| = 0` only if `|W⁺_i| → |W⁺_∞|` strongly (a.e. or in `L²`). Under *weak* `W^{2,p}` convergence of `g_i`, `Rm_i ⇀ Rm_∞` only weakly, and a quadratic curvature functional is not passed to the limit by weak convergence. "Lipschitz in metric coefficients" describes continuity under strong `C^0` change of coefficients, which is not supplied by weak `W^{2,p}`. So §7.2 as written cannot reach `|W⁺_∞|² = 1/24`, and the Derdziński contradiction (which is entirely about the exact value `1/24 ≠ 2/3`) does not activate.
- §7.2 also omits the tangent-space noncollapse/harmonic-radius step (Step 28 §3 point 1) that is what makes strong `W^{2,p}` convergence available in the pullback despite base collapse.

**This is an internal inconsistency, not a genuine obstruction:** the module (Step 28) is correct; the assembled theorem (Step 39 §7.2) restates it in a weaker form that would not close. The repair is to replace §7.2 verbatim by Step 28 §2–3: strong finite-`W^{2,p}` convergence with the Rauch-manufactured harmonic radius, then Einstein elliptic regularity (`E_∞=0` ⇒ `g_∞` real-analytic in harmonic coordinates) so that Derdziński's harmonic-`W⁺` hypothesis applies to a genuinely smooth Einstein germ.

The Derdziński contradiction itself is sound: Einstein `Ric=−g` with `spec(W⁺)=(−1/6,1/12,1/12)` (two distinct eigenvalues, `W⁺≠0`) is locally conformally Kähler by the factor `(24|W⁺|²)^{1/3}`, constant here, hence locally Kähler; but a Kähler–Einstein 4-metric with `s=−4` has `|W⁺|²=s²/24=16/24=2/3 ≠ 1/24`. The arithmetic and the constants `108, 6, 119` in the recalibration chain (`864π²D ≤ 108Q` via `D ≤ J ≤ Q/8π²`, `48π²D ≤ 6Q`, sum `= (1+4+108+6)Q = 119Q`) are internally consistent.

---

## Synthesis: what to repair to make the restricted theorem rigorous

The seven modules split cleanly into *rigorous now*, *presentational repair*, and *analytic work outstanding*.

**Rigorous now (Ric ≈ −g branch, Ishida–LeBrun family):** the near-critical calibration §2 (mixed SW, completion of squares, calibrated profile), the `m=0` index-level curvature/defect power inequalities (Step 35), the `G`-parallel harmlessness, the Derdziński contradiction algebra, and the Step 28 exponential-pullback/strong-`W^{2,p}` terminal passage.

**Presentational repairs (mechanism correct, write-up must be fixed):**
1. Delete the unconstructible `‖∇²χ‖ ≤ C/r²` clause in Lemma 3.1(a); keep `|dχ| ≤ C/r`; state that every second-cutoff-derivative use is signed IBP; establish `χ ∈ C^∞` and per-datum finiteness of its jets.
2. Display `C₀ ≤ C·Vol(supp η)` and `K₂^η(0) ≥ c·Vol(supp η)` so the (F1) self-improvement ratio is a `θ`-, collapse-, and tiny-support-uniform `Cθr²`.
3. Move Step 28's explicit hypotheses `q_i ≥ 0` (or `|q_i|=o(A_i)`) and the selected monopole class `(a_ε⁺)² ≥ A_i` into Theorem 1.1, and have §6 name the class and its metric-independent lower bound `(a⁺)² ≥ a² = A`.
4. Replace Step 39 §7.2 by Step 28 §2–3 (strong finite-`W^{2,p}`, Rauch-manufactured harmonic radius, Einstein elliptic upgrade to smooth), dropping "weakly in `W^{2,p}`" and "Lipschitz in metric coefficients."
5. Reconcile the source citation for degenerate DeTurck existence (Wang–Yang "Theorem 4.1" vs. integral-bounds "Theorem 8.2").

**Analytic work outstanding (the substantive remainder):**
6. The `ε`-uniform tame energy estimate for the *normalized* transported-coefficient degenerate linearized system (Step 37 §3): write the `ε`-independent inequalities with the two added lower-order matrices included, so short-time existence is a theorem rather than an adaptation-in-principle. Restart is then immediate.
7. The all-order structural equations (Step 40 (1.4)–(1.5)) and the unweighted `T ∈ L^q` propagation (Step 41 stage 0 / the discharged (H2)): derive the highest-derivative ordering of `𝒢_m, 𝒩_m` from connection variation at general `m`, and reproduce the Wang-Lemma-4.10 unweighted curvature propagation with the `+g` normalization at the index level, matching the rigor already achieved at `m=0` in Step 35.

Once (6)–(7) are written at the standard of Step 35 and (1)–(5) are corrected, the energy → Moser → drift → Sobolev → global-`Q` feedback closes and Theorem 1.1 becomes a rigorous statement about the Ishida–LeBrun family in the `λ=−1` branch. As the notes themselves record, even that result does not touch the `λ>0` branch, arbitrary 4-manifold topology, `n ≥ 5`, dimension-only constants (the present `ε₄` depends on `K̄₀` and `r`), or the Lean formalization — so it advances Yau 26 as a consistency result for one obstructed family, not as a resolution.

**Unresolved with current files:** I cannot independently re-derive the exact `‖aE(t)‖_∞ ≤ Cδ(r²/t)^{1/3}` Moser endpoint, because the nested-time recurrence it depends on (Step 34 eq. 6.1 → the `1/3` exponent) is referenced but not reproduced in the supplied notes; the `t^{-1/3}` singularity is integrable and the drift bound is correct *given* that endpoint, but the endpoint exponent itself needs the unshown recurrence to verify. Likewise the `m=2` full derivation (companion note) and the two TTCS integrations referenced for Step 40 are not in the supplied set, so the "70/70" and "41/41" pass counts certify bookkeeping, not the two outstanding analytic items in (6)–(7).