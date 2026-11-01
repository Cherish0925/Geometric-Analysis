# TTCS Independent Branch Record

```json
{
  "step_id": 44,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step42_uniform_gap_weight_terminal_repairs.md",
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md",
    "Sessions/S0910A01/workspace/notes/step43_H_DT_assessment.md",
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A03/trace/ttcs/results/step45_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/trace/ttcs/results/step45_ttcs01_verifier2_integration.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md"
  ]
}
```

## Task

Independently review the restricted four-dimensional negative Ishida--LeBrun defect-gap chain as assembled in A01. Focus on whether the proof now coherently runs on one exact degenerate cutoff flow after coefficient regularization, and whether the analytic estimates feed the terminal Derdzinski contradiction without a hidden unsupported step. Please examine especially: (1) A01 Step43 §6 saying C_{m+1} is a previous layer versus A03 Step45/TTCS correction that it is the current partner of U_m and closes by same-exponent L^p energies; (2) whether coefficient-regularized flows with b=chi^2+eps^2 are used only to construct a common-time smooth limit solving the exact a=chi^2 flow before stationary collars, frozen complement, disjoint supports, and global Q are applied; (3) support construction with maximal-function good sets, disjoint buffers, one global a=sum chi_alpha^2, inner centers, and plateau volume from Vol/A -> 32 pi^2/9; (4) first-exit chain K2^eta -> integrated Y -> J6 -> Moser endpoints and global Q on the same exact flow; (5) terminal recalibration with q>=0 and the corrected D_av identity; (6) Liouville--Rauch pullback, strong finite W^{2,p} convergence, and Derdzinski forbidden germ. Return a direct scientific memo: which links are now sound, which statements in the notes must be corrected, and whether the family-uniform restricted gap follows after those corrections. Do not treat this as a solution of full Yau Problem 26.

## Output

# Verification Memo: the λ<0 Ishida–LeBrun defect-gap chain as assembled in A01

## Overall reading

The chain now has a single intended spine: a contradiction argument over the permitted Ishida–LeBrun geography (all `A,D,q,N` with `q≥0`), running one exact degenerate flow `∂_t g = -2χ²(Ric+g)`, with all constants universal in dimension four so that the resulting gap `ε_IL` does not depend on `A,D,q,N` or the input metric. The geometric endpoints (calibration, support selection, terminal recalibration, Liouville–Rauch pullback, Derdziński germ) are individually sound and connect correctly. The load-bearing residuals are analytic: the arbitrary-order weighted/unweighted curvature ledger and the parallel defect-variation ledger, both of which are asserted but not yet delivered as proved index-level lemmas. With the corrections below, the family-uniform restricted gap does follow from the assembled reasoning; without them, the statements "H-WU resolved" and "H-DT resolved" run ahead of what the notes actually establish. Below, each requested link.

---

## (1) Role of `C_{m+1}`: A01 Step 43 §6 vs A03 Step 45/TTCS

The A03 Step 45 / TTCS description is the correct one, and A01 Step 43 §6 must be corrected. Two concrete points.

- The cutoff-jet evolution (Step 45 (1.6)) is `∂_t C_{m+1} = Σ_{r+s=m-1} U_{r+1}*C_{s+1}`, whose top allocation is `U_m*C_1`. This couples `C_{m+1}` to the *current* variable `U_m`. Hence `C_{m+1}` is the current partner of `U_m`, and the two must be estimated in one joint energy, not in sequence. This is exactly Step 45 (5.7): `d/dt(‖U_m‖_p^p + ‖C_{m+1}‖_p^p) + c∫b|∇U_m|²|U_m|^{p-2} ≤ C(1+‖U_m‖_p^p+‖C_{m+1}‖_p^p)`, with the only current cross-products `|Z||V|^{p-1}` and `|Z|²|V|^{p-2}` (Step 45 (5.6), `Z=C_{m+1}`, `V=U_m`).

- A01 Step 43 §6, Term (III), writes the residual with "`C_{m+1} ∈ L^{2p}` (established at the previous staggered level)." This is wrong on both counts. The natural Hölder on `∫|C_{m+1}|²|U_m|^{p-2}` gives `‖C_{m+1}‖_p² ‖U_m‖_p^{p-2}` — exponent `p`, not `2p` — and by Young `≤ c(‖C_{m+1}‖_p^p + ‖U_m‖_p^p)`, i.e. a same-exponent coupling in the joint Gronwall. `C_{m+1}` is not a quantity known before `U_m`; treating it as a fixed higher-integrability input from an earlier level misdescribes the dependency and is not what closes the estimate.

