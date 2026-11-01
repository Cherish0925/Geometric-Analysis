# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A03/workspace/notes/step44_arbitrary_order_tensor_ledger.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently check the corrected coordinate-time tensor ledger for the normalized coefficient flow. The active equations are ∂_t g=-2 Ric(U), T=Rm+g∧g/[2(n-1)], U=bT, b=χ²+ε². Read the new Step 45 note, the superseded Step 44 ledger, Wang's exact coordinate-time local Ricci-flow formulas, and the zero-order seed. Verify: (i) consistency of the ∂_t convention, ∂_t G, ∂_tΓ, [∂_t,∇^m], and cutoff-jet evolution; (ii) the base T and division-free U equations including all coefficient weights; (iii) the corrected differentiated family ∇^{r+1}b*∇^{s+1}b*T_t and its χ factors; (iv) exhaustive current-variable allocations, spatial/time commutators, and signed integrations; (v) whether the staggered finite-Lp estimates really close uniformly for b=χ²+ε² without hidden T∞, current-exponent escalation, ε^{-1}, or an omitted current derivative. Give explicit corrections to any formula or inference; do not infer correctness from schematic notation alone.

## Output

## Verification memo — coordinate-time tensor ledger for ∂ₜg = −2 Ric(U), U = bT, b = χ²+ε²

I read Step 45, the superseded Step 44 ledger and its zero-order seed, Step 40, and Wang's explicit coordinate-time formulas (the displayed ∂ₜR_{ijkl}, Lemmas 4.4–4.6, Props 4.13–4.14). Below I reconstruct the identities from scratch rather than trust the star-notation, then state where the argument holds and where substance is imported.

### A. Conventions and base identities — reconstructed and confirmed

**∂ₜb = 0, ∂ₜΓ, time commutator, cutoff-jet evolution.** With χ, ε fixed in space/time, ∂ₜb = 0 is correct. For ∂ₜg = −2S the standard variation gives (∂ₜΓ)ᵏ_{ij} = −gᵏˡ(∇ᵢS_{jl}+∇_jS_{il}−∇ₗS_{ij}), matching (1.4); since S = Ric(U) is a g⁻¹-trace of U and ∇g⁻¹ = 0, ∇ʳ(∂ₜΓ) = g⁻¹*U_{r+1} (1.5) is right. The coordinate-time commutator (1.3) and its consequence for C_{m+1},

  ∂ₜC_{m+1} = Σ_{r+s=m−1} U_{r+1}*C_{s+1},

is correct, and I confirm the top allocation is U_m*C_1 with no U_{m+1} and no C_{m+2}; the only jet reaching order m+1 on the right is the tested quantity itself, plus U₀-weighted metric/measure variation. This is the mechanism that keeps the cutoff hierarchy from escalating, and it holds.

**Base T equation (2.1).** Reconstructing ∂ₜRm from ∂ₜg = −2h, h = bE, E = Ric+g: the principal part is ∇²h. Leibniz gives b∇²E + 2∇b·∇E + ∇²b·E; via the second Bianchi identity b∇²E → b(ΔRm + Rm*Rm), and ΔRm = ΔT since ∇G = 0. Hence the diffusion coefficient is genuinely b (not χ²), 2∇b·∇E = B₁*∇T, ∇²b·E = B₂*T, and the reaction is b(T*T+T+1) with the shift producing the +T, +1 g-contractions. This reproduces Wang's displayed ∂ₜR_{ijkl} under a→b with the shift adding only lower algebraic terms, as stated. I confirm (2.1).

**Division-free U equation (2.3).** I carried out the multiplication by b explicitly using ∇U = b∇T + B₁*T and Δ(bT) = bΔT + 2B₁*∇T + (Δb)T. Collecting:

  ∂ₜU = bΔU − B₁*∇U + (B₂−Δb)*U + (B₁*B₁)*T + U*U + bU + b².

Up to the star's coefficients this is exactly (2.3), and the structurally decisive point survives: **the only unweighted T factor sits in (B₁*B₁)*T**. Since B₁ = 2χC₁, B₁*B₁ = 4χ²C₁*C₁, and χ²T = (χ²/b)·U with χ²/b ≤ 1, this term is a bounded-coefficient multiple of U at zeroth relative order. Correct and central.

