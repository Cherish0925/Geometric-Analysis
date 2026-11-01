# TTCS Independent Branch Record

```json
{
  "step_id": 42,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A01/workspace/notes/step39_complete_conditional_defect_gap_theorem.md",
    "Sessions/S0910A03/workspace/notes/step29_terminal_density_bridge_lemma.md",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Independently examine the terminal contradiction and the claimed full spectral calibration. There are two possible routes in the files: the explicit nonnegative LeBrun spectral density G=f²-(b_-)², and the positive-part rescaled-monopole harmonic form/eigenline density. Determine which route is actually sufficient once a smooth Einstein chart with s=-4 and |W+|²=1/24 is obtained. Verify algebraically that G=0 forces the calibrated spectrum under the stated eigenvalue ordering, and identify the regularity/convergence needed to pass ∫G→0 to the limit. In parallel, assess whether the positive-part monopole construction is proven in the session files or only generator/Codex-level material, and whether it should be removed from the load-bearing proof. Finally check the local Derdziński/projector contradiction constants and orientation. Ground the answer in the supplied files and do not assume weak W2p convergence passes curvature nonlinearities.

## Output

## Verifier memo: terminal spectral calibration and the local Derdziński contradiction

I checked the algebra of the two candidate routes, the passage of the densities to the limit, the provenance of the positive‑part monopole material, and the Derdziński/projector constants. Findings below are grounded in Step 8 (A01), Step 28 (A01), Step 39 (A01), Step 16 (A03), Step 29 (A03), Step 6 (A03), and `quantitative_deficit_analysis.md`.

### A. The G‑density algebra is correct and self‑contained

With the labeling α≥β≥w (w the lowest eigenvalue of W⁺), and
f = (2/3)s − 2√(2/3)|W⁺|, b = (2/3)s + 2w, G = f² − (b₋)², I reproduced every step.

- Nonnegativity: b − f = 2ξ with ξ = w + √(2/3)|W⁺|. The linear‑algebra fact that a trace‑free symmetric operator on the 3‑dimensional Λ⁺ has lowest eigenvalue w ≥ −√(2/3)|W⁺| (extremal when the top two coincide) gives ξ ≥ 0, hence b ≥ f. If b < 0 then f ≤ b < 0 so f² ≥ b² and G = f² − b² ≥ 0; if b ≥ 0 the subtracted term vanishes. So G ≥ 0 pointwise for **every** metric — the density is legitimate.
- At the calibrated data s = −4, |W⁺|² = 1/24 (so |W⁺| = 1/(2√6)): √(2/3)·(1/(2√6)) = 1/6, giving f = −8/3 − 1/3 = −3, and b = −3 + 2ξ ≤ −8/3 < 0 because ξ ≤ 1/6. Then G = 9 − (−3+2ξ)² = 12ξ − 4ξ² = **4ξ(3−ξ)**, matching Step 8.
- Since u is pinned to 1/(2√6) by the *other* two densities, ξ ranges only over [0, 1/6] (w ∈ [−1/6, 0]). On this interval 3−ξ > 0, so **G = 0 ⇔ ξ = 0 ⇔ w = −1/6**. This is the extremal case w = −√(2/3)|W⁺|, which forces the remaining two eigenvalues equal, giving spec(W⁺) = (−1/6, 1/12, 1/12). Trace and norm check: −1/6+1/12+1/12 = 0, 1/36+2/144 = 1/24. ✓

I also verified the completion identity s²/24 + 2u² = (1/12)f² + (1/216)(s+8√6u)² by expanding: s² coefficient 1/27+1/216 = 1/24; the su cross terms cancel (−2√6/27 + 2√6/27 = 0); u² coefficient 2/9+16/9 = 2. This confirms the algebra behind the 864π² and 48π² deficit constants.

**Logical order that matters:** (s+4)² and (s+8√6|W⁺|)² first fix s = −4 and |W⁺|² = 1/24 (hence u, hence the coefficient 1/6 in ξ); only then does G = 0 pin the eigenvalue split. This ordering is respected in the notes and is essential.

### B. Which route is sufficient: the G‑density route, alone

Once a smooth Einstein chart with Ric = −g, s = −4, |W⁺|² = 1/24 is in hand, the three scalar/spectral densities |E|², (s+4)², (s+8√6|W⁺|)², plus G, determine the full spectrum by pure algebra (part A). The Derdziński/projector contradiction then needs only δW⁺ = 0 (from Einstein) and the two‑distinct‑constant‑eigenvalue structure. **No surviving monopole, no limiting harmonic form, no eigenline density is required.**

The positive‑part rescaled‑monopole density (Step 16 D, Step 29 𝔇 with the extra terms (|2πH| − r/(3√2))² + 2⟨𝒜H,H⟩) is a heavier and redundant alternative to reach the same spectrum. Notably, A01 Step 39's assembled density (eqn 6.3) already uses only |E|²+(s+4)²+(s+8√6|W⁺|)²+G — the clean G‑route. A03 Step 29 augments this with the monopole terms; that augmentation is not needed for the terminal contradiction.

One distinction to keep explicit: the **global** Seiberg–Witten integral inequality I ≥ (2/3)(a⁺)² (LeBrun, eqn 2.2) is still the source of all calibration and stays load‑bearing. What is redundant is the *pointwise chart* reconstruction of a weighted monopole and its limiting harmonic form. These are different uses of gauge theory.

### C. Regularity needed to pass ∫G → 0 to the limit

This is the decisive analytic point, and it is exactly where the task's caution applies. G is a nonlinear (quadratic in the eigenvalues, hence in the full curvature) function of ∂²g. Under **weak** W^{2,p} convergence, ∂²gᵢ ⇀ ∂²g_∞ only weakly, and nonlinear curvature functionals do **not** pass through weak limits. So "eigenvalues/|W⁺|/G are Lipschitz in the metric coefficients, therefore the limit satisfies the equations a.e." — the justification written verbatim in **Step 39 §7.2** (and echoed in Step 29 Step 5's "Lipschitz in the metric") — is not valid as stated. Lipschitz continuity in the second derivatives does not commute with weak convergence.

The correct mechanism, which the notes do contain elsewhere, is to upgrade to **strong** W^{2,q} (q > 4) first, and only then pass the nonlinear densities:

- **Regular‑patch / fixed‑critical route (Step 6 A03, Step 8 §5 A01):** in harmonic coordinates, g^{ab}∂_a∂_b g_{jk} = −2Ric_{jk} + Q(g⁻¹,∂g). Since Ricᵢ = −gᵢ + eᵢ with ‖eᵢ‖_∞ → 0, and ∂gᵢ → ∂g_∞ strongly in C^{0,β} (from the C^{1,β} harmonic‑radius bound), the RHS converges strongly in L^q. Interior Calderón–Zygmund W^{2,q} estimates for the operator with C⁰‑converging coefficients then give **strong** W^{2,q} convergence on a smaller chart. This upgrade is correctly described and, importantly, avoids Schauder/C^{2,α} control of the approximants. Strong W^{2,q} gives Rmᵢ → Rm_∞ in L^q, hence W⁺, s, ordered eigenvalues, and G converge strongly in L^{q}/L^{q/2}. Then ∫_chart Gᵢ → ∫_chart G_∞, the selection gives ∫_chart Gᵢ → 0, so G_∞ = 0 a.e., and elliptic bootstrap makes the limit smooth with G_∞ ≡ 0. This is rigorous.

- **Pullback/flow route (Step 28 §3):** here bounded sectional curvature |Rm(T)| ≤ C_F is available on the plateau (Step 39 eqn 7.1), together with a Rauch volume lower bound. At positive flow time interior Shi estimates supply all ∇^m Rm bounds and hence smooth convergence, which passes nonlinear curvature quantities directly. This is the cleanest upgrade and the substance is present.

So the substantive input everywhere is bounded curvature (or the elliptic RHS upgrade), giving strong convergence. **Step 39 §7.2 should be rewritten to invoke the bounded‑curvature strong‑convergence upgrade (Shi at positive time, or the harmonic‑coordinate elliptic upgrade) rather than "weak W^{2,p} + Lipschitz ⇒ a.e."** The needed hypothesis (|Rm| ≤ C_F on the plateau) is already established at eqn 7.1, so this is an exposition correction, not a hole — provided the smoothing chain actually delivers the bounded‑curvature plateau it assumes (H1 and the selected‑support outputs remain the conditional inputs).

### D. Status of the positive‑part monopole construction

In the session files this construction is supported only at the algebra/generator level:

- Step 16 §4 and `quantitative_deficit_analysis.md` derive the exact nonnegative decomposition (9)/(12) and the amplitude/eigenline estimates (13)–(17), (L). The supporting scripts `verify_positive_part_monopole_algebra.py` and `verify_deficit_constants.py` "verify algebra only, not the Seiberg–Witten existence input or analytic passage to a chart limit" (Step 16 §6, explicit).
- The weighted/rescaled monopole (equations (2) with weight f, regularized f_k → √q) needs an existence theory for the modified system; the notes state (13)–(17) "assert the existence of arbitrarily close regularized solutions; they do not assert convergence of a canonical sequence of monopoles."
- Producing a **nonzero** limiting harmonic form |H_∞| = 3/(4√2 π) > 0 requires the additional uniform hypotheses (40)–(41) in `quantitative_deficit_analysis.md` §5 (uniform C^{2,α} harmonic radius, C⁰ control of the determinant‑line map); the note is explicit that a Sobolev bound alone does not suffice, and unique continuation only forces nonvanishing in a compact‑geometry limit.
- Provenance is generator/TTCS (`step16_ttcs02_generator1_integration.md`, `step16_ttcs02_sub1_generator.md`).

Because the G‑route reaches the identical spectrum with none of this, the positive‑part monopole harmonic/eigenline density carries extra unproven analytic burden (weighted‑SW existence, nonzero‑limit regularity) without adding to the terminal contradiction. Keeping it out of the load‑bearing chain and treating it as an exploratory alternative makes the proof rest only on: the global LeBrun SW inequality, the verified completion/G algebra, and the strong‑convergence chart upgrade.

### E. Derdziński/projector constants and orientation

The local lemma and its two closures check out:

- **Projector lemma (Step 6):** with W⁺ = μI + (λ−μ)P_ω, δW⁺ = 0 gives (∇^aω_{ab})ω_{cd} + ω_{ab}∇^aω_{cd} = 0. Contracting with ω^{cd} and using constant |ω| gives div ω = 0 (the first term is correctly retained, unlike an earlier version). Substituting back gives ω_{ab}∇^aω_{cd} = 0; nondegeneracy of a self‑dual 2‑form (ω_a{}^cω_c{}^b = −δ_a{}^b) then forces ∇ω = 0, hence ∇W⁺ = 0. Depends only on λ ≠ μ, not on signs. Correct.
- **Einstein–Weyl closure (needs the cubic constant):** det W⁺ = (−1/6)(1/12)(1/12) = −1/864. With Δ|W⁺|² = 2|∇W⁺|² + s|W⁺|² − 36 det W⁺ and |W⁺|² ≡ 1/24 constant (Δ = 0): 0 = 2|∇W⁺|² − 1/6 + 36/864 = 2|∇W⁺|² − 1/8, so |∇W⁺|² = 1/16 ≠ 0, contradicting ∇W⁺ = 0. Three notes agree on 1/16. **Caution:** this closure is sensitive to the "36": the contradiction survives iff s|W⁺|² ≠ 36 det W⁺, i.e. −1/6 ≠ −1/24; it would collapse only if the true constant were 144. The value 36 is the standard Weyl‑cubic constant (Derdziński 1983; Besse §16), consistent with the extracted primary text cited in Step 8, but if this route is kept load‑bearing the constant should be confirmed once against the primary source.
- **Kähler‑norm closure (independent of the cubic constant):** Derdziński's factor (24|W⁺|²)^{1/3} = 1 at |W⁺|² = 1/24, so the limit is locally Kähler; a Kähler‑Einstein 4‑metric has |W⁺|² = s²/24 = 16/24 = 2/3 ≠ 1/24. This closure uses only the sourced factor "24" and the Kähler identity |W⁺|² = s²/24 (I verified: Kähler W⁺ eigenvalues (s/6, −s/12, −s/12) give |W⁺|² = s²/24, and at s = −4 spec = (−2/3, 1/3, 1/3), |W⁺|² = 2/3). It does **not** invoke the "36 det" constant and is therefore the more robust of the two. I recommend it be the primary statement of the contradiction, with the ∇W⁺ route as corroboration.
- **Orientation:** for a Kähler surface with s < 0 the Kähler form ω lies in the eigenline of the lowest (most negative) W⁺ eigenvalue s/6. In the calibrated germ the simple eigenvalue is the lowest, −1/6, so the Kähler orientation aligns with the simple lowest eigenline — consistent with Derdziński's "the Kähler orientation is the prescribed orientation." The projector 𝒜 = W⁺ + √(2/3)|W⁺|I has eigenvalues (0, 1/4, 1/4) at the calibrated spectrum (the +1/6 shift I computed), so 𝒜 ≥ 0 with kernel exactly the lowest eigenline — internally consistent with 𝒜H = 0 selecting that line. No orientation inconsistency found.

### What remains open in the material examined

The terminal contradiction (parts A, B, E) is sound and, in the G‑form with the Kähler‑norm closure, does not depend on the redundant monopole construction or on the Weyl cubic constant. The one substantive correction inside the terminal step is C: the limit passage must be written through strong W^{2,q}/Shi convergence, not weak W^{2,p} with a Lipschitz remark. All of this remains conditional on the upstream deliverables the notes themselves mark as unproven — H1 (degenerate DeTurck existence/restart), the selected‑support flow producing a sequence‑uniform bounded‑curvature plateau with Vol(Pᵢ) ≥ αAᵢ, global Q(T)/Aᵢ → 0, and the positive‑time regularity that feeds the strong convergence. The terminal calibration verified here is the part that is in good shape; the geometric‑analytic production of the bounded‑curvature plateau is where the argument still needs its independent parabolic theorem.