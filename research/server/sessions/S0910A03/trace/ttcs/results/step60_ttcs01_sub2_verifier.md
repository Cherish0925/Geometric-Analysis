# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step59_finite_regularity_continuation_and_common_time.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md"
  ]
}
```

## Task

Audit the continuation mechanism for the exact degenerate geometric flow ∂_t g=-2χ²(Ric_g+g), focusing on the two disputed points. First, determine whether the coordinate-time derivative-family enumeration (T1–T6 and U1–U7) in step45, combined with the signed integrations and Step59/A01 Step55 residual estimate, genuinely exhausts every commutator and gives the arbitrary finite-order L^p induction for the exact case b=χ². Identify any missing current-level or unweighted coefficient, with an explicit derivative allocation if one exists. Second, assess uniqueness: is A01 Step56's proposed direct estimate d/dt∫|g1-g2|²≤C∫|g1-g2|² valid for the geometric Ricci-type equation without fixing diffeomorphism gauge? Account for diffeomorphism invariance and the actual principal symbol. If invalid, decide whether the all-order energy route can instead yield a smooth terminal metric and a direct smooth splice/restart without overlap uniqueness, and state the precise time-regularity/matching needed. Give a mathematical memo, not process advice.

## Output

# Memo: continuation mechanism for ∂ₜg = −2χ²(Ric_g + g) — enumeration completeness and the matching/uniqueness question

## Part 1 — Does the T1–T6 / U1–U7 enumeration plus signed integration close the arbitrary finite-order weighted Lᵖ induction for exact b = χ²?

**Verdict.** At the level of Leibniz + commutator bookkeeping the enumeration is coherent and I find no missing current-level term and no unweighted pointwise coefficient at top order. The two allocations that would break the induction are present and are converted by exact identities, not overlooked. The one thing that is genuinely not yet written is the term-by-term tensor-contraction verification; completeness currently rests on the schematic star-calculus, which the notes themselves record as unfinished.

**Structural equation is correct.** I reconstructed (2.3) from (2.1). Under ∂ₜg = −2S with S = Ric(U) = bE, the all-covariant Riemann variation is ∂ₜT = ∇²S + S∗Rm; with S = b·Ric(T), Bianchi commutation keeps the whole reaction weighted, giving ∂ₜT = bΔT + B₁∗∇T + B₂∗T + b(T∗T + T + 1). Multiplying by b and substituting Δ(bT) = bΔT + 2B₁∗∇T + (Δb)T and ∇U = b∇T + B₁∗T reproduces
∂ₜU = bΔU + B₁∗∇U + B₂∗U + (B₁∗B₁)∗T + U∗U + bU + b²,
including the sign combination −2B₁∇U + B₁∇U = −B₁∇U and +2(B₁B₁)T − (B₁B₁)T = +(B₁B₁)T. The single unweighted-T factor in the whole system sits in (B₁∗B₁)∗T = 4χ²(C₁∗C₁)T, and χ²T = U makes it a bounded-coefficient object. This is exact.

**The two load-bearing allocations.** These are the places an unweighted current coefficient would appear if the exact identities were dropped:

1. **U3 extremal r = s = 0, t = m:** B₁∗B₁∗T_m = 4χ²(C₁C₁)T_m. Naively this is an unweighted T_m at current order. Using χ²T_m: with bT_m = U_m − Σ_{q≥1}(∇^q b)T_{m−q}, equation (4.4) rewrites it as 4(χ²/b)(C₁C₁)[U_m − Σ(∇^q b)T_{m−q}]. Current coefficient of U_m is bounded (χ²/b ≤ 1, C₁ bounded); the correction pulls in only T_{m−1},…,T₀, already established. If the χ² were dropped to C₁C₁T_m, the base stage would demand T₀ ∈ L^∞, which the collar does not supply. The retained factor is exactly what saves it.

2. **Spatial commutator, r = m in the U-equation:** b∇^m Rm ∗ U₀ = bT_m∗U₀, again an unweighted current T_m. The same Leibniz identity converts bT_m∗U₀ = U_m∗U₀ − Σ(∇^q b)T_{m−q}∗U₀ — current U_m with bounded coefficient U₀ plus lower forcing (4.6).

I checked the remaining current entries in tables (4.2)/(4.6). Every top object appears with coefficient in {bounded (U₀, b≤2, bG, χ²/b·C₁C₁), degenerate-dissipation (B₁∗T_{m+1}, B₁∗U_{m+1} absorbed via |B₁|²/b ≤ 4|C₁|²), signed-Hessian (χC₂∗·, integrated by parts to ε∫b|∇·|²|·|^{p−2} + C‖dχ‖²_∞‖·‖ᵖ_p using χ² = b), or genuine Lᵖ forcing (products of separately-known factors)}. The top cutoff jets χC_{m+2}∗U₀ and 2χC_{m+2}∗T₀ are each integrated once; the χC_{m+2}∗T₀ case is the only one carrying an unweighted T₀, and it becomes forcing because T₀ ∈ ∩_q L^q from the independent signed-Hessian seed (Step 56 §1, eq. 1.1), not L^∞.

**The reordering remainders — the subtlest point.** Ricci commutation inside ∇^r(∂ₜΓ) and inside [∇^m,Δ] produces unweighted ∇^a Rm = T_a factors. I traced their maximal order. In the **spatial** commutator these carry the b weight (b∇^r Rm = bT_r = U_r − lower), so they are clean. In the **time** commutator U_{r+1}∗U_s (r+s = m−1) the reordering yields ∇^a Rm ∗ U_{b+1} ∗ U_s with a + b = r − 1, so a ≤ m − 2. The unweighted T_a therefore sits at level ≤ m − 2, is a previously-established unweighted level, and enters only as Lᵖ forcing (T_a ∈ ∩_q L^q). No current-order unweighted coefficient survives. This is the place where the argument leans hardest on the fact that the whole unweighted tower T₀,…,T_{m−1} lives in every finite exponent, which the staggered order T₀ → (U₁,C₂) → T₁ → (U₂,C₃) → … supplies without circularity (the U_m/C_{m+1} substep needs only T_{≤m−1}).

**The residual estimate is sound.** The counterterm χC_{m+1}∗U₁∗P(U_m) from integrating χC_{m+2}∗U by parts is controlled with f = χ|U_m|^{p/2}: |∇f|² ≤ 2|∇χ|²|U_m|^p + (p²/2)χ²|U_m|^{p−2}|∇U_m|², so ‖f‖₄² ≤ C_S(p²D^U_{m,p} + C‖U_m‖ᵖ_p) by four-dimensional Sobolev; Hölder (4,p,4,·) then Young with U₁ ∈ L⁴ (base pair) gives εD^U + C(1 + ‖C_{m+1}‖ᵖ_p + ‖U_m‖ᵖ_p). The current cutoff jet appears only at exponent p, so the induction is finite-triangular, not an exponent ascent. This genuinely uses n = 4 (2* = 4).

**What is not yet established.** Completeness of {T1–T6, U1–U7} is asserted from schematic Leibniz/commutator counting; the exhaustive tensor-contraction proof (every slot permutation, every commutator remainder with correct structural constant) is not written, and the allocation scripts (110/110; 14,002,305 partitions) test only integer derivative budgets and interpolation exponents, not tensor identities or the PDE. So the correct reading is: no missing current or unweighted coefficient is visible in the schematic system, and the weighted arbitrary-finite-order Lᵖ induction closes per-datum on a slab with |U| ≤ K and bilipschitz metrics **given** the T₀ seed and the exact identities; the remaining work is the tensor-level enumeration proof.

## Part 2 — The uniqueness estimate, the principal symbol, and a matching that needs no overlap uniqueness

**A01 Step 56 eq. (2.9) is not valid as written.** For h = g₁ − g₂ the note takes δRic(h) = −½Δ_L h + "lower order" and concludes d/dt∫|h|² ≤ −∫χ²|∇h|² + C∫|h|². The linearization is actually
DRic(h)_{ij} = −½Δ_L h_{ij} − ½∇_i∇_j(tr h) + ½(∇_i(δh)_j + ∇_j(δh)_i) + Rm∗h,
where (δh)_j = −∇^a h_{aj}. The terms ∇²(tr h) and ∇(δh) are **second order**, not lower order; they are exactly the pieces that make the linearized Ricci operator non-elliptic and force DeTurck's construction in ordinary Ricci flow. Testing χ²DRic(h) against h and integrating by parts, the gauge terms contribute ∫χ²(δh)(∇ tr h) and similar, which are of size ∫χ²|∇h|² with **indefinite sign and no smallness**. They are the same order as the dissipation −∫χ²|∇h|² and can cancel it. The symbol σ(DRic)(ξ) vanishes on Lie-derivative directions h = ∇_iX_j + ∇_jX_i, so there is no dissipation in gauge directions and a plain L² energy cannot close. The degenerate weight χ² makes matters worse on the collar, where any DeTurck-type gauge coupling is itself weight-degenerate. So (2.9) does not establish uniqueness of the geometric flow.

**But overlap uniqueness is not needed for continuation.** The equation ∂ₜg = F[g] := −2χ²(Ric_g + g) is autonomous and first order in time. This gives a splice that extends the maximal branch past T\* using only Part 1's all-order energy output, with no uniqueness statement:

Let g ∈ C^∞([0,T\*)×M) solve ∂ₜg = F[g], with g(t) → ḡ in C^∞(M) as t↑T\*, ḡ positive-definite. Because g solves the equation, ∂ₜ^k g(·,t) = F_k[g(·,t)], where F_k is the k-th total time-derivative of F along the flow — a fixed differential polynomial in the spatial jet of g and χ, with no explicit t. Continuity of F_k gives ∂ₜ^k g(·,t) → F_k[ḡ] in C^∞; the one-variable lemma (u ∈ C^1[0,T\*), u→u(T\*), u′→v ⟹ u ∈ C^1[0,T\*], u′(T\*)=v) applied at every order shows g ∈ C^∞([0,T\*]×M) and ∂ₜ^k g(T\*⁻) = F_k[ḡ].

Now take **any** restart h ∈ C^∞([T\*,T\*+τ]×M) with ∂ₜh = F[h] and h(T\*) = ḡ (the Step 56 per-datum construction supplies one; its lifespan is controlled by the uniformly bounded H^{s₀} radius of the ḡ family). Since h solves the same autonomous equation, ∂ₜ^k h(T\*⁺) = F_k[h(T\*)] = F_k[ḡ] = ∂ₜ^k g(T\*⁻) for every k. Hence the concatenation g̃ (= g on [0,T\*], = h on [T\*,T\*+τ]) is C^∞ in time at T\*, and ∂ₜg̃(T\*) = F[ḡ] = F[g̃(T\*)] one-sidedly from both directions. Therefore g̃ solves ∂ₜg̃ = F[g̃] on all of [0,T\*+τ], contradicting maximality of T\*.

**Why this is the right move.** All k-th derivatives match automatically because both sides are the *same* universal polynomial F_k evaluated at the *same* data ḡ. No assertion about h being unique is used; a non-unique restart splices just as well. This is precisely the property a first-order autonomous evolution enjoys and that the invalid L² argument was trying to obtain by the wrong route. It also fits the rest of the architecture, which already runs the first-exit bootstrap on a chosen maximal branch and never needs a canonical flow.

**Exact inputs the matching route requires (and where Part 1 is consumed):**
1. g(t) → ḡ in C^∞(M) — i.e. Cauchy in H^s for **every** s as t↑T\*. Step 56 §2.4–2.5 and Step 59 §4 give this rigorously only through the finite level s₀ = 7 (uniform H⁷ bound + Lipschitz-in-time in H⁵). The full C^∞ convergence, and hence the "all ∂ₜ^k match" statement, requires Part 1's induction at **every** m, integrated in time to ∂ₜg ∈ L¹_t H^s for all s. So the uniqueness-free splice literally depends on the arbitrary-order induction being complete, not merely the finite s₀ = 7 restart package.
2. ḡ positive-definite — from ∫‖U‖_∞ dt < ∞ on the slab, giving bilipschitz control (established).
3. A restart from ḡ — Step 56 §4–5 tame existence for smooth data (per-datum, plausible modulo the standard tame details it itself flags as not-yet-a-theorem).

If one instead insists on a finite-regularity splice, the same matching works with C^{s₀} in place of C^∞: the one-sided time-derivatives up to the order permitted by H^{s₀} match by the same F_k identity, and the concatenation solves the equation in H^{s₀−2}; positive-definiteness and the restart carry over. The C^∞ version is cleanest and is what the all-order induction targets.

**Net.** Part 1's schematic weighted Lᵖ tower has no visible missing coefficient and closes per-datum given the T₀ seed and exact identities, with the tensor-level enumeration still to be written. Part 2's L² uniqueness estimate misidentifies the second-order gauge terms and does not close; the continuation it was meant to support is better obtained by the autonomous-equation smooth splice, whose validity rests on C^∞ (or C^{s₀}) convergence to a positive-definite terminal metric — an all-order input drawn from Part 1 — and on existence of a restart, with the time-derivative matching being automatic and uniqueness-free.