Verdict: the link is sound once A01 Step 43 §6 is restated in the Step 45 (5.7) joint-pair form at exponent `p`. The corrected mechanism is in fact simpler than the version written in A01. The TTCS integration (verifier1 §4.3) makes the same point explicitly, including `∫|Z|²|V|^{p-2} ≤ (2/p)‖Z‖_p^p + ((p-2)/p)‖V‖_p^p`.

---

## (2) Coefficient regularization and the ordering of the geometric structure

The intended ordering is correct and is the only ordering that is self-consistent, but it must be stated explicitly in the A01 notes, where it currently is not.

- For `b = χ²+ε² > 0` the flow is nondegenerate: on `{χ=0}` the metric still evolves with coefficient `ε²`. So the frozen complement, the disjoint-support additivity of `Q`, and the stationary collar are **not** properties of the regularized flows. They are properties only of the exact `a=χ²` limit, where `∂_t g = 0` on `{χ=0}`.

- Therefore the correct sequence is: (i) fixed-`ε` strictly-parabolic DeTurck existence with transported coefficient `\hat b_ε = b_ε∘φ_t^{-1}` (so pullback restores the exact geometric equation); (ii) `ε`-uniform finite-`L^p` propagation on a common per-datum interval; (iii) diagonal `C^∞` limit solving `∂_t g = -2χ²(Ric+g)` (Step 45 §6, TTCS verifier2 §§4–5), with positivity `½g_0 ≤ g ≤ 2g_0` preserved; then and only then (iv) apply frozen complement, disjoint supports, collar, and global `Q` to that one limit flow.

- A01 Step 36 §1 and Step 41 §2/§6 write the exact flow and its frozen complement directly, without threading (i)–(iii). This is a presentational correction, not a mathematical one: the exact-flow limit is supplied by Step 45 §6 and confirmed by TTCS verifier2 §5, and applying the collar/`Q` structure to the limit is legitimate. Uniqueness of the degenerate limit is not needed, because the contradiction argument only requires *one* existing common flow (TTCS verifier2 §6). This should be stated where the global `Q` and collar are invoked, so that no reader applies those properties to `b=χ²+ε²`.

Verdict: sound in substance; the ordering must be made explicit in the A01 platform notes.

---

## (3) Support construction

Sound. The one hypothesis that must be visibly justified is `Ric ≥ -2g`, used globally for the Bishop–Gromov weak-type maximal inequality (Step 41 (2.2)). It follows directly from the contradiction hypothesis: `δ = ‖g^{-1}(Ric+g)‖_{∞,op} → 0` puts the eigenvalues of `g^{-1}Ric` in `[-1-δ, -1+δ]`, so `Ric ≥ -(1+δ)g ≥ -2g` for large `i`. This makes the doubling/maximal-function machinery global, not merely local, which is what the argument uses.

The remaining ingredients check out: `∫|Rm|² ≤ C A_i` (in 4D, `∫|W^-|² = ∫|W^+|² - 12π²τ`, and both `∫|W^+|²` and `τ` are `O(A)`); the `14r`-coloring giving disjoint `B_{7r}`; and the plateau volume from the calibrated ratio. That ratio is internally consistent: at `s=-4`, `|W^+|²=1/24`, the density `s²/24 + 2|W^+|² = 3/4`, `I → (2/3)A` forces `Vol/A → 32π²/9`, and `Vol(good) ≥ (32π²/9 - Cr⁴/γ_0²)A ≥ α_0 A`. Inner-plateau volume `≥ cα_0 A` survives the terminal `C^0` drift `‖g(T)-g(0)‖ ≤ Cδθ^{2/3}r² → 0`.

---

## (4) First-exit chain `K_2^η → ∫Y → J_6 → Moser → Q`

Structurally coherent on the exact limit flow, with two concrete items to settle.

- The curvature side (`K_2^η` propagation Step 34 (3.1), `∫Y ≤ CγK_2^η(0)` (3.6), `B(t) ≤ Cγ³` (3.7), `Y(t) ≤ CγK_2^η(0)/t` (4.4), Moser endpoint `‖aF‖_∞ ≤ Cγ/t`) rests on the curvature-variation premise (2.3) and derivative-structure bound (2.10). These are exactly the objects that Step 45's ledger addresses at all orders (`∂_t T = bΔT + B_1*∇T + B_2*T + b(T*T+T+1)`), checked against Wang's coordinate-time formulas by two TTCS branches. Good, conditional on ledger completeness (see below).