### B. The two repairs relative to Step 44 — both genuine and correctly executed

1. **Coordinate ∂ₜ throughout.** Step 44 mixed a metric-compatible D_t with an explicit ∂ₜ(g∧g). Those are incompatible: D_tg = 0 cannot coexist with differentiating g∧g. Step 45's uniform use of coordinate ∂ₜ, with ∂ₜG algebraic in U through ∂ₜg, is the consistent choice and matches Wang's convention. The two conventions differ only by U*X algebraic terms already present, so the final families (4.1)–(4.3) are unchanged; the repair is about derivational consistency, and it is right.

2. **Retaining χ² in the (U3) family.** This is the substantive fix. Step 44 wrote (U3) as C_{α+1}*C_{β+1}*T_γ, dropping the χ factors. At the cutoff-jet extremal (α,β,γ)=(m,0,0) this produced C_{m+1}*C₁*T₀ with an **unweighted T₀**, which would demand T₀∈L^∞ — unavailable, since U = bT bounded permits T large where χ is small. Keeping B-notation, B_{m+1}*B₁*T₀ = 4χ²C_{m+1}C₁T₀ = 4(χ²/b)C_{m+1}C₁·U₀, a bounded-U₀ coupling (4.5). I verified the companion extremal (4.4): using bT_m = U_m − Σ_{q≥1}(m choose q)B_q T_{m−q}, the current-T_m allocation becomes 4(χ²/b)C₁C₁·U_m plus strictly lower T-levels. Both χ factors are essential and are correctly preserved. I also checked the exhaustiveness point that no C_{m+1}*U_j with j≥2 occurs: C_{m+1} pairs with T₀ (→U₀) in (U3) and with U₁ in (U2, r=m+1); r=m+2 yields C_{m+2}, not C_{m+1}. Confirmed.

### C. Finite-Lᵖ triangular induction and ε-uniformity

I checked the four control mechanisms and they are valid:

- **Gradient absorption.** ∫B₁*∇V*P(V) is bounded by δ∫b|∇V|²|V|^{p−2} + C(|B₁|²/b)‖V‖ₚᵖ, and |B₁|²/b = 4χ²|C₁|²/b ≤ 4|C₁|². No inverse power of ε enters; the b-weighted dissipation is only used through this bounded ratio.
- **Signed Hessian.** ∫(∇²b)𝓑(V), with db = 2χ dχ, is integrated once and closed by δ∫b|∇V|²|V|^{p−2} + C‖dχ‖_∞²‖V‖ₚᵖ. No pointwise ‖∇²χ‖_∞ is used. Correct.
- **Second integration by parts (5.5)/(2.6).** The term χC_{m+1}*U₁*P(V), which caused exponent escalation in the earlier attempt, is reduced by writing C_{m+1}=∇C_m and integrating once more to dχ*C_m*U₁, χC_m*U₂, χC_m*U₁*∇P(V), plus Ricci-commutation remainders T_q*C_s*U₁ (q≤m−1). For m≥3 every factor is a prior level; for m=2 the χC₂*U₂ = χC₂*V*P(V) piece is a further signed-Hessian contraction requiring the same one-derivative-off treatment (the note names it correctly but leaves that third integration implicit — worth writing out, since it is the m=2 endpoint of the reduction); for m=1 it is directly the signed Hessian. After this, the current unknowns V=U_m, Z=C_{m+1} appear only as |Z||V|^{p−1} and |Z|²|V|^{p−2}, i.e. at exponent p. Confirmed: no current-exponent escalation.
- **No hidden T_∞.** The T_m stage is treated after the pair is closed, so C_{m+1}, U_m are available at all finite exponents; the top time-commutator U_m*T₀ is an L^p forcing (both factors in every finite L^q via the zero-order seed), not a pointwise coefficient. The seed note's gain a|T|^{p+1} = |U||T|^p ≤ K|T|^p is the correct reason T₀∈L^q (all finite q) closes without T₀∈L^∞. Confirmed.

The uniformity in (6.1) rests only on 0<b≤2, ∇ʳb = ∇ʳ(χ²) for r≥1, |B₁|²/b ≤ 4|C₁|², χ²/b ≤ 1, and initial norms of U = bT and its derivatives, which are uniform in ε because b_ε ≤ 2 and ∇^i b_ε = ∇^i(χ²) for i≥1. So the finite-L^p bounds are uniform in ε on a common per-datum interval. I find no ε^{−1} anywhere.

**Net on the ledger's internal correctness:** the classification is exhaustive as reconstructed, the two repairs are real and correctly implemented, and the triangular finite-L^p induction closes uniformly in ε for the degenerate-in-the-limit coefficient b = χ²+ε², without T_∞, exponent escalation, ε^{−1}, or a missing current derivative.

### D. One explicit formula correction

Equation (1.2): ∂ₜ(g∧g) = (∂ₜg)∧g + g∧(∂ₜg) = −2(S∧g + g∧S), so

  ∂ₜG = −(S∧g + g∧S)/(n−1),   not  −(S∧g + g∧S)/[2(n−1)].

The note's version drops the factor 2 from ∂ₜg = −2S. (The convention (g∧g)_{ijkl}=2(g_{ik}g_{jl}−g_{il}g_{jk}) is the one forced by Ric(G)=g, so the factor is really missing.) This is a bounded coefficient hidden by the star in every downstream use, so it does not affect any structural conclusion — but as a written identity it should be corrected, and any place that reads ∂ₜG as an exact input (e.g. if later notes calibrate constants) inherits the factor.

### E. What is imported rather than derived here, stated as substance

The ledger is one analytic input, and the following are asserted/referenced, not established in these notes:

1. **Fixed-ε short-time existence.** For ε>0 the transported DeTurck system ∂ₜg_ε = −2b_ε(Ric+g) has principal symbol b_ε|ξ|² ≥ ε²|ξ|² > 0, so it is strictly parabolic and standard DeTurck short-time existence applies at each fixed ε. This supports Step 45 §6's statement that the compressed tame-inverse reconstruction is not needed for the ε-regularized existence. Note the tension with Step 44 (zero-order §4) and Step 40 (§5), which state the restart still needs a faithful adaptation of Yang's tame inverse: the two are reconcilable only if the ε→0 limit genuinely inherits both existence and the terminal-restart property from the fixed-ε problems. Reconciling these two notes explicitly would remove an apparent internal disagreement about whether the existence/restart question is closed.

2. **Uniform-in-ε existence interval.** §6 argues a common positive interval from uniform initial norms plus fixed-ε parabolic continuation. This is plausible but leans on the fixed-ε short-time theorem of item 1; the argument that no earlier maximal time occurs is standard only once that theorem is in hand.

3. **ε→0 limit to (6.3).** Uniform C^∞-in-space and ∂ₜg, ∂ₜΓ bounds on a common interval give an Arzelà–Ascoli/diagonal smooth limit solving ∂ₜg = −2χ²(Ric+g). Standard given the uniform bounds, but the identification of the limit as a solution of the degenerate equation and its restart are sketched, not written.

4. **The estimates are per-datum, not sequence-uniform.** The additive finite-volume term in the seed (2.13) and the K-dependent constants are explicitly not the collapse-uniform, homogeneous estimates the first-exit smoothing argument needs. This is stated in all three notes and is correct.

5. **Distance to Yau 26.** The static solution of the target flow is Ric = −g (λ = −1), so this addresses only the λ<0 four-dimensional Ishida–LeBrun smoothing route on restricted topology. Even a complete treatment of that route would not deliver a dimension-only pinching-implies-Einstein statement, the λ>0 case, arbitrary topology, dimensions n≥5, or the Lean formalization. The notes state this plainly.

### Suggested concrete items for the core agent

- Write out the m=2 third integration by parts for χC₂*U₂*P(U₂) explicitly (the endpoint of the (5.5) reduction), since it is the one place where the reduction terminates in a signed Hessian in the current variable rather than a prior level.
- Correct the ∂ₜG factor in (1.2) and check no later constant calibration used the halved value.
- Resolve the existence/restart statement between Step 45 §6 and Step 40 §5 / Step 44 §4 into a single account: exactly which short-time theorem is invoked at fixed ε, and precisely how the ε→0 limit inherits restart from a smooth positive-definite terminal metric.
- If sequence-uniform smoothing is the eventual target, note that the present per-datum constants (K-dependent, additive volume) are structurally different from the homogeneous estimates required, so this ledger does not yet feed that argument.