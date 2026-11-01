# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A03/workspace/notes/step44_coefficient_regularization_start.md",
    "Sessions/S0910A03/workspace/notes/step44_normalized_yang_tame_start_restart.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Check whether the coefficient-regularization construction now yields a genuine per-datum short-time existence and restart theorem for ∂_t g=-2χ²(Ric+g), assuming the corrected Step 45 finite-exponent ledger. Compare with Yang Theorem 8.2 Approach 2 and the Step 44 coefficient-regularization note. Examine fixed-ε geometric/DeTurck existence with a spatial coefficient, the first-exit bootstrap, uniform Sobolev upgrades, control of spatial and time derivatives, ε→0 compactness, passage to the exact degenerate equation, positivity, and smooth endpoint restart by time-jet matching. Identify any remaining circularity, missing gauge transport, dependence on ε, loss of derivatives, or need for uniqueness. State precisely what would be established for the restricted Ishida–LeBrun route, without treating it as a solution of Yau 26.

## Output

# Verification memo: coefficient‑regularization start/restart for ∂_t g = −2χ²(Ric+g)

## Bottom line on the conditional statement

Granting the Step 45 finite‑exponent tensor ledger (the families T1–T6 / U1–U7 with the stated bounded coefficients) and the Step 44 zero‑order seed, the chain
fixed‑ε existence → ε‑uniform bootstrap → first‑exit improvement → uniform Sobolev → ε→0 C^∞ compactness → passage to the degenerate equation → positivity → jet‑matched restart
is internally consistent and does produce a genuine per‑datum smooth short‑time solution on a common interval [0,T₀], plus a smooth extension across a positive‑definite endpoint. It is not circular. The construction rests on one unproven mathematical object (the index‑level exhaustiveness of the ledger), one omitted‑but‑standard bookkeeping step (gauge/diffeomorphism tracking in the ε→0 passage), and one item left to a separate route (uniqueness of the degenerate limit). Below I verify each load‑bearing step, mark what is grounded in the provided Yang source, and state precisely what is delivered for the restricted Ishida–LeBrun route.

## 1. Fixed‑ε geometric/DeTurck existence with a spatial coefficient — sound

For ε>0, b_ε = χ²+ε² ≥ ε² > 0, so the principal spatial part b_εΔ of the DeTurck‑reduced system is uniformly elliptic for that ε. Yang's Approach 2 (source §8, "∂_t g = −2(ε²+χ²)Rc … reduced to a nonlinear strictly parabolic system") supplies exactly this reduction. The normalization −2b_εg is undifferentiated and smooth: it does not touch the principal symbol or the DeTurck gauge vector, so it enters only as a zeroth‑order term. Hence a unique smooth fixed‑ε solution on [0,T_ε) is well supported. This step is essentially Yang Approach 2 itself with a smooth lower‑order addition, and I find no defect.

## 2. The base curvature evolution is verifiable against the provided source

Step 45 (2.1),
∂_t T = bΔT + B₁∗∇T + B₂∗T + b(T∗T+T+1),
matches Yang's own curvature evolution in the provided paper §9:
∂Rm/∂t = χ²(ΔRm+Q(Rm,Rm)) + 2χa(∇χ,∇Rm) + b(∇χ,∇χ,Rm) + χc(∇²χ,Rm).
The correspondence is exact once one sets T = Rm+G and expands B₂ = ∇²(χ²) = 2(χ∇²χ + ∇χ⊗∇χ): Step 45's single B₂∗T term reproduces Yang's separate |∇χ|²Rm and χ∇²χRm terms, B₁∗∇T = 2χ∇χ∗∇Rm reproduces Yang's first‑derivative term, and bT∗T reproduces χ²Q(Rm,Rm). The added +g shift contributes only the displayed algebraic b(T+1) terms. So the ledger's starting equation is grounded in the source, not merely asserted. This is a real point of strength for the base of the induction.

By contrast, the cross‑references to "Wang … lines 414–423" and "Wang's Lemmas 4.4–4.6, Propositions 4.13–4.14" cannot be checked: the Pseudolocality paper is named but not included in the supplied files. Those citations concern only the coordinate‑time bookkeeping convention, which is a presentation choice; the mathematical content of (2.1) stands on the Yang §9 match above.

## 3. Absence of inverse powers of ε — verified

Every constant in (5.7)–(5.9), Step 44 (2.3)/(2.5), and Step 45 §6 uses only: 0<b_ε≤2; ∇^r b_ε = ∇^r a for r≥1; |∇b_ε|²/b_ε = |∇a|²/(χ²+ε²) = 4χ²|∇χ|²/(χ²+ε²) ≤ 4|∇χ|²; and χ²/b_ε ≤ 1. Each is ε‑independent, and I confirm the arithmetic of the middle identity directly. The weighted dissipation ∫b_ε|∇X|²|X|^{p−2} degenerates as b_ε→0, but it is only used as an absorbing (good) term — it is never inverted — so degeneracy introduces no ε^{−1}. This is genuinely the mechanism that makes the regularization uniform, and it holds.