- The defect side is a separate ledger that has **not** received the same treatment. `J_6` persistence (Step 34 §5) and global `Q` propagation (Step 36 §3) both use the defect evolution (Step 34 (5.5)) and the Hessian-`a` defect tensor `B_def = |E|²g + (tr E)E - 2E²` (5.8) with `|∇B_def| ≤ Cs^{1/2}|∇E|`. Step 45 verifies the ledger for `T = Rm+G, U = bT`, i.e. the curvature object, not `s = |E|²`. Step 34 §7 item 2 itself lists the defect-variation index-level derivation as outstanding. Since `Q(T)/A → 0` (the terminal input, point (5)) and the metric-drift endpoint `‖aE‖_∞ ≤ Cδ(r²/t)^{1/3}` both flow through this defect ledger, it is load-bearing for the terminal contradiction and must be delivered at the same index level as the curvature ledger. This is the most concrete not-yet-closed analytic object beyond the curvature ledger.

- The moving-Sobolev/first-exit self-improvement (Step 41 §5.6) closes because the collapse-surviving estimates are multiplicative (`e^{C r^{-2} t}` with `t ≤ θr²`, giving `e^{Cθ}` independent of `r`) and `γ ≤ Cr²√K_0` is small on good supports. For the *family-uniform* conclusion, the note should state that `θ` is chosen last, small relative to the universal `C`, so `e^{Cθ} < 2` and the drift stays below `α_0/2` uniformly in `i` and `ε`. The mechanism is right; the order of quantifier choice should be written down.

Verdict: the curvature side of the chain feeds the terminal step cleanly given the ledger; the defect side needs its own verified variation before `J_6`, the Moser defect endpoint, and global `Q` can be regarded as established.

---

## (5) Terminal recalibration, `q≥0`, and the `D_av` identity

Correct. The corrected deficit algebra is internally consistent:
`(2χ+3τ)(M) = A - D = 2A/3 - q` with `q = D - A/3`; `I - J = 2A/3 - q` (Step 42 (2.1)); sign-averaged monopole `I ≥ (2/3)(A + Σ(E_ℓ^+)²)`; hence
`D_av = I - 2A/3 - (2/3)Σ(E_ℓ^+)² = J - q - (2/3)Σ(E_ℓ^+)² ≥ 0` (Step 42 (2.3)).
I verified the substitution: `I = J + 2A/3 - q` gives `D_av = J - q - (2/3)Σ` directly. For `q≥0`, `0 ≤ D_av ≤ J`, and with `J ≤ Cδ²Vol`, `Vol/A → 32π²/9`, one gets `q/A → 0`, `Σ(E^+)²/A → 0`, `D_av/A → 0`. The note correctly flags the earlier `I-J = A-k = -q` line as an error (a `2A/3` had been dropped).

The terminal `SW` inequality for `g_i(T)` is valid because Seiberg–Witten invariants are diffeomorphism-invariant and the flow does not change the smooth manifold; every sign class remains a monopole class for `g_i(T)`. The terminal density combination `∫𝔇 ≤ 119 Q(T)` (Step 28 (1.7), Step 41 (7.5)) then gives `∫𝔇/A → 0` via global `Q` propagation. The single-class Step 28 form `D_{a_i} = J - q - (2/3)((a_i^+)² - A)` and the averaged Step 42 form both deliver `D/A → 0`; they are consistent. One presentational note: Step 28 is written for `M = X # k\overline{CP}²` while Step 41/42 use the general `(#X_j)#N`; Step 41 §7 re-derives in the general geography, so this is a difference of representative case, not an inconsistency.

---

## (6) Liouville–Rauch pullback, finite `W^{2,p}` convergence, Derdziński germ

Sound, and the earlier unsupported step has been removed.

- Liouville–Rauch averaging (Step 28 (2.3), Step 41 (8.3)) is the correct mechanism: for nonnegative `D`, `∫_{P^in} A_ρ D dμ ≤ C(K,ρ)∫_M D dμ`, using Rauch Jacobian bounds and Liouville invariance; multiplicity is harmless because `D ≥ 0`, and no injectivity radius on `M` is used. Applied to `𝔇` with `∫𝔇/A → 0` and `Vol(P^in) ≥ cα_0 A`, this selects `p_i` with `A_ρ𝔇(p_i) → 0`.

- The convergence is now correctly stated at `W^{2,p}` (Step 42 §5, replacing the earlier `W^{4,p}` inference, which would have needed derivative control on the defect and was unsupported). Bounded sectional curvature `≤ K` on the plateau (`a=1`, `‖aF‖_∞ ≤ C/T`) plus Rauch volume lower bound give a harmonic radius; `L²` pullback smallness of `E` interpolated against the uniform `L^∞` bound gives `‖E‖_{L^p} → 0` for all finite `p`; elliptic stability of `g^{ab}∂_a∂_b g_{jk} = -2Ric_{jk} + Q(g^{-1},∂g)` yields `g_i → g_∞` in `W^{2,p}_loc` with `Ric_{g_∞} = -g_∞` weakly, and elliptic bootstrap makes `g_∞` smooth. The requirement `Kρ² < π²/4` (no radial conjugate points) forces `ρ ~ r`, which is a consistent choice.

- The Derdziński germ is correct arithmetically. The calibrated spectrum `spec(W^+_∞) = (-1/6, 1/12, 1/12)` is trace-free and has `|W^+_∞|² = 1/36 + 1/144 + 1/144 = 1/24 ≠ 0`, so `W^+ ≠ 0` everywhere with exactly two eigenvalues; Derdziński's proposition applies, the conformal factor `(24|W^+|²)^{1/3} = 1` is constant, so `g_∞` is locally Kähler. A Kähler–Einstein 4-metric has `|W^+|² = s²/24`, which at `s = -4` is `2/3`, contradicting `1/24`. The contradiction is genuine.

Verdict: sound with the Step 42 §5 correction in place.

---

## Load-bearing residual objects (name the causes)

Two of the required corrections trace to a single cause: the analytic status is written as "resolved," but the TTCS verifiers establish closure **conditional on** two index-level ledgers being proved lemmas rather than schematic star-expressions.

1. **Arbitrary-order curvature ledger (H-WU).** TTCS verifier1/verifier2 confirm the staggered finite-`L^p` induction closes uniformly in `ε` with no hidden `T_∞`, no current-exponent escalation, no `ε^{-1}`, and no omitted current derivative — **given** the completeness of the families (T1–T6, U1–U7). But the same verifiers state the ledger's stars still hide numerical coefficients and slot permutations, and that `[∇^m, bΔ]`, `∇^r(∂_tΓ)`, `∂_t∇^{m+1}χ`, and the signed-Hessian/cutoff contractions all falling into those families "must be proved as a lemma, not inferred from schematic notation." Concretely, incorporate the TTCS verifier1 corrections into the assembled chain: `∂_t G = -(S⊗g + g⊗S)/(n-1)` (Step 45 (1.2) has `/2(n-1)`; the `S=g` scaling test gives `∂_t G = -4G`, confirming `/(n-1)`); add `bT_m` and `bU_m` to the current-variable tables; write the spatial-commutator zero-order curvature as `b·Rm = U - bG` rather than `bT_0`; and treat the `m=2` term `χC_2*U_2*P(U_2)` as an explicit signed integration by parts, not merely as a "signed Hessian contraction." These are stated to be harmless to closure, but they are corrections to the ledger the assembled proof depends on.

2. **Defect-variation ledger.** As in (4), the `s=|E|²` evolution (Step 34 (5.5), (5.8)) underlying `J_6`, the Moser defect endpoint, and global `Q` has not received the index-level derivation the curvature ledger got. This is a distinct object and is load-bearing for `Q(T)/A → 0`.

A third residual is H-DT: the Step 43 assessment reduces normalized existence to importing Yang's Theorem 8.2 and verifying the normalization is a zeroth-order tame perturbation, or to the coefficient-regularization `C^∞` limit (Step 45 §6). For the contradiction argument this suffices, because only existence of one common flow is needed and uniqueness is not. It should be recorded as "established modulo importing Yang's published existence and modulo the ledger of item 1," not as an unconditional resolution.

---

## Does the family-uniform restricted gap follow?

Yes, conditionally and coherently, on one exact degenerate flow, provided:

- the two index-level ledgers (curvature and defect) are delivered as proved lemmas with the TTCS formula corrections incorporated;
- the `ε→0` limit is threaded before the frozen complement / disjoint supports / global `Q` are applied (point 2);
- A01 Step 43 §6 is restated in the joint same-exponent `(U_m, C_{m+1})` form of Step 45 (5.7) (point 1);
- the quantifier order for the first-exit self-improvement (`θ` chosen last, universal) is written down (point 4).

There is no longer a hidden unsupported step in the terminal passage: the `W^{4,p}` overreach is gone, the Derdziński arithmetic is correct, the `D_av` identity is correct, and the pullback selection needs no base noncollapse. The uniformity of `ε_IL` across the geography is genuine because every constant used (`r, γ_0, θ, α_0, K, ρ, C`) is universal in dimension four and the collapse-surviving estimates are multiplicative in `r^{-2}t ≤ θ`, so no constant depends on `A, D, q, N`, and the bounded-`A`/unbounded-`A` split (Step 42 §3) covers the whole `q≥0` range.

This remains a restricted four-dimensional `λ<0` Ishida–LeBrun result. It does not settle the `λ>0` branch, general four-manifold topology, dimensions `n≥5`, dimension-only constants for the original Yau Problem 26 proposition, or the Lean formalization.