## 4. Derivative propagation without loss — the χ² weighting does the work

Two structural features carry the induction, and both check out at the term level:

- Every quadratic curvature reaction carries a factor b, so a|T|^{p+1} = |U||T|^p ≤ K|T|^p. In Step 45 (4.1), families (T3)–(T4) give the current object T_m only with coefficient bT₀ = U₀, never an unweighted T₀. I verified this by the index count: T3 with r=0,i+j=m and T4 with r+s=m both force the extra factor to be bT₀ = U₀.
- The single place an unweighted T appears is (U3), B₁∗B₁∗T (eq 4.4). Here 4χ²(∇χ)²T_m = 4(χ²/b)(∇χ)²·(bT_m) = 4(χ²/b)(∇χ)²U_m with χ²/b ≤ 1, so the coefficient is bounded. Dropping the χ² would have produced the unavailable T₀ coefficient at the base stage; retaining it converts C₂∗T₀ into the bounded C₂∗U₀. This is the substantive repair over the earlier ledger, and it is correct.

The next‑order object (T_{m+1}, U_{m+1}) appears only multiplied by B₁ = ∇b (tables 4.2, 4.6), absorbed via |B₁|²/b ≤ 4|C₁|². The spatial commutator coefficient bRm = U − bG (eq 2.5) is bounded when U is bounded. Thus, granting the enumeration is complete, there is no genuine top‑order loss and no current‑exponent escalation; the staggered order T₀→(U₁,C₂)→T₁→… closes with Hölder pulling only finitely larger exponents of previously completed levels. The joint (U_m,C_{m+1}) energy in (5.7), coupled through the ∂_tC test‑term U_m∗C₁ in (1.6), is handled together — this coupling is necessary and is respected.

## 5. Bootstrap and first‑exit — non‑circular

The reaction bound uses |U_ε|≤K, which is the bootstrap hypothesis, not a conclusion; it is improved to |U_ε|<K₀ through ‖∂_tU_ε‖_{C⁰}≤C(g₀,χ,K), obtained from high‑order L^p bounds (m₀>n/2+4) and fixed‑background Sobolev. The improvement is the standard first‑exit continuation: with K=2K₀, ‖U_ε(0)‖≤K₀−1, and CT₀<½, one gets |U_ε(t)|≤(K₀−1)+CT₀<K₀ on [0,T₀]; the metric comparison improves via ‖∂_tg_ε‖_{C⁰}≤C_nK and C_nKT₀<½log2. Since C depends on K but not on interval length, T₀ is fixed. A fixed‑ε solution cannot have maximal time below T₀ without first exit, because the ε‑uniform (hence certainly ε‑fixed) derivative bounds allow fixed‑ε parabolic continuation. So T_ε ≥ T₀ for all ε, with no hidden ε‑dependence in the existence time. I find this logic complete, conditional on the ledger.

The zero‑order seed (Step 44 (2.13)) carries an additive C(K+1)Vol(g(t)) term; the note correctly reads this as sufficient for per‑datum finiteness but not homogeneous/sequence‑uniform. That distinction is respected and matters: the seed feeds the per‑datum theorem, not the downstream collapse‑uniform estimates.

## 6. ε→0 compactness and the one omitted step: gauge/diffeomorphism transport

The uniform space‑time C^∞ bounds justify a diagonal Arzelà–Ascoli limit, and b_{ε_j}→χ² smoothly gives ∂_tg = −2χ²(Ric+g); at χ=0 the equation forces ∂_tg=0 and the limit inherits this by smooth convergence, correctly not by an informal triviality statement. One point should be stated explicitly rather than compressed into "repeated time differentiation gives space‑time bounds of every order": the uniform estimates (2.5) control curvature‑type tensors ∇^m U_ε, ∇^m T_ε, which are diffeomorphism‑invariant. Passing from these to uniform bounds on the metric components g_ε (and to convergence of g_ε itself) requires a common gauge — the DeTurck gauge in which ĝ_ε is directly controlled, together with convergence of the diffeomorphism family φ_ε. Since ∂_tφ_ε = −b_ε[S^{−1}δG(S)]^♯ with b_ε≤2 and a metric‑derivative‑controlled generator, φ_ε does converge, and this is the standard Hamilton §14 argument that Yang invokes in §9.2. It is legitimate, but as written the note asserts C^∞ convergence of the geometric metric without recording the gauge in which curvature‑derivative bounds become metric‑derivative bounds. Making this explicit closes the only genuine hole in the ε→0 passage.

## 7. Positivity and jet‑matched restart — correct, and independent of uniqueness

Positivity of the limit follows from ½g₀≤g_ε≤2g₀ maintained on [0,T₀], so ½g₀≤g≤2g₀. The endpoint g(T₀) is smooth and positive‑definite from the uniform bounds up to T₀, enabling restart. The jet‑matching argument is correct: for the autonomous F(g)=−2χ²(Ric+g), a smooth solution converging to g_* has left jets ∂_t^j g(T_*^−)=F‑jets(g_*), the restarted right solution has the same F‑jets, so the concatenation is C^∞ and solves the equation across T_*. This constructs a specific smooth extension and does not require uniqueness. I confirm no circularity: the per‑datum theorem itself produces the smooth endpoint that the restart consumes.

## 8. Where uniqueness re‑enters

Approach 2 as used here does not supply uniqueness of the degenerate limit; distinct subsequences ε_j could a priori yield distinct limits, and the jet‑matched extension is "a" smooth continuation, not demonstrably "the" canonical one. Step 45 §7 anticipates the downstream need for "simultaneous first‑exit application on one common flow." Running the collapse/first‑exit estimates on a single canonical object plausibly requires uniqueness. That uniqueness is proved only in the sibling transported‑tame note (coupled (h,ψ) estimate, mean‑value identity), i.e. for Approach 1, not by the coefficient‑regularization construction. So the present route delivers existence + restart but imports uniqueness from elsewhere or leaves it open. This should be tracked, because the two routes share the feature that each has one compressed hard input — Yang's tame inverse for Approach 1, the ledger for Approach 2 — and they cross‑validate rather than either being self‑contained.

## 9. The remaining load‑bearing object

Both notes state, and I concur, that the single unproven item is the exhaustive index‑level expansion of [∇^m, b_εΔ], the coordinate‑time connection‑variation terms (1.3)–(1.5), the ∂_tC recursion (1.6), and every signed Hessian‑cutoff contraction, verifying that all fall into the enumerated families with the stated bounded (U‑weighted or χ²/b‑weighted) coefficients. Step 45 presents these families and the two extremal U3 allocations explicitly, but still writes coefficients schematically (stars "hide fixed numerical coefficients and slot permutations"). The base equation (2.1) is grounded in Yang §9 (§2 above), and the key extremal terms (4.4)–(4.5) are checked, but the assertion that no term escapes the families is by inspection of the recursion, not a written index‑level proof. Since the task instructs to assume the corrected ledger, everything downstream follows; the weight of that assumption is exactly this exhaustiveness.

## 10. What is precisely established for the restricted Ishida–LeBrun route

Assuming the ledger and adding the gauge bookkeeping of §6, the construction supplies, for a closed smooth manifold with fixed smooth (g₀,χ), 0≤χ≤1:

1. a common short‑time interval [0,T₀], T₀=T₀(g₀,χ)>0, independent of ε;
2. a smooth solution g on M×[0,T₀] of ∂_t g = −2χ²(Ric_g+g), g(0)=g₀, with ½g₀≤g≤2g₀, obtained as a C^∞ limit of the strictly parabolic ε‑flows, with all constants free of ε^{−1};
3. per‑datum finite‑exponent derivative propagation for T, U=χ²T, and cutoff jets on that interval;
4. a smooth positive‑definite endpoint and a C^∞ jet‑matched extension across it.

This is the analytic start/restart and derivative‑propagation interface for the restricted four‑dimensional negative Ishida–LeBrun smoothing route. It does not, and the notes do not assert that it does, produce a dimension‑only Ricci‑pinching theorem, settle the positive branch, cover general four‑manifold topology or n≥5, provide the sequence‑uniform observation time (that comes from separate weighted curvature/defect and first‑exit estimates), supply uniqueness of the degenerate flow, or provide any Lean formalization. It is one component, contingent on the ledger, not a solution of Yau 26.

## Items worth resolving to make the interface stand alone

- Write the index‑level expansion behind families T1–T6 / U1–U7 with numerical coefficients fixed, confirming closure and the bounded‑coefficient allocation for every commutator, connection‑variation, and Hessian‑cutoff term — this is the assumed object and the only genuinely open mathematics in the chain.
- State the gauge (DeTurck/harmonic) in which the ε‑uniform curvature‑derivative bounds become metric‑derivative bounds, and record convergence of φ_ε, so that "g_{ε_j}→g in C^∞" is fully supported.
- Fix whether the downstream first‑exit application needs one canonical degenerate flow; if so, connect this route to the coupled uniqueness proved for the transported system, since Approach 2 does not itself deliver it.
- Obtain the Wang paper to confirm the coordinate‑time bookkeeping cross‑references, or replace them with the Yang §9 formula already verified